"""
Expressive TTS V3 — giọng đọc theo từng câu, có nhấn nhá & word timing thật
==========================================================================
- Đọc từng câu bằng Edge-TTS (vi-VN-NamMinhNeural) để tránh lỗi NoAudioReceived
  khi gửi đoạn dài; tự retry với backoff, cache theo hash câu (chạy lại không tốn thời gian).
- Fallback từng câu sang gTTS (+atempo) nếu Edge-TTS thất bại liên tục.
- Cắt khoảng lặng đầu/cuối mỗi câu rồi ghép lại với khoảng nghỉ có chủ đích theo dấu câu
  (".": 230ms, "!": 300ms, "?": 380ms, "...": 520ms, ":" 160ms) -> nhịp kể chuyện dứt khoát.
- Word timing lấy trực tiếp từ WordBoundary (Edge) -> đồng bộ chữ/hiệu ứng chính xác.
- Mastering: HPF 80Hz, ấm 160Hz +2.5dB, presence 3.2kHz +2dB, de-harsh 7kHz, compressor.

Usage:
    python src/audio/expressive_tts.py --text-file script.txt --out-dir projects/x/audio_v3 --id scene01
"""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import re
import subprocess
import sys
import time
from pathlib import Path

import numpy as np

SR = 48000
VOICE = "vi-VN-NamMinhNeural"
RATE = "+50%"

PAUSE_MS = {"...": 350, "…": 350, "?": 250, "!": 200, ".": 150, ":": 110, ";": 110}

MASTER_CHAIN = (
    "highpass=f=80,"
    "equalizer=f=160:width_type=o:w=1.0:g=2.5,"
    "equalizer=f=3200:width_type=o:w=1.2:g=2.0,"
    "equalizer=f=7000:width_type=o:w=1.0:g=-1.5,"
    "acompressor=threshold=-18dB:ratio=3:attack=5:release=80:makeup=2"
)


def split_sentences(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text.replace("\n", " ")).strip()
    parts = re.findall(r".+?(?:\.\.\.|…|[.!?:;]|$)(?=\s|$)", text)
    out = [p.strip() for p in parts if p.strip()]
    # Gộp mảnh quá ngắn (vd "Lửng Mật!") vào câu sau để giọng không bị cụt
    merged: list[str] = []
    for p in out:
        if merged and len(merged[-1].split()) <= 2 and not merged[-1].endswith(("?", "!", "...")):
            merged[-1] = merged[-1] + " " + p
        else:
            merged.append(p)
    return merged


def _decode(path: Path) -> np.ndarray:
    proc = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(path), "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"],
        capture_output=True, check=True)
    return np.frombuffer(proc.stdout, dtype=np.float32).copy()


def _trim_bounds(x: np.ndarray, thr_db: float = -42.0) -> tuple[int, int]:
    thr = 10 ** (thr_db / 20)
    win = int(0.01 * SR)
    if len(x) < win:
        return 0, len(x)
    env = np.sqrt(np.convolve(x * x, np.ones(win) / win, mode="same"))
    idx = np.where(env > thr)[0]
    if len(idx) == 0:
        return 0, len(x)
    margin = int(0.025 * SR)
    return max(0, idx[0] - margin), min(len(x), idx[-1] + margin)


async def _edge_sentence(sentence: str, mp3: Path, voice: str, rate: str) -> list[dict]:
    import edge_tts
    comm = edge_tts.Communicate(sentence, voice, rate=rate, boundary="WordBoundary")
    data = bytearray()
    words = []
    async for ch in comm.stream():
        if ch["type"] == "audio":
            data.extend(ch["data"])
        elif ch["type"] == "WordBoundary":
            s = ch["offset"] / 10000.0
            words.append({"word": ch["text"], "startMs": s, "endMs": s + ch["duration"] / 10000.0})
    if not data:
        raise RuntimeError("empty audio")
    mp3.write_bytes(bytes(data))
    return words


def _gtts_sentence(sentence: str, mp3: Path) -> list[dict]:
    from gtts import gTTS
    raw = mp3.with_suffix(".g.mp3")
    gTTS(text=sentence, lang="vi", tld="com.vn").save(str(raw))
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(raw), "-af", "atempo=1.22", str(mp3)], check=True)
    raw.unlink(missing_ok=True)
    x = _decode(mp3)
    a, b = _trim_bounds(x)
    toks = sentence.split()
    weights = [len(re.sub(r"\W", "", t)) + 2 for t in toks]
    tot = sum(weights)
    dur = (b - a) / SR * 1000
    cur = a / SR * 1000
    words = []
    for t, w in zip(toks, weights):
        d = dur * w / tot
        words.append({"word": re.sub(r"[^\w]", "", t), "startMs": cur, "endMs": cur + d * 0.85})
        cur += d
    return words


def synth_sentence(sentence: str, cache_dir: Path, voice: str = VOICE, rate: str = RATE,
                   max_retry: int = 30, allow_gtts: bool = False) -> tuple[np.ndarray, list[dict], str]:
    key = hashlib.md5(f"{voice}|{rate}|{sentence}".encode("utf-8")).hexdigest()[:16]
    mp3 = cache_dir / f"{key}.mp3"
    meta = cache_dir / f"{key}.json"
    if mp3.exists() and meta.exists():
        m = json.loads(meta.read_text(encoding="utf-8"))
        return _decode(mp3), m["words"], m["engine"]

    words, engine = None, "edge"
    for attempt in range(max_retry):
        try:
            words = asyncio.run(_edge_sentence(sentence, mp3, voice, rate))
            break
        except Exception:
            time.sleep(min(6.0, 1.0 + attempt * 0.8))
    if words is None:
        # Không trộn 2 giọng khác nhau trong cùng một video trừ khi được cho phép rõ ràng
        if not allow_gtts:
            raise RuntimeError(f"Edge-TTS failed {max_retry}x for: {sentence[:60]} (chạy lại để tiếp tục từ cache)")
        engine = "gtts"
        words = _gtts_sentence(sentence, mp3)
    meta.write_text(json.dumps({"sentence": sentence, "engine": engine, "words": words}, ensure_ascii=False),
                    encoding="utf-8")
    return _decode(mp3), words, engine


def pause_after(sentence: str) -> int:
    s = sentence.rstrip()
    for k in ("...", "…", "?", "!", ".", ":", ";"):
        if s.endswith(k):
            return PAUSE_MS[k]
    return 140


def build_narration(text: str, out_dir: Path, sid: str, voice: str = VOICE, rate: str = RATE,
                    lead_ms: int = 150, tail_ms: int = 450) -> dict:
    out_dir = Path(out_dir)
    cache = out_dir / "_cache"
    cache.mkdir(parents=True, exist_ok=True)
    sentences = split_sentences(text)
    chunks = [np.zeros(int(lead_ms * SR / 1000), np.float32)]
    cursor_ms = float(lead_ms)
    all_words, engines = [], []
    for i, sent in enumerate(sentences):
        x, words, eng = synth_sentence(sent, cache, voice, rate)
        engines.append(eng)
        a, b = _trim_bounds(x)
        seg = x[a:b]
        off = a / SR * 1000
        for w in words:
            all_words.append({
                "word": w["word"],
                "startMs": int(round(cursor_ms + max(0.0, w["startMs"] - off))),
                "endMs": int(round(cursor_ms + max(0.0, w["endMs"] - off))),
                "sentence": i,
            })
        chunks.append(seg)
        cursor_ms += len(seg) / SR * 1000
        gap = pause_after(sent) if i < len(sentences) - 1 else tail_ms
        chunks.append(np.zeros(int(gap * SR / 1000), np.float32))
        cursor_ms += gap
        print(f"  [{sid}] {i + 1}/{len(sentences)} {eng:5s} {len(seg) / SR:5.2f}s | {sent[:60]}", flush=True)

    audio = np.concatenate(chunks)
    raw_wav = out_dir / f"{sid}_dry.wav"
    _write_wav(raw_wav, audio)
    wav = out_dir / f"{sid}.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(raw_wav), "-af", MASTER_CHAIN,
                    "-ar", str(SR), "-ac", "2", "-c:a", "pcm_s16le", str(wav)], check=True)
    raw_wav.unlink(missing_ok=True)
    total_ms = int(round(len(audio) / SR * 1000))
    data = {"id": sid, "voice": voice, "rate": rate, "totalDurationMs": total_ms,
            "engines": {e: engines.count(e) for e in set(engines)},
            "sentences": sentences, "words": all_words}
    (out_dir / f"{sid}_words.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"[TTS] {sid}: {total_ms / 1000:.2f}s, {len(all_words)} words, engines={data['engines']}")
    return data


def _write_wav(path: Path, x: np.ndarray):
    from scipy.io import wavfile
    wavfile.write(str(path), SR, (np.clip(x, -1, 1) * 32767).astype(np.int16))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--text-file", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--id", required=True)
    ap.add_argument("--voice", default=VOICE)
    ap.add_argument("--rate", default=RATE)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    build_narration(Path(a.text_file).read_text(encoding="utf-8"), Path(a.out_dir), a.id, a.voice, a.rate)

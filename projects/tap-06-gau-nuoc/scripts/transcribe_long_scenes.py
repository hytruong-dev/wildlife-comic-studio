"""Word-level Whisper timestamps for the 6 long-form scene voice tracks (cached JSON)."""
import json
import sys
from pathlib import Path

import numpy as np
import soundfile as sf
from faster_whisper import WhisperModel

PROJ = Path(__file__).resolve().parents[1]
AUDIO = PROJ / "audio"
OUT = AUDIO / "long_words.json"
MODEL = sys.argv[1] if len(sys.argv) > 1 else "small"


def load_16k(p: Path) -> np.ndarray:
    data, sr = sf.read(str(p), dtype="float32")
    if data.ndim > 1:
        data = data.mean(axis=1)
    if sr != 16000:
        idx = np.arange(0, len(data), sr / 16000.0)
        data = np.interp(idx, np.arange(len(data)), data).astype(np.float32)
    return data


def main():
    model = WhisperModel(MODEL, device="cpu", compute_type="int8")
    result = {}
    for i in range(1, 7):
        sid = f"scene{i:02d}"
        segs, _ = model.transcribe(
            load_16k(AUDIO / f"{sid}.wav"), language="vi", word_timestamps=True,
            initial_prompt="Gấu Nước Tardigrade bất tử, âm 272 độ C, 150 độ C, Ma-ri-a-na, Gray, ốc sên, Mặt Trăng, Bê-rê-shít",
        )
        words = [{"w": w.word.strip(), "s": round(w.start, 2), "e": round(w.end, 2)} for s in segs for w in s.words]
        result[sid] = words
        print(f"\n== {sid}: {len(words)} words")
        for k in range(0, len(words), 14):
            ch = words[k:k + 14]
            print(f"[{ch[0]['s']:6.2f}-{ch[-1]['e']:6.2f}] " + " ".join(w["w"] for w in ch))
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
    print("saved", OUT)


if __name__ == "__main__":
    main()

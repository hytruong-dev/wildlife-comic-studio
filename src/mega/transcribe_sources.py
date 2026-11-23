"""Transcribe the published long-form MP4 of every source episode of a Mega Compilation.

Output: projects/<mega>/sources/<slug>.words.json  ({"file", "duration_s", "segments":[{s,e,text,words:[{w,s,e}]}]})
These word timestamps are what cut points (in/out) in mega.json are derived from.

Usage:
  python src/mega/transcribe_sources.py projects/mega-01-bang-phong-than [--only tap-07-tom-tit] [--model small]
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def duration(p: Path) -> float:
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                         capture_output=True, text=True, check=True).stdout
    return float(out.strip())


def main():
    proj = Path(sys.argv[1]).resolve()
    mega = json.loads((proj / "mega.json").read_text(encoding="utf-8"))
    only = sys.argv[sys.argv.index("--only") + 1] if "--only" in sys.argv else None
    model_name = sys.argv[sys.argv.index("--model") + 1] if "--model" in sys.argv else "small"
    out_dir = proj / "sources"
    out_dir.mkdir(exist_ok=True)
    wav_dir = out_dir / "_wav"
    wav_dir.mkdir(exist_ok=True)

    from faster_whisper import WhisperModel
    model = WhisperModel(model_name, device="cpu", compute_type="int8", cpu_threads=8)

    for src in mega["sources"]:
        slug = src["slug"]
        if only and slug != only:
            continue
        dst = out_dir / f"{slug}.words.json"
        if dst.exists() and "--force" not in sys.argv:
            print("skip (cached):", dst.name, flush=True)
            continue
        mp4 = ROOT / src["file"]
        wav = wav_dir / f"{slug}.wav"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(mp4), "-ac", "1", "-ar", "16000", str(wav)], check=True)
        import soundfile as sf  # pass an array: this PyAV build rejects faster-whisper's file decoder (metadata_errors)
        audio, _sr = sf.read(str(wav), dtype="float32")
        segs, _ = model.transcribe(audio, language="vi", word_timestamps=True, vad_filter=False, beam_size=5,
                                   initial_prompt=src.get("whisper_prompt", src["animal"]))
        data = {"file": src["file"], "duration_s": round(duration(mp4), 3), "segments": []}
        for s in segs:
            data["segments"].append({"s": round(s.start, 2), "e": round(s.end, 2), "text": s.text.strip(),
                                     "words": [{"w": w.word.strip(), "s": round(w.start, 2), "e": round(w.end, 2)} for w in (s.words or [])]})
        dst.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"{slug}: {len(data['segments'])} segments, {data['duration_s']}s -> {dst.name}", flush=True)
        wav.unlink(missing_ok=True)


if __name__ == "__main__":
    main()

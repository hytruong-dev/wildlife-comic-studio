"""Re-transcribe one time range of a source video (when the full-file pass skipped speech) and print it.

  python src/mega/probe_range.py <video.mp4> <start_s> <end_s> [--model small]
"""
import subprocess
import sys
import tempfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")


def main():
    src, a, b = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
    model_name = sys.argv[sys.argv.index("--model") + 1] if "--model" in sys.argv else "small"
    wav = Path(tempfile.gettempdir()) / "mega_probe.wav"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(a), "-to", str(b), "-i", src, "-ac", "1", "-ar", "16000", str(wav)],
                   check=True)
    import soundfile as sf
    from faster_whisper import WhisperModel
    audio, _ = sf.read(str(wav), dtype="float32")
    model = WhisperModel(model_name, device="cpu", compute_type="int8", cpu_threads=8)
    segs, _ = model.transcribe(audio, language="vi", word_timestamps=True, vad_filter=False)
    for s in segs:
        print(f"{a + s.start:7.2f}-{a + s.end:7.2f} | {s.text.strip()}")
        for w in s.words or []:
            print(f"      {a + w.start:7.2f} {w.word.strip()}")


if __name__ == "__main__":
    main()

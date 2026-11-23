import subprocess
import json
from pathlib import Path

AUDIO_DIR = Path("projects/tap-05-chim-bo-nong/audio")

# Generate 100ms gap
gap_wav = AUDIO_DIR / "shorts_gap_100ms.wav"
subprocess.run([
    "ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
    "-t", "0.10", "-c:a", "pcm_s16le", str(gap_wav)
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

lines = []
part_durs = {}
for i in range(6):
    w = AUDIO_DIR / f"shorts_fast_p{i}.wav"
    dur = float(subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(w)
    ], text=True).strip())
    part_durs[f"part{i}"] = round(dur, 3)
    lines.append(f"file '{w.resolve().as_posix()}'")
    if i < 5:
        lines.append(f"file '{gap_wav.resolve().as_posix()}'")

concat_txt = AUDIO_DIR / "shorts_concat.txt"
concat_txt.write_text("\n".join(lines), encoding="utf-8")

final_wav = AUDIO_DIR / "shorts.wav"
subprocess.run([
    "ffmpeg", "-y", "-f", "concat", "-safe", "0",
    "-i", str(concat_txt), "-c:a", "pcm_s16le", str(final_wav)
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

dur = float(subprocess.check_output([
    "ffprobe", "-v", "error", "-show_entries", "format=duration",
    "-of", "default=noprint_wrappers=1:nokey=1", str(final_wav)
], text=True).strip())
print(f"New shorts.wav duration: {dur:.3f}s")

dur_json = AUDIO_DIR / "shorts_parts_duration.json"
dur_json.write_text(json.dumps({
    "total_duration": round(dur, 3),
    "gap_sec": 0.10,
    "parts": part_durs
}, indent=2), encoding="utf-8")
print("Saved:", dur_json.name)

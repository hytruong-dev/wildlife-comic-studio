import subprocess
import json
from pathlib import Path

AUDIO_DIR = Path("projects/tap-05-chim-bo-nong/audio")

lead_wav = AUDIO_DIR / "gap_leadin.wav"
gap_wav = AUDIO_DIR / "gap_breathing.wav"

lines = [
    f"file '{lead_wav.resolve().as_posix()}'",
    f"file '{(AUDIO_DIR / 'scene01_part0.wav').resolve().as_posix()}'",
    f"file '{gap_wav.resolve().as_posix()}'",
    f"file '{(AUDIO_DIR / 'scene01_part1.wav').resolve().as_posix()}'",
    f"file '{gap_wav.resolve().as_posix()}'",
    f"file '{(AUDIO_DIR / 'scene01_part2.wav').resolve().as_posix()}'",
    f"file '{gap_wav.resolve().as_posix()}'",
    f"file '{(AUDIO_DIR / 'scene01_part3.wav').resolve().as_posix()}'"
]

concat_f = AUDIO_DIR / "scene01_master_concat.txt"
concat_f.write_text("\n".join(lines), encoding="utf-8")

out_wav = AUDIO_DIR / "scene01.wav"
subprocess.run([
    "ffmpeg", "-y", "-f", "concat", "-safe", "0",
    "-i", str(concat_f), "-c:a", "pcm_s16le", str(out_wav)
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(out_wav)]
total_dur = float(subprocess.check_output(cmd, text=True).strip())
print(f"New scene01.wav duration: {total_dur:.3f}s")

dur_json = AUDIO_DIR / "scene01_parts_duration.json"
data = {
    "total_duration": round(total_dur, 3),
    "lead_in_sec": 0.4,
    "gap_sec": 0.35,
    "parts": {
        "part0": 13.321,
        "part1": 17.116,
        "part2": 14.702,
        "part3": 9.300
    }
}
dur_json.write_text(json.dumps(data, indent=2), encoding="utf-8")
print("Updated scene01_parts_duration.json")

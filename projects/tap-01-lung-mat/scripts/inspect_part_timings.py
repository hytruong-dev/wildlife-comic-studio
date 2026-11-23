import subprocess
from pathlib import Path

AUDIO_DIR = Path("projects/tap-01-lung-mat/audio")

def get_dur(f: Path):
    cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(f)]
    return float(subprocess.check_output(cmd, text=True).strip())

for s in ["scene03", "scene04", "scene05", "scene06"]:
    parts = sorted(AUDIO_DIR.glob(f"{s}_eleven_p*.wav"))
    full_dur = get_dur(AUDIO_DIR / f"{s}.wav")
    print(f"\n{s} (Total: {full_dur:.2f}s):")
    cum = 0.0
    for p in parts:
        d = get_dur(p)
        print(f"  {p.name}: {d:.2f}s (Start: {cum:.2f}s -> End: {cum+d:.2f}s)")
        cum += d + 0.4 # with 400ms pause

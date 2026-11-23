"""
Audit exact narration paragraph timings across all 6 scenes of Episode 1.
"""
import subprocess
from pathlib import Path

PROJ = Path(__file__).resolve().parent.parent
AUDIO_DIR = PROJ / "audio"


def get_dur_s(p: Path) -> float:
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(p),
    ]
    return float(subprocess.check_output(cmd, text=True).strip())


if __name__ == "__main__":
    for i in range(1, 7):
        sid = f"scene{i:02d}"
        full_wav = AUDIO_DIR / f"{sid}.wav"
        full_s = get_dur_s(full_wav)
        print(f"=== {sid} (Total: {full_s:.2f}s / {int(round(full_s*1000))}ms) ===")
        for prefix in [f"{sid}_eleven_p", f"{sid}_part_"]:
            parts = sorted(AUDIO_DIR.glob(f"{prefix}*.wav"))
            if parts:
                cum = 0.0
                for p in parts:
                    d = get_dur_s(p)
                    print(f"  {p.name:28s}: {d:6.2f}s | {int(round(cum*1000)):6d}ms -> {int(round((cum+d)*1000)):6d}ms")
                    cum += d + 0.35
                break

import subprocess
from pathlib import Path

P = Path("projects/tap-07-tom-tit")
long_mp4 = P / "renders" / "tap-07-tom-tit_long.mp4"
audit_dir = P / "renders" / "audit_frames"
audit_dir.mkdir(parents=True, exist_ok=True)

# Timestamps where emotion tags previously leaked (0.5s into scene 1, scene 2, scene 3, scene 4)
# Note: Intro is ~12.2s, so scene 1 starts at 12.2s.
# Let's extract at 15s (Scene 1 intro), 35s (Mike Tyson/Càng búa), 95s (Scene 2 RPG), 200s (Cavitation), 290s (Mùa lột xác)
timestamps = [
    ("15.0", "audit_scene01_hook.jpg"),
    ("35.0", "audit_scene01_punch.jpg"),
    ("105.0", "audit_scene02_rpg.jpg"),
    ("195.0", "audit_scene03_cavitation.jpg"),
    ("295.0", "audit_scene04_molt.jpg")
]

for t, name in timestamps:
    out = audit_dir / name
    cmd = ["ffmpeg", "-y", "-ss", t, "-i", str(long_mp4), "-vframes", "1", "-q:v", "2", str(out)]
    subprocess.run(cmd, check=True, capture_output=True)
    print(f"Extracted {name} at {t}s")

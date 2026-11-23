import subprocess
from pathlib import Path

P = Path("projects/tap-07-tom-tit")
shorts_mp4 = P / "renders" / "tap-07-tom-tit_shorts.mp4"
out = P / "renders" / "audit_frames" / "audit_shorts_start.jpg"

cmd = ["ffmpeg", "-y", "-ss", "1.5", "-i", str(shorts_mp4), "-vframes", "1", "-q:v", "2", str(out)]
subprocess.run(cmd, check=True, capture_output=True)
print("Extracted audit_shorts_start.jpg")

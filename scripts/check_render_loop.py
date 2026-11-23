from pathlib import Path
import time

P = Path("projects/tap-07-tom-tit/renders/long_v2")
vid_files = list(P.glob("*_video.mp4"))
mkv_files = list(P.glob("scene*.mkv"))

print(f"MKV completed: {[f.name for f in mkv_files]}")
for v in vid_files:
    print(f"Currently rendering: {v.name} (size: {v.stat().st_size:,} bytes)")

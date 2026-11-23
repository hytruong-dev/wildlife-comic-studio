import time
from pathlib import Path

rdir = Path("projects/tap-07-tom-tit/renders/long_v2")
files = sorted(rdir.glob("*.*"))
print(f"Time: {time.strftime('%H:%M:%S')}")
for f in files:
    sz_mb = f.stat().st_size / (1024 * 1024)
    print(f"  {f.name:25s} -> {sz_mb:6.2f} MB")

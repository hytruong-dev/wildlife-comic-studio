from pathlib import Path
import time

renders = Path("projects/tap-07-tom-tit/renders")
for f in renders.glob("*.*"):
    print(f"File: {f.name} ({f.stat().st_size / 1024 / 1024:.2f} MB), modified {time.time() - f.stat().st_mtime:.1f}s ago")

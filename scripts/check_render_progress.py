from pathlib import Path

rdir = Path("projects/tap-07-tom-tit/renders/long_v2")
for f in rdir.glob("*.mkv"):
    print(f"Rendered: {f.name} ({f.stat().st_size / 1024 / 1024:.2f} MB)")

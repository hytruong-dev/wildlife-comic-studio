from pathlib import Path

rdir = Path("projects/tap-07-tom-tit/renders/long_v2")
if rdir.exists():
    for f in rdir.glob("*.mkv"):
        print("Removing old cached scene:", f.name)
        f.unlink()
print("Done cleaning old long_v2 scenes!")

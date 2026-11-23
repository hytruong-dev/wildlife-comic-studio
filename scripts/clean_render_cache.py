from pathlib import Path

P = Path("projects/tap-07-tom-tit/renders/long_v2")
for f in P.glob("*.mkv"):
    print(f"Deleting old render cache: {f.name}")
    f.unlink()

for f in P.glob("scene*.mp4"):
    print(f"Deleting old render cache: {f.name}")
    f.unlink()

print("Cleaned long_v2 cache!")

from PIL import Image
from pathlib import Path

P = Path("projects/tap-07-tom-tit/assets")
print("Long images:")
for f in sorted((P / "long").glob("*.png")):
    im = Image.open(f)
    print(f"  {f.name}: {im.size}")

print("\nShorts images:")
for f in sorted((P / "shorts").glob("*.png")):
    im = Image.open(f)
    print(f"  {f.name}: {im.size}")

"""Contact sheet of images: python scripts/contact_sheet.py out.jpg img1 img2 ..."""
import sys
from pathlib import Path
from PIL import Image, ImageDraw

out, files = sys.argv[1], sys.argv[2:]
TW, TH = 300, 420
cols = 5
rows = (len(files) + cols - 1) // cols
sheet = Image.new("RGB", (cols * TW, rows * TH), "white")
d = ImageDraw.Draw(sheet)
for i, f in enumerate(files):
    im = Image.open(f).convert("RGB")
    im.thumbnail((TW - 10, TH - 40))
    x, y = (i % cols) * TW, (i // cols) * TH
    sheet.paste(im, (x + 5, y + 30))
    d.text((x + 8, y + 8), Path(f).stem, fill="red")
sheet.save(out, quality=85)
print(out)

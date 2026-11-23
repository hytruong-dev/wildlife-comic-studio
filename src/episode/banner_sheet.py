"""Bảng xem nhanh banner chương + banner Shorts (kiểm tra chính tả tiếng Việt do Gemini vẽ).

  python src/episode/banner_sheet.py projects/<slug>   -> renders/snapshots/banners.jpg
"""
import sys
from pathlib import Path

from PIL import Image

P = Path(sys.argv[1]).resolve()
B = P / "assets" / "banners"
files = sorted(B.glob("chapter_*.png")) + ([B / "shorts_title.png"] if (B / "shorts_title.png").exists() else [])
if not files:
    raise SystemExit(f"no banners in {B}")
W = 1000
ims = [Image.open(f).convert("RGBA") for f in files]
ims = [im.resize((W, max(1, int(im.height * W / im.width)))) for im in ims]
sheet = Image.new("RGB", (W, sum(im.height + 10 for im in ims)), (200, 200, 200))
y = 0
for im in ims:
    sheet.paste(im, (0, y), im)
    y += im.height + 10
out = P / "renders" / "snapshots" / "banners.jpg"
out.parent.mkdir(parents=True, exist_ok=True)
sheet.save(out, quality=88)
print(out)

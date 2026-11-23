"""Contact sheet of all long-form illustrations with a 10% grid, so targets can be read off precisely."""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

P = Path("projects/tap-07-tom-tit/assets/long")
out = Path("projects/tap-07-tom-tit/renders/audit_frames")
out.mkdir(parents=True, exist_ok=True)
files = sorted(P.glob("L*.png"))
names = sys.argv[1:] or [f.stem for f in files]
font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 28)
small = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 14)
W, H = 800, 447
per = 4
for page in range(0, len(names), per):
    sheet = Image.new("RGB", (W * 2, H * 2), "white")
    for k, n in enumerate(names[page:page + per]):
        im = Image.open(P / f"{n}.png").convert("RGB").resize((W, H))
        d = ImageDraw.Draw(im)
        for i in range(1, 10):
            x, y = W * i // 10, H * i // 10
            d.line([(x, 0), (x, H)], fill=(255, 0, 255), width=1)
            d.line([(0, y), (W, y)], fill=(255, 0, 255), width=1)
            d.text((x + 2, 2), f".{i}", fill=(255, 0, 255), font=small)
            d.text((2, y + 2), f".{i}", fill=(255, 0, 255), font=small)
        d.rectangle([0, H - 40, 110, H], fill="black")
        d.text((8, H - 36), n, fill="yellow", font=font)
        sheet.paste(im, ((k % 2) * W, (k // 2) * H))
    dst = out / f"sheet_{names[page]}_{names[min(page + per, len(names)) - 1]}.jpg"
    sheet.save(dst, quality=85)
    print(dst)

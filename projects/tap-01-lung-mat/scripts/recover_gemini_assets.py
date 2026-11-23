import json
import base64
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

candidates = [
    Path("projects/tap-01-lung-mat/assets/gemini_downloaded/tmp_all_37.json"),
    Path(r"C:\Users\PC\projects\tap-01-lung-mat\assets\gemini_downloaded\tmp_all_37.json"),
]
p = next((c for c in candidates if c.exists()), None)
print("Found:", p)
raw = p.read_text(encoding="utf-8").strip()
if raw.startswith('"'):
    raw = json.loads(raw)
data = json.loads(raw) if isinstance(raw, str) else raw

out_dir = Path("projects/tap-01-lung-mat/renders/qa_audit/all_gemini_37")
out_dir.mkdir(parents=True, exist_ok=True)
items = []
for k, b64 in sorted(data.items()):
    out_p = out_dir / f"{k}.png"
    out_p.write_bytes(base64.b64decode(b64))
    items.append((k, out_p))
print(f"Decoded {len(items)} images to {out_dir}")
p.unlink()

# Build contact sheets (20 images per sheet, 4x5 grid)
for sheet_idx in range(0, len(items), 20):
    batch = items[sheet_idx:sheet_idx + 20]
    cols = 4
    rows = (len(batch) + cols - 1) // cols
    tw, th = 360, 210
    sheet = Image.new("RGB", (cols * tw, rows * (th + 28)), (245, 245, 245))
    draw = ImageDraw.Draw(sheet)
    for i, (k, img_p) in enumerate(batch):
        r = i // cols
        c = i % cols
        im = Image.open(img_p).convert("RGB")
        im.thumbnail((tw - 10, th - 10))
        x0 = c * tw + (tw - im.size[0]) // 2
        y0 = r * (th + 28) + 24 + (th - im.size[1]) // 2
        sheet.paste(im, (x0, y0))
        draw.text((c * tw + 8, r * (th + 28) + 4), f"{k} ({im.size[0]}x{im.size[1]})", fill=(20, 20, 20))
    sheet_path = out_dir / f"sheet_{sheet_idx // 20 + 1}.png"
    sheet.save(sheet_path)
    print("Saved sheet:", sheet_path)

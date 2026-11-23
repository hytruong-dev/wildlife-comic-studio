"""
Build High-CTR 1280x720 YouTube Thumbnail for Episode 2: Rái Cá Biển (`tap-02-rai-ca-bien`)
Follows the channel thumbnail design standard:
- 2D Comic Whiteboard Illustration of Sea Otter unmasking Cute Plushie disguise into Ocean Thug
- Vibrant yellow/gold border & top badges (`TẬP 02`, `TRICKERY: 999 ĐIỂM!`)
- Ultra-bold 3-word Hook Banner: `CÚ LỪA ĐẠI DƯƠNG!`
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[3]
PROJ = Path(__file__).resolve().parents[1]
FONT_DIR = ROOT / "assets" / "fonts"
OUT_PATH = PROJ / "renders" / "tap02_rai_ca_bien_thumbnail.png"

W, H = 1280, 720
canvas = Image.new("RGBA", (W, H), (255, 252, 240, 255))

# Load main Sea Otter Myth-Busted artwork + Kidnap/Ransom corner badge
hero_path = PROJ / "assets" / "gemini_downloaded" / "c1_otter_myth_busted_thug_mask.png"
hero_img = Image.open(hero_path).convert("RGBA")

scale = max(W / hero_img.width, (H - 80) / hero_img.height) * 0.94
nw = int(hero_img.width * scale)
nh = int(hero_img.height * scale)
hero_resized = hero_img.resize((nw, nh), Image.Resampling.LANCZOS)

hx = (W - nw) // 2
hy = 8
canvas.paste(hero_resized, (hx, hy), hero_resized)

overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)

# Outer high-contrast comic frame
draw.rectangle([0, 0, W - 1, H - 1], outline=(220, 38, 38, 255), width=14)
draw.rectangle([14, 14, W - 15, H - 15], outline=(250, 204, 21, 255), width=6)

font_huge = ImageFont.truetype(str(FONT_DIR / "BeVietnamPro-Bold.ttf"), 84)
font_sub = ImageFont.truetype(str(FONT_DIR / "BeVietnamPro-Bold.ttf"), 42)
font_badge = ImageFont.truetype(str(FONT_DIR / "BeVietnamPro-Bold.ttf"), 34)


def draw_stroked_text(draw_obj, pos, text, font, fill, stroke_fill=(0, 0, 0, 255), stroke_width=8):
    x, y = pos
    draw_obj.text(
        (x, y),
        text,
        font=font,
        fill=fill,
        stroke_width=stroke_width,
        stroke_fill=stroke_fill,
        anchor="mm",
    )


# Top-left Episode Badge
draw.rounded_rectangle([32, 28, 275, 98], radius=18, fill=(13, 148, 136, 245), outline=(255, 255, 255, 255), width=4)
draw_stroked_text(draw, (153, 63), "TẬP 02", font_badge, (255, 255, 255, 255), stroke_width=4)

# Top-right RPG Stat Badge
draw.rounded_rectangle([830, 28, 1248, 98], radius=18, fill=(220, 38, 38, 245), outline=(250, 204, 21, 255), width=4)
draw_stroked_text(draw, (1039, 63), "ĐỘ LẦY LỘI: 999!", font_badge, (250, 204, 21, 255), stroke_width=5)

# Bottom High-Contrast Banner
draw.rectangle([14, 520, W - 14, H - 14], fill=(15, 23, 42, 235))
draw.line([(14, 520), (W - 14, 520)], fill=(250, 204, 21, 255), width=6)

# Main Hook Text
draw_stroked_text(
    draw,
    (W // 2, 588),
    "CÚ LỪA ĐẠI DƯƠNG!",
    font_huge,
    (250, 204, 21, 255),
    stroke_fill=(0, 0, 0, 255),
    stroke_width=10,
)

# Subtitle Hook Text
draw_stroked_text(
    draw,
    (W // 2, 666),
    "TÚI DORAEMON & BẮT CON TIN ĐÒI CUA!",
    font_sub,
    (255, 255, 255, 255),
    stroke_fill=(220, 38, 38, 255),
    stroke_width=6,
)

final_rgb = Image.alpha_composite(canvas, overlay).convert("RGB")
final_rgb.save(OUT_PATH, quality=95)
print(f"[THUMBNAIL EP02 READY] Saved to {OUT_PATH} ({W}x{H})")

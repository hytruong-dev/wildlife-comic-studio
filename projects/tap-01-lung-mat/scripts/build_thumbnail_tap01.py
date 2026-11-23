"""
Build High-CTR 1280x720 YouTube Thumbnail for Episode 1: Lửng Mật (`tap-01-lung-mat`)
Follows `SamurAIGPT/open-ai-youtube-agent` & `Open-Tube-SEO` High-CTR Thumbnail rules:
  - 1280x720 (16:9 HD), < 2MB PNG/JPG
  - High-contrast comic-whiteboard aesthetic with bold 3-5 word hook ("CHẤP 3 SƯ TỬ!", "12KG BẤT TỬ!")
  - Visual confrontation + RPG Stat Badge (`FEAR: 0 / DEF: 99`)
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parents[3]
PROJ = Path(__file__).resolve().parents[1]
G = PROJ / "assets" / "gemini_downloaded"
RENDERS = PROJ / "renders"


def load_bold_font(size: int) -> ImageFont.FreeTypeFont:
    candidates = [
        r"C:\Windows\Fonts\arialbd.ttf",
        r"C:\Windows\Fonts\impact.ttf",
        r"C:\Windows\Fonts\segoeuib.ttf",
        r"C:\Windows\Fonts\tahomabd.ttf",
    ]
    for c in candidates:
        if Path(c).exists():
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()


def draw_stroked_text(
    draw: ImageDraw.Draw,
    pos: tuple[int, int],
    text: str,
    font: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
    stroke_fill: tuple[int, int, int] = (15, 18, 24),
    stroke_width: int = 8,
):
    draw.text(pos, text, font=font, fill=fill, stroke_width=stroke_width, stroke_fill=stroke_fill)


def build_thumbnail() -> Path:
    W, H = 1280, 720
    canvas = Image.new("RGBA", (W, H), (255, 255, 255, 255))
    draw = ImageDraw.Draw(canvas)

    # 1. Dynamic warm editorial border & subtle diagonal energy accent on top-left
    draw.polygon([(0, 0), (540, 0), (440, 145), (0, 145)], fill=(214, 40, 40, 255))
    draw.polygon([(0, 145), (440, 145), (425, 160), (0, 160)], fill=(247, 127, 0, 255))

    # 2. Main Hero Artwork: Honey Badger vs 3 Male Lions (`c5_badger_vs_3_lions.png`)
    hero_path = G / "c5_badger_vs_3_lions.png"
    hero = Image.open(hero_path).convert("RGBA")
    hw, hh = hero.size
    scale = min(980 / hw, 560 / hh)
    nhw, nhh = int(hw * scale), int(hh * scale)
    hero_resized = hero.resize((nhw, nhh), Image.Resampling.LANCZOS)
    canvas.paste(hero_resized, (W - nhw - 10, H - nhh - 8), hero_resized)

    # 3. Secondary Inset Badge: RPG STR 85 / FEAR 0 stat card on bottom-left
    stat_path = G / "c2_badger_fear_zero.png"
    if stat_path.exists():
        stat_img = Image.open(stat_path).convert("RGBA")
        sw, sh = stat_img.size
        s_scale = min(430 / sw, 260 / sh)
        nsw, nsh = int(sw * s_scale), int(sh * s_scale)
        stat_resized = stat_img.resize((nsw, nsh), Image.Resampling.LANCZOS)
        # Draw white card backing with dark comic border
        bx0, by0 = 24, H - nsh - 26
        bx1, by1 = bx0 + nsw + 16, by0 + nsh + 16
        draw.rounded_rectangle([bx0 - 4, by0 - 4, bx1 + 4, by1 + 4], radius=18, fill=(20, 24, 30, 255))
        draw.rounded_rectangle([bx0, by0, bx1, by1], radius=15, fill=(255, 255, 255, 255))
        canvas.paste(stat_resized, (bx0 + 8, by0 + 8), stat_resized)

    # 4. High-CTR Typography Overlays
    font_top = load_bold_font(56)
    font_main = load_bold_font(84)
    font_pill = load_bold_font(38)

    # Top-left Red Ribbon Text: "KẺ CHÍ PHÈO 12KG"
    draw_stroked_text(draw, (28, 34), "KẺ CHÍ PHÈO 12KG", font_top, fill=(255, 242, 75), stroke_width=7)

    # Main Hook Text: "CHẤP 3 SƯ TỬ!"
    draw_stroked_text(draw, (30, 178), "CHẤP 3 SƯ TỬ!", font_main, fill=(220, 28, 28), stroke_width=10)

    # RPG Stat Pill on Top Right: "SỢ HÃI: 0/100 | GIÁP: 99"
    pill_box = [690, 24, 1252, 98]
    draw.rounded_rectangle([pill_box[0] - 4, pill_box[1] - 4, pill_box[2] + 4, pill_box[3] + 4], radius=36, fill=(18, 22, 28, 255))
    draw.rounded_rectangle(pill_box, radius=34, fill=(255, 230, 40, 255))
    draw_stroked_text(draw, (722, 38), "FEAR: 0/100  |  DEF: 99", font_pill, fill=(20, 24, 30), stroke_fill=(255, 255, 255), stroke_width=3)

    # Outer crisp frame
    draw.rectangle([0, 0, W - 1, H - 1], outline=(20, 24, 30, 255), width=8)

    out_png = RENDERS / "tap01_lung_mat_thumbnail.png"
    out_jpg = RENDERS / "tap01_lung_mat_thumbnail.jpg"
    rgb = canvas.convert("RGB")
    rgb.save(out_png, quality=95)
    rgb.save(out_jpg, quality=92)
    print(f"[THUMBNAIL BUILT] {out_png} ({out_png.stat().st_size / 1024:.1f} KB)")
    return out_png


if __name__ == "__main__":
    build_thumbnail()

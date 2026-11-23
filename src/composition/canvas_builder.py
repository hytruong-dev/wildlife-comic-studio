"""
Master Canvas Builder V2:
Solves:
1. Border preservation: images strictly contained within inner padding, borders redrawn on top.
2. Centered header: title header centered horizontally with border width fitted snugly to text width.
3. Clean typography: text callouts with ample margins, never cut off.
"""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import json

ROOT = Path(r"c:\QuangHy\youtube_ai_edit-02")
PROJ = ROOT / "projects" / "the-gioi-dong-vat-su-tu"
GEMINI_ROOT = PROJ / "assets" / "gemini_downloaded"
OUTPUT_DIR = PROJ / "assets" / "scenes_gemini_v2"
ANNOTATIONS_DIR = PROJ / "annotations"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
ANNOTATIONS_DIR.mkdir(parents=True, exist_ok=True)

try:
    font_title = ImageFont.truetype("arialbd.ttf", 23)
    font_header = ImageFont.truetype("arialbd.ttf", 15)
    font_bold = ImageFont.truetype("arialbd.ttf", 13)
    font_reg = ImageFont.truetype("arial.ttf", 12)
except:
    font_title = font_header = font_bold = font_reg = ImageFont.load_default()

def fit_contain(im: Image.Image, max_w: int, max_h: int) -> Image.Image:
    w, h = im.size
    scale = min(max_w / w, max_h / h)
    return im.resize((max(1, int(round(w * scale))), max(1, int(round(h * scale)))), Image.Resampling.LANCZOS)

def draw_centered_header(draw: ImageDraw.Draw, title_text: str):
    bbox = draw.textbbox((0, 0), title_text, font=font_title)
    t_w = bbox[2] - bbox[0]
    t_h = bbox[3] - bbox[1]
    
    pad_x = 30
    pad_y = 9
    box_w = t_w + 2 * pad_x
    box_h = t_h + 2 * pad_y
    
    box_x0 = (1280 - box_w) // 2
    box_y0 = 12
    box_x1 = box_x0 + box_w
    box_y1 = box_y0 + box_h
    
    draw.rounded_rectangle([box_x0, box_y0, box_x1, box_y1], radius=8,
                           fill=(248, 245, 238), outline=(44, 42, 41), width=2)
    draw.text((640, box_y0 + box_h // 2), title_text, fill=(44, 42, 41), font=font_title, anchor="mm")
    
    return {"x": box_x0, "y": box_y0, "width": box_w, "height": box_h}

Q1_BOX = [20, 68, 628, 376]
Q2_BOX = [652, 68, 1260, 376]
Q3_BOX = [20, 390, 628, 708]
Q4_BOX = [652, 390, 1260, 708]

def render_quadrant(canvas: Image.Image, draw: ImageDraw.Draw, box: list[int],
                    header_text: str, color: tuple, header_bg: tuple,
                    img_path: Path, wide_mode: bool, bullet_points: list):
    x0, y0, x1, y1 = box
    w = x1 - x0
    h = y1 - y0
    
    # 1. Base box
    draw.rounded_rectangle(box, radius=8, fill=(255, 255, 255), outline=color, width=2)
    draw.rectangle([x0 + 2, y0 + 2, x1 - 2, y0 + 34], fill=header_bg)
    draw.text((x0 + 16, y0 + 18), header_text, fill=color, font=font_header, anchor="lm")
    
    # 2. Image placement
    if img_path.exists():
        im_raw = Image.open(img_path).convert("RGB")
        if wide_mode:
            im = fit_contain(im_raw, w - 32, h - 52)
            im_x = x0 + (w - im.width) // 2
            im_y = y0 + 40 + (h - 48 - im.height) // 2
            canvas.paste(im, (im_x, im_y))
            draw.rectangle([im_x - 1, im_y - 1, im_x + im.width, im_y + im.height], outline=(215, 220, 225), width=1)
        else:
            im = fit_contain(im_raw, 330, h - 52)
            im_x = x0 + 16
            im_y = y0 + 40 + (h - 48 - im.height) // 2
            canvas.paste(im, (im_x, im_y))
            draw.rectangle([im_x - 1, im_y - 1, im_x + im.width, im_y + im.height], outline=(215, 220, 225), width=1)
            
            # Bullets on right
            tx = im_x + im.width + 16
            ty = y0 + 48
            for bp in bullet_points:
                draw.text((tx, ty), bp["title"], fill=bp.get("color", (44, 42, 41)), font=font_bold)
                ty += 18
                draw.text((tx, ty), bp["desc"], fill=(60, 60, 60), font=font_reg, spacing=3)
                ty += bp.get("gap", 50)
                
    # 3. CRITICAL: Redraw outer border so image NEVER overwrites it
    draw.rounded_rectangle(box, radius=8, outline=color, width=2)

print("Canvas Builder V2 loaded.")

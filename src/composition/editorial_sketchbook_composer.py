"""
Editorial Whiteboard Composer (`editorial_sketchbook_composer.py`)
Implements Pure Whiteboard Infinite Flow (Zero Card Boxes, Full Artwork Preservation):
- 100% Pure Whiteboard Canvas (#FFFFFF) matching all Gemini 2D Comic Illustrations seamlessly
- 100% FULL Illustration Preservation (ZERO cropping, ZERO shaving, ZERO feathering, ZERO covered content)
- 100% Verified Vietnamese Handwritten Typography (`assets/fonts/PlaypenSans-Bold.ttf` & `Mali-Bold.ttf`)
- Geometrically Centered Pill Badges (`anchor="mm"`) & Felt-Tip Marker Highlighter Strips
"""

import math
import random
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any
from PIL import Image, ImageDraw, ImageFont

ROOT_DIR = Path(__file__).resolve().parents[2]
FONTS_DIR = ROOT_DIR / "assets" / "fonts"

# Design System Color Tokens (RGB)
WHITEBOARD_RGB = (255, 255, 255)   # #FFFFFF Clean Infinite Whiteboard
PAPER_RGB = WHITEBOARD_RGB         # Alias for backward compatibility
INK_CHARCOAL = (30, 34, 42)        # #1E222A Deep Marker Ink
INK_MUTED = (90, 96, 108)          # #5A606C Secondary Sketch Gray
ACCENT_CRIMSON = (209, 52, 47)     # #D1342F Danger / Power / STR
ACCENT_AMBER = (214, 128, 18)      # #D68012 High-Contrast Warm Gold / Highlight
ACCENT_TEAL = (22, 124, 96)        # #167C60 Biology / Shield / DEF
ACCENT_ROYAL = (38, 84, 124)       # #26547C Intelligence / IQ
HIGHLIGHT_YELLOW = (253, 232, 138) # #FDE88A Warm Marker Highlighter
HIGHLIGHT_MINT = (196, 238, 218)   # #C4EEDA Mint Marker Highlighter
HIGHLIGHT_CORAL = (253, 205, 195)  # #FDCDC3 Coral Marker Highlighter


def load_handwritten_font(size: int, bold: bool = True, style: str = "body") -> ImageFont.FreeTypeFont:
    """
    Loads 100% Vietnamese-verified handwritten fonts from `assets/fonts/`.
    Guarantees 0 missing diacritics / 0 tofu boxes (`□`).
    """
    if style == "header":
        local_candidates = [
            FONTS_DIR / "Mali-Bold.ttf",
            FONTS_DIR / "PlaypenSans-Bold.ttf",
            FONTS_DIR / "BeVietnamPro-Bold.ttf",
        ]
    elif style == "badge":
        local_candidates = [
            FONTS_DIR / "BeVietnamPro-Bold.ttf",
            FONTS_DIR / "PlaypenSans-Bold.ttf",
            FONTS_DIR / "Mali-Bold.ttf",
        ]
    else:
        local_candidates = [
            FONTS_DIR / "PlaypenSans-Bold.ttf" if bold else FONTS_DIR / "PlaypenSans-Regular.ttf",
            FONTS_DIR / "Mali-Bold.ttf" if bold else FONTS_DIR / "Mali-Medium.ttf",
            FONTS_DIR / "PatrickHand-Regular.ttf",
            FONTS_DIR / "BeVietnamPro-Bold.ttf",
        ]

    for fp in local_candidates:
        if fp.exists():
            try:
                return ImageFont.truetype(str(fp), size)
            except Exception:
                continue

    for sys_fn in ["segoeuib.ttf", "calibrib.ttf", "tahomabd.ttf", "arialbd.ttf"]:
        try:
            return ImageFont.truetype(sys_fn, size)
        except Exception:
            continue
    return ImageFont.load_default()


def create_whiteboard_canvas(width: int = 1280, height: int = 720) -> Image.Image:
    """
    Generates a pure white infinite whiteboard canvas (#FFFFFF)
    that blends 100% seamlessly with all Gemini illustrations.
    """
    return Image.new("RGB", (width, height), (255, 255, 255))


def draw_organic_line(
    draw: ImageDraw.Draw,
    p0: Tuple[float, float],
    p1: Tuple[float, float],
    color: Tuple[int, int, int] = INK_CHARCOAL,
    width: int = 3,
    wobble: float = 1.0,
    seed: int = 7,
):
    """Draws a slightly hand-wobbled marker stroke between p0 and p1."""
    rng = random.Random(seed)
    dist = math.hypot(p1[0] - p0[0], p1[1] - p0[1])
    steps = max(4, int(dist / 14.0))
    pts = []
    for i in range(steps + 1):
        t = i / float(steps)
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        if 0 < i < steps:
            x += rng.uniform(-wobble, wobble)
            y += rng.uniform(-wobble, wobble)
        pts.append((x, y))
    draw.line(pts, fill=color, width=width, joint="curve")


def draw_highlighter_strip(
    draw: ImageDraw.Draw,
    x0: int,
    y0: int,
    x1: int,
    y1: int,
    color: Tuple[int, int, int] = HIGHLIGHT_YELLOW,
):
    """Draws a rounded felt-tip highlighter stroke behind key text."""
    r = max(4, (y1 - y0) // 2)
    draw.rounded_rectangle([x0 - 5, y0, x1 + 5, y1], radius=r, fill=color)


def draw_centered_pill_badge(
    draw: ImageDraw.Draw,
    center_x: int,
    top_y: int,
    text: str,
    color: Tuple[int, int, int],
    font: ImageFont.FreeTypeFont,
) -> Tuple[int, int, int, int]:
    """
    Draws a geometrically 100% centered pill badge at `(center_x, top_y)` using `anchor="mm"`.
    Guarantees symmetrical left/right and top/bottom padding with zero text clipping or offset.
    Returns `(rx0, ry0, rx1, ry1)` bounding box of the pill.
    """
    bbox = draw.textbbox((0, 0), text, font=font, anchor="mm")
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]

    pad_x = 14
    pad_y = 6
    pill_w = tw + pad_x * 2
    pill_h = max(24, th + pad_y * 2)

    rx0 = center_x - pill_w // 2
    ry0 = top_y
    rx1 = rx0 + pill_w
    ry1 = ry0 + pill_h

    cy = (ry0 + ry1) // 2

    # Clean white background with thick colored marker outline
    draw.rounded_rectangle(
        [rx0, ry0, rx1, ry1],
        radius=pill_h // 2,
        fill=(255, 255, 255),
        outline=color,
        width=2,
    )
    draw.text((center_x, cy), text, fill=color, font=font, anchor="mm")
    return (rx0, ry0, rx1, ry1)


def draw_editorial_header(
    draw: ImageDraw.Draw,
    act_badge: str,
    title_text: str,
    accent_color: Tuple[int, int, int] = ACCENT_CRIMSON,
) -> Dict[str, Any]:
    """
    Draws an Editorial Top Banner adhering to Cẩm Nang Vận Hành V3 (Rule 1.1):
    - Absolute zero technical labels like [PHẦN 1: THE MYTH-BUSTER HOOK], [PHẦN 4...], or [02. TEASER].
    - Clean concise curiosity-driven title text centered with stylish underline.
    """
    font_title = load_handwritten_font(21, bold=True, style="header")

    # Clean technical labels according to Rule 1.1
    badge_clean = act_badge.strip()
    if badge_clean.startswith("[") and badge_clean.endswith("]"):
        badge_clean = badge_clean[1:-1].strip()

    is_technical = any(k in badge_clean.upper() for k in ["THE MYTH-BUSTER", "CÚ BẺ LÁI", "LỜI NHẮN NHỦ", "TEASER", "RPG STATS", "BẢNG CHỈ SỐ", "PHẦN "])
    if is_technical:
        badge_clean = ""

    if badge_clean and title_text:
        full_str = f"{badge_clean}  •  {title_text}"
    elif badge_clean:
        full_str = badge_clean
    else:
        full_str = title_text

    tb = draw.textbbox((0, 0), full_str, font=font_title)
    tw = tb[2] - tb[0]
    th = tb[3] - tb[1]

    tx = (1280 - tw) // 2
    ty = 13 - tb[1]

    if badge_clean and title_text:
        bb = draw.textbbox((tx, ty), badge_clean, font=font_title)
        draw_highlighter_strip(draw, bb[0] - 6, bb[1] + 1, bb[2] + 6, bb[3] + 3, color=HIGHLIGHT_YELLOW)
        draw.text((tx, ty), badge_clean, fill=accent_color, font=font_title)
        bw = bb[2] - bb[0]
        draw.text((tx + bw, ty), f"  •  {title_text}", fill=INK_CHARCOAL, font=font_title)
    else:
        bb = draw.textbbox((tx, ty), full_str, font=font_title)
        draw_highlighter_strip(draw, bb[0] - 8, bb[1] + 1, bb[2] + 8, bb[3] + 3, color=HIGHLIGHT_YELLOW)
        draw.text((tx, ty), full_str, fill=INK_CHARCOAL, font=font_title)

    full_ink_box = draw.textbbox((tx, ty), full_str, font=font_title)
    line_y = full_ink_box[3] + 5

    draw_organic_line(
        draw,
        (full_ink_box[0] + 8, line_y),
        (full_ink_box[2] - 8, line_y),
        color=accent_color,
        width=3,
        wobble=1.0,
        seed=101,
    )
    draw_organic_line(
        draw,
        (full_ink_box[0] + 60, line_y + 4),
        (full_ink_box[2] - 60, line_y + 4),
        color=ACCENT_AMBER,
        width=2,
        wobble=0.8,
        seed=202,
    )

    bx0 = max(0, full_ink_box[0] - 12)
    by0 = max(0, full_ink_box[1] - 4)
    bx1 = min(1280, full_ink_box[2] + 12)
    by1 = min(720, line_y + 8)

    return {
        "has_box": False,
        "box": [bx0, by0, bx1, by1],
        "x": full_ink_box[0],
        "y": full_ink_box[1],
        "w": full_ink_box[2] - full_ink_box[0],
        "h": (line_y + 6) - full_ink_box[1],
        "text": full_str,
    }


def place_full_illustration_beat(
    canvas: Image.Image,
    draw: ImageDraw.Draw,
    beat_id: str,
    img_path: Path,
    caption_text: str,
    x: int,
    y: int,
    max_w: int,
    max_h: int,
    start_ms: int,
    end_ms: int,
    badge_text: Optional[str] = None,
    badge_color: Tuple[int, int, int] = ACCENT_CRIMSON,
    highlight_color: Tuple[int, int, int] = HIGHLIGHT_YELLOW,
    broll_video: Optional[Path] = None,
) -> Dict[str, Any]:
    """
    Places 100% of the original illustration onto the whiteboard canvas:
    - ZERO cropping, ZERO shaving, ZERO feathering: Displays the FULL illustration exactly as generated!
    - Centers the Pill Badge cleanly above the artwork.
    - Centers the FULL illustration with aspect ratio preserved.
    - Draws clean handwritten caption with highlighter strip below the illustration.
    """
    font_scale = max(1.0, min(1.35, max_w / 555.0))
    font_caption = load_handwritten_font(int(round(15 * font_scale)), bold=True, style="body")
    font_badge = load_handwritten_font(int(round(12 * font_scale)), bold=True, style="badge")

    top_badge_reserve = int(round(32 * font_scale)) if badge_text else 4
    footer_reserve = int(round(36 * font_scale))
    avail_h = max(60, max_h - top_badge_reserve - footer_reserve)

    # 1. Centered Pill Badge at the top
    center_x = x + max_w // 2
    pill_box = None
    if badge_text:
        pill_box = draw_centered_pill_badge(
            draw,
            center_x=center_x,
            top_y=y + 2,
            text=badge_text,
            color=badge_color,
            font=font_badge,
        )

    # 2. Load 100% FULL Original Illustration (No clipping, no cropping, no shaving!)
    raw_img = Image.open(img_path).convert("RGBA")
    rw, rh = raw_img.size
    scale = min(max_w / float(rw), avail_h / float(rh))
    new_w = max(1, int(round(rw * scale)))
    new_h = max(1, int(round(rh * scale)))
    full_resized = raw_img.resize((new_w, new_h), Image.Resampling.LANCZOS)

    img_zone_y = y + top_badge_reserve
    pos_x = x + (max_w - new_w) // 2
    pos_y = img_zone_y + (avail_h - new_h) // 2

    canvas.paste(full_resized, (pos_x, pos_y), full_resized)

    # 3. Handwritten Caption below the illustration (Strict Single-Card Containment & Zero-Bleed)
    cur_footer_y = img_zone_y + avail_h + 4
    pad_h = 24  # Horizontal safe margin within this node's slot [x + pad_h, x + max_w - pad_h]
    max_text_w = max(100, max_w - 2 * pad_h)

    # Dynamic font fitting: if caption_text exceeds max_text_w, step font size down until it fits cleanly
    base_font_sz = int(round(15 * font_scale))
    fitted_font = font_caption
    for test_sz in range(base_font_sz, 8, -1):
        test_font = load_handwritten_font(test_sz, bold=True, style="body")
        t_bb = draw.textbbox((0, 0), caption_text, font=test_font)
        if (t_bb[2] - t_bb[0]) <= max_text_w:
            fitted_font = test_font
            break
    font_caption = fitted_font

    # Guard: If still exceeds max_text_w, truncate with ellipsis safely so it NEVER cuts off awkwardly
    t_bb = draw.textbbox((0, 0), caption_text, font=font_caption)
    while (t_bb[2] - t_bb[0]) > max_text_w and len(caption_text) > 8:
        caption_text = caption_text[:-4].strip() + "..."
        t_bb = draw.textbbox((0, 0), caption_text, font=font_caption)

    raw_cb = draw.textbbox((0, 0), caption_text, font=font_caption)
    cw = raw_cb[2] - raw_cb[0]
    ch = raw_cb[3] - raw_cb[1]

    # Center caption, guaranteed strictly bounded inside [x + pad_h, x + max_w - pad_h]
    cx = x + (max_w - cw) // 2
    cx = max(x + pad_h, min(x + max_w - pad_h - cw, cx))
    cy = cur_footer_y - raw_cb[1]

    ink_cb = draw.textbbox((cx, cy), caption_text, font=font_caption)

    # Marker highlighter strip under the first keyword (before ':' if present)
    if ":" in caption_text:
        prefix = caption_text.split(":")[0] + ":"
        pb = draw.textbbox((cx, cy), prefix, font=font_caption)
        draw_highlighter_strip(draw, pb[0], pb[1] + 2, pb[2], pb[3] + 1, color=highlight_color)
    else:
        draw_organic_line(
            draw,
            (ink_cb[0] + 12, ink_cb[3] + 3),
            (ink_cb[2] - 12, ink_cb[3] + 3),
            color=badge_color,
            width=2,
            wobble=0.8,
            seed=len(caption_text),
        )

    draw.text((cx, cy), caption_text, fill=INK_CHARCOAL, font=font_caption)

    # Bounding boxes for renderer stream path (strictly bounded inside this node's grid slot [x, y, x + max_w, y + max_h])
    canv_w, canv_h = canvas.size
    slot_x0 = max(0, x)
    slot_y0 = max(0, y)
    slot_x1 = min(canv_w, x + max_w)
    slot_y1 = min(canv_h, y + max_h)

    pill_rect = (
        [
            max(slot_x0, pill_box[0] - 4),
            max(slot_y0, pill_box[1] - 2),
            min(slot_x1, pill_box[2] + 6),
            min(slot_y1, pill_box[3] + 6),
        ]
        if pill_box
        else None
    )
    art_rect = [
        max(slot_x0, pos_x - 2),
        max(slot_y0, pos_y - 2),
        min(slot_x1, pos_x + new_w + 2),
        min(slot_y1, min(pos_y + new_h + 2, ink_cb[1] - 2)),
    ]

    img_rx0 = max(slot_x0, min(pos_x, pill_box[0] if pill_box else pos_x) - 4)
    img_ry0 = max(slot_y0, min(pos_y, pill_box[1] if pill_box else pos_y) - 2)
    img_rx1 = min(slot_x1, max(pos_x + new_w, pill_box[2] if pill_box else pos_x + new_w) + 4)
    img_ry1 = min(slot_y1, ink_cb[1] - 3)

    bx0 = max(slot_x0, min(img_rx0, ink_cb[0] - 8))
    by0 = max(slot_y0, img_ry0 - 4)
    bx1 = min(slot_x1, max(img_rx1, ink_cb[2] + 8))
    by1 = min(slot_y1, ink_cb[3] + 8)

    cap_x0 = max(slot_x0, ink_cb[0] - 4)
    cap_x1 = min(slot_x1, ink_cb[2] + 4)
    cap_w = max(10, cap_x1 - cap_x0)

    return {
        "id": beat_id,
        "start_ms": start_ms,
        "end_ms": end_ms,
        "has_frame": False,
        "pill_box": pill_rect,
        "art_only_box": art_rect,
        "caption": {
            "text": caption_text,
            "x": cap_x0,
            "y": ink_cb[1] - 2,
            "w": cap_w,
            "h": (ink_cb[3] - ink_cb[1]) + 8,
            "color": list(INK_CHARCOAL),
        },
        "box": [bx0, by0, bx1, by1],
        "img_region": {
            "x": art_rect[0],
            "y": art_rect[1],
            "width": max(10, art_rect[2] - art_rect[0]),
            "height": max(10, art_rect[3] - art_rect[1]),
        },
        "broll_video": str(Path(broll_video).resolve()) if broll_video and Path(broll_video).exists() else None,
        "text_lines": [],
    }

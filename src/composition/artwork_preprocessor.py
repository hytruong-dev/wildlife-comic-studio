"""
Editorial Sketchbook Preprocessor (`artwork_preprocessor.py`)
Transforms raw AI-generated illustrations (e.g. from Gemini) into borderless,
organic 2D sketch cutouts that blend 100% seamlessly into the warm sketchbook
paper (#F8F6F1) with zero rectangular box edges or hard photo boundaries.

Key Capabilities:
1. Auto-detects and strips outer white margins and rectangular comic borders.
2. Converts near-white backgrounds into transparent alpha while preserving
   delicate ink lines, crosshatching, and watercolor highlights.
3. Applies an organic feathered vignette ONLY when colored backgrounds actually
   touch the image perimeter — never clips or fades clean line-art subjects!
"""

from pathlib import Path
from typing import Tuple
import cv2
import numpy as np
from PIL import Image


PAPER_RGB = (248, 246, 241)  # #F8F6F1 Warm Sketchbook Cream


def preprocess_illustration(
    img_path: Path,
    target_max_w: int,
    target_max_h: int,
    paper_rgb: Tuple[int, int, int] = PAPER_RGB,
) -> Image.Image:
    """
    Loads an illustration, strips any outer white margin or dark rectangular comic border,
    eliminates pure-white box patches via luminance-to-alpha matting, and scales cleanly
    to fit `(target_max_w, target_max_h)`.
    Returns an RGBA PIL Image ready to composite onto the sketchbook canvas.
    """
    im_bgr = cv2.imread(str(img_path), cv2.IMREAD_COLOR)
    if im_bgr is None:
        raise FileNotFoundError(f"Cannot load image: {img_path}")

    im_rgb = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2RGB)
    h, w, _ = im_rgb.shape
    gray = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2GRAY)

    # Step 1: Detect & shave rectangular black comic frame if Gemini drew one around the edge
    # First crop outer pure white margin if any
    non_white = gray < 246
    ys, xs = np.where(non_white)
    if len(ys) > 20:
        y0, y1 = max(0, int(ys.min()) - 2), min(h, int(ys.max()) + 3)
        x0, x1 = max(0, int(xs.min()) - 2), min(w, int(xs.max()) + 3)
        im_rgb = im_rgb[y0:y1, x0:x1]
        gray = gray[y0:y1, x0:x1]
        h, w = gray.shape

    border_shave = 0
    for shave in range(1, 22):
        if h <= 2 * shave + 40 or w <= 2 * shave + 40:
            break
        top_line = (gray[shave, :] < 115).mean()
        bot_line = (gray[h - 1 - shave, :] < 115).mean()
        left_line = (gray[:, shave] < 115).mean()
        right_line = (gray[:, w - 1 - shave] < 115).mean()
        if max(top_line, bot_line, left_line, right_line) > 0.45:
            border_shave = shave + 4

    if border_shave > 0:
        im_rgb = im_rgb[border_shave : h - border_shave, border_shave : w - border_shave]
        gray = gray[border_shave : h - border_shave, border_shave : w - border_shave]
        h, w = gray.shape

    # Step 2: Add a 10px white safety buffer around the cropped image BEFORE alpha matting
    # so that illustrations with characters near the edge are NEVER clipped by border feathering!
    pad = 10
    im_rgb = cv2.copyMakeBorder(im_rgb, pad, pad, pad, pad, cv2.BORDER_CONSTANT, value=(255, 255, 255))
    gray = cv2.copyMakeBorder(gray, pad, pad, pad, pad, cv2.BORDER_CONSTANT, value=255)
    h, w = gray.shape

    # Step 3: Resize to fit target bounding box with LANCZOS
    scale = min(target_max_w / float(w), target_max_h / float(h))
    new_w = max(1, int(round(w * scale)))
    new_h = max(1, int(round(h * scale)))
    im_rgb = cv2.resize(im_rgb, (new_w, new_h), interpolation=cv2.INTER_LANCZOS4)
    gray = cv2.resize(gray, (new_w, new_h), interpolation=cv2.INTER_AREA)

    # Step 4: Flood-fill connected near-white background from the outer perimeter
    # Also replace interior bright white (> 235) with warm paper tone (#F8F6F1) so there is ZERO white halo box!
    bg_candidates = (gray > 235).astype(np.uint8)
    num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(bg_candidates, connectivity=8)

    border_labels = set()
    border_labels.update(labels[0, :].tolist())
    border_labels.update(labels[new_h - 1, :].tolist())
    border_labels.update(labels[:, 0].tolist())
    border_labels.update(labels[:, new_w - 1].tolist())
    border_labels.discard(0)

    outer_bg_mask = np.isin(labels, list(border_labels)).astype(np.float32)

    # Dilate outer mask slightly (3px) and blur (9x9) to eliminate any white fringe around black ink strokes
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    outer_bg_dilated = cv2.dilate(outer_bg_mask, kernel, iterations=1)
    outer_bg_smooth = cv2.GaussianBlur(outer_bg_dilated, (9, 9), 2.2)

    # Luminance-based transparency for any remaining bright white pixels (> 232) connected or near exterior
    # Pure white (255) -> alpha 0.0; gray 228 -> alpha 1.0
    lum_alpha = np.clip((250.0 - gray.astype(np.float32)) / 22.0, 0.0, 1.0)
    final_alpha = np.where(
        outer_bg_mask > 0.5,
        0.0,
        np.minimum(1.0 - outer_bg_smooth * 0.85, np.maximum(lum_alpha, 1.0 - outer_bg_smooth * 1.5)),
    )
    # Any pixel with gray > 244 anywhere in the outer 85% region becomes semi-transparent so paper grain blends
    final_alpha = np.where(gray > 246, final_alpha * 0.15, final_alpha)
    final_alpha = np.clip(final_alpha, 0.0, 1.0)

    # Shift near-white RGB pixels (gray > 220) softly toward PAPER_RGB so anti-aliased edges match warm paper
    white_weight = np.clip((gray.astype(np.float32) - 215.0) / 40.0, 0.0, 1.0)[:, :, None]
    paper_arr = np.array(paper_rgb, dtype=np.float32)[None, None, :]
    im_rgb = np.clip(im_rgb.astype(np.float32) * (1.0 - white_weight * 0.85) + paper_arr * (white_weight * 0.85), 0, 255).astype(np.uint8)

    # Step 5: If the image has a full-bleed colored background touching the inner boundary
    # (before the 10px pad), apply a gentle vignette only on the colored background edges
    inner_margin = max(6, int(round(pad * scale)) + 2)
    inner_top = (gray[inner_margin, :] < 225).mean()
    inner_bot = (gray[new_h - 1 - inner_margin, :] < 225).mean()
    inner_left = (gray[:, inner_margin] < 225).mean()
    inner_right = (gray[:, new_w - 1 - inner_margin] < 225).mean()

    if max(inner_top, inner_bot, inner_left, inner_right) > 0.55:
        feather_px = max(14.0, min(new_w, new_h) * 0.065)
        dist_left = np.maximum(0.0, np.arange(new_w, dtype=np.float32)[None, :] - inner_margin + 2)
        dist_right = np.maximum(0.0, (new_w - 1 - np.arange(new_w, dtype=np.float32))[None, :] - inner_margin + 2)
        dist_top = np.maximum(0.0, np.arange(new_h, dtype=np.float32)[:, None] - inner_margin + 2)
        dist_bot = np.maximum(0.0, (new_h - 1 - np.arange(new_h, dtype=np.float32))[:, None] - inner_margin + 2)

        edge_dist = np.minimum(np.minimum(dist_left, dist_right), np.minimum(dist_top, dist_bot))
        edge_feather = np.clip(edge_dist / feather_px, 0.0, 1.0)
        edge_feather = edge_feather * edge_feather * (3.0 - 2.0 * edge_feather)
        final_alpha = np.clip(final_alpha * edge_feather, 0.0, 1.0)

    rgba = np.zeros((new_h, new_w, 4), dtype=np.uint8)
    rgba[:, :, :3] = im_rgb
    rgba[:, :, 3] = (final_alpha * 255.0).astype(np.uint8)

    return Image.fromarray(rgba, mode="RGBA")

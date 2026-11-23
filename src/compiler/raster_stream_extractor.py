import os
import cv2
import json
import argparse
import numpy as np
from skimage.morphology import skeletonize
from pathlib import Path

def extract_raster_strokes(
    image_path: str,
    target_x: int = 100,
    target_y: int = 100,
    target_w: int = 400,
    target_h: int = 400,
    ink_threshold: int = 65,
    brush_radius: int = 24
):
    """
    Biên dịch ảnh bitmap (PNG/JPG) thành chuỗi nét vẽ Ink-Path (skeleton) 
    và nét quét màu Color-Fill (contour-wipe / zigzag brush) theo thuật toán geeklee & letuandat131.
    """
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    if img is None:
        raise FileNotFoundError(f"Không thể đọc ảnh: {image_path}")

    # Resize to target box keeping aspect ratio
    orig_h, orig_w = img.shape[:2]
    scale = min(target_w / orig_w, target_h / orig_h)
    new_w = int(orig_w * scale)
    new_h = int(orig_h * scale)
    img_resized = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)

    # Handle Alpha channel if present
    if img_resized.shape[-1] == 4:
        alpha = img_resized[:, :, 3]
        bgr = img_resized[:, :, :3]
    else:
        alpha = np.ones((new_h, new_w), dtype=np.uint8) * 255
        bgr = img_resized

    # 1. CIELAB Color Space conversion
    lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)
    l_channel = lab[:, :, 0] # L* lightness 0..255 (OpenCV scales L to 0..255)

    # Segment ink lines: dark pixels with alpha > 128
    ink_mask = (l_channel < (ink_threshold * 255 // 100)) & (alpha > 128)
    ink_binary = ink_mask.astype(bool)

    # 2. Skeletonization (1-pixel width skeleton)
    skeleton = skeletonize(ink_binary)

    # 3. Trace skeleton pixels into continuous strokes
    skel_pts = np.argwhere(skeleton)
    strokes = []

    if len(skel_pts) > 0:
        # Build connected component contours from skeleton
        skel_u8 = (skeleton * 255).astype(np.uint8)
        contours, _ = cv2.findContours(skel_u8, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

        for cnt_idx, cnt in enumerate(contours):
            if len(cnt) < 3:
                continue
            # Smooth contour slightly with Douglas-Peucker
            epsilon = 1.2
            approx = cv2.approxPolyDP(cnt, epsilon, False)
            if len(approx) < 2:
                continue

            pts = []
            for p in approx:
                px = target_x + int(p[0][0])
                py = target_y + int(p[0][1])
                pts.append((px, py))

            # Convert to SVG path string
            d_parts = [f"M {pts[0][0]} {pts[0][1]}"]
            length = 0
            for i in range(1, len(pts)):
                d_parts.append(f"L {pts[i][0]} {pts[i][1]}")
                length += np.hypot(pts[i][0] - pts[i-1][0], pts[i][1] - pts[i-1][1])

            strokes.append({
                "id": f"raster_ink_{cnt_idx}",
                "d": " ".join(d_parts),
                "length": max(2.0, float(length)),
                "startPoint": { "x": pts[0][0], "y": pts[0][1] },
                "endPoint": { "x": pts[-1][0], "y": pts[-1][1] },
                "strokeColor": "#242322",
                "strokeWidth": 3.0,
                "isFillStroke": False,
                "priority": 10
            })

    # 4. Color fill zigzag strokes (contour-wipe / zigzag brush)
    # Regions that are colored (alpha > 128 and not ink)
    color_mask = (alpha > 128) & (~ink_mask)
    if np.any(color_mask):
        step = brush_radius
        # 45-degree zigzag lines across the colored bounding box
        min_y, min_x = np.min(np.argwhere(color_mask), axis=0)
        max_y, max_x = np.max(np.argwhere(color_mask), axis=0)

        # Average color in the region
        avg_bgr = np.mean(bgr[color_mask], axis=0)
        hex_color = f"#{int(avg_bgr[2]):02x}{int(avg_bgr[1]):02x}{int(avg_bgr[0]):02x}"

        fill_pts = []
        direction = 1
        for y_scan in range(min_y, max_y, step):
            row_mask = color_mask[y_scan, :]
            indices = np.where(row_mask)[0]
            if len(indices) > 0:
                x_left = int(target_x + indices[0])
                x_right = int(target_x + indices[-1])
                cur_y = int(target_y + y_scan)
                if direction == 1:
                    fill_pts.append((x_left, cur_y))
                    fill_pts.append((x_right, cur_y))
                else:
                    fill_pts.append((x_right, cur_y))
                    fill_pts.append((x_left, cur_y))
                direction *= -1

        if len(fill_pts) >= 2:
            d_parts = [f"M {fill_pts[0][0]} {fill_pts[0][1]}"]
            fill_len = 0
            for i in range(1, len(fill_pts)):
                d_parts.append(f"L {fill_pts[i][0]} {fill_pts[i][1]}")
                fill_len += float(np.hypot(fill_pts[i][0] - fill_pts[i-1][0], fill_pts[i][1] - fill_pts[i-1][1]))

            strokes.append({
                "id": "raster_color_fill",
                "d": " ".join(d_parts),
                "length": max(2.0, float(fill_len)),
                "startPoint": { "x": int(fill_pts[0][0]), "y": int(fill_pts[0][1]) },
                "endPoint": { "x": int(fill_pts[-1][0]), "y": int(fill_pts[-1][1]) },
                "strokeColor": hex_color,
                "strokeWidth": float(brush_radius),
                "isFillStroke": True,
                "priority": 100
            })

    print(f"[OK] Đã trích xuất {len(strokes)} nét vẽ từ ảnh raster: {image_path}")
    return strokes

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Raster Stream Ink-to-Color Extractor")
    parser.add_argument("--image", type=str, required=True, help="Đường dẫn ảnh PNG/JPG")
    parser.add_argument("--output", type=str, required=True, help="File JSON kết quả")
    parser.add_argument("--x", type=int, default=200)
    parser.add_argument("--y", type=int, default=200)
    parser.add_argument("--width", type=int, default=400)
    parser.add_argument("--height", type=int, default=400)
    args = parser.parse_args()

    res = extract_raster_strokes(args.image, args.x, args.y, args.width, args.height)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=2)
    print(f"[OK] Đã lưu annotations: {args.output}")

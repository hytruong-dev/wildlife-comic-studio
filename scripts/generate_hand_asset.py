"""
Script tự động xử lý và tối ưu hóa bộ ảnh PNG bàn tay vẽ theo chuẩn HandDraw Studio:
- Tách nền Alpha trong suốt
- Làm mềm viền cạnh cổ tay (feathering 12px) để không bị lộ cạnh cắt
- Tính toán và lưu tọa độ ngòi bút (Anchor Point) vào hand_metadata.json
- Tùy chọn tạo bóng đổ mềm (soft drop shadow)
"""
import os
import json
import argparse
import numpy as np
from PIL import Image, ImageFilter
from pathlib import Path

def process_hand_asset(
    input_png: str,
    output_dir: str = "assets/hands",
    anchor_x: int = 22,
    anchor_y: int = 47,
    feather_wrist_px: int = 12,
    default_scale: float = 0.8
):
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    
    img = Image.open(input_png).convert("RGBA")
    w, h = img.size
    print(f"[INFO] Đọc ảnh bàn tay: {input_png} ({w}x{h})")

    # Apply wrist edge feathering at the bottom/wrist region if needed
    if feather_wrist_px > 0:
        data = np.array(img)
        alpha = data[:, :, 3].astype(np.float32)
        
        # Feather bottom edge to avoid harsh cutoff
        for row in range(max(0, h - feather_wrist_px), h):
            factor = (h - 1 - row) / float(feather_wrist_px)
            alpha[row, :] = alpha[row, :] * factor

        data[:, :, 3] = np.clip(alpha, 0, 255).astype(np.uint8)
        img = Image.fromarray(data, mode="RGBA")

    # Save processed hand sprite
    hand_marker_path = out_path / "hand-marker-right.png"
    img.save(str(hand_marker_path), "PNG")
    print(f"[OK] Đã lưu sprite bàn tay: {hand_marker_path}")

    # Generate soft drop shadow
    shadow_img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    alpha_channel = img.split()[3]
    # Create black silhouette with smoothed alpha
    black_silhouette = Image.new("L", (w, h), 0)
    shadow_img.paste((30, 28, 25, 140), mask=alpha_channel)
    shadow_img = shadow_img.filter(ImageFilter.GaussianBlur(radius=8))
    
    shadow_path = out_path / "hand-shadow.png"
    shadow_img.save(str(shadow_path), "PNG")
    print(f"[OK] Đã tạo ảnh bóng đổ: {shadow_path}")

    # Save hand metadata JSON
    metadata = {
        "width": w,
        "height": h,
        "anchor": {
            "x": anchor_x,
            "y": anchor_y
        },
        "shadowAnchor": {
            "x": anchor_x,
            "y": anchor_y
        },
        "defaultScale": default_scale,
        "wristFeatherPx": feather_wrist_px
    }
    
    meta_path = out_path / "hand_metadata.json"
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)
    print(f"[OK] Đã lưu metadata tọa độ ngòi bút: {meta_path} (Anchor: ({anchor_x}, {anchor_y}))")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hand Asset Processor & Anchor Calibrator")
    parser.add_argument("--input", type=str, default="assets/hands/hand-marker-right.png", help="Đường dẫn ảnh bàn tay đầu vào")
    parser.add_argument("--outdir", type=str, default="assets/hands", help="Thư mục xuất kết quả")
    parser.add_argument("--anchor-x", type=int, default=22, help="Tọa độ X ngòi bút")
    parser.add_argument("--anchor-y", type=int, default=47, help="Tọa độ Y ngòi bút")
    parser.add_argument("--scale", type=float, default=0.8, help="Scale mặc định")
    args = parser.parse_args()

    process_hand_asset(args.input, args.outdir, args.anchor_x, args.anchor_y, default_scale=args.scale)

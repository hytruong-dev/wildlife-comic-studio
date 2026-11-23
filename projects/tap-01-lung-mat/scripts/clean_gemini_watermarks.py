"""
Clean Google Gemini 4-pointed star watermarks from:
1. All downloaded Gemini PNG illustrations in `projects/tap-01-lung-mat/assets/gemini_downloaded/*.png`
2. All frame-by-frame video streams in `assets/branding/gemini_generated_video_105939de.mp4` (Intro)
   and `assets/branding/gemini_generated_video_3314fb91.mp4` (Outro), exporting clean normalized
   `assets/branding/intro_ve_chuyen_hoang_da.mp4` and `assets/branding/outro_ve_chuyen_hoang_da.mp4`.
"""

import subprocess
import shutil
from pathlib import Path
import cv2
import numpy as np


def build_video_star_alpha_template() -> np.ndarray:
    """
    Reconstruct the exact 56x56 8-way symmetric alpha template of the Gemini Veo 2
    4-pointed star watermark at (w-148:w-92, h-148:h-92) on 1280x720 video frames.
    """
    cap = cv2.VideoCapture("assets/branding/gemini_generated_video_105939de.mp4")
    cap.set(cv2.CAP_PROP_POS_MSEC, 3500)
    ret, frame = cap.read()
    cap.release()
    if not ret or frame is None:
        raise RuntimeError("Could not read Intro video at t=3.5s for star template calibration.")

    roi = frame[-180:, -180:].astype(np.float32)
    sub = roi[32:88, 32:88].copy()
    yy, xx = np.mgrid[0:56, 0:56]
    dist = np.sqrt((xx - 27.5) ** 2 + (yy - 27.5) ** 2)
    border = dist > 25.0
    A = np.column_stack([xx[border], yy[border], np.ones(np.sum(border))])
    skin_plane = np.zeros_like(sub)
    for ch in range(3):
        coeffs, _, _, _ = np.linalg.lstsq(A, sub[:, :, ch][border], rcond=None)
        skin_plane[:, :, ch] = coeffs[0] * xx + coeffs[1] * yy + coeffs[2]

    alpha_raw = np.mean((sub - skin_plane) / (255.0 - skin_plane), axis=2)
    alpha_raw = np.clip(alpha_raw, 0.0, 0.45)
    alpha_sym = 0.25 * (
        alpha_raw + alpha_raw[::-1, :] + alpha_raw[:, ::-1] + alpha_raw[::-1, ::-1]
    )
    alpha_sym = 0.5 * (alpha_sym + alpha_sym.T)
    alpha_sym[alpha_sym < 0.015] = 0.0
    return alpha_sym


def clean_video_watermark(src_mp4: Path, dst_mp4: Path, alpha_sym: np.ndarray) -> None:
    """
    Remove the Gemini 4-pointed star watermark from every frame of a 1280x720 video
    using exact inverse alpha deblending, then mux with the original audio track
    normalized to 24fps, timescale 12288, 48kHz stereo 320kbps AAC.
    """
    cap = cv2.VideoCapture(str(src_mp4))
    fps = cap.get(cv2.CAP_PROP_FPS) or 24.0
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    tmp_vid = dst_mp4.with_suffix(".tmp_noaudio.mp4")
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(str(tmp_vid), fourcc, fps, (w, h))

    a3 = alpha_sym[:, :, None]
    y1, y2 = h - 148, h - 92
    x1, x2 = w - 148, w - 92

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        patch = frame[y1:y2, x1:x2].astype(np.float32)
        deblended = np.clip((patch - a3 * 255.0) / np.maximum(1.0 - a3, 0.2), 0, 255)
        frame[y1:y2, x1:x2] = deblended.astype(np.uint8)
        writer.write(frame)
        frame_count += 1

    cap.release()
    writer.release()

    # Mux cleaned video with original audio and normalize to master pipeline timebase
    cmd = [
        "ffmpeg", "-y",
        "-i", str(tmp_vid),
        "-i", str(src_mp4),
        "-map", "0:v:0",
        "-map", "1:a:0",
        "-vf", "scale=1280:720,fps=24,format=yuv420p",
        "-video_track_timescale", "12288",
        "-c:v", "libx264", "-preset", "fast", "-crf", "16",
        "-c:a", "aac", "-b:a", "320k", "-ar", "48000", "-ac", "2",
        str(dst_mp4),
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if tmp_vid.exists():
        tmp_vid.unlink()
    print(f"[Video Cleaned] {src_mp4.name} -> {dst_mp4.name} ({frame_count} frames deblended)")


def clean_gemini_png_assets(assets_dir: Path) -> None:
    """
    Clean the bottom-right Gemini 4-pointed star watermark from all PNGs in `assets_dir`.
    """
    backup_dir = assets_dir / "_raw_with_watermark_backup"
    backup_dir.mkdir(exist_ok=True)

    for png_path in sorted(assets_dir.glob("*.png")):
        backup_path = backup_dir / png_path.name
        if not backup_path.exists():
            shutil.copy2(png_path, backup_path)

        # Always read from the original backup so running the script is idempotent
        im = cv2.imread(str(backup_path))
        if im is None:
            continue
        h, w = im.shape[:2]
        roi = im[h - 140 : h, w - 140 : w].copy()
        b, g, r = cv2.split(roi)
        yy, xx = np.mgrid[0:140, 0:140]

        if png_path.name == "c5_stoffel_escape.png":
            # Wooden post corner: restore dark plank color [71, 117, 178] and crisp black border
            wood_bgr = roi[60, 100].copy()
            is_white = (b > 220) & (g > 220) & (r > 220)
            dist_to_white = cv2.distanceTransform((~is_white).astype(np.uint8), cv2.DIST_L2, 5)
            interior_star = (
                (dist_to_white > 4.2) & (yy >= 68) & (yy <= 108) & (xx >= 50) & (xx <= 115)
            )
            border_lightened = (
                (dist_to_white >= 1.2)
                & (dist_to_white <= 4.2)
                & (yy >= 75)
                & (yy <= 108)
                & (xx >= 55)
                & (xx <= 118)
                & (b > 40)
            )
            halo = (dist_to_white < 1.2) & (yy >= 72) & (xx >= 55) & (b < 254) & is_white
            roi[interior_star] = wood_bgr
            roi[border_lightened] = [16, 20, 28]
            roi[halo] = [255, 255, 255]
            blur = cv2.GaussianBlur(roi, (3, 3), 0.8)
            mod = interior_star | border_lightened
            roi[mod] = blur[mod]

        elif png_path.name == "c1_lions_sweating_scared.png":
            # Brown lion mane corner: restore brown fur and crisp black outline
            fur_bgr = roi[110, 62].copy()
            is_w1 = (b > 215) & (g > 215) & (r > 215)
            dist1 = cv2.distanceTransform((~is_w1).astype(np.uint8), cv2.DIST_L2, 5)
            int1 = (dist1 > 5.0) & (yy >= 75) & (yy <= 128) & (xx >= 55) & (xx <= 110) & (b > 65)
            bord1 = (
                (dist1 >= 0.8)
                & (dist1 <= 5.0)
                & (yy >= 78)
                & (yy <= 128)
                & (xx >= 68)
                & (xx <= 108)
                & (b > 35)
            )
            halo1 = (dist1 == 0) & (yy >= 78) & (yy <= 128) & (xx >= 68) & (xx <= 115) & (b < 254)
            roi[int1] = fur_bgr
            roi[bord1] = [12, 16, 22]
            roi[halo1] = [255, 255, 255]
            blur1 = cv2.GaussianBlur(roi, (3, 3), 0.8)
            roi[int1 | bord1] = blur1[int1 | bord1]

        elif png_path.name == "c5_stoffel_bbc_star.png":
            # Green leaf corner: inpaint lighter green star patch from surrounding leaf
            light_leaf = (yy >= 55) & (yy <= 115) & (xx >= 16) & (xx <= 68) & (g > 116) & (b < 210)
            mask2 = cv2.dilate(light_leaf.astype(np.uint8) * 255, np.ones((3, 3), np.uint8), iterations=1)
            mask2[(b > 220) | (g < 45)] = 0
            roi = cv2.inpaint(roi, mask2, 5, cv2.INPAINT_TELEA)
            roi[(yy >= 113) & (yy <= 116) & (xx >= 32) & (xx <= 62) & (g > 150) & (g < 245)] = [
                255,
                255,
                255,
            ]

        # For all images: normalize any off-white watermark/paper haze (B,G,R >= 228) in the bottom-right star zone to pure #FFFFFF
        star_paper_zone = (yy >= 40) & (xx >= 40) & (b >= 228) & (g >= 228) & (r >= 228)
        roi[star_paper_zone] = [255, 255, 255]

        im[h - 140 : h, w - 140 : w] = roi
        cv2.imwrite(str(png_path), im)
        print(f"[PNG Cleaned] {png_path.name}")


if __name__ == "__main__":
    alpha_sym = build_video_star_alpha_template()
    brand_dir = Path("assets/branding")
    clean_video_watermark(
        brand_dir / "gemini_generated_video_105939de.mp4",
        brand_dir / "intro_ve_chuyen_hoang_da.mp4",
        alpha_sym,
    )
    clean_video_watermark(
        brand_dir / "gemini_generated_video_3314fb91.mp4",
        brand_dir / "outro_ve_chuyen_hoang_da.mp4",
        alpha_sym,
    )
    clean_gemini_png_assets(Path("projects/tap-01-lung-mat/assets/gemini_downloaded"))
    print("[ALL GEMINI WATERMARKS CLEANED SUCCESSFULLY]")

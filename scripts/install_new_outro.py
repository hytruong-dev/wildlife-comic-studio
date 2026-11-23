"""
Clean Gemini watermark from new outro video and install as official branding asset.
Enforces TASTE-30, TASTE-36, LESSON-25 & LESSON-46.

Source: c:/Users/PC/Downloads/gemini_generated_video_0d2c9c41.mp4
Output: assets/branding/outro_ve_chuyen_hoang_da.mp4 (1280x720 @ 24fps, tbn=12288, 48kHz stereo)
"""

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import cv2
import numpy as np
from src.pipeline.asset_sanitizer import build_astroid_star_mask
BRAND_DIR = ROOT / "assets/branding"
SRC_DOWNLOAD = Path("c:/Users/PC/Downloads/gemini_generated_video_0d2c9c41.mp4")
RAW_BACKUP = BRAND_DIR / "gemini_generated_video_0d2c9c41.mp4"
OLD_OUTRO = BRAND_DIR / "outro_ve_chuyen_hoang_da.mp4"
OLD_BACKUP = BRAND_DIR / "outro_ve_chuyen_hoang_da_backup_v1.mp4"
OUT_OUTRO = BRAND_DIR / "outro_ve_chuyen_hoang_da.mp4"


def main():
    if not SRC_DOWNLOAD.exists():
        raise FileNotFoundError(f"Source video not found: {SRC_DOWNLOAD}")

    # 1. Back up raw download to assets/branding/
    print(f"1. Copying raw download to {RAW_BACKUP}...")
    shutil.copy2(SRC_DOWNLOAD, RAW_BACKUP)

    # 2. Back up existing old outro if not backed up yet
    if OLD_OUTRO.exists() and not OLD_BACKUP.exists():
        print(f"2. Backing up previous outro to {OLD_BACKUP}...")
        shutil.copy2(OLD_OUTRO, OLD_BACKUP)

    # 3. Clean watermark frame-by-frame
    print("3. Removing Gemini watermark from all frames...")
    cap = cv2.VideoCapture(str(RAW_BACKUP))
    fps = cap.get(cv2.CAP_PROP_FPS) or 24.0
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"   Video: {w}x{h} @ {fps:.2f}fps, {total_frames} frames")

    tmp_noaudio = BRAND_DIR / "outro_cleaned_noaudio.mp4"
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(str(tmp_noaudio), fourcc, fps, (w, h))

    # Astroid star mask & Telea core mask
    mask = build_astroid_star_mask(70, R=25.5, p=0.52)
    alpha = (mask.astype(np.float32) / 255.0) * 0.40
    alpha3 = alpha[:, :, None]

    core_mask = np.zeros((70, 70), dtype=np.uint8)
    cv2.circle(core_mask, (35, 35), 4, 255, -1)

    cx, cy = 1220, 660
    y1, y2 = cy - 35, cy + 35
    x1, x2 = cx - 35, cx + 35

    count = 0
    while True:
        ret, frame = cap.read()
        if not ret or frame is None:
            break
        patch = frame[y1:y2, x1:x2].astype(np.float32)
        deblended = np.clip(
            (patch - alpha3 * 255.0) / np.maximum(1.0 - alpha3, 0.1), 0, 255
        ).astype(np.uint8)
        inpainted = cv2.inpaint(deblended, core_mask, 3.0, cv2.INPAINT_TELEA)
        frame[y1:y2, x1:x2] = inpainted
        writer.write(frame)
        count += 1
        if count % 60 == 0 or count == total_frames:
            print(f"   Deblended {count}/{total_frames} frames...")

    cap.release()
    writer.release()
    print(f"   Deblended total {count} frames.")

    # 4. Mux with original audio and normalize timebase to 12288
    print("4. Muxing with audio track & normalizing timescale (12288 tbn, 48kHz stereo)...")
    tmp_final = BRAND_DIR / "outro_normalized_tmp.mp4"
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-i", str(tmp_noaudio),
        "-i", str(RAW_BACKUP),
        "-map", "0:v:0",
        "-map", "1:a:0",
        "-vf", "scale=1280:720,fps=24,format=yuv420p",
        "-video_track_timescale", "12288",
        "-c:v", "libx264", "-preset", "slow", "-crf", "16",
        "-c:a", "aac", "-b:a", "320k", "-ar", "48000", "-ac", "2",
        str(tmp_final),
    ]
    subprocess.run(cmd, check=True)

    # Replace OUT_OUTRO atomically
    tmp_noaudio.unlink(missing_ok=True)
    shutil.move(tmp_final, OUT_OUTRO)
    print(f"[SUCCESS] Official outro installed at: {OUT_OUTRO}")

    # 5. Extract sample verification frames
    verify_dir = ROOT / "tmp/verify_outro"
    verify_dir.mkdir(parents=True, exist_ok=True)
    for s, name in [(1.0, "t1s"), (5.0, "t5s"), (9.0, "t9s")]:
        out_png = verify_dir / f"outro_{name}.png"
        subprocess.run([
            "ffmpeg", "-y", "-loglevel", "error",
            "-ss", str(s), "-i", str(OUT_OUTRO),
            "-vframes", "1", str(out_png)
        ], check=True)
        # also save corner
        im = cv2.imread(str(out_png))
        if im is not None:
            cv2.imwrite(str(verify_dir / f"outro_{name}_corner.png"), im[600:720, 1150:1280])
    print(f"[VERIFY] Verification frames extracted to: {verify_dir}")


if __name__ == "__main__":
    main()

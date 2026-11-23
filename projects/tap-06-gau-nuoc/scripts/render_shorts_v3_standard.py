"""
Shorts Video Renderer V3 Standard — Episode 06: Gấu Nước (Tardigrade)
Strictly adheres to PHẦN 1.2 & PHẦN 3.2 of CẨM NANG VẬN HÀNH & KỊCH BẢN SẢN XUẤT V3:
1. Native 9:16 Vertical (1080 x 1920) at 30fps (54.0s duration)
2. 0 - 200px: Empty top safe zone
3. 200 - 380px: Fixed title banner pill: "KẺ BẤT TỬ CHẾT LÃNG XẸT VÌ... ỐC SÊN!"
4. 380 - 1250px: Main stage: EXACTLY 1 single large illustration at a time.
   Hand marker draws black ink outline in 1.8s, then color pops with smooth 100% -> 110% zoom.
5. 1250 - 1480px: Dynamic Kinetic Auto Captions (jumping in 3-4 word phrases, bold font, yellow/white with black outline).
6. 1480 - 1920px: Empty bottom safe zone (for channel name, title, and Related Video button).
7. Audio: ElevenLabs Adam eleven_v3, 100% complete sentences, zero cut-off, with 1.4s breathing buffer & smooth audio fade at the end.
"""

import sys
import os
import json
import subprocess
from pathlib import Path
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont

PROJ = Path(__file__).resolve().parent.parent
ROOT = PROJ.parent.parent
G_SHORTS = PROJ / "assets" / "gemini_downloaded_shorts"
AUDIO_DIR = PROJ / "audio"
SFX_DIR = ROOT / "assets" / "sfx"
RENDERS_DIR = PROJ / "renders"
RENDERS_DIR.mkdir(parents=True, exist_ok=True)

VOICE_WAV = AUDIO_DIR / "shorts_v3_perfect.wav"
BGM_WAV = ROOT / "assets" / "bgm" / "calm-acoustic.wav"
SCRIBBLE_WAV = SFX_DIR / "marker-scribble-loop.wav"
POP_WAV = SFX_DIR / "pop.mp3" if (SFX_DIR / "pop.mp3").exists() else SFX_DIR / "tap_1.wav"
OUTPUT_MP4 = RENDERS_DIR / "shorts_ep06_v3_standard.mp4"

# Fonts
font_title = ImageFont.truetype("c:/Windows/Fonts/segoeuib.ttf", 36)
font_caption = ImageFont.truetype("c:/Windows/Fonts/segoeuib.ttf", 46)


class HandRig:
    def __init__(self, target_scale: float = 0.70):
        hand_path = ROOT / "tools" / "srt-whiteboard-animation" / "assets" / "drawing-hand.png"
        if not hand_path.exists():
            hand_path = ROOT / "projects" / "tap-01-lung-mat" / "assets" / "user_clean_hand.png"
        raw = cv2.imread(str(hand_path), cv2.IMREAD_UNCHANGED)
        if raw is None:
            raise FileNotFoundError(f"Hand image not found at {hand_path}")

        # Scale down hand
        new_w = int(raw.shape[1] * target_scale)
        new_h = int(raw.shape[0] * target_scale)
        self.hand_img = cv2.resize(raw, (new_w, new_h), interpolation=cv2.INTER_AREA)

        # Pen tip anchor: top-left region of the marker nib
        self.tip_x = int(58 * target_scale)
        self.tip_y = int(32 * target_scale)
        self.h, self.w = self.hand_img.shape[:2]

    def stamp(self, canvas_bgr: np.ndarray, pen_x: int, pen_y: int) -> np.ndarray:
        top_left_x = pen_x - self.tip_x
        top_left_y = pen_y - self.tip_y

        h_canvas, w_canvas = canvas_bgr.shape[:2]
        x1_src = max(0, -top_left_x)
        y1_src = max(0, -top_left_y)
        x2_src = min(self.w, w_canvas - top_left_x)
        y2_src = min(self.h, h_canvas - top_left_y)

        if x1_src >= x2_src or y1_src >= y2_src:
            return canvas_bgr

        x1_dst = max(0, top_left_x)
        y1_dst = max(0, top_left_y)
        x2_dst = x1_dst + (x2_src - x1_src)
        y2_dst = y1_dst + (y2_src - y1_src)

        hand_crop = self.hand_img[y1_src:y2_src, x1_src:x2_src]
        canvas_crop = canvas_bgr[y1_dst:y2_dst, x1_dst:x2_dst]

        if hand_crop.shape[2] == 4:
            alpha = (hand_crop[:, :, 3] / 255.0)[:, :, np.newaxis]
            rgb = hand_crop[:, :, :3]
            blended = (rgb * alpha + canvas_crop * (1.0 - alpha)).astype(np.uint8)
            canvas_bgr[y1_dst:y2_dst, x1_dst:x2_dst] = blended
        else:
            canvas_bgr[y1_dst:y2_dst, x1_dst:x2_dst] = hand_crop[:, :, :3]

        return canvas_bgr


def prepare_illustration_assets(img_path: Path, target_w: int = 900, target_h: int = 800):
    """Load color image, resize maintaining aspect ratio within target bounding box, and extract Canny edge paths."""
    im = cv2.imread(str(img_path))
    if im is None:
        raise FileNotFoundError(f"Missing image: {img_path}")

    ih, iw = im.shape[:2]
    scale = min(target_w / iw, target_h / ih)
    nw = int(round(iw * scale))
    nh = int(round(ih * scale))
    resized_color = cv2.resize(im, (nw, nh), interpolation=cv2.INTER_LANCZOS4)

    # Convert to grayscale and get edges
    gray = cv2.cvtColor(resized_color, cv2.COLOR_BGR2GRAY)
    # Threshold background to pure white
    _, bg_mask = cv2.threshold(gray, 248, 255, cv2.THRESH_BINARY)
    resized_color[bg_mask == 255] = [255, 255, 255]

    edges = cv2.Canny(gray, 50, 150)
    # Morphological close to join broken contours
    kernel = np.ones((2, 2), np.uint8)
    edges = cv2.dilate(edges, kernel, iterations=1)

    contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    # Sort contours by length descending
    contours = sorted(contours, key=lambda c: len(c), reverse=True)

    # Flatten contour points into a sequential drawing path
    path_points = []
    for c in contours:
        for pt in c:
            path_points.append((int(pt[0][0]), int(pt[0][1])))

    return {
        "color": resized_color,
        "nw": nw,
        "nh": nh,
        "path": path_points,
        "contours": contours,
    }


def render_fixed_header(draw: ImageDraw.ImageDraw, w: int):
    """Zone 2 (200 - 380px): Fixed Title Banner Pill."""
    banner_w = 980
    banner_h = 100
    x0 = (w - banner_w) // 2
    y0 = 240
    x1 = x0 + banner_w
    y1 = y0 + banner_h

    # Pill shape background (Dark Slate Blue)
    draw.rounded_rectangle([x0, y0, x1, y1], radius=50, fill=(15, 23, 42))
    # Golden border
    draw.rounded_rectangle([x0, y0, x1, y1], radius=50, outline=(234, 179, 8), width=5)

    text = "KẺ BẤT TỬ CHẾT LÃNG XẸT VÌ... ỐC SÊN!"
    bbox = draw.textbbox((0, 0), text, font=font_title)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = x0 + (banner_w - tw) // 2
    ty = y0 + (banner_h - th) // 2 - 3

    # White bold text
    draw.text((tx, ty), text, font=font_title, fill=(255, 255, 255))


def render_caption_text(draw: ImageDraw.ImageDraw, text: str, w: int):
    """Zone 4 (1250 - 1480px): Dynamic Kinetic Auto Captions."""
    bbox = draw.textbbox((0, 0), text, font=font_caption)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = (w - tw) // 2
    ty = 1365 - th // 2

    # Thick Black Outline
    stroke_w = 5
    for dx in range(-stroke_w, stroke_w + 1):
        for dy in range(-stroke_w, stroke_w + 1):
            if dx * dx + dy * dy <= stroke_w * stroke_w:
                draw.text((tx + dx, ty + dy), text, font=font_caption, fill=(0, 0, 0))

    # Bright Gold fill
    draw.text((tx, ty), text, font=font_caption, fill=(253, 224, 71))


def main():
    print("=== RENDER SHORTS V3 STANDARD (TẬP 06) — ZERO CUT-OFF & COMPLETE SENTENCE ===")
    fps = 30
    w = 1080
    h = 1920

    # 6 Beats specification matching Whisper word timestamps:
    # Total voice ends at 52.56s. Total video is 54.0s (1.44s clean buffer with fading BGM).
    beats_meta = [
        {
            "id": "beat1",
            "start_s": 0.0,
            "end_s": 9.8,
            "draw_dur_s": 1.8,
            "img_path": G_SHORTS / "shorts01_superhero_space_radiation.png",
            "captions": [
                (0.0, 2.2, "Chỉ một con ốc sên nhỏ bé,"),
                (2.2, 4.8, "cũng đủ hạ gục kẻ bất tử này!"),
                (4.8, 6.8, "Dù đây là sinh vật duy nhất trên Trái Đất"),
                (6.8, 9.8, "sống sót qua 5 cuộc đại tuyệt chủng!"),
            ],
        },
        {
            "id": "beat2",
            "start_s": 9.8,
            "end_s": 22.4,
            "draw_dur_s": 1.8,
            "img_path": G_SHORTS / "shorts02_temperature_extreme_scale.png",
            "captions": [
                (9.8, 12.5, "Chỉ dài nửa mi-li-mét bằng dấu chấm câu,"),
                (12.5, 15.0, "chịu được cái lạnh âm 272 độ C,"),
                (15.0, 17.5, "nước sôi 150 độ C,"),
                (17.5, 22.4, "ném ra vũ trụ 10 ngày vẫn đẻ con bình thường!"),
            ],
        },
        {
            "id": "beat3",
            "start_s": 22.4,
            "end_s": 32.2,
            "draw_dur_s": 1.8,
            "img_path": G_SHORTS / "shorts03_tun_state_glass_hibernation.png",
            "captions": [
                (22.4, 25.5, "Bí mật nằm ở tuyệt kỹ rút 99% nước,"),
                (25.5, 28.5, "tiết chất đạm biến nội tạng thành thủy tinh!"),
                (28.5, 32.2, "Chỉ cần 1 giọt nước, sống dậy sau 30 năm đóng băng!"),
            ],
        },
        {
            "id": "beat4",
            "start_s": 32.2,
            "end_s": 41.5,
            "draw_dur_s": 1.8,
            "img_path": G_SHORTS / "shorts04_snail_slime_choke_trap.png",
            "captions": [
                (32.2, 35.5, "Thế nhưng, hóa thủy tinh mất vài tiếng chuẩn bị,"),
                (35.5, 38.5, "khi ốc sên bất ngờ trườn qua nuốt gọn,"),
                (38.5, 41.5, "vị thần bất tử hoàn toàn không kịp biến hình!"),
            ],
        },
        {
            "id": "beat5",
            "start_s": 41.5,
            "end_s": 47.5,
            "draw_dur_s": 1.8,
            "img_path": G_SHORTS / "shorts05_moon_crash_sleeping_bears.png",
            "captions": [
                (41.5, 44.5, "Bí ẩn hàng ngàn Gấu Nước trên Mặt Trăng"),
                (44.5, 47.5, "đã có ở video dài bên dưới kênh!"),
            ],
        },
        {
            "id": "beat6",
            "start_s": 47.5,
            "end_s": 54.0,
            "draw_dur_s": 1.8,
            "img_path": G_SHORTS / "shorts06_channel_funnel_cta_mascot.png",
            "captions": [
                (47.5, 50.5, "Dù bất tử ngoài vũ trụ nhưng trước ốc sên,"),
                (50.5, 52.6, "nó vẫn sẽ tiêu đời ngay lập tức!"),
                (52.6, 54.0, "Bấm xem video dài ngay bên dưới nhé! 👇"),
            ],
        },
    ]

    total_dur_s = 54.0
    total_frames = int(round(total_dur_s * fps))
    print(f"Total video duration: {total_dur_s:.2f}s ({total_frames} frames @ {fps}fps)")

    # Pre-process illustration edge paths
    print("Pre-processing illustration edge paths...")
    assets = {}
    for b in beats_meta:
        assets[b["id"]] = prepare_illustration_assets(b["img_path"])
        print(f"  Processed {b['id']}: nw={assets[b['id']]['nw']}, nh={assets[b['id']]['nh']}, path pts={len(assets[b['id']]['path'])}")

    hand = HandRig(target_scale=0.72)

    # Setup FFmpeg raw video encoding pipe
    temp_raw_mp4 = RENDERS_DIR / "temp_shorts_visual.mp4"
    cmd_ffmpeg = [
        "ffmpeg", "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{w}x{h}",
        "-pix_fmt", "bgr24",
        "-r", str(fps),
        "-i", "-",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        str(temp_raw_mp4)
    ]

    pipe = subprocess.Popen(cmd_ffmpeg, stdin=subprocess.PIPE)

    # Stage coordinates: centered in Zone 3 (380 to 1250 -> center Y = 815)
    stage_center_x = 540
    stage_center_y = 815

    print("Rendering frames to FFmpeg pipe...")
    for frame_idx in range(total_frames):
        t = frame_idx / fps

        # Find current beat
        curr_beat = beats_meta[-1]
        for b in beats_meta:
            if b["start_s"] <= t < b["end_s"]:
                curr_beat = b
                break

        b_id = curr_beat["id"]
        b_st = curr_beat["start_s"]
        b_en = curr_beat["end_s"]
        b_dur = b_en - b_st
        b_elapsed = t - b_st
        ast = assets[b_id]

        # 1. Base clean white canvas
        canvas_bgr = np.full((h, w, 3), 255, dtype=np.uint8)

        # 2. Stage rendering in Zone 3
        nw, nh = ast["nw"], ast["nh"]
        draw_dur = curr_beat["draw_dur_s"]

        if b_elapsed < draw_dur:
            # PHASE 1: Progressive Hand Outline Drawing (0.0s -> 1.8s)
            u = max(0.01, min(1.0, b_elapsed / draw_dur))
            total_pts = len(ast["path"])
            curr_pts_count = int(total_pts * u)

            # Draw progressive ink mask
            ink_layer = np.full((nh, nw), 255, dtype=np.uint8)
            # Find contours up to current progress
            cum_pts = 0
            pen_x_img, pen_y_img = nw // 2, nh // 2
            for c in ast["contours"]:
                c_len = len(c)
                if cum_pts + c_len <= curr_pts_count:
                    cv2.drawContours(ink_layer, [c], -1, 0, 2)
                    cum_pts += c_len
                    pen_x_img, pen_y_img = int(c[-1][0][0]), int(c[-1][0][1])
                elif cum_pts < curr_pts_count:
                    partial = c[: curr_pts_count - cum_pts]
                    if len(partial) > 1:
                        cv2.polylines(ink_layer, [partial], False, 0, 2)
                        pen_x_img, pen_y_img = int(partial[-1][0][0]), int(partial[-1][0][1])
                    cum_pts = curr_pts_count
                    break
                else:
                    break

            # Stamp ink layer onto canvas centered at stage
            x0 = stage_center_x - nw // 2
            y0 = stage_center_y - nh // 2
            ink_3ch = cv2.cvtColor(ink_layer, cv2.COLOR_GRAY2BGR)
            canvas_bgr[y0 : y0 + nh, x0 : x0 + nw] = ink_3ch

            # Hand stamps at pen tip
            pen_x_global = x0 + pen_x_img
            pen_y_global = y0 + pen_y_img
            canvas_bgr = hand.stamp(canvas_bgr, pen_x_global, pen_y_global)

        elif b_elapsed < draw_dur + 0.35:
            # PHASE 2: Color burst + Hand exiting downwards
            color_img = ast["color"]
            x0 = stage_center_x - nw // 2
            y0 = stage_center_y - nh // 2
            canvas_bgr[y0 : y0 + nh, x0 : x0 + nw] = color_img

            # Hand gliding away downwards
            glide_u = (b_elapsed - draw_dur) / 0.35
            pen_x_global = x0 + nw // 2
            pen_y_global = y0 + nh + int(glide_u * 350)
            canvas_bgr = hand.stamp(canvas_bgr, pen_x_global, pen_y_global)

        else:
            # PHASE 3: Color display with subtle breathing zoom (1.0 -> 1.10)
            zoom_u = (b_elapsed - draw_dur) / max(0.1, (b_dur - draw_dur))
            zoom_scale = 1.0 + 0.10 * zoom_u
            cur_w = int(round(nw * zoom_scale))
            cur_h = int(round(nh * zoom_scale))
            zoomed_im = cv2.resize(ast["color"], (cur_w, cur_h), interpolation=cv2.INTER_LANCZOS4)

            x0 = stage_center_x - cur_w // 2
            y0 = stage_center_y - cur_h // 2

            # Clamp boundaries within canvas
            cx0 = max(0, x0)
            cy0 = max(0, y0)
            cx1 = min(w, x0 + cur_w)
            cy1 = min(h, y0 + cur_h)

            zx0 = cx0 - x0
            zy0 = cy0 - y0
            zx1 = zx0 + (cx1 - cx0)
            zy1 = zy0 + (cy1 - cy0)

            canvas_bgr[cy0:cy1, cx0:cx1] = zoomed_im[zy0:zy1, zx0:zx1]

        # 3. Overlay PIL graphics (Fixed Header & Kinetic Captions)
        pil_canvas = Image.fromarray(cv2.cvtColor(canvas_bgr, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(pil_canvas)

        # Render Zone 2: Fixed Header Banner
        render_fixed_header(draw, w)

        # Render Zone 4: Kinetic Auto Captions
        active_caption = ""
        for st, en, cap_text in curr_beat["captions"]:
            if st <= t < en:
                active_caption = cap_text
                break
        if active_caption:
            render_caption_text(draw, active_caption, w)

        # Convert back to BGR and write to pipe
        final_bgr = cv2.cvtColor(np.array(pil_canvas), cv2.COLOR_RGB2BGR)
        pipe.stdin.write(final_bgr.tobytes())

        if frame_idx % 150 == 0:
            print(f"  Frame {frame_idx}/{total_frames} ({frame_idx/total_frames*100:.1f}%)")

    pipe.stdin.close()
    pipe.wait()
    print("Video stream finished. Now muxing audio & SFX...")

    # Audio Muxing with FFmpeg:
    # 1. Voice audio with apad (pad duration 3s) so it NEVER truncates prematurely
    # 2. Duck BGM to volume 0.08
    # 3. Marker scribble loop volume 0.25
    # 4. Mix all 3 with amix, and add smooth 1.5s fade out starting at 52.5s
    cmd_mux = [
        "ffmpeg", "-y",
        "-i", str(temp_raw_mp4),
        "-i", str(VOICE_WAV),
        "-i", str(BGM_WAV),
        "-i", str(SCRIBBLE_WAV),
        "-filter_complex",
        "[1:a]apad=pad_dur=3.0[vpad];"
        "[2:a]aloop=loop=-1:size=2e+09,volume=0.08[bgm];"
        "[3:a]aloop=loop=-1:size=2e+09,volume=0.25[scribble];"
        "[vpad][bgm][scribble]amix=inputs=3:duration=first:dropout_transition=0[mixed];"
        "[mixed]afade=t=out:st=52.5:d=1.5[aout]",
        "-map", "0:v",
        "-map", "[aout]",
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "192k",
        "-t", f"{total_dur_s}",
        str(OUTPUT_MP4)
    ]

    subprocess.run(cmd_mux, check=True)
    print(f"=== COMPLETED SHORTS MASTER RENDER: {OUTPUT_MP4} ===")


if __name__ == "__main__":
    main()

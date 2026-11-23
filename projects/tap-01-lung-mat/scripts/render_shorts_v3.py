"""
YouTube Shorts V3 Renderer (9:16 Vertical 1080x1920)
Engine: Card Reveal + Handwriting Whiteboard + Full SFX Design
Duration: 36.49s
"""

import math
import subprocess
import time
from pathlib import Path
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

SCRIPT_DIR = Path(__file__).resolve().parent
PROJ = SCRIPT_DIR.parent
ROOT = PROJ.parent.parent
G = PROJ / "assets" / "gemini_downloaded"
HAND_ASSET = PROJ / "assets" / "user_clean_hand.png"
SFX_DIR = ROOT / "assets" / "sfx" / "pixabay"
SCRIBBLE_WAV = ROOT / "assets" / "sfx" / "marker-scribble-loop.wav"
RENDERS_DIR = PROJ / "renders_v3"
RENDERS_DIR.mkdir(parents=True, exist_ok=True)

# Fonts
FONT_DIR = ROOT / "assets" / "fonts"
try:
    font_main_title = ImageFont.truetype(str(FONT_DIR / "BeVietnamPro-Bold.ttf"), 38)
    font_sub_title = ImageFont.truetype(str(FONT_DIR / "BeVietnamPro-SemiBold.ttf"), 23)
    font_card_header = ImageFont.truetype(str(FONT_DIR / "BeVietnamPro-Bold.ttf"), 26)
    font_card_bold = ImageFont.truetype(str(FONT_DIR / "PlaypenSans-Bold.ttf"), 23)
    font_card_reg = ImageFont.truetype(str(FONT_DIR / "PatrickHand-Regular.ttf"), 24)
    font_cta = ImageFont.truetype(str(FONT_DIR / "BeVietnamPro-Bold.ttf"), 28)
except Exception:
    font_main_title = font_sub_title = font_card_header = font_card_bold = font_card_reg = font_cta = ImageFont.load_default()


def fit_contain(im: Image.Image, max_w: int, max_h: int) -> Image.Image:
    w, h = im.size
    scale = min(max_w / w, max_h / h)
    return im.resize((max(1, int(round(w * scale))), max(1, int(round(h * scale)))), Image.Resampling.LANCZOS)


def ease_out_back(t: float, c1: float = 1.70158) -> float:
    t = max(0.0, min(1.0, t))
    c3 = c1 + 1.0
    return 1.0 + c3 * math.pow(t - 1.0, 3) + c1 * math.pow(t - 1.0, 2)


def create_shorts_canvases_v3():
    w, h = 1080, 1920
    bg_color = (249, 246, 240)
    base_pil = Image.new("RGB", (w, h), bg_color)
    draw_b = ImageDraw.Draw(base_pil)
    full_pil = Image.new("RGB", (w, h), bg_color)
    draw_f = ImageDraw.Draw(full_pil)

    # 1. Top Header Banner
    h_box = [30, 30, 1050, 175]
    for d in (draw_b, draw_f):
        # Drop shadow
        d.rounded_rectangle([h_box[0] + 4, h_box[1] + 4, h_box[2] + 4, h_box[3] + 4], radius=18, fill=(228, 224, 216))
        d.rounded_rectangle(h_box, radius=18, fill=(255, 243, 240), outline=(217, 56, 30), width=4)
    draw_f.text((540, 78), "3 SỰ THẬT ĐIÊN RỒ VỀ LỬNG MẬT", fill=(217, 56, 30), font=font_main_title, anchor="mm")
    draw_f.text((540, 130), "KẺ CHÍ PHÈO KHÔNG BIẾT SỢ BẤT KỲ AI TRÊN TRÁI ĐẤT", fill=(60, 60, 60), font=font_sub_title, anchor="mm")

    # Card 1: Fact 1 (Top)
    c1_box = [40, 195, 1040, 705]
    im1 = fit_contain(Image.open(G / "c3_badger_turn_180.png").convert("RGB"), 460, 420)
    for d, im_tgt in ((draw_b, base_pil), (draw_f, full_pil)):
        d.rounded_rectangle([c1_box[0] + 4, c1_box[1] + 4, c1_box[2] + 4, c1_box[3] + 4], radius=16, fill=(228, 224, 216))
        d.rounded_rectangle(c1_box, radius=16, fill=(255, 255, 255), outline=(43, 108, 176), width=3)
        d.rectangle([43, 198, 1037, 248], fill=(240, 246, 255))
        d.text((65, 223), "1. BỘ GIÁP 6MM XOAY 180 ĐỘ TRONG DA", fill=(43, 108, 176), font=font_card_header, anchor="lm")
        im_tgt.paste(im1, (65, 260))
        d.rectangle([64, 259, 65 + im1.width, 260 + im1.height], outline=(220, 225, 230), width=1)
        d.rounded_rectangle(c1_box, radius=16, outline=(43, 108, 176), width=3)

    draw_f.text((550, 280), "• Da dày 6mm trơn tuột:", fill=(30, 30, 30), font=font_card_bold)
    draw_f.text((565, 315), "Răng nanh sư tử cắn vào bị trượt\nKhông thể xuyên thủng lớp sừng", fill=(70, 70, 70), font=font_card_reg)
    draw_f.text((550, 385), "• Xoay 180 độ trong bao da:", fill=(217, 56, 30), font=font_card_bold)
    draw_f.text((565, 420), "Bị cắn gáy liền quay ngoắt đầu\nNgoạm đứt mũi báo hoa phản đòn!", fill=(70, 70, 70), font=font_card_reg)
    draw_f.text((550, 495), "• Vũ khí không góc chết:", fill=(43, 108, 176), font=font_card_bold)
    draw_f.text((565, 530), "Biến mọi thế bị bắt thành tử địa!", fill=(70, 70, 70), font=font_card_reg)

    # Card 2: Fact 2 (Middle)
    c2_box = [40, 730, 1040, 1240]
    im2 = fit_contain(Image.open(G / "c4_badger_sleeping_venom.png").convert("RGB"), 460, 420)
    for d, im_tgt in ((draw_b, base_pil), (draw_f, full_pil)):
        d.rounded_rectangle([c2_box[0] + 4, c2_box[1] + 4, c2_box[2] + 4, c2_box[3] + 4], radius=16, fill=(228, 224, 216))
        d.rounded_rectangle(c2_box, radius=16, fill=(255, 255, 255), outline=(130, 60, 160), width=3)
        d.rectangle([43, 733, 1037, 783], fill=(250, 242, 255))
        d.text((65, 758), "2. MIỄN NHIỄM NỌC ĐỘC & NGỦ HỒI SINH", fill=(130, 60, 160), font=font_card_header, anchor="lm")
        im_tgt.paste(im2, (65, 795))
        d.rectangle([64, 794, 65 + im2.width, 795 + im2.height], outline=(220, 225, 230), width=1)
        d.rounded_rectangle(c2_box, radius=16, outline=(130, 60, 160), width=3)

    draw_f.text((550, 815), "• Coi rắn độc là đồ ăn vặt:", fill=(30, 30, 30), font=font_card_bold)
    draw_f.text((565, 850), "Hổ mang chúa, rắn lục, mamba đen\nĐều bị ngoạm đứt đầu nuốt chửng", fill=(70, 70, 70), font=font_card_reg)
    draw_f.text((550, 920), "• Đột biến gen kháng độc:", fill=(130, 60, 160), font=font_card_bold)
    draw_f.text((565, 955), "Thụ thể thần kinh không dính nọc\nMiễn nhiễm nọc độc tự nhiên", fill=(70, 70, 70), font=font_card_reg)
    draw_f.text((550, 1025), "• Giấc ngủ giải độc 2 tiếng:", fill=(47, 133, 90), font=font_card_bold)
    draw_f.text((565, 1060), "Bị cắn chỉ lăn ra ngủ mê man\nTỉnh dậy lại xơi nốt nửa con rắn!", fill=(70, 70, 70), font=font_card_reg)

    # Card 3: Fact 3 (Bottom)
    c3_box = [40, 1265, 1040, 1775]
    im3 = fit_contain(Image.open(G / "c5_stoffel_escape.png").convert("RGB"), 460, 420)
    for d, im_tgt in ((draw_b, base_pil), (draw_f, full_pil)):
        d.rounded_rectangle([c3_box[0] + 4, c3_box[1] + 4, c3_box[2] + 4, c3_box[3] + 4], radius=16, fill=(228, 224, 216))
        d.rounded_rectangle(c3_box, radius=16, fill=(255, 255, 255), outline=(47, 133, 90), width=3)
        d.rectangle([43, 1268, 1037, 1318], fill=(240, 252, 245))
        d.text((65, 1293), "3. THIÊN TÀI VƯỢT NGỤC STOFFEL (IQ 90)", fill=(47, 133, 90), font=font_card_header, anchor="lm")
        im_tgt.paste(im3, (65, 1330))
        d.rectangle([64, 1329, 65 + im3.width, 1330 + im3.height], outline=(220, 225, 230), width=1)
        d.rounded_rectangle(c3_box, radius=16, outline=(47, 133, 90), width=3)

    draw_f.text((550, 1350), "• Khả năng dùng công cụ siêu phàm:", fill=(30, 30, 30), font=font_card_bold)
    draw_f.text((565, 1385), "Xếp đá làm thang trèo tường\nDùng que cây, chổi làm đòn bẩy", fill=(70, 70, 70), font=font_card_reg)
    draw_f.text((550, 1455), "• Đắp bóng bùn phơi khô:", fill=(47, 133, 90), font=font_card_bold)
    draw_f.text((565, 1490), "Khi hết đá, tự nặn bóng bùn\nLăn qua rào điện thoát ra ngoài!", fill=(70, 70, 70), font=font_card_reg)
    draw_f.text((550, 1560), "• Trí thông minh giải đố:", fill=(217, 56, 30), font=font_card_bold)
    draw_f.text((565, 1595), "Top đầu thông minh thế giới loài vật!", fill=(70, 70, 70), font=font_card_reg)

    # 4. Bottom CTA Banner
    cta_box = [40, 1795, 1040, 1900]
    for d in (draw_b, draw_f):
        d.rounded_rectangle([cta_box[0] + 4, cta_box[1] + 4, cta_box[2] + 4, cta_box[3] + 4], radius=18, fill=(228, 224, 216))
        d.rounded_rectangle(cta_box, radius=18, fill=(217, 56, 30), outline=(180, 40, 20), width=3)
    draw_f.text((540, 1847), "🔥 XEM NGAY BẢN FULL TRÊN KÊNH!", fill=(255, 255, 255), font=font_cta, anchor="mm")

    return cv2.cvtColor(np.array(base_pil), cv2.COLOR_RGB2BGR), cv2.cvtColor(np.array(full_pil), cv2.COLOR_RGB2BGR)


def render_shorts_v3():
    base_bgr, full_bgr = create_shorts_canvases_v3()
    audio_wav = PROJ / "audio_v3" / "shorts.wav"
    out_mp4 = RENDERS_DIR / "tap01_lung_mat_shorts_v3.mp4"
    raw_video = out_mp4.with_name(out_mp4.stem + "_raw.mp4")
    sfx_wav = out_mp4.with_name(out_mp4.stem + "_sfx.wav")
    master_audio = out_mp4.with_name(out_mp4.stem + "_master.wav")

    fps = 24
    w, h = 1080, 1920
    total_ms = 36493
    total_frames = max(1, int(round(total_ms * fps / 1000.0)))
    ms_per_frame = 1000.0 / fps

    # Hand Rig scaled for vertical 1080x1920 (h = 580)
    hand_raw = cv2.imread(str(HAND_ASSET), cv2.IMREAD_UNCHANGED)
    hand_h = 580
    scale = hand_h / hand_raw.shape[0]
    hand_w = int(hand_raw.shape[1] * scale)
    hand_resized = cv2.resize(hand_raw, (hand_w, hand_h), interpolation=cv2.INTER_AREA)
    hand_bgr = hand_resized[:, :, :3]
    hand_alpha = (hand_resized[:, :, 3] / 255.0)[:, :, None].astype(np.float32)
    tip_x = int(round(9 * scale))
    tip_y = int(round(2 * scale))

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(str(raw_video), fourcc, fps, (w, h))

    print(f"\n[SHORTS V3] Rendering {total_frames} frames ({total_ms}ms) @ {fps}fps...")
    t0 = time.time()

    def stamp_hand(cv_frame, px, py):
        top_x = px - tip_x
        top_y = py - tip_y
        c_x0, c_y0 = max(0, top_x), max(0, top_y)
        c_x1, c_y1 = min(w, top_x + hand_w), min(h, top_y + hand_h)
        if c_x1 <= c_x0 or c_y1 <= c_y0:
            return cv_frame
        h_x0, h_y0 = c_x0 - top_x, c_y0 - top_y
        h_x1, h_y1 = h_x0 + (c_x1 - c_x0), h_y0 + (c_y1 - c_y0)
        out = cv_frame.copy()
        hb = hand_bgr[h_y0:h_y1, h_x0:h_x1]
        ha = hand_alpha[h_y0:h_y1, h_x0:h_x1]
        out[c_y0:c_y1, c_x0:c_x1] = (out[c_y0:c_y1, c_x0:c_x1] * (1.0 - ha) + hb * ha).astype(np.uint8)
        return out

    # SFX Cues for Shorts
    sfx_cues = [
        {"timeMs": 0, "type": "whoosh"},
        {"timeMs": 1500, "type": "pop"},
        {"timeMs": 5200, "type": "scribble", "durMs": 6000},
        {"timeMs": 13500, "type": "pop"},
        {"timeMs": 14500, "type": "scribble", "durMs": 5000},
        {"timeMs": 20200, "type": "pop"},
        {"timeMs": 21200, "type": "scribble", "durMs": 6000},
        {"timeMs": 30800, "type": "impact"},
    ]

    for fi in range(total_frames):
        cur_ms = fi * ms_per_frame
        frame = np.full((h, w, 3), (249, 246, 240), dtype=np.uint8)
        hand_pos = None

        # 1. Header (0 -> 1500ms)
        frame[30:175 + 4, 30:1050 + 4] = base_bgr[30:175 + 4, 30:1050 + 4]
        if cur_ms < 1500:
            p = cur_ms / 1500.0
            rx = int(30 + p * 1020)
            frame[30:175, 30:rx] = full_bgr[30:175, 30:rx]
            hand_pos = (rx, 105)
        else:
            frame[30:175, 30:1050] = full_bgr[30:175, 30:1050]

        # 2. Card 1 (1500 -> 13500ms)
        if cur_ms >= 1500:
            card_pop_dur = 380.0
            if cur_ms < 1500 + card_pop_dur:
                p = (cur_ms - 1500) / card_pop_dur
                scale = 0.84 + 0.16 * ease_out_back(p)
                pw, ph = 1000, 510
                sw, sh = max(1, int(round(pw * scale))), max(1, int(round(ph * scale)))
                crop = base_bgr[195:705, 40:1040]
                scaled = cv2.resize(crop, (sw, sh), interpolation=cv2.INTER_LINEAR)
                dx0 = max(0, 40 + (pw - sw) // 2)
                dy0 = max(0, 195 + (ph - sh) // 2)
                frame[dy0:dy0 + sh, dx0:dx0 + sw] = scaled
            else:
                frame[195:705 + 4, 40:1040 + 4] = base_bgr[195:705 + 4, 40:1040 + 4]
                if cur_ms < 13500:
                    p = (cur_ms - 1500) / 12000.0
                    rx = int(550 + p * 480)
                    frame[260:700, 540:rx] = full_bgr[260:700, 540:rx]
                    jitter = int(math.sin(p * 24 * math.pi) * 3)
                    hand_pos = (rx, 360 + int(p * 220) + jitter)
                else:
                    frame[195:705, 40:1040] = full_bgr[195:705, 40:1040]

        # 3. Card 2 (13500 -> 20200ms)
        if cur_ms >= 13500:
            card_pop_dur = 380.0
            if cur_ms < 13500 + card_pop_dur:
                p = (cur_ms - 13500) / card_pop_dur
                scale = 0.84 + 0.16 * ease_out_back(p)
                pw, ph = 1000, 510
                sw, sh = max(1, int(round(pw * scale))), max(1, int(round(ph * scale)))
                crop = base_bgr[730:1240, 40:1040]
                scaled = cv2.resize(crop, (sw, sh), interpolation=cv2.INTER_LINEAR)
                dx0 = max(0, 40 + (pw - sw) // 2)
                dy0 = max(0, 730 + (ph - sh) // 2)
                frame[dy0:dy0 + sh, dx0:dx0 + sw] = scaled
            else:
                frame[730:1240 + 4, 40:1040 + 4] = base_bgr[730:1240 + 4, 40:1040 + 4]
                if cur_ms < 20200:
                    p = (cur_ms - 13500) / 6700.0
                    rx = int(550 + p * 480)
                    frame[795:1230, 540:rx] = full_bgr[795:1230, 540:rx]
                    jitter = int(math.sin(p * 24 * math.pi) * 3)
                    hand_pos = (rx, 890 + int(p * 220) + jitter)
                else:
                    frame[730:1240, 40:1040] = full_bgr[730:1240, 40:1040]

        # 4. Card 3 (20200 -> 30800ms)
        if cur_ms >= 20200:
            card_pop_dur = 380.0
            if cur_ms < 20200 + card_pop_dur:
                p = (cur_ms - 20200) / card_pop_dur
                scale = 0.84 + 0.16 * ease_out_back(p)
                pw, ph = 1000, 510
                sw, sh = max(1, int(round(pw * scale))), max(1, int(round(ph * scale)))
                crop = base_bgr[1265:1775, 40:1040]
                scaled = cv2.resize(crop, (sw, sh), interpolation=cv2.INTER_LINEAR)
                dx0 = max(0, 40 + (pw - sw) // 2)
                dy0 = max(0, 1265 + (ph - sh) // 2)
                frame[dy0:dy0 + sh, dx0:dx0 + sw] = scaled
            else:
                frame[1265:1775 + 4, 40:1040 + 4] = base_bgr[1265:1775 + 4, 40:1040 + 4]
                if cur_ms < 30800:
                    p = (cur_ms - 20200) / 10600.0
                    rx = int(550 + p * 480)
                    frame[1330:1765, 540:rx] = full_bgr[1330:1765, 540:rx]
                    jitter = int(math.sin(p * 24 * math.pi) * 3)
                    hand_pos = (rx, 1420 + int(p * 220) + jitter)
                else:
                    frame[1265:1775, 40:1040] = full_bgr[1265:1775, 40:1040]

        # 5. CTA (30800 -> 36493ms)
        if cur_ms >= 30800:
            frame[1795:1900 + 4, 40:1040 + 4] = base_bgr[1795:1900 + 4, 40:1040 + 4]
            p = (cur_ms - 30800) / 5693.0
            rx = int(40 + min(1.0, p * 1.5) * 1000)
            frame[1795:1900, 40:rx] = full_bgr[1795:1900, 40:rx]
            if p < 0.7:
                hand_pos = (rx, 1847)

        if hand_pos is not None:
            frame = stamp_hand(frame, hand_pos[0], hand_pos[1])

        writer.write(frame)

    writer.release()
    print(f"[SHORTS V3] Silent video generated in {time.time() - t0:.1f}s")

    # Generate SFX track
    sr = 48000
    total_samples = int((total_ms / 1000.0) * sr)
    mix = np.zeros(total_samples, dtype=np.float32)

    def load_sfx(path: Path) -> np.ndarray:
        if not path.exists():
            return np.zeros(1, dtype=np.float32)
        cmd = ["ffmpeg", "-v", "error", "-i", str(path), "-f", "f32le", "-ac", "1", "-ar", str(sr), "-"]
        proc = subprocess.run(cmd, capture_output=True, check=True)
        return np.frombuffer(proc.stdout, dtype=np.float32)

    pop_snd = load_sfx(SFX_DIR / "pop.mp3") * 0.35
    whoosh_snd = load_sfx(SFX_DIR / "whoosh-short.mp3") * 0.30
    impact_snd = load_sfx(SFX_DIR / "impact-bass-1.mp3") * 0.40
    scribble_snd = load_sfx(SCRIBBLE_WAV) * 0.12

    def stamp_snd(snd, t_ms):
        st = int((t_ms / 1000.0) * sr)
        if st < total_samples and len(snd) > 0:
            en = min(total_samples, st + len(snd))
            mix[st:en] += snd[:en - st]

    for c in sfx_cues:
        if c["type"] == "pop": stamp_snd(pop_snd, c["timeMs"])
        elif c["type"] == "whoosh": stamp_snd(whoosh_snd, c["timeMs"])
        elif c["type"] == "impact": stamp_snd(impact_snd, c["timeMs"])
        elif c["type"] == "scribble" and len(scribble_snd) > 10:
            dur_samp = int((c.get("durMs", 1000) / 1000.0) * sr)
            st = int((c["timeMs"] / 1000.0) * sr)
            en = min(total_samples, st + dur_samp)
            if en > st:
                seg = en - st
                looped = np.tile(scribble_snd, int(math.ceil(seg / len(scribble_snd))))[:seg]
                fade = min(int(0.04 * sr), seg // 2)
                if fade > 0:
                    looped[:fade] *= np.linspace(0, 1, fade)
                    looped[-fade:] *= np.linspace(1, 0, fade)
                mix[st:en] += looped

    mix = np.clip(mix, -0.98, 0.98)
    from scipy.io import wavfile
    wavfile.write(str(sfx_wav), sr, (mix * 32767).astype(np.int16))

    # Mix audio
    cmd_mix = [
        "ffmpeg", "-y",
        "-i", str(audio_wav),
        "-i", str(sfx_wav),
        "-filter_complex",
        "[0:a]volume=1.0[v];[1:a]volume=0.9[s];[v][s]amix=inputs=2:weights=1 1:normalize=0:duration=first[aout]",
        "-map", "[aout]",
        "-ar", "48000",
        "-ac", "2",
        "-c:a", "pcm_s16le",
        str(master_audio)
    ]
    subprocess.run(cmd_mix, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Mux final video
    cmd_mux = [
        "ffmpeg", "-y",
        "-i", str(raw_video),
        "-i", str(master_audio),
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "256k",
        "-shortest",
        str(out_mp4)
    ]
    subprocess.run(cmd_mux, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    for p in (raw_video, sfx_wav, master_audio):
        p.unlink(missing_ok=True)

    print(f"\n[SUCCESS] Master Shorts V3 Exported: {out_mp4} ({out_mp4.stat().st_size / 1024 / 1024:.2f} MB)")
    return out_mp4


if __name__ == "__main__":
    render_shorts_v3()

"""
Build and Render Fast YouTube Shorts V2 (9:16 Vertical 1080x1920)
Engine: Card Reveal + Handwriting Whiteboard Engine
Duration: 30.12s
"""

import sys
import math
import time
import subprocess
from pathlib import Path
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

SCRIPT_DIR = Path(__file__).resolve().parent
PROJ = SCRIPT_DIR.parent
ROOT = PROJ.parent.parent

G = PROJ / "assets" / "gemini_downloaded"
RENDERS_DIR = PROJ / "renders_v2"
RENDERS_DIR.mkdir(parents=True, exist_ok=True)
HAND_ASSET = PROJ / "assets" / "user_clean_hand.png"

try:
    font_main_title = ImageFont.truetype("arialbd.ttf", 36)
    font_sub_title = ImageFont.truetype("arialbd.ttf", 22)
    font_card_header = ImageFont.truetype("arialbd.ttf", 24)
    font_card_bold = ImageFont.truetype("arialbd.ttf", 20)
    font_card_reg = ImageFont.truetype("arial.ttf", 18)
    font_cta = ImageFont.truetype("arialbd.ttf", 26)
except:
    font_main_title = font_sub_title = font_card_header = font_card_bold = font_card_reg = font_cta = ImageFont.load_default()

def fit_contain(im: Image.Image, max_w: int, max_h: int) -> Image.Image:
    w, h = im.size
    scale = min(max_w / w, max_h / h)
    return im.resize((max(1, int(round(w * scale))), max(1, int(round(h * scale)))), Image.Resampling.LANCZOS)

def ease_out_back(t: float) -> float:
    c1 = 1.70158
    c3 = c1 + 1
    return 1 + c3 * math.pow(t - 1, 3) + c1 * math.pow(t - 1, 2)

def create_shorts_canvases():
    w, h = 1080, 1920
    base_pil = Image.new("RGB", (w, h), (255, 255, 255))
    draw_b = ImageDraw.Draw(base_pil)
    full_pil = Image.new("RGB", (w, h), (255, 255, 255))
    draw_f = ImageDraw.Draw(full_pil)
    
    # 1. Top Header Banner
    h_box = [30, 30, 1050, 160]
    for d in (draw_b, draw_f):
        d.rounded_rectangle(h_box, radius=16, fill=(255, 243, 240), outline=(217, 56, 30), width=4)
    draw_f.text((540, 75), "3 SỰ THẬT ĐIÊN RỒ VỀ LỬNG MẬT", fill=(217, 56, 30), font=font_main_title, anchor="mm")
    draw_f.text((540, 120), "KẺ CHÍ PHÈO KHÔNG BIẾT SỢ BẤT KỲ AI TRÊN TRÁI ĐẤT", fill=(60, 60, 60), font=font_sub_title, anchor="mm")
    
    # Card 1: Fact 1 (Top)
    c1_box = [40, 185, 1040, 695]
    im1 = fit_contain(Image.open(G / "c3_badger_turn_180.png").convert("RGB"), 460, 420)
    for d, im_tgt in ((draw_b, base_pil), (draw_f, full_pil)):
        d.rounded_rectangle(c1_box, radius=14, fill=(255, 255, 255), outline=(43, 108, 176), width=3)
        d.rectangle([43, 188, 1037, 235], fill=(240, 246, 255))
        d.text((60, 212), "1. BỘ GIÁP 6MM XOAY 180 ĐỘ TRONG DA", fill=(43, 108, 176), font=font_card_header, anchor="lm")
        im_tgt.paste(im1, (60, 250))
        d.rectangle([59, 249, 60 + im1.width, 250 + im1.height], outline=(220, 225, 230), width=1)
        d.rounded_rectangle(c1_box, radius=14, outline=(43, 108, 176), width=3)
        
    draw_f.text((540, 270), "• Da dày 6mm trơn tuột:", fill=(30, 30, 30), font=font_card_bold)
    draw_f.text((555, 305), "Răng nanh sư tử cắn vào bị trượt\nKhông thể xuyên thủng lớp sừng", fill=(70, 70, 70), font=font_card_reg)
    draw_f.text((540, 375), "• Xoay 180 độ trong bao da:", fill=(217, 56, 30), font=font_card_bold)
    draw_f.text((555, 410), "Bị cắn gáy liền quay ngoắt đầu\nNgoạm đứt mũi báo hoa phản đòn!", fill=(70, 70, 70), font=font_card_reg)
    draw_f.text((540, 480), "• Vũ khí không góc chết:", fill=(43, 108, 176), font=font_card_bold)
    draw_f.text((555, 515), "Biến mọi thế bị bắt thành bẫy tử thần!", fill=(70, 70, 70), font=font_card_reg)
    
    # Card 2: Fact 2 (Middle)
    c2_box = [40, 720, 1040, 1230]
    im2 = fit_contain(Image.open(G / "c4_badger_sleeping_venom.png").convert("RGB"), 460, 420)
    for d, im_tgt in ((draw_b, base_pil), (draw_f, full_pil)):
        d.rounded_rectangle(c2_box, radius=14, fill=(255, 255, 255), outline=(130, 60, 160), width=3)
        d.rectangle([43, 723, 1037, 770], fill=(250, 242, 255))
        d.text((60, 747), "2. MIỄN NHIỄM NỌC ĐỘC & GIẤC NGỦ THẦN THÁNH", fill=(130, 60, 160), font=font_card_header, anchor="lm")
        im_tgt.paste(im2, (60, 785))
        d.rectangle([59, 784, 60 + im2.width, 785 + im2.height], outline=(220, 225, 230), width=1)
        d.rounded_rectangle(c2_box, radius=14, outline=(130, 60, 160), width=3)
        
    draw_f.text((540, 805), "• Coi rắn độc là đồ ăn vặt:", fill=(30, 30, 30), font=font_card_bold)
    draw_f.text((555, 840), "Hổ mang chúa, rắn lục, mamba đen\nĐều bị ngoạm đứt đầu nuốt chửng", fill=(70, 70, 70), font=font_card_reg)
    draw_f.text((540, 910), "• Đột biến gen kháng độc:", fill=(130, 60, 160), font=font_card_bold)
    draw_f.text((555, 945), "Thụ thể thần kinh không dính nọc\nMiễn nhiễm độc tố thần kinh tự nhiên", fill=(70, 70, 70), font=font_card_reg)
    draw_f.text((540, 1015), "• Giấc ngủ giải độc 2 tiếng:", fill=(47, 133, 90), font=font_card_bold)
    draw_f.text((555, 1050), "Bị cắn chỉ lăn ra ngủ mê man\nTỉnh dậy lại xơi nốt nửa con rắn!", fill=(70, 70, 70), font=font_card_reg)
    
    # Card 3: Fact 3 (Bottom)
    c3_box = [40, 1255, 1040, 1765]
    im3 = fit_contain(Image.open(G / "c5_stoffel_escape.png").convert("RGB"), 460, 420)
    for d, im_tgt in ((draw_b, base_pil), (draw_f, full_pil)):
        d.rounded_rectangle(c3_box, radius=14, fill=(255, 255, 255), outline=(47, 133, 90), width=3)
        d.rectangle([43, 1258, 1037, 1305], fill=(240, 252, 245))
        d.text((60, 1282), "3. THIÊN TÀI VƯỢT NGỤC STOFFEL (IQ ĐỈNH CAO)", fill=(47, 133, 90), font=font_card_header, anchor="lm")
        im_tgt.paste(im3, (60, 1320))
        d.rectangle([59, 1319, 60 + im3.width, 1320 + im3.height], outline=(220, 225, 230), width=1)
        d.rounded_rectangle(c3_box, radius=14, outline=(47, 133, 90), width=3)
        
    draw_f.text((540, 1340), "• Khả năng dùng công cụ siêu đẳng:", fill=(30, 30, 30), font=font_card_bold)
    draw_f.text((555, 1375), "Xếp đá làm thang trèo tường\nDùng que cây, chổi làm đòn bẩy", fill=(70, 70, 70), font=font_card_reg)
    draw_f.text((540, 1445), "• Đắp bóng bùn phơi khô:", fill=(47, 133, 90), font=font_card_bold)
    draw_f.text((555, 1480), "Khi hết đá, tự nặn bóng bùn\nLăn qua rào điện thoát ra ngoài!", fill=(70, 70, 70), font=font_card_reg)
    draw_f.text((540, 1550), "• Trí thông minh giải đố:", fill=(217, 56, 30), font=font_card_bold)
    draw_f.text((555, 1585), "Top đầu thông minh thế giới loài vật!", fill=(70, 70, 70), font=font_card_reg)
    
    # 5. Bottom CTA Banner
    cta_box = [40, 1785, 1040, 1890]
    for d in (draw_b, draw_f):
        d.rounded_rectangle(cta_box, radius=16, fill=(217, 56, 30), outline=(180, 40, 20), width=3)
    draw_f.text((540, 1837), "🔥 XEM NGAY BẢN FULL TRÊN KÊNH!", fill=(255, 255, 255), font=font_cta, anchor="mm")
    
    return cv2.cvtColor(np.array(base_pil), cv2.COLOR_RGB2BGR), cv2.cvtColor(np.array(full_pil), cv2.COLOR_RGB2BGR)

def render_shorts_v2():
    base_bgr, full_bgr = create_shorts_canvases()
    audio_wav = PROJ / "audio_fast" / "shorts.wav"
    out_mp4 = RENDERS_DIR / "tap01_lung_mat_shorts_v2.mp4"
    raw_video = out_mp4.with_name(out_mp4.stem + "_raw.mp4")
    
    fps = 24
    w, h = 1080, 1920
    total_ms = 30118
    total_frames = max(1, int(round(total_ms * fps / 1000.0)))
    ms_per_frame = 1000.0 / fps
    
    # Load Hand Rig for vertical 1080x1920
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
    
    print(f"\n[SHORTS V2] Rendering {total_frames} frames ({total_ms}ms)...")
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
        
    for fi in range(total_frames):
        cur_ms = fi * ms_per_frame
        frame = np.full((h, w, 3), 255, dtype=np.uint8)
        hand_pos = None
        
        # Header (0 -> 1500ms)
        frame[30:160, 30:1050] = base_bgr[30:160, 30:1050]
        if cur_ms < 1500:
            p = cur_ms / 1500.0
            rx = int(30 + p * 1020)
            frame[30:160, 30:rx] = full_bgr[30:160, 30:rx]
            hand_pos = (rx, 95)
        else:
            frame[30:160, 30:1050] = full_bgr[30:160, 30:1050]
            
        # Card 1 (1500 -> 10000ms)
        if cur_ms >= 1500:
            frame[185:695, 40:1040] = base_bgr[185:695, 40:1040]
            if cur_ms < 10000:
                p = (cur_ms - 1500) / 8500.0
                rx = int(540 + p * 500)
                frame[250:680, 530:rx] = full_bgr[250:680, 530:rx]
                jitter = int(math.sin(p * 25 * math.pi) * 3)
                hand_pos = (rx, 350 + int(p * 200) + jitter)
            else:
                frame[185:695, 40:1040] = full_bgr[185:695, 40:1040]
                
        # Card 2 (10000 -> 18500ms)
        if cur_ms >= 10000:
            frame[720:1230, 40:1040] = base_bgr[720:1230, 40:1040]
            if cur_ms < 18500:
                p = (cur_ms - 10000) / 8500.0
                rx = int(540 + p * 500)
                frame[780:1210, 530:rx] = full_bgr[780:1210, 530:rx]
                jitter = int(math.sin(p * 25 * math.pi) * 3)
                hand_pos = (rx, 890 + int(p * 200) + jitter)
            else:
                frame[720:1230, 40:1040] = full_bgr[720:1230, 40:1040]
                
        # Card 3 (18500 -> 26500ms)
        if cur_ms >= 18500:
            frame[1255:1765, 40:1040] = base_bgr[1255:1765, 40:1040]
            if cur_ms < 26500:
                p = (cur_ms - 18500) / 8000.0
                rx = int(540 + p * 500)
                frame[1320:1740, 530:rx] = full_bgr[1320:1740, 530:rx]
                jitter = int(math.sin(p * 25 * math.pi) * 3)
                hand_pos = (rx, 1420 + int(p * 200) + jitter)
            else:
                frame[1255:1765, 40:1040] = full_bgr[1255:1765, 40:1040]
                
        # CTA (26500 -> 30118ms)
        if cur_ms >= 26500:
            frame[1785:1890, 40:1040] = base_bgr[1785:1890, 40:1040]
            p = (cur_ms - 26500) / 3618.0
            rx = int(40 + p * 1000)
            frame[1785:1890, 40:rx] = full_bgr[1785:1890, 40:rx]
            hand_pos = (rx, 1837)
            
        if hand_pos is not None:
            frame = stamp_hand(frame, hand_pos[0], hand_pos[1])
        writer.write(frame)
        
    writer.release()
    print(f"[SHORTS V2] Silent video generated in {time.time() - t0:.1f}s")
    
    # Mux audio
    cmd_mux = [
        "ffmpeg", "-y",
        "-i", str(raw_video),
        "-i", str(audio_wav),
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "20",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        str(out_mp4)
    ]
    subprocess.run(cmd_mux, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if raw_video.exists():
        try:
            raw_video.unlink()
        except:
            pass
    print(f"[SUCCESS] Master Shorts V2 Exported: {out_mp4}")
    return out_mp4

if __name__ == "__main__":
    render_shorts_v2()

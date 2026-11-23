"""
Build Canvas, Annotation, and Render YouTube Shorts (9:16 1080x1920)
Project: Tap 01 - Lung Mat (Honey Badger)
Duration: 50.70 seconds
"""

import sys
import json
import time
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont

SCRIPT_DIR = Path(__file__).resolve().parent
PROJ = SCRIPT_DIR.parent
ROOT = PROJ.parent.parent

sys.path.insert(0, str(ROOT / "src" / "render"))
from hybrid_whiteboard_renderer import HybridWhiteboardRenderer

G = PROJ / "assets" / "gemini_downloaded"
OUTPUT_DIR = PROJ / "assets" / "scenes_composed"
ANNOTATIONS_DIR = PROJ / "annotations"
RENDERS_DIR = PROJ / "renders"

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

def build_shorts_canvas():
    w, h = 1080, 1920
    canvas = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(canvas)
    
    # 1. Top Header Banner
    h_box = [30, 30, 1050, 160]
    draw.rounded_rectangle(h_box, radius=16, fill=(255, 243, 240), outline=(217, 56, 30), width=4)
    draw.text((540, 75), "3 SỰ THẬT ĐIÊN RỒ VỀ LỬNG MẬT", fill=(217, 56, 30), font=font_main_title, anchor="mm")
    draw.text((540, 120), "KẺ CHÍ PHÈO KHÔNG BIẾT SỢ BẤT KỲ AI TRÊN TRÁI ĐẤT", fill=(60, 60, 60), font=font_sub_title, anchor="mm")
    
    # Card 1: Fact 1 (Top) - Y: 190 to 680
    c1_box = [40, 185, 1040, 695]
    draw.rounded_rectangle(c1_box, radius=14, fill=(255, 255, 255), outline=(43, 108, 176), width=3)
    draw.rectangle([43, 188, 1037, 235], fill=(240, 246, 255))
    draw.text((60, 212), "1. BỘ GIÁP 6MM XOAY 180 ĐỘ TRONG DA", fill=(43, 108, 176), font=font_card_header, anchor="lm")
    
    im1 = fit_contain(Image.open(G / "c3_badger_turn_180.png").convert("RGB"), 460, 420)
    canvas.paste(im1, (60, 250))
    draw.rectangle([59, 249, 60 + im1.width, 250 + im1.height], outline=(220, 225, 230), width=1)
    
    draw.text((540, 270), "• Da dày 6mm trơn tuột:", fill=(30, 30, 30), font=font_card_bold)
    draw.text((555, 305), "Răng nanh sư tử cắn vào bị trượt\nKhông thể xuyên thủng lớp sừng", fill=(70, 70, 70), font=font_card_reg)
    draw.text((540, 375), "• Xoay 180 độ trong bao da:", fill=(217, 56, 30), font=font_card_bold)
    draw.text((555, 410), "Bị cắn gáy liền quay ngoắt đầu\nNgoạm đứt mũi báo hoa phản đòn!", fill=(70, 70, 70), font=font_card_reg)
    draw.text((540, 480), "• Vũ khí không góc chết:", fill=(43, 108, 176), font=font_card_bold)
    draw.text((555, 515), "Biến mọi thế bị bắt thành bẫy tử thần!", fill=(70, 70, 70), font=font_card_reg)
    draw.rounded_rectangle(c1_box, radius=14, outline=(43, 108, 176), width=3)
    
    # Card 2: Fact 2 (Middle) - Y: 720 to 1230
    c2_box = [40, 720, 1040, 1230]
    draw.rounded_rectangle(c2_box, radius=14, fill=(255, 255, 255), outline=(130, 60, 160), width=3)
    draw.rectangle([43, 723, 1037, 770], fill=(250, 242, 255))
    draw.text((60, 747), "2. MIỄN NHIỄM NỌC ĐỘC & GIẤC NGỦ THẦN THÁNH", fill=(130, 60, 160), font=font_card_header, anchor="lm")
    
    im2 = fit_contain(Image.open(G / "c4_badger_sleeping_venom.png").convert("RGB"), 460, 420)
    canvas.paste(im2, (60, 785))
    draw.rectangle([59, 784, 60 + im2.width, 785 + im2.height], outline=(220, 225, 230), width=1)
    
    draw.text((540, 805), "• Coi rắn độc là đồ ăn vặt:", fill=(30, 30, 30), font=font_card_bold)
    draw.text((555, 840), "Hổ mang chúa, rắn lục, mamba đen\nĐều bị ngoạm đứt đầu nuốt chửng", fill=(70, 70, 70), font=font_card_reg)
    draw.text((540, 910), "• Đột biến gen kháng độc:", fill=(130, 60, 160), font=font_card_bold)
    draw.text((555, 945), "Thụ thể thần kinh không dính nọc\nMiễn nhiễm độc tố thần kinh tự nhiên", fill=(70, 70, 70), font=font_card_reg)
    draw.text((540, 1015), "• Giấc ngủ giải độc 2 tiếng:", fill=(47, 133, 90), font=font_card_bold)
    draw.text((555, 1050), "Bị cắn chỉ lăn ra ngủ mê man\nTỉnh dậy lại xơi nốt nửa con rắn!", fill=(70, 70, 70), font=font_card_reg)
    draw.rounded_rectangle(c2_box, radius=14, outline=(130, 60, 160), width=3)
    
    # Card 3: Fact 3 (Bottom) - Y: 1255 to 1765
    c3_box = [40, 1255, 1040, 1765]
    draw.rounded_rectangle(c3_box, radius=14, fill=(255, 255, 255), outline=(47, 133, 90), width=3)
    draw.rectangle([43, 1258, 1037, 1305], fill=(240, 252, 245))
    draw.text((60, 1282), "3. THIÊN TÀI VƯỢT NGỤC STOFFEL (IQ ĐỈNH CAO)", fill=(47, 133, 90), font=font_card_header, anchor="lm")
    
    im3 = fit_contain(Image.open(G / "c5_stoffel_escape.png").convert("RGB"), 460, 420)
    canvas.paste(im3, (60, 1320))
    draw.rectangle([59, 1319, 60 + im3.width, 1320 + im3.height], outline=(220, 225, 230), width=1)
    
    draw.text((540, 1340), "• Khả năng dùng công cụ siêu đẳng:", fill=(30, 30, 30), font=font_card_bold)
    draw.text((555, 1375), "Xếp đá làm thang trèo tường\nDùng que cây, chổi làm đòn bẩy", fill=(70, 70, 70), font=font_card_reg)
    draw.text((540, 1445), "• Đắp bóng bùn phơi khô:", fill=(47, 133, 90), font=font_card_bold)
    draw.text((555, 1480), "Khi hết đá, tự nặn bóng bùn\nLăn qua rào điện thoát ra ngoài!", fill=(70, 70, 70), font=font_card_reg)
    draw.text((540, 1550), "• Trí thông minh giải đố:", fill=(217, 56, 30), font=font_card_bold)
    draw.text((555, 1585), "Top đầu thông minh thế giới loài vật!", fill=(70, 70, 70), font=font_card_reg)
    draw.rounded_rectangle(c3_box, radius=14, outline=(47, 133, 90), width=3)
    
    # 5. Bottom CTA Banner - Y: 1785 to 1890
    cta_box = [40, 1785, 1040, 1890]
    draw.rounded_rectangle(cta_box, radius=16, fill=(217, 56, 30), outline=(180, 40, 20), width=3)
    draw.text((540, 1837), "🔥 XEM NGAY BẢN FULL 9 PHÚT TRÊN KÊNH!", fill=(255, 255, 255), font=font_cta, anchor="mm")
    
    canvas_path = OUTPUT_DIR / "shorts_canvas.png"
    canvas.save(canvas_path)
    print(f"[SHORTS] Canvas saved: {canvas_path}")
    
    # Annotation timeline for 50.70s (50700ms)
    ann = {
        "version": "1.0",
        "canvas": {"width": 1080, "height": 1920},
        "sceneDurationMs": 50700,
        "elements": [
            {"id": "sh_header", "region": {"x": 30, "y": 30, "width": 1020, "height": 130}, "reveal": {"startMs": 0, "durationMs": 1500}},
            {"id": "sh_card1", "region": {"x": 40, "y": 185, "width": 1000, "height": 510}, "reveal": {"startMs": 1500, "durationMs": 15000}},
            {"id": "sh_card2", "region": {"x": 40, "y": 720, "width": 1000, "height": 510}, "reveal": {"startMs": 16500, "durationMs": 15000}},
            {"id": "sh_card3", "region": {"x": 40, "y": 1255, "width": 1000, "height": 510}, "reveal": {"startMs": 31500, "durationMs": 14000}},
            {"id": "sh_cta", "region": {"x": 40, "y": 1785, "width": 1000, "height": 105}, "reveal": {"startMs": 45500, "durationMs": 5200}}
        ]
    }
    ann_path = ANNOTATIONS_DIR / "shorts.annotation.json"
    with open(ann_path, "w", encoding="utf-8") as f:
        json.dump(ann, f, indent=2, ensure_ascii=False)
    print(f"[SHORTS] Annotation saved: {ann_path}")
    return canvas_path, ann_path

def render_shorts():
    c_p = OUTPUT_DIR / "shorts_canvas.png"
    spec_p = PROJ / "specs" / "shorts_spec.json"
    audio_p = PROJ / "audio" / "shorts.wav"
    out_p = RENDERS_DIR / "tap01_lung_mat_shorts.mp4"
    hand_p = ROOT / "assets" / "hands" / "hand-marker-right.png"
    if not hand_p.exists():
        hand_p = PROJ / "assets" / "user_clean_hand.png"
    
    print("\n=======================================================")
    print("[HYBRID RENDER SHORTS] Rendering 9:16 Vertical Shorts Video...")
    print(f"Canvas: {c_p}")
    print(f"Spec  : {spec_p}")
    print(f"Audio : {audio_p}")
    print(f"Output: {out_p}")
    print("=======================================================")
    
    t0 = time.time()
    renderer = HybridWhiteboardRenderer(spec_p, c_p, hand_path=hand_p, fps=24)
    renderer.render(out_p, audio_p)
    print(f"[SUCCESS] Shorts Video Rendered in {time.time() - t0:.1f}s -> {out_p}")
    return out_p

if __name__ == "__main__":
    render_shorts()

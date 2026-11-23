"""
Build Canvases & Annotations for Tap 01: Lung Mat (Honey Badger)
Master Production with Colorful Comic 2D Illustrations + Whiteboard QA Guarantee
"""

import sys
import json
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont

SCRIPT_DIR = Path(__file__).resolve().parent
PROJ = SCRIPT_DIR.parent
ROOT = PROJ.parent.parent

G = PROJ / "assets" / "gemini_downloaded"
OUTPUT_DIR = PROJ / "assets" / "scenes_composed"
ANNOTATIONS_DIR = PROJ / "annotations"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
ANNOTATIONS_DIR.mkdir(parents=True, exist_ok=True)

try:
    font_title = ImageFont.truetype("arialbd.ttf", 22)
    font_header = ImageFont.truetype("arialbd.ttf", 15)
    font_bold = ImageFont.truetype("arialbd.ttf", 14)
    font_reg = ImageFont.truetype("arial.ttf", 13)
    font_reg_bold = ImageFont.truetype("arialbd.ttf", 13)
except:
    font_title = font_header = font_bold = font_reg = font_reg_bold = ImageFont.load_default()

def fit_contain(im: Image.Image, max_w: int, max_h: int) -> Image.Image:
    w, h = im.size
    scale = min(max_w / w, max_h / h)
    return im.resize((max(1, int(round(w * scale))), max(1, int(round(h * scale)))), Image.Resampling.LANCZOS)

def draw_centered_header(draw: ImageDraw.Draw, title_text: str):
    bbox = draw.textbbox((0, 0), title_text, font=font_title)
    t_w = bbox[2] - bbox[0]
    t_h = bbox[3] - bbox[1]
    
    pad_x = 28
    pad_y = 8
    box_w = t_w + 2 * pad_x
    box_h = t_h + 2 * pad_y
    
    box_x0 = (1280 - box_w) // 2
    box_y0 = 10
    box_x1 = box_x0 + box_w
    box_y1 = box_y0 + box_h
    
    draw.rounded_rectangle([box_x0, box_y0, box_x1, box_y1], radius=8,
                           fill=(250, 248, 242), outline=(40, 40, 40), width=2)
    draw.text((640, box_y0 + box_h // 2), title_text, fill=(35, 35, 35), font=font_title, anchor="mm")
    return {"x": box_x0, "y": box_y0, "width": box_w, "height": box_h}

BOX_LEFT = [20, 64, 628, 706]
BOX_RIGHT = [652, 64, 1260, 706]

def render_scene_box(canvas: Image.Image, draw: ImageDraw.Draw, box: list[int],
                     header_text: str, color: tuple, header_bg: tuple,
                     img_path: Path, bullet_points: list):
    if not img_path.exists():
        raise FileNotFoundError(f"[CRITICAL QA ERROR] Image missing: {img_path}")
        
    x0, y0, x1, y1 = box
    w = x1 - x0
    h = y1 - y0
    
    # Outer frame
    draw.rounded_rectangle(box, radius=8, fill=(255, 255, 255), outline=color, width=2)
    # Header bar
    draw.rectangle([x0 + 2, y0 + 2, x1 - 2, y0 + 34], fill=header_bg)
    draw.text((x0 + 16, y0 + 18), header_text, fill=color, font=font_header, anchor="lm")
    
    # Image container (570 x 280)
    im_raw = Image.open(img_path).convert("RGB")
    im = fit_contain(im_raw, w - 32, 280)
    im_x = x0 + (w - im.width) // 2
    im_y = y0 + 44
    canvas.paste(im, (im_x, im_y))
    draw.rectangle([im_x - 1, im_y - 1, im_x + im.width, im_y + im.height], outline=(220, 225, 230), width=1)
    
    # Bullet points below image
    ty = im_y + im.height + 18
    tx = x0 + 20
    for bp in bullet_points:
        draw.text((tx, ty), bp["title"], fill=bp.get("color", (30, 30, 30)), font=font_bold)
        ty += 22
        lines = bp["desc"].split("\n")
        for line in lines:
            draw.text((tx + 12, ty), line, fill=(70, 70, 70), font=font_reg)
            ty += 18
        ty += bp.get("gap", 10)
        
    # Re-stroke outer border
    draw.rounded_rectangle(box, radius=8, outline=color, width=2)

def qa_verify_canvas(canvas_img: Image.Image, boxes: list[list[int]], scene_id: str):
    arr = np.array(canvas_img)
    diff = np.sum(np.abs(arr.astype(np.int16) - np.array([255, 255, 255])), axis=2)
    for i, b in enumerate(boxes):
        x0, y0, x1, y1 = b
        crop_diff = diff[y0+38:y1-10, x0+10:x1-10]
        content_pixels = (crop_diff > 25).sum()
        total_pixels = crop_diff.size
        ratio = content_pixels / total_pixels
        if ratio < 0.05:
            raise RuntimeError(f"[QA FAILED] Scene {scene_id} Box {i+1} is EMPTY! (content ratio: {ratio:.1%})")
        print(f"  [QA PASSED] Scene {scene_id} Box {i+1}: {content_pixels} content px ({ratio:.1%})")

def build_scene01():
    canvas = Image.new("RGB", (1280, 720), (255, 255, 255))
    draw = ImageDraw.Draw(canvas)
    h_reg = draw_centered_header(draw, "PHẦN 1: BÁ CHỦ LỲ LỢM & CƠN ÁC MỘNG CỦA CHÚA SƠN LÂM")
    
    render_scene_box(canvas, draw, BOX_LEFT, "1. GÃ CHÍ PHÈO THẢO NGUYÊN (MELLIVORA CAPENSIS)",
                     (217, 56, 30), (255, 243, 240),
                     G / "c1_badger_thug_sunglasses.png",
                     [
                         {"title": "• Kích thước khiêm tốn - Khí phách ngút trời:",
                          "desc": "Chỉ dài 60-70cm, nặng vỏn vẹn 10-14kg\nNhưng mang phong thái bá chủ không sợ bất kỳ ai",
                          "gap": 8},
                         {"title": "• Kỷ lục Guinness thế giới vinh danh:",
                          "desc": "Được công nhận là 'Sinh vật không biết sợ nhất hành tinh'\nSẵn sàng đối đầu bất kỳ loài thú săn mồi nào",
                          "gap": 8},
                         {"title": "• Phương châm sống kinh điển:",
                          "desc": "Sống là chiến đấu, không lùi bước trước hiểm nguy!",
                          "color": (217, 56, 30), "gap": 6}
                     ])
                     
    render_scene_box(canvas, draw, BOX_RIGHT, "2. SƯ TỬ VÀ BÁO HOA CŨNG PHẢI NHƯỢNG BỘ",
                     (43, 108, 176), (240, 246, 255),
                     G / "c1_lions_sweating_scared.png",
                     [
                         {"title": "• Chúa sơn lâm to lớn cũng e dè:",
                          "desc": "Nặng gấp 15 lần nhưng không bao giờ muốn đụng độ\nMỗi lần chạm mặt đều chủ động né sang một bên",
                          "gap": 8},
                         {"title": "• Cái giá đánh đổi quá đắt:",
                          "desc": "Tốn cả tiếng vật lộn mệt đứt hơi, rách môi mẻ vuốt\nĐổi lại chỉ là miếng thịt dai nhách đầy mùi hôi hám",
                          "gap": 8},
                         {"title": "• Tính khí trả đũa khốc liệt:",
                          "desc": "Ai trót đụng vào sẽ bị nó đuổi theo cắn xé tới cùng!",
                          "color": (43, 108, 176), "gap": 6}
                     ])
                     
    qa_verify_canvas(canvas, [BOX_LEFT, BOX_RIGHT], "01")
    canvas.save(OUTPUT_DIR / "scene01_canvas.png")
    
    ann = {
        "version": "1.0",
        "canvas": {"width": 1280, "height": 720},
        "sceneDurationMs": 65293,
        "elements": [
            {"id": "s01_header", "region": h_reg, "reveal": {"startMs": 0, "durationMs": 2000}},
            {"id": "s01_left", "region": {"x": 20, "y": 64, "width": 608, "height": 642}, "reveal": {"startMs": 2000, "durationMs": 31000}},
            {"id": "s01_right", "region": {"x": 652, "y": 64, "width": 608, "height": 642}, "reveal": {"startMs": 33000, "durationMs": 32293}}
        ]
    }
    with open(ANNOTATIONS_DIR / "scene01.annotation.json", "w", encoding="utf-8") as f:
        json.dump(ann, f, indent=2, ensure_ascii=False)
    print("Scene 01 Built & Verified.")

def build_scene02():
    canvas = Image.new("RGB", (1280, 720), (255, 255, 255))
    draw = ImageDraw.Draw(canvas)
    h_reg = draw_centered_header(draw, "PHẦN 2: BỘ GIÁP CAO SU 6MM & CƠ THỂ BẤT HOẠI")
    
    render_scene_box(canvas, draw, BOX_LEFT, "1. THỂ LỰC PHI THƯỜNG & KHUNG XƯƠNG ĐẶC (STR 85)",
                     (47, 133, 90), (240, 252, 245),
                     G / "c2_badger_muscles_strength.png",
                     [
                         {"title": "• Thể lực bền bỉ vô tận:",
                          "desc": "Chạy rong ruổi hàng chục km khắp thảo nguyên săn mồi\nCơ bắp dẻo dai giúp vận động liên tục không mệt mỏi",
                          "gap": 8},
                         {"title": "• Khung xương nén mật độ cao:",
                          "desc": "Chịu được cú vồ đập nghìn cân của mãnh thú săn mồi\nCổ to chắc nịch bảo vệ hoàn hảo đốt sống cổ",
                          "gap": 8},
                         {"title": "• Chỉ số chiến binh toàn diện:",
                          "desc": "Sức bền 85/100 - Bền bỉ vượt trội mọi loài săn mồi!",
                          "color": (47, 133, 90), "gap": 6}
                     ])
                     
    render_scene_box(canvas, draw, BOX_RIGHT, "2. BỘ GIÁP DA CAO SU DÀY 6MM TRƠN TUỘT (DEF 99)",
                     (180, 80, 30), (255, 248, 240),
                     G / "c2_badger_rubber_armor.png",
                     [
                         {"title": "• Lớp da cao su dày 6mm bất khả xâm phạm:",
                          "desc": "Cấu tạo từ mô liên kết collagen dày đặc và chất sừng\nRăng nanh sư tử cắn vào bị trượt, gai nhím gãy vụn",
                          "gap": 8},
                         {"title": "• Da lỏng lẻo như áo khoác rộng thùng thình:",
                          "desc": "Cơ thịt trượt tự do bên dưới mà không bị tổn thương\nKẻ thù ngậm chặt lớp da ngoài nhưng bên trong vẫn an toàn",
                          "gap": 8},
                         {"title": "• Phòng thủ tuyệt đối DEF 99:",
                          "desc": "Áo giáp sinh học thần kỳ bảo vệ tính mạng!",
                          "color": (180, 80, 30), "gap": 6}
                     ])
                     
    qa_verify_canvas(canvas, [BOX_LEFT, BOX_RIGHT], "02")
    canvas.save(OUTPUT_DIR / "scene02_canvas.png")
    
    ann = {
        "version": "1.0",
        "canvas": {"width": 1280, "height": 720},
        "sceneDurationMs": 102885,
        "elements": [
            {"id": "s02_header", "region": h_reg, "reveal": {"startMs": 0, "durationMs": 2000}},
            {"id": "s02_left", "region": {"x": 20, "y": 64, "width": 608, "height": 642}, "reveal": {"startMs": 2000, "durationMs": 50000}},
            {"id": "s02_right", "region": {"x": 652, "y": 64, "width": 608, "height": 642}, "reveal": {"startMs": 52000, "durationMs": 50885}}
        ]
    }
    with open(ANNOTATIONS_DIR / "scene02.annotation.json", "w", encoding="utf-8") as f:
        json.dump(ann, f, indent=2, ensure_ascii=False)
    print("Scene 02 Built & Verified.")

def build_scene03():
    canvas = Image.new("RGB", (1280, 720), (255, 255, 255))
    draw = ImageDraw.Draw(canvas)
    h_reg = draw_centered_header(draw, "PHẦN 3: TUYỆT KỸ XOAY 180 ĐỘ & VŨ KHÍ TẤN CÔNG BẠO TÀN")
    
    render_scene_box(canvas, draw, BOX_LEFT, "1. TUYỆT KỸ XOAY 180 ĐỘ TRONG BAO DA PHẢN ĐÒN",
                     (217, 56, 30), (255, 243, 240),
                     G / "c3_badger_turn_180.png",
                     [
                         {"title": "• Cấu trúc giải phẫu độc nhất vô nhị:",
                          "desc": "Xoay toàn bộ thân hình 180 độ ngay bên trong túi da\nBiến tư thế bị khống chế thành đòn phản công chí mạng",
                          "gap": 8},
                         {"title": "• Đòn cắn ngược bất ngờ vào mũi kẻ thù:",
                          "desc": "Báo hoa ngậm gáy liền bị quay đầu đớp thẳng vào mũi\nKhiến kẻ săn mồi đau đớn hoảng loạn nhả ra ngay tức khắc",
                          "gap": 8},
                         {"title": "• Không góc chết phòng ngự:",
                          "desc": "Bất cứ vị trí nào bị tóm đều biến thành tử địa của kẻ địch!",
                          "color": (217, 56, 30), "gap": 6}
                     ])
                     
    render_scene_box(canvas, draw, BOX_RIGHT, "2. MÓNG VUỐT 5CM & BỘ HÀM PHÁ VỠ CẢ MAI RÙA",
                     (43, 108, 176), (240, 246, 255),
                     G / "c3_badger_sharp_claws.png",
                     [
                         {"title": "• Cặp móng vuốt hình lưỡi liềm dài 5cm:",
                          "desc": "Đào bới tổ mối cứng như bê tông chỉ trong vài phút\nCào xé dữ dội gây thương tích nặng nề cho đối thủ",
                          "gap": 8},
                         {"title": "• Lực cắn nghiền nát xương và mai rùa:",
                          "desc": "Răng sắc nhọn kết hợp cơ hàm cực khỏe đập vỡ mai rùa\nĂn trọn vẹn cả xương tủy không để sót calo nào",
                          "gap": 8},
                         {"title": "• Tấn công điểm yếu nhạy cảm:",
                          "desc": "Nhắm thẳng vào mắt và hạ bộ kẻ thù để vô hiệu hóa!",
                          "color": (43, 108, 176), "gap": 6}
                     ])
                     
    qa_verify_canvas(canvas, [BOX_LEFT, BOX_RIGHT], "03")
    canvas.save(OUTPUT_DIR / "scene03_canvas.png")
    
    ann = {
        "version": "1.0",
        "canvas": {"width": 1280, "height": 720},
        "sceneDurationMs": 103655,
        "elements": [
            {"id": "s03_header", "region": h_reg, "reveal": {"startMs": 0, "durationMs": 2000}},
            {"id": "s03_left", "region": {"x": 20, "y": 64, "width": 608, "height": 642}, "reveal": {"startMs": 2000, "durationMs": 50000}},
            {"id": "s03_right", "region": {"x": 652, "y": 64, "width": 608, "height": 642}, "reveal": {"startMs": 52000, "durationMs": 51655}}
        ]
    }
    with open(ANNOTATIONS_DIR / "scene03.annotation.json", "w", encoding="utf-8") as f:
        json.dump(ann, f, indent=2, ensure_ascii=False)
    print("Scene 03 Built & Verified.")

def build_scene04():
    canvas = Image.new("RGB", (1280, 720), (255, 255, 255))
    draw = ImageDraw.Draw(canvas)
    h_reg = draw_centered_header(draw, "PHẦN 4: KHÁNG ĐỘC TỰ NHIÊN & GIẤC NGỦ THẦN THÁNH")
    
    render_scene_box(canvas, draw, BOX_LEFT, "1. TỬ CHIẾN HỔ MANG CHÚA & RẮN ĐỘC THẢO NGUYÊN",
                     (47, 133, 90), (240, 252, 245),
                     G / "c4_badger_vs_cobra.png",
                     [
                         {"title": "• Coi rắn kịch độc là món ăn khoái khẩu:",
                          "desc": "Hơn 25% khẩu phần ăn hàng ngày là các loài rắn độc\nTừ hổ mang, rắn lục phì đến mamba đen nguy hiểm nhất",
                          "gap": 8},
                         {"title": "• Tốc độ né đòn chuẩn xác từng mili-giây:",
                          "desc": "Dụ rắn mổ trượt rồi ngoạm đứt đầu trong chớp mắt\nKỹ năng săn rắn lão luyện di truyền qua nhiều thế hệ",
                          "gap": 8},
                         {"title": "• Cơn ác mộng của họ hàng nhà rắn:",
                          "desc": "Không loài rắn độc nào thoát khỏi thực đơn của nó!",
                          "color": (47, 133, 90), "gap": 6}
                     ])
                     
    render_scene_box(canvas, draw, BOX_RIGHT, "2. ĐỘT BIẾN GEN KHÁNG NỌC ĐỘC & GIẤC NGỦ HỒI SINH",
                     (130, 60, 160), (250, 242, 255),
                     G / "c4_badger_sleeping_venom.png",
                     [
                         {"title": "• Đột biến thụ thể Nicotinic Acetylcholine:",
                          "desc": "Nọc độc thần kinh neurotoxin không thể gắn kết tế bào\nCơ thể miễn nhiễm tự nhiên trước liều độc giết chết người",
                          "gap": 8},
                         {"title": "• Giấc ngủ 2 tiếng giải độc thần kỳ:",
                          "desc": "Khi bị tiêm liều nọc quá nặng, nó chỉ lăn ra ngủ mê man\nGan và thận chuyển hóa toàn bộ độc chất về trạng thái 0",
                          "gap": 8},
                         {"title": "• Tỉnh dậy tỉnh bơ ăn nốt con mồi:",
                          "desc": "Vươn vai thức dậy và xơi tái nửa khúc rắn còn lại ngon lành!",
                          "color": (130, 60, 160), "gap": 6}
                     ])
                     
    qa_verify_canvas(canvas, [BOX_LEFT, BOX_RIGHT], "04")
    canvas.save(OUTPUT_DIR / "scene04_canvas.png")
    
    ann = {
        "version": "1.0",
        "canvas": {"width": 1280, "height": 720},
        "sceneDurationMs": 110606,
        "elements": [
            {"id": "s04_header", "region": h_reg, "reveal": {"startMs": 0, "durationMs": 2000}},
            {"id": "s04_left", "region": {"x": 20, "y": 64, "width": 608, "height": 642}, "reveal": {"startMs": 2000, "durationMs": 54000}},
            {"id": "s04_right", "region": {"x": 652, "y": 64, "width": 608, "height": 642}, "reveal": {"startMs": 56000, "durationMs": 54606}}
        ]
    }
    with open(ANNOTATIONS_DIR / "scene04.annotation.json", "w", encoding="utf-8") as f:
        json.dump(ann, f, indent=2, ensure_ascii=False)
    print("Scene 04 Built & Verified.")

def build_scene05():
    canvas = Image.new("RGB", (1280, 720), (255, 255, 255))
    draw = ImageDraw.Draw(canvas)
    h_reg = draw_centered_header(draw, "PHẦN 5: TRÍ THÔNG MINH BẬC THẦY & DŨNG KHÍ VÔ SONG")
    
    render_scene_box(canvas, draw, BOX_LEFT, "1. HUYỀN THOẠI VƯỢT NGỤC STOFFEL (TRÍ KHÔN TẬP TÍNH)",
                     (43, 108, 176), (240, 246, 255),
                     G / "c5_stoffel_escape.png",
                     [
                         {"title": "• Khả năng sử dụng công cụ xuất sắc:",
                          "desc": "Xếp chồng những hòn đá làm bậc thang trèo qua tường rào\nDùng que cây và xẻng của người chăm sóc làm đòn bẩy",
                          "gap": 8},
                         {"title": "• Vo đất bùn thành bóng vượt tường bê tông:",
                          "desc": "Khi chuồng bị dọn sạch đá, nó vo bùn phơi khô làm bậc\nVượt ngục hàng chục lần khiến chuyên gia ngả mũ thán phục",
                          "gap": 8},
                         {"title": "• Bộ não giải đố sắc sảo:",
                          "desc": "Minh chứng cho trí tuệ sáng tạo vượt bậc trong hoang dã!",
                          "color": (43, 108, 176), "gap": 6}
                     ])
                     
    render_scene_box(canvas, draw, BOX_RIGHT, "2. MÀN ĐỐI ĐẦU 1 ĐẤU 3 VỚI SƯ TỬ DŨNG MÃNH",
                     (217, 56, 30), (255, 243, 240),
                     G / "c5_badger_vs_3_lions.png",
                     [
                         {"title": "• Tinh thần thép không chịu khuất phục:",
                          "desc": "Bị bao vây bởi 3 con sư tử trưởng thành vẫn không hề nao núng\nXù lông bờm trắng, gầm gừ hung tợn đe dọa chúa sơn lâm",
                          "gap": 8},
                         {"title": "• Vũ khí bí mật: Phun túi xạ hôi thối ngột ngạt:",
                          "desc": "Tuyến xạ hậu môn bắn ra dịch hôi nồng nặc làm cay mắt\nKhiến sư tử nghẹt thở, mất hết hứng thú săn mồi",
                          "gap": 8},
                         {"title": "• Chúa sơn lâm chịu thua rút lui:",
                          "desc": "Đàn sư tử lùi bước, nhường lại toàn bộ lãnh địa!",
                          "color": (217, 56, 30), "gap": 6}
                     ])
                     
    qa_verify_canvas(canvas, [BOX_LEFT, BOX_RIGHT], "05")
    canvas.save(OUTPUT_DIR / "scene05_canvas.png")
    
    ann = {
        "version": "1.0",
        "canvas": {"width": 1280, "height": 720},
        "sceneDurationMs": 109498,
        "elements": [
            {"id": "s05_header", "region": h_reg, "reveal": {"startMs": 0, "durationMs": 2000}},
            {"id": "s05_left", "region": {"x": 20, "y": 64, "width": 608, "height": 642}, "reveal": {"startMs": 2000, "durationMs": 53000}},
            {"id": "s05_right", "region": {"x": 652, "y": 64, "width": 608, "height": 642}, "reveal": {"startMs": 55000, "durationMs": 54498}}
        ]
    }
    with open(ANNOTATIONS_DIR / "scene05.annotation.json", "w", encoding="utf-8") as f:
        json.dump(ann, f, indent=2, ensure_ascii=False)
    print("Scene 05 Built & Verified.")

def build_scene06():
    canvas = Image.new("RGB", (1280, 720), (255, 255, 255))
    draw = ImageDraw.Draw(canvas)
    h_reg = draw_centered_header(draw, "PHẦN 6: BÀI HỌC CUỘC SỐNG & HÉ LỘ TẬP TIẾP THEO")
    
    render_scene_box(canvas, draw, BOX_LEFT, "1. TRIẾT LÝ SỐNG BẤT KHUẤT TỪ LỬNG MẬT",
                     (47, 133, 90), (240, 252, 245),
                     G / "c1_badger_thug_sunglasses.png",
                     [
                         {"title": "• Kích thước cơ thể không quyết định vị thế:",
                          "desc": "Dù bạn nhỏ bé, chỉ cần đủ bản lĩnh bạn sẽ khiến cả thế giới kiêng nể\nBiến những điểm yếu thành vũ khí sinh tồn mạnh mẽ nhất",
                          "gap": 8},
                         {"title": "• Dũng cảm đối mặt nghịch cảnh cuộc đời:",
                          "desc": "Không lùi bước trước khó khăn, coi thách thức là cơ hội rèn luyện\nBền bỉ tiến về phía trước tới cùng",
                          "gap": 8},
                         {"title": "• Bản lĩnh tạo nên sự khác biệt:",
                          "desc": "Hãy sống kiên cường và tự tin như một chiến binh lửng mật!",
                          "color": (47, 133, 90), "gap": 6}
                     ])
                     
    render_scene_box(canvas, draw, BOX_RIGHT, "2. HÉ LỘ TẬP 2: SỰ THẬT RÙNG MÌNH VỀ RÁI CÁ BIỂN",
                     (180, 80, 30), (255, 248, 240),
                     G / "c6_sea_otter_teaser.png",
                     [
                         {"title": "• Vẻ ngoài ngây thơ đáng yêu gây sốt thế giới:",
                          "desc": "Cặp mắt to tròn, nắm tay nhau ngủ bập bềnh trên sóng nước\nNhưng đằng sau nụ cười đó là bí mật đen tối rùng mình!",
                          "gap": 8},
                         {"title": "• Mặt tối man rợ chưa từng được công bố:",
                          "desc": "Hành vi săn mồi tàn nhẫn và những góc khuất gây sốc\nBạn sẽ hoàn toàn thay đổi cái nhìn về sinh vật 'cute' này",
                          "gap": 8},
                         {"title": "• Đón xem ngay Tập 2 trên kênh:",
                          "desc": "Đăng ký kênh & Bấm chuông thông báo để không bỏ lỡ!",
                          "color": (217, 56, 30), "gap": 6}
                     ])
                     
    qa_verify_canvas(canvas, [BOX_LEFT, BOX_RIGHT], "06")
    canvas.save(OUTPUT_DIR / "scene06_canvas.png")
    
    ann = {
        "version": "1.0",
        "canvas": {"width": 1280, "height": 720},
        "sceneDurationMs": 56947,
        "elements": [
            {"id": "s06_header", "region": h_reg, "reveal": {"startMs": 0, "durationMs": 2000}},
            {"id": "s06_left", "region": {"x": 20, "y": 64, "width": 608, "height": 642}, "reveal": {"startMs": 2000, "durationMs": 26000}},
            {"id": "s06_right", "region": {"x": 652, "y": 64, "width": 608, "height": 642}, "reveal": {"startMs": 28000, "durationMs": 28947}}
        ]
    }
    with open(ANNOTATIONS_DIR / "scene06.annotation.json", "w", encoding="utf-8") as f:
        json.dump(ann, f, indent=2, ensure_ascii=False)
    print("Scene 06 Built & Verified.")

if __name__ == "__main__":
    print("--- Building Canvases & Annotations for Lung Mat Project ---")
    build_scene01()
    build_scene02()
    build_scene03()
    build_scene04()
    build_scene05()
    build_scene06()
    print("--- All Canvases & Annotations Successfully Generated and QA Passed! ---")

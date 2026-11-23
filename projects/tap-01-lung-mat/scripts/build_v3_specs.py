"""
Scene Specifications Builder for Episode 1: Lửng Mật (V3 Production Standards)
- Native 1920x1080 Full HD
- Word-level precise timings from edge-tts
- Full animated card reveals + handwriting lines + stat bars
"""

from pathlib import Path

PROJ = Path(__file__).resolve().parent.parent
G = PROJ / "assets" / "gemini_downloaded"

BOX_LEFT = [50, 110, 935, 1040]
BOX_RIGHT = [985, 110, 1870, 1040]

SCENE_SPECS_V3 = {
    "scene01": {
        "id": "scene01",
        "totalDurationMs": 49637,
        "header": {
            "text": "PHẦN 1: BÁ CHỦ LỲ LỢM & CƠN ÁC MỘNG CỦA CHÚA SƠN LÂM",
            "startMs": 0,
            "durMs": 1500,
        },
        "panels": [
            {
                "id": "p1_badger",
                "box": BOX_LEFT,
                "title": "1. GÃ CHÍ PHÈO THẢO NGUYÊN (MELLIVORA CAPENSIS)",
                "color": (217, 56, 30),
                "header_bg": (255, 243, 240),
                "img_path": G / "c1_badger_thug_sunglasses.png",
                "startMs": 1500,
                "bullets": [
                    {
                        "title": "• Kích thước khiêm tốn - Khí phách ngút trời:",
                        "desc": "Chỉ cao 30cm, nặng vỏn vẹn 10-14kg\nPhong thái bất cần đời, không biết sợ cái chết",
                        "startMs": 2200,
                        "durMs": 6500,
                    },
                    {
                        "title": "• Kỷ lục Guinness thế giới vinh danh:",
                        "desc": "Sinh vật không biết sợ nhất hành tinh\nSẵn sàng quyết đấu sinh tử với mọi đối thủ",
                        "startMs": 16400,
                        "durMs": 7000,
                    },
                    {
                        "title": "• Phương châm sống bất tử:",
                        "desc": "Mellivora capensis - Kẻ Chí Phèo số 1 hoang dã!",
                        "color": (217, 56, 30),
                        "startMs": 29000,
                        "durMs": 4500,
                    },
                ],
            },
            {
                "id": "p2_lions",
                "box": BOX_RIGHT,
                "title": "2. SƯ TỬ VÀ BÁO HOA CŨNG PHẢI NHƯỢNG BỘ",
                "color": (43, 108, 176),
                "header_bg": (240, 246, 255),
                "img_path": G / "c1_lions_sweating_scared.png",
                "startMs": 36500,
                "bullets": [
                    {
                        "title": "• Chúa sơn lâm to lớn cũng e dè:",
                        "desc": "Nặng gấp 15 lần nhưng luôn chủ động né tránh\nKhông bao giờ muốn dây vào gã lỳ lợm này",
                        "startMs": 36800,
                        "durMs": 3500,
                    },
                    {
                        "title": "• Cái giá đánh đổi quá đắt đỏ:",
                        "desc": "Vật lộn cả tiếng, rách môi mẻ vuốt\nĐổi lại chỉ là miếng thịt dai nhách đầy mùi hôi",
                        "startMs": 40600,
                        "durMs": 3800,
                    },
                    {
                        "title": "• Bản tính trả đũa khốc liệt:",
                        "desc": "Ai trót đụng vào sẽ bị nó đuổi theo cắn xé tới cùng!",
                        "color": (43, 108, 176),
                        "startMs": 46300,
                        "durMs": 3000,
                    },
                ],
            },
        ],
    },

    "scene02": {
        "id": "scene02",
        "totalDurationMs": 46772,
        "header": {
            "text": "PHẦN 2: BẢNG CHỈ SỐ SINH TỒN RPG STATS",
            "startMs": 0,
            "durMs": 1500,
        },
        "panels": [
            {
                "id": "p1_stats_left",
                "box": BOX_LEFT,
                "title": "1. SỨC MẠNH THỂ CHẤT & BỀN BỈ (STR 85)",
                "color": (47, 133, 90),
                "header_bg": (240, 252, 245),
                "img_path": G / "c2_badger_muscles_strength.png",
                "startMs": 1500,
                "bullets": [
                    {
                        "title": "• Sức mạnh thể chất:",
                        "desc": "Cơ bắp nén đặc, kéo lê mồi nặng gấp 3 lần cơ thể\nChạy bền bỉ hàng chục km săn mồi không mệt",
                        "stat": {"label": "STR", "val": 85, "max": 100, "color": (47, 133, 90)},
                        "startMs": 7300,
                        "durMs": 4500,
                    },
                    {
                        "title": "• Khung xương nén mật độ cao:",
                        "desc": "Chịu được cú vồ đập nghìn cân của mãnh thú\nĐốt sống cổ to chắc bảo vệ yết hầu hoàn hảo",
                        "startMs": 13000,
                        "durMs": 3500,
                    },
                ],
            },
            {
                "id": "p2_stats_right",
                "box": BOX_RIGHT,
                "title": "2. GIÁP BẤT HOẠI & BỘ NÃO THIÊN TÀI (DEF 99)",
                "color": (180, 80, 30),
                "header_bg": (255, 248, 240),
                "img_path": G / "c2_badger_rubber_armor.png",
                "startMs": 14800,
                "bullets": [
                    {
                        "title": "• Phòng thủ tuyệt đối:",
                        "desc": "Lớp da cao su dày 6mm trơn tuột\nRăng nanh sư tử cắn vào bị trượt hoàn toàn",
                        "stat": {"label": "DEF", "val": 99, "max": 100, "color": (180, 80, 30)},
                        "startMs": 15000,
                        "durMs": 4500,
                    },
                    {
                        "title": "• Trí thông minh giải đố:",
                        "desc": "Thiên tài bẻ khóa, chế tạo công cụ và chiến thuật",
                        "stat": {"label": "IQ", "val": 90, "max": 100, "color": (43, 108, 176)},
                        "startMs": 24600,
                        "durMs": 4000,
                    },
                    {
                        "title": "• Độ lì đòn & Bản lĩnh:",
                        "desc": "Phá vỡ mọi thang đo - Không bao giờ đầu hàng!\nNỗi sợ: 0 tròn trĩnh - Hạch hạnh nhân tê liệt!",
                        "stat": {"label": "LÌ ĐÒN", "val": 100, "max": 100, "color": (217, 56, 30)},
                        "startMs": 31500,
                        "durMs": 5500,
                    },
                ],
            },
        ],
    },

    "scene03": {
        "id": "scene03",
        "totalDurationMs": 44714,
        "header": {
            "text": "PHẦN 3: TUYỆT KỸ XOAY 180 ĐỘ & VŨ KHÍ TẤN CÔNG",
            "startMs": 0,
            "durMs": 1500,
        },
        "panels": [
            {
                "id": "p1_turn180",
                "box": BOX_LEFT,
                "title": "1. TUYỆT KỸ XOAY 180 ĐỘ TRONG BAO DA PHẢN ĐÒN",
                "color": (217, 56, 30),
                "header_bg": (255, 243, 240),
                "img_path": G / "c3_badger_turn_180.png",
                "startMs": 1500,
                "bullets": [
                    {
                        "title": "• Da lỏng lẻo như áo khoác rộng:",
                        "desc": "Dày hơn da trâu nhưng trượt tự do quanh cơ bắp\nKẻ thù ngậm chặt bên ngoài nhưng bên trong an toàn",
                        "startMs": 6300,
                        "durMs": 5000,
                    },
                    {
                        "title": "• Cú cắn ngược bất ngờ vào mũi báo hoa:",
                        "desc": "Bị tóm gáy liền xoay 180 độ đớp thẳng vào mắt kẻ địch\nKhiến kẻ săn mồi đau đớn nhả ra ngay tức khắc",
                        "startMs": 13400,
                        "durMs": 5500,
                    },
                    {
                        "title": "• Vũ khí không góc chết:",
                        "desc": "Biến mọi vị trí bị tóm thành bẫy tử địa phản công!",
                        "color": (217, 56, 30),
                        "startMs": 21600,
                        "durMs": 3500,
                    },
                ],
            },
            {
                "id": "p2_weapons",
                "box": BOX_RIGHT,
                "title": "2. MÓNG VUỐT 5CM & BỘ HÀM PHÁ MAI RÙA",
                "color": (43, 108, 176),
                "header_bg": (240, 246, 255),
                "img_path": G / "c3_badger_sharp_claws.png",
                "startMs": 26200,
                "bullets": [
                    {
                        "title": "• Móng vuốt cứng như mũi khoan thép:",
                        "desc": "Dài hơn 5cm, cong vút và siêu cứng\nXới tung tổ mối cứng như bê tông trong vài phút",
                        "startMs": 26500,
                        "durMs": 4500,
                    },
                    {
                        "title": "• Lực cắn nghiền nát mai rùa:",
                        "desc": "Cơ hàm cực khỏe đập vỡ mai rùa và xương tủy\nNhai trọn vẹn con mồi không để sót lại calo nào",
                        "startMs": 33700,
                        "durMs": 3500,
                    },
                    {
                        "title": "• Vũ khí phòng vệ hóa học:",
                        "desc": "Túi xạ phun khí gas thối nồng nặc làm cay mắt kẻ thù!",
                        "color": (43, 108, 176),
                        "startMs": 37500,
                        "durMs": 4500,
                    },
                ],
            },
        ],
    },

    "scene04": {
        "id": "scene04",
        "totalDurationMs": 47462,
        "header": {
            "text": "PHẦN 4: KHÁNG ĐỘC TỰ NHIÊN & GIẤC NGỦ THẦN THÁNH",
            "startMs": 0,
            "durMs": 1500,
        },
        "panels": [
            {
                "id": "p1_cobra",
                "box": BOX_LEFT,
                "title": "1. THỰC ĐƠN ĐIÊN RỒ: SĂN RẮN KỊCH ĐỘC",
                "color": (47, 133, 90),
                "header_bg": (240, 252, 245),
                "img_path": G / "c4_badger_vs_cobra.png",
                "startMs": 1500,
                "bullets": [
                    {
                        "title": "• Coi rắn kịch độc là món ăn khoái khẩu:",
                        "desc": "Hơn 25% thức ăn là hổ mang chúa, rắn lục, mamba đen\nMột giọt nọc rắn đủ giết sinh vật to gấp 10 lần nó",
                        "startMs": 5000,
                        "durMs": 5000,
                    },
                    {
                        "title": "• Tốc độ né đòn chuẩn xác từng mili-giây:",
                        "desc": "Dụ rắn mổ trượt rồi ngoạm đứt đầu trong chớp mắt\nKỹ năng săn rắn lão luyện di truyền qua nhiều thế hệ",
                        "startMs": 12600,
                        "durMs": 4500,
                    },
                    {
                        "title": "• Cơn ác mộng của loài rắn:",
                        "desc": "Không loài rắn độc nào thoát khỏi thực đơn của nó!",
                        "color": (47, 133, 90),
                        "startMs": 19600,
                        "durMs": 3000,
                    },
                ],
            },
            {
                "id": "p2_sleeping",
                "box": BOX_RIGHT,
                "title": "2. ĐỘT BIẾN GEN KHÁNG ĐỘC & GIẤC NGỦ HỒI SINH",
                "color": (130, 60, 160),
                "header_bg": (250, 242, 255),
                "img_path": G / "c4_badger_sleeping_venom.png",
                "startMs": 22400,
                "bullets": [
                    {
                        "title": "• Đột biến thụ thể Nicotinic Acetylcholine:",
                        "desc": "Áo giáp phân tử ngăn nọc thần kinh gắn vào tế bào\nCơ thể miễn nhiễm tự nhiên trước liều độc cực mạnh",
                        "startMs": 25200,
                        "durMs": 5500,
                    },
                    {
                        "title": "• Giấc ngủ 2 tiếng giải độc thần kỳ:",
                        "desc": "Khi bị cắn trúng, nó lăn ra ngủ mê man như say rượu\nGan và thận chuyển hóa toàn bộ độc chất về số 0",
                        "startMs": 33600,
                        "durMs": 5000,
                    },
                    {
                        "title": "• Tỉnh dậy tỉnh bơ ăn nốt con mồi:",
                        "desc": "Vươn vai thức dậy và xơi trọn nửa con rắn còn lại!",
                        "color": (130, 60, 160),
                        "startMs": 41500,
                        "durMs": 4500,
                    },
                ],
            },
        ],
    },

    "scene05": {
        "id": "scene05",
        "totalDurationMs": 50648,
        "header": {
            "text": "PHẦN 5: TRÍ THÔNG MINH BẬC THẦY & DŨNG KHÍ VÔ SONG",
            "startMs": 0,
            "durMs": 1500,
        },
        "panels": [
            {
                "id": "p1_stoffel",
                "box": BOX_LEFT,
                "title": "1. HUYỀN THOẠI VƯỢT NGỤC STOFFEL (IQ ĐỈNH CAO)",
                "color": (43, 108, 176),
                "header_bg": (240, 246, 255),
                "img_path": G / "c5_stoffel_escape.png",
                "startMs": 1500,
                "bullets": [
                    {
                        "title": "• Siêu sao vượt ngục nổi tiếng toàn cầu:",
                        "desc": "Được đài BBC làm riêng bộ phim về những vụ trốn thoát\nChuồng tường bê tông cao lút đầu người vẫn không cản nổi",
                        "startMs": 4200,
                        "durMs": 5500,
                    },
                    {
                        "title": "• Nặn bóng bùn và xếp đá làm thang:",
                        "desc": "Tự vo đất bùn phơi khô, xếp đá và cành cây leo qua tường\nChuyên gia động vật học ngả mũ thán phục trí tuệ",
                        "startMs": 17600,
                        "durMs": 5500,
                    },
                    {
                        "title": "• Trèo lên lưng bạn gái vượt ngục:",
                        "desc": "Dụ lửng cái đứng góc tường làm bàn đạp phóng ra ngoài!",
                        "color": (43, 108, 176),
                        "startMs": 27700,
                        "durMs": 5000,
                    },
                ],
            },
            {
                "id": "p2_lions_clash",
                "box": BOX_RIGHT,
                "title": "2. MÀN ĐỐI ĐẦU 1 ĐẤU 3 VỚI SƯ TỬ DŨNG MÃNH",
                "color": (217, 56, 30),
                "header_bg": (255, 243, 240),
                "img_path": G / "c5_badger_vs_3_lions.png",
                "startMs": 35000,
                "bullets": [
                    {
                        "title": "• Vượt ngục sang chuồng sư tử gây sự:",
                        "desc": "Trốn ra không phải về rừng mà để khiêu chiến sư tử!",
                        "startMs": 35600,
                        "durMs": 3500,
                    },
                    {
                        "title": "• 1 chọi 3 không bao giờ lùi bước:",
                        "desc": "Bị 3 sư tử bao vây vẫn xù lông gầm thét lao vào giữa bầy\nTinh thần thép khiến các chúa tể phải kiêng nể",
                        "startMs": 40400,
                        "durMs": 4500,
                    },
                    {
                        "title": "• Chúa sơn lâm chịu thua tháo lui:",
                        "desc": "Phun túi xạ cay mắt, buộc đàn sư tử phải rút lui!",
                        "color": (217, 56, 30),
                        "startMs": 46800,
                        "durMs": 3500,
                    },
                ],
            },
        ],
    },

    "scene06": {
        "id": "scene06",
        "totalDurationMs": 29191,
        "header": {
            "text": "PHẦN 6: BÀI HỌC CUỘC SỐNG & HÉ LỘ TẬP TIẾP THEO",
            "startMs": 0,
            "durMs": 1500,
        },
        "panels": [
            {
                "id": "p1_lesson",
                "box": BOX_LEFT,
                "title": "1. TRIẾT LÝ SỐNG BẤT KHUẤT TỪ LỬNG MẬT",
                "color": (47, 133, 90),
                "header_bg": (240, 252, 245),
                "img_path": G / "c1_badger_thug_sunglasses.png",
                "startMs": 1500,
                "bullets": [
                    {
                        "title": "• Kích thước cơ thể không quyết định vị thế:",
                        "desc": "Dù bạn nhỏ bé, chỉ cần đủ bản lĩnh bạn sẽ khiến cả thế giới nể\nBiến những điểm yếu thành vũ khí sinh tồn mạnh mẽ nhất",
                        "startMs": 1800,
                        "durMs": 4500,
                    },
                    {
                        "title": "• Bản lĩnh tạo nên sự khác biệt:",
                        "desc": "Hãy sống kiên cường và tự tin như một chiến binh lửng mật!",
                        "color": (47, 133, 90),
                        "startMs": 4000,
                        "durMs": 3000,
                    },
                ],
            },
            {
                "id": "p2_teaser",
                "box": BOX_RIGHT,
                "title": "2. HÉ LỘ TẬP 2: SỰ THẬT RÙNG MÌNH VỀ RÁI CÁ BIỂN",
                "color": (180, 80, 30),
                "header_bg": (255, 248, 240),
                "img_path": G / "c6_sea_otter_teaser.png",
                "startMs": 7100,
                "bullets": [
                    {
                        "title": "• Vẻ ngoài dễ thương đáng yêu gây sốt thế giới:",
                        "desc": "Nắm tay nhau ngủ bập bềnh nhưng ẩn chứa bí mật rùng mình!",
                        "startMs": 9700,
                        "durMs": 4000,
                    },
                    {
                        "title": "• Mặt tối man rợ chưa từng được công bố:",
                        "desc": "Hành vi săn mồi tàn nhẫn và góc khuất gây sốc",
                        "startMs": 13800,
                        "durMs": 5000,
                    },
                    {
                        "title": "• Đón xem ngay Tập 2 trên kênh:",
                        "desc": "Đăng ký kênh & Bấm chuông thông báo để không bỏ lỡ!",
                        "color": (217, 56, 30),
                        "startMs": 22100,
                        "durMs": 4500,
                    },
                ],
            },
        ],
    },
}

def get_scene_spec_v3(scene_id: str) -> dict:
    return SCENE_SPECS_V3[scene_id]

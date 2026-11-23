"""
Scene Specifications Builder for Episode 1: Lửng Mật
Configures:
- Fast narration timings (53.97s, 84.04s, 73.98s, 90.80s, 88.30s, 48.64s)
- AI Image Card Pop-in animations (no scribbling on images!)
- Hand writing text exclusively (Header & bullet points line-by-line)
"""

from pathlib import Path

PROJ = Path(__file__).resolve().parent.parent
G = PROJ / "assets" / "gemini_downloaded"

BOX_LEFT = [20, 64, 628, 706]
BOX_RIGHT = [652, 64, 1260, 706]

SCENE_SPECS = [
    # SCENE 1 (53.97s = 53967ms)
    {
        "id": "scene01",
        "totalDurationMs": 53967,
        "header": {
            "text": "PHẦN 1: BÁ CHỦ LỲ LỢM & CƠN ÁC MỘNG CỦA CHÚA SƠN LÂM",
            "box": [280, 10, 1000, 52],
            "startMs": 0,
            "durMs": 1500
        },
        "panels": [
            {
                "id": "p1_left",
                "box": BOX_LEFT,
                "title": "1. GÃ CHÍ PHÈO THẢO NGUYÊN (MELLIVORA CAPENSIS)",
                "color": (217, 56, 30),
                "header_bg": (255, 243, 240),
                "img_path": G / "c1_badger_thug_sunglasses.png",
                "startMs": 1500,
                "bullets": [
                    {
                        "title": "• Kích thước khiêm tốn - Khí phách ngút trời:",
                        "desc": "Chỉ dài 60-70cm, nặng vỏn vẹn 10-14kg\nNhưng mang phong thái bá chủ không sợ bất kỳ ai",
                        "region": [35, 395, 615, 455],
                        "startMs": 2200,
                        "durMs": 9500
                    },
                    {
                        "title": "• Kỷ lục Guinness thế giới vinh danh:",
                        "desc": "Được công nhận là 'Sinh vật không biết sợ nhất hành tinh'\nSẵn sàng đối đầu bất kỳ loài thú săn mồi nào",
                        "region": [35, 465, 615, 525],
                        "startMs": 12000,
                        "durMs": 8500
                    },
                    {
                        "title": "• Phương châm sống kinh điển:",
                        "desc": "Sống là chiến đấu, không lùi bước trước hiểm nguy!",
                        "color": (217, 56, 30),
                        "region": [35, 535, 615, 585],
                        "startMs": 21000,
                        "durMs": 5000
                    }
                ]
            },
            {
                "id": "p2_right",
                "box": BOX_RIGHT,
                "title": "2. SƯ TỬ VÀ BÁO HOA CŨNG PHẢI NHƯỢNG BỘ",
                "color": (43, 108, 176),
                "header_bg": (240, 246, 255),
                "img_path": G / "c1_lions_sweating_scared.png",
                "startMs": 26500,
                "bullets": [
                    {
                        "title": "• Chúa sơn lâm to lớn cũng e dè:",
                        "desc": "Nặng gấp 15 lần nhưng không bao giờ muốn đụng độ\nMỗi lần chạm mặt đều chủ động né sang một bên",
                        "region": [667, 395, 1245, 455],
                        "startMs": 27200,
                        "durMs": 9500
                    },
                    {
                        "title": "• Cái giá đánh đổi quá đắt:",
                        "desc": "Tốn cả tiếng vật lộn mệt đứt hơi, rách môi mẻ vuốt\nĐổi lại chỉ là miếng thịt dai nhách đầy mùi hôi hám",
                        "region": [667, 465, 1245, 525],
                        "startMs": 37000,
                        "durMs": 9500
                    },
                    {
                        "title": "• Tính khí trả đũa khốc liệt:",
                        "desc": "Ai trót đụng vào sẽ bị nó đuổi theo cắn xé tới cùng!",
                        "color": (43, 108, 176),
                        "region": [667, 535, 1245, 585],
                        "startMs": 47000,
                        "durMs": 6500
                    }
                ]
            }
        ]
    },

    # SCENE 2 (84.04s = 84039ms)
    {
        "id": "scene02",
        "totalDurationMs": 84039,
        "header": {
            "text": "PHẦN 2: BỘ GIÁP CAO SU 6MM & CƠ THỂ BẤT HOẠI",
            "box": [320, 10, 960, 52],
            "startMs": 0,
            "durMs": 1500
        },
        "panels": [
            {
                "id": "p1_left",
                "box": BOX_LEFT,
                "title": "1. THỂ LỰC PHI THƯỜNG & KHUNG XƯƠNG ĐẶC (STR 85)",
                "color": (47, 133, 90),
                "header_bg": (240, 252, 245),
                "img_path": G / "c2_badger_muscles_strength.png",
                "startMs": 1500,
                "bullets": [
                    {
                        "title": "• Thể lực bền bỉ vô tận:",
                        "desc": "Chạy rong ruổi hàng chục km khắp thảo nguyên săn mồi\nCơ bắp dẻo dai giúp vận động liên tục không mệt mỏi",
                        "region": [35, 395, 615, 455],
                        "startMs": 2200,
                        "durMs": 14000
                    },
                    {
                        "title": "• Khung xương nén mật độ cao:",
                        "desc": "Chịu được cú vồ đập nghìn cân của mãnh thú săn mồi\nCổ to chắc nịch bảo vệ hoàn hảo đốt sống cổ",
                        "region": [35, 465, 615, 525],
                        "startMs": 16500,
                        "durMs": 13000
                    },
                    {
                        "title": "• Chỉ số chiến binh toàn diện:",
                        "desc": "Sức bền 85/100 - Bền bỉ vượt trội mọi loài săn mồi!",
                        "color": (47, 133, 90),
                        "region": [35, 535, 615, 585],
                        "startMs": 30000,
                        "durMs": 11000
                    }
                ]
            },
            {
                "id": "p2_right",
                "box": BOX_RIGHT,
                "title": "2. BỘ GIÁP DA CAO SU DÀY 6MM TRƠN TUỘT (DEF 99)",
                "color": (180, 80, 30),
                "header_bg": (255, 248, 240),
                "img_path": G / "c2_badger_rubber_armor.png",
                "startMs": 42000,
                "bullets": [
                    {
                        "title": "• Lớp da cao su dày 6mm bất khả xâm phạm:",
                        "desc": "Cấu tạo từ mô liên kết collagen dày đặc và chất sừng\nRăng nanh sư tử cắn vào bị trượt, gai nhím gãy vụn",
                        "region": [667, 395, 1245, 455],
                        "startMs": 42700,
                        "durMs": 14000
                    },
                    {
                        "title": "• Da lỏng lẻo như áo khoác rộng thùng thình:",
                        "desc": "Cơ thịt trượt tự do bên dưới mà không bị tổn thương\nKẻ thù ngậm chặt lớp da ngoài nhưng bên trong vẫn an toàn",
                        "region": [667, 465, 1245, 525],
                        "startMs": 57000,
                        "durMs": 14000
                    },
                    {
                        "title": "• Phòng thủ tuyệt đối DEF 99:",
                        "desc": "Áo giáp sinh học thần kỳ bảo vệ tính mạng!",
                        "color": (180, 80, 30),
                        "region": [667, 535, 1245, 585],
                        "startMs": 71500,
                        "durMs": 12000
                    }
                ]
            }
        ]
    },

    # SCENE 3 (73.98s = 73976ms)
    {
        "id": "scene03",
        "totalDurationMs": 73976,
        "header": {
            "text": "PHẦN 3: TUYỆT KỸ XOAY 180 ĐỘ & VŨ KHÍ TẤN CÔNG BẠO TÀN",
            "box": [270, 10, 1010, 52],
            "startMs": 0,
            "durMs": 1500
        },
        "panels": [
            {
                "id": "p1_left",
                "box": BOX_LEFT,
                "title": "1. TUYỆT KỸ XOAY 180 ĐỘ TRONG BAO DA PHẢN ĐÒN",
                "color": (217, 56, 30),
                "header_bg": (255, 243, 240),
                "img_path": G / "c3_badger_turn_180.png",
                "startMs": 1500,
                "bullets": [
                    {
                        "title": "• Cấu trúc giải phẫu độc nhất vô nhị:",
                        "desc": "Xoay toàn bộ thân hình 180 độ ngay bên trong túi da\nBiến tư thế bị khống chế thành đòn phản công chí mạng",
                        "region": [35, 395, 615, 455],
                        "startMs": 2200,
                        "durMs": 12000
                    },
                    {
                        "title": "• Đòn cắn ngược bất ngờ vào mũi kẻ thù:",
                        "desc": "Báo hoa ngậm gáy liền bị quay đầu đớp thẳng vào mũi\nKhiến kẻ săn mồi đau đớn hoảng loạn nhả ra ngay tức khắc",
                        "region": [35, 465, 615, 525],
                        "startMs": 14500,
                        "durMs": 13000
                    },
                    {
                        "title": "• Không góc chết phòng ngự:",
                        "desc": "Bất cứ vị trí nào bị tóm đều biến thành tử địa của kẻ địch!",
                        "color": (217, 56, 30),
                        "region": [35, 535, 615, 585],
                        "startMs": 28000,
                        "durMs": 8500
                    }
                ]
            },
            {
                "id": "p2_right",
                "box": BOX_RIGHT,
                "title": "2. MÓNG VUỐT 5CM & BỘ HÀM PHÁ VỠ CẢ MAI RÙA",
                "color": (43, 108, 176),
                "header_bg": (240, 246, 255),
                "img_path": G / "c3_badger_sharp_claws.png",
                "startMs": 37000,
                "bullets": [
                    {
                        "title": "• Cặp móng vuốt hình lưỡi liềm dài 5cm:",
                        "desc": "Đào bới tổ mối cứng như bê tông chỉ trong vài phút\nCào xé dữ dội gây thương tích nặng nề cho đối thủ",
                        "region": [667, 395, 1245, 455],
                        "startMs": 37700,
                        "durMs": 13000
                    },
                    {
                        "title": "• Lực cắn nghiền nát xương và mai rùa:",
                        "desc": "Răng sắc nhọn kết hợp cơ hàm cực khỏe đập vỡ mai rùa\nĂn trọn vẹn cả xương tủy không để sót calo nào",
                        "region": [667, 465, 1245, 525],
                        "startMs": 51000,
                        "durMs": 13000
                    },
                    {
                        "title": "• Tấn công điểm yếu nhạy cảm:",
                        "desc": "Nhắm thẳng vào mắt và hạ bộ kẻ thù để vô hiệu hóa!",
                        "color": (43, 108, 176),
                        "region": [667, 535, 1245, 585],
                        "startMs": 64500,
                        "durMs": 9000
                    }
                ]
            }
        ]
    },

    # SCENE 4 (90.80s = 90796ms)
    {
        "id": "scene04",
        "totalDurationMs": 90796,
        "header": {
            "text": "PHẦN 4: KHÁNG ĐỘC TỰ NHIÊN & GIẤC NGỦ THẦN THÁNH",
            "box": [290, 10, 990, 52],
            "startMs": 0,
            "durMs": 1500
        },
        "panels": [
            {
                "id": "p1_left",
                "box": BOX_LEFT,
                "title": "1. TỬ CHIẾN HỔ MANG CHÚA & RẮN ĐỘC THẢO NGUYÊN",
                "color": (47, 133, 90),
                "header_bg": (240, 252, 245),
                "img_path": G / "c4_badger_vs_cobra.png",
                "startMs": 1500,
                "bullets": [
                    {
                        "title": "• Coi rắn kịch độc là món ăn khoái khẩu:",
                        "desc": "Hơn 25% khẩu phần ăn hàng ngày là các loài rắn độc\nTừ hổ mang, rắn lục phì đến mamba đen nguy hiểm nhất",
                        "region": [35, 395, 615, 455],
                        "startMs": 2200,
                        "durMs": 14000
                    },
                    {
                        "title": "• Tốc độ né đòn chuẩn xác từng mili-giây:",
                        "desc": "Dụ rắn mổ trượt rồi ngoạm đứt đầu trong chớp mắt\nKỹ năng săn rắn lão luyện di truyền qua nhiều thế hệ",
                        "region": [35, 465, 615, 525],
                        "startMs": 16500,
                        "durMs": 14000
                    },
                    {
                        "title": "• Cơn ác mộng của họ hàng nhà rắn:",
                        "desc": "Không loài rắn độc nào thoát khỏi thực đơn của nó!",
                        "color": (47, 133, 90),
                        "region": [35, 535, 615, 585],
                        "startMs": 31000,
                        "durMs": 14000
                    }
                ]
            },
            {
                "id": "p2_right",
                "box": BOX_RIGHT,
                "title": "2. ĐỘT BIẾN GEN KHÁNG NỌC ĐỘC & GIẤC NGỦ HỒI SINH",
                "color": (130, 60, 160),
                "header_bg": (250, 242, 255),
                "img_path": G / "c4_badger_sleeping_venom.png",
                "startMs": 46000,
                "bullets": [
                    {
                        "title": "• Đột biến thụ thể Nicotinic Acetylcholine:",
                        "desc": "Nọc độc thần kinh neurotoxin không thể gắn kết tế bào\nCơ thể miễn nhiễm tự nhiên trước liều độc giết chết người",
                        "region": [667, 395, 1245, 455],
                        "startMs": 46700,
                        "durMs": 15000
                    },
                    {
                        "title": "• Giấc ngủ 2 tiếng giải độc thần kỳ:",
                        "desc": "Khi bị tiêm liều nọc quá nặng, nó chỉ lăn ra ngủ mê man\nGan và thận chuyển hóa toàn bộ độc chất về trạng thái 0",
                        "region": [667, 465, 1245, 525],
                        "startMs": 62000,
                        "durMs": 15000
                    },
                    {
                        "title": "• Tỉnh dậy tỉnh bơ ăn nốt con mồi:",
                        "desc": "Vươn vai thức dậy và xơi tái nửa khúc rắn còn lại ngon lành!",
                        "color": (130, 60, 160),
                        "region": [667, 535, 1245, 585],
                        "startMs": 77500,
                        "durMs": 12500
                    }
                ]
            }
        ]
    },

    # SCENE 5 (88.30s = 88299ms)
    {
        "id": "scene05",
        "totalDurationMs": 88299,
        "header": {
            "text": "PHẦN 5: TRÍ THÔNG MINH BẬC THẦY & DŨNG KHÍ VÔ SONG",
            "box": [280, 10, 1000, 52],
            "startMs": 0,
            "durMs": 1500
        },
        "panels": [
            {
                "id": "p1_left",
                "box": BOX_LEFT,
                "title": "1. HUYỀN THOẠI VƯỢT NGỤC STOFFEL (TRÍ KHÔN TẬP TÍNH)",
                "color": (43, 108, 176),
                "header_bg": (240, 246, 255),
                "img_path": G / "c5_stoffel_escape.png",
                "startMs": 1500,
                "bullets": [
                    {
                        "title": "• Khả năng sử dụng công cụ xuất sắc:",
                        "desc": "Xếp chồng những hòn đá làm bậc thang trèo qua tường rào\nDùng que cây và xẻng của người chăm sóc làm đòn bẩy",
                        "region": [35, 395, 615, 455],
                        "startMs": 2200,
                        "durMs": 14000
                    },
                    {
                        "title": "• Vo đất bùn thành bóng vượt tường bê tông:",
                        "desc": "Khi chuồng bị dọn sạch đá, nó vo bùn phơi khô làm bậc\nVượt ngục hàng chục lần khiến chuyên gia ngả mũ thán phục",
                        "region": [35, 465, 615, 525],
                        "startMs": 16500,
                        "durMs": 14000
                    },
                    {
                        "title": "• Bộ não giải đố sắc sảo:",
                        "desc": "Minh chứng cho trí tuệ sáng tạo vượt bậc trong hoang dã!",
                        "color": (43, 108, 176),
                        "region": [35, 535, 615, 585],
                        "startMs": 31000,
                        "durMs": 13000
                    }
                ]
            },
            {
                "id": "p2_right",
                "box": BOX_RIGHT,
                "title": "2. MÀN ĐỐI ĐẦU 1 ĐẤU 3 VỚI SƯ TỬ DŨNG MÃNH",
                "color": (217, 56, 30),
                "header_bg": (255, 243, 240),
                "img_path": G / "c5_badger_vs_3_lions.png",
                "startMs": 45000,
                "bullets": [
                    {
                        "title": "• Tinh thần thép không chịu khuất phục:",
                        "desc": "Bị bao vây bởi 3 con sư tử trưởng thành vẫn không hề nao núng\nXù lông bờm trắng, gầm gừ hung tợn đe dọa chúa sơn lâm",
                        "region": [667, 395, 1245, 455],
                        "startMs": 45700,
                        "durMs": 14000
                    },
                    {
                        "title": "• Vũ khí bí mật: Phun túi xạ hôi thối ngột ngạt:",
                        "desc": "Tuyến xạ hậu môn bắn ra dịch hôi nồng nặc làm cay mắt\nKhiến sư tử nghẹt thở, mất hết hứng thú săn mồi",
                        "region": [667, 465, 1245, 525],
                        "startMs": 60000,
                        "durMs": 14000
                    },
                    {
                        "title": "• Chúa sơn lâm chịu thua rút lui:",
                        "desc": "Đàn sư tử lùi bước, nhường lại toàn bộ lãnh địa!",
                        "color": (217, 56, 30),
                        "region": [667, 535, 1245, 585],
                        "startMs": 74500,
                        "durMs": 13000
                    }
                ]
            }
        ]
    },

    # SCENE 6 (48.64s = 48641ms)
    {
        "id": "scene06",
        "totalDurationMs": 48641,
        "header": {
            "text": "PHẦN 6: BÀI HỌC CUỘC SỐNG & HÉ LỘ TẬP TIẾP THEO",
            "box": [300, 10, 980, 52],
            "startMs": 0,
            "durMs": 1500
        },
        "panels": [
            {
                "id": "p1_left",
                "box": BOX_LEFT,
                "title": "1. TRIẾT LÝ SỐNG BẤT KHUẤT TỪ LỬNG MẬT",
                "color": (47, 133, 90),
                "header_bg": (240, 252, 245),
                "img_path": G / "c1_badger_thug_sunglasses.png",
                "startMs": 1500,
                "bullets": [
                    {
                        "title": "• Kích thước cơ thể không quyết định vị thế:",
                        "desc": "Dù bạn nhỏ bé, chỉ cần đủ bản lĩnh bạn sẽ khiến cả thế giới kiêng nể\nBiến những điểm yếu thành vũ khí sinh tồn mạnh mẽ nhất",
                        "region": [35, 395, 615, 455],
                        "startMs": 2200,
                        "durMs": 10000
                    },
                    {
                        "title": "• Dũng cảm đối mặt nghịch cảnh cuộc đời:",
                        "desc": "Không lùi bước trước khó khăn, coi thách thức là cơ hội rèn luyện\nBền bỉ tiến về phía trước tới cùng",
                        "region": [35, 465, 615, 525],
                        "startMs": 12500,
                        "durMs": 9500
                    },
                    {
                        "title": "• Bản lĩnh tạo nên sự khác biệt:",
                        "desc": "Hãy sống kiên cường và tự tin như một chiến binh lửng mật!",
                        "color": (47, 133, 90),
                        "region": [35, 535, 615, 585],
                        "startMs": 22500,
                        "durMs": 4500
                    }
                ]
            },
            {
                "id": "p2_right",
                "box": BOX_RIGHT,
                "title": "2. HÉ LỘ TẬP 2: SỰ THẬT RÙNG MÌNH VỀ RÁI CÁ BIỂN",
                "color": (180, 80, 30),
                "header_bg": (255, 248, 240),
                "img_path": G / "c6_sea_otter_teaser.png",
                "startMs": 27500,
                "bullets": [
                    {
                        "title": "• Vẻ ngoài ngây thơ đáng yêu gây sốt thế giới:",
                        "desc": "Cặp mắt to tròn, nắm tay nhau ngủ bập bềnh trên sóng nước\nNhưng đằng sau nụ cười đó là bí mật đen tối rùng mình!",
                        "region": [667, 395, 1245, 455],
                        "startMs": 28200,
                        "durMs": 8500
                    },
                    {
                        "title": "• Mặt tối man rợ chưa từng được công bố:",
                        "desc": "Hành vi săn mồi tàn nhẫn và những góc khuất gây sốc\nBạn sẽ hoàn toàn thay đổi cái nhìn về sinh vật 'cute' này",
                        "region": [667, 465, 1245, 525],
                        "startMs": 37000,
                        "durMs": 6500
                    },
                    {
                        "title": "• Đón xem ngay Tập 2 trên kênh:",
                        "desc": "Đăng ký kênh & Bấm chuông thông báo để không bỏ lỡ!",
                        "color": (217, 56, 30),
                        "region": [667, 535, 1245, 585],
                        "startMs": 44000,
                        "durMs": 4200
                    }
                ]
            }
        ]
    }
]

def get_scene_spec(scene_idx: int) -> dict:
    return SCENE_SPECS[scene_idx - 1]

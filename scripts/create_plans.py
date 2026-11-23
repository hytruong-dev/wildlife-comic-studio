import json
from pathlib import Path

P = Path("projects/tap-07-tom-tit")
specs = P / "specs"
specs.mkdir(parents=True, exist_ok=True)

# 1. LONG-FORM PLAN
longform_plan = {
    "targets": {
        "PUNCH": [0.65, 0.45],
        "STAT": [0.35, 0.50],
        "CAVIT": [0.60, 0.55],
        "MOLT": [0.50, 0.60],
        "TANK": [0.55, 0.45],
        "EYE": [0.60, 0.40]
    },
    "scenes": {
        "scene01": {
            "chapter_no": 1,
            "title": "KẺ SỞ HỮU CÚ ĐẤM NHANH NHƯ ĐẠN BẮN",
            "hook": "MIKE TYSON CỦA ĐẠI DƯƠNG",
            "card": False,
            "beats": [
                {
                    "at": 0,
                    "image": "assets/long/L01.png",
                    "stickers": [
                        {"at": "hai mươi xăng-ti-mét", "side": "L", "y": 380, "value": "< 20 cm", "label": "chiều dài tí hon"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Hãy làm quen với Tôm Tít",
                    "image": "assets/long/L01.png",
                    "stickers": [
                        {"at": "Mike Tyson", "side": "R", "y": 420, "value": "TYSON", "label": "võ sĩ đại dương"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Nhìn từ xa",
                    "image": "assets/long/L01.png",
                    "stickers": [],
                    "impacts": []
                },
                {
                    "at": "Thế nhưng ẩn dưới",
                    "image": "assets/long/L02.png",
                    "stickers": [
                        {"at": "súng trường bắn", "side": "R", "y": 380, "value": "NHƯ ĐẠN", "label": "tốc độ súng trường"}
                    ],
                    "impacts": ["súng"]
                },
                {
                    "at": "Cua biển mai dày",
                    "image": "assets/long/L02.png",
                    "stickers": [
                        {"at": "Một đấm vỡ nát", "side": "R", "y": 420, "value": "1 ĐẤM", "label": "vỡ nát mai cua"}
                    ],
                    "impacts": ["đấm"]
                },
                {
                    "at": "Thậm chí ngay cả mặt",
                    "image": "assets/long/L12.png",
                    "stickers": [
                        {"at": "đấm nứt toác", "side": "L", "y": 400, "value": "NỨT KÍNH", "label": "bể cá dày cm"}
                    ],
                    "impacts": ["nứt"]
                },
                {
                    "at": "Các thợ lặn biển từ lâu",
                    "image": "assets/long/L03.png",
                    "stickers": [
                        {"at": "Kẻ Chẻ Ngón Tay", "side": "L", "y": 420, "value": "CẢNH BÁO", "label": "kẻ chẻ ngón tay"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Lý do vô cùng đơn giản",
                    "image": "assets/long/L03.png",
                    "stickers": [],
                    "impacts": []
                },
                {
                    "at": "Một gã tí hon dưới đáy",
                    "image": "assets/long/L01.png",
                    "stickers": [],
                    "impacts": []
                }
            ]
        },
        "scene02": {
            "chapter_no": 2,
            "title": "BẢNG CHỈ SỐ GIAN LẬN: ATK 9999, GIA TỐC 10.400G",
            "hook": "NHÂN VẬT GIAN LẬN CHỈ SỐ",
            "card": True,
            "beats": [
                {
                    "at": 0,
                    "image": "assets/long/L04.png",
                    "stickers": [],
                    "impacts": []
                },
                {
                    "at": "Hãy cùng bóc tách bảng",
                    "image": "assets/long/L04.png",
                    "stickers": [
                        {"at": "chín ngàn chín trăm", "side": "L", "y": 360, "value": "ATK 9999", "label": "sức mạnh tối đa"},
                        {"at": "một ngàn năm trăm Newton", "side": "R", "y": 420, "value": "1.500 N", "label": "lực va chạm"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Tốc độ vung đòn",
                    "image": "assets/long/L03.png",
                    "stickers": [
                        {"at": "mười ngàn bốn trăm g", "side": "L", "y": 380, "value": "10.400 g", "label": "gia tốc thần sầu"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Bạn chớp mắt mất một",
                    "image": "assets/long/L03.png",
                    "stickers": [
                        {"at": "một phần mười", "side": "R", "y": 420, "value": "0.1s", "label": "một cái chớp mắt"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Trong một cái chớp mắt",
                    "image": "assets/long/L02.png",
                    "stickers": [
                        {"at": "ba mươi lần", "side": "R", "y": 380, "value": "30 LẦN", "label": "cú đấm liên hoàn"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Chỉ số phòng thủ",
                    "image": "assets/long/L05.png",
                    "stickers": [
                        {"at": "tám mươi lăm", "side": "L", "y": 360, "value": "DEF 85", "label": "sợi nano chống nứt"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Và chỉ số thị giác",
                    "image": "assets/long/L10.png",
                    "stickers": [
                        {"at": "mười sáu loại tế bào", "side": "R", "y": 400, "value": "16 MÀU", "label": "cực tím & phân cực"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Để bạn dễ hình dung",
                    "image": "assets/long/L03.png",
                    "stickers": [
                        {"at": "chín g", "side": "L", "y": 420, "value": "9 G", "label": "giới hạn phi công"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Vậy mà đôi càng tí hon này",
                    "image": "assets/long/L03.png",
                    "stickers": [
                        {"at": "gấp hơn một ngàn", "side": "R", "y": 400, "value": "> 1.000x", "label": "vượt ngưỡng con người"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Nếu cánh tay của bạn",
                    "image": "assets/long/L02.png",
                    "stickers": [
                        {"at": "quỹ đạo Trái Đất", "side": "R", "y": 380, "value": "VŨ TRỤ", "label": "bay vào quỹ đạo"}
                    ],
                    "impacts": []
                }
            ]
        },
        "scene03": {
            "chapter_no": 3,
            "title": "BỌT KHÍ CAVITATION 4.700°C: NÓNG BẰNG MẶT TRỜI",
            "hook": "VŨ KHÍ VẬT LÝ KỲ DỊ",
            "card": True,
            "beats": [
                {
                    "at": 0,
                    "image": "assets/long/L06.png",
                    "stickers": [
                        {"at": "Cavitation", "side": "L", "y": 380, "value": "CAVITATION", "label": "bọt khí xâm thực"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Do chiếc càng vung đi",
                    "image": "assets/long/L07.png",
                    "stickers": [
                        {"at": "nhiệt độ phòng", "side": "R", "y": 400, "value": "SÔI NƯỚC", "label": "áp suất chân không"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Ngay khoảnh khắc tiếp theo",
                    "image": "assets/long/L06.png",
                    "stickers": [
                        {"at": "bốn ngàn bảy trăm", "side": "R", "y": 360, "value": "4.700°C", "label": "sóng xung kích"}
                    ],
                    "impacts": ["nổ"]
                },
                {
                    "at": "Vụ nổ này thậm chí",
                    "image": "assets/long/L06.png",
                    "stickers": [
                        {"at": "Sonoluminescence", "side": "L", "y": 400, "value": "PHÁT QUANG", "label": "ánh sáng âm thanh"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Nghĩa là mỗi cú ra đòn",
                    "image": "assets/long/L06.png",
                    "stickers": [
                        {"at": "tấn công kép", "side": "R", "y": 420, "value": "ĐÒN KÉP", "label": "càng đập + sóng nhiệt"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Dù nó có đấm trượt",
                    "image": "assets/long/L02.png",
                    "stickers": [
                        {"at": "nướng chín", "side": "L", "y": 380, "value": "NƯỚNG CHÍN", "label": "dù đấm trượt"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Vậy câu hỏi đặt ra",
                    "image": "assets/long/L05.png",
                    "stickers": [
                        {"at": "Bouligand", "side": "R", "y": 400, "value": "BOULIGAND", "label": "cấu trúc nano chống nứt"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Bên trong chiếc càng búa",
                    "image": "assets/long/L05.png",
                    "stickers": [
                        {"at": "hình xoắn ốc", "side": "L", "y": 420, "value": "XOẮN ỐC", "label": "hàng ngàn lớp nano"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Khi một vết nứt nhỏ",
                    "image": "assets/long/L05.png",
                    "stickers": [],
                    "impacts": []
                },
                {
                    "at": "Quân đội Mỹ và các",
                    "image": "assets/long/L14.png",
                    "stickers": [
                        {"at": "áo giáp chống đạn", "side": "R", "y": 380, "value": "ÁO GIÁP", "label": "công nghệ quân sự"}
                    ],
                    "impacts": []
                }
            ]
        },
        "scene04": {
            "chapter_no": 4,
            "title": "MÙA LỘT XÁC: MIẾNG THẠCH BƠ SỢ CẢ ỐC SÊN",
            "hook": "ĐIỂM YẾU BI HÀI",
            "card": True,
            "beats": [
                {
                    "at": 0,
                    "image": "assets/long/L08.png",
                    "stickers": [],
                    "impacts": []
                },
                {
                    "at": "Võ sĩ Mike Tyson đại dương",
                    "image": "assets/long/L08.png",
                    "stickers": [
                        {"at": "Mùa lột xác", "side": "L", "y": 380, "value": "LỘT XÁC", "label": "điểm yếu chí mạng"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Giống như loài tôm cua",
                    "image": "assets/long/L08.png",
                    "stickers": [],
                    "impacts": []
                },
                {
                    "at": "Ngay sau khi lột xác",
                    "image": "assets/long/L08.png",
                    "stickers": [
                        {"at": "mềm nhũn ra", "side": "R", "y": 400, "value": "MỀM NHƯ BƠ", "label": "không còn áo giáp"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Kẻ từng đấm nứt kính",
                    "image": "assets/long/L09.png",
                    "stickers": [
                        {"at": "chú ốc sên bò qua", "side": "L", "y": 420, "value": "SỢ ỐC SÊN", "label": "kẻ thù đáng sợ nhất"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Trong suốt vài tuần chờ",
                    "image": "assets/long/L09.png",
                    "stickers": [
                        {"at": "đáy hang sâu", "side": "R", "y": 380, "value": "TRỐN HANG", "label": "nhịn đói & run rẩy"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Điều hài hước nhất là",
                    "image": "assets/long/L09.png",
                    "stickers": [],
                    "impacts": []
                },
                {
                    "at": "Nếu chẳng may có kẻ thù",
                    "image": "assets/long/L09.png",
                    "stickers": [
                        {"at": "đòn nghi binh", "side": "L", "y": 400, "value": "NGHI BINH", "label": "giương càng dọa ma"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Nhưng thực chất đó hoàn toàn",
                    "image": "assets/long/L09.png",
                    "stickers": [],
                    "impacts": []
                },
                {
                    "at": "Nếu kẻ thù liều lĩnh",
                    "image": "assets/long/L08.png",
                    "stickers": [],
                    "impacts": []
                },
                {
                    "at": "Ngoài ra gã này còn",
                    "image": "assets/long/L12.png",
                    "stickers": [
                        {"at": "ác mộng kinh hoàng", "side": "R", "y": 380, "value": "ÁC MỘNG", "label": "người nuôi cá cảnh"}
                    ],
                    "impacts": []
                }
            ]
        },
        "scene05": {
            "chapter_no": 5,
            "title": "VỤ ÁN THỦY CUNG NƯỚC ANH VÀ MẮT 16 MÀU",
            "hook": "BỂ KÍNH VỠ NÁT",
            "card": True,
            "beats": [
                {
                    "at": 0,
                    "image": "assets/long/L12.png",
                    "stickers": [],
                    "impacts": []
                },
                {
                    "at": "Vào tháng tư năm 1998",
                    "image": "assets/long/L12.png",
                    "stickers": [
                        {"at": "năm 1998", "side": "L", "y": 380, "value": "NĂM 1998", "label": "thủy cung Norfolk"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Có vẻ như bực mình vì",
                    "image": "assets/long/L12.png",
                    "stickers": [
                        {"at": "sáu mi-li-mét", "side": "R", "y": 400, "value": "> 6 mm", "label": "kính cường lực"}
                    ],
                    "impacts": ["đấm"]
                },
                {
                    "at": "Kết quả là mặt kính",
                    "image": "assets/long/L13.png",
                    "stickers": [
                        {"at": "hình mạng nhện", "side": "L", "y": 420, "value": "SƠ TÁN", "label": "báo động khẩn cấp"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Từ đó các viện hải dương",
                    "image": "assets/long/L14.png",
                    "stickers": [
                        {"at": "nhựa acrylic", "side": "R", "y": 380, "value": "ACRYLIC", "label": "chống đạn siêu dày"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Bên cạnh cú đấm thần sầu",
                    "image": "assets/long/L10.png",
                    "stickers": [
                        {"at": "ba loại tế bào", "side": "L", "y": 400, "value": "3 MÀU", "label": "con người"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Nó không chỉ nhìn thấy",
                    "image": "assets/long/L10.png",
                    "stickers": [
                        {"at": "gấp năm lần", "side": "R", "y": 360, "value": "x5 LẦN", "label": "rực rỡ hơn người"},
                        {"at": "phân cực tròn", "side": "L", "y": 420, "value": "CỰC TÍM UV", "label": "ánh sáng phân cực"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Mỗi con mắt của nó",
                    "image": "assets/long/L10.png",
                    "stickers": [
                        {"at": "ba trăm sáu mươi độ", "side": "R", "y": 380, "value": "360°", "label": "xoay độc lập & 3D"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Các nhà khoa học hiện đang",
                    "image": "assets/long/L11.png",
                    "stickers": [
                        {"at": "tế bào ung thư", "side": "L", "y": 400, "value": "Y HỌC", "label": "phát hiện sớm ung thư"}
                    ],
                    "impacts": []
                }
            ]
        },
        "scene06": {
            "chapter_no": 6,
            "title": "BÀI HỌC TỪ TÔM TÍT VÀ TEASER TẬP TIẾP THEO",
            "hook": "TRIẾT LÝ SINH TỒN",
            "card": True,
            "beats": [
                {
                    "at": 0,
                    "image": "assets/long/L15.png",
                    "stickers": [],
                    "impacts": []
                },
                {
                    "at": "Sở hữu sức mạnh vô song",
                    "image": "assets/long/L15.png",
                    "stickers": [],
                    "impacts": []
                },
                {
                    "at": "Đỉnh cao thực sự của",
                    "image": "assets/long/L16.png",
                    "stickers": [
                        {"at": "nhẫn nhịn thu mình", "side": "L", "y": 380, "value": "BÀI HỌC", "label": "khiêm tốn & nhẫn nhịn"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Bạn ấn tượng nhất với",
                    "image": "assets/long/L17.png",
                    "stickers": [
                        {"at": "để lại bình luận", "side": "R", "y": 400, "value": "BÌNH LUẬN", "label": "chia sẻ cảm nghĩ"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Ở tập tiếp theo chúng ta",
                    "image": "assets/long/L18.png",
                    "stickers": [
                        {"at": "biết trèo cây", "side": "L", "y": 380, "value": "TẬP 8", "label": "Cá Thòi Lòi biết trèo cây"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Bạn có đoán được đó",
                    "image": "assets/long/L18.png",
                    "stickers": [],
                    "impacts": []
                },
                {
                    "at": "Đừng quên bấm Đăng ký",
                    "image": "assets/long/L17.png",
                    "stickers": [
                        {"at": "Đăng ký kênh", "side": "R", "y": 380, "value": "ĐĂNG KÝ", "label": "Vẽ Chuyện Hoang Dã"}
                    ],
                    "impacts": []
                }
            ]
        }
    }
}

# 2. SHORTS PLAN
shorts_plan = {
    "title_lines": [
        "CÚ ĐẤM NÓNG BẰNG MẶT TRỜI",
        "ĐẤM VỠ CẢ BỂ KÍNH?!"
    ],
    "beats": [
        {
            "at_s": 0.0,
            "image": "assets/shorts/S01.png",
            "draw_s": 1.1,
            "stickers": [
                {"at_s": 0.5, "side": "L", "y": 800, "value": "1 VIÊN ĐẠN", "label": "súng trường dưới nước"}
            ]
        },
        {
            "at": "nhiệt độ bốn ngàn",
            "image": "assets/shorts/S05.png",
            "draw_s": 1.1,
            "stickers": [
                {"at": "bốn ngàn bảy trăm", "side": "R", "y": 700, "value": "4.700°C", "label": "nóng ngang Mặt Trời"}
            ]
        },
        {
            "at": "Kẻ sở hữu siêu",
            "image": "assets/shorts/S02.png",
            "draw_s": 1.1,
            "stickers": [
                {"at": "Mike Tyson", "side": "L", "y": 750, "value": "TYSON", "label": "võ sĩ đại dương"}
            ]
        },
        {
            "at": "Với đôi càng búa",
            "image": "assets/shorts/S03.png",
            "draw_s": 1.1,
            "stickers": [
                {"at": "mười ngàn bốn trăm", "side": "R", "y": 720, "value": "10.400 g", "label": "gia tốc thần sầu"}
            ]
        },
        {
            "at": "và thậm chí từng",
            "image": "assets/shorts/S04.png",
            "draw_s": 1.1,
            "stickers": [
                {"at": "mặt kính bể cá", "side": "L", "y": 780, "value": "NỨT KÍNH", "label": "thủy cung nước Anh"}
            ]
        },
        {
            "at": "Cú vung càng nhanh",
            "image": "assets/shorts/S11.png",
            "draw_s": 1.1,
            "stickers": [
                {"at": "sôi nước biển", "side": "R", "y": 740, "value": "SÔI NƯỚC", "label": "nướng chín con mồi"}
            ]
        },
        {
            "at": "Thế nhưng cứ mỗi",
            "image": "assets/shorts/S06.png",
            "draw_s": 1.1,
            "stickers": [
                {"at": "thạch bơ mềm nhũn", "side": "L", "y": 750, "value": "MỀM NHƯ THẠCH", "label": "mùa lột xác"}
            ]
        },
        {
            "at": "phải trốn chui trốn",
            "image": "assets/shorts/S07.png",
            "draw_s": 1.1,
            "stickers": [
                {"at": "một con ốc sên", "side": "R", "y": 780, "value": "SỢ ỐC SÊN", "label": "trốn trong hang sâu"}
            ]
        },
        {
            "at": "Bí mật về đôi",
            "image": "assets/shorts/S08.png",
            "draw_s": 1.0,
            "stickers": [
                {"at": "mười sáu dải màu", "side": "L", "y": 720, "value": "16 MÀU", "label": "thị giác siêu cấp"}
            ]
        },
        {
            "at": "giúp phát hiện ung",
            "image": "assets/shorts/S09.png",
            "draw_s": 1.0,
            "stickers": [
                {"at": "phát hiện ung thư", "side": "R", "y": 750, "value": "Y HỌC", "label": "tầm soát ung thư"}
            ]
        },
        {
            "at": "đã có ở video",
            "image": "assets/shorts/S10.png",
            "draw_s": 1.1,
            "stickers": [
                {"at": "Bấm xem ngay", "side": "R", "y": 750, "value": "XEM NGAY", "label": "Tập 7 bản đầy đủ"}
            ]
        }
    ]
}

with open(specs / "longform_plan.json", "w", encoding="utf-8") as f:
    json.dump(longform_plan, f, ensure_ascii=False, indent=2)

with open(specs / "shorts_plan.json", "w", encoding="utf-8") as f:
    json.dump(shorts_plan, f, ensure_ascii=False, indent=2)

print("Saved specs/longform_plan.json and specs/shorts_plan.json successfully!")

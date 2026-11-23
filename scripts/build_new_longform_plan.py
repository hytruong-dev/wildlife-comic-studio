import json
from pathlib import Path

P = Path("projects/tap-07-tom-tit")
specs = P / "specs"

# Plan with 46 distinct beats, NO consecutive duplicates, 100% narrative match!
longform_plan_fixed = {
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
            "title": "VÕ SĨ QUYỀN ANH LÒE LOẸT NHẤT ĐẠI DƯƠNG",
            "hook": "",
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
                    "image": "assets/shorts/S02.png",
                    "stickers": [
                        {"at": "Mike Tyson", "side": "R", "y": 420, "value": "TYSON", "label": "võ sĩ đại dương"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Nhìn từ xa",
                    "image": "assets/long/L19.png",
                    "stickers": [
                        {"at": "ra-đa", "side": "R", "y": 380, "value": "RA-ĐA", "label": "mắt lồi xoay độc lập"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Thế nhưng ẩn dưới",
                    "image": "assets/shorts/S01.png",
                    "stickers": [
                        {"at": "súng trường", "side": "R", "y": 380, "value": "NHƯ ĐẠN", "label": "tốc độ súng trường"}
                    ],
                    "impacts": ["súng"]
                },
                {
                    "at": "Cua biển mai dày",
                    "image": "assets/shorts/S03.png",
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
                    "at": "Một gã tí hon dưới đáy",
                    "image": "assets/long/L20.png",
                    "stickers": [
                        {"at": "giang hồ", "side": "R", "y": 420, "value": "GIANG HỒ", "label": "gã tí hon cục súc"}
                    ],
                    "impacts": []
                }
            ]
        },
        "scene02": {
            "chapter_no": 2,
            "title": "BẢNG CHỈ SỐ RPG — LỖI GAME CỦA TẠO HÓA",
            "hook": "KHI THIÊN NHIÊN QUÊN CÀI GIỚI HẠN SÁT THƯƠNG",
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
                    "image": "assets/long/L21.png",
                    "stickers": [
                        {"at": "chín ngàn chín trăm", "side": "L", "y": 360, "value": "ATK 9999", "label": "sức mạnh tối đa"},
                        {"at": "một ngàn năm trăm Newton", "side": "R", "y": 420, "value": "1.500 N", "label": "lực va chạm"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Tốc độ vung đòn",
                    "image": "assets/long/L22.png",
                    "stickers": [
                        {"at": "mười ngàn bốn trăm g", "side": "L", "y": 380, "value": "10.400 g", "label": "gia tốc thần sầu"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Bạn chớp mắt mất một",
                    "image": "assets/long/L23.png",
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
                    "image": "assets/shorts/S08.png",
                    "stickers": [
                        {"at": "mười sáu loại tế bào", "side": "R", "y": 400, "value": "16 MÀU", "label": "cực tím & phân cực"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Để bạn dễ hình dung",
                    "image": "assets/long/L14.png",
                    "stickers": [
                        {"at": "chín g", "side": "L", "y": 420, "value": "9 G", "label": "giới hạn phi công"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Vậy mà đôi càng tí hon này",
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
            "title": "CÚ ĐẤM CAVITATION & GIÁP NANO BOULIGAND",
            "hook": "TẠO RA SỨC NÓNG NGANG BỀ MẶT MẶT TRỜI",
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
                    "image": "assets/shorts/S05.png",
                    "stickers": [
                        {"at": "bốn ngàn bảy trăm", "side": "R", "y": 360, "value": "4.700°C", "label": "sóng xung kích"}
                    ],
                    "impacts": ["nổ"]
                },
                {
                    "at": "Vụ nổ này thậm chí",
                    "image": "assets/shorts/S11.png",
                    "stickers": [
                        {"at": "Sonoluminescence", "side": "L", "y": 400, "value": "PHÁT QUANG", "label": "ánh sáng âm thanh"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Nghĩa là mỗi cú ra đòn",
                    "image": "assets/shorts/S01.png",
                    "stickers": [
                        {"at": "tấn công kép", "side": "R", "y": 420, "value": "ĐÒN KÉP", "label": "càng đập + sóng nhiệt"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Dù nó có đấm trượt",
                    "image": "assets/shorts/S03.png",
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
                    "at": "Khi một vết nứt nhỏ",
                    "image": "assets/long/L07.png",
                    "stickers": [
                        {"at": "tiêu tán năng lượng", "side": "L", "y": 420, "value": "TIÊU TÁN", "label": "bẻ cong vết nứt"}
                    ],
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
            "title": "GÓT CHÂN A-SIN — MÙA LỘT XÁC MỀM NHƯ THẠCH",
            "hook": "VÕ SĨ VÔ ĐỊCH BIẾN THÀNH MIẾNG THẠCH BƠ",
            "card": True,
            "beats": [
                {
                    "at": 0,
                    "image": "assets/shorts/S02.png",
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
                    "at": "Ngay sau khi lột xác",
                    "image": "assets/shorts/S06.png",
                    "stickers": [
                        {"at": "mềm nhũn ra", "side": "R", "y": 400, "value": "MỀM NHƯ BƠ", "label": "không còn áo giáp"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Kẻ từng đấm nứt kính",
                    "image": "assets/shorts/S07.png",
                    "stickers": [
                        {"at": "chú ốc sên", "side": "L", "y": 420, "value": "SỢ ỐC SÊN", "label": "kẻ thù đáng sợ nhất"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Trong suốt vài tuần chờ",
                    "image": "assets/long/L20.png",
                    "stickers": [
                        {"at": "đáy hang sâu", "side": "R", "y": 380, "value": "TRỐN HANG", "label": "nhịn đói & run rẩy"}
                    ],
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
                    "at": "Nếu kẻ thù liều lĩnh",
                    "image": "assets/long/L08.png",
                    "stickers": [
                        {"at": "đau thấu trời xanh", "side": "L", "y": 400, "value": "ĐAU ĐỚN", "label": "càng mềm chạm đá"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Ngoài ra gã này còn",
                    "image": "assets/shorts/S04.png",
                    "stickers": [
                        {"at": "ác mộng kinh hoàng", "side": "R", "y": 380, "value": "ÁC MỘNG", "label": "người nuôi cá cảnh"}
                    ],
                    "impacts": []
                }
            ]
        },
        "scene05": {
            "chapter_no": 5,
            "title": "VỤ ÁN THỦY CUNG BỂ NÁT & ĐÔI MẮT THẦN 16 MÀU",
            "hook": "ĐẤM NỨT KÍNH THỦY CUNG VÀ NHÌN THẤY TẾ BÀO UNG THƯ",
            "card": True,
            "beats": [
                {
                    "at": 0,
                    "image": "assets/long/L12.png",
                    "stickers": [
                        {"at": "năm 1998", "side": "L", "y": 380, "value": "NĂM 1998", "label": "thủy cung Norfolk"}
                    ],
                    "impacts": []
                },
                {
                    "at": "Có vẻ như bực mình vì",
                    "image": "assets/shorts/S04.png",
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
                    "image": "assets/long/L19.png",
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
                    "image": "assets/shorts/S08.png",
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
            "title": "BÀI HỌC SINH TỒN TỪ TÔM TÍT",
            "hook": "BIẾT THU MÌNH KHI YẾU MỀM MỚI LÀ KẺ KHÔN NGOAN",
            "card": True,
            "beats": [
                {
                    "at": 0,
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
                    "at": "Đừng quên bấm Đăng ký",
                    "image": "assets/shorts/S10.png",
                    "stickers": [
                        {"at": "Đăng ký kênh", "side": "R", "y": 380, "value": "ĐĂNG KÝ", "label": "Vẽ Chuyện Hoang Dã"}
                    ],
                    "impacts": []
                }
            ]
        }
    }
}

with open(specs / "longform_plan.json", "w", encoding="utf-8") as f:
    json.dump(longform_plan_fixed, f, ensure_ascii=False, indent=2)

print("Saved new longform_plan.json successfully!")

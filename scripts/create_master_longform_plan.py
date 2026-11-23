import json
from pathlib import Path

P = Path("projects/tap-07-tom-tit")
specs = P / "specs"

# Master longform plan using EXCLUSIVELY 16:9 horizontal images L01-L32,
# with exact narrative matching, no consecutive duplicates, and arrows (targets) on all stickers!
master_longform_plan = {
    "targets": {
        "TYSON": [0.65, 0.45],
        "RADAR_EYE": [0.55, 0.35],
        "BULLET_CLAW": [0.65, 0.45],
        "CRAB_CRACK": [0.65, 0.50],
        "TANK_CRACK": [0.50, 0.45],
        "FINGER_CUT": [0.55, 0.50],
        "GANGSTER": [0.50, 0.55],
        "RPG_ATK": [0.45, 0.45],
        "SPEED_RACE": [0.60, 0.50],
        "BLINK_PUNCH": [0.65, 0.45],
        "NANO_DEF": [0.50, 0.50],
        "VISION_16": [0.65, 0.45],
        "PILOT_9G": [0.45, 0.45],
        "BASEBALL_ORBIT": [0.65, 0.40],
        "CAVIT_BUBBLE": [0.55, 0.50],
        "WATER_BOIL": [0.50, 0.50],
        "SUN_HEAT": [0.60, 0.45],
        "SONO_LIGHT": [0.50, 0.50],
        "COOKED_CRAB": [0.65, 0.55],
        "BOULIGAND": [0.50, 0.50],
        "CRACK_BEND": [0.55, 0.50],
        "ARMOR_TECH": [0.50, 0.50],
        "MOLT_WEAK": [0.50, 0.55],
        "FLAN_MOLT": [0.50, 0.55],
        "SNAIL_SCARE": [0.65, 0.55],
        "DEEP_CAVE": [0.50, 0.55],
        "BLUFF_CLAW": [0.50, 0.45],
        "AQUARIUM_NIGHTMARE": [0.50, 0.45],
        "NORFOLK_BREAK": [0.50, 0.45],
        "WATER_BURST": [0.55, 0.50],
        "ACRYLIC_TANK": [0.50, 0.45],
        "RADAR_3D": [0.55, 0.35],
        "CANCER_SENSOR": [0.55, 0.45],
        "LESSON": [0.50, 0.50],
        "PATIENCE_CAVE": [0.50, 0.55],
        "COMMENT_CHOICE": [0.50, 0.50],
        "MUD_FISH": [0.55, 0.50],
        "SUBSCRIBE_CTA": [0.50, 0.50]
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
                        {"at": "20cm", "side": "L", "y": 380, "value": "< 20 cm", "label": "chiều dài tí hon", "target": [0.45, 0.55]},
                        {"at": "Mike Tyson", "side": "R", "y": 420, "value": "TYSON", "label": "võ sĩ đại dương", "target": [0.65, 0.45]}
                    ],
                    "impacts": []
                },
                {
                    "at": "Nhìn từ xa chú ta",
                    "image": "assets/long/L19.png",
                    "stickers": [
                        {"at": "ra-đa", "side": "R", "y": 380, "value": "RA-ĐA", "label": "mắt lồi xoay độc lập", "target": [0.55, 0.35]}
                    ],
                    "impacts": []
                },
                {
                    "at": "Thế nhưng ẩn dưới bộ",
                    "image": "assets/long/L02.png",
                    "stickers": [
                        {"at": "súng trường", "side": "R", "y": 380, "value": "NHƯ ĐẠN", "label": "tốc độ súng trường", "target": [0.65, 0.45]}
                    ],
                    "impacts": ["súng"]
                },
                {
                    "at": "Cua biển mai dày",
                    "image": "assets/long/L32.png",
                    "stickers": [
                        {"at": "Một đấm vỡ nát", "side": "L", "y": 380, "value": "1 ĐẤM", "label": "vỡ nát mai cua", "target": [0.60, 0.50]},
                        {"at": "thành bột vụn", "side": "R", "y": 420, "value": "2 ĐẤM", "label": "nghiền nát vỏ ốc", "target": [0.75, 0.60]}
                    ],
                    "impacts": ["đấm", "bột"]
                },
                {
                    "at": "Thậm chí ngay cả mặt",
                    "image": "assets/long/L12.png",
                    "stickers": [
                        {"at": "đấm nứt toác", "side": "L", "y": 400, "value": "NỨT KÍNH", "label": "bể cá dày vài cm", "target": [0.55, 0.45]}
                    ],
                    "impacts": ["nứt"]
                },
                {
                    "at": "Các thợ lặn biển từ",
                    "image": "assets/long/L03.png",
                    "stickers": [
                        {"at": "Kẻ Chẻ Ngón Tay", "side": "L", "y": 380, "value": "CẢNH BÁO", "label": "kẻ chẻ ngón tay", "target": [0.45, 0.50]},
                        {"at": "đập vỡ nát móng tay", "side": "R", "y": 420, "value": "TOẠC THỊT", "label": "tới tận xương", "target": [0.60, 0.55]}
                    ],
                    "impacts": ["toạc"]
                },
                {
                    "at": "Một gã tí hon dưới",
                    "image": "assets/long/L20.png",
                    "stickers": [
                        {"at": "giang hồ", "side": "R", "y": 420, "value": "GIANG HỒ", "label": "gã tí hon cục súc", "target": [0.50, 0.55]}
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
                        {"at": "ATK:", "side": "L", "y": 360, "value": "ATK 9999", "label": "sức mạnh tối đa", "target": [0.35, 0.45]},
                        {"at": "1.500 Newton", "side": "R", "y": 420, "value": "1.500 N", "label": "lực va chạm", "target": [0.70, 0.50]}
                    ],
                    "impacts": ["tạ"]
                },
                {
                    "at": "Tốc độ vung đòn",
                    "image": "assets/long/L22.png",
                    "stickers": [
                        {"at": "SPD:", "side": "L", "y": 360, "value": "SPD 999", "label": "tốc độ tối đa", "target": [0.25, 0.40]},
                        {"at": "10.400g", "side": "R", "y": 420, "value": "10.400 g", "label": "nhanh hơn đạn 22 ly", "target": [0.65, 0.45]}
                    ],
                    "impacts": ["đạn"]
                },
                {
                    "at": "Bạn chớp mắt mất",
                    "image": "assets/long/L23.png",
                    "stickers": [
                        {"at": "0,1s", "side": "L", "y": 380, "value": "0,1s", "label": "1 cái chớp mắt", "target": [0.30, 0.45]},
                        {"at": "30 lần", "side": "R", "y": 420, "value": "30 ĐẤM", "label": "liên hoàn cước", "target": [0.70, 0.45]}
                    ],
                    "impacts": []
                },
                {
                    "at": "Chỉ số phòng thủ",
                    "image": "assets/long/L05.png",
                    "stickers": [
                        {"at": "DEF:", "side": "L", "y": 360, "value": "DEF 85", "label": "giáp nano chống nứt", "target": [0.50, 0.50]}
                    ],
                    "impacts": []
                },
                {
                    "at": "Và chỉ số thị giác",
                    "image": "assets/long/L31.png",
                    "stickers": [
                        {"at": "16 loại tế bào", "side": "R", "y": 400, "value": "16 MÀU", "label": "quang phổ cực tím & UV", "target": [0.70, 0.45]}
                    ],
                    "impacts": []
                },
                {
                    "at": "Để bạn dễ hình dung",
                    "image": "assets/long/L14.png",
                    "stickers": [
                        {"at": "9g", "side": "L", "y": 420, "value": "9 G", "label": "giới hạn phi công tiêm kích", "target": [0.45, 0.45]}
                    ],
                    "impacts": []
                },
                {
                    "at": "Nếu cánh tay của bạn",
                    "image": "assets/long/L24.png",
                    "stickers": [
                        {"at": "quỹ đạo Trái Đất", "side": "R", "y": 380, "value": "VŨ TRỤ", "label": "ném bóng vào quỹ đạo", "target": [0.65, 0.40]}
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
                        {"at": "Cavitation", "side": "L", "y": 380, "value": "CAVITATION", "label": "bọt khí xâm thực", "target": [0.55, 0.50]}
                    ],
                    "impacts": []
                },
                {
                    "at": "Do chiếc càng vung đi",
                    "image": "assets/long/L07.png",
                    "stickers": [
                        {"at": "chân không", "side": "L", "y": 380, "value": "CHÂN KHÔNG", "label": "áp suất sụt giảm", "target": [0.35, 0.45]},
                        {"at": "nhiệt độ phòng", "side": "R", "y": 420, "value": "NƯỚC SÔI", "label": "ngay nhiệt độ phòng", "target": [0.65, 0.50]}
                    ],
                    "impacts": []
                },
                {
                    "at": "Ngay khoảnh khắc tiếp",
                    "image": "assets/long/L25.png",
                    "stickers": [
                        {"at": "4.700°C", "side": "R", "y": 380, "value": "4.700°C", "label": "nóng ngang Mặt Trời", "target": [0.65, 0.45]}
                    ],
                    "impacts": ["nổ", "mặt trời"]
                },
                {
                    "at": "Vụ nổ này thậm chí",
                    "image": "assets/long/L26.png",
                    "stickers": [
                        {"at": "Sonoluminescence", "side": "L", "y": 400, "value": "PHÁT QUANG", "label": "âm thanh sinh ánh sáng", "target": [0.50, 0.50]}
                    ],
                    "impacts": []
                },
                {
                    "at": "Nghĩa là mỗi cú ra đòn",
                    "image": "assets/long/L02.png",
                    "stickers": [
                        {"at": "tấn công kép", "side": "R", "y": 420, "value": "ĐÒN KÉP", "label": "càng đập + sóng nhiệt", "target": [0.65, 0.45]}
                    ],
                    "impacts": []
                },
                {
                    "at": "Dù nó có đấm trượt",
                    "image": "assets/long/L27.png",
                    "stickers": [
                        {"at": "nướng chín", "side": "L", "y": 380, "value": "NƯỚNG CHÍN", "label": "sóng xung kích nấu chín", "target": [0.65, 0.55]}
                    ],
                    "impacts": []
                },
                {
                    "at": "Vậy câu hỏi đặt ra",
                    "image": "assets/long/L05.png",
                    "stickers": [
                        {"at": "Bouligand", "side": "R", "y": 400, "value": "BOULIGAND", "label": "cấu trúc nano chống nứt", "target": [0.50, 0.50]}
                    ],
                    "impacts": []
                },
                {
                    "at": "Bên trong chiếc càng",
                    "image": "assets/long/L07.png",
                    "stickers": [
                        {"at": "xoắn ốc", "side": "L", "y": 400, "value": "XOẮN ỐC", "label": "hàng ngàn lớp ván ép", "target": [0.50, 0.50]},
                        {"at": "tiêu tán năng lượng", "side": "R", "y": 420, "value": "TIÊU TÁN", "label": "tự bẻ cong vết nứt", "target": [0.60, 0.55]}
                    ],
                    "impacts": []
                },
                {
                    "at": "Quân đội Mỹ và các",
                    "image": "assets/long/L14.png",
                    "stickers": [
                        {"at": "áo giáp chống đạn", "side": "R", "y": 380, "value": "ÁO GIÁP", "label": "công nghệ quân sự & vũ trụ", "target": [0.50, 0.50]}
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
                    "image": "assets/long/L01.png",
                    "stickers": [],
                    "impacts": []
                },
                {
                    "at": "Võ sĩ Mike Tyson đại dương",
                    "image": "assets/long/L08.png",
                    "stickers": [
                        {"at": "Mùa lột xác", "side": "L", "y": 380, "value": "LỘT XÁC", "label": "điểm yếu chí mạng", "target": [0.50, 0.55]}
                    ],
                    "impacts": []
                },
                {
                    "at": "Ngay sau khi lột xác",
                    "image": "assets/long/L28.png",
                    "stickers": [
                        {"at": "mềm nhũn ra", "side": "R", "y": 400, "value": "MỀM NHƯ BƠ", "label": "như bánh flan thạch dừa", "target": [0.50, 0.55]}
                    ],
                    "impacts": []
                },
                {
                    "at": "Kẻ từng đấm nứt kính",
                    "image": "assets/long/L29.png",
                    "stickers": [
                        {"at": "chú ốc sên", "side": "L", "y": 420, "value": "SỢ ỐC SÊN", "label": "kẻ thù đáng sợ nhất", "target": [0.65, 0.55]}
                    ],
                    "impacts": []
                },
                {
                    "at": "Trong suốt vài tuần",
                    "image": "assets/long/L20.png",
                    "stickers": [
                        {"at": "đáy hang sâu", "side": "R", "y": 380, "value": "TRỐN HANG", "label": "nhịn đói & run rẩy", "target": [0.50, 0.55]}
                    ],
                    "impacts": []
                },
                {
                    "at": "Nếu chẳng may có kẻ",
                    "image": "assets/long/L09.png",
                    "stickers": [
                        {"at": "dọa ma", "side": "L", "y": 380, "value": "DỌA MA", "label": "nghệ thuật dọa ma", "target": [0.45, 0.45]},
                        {"at": "nghi binh trắng trợn", "side": "R", "y": 420, "value": "NGHI BINH", "label": "giương càng mềm oặt", "target": [0.60, 0.50]}
                    ],
                    "impacts": []
                },
                {
                    "at": "Nếu kẻ thù liều lĩnh",
                    "image": "assets/long/L08.png",
                    "stickers": [
                        {"at": "đau thấu trời xanh", "side": "L", "y": 400, "value": "ĐAU ĐỚN", "label": "càng mềm chạm đá", "target": [0.50, 0.55]}
                    ],
                    "impacts": []
                },
                {
                    "at": "Ngoài ra gã này còn",
                    "image": "assets/long/L30.png",
                    "stickers": [
                        {"at": "ác mộng kinh hoàng", "side": "R", "y": 380, "value": "ÁC MỘNG", "label": "người nuôi cá cảnh", "target": [0.70, 0.45]},
                        {"at": "nứt một vệt dài", "side": "L", "y": 420, "value": "VỠ BỂ", "label": "bể nứt tung tóe", "target": [0.45, 0.50]}
                    ],
                    "impacts": ["nứt"]
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
                        {"at": "tháng 4 năm 1998", "side": "L", "y": 380, "value": "NĂM 1998", "label": "thủy cung Norfolk", "target": [0.35, 0.45]},
                        {"at": "10cm", "side": "R", "y": 420, "value": "10 cm", "label": "chú tôm Tyson", "target": [0.65, 0.50]}
                    ],
                    "impacts": []
                },
                {
                    "at": "Có vẻ như bực mình",
                    "image": "assets/long/L02.png",
                    "stickers": [
                        {"at": "6mm", "side": "R", "y": 400, "value": "> 6 mm", "label": "kính cường lực", "target": [0.65, 0.45]}
                    ],
                    "impacts": ["đấm"]
                },
                {
                    "at": "Kết quả là mặt kính",
                    "image": "assets/long/L13.png",
                    "stickers": [
                        {"at": "hình mạng nhện", "side": "L", "y": 420, "value": "SƠ TÁN", "label": "báo động khẩn cấp", "target": [0.55, 0.50]}
                    ],
                    "impacts": []
                },
                {
                    "at": "Từ đó các viện hải",
                    "image": "assets/long/L14.png",
                    "stickers": [
                        {"at": "nhựa acrylic", "side": "R", "y": 380, "value": "ACRYLIC", "label": "chống đạn siêu dày", "target": [0.50, 0.50]}
                    ],
                    "impacts": []
                },
                {
                    "at": "Bên cạnh cú đấm thần",
                    "image": "assets/long/L19.png",
                    "stickers": [
                        {"at": "3 loại tế bào", "side": "L", "y": 400, "value": "3 MÀU", "label": "con người", "target": [0.45, 0.35]}
                    ],
                    "impacts": []
                },
                {
                    "at": "Nó không chỉ nhìn",
                    "image": "assets/long/L10.png",
                    "stickers": [
                        {"at": "5 lần", "side": "R", "y": 360, "value": "x5 LẦN", "label": "rực rỡ hơn người", "target": [0.65, 0.45]},
                        {"at": "phân cực tròn", "side": "L", "y": 420, "value": "CỰC TÍM UV", "label": "ánh sáng phân cực", "target": [0.35, 0.50]}
                    ],
                    "impacts": []
                },
                {
                    "at": "Mỗi con mắt của nó",
                    "image": "assets/long/L31.png",
                    "stickers": [
                        {"at": "360°", "side": "R", "y": 380, "value": "360°", "label": "xoay độc lập & 3D", "target": [0.70, 0.45]}
                    ],
                    "impacts": []
                },
                {
                    "at": "Các nhà khoa học hiện",
                    "image": "assets/long/L11.png",
                    "stickers": [
                        {"at": "tế bào ung thư", "side": "L", "y": 400, "value": "Y HỌC", "label": "phát hiện sớm ung thư", "target": [0.55, 0.45]}
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
                    "image": "assets/long/L01.png",
                    "stickers": [],
                    "impacts": []
                },
                {
                    "at": "Sở hữu sức mạnh vô",
                    "image": "assets/long/L15.png",
                    "stickers": [
                        {"at": "bất khả chiến bại", "side": "L", "y": 380, "value": "BÀI HỌC", "label": "không bất khả chiến bại", "target": [0.50, 0.50]}
                    ],
                    "impacts": []
                },
                {
                    "at": "Đỉnh cao thực sự của",
                    "image": "assets/long/L16.png",
                    "stickers": [
                        {"at": "nhẫn nhịn", "side": "R", "y": 380, "value": "KHIÊM TỐN", "label": "nhẫn nhịn chờ thời", "target": [0.50, 0.55]}
                    ],
                    "impacts": []
                },
                {
                    "at": "Bạn ấn tượng nhất với",
                    "image": "assets/long/L17.png",
                    "stickers": [
                        {"at": "bình luận", "side": "R", "y": 400, "value": "BÌNH LUẬN", "label": "chia sẻ cảm nghĩ", "target": [0.50, 0.50]}
                    ],
                    "impacts": []
                },
                {
                    "at": "Ở tập tiếp theo chúng",
                    "image": "assets/long/L18.png",
                    "stickers": [
                        {"at": "trèo cây", "side": "L", "y": 380, "value": "TẬP 8", "label": "Cá Thòi Lòi biết trèo cây", "target": [0.55, 0.50]}
                    ],
                    "impacts": []
                },
                {
                    "at": "Đừng quên bấm Đăng",
                    "image": "assets/long/L17.png",
                    "stickers": [
                        {"at": "Đăng ký kênh", "side": "R", "y": 380, "value": "ĐĂNG KÝ", "label": "Vẽ Chuyện Hoang Dã", "target": [0.50, 0.50]}
                    ],
                    "impacts": []
                }
            ]
        }
    }
}

with open(specs / "longform_plan.json", "w", encoding="utf-8") as f:
    json.dump(master_longform_plan, f, ensure_ascii=False, indent=2)

print("Saved master longform_plan.json successfully!")

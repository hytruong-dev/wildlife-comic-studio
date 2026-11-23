import json
import re
from pathlib import Path

P = Path("projects/tap-08-chon-gulo")
A = P / "audio"
ep = json.loads((P / "episode.json").read_text(encoding="utf-8"))
words = json.loads((A / "long_words_fixed.json").read_text(encoding="utf-8"))
shorts_words = json.loads((A / "shorts_words.json").read_text(encoding="utf-8"))

false = False
true = True

scenes_data = {
    "scene01": {
        "chapter_no": 1,
        "title": "GÃ CHÍ PHÈO XỨ TUYẾT DÁM CƯỚP MỒI CỦA GẤU XÁM",
        "hook": "Kẻ điên rồ nhất vùng băng giá Bắc Cực",
        "card": false,
        "beats": [
            {
                "at": 0,
                "image": "assets/long/L01.png",
                "stickers": [],
                "impacts": []
            },
            {
                "at": "Một sinh vật thân hình",
                "image": "assets/long/L02.png",
                "stickers": [
                    {"at": "15kg", "side": "L", "y": 380, "value": "15 kg", "label": "cân nặng tí hon", "target": [0.35, 0.55]}
                ],
                "impacts": []
            },
            {
                "at": "Hãy làm quen với Chồn",
                "image": "assets/long/L03.png",
                "stickers": [
                    {"at": "Marvel", "side": "R", "y": 420, "value": "MARVEL", "label": "nguyên mẫu Người Sói", "target": [0.65, 0.45]}
                ],
                "impacts": []
            },
            {
                "at": "Nhìn bề ngoài, chú ta",
                "image": "assets/long/L04.png",
                "stickers": [],
                "impacts": []
            },
            {
                "at": "Thế nhưng, ẩn sau ngoại",
                "image": "assets/long/L05.png",
                "stickers": [],
                "impacts": ["cục súc và liều lĩnh"]
            },
            {
                "at": "Kẻ thù thấy nó thì",
                "image": "assets/long/L06.png",
                "stickers": [],
                "impacts": []
            },
            {
                "at": "Các nhà động vật học",
                "image": "assets/long/L07.png",
                "stickers": [
                    {"at": "Lửng Mật", "side": "L", "y": 380, "value": "LỬNG MẬT", "label": "anh em kết nghĩa", "target": [0.3, 0.5]}
                ],
                "impacts": []
            },
            {
                "at": "Nếu Lửng Mật là Chí",
                "image": "assets/long/L08.png",
                "stickers": [
                    {"at": "Taiga", "side": "R", "y": 400, "value": "TAIGA", "label": "địa bàn bảo kê", "target": [0.5, 0.5]}
                ],
                "impacts": []
            },
            {
                "at": "Lý do đơn giản: chú",
                "image": "assets/long/L09.png",
                "stickers": [],
                "impacts": ["sợ hãi"]
            },
            {
                "at": "Dù đối thủ có là",
                "image": "assets/long/L10.png",
                "stickers": [
                    {"at": "300kg", "side": "R", "y": 360, "value": "300 kg", "label": "Gấu Xám Grizzly", "target": [0.25, 0.45]}
                ],
                "impacts": ["cướp trắng miếng thịt"]
            },
            {
                "at": "Chưa hết đâu, gã này",
                "image": "assets/long/L11.png",
                "stickers": [],
                "impacts": []
            },
            {
                "at": "Mỗi khi thợ săn dựng",
                "image": "assets/long/L12.png",
                "stickers": [],
                "impacts": ["cắn nát bẫy"]
            },
            {
                "at": "Đỉnh điểm của sự trêu",
                "image": "assets/long/L13.png",
                "stickers": [
                    {"at": "mùi hôi", "side": "R", "y": 420, "value": "SKUNK", "label": "xạ hôi nồng nặc", "target": [0.65, 0.5]}
                ],
                "impacts": []
            }
        ]
    },
    "scene02": {
        "chapter_no": 2,
        "title": "BẢNG CHỈ SỐ RPG — LỖI GAME CỦA TẠO HÓA XỨ LẠNH",
        "hook": "Khi thiên nhiên quên cài thanh tụt máu",
        "card": true,
        "beats": [
            {
                "at": 0,
                "image": "assets/long/L14.png",
                "stickers": [
                    {"at": "ATK", "side": "L", "y": 380, "value": "ATK 90", "label": "sức tấn công", "target": [0.35, 0.45]},
                    {"at": "DEF", "side": "R", "y": 420, "value": "DEF 95", "label": "sức phòng thủ", "target": [0.65, 0.45]}
                ],
                "impacts": []
            },
            {
                "at": "Đừng để thân hình dài",
                "image": "assets/long/L15.png",
                "stickers": [
                    {"at": "65cm", "side": "L", "y": 380, "value": "65 cm", "label": "chiều dài cơ thể", "target": [0.45, 0.55]}
                ],
                "impacts": ["bẻ gãy xương"]
            },
            {
                "at": "Chỉ số phòng thủ DEF",
                "image": "assets/long/L16.png",
                "stickers": [
                    {"at": "-40°C", "side": "R", "y": 420, "value": "-40°C", "label": "không đóng băng", "target": [0.5, 0.5]}
                ],
                "impacts": []
            },
            {
                "at": "Và đáng sợ nhất là",
                "image": "assets/long/L17.png",
                "stickers": [
                    {"at": "ngàn điểm", "side": "R", "y": 420, "value": "STA 1000", "label": "thể lực không đáy", "target": [0.65, 0.45]}
                ],
                "impacts": []
            },
            {
                "at": "Nó có thể chạy liên",
                "image": "assets/long/L18.png",
                "stickers": [
                    {"at": "70km", "side": "L", "y": 380, "value": "70 km", "label": "chạy bền bỉ", "target": [0.5, 0.5]}
                ],
                "impacts": []
            },
            {
                "at": "Để bạn dễ hình dung",
                "image": "assets/long/L19.png",
                "stickers": [
                    {"at": "ủng trượt tuyết", "side": "R", "y": 440, "value": "SNOWSHOE", "label": "đệm chân rộng", "target": [0.55, 0.5]}
                ],
                "impacts": []
            },
            {
                "at": "Trong khi những con mồi",
                "image": "assets/long/L20.png",
                "stickers": [],
                "impacts": []
            },
            {
                "at": "Thế là một cuộc rượt",
                "image": "assets/long/L21.png",
                "stickers": [],
                "impacts": []
            },
            {
                "at": "Chưa hết đâu, cơ bắp",
                "image": "assets/long/L22.png",
                "stickers": [
                    {"at": "gấp đôi", "side": "L", "y": 380, "value": "200%", "label": "trọng lượng cơ thể", "target": [0.5, 0.5]}
                ],
                "impacts": []
            },
            {
                "at": "Cứ như thể một cậu",
                "image": "assets/long/L23.png",
                "stickers": [],
                "impacts": []
            },
            {
                "at": "Thật là một thiết kế",
                "image": "assets/long/L24.png",
                "stickers": [],
                "impacts": []
            }
        ]
    },
    "scene03": {
        "chapter_no": 3,
        "title": "CHIẾC RĂNG HÀM XOAY 90 ĐỘ & TUYẾN XẠ SKUNK BEAR",
        "hook": "Cỗ máy nghiền xương đá và vũ khí sinh học",
        "card": true,
        "beats": [
            {
                "at": 0,
                "image": "assets/long/L25.png",
                "stickers": [],
                "impacts": []
            },
            {
                "at": "Các nhà giải phẫu học",
                "image": "assets/long/L26.png",
                "stickers": [
                    {"at": "90°", "side": "R", "y": 380, "value": "90°", "label": "răng hàm xoay ngang", "target": [0.5, 0.45]}
                ],
                "impacts": []
            },
            {
                "at": "Chiếc răng này hoạt động",
                "image": "assets/long/L27.png",
                "stickers": [
                    {"at": "-50°C", "side": "L", "y": 400, "value": "-50°C", "label": "xương đá đông cứng", "target": [0.5, 0.5]}
                ],
                "impacts": ["bẻ vụn từng mẩu xương"]
            },
            {
                "at": "Vào mùa đông khắc nghiệt",
                "image": "assets/long/L28.png",
                "stickers": [],
                "impacts": []
            },
            {
                "at": "Đối với nó, xương đông",
                "image": "assets/long/L29.png",
                "stickers": [],
                "impacts": []
            },
            {
                "at": "Bên cạnh chiếc răng kìm",
                "image": "assets/long/L30.png",
                "stickers": [
                    {"at": "Skunk Bear", "side": "R", "y": 380, "value": "SKUNK BEAR", "label": "chồn gấu hôi", "target": [0.5, 0.5]}
                ],
                "impacts": []
            },
            {
                "at": "Ngay dưới đuôi của nó",
                "image": "assets/long/L31.png",
                "stickers": [],
                "impacts": []
            },
            {
                "at": "Mùi hôi này là sự",
                "image": "assets/long/L32.png",
                "stickers": [],
                "impacts": []
            },
            {
                "at": "Khi cướp được thức ăn",
                "image": "assets/long/L33.png",
                "stickers": [],
                "impacts": []
            },
            {
                "at": "Kết quả là chẳng có",
                "image": "assets/long/L34.png",
                "stickers": [],
                "impacts": []
            },
            {
                "at": "Ngoài ra, khứu giác của",
                "image": "assets/long/L35.png",
                "stickers": [
                    {"at": "6m", "side": "L", "y": 400, "value": "6 m", "label": "sâu dưới tuyết", "target": [0.5, 0.65]}
                ],
                "impacts": []
            },
            {
                "at": "Sau đó, nó dùng bốn",
                "image": "assets/long/L36.png",
                "stickers": [],
                "impacts": []
            },
            {
                "at": "Đặc biệt, bộ lông của",
                "image": "assets/long/L37.png",
                "stickers": [],
                "impacts": []
            },
            {
                "at": "Người thợ săn bản địa",
                "image": "assets/long/L38.png",
                "stickers": [
                    {"at": "-40°C", "side": "R", "y": 400, "value": "-40°C", "label": "viền mũ Eskimo", "target": [0.5, 0.5]}
                ],
                "impacts": []
            },
            {
                "at": "nhưng với lông Chồn Gu-lô",
                "image": "assets/long/L38b.png",
                "stickers": [
                    {"at": "rơi sạch như bụi", "side": "L", "y": 420, "value": "SẠCH TUYẾT", "label": "sợi lông kỵ nước", "target": [0.5, 0.5]}
                ],
                "impacts": []
            }
        ]
    },
    "scene04": {
        "chapter_no": 4,
        "title": "GÓT CHÂN A-SIN — QUÁI VẬT DẠ DÀY & ĐỘC HÀNH XỨ TUYẾT",
        "hook": "Cái bụng không đáy và gã độc thân khó tính nhất hành tinh",
        "card": true,
        "beats": [
            {
                "at": 0,
                "image": "assets/long/L39.png",
                "stickers": [
                    {"at": "Gulo Gulo", "side": "L", "y": 380, "value": "GULO GULO", "label": "kẻ phàm ăn", "target": [0.5, 0.5]}
                ],
                "impacts": []
            },
            {
                "at": "Tốc độ trao đổi chất",
                "image": "assets/long/L40.png",
                "stickers": [
                    {"at": "-40°C", "side": "R", "y": 420, "value": "-40°C", "label": "đốt cháy năng lượng", "target": [0.5, 0.5]}
                ],
                "impacts": []
            },
            {
                "at": "Để không bị chết đói",
                "image": "assets/long/L41.png",
                "stickers": [],
                "impacts": []
            },
            {
                "at": "Nhưng chính cái nết ăn",
                "image": "assets/long/L42.png",
                "stickers": [
                    {"at": "24/7", "side": "R", "y": 420, "value": "24/7", "label": "cáu kỉnh vì đói", "target": [0.5, 0.5]}
                ],
                "impacts": []
            },
            {
                "at": "Và điểm yếu bi hài",
                "image": "assets/long/L43.png",
                "stickers": [
                    {"at": "1.500km²", "side": "L", "y": 380, "value": "1.500 km²", "label": "lãnh thổ độc hành", "target": [0.5, 0.5]}
                ],
                "impacts": []
            },
            {
                "at": "Ngay cả với đồng loại",
                "image": "assets/long/L44.png",
                "stickers": [],
                "impacts": []
            },
            {
                "at": "Chúng chỉ gặp nhau đúng",
                "image": "assets/long/L45.png",
                "stickers": [],
                "impacts": []
            },
            {
                "at": "Một chiến binh vô địch",
                "image": "assets/long/L46.png",
                "stickers": [],
                "impacts": []
            },
            {
                "at": "Nhưng bạn có biết điều",
                "image": "assets/long/L47.png",
                "stickers": [],
                "impacts": []
            },
            {
                "at": "Chồn bố thỉnh thoảng vẫn",
                "image": "assets/long/L48.png",
                "stickers": [],
                "impacts": []
            },
            {
                "at": "Đúng là giang hồ xứ",
                "image": "assets/long/L49.png",
                "stickers": [],
                "impacts": []
            }
        ]
    },
    "scene05": {
        "chapter_no": 5,
        "title": "NHỮNG TRẬN CHIẾN CÓ THẬT — MỘT MÌNH ĐUỔI CẢ GẤU LẪN SÓI",
        "hook": "Kẻ điên rồ biến chúa tể phương Bắc thành trò hề",
        "card": true,
        "beats": [
            {
                "at": 0,
                "image": "assets/long/L50a.png",
                "stickers": [],
                "impacts": []
            },
            {
                "at": "Tại Vườn quốc gia Yellowstone",
                "image": "assets/long/L50.png",
                "stickers": [
                    {"at": "Yellowstone", "side": "R", "y": 400, "value": "YELLOWSTONE", "label": "địa danh ghi nhận", "target": [0.5, 0.5]}
                ],
                "impacts": []
            },
            {
                "at": "Chú chồn nhỏ không hề",
                "image": "assets/long/L51.png",
                "stickers": [],
                "impacts": ["đớp thẳng vào mõm gấu"]
            },
            {
                "at": "Bị tấn công bất ngờ",
                "image": "assets/long/L52.png",
                "stickers": [
                    {"at": "20 lần", "side": "L", "y": 380, "value": "x20", "label": "gấu xám nặng gấp 20 lần", "target": [0.25, 0.45]}
                ],
                "impacts": []
            },
            {
                "at": "Chưa dừng lại ở đó",
                "image": "assets/long/L53.png",
                "stickers": [
                    {"at": "Alaska", "side": "R", "y": 400, "value": "ALASKA", "label": "lãnh nguyên băng giá", "target": [0.5, 0.5]},
                    {"at": "3 con sói", "side": "L", "y": 380, "value": "1 vs 3", "label": "đánh bật đàn sói", "target": [0.35, 0.5]}
                ],
                "impacts": []
            },
            {
                "at": "Sói xám nổi tiếng với",
                "image": "assets/long/L54.png",
                "stickers": [],
                "impacts": []
            },
            {
                "at": "bầy sói đành ngậm ngùi",
                "image": "assets/long/L54b.png",
                "stickers": [
                    {"at": "rút lui", "side": "L", "y": 380, "value": "RÚT LUI", "label": "bầy sói chùn bước", "target": [0.5, 0.5]}
                ],
                "impacts": []
            },
            {
                "at": "Một nghiên cứu nổi tiếng",
                "image": "assets/long/L55.png",
                "stickers": [
                    {"at": "M3", "side": "L", "y": 380, "value": "M3", "label": "mã số theo dõi", "target": [0.5, 0.5]}
                ],
                "impacts": []
            },
            {
                "at": "Trong vòng 90 phút",
                "image": "assets/long/L56.png",
                "stickers": [
                    {"at": "90 phút", "side": "R", "y": 420, "value": "90 PHÚT", "label": "thời gian leo đỉnh", "target": [0.5, 0.5]},
                    {"at": "3.100m", "side": "L", "y": 380, "value": "3.100 m", "label": "đỉnh Mount Cleveland", "target": [0.5, 0.35]}
                ],
                "impacts": []
            },
            {
                "at": "Các vận động viên leo",
                "image": "assets/long/L57.png",
                "stickers": [],
                "impacts": []
            }
        ]
    },
    "scene06": {
        "chapter_no": 6,
        "title": "BÀI HỌC SINH TỒN TỪ CHỒN GULO & TEASER TẬP SAU",
        "hook": "Ý chí thép của chiến binh xứ tuyết",
        "card": true,
        "beats": [
            {
                "at": 0,
                "image": "assets/long/L58.png",
                "stickers": [],
                "impacts": []
            },
            {
                "at": "Sinh ra với thân hình",
                "image": "assets/long/L59.png",
                "stickers": [],
                "impacts": []
            },
            {
                "at": "Nó biến cái lạnh chết",
                "image": "assets/long/L60.png",
                "stickers": [],
                "impacts": []
            },
            {
                "at": "Trong cuộc sống cũng vậy",
                "image": "assets/long/L61.png",
                "stickers": [],
                "impacts": []
            },
            {
                "at": "Nếu được chọn giữa sức",
                "image": "assets/long/L62.png",
                "stickers": [
                    {"at": "Tập", "side": "R", "y": 400, "value": "BÌNH LUẬN", "label": "Wolverine hay Tôm Tít?", "target": [0.5, 0.5]}
                ],
                "impacts": []
            },
            {
                "at": "Đừng quên bấm Đăng ký",
                "image": "assets/long/L63.png",
                "stickers": [
                    {"at": "Cánh Cụt", "side": "L", "y": 380, "value": "TẬP 9", "label": "Chim Cánh Cụt Nam Cực", "target": [0.5, 0.5]}
                ],
                "impacts": []
            },
            {
                "at": "Hẹn gặp lại các bạn",
                "image": "assets/long/L64.png",
                "stickers": [
                    {"at": "tiếp theo", "side": "R", "y": 420, "value": "ĐĂNG KÝ", "label": "Vẽ Chuyện Hoang Dã", "target": [0.5, 0.5]}
                ],
                "impacts": []
            }
        ]
    }
}

# Shorts plan: 14 beats (S01 - S10b), all hold <= 5.0s
shorts_data = {
    "title_lines": [
        "CHỒN GULO 15KG ĐUỔI",
        "GẤU XÁM 300KG CƯỚP MỒI?!"
    ],
    "beats": [
        {
            "at": 0,
            "draw_s": 1.0,
            "image": "assets/shorts/S01.png",
            "stickers": [
                {"at": "15kg", "side": "L", "y": 500, "value": "15 kg", "label": "trọng lượng", "target": [0.5, 0.5]}
            ]
        },
        {
            "at": "cướp mồi của một con",
            "draw_s": 1.0,
            "image": "assets/shorts/S02.png",
            "stickers": [
                {"at": "300kg", "side": "R", "y": 520, "value": "300 kg", "label": "Gấu Xám Grizzly", "target": [0.5, 0.5]}
            ]
        },
        {
            "at": "Kẻ điên rồ bậc nhất",
            "draw_s": 1.0,
            "image": "assets/shorts/S03.png",
            "stickers": [
                {"at": "Wolverine", "side": "L", "y": 480, "value": "WOLVERINE", "label": "Chồn Gulo", "target": [0.5, 0.5]}
            ]
        },
        {
            "at": "Với bốn bàn chân bè",
            "draw_s": 1.0,
            "image": "assets/shorts/S04.png",
            "stickers": [
                {"at": "ủng trượt tuyết", "side": "R", "y": 540, "value": "SNOWSHOE", "label": "ủng tuyết tự nhiên", "target": [0.5, 0.5]}
            ]
        },
        {
            "at": "hon này lướt nhẹ trên",
            "draw_s": 1.0,
            "image": "assets/shorts/S04b.png",
            "stickers": [],
            "impacts": []
        },
        {
            "at": "Bộ lông kỵ nước",
            "draw_s": 1.0,
            "image": "assets/shorts/S05.png",
            "stickers": [
                {"at": "-40°C", "side": "L", "y": 500, "value": "-40°C", "label": "không đóng băng", "target": [0.5, 0.5]}
            ]
        },
        {
            "at": "xoay ngang 90°",
            "draw_s": 1.0,
            "image": "assets/shorts/S06.png",
            "stickers": [
                {"at": "90°", "side": "R", "y": 520, "value": "90°", "label": "răng kìm sắt", "target": [0.5, 0.5]}
            ]
        },
        {
            "at": "Nó có thể chạy liên",
            "draw_s": 1.0,
            "image": "assets/shorts/S07.png",
            "stickers": [
                {"at": "70km", "side": "L", "y": 480, "value": "70 km", "label": "vượt vách núi", "target": [0.5, 0.5]}
            ]
        },
        {
            "at": "khi bị bao vây, nó",
            "draw_s": 1.0,
            "image": "assets/shorts/S08.png",
            "stickers": [
                {"at": "mùi hôi thối", "side": "R", "y": 540, "value": "SKUNK", "label": "xạ hôi xua đuổi", "target": [0.5, 0.5]}
            ]
        },
        {
            "at": "sói cũng phải ôm mũi",
            "draw_s": 1.0,
            "image": "assets/shorts/S08b.png",
            "stickers": [],
            "impacts": []
        },
        {
            "at": "bất bại này lại cô",
            "draw_s": 1.0,
            "image": "assets/shorts/S09.png",
            "stickers": [
                {"at": "cô độc", "side": "L", "y": 500, "value": "CÔ ĐỘC", "label": "không một bóng bạn", "target": [0.5, 0.5]}
            ]
        },
        {
            "at": "Bạn muốn biết chú ta",
            "draw_s": 1.0,
            "image": "assets/shorts/S09b.png",
            "stickers": [],
            "impacts": []
        },
        {
            "at": "Bấm xem ngay video dài",
            "draw_s": 1.0,
            "image": "assets/shorts/S10.png",
            "stickers": [
                {"at": "Tập tám", "side": "R", "y": 520, "value": "XEM TẬP 8", "label": "full bản dài 16:9", "target": [0.5, 0.5]}
            ]
        },
        {
            "at_s": 47.8,
            "draw_s": 1.0,
            "image": "assets/shorts/S10b.png",
            "stickers": [
                {"at_s": 48.5, "side": "L", "y": 500, "value": "15KG vs 300KG", "label": "vòng lặp vô tận", "target": [0.5, 0.5]}
            ]
        }
    ]
}

# Write plans
(P / "specs" / "longform_plan.json").write_text(json.dumps({"targets": {}, "scenes": scenes_data}, ensure_ascii=False, indent=2), encoding="utf-8")
(P / "specs" / "shorts_plan.json").write_text(json.dumps(shorts_data, ensure_ascii=False, indent=2), encoding="utf-8")
print("Saved updated longform_plan.json and shorts_plan.json!")

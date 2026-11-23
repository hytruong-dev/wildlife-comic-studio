import json
from pathlib import Path

P = Path("projects/tap-07-tom-tit")
swords = json.load(open(P / "audio" / "shorts_words.json", encoding="utf-8"))
norm = lambda s: "".join(c.lower() for c in s if c.isalnum() or c in "°/-_")

def find_word_time(phrase, after=0.0):
    toks = [norm(x) for x in phrase.split() if norm(x)]
    nw = [norm(w['word']) for w in swords]
    for i in range(len(swords) - len(toks) + 1):
        if swords[i]['start'] >= after and nw[i:i+len(toks)] == toks:
            return swords[i]['start']
    # fallback: check if any token matches
    for i in range(len(swords)):
        if swords[i]['start'] >= after and any(t == nw[i] for t in toks):
            return swords[i]['start']
    raise SystemExit(f"NOT FOUND in shorts: {phrase!r}")

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
                {
                    "at_s": 0.5,
                    "side": "L",
                    "y": 800,
                    "value": "1 VIÊN ĐẠN",
                    "label": "súng trường dưới nước",
                    "target": [0.65, 0.50]
                }
            ]
        },
        {
            "at": "sinh ra nhiệt độ",
            "image": "assets/shorts/S05.png",
            "draw_s": 1.1,
            "stickers": [
                {
                    "at": "4.700°C",
                    "side": "R",
                    "y": 700,
                    "value": "4.700°C",
                    "label": "nóng ngang Mặt Trời",
                    "target": [0.55, 0.45]
                }
            ]
        },
        {
            "at": "Kẻ sở hữu siêu",
            "image": "assets/shorts/S02.png",
            "draw_s": 1.1,
            "stickers": [
                {
                    "at": "Mike Tyson",
                    "side": "L",
                    "y": 750,
                    "value": "TYSON",
                    "label": "võ sĩ đại dương",
                    "target": [0.50, 0.45]
                }
            ]
        },
        {
            "at": "Với đôi càng búa",
            "image": "assets/shorts/S03.png",
            "draw_s": 1.1,
            "stickers": [
                {
                    "at": "10.400g,",
                    "side": "R",
                    "y": 720,
                    "value": "10.400 g",
                    "label": "gia tốc thần sầu",
                    "target": [0.60, 0.45]
                }
            ]
        },
        {
            "at": "và thậm chí từng",
            "image": "assets/shorts/S04.png",
            "draw_s": 1.1,
            "stickers": [
                {
                    "at": "mặt kính bể cá",
                    "side": "L",
                    "y": 780,
                    "value": "NỨT KÍNH",
                    "label": "thủy cung nước Anh",
                    "target": [0.50, 0.50]
                }
            ]
        },
        {
            "at": "Cú vung càng nhanh",
            "image": "assets/shorts/S11.png",
            "draw_s": 1.1,
            "stickers": [
                {
                    "at": "sôi nước biển",
                    "side": "R",
                    "y": 740,
                    "value": "SÔI NƯỚC",
                    "label": "nướng chín con mồi",
                    "target": [0.55, 0.45]
                }
            ]
        },
        {
            "at": "Thế nhưng cứ mỗi",
            "image": "assets/shorts/S06.png",
            "draw_s": 1.1,
            "stickers": [
                {
                    "at": "thạch bơ mềm nhũn",
                    "side": "L",
                    "y": 750,
                    "value": "MỀM NHƯ THẠCH",
                    "label": "mùa lột xác",
                    "target": [0.50, 0.55]
                }
            ]
        },
        {
            "at": "phải trốn chui trốn",
            "image": "assets/shorts/S07.png",
            "draw_s": 1.1,
            "stickers": [
                {
                    "at": "một con ốc sên",
                    "side": "R",
                    "y": 780,
                    "value": "SỢ ỐC SÊN",
                    "label": "trốn trong hang sâu",
                    "target": [0.65, 0.55]
                }
            ]
        },
        {
            "at": "Bí mật về đôi",
            "image": "assets/shorts/S08.png",
            "draw_s": 1.0,
            "stickers": [
                {
                    "at": "mười sáu dải màu",
                    "side": "L",
                    "y": 720,
                    "value": "16 MÀU",
                    "label": "thị giác siêu cấp",
                    "target": [0.55, 0.35]
                }
            ]
        },
        {
            "at": "giúp phát hiện ung",
            "image": "assets/shorts/S09.png",
            "draw_s": 1.0,
            "stickers": [
                {
                    "at": "phát hiện ung thư",
                    "side": "R",
                    "y": 750,
                    "value": "Y HỌC",
                    "label": "tầm soát ung thư",
                    "target": [0.55, 0.50]
                }
            ]
        },
        {
            "at": "đã có ở video",
            "image": "assets/shorts/S10.png",
            "draw_s": 1.1,
            "stickers": [
                {
                    "at": "Bấm xem ngay",
                    "side": "R",
                    "y": 750,
                    "value": "XEM NGAY",
                    "label": "Tập 7 bản đầy đủ",
                    "target": [0.50, 0.50]
                }
            ]
        }
    ]
}

# Test all anchors
for b in shorts_plan['beats']:
    if 'at' in b:
        t = find_word_time(b['at'])
        print(f"Beat '{b['at']}': {t:.2f}s")
    for s in b.get('stickers', []):
        if 'at' in s:
            t = find_word_time(s['at'])
            print(f"  Sticker '{s['at']}': {t:.2f}s (target: {s['target']})")

with open(P / "specs" / "shorts_plan.json", "w", encoding="utf-8") as f:
    json.dump(shorts_plan, f, ensure_ascii=False, indent=2)

print("Saved perfected shorts_plan.json successfully!")

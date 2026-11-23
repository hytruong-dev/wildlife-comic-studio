import json

sw = json.load(open('projects/tap-07-tom-tit/audio/shorts_words.json', encoding='utf-8'))
vd = sw[-1]['end']

# Verify exact match finder
norm = lambda s: "".join(c.lower() for c in s if c.isalnum() or c in "°/-_")

def finder(words, ks=("word", "start")):
    n = [norm(w[ks[0]]) for w in words]
    def T(phrase, after=0.0):
        toks = [norm(x) for x in phrase.split() if norm(x)]
        for i in range(len(words) - len(toks) + 1):
            if words[i][ks[1]] >= after and n[i:i + len(toks)] == toks:
                return words[i][ks[1]]
        raise SystemExit(f"phrase not found: {phrase!r}")
    return T

T = finder(sw)

beats = [
    {
        "at_s": 0.0,
        "image": "assets/shorts/S01.png",
        "draw_s": 1.1,
        "stickers": [
            {"at_s": 0.5, "side": "L", "y": 800, "value": "1 VIÊN ĐẠN", "label": "tốc độ súng trường"}
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

print(f"Total shorts duration: {vd:.2f}s")
for i, b in enumerate(beats):
    st = float(b["at_s"]) if "at_s" in b else round(T(b["at"]) - 0.25, 2)
    nxt = round(T(beats[i+1]["at"]) - 0.25, 2) if i + 1 < len(beats) else vd
    hold = nxt - st
    print(f"Beat {i+1:02d} ({b['image']}): st={st:.2f}s, hold={hold:.2f}s")
    for s in b.get("stickers", []):
        st_t = float(s["at_s"]) if "at_s" in s else round(T(s["at"], st - 0.5), 2)
        print(f"   Sticker {s['value']}: at={st_t:.2f}s")

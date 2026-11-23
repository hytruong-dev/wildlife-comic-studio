import json

words = json.load(open('projects/tap-07-tom-tit/audio/long_words_fixed.json', encoding='utf-8'))
norm = lambda s: "".join(c.lower() for c in s if c.isalnum() or c in "°/-_")

def finder(ws):
    nw = [norm(w['w']) for w in ws]
    def T(phrase, after=0.0):
        toks = [norm(x) for x in phrase.split() if norm(x)]
        for i in range(len(ws) - len(toks) + 1):
            if ws[i]['s'] >= after and nw[i:i+len(toks)] == toks:
                return ws[i]['s']
        raise SystemExit(f"NOT FOUND: {phrase!r} (after {after})")
    return T

plan_test = {
    "scene01": [
        (0, "assets/long/L01.png"),
        ("Hãy làm quen với Tôm Tít", "assets/long/L01.png"),
        ("Nhìn từ xa", "assets/long/L01.png"),
        ("Thế nhưng ẩn dưới", "assets/long/L02.png"),
        ("Cua biển mai dày", "assets/long/L02.png"),
        ("Thậm chí ngay cả mặt", "assets/long/L12.png"),
        ("Các thợ lặn biển từ lâu", "assets/long/L03.png"),
        ("Lý do vô cùng đơn giản", "assets/long/L03.png"),
        ("Một gã tí hon dưới đáy", "assets/long/L01.png")
    ],
    "scene02": [
        (0, "assets/long/L04.png"),
        ("Hãy cùng bóc tách bảng", "assets/long/L04.png"),
        ("Tốc độ vung đòn", "assets/long/L03.png"),
        ("Bạn chớp mắt mất một", "assets/long/L03.png"),
        ("Trong một cái chớp mắt", "assets/long/L02.png"),
        ("Chỉ số phòng thủ", "assets/long/L05.png"),
        ("Và chỉ số thị giác", "assets/long/L10.png"),
        ("Để bạn dễ hình dung", "assets/long/L03.png"),
        ("Vậy mà đôi càng tí hon này", "assets/long/L03.png"),
        ("Nếu cánh tay của bạn", "assets/long/L02.png")
    ],
    "scene03": [
        (0, "assets/long/L06.png"),
        ("Do chiếc càng vung đi", "assets/long/L07.png"),
        ("Ngay khoảnh khắc tiếp theo", "assets/long/L06.png"),
        ("Vụ nổ này thậm chí", "assets/long/L06.png"),
        ("Nghĩa là mỗi cú ra đòn", "assets/long/L06.png"),
        ("Dù nó có đấm trượt", "assets/long/L02.png"),
        ("Vậy câu hỏi đặt ra", "assets/long/L05.png"),
        ("Bên trong chiếc càng búa", "assets/long/L05.png"),
        ("Khi một vết nứt nhỏ", "assets/long/L05.png"),
        ("Quân đội Mỹ và các", "assets/long/L14.png")
    ],
    "scene04": [
        (0, "assets/long/L08.png"),
        ("Võ sĩ Mike Tyson đại dương", "assets/long/L08.png"),
        ("Giống như loài tôm cua", "assets/long/L08.png"),
        ("Ngay sau khi lột xác", "assets/long/L08.png"),
        ("Kẻ từng đấm nứt kính", "assets/long/L09.png"),
        ("Trong suốt vài tuần chờ", "assets/long/L09.png"),
        ("Điều hài hước nhất là", "assets/long/L09.png"),
        ("Nếu chẳng may có kẻ thù", "assets/long/L09.png"),
        ("Nhưng thực chất đó hoàn toàn", "assets/long/L09.png"),
        ("Nếu kẻ thù liều lĩnh", "assets/long/L08.png"),
        ("Ngoài ra gã này còn", "assets/long/L12.png")
    ],
    "scene05": [
        (0, "assets/long/L12.png"),
        ("Vào tháng tư năm 1998", "assets/long/L12.png"),
        ("Có vẻ như bực mình vì", "assets/long/L12.png"),
        ("Kết quả là mặt kính", "assets/long/L13.png"),
        ("Từ đó các viện hải dương", "assets/long/L14.png"),
        ("Bên cạnh cú đấm thần sầu", "assets/long/L10.png"),
        ("Nó không chỉ nhìn thấy", "assets/long/L10.png"),
        ("Mỗi con mắt của nó", "assets/long/L10.png"),
        ("Các nhà khoa học hiện đang", "assets/long/L11.png")
    ],
    "scene06": [
        (0, "assets/long/L15.png"),
        ("Sở hữu sức mạnh vô song", "assets/long/L15.png"),
        ("Đỉnh cao thực sự của", "assets/long/L16.png"),
        ("Bạn ấn tượng nhất với", "assets/long/L17.png"),
        ("Ở tập tiếp theo chúng ta", "assets/long/L18.png"),
        ("Bạn có đoán được đó", "assets/long/L18.png"),
        ("Đừng quên bấm Đăng ký", "assets/long/L17.png")
    ]
}

all_ok = True
for sid, beats in plan_test.items():
    ws = words[sid]
    T = finder(ws)
    D = ws[-1]['e']
    print(f"\n--- {sid} (D={D:.2f}s) ---")
    st_list = []
    for at, img in beats:
        st = 0.0 if at == 0 else max(0.0, round(T(at) - 0.30, 2))
        st_list.append(st)
    for i in range(len(beats)):
        nxt = st_list[i+1] if i + 1 < len(beats) else D
        hold = nxt - st_list[i]
        at, img = beats[i]
        warn = ""
        if hold > 15.0:
            warn = f"!! ERROR: hold {hold:.1f}s > 15s"
            all_ok = False
        elif hold < 2.0:
            warn = f"!! ERROR: hold {hold:.1f}s < 2s"
            all_ok = False
        print(f"  b{i+1:02d}: at={at!r:30s} -> st={st_list[i]:5.2f}s, hold={hold:5.2f}s  {warn}")

if all_ok:
    print("\n>>> ALL BEATS PASS THE DURATION CONSTRAINTS (NO ERROR)! <<<")

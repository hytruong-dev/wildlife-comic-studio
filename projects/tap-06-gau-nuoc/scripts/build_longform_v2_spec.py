"""Build specs/longform_v2_spec.json — one illustration per spoken idea, timed from word timestamps.

Every beat / sticker / impact is anchored to a PHRASE of the narration (looked up in
audio/long_words_fixed.json), so pictures and callouts land exactly when the voice says it.
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
P = Path(__file__).resolve().parents[1]
WORDS = json.loads((P / "audio" / "long_words_fixed.json").read_text(encoding="utf-8"))
DUR = {f"scene0{i}": json.loads((P / "audio" / f"scene0{i}_parts_duration.json").read_text())["total_duration"]
       for i in range(1, 7)}

def norm(w):
    w = unicodedata.normalize("NFD", w.lower())
    w = "".join(c for c in w if unicodedata.category(c) != "Mn").replace("đ", "d")
    return re.sub(r"[^a-z0-9]", "", w)

def T(sc, phrase, after=0.0):
    ws = WORDS[sc]
    toks = [norm(x) for x in phrase.split() if norm(x)]
    n = [norm(w["w"]) for w in ws]
    for i in range(len(ws) - len(toks) + 1):
        if ws[i]["s"] >= after and n[i:i + len(toks)] == toks:
            return ws[i]["s"]
    raise SystemExit(f"phrase not found in {sc}: {phrase!r}")

L = lambda k: f"assets/gemini_downloaded_long/L{k:02d}.png"
O = lambda n: f"assets/gemini_downloaded/{n}.png"

# (start phrase | 0, image, entrance, stickers[(phrase, side, y, value, label, target|None)], impacts[phrase])
PLAN = {
    "scene01": dict(chapter_no=1, title="KẺ SỐNG SÓT CUỐI CÙNG CỦA TRÁI ĐẤT", card=False, beats=[
        (0, O("scene01_01_meteor_extinction_survivor"), "draw", [], ["đâm sầm"]),
        ("Không phải gián", L(1), "pop", [("chưa đầy một", "R", 380, "< 1 mm", "nhỏ hơn hạt cát", None)], []),
        ("Nhìn qua kính hiển vi", O("scene01_02_microscopic_cute_water_bear"), "slide", [], []),
        ("Các nhà khoa học phương", L(9), "draw_fast", [], []),
        ("Nhưng ẩn sau", L(3), "pop", [("năm cuộc đại", "R", 420, "5 LẦN", "đại tuyệt chủng", None)], []),
        ("Nó trơ trơ", O("scene01_03_extreme_endurance_triad"), "draw",
         [("âm 272", "L", 330, "-272°C", "lạnh vũ trụ", "ICE"),
          ("nước sôi 150", "R", 330, "150°C", "nước sôi", "HOT"),
          ("gấp sáu lần", "R", 610, "x6", "áp suất Mariana", None)], []),
        ("Thậm chí vào năm 2007", L(17), "slide", [("mười ngày", "L", 420, "10 NGÀY", "trần trụi ngoài vũ trụ", None)], []),
        ("Khi đem về tưới", O("scene03_04_revival_single_water_drop"), "draw_fast", [], []),
        ("Nhưng bi hài thay", L(7), "pop", [], ["ốc sên bò"]),
        ("Trong sứ mệnh Foton", O("scene01_04_space_vacuum_foton_mission"), "draw",
         [("gấp một ngàn lần", "R", 420, "x1.000", "tia UV Mặt Trời", None)], []),
        ("Không gian chân không", L(2), "slide", [], []),
    ]),
    "scene02": dict(chapter_no=2, title="BẢNG CHỈ SỐ RPG — LỖI GAME TIẾN HÓA", hook="Được tạo hóa buff chỉ số đến mức vô lý", beats=[
        (0, L(21), "draw", [], []),
        ("Sức mạnh tấn công", O("scene02_01_rpg_card_atk_spd_low"), "slide",
         [("5 trên 100", "L", 330, "ATK 5", "yếu xìu", None), ("2 trên 100", "L", 600, "SPD 2", "chậm như rùa", None)], []),
        ("Nhưng hãy nhìn sang cột", O("scene02_02_rpg_card_def_max_temperature"), "pop",
         [("9999 trên 100", "R", 420, "DEF 9999", "phòng thủ vô lý", None)], ["9999 trên 100"]),
        ("Khả năng chịu lạnh", O("scene01_03_extreme_endurance_triad"), "slide",
         [("âm 272 độ C, điểm", "L", 330, "-272°C", "chịu lạnh", "ICE"),
          ("150 độ C, nướng", "R", 330, "150°C", "chịu nhiệt", "HOT")], []),
        ("Khả năng kháng phóng xạ", O("scene02_03_radiation_lethal_dose_comparison"), "draw_fast",
         [("5000 đến 6000", "R", 330, "6.000 Gray", "gấu nước chịu được", None),
          ("liều phóng xạ 5 Gray", "L", 330, "5 Gray", "đủ giết người", None)], []),
        ("Vậy mà Gấu Nước có thể thản", L(8), "pop", [("gấp một ngàn lần", "R", 420, "x1.000", "liều chết người", None)], []),
        ("Và tuyệt chiêu tối thượng", O("scene02_04_rpg_cryptobiosis_tun_state"), "slide",
         [("100 trên 100", "R", 420, "100/100", "Cryptobiosis", None)], ["100 trên 100"]),
        ("Khi đối mặt hiểm họa", O("scene03_01_water_desiccation_process"), "draw_fast",
         [("99 phần trăm", "L", 330, "99%", "nước bị rút ra", None), ("30 năm trời", "R", 600, "30 NĂM", "ngủ đông", None)], []),
        ("Để dễ hình dung", L(4), "draw",
         [("mười một ngàn mét", "L", 330, "11.000 m", "đáy Mariana", None),
          ("một ngàn atmosphere", "R", 330, "1.000 atm", "ép bẹp xe tải", None)], []),
        ("Thế nhưng gấu nước vẫn", L(27), "pop", [("sáu ngàn atmosphere", "R", 420, "6.000 atm", "vẫn sống!", None)], ["sáu ngàn atmosphere"]),
        ("Các nhà vật lý học", L(5), "slide", [("ba ngàn cây số", "L", 420, "3.000 km/h", "bắn ra từ súng", None)], ["chạm đích"]),
    ]),
    "scene03": dict(chapter_no=3, title="TUYỆT KỸ THỦY TINH HÓA", hook="Ngừng sống — nhưng không hề chết", beats=[
        (0, L(10), "draw", [], []),
        ("Nhưng Gấu Nước thì bảo", O("scene02_04_rpg_cryptobiosis_tun_state"), "pop", [("Trạng thái Tun", "R", 420, "TUN", "kén ngủ đông", None)], []),
        ("Bí mật giúp nó", O("scene03_02_tdp_amorphous_glass_matrix"), "slide", [("TDP, tức", "L", 420, "TDP", "protein vô định hình", None)], []),
        ("Thay vì để tế bào", L(28), "draw_fast", [], []),
        ("Ở trạng thái này", L(25), "pop", [("0,01 phần trăm", "R", 420, "0,01%", "trao đổi chất", None)], []),
        ("Bức xạ hạt nhân chiếu", O("scene03_03_dsup_protein_radiation_shield"), "slide", [("Dsup", "L", 420, "Dsup", "khiên chắn ADN", None)], []),
        ("Cứ thế, cái hạt", L(29), "draw_fast", [("ba thập kỷ", "R", 420, "30 NĂM", "ngủ trong băng", None)], []),
        ("Chỉ cần bạn nhỏ", L(11), "draw", [("ba mươi phút", "L", 420, "30 PHÚT", "là sống lại", None)], []),
        ("Điều kỳ diệu nhất", L(35), "pop", [], []),
        ("Cơ chế này giống hệt", L(6), "slide", [("hàng trăm năm", "R", 420, "100+ NĂM", "tươi nguyên vẹn", None)], []),
        ("Nhờ phát hiện chấn động", L(12), "draw_fast", [], []),
    ]),
    "scene04": dict(chapter_no=4, title="GÓT CHÂN A-SIN CỦA KẺ BẤT TỬ", hook="Tạo hóa có khiếu hài hước rất cay nghiệt", beats=[
        (0, O("scene04_01_superhero_vs_glass_fragile"), "draw", [], []),
        ("Tất cả những siêu năng lực", L(18), "slide", [], []),
        ("Điểm yếu bi hài số một", L(38), "pop", [("Điểm yếu bi hài", "R", 380, "#1", "chất nhầy ốc sên", None)], ["Điểm yếu bi hài"]),
        ("Một nghiên cứu khoa học", O("scene04_02_snail_slime_lethal_trap"), "draw", [], ["ngạt thở chết"]),
        ("Điểm yếu số hai", O("scene04_03_nematode_worm_predator_snack"), "slide",
         [("Điểm yếu số hai", "L", 380, "#2", "không có giáp", None)], []),
        ("Kháng được bom", L(22), "pop", [], ["cú cắn"]),
        ("Và trớ trêu nhất", O("scene04_04_global_warming_water_temp"), "draw_fast",
         [("trớ trêu nhất", "L", 330, "#3", "nóng lên toàn cầu", None),
          ("37,6 độ C", "R", 330, "37,6°C", "nước hơi ấm", None),
          ], []),
        ("gấu nước đang hoạt động sẽ chết", O("scene04_01_superhero_vs_glass_fragile"), "draw_fast",
         [("50 phần trăm", "R", 420, "50%", "chết", None)], []),
        ("Bất tử ngoài vũ trụ", L(34), "pop", [], []),
        ("Chính vì toàn bộ", L(30), "slide", [], []),
        ("Nó không có lớp vỏ", L(13), "draw_fast", [], []),
        ("Trong thế giới của một giọt", L(31), "pop", [], []),
        ("Một con bọ đuôi bật", L(20), "slide", [], ["xé toạc"]),
    ]),
    "scene05": dict(chapter_no=5, title="GẤU NƯỚC ĐANG NẰM TRÊN MẶT TRĂNG", hook="Vụ tai nạn vũ trụ có thật năm 2019", beats=[
        (0, L(26), "draw", [("năm 2019!", "R", 420, "2019", "sự cố có thật", None)], []),
        ("Vào tháng 4", O("scene05_01_beresheet_moon_lander_launch"), "slide", [], []),
        ("Bên trong tàu mang", L(32), "draw_fast", [], []),
        ("Nhưng một trục trặc", O("scene05_02_moon_crash_explosion_debris"), "pop",
         [("500 cây số", "L", 420, "500 km/h", "lao xuống", None)], ["phát nổ"]),
        ("Vỏ tàu vỡ nát", O("scene05_03_tardigrades_scattered_moon_craters"), "draw_fast", [], []),
        ("Vì Mặt Trăng không", L(23), "slide",
         [("âm 170", "L", 330, "-170°C", "đêm", "COLD"), ("dương 120", "R", 330, "+120°C", "ngày", "HOTMOON")], []),
        ("Giới khoa học tin", O("scene05_04_astronaut_water_revival_dream"), "draw", [], []),
        ("Vụ tai nạn của tàu", L(14), "pop", [], []),
        ("Mặc dù gấu nước trên", L(36), "slide", [], []),
        ("Nếu một ngày nào đó", L(37), "draw_fast", [], []),
        ("Các nhà sinh học vũ trụ", L(39), "pop", [("hàng trăm năm", "R", 420, "100+ NĂM", "ngủ đông", None)], []),
        ("Dù không có bầu", L(19), "draw", [], []),
    ]),
    "scene06": dict(chapter_no=6, title="BÀI HỌC SINH TỒN TỪ GẤU NƯỚC", hook="Kẻ kiên cường mới là kẻ sống sót", beats=[
        (0, O("scene06_01_philosophical_adaptation_triumph"), "draw", [], []),
        ("Bạn không cần phải", L(15), "slide", [], []),
        ("Bạn ấn tượng nhất", L(16), "pop", [], []),
        ("Và ở tập tiếp theo", O("scene06_02_mantis_shrimp_boxing_teaser"), "slide", [], ["nổ tung"]),
        ("Tự nhiên không tạo", L(24), "draw_fast", [], []),
        ("Gấu Nước nhắc nhở chúng ta", O("scene06_01_philosophical_adaptation_triumph"), "draw", [], []),
        ("Nếu bạn thấy video", L(33), "pop", [], []),
    ]),
}

# verified feature anchors (fraction of the original image)
TARGETS = {
    "ICE": (0.19, 0.45),      # scene01_03: frozen ice block, left
    "HOT": (0.58, 0.62),      # scene01_03: boiling pot / thermometer
    "COLD": (0.25, 0.60),     # L23: icy night half
    "HOTMOON": (0.68, 0.70),  # L23: burning day half
}

def main():
    scenes = []
    for sid, pl in PLAN.items():
        beats = []
        for k, (ph, img, ent, stk, imps) in enumerate(pl["beats"]):
            st = 0.0 if ph == 0 else max(0.0, round(T(sid, ph) - 0.30, 2))
            b = {"id": f"{sid}_b{k + 1:02d}", "start_s": st, "image": img, "entrance": ent, "stickers": [], "impacts": []}
            for sp, side, y, val, lab, tg in stk:
                s = {"t": round(T(sid, sp, st - 0.5), 2), "side": side, "y": y, "value": val, "label": lab}
                if tg:
                    s["target"] = list(TARGETS[tg])
                b["stickers"].append(s)
            b["impacts"] = [round(T(sid, x, st - 0.5), 2) for x in imps]
            beats.append(b)
        # TASTE-58: every picture is hand-drawn (no slide/pop). Short holds use the faster draw.
        for i, b in enumerate(beats):
            nxt = beats[i + 1]["start_s"] if i + 1 < len(beats) else DUR[sid]
            b["entrance"] = "draw" if nxt - b["start_s"] >= 5.0 else "draw_fast"
        for i in range(len(beats) - 1):
            assert beats[i + 1]["start_s"] > beats[i]["start_s"], (sid, i)
            hold = beats[i + 1]["start_s"] - beats[i]["start_s"]
            print(f"  {beats[i]['id']} {beats[i]['start_s']:6.2f}  hold {hold:5.2f}  {Path(beats[i]['image']).stem}")
        print(f"  {beats[-1]['id']} {beats[-1]['start_s']:6.2f}  hold {DUR[sid] - beats[-1]['start_s']:5.2f}  {Path(beats[-1]['image']).stem}")
        scenes.append({"id": sid, "voice": f"audio/{sid}.wav", "duration_s": DUR[sid], "chapter_no": pl["chapter_no"],
                       "title": pl["title"], "card_hook": pl.get("hook", ""), "chapter_card": pl.get("card", True),
                       "card_s": 1.8, "beats": beats})
    spec = {
        "episode": "tap-06-gau-nuoc", "version": "longform v2 — 66 voice-matched beats, fixed captions, accurate chapter titles",
        "words": "audio/long_words_fixed.json", "n_chapters": 6,
        "bgm": "assets/bgm/calm-acoustic.wav",
        "intro": "assets/branding/intro_ve_chuyen_hoang_da.mp4", "outro": "assets/branding/outro_ve_chuyen_hoang_da.mp4",
        "cold_open_s": round(T("scene01", "Không phải gián") - 0.25, 2), "intro_sting_s": 4.0, "intro_mode": "full_first",
        "output": "renders/tap06_gau_nuoc_long_v2.mp4", "scenes": scenes,
    }
    out = P / "specs" / "longform_v2_spec.json"
    out.write_text(json.dumps(spec, ensure_ascii=False, indent=1), encoding="utf-8")
    print("beats:", sum(len(s["beats"]) for s in scenes), "->", out)

if __name__ == "__main__":
    main()

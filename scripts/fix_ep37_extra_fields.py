import json
from pathlib import Path

p = Path("projects/tap-37-lac-da-sa-mac/episode.json")
ep = json.loads(p.read_text(encoding="utf-8"))

ep["episode_no"] = 37

b_titles = [
    ("CA CẤP CỨU", "BÀI TOÁN SỐC NHIỆT 50°C"),
    ("BỆNH ÁN SỐ 1", "BƯỚU MỠ NĂNG LƯỢNG KỲ DIỆU"),
    ("BỆNH ÁN SỐ 2", "HỒNG CẦU OVAL CO GIÃN 240%"),
    ("BỆNH ÁN SỐ 3", "QUẢ THẬN SIÊU LỌC NƯỚC TIỂU"),
    ("BỆNH ÁN SỐ 4", "ỐNG THỞ NGƯNG TỤ VÀ VAN MŨI"),
    ("XUẤT VIỆN", "ĐỈNH CAO Y HỌC PHỎNG SINH HỌC")
]

for i, sc in enumerate(ep["longform"]["scenes"]):
    sc["badge"] = b_titles[i][0]
    sc["banner_title"] = b_titles[i][1]

p.write_text(json.dumps(ep, ensure_ascii=False, indent=2), encoding="utf-8")
print("Updated episode_no, badges, and banner_titles!")


"""Tập 7 v3: append beats for the 3 new narration parts (L60-L66) to longform_plan.json."""
import json
from pathlib import Path

p = Path("projects/tap-07-tom-tit/specs/longform_plan.json")
plan = json.loads(p.read_text(encoding="utf-8"))
B = lambda at, img, st=(), imp=(): {"at": at, "image": f"assets/long/{img}.png", "stickers": list(st), "impacts": list(imp)}
S = lambda at, side, y, value, label, target: {"at": at, "side": side, "y": y, "value": value, "label": label, "target": target}
NEW = {
    "scene02": [B("Mà khoan đã, đó", "L60", [S("phe đâm", "L", 380, "PHE ĐÂM", "càng gai như xiên nướng", [0.62, 0.5])]),
                B("Một phe đấm bốc,", "L61")],
    "scene03": [B("Mà cái hay nhất", "L62", [S("cặp búa mới tinh", "L", 380, "BÚA MỚI", "thay sau mỗi lần lột xác", [0.5, 0.45])]),
                B("Nhưng cái giá của", "L63")],
    "scene05": [B("Chưa hết đâu!", "L64", [S("ánh sáng phân cực", "L", 380, "PHÂN CỰC", "tin nhắn bí mật", [0.33, 0.45])]),
                B("Và gã giang hồ", "L65", [S("20 năm", "R", 400, "20 NĂM", "chung một hang", [0.5, 0.55])]),
                B("Ra ngoài thì đấm", "L66")],
}
for sid, beats in NEW.items():
    sc = plan["scenes"][sid]
    have = {b["image"] for b in sc["beats"]}
    sc["beats"] += [b for b in beats if b["image"] not in have]
p.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
print("beats:", sum(len(s["beats"]) for s in plan["scenes"].values()))

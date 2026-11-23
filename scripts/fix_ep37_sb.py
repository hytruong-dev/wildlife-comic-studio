import json
from pathlib import Path

sb_path = Path("projects/tap-37-lac-da-sa-mac/specs/storyboard.json")
sb = json.loads(sb_path.read_text(encoding="utf-8"))

# Fix 1: scene01 b04 anchor
for b in sb["long"]:
    if b["scene"] == "scene01" and b["at"] == "hai tuần ròng rã":
        b["at"] = "2 tuần ròng rã"
        b["stickers"][0]["at"] = "2 tuần"
    elif b["scene"] == "scene02" and b["at"] == "sinh tồn suốt cả tháng trời":
        b["stickers"][0]["at"] = "cả tháng trời"
    elif b["scene"] == "scene05" and b["at"] == "bão cát có tràn vào phổi":
        b["at"] = "Bụi cát có tràn vào phổi"

# Fix 4: shorts
for b in sb["shorts"]:
    if b["at"] == "năm mươi độ C":
        b["at"] = "50°C"

sb_path.write_text(json.dumps(sb, ensure_ascii=False, indent=2), encoding="utf-8")
print("Fixed all ep37 anchors and stickers!")


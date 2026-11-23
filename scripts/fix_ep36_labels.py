import json, re
from pathlib import Path

sb_path = Path("projects/tap-36-chim-go-kien/specs/storyboard.json")
sb = json.loads(sb_path.read_text(encoding="utf-8"))

# Fix stickers in long beats
for b in sb["long"]:
    for s in b.get("stickers", []):
        if s.get("label") == "gia tốc va chạm cực đại":
            s["label"] = "gia tốc va chạm"
        elif s.get("label") == "giới hạn người ngất xỉu":
            s["label"] = "giới hạn người ngất"
        elif s.get("label") == "chiều dài lưỡi so với mỏ":
            s["label"] = "dài gấp 3 lần mỏ"
        elif s.get("label") == "lực còn sót lại vào não":
            s["label"] = "lực sót lại vào não"
        elif s.get("label") == "tốc độ máy quay siêu tốc":
            s["label"] = "máy quay siêu tốc"
        elif s.get("label") == "tần suất chớp mắt đồng bộ":
            s["label"] = "chớp mắt đồng bộ"

# Fix shorts beat 1 sticker at
sb["shorts"][0]["stickers"][0]["at"] = "20 lần"

sb_path.write_text(json.dumps(sb, ensure_ascii=False, indent=2), encoding="utf-8")
print("Updated storyboard labels and shorts sticker!")


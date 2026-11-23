import json
from pathlib import Path

P = Path("projects/tap-35-ca-voi-sat-thu")
sb_file = P / "specs/storyboard.json"
sb = json.loads(sb_file.read_text(encoding="utf-8"))

sc5 = [b for b in sb["long"] if b.get("scene") == "scene05"]

# Move stickers from b01 to b02
sc5[1]["stickers"] = sc5[0]["stickers"]
sc5[0]["stickers"] = []

# Fix b10 and b11 anchors
sc5[9]["at"] = "cực kỳ ít ỏi các loài sinh vật"
sc5[10]["at"] = "Sau khi hết khả năng sinh sản"

sb_file.write_text(json.dumps(sb, ensure_ascii=False, indent=2), encoding="utf-8")
print("Updated scene05 stickers and anchors successfully!")


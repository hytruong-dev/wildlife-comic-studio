import json
from pathlib import Path

P = Path("projects/tap-35-ca-voi-sat-thu")
sb_file = P / "specs/storyboard.json"
sb = json.loads(sb_file.read_text(encoding="utf-8"))

# 1. Scene 03: change b06 anchor to 'tung cú húc lật ngửa'
sc3 = [b for b in sb["long"] if b.get("scene") == "scene03"]
sc3[5]["at"] = "tung cú húc lật ngửa"

# 2. Scene 04: change b02 anchor to 'Giống như các gia tộc'
sc4 = [b for b in sb["long"] if b.get("scene") == "scene04"]
sc4[1]["at"] = "Giống như các gia tộc"

sb_file.write_text(json.dumps(sb, ensure_ascii=False, indent=2), encoding="utf-8")
print("Updated scene03 and scene04 anchors successfully!")


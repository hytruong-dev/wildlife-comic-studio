import json
from pathlib import Path

P = Path("projects/tap-44-ca-mat-trang")
sb = json.loads((P / "specs" / "storyboard.json").read_text(encoding="utf-8"))
phrases_data = json.loads((P / "scripts" / "phrases.json").read_text(encoding="utf-8"))
scene_phrases = phrases_data["scenes"]
shorts_phrases = phrases_data["shorts"]

# Map phrases to longform beats
by_scene = {}
for b in sb["long"]:
    by_scene.setdefault(b["scene"], []).append(b)

for sid, beats in by_scene.items():
    phrases = scene_phrases[sid]
    assert len(beats) == len(phrases), f"Mismatch in {sid}: {len(beats)} beats vs {len(phrases)} phrases"
    for b, p in zip(beats, phrases):
        b["at"] = p

# Map phrases to shorts beats
assert len(sb["shorts"]) == len(shorts_phrases)
for b, p in zip(sb["shorts"], shorts_phrases):
    b["at"] = p

(P / "specs" / "storyboard.json").write_text(json.dumps(sb, ensure_ascii=False, indent=2), encoding="utf-8")
print("Applied phrases to storyboard.json successfully!")


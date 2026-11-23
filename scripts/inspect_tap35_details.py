import json
from pathlib import Path

P = Path("projects/tap-35-ca-voi-sat-thu")
long_words = json.loads((P / "audio/long_words_fixed.json").read_text(encoding="utf-8"))
shorts_words = json.loads((P / "audio/shorts_words.json").read_text(encoding="utf-8"))
storyboard = json.loads((P / "specs/storyboard.json").read_text(encoding="utf-8"))
ep = json.loads((P / "episode.json").read_text(encoding="utf-8"))

def print_scene_words(sid, start_s=0, end_s=999):
    print(f"\n--- Words in {sid} from {start_s}s to {end_s}s ---")
    ws = long_words[sid]
    for w in ws:
        if w and start_s <= w["s"] <= end_s:
            print(f"{w['s']:5.2f}s - {w['e']:5.2f}s: {w['w']}")

print("=== SCENE 01 ===")
print_scene_words("scene01", 45, 66)
print_scene_words("scene01", 90, 118)

print("=== SCENE 02 ===")
print_scene_words("scene02", 58, 96)

print("=== SCENE 03 ===")
print_scene_words("scene03", 24, 43)
print_scene_words("scene03", 94, 101)

print("=== SCENE 04 ===")
print_scene_words("scene04", 0, 18)

print("=== SCENE 05 ===")
print_scene_words("scene05", 0, 30)
print_scene_words("scene05", 70, 85)

print("=== SHORTS ===")
print("Shorts words from 25s to 38s:")
for w in shorts_words:
    if 25 <= w["start"] <= 38:
        print(f"{w['start']:5.2f}s - {w['end']:5.2f}s: {w['word']}")


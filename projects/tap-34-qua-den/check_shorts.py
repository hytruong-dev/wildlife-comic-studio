import json
with open("projects/tap-34-qua-den/audio/shorts_words.json", "r", encoding="utf-8") as f:
    sw = json.load(f)
for w in sw:
    if 25 <= w["start"] <= 42:
        print(f"{w['start']:.1f}s:{w['word']}", end=" ")
print()


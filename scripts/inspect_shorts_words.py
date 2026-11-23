import json

sw = json.load(open("projects/tap-18-bo-phao-thu/audio/shorts_words.json", encoding="utf-8"))
for i, w in enumerate(sw):
    print(f"{i:03d} {w['word']}: {w['start']:.2f}s - {w['end']:.2f}s")

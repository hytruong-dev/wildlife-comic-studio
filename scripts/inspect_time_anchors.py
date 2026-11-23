import json

words = json.load(open('projects/tap-07-tom-tit/audio/long_words_fixed.json', encoding='utf-8'))
for sc_id in ["scene01", "scene02", "scene03", "scene04", "scene05", "scene06"]:
    ws = words[sc_id]
    print(f"\n==================== {sc_id} (total {len(ws)} words, {ws[-1]['e']:.1f}s) ====================")
    # print words every ~5-10 seconds
    for i, w in enumerate(ws):
        if i % 10 == 0:
            print(f"  {w['s']:5.2f}s: {w['w']}")

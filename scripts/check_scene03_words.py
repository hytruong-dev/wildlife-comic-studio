import json

words = json.load(open('projects/tap-07-tom-tit/audio/long_words_fixed.json', encoding='utf-8'))
for w in words['scene03']:
    if 50.0 <= w['s'] <= 65.0:
        print(f"{w['s']:.2f}s: {w['w']}")

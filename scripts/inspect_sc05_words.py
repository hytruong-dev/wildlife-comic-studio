import json

words = json.load(open('projects/tap-07-tom-tit/audio/long_words_fixed.json', encoding='utf-8'))
for w in words['scene05']:
    if 62.0 <= w['s'] <= 72.0:
        print(f"  {w['s']:.2f}s - {w['e']:.2f}s: {w['w']}")

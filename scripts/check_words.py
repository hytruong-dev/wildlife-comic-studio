import json

words = json.load(open('projects/tap-07-tom-tit/audio/long_words_fixed.json', encoding='utf-8'))
print("=== SCENE 05 (58s - 70s) ===")
for w in words['scene05']:
    if 58.0 <= w['s'] <= 70.0:
        print(f"{w['s']:.2f}s: {w['w']}")

print("\n=== SCENE 06 (38s - 50s) ===")
for w in words['scene06']:
    if 38.0 <= w['s'] <= 50.0:
        print(f"{w['s']:.2f}s: {w['w']}")

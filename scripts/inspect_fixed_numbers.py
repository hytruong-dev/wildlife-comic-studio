import json

words = json.load(open('projects/tap-07-tom-tit/audio/long_words_fixed.json', encoding='utf-8'))
print("=== Scene 01 sample ===")
for w in words['scene01'][:15]:
    print(f"  {w['w']:15s} [{w['s']:.2f}s - {w['e']:.2f}s]")

print("\n=== Scene 02 sample (Numbers) ===")
num_words = [w for w in words['scene02'] if any(c.isdigit() or c in "ATKSPDDEF" for c in w['w'])]
for w in num_words:
    print(f"  {w['w']:15s} [{w['s']:.2f}s - {w['e']:.2f}s]")

print("\n=== Shorts sample (Numbers) ===")
swords = json.load(open('projects/tap-07-tom-tit/audio/shorts_words.json', encoding='utf-8'))
s_nums = [w for w in swords if any(c.isdigit() or c in "°C" for c in w['word'])]
for w in s_nums:
    print(f"  {w['word']:15s} [{w['start']:.2f}s - {w['end']:.2f}s]")

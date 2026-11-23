import json

swords = json.load(open('projects/tap-07-tom-tit/audio/shorts_words.json', encoding='utf-8'))
print(f"Total shorts words: {len(swords)}")
for i, w in enumerate(swords):
    if i % 10 == 0:
        print(f"  {w['start']:5.2f}s: {w['word']}")

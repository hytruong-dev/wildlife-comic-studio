import json

swords = json.load(open('projects/tap-07-tom-tit/audio/shorts_words.json', encoding='utf-8'))
for w in swords:
    if 40.0 <= w['start'] <= 46.0:
        print(f"  {w['start']:5.2f}s - {w['end']:5.2f}s: {w['word']}")

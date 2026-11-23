import json

swords = json.load(open('projects/tap-07-tom-tit/audio/shorts_words.json', encoding='utf-8'))
for w in swords:
    if any(c.isdigit() or c in "°C" for c in w['word']) or w['word'] in ['Cavitation', 'Bouligand', 'Tyson']:
        print(f"  {w['start']:5.2f}s - {w['end']:5.2f}s: {w['word']}")

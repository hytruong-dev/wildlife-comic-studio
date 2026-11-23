import json

swords = json.load(open("projects/tap-15-capybara/audio/shorts_words.json", encoding="utf-8"))
print(" ".join(f"{w['word']}({w['start']:.1f})" for w in swords if w['start'] >= 35.0))

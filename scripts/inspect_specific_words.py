import json

P = "projects/tap-15-capybara"
words = json.load(open(f"{P}/audio/long_words_fixed.json", encoding="utf-8"))
swords = json.load(open(f"{P}/audio/shorts_words.json", encoding="utf-8"))

def show_words(ws, start, end):
    return " ".join(f"{w['w']}({w['s']:.1f})" for w in ws if start <= w['s'] <= end)

print("scene01 (15-35s):")
print(show_words(words["scene01"], 15.0, 35.0))

print("\nscene05 (0-20s):")
print(show_words(words["scene05"], 0.0, 20.0))

print("\nscene06 (35-55s):")
print(show_words(words["scene06"], 35.0, 55.0))

print("\nshorts (last 15s):")
print(show_words(swords, 40.0, 55.0))

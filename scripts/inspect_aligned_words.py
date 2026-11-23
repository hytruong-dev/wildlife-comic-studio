import json

data = json.load(open('projects/tap-07-tom-tit/audio/long_words_fixed.json', encoding='utf-8'))
for sc_id, words in data.items():
    print(f"=== {sc_id} ({len(words)} words) ===")
    sample = [w['w'] for w in words[:15]]
    print("  First 15:", " ".join(sample))
    sample_mid = [w['w'] for w in words[len(words)//2:len(words)//2 + 15]]
    print("  Mid 15:", " ".join(sample_mid))

import json

raw = json.load(open('projects/tap-07-tom-tit/audio/long_words_raw.json', encoding='utf-8'))
for sid, ws in raw.items():
    print(f"\n{sid} (total {len(ws)} whisper words):")
    # print first 10 and last 10
    sample = [w['w'] for w in ws[:25]]
    print("  First 25:", " ".join(sample))

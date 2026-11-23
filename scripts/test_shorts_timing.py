import json

sw = json.load(open('projects/tap-07-tom-tit/audio/shorts_words.json', encoding='utf-8'))

phrases = [
    "Một cú đấm",
    "nhiệt độ bốn ngàn",
    "Kẻ sở hữu siêu",
    "Với đôi càng búa",
    "và thậm chí từng",
    "Cú vung càng nhanh",
    "Thế nhưng cứ mỗi",
    "phải trốn chui trốn",
    "Bí mật về đôi",
    "giúp phát hiện ung",
    "đã có ở video"
]

def find_start(phrase):
    toks = phrase.lower().split()
    words_n = [w['word'].lower().strip('.,!?:;[]') for w in sw]
    for i in range(len(words_n) - len(toks) + 1):
        if words_n[i:i+len(toks)] == toks:
            return sw[i]['start']
    return None

vd = sw[-1]['end']
times = [0.0]
for p in phrases[1:]:
    t = find_start(p)
    print(f"{p!r:25s} -> {t}s")
    times.append(t)

print("Durations between beats:")
for i in range(len(times)):
    nxt = times[i+1] if i + 1 < len(times) else vd
    print(f"  Beat {i+1} (S{i+1:02d}): start={times[i]:.2f}s, hold={nxt - times[i]:.2f}s")

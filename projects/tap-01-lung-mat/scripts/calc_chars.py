from generate_full_duration_audio_125x import FULL_SCENES

total = 0
for sc in FULL_SCENES:
    txt = " ".join(sc["paragraphs"])
    print(f"{sc['id']}: {len(txt)} chars")
    total += len(txt)

print(f"Total all: {total} chars")

import json
import re
from pathlib import Path

p = Path("projects/tap-08-chon-gulo/episode.json")
ep = json.loads(p.read_text(encoding="utf-8"))

print(f"Episode: {ep['animal']} ({ep['slug']})")
total_long_sentences = 0
for sc in ep["longform"]["scenes"]:
    print(f"\n=== {sc['id']}: {sc['chapter_title']} ===")
    sc_text = " ".join(sc["parts"])
    # Clean emotion tags for sentence counting
    clean_text = re.sub(r"\[.*?\]", "", sc_text).strip()
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", clean_text) if s.strip()]
    print(f"Parts: {len(sc['parts'])}, Sentences/Ideas: {len(sentences)}")
    for i, s in enumerate(sentences):
        print(f"  [{i+1:02d}] {s[:100]}...")
    total_long_sentences += len(sentences)

print(f"\nTotal longform sentences/beats: {total_long_sentences}")

# Shorts
shorts_text = ep["shorts"]["text"]
clean_shorts = re.sub(r"\[.*?\]", "", shorts_text).strip()
shorts_sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", clean_shorts) if s.strip()]
print(f"\nShorts sentences/beats: {len(shorts_sentences)}")
for i, s in enumerate(shorts_sentences):
    print(f"  [S{i+1:02d}] {s[:100]}...")

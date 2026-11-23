import json

ep = json.load(open('projects/tap-07-tom-tit/episode.json', encoding='utf-8'))
scenes = ep['longform']['scenes']

for sc in scenes:
    print(f"\n==================== {sc['id']}: {sc['chapter_title']} ====================")
    for p_idx, part in enumerate(sc['parts']):
        # Split part into sentences
        # Simple split by punctuation
        import re
        sents = re.split(r'(?<=[.!?])\s+', part)
        for s_idx, sent in enumerate(sents):
            if sent.strip():
                print(f"[{p_idx+1}.{s_idx+1}] {sent.strip()}")

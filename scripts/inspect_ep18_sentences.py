import json, re

ep = json.load(open("projects/tap-18-bo-phao-thu/episode.json", encoding="utf-8"))
display = ep.get("display_fix", {})

def to_subtitle(t):
    clean = re.sub(r"\[[^\]]+\]", "", t)
    for k in sorted(display, key=len, reverse=True):
        clean = clean.replace(k, display[k])
    return clean

for sc in ep["longform"]["scenes"]:
    print(f"\n=================== {sc['id']} ({sc['badge']}) ===================")
    full_text = ""
    for p in sc["parts"]:
        t = p["text"] if isinstance(p, dict) else p
        full_text += " " + to_subtitle(t)
    
    # split into sentences
    sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+", full_text.strip()) if s.strip()]
    for idx, s in enumerate(sents):
        first_words = " ".join(s.split()[:4])
        print(f"  Beat {idx+1:02d} | at: '{first_words}' | {s[:85]}...")

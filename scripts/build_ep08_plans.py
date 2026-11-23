import json
import re
from pathlib import Path

P = Path("projects/tap-08-chon-gulo")
A = P / "audio"
ep = json.loads((P / "episode.json").read_text(encoding="utf-8"))
words = json.loads((A / "long_words_fixed.json").read_text(encoding="utf-8"))
shorts_words = json.loads((A / "shorts_words.json").read_text(encoding="utf-8"))

def norm(s):
    return re.sub(r"[^0-9a-zA-Z\u00C0-\u1EF9]+", "", str(s)).lower()

def make_finder(word_list, ks=("w", "s")):
    n = [norm(w[ks[0]]) for w in word_list]
    def T(phrase: str, after: float = 0.0) -> float:
        toks = [norm(x) for x in phrase.split() if norm(x)]
        if not toks:
            return after
        for i in range(len(word_list) - len(toks) + 1):
            if word_list[i][ks[1]] >= after and n[i:i + len(toks)] == toks:
                return word_list[i][ks[1]]
        # Fallback: try searching single first word after
        for i in range(len(word_list)):
            if word_list[i][ks[1]] >= after and n[i] == toks[0]:
                return word_list[i][ks[1]]
        raise ValueError(f"Phrase '{phrase}' not found after {after:.1f}s")
    return T

print("Building Tap 08 plans...")

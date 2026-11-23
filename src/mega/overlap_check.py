"""Dò TRÙNG LẶP giữa lời mega (content/*.md) và lời 10 tập lẻ (sources/*.words.json hoặc projects/*/script).

  python src/mega/overlap_check.py projects/<mega> --sources projects/mega-01-bang-phong-than/sources [--n 5]

In các cụm n-từ (mặc định 5) của mega xuất hiện y nguyên trong tập lẻ, kèm tên tập.
Đây là lưới lọc thô: cụm chung chung ("các nhà khoa học đã phát hiện") có thể trùng mà không sao;
cái cần soi là cụm mang SỰ KIỆN (con số, địa danh, tên nghiên cứu).
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
W = re.compile(r"[0-9A-Za-zÀ-ỹ]+")


def norm_words(text: str) -> list[str]:
    return [w.lower() for w in W.findall(text)]


def load_source(p: Path) -> list[str]:
    d = json.loads(p.read_text(encoding="utf-8-sig"))
    if isinstance(d, dict) and "segments" in d:  # đầu ra transcribe_sources.py
        return norm_words(" ".join(s.get("text", "") for s in d["segments"]))
    words = d.get("words", d) if isinstance(d, dict) else d
    out = []
    for w in words:
        t = (w.get("word") or w.get("w") or w.get("text") or "") if isinstance(w, dict) else str(w)
        out += norm_words(t)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project")
    ap.add_argument("--sources", required=True)
    ap.add_argument("--n", type=int, default=5)
    a = ap.parse_args()
    P = Path(a.project)
    idx = defaultdict(set)
    for f in sorted(Path(a.sources).glob("*.words.json")):
        ws = load_source(f)
        name = f.name.split(".")[0]
        for i in range(len(ws) - a.n + 1):
            idx[" ".join(ws[i:i + a.n])].add(name)
    hits = []
    for f in sorted((P / "content").glob("s*.md")):
        for ln_no, ln in enumerate(f.read_text(encoding="utf-8-sig").splitlines(), 1):
            if "::" not in ln:
                continue
            ws = norm_words(ln.split("::")[0])
            seen = set()
            for i in range(len(ws) - a.n + 1):
                g = " ".join(ws[i:i + a.n])
                if g in idx and g not in seen:
                    seen.add(g)
                    hits.append((f.name, ln_no, g, ",".join(sorted(idx[g]))))
    for h in hits:
        print(f"{h[0]}:{h[1]}  [{h[3]}]  {h[2]}")
    print(f"--- {len(hits)} cụm {a.n}-từ trùng")


if __name__ == "__main__":
    main()

import json, sys
d = json.load(open(sys.argv[1], encoding="utf-8"))
w = d["words"] if isinstance(d, dict) else d
print(" ".join(f"{x.get('word', x.get('text'))}@{x['start']:.1f}" for x in w))

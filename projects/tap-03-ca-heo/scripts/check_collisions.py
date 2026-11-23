import json
from pathlib import Path

for p in sorted(Path("projects/tap-03-ca-heo/specs").glob("scene*_spec.json")):
    data = json.loads(p.read_text(encoding="utf-8"))
    panels = data.get("panels", [])
    print(f"=== {p.name} ===")
    for i in range(len(panels)):
        for j in range(i+1, len(panels)):
            c1 = panels[i]["caption"]
            c2 = panels[j]["caption"]
            if abs(c1["y"] - c2["y"]) < 50:
                c1_x0, c1_x1 = c1["x"], c1["x"] + c1["w"]
                c2_x0, c2_x1 = c2["x"], c2["x"] + c2["w"]
                overlap = min(c1_x1, c2_x1) - max(c1_x0, c2_x0)
                if overlap > 0:
                    print(f"  COLLISION between {panels[i]['id']} and {panels[j]['id']}: overlap={overlap}px!")
                    print(f"    [{panels[i]['id']}] (x={c1_x0}..{c1_x1}): {c1['text']}")
                    print(f"    [{panels[j]['id']}] (x={c2_x0}..{c2_x1}): {c2['text']}")

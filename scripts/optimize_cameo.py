import json
from pathlib import Path

p = Path("projects/tap-37-lac-da-sa-mac/episode.json")
ep = json.loads(p.read_text(encoding="utf-8"))

# Keep 5 cameo parts: scene01_p2, scene02_p2, scene03_p2, scene04_p2, scene05_p2
# Convert scene02_p5, scene03_p5, scene04_p5, scene05_p5, scene06_p2 back to host
ep["longform"]["scenes"][1]["parts"][5]["speaker"] = "host"
ep["longform"]["scenes"][1]["parts"][5].pop("cast", None)

ep["longform"]["scenes"][2]["parts"][5]["speaker"] = "host"
ep["longform"]["scenes"][2]["parts"][5].pop("cast", None)

ep["longform"]["scenes"][3]["parts"][5]["speaker"] = "host"
ep["longform"]["scenes"][3]["parts"][5].pop("cast", None)

ep["longform"]["scenes"][4]["parts"][5]["speaker"] = "host"
ep["longform"]["scenes"][4]["parts"][5].pop("cast", None)

ep["longform"]["scenes"][5]["parts"][2]["speaker"] = "host"
ep["longform"]["scenes"][5]["parts"][2].pop("cast", None)

p.write_text(json.dumps(ep, ensure_ascii=False, indent=2), encoding="utf-8")
print("Adjusted cameo parts to optimal percentage!")


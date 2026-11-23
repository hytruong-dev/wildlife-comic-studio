"""Remap every Tập 7 long-form beat to the image that literally illustrates its narration (v3)."""
import copy, json
from pathlib import Path

PLAN = Path("projects/tap-07-tom-tit/specs/longform_plan.json")
plan = json.loads(PLAN.read_text(encoding="utf-8"))

# scene -> {beat index (0-based, original order): image}
REMAP = {
    "scene01": {0: "L01", 1: "L02", 2: "L19", 3: "L03", 4: "L32", 5: "L05", 6: "L06", 7: "L33", 8: "L20"},
    "scene02": {0: "L07", 1: "L21", 2: "L22", 3: "L23", 4: "L34", 5: "L31", 6: "L35", 7: "L36", 8: "L24"},
    "scene03": {0: "L37", 1: "L38", 2: "L25", 3: "L26", 4: "L39", 5: "L27", 6: "L40", 7: "L10", 8: "L41", 9: "L42"},
    "scene04": {0: "L43", 1: "L11", 2: "L44", 3: "L28", 4: "L29", 5: "L12", 6: "L46", 7: "L13", 8: "L45", 9: "L47", 10: "L48"},
    "scene05": {0: "L49", 1: "L50", 2: "L14", 3: "L51", 4: "L52", 5: "L15", 6: "L53", 7: "L54", 8: "L16"},
    "scene06": {0: "L55", 1: "L08", 2: "L12", 3: "L09", 4: "L18", 5: "L01"},
}

# Long beats that narrate two different pictures get split: (scene, beat idx, new "at", image, stickers moved by "at")
SPLITS = [
    ("scene04", 10, "sáng hôm sau", "L30", {"nứt một vệt dài"}),
    ("scene06", 2, "kiên nhẫn chờ đợi", "L17", set()),
    ("scene06", 3, "hay đôi mắt", "L16", {"bình luận"}),
]

for sid, m in REMAP.items():
    beats = plan["scenes"][sid]["beats"]
    assert len(beats) == len(m), (sid, len(beats))
    for i, img in m.items():
        beats[i]["image"] = f"assets/long/{img}.png"

for sid, idx, at, img, moved in sorted(SPLITS, key=lambda x: -x[1]):
    beats = plan["scenes"][sid]["beats"]
    b = beats[idx]
    nb = {"at": at, "image": f"assets/long/{img}.png",
          "stickers": [s for s in b["stickers"] if s["at"] in moved], "impacts": []}
    b["stickers"] = [s for s in b["stickers"] if s["at"] not in moved]
    if "nứt" in b.get("impacts", []) and moved:
        b["impacts"].remove("nứt"); nb["impacts"].append("nứt")
    beats.insert(idx + 1, nb)

PLAN.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
print("ok", sum(len(s["beats"]) for s in plan["scenes"].values()), "beats")

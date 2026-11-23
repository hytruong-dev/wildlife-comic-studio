"""Correct Whisper spelling for long-form captions while keeping Whisper word timing.

Whisper (vi) mis-hears many words ("vũ chủ", "ngần sau", "chơi chơi"...). The real narration
text lives in the TTS generator scripts. We align script tokens to Whisper tokens (difflib on
diacritic-free lowercase forms) and copy / interpolate the timings onto the correct words.

Output: audio/long_words_fixed.json  (same schema: {"sceneXX": [{"w","s","e"}, ...]})
"""
import ast
import difflib
import json
import re
import sys
import unicodedata
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
P = Path(__file__).resolve().parents[1]
S = P / "scripts"

def dict_literal(path: Path, name: str) -> dict:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and any(getattr(t, "id", "") == name for t in node.targets):
            return ast.literal_eval(node.value)
    raise KeyError(name)

A = dict_literal(S / "generate_audio_ep06.py", "LONGFORM_ACTS")
B = dict_literal(S / "generate_longform_expansion_ep06.py", "EXPANSION_PARTS")
C = dict_literal(S / "generate_act1_and_act5_extras.py", "EXTRA_PARTS")
SCENES = {
    "scene01": [A["act01_myth_buster_hook.mp3"], C["act01_part2.mp3"]],
    "scene02": [A["act02_rpg_stats.mp3"], B["act02_part2.mp3"]],
    "scene03": [A["act03_cryptobiosis_mechanism.mp3"], B["act03_part2.mp3"]],
    "scene04": [A["act04_snail_weakness.mp3"], B["act04_part2.mp3"]],
    "scene05": [A["act05_moon_mission_beresheet.mp3"], B["act05_part2.mp3"], C["act05_part3.mp3"]],
    "scene06": [A["act06_evolution_lesson_teaser.mp3"], B["act06_part2.mp3"]],
}
# TTS phonetic spellings -> what the viewer should read
DISPLAY = {
    "Ma-ri-a-na": "Mariana", "Bê-rê-shít": "Beresheet", "E-vơ-rét": "Everest", "T-D-Ps": "TDP",
    "A-T-K": "ATK", "S-P-D": "SPD", "D-E-F": "DEF", "D-súp": "Dsup", "regolith": "Regolith",
    "9999": "9999", "Foton": "Foton",
}

def norm(w: str) -> str:
    w = unicodedata.normalize("NFD", w.lower())
    w = "".join(c for c in w if unicodedata.category(c) != "Mn").replace("đ", "d")
    return re.sub(r"[^a-z0-9]", "", w)

def tokens(text: str) -> list[str]:
    out = []
    for t in text.split():
        core = t.strip(".,!?:;\"'()")
        for k, v in DISPLAY.items():
            if core == k:
                t = t.replace(k, v)
        out.append(t)
    return out

def align(script: list[str], wh: list[dict]) -> list[dict]:
    a = [norm(x["w"]) for x in wh]
    b = [norm(x) for x in script]
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    res: list[dict | None] = [None] * len(script)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            for k in range(j2 - j1):
                res[j1 + k] = {"w": script[j1 + k], "s": wh[i1 + k]["s"], "e": wh[i1 + k]["e"]}
        elif op in ("replace", "insert"):
            if i2 > i1:
                t0, t1 = wh[i1]["s"], wh[i2 - 1]["e"]
            else:
                t0 = wh[i1 - 1]["e"] if i1 > 0 else 0.0
                t1 = wh[i1]["s"] if i1 < len(wh) else t0 + 0.3 * (j2 - j1)
                t1 = max(t1, t0 + 0.12 * (j2 - j1))
            n = j2 - j1
            # weight by syllable length so long words get more time
            lens = [max(1, len(norm(script[j]))) for j in range(j1, j2)]
            tot, acc = sum(lens), 0
            for k, j in enumerate(range(j1, j2)):
                s = t0 + (t1 - t0) * acc / tot
                acc += lens[k]
                e = t0 + (t1 - t0) * acc / tot
                res[j] = {"w": script[j], "s": round(s, 3), "e": round(e, 3)}
    return res  # type: ignore[return-value]

def main():
    wh_all = json.loads((P / "audio" / "long_words.json").read_text(encoding="utf-8"))
    out = {}
    for sc, parts in SCENES.items():
        script = tokens(" ".join(parts))
        wh = [w for w in wh_all[sc] if norm(w["w"])]
        fixed = align(script, wh)
        ratio = difflib.SequenceMatcher(None, [norm(x["w"]) for x in wh], [norm(x) for x in script], autojunk=False).ratio()
        print(f"{sc}: whisper {len(wh)} words, script {len(script)} words, match ratio {ratio:.2f}")
        out[sc] = fixed
    (P / "audio" / "long_words_fixed.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    for sc in out:
        print(sc, " ".join(f"{w['w']}@{w['s']:.1f}" for w in out[sc][:14]))

if __name__ == "__main__":
    main()

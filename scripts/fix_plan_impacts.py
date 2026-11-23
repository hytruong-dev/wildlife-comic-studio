import json
from pathlib import Path

P = Path("projects/tap-07-tom-tit")
plan = json.load(open(P / "specs" / "longform_plan.json", encoding="utf-8"))
words = json.load(open(P / "audio" / "long_words_fixed.json", encoding="utf-8"))
norm = lambda s: "".join(c.lower() for c in s if c.isalnum() or c in "°/-_")

for sid, sc in plan['scenes'].items():
    all_words = set(norm(w['w']) for w in words[sid])
    print(f"\nChecking impacts for {sid}:")
    for b_idx, b in enumerate(sc['beats']):
        new_impacts = []
        for imp in b.get('impacts', []):
            imp_norm = norm(imp)
            if imp_norm in all_words:
                new_impacts.append(imp)
                print(f"  b{b_idx+1}: OK -> {imp}")
            else:
                print(f"  b{b_idx+1}: REMOVING NOT SPOKEN -> {imp}")
        b['impacts'] = new_impacts

with open(P / "specs" / "longform_plan.json", "w", encoding="utf-8") as f:
    json.dump(plan, f, ensure_ascii=False, indent=2)

print("Updated plan impacts!")

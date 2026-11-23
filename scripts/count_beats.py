import json

plan = json.load(open('projects/tap-07-tom-tit/specs/longform_plan.json', encoding='utf-8'))
total_beats = 0
for sid, sc in plan['scenes'].items():
    print(f"{sid}: {len(sc['beats'])} beats")
    total_beats += len(sc['beats'])
print(f"Total beats: {total_beats}")

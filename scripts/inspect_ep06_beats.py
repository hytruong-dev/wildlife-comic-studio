import json

plan = json.load(open('examples/ep06_reference/longform_plan.json', encoding='utf-8'))
for sid, sc in plan['scenes'].items():
    print(f"{sid}: {len(sc['beats'])} beats")
    for b in sc['beats']:
        print(f"   at: {b['at']!r:25s} -> {b['image']}")

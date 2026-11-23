import json

ep6 = json.load(open('examples/ep06_reference/longform_plan.json', encoding='utf-8'))
imgs = set()
for sid, sc in ep6['scenes'].items():
    for b in sc['beats']:
        imgs.add(b['image'])

print(f"Total unique images in ep06 longform: {len(imgs)}")
for im in sorted(imgs):
    print(" ", im)

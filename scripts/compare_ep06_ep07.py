import json
from pathlib import Path

ep6 = json.load(open('examples/ep06_reference/longform_plan.json', encoding='utf-8'))
ep7 = json.load(open('projects/tap-07-tom-tit/specs/longform_plan.json', encoding='utf-8'))

print("=== EP06 Longform Plan ===")
total_beats_6 = sum(len(sc['beats']) for sc in ep6['scenes'].values())
total_stickers_6 = sum(len(b.get('stickers', [])) for sc in ep6['scenes'].values() for b in sc['beats'])
total_impacts_6 = sum(len(b.get('impacts', [])) for sc in ep6['scenes'].values() for b in sc['beats'])
imgs_6 = set(b['image'] for sc in ep6['scenes'].values() for b in sc['beats'])
print(f"Scenes: {len(ep6['scenes'])}, Beats: {total_beats_6}, Stickers: {total_stickers_6}, Impacts: {total_impacts_6}, Unique Images: {len(imgs_6)}")

print("\n=== EP07 Longform Plan ===")
total_beats_7 = sum(len(sc['beats']) for sc in ep7['scenes'].values())
total_stickers_7 = sum(len(b.get('stickers', [])) for sc in ep7['scenes'].values() for b in sc['beats'])
total_impacts_7 = sum(len(b.get('impacts', [])) for sc in ep7['scenes'].values() for b in sc['beats'])
imgs_7 = set(b['image'] for sc in ep7['scenes'].values() for b in sc['beats'])
print(f"Scenes: {len(ep7['scenes'])}, Beats: {total_beats_7}, Stickers: {total_stickers_7}, Impacts: {total_impacts_7}, Unique Images: {len(imgs_7)}")

# Check shorts images used in longform ep7:
shorts_in_long = [img for img in imgs_7 if "shorts" in img]
print(f"\nShorts images used in Longform EP07: {len(shorts_in_long)}")
for s in sorted(shorts_in_long):
    print(" ", s)

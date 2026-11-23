import json

sb = json.load(open('projects/tap-42-ca-thoi-loi/specs/storyboard.json', encoding='utf-8'))
for b in sb['long']:
    if b['id'] in ['L05', 'L06', 'L07', 'L09', 'L10', 'L11', 'L12', 'L18', 'L19', 'L20', 'L56', 'L57']:
        print(f"{b['id']}: at='{b.get('at')}', scene={b.get('scene')}")

print("\n--- shorts ---")
for b in sb['shorts']:
    print(f"{b['id']}: at='{b.get('at')}'")


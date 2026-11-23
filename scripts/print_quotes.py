import json
from pathlib import Path

p = json.loads(Path('projects/tap-08-chon-gulo/specs/image_prompts.json').read_text(encoding='utf-8'))
for item in p['longform']:
    print(f"{item['id']}: {item['quote'][:70]}")

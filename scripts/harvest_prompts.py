"""Collect every Gemini image prompt actually sent in a chat transcript -> specs/image_prompts.json (last one per image wins).
usage: python scripts/harvest_prompts.py <transcript.jsonl> projects/<slug> [extra_prompts.json ...]"""
import json, re, sys
from pathlib import Path

tr, P = Path(sys.argv[1]), Path(sys.argv[2])
found: dict[str, str] = {}
for line in tr.read_text(encoding="utf-8", errors="ignore").splitlines():
    try:
        ev = json.loads(line)
    except Exception:
        continue
    for part in (ev.get("message") or {}).get("content") or []:
        if part.get("type") != "tool_use":
            continue
        blob = json.dumps(part.get("input", {}), ensure_ascii=False)
        blob = blob.encode().decode("unicode_escape", errors="ignore").encode("latin-1", errors="ignore").decode("utf-8", errors="ignore")
        for m in re.finditer(r"((?:HÌNH|Tạo hình ảnh)[^\"]{0,40}?\b([LST]\d{2})\b.{40,2500}?)(?<!\\)\"\s*[;,)]", blob, re.S):
            txt = m.group(1).replace('\\"', '"').strip()
            txt = re.split(r"['`]\s*;|\s//\s|\n\s*(?:const|let|await|el\.)\b", txt)[0].strip()
            if re.search(r"Bố cục|NỘI DUNG CẢNH", txt) and not re.search(r"Select-String|\$_|\\\(", txt):
                found[m.group(2)] = txt
for extra in sys.argv[3:]:  # {"L60": ["line", "layout"]} files written by gen.py workflow
    for k, (line, layout) in json.loads(Path(extra).read_text(encoding="utf-8")).items():
        found.setdefault(k, f'Lời thoại: "{line}". Bố cục: {layout}')
out = P / "specs/image_prompts.json"
old = json.loads(out.read_text(encoding="utf-8")) if out.exists() else {}
old.update(found)
out.write_text(json.dumps(dict(sorted(old.items())), ensure_ascii=False, indent=1), encoding="utf-8")
print(len(old), "prompts:", " ".join(sorted(old)))

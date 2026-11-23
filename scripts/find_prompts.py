import re, sys
from pathlib import Path
t = (Path.home() / ".cursor/projects/c-QuangHy-youtube-ai-edit-02/agent-transcripts/b04949ca-fe2c-4dc9-bfa3-6c511c754bac/b04949ca-fe2c-4dc9-bfa3-6c511c754bac.jsonl").read_text(encoding="utf-8", errors="ignore")
pat = sys.argv[1]
n = int(sys.argv[2]) if len(sys.argv) > 2 else 4
ms = [m.start() for m in re.finditer(pat, t)]
print(len(ms))
for i in ms[:n]:
    print(t[max(0, i - 300):i + 1500].replace("\\n", "\n"))
    print("=====")

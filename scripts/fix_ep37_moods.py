import json
from pathlib import Path

ep37_path = Path("projects/tap-37-lac-da-sa-mac/episode.json")
ep = json.loads(ep37_path.read_text(encoding="utf-8"))

for sc in ep["longform"]["scenes"]:
    for p in sc["parts"]:
        if p["mood"] not in ["hao_hung", "don_dap", "tram_bi_an", "nghiem_trang_gia", "bi_hai", "am_ap"]:
            p["mood"] = "hao_hung"

ep37_path.write_text(json.dumps(ep, ensure_ascii=False, indent=2), encoding="utf-8")
print("Updated ep37 parts moods!")


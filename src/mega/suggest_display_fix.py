"""Liệt kê các cụm số đọc bằng chữ trong content/*.md chưa có display_fix trong content/meta.json.

  python src/mega/suggest_display_fix.py projects/<mega>
In ra JSON gợi ý (giá trị để trống "?" cho mình điền) — chép vào meta.json > display_fix.
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
NW = ("không một hai ba bốn năm sáu bảy tám chín mười mươi lăm lẻ linh trăm ngàn nghìn triệu tỷ rưỡi mốt tư").split()
UNITS = r"(?:độ C|ki-lô-gam|ki-lô-mét|cây số|mét|xăng-ti-mét|mi-li-mét|phút|giây|tiếng|giờ|ngày|năm|lần|phần trăm|lít|con|kg|km|m)"


def main():
    P = Path(sys.argv[1]).resolve()
    meta = json.loads((P / "content" / "meta.json").read_text(encoding="utf-8-sig"))
    have = meta.get("display_fix", {})
    text = "\n".join(f.read_text(encoding="utf-8-sig") for f in sorted((P / "content").glob("*.md")))
    spoken = "\n".join(ln.split("::")[0] for ln in text.splitlines() if "::" in ln)
    nw = "|".join(NW)
    found = {}
    for m in re.finditer(rf"(?<![\wÀ-ỹ])((?:âm |Âm )?(?:{nw})(?:[ -](?:{nw}))*(?: {UNITS})?)(?![\wÀ-ỹ])", spoken, flags=re.I):
        s = m.group(1).strip()
        if not any(s in k or k in s for k in have) and len(s.split()) >= 2:
            found[s] = "?"
    print(json.dumps(found, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()

"""Tự gắn "Video có liên quan" (Shorts -> video dài) cho mọi tập mà video dài ĐÃ công khai và Shorts chưa gắn.

YouTube chỉ cho chọn video dài đã công khai, nên script này chạy hằng ngày sau giờ đăng (Task Scheduler
"VeChuyenHoangDa_AutoLinkShorts", 17:20 và 20:20). Chủ kênh đồng ý chạy tự động ngày 23/11/2026.

  python src/episode/auto_link_shorts.py            # gắn các tập đến hạn
  python src/episode/auto_link_shorts.py --list     # chỉ liệt kê, không mở trình duyệt
  python src/episode/auto_link_shorts.py --test tap-20-ca-cung-thu   # kiểm tra đường chạy trên tập đã gắn (không đổi gì)

Chỉ sửa trường "Video có liên quan" của Shorts. Không đụng tiêu đề, mô tả, tag, lịch đăng.
Nhật ký: logs/auto_link_shorts.log
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LOG = ROOT / "logs" / "auto_link_shorts.log"
GRACE = timedelta(minutes=10)  # đợi YouTube chuyển hẳn sang công khai


def log(msg: str) -> None:
    LOG.parent.mkdir(exist_ok=True)
    line = f"{datetime.now():%Y-%m-%d %H:%M:%S} {msg}"
    print(line)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def due_projects() -> list[Path]:
    out = []
    now = datetime.now()
    for f in sorted((ROOT / "projects").glob("*/upload_result.json")):
        try:
            r = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        if r.get("shorts_related") or not r.get("long_id") or not r.get("shorts_id") or not r.get("date"):
            continue
        try:
            when = datetime.strptime(f"{r['date']} {r.get('time', '00:00')}", "%Y-%m-%d %H:%M")
        except ValueError:
            continue
        if when + GRACE <= now:
            out.append(f.parent)
    return out


def playwright_env() -> dict:
    """Shim ngoài repo: require('playwright') -> node_modules/playwright-core (repo không cài gói 'playwright')."""
    shim = Path(tempfile.gettempdir()) / "pw_shim" / "node_modules"
    idx = shim / "playwright" / "index.js"
    if not idx.exists():
        idx.parent.mkdir(parents=True, exist_ok=True)
        core = (ROOT / "node_modules" / "playwright-core").as_posix()
        idx.write_text(f"module.exports = require('{core}');\n", encoding="ascii")
    env = dict(os.environ)
    env["NODE_PATH"] = str(shim)
    return env


def main() -> int:
    todo = due_projects()
    if "--test" in sys.argv:
        # Kiểm tra toàn bộ đường chạy trên 1 tập ĐÃ gắn sẵn (không thay đổi gì trên YouTube: Lưu bị khoá khi không đổi).
        todo = [ROOT / "projects" / sys.argv[sys.argv.index("--test") + 1]]
    if "--list" in sys.argv:
        print("\n".join(p.name for p in todo) or "(không có tập nào đến hạn)")
        return 0
    if not todo:
        log("không có tập nào đến hạn")
        return 0
    log("gắn link: " + ", ".join(p.name for p in todo))
    p = subprocess.run(["node", str(ROOT / "src/episode/link_shorts_related.cjs"), *map(str, todo)],
                       cwd=ROOT, env=playwright_env(), capture_output=True, text=True, encoding="utf-8", timeout=1800)
    for line in (p.stdout + p.stderr).splitlines():
        if line.strip():
            log("  " + line.strip()[:300])
    left = [x.name for x in todo if not json.loads((x / "upload_result.json").read_text(encoding="utf-8")).get("shorts_related")]
    log("xong" if not left else f"CHƯA gắn được (thử lại lần chạy sau): {', '.join(left)}")
    return 1 if left else 0


if __name__ == "__main__":
    sys.exit(main())

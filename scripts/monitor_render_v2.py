import time
from pathlib import Path

term_file = Path(r"C:\Users\PC\.cursor\projects\c-QuangHy-youtube-ai-edit-02\terminals\344169.txt")

for _ in range(60):
    if term_file.exists():
        txt = term_file.read_text(encoding="utf-8", errors="ignore")
        lines = [line.strip() for line in txt.splitlines() if line.strip()]
        last_lines = lines[-5:] if len(lines) >= 5 else lines
        status_line = [l for l in lines[:10] if l.startswith("status:")]
        status = status_line[0] if status_line else "running"
        print(f"[{status}] Latest output:")
        for l in last_lines:
            print("  ", l[:100])
        if "succeeded" in status or "failed" in status:
            break
    time.sleep(10)

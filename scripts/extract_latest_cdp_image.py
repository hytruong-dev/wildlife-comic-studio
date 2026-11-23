import json
import base64
from pathlib import Path

LOGS_DIR = Path(r"C:\Users\PC\.cursor\browser-logs")
INBOX_DIR = Path(__file__).resolve().parents[1] / "projects" / "tap-07-tom-tit" / "assets" / "inbox"
INBOX_DIR.mkdir(parents=True, exist_ok=True)

def main():
    files = sorted(LOGS_DIR.glob("cdp-response-Runtime.evaluate-*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not files:
        print("No cdp response files found")
        return
    
    target_file = files[0]
    print(f"Reading {target_file.name} ...")
    data = json.loads(target_file.read_text(encoding="utf-8"))
    
    val = data.get("result", {}).get("value", {})
    filename = val.get("filename", "unknown.png")
    data_url = val.get("dataURL", "")
    
    if not data_url or "," not in data_url:
        print("No valid dataURL found in response")
        return
    
    header, b64 = data_url.split(",", 1)
    img_bytes = base64.b64decode(b64)
    out_path = INBOX_DIR / filename
    out_path.write_bytes(img_bytes)
    print(f"SUCCESS: Saved {filename} ({len(img_bytes):,} bytes) to {out_path}")

if __name__ == "__main__":
    main()

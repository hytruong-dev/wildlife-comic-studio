import os
import json
import base64
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler

PROJ = Path(__file__).resolve().parents[1]
RAW_DIR = PROJ / "assets" / "gemini_downloaded" / "_raw_with_watermark_backup"
RAW_DIR.mkdir(parents=True, exist_ok=True)

class SaveHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        payload = json.loads(post_data.decode('utf-8'))
        filename = payload['filename']
        data_url = payload['dataUrl']

        header, encoded = data_url.split(',', 1)
        img_bytes = base64.b64decode(encoded)

        out_path = RAW_DIR / filename
        out_path.write_bytes(img_bytes)
        print(f"[SAVED] {filename} -> {len(img_bytes):,} bytes at {out_path.name}")

        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(b'{"status":"ok"}')

def run_server():
    server = HTTPServer(('127.0.0.1', 8765), SaveHandler)
    print("Image receiver server listening on http://127.0.0.1:8765 ...")
    server.serve_forever()

if __name__ == '__main__':
    run_server()

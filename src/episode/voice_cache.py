"""Giữ cache giọng đúng khi CHÈN / XÓA / ĐỔI THỨ TỰ part trong episode.json (lỗi suýt gặp ở Tập 9).

Cache giọng tên theo vị trí: audio/vs/<scene>_p<i>.wav. Chèn 1 part vào giữa chương -> mọi part phía sau đổi số,
`tts` sẽ ghép NHẦM giọng cũ vào lời mới (hoặc đọc lại cả chương). Công cụ này khớp theo NỘI DUNG:

  python src/episode/voice_cache.py projects/<slug> snapshot   # TRƯỚC khi sửa episode.json: lưu text của từng file cache
  ... sửa episode.json (chèn/xóa/sửa part) ...
  python src/episode/voice_cache.py projects/<slug> remap      # đổi tên file cache theo text mới; part mới/sửa -> xóa để tts đọc lại
  python src/episode/pipeline.py tts projects/<slug>            # chỉ đọc part mới

snapshot ghi audio/vs/_cache_index.json {file: text}. Part có text đổi (dù 1 chữ) được coi là mới.
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parent))
from pipeline import ptext  # noqa: E402


def current(ep: dict) -> dict:
    out = {}
    for sc in ep["longform"]["scenes"]:
        for i, p in enumerate(sc["parts"]):
            d = p if isinstance(p, dict) else {}
            out[f"{sc['id']}_p{i}.wav"] = json.dumps([ptext(p), d.get("mood"), d.get("cast")], ensure_ascii=False)
    out["shorts.wav"] = json.dumps([ep["shorts"]["text"], ep["shorts"].get("mood"), None], ensure_ascii=False)
    return out


def main() -> None:
    P, cmd = Path(sys.argv[1]).resolve(), sys.argv[2]
    vs = P / "audio" / "vs"
    idx_f = vs / "_cache_index.json"
    ep = json.loads((P / "episode.json").read_text(encoding="utf-8"))
    cur = current(ep)
    if cmd == "snapshot":
        snap = {f: t for f, t in cur.items() if (vs / f).exists()}
        idx_f.write_text(json.dumps(snap, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"snapshot: {len(snap)} cached parts -> {idx_f.name}")
        return
    if cmd != "remap":
        raise SystemExit(__doc__)
    if not idx_f.exists():
        raise SystemExit("chưa có snapshot — chạy 'snapshot' TRƯỚC khi sửa episode.json")
    old = json.loads(idx_f.read_text(encoding="utf-8"))
    by_text = {}
    for f, t in old.items():
        by_text.setdefault(t, []).append(f)
    tmp = vs / "_remap_tmp"
    tmp.mkdir(exist_ok=True)
    for f in old:  # move everything aside first (avoids name collisions when shifting)
        if (vs / f).exists():
            (vs / f).replace(tmp / f)
    kept = new = 0
    for f, t in cur.items():
        src = by_text.get(t, [])
        if src:
            (tmp / src.pop(0)).replace(vs / f)
            kept += 1
        else:
            new += 1
            print(f"  NEW/CHANGED -> sẽ đọc lại: {f}")
    for f in tmp.iterdir():  # cached parts no longer used
        f.unlink()
        print(f"  dropped (không còn trong kịch bản): {f.name}")
    tmp.rmdir()
    for f in vs.glob("*_48k.wav"):  # tempo-processed copies are rebuilt by tts
        f.unlink()
    idx_f.write_text(json.dumps({f: t for f, t in cur.items() if (vs / f).exists()}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"remap: giữ {kept} part, cần đọc mới {new} part -> chạy pipeline.py tts")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        raise SystemExit(1)
    main()

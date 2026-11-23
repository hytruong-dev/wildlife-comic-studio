"""Lịch đăng chuẩn TASTE-68 cho mọi tập lẻ + mega (nguồn duy nhất khi chủ kênh nói "đăng").

  python src/episode/publish_schedule.py            # sinh lại config/publish_schedule.json + docs/LICH_DANG_VIDEO.md
  python src/episode/publish_schedule.py --show 21  # in lịch + lệnh upload của Tập 21 (hoặc --show mega-02)
  python src/episode/publish_schedule.py --next     # mục chưa đăng kế tiếp (đã có video render)

Quy tắc:
  * 1 tập/ngày: video dài 17:00 ngày D, Shorts của tập đó 11:30 ngày D+1 (rồi gắn "Video có liên quan").
  * Mega (tổng hợp 10 tập): THỨ BẢY 17:00 đầu tiên SAU khi tập thứ 10 của nhóm đã lên sóng; ngày đó không đăng tập lẻ
    (tập lẻ lùi 1 ngày). Shorts của mega 11:30 Chủ Nhật -> mỗi ngày vẫn đúng 1 Shorts + 1 video dài.
  * Mục đã đăng lấy giờ thực tế từ projects/*/upload_result.json (hoặc ACTUAL bên dưới), không bao giờ bị dời.
"""
from __future__ import annotations

import datetime as dt
import glob
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ROADMAP = json.loads((ROOT / "config/series_roadmap.json").read_text(encoding="utf-8"))
OUT_JSON = ROOT / "config/publish_schedule.json"
OUT_MD = ROOT / "docs/LICH_DANG_VIDEO.md"

LONG_T, SHORTS_T = "17:00", "11:30"
FIRST_FREE_DAY = dt.date(2026, 11, 17)   # ngày đầu tiên chưa có tập nào lên lịch (Tập 20 = 16/11)
LAST_EP = 60
WD = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"]

# Giờ lên sóng thực tế (đo trên YouTube 12/11/2026) cho mục không có/ sai upload_result.json
ACTUAL = {
    "ep1": ("2026-11-04 17:34", None), "ep2": ("2026-11-05 11:48", None), "ep3": ("2026-11-05 18:23", None),
    "ep4": ("2026-11-06 16:07", None), "ep5": ("2026-11-07 11:00", None),
    "ep6": ("2026-11-07 18:30", "2026-11-07 18:30"),
    "mega-01": ("2026-11-10 18:30", "2026-11-10 18:30"),
}
YT_ID = {"ep1": "WRAp223qZ60", "ep2": "DOPcbU7gvjs", "ep3": "WbE6Nn7XUIE", "ep4": "ogvEUfQOWGA", "ep5": "KXJQReDxDcA", "ep6": "HEjl0zaZSTQ"}


def project_for(key: str) -> str | None:
    pat = f"tap-{int(key[2:]):02d}-*" if key.startswith("ep") else f"{key}-*"
    hits = [p for p in sorted(glob.glob(str(ROOT / "projects" / pat))) if "bang-phong-than" not in p]
    return os.path.relpath(hits[0], ROOT).replace("\\", "/") if hits else None


def uploaded(proj: str | None) -> dict | None:
    if not proj or not (ROOT / proj / "upload_result.json").exists():
        return None
    r = json.loads((ROOT / proj / "upload_result.json").read_text(encoding="utf-8"))
    if "date" not in r:
        long_val = r.get("publish", "").split(" (")[0] or None
        m_l = re.search(r"youtu\.be/([\w-]+)", str(r.get("long", "")))
        m_s = re.search(r"youtu\.be/([\w-]+)", str(r.get("shorts", "")))
        return {
            "long": long_val, "shorts": long_val,
            "long_id": r.get("long_id") or (m_l.group(1) if m_l else None),
            "shorts_id": r.get("shorts_id") or (m_s.group(1) if m_s else None),
            "related": r.get("shorts_related"),
        }
    sh_date = r.get("shorts_date", r["date"])
    sh_time = r.get("shorts_time", r.get("time", "11:30"))
    return {
        "long": f"{r['date']} {r['time']}" if "time" in r else None,
        "shorts": f"{sh_date} {sh_time}",
        "long_id": r.get("long_id"), "shorts_id": r.get("shorts_id"), "related": r.get("shorts_related"),
    }


def build() -> list[dict]:
    names = {e["ep"]: e["animal"] for e in ROADMAP["episodes"]}
    items: list[dict] = []
    for n in range(1, LAST_EP + 1):
        key = f"ep{n}"
        proj = project_for(key)
        it = {"key": key, "kind": "tap", "no": n, "title": f"Tập {n} — {names.get(n, '?')}", "project": proj}
        up = uploaded(proj)
        if key in ACTUAL:
            sh_time = (up or {}).get("shorts") or ACTUAL[key][1]
            it.update(long=ACTUAL[key][0], shorts=sh_time, status="published")
            it["long_id"] = YT_ID.get(key) or (up or {}).get("long_id")
            it["shorts_id"] = (up or {}).get("shorts_id")
        elif up and up.get("long"):
            it.update(up, status="scheduled")
        items.append(it)
        if n % 10 == 0:  # mega sau mỗi 10 tập
            m = n // 10
            mk = f"mega-{m:02d}"
            mp = project_for(mk)
            mi = {"key": mk, "kind": "mega", "no": m, "title": f"Mega {m:02d} — tổng hợp Tập {n - 9}-{n}", "project": mp}
            if m == 1:
                mi["title"] = "Mega 01 — Đại Hội Sinh Tồn #1 (Tập 1-10)"
            if m == 2:
                mi["title"] = "Mega 02 — Đại Hội Sinh Tồn Mùa 2 (Tập 11-20)"
            mup = uploaded(mp)
            if mk in ACTUAL:
                mi.update(long=ACTUAL[mk][0], shorts=ACTUAL[mk][1], status="published",
                          long_id=(mup or {}).get("long_id"), shorts_id=(mup or {}).get("shorts_id"))
            elif mup and mup.get("long"):
                mi.update(mup, status="scheduled")
            items.append(mi)

    for it in items:
        it.setdefault("status", "planned")
    return items


def build_fixed() -> list[dict]:
    """Xếp tuần tự: mỗi ngày 1 mục; mega luôn chiếm thứ Bảy đầu tiên sau khi tập thứ 10 của nhóm đã lên."""
    items = build()
    fixed = [i for i in items if i["status"] != "planned"]
    queue = [i for i in items if i["status"] == "planned"]
    taps = [i for i in queue if i["kind"] == "tap"]
    megas = [i for i in queue if i["kind"] == "mega"]
    long_day = {i["key"]: dt.date.fromisoformat(i["long"][:10]) for i in fixed}
    day = (max(long_day.values()) + dt.timedelta(days=1)) if long_day else FIRST_FREE_DAY
    out = []
    while taps or megas:
        m = megas[0] if megas else None
        ready = m and f"ep{m['no'] * 10}" in long_day and day > long_day[f"ep{m['no'] * 10}"]
        if m and ready:
            cur = megas.pop(0)
        elif taps:
            cur = taps.pop(0)
        else:
            cur = megas.pop(0)
        cur.update(long=f"{day} {LONG_T}", shorts=f"{day + dt.timedelta(days=1)} {SHORTS_T}")
        long_day[cur["key"]] = day
        out.append(cur)
        day += dt.timedelta(days=1)
    return fixed + out


def fmt(s: str | None) -> str:
    if not s:
        return "—"
    d = dt.datetime.strptime(s, "%Y-%m-%d %H:%M")
    return f"{WD[d.weekday()]} {d:%d/%m/%Y} {d:%H:%M}"


def upload_cmd(it: dict) -> str:
    proj = it.get("project") or f"projects/<{it['key']}-slug>"
    ld, lt = it["long"].split()
    sd, st = it["shorts"].split()
    return f"node src/episode/upload_youtube.cjs {proj} --date {ld} --time {lt} --shorts-date {sd} --shorts-time {st}"


def write(items: list[dict]) -> None:
    OUT_JSON.write_text(json.dumps({
        "_doc": "SINH TỰ ĐỘNG bởi src/episode/publish_schedule.py — đừng sửa tay. Lịch TASTE-68: dài 17:00 ngày D, Shorts 11:30 ngày D+1, "
                "mega thứ Bảy 17:00. Giờ = Asia/Ho_Chi_Minh (UTC+7). Khi chủ kênh nói 'đăng' mà không kèm giờ -> dùng đúng mục này.",
        "generated": dt.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "items": items}, ensure_ascii=False, indent=1), encoding="utf-8")

    L = ["# LỊCH ĐĂNG VIDEO — Vẽ Chuyện Hoang Dã", "",
         "> **SINH TỰ ĐỘNG** từ `python src/episode/publish_schedule.py` (dữ liệu: `config/publish_schedule.json`). Đừng sửa tay — sửa script rồi chạy lại.",
         f"> Cập nhật: {dt.datetime.now():%d/%m/%Y %H:%M}. Giờ Việt Nam (UTC+7).", "",
         "## Quy tắc (TASTE-68, chốt 12/11/2026)", "",
         "| Loại | Giờ | Ghi chú |", "|---|---|---|",
         "| Video dài tập lẻ | **17:00** ngày D | 1 tập/ngày, không đăng 2 tập/ngày |",
         "| Shorts của tập đó | **11:30** ngày D+1 | Sau đó chạy `link_shorts_related.cjs` (video dài đã công khai) |",
         "| Mega (10 tập) | **17:00 ngày tiếp theo** | Phát sóng ngay sau khi tập thứ 10 của nhóm lên sóng (cứ 10 tập có 1 Mega). Shorts mega 11:30 ngày hôm sau |",
         "| Hashtag | 3 tag có dấu | `#độngvật #<con vật> #VẽChuyệnHoangDã` — tiêu đề không `| Tập N`, Shorts không `#shorts` |", "",
         "## Khi chủ kênh nói \"đăng\"", "",
         "1. `python src/episode/publish_schedule.py --show <số tập | mega-NN>` → in ngày giờ + lệnh upload đúng lịch.",
         "2. Nếu giờ trong lịch đã qua (hoặc < 30 phút nữa) → báo chủ kênh, đề xuất mục kế tiếp; **không** tự dời cả lịch.",
         "3. Chủ kênh chỉ định giờ khác → dùng giờ đó, rồi chạy lại script để cập nhật lịch (mục đã lên lịch lấy giờ từ `upload_result.json`).",
         "4. Sau 17:00 ngày đăng video dài: `node src/episode/link_shorts_related.cjs <project>`.", "",
         "## Lịch đầy đủ", "",
         "| # | Video | Video dài | Shorts | Trạng thái | Dự án |", "|---|---|---|---|---|---|"]
    st_vi = {"published": "✅ đã lên", "scheduled": "⏰ đã hẹn giờ", "planned": "📝 kế hoạch"}
    now = dt.datetime.now()
    for it in items:
        st = it["status"]
        if st == "scheduled" and dt.datetime.strptime(it["long"], "%Y-%m-%d %H:%M") <= now:
            st = "published"
        it["status"] = st
        name = f"**{it['title']}**" if it["kind"] == "mega" else it["title"]
        link = f" [▶](https://youtu.be/{it['long_id']})" if it.get("long_id") else ""
        L.append(f"| {it['key']} | {name}{link} | {fmt(it['long'])} | {fmt(it.get('shorts'))} | {st_vi[st]} | "
                 f"{('`' + it['project'] + '`') if it.get('project') else '_chưa làm_'} |")
    L += ["", "## Ghi chú lịch sử", "",
          "- Tập 1–15 + Mega 01 đăng theo lịch cũ (2 tập/ngày 11:30 & 18:00, Shorts cùng giờ). Số liệu 12/11/2026: Shorts 11:30 hơn Shorts tối; "
          "video dài 0–33 view vì Shorts chưa gắn \"Video có liên quan\" (đã gắn lại Tập 6–15 + Mega 01).",
          "- Tập 16–20 đã dời sang lịch mới ngày 12/11/2026.",
          "- `projects/mega-01-bang-phong-than/` (bản cắt ghép) **không nằm trong lịch** — chỉ đăng khi chủ kênh yêu cầu.", ""]
    OUT_MD.write_text("\n".join(L), encoding="utf-8")


def main() -> None:
    items = build_fixed()
    write(items)
    a = sys.argv[1:]
    if "--show" in a:
        q = a[a.index("--show") + 1].lower()
        key = q if q.startswith(("ep", "mega")) else f"ep{int(q)}"
        it = next((i for i in items if i["key"] == key), None)
        if not it:
            raise SystemExit(f"không có {key} trong lịch")
        print(f"{it['title']} [{it['status']}]\n  Video dài: {fmt(it['long'])}\n  Shorts   : {fmt(it.get('shorts'))}")
        if it["status"] == "planned":
            print("  Lệnh:", upload_cmd(it))
    elif "--next" in a:
        for it in items:
            if it["status"] == "planned":
                ready = it.get("project") and list((ROOT / it["project"] / "renders").glob("*_long.mp4"))
                print(f"{it['title']}: {fmt(it['long'])} | Shorts {fmt(it['shorts'])} | render: {'có' if ready else 'CHƯA'}")
                if ready:
                    print("  Lệnh:", upload_cmd(it))
                break
    else:
        print(f"-> {OUT_JSON.relative_to(ROOT)} + {OUT_MD.relative_to(ROOT)} ({len(items)} mục)")


if __name__ == "__main__":
    main()


"""Sinh specs/extra_prompts.json: banner chương C01..C0N + banner Shorts B00 + thumbnail T01 (Gemini vẽ CẢ chữ).

  python src/episode/extra_prompts.py projects/<slug>

Lấy dữ liệu từ episode.json:
  scenes[].badge (nhãn trái, ≤ 16 ký tự) + scenes[].banner_title (chữ thanh navy; mặc định = phần sau dấu ':' của chapter_title)
  format (F1..F7 -> màu badge + icon, docs/strategy/FORMAT_KE_CHUYEN.md 4.B)
  "art": {
    "decor": "tiny snowflakes",                          # đạo cụ theo chủ đề con vật (tuyết, lá, sóng...)
    "shorts_banner_lines": ["DÒNG 1", "DÒNG 2?!"],        # mặc định = shorts_title_lines của storyboard
    "shorts_mascot": "a small cute cartoon ... holding a small wooden judge gavel",
    "thumb_title": ["DÒNG 1?!", "DÒNG 2"],
    "thumb_scene": "mô tả nhân vật chính to bên PHẢI + biểu cảm + đạo cụ format",
    "thumb_gag": "chi tiết hài góc dưới phải",
    "thumb_bg": "nền tối tương phản (biển đêm, vũ trụ, rừng đêm...)"
  }
Sau khi tạo ảnh: ảnh C*/B00 nằm ở assets/_src/*.txt -> python src/episode/prep_banners.py <project> <project>/assets/_src
(prep_banners tự giải mã .txt), T01 nằm ở inbox -> import_images.py.
"""
import json
import sys
from pathlib import Path
from prompt_sanitizer import sanitize_prompt

sys.stdout.reconfigure(encoding="utf-8")

FMT = {  # FORMAT_KE_CHUYEN.md 4.B + 4.D
    "F1": ("medical teal", "medical cross, stethoscope, X-ray film, pill capsules", "một tấm phim X-quang"),
    "F2": ("military olive green", "measurement grid, blueprint gears, warning stripes", "một bản vẽ blueprint kỹ thuật"),
    "F3": ("courtroom gold", "a small gavel, scales of justice, magnifying glass and fingerprint", "vành móng ngựa và chiếc búa tòa án"),
    "F4": ("sunrise orange", "alarm clock, sun and moon, hourglass", "một chiếc đồng hồ báo thức to"),
    "F5": ("laboratory purple", "test tubes, bubbling flask, level-up arrows, warning signs", "ống nghiệm sủi bọt và thanh level"),
    "F6": ("crimson red", "crown, chess pieces, fedora hat, pyramid hierarchy chart", "vương miện và sơ đồ quyền lực"),
    "F7": ("red-orange", "crossed swords, shield, lightning bolt, HP bar", "thanh máu HP"),
}
FMT["LEGACY_6CH"] = FMT["F7"]
# Mega Compilation / Đại hội (docs/strategy/MEGA_COMPILATION.md)
FMT["F_SPECIAL"] = ("royal purple", "golden trophy, small crown, ranking podium, tier list badges",
                    "một tấm bảng xếp hạng Tier List 4 hàng màu vàng-đỏ-tím-xám")

FMT_BAR_STYLES = {
    "F1": (
        "on the left is a medical teal clipboard badge with a silver metal clip and red cross icon containing bold white uppercase Vietnamese text \"{badge}\"; "
        "immediately to the right is a glowing dark X-ray film horizontal bar with an ECG heartbeat line frame containing bold cyan-white uppercase Vietnamese text \"{title}\""
    ),
    "F2": (
        "on the left is a brushed steel mechanical tag with bolted corners and military olive green fill containing bold white stencil uppercase Vietnamese text \"{badge}\"; "
        "immediately to the right is a technical CAD blueprint horizontal bar with millimeter ruler markings and brass gear corners containing bold bright yellow uppercase Vietnamese text \"{title}\""
    ),
    "F3": (
        "on the left is a crimson red wax-sealed detective evidence tag with a magnifying glass icon containing bold white uppercase Vietnamese text \"{badge}\"; "
        "immediately to the right is a vintage kraft-paper dossier bar wrapped with yellow-and-black hazard tape stripes containing bold dark-outlined yellow uppercase Vietnamese text \"{title}\""
    ),
    "F4": (
        "on the left is a glowing sunrise-orange survival timer badge with an hourglass icon containing bold white uppercase Vietnamese text \"{badge}\"; "
        "immediately to the right is a rugged expedition log horizontal bar with cracked frost/rock edges and neon survival frame containing bold bright yellow uppercase Vietnamese text \"{title}\""
    ),
    "F5": (
        "on the left is a glowing laboratory purple bio-specimen tag with a barcode and bubbling flask icon containing bold white uppercase Vietnamese text \"{badge}\"; "
        "immediately to the right is a high-tech stainless steel lab chamber bar with neon acid-green hazard borders containing bold bright yellow uppercase Vietnamese text \"{title}\""
    ),
    "F6": (
        "on the left is a royal crimson emblem shield with a golden crown and wax seal containing bold white uppercase Vietnamese text \"{badge}\"; "
        "immediately to the right is an ornate vintage parchment scroll bar with engraved golden filigree borders containing bold dark-outlined golden uppercase Vietnamese text \"{title}\""
    ),
    "F7": (
        "on the left is a fiery red-orange RPG level shield badge with crossed swords containing bold white uppercase Vietnamese text \"{badge}\"; "
        "immediately to the right is a dark obsidian game UI horizontal bar with a glowing golden HP-bar frame containing bold bright yellow uppercase Vietnamese text \"{title}\""
    ),
}

FMT_SHORTS_BANNERS = {
    "F1": (
        "a 2D cartoon medical emergency dossier title board isolated on a pure solid white background: a sleek dark teal clinical monitor frame "
        "with glowing ECG pulse lines, a silver clipboard clasp on top, and red medical cross badges on the sides"
    ),
    "F2": (
        "a 2D cartoon mechanical blueprint title plaque isolated on a pure solid white background: a riveted dark cobalt engineering plate "
        "with brass gears, caliper measurement marks on the border, and yellow-black industrial stripes on the corners"
    ),
    "F3": (
        "a 2D cartoon detective case-file title board isolated on a pure solid white background: a dark charcoal investigation board "
        "pinned with red string, a golden magnifying glass emblem, and yellow crime-scene tape folded on both ends"
    ),
    "F4": (
        "a 2D cartoon extreme-survival title plaque isolated on a pure solid white background: a rugged dark slate survivalist sign "
        "with glowing orange countdown framing, cracked ice/lava elemental accents on the corners, and compass emblems"
    ),
    "F5": (
        "a 2D cartoon secret-laboratory title board isolated on a pure solid white background: a metallic dark purple containment plaque "
        "with glowing neon acid-green tube borders, bubbling test flasks on the left corner, and hazard warning chevrons"
    ),
    "F6": (
        "a 2D cartoon royal mafia syndicate title crest isolated on a pure solid white background: a deep velvet crimson and obsidian banner "
        "with ornate golden baroque framing, red wax seals, and royal crown/chess emblems on the ends"
    ),
    "F7": (
        "a 2D cartoon RPG boss-arena title banner isolated on a pure solid white background: a dark volcanic stone plaque "
        "with a blazing golden metallic frame, crossed swords, and glowing energy crystals on both ends"
    ),
}

FMT_CARD_STYLES = {
    "F1": (
        "a large ornate 2D cartoon clinical medical monitor chapter title plaque isolated on a pure solid white background: "
        "a glowing dark teal X-ray screen frame with silver surgical clamps, a red medical cross emblem on top containing bold white uppercase Vietnamese text \"{badge}\", "
        "center large glowing yellow uppercase Vietnamese headline \"{title}\", and a bottom cyan ECG pulse ribbon containing bold white uppercase Vietnamese subtitle \"{sub}\""
    ),
    "F2": (
        "a large ornate 2D cartoon mechanical blueprint chapter title board isolated on a pure solid white background: "
        "a riveted cobalt-blue steel engineering plate with rotating brass gears on the corners, a top military olive stencil tag containing bold white uppercase Vietnamese text \"{badge}\", "
        "center large bright yellow uppercase Vietnamese headline \"{title}\", and a bottom caliper ruler strip containing bold cyan-white uppercase Vietnamese subtitle \"{sub}\""
    ),
    "F3": (
        "a large ornate 2D cartoon detective case-file chapter title board isolated on a pure solid white background: "
        "a vintage manila dossier board wrapped with yellow-and-black crime-scene hazard tape and pinned with a golden magnifying glass, a top crimson wax-seal badge containing bold white uppercase Vietnamese text \"{badge}\", "
        "center large bright yellow dark-outlined uppercase Vietnamese headline \"{title}\", and a bottom dark evidence strip containing bold white uppercase Vietnamese subtitle \"{sub}\""
    ),
    "F4": (
        "a large ornate 2D cartoon extreme-survival chapter title plaque isolated on a pure solid white background: "
        "a rugged expedition board framed with glowing frost crystals and thermal lava cracks, a top sunrise-orange timer badge containing bold white uppercase Vietnamese text \"{badge}\", "
        "center large bright yellow uppercase Vietnamese headline \"{title}\", and a bottom survival gauge bar containing bold cyan-white uppercase Vietnamese subtitle \"{sub}\""
    ),
    "F5": (
        "a large ornate 2D cartoon secret bio-laboratory chapter title plaque isolated on a pure solid white background: "
        "a high-tech chamfered dark purple containment chamber board with glowing neon acid-green glass tubes and bubbling flasks on the corners, a top purple barcode specimen badge containing bold white uppercase Vietnamese text \"{badge}\", "
        "center large glowing bright yellow uppercase Vietnamese headline \"{title}\", and a bottom dark cyber-lab ribbon containing bold cyan uppercase Vietnamese subtitle \"{sub}\""
    ),
    "F6": (
        "a large ornate 2D cartoon royal mafia syndicate chapter title crest isolated on a pure solid white background: "
        "a deep velvet crimson and obsidian plaque with baroque golden filigree borders and a golden crown on top, a top crimson shield badge containing bold white uppercase Vietnamese text \"{badge}\", "
        "center large metallic golden uppercase Vietnamese headline \"{title}\", and a bottom parchment scroll ribbon containing bold white uppercase Vietnamese subtitle \"{sub}\""
    ),
    "F7": (
        "a large ornate 2D cartoon RPG boss-arena chapter title plaque isolated on a pure solid white background: "
        "a dark volcanic armor board with blazing golden flames and crossed swords, a top fiery red-orange shield badge containing bold white uppercase Vietnamese text \"{badge}\", "
        "center large glowing yellow uppercase Vietnamese headline \"{title}\", and a bottom glowing HP-bar ribbon containing bold white uppercase Vietnamese subtitle \"{sub}\""
    ),
}

BAR_TEMPLATE = (
    "Tạo hình ảnh tỉ lệ 21:9 rất dẹt ngang (chiều cao chỉ khoảng 1/10 chiều dài). 2D hand-drawn cartoon illustration "
    "of a two-part horizontal header bar isolated on a pure solid white background: {bar_design}. "
    "Decorated with {decor}, {icons} around the frame corners. Vibrant colors, bold clean outlines, clean cutout, no watermark. "
    "Vietnamese text must be spelled exactly with correct diacritics."
)

CARD_TEMPLATE = (
    "Tạo hình ảnh tỉ lệ ngang 16:9. {card_design}. "
    "Decorated with {decor}, {icons} around the outer frame. 2D comic cartoon illustration, vibrant colors, bold black ink outlines, "
    "isolated on a pure solid white background, clean cutout, no watermark. "
    "Vietnamese text must be spelled exactly with correct diacritics."
)


def main() -> None:
    P = Path(sys.argv[1]).resolve()
    ep = json.loads((P / "episode.json").read_text(encoding="utf-8"))
    sbf = P / "specs" / "storyboard.json"
    sb = json.loads(sbf.read_text(encoding="utf-8")) if sbf.exists() else {}
    art = ep.get("art", {})
    fmt_key = ep.get("format", "F7")
    color, icons, prop = FMT.get(fmt_key, FMT["F7"])
    decor = art.get("decor", "tiny green leaves")
    custom_bar_design = art.get("banner_bar_style") or FMT_BAR_STYLES.get(fmt_key, FMT_BAR_STYLES["F7"])
    custom_card_design = art.get("card_style") or FMT_CARD_STYLES.get(fmt_key, FMT_CARD_STYLES["F7"])
    out = {"_doc": "Sinh bởi src/episode/extra_prompts.py. C = banner thanh tiêu đề trên, K = bảng chuyển chương giữa màn hình, B00 = banner Shorts, T01 = thumbnail."}
    for i, sc in enumerate(ep["longform"]["scenes"], 1):
        badge = sc.get("badge") or f"CHƯƠNG {i}"
        title = (sc.get("banner_title") or sc["chapter_title"].split(":", 1)[-1]).strip().upper()
        if len(title) > 32:
            print(f"  !! C{i:02d}: banner_title dài {len(title)} ký tự — nên ≤ 32 (đặt scenes[].banner_title ngắn hơn)")
        scene_bar_design = sc.get("banner_bar_style") or custom_bar_design
        bar_filled = scene_bar_design.format(color=color, badge=badge.upper(), title=title)
        out[f"C{i:02d}"] = BAR_TEMPLATE.format(bar_design=bar_filled, decor=decor, icons=icons)

        sub = (sc.get("card_sub") or sc.get("hook") or "").strip().upper()
        scene_card_design = sc.get("card_style") or custom_card_design
        card_filled = scene_card_design.format(color=color, badge=badge.upper(), title=title, sub=sub)
        out[f"K{i:02d}"] = CARD_TEMPLATE.format(card_design=card_filled, decor=decor, icons=icons)
    l1, l2 = art.get("shorts_banner_lines") or sb.get("shorts_title_lines") or ["?", "?"]
    mascot = art.get("shorts_mascot", f"a small cute cartoon {ep['animal']}")
    shorts_board = art.get("shorts_banner_style") or FMT_SHORTS_BANNERS.get(fmt_key, FMT_SHORTS_BANNERS["F7"])
    out["B00"] = (f"Tạo hình ảnh tỉ lệ ngang 3:1. {shorts_board}, hard drop shadow. "
                  f"Inside, two lines of bold uppercase Vietnamese comic text: line 1 white \"{l1}\", line 2 bright yellow "
                  f"gradient with thick dark outline \"{l2}\". {mascot} sits on the top-right corner of the banner. "
                  f"Decorated with {decor}. Clean cutout, no watermark. Vietnamese text must be spelled exactly with correct diacritics.")
    t1, t2 = art.get("thumb_title", [l1 + "?!", ep["animal"].upper()])
    prop = art.get("thumb_prop", prop)
    thumb_style = art.get('style_label') or sb.get('style_label') or 'nghệ thuật độc bản'
    out["T01"] = (f"Tạo ảnh thumbnail YouTube tỉ lệ 16:9 theo {thumb_style} cực kỳ bắt mắt, đọc rõ ở kích thước nhỏ. NỀN TỐI "
                  f"tương phản mạnh: {art.get('thumb_bg', 'nền xanh đêm thẫm')} với tia sáng sunburst vàng tỏa ra từ phía sau nhân vật. "
                  f"BÊN PHẢI (chiếm ~45% khung): {art.get('thumb_scene', ep['animal'] + ' hoạt hình to rõ, biểu cảm cực mạnh')}"
                  + (f", kèm {prop}" if prop else "") + ". "
                  f"GÓC DƯỚI PHẢI: {art.get('thumb_gag', 'một chi tiết hài nghịch lý của tập')}. "
                  f"GÓC TRÊN TRÁI: huy hiệu nổ màu đỏ chữ trắng \"{art.get('thumb_badge') or 'TẬP %02d' % ep['episode_no']}\". BÊN TRÁI-TRÊN: tiêu đề 2 dòng chữ IN HOA "
                  f"tiếng Việt cực lớn màu vàng viền đen rất dày: dòng 1 \"{t1}\", dòng 2 \"{t2}\". Ít chi tiết, tương phản cao. "
                  "Chữ tiếng Việt phải viết đúng chính tả và đủ dấu.")
    out = {k: (sanitize_prompt(v) if not k.startswith("_") else v) for k, v in out.items()}
    (P / "specs" / "extra_prompts.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"extra prompts OK: {len(ep['longform']['scenes'])} banner chương + B00 + T01 -> specs/extra_prompts.json")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        raise SystemExit(1)
    main()

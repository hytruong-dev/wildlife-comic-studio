"""Export EP06 (the approved reference episode) into the generic episode format used by
src/episode/pipeline.py, into examples/ep06_reference/ — the worked example for future episodes."""
import ast
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
P = Path(__file__).resolve().parents[1]
ROOT = P.parents[1]
OUT = ROOT / "examples" / "ep06_reference"
OUT.mkdir(parents=True, exist_ok=True)
S = P / "scripts"

def dict_literal(path, name):
    for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
        if isinstance(node, ast.Assign) and any(getattr(t, "id", "") == name for t in node.targets):
            return ast.literal_eval(node.value)

TEXT = {**dict_literal(S / "generate_audio_ep06.py", "LONGFORM_ACTS"), **dict_literal(S / "generate_longform_expansion_ep06.py", "EXPANSION_PARTS"),
        **dict_literal(S / "generate_act1_and_act5_extras.py", "EXTRA_PARTS")}
sys.path.insert(0, str(S))
import build_longform_v2_spec as B  # noqa: E402

FILES = {"scene01": ["act01_myth_buster_hook.mp3", "act01_part2.mp3"], "scene02": ["act02_rpg_stats.mp3", "act02_part2.mp3"],
         "scene03": ["act03_cryptobiosis_mechanism.mp3", "act03_part2.mp3"], "scene04": ["act04_snail_weakness.mp3", "act04_part2.mp3"],
         "scene05": ["act05_moon_mission_beresheet.mp3", "act05_part2.mp3", "act05_part3.mp3"],
         "scene06": ["act06_evolution_lesson_teaser.mp3", "act06_part2.mp3"]}
SHORTS_TEXT = ast.literal_eval(ast.parse((S / "synthesize_perfect_shorts_voice.py").read_text(encoding="utf-8")).body[3].value) \
    if False else None
src = (S / "synthesize_perfect_shorts_voice.py").read_text(encoding="utf-8")
SHORTS_TEXT = "".join(ast.literal_eval(n.value) for n in ast.walk(ast.parse(src))
                      if isinstance(n, ast.Assign) and getattr(n.targets[0], "id", "") == "script" for _ in [0])

ep = {
    "episode_no": 6, "animal": "Gấu Nước", "slug": "tap-06-gau-nuoc",
    "whisper_prompt": "Gấu Nước Tardigrade bất tử, âm 272 độ C, 150 độ C, Ma-ri-a-na, Gray, ốc sên, Mặt Trăng, Bê-rê-shít",
    "display_fix": {"Ma-ri-a-na": "Mariana", "Bê-rê-shít": "Beresheet", "E-vơ-rét": "Everest", "T-D-Ps": "TDP",
                    "A-T-K": "ATK", "S-P-D": "SPD", "D-E-F": "DEF", "D-súp": "Dsup"},
    "longform": {"scenes": [{"id": sid, "chapter_title": B.PLAN[sid]["title"].capitalize(), "hook": B.PLAN[sid].get("hook", ""),
                             "parts": [TEXT[f] for f in fs]} for sid, fs in FILES.items()]},
    "shorts": {"target_s": 53.0, "text": SHORTS_TEXT},
    "seo": {
        "title": "Sống Sót 5 Lần Tận Thế... Nhưng Chết Vì Một Con Ốc Sên! | Gấu Nước | Tập 6",
        "hook_paragraph": "Gấu Nước (Tardigrade) nhỏ hơn hạt cát, chịu được âm 272°C, nước sôi 150°C, phóng xạ gấp 1.000 lần liều chết người và từng bị thả trần trụi ngoài vũ trụ 10 ngày mà vẫn sống. Vậy mà một con ốc sên lại có thể giết chết nó! Và ngay lúc này, hàng ngàn con Gấu Nước đang nằm ngủ trên Mặt Trăng...",
        "bullets": ["Vì sao Gấu Nước sống sót qua cả 5 cuộc đại tuyệt chủng", "Protein TDP biến cơ thể thành \"thủy tinh\", Dsup che chắn ADN khỏi phóng xạ",
                    "3 điểm yếu bi hài: chất nhầy ốc sên, giun tròn và… nước hơi ấm 37,6°C", "Vụ rơi tàu Beresheet năm 2019 rải Gấu Nước lên Mặt Trăng"],
        "question": "Nếu có siêu năng lực ngủ đông như Gấu Nước, bạn muốn thức dậy vào năm nào? Bình luận cho mình biết nhé!",
        "next_teaser": "Tôm Tít — cú đấm nhanh như đạn bắn!",
        "hashtags": ["#GauNuoc", "#Tardigrade", "#TheGioiDongVat", "#VeChuyenHoangDa", "#KhoaHoc"],
        "tags": ["gấu nước", "tardigrade", "gau nuoc", "water bear", "sinh vật bất tử", "sinh vật bất tử nhất trái đất", "gấu nước mặt trăng",
                 "gấu nước ốc sên", "cryptobiosis", "động vật kỳ lạ", "thế giới động vật", "khám phá động vật", "vẽ chuyện hoang dã",
                 "whiteboard animation", "khoa học thú vị", "beresheet", "đại tuyệt chủng"],
        "shorts_title": "Bất Tử Ngoài Vũ Trụ Nhưng Chết Vì Ốc Sên?! 🐌 #shorts #gaunuoc",
        "shorts_desc": "Sống qua 5 cuộc đại tuyệt chủng, chịu âm 272°C và nước sôi 150°C… nhưng Gấu Nước lại thua một con ốc sên! 🐌\n👉 Xem bản đầy đủ: hàng ngàn Gấu Nước đang nằm trên Mặt Trăng — video Tập 6 trên kênh Vẽ Chuyện Hoang Dã.",
        "shorts_tags": ["gấu nước", "tardigrade", "sinh vật bất tử", "shorts", "thế giới động vật", "vẽ chuyện hoang dã", "động vật kỳ lạ"],
    },
}
(OUT / "episode.json").write_text(json.dumps(ep, ensure_ascii=False, indent=1), encoding="utf-8")

rel = lambda p: p.replace("assets/", "../../projects/tap-06-gau-nuoc/assets/") if False else p
lp = {"targets": {k: list(v) for k, v in B.TARGETS.items()}, "scenes": {}}
for sid, pl in B.PLAN.items():
    lp["scenes"][sid] = {"chapter_no": pl["chapter_no"], "title": pl["title"], "hook": pl.get("hook", ""), "card": pl.get("card", True),
                         "beats": [{"at": ph, "image": img,
                                    "stickers": [{"at": a, "side": sd, "y": y, "value": v, "label": lb, **({"target": tg} if tg else {})}
                                                 for a, sd, y, v, lb, tg in stk], "impacts": imps}
                                   for ph, img, _ent, stk, imps in pl["beats"]]}
(OUT / "longform_plan.json").write_text(json.dumps(lp, ensure_ascii=False, indent=1), encoding="utf-8")

sv5 = json.loads((P / "specs" / "shorts_v5_spec.json").read_text(encoding="utf-8"))
sp = {"title_lines": sv5["title_lines"], "beats": [
    {"at_s": b["start_s"], "image": b["image"], "draw_s": b["draw_s"],
     "stickers": [{"at_s": s["t"], "side": s["side"], "y": s["y"], "value": s["value"], "label": s["label"], "target": s.get("target")} for s in b["stickers"]]}
    for b in sv5["beats"]]}
(OUT / "shorts_plan.json").write_text(json.dumps(sp, ensure_ascii=False, indent=1), encoding="utf-8")
print("exported ->", OUT, "| shorts chars", len(SHORTS_TEXT))

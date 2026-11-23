---
name: episode-production
description: Sản xuất trọn gói 1 tập "Vẽ Chuyện Hoang Dã" (video dài 16:9 ≥ 8:30 + Shorts 9:16 ~50s + banner + thumbnail + gói SEO) theo chuẩn vàng Tập 9 Chim Cánh Cụt — làm 1 lần là xong, không lỗi. Dùng khi chủ kênh nói "làm tập tiếp theo", "làm tập về <con vật>", "làm video <con vật>". Tự động làm mọi bước, DỪNG trước khi đăng YouTube.
---

# Sản xuất 1 tập — chuẩn vàng Tập 9 (Chim Cánh Cụt)

Lệnh kích hoạt: **"làm tập tiếp theo <con vật>"**. Làm hết Bước 0 → 8 **không hỏi lại** những gì đã quy định.
Chỉ dừng hỏi khi thật sự bị chặn (VoiceStudio không chạy, Google chưa đăng nhập trong profile Chrome).

> 📖 Đọc trước: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md` (12 luật + bảng lỗi) · `.agents/skills/core/humor-voice/SKILL.md` (kịch bản + giọng)
> · `docs/strategy/FORMAT_KE_CHUYEN.md` (format) · `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md` (mood/cameo).
> 🧩 **Mẫu hoàn chỉnh để bắt chước: `examples/ep09_reference/`** (episode.json, storyboard.json, plans, prompts, EPISODE_SPEC.md).
> ⛔ **CỔNG CẤM ĐĂNG:** không bao giờ tự upload/lên lịch. Xong Bước 8 → báo cáo → chờ lệnh "đăng" + giờ.

Kết quả Tập 9 (làm 1 lượt, QA PASS lần đầu): dài **8:48**, -14.2 LUFS, **87 ảnh** 16:9 riêng (0 dùng lại); Shorts 50s, 13 ảnh;
6 banner chương + banner Shorts + thumbnail do Gemini vẽ chữ đúng dấu; sàn nhiễu Shorts -47.6 dBFS. Tổng ~4 giờ máy (phần lớn chạy nền).

---

## Bản đồ công cụ (tất cả trong `src/episode/`, chạy từ thư mục gốc dự án)

| Bước | Lệnh | Ra |
|---|---|---|
| 0 | `python src/episode/pipeline.py init projects/<slug> --no N --animal "Tên"` | khung dự án, **format/persona tự lấy từ `config/series_roadmap.json`** |
| 0b | `python src/seo/episode_research.py projects/<slug> ideas [--en "English name"]` (~1-2 phút) | `specs/research_ideas.md` — khán giả tìm gì / hỏi gì (TubeLab `comment-mining`) |
| 1 | `python src/episode/pipeline.py check projects/<slug>` | ước lượng thời lượng (đã hiệu chỉnh ±5s), lint kịch bản, đa dạng giọng |
| 2 | `python src/episode/pipeline.py tts projects/<slug>` (nền, ~70-85 phút) | `audio/sceneXX.wav`, `audio/shorts.wav` |
| 2b | `python src/episode/voice_cache.py projects/<slug> snapshot` / `remap` | giữ cache giọng đúng khi chèn/xóa part |
| 3 | `python src/episode/build_plans.py projects/<slug>` | storyboard → `longform_plan.json`, `shorts_plan.json`, `image_prompts.json`, `image_catalog.md` |
| 3a | `python src/seo/episode_research.py projects/<slug> thumbs` | `specs/research_thumbs.md` + ảnh mẫu — MỞ XEM trước khi viết `art.thumb_*` (TubeLab `thumbnail-concepts`) |
| 3b | `python src/episode/extra_prompts.py projects/<slug>` | `extra_prompts.json` (banner C01..C0N, B00, thumbnail T01) |
| 4 | `node src/episode/gemini_gen.cjs projects/<slug> probe\|long\|shorts\|extra` (nền) | ảnh Gemini → `assets/inbox/*.txt`, `assets/_src/*.txt` — **không cần Playwright MCP** |
| 4b | `python src/episode/import_images.py projects/<slug> --sheet` | `assets/long|shorts/*.png`, thumbnail jpg, bảng xem `renders/snapshots/sheet_*.jpg` |
| 4c | `python src/episode/prep_banners.py projects/<slug> projects/<slug>/assets/_src` + `python src/episode/banner_sheet.py projects/<slug>` | `assets/banners/*.png` + bảng kiểm chính tả |
| 5 | `python src/episode/pipeline.py align projects/<slug>` (~4 phút) | `audio/long_words_fixed.json`, `shorts_words.json` |
| 6 | `python src/episode/pipeline.py spec projects/<slug>` → `python scripts/audit_beats.py projects/<slug>` → `python src/episode/target_sheet.py projects/<slug>` | spec OK + đọc từng beat + mũi tên đúng chỗ |
| 7 | `python src/episode/pipeline.py render projects/<slug> --preview` rồi `--force` (nền, ~25 phút) | `renders/<slug>_long.mp4`, `_shorts.mp4` |
| 7b | `pipeline.py qa` · `python scripts/beat_sheet.py` · `python scripts/hum_probe.py <P>/audio/shorts.wav <P>/renders/<slug>_shorts.mp4` | PASS / khung hình thật / sàn nhiễu |
| 8 | `python src/seo/episode_research.py projects/<slug> titles` (TubeLab `title-formulas`) · `pipeline.py seo` · `python src/seo/seo_research.py projects/<slug> --apply` · `python src/episode/episode_doc.py projects/<slug>` · `python src/memory/memory_harvester.py --log-video ...` | `seo_package.md`, `upload.json`, `specs/seo_research.md`, `EPISODE_SPEC.md`, nhật ký |
| 9 | `node src/episode/upload_youtube.cjs projects/<slug> --date YYYY-MM-DD --time HH:MM` | **CHỈ khi chủ kênh ra lệnh** |

Script riêng của tập (nếu cần) để trong `projects/<slug>/scripts/` (TASTE-18). Không viết lại công cụ chung cho từng tập.

## Thứ tự tối ưu thời gian (song song)
```
init → nghiên cứu → episode.json → check (sửa đến khi sạch) ─┬─► tts (nền ~80')
                                                             └─► storyboard.json → build_plans → extra_prompts
                                                                   → gemini_gen long/shorts/extra (nền, ~30s/ảnh ≈ 60')
tts xong → nếu TOO SHORT: viết thêm part (voice_cache snapshot/remap) → tts → thêm beat có "id" → gemini_gen --only
→ align → spec → audit_beats → target_sheet → render --preview → render --force → qa/beat_sheet/hum_probe → seo → doc → DỪNG
```
Trong lúc tts chạy, Chrome tạo ảnh làm tts chậm ~30% — vẫn nhanh hơn chạy tuần tự.

---

## Bước 0 — Đồng bộ, chọn đề tài, khởi tạo
1. Đọc bộ nhớ theo `AGENTS.md` (director_taste TASTE-45…64, lessons LESSON-60…81).
2. Con vật: lời chủ kênh, hoặc `next_teaser` tập trước, hoặc tập kế trong `config/series_roadmap.json`.
3. Slug `tap-<NN>-<ten-khong-dau>` → `pipeline.py init` (tự điền `format`, `persona`, `_angle_from_roadmap`, `_shorts_idea_from_roadmap`).
4. Thêm link tập vừa đăng vào `config/channel.json > previous_episodes` nếu thiếu.
5. Máy mới lần đầu: `python scripts/make_cast_refs.py` (clip cameo) — kiểm `assets/voice_refs/cast_*.wav` đã có thì bỏ qua.
6. **Nghiên cứu khán giả (TubeLab `comment-mining`, miễn phí, ~1-2 phút):**
   `python src/seo/episode_research.py projects/<slug> ideas --animal "<Tên>" --en "<English name>"`
   → `specs/research_ideas.md`: từ người Việt gõ tìm (autocomplete), câu hỏi + hiểu lầm trong bình luận video top.
   Dùng cho Bước 1: câu hỏi nhiều like → hook/nghịch lý; hiểu lầm → cú bẻ lái (kiểm chứng nguồn trước); câu chưa ai trả lời →
   `seo.question`. Có ⚠️ "người Việt gần như chưa tìm" → tiêu đề/thumbnail phải bán bằng **nghịch lý**, không bằng tên loài.
   Luôn truyền `--en` với loài hiếm (Tập 41 nhện lặn chuông: tiếng Việt 0 kết quả, tiếng Anh ra 8 video + bình luận).

## Bước 1 — Nghiên cứu & kịch bản (`episode.json`)
**Nghiên cứu (WebSearch, 6-8 sự thật có nguồn):** tìm bài báo khoa học/tổ chức uy tín cho từng con số. Ghi vào `"sources"`.
- Kiểm tra cả **huyền thoại phổ biến** của đề tài: Tập 9 "cánh cụt cố ý đẩy bạn xuống nước dò hải cẩu" là chuyện sách thiếu nhi,
  khoa học nói là chen lấn vô tình → biến chính điều đó thành **cú bẻ lái ở chương bào chữa** (vừa đúng khoa học vừa hay hơn).
- Cần: nghịch lý hook, 4-6 số liệu kỷ lục, cơ chế khoa học, 1 câu chuyện có thật (năm, nơi, tên người), teaser tập sau.
  **Teaser tập sau (TASTE-68 — chủ kênh chốt 09/11/2026):** TUYỆT ĐỐI KHÔNG đọc thẳng tên con vật tập sau!
  Vẽ con vật tiếp theo dưới dạng **BÓNG ĐEN BÍ ẨN (solid black silhouette / shadowed cutout)** kèm dấu hỏi chấm;
  lời đọc đưa ra 2-3 gợi ý gây sốc về siêu năng lực/nghịch lý và kêu gọi khán giả đoán tên con vật ở phần bình luận.

**Cấu trúc theo FORMAT** (`docs/strategy/FORMAT_KE_CHUYEN.md`) — số scene = số phần của format, mẫu F3 Tập 9:
`scene01 VỤ ÁN NAM CỰC (hook) → scene02-05 BẰNG CHỨNG #1-#4 → scene06 PHÁN QUYẾT (đổi vai luật sư, lật ngược, teaser)`.
Mỗi scene có: `badge` (≤ 16 ký tự, nhãn format), `banner_title` (≤ 32 ký tự, chữ trên banner AI), `chapter_title` (mục lục YouTube),
`hook` (phụ đề thẻ chương), `mood` mặc định, `parts`.

**Viết lời** theo humor-voice (persona, ≥ 1 chỗ cười / 20-30s, biệt danh ≥ 4 lần, punchline ≤ 8 từ):
- Part ≤ 1.300 ký tự; mỗi câu **vẽ được thành 1 hình** (ai, làm gì, đạo cụ nào).
- Part dạng `{"text", "mood"}` hoặc `{"text", "cast"}`; ≥ 3 mood, không mood > 50%; **2-6 cameo** (Tập 9: thẩm phán ×2, chú cánh cụt
  "mượn vĩnh viễn", nhân chứng 1911), mỗi cameo ≤ 2 câu, ngay sau là giọng chính phản ứng = chỗ cười.
- **Số đọc bằng chữ** ("ba mét rưỡi"), **mọi số có `display_fix`** ("ba mét rưỡi": "3,5m"). Chú ý chữ hoa đầu câu là KEY RIÊNG
  ("Âm bốn mươi độ C" và "âm bốn mươi độ C" — lỗi thật Tập 9). Năm: "một ngàn chín trăm mười một": "1911".
- Tên nước ngoài phiên âm + `display_fix` ("Lê-vích": "Levick", "I-gơ Nô-ben": "Ig Nobel").
- **Cụm từ dùng làm mốc beat phải duy nhất trong chương**: tránh lặp nguyên văn câu mở đầu ("Về bằng chứng số…" lặp 4 lần ở Tập 9
  → phải chọn cụm khác làm mốc). Viết lời đa dạng ngay từ đầu cho dễ.
- Thêm `nickname`, `sources`, `whisper_prompt` (tên riêng + phiên âm), `art` (đạo cụ banner, mascot Shorts, nội dung thumbnail), `seo`.
- Shorts tập lẻ **KỂ TRỌN VẸN** (TASTE-66; video tổng hợp/mega thì giữ Shorts phễu cũ — xem skill mega-compilation): 900-1.050 ký tự, 10-12 câu, mở bằng giọng format ("Bị cáo, mời đứng lên!").
  Khung 5 nhịp: hook nghịch lý → giới thiệu con vật (là gì, ở đâu) → 2-3 sự thật có số liệu → giải thích VÌ SAO → câu chốt
  trọn ý trả lời hook. KHÔNG "xem video dài/bấm vào kênh", KHÔNG câu hỏi bỏ lửng, KHÔNG câu cắt lửng nối vòng
  (chi tiết: `docs/strategy/FORMAT_KE_CHUYEN.md` mục 5). `seo.shorts_desc` cũng tóm trọn ý, link video dài chỉ là tùy chọn.
- **Tiếng Anh bắt buộc (TASTE-42, LESSON-86):** thêm `seo.en_title` (≤100 ký tự, dạng "Hook?! | Animal | Ep N"),
  `seo.en_hook` (2-3 câu), `seo.en_chapters` (1 dòng/chương, đúng thứ tự scenes), `seo.en_shorts_title`.
  `pipeline.py seo` đưa vào `upload.json`; `upload_youtube.cjs` tự thêm bản dịch tiếng Anh + màn hình kết thúc
  (video + playlist "Thế Giới Động Vật" + đăng ký). Shorts → "Video có liên quan": `link_shorts_related.cjs` (chỉ chạy được khi video dài đã công khai).
  Hashtag (TASTE-68): `pipeline.py seo` tự đặt 3 tag có dấu `#độngvật #<con vật> #VẽChuyệnHoangDã`, bỏ `| Tập N` và `#shorts` khỏi tiêu đề.

**Độ dài:** nhắm **≥ 10.000 ký tự lời** (không tính tag) cho format đa mood. `check` in ước lượng (đã hiệu chỉnh trên Tập 9:
17,6 ký tự/s ở tempo 1.0, tempo theo mood) — phải ≥ 8:45 (biên an toàn 15s vì OmniVoice dao động ±3%).

`python src/episode/pipeline.py check projects/<slug>` phải sạch: không `!! script:`, không `!! voice-diversity`, không `TOO SHORT`.

## Bước 2 — Giọng (`tts`, chạy nền)
- `pipeline.py tts` (block_until_ms 0, theo dõi bằng AwaitShell; ~7s CPU / 1s audio). Cache theo file `audio/vs/<scene>_p<i>.wav`.
- Thiếu thời lượng (`!! TOO SHORT`) → **viết thêm part** (sự thật vui có nguồn + punchline) ở chương 2-5, **không hạ tempo**:
  1. `python src/episode/voice_cache.py projects/<slug> snapshot` **trước khi sửa** episode.json
  2. chèn part mới (ở giữa chương cũng được) → `voice_cache.py remap` (đổi tên cache theo nội dung, chỉ part mới bị đọc lại)
  3. `pipeline.py tts` → 1-2 phút/part. Thêm beat + ảnh cho câu mới (Bước 3, dùng `"id"`).
- Shorts tự co tempo ≤ 53s; `aresample=48000` đứng đầu filter (đã khóa trong code).

## Bước 3 — Storyboard → plans + prompt (KHÔNG cần audio, làm song song với tts)
Viết `specs/storyboard.json` (mẫu: `examples/ep09_reference/storyboard.json`, khung: `templates/episode/storyboard.json`):
- `characters`: `HERO` (mô tả đầy đủ + **1 phụ kiện nhận dạng cố định**, vd nơ bướm đỏ — giúp Gemini giữ nhân vật qua 80+ ảnh và
  phân biệt với đồng loại), `HERO_S` (ngắn), `NO_HERO`, nhân vật phụ cố định (`JUDGE`…); `side_characters` vào prompt mở chat.
- `long`: mỗi câu/ý = 1 beat `{"scene", "at", "layout", "stickers", "impacts"}`; `at` = 3-5 chữ **dạng phụ đề** (số đã thành "3,5m"),
  beat đầu chương `0`. Nhắm 13-18 beat/chương (Tập 9: 87 beat cho 8:48 → trung bình 6s/ảnh).
- `layout`: chia vùng TRÁI/GIỮA/PHẢI; hình ảnh hóa con số bằng đạo cụ (thước dây, cân, nhiệt kế, đồng hồ đo); so sánh = chia đôi khung;
  cảnh không có nhân vật chính → `{NO_HERO}`; nhạy cảm (phân, săn mồi) → "phong cách hoạt hình hài thân thiện trẻ em, không máu".
- `stickers` (≤ 2/ảnh, chỉ số đắt giá): `at` = lúc số được đọc; `value` ≤ 10, `label` ≤ 22 ký tự; `side` L/R; `y` 300-560 (dài),
  L 540-1060 / R 520-780 (Shorts); **`target` [x,y] BẮT BUỘC** — đặt theo bố cục đã ra lệnh (TRÁI ≈ 0.25, GIỮA 0.5, PHẢI 0.75), đo lại ở Bước 6.
- `shorts`: 12-13 beat, 3-6s mỗi ảnh; beat cuối là cảnh con vật đúng câu kết (không mascot/CTA).
- **Chèn beat sau khi đã tạo ảnh** → thêm `"id": "L85"` (số mới, lớn hơn số cuối) để các ảnh cũ giữ đúng tên. Gộp/bỏ beat đã có ảnh
  → thêm số đó vào `skip_numbers`.

`python src/episode/build_plans.py projects/<slug>` — lỗi gì cũng báo ngay (cụm không tìm thấy, cụm trùng nhảy ngược, sticker thiếu
target, sticker đọc sau khi ảnh đã chuyển, ảnh trùng). Rồi `python src/episode/extra_prompts.py projects/<slug>`.

## Bước 4 — Ảnh Gemini (tự động, chạy nền)
1. Đóng mọi cửa sổ Chrome dùng profile `config/channel.json > chrome_profile`.
2. `node src/episode/gemini_gen.cjs projects/<slug> probe` → `signedIn: true` (false → mở Chrome profile đó, đăng nhập Google 1 lần).
3. Chạy nền lần lượt: `... long` (~30s/ảnh) → `... shorts` → `... extra`. Mỗi chat mới tự gửi lại quy chuẩn + nhân vật; 20 ảnh/chat.
4. Đọc cuối log `{"done":..., "missing":[...]}`. Ảnh lỗi `timeout` (~5%): chạy lại `--only L09,L23 --per-chat 1`.
   Vẫn timeout → viết lại `layout` ít "nhạy cảm"/đơn giản hơn trong storyboard → `build_plans` → chạy lại `--only`.
   3 lỗi liên tiếp (hết lượt) → `--account 1`.
5. `import_images.py --sheet` cứ sau mỗi đợt; **XEM** `renders/snapshots/sheet_long.jpg`, `sheet_shorts.jpg` và mở vài ảnh lớn:
   đúng nội dung câu? đúng nhân vật (phụ kiện)? không chữ? Sai → xóa `assets/long/Lxx.png` (+ `_raw/`) → `gemini_gen --only Lxx`.
6. Banner: `prep_banners.py <P> <P>/assets/_src` → `banner_sheet.py` → **đọc từng chữ tiếng Việt** (Gemini vẽ chữ). Sai dấu → xóa
   `assets/_src/Cxx.*` → `gemini_gen extra --only Cxx`.
7. Thumbnail: `import_images.py` đưa `T01` → `renders/<slug>_thumbnail.jpg`; mở xem chữ + bố cục TASTE-57.
   **Trước khi viết `art.thumb_title/thumb_scene/thumb_gag` (Bước 3b, TubeLab `thumbnail-concepts`):**
   `python src/seo/episode_research.py projects/<slug> thumbs` → MỞ XEM 3-5 ảnh ratio cao nhất trong `specs/research_thumbs/`,
   ghi 3 điểm chung (bố cục, khoảng cách chủ thể, màu, chữ, cảm xúc) vào cuối `specs/research_thumbs.md`, rồi ghép với nghịch lý
   riêng của tập. Giữ phong cách vẽ tay của kênh; không chép ảnh/chữ kênh khác.
8. Không có Chrome/Playwright (máy khác)? Dán từng prompt trong `specs/image_prompts.json` lên Gemini tay, lưu ảnh đúng tên vào
   `assets/inbox/` (png/jpg), `import_images.py` nhận hết.

## Bước 5 — Căn thời gian (`align`)
Whisper small, ~4 phút. Match **≥ 0.9** mỗi chương (Tập 9: 0.92-0.94). < 0.8 → nghe part đó, xóa `audio/vs/<part>.wav`, `tts` lại.
Kiểm: `long_words_fixed.json` không còn `[tag]`, không còn số dạng chữ (đã có `script_lint` chặn từ Bước 1).

## Bước 6 — Spec + kiểm tra trước render
1. `pipeline.py spec` → phải `spec OK`. Lỗi hay gặp:
   - `holds only 1.6s (<2s)` → gộp beat (chuyển sticker sang beat trước, đưa số ảnh vào `skip_numbers`).
   - `holds > 15s` → tách câu, thêm beat (`"id"` mới) + ảnh.
   - Shorts `holds > 7s` → tách câu, thêm ảnh (`"id": "S13"`).
   - `phrase not found` → cụm `at`/`impacts` không đúng chữ phụ đề; sửa storyboard → `build_plans`.
2. `python scripts/audit_beats.py projects/<slug>` — **đọc từng dòng**: lời đang nói ↔ ảnh, sticker đúng lúc, cuối `Image reuse: {}`.
3. `python src/episode/target_sheet.py projects/<slug>` — xem `renders/snapshots/targets_*.jpg`: vòng đỏ phải nằm **trên** chi tiết
   (nhiệt kế, thước, con vật…). Lệch → sửa `target` trong storyboard → `build_plans` → `spec`.

## Bước 7 — Render & QA
1. `pipeline.py render <P> --preview` (~1 phút) → xem `renders/long_v2/snapshots_long_v2/scene0X_sheet.jpg` + `renders/snapshots_shorts_v4/contact_sheet.png`.
2. `pipeline.py render <P> --force` (nền ~25 phút). **Luôn `--force`** sau mọi thay đổi ảnh/beat/giọng (LESSON-72).
3. `pipeline.py qa` → PASS (dài 8:30-11:00, -14±1,5 LUFS, TP ≤ -1; Shorts 40-59,5s; 0 đoạn đứng hình).
4. `scripts/beat_sheet.py` → xem `renders/beat_audit/scene0X.jpg`: banner chương, mũi tên, phụ đề số, không `[tag]`.
5. `scripts/hum_probe.py <P>/audio/shorts.wav <P>/renders/<slug>_shorts.mp4` → NOISE FLOOR < -40 dBFS.

## Bước 8 — SEO, tài liệu, nhật ký, báo cáo (DỪNG)
0. **Chốt tiêu đề (TubeLab `title-formulas`, ~1 phút):** `python src/seo/episode_research.py projects/<slug> titles`
   → `specs/research_titles.md`: tiêu đề video top về con vật, xếp theo ratio (lượt xem ÷ trung vị kênh đó), ✅ = khuôn đã thắng.
   Chọn 2-3 khuôn ✅ hợp nghịch lý của tập, viết lại bằng giọng kênh → `seo.title` (giữ đuôi `| Tập N`, TASTE-72);
   2 phương án còn lại → `seo.title_alternatives` (để chủ kênh A/B trong Studio). Có ⚠️ "tín hiệu mỏng" → dùng khuôn đã thắng
   của chính kênh (`python src/seo/channel_outliers.py`).
1. `pipeline.py seo` → mục lục chương đúng timestamp, `upload.json`, `seo_package.md`.
1b. `python src/seo/seo_research.py projects/<slug> --apply` → lấy gợi ý tìm kiếm thật của người Việt (YoutubeTags)
   + tag của video đối thủ top (yt-dlp), lọc giữ tag đúng con vật và có trong kịch bản, lấp ngân sách tag tới ~470/500
   (đếm kiểu YouTube Studio), chấm điểm SEO trước/sau (hybrid-youtube-growth-engine), ghi `specs/seo_research.md`,
   rồi tự chạy lại `pipeline.py seo`. Bỏ `--apply` để chỉ xem báo cáo. Chỉ sửa tag trong `episode.json` — không đụng tiêu đề/mô tả.
   **Soát tay danh sách tag thêm** trong `specs/seo_research.md` trước khi đăng: bộ lọc vẫn để lọt tag nấu ăn/bắt/nuôi
   hoặc tên phim (đợt 17/11 phải gỡ tay ~25 tag kiểu "cách chế biến cá mút đá", "nuôi bạch tuộc").
   Tập tổng hợp (mega): thêm `--cores "con vật 1,con vật 2,..."`; KHÔNG để `pipeline.py seo` ghi đè `upload.json` của mega
   (nó thay bộ hashtag riêng của mega) — chỉ thay `long.tags`.
   Shorts → "Video có liên quan": **tự động** — Task Scheduler `VeChuyenHoangDa_AutoLinkShorts` (17:20 & 20:20 mỗi ngày,
   tới 31/12/2026) chạy `python src/episode/auto_link_shorts.py`, gắn mọi tập có video dài đã công khai mà Shorts chưa gắn.
   Nhật ký `logs/auto_link_shorts.log`. Cần máy bật + đã đăng nhập Windows + không mở Chrome bằng profile kênh lúc đó.
   Video ĐÃ đăng/hẹn lịch: `node src/episode/update_tags.cjs projects/<slug> [--dry-run]` — giữ nguyên tag đang có trên
   Studio, chỉ thêm tag còn thiếu tới gần 500 ký tự, đọc lại sau khi lưu để xác minh. Không đụng tiêu đề/mô tả/lịch.
2. `python src/episode/episode_doc.py projects/<slug>` → `EPISODE_SPEC.md`.
3. `python src/memory/memory_harvester.py --log-video <slug> "<title>" <giây> "<bài học>"`; lỗi mới đã sửa → `--add-lesson`.
4. Báo cáo: đường dẫn 2 video + thumbnail, thời lượng, số ảnh, LUFS, tiêu đề, bình luận ghim. Hỏi giờ đăng → **dừng**.

## Bước 9 — Đăng (chỉ khi được lệnh)
Lịch chuẩn TASTE-68 (1 tập/ngày): **video dài 17:00 ngày D, Shorts 11:30 ngày D+1**. Ngày D của từng tập/mega nằm trong
**`docs/LICH_DANG_VIDEO.md`** → `python src/episode/publish_schedule.py --show <N|mega-NN>` in sẵn lệnh upload (giờ đã qua → báo chủ kênh).
Sau upload: `python src/episode/publish_schedule.py` để cập nhật docs.
Đóng Chrome profile → `node src/episode/upload_youtube.cjs projects/<slug> --date D --time 17:00 --shorts-date D+1 --shorts-time 11:30`
→ kiểm `upload_result.json` → chạy lại `--fix-only` xác minh ngày giờ (LESSON-75) → ghim bình luận → cập nhật `previous_episodes`
→ **sau 17:00 ngày D** (video dài đã công khai): `node src/episode/link_shorts_related.cjs projects/<slug>` gắn "Video có liên quan" (LESSON-91).

---

## Checklist "xong" (đánh dấu hết mới báo cáo)
- [ ] `check` sạch (script lint, voice diversity, ước lượng ≥ 8:45); `sources` có nguồn cho mọi số
- [ ] tts: LONG-FORM ≥ 8:30 thật; align match ≥ 0.9
- [ ] build_plans OK; `gemini_gen` missing = []; đã xem sheet_long/sheet_shorts/banners/thumbnail
- [ ] spec OK; audit_beats đọc hết + `Image reuse: {}`; target_sheet vòng đỏ đúng chi tiết
- [ ] render `--force`; qa PASS; beat_sheet đã xem; hum_probe < -40 dBFS
- [ ] **Chuẩn Đa Phong Cách từ Tập 32 (`TASTE-73`, `TASTE-74`, `TASTE-75`)**: Khai báo `art.visual_style`, `scenes[].banner_bar_style` (`C01..C06`), `scenes[].card_style` + `card_sub` (`K01..K06` bảng chuyển chương AI giữa màn hình -> `assets/banners/card_01..06.png`), `art.shorts_banner_style` (`B00`) và bộ hiệu ứng Sticker/Mũi tên/Tâm ngắm theo chủ đề trong `src/render/theme_effects.py`.
- [ ] `specs/research_ideas.md`, `research_thumbs.md` (có 3 điểm chung đã ghi), `research_titles.md` — đã dùng vào kịch bản/thumbnail/tiêu đề
- [ ] seo + EPISODE_SPEC.md + production_log; báo cáo và DỪNG

## Chuyển máy mới / AntiGravity
Toàn bộ ở **`SETUP_MAY_MOI.md`**. Tóm tắt:
1. `git clone https://github.com/hytruong-dev/wildlife-comic-studio.git` → `powershell -ExecutionPolicy Bypass -File scripts\setup_new_machine.ps1`
   (tự cài Python/Node/ffmpeg/Chrome, `requirements.txt` đã khóa phiên bản, `npm ci`, 8 repo `tools/` đúng commit, whisper `small`).
2. Tay, 1 lần: cài VoiceStudio 0.5.3 + tải model OmniVoice (mục 6); đăng nhập Google qua `gemini_gen.cjs ... probe` (mục 8).
3. Khác máy → ghi `config/local.json` (Chrome profile, đường dẫn VoiceStudio) — KHÔNG sửa `config/channel.json`.
4. Ảnh/giọng/video đã render không có trong git; tập đang dở thì chép tay `projects/<slug>/`.

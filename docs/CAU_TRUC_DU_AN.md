# CẤU TRÚC DỰ ÁN — "Vẽ Chuyện Hoang Dã" (cập nhật sau Tập 9)

> Bản đồ để AI bất kỳ (Cursor, AntiGravity, Claude, Codex) hiểu dự án trong 5 phút và làm tập mới **một lần là xong**.
> Quy trình: `.agents/skills/core/episode-production/SKILL.md` · Luật + lỗi: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md` · Mẫu: `examples/ep09_reference/`.

## 1. Đường đi của 1 tập (dữ liệu chảy qua file nào)

```
config/series_roadmap.json ──init──► projects/<slug>/episode.json   (kịch bản, mood/cast, display_fix, art, seo)
                                          │  pipeline.py check (lint + ước lượng thời lượng)
             ┌────────────────────────────┼─────────────────────────────────────────┐
             ▼                            ▼                                         ▼
   pipeline.py tts               specs/storyboard.json                     extra_prompts.py
   (VoiceStudio/OmniVoice)       build_plans.py                            specs/extra_prompts.json
   audio/vs/*.wav (cache)        ├ specs/longform_plan.json                       │
   audio/sceneXX.wav             ├ specs/shorts_plan.json                         │
   audio/shorts.wav              ├ specs/image_prompts.json ──► gemini_gen.cjs ◄──┘
             │                   └ specs/image_catalog.md        assets/inbox/*.txt, assets/_src/*.txt
             ▼                                                   import_images.py ─► assets/long|shorts/*.png, renders/<slug>_thumbnail.jpg
   pipeline.py align                                             prep_banners.py ─► assets/banners/chapter_NN.png, shorts_title.png
   audio/long_words_fixed.json, shorts_words.json
             └──────────────┬──────────────┘
                            ▼
             pipeline.py spec ─► specs/longform_spec.json, shorts_spec.json
             audit_beats.py · target_sheet.py · render --preview
                            ▼
             pipeline.py render --force ─► src/render/longform_v2_renderer.py ─► renders/<slug>_long.mp4 (intro + nội dung + outro)
                                       └► src/render/shorts_v4_renderer.py   ─► renders/<slug>_shorts.mp4
                            ▼
             pipeline.py qa · beat_sheet.py · hum_probe.py ─► pipeline.py seo ─► upload.json, seo_package.md
             episode_doc.py ─► EPISODE_SPEC.md                ⛔ DỪNG — chỉ đăng khi chủ kênh ra lệnh (upload_youtube.cjs)
```

## 2. Thư mục gốc

| Đường dẫn | Nội dung | Ai sửa |
|---|---|---|
| `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` | điểm vào cho AI (Cursor/Claude/AntiGravity) | khi đổi quy trình |
| `.agent/workflows/lam-tap-moi.md` | workflow ngắn cho AntiGravity | khi đổi quy trình |
| `.agents/skills/core/episode-production/` | **skill sản xuất 1 tập (Bước 0-9)** | khi đổi quy trình |
| `.agents/skills/core/humor-voice/` | skill viết kịch bản hài + giọng VoiceStudio | khi đổi văn phong/giọng |
| `.agents/skills/learned/` | kỹ năng đúc kết (bố cục, camera…) | `/retro` |
| `.agent_memory/` | `director_taste.md` (TASTE-xx), `lessons_learned.md` (LESSON-xx), `production_log.md` | `src/memory/memory_harvester.py` |
| `.cursor/mcp.json` | Playwright MCP (tùy chọn, profile Chrome của kênh) | — |
| `config/channel.json` | tên kênh, intro/outro/BGM, giọng (VoiceStudio path, tempo, min 510s), Chrome profile, link tập cũ | khi đổi máy / đăng tập mới |
| `config/series_roadmap.json` | lộ trình 61 tập: con vật, format F1-F7, persona, angle, ý Shorts | khi đổi lộ trình |
| `config/voice_personas.json` | 6 mood, 9 cameo, 8 persona, luật đa dạng giọng | hiếm |
| `docs/` | quy trình, format kể chuyện, hệ thống giọng, chiến lược kênh, file này | — |
| `examples/ep09_reference/` | **tập mẫu chuẩn vàng** (F3, đa mood, storyboard) | không sửa |
| `examples/ep06_reference/` | tập mẫu khung cũ 6 chương | không sửa |
| `templates/episode/` | `episode.json`, `storyboard.json` mẫu cho `init` | khi đổi định dạng |
| `assets/` | `branding/` (intro, outro, logo), `bgm/`, `sfx/`, `fonts/` (Mali, BeVietnamPro, PlaypenSans), `hands/`, `voice_refs/` (adam_*, cast_*) | hiếm |
| `projects/<slug>/` | 1 tập = 1 thư mục, mọi thứ của tập nằm trong đó (TASTE-18) | mỗi tập |
| `scripts/` | công cụ kiểm tra dùng chung (audit_beats, beat_sheet, hum_probe, voice_budget, grid_sheet, make_cast_refs…) + script cũ từng tập | — |
| `src/` | mã nguồn (bảng dưới) | — |
| `tools/`, `node_modules/` | 14 repo/thư viện bên thứ ba (hệ sinh thái cũ, xem AGENTS.md §4) | không dùng cho quy trình tập mới |

## 3. `src/episode/` — bộ công cụ sản xuất tập (dùng cho MỌI tập mới)

| File | Việc | Lệnh |
|---|---|---|
| `pipeline.py` | init · check (lint kịch bản, ước lượng thời lượng, đa dạng giọng) · tts · align · spec · render · qa · seo · status | `python src/episode/pipeline.py <stage> projects/<slug>` |
| `build_plans.py` | storyboard → 2 plan + prompt Gemini (chép lời nguyên văn) + catalog; chặn lỗi cụm/sticker/ảnh trùng | `python src/episode/build_plans.py <P>` |
| `extra_prompts.py` | prompt banner chương (theo format), banner Shorts, thumbnail từ `episode.json > art` | `python src/episode/extra_prompts.py <P>` |
| `gemini_gen.cjs` | tạo ảnh Gemini hàng loạt bằng Playwright + Chrome profile (không cần MCP), có cache, chống trùng | `node src/episode/gemini_gen.cjs <P> probe\|long\|shorts\|extra [--only] [--per-chat] [--account]` |
| `import_images.py` | inbox → assets (khử watermark Gemini nếu có), thumbnail jpg, bảng xem | `python src/episode/import_images.py <P> --sheet` |
| `prep_banners.py` | cắt nền banner AI (tự giải mã .txt) → `assets/banners/` | `python src/episode/prep_banners.py <P> <P>/assets/_src` |
| `banner_sheet.py` | bảng xem banner để đọc chính tả | `python src/episode/banner_sheet.py <P>` |
| `target_sheet.py` | vẽ điểm target sticker lên ảnh gốc | `python src/episode/target_sheet.py <P>` |
| `voice_cache.py` | giữ cache giọng khi chèn/xóa part | `python src/episode/voice_cache.py <P> snapshot\|remap` |
| `episode_doc.py` | sinh `EPISODE_SPEC.md` | `python src/episode/episode_doc.py <P>` |
| `upload_youtube.cjs` | đăng + lên lịch YouTube (**chỉ khi được lệnh**) | `node src/episode/upload_youtube.cjs <P> --date … --time …` |

### `src/mega/` — video tổng hợp 60-80 phút (`docs/strategy/MEGA_COMPILATION.md`, skill `mega-compilation`)
| File | Việc |
|---|---|
| `transcribe_sources.py` | Whisper từng từ cho video đã đăng của 10 tập → `sources/<slug>.words.json` |
| `silences.py` | khoảng lặng giọng → `sources/<slug>.silences.json` (+ báo lỗ transcript) |
| `show_transcript.py` / `probe_range.py` / `part_map.py` | đọc lời, mốc từng chữ, nghe lại 1 đoạn, mốc từng part (tập 7+) để chọn `keep` |
| `assemble.py` | `check [--snap]` (luật biên tập, từ cấm, độ dài) · `plan` · `build` (cắt + cầu nối + intro/outro → `<slug>_mega.mp4`) · `seo` (chapters thật, mid-roll) · `qa` |
Dự án Mega = `projects/mega-NN-<ten>/` với `mega.json` (nguồn + timeline) và `episode.json` có `"mega": 1` (chỉ lời cầu nối).

Mã khác được pipeline gọi: `src/audio/omnivoice_tts.py` (VoiceStudio), `src/render/longform_v2_renderer.py`, `src/render/shorts_v4_renderer.py`,
`src/qa/retention_audit.py`, `src/pipeline/asset_sanitizer.py` (khử watermark), `src/memory/memory_harvester.py`.
Các thư mục `src/engine`, `src/compiler`, `src/composition`, `src/cli`, `src/hub`, `src/image_gen`, `src/studio`, `src/seo` là hệ cũ
(Tập 1-5, whiteboard-director) — **không dùng cho tập mới**.

## 4. `projects/<slug>/` — 1 tập

| Đường dẫn | Tạo bởi | Ghi chú |
|---|---|---|
| `episode.json` | AI viết | nguồn sự thật nội dung + SEO |
| `specs/storyboard.json` | AI viết | nguồn sự thật phân cảnh/ảnh |
| `specs/longform_plan.json`, `shorts_plan.json`, `image_prompts.json`, `image_catalog.md` | `build_plans.py` | không sửa tay |
| `specs/extra_prompts.json` | `extra_prompts.py` | có thể sửa tay 1 prompt nếu Gemini vẽ sai |
| `specs/longform_spec.json`, `shorts_spec.json` | `pipeline.py spec` | renderer đọc |
| `audio/vs/<scene>_p<i>.wav`, `shorts.wav`, `_cache_index.json` | `tts`, `voice_cache.py` | cache giọng thô — xóa 1 file để đọc lại 1 part |
| `audio/sceneXX.wav`, `sceneXX_parts_duration.json`, `shorts.wav` | `tts` | giọng đã tempo, 48 kHz |
| `audio/long_words_fixed.json`, `shorts_words.json` | `align` | mốc thời gian từng chữ (chữ kịch bản, số đã hiện số) |
| `assets/inbox/` | `gemini_gen.cjs` | `.txt` dataURL + `_gen_log.jsonl` |
| `assets/long/`, `assets/shorts/` (+ `_raw/`) | `import_images.py` | ảnh dùng render |
| `assets/_src/`, `assets/banners/` | `gemini_gen extra`, `prep_banners.py` | banner thô / đã cắt nền |
| `renders/<slug>_long.mp4`, `_shorts.mp4`, `_thumbnail.jpg` | render / import | sản phẩm |
| `renders/long_v2/sceneXX.mkv` | render | cache — đổi gì cũng `--force` |
| `renders/snapshots/` | sheet_long/shorts, banners, targets_*.jpg | kiểm tra bằng mắt |
| `renders/beat_audit/`, `renders/audit_beats.txt` | beat_sheet / audit_beats | kiểm tra bằng mắt |
| `seo_package.md`, `upload.json` | `seo` | gói đăng |
| `EPISODE_SPEC.md` | `episode_doc.py` | tài liệu đầy đủ của tập |
| `scripts/` | tùy tập | chỉ script riêng của tập; công cụ chung để ở `src/episode/` |

## 5. Phụ thuộc bên ngoài

| Thứ | Dùng cho | Kiểm tra |
|---|---|---|
| VoiceStudio (OmniVoice) — `config/channel.json > voice.voicestudio_python` | giọng đọc cục bộ | `pipeline.py check` → "VoiceStudio OK" |
| Python 3.11+ (`requirements.txt`: faster-whisper, opencv, pillow, numpy, soundfile…) | pipeline, render | `python --version` |
| Node 20+ + `playwright` (npm) + Google Chrome | gemini_gen, upload | `node src/episode/gemini_gen.cjs <P> probe` |
| ffmpeg/ffprobe trong PATH | mọi bước âm thanh/video | `ffmpeg -version` |
| Tài khoản Google đã đăng nhập trong Chrome profile của kênh | Gemini + YouTube Studio | `probe` → signedIn true |
| Playwright MCP (tùy chọn) — `.cursor/mcp.json` | thao tác trình duyệt tay trong Cursor | Cursor Settings → MCP |

# MEGA COMPILATION — cứ 10 tập lẻ ra 1 video tổng hợp 60-80 phút

> Bản chuẩn hóa (dùng cho pipeline) của **PHẦN 2** trong cẩm nang chủ kênh `docs/strategy/CAM_NANG_V5_MEGA_COMPILATION_GOC.md`.
> Skill thực thi: `.agents/skills/core/mega-compilation/SKILL.md`. Mẫu đã làm xong phần lõi: `projects/mega-01-bang-phong-than/`.

## 0. ⚠️ CẬP NHẬT 21/11/2026 — MỖI MEGA LÀ MỘT PHONG CÁCH ĐỘC BẢN (TASTE-76)
Chủ kênh chốt:
1. **Nội dung mới hoàn toàn (09/11/2026 — TASTE-67)**: Tập đặc biệt sau mỗi 10 tập = **10 con vật cũ gặp lại nhau trong một khung chuyện mới, 100% sự thật mới có nguồn, không lặp tập lẻ**, render như tập thường (không `assemble.py`).
2. **Đa dạng hóa tuyệt đối giữa các phần Mega (21/11/2026 — TASTE-76)**: *"Mỗi phần Mega là một phong cách khác nhau, không giống nhau từ nội dung đến lời thoại."*
   - **TUYỆT ĐỐI KHÔNG** lặp lại khung "Đại Hội Sinh Tồn" hay cùng một kiểu dẫn chuyện MC/bảng điểm giữa các phần Mega (Mega 01–03 là kỷ nguyên cũ; từ **Mega 04 trở đi** mỗi phần phải có một thể loại, cốt truyện, persona giọng đọc, ngôn ngữ lời thoại, mỹ thuật vẽ tranh và bộ banner/HUD hoàn toàn riêng biệt).
   - Chi tiết lộ trình từng Mega đọc tại **`config/mega_roadmap.json`**:
     - **Mega 04 (Tập 31-40)**: *Phi Vụ Thế Kỷ: Biệt Đội Đặc Nhiệm Sinh Học* — Thể loại Điệp viên hài kịch đen (*Ocean's Eleven* x *Kingsman*), 7 Cửa Ải Đột Nhập, persona Chỉ Huy Mật Vụ, mỹ thuật *Retro Spy-Fi 1960s Classified Dossier*.
     - **Mega 05 (Tập 41-50)**: *Phòng Cấp Cứu Tạo Hóa: Ca Trực Đêm Kinh Hoàng* — Thể loại Y khoa hài châm biếm (*House M.D.* x *Scrubs*), 6 Khoa Hội Chẩn, persona Bác Sĩ Trưởng Khoa, mỹ thuật *Vintage Anatomical Atlas 1950s*.
     - **Mega 06 (Tập 51-60)**: *Chuyến Tàu Tốc Hành Xuyên Đêm: 10 Toa Bí Ẩn* — Thể loại Trinh thám cổ điển (*Orient Express* x *Knives Out*), 7 Toa Thẩm Vấn & Phá Án, persona Thám Tử Cổ Điển, mỹ thuật *Art Deco Noir 1930s*.
- Viết ở `content/*.md` (DSL "lời :: bố cục || sticker") → `python src/mega/build_from_content.py P` sinh `episode.json` + `specs/storyboard.json`.
- Công cụ phụ: `src/mega/suggest_display_fix.py` (số đọc bằng chữ thiếu display_fix), `src/mega/overlap_check.py` (cụm trùng transcript tập lẻ).
- `meta.json`: `special`, `series_label`, `next_label`, `voice.min_long_s = 3600`, `art` (style_label + banner/card theme độc bản theo `config/mega_roadmap.json`); KHÔNG đặt `"mega": 1` (chỉ cho kiểu cắt ghép).
- Kiểu cắt ghép (§2-§6 dưới đây, `projects/mega-01-bang-phong-than/`) chỉ dùng khi chủ kênh yêu cầu rõ.

## 1. Vì sao làm
- **Giờ xem:** 1 video 70 phút, 1.000 người xem trung bình 30 phút = 500 giờ xem (mục tiêu 4.000 giờ bật kiếm tiền).
- **Mid-roll:** video > 60 phút đặt được 8-12 điểm quảng cáo giữa video → RPM gấp 2,5-3 lần video 8 phút.
- **Session watch time:** người mới vào kênh ở tập 10 ngại tìm từng tập cũ, nhưng bấm ngay vào "Trọn bộ 10 quái kiệt".

## 2. 4 luật biên tập BẮT BUỘC (chống "nội dung trùng lặp" + chống bỏ xem)
| # | Luật | Thực thi trong code |
|---|---|---|
| 1 | **Chỉ 1 intro kênh ở 00:00 và 1 outro ở cuối.** Mỗi tập lẻ chỉ lấy **phần thân**: bỏ intro kênh, câu "Ở tập trước…", bài học sáo rỗng, câu hỏi bình luận, teaser tập sau, kêu gọi đăng ký, chữ ký kênh khác lọt vào cuối file cũ | `assemble.py check`: timeline phải mở bằng `intro`, đóng bằng `outro`; quét **từ cấm** (`tập trước`, `tập sau`, `đăng ký`, `chuông`, `bình luận`, `hành trình khám phá`, `phút thứ`…) trong mọi đoạn giữ lại; cảnh báo in-point < 9,5s |
| 2 | **Không xếp theo thứ tự đăng (Tập 1→10).** Đóng gói thành **bảng xếp hạng đếm ngược** (Tier List) — mở bằng con vật gây tò mò, kết bằng ngôi vương | `check` báo lỗi nếu thứ tự = thứ tự đăng |
| 3 | **1 mở đầu mới (~45s) + cầu nối giữa MỌI cặp con vật (12-25s)**: bàn tay gắn huy hiệu con vừa xem lên **Bảng Phong Thần** rồi gọi tên ứng cử viên kế tiếp. Thêm 1 cảnh kết (bảng hoàn chỉnh + câu hỏi bình luận + teaser đại hội sau) | `check` báo lỗi nếu 2 thân tập dính liền không có cầu nối |
| 4 | **Chapters trong mô tả** — 1 chương/con vật, mốc lấy từ bản dựng thật | `assemble.py seo` (sau `build`) sinh mục lục + gợi ý điểm mid-roll |

Thêm (kinh nghiệm khi làm Mega #01):
- **Cắt trong khoảng lặng giọng, không bao giờ giữa chữ**: `assemble.py check --snap` kéo mọi mốc vào khoảng lặng gần nhất (`silences.py`).
- **Mỗi lần cắt có fade trắng 0,2s** (như lật trang bảng trắng) — che được cảnh bàn tay đang vẽ dở.
- **Cắt cả đoạn phụ trong thân** nếu bị lặp ý hoặc lộ cấu trúc ("vào phút thứ 4", "Ở tập trước") — `keep` cho phép nhiều đoạn.
- Tổng **60-80 phút** (`target_min` trong `mega.json`). Thừa → cắt đoạn bài học/đoạn phụ trước; thiếu → không kéo lời cầu nối, giữ thêm thân.
- Tập lẻ cũ có chất lượng khác nhau (Tập 1-5: 1280×720@24; Tập 6+: 1920×1080@30) → `build` chuẩn hóa tất cả về 1920×1080@30, -14 LUFS.

## 3. Cấu trúc dữ liệu (1 dự án Mega = 1 thư mục `projects/mega-NN-<ten>/`)
```
mega.json              nguồn + timeline cắt ghép (do AI viết, xem §4)
episode.json           LỜI MỚI: scene01 mở đầu, scene02..N cầu nối, scene cuối kết + Shorts tổng hợp + seo  ("mega": 1)
specs/storyboard.json  ảnh cho lời mới (mỗi câu 1 ảnh) + Shorts
sources/<slug>.words.json     transcript Whisper từng từ của video ĐÃ ĐĂNG (transcribe_sources.py)
sources/<slug>.silences.json  khoảng lặng giọng (silences.py)
renders/long_v2/sceneXX.mkv   cầu nối đã render (pipeline.py render --long)
renders/mega_parts/           từng đoạn đã cắt/chuẩn hóa (cache)
renders/<slug>_mega.mp4       VIDEO DÀI CUỐI CÙNG   ·   renders/<slug>_shorts.mp4   Shorts tổng hợp
renders/mega_timeline.json    thời lượng thật từng đoạn → chapters
```
`episode.json` của Mega dùng **đúng định dạng tập thường** nên mọi công cụ cũ chạy được: `pipeline.py check/tts/align/spec/render`,
`build_plans.py`, `extra_prompts.py`, `gemini_gen.cjs`, `import_images.py`, `prep_banners.py`. Khác biệt duy nhất: `"mega": 1`
(tắt luật "≥ 8:30" vì thời lượng tính trên cả video ghép), `format: "F_SPECIAL"`, `persona: "giai_dau"` (MC đại hội),
`art.thumb_badge` (vd "TRỌN BỘ 10 TẬP" hoặc "TẬP ĐẶC BIỆT"), `seo.title` KHÔNG ghi số phút (TASTE-70: YouTube đã hiện thời gian trên thumbnail, ghi vào tiêu đề sẽ làm tốn chỗ và bị cắt cụt ba chấm `...`).

## 4. `mega.json`
```json
{"mega_no": 1, "target_min": [60, 80], "publish_note": "...",
 "sources": [{"ep": 7, "slug": "tap-07-tom-tit", "animal": "Tôm Tít", "file": "projects/tap-07-tom-tit/renders/tap-07-tom-tit_long.mp4",
              "whisper_prompt": "tên riêng..."}],
 "timeline": [
  {"type": "intro"},
  {"type": "bridge", "scene": "scene01", "chapter": "Mở đầu: ..."},
  {"type": "source", "slug": "tap-10-gau-koala", "chapter": "Hạng 10 — ...", "_cut": "ghi chú bỏ gì", "keep": [[10.4, 510.6]]},
  {"type": "bridge", "scene": "scene02", "chapter": "Hạng 9 — ..."},   ← chapter của con vật đặt ở CẦU NỐI giới thiệu nó
  ...
  {"type": "outro"}]}
```
- `file` = **video đã đăng** (có intro/outro gốc). Tìm đúng file: `upload_result.json`/`specs/youtube_publish_metadata.json` của tập.
- `keep` = danh sách `[giây vào, giây ra]` trên video nguồn. Với tập làm bằng pipeline (Tập 7+): intro = 10,03s, mốc từng part
  lấy bằng `python src/mega/part_map.py projects/<tập>` (cắt theo ranh giới part = sạch nhất).
- Chương của con vật bắt đầu ở **cầu nối gọi tên nó** (người xem bấm mục lục nghe luôn lời giới thiệu).

## 5. Chuỗi lệnh (P = projects/mega-NN-ten)
| Bước | Lệnh | Ghi chú |
|---|---|---|
| 1 | viết `P/mega.json > sources` → `python src/mega/transcribe_sources.py P` | nền, ~5 phút/tập (CPU) |
| 2 | `python src/mega/silences.py P` | báo "transcript holes" > 8s → `python src/mega/probe_range.py <mp4> a b` nghe lại |
| 3 | đọc transcript: `python src/mega/show_transcript.py P <slug> --all` · mốc từng chữ: `show_transcript.py P slug@giây slug@giây` · tập 7+: `part_map.py` | chọn `keep` |
| 4 | viết `timeline` → `python src/mega/assemble.py check P --snap` → `plan` | sửa tới khi `CHECK OK`, tổng 60-80' |
| 5 | viết `P/episode.json` (lời mới) → `python src/episode/pipeline.py check P` | sạch `!!` |
| 6 | viết `P/specs/storyboard.json` → `build_plans.py P` → `extra_prompts.py P` | |
| 7 | **ảnh**: `node src/episode/gemini_gen.cjs P probe/long/shorts/extra` → `import_images.py P --sheet` → `prep_banners.py P P/assets/_src` | xem ảnh |
| 8 | **giọng**: nền `pipeline.py tts P` → `pipeline.py align P` → `pipeline.py spec P` | |
| 9 | **render cầu nối**: `pipeline.py render P --preview` → nền `pipeline.py render P --force --long` | ra `renders/long_v2/scene*.mkv` (file `_long.mp4` phụ chỉ là các cầu nối ghép lại, không dùng) |
| 10 | **Shorts**: `pipeline.py render P --shorts` | `renders/<slug>_shorts.mp4` |
| 11 | **ghép**: nền `python src/mega/assemble.py build P` (~20-40 phút, encode lại 70 phút) | `renders/<slug>_mega.mp4` |
| 12 | `assemble.py qa P` · `assemble.py seo P` · `episode_doc.py P` (nếu cần) | ⛔ DỪNG, chờ lệnh đăng |

Đăng (chỉ khi được lệnh): `node src/episode/upload_youtube.cjs P --date … --time …` (đọc `upload.json` do `assemble.py seo` sinh).

## 6. Lời cầu nối — cách viết (persona `giai_dau`, MC đại hội)
- Mỗi cầu nối 2-3 part, 12-25s: **(a) chốt con vừa xem** bằng 1 câu tóm tắt hài nhất của tập đó + "nhận huy hiệu …" →
  **(b) câu chuyển tầng** (khi đổi tầng: "đèn tắt dần… tầng Tội Phạm") → **(c) gọi tên ứng cử viên kế** bằng 2-3 sự thật gây tò mò
  rồi tên con vật ở cuối câu (= punchline). Có 2-4 cameo cả bài (bệnh nhân Koala hỏi ngơ ngác, thẩm phán, phát thanh viên báo động).
- **Chỉ dùng sự thật ĐÃ CÓ trong tập lẻ** (đã kiểm chứng). Không thêm số liệu mới, không chép lại nguyên câu hook của thân tập ngay sau đó
  (luật "1 chi tiết chỉ bung 1 lần": cầu nối nói *tóm tắt/hé lộ*, thân tập kể *chi tiết*).
- Mọi số đọc bằng chữ + `display_fix`; `pipeline.py check` lint như tập thường.
- Ảnh: nhân vật chính = **Bảng Phong Thần** (4 hàng màu + biểu tượng, KHÔNG chữ) xuất hiện lại ở mỗi cầu nối, đầy dần qua từng cầu nối
  (mạch liên tục). Ngoại hình 10 con vật chép từ storyboard/prompt tập gốc (giữ phụ kiện nhận dạng: nơ đỏ cánh cụt, áo bệnh nhân Koala).

## 7. Lộ trình 6 Mega Đa Phong Cách (TASTE-76 — chi tiết tại `config/mega_roadmap.json`)
| Mega | Gộp | Thể loại & Khung chuyện độc bản | Persona & Lời thoại | Mỹ thuật (Art Style) | Trạng thái |
|---|---|---|---|---|---|
| #01 | Tập 1-10 | Đại Hội Sinh Tồn #1 (Giải đấu thể thao — Legacy) | MC Đại Hội + Giám khảo Cú Mèo | Whiteboard Comic 2D | ✅ Đã đăng |
| #02 | Tập 11-20 | Đại Hội Sinh Tồn Mùa 2 (Giải đấu — Legacy) | MC Đại Hội | Whiteboard Comic 2D | ✅ Đã đăng |
| #03 | Tập 21-30 | Đại Hội Sinh Tồn Mùa 3 (Giải đấu — Legacy) | MC Đại Hội | Whiteboard Comic 2D | ⏰ Đã hẹn giờ (28/11) |
| **#04** | **Tập 31-40** | **Phi Vụ Thế Kỷ: Biệt Đội Đặc Nhiệm Sinh Học** (Điệp viên 7 Cửa Ải) | Chỉ Huy Trưởng Mật Vụ (Spy-Fi hài kịch đen) | Retro Spy-Fi 1960s Graphic Novel | 📝 Kế hoạch mới |
| **#05** | **Tập 41-50** | **Phòng Cấp Cứu Tạo Hóa: Ca Trực Đêm Kinh Hoàng** (Y khoa 6 Khoa Hội Chẩn) | Bác Sĩ Trưởng Khoa châm biếm (*House M.D.*) | Vintage Anatomical Atlas 1950s | 📝 Kế hoạch mới |
| **#06** | **Tập 51-60** | **Chuyến Tàu Tốc Hành Xuyên Đêm: 10 Toa Bí Ẩn** (Trinh thám phá án) | Thám Tử Cổ Điển lịch lãm (*Poirot*) | Art Deco Noir 1930s | 📝 Kế hoạch mới |
Lưu ý: cẩm nang gốc ghi Tập 8 = Koala, Tập 10 = Gấu Trúc — **thực tế Tập 8 = Chồn Gulo, Tập 10 = Koala** (`config/series_roadmap.json`).
Mega #01 vì vậy có Chồn Gulo (Hạng A, hạng 4) thay cho Gấu Trúc; Gấu Trúc (Tập 11) thuộc Mega #02.
Mỗi Mega đổi **chủ đề đóng gói + kiểu bảng** (Tier List / triển lãm vũ khí / hồ sơ dị nhân…) để không lặp mô-típ giữa các Mega.
Lịch: đăng 20:00 cùng ngày tập lẻ thứ 10 của nhóm (cẩm nang), kèm 1 Shorts tổng hợp — chỉ khi chủ kênh ra lệnh.

**Shorts tổng hợp GIỮ KIỂU PHỄU CŨ** (TASTE-33/49, chủ kênh chốt 09/11/2026 — khác tập lẻ dùng Shorts kể trọn vẹn TASTE-66):
hook nghịch lý → leo thang sự thật mỗi 3-5s → bỏ lửng kết cục (ai vô địch?) + kêu xem video dài → câu cuối nối vòng về câu đầu.

---
name: mega-compilation
description: Sản xuất TẬP ĐẶC BIỆT 60-80 phút sau mỗi 10 tập lẻ cho kênh Vẽ Chuyện Hoang Dã. MẶC ĐỊNH (chủ kênh chốt 09/11/2026) = NỘI DUNG MỚI HOÀN TOÀN — 10 con vật của 10 tập gặp lại nhau trong một khung chuyện mới (vd Đại Hội Sinh Tồn), 100% sự thật mới đã kiểm chứng, không cắt ghép tập cũ. Kiểu cũ "cắt thân 10 tập + cầu nối" chỉ làm khi chủ kênh yêu cầu rõ. Dùng khi chủ kênh nói "làm mega", "làm tập tổng hợp", "tập đặc biệt", "trọn bộ 10 tập", "tổng hợp tập X-Y". DỪNG trước khi đăng.
---

# Tập đặc biệt 60-80 phút — quy trình thực thi

⛔ Không tự đăng/lên lịch YouTube. Đọc: `docs/strategy/MEGA_COMPILATION.md` (luật), mẫu chuẩn **`projects/mega-01-dai-hoi-sinh-ton/`**
(Đại Hội Sinh Tồn #1 — 14 chương, ~70.700 ký tự, ~60:35, 471 ảnh). Giọng/ảnh/render = bộ công cụ tập thường
(`.agents/skills/core/episode-production/SKILL.md`, `humor-voice`).

## 0. Chọn kiểu (hỏi nếu chủ kênh chưa nói)
| Kiểu | Khi nào | Công cụ |
|---|---|---|
| **A. Nội dung mới hoàn toàn (MẶC ĐỊNH)** | Chủ kênh 09/11/2026: "làm nội dung dài tập này mới hoàn toàn… không phải lấy 10 video ghép chèn" | `content/*.md` → `src/mega/build_from_content.py` → render như tập thường |
| B. Cắt ghép thân 10 tập + cầu nối | Chỉ khi chủ kênh yêu cầu rõ "ghép lại các tập" | `mega.json` + `src/mega/assemble.py` (mẫu `projects/mega-01-bang-phong-than/`) |

## KIỂU A — Phần 1: LÕI NỘI DUNG (AI chính làm — BẮT BUỘC THEO TASTE-76)
1. **Đọc `config/mega_roadmap.json` trước khi viết — MỖI MEGA MỘT THỂ LOẠI & LỜI THOẠI ĐỘC BẢN (TASTE-76)**:
   - **TUYỆT ĐỐI KHÔNG** lặp lại mô-típ "Đại Hội Sinh Tồn", MC bình luận hay bảng điểm giữa các phần Mega.
   - Áp dụng đúng 5 trục đổi mới của Mega tương ứng trong `config/mega_roadmap.json`:
     - **Khung chuyện & Cấu trúc chương riêng**: vd Mega 04 = *Phi Vụ Điệp Viên 7 Cửa Ải Đột Nhập* (không chấm điểm), Mega 05 = *Phòng Cấp Cứu Tạo Hóa 6 Khoa Hội Chẩn*, Mega 06 = *Chuyến Tàu Tốc Hành Xuyên Đêm 7 Toa Thẩm Vấn & Phá Án*.
     - **Persona dẫn chuyện & Lời thoại riêng**: đổi hoàn toàn giọng văn, từ vựng chuyên ngành, nhịp nói và gu hài (Chỉ huy mật vụ Spy-Fi hài kịch đen, Bác sĩ trưởng khoa châm biếm kiểu *House M.D.*, Thám tử cổ điển lịch lãm kiểu *Poirot*...).
     - **Tương tác chéo giữa 10 loài vật (Cross-animal chemistry)**: 10 con vật phải tương tác, cà khịa, phối hợp hoặc gây rắc rối cho nhau xuyên suốt phim qua cameo giọng đọc đa nhân vật (`@cast`).
     - **Mỹ thuật vẽ tranh & Banner/Card/HUD độc bản (TASTE-73/74/75)**: khai báo `art.style_label`, `art.banner_theme`, `art.card_theme` riêng cho từng Mega trong `meta.json` (tuyệt đối KHÔNG dùng "comic 2D whiteboard").
     - **12-14 chương (~60-75 phút)**: mở màn nhập vai thế giới mới → 6-7 chương trọng tâm (xen 2-3 chương hậu trường/tương tác nhẹ nhịp) → chương cao trào cú Twist bất ngờ có lý → kết thúc & hé lộ phần sau.
2. **Nghiên cứu sự thật MỚI**: mỗi chương 1 chủ đề chuyên sâu phù hợp khung chuyện. Mỗi sự thật phải có nguồn nghiên cứu (ghi vào `meta.json > sources`).
3. **Chống lặp tập cũ (bắt buộc)**: transcript 10 tập gốc (tập mới: `python src/mega/transcribe_sources.py`). Dò từ khóa từng sự thật trước khi viết; viết xong chạy
   `python src/mega/overlap_check.py P --sources <thư mục transcript> --n 5` và soi mọi cụm mang SỰ KIỆN (số, địa danh, nghiên cứu).
   Sự thật đã kể ở tập lẻ thì bỏ, hoặc chỉ nhắc 1 câu kiểu "khán giả đã biết… nhưng phần ít ai kể là…" rồi đưa chi tiết MỚI.
4. **Viết `P/content/`** (DSL "lời :: bố cục"):
   - `meta.json` (khóa của `episode.json` trừ `longform/shorts`: `special`, `series_label`, `next_label`, `format F_SPECIAL`,
     `persona` theo `config/mega_roadmap.json`, `voice.min_long_s` = 3600, `display_fix`, `sources`, `art` có `style_label` độc bản, `seo` với `{MINUTES}`). **KHÔNG** đặt `"mega": 1` (khóa này chỉ cho Kiểu B).
   - `characters.json`: `HERO` (MC), `JUDGE`, `BOARD`, `NO_HERO`, 10 con vật — ngoại hình + phụ kiện chép từ tập gốc.
   - `s01.md … sNN.md`: dòng 1 `# sceneNN | BADGE | Tiêu đề banner | Tiêu đề chương | HOOK | mood=…`; `@ <mood>` hoặc
     `@cast <vai>` mở part; mỗi dòng = 1 ảnh: `lời :: mô tả ảnh {KEY} … || mốc;L/R;rộng;GIÁ TRỊ ≤10;nhãn ≤22;x,y`.
   - `shorts.md`: `## Dòng 1 | Dòng 2`, 9-10 ảnh, ~950 ký tự — **GIỮ KIỂU PHỄU CŨ** (TASTE-33/49, chủ kênh chốt 09/11/2026):
     hook nghịch lý → leo thang sự thật → bỏ lửng kết cục + kêu xem video dài → câu cuối nối vòng về câu đầu.
     (Khác tập lẻ: tập lẻ dùng Shorts kể trọn vẹn TASTE-66. `pipeline.py check` không bắt lỗi phễu cho mega.)
5. Số đọc bằng chữ + `display_fix` (gợi ý thiếu: `python src/mega/suggest_display_fix.py P`); tên nước ngoài phiên âm + `display_fix`.
6. Sinh và kiểm: `python src/mega/build_from_content.py P` (mỗi ảnh 2,2-14,5s) → `python src/episode/build_plans.py P` →
   `python src/episode/extra_prompts.py P` → `python src/episode/pipeline.py check P` **sạch `!!`**, ≥ 60:00 + 15s biên,
   không mood nào > 50%, tempo TB ≥ 1.10. Kiểm lại cộng điểm qua từng vòng (bảng điểm đọc trong lời phải khớp).
7. ⛔ Dừng, báo chủ kênh (số chương, thời lượng, số ảnh, bảng điểm, nguồn) trước khi tạo ảnh.

## KIỂU A — Phần 2: SẢN XUẤT (Gemini/Cursor, giống tập thường)
| # | Lệnh | Xong khi |
|---|---|---|
| P1 | `node src/episode/gemini_gen.cjs P probe` → `long`, `shorts`, `extra` (nền; thiếu: `--only L07,L09 --per-chat 1`; hết lượt: `--account 1`) | `assets/inbox/` đủ L01-Lnnn, S01-S10; banner + B00 + T01 |
| P2 | `import_images.py P --sheet` · `prep_banners.py P P/assets/_src` · `banner_sheet.py P` | MỞ XEM sheet: đúng con vật/phụ kiện, không chữ trong ảnh, banner đúng chính tả |
| P3 | nền `pipeline.py tts P` (~2-3 giờ với 70k ký tự) → `pipeline.py align P` | match mỗi scene ≥ 0.8; dòng LONG-FORM ≥ 60:00 |
| P4 | `pipeline.py spec P` → `target_sheet.py P` → `pipeline.py render P --preview` | `spec OK`, sticker đúng chỗ |
| P5 | nền `pipeline.py render P --force` | `renders/<slug>_long.mp4` + `_shorts.mp4` + thumbnail |
| P6 | `pipeline.py qa P` → `pipeline.py seo P` → `episode_doc.py P` | QA PASS; `upload.json`, `seo_package.md`, `EPISODE_SPEC.md` — ⛔ DỪNG |

## KIỂU B (chỉ khi được yêu cầu) — cắt ghép
Giữ nguyên quy trình cũ: `mega.json > sources/keep/timeline`, `transcribe_sources.py` → `silences.py` → `show_transcript.py` /
`part_map.py` / `probe_range.py` → `assemble.py check --snap` → lời cầu nối trong `episode.json` (`"mega": 1`) →
ảnh/giọng/render cầu nối → `assemble.py build` → `assemble.py qa` → `assemble.py seo`. Mẫu: `projects/mega-01-bang-phong-than/`.

## Kiểm tra cuối (Kiểu A)
- [ ] 0 sự thật trùng tập lẻ (overlap_check + dò từ khóa); mọi sự thật có nguồn trong `meta.json > sources`
- [ ] ≥ 60:00 (thật sau `tts`), không mood > 50%, tempo TB ≥ 1.10, cameo ≥ 4%
- [ ] Bảng điểm khớp qua mọi vòng; nhà vô địch bất ngờ nhưng có lý
- [ ] Chapters 1/chương; Shorts 45-55s kiểu phễu cũ (bỏ lửng + kêu xem video dài + nối vòng); thumbnail badge "TẬP ĐẶC BIỆT"

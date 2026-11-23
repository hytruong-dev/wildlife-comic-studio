---
name: whiteboard-director
description: Quy trình cũ đạo diễn bảng trắng (Tập 1-5, edge-tts). Lưu ý - dự án hiện tại sản xuất tập mới theo skill episode-production.
---

# Skill: Whiteboard Director (AI Whiteboard Animation & Self-Evolving Engine)
*Zero-API-Key Local Agent-as-Director Workflow with Portable Memory*

Kỹ năng này biến AI Coding Agent (Gemini 3.8 / Antigravity) thành **Đạo diễn & Họa sĩ Bảng Trắng AI Cục Bộ kiêm Quản trị viên Bộ nhớ**.
Hệ thống **TUYỆT ĐỐI KHÔNG DÙNG API KEY BÊN NGOÀI**. Mọi công đoạn từ tạo giọng đọc, trích xuất mốc thời gian từng từ, thiết kế nét vẽ SVG/Rough.js đến render video MP4 đều chạy 100% trên máy tính của bạn.

---

## 1. NGUYÊN TẮC CỐT LÕI (CORE PRINCIPLES)
1. **Agent-as-Director & Memory Sync:** Trước khi làm video, luôn đồng bộ bộ nhớ từ `.agent_memory/` để áp dụng gu đạo diễn và các bài học kỹ thuật đã kiểm chứng.
2. **Contextual Word-to-Stroke Sync:** Nói tới từ khóa nào (`triggerWord`), ngòi bút bắt đầu đặt xuống vẽ sớm hơn 150 ms.
3. **Deterministic Frame Rendering:** Mọi chuyển động là hàm phụ thuộc vào số mili-giây $t$, không dùng `setTimeout` hay CSS transition tự do.
4. **Warm Sketchbook Aesthetic:** Nền giấy kem ấm `#F5EBD7`, nét than chì `#2C2A29`, dùng tối đa 3 màu nhấn (`#D9381E` Đỏ cam, `#2B6CB0` Xanh lam, `#2F855A` Xanh lá).

---

## 2. QUY TRÌNH 6 CỔNG KIỂM DUYỆT & TỰ HỌC (THE 6 GATES)

### Cổng 0: Đồng bộ Bộ Nhớ Dự Án (`Memory Sync Gate`)
1. Đọc `.agent_memory/director_taste.md`, `.agent_memory/lessons_learned.md`, `.agent_memory/visual_metaphor_dictionary.json` và thư mục `.agents/skills/learned/`.
2. Chạy lệnh kiểm tra bộ nhớ:
   ```bash
   python src/memory/memory_harvester.py --status
   ```
3. Mở đầu câu trả lời với người dùng bằng câu xác nhận đồng bộ bộ nhớ:
   *"🧠 [Memory Synced] Đã đồng bộ bộ nhớ dự án (N quy tắc đạo diễn, M mẫu ẩn dụ hình ảnh, K kỹ năng đã học). Sẵn sàng sản xuất video tiếp theo theo đúng chuẩn của bạn!"*

### Cổng 1: Thu thập & Tạo Giọng Đọc Chuẩn Xác (`Audio & Word-Timing Gate`)
1. Nhận chủ đề hoặc kịch bản từ người dùng. Nếu chỉ có chủ đề: Agent viết kịch bản lời bình súc tích (15 - 60 giây), giàu hình ảnh ẩn dụ theo phong cách `director_taste.md`.
2. Lưu kịch bản vào `projects/<project-name>/script.txt`.
3. Chạy lệnh:
   ```bash
   python src/audio/tts_engine.py --input projects/<project-name>/script.txt --voice vi-VN-NamMinhNeural --output projects/<project-name>/
   ```
   Lệnh này sinh ra:
   - `projects/<project-name>/narration.wav`: Giọng đọc chuẩn 44.1kHz.
   - `projects/<project-name>/words_timeline.json`: Thời điểm bắt đầu và kết thúc chính xác đến từng mili-giây của từng từ.

### Cổng 2: Lên Kịch Bản Phân Cảnh & Tra Cứu Ẩn Dụ (`Semantic Storyboard Gate`)
1. Đọc file `words_timeline.json` vừa tạo.
2. Tra cứu `visual_metaphor_dictionary.json` để tái sử dụng các mẫu hình vẽ đã được phê duyệt.
3. Phân chia các `VisualBeat`:
   - Gán `triggerWord` ứng với từ khóa trong câu (bắt đầu vẽ sớm hơn 150ms).
   - Chọn kiểu hình vẽ: `stick_character_*`, `rough_shape`, `rough_arrow`, `rough_chart_buckets`, `rough_bar_chart`, `lucide_icon` hoặc `handwritten_text`.
   - Bố cục theo mô hình **Song Đảo Ngữ Nghĩa (Dual Semantic Islands)** hoặc sơ đồ tâm điểm.
4. Lưu dữ liệu vào `projects/<project-name>/storyboard.json` theo đúng schema quy định.

### Cổng 3: Biên dịch Hình Vẽ & Kiểm Tra Bố Cục Tĩnh (`Look & Preview Gate`)
1. Chạy lệnh kiểm tra ảnh chụp kết thúc của từng cảnh:
   ```bash
   node src/cli/build_video.mjs projects/<project-name>/storyboard.json --preview-stills
   ```
2. Chạy công cụ kiểm tra va chạm tự động (Automated Visual QA):
   ```bash
   node src/cli/qa_checker.mjs projects/<project-name>/storyboard.json
   ```

### Cổng 4: Render Video MP4 Tất Định & Trộn Âm Thanh (`Deterministic Render Gate`)
1. Chạy lệnh render chính thức:
   ```bash
   node src/cli/build_video.mjs projects/<project-name>/storyboard.json --export projects/<project-name>/output.mp4 --fps 30
   ```
2. Quá trình render:
   - Playwright Chromium mở `src/engine/stage.html`, chụp từng khung hình và pipe trực tiếp qua MJPEG vào `ffmpeg`.
   - `src/audio/sfx_mixer.py` đọc nhật ký chuyển động bàn tay và tự động trộn tiếng bút sột soạt khớp từng mili-giây bút chạm giấy.
   - FFmpeg ghép video và master audio thành file `output.mp4`.

### Cổng 5: Phản Tư & Thu Hoạch Tri Thức Tự Động (`Retro & Self-Learning Gate`)
Ngay khi người dùng phê duyệt hoặc đưa ra góp ý chỉnh sửa:
1. Chạy `python src/memory/memory_harvester.py` để ghi nhận quy tắc thẩm mỹ mới vào `director_taste.md`.
2. Lưu các ẩn dụ hình ảnh mới vào `visual_metaphor_dictionary.json`.
3. Ghi nhật ký vào `production_log.md`:
   ```bash
   python src/memory/memory_harvester.py --log-video <project-id> "<title>" <duration-s> "<bài học rút ra>"
   ```
4. Nếu có mẫu bố cục mới nhiều bước, đóng gói thành skill mới tại `.agents/skills/learned/<skill-slug>/SKILL.md`.

# SVG & Rough.js Composer Rules
*Quy Tắc Sinh Hình Vẽ Ngữ Cảnh Tự Động cho Agent*

Agent khi phân tích câu thoại kịch bản cần ánh xạ các ý niệm trừu tượng thành hình ảnh ẩn dụ (Visual Metaphors) theo các mẫu tham số sau:

## 1. Ánh Xạ Ý Niệm Thành Hình Ảnh (Metaphor Mapping)
| Khái niệm trong lời bình | Hình tượng trực quan nên vẽ | Kiểu phần tử (`type`) |
| :--- | :--- | :--- |
| **Tiền bạc, chi tiêu, tài chính** | Chiếc ví mở rỗng, xấp tiền, giỏ hàng | `lucide_icon: wallet`, `shopping-cart` |
| **Lạm phát, giá cả leo thang** | Mũi tên uốn lượn hướng lên, biểu đồ cột dâng cao | `rough_arrow`, `rough_bar_chart` |
| **Phân chia ngân sách, quy tắc** | 3 hũ/giỏ chia tiền (50/30/20) | `rough_chart_buckets` |
| **Khó khăn, bế tắc, thắc mắc** | Nhân vật gãi đầu, nhíu mày, dấu hỏi | `stick_character_confused`, `stick_character_thinking` |
| **Thành công, giải pháp, niềm vui** | Nhân vật giơ tay ăn mừng, bóng đèn ý tưởng | `stick_character_happy`, `lucide_icon: lightbulb` |
| **Quy trình, các bước thực hiện** | Các thẻ hộp nối bằng mũi tên cong vẽ tay | `rough_shape: rectangle`, `rough_arrow` |

## 2. Quy Tắc Đồng Bộ Nhịp Vẽ (Beat Timing Rule)
- Tìm mốc `startMs` của từ khóa kích hoạt (`triggerWord`) từ `words_timeline.json`.
- Gán `beat.startMs = max(0, word.startMs - 120)` (đặt bút sớm hơn 120ms).
- Thời lượng vẽ `durationMs`: tương ứng với thời gian phát âm của cụm từ hoặc phân đoạn câu nói (thường từ 1800ms đến 3500ms).

## 3. Quy Tắc Giữ Nét Vẽ (Board Retention)
- Không xóa sạch bảng khi đang giải thích một ý. Các nét vẽ cũ của cụm bên trái được giữ nguyên trong khi bàn tay di chuyển sang vẽ cụm bên phải, giúp người xem nhìn thấy toàn bộ tiến trình tư duy logic.

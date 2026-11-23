---
name: self-learning-harvester
description: Tự động đúc kết tri thức, quy tắc đạo diễn và bài học kỹ thuật vào .agent_memory/.
---

# Skill: Self-Learning Harvester
*Tự động Đúc kết Tri thức, Quy tắc Đạo diễn & Bài học Kỹ thuật (Theo chuẩn kulaxyz & mattpocock)*

Kỹ năng này chịu trách nhiệm giám sát toàn bộ tương tác giữa người dùng và Agent để tự động thu hoạch tri thức, chống lặp lại lỗi cũ và duy trì bộ não tiến hóa liên tục cho dự án.

---

## 1. NGUYÊN TẮC HOẠT ĐỘNG
1. **Zero-Overhead:** Mọi việc thu hoạch diễn ra ngay trong phiên làm việc, lưu trữ trực tiếp dưới dạng Markdown/JSON trong `.agent_memory/`.
2. **Golden Paths Only:** Chỉ lưu trữ những giải pháp đã chạy thực tế thành công (verified golden paths) kèm triệu chứng lỗi cần tránh.
3. **Capped Compaction:** Tự động nén và gộp các quy tắc cũ nếu file bộ nhớ vượt quá 150 dòng, tránh làm tràn context window khi di chuyển sang máy mới.

---

## 2. KHI NÀO KÍCH HOẠT THU HOẠCH?
- Khi người dùng phản hồi: *"Chỉnh tay vẽ nhanh lên một chút"*, *"Giữ nét này nhé"*, *"Đẹp đấy"*.
- Khi vừa giải quyết xong một lỗi render, ffmpeg, tts, hoặc font tiếng Việt.
- Khi hoàn thành xuất file video MP4 cuối cùng của một dự án.

---

## 3. CÁC THAO TÁC CƠ BẢN
- Xem trạng thái bộ nhớ:
  ```bash
  python src/memory/memory_harvester.py --status
  ```
- Thêm quy tắc gu đạo diễn:
  ```bash
  python src/memory/memory_harvester.py --add-taste <RULE_ID> "<Quy tắc thẩm mỹ mới>"
  ```
- Thêm bài học kỹ thuật đã kiểm chứng:
  ```bash
  python src/memory/memory_harvester.py --add-lesson <ID> "<Triệu chứng>" "<Cách sai cần tránh>" "<Giải pháp chuẩn>"
  ```
- Thêm mẫu ẩn dụ hình ảnh đã được duyệt:
  ```bash
  python src/memory/memory_harvester.py --add-metaphor "<Từ khóa>" "<Layout Pattern>" "<Primitives CSV>" "<Colors CSV>" "<Ghi chú>"
  ```
- Ghi nhật ký video hoàn thành:
  ```bash
  python src/memory/memory_harvester.py --log-video <project-id> "<Tên video>" <Thời lượng s> "<Bài học rút ra>"
  ```

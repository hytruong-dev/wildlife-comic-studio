---
name: dual-semantic-islands
description: Kỹ năng bố cục bảng trắng chia 2 cụm ngữ nghĩa song song (trái - phải) nối bằng mũi tên chuyển hóa.
---

# Learned Skill: Dual Semantic Islands Layout
*Đúc kết từ repo hi-nikola & dự án demo-project 50/30/20*

Kỹ năng này tổ chức bảng trắng thành hai cụm đối xứng ngữ nghĩa, giải quyết vấn đề người xem theo dõi luồng tư duy so sánh hoặc nguyên nhân - kết quả.

## 1. PHÂN BỐ VÙNG KHÔNG GIAN
- **Cụm Trái (Vấn đề / Quá khứ / Nguyên nhân):**
  - Vùng tọa độ: $x \in [200, 750], y \in [300, 800]$.
  - Màu chủ đạo: Than chì `#2C2A29` kết hợp Đỏ cam `#D9381E`.
- **Trục Giữa (Mũi tên Chuyển hóa / Cân bằng):**
  - Vùng tọa độ: $x \in [750, 1150], y \in [450, 600]$.
  - Mũi tên cong vẽ tay `rough_arrow` uốn lượn nhẹ hướng từ trái sang phải.
- **Cụm Phải (Giải pháp / Tương lai / Kết quả):**
  - Vùng tọa độ: $x \in [1150, 1720], y \in [300, 800]$.
  - Màu chủ đạo: Xanh lam `#2B6CB0` kết hợp Xanh lá `#2F855A`.

## 2. NGUYÊN TẮC GIỮ BẢNG (BOARD RETENTION)
- Khi bàn tay di chuyển từ cụm trái sang cụm phải, nét vẽ cụm trái KHÔNG ĐƯỢC XÓA mà giữ nguyên trên mặt giấy.
- Nhờ đó, tại thời điểm kết thúc phân cảnh, người xem nhìn thấy toàn bộ bức tranh tổng thể gồm cả Vấn đề và Giải pháp trên cùng một trang giấy.

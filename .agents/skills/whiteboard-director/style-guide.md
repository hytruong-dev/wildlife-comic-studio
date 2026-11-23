# Style Guide: AI Whiteboard Animation Engine
*Chuẩn Bố Cục, Màu Sắc & Nhịp Điệu cho Bảng Trắng AI*

## 1. BẢNG MÀU SKETCHBOOK ẤM ÁP (Warm Sketchbook Palette)
- **Màu nền giấy chính:** `#F5EBD7` (Warm Cream Paper Texture, độ đục vân giấy 0.85).
- **Màu nét mực chính (Ink Outline):** `#2C2A29` hoặc `#242322` (Than chì đậm, không dùng màu đen tuyền `#000000` để tránh cảm giác kỹ thuật số giả tạo).
- **Màu nhấn cảnh báo / vấn đề:** `#D9381E` / `#E86A58` (Đỏ cam ấm).
- **Màu nhấn logic / cấu trúc / liên kết:** `#2B6CB0` / `#3182CE` (Xanh lam phong cách bút dạ).
- **Màu nhấn kết quả tích cực / tiền tài / thành công:** `#2F855A` / `#38A169` (Xanh lá tự nhiên).
- **Màu ghi chú / nổi bật:** `#FAF089` / `#D69E2E` (Vàng nghệ).

## 2. QUY CHUẨN ĐƯỜNG NÉT & TYPOGRAPHY
- **Độ dày nét bút (Stroke Width):**
  - Nét chính nhân vật / khung sơ đồ: `3.5px - 4.5px`.
  - Nét tô màu (Hachure Fill): `1.8px - 2.5px`, khoảng cách nét chéo `6px - 9px`.
  - Nét chữ viết tay: `2.5px - 3.5px`, cỡ chữ `28px - 48px`.
- **Font chữ viết tay tiếng Việt:** Sử dụng font `PatrickHand-Regular.ttf` hoặc `PlaypenSans-Regular.ttf` có đầy đủ dấu thanh tiếng Việt (sắc, huyền, hỏi, ngã, nặng, mũ).

## 3. BỐ CỤC SONG ĐẢO NGỮ NGHĨA (Dual Semantic Islands)
- **Trục ngang:**
  - Cụm bên trái: Khung hoành độ $x \in [200, 750]$ (Thường biểu thị Vấn đề, Hiện trạng, Nguyên nhân).
  - Cụm bên phải: Khung hoành độ $x \in [1150, 1720]$ (Thường biểu thị Giải pháp, Kết quả, Tương lai).
  - Trục giữa: Khung $x \in [750, 1150]$ dành cho Mũi tên chuyển hóa hoặc Sơ đồ cân bằng.
- **Trục dọc:** Tiêu đề ở đỉnh ($y \approx 120$), nội dung chính ở giữa ($y \in [300, 800]$), phụ đề ở đáy ($y \approx 980$).

## 4. CHUYỂN ĐỘNG CAMERA & BÀN TAY
- Bàn tay vẽ đi nét mực (Ink) chiếm 70% thời gian beat, tô màu chiếm 30%.
- Khi nhấc bút chuyển nét ($Z > 0$), cổ tay nghiêng nhẹ $-6^\circ$, bàn tay nâng cao vồng theo đường cong Bézier bậc hai.
- Camera di chuyển mượt mà theo hàm lò xo (`springEase`), không giật cục.

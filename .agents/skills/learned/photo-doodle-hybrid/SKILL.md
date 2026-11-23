---
name: photo-doodle-hybrid
description: Phương pháp sản xuất video Whiteboard Animation kết hợp Ảnh chụp thực tế (Photo Cutout) với Nét vẽ tay phác thảo (Doodle Sketch) chuẩn Web5Ngay / Tri Kỷ Cảm Xúc.
---

# KỸ NĂNG: KẾT HỢP ẢNH THẬT & NÉT VẼ TAY (PHOTO-DOODLE HYBRID WHITEBOARD)

## 1. Nguyên lý Cốt lõi (The Core Hybrid Philosophy)
- Không biến toàn bộ ảnh thật thành nét vẽ vector giả (tránh làm mất tính chân thực và biểu cảm của ảnh gốc).
- Tỷ lệ vàng: **30% Ảnh thật tách nền (Cutout)** + **70% Nét vẽ tay mực than chì & màu nhấn (Sketch/Doodle)**.
- Ảnh thật đóng vai trò **mỏ neo cảm xúc** (người đang mệt mỏi, người thức dậy sảng khoái, cốc cà phê, chiếc smartphone báo thức).
- Nét vẽ doodle đóng vai trò **người dẫn truyện & giải thích khoa học** (đồ thị sóng giấc ngủ, mũi tên chỉ số, công thức toán, biểu tượng chú thích Zzz, tích xanh, gạch chéo đỏ).

## 2. Kỹ thuật Render Mặt nạ Ngòi bút (Ink-Reveal Masking)
1. Ảnh thật được đặt trên canvas tại vị trí cố định với đường viền sticker trắng mỏng (4-6px) hoặc alpha trong suốt.
2. Khi bàn tay di chuyển qua vùng ảnh (theo đường zig-zag quét từ trên xuống hoặc từ tâm ra ngoài), lớp SVG mask mở dần theo đầu bút `(handTipX, handTipY)`.
3. Âm thanh ngòi bút sột soạt (`draw_scratch.wav`) vang lên đồng bộ với hành động quét cọ, tạo cảm giác người vẽ đang phác họa hoặc dán bức ảnh thật trực tiếp lên trang giấy.

## 3. Quy chuẩn Bố cục Sơ đồ Khoa học (Scientific Infographic Layout)
- **Đồ thị sóng ngủ 90 phút (Sleep Cycle Sine Curve)**:
  - Trục hoành là trục thời gian (0 -> 90 phút).
  - Trục tung là độ sâu (Ru ngủ -> Ngủ nông 50% -> Ngủ sâu 10% -> Ngủ rất sâu -> REM).
  - Gắn nhãn rõ ràng: Vùng Đỏ (Ngủ sâu/rất sâu = cấm đánh thức) vs Vùng Xanh (Ru ngủ/REM = điểm vàng thức dậy).
- **Hộp công thức (Formula Board)**:
  - Khung chữ nhật vẽ tay chứa công thức nổi bật.
  - Các mũi tên phân giải từng thành phần: Giờ ngủ, 14 phút chìm vào giấc ngủ, 90 phút một chu kỳ.
  - Đi kèm bảng tính các mốc giờ thức dậy tối ưu (5h44, 6h44, 7h14, v.v.).

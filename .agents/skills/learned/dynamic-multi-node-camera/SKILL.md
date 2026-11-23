---
name: dynamic-multi-node-camera
description: Hệ thống Layout & Camera chuẩn "Dynamic Multi-Node Canvas & Auto-Fit Bounding Box" kết hợp Fixed Top Header (1280x68) và Exclusive Active-Node Isolation khi vẽ từng phần tử.
---

# Dynamic Multi-Node Canvas & Auto-Fit Bounding Box Camera (`dynamic-multi-node-camera`)

## 1. Khi nào sử dụng kỹ năng này
Sử dụng cho mọi dự án video Whiteboard Animation dài (YouTube Long-form) của kênh **Vẽ Chuyện Hoang Dã**, giúp mỗi chương (Scene/Act) hiển thị linh hoạt $N$ hình vẽ ($N = 2, 3, 4, 5, 6+$) với chuyển động camera chuyên nghiệp.

## 2. 4 Quy Tắc Vàng Bắt Buộc (`TASTE-14` & `LESSON-12`)
1. **Fixed Viewport Header (`1280 x 68` px)**:
   - Thanh tiêu đề chương (`[PHẦN X] TIÊU ĐỀ CHƯƠNG`) được tách riêng thành lớp HUD cố định ở đỉnh màn hình (`0..68px`).
   - Tuyệt đối không đưa Header vào World Canvas để tránh bị phóng to hay cắt lấp lửng khi camera zoom.
2. **Dynamic Flow/Snake World Coordinates (`Gap >= 150px`)**:
   - Phân bổ $N$ hình vẽ trên vùng Body World Canvas (`gap_x >= 200px, gap_y >= 150px`, luôn đảm bảo `>= 120px`).
   - Hàng lẻ đi từ Trái $\rightarrow$ Phải; hàng chẵn uốn lượn kiểu Snake từ Phải $\rightarrow$ Trái để đường trượt camera ngắn và mượt nhất.
3. **Sequential Focus (`1.85x - 2.10x`) & Exclusive Active-Node Isolation**:
   - Khi đang vẽ hình thứ $i$, camera khóa tâm hình $i$ với độ phóng đại `1.85x - 2.10x`.
   - Bật `isolate_active_node_during_focus = True`: tự động ẩn các hình đã vẽ trước đó ($1..i-1$) trên nền giấy trắng tinh, đảm bảo **0% chi tiết thừa từ hình cũ lọt vào mép khung hình**.
   - Khi vẽ xong hình $i$, trượt camera mượt mà (`0.62s`, hàm `cubic-bezier(0.42, 0.0, 0.22, 1.0)` bằng `cv2.warpAffine`) sang hình $i+1$.
4. **Auto-Fit Bounding Box Overview Reveal (`Zoom Out Toàn Cảnh`)**:
   - Ngay khi hoàn thành hình cuối cùng thứ $N$ của chương, tính Bounding Box $[X_{\min}, X_{\max}, Y_{\min}, Y_{\max}]$ bao trọn cả $N$ hình, đưa camera mượt về `Center` và tỷ lệ `Zoom_out` để hiển thị đầy đủ toàn bộ tác phẩm bên dưới thanh Header cố định.

## 3. Module Thực Thi Chuẩn
- **Bộ định tuyến Layout & Keyframe**: `src/composition/dynamic_flow_layout.py` (`build_dynamic_multi_node_scene`)
- **Bộ kết xuất Video & Camera**: `src/render/hybrid_whiteboard_renderer.py` (`HybridWhiteboardRenderer`)

# GLOSSARY.md - Ubiquitous Language & Core Terminology
*Chuẩn thuật ngữ kỹ thuật dự án AI Whiteboard Animation Engine (Theo chuẩn mattpocock/skills)*

Dự án tuân thủ nghiêm ngặt các thuật ngữ và khái niệm dưới đây trên toàn bộ codebase (Node.js/TypeScript, Python, JSON Schemas):

## 1. Timing & Audio Synchrony
- **`WordToken`**: Đơn vị từ đơn lẻ có thời gian bắt đầu `startMs` và kết thúc `endMs` trích xuất từ âm thanh (thông qua `edge-tts` WordBoundary hoặc `faster-whisper`).
- **`WordTimeline`**: Danh sách tuần tự các `WordToken` kèm metadata tổng thời lượng `totalDurationMs` và text đầy đủ.
- **`TriggerWord`**: Từ khóa kích hoạt một hành động vẽ cụ thể trong kịch bản; ngòi bút chạm giấy sớm hơn thời điểm bắt đầu của từ khóa này khoảng 100 - 150 ms để thị giác bắt kịp thính giác.

## 2. Visual & Stroke Architecture
- **`VisualBeat`**: Một hành động vẽ gắn liền với một khoảng thời gian của câu nói (bắt đầu vẽ khi đọc đến từ khóa `triggerWord` và kết thúc nét vẽ tại `endWord` hoặc theo `durationMs`).
- **`StrokePath`**: Một đường vẽ đơn lẻ.
  - Trong chế độ Vector: Chuỗi lệnh SVG Path (`d="M x y C..."`) có tổng chiều dài $L$, hỗ trợ nội suy `stroke-dashoffset`.
  - Trong chế độ Raster: Mảng tọa độ pixel $(x_k, y_k)$ đã được làm khung xương (skeletonized) và sắp xếp tối ưu theo thuật toán TSP.
- **`CompiledStroke`**: Đối tượng nét vẽ đã được tính toán thời gian `startMs`, `endMs`, chiều dài `length`, màu sắc `strokeColor`, độ dày `strokeWidth`, và phân loại (nét mực `isFillStroke: false` hay nét quét màu `isFillStroke: true`).
- **`ProtectedRegion`**: Vùng hình chữ nhật hoặc đa giác thuộc về một đối tượng sẽ xuất hiện ở tương lai, được che chắn (mask) để các nét vẽ hiện tại không đè lên làm lộ trước.

## 3. Kinematics & Physics
- **`HandRig`**: Hệ thống điều khiển bàn tay cầm bút, bao gồm vị trí ngòi bút $(x_{\text{tip}}, y_{\text{tip}})$, góc xoay cổ tay $\theta(t)$, trạng thái chạm giấy $Z(t) \in [0, 1]$ ($0$: đang chạm giấy vẽ, $1$: nhấc cao nhất trên không), tỷ lệ thu phóng `scale`, và vector độ lệch bóng đổ `shadowOffset`.
- **`PenLift`**: Hành vi nhấc bút khi di chuyển giữa hai nét vẽ rời rạc; quỹ đạo nâng bút theo đường cong Bézier bậc 2 có độ vồng và bóng đổ dịch xa.

## 4. Camera & Canvas
- **`CameraFrame`**: Khung nhìn hiện tại của máy quay trên bảng trắng vô tận (Infinite Whiteboard), xác định bởi tâm $(c_x, c_y)$ và độ phóng đại $s$ (`scale`).
- **`DualSemanticIslands`**: Bố cục bảng trắng chia 2 cụm ngữ nghĩa song song (trái - phải hoặc trên - dưới), nối với nhau bằng mũi tên tổng kết hoặc sơ đồ so sánh.
- **`DeterministicRenderer`**: Cơ chế kết xuất khung hình tất định: với bất kỳ thời điểm $t$ (hoặc frame $f$), trạng thái hình ảnh, vị trí nét mực và bàn tay luôn cho ra kết quả duy nhất, không phụ thuộc vào xung nhịp thời gian thực của CPU.

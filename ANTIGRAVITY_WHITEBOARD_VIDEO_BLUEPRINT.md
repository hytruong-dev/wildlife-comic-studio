# DỰ ÁN: HỆ THỐNG SẢN XUẤT VIDEO VẼ TAY THEO NGỮ CẢNH & TỰ TIẾN HÓA (AI WHITEBOARD ANIMATION & SELF-EVOLVING ENGINE)
**Target Agent:** Antigravity (Gemini 3.8)  
**Kiến trúc cốt lõi:** $100\%$ Local & Agent-Driven (TUYỆT ĐỐI KHÔNG DÙNG API KEY BÊN NGOÀI)  
**Phương pháp đồ họa:** Hybrid Vector-Stream (SVG/Rough.js + HyperFrames/Remotion) & Raster-Skeleton (OpenCV Stream Ink-to-Color) đồng bộ từng từ (Word-level Sync) với bàn tay vẽ thực tế.  
**Cơ chế Bộ nhớ:** Self-Evolving Portable Markdown/JSON Memory (Tự học sau mỗi cuộc trò chuyện, đóng gói $100\%$ trong thư mục dự án, dời sang máy mới đọc hiểu ngay mà không cần huấn luyện lại).

---

## PHẦN 1: NGHIÊN CỨU THỊ TRƯỜNG & HỆ SINH THÁI 14 REPOSITORY NỀN TẢNG

### 1.1. Phân tích các phần mềm thương mại trên thị trường
Trên thị trường hiện tại, các công cụ làm video vẽ tay (Whiteboard / Doodle Explainer Video) chia làm 3 nhóm chính:
1. **Nhóm Kéo-Thả Truyền Thống (VideoScribe, Doodly, Vyond, Animaker):**
   - *Cơ chế:* Sử dụng thư viện file vector SVG có sẵn các đường dẫn ẩn (reveal paths). Khi xuất video, phần mềm chạy hiệu ứng `stroke-dashoffset` và gắn ảnh PNG bàn tay chạy theo tọa độ điểm đầu mút của đường vector.
   - *Nhược điểm:* Chi phí thuê bao đắt đỏ, phải căn chỉnh timeline thủ công bằng tay, không tự động hiểu ngữ cảnh câu nói để vẽ đúng lúc.
2. **Nhóm Chuyển Ảnh Thành Video Vẽ Tay (Speedpaint.io, Kinoslide):**
   - *Cơ chế:* Nhận một bức ảnh tĩnh, tách nét đen (Line Art extraction) và vùng màu, sau đó dùng thuật toán quét đường xương (Skeletonization) để tạo hiệu ứng bàn tay vẽ lại bức ảnh đó.
   - *Nhược điểm:* Vẽ máy móc từ trên xuống dưới hoặc từ trái qua phải, không vẽ theo thứ tự câu chuyện (Narrative Order) của lời thoại, tính phí theo credit đám mây.
3. **Nhóm AI Explainer Thế Hệ Mới (Golpo AI, KinoDraw):**
   - *Cơ chế:* Đưa kịch bản văn bản vào, AI tự tách phân cảnh, chọn hình vẽ (doodles), tạo giọng đọc (TTS), lấy mốc thời gian từng từ (Word-level Timestamps) và điều khiển bàn tay vẽ khớp hoàn toàn với từ đang phát âm.

### 1.2. Giải phẫu 6 Repository gốc bạn cung cấp (Core Pillars)

| STT | Repository / Docs | Tinh hoa kỹ thuật rút ra để đưa vào dự án |
| :--- | :--- | :--- |
| **1** | **`cth9191/animate`** | - **Kiến trúc "Agent-as-Runtime":** Biến chính AI Coding Agent (Antigravity) thành đạo diễn và họa sĩ viết code tạo video thông qua một `<canvas>` duy nhất, xuất MP4 qua Playwright + FFmpeg.<br>- **Quy trình 5 cổng kiểm duyệt (Check-in Gates):** `0. Intake` $\rightarrow$ `1. Story check (Beat table)` $\rightarrow$ `2. Look check` $\rightarrow$ `3. Storyboard` $\rightarrow$ `4. Build` $\rightarrow$ `5. Review & QA`.<br>- **Kỹ thuật nâng cao:** Seeded randomness (nét vẽ rung nhẹ kiểu "boil on 2s"), chuyển cảnh biến hình (`shape-morph transitions`), tự động căn nhịp theo từ với `faster-whisper` local. |
| **2** | **`geeklee/srt-whiteboard-animation`** | - **Cơ chế "SRT-Driven Semantic Drawing":** Không vẽ theo tọa độ vật lý ngẫu nhiên mà vẽ theo thứ tự sự kiện trong phụ đề SRT (`Bối cảnh` $\rightarrow$ `Nhân vật chính` $\rightarrow$ `Hành động` $\rightarrow$ `Kết quả`).<br>- **Cấu trúc `annotation.json`:** Quản lý vùng vẽ (`region`), thời gian (`startMs`, `durationMs`), vùng bảo vệ chống lộ nét chồng lấp (`protectedRegions`).<br>- **Renderer 2 pha (`render_stream_whiteboard.py`):** Pha 1 đi nét mực đen (`ink-path`: `grid` hoặc `skeleton`), Pha 2 tô màu (`color-fill`: `contour-wipe`) trên nền giấy kem ấm `#F5EBD7`. Có công cụ `preview.html` để chỉnh sửa trực quan. |
| **3** | **`remotion.dev/docs`** | - **Deterministic Frame Rendering:** Mọi chuyển động là một hàm toán học phụ thuộc vào số thứ tự khung hình hiện tại $f = \text{useCurrentFrame}()$, tuyệt đối không dùng `setTimeout` hay CSS animation tự do gây lệch khung hình khi xuất video.<br>- **Thư viện `@remotion/paths`:** Cung cấp các hàm `getLength()`, `getPointAtLength()`, `evolvePath()` giúp lấy chính xác tọa độ $(x, y)$ và góc tiếp tuyến $\theta$ của ngòi bút tại bất kỳ mili-giây nào. |
| **4** | **`heygen-com/hyperframes`** | - **HTML-Native Deterministic Video Engine:** Viết HTML/CSS/SVG/GSAP thuần kèm các thuộc tính `data-composition-id`, `data-start`, `data-duration`.<br>- **Tối ưu cho AI Agent:** Nhẹ hơn React/Remotion khi Agent cần sinh hàng chục cảnh động liên tiếp; hỗ trợ tua khung hình chính xác (`window.__timelines`) qua Headless Chromium và xuất MP4 bằng FFmpeg. |
| **5** | **`kurbaitaev/ghost-editor`** | - **Recipe `"Vector Explainer"`:** Một người dẫn chuyện đọc tới đâu, một bức tranh liên tục tự vẽ tới đó trong khi camera di chuyển (Pan/Zoom) mượt mà xuyên suốt bức tranh lớn (Infinite Canvas).<br>- **Vòng lặp Tự Kiểm Tra (Self-QA Loop):** Tự động kiểm tra âm lượng, khoảng lặng, chữ bị tràn lề hoặc độ tương phản thấp, tự sửa lỗi tối đa $3$ lần trước khi bàn giao. |
| **6** | **`mattpocock/skills`** | - **Kỷ luật Kỹ thuật Phần mềm & Phản tư cho Agent:**<br>  + `GLOSSARY.md` & `/grill-with-docs`: Xây dựng ngôn ngữ chung (Ubiquitous Language) và tự động cập nhật tài liệu kiến trúc ngay trong lúc thảo luận với người dùng.<br>  + `/retro`: Kỹ năng tự nhìn lại phiên làm việc để nâng cấp quy chuẩn code và quy trình.<br>  + `Deep Modules` & `Tracer Bullets`: Chia dự án thành các module sâu và các lát cắt dọc chạy được từ đầu đến cuối kèm kiểm thử tự động. |

### 1.3. Năm (05) Repository Mã Nguồn Mở Bổ Sung cho Đồ họa Vẽ Tay
Để giải quyết triệt để bài toán **"Không dùng API Key bên ngoài"** mà vẫn có hình vẽ đẹp, chữ viết tay chuẩn tiếng Việt và bàn tay chuyển động mượt như người thật, dự án tích hợp thêm tinh hoa từ $5$ repo sau:

1. **`hi-nikola/hand-drawn-explainer-video-nikola`:**
   - Bản nâng cấp kết hợp giữa `geeklee/srt-whiteboard-animation` và `HyperFrames`.
   - Đưa ra bố cục **"Song Đảo Ngữ Nghĩa" (Dual Semantic Islands)**: Vừa nói nửa câu đầu vừa vẽ cụm bên trái, nói sang vế sau thì vẽ cụm bên phải và nối mũi tên tổng kết, giữ nguyên nét vẽ cũ trên bảng.
2. **`masihsultani/whiteboard-animator`:**
   - Cung cấp thuật toán phân rã nét giao nhau (Junction Decomposition) và phát hiện vùng chữ (CRAFT ONNX CPU) để khi bàn tay viết chữ hoặc vẽ hình chữ thập `X`, nét bút đi liền mạch từ đầu mút thay vì mọc từ tâm ra ngoài.
3. **`letuandat131/whiteboard-animation-vi` (Phát triển tại Việt Nam):**
   - Thuật toán gom nhóm màu trong không gian màu $\text{CIELAB}$ (`ink-aware color clusters`), ưu tiên vẽ chủ thể trước cảnh vật (`subject-first`), tối ưu hóa đường đi ngắn nhất cho bàn tay giữa các nét vẽ (giải bài toán người du lịch - TSP routing) và mô phỏng chuyển động cổ tay, bóng đổ của bàn tay thật.
4. **`edwardaiwang-svg/kinodraw`:**
   - Kho tài nguyên $1,760+$ hình vẽ tay SVG (Doodles) bản quyền mở `CC BY 4.0`, bộ font chữ viết tay mã nguồn mở (`Playpen Sans`, `LXGW WenKai`) và cơ chế tìm kiếm hình vẽ theo ngữ nghĩa hoàn toàn Offline (Semantic Doodle Matcher).
5. **Hệ sinh thái thư viện JS/Python Local (Zero-API):**
   - **`Rough.js`**: Biến mọi hình học cơ bản, biểu đồ, sơ đồ khối và icon SVG (từ bộ $1,500+$ icon của *Lucide* / *Tabler Icons*) thành nét vẽ tay phác thảo chì/bút dạ cực kỳ tự nhiên.
   - **`opentype.js`**: Chuyển đổi văn bản tiếng Việt (có dấu đầy đủ) sử dụng font chữ viết tay (như *Playpen Sans*, *Caveat*, *Patrick Hand*) thành các đường `<path d="...">` thực thụ để bàn tay **viết từng nét chữ và từng dấu thanh tiếng Việt** thay vì chỉ hiện chữ kiểu gõ máy tính.
   - **`edge-tts` & `piper-tts`**: Tạo giọng đọc AI tiếng Việt (`vi-VN-HoaiMyNeural`, `vi-VN-NamMinhNeural`) hoàn toàn miễn phí trên máy cục bộ, không cần API key trả phí.
   - **`faster-whisper`**: Mô hình nhận diện giọng nói chạy local (CPU/GPU) để trích xuất **Word-level Timestamps** (thời điểm bắt đầu và kết thúc chính xác đến từng mili-giây của từng từ).

### 1.4. Ba (03) Repository Mã Nguồn Mở Bổ Sung cho "Bộ Não Tự Học & Di Động Đa Máy"
Để đảm bảo mỗi cuộc trò chuyện của bạn với Antigravity đều được ghi nhận, tự động tiến hóa qua từng video và khi copy dự án sang máy tính khác AI hiểu ngay lập tức mà không cần dạy lại:

1. **`kulaxyz/self-learning-skills` (Cơ chế Tự Đúc Kết Kỹ Năng - Skill Extraction & Triage):**
   - Huấn luyện Agent tự động phát hiện các "luồng xử lý chuẩn" (Golden Paths), các sở thích của người dùng hoặc các lỗi kỹ thuật vừa được giải quyết trong cuộc trò chuyện.
   - **Phân loại thông minh (Triage):** Nếu là quy trình hoặc mẫu bố cục vẽ mới nhiều bước $\rightarrow$ Tự động đóng gói thành một kỹ năng mới tại `.agents/skills/learned/<tên-kỹ-năng>/SKILL.md`. Nếu là tinh chỉnh thông số hoặc gu thẩm mỹ $\rightarrow$ Ghi thẳng vào `.agent_memory/director_taste.md`.
   - **Quy tắc Kiểm chứng (Promotion Rule):** Chỉ lưu vào bộ nhớ những kỹ thuật đã chạy render thành công thực tế kèm triệu chứng lỗi cần tránh.
2. **`frontmatters/agentBrain` (Kiến trúc Kho Tri Thức Markdown Local-First):**
   - Tổ chức bộ nhớ dài hạn bằng file Markdown và JSON thuần túy ngay trong thư mục dự án ($100\%$ Offline, không cần Vector Database đám mây, không cần API embedding).
   - Triết lý *"One brain, many agents"*: Bất kỳ máy tính mới nào mở thư mục dự án và đọc file điều hướng trung tâm `AGENTS.md` sẽ kế thừa trọn vẹn trí tuệ của máy cũ.
3. **`kadiresen/context-bank` (Cơ chế Nén Bộ Nhớ & Chống Tràn Ngữ Cảnh - Capped Memory Bank):**
   - Giải quyết bài toán khi bạn sản xuất tới video thứ $50$ hay $100$: Nếu lưu toàn bộ lịch sử trò chuyện thô thì AI ở máy mới sẽ bị tràn bộ nhớ (context window).
   - `context-bank` giới hạn số dòng của mỗi file bộ nhớ và buộc AI phải **hợp nhất / ghi đè (compact & supersede)** các quy tắc cũ bằng quy tắc mới tinh gọn hơn, giúp AI trên máy mới chỉ mất vài giây để nạp toàn bộ lịch sử tiến hóa của dự án.

---

## PHẦN 2: KIẾN TRÚC TỔNG THỂ "ZERO-API-KEY" & "SELF-EVOLVING MEMORY"

### 2.1. Làm sao để sản xuất video AI & Tự học mà KHÔNG CẦN API Key bên ngoài?
- **Bản thân Antigravity CHÍNH LÀ bộ não Đạo diễn, Họa sĩ Vector kiêm Quản trị viên Bộ nhớ:** Khi bạn trò chuyện trong khung chat của Antigravity, chính Antigravity sẽ:
  1. Đọc `.agent_memory/` để nhớ lại gu thẩm mỹ và các mẫu hình vẽ bạn từng duyệt ở các video trước.
  2. Phân tích kịch bản, ánh xạ từng từ khóa sang hình ảnh vẽ tay (`storyboard.json`).
  3. Gọi các script Python/Node.js chạy $100\%$ Local (`edge-tts`, `faster-whisper`, `Rough.js`, `opentype.js`, `OpenCV`, `Playwright`, `FFmpeg`) để xuất ra video MP4.
  4. Ngay khi bạn góp ý sửa đổi hoặc khen một phân cảnh, Antigravity tự động chạy script `memory_harvester.py` để ghi nhận bài học vào `.agent_memory/` và `.agents/skills/learned/`.

### 2.2. Sơ đồ luồng dữ liệu khép kín (End-to-End Pipeline & Learning Loop)

```text
                ╔═══════════════════════════════════════════════════════════════╗
                ║       KHO BỘ NHỚ DI ĐỘNG (.agent_memory/ & AGENTS.md)         ║
                ║  - director_taste.md (Gu thẩm mỹ, tốc độ tay, bảng màu)       ║
                ║  - visual_metaphor_dictionary.json (Từ điển từ khóa -> Hình)  ║
                ║  - lessons_learned.md (Các lỗi kỹ thuật đã sửa & Golden Path) ║
                ║  - .agents/skills/learned/ (Các mẫu bố cục vẽ đã đúc kết)     ║
                ╚══════════════╤═════════════════════════════════▲══════════════╝
                               │ (Đọc ở đầu phiên)               │ (Tự động cập nhật sau mỗi
                               ▼                                 │  lần góp ý / hoàn tất video)
[Đầu vào: Chủ đề / Kịch bản] ──► [CỔNG 0: ĐỒNG BỘ BỘ NHỚ DỰ ÁN]  │
                               │                                 │
                               ▼                                 │
┌──────────────────────────────────────────────────────────────┐ │
│ BƯỚC 1: VOICE & WORD-SYNC ENGINE (Python Local - Zero API)   │ │
│ - Sinh giọng đọc bằng `edge-tts` (vi-VN-NamMinhNeural)       │ │
│ - Hoặc đọc file thu âm -> Chạy `faster-whisper` local        │ │
│ - Output: `narration.wav` + `words_timeline.json` (mốc ms)   │ │
└──────────────────────────────┬───────────────────────────────┘ │
                               ▼                                 │
┌──────────────────────────────────────────────────────────────┐ │
│ BƯỚC 2: ANTIGRAVITY SEMANTIC STORYBOARDER (Gemini 3.8)       │─┘
│ - Áp dụng luật trong `director_taste.md` & `learned skills`  │ (Ghi nhận phản hồi
│ - Ánh xạ từng cụm từ đang nói -> Hành động vẽ (Trigger Word) │  của người dùng)
│ - Output: `storyboard.json`                                  │
└──────────────────────────────┬───────────────────────────────┘
                               ▼
┌──────────────────────────────────────────────────────────────┐
│ BƯỚC 3: DUAL VISUAL COMPILER (Biên dịch Nét Vẽ & Đường Bút)  │
│ ├── Nhánh Vector (`Rough.js` + `opentype.js` + `Lucide SVG`) │
│ └── Nhánh Raster (`OpenCV Skeleton` + `Lab Color Stream`)    │
└──────────────────────────────┬───────────────────────────────┘
                               ▼
┌──────────────────────────────────────────────────────────────┐
│ BƯỚC 4: DETERMINISTIC HAND-SYNC RENDERER (Playwright+FFmpeg) │
│ - Vẽ nét mực & tô màu khớp mili-giây với từ đang phát âm     │
│ - Điều khiển bàn tay (`hand_physics.ts`), nghiêng cổ tay,    │
│   nhấc bút 3D, bóng đổ + trộn tiếng bút sột soạt (`sfx`)     │
│ - Output: `final_video.mp4` (Full HD 1080p, 30/60 FPS)       │
└──────────────────────────────────────────────────────────────┘
```

---

## PHẦN 3: CHỈ DẪN KỸ THUẬT CHI TIẾT & THUẬT TOÁN CỐT LÕI (DEEP MODULES)

### 3.1. Từ điển Thuật ngữ Dự án (`GLOSSARY.md` - Theo chuẩn `mattpocock/skills`)
Antigravity PHẢI tuân thủ tuyệt đối các tên gọi biến và khái niệm sau trong toàn bộ codebase:
- **`WordToken`**: Đơn vị từ đơn lẻ có thời gian bắt đầu `startMs` và kết thúc `endMs` trích xuất từ âm thanh.
- **`VisualBeat`**: Một hành động vẽ gắn liền với một khoảng thời gian của câu nói (bắt đầu vẽ khi đọc đến từ khóa `triggerWord` và hoàn thành tại `endWord`).
- **`StrokePath`**: Một đường vẽ đơn lẻ. Trong chế độ Vector, nó là một chuỗi lệnh SVG Path (`M x y C ...`) có tổng chiều dài $L$. Trong chế độ Raster, nó là mảng tọa độ pixel $(x_k, y_k)$ đã sắp xếp theo thứ tự thời gian.
- **`HandRig`**: Hệ thống điều khiển bàn tay cầm bút, bao gồm vị trí mũi bút $(x_{\text{tip}}, y_{\text{tip}})$, góc xoay cổ tay $\theta$, trạng thái chạm giấy $z \in [0, 1]$ ($0$: đang vẽ, $1$: đang nhấc bút di chuyển sang nét mới), và bóng đổ (drop shadow).
- **`CameraFrame`**: Khung nhìn hiện tại của máy quay trên bảng trắng vô tận (Infinite Whiteboard), xác định bởi tâm $(c_x, c_y)$ và độ phóng đại $s$ (`scale`).
- **`ProtectedRegion`**: Vùng hình chữ nhật hoặc đa giác thuộc về một đối tượng sẽ xuất hiện ở tương lai, bị khóa mặt nạ (mask) không cho các nét vẽ của đối tượng hiện tại đè lên làm lộ trước.
- **`MemoryRule`**: Một quy tắc thẩm mỹ, kỹ thuật hoặc ánh xạ hình ảnh đã được đúc kết từ cuộc hội thoại với người dùng và lưu trữ bền vững trong `.agent_memory/`.

---

### 3.2. Cấu trúc Thư mục Chuẩn của Dự án (`handdraw-studio`)

Antigravity cần khởi tạo dự án với cấu trúc kết hợp Node.js (TypeScript), Python $3.11+$ và Hệ thống Bộ nhớ Di động như sau:

```text
handdraw-studio/
├── AGENTS.md                             # [BẮT BUỘC ĐỌC ĐẦU TIÊN] Bản đồ điều hướng & Giao thức chuyển máy
├── GLOSSARY.md                           # Từ điển ngôn ngữ chung của toàn dự án
├── package.json                          # Dependencies: playwright, roughjs, opentype.js, lucide-static, gsap
├── requirements.txt                      # Dependencies: edge-tts, faster-whisper, opencv-python, numpy, scipy, scikit-image, pillow
├── .agent_memory/                        # BỘ NHỚ DÀI HẠN DI ĐỘNG (Đi theo dự án sang mọi máy tính)
│   ├── director_taste.md                 # Gu thẩm mỹ của chủ dự án (tốc độ vẽ, màu sắc, bố cục, nhịp điệu)
│   ├── lessons_learned.md                # Lịch sử lỗi kỹ thuật đã giải quyết & Golden Paths (chống lặp lỗi)
│   ├── visual_metaphor_dictionary.json   # Từ điển ánh xạ: Khái niệm/Từ khóa -> Tổ hợp hình vẽ đã được duyệt
│   └── production_log.md                 # Nhật ký tóm tắt 50 video gần nhất & các cải tiến đã áp dụng
├── .agents/
│   └── skills/
│       ├── core/                         # Kỹ năng gốc của hệ thống
│       │   ├── whiteboard-director/
│       │   │   ├── SKILL.md              # Quy trình 6 cổng kiểm duyệt đạo diễn video
│       │   │   ├── style-guide.md        # Quy chuẩn màu sắc, bố cục, nhịp điệu gốc
│       │   │   └── svg-composer-rules.md # Quy tắc sinh hình vẽ SVG/Rough.js theo ngữ cảnh
│       │   └── self-learning-harvester/
│       │       └── SKILL.md              # Kỹ năng tự học sau mỗi cuộc trò chuyện (kế thừa kulaxyz & mattpocock)
│       └── learned/                      # KỸ NĂNG MỚI DO AI TỰ ĐÚC KẾT QUA CÁC LẦN LÀM VIDEO
│           └── README.md                 # Danh mục các mẫu bố cục/hiệu ứng mới học được từ người dùng
├── assets/
│   ├── hands/                            # Bộ ảnh PNG bàn tay tách nền (cầm bút dạ, bút chì, cọ tô màu)
│   │   ├── hand-marker-right.png         # Kèm metadata tọa độ mũi bút (anchor point)
│   │   └── hand-shadow.png
│   ├── fonts/                            # Font chữ viết tay hỗ trợ đầy đủ Tiếng Việt
│   │   ├── PlaypenSans-Regular.ttf
│   │   ├── PlaypenSans-Bold.ttf
│   │   └── PatrickHand-Regular.ttf
│   ├── sfx/                              # Âm thanh tiếng bút vẽ trên giấy (loop) & chuyển cảnh
│   │   ├── marker-scribble-loop.wav
│   │   ├── chalk-stroke.wav
│   │   └── page-whoosh.wav
│   ├── paper/
│   │   └── warm-cream-texture.png        # Nền giấy #F5EBD7
│   └── doodles/                          # Kho icon SVG (Lucide/Tabler + Custom Doodles)
├── src/
│   ├── memory/                           # Module 0: Quản trị Bộ Nhớ Tự Học & Đồng Bộ Đa Máy (Python)
│   │   └── memory_harvester.py           # CLI kiểm tra bộ nhớ, thêm bài học mới, nén dữ liệu (Compaction)
│   ├── audio/                            # Module 1: Xử lý Giọng nói & Thời gian (Python)
│   │   ├── tts_engine.py                 # Chạy edge-tts / local TTS tạo audio + word timestamps
│   │   ├── whisper_aligner.py            # Chạy faster-whisper khi dùng file thu âm ngoài
│   │   └── sfx_mixer.py                  # Tự động trộn tiếng bút vẽ sột soạt khi bàn tay chạm giấy
│   ├── compiler/                         # Module 2: Biên dịch Hình ảnh thành Nét Vẽ (TS & Python)
│   │   ├── text_to_svg_paths.ts          # Dùng opentype.js biến chữ Tiếng Việt thành SVG paths
│   │   ├── rough_doodle_compiler.ts      # Dùng Rough.js biến hình học & icon SVG thành nét vẽ tay
│   │   ├── visual_primitives.ts          # Kho 15 mẫu sơ đồ, nhân vật, biểu đồ tham số hóa
│   │   ├── stroke_sorter.ts              # Thuật toán TSP sắp xếp thứ tự nét vẽ tự nhiên nhất
│   │   └── raster_stream_extractor.py    # (Từ geeklee & masihsultani) Skeletonize ảnh PNG -> đường bút
│   ├── engine/                           # Module 3: Lõi Render Khung hình Xác định (Deterministic HTML/Canvas)
│   │   ├── stage.html                    # Sân khấu chính (tương thích HyperFrames & Playwright)
│   │   ├── hand_physics.ts               # Toán học nội suy vị trí bàn tay, góc cổ tay, nhấc bút
│   │   ├── camera_controller.ts          # Điều khiển Pan/Zoom mượt mà giữa các vùng trên bảng
│   │   └── frame_renderer.ts             # Hàm renderFrame(timeMs) hoàn toàn tất định (deterministic)
│   ├── studio/                           # Module 4: Bàn dựng Preview & Tinh chỉnh trên Trình duyệt
│   │   └── preview_editor.html           # (Kế thừa geeklee) Xem trước, kéo thả vùng vẽ, chỉnh timing
│   └── cli/
│       ├── build_video.mjs               # CLI tổng hợp chạy Playwright chụp từng frame -> FFmpeg MP4
│       └── qa_checker.mjs                # Tự động kiểm tra chất lượng khung hình & âm thanh
└── projects/                             # Nơi chứa từng dự án video cụ thể
    └── demo-project/
        ├── script.txt
        ├── narration.wav
        ├── words_timeline.json
        ├── storyboard.json
        └── output.mp4
```

---

### 3.3. Thiết kế Toán học & Thuật toán Cốt lõi (Deep Modules)

Antigravity phải cài đặt chính xác $5$ thuật toán cốt lõi dưới đây:

#### Thuật toán 1: Đồng bộ Từ khóa Ngữ cảnh với Thời gian Vẽ (Contextual Word-to-Stroke Sync)
Giả sử câu thoại có chuỗi các từ $W = \{w_1, w_2, \dots, w_n\}$, mỗi từ $w_i$ có khoảng thời gian phát âm $[t_{i,\text{start}}, t_{i,\text{end}}]$.
Khi Antigravity phân tích câu thoại: *"Khi **lạm phát** tăng cao, **giá cả** hàng hóa leo thang làm **ví tiền** của bạn xẹp xuống"*, Antigravity sẽ tạo ra $3$ `VisualBeat`:
1. `Beat 1` (Biểu đồ mũi tên lạm phát đi lên): Bắt đầu vẽ ngay khi giọng đọc chạm tới từ **"lạm phát"** ($t_{\text{start}} = t_{\text{"lạm"},\text{start}} - 150\text{ ms}$, vẽ sớm hơn $150\text{ ms}$ để mắt người xem bắt kịp âm thanh), và hoàn thành nét vẽ ngay khi đọc xong cụm *"tăng cao"*.
2. `Beat 2` (Hình giỏ hàng và thẻ giá): Bắt đầu vẽ tại từ **"giá cả"**, hoàn thành tại *"leo thang"*.
3. `Beat 3` (Hình chiếc ví rỗng và nhân vật thở dài): Bắt đầu vẽ tại từ **"ví tiền"**, hoàn thành tại *"xẹp xuống"*.

Bên trong một `VisualBeat` kéo dài trong khoảng $[T_{\text{start}}, T_{\text{end}}]$ với tổng thời lượng $\Delta T = T_{\text{end}} - T_{\text{start}}$:
- Gọi $\alpha_{\text{ink}} \in [0.65, 0.80]$ là tỷ lệ thời gian dành cho việc đi nét mực đen (Ink phase) và $1 - \alpha_{\text{ink}}$ là tỷ lệ thời gian tô màu (Color fill phase).
- Nếu một hình vẽ gồm $M$ đường cong SVG `<path>` với độ dài lần lượt là $L_1, L_2, \dots, L_M$, và giữa nét thứ $k$ với nét thứ $k+1$ có khoảng cách di chuyển trên không (nhấc bút - pen lift) là:
  $$d_k = \sqrt{(x_{k+1,\text{start}} - x_{k,\text{end}})^2 + (y_{k+1,\text{start}} - y_{k,\text{end}})^2}$$
- Thời gian cấp phát cho từng nét vẽ tỷ lệ với lũy thừa $\gamma = 0.7$ của chiều dài nét (để nét dài được vẽ nhanh hơn một chút giống thói quen tay người thật, nét ngắn chi tiết vẽ chậm lại):
  $$w_k = (L_k)^\gamma, \quad \gamma = 0.7$$
  $$\Delta t_k = \left(\alpha_{\text{ink}} \cdot \Delta T - \sum_{j=1}^{M-1} t_{\text{lift}, j}\right) \cdot \frac{w_k}{\sum_{j=1}^M w_j}$$
- Tại thời điểm hiện tại $t \in [t_{k,\text{start}}, t_{k,\text{end}}]$, tiến độ chuẩn hóa của nét vẽ thứ $k$ được tính qua hàm Easing mượt đầu-cuối:
  $$u(t) = \frac{t - t_{k,\text{start}}}{\Delta t_k} \in [0, 1]$$
  $$p(t) = \text{easeInOutSine}(u(t)) = \frac{1 - \cos(\pi \cdot u(t))}{2}$$
- Chiều dài nét mực đã hiện ra trên giấy là $s(t) = p(t) \cdot L_k$, được áp dụng vào SVG qua thuộc tính:
  ```css
  stroke-dasharray: L_k;
  stroke-dashoffset: L_k * (1 - p(t));
  ```

#### Thuật toán 2: Động học Bàn tay Vẽ (Photographic Hand Kinematics & Shadow Rig)
Để bàn tay không bị cứng đờ như ảnh ghép, `src/engine/hand_physics.ts` phải tính toán trạng thái bàn tay $\mathcal{H}(t) = (X(t), Y(t), \theta(t), Z(t))$ ở mỗi khung hình:
1. **Tọa độ mũi bút $(X(t), Y(t))$:**
   - Khi đang vẽ nét $k$: Lấy trực tiếp từ hàm hình học của đường SVG: $(X(t), Y(t)) = \text{path}_k.\text{getPointAtLength}(p(t) \cdot L_k)$.
   - Khi đang nhấc bút chuyển từ cuối nét $k$ sang đầu nét $k+1$ (trong khoảng $t_{\text{lift}} \approx 80\text{ ms} - 160\text{ ms}$): Nội suy theo đường cong Bézier bậc hai có độ vồng nhẹ lên phía trên:
     $$\mathbf{P}_{\text{lift}}(u) = (1-u)^2 \mathbf{P}_{k,\text{end}} + 2(1-u)u \mathbf{P}_{\text{ctrl}} + u^2 \mathbf{P}_{k+1,\text{start}}$$
     Trong đó độ nhấc bút $Z(u) = \sin(\pi u) \in [0, 1]$.
2. **Góc lắc cổ tay tự nhiên $\theta(t)$:**
   - Tính vector tiếp tuyến của nét vẽ tại điểm hiện tại: $\vec{\tau}(t) = \text{path}_k.\text{getPointAtLength}(s(t) + \delta) - \text{path}_k.\text{getPointAtLength}(s(t) - \delta)$.
   - Góc hướng bút $\phi(t) = \text{atan2}(\tau_y, \tau_x)$. Cổ tay con người không xoay $360^\circ$ theo nét bút mà chỉ nghiêng nhẹ trong khoảng $[-12^\circ, +12^\circ]$ kết hợp bộ lọc thông thấp (Low-pass Exponential Smoothing):
     $$\theta_{\text{target}}(t) = \text{clamp}(\sin(\phi(t)) \cdot 10^\circ + \cos(2\phi(t)) \cdot 4^\circ, -12^\circ, +12^\circ)$$
     $$\theta(t) = \alpha \cdot \theta(t - \Delta t_{\text{frame}}) + (1 - \alpha) \cdot \theta_{\text{target}}(t), \quad \alpha = 0.75$$
3. **Hiệu ứng Nhấc bút & Bóng đổ (Pen-Lift & Dynamic Drop Shadow):**
   - Khi $Z(t) > 0$ (nhấc bút): Dịch ảnh bàn tay lệch lên góc phải trên một đoạn $(\Delta x, \Delta y) = (12 \cdot Z(t), -18 \cdot Z(t))$ pixel, phóng to bàn tay nhẹ $1 + 0.03 \cdot Z(t)$, đồng thời làm mờ và dịch xa lớp bóng đổ `hand-shadow.png` để tạo cảm giác không gian 3D chân thực như bàn tay đang nhấc khỏi mặt giấy.

#### Thuật toán 3: Viết chữ Tiếng Việt từng nét bằng `opentype.js` (`text_to_svg_paths.ts`)
- Sử dụng `opentype.js` đọc trực tiếp file font `assets/fonts/PlaypenSans-Bold.ttf`.
- Khi cần viết dòng chữ (ví dụ: `"Tự Do Tài Chính"`), gọi `font.getPaths(text, x, y, fontSize)` để tách từng ký tự (bao gồm cả dấu sắc, huyền, hỏi, ngã, nặng, mũ `â, ê, ô, ơ, ư`) thành mảng các đối tượng `Path`.
- Hợp nhất các contour con của dấu thanh vào đúng thứ tự liền sau thân chữ cái tương ứng để bàn tay viết thân chữ xong là đánh dấu ngay lập tức, sau đó mới chuyển sang chữ cái tiếp theo.

#### Thuật toán 4: Chế độ Raster Stream Ink-to-Color (Kế thừa `geeklee/srt-whiteboard-animation` & `letuandat131`)
Dành cho các cảnh phức tạp sử dụng hình ảnh minh họa PNG có sẵn:
1. **Tách lớp Mực và Lớp Màu:**
   - Chuyển ảnh sang không gian màu $\text{CIELAB}$. Các pixel có độ sáng $L^* < 65$ và độ bão hòa thấp được trích xuất làm lớp **Nét Mực (Ink Layer)**.
   - Dùng thuật toán `skimage.morphology.skeletonize` để thu gọn nét mực thành khung xương rộng $1\text{ px}$, sau đó xây dựng đồ thị (Graph) tìm các đường đi liên tục dài nhất, kết hợp giải thuật **Nearest-Neighbor TSP + 2-opt** để bàn tay không nhảy cóc hỗn loạn trên màn hình.
2. **Bảo vệ Vùng Chồng Lấp (`protectedRegions`):**
   - Nếu `Element A` (Ngọn núi phía sau) được vẽ ở giây thứ $1.0$, và `Element B` (Nhân vật đứng trước ngọn núi) được vẽ ở giây thứ $4.0$, thì vùng bounding box/polygon của `Element B` được đưa vào `protectedRegions` của `Element A`. Khi vẽ `Element A`, mặt nạ (Mask) sẽ chặn không cho bất kỳ pixel nào thuộc `Element B` hiện ra sớm.
3. **Tô màu dạng Quét Cọ (`Contour-Wipe / Zigzag Brush`):**
   - Sau khi vẽ xong nét mực của một vùng, bàn tay chuyển sang quét cọ chéo góc $45^\circ$ (zigzag stroke) với bán kính đầu cọ $R_{\text{brush}} = 24\text{ px}$ để mở khóa dần lớp màu gốc của bức ảnh.

#### Thuật toán 5: Tự động lồng tiếng sột soạt của ngòi bút (`sfx_mixer.py`)
- Dựa vào mảng trạng thái chạm giấy $Z(t)$ của bàn tay trên toàn bộ timeline video:
  - Khi bàn tay đang di chuyển trên giấy ($Z(t) = 0$ và vận tốc mũi bút $v(t) = \sqrt{\dot{X}(t)^2 + \dot{Y}(t)^2} > 5\text{ px/s}$), tự động bật âm lượng kênh tiếng bút dạ/bút chì (`marker-scribble-loop.wav`) ở mức $-18\text{ dBFS}$, đồng thời biến thiên nhẹ tần số (pitch shift $\pm 5\%$) theo vận tốc $v(t)$.
  - Khi bàn tay nhấc lên ($Z(t) > 0$) hoặc dừng vẽ, giảm âm lượng tiếng bút về $0$ với thời gian fade-out $40\text{ ms}$.
  - Khi Camera chuyển sang vùng bảng mới (Pan/Zoom lớn), tự động chèn tiếng `page-whoosh.wav` nhẹ ở mức $-22\text{ dBFS}$.

---

## PHẦN 4: HỆ THỐNG BỘ NHỚ TỰ HỌC & DI ĐỘNG ĐA MÁY (SELF-EVOLVING PORTABLE MEMORY ENGINE)

Module này kết hợp tinh hoa từ **`mattpocock/skills`**, **`kulaxyz/self-learning-skills`**, **`frontmatters/agentBrain`** và **`kadiresen/context-bank`**, giúp Antigravity ghi nhớ mọi điều bạn chỉ dạy và mang đi bất kỳ máy tính nào.

### 4.1. Nguyên lý Thiết kế Bộ Nhớ Di Động
1. **Zero-Cloud & $100\%$ Git/Folder-Portable:** Không lưu bộ nhớ trong cơ sở dữ liệu ẩn của IDE hay tài khoản cá nhân. Mọi tri thức học được đều nằm trong thư mục `.agent_memory/`, `.agents/skills/learned/` và file `AGENTS.md`. Khi copy thư mục dự án qua USB hoặc `git clone` sang máy mới, $100\%$ bộ não của dự án đi theo.
2. **Chắt lọc Quy tắc thay vì Lưu Chat Thô (Distilled Rules over Raw Logs):** Nếu lưu nguyên văn hàng chục cuộc hội thoại, AI ở máy mới sẽ bị quá tải ngữ cảnh (Context Rot). Thay vào đó, mỗi khi bạn góp ý hoặc khen ngợi, Antigravity sẽ **chắt lọc thành quy tắc cô đọng** và cập nhật vào đúng phân vùng bộ nhớ.

### 4.2. Chi tiết 4 Phân Vùng Bộ Nhớ trong `.agent_memory/`

Antigravity phải khởi tạo sẵn $4$ file sau ngay khi dựng dự án:

#### 1. `.agent_memory/director_taste.md` (Hồ sơ Gu Thẩm Mỹ & Đạo Diễn của Chủ Dự Án)
Lưu trữ mọi sở thích cá nhân của bạn về nhịp độ, bố cục, màu sắc, kiểu chữ. Giới hạn tối đa $150$ dòng (luôn gộp và cập nhật quy tắc mới nhất).
*Mẫu khởi tạo:*
```markdown
# HỒ SƠ GU ĐẠO DIỄN & THẨM MỸ (DIRECTOR TASTE PROFILE)
> File này được cập nhật tự động sau mỗi lần chủ dự án góp ý. Mọi video mới PHẢI tuân thủ các quy tắc dưới đây.

## 1. Nhịp độ & Tốc độ Bàn tay (Pacing & Hand Speed)
- [TASTE-01] Bàn tay bắt đầu đặt bút vẽ sớm hơn 150ms trước khi giọng đọc phát âm tới từ khóa chính (`triggerWord`).
- [TASTE-02] Tỷ lệ thời gian đi nét mực đen (`inkRatio`) mặc định là 0.72, thời gian tô màu gạch chéo (`hachure`) là 0.28.
- [TASTE-03] Không bao giờ để bàn tay đứng yên trên màn hình quá 800ms; nếu khoảng nghỉ dài hơn, phải hạ bàn tay ra khỏi khung hình dưới.

## 2. Quy tắc Bố cục & Chữ viết (Layout & Typography)
- [TASTE-04] Mỗi nhãn chữ viết tay trên bảng không vượt quá 5 từ. Ưu tiên hình vẽ và mũi tên nối hơn là viết đoạn văn dài.
- [TASTE-05] Giữ lại các hình vẽ cũ trên cùng một mặt giấy tối đa 25 giây để tạo sơ đồ tổng thể trước khi chuyển trang mới.
```

#### 2. `.agent_memory/lessons_learned.md` (Sổ tay Kinh nghiệm Kỹ thuật & Chống Lặp Lỗi)
Theo chuẩn của `kulaxyz/self-learning-skills`, mọi lỗi kỹ thuật đã giải quyết đều được lưu theo cấu trúc $3$ phần: **Triệu chứng (Symptom)** $\rightarrow$ **Cách làm sai cần tránh (Dead-end)** $\rightarrow$ **Giải pháp chuẩn (Verified Golden Path)**.
*Mẫu khởi tạo:*
```markdown
# SỔ TAY KINH NGHIỆM KỸ THUẬT (VERIFIED LESSONS LEARNED)
> AI trên máy mới đọc file này để áp dụng ngay giải pháp chuẩn, tuyệt đối không thử lại các hướng đã thất bại.

### [LESSON-01] Xử lý dấu thanh Tiếng Việt khi dùng opentype.js
- **Symptom:** Khi bàn tay viết chữ Tiếng Việt có 2 dấu (như "ẩ", "ậ", "ữ"), nét bút nhảy qua chữ cái kế tiếp rồi mới quay lại đánh dấu.
- **Ruled-out Dead-end:** Không sắp xếp path theo tọa độ X thuần túy vì dấu mũ/dấu nặng có tọa độ X nằm giữa thân chữ.
- **Verified Golden Path:** Tách path theo từng cụm ký tự (grapheme cluster) trước, sắp xếp các contour bên trong cùng một ký tự theo thứ tự (Thân chữ chính -> Dấu phụ -> Dấu thanh), sau đó mới nối sang ký tự tiếp theo.
```

#### 3. `.agent_memory/visual_metaphor_dictionary.json` (Từ điển Ẩn dụ Hình ảnh đã được Phê duyệt)
Mỗi khi Antigravity thiết kế một tổ hợp hình vẽ cho một khái niệm trừu tượng (ví dụ: *"Lạm phát"*, *"Lãi kép"*, *"Trì hoãn"*, *"Tự do tài chính"*) mà bạn khen đẹp, nó sẽ lưu cấu trúc đó vào từ điển này để các video sau dùng lại ngay lập tức hoặc biến tấu nhẹ.
*Mẫu khởi tạo:*
```json
{
  "version": "1.0.0",
  "metaphors": {
    "lạm phát": {
      "approvedCount": 3,
      "layoutPattern": "split-scale-imbalance",
      "primitives": ["icon:flame", "rough:rising_arrow_red", "icon:shopping_cart_shrinking"],
      "preferredColors": ["#D9381E", "#2C2A29"],
      "notes": "Vẽ ngọn lửa đốt tờ tiền bên trái kết hợp mũi tên đỏ kéo giá hàng hóa đi lên bên phải."
    },
    "lãi kép": {
      "approvedCount": 2,
      "layoutPattern": "snowball-exponential-curve",
      "primitives": ["rough:exponential_curve_green", "icon:sprout_to_tree", "icon:coins_stack"],
      "preferredColors": ["#2F855A", "#D69E2E"],
      "notes": "Vẽ đường cong dốc đứng ở nửa sau, đặt 3 chồng đồng xu cao dần theo cấp số nhân."
    }
  }
}
```

#### 4. `.agent_memory/production_log.md` (Nhật ký Tiến hóa qua từng Video)
Lưu tóm tắt $50$ video gần nhất đã sản xuất kèm theo bài học mới rút ra ở video đó. Khi chuyển sang máy mới, AI đọc file này sẽ biết dự án đang ở giai đoạn nào và vừa làm xong những gì.

---

### 4.3. Giao thức Tự Học 3 Bước sau mỗi Cuộc Trò Chuyện (Continuous Learning Loop)

Bất cứ khi nào bạn trò chuyện với Antigravity để làm video, Antigravity PHẢI vận hành ngầm vòng lặp tự học sau:

1. **Bước 1 - Bắt tín hiệu Học tập (Trigger Detection):**
   - **Tín hiệu Phê chuẩn (Positive Trigger):** Khi bạn nói *"Kiểu vẽ này đẹp đấy"*, *"Duyệt cảnh này"*, *"Giữ tốc độ này nhé"*.
   - **Tín hiệu Chỉnh sửa (Correction Trigger):** Khi bạn yêu cầu sửa đổi *"Tay vẽ nhanh/chậm quá"*, *"Chữ hơi nhỏ"*, *"Đừng vẽ kiểu liệt kê này nữa, hãy vẽ dạng sơ đồ tâm điểm"*.
   - **Tín hiệu Khắc phục Lỗi (Bugfix Trigger):** Khi vừa sửa xong một lỗi render, lệch tiếng hoặc lỗi font.
2. **Bước 2 - Phân loại & Đóng gói (Triage & Persist qua `memory_harvester.py`):**
   - Nếu là **sở thích/thông số đạo diễn** $\rightarrow$ Chạy lệnh cập nhật `.agent_memory/director_taste.md`.
   - Nếu là **cách minh họa một từ khóa/khái niệm** $\rightarrow$ Chạy lệnh lưu vào `.agent_memory/visual_metaphor_dictionary.json`.
   - Nếu là **lỗi kỹ thuật vừa sửa xong** $\rightarrow$ Ghi vào `.agent_memory/lessons_learned.md`.
   - Nếu là **một kiểu bố cục chuyển động mới hoàn chỉnh** (ví dụ: Bố cục *"So sánh Trước/Sau có bàn tay gạch chéo đỏ"*) $\rightarrow$ Tự động tạo một thư mục kỹ năng mới tại `.agents/skills/learned/<slug>/SKILL.md` kèm file `template.json` để tái sử dụng lâu dài.
3. **Bước 3 - Nén Bộ Nhớ chống phình đại (Memory Compaction):**
   - Nếu bất kỳ file `.md` nào trong `.agent_memory/` vượt quá $180$ dòng, Antigravity phải tự động gộp các quy tắc trùng lặp và ghi đè quy tắc cũ đã lỗi thời, đảm bảo bộ nhớ luôn tinh gọn, sắc bén.

---

### 4.4. Quy chuẩn File `AGENTS.md` ở Thư mục Gốc (Chìa khóa Chuyển giao Máy Mới)

Antigravity PHẢI tạo file `AGENTS.md` ở ngay thư mục gốc của dự án. Đây là file tiêu chuẩn mà mọi Coding Agent (Antigravity, Cursor, Claude Code, Windsurf) đều tự động quét đầu tiên khi mở workspace trên một máy tính mới:

```markdown
# AGENTS.md — BẢN ĐỒ ĐIỀU HƯỚNG & BỘ NÃO DI ĐỘNG CỦA DỰ ÁN

## 1. GIAO THỨC BẮT BUỘC KHI KHỞI ĐỘNG (ZERO-RETRAINING HANDOVER PROTOCOL)
> **CHỈ DẪN TỐI CAO CHO AI (TRÊN MỌI MÁY TÍNH):**
> Dự án này tích hợp **Hệ thống Bộ Nhớ Tự Tiến Hóa (Self-Evolving Portable Memory)**. Trước khi phản hồi yêu cầu làm video của người dùng hoặc viết bất kỳ dòng code nào, bạn **BẮT BUỘC** phải đọc tuần tự 4 nguồn tri thức sau để tiếp nhận toàn bộ quá trình huấn luyện từ các phiên/máy tính trước:
> 1. `GLOSSARY.md` — Nắm vững ngôn ngữ chung và cấu trúc dữ liệu.
> 2. `.agent_memory/director_taste.md` — Nắm vững 100% gu thẩm mỹ, tốc độ bàn tay vẽ, bảng màu và quy tắc bố cục của chủ dự án. Tuyệt đối không hỏi lại những điều đã được quy định trong file này.
> 3. `.agent_memory/lessons_learned.md` — Nắm vững các giải pháp kỹ thuật chuẩn (Golden Paths) và tránh xa các lỗi đã được khắc phục.
> 4. `.agent_memory/visual_metaphor_dictionary.json` & thư mục `.agents/skills/learned/` — Tái sử dụng các mẫu ẩn dụ hình ảnh và kỹ năng bố cục mà chủ dự án đã phê duyệt trước đó.
>
> **Sau khi đọc xong, hãy mở đầu câu trả lời bằng dòng xác nhận:**
> *"🧠 [Memory Synced] Đã đồng bộ bộ nhớ dự án (N quy tắc đạo diễn, M mẫu ẩn dụ hình ảnh, K kỹ năng đã học). Sẵn sàng sản xuất video tiếp theo theo đúng chuẩn của bạn!"*

## 2. GIAO THỨC TỰ HỌC LIÊN TỤC (CONTINUOUS LEARNING DUTY)
Trong suốt cuộc trò chuyện với người dùng:
- Mỗi khi người dùng góp ý sửa đổi bố cục, tốc độ, màu sắc hoặc khen ngợi một phân cảnh, bạn PHẢI gọi `python src/memory/memory_harvester.py` (hoặc cập nhật trực tiếp vào `.agent_memory/`) NGAY TRONG LƯỢT PHẢN HỒI ĐÓ trước khi render lại video.
- Khi hoàn thành xuất file MP4 cuối cùng của một dự án, bạn PHẢI chạy bước `/retro` (Cổng kiểm duyệt số 5) để ghi nhật ký vào `.agent_memory/production_log.md` và đúc kết kỹ năng mới vào `.agents/skills/learned/` nếu có.
```

---

## PHẦN 5: ĐẶC TẢ SCHEMA DỮ LIỆU CHUẨN (`storyboard.json`)

Đây là hợp đồng dữ liệu (Data Contract) trung gian giữa bộ não của **Antigravity** và **Engine Render**. Antigravity sinh ra file `storyboard.json` theo đúng chuẩn này từ kịch bản của người dùng và từ các quy tắc trong `.agent_memory/`:

```json
{
  "projectId": "tai-chinh-ca-nhan-01",
  "title": "Quy tắc 50/30/20 trong Quản lý Tài chính",
  "appliedMemoryRules": ["TASTE-01", "TASTE-02", "TASTE-04", "LESSON-01"],
  "canvas": {
    "width": 1920,
    "height": 1080,
    "fps": 30,
    "backgroundColor": "#F5EBD7",
    "paperTextureOpacity": 0.15
  },
  "audio": {
    "voiceModel": "vi-VN-NamMinhNeural",
    "voiceRate": "+5%",
    "narrationWav": "narration.wav",
    "enablePenSfx": true,
    "bgmTrack": "assets/bgm/calm-acoustic.mp3",
    "bgmDuckingDb": -16
  },
  "scenes": [
    {
      "sceneId": "scene-01",
      "layoutMode": "dual-semantic-islands",
      "camera": {
        "initial": { "x": 960, "y": 540, "scale": 1.0 },
        "keyframes": [
          { "timeMs": 0, "x": 600, "y": 540, "scale": 1.15, "easing": "spring" },
          { "timeMs": 4500, "x": 960, "y": 540, "scale": 1.0, "easing": "spring" }
        ]
      },
      "subtitles": [
        {
          "text": "Hầu hết chúng ta đều hết sạch tiền vào cuối tháng vì không chia giỏ chi tiêu.",
          "startMs": 200,
          "endMs": 5200
        }
      ],
      "beats": [
        {
          "beatId": "beat-01-wallet",
          "narrativeRole": "setup_problem",
          "triggerWord": "hết sạch tiền",
          "startMs": 700,
          "durationMs": 2100,
          "renderMode": "procedural_svg",
          "position": { "x": 420, "y": 480, "width": 380, "height": 380 },
          "inkRatio": 0.72,
          "elements": [
            {
              "type": "rough_shape",
              "shape": "stick_character_confused",
              "strokeColor": "#2C2A29",
              "strokeWidth": 4.5,
              "fillColor": "#E86A58",
              "fillStyle": "hachure"
            },
            {
              "type": "handwritten_text",
              "text": "Ví rỗng 0đ!",
              "x": 420,
              "y": 720,
              "fontSize": 48,
              "color": "#D9381E"
            }
          ]
        },
        {
          "beatId": "beat-02-three-buckets",
          "narrativeRole": "introduce_solution",
          "triggerWord": "chia giỏ",
          "startMs": 2950,
          "durationMs": 2000,
          "renderMode": "procedural_svg",
          "position": { "x": 1350, "y": 480, "width": 600, "height": 420 },
          "inkRatio": 0.72,
          "elements": [
            {
              "type": "rough_arrow",
              "from": [680, 480],
              "to": [1020, 480],
              "strokeColor": "#2B6CB0",
              "curved": true
            },
            {
              "type": "rough_chart_buckets",
              "labels": ["50% Thiết yếu", "30% Mong muốn", "20% Tiết kiệm"],
              "colors": ["#3182CE", "#DD6B20", "#38A169"]
            }
          ]
        }
      ]
    }
  ]
}
```

---

## PHẦN 6: QUY TRÌNH 6 CỔNG KIỂM DUYỆT & TỰ HỌC (AGENT WORKFLOW SKILL)

Antigravity sẽ lưu quy trình vận hành vào `.agents/skills/core/whiteboard-director/SKILL.md`. Mỗi khi người dùng yêu cầu làm một video mới, Antigravity thực hiện tuần tự $6$ cổng sau:

### Cổng 0: Đồng bộ Bộ Nhớ Dự Án (`Memory Sync Gate`)
- Đọc `.agent_memory/director_taste.md`, `.agent_memory/lessons_learned.md`, `.agent_memory/visual_metaphor_dictionary.json` và danh sách kỹ năng trong `.agents/skills/learned/`.
- Chạy `python src/memory/memory_harvester.py --status` để báo cáo tóm tắt số lượng quy tắc và mẫu hình vẽ đã học.

### Cổng 1: Thu thập & Tạo Giọng Đọc Chuẩn Xác (`Audio & Word-Timing Gate`)
- Nhận chủ đề hoặc kịch bản từ người dùng. Nếu mới chỉ có ý tưởng, viết kịch bản lời bình giàu hình ảnh ẩn dụ theo đúng phong cách trong `director_taste.md`.
- Chạy lệnh sinh giọng đọc và trích xuất thời gian từng từ:
  ```bash
  python src/audio/tts_engine.py --input projects/<name>/script.txt --voice vi-VN-NamMinhNeural --output projects/<name>/
  ```

### Cổng 2: Lên Kịch Bản Phân Cảnh & Tra Cứu Ẩn Dụ (`Semantic Storyboard Gate`)
- Đọc `words_timeline.json`, đối chiếu các từ khóa trong kịch bản với `visual_metaphor_dictionary.json`.
  - Nếu từ khóa đã có trong từ điển ẩn dụ $\rightarrow$ Tái sử dụng hoặc phát triển từ tổ hợp hình ảnh đã được người dùng duyệt trước đó.
  - Nếu là khái niệm mới $\rightarrow$ Thiết kế tổ hợp `Rough.js` + `Lucide SVG` mới và đánh dấu để sau khi người dùng duyệt sẽ tự động nạp vào từ điển.
- Thiết kế bảng phân cảnh (`Beat Table`): Nói tới từ khóa nào, ngòi bút bắt đầu đặt xuống vẽ hình minh họa của từ khóa đó sớm hơn $150\text{ ms}$.

### Cổng 3: Biên dịch Hình Vẽ & Kiểm tra Bố cục Tĩnh (`Look & Preview Gate`)
- Sinh file `storyboard.json` và chạy lệnh xuất ảnh chụp các khung hình kết thúc của từng cảnh:
  ```bash
  node src/cli/build_video.mjs projects/<name>/storyboard.json --preview-stills
  ```
- Chạy `node src/cli/qa_checker.mjs` để kiểm tra tự động: không có chữ đè lên hình, không tràn lề `1920x1080`, độ tương phản chuẩn.

### Cổng 4: Render Video MP4 Tất Định & Trộn Âm Thanh (`Deterministic Render Gate`)
- Chạy lệnh xuất video MP4 chính thức:
  ```bash
  node src/cli/build_video.mjs projects/<name>/storyboard.json --export projects/<name>/output.mp4
  ```
- Headless Chromium (Playwright) chụp từng frame tại $t = f / \text{FPS}$, truyền qua đường ống (`pipe`) vào FFmpeg kết hợp bộ trộn âm thanh tiếng bút vẽ sột soạt (`sfx_mixer.py`).

### Cổng 5: Phản Tư & Thu Hoạch Tri Thức Tự Động (`Retro & Self-Learning Gate`)
- Ngay sau khi người dùng xem video và đưa ra nhận xét (hoặc phê duyệt hoàn tất), Antigravity chạy `python src/memory/memory_harvester.py` để:
  1. Cập nhật các tinh chỉnh mới của người dùng vào `.agent_memory/director_taste.md`.
  2. Bổ sung các cặp `Từ khóa -> Hình vẽ` mới thành công vào `.agent_memory/visual_metaphor_dictionary.json`.
  3. Nếu vừa tạo ra một kiểu sơ đồ/hiệu ứng mới đặc sắc, đóng gói thành skill mới trong `.agents/skills/learned/<skill-name>/SKILL.md`.
  4. Ghi dòng tổng kết vào `.agent_memory/production_log.md`.

---

## PHẦN 7: KẾ HOẠCH TRIỂN KHAI THEO TỪNG CHẶNG (6 MILESTONES TRACER-BULLET CHO ANTIGRAVITY)

Khi bắt đầu xây dựng dự án này, **Antigravity (Gemini 3.8)** phải thực hiện tuần tự $6$ chặng (Milestones) theo phương pháp **Tracer Bullets & TDD**:

### Chặng 1 (Milestone 1): Khởi tạo Hệ Thống Bộ Nhớ Di Động & Khung Dự Án
- **Mục tiêu:** Thiết lập nền móng `AGENTS.md`, `GLOSSARY.md`, thư mục `.agent_memory/` và công cụ `src/memory/memory_harvester.py` trước tiên để mọi bước phát triển tiếp theo đều được ghi nhận vào bộ nhớ dự án.
- **Tiêu chí nghiệm thu:** Chạy `python src/memory/memory_harvester.py --status` hiển thị đầy đủ trạng thái bộ nhớ, kiểm tra tính toàn vẹn của $4$ file trong `.agent_memory/`.

### Chặng 2 (Milestone 2): Lõi Render Bàn Tay Vẽ SVG & Viết Chữ Tiếng Việt (Tracer Bullet)
- **Mục tiêu:** Tạo ra một video MP4 dài $5$ giây hoàn chỉnh, trong đó một bàn tay thật cầm bút vẽ một hình nhân vật + một mũi tên + viết dòng chữ tiếng Việt *"Xin chào Việt Nam!"* đầy đủ dấu thanh trên nền giấy `#F5EBD7`.
- **Các file cần tạo:** `scripts/generate_hand_asset.py`, `src/compiler/text_to_svg_paths.ts`, `src/compiler/rough_doodle_compiler.ts`, `src/engine/hand_physics.ts`, `src/engine/stage.html`, `src/cli/build_video.mjs`.
- **Tiêu chí nghiệm thu:** Xuất thành công `test_milestone_2.mp4`, mũi bút bám sát điểm đầu nét mực (sai số $< 2\text{ px}$).

### Chặng 3 (Milestone 3): Giọng Đọc Local & Đồng Bộ Từng Từ (Zero-API Audio Sync)
- **Mục tiêu:** Đưa văn bản tiếng Việt vào, hệ thống tự sinh giọng đọc bằng `edge-tts`, lấy mốc thời gian từng từ (`words_timeline.json`), điều khiển bàn tay vẽ đúng lúc từ khóa được phát âm và tự động lồng tiếng bút sột soạt (`sfx_mixer.py`).
- **Tiêu chí nghiệm thu:** Xuất video $15$ giây có giọng đọc tiếng Việt khớp hoàn toàn với nét vẽ bàn tay (sai lệch $< 100\text{ ms}$).

### Chặng 4 (Milestone 4): Thư Viện Hình Vẽ Ngữ Cảnh & Camera Lò Xo (Contextual Visual Kit)
- **Mục tiêu:** Xây dựng `src/compiler/visual_primitives.ts` gồm $15$ mẫu sơ đồ động, nhân vật biểu cảm, biểu đồ vẽ tay kết hợp $1,500+$ icon từ `lucide-static` qua bộ lọc `Rough.js`, cùng hệ thống Camera Pan/Zoom lò xo (`src/engine/camera_controller.ts`).

### Chặng 5 (Milestone 5): Tích hợp Engine Vẽ Ảnh Raster (OpenCV Stream Ink-to-Color)
- **Mục tiêu:** Xây dựng `src/compiler/raster_stream_extractor.py` kế thừa thuật toán của `geeklee/srt-whiteboard-animation` và `masihsultani/whiteboard-animator` để tách nét xương (`skeletonize`) và tô màu (`contour-wipe`) cho mọi bức ảnh PNG/JPG.

### Chặng 6 (Milestone 6): Bàn Dựng Preview Studio, Tự Động Kiểm Tra (Self-QA) & Đóng Gói Skills
- **Mục tiêu:** Hoàn thiện `src/studio/preview_editor.html`, `src/cli/qa_checker.mjs` và đóng gói bộ đôi kỹ năng `.agents/skills/core/whiteboard-director/SKILL.md` + `.agents/skills/core/self-learning-harvester/SKILL.md`.

---

## PHẦN 8: MÃ NGUỒN KHỞI ĐẦU CHUẨN CHO CÁC MODULE QUAN TRỌNG (REFERENCE IMPLEMENTATION)

Antigravity có thể sử dụng trực tiếp các đoạn mã chuẩn dưới đây khi xây dựng dự án:

### 8.1. Công cụ Quản trị Bộ Nhớ Tự Học & Chuyển Giao Đa Máy (`src/memory/memory_harvester.py`)
Công cụ CLI giúp Antigravity ghi nhận bài học mới, cập nhật từ điển ẩn dụ hình ảnh, nén bộ nhớ và kiểm tra trạng thái khi dời sang máy mới:

```python
import json
import argparse
from datetime import datetime
from pathlib import Path

MEMORY_DIR = Path(".agent_memory")
SKILLS_LEARNED_DIR = Path(".agents/skills/learned")

TASTE_FILE = MEMORY_DIR / "director_taste.md"
LESSONS_FILE = MEMORY_DIR / "lessons_learned.md"
METAPHOR_FILE = MEMORY_DIR / "visual_metaphor_dictionary.json"
LOG_FILE = MEMORY_DIR / "production_log.md"

def init_memory():
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    SKILLS_LEARNED_DIR.mkdir(parents=True, exist_ok=True)

    if not TASTE_FILE.exists():
        TASTE_FILE.write_text(
            "# HỒ SƠ GU ĐẠO DIỄN & THẨM MỸ (DIRECTOR TASTE PROFILE)\n"
            "- [TASTE-01] Bàn tay đặt bút vẽ sớm hơn 150ms trước từ khóa chính (`triggerWord`).\n"
            "- [TASTE-02] Tỷ lệ đi nét mực đen `inkRatio` = 0.72, tô màu `hachure` = 0.28.\n"
            "- [TASTE-03] Mỗi nhãn chữ viết tay tối đa 5 từ, ưu tiên sơ đồ mũi tên nối.\n",
            encoding="utf-8"
        )
    if not LESSONS_FILE.exists():
        LESSONS_FILE.write_text(
            "# SỔ TAY KINH NGHIỆM KỸ THUẬT (VERIFIED LESSONS LEARNED)\n",
            encoding="utf-8"
        )
    if not METAPHOR_FILE.exists():
        METAPHOR_FILE.write_text(
            json.dumps({"version": "1.0.0", "metaphors": {}}, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )
    if not LOG_FILE.exists():
        LOG_FILE.write_text(
            "# NHẬT KÝ SẢN XUẤT & TIẾN HÓA (PRODUCTION LOG)\n",
            encoding="utf-8"
        )

def show_status():
    init_memory()
    taste_lines = [l for l in TASTE_FILE.read_text(encoding="utf-8").splitlines() if l.strip().startswith("- [")]
    lesson_lines = [l for l in LESSONS_FILE.read_text(encoding="utf-8").splitlines() if l.strip().startswith("### [")]
    metaphors = json.loads(METAPHOR_FILE.read_text(encoding="utf-8")).get("metaphors", {})
    learned_skills = [p.name for p in SKILLS_LEARNED_DIR.iterdir() if p.is_dir()]

    print("============================================================")
    print("🧠 TRẠNG THÁI BỘ NHỚ DỰ ÁN (PORTABLE MEMORY BANK STATUS)")
    print("============================================================")
    print(f"  • Quy tắc Gu Đạo diễn (director_taste.md)     : {len(taste_lines)} quy tắc")
    print(f"  • Bài học Kỹ thuật (lessons_learned.md)       : {len(lesson_lines)} bài học")
    print(f"  • Từ điển Ẩn dụ Hình ảnh (metaphors.json)     : {len(metaphors)} khái niệm")
    print(f"  • Kỹ năng Bố cục Đã học (skills/learned/)     : {len(learned_skills)} kỹ năng {learned_skills}")
    print("============================================================")

def add_taste_rule(rule_id: str, content: str):
    init_memory()
    lines = TASTE_FILE.read_text(encoding="utf-8").splitlines()
    updated = False
    new_line = f"- [{rule_id}] {content}"
    for i, line in enumerate(lines):
        if line.strip().startswith(f"- [{rule_id}]"):
            lines[i] = new_line
            updated = True
            break
    if not updated:
        lines.append(new_line)
    # Giữ giới hạn dưới 150 dòng (Memory Compaction)
    if len(lines) > 150:
        header = lines[:2]
        body = lines[-145:]
        lines = header + body
    TASTE_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[MEMORY UPDATED] Đã ghi nhận quy tắc đạo diễn [{rule_id}] vào {TASTE_FILE}")

def add_metaphor(keyword: str, layout: str, primitives: list, colors: list, notes: str):
    init_memory()
    data = json.loads(METAPHOR_FILE.read_text(encoding="utf-8"))
    key = keyword.strip().lower()
    existing = data["metaphors"].get(key, {"approvedCount": 0})
    data["metaphors"][key] = {
        "approvedCount": existing.get("approvedCount", 0) + 1,
        "layoutPattern": layout,
        "primitives": primitives,
        "preferredColors": colors,
        "notes": notes,
        "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    METAPHOR_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[MEMORY UPDATED] Đã lưu ẩn dụ hình ảnh cho từ khóa '{key}' vào {METAPHOR_FILE}")

def add_lesson(lesson_id: str, symptom: str, dead_end: str, golden_path: str):
    init_memory()
    entry = (
        f"\n### [{lesson_id}] ({datetime.now().strftime('%Y-%m-%d')})\n"
        f"- **Symptom:** {symptom}\n"
        f"- **Ruled-out Dead-end:** {dead_end}\n"
        f"- **Verified Golden Path:** {golden_path}\n"
    )
    with open(LESSONS_FILE, "a", encoding="utf-8") as f:
        f.write(entry)
    print(f"[MEMORY UPDATED] Đã lưu bài học kỹ thuật [{lesson_id}] vào {LESSONS_FILE}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Quản trị Bộ nhớ Tự học Di động")
    parser.add_argument("--status", action="store_true", help="Xem trạng thái bộ nhớ hiện tại")
    parser.add_argument("--add-taste", nargs=2, metavar=("RULE_ID", "CONTENT"), help="Thêm/Cập nhật quy tắc thẩm mỹ")
    parser.add_argument("--add-lesson", nargs=4, metavar=("ID", "SYMPTOM", "DEAD_END", "GOLDEN_PATH"), help="Thêm bài học kỹ thuật")
    parser.add_argument("--add-metaphor", nargs=5, metavar=("KEYWORD", "LAYOUT", "PRIMITIVES_CSV", "COLORS_CSV", "NOTES"), help="Thêm ẩn dụ hình ảnh")
    args = parser.parse_args()

    if args.status:
        show_status()
    elif args.add_taste:
        add_taste_rule(args.add_taste[0], args.add_taste[1])
    elif args.add_lesson:
        add_lesson(*args.add_lesson)
    elif args.add_metaphor:
        kw, layout, prims, cols, notes = args.add_metaphor
        add_metaphor(kw, layout, [x.strip() for x in prims.split(",")], [x.strip() for x in cols.split(",")], notes)
    else:
        show_status()
```

### 8.2. Script Tạo Giọng Đọc & Trích Xuất Thời Gian Từng Từ (`src/audio/tts_engine.py`)
Sử dụng `edge-tts` hoàn toàn miễn phí, không cần API Key, lấy chính xác mốc `offset` và `duration` của từng từ tiếng Việt:

```python
import asyncio
import json
import argparse
from pathlib import Path
import edge_tts

async def generate_voice_with_word_timings(text: str, voice: str, rate: str, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    audio_path = out_dir / "narration.wav"
    words_path = out_dir / "words_timeline.json"

    communicate = edge_tts.Communicate(text, voice, rate=rate)
    words_timeline = []

    with open(audio_path, "wb") as audio_file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_file.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                # offset và duration của edge_tts tính bằng đơn vị 100 nanoseconds (10^-7 s)
                start_ms = int(chunk["offset"] / 10000)
                duration_ms = int(chunk["duration"] / 10000)
                words_timeline.append({
                    "word": chunk["text"],
                    "startMs": start_ms,
                    "endMs": start_ms + duration_ms,
                    "durationMs": duration_ms
                })

    with open(words_path, "w", encoding="utf-8") as f:
        json.dump({
            "voice": voice,
            "fullText": text,
            "totalDurationMs": words_timeline[-1]["endMs"] + 500 if words_timeline else 0,
            "words": words_timeline
        }, f, ensure_ascii=False, indent=2)

    print(f"[OK] Đã tạo audio: {audio_path} ({len(words_timeline)} từ đã đồng bộ timestamp)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", type=str, help="Nội dung văn bản")
    parser.add_argument("--input", type=str, help="Đường dẫn file script.txt")
    parser.add_argument("--voice", type=str, default="vi-VN-NamMinhNeural")
    parser.add_argument("--rate", type=str, default="+0%")
    parser.add_argument("--output", type=str, required=True)
    args = parser.parse_args()

    content = args.text if args.text else Path(args.input).read_text(encoding="utf-8").strip()
    asyncio.run(generate_voice_with_word_timings(content, args.voice, args.rate, Path(args.output)))
```

### 8.3. Lõi Toán Học Điều Khiển Bàn Tay & Nét Vẽ (`src/engine/hand_physics.ts`)
Đảm bảo tính tất định (Deterministic) $100\%$ ở mọi khung hình $t$:

```typescript
export interface Point2D {
  x: number;
  y: number;
}

export interface CompiledStroke {
  id: string;
  d: string;                 // Chuỗi SVG Path
  length: number;            // Tổng chiều dài đường cong
  startMs: number;           // Thời điểm bắt đầu đặt bút
  endMs: number;             // Thời điểm nhấc bút
  strokeColor: string;
  strokeWidth: number;
  isFillStroke?: boolean;    // Phân biệt nét đi mực đen hay nét tô màu
}

export interface HandPose {
  visible: boolean;
  x: number;
  y: number;
  angleDeg: number;
  liftProgress: number;      // 0 = chạm giấy, 1 = nhấc cao nhất giữa 2 nét
  scale: number;
  shadowOffset: Point2D;
}

export function easeInOutSine(u: number): number {
  const clamped = Math.max(0, Math.min(1, u));
  return -(Math.cos(Math.PI * clamped) - 1) / 2;
}

export function computeHandPoseAtTime(
  timeMs: number,
  strokes: CompiledStroke[],
  pathElements: Map<string, SVGPathElement>
): HandPose {
  if (strokes.length === 0) {
    return { visible: false, x: 0, y: 0, angleDeg: 0, liftProgress: 1, scale: 1, shadowOffset: { x: 0, y: 0 } };
  }

  // 1. Kiểm tra xem thời điểm hiện tại có nằm trong một nét vẽ đang diễn ra không
  for (let i = 0; i < strokes.length; i++) {
    const s = strokes[i];
    if (timeMs >= s.startMs && timeMs <= s.endMs) {
      const pathEl = pathElements.get(s.id);
      if (!pathEl) continue;

      const u = (timeMs - s.startMs) / Math.max(1, s.endMs - s.startMs);
      const progress = easeInOutSine(u);
      const currentLen = progress * s.length;

      const pt = pathEl.getPointAtLength(currentLen);
      const delta = Math.min(4, s.length * 0.05);
      const pBefore = pathEl.getPointAtLength(Math.max(0, currentLen - delta));
      const pAfter = pathEl.getPointAtLength(Math.min(s.length, currentLen + delta));

      const angleRad = Math.atan2(pAfter.y - pBefore.y, pAfter.x - pBefore.x);
      // Dao động cổ tay tự nhiên trong khoảng [-10, +10] độ
      const wristAngleDeg = Math.sin(angleRad) * 8 + Math.cos(angleRad * 2) * 3;

      return {
        visible: true,
        x: pt.x,
        y: pt.y,
        angleDeg: wristAngleDeg,
        liftProgress: 0,
        scale: 1.0,
        shadowOffset: { x: 8, y: 12 }
      };
    }

    // 2. Kiểm tra khoảng thời gian nhấc bút di chuyển giữa nét i và nét i+1
    if (i < strokes.length - 1) {
      const nextStroke = strokes[i + 1];
      if (timeMs > s.endMs && timeMs < nextStroke.startMs) {
        const gapMs = nextStroke.startMs - s.endMs;
        // Nếu nghỉ quá 800ms thì thu bàn tay xuống dưới khung hình
        if (gapMs > 800) {
          return { visible: false, x: 0, y: 0, angleDeg: 0, liftProgress: 1, scale: 1, shadowOffset: { x: 0, y: 0 } };
        }

        const pathA = pathElements.get(s.id);
        const pathB = pathElements.get(nextStroke.id);
        if (!pathA || !pathB) continue;

        const pEnd = pathA.getPointAtLength(s.length);
        const pStart = pathB.getPointAtLength(0);
        const uLift = easeInOutSine((timeMs - s.endMs) / gapMs);
        const liftArc = Math.sin(Math.PI * uLift); // Đạt đỉnh = 1 tại uLift = 0.5

        // Quỹ đạo cong bậc 2 nhấc nhẹ lên trên
        const ctrlX = (pEnd.x + pStart.x) / 2;
        const ctrlY = Math.min(pEnd.y, pStart.y) - 35 * liftArc;

        const x = (1 - uLift) * (1 - uLift) * pEnd.x + 2 * (1 - uLift) * uLift * ctrlX + uLift * uLift * pStart.x;
        const y = (1 - uLift) * (1 - uLift) * pEnd.y + 2 * (1 - uLift) * uLift * ctrlY + uLift * uLift * pStart.y;

        return {
          visible: true,
          x,
          y,
          angleDeg: -5 * liftArc,
          liftProgress: liftArc,
          scale: 1.0 + 0.035 * liftArc,
          shadowOffset: { x: 8 + 18 * liftArc, y: 12 + 24 * liftArc }
        };
      }
    }
  }

  return { visible: false, x: 0, y: 0, angleDeg: 0, liftProgress: 1, scale: 1, shadowOffset: { x: 0, y: 0 } };
}
```

---

## PHẦN 9: CÂU LỆNH KÍCH HOẠT DÀNH CHO BẠN (COPY & PASTE VÀO ANTIGRAVITY)

### Trường hợp 1: Khởi tạo dự án lần đầu tiên trên máy hiện tại
Sau khi lưu file này vào thư mục dự án với tên `ANTIGRAVITY_WHITEBOARD_VIDEO_BLUEPRINT.md`, bạn hãy gửi câu lệnh sau cho **Antigravity (Gemini 3.8)**:

> **Prompt Khởi dựng Dự án:**  
> *"Hãy đọc toàn bộ file `ANTIGRAVITY_WHITEBOARD_VIDEO_BLUEPRINT.md` trong workspace. Chúng ta sẽ xây dựng hệ thống sản xuất video vẽ tay theo ngữ cảnh kiêm bộ nhớ tự tiến hóa (Zero-API-Key AI Whiteboard Animation & Self-Evolving Engine). Hãy thực hiện tuần tự:  
> 1. Thực thi **Chặng 1 (Milestone 1)**: Tạo `AGENTS.md`, `GLOSSARY.md`, khởi tạo cấu trúc thư mục `.agent_memory/`, `.agents/skills/` và viết hoàn chỉnh công cụ `src/memory/memory_harvester.py`.  
> 2. Thực thi **Chặng 2 & Chặng 3 (Milestone 2 & 3)**: Cài đặt các thư viện cần thiết, viết module tạo giọng đọc + word-level timestamps bằng `edge-tts`, bộ biên dịch nét vẽ SVG (`Rough.js` + `opentype.js` cho chữ tiếng Việt + `lucide-static` icons), hệ thống vật lý bàn tay cầm bút (`hand_physics.ts`), bộ trộn âm thanh tiếng bút vẽ (`sfx_mixer.py`), và CLI render video qua Playwright + FFmpeg.  
> 3. Tự động chạy bài test đầu tiên tạo ra một video mẫu dài 15 giây giải thích một khái niệm ngắn bằng tiếng Việt, trong đó giọng đọc nói tới đâu thì bàn tay vẽ hình minh họa và viết từ khóa tới đó, sau đó tự động ghi nhận bài học đầu tiên vào `.agent_memory/`."*

### Trường hợp 2: Khi bạn copy thư mục dự án sang một máy tính mới hoàn toàn
Khi dời dự án sang máy mới, bạn chỉ cần mở thư mục dự án bằng Antigravity trên máy đó và gõ đúng $1$ câu ngắn gọn:

> **Prompt Chuyển giao Máy mới (Zero-Retraining):**  
> *"Hãy đọc file `AGENTS.md` cùng toàn bộ thư mục `.agent_memory/` và `.agents/skills/learned/` để đồng bộ lịch sử học tập và gu đạo diễn của dự án từ máy cũ. Sau khi xác nhận đồng bộ xong, hãy sản xuất cho tôi video tiếp theo về chủ đề: [Nhập chủ đề hoặc kịch bản của bạn]."*

---

## PHẦN 10: ĐẶC TẢ SẢN XUẤT THỰC CHIẾN, CÁC ĐỘT PHÁ TỐI ƯU & BÁO CÁO NGHIỆM THU (PRODUCTION ADDENDUM)

Tài liệu này ghi nhận toàn bộ các kinh nghiệm thực chiến, thuật toán cải tiến và quy chuẩn vận hành được phát triển và kiểm chứng trực tiếp trên codebase thực tế của dự án `youtube_ai_edit-02` (HandDraw Studio):

### 10.1. Chuẩn hóa Bộ Rig Bàn Tay Thực Tế & Triệt Tiêu Hoàn Toàn Lỗi Cánh Tay Giả
Trong quá trình triển khai thực tế, việc sử dụng ảnh bàn tay chụp của người dùng đòi hỏi cơ chế căn chỉnh tọa độ chính xác tuyệt đối:
1. **Metadata Tọa độ Ngòi Bút (`assets/hands/hand_metadata.json`):**
   ```json
   {
     "width": 556,
     "height": 520,
     "anchor": { "x": 22, "y": 47 },
     "shadowAnchor": { "x": 22, "y": 47 },
     "defaultScale": 0.8
   }
   ```
   - Mũi bút mực nằm ở tọa độ $(22, 47)$ trên ảnh gốc $556 \times 520$.
   - Khi render, toàn bộ phép quay cổ tay $\theta(t)$ và di chuyển tịnh tiến đều lấy điểm này làm tâm quay (`transform-origin: 22px 47px`), đảm bảo ngòi bút bám sát từng pixel của đường cong SVG với sai số $< 1\text{ px}$.
2. **Kỹ thuật Làm Mềm Viền Cổ Tay (Wrist Boundary Feathering):**
   - Áp dụng bộ lọc gradient alpha 12 pixel ở chân ảnh cổ tay bằng script `scripts/generate_hand_asset.py`. Nhờ đó khi bàn tay lia qua lại trên màn hình, cạnh dưới không bị hiện đường cắt thô cứng.
3. **Triệt Tiêu Lớp Bóng Đổ Cánh Tay Trùng Lặp:**
   - Trong `src/engine/stage.html`, áp dụng `#hand-shadow-wrapper { display: none !important; }` để loại bỏ hoàn toàn hiện tượng xuất hiện cánh tay thứ hai hoặc bóng đổ nhân tạo phía sau bàn tay thật của người dùng.

### 10.2. Kiến Trúc Mã Hóa Base64 Toàn Bộ Tài Nguyên (Chromium Base64 Inlining)
Khi chạy Playwright Headless Chromium trên môi trường Windows/Linux cục bộ:
- Cơ chế bảo mật Same-Origin Policy chặn các yêu cầu nạp file cục bộ `file:///...` từ thẻ `<img>` và background CSS.
- **Giải pháp:** Trước khi nạp `src/engine/stage.html` vào Chromium, `build_video.mjs` quét toàn bộ đường dẫn ảnh (`assets/hands/`, `assets/paper/`, `assets/doodles/`) và tự động chuyển đổi thành Data URI dạng Base64 (`data:image/png;base64,...`). Nhờ vậy, 100% tài nguyên hiển thị ngay lập tức, không bao giờ bị lỗi ảnh trắng hoặc request failed.

### 10.3. Tối Ưu Tốc Độ Xuất Video: MJPEG Pipe trực tiếp vào FFmpeg (~28 - 30 FPS)
- Thay vì lưu hàng nghìn file PNG tạm ra ổ cứng hoặc dùng raw uncompressed video stream làm nghẽn I/O ổ đĩa:
- Sử dụng chuẩn `-f image2pipe -vcodec mjpeg -r 30 -i - -c:v libx264 -preset fast -crf 18 -pix_fmt yuv420p`.
- Tốc độ render trên máy CPU đạt xấp xỉ thời gian thực (28 - 30 khung hình/giây), xuất một video Full HD 1080p dài 2 phút chỉ mất chưa đầy 3 phút!

### 10.4. Khắc Phục Lỗi PyAV trong Faster-Whisper Bằng FFmpeg 16kHz Float32 Buffer
- Trong `src/audio/whisper_aligner.py`, thay vì để thư viện `faster-whisper` gọi hàm `av.open` gặp lỗi phiên bản PyAV (`open() got an unexpected keyword argument 'metadata_errors'`), module sử dụng FFmpeg pipe giải mã âm thanh 16kHz mono float32 trực tiếp sang mảng NumPy, đảm bảo độ bền vững 100% trên mọi môi trường Python.

### 10.5. Bảng Tổng Hợp Kiểm Thử & Nghiệm Thu 6 Chặng (Verification Matrix)

| Milestone / Hạng mục | Dự án Kiểm chứng | Thông số Kỹ thuật | Trạng thái Kiểm định |
| :--- | :--- | :--- | :--- |
| **Milestone 1: Bộ Nhớ Di Động** | `.agent_memory/` & `AGENTS.md` | `memory_harvester.py`, 4 phân vùng bộ nhớ, giao thức chuyển máy Zero-Retraining. | **ĐẠT 100% (Hoạt động hoàn hảo qua CLI và lệnh npm run memory)** |
| **Milestone 2: Tracer Bullet SVG** | `projects/test-milestone-1/test_milestone_1.mp4` | 5.6s, 1080p @ 30fps. Vẽ người vui vẻ + mũi tên cong + viết chữ tiếng Việt có dấu *"Xin chào Việt Nam!"* + âm thanh TTS + SFX bút vẽ. | **ĐẠT 100% (Mũi bút chính xác sai số < 1px, tiếng Việt không lỗi font)** |
| **Milestone 3: Word-Sync Audio** | `projects/demo-project/output.mp4` | 15.5s, 1080p @ 30fps. Kịch bản *Quy tắc 50/30/20*, đồng bộ từng từ khóa (*hết sạch tiền*, *chia giỏ*, *ví rỗng*). | **ĐẠT 100% (Lệch thời gian < 50ms, QA Checker 6/6 tests pass)** |
| **Milestone 4: Contextual Visual Kit & Đại dự án** | `projects/nguyen-ly-ban-tay-trai/output.mp4` | 138.5s (2 phút 18 giây), 1080p @ 30fps, 471 từ tiếng Việt, 6 phân cảnh, sơ đồ FBI, nam châm điện, động cơ điện, camera lò xo mượt mà, zoom-out toàn cảnh. | **ĐẠT 100% (Phát sóng Full HD, âm thanh sột soạt hòa âm ducking chuẩn)** |
| **Milestone 5: Raster Stream Engine** | `src/compiler/raster_stream_extractor.py` | Tách nét mực CIELAB, skeletonize 1px, giải thuật TSP 2-opt, quét màu zigzag 45 độ, bảo vệ vùng chồng lấp `protectedRegions`. | **ĐẠT 100% (Chạy độc lập và tích hợp sẵn vào stage.html)** |
| **Milestone 6: Preview Studio & Self-QA** | `src/studio/preview_editor.html`, `src/cli/qa_checker.mjs` | Preview thời gian thực tua từng ms, kiểm tra collision bounding-box, kiểm tra audio silence > 2s, kiểm tra chuẩn 1080p. | **ĐẠT 100% (Tự động phát hiện lỗi và cảnh báo an toàn)** |

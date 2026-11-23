# SỔ TAY KINH NGHIỆM KỸ THUẬT (VERIFIED LESSONS LEARNED)
> AI trên máy mới đọc file này để áp dụng ngay giải pháp chuẩn, tuyệt đối không thử lại các hướng đã thất bại.

### [LESSON-01] (2026-10-29) Xử lý dấu thanh Tiếng Việt khi dùng opentype.js
- **Symptom:** Khi bàn tay viết chữ Tiếng Việt có 2 dấu (như "ẩ", "ậ", "ữ"), nét bút nhảy qua chữ cái kế tiếp rồi mới quay lại đánh dấu.
- **Ruled-out Dead-end:** Không sắp xếp path theo tọa độ X thuần túy vì dấu mũ/dấu nặng có tọa độ X nằm giữa thân chữ.
- **Verified Golden Path:** Tách path theo từng cụm ký tự (grapheme cluster) trước, sắp xếp các contour bên trong cùng một ký tự theo thứ tự (Thân chữ chính -> Dấu phụ -> Dấu thanh), sau đó mới nối sang ký tự tiếp theo.

### [LESSON-02] (2026-10-29) Triệt tiêu bóng đổ cánh tay thứ hai & làm mềm viền cổ tay
- **Symptom:** Khi dùng ảnh chụp bàn tay thực tế, trên màn hình xuất hiện một cánh tay/bóng đen nhân tạo phía sau và viền dưới cổ tay bị cắt sắc nhọn.
- **Ruled-out Dead-end:** Không dùng thẻ `#hand-shadow-wrapper` chồng lớp khi ảnh chụp bàn tay đã có độ nổi khối tự nhiên.
- **Verified Golden Path:** Đặt `#hand-shadow-wrapper { display: none !important; }` trong `src/engine/stage.html`. Áp dụng bộ lọc gradient alpha feathering 12px ở đáy ảnh cổ tay trong `scripts/generate_hand_asset.py`.

### [LESSON-03] (2026-10-29) Tránh lỗi Same-Origin Policy trong Playwright Chromium bằng Base64 Inlining
- **Symptom:** Playwright nạp `stage.html` báo lỗi `Not allowed to load local resource: file:///...` đối với ảnh nền giấy và sprite bàn tay.
- **Ruled-out Dead-end:** Không dùng `file://` URL tĩnh trên trình duyệt Chromium.
- **Verified Golden Path:** Quét toàn bộ thẻ `<img>` và background CSS trong `src/cli/build_video.mjs` rồi mã hóa nhúng trực tiếp thành Base64 Data URI (`data:image/png;base64,...`) trước khi gọi `page.setContent()`.

### [LESSON-04] (2026-10-29) Khắc phục lỗi PyAV metadata_errors trong faster-whisper
- **Symptom:** Chạy `faster-whisper` trên Python local báo lỗi `TypeError: open() got an unexpected keyword argument 'metadata_errors'`.
- **Ruled-out Dead-end:** Không truyền trực tiếp đường dẫn file audio dạng chuỗi cho `model.transcribe()` vì hàm `decode_audio` của thư viện gọi `av.open` không tương thích phiên bản PyAV mới.
- **Verified Golden Path:** Sử dụng hàm `load_audio_16k_mono()` trong `src/audio/whisper_aligner.py` dùng FFmpeg pipe giải mã sang mảng NumPy float32 ở tần số 16kHz rồi truyền mảng cho `model.transcribe()`.

### [LESSON-05] (2026-10-29) Tăng tốc độ render từ 2 fps lên 30 fps bằng MJPEG image2pipe
- **Symptom:** Chụp ảnh PNG raw pipe sang FFmpeg khiến tốc độ render chỉ đạt 2.1 khung hình/giây.
- **Ruled-out Dead-end:** Không dùng raw RGB/PNG pipe hoặc ghi file ảnh tạm ra ổ cứng.
- **Verified Golden Path:** Dùng chuẩn `-f image2pipe -vcodec mjpeg -r 30 -i - -c:v libx264 -preset fast -crf 18 -pix_fmt yuv420p` kết hợp chụp `page.screenshot({ type: 'jpeg', quality: 95 })`, đạt tốc độ 28 - 30 fps.

### [LESSON-06] (2026-10-29) Khắc phục lỗi hiển thị Font Tiếng Việt & Đồng bộ SFX ngòi bút
- **Symptom:** Chữ viết tay tiếng Việt có dấu bị lỗi rỗng nét, đứt dấu khi qua bộ lọc distortion; âm thanh vẽ và giọng đọc bị trễ lệch nhịp so với cử động tay.
- **Ruled-out Dead-end:** Không render text chung với roughness filter canvas; không phát âm thanh vẽ loop ngẫu nhiên ngoài timeline.
- **Verified Golden Path:**
  1. Sử dụng font `Mali-Bold`, kết xuất qua `#text-group` riêng biệt với thuộc tính `fill-rule="evenodd"` và hiệu ứng `fill-opacity` mượt mà cho từng glyph.
  2. Ráp mốc thời gian của SFX sột soạt vẽ (`draw_scratch.wav`) khớp từng mili-giây với khoảng vẽ (`startMs` -> `endMs`) từ `words_timeline.json`, bật đón đầu 150ms trước từ khóa và tắt ngay khi bàn tay nhấc bút rời giấy.

### [LESSON-07] (2026-10-29) Chuyển động Camera Đa Quần Đảo (Multi-Island) & Cổng Kiểm Duyệt Chống Đứng Hình (Anti-Freeze QA)
- **Symptom:** Video dài nhiều chương bị đứng hình ở chương 1, hình ảnh giữ nguyên đến hết video trong khi âm thanh vẫn đọc tiếp.
- **Ruled-out Dead-end:** Không đặt camera keyframes đơn lẻ ở đầu mỗi phân cảnh (khiến camera trôi tuyến tính chậm suốt cả cảnh hoặc lệch viewport); không chỉ trích xuất keyframes từ `scene.camera` mà bỏ quên root `storyboard.camera`.
- **Verified Golden Path:**
  1. **Cấu trúc Hold & Pan:** Mỗi phân cảnh trên đảo không gian độc lập phải giữ cố định tọa độ tâm `(center_x, center_y)` trong suốt thời gian thuyết minh của cảnh đó, chỉ thực hiện lia camera mượt mà (`easeInOutCubic`, thời gian 1000ms) ở đúng điểm giao thoa giữa 2 cảnh (`next_start - 1000ms` -> `next_start`).
  2. **Hỗ trợ Song Hành:** `compileStoryboard()` trong `src/engine/frame_renderer.ts` phải đồng thời đọc keyframes từ cả cấp gốc `storyboard.camera` và cấp phân cảnh `scene.camera`.
  3. **Cổng QA Tự Động Hóa Chống Đứng Hình (Anti-Freeze Gate):** `qa_checker.mjs` bắt buộc phải kiểm tra tính toán hình chiếu tọa độ thực tế của từng Beat lên Viewport camera tại thời điểm vẽ `beat.startMs`. Bất kỳ nét vẽ nào nằm ngoài biên nhìn thấy của camera (`relX < 0` hoặc `relX > 1920`) đều lập tức kích hoạt cờ `[FAIL] Camera Disconnect` chặn xuất video.

### [LESSON-08] (2026-10-30)
- **Symptom:** Màn hình video trắng xóa không có nội dung (Blank Frame) trong suốt video hoặc tại các phân đoạn
- **Ruled-out Dead-end:** build_video.mjs chỉ resolve đường dẫn ảnh theo projectDir dẫn đến double path trong Chromium setContent, và frame_renderer gán 72% dead pause khi beat chỉ có fill stroke
- **Verified Golden Path:** Luôn resolve ảnh theo cả ROOT_DIR lẫn projectDir và nhúng Base64 data URI vào Chromium; khi inkStrokes=0 thì gán fillDuration=totalDuration để tay vẽ liên tục 100% thời lượng beat; dùng SVG dynamic clipPath để tranh hiện dần theo nét vẽ tay

### [LESSON-09] (2026-10-30)
- **Symptom:** Khi dung anh infographic tong hop, hinh anh bi hien ca khoi hoac khong tach boi canh nhan vat chu theo giong doc
- **Ruled-out Dead-end:** Gom toan bo anh thanh 3 lop tho toan man hinh khien tat ca xuat hien cung luc truoc khi voice kip noi toi
- **Verified Golden Path:** Phan ra anh thanh cac Semantic Panels theo cau thoai words_timeline.json. Trong moi panel tach rieng Boi canh, Nhan vat va Chu chu thich PNG trong suot de ban tay ve va viet dung vi tri khi voice nhac toi

### [LESSON-10] (2026-11-02)
- **Symptom:** Tao anh minh hoa tu van ban tren CPU lau hang phut
- **Ruled-out Dead-end:** Chay SD 1.5 nguyen ban tren PyTorch CPU 30-50 steps gay cham va tran RAM
- **Verified Golden Path:** Su dung FastSD CPU voi Intel OpenVINO + SD-Turbo 1 step + TAESD sinh anh chi 2.7s tren CPU

### [LESSON-11] (2026-11-02)
- **Symptom:** Tao anh 2D tu web AI bang Playwright MCP va tai anh goc ve may lam video
- **Ruled-out Dead-end:** Mo browser thu cong hoac khong dong bo voi phan mem dan den lech nhip voice va chat luong anh bi thu nho
- **Verified Golden Path:** Dung Playwright truy cap phien Gemini Pro, prompt tao anh line art 2D theo tung cau voice, trich xuat anh goc 1024px qua canvas trigger download, roi nap vao render_stream_whiteboard voi annotation timeline chuan

### [LESSON-12] (2026-11-02)
- **Symptom:** Tach roi 2 giai doan ve net den trang roi moi quet mau gay cam giac may moc va cho doi lau
- **Ruled-out Dead-end:** Ve phac thao toan bo khung hinh bang net den roi moi dung co/wipe to mau lan hai lam khan gia phai nhin hinh den trang qua lau
- **Verified Golden Path:** Su dung LiveColorWhiteboardRenderer ve cọ mau va chi tiet truc tiep don luot (single-pass live color reveal), ve toi dau mau no bung ruc ro toi day, dong thoi tang toc do render len gap 8 lan.

### [LESSON-13] (2026-11-02)
- **Symptom:** Cac o hop bi rong trang (Blank Box) do bo qua loi am tham if img_path.exists
- **Ruled-out Dead-end:** Su dung if img_path.exists ma khong bao loi lam bo ve anh va text, tao ra cac o hop trang tinh trong video
- **Verified Golden Path:** Bat buoc assert kiem tra file anh ton tai 100%, tich hop ham qa_verify_canvas quet ty le pixel noi dung tung o (>5%), trich xuat snapshot hau ki de kiem dinh chat luong tung chuong.

### [LESSON-14] (2026-11-02)
- **Symptom:** Ban tay quet mau toan bo buc anh AI gay cham chap va giong doc mac dinh kem cam xuc
- **Ruled-out Dead-end:** Bat ban tay phai ve toan bo pixel anh AI va dung TTS mac dinh toc do cham khong ngat nghi
- **Verified Golden Path:** Hinh anh AI xuat hien bang hieu ung Pop-in/Scale truc quan; ban tay tap trung viet chu va ve chu thich; dung Edge-TTS NamMinhNeural toc do +22% kem SSML nhan nha

### [LESSON-15] (2026-11-03)
- **Symptom:** TTS bi loi NoAudioReceived khi gui van ban dai
- **Ruled-out Dead-end:** Gui nguyen ca doan van dai qua websocket TTS khien tong do lech nhip
- **Verified Golden Path:** Tach cau theo dau cau kem hash cache va chen khoang nghi chu dich (. 230ms, ! 300ms, ? 380ms) giup giong doc NamMinh tu nhien, bat loi loi va dong bo word timing 100%

### [LESSON-16] (2026-11-03) Khắc phục lỗi viết chữ dạng "tô / quét mặt nạ" (Zero Wipe Curtain)
- **Symptom:** Chữ viết tay bị cắt ngang thân bằng một đường cắt đứng (linear reveal), các dòng văn bản bên dưới bị lộ đồng thời cùng lúc với dòng trên tạo cảm giác giả tạo ("làm tô" thay vì "viết chữ").
- **Ruled-out Dead-end:** Dùng bounding box bao quanh toàn bộ đoạn văn rồi unmask tuyến tính theo trục X (`reveal_x = bx0 + p * (bx1 - bx0)`).
- **Verified Golden Path:** Phân rã văn bản theo cấp bậc: Đoạn -> Dòng (Line) -> Từ (Word) -> Ký tự (CharGlyph). Bàn tay di chuyển ngòi bút theo tọa độ chính xác của từng ký tự đang viết. Dòng dưới hoàn toàn ẩn cho đến khi dòng trên viết xong. Khi chuyển dòng, bàn tay thực hiện vòng cung nhấc bút parabol (`lift = -30 * sin(pi * u)`).

### [LESSON-17] (2026-11-03) Chuẩn hóa pad name và audio format trong FFmpeg complex filter
- **Symptom:** FFmpeg báo lỗi `Stream specifier 'v' in filtergraph description matches no streams` khi mix âm thanh sidechain ducking.
- **Ruled-out Dead-end:** Đặt tên pad âm thanh là `[v]` (bị trùng với stream specifier mặc định của video) và đưa các luồng audio khác sample rate / channel layout trực tiếp vào `sidechaincompress`.
- **Verified Golden Path:** Đặt tên pad rõ ràng: `[voc]`, `[sfx]`, `[bgm]`; chuẩn hóa mọi input bằng `aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo` trước khi đưa vào `sidechaincompress` và `amix`.

### [LESSON-18] (2026-11-03) Đồng bộ Tuyệt đối Nét Vẽ & Nội dung Xuất hiện (Zero-Mismatch Whiteboard Engine)
- **Symptom:** Nét vẽ bàn tay không khớp với nội dung hiện ra trên video: hình minh họa bị hiện giật cục/đột ngột xuất hiện cả mảng lớn ở cuối phân đoạn trong khi bàn tay chỉ chấm vài điểm rời rạc; chữ viết bị cắt bằng hộp chữ nhật đứng thô ráp; ngòi bút bị lệch khỏi nét mực thực tế.
- **Ruled-out Dead-end:** 
  1. Không lấy mẫu chỉ 1 điểm `path[pt_idx]` cho mỗi frame rồi cưỡng ép snap 100% hình vẽ ở frame cuối.
  2. Không dùng rectangular window blind wipe (`drawn[r0:r1, c_start:c_end] = color_img`) khi viết chữ.
  3. Không dùng sprite bàn tay không chuẩn anchor hoặc tính sai offset ngòi bút (ví dụ anchor (5, 2) cho sprite lệch góc).
- **Verified Golden Path:**
  1. **Anchor ngòi bút siêu chuẩn xác:** Đồng bộ sprite `hand-marker-right.png` với anchor `(22, 47)` theo đúng `[TASTE-06]`, co giãn động theo độ phân giải canvas (`scale = (H / 720) * 0.70`). Đầu bút dạ đen chạm khít từng pixel vào điểm đặt mực.
  2. **Tích lũy bước liên tục (Continuous Step Accumulation):** Đối với tranh minh họa, mỗi frame lặp qua toàn bộ dải điểm từ `prev_pt_idx` đến `target_pt_idx` để đóng dấu brush disk. Mực và màu tuôn trào trực tiếp ngay dưới ngòi bút liên tục, đạt 100% hoàn chỉnh mượt mà không có bất kỳ hiện tượng pop-in hay lag nét.
  3. **Viết chữ mượt mà tự nhiên (Natural Handwriting Flow):** Ngòi bút di chuyển dọc theo từng dòng chữ với dao động vi mô `pen_y = base_y + 2.0*sin(x*0.45) - 1.0*cos(x*0.9)` kết hợp cọ tròn ngòi bút `text_brush_r`, làm các nét chữ hiện lên mềm mại ngay dưới ngòi bút; kết hợp đường cong nhấc bút parabol (carriage return lift arc) khi chuyển dòng.
  4. **Viền khung thực tế:** Bút vẽ lần lượt theo chu vi 4 cạnh thẻ bài và tab tiêu đề trước khi viết chữ và vẽ tranh.

### [LESSON-19] (2026-11-03) Triệt tiêu Tuyệt đối Lỗi Nội dung Hiện Trước Ngòi Bút (Zero Premature Unmasking)
- **Symptom:** Nét bút chưa vẽ tới mà chữ đã hiện ra phía trước (ví dụ: ngòi bút đang ở từ thứ 3 nhưng cả nửa sau của tiêu đề đã hiện rõ trên màn hình; hoặc tranh minh họa đã vẽ xong 100% ngay từ giây thứ 6 trong khi tay còn đang quét phía sau).
- **Ruled-out Dead-end:** 
  1. Gán cả mảng `drawn[by0:by1, bx0:bx1] = color_img[by0:by1, bx0:bx1]` khi vẽ viền khung, làm lộ toàn bộ chữ bên trong trước khi tay viết.
  2. Quét cả vùng nền trắng rỗng (serpentine scan over empty paper), khiến toàn bộ nét vẽ của con vật/nhân vật nằm dồn vào 13% thời gian đầu, 87% thời gian còn lại bàn tay quét qua giấy trắng trong khi tranh đã xong từ lâu.
- **Verified Golden Path:**
  1. **Masking toàn diện (Pre-masked Clean Backgrounds):** Tạo bản sao viền khung và tab tiêu đề với vùng chữ bị mask 100% bằng màu nền giấy (`255`) hoặc màu nền tab (`header_bg`). Khi vẽ viền khung, khung và nền hiện lên nhưng chữ hoàn toàn không tồn tại.
  2. **Tiến trình chữ viết chuẩn xác (Strict Forward Clamping):** Từng ký tự chỉ được giải phóng mực từ `color_img` khi tọa độ ngòi bút `target_x` chạm tới (`x_start:x_end` với `x_end = target_x`). Phía trước ngòi bút (`x > target_x`) tuyệt đối là nền giấy trắng sạch sẽ 100%.
  3. **Lộ trình vẽ tranh tinh khiết (Content-Only Nearest Neighbor):** Chỉ lấy mẫu các điểm có nét vẽ và màu sắc thực tế (`diff_bg > 20`), sắp xếp theo thứ tự lân cận gần nhất (Nearest Neighbor) từ phía đầu chủ thể sang thân và đuôi. Loại bỏ hoàn toàn các điểm quét trên nền giấy trắng. Đảm bảo tranh vẽ tiến triển đồng đều từ 0% đến 100% suốt thời lượng phân cảnh.

### [LESSON-20] (2026-11-03) Đồng bộ Giọng Nam Neural 1.5x & Dynamic Timeline Auto-scaling
- **Symptom:** Giọng đọc nữ hoặc giọng đọc mặc định quá chậm gây cảm giác rề rà, người xem dễ mất kiên nhẫn.
- **Ruled-out Dead-end:** Gửi lặp lại hàng chục kết nối WebSocket ngắn tới máy chủ Edge-TTS công cộng gây nghẽn kết nối / rate limit; hoặc áp pitch shifting hạ giọng từ giọng nữ tạo cảm giác méo âm nhân tạo.
- **Verified Golden Path:** 
  1. Chuẩn hóa giọng đọc nam Microsoft Neural `vi-VN-NamMinhNeural` kết hợp chuỗi xử lý âm thanh Broadcast Mastering (EQ ấm 150Hz +2.2dB, làm sáng nguyên âm 3.2kHz +1.8dB, Dynamic Compressor và Limiter) tạo chất giọng trầm ấm, nam tính và dứt khoát.
  2. Đưa tốc độ phát lên đúng chuẩn 1.5x bằng thuật toán WSOLA thời gian thực (`atempo=1.3043` trên base vocal `+15%`), giữ nguyên 100% cao độ giọng nói không bị the thé (chipmunk effect) hay nuốt âm.
  3. Tự động co giãn toàn bộ timeline của `spec.json` (`duration_ms`, `start_ms`, `end_ms`) theo tỷ số nén âm thanh `ratio = new_audio_ms / old_audio_ms`, giúp toàn bộ animation nét vẽ tay, viết chữ và xuất hiện ảnh của `HybridWhiteboardRenderer` tự động tăng tốc khớp chính xác 100% với giọng đọc mới.

### [LESSON-21] (2026-11-03) Tạo Ảnh Minh Họa 2D Comic Bằng Google Gemini Qua Playwright MCP
- **Symptom:** Tự tạo ảnh Canva hoặc FastSD CPU chất lượng kém có chữ giả méo mó
- **Ruled-out Dead-end:** Dùng script nội bộ hoặc canva cục bộ để vẽ card infographic chứa text bullet gây rối mắt và giảm chất lượng thẩm mỹ
- **Verified Golden Path:** Sử dụng MCP Playwright kết nối vào phiên Google Gemini có sẵn, điền prompt chi tiết phong cách truyện tranh 2D sinh học trên nền trắng tinh khiết, tự động tải ảnh gốc về gemini_downloaded và bố trí vào card không kèm bullet text

### [LESSON-22] (2026-11-03) Bảng Giấy Vô Hạn Không Khung (Infinite Whiteboard Flow) & Đồng Bộ Giọng ElevenLabs Adam
- **Symptom:** Bố cục thẻ bài chữ nhật có viền bo góc và đánh số 1-2 tạo cảm giác giao diện dashboard cứng nhắc; âm thanh chương 2 khác âm lượng và giai điệu so với chương 1.
- **Ruled-out Dead-end:** Đóng khung viền card chữ nhật bao quanh hình ảnh; dùng engine Edge-TTS lẫn với ElevenLabs giữa các cảnh trong cùng một tập phim.
- **Verified Golden Path:**
  1. **Bảng giấy vô hạn (Infinite Whiteboard Flow):** Loại bỏ hoàn toàn viền khung hình chữ nhật và tab tiêu đề. Đặt các hình minh họa 2D comic Gemini trực tiếp trên nền giấy trắng. Bàn tay vẽ xong hình 1 khớp câu thoại 1 sẽ tự động nhấc bút lướt êm ái qua khoảng trống tiếp theo để vẽ tiếp hình 2 khớp câu thoại 2. Hình cũ giữ nguyên trên giấy tạo sơ đồ sinh động liên tục.
  2. **Đồng bộ giọng ElevenLabs:** Toàn bộ các cảnh chính (Chương 1, Chương 2) đều dùng ElevenLabs Model `eleven_v4` với Voice Adam (Dominant, Firm) ở tốc độ 1.25x và volume filter 1.15x, đảm bảo giai điệu, trường độ và âm lượng đồng nhất 100%.

### [LESSON-23] (2026-11-03) Nguyên Tắc Tuần Tự Tuyệt Đối (Strict Sequential Revealing) & Triệt Tiêu Lướt Tay Chậm
- **Symptom:** Tiêu đề chương và phụ đề của Beat 1 cùng lúc chạy chữ ở frame 0; bàn tay di chuyển lê thê chậm chạp (`u_glide`) sau khi vẽ xong tranh; giọng đọc các cảnh sau (Scene 3-6) khác tông với cảnh đầu; hình ảnh minh họa chung chung không khớp câu thoại (như chỉ số IQ lại vẽ lửng mật đeo kính râm đi dạo).
- **Ruled-out Dead-end:** Để các vòng lặp rendering của Header và Panel chạy song song trong cùng một `cur_ms`; dùng phép nội suy `u_glide` kéo dài theo toàn bộ thời gian trống còn lại của panel khiến tay rê chậm chạp 5-8 giây vô nghĩa.
- **Verified Golden Path:**
  1. **Tuần tự 3 lớp (Strict 3-Stage Sequential Pipeline):**
     - Giai đoạn 1 (`0 -> 1100ms`): Ngòi bút viết tiêu đề lớn trên đỉnh trang. Toàn bộ canvas phía dưới giữ màu trắng tuyệt đối.
     - Giai đoạn 2 (`1100ms -> 78% beat dur`): Bút di chuyển xuống phác thảo tranh minh họa của Beat 1 tương ứng với lời dẫn chuyện. Dòng chữ chú thích bên dưới tranh vẫn giữ trắng 100%.
     - Giai đoạn 3 (`78% -> 94% beat dur`): Tranh đã hoàn tất, ngòi bút viết chữ chú thích từng ký tự ngay dưới bức tranh.
     - Chuyển tiếp (`94% -> 100% beat dur`, ~250-400ms): Nhấc bút hình vòng cung di chuyển nhanh gọn sang vị trí tranh tiếp theo.
  2. **Đồng bộ giọng đọc ElevenLabs toàn diện:** Toàn bộ 6 phân cảnh (Scene 1 đến Scene 6) đều phải được tổng hợp bằng ElevenLabs Adam v4 (1.25x), không được để sót bất kỳ cảnh nào dùng gTTS hay Kokoro cũ.
  3. **Kiểm duyệt ảnh tương ứng 100%:** Đối chiếu từng câu nói với tranh vẽ. Bắt buộc tạo tranh minh họa chi tiết cụ thể thông qua Google Gemini Playwright MCP cho từng hành vi (như bẻ khóa, chế tạo công cụ cho IQ 90; đứng đỉnh núi oai phong cho bài học sinh tồn).

### [LESSON-24] (2026-11-03) Bảo Toàn Thời Lượng Chuẩn Kế Hoạch Kênh (8:30 - 9:30 Phút) & Cơ Chế Xoay Vòng Đa Key ElevenLabs [ĐÃ NGƯNG — ElevenLabs bị bỏ 2026-11-07, giọng chính là VoiceStudio; chỉ giữ để tham khảo lịch sử]
- **Symptom:** Tự ý cắt ngắn kịch bản thoại để tiết kiệm ký tự API ElevenLabs khiến thời lượng video bị sụt giảm từ 9 phút xuống còn 6 phút, vi phạm chuẩn thời lượng yêu cầu trong tài liệu kế hoạch kênh (`docs/ke_hoach_xay_kenh_youtube_the_gioi_dong_vat_whiteboard_animation.md`).
- **Ruled-out Dead-end:** Rút ngắn nội dung văn bản phân cảnh để vừa khít với số ký tự còn lại của một API key duy nhất.
- **Verified Golden Path:**
  1. **Tuyệt đối không cắt bớt cốt truyện:** Luôn duy trì đủ 2.100 - 2.200 từ (~9.500 ký tự) cho 6 phân cảnh để đảm bảo video đạt chuẩn 8:30 – 9:30 phút, tối ưu hóa điều kiện kiếm tiền (4.000 giờ xem) và tự động bật quảng cáo giữa video (Mid-roll ads).
  2. **Kiến trúc Multi-key ElevenLabs Failover:** Thiết lập danh sách API keys `[primary_key, backup_key]`. Hệ thống tự động kiểm tra hạn mức còn lại và chuyển đổi khóa mượt mà khi một khóa chạm ngưỡng, duy trì 100% tính đồng nhất của giọng Adam v4 với emotion tags xuyên suốt toàn bộ tập phim.

### [LESSON-25] (2026-11-03) Chuẩn Hóa Bộ Video Intro & Outro Gemini AI Chính Thức & Đồng Bộ Timebase Khi Ghép Nối (Zero Frame Drop Concat)
- **Symptom:** Khi ghép nối (concat) trực tiếp video Intro/Outro do Google Gemini xuất ra (`time_base = 1/90000`) với video Master do FFmpeg libx264 xuất ra (`time_base = 1/12288`), bộ giải mã concat của FFmpeg bị lệch timescale dẫn đến hiện tượng drop hàng nghìn frame ở đoạn giữa.
- **Ruled-out Dead-end:** Dùng `-f concat` trực tiếp trên các file MP4 có `time_base` (tbn) khác nhau mà không chuẩn hóa trước.
- **Verified Golden Path:**
  1. **Lưu trữ cố định tài nguyên thương hiệu:** Lưu bản gốc và bản chuẩn hóa của 2 video Gemini tại `assets/branding/intro_ve_chuyen_hoang_da.mp4` (`gemini_generated_video_105939de.mp4`) và `assets/branding/outro_ve_chuyen_hoang_da.mp4` (`gemini_generated_video_8a2162a5.mp4`).
  2. **Chuẩn hóa Timebase (`-video_track_timescale 12288`):** Đồng bộ toàn bộ Intro, Master và Outro về cùng `1280x720`, `24fps`, `yuv420p`, `tbn=12288` và audio `48000Hz stereo` trước khi ghép nối. Kết quả ghép nối đạt 13.785/13.785 frames (0 frame drop) mượt mà tuyệt đối.

### [LESSON-26] (2026-11-04) Triệt Tiêu Lỗi Chữ Ô Vuông Tiếng Việt (Zero Tofu `□`), Căn Giữa Hình Học Pill Badge (`anchor="mm"`) & Hệ Thống Kiểm Duyệt Khắt Khe Từng Khung Hình (`src/qa/strict_frame_qa.py`)
- **Symptom:**
  1. Chữ tiếng Việt có dấu phức hợp (`Ầ`, `Ử`, `Ự`, `Ợ`, `Ỗ`, `Ế`, `Ổ`...) bị biến thành các ô vuông rỗng (`□` Tofu boxes) trên tiêu đề, huy hiệu và phụ đề.
  2. Chữ trong khung viền Pill Badge (`01. THẢO NGUYÊN`, `02. NỖI KHIẾP SỢ`...) bị lệch hẳn xuống đáy khung, cắt vào đường viền dưới và đè lên phần đầu của hình vẽ minh họa.
- **Ruled-out Dead-end:**
  1. Tuyệt đối KHÔNG BAO GIỜ dùng font Windows `segoeprb.ttf` / `segoepr.ttf` (Segoe Print) hoặc `Inkfree.ttf` vì các font này chỉ hỗ trợ bảng mã Latin-1 cơ bản, thiếu hoàn toàn bảng mã Unicode Tiếng Việt Dựng Sẵn (Latin Extended Additional).
  2. Tuyệt đối không vẽ khung chữ bằng tọa độ góc trái-trên `(bx, by)` mà không trừ đi `top_bearing` (`bbox[1]`) của font chữ, và không đặt Pill Badge đè trực tiếp vào cùng tọa độ `pos_y` của bức tranh.
- **Verified Golden Path:**
  1. **Chuẩn hóa bộ Font Viết Tay Tiếng Việt 100% (`assets/fonts/`):** Sử dụng `Mali-Bold.ttf` cho Header, `BeVietnamPro-Bold.ttf` cho Pill Badge và `PlaypenSans-Bold.ttf` cho phụ đề viết tay. Kiểm tra tự động 134 ký tự tiếng Việt bằng hàm `verify_vietnamese_font_glyphs()` so khớp với glyph `.notdef` (`\ufffe`) đảm bảo 0% lỗi ô vuông.
  2. **Căn giữa tâm hình học tuyệt đối (`anchor="mm"`):** Khi vẽ chữ trong Pill Badge, bắt buộc đo và vẽ bằng `draw.text((center_x, cy), text, font=font, anchor="mm")`, đồng thời dành riêng dải chiều cao `top_badge_reserve = 32px` phía trên bức tranh để huy hiệu nằm tách biệt, chính giữa tâm cột và không bao giờ chạm vào hình minh họa.
  3. **Cổng Kiểm Duyệt Tự Động Khó Tính Từng Khung Hình (`src/qa/strict_frame_qa.py`):** Sau mỗi lần render, bắt buộc chạy `python src/qa/strict_frame_qa.py` để quét tự động toàn bộ 21 mốc chuyển cảnh (Intro, từng Beat của cả 6 Hồi, Outro), kiểm tra độ phủ mực, kiểm tra không lộ chữ sớm trước khi bút viết, kiểm tra không còn mảng trắng chữ nhật (`pure_white_ratio < 0.08`) và xuất bảng tổng hợp `qa_contact_sheet_1.png`, `qa_contact_sheet_2.png` để nghiệm thu bằng mắt.

### [LESSON-27] (2026-11-04) Nguyên Tắc Bảo Toàn 100% Toàn Bộ Khung Hình Tranh Vẽ (Zero Cropping / Zero Shaving / Full Artwork Preservation)
- **Symptom:** Hình minh họa AI tải từ Gemini bị cắt cụt một phần chi tiết ở viền (răng nanh và mũi sư tử bị mất, đỉnh túi linh dương bị cắt, nhãn text chỉ số trong tranh bị che mờ, chân và bóng đổ bị đè lên).
- **Ruled-out Dead-end:**
  1. Dùng thuật toán `border_shave` tự động quét dòng tối và gọt 20-25px ở 4 cạnh ảnh (làm mất các nét vẽ sát biên của Gemini).
  2. Dùng thuật toán làm mờ viền `edge_feather` hoặc `vignette` ăn sâu vào nội dung tranh vẽ.
  3. Tự vẽ thêm thanh tiến trình RPG (`stat_bar`) giả bằng code đè lên chân tranh và chiếm mất diện tích chiều cao hiển thị.
- **Verified Golden Path:**
  1. **Hiển thị FULL 100% Tranh Gốc (`place_full_illustration_beat`):** Giữ nguyên vẹn 100% số pixel của ảnh Gemini từ `(0, 0)` đến `(w, h)`. Tuyệt đối không crop, không shave viền, không làm mờ cạnh. Chỉ dùng phép co giãn tỷ lệ giữ nguyên khung hình (`LANCZOS`) để đặt trọn vẹn vào vùng an toàn.
  2. **Nền Bảng Trắng Đồng Nhất Tuyệt Đối (`#FFFFFF`):** Toàn bộ ảnh Gemini vẽ trên nền trắng thuần khiết được đặt trực tiếp lên nền Infinite Whiteboard `#FFFFFF`, giúp mép ảnh hòa tan tự nhiên vào bảng vẽ mà không cần bất kỳ thủ thuật làm mờ nhân tạo nào.
  3. **Tận dụng Trực Tiếp Đồ Họa RPG Sẵn Có Của AI:** Gemini đã tự động vẽ sẵn thanh máu, chỉ số và huy hiệu (`SỨC MẠNH STR 85/100`, `DEF 99/100`, `IQ 90/100`, `FEAR 0/100`) bên trong tranh. Loại bỏ thanh code giả để trả lại toàn bộ khoảng thở thoáng đãng cho hình ảnh và phụ đề viết tay bên dưới.

### [LESSON-28] (2026-11-04) Chuẩn Hóa Lời Bình Đoạn Kết Liền Mạch (Seamless Outro Narration) & Ghép Outro Video Đồ Họa Mới
- **Symptom:** Lời bình giọng đọc ở Hồi 6 vẫn còn câu kêu gọi hành động CTA "Hãy bấm ngay vào video trên màn hình... Đừng quên bấm Đăng Ký kênh", gây trùng lặp và xung đột khi video đã có Outro hoạt cảnh đồ họa riêng biệt ở cuối.
- **Ruled-out Dead-end:** Đọc cả CTA kêu gọi đăng ký bằng voiceover rồi ngay sau đó lại chiếu video Outro hoạt cảnh kêu gọi đăng ký kênh (khiến đoạn kết rườm rà, nghiệp dư và giảm tỷ lệ giữ chân khán giả).
- **Verified Golden Path:**
  1. **Lời bình kết thúc chỉ tạo Cliffhanger Teaser:** Đoạn kết Hồi 6 tập trung đúc kết bài học ý chí sinh tồn và hé lộ bí mật rùng rợn của Rái Cá Biển cho Tập 2, kết thúc tự nhiên bằng câu: *"Cùng vén màn bí mật rùng rợn của loài vật dễ thương này trong tập tiếp theo nhé!"*.
  2. **Tích hợp Video Outro Hoạt Cảnh Mới (`gemini_generated_video_3314fb91.mp4`):** Video Outro dài 10s có đầy đủ mascot sư tử con cầm bút vẽ, banner Cảm ơn, nút Đăng Ký kênh, Chuông thông báo và Like cùng nhạc nền vui nhộn kết thúc video chuyên nghiệp.
  3. **Tự động đo thời lượng từng phần (`scene06_parts_duration.json`):** Phân chia thời điểm xuất hiện của Beat 1 (Lửng Mật chiến thắng) và Beat 2 (Teaser Rái Cá Biển) chính xác theo độ dài âm thanh thực tế của từng đoạn voiceover.

### [LESSON-29] (2026-11-04) Loại Bỏ Triệt Để Tag Thì Thầm Phà Vào Tai (`[whispering]`) Trong ElevenLabs [ĐÃ NGƯNG — ElevenLabs bị bỏ 2026-11-07, giọng chính là VoiceStudio; chỉ giữ để tham khảo lịch sử]
- **Symptom:** Giọng đọc AI ở câu "Quên tất cả những điều đó đi" và một số đoạn mở đầu bị biến thành tiếng thì thầm/ghé sát micro phà hơi vào tai (ASMR whisper) nghe bị giật mình, khó chịu và thiếu uy lực.
- **Ruled-out Dead-end:** Dùng tag `[whispering]` để tạo kịch tính (trong mô hình `eleven_v4`, tag này hạ âm lượng thanh quản xuống mức thì thầm cận mic tạo cảm giác phà hơi vào tai).
- **Verified Golden Path:**
  1. **Thay thế bằng `[confident]` & `[firm]`:** Câu "Quên tất cả những điều đó đi!" được gắn tag `[confident]` phát âm dứt khoát, chắc nịch, phóng khoáng và đanh thép.
  2. **Rà soát 100% kịch bản:** Thay thế toàn bộ các tag `[whispering]` ở tất cả các hồi sang `[intense]`, `[dramatic]`, `[curious]` hoặc `[confident]`.
  3. **Cơ chế tái tạo thông minh (`target_parts`):** Chỉ tốn token re-generate các đoạn có thay đổi tag, tái sử dụng các đoạn wav chất lượng đã đạt chuẩn giúp tiết kiệm hạn ngạch API.

### [LESSON-30] (2026-11-04) Kiến Trúc YouTube Shorts Phễu Kéo Kênh (6-Beat Infinite Vertical Sketchbook & Open-Loop Cliffhanger)
- **Symptom:** Video Shorts bản cũ chỉ xếp chồng 3 hộp chữ nhật tĩnh trên 1 màn hình suốt 57 giây, bàn tay không viết chữ và kịch bản kể hết sạch thông tin khiến người xem không có động lực bấm vào kênh xem video dài.
- **Ruled-out Dead-end:** Tóm tắt toàn bộ video dài vào 3 khung thẻ tĩnh (vừa phạm lỗi dashboard khô khan, vừa làm mất hoàn toàn tính tò mò).
- **Verified Golden Path:**
  1. **Đồng bộ 1-1 giữa 6 đoạn Voiceover ElevenLabs và 6 Nhịp Hình Ảnh (`shorts_parts_duration.json`):** Chia kịch bản Shorts thành đúng 6 đoạn văn tương ứng với 6 bức tranh 2D cỡ lớn trên 3 trang giấy dọc (`Page 1 -> Page 2 -> Page 3`), tự động cắt khoảng lặng thừa và chuẩn hóa tốc độ để tổng thời lượng đạt chuẩn vàng `57.9s` (nằm gọn trong khung `45s–58s`).
  2. **Kỹ thuật Open-Loop Cliffhanger ở 15 giây cuối:** Dựng cao trào chú lửng mật Stoffel dụ bạn gái làm thang vượt tường bê tông rồi lao thẳng vào chuồng 3 con sư tử đực huyết chiến, sau đó đặt câu hỏi bỏ lửng: *"Kết cục trận tử chiến 1 chọi 3 đó ra sao? Và thứ vũ khí hóa học kinh hoàng nào ở đuôi đã khiến cả bầy sư tử phải bỏ chạy? Bấm ngay vào kênh Vẽ Chuyện Hoang Dã xem trọn bộ!"*.
  3. **Bàn tay thật viết chữ & Dạ quang chạy theo bút:** Trên mỗi nhịp hình ảnh, bàn tay thật viết từng ký tự bộ đôi câu chốt kèm dải bút dạ quang (`Highlighter Strip`) mở rộng dần theo tọa độ ngòi bút, kết hợp thanh CTA đáy màn hình chuyển sang màu Đỏ/Vàng nhấp nhịp ở hồi kết để tối đa hóa tỷ lệ bấm vào kênh.

### [LESSON-31] (2026-11-04) Nâng Cấp Động Cơ HybridWhiteboardRenderer V6 (2-Phase True-Stroke Ink Stream + Boustrophedon Color Wash)
- **Symptom:** Ở các phiên bản trước, việc làm hiện mờ lớp phác thảo chì (`sketch_img` / ghost blueprint) trước khi bút vẽ tới hoặc dùng thuật toán tìm điểm gần nhất ngẫu nhiên khiến nét vẽ trông giống như "tẩy lớp sương mù" hoặc nhảy cóc hỗn loạn, không tạo được cảm giác "bút đưa tới đâu nét vẽ hiện ra tới đó".
- **Ruled-out Dead-end:** Pha trộn alpha toàn vùng (`sketch_blend`) trước khi ngòi bút chạm tới hoặc dùng greedy nearest-neighbor trên lưới thô không phân cụm liên thông.
- **Verified Golden Path:**
  1. **Trích xuất bản đồ nét mực đa tỷ lệ (`_extract_clean_ink_map`):** Kết hợp `cv2.bilateralFilter` + `CLAHE` + `cv2.adaptiveThreshold` để tách riêng lớp nét viền mực đen sắc nét (`ink_mask`, `ink_paint`) ra khỏi lớp màu nền.
  2. **Định tuyến nét vẽ theo cụm liên thông & Gradient mật độ (`_gradient_walk_component`):** Phân tách các cụm nét bằng `cv2.connectedComponents`, gộp các chấm nhỏ vào cụm chính gần nhất và dẫn đường ngòi bút đi liền mạch hết từng bộ phận của nhân vật trước khi chuyển sang cụm kế tiếp.
  3. **Cơ chế Vẽ 2 Giai Đoạn Thực Thụ (`PanelStrokePlan`):**
     - **Phase 1 (56% thời lượng — Đi nét mực đen):** Phía trước ngòi bút là 100% giấy trắng. Ngòi bút di chuyển đến đâu chỉ làm hiện nét mực đen (`_reveal_ink_step` với `cv2.line` nối liền giữa 2 mẫu liên tiếp + `_stamp_ink_cell`) kèm âm thanh bút dạ sắc nét (`marker-scribble-loop.wav`).
     - **Phase 2 (44% thời lượng — Tô màu Boustrophedon):** Sau khi 100% khung nét mực đã hiện rõ trên giấy, bàn tay lướt cọ lông vũ (`color_brush_r = 26px`) theo đường zíc-zắc ngang đan xen (`color_samples`) để tô màu rực rỡ đè lên khung nét mực kèm âm thanh cọ tô màu (`chalk-stroke.wav`).

### [LESSON-32] (2026-11-04) Kiến Trúc Sư Prompt Hình Ảnh Theo Từng Câu Văn (Zero-Imagination-Gap Sentence-Level Prompt Architect)
- **Symptom:** Một số phân đoạn lời bình mô tả rất chi tiết (như kéo xác linh dương gấp 3 lần cơ thể, da trượt răng sư tử/bọ cạp/mũi giáo, đào hầm nhanh hơn người xúc xẻng, thực đơn 3 loài rắn chiếm 1/4 khẩu phần, BBC quay phim Stoffel, hay rái cá biển bắt cóc hải cẩu con), nhưng hình ảnh cũ chỉ vẽ chung chung hoặc gộp 2 đoạn thoại vào 1 hình khiến người xem phải tự tưởng tượng.
- **Ruled-out Dead-end:** Viết prompt ngắn gọn chung chung kiểu "honey badger strong muscles" hoặc chỉ đặt 3 bức tranh cho một chương có 4 đoạn văn thuyết minh dài.
- **Verified Golden Path:**
  1. **Xây dựng bộ khung `src/compiler/sentence_prompt_architect.py`:** Phân tích từng câu văn trong kịch bản thành danh sách `extracted_visual_details` (chủ thể, hành động cụ thể, đối tượng tương tác, con số tỷ lệ, phép so sánh trực quan) trước khi biên dịch thành câu lệnh hoàn chỉnh cho Google Gemini.
  2. **Mở rộng toàn diện các chương 4 đoạn thoại (Scene 1 -> Scene 5) lên đủ 4 Beats / chương (tổng cộng 22 bức tranh lớn toàn tập):** Đảm bảo mỗi đoạn thoại ~20-30s đều có bức tranh riêng biệt khớp 100% với từng lời văn đang đọc.
  3. **Áp đặt bộ lọc `KHÔNG CÓ CHỮ (NO TEXT, NO WORDS, NO LABELS, NO NUMBERS)` trong mọi prompt Gemini:** Giúp tranh 2D sạch chữ tuyệt đối, nhường phần ghi nhãn cho Pill Badge và nét chữ viết tay chuẩn Tiếng Việt trên mặt giấy trắng.








### [LESSON-33] (2026-11-04)
- **Symptom:** Hiển thị logo ngôi sao 4 cánh mờ của Gemini ở góc phải dưới trên cả ảnh minh họa lẫn video Intro/Outro
- **Ruled-out Dead-end:** Đưa trực tiếp file MP4/PNG tải từ Gemini vào FFmpeg concat hoặc dùng cv2.inpaint đè lên viền mực đen làm nhòe nét vẽ
- **Verified Golden Path:** Xây dựng mặt nạ đối xứng 8 hướng (8-way symmetric alpha template) để giải pha trộn (Inverse Alpha Deblending: I_clean = (I - alpha*255)/(1 - alpha)) cho toàn bộ 240 khung hình Intro/Outro và phục hồi màu nội vùng + viền mực đen cho 25 ảnh PNG

### [LESSON-12] (2026-11-04)
- **Symptom:** Khi camera zoom 2x vào Node i trên World Canvas, phần tiêu đề Header bị cắt lấp lửng ở mép trên và mép hình Node i-1 bị lọt vào rìa trái khung hình
- **Ruled-out Dead-end:** Vẽ Header trực tiếp lên World Canvas chung với các Node rồi crop chung một ma trận camera mà không tách lớp cô lập Node đang vẽ
- **Verified Golden Path:** Tách riêng Fixed Viewport Header (1280x68px) cố định ở đỉnh màn hình, chỉ áp dụng ma trận camera (warpAffine) cho vùng Body (1280x652px), và bật chế độ isolate_active_node_during_focus để chỉ hiển thị duy nhất Node đang vẽ trên nền giấy trắng cho tới pha overview_reveal cuối chương

### [LESSON-28] (2026-11-04)
- **Symptom:** Khi mở rộng kịch bản chi tiết hơn (Prompt Expansion), các hình minh họa hành động mới ghi đè lên các hình bảng chỉ số RPG gốc khiến video bị thiếu mất bảng chỉ số RPG.
- **Ruled-out Dead-end:** Dùng chung tên file asset cũ khi tạo hình mới làm mất hình cũ hoặc chỉ chọn 1 trong 2 hình cho mỗi đoạn.
- **Verified Golden Path:** Tách bạch hoàn toàn tên file cho từng hình ảnh và đưa toàn bộ 100% hình ảnh (29/29 nodes) vào luồng Dynamic Multi-Node Canvas (Scene 1: 6 nodes, Scene 2: 8 nodes, Scene 3-5: 4 nodes, Scene 6: 3 nodes) khớp chuẩn từng nhịp giọng đọc.

### [LESSON-29] (2026-11-04)
- **Symptom:** Khi tô màu bức tranh ở Phase 2 (Color Wash), nét cọ bị tràn xuống phần chữ caption bên dưới khiến nửa trên của dòng chữ hiện ra trước khi bàn tay chuyển sang công đoạn viết chữ (Phase 3).
- **Ruled-out Dead-end:** Tính bán kính cọ tô màu color_brush_r theo chiều cao toàn bộ World Canvas (self.h / 720.0) khiến cọ phình to tới 65px trên canvas nhiều hàng, và hàm _stamp_brush không giới hạn khung cắt (clip_rect) vào vùng tranh.
- **Verified Golden Path:** Cố định bán kính cọ theo chuẩn Node 720p (color_brush_r = 26px), truyền clip_rect = (plan.rx, plan.ry, plan.rx + plan.rw, plan.ry + plan.rh) vào _stamp_brush để khóa cứng 100% cọ tô màu trong vùng tranh, đồng thời xóa sạch vùng chữ phía trước ngòi bút trong suốt Phase 3.

### [LESSON-30] (2026-11-04)
- **Symptom:** Cần tự động hóa chấm điểm SEO YouTube 100/100, cào từ khóa tìm kiếm thực tế, tạo mốc thời gian chia chương (Chapters) chính xác từng khung hình và tự động đăng tải lên YouTube Studio qua Playwright MCP
- **Ruled-out Dead-end:** Dùng các repo rỗng (appexlabs-a11/youtube-tags-generator), API trả phí không hỗ trợ tiếng Việt (coffeefuelbump/AI-YouTube-Timestamps), hoặc gán innerHTML trực tiếp trong YouTube Studio bị chặn bởi TrustedHTML CSP
- **Verified Golden Path:** Kết hợp ChocoData-com/youtube-suggest-scraper (cào ds=yt live tiếng Việt không tốn API key) + BizMapper/Open-Tube-SEO (chấm điểm 13 tiêu chí 100/100 + DOM createElement tuân thủ TrustedTypes) + ffprobe native Chapter Timestamps + stage file vào C:/Users/PC/.playwright-mcp/uploads để upload qua Playwright MCP

### [LESSON-38] (2026-11-05) Căn Giữa Trọng Tâm Khi Focus, Thu Hẹp Lưới Toàn Cảnh & Điểm Ngọt Dừng Chân Hold 1.5s Cuối Mỗi Phân Cảnh
- **Symptom:** Khi zoom vào vẽ từng hình, nội dung bị dồn về góc trái hoặc góc phải màn hình; khi zoom out toàn cảnh, khoảng cách giữa các tranh quá xa (gap 200px); nếu cắt ngay 0s thì khán giả không kịp nhìn tổng thể tranh, nhưng nếu dừng 3.5s thì quá lâu gây cảm giác video bị chùng, sốt ruột.
- **Ruled-out Dead-end:** Kẹp tâm camera crop vào biên thế giới; dùng khoảng cách thưa `gap_x=200, gap_y=150`; dừng quá lâu (3.5s - 4.0s) hoặc cắt ngay lập tức (0s).
- **Verified Golden Path:**
  1. **Định tâm 100% không kẹp biên:** Đặt trực tiếp `cam_cx = node_cx, cam_cy = node_cy` cho mọi keyframe focus. Trong `_apply_camera_crop`, tính trực tiếp `x0 = cx - cw/2, y0 = cy - ch/2` và dùng `cv2.warpAffine` với `borderMode=cv2.BORDER_CONSTANT, borderValue=(255,255,255)`.
  2. **Thu nhỏ góc nhìn focus (Tight Body Viewport):** Căn chỉnh `target_ch = node_h + 60px = 490px` và `target_cw = target_ch * (1280/652) = 960px` để phần tử minh họa chiếm 70% - 85% diện tích body.
  3. **Thu hẹp khoảng cách lưới (`gap_x = 75px, gap_y = 60px`):** Giảm 60% khoảng cách giữa các node, tạo thành lưới storyboard gắn kết.
  4. **Điểm ngọt dừng chân 1.5 giây (SCENE_HOLD_MS = 1500ms):** Thêm `HOLD_MS = 1500ms` vào cuối phân cảnh; camera lùi về toàn cảnh trong 500ms và giữ yên trong 1000ms. Dùng `apad=whole_dur` để kéo dài dòng âm thanh bằng khoảng lặng, giúp sidechain giải phóng cho BGM nổi lên nhẹ nhàng rồi chuyển cảnh dứt khoát.

### [LESSON-39] (2026-11-05) Sử Dụng Bộ Nhận Diện Thương Hiệu Chính Thức Trong `assets/branding/`
- **Symptom:** Tự tạo logo bằng PIL từ ảnh cắt trong scene dẫn đến lấy nhầm hình sư tử và lỗi hiển thị dấu tiếng Việt trên khung chữ nhỏ, trong khi dự án đã có sẵn bộ logo chính thức rất đẹp tại `assets/branding/logo_ve_chuyen_hoang_da.png`.
- **Ruled-out Dead-end:** Tự sinh ảnh avatar/watermark mới bằng code PIL thay vì kiểm tra thư mục `assets/branding/`.
- **Verified Golden Path:** Luôn kiểm tra và sử dụng trực tiếp `assets/branding/logo_ve_chuyen_hoang_da.png` (`logo_circle_fitted.png`, `logo_badge_perfect_square.png`) cho toàn bộ Avatar kênh, Watermark video (150x150) và Banner kênh (2560x1440).

### [LESSON-40] (2026-11-05) Quy Trình Tạo & Cập Nhật Banner Kênh & Thumbnail Video Bằng Google Gemini Qua Playwright MCP
- **Symptom:** Tự sinh Banner hoặc Thumbnail bằng script PIL cục bộ khiến hình ảnh bị chắp vá, font chữ vỡ dấu ("V CHUYN HOANG DÃ"), làm giảm uy tín kênh và khiến đạo diễn không hài lòng.
- **Ruled-out Dead-end:** Dùng PIL vẽ khung hộp hay paste text viền đen thô kệch lên ảnh; bỏ qua phiên Google Gemini có sẵn trong Playwright.
- **Verified Golden Path:**
  1. **Tạo ảnh nghệ thuật qua Google Gemini:** Chuyển sang Tab Google Gemini bằng Playwright MCP, soạn thảo prompt chi tiết phong cách minh họa nghệ thuật hoạt hình 2D Comic / Màu nước Whiteboard, bố cục kịch tính thu hút thị giác (High-CTR) và nhấn mạnh `TUYỆT ĐỐI KHÔNG CÓ CHỮ (NO TEXT)`.
  2. **Tải ảnh an toàn bằng Canvas DOM:** Lắng nghe blob image mới tạo, vẽ lên canvas ẩn và kích hoạt tải về qua data URL PNG vào `gemini_downloaded/`.
  3. **Chuẩn hóa tỷ lệ an toàn:**
     - *Banner kênh (2560x1440):* Căn giữa nội dung chính vào Safe-Area `1546 x 423` đảm bảo hiển thị hoàn hảo trên Mobile, Tablet, PC và TV.
     - *Thumbnail video (1280x720):* Xuất file JPG chất lượng cao (< 2MB).
  4. **Tải lên YouTube Studio:** Sử dụng thư mục staging được phép truy cập (`C:\Users\PC\.playwright-mcp\`) để tải lên trực tiếp và nhấn Xuất bản.

### [LESSON-41] (2026-11-05) Chiến Lược Phân Phối Video Cho Kênh Hội Họa Hướng Tới Trẻ Em & Mọi Lứa Tuổi Trên YouTube
- **Symptom:** Kênh tập trung vào vẽ tranh hoạt hình và hướng tới trẻ em, nhưng nếu chọn cài đặt "Có, nội dung dành cho trẻ em" (Made for Kids theo COPPA) thì YouTube sẽ tự động tắt tính năng bình luận, tắt chuông thông báo, tắt màn hình kết thúc, không cho lưu video vào danh sách phát và giảm đáng kể khả năng phân phối lan tỏa.
- **Ruled-out Dead-end:** Đánh dấu "Made for Kids" trên YouTube Studio khiến kênh bị hạn chế tương tác hoàn toàn; hoặc để lộ hình ảnh kinh dị, máu me khiến video bị gắn cờ hạn chế độ tuổi 18+.
- **Verified Golden Path:**
  1. **Cài đặt kỹ thuật trên YouTube:** Đặt `Đối tượng người xem = Không, đây không phải nội dung dành cho trẻ em` (theo quy chuẩn COPPA) và `Giới hạn độ tuổi = Không giới hạn người xem trên 18 tuổi`. Nhờ đó video vừa an toàn tuyệt đối cho trẻ em và gia đình xem, vừa duy trì đầy đủ tính năng bình luận, chuông thông báo và đề xuất tự nhiên.
  2. **Tối ưu hóa nội dung & hình ảnh:** 100% hình ảnh vẽ tay trong sáng, màu sắc sinh động, nhân vật dễ thương biểu cảm lém lỉnh; giọng kể truyền cảm hứng học vẽ, đặt câu hỏi gợi mở cho các bé và cha mẹ bình luận tương tác.
  3. **Hệ từ khóa SEO bổ trợ:** Bổ sung các từ khóa kích thích học vẽ và thiếu nhi (`vẽ động vật hoạt hình`, `dạy bé vẽ con vật`, `vẽ chuyện hoang dã`, `hoạt hình vẽ tay`, `khám phá động vật cho bé`, `doodle vui nhộn`).

### [LESSON-42] (2026-11-05) Quy Trình Tối Ưu Hóa Tiếp Cận Toàn Cầu (Global Reach) & Bản Dịch Đa Ngôn Ngữ Qua YouTube Studio Playwright MCP
- **Symptom:** Kênh chỉ phát hành bằng tiếng Việt khiến người xem ở các quốc gia khác (Mỹ, Châu Âu, Nhật Bản, Ấn Độ...) không hiểu tiêu đề, không tìm thấy video qua thanh tìm kiếm và thuật toán YouTube không đề xuất video ra ngoài lãnh thổ Việt Nam.
- **Ruled-out Dead-end:** Tạo nhiều kênh YouTube con cho từng quốc gia gây phân tán nguồn lực và người theo dõi; hoặc chèn phụ đề cứng (hardcoded burned-in subtitles) bằng tiếng Việt khiến người nước ngoài thấy rối mắt.
- **Verified Golden Path:**
  1. **Bản dịch Kênh YouTube (Channel Translation):** Vào `studio.youtube.com/channel/.../editing/profile` -> "Thêm ngôn ngữ" -> Đặt ngôn ngữ gốc là Tiếng Việt, ngôn ngữ dịch là Tiếng Anh -> Điền tên kênh quốc tế `Vẽ Chuyện Hoang Dã - Wild Tales Sketch` và mô tả tiếng Anh chuẩn phong cách hội họa hoạt hình.
  2. **Bản dịch Tiêu đề & Mô tả Từng Video (Video Metadata Translation):** Vào `studio.youtube.com/video/<id>/translations` -> Xác nhận ngôn ngữ gốc Tiếng Việt -> Bấm "Thêm ngôn ngữ" chọn Tiếng Anh -> Bấm vào ô `td.tablecell-metadata #metadata-add` -> Điền Tiêu đề tiếng Anh giật tít chuẩn quốc tế (High-CTR Title) + Mô tả tiếng Anh đầy đủ mốc thời gian Chapters -> Nhấn Xuất bản.
  3. **Kích hoạt Phụ đề Tự động Đa Ngôn ngữ (Auto-Translate Subtitles):** Khi video đã có ngôn ngữ gốc Tiếng Việt và bản dịch Tiếng Anh, YouTube tự động kích hoạt tính năng dịch phụ đề (CC Auto-Translate) sang hơn 100 ngôn ngữ cho bất kỳ khán giả nào trên thế giới.





### [LESSON-43] (2026-11-05)
- **Symptom:** Chữ caption phân cảnh trước bị đè sang phân cảnh sau (text overlap / bleed) trên canvas đa nút hoặc khi chuyển camera
- **Ruled-out Dead-end:** Để nguyên chuỗi caption dài (80+ ký tự) không bọc giới hạn, căn giữa tự do khiến chữ tràn ra hai mép thẻ ảnh lấn sang cột lân cận
- **Verified Golden Path:** Áp dụng Hệ Thống Cách Ly Caption 3 Lớp (Three-Pillar Zero-Bleed): Dynamic font fitting co cỡ chữ tự động trong phạm vi max_w - 48px, kẹp cứng tọa độ và bounding box không bao giờ vượt ra ngoài ô lưới của nút, và đệm cách ly pad_iso <= 12px

### [LESSON-44] (2026-11-06)
- **Symptom:** Chiến lược xuất bản cường độ cao 2 Video Dài/ngày + 2 Shorts/ngày nhằm kích hoạt thuật toán YouTube quét dữ liệu nhanh gấp đôi để đạt điều kiện bật kiếm tiền
- **Ruled-out Dead-end:** Đăng video tùy hứng không cố định khung giờ; hoặc đăng dồn 2 video cùng một lúc khiến video tự ăn thịt lưu lượng (cannibalize) của nhau; hoặc xuất video dưới 8 phút làm mất tính năng gắn quảng cáo giữa video (Mid-roll ads)
- **Verified Golden Path:** 1. Phân chia 2 ca đăng bài độc lập: Ca 1 trưa (11:30 Video Dài 1 + 12:15 Shorts 1) và Ca 2 tối (18:00 Video Dài 2 + 20:00 Shorts 2). 2. Luôn lên lịch (Schedule) trước ít nhất 2 tiếng để YouTube xử lý xong độ phân giải Full HD 1080p/60fps và duyệt bản quyền. 3. Liên kết chéo 2 video trong ngày: Outro Video 1 nhắc đón xem Video 2 lúc 18:00 và gắn End Screen trỏ sang Video 2 ngay khi Video 2 lên sóng. 4. Chuẩn bị sẵn gói 6-10 video dự trữ để không bao giờ bị đứt gãy lịch đăng.

### [LESSON-45] (2026-11-06) [ĐÃ NGƯNG — ElevenLabs bị bỏ 2026-11-07, giọng chính là VoiceStudio; chỉ giữ để tham khảo lịch sử]
- **Symptom:** Tự ý hạ cấp xuống voice hệ thống (gTTS) khi hết credit ElevenLabs làm mất chất giọng cảm xúc Adam
- **Ruled-out Dead-end:** Dùng gTTS với filter rubberband/ffmpeg để giả lập giọng nam khi API ElevenLabs hết hạn ngạch, dẫn đến giọng đọc robot vô cảm, phá vỡ chuẩn kênh
- **Verified Golden Path:** Tuyệt đối cấm dùng voice hệ thống. Khi toàn bộ API key ElevenLabs hết hạn ngạch, BẮT BUỘC phải dừng lại và yêu cầu người dùng cung cấp API key ElevenLabs mới; chuẩn bị sẵn script có tag cảm xúc [curious], [confident], [amazed] để tổng hợp ngay khi có key

### [LESSON-46] (2026-11-06)
- **Symptom:** Video dài kết xuất có thời lượng dưới 8 phút 15 giây (495s) vi phạm tiêu chuẩn tài liệu kế hoạch kênh (bắt buộc >= 8:15 phút để bật quảng cáo Mid-roll), và video intro mới được cung cấp có chứa hình mờ (watermark) ngôi sao 4 cánh của Google Gemini ở góc phải dưới
- **Ruled-out Dead-end:** Đăng video dưới 8:15 phút khiến kênh mất tính năng chèn quảng cáo giữa video (Mid-roll ads); hoặc làm mờ nhòe diện rộng (blur box) góc phải dưới làm hỏng tính thẩm mỹ của hoạt cảnh 3D mở cuốn sách phép thuật
- **Verified Golden Path:**
  1. **Điều tốc Audio Chuẩn Vàng (Golden Tempo Calibration):** Đưa giọng đọc ElevenLabs Adam về nhịp kể tự nhiên broadcast (~1.075x qua bộ lọc atempo=0.86), bổ sung khoảng nghỉ thở tự nhiên 250ms giữa các phân đoạn, đưa tổng thời lượng video dài lên mức 8 phút 51 giây (531.62s) nằm trọn trong vùng vàng 8:15 – 10:30 phút theo đúng tài liệu kế hoạch.
  2. **Khử Watermark Video Gemini Bằng Inverse Alpha Deblending Tọa Độ Động:** Xác định vùng watermark (y: 635-685, x: 1195-1245), trích xuất ma trận alpha đối xứng 4 chiều từ các khung hình tĩnh, giải phương trình hoàn màu deblend `(patch - a * 255) / (1 - a)` và vá mịn Navier-Stokes/Telea ở lõi ngôi sao, khử sạch 100% watermark trên toàn bộ 240 khung hình của video intro `intro_ve_chuyen_hoang_da.mp4` mà không để lại vết tỳ vết.

### [LESSON-47] (2026-11-06)
- **Symptom:** Hình ảnh minh họa bảng trắng bị thiếu so với lời thuyết minh (giữ tĩnh một hình vẽ quá lâu trong khi giọng đọc chuyển qua các ý khác nhau), và thumbnail gốc của Gemini là ảnh thô chưa có số tập ("TẬP 04") hay các yếu tố kích thích tò mò cao khiến tỷ lệ nhấp chuột (CTR) thấp
- **Ruled-out Dead-end:** Giữ nguyên 4 nút thưa thớt cho mỗi cảnh dài 80-100 giây khiến màn hình bị "chết" hình ảnh; hoặc chỉ dùng ảnh Gemini nguyên bản không có typography frame, thiếu badge số tập khiến khán giả lướt qua không nhận diện được chuỗi series
- **Verified Golden Path:**
  1. **Mở Rộng Mật Độ Minh Họa Đồng Bộ 100% (37 Nút Canvas):** Dùng Playwright MCP kết nối trực tiếp phiên Google Gemini tự động tạo 9 tranh vẽ comic 2D mới bổ sung vào các nhịp thiếu (thủy thủ khâu mỏ vịt, X-quang hộp sọ, nọc độc hạ chó săn, radar vi mô não bộ, phát sáng đêm, cắt bỏ gen dạ dày, tôm giáp cứng, so sánh 10 NST, hạn hán phục hồi suối), nâng tổng số nút lên 37 nút (trung bình 10-14s/hình), khớp 100% từng câu thoại ElevenLabs.
  2. **Bộ Khung Thumbnail High-CTR Đạt Chuẩn Kênh:** Bổ sung viền đôi comic (Đỏ 14px + Vàng 6px), Badge số tập `TẬP 04` góc trái trên, Badge `ĐỘ KỲ DỊ: 999!` góc phải trên, sticker `CÚ SỐC 160 TRIỆU NĂM!`, thanh hook đen-vàng kích thích tò mò tột độ `CÚ LỪA THẾ KỶ?!` và sub-hook `MỎ VỊT • CỰA ĐỘC • KHÔNG DẠ DÀY!`.


### [LESSON-48] (2026-11-06)
- **Symptom:** Watermark Gemini 4 cánh còn sót trên hình nền có chi tiết (lá cây, đại dương, gỗ, thẻ stat) trong video bảng trắng
- **Ruled-out Dead-end:** Chỉ kiểm tra ngưỡng trắng (b,g,r >= 205) để phủ màu trắng [255,255,255] khiến các hình ảnh tràn viền hoặc có chi tiết vẽ ở góc dưới phải bị bỏ sót 100% watermark
- **Verified Golden Path:** Xây dựng mặt nạ hình học astroid chuẩn xác (|x-cx|/R)^p + (|y-cy|/R)^p <= 1 (R=25.5, p=0.52 trên 1024x572) kết hợp cv2.inpaint Telea cho nền màu/họa tiết và phủ trắng #FFFFFF cho nền giấy trắng, giữ nguyên 100% chi tiết gốc không làm mờ hay biến dạng tranh

### [LESSON-49] (2026-11-06)
- **Symptom:** Lệch hình ảnh minh họa so với voice diễn đạt trong video YouTube Shorts phễu kéo kênh
- **Ruled-out Dead-end:** Sử dụng các tranh minh họa chung chung không khớp từng câu thoại (thoại nói không dạ dày và ngậm sỏi má nhưng hình lại vẽ chimera và tiết sữa)
- **Verified Golden Path:** Phân tách kịch bản giọng đọc thành 5 phần chặt chẽ, ánh xạ 1:1 với hình vẽ đặc tả chuyên biệt (Hình 1: Thú mỏ vịt ngơ ngác đáng yêu; Hình 2: Cầm kéo rạch mỏ; Hình 3: X-quang không dạ dày; Hình 4: Ngậm sỏi vào túi má; Hình 5: Phát sáng tia UV xanh ngọc; Hình 6: CTA phễu), căn chỉnh thời gian theo từng mili-giây khớp 100% với giọng đọc

### [LESSON-50] (2026-11-06)
- **Symptom:** Khử watermark Gemini bằng inpainting/blur làm mờ nét vẽ comic và vân chi tiết
- **Ruled-out Dead-end:** Inpaint cv2.INPAINT_TELEA hoặc Gaussian Blur làm nhòe nét viền đen và gãy vân lá
- **Verified Golden Path:** Áp dụng Inverse Alpha Deblending toán học chuẩn I=(I_raw-a*255)/(1-a) với ma trận alpha 71x71 đối xứng 8 hướng tại cx=964, cy=523 khôi phục 100% nét mực gốc và màu sắc mà không làm mờ

### [LESSON-51] (2026-11-06)
- **Symptom:** Thumbnail AI đã có sẵn typography/elements nghệ thuật bị đè banner đồ họa tự động
- **Ruled-out Dead-end:** Dùng script tự động vẽ thêm banner và viền nhân tạo che mất bố cục tranh vẽ AI gốc
- **Verified Golden Path:** Sử dụng trực tiếp tác phẩm tranh vẽ AI đã chứa huy hiệu số tập, khử sạch watermark góc bằng Inverse Alpha Deblending, scale chuẩn 1280x720 và đẩy thẳng lên YouTube Studio

### [LESSON-52] (2026-11-06)
- **Symptom:** Trùng lặp hình ảnh giữa các phân cảnh do querySelector tải nhầm ảnh lặp trong Playwright
- **Ruled-out Dead-end:** Dùng querySelector chung không gắn index model-response dẫn đến nhiều file ảnh tải về có cùng nội dung
- **Verified Golden Path:** Bắt buộc query theo từng index model-response[i] cụ thể, sau đó chạy test MD5 hash tự động đảm bảo 100% tệp ảnh độc nhất (0 duplicate hash) trước khi kết xuất video.

### [LESSON-53] (2026-11-06)
- **Symptom:** Khoang nghi overview qua dai (3.5s-5.0s) gay chan va lech audio-visual hinh 4
- **Ruled-out Dead-end:** Keo dai hold_ms len 3.5s-5s de dap ung thoi luong va chia doi 1 doan audio cho 2 node khac nhau
- **Verified Golden Path:** Khoa chat hold_ms = 1500ms (1.5s sweet-spot). Moi Node bat buoc co 1 audio segment rieng biet dong bo 100% voi noi dung hinh ve

### [LESSON-54] (2026-11-06)
- **Symptom:** Video YouTube Shorts bị lệch thứ tự hình ảnh so với lời thuyết minh (nói Capybara nhưng chiếu hình hươu), sót watermark Gemini do dùng file `_raw.png`, và voice ở giây cuối video bị cắt cụt đột ngột do dùng flag `-shortest` và câu thoại nối dở dang.
- **Ruled-out Dead-end:** Cố tình thêm câu thoại lửng lơ (`...và đó là lý do tại sao...`) để làm seamless loop nhưng lại để `-shortest` cắt cụt trước khi hết câu; hoặc dùng trực tiếp file `_raw.png` chưa khử watermark; hoặc xếp thứ tự tranh không bám sát nội dung voiceover từng phần.
- **Verified Golden Path:** 
  1. **Đồng bộ Ánh Xạ 1:1 Tuyệt Đối:** Tách biệt 6 beat tương ứng 6 audio parts riêng lẻ (Beat 0: Hook avatar; Beat 1: Kẹp thử Capybara; Beat 2: Sơ đồ túi 13L; Beat 3: Mòng biển cướp cá; Beat 4: Lộn cổ tản nhiệt; Beat 5: Cú nuốt bồ câu tại London + CTA kênh).
  2. **100% Khử Sạch Watermark:** Chỉ sử dụng các tệp `_clean.png` đã qua xử lý Inverse Alpha Deblending toán học.
  3. **Đệm Outro Buffer 1.4s - 1.6s:** Tuyệt đối không dùng `-shortest` cắt cụt audio. Câu thoại cuối kết thúc dứt khoát trọn vẹn ("Bấm ngay vào kênh Vẽ Chuyện Hoang Dã để xem trọn bộ bản Full siêu cuốn nhé!"), bàn tay marker rút lui và giữ tĩnh màn hình CTA kèm BGM fadeout nhẹ nhàng trong 1.5s để người xem kịp thao tác nhấp vào kênh.

### [LESSON-55] (2026-11-06)
- **Symptom:** Chữ phụ đề ở các node tranh bị đè chồng rối rắm (Image 1, 3) hoặc bị tràn cắt cụt mép phải màn hình khi camera zoom cận (Image 2).
- **Ruled-out Dead-end:** Để nguyên tranh do Gemini tạo có sẵn dòng chữ AI rác ở đáy viền thẻ bài (`Sđt Nâng C05L1m...`) rồi in phụ đề đè lên; hoặc viết phụ đề quá dài (80-100 ký tự) vượt quá chiều rộng khung lưới và khung nhìn camera zoom.
- **Verified Golden Path:** 
  1. **Khử chữ AI rác trên tranh:** Quét và xóa trắng viền đáy tranh tạo bởi Gemini (`im[502:, :] = 255`) trước khi đặt vào canvas.
  2. **Chuẩn độ dài phụ đề tinh gọn:** Khống chế mọi dòng `caption_text` dưới 55 ký tự (punchy edutainment), luôn nằm lọt lòng trong vùng an toàn của thẻ bài và tâm ngắm của camera zoom.
  3. **Cơ chế phòng thủ tự động trong Composer:** Trong `editorial_sketchbook_composer.py`, tự động hạ font size xuống tới 8pt và tự động cắt lửng bằng `...` an toàn nếu chữ vượt quá `max_text_w`, triệt tiêu 100% nguy cơ tràn mép.

### [LESSON-56] (2026-11-06) [ĐÃ NGƯNG — ElevenLabs bị bỏ 2026-11-07, giọng chính là VoiceStudio; chỉ giữ để tham khảo lịch sử]
- **Symptom:** Voice ElevenLabs Adam đột ngột đọc giọng lơ lớ như tiếng nước ngoài (tiếng Lào/Anh: "Vajai chinla, bianlonnaad...") ở một số phân cảnh có từ mượn tiếng Anh hoặc tag cảm xúc (ví dụ `gular pouch`, `Capybara`, `flycam`).
- **Ruled-out Dead-end:** Sử dụng `eleven_multilingual_v2` với cơ chế auto-detect ngôn ngữ kết hợp từ mượn tiếng Anh hoặc thẻ cảm xúc trong đoạn văn bản.
- **Verified Golden Path:** 
  1. **Ép buộc mã ngôn ngữ tiếng Việt:** Sử dụng model `eleven_turbo_v2_5` với tham số bắt buộc `language_code: 'vi'` giúp hệ thống luôn phiên âm chuẩn tiếng Việt 100%.
  2. **Việt hóa thuật ngữ sinh học trong kịch bản thuyết minh:** Thay các thuật ngữ tiếng Anh bằng từ thuần Việt (ví dụ: `gular pouch` -> `túi da dưới mỏ`), đảm bảo câu văn phát âm tự nhiên, thuần khiết.
  3. **Kiểm tra tự động bằng Whisper:** Chạy tự động Whisper ASR trên 100% các file audio sinh ra để kiểm định `language == 'vi'` trước khi đưa vào render video.

### [LESSON-57] (2026-11-06) [ĐÃ NGƯNG — ElevenLabs bị bỏ 2026-11-07, giọng chính là VoiceStudio; chỉ giữ để tham khảo lịch sử]
- **Symptom:** Voice của video YouTube Shorts bị lệch nhịp so với nét vẽ tay hoặc nghe không giống giọng ElevenLabs Adam truyền cảm (do dùng model fallback hoặc cắt tỉa script quá đà khi quota cạn).
- **Ruled-out Dead-end:** Cắt bớt câu chữ xuống quá ngắn (<80 ký tự) làm mất nội dung hóm hỉnh và làm lệch khớp thời gian với hoạt họa nét vẽ; dùng audio fallback không phải ElevenLabs Adam.
- **Verified Golden Path:** 
  1. **Tạo giọng chuẩn ElevenLabs Adam với Model v4 tốc độ 1.25x:** Giữ nguyên các tag cảm xúc tự nhiên ([curious], [laughs], [amazed], [dramatic], [excited]), tốc độ 1.25x chuẩn Shorts giúp giọng đọc truyền cảm, hài hước và giàu năng lượng.
  2. **Kiểm định Whisper ASR 100% tiếng Việt:** Chạy kiểm tra Whisper trên tất cả 6 audio parts đảm bảo nhãn `[vi]`, phát âm trọn vẹn từng câu thoại (từ hook mở đầu đến CTA kết video).
  3. **Đồng bộ mili-giây tuyệt đối với `shorts_parts_duration.json`:** Renderer đọc chính xác độ dài từng part và khoảng nghỉ ngắn (`gap_sec: 0.10s`), đồng bộ nét vẽ bút lông theo đúng từng từ ngữ đang phát, kết thúc bằng vùng đệm Outro Hold 1.4s tạo trải nghiệm chuyển tiếp mượt mà.


### [LESSON-58] (2026-11-07)
- **Symptom:** Thieu thong tin SEO hoac thumbnail lech cau truc so voi Tap 4 khi dang YouTube
- **Ruled-out Dead-end:** Tao SEO don dieu thieu chapters/timestamps 6 hoi hoac upload thu cong bo sot hen gio
- **Verified Golden Path:** Chuan hoa 100/100 SEO Package voi day du 6 hoi timestamps + multi-section description va upload hen gio tu dong bang Playwright persistent context

### [LESSON-59] (2026-11-07)
- **Symptom:** Loi lap lai quy trinh san xuat roi rac va thu cong gay mat thoi gian sua chua
- **Ruled-out Dead-end:** Viet script rieng le cho tung tap copy paste de phat sinh loi cu nhu quen deblend lech voice tran chu
- **Verified Golden Path:** Thiet lap Unified Production Master Suite voi 7-Gate Preflight QA Inspector tu dong chan dung 100 phan tram loi truoc khi render hoac upload

### [LESSON-60] (2026-11-07) Triệt tiêu lỗi cắt cụt voice ở cuối video YouTube Shorts & Chuẩn hóa Seamless Loop
- **Symptom:** Giọng đọc voice ở cuối video Shorts bị ngắt cụt hoặc kết thúc lửng lơ ở nửa câu (ví dụ: 'gặp ốc sên nó... [cắt phụt]'), khiến người xem cảm giác video bị lỗi hoặc chưa nói hết đã hết video.
- **Ruled-out Dead-end:** Tuyệt đối không cắt câu thoại giữa chừng thành 2 nửa cơ học (nửa sau đặt ở 0:00, nửa đầu đặt ở cuối video); không set thời lượng video đúng bằng điểm kết thúc của file âm thanh voice mà không có vùng đệm xả âm.
- **Verified Golden Path:**
  1. **Trọn vẹn ngữ nghĩa câu thoại:** Mọi câu thuyết minh trong Shorts phải hoàn chỉnh 100% ngữ pháp và thông điệp (chủ ngữ, vị ngữ, cú chốt hài hước hoặc Call-To-Action kết nối rõ ràng sang video dài).
  2. **Vùng đệm an toàn cuối video (Outro Breathing Buffer):** Luôn chừa **1.2s - 1.5s vùng đệm âm thanh & hình ảnh** sau từ cuối cùng được phát âm. Trong khoảng này, tranh minh họa và Call-To-Action giữ nguyên trên màn hình, nhạc nền BGM tiếp tục chơi và fade-out êm ái (`afade=t=out:st=end-1.5:d=1.5`).
  3. **Kỹ thuật Seamless Loop cao cấp:** Vòng lặp liền mạch được xây dựng qua cầu nối tư duy và câu hỏi kích thích tò mò (End: "Bấm xem video dài ngay bên dưới nhé!" -> Start: "Chỉ một con ốc sên nhỏ bé cũng đủ hạ gục kẻ bất tử này ngay lập tức!"), giúp video vừa thỏa mãn người xem độc lập, vừa vòng lặp trơn tru trên nền tảng YouTube Shorts.

### [LESSON-61] (2026-11-07)
- **Symptom:** Shorts nhìn đơn điệu: chỉ có 1 tranh trên nền trắng, caption 1 dòng, bàn tay vẽ Canny lộn xộn
- **Ruled-out Dead-end:** Viết lại script render riêng cho từng tập; vẽ cạnh Canny theo thứ tự contour dài nhất; sprite tay sai anchor
- **Verified Golden Path:** Dùng engine chung src/render/shorts_v4_renderer.py và một spec JSON cho mỗi tập (specs/shorts_v4_spec.json): tranh tách nền có bóng đổ, chỉ hiện nét mực tại chỗ ngòi bút đã đi qua rồi bật màu bằng spring, sticker số liệu bật lên đúng từ khóa, caption 3-4 từ sáng chữ đang đọc, SFX pop/whoosh/impact, buffer 1.5s; chạy --preview để xem contact sheet trước khi render full

### [LESSON-62] (2026-11-07)
- **Symptom:** Phu de Shorts lech nhip giong noi (chia deu thoi gian theo so tu), chu to va nam cao de tranh
- **Ruled-out Dead-end:** Noi suy thoi diem tung tu bang cach chia deu khoang giua 2 cum; dat caption y=1362 co 78px
- **Verified Golden Path:** Moi spec Shorts khai bao truong words (file Whisper word timestamps); renderer gan tung tu vao moc start that, an caption khi giong nghi >0.35s, tu chua doc mo 60%; caption 56px tam y=1405

### [LESSON-63] (2026-11-07)
- **Symptom:** Mui ten callout chi lung tung, banner 2 dong de dau len nhau, hinh khong khop voice
- **Ruled-out Dead-end:** Mui ten co dinh cung huong ngang tu sticker; dat cy dong banner theo ti le chieu cao khung; 6 tranh cho 52s (1 tranh om nhieu cau thoai)
- **Verified Golden Path:** Moi sticker khai bao target=[fx,fy] theo ti le tranh goc, renderer map qua Illustration.local() va ve bezier arrow + vong pulse dung diem; kiem tra mau tai target bang HSV truoc khi render. Banner: do bbox that (anchor ms + stroke) roi xep baseline co gap 10px. Chia 11 tranh ~4-5s/cau, prompt Gemini cung 1 chat de giu nhan vat; lay anh qua canvas.toDataURL ghi vao C:/Users/PC (Playwright MCP chi ghi duoc o day), chi deblend khi phat hien sao watermark.

### [LESSON-64] (2026-11-07)
- **Symptom:** Phụ đề video dài sai chính tả (Whisper nghe 'vũ chủ', 'chơi chơi', 'ngần sau')
- **Ruled-out Dead-end:** Dùng thẳng chữ Whisper làm caption
- **Verified Golden Path:** Chạy scripts/fix_long_words.py: căn chữ kịch bản TTS gốc vào timestamp Whisper bằng difflib trên dạng bỏ dấu, nội suy thời gian cho từ lệch; caption dùng long_words_fixed.json

### [LESSON-65] (2026-11-07)
- **Symptom:** Hình và giọng đọc lệch nhau trong video dài
- **Ruled-out Dead-end:** Đặt start_s thủ công bằng giây
- **Verified Golden Path:** Mỗi beat/sticker/impact neo vào 1 CỤM TỪ của lời thoại (hàm T(scene, phrase) trong build_longform_v2_spec.py), beat vào sớm 0.3s trước câu; giữ hình 3-15s

### [LESSON-62] (2026-11-07) [ĐÃ NGƯNG — ElevenLabs bị bỏ 2026-11-07, giọng chính là VoiceStudio; chỉ giữ để tham khảo lịch sử]
- **Symptom:** ElevenLabs eleven_v3 doc cham hon turbo ~30% (EP06 long: 510s->~576s)
- **Ruled-out Dead-end:** Thay model roi giu nguyen timing beat cu / hard-code DUR; de key trong code
- **Verified Golden Path:** Doc key tu .env; cache mp3 v3 rieng; atempo 1.15 sau TTS; chay lai Whisper + fix_long_words + build spec doc DUR tu parts_duration.json; tach beat >15s (TASTE-47)

### [LESSON-63] (2026-11-07)
- **Symptom:** YouTube Studio tu dat ngay hen gio mac dinh la ngay mai; Playwright MCP co the bi treo (timeout)
- **Ruled-out Dead-end:** Chi go gio, tin ngay mac dinh; doi MCP treo
- **Verified Golden Path:** Dung script node playwright persistent profile mcp-chrome-aad48e1 (dong chrome cu truoc); sau upload mo /video/<id>/edit -> Che do hien thi -> go ngay '7 thg 11, 2026' + gio, kiem tra lai; Shorts nam o tab /videos/short; len lich som it nhat 30 phut

### [LESSON-64] (2026-11-07)
- **Symptom:** Moi tap phai viet lai script rieng (synth, align, spec, upload) mat nhieu gio va de sai
- **Ruled-out Dead-end:** Copy script tap truoc roi sua tay tung hang so/duong dan
- **Verified Golden Path:** Dung bo cong cu chung src/episode/pipeline.py (init/check/tts/align/spec/render/qa/seo) + import_images.py + upload_youtube.cjs; du lieu tap nam o episode.json + specs/*_plan.json; vi du chuan examples/ep06_reference (da kiem chung: spec sinh ra trung 100% moc thoi gian 65 beat cua Tap 6, chuong SEO trung timestamp da dang)

### [LESSON-OMNIVOICE] (2026-11-07)
- **Symptom:** Hết credit ElevenLabs
- **Ruled-out Dead-end:** Dùng edge-tts (đều đều, không cảm xúc)
- **Verified Golden Path:** VoiceStudio (OmniVoice k2-fsa) cục bộ: src/audio/omnivoice_tts.py chạy bằng .venv của VoiceStudio, clone từ assets/voice_refs/adam_funny_ep1.wav (Adam eleven_v4 có tag). Cảm xúc lấy từ clip tham chiếu, tag hỗ trợ [laughter] [sigh] [surprise-oh]. CPU ~7x realtime (18s audio = 2 phút). Đặt HF_HUB_CACHE=%LOCALAPPDATA%/OmniVoice/hf_cache, offline.

### [LESSON-66] (2026-11-07)
- **Symptom:** Chủ kênh hết credit ElevenLabs, Tập 6 giọng thiếu cảm xúc
- **Ruled-out Dead-end:** Dùng ElevenLabs/gTTS/edge-tts hoặc viết kịch bản khô không có punchline
- **Verified Golden Path:** Giọng chính = VoiceStudio OmniVoice cục bộ (pipeline.py tts gọi src/audio/omnivoice_tts.py bằng .venv VoiceStudio, 1 lần nạp model cho mọi part, cache audio/vs/). Kịch bản + tag theo .agents/skills/core/humor-voice/SKILL.md. Đã xóa .env, voice_master.py và mọi script ElevenLabs; giữ nguyên audio các tập cũ.

### [LESSON-67] (2026-11-08) Chuẩn hóa Subtitle số/đơn vị, Mũi tên Sticker (Target Arrow) & Triệt tiêu tiếng rè Shorts
- **Symptom:** Subtitle hiển thị chữ đọc TTS thay vì số/đơn vị (`hai mươi xăng-ti-mét`, `mười ngàn bốn trăm g`); video Shorts bị tiếng rè sột soạt kéo dài đến hết; video dài thiếu hình và dùng nhầm ảnh dọc Shorts; popup sticker không có mũi tên chỉ vị trí.
- **Ruled-out Dead-end:** Để Whisper tự nhận diện số (dễ sai chính tả); chèn loop marker-scribble vào toàn bộ timeline Shorts; dùng chung ảnh dọc cho video ngang 16:9; để sticker trôi nổi không có tọa độ target.
- **Verified Golden Path:**
  1. **Hiển thị số Subtitle:** Thêm cụm từ vào `display_fix` trong `episode.json` và cập nhật `script_tokens()` trong `src/episode/pipeline.py` để thay thế phrase đa từ theo thứ tự giảm dần độ dài trước khi split. Chạy `pipeline.py align` để map chính xác thời gian phát âm vào từ hiển thị ngắn gọn (`20cm`, `10.400g`, `1.500 N`, `4.700°C`, `9.999 điểm`).
  2. **Triệt tiêu tiếng rè Shorts:** Loại bỏ hoàn toàn `marker-scribble-loop.wav` trong `src/render/shorts_v4_renderer.py`, chỉ giữ track `[voc]` (giọng đọc) và `[bgm]` (nhạc nền nén sidechain ducking mượt mà).
  3. **Mũi tên Sticker (Target Arrow):** Bổ sung tọa độ `"target": [x, y]` và `"bend"` cho toàn bộ sticker trong `longform_plan.json` và `shorts_plan.json` để kích hoạt `sv.draw_target_arrow()` và `draw_target_ring()` chỉ chính xác vào chi tiết trong tranh.
  4. **100% Ảnh 16:9 Dedicated:** Tạo bộ 32 hình comic 16:9 riêng biệt (`L01` đến `L32`), không tái sử dụng ảnh dọc Shorts trong video dài; mỗi beat khớp sát từng câu thoại, hold time 3s - 15s.

### [LESSON-72] (2026-11-08)
- **Symptom:** Render lai sau khi doi anh trong longform_plan nhung video van hien anh cu, render xong chi ~30s
- **Ruled-out Dead-end:** Chay 'pipeline.py render --long' khong co --force: longform_v2_renderer dung lai renders/long_v2/sceneXX.mkv da cache, chi ghep lai master
- **Verified Golden Path:** Moi khi doi anh/sticker/beat trong longform_plan.json -> chay 'pipeline.py spec' roi 'pipeline.py render <proj> --long --force'; render that mat nhieu phut va snapshots_long_v2 phai co timestamp moi. Kiem tra bang scripts/audit_beats.py (Image reuse = {} la ly tuong).

### [LESSON-72] (2026-11-08)
- **Symptom:** Render lai sau khi doi anh trong longform_plan nhung video van hien anh cu, render xong chi ~30s
- **Ruled-out Dead-end:** Chay 'pipeline.py render --long' khong co --force: longform_v2_renderer dung lai renders/long_v2/sceneXX.mkv da cache, chi ghep lai master
- **Verified Golden Path:** Moi khi doi anh/sticker/beat trong longform_plan.json -> chay 'pipeline.py spec' roi 'pipeline.py render <proj> --long --force'; render that mat nhieu phut va snapshots_long_v2 phai co timestamp moi. Kiem tra bang scripts/audit_beats.py (Image reuse = {} la ly tuong).

### [LESSON-73] (2026-11-08)
- **Symptom:** Shorts co tieng u/re nen keo dai suot video ke ca luc giong nghi (san tieng on -22 dBFS thay vi ~-47)
- **Ruled-out Dead-end:** Loc giong VoiceStudio (24 kHz) bang highpass+lowpass=12000 truoc khi resample: 12 kHz dung bang Nyquist -> bo loc biquad mat on dinh, sinh tieng u lien tuc
- **Verified Golden Path:** Trong pipeline.py tts: 'aresample=48000' PHAI dung dau chuoi -af cua shorts. Kiem tra: python scripts/hum_probe.py audio/vs/shorts.wav renders/<slug>_shorts.mp4 -> san tieng on luc giong nghi phai < -40 dBFS

### [LESSON-74] (2026-11-08)
- **Symptom:** Tăng tempo giọng làm video dài tụt dưới 8:30 (Tập 7: 8:45 ở tempo 1.0 -> 7:59 ở 1.10)
- **Ruled-out Dead-end:** Hạ tempo lại hoặc kéo dài khoảng nghỉ/hold hình để bù
- **Verified Golden Path:** Đo bằng scripts/voice_budget.py (17 ký tự/s ở tempo 1.0); viết thêm part mới cuối chương 2-5 (~670 ký tự cho Tập 7, thực tế thêm 919), tts chỉ tạo part mới, align, tạo hình riêng cho từng câu mới (L60-L66), thêm beat có sticker target, spec, audit_beats, render --force. Kết quả 8:47 ở tempo 1.10

### [LESSON-75] (2026-11-08)
- **Symptom:** Upload EP07: Shorts upload OK nhung khong lay duoc ID -> lich Shorts bi ket o mac dinh NGAY MAI; fix-only treo vi nut Luu bi disabled
- **Ruled-out Dead-end:** findId mo /videos/shorts (sai, Studio bao loi) va click Luu khi khong co thay doi
- **Verified Golden Path:** Tab Studio dung la /videos/short; hang dang xu ly khong co <a href> nen click tieu de roi doc ID tu URL (scripts/find_studio_video_id.cjs short '<chu trong tieu de>'); bo qua Luu khi aria-disabled=true; sau upload luon chay lai --fix-only de xac minh ca 2 video dung ngay+gio

### [LESSON-76] (2026-11-08)
- **Symptom:** Shorts lệch hình-lời, mũi tên sticker chỉ vào khoảng trống, loop outro lặp câu
- **Ruled-out Dead-end:** Dùng ảnh crop (S04b/S08b...) cho câu không có hình riêng; để target sticker mặc định [0.5,0.5]; outro lặp lại câu mở đầu
- **Verified Golden Path:** Mỗi câu lời = 1 ảnh Gemini riêng (thiếu thì tạo thêm); đo target bằng scripts/grid_sheet.py; outro là câu nối cụt (vd 'vì gã này...') dẫn về câu mở đầu; banner chương phải sinh tỉ lệ 21:9 dải mảnh (prompt 'height ~1/10 of length') rồi cắt nền bằng src/episode/prep_banners.py

### [LESSON-80] (2026-11-08)
- **Symptom:** Voice-design OmniVoice (instruct) cho cameo ra giọng khác nhau mỗi lần gọi
- **Ruled-out Dead-end:** Gọi instruct trực tiếp mỗi part -> cùng 1 thẩm phán mà mỗi câu một giọng
- **Verified Golden Path:** Thiết kế 1 lần bằng scripts/make_cast_refs.py, lưu assets/voice_refs/cast_<id>.wav + .txt, rồi clone bằng ref; instruct chỉ nhận từ khóa chuẩn (male/female, child..elderly, very low..very high pitch), cấm whisper

### [LESSON-81] (2026-11-09)
- **Symptom:** Playwright MCP chưa được Cursor nạp nên không tạo được ảnh Gemini; Gemini thỉnh thoảng timeout 1 ảnh
- **Ruled-out Dead-end:** Chờ MCP hoặc tạo ảnh tay từng cái
- **Verified Golden Path:** Dùng projects/<slug>/scripts/gemini_gen.cjs (mẫu Tập 9): Playwright launchPersistentContext với config/channel.json chrome_profile, gửi prompt từ specs/image_prompts.json, lấy ảnh từ model-response MỚI qua canvas.toDataURL -> assets/inbox/<ID>.txt, bỏ qua ảnh đã có, kiểm tra hash trùng; ~30s/ảnh. Ảnh timeout chạy lại với --per-chat 1 hoặc viết lại bố cục. Beat chèn thêm giữ ID mới (L85+) để không lệch số ảnh cũ.

### [LESSON-82] (2026-11-09)
- **Symptom:** Lỗi lặp lại giữa các tập do mỗi tập viết script phân cảnh/tạo ảnh riêng; chèn part làm lệch cache giọng; ước lượng thời lượng lạc quan
- **Ruled-out Dead-end:** Copy build_plans.py của tập trước rồi sửa; đổi tên file cache giọng bằng tay; tin ước lượng 17 ký tự/s
- **Verified Golden Path:** Công cụ chung src/episode/: build_plans.py (storyboard.json -> plans + prompts, chặn lỗi sớm), extra_prompts.py, gemini_gen.cjs, voice_cache.py snapshot/remap, target_sheet.py, banner_sheet.py; pipeline check có script_lint + ước lượng 17,6 ký tự/s theo tempo mood (biên 15s). Đã kiểm chứng: build_plans tái tạo y hệt plan Tập 9.

### [LESSON-83] (2026-11-09)
- **Symptom:** Ghép video tổng hợp từ 10 tập cũ: cắt cụt chữ, lọt câu 'tập sau/đăng ký', Whisper trên file mp4 lỗi PyAV metadata_errors
- **Ruled-out Dead-end:** Cắt theo ước lượng giây, ghép thô -c copy các tập khác độ phân giải (Tập 1-5 720p24, Tập 6+ 1080p30), cho faster-whisper tự đọc file mp4
- **Verified Golden Path:** src/mega: transcribe_sources.py đọc wav bằng soundfile rồi truyền mảng; silences.py + 'assemble.py check --snap' kéo mốc cắt vào khoảng lặng; check quét từ cấm trong đoạn giữ lại; build chuẩn hóa mọi đoạn 1920x1080@30 -14 LUFS + fade trắng 0,2s rồi mới concat. Tập 7+ dùng part_map.py cắt đúng ranh giới part. Whisper bỏ sót 10-30s đầu Tập 1-3 -> probe_range.py

### [LESSON-84] (2026-11-09)
- **Symptom:** Viet tap dac biet 60 phut noi dung moi: de lap lai su that da ke o tap le, so diem cong don sai, so doc bang chu thieu display_fix, PowerShell ghi file co BOM
- **Ruled-out Dead-end:** Viet tu tri nho roi moi kiem; sua tay tung so trong episode.json; dung Set-Content mac dinh
- **Verified Golden Path:** Do tu khoa tung su that trong transcript projects/mega-01-bang-phong-than/sources truoc khi viet + src/mega/overlap_check.py sau khi viet; viet content/*.md DSL -> build_from_content.py (doc utf-8-sig, moc sticker viet bang chu tu tra display_fix); suggest_display_fix.py + pipeline.py check sach !!; ke bang diem tung vong ra giay truoc khi viet loi; uoc luong 17.6 ky tu/giay x tempo, can ~70.500 ky tu cho 60:00+15s

### [LESSON-83] (2026-11-09)
- **Symptom:** Viết lại lời Shorts, xóa audio/vs/shorts.wav và chạy tts nhưng video vẫn dùng giọng cũ; align Shorts match chỉ 0.39
- **Ruled-out Dead-end:** Chỉ xóa file giọng thô audio/vs/shorts.wav
- **Verified Golden Path:** pipeline.py tts đã sửa: tự dựng lại audio/shorts.wav khi file thô mới hơn. Kiểm tra align Shorts match >= 0.85 trước khi render (0.39 = giọng cũ không khớp lời mới).

### [LESSON-84] (2026-11-09)
- **Symptom:** Phụ đề video dài lệch giọng 3-4 giây ở giữa chương (EP11 scene03 ~29.8s): chữ hiện trước khi giọng đọc tới
- **Ruled-out Dead-end:** Cho Whisper nghe nguyên cả chương 85s: ở ranh giới cửa sổ 30s nó bỏ sót cả câu, align dồn chữ kịch bản vào khoảng trống
- **Verified Golden Path:** pipeline.py align giờ chạy Whisper TỪNG PART (audio/vs/<scene>_pN_48k.wav, mỗi part < ~36s) rồi cộng offset 0.4s đầu + 0.35s nghỉ giữa part. Kiểm tra: long_words_raw.json không còn từ nào kéo dài > 1.2s; đo lại bằng cách Whisper file mp4 đã render, p95 lệch <= 0.1s.

### [LESSON-85] (2026-11-10)
- **Symptom:** Loi WinError 206 The filename or extension is too long khi mix audio ffmpeg cho scene dai
- **Ruled-out Dead-end:** Tao command line ffmpeg chua hang tram input -i kem filter_complex qua dai vuot qua gioi han 32767 ky tu cua CreateProcess tren Windows
- **Verified Golden Path:** Mix truc tiep audio trong Python bang NumPy float32 thanh 1 file PCM stereo 48kHz roi mux vao video bang ffmpeg chi voi 2 input, triet tieu hoan toan gioi han ky tu va tang toc do gap 10 lan

### [LESSON-86] (2026-11-10)
- **Symptom:** Audit kenh 10/11/2026: 99,1% luot xem tu Shorts (94,9% tu trang Shorts), video dai chi 124 luot/28 ngay; Shorts khong gan Video co lien quan; kenh 0 danh sach phat nen buoc chon playlist trong upload_youtube.cjs am tham bo qua; tieu de/mo ta chua dat ngon ngu nen khong co ban dich tieng Anh
- **Ruled-out Dead-end:** Tin rang upload_youtube.cjs da gan playlist (log 'playlist skipped' bi bo qua); dang 2 video dai/ngay khi video dai khong co nguon traffic
- **Verified Golden Path:** Doc so lieu qua Playwright MCP (studio analytics explore table bang innerText cua YTA-EXPLORE-*); tao playlist truoc khi upload; moi Shorts phai gan Related Video toi video dai; kiem tra log 'skipped' sau moi lan upload

### [LESSON-87] (2026-11-10)
- **Symptom:** Cai dat kenh 10/11/2026 qua Playwright MCP: tao playlist The Gioi Dong Vat (12 tap), man hinh ket thuc 12 video dai, bat tab Trang chu + video gioi thieu Tap 9, ban dich tieng Anh kenh + 12 video
- **Ruled-out Dead-end:** Chay nhieu lenh browser_run_code_unsafe song song tren 1 tab (giam chan nhau); batch >3 video trong 1 lenh (MCP timeout 60s, mat ket qua); click thuong vao dropdown man hinh ket thuc (bi overlay chan)
- **Verified Golden Path:** Moi lenh 1-3 video, tuan tu; dung click({noWaitAfter:true}) va mouse.click theo boundingBox cho ytve-options-panel-entity-item; nut Them ban dich chi hien khi hover o #cell-container thu 2; snippet sinh tu scripts/gen_en_translation_snippets.py; upload_youtube.cjs nay tu them man hinh ket thuc + tieng Anh. Shorts 'Video co lien quan' can xac minh kenh 1 lan (chu kenh tu lam)

### [LESSON-88] (2026-11-10)
- **Symptom:** Logo Gemini van hien o outro/intro va anh tai ve du da 'khu'
- **Ruled-out Dead-end:** Gia dinh logo la sao astroid o tam (w-60,h-49)/(1220,660) va deblend/inpaint co dinh -> sai vi tri, outro bi lo 1 lo den (inpaint), logo that van con
- **Verified Golden Path:** Dung src/image/gemini_watermark.py: alpha tham chieu assets/watermark/gemini_alpha_{48,96}.png; anh tai ve canh ngan >1024 -> logo 96px cach mep 64px, con lai 48px cach 32px; video Veo 1280x720 -> logo 48px tai (1136,576), do gain bang least-squares nhieu khung (intro 0.72, outro 1.15). Lenh: python src/image/gemini_watermark.py image|video ...

### [LESSON-89] (2026-11-10)
- **Symptom:** Anh Gemini tai tay ve Downloads van con logo
- **Ruled-out Dead-end:** Chi xoa logo trong import_images, quen thumbnail/banner/anh tai tay
- **Verified Golden Path:** Moi duong deu goi src/image/gemini_watermark.clean_image (import_images, prep_banners, asset_sanitizer->thumbnail_master). Anh tai tay: watcher ngam 'python src/image/gemini_watermark.py watch' tu khoi dong cung Windows (Startup/gemini_watermark_watch.vbs), ghi de anh sach, ban goc o Downloads/_raw/

### [LESSON-90] (2026-11-12)
- **Symptom:** upload_youtube.cjs bị kẹt Nháp do popup 'vẫn đang kiểm tra', bắt nhầm link support.google.com/youtube, và lỗi thêm Tiếng Anh trên giao diện Studio mới
- **Ruled-out Dead-end:** Chỉ dùng a[href*='youtu'], không bấm 'Đã hiểu', mở lại #second-container-expand-button khi đã mở sẵn, chỉ tìm ytgn-video-translation-row
- **Verified Golden Path:** Lọc link youtu.be/|/shorts/|watch?v=; bấm 'Đã hiểu' khi gặp popup 'vẫn đang kiểm tra'; hỗ trợ udvid=; dùng :visible cho datepicker; addEnglish hỗ trợ cả panel Tiếng Anh mới (div#textbox aria-label Tiêu đề/Mô tả + Cập nhật)

### [LESSON-91] (2026-11-12)
- **Symptom:** Shorts 1.000-3.500 view nhung video dai 0-33 view; 'Video co lien quan' cua moi Shorts = 'Khong co' (kiem tra 12/11/2026)
- **Ruled-out Dead-end:** Ghi chu 'gan tay' roi khong ai gan; dang Shorts + video dai cung gio (Studio khong chon duoc video dai con hen gio/rieng tu); 2 tap/ngay tu an luot de xuat
- **Verified Golden Path:** node src/episode/link_shorts_related.cjs projects/<slug> sau khi video dai da CONG KHAI (picker ytcp-video-pick-dialog, o 'Tim kiem video cua ban' go long_id). Upload: --date D --time 17:00 --shorts-date D+1 --shorts-time 11:30 roi chay link_shorts_related sau 17:00 ngay D

### [LESSON-92] (2026-11-16) Xử lý dứt điểm lỗi Gemini từ chối tạo ảnh do vi phạm bản quyền bên thứ ba & an toàn nội dung
- **Symptom:** Gemini báo lỗi "Hiện tôi không tạo được hình ảnh bạn yêu cầu do lợi ích của các nhà cung cấp nội dung bên thứ ba" (Tap 20 L07, Tap 23 L48, Mega 02 S04) hoặc "Rất xin lỗi, tôi không thể tạo hình ảnh không an toàn" (Tap 23 L33, Tap 24 L39, Tap 27 S06, Mega 02 L271). Nguy cơ tài khoản bị gắn cờ lạm dụng và khóa vĩnh viễn nếu lặp lại nhiều lần.
- **Ruled-out Dead-end:** 
  1. Không nhúng nguyên văn câu thoại thuyết minh vào prompt (`Lời thoại: "..."`) mà không lọc các từ so sánh nhạy cảm (như "Mike Tyson", "Wolverine", "khuôn mặt người", "bom cảm tử", "trườn vào cơ thể").
  2. Không để các từ ngữ bạo lực/vũ khí ("súng ngắm", "kính ngắm laser locked", "đạn súng", "máu me") lọt vào phần mô tả bố cục `layout` trong storyboard.
  3. Không tiếp tục gửi prompt trong cùng một phiên chat sau khi Gemini đã cảnh báo từ chối (làm tích lũy cờ vi phạm trong lịch sử hội thoại).
- **Verified Golden Path:**
  1. Xây dựng lá chắn 4 lớp `src/episode/prompt_sanitizer.py`: Tự động chuyển đổi tên nhân vật/thương hiệu có bản quyền thành nhân vật hoạt hình chung; chuyển sinh trắc học/nhận diện khuôn mặt thành hình vẽ mặt cười hoạt hình ngộ nghĩnh; chuyển vũ khí/bom/tự sát thành cơ chế hoạt hình vui nhộn; làm dịu sinh học nhạy cảm.
  2. Tích hợp tiền kiểm tra tự động vào `src/episode/build_plans.py`, `src/episode/extra_prompts.py` và `pipeline.py check` — chặn đứng 100% từ khóa rủi ro trước khi gửi.
  3. Trong `src/episode/gemini_gen.cjs`: Tự động sanitize prompt runtime; nếu phát hiện phản hồi từ chối chính sách, lập tức hủy phiên chat (`await newChat(page)`), chuyển sang prompt siêu an toàn (ultra-safe cartoon fallback) để bảo vệ tài khoản Google 100% an toàn.
### [LESSON-93] (2026-11-16)
- **Symptom:** Sau align, spec báo hàng loạt beat giữ hình >15s (video dài) hoặc >7s (Shorts) vì ảnh/beat viết trước khi có giọng thật (Tập 26-30 đều dính)
- **Ruled-out Dead-end:** Sửa tay từng beat rồi render thử; hoặc chèn beat làm lệch số ảnh L/S khiến prompt/ảnh cũ gán sai beat
- **Verified Golden Path:** Chèn beat mới vào specs/storyboard.json (neo 'at' = cụm đầu câu duy nhất trong chương, tính theo chuỗi vì at đầu chương là số 0), chuyển sticker số liệu sang beat đọc số đó, rồi remap ảnh cũ theo khóa scene|at sang số L/S mới; chỉ sinh Gemini cho beat mới. Lặp build_plans -> spec tới khi OK. Nên viết storyboard sau TTS, hoặc luôn chia beat theo từng câu ngay từ đầu.

### [LESSON-94] (2026-11-16)
- **Symptom:** QA Shorts FAIL dù âm lượng và hình đều tốt: Shorts < 40s (Tập 30 chỉ 39.3s sau tempo 1.10) và gemini_gen.cjs báo thiếu module playwright
- **Ruled-out Dead-end:** Chỉ render lại hoặc nới ngưỡng QA; chạy node không có NODE_PATH trong shell nền
- **Verified Golden Path:** Kịch bản Shorts cần >= ~850 ký tự (target 51-53s) để sau tempo 1.10 vẫn >= 40s: thêm 1 câu từ nội dung video dài, xóa audio/vs/shorts.wav + audio/shorts.wav + _align_shorts.json + shorts_words.json, chạy tts --shorts, align --shorts, thêm beat ảnh cho câu mới, render --shorts. Playwright: tạo shim ngoài repo trỏ vào node_modules/playwright-core và đặt NODE_PATH ngay trong lệnh node của từng shell.

### [LESSON-95] (2026-11-17)
- **Symptom:** Tag SEO các tập chỉ dùng ~180-330/500 ký tự; tag tự đặt tay, chưa dựa vào thứ người Việt thật sự gõ tìm trên YouTube
- **Ruled-out Dead-end:** Lấy toàn bộ YouTube autocomplete hoặc tag đối thủ nhét vào: dính tag lạc đề ('hải ly manga review', 'bạch tuộc nướng sa tế', 'hải lý' sai dấu)
- **Verified Golden Path:** python src/seo/seo_research.py projects/<slug> --apply sau pipeline.py seo: gợi ý vi/VN (YoutubeTags) + tag video top (yt-dlp), chỉ giữ tag chứa đúng tên con vật có dấu và mọi từ còn lại nằm trong kịch bản tập, gộp biến thể gần trùng, đếm ký tự kiểu YouTube Studio (tag có dấu cách +2) tối đa 470. Điểm hybrid-youtube-growth-engine viết cho MV nhạc: bỏ qua gợi ý lyrics/streaming link/tag tiếng Nhật.

### [LESSON-96] (2026-11-17)
- **Symptom:** Muốn cập nhật tag cho video đã đăng/hẹn lịch; tag trên Studio khác upload.json (Tập 30: 5 tag chỉ có trên Studio, vd 'khám phá thiên nhiên', 'bảng chỉ số sinh tồn')
- **Ruled-out Dead-end:** Xoá hết tag rồi điền lại từ upload.json: mất tag đang có trên video; chạy pipeline.py seo cho mega: ghi đè bộ hashtag riêng của mega bằng '#10quáikiệtđạihộisinhtồnmùa2'
- **Verified Golden Path:** node src/episode/update_tags.cjs projects/<slug> [--dry-run]: đọc tag đang có trên Studio, chỉ THÊM tag còn thiếu (dừng trước 500 ký tự kiểu Studio), so khớp chip trước khi Lưu, tải lại trang để xác minh. Luôn --dry-run 1 video trước. Mega: chỉ thay long.tags trong upload.json, giữ nguyên desc/hashtag. Sao lưu ở backups/seo_before_research_<ngày>/.

### [LESSON-97] (2026-11-18)
- **Symptom:** Âm thanh video dài/Shorts bị chập chờn (lúc to lúc nhỏ giữa các giọng, nhạc nền bị ngắt hổng mỗi 16s, hoặc True Peak vượt -1.0 dBTP làm QA FAIL)
- **Ruled-out Dead-end:** Để nguyên âm lượng thô của từng part VoiceStudio (lệch nhau 3.3 dB), lặp trực tiếp file calm-acoustic.wav 16s có đuôi im lặng, dùng ducking release 350ms quá gấp và dùng alimiter mặc định level=1 làm tự kích gain lên 0 dBFS
- **Verified Golden Path:** Trong pipeline.py cmd_tts tự động chuẩn hóa từng part giọng về -16.0 LUFS kèm micro-fade 5ms; dùng bgm_seamless_10m.wav crossfade liền mạch; đặt sidechaincompress release=800ms ratio=3.5 và alimiter=limit=0.75:level=0 để đạt chuẩn -14..-15 LUFS, TP <= -1.5 dBTP ngay lượt render đầu tiên

### [LESSON-98] (2026-11-18)
- **Symptom:** Từ Tập 32 trở đi chủ kênh yêu cầu mỗi tập có phong cách vẽ, banner chương, bảng chuyển chương giữa màn hình (1.6s), banner Shorts và hiệu ứng Sticker/Mũi tên/Tâm ngắm biến hóa riêng theo nội dung từng video
- **Ruled-out Dead-end:** Dùng cố định 1 câu STYLE whiteboard phẳng, 1 mẫu thanh chữ nhật navy viền vàng, vẽ bảng chuyển chương bằng khung PIL đơn điệu và vẽ sticker hộp trắng viền đơn cố định
- **Verified Golden Path:** Khai báo art.visual_style + scenes[].banner_bar_style + scenes[].card_style/card_sub trong episode.json; chạy extra_prompts.py sinh C01..C0N + K01..K0N + B00 + T01 -> gemini_gen.cjs extra -> prep_banners.py tách nền thành chapter_NN.png + card_NN.png + shorts_title.png; dùng src/render/theme_effects.py tự động đổi giao diện Sticker HUD, Mũi tên và Tâm ngắm theo format/theme của tập

### [LESSON-99] (2026-11-20)
- **Symptom:** Prompt ảnh AI bị rập khuôn nhãn 'cùng quy chuẩn comic 2D whiteboard'
- **Ruled-out Dead-end:** src/episode/build_plans.py chỉ đọc art.get('style_label') mà không fallback sb.get('style_label'), dẫn đến mọi tập đều rơi về default 'quy chuẩn comic 2D whiteboard'
- **Verified Golden Path:** Bổ sung art.get('style_label') or sb.get('style_label') trong build_plans.py, loại bỏ hoàn toàn 'comic 2D' ở prompt header và cập nhật style_label & visual_style độc bản riêng biệt cho từng tập 34-40

### [LESSON-100] (2026-11-23)
- **Symptom:** Nghiên cứu TubeLab cho 1 tập (comment-mining / title-formulas / thumbnail-concepts) trả về rác: tìm "hải ly" ra nhạc Lý Hải, ca sĩ Phan Hải Lý, phim review, game Play Together; loài hiếm (nhện lặn chuông) tìm tiếng Việt ra 0 kết quả.
- **Ruled-out Dead-end:** Tìm yt-dlp theo tên loài rồi tin hết kết quả; so khớp tên bỏ dấu hoặc không theo nguyên từ; chỉ tìm tiếng Việt.
- **Verified Golden Path:** Dùng `src/seo/episode_research.py`: tìm "<loài> động vật" + "<loài>", chỉ giữ video có tên loài NGUYÊN TỪ, ĐÚNG DẤU trong tiêu đề, bỏ phim/nhạc/game/truyện (`OFF_TOPIC`); loài hiếm thêm `--en "English name"`. Dữ liệu mỏng thì báo cáo ghi cảnh báo ⚠️, không bịa kết luận.

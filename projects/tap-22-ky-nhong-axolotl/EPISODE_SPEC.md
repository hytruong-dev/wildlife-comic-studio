# TẬP 22 — KỲ NHÔNG AXOLOTL · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-22-ky-nhong-axolotl`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-22-ky-nhong-axolotl`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F5` · **Persona giọng:** `nha_khoa_hoc` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Kỳ Nhông Axolotl |
| Tiêu đề YouTube | Sinh Vật Bị Mất Não & Thủng Tim Vẫn Tự Mọc Lại Không Sẹo?! |
| Video dài | `renders/tap-22-ky-nhong-axolotl_long.mp4` — 9:52.3 (592.3s) |
| Shorts | `renders/tap-22-ky-nhong-axolotl_shorts.mp4` — 0:54.5 (54.5s) |
| Thumbnail | `renders/tap-22-ky-nhong-axolotl_thumbnail.jpg` |
| Số hình | dài 80 beat / 80 ảnh riêng; Shorts 12 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/80 của video YouTube về Kỳ Nhông Axolotl). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán. Nhân vật phụ cố định: ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước; cô trợ lý phòng thí nghiệm hoạt hình mặc áo blouse xanh nhạt đeo thẻ nhân viên. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — KHỦNG LONG 6 SỪNG GIỮ NỤ CƯỜI ẤU TRÙNG
*Badge:* `HỒ SƠ MẪU VẬT` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene01_p0.wav` (490 ký tự) · mood `tram_bi_an`

```text
Nhật ký phòng thí nghiệm, ca trực nửa đêm. Đèn chiếu sáng chuyển sang sắc tím huỳnh quang, hệ thống cảm biến bắt đầu ghi nhận sóng sinh học từ bể kính số hai mươi hai. Giữa làn nước trong veo, một sinh vật kỳ dị đang lơ lửng bồng bềnh... Toàn thân màu hồng phấn mọng nước như kẹo bông gòn. Trên đầu xòe ra sáu chiếc sừng lông xù màu đỏ thẫm rung rinh trong nước. Và đặc biệt nhất là khuôn mặt: hai chấm mắt đen tròn xoe cùng khóe miệng luôn nở một nụ cười toe toét ngây thơ đến mức kỳ quặc!
```
**Part 1** → `audio/vs/scene01_p1.wav` (116 ký tự) · 🎭 cameo `co_tro_ly`

```text
Viện trưởng ơi, mẫu vật này nhìn cưng xỉu như thú bông, đưa vào phòng thí nghiệm thử thách chi cho tội nghiệp vậy ạ?
```
**Part 2** → `audio/vs/scene01_p2.wav` (479 ký tự) · mood `hao_hung`

```text
[surprise-oh] Trợ lý chớ vội để vẻ mặt ngây thơ của mẫu vật đánh lừa! [laughter] Đây là Kỳ Nhông Axolotl, sinh vật đặc hữu của vùng hồ Xô-chi-min-cô ở Mê-hi-cô, còn được dân gian gọi bằng cái tên cực kỳ kiêu hãnh: Khủng Long Sáu Sừng! Kích thước một cá thể trưởng thành dài khoảng hai mươi đến ba mươi xăng-ti-mét. Nhưng điều khiến cả giới sinh học thế giới phải ngả mũ bái phục không nằm ở vẻ ngoài đáng yêu, mà là danh hiệu tối thượng chúng tôi đặt cho nó: Chiến Thần Tái Sinh!
```
**Part 3** → `audio/vs/scene01_p3.wav` (594 ký tự) · mood `nghiem_trang_gia`

```text
Tạo hóa đã ban cho sinh vật này một hiện tượng kỳ lạ bậc nhất hành tinh gọi là ấu nhi vĩnh viễn. Nghĩa là dù đã sống tới mười lăm năm và sinh con đẻ cái bình thường, cơ thể nó vẫn từ chối lớn lên, mãi mãi giữ nguyên hình hài của một đứa trẻ sơ sinh dưới nước! Sáu chiếc sừng xù xì kia thực chất là mang ngoài chứa đầy mạch máu để thở. Và chính vì giữ mãi thể trạng non nớt của phôi thai, tế bào của nó sở hữu năng lực hồi sinh thần thánh thách thức mọi định luật y học! Đêm nay, tôi tuyên bố kích hoạt hệ thống thử thách năm cấp độ cực hạn để kiểm tra giới hạn sinh tồn của Chiến Thần Tái Sinh!
```

### scene02 — MỌC LẠI CHÂN TAY HOÀN CHỈNH TỪ KHỐI TẾ BÀO MẦM
*Thẻ chương:* MỌC LẠI NGUYÊN VẸN CẢ CÁNH TAY TRONG 30 NGÀY

*Badge:* `CẤP ĐỘ 1: TỨ CHI` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene02_p0.wav` (400 ký tự) · mood `hao_hung`

```text
Kích hoạt Cấp độ một: Thử thách tái tạo tứ chi! Hãy tưởng tượng một kịch bản tồi tệ xảy ra trong tự nhiên: một con cá đói khát lao tới đớp đứt lìa cánh tay trước của chú kỳ nhông. Ở con người hay bất kỳ loài thú có vú nào, mất một cánh tay là vĩnh viễn mất đi. Cơ thể chúng ta sẽ nhanh chóng hình thành một lớp mô sẹo xơ cứng gồ ghề để bịt kín vết thương, chấm dứt hoàn toàn khả năng mọc lại chi mới.
```
**Part 1** → `audio/vs/scene02_p1.wav` (344 ký tự) · mood `hao_hung`

```text
Nhưng tại bàn thí nghiệm của Chiến Thần Tái Sinh, đồng hồ đếm ngược bắt đầu vận hành một phép màu sinh học! Chỉ trong vòng chưa đầy hai mươi bốn giờ đầu tiên, các tế bào da xung quanh đã bò thần tốc qua miệng vết thương để tạo thành một lớp màng bảo vệ gọi là biểu mô vết thương. Không hề có máu chảy đầm đìa, không hề có nhiễm trùng nguy hiểm!
```
**Part 2** → `audio/vs/scene02_p2.wav` (395 ký tự) · mood `don_dap`

```text
Và ngay dưới lớp biểu mô ấy, điều kỳ diệu nhất bắt đầu xuất hiện: một khối tế bào mầm đặc biệt mang tên Bờ-lát-xtê-ma được kích hoạt! [surprise-wa] Đây là lúc khoa học phải kinh ngạc: các tế bào cơ bắp, tế bào xương, tế bào mạch máu đã trưởng thành tại vết cắt bỗng nhiên... tự bẻ ngược bánh xe thời gian, rũ bỏ thân phận cũ để quay trở lại trạng thái tế bào gốc sơ khai như lúc còn trong trứng!
```
**Part 3** → `audio/vs/scene02_p3.wav` (323 ký tự) · mood `don_dap`

```text
Khối tế bào mầm Bờ-lát-xtê-ma này phân chia điên cuồng với độ chính xác tuyệt đối như một máy in ba đê sinh học tự nhiên! Tuần thứ nhất, một chồi thịt nhỏ nhú ra. Tuần thứ hai, chồi thịt kéo dài và bắt đầu phân nhánh khớp khuỷu tay. Đến tuần thứ tư, năm ngón tay nhỏ xíu màu hồng phấn bắt đầu tách rời rõ rệt! [surprise-oh]
```
**Part 4** → `audio/vs/scene02_p4.wav` (510 ký tự) · mood `hao_hung`

```text
Sau đúng ba mươi đến bốn mươi ngày, một cánh tay hoàn chỉnh mới toanh đã mọc lại nguyên vẹn một trăm phần trăm: từ tủy xương, cơ bắp, mạch máu cho đến các đầu dây thần kinh điều khiển cử động tinh vi! Các nhà khoa học từng làm thí nghiệm cắt đi cắt lại hàng trăm lần trên cùng một vị trí của Chiến Thần Tái Sinh, và kết quả mỗi lần đều mọc lại hoàn hảo như đúc, không để lại lấy một vết sẹo nhỏ, và đặc biệt nhất là không bao giờ bị đột biến thành tế bào ung thư! [laughter] Cấp độ một: Vượt qua dễ như ăn kẹo!
```

### scene03 — TÁI TẠO TỦY SỐNG VÀ BƠI LỘI BÌNH THƯỜNG SAU VÀI TUẦN
*Thẻ chương:* BẮC CẦU TỦY SỐNG VÀ XÓA BỎ MỌI MÔ SẸO LIỆT

*Badge:* `CẤP ĐỘ 2: TỦY SỐNG` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene03_p0.wav` (409 ký tự) · mood `nghiem_trang_gia`

```text
Trợ lý, nâng độ khó lên Cấp độ hai: Thử thách tổn thương hệ thần kinh trung ương! Đối với loài người, đứt tủy sống là bản án chung thân khủng khiếp nhất của y học hiện đại. Tủy sống là đại lộ thông tin kết nối bộ não với toàn bộ cơ thể. Khi đại lộ đó bị cắt đứt, các tế bào hình sao sẽ lập tức dựng lên một bức tường mô sẹo dày đặc ngăn cản tín hiệu, khiến nạn nhân bị liệt vĩnh viễn không thuốc nào chữa nổi.
```
**Part 1** → `audio/vs/scene03_p1.wav` (112 ký tự) · 🎭 cameo `co_tro_ly`

```text
Báo cáo viện trưởng, máy quét huỳnh quang phát hiện vết đứt tủy sống của mẫu vật đang tự phát tín hiệu hồi phục!
```
**Part 2** → `audio/vs/scene03_p2.wav` (367 ký tự) · mood `don_dap`

```text
[surprise-oh] Nhìn vào màn hình hiển vi điện tử đi các trợ lý! Trong tủy sống của Chiến Thần Tái Sinh, đội quân tế bào biểu mô thần kinh mang tên Ê-pen-đi-mô-gờ-li-an lập tức nhận lệnh khẩn cấp! Thay vì tạo sẹo ngăn chặn như ở con người, những tế bào này phân chia với tốc độ vũ bão và vươn dài ra hai đầu để bắc một chiếc cầu sinh học xuyên qua khoảng trống đứt gãy!
```
**Part 3** → `audio/vs/scene03_p3.wav` (291 ký tự) · mood `hao_hung`

```text
Chiếc cầu biểu mô thần kinh ấy tiết ra các phân tử dẫn đường hóa học cực kỳ tinh vi, ngăn chặn hoàn toàn phản ứng viêm sẹo xơ cứng. Hàng ngàn sợi trục thần kinh bị đứt liền nương theo chiếc cầu đó mà mọc xuyên qua, tìm đúng đầu nối cũ bên kia chiến tuyến để kết nối lại từng xung điện li ti!
```
**Part 4** → `audio/vs/scene03_p4.wav` (525 ký tự) · mood `hao_hung`

```text
Chỉ sau ba đến bốn tuần ngắn ngủi, toàn bộ bó dây thần kinh tủy sống đã hàn gắn liền mạch một trăm phần trăm! Chiến Thần Tái Sinh lại phe phẩy chiếc đuôi bơi lượn thoăn thoắt trong bể nước với dáng vẻ ung dung tự tại, hoàn toàn không hề có một chút triệu chứng tê liệt hay suy giảm phản xạ vận động nào! [laughter] Các viện nghiên cứu thần kinh hàng đầu thế giới đang dồn hàng chục triệu đô la vào ca bệnh này với hy vọng một ngày nào đó tìm ra chìa khóa chữa lành cho các bệnh nhân bại liệt! Cấp độ hai: Hoàn thành xuất sắc!
```

### scene04 — CẮT 1/3 TÂM THẤT TIM VÀ MỌC LẠI TẾ BÀO NÃO BỘ
*Thẻ chương:* CẮT BỎ 1/3 TRÁI TIM VẪN TỰ ĐẬP VÀ MỌC LẠI SAU 30 NGÀY

*Badge:* `CẤP ĐỘ 3: TIM & NÃO` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene04_p0.wav` (281 ký tự) · mood `tram_bi_an`

```text
Cảnh báo toàn phòng thí nghiệm: Chúng ta bước vào Cấp độ ba — Thử thách nội tạng sinh tử! Lần này, mục tiêu không còn là tay chân hay da thịt bên ngoài nữa. Chúng ta đưa lưỡi dao vi phẫu chạm thẳng vào hai cơ quan tối thượng quyết định sự sống còn của sinh vật: Trái tim và Bộ não!
```
**Part 1** → `audio/vs/scene04_p1.wav` (430 ký tự) · mood `nghiem_trang_gia`

```text
Các nhà khoa học tim mạch đã thực hiện một cuộc phẫu thuật không tưởng: dùng kéo vi phẫu cắt phăng tới một phần ba tâm thất dưới đáy trái tim của chú kỳ nhông! Ở con người, một vết thủng nhỏ hay một cơn nhồi máu cơ tim cũng đủ để giết chết hàng triệu tế bào cơ tim không thể thay thế, để lại vết sẹo xơ vĩnh viễn dẫn tới suy tim tử vong. Nhưng khi nhìn vào lồng ngực trong suốt của Axolotl, các nhà phẫu thuật phải dụi mắt ba lần!
```
**Part 2** → `audio/vs/scene04_p2.wav` (409 ký tự) · mood `don_dap`

```text
Ngay tại vùng biên vết cắt, các tế bào cơ tim còn lại tự kích hoạt thụ thể bề mặt đặc biệt, tự tháo dỡ các sợi tơ co bóp để quay về trạng thái tế bào phôi thai! Chúng phân chia ồ ạt, lấp đầy lỗ hổng máu chảy chỉ trong vài ngày, và sau ba mươi ngày, một phần ba trái tim bị mất đã mọc lại nguyên vẹn cả buồng tâm thất mới tinh, đập rộn ràng bơm máu khắp cơ thể mà không có một milimet mô sẹo nào! [surprise-wa]
```
**Part 3** → `audio/vs/scene04_p3.wav` (443 ký tự) · mood `don_dap`

```text
Chưa dừng lại ở đó! Trong công trình chấn động công bố trên tạp chí Science năm hai ngàn hai mươi hai bằng công nghệ giải trình tự không gian đơn bào, các nhà khoa học đã thử cắt bỏ một phần thùy não trước của chú kỳ nhông. Và kết quả khiến cả thế giới sửng sốt: các tế bào gốc biểu mô thần kinh lại thức giấc, chia thành từng lớp tế bào mới và tái cấu trúc lại toàn bộ các nơ-ron não bộ bị mất theo đúng sơ đồ phôi thai ban đầu! [surprise-oh]
```
**Part 4** → `audio/vs/scene04_p4.wav` (118 ký tự) · 🎭 cameo `co_tro_ly`

```text
Trời đất ơi viện trưởng ơi, nó vừa mọc lại cả một phần bộ não mà nhìn cái mặt vẫn cười toe toét ngây thơ y như cũ kìa!
```
**Part 5** → `audio/vs/scene04_p5.wav` (269 ký tự) · mood `hao_hung`

```text
[laughter] Bị cắt mất một góc não bộ mà nụ cười vẫn không hề biến mất! Khả năng tự sửa chữa bộ não và quả tim đã đưa Chiến Thần Tái Sinh bước vào hàng ngũ những sinh vật có cơ chế hồi phục kỳ ảo nhất từng được ghi nhận trong lịch sử tiến hóa của động vật có xương sống!
```

### scene05 — NHẬN GHÉP TẠNG XUYÊN CÁ THỂ VÀ GIẢI MÃ BỘ GEN 32 TỶ
*Thẻ chương:* DUNG NẠP MỌI MẢNH GHÉP VÀ BỘ GEN GẤP 10 LẦN CON NGƯỜI

*Badge:* `CẤP ĐỘ 4: GHÉP TẠNG` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene05_p0.wav` (424 ký tự) · mood `nghiem_trang_gia`

```text
Tăng công suất máy quét lên Cấp độ bốn: Thử thách ghép tạng xuyên cá thể! Trong y học ghép tạng của con người, kẻ thù số một luôn là hiện tượng thải ghép. Hệ miễn dịch của chúng ta cực kỳ hung dữ và cảnh giác: chỉ cần phát hiện một quả thận hay lá gan có kháng nguyên lạ từ người khác đưa vào, đội quân bạch cầu sẽ lập tức tổng tấn công tiêu diệt mảnh ghép đến cùng, buộc bệnh nhân phải uống thuốc ức chế miễn dịch suốt đời.
```
**Part 1** → `audio/vs/scene05_p1.wav` (516 ký tự) · mood `hao_hung`

```text
Thế nhưng trong cơ thể của Chiến Thần Tái Sinh, hệ miễn dịch lại hành xử như một đại sứ hòa bình đầy bao dung! Các nhà khoa học tại viện nghiên cứu đã làm những thí nghiệm kỳ lạ đến mức khó tin: lấy một cánh tay của chú kỳ nhông màu trắng bạch tạng ghép sang cơ thể một chú kỳ nhông màu xanh đen hoang dã. [surprise-oh] Thay vì đào thải, các tế bào đại thực bào của cơ thể tiếp nhận ân cần dọn dẹp tế bào chết, kết nối mạch máu và nuôi dưỡng cánh tay ghép đó hoạt động trơn tru như chính cánh tay ruột thịt của mình!
```
**Part 2** → `audio/vs/scene05_p2.wav` (447 ký tự) · mood `don_dap`

```text
Thậm chí trong những thí nghiệm giải phẫu kinh điển, người ta từng ghép thêm một chiếc đầu thứ hai hoặc một cánh tay phụ lên lưng của chú kỳ nhông, và cơ thể nó vẫn bình thản dung nạp, kết nối dây thần kinh và nuôi sống cả hai phần cơ thể một cách kỳ dị! [surprise-wa] Bí mật đằng sau sức mạnh bao la này nằm ở đâu? Năm hai ngàn mười tám, một bài báo chấn động trên tạp chí Tự Nhiên danh tiếng đã giải mã thành công toàn bộ bản đồ gen của Axolotl.
```
**Part 3** → `audio/vs/scene05_p3.wav` (438 ký tự) · mood `hao_hung`

```text
Các đồng nghiệp hãy chuẩn bị tinh thần đón nhận con số này: Bộ gen của chú kỳ nhông nhỏ bé này dài tới ba mươi hai tỷ cặp base — tức là lớn gấp hơn mười lần toàn bộ bộ gen của loài người chúng ta với chỉ ba tỷ cặp base! [surprise-oh] Cả một đại dương thông tin di truyền khổng lồ chứa hàng ngàn đoạn mã cổ xưa chuyên kích hoạt tái sinh mô đang được cơ thể nó bảo tồn nguyên vẹn suốt hàng trăm triệu năm qua! Cấp độ bốn: Hoàn thành mỹ mãn!
```

### scene06 — HOÁ THÚ MẤT SIÊU NĂNG LỰC VÀ BÓNG ĐEN BÍ ẨN
*Thẻ chương:* CÁI GIÁ CỦA SỰ TRƯỞNG THÀNH: ĐÁNH MẤT SỰ BẤT TỬ

*Badge:* `CẤP TỐI THƯỢNG` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (277 ký tự) · mood `tram_bi_an`

```text
Chúng ta bước vào Cấp độ tối thượng: Điều gì trên đời này có thể đánh bại được Chiến Thần Tái Sinh? Chặt chân chân mọc lại. Đứt tủy tủy nối liền. Thủng tim tim tự vá. Ghép tạng tạng dung nạp. Chẳng lẽ sinh vật này thực sự bất tử không có lấy một điểm yếu nào sao? [question-oh]
```
**Part 1** → `audio/vs/scene06_p1.wav` (431 ký tự) · mood `bi_hai`

```text
Và đây là cú bẻ lái triết lý sâu sắc nhất mà tạo hóa cài cắm vào hồ sơ của mẫu vật: Thứ vũ khí duy nhất tước đoạt siêu năng lực của nó... chính là sự trưởng thành! [sigh] Trong tự nhiên, tuyến giáp của Axolotl bị khiếm khuyết bẩm sinh nên không thể tự sản sinh đủ lượng hoóc-môn Tuy-rốc-xin để kích hoạt quá trình biến thái. Nó chọn sống cả đời dưới nước trong hình hài một đứa trẻ ngây thơ để bảo lưu năng lực tái sinh thần thánh.
```
**Part 2** → `audio/vs/scene06_p2.wav` (368 ký tự) · mood `don_dap`

```text
Nhưng khi các nhà khoa học trong phòng thí nghiệm can thiệp bằng cách tiêm trực tiếp hoóc-môn Tuy-rốc-xin vào cơ thể, chiếc đồng hồ sinh học bị cưỡng ép quay nhanh! Sáu chiếc sừng mang ngoài rực rỡ từ từ teo rụng. Phổi bên trong phồng to lên. Mi mắt bắt đầu khép mở. Toàn bộ cơ thể nó trèo lên cạn biến thành một con kỳ nhông hổ trưởng thành màu nâu xám! [surprise-oh]
```
**Part 3** → `audio/vs/scene06_p3.wav` (395 ký tự) · mood `bi_hai`

```text
Và cái giá phải trả cho sự lớn khôn là vô cùng tàn nhẫn: Khi đã bước lên cạn thành thú trưởng thành, siêu năng lực mọc lại tứ chi bị suy giảm nghiêm trọng, các vết thương bắt đầu hình thành mô sẹo xơ cứng, và tuổi thọ của nó tụt dốc thê thảm chỉ còn lại một nửa! Hóa ra để giữ được nụ cười bất tử vô ưu vô lo, tạo hóa bắt nó phải đánh đổi bằng cách mãi mãi không bao giờ được lớn lên! [laughter]
```
**Part 4** → `audio/vs/scene06_p4.wav` (465 ký tự) · mood `hao_hung`

```text
Tổng kết ghi chép phòng thí nghiệm số hai mươi hai: Chiến Thần Tái Sinh đạt điểm mười tuyệt đối cho bài kiểm tra sinh tồn! Kê đơn xuất viện: Cho mẫu vật bơi lội tung tăng trong làn nước mát và tuyệt đối cấm tiêm hoóc-môn ép lớn! Còn các trợ lý phòng thí nghiệm thì sao? Nếu được chọn giữa việc lớn lên thành người lớn nhiều âu lo, hay mãi mãi giữ nụ cười trẻ thơ và khả năng tự chữa lành mọi vết thương trong cuộc sống, bạn chọn cái nào? Hãy bình luận bên dưới nhé!
```
**Part 5** → `audio/vs/scene06_p5.wav` (551 ký tự) · mood `am_ap`

```text
Hồ sơ cấp độ tối thượng xin khép lại tại đây. Nhưng tập sau, phòng thí nghiệm của chúng ta sẽ chuyển thẳng xuống đáy biển sâu để đón tiếp một sinh vật quái đản bậc nhất hành tinh! Một cục thịt dài ngoằng không xương, không mắt, nhưng khi bị kẻ săn mồi dồn vào đường cùng, cơ thể nó có thể tự hóa lỏng thành một đống thạch nhớt nhầy nhụa, và trong tích tắc... bắn toàn bộ ruột gan phèo phổi của mình qua đường hậu môn để trói chặt kẻ thù rồi ung dung tẩu thoát! Đố các bạn biết bóng đen bí ẩn kỳ sau là loài vật nào? Hãy đoán ngay ở phần bình luận nhé!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Chuyện gì sẽ xảy ra nếu một con cá đói cắn đứt một phần ba trái tim hoặc cắt mất một mảng não bộ của con vật này? [laughter] Đối với chúng ta đó là dấu chấm hết, nhưng với Kỳ Nhông Axolotl, nó chỉ mất đúng ba mươi ngày để tự mọc lại nguyên vẹn một trăm phần trăm mà không để lại một vết sẹo nhỏ! Đây là loài Khủng Long Sáu Sừng sống ở Mê-hi-cô, dài ba mươi xăng-ti-mét với nụ cười toe toét ngây thơ. Nhờ hiện tượng ấu nhi vĩnh viễn không bao giờ trưởng thành, tế bào của nó có thể tự quay ngược thời gian thành tế bào gốc để tái tạo từ chân tay, đuôi, mắt cho đến tủy sống bị đứt đoạn! [surprise-wa] Thậm chí khi các nhà khoa học cắt bỏ một phần ba tâm thất tim hay ghép một cánh tay từ cá thể khác sang, cơ thể nó vẫn tự vá lành và dung nạp bình thường! [surprise-oh] Bộ gen của nó dài tới ba mươi hai tỷ cặp base, lớn gấp mười lần bộ gen con người! Bí mật duy nhất đánh bại được nó là sự lớn khôn: nếu bị ép tiêm hoóc-môn biến thái lên cạn, nó sẽ rụng mất sáu chiếc sừng và đánh mất luôn khả năng bất tử! Một chiến thần tái sinh chọn mãi mãi làm một đứa trẻ để giữ trọn nụ cười kỳ diệu!
```

**Whisper prompt:** `Kỳ Nhông Axolotl, Chiến Thần Tái Sinh, Khủng Long Sáu Sừng, Ambystoma mexicanum, Mê-hi-cô, Mexico, Xochimilco, Bờ-lát-xtê-ma, Blastema, Ependymoglial, Tuy-rốc-xin, Thyroxine, Stereo-seq, Nature, Science, 20cm, 30cm, 24 giờ, 30 ngày, 40 ngày, 1/3, 32 tỷ, 3 tỷ, 10 lần`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| hai mươi hai | 22 |
| hai mươi ba | 23 |
| hai mươi đến ba mươi xăng-ti-mét | 20-30cm |
| ba mươi xăng-ti-mét | 30cm |
| hai mươi xăng-ti-mét | 20cm |
| hai mươi bốn giờ | 24 giờ |
| ba mươi đến bốn mươi ngày | 30-40 ngày |
| ba mươi ngày | 30 ngày |
| bốn mươi ngày | 40 ngày |
| ba đến bốn tuần | 3-4 tuần |
| năm ngón tay | 5 ngón tay |
| hàng trăm lần | hàng trăm lần |
| hàng trăm | hàng trăm |
| một trăm phần trăm | 100% |
| một phần ba | 1/3 |
| ba ngăn | 3 ngăn |
| Năm hai ngàn mười tám | 2018 |
| năm hai ngàn mười tám | 2018 |
| năm hai ngàn hai mươi hai | 2022 |
| mười lăm năm | 15 năm |
| hàng trăm triệu năm | hàng trăm triệu năm |
| ba mươi hai tỷ | 32 tỷ |
| mười lần | 10 lần |
| ba tỷ | 3 tỷ |
| sáu chiếc sừng | 6 chiếc sừng |
| sáu sừng | 6 sừng |
| năm cấp độ | 5 cấp độ |
| cấp độ một | cấp độ 1 |
| cấp độ hai | cấp độ 2 |
| cấp độ ba | cấp độ 3 |
| cấp độ bốn | cấp độ 4 |
| cấp độ năm | cấp độ 5 |
| cấp một | cấp 1 |
| cấp hai | cấp 2 |
| cấp ba | cấp 3 |
| cấp bốn | cấp 4 |
| thứ nhất | thứ 1 |
| thứ hai | thứ 2 |
| thứ ba | thứ 3 |
| thứ tư | thứ 4 |
| thứ năm | thứ 5 |
| một nửa | 1/2 |
| điểm mười | điểm 10 |
| Mê-hi-cô | Mexico |
| Xô-chi-min-cô | Xochimilco |
| Bờ-lát-xtê-ma | Blastema |
| Ê-pen-đi-mô-gờ-li-an | Ependymoglial |
| Tuy-rốc-xin | Thyroxine |
| Tự Nhiên | Nature |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · KHỦNG LONG 6 SỪNG GIỮ NỤ CƯỜI ẤU TRÙNG · 82.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.7 (7.7s) | L01 | Nhật ký phòng thí nghiệm, ca trực nửa đêm. Đèn chiếu sáng chuyển sang sắc tím huỳnh quang, hệ thống cảm biến bắt đầu ghi nhận sóng sinh học từ bể kính số 22. |  | BÊN TRÁI ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước và cô trợ lý phòng thí nghiệm hoạt hình mặc áo blouse xanh nhạt đeo thẻ nhân viên đứng trước hệ thống máy tính phát sáng tím huỳnh quang; Ở GIỮA là bể kính số 22 phát sáng lung linh giữa ca trực nửa đêm. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b02 | 00:07.7–00:11.0 (3.4s) | L02 | Giữa làn nước trong veo, một sinh vật kỳ dị đang lơ lửng bồng |  | Bên trong làn nước trong veo của bể kính số 22, một sinh vật kỳ dị đang lơ lửng bồng bềnh tỏa ánh sáng tím mờ ảo. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b03 | 00:11.0–00:13.6 (2.5s) | L03 | bềnh... Toàn thân màu hồng phấn mọng nước như kẹo bông |  | Giữa làn nước trong veo, chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán lơ lửng bồng bềnh, toàn thân màu hồng phấn mọng nước mềm mại như kẹo bông gòn đáng yê |
| b04 | 00:13.6–00:17.1 (3.6s) | L04 | gòn. Trên đầu xòe ra 6 chiếc sừng lông xù màu đỏ thẫm rung rinh trong |  | Cận cảnh trên đầu chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán: sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm rung rinh xòe rộng trong nước như những chiếc |
| b05 | 00:17.1–00:23.9 (6.7s) | L05 | nước. Và đặc biệt nhất là khuôn mặt: hai chấm mắt đen tròn xoe cùng khóe miệng luôn nở một nụ cười toe toét ngây thơ đến mức kỳ quặc! |  | Khuôn mặt chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán cận cảnh chính diện: hai chấm mắt đen tròn xoe cùng khóe miệng luôn nở nụ cười toe toét ngây thơ ngộ |
| b06 | 00:23.9–00:30.7 (6.8s) | L06 | Viện trưởng ơi, mẫu vật này nhìn cưng xỉu như thú bông, đưa vào phòng thí nghiệm thử thách chi cho tội nghiệp vậy ạ? |  | BÊN TRÁI cô trợ lý phòng thí nghiệm hoạt hình mặc áo blouse xanh nhạt đeo thẻ nhân viên ôm tập hồ sơ bệnh án nghiêng đầu cưng nựng nhìn vào bể kính; BÊN PHẢI chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp  |
| b07 | 00:30.7–00:34.0 (3.3s) | L07 | Trợ lý chớ vội để vẻ mặt ngây thơ của mẫu vật đánh lừa! |  | BÊN TRÁI ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước nghiêm nghị lắc ngón tay cảnh báo; BÊN PHẢI trên màn hình máy quét phân tích sinh học hiện sơ đồ tế bào phát sáng rực rỡ. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b08 | 00:34.0–00:41.6 (7.7s) | L08 | Đây là Kỳ Nhông Axolotl, sinh vật đặc hữu của vùng hồ Xochimilco ở Mexico, còn được dân gian gọi bằng cái tên cực kỳ kiêu hãnh: Khủng Long Sáu Sừng! |  | Bản đồ hồ Xochimilco ở Mexico màu xanh ngọc ở BÊN TRÁI; BÊN PHẢI là chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán bơi kiêu hãnh đội chiếc vương miện Khủng L |
| b09 | 00:41.6–00:46.0 (4.3s) | L09 | Kích thước một cá thể trưởng thành dài khoảng 20-30cm. | **20-30 CM** · kích thước mẫu vật · R/350 · [0.68, 0.5] | Ở GIỮA chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán đứng thẳng cạnh chiếc thước đo chiều cao phòng thí nghiệm màu vàng có kẻ vạch đo kích thước. |
| b10 | 00:46.0–00:54.8 (8.9s) | L10 | Nhưng điều khiến cả giới sinh học thế giới phải ngả mũ bái phục không nằm ở vẻ ngoài đáng yêu, mà là danh hiệu tối thượng chúng tôi đặt cho nó: Chiến Thần Tái Sinh! |  | Các nhà khoa học thế giới đứng quỳ gối ngả mũ kính phục trước bục vinh danh của chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán với dải ruy băng danh hiệu Chi |
| b11 | 00:54.8–00:59.2 (4.3s) | L11 | Tạo hóa đã ban cho sinh vật này một hiện tượng kỳ lạ bậc nhất hành tinh gọi là ấu nhi vĩnh |  | chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán ngậm một chiếc núm vú giả em bé màu xanh hài hước, đứng cạnh chiếc đồng hồ thời gian bị khóa chặt ở số 0. |
| b12 | 00:59.2–01:06.6 (7.5s) | L12 | viễn. Nghĩa là dù đã sống tới 15 năm và sinh con đẻ cái bình thường, cơ thể nó vẫn từ chối lớn lên, mãi mãi giữ nguyên hình hài của một đứa trẻ sơ sinh | **15 NĂM** · ấu nhi vĩnh viễn · L/350 · [0.35, 0.48] | Cảnh gia đình hạnh phúc: chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán vừa bơi vừa trông đàn kỳ nhông con tung tăng, bảng lịch 15 năm lật trang bên cạnh. |
| b13 | 01:06.6–01:10.0 (3.4s) | L13 | dưới nước! Sáu chiếc sừng xù xì kia thực chất là mang ngoài chứa đầy mạch máu để |  | Kính hiển vi phóng to cấu trúc một chiếc sừng mang ngoài: mạng lưới mao mạch máu màu đỏ tươi dày đặc chạy sát bề mặt để hút oxy trong nước. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b14 | 01:10.0–01:16.2 (6.1s) | L14 | thở. Và chính vì giữ mãi thể trạng non nớt của phôi thai, tế bào của nó sở hữu năng lực hồi sinh thần thánh thách thức mọi định luật |  | chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán bơi giữa làn nước, xung quanh cơ thể tỏa hào quang tế bào phôi thai màu xanh ngọc lấp lánh như phép màu tái si |
| b15 | 01:16.2–01:22.2 (6.0s) | L15 | y học! Đêm nay, tôi tuyên bố kích hoạt hệ thống thử thách 5 cấp độ cực hạn để kiểm tra giới hạn sinh tồn của Chiến Thần Tái Sinh! |  | ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước gạt cần công tắc khởi động hệ thống thí nghiệm lớn; phía trên bảng đèn LED bật sáng dòng chữ THỬ THÁCH 5 CẤP ĐỘ CỰC HẠN. |

### scene02 · MỌC LẠI CHÂN TAY HOÀN CHỈNH TỪ KHỐI TẾ BÀO MẦM · 98.8s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.9 (9.9s) | L16 | Kích hoạt Cấp độ một: Thử thách tái tạo tứ chi! Hãy tưởng tượng một kịch bản tồi tệ xảy ra trong tự nhiên: một con cá đói khát lao tới đớp đứt lìa cánh tay trước của chú kỳ nhông. |  | Bảng điện tử hiện cấp độ 1: THỬ THÁCH TÁI TẠO TỨ CHI; BÊN PHẢI một con cá săn mồi hung dữ há to miệng lao tới cắn vào cánh tay chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tr |
| b02 | 00:09.9–00:20.8 (10.8s) | L17 | Ở con người hay bất kỳ loài thú có vú nào, mất một cánh tay là vĩnh viễn mất đi. Cơ thể chúng ta sẽ nhanh chóng hình thành một lớp mô sẹo xơ cứng gồ ghề để bịt kín vết thương, chấm dứt hoàn toàn khả năng mọc lại chi mới. |  | So sánh chia đôi: BÊN TRÁI cánh tay người bị thương để lại vết mô sẹo xơ cứng gồ ghề kèm dấu gạch chéo đỏ; BÊN PHẢI là dấu chấm hỏi khoa học. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b03 | 00:20.8–00:26.3 (5.5s) | L18 | Nhưng tại bàn thí nghiệm của Chiến Thần Tái Sinh, đồng hồ đếm ngược bắt đầu vận hành một phép màu sinh học! |  | chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán nằm thảnh thơi trên bàn thí nghiệm nước, bên cạnh chiếc đồng hồ cát 24 giờ đếm ngược phát sáng hào quang kỳ di |
| b04 | 00:26.3–00:35.4 (9.1s) | L19 | Chỉ trong vòng chưa đầy 24 giờ đầu tiên, các tế bào da xung quanh đã bò thần tốc qua miệng vết thương để tạo thành một lớp màng bảo vệ gọi là biểu mô vết thương. | **24 GIỜ** · khép kín vết thương · R/350 · [0.58, 0.46] | Mặt cắt phóng đại vết cắt cánh tay: trong 24 giờ, các tế bào da bò thần tốc phủ kín bề mặt vết thương tạo thành lớp màng biểu mô bảo vệ hoàn hảo. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b05 | 00:35.4–00:38.9 (3.5s) | L20 | Không hề có máu chảy đầm đìa, không hề có nhiễm trùng nguy hiểm! |  | Vết thương sạch sẽ không một giọt máu, các vi khuẩn gây nhiễm trùng bên ngoài bị lớp màng biểu mô chặn đứng hoàn toàn. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b06 | 00:38.9–00:45.9 (7.0s) | L21 | Và ngay dưới lớp biểu mô ấy, điều kỳ diệu nhất bắt đầu xuất hiện: một khối tế bào mầm đặc biệt mang tên Blastema được kích |  | Ngay dưới lớp da vết thương, một khối tế bào mầm Blastema màu hồng ngọc nhú lên phát sáng rực rỡ như mầm cây sinh học. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b07 | 00:45.9–00:50.6 (4.7s) | L22 | hoạt! Đây là lúc khoa học phải kinh ngạc: các tế bào cơ bắp, tế bào xương, tế bào mạch máu đã trưởng thành tại vết cắt bỗng |  | Kính hiển vi phóng to vết thương: các tế bào cơ bắp và xương trưởng thành bắt đầu có biểu hiện rung động lạ thường chuẩn bị phân tách. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b08 | 00:50.6–00:59.0 (8.3s) | L23 | nhiên... tự bẻ ngược bánh xe thời gian, rũ bỏ thân phận cũ để quay trở lại trạng thái tế bào gốc sơ khai như lúc còn trong trứng! Khối tế bào mầm Blastema |  | Sơ đồ chuyển hóa tế bào: tế bào cơ, xương, mạch máu xoay ngược bánh xe thời gian, rũ bỏ thân phận để trở lại thành tế bào gốc phôi thai tròn xoe. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b09 | 00:59.0–01:02.6 (3.6s) | L24 | này phân chia điên cuồng với độ chính xác tuyệt đối như một máy in ba đê sinh học tự |  | Mô hình máy in 3D sinh học hoạt hình đang quét tia laser xanh in từng lớp xương, cơ bắp và mạch máu cho cánh tay mới của chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe |
| b10 | 01:02.6–01:07.8 (5.3s) | L25 | nhiên! Tuần thứ 1, một chồi thịt nhỏ nhú ra. Tuần thứ 2, chồi thịt kéo dài và bắt đầu phân nhánh khớp khuỷu |  | Timeline tiến trình 4 tuần: tuần 1 nhú chồi thịt nhỏ; tuần 2 chồi kéo dài phân nhánh khuỷu tay; ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước cầm kính lúp ghi chép tiến độ. |
| b11 | 01:07.8–01:12.5 (4.6s) | L26 | tay. Đến tuần thứ 4, 5 ngón tay nhỏ xíu màu hồng phấn bắt đầu tách rời rõ rệt! | **5 NGÓN TAY** · hoàn chỉnh như mới · R/350 · [0.62, 0.5] | Cận cảnh bàn tay mới nhú của chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán: năm ngón tay nhỏ xíu màu hồng phấn bắt đầu tách rời rõ rệt, cử động ngọ nguậy li |
| b12 | 01:12.5–01:22.2 (9.8s) | L27 | Sau đúng 30-40 ngày, một cánh tay hoàn chỉnh mới toanh đã mọc lại nguyên vẹn 100%: từ tủy xương, cơ bắp, mạch máu cho đến các đầu dây thần kinh điều khiển cử động tinh vi! | **30-40 NGÀY** · mọc lại 100% · L/350 · [0.38, 0.48] | chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán giơ cánh tay mới mọc trắng hồng khỏe khoắn vỗ vỗ vào cánh tay kia, kiểm tra khớp xương và cơ bắp cử động trơn  |
| b13 | 01:22.2–01:32.5 (10.2s) | L28 | Các nhà khoa học từng làm thí nghiệm cắt đi cắt lại hàng trăm lần trên cùng một vị trí của Chiến Thần Tái Sinh, và kết quả mỗi lần đều mọc lại hoàn hảo như đúc, không để lại lấy một vết sẹo nhỏ, | **100 LẦN** · không hề tạo sẹo · R/350 · [0.65, 0.42] | Chiếc máy đếm số lần thí nghiệm nhảy số lên hàng trăm lần, mỗi lần cánh tay đều mọc lại hoàn hảo không sẹo. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b14 | 01:32.5–01:38.8 (6.4s) | L29 | và đặc biệt nhất là không bao giờ bị đột biến thành tế bào ung thư! Cấp độ một: Vượt qua dễ như ăn kẹo! |  | Biểu tượng tế bào ung thư bị vòng tròn gạch chéo đỏ bảo vệ; BÊN PHẢI chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán ngậm kẹo mút cười tít mắt, bảng cấp độ 1  |

### scene03 · TÁI TẠO TỦY SỐNG VÀ BƠI LỘI BÌNH THƯỜNG SAU VÀI TUẦN · 85.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.0 (8.0s) | L30 | Trợ lý, nâng độ khó lên Cấp độ hai: Thử thách tổn thương hệ thần kinh trung ương! Đối với loài người, đứt tủy sống là bản án chung thân khủng khiếp nhất của y học hiện |  | Bảng điện tử phòng lab chuyển sang chữ CẤP ĐỘ 2: TỔN THƯƠNG HỆ THẦN KINH; ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước giơ ngón tay chỉ lên màn hình. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b02 | 00:08.0–00:11.1 (3.1s) | L31 | đại. Tủy sống là đại lộ thông tin kết nối bộ não với toàn bộ |  | Mô hình tủy sống phát sáng chạy dọc sống lưng như một đại lộ cao tốc truyền xung điện kết nối não và cơ thể. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b03 | 00:11.1–00:19.0 (8.0s) | L32 | cơ thể. Khi đại lộ đó bị cắt đứt, các tế bào hình sao sẽ lập tức dựng lên một bức tường mô sẹo dày đặc ngăn cản tín hiệu, khiến nạn nhân bị liệt vĩnh viễn không thuốc nào chữa nổi. |  | Sơ đồ tủy sống người bị đứt: các tế bào hình sao dựng lên bức tường mô sẹo đen dày đặc chặn tín hiệu, biểu tượng xe lăn bị gạch chéo. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b04 | 00:19.0–00:25.7 (6.7s) | L33 | Báo cáo viện trưởng, máy quét huỳnh quang phát hiện vết đứt tủy sống của mẫu vật đang tự phát tín hiệu hồi phục! |  | cô trợ lý phòng thí nghiệm hoạt hình mặc áo blouse xanh nhạt đeo thẻ nhân viên reo lên chỉ tay vào màn hình máy quét huỳnh quang đang nhấp nháy luồng tín hiệu hồi phục màu xanh ngọc từ lưng mẫu vật. |
| b05 | 00:25.7–00:33.2 (7.5s) | L34 | Nhìn vào màn hình hiển vi điện tử đi các trợ lý! Trong tủy sống của Chiến Thần Tái Sinh, đội quân tế bào biểu mô thần kinh mang tên Ependymoglial lập tức nhận lệnh khẩn |  | Màn hình kính hiển vi điện tử: đội quân tế bào biểu mô thần kinh Ependymoglial màu tím huỳnh quang phân chia ồ ạt với tốc độ vũ bão. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b06 | 00:33.2–00:42.1 (8.9s) | L35 | cấp! Thay vì tạo sẹo ngăn chặn như ở con người, những tế bào này phân chia với tốc độ vũ bão và vươn dài ra hai đầu để bắc một chiếc cầu sinh học xuyên qua khoảng trống đứt gãy! |  | Sơ đồ tủy sống đứt gãy: các tế bào thần kinh vươn dài ra hai đầu tạo thành một chiếc cầu treo sinh học nối liền khoảng trống. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b07 | 00:42.1–00:49.2 (7.0s) | L36 | Chiếc cầu biểu mô thần kinh ấy tiết ra các phân tử dẫn đường hóa học cực kỳ tinh vi, ngăn chặn hoàn toàn phản ứng viêm sẹo xơ cứng. |  | Chiếc cầu biểu mô tiết ra các phân tử phát sáng dẫn đường hóa học, ngăn chặn hoàn toàn mô sẹo xơ cứng hình thành. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b08 | 00:49.2–00:57.5 (8.3s) | L37 | Hàng ngàn sợi trục thần kinh bị đứt liền nương theo chiếc cầu đó mà mọc xuyên qua, tìm đúng đầu nối cũ bên kia chiến tuyến để kết nối lại từng xung điện li ti! |  | Các sợi trục thần kinh men theo chiếc cầu mọc xuyên qua, các tia lửa xung điện li ti xẹt sáng kết nối hai đầu dây thần kinh. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b09 | 00:57.5–01:04.3 (6.8s) | L38 | Chỉ sau 3-4 tuần ngắn ngủi, toàn bộ bó dây thần kinh tủy sống đã hàn gắn liền mạch 100%! Chiến Thần Tái | **3-4 TUẦN** · hàn gắn tủy sống · L/350 · [0.35, 0.45] | Tờ lịch 3-4 tuần bóc trang rụng xuống, bó tủy sống đã hàn gắn trơn tru liền mạch 100% không một vết sẹo. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b10 | 01:04.3–01:14.5 (10.2s) | L39 | Sinh lại phe phẩy chiếc đuôi bơi lượn thoăn thoắt trong bể nước với dáng vẻ ung dung tự tại, hoàn toàn không hề có một chút triệu chứng tê liệt hay suy giảm phản xạ vận động nào! |  | chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán uốn lượn chiếc đuôi hồng bơi lội thoăn thoắt hình số 8 trong bể nước, phản xạ bơi lội nhanh nhẹn hoàn hảo. |
| b11 | 01:14.5–01:25.0 (10.5s) | L40 | Các viện nghiên cứu thần kinh hàng đầu thế giới đang dồn hàng chục triệu đô la vào ca bệnh này với hy vọng một ngày nào đó tìm ra chìa khóa chữa lành cho các bệnh nhân bại liệt! Cấp độ hai: Hoàn thành xuất sắc! |  | Tòa nhà viện nghiên cứu thần kinh quốc tế với biểu tượng ADN phát sáng và hy vọng mở ra chìa khóa chữa lành cho bệnh nhân bại liệt; bảng Cấp độ 2 bật đèn xanh PASS. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |

### scene04 · CẮT 1/3 TÂM THẤT TIM VÀ MỌC LẠI TẾ BÀO NÃO BỘ · 93.8s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.9 (7.9s) | L41 | Cảnh báo toàn phòng thí nghiệm: Chúng ta bước vào Cấp độ ba — Thử thách nội tạng sinh tử! Lần này, mục tiêu không còn là tay chân hay da thịt bên ngoài nữa. |  | Đèn còi báo động màu đỏ xoay tít, màn hình phòng lab hiện dòng chữ cảnh báo CẤP ĐỘ 3: THỬ THÁCH NỘI TẠNG SINH TỬ. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b02 | 00:07.9–00:13.7 (5.9s) | L42 | Chúng ta đưa lưỡi dao vi phẫu chạm thẳng vào hai cơ quan tối thượng quyết định sự sống còn của sinh vật: Trái tim và Bộ não! |  | Dao vi phẫu chạm vào mô hình đồ họa của Trái Tim và Bộ Não phát sáng lung linh giữa phòng thí nghiệm. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b03 | 00:13.7–00:20.5 (6.8s) | L43 | Các nhà khoa học tim mạch đã thực hiện một cuộc phẫu thuật không tưởng: dùng kéo vi phẫu cắt phăng tới 1/3 tâm thất dưới đáy trái tim của chú kỳ nhông! | **1/3 TIM** · cắt bỏ tâm thất · R/350 · [0.58, 0.5] | Kéo vi phẫu chuyên dụng cắt rời 1/3 góc tâm thất dưới đáy trái tim ba ngăn nhỏ xíu của chú kỳ nhông trên khay phẫu thuật trong suốt. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b04 | 00:20.5–00:29.2 (8.7s) | L44 | Ở con người, một vết thủng nhỏ hay một cơn nhồi máu cơ tim cũng đủ để giết chết hàng triệu tế bào cơ tim không thể thay thế, để lại vết sẹo xơ vĩnh viễn dẫn tới suy tim tử vong. |  | So sánh: mô hình trái tim người bị vết sẹo xơ đen xám sau cơn nhồi máu cơ tim, máy đo điện tim kêu tút dài báo động. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b05 | 00:29.2–00:33.7 (4.5s) | L45 | Nhưng khi nhìn vào lồng ngực trong suốt của Axolotl, các nhà phẫu thuật phải dụi mắt ba lần! |  | Các bác sĩ phẫu thuật dụi mắt kinh ngạc nhìn vào lồng ngực trong suốt của chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán: trái tim bị khuyết một góc vẫn tự đ |
| b06 | 00:33.7–00:41.2 (7.5s) | L46 | Ngay tại vùng biên vết cắt, các tế bào cơ tim còn lại tự kích hoạt thụ thể bề mặt đặc biệt, tự tháo dỡ các sợi tơ co bóp để quay về trạng thái tế bào phôi thai! |  | Phóng to vùng biên vết cắt tim: các tế bào cơ tim tháo dỡ sợi tơ co bóp, biến ngược thành tế bào phôi thai phân chia ồ ạt lấp kín lỗ hổng. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b07 | 00:41.2–00:52.6 (11.4s) | L47 | Chúng phân chia ồ ạt, lấp đầy lỗ hổng máu chảy chỉ trong vài ngày, và sau 30 ngày, 1/3 trái tim bị mất đã mọc lại nguyên vẹn cả buồng tâm thất mới tinh, đập rộn ràng bơm máu khắp cơ thể mà không có một milimet mô sẹo nào! | **30 NGÀY** · tim mọc lại 100% · R/350 · [0.65, 0.45] | Sau 30 ngày, buồng tâm thất mới tinh mọc lại hoàn chỉnh 100%, trái tim đập rộn ràng phát sáng hào quang đỏ hồng không một vết sẹo. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b08 | 00:52.6–01:02.1 (9.5s) | L48 | Chưa dừng lại ở đó! Trong công trình chấn động công bố trên tạp chí Science 2022 bằng công nghệ giải trình tự không gian đơn bào, các nhà khoa học đã thử cắt bỏ một phần thùy não trước của chú kỳ | **SCIENCE** · nghiên cứu não bộ · L/350 · [0.35, 0.45] | Bìa tạp chí Science 2022 hiển thị sơ đồ giải trình tự không gian đơn bào thùy não trước của chú kỳ nhông. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b09 | 01:02.1–01:13.8 (11.6s) | L49 | nhông. Và kết quả khiến cả thế giới sửng sốt: các tế bào gốc biểu mô thần kinh lại thức giấc, chia thành từng lớp tế bào mới và tái cấu trúc lại toàn bộ các nơ-ron não bộ bị mất theo đúng sơ đồ phôi thai ban đầu! |  | Mặt cắt bộ não: các tế bào gốc biểu mô thần kinh thức giấc, xếp từng lớp tế bào nơ-ron mới tái tạo lại thùy não trước bị cắt mất. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b10 | 01:13.8–01:20.6 (6.8s) | L50 | Trời đất ơi viện trưởng ơi, nó vừa mọc lại cả một phần bộ não mà nhìn cái mặt vẫn cười toe toét ngây thơ y như cũ kìa! |  | cô trợ lý phòng thí nghiệm hoạt hình mặc áo blouse xanh nhạt đeo thẻ nhân viên ôm hai má há hốc mồm kinh ngạc; BÊN PHẢI chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe  |
| b11 | 01:20.6–01:24.2 (3.6s) | L51 | Bị cắt mất một góc não bộ mà nụ cười vẫn không hề biến mất! |  | chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán tạo dáng ngộ nghĩnh, nụ cười bất biến; bên cạnh là hình đồ họa trái tim và bộ não tỏa hào quang chữa lành thần |
| b12 | 01:24.2–01:33.8 (9.6s) | L52 | Khả năng tự sửa chữa bộ não và quả tim đã đưa Chiến Thần Tái Sinh bước vào hàng ngũ những sinh vật có cơ chế hồi phục kỳ ảo nhất từng được ghi nhận trong lịch sử tiến hóa của động vật có xương sống! |  | Bảng điện tử cấp độ 3 bật đèn xanh PASS kèm biểu tượng trái tim và bộ não vàng rực rỡ. |

### scene05 · NHẬN GHÉP TẠNG XUYÊN CÁ THỂ VÀ GIẢI MÃ BỘ GEN 32 TỶ · 90.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.4 (7.4s) | L53 | Tăng công suất máy quét lên Cấp độ bốn: Thử thách ghép tạng xuyên cá thể! Trong y học ghép tạng của con người, kẻ thù số một luôn là hiện tượng thải ghép. |  | Màn hình chuyển sang CẤP ĐỘ 4: GHÉP TẠNG XUYÊN CÁ THỂ; ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước đứng giải thích bên sơ đồ y học ghép tạng. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b02 | 00:07.4–00:09.9 (2.4s) | L54 | Hệ miễn dịch của chúng ta cực kỳ hung dữ và cảnh |  | Mô hình hệ miễn dịch người báo động đỏ hung dữ với đội quân bạch cầu giơ vũ khí cảnh giác. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b03 | 00:09.9–00:19.7 (9.8s) | L55 | giác: chỉ cần phát hiện một quả thận hay lá gan có kháng nguyên lạ từ người khác đưa vào, đội quân bạch cầu sẽ lập tức tổng tấn công tiêu diệt mảnh ghép đến cùng, buộc bệnh nhân phải uống thuốc ức chế miễn dịch suốt đời. |  | Đội quân bạch cầu người tổng tấn công tiêu diệt mảnh ghép tạng lạ, bắt bệnh nhân uống thuốc ức chế miễn dịch. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b04 | 00:19.7–00:26.2 (6.5s) | L56 | Thế nhưng trong cơ thể của Chiến Thần Tái Sinh, hệ miễn dịch lại hành xử như một đại sứ hòa bình đầy bao dung! |  | Đại thực bào của chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán mang hình ảnh sứ giả hòa bình thân thiện, ân cần quét dọn tế bào chết và bắt tay các tế bào g |
| b05 | 00:26.2–00:36.2 (10.1s) | L57 | Các nhà khoa học tại viện nghiên cứu đã làm những thí nghiệm kỳ lạ đến mức khó tin: lấy một cánh tay của chú kỳ nhông màu trắng bạch tạng ghép sang cơ thể một chú kỳ nhông màu xanh đen hoang dã. |  | Thí nghiệm ghép chi: một chú kỳ nhông màu xanh đen hoang dã được ghép một cánh tay màu trắng bạch tạng, cánh tay cử động vẫy chào mượt mà. |
| b06 | 00:36.2–00:46.6 (10.4s) | L58 | Thay vì đào thải, các tế bào đại thực bào của cơ thể tiếp nhận ân cần dọn dẹp tế bào chết, kết nối mạch máu và nuôi dưỡng cánh tay ghép đó hoạt động trơn tru như chính cánh tay ruột thịt của mình! |  | Mạch máu đỏ nối thông từ thân sang cánh tay trắng ghép, nuôi dưỡng các khớp ngón tay cử động khỏe khoắn như ruột thịt. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b07 | 00:46.6–00:58.5 (11.9s) | L59 | Thậm chí trong những thí nghiệm giải phẫu kinh điển, người ta từng ghép thêm một chiếc đầu thứ 2 hoặc một cánh tay phụ lên lưng của chú kỳ nhông, và cơ thể nó vẫn bình thản dung nạp, kết nối dây thần kinh và nuôi sống cả hai phần cơ thể một cách kỳ dị! |  | Minh họa thí nghiệm giải phẫu kinh điển: chú kỳ nhông dung nạp thêm một cánh tay phụ nhỏ trên lưng, các dây thần kinh nối liền hoàn hảo. |
| b08 | 00:58.5–01:07.4 (8.9s) | L60 | Bí mật đằng sau sức mạnh bao la này nằm ở đâu? 2018, một bài báo chấn động trên tạp chí Nature danh tiếng đã giải mã thành công toàn bộ bản đồ gen của Axolotl. | **2018** · công bố Nature · L/350 · [0.35, 0.45] | Bìa bài báo tạp chí Nature danh tiếng năm 2018 mở ra mô hình chuỗi xoắn kép ADN khổng lồ rực rỡ màu sắc. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b09 | 01:07.4–01:19.3 (11.9s) | L61 | Các đồng nghiệp hãy chuẩn bị tinh thần đón nhận con số này: Bộ gen của chú kỳ nhông nhỏ bé này dài tới 32 tỷ cặp base — tức là lớn gấp hơn 10 lần toàn bộ bộ gen của loài người chúng ta với chỉ 3 tỷ cặp base! | **32 TỶ** · cặp base ADN · R/350 · [0.68, 0.48]<br>**GẤP 10 LẦN** · so với bộ gen người · L/480 · [0.28, 0.55] | Thước cuộn ADN so sánh: sợi ADN người 3 tỷ cặp base ngắn tũn bên cạnh cuộn ADN khổng lồ 32 tỷ cặp base dài gấp 10 lần của chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xo |
| b10 | 01:19.3–01:30.2 (10.9s) | L62 | Cả một đại dương thông tin di truyền khổng lồ chứa hàng ngàn đoạn mã cổ xưa chuyên kích hoạt tái sinh mô đang được cơ thể nó bảo tồn nguyên vẹn suốt hàng trăm triệu năm qua! Cấp độ bốn: Hoàn thành mỹ mãn! |  | Kho tàng dữ liệu di truyền cổ xưa hàng trăm triệu năm bừng sáng bên trong nhân tế bào của chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán, bảng cấp độ 4 bật đ |

### scene06 · HOÁ THÚ MẤT SIÊU NĂNG LỰC VÀ BÓNG ĐEN BÍ ẨN · 122.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:04.8 (4.8s) | L63 | Chúng ta bước vào Cấp độ tối thượng: Điều gì trên đời này có thể đánh bại được Chiến Thần Tái Sinh? |  | Đèn tím phòng lab rực rỡ, màn hình trung tâm chớp sáng dòng chữ CẤP ĐỘ TỐI THƯỢNG: TRÙM CUỐI SINH TỒN; ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước khoanh tay trầm ngâm suy nghĩ. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b02 | 00:04.8–00:13.7 (8.9s) | L64 | Chặt chân chân mọc lại. Đứt tủy tủy nối liền. Thủng tim tim tự vá. Ghép tạng tạng dung nạp. Chẳng lẽ sinh vật này thực sự bất tử không có lấy một điểm yếu nào sao? |  | Bốn ô đồ họa tóm tắt: chân mọc lại, tủy nối liền, tim tự vá, tạng dung nạp; ở giữa là dấu chấm hỏi khổng lồ phát sáng vàng. |
| b03 | 00:13.7–00:21.9 (8.2s) | L65 | Và đây là cú bẻ lái triết lý sâu sắc nhất mà tạo hóa cài cắm vào hồ sơ của mẫu vật: Thứ vũ khí duy nhất tước đoạt siêu năng lực của nó... chính là sự trưởng thành! |  | Chiếc đồng hồ thời gian quay vùn vụt và bóng đen của dòng chữ SỰ TRƯỞNG THÀNH xuất hiện như một bức màn bí ẩn. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b04 | 00:21.9–00:29.7 (7.8s) | L66 | Trong tự nhiên, tuyến giáp của Axolotl bị khiếm khuyết bẩm sinh nên không thể tự sản sinh đủ lượng hoóc-môn Thyroxine để kích hoạt quá trình biến thái. | **THYROXINE** · hoóc-môn tuyến giáp · L/350 · [0.45, 0.5] | Sơ đồ giải phẫu tuyến giáp của chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán thiếu hụt hoóc-môn Thyroxine, biểu tượng chiếc van khóa chặn giữ nguyên hình hà |
| b05 | 00:29.7–00:34.5 (4.8s) | L67 | Nó chọn sống cả đời dưới nước trong hình hài một đứa trẻ ngây thơ để bảo lưu năng lực tái sinh thần thánh. |  | chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán tung tăng bơi lội dưới làn nước mát với nụ cười trẻ thơ ngây ngô bất tử, xung quanh là cỏ nước và ốc nhỏ. |
| b06 | 00:34.5–00:42.1 (7.6s) | L68 | Nhưng khi các nhà khoa học trong phòng thí nghiệm can thiệp bằng cách tiêm trực tiếp hoóc-môn Thyroxine vào cơ thể, chiếc đồng hồ sinh học bị cưỡng ép quay nhanh! |  | Bàn tay nhà khoa học cầm ống tiêm chứa dung dịch hoóc-môn Thyroxine tiêm vào cơ thể kỳ nhông, chiếc đồng hồ sinh học bị kích hoạt quay tít. |
| b07 | 00:42.1–00:47.0 (5.0s) | L69 | Sáu chiếc sừng mang ngoài rực rỡ từ từ teo rụng. Phổi bên trong phồng to lên. Mi mắt bắt đầu khép mở. |  | Sáu chiếc sừng đỏ của chú kỳ nhông từ từ teo nhỏ và rụng dần, phổi bên trong phồng to, hai mắt xuất hiện mi mắt bắt đầu khép mở. |
| b08 | 00:47.0–00:51.9 (4.9s) | L70 | Toàn bộ cơ thể nó trèo lên cạn biến thành một con kỳ nhông hổ trưởng thành màu nâu xám! |  | Chú kỳ nhông bò lên cạn biến thành một con kỳ nhông hổ trưởng thành màu nâu xám sần sùi, không còn sừng đỏ, dáng đi nặng nề. |
| b09 | 00:51.9–00:54.9 (3.0s) | L71 | Và cái giá phải trả cho sự lớn khôn là vô cùng tàn nhẫn: |  | Đồng hồ cát vỡ đôi, chiếc mặt nạ bi hài kịch của sự trưởng thành xuất hiện trong phòng lab. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b10 | 00:54.9–01:04.0 (9.1s) | L72 | Khi đã bước lên cạn thành thú trưởng thành, siêu năng lực mọc lại tứ chi bị suy giảm nghiêm trọng, các vết thương bắt đầu hình thành mô sẹo xơ cứng, và tuổi thọ của nó tụt dốc thê thảm chỉ còn lại 1/2! | **GIẢM 1/2** · tuổi thọ khi lên cạn · R/350 · [0.65, 0.45] | Cận cảnh bàn chân của kỳ nhông trên cạn bị thương xuất hiện vết sẹo xơ cứng xám ngoét gạch chéo đỏ, không thể tự mọc lại nguyên vẹn. |
| b11 | 01:04.0–01:11.0 (7.0s) | L73 | Hóa ra để giữ được nụ cười bất tử vô ưu vô lo, tạo hóa bắt nó phải đánh đổi bằng cách mãi mãi không bao giờ được lớn lên! |  | So sánh đối chiếu: BÊN TRÁI chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán hồng phấn dưới nước cười ngây thơ bất tử; BÊN PHẢI kỳ nhông cạn nâu xám già nua đầ |
| b12 | 01:11.0–01:17.2 (6.2s) | L74 | Tổng kết ghi chép phòng thí nghiệm số 22: Chiến Thần Tái Sinh đạt điểm 10 tuyệt đối cho bài kiểm tra sinh | **ĐIỂM 10** · sinh tồn tuyệt đối · R/350 · [0.58, 0.45] | ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước giơ tấm bảng điểm 10 đỏ chót trao cho chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng |
| b13 | 01:17.2–01:23.6 (6.4s) | L75 | tồn! Kê đơn xuất viện: Cho mẫu vật bơi lội tung tăng trong làn nước mát và tuyệt đối cấm tiêm hoóc-môn lý |  | chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán được thả lại vào bể kính nước mát trong veo, bơi tung tăng vẫy tay chào tạm biệt phòng thí nghiệm. |
| b14 | 01:23.6–01:35.4 (11.8s) | L76 | ép lớn! Còn các trợ phòng thí nghiệm thì sao? Nếu được chọn giữa việc lớn lên thành người lớn nhiều âu lo, hay mãi mãi giữ nụ cười trẻ thơ và khả năng tự chữa lành mọi vết thương trong cuộc sống, bạn chọn cái nào? Hãy bình luận bên dưới nhé! |  | Hai ngã rẽ cuộc đời: BÊN TRÁI biểu tượng người lớn xách cặp đi làm nhiều âu lo; BÊN PHẢI nụ cười trẻ thơ của chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán c |
| b15 | 01:35.4–01:43.8 (8.3s) | L77 | Hồ sơ cấp độ tối thượng xin khép lại tại đây. Nhưng tập sau, phòng thí nghiệm của chúng ta sẽ chuyển thẳng xuống đáy biển sâu để đón tiếp một sinh vật quái đản bậc nhất hành tinh! |  | ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước đóng tập hồ sơ số 22 lại, trên bàn mở ra bản đồ thám hiểm đáy đại dương tối thẫm với ngọn hải đăng quét sáng. |
| b16 | 01:43.8–01:50.6 (6.9s) | L78 | Một cục thịt dài ngoằng không xương, không mắt, nhưng khi bị kẻ săn mồi dồn vào đường cùng, cơ thể nó có thể tự hóa lỏng thành một đống thạch nhớt nhầy |  | Một sinh vật bí ẩn được vẽ hoàn toàn bằng BÓNG ĐEN ĐẶC TUYỀN (solid black silhouette) dài ngoằng như khúc xúc xích nằm lững lờ trên đáy cát biển sâu tối tăm, có dấu hỏi chấm vàng phát sáng phía trên; KHÔNG vẽ rõ mắt mũi hay màu da thật. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b17 | 01:50.6–01:57.0 (6.3s) | L79 | nhụa, và trong tích tắc... bắn toàn bộ ruột gan phèo phổi của mình qua đường hậu môn để trói chặt kẻ thù rồi ung dung tẩu thoát! |  | Cũng chiếc BÓNG ĐEN ĐẶC TUYỀN (solid black silhouette) dài ngoằng đó dưới đáy biển tự hóa lỏng cơ thể thành đống thạch và bắn chùm tơ ruột màu trắng qua phía sau trói chặt một con cua biển săn mồi hung dữ. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |
| b18 | 01:57.0–02:02.0 (5.0s) | L80 | Đố các bạn biết bóng đen bí ẩn kỳ sau là loài vật nào? Hãy đoán ngay ở phần bình luận nhé! |  | Chiếc BÓNG ĐEN ĐẶC TUYỀN bí ẩn dưới đáy biển nằm giữa ba dấu hỏi chấm vàng cam lấp lánh mời gọi khán giả bình luận đoán tên loài vật tập sau. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này. |

## 5. Phân cảnh Shorts — từng beat

Banner: **MẤT NÃO VÀ THỦNG TIM / VẪN TỰ MỌC LẠI?!** · giọng 53.0s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Chuyện gì sẽ xảy ra nếu một con cá đói cắn đứt 1/3 trái |  |
| s02 | 00:03.4 | S12 | tim hoặc cắt mất một mảng não bộ của con vật này? Đối với chúng ta đó là dấu chấm hết, |  |
| s03 | 00:08.0 | S02 | nhưng với Kỳ Nhông Axolotl, nó chỉ mất đúng 30 ngày để tự mọc lại nguyên vẹn 100% mà không để lại một vết sẹo nhỏ! | **30 NGÀY** · mọc lại 100% · R/560 · [0.55, 0.45] |
| s04 | 00:14.4 | S03 | Đây là loài Khủng Long Sáu Sừng sống ở Mexico, dài 30cm với nụ cười toe toét ngây thơ. | **30 CM** · Khủng Long Sáu Sừng · R/750 · [0.6, 0.5] |
| s05 | 00:20.0 | S04 | Nhờ hiện tượng ấu nhi vĩnh viễn không bao giờ trưởng thành, tế bào của nó có thể tự quay ngược thời gian thành tế bào |  |
| s06 | 00:24.9 | S05 | gốc để tái tạo từ chân tay, đuôi, mắt cho đến tủy sống bị đứt đoạn! |  |
| s07 | 00:29.1 | S06 | Thậm chí khi các nhà khoa học cắt bỏ 1/3 tâm thất | **1/3 TIM** · tự vá tâm thất · L/560 · [0.48, 0.55] |
| s08 | 00:31.7 | S07 | tim hay ghép một cánh tay từ cá thể khác sang, cơ thể nó vẫn tự vá lành và dung nạp bình thường! |  |
| s09 | 00:37.5 | S08 | Bộ gen của nó dài tới 32 tỷ cặp base, lớn gấp 10 lần bộ gen con người! | **32 TỶ** · gấp 10 lần người · R/650 · [0.55, 0.5] |
| s10 | 00:41.7 | S09 | Bí mật duy nhất đánh bại được nó là sự lớn khôn: nếu bị ép tiêm hoóc-môn biến thái lên cạn, |  |
| s11 | 00:46.0 | S10 | nó sẽ rụng mất 6 chiếc sừng và đánh mất luôn khả năng bất tử! | **6 SỪNG** · teo rụng khi lớn · L/780 · [0.45, 0.5] |
| s12 | 00:49.0 | S11 | Một chiến thần tái sinh chọn mãi mãi làm một đứa trẻ để giữ trọn nụ cười kỳ diệu! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhật ký phòng thí nghiệm, ca trực nửa đêm. Đèn chiếu sáng chuyển sang sắc tím huỳnh quang, hệ thống cảm biến bắt đầu ghi nhận sóng sinh học từ bể kính số 22.". Bố cục: BÊN TRÁI ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước và cô trợ lý phòng thí nghiệm hoạt hình mặc áo blouse xanh nhạt đeo thẻ nhân viên đứng trước hệ thống máy tính phát sáng tím huỳnh quang; Ở GIỮA là bể kính số 22 phát sáng lung linh giữa ca trực nửa đêm. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giữa làn nước trong veo, một sinh vật kỳ dị đang lơ lửng bồng bềnh...". Bố cục: Bên trong làn nước trong veo của bể kính số 22, một sinh vật kỳ dị đang lơ lửng bồng bềnh tỏa ánh sáng tím mờ ảo. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn thân màu hồng phấn mọng nước như kẹo bông gòn.". Bố cục: Giữa làn nước trong veo, chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán lơ lửng bồng bềnh, toàn thân màu hồng phấn mọng nước mềm mại như kẹo bông gòn đáng yêu.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trên đầu xòe ra 6 chiếc sừng lông xù màu đỏ thẫm rung rinh trong nước.". Bố cục: Cận cảnh trên đầu chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán: sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm rung rinh xòe rộng trong nước như những chiếc quạt lông vũ nhỏ.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và đặc biệt nhất là khuôn mặt: hai chấm mắt đen tròn xoe cùng khóe miệng luôn nở một nụ cười toe toét ngây thơ đến mức kỳ quặc!". Bố cục: Khuôn mặt chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán cận cảnh chính diện: hai chấm mắt đen tròn xoe cùng khóe miệng luôn nở nụ cười toe toét ngây thơ ngộ nghĩnh vô cực.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Viện trưởng ơi, mẫu vật này nhìn cưng xỉu như thú bông, đưa vào phòng thí nghiệm thử thách chi cho tội nghiệp vậy ạ?". Bố cục: BÊN TRÁI cô trợ lý phòng thí nghiệm hoạt hình mặc áo blouse xanh nhạt đeo thẻ nhân viên ôm tập hồ sơ bệnh án nghiêng đầu cưng nựng nhìn vào bể kính; BÊN PHẢI chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán trong bể bơi tới áp mặt vào kính cười toe toét.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trợ lý chớ vội để vẻ mặt ngây thơ của mẫu vật đánh lừa!". Bố cục: BÊN TRÁI ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước nghiêm nghị lắc ngón tay cảnh báo; BÊN PHẢI trên màn hình máy quét phân tích sinh học hiện sơ đồ tế bào phát sáng rực rỡ. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây là Kỳ Nhông Axolotl, sinh vật đặc hữu của vùng hồ Xochimilco ở Mexico, còn được dân gian gọi bằng cái tên cực kỳ kiêu hãnh: Khủng Long Sáu Sừng!". Bố cục: Bản đồ hồ Xochimilco ở Mexico màu xanh ngọc ở BÊN TRÁI; BÊN PHẢI là chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán bơi kiêu hãnh đội chiếc vương miện Khủng Long Sáu Sừng nhỏ xíu.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kích thước một cá thể trưởng thành dài khoảng 20-30cm.". Bố cục: Ở GIỮA chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán đứng thẳng cạnh chiếc thước đo chiều cao phòng thí nghiệm màu vàng có kẻ vạch đo kích thước.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng điều khiến cả giới sinh học thế giới phải ngả mũ bái phục không nằm ở vẻ ngoài đáng yêu, mà là danh hiệu tối thượng chúng tôi đặt cho nó: Chiến Thần Tái Sinh!". Bố cục: Các nhà khoa học thế giới đứng quỳ gối ngả mũ kính phục trước bục vinh danh của chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán với dải ruy băng danh hiệu Chiến Thần Tái Sinh.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tạo hóa đã ban cho sinh vật này một hiện tượng kỳ lạ bậc nhất hành tinh gọi là ấu nhi vĩnh viễn.". Bố cục: chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán ngậm một chiếc núm vú giả em bé màu xanh hài hước, đứng cạnh chiếc đồng hồ thời gian bị khóa chặt ở số 0.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nghĩa là dù đã sống tới 15 năm và sinh con đẻ cái bình thường, cơ thể nó vẫn từ chối lớn lên, mãi mãi giữ nguyên hình hài của một đứa trẻ sơ sinh dưới nước!". Bố cục: Cảnh gia đình hạnh phúc: chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán vừa bơi vừa trông đàn kỳ nhông con tung tăng, bảng lịch 15 năm lật trang bên cạnh.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sáu chiếc sừng xù xì kia thực chất là mang ngoài chứa đầy mạch máu để thở.". Bố cục: Kính hiển vi phóng to cấu trúc một chiếc sừng mang ngoài: mạng lưới mao mạch máu màu đỏ tươi dày đặc chạy sát bề mặt để hút oxy trong nước. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và chính vì giữ mãi thể trạng non nớt của phôi thai, tế bào của nó sở hữu năng lực hồi sinh thần thánh thách thức mọi định luật y học!". Bố cục: chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán bơi giữa làn nước, xung quanh cơ thể tỏa hào quang tế bào phôi thai màu xanh ngọc lấp lánh như phép màu tái sinh.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đêm nay, tôi tuyên bố kích hoạt hệ thống thử thách 5 cấp độ cực hạn để kiểm tra giới hạn sinh tồn của Chiến Thần Tái Sinh!". Bố cục: ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước gạt cần công tắc khởi động hệ thống thí nghiệm lớn; phía trên bảng đèn LED bật sáng dòng chữ THỬ THÁCH 5 CẤP ĐỘ CỰC HẠN.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kích hoạt Cấp độ một: Thử thách tái tạo tứ chi! Hãy tưởng tượng một kịch bản tồi tệ xảy ra trong tự nhiên: một con cá đói khát lao tới đớp đứt lìa cánh tay trước của chú kỳ nhông.". Bố cục: Bảng điện tử hiện cấp độ 1: THỬ THÁCH TÁI TẠO TỨ CHI; BÊN PHẢI một con cá săn mồi hung dữ há to miệng lao tới cắn vào cánh tay chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở con người hay bất kỳ loài thú có vú nào, mất một cánh tay là vĩnh viễn mất đi. Cơ thể chúng ta sẽ nhanh chóng hình thành một lớp mô sẹo xơ cứng gồ ghề để bịt kín vết thương, chấm dứt hoàn toàn khả năng mọc lại chi mới.". Bố cục: So sánh chia đôi: BÊN TRÁI cánh tay người bị thương để lại vết mô sẹo xơ cứng gồ ghề kèm dấu gạch chéo đỏ; BÊN PHẢI là dấu chấm hỏi khoa học. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng tại bàn thí nghiệm của Chiến Thần Tái Sinh, đồng hồ đếm ngược bắt đầu vận hành một phép màu sinh học!". Bố cục: chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán nằm thảnh thơi trên bàn thí nghiệm nước, bên cạnh chiếc đồng hồ cát 24 giờ đếm ngược phát sáng hào quang kỳ diệu.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ trong vòng chưa đầy 24 giờ đầu tiên, các tế bào da xung quanh đã bò thần tốc qua miệng vết thương để tạo thành một lớp màng bảo vệ gọi là biểu mô vết thương.". Bố cục: Mặt cắt phóng đại vết cắt cánh tay: trong 24 giờ, các tế bào da bò thần tốc phủ kín bề mặt vết thương tạo thành lớp màng biểu mô bảo vệ hoàn hảo. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không hề có máu chảy đầm đìa, không hề có nhiễm trùng nguy hiểm!". Bố cục: Vết thương sạch sẽ không một giọt máu, các vi khuẩn gây nhiễm trùng bên ngoài bị lớp màng biểu mô chặn đứng hoàn toàn. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và ngay dưới lớp biểu mô ấy, điều kỳ diệu nhất bắt đầu xuất hiện: một khối tế bào mầm đặc biệt mang tên Blastema được kích hoạt!". Bố cục: Ngay dưới lớp da vết thương, một khối tế bào mầm Blastema màu hồng ngọc nhú lên phát sáng rực rỡ như mầm cây sinh học. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây là lúc khoa học phải kinh ngạc: các tế bào cơ bắp, tế bào xương, tế bào mạch máu đã trưởng thành tại vết cắt bỗng nhiên...". Bố cục: Kính hiển vi phóng to vết thương: các tế bào cơ bắp và xương trưởng thành bắt đầu có biểu hiện rung động lạ thường chuẩn bị phân tách. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tự bẻ ngược bánh xe thời gian, rũ bỏ thân phận cũ để quay trở lại trạng thái tế bào gốc sơ khai như lúc còn trong trứng! Khối tế bào mầm Blastema này". Bố cục: Sơ đồ chuyển hóa tế bào: tế bào cơ, xương, mạch máu xoay ngược bánh xe thời gian, rũ bỏ thân phận để trở lại thành tế bào gốc phôi thai tròn xoe. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "phân chia điên cuồng với độ chính xác tuyệt đối như một máy in ba đê sinh học tự nhiên!". Bố cục: Mô hình máy in 3D sinh học hoạt hình đang quét tia laser xanh in từng lớp xương, cơ bắp và mạch máu cho cánh tay mới của chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuần thứ 1, một chồi thịt nhỏ nhú ra. Tuần thứ 2, chồi thịt kéo dài và bắt đầu phân nhánh khớp khuỷu tay.". Bố cục: Timeline tiến trình 4 tuần: tuần 1 nhú chồi thịt nhỏ; tuần 2 chồi kéo dài phân nhánh khuỷu tay; ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước cầm kính lúp ghi chép tiến độ.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đến tuần thứ 4, 5 ngón tay nhỏ xíu màu hồng phấn bắt đầu tách rời rõ rệt!". Bố cục: Cận cảnh bàn tay mới nhú của chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán: năm ngón tay nhỏ xíu màu hồng phấn bắt đầu tách rời rõ rệt, cử động ngọ nguậy linh hoạt.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sau đúng 30-40 ngày, một cánh tay hoàn chỉnh mới toanh đã mọc lại nguyên vẹn 100%: từ tủy xương, cơ bắp, mạch máu cho đến các đầu dây thần kinh điều khiển cử động tinh vi!". Bố cục: chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán giơ cánh tay mới mọc trắng hồng khỏe khoắn vỗ vỗ vào cánh tay kia, kiểm tra khớp xương và cơ bắp cử động trơn tru 100%.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học từng làm thí nghiệm cắt đi cắt lại hàng trăm lần trên cùng một vị trí của Chiến Thần Tái Sinh, và kết quả mỗi lần đều mọc lại hoàn hảo như đúc, không để lại lấy một vết sẹo nhỏ,". Bố cục: Chiếc máy đếm số lần thí nghiệm nhảy số lên hàng trăm lần, mỗi lần cánh tay đều mọc lại hoàn hảo không sẹo. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "và đặc biệt nhất là không bao giờ bị đột biến thành tế bào ung thư! Cấp độ một: Vượt qua dễ như ăn kẹo!". Bố cục: Biểu tượng tế bào ung thư bị vòng tròn gạch chéo đỏ bảo vệ; BÊN PHẢI chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán ngậm kẹo mút cười tít mắt, bảng cấp độ 1 bật sáng đèn xanh PASS.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trợ lý, nâng độ khó lên Cấp độ hai: Thử thách tổn thương hệ thần kinh trung ương! Đối với loài người, đứt tủy sống là bản án chung thân khủng khiếp nhất của y học hiện đại.". Bố cục: Bảng điện tử phòng lab chuyển sang chữ CẤP ĐỘ 2: TỔN THƯƠNG HỆ THẦN KINH; ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước giơ ngón tay chỉ lên màn hình. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tủy sống là đại lộ thông tin kết nối bộ não với toàn bộ cơ thể.". Bố cục: Mô hình tủy sống phát sáng chạy dọc sống lưng như một đại lộ cao tốc truyền xung điện kết nối não và cơ thể. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi đại lộ đó bị cắt đứt, các tế bào hình sao sẽ lập tức dựng lên một bức tường mô sẹo dày đặc ngăn cản tín hiệu, khiến nạn nhân bị liệt vĩnh viễn không thuốc nào chữa nổi.". Bố cục: Sơ đồ tủy sống người bị đứt: các tế bào hình sao dựng lên bức tường mô sẹo đen dày đặc chặn tín hiệu, biểu tượng xe lăn bị gạch chéo. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo viện trưởng, máy quét huỳnh quang phát hiện vết đứt tủy sống của mẫu vật đang tự phát tín hiệu hồi phục!". Bố cục: cô trợ lý phòng thí nghiệm hoạt hình mặc áo blouse xanh nhạt đeo thẻ nhân viên reo lên chỉ tay vào màn hình máy quét huỳnh quang đang nhấp nháy luồng tín hiệu hồi phục màu xanh ngọc từ lưng mẫu vật.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhìn vào màn hình hiển vi điện tử đi các trợ lý! Trong tủy sống của Chiến Thần Tái Sinh, đội quân tế bào biểu mô thần kinh mang tên Ependymoglial lập tức nhận lệnh khẩn cấp!". Bố cục: Màn hình kính hiển vi điện tử: đội quân tế bào biểu mô thần kinh Ependymoglial màu tím huỳnh quang phân chia ồ ạt với tốc độ vũ bão. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thay vì tạo sẹo ngăn chặn như ở con người, những tế bào này phân chia với tốc độ vũ bão và vươn dài ra hai đầu để bắc một chiếc cầu sinh học xuyên qua khoảng trống đứt gãy!". Bố cục: Sơ đồ tủy sống đứt gãy: các tế bào thần kinh vươn dài ra hai đầu tạo thành một chiếc cầu treo sinh học nối liền khoảng trống. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiếc cầu biểu mô thần kinh ấy tiết ra các phân tử dẫn đường hóa học cực kỳ tinh vi, ngăn chặn hoàn toàn phản ứng viêm sẹo xơ cứng.". Bố cục: Chiếc cầu biểu mô tiết ra các phân tử phát sáng dẫn đường hóa học, ngăn chặn hoàn toàn mô sẹo xơ cứng hình thành. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hàng ngàn sợi trục thần kinh bị đứt liền nương theo chiếc cầu đó mà mọc xuyên qua, tìm đúng đầu nối cũ bên kia chiến tuyến để kết nối lại từng xung điện li ti!". Bố cục: Các sợi trục thần kinh men theo chiếc cầu mọc xuyên qua, các tia lửa xung điện li ti xẹt sáng kết nối hai đầu dây thần kinh. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ sau 3-4 tuần ngắn ngủi, toàn bộ bó dây thần kinh tủy sống đã hàn gắn liền mạch 100%! Chiến Thần Tái Sinh". Bố cục: Tờ lịch 3-4 tuần bóc trang rụng xuống, bó tủy sống đã hàn gắn trơn tru liền mạch 100% không một vết sẹo. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "lại phe phẩy chiếc đuôi bơi lượn thoăn thoắt trong bể nước với dáng vẻ ung dung tự tại, hoàn toàn không hề có một chút triệu chứng tê liệt hay suy giảm phản xạ vận động nào!". Bố cục: chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán uốn lượn chiếc đuôi hồng bơi lội thoăn thoắt hình số 8 trong bể nước, phản xạ bơi lội nhanh nhẹn hoàn hảo.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các viện nghiên cứu thần kinh hàng đầu thế giới đang dồn hàng chục triệu đô la vào ca bệnh này với hy vọng một ngày nào đó tìm ra chìa khóa chữa lành cho các bệnh nhân bại liệt! Cấp độ hai: Hoàn thành xuất sắc!". Bố cục: Tòa nhà viện nghiên cứu thần kinh quốc tế với biểu tượng ADN phát sáng và hy vọng mở ra chìa khóa chữa lành cho bệnh nhân bại liệt; bảng Cấp độ 2 bật đèn xanh PASS. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cảnh báo toàn phòng thí nghiệm: Chúng ta bước vào Cấp độ ba — Thử thách nội tạng sinh tử! Lần này, mục tiêu không còn là tay chân hay da thịt bên ngoài nữa.". Bố cục: Đèn còi báo động màu đỏ xoay tít, màn hình phòng lab hiện dòng chữ cảnh báo CẤP ĐỘ 3: THỬ THÁCH NỘI TẠNG SINH TỬ. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chúng ta đưa lưỡi dao vi phẫu chạm thẳng vào hai cơ quan tối thượng quyết định sự sống còn của sinh vật: Trái tim và Bộ não!". Bố cục: Dao vi phẫu chạm vào mô hình đồ họa của Trái Tim và Bộ Não phát sáng lung linh giữa phòng thí nghiệm. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học tim mạch đã thực hiện một cuộc phẫu thuật không tưởng: dùng kéo vi phẫu cắt phăng tới 1/3 tâm thất dưới đáy trái tim của chú kỳ nhông!". Bố cục: Kéo vi phẫu chuyên dụng cắt rời 1/3 góc tâm thất dưới đáy trái tim ba ngăn nhỏ xíu của chú kỳ nhông trên khay phẫu thuật trong suốt. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở con người, một vết thủng nhỏ hay một cơn nhồi máu cơ tim cũng đủ để giết chết hàng triệu tế bào cơ tim không thể thay thế, để lại vết sẹo xơ vĩnh viễn dẫn tới suy tim tử vong.". Bố cục: So sánh: mô hình trái tim người bị vết sẹo xơ đen xám sau cơn nhồi máu cơ tim, máy đo điện tim kêu tút dài báo động. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng khi nhìn vào lồng ngực trong suốt của Axolotl, các nhà phẫu thuật phải dụi mắt ba lần!". Bố cục: Các bác sĩ phẫu thuật dụi mắt kinh ngạc nhìn vào lồng ngực trong suốt của chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán: trái tim bị khuyết một góc vẫn tự đập bơm máu nhịp nhàng.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngay tại vùng biên vết cắt, các tế bào cơ tim còn lại tự kích hoạt thụ thể bề mặt đặc biệt, tự tháo dỡ các sợi tơ co bóp để quay về trạng thái tế bào phôi thai!". Bố cục: Phóng to vùng biên vết cắt tim: các tế bào cơ tim tháo dỡ sợi tơ co bóp, biến ngược thành tế bào phôi thai phân chia ồ ạt lấp kín lỗ hổng. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chúng phân chia ồ ạt, lấp đầy lỗ hổng máu chảy chỉ trong vài ngày, và sau 30 ngày, 1/3 trái tim bị mất đã mọc lại nguyên vẹn cả buồng tâm thất mới tinh, đập rộn ràng bơm máu khắp cơ thể mà không có một milimet mô sẹo nào!". Bố cục: Sau 30 ngày, buồng tâm thất mới tinh mọc lại hoàn chỉnh 100%, trái tim đập rộn ràng phát sáng hào quang đỏ hồng không một vết sẹo. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa dừng lại ở đó! Trong công trình chấn động công bố trên tạp chí Science 2022 bằng công nghệ giải trình tự không gian đơn bào, các nhà khoa học đã thử cắt bỏ một phần thùy não trước của chú kỳ nhông.". Bố cục: Bìa tạp chí Science 2022 hiển thị sơ đồ giải trình tự không gian đơn bào thùy não trước của chú kỳ nhông. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và kết quả khiến cả thế giới sửng sốt: các tế bào gốc biểu mô thần kinh lại thức giấc, chia thành từng lớp tế bào mới và tái cấu trúc lại toàn bộ các nơ-ron não bộ bị mất theo đúng sơ đồ phôi thai ban đầu!". Bố cục: Mặt cắt bộ não: các tế bào gốc biểu mô thần kinh thức giấc, xếp từng lớp tế bào nơ-ron mới tái tạo lại thùy não trước bị cắt mất. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trời đất ơi viện trưởng ơi, nó vừa mọc lại cả một phần bộ não mà nhìn cái mặt vẫn cười toe toét ngây thơ y như cũ kìa!". Bố cục: cô trợ lý phòng thí nghiệm hoạt hình mặc áo blouse xanh nhạt đeo thẻ nhân viên ôm hai má há hốc mồm kinh ngạc; BÊN PHẢI chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán trong bể nước nghiêng đầu mỉm cười toe toét ngây thơ vô số tội.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bị cắt mất một góc não bộ mà nụ cười vẫn không hề biến mất!". Bố cục: chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán tạo dáng ngộ nghĩnh, nụ cười bất biến; bên cạnh là hình đồ họa trái tim và bộ não tỏa hào quang chữa lành thần thánh.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khả năng tự sửa chữa bộ não và quả tim đã đưa Chiến Thần Tái Sinh bước vào hàng ngũ những sinh vật có cơ chế hồi phục kỳ ảo nhất từng được ghi nhận trong lịch sử tiến hóa của động vật có xương sống!". Bố cục: Bảng điện tử cấp độ 3 bật đèn xanh PASS kèm biểu tượng trái tim và bộ não vàng rực rỡ.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tăng công suất máy quét lên Cấp độ bốn: Thử thách ghép tạng xuyên cá thể! Trong y học ghép tạng của con người, kẻ thù số một luôn là hiện tượng thải ghép.". Bố cục: Màn hình chuyển sang CẤP ĐỘ 4: GHÉP TẠNG XUYÊN CÁ THỂ; ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước đứng giải thích bên sơ đồ y học ghép tạng. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hệ miễn dịch của chúng ta cực kỳ hung dữ và cảnh giác:". Bố cục: Mô hình hệ miễn dịch người báo động đỏ hung dữ với đội quân bạch cầu giơ vũ khí cảnh giác. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chỉ cần phát hiện một quả thận hay lá gan có kháng nguyên lạ từ người khác đưa vào, đội quân bạch cầu sẽ lập tức tổng tấn công tiêu diệt mảnh ghép đến cùng, buộc bệnh nhân phải uống thuốc ức chế miễn dịch suốt đời.". Bố cục: Đội quân bạch cầu người tổng tấn công tiêu diệt mảnh ghép tạng lạ, bắt bệnh nhân uống thuốc ức chế miễn dịch. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thế nhưng trong cơ thể của Chiến Thần Tái Sinh, hệ miễn dịch lại hành xử như một đại sứ hòa bình đầy bao dung!". Bố cục: Đại thực bào của chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán mang hình ảnh sứ giả hòa bình thân thiện, ân cần quét dọn tế bào chết và bắt tay các tế bào ghép lạ. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học tại viện nghiên cứu đã làm những thí nghiệm kỳ lạ đến mức khó tin: lấy một cánh tay của chú kỳ nhông màu trắng bạch tạng ghép sang cơ thể một chú kỳ nhông màu xanh đen hoang dã.". Bố cục: Thí nghiệm ghép chi: một chú kỳ nhông màu xanh đen hoang dã được ghép một cánh tay màu trắng bạch tạng, cánh tay cử động vẫy chào mượt mà.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thay vì đào thải, các tế bào đại thực bào của cơ thể tiếp nhận ân cần dọn dẹp tế bào chết, kết nối mạch máu và nuôi dưỡng cánh tay ghép đó hoạt động trơn tru như chính cánh tay ruột thịt của mình!". Bố cục: Mạch máu đỏ nối thông từ thân sang cánh tay trắng ghép, nuôi dưỡng các khớp ngón tay cử động khỏe khoắn như ruột thịt. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thậm chí trong những thí nghiệm giải phẫu kinh điển, người ta từng ghép thêm một chiếc đầu thứ 2 hoặc một cánh tay phụ lên lưng của chú kỳ nhông, và cơ thể nó vẫn bình thản dung nạp, kết nối dây thần kinh và nuôi sống cả hai phần cơ thể một cách kỳ dị!". Bố cục: Minh họa thí nghiệm giải phẫu kinh điển: chú kỳ nhông dung nạp thêm một cánh tay phụ nhỏ trên lưng, các dây thần kinh nối liền hoàn hảo.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bí mật đằng sau sức mạnh bao la này nằm ở đâu? 2018, một bài báo chấn động trên tạp chí Nature danh tiếng đã giải mã thành công toàn bộ bản đồ gen của Axolotl.". Bố cục: Bìa bài báo tạp chí Nature danh tiếng năm 2018 mở ra mô hình chuỗi xoắn kép ADN khổng lồ rực rỡ màu sắc. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các đồng nghiệp hãy chuẩn bị tinh thần đón nhận con số này: Bộ gen của chú kỳ nhông nhỏ bé này dài tới 32 tỷ cặp base — tức là lớn gấp hơn 10 lần toàn bộ bộ gen của loài người chúng ta với chỉ 3 tỷ cặp base!". Bố cục: Thước cuộn ADN so sánh: sợi ADN người 3 tỷ cặp base ngắn tũn bên cạnh cuộn ADN khổng lồ 32 tỷ cặp base dài gấp 10 lần của chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán.
```
</details>

<details><summary>L62</summary>

```text
HÌNH L62 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cả một đại dương thông tin di truyền khổng lồ chứa hàng ngàn đoạn mã cổ xưa chuyên kích hoạt tái sinh mô đang được cơ thể nó bảo tồn nguyên vẹn suốt hàng trăm triệu năm qua! Cấp độ bốn: Hoàn thành mỹ mãn!". Bố cục: Kho tàng dữ liệu di truyền cổ xưa hàng trăm triệu năm bừng sáng bên trong nhân tế bào của chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán, bảng cấp độ 4 bật đèn xanh PASS.
```
</details>

<details><summary>L63</summary>

```text
HÌNH L63 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chúng ta bước vào Cấp độ tối thượng: Điều gì trên đời này có thể đánh bại được Chiến Thần Tái Sinh?". Bố cục: Đèn tím phòng lab rực rỡ, màn hình trung tâm chớp sáng dòng chữ CẤP ĐỘ TỐI THƯỢNG: TRÙM CUỐI SINH TỒN; ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước khoanh tay trầm ngâm suy nghĩ. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L64</summary>

```text
HÌNH L64 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chặt chân chân mọc lại. Đứt tủy tủy nối liền. Thủng tim tim tự vá. Ghép tạng tạng dung nạp. Chẳng lẽ sinh vật này thực sự bất tử không có lấy một điểm yếu nào sao?". Bố cục: Bốn ô đồ họa tóm tắt: chân mọc lại, tủy nối liền, tim tự vá, tạng dung nạp; ở giữa là dấu chấm hỏi khổng lồ phát sáng vàng.
```
</details>

<details><summary>L65</summary>

```text
HÌNH L65 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và đây là cú bẻ lái triết lý sâu sắc nhất mà tạo hóa cài cắm vào hồ sơ của mẫu vật: Thứ vũ khí duy nhất tước đoạt siêu năng lực của nó... chính là sự trưởng thành!". Bố cục: Chiếc đồng hồ thời gian quay vùn vụt và bóng đen của dòng chữ SỰ TRƯỞNG THÀNH xuất hiện như một bức màn bí ẩn. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L66</summary>

```text
HÌNH L66 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong tự nhiên, tuyến giáp của Axolotl bị khiếm khuyết bẩm sinh nên không thể tự sản sinh đủ lượng hoóc-môn Thyroxine để kích hoạt quá trình biến thái.". Bố cục: Sơ đồ giải phẫu tuyến giáp của chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán thiếu hụt hoóc-môn Thyroxine, biểu tượng chiếc van khóa chặn giữ nguyên hình hài phôi thai.
```
</details>

<details><summary>L67</summary>

```text
HÌNH L67 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó chọn sống cả đời dưới nước trong hình hài một đứa trẻ ngây thơ để bảo lưu năng lực tái sinh thần thánh.". Bố cục: chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán tung tăng bơi lội dưới làn nước mát với nụ cười trẻ thơ ngây ngô bất tử, xung quanh là cỏ nước và ốc nhỏ.
```
</details>

<details><summary>L68</summary>

```text
HÌNH L68 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng khi các nhà khoa học trong phòng thí nghiệm can thiệp bằng cách tiêm trực tiếp hoóc-môn Thyroxine vào cơ thể, chiếc đồng hồ sinh học bị cưỡng ép quay nhanh!". Bố cục: Bàn tay nhà khoa học cầm ống tiêm chứa dung dịch hoóc-môn Thyroxine tiêm vào cơ thể kỳ nhông, chiếc đồng hồ sinh học bị kích hoạt quay tít.
```
</details>

<details><summary>L69</summary>

```text
HÌNH L69 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sáu chiếc sừng mang ngoài rực rỡ từ từ teo rụng. Phổi bên trong phồng to lên. Mi mắt bắt đầu khép mở.". Bố cục: Sáu chiếc sừng đỏ của chú kỳ nhông từ từ teo nhỏ và rụng dần, phổi bên trong phồng to, hai mắt xuất hiện mi mắt bắt đầu khép mở.
```
</details>

<details><summary>L70</summary>

```text
HÌNH L70 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn bộ cơ thể nó trèo lên cạn biến thành một con kỳ nhông hổ trưởng thành màu nâu xám!". Bố cục: Chú kỳ nhông bò lên cạn biến thành một con kỳ nhông hổ trưởng thành màu nâu xám sần sùi, không còn sừng đỏ, dáng đi nặng nề.
```
</details>

<details><summary>L71</summary>

```text
HÌNH L71 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và cái giá phải trả cho sự lớn khôn là vô cùng tàn nhẫn:". Bố cục: Đồng hồ cát vỡ đôi, chiếc mặt nạ bi hài kịch của sự trưởng thành xuất hiện trong phòng lab. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L72</summary>

```text
HÌNH L72 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi đã bước lên cạn thành thú trưởng thành, siêu năng lực mọc lại tứ chi bị suy giảm nghiêm trọng, các vết thương bắt đầu hình thành mô sẹo xơ cứng, và tuổi thọ của nó tụt dốc thê thảm chỉ còn lại 1/2!". Bố cục: Cận cảnh bàn chân của kỳ nhông trên cạn bị thương xuất hiện vết sẹo xơ cứng xám ngoét gạch chéo đỏ, không thể tự mọc lại nguyên vẹn.
```
</details>

<details><summary>L73</summary>

```text
HÌNH L73 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hóa ra để giữ được nụ cười bất tử vô ưu vô lo, tạo hóa bắt nó phải đánh đổi bằng cách mãi mãi không bao giờ được lớn lên!". Bố cục: So sánh đối chiếu: BÊN TRÁI chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán hồng phấn dưới nước cười ngây thơ bất tử; BÊN PHẢI kỳ nhông cạn nâu xám già nua đầy âu lo.
```
</details>

<details><summary>L74</summary>

```text
HÌNH L74 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tổng kết ghi chép phòng thí nghiệm số 22: Chiến Thần Tái Sinh đạt điểm 10 tuyệt đối cho bài kiểm tra sinh tồn!". Bố cục: ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước giơ tấm bảng điểm 10 đỏ chót trao cho chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán; cả phòng thí nghiệm vỗ tay chúc mừng Chiến Thần Tái Sinh.
```
</details>

<details><summary>L75</summary>

```text
HÌNH L75 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kê đơn xuất viện: Cho mẫu vật bơi lội tung tăng trong làn nước mát và tuyệt đối cấm tiêm hoóc-môn ép lớn!". Bố cục: chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán được thả lại vào bể kính nước mát trong veo, bơi tung tăng vẫy tay chào tạm biệt phòng thí nghiệm.
```
</details>

<details><summary>L76</summary>

```text
HÌNH L76 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn các trợ lý phòng thí nghiệm thì sao? Nếu được chọn giữa việc lớn lên thành người lớn nhiều âu lo, hay mãi mãi giữ nụ cười trẻ thơ và khả năng tự chữa lành mọi vết thương trong cuộc sống, bạn chọn cái nào? Hãy bình luận bên dưới nhé!". Bố cục: Hai ngã rẽ cuộc đời: BÊN TRÁI biểu tượng người lớn xách cặp đi làm nhiều âu lo; BÊN PHẢI nụ cười trẻ thơ của chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán cùng khả năng tự chữa lành, khán giả giơ thẻ bình luận có hình trái tim. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L77</summary>

```text
HÌNH L77 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hồ sơ cấp độ tối thượng xin khép lại tại đây. Nhưng tập sau, phòng thí nghiệm của chúng ta sẽ chuyển thẳng xuống đáy biển sâu để đón tiếp một sinh vật quái đản bậc nhất hành tinh!". Bố cục: ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước đóng tập hồ sơ số 22 lại, trên bàn mở ra bản đồ thám hiểm đáy đại dương tối thẫm với ngọn hải đăng quét sáng.
```
</details>

<details><summary>L78</summary>

```text
HÌNH L78 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một cục thịt dài ngoằng không xương, không mắt, nhưng khi bị kẻ săn mồi dồn vào đường cùng, cơ thể nó có thể tự hóa lỏng thành một đống thạch nhớt nhầy nhụa,". Bố cục: Một sinh vật bí ẩn được vẽ hoàn toàn bằng BÓNG ĐEN ĐẶC TUYỀN (solid black silhouette) dài ngoằng như khúc xúc xích nằm lững lờ trên đáy cát biển sâu tối tăm, có dấu hỏi chấm vàng phát sáng phía trên; KHÔNG vẽ rõ mắt mũi hay màu da thật. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L79</summary>

```text
HÌNH L79 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "và trong tích tắc... bắn toàn bộ ruột gan phèo phổi của mình qua đường hậu môn để trói chặt kẻ thù rồi ung dung tẩu thoát!". Bố cục: Cũng chiếc BÓNG ĐEN ĐẶC TUYỀN (solid black silhouette) dài ngoằng đó dưới đáy biển tự hóa lỏng cơ thể thành đống thạch và bắn chùm tơ ruột màu trắng qua phía sau trói chặt một con cua biển săn mồi hung dữ. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L80</summary>

```text
HÌNH L80 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đố các bạn biết bóng đen bí ẩn kỳ sau là loài vật nào? Hãy đoán ngay ở phần bình luận nhé!". Bố cục: Chiếc BÓNG ĐEN ĐẶC TUYỀN bí ẩn dưới đáy biển nằm giữa ba dấu hỏi chấm vàng cam lấp lánh mời gọi khán giả bình luận đoán tên loài vật tập sau. KHÔNG có chú kỳ nhông đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Chuyện gì sẽ xảy ra nếu một con cá đói cắn đứt 1/3 trái tim". Bố cục: Khung dọc: con cá săn mồi hung dữ lao tới đớp vào chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán trong bể nước, bong bóng X-quang hiện hình 1/3 trái tim bị cắn đứt.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "nhưng với Kỳ Nhông Axolotl, nó chỉ mất đúng 30 ngày để tự mọc lại nguyên vẹn 100% mà không để lại một vết sẹo nhỏ!". Bố cục: Bác sĩ ôm đầu hốt hoảng gạch chéo đỏ, bên cạnh chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán mỉm cười toe toét giơ bàn tay phát sáng hào quang chữa lành.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đây là loài Khủng Long Sáu Sừng sống ở Mexico, dài 30cm với nụ cười toe toét ngây thơ.". Bố cục: chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán bơi bảnh bao giữa làn nước hồ Mexico, chiếc thước đo chiều cao màu vàng 30cm dựng thẳng đứng bên cạnh.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Nhờ hiện tượng ấu nhi vĩnh viễn không bao giờ trưởng thành, tế bào của nó có thể tự quay ngược thời gian thành tế bào gốc". Bố cục: Mô hình tế bào phôi thai phát sáng xanh ngọc, chiếc đồng hồ sinh học bị khóa chặt ở số 0, chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán giữ mãi hình hài ấu nhi.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "để tái tạo từ chân tay, đuôi, mắt cho đến tủy sống bị đứt đoạn!". Bố cục: Minh họa chân tay, chiếc đuôi, mắt và tủy sống của chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán phát sáng hào quang tự mọc lại nguyên vẹn không để lại một vết sẹo nhỏ.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Thậm chí khi các nhà khoa học cắt bỏ 1/3 tâm thất tim". Bố cục: Kéo vi phẫu cắt 1/3 tâm thất tim của chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán, buồng tim tự khép miệng phân chia tế bào bơm máu đập rộn ràng.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "hay ghép một cánh tay từ cá thể khác sang, cơ thể nó vẫn tự vá lành và dung nạp bình thường!". Bố cục: Cánh tay màu trắng bạch tạng ghép sang chú kỳ nhông màu đen, mạch máu nối liền nuôi dưỡng cử động mượt mà không hề đào thải.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bộ gen của nó dài tới 32 tỷ cặp base, lớn gấp 10 lần bộ gen con người!". Bố cục: Thước cuộn ADN khổng lồ: bộ gen Axolotl 32 tỷ cặp base dài gấp 10 lần bộ gen con người 3 tỷ cặp base.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bí mật duy nhất đánh bại được nó là sự lớn khôn: nếu bị ép tiêm hoóc-môn biến thái lên cạn,". Bố cục: Ống tiêm chứa hoóc-môn Thyroxine làm sáu chiếc sừng mang ngoài lông xù của chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán teo rụng dần, chiếc đồng hồ quay nhanh.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "nó sẽ rụng mất 6 chiếc sừng và đánh mất luôn khả năng bất tử!". Bố cục: Cận cảnh 6 chiếc sừng mang ngoài của chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán teo rụng, chú kỳ nhông hổ nâu xám leo lên cạn, bàn chân bị vết sẹo xơ cứng gạch chéo đỏ, không còn tự mọc lại được nữa.
```
</details>

<details><summary>S11</summary>

```text
HÌNH S11 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Một chiến thần tái sinh chọn mãi mãi làm một đứa trẻ để giữ trọn nụ cười kỳ diệu!". Bố cục: Chân dung chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán hồng phấn tỏa hào quang rực rỡ dưới nước, 6 sừng xòe rộng, nụ cười bất tử vô ưu vô lo ngây thơ ngộ nghĩnh.
```
</details>

<details><summary>S12</summary>

```text
HÌNH S12 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kỳ Nhông Axolotl hồng phấn, 6 sừng mang đỏ xù, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "hoặc cắt mất một mảng não bộ của con vật này? Đối với chúng ta đó là dấu chấm hết,". Bố cục: Khung dọc cận cảnh: mô hình bộ não nhỏ xíu bị cắt khuyết một góc, bên cạnh là biểu tượng dấu chấm hết gạch chéo đỏ; chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán vẫn nghiêng đầu chớp mắt ngây thơ.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/80 của video YouTube về Kỳ Nhông Axolotl). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán. Nhân vật phụ cố định: ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước; cô trợ lý phòng thí nghiệm hoạt hình mặc áo blouse xanh nhạt đeo thẻ nhân viên. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/12 của video YouTube Shorts về Kỳ Nhông Axolotl). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Kỳ Nhông Axolotl (Ambystoma mexicanum) hoạt hình màu hồng phấn mọng nước, thân bè tròn mềm mại, hai mắt đen tròn xoe long lanh ngây thơ, miệng luôn cười toe toét ngộ nghĩnh, trên đầu xòe ra sáu chiếc sừng mang ngoài lông xù màu đỏ thẫm xòe rộng, đeo một cặp kính bảo hộ phòng thí nghiệm tròn xoe trên trán. Nhân vật phụ: ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước. 
```
</details>

## 7. SEO

- **title:** Sinh Vật Bị Mất Não & Thủng Tim Vẫn Tự Mọc Lại Không Sẹo?!
- **hook_paragraph:** Kỳ Nhông Axolotl (Ambystoma mexicanum) sở hữu bộ gen 32 tỷ cặp base gấp 10 lần con người, có khả năng mọc lại chân tay, nối liền tủy sống, thậm chí tái tạo 1/3 quả tim và mô não bộ mà không để lại một vết sẹo! Khám phá 5 cấp độ thử thách tái sinh thần thánh của loài Khủng Long Sáu Sừng.
- **question:** Nếu được sở hữu 1 siêu năng lực của Kỳ Nhông Axolotl: tự chữa lành mọi vết thương không để lại sẹo, hay giữ mãi nụ cười trẻ thơ không bao giờ già đi, bạn chọn cái nào? Và đoán xem bóng đen tập sau là loài nào?
- **next_teaser:** Bóng đen bí ẩn dưới đáy biển sâu: tự hóa lỏng cơ thể thành thạch và bắn toàn bộ ruột gan qua đường hậu môn để tẩu thoát!
- **shorts_title:** Bị Mất Não & Thủng Tim Vẫn Tự Mọc Lại Không Sẹo?! 🦎 #độngvật #kỳnhôngaxolotl
- **shorts_desc:** Kỳ Nhông Axolotl dài 30cm sở hữu bộ gen 32 tỷ cặp base gấp 10 lần con người, tự mọc lại chân tay, tủy sống, 1/3 quả tim và mô não trong 30 ngày mà không để lại một vết sẹo! Giải mã bí mật Khủng Long Sáu Sừng.
- **bullets:** Cấp độ 1: Mọc lại cánh tay hoàn chỉnh với 5 ngón trong 30-40 ngày từ khối tế bào mầm Blastema · Cấp độ 2: Tế bào Ependymoglial bắc cầu nối liền tủy sống bị đứt, bơi lội bình thường sau 3-4 tuần · Cấp độ 3: Cắt 1/3 tâm thất tim và mô não trước vẫn tự tái tạo 100% chức năng không sẹo xơ · Cấp độ 4: Ghép tạng xuyên cá thể không đào thải và giải mã bộ gen 32 tỷ cặp base khổng lồ · Cấp độ 5: Cái giá của sự trưởng thành — ép biến thái lên cạn sẽ đánh mất siêu năng lực bất tử
- **tags:** kỳ nhông axolotl, ky nhong axolotl, axolotl, khủng long sáu sừng, khung long sau sung, ambystoma mexicanum, tái sinh không sẹo, mọc lại chi, động vật kỳ lạ, thế giới động vật, động vật hài hước, vẽ chuyện hoang dã, whiteboard animation, khoa học thú vị
- **hashtags:** #độngvật #kỳnhôngaxolotl #VẽChuyệnHoangDã

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-22-ky-nhong-axolotl
python src/episode/pipeline.py tts    projects/tap-22-ky-nhong-axolotl     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-22-ky-nhong-axolotl     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-22-ky-nhong-axolotl     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-22-ky-nhong-axolotl              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-22-ky-nhong-axolotl --force
python scripts/beat_sheet.py projects/tap-22-ky-nhong-axolotl               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-22-ky-nhong-axolotl/audio/shorts.wav projects/tap-22-ky-nhong-axolotl/renders/tap-22-ky-nhong-axolotl_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-22-ky-nhong-axolotl
python src/episode/pipeline.py seo    projects/tap-22-ky-nhong-axolotl
python src/episode/episode_doc.py     projects/tap-22-ky-nhong-axolotl
```

# TẬP 29 — SỨA BẤT TỬ · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-29-sua-bat-tu`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-29-sua-bat-tu`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F5` · **Persona giọng:** `nha_khoa_hoc` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Sứa Bất Tử |
| Tiêu đề YouTube | Sinh Vật Già Yếu Tự Biến Ngược Thành Sơ Sinh Để Bất Tử?! |
| Video dài | `renders/tap-29-sua-bat-tu_long.mp4` — 8:40.9 (520.9s) |
| Shorts | `renders/tap-29-sua-bat-tu_shorts.mp4` — 0:40.4 (40.4s) |
| Thumbnail | `renders/tap-29-sua-bat-tu_thumbnail.jpg` |
| Số hình | dài 50 beat / 50 ảnh riêng; Shorts 9 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/50 của video YouTube về Sứa Bất Tử). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa. Nhân vật phụ cố định: ông giáo sư già tóc bạc đeo kính lão cầm kính hiển vi; thảm polyp san hô non nớt màu cam nhạt đâm chồi dưới đáy biển; khối kén tròn cyst màu cam nhạt bám trên vỏ ốc rỗng. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — BÍ ẨN PHÁ VỠ QUY LUẬT SINH TỬ CỦA VŨ TRỤ
*Badge:* `PHÒNG LAB 5 CẤP ĐỘ` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene01_p0.wav` (306 ký tự) · mood `tram_bi_an`

```text
Chào mừng quý vị đồng nghiệp và các bạn đến với phòng thí nghiệm sinh học cực hạn! Trong tự nhiên, có một chân lý sắt đá mà mọi sinh vật từ vi khuẩn bé nhỏ cho đến loài người vĩ đại đều phải tuân theo: Sinh ra, lớn lên, già nua và trở về với cát bụi. Đó là định luật nhiệt động lực học không thể đảo ngược!
```
**Part 1** → `audio/vs/scene01_p1.wav` (163 ký tự) · 🎭 cameo `co_tro_ly`

```text
Thưa giáo sư, mẫu vật số hai mươi chín vừa được đưa từ vùng biển Địa Trung Hải về phòng lab, các chỉ số tế bào đang đảo ngược chiều thời gian một cách không tưởng!
```
**Part 2** → `audio/vs/scene01_p2.wav` (306 ký tự) · mood `don_dap`

```text
[surprise-oh] Bật toàn bộ kính hiển vi điện tử quét lên! Hôm nay chúng ta sẽ cùng nhau thực hiện năm cấp độ thử nghiệm sinh tử để giải mã một bí ẩn vĩ đại nhất hành tinh! [laughter] Xin trân trọng giới thiệu: đây là Turritopsis dohrnii, loài sinh vật biển độc nhất vô nhị được mệnh danh là Sinh Vật Bất Tử!
```
**Part 3** → `audio/vs/scene01_p3.wav` (389 ký tự) · mood `hao_hung`

```text
Loài sứa này được các nhà khoa học mô tả lần đầu vào năm một ngàn tám trăm tám mươi ba, nhưng phải mất hơn một thế kỷ sau, nhân loại mới tình cờ phát hiện ra quyền năng kinh ngạc của nó. Với kích thước trưởng thành chỉ vỏn vẹn bốn phẩy năm mi-li-mét — bé hơn cả một đầu ngón tay út — nhưng bên trong khối thạch trong suốt mỏng manh ấy là chiếc chìa khóa phá vỡ bản án tử thần của tự nhiên!
```
**Part 4** → `audio/vs/scene01_p4.wav` (267 ký tự) · mood `tram_bi_an`

```text
Nếu bạn nghĩ đây chỉ là một loài sứa bình thường trôi dạt lững lờ theo dòng nước biển, thì hãy chuẩn bị tinh thần! Vì ngay bây giờ, chúng ta sẽ lần lượt đưa Sinh Vật Bất Tử qua năm tầng thử thách cực hạn để tận mắt chứng kiến bánh xe thời gian bị bẻ cong như thế nào!
```
**Part 5** → `audio/vs/scene01_p5.wav` (314 ký tự) · mood `hao_hung`

```text
Hãy quan sát thật kỹ cấu trúc giải phẫu dưới ánh đèn huỳnh quang: một chiếc chuông sứa hình bán cầu trong suốt như thủy tinh pha lê, bên trong lộ rõ dạ dày màu đỏ tươi rực rỡ và xung quanh mép chuông có tới tám mươi đến chín mươi chiếc xúc tu mảnh mai như sợi tơ nhện. Một kiệt tác tạo hình của đại dương sâu thẳm!
```

### scene02 — THỬ THÁCH TỔN THƯƠNG CƠ HỌC VÀ STRESS MÔI TRƯỜNG CỰC HẠN
*Thẻ chương:* BỊ ĐÓI KHÁT VÀ TỔN THƯƠNG NẶNG TỰ KÍCH HOẠT QUY TRÌNH HỒI SINH

*Badge:* `CẤP ĐỘ 1: STRESS MÔI TRƯỜNG` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene02_p0.wav` (275 ký tự) · mood `tram_bi_an`

```text
Bước vào cấp độ thử nghiệm thứ nhất: Kích hoạt tình trạng nguy cấp cận kề cái chết! Đối với bất kỳ sinh vật nào khác, khi bị bỏ đói nhiều ngày, bị giảm độ mặn đột ngột hoặc chịu những vết cắt thương tật xé rách cơ thể, kết cục tất yếu sẽ là cái chết và sự phân hủy hoàn toàn.
```
**Part 1** → `audio/vs/scene02_p1.wav` (269 ký tự) · mood `don_dap`

```text
Năm một ngàn chín trăm chín mươi hai, tại một phòng thí nghiệm ở Ý, các nhà sinh học biển đã vô tình để quên một vài cá thể sứa già yếu trong đĩa thí nghiệm mà không cho ăn. Vài ngày sau quay lại, họ không hề nhìn thấy những xác chết thối rữa như dự đoán! [surprise-wa]
```
**Part 2** → `audio/vs/scene02_p2.wav` (272 ký tự) · mood `hao_hung`

```text
Thay vào đó, dưới đáy đĩa thủy tinh là những cụm polyp non nớt đang đâm chồi phát triển rực rỡ, hệt như những hạt mầm vừa mới nảy mầm sau cơn mưa đầu mùa! Những con sứa già cỗi không hề chết đi, chúng đã tự động chuyển đổi trạng thái cơ thể để trốn thoát lưỡi hái tử thần!
```
**Part 3** → `audio/vs/scene02_p3.wav` (260 ký tự) · mood `don_dap`

```text
Khi đối mặt với khủng hoảng sinh tồn, Sinh Vật Bất Tử không kích hoạt chế độ tự sát hay suy sụp tế bào. Ngược lại, nó phát đi một mệnh lệnh sinh học tối cao tới từng tế bào: Dừng ngay quá trình lão hóa, thu hồi toàn bộ xúc tu và chuẩn bị đảo ngược chu kỳ sống!
```
**Part 4** → `audio/vs/scene02_p4.wav` (268 ký tự) · mood `nghiem_trang_gia`

```text
Toàn bộ chiếc chuông sứa hình dù bắt đầu co thắt mạnh mẽ, các mô liên kết mềm nhũn ra và chìm dần xuống đáy biển sâu. Đây không phải là sự buông xuôi đầu hàng số phận, mà là phát súng lệnh mở màn cho một phép màu sinh học kỳ diệu chưa từng thấy trong lịch sử tự nhiên!
```
**Part 5** → `audio/vs/scene02_p5.wav` (390 ký tự) · mood `hao_hung`

```text
Nhóm nghiên cứu tại vịnh Genoa sau đó đã lặp lại thí nghiệm này hàng trăm lần với nhiều hình thức kích thích cực đoan khác nhau: hạ nhiệt độ nước xuống gần điểm đóng băng, tăng độ mặn lên gấp đôi, thậm chí dùng dao vi phẫu cắt đôi cơ thể sứa. Kết quả kinh ngạc là trong hầu hết mọi trường hợp, cơ thể nó đều tự gom lại thành một khối tế bào sống sót và bắt đầu quá trình tái sinh ngoạn mục!
```

### scene03 — CƠ CHẾ CHUYỂN BIỆT HÓA TẾ BÀO TRANSDIFFERENTIATION THẦN KỲ
*Thẻ chương:* TẾ BÀO CƠ BẮP TỰ BIẾN THÀNH TẾ BÀO GỐC NON NỚT

*Badge:* `CẤP ĐỘ 2: CHUYỂN BIỆT HÓA TẾ BÀO` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene03_p0.wav` (319 ký tự) · mood `tram_bi_an`

```text
Bước vào cấp độ thử nghiệm thứ hai: Soi rọi vào cỗ máy phân tử Transdifferentiation — Chuyển biệt hóa tế bào! Hãy hình dung thế này cho dễ hiểu: Trong cơ thể người, một tế bào cơ tim vĩnh viễn là tế bào cơ tim, tế bào da vĩnh viễn là tế bào da. Bạn không thể bắt một tế bào da biến thành tế bào mắt hay tế bào não được!
```
**Part 1** → `audio/vs/scene03_p1.wav` (159 ký tự) · 🎭 cameo `co_tro_ly`

```text
Báo cáo kính hiển vi: Các tế bào biểu bì và tế bào thần kinh của mẫu vật đang tự tẩy trắng danh tính ban đầu, chúng đang biến ngược thành tế bào gốc phôi thai!
```
**Part 2** → `audio/vs/scene03_p2.wav` (332 ký tự) · mood `don_dap`

```text
[surprise-oh] Chính xác là như vậy! Sinh Vật Bất Tử sở hữu một siêu năng lực mà y học hiện đại thèm khát suốt hàng thế kỷ: Nó có thể ra lệnh cho một tế bào cơ bắp đã trưởng thành tự xóa bỏ chức năng hiện tại, quay trở lại trạng thái tế bào gốc sơ khai chưa chuyên hóa, rồi từ đó biến đổi thành bất kỳ loại tế bào nào khác cần thiết!
```
**Part 3** → `audio/vs/scene03_p3.wav` (292 ký tự) · mood `hao_hung`

```text
Các nhà khoa học ví hiện tượng này giống như việc một con bướm trưởng thành xinh đẹp bỗng nhiên thu gọn đôi cánh lại, hóa ngược thành một chiếc kén tằm, rồi từ chiếc kén lại chui ra một chú sâu bướm non nớt! Một quy trình đảo ngược thời gian hoàn chỉnh diễn ra chỉ trong vòng ba đến bốn ngày!
```
**Part 4** → `audio/vs/scene03_p4.wav` (262 ký tự) · mood `am_ap`

```text
Hàng triệu tế bào khắp cơ thể sứa phối hợp tái tổ chức lại với nhau trong một vũ điệu sinh học hoàn hảo. Không có bất kỳ sự hỗn loạn hay sai sót nào xảy ra. Mọi dấu vết của sự già nua và bệnh tật tích tụ trong kiếp sống cũ đều bị xóa sạch hoàn toàn không tì vết!
```
**Part 5** → `audio/vs/scene03_p5.wav` (277 ký tự) · mood `nghiem_trang_gia`

```text
Ở động vật có xương sống bậc cao, khi mô bị tổn thương, cơ thể chỉ có thể hình thành mô sẹo xơ cứng để vá víu tạm bợ. Nhưng ở chú sứa kỳ diệu này, toàn bộ mạng lưới tế bào được lập trình lại từ đầu, loại bỏ hoàn toàn sẹo và khôi phục sự nguyên vẹn hoàn mỹ như lúc mới chào đời!
```

### scene04 — HÓA THÀNH BÚP POLYP NON NỚT VÀ NHÂN BẢN HÀNG TRĂM BẢN SAO
*Thẻ chương:* TỪ MỘT CON SỨA GIÀ MỌC THÀNH THẢM POLYP SINH RA TRĂM CON SỨA CON

*Badge:* `CẤP ĐỘ 3: TÁI SINH THÀNH POLYP` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene04_p0.wav` (290 ký tự) · mood `tram_bi_an`

```text
Bước sang cấp độ thử nghiệm thứ ba: Tái tạo cấu trúc sống từ con số không! Sau khi toàn bộ các tế bào đã được trẻ hóa thành công, khối cơ thể thạch của sứa chìm xuống đáy biển và bám chặt vào một tảng đá hay vỏ ốc rỗng. Tại đây, nó biến thành một khối búp tròn màu cam nhạt gọi là kén cyst.
```
**Part 1** → `audio/vs/scene04_p1.wav` (264 ký tự) · mood `hao_hung`

```text
Từ chiếc kén non nớt này, một phép màu sinh sản tiếp tục bùng nổ: Nó mọc rễ và vươn lên thành một quần thể polyp mới tinh! Polyp này bắt đầu đâm chồi, phân nhánh như những cành cây nhỏ dưới đáy biển và nuôi dưỡng hàng chục, thậm chí hàng trăm chồi sứa non lơ lửng!
```
**Part 2** → `audio/vs/scene04_p2.wav` (335 ký tự) · mood `don_dap`

```text
Khi đến thời điểm thích hợp, từng chiếc chuông sứa con trong suốt tách mình ra khỏi cành polyp, bung nở xúc tu bơi vút lên mặt nước để bắt đầu một kiếp sống mới! Hãy chú ý kỹ điều này: Từ một cá thể sứa già nua duy nhất ban đầu, nó không chỉ trẻ lại cho riêng mình, mà còn nhân bản ra hàng trăm bản sao giống hệt nhau về mặt di truyền!
```
**Part 3** → `audio/vs/scene04_p3.wav` (284 ký tự) · mood `hao_hung`

```text
Giáo sư Shin Kubota tại Đại học Kyoto Nhật Bản đã dành hơn mười lăm năm cuộc đời để chăm sóc loài sứa này trong phòng thí nghiệm. Ông đã chứng kiến một cá thể sứa lặp lại chu kỳ đảo ngược lão hóa này tới mười hai lần liên tiếp mà sức sống vẫn tràn trề không hề suy giảm! [surprise-wa]
```
**Part 4** → `audio/vs/scene04_p4.wav` (156 ký tự) · mood `tram_bi_an`

```text
Về mặt lý thuyết sinh học thuần túy, chu kỳ này có thể lặp đi lặp lại vô tận đến vĩnh hằng! Sinh Vật Bất Tử hoàn toàn miễn nhiễm trước cái chết vì tuổi già!
```
**Part 5** → `audio/vs/scene04_p5.wav` (283 ký tự) · mood `am_ap`

```text
Mỗi nhánh polyp dưới đáy biển giống như một nhà máy sản xuất sinh học tự động: khi nhiệt độ nước ấm lên vào mùa xuân, các chồi sứa bắt đầu nhấp nháy phát sáng rồi tách rời cuống bơi đi. Một chu trình tuần hoàn vĩnh cửu nối liền quá khứ và tương lai mà không bao giờ có điểm kết thúc!
```

### scene05 — GIẢI MÃ BÍ MẬT BẢO VỆ TELOMERE VÀ GEN SỬA CHỮA ADN
*Thẻ chương:* TELOMERE KHÔNG HỀ CO NGẮN VÀ HỆ THỐNG SỬA CHỮA ADN VƯỢT TRỘI

*Badge:* `CẤP ĐỘ 4 & 5: HỆ GEN THẦN THÁNH` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene05_p0.wav` (306 ký tự) · mood `hao_hung`

```text
Bước vào hai cấp độ tối mật cuối cùng: Cấp độ bốn và cấp độ năm — Giải mã bản thiết kế hệ gen! Năm hai ngàn không trăm hai mươi hai, một công trình nghiên cứu chấn động thế giới đăng trên tạp chí danh giá PNAS do tiến sĩ Maria Pascual-Torner dẫn đầu đã giải trình tự toàn bộ bộ gen của Turritopsis dohrnii.
```
**Part 1** → `audio/vs/scene05_p1.wav` (387 ký tự) · mood `don_dap`

```text
Kết quả phân tích đã hé lộ hai vũ khí phân tử vô giá: Thứ nhất là hệ thống bảo vệ telomere — đoạn mũ bảo vệ ở hai đầu sợi nhiễm sắc thể. Ở người, mỗi lần tế bào phân chia, telomere sẽ ngắn dần lại cho đến khi tế bào già nua và chết đi. Nhưng ở Sinh Vật Bất Tử, các enzym telomerase liên tục bảo dưỡng và kéo dài telomere, khiến đồng hồ tuổi tác của tế bào không bao giờ bị điểm giờ chết!
```
**Part 2** → `audio/vs/scene05_p2.wav` (316 ký tự) · mood `hao_hung`

```text
Vũ khí thứ hai là sự nhân đôi vượt trội của các gen liên quan đến sửa chữa ADN và chống oxy hóa. Cơ thể nó sở hữu số lượng bản sao gen sửa chữa lỗi sai sót phân tử nhiều gấp đôi so với các loài sứa thông thường! Bất kỳ tổn hại hay đột biến nào phát sinh đều được các cỗ máy enzym quét sạch và khắc phục ngay lập tức!
```
**Part 3** → `audio/vs/scene05_p3.wav` (355 ký tự) · mood `hao_hung`

```text
Các nhà khoa học đã so sánh bộ gen của nó với người họ hàng gần là loài sứa Turritopsis rubra — một loài sứa có ngoại hình gần như giống hệt nhưng lại không thể đảo ngược vòng đời. Sự so sánh này đã chỉ ra chính xác gần một ngàn gen đặc hữu chịu trách nhiệm cho khả năng bất tử, mở ra chân trời mới cho ngành y học tái tạo và chống lão hóa của loài người!
```
**Part 4** → `audio/vs/scene05_p4.wav` (286 ký tự) · mood `nghiem_trang_gia`

```text
Tuy nhiên, cần phải làm rõ một hiểu lầm phổ biến: Bất tử về mặt sinh học không có nghĩa là bất khả chiến bại trước mọi hiểm nguy! Trong môi trường đại dương tự nhiên đầy rẫy kẻ thù, Sinh Vật Bất Tử vẫn có thể bị rùa biển ăn thịt, bị cá voi nuốt chửng hoặc chết vì dịch bệnh nấm ký sinh.
```
**Part 5** → `audio/vs/scene05_p5.wav` (156 ký tự) · mood `hao_hung`

```text
Nhưng miễn là không bị nghiền nát thành tro bụi hay trở thành bữa ăn của kẻ khác, nó sẽ mãi mãi nắm giữ quyền năng quay ngược bánh xe thời gian để tái sinh!
```

### scene06 — TRIẾT LÝ CỦA SỰ BẤT TỬ VÀ BÓNG ĐEN KỲ SƯ ĐẬP NƯỚC
*Thẻ chương:* BÀI HỌC VỀ SỰ TÁI SINH VÀ BÓNG ĐEN KỸ SƯ HẢI LY TẬP 30

*Badge:* `TỔNG KẾT & DẤU ẤN` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (291 ký tự) · mood `am_ap`

```text
Tổng kết hồ sơ phòng thí nghiệm số hai mươi chín. Từ một giọt thạch trong suốt giữa đại dương bao la, Sinh Vật Bất Tử đã chứng minh cho nhân loại thấy rằng: giới hạn của sự sống là điều hoàn toàn có thể vượt qua, và tự nhiên luôn ẩn chứa những phép màu vượt xa trí tưởng tượng của con người!
```
**Part 1** → `audio/vs/scene06_p1.wav` (179 ký tự) · mood `hao_hung`

```text
Hội đồng khoa học biểu quyết: Đạt điểm mười xuất sắc cho cơ chế sinh học đảo ngược lão hóa vĩ đại nhất hành tinh! Ký tên: Viện trưởng phòng thí nghiệm sinh học cực hạn! [laughter]
```
**Part 2** → `audio/vs/scene06_p2.wav` (364 ký tự) · mood `am_ap`

```text
Còn quý vị khán giả thì sao? Nếu loài người thực sự giải mã thành công hệ gen của sứa để có được năng lực bất tử: cứ già đi lại quay về tuổi mười tám để sống lại một cuộc đời mới, bạn có muốn sở hữu món quà đó không? Hay vòng đời hữu hạn mới chính là điều làm nên giá trị đẹp đẽ nhất của cuộc sống? Hãy chia sẻ suy nghĩ sâu sắc của bạn bên dưới phần bình luận nhé!
```
**Part 3** → `audio/vs/scene06_p3.wav` (641 ký tự) · mood `hao_hung`

```text
Cánh cửa phòng thí nghiệm số hai mươi chín xin được khép lại tại đây. Nhưng tập sau, chúng ta sẽ chuyển ống kính sang một chương trình truyền hình thực tế hai mươi tư giờ nghẹt thở trên cạn! Chúng ta sẽ theo chân một kỹ sư xây dựng đại tài nhưng mắc chứng ám ảnh cưỡng chế cực kỳ lầy lội! Một sinh vật có bộ răng cửa màu cam chứa đầy kim loại sắt cứng hơn cả gỗ lim, suốt ngày đêm phát điên mỗi khi nghe tiếng nước chảy và sẵn sàng đắp bùn đất bịt kín cả chiếc loa phát nhạc để dựng nên những con đập làm thay đổi dòng chảy của cả một vùng sông ngòi! Đố các bạn biết bóng đen bí ẩn kỳ sau là loài vật nào? Hãy đoán ngay ở phần bình luận nhé!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Một sinh vật già yếu cận kề cái chết bỗng nhiên tự biến ngược thành trẻ sơ sinh để sống lại từ đầu một cuộc đời mới! [laughter] Xin giới thiệu Sứa Bất Tử, loài sinh vật bé nhỏ chỉ bốn phẩy năm mi-li-mét sống dưới đáy đại dương. Khi bị đói, bị thương nặng hoặc già cỗi, nó không hề chết đi! [surprise-wa] Thay vào đó, nó kích hoạt quá trình chuyển biệt hóa tế bào thần kỳ: toàn bộ tế bào cơ bắp và biểu bì tự tẩy trắng danh tính, quay trở lại thành tế bào gốc phôi thai! Khối cơ thể sứa chìm xuống đáy biển hóa thành búp polyp non nớt, rồi từ đó nhân bản ra hàng trăm chú sứa con mới tinh! Miễn là không bị kẻ thù ăn thịt, nó có thể lặp lại chu kỳ đảo ngược thời gian này mãi mãi, trở thành sinh vật bất tử duy nhất trên hành tinh!
```

**Whisper prompt:** `Sứa Bất Tử, Sinh Vật Bất Tử, Turritopsis dohrnii, polyp, medusa, chuyển biệt hóa tế bào, transdifferentiation, telomere, ADN, Địa Trung Hải, Nhật Bản, Shin Kubota, 4,5mm, 1883, 1992, 2022, 12 lần, 15 năm, 100%, 5 cấp độ, 24h, tuổi 18, Hải Ly, Castor`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| hai mươi chín | 29 |
| ba mươi | 30 |
| bốn phẩy năm mi-li-mét | 4,5mm |
| bốn phẩy năm | 4,5mm |
| năm cấp độ | 5 cấp độ |
| cấp độ một | cấp độ 1 |
| cấp độ hai | cấp độ 2 |
| cấp độ ba | cấp độ 3 |
| cấp độ bốn | cấp độ 4 |
| cấp độ năm | cấp độ 5 |
| Cấp độ bốn và cấp độ năm | Cấp độ 4 & 5 |
| cấp độ bốn và cấp độ năm | cấp độ 4 & 5 |
| thứ nhất | thứ 1 |
| thứ hai | thứ 2 |
| thứ ba | thứ 3 |
| thứ tư | thứ 4 |
| thứ năm | thứ 5 |
| mười hai lần | 12 lần |
| mười lăm năm | 15 năm |
| tuổi mười tám | tuổi 18 |
| hai mươi tư giờ | 24h |
| hàng trăm | hàng trăm |
| hàng ngàn | hàng ngàn |
| hàng triệu | hàng triệu |
| hàng chục | hàng chục |
| một giây | 1 giây |
| vài ngày | vài ngày |
| ba ngày | 3 ngày |
| bốn ngày | 4 ngày |
| ba đến bốn ngày | 3-4 ngày |
| một trăm phần trăm | 100% |
| điểm mười | điểm 10 |
| Địa Trung Hải | Địa Trung Hải |
| một ngàn | 1.000 |
| gần một ngàn | gần 1.000 |
| tám mươi đến chín mươi | 80-90 |
| tám mươi | 80 |
| chín mươi | 90 |
| Nhật Bản | Nhật Bản |
| Shin Kubota | Shin Kubota |
| năm một ngàn tám trăm tám mươi ba | 1883 |
| Năm một ngàn chín trăm chín mươi hai | 1992 |
| năm một ngàn chín trăm chín mươi hai | 1992 |
| Năm hai ngàn không trăm hai mươi hai | 2022 |
| năm hai ngàn không trăm hai mươi hai | 2022 |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · BÍ ẨN PHÁ VỠ QUY LUẬT SINH TỬ CỦA VŨ TRỤ · 87.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:14.8 (14.8s) | L01 | Chào mừng quý vị đồng nghiệp và các bạn đến với phòng thí nghiệm sinh học cực hạn! Trong tự nhiên, có một chân lý sắt đá mà mọi sinh vật từ vi khuẩn bé nhỏ cho đến loài người vĩ đại đều phải tuân theo: Sinh ra, lớn lên, già nua và trở về với cát bụi. Đó là định luật nhiệt động lực học không thể đảo ngược! |  | Căn phòng thí nghiệm sinh học cực hạn hiện đại với các dàn ống nghiệm phát sáng huỳnh quang xanh ngọc, máy quét phân tử và màn hình biểu đồ nhiệt động lực học. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b02 | 00:14.8–00:23.9 (9.1s) | L02 | Thưa giáo sư, mẫu vật số 29 vừa được đưa từ vùng biển Địa Trung Hải về phòng lab, các chỉ số tế bào đang đảo ngược chiều thời gian một cách không tưởng! |  | BÊN TRÁI nữ trợ lý phòng lab đeo kính bảo hộ cầm khay kính đựng mẫu vật số 29 phát sáng; BÊN PHẢI ông giáo sư già tóc bạc đeo kính lão cầm kính hiển vi chăm chú quan sát. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b03 | 00:23.9–00:31.1 (7.2s) | L03 | Bật toàn bộ kính hiển vi điện tử quét lên! Hôm nay chúng ta sẽ cùng nhau thực hiện 5 cấp độ thử nghiệm sinh tử để giải mã một bí ẩn vĩ đại nhất hành tinh! | **5 CẤP ĐỘ** · thử nghiệm sinh tử · R/350 · [0.65, 0.45] | Kính hiển vi điện tử quét công suất lớn chiếu chùm tia laser xanh vào mẫu vật, màn hình hiện 5 CẤP ĐỘ THỬ NGHIỆM SINH TỬ. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b04 | 00:31.1–00:37.7 (6.6s) | L04 | Xin trân trọng giới thiệu: đây là Turritopsis dohrnii, loài sinh vật biển độc nhất vô nhị được mệnh danh là Sinh Vật Bất Tử! |  | chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa bơi lơ lửng giữa làn nước biển trong suốt, chuông sứa lấp lánh ánh hào quang xanh ngọc rực rỡ mang danh hiệu |
| b05 | 00:37.7–00:47.5 (9.8s) | L05 | Loài sứa này được các nhà khoa học mô tả lần đầu vào 1883, nhưng phải mất hơn một thế kỷ sau, nhân loại mới tình cờ phát hiện ra quyền năng kinh ngạc của nó. |  | BÀN TAY người xòe ra so sánh: chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa nhỏ xíu chỉ 4,5mm nằm lọt thỏm trên đầu ngón tay út con người. |
| b06 | 00:47.5–00:58.0 (10.5s) | L06 | Với kích thước trưởng thành chỉ vỏn vẹn 4,5mm — bé hơn cả một đầu ngón tay út — nhưng bên trong khối thạch trong suốt mỏng manh ấy là chiếc chìa khóa phá vỡ bản án tử thần của tự nhiên! | **CỠ 4,5MM** · kích thước tí hon · L/350 · [0.35, 0.45] | Bàn tay người xòe ra so sánh: chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa nhỏ xíu chỉ 4,5mm nằm lọt thỏm trên đầu ngón tay út, bên trong khối thạch tron |
| b07 | 00:58.0–01:11.0 (13.1s) | L07 | Nếu bạn nghĩ đây chỉ là một loài sứa bình thường trôi dạt lững lờ theo dòng nước biển, thì hãy chuẩn bị tinh thần! Vì ngay bây giờ, chúng ta sẽ lần lượt đưa Sinh Vật Bất Tử qua năm tầng thử thách cực hạn để tận mắt chứng kiến bánh xe thời gian bị bẻ cong như thế nào! |  | Chiếc đồng hồ cát ma thuật bị bẻ cong trong không gian vũ trụ, những hạt cát thời gian phát sáng chảy ngược từ dưới lên trên. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b08 | 01:11.0–01:17.8 (6.8s) | L08 | Hãy quan sát thật kỹ cấu trúc giải phẫu dưới ánh đèn huỳnh quang: một chiếc chuông sứa hình bán cầu trong suốt như thủy tinh pha lê, |  | Cận cảnh giải phẫu chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa: chuông sứa trong suốt như pha lê để lộ dạ dày màu đỏ tươi rực rỡ và 80-90 chiếc xúc tu m |
| b09 | 01:17.8–01:27.5 (9.7s) | L09 | bên trong lộ rõ dạ dày màu đỏ tươi rực rỡ và xung quanh mép chuông có tới 80-90 chiếc xúc tu mảnh mai như sợi tơ nhện. Một kiệt tác tạo hình của đại dương sâu thẳm! | **80-90 TU** · xúc tu tơ nhện · R/350 · [0.65, 0.48] | Cận cảnh dạ dày màu đỏ tươi rực rỡ nằm giữa chiếc chuông sứa trong suốt như thủy tinh pha lê, xung quanh mép chuông tỏa ra những xúc tu mảnh như sợi tơ nhện. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |

### scene02 · THỬ THÁCH TỔN THƯƠNG CƠ HỌC VÀ STRESS MÔI TRƯỜNG CỰC HẠN · 85.8s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:13.9 (13.9s) | L10 | Bước vào cấp độ thử nghiệm thứ 1: Kích hoạt tình trạng nguy cấp cận kề cái chết! Đối với bất kỳ sinh vật nào khác, khi bị bỏ đói nhiều ngày, bị giảm độ mặn đột ngột hoặc chịu những vết cắt thương tật xé rách cơ thể, kết cục tất yếu sẽ là cái chết và sự phân hủy hoàn toàn. |  | Bảng hồ sơ hiện CẤP ĐỘ 1: STRESS MÔI TRƯỜNG CỰC HẠN; một chú sứa bị bỏ đói nhiều ngày chìm xuống đáy đĩa thí nghiệm. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b02 | 00:13.9–00:26.2 (12.3s) | L11 | 1992, tại một phòng thí nghiệm ở Ý, các nhà sinh học biển đã vô tình để quên một vài cá thể sứa già yếu trong đĩa thí nghiệm mà không cho ăn. Vài ngày sau quay lại, họ không hề nhìn thấy những xác chết thối rữa như dự đoán! | **NĂM 1992** · phát hiện tại Ý · L/350 · [0.35, 0.45] | Phòng thí nghiệm ven biển ở Ý năm 1992: đĩa petri đựng sứa già yếu bị bỏ quên trên bàn đá dưới ánh trăng. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b03 | 00:26.2–00:40.6 (14.4s) | L12 | Thay vào đó, dưới đáy đĩa thủy tinh là những cụm polyp non nớt đang đâm chồi phát triển rực rỡ, hệt như những hạt mầm vừa mới nảy mầm sau cơn mưa đầu mùa! Những con sứa già cỗi không hề chết đi, chúng đã tự động chuyển đổi trạng thái cơ thể để trốn thoát lưỡi hái tử thần! |  | Đáy đĩa thủy tinh đâm chồi những mầm polyp non nớt màu cam rực rỡ nảy mầm như vườn hoa sau mưa; các nhà khoa học trợn tròn mắt. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b04 | 00:40.6–00:52.8 (12.2s) | L13 | Khi đối mặt với khủng hoảng sinh tồn, Sinh Vật Bất Tử không kích hoạt chế độ tự sát hay suy sụp tế bào. Ngược lại, nó phát đi một mệnh lệnh sinh học tối cao tới từng tế bào: Dừng ngay quá trình lão hóa, thu hồi toàn bộ xúc tu và chuẩn bị đảo ngược chu kỳ sống! |  | chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa phát đi làn sóng tín hiệu sinh học màu vàng chỉ huy khắp cơ thể: lập tức dừng lão hóa và chuẩn bị đảo ngược  |
| b05 | 00:52.8–01:05.3 (12.5s) | L14 | Toàn bộ chiếc chuông sứa hình dù bắt đầu co thắt mạnh mẽ, các mô liên kết mềm nhũn ra và chìm dần xuống đáy biển sâu. Đây không phải là sự buông xuôi đầu hàng số phận, mà là phát súng lệnh mở màn cho một phép màu sinh học kỳ diệu chưa từng thấy trong lịch sử tự nhiên! |  | Chiếc chuông sứa của chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa co thắt mạnh mẽ, toàn bộ xúc tu tự thu gọn vào trong rồi từ từ chìm xuống đáy nước xanh |
| b06 | 01:05.3–01:18.3 (12.9s) | L15 | Nhóm nghiên cứu tại vịnh Genoa sau đó đã lặp lại thí nghiệm này hàng trăm lần với nhiều hình thức kích thích cực đoan khác nhau: hạ nhiệt độ nước xuống gần điểm đóng băng, tăng độ mặn lên gấp đôi, thậm chí dùng dao vi phẫu cắt đôi cơ thể sứa. |  | Hàng loạt thí nghiệm cực đoan tại vịnh Genoa: cắt đôi sứa, hạ nhiệt độ đóng băng, khối tế bào vẫn tự gom lại tái sinh; bảng Cấp độ 1 bật PASS. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b07 | 01:18.3–01:25.8 (7.5s) | L16 | Kết quả kinh ngạc là trong hầu hết mọi trường hợp, cơ thể nó đều tự gom lại thành một khối tế bào sống sót và bắt đầu quá trình tái sinh ngoạn mục! |  | Khối tế bào sống sót của sứa tự gom lại thành một cụm tròn lấp lánh và bắt đầu quá trình tái sinh ngoạn mục dưới ánh đèn phòng lab. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |

### scene03 · CƠ CHẾ CHUYỂN BIỆT HÓA TẾ BÀO TRANSDIFFERENTIATION THẦN KỲ · 80.3s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.0 (7.0s) | L17 | Bước vào cấp độ thử nghiệm thứ 2: Soi rọi vào cỗ máy phân tử Transdifferentiation — Chuyển biệt hóa tế bào! Hãy hình dung thế này cho dễ |  | Bảng hồ sơ hiện CẤP ĐỘ 2: CHUYỂN BIỆT HÓA TRANSDIFFERENTIATION; đồ họa tế bào cơ tim và tế bào da người cố định vĩnh viễn không thể đổi vai. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b02 | 00:07.0–00:15.6 (8.6s) | L18 | hiểu: Trong cơ thể người, một tế bào cơ tim vĩnh viễn là tế bào cơ tim, tế bào da vĩnh viễn là tế bào da. Bạn không thể bắt một tế bào da biến thành tế bào mắt hay tế bào não được! |  | Sơ đồ hoạt hình dễ thương: các tế bào tròn nhiều màu mỗi loại đứng đúng vị trí của mình; ông giáo sư già tóc bạc đeo kính lão cầm kính hiển vi mỉm cười giải thích. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b03 | 00:15.6–00:24.4 (8.7s) | L19 | Báo cáo kính hiển vi: Các tế bào biểu bì và tế bào thần kinh của mẫu vật đang tự tẩy trắng danh tính ban đầu, chúng đang biến ngược thành tế bào gốc phôi thai! |  | Hình ảnh kính hiển vi huỳnh quang: tế bào cơ bắp của sứa tự tẩy sạch màu sắc ban đầu, biến ngược thành những tế bào gốc phôi thai non nớt. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b04 | 00:24.4–00:39.3 (14.9s) | L20 | Chính xác là như vậy! Sinh Vật Bất Tử sở hữu một siêu năng lực mà y học hiện đại thèm khát suốt hàng thế kỷ: Nó có thể ra lệnh cho một tế bào cơ bắp đã trưởng thành tự xóa bỏ chức năng hiện tại, quay trở lại trạng thái tế bào gốc sơ khai chưa chuyên hóa, rồi từ đó biến đổi thành bất kỳ loại tế bào nào khác cần thiết! |  | chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa được bao bọc trong vầng sáng tế bào gốc lấp lánh, các tế bào cơ bắp trưởng thành tự do biến đổi thành bất kỳ |
| b05 | 00:39.3–00:50.3 (11.1s) | L21 | Các nhà khoa học ví hiện tượng này giống như việc một con bướm trưởng thành xinh đẹp bỗng nhiên thu gọn đôi cánh lại, hóa ngược thành một chiếc kén tằm, rồi từ chiếc kén lại chui ra một chú sâu bướm non nớt! |  | Hình ảnh ẩn dụ kỳ diệu: BÊN TRÁI một chú bướm thu cánh lại chui vào kén tằm; BÊN PHẢI từ kén chui ra chú sâu bướm non nớt. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b06 | 00:50.3–00:54.8 (4.5s) | L22 | Một quy trình đảo ngược thời gian hoàn chỉnh diễn ra chỉ trong vòng 3-4 ngày! | **3-4 NGÀY** · đảo ngược hoàn toàn · R/350 · [0.65, 0.45] | Đồng hồ cát thời gian xoay ngược: quy trình đảo ngược hoàn chỉnh chỉ diễn ra trong vòng 3-4 ngày, chú sâu bướm non nớt chui ra khỏi chiếc kén. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b07 | 00:54.8–01:07.6 (12.8s) | L23 | Hàng triệu tế bào khắp cơ thể sứa phối hợp tái tổ chức lại với nhau trong một vũ điệu sinh học hoàn hảo. Không có bất kỳ sự hỗn loạn hay sai sót nào xảy ra. Mọi dấu vết của sự già nua và bệnh tật tích tụ trong kiếp sống cũ đều bị xóa sạch hoàn toàn không tì vết! |  | Hàng triệu tế bào khắp cơ thể sứa xếp hàng phối hợp tái tổ chức lại trong một vũ điệu sinh học hoàn mỹ, xóa sạch dấu vết già nua. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b08 | 01:07.6–01:20.3 (12.7s) | L24 | Ở động vật có xương sống bậc cao, khi mô bị tổn thương, cơ thể chỉ có thể hình thành mô sẹo xơ cứng để vá víu tạm bợ. Nhưng ở chú sứa kỳ diệu này, toàn bộ mạng lưới tế bào được lập trình lại từ đầu, loại bỏ hoàn toàn sẹo và khôi phục sự nguyên vẹn hoàn mỹ như lúc mới chào đời! |  | So sánh: BÊN TRÁI vết sẹo xơ cứng của động vật có xương; BÊN PHẢI chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa tái sinh hoàn mỹ không để lại vết sẹo; bản |

### scene04 · HÓA THÀNH BÚP POLYP NON NỚT VÀ NHÂN BẢN HÀNG TRĂM BẢN SAO · 80.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:14.2 (14.2s) | L25 | Bước sang cấp độ thử nghiệm thứ 3: Tái tạo cấu trúc sống từ con số không! Sau khi toàn bộ các tế bào đã được trẻ hóa thành công, khối cơ thể thạch của sứa chìm xuống đáy biển và bám chặt vào một tảng đá hay vỏ ốc rỗng. Tại đây, nó biến thành một khối búp tròn màu cam nhạt gọi là kén cyst. |  | Bảng hồ sơ hiện CẤP ĐỘ 3: TÁI TẠO CẤU TRÚC SỐNG TỪ CON SỐ KHÔNG; khối cơ thể thạch của sứa chìm xuống đáy biển bám vào vỏ ốc rỗng. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b02 | 00:14.2–00:28.2 (14.0s) | L26 | Từ chiếc kén non nớt này, một phép màu sinh sản tiếp tục bùng nổ: Nó mọc rễ và vươn lên thành một quần thể polyp mới tinh! Polyp này bắt đầu đâm chồi, phân nhánh như những cành cây nhỏ dưới đáy biển và nuôi dưỡng hàng chục, thậm chí hàng trăm chồi sứa non lơ lửng! |  | khối kén tròn cyst màu cam nhạt bám trên vỏ ốc rỗng kén tròn màu cam nhạt mọc rễ vươn nhánh lên thành quần thể thảm polyp san hô non nớt màu cam nhạt đâm chồi dưới đáy biển rực rỡ như cây san hô tí hon nuôi dưỡng hàng chục chồi sứa non. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b03 | 00:28.2–00:35.6 (7.4s) | L27 | Khi đến thời điểm thích hợp, từng chiếc chuông sứa con trong suốt tách mình ra khỏi cành polyp, bung nở xúc tu bơi vút lên mặt nước để bắt đầu một kiếp sống mới! |  | Từng chiếc chuông sứa con trong suốt tách mình ra khỏi polyp bay vút lên mặt nước; hàng trăm bản sao giống hệt sứa mẹ ban đầu. |
| b04 | 00:35.6–00:43.8 (8.2s) | L28 | Hãy chú ý kỹ điều này: Từ một cá thể sứa già nua duy nhất ban đầu, nó không chỉ trẻ lại cho riêng mình, mà còn nhân bản ra hàng trăm bản sao giống hệt nhau về mặt di truyền! | **100 BẢN** · nhân bản di truyền · L/350 · [0.35, 0.45] | Từ một chú sứa già nua duy nhất ban đầu nhân bản ra hàng trăm bản sao giống hệt nhau về mặt di truyền, xếp thành hàng dài lấp lánh. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b05 | 00:43.8–00:50.7 (6.9s) | L29 | Giáo sư Shin Kubota tại Đại học Kyoto Nhật Bản đã dành hơn 15 năm cuộc đời để chăm sóc loài sứa này trong phòng thí nghiệm. |  | Giáo sư Shin Kubota tại Đại học Kyoto mỉm cười nâng niu bể nuôi sứa lặp lại chu kỳ đảo ngược lão hóa tới 12 lần liên tiếp. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b06 | 00:50.7–00:58.9 (8.2s) | L30 | Ông đã chứng kiến một cá thể sứa lặp lại chu kỳ đảo ngược lão hóa này tới 12 lần liên tiếp mà sức sống vẫn tràn trề không hề suy giảm! | **12 LẦN** · chu kỳ trẻ hóa · R/350 · [0.65, 0.45] | ông giáo sư già tóc bạc đeo kính lão cầm kính hiển vi ghi nhật ký quan sát một chú sứa lặp lại chu kỳ đảo ngược lão hóa 12 lần liên tiếp mà sức sống vẫn tràn trề. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b07 | 00:58.9–01:06.8 (7.9s) | L31 | Về mặt lý thuyết sinh học thuần túy, chu kỳ này có thể lặp đi lặp lại vô tận đến vĩnh hằng! Sinh Vật Bất Tử hoàn toàn miễn nhiễm trước cái chết vì tuổi già! |  | Vòng tròn vô cực biểu tượng bất tử: chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa bơi lượn trong chu kỳ tuần hoàn vĩnh cửu không bao giờ chết vì tuổi già. |
| b08 | 01:06.8–01:20.5 (13.7s) | L32 | Mỗi nhánh polyp dưới đáy biển giống như một nhà máy sản xuất sinh học tự động: khi nhiệt độ nước ấm lên vào mùa xuân, các chồi sứa bắt đầu nhấp nháy phát sáng rồi tách rời cuống bơi đi. Một chu trình tuần hoàn vĩnh cửu nối liền quá khứ và tương lai mà không bao giờ có điểm kết thúc! |  | Nhà máy sinh học tự động dưới đáy biển: các chồi sứa nhấp nháy phát sáng rồi bung nở xúc tu bơi đi đón mùa xuân; bảng Cấp độ 3 bật PASS. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |

### scene05 · GIẢI MÃ BÍ MẬT BẢO VỆ TELOMERE VÀ GEN SỬA CHỮA ADN · 91.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:05.2 (5.2s) | L33 | Bước vào hai cấp độ tối mật cuối cùng: Cấp độ 4 & 5 — Giải mã bản thiết kế hệ gen! |  | Bảng hồ sơ hiện CẤP ĐỘ 4 & 5: GIẢI MÃ BẢN THIẾT KẾ HỆ GEN; chuỗi xoắn kép ADN phát sáng rực rỡ trong phòng lab. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b02 | 00:05.2–00:16.3 (11.2s) | L34 | 2022, một công trình nghiên cứu chấn động thế giới đăng trên tạp chí danh giá PNAS do tiến sĩ Maria Pascual-Torner dẫn đầu đã giải trình tự toàn bộ bộ gen của Turritopsis dohrnii. |  | Bìa tạp chí PNAS năm 2022 mở ra bản đồ giải trình tự toàn bộ bộ gen của Turritopsis dohrnii do tiến sĩ Maria Pascual-Torner dẫn đầu. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b03 | 00:16.3–00:22.8 (6.5s) | L35 | Kết quả phân tích đã hé lộ hai vũ khí phân tử vô giá: Thứ nhất là hệ thống bảo vệ telomere — đoạn mũ bảo vệ ở hai đầu sợi nhiễm sắc thể. | **TELOMERE** · mũ bảo vệ ADN · L/350 · [0.35, 0.45] | Cận cảnh phân tử: enzym telomerase gắn dài thêm đoạn mũ telomere ở đầu sợi nhiễm sắc thể, đồng hồ tuổi tác tế bào không bị điểm giờ chết. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b04 | 00:22.8–00:34.3 (11.5s) | L36 | Ở người, mỗi lần tế bào phân chia, telomere sẽ ngắn dần lại cho đến khi tế bào già nua và chết đi. Nhưng ở Sinh Vật Bất Tử, các enzym telomerase liên tục bảo dưỡng và kéo dài telomere, khiến đồng hồ tuổi tác của tế bào không bao giờ bị điểm giờ chết! |  | So sánh: ở người telomere ngắn dần mỗi lần tế bào phân chia; ở chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa enzym telomerase liên tục kéo dài telomere nê |
| b05 | 00:34.3–00:45.5 (11.2s) | L37 | Vũ khí thứ 2 là sự nhân đôi vượt trội của các gen liên quan đến sửa chữa ADN và chống oxy hóa. Cơ thể nó sở hữu số lượng bản sao gen sửa chữa lỗi sai sót phân tử nhiều gấp đôi so với các loài sứa thông thường! |  | Đội quân enzym phân tử tí hon cầm mỏ lết đi dọc chuỗi ADN sửa chữa lỗi sai sót và đột biến nhanh gấp đôi bình thường. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b06 | 00:45.5–00:50.8 (5.3s) | L38 | Bất kỳ tổn hại hay đột biến nào phát sinh đều được các cỗ máy enzym quét sạch và khắc phục ngay lập tức! |  | Đội quân enzym tí hon quét sạch mọi tổn hại và đột biến phát sinh trên chuỗi ADN rồi khắc phục ngay lập tức. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b07 | 00:50.8–01:00.7 (10.0s) | L39 | Các nhà khoa học đã so sánh bộ gen của nó với người họ hàng gần là loài sứa Turritopsis rubra — một loài sứa có ngoại hình gần như giống hệt nhưng lại không thể đảo ngược vòng đời. |  | So sánh hai chuỗi gen: BÊN TRÁI loài sứa họ hàng không bất tử; BÊN PHẢI chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa sở hữu gần 1.000 gen đặc hữu tái sin |
| b08 | 01:00.7–01:09.4 (8.6s) | L40 | Sự so sánh này đã chỉ ra chính xác gần 1.000 gen đặc hữu chịu trách nhiệm cho khả năng bất tử, mở ra chân trời mới cho ngành y học tái tạo và chống lão hóa của loài người! | **1.000 GEN** · đặc hữu bất tử · R/350 · [0.65, 0.45] | Hai chuỗi gen đối chiếu nhau, hiện ra gần 1.000 gen đặc hữu chịu trách nhiệm cho khả năng bất tử, mở ra chân trời mới cho y học tái tạo. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b09 | 01:09.4–01:22.7 (13.4s) | L41 | Tuy nhiên, cần phải làm rõ một hiểu lầm phổ biến: Bất tử về mặt sinh học không có nghĩa là bất khả chiến bại trước mọi hiểm nguy! Trong môi trường đại dương tự nhiên đầy rẫy kẻ thù, Sinh Vật Bất Tử vẫn có thể bị rùa biển ăn thịt, bị cá voi nuốt chửng hoặc chết vì dịch bệnh nấm ký sinh. |  | Một con rùa biển khổng lồ há miệng đớp sứa: bất tử sinh học nhưng không bất khả chiến bại trước kẻ săn mồi. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b10 | 01:22.7–01:31.2 (8.4s) | L42 | Nhưng miễn là không bị nghiền nát thành tro bụi hay trở thành bữa ăn của kẻ khác, nó sẽ mãi mãi nắm giữ quyền năng quay ngược bánh xe thời gian để tái sinh! |  | chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa kiêu hãnh bơi lên giữa làn nước xanh thẳm, vương miện thời gian phát sáng trên đầu; bảng Cấp độ 4 & 5 bật PA |

### scene06 · TRIẾT LÝ CỦA SỰ BẤT TỬ VÀ BÓNG ĐEN KỲ SƯ ĐẬP NƯỚC · 75.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:14.6 (14.6s) | L43 | Tổng kết hồ sơ phòng thí nghiệm số 29. Từ một giọt thạch trong suốt giữa đại dương bao la, Sinh Vật Bất Tử đã chứng minh cho nhân loại thấy rằng: giới hạn của sự sống là điều hoàn toàn có thể vượt qua, và tự nhiên luôn ẩn chứa những phép màu vượt xa trí tưởng tượng của con người! |  | Bàn tổng kết phòng thí nghiệm số 29: chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa đứng cạnh bản đồ giải mã gen bất tử với huy chương khoa học vàng óng. |
| b02 | 00:14.6–00:24.3 (9.7s) | L44 | Hội đồng khoa học biểu quyết: Đạt điểm 10 xuất sắc cho cơ chế sinh học đảo ngược lão hóa vĩ đại nhất hành tinh! Ký tên: Viện trưởng phòng thí nghiệm sinh học cực hạn! | **ĐIỂM 10** · đảo ngược lão hóa · R/350 · [0.65, 0.45] | Dấu mộc đỏ ĐẠT ĐIỂM 10 đóng lên tập hồ sơ đảo ngược lão hóa; cả hội đồng khoa học vỗ tay chúc mừng. |
| b03 | 00:24.3–00:35.0 (10.7s) | L45 | Còn quý vị khán giả thì sao? Nếu loài người thực sự giải mã thành công hệ gen của sứa để có được năng lực bất tử: cứ già đi lại quay về tuổi 18 để sống lại một cuộc đời mới, bạn có muốn sở hữu món quà đó không? |  | Hai bàn cân lựa chọn: BÊN TRÁI biểu tượng bất tử quay về tuổi 18; BÊN PHẢI biểu tượng vòng đời hữu hạn quý giá, khán giả giơ thẻ bình chọn. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b04 | 00:35.0–00:41.9 (6.9s) | L46 | Hay vòng đời hữu hạn mới chính là điều làm nên giá trị đẹp đẽ nhất của cuộc sống? Hãy chia sẻ suy nghĩ sâu sắc của bạn bên dưới phần bình luận nhé! |  | Cán cân suy ngẫm: một bên là bất tử quay về tuổi 18, một bên là vòng đời hữu hạn đẹp đẽ quý giá của cuộc sống. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b05 | 00:41.9–00:52.0 (10.1s) | L47 | Cánh cửa phòng thí nghiệm số 29 xin được khép lại tại đây. Nhưng tập sau, chúng ta sẽ chuyển ống kính sang một chương trình truyền hình thực tế 24h nghẹt thở trên cạn! |  | Cánh cửa phòng lab số 29 khép lại, chuyển sang ống kính máy quay chương trình thực địa rừng ôn đới Bắc Mỹ. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b06 | 00:52.0–00:57.0 (5.0s) | L48 | Chúng ta sẽ theo chân một kỹ sư xây dựng đại tài nhưng mắc chứng ám ảnh cưỡng chế cực kỳ lầy lội! |  | Một sinh vật bí ẩn được vẽ hoàn toàn bằng BÓNG ĐEN ĐẶC TUYỀN (solid black silhouette) hình chú chuột mập mạp béo ú có chiếc đuôi dẹp như mái chèo đang dùng hai chiếc răng cửa dài cắm vào thân cây gỗ lớn bên bờ suối; ba dấu hỏi chấm vàng to tướng; KHÔNG vẽ mắt mũi lông lá thật. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b07 | 00:57.0–01:10.1 (13.1s) | L49 | Một sinh vật có bộ răng cửa màu cam chứa đầy kim loại sắt cứng hơn cả gỗ lim, suốt ngày đêm phát điên mỗi khi nghe tiếng nước chảy và sẵn sàng đắp bùn đất bịt kín cả chiếc loa phát nhạc để dựng nên những con đập làm thay đổi dòng chảy của cả một vùng sông ngòi! |  | Cũng chiếc BÓNG ĐEN ĐẶC TUYỀN đó đang vác từng tảng bùn đất đắp kín mít một chiếc loa phát thanh đang phát sóng âm nhạc róc rách; ba dấu hỏi chấm to tướng. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |
| b08 | 01:10.1–01:15.4 (5.3s) | L50 | Đố các bạn biết bóng đen bí ẩn kỳ sau là loài vật nào? Hãy đoán ngay ở phần bình luận nhé! |  | Chiếc BÓNG ĐEN ĐẶC TUYỀN kỹ sư đắp đập đứng cạnh con đập gỗ khổng lồ chặn dòng sông, mời gọi khán giả đoán tên Hải Ly tập sau. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này. |

## 5. Phân cảnh Shorts — từng beat

Banner: **TỰ BIẾN NGƯỢC THÀNH SƠ SINH / ĐỂ BẤT TỬ MÃI MÃI?!** · giọng 38.9s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Một sinh vật già yếu cận kề cái chết bỗng nhiên tự biến ngược thành trẻ sơ sinh để sống lại từ đầu một cuộc đời mới! |  |
| s02 | 00:06.4 | S02 | Xin giới thiệu Sứa Bất Tử, loài sinh vật bé nhỏ chỉ 4,5mm sống dưới đáy đại dương. | **CHỈ 4,5MM** · kích thước siêu nhỏ · R/620 · [0.62, 0.5] |
| s03 | 00:12.3 | S03 | Khi bị đói, bị thương nặng hoặc già cỗi, nó không hề chết đi! |  |
| s04 | 00:16.7 | S04 | Thay vào đó, nó kích hoạt quá trình chuyển biệt hóa tế bào thần kỳ: |  |
| s05 | 00:20.2 | S05 | toàn bộ tế bào cơ bắp và biểu bì tự tẩy trắng danh tính, quay trở lại thành tế bào gốc phôi thai! |  |
| s06 | 00:25.3 | S06 | Khối cơ thể sứa chìm xuống đáy biển hóa thành búp polyp non nớt, |  |
| s07 | 00:28.7 | S07 | rồi từ đó nhân bản ra hàng trăm chú sứa con mới tinh! | **100 BẢN** · nhân bản vô tính · L/620 · [0.38, 0.5] |
| s08 | 00:31.6 | S08 | Miễn là không bị kẻ thù ăn thịt, nó có thể lặp lại chu kỳ đảo ngược thời gian này mãi mãi, |  |
| s09 | 00:36.3 | S09 | trở thành sinh vật bất tử duy nhất trên hành tinh! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chào mừng quý vị đồng nghiệp và các bạn đến với phòng thí nghiệm sinh học cực hạn! Trong tự nhiên, có một chân lý sắt đá mà mọi sinh vật từ vi khuẩn bé nhỏ cho đến loài người vĩ đại đều phải tuân theo: Sinh ra, lớn lên, già nua và trở về với cát bụi. Đó là định luật nhiệt động lực học không thể đảo ngược!". Bố cục: Căn phòng thí nghiệm sinh học cực hạn hiện đại với các dàn ống nghiệm phát sáng huỳnh quang xanh ngọc, máy quét phân tử và màn hình biểu đồ nhiệt động lực học. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thưa giáo sư, mẫu vật số 29 vừa được đưa từ vùng biển Địa Trung Hải về phòng lab, các chỉ số tế bào đang đảo ngược chiều thời gian một cách không tưởng!". Bố cục: BÊN TRÁI nữ trợ lý phòng lab đeo kính bảo hộ cầm khay kính đựng mẫu vật số 29 phát sáng; BÊN PHẢI ông giáo sư già tóc bạc đeo kính lão cầm kính hiển vi chăm chú quan sát. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bật toàn bộ kính hiển vi điện tử quét lên! Hôm nay chúng ta sẽ cùng nhau thực hiện 5 cấp độ thử nghiệm sinh tử để giải mã một bí ẩn vĩ đại nhất hành tinh!". Bố cục: Kính hiển vi điện tử quét công suất lớn chiếu chùm tia laser xanh vào mẫu vật, màn hình hiện 5 CẤP ĐỘ THỬ NGHIỆM SINH TỬ. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Xin trân trọng giới thiệu: đây là Turritopsis dohrnii, loài sinh vật biển độc nhất vô nhị được mệnh danh là Sinh Vật Bất Tử!". Bố cục: chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa bơi lơ lửng giữa làn nước biển trong suốt, chuông sứa lấp lánh ánh hào quang xanh ngọc rực rỡ mang danh hiệu Sinh Vật Bất Tử.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Loài sứa này được các nhà khoa học mô tả lần đầu vào 1883, nhưng phải mất hơn một thế kỷ sau, nhân loại mới tình cờ phát hiện ra quyền năng kinh ngạc của nó.". Bố cục: BÀN TAY người xòe ra so sánh: chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa nhỏ xíu chỉ 4,5mm nằm lọt thỏm trên đầu ngón tay út con người.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Với kích thước trưởng thành chỉ vỏn vẹn 4,5mm — bé hơn cả một đầu ngón tay út — nhưng bên trong khối thạch trong suốt mỏng manh ấy là chiếc chìa khóa phá vỡ bản án tử thần của tự nhiên!". Bố cục: Bàn tay người xòe ra so sánh: chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa nhỏ xíu chỉ 4,5mm nằm lọt thỏm trên đầu ngón tay út, bên trong khối thạch trong suốt phát sáng như chiếc chìa khóa của tự nhiên.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu bạn nghĩ đây chỉ là một loài sứa bình thường trôi dạt lững lờ theo dòng nước biển, thì hãy chuẩn bị tinh thần! Vì ngay bây giờ, chúng ta sẽ lần lượt đưa Sinh Vật Bất Tử qua năm tầng thử thách cực hạn để tận mắt chứng kiến bánh xe thời gian bị bẻ cong như thế nào!". Bố cục: Chiếc đồng hồ cát ma thuật bị bẻ cong trong không gian vũ trụ, những hạt cát thời gian phát sáng chảy ngược từ dưới lên trên. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy quan sát thật kỹ cấu trúc giải phẫu dưới ánh đèn huỳnh quang: một chiếc chuông sứa hình bán cầu trong suốt như thủy tinh pha lê,". Bố cục: Cận cảnh giải phẫu chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa: chuông sứa trong suốt như pha lê để lộ dạ dày màu đỏ tươi rực rỡ và 80-90 chiếc xúc tu mảnh mai như sợi tơ nhện.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bên trong lộ rõ dạ dày màu đỏ tươi rực rỡ và xung quanh mép chuông có tới 80-90 chiếc xúc tu mảnh mai như sợi tơ nhện. Một kiệt tác tạo hình của đại dương sâu thẳm!". Bố cục: Cận cảnh dạ dày màu đỏ tươi rực rỡ nằm giữa chiếc chuông sứa trong suốt như thủy tinh pha lê, xung quanh mép chuông tỏa ra những xúc tu mảnh như sợi tơ nhện. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bước vào cấp độ thử nghiệm thứ 1: Kích hoạt tình trạng nguy cấp cận kề cái chết! Đối với bất kỳ sinh vật nào khác, khi bị bỏ đói nhiều ngày, bị giảm độ mặn đột ngột hoặc chịu những vết cắt thương tật xé rách cơ thể, kết cục tất yếu sẽ là cái chết và sự phân hủy hoàn toàn.". Bố cục: Bảng hồ sơ hiện CẤP ĐỘ 1: STRESS MÔI TRƯỜNG CỰC HẠN; một chú sứa bị bỏ đói nhiều ngày chìm xuống đáy đĩa thí nghiệm. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "1992, tại một phòng thí nghiệm ở Ý, các nhà sinh học biển đã vô tình để quên một vài cá thể sứa già yếu trong đĩa thí nghiệm mà không cho ăn. Vài ngày sau quay lại, họ không hề nhìn thấy những xác chết thối rữa như dự đoán!". Bố cục: Phòng thí nghiệm ven biển ở Ý năm 1992: đĩa petri đựng sứa già yếu bị bỏ quên trên bàn đá dưới ánh trăng. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thay vào đó, dưới đáy đĩa thủy tinh là những cụm polyp non nớt đang đâm chồi phát triển rực rỡ, hệt như những hạt mầm vừa mới nảy mầm sau cơn mưa đầu mùa! Những con sứa già cỗi không hề chết đi, chúng đã tự động chuyển đổi trạng thái cơ thể để trốn thoát lưỡi hái tử thần!". Bố cục: Đáy đĩa thủy tinh đâm chồi những mầm polyp non nớt màu cam rực rỡ nảy mầm như vườn hoa sau mưa; các nhà khoa học trợn tròn mắt. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi đối mặt với khủng hoảng sinh tồn, Sinh Vật Bất Tử không kích hoạt chế độ tự sát hay suy sụp tế bào. Ngược lại, nó phát đi một mệnh lệnh sinh học tối cao tới từng tế bào: Dừng ngay quá trình lão hóa, thu hồi toàn bộ xúc tu và chuẩn bị đảo ngược chu kỳ sống!". Bố cục: chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa phát đi làn sóng tín hiệu sinh học màu vàng chỉ huy khắp cơ thể: lập tức dừng lão hóa và chuẩn bị đảo ngược chu kỳ sống.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn bộ chiếc chuông sứa hình dù bắt đầu co thắt mạnh mẽ, các mô liên kết mềm nhũn ra và chìm dần xuống đáy biển sâu. Đây không phải là sự buông xuôi đầu hàng số phận, mà là phát súng lệnh mở màn cho một phép màu sinh học kỳ diệu chưa từng thấy trong lịch sử tự nhiên!". Bố cục: Chiếc chuông sứa của chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa co thắt mạnh mẽ, toàn bộ xúc tu tự thu gọn vào trong rồi từ từ chìm xuống đáy nước xanh thẳm.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhóm nghiên cứu tại vịnh Genoa sau đó đã lặp lại thí nghiệm này hàng trăm lần với nhiều hình thức kích thích cực đoan khác nhau: hạ nhiệt độ nước xuống gần điểm đóng băng, tăng độ mặn lên gấp đôi, thậm chí dùng dao vi phẫu cắt đôi cơ thể sứa.". Bố cục: Hàng loạt thí nghiệm cực đoan tại vịnh Genoa: cắt đôi sứa, hạ nhiệt độ đóng băng, khối tế bào vẫn tự gom lại tái sinh; bảng Cấp độ 1 bật PASS. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kết quả kinh ngạc là trong hầu hết mọi trường hợp, cơ thể nó đều tự gom lại thành một khối tế bào sống sót và bắt đầu quá trình tái sinh ngoạn mục!". Bố cục: Khối tế bào sống sót của sứa tự gom lại thành một cụm tròn lấp lánh và bắt đầu quá trình tái sinh ngoạn mục dưới ánh đèn phòng lab. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bước vào cấp độ thử nghiệm thứ 2: Soi rọi vào cỗ máy phân tử Transdifferentiation — Chuyển biệt hóa tế bào! Hãy hình dung thế này cho dễ hiểu:". Bố cục: Bảng hồ sơ hiện CẤP ĐỘ 2: CHUYỂN BIỆT HÓA TRANSDIFFERENTIATION; đồ họa tế bào cơ tim và tế bào da người cố định vĩnh viễn không thể đổi vai. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong cơ thể người, một tế bào cơ tim vĩnh viễn là tế bào cơ tim, tế bào da vĩnh viễn là tế bào da. Mỗi loại tế bào giữ nguyên vai trò của mình.". Bố cục: Sơ đồ hoạt hình dễ thương: các tế bào tròn nhiều màu mỗi loại đứng đúng vị trí của mình; ông giáo sư già tóc bạc đeo kính lão cầm kính hiển vi mỉm cười giải thích. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo kính hiển vi: Các tế bào biểu bì và tế bào thần kinh của mẫu vật đang tự tẩy trắng danh tính ban đầu, chúng đang biến ngược thành tế bào gốc phôi thai!". Bố cục: Hình ảnh kính hiển vi huỳnh quang: tế bào cơ bắp của sứa tự tẩy sạch màu sắc ban đầu, biến ngược thành những tế bào gốc phôi thai non nớt. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chính xác là như vậy! Sinh Vật Bất Tử sở hữu một siêu năng lực mà y học hiện đại thèm khát suốt hàng thế kỷ: Nó có thể ra lệnh cho một tế bào cơ bắp đã trưởng thành tự xóa bỏ chức năng hiện tại, quay trở lại trạng thái tế bào gốc sơ khai chưa chuyên hóa, rồi từ đó biến đổi thành bất kỳ loại tế bào nào khác cần thiết!". Bố cục: chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa được bao bọc trong vầng sáng tế bào gốc lấp lánh, các tế bào cơ bắp trưởng thành tự do biến đổi thành bất kỳ tế bào nào khác cần thiết.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học ví hiện tượng này giống như việc một con bướm trưởng thành xinh đẹp bỗng nhiên thu gọn đôi cánh lại, hóa ngược thành một chiếc kén tằm, rồi từ chiếc kén lại chui ra một chú sâu bướm non nớt!". Bố cục: Hình ảnh ẩn dụ kỳ diệu: BÊN TRÁI một chú bướm thu cánh lại chui vào kén tằm; BÊN PHẢI từ kén chui ra chú sâu bướm non nớt. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một quy trình đảo ngược thời gian hoàn chỉnh diễn ra chỉ trong vòng 3-4 ngày!". Bố cục: Đồng hồ cát thời gian xoay ngược: quy trình đảo ngược hoàn chỉnh chỉ diễn ra trong vòng 3-4 ngày, chú sâu bướm non nớt chui ra khỏi chiếc kén. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hàng triệu tế bào khắp cơ thể sứa phối hợp tái tổ chức lại với nhau trong một vũ điệu sinh học hoàn hảo. Không có bất kỳ sự hỗn loạn hay sai sót nào xảy ra. Mọi dấu vết của sự già nua và bệnh tật tích tụ trong kiếp sống cũ đều bị xóa sạch hoàn toàn không tì vết!". Bố cục: Hàng triệu tế bào khắp cơ thể sứa xếp hàng phối hợp tái tổ chức lại trong một vũ điệu sinh học hoàn mỹ, xóa sạch dấu vết già nua. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở động vật có xương sống bậc cao, khi mô bị tổn thương, cơ thể chỉ có thể hình thành mô sẹo xơ cứng để vá víu tạm bợ. Nhưng ở chú sứa kỳ diệu này, toàn bộ mạng lưới tế bào được lập trình lại từ đầu, loại bỏ hoàn toàn sẹo và khôi phục sự nguyên vẹn hoàn mỹ như lúc mới chào đời!". Bố cục: So sánh: BÊN TRÁI vết sẹo xơ cứng của động vật có xương; BÊN PHẢI chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa tái sinh hoàn mỹ không để lại vết sẹo; bảng Cấp độ 2 bật PASS.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bước sang cấp độ thử nghiệm thứ 3: Tái tạo cấu trúc sống từ con số không! Sau khi toàn bộ các tế bào đã được trẻ hóa thành công, khối cơ thể thạch của sứa chìm xuống đáy biển và bám chặt vào một tảng đá hay vỏ ốc rỗng. Tại đây, nó biến thành một khối búp tròn màu cam nhạt gọi là kén cyst.". Bố cục: Bảng hồ sơ hiện CẤP ĐỘ 3: TÁI TẠO CẤU TRÚC SỐNG TỪ CON SỐ KHÔNG; khối cơ thể thạch của sứa chìm xuống đáy biển bám vào vỏ ốc rỗng. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Từ chiếc kén non nớt này, một phép màu sinh sản tiếp tục bùng nổ: Nó mọc rễ và vươn lên thành một quần thể polyp mới tinh! Polyp này bắt đầu đâm chồi, phân nhánh như những cành cây nhỏ dưới đáy biển và nuôi dưỡng hàng chục, thậm chí hàng trăm chồi sứa non lơ lửng!". Bố cục: khối kén tròn cyst màu cam nhạt bám trên vỏ ốc rỗng kén tròn màu cam nhạt mọc rễ vươn nhánh lên thành quần thể thảm polyp san hô non nớt màu cam nhạt đâm chồi dưới đáy biển rực rỡ như cây san hô tí hon nuôi dưỡng hàng chục chồi sứa non. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi đến thời điểm thích hợp, từng chiếc chuông sứa con trong suốt tách mình ra khỏi cành polyp, bung nở xúc tu bơi vút lên mặt nước để bắt đầu một kiếp sống mới!". Bố cục: Từng chiếc chuông sứa con trong suốt tách mình ra khỏi polyp bay vút lên mặt nước; hàng trăm bản sao giống hệt sứa mẹ ban đầu.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy chú ý kỹ điều này: Từ một cá thể sứa già nua duy nhất ban đầu, nó không chỉ trẻ lại cho riêng mình, mà còn nhân bản ra hàng trăm bản sao giống hệt nhau về mặt di truyền!". Bố cục: Từ một chú sứa già nua duy nhất ban đầu nhân bản ra hàng trăm bản sao giống hệt nhau về mặt di truyền, xếp thành hàng dài lấp lánh. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giáo sư Shin Kubota tại Đại học Kyoto Nhật Bản đã dành hơn 15 năm cuộc đời để chăm sóc loài sứa này trong phòng thí nghiệm.". Bố cục: Giáo sư Shin Kubota tại Đại học Kyoto mỉm cười nâng niu bể nuôi sứa lặp lại chu kỳ đảo ngược lão hóa tới 12 lần liên tiếp. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ông đã chứng kiến một cá thể sứa lặp lại chu kỳ đảo ngược lão hóa này tới 12 lần liên tiếp mà sức sống vẫn tràn trề không hề suy giảm!". Bố cục: ông giáo sư già tóc bạc đeo kính lão cầm kính hiển vi ghi nhật ký quan sát một chú sứa lặp lại chu kỳ đảo ngược lão hóa 12 lần liên tiếp mà sức sống vẫn tràn trề. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Về mặt lý thuyết sinh học thuần túy, chu kỳ này có thể lặp đi lặp lại vô tận đến vĩnh hằng! Sinh Vật Bất Tử hoàn toàn miễn nhiễm trước cái chết vì tuổi già!". Bố cục: Vòng tròn vô cực biểu tượng bất tử: chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa bơi lượn trong chu kỳ tuần hoàn vĩnh cửu không bao giờ chết vì tuổi già.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi nhánh polyp dưới đáy biển giống như một nhà máy sản xuất sinh học tự động: khi nhiệt độ nước ấm lên vào mùa xuân, các chồi sứa bắt đầu nhấp nháy phát sáng rồi tách rời cuống bơi đi. Một chu trình tuần hoàn vĩnh cửu nối liền quá khứ và tương lai mà không bao giờ có điểm kết thúc!". Bố cục: Nhà máy sinh học tự động dưới đáy biển: các chồi sứa nhấp nháy phát sáng rồi bung nở xúc tu bơi đi đón mùa xuân; bảng Cấp độ 3 bật PASS. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bước vào hai cấp độ tối mật cuối cùng: Cấp độ 4 & 5 — Giải mã bản thiết kế hệ gen!". Bố cục: Bảng hồ sơ hiện CẤP ĐỘ 4 & 5: GIẢI MÃ BẢN THIẾT KẾ HỆ GEN; chuỗi xoắn kép ADN phát sáng rực rỡ trong phòng lab. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "2022, một công trình nghiên cứu chấn động thế giới đăng trên tạp chí danh giá PNAS do tiến sĩ Maria Pascual-Torner dẫn đầu đã giải trình tự toàn bộ bộ gen của Turritopsis dohrnii.". Bố cục: Bìa tạp chí PNAS năm 2022 mở ra bản đồ giải trình tự toàn bộ bộ gen của Turritopsis dohrnii do tiến sĩ Maria Pascual-Torner dẫn đầu. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kết quả phân tích đã hé lộ hai vũ khí phân tử vô giá: Thứ nhất là hệ thống bảo vệ telomere — đoạn mũ bảo vệ ở hai đầu sợi nhiễm sắc thể.". Bố cục: Cận cảnh phân tử: enzym telomerase gắn dài thêm đoạn mũ telomere ở đầu sợi nhiễm sắc thể, đồng hồ tuổi tác tế bào không bị điểm giờ chết. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở người, mỗi lần tế bào phân chia, telomere sẽ ngắn dần lại cho đến khi tế bào già nua và chết đi. Nhưng ở Sinh Vật Bất Tử, các enzym telomerase liên tục bảo dưỡng và kéo dài telomere, khiến đồng hồ tuổi tác của tế bào không bao giờ bị điểm giờ chết!". Bố cục: So sánh: ở người telomere ngắn dần mỗi lần tế bào phân chia; ở chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa enzym telomerase liên tục kéo dài telomere nên đồng hồ tuổi tác không bao giờ điểm giờ.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vũ khí thứ 2 là sự nhân đôi vượt trội của các gen liên quan đến sửa chữa ADN và chống oxy hóa. Cơ thể nó sở hữu số lượng bản sao gen sửa chữa lỗi sai sót phân tử nhiều gấp đôi so với các loài sứa thông thường!". Bố cục: Đội quân enzym phân tử tí hon cầm mỏ lết đi dọc chuỗi ADN sửa chữa lỗi sai sót và đột biến nhanh gấp đôi bình thường. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bất kỳ tổn hại hay đột biến nào phát sinh đều được các cỗ máy enzym quét sạch và khắc phục ngay lập tức!". Bố cục: Đội quân enzym tí hon quét sạch mọi tổn hại và đột biến phát sinh trên chuỗi ADN rồi khắc phục ngay lập tức. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học đã so sánh bộ gen của nó với người họ hàng gần là loài sứa Turritopsis rubra — một loài sứa có ngoại hình gần như giống hệt nhưng lại không thể đảo ngược vòng đời.". Bố cục: So sánh hai chuỗi gen: BÊN TRÁI loài sứa họ hàng không bất tử; BÊN PHẢI chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa sở hữu gần 1.000 gen đặc hữu tái sinh mở ra tương lai y học.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sự so sánh này đã chỉ ra chính xác gần 1.000 gen đặc hữu chịu trách nhiệm cho khả năng bất tử, mở ra chân trời mới cho ngành y học tái tạo và chống lão hóa của loài người!". Bố cục: Hai chuỗi gen đối chiếu nhau, hiện ra gần 1.000 gen đặc hữu chịu trách nhiệm cho khả năng bất tử, mở ra chân trời mới cho y học tái tạo. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuy nhiên, cần phải làm rõ một hiểu lầm phổ biến: Bất tử về mặt sinh học không có nghĩa là bất khả chiến bại trước mọi hiểm nguy! Trong môi trường đại dương tự nhiên đầy rẫy kẻ thù, Sinh Vật Bất Tử vẫn có thể bị rùa biển ăn thịt, bị cá voi nuốt chửng hoặc chết vì dịch bệnh nấm ký sinh.". Bố cục: Một con rùa biển khổng lồ há miệng đớp sứa: bất tử sinh học nhưng không bất khả chiến bại trước kẻ săn mồi. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng miễn là không bị nghiền nát thành tro bụi hay trở thành bữa ăn của kẻ khác, nó sẽ mãi mãi nắm giữ quyền năng quay ngược bánh xe thời gian để tái sinh!". Bố cục: chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa kiêu hãnh bơi lên giữa làn nước xanh thẳm, vương miện thời gian phát sáng trên đầu; bảng Cấp độ 4 & 5 bật PASS rực rỡ.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tổng kết hồ sơ phòng thí nghiệm số 29. Từ một giọt thạch trong suốt giữa đại dương bao la, Sinh Vật Bất Tử đã chứng minh cho nhân loại thấy rằng: giới hạn của sự sống là điều hoàn toàn có thể vượt qua, và tự nhiên luôn ẩn chứa những phép màu vượt xa trí tưởng tượng của con người!". Bố cục: Bàn tổng kết phòng thí nghiệm số 29: chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa đứng cạnh bản đồ giải mã gen bất tử với huy chương khoa học vàng óng.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hội đồng khoa học biểu quyết: Đạt điểm 10 xuất sắc cho cơ chế sinh học đảo ngược lão hóa vĩ đại nhất hành tinh! Ký tên: Viện trưởng phòng thí nghiệm sinh học cực hạn!". Bố cục: Dấu mộc đỏ ĐẠT ĐIỂM 10 đóng lên tập hồ sơ đảo ngược lão hóa; cả hội đồng khoa học vỗ tay chúc mừng.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn quý vị khán giả thì sao? Nếu loài người thực sự giải mã thành công hệ gen của sứa để có được năng lực bất tử: cứ già đi lại quay về tuổi 18 để sống lại một cuộc đời mới, bạn có muốn sở hữu món quà đó không?". Bố cục: Hai bàn cân lựa chọn: BÊN TRÁI biểu tượng bất tử quay về tuổi 18; BÊN PHẢI biểu tượng vòng đời hữu hạn quý giá, khán giả giơ thẻ bình chọn. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hay vòng đời hữu hạn mới chính là điều làm nên giá trị đẹp đẽ nhất của cuộc sống? Hãy chia sẻ suy nghĩ sâu sắc của bạn bên dưới phần bình luận nhé!". Bố cục: Cán cân suy ngẫm: một bên là bất tử quay về tuổi 18, một bên là vòng đời hữu hạn đẹp đẽ quý giá của cuộc sống. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cánh cửa phòng thí nghiệm số 29 xin được khép lại tại đây. Nhưng tập sau, chúng ta sẽ chuyển ống kính sang một chương trình truyền hình thực tế 24h nghẹt thở trên cạn!". Bố cục: Cánh cửa phòng lab số 29 khép lại, chuyển sang ống kính máy quay chương trình thực địa rừng ôn đới Bắc Mỹ. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chúng ta sẽ theo chân một kỹ sư xây dựng đại tài nhưng mắc chứng ám ảnh cưỡng chế cực kỳ lầy lội!". Bố cục: Một sinh vật bí ẩn được vẽ hoàn toàn bằng BÓNG ĐEN ĐẶC TUYỀN (solid black silhouette) hình chú chuột mập mạp béo ú có chiếc đuôi dẹp như mái chèo đang dùng hai chiếc răng cửa dài cắm vào thân cây gỗ lớn bên bờ suối; ba dấu hỏi chấm vàng to tướng; KHÔNG vẽ mắt mũi lông lá thật. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một sinh vật có bộ răng cửa màu cam chứa đầy kim loại sắt cứng hơn cả gỗ lim, suốt ngày đêm phát điên mỗi khi nghe tiếng nước chảy và sẵn sàng đắp bùn đất bịt kín cả chiếc loa phát nhạc để dựng nên những con đập làm thay đổi dòng chảy của cả một vùng sông ngòi!". Bố cục: Cũng chiếc BÓNG ĐEN ĐẶC TUYỀN đó đang vác từng tảng bùn đất đắp kín mít một chiếc loa phát thanh đang phát sóng âm nhạc róc rách; ba dấu hỏi chấm to tướng. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đố các bạn biết bóng đen bí ẩn kỳ sau là loài vật nào? Hãy đoán ngay ở phần bình luận nhé!". Bố cục: Chiếc BÓNG ĐEN ĐẶC TUYỀN kỹ sư đắp đập đứng cạnh con đập gỗ khổng lồ chặn dòng sông, mời gọi khán giả đoán tên Hải Ly tập sau. KHÔNG có chú sứa đeo kính bảo hộ trong cảnh này.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Một sinh vật già yếu cận kề cái chết bỗng nhiên tự biến ngược thành trẻ sơ sinh để sống lại từ đầu một cuộc đời mới!". Bố cục: Khung dọc: chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa từ một sinh vật già nua tự xoay ngược bánh xe thời gian biến ngược thành trẻ sơ sinh.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Xin giới thiệu Sứa Bất Tử, loài sinh vật bé nhỏ chỉ 4,5mm sống dưới đáy đại dương.". Bố cục: chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa bơi lơ lửng trong một giọt nước biển, chiếc thước đo mini hiện kích thước chỉ 4,5mm.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Khi bị đói, bị thương nặng hoặc già cỗi, nó không hề chết đi!". Bố cục: Sứa bị thương nặng và đói khát chìm xuống đáy biển nhưng không hề chết đi.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Thay vào đó, nó kích hoạt quá trình chuyển biệt hóa tế bào thần kỳ:". Bố cục: Đồ họa phân tử huỳnh quang: tế bào cơ bắp tự tẩy trắng danh tính biến ngược thành tế bào gốc phôi thai.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "toàn bộ tế bào cơ bắp và biểu bì tự tẩy trắng danh tính, quay trở lại thành tế bào gốc phôi thai!". Bố cục: Đồ họa phân tử khung dọc: toàn bộ tế bào cơ bắp và biểu bì của chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa tự trẻ hóa thành những tế bào mầm non nớt lấp lánh.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Khối cơ thể sứa chìm xuống đáy biển hóa thành búp polyp non nớt,". Bố cục: Khối thạch sứa chìm xuống đáy biển biến thành búp kén cyst non nớt màu cam bám vào vỏ ốc.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "rồi từ đó nhân bản ra hàng trăm chú sứa con mới tinh!". Bố cục: thảm polyp san hô non nớt màu cam nhạt đâm chồi dưới đáy biển đâm chồi nở rộ dưới đáy biển sinh ra hàng trăm bản sao sứa con bơi lên mặt nước.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Miễn là không bị kẻ thù ăn thịt, nó có thể lặp lại chu kỳ đảo ngược thời gian này mãi mãi,". Bố cục: Vòng tuần hoàn vô cực phát sáng ma thuật: chu kỳ đảo ngược lão hóa lặp đi lặp lại mãi mãi.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Sứa Bất Tử xanh ngọc trong suốt, dạ dày đỏ cam, kính bảo hộ tí hon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "trở thành sinh vật bất tử duy nhất trên hành tinh!". Bố cục: Chân dung chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa kiêu hãnh đội vương miện bất tử giữa đại dương sâu thẳm, ánh hào quang rực rỡ.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/50 của video YouTube về Sứa Bất Tử). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa. Nhân vật phụ cố định: ông giáo sư già tóc bạc đeo kính lão cầm kính hiển vi; thảm polyp san hô non nớt màu cam nhạt đâm chồi dưới đáy biển; khối kén tròn cyst màu cam nhạt bám trên vỏ ốc rỗng. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/9 của video YouTube Shorts về Sứa Bất Tử). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Sứa Bất Tử (Turritopsis dohrnii) hoạt hình màu xanh ngọc trong suốt lấp lánh, chiếc chuông sứa hình bán cầu căng tròn mềm mại, bên trong lộ rõ dạ dày màu đỏ cam ấm áp, xung quanh mép chuông xòe ra các xúc tu mảnh mai uốn lượn uyển chuyển, đeo một cặp kính bảo hộ phòng thí nghiệm tí hon trên đỉnh chuông sứa. Nhân vật phụ: thảm polyp san hô non nớt màu cam nhạt đâm chồi dưới đáy biển. 
```
</details>

## 7. SEO

- **title:** Sinh Vật Già Yếu Tự Biến Ngược Thành Sơ Sinh Để Bất Tử?!
- **hook_paragraph:** Sứa Bất Tử (Turritopsis dohrnii) nắm giữ bí mật đảo ngược lão hóa vĩ đại nhất tự nhiên: khi già yếu hoặc bị thương, toàn bộ tế bào cơ bắp tự chuyển hóa ngược thành tế bào gốc non nớt, hóa thành búp polyp để sinh ra hàng trăm bản sao mới!
- **question:** Nếu con người giải mã thành công hệ gen của sứa bất tử: cứ già lại biến về 18 tuổi để sống lại từ đầu, bạn có muốn bất tử không? Và đoán xem bóng đen tập sau là loài nào?
- **next_teaser:** Bóng đen kỹ sư đại tài: sở hữu răng cửa màu cam chứa sắt cực cứng, bị ám ảnh tiếng nước chảy đắp bùn kín loa phát nhạc!
- **shorts_title:** Sinh Vật Tự Biến Ngược Về Sơ Sinh Để Bất Tử?! 🪼 #độngvật #sứabấttử
- **shorts_desc:** Sứa Bất Tử Turritopsis dohrnii khi già yếu tự chuyển hóa tế bào ngược về phôi thai sơ sinh để sống lại từ đầu! Khám phá sinh vật bất tử duy nhất hành tinh.
- **bullets:** Phòng lab 5 cấp độ: Bí ẩn phá vỡ quy luật nhiệt động lực học không thể đảo ngược · Cơ chế Transdifferentiation: Tế bào cơ bắp tự biến ngược thành tế bào gốc phôi thai · Tái sinh đáy biển: Hóa thành kén cyst đâm chồi polyp nhân bản hàng trăm cá thể mới · Bản thiết kế gen PNAS 2022: Telomere không bao giờ co ngắn và nhân đôi gen sửa ADN
- **tags:** sứa bất tử, sua bat tu, turritopsis dohrnii, immortal jellyfish, sinh vật bất tử, đảo ngược lão hóa, động vật kỳ lạ, thế giới động vật, động vật hài hước, vẽ chuyện hoang dã, whiteboard animation, khoa học thú vị
- **hashtags:** #độngvật #sứabấttử #VẽChuyệnHoangDã

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-29-sua-bat-tu
python src/episode/pipeline.py tts    projects/tap-29-sua-bat-tu     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-29-sua-bat-tu     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-29-sua-bat-tu     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-29-sua-bat-tu              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-29-sua-bat-tu --force
python scripts/beat_sheet.py projects/tap-29-sua-bat-tu               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-29-sua-bat-tu/audio/shorts.wav projects/tap-29-sua-bat-tu/renders/tap-29-sua-bat-tu_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-29-sua-bat-tu
python src/episode/pipeline.py seo    projects/tap-29-sua-bat-tu
python src/episode/episode_doc.py     projects/tap-29-sua-bat-tu
```

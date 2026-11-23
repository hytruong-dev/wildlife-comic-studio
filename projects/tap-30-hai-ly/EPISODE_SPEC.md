# TẬP 30 — HẢI LY · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-30-hai-ly`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-30-hai-ly`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F4` · **Persona giọng:** `phong_vien_24h` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Hải Ly |
| Tiêu đề YouTube | Đặt Loa Phát Tiếng Nước Chảy Trước Mặt Hải Ly Và Cái Kết?! |
| Video dài | `renders/tap-30-hai-ly_long.mp4` — 8:44.7 (524.7s) |
| Shorts | `renders/tap-30-hai-ly_shorts.mp4` — 0:50.1 (50.1s) |
| Thumbnail | `renders/tap-30-hai-ly_thumbnail.jpg` |
| Số hình | dài 50 beat / 50 ảnh riêng; Shorts 11 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/50 của video YouTube về Hải Ly). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu. Nhân vật phụ cố định: phóng viên hiện trường cầm mic có logo 24H; con chó sói xám hung dữ đứng bên bờ hồ rình mò; con đập gỗ khổng lồ đan cành cây và trát bùn đất bắc ngang dòng sông. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — 00 SÁNG: BẮT ĐẦU CA TRỰC 24H THỰC ĐỊA THEO CHÂN KIẾN TRÚC SƯ ĐẠI TÀI
*Badge:* `06:00 SÁNG: XUẤT PHÁT` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene01_p0.wav` (337 ký tự) · mood `hao_hung`

```text
Alo alo, xin chào toàn thể quý vị khán giả của chương trình thực địa hai mươi tư giờ! Tôi đang có mặt tại một cánh rừng rậm rạp thuộc vùng hoang dã Bắc Mỹ, nơi sương sớm còn đang giăng kín mặt hồ phẳng lặng. Hôm nay, chiếc camera giấu kín của chúng ta sẽ bám sát từng bước chân của một kỹ sư xây dựng thiên tài nhưng cũng cực kỳ lầy lội!
```
**Part 1** → `audio/vs/scene01_p1.wav` (133 ký tự) · 🎭 cameo `co_tro_ly`

```text
Báo cáo phóng viên, mục tiêu số ba mươi đã xuất hiện từ bờ suối, đang lạch bạch vác theo một khúc gỗ nặng gấp đôi trọng lượng cơ thể!
```
**Part 2** → `audio/vs/scene01_p2.wav` (264 ký tự) · mood `don_dap`

```text
[surprise-oh] Hướng máy quay sang góc chín giờ ngay lập tức! [laughter] Xin giới thiệu với toàn thể anh em: đây là Hải Ly, thuộc chi Castor, loài gặm nhấm lớn thứ hai trên Trái Đất và là nhân vật duy nhất trong giới động vật có chứng chỉ hành nghề: Kỹ Sư Đập Nước!
```
**Part 3** → `audio/vs/scene01_p3.wav` (339 ký tự) · mood `hao_hung`

```text
Nhìn dáng đi trên cạn của gã thì vụng về buồn cười vô cùng: thân hình mập mạp béo ú nặng tới ba mươi cân, bốn chân ngắn củn và chiếc đuôi dẹt phẳng lì hình mái chèo kéo lê lết trên mặt đất. Nhưng chỉ cần chạm vào làn nước mát, gã lập tức biến thành một thợ lặn cừ khôi với đôi chân màng bơi thoăn thoắt và bộ lông chống thấm nước hoàn hảo!
```
**Part 4** → `audio/vs/scene01_p4.wav` (300 ký tự) · mood `don_dap`

```text
Và điều điên rồ nhất sắp diễn ra trong hai mươi tư giờ tới: Chúng ta sẽ chứng kiến cách một chú chuột khổng lồ dùng chính hàm răng của mình để đốn ngã cả một cánh rừng, tự tay xây nên những công trình vĩ đại có thể nhìn thấy rõ mồn một từ vệ tinh không gian ngoài Trái Đất! Bắt đầu đồng hồ đếm ngược!
```
**Part 5** → `audio/vs/scene01_p5.wav` (348 ký tự) · mood `am_ap`

```text
Trước khi gã bước vào ca làm việc chính thức, hãy chú ý chiếc đuôi vảy da dẹt hình mái chèo độc đáo: Đây không chỉ là bánh lái khi bơi lội dưới dòng nước xiết, mà còn là chiếc còi báo động khẩn cấp. Mỗi khi phát hiện nguy hiểm, gã đập mạnh chiếc đuôi xuống mặt nước tạo tiếng nổ chan chát vang xa hàng trăm mét để báo động cho cả gia đình lặn trốn!
```

### scene02 — 00 SÁNG: CẬN CẢNH CỖ MÁY ĐỐN CÂY BẰNG BỘ RĂNG CỬA BỌC SẮT MÀU CAM
*Thẻ chương:* BỘ RĂNG MÀU CAM CHỨA ĐẦY OXIT SẮT CHÉM NGỌT CÂY GỖ CỔ THỤ

*Badge:* `09:00 SÁNG: CỖ MÁY ĐỐN GỖ` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene02_p0.wav` (292 ký tự) · mood `tram_bi_an`

```text
Đồng hồ điểm chín giờ sáng! Chúng ta đang áp sát hiện trường khai thác gỗ của Kỹ Sư Đập Nước. Hãy nhìn thẳng vào cận cảnh khuôn mặt của gã: Hai chiếc răng cửa hàm trên dài ngoằng nhô ra ngoài không phải màu trắng ngà như bình thường, mà lại có màu cam đậm rực rỡ như vừa mới nhúng vào gỉ sắt!
```
**Part 1** → `audio/vs/scene02_p1.wav` (361 ký tự) · mood `don_dap`

```text
Năm hai ngàn không trăm mười lăm, một nghiên cứu đột phá trên tạp chí Science đã hé lộ bí mật chấn động: Lớp men phía trước răng của hải ly không phải chỉ có canxi, mà chứa đầy các tinh thể oxit sắt vô định hình siêu cứng! Lớp kim loại tự nhiên này giúp răng của nó cứng hơn bất kỳ loài gặm nhấm nào trên hành tinh và kháng axit mài mòn tuyệt đối! [surprise-wa]
```
**Part 2** → `audio/vs/scene02_p2.wav` (253 ký tự) · mood `hao_hung`

```text
Chưa dừng lại ở đó, mặt trước của răng cứng như thép trong khi mặt sau lại mềm hơn. Khi hải ly gặm gỗ, lớp mặt sau mòn nhanh hơn mặt trước, khiến đầu răng luôn tự động mài sắc bén như một chiếc lưỡi đục kim cương! Càng gặm nhiều, răng lại càng sắc ngọt!
```
**Part 3** → `audio/vs/scene02_p3.wav` (276 ký tự) · mood `don_dap`

```text
Hãy bấm giờ đếm ngược xem: Một thân cây bạch dương đường kính mười lăm centimet cứng cáp... gã chỉ cần đúng ba mươi phút gặm vòng quanh gốc cây là cả thân cây gỗ cổ thụ to lớn đổ rầm xuống mặt đất! Tiếng gặm cộp cộp vang vọng khắp góc rừng như một xưởng cưa máy chạy bằng cơm!
```
**Part 4** → `audio/vs/scene02_p4.wav` (318 ký tự) · mood `hao_hung`

```text
Và điều kỳ diệu về giải phẫu miệng: Phía sau hai chiếc răng cửa là một màng da đặc biệt có thể khép kín miệng lại, cho phép gã vừa gặm gỗ vừa ngụp lặn dưới nước mà không sợ dăm gỗ hay nước tràn vào cổ họng! Người bản địa Bắc Mỹ thời xưa thậm chí từng lấy hàm răng hải ly gắn vào cán gỗ để làm dao đục khắc gỗ siêu bền!
```
**Part 5** → `audio/vs/scene02_p5.wav` (321 ký tự) · mood `hao_hung`

```text
Chưa hết, gã kỹ sư này còn sở hữu một túi tuyến xạ hương đặc biệt dưới đuôi tiết ra chất ca-xtô-ri-um thơm nồng mùi vani ngọt ngào! Gã thường đắp những gò bùn nhỏ dọc bờ suối rồi phun xạ hương lên đó để đóng dấu chủ quyền lãnh thổ, một mùi hương quyến rũ đến mức ngành công nghiệp nước hoa cổ điển từng săn lùng ráo riết!
```
**Part 6** → `audio/vs/scene02_p6.wav` (222 ký tự) · mood `nghiem_trang_gia`

```text
Và răng của hải ly mọc liên tục suốt cả cuộc đời! Nếu không chịu khó gặm gỗ mỗi ngày, chiếc răng thép này sẽ dài ra chọc thủng hộp sọ. Gặm cây không chỉ là đam mê xây dựng, mà là mệnh lệnh sinh tồn bắt buộc của giống loài!
```

### scene03 — 00 CHIỀU: THÍ NGHIỆM KINH ĐIỂN VỚI CHIẾC LOA PHÁT TIẾNG NƯỚC CHẢY
*Thẻ chương:* PHÁT ĐIÊN VÌ TIẾNG NƯỚC CHẢY ĐẮP BÙN BỊT KÍN CẢ LOA PHÁT NHẠC

*Badge:* `14:00 CHIỀU: CƠN PHÁT ĐIÊN` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene03_p0.wav` (301 ký tự) · mood `tram_bi_an`

```text
Mười bốn giờ chiều: Đến lúc đội phóng sự chúng tôi thực hiện bài kiểm tra tâm lý lầy lội nhất! Các nhà sinh học từng thắc mắc: Động lực nào thôi thúc Kỹ Sư Đập Nước làm việc quần quật suốt ngày đêm không ngừng nghỉ? Có phải nó nhìn thấy dòng nước chảy xiết nên muốn ngăn lại? Câu trả lời là: Không hề!
```
**Part 1** → `audio/vs/scene03_p1.wav` (262 ký tự) · mood `hao_hung`

```text
Thứ khiến hải ly phát điên không phải là thị giác, mà chính là âm thanh của tiếng nước chảy róc rách! Trong một thí nghiệm kinh điển của nhà khoa học Wilson, người ta đặt một chiếc loa phát thanh trên nền đất khô ráo giữa rừng và bật tiếng nước róc rách thật to.
```
**Part 2** → `audio/vs/scene03_p2.wav` (150 ký tự) · 🎭 cameo `co_tro_ly`

```text
Báo cáo hiện trường: Hải Ly vừa nghe thấy tiếng loa đã lập tức vứt bỏ mọi việc, đôi mắt đỏ ngầu hoảng hốt lao ngay ra suối khuân bùn đất chạy lên cạn!
```
**Part 3** → `audio/vs/scene03_p3.wav` (299 ký tự) · mood `hao_hung`

```text
[laughter] Quý vị hãy nhìn xem: Gã hì hục tha cành cây, vốc từng nắm bùn đất trát kín mít xung quanh chiếc loa phát thanh cho đến khi âm thanh róc rách bị dập tắt hoàn toàn thì mới thở phào nhẹ nhõm! Dù dưới chân là đất khô ráo không có lấy một giọt nước, gã vẫn đắp thành một ngọn đồi bùn khổng lồ!
```
**Part 4** → `audio/vs/scene03_p4.wav` (347 ký tự) · mood `hao_hung`

```text
Thậm chí khi các nhà nghiên cứu treo chiếc loa lơ lửng trên cành cây cách mặt đất cả mét, chú hải ly vẫn kiên nhẫn khuân đất đắp cao dần quanh thân cây thành một chiếc cầu thang bùn kiên cố để trèo lên bịt chặt chiếc loa phát thanh! Sự kiên trì và độ lầy lội đỉnh cao của gã kiến trúc sư này khiến toàn bộ các nhà khoa học phải phì cười thán phục!
```
**Part 5** → `audio/vs/scene03_p5.wav` (222 ký tự) · mood `don_dap`

```text
Đây chính là chứng ám ảnh cưỡng chế bẩm sinh kỳ quặc nhất tự nhiên: Đối với Kỹ Sư Đập Nước, tiếng nước chảy rò rỉ là một tội ác không thể tha thứ! Ở đâu có tiếng nước róc rách, ở đó phải được trát bùn bọc kín ngay lập tức!
```

### scene04 — 00 TỐI: CÔNG TRƯỜNG XÂY ĐẬP VĨ ĐẠI CHẶN ĐỨNG DÒNG SÔNG
*Thẻ chương:* ĐAN CÀNH CÂY VÀ TRÁT BÙN TẠO CON ĐẬP DÀI 850M NHÌN THẤY TỪ VŨ TRỤ

*Badge:* `18:00 TỐI: ĐẠI CÔNG TRƯỜNG` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene04_p0.wav` (203 ký tự) · mood `hao_hung`

```text
Hoàng hôn buông xuống lúc mười tám giờ: Đại công trường xây dựng chính thức bước vào giờ cao điểm! Cả gia đình hải ly gồm bố mẹ và các con bắt đầu phối hợp nhịp nhàng như một đội ngũ công nhân lành nghề.
```
**Part 1** → `audio/vs/scene04_p1.wav` (286 ký tự) · mood `hao_hung`

```text
Chúng kéo những thân cây lớn cắm sâu xuống đáy bùn tạo khung dầm chữ V ngược chịu lực, sau đó đan xen những cành cây nhỏ hơn vào giữa như đan phên liếp. Cuối cùng, chiếc đuôi dẹp như mái chèo được sử dụng như một chiếc bay thợ nề: múc bùn non, đá cuội và lá cây đầm chặt vào từng kẽ hở!
```
**Part 2** → `audio/vs/scene04_p2.wav` (301 ký tự) · mood `don_dap`

```text
Để vận chuyển những khúc gỗ nặng hàng trăm cân từ sâu trong rừng ra bờ suối mà không tốn sức, chúng còn tự đào những con kênh dẫn nước dài hàng trăm mét len lỏi qua các bụi cây! Gỗ đốn hạ xong chỉ việc thả trôi nổi trên kênh đào về thẳng công trường xây dựng! Một tư duy logistics vượt trước thời đại!
```
**Part 3** → `audio/vs/scene04_p3.wav` (279 ký tự) · mood `am_ap`

```text
Công trình này kiên cố đến mức áp lực nước cuồn cuộn không tài nào cuốn trôi nổi! Nước sông bị chặn lại dâng cao dần, biến cả một thung lũng khô cằn thành một hồ nước rộng mênh mông, tạo nên một vùng đất ngập nước trù phú cho hàng ngàn loài cá, chim và ếch nhái kéo về sinh sống!
```
**Part 4** → `audio/vs/scene04_p4.wav` (353 ký tự) · mood `don_dap`

```text
Tại Vườn quốc gia Wood Buffalo ở Canada, các nhà khoa học đã phát hiện một con đập do các thế hệ Kỹ Sư Đập Nước kiên trì xây dựng suốt hàng chục năm: Con đập dài tới tám trăm năm mươi mét — gấp đôi chiều dài của đập thủy điện Hoover do con người xây — và là công trình động vật duy nhất nhìn thấy rõ mồn một từ ảnh chụp vệ tinh không gian! [surprise-wa]
```
**Part 5** → `audio/vs/scene04_p5.wav` (305 ký tự) · mood `am_ap`

```text
Ngày nay, các nhà bảo tồn thiên nhiên trên khắp thế giới đang tích cực tái thả hải ly về các vùng hoang dã. Những con đập của chúng giúp nâng cao mạch nước ngầm, ngăn chặn thảm họa cháy rừng, thanh lọc các chất ô nhiễm độc hại và hồi sinh những dòng sông chết mà không tốn lấy một đồng ngân sách xây dựng!
```
**Part 6** → `audio/vs/scene04_p6.wav` (176 ký tự) · mood `hao_hung`

```text
Một sinh vật không có bằng kỹ sư, không có máy móc hiện đại, nhưng lại có thể tự tay vẽ lại bản đồ thủy văn của cả một lục địa! Thật là một kỳ quan kiến trúc không thể tin nổi!
```

### scene05 — 00 ĐÊM: PHÁO ĐÀI LÂU ĐÀI LODGE GIỮA HỒ VỚI CỬA VÀO NGẬP DƯỚI NƯỚC
*Thẻ chương:* LÂU ĐÀI HAI TẦNG GIỮA HỒ NƯỚC CỬA VÀO NGẬP SÂU TRÁNH THÚ DỮ

*Badge:* `23:00 ĐÊM: PHÁO ĐÀI NGẦM` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene05_p0.wav` (253 ký tự) · mood `tram_bi_an`

```text
Đồng hồ điểm hai mươi ba giờ đêm! Nhiệt độ ngoài trời giảm xuống buốt giá, tiếng chó sói hú vang vọng từ bìa rừng săn tìm con mồi. Nhưng gia đình hải ly thì đã rút lui an toàn vào bên trong lâu đài kiên cố mang tên lodge nằm sừng sững giữa lòng hồ nước!
```
**Part 1** → `audio/vs/scene05_p1.wav` (245 ký tự) · mood `hao_hung`

```text
Hãy quan sát mặt cắt kiến trúc tinh xảo của chiếc lâu đài này: Nó được đắp bằng hàng ngàn khúc gỗ và bùn đất dày tới một mét, mùa đông bùn đông cứng lại như bê tông cốt thép, móng vuốt của gấu hay sói cào rách móng cũng không tài nào phá vỡ nổi!
```
**Part 2** → `audio/vs/scene05_p2.wav` (281 ký tự) · mood `don_dap`

```text
Và điều thiên tài nhất nằm ở hệ thống cửa ra vào: Tuyệt đối không có bất kỳ cánh cửa nào mở trên cạn! Lối vào duy nhất là hai đường hầm ngầm nằm sâu dưới mặt nước! Kẻ săn mồi trên cạn muốn đột nhập thì phải biết lặn sâu nín thở, điều mà chó sói và linh miêu không bao giờ làm được!
```
**Part 3** → `audio/vs/scene05_p3.wav` (298 ký tự) · mood `am_ap`

```text
Bên trong lâu đài được chia làm hai tầng khô ráo: Tầng dưới là phòng thay đồ để rũ sạch nước trên lông, còn tầng trên là phòng ngủ ấm cúng lót bằng vỏ cây khô êm ái, nơi cả gia đình quây quần sưởi ấm cho nhau. Đỉnh chóp lâu đài còn chừa lại một khe thông gió thông minh để đón không khí trong lành!
```
**Part 4** → `audio/vs/scene05_p4.wav` (350 ký tự) · mood `hao_hung`

```text
Vào mùa đông băng giá khi mặt hồ đóng băng dày cả mét, gia đình hải ly vẫn sống ung dung sung túc nhờ một kho lương thực bí mật: Trước mùa đông, chúng cắm hàng ngàn cành cây bạch dương tươi ngon găm sâu xuống đáy bùn dưới lòng hồ. Dưới lớp băng dày, chúng chỉ việc bơi ra tủ lạnh đáy nước lấy cành cây về thưởng thức mà không cần ló đầu lên mặt băng!
```
**Part 5** → `audio/vs/scene05_p5.wav` (182 ký tự) · mood `hao_hung`

```text
Một công trình phòng thủ toàn diện chuẩn năm sao: vừa có hồ nước bảo vệ, vừa có cửa hầm bí mật, vừa có hệ thống sưởi ấm và thông gió tự nhiên! Đúng là đỉnh cao trí tuệ loài gặm nhấm!
```

### scene06 — 00 SÁNG HÔM SAU: KẾT THÚC CA TRỰC VÀ HÉ LỘ BÓNG ĐEN TÊN LỬA 389 KM/H
*Thẻ chương:* TỔNG KẾT 24H VÀ BÓNG ĐEN TÊN LỬA SỐNG CHIM CẮT TẬP 31

*Badge:* `06:00 SÁNG: KẾT THÚC 24H` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene06_p0.wav` (289 ký tự) · mood `am_ap`

```text
Đồng hồ điểm sáu giờ sáng hôm sau: Ca trực thực địa hai mươi tư giờ chính thức khép lại! Ánh bình minh rực rỡ chiếu rọi xuống mặt hồ nước phẳng lặng do chính bàn tay Kỹ Sư Đập Nước tạo nên. Một đêm lao động cật lực, một hồ nước mới ra đời và sự sống lại sinh sôi nảy nở khắp cánh rừng già!
```
**Part 1** → `audio/vs/scene06_p1.wav` (179 ký tự) · mood `hao_hung`

```text
Báo cáo thực địa hai mươi tư giờ: Đạt điểm mười xuất sắc cho danh hiệu Kiến trúc sư vĩ đại nhất giới động vật! Ký tên: Phóng viên thực địa chương trình hai mươi tư giờ! [laughter]
```
**Part 2** → `audio/vs/scene06_p2.wav` (245 ký tự) · mood `hao_hung`

```text
Còn anh em thì sao? Nếu được sở hữu bộ răng cửa bọc sắt không bao giờ mòn của hải ly, hay năng lực xây nên cả một kỳ quan thiên nhiên thay đổi cảnh quan Trái Đất, anh em sẽ chọn siêu năng lực nào? Hãy để lại bình luận chia sẻ cùng chúng tôi nhé!
```
**Part 3** → `audio/vs/scene06_p3.wav` (506 ký tự) · mood `don_dap`

```text
Ca trực thực địa tập ba mươi xin được đóng máy tại đây. Nhưng tập sau, chúng ta sẽ chuyển thẳng tới một xưởng vũ khí khí động học đỉnh cao trên bầu trời để giải mã một sát thủ tốc độ kinh hoàng nhất lịch sử hành tinh! Một cỗ tên lửa sống có thể bổ nhào từ tầng mây với vận tốc kinh hoàng lên tới ba trăm tám mươi chín kilômét trên giờ mà không hề bị nổ tung lồng ngực nhờ hai chiếc nón giảm áp thần kỳ trong lỗ mũi! Đố các bạn biết bóng đen bí ẩn kỳ sau là loài vật nào? Hãy đoán ngay ở phần bình luận nhé!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Điều gì sẽ xảy ra nếu bạn đặt một chiếc loa phát tiếng nước chảy trước mặt Hải Ly? [laughter] Ngay lập tức, gã kỹ sư đập nước này sẽ phát điên cuồng loạn, vác bùn đất chạy hộc tốc lên cạn để trát kín mít chiếc loa cho đến khi tiếng nước róc rách tắt ngấm! [surprise-wa] Hải Ly mắc chứng ám ảnh cưỡng chế bẩm sinh với âm thanh nước rò rỉ. Thậm chí khi các nhà khoa học treo chiếc loa lơ lửng trên cành cây, gã còn kiên nhẫn đắp cả chiếc cầu thang bùn để trèo lên bịt chặt cho bằng được, vì với gã tiếng nước rò rỉ là một tội ác không thể tha thứ! Để phục vụ đam mê đắp đập, nó trang bị bộ răng cửa màu cam chứa đầy oxit sắt cứng như kim loại thép, có khả năng tự mài sắc để đốn hạ thân cây to chỉ trong ba mươi phút! Những con đập do nó xây dựng có thể dài tới tám trăm năm mươi mét, chặn đứng dòng sông và nhìn thấy rõ mồn một từ vệ tinh không gian! Đúng là kỹ sư xây dựng cuồng nhiệt và lầy lội nhất thế giới động vật!
```

**Whisper prompt:** `Hải Ly, Kỹ Sư Đập Nước, Castor canadensis, Castor fiber, răng cửa oxit sắt, đập hải ly, lodge, lâu đài ngầm, tiếng nước chảy, loa phát nhạc, 24h, 850m, 389 km/h, Chim Cắt Lớn, 100%, Bắc Mỹ, 2015, 30kg, 15cm, 30 phút`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| ba mươi | 30 |
| ba mươi mốt | 31 |
| hai mươi tư giờ | 24h |
| hai mươi tư | 24 |
| sáu giờ | 6h |
| chín giờ | 9h |
| mười bốn giờ | 14h |
| Mười bốn giờ | 14h |
| mười bốn | 14 |
| Mười bốn | 14 |
| mười lăm centimet | 15cm |
| mười lăm | 15 |
| mười tám giờ | 18h |
| hai mươi ba giờ | 23h |
| ba mươi cân | 30kg |
| tám trăm năm mươi mét | 850m |
| tám trăm | 800 |
| hàng trăm | hàng trăm |
| hàng ngàn | hàng ngàn |
| hàng triệu | hàng triệu |
| hàng chục | hàng chục |
| một giây | 1 giây |
| ba mươi giây | 30 giây |
| ba mươi phút | 30 phút |
| bốn mươi centimet | 40cm |
| ba mươi centimet | 30cm |
| một mét | 1m |
| một trăm phần trăm | 100% |
| điểm mười | điểm 10 |
| Bắc Mỹ | Bắc Mỹ |
| Canada | Canada |
| Năm hai ngàn không trăm mười lăm | 2015 |
| năm hai ngàn không trăm mười lăm | 2015 |
| ba trăm tám mươi chín kilômét trên giờ | 389 km/h |
| bốn trăm kilômét trên giờ | 400 km/h |
| Chim Cắt Lớn | Chim Cắt Lớn |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · 00 SÁNG: BẮT ĐẦU CA TRỰC 24H THỰC ĐỊA THEO CHÂN KIẾN TRÚC SƯ ĐẠI TÀI · 85.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.7 (10.7s) | L01 | Alo alo, xin chào toàn thể quý vị khán giả của chương trình thực địa 24h! Tôi đang có mặt tại một cánh rừng rậm rạp thuộc vùng hoang dã Bắc Mỹ, nơi sương sớm còn đang giăng kín mặt hồ phẳng lặng. |  | Cánh rừng ôn đới rậm rạp hoang dã Bắc Mỹ với sương sớm giăng mờ ảo trên mặt hồ phẳng lặng, chiếc đồng hồ đếm ngược 24H nhấp nháy góc màn hình. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này. |
| b02 | 00:10.7–00:17.3 (6.6s) | L02 | Hôm nay, chiếc camera giấu kín của chúng ta sẽ bám sát từng bước chân của một kỹ sư xây dựng thiên tài nhưng cũng cực kỳ lầy lội! |  | Chiếc camera giấu kín trong bụi cây rình sẵn bám sát từng bước chân của một kỹ sư xây dựng thiên tài nhưng cực kỳ lầy lội, ống kính phản chiếu mặt hồ sương sớm. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này. |
| b03 | 00:17.3–00:24.7 (7.4s) | L03 | Báo cáo phóng viên, mục tiêu số 30 đã xuất hiện từ bờ suối, đang lạch bạch vác theo một khúc gỗ nặng gấp đôi trọng lượng cơ thể! |  | BÊN TRÁI nữ trợ lý cầm bộ đàm chỉ tay về phía bờ suối; BÊN PHẢI phóng viên hiện trường cầm mic có logo 24H cầm mic hướng máy quay vào mục tiêu. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này. |
| b04 | 00:24.7–00:36.6 (11.9s) | L04 | Hướng máy quay sang góc 9h ngay lập tức! Xin giới thiệu với toàn thể anh em: đây là Hải Ly, thuộc chi Castor, loài gặm nhấm lớn thứ hai trên Trái Đất và là nhân vật duy nhất trong giới động vật có chứng chỉ hành nghề: Kỹ Sư Đập Nước! |  | Ở GIỮA chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu mũm mĩm đáng yêu đội chiếc mũ bảo hộ kỹ sư màu vàng tươi, hai chân trước ôm khúc gỗ to tướng bước đi lạch bạch. |
| b05 | 00:36.6–00:46.7 (10.1s) | L05 | Nhìn dáng đi trên cạn của gã thì vụng về buồn cười vô cùng: thân hình mập mạp béo ú nặng tới 30kg, bốn chân ngắn củn và chiếc đuôi dẹt phẳng lì hình mái chèo kéo lê lết trên mặt đất. | **NẶNG 30KG** · chuột khổng lồ · L/350 · [0.35, 0.45] | Chia đôi: BÊN TRÁI chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu đi lạch bạch vụng về trên bờ suối nặng 30kg; BÊN PHẢI chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng |
| b06 | 00:46.7–00:53.9 (7.2s) | L06 | Nhưng chỉ cần chạm vào làn nước mát, gã lập tức biến thành một thợ lặn cừ khôi với đôi chân màng bơi thoăn thoắt và bộ lông chống thấm nước hoàn |  | chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu lao xuống làn nước mát, biến thành thợ lặn cừ khôi với đôi chân màng bơi thoăn thoắt và bộ lông chống thấm nước hoàn hảo. |
| b07 | 00:53.9–01:08.6 (14.7s) | L07 | hảo! Và điều điên rồ nhất sắp diễn ra trong 24h tới: Chúng ta sẽ chứng kiến cách một chú chuột khổng lồ dùng chính hàm răng của mình để đốn ngã cả một cánh rừng, tự tay xây nên những công trình vĩ đại có thể nhìn thấy rõ mồn một từ vệ tinh không gian ngoài Trái Đất! Bắt đầu đồng hồ đếm ngược! |  | Hình ảnh bản đồ chụp từ vệ tinh không gian ngoài Trái Đất: các công trình đập nước vĩ đại của loài hải ly hiện rõ mồn một giữa lục địa. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này. |
| b08 | 01:08.6–01:18.4 (9.8s) | L08 | Trước khi gã bước vào ca làm việc chính thức, hãy chú ý chiếc đuôi vảy da dẹt hình mái chèo độc đáo: Đây không chỉ là bánh lái khi bơi lội dưới dòng nước xiết, mà còn là chiếc còi báo động khẩn cấp. |  | chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu đập mạnh chiếc đuôi dẹp như mái chèo xuống mặt nước bắn tung tóe bọt trắng xóa, phát ra tiếng nổ chan chát vang xa hàng trăm mét. |
| b09 | 01:18.4–01:25.4 (7.0s) | L09 | Mỗi khi phát hiện nguy hiểm, gã đập mạnh chiếc đuôi xuống mặt nước tạo tiếng nổ chan chát vang xa hàng trăm mét để báo động cho cả gia đình lặn trốn! |  | chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu đập mạnh chiếc đuôi xuống mặt nước tạo tiếng nổ chan chát vang xa hàng trăm mét báo động cho cả gia đình lặn trốn. |

### scene02 · 00 SÁNG: CẬN CẢNH CỖ MÁY ĐỐN CÂY BẰNG BỘ RĂNG CỬA BỌC SẮT MÀU CAM · 101.8s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:15.0 (15.0s) | L10 | Đồng hồ điểm 9h sáng! Chúng ta đang áp sát hiện trường khai thác gỗ của Kỹ Sư Đập Nước. Hãy nhìn thẳng vào cận cảnh khuôn mặt của gã: Hai chiếc răng cửa hàm trên dài ngoằng nhô ra ngoài không phải màu trắng ngà như bình thường, mà lại có màu cam đậm rực rỡ như vừa mới nhúng vào gỉ sắt! | **09:00 SÁNG** · hiện trường đốn gỗ · L/350 · [0.35, 0.45] | Đồng hồ hiện 9H SÁNG; cận cảnh khuôn mặt chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu khoe hai chiếc răng cửa hàm trên màu cam đậm rực rỡ bóng loáng như kim loại sắt. |
| b02 | 00:15.0–00:25.5 (10.5s) | L11 | 2015, một nghiên cứu đột phá trên tạp chí Science đã hé lộ bí mật chấn động: Lớp men phía trước răng của hải ly không phải chỉ có canxi, mà chứa đầy các tinh thể oxit sắt vô định hình siêu cứng! | **NĂM 2015** · men răng oxit sắt · R/350 · [0.65, 0.45] | Bìa tạp chí Science năm 2015 mở ra phân tích cấu trúc nano: các tinh thể oxit sắt vô định hình siêu cứng gắn chặt trong men răng hải ly. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này. |
| b03 | 00:25.5–00:31.6 (6.1s) | L12 | Lớp kim loại tự nhiên này giúp răng của nó cứng hơn bất kỳ loài gặm nhấm nào trên hành tinh và kháng axit mài mòn tuyệt đối! |  | Hai chiếc răng cửa cam bóng loáng cứng hơn bất kỳ loài gặm nhấm nào, kháng axit mài mòn tuyệt đối, tỏa sáng như kim loại thép. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này. |
| b04 | 00:31.6–00:44.8 (13.3s) | L13 | Chưa dừng lại ở đó, mặt trước của răng cứng như thép trong khi mặt sau lại mềm hơn. Khi hải ly gặm gỗ, lớp mặt sau mòn nhanh hơn mặt trước, khiến đầu răng luôn tự động mài sắc bén như một chiếc lưỡi đục kim cương! Càng gặm nhiều, răng lại càng sắc ngọt! |  | Sơ đồ vát nhọn 20 độ của răng cửa: mặt sau mềm mòn nhanh hơn mặt trước cứng, đầu răng tự động mài sắc ngọt như lưỡi đục kim cương. |
| b05 | 00:44.8–00:57.9 (13.1s) | L14 | Hãy bấm giờ đếm ngược xem: Một thân cây bạch dương đường kính 15cm cứng cáp... gã chỉ cần đúng 30 phút gặm vòng quanh gốc cây là cả thân cây gỗ cổ thụ to lớn đổ rầm xuống mặt đất! Tiếng gặm cộp cộp vang vọng khắp góc rừng như một xưởng cưa máy chạy bằng cơm! | **GỐC 15CM** · thân cây bạch dương · L/350 · [0.35, 0.45]<br>**30 PHÚT** · đốn ngã cây to · R/350 · [0.65, 0.45] | Chiếc đồng hồ bấm giờ 30 phút: chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu gặm vòng quanh gốc cây bạch dương 15cm làm cả thân cây to lớn đổ rầm xuống đất; dăm gỗ bay rào rào. |
| b06 | 00:57.9–01:08.3 (10.4s) | L15 | Và điều kỳ diệu về giải phẫu miệng: Phía sau hai chiếc răng cửa là một màng da đặc biệt có thể khép kín miệng lại, cho phép gã vừa gặm gỗ vừa ngụp lặn dưới nước mà không sợ dăm gỗ hay nước tràn vào cổ họng! |  | Giải phẫu khoang miệng chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu: chiếc màng da sau răng cửa khép kín miệng lại giúp gã vừa gặm cành cây vừa ngụp lặn dưới nước không bị sặc. |
| b07 | 01:08.3–01:14.5 (6.2s) | L16 | Người bản địa Bắc Mỹ thời xưa thậm chí từng lấy hàm răng hải ly gắn vào cán gỗ để làm dao đục khắc gỗ siêu bền! |  | Người bản địa Bắc Mỹ thời xưa lấy hàm răng hải ly gắn vào cán gỗ làm dao đục khắc gỗ siêu bền. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này. |
| b08 | 01:14.5–01:21.9 (7.3s) | L17 | Chưa hết, gã kỹ sư này còn sở hữu một túi tuyến xạ hương đặc biệt dưới đuôi tiết ra chất ca-xtô-ri-um thơm nồng mùi vani ngọt ngào! |  | chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu đắp gò bùn nhỏ bên bờ suối rồi dùng đuôi quét xạ hương castoreum thơm mùi vani đóng dấu lãnh thổ; chai nước hoa cổ điển minh họa bên cạnh. |
| b09 | 01:21.9–01:31.5 (9.6s) | L18 | Gã thường đắp những gò bùn nhỏ dọc bờ suối rồi phun xạ hương lên đó để đóng dấu chủ quyền lãnh thổ, một mùi hương quyến rũ đến mức ngành công nghiệp nước hoa cổ điển từng săn lùng ráo riết! |  | chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu đắp những gò bùn nhỏ dọc bờ suối rồi phun xạ hương lên đóng dấu chủ quyền lãnh thổ, bên cạnh là lọ nước hoa cổ điển. |
| b10 | 01:31.5–01:41.8 (10.4s) | L19 | Và răng của hải ly mọc liên tục suốt cả cuộc đời! Nếu không chịu khó gặm gỗ mỗi ngày, chiếc răng thép này sẽ dài ra chọc thủng hộp sọ. Gặm cây không chỉ là đam mê xây dựng, mà là mệnh lệnh sinh tồn bắt buộc của giống loài! |  | chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu say sưa gặm khúc gỗ tròn xoe để mài răng không bị mọc dài quá mức; bảng 09:00 Sáng bật PASS. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này |

### scene03 · 00 CHIỀU: THÍ NGHIỆM KINH ĐIỂN VỚI CHIẾC LOA PHÁT TIẾNG NƯỚC CHẢY · 80.8s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:14.8 (14.8s) | L20 | 14h chiều: Đến lúc đội phóng sự chúng tôi thực hiện bài kiểm tra tâm lý lầy lội nhất! Các nhà sinh học từng thắc mắc: Động lực nào thôi thúc Kỹ Sư Đập Nước làm việc quần quật suốt ngày đêm không ngừng nghỉ? Có phải nó nhìn thấy dòng nước chảy xiết nên muốn ngăn lại? Câu trả lời là: Không hề! | **14:00** · thử thách tâm lý · L/350 · [0.35, 0.45] | Đồng hồ hiện 14H CHIỀU; chiếc máy quay phóng sự giấu kín ghi lại bài kiểm tra tâm lý ám ảnh tiếng nước chảy của hải ly. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này. |
| b02 | 00:14.8–00:28.5 (13.7s) | L21 | Thứ khiến hải ly phát điên không phải là thị giác, mà chính là âm thanh của tiếng nước chảy róc rách! Trong một thí nghiệm kinh điển của nhà khoa học Wilson, người ta đặt một chiếc loa phát thanh trên nền đất khô ráo giữa rừng và bật tiếng nước róc rách thật to. |  | Chiếc loa phóng thanh đặt trên bãi cỏ khô ráo giữa rừng đang phát ra từng đợt sóng âm thanh tiếng nước chảy róc rách thật to. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này. |
| b03 | 00:28.5–00:36.8 (8.3s) | L22 | Báo cáo hiện trường: Hải Ly vừa nghe thấy tiếng loa đã lập tức vứt bỏ mọi việc, đôi mắt đỏ ngầu hoảng hốt lao ngay ra suối khuân bùn đất chạy lên cạn! |  | chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu nghe tiếng loa róc rách mắt đỏ ngầu hoảng hốt, vứt bỏ khúc gỗ đang gặm lao ngay ra bờ suối vốc bùn đất chạy lên cạn. |
| b04 | 00:36.8–00:46.6 (9.8s) | L23 | Quý vị hãy nhìn xem: Gã hì hục tha cành cây, vốc từng nắm bùn đất trát kín mít xung quanh chiếc loa phát thanh cho đến khi âm thanh róc rách bị dập tắt hoàn toàn thì mới thở phào nhẹ nhõm! |  | chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu hì hục trát từng nắm bùn đất và cành cây bọc kín mít chiếc loa phát thanh thành một ngọn đồi bùn khổng lồ trên nền đất khô ráo. |
| b05 | 00:46.6–00:52.1 (5.5s) | L24 | Dù dưới chân là đất khô ráo không có lấy một giọt nước, gã vẫn đắp thành một ngọn đồi bùn khổng lồ! |  | Nền đất khô ráo không có lấy một giọt nước nhưng chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu vẫn đắp thành một ngọn đồi bùn khổng lồ quanh chiếc loa. |
| b06 | 00:52.1–01:04.3 (12.2s) | L25 | Thậm chí khi các nhà nghiên cứu treo chiếc loa lơ lửng trên cành cây cách mặt đất cả mét, chú hải ly vẫn kiên nhẫn khuân đất đắp cao dần quanh thân cây thành một chiếc cầu thang bùn kiên cố để trèo lên bịt chặt chiếc loa phát thanh! |  | Chiếc loa treo lơ lửng trên cành cây: chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu kiên nhẫn đắp bùn quanh thân cây thành chiếc cầu thang xoắn ốc để trèo lên bịt chặt chiếc loa. |
| b07 | 01:04.3–01:10.4 (6.1s) | L26 | Sự kiên trì và độ lầy lội đỉnh cao của gã kiến trúc sư này khiến toàn bộ các nhà khoa học phải phì cười thán phục! |  | Các nhà khoa học bật cười thán phục trước sự kiên trì và độ lầy lội đỉnh cao của gã kiến trúc sư hải ly. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này. |
| b08 | 01:10.4–01:20.8 (10.4s) | L27 | Đây chính là chứng ám ảnh cưỡng chế bẩm sinh kỳ quặc nhất tự nhiên: Đối với Kỹ Sư Đập Nước, tiếng nước chảy rò rỉ là một tội ác không thể tha thứ! Ở đâu có tiếng nước róc rách, ở đó phải được trát bùn bọc kín ngay lập tức! |  | Biểu tượng hội chứng ám ảnh cưỡng chế: biển cấm nước rò rỉ; chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu thở phào nhẹ nhõm cạnh ngọn đồi bùn; bảng 14:00 Chiều bật PASS. |

### scene04 · 00 TỐI: CÔNG TRƯỜNG XÂY ĐẬP VĨ ĐẠI CHẶN ĐỨNG DÒNG SÔNG · 94.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:11.0 (11.0s) | L28 | Hoàng hôn buông xuống lúc 18h: Đại công trường xây dựng chính thức bước vào giờ cao điểm! Cả gia đình hải ly gồm bố mẹ và các con bắt đầu phối hợp nhịp nhàng như một đội ngũ công nhân lành nghề. | **18:00 TỐI** · đại công trường · L/350 · [0.35, 0.45] | Đồng hồ hiện 18H TỐI; hoàng hôn đỏ rực buông xuống đại công trường xây đập: cả gia đình hải ly phối hợp kéo gỗ trát bùn tấp nập. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này. |
| b02 | 00:11.0–00:25.9 (15.0s) | L29 | Chúng kéo những thân cây lớn cắm sâu xuống đáy bùn tạo khung dầm chữ V ngược chịu lực, sau đó đan xen những cành cây nhỏ hơn vào giữa như đan phên liếp. Cuối cùng, chiếc đuôi dẹp như mái chèo được sử dụng như một chiếc bay thợ nề: múc bùn non, đá cuội và lá cây đầm chặt vào từng kẽ hở! |  | Khung dầm chữ V ngược bằng cọc gỗ cắm sâu đáy bùn; chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu dùng chiếc đuôi dẹp như bay thợ nề múc bùn non đầm chặt từng kẽ hở. |
| b03 | 00:25.9–00:40.2 (14.3s) | L30 | Để vận chuyển những khúc gỗ nặng hàng trăm cân từ sâu trong rừng ra bờ suối mà không tốn sức, chúng còn tự đào những con kênh dẫn nước dài hàng trăm mét len lỏi qua các bụi cây! Gỗ đốn hạ xong chỉ việc thả trôi nổi trên kênh đào về thẳng công trường xây dựng! Một tư duy logistics vượt trước thời đại! |  | Hệ thống kênh đào nhân tạo do hải ly đào sâu vào rừng: những khúc gỗ lớn được thả trôi nổi nhẹ nhàng theo dòng kênh về con đập. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này. |
| b04 | 00:40.2–00:53.9 (13.6s) | L31 | Công trình này kiên cố đến mức áp lực nước cuồn cuộn không tài nào cuốn trôi nổi! Nước sông bị chặn lại dâng cao dần, biến cả một thung lũng khô cằn thành một hồ nước rộng mênh mông, tạo nên một vùng đất ngập nước trù phú cho hàng ngàn loài cá, chim và ếch nhái kéo về sinh sống! |  | con đập gỗ khổng lồ đan cành cây và trát bùn đất bắc ngang dòng sông kiên cố chặn đứng dòng sông xiết: nước dâng lên biến thung lũng thành hồ nước mênh mông, đàn chim và cá kéo về sinh sống trù phú. |
| b05 | 00:53.9–01:02.8 (8.9s) | L32 | Tại Vườn quốc gia Wood Buffalo ở Canada, các nhà khoa học đã phát hiện một con đập do các thế hệ Kỹ Sư Đập Nước kiên trì xây dựng suốt hàng chục năm: Con đập dài tới 850m | **DÀI 850M** · kỷ lục thế giới · R/350 · [0.65, 0.45] | Toàn cảnh con đập dài 850m tại Canada nhìn từ vệ tinh không gian; so sánh với hình ảnh đập thủy điện Hoover khổng lồ. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này. |
| b06 | 01:02.8–01:10.4 (7.6s) | L33 | — gấp đôi chiều dài của đập thủy điện Hoover do con người xây — và là công trình động vật duy nhất nhìn thấy rõ mồn một từ ảnh chụp vệ tinh không gian! |  | So sánh: con đập hải ly dài gấp đôi đập thủy điện Hoover của con người, nhìn rõ mồn một từ ảnh vệ tinh không gian. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này. |
| b07 | 01:10.4–01:16.1 (5.7s) | L34 | Ngày nay, các nhà bảo tồn thiên nhiên trên khắp thế giới đang tích cực tái thả hải ly về các vùng hoang dã. |  | Khu rừng xanh tươi hồi sinh bên cạnh đập hải ly: ranh giới chống cháy rừng tự nhiên và lọc sạch nguồn nước; bảng 18:00 Tối bật PASS. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này. |
| b08 | 01:16.1–01:25.4 (9.3s) | L35 | Những con đập của chúng giúp nâng cao mạch nước ngầm, ngăn chặn thảm họa cháy rừng, thanh lọc các chất ô nhiễm độc hại và hồi sinh những dòng sông chết mà không tốn lấy một đồng ngân sách xây dựng! |  | Những con đập hải ly nâng cao mạch nước ngầm, ngăn thảm họa cháy rừng và thanh lọc nguồn nước ô nhiễm. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này. |
| b09 | 01:25.4–01:34.7 (9.3s) | L36 | Một sinh vật không có bằng kỹ sư, không có máy móc hiện đại, nhưng lại có thể tự tay vẽ lại bản đồ thủy văn của cả một lục địa! Thật là một kỳ quan kiến trúc không thể tin nổi! |  | chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu đứng ngạo nghễ trên đỉnh con đập giữa dòng sông hồi sinh, vẽ lại bản đồ thủy văn của cả một lục địa không cần máy móc hiện đại. |

### scene05 · 00 ĐÊM: PHÁO ĐÀI LÂU ĐÀI LODGE GIỮA HỒ VỚI CỬA VÀO NGẬP DƯỚI NƯỚC · 81.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:12.5 (12.5s) | L37 | Đồng hồ điểm 23h đêm! Nhiệt độ ngoài trời giảm xuống buốt giá, tiếng chó sói hú vang vọng từ bìa rừng săn tìm con mồi. Nhưng gia đình hải ly thì đã rút lui an toàn vào bên trong lâu đài kiên cố mang tên lodge nằm sừng sững giữa lòng hồ nước! | **23:00 ĐÊM** · pháo đài ngầm · L/350 · [0.35, 0.45] | Đồng hồ hiện 23H ĐÊM; ánh trăng lạnh buốt chiếu rọi khu rừng, con chó sói xám hung dữ đứng bên bờ hồ rình mò sói xám hú dài bên bờ trong khi gia đình hải ly an toàn trong pháo đài giữa hồ. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này. |
| b02 | 00:12.5–00:25.4 (12.9s) | L38 | Hãy quan sát mặt cắt kiến trúc tinh xảo của chiếc lâu đài này: Nó được đắp bằng hàng ngàn khúc gỗ và bùn đất dày tới 1m, mùa đông bùn đông cứng lại như bê tông cốt thép, móng vuốt của gấu hay sói cào rách móng cũng không tài nào phá vỡ nổi! | **DÀY 1 MÉT** · vách thành bê tông · R/350 · [0.65, 0.45] | Mặt cắt lâu đài lodge hình vòm giữa hồ: đắp bằng gỗ và bùn đất dày 1m đông cứng như bê tông cốt thép, sói cào rách móng không thủng. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này. |
| b03 | 00:25.4–00:39.5 (14.1s) | L39 | Và điều thiên tài nhất nằm ở hệ thống cửa ra vào: Tuyệt đối không có bất kỳ cánh cửa nào mở trên cạn! Lối vào duy nhất là hai đường hầm ngầm nằm sâu dưới mặt nước! Kẻ săn mồi trên cạn muốn đột nhập thì phải biết lặn sâu nín thở, điều mà chó sói và linh miêu không bao giờ làm được! Bên trong lâu |  | Đồ họa hai đường hầm ngập sâu dưới nước: chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu lặn xuống đáy bơi vào hầm bí mật, thú dữ trên bờ đứng nhìn bất lực. |
| b04 | 00:39.5–00:53.3 (13.8s) | L40 | đài được chia làm hai tầng khô ráo: Tầng dưới là phòng thay đồ để rũ sạch nước trên lông, còn tầng trên là phòng ngủ ấm cúng lót bằng vỏ cây khô êm ái, nơi cả gia đình quây quần sưởi ấm cho nhau. Đỉnh chóp lâu đài còn chừa lại một khe thông gió thông minh để đón không khí trong lành! |  | Bên trong lâu đài 2 tầng: tầng dưới vắt khô lông; tầng trên ấm áp lót vỏ cây khô nơi cả gia đình chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu quây quần ngủ say bên khe thông gió. |
| b05 | 00:53.3–01:05.6 (12.3s) | L41 | Vào mùa đông băng giá khi mặt hồ đóng băng dày cả mét, gia đình hải ly vẫn sống ung dung sung túc nhờ một kho lương thực bí mật: Trước mùa đông, chúng cắm hàng ngàn cành cây bạch dương tươi ngon găm sâu xuống đáy bùn dưới lòng hồ. |  | Tủ lạnh đáy hồ dưới lớp băng dày 1m: chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu bơi dưới băng lấy cành cây tươi cắm dưới bùn lên ăn ấm cúng trong lâu đài. |
| b06 | 01:05.6–01:11.7 (6.1s) | L42 | Dưới lớp băng dày, chúng chỉ việc bơi ra tủ lạnh đáy nước lấy cành cây về thưởng thức mà không cần ló đầu lên mặt băng! |  | chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu bơi dưới lớp băng dày ra tủ lạnh đáy nước lấy cành bạch dương tươi ngon về thưởng thức mà không cần ló đầu lên mặt băng. |
| b07 | 01:11.7–01:21.4 (9.7s) | L43 | Một công trình phòng thủ toàn diện chuẩn năm sao: vừa có hồ nước bảo vệ, vừa có cửa hầm bí mật, vừa có hệ thống sưởi ấm và thông gió tự nhiên! Đúng là đỉnh cao trí tuệ loài gặm nhấm! |  | Biểu tượng pháo đài 5 sao giữa hồ nước; bảng 23:00 Đêm bật PASS rực rỡ. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này. |

### scene06 · 00 SÁNG HÔM SAU: KẾT THÚC CA TRỰC VÀ HÉ LỘ BÓNG ĐEN TÊN LỬA 389 KM/H · 60.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:14.3 (14.3s) | L44 | Đồng hồ điểm 6h sáng hôm sau: Ca trực thực địa 24h chính thức khép lại! Ánh bình minh rực rỡ chiếu rọi xuống mặt hồ nước phẳng lặng do chính bàn tay Kỹ Sư Đập Nước tạo nên. Một đêm lao động cật lực, một hồ nước mới ra đời và sự sống lại sinh sôi nảy nở khắp cánh rừng già! | **06:00 SÁNG** · kết thúc 24h · L/350 · [0.35, 0.45] | Đồng hồ điểm 6H SÁNG HÔM SAU; ánh bình minh rạng rỡ trên mặt hồ yên ả, phóng viên hiện trường cầm mic có logo 24H kết thúc phóng sự 24h cạnh chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu. |
| b02 | 00:14.3–00:24.0 (9.7s) | L45 | Báo cáo thực địa 24h: Đạt điểm 10 xuất sắc cho danh hiệu Kiến trúc sư vĩ đại nhất giới động vật! Ký tên: Phóng viên thực địa chương trình 24h! | **ĐIỂM 10** · kỹ sư vĩ đại · R/350 · [0.65, 0.45] | Dấu mộc đỏ ĐẠT ĐIỂM 10 đóng lên tập phóng sự 24h; chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu nhận cúp vàng Kiến trúc sư vĩ đại nhất giới động vật. |
| b03 | 00:24.0–00:38.3 (14.3s) | L46 | Còn anh em thì sao? Nếu được sở hữu bộ răng cửa bọc sắt không bao giờ mòn của hải ly, hay năng lực xây nên cả một kỳ quan thiên nhiên thay đổi cảnh quan Trái Đất, anh em sẽ chọn siêu năng lực nào? Hãy để lại bình luận chia sẻ cùng chúng tôi nhé! Ca trực thực địa tập |  | Hai bàn cân lựa chọn: BÊN TRÁI bộ răng cửa bọc sắt cam không mòn; BÊN PHẢI năng lực xây đập thay đổi cả dòng sông, khán giả bình chọn. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này. |
| b04 | 00:38.3–00:46.0 (7.7s) | L47 | 30 xin được đóng máy tại đây. Nhưng tập sau, chúng ta sẽ chuyển thẳng tới một xưởng vũ khí khí động học đỉnh cao trên bầu trời để giải mã một sát thủ tốc độ kinh hoàng nhất lịch sử hành |  | Ống kính máy quay 24h đóng nắp lại, chuyển sang khung cảnh bầu trời xanh ngắt nơi có xưởng vũ khí khí động học tầng cao. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này. |
| b05 | 00:46.0–00:53.0 (7.0s) | L48 | tinh! Một cỗ tên lửa sống có thể bổ nhào từ tầng mây với vận tốc kinh hoàng lên tới 389 km/h mà không hề bị nổ tung lồng | **389 KM/H** · tên lửa sống · R/350 · [0.65, 0.45] | Một sinh vật bí ẩn được vẽ hoàn toàn bằng BÓNG ĐEN ĐẶC TUYỀN (solid black silhouette) hình chú chim cắt dũng mãnh xếp cánh hình chữ V lao bổ nhào thẳng từ tầng mây với vận tốc 389 km/h xé toạc không khí; ba dấu hỏi chấm vàng to tướng; KHÔNG vẽ mắt mỏ lông vũ thật. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này. |
| b06 | 00:53.0–00:55.2 (2.3s) | L49 | ngực nhờ hai chiếc nón giảm áp thần kỳ trong lỗ |  | Cận cảnh chiếc BÓNG ĐEN ĐẶC TUYỀN đầu chim với hai chiếc nón giảm áp xoắn ốc trong lỗ mũi chống vỡ phổi khi bổ nhào siêu thanh; ba dấu hỏi chấm to tướng. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này. |
| b07 | 00:55.2–01:00.2 (5.0s) | L50 | mũi! Đố các bạn biết bóng đen bí ẩn kỳ sau là loài vật nào? Hãy đoán ngay ở phần bình luận nhé! |  | Chiếc BÓNG ĐEN ĐẶC TUYỀN sát thủ tốc độ bổ nhào giữa ba dấu hỏi chấm vàng mời gọi khán giả đoán tên Chim Cắt Lớn tập sau. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này. |

## 5. Phân cảnh Shorts — từng beat

Banner: **ĐẶT LOA NƯỚC CHẢY TRƯỚC MẶT / HẢI LY VÀ CÁI KẾT?!** · giọng 48.6s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Điều gì sẽ xảy ra nếu bạn đặt một chiếc loa phát tiếng nước chảy trước mặt Hải Ly? |  |
| s02 | 00:05.2 | S02 | Ngay lập tức, gã kỹ sư đập nước này sẽ phát điên cuồng loạn, |  |
| s03 | 00:08.8 | S03 | vác bùn đất chạy hộc tốc lên cạn để trát kín mít chiếc loa cho đến khi tiếng nước róc rách tắt ngấm! |  |
| s04 | 00:14.2 | S04 | Hải Ly mắc chứng ám ảnh cưỡng chế bẩm sinh với âm thanh nước rò rỉ. |  |
| s05 | 00:18.6 | S05 | Thậm chí khi các nhà khoa học treo chiếc loa lơ lửng trên cành cây, gã còn kiên nhẫn đắp cả chiếc cầu thang bùn để trèo lên bịt chặt cho |  |
| s06 | 00:25.4 | S06 | bằng được, vì với gã tiếng nước rò rỉ là một tội ác không thể tha thứ! |  |
| s07 | 00:29.0 | S07 | Để phục vụ đam mê đắp đập, nó trang bị bộ răng cửa màu cam chứa đầy oxit sắt cứng như kim loại thép, |  |
| s08 | 00:34.5 | S08 | có khả năng tự mài sắc để đốn hạ thân cây to chỉ trong 30 phút! | **30 PHÚT** · hạ cây cổ thụ · R/620 · [0.62, 0.5] |
| s09 | 00:38.4 | S09 | Những con đập do nó xây dựng có thể dài tới 850m, chặn đứng dòng sông | **DÀI 850M** · đập khổng lồ · L/620 · [0.38, 0.5] |
| s10 | 00:42.4 | S10 | và nhìn thấy rõ mồn một từ vệ tinh không gian! |  |
| s11 | 00:45.1 | S11 | Đúng là kỹ sư xây dựng cuồng nhiệt và lầy lội nhất thế giới động vật! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Alo alo, xin chào toàn thể quý vị khán giả của chương trình thực địa 24h! Tôi đang có mặt tại một cánh rừng rậm rạp thuộc vùng hoang dã Bắc Mỹ, nơi sương sớm còn đang giăng kín mặt hồ phẳng lặng.". Bố cục: Cánh rừng ôn đới rậm rạp hoang dã Bắc Mỹ với sương sớm giăng mờ ảo trên mặt hồ phẳng lặng, chiếc đồng hồ đếm ngược 24H nhấp nháy góc màn hình. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Hôm nay, chiếc camera giấu kín của chúng ta sẽ bám sát từng bước chân của một kỹ sư xây dựng thiên tài nhưng cũng cực kỳ lầy lội!". Bố cục: Chiếc camera giấu kín trong bụi cây rình sẵn bám sát từng bước chân của một kỹ sư xây dựng thiên tài nhưng cực kỳ lầy lội, ống kính phản chiếu mặt hồ sương sớm. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Báo cáo phóng viên, mục tiêu số 30 đã xuất hiện từ bờ suối, đang lạch bạch vác theo một khúc gỗ nặng gấp đôi trọng lượng cơ thể!". Bố cục: BÊN TRÁI nữ trợ lý cầm bộ đàm chỉ tay về phía bờ suối; BÊN PHẢI phóng viên hiện trường cầm mic có logo 24H cầm mic hướng máy quay vào mục tiêu. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Hướng máy quay sang góc 9h ngay lập tức! Xin giới thiệu với toàn thể anh em: đây là Hải Ly, thuộc chi Castor, loài gặm nhấm lớn thứ hai trên Trái Đất và là nhân vật duy nhất trong giới động vật có chứng chỉ hành nghề: Kỹ Sư Đập Nước!". Bố cục: Ở GIỮA chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu mũm mĩm đáng yêu đội chiếc mũ bảo hộ kỹ sư màu vàng tươi, hai chân trước ôm khúc gỗ to tướng bước đi lạch bạch.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nhìn dáng đi trên cạn của gã thì vụng về buồn cười vô cùng: thân hình mập mạp béo ú nặng tới 30kg, bốn chân ngắn củn và chiếc đuôi dẹt phẳng lì hình mái chèo kéo lê lết trên mặt đất.". Bố cục: Chia đôi: BÊN TRÁI chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu đi lạch bạch vụng về trên bờ suối nặng 30kg; BÊN PHẢI chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu lặn xuống nước rẽ sóng bơi thoăn thoắt như tàu ngầm.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nhưng chỉ cần chạm vào làn nước mát, gã lập tức biến thành một thợ lặn cừ khôi với đôi chân màng bơi thoăn thoắt và bộ lông chống thấm nước hoàn hảo!". Bố cục: chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu lao xuống làn nước mát, biến thành thợ lặn cừ khôi với đôi chân màng bơi thoăn thoắt và bộ lông chống thấm nước hoàn hảo.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và điều điên rồ nhất sắp diễn ra trong 24h tới: Chúng ta sẽ chứng kiến cách một chú chuột khổng lồ dùng chính hàm răng của mình để đốn ngã cả một cánh rừng, tự tay xây nên những công trình vĩ đại có thể nhìn thấy rõ mồn một từ vệ tinh không gian ngoài Trái Đất! Bắt đầu đồng hồ đếm ngược!". Bố cục: Hình ảnh bản đồ chụp từ vệ tinh không gian ngoài Trái Đất: các công trình đập nước vĩ đại của loài hải ly hiện rõ mồn một giữa lục địa. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Trước khi gã bước vào ca làm việc chính thức, hãy chú ý chiếc đuôi vảy da dẹt hình mái chèo độc đáo: Đây không chỉ là bánh lái khi bơi lội dưới dòng nước xiết, mà còn là chiếc còi báo động khẩn cấp.". Bố cục: chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu đập mạnh chiếc đuôi dẹp như mái chèo xuống mặt nước bắn tung tóe bọt trắng xóa, phát ra tiếng nổ chan chát vang xa hàng trăm mét.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Mỗi khi phát hiện nguy hiểm, gã đập mạnh chiếc đuôi xuống mặt nước tạo tiếng nổ chan chát vang xa hàng trăm mét để báo động cho cả gia đình lặn trốn!". Bố cục: chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu đập mạnh chiếc đuôi xuống mặt nước tạo tiếng nổ chan chát vang xa hàng trăm mét báo động cho cả gia đình lặn trốn.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Đồng hồ điểm 9h sáng! Chúng ta đang áp sát hiện trường khai thác gỗ của Kỹ Sư Đập Nước. Hãy nhìn thẳng vào cận cảnh khuôn mặt của gã: Hai chiếc răng cửa hàm trên dài ngoằng nhô ra ngoài không phải màu trắng ngà như bình thường, mà lại có màu cam đậm rực rỡ như vừa mới nhúng vào gỉ sắt!". Bố cục: Đồng hồ hiện 9H SÁNG; cận cảnh khuôn mặt chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu khoe hai chiếc răng cửa hàm trên màu cam đậm rực rỡ bóng loáng như kim loại sắt.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "2015, một nghiên cứu đột phá trên tạp chí Science đã hé lộ bí mật chấn động: Lớp men phía trước răng của hải ly không phải chỉ có canxi, mà chứa đầy các tinh thể oxit sắt vô định hình siêu cứng!". Bố cục: Bìa tạp chí Science năm 2015 mở ra phân tích cấu trúc nano: các tinh thể oxit sắt vô định hình siêu cứng gắn chặt trong men răng hải ly. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Lớp kim loại tự nhiên này giúp răng của nó cứng hơn bất kỳ loài gặm nhấm nào trên hành tinh và kháng axit mài mòn tuyệt đối!". Bố cục: Hai chiếc răng cửa cam bóng loáng cứng hơn bất kỳ loài gặm nhấm nào, kháng axit mài mòn tuyệt đối, tỏa sáng như kim loại thép. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chưa dừng lại ở đó, mặt trước của răng cứng như thép trong khi mặt sau lại mềm hơn. Khi hải ly gặm gỗ, lớp mặt sau mòn nhanh hơn mặt trước, khiến đầu răng luôn tự động mài sắc bén như một chiếc lưỡi đục kim cương! Càng gặm nhiều, răng lại càng sắc ngọt!". Bố cục: Sơ đồ vát nhọn 20 độ của răng cửa: mặt sau mềm mòn nhanh hơn mặt trước cứng, đầu răng tự động mài sắc ngọt như lưỡi đục kim cương.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Hãy bấm giờ đếm ngược xem: Một thân cây bạch dương đường kính 15cm cứng cáp... gã chỉ cần đúng 30 phút gặm vòng quanh gốc cây là cả thân cây gỗ cổ thụ to lớn đổ rầm xuống mặt đất! Tiếng gặm cộp cộp vang vọng khắp góc rừng như một xưởng cưa máy chạy bằng cơm!". Bố cục: Chiếc đồng hồ bấm giờ 30 phút: chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu gặm vòng quanh gốc cây bạch dương 15cm làm cả thân cây to lớn đổ rầm xuống đất; dăm gỗ bay rào rào.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và điều kỳ diệu về giải phẫu miệng: Phía sau hai chiếc răng cửa là một màng da đặc biệt có thể khép kín miệng lại, cho phép gã vừa gặm gỗ vừa ngụp lặn dưới nước mà không sợ dăm gỗ hay nước tràn vào cổ họng!". Bố cục: Giải phẫu khoang miệng chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu: chiếc màng da sau răng cửa khép kín miệng lại giúp gã vừa gặm cành cây vừa ngụp lặn dưới nước không bị sặc.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Người bản địa Bắc Mỹ thời xưa thậm chí từng lấy hàm răng hải ly gắn vào cán gỗ để làm dao đục khắc gỗ siêu bền!". Bố cục: Người bản địa Bắc Mỹ thời xưa lấy hàm răng hải ly gắn vào cán gỗ làm dao đục khắc gỗ siêu bền. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chưa hết, gã kỹ sư này còn sở hữu một túi tuyến xạ hương đặc biệt dưới đuôi tiết ra chất ca-xtô-ri-um thơm nồng mùi vani ngọt ngào!". Bố cục: chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu đắp gò bùn nhỏ bên bờ suối rồi dùng đuôi quét xạ hương castoreum thơm mùi vani đóng dấu lãnh thổ; chai nước hoa cổ điển minh họa bên cạnh.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Gã thường đắp những gò bùn nhỏ dọc bờ suối rồi phun xạ hương lên đó để đóng dấu chủ quyền lãnh thổ, một mùi hương quyến rũ đến mức ngành công nghiệp nước hoa cổ điển từng săn lùng ráo riết!". Bố cục: chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu đắp những gò bùn nhỏ dọc bờ suối rồi phun xạ hương lên đóng dấu chủ quyền lãnh thổ, bên cạnh là lọ nước hoa cổ điển.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và răng của hải ly mọc liên tục suốt cả cuộc đời! Nếu không chịu khó gặm gỗ mỗi ngày, chiếc răng thép này sẽ dài ra chọc thủng hộp sọ. Gặm cây không chỉ là đam mê xây dựng, mà là mệnh lệnh sinh tồn bắt buộc của giống loài!". Bố cục: chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu say sưa gặm khúc gỗ tròn xoe để mài răng không bị mọc dài quá mức; bảng 09:00 Sáng bật PASS. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "14h chiều: Đến lúc đội phóng sự chúng tôi thực hiện bài kiểm tra tâm lý lầy lội nhất! Các nhà sinh học từng thắc mắc: Động lực nào thôi thúc Kỹ Sư Đập Nước làm việc quần quật suốt ngày đêm không ngừng nghỉ? Có phải nó nhìn thấy dòng nước chảy xiết nên muốn ngăn lại? Câu trả lời là: Không hề!". Bố cục: Đồng hồ hiện 14H CHIỀU; chiếc máy quay phóng sự giấu kín ghi lại bài kiểm tra tâm lý ám ảnh tiếng nước chảy của hải ly. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Thứ khiến hải ly phát điên không phải là thị giác, mà chính là âm thanh của tiếng nước chảy róc rách! Trong một thí nghiệm kinh điển của nhà khoa học Wilson, người ta đặt một chiếc loa phát thanh trên nền đất khô ráo giữa rừng và bật tiếng nước róc rách thật to.". Bố cục: Chiếc loa phóng thanh đặt trên bãi cỏ khô ráo giữa rừng đang phát ra từng đợt sóng âm thanh tiếng nước chảy róc rách thật to. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Báo cáo hiện trường: Hải Ly vừa nghe thấy tiếng loa đã lập tức vứt bỏ mọi việc, đôi mắt đỏ ngầu hoảng hốt lao ngay ra suối khuân bùn đất chạy lên cạn!". Bố cục: chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu nghe tiếng loa róc rách mắt đỏ ngầu hoảng hốt, vứt bỏ khúc gỗ đang gặm lao ngay ra bờ suối vốc bùn đất chạy lên cạn.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Quý vị hãy nhìn xem: Gã hì hục tha cành cây, vốc từng nắm bùn đất trát kín mít xung quanh chiếc loa phát thanh cho đến khi âm thanh róc rách bị dập tắt hoàn toàn thì mới thở phào nhẹ nhõm!". Bố cục: chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu hì hục trát từng nắm bùn đất và cành cây bọc kín mít chiếc loa phát thanh thành một ngọn đồi bùn khổng lồ trên nền đất khô ráo.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Dù dưới chân là đất khô ráo không có lấy một giọt nước, gã vẫn đắp thành một ngọn đồi bùn khổng lồ!". Bố cục: Nền đất khô ráo không có lấy một giọt nước nhưng chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu vẫn đắp thành một ngọn đồi bùn khổng lồ quanh chiếc loa.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Thậm chí khi các nhà nghiên cứu treo chiếc loa lơ lửng trên cành cây cách mặt đất cả mét, chú hải ly vẫn kiên nhẫn khuân đất đắp cao dần quanh thân cây thành một chiếc cầu thang bùn kiên cố để trèo lên bịt chặt chiếc loa phát thanh!". Bố cục: Chiếc loa treo lơ lửng trên cành cây: chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu kiên nhẫn đắp bùn quanh thân cây thành chiếc cầu thang xoắn ốc để trèo lên bịt chặt chiếc loa.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Sự kiên trì và độ lầy lội đỉnh cao của gã kiến trúc sư này khiến toàn bộ các nhà khoa học phải phì cười thán phục!". Bố cục: Các nhà khoa học bật cười thán phục trước sự kiên trì và độ lầy lội đỉnh cao của gã kiến trúc sư hải ly. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Đây chính là chứng ám ảnh cưỡng chế bẩm sinh kỳ quặc nhất tự nhiên: Đối với Kỹ Sư Đập Nước, tiếng nước chảy rò rỉ là một tội ác không thể tha thứ! Ở đâu có tiếng nước róc rách, ở đó phải được trát bùn bọc kín ngay lập tức!". Bố cục: Biểu tượng hội chứng ám ảnh cưỡng chế: biển cấm nước rò rỉ; chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu thở phào nhẹ nhõm cạnh ngọn đồi bùn; bảng 14:00 Chiều bật PASS.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Hoàng hôn buông xuống lúc 18h: Đại công trường xây dựng chính thức bước vào giờ cao điểm! Cả gia đình hải ly gồm bố mẹ và các con bắt đầu phối hợp nhịp nhàng như một đội ngũ công nhân lành nghề.". Bố cục: Đồng hồ hiện 18H TỐI; hoàng hôn đỏ rực buông xuống đại công trường xây đập: cả gia đình hải ly phối hợp kéo gỗ trát bùn tấp nập. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chúng kéo những thân cây lớn cắm sâu xuống đáy bùn tạo khung dầm chữ V ngược chịu lực, sau đó đan xen những cành cây nhỏ hơn vào giữa như đan phên liếp. Cuối cùng, chiếc đuôi dẹp như mái chèo được sử dụng như một chiếc bay thợ nề: múc bùn non, đá cuội và lá cây đầm chặt vào từng kẽ hở!". Bố cục: Khung dầm chữ V ngược bằng cọc gỗ cắm sâu đáy bùn; chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu dùng chiếc đuôi dẹp như bay thợ nề múc bùn non đầm chặt từng kẽ hở.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Để vận chuyển những khúc gỗ nặng hàng trăm cân từ sâu trong rừng ra bờ suối mà không tốn sức, chúng còn tự đào những con kênh dẫn nước dài hàng trăm mét len lỏi qua các bụi cây! Gỗ đốn hạ xong chỉ việc thả trôi nổi trên kênh đào về thẳng công trường xây dựng! Một tư duy logistics vượt trước thời đại!". Bố cục: Hệ thống kênh đào nhân tạo do hải ly đào sâu vào rừng: những khúc gỗ lớn được thả trôi nổi nhẹ nhàng theo dòng kênh về con đập. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Công trình này kiên cố đến mức áp lực nước cuồn cuộn không tài nào cuốn trôi nổi! Nước sông bị chặn lại dâng cao dần, biến cả một thung lũng khô cằn thành một hồ nước rộng mênh mông, tạo nên một vùng đất ngập nước trù phú cho hàng ngàn loài cá, chim và ếch nhái kéo về sinh sống!". Bố cục: con đập gỗ khổng lồ đan cành cây và trát bùn đất bắc ngang dòng sông kiên cố chặn đứng dòng sông xiết: nước dâng lên biến thung lũng thành hồ nước mênh mông, đàn chim và cá kéo về sinh sống trù phú.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tại Vườn quốc gia Wood Buffalo ở Canada, các nhà khoa học đã phát hiện một con đập do các thế hệ Kỹ Sư Đập Nước kiên trì xây dựng suốt hàng chục năm: Con đập dài tới 850m —". Bố cục: Toàn cảnh con đập dài 850m tại Canada nhìn từ vệ tinh không gian; so sánh với hình ảnh đập thủy điện Hoover khổng lồ. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "gấp đôi chiều dài của đập thủy điện Hoover do con người xây — và là công trình động vật duy nhất nhìn thấy rõ mồn một từ ảnh chụp vệ tinh không gian!". Bố cục: So sánh: con đập hải ly dài gấp đôi đập thủy điện Hoover của con người, nhìn rõ mồn một từ ảnh vệ tinh không gian. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Ngày nay, các nhà bảo tồn thiên nhiên trên khắp thế giới đang tích cực tái thả hải ly về các vùng hoang dã.". Bố cục: Khu rừng xanh tươi hồi sinh bên cạnh đập hải ly: ranh giới chống cháy rừng tự nhiên và lọc sạch nguồn nước; bảng 18:00 Tối bật PASS. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Những con đập của chúng giúp nâng cao mạch nước ngầm, ngăn chặn thảm họa cháy rừng, thanh lọc các chất ô nhiễm độc hại và hồi sinh những dòng sông chết mà không tốn lấy một đồng ngân sách xây dựng!". Bố cục: Những con đập hải ly nâng cao mạch nước ngầm, ngăn thảm họa cháy rừng và thanh lọc nguồn nước ô nhiễm. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Một sinh vật không có bằng kỹ sư, không có máy móc hiện đại, nhưng lại có thể tự tay vẽ lại bản đồ thủy văn của cả một lục địa! Thật là một kỳ quan kiến trúc không thể tin nổi!". Bố cục: chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu đứng ngạo nghễ trên đỉnh con đập giữa dòng sông hồi sinh, vẽ lại bản đồ thủy văn của cả một lục địa không cần máy móc hiện đại.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Đồng hồ điểm 23h đêm! Nhiệt độ ngoài trời giảm xuống buốt giá, tiếng chó sói hú vang vọng từ bìa rừng săn tìm con mồi. Nhưng gia đình hải ly thì đã rút lui an toàn vào bên trong lâu đài kiên cố mang tên lodge nằm sừng sững giữa lòng hồ nước!". Bố cục: Đồng hồ hiện 23H ĐÊM; ánh trăng lạnh buốt chiếu rọi khu rừng, con chó sói xám hung dữ đứng bên bờ hồ rình mò sói xám hú dài bên bờ trong khi gia đình hải ly an toàn trong pháo đài giữa hồ. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Hãy quan sát mặt cắt kiến trúc tinh xảo của chiếc lâu đài này: Nó được đắp bằng hàng ngàn khúc gỗ và bùn đất dày tới 1m, mùa đông bùn đông cứng lại như bê tông cốt thép, móng vuốt của gấu hay sói cào rách móng cũng không tài nào phá vỡ nổi!". Bố cục: Mặt cắt lâu đài lodge hình vòm giữa hồ: đắp bằng gỗ và bùn đất dày 1m đông cứng như bê tông cốt thép, sói cào rách móng không thủng. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và điều thiên tài nhất nằm ở hệ thống cửa ra vào: Tuyệt đối không có bất kỳ cánh cửa nào mở trên cạn! Lối vào duy nhất là hai đường hầm ngầm nằm sâu dưới mặt nước! Kẻ săn mồi trên cạn muốn đột nhập thì phải biết lặn sâu nín thở, điều mà chó sói và linh miêu không bao giờ làm được! Bên trong lâu đài được". Bố cục: Đồ họa hai đường hầm ngập sâu dưới nước: chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu lặn xuống đáy bơi vào hầm bí mật, thú dữ trên bờ đứng nhìn bất lực.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "chia làm hai tầng khô ráo: Tầng dưới là phòng thay đồ để rũ sạch nước trên lông, còn tầng trên là phòng ngủ ấm cúng lót bằng vỏ cây khô êm ái, nơi cả gia đình quây quần sưởi ấm cho nhau. Đỉnh chóp lâu đài còn chừa lại một khe thông gió thông minh để đón không khí trong lành!". Bố cục: Bên trong lâu đài 2 tầng: tầng dưới vắt khô lông; tầng trên ấm áp lót vỏ cây khô nơi cả gia đình chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu quây quần ngủ say bên khe thông gió.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Vào mùa đông băng giá khi mặt hồ đóng băng dày cả mét, gia đình hải ly vẫn sống ung dung sung túc nhờ một kho lương thực bí mật: Trước mùa đông, chúng cắm hàng ngàn cành cây bạch dương tươi ngon găm sâu xuống đáy bùn dưới lòng hồ.". Bố cục: Tủ lạnh đáy hồ dưới lớp băng dày 1m: chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu bơi dưới băng lấy cành cây tươi cắm dưới bùn lên ăn ấm cúng trong lâu đài.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Dưới lớp băng dày, chúng chỉ việc bơi ra tủ lạnh đáy nước lấy cành cây về thưởng thức mà không cần ló đầu lên mặt băng!". Bố cục: chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu bơi dưới lớp băng dày ra tủ lạnh đáy nước lấy cành bạch dương tươi ngon về thưởng thức mà không cần ló đầu lên mặt băng.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Một công trình phòng thủ toàn diện chuẩn năm sao: vừa có hồ nước bảo vệ, vừa có cửa hầm bí mật, vừa có hệ thống sưởi ấm và thông gió tự nhiên! Đúng là đỉnh cao trí tuệ loài gặm nhấm!". Bố cục: Biểu tượng pháo đài 5 sao giữa hồ nước; bảng 23:00 Đêm bật PASS rực rỡ. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Đồng hồ điểm 6h sáng hôm sau: Ca trực thực địa 24h chính thức khép lại! Ánh bình minh rực rỡ chiếu rọi xuống mặt hồ nước phẳng lặng do chính bàn tay Kỹ Sư Đập Nước tạo nên. Một đêm lao động cật lực, một hồ nước mới ra đời và sự sống lại sinh sôi nảy nở khắp cánh rừng già!". Bố cục: Đồng hồ điểm 6H SÁNG HÔM SAU; ánh bình minh rạng rỡ trên mặt hồ yên ả, phóng viên hiện trường cầm mic có logo 24H kết thúc phóng sự 24h cạnh chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Báo cáo thực địa 24h: Đạt điểm 10 xuất sắc cho danh hiệu Kiến trúc sư vĩ đại nhất giới động vật! Ký tên: Phóng viên thực địa chương trình 24h!". Bố cục: Dấu mộc đỏ ĐẠT ĐIỂM 10 đóng lên tập phóng sự 24h; chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu nhận cúp vàng Kiến trúc sư vĩ đại nhất giới động vật.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Còn anh em thì sao? Nếu được sở hữu bộ răng cửa bọc sắt không bao giờ mòn của hải ly, hay năng lực xây nên cả một kỳ quan thiên nhiên thay đổi cảnh quan Trái Đất, anh em sẽ chọn siêu năng lực nào? Hãy để lại bình luận chia sẻ cùng chúng tôi nhé! Ca trực thực địa tập 30". Bố cục: Hai bàn cân lựa chọn: BÊN TRÁI bộ răng cửa bọc sắt cam không mòn; BÊN PHẢI năng lực xây đập thay đổi cả dòng sông, khán giả bình chọn. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "xin được đóng máy tại đây. Nhưng tập sau, chúng ta sẽ chuyển thẳng tới một xưởng vũ khí khí động học đỉnh cao trên bầu trời để giải mã một sát thủ tốc độ kinh hoàng nhất lịch sử hành tinh!". Bố cục: Ống kính máy quay 24h đóng nắp lại, chuyển sang khung cảnh bầu trời xanh ngắt nơi có xưởng vũ khí khí động học tầng cao. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Một cỗ tên lửa sống có thể bổ nhào từ tầng mây với vận tốc kinh hoàng lên tới 389 km/h mà không hề bị nổ tung lồng ngực". Bố cục: Một sinh vật bí ẩn được vẽ hoàn toàn bằng BÓNG ĐEN ĐẶC TUYỀN (solid black silhouette) hình chú chim cắt dũng mãnh xếp cánh hình chữ V lao bổ nhào thẳng từ tầng mây với vận tốc 389 km/h xé toạc không khí; ba dấu hỏi chấm vàng to tướng; KHÔNG vẽ mắt mỏ lông vũ thật. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "nhờ hai chiếc nón giảm áp thần kỳ trong lỗ mũi!". Bố cục: Cận cảnh chiếc BÓNG ĐEN ĐẶC TUYỀN đầu chim với hai chiếc nón giảm áp xoắn ốc trong lỗ mũi chống vỡ phổi khi bổ nhào siêu thanh; ba dấu hỏi chấm to tướng. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Đố các bạn biết bóng đen bí ẩn kỳ sau là loài vật nào? Hãy đoán ngay ở phần bình luận nhé!". Bố cục: Chiếc BÓNG ĐEN ĐẶC TUYỀN sát thủ tốc độ bổ nhào giữa ba dấu hỏi chấm vàng mời gọi khán giả đoán tên Chim Cắt Lớn tập sau. KHÔNG có chú hải ly đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Điều gì sẽ xảy ra nếu bạn đặt một chiếc loa phát tiếng nước chảy trước mặt Hải Ly?". Bố cục: Khung dọc: Đặt chiếc loa phát tiếng nước chảy róc rách trước mặt chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu trên bãi cỏ khô ráo.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Ngay lập tức, gã kỹ sư đập nước này sẽ phát điên cuồng loạn,". Bố cục: chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu mắt đỏ ngầu hoảng hốt, vứt bỏ khúc gỗ lao ra suối vác bùn chạy thục mạng lên cạn.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "vác bùn đất chạy hộc tốc lên cạn để trát kín mít chiếc loa cho đến khi tiếng nước róc rách tắt ngấm!". Bố cục: chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu vác bùn đất chạy hộc tốc lên cạn, trát kín mít chiếc loa cho đến khi tiếng nước róc rách tắt ngấm.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Hải Ly mắc chứng ám ảnh cưỡng chế bẩm sinh với âm thanh nước rò rỉ.". Bố cục: chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu trát bùn bọc kín mít chiếc loa phát thanh cho đến khi âm thanh róc rách tắt ngấm.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Thậm chí khi các nhà khoa học treo chiếc loa lơ lửng trên cành cây, gã còn kiên nhẫn đắp cả chiếc cầu thang bùn để trèo lên bịt chặt cho bằng được,". Bố cục: Chiếc loa treo lơ lửng trên cành cây; chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu kiên nhẫn đắp chiếc cầu thang bùn xoắn ốc để trèo lên bịt chặt chiếc loa bằng được.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "vì với gã tiếng nước rò rỉ là một tội ác không thể tha thứ!". Bố cục: Biển cấm khổng lồ gạch chéo giọt nước rò rỉ; chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu khoanh tay nghiêm nghị trước chiếc loa đã bị bọc kín bùn: tiếng nước rò rỉ là tội ác không thể tha thứ.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Để phục vụ đam mê đắp đập, nó trang bị bộ răng cửa màu cam chứa đầy oxit sắt cứng như kim loại thép,". Bố cục: Cận cảnh bộ răng cửa màu cam rực rỡ chứa oxit sắt siêu cứng lấp lánh như kim loại thép.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "có khả năng tự mài sắc để đốn hạ thân cây to chỉ trong 30 phút!". Bố cục: chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu gặm đốn ngã thân cây bạch dương to lớn chỉ trong 30 phút, dăm gỗ bay rào rào.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Những con đập do nó xây dựng có thể dài tới 850m, chặn đứng dòng sông và". Bố cục: con đập gỗ khổng lồ đan cành cây và trát bùn đất bắc ngang dòng sông kiên cố dài 850m chặn đứng dòng sông lớn, nước dâng lên tạo hồ nước mênh mông.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "nhìn thấy rõ mồn một từ vệ tinh không gian!". Bố cục: Ảnh chụp từ vệ tinh không gian ngoài Trái Đất nhìn thấy rõ mồn một con đập hải ly.
```
</details>

<details><summary>S11</summary>

```text
HÌNH S11 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Ly nâu mũm mĩm, răng cửa cam rực rỡ, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đúng là kỹ sư xây dựng cuồng nhiệt và lầy lội nhất thế giới động vật!". Bố cục: Chân dung chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu đội mũ bảo hộ kỹ sư giơ bay trát bùn đứng trên đỉnh con đập ngạo nghễ.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/50 của video YouTube về Hải Ly). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu. Nhân vật phụ cố định: phóng viên hiện trường cầm mic có logo 24H; con chó sói xám hung dữ đứng bên bờ hồ rình mò; con đập gỗ khổng lồ đan cành cây và trát bùn đất bắc ngang dòng sông. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/11 của video YouTube Shorts về Hải Ly). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Hải Ly (Castor canadensis) hoạt hình màu nâu hạt dẻ mũm mĩm đáng yêu, đôi tai tròn nhỏ, đôi mắt to lanh lợi, bộ răng cửa màu cam đậm rực rỡ lấp lánh như kim loại sắt, chiếc đuôi dẹp hình mái chèo có vân vảy da, đội một chiếc mũ bảo hộ kỹ sư công trình màu vàng tươi trên đầu. Nhân vật phụ: con đập gỗ khổng lồ đan cành cây và trát bùn đất bắc ngang dòng sông. 
```
</details>

## 7. SEO

- **title:** Đặt Loa Phát Tiếng Nước Chảy Trước Mặt Hải Ly Và Cái Kết?!
- **hook_paragraph:** Hải Ly (Castor canadensis) - Kỹ Sư Đập Nước thiên tài với bộ răng cửa bọc oxit sắt cực cứng, bị ám ảnh cưỡng chế tiếng nước róc rách đến mức đắp bùn đất kín cả chiếc loa phát nhạc và xây nên con đập dài 850m nhìn thấy từ vũ trụ!
- **question:** Nếu được sở hữu 1 năng lực của Hải Ly: bộ răng bọc sắt không bao giờ mòn hay tài năng kiến trúc xây đập thay đổi cả dòng sông, bạn chọn cái nào? Và đoán xem bóng đen tập sau là loài nào?
- **next_teaser:** Bóng đen sát thủ tốc độ: cỗ tên lửa sống bổ nhào 389 km/h có nón giảm áp trong mũi chống vỡ phổi!
- **shorts_title:** Đặt Loa Tiếng Nước Chảy Trước Mặt Hải Ly Và Cái Kết?! 🦫 #độngvật #hảily
- **shorts_desc:** Hải Ly nghe tiếng loa nước chảy liền phát điên trát bùn kín mít loa! Khám phá Kỹ Sư Đập Nước với bộ răng bằng oxit sắt và con đập 850m nhìn từ vũ trụ.
- **bullets:** Vũ khí răng cửa sắt: Lớp oxit sắt màu cam siêu cứng và cấu tạo tự mài sắc bén · Ám ảnh tiếng nước chảy: Thí nghiệm đắp bùn kín mít chiếc loa phát thanh róc rách · Kỳ quan đập nước: Đan cành cây và trát bùn đất chịu áp lực dòng sông cuồn cuộn · Lâu đài lodge pháo đài: Hai tầng khô ráo với cửa hầm bí mật ngập sâu dưới nước
- **tags:** hải ly, hai ly, castor, beaver, kỹ sư đập nước, đập hải ly, động vật kỳ lạ, thế giới động vật, động vật hài hước, vẽ chuyện hoang dã, whiteboard animation, khoa học thú vị
- **hashtags:** #độngvật #hảily #VẽChuyệnHoangDã

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-30-hai-ly
python src/episode/pipeline.py tts    projects/tap-30-hai-ly     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-30-hai-ly     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-30-hai-ly     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-30-hai-ly              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-30-hai-ly --force
python scripts/beat_sheet.py projects/tap-30-hai-ly               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-30-hai-ly/audio/shorts.wav projects/tap-30-hai-ly/renders/tap-30-hai-ly_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-30-hai-ly
python src/episode/pipeline.py seo    projects/tap-30-hai-ly
python src/episode/episode_doc.py     projects/tap-30-hai-ly
```

# TẬP 33 — ẾCH GỖ BẮC CỰC · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-33-ech-go-bac-cuc`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-33-ech-go-bac-cuc`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F4` · **Persona giọng:** `phong_vien_24h` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Ếch Gỗ Bắc Cực |
| Tiêu đề YouTube | Sinh Vật Tự Đóng Băng Tim Ngừng Đập & Hồi Sinh Sau Mùa Đông?! \| Tập 33 |
| Video dài | `renders/tap-33-ech-go-bac-cuc_long.mp4` — 12:29.6 (749.6s) |
| Shorts | `renders/tap-33-ech-go-bac-cuc_shorts.mp4` — 0:55.5 (55.5s) |
| Thumbnail | `renders/tap-33-ech-go-bac-cuc_thumbnail.jpg` |
| Số hình | dài 74 beat / 74 ảnh riêng; Shorts 13 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/74 của video YouTube về Ếch Gỗ Bắc Cực). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa truyện tranh sinh tồn Bắc Cực Cryo-Noir Graphic Novel 2D: nét mực đen sắc sảo gai góc, các tinh thể băng tuyết lam ngọc sắc nhọn, phối hợp dải màu cam nhiệt kế sinh tồn rực rỡ tương phản mạnh mẽ, nền trắng tinh hoàn toàn, không watermark, không chữ, biểu cảm nhân vật hài hước kịch tính theo chuẩn khoa học.. NHÂN VẬT CHÍNH cố định: chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles). Nhân vật phụ cố định: chú chim cánh cụt phóng viên hoạt hình mặc áo phao lông thú ấm áp, cầm micro phỏng vấn run rẩy giữa trời tuyết rơi; chú gấu Bắc Cực hoạt hình lông trắng to lớn mập mạp ngơ ngác, cầm một cành cây nhỏ gõ vào khối đá lạnh; nhân vật trái tim hoạt hình màu đỏ đội mũ len nhỏ bị bọc trong tinh thể băng xanh lam trong suốt; bác sĩ cú mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắng và cầm bảng theo dõi thông số sinh tồn. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — KHÁM PHÁ QUÁI KIỆT BĂNG GIÁ GIỮA BÃO TUYẾT ÂM 20 ĐỘ C Ở ALASKA
*Thẻ chương:* BÁO ĐỘNG SINH TỒN VÙNG CỰC: ÂM HAI MƯƠI ĐỘ C VÀ KẺ THÁCH THỨC TỬ THẦN

*Badge:* `BÁO ĐỘNG VÙNG CỰC` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene01_p0.wav` (551 ký tự) · mood `don_dap`

```text
Báo cáo khẩn cấp từ hiện trường vùng cực! Phóng viên hai mươi bốn giờ đang có mặt trực tiếp tại cánh rừng lá kim taiga phủ đầy tuyết trắng ở tiểu bang A-lát-xka, nơi chiếc nhiệt kế chuyên dụng vừa tụt thẳng đứng xuống mức âm hai mươi độ C! Gió bắc cực gầm rú rít từng cơn lạnh buốt thấu tận xương tủy, làm cho lớp hơi nước thở ra vừa chạm vào không khí là đông đặc thành bụi băng li ti. Mọi nhánh cây ngọn cỏ đều phủ một lớp sương muối trắng toát, và các mặt hồ nước ngọt sâu thẳm đã hóa thành những khối đá tảng hoa cương chẳng hề có một vết rạn nứt.
```
**Part 1** → `audio/vs/scene01_p1.wav` (411 ký tự) · mood `don_dap`

```text
Trong điều kiện thời tiết tử thần khắc nghiệt đến rợn người này, hãy quan sát cách các cư dân bản địa đối phó với mùa đông: Lũ gấu Bắc Cực to lớn phải cuộn tròn trong hang tuyết với lớp mỡ dày hàng chục xăng-ti-mét, đàn chim di cư thiện chiến đã vỗ cánh bay hàng ngàn cây số về phương Nam ấm áp từ ba tháng trước, còn lũ chuột đồng thì rúc sâu cả mét dưới lòng đất nơi nhiệt độ còn giữ được trên mức không độ C.
```
**Part 2** → `audio/vs/scene01_p2.wav` (180 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Alo phóng viên ơi! Tôi không có lông vũ, không có mỡ dày, cũng chẳng thèm đào hang sâu luôn! Chỉ có mỗi chiếc quần đùi da cóc mỏng manh này thôi thì có trụ nổi qua đêm nay không ạ?
```
**Part 3** → `audio/vs/scene01_p3.wav` (438 ký tự) · mood `hao_hung`

```text
[surprise-oh] Ấy thế mà ngay dưới chân của chúng tôi, chỉ cách mặt tuyết chừng vài phân bên dưới lớp lá rụng và rêu mục mỏng manh, một sinh vật bé nhỏ lại đang thản nhiên chờ đón lưỡi hái tử thần của mùa đông! Xin giới thiệu nhân vật chính của hồ sơ sinh tồn số ba mươi ba: Ếch Gỗ Bắc Cực, mang danh pháp khoa học Li-thô-ba-tét xin-va-ti-cút, kẻ được giới sinh học toàn cầu ngả mũ thán phục với biệt danh Quái Kiệt Băng Giá của muôn loài!
```
**Part 4** → `audio/vs/scene01_p4.wav` (493 ký tự) · mood `tram_bi_an`

```text
Hãy nhìn vào những thông số trắc lượng cơ thể vô cùng khiêm tốn của sinh vật này: Toàn thân chú ếch gỗ trưởng thành chỉ dài từ năm đến bảy xăng-ti-mét, và cân nặng vỏn vẹn từ tám đến mười lăm gam, nghĩa là chỉ nhẹ tương đương một quả nho nhỏ hoặc hai quả trứng cút luộc! Làn da của nó có màu nâu đồng pha lẫn xám của vỏ cây rừng, và điểm nhận dạng đặc trưng nhất chính là hai vệt sọc đen sẫm kéo dài từ khóe mắt vòng qua tai, trông hệt như chiếc mặt nạ hiệp sĩ bí ẩn trong các bộ truyện tranh!
```
**Part 5** → `audio/vs/scene01_p5.wav` (504 ký tự) · mood `tram_bi_an`

```text
Thế nhưng, điểm điên rồ và kỳ quặc nhất trong tập tính sinh học của chú ếch này là gì? Các loài ếch nhái thông thường khác ở xứ ôn đới bắt buộc phải lặn sâu xuống đáy bùn lầy của đáy hồ không đóng băng để sống sót qua mùa đông. Còn Ếch Gỗ Bắc Cực thì không! Nó không thể bơi xuống đáy hồ vì phổi và da của nó sẽ chết ngạt. Thay vào đó, nó chọn cách ở lì ngay trên nền rừng lạnh giá, nơi nhiệt độ sẽ chạm đáy âm hai mươi độ C, và sẵn sàng để toàn bộ cơ thể mình bị đóng băng thành một tảng đá vô tri giác!
```

### scene02 — CƠ CHẾ TỰ ĐÓNG BĂNG 70% LƯỢNG NƯỚC CƠ THỂ MÀ KHÔNG RÁCH TẾ BÀO
*Thẻ chương:* BÍ MẬT MẦM ĐÁ NGOẠI BÀO: BIẾN NƯỚC THÀNH GIÁP BĂNG BẢO VỆ NỘI TẠNG

*Badge:* `MẦM ĐÁ NGOẠI BÀO` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene02_p0.wav` (533 ký tự) · mood `don_dap`

```text
Để thấy được sự phi thường của Quái Kiệt Băng Giá, trước hết chúng ta cần hiểu rõ vì sao đối với hầu hết mọi sinh vật trên Trái Đất, việc bị đóng băng đồng nghĩa với một bản án tử hình không thể đảo ngược! Khi nước nguyên chất chuyển từ thể lỏng sang thể rắn ở nhiệt độ dưới không độ C, thể tích của nó sẽ giãn nở đột ngột thêm khoảng chín phần trăm. Nguy hiểm hơn nữa, các tinh thể đá hình thành tự do trong môi trường sống sẽ phát triển thành những cấu trúc gai nhọn li ti, sắc bén hệt như hàng triệu lưỡi dao găm siêu nhỏ sắc lẹm!
```
**Part 1** → `audio/vs/scene02_p1.wav` (432 ký tự) · mood `don_dap`

```text
Nếu hiện tượng đóng băng vô kiểm soát này xảy ra bên trong cơ thể con người hay bất kỳ loài động vật nào khác, những mũi dao băng sắc nhọn đó sẽ lập tức đâm thủng lớp màng lipid mỏng manh của tế bào, xé toạc các vi mạch máu trong tích tắc và phá nát toàn bộ cấu trúc nội tạng! Hậu quả là ngay khi vừa tan đá, các mô tế bào sẽ vỡ vụn và hoại tử hoàn toàn, dẫn đến cái chết gần như tức thì mà chẳng thiết bị y khoa nào có thể cứu vãn!
```
**Part 2** → `audio/vs/scene02_p2.wav` (188 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Kính thưa các tinh thể đá mũi nhọn hung dữ! Tuyệt đối cấm bén mảng vào khoang tim và lá gan của tôi nhé! Ai muốn đóng băng thì xếp hàng ngay ngắn ra ngoài da và dưới bụng đứng hết cho tôi!
```
**Part 3** → `audio/vs/scene02_p3.wav` (615 ký tự) · mood `hao_hung`

```text
[surprise-oh] Và đó chính là lúc chiến thuật tạo mầm đá ngoại bào thần kỳ của chú ếch gỗ phát huy uy lực tối thượng! Năm một ngàn chín trăm chín mươi ba, nhóm nghiên cứu của tiến sĩ Giắc Cốt-xtan-dô tại Đại học Miami đã công bố một phát hiện chấn động trên Tạp chí Sinh lý học Hoa Kỳ: Trong huyết tương và dịch ngoại bào của Ếch Gỗ Bắc Cực chứa một họ protein chuyên biệt mang tên protein tạo mầm đá! Khi nhiệt độ môi trường vừa hạ xuống mức âm một đến âm hai độ C, những protein này lập tức đóng vai trò như những thỏi nam châm định hướng, kích thích các phân tử nước bên ngoài tế bào kết tinh thành đá trước tiên!
```
**Part 4** → `audio/vs/scene02_p4.wav` (456 ký tự) · mood `tram_bi_an`

```text
Thay vì để băng đá xuất hiện ngẫu nhiên và bừa bãi, cơ thể của ếch gỗ chủ động kiểm soát tuyệt đối vị trí đóng băng: Băng chỉ được phép hình thành ở các khoang trống nằm ngoài màng tế bào, trong ổ bụng, dưới lớp da lưng và xung quanh các bó cơ bắp! Khi nước ở bên ngoài đóng băng, hiện tượng thẩm thấu tự nhiên sẽ rút dần nước lỏng từ bên trong tế bào ra ngoài, giống như việc bạn rút ruột nước ra khỏi một quả bóng bay để nó xẹp lại một cách có tính toán.
```
**Part 5** → `audio/vs/scene02_p5.wav` (422 ký tự) · mood `tram_bi_an`

```text
Khối lượng băng hình thành bên ngoài tế bào này tăng dần lên một cách đáng kinh ngạc, cho đến khi chiếm tới sáu mươi lăm đến bảy mươi phần trăm tổng dung tích nước của toàn bộ cơ thể! Hãy tưởng tượng: Bảy mươi phần trăm cơ thể của bạn biến thành băng cứng ngắc như một hòn đá hoa cương, nhưng nhờ có cơ chế điều hướng mầm đá tài tình, chẳng có tinh thể nhọn nào được phép chạm vào không gian thiêng liêng bên trong tế bào!
```

### scene03 — GAN PHÌNH TO BƠM GLUCOSE SIÊU ĐẬM ĐẶC GẤP 300 LẦN CHỐNG ĐÔNG TẾ BÀO
*Thẻ chương:* BÁO ĐỘNG ĐỎ TRONG GAN: CƠN BÃO ĐƯỜNG HUYẾT CỨU MẠNG KỲ DIỆU

*Badge:* `BÃO ĐƯỜNG CẤP TỐC` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene03_p0.wav` (414 ký tự) · mood `don_dap`

```text
Thế nhưng, một bài toán hóc búa khác lập tức xuất hiện ngay tại đây! Nếu nước bên ngoài tế bào liên tục bị hút đi để tạo thành lớp giáp băng, chẳng phải áp suất thẩm thấu sẽ vắt kiệt từng giọt nước bên trong tế bào, khiến tế bào bị mất nước nghiêm trọng, teo tóp lại thành một mảnh vụn khô cằn và chết vì suy kiệt hay sao? Đúng là như vậy, nếu không có vũ khí bí mật thứ hai mang tên siêu chất chống đông sinh học!
```
**Part 1** → `audio/vs/scene03_p1.wav` (256 ký tự) · mood `don_dap`

```text
Ngay vào khoảnh khắc những cảm biến nhiệt độ trên da của ếch cảm nhận được tinh thể băng chạm vào lớp biểu bì, một tín hiệu báo động đỏ cấp quốc gia được phát đi dọc theo tủy sống, truyền thẳng đến cơ quan nội tạng quan trọng nhất: Nhà máy hóa chất lá gan!
```
**Part 2** → `audio/vs/scene03_p2.wav` (169 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Báo cáo chỉ huy trưởng! Bộ phận gan đã nhận lệnh báo động khẩn cấp! Kho dự trữ đường năng lượng đang mở hết van xả lũ, chuẩn bị biến toàn bộ máu thành siro ngọt lịm đây!
```
**Part 3** → `audio/vs/scene03_p3.wav` (501 ký tự) · mood `hao_hung`

```text
[surprise-oh] Những nghiên cứu đột phá mang tính lịch sử của vợ chồng giáo sư Kên-nét Xtô-ri từ năm một ngàn chín trăm tám mươi tám đã hé lộ một kỳ quan chuyển hóa sinh hóa: Trong suốt mùa thu, lá gan của ếch gỗ tích lũy một lượng đường phức gờ-ly-cô-gien khổng lồ, khiến lá gan phình to chiếm tới mười phần trăm trọng lượng cơ thể. Và ngay khi quá trình đóng băng bắt đầu, lá gan này lập tức kích hoạt enzyme phân giải gờ-ly-cô-gien với tốc độ tên lửa, biến toàn bộ thành đường đơn gờ-lu-cô-zơ tự do!
```
**Part 4** → `audio/vs/scene03_p4.wav` (558 ký tự) · mood `tram_bi_an`

```text
Chỉ trong vòng vài giờ đồng hồ ngắn ngủi, lượng đường gờ-lu-cô-zơ được bơm ồ ạt vào dòng máu, đẩy nồng độ đường huyết của chú ếch vọt lên gấp từ một trăm đến ba trăm lần so với mức bình thường! Để dễ hình dung độ kinh hoàng của con số này: Nếu nồng độ đường huyết của một người trưởng thành chỉ cần tăng lên gấp ba đến bốn lần bình thường, người đó đã rơi vào trạng thái hôn mê tiểu đường cấp tính và tử vong nếu không được tiêm insulin cấp cứu! Nhưng với Quái Kiệt Băng Giá, nồng độ đường gấp ba trăm lần lại chính là chiếc phao cứu sinh vĩ đại nhất của nó!
```
**Part 5** → `audio/vs/scene03_p5.wav` (562 ký tự) · mood `tram_bi_an`

```text
Song song với đường gờ-lu-cô-zơ, thận của ếch gỗ cũng giữ lại hợp chất u-rê ở nồng độ cực cao. Hai hợp chất này hòa quyện tạo thành một dung dịch siro chống đông cờ-rai-ô-prô-tếch-tần tự nhiên siêu đậm đặc, thấm đẫm vào từng milimet khối chất nguyên sinh bên trong tế bào. Siro này hạ điểm đông đặc của dịch nội bào xuống rất sâu, khiến nước bên trong tế bào không thể đóng băng thành đá được nữa mà vẫn duy trì ở trạng thái sền sệt dạng gel. Nhờ đó, tế bào không bị mất nước, màng tế bào giữ nguyên hình dạng và sự sống bên trong được bảo tồn tuyệt đối an toàn!
```

### scene04 — TRÁI TIM NGỪNG ĐẬP 0 NHỊP SUỐT 7 THÁNG MÙA ĐÔNG HÓA ĐÁ
*Thẻ chương:* ĐỒNG HỒ ĐẾM NGƯỢC CHẠM SỐ KHÔNG: CHẾT LÂM SÀNG HOÀN TOÀN GIỮA MÙA ĐÔNG

*Badge:* `CHẾT LÂM SÀNG` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene04_p0.wav` (390 ký tự) · mood `don_dap`

```text
Và bây giờ, kim đồng hồ đếm ngược sinh tồn hai mươi bốn giờ chính thức chạm mốc số không tử thần! Khi màn đêm vùng cực buông xuống và nhiệt độ không khí bên ngoài tụt sâu từ âm mười hai độ C, âm mười sáu độ C cho đến âm hai mươi độ C, quá trình đông cứng toàn thân của chú ếch bước vào giai đoạn quyết định. Dòng máu chứa đầy siro đường trở nên đặc quánh như mật mía rồi ngưng tụ hoàn toàn.
```
**Part 1** → `audio/vs/scene04_p1.wav` (308 ký tự) · mood `don_dap`

```text
Trái tim bé bỏng của chú ếch gỗ đập chậm dần từng nhịp: Từ một trăm nhịp một phút xuống năm mươi nhịp, rồi mười nhịp, năm nhịp... và rồi chiếc van tim cuối cùng khép lại. Nhịp tim dừng hẳn ở con số không tròn trĩnh! Không còn một giọt máu nào được bơm đi nuôi cơ thể, hệ tuần hoàn tê liệt một trăm phần trăm!
```
**Part 2** → `audio/vs/scene04_p2.wav` (175 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Cốc cốc cốc! Bác ếch gỗ ơi còn nghe thấy em nói gì không đấy? Chân tay bác cứng đơ rồi, em gõ thử cái que vào bụng bác nghe kêu cộp cộp giòn tan như gõ vào hòn đá cuội vậy nè!
```
**Part 3** → `audio/vs/scene04_p3.wav` (567 ký tự) · mood `hao_hung`

```text
[surprise-oh] Không còn một nhịp tim nào đập trong lồng ngực! Hai lá phổi ngừng phập phồng co bóp hoàn toàn, không có một phân tử khí oxy nào được hít vào hay thải ra! Nếu bạn gắn một bộ cảm biến điện não đồ siêu nhạy lên hộp sọ của chú ếch lúc này, chiếc kim ghi nhận tín hiệu sẽ chỉ vẽ ra một đường chân trời thẳng tắp phẳng lì: Không còn bất kỳ xung điện thần kinh nào được truyền đi giữa các tế bào não! Xét theo mọi tiêu chuẩn và định nghĩa y khoa khắt khe nhất của con người, chú ếch gỗ lúc này đã bước vào trạng thái chết lâm sàng toàn diện một trăm phần trăm!
```
**Part 4** → `audio/vs/scene04_p4.wav` (394 ký tự) · mood `tram_bi_an`

```text
Hãy quan sát diện mạo bên ngoài của chú ếch lúc này: Đôi mắt của nó đã chuyển sang màu đục ngầu và đông cứng hệt như hai viên bi ve bằng thủy tinh. Cơ bắp toàn thân cứng như thép nguội, các khớp xương chân không thể bẻ cong. Nếu bạn nhấc chú ếch lên và thả rơi từ độ cao ba mươi phân xuống mặt băng, nó sẽ nảy tưng tưng phát ra âm thanh côm cốp vang dội như một viên sỏi cuội lăn lóc ven đường!
```
**Part 5** → `audio/vs/scene04_p5.wav` (456 ký tự) · mood `tram_bi_an`

```text
Trong nghiên cứu đột phá xuất bản năm hai ngàn không trăm mười bốn trên Tạp chí Sinh học Thực nghiệm, tiến sĩ Đôn Lác-xơn tại Viện Sinh học Bắc Cực thuộc Đại học A-lát-xka Fairbanks đã chứng minh rằng: Những cá thể Ếch Gỗ Bắc Cực hoang dã có thể duy trì trạng thái đóng băng hóa đá, tim ngừng đập hoàn toàn này liên tục suốt bảy tháng, tức là hơn hai trăm ngày đêm ròng rã giữa mùa đông vùng cực mà không hề chịu bất kỳ di chứng tổn thương nào khi rã đông!
```

### scene05 — TRÁI TIM TỰ RÃ ĐÔNG VÀ TỰ ĐẬP LẠI MÀ KHÔNG CẦN MÁY SỐC ĐIỆN
*Thẻ chương:* ÁNH NẮNG MÙA XUÂN CHẠM TỚI: PHÉP MÀU HỒI SINH KHÔNG CẦN SỐC ĐIỆN

*Badge:* `KỲ TÍCH HỒI SINH` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene05_p0.wav` (394 ký tự) · mood `don_dap`

```text
Bảy tháng mùa đông dài đằng đẵng cuối cùng cũng trôi qua. Khi tháng tư và tháng năm gõ cửa cánh rừng Bắc Cực, những tia nắng ấm áp đầu tiên của mùa xuân bắt đầu len lỏi qua các tán cây thông, làm tan chảy lớp tuyết dày trắng xóa bên trên mặt đất. Nước tuyết tan nhỏ từng giọt róc rách, thấm dần xuống lớp thảm rêu và lá mục ẩm ướt, nơi viên đá ếch gỗ đang nằm im lìm suốt hơn hai trăm ngày đêm.
```
**Part 1** → `audio/vs/scene05_p1.wav` (463 ký tự) · mood `don_dap`

```text
Và ngay tại giây phút này, một trong những kỳ quan sinh học ngoạn mục nhất hành tinh chính thức bắt đầu vận hành: Quy trình rã đông thần tốc từ trong ra ngoài! Ở các loài động vật có vú, nếu bị đóng băng rồi đem sưởi ấm, cơ thể sẽ rã đông từ bề mặt da bên ngoài vào trong, khiến các mô bên ngoài ấm lên và đòi hỏi oxy trong khi trái tim bên trong vẫn còn là khối băng đông cứng, dẫn đến tử vong ngay tức khắc. Nhưng ếch gỗ thì sở hữu quy luật hoàn toàn ngược lại!
```
**Part 2** → `audio/vs/scene05_p2.wav` (177 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Thình thịch! Thình thịch! Cảm ơn bác mặt trời mùa xuân nhé! Máy bơm sự sống trong lồng ngực em đã khởi động lại trơn tru rồi nè, chuẩn bị xả van cho máu ấm chạy khắp người thôi!
```
**Part 3** → `audio/vs/scene05_p3.wav` (435 ký tự) · mood `hao_hung`

```text
[surprise-oh] Trái tim nằm sâu trong lồng ngực chú ếch chính là cơ quan đầu tiên được rã đông và tan chảy hoàn toàn! Không cần bất kỳ một cú sốc điện khử rung tim nào từ bác sĩ cấp cứu, các tế bào cơ tim của ếch gỗ tự động phát ra những xung điện sinh học tự nhiên. Ban đầu là một nhịp co bóp yếu ớt, rồi nhịp thứ hai, nhịp thứ ba... Từng nhịp đập bắt đầu dồn dập và mạnh mẽ trở lại, khôi phục dòng chảy tuần hoàn huyết áp khắp cơ thể!
```
**Part 4** → `audio/vs/scene05_p4.wav` (399 ký tự) · mood `tram_bi_an`

```text
Dòng máu ấm nóng giàu đường gờ-lu-cô-zơ được trái tim bơm đi khắp nơi, nhanh chóng làm tan chảy lớp băng bao quanh phổi, gan và thận. Chỉ trong vòng một đến hai giờ đồng hồ sau đó, hai lá phổi bắt đầu phập phồng hít thở trở lại từng luồng không khí trong lành của mùa xuân! Máu giàu oxy được đưa lên não bộ, kích hoạt hàng triệu tế bào thần kinh bừng tỉnh sau một giấc ngủ đông kéo dài nửa năm ròng!
```
**Part 5** → `audio/vs/scene05_p5.wav` (458 ký tự) · mood `tram_bi_an`

```text
Và điều kỳ diệu nhất là chỉ sau khoảng vài tiếng đồng hồ ngắn ngủi, lớp băng cứng ngắc ngoài các chi tan biến hoàn toàn. Chú ếch gỗ khẽ chớp đôi mắt trong veo, vươn vai cựa quậy bốn chân, rồi bất ngờ bật nhảy tanh tách từng bước dài đầy uy lực! Nó lao thẳng xuống những vũng nước băng tan đầu mùa để cất tiếng kêu ộp ộp vang dội gọi bạn tình, giành lấy vị trí đẻ trứng thuận lợi nhất trước khi bất kỳ loài sinh vật nào khác trong rừng kịp tỉnh giấc ngủ đông!
```

### scene06 — MỞ KHÓA BÍ MẬT BẢO QUẢN TẠNG NGƯỜI VÀ CÂU ĐỐ LINH THÚ TẬP 34
*Thẻ chương:* TỔNG KẾT HỒ SƠ SINH TỒN: TỪ QUÁI KIỆT BĂNG GIÁ ĐẾN GIẤC MƠ DU HÀNH VŨ TRỤ

*Badge:* `BÀI HỌC VÙNG CỰC` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene06_p0.wav` (368 ký tự) · mood `don_dap`

```text
Báo cáo tổng kết hồ sơ sinh tồn số ba mươi ba từ phóng viên hai mươi bốn giờ: Bảy tháng tim ngừng đập hoàn toàn, bảy mươi phần trăm lượng nước trong cơ thể hóa thành băng đá, sinh tồn ngoạn mục ở mức âm hai mươi độ C mà không hề suy suyển một tế bào nào! Quái Kiệt Băng Giá xứng đáng là một trong những kỳ tích tiến hóa vĩ đại nhất của sự sống trên hành tinh chúng ta!
```
**Part 1** → `audio/vs/scene06_p1.wav` (239 ký tự) · mood `don_dap`

```text
Nhưng giá trị của chú ếch gỗ bé nhỏ này không chỉ dừng lại ở thế giới tự nhiên hoang dã. Cơ chế sinh học độc nhất vô nhị của nó đang trở thành chiếc chìa khóa vàng mở ra cuộc cách mạng y học lớn nhất thế kỷ hai mươi mốt dành cho nhân loại!
```
**Part 2** → `audio/vs/scene06_p2.wav` (187 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Bí kíp chống đông hóa đá của dòng họ nhà ếch chúng tôi xin kính tặng lại cho các bác sĩ và nhà khoa học loài người nhé! Nhớ nghiên cứu thành công để cứu thật nhiều bệnh nhân trên đời nha!
```
**Part 3** → `audio/vs/scene06_p3.wav` (495 ký tự) · mood `hao_hung`

```text
[surprise-oh] Các bạn có biết một sự thật đau lòng này không: Trong nền y học ghép tạng hiện đại, một quả tim hoặc một lá phổi người sau khi được hiến tặng chỉ có thể bảo quản lạnh trong thùng đá chuyên dụng tối đa từ bốn đến sáu tiếng đồng hồ! Sau khoảng thời gian ngắn ngủi đó, các mô tế bào sẽ hoại tử và không thể cấy ghép được nữa. Mỗi năm có hàng chục ngàn bệnh nhân trên toàn thế giới qua đời trong tuyệt vọng chỉ vì khoảng cách địa lý quá xa, không kịp vận chuyển tạng ghép đến phòng mổ!
```
**Part 4** → `audio/vs/scene06_p4.wav` (491 ký tự) · mood `tram_bi_an`

```text
Hiện nay, các nhà khoa học hàng đầu tại Đại học Harvard và Bệnh viện Đa khoa Massachusetts đang tích cực nghiên cứu tổng hợp các phân tử mầm đá và hợp chất cờ-rai-ô-prô-tếch-tần mô phỏng từ loài ếch gỗ. Mục tiêu tối thượng là có thể đưa các cơ quan nội tạng người vào trạng thái đông lạnh sâu an toàn suốt nhiều tuần, thậm chí nhiều tháng trời mà không bị tổn thương tế bào! Khi công nghệ này thành công, nó sẽ tạo ra những ngân hàng nội tạng toàn cầu, cứu sống hàng triệu sinh mạng mỗi năm!
```
**Part 5** → `audio/vs/scene06_p5.wav` (699 ký tự) · mood `tram_bi_an`

```text
Và xa hơn nữa, đó chính là giấc mơ đưa các phi hành gia tương lai vào trạng thái ngủ đông sâu kéo dài hàng bao thế kỷ để thực hiện những chuyến du hành không gian xuyên qua các dải ngân hà xa xôi! Còn bây giờ, chương trình xin gửi tới các bạn câu đố hóc búa để hé lộ nhân vật chính của Tập ba mươi tư: Sinh vật nào sở hữu tỷ lệ kích thước bộ não so với cơ thể tương đương loài tinh tinh, biết tự uốn cong que sắt làm lưỡi câu bắt ấu trùng, và đặc biệt có thể ghi nhớ chính xác khuôn mặt của kẻ thù suốt năm năm trời để truyền lại cho đàn con cháu đời sau tiếp tục báo thù? Hãy để lại câu trả lời của bạn dưới phần bình luận, bấm like và đăng ký kênh để không bỏ lỡ những thước phim kỳ thú tiếp theo!
```

### Shorts → `audio/vs/shorts.wav`

```text
Cảnh báo sinh tồn vùng cực âm hai mươi độ C! [surprise-oh] Tại sao loài ếch tí hon này có thể để tim ngừng đập hoàn toàn suốt bảy tháng mùa đông rồi tự rã đông bật nhảy sống dậy? Đây là Ếch Gỗ Bắc Cực, Quái Kiệt Băng Giá của xứ sở A-lát-xka! Khi mùa đông ập đến, thay vì trốn sâu dưới lòng đất, nó ở lì trên mặt đất và chủ động để cơ thể mình bị đóng băng! Một loại protein tạo mầm đá đặc biệt ép sáu mươi lăm đến bảy mươi phần trăm lượng nước trong cơ thể nó hóa thành băng đá ngoại bào. Để tế bào không bị xé rách, lá gan của nó lập tức phình to, bơm một lượng đường gờ-lu-cô-zơ siêu đậm đặc gấp ba trăm lần vào bên trong từng tế bào như siro chống đông sinh học! Kết quả: Trái tim ngừng đập hoàn toàn ở mức không nhịp một phút. Máu ngừng chảy, sóng não phẳng lì, cơ thể cứng như đá gõ côm cốp suốt hai trăm ngày! Về mặt y học, nó đã chết lâm sàng một trăm phần trăm! Thế nhưng khi ánh nắng mùa xuân rọi xuống, trái tim tự rã đông đầu tiên, tự động đập lại mà không cần sốc điện, và chỉ vài tiếng sau chú ếch đã bật dậy nhảy tanh tách đi tìm bạn tình! Một kiệt tác hồi sinh đang mở ra cuộc cách mạng bảo quản tạng ghép cho loài người!
```

**Whisper prompt:** `Ếch Gỗ Bắc Cực, Quái Kiệt Băng Giá, Lithobates sylvaticus, Rana sylvatica, Kenneth Storey, Jack Costanzo, Richard Lee, Don Larson, Alaska, Glucose, Glycogen, Urea, Urê, Cryoprotectant, Ice-nucleating proteins, mầm đá, -20°C, -16°C, -2°C, 0 nhịp/phút, 7 tháng, 200 ngày, 70%, 65%, 300 lần, 100 lần, 5-7cm, 8-15g, 4-6 tiếng, Quạ Đen, Tập 33, Tập 34`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| âm hai mươi độ C | -20°C |
| Âm hai mươi độ C | -20°C |
| âm mười sáu độ C | -16°C |
| Âm mười sáu độ C | -16°C |
| âm mười lăm độ C | -15°C |
| âm mười hai độ C | -12°C |
| âm năm độ C | -5°C |
| âm hai độ C | -2°C |
| Âm hai độ C | -2°C |
| âm một đến âm hai độ C | -1°C đến -2°C |
| không độ C | 0°C |
| Không độ C | 0°C |
| bảy tháng | 7 tháng |
| Bảy tháng | 7 tháng |
| tám tháng | 8 tháng |
| hai trăm ngày | 200 ngày |
| Hai trăm ngày | 200 ngày |
| ba trăm lần | 300 lần |
| Ba trăm lần | 300 lần |
| một trăm đến ba trăm lần | 100-300 lần |
| một trăm lần | 100 lần |
| bảy mươi phần trăm | 70% |
| Bảy mươi phần trăm | 70% |
| sáu mươi lăm đến bảy mươi phần trăm | 65-70% |
| sáu mươi lăm phần trăm | 65% |
| năm mươi phần trăm | 50% |
| không nhịp một phút | 0 nhịp/phút |
| Không nhịp một phút | 0 nhịp/phút |
| mười nhịp một phút | 10 nhịp/phút |
| năm mươi nhịp một phút | 50 nhịp/phút |
| một trăm nhịp một phút | 100 nhịp/phút |
| năm đến bảy xăng-ti-mét | 5-7cm |
| Năm đến bảy xăng-ti-mét | 5-7cm |
| tám đến mười lăm gam | 8-15g |
| Tám đến mười lăm gam | 8-15g |
| bốn đến sáu tiếng | 4-6 tiếng |
| Bốn đến sáu tiếng | 4-6 tiếng |
| bốn đến sáu giờ | 4-6 giờ |
| vài tiếng | vài tiếng |
| hai mươi bốn giờ | 24h |
| Hai mươi bốn giờ | 24h |
| một trăm phần trăm | 100% |
| Một trăm phần trăm | 100% |
| mười nhịp | 10 nhịp |
| năm mươi nhịp | 50 nhịp |
| năm nhịp | 5 nhịp |
| một trăm nhịp | 100 nhịp |
| ba mươi phân | 30cm |
| thế kỷ hai mươi mốt | thế kỷ 21 |
| suốt năm năm | suốt 5 năm |
| năm năm | 5 năm |
| Năm một ngàn chín trăm chín mươi ba | Năm 1993 |
| Năm một ngàn chín trăm tám mươi tám | Năm 1988 |
| số ba mươi ba | số 33 |
| ba mươi ba | 33 |
| Ba mươi ba | 33 |
| tập ba mươi ba | Tập 33 |
| Tập ba mươi ba | Tập 33 |
| tập ba mươi tư | Tập 34 |
| Tập ba mươi tư | Tập 34 |
| năm một ngàn chín trăm tám mươi tám | năm 1988 |
| năm một ngàn chín trăm chín mươi | năm 1990 |
| năm một ngàn chín trăm chín mươi ba | năm 1993 |
| năm hai ngàn không trăm mười ba | năm 2013 |
| năm hai ngàn không trăm mười bốn | năm 2014 |
| A-lát-xka | Alaska |
| Li-thô-ba-tét xin-va-ti-cút | Lithobates sylvaticus |
| Kên-nét Xtô-ri | Kenneth Storey |
| Giắc Cốt-xtan-dô | Jack Costanzo |
| gờ-lu-cô-zơ | Glucose |
| gờ-ly-cô-gien | Glycogen |
| u-rê | Urea |
| cờ-rai-ô-prô-tếch-tần | Cryoprotectant |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · KHÁM PHÁ QUÁI KIỆT BĂNG GIÁ GIỮA BÃO TUYẾT ÂM 20 ĐỘ C Ở ALASKA · 126.3s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:06.6 (6.6s) | L02 | Báo cáo khẩn cấp từ hiện trường vùng cực! Phóng viên 24h đang có mặt trực tiếp tại cánh rừng lá kim taiga phủ đầy tuyết trắng |  | Hiện trường bão tuyết Alaska mù mịt: chú chim cánh cụt phóng viên hoạt hình mặc áo phao lông thú ấm áp, cầm micro phỏng vấn run rẩy giữa trời tuyết rơi trùm áo phao lông thú to sụ, hai tay run bần bật cầm micro truyền hình trực tiếp giữa cơn lốc tuyết trắng xóa. KHÔNG có chú Ếch Gỗ trong cảnh này. |
| b02 | 00:06.6–00:11.3 (4.6s) | L03 | ở tiểu bang Alaska, nơi chiếc nhiệt kế chuyên dụng vừa tụt thẳng đứng xuống mức -20°C! | **-20°C** · nhiệt độ bắc cực · L/340 · [0.45, 0.55] | Cận cảnh cột nhiệt kế sinh tồn cắm ngập trong đụn tuyết: Cột thủy ngân tụt dốc không phanh thẳng đứng xuống vạch âm hai mươi độ C đỏ rực với sương tuyết bám quanh. KHÔNG có chú Ếch Gỗ trong cảnh này. |
| b03 | 00:11.3–00:20.7 (9.4s) | L04 | Gió bắc cực gầm rú rít từng cơn lạnh buốt thấu tận xương tủy, làm cho lớp hơi nước thở ra vừa chạm vào không khí là đông đặc thành bụi băng li ti. Mọi nhánh cây ngọn cỏ đều phủ một lớp sương muối trắng |  | Minh họa cơn gió lốc vùng cực đóng băng mọi thứ: Luồng hơi nước thở ra từ miệng biến ngay thành chùm tinh thể băng rơi lả tả xuống mặt đất tuyết. KHÔNG có chú Ếch Gỗ trong cảnh này. |
| b04 | 00:20.7–00:31.4 (10.8s) | L05 | toát, và các mặt hồ nước ngọt sâu thẳm đã hóa thành những khối đá tảng hoa cương chẳng hề có một vết rạn nứt. Trong điều kiện thời tiết tử thần khắc nghiệt đến rợn người này, hãy quan sát cách các cư dân bản địa đối phó với mùa đông: |  | Mặt cắt hồ nước ngọt Bắc Cực: Toàn bộ tầng nước mặt đóng băng thành một khối đá hoa cương dày đặc, bên dưới các sinh vật đều chìm vào giấc ngủ im lìm. KHÔNG có chú Ếch Gỗ trong cảnh này. |
| b05 | 00:31.4–00:39.9 (8.5s) | L06 | Lũ gấu Bắc Cực to lớn phải cuộn tròn trong hang tuyết với lớp mỡ dày hàng chục xăng-ti-mét, đàn chim di cư thiện chiến đã vỗ cánh bay hàng ngàn cây số về phương Nam ấm áp từ ba tháng trước, |  | Bức tranh so sánh sinh tồn mùa đông: chú gấu Bắc Cực hoạt hình lông trắng to lớn mập mạp ngơ ngác, cầm một cành cây nhỏ gõ vào khối đá lạnh cuộn tròn trong hang tuyết ấm áp, phía trên là đàn chim di cư bay về phương Nam theo hình chữ V. KHÔNG có chú Ếch Gỗ trong cảnh này. |
| b06 | 00:39.9–00:46.6 (6.7s) | L07 | còn lũ chuột đồng thì rúc sâu cả mét dưới lòng đất nơi nhiệt độ còn giữ được trên mức 0°C. Alo phóng viên ơi! |  | Sơ đồ mặt cắt đất rừng taiga: Chú chuột đồng cuộn tròn trong chiếc tổ đào sâu cả mét dưới lòng đất ấm cúng, xung quanh chất đầy hạt dẻ dự trữ. KHÔNG có chú Ếch Gỗ trong cảnh này. |
| b07 | 00:46.6–00:56.2 (9.5s) | L08 | Tôi không có lông vũ, không có mỡ dày, cũng chẳng thèm đào hang sâu luôn! Chỉ có mỗi chiếc quần đùi da cóc mỏng manh này thôi thì có trụ nổi qua đêm nay không ạ? |  | Hình ảnh hài hước: chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) đứng trên tảng băng trôi, mặc mỗi chiếc quần đùi da cóc tí hon, hai tay chống nạnh cười toe toét nhìn về phía chú chim cánh cụt phóng viên hoạt hình mặc áo phao lông thú ấm áp, cầm micro phỏn |
| b08 | 00:56.2–01:05.9 (9.7s) | L09 | Ấy thế mà ngay dưới chân của chúng tôi, chỉ cách mặt tuyết chừng vài phân bên dưới lớp lá rụng và rêu mục mỏng manh, một sinh vật bé nhỏ lại đang thản nhiên chờ đón lưỡi hái tử thần của mùa đông! |  | Lớp lá rụng và rêu mục trên mặt đất rừng: chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) đang thong thả nằm tựa lưng vào hòn đá nhỏ, đắp chiếc chăn lá cây mỏng manh như đang đi nghỉ dưỡng. |
| b09 | 01:05.9–01:13.7 (7.8s) | L10 | Xin giới thiệu nhân vật chính của hồ sơ sinh tồn số 33: Ếch Gỗ Bắc Cực, mang danh pháp khoa học Lithobates sylvaticus, kẻ được giới |  | Tấm áp phích hồ sơ định danh vùng cực Cryo-Noir: Chân dung dũng mãnh của chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) với huy hiệu Quái Kiệt Băng Giá phát sáng rực rỡ trên nền tinh thể băng tuyết. |
| b10 | 01:13.7–01:21.8 (8.1s) | L54 | sinh học toàn cầu ngả mũ thán phục với biệt danh Quái Kiệt Băng Giá của muôn loài! Hãy nhìn vào những thông số trắc lượng cơ thể vô cùng khiêm tốn của sinh vật này: |  | Biểu đồ vinh danh Quái Kiệt Băng Giá: Chân dung chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) đứng trên bục vinh quang giữa các huân chương băng tuyết và cờ hiệu sinh tồn vùng cực. |
| b11 | 01:21.8–01:31.3 (9.5s) | L11 | Toàn thân chú ếch gỗ trưởng thành chỉ dài từ 5-7cm, và cân nặng vỏn vẹn từ 8-15g, nghĩa là chỉ nhẹ tương đương một quả nho nhỏ hoặc hai quả trứng cút luộc! | **5-7CM** · chiều dài cơ thể · L/330 · [0.4, 0.5]<br>**8-15G** · trọng lượng tí hon · R/410 · [0.65, 0.6] | Màn hình thước đo sinh trắc học vùng cực: Thước đo laser hiển thị chiều dài 5-7cm và chiếc cân đá mini hiện 8-15g của chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) bên cạnh một quả nho nhỏ. |
| b12 | 01:31.3–01:39.0 (7.8s) | L55 | Làn da của nó có màu nâu đồng pha lẫn xám của vỏ cây rừng, và điểm nhận dạng đặc trưng nhất chính là hai vệt sọc đen sẫm kéo dài từ khóe mắt vòng qua tai, |  | Bản vẽ phối màu ngụy trang vùng cực: Cận cảnh lớp da sần sùi màu nâu đồng của chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) hòa lẫn hoàn hảo vào thảm rêu rừng taiga và vỏ cây thông tuyết. |
| b13 | 01:39.0–01:47.8 (8.7s) | L12 | trông hệt như chiếc mặt nạ hiệp sĩ bí ẩn trong các bộ truyện tranh! Thế nhưng, điểm điên rồ và kỳ quặc nhất trong tập tính sinh học của chú ếch này là gì? Các loài ếch nhái thông thường |  | Cận cảnh đôi mắt của chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles): Hai vệt sọc đen sẫm kéo dài qua mắt như mặt nạ hiệp sĩ Zorro, đôi mắt tinh anh lấp lánh ánh nhìn kiên định trước bão tuyết. |
| b14 | 01:47.8–01:58.2 (10.4s) | L56 | khác ở xứ ôn đới bắt buộc phải lặn sâu xuống đáy bùn lầy của đáy hồ không đóng băng để sống sót qua mùa đông. Còn Ếch Gỗ Bắc Cực thì không! Nó không thể bơi xuống đáy hồ vì phổi và da của nó sẽ chết ngạt. Thay vào đó, nó |  | So sánh sinh thái: Các chú ếch xanh thông thường co ro rúc dưới đáy bùn hồ nước lạnh run rẩy, nhìn lên thán phục lòng dũng cảm của chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) trên mặt đất. |
| b15 | 01:58.2–02:06.3 (8.1s) | L13 | chọn cách ở lì ngay trên nền rừng lạnh giá, nơi nhiệt độ sẽ chạm đáy -20°C, và sẵn sàng để toàn bộ cơ thể mình bị đóng băng thành một tảng đá vô tri giác! |  | Đồng hồ sinh tồn đếm ngược: chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) khoanh tay ngồi thiền trên lớp rêu rừng taiga, xung quanh những bông tuyết bắt đầu phủ kín người biến thành một khối băng tảng. |

### scene02 · CƠ CHẾ TỰ ĐÓNG BĂNG 70% LƯỢNG NƯỚC CƠ THỂ MÀ KHÔNG RÁCH TẾ BÀO · 130.6s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:12.2 (12.2s) | L14 | Để thấy được sự phi thường của Quái Kiệt Băng Giá, trước hết chúng ta cần hiểu rõ vì sao đối với hầu hết mọi sinh vật trên Trái Đất, việc bị đóng băng đồng nghĩa với một bản án tử hình không thể đảo ngược! Khi nước nguyên chất chuyển từ thể lỏng sang thể rắn ở |  | Sơ đồ khoa học phân tử Cryo-Noir: Một giọt nước tinh khiết đang đóng băng, các phân tử nước kết tinh giãn nở và mọc ra những mũi gai băng nhọn hoắt như dao găm. KHÔNG có chú Ếch Gỗ trong cảnh này. |
| b02 | 00:12.2–00:24.9 (12.7s) | L57 | nhiệt độ dưới 0°C, thể tích của nó sẽ giãn nở đột ngột thêm khoảng chín phần trăm. Nguy hiểm hơn nữa, các tinh thể đá hình thành tự do trong môi trường sống sẽ phát triển thành những cấu trúc gai nhọn li ti, sắc bén hệt như hàng triệu lưỡi dao găm siêu nhỏ sắc lẹm! |  | Mô hình vật lý giãn nở thể tích: Khối băng trong suốt nở bung với các vết nứt rạn tỏa ra xung quanh, làm vỡ tung một ống nghiệm thủy tinh đo lường. KHÔNG có chú Ếch Gỗ trong cảnh này. |
| b03 | 00:24.9–00:34.3 (9.4s) | L15 | Nếu hiện tượng đóng băng vô kiểm soát này xảy ra bên trong cơ thể con người hay bất kỳ loài động vật nào khác, những mũi dao băng sắc nhọn đó sẽ lập tức đâm thủng lớp màng lipid mỏng manh của tế bào, xé toạc các vi mạch |  | Hình ảnh kính hiển vi mô phỏng tế bào thông thường: Những mũi gai băng sắc lẹm đâm rách toạc màng tế bào, dịch nội bào tràn ra ngoài gây hoại tử hoàn toàn. KHÔNG có chú Ếch Gỗ trong cảnh này. |
| b04 | 00:34.3–00:44.9 (10.5s) | L58 | máu trong tích tắc và phá nát toàn bộ cấu trúc nội tạng! Hậu quả là ngay khi vừa tan đá, các mô tế bào sẽ vỡ vụn và hoại tử hoàn toàn, dẫn đến cái chết gần như tức thì mà chẳng thiết bị y khoa nào có thể cứu vãn! |  | Cảnh báo hoại tử mô: Hình vẽ đồ họa vi phẫu thuật cho thấy các mao mạch bị tắc nghẽn và đóng băng đỏ rực dưới kính hiển vi điện tử. KHÔNG có chú Ếch Gỗ trong cảnh này. |
| b05 | 00:44.9–00:56.6 (11.7s) | L16 | Kính thưa các tinh thể đá mũi nhọn hung dữ! Tuyệt đối cấm bén mảng vào khoang tim và lá gan của tôi nhé! Ai muốn đóng băng thì xếp hàng ngay ngắn ra ngoài da và dưới bụng đứng hết cho tôi! |  | chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) hóa thân thành chú cảnh sát giao thông vùng cực tí hon, tay cầm gậy chỉ huy điều hướng các tinh thể băng xếp hàng rồng rắn đi ra phía ngoài da. |
| b06 | 00:56.6–01:06.0 (9.5s) | L17 | Và đó chính là lúc chiến thuật tạo mầm đá ngoại bào thần kỳ của chú ếch gỗ phát huy uy lực tối thượng! Năm 1993, nhóm nghiên cứu của tiến sĩ Jack Costanzo | **NĂM 1993** · công bố khoa học · L/350 · [0.45, 0.5] | Trang bìa công trình nghiên cứu khoa học năm 1993 của tiến sĩ Jack Costanzo, bên cạnh là mô hình 3D phân tử protein tạo mầm đá phát sáng màu lam ngọc. KHÔNG có chú Ếch Gỗ trong cảnh này. |
| b07 | 01:06.0–01:13.5 (7.5s) | L74 | tại Đại học Miami đã công bố một phát hiện chấn động trên Tạp chí Sinh lý học Hoa Kỳ: Trong huyết tương và dịch ngoại bào của Ếch Gỗ Bắc Cực chứa |  | Viện nghiên cứu sinh học Đại học Miami: Nhóm các nhà khoa học đang hào hứng quan sát mẫu huyết tương của chú ếch chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) dưới kính hiển vi điện tử. KHÔNG có chú Ếch Gỗ trong cảnh này. |
| b08 | 01:13.5–01:18.1 (4.5s) | L59 | một họ protein chuyên biệt mang tên protein tạo mầm đá! Khi nhiệt độ môi trường |  | Cận cảnh chuỗi protein tạo mầm đá: Những hạt phân tử protein hình cầu màu lam ngọc phát sáng, đang hút các phân tử nước li ti lại gần tạo thành mạng lưới tinh thể có trật tự. KHÔNG có chú Ếch Gỗ trong cảnh này. |
| b09 | 01:18.1–01:27.9 (9.8s) | L18 | vừa hạ xuống mức -1°C đến -2°C, những protein này lập tức đóng vai trò như những thỏi nam châm định hướng, kích thích các phân tử nước bên ngoài tế bào kết tinh thành đá trước tiên! | **-1°..-2°C** · ngưỡng mầm đá · R/360 · [0.55, 0.5] | Bảng đo vi khí hậu tế bào: Khi nhiệt độ chạm ngưỡng -1°C đến -2°C, các protein mầm đá hoạt động như nam châm gom các tinh thể băng về khoang ngoại bào. KHÔNG có chú Ếch Gỗ trong cảnh này. |
| b10 | 01:27.9–01:42.8 (14.9s) | L19 | Thay vì để băng đá xuất hiện ngẫu nhiên và bừa bãi, cơ thể của ếch gỗ chủ động kiểm soát tuyệt đối vị trí đóng băng: Băng chỉ được phép hình thành ở các khoang trống nằm ngoài màng tế bào, trong ổ bụng, dưới lớp da lưng và xung quanh các bó cơ bắp! Khi nước ở bên ngoài đóng băng, hiện tượng thẩm thấu tự nhiên |  | Bản đồ giải phẫu cắt lớp cơ thể chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles): Băng đá đóng thành lớp giáp bảo vệ dày ở ổ bụng và dưới da, trong khi các cơ quan tim gan bên trong vẫn an toàn nguyên vẹn. |
| b11 | 01:42.8–01:54.9 (12.1s) | L20 | sẽ rút dần nước lỏng từ bên trong tế bào ra ngoài, giống như việc bạn rút ruột nước ra khỏi một quả bóng bay để nó xẹp lại một cách có tính toán. Khối lượng băng hình thành bên ngoài tế bào này tăng dần lên một cách đáng kinh ngạc, cho đến khi chiếm |  | Mô hình minh họa thẩm thấu nước: Tế bào nội bào nhẹ nhàng co lại một cách có kiểm soát như quả bóng xẹp bớt nước, nhường chỗ cho lớp băng ngoài khoang đệm. |
| b12 | 01:54.9–01:59.4 (4.5s) | L21 | tới 65-70% tổng dung tích nước của toàn bộ cơ thể! Hãy tưởng | **70% BĂNG** · nước hóa băng đá · L/340 · [0.4, 0.55] | Biểu đồ tròn tỷ lệ thể tích nước cơ thể chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles): Mảng màu xanh lam ngọc chiếm trọn 70% tổng lượng nước hóa thành giáp băng bao bọc bên ngoài. chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vù |
| b13 | 01:59.4–02:10.6 (11.2s) | L22 | tượng: 70% cơ thể của bạn biến thành băng cứng ngắc như một hòn đá hoa cương, nhưng nhờ có cơ chế điều hướng mầm đá tài tình, chẳng có tinh thể nhọn nào được phép chạm vào không gian thiêng liêng bên trong tế bào! |  | chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) trong tư thế siêu anh hùng khoác bộ giáp băng tinh thể trong suốt óng ánh, tự tin mỉm cười trước bão tuyết vùng cực. |

### scene03 · GAN PHÌNH TO BƠM GLUCOSE SIÊU ĐẬM ĐẶC GẤP 300 LẦN CHỐNG ĐÔNG TẾ BÀO · 122.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.5 (9.5s) | L23 | Thế nhưng, một bài toán hóc búa khác lập tức xuất hiện ngay tại đây! Nếu nước bên ngoài tế bào liên tục bị hút đi để tạo thành lớp giáp băng, chẳng phải áp suất thẩm thấu sẽ vắt kiệt từng giọt nước bên trong tế bào, |  | Tế bào sinh học đang đối mặt nguy cơ co rúm: Áp suất thẩm thấu đè nặng lên màng tế bào, chiếc còi báo động khẩn cấp màu đỏ nhấp nháy liên hồi. KHÔNG có chú Ếch Gỗ trong cảnh này. |
| b02 | 00:09.5–00:19.4 (9.9s) | L60 | khiến tế bào bị mất nước nghiêm trọng, teo tóp lại thành một mảnh vụn khô cằn và chết vì suy kiệt hay sao? Đúng là như vậy, nếu không có vũ khí bí mật thứ hai mang tên siêu chất chống đông sinh học! |  | Hình ảnh mô phỏng quả bóng bay tế bào bị xì hơi teo tóp nhăn nhúm vì mất nước, biểu cảm nhân vật tế bào hoạt hình méo xệch kêu cứu. KHÔNG có chú Ếch Gỗ trong cảnh này. |
| b03 | 00:19.4–00:31.6 (12.2s) | L24 | Ngay vào khoảnh khắc những cảm biến nhiệt độ trên da của ếch cảm nhận được tinh thể băng chạm vào lớp biểu bì, một tín hiệu báo động đỏ cấp quốc gia được phát đi dọc theo tủy sống, truyền thẳng đến cơ quan nội tạng quan trọng nhất: Nhà máy hóa chất lá gan! |  | Hệ thống thần kinh cảm giác của chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles): Làn da chạm vào băng đá bắn ra tia sét tín hiệu sinh học chạy dọc sống lưng về trung tâm chỉ huy lá gan. |
| b04 | 00:31.6–00:42.2 (10.6s) | L25 | Báo cáo chỉ huy trưởng! Bộ phận gan đã nhận lệnh báo động khẩn cấp! Kho dự trữ đường năng lượng đang mở hết van xả lũ, chuẩn bị biến toàn bộ máu thành siro ngọt lịm đây! |  | Hình ảnh hài hước bên trong nhà máy lá gan: chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) đội mũ thuyền trưởng gạt cần van xả lũ màu vàng cam, mở toang các bồn chứa siro đường mật mía ngọt lịm. |
| b05 | 00:42.2–00:56.2 (14.0s) | L26 | Những nghiên cứu đột phá mang tính lịch sử của vợ chồng giáo sư Kenneth Storey từ năm 1988 đã hé lộ một kỳ quan chuyển hóa sinh hóa: Trong suốt mùa thu, lá gan của ếch gỗ tích lũy một lượng đường phức Glycogen khổng lồ, khiến lá gan phình | **NĂM 1988** · nghiên cứu Storey · L/350 · [0.45, 0.5] | Chân dung giáo sư Kenneth Storey trên bìa tạp chí khoa học năm 1988, bên cạnh là biểu đồ lá gan chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) phình to gấp nhiều lần chứa đầy kho Glycogen. |
| b06 | 00:56.2–01:07.8 (11.6s) | L61 | to chiếm tới mười phần trăm trọng lượng cơ thể. Và ngay khi quá trình đóng băng bắt đầu, lá gan này lập tức kích hoạt enzyme phân giải Glycogen với tốc độ tên lửa, biến toàn bộ thành đường đơn Glucose tự do! |  | Cân đo bên trong cơ thể Bio-Lab: Chiếc cân điện tử cân lá gan màu nâu đỏ phình to bằng một phần mười cơ thể chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles), các khoang chứa đầy ắp những hạt Glycogen vàng lấp lánh. |
| b07 | 01:07.8–01:19.8 (12.1s) | L27 | Chỉ trong vòng vài giờ đồng hồ ngắn ngủi, lượng đường Glucose được bơm ồ ạt vào dòng máu, đẩy nồng độ đường huyết của chú ếch vọt lên gấp từ 100-300 lần so với mức bình thường! Để dễ hình dung độ kinh hoàng của con số này: | **300 LẦN** · glucose chống đông · R/340 · [0.65, 0.55] | Đồng hồ đo nồng độ đường huyết điện tử: Kim chỉ số vọt từ mức bình thường bay thẳng lên con số 300 lần với cột thủy tinh phát sáng màu vàng mật ong rực rỡ. |
| b08 | 01:19.8–01:27.4 (7.5s) | L28 | Nếu nồng độ đường huyết của một người trưởng thành chỉ cần tăng lên gấp ba đến bốn lần bình thường, người đó đã rơi vào trạng thái hôn mê tiểu đường cấp tính và tử vong nếu |  | Hình ảnh so sánh y học: Bệnh nhân người sốt sắng trước kết quả tiểu đường cao, trong khi chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) đang thong thả nhâm nhi cốc siro đường vàng ươm cười khoái chí. |
| b09 | 01:27.4–01:34.9 (7.5s) | L62 | không được tiêm insulin cấp cứu! Nhưng với Quái Kiệt Băng Giá, nồng độ đường gấp 300 lần lại chính là chiếc phao cứu sinh vĩ đại nhất của nó! |  | Bệnh viện dã chiến hài hước: Chiếc xe cứu thương vùng cực nhấp nháy đèn còi với ống tiêm insulin to đùng, trong khi chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) đứng bên cạnh vỗ bụng cười tự hào. |
| b10 | 01:34.9–01:48.0 (13.1s) | L29 | Song song với đường Glucose, thận của ếch gỗ cũng giữ lại hợp chất Urea ở nồng độ cực cao. Hai hợp chất này hòa quyện tạo thành một dung dịch siro chống đông Cryoprotectant tự nhiên siêu đậm đặc, thấm đẫm vào từng milimet khối chất nguyên sinh bên trong tế bào. |  | Mô hình phân tử Cryoprotectant: Các phân tử Glucose hình lục giác đan xen với hạt Urea bao bọc lấy các phân tử protein nội bào như chiếc khiên đệm siêu mềm. KHÔNG có chú Ếch Gỗ trong cảnh này. |
| b11 | 01:48.0–02:02.2 (14.2s) | L30 | Siro này hạ điểm đông đặc của dịch nội bào xuống rất sâu, khiến nước bên trong tế bào không thể đóng băng thành đá được nữa mà vẫn duy trì ở trạng thái sền sệt dạng gel. Nhờ đó, tế bào không bị mất nước, màng tế bào giữ nguyên hình dạng và sự sống bên trong được bảo tồn tuyệt đối an toàn! |  | Cận cảnh chất nguyên sinh bên trong tế bào chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles): Dung dịch duy trì ở dạng thạch gel sánh mịn màng, không một tinh thể đá nào có thể kết tủa bên trong. |

### scene04 · TRÁI TIM NGỪNG ĐẬP 0 NHỊP SUỐT 7 THÁNG MÙA ĐÔNG HÓA ĐÁ · 113.6s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:13.2 (13.2s) | L31 | Và bây giờ, kim đồng hồ đếm ngược sinh tồn 24h chính thức chạm mốc số không tử thần! Khi màn đêm vùng cực buông xuống và nhiệt độ không khí bên ngoài tụt sâu từ -12°C, -16°C cho đến -20°C, quá trình đông cứng toàn thân của chú ếch | **24H** · đồng hồ sinh tồn · L/340 · [0.4, 0.45] | Băng giá phủ kín toàn cảnh rừng taiga: Đồng hồ đếm ngược sinh tồn 24h chạy về đúng con số 00:00:00, bão tuyết rít gào buốt lạnh âm hai mươi độ C. KHÔNG có chú Ếch Gỗ trong cảnh này. |
| b02 | 00:13.2–00:18.3 (5.1s) | L63 | bước vào giai đoạn quyết định. Dòng máu chứa đầy siro đường trở nên đặc quánh như mật mía rồi ngưng tụ hoàn toàn. |  | Bão tuyết màn đêm cực hàn: Cơn lốc xoáy tuyết xanh thẫm bao trùm toàn cảnh rừng taiga, những cột băng đá nhọn hoắt mọc lên từ mặt đất như rừng chông tuyết. |
| b03 | 00:18.3–00:32.7 (14.4s) | L32 | Trái tim bé bỏng của chú ếch gỗ đập chậm dần từng nhịp: Từ 100 nhịp/phút xuống 50 nhịp, rồi 10 nhịp, 5 nhịp... và rồi chiếc van tim cuối cùng khép lại. Nhịp tim dừng hẳn ở con số không tròn trĩnh! Không còn một giọt máu nào được bơm đi nuôi cơ thể, hệ tuần hoàn tê liệt 100%! | **100 NHỊP** · nhịp tim ban đầu · L/330 · [0.35, 0.5]<br>**0 NHỊP/P** · tim ngừng đập hẳn · R/410 · [0.65, 0.55] | Màn hình điện tâm đồ ECG theo dõi nhịp tim: Đồ thị nhịp tim từ 100 nhịp/phút tụt xuống 50 nhịp, 10 nhịp rồi tắt hẳn thành một đường chân trời phẳng lặng. |
| b04 | 00:32.7–00:43.3 (10.6s) | L33 | Cốc cốc cốc! Bác ếch gỗ ơi còn nghe thấy em nói gì không đấy? Chân tay bác cứng đơ rồi, em gõ thử cái que vào bụng bác nghe kêu cộp cộp giòn tan như gõ vào hòn đá cuội vậy nè! |  | chú gấu Bắc Cực hoạt hình lông trắng to lớn mập mạp ngơ ngác, cầm một cành cây nhỏ gõ vào khối đá lạnh tò mò ngồi xổm bên tảng rêu tuyết, dùng que gỗ nhỏ gõ vào người chú ếch chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) đã đông cứng, phát ra âm thanh côm  |
| b05 | 00:43.3–00:58.0 (14.7s) | L34 | Không còn một nhịp tim nào đập trong lồng ngực! Hai lá phổi ngừng phập phồng co bóp hoàn toàn, không có một phân tử khí oxy nào được hít vào hay thải ra! Nếu bạn gắn một bộ cảm biến điện não đồ siêu nhạy lên hộp sọ của chú ếch lúc này, chiếc kim ghi nhận tín hiệu sẽ chỉ vẽ ra |  | Màn hình điện não đồ EEG của bác sĩ cú mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắng và cầm bảng theo dõi thông số sinh tồn: Chiếc kim vạch ra đường thẳng tắp 0% sóng não, bên cạnh là biểu tượng trái tim bị đóng băng hoàn toàn nhân vật trái tim hoạt hình màu đỏ đội mũ len nhỏ bị bọc trong tinh thể băng xanh lam trong suốt. |
| b06 | 00:58.0–01:04.0 (6.0s) | L64 | một đường chân trời thẳng tắp phẳng lì: Không còn bất kỳ xung điện thần kinh nào được truyền đi giữa các tế bào não! |  | Bản ghi điện não đồ EEG phóng đại: Màn hình oscilloscope màu xanh lá cây hiện đường chân trời thẳng tắp 0Hz phẳng lì, chiếc bút đo nằm im không một dao động. KHÔNG có chú Ếch Gỗ trong cảnh này. |
| b07 | 01:04.0–01:14.7 (10.7s) | L75 | Xét theo mọi tiêu chuẩn và định nghĩa y khoa khắt khe nhất của con người, chú ếch gỗ lúc này đã bước vào trạng thái chết lâm sàng toàn diện 100%! Hãy quan sát diện mạo bên ngoài của chú ếch lúc này: | **100%** · chết lâm sàng y học · R/350 · [0.6, 0.5] | Bác sĩ cú mèo bác sĩ cú mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắng và cầm bảng theo dõi thông số sinh tồn cầm chiếc búa phản xạ y tế gõ vào đầu gối chú ếch chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) đã đông cứng, lắc đầu xác nhận chết lâm sàng |
| b08 | 01:14.7–01:24.6 (9.8s) | L35 | Đôi mắt của nó đã chuyển sang màu đục ngầu và đông cứng hệt như hai viên bi ve bằng thủy tinh. Cơ bắp toàn thân cứng như thép nguội, các khớp xương chân không thể bẻ cong. Nếu bạn nhấc chú ếch lên và thả |  | Cận cảnh khuôn mặt đông đá của chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles): Đôi mắt đục ngầu như hai hòn bi ve thủy tinh, toàn thân cứng như thép nguội đọng lớp sương tuyết lấp lánh. |
| b09 | 01:24.6–01:35.8 (11.2s) | L36 | rơi từ độ cao 30cm xuống mặt băng, nó sẽ nảy tưng tưng phát ra âm thanh côm cốp vang dội như một viên sỏi cuội lăn lóc ven đường! Trong nghiên cứu đột phá xuất bản năm 2014 trên Tạp chí Sinh học Thực nghiệm, | **30CM** · thử nghiệm rơi · L/360 · [0.45, 0.5] | Minh họa chú ếch đông đá rơi từ độ cao 30cm xuống mặt băng nảy tưng tưng côm cốp mà không hề trầy xước mô mềm trước ánh mắt thảng thốt của chú gấu Bắc Cực hoạt hình lông trắng to lớn mập mạp ngơ ngác, cầm một cành cây nhỏ gõ vào khối đá lạnh. |
| b10 | 01:35.8–01:44.9 (9.1s) | L37 | tiến sĩ Đôn Lác-xơn tại Viện Sinh học Bắc Cực thuộc Đại học Alaska Fairbanks đã chứng minh rằng: Những cá thể Ếch Gỗ Bắc Cực hoang dã có thể duy trì trạng thái đóng băng hóa đá, |  | Tấm lịch mùa đông Bắc Cực lật trang liên tục từ tháng 10 đến tháng 4: Biểu đồ thời gian 7 tháng tương đương 200 ngày đêm ngủ đông hóa đá của chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles). |
| b11 | 01:44.9–01:53.6 (8.6s) | L65 | tim ngừng đập hoàn toàn này liên tục suốt 7 tháng, tức là hơn 200 ngày đêm ròng rã giữa mùa đông vùng cực mà không hề chịu bất kỳ di chứng tổn thương nào khi rã đông! | **7 THÁNG** · thời gian đông đá · L/330 · [0.35, 0.5]<br>**200 NGÀY** · chịu cực lạnh · R/410 · [0.65, 0.55] | Vũ trụ thời gian 4 mùa Bắc Cực: Hình ảnh quả cầu Trái Đất quay tròn qua các mùa tuyết phủ, chú ếch chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) hóa đá nằm im bất động thách thức dòng chảy thời gian. |

### scene05 · TRÁI TIM TỰ RÃ ĐÔNG VÀ TỰ ĐẬP LẠI MÀ KHÔNG CẦN MÁY SỐC ĐIỆN · 114.3s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:11.5 (11.5s) | L38 | 7 tháng mùa đông dài đằng đẵng cuối cùng cũng trôi qua. Khi tháng tư và tháng năm gõ cửa cánh rừng Bắc Cực, những tia nắng ấm áp đầu tiên của mùa xuân bắt đầu len lỏi qua các tán cây thông, làm tan chảy lớp tuyết dày trắng xóa bên trên mặt đất. |  | Ánh bình minh mùa xuân tháng 4 rọi xuống cánh rừng Bắc Cực: Băng tuyết bắt đầu tan chảy, những mầm rêu xanh non nhú lên khỏi mặt đất ẩm ướt. KHÔNG có chú Ếch Gỗ trong cảnh này. |
| b02 | 00:11.5–00:18.5 (7.0s) | L66 | Nước tuyết tan nhỏ từng giọt róc rách, thấm dần xuống lớp thảm rêu và lá mục ẩm ướt, nơi viên đá ếch gỗ đang nằm im lìm suốt hơn 200 ngày đêm. |  | Mùa xuân rã đông cận cảnh: Từng giọt nước tuyết trong suốt lấp lánh rơi róc rách xuống thảm rêu xanh tươi, những bông hoa tuyết màu vàng nở rộ đón nắng mai. KHÔNG có chú Ếch Gỗ trong cảnh này. |
| b03 | 00:18.5–00:29.4 (10.9s) | L39 | Và ngay tại giây phút này, một trong những kỳ quan sinh học ngoạn mục nhất hành tinh chính thức bắt đầu vận hành: Quy trình rã đông thần tốc từ trong ra ngoài! Ở các loài động vật có vú, nếu bị đóng băng rồi đem sưởi ấm, cơ thể sẽ rã |  | Sơ đồ so sánh cơ chế rã đông: Động vật có vú rã đông từ ngoài vào trong gây tổn thương tim, trong khi chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) rã đông từ sâu trong tâm thất ra ngoài. chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính b |
| b04 | 00:29.4–00:41.2 (11.8s) | L67 | đông từ bề mặt da bên ngoài vào trong, khiến các mô bên ngoài ấm lên và đòi hỏi oxy trong khi trái tim bên trong vẫn còn là khối băng đông cứng, dẫn đến tử vong ngay tức khắc. Nhưng ếch gỗ thì sở hữu quy luật hoàn toàn ngược lại! |  | Sơ đồ nhiệt bức xạ: Sơ đồ nhiệt chụp cắt lớp cho thấy nhiệt lượng lan tỏa từ bên ngoài vào trong của một chú chuột, đối lập với nhiệt lượng tỏa ra từ tim của chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles). |
| b05 | 00:41.2–00:50.8 (9.7s) | L40 | Thình thịch! Thình thịch! Cảm ơn bác mặt trời mùa xuân nhé! Máy bơm sự sống trong lồng ngực em đã khởi động lại trơn tru rồi nè, chuẩn bị xả van cho máu ấm chạy khắp người thôi! |  | nhân vật trái tim hoạt hình màu đỏ đội mũ len nhỏ bị bọc trong tinh thể băng xanh lam trong suốt bên trong lồng ngực chú ếch bắt đầu tỏa ra ánh hào quang ấm áp màu vàng cam, lớp băng tan chảy thành nước và trái tim bắt đầu co bóp đập lại rộn ràng. |
| b06 | 00:50.8–01:01.5 (10.6s) | L41 | Trái tim nằm sâu trong lồng ngực chú ếch chính là cơ quan đầu tiên được rã đông và tan chảy hoàn toàn! Không cần bất kỳ một cú sốc điện khử rung tim nào từ bác sĩ cấp cứu, các tế bào cơ tim của ếch gỗ tự động phát |  | Cận cảnh cơ tim tự phát xung điện sinh học: Không cần máy sốc điện, từng tế bào cơ tim tự phát ra tia năng lượng hồi sinh nhịp đập đầu tiên sau 7 tháng ngủ vùi. KHÔNG có chú Ếch Gỗ trong cảnh này. |
| b07 | 01:01.5–01:12.6 (11.2s) | L68 | ra những xung điện sinh học tự nhiên. Ban đầu là một nhịp co bóp yếu ớt, rồi nhịp thứ hai, nhịp thứ ba... Từng nhịp đập bắt đầu dồn dập và mạnh mẽ trở lại, khôi phục dòng chảy tuần hoàn huyết áp khắp cơ thể! |  | Tia sét sinh học phục sinh: Một tia chớp nhỏ màu vàng cam lóe lên ngay tại tâm thất của trái tim chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles), phá vỡ lớp vỏ băng mỏng cuối cùng để bơm nước màu trở lại. |
| b08 | 01:12.6–01:19.4 (6.8s) | L42 | Dòng máu ấm nóng giàu đường Glucose được trái tim bơm đi khắp nơi, nhanh chóng làm tan chảy lớp băng bao quanh phổi, gan và thận. |  | Hệ tuần hoàn bừng sáng: Dòng nước màu ấm màu đỏ cam chở oxy và glucose lưu thông qua phổi, gan, thận làm tan biến hoàn toàn các khối băng bên trong cơ thể. chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực. |
| b09 | 01:19.4–01:32.0 (12.6s) | L43 | Chỉ trong vòng một đến hai giờ đồng hồ sau đó, hai lá phổi bắt đầu phập phồng hít thở trở lại từng luồng không khí trong lành của mùa xuân! Máu giàu oxy được đưa lên não bộ, kích hoạt hàng triệu tế bào thần kinh bừng tỉnh sau một giấc ngủ đông kéo dài nửa năm ròng! |  | Hai lá phổi của chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) phập phồng hít thở trở lại luồng không khí mùa xuân trong lành, não bộ bừng sáng hàng triệu tế bào thần kinh hoạt động nhộn nhịp. |
| b10 | 01:32.0–01:44.7 (12.6s) | L44 | Và điều kỳ diệu nhất là chỉ sau khoảng vài tiếng đồng hồ ngắn ngủi, lớp băng cứng ngắc ngoài các chi tan biến hoàn toàn. Chú ếch gỗ khẽ chớp đôi mắt trong veo, vươn vai cựa quậy bốn chân, rồi bất ngờ bật nhảy tanh tách từng bước dài đầy uy lực! |  | chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) chớp mắt trong veo, vươn vai cựa quậy rồi bật nhảy tanh tách từng bước dài dũng mãnh trên nền rừng mùa xuân rực rỡ hoa tuyết. chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực. |
| b11 | 01:44.7–01:54.3 (9.7s) | L45 | Nó lao thẳng xuống những vũng nước băng tan đầu mùa để cất tiếng kêu ộp ộp vang dội gọi bạn tình, giành lấy vị trí đẻ trứng thuận lợi nhất trước khi bất kỳ loài sinh vật nào khác trong rừng kịp tỉnh giấc ngủ đông! |  | Đầm lầy nước băng tan rộn rã: chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) đứng trên tảng đá cất tiếng kêu ộp ộp vang lừng gọi bạn tình, các đối thủ trong rừng ngơ ngác nhìn theo thán phục. |

### scene06 · MỞ KHÓA BÍ MẬT BẢO QUẢN TẠNG NGƯỜI VÀ CÂU ĐỐ LINH THÚ TẬP 34 · 122.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.2 (8.2s) | L46 | Báo cáo tổng kết hồ sơ sinh tồn số 33 từ phóng viên 24h: 7 tháng tim ngừng đập hoàn toàn, 70% lượng nước trong cơ thể hóa thành băng đá, |  | Bảng tổng kết hồ sơ sinh tồn số 33: Các chỉ số kỷ lục của chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) gồm 7 tháng tim 0 nhịp, 70% nước hóa đá và sống sót ở -20°C được vinh danh trang trọng. |
| b02 | 00:08.2–00:17.2 (9.1s) | L69 | sinh tồn ngoạn mục ở mức -20°C mà không hề suy suyển một tế bào nào! Quái Kiệt Băng Giá xứng đáng là một trong những kỳ tích tiến hóa vĩ đại nhất của sự sống trên hành tinh chúng ta! |  | Cúp vàng vinh danh sinh tồn Bắc Cực: Chiếc cúp vàng khắc hình chú ếch gỗ dũng mãnh đứng trên tảng băng trôi giữa tràng pháo tay của muôn loài động vật vùng cực. |
| b03 | 00:17.2–00:28.6 (11.3s) | L47 | Nhưng giá trị của chú ếch gỗ bé nhỏ này không chỉ dừng lại ở thế giới tự nhiên hoang dã. Cơ chế sinh học độc nhất vô nhị của nó đang trở thành chiếc chìa khóa vàng mở ra cuộc cách mạng y học lớn nhất thế kỷ 21 dành cho nhân loại! |  | Biểu tượng phòng thí nghiệm công nghệ y sinh tương lai: Mô hình phân tử chống đông của ếch gỗ được chiếu sáng hologram giữa các ống nghiệm hiện đại. KHÔNG có chú Ếch Gỗ trong cảnh này. |
| b04 | 00:28.6–00:40.7 (12.2s) | L48 | Bí kíp chống đông hóa đá của dòng họ nhà ếch chúng tôi xin kính tặng lại cho các bác sĩ và nhà khoa học loài người nhé! Nhớ nghiên cứu thành công để cứu thật nhiều bệnh nhân trên đời nha! Các bạn có |  | chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) trong trang phục giáo sư tí hon cầm cuộn bí kíp cổ truyền trao tặng cho các bác sĩ trong phòng mổ cứu người. |
| b05 | 00:40.7–00:44.3 (3.6s) | L70 | biết một sự thật đau lòng này không: Trong nền y học ghép tạng hiện đại, |  | Bệnh viện cấp cứu ghép tạng: Đồng hồ đếm ngược gấp gáp trên tường phòng mổ, các bác sĩ đang căng thẳng theo dõi chiếc thùng bảo quản tạng ghép người. KHÔNG có chú Ếch Gỗ trong cảnh này. |
| b06 | 00:44.3–00:54.6 (10.3s) | L49 | một quả tim hoặc một lá phổi người sau khi được hiến tặng chỉ có thể bảo quản lạnh trong thùng đá chuyên dụng tối đa từ 4-6 tiếng đồng hồ! Sau khoảng thời gian ngắn ngủi đó, các mô tế bào sẽ hoại tử và | **4-6 GIỜ** · giới hạn tạng người · L/340 · [0.45, 0.5] | Thực trạng y tế ghép tạng hiện nay: Chiếc thùng bảo quản đá lạnh có đồng hồ đếm ngược chỉ còn 4-6 giờ giới hạn trước khi tạng ghép bị hỏng. KHÔNG có chú Ếch Gỗ trong cảnh này. |
| b07 | 00:54.6–01:04.6 (10.1s) | L71 | không thể cấy ghép được nữa. Mỗi năm có hàng chục ngàn bệnh nhân trên toàn thế giới qua đời trong tuyệt vọng chỉ vì khoảng cách địa lý quá xa, không kịp vận chuyển tạng ghép đến phòng mổ! |  | Bản đồ vận chuyển tạng khẩn cấp: Tuyến đường bay trực thăng chở thùng tạng ghép nối giữa hai thành phố xa xôi trên bản đồ thế giới với đồng hồ đếm ngược đỏ rực. KHÔNG có chú Ếch Gỗ trong cảnh này. |
| b08 | 01:04.6–01:18.1 (13.5s) | L50 | Hiện nay, các nhà khoa học hàng đầu tại Đại học Harvard và Bệnh viện Đa khoa Massachusetts đang tích cực nghiên cứu tổng hợp các phân tử mầm đá và hợp chất Cryoprotectant mô phỏng từ loài ếch gỗ. Mục tiêu tối thượng là có thể đưa các cơ quan nội tạng người vào trạng |  | Phòng nghiên cứu sinh học tương lai tại Đại học Harvard: Các buồng bảo quản lạnh sâu mô phỏng phân tử ếch gỗ bảo quản an toàn cơ quan bên trong cơ thể suốt nhiều tháng. KHÔNG có chú Ếch Gỗ trong cảnh này. |
| b09 | 01:18.1–01:28.7 (10.6s) | L72 | thái đông lạnh sâu an toàn suốt nhiều tuần, thậm chí nhiều tháng trời mà không bị tổn thương tế bào! Khi công nghệ này thành công, nó sẽ tạo ra những ngân hàng nội tạng toàn cầu, cứu sống hàng triệu sinh mạng mỗi năm! |  | Ngân hàng bên trong cơ thể tương lai Bio-Vault: Các buồng chứa cryo-capsule công nghệ cao bảo quản trái tim và lá gan phát sáng trong dung dịch bảo quản phôi ếch gỗ. KHÔNG có chú Ếch Gỗ trong cảnh này. |
| b10 | 01:28.7–01:38.0 (9.3s) | L51 | Và xa hơn nữa, đó chính là giấc mơ đưa các phi hành gia tương lai vào trạng thái ngủ đông sâu kéo dài hàng bao thế kỷ để thực hiện những chuyến du hành không gian xuyên qua các dải ngân hà xa xôi! |  | Phi thuyền không gian tương lai bay giữa dải ngân hà rực rỡ: Các phi hành gia nằm ngủ đông an toàn trong khoang cryo-stasis mô phỏng cơ chế của chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles). |
| b11 | 01:38.0–01:48.3 (10.2s) | L52 | Còn bây giờ, chương trình xin gửi tới các bạn câu đố hóc búa để hé lộ nhân vật chính của Tập 34: Sinh vật nào sở hữu tỷ lệ kích thước bộ não so với cơ thể tương đương loài tinh tinh, biết tự uốn cong |  | Bức tranh bí ẩn hé lộ linh thú Tập 34: Bóng đen huyền bí của chú Quạ Đen thông minh đang dùng mỏ uốn cong chiếc que sắt làm móc câu bắt mồi bên gốc cây cổ thụ. KHÔNG có chú Ếch Gỗ trong cảnh này. |
| b12 | 01:48.3–01:56.1 (7.8s) | L73 | que sắt làm lưỡi câu bắt ấu trùng, và đặc biệt có thể ghi nhớ chính xác khuôn mặt của kẻ thù suốt 5 năm trời để truyền lại cho đàn con cháu đời sau tiếp tục báo thù? | **5 NĂM** · nhớ mặt kẻ thù · R/360 · [0.6, 0.5] | Bộ não chim thiên tài: Bản chụp tia X hộp sọ chú Quạ Đen với bộ não phát sáng màu tím thông tuệ, chiếc mỏ khéo léo gắp que sắt uốn cong câu con sâu trong khúc gỗ mục. KHÔNG có chú Ếch Gỗ trong cảnh này. |
| b13 | 01:56.1–02:02.4 (6.3s) | L53 | Hãy để lại câu trả lời của bạn dưới phần bình luận, bấm like và đăng ký kênh để không bỏ lỡ những thước phim kỳ thú tiếp theo! |  | Khung kết thúc video YouTube thân thiện: chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) cùng chú chim cánh cụt phóng viên hoạt hình mặc áo phao lông thú ấm áp, cầm micro phỏng vấn run rẩy giữa trời tuyết rơi vẫy tay chào khán giả bên cạnh nút Like, Subscrib |

## 5. Phân cảnh Shorts — từng beat

Banner: **TIM NGỪNG ĐẬP 7 THÁNG: / TỰ RÃ ĐÔNG BẬT NHẢY?!** · giọng 54.0s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Cảnh báo sinh tồn vùng cực -20°C! Tại sao loài ếch tí hon này có thể để tim ngừng đập hoàn toàn suốt 7 tháng mùa | **-20°C** · bão tuyết Alaska · R/480 · [0.5, 0.4] |
| s02 | 00:06.1 | S11 | đông rồi tự rã đông bật nhảy sống dậy? Đây là Ếch Gỗ Bắc Cực, Quái Kiệt Băng Giá của xứ sở Alaska! |  |
| s03 | 00:11.2 | S02 | Khi mùa đông ập đến, thay vì trốn sâu dưới lòng đất, nó ở lì trên mặt đất và chủ động để cơ thể mình bị đóng băng! |  |
| s04 | 00:17.3 | S03 | Một loại protein tạo mầm đá đặc biệt ép 65-70% lượng nước trong cơ thể nó hóa thành băng đá ngoại | **70% BĂNG** · giáp băng ngoại bào · L/450 · [0.45, 0.5] |
| s05 | 00:22.4 | S04 | bào. Để tế bào không bị xé rách, lá gan của nó lập tức phình to, bơm một lượng đường Glucose siêu đậm đặc gấp 300 lần | **300 LẦN** · glucose chống đông · R/480 · [0.55, 0.45] |
| s06 | 00:28.9 | S12 | vào bên trong từng tế bào như siro chống đông sinh học! |  |
| s07 | 00:31.2 | S05 | Kết quả: Trái tim ngừng đập hoàn toàn ở mức 0 nhịp/phút. Máu ngừng chảy, | **0 NHỊP/P** · tim ngừng đập hẳn · L/460 · [0.4, 0.5] |
| s08 | 00:35.5 | S13 | sóng não phẳng lì, cơ thể cứng như đá gõ côm cốp suốt 200 ngày! |  |
| s09 | 00:39.0 | S06 | Về mặt y học, nó đã chết lâm sàng 100%! | **100%** · chết lâm sàng · R/480 · [0.55, 0.45] |
| s10 | 00:41.2 | S07 | Thế nhưng khi ánh nắng mùa xuân rọi xuống, |  |
| s11 | 00:43.2 | S08 | trái tim tự rã đông đầu tiên, tự động đập lại mà không cần sốc điện, |  |
| s12 | 00:46.5 | S09 | và chỉ vài tiếng sau chú ếch đã bật dậy nhảy tanh tách đi tìm bạn tình! |  |
| s13 | 00:50.3 | S10 | Một kiệt tác hồi sinh đang mở ra cuộc cách mạng bảo quản tạng ghép cho loài người! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo khẩn cấp từ hiện trường vùng cực! Phóng viên 24h đang có mặt trực tiếp tại cánh rừng lá kim taiga phủ đầy tuyết trắng ở". Bố cục: Hiện trường bão tuyết Alaska mù mịt: chú chim cánh cụt phóng viên hoạt hình mặc áo phao lông thú ấm áp, cầm micro phỏng vấn run rẩy giữa trời tuyết rơi trùm áo phao lông thú to sụ, hai tay run bần bật cầm micro truyền hình trực tiếp giữa cơn lốc tuyết trắng xóa. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tiểu bang Alaska, nơi chiếc nhiệt kế chuyên dụng vừa tụt thẳng đứng xuống mức -20°C!". Bố cục: Cận cảnh cột nhiệt kế sinh tồn cắm ngập trong đụn tuyết: Cột thủy ngân tụt dốc không phanh thẳng đứng xuống vạch âm hai mươi độ C đỏ rực với sương tuyết bám quanh. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gió bắc cực gầm rú rít từng cơn lạnh buốt thấu tận xương tủy, làm cho lớp hơi nước thở ra vừa chạm vào không khí là đông đặc thành bụi băng li ti. Mọi nhánh cây ngọn cỏ đều phủ một lớp sương muối trắng toát,". Bố cục: Minh họa cơn gió lốc vùng cực đóng băng mọi thứ: Luồng hơi nước thở ra từ miệng biến ngay thành chùm tinh thể băng rơi lả tả xuống mặt đất tuyết. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "và các mặt hồ nước ngọt sâu thẳm đã hóa thành những khối đá tảng hoa cương chẳng hề có một vết rạn nứt. Trong điều kiện thời tiết tử thần khắc nghiệt đến rợn người này, hãy quan sát cách các cư dân bản địa đối phó với mùa đông:". Bố cục: Mặt cắt hồ nước ngọt Bắc Cực: Toàn bộ tầng nước mặt đóng băng thành một khối đá hoa cương dày đặc, bên dưới các sinh vật đều chìm vào giấc ngủ im lìm. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lũ gấu Bắc Cực to lớn phải cuộn tròn trong hang tuyết với lớp mỡ dày hàng chục xăng-ti-mét, đàn chim di cư thiện chiến đã vỗ cánh bay hàng ngàn cây số về phương Nam ấm áp từ ba tháng trước,". Bố cục: Bức tranh so sánh sinh tồn mùa đông: chú gấu Bắc Cực hoạt hình lông trắng to lớn mập mạp ngơ ngác, cầm một cành cây nhỏ gõ vào khối đá lạnh cuộn tròn trong hang tuyết ấm áp, phía trên là đàn chim di cư bay về phương Nam theo hình chữ V. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "còn lũ chuột đồng thì rúc sâu cả mét dưới lòng đất nơi nhiệt độ còn giữ được trên mức 0°C. Alo phóng viên ơi!". Bố cục: Sơ đồ mặt cắt đất rừng taiga: Chú chuột đồng cuộn tròn trong chiếc tổ đào sâu cả mét dưới lòng đất ấm cúng, xung quanh chất đầy hạt dẻ dự trữ. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôi không có lông vũ, không có mỡ dày, cũng chẳng thèm đào hang sâu luôn! Chỉ có mỗi chiếc quần đùi da cóc mỏng manh này thôi thì có trụ nổi qua đêm nay không ạ?". Bố cục: Hình ảnh hài hước: chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) đứng trên tảng băng trôi, mặc mỗi chiếc quần đùi da cóc tí hon, hai tay chống nạnh cười toe toét nhìn về phía chú chim cánh cụt phóng viên hoạt hình mặc áo phao lông thú ấm áp, cầm micro phỏng vấn run rẩy giữa trời tuyết rơi.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ấy thế mà ngay dưới chân của chúng tôi, chỉ cách mặt tuyết chừng vài phân bên dưới lớp lá rụng và rêu mục mỏng manh, một sinh vật bé nhỏ lại đang thản nhiên chờ đón lưỡi hái tử thần của mùa đông!". Bố cục: Lớp lá rụng và rêu mục trên mặt đất rừng: chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) đang thong thả nằm tựa lưng vào hòn đá nhỏ, đắp chiếc chăn lá cây mỏng manh như đang đi nghỉ dưỡng.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Xin giới thiệu nhân vật chính của hồ sơ sinh tồn số 33: Ếch Gỗ Bắc Cực, mang danh pháp khoa học Lithobates sylvaticus, kẻ được giới sinh học". Bố cục: Tấm áp phích hồ sơ định danh vùng cực Cryo-Noir: Chân dung dũng mãnh của chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) với huy hiệu Quái Kiệt Băng Giá phát sáng rực rỡ trên nền tinh thể băng tuyết.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn thân chú ếch gỗ trưởng thành chỉ dài từ 5-7cm, và cân nặng vỏn vẹn từ 8-15g, nghĩa là chỉ nhẹ tương đương một quả nho nhỏ hoặc hai quả trứng cút luộc!". Bố cục: Màn hình thước đo sinh trắc học vùng cực: Thước đo laser hiển thị chiều dài 5-7cm và chiếc cân đá mini hiện 8-15g của chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) bên cạnh một quả nho nhỏ.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "như chiếc mặt nạ hiệp sĩ bí ẩn trong các bộ truyện tranh! Thế nhưng, điểm điên rồ và kỳ quặc nhất trong tập tính sinh học của chú ếch này là gì? Các loài ếch nhái thông thường khác". Bố cục: Cận cảnh đôi mắt của chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles): Hai vệt sọc đen sẫm kéo dài qua mắt như mặt nạ hiệp sĩ Zorro, đôi mắt tinh anh lấp lánh ánh nhìn kiên định trước bão tuyết.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "ở lì ngay trên nền rừng lạnh giá, nơi nhiệt độ sẽ chạm đáy -20°C, và sẵn sàng để toàn bộ cơ thể mình bị đóng băng thành một tảng đá vô tri giác!". Bố cục: Đồng hồ sinh tồn đếm ngược: chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) khoanh tay ngồi thiền trên lớp rêu rừng taiga, xung quanh những bông tuyết bắt đầu phủ kín người biến thành một khối băng tảng.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để thấy được sự phi thường của Quái Kiệt Băng Giá, trước hết chúng ta cần hiểu rõ vì sao đối với hầu hết mọi sinh vật trên Trái Đất, việc bị đóng băng đồng nghĩa với một bản án tử hình không thể đảo ngược! Khi nước nguyên chất chuyển từ thể lỏng sang thể rắn ở nhiệt độ". Bố cục: Sơ đồ khoa học phân tử Cryo-Noir: Một giọt nước tinh khiết đang đóng băng, các phân tử nước kết tinh giãn nở và mọc ra những mũi gai băng nhọn hoắt như dao găm. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu hiện tượng đóng băng vô kiểm soát này xảy ra bên trong cơ thể con người hay bất kỳ loài động vật nào khác, những mũi dao băng sắc nhọn đó sẽ lập tức đâm thủng lớp màng lipid mỏng manh của tế bào, xé toạc các vi mạch nước màu". Bố cục: Hình ảnh kính hiển vi mô phỏng tế bào thông thường: Những mũi gai băng sắc lẹm đâm rách toạc màng tế bào, dịch nội bào tràn ra ngoài gây hoại tử hoàn toàn. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kính thưa các tinh thể đá mũi nhọn hung dữ! Tuyệt đối cấm bén mảng vào khoang tim và lá gan của tôi nhé! Ai muốn đóng băng thì xếp hàng ngay ngắn ra ngoài da và dưới bụng đứng hết cho tôi!". Bố cục: chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) hóa thân thành chú cảnh sát giao thông vùng cực tí hon, tay cầm gậy chỉ huy điều hướng các tinh thể băng xếp hàng rồng rắn đi ra phía ngoài da.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và đó chính là lúc chiến thuật tạo mầm đá ngoại bào thần kỳ của chú ếch gỗ phát huy uy lực tối thượng! Năm 1993, nhóm nghiên cứu của tiến sĩ Jack Costanzo tại". Bố cục: Trang bìa công trình nghiên cứu khoa học năm 1993 của tiến sĩ Jack Costanzo, bên cạnh là mô hình 3D phân tử protein tạo mầm đá phát sáng màu lam ngọc. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hạ xuống mức -1°C đến -2°C, những protein này lập tức đóng vai trò như những thỏi nam châm định hướng, kích thích các phân tử nước bên ngoài tế bào kết tinh thành đá trước tiên!". Bố cục: Bảng đo vi khí hậu tế bào: Khi nhiệt độ chạm ngưỡng -1°C đến -2°C, các protein mầm đá hoạt động như nam châm gom các tinh thể băng về khoang ngoại bào. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thay vì để băng đá xuất hiện ngẫu nhiên và bừa bãi, cơ thể của ếch gỗ chủ động kiểm soát tuyệt đối vị trí đóng băng: Băng chỉ được phép hình thành ở các khoang trống nằm ngoài màng tế bào, trong ổ bụng, dưới lớp da lưng và xung quanh các bó cơ bắp! Khi nước ở bên ngoài đóng băng, hiện tượng thẩm thấu tự nhiên sẽ". Bố cục: Bản đồ giải phẫu cắt lớp cơ thể chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles): Băng đá đóng thành lớp giáp bảo vệ dày ở ổ bụng và dưới da, trong khi các cơ quan tim gan bên trong vẫn an toàn nguyên vẹn.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "rút dần nước lỏng từ bên trong tế bào ra ngoài, giống như việc bạn rút ruột nước ra khỏi một quả bóng bay để nó xẹp lại một cách có tính toán. Khối lượng băng hình thành bên ngoài tế bào này tăng dần lên một cách đáng kinh ngạc, cho đến khi chiếm tới". Bố cục: Mô hình minh họa thẩm thấu nước: Tế bào nội bào nhẹ nhàng co lại một cách có kiểm soát như quả bóng xẹp bớt nước, nhường chỗ cho lớp băng ngoài khoang đệm.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "65-70% tổng dung tích nước của toàn bộ cơ thể! Hãy tưởng tượng:". Bố cục: Biểu đồ tròn tỷ lệ thể tích nước cơ thể chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles): Mảng màu xanh lam ngọc chiếm trọn 70% tổng lượng nước hóa thành giáp băng bao bọc bên ngoài. chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "70% cơ thể của bạn biến thành băng cứng ngắc như một hòn đá hoa cương, nhưng nhờ có cơ chế điều hướng mầm đá tài tình, chẳng có tinh thể nhọn nào được phép chạm vào không gian thiêng liêng bên trong tế bào!". Bố cục: chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) trong tư thế siêu anh hùng khoác bộ giáp băng tinh thể trong suốt óng ánh, tự tin mỉm cười trước bão tuyết vùng cực.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thế nhưng, một bài toán hóc búa khác lập tức xuất hiện ngay tại đây! Nếu nước bên ngoài tế bào liên tục bị hút đi để tạo thành lớp giáp băng, chẳng phải áp suất thẩm thấu sẽ vắt kiệt từng giọt nước bên trong tế bào,". Bố cục: Tế bào sinh học đang đối mặt nguy cơ co rúm: Áp suất thẩm thấu đè nặng lên màng tế bào, chiếc còi báo động khẩn cấp màu đỏ nhấp nháy liên hồi. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngay vào khoảnh khắc những cảm biến nhiệt độ trên da của ếch cảm nhận được tinh thể băng chạm vào lớp biểu bì, một tín hiệu báo động đỏ cấp quốc gia được phát đi dọc theo tủy sống, truyền thẳng đến cơ quan bên trong cơ thể quan trọng nhất: Nhà máy hóa chất lá gan!". Bố cục: Hệ thống thần kinh cảm giác của chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles): Làn da chạm vào băng đá bắn ra tia sét tín hiệu sinh học chạy dọc sống lưng về trung tâm chỉ huy lá gan.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo chỉ huy trưởng! Bộ phận gan đã nhận lệnh báo động khẩn cấp! Kho dự trữ đường năng lượng đang mở hết van xả lũ, chuẩn bị biến toàn bộ nước màu thành siro ngọt lịm đây!". Bố cục: Hình ảnh hài hước bên trong nhà máy lá gan: chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) đội mũ thuyền trưởng gạt cần van xả lũ màu vàng cam, mở toang các bồn chứa siro đường mật mía ngọt lịm.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Những nghiên cứu đột phá mang tính lịch sử của vợ chồng giáo sư Kenneth Storey từ năm 1988 đã hé lộ một kỳ quan chuyển hóa sinh hóa: Trong suốt mùa thu, lá gan của ếch gỗ tích lũy một lượng đường phức Glycogen khổng lồ, khiến lá gan phình to". Bố cục: Chân dung giáo sư Kenneth Storey trên bìa tạp chí khoa học năm 1988, bên cạnh là biểu đồ lá gan chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) phình to gấp nhiều lần chứa đầy kho Glycogen.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ trong vòng vài giờ đồng hồ ngắn ngủi, lượng đường Glucose được bơm ồ ạt vào dòng nước màu, đẩy nồng độ đường huyết của chú ếch vọt lên gấp từ 100-300 lần so với mức bình thường! Để dễ hình dung độ kinh hoàng của con số này:". Bố cục: Đồng hồ đo nồng độ đường huyết điện tử: Kim chỉ số vọt từ mức bình thường bay thẳng lên con số 300 lần với cột thủy tinh phát sáng màu vàng mật ong rực rỡ.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu nồng độ đường huyết của một người trưởng thành chỉ cần tăng lên gấp ba đến bốn lần bình thường, người đó đã rơi vào trạng thái hôn mê tiểu đường cấp tính và tử vong nếu không được". Bố cục: Hình ảnh so sánh y học: Bệnh nhân người sốt sắng trước kết quả tiểu đường cao, trong khi chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) đang thong thả nhâm nhi cốc siro đường vàng ươm cười khoái chí.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Song song với đường Glucose, thận của ếch gỗ cũng giữ lại hợp chất Urea ở nồng độ cực cao. Hai hợp chất này hòa quyện tạo thành một dung dịch siro chống đông Cryoprotectant tự nhiên siêu đậm đặc, thấm đẫm vào từng milimet khối chất nguyên sinh bên trong tế bào.". Bố cục: Mô hình phân tử Cryoprotectant: Các phân tử Glucose hình lục giác đan xen với hạt Urea bao bọc lấy các phân tử protein nội bào như chiếc khiên đệm siêu mềm. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Siro này hạ điểm đông đặc của dịch nội bào xuống rất sâu, khiến nước bên trong tế bào không thể đóng băng thành đá được nữa mà vẫn duy trì ở trạng thái sền sệt dạng gel. Nhờ đó, tế bào không bị mất nước, màng tế bào giữ nguyên hình dạng và sự sống bên trong được bảo tồn tuyệt đối an toàn!". Bố cục: Cận cảnh chất nguyên sinh bên trong tế bào chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles): Dung dịch duy trì ở dạng thạch gel sánh mịn màng, không một tinh thể đá nào có thể kết tủa bên trong.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và bây giờ, kim đồng hồ đếm ngược sinh tồn 24h chính thức chạm mốc số không tử thần! Khi màn đêm vùng cực buông xuống và nhiệt độ không khí bên ngoài tụt sâu từ -12°C, -16°C cho đến -20°C, quá trình đông cứng toàn thân của chú ếch bước vào". Bố cục: Băng giá phủ kín toàn cảnh rừng taiga: Đồng hồ đếm ngược sinh tồn 24h chạy về đúng con số 00:00:00, bão tuyết rít gào buốt lạnh âm hai mươi độ C. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trái tim bé bỏng của chú ếch gỗ đập chậm dần từng nhịp: Từ 100 nhịp/phút xuống 50 nhịp, rồi 10 nhịp, 5 nhịp... và rồi chiếc van tim cuối cùng khép lại. Nhịp tim dừng hẳn ở con số không tròn trĩnh! Không còn một giọt nước màu nào được bơm đi nuôi cơ thể, hệ tuần hoàn tê liệt 100%!". Bố cục: Màn hình điện tâm đồ ECG theo dõi nhịp tim: Đồ thị nhịp tim từ 100 nhịp/phút tụt xuống 50 nhịp, 10 nhịp rồi tắt hẳn thành một đường chân trời phẳng lặng.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cốc cốc cốc! Bác ếch gỗ ơi còn nghe thấy em nói gì không đấy? Chân tay bác cứng đơ rồi, em gõ thử cái que vào bụng bác nghe kêu cộp cộp giòn tan như gõ vào hòn đá cuội vậy nè!". Bố cục: chú gấu Bắc Cực hoạt hình lông trắng to lớn mập mạp ngơ ngác, cầm một cành cây nhỏ gõ vào khối đá lạnh tò mò ngồi xổm bên tảng rêu tuyết, dùng que gỗ nhỏ gõ vào người chú ếch chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) đã đông cứng, phát ra âm thanh côm cốp như gõ đá cuội.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không còn một nhịp tim nào đập trong lồng ngực! Hai lá phổi ngừng phập phồng co bóp hoàn toàn, không có một phân tử khí oxy nào được hít vào hay thải ra! Nếu bạn gắn một bộ cảm biến điện não đồ siêu nhạy lên hộp sọ của chú ếch lúc này, chiếc kim ghi nhận tín hiệu sẽ chỉ vẽ ra một". Bố cục: Màn hình điện não đồ EEG của bác sĩ cú mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắng và cầm bảng theo dõi thông số sinh tồn: Chiếc kim vạch ra đường thẳng tắp 0% sóng não, bên cạnh là biểu tượng trái tim bị đóng băng hoàn toàn nhân vật trái tim hoạt hình màu đỏ đội mũ len nhỏ bị bọc trong tinh thể băng xanh lam trong suốt.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đôi mắt của nó đã chuyển sang màu đục ngầu và đông cứng hệt như hai viên bi ve bằng thủy tinh. Cơ bắp toàn thân cứng như thép nguội, các khớp xương chân không thể bẻ cong. Nếu bạn nhấc chú ếch lên và thả rơi". Bố cục: Cận cảnh khuôn mặt đông đá của chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles): Đôi mắt đục ngầu như hai hòn bi ve thủy tinh, toàn thân cứng như thép nguội đọng lớp sương tuyết lấp lánh.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "từ độ cao 30cm xuống mặt băng, nó sẽ nảy tưng tưng phát ra âm thanh côm cốp vang dội như một viên sỏi cuội lăn lóc ven đường! Trong nghiên cứu đột phá xuất bản năm 2014 trên Tạp chí Sinh học Thực nghiệm,". Bố cục: Minh họa chú ếch đông đá rơi từ độ cao 30cm xuống mặt băng nảy tưng tưng côm cốp mà không hề trầy xước mô mềm trước ánh mắt thảng thốt của chú gấu Bắc Cực hoạt hình lông trắng to lớn mập mạp ngơ ngác, cầm một cành cây nhỏ gõ vào khối đá lạnh.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tiến sĩ Đôn Lác-xơn tại Viện Sinh học Bắc Cực thuộc Đại học Alaska Fairbanks đã chứng minh rằng: Những cá thể Ếch Gỗ Bắc Cực hoang dã có thể duy trì trạng thái đóng băng hóa đá,". Bố cục: Tấm lịch mùa đông Bắc Cực lật trang liên tục từ tháng 10 đến tháng 4: Biểu đồ thời gian 7 tháng tương đương 200 ngày đêm ngủ đông hóa đá của chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles).
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "7 tháng mùa đông dài đằng đẵng cuối cùng cũng trôi qua. Khi tháng tư và tháng năm gõ cửa cánh rừng Bắc Cực, những tia nắng ấm áp đầu tiên của mùa xuân bắt đầu len lỏi qua các tán cây thông, làm tan chảy lớp tuyết dày trắng xóa bên trên mặt đất.". Bố cục: Ánh bình minh mùa xuân tháng 4 rọi xuống cánh rừng Bắc Cực: Băng tuyết bắt đầu tan chảy, những mầm rêu xanh non nhú lên khỏi mặt đất ẩm ướt. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và ngay tại giây phút này, một trong những kỳ quan sinh học ngoạn mục nhất hành tinh chính thức bắt đầu vận hành: Quy trình rã đông thần tốc từ trong ra ngoài! Ở các loài động vật có vú, nếu bị đóng băng rồi đem sưởi ấm, cơ thể sẽ rã đông từ". Bố cục: Sơ đồ so sánh cơ chế rã đông: Động vật có vú rã đông từ ngoài vào trong gây tổn thương tim, trong khi chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) rã đông từ sâu trong tâm thất ra ngoài. chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thình thịch! Thình thịch! Cảm ơn bác mặt trời mùa xuân nhé! Máy bơm sự sống trong lồng ngực em đã khởi động lại trơn tru rồi nè, chuẩn bị xả van cho nước màu ấm chạy khắp người thôi!". Bố cục: nhân vật trái tim hoạt hình màu đỏ đội mũ len nhỏ bị bọc trong tinh thể băng xanh lam trong suốt bên trong lồng ngực chú ếch bắt đầu tỏa ra ánh hào quang ấm áp màu vàng cam, lớp băng tan chảy thành nước và trái tim bắt đầu co bóp đập lại rộn ràng.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trái tim nằm sâu trong lồng ngực chú ếch chính là cơ quan đầu tiên được rã đông và tan chảy hoàn toàn! Không cần bất kỳ một cú sốc điện khử rung tim nào từ bác sĩ cấp cứu, các tế bào cơ tim của ếch gỗ tự động phát ra". Bố cục: Cận cảnh cơ tim tự phát xung điện sinh học: Không cần máy sốc điện, từng tế bào cơ tim tự phát ra tia năng lượng hồi sinh nhịp đập đầu tiên sau 7 tháng ngủ vùi. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dòng nước màu ấm nóng giàu đường Glucose được trái tim bơm đi khắp nơi, nhanh chóng làm tan chảy lớp băng bao quanh phổi, gan và thận.". Bố cục: Hệ tuần hoàn bừng sáng: Dòng nước màu ấm màu đỏ cam chở oxy và glucose lưu thông qua phổi, gan, thận làm tan biến hoàn toàn các khối băng bên trong cơ thể. chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ trong vòng một đến hai giờ đồng hồ sau đó, hai lá phổi bắt đầu phập phồng hít thở trở lại từng luồng không khí trong lành của mùa xuân! nước màu giàu oxy được đưa lên não bộ, kích hoạt hàng triệu tế bào thần kinh bừng tỉnh sau một giấc ngủ đông kéo dài nửa năm ròng!". Bố cục: Hai lá phổi của chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) phập phồng hít thở trở lại luồng không khí mùa xuân trong lành, não bộ bừng sáng hàng triệu tế bào thần kinh hoạt động nhộn nhịp.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và điều kỳ diệu nhất là chỉ sau khoảng vài tiếng đồng hồ ngắn ngủi, lớp băng cứng ngắc ngoài các chi tan biến hoàn toàn. Chú ếch gỗ khẽ chớp đôi mắt trong veo, vươn vai cựa quậy bốn chân, rồi bất ngờ bật nhảy tanh tách từng bước dài đầy uy lực! Nó". Bố cục: chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) chớp mắt trong veo, vươn vai cựa quậy rồi bật nhảy tanh tách từng bước dài dũng mãnh trên nền rừng mùa xuân rực rỡ hoa tuyết. chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "lao thẳng xuống những vũng nước băng tan đầu mùa để cất tiếng kêu ộp ộp vang dội gọi bạn tình, giành lấy vị trí đẻ trứng thuận lợi nhất trước khi bất kỳ loài sinh vật nào khác trong rừng kịp tỉnh giấc ngủ đông!". Bố cục: Đầm lầy nước băng tan rộn rã: chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) đứng trên tảng đá cất tiếng kêu ộp ộp vang lừng gọi bạn tình, các đối thủ trong rừng ngơ ngác nhìn theo thán phục.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo tổng kết hồ sơ sinh tồn số 33 từ phóng viên 24h: 7 tháng tim ngừng đập hoàn toàn, 70% lượng nước trong cơ thể hóa thành băng đá,". Bố cục: Bảng tổng kết hồ sơ sinh tồn số 33: Các chỉ số kỷ lục của chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) gồm 7 tháng tim 0 nhịp, 70% nước hóa đá và sống sót ở -20°C được vinh danh trang trọng.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng giá trị của chú ếch gỗ bé nhỏ này không chỉ dừng lại ở thế giới tự nhiên hoang dã. Cơ chế sinh học độc nhất vô nhị của nó đang trở thành chiếc chìa khóa vàng mở ra cuộc cách mạng y học lớn nhất thế kỷ 21 dành cho nhân loại!". Bố cục: Biểu tượng phòng thí nghiệm công nghệ y sinh tương lai: Mô hình phân tử chống đông của ếch gỗ được chiếu sáng hologram giữa các ống nghiệm hiện đại. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bí kíp chống đông hóa đá của dòng họ nhà ếch chúng tôi xin kính tặng lại cho các bác sĩ và nhà khoa học loài người nhé! Nhớ nghiên cứu thành công để cứu thật nhiều bệnh nhân trên đời nha! Các bạn có biết một". Bố cục: chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) trong trang phục giáo sư tí hon cầm cuộn bí kíp cổ truyền trao tặng cho các bác sĩ trong phòng mổ cứu người.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "một quả tim hoặc một lá phổi người sau khi được hiến tặng chỉ có thể bảo quản lạnh trong thùng đá chuyên dụng tối đa từ 4-6 tiếng đồng hồ! Sau khoảng thời gian ngắn ngủi đó, các mô tế bào sẽ hoại tử và". Bố cục: Thực trạng y tế ghép tạng hiện nay: Chiếc thùng bảo quản đá lạnh có đồng hồ đếm ngược chỉ còn 4-6 giờ giới hạn trước khi tạng ghép bị hỏng. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hiện nay, các nhà khoa học hàng đầu tại Đại học Harvard và Bệnh viện Đa khoa Massachusetts đang tích cực nghiên cứu tổng hợp các phân tử mầm đá và hợp chất Cryoprotectant mô phỏng từ loài ếch gỗ. Mục tiêu tối thượng là có thể đưa các cơ quan bên trong cơ thể người vào trạng thái". Bố cục: Phòng nghiên cứu sinh học tương lai tại Đại học Harvard: Các buồng bảo quản lạnh sâu mô phỏng phân tử ếch gỗ bảo quản an toàn cơ quan bên trong cơ thể suốt nhiều tháng. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và xa hơn nữa, đó chính là giấc mơ đưa các phi hành gia tương lai vào trạng thái ngủ đông sâu kéo dài hàng bao thế kỷ để thực hiện những chuyến du hành không gian xuyên qua các dải ngân hà xa xôi!". Bố cục: Phi thuyền không gian tương lai bay giữa dải ngân hà rực rỡ: Các phi hành gia nằm ngủ đông an toàn trong khoang cryo-stasis mô phỏng cơ chế của chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles).
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn bây giờ, chương trình xin gửi tới các bạn câu đố hóc búa để hé lộ nhân vật chính của Tập 34: Sinh vật nào sở hữu tỷ lệ kích thước bộ não so với cơ thể tương đương loài tinh tinh, biết tự uốn cong que sắt". Bố cục: Bức tranh bí ẩn hé lộ linh thú Tập 34: Bóng đen huyền bí của chú Quạ Đen thông minh đang dùng mỏ uốn cong chiếc que sắt làm móc câu bắt mồi bên gốc cây cổ thụ. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy để lại câu trả lời của bạn dưới phần bình luận, bấm like và đăng ký kênh để không bỏ lỡ những thước phim kỳ thú tiếp theo!". Bố cục: Khung kết thúc video YouTube thân thiện: chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) cùng chú chim cánh cụt phóng viên hoạt hình mặc áo phao lông thú ấm áp, cầm micro phỏng vấn run rẩy giữa trời tuyết rơi vẫy tay chào khán giả bên cạnh nút Like, Subscribe và chuông thông báo hoạt hình rực rỡ.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "toàn cầu ngả mũ thán phục với biệt danh Quái Kiệt Băng Giá của muôn loài! Hãy nhìn vào những thông số trắc lượng cơ thể vô cùng khiêm tốn của sinh vật này:". Bố cục: Biểu đồ vinh danh Quái Kiệt Băng Giá: Chân dung chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) đứng trên bục vinh quang giữa các huân chương băng tuyết và cờ hiệu sinh tồn vùng cực.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Làn da của nó có màu nâu đồng pha lẫn xám của vỏ cây rừng, và điểm nhận dạng đặc trưng nhất chính là hai vệt sọc đen sẫm kéo dài từ khóe mắt vòng qua tai, trông hệt". Bố cục: Bản vẽ phối màu ngụy trang vùng cực: Cận cảnh lớp da sần sùi màu nâu đồng của chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) hòa lẫn hoàn hảo vào thảm rêu rừng taiga và vỏ cây thông tuyết.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "ở xứ ôn đới bắt buộc phải lặn sâu xuống đáy bùn lầy của đáy hồ không đóng băng để sống sót qua mùa đông. Còn Ếch Gỗ Bắc Cực thì không! Nó không thể bơi xuống đáy hồ vì phổi và da của nó sẽ chết ngạt. Thay vào đó, nó chọn cách". Bố cục: So sánh sinh thái: Các chú ếch xanh thông thường co ro rúc dưới đáy bùn hồ nước lạnh run rẩy, nhìn lên thán phục lòng dũng cảm của chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) trên mặt đất.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "dưới 0°C, thể tích của nó sẽ giãn nở đột ngột thêm khoảng chín phần trăm. Nguy hiểm hơn nữa, các tinh thể đá hình thành tự do trong môi trường sống sẽ phát triển thành những cấu trúc gai nhọn li ti, sắc bén hệt như hàng triệu lưỡi dao găm siêu nhỏ sắc lẹm!". Bố cục: Mô hình vật lý giãn nở thể tích: Khối băng trong suốt nở bung với các vết nứt rạn tỏa ra xung quanh, làm vỡ tung một ống nghiệm thủy tinh đo lường. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "trong tích tắc và phá nát toàn bộ cấu trúc bên trong cơ thể! Hậu quả là ngay khi vừa tan đá, các mô tế bào sẽ vỡ vụn và hoại tử hoàn toàn, dẫn đến cái chết gần như tức thì mà chẳng thiết bị y khoa nào có thể cứu vãn!". Bố cục: Cảnh báo hoại tử mô: Hình vẽ đồ họa vi phẫu thuật cho thấy các mao mạch bị tắc nghẽn và đóng băng đỏ rực dưới kính hiển vi điện tử. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "protein chuyên biệt mang tên protein tạo mầm đá! Khi nhiệt độ môi trường vừa". Bố cục: Cận cảnh chuỗi protein tạo mầm đá: Những hạt phân tử protein hình cầu màu lam ngọc phát sáng, đang hút các phân tử nước li ti lại gần tạo thành mạng lưới tinh thể có trật tự. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "khiến tế bào bị mất nước nghiêm trọng, teo tóp lại thành một mảnh vụn khô cằn và chết vì suy kiệt hay sao? Đúng là như vậy, nếu không có vũ khí bí mật thứ hai mang tên siêu chất chống đông sinh học!". Bố cục: Hình ảnh mô phỏng quả bóng bay tế bào bị xì hơi teo tóp nhăn nhúm vì mất nước, biểu cảm nhân vật tế bào hoạt hình méo xệch kêu cứu. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chiếm tới mười phần trăm trọng lượng cơ thể. Và ngay khi quá trình đóng băng bắt đầu, lá gan này lập tức kích hoạt enzyme phân giải Glycogen với tốc độ tên lửa, biến toàn bộ thành đường đơn Glucose tự do!". Bố cục: Cân đo bên trong cơ thể Bio-Lab: Chiếc cân điện tử cân lá gan màu nâu đỏ phình to bằng một phần mười cơ thể chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles), các khoang chứa đầy ắp những hạt Glycogen vàng lấp lánh.
```
</details>

<details><summary>L62</summary>

```text
HÌNH L62 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tiêm insulin cấp cứu! Nhưng với Quái Kiệt Băng Giá, nồng độ đường gấp 300 lần lại chính là chiếc phao cứu sinh vĩ đại nhất của nó!". Bố cục: Bệnh viện dã chiến hài hước: Chiếc xe cứu thương vùng cực nhấp nháy đèn còi với ống tiêm insulin to đùng, trong khi chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) đứng bên cạnh vỗ bụng cười tự hào.
```
</details>

<details><summary>L63</summary>

```text
HÌNH L63 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "giai đoạn quyết định. Dòng nước màu chứa đầy siro đường trở nên đặc quánh như mật mía rồi ngưng tụ hoàn toàn.". Bố cục: Bão tuyết màn đêm cực hàn: Cơn lốc xoáy tuyết xanh thẫm bao trùm toàn cảnh rừng taiga, những cột băng đá nhọn hoắt mọc lên từ mặt đất như rừng chông tuyết.
```
</details>

<details><summary>L64</summary>

```text
HÌNH L64 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đường chân trời thẳng tắp phẳng lì: Không còn bất kỳ xung điện thần kinh nào được truyền đi giữa các tế bào não!". Bố cục: Bản ghi điện não đồ EEG phóng đại: Màn hình oscilloscope màu xanh lá cây hiện đường chân trời thẳng tắp 0Hz phẳng lì, chiếc bút đo nằm im không một dao động. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>L65</summary>

```text
HÌNH L65 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tim ngừng đập hoàn toàn này liên tục suốt 7 tháng, tức là hơn 200 ngày đêm ròng rã giữa mùa đông vùng cực mà không hề chịu bất kỳ di chứng tổn thương nào khi rã đông!". Bố cục: Vũ trụ thời gian 4 mùa Bắc Cực: Hình ảnh quả cầu Trái Đất quay tròn qua các mùa tuyết phủ, chú ếch chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) hóa đá nằm im bất động thách thức dòng chảy thời gian.
```
</details>

<details><summary>L66</summary>

```text
HÌNH L66 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nước tuyết tan nhỏ từng giọt róc rách, thấm dần xuống lớp thảm rêu và lá mục ẩm ướt, nơi viên đá ếch gỗ đang nằm im lìm suốt hơn 200 ngày đêm.". Bố cục: Mùa xuân rã đông cận cảnh: Từng giọt nước tuyết trong suốt lấp lánh rơi róc rách xuống thảm rêu xanh tươi, những bông hoa tuyết màu vàng nở rộ đón nắng mai. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>L67</summary>

```text
HÌNH L67 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bề mặt da bên ngoài vào trong, khiến các mô bên ngoài ấm lên và đòi hỏi oxy trong khi trái tim bên trong vẫn còn là khối băng đông cứng, dẫn đến tử vong ngay tức khắc. Nhưng ếch gỗ thì sở hữu quy luật hoàn toàn ngược lại!". Bố cục: Sơ đồ nhiệt bức xạ: Sơ đồ nhiệt chụp cắt lớp cho thấy nhiệt lượng lan tỏa từ bên ngoài vào trong của một chú chuột, đối lập với nhiệt lượng tỏa ra từ tim của chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles).
```
</details>

<details><summary>L68</summary>

```text
HÌNH L68 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "những xung điện sinh học tự nhiên. Ban đầu là một nhịp co bóp yếu ớt, rồi nhịp thứ hai, nhịp thứ ba... Từng nhịp đập bắt đầu dồn dập và mạnh mẽ trở lại, khôi phục dòng chảy tuần hoàn huyết áp khắp cơ thể!". Bố cục: Tia sét sinh học phục sinh: Một tia chớp nhỏ màu vàng cam lóe lên ngay tại tâm thất của trái tim chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles), phá vỡ lớp vỏ băng mỏng cuối cùng để bơm nước màu trở lại.
```
</details>

<details><summary>L69</summary>

```text
HÌNH L69 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "sinh tồn ngoạn mục ở mức -20°C mà không hề suy suyển một tế bào nào! Quái Kiệt Băng Giá xứng đáng là một trong những kỳ tích tiến hóa vĩ đại nhất của sự sống trên hành tinh chúng ta!". Bố cục: Cúp vàng vinh danh sinh tồn Bắc Cực: Chiếc cúp vàng khắc hình chú ếch gỗ dũng mãnh đứng trên tảng băng trôi giữa tràng pháo tay của muôn loài động vật vùng cực.
```
</details>

<details><summary>L70</summary>

```text
HÌNH L70 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "sự thật đau lòng này không: Trong nền y học ghép tạng hiện đại,". Bố cục: Bệnh viện cấp cứu ghép tạng: Đồng hồ đếm ngược gấp gáp trên tường phòng mổ, các bác sĩ đang căng thẳng theo dõi chiếc thùng bảo quản tạng ghép người. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>L71</summary>

```text
HÌNH L71 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "không thể cấy ghép được nữa. Mỗi năm có hàng chục ngàn bệnh nhân trên toàn thế giới qua đời trong tuyệt vọng chỉ vì khoảng cách địa lý quá xa, không kịp vận chuyển tạng ghép đến phòng mổ!". Bố cục: Bản đồ vận chuyển tạng khẩn cấp: Tuyến đường bay trực thăng chở thùng tạng ghép nối giữa hai thành phố xa xôi trên bản đồ thế giới với đồng hồ đếm ngược đỏ rực. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>L72</summary>

```text
HÌNH L72 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đông lạnh sâu an toàn suốt nhiều tuần, thậm chí nhiều tháng trời mà không bị tổn thương tế bào! Khi công nghệ này thành công, nó sẽ tạo ra những ngân hàng bên trong cơ thể toàn cầu, cứu sống hàng triệu sinh mạng mỗi năm!". Bố cục: Ngân hàng bên trong cơ thể tương lai Bio-Vault: Các buồng chứa cryo-capsule công nghệ cao bảo quản trái tim và lá gan phát sáng trong dung dịch bảo quản phôi ếch gỗ. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>L73</summary>

```text
HÌNH L73 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "làm lưỡi câu bắt ấu trùng, và đặc biệt có thể ghi nhớ chính xác khuôn mặt của kẻ thù suốt 5 năm trời để truyền lại cho đàn con cháu đời sau tiếp tục báo thù?". Bố cục: Bộ não chim thiên tài: Bản chụp tia X hộp sọ chú Quạ Đen với bộ não phát sáng màu tím thông tuệ, chiếc mỏ khéo léo gắp que sắt uốn cong câu con sâu trong khúc gỗ mục. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>L74</summary>

```text
HÌNH L74 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đại học Miami đã công bố một phát hiện chấn động trên Tạp chí Sinh lý học Hoa Kỳ: Trong huyết tương và dịch ngoại bào của Ếch Gỗ Bắc Cực chứa một họ". Bố cục: Viện nghiên cứu sinh học Đại học Miami: Nhóm các nhà khoa học đang hào hứng quan sát mẫu huyết tương của chú ếch chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) dưới kính hiển vi điện tử. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>L75</summary>

```text
HÌNH L75 (16:9 ngang, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Xét theo mọi tiêu chuẩn và định nghĩa y khoa khắt khe nhất của con người, chú ếch gỗ lúc này đã bước vào trạng thái chết lâm sàng toàn diện 100%! Hãy quan sát diện mạo bên ngoài của chú ếch lúc này:". Bố cục: Bác sĩ cú mèo bác sĩ cú mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắng và cầm bảng theo dõi thông số sinh tồn cầm chiếc búa phản xạ y tế gõ vào đầu gối chú ếch chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles) đã đông cứng, lắc đầu xác nhận chết lâm sàng 100%.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Cảnh báo sinh tồn vùng cực -20°C! Tại sao loài ếch tí hon này có thể để tim ngừng đập hoàn toàn suốt 7 tháng mùa đông". Bố cục: chú chim cánh cụt phóng viên hoạt hình mặc áo phao lông thú ấm áp, cầm micro phỏng vấn run rẩy giữa trời tuyết rơi trùm áo phao lông thú giữa bão tuyết Alaska -20°C, chỉ tay về phía chiếc nhiệt kế đóng băng rực rỡ. KHÔNG có chú Ếch Gỗ trong cảnh này.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Khi mùa đông ập đến, thay vì trốn sâu dưới lòng đất, nó ở lì trên mặt đất và chủ động để cơ thể mình bị đóng băng!". Bố cục: chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực nằm tựa lưng trên lớp lá rêu mỏng manh sát mặt đất, thản nhiên đắp chiếc chăn lá cây chờ đợi mùa đông.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Một loại protein tạo mầm đá đặc biệt ép 65-70% lượng nước trong cơ thể nó hóa thành băng đá ngoại bào.". Bố cục: Sơ đồ cắt lớp cơ thể chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực: 70% lượng nước hóa thành giáp băng bao bọc bên ngoài bảo vệ bên trong cơ thể an toàn.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Để tế bào không bị xé rách, lá gan của nó lập tức phình to, bơm một lượng đường Glucose siêu đậm đặc gấp 300 lần vào". Bố cục: Lá gan chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực phình to mở van xả lũ, bơm dòng siro đường Glucose siêu đậm đặc gấp 300 lần vào từng tế bào.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Kết quả: Trái tim ngừng đập hoàn toàn ở mức 0 nhịp/phút. nước màu ngừng chảy, sóng". Bố cục: Màn hình điện tâm đồ ECG thẳng tắp: Tim 0 nhịp/phút, chú gấu Bắc Cực chú gấu Bắc Cực hoạt hình lông trắng to lớn mập mạp ngơ ngác, cầm một cành cây nhỏ gõ vào khối đá lạnh dùng que gõ vào chú ếch hóa đá kêu côm cốp.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Về mặt y học, nó đã chết lâm sàng 100%!". Bố cục: bác sĩ cú mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắng và cầm bảng theo dõi thông số sinh tồn giơ bảng kết luận chết lâm sàng 100% trong khi chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực hóa thành viên đá hoa cương suốt 200 ngày.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Thế nhưng khi ánh nắng mùa xuân rọi xuống,". Bố cục: Nắng ấm mùa xuân rọi xuống làm tan chảy băng tuyết, những mầm cây xanh non nhú lên xung quanh khối đá ếch gỗ.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "trái tim tự rã đông đầu tiên, tự động đập lại mà không cần sốc điện,". Bố cục: nhân vật trái tim hoạt hình màu đỏ đội mũ len nhỏ bị bọc trong tinh thể băng xanh lam trong suốt bừng sáng rực rỡ, tự phát xung điện sinh học và đập lại thình thịch mà không cần máy sốc điện.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "và chỉ vài tiếng sau chú ếch đã bật dậy nhảy tanh tách đi tìm bạn tình!". Bố cục: chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực bật dậy vươn vai rồi phóng từng bước nhảy dũng mãnh xuống hồ nước mùa xuân cất tiếng gọi bạn tình.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Một kiệt tác hồi sinh đang mở ra cuộc cách mạng bảo quản tạng ghép cho loài người!". Bố cục: chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực cười tươi nháy mắt bên cạnh nút Đăng ký kênh YouTube hoạt hình phát sáng rực rỡ.
```
</details>

<details><summary>S11</summary>

```text
HÌNH S11 (DỌC 9:16, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "rồi tự rã đông bật nhảy sống dậy? Đây là Ếch Gỗ Bắc Cực, Quái Kiệt Băng Giá của xứ sở Alaska!". Bố cục: chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực bật nhảy tanh tách từ khối đá băng tan, đôi mắt đeo kính bảo hộ lấp lánh cười toe toét.
```
</details>

<details><summary>S12</summary>

```text
HÌNH S12 (DỌC 9:16, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "bên trong từng tế bào như siro chống đông sinh học!". Bố cục: Cận cảnh tế bào nội bào chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực: Dòng siro vàng cam mật ong tràn vào ngập tràn tế bào, bảo vệ màng tế bào căng mọng an toàn.
```
</details>

<details><summary>S13</summary>

```text
HÌNH S13 (DỌC 9:16, cùng phong cách Cryo-Noir Graphic Novel 2D và cùng nhân vật chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "não phẳng lì, cơ thể cứng như đá gõ côm cốp suốt 200 ngày!". Bố cục: Bác sĩ cú mèo bác sĩ cú mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắng và cầm bảng theo dõi thông số sinh tồn đeo kính lúp soi vào chú ếch chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực hóa thành tảng đá hoa cương phủ sương tuyết, bên cạnh là máy EEG phẳng lì 0Hz.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/74 của video YouTube về Ếch Gỗ Bắc Cực). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa truyện tranh sinh tồn Bắc Cực Cryo-Noir Graphic Novel 2D: nét mực đen sắc sảo gai góc, các tinh thể băng tuyết lam ngọc sắc nhọn, phối hợp dải màu cam nhiệt kế sinh tồn rực rỡ tương phản mạnh mẽ, nền trắng tinh hoàn toàn, không watermark, không chữ, biểu cảm nhân vật hài hước kịch tính theo chuẩn khoa học.. NHÂN VẬT CHÍNH cố định: chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles). Nhân vật phụ cố định: chú chim cánh cụt phóng viên hoạt hình mặc áo phao lông thú ấm áp, cầm micro phỏng vấn run rẩy giữa trời tuyết rơi; chú gấu Bắc Cực hoạt hình lông trắng to lớn mập mạp ngơ ngác, cầm một cành cây nhỏ gõ vào khối đá lạnh; nhân vật trái tim hoạt hình màu đỏ đội mũ len nhỏ bị bọc trong tinh thể băng xanh lam trong suốt; bác sĩ cú mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắng và cầm bảng theo dõi thông số sinh tồn. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/13 của video YouTube Shorts về Ếch Gỗ Bắc Cực). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa truyện tranh sinh tồn Bắc Cực Cryo-Noir Graphic Novel 2D: nét mực đen sắc sảo gai góc, các tinh thể băng tuyết lam ngọc sắc nhọn, phối hợp dải màu cam nhiệt kế sinh tồn rực rỡ tương phản mạnh mẽ, nền trắng tinh hoàn toàn, không watermark, không chữ, biểu cảm nhân vật hài hước kịch tính theo chuẩn khoa học.. NHÂN VẬT CHÍNH cố định: chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles). Nhân vật phụ: chú chim cánh cụt phóng viên hoạt hình mặc áo phao lông thú ấm áp, cầm micro phỏng vấn run rẩy giữa trời tuyết rơi; chú gấu Bắc Cực hoạt hình lông trắng to lớn mập mạp ngơ ngác, cầm một cành cây nhỏ gõ vào khối đá lạnh; bác sĩ cú mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắng và cầm bảng theo dõi thông số sinh tồn. 
```
</details>

## 7. SEO

- **title:** Sinh Vật Tự Đóng Băng Tim Ngừng Đập & Hồi Sinh Sau Mùa Đông?! | Tập 33
- **hook_paragraph:** Ếch Gỗ Bắc Cực (Lithobates sylvaticus) sống sót qua mùa đông Alaska âm 20°C bằng khả năng không tưởng: để tim ngừng đập 0 nhịp/phút suốt 7 tháng, 70% cơ thể hóa đá, gan bơm đường glucose gấp 300 lần chống đông tế bào và tự đập lại hồi sinh thần kỳ vào mùa xuân!
- **question:** Giữa khả năng tự đóng băng 70% cơ thể thành đá và trái tim tự đập lại sau 7 tháng chết lâm sàng, bạn thấy điều kỳ diệu nào của Ếch Gỗ Bắc Cực đỉnh cao hơn?
- **next_teaser:** loài chim đen huyền bí sở hữu bộ não có tỷ lệ tương đương tinh tinh, biết uốn que sắt làm câu mồi và nhớ mặt kẻ thù suốt 5 năm
- **shorts_title:** Tại Sao Trái Tim Loài Ếch Này Ngừng Đập 7 Tháng Rồi Tự Sống Dậy?!
- **shorts_desc:** Ếch Gỗ Bắc Cực (Lithobates sylvaticus) để tim ngừng đập hoàn toàn suốt 7 tháng mùa đông Alaska -20°C, 70% cơ thể hóa đá nhờ gan bơm glucose gấp 300 lần chống đông và tự rã đông nhảy đi vào mùa xuân!
- **bullets:** Sinh tồn giữa bão tuyết Alaska -20°C mà không cần đào hang sâu hay lớp mỡ dày · Protein tạo mầm đá ngoại bào ép 70% lượng nước cơ thể đóng băng có kiểm soát · Lá gan phình to bơm glucose siêu đậm đặc gấp 300 lần làm siro chống đông tế bào · Trạng thái chết lâm sàng hoàn toàn: tim 0 nhịp, máu ngừng chảy, cơ thể hóa đá 200 ngày · Phép màu mùa xuân: Trái tim tự rã đông và tự đập lại đầu tiên không cần máy sốc điện · Ứng dụng y học đột phá: Mở rộng thời gian bảo quản nội tạng người ghép tạng từ vài giờ lên nhiều tháng
- **tags:** ếch gỗ bắc cực, ếch gỗ, wood frog, lithobates sylvaticus, động vật đóng băng, tim ngừng đập hồi sinh, sinh tồn bắc cực, chất chống đông sinh học, alaska âm 20 độ, thế giới động vật, vẽ chuyện hoang dã, whiteboard animation, khoa học vui, tập 33
- **hashtags:** #độngvật #ếchgỗ #VẽChuyệnHoangDã

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-33-ech-go-bac-cuc
python src/episode/pipeline.py tts    projects/tap-33-ech-go-bac-cuc     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-33-ech-go-bac-cuc     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-33-ech-go-bac-cuc     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-33-ech-go-bac-cuc              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-33-ech-go-bac-cuc --force
python scripts/beat_sheet.py projects/tap-33-ech-go-bac-cuc               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-33-ech-go-bac-cuc/audio/shorts.wav projects/tap-33-ech-go-bac-cuc/renders/tap-33-ech-go-bac-cuc_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-33-ech-go-bac-cuc
python src/episode/pipeline.py seo    projects/tap-33-ech-go-bac-cuc
python src/episode/episode_doc.py     projects/tap-33-ech-go-bac-cuc
```

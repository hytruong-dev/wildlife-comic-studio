# TẬP 39 — CHIM BÁCH THANH · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-39-chim-bach-thanh`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-39-chim-bach-thanh`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F4` · **Persona giọng:** `chuyen_gia_hinh_su` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Chim Bách Thanh |
| Tiêu đề YouTube | Hồ Sơ Sát Thủ Bụi Rậm: Chim Bách Thanh Xiên Cọc Con Mồi Tẩm Độc Để Dự Trữ Lương Thực?! \| Tập 39 |
| Video dài | `renders/tap-39-chim-bach-thanh_long.mp4` — 8:50.0 (530.0s) |
| Shorts | `renders/tap-39-chim-bach-thanh_shorts.mp4` — 0:43.5 (43.5s) |
| Thumbnail | `renders/tap-39-chim-bach-thanh_thumbnail.jpg` |
| Số hình | dài 70 beat / 70 ảnh riêng; Shorts 12 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.11**, Shorts tempo tự tính (≥ 1.06) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/70 của video YouTube về Chim Bách Thanh). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách bản vẽ phác thảo khám nghiệm hiện trường pháp y kết hợp truyện tranh điện ảnh trinh thám Noir (Forensic Crime Scene Sketch & Noir Pen-and-Ink): nét vẽ bút kim kỹ thuật đen trắng sắc sảo lạnh lùng, chi tiết thước đo tỉ lệ hiện trường màu vàng dạ quang neon, bảng manh mối ghim chỉ đỏ kết nối chứng cứ, vòng phấn đánh dấu hiện trường, kính lúp quang học soi vết cành gai nhọn, độ tương phản thị giác cực cao giàu tính điều tra phá án; NỀN TRẮNG TINH hoàn toàn, không watermark, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — KHÁM NGHIỆM HIỆN TRƯỜNG CÀNH GAI CẮM XÁC KỲ BÍ GIỮA RỪNG SÂU
*Thẻ chương:* Bức màn trinh thám về kẻ săn mồi đội lốt chim ca hót

*Badge:* `HIỆN TRƯỜNG VỤ ÁN` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene01_p0.wav` (510 ký tự) · mood `tram_bi_an`

```text
Chào mừng các thám tử tư, các chuyên gia giám định pháp y và những bộ óc đam mê suy luận phá án bước vào hồ sơ hình sự kỳ lạ bậc nhất của thế giới tự nhiên! [laughter] Hôm nay, phòng điều tra trọng án sinh thái của chúng tôi xin mời quý vị lật mở một tập tài liệu tuyệt mật, giải mã hiện trường của một bóng ma tội phạm có vẻ ngoài ngây thơ tựa thiên thần nhưng lại mang phong cách hành động của một đồ tể tàn nhẫn! Một vụ án hóc búa thách thức mọi định kiến thông thường của chúng ta về giới loài chim ca hót!
```
**Part 1** → `audio/vs/scene01_p1.wav` (361 ký tự) · mood `don_dap`

```text
Hãy nhìn vào cành cây mận gai cằn cỗi ven bìa rừng: Một hiện trường rùng rợn và quái đản đang phơi bày trước mắt chúng ta! Trên những chiếc gai nhọn hoắt dài năm xăng-ti-mét, hàng loạt con mồi từ thằn lằn, chuột đồng, ếch nhái cho đến những chú chim sẻ nhỏ bé đều bị xiên thủng qua cổ hoặc ức, treo lơ lửng giữa không trung như những xâu thịt nướng trong lò mổ!
```
**Part 2** → `audio/vs/scene01_p2.wav` (207 ký tự) · 🎭 cameo `co_tro_ly`

```text
[surprise-oh] Thưa Thanh tra trưởng, dấu vết khám nghiệm xác nhận tất cả các nạn nhân đều bị gãy đốt sống cổ chỉ bằng một nhát cắn cực kỳ hiểm hóc, không hề có dấu vết giằng co hay móng vuốt đại bàng cào xé!
```
**Part 3** → `audio/vs/scene01_p3.wav` (486 ký tự) · mood `tram_bi_an`

```text
Một quan sát hiện trường vô cùng sắc bén thưa trợ lý pháp y! Thủ phạm của vụ án liên hoàn này không phải là một con mãnh thú khổng lồ hay một con chim ưng dũng mãnh, mà lại là một chú chim sẻ nhỏ nhắn chỉ nặng vỏn vẹn năm mươi gam, mang bộ lông xám trắng thanh lịch và một dải lông đen tuyền vắt ngang mắt trông hệt như chiếc mặt nạ của hiệp sĩ Zorro! Sinh vật này mang tên khoa học thuộc họ Laniidae, nhưng giới điều tra tự nhiên gọi nó bằng danh xưng rợn gáy: Sát Thủ Đồ Tể Lừng Danh!
```
**Part 4** → `audio/vs/scene01_p4.wav` (332 ký tự) · mood `hao_hung`

```text
Tại sao một loài chim ca hót nhỏ bé lại sở hữu thói quen treo xác con mồi lên gai nhọn rùng rợn đến như vậy? Phải chăng đây là một hành vi tàn bạo bản năng, hay đằng sau đó là một chiến lược cơ học và hóa học sinh tồn thiên tài? Ngay sau đây, xin mời các bạn cùng tôi mở cánh cửa phòng giải phẫu để vạch trần vũ khí bí mật đầu tiên!
```

### scene02 — MẤU RĂNG MỎ CHIM ƯNG THU NHỎ BẺ GÃY ĐỐT SỐNG CỔ
*Thẻ chương:* Cấu trúc mỏ sát thủ tomial tooth độc nhất vô nhị

*Badge:* `VŨ KHÍ SỐ 1` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene02_p0.wav` (303 ký tự) · mood `don_dap`

```text
Xin mời các giám định viên cơ học hãy đặt chiếc mỏ của nghi phạm dưới kính hiển vi điện tử: Đây chính là vũ khí đoạt mạng then chốt! Mặc dù thuộc bộ Sẻ vốn chỉ quen ăn hạt và sâu bọ nhỏ, mỏ của Sát Thủ Đồ Tể Lừng Danh lại tiến hóa theo hướng của các loài chim săn mồi đỉnh cao như chim ưng hay chim cắt!
```
**Part 1** → `audio/vs/scene02_p1.wav` (230 ký tự) · mood `tram_bi_an`

```text
Đầu mỏ trên uốn cong quặp xuống sắc lẹm như một chiếc móc câu sắt. Nhưng chi tiết kinh hoàng nhất nằm ở hai bên rìa mỏ trên: Hai mấu răng xương nhọn hoắt mọc chìa ra ngoài, giới giải phẫu học gọi là cấu trúc mấu răng tomial tooth!
```
**Part 2** → `audio/vs/scene02_p2.wav` (324 ký tự) · mood `don_dap`

```text
Khi lao xuống tấn công con mồi từ trên cành cây cao, nó không cắn bừa bãi vào thân xác mà nhắm thẳng chuẩn xác vào gáy hoặc sau hộp sọ nạn nhân. Hai chiếc mấu răng tomial tooth sẽ cắm phập vào khoảng hở giữa các đốt sống cổ, sau đó hàm dưới khép chặt lại tạo lực đòn bẩy bẻ gãy tủy sống con mồi chỉ trong một phần mười giây!
```
**Part 3** → `audio/vs/scene02_p3.wav` (271 ký tự) · mood `hao_hung`

```text
Con mồi lập tức bị liệt toàn thân và chết lâm sàng trước cả khi kịp nhận ra điều gì vừa xảy ra. Một cú cắn kết liễu hoàn hảo, không lãng phí một mi-li-giun năng lượng nào, biến chú chim sẻ nhỏ bé thành một cỗ máy hành quyết chuẩn xác không thua kém gì đại bàng dũng mãnh!
```
**Part 4** → `audio/vs/scene02_p4.wav` (200 ký tự) · mood `tram_bi_an`

```text
Thế nhưng, sau khi hạ gục con mồi nặng gần bằng chính cơ thể mình, một vấn đề nan giải mới lại xuất hiện đối với sát thủ nhỏ con này. Đó là gì? Xin mời quý vị cùng tôi bước sang hiện trường tiếp theo!
```
**Part 5** → `audio/vs/scene02_p5.wav` (312 ký tự) · mood `hao_hung`

```text
Lực cắn đo được từ cơ hàm của chim bách thanh mạnh gấp ba lần so với bất kỳ loài chim nào có cùng kích cỡ cơ thể! Thậm chí khi săn bắt những con chuột đồng nặng gấp đôi cơ thể nó, cú bẻ cổ bằng mấu răng tomial tooth vẫn diễn ra chớp nhoáng đến mức con mồi không hề có cơ hội phản kháng dù chỉ là một cú cào xước!
```

### scene03 — CHIẾC ĐINH GAI THIÊN NHIÊN THAY THẾ BÀN CHÂN QUẮP MỒI
*Thẻ chương:* Khắc phục nhược điểm bàn chân sẻ bằng đòn bẩy ngoại vi

*Badge:* `VŨ KHÍ SỐ 2` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene03_p0.wav` (311 ký tự) · mood `hao_hung`

```text
Đây chính là nút thắt logic thú vị nhất trong toàn bộ hồ sơ vụ án: Tại sao chim bách thanh phải xiên con mồi lên cành gai? Các loài chim săn mồi thực thụ như đại bàng hay cú mèo sở hữu đôi bàn chân có cơ bắp khổng lồ cùng bộ móng vuốt sắc nhọn hình lưỡi liềm để ghim chặt con mồi xuống đất trong khi mỏ xé thịt.
```
**Part 1** → `audio/vs/scene03_p1.wav` (277 ký tự) · mood `tram_bi_an`

```text
Thế nhưng nghi phạm của chúng ta, dù sở hữu chiếc mỏ đại bàng, bàn chân của nó lại chỉ là bàn chân chim sẻ thông thường: Các ngón chân mảnh khảnh chỉ đủ lực để đậu bám trên cành cây chứ tuyệt đối không thể giữ chặt một con chuột đồng hay một chú thằn lằn to lớn đang giãy giụa!
```
**Part 2** → `audio/vs/scene03_p2.wav` (311 ký tự) · mood `don_dap`

```text
Để giải quyết nghịch lý cơ học này, Sát Thủ Đồ Tể Lừng Danh đã phát minh ra một giải pháp phỏng sinh học đỉnh cao: Sử dụng công cụ môi trường làm bàn kẹp trợ lực! Nó tha xác con mồi đến những bụi cây có gai nhọn dài như gai bồ kết, gai mận rừng, hoặc thậm chí là các hàng rào dây thép gai do con người dựng lên!
```
**Part 3** → `audio/vs/scene03_p3.wav` (293 ký tự) · mood `hao_hung`

```text
Nó dùng toàn lực cắm phập xác nạn nhân vào chiếc gai nhọn, biến chiếc gai thành một chiếc kẹp cố định vĩnh cửu. Khi con mồi đã bị khóa cứng tại chỗ, chú chim có thể thong thả dùng chiếc mỏ móc câu của mình để xé nhỏ từng thớ thịt một cách nhàn nhã mà không cần tốn chút sức lực nào để ghì giữ!
```
**Part 4** → `audio/vs/scene03_p4.wav` (207 ký tự) · mood `tram_bi_an`

```text
Một bằng chứng hùng hồn cho thấy trí thông minh sử dụng ngoại vật phi thường của loài chim! Nhưng hiện trường cành gai không chỉ đơn thuần là bàn ăn dã chiến, nó còn là một kho dự trữ hóa học cực kỳ tinh vi!
```
**Part 5** → `audio/vs/scene03_p5.wav` (406 ký tự) · mood `tram_bi_an`

```text
Đáng kinh ngạc hơn nữa, mỗi chú chim bách thanh sở hữu một bản đồ trí nhớ không gian hoàn hảo về hàng trăm chiếc gai nhọn trong phạm vi lãnh thổ rộng hàng chục héc-ta của nó! Nó ghi nhớ chính xác vị trí nào có cành gai phù hợp với kích thước từng con mồi: Gai mảnh cho thằn lằn và cào cào, gai chạc ba dày dặn cho chuột đồng và chim sẻ, tạo thành một hệ thống kho tàng thực phẩm dã ngoại quy củ và bài bản!
```

### scene04 — KHO BẢO QUẢN VÀ GIẢI TRỪ ĐỘC TỐ CON MỒI SUỐT BỐN MƯƠI TÁM GIỜ
*Thẻ chương:* Chiến lược hóa sinh biến thức ăn độc hại thành bữa tiệc an toàn

*Badge:* `VŨ KHÍ SỐ 3` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene04_p0.wav` (544 ký tự) · mood `tram_bi_an`

```text
Xin mời các nhà hóa nghiệm pháp y cùng phân tích mẫu vật kỳ lạ nhất tìm thấy trên giá treo gai: Đó là những chú cào cào lubber khổng lồ màu vàng đen rực rỡ! Trong tự nhiên, loài cào cào này tích tụ hàm lượng chất độc cardenolide cực mạnh trong cơ thể, có thể làm tê liệt tim và gây nôn mửa dữ dội cho bất kỳ loài chim nào dại dột nuốt phải. Mỗi cành gai nhọn hoắt trong lãnh địa của nó không chỉ đơn thuần là bàn ăn dã chiến, mà còn là một kho tàng bí mật ẩn chứa những bất ngờ hóa học vượt ngoài sức tưởng tượng của các nhà khoa học đương đại!
```
**Part 1** → `audio/vs/scene04_p1.wav` (237 ký tự) · mood `don_dap`

```text
Mọi loài chim săn mồi khác đều phải tránh xa món ăn chết chóc này. Thế nhưng Sát Thủ Đồ Tể Lừng Danh lại thản nhiên bắt sống những con cào cào độc và xiên chúng lên cành gai nhọn hoắt phơi nắng! Tại sao nó không ăn ngay mà lại treo ở đó?
```
**Part 2** → `audio/vs/scene04_p2.wav` (204 ký tự) · mood `tram_bi_an`

```text
Bí mật nằm ở chỗ: Độc tố cardenolide trong cơ thể cào cào sẽ bị phân hủy sinh học và bay hơi hoàn toàn dưới tác động của ánh nắng mặt trời và gió sau khoảng bốn mươi tám giờ đến bảy mươi hai giờ phơi khô!
```
**Part 3** → `audio/vs/scene04_p3.wav` (318 ký tự) · mood `hao_hung`

```text
Chú chim bách thanh kiên nhẫn chờ đợi đúng hai ngày đêm cho đến khi các phản ứng hóa học tự nhiên biến con mồi độc hại thành một miếng mồi khô thơm ngon và hoàn toàn vô hại rồi mới quay lại thưởng thức! [laughter] Đây chẳng khác nào quy trình ủ thực phẩm lên men hoặc phơi khô thịt bò của các đầu bếp ẩm thực hàng đầu!
```
**Part 4** → `audio/vs/scene04_p4.wav` (203 ký tự) · mood `tram_bi_an`

```text
Vừa là kho lương thực chống đói trong mùa đông khan hiếm, vừa là nhà máy xử lý chất độc tự nhiên. Khả năng tính toán thời gian và hóa sinh của loài chim này thực sự khiến con người phải ngả mũ thán phục!
```
**Part 5** → `audio/vs/scene04_p5.wav` (362 ký tự) · mood `hao_hung`

```text
Trong mùa sinh sản vào mùa xuân, số lượng con mồi được xiên trên các cành gai nhọn xung quanh tổ chính là thước đo độ giàu có và tài năng săn mồi của con đực! Những chú chim mái sẽ bay đi kiểm tra từng cây gai, và con đực nào sở hữu một hàng rào gai treo đầy chuột đồng, thằn lằn và cào cào béo ngậy sẽ lập tức chiếm trọn trái tim của bạn tình để cùng xây tổ ấm!
```

### scene05 — BẬC THẦY NHẠI GIỌNG HÓT DỤ DỖ CON MỒI VÀO BẪY PHỤC KÍCH
*Thẻ chương:* Nghệ thuật cải trang âm thanh đánh lừa cả khu rừng

*Badge:* `VŨ KHÍ SỐ 4` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene05_p0.wav` (319 ký tự) · mood `hao_hung`

```text
Và để khép lại bản cáo trạng điều tra, chúng ta không thể bỏ qua ngón đòn lừa đảo tâm lý đỉnh cao nhất của kẻ thủ ác: Nghệ thuật cải trang giọng hót dụ mồi! Là một thành viên xuất sắc của bộ Sẻ biết ca hót, chim bách thanh sở hữu thanh quản cực kỳ linh hoạt có thể bắt chước tiếng kêu của hàng chục loài chim khác nhau!
```
**Part 1** → `audio/vs/scene05_p1.wav` (274 ký tự) · mood `don_dap`

```text
Khi đi săn, nó sẽ nấp kín trong tán lá rậm rạp và cất lên tiếng hót lảnh lót giả dạng tiếng chim sẻ non đang đòi ăn hoặc tiếng chim bạn tình đang gọi đàn. Những chú chim nhỏ ngây thơ nghe thấy tiếng đồng loại liền mất cảnh giác bay lại gần bụi cây để tìm kiếm bạn đồng hành.
```
**Part 2** → `audio/vs/scene05_p2.wav` (155 ký tự) · 🎭 cameo `co_tro_ly`

```text
[surprise-oh] Thưa Thanh tra, nghĩa là nó dùng chính giọng hót thánh thót ngọt ngào để dẫn dụ nạn nhân vào tầm ngắm tử thần mà không cần tốn công đuổi bắt?
```
**Part 3** → `audio/vs/scene05_p3.wav` (259 ký tự) · mood `don_dap`

```text
Chính xác một trăm phần trăm! Ngay khi con mồi bay vào cự ly phục kích chưa đầy hai mét, Sát Thủ Đồ Tể Lừng Danh sẽ lao ra như một mũi tên xé gió, tung cú cắn bẻ cổ thần tốc trước khi nạn nhân kịp nhận ra kẻ vừa cất tiếng hát ngọt ngào lại chính là thần chết!
```
**Part 4** → `audio/vs/scene05_p4.wav` (197 ký tự) · mood `tram_bi_an`

```text
Từ chiếc mặt nạ đen ngụy trang, giọng hót quyến rũ chết người, chiếc mỏ bẻ cổ siêu tốc cho đến giá treo gai nhọn đa năng, toàn bộ kế hoạch săn mồi tạo thành một chuỗi mắt xích hoàn mỹ không tì vết!
```
**Part 5** → `audio/vs/scene05_p5.wav` (343 ký tự) · mood `don_dap`

```text
Cơ quan phát âm syrinx của chim bách thanh sở hữu các bó cơ độc lập có thể kiểm soát hai luồng âm thanh cùng lúc! Điều này cho phép nó tạo ra những âm điệu phức tạp, từ tiếng chích chòe líu lo cho đến tiếng chim sẻ non nỉ non cầu cứu, khiến ngay cả những kẻ quan sát dày dạn kinh nghiệm nhất cũng dễ dàng bị mắc lừa nếu chỉ lắng nghe bằng tai!
```

### scene06 — TÔN VINH KIỆT TÁC SINH TỒN VÀ CÂN BẰNG SINH THÁI
*Thẻ chương:* Khép lại vụ án với góc nhìn tôn trọng quy luật tự nhiên

*Badge:* `KẾT LUẬN ĐIỀU TRA` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene06_p0.wav` (305 ký tự) · mood `hao_hung`

```text
Kính thưa toàn thể ban chuyên án và quý khán giả theo dõi hồ sơ vụ án, sau khi làm rõ toàn bộ bốn bằng chứng từ mỏ móc câu bẻ cổ, bàn kẹp gai nhọn trợ lực, kho phân hủy độc tố bốn mươi tám giờ cho đến giọng hót phục kích thiên tài, chúng tôi xin tuyên bố khép lại tập tài liệu điều tra về Chim Bách Thanh!
```
**Part 1** → `audio/vs/scene06_p1.wav` (301 ký tự) · mood `tram_bi_an`

```text
Dù thói quen xiên mồi lên cành gai có phần đáng sợ trong mắt con người, nhưng đối với hệ sinh thái đồng cỏ và bìa rừng, Sát Thủ Đồ Tể Lừng Danh chính là một mắt xích kiểm soát số lượng côn trùng gây hại và các loài gặm nhấm cực kỳ hữu ích, giữ cho cán cân tự nhiên luôn ở trạng thái cân bằng hoàn hảo.
```
**Part 2** → `audio/vs/scene06_p2.wav` (432 ký tự) · mood `am_ap`

```text
Bài học phá án hôm nay nhắc nhở chúng ta rằng: Đừng bao giờ đánh giá một sinh vật chỉ qua vẻ bề ngoài dễ thương hay giọng hót ngọt ngào! Sự sinh tồn trong thế giới hoang dã luôn đòi hỏi những chiến lược thích nghi thông minh và kiên cường vượt qua mọi giới hạn của cơ thể! Trong cuộc sống cũng vậy, sự nhạy bén và năng lực tận dụng tối đa những nguồn lực sẵn có xung quanh sẽ là chìa khóa mở ra cánh cửa thành công cho mỗi chúng ta!
```
**Part 3** → `audio/vs/scene06_p3.wav` (233 ký tự) · mood `hao_hung`

```text
Giữa kỹ thuật bẻ cổ bằng mấu răng tomial tooth và chiếc bẫy gai nhọn giải độc, tuyệt chiêu nào của chú chim bách thanh khiến bạn rùng mình và thán phục nhất? Hãy chia sẻ suy luận phá án của bạn ngay trong phần bình luận bên dưới nhé!
```
**Part 4** → `audio/vs/scene06_p4.wav` (239 ký tự) · mood `am_ap`

```text
Và đừng quên nhấn nút Đăng Ký Kênh cùng chiếc chuông thông báo để không bỏ lỡ Tập bốn mươi: Khám phá siêu kiến trúc quân sự của Kiến Cắt Lá! Xin chào tạm biệt và hẹn gặp lại toàn thể các thám tử trong những vụ án tự nhiên kỳ thú tiếp theo!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Bạn có tin một chú chim nhỏ nặng chỉ năm mươi gam với vẻ ngoài ngây thơ lại mang danh hiệu Sát Thủ Đồ Tể khét tiếng nhất thế giới tự nhiên không? [laughter] Đó chính là Chim Bách Thanh! Bí mật rợn người nằm ở chiếc mỏ móc câu có hai mấu răng xương sắc bén có thể bẻ gãy đốt sống cổ con mồi chỉ trong chớp mắt! [dissatisfaction-hnn] Vì đôi chân chim sẻ quá yếu không thể giữ chặt mồi, nó đã sáng tạo ra một tuyệt chiêu độc nhất vô nhị: Xiên thủng xác con mồi lên những chiếc gai cây nhọn hoắt hoặc hàng rào dây thép gai để làm điểm tựa xé thịt! Thậm chí những con cào cào cực độc cũng bị nó treo gai phơi nắng suốt bốn mươi tám giờ cho bay hết chất độc rồi mới ăn! [laughter] Một kho lương thực rùng rợn biến nó thành thám tử sát thủ thiên tài của bụi rậm!
```

**Whisper prompt:** `Chim Bách Thanh, Laniidae, Lanius, Sát Thủ Đồ Tể Lừng Danh, gai nhọn, bẻ cổ, mấu răng mỏ chim, cào cào độc, 48 giờ, trinh thám hình sự`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| Tập ba mươi chín | Tập 39 |
| Tập bốn mươi | Tập 40 |
| bốn mươi tám giờ | 48 giờ |
| bảy mươi hai giờ | 72 giờ |
| hai mươi bốn giờ | 24 giờ |
| hai mươi xăng-ti-mét | 20cm |
| mười lăm xăng-ti-mét | 15cm |
| ba mươi xăng-ti-mét | 30cm |
| năm xăng-ti-mét | 5cm |
| năm mươi gam | 50g |
| bảy mươi gam | 70g |
| một trăm phần trăm | 100% |
| năm mươi phần trăm | 50% |
| hai lần | 2 lần |
| ba lần | 3 lần |
| mười lần | 10 lần |
| thế kỷ hai mươi mốt | thế kỷ 21 |
| hàng triệu năm | hàng triệu năm |
| triệu năm | triệu năm |
| Sát Thủ Đồ Tể Lừng Danh | Sát Thủ Đồ Tể Lừng Danh |
| Laniidae | Laniidae |
| Lanius | Lanius |
| tomial tooth | tomial tooth |
| Sherlock Holmes | Sherlock Holmes |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · KHÁM NGHIỆM HIỆN TRƯỜNG CÀNH GAI CẮM XÁC KỲ BÍ GIỮA RỪNG SÂU · 93.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.5 (9.5s) | L01 | Chào mừng các thám tử tư, các chuyên gia giám định pháp y và những bộ óc đam mê suy luận phá án bước vào hồ sơ hình sự kỳ lạ bậc nhất của thế giới tự nhiên! Hôm nay, |  | Phòng điều tra trọng án sinh thái: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền trong vai thám tử trưởng chỉ gậy vào bảng chứng cứ gắn đầy ảnh và chỉ đỏ. |
| b02 | 00:09.5–00:13.4 (4.0s) | L02 | phòng điều tra trọng án sinh thái của chúng tôi xin mời quý vị lật mở một tập tài liệu tuyệt mật, |  | Cận cảnh tập hồ sơ tuyệt mật màu nâu đề chữ Tuyệt Mật và dấu vân tay hiện trường vụ án bí ẩn. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b03 | 00:13.4–00:20.1 (6.6s) | L03 | giải mã hiện trường của một bóng ma tội phạm có vẻ ngoài ngây thơ tựa thiên thần nhưng lại mang phong cách hành động của một đồ tể tàn nhẫn! |  | Bóng đen bí ẩn mang mặt nạ hiệp sĩ Zorro lướt qua màn sương đêm bìa rừng u ám. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b04 | 00:20.1–00:24.5 (4.5s) | L04 | Một vụ án hóc búa thách thức mọi định kiến thông thường của chúng ta về giới loài chim ca hót! |  | chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền ngồi chống cằm suy tư bên bàn làm việc đầy hồ sơ và kính lúp quang học kiểu trinh thám cổ điển. |
| b05 | 00:24.5–00:27.3 (2.8s) | L05 | Hãy nhìn vào cành cây mận gai cằn cỗi ven bìa rừng: |  | Hiện trường bìa rừng: Bụi cây mận gai cằn cỗi với những nhánh gai nhọn dài lởm chởm trong sương mù. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b06 | 00:27.3–00:32.9 (5.6s) | L06 | Một hiện trường rùng rợn và quái đản đang phơi bày trước mắt chúng ta! Trên những chiếc gai nhọn hoắt dài 5cm, |  | Vòng tròn phấn trắng và thước dây pháp y vàng neon bao quanh cành cây có những chiếc gai nhọn 5cm sắc lẹm. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b07 | 00:32.9–00:36.8 (3.9s) | L07 | hàng loạt con mồi từ thằn lằn, chuột đồng, ếch nhái cho đến những chú chim sẻ nhỏ bé đều |  | Xác thằn lằn, chuột đồng và chim sẻ nhỏ bị xiên treo lơ lửng trên các cành gai nhọn ven đường. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b08 | 00:36.8–00:42.4 (5.6s) | L08 | bị xiên thủng qua cổ hoặc ức, treo lơ lửng giữa không trung như những xâu thịt nướng trong lò mổ! |  | Cận cảnh giám định pháp y: Đầu gai nhọn cắm xuyên qua gáy con mồi chuẩn xác đến từng mi-li-mét. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b09 | 00:42.4–00:54.8 (12.4s) | L09 | Thưa Thanh tra trưởng, dấu vết khám nghiệm xác nhận tất cả các nạn nhân đều bị gãy đốt sống cổ chỉ bằng một nhát cắn cực kỳ hiểm hóc, không hề có dấu vết giằng co hay móng vuốt đại bàng cào xé! Một quan sát hiện trường vô cùng sắc bén thưa trợ lý |  | Cô trợ lý pháp y đeo kính trắng cầm bảng kẹp hồ sơ báo cáo kết quả khám nghiệm hiện trường. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b10 | 00:54.8–01:06.6 (11.8s) | L10 | pháp y! Thủ phạm của vụ án liên hoàn này không phải là một con mãnh thú khổng lồ hay một con chim ưng dũng mãnh, mà lại là một chú chim sẻ nhỏ nhắn chỉ nặng vỏn vẹn 50g, mang bộ lông xám trắng thanh lịch và một dải lông đen tuyền vắt ngang mắt trông hệt |  | Sơ đồ giải phẫu hiển vi cho thấy đốt sống cổ bị bẻ gãy gập bằng một lực cắt chớp nhoáng không tì vết. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b11 | 01:06.6–01:18.7 (12.1s) | L11 | như chiếc mặt nạ của hiệp sĩ Zorro! Sinh vật này mang tên khoa học thuộc họ Laniidae, nhưng giới điều tra tự nhiên gọi nó bằng danh xưng rợn gáy: Sát Thủ Đồ Tể Lừng Danh! Tại sao một loài chim ca hót nhỏ bé lại sở hữu thói |  | chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền xuất hiện trong vùng sáng đèn rọi, ánh mắt sắc bén lấp lánh sau dải lông đen ngang mắt. |
| b12 | 01:18.7–01:33.0 (14.3s) | L12 | quen treo xác con mồi lên gai nhọn rùng rợn đến như vậy? Phải chăng đây là một hành vi tàn bạo bản năng, hay đằng sau đó là một chiến lược cơ học và hóa học sinh tồn thiên tài? Ngay sau đây, xin mời các bạn cùng tôi mở cánh cửa phòng giải phẫu để vạch trần vũ khí bí mật đầu tiên! |  | Bảng chân dung truy nã pháp y: Chú chim bách thanh họ Laniidae với danh xưng Sát Thủ Đồ Tể Lừng Danh. |

### scene02 · MẤU RĂNG MỎ CHIM ƯNG THU NHỎ BẺ GÃY ĐỐT SỐNG CỔ · 81.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:04.1 (4.1s) | L13 | Xin mời các giám định viên cơ học hãy đặt chiếc mỏ của nghi phạm dưới kính hiển vi điện tử: |  | Phòng giải phẫu cơ học: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền đứng bên cạnh mô hình kính hiển vi điện tử chiếu rọi cấu trúc đầu chim. |
| b02 | 00:04.1–00:10.5 (6.3s) | L14 | Đây chính là vũ khí đoạt mạng then chốt! Mặc dù thuộc bộ Sẻ vốn chỉ quen ăn hạt và sâu bọ nhỏ, mỏ của Sát Thủ Đồ Tể Lừng Danh |  | Mô hình 3D chiếc mỏ sát thủ phóng to với các tia laser đo đạc lực cắn và góc uốn cong nguy hiểm. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b03 | 00:10.5–00:14.2 (3.8s) | L15 | lại tiến hóa theo hướng của các loài chim săn mồi đỉnh cao như chim ưng hay chim cắt! |  | Bản vẽ so sánh: Chiếc mỏ bách thanh mang cấu trúc thu nhỏ của chim ưng và chim cắt dũng mãnh. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b04 | 00:14.2–00:20.5 (6.3s) | L16 | Đầu mỏ trên uốn cong quặp xuống sắc lẹm như một chiếc móc câu sắt. Nhưng chi tiết kinh hoàng nhất nằm ở hai bên rìa mỏ trên: |  | Cận cảnh đầu mỏ trên uốn quặp xuống như móc câu sắt bằng thép tôi luyện đen nhánh. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b05 | 00:20.5–00:25.8 (5.3s) | L17 | Hai mấu răng xương nhọn hoắt mọc chìa ra ngoài, giới giải phẫu học gọi là cấu trúc mấu răng tomial tooth! |  | Phóng to hai mấu răng xương tomial tooth sắc nhọn ở hai bên rìa mỏ trên với mũi tên chỉ thị vàng neon. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b06 | 00:25.8–00:28.6 (2.8s) | L18 | Khi lao xuống tấn công con mồi từ trên cành cây cao, |  | chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền lao bổ nhào từ cành cây cao xuống như một mũi tên xé gió với đôi cánh khép gọn. |
| b07 | 00:28.6–00:32.2 (3.6s) | L19 | nó không cắn bừa bãi vào thân xác mà nhắm thẳng chuẩn xác vào gáy hoặc sau hộp sọ |  | Tâm ngắm chữ thập màu đỏ khóa chặt vào gáy và sau hộp sọ của con chuột đồng đang gặm cỏ. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b08 | 00:32.2–00:38.3 (6.2s) | L20 | nạn nhân. Hai chiếc mấu răng tomial tooth sẽ cắm phập vào khoảng hở giữa các đốt sống cổ, sau đó hàm dưới khép chặt lại tạo lực đòn |  | Khoảnh khắc mấu răng tomial tooth cắm phập vào khe hở giữa hai đốt sống cổ tạo lực đòn bẩy cực đại. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b09 | 00:38.3–00:46.2 (7.9s) | L21 | bẩy bẻ gãy tủy sống con mồi chỉ trong một phần mười giây! Con mồi lập tức bị liệt toàn thân và chết lâm sàng trước cả khi kịp nhận ra điều gì vừa xảy |  | Đồng hồ bấm giờ điện tử ghi nhận 0.1 giây: Đốt sống cổ đứt lìa hoàn toàn, con mồi mất tri giác. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b10 | 00:46.2–00:58.9 (12.7s) | L22 | ra. Một cú cắn kết liễu hoàn hảo, không lãng phí một mi-li-giun năng lượng nào, biến chú chim sẻ nhỏ bé thành một cỗ máy hành quyết chuẩn xác không thua kém gì đại bàng dũng mãnh! Thế nhưng, sau khi hạ gục con mồi nặng gần bằng chính cơ thể mình, |  | chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền đứng trên con mồi đã bất động hoàn toàn, thể hiện độ chính xác tuyệt đối không tốn sức. |
| b11 | 00:58.9–01:11.1 (12.1s) | L23 | một vấn đề nan giải mới lại xuất hiện đối với sát thủ nhỏ con này. Đó là gì? Xin mời quý vị cùng tôi bước sang hiện trường tiếp theo! Lực cắn đo được từ cơ hàm của chim bách thanh mạnh gấp 3 lần so với bất kỳ loài chim nào có cùng kích cỡ cơ thể! |  | chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền đứng gãi đầu nhìn con mồi nặng bằng chính mình, đối mặt với bài toán cơ học nan giải. |
| b12 | 01:11.1–01:21.5 (10.4s) | L24 | Thậm chí khi săn bắt những con chuột đồng nặng gấp đôi cơ thể nó, cú bẻ cổ bằng mấu răng tomial tooth vẫn diễn ra chớp nhoáng đến mức con mồi không hề có cơ hội phản kháng dù chỉ là một cú cào xước! |  | Biểu đồ cột so sánh: Lực cắn cơ hàm chim bách thanh cao gấp 3 lần chim cùng kích cỡ. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |

### scene03 · CHIẾC ĐINH GAI THIÊN NHIÊN THAY THẾ BÀN CHÂN QUẮP MỒI · 90.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:03.6 (3.6s) | L25 | Đây chính là nút thắt logic thú vị nhất trong toàn bộ hồ sơ vụ án: |  | Khu vực trưng bày vũ khí số 2: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền đứng cạnh cành cây gai bồ kết khổng lồ với nụ cười bí ẩn. |
| b02 | 00:03.6–00:06.7 (3.1s) | L26 | Tại sao chim bách thanh phải xiên con mồi lên cành gai? |  | Dấu chấm hỏi lớn màu đỏ trên nền cành gai nhọn hoắt cắm xác con mồi giữa sương mù. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b03 | 00:06.7–00:16.3 (9.6s) | L27 | Các loài chim săn mồi thực thụ như đại bàng hay cú mèo sở hữu đôi bàn chân có cơ bắp khổng lồ cùng bộ móng vuốt sắc nhọn hình lưỡi liềm để ghim chặt con mồi xuống đất trong khi mỏ xé thịt. |  | Bàn chân đại bàng lực lưỡng với những móng vuốt cong vút ghim chặt con mồi xuống tảng đá. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b04 | 00:16.3–00:22.4 (6.1s) | L28 | Thế nhưng nghi phạm của chúng ta, dù sở hữu chiếc mỏ đại bàng, bàn chân của nó lại chỉ là bàn chân chim sẻ thông thường: |  | Cận cảnh bàn chân chim sẻ mảnh khảnh của chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền với các ngón nhỏ chỉ đủ để đậu cành cây. |
| b05 | 00:22.4–00:30.0 (7.7s) | L29 | Các ngón chân mảnh khảnh chỉ đủ lực để đậu bám trên cành cây chứ tuyệt đối không thể giữ chặt một con chuột đồng hay một chú thằn lằn to lớn đang giãy giụa! |  | Hình ảnh con thằn lằn trơn trượt tuột khỏi đôi bàn chân nhỏ bé không có móng quắp. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b06 | 00:30.0–00:37.4 (7.4s) | L30 | Để giải quyết nghịch lý cơ học này, Sát Thủ Đồ Tể Lừng Danh đã phát minh ra một giải pháp phỏng sinh học đỉnh cao: Sử dụng công cụ môi trường làm bàn kẹp trợ lực! |  | chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền nảy ra ý tưởng phát minh thông minh, bóng đèn sáng rực trên đầu trong phòng thí nghiệm rừng. |
| b07 | 00:37.4–00:44.6 (7.2s) | L31 | Nó tha xác con mồi đến những bụi cây có gai nhọn dài như gai bồ kết, gai mận rừng, hoặc thậm chí là các hàng rào dây thép gai do con người dựng lên! |  | chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền ngậm xác con mồi bay đến hàng rào dây thép gai và bụi mận gai nhọn hoắt. |
| b08 | 00:44.6–00:53.5 (8.9s) | L32 | Nó dùng toàn lực cắm phập xác nạn nhân vào chiếc gai nhọn, biến chiếc gai thành một chiếc kẹp cố định vĩnh cửu. Khi con mồi đã bị khóa cứng tại chỗ, chú chim |  | chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền dùng toàn lực ấn mạnh xác con mồi ghim chặt vào chiếc đinh gai nhọn như chiếc kẹp bàn thợ cơ khí. |
| b09 | 00:53.5–01:00.0 (6.6s) | L33 | có thể thong thả dùng chiếc mỏ móc câu của mình để xé nhỏ từng thớ thịt một cách nhàn nhã mà không cần tốn chút sức lực nào để ghì giữ! |  | chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền nhàn nhã dùng mỏ móc xé từng miếng thịt nhỏ khi con mồi đã bị cố định vững chắc trên gai. |
| b10 | 01:00.0–01:10.3 (10.3s) | L34 | Một bằng chứng hùng hồn cho thấy trí thông minh sử dụng ngoại vật phi thường của loài chim! Nhưng hiện trường cành gai không chỉ đơn thuần là bàn ăn dã chiến, nó còn là một kho dự trữ hóa học cực kỳ tinh vi! |  | Bản vẽ phỏng sinh học: Chiếc gai nhọn biến thành cánh tay đòn cơ học ngoại vi thiên tài. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b11 | 01:10.3–01:22.4 (12.1s) | L35 | Đáng kinh ngạc hơn nữa, mỗi chú chim bách thanh sở hữu một bản đồ trí nhớ không gian hoàn hảo về hàng trăm chiếc gai nhọn trong phạm vi lãnh thổ rộng hàng chục héc-ta của nó! Nó ghi nhớ chính xác vị trí nào có cành gai phù hợp với kích thước từng con mồi: |  | Bản đồ vệ tinh lãnh thổ rừng với hàng trăm điểm đánh dấu cành gai được lưu trữ trong trí nhớ của chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền. |
| b12 | 01:22.4–01:30.0 (7.6s) | L36 | Gai mảnh cho thằn lằn và cào cào, gai chạc ba dày dặn cho chuột đồng và chim sẻ, tạo thành một hệ thống kho tàng thực phẩm dã ngoại quy củ và bài bản! |  | Sơ đồ kho bãi tự nhiên: Phân loại gai mảnh cho cào cào và gai chạc ba cho chuột đồng béo ngậy. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |

### scene04 · KHO BẢO QUẢN VÀ GIẢI TRỪ ĐỘC TỐ CON MỒI SUỐT BỐN MƯƠI TÁM GIỜ · 93.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.1 (9.1s) | L37 | Xin mời các nhà hóa nghiệm pháp y cùng phân tích mẫu vật kỳ lạ nhất tìm thấy trên giá treo gai: Đó là những chú cào cào lubber khổng lồ màu vàng đen rực rỡ! Trong tự nhiên, |  | Phòng hóa nghiệm sinh hóa: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền đeo kính bảo hộ bên cạnh các ống nghiệm chứa chất độc màu tím và xanh lục. |
| b02 | 00:09.1–00:16.4 (7.3s) | L38 | loài cào cào này tích tụ hàm lượng chất độc cardenolide cực mạnh trong cơ thể, có thể làm tê liệt tim và gây nôn mửa dữ dội cho bất kỳ loài chim nào dại dột nuốt |  | Cận cảnh chú cào cào lubber khổng lồ thân màu vàng sọc đen bóng bẩy nằm dưới kính lúp. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b03 | 00:16.4–00:26.4 (10.0s) | L39 | phải. Mỗi cành gai nhọn hoắt trong lãnh địa của nó không chỉ đơn thuần là bàn ăn dã chiến, mà còn là một kho tàng bí mật ẩn chứa những bất ngờ hóa học vượt ngoài sức tưởng tượng của các nhà khoa học đương đại! |  | Công thức hóa học cardenolide phát sáng cảnh báo nguy hiểm độc tố làm ngừng tim. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b04 | 00:26.4–00:33.1 (6.6s) | L40 | Mọi loài chim săn mồi khác đều phải tránh xa món ăn chết chóc này. Thế nhưng Sát Thủ Đồ Tể Lừng Danh lại thản nhiên bắt sống những con cào cào độc |  | Các chú chim rừng khác sợ hãi bay dạt ra xa khi thấy chú cào cào độc lubber. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b05 | 00:33.1–00:37.7 (4.6s) | L41 | và xiên chúng lên cành gai nhọn hoắt phơi nắng! Tại sao nó không ăn ngay mà lại treo ở đó? |  | chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền thản nhiên ghim chú cào cào độc lên cành gai cao nhất phơi dưới ánh nắng mặt trời rực rỡ. |
| b06 | 00:37.7–00:45.0 (7.3s) | L42 | Bí mật nằm ở chỗ: Độc tố cardenolide trong cơ thể cào cào sẽ bị phân hủy sinh học và bay hơi hoàn toàn dưới tác động của ánh nắng mặt trời |  | Tia nắng mặt trời và những luồng gió tự nhiên phá vỡ chuỗi phân tử độc tố cardenolide. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b07 | 00:45.0–00:47.9 (2.9s) | L43 | và gió sau khoảng 48 giờ đến 72 giờ phơi khô! |  | Đồng hồ cát điện tử đếm ngược từ 48 giờ đến 72 giờ: Độc tố giảm dần về 0%. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b08 | 00:47.9–00:59.0 (11.1s) | L44 | Chú chim bách thanh kiên nhẫn chờ đợi đúng hai ngày đêm cho đến khi các phản ứng hóa học tự nhiên biến con mồi độc hại thành một miếng mồi khô thơm ngon và hoàn toàn vô hại rồi mới quay lại thưởng thức! |  | chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền đeo khăn ăn cầm dao nĩa phong cách ẩm thực, thưởng thức món cào cào khô đã sạch độc tố. |
| b09 | 00:59.0–01:04.8 (5.8s) | L45 | Đây chẳng khác nào quy trình ủ thực phẩm lên men hoặc phơi khô thịt bò của các đầu bếp ẩm thực hàng đầu! |  | Bếp trưởng ẩm thực rừng xanh: Quy trình ủ men và phơi thịt bò khô của tự nhiên hoang dã. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b10 | 01:04.8–01:14.7 (10.0s) | L46 | Vừa là kho lương thực chống đói trong mùa đông khan hiếm, vừa là nhà máy xử lý chất độc tự nhiên. Khả năng tính toán thời gian và hóa sinh của loài chim này thực sự khiến con người phải ngả mũ thán phục! |  | Cành gai phủ đầy tuyết trắng mùa đông treo các gói mồi khô thơm ngon làm lương thực dự trữ. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b11 | 01:14.7–01:22.5 (7.8s) | L47 | Trong mùa sinh sản vào mùa xuân, số lượng con mồi được xiên trên các cành gai nhọn xung quanh tổ chính là thước đo độ giàu có và tài năng săn mồi của con đực! |  | chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền tự hào đứng cạnh hàng rào gai treo đầy thức ăn béo ngậy để khoe tài năng. |
| b12 | 01:22.5–01:33.4 (10.9s) | L48 | Những chú chim mái sẽ bay đi kiểm tra từng cây gai, và con đực nào sở hữu một hàng rào gai treo đầy chuột đồng, thằn lằn và cào cào béo ngậy sẽ lập tức chiếm trọn trái tim của bạn tình để cùng xây tổ ấm! |  | Cô chim bách thanh mái bay qua chấm điểm hàng rào gai đầy ắp mồi và gật đầu hài lòng. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |

### scene05 · BẬC THẦY NHẠI GIỌNG HÓT DỤ DỖ CON MỒI VÀO BẪY PHỤC KÍCH · 75.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:02.5 (2.5s) | L49 | Và để khép lại bản cáo trạng điều tra, |  | Hiện trường phục kích: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền nấp sau tán lá rậm rạp, chiếc micro thu âm âm thanh rung động. |
| b02 | 00:02.5–00:11.8 (9.2s) | L50 | chúng ta không thể bỏ qua ngón đòn lừa đảo tâm lý đỉnh cao nhất của kẻ thủ ác: Nghệ thuật cải trang giọng hót dụ mồi! Là một thành viên xuất sắc của bộ Sẻ biết ca hót, |  | Bản vẽ phân tích tâm lý con mồi với các nốt nhạc ma thuật quyến rũ bay lơ lửng. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b03 | 00:11.8–00:16.8 (5.0s) | L51 | chim bách thanh sở hữu thanh quản cực kỳ linh hoạt có thể bắt chước tiếng kêu của hàng chục loài chim khác nhau! |  | Sơ đồ giải phẫu thanh quản syrinx linh hoạt của chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền phát ra những dải sóng âm đa dạng. |
| b04 | 00:16.8–00:20.6 (3.8s) | L52 | Khi đi săn, nó sẽ nấp kín trong tán lá rậm rạp và cất lên tiếng hót lảnh |  | chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền hòa mình hoàn hảo vào vòm lá xanh, chỉ để lộ đôi mắt quan sát sắc lạnh. |
| b05 | 00:20.6–00:24.3 (3.8s) | L53 | lót giả dạng tiếng chim sẻ non đang đòi ăn hoặc tiếng chim bạn tình đang gọi đàn. |  | Tiếng chim sẻ non nỉ non cầu cứu vang lên từ bụi cây, dụ dỗ những chú chim sẻ tò mò. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b06 | 00:24.3–00:30.6 (6.2s) | L54 | Những chú chim nhỏ ngây thơ nghe thấy tiếng đồng loại liền mất cảnh giác bay lại gần bụi cây để tìm kiếm bạn đồng hành. |  | Đàn chim sẻ nhỏ mất cảnh giác bay chầm chậm lại gần bụi cây tìm bạn đồng hành. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b07 | 00:30.6–00:37.8 (7.3s) | L55 | Thưa Thanh tra, nghĩa là nó dùng chính giọng hót thánh thót ngọt ngào để dẫn dụ nạn nhân vào tầm ngắm tử thần mà không cần tốn công đuổi bắt? |  | Cô trợ lý pháp y giật mình kinh ngạc chỉ vào sơ đồ âm thanh bẫy mồi xảo quyệt. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b08 | 00:37.8–00:43.0 (5.2s) | L56 | Chính xác 100%! Ngay khi con mồi bay vào cự ly phục kích chưa đầy hai mét, Sát Thủ Đồ Tể Lừng Danh |  | Vạch đo khoảng cách: Con mồi tiến vào vùng nguy hiểm tử thần dưới 2 mét. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b09 | 00:43.0–00:49.9 (6.9s) | L57 | sẽ lao ra như một mũi tên xé gió, tung cú cắn bẻ cổ thần tốc trước khi nạn nhân kịp nhận ra kẻ vừa cất tiếng hát ngọt ngào lại chính là thần chết! |  | chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền phóng ra như tia chớp, chiếc mỏ khóa chặt sau gáy con mồi trong chớp mắt. |
| b10 | 00:49.9–00:59.6 (9.7s) | L58 | Từ chiếc mặt nạ đen ngụy trang, giọng hót quyến rũ chết người, chiếc mỏ bẻ cổ siêu tốc cho đến giá treo gai nhọn đa năng, toàn bộ kế hoạch săn mồi tạo thành một chuỗi mắt xích hoàn mỹ không tì vết! |  | Bảng tổng hợp chiến thuật: Mặt nạ noir, mỏ móc bẻ cổ, cành gai cố định và âm thanh ngụy trang. |
| b11 | 00:59.6–01:10.6 (11.0s) | L59 | Cơ quan phát âm syrinx của chim bách thanh sở hữu các bó cơ độc lập có thể kiểm soát hai luồng âm thanh cùng lúc! Điều này cho phép nó tạo ra những âm điệu phức tạp, từ tiếng chích chòe líu lo cho đến tiếng chim sẻ non nỉ non cầu cứu, |  | Mô hình hai luồng khí độc lập trong cơ quan syrinx tạo hai âm điệu hòa âm cùng một lúc. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b12 | 01:10.6–01:15.7 (5.1s) | L60 | khiến ngay cả những kẻ quan sát dày dạn kinh nghiệm nhất cũng dễ dàng bị mắc lừa nếu chỉ lắng nghe bằng tai! |  | Các nhà điểu học đeo ống nhòm bị đánh lừa bởi tiếng hót ngọt ngào phát ra từ bụi gai. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |

### scene06 · TÔN VINH KIỆT TÁC SINH TỒN VÀ CÂN BẰNG SINH THÁI · 76.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:03.8 (3.8s) | L61 | Kính thưa toàn thể ban chuyên án và quý khán giả theo dõi hồ sơ vụ án, |  | Khép lại hồ sơ vụ án: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền đứng trên bục vinh danh với huy hiệu thám tử vàng sáng chói. |
| b02 | 00:03.8–00:16.1 (12.3s) | L62 | sau khi làm rõ toàn bộ bốn bằng chứng từ mỏ móc câu bẻ cổ, bàn kẹp gai nhọn trợ lực, kho phân hủy độc tố 48 giờ cho đến giọng hót phục kích thiên tài, chúng tôi xin tuyên bố khép lại tập tài liệu điều tra về Chim Bách Thanh! |  | Bốn biểu tượng vàng: Mỏ móc câu, cành gai trợ lực, kho lọc độc 48 giờ và tiếng hót thiên tài. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b03 | 00:16.1–00:27.4 (11.3s) | L63 | Dù thói quen xiên mồi lên cành gai có phần đáng sợ trong mắt con người, nhưng đối với hệ sinh thái đồng cỏ và bìa rừng, Sát Thủ Đồ Tể Lừng Danh chính là một mắt xích kiểm soát số lượng côn trùng gây hại và các loài gặm nhấm cực kỳ hữu ích, |  | Cánh đồng cỏ xanh mướt thanh bình được bảo vệ khỏi nạn chuột đồng và sâu bệnh phá hoại. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b04 | 00:27.4–00:33.3 (5.8s) | L64 | giữ cho cán cân tự nhiên luôn ở trạng thái cân bằng hoàn hảo. Bài học phá án hôm nay nhắc nhở chúng ta rằng: |  | Biểu tượng chiếc cân công lý sinh thái cân bằng giữa các loài sinh vật trong tự nhiên. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b05 | 00:33.3–00:44.2 (10.9s) | L65 | Đừng bao giờ đánh giá một sinh vật chỉ qua vẻ bề ngoài dễ thương hay giọng hót ngọt ngào! Sự sinh tồn trong thế giới hoang dã luôn đòi hỏi những chiến lược thích nghi thông minh và kiên cường vượt qua mọi giới hạn của cơ thể! |  | chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền nháy mắt tinh nghịch, thông điệp bài học cuộc sống hiện lên lấp lánh. |
| b06 | 00:44.2–00:52.0 (7.8s) | L66 | Trong cuộc sống cũng vậy, sự nhạy bén và năng lực tận dụng tối đa những nguồn lực sẵn có xung quanh sẽ là chìa khóa mở ra cánh cửa thành công cho mỗi chúng ta! |  | Bàn tay con người vươn tới thành công bằng trí tuệ và sự tận dụng nguồn lực xung quanh. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b07 | 00:52.0–01:00.5 (8.4s) | L67 | Giữa kỹ thuật bẻ cổ bằng mấu răng tomial tooth và chiếc bẫy gai nhọn giải độc, tuyệt chiêu nào của chú chim bách thanh khiến bạn rùng mình và thán phục nhất? |  | Hai màn hình đối chiếu: Cú cắn bẻ tủy sống siêu tốc và cành gai giải trừ độc tố kỳ diệu. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b08 | 01:00.5–01:05.2 (4.8s) | L68 | Hãy chia sẻ suy luận phá án của bạn ngay trong phần bình luận bên dưới nhé! Và đừng |  | Biểu tượng khung bình luận trò chuyện cùng cộng đồng thám tử suy luận sắc sảo. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b09 | 01:05.2–01:08.1 (2.8s) | L69 | quên nhấn nút Đăng Ký Kênh cùng chiếc chuông thông báo để không bỏ |  | Nút Đăng Ký Kênh màu đỏ rực cùng chiếc chuông thông báo rung chuyển sống động. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này. |
| b10 | 01:08.1–01:16.2 (8.1s) | L70 | lỡ Tập 40: Khám phá siêu kiến trúc quân sự của Kiến Cắt Lá! Xin chào tạm biệt và hẹn gặp lại toàn thể các thám tử trong những vụ án tự nhiên kỳ thú tiếp theo! |  | Trailer hé lộ Tập 40: Đội quân Kiến Cắt Lá hùng hậu hành quân mang lá xanh trong rừng rậm nhiệt đới. |

## 5. Phân cảnh Shorts — từng beat

Banner: **SÁT THỦ NGÂY THƠ / BÍ ẨN CÀNH GAI XUYÊN THÂM?!** · giọng 42.0s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Bạn có tin một chú chim nhỏ nặng chỉ 50g với vẻ ngoài ngây thơ lại mang danh |  |
| s02 | 00:05.7 | S02 | hiệu Sát Thủ Đồ Tể khét tiếng nhất thế giới tự nhiên không? Đó chính là Chim Bách Thanh! |  |
| s03 | 00:11.2 | S03 | Bí mật rợn người nằm ở chiếc mỏ móc câu |  |
| s04 | 00:13.7 | S04 | có hai mấu răng xương sắc bén có |  |
| s05 | 00:15.7 | S05 | thể bẻ gãy đốt sống cổ con mồi chỉ trong chớp mắt! |  |
| s06 | 00:18.9 | S06 | Vì đôi chân chim sẻ quá yếu không thể giữ chặt mồi, |  |
| s07 | 00:21.9 | S07 | nó đã sáng tạo ra một tuyệt chiêu độc nhất vô |  |
| s08 | 00:24.0 | S08 | nhị: Xiên thủng xác con mồi lên những chiếc gai cây nhọn hoắt hoặc hàng rào dây thép gai |  |
| s09 | 00:28.8 | S09 | để làm điểm tựa xé thịt! |  |
| s10 | 00:30.4 | S10 | Thậm chí những con cào cào cực độc cũng bị |  |
| s11 | 00:32.9 | S11 | nó treo gai phơi nắng suốt 48 giờ cho bay hết chất độc rồi mới ăn! |  |
| s12 | 00:37.4 | S12 | Một kho lương thực rùng rợn biến nó thành thám tử sát thủ thiên tài của bụi rậm! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chào mừng các thám tử tư, các chuyên gia giám định pháp y và những bộ óc đam mê suy luận phá án bước vào hồ sơ hình sự kỳ lạ bậc nhất của thế giới tự nhiên! Hôm nay,". Bố cục: Phòng điều tra trọng án sinh thái: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền trong vai thám tử trưởng chỉ gậy vào bảng chứng cứ gắn đầy ảnh và chỉ đỏ.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "phòng điều tra trọng án sinh thái của chúng tôi xin mời quý vị lật mở một tập tài liệu tuyệt mật,". Bố cục: Cận cảnh tập hồ sơ tuyệt mật màu nâu đề chữ Tuyệt Mật và dấu vân tay hiện trường vụ án bí ẩn. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "giải mã hiện trường của một bóng ma tội phạm có vẻ ngoài ngây thơ tựa thiên thần nhưng lại mang phong cách hành động của một đồ tể tàn nhẫn!". Bố cục: Bóng đen bí ẩn mang mặt nạ hiệp sĩ Zorro lướt qua màn sương đêm bìa rừng u ám. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một vụ án hóc búa thách thức mọi định kiến thông thường của chúng ta về giới loài chim ca hót!". Bố cục: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền ngồi chống cằm suy tư bên bàn làm việc đầy hồ sơ và kính lúp quang học kiểu trinh thám cổ điển.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy nhìn vào cành cây mận gai cằn cỗi ven bìa rừng:". Bố cục: Hiện trường bìa rừng: Bụi cây mận gai cằn cỗi với những nhánh gai nhọn dài lởm chởm trong sương mù. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một hiện trường rùng rợn và quái đản đang phơi bày trước mắt chúng ta! Trên những chiếc gai nhọn hoắt dài 5cm,". Bố cục: Vòng tròn phấn trắng và thước dây pháp y vàng neon bao quanh cành cây có những chiếc gai nhọn 5cm sắc lẹm. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hàng loạt con mồi từ thằn lằn, chuột đồng, ếch nhái cho đến những chú chim sẻ nhỏ bé đều bị". Bố cục: Xác thằn lằn, chuột đồng và chim sẻ nhỏ bị xiên treo lơ lửng trên các cành gai nhọn ven đường. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "xiên thủng qua cổ hoặc ức, treo lơ lửng giữa không trung như những xâu thịt nướng trong lò mổ!". Bố cục: Cận cảnh giám định pháp y: Đầu gai nhọn cắm xuyên qua gáy con mồi chuẩn xác đến từng mi-li-mét. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thưa Thanh tra trưởng, dấu vết khám nghiệm xác nhận tất cả các nạn nhân đều bị gãy đốt sống cổ chỉ bằng một nhát cắn cực kỳ hiểm hóc, không hề có dấu vết giằng co hay móng vuốt đại bàng cào xé! Một quan sát hiện trường vô cùng sắc bén thưa trợ lý pháp y!". Bố cục: Cô trợ lý pháp y đeo kính trắng cầm bảng kẹp hồ sơ báo cáo kết quả khám nghiệm hiện trường. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thủ phạm của vụ án liên hoàn này không phải là một con mãnh thú khổng lồ hay một con chim ưng dũng mãnh, mà lại là một chú chim sẻ nhỏ nhắn chỉ nặng vỏn vẹn 50g, mang bộ lông xám trắng thanh lịch và một dải lông đen tuyền vắt ngang mắt trông hệt như". Bố cục: Sơ đồ giải phẫu hiển vi cho thấy đốt sống cổ bị bẻ gãy gập bằng một lực cắt chớp nhoáng không tì vết. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chiếc mặt nạ của hiệp sĩ Zorro! Sinh vật này mang tên khoa học thuộc họ Laniidae, nhưng giới điều tra tự nhiên gọi nó bằng danh xưng rợn gáy: Sát Thủ Đồ Tể Lừng Danh! Tại sao một loài chim ca hót nhỏ bé lại sở hữu thói quen". Bố cục: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền xuất hiện trong vùng sáng đèn rọi, ánh mắt sắc bén lấp lánh sau dải lông đen ngang mắt.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "treo xác con mồi lên gai nhọn rùng rợn đến như vậy? Phải chăng đây là một hành vi tàn bạo bản năng, hay đằng sau đó là một chiến lược cơ học và hóa học sinh tồn thiên tài? Ngay sau đây, xin mời các bạn cùng tôi mở cánh cửa phòng giải phẫu để vạch trần vũ khí bí mật đầu tiên!". Bố cục: Bảng chân dung truy nã pháp y: Chú chim bách thanh họ Laniidae với danh xưng Sát Thủ Đồ Tể Lừng Danh.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Xin mời các giám định viên cơ học hãy đặt chiếc mỏ của nghi phạm dưới kính hiển vi điện tử:". Bố cục: Phòng giải phẫu cơ học: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền đứng bên cạnh mô hình kính hiển vi điện tử chiếu rọi cấu trúc đầu chim.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây chính là vũ khí đoạt mạng then chốt! Mặc dù thuộc bộ Sẻ vốn chỉ quen ăn hạt và sâu bọ nhỏ, mỏ của Sát Thủ Đồ Tể Lừng Danh lại". Bố cục: Mô hình 3D chiếc mỏ sát thủ phóng to với các tia laser đo đạc lực cắn và góc uốn cong nguy hiểm. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tiến hóa theo hướng của các loài chim săn mồi đỉnh cao như chim ưng hay chim cắt!". Bố cục: Bản vẽ so sánh: Chiếc mỏ bách thanh mang cấu trúc thu nhỏ của chim ưng và chim cắt dũng mãnh. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đầu mỏ trên uốn cong quặp xuống sắc lẹm như một chiếc móc câu sắt. Nhưng chi tiết kinh hoàng nhất nằm ở hai bên rìa mỏ trên:". Bố cục: Cận cảnh đầu mỏ trên uốn quặp xuống như móc câu sắt bằng thép tôi luyện đen nhánh. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hai mấu răng xương nhọn hoắt mọc chìa ra ngoài, giới giải phẫu học gọi là cấu trúc mấu răng tomial tooth!". Bố cục: Phóng to hai mấu răng xương tomial tooth sắc nhọn ở hai bên rìa mỏ trên với mũi tên chỉ thị vàng neon. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi lao xuống tấn công con mồi từ trên cành cây cao, nó". Bố cục: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền lao bổ nhào từ cành cây cao xuống như một mũi tên xé gió với đôi cánh khép gọn.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "không cắn bừa bãi vào thân xác mà nhắm thẳng chuẩn xác vào gáy hoặc sau hộp sọ nạn nhân.". Bố cục: Tâm ngắm chữ thập màu đỏ khóa chặt vào gáy và sau hộp sọ của con chuột đồng đang gặm cỏ. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hai chiếc mấu răng tomial tooth sẽ cắm phập vào khoảng hở giữa các đốt sống cổ, sau đó hàm dưới khép chặt lại tạo lực đòn bẩy". Bố cục: Khoảnh khắc mấu răng tomial tooth cắm phập vào khe hở giữa hai đốt sống cổ tạo lực đòn bẩy cực đại. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bẻ gãy tủy sống con mồi chỉ trong một phần mười giây! Con mồi lập tức bị liệt toàn thân và chết lâm sàng trước cả khi kịp nhận ra điều gì vừa xảy ra.". Bố cục: Đồng hồ bấm giờ điện tử ghi nhận 0.1 giây: Đốt sống cổ đứt lìa hoàn toàn, con mồi mất tri giác. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một cú cắn kết liễu hoàn hảo, không lãng phí một mi-li-giun năng lượng nào, biến chú chim sẻ nhỏ bé thành một cỗ máy hành quyết chuẩn xác không thua kém gì đại bàng dũng mãnh! Thế nhưng, sau khi hạ gục con mồi nặng gần bằng chính cơ thể mình, một". Bố cục: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền đứng trên con mồi đã bất động hoàn toàn, thể hiện độ chính xác tuyệt đối không tốn sức.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "vấn đề nan giải mới lại xuất hiện đối với sát thủ nhỏ con này. Đó là gì? Xin mời quý vị cùng tôi bước sang hiện trường tiếp theo! Lực cắn đo được từ cơ hàm của chim bách thanh mạnh gấp 3 lần so với bất kỳ loài chim nào có cùng kích cỡ cơ thể!". Bố cục: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền đứng gãi đầu nhìn con mồi nặng bằng chính mình, đối mặt với bài toán cơ học nan giải.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thậm chí khi săn bắt những con chuột đồng nặng gấp đôi cơ thể nó, cú bẻ cổ bằng mấu răng tomial tooth vẫn diễn ra chớp nhoáng đến mức con mồi không hề có cơ hội phản kháng dù chỉ là một cú cào xước!". Bố cục: Biểu đồ cột so sánh: Lực cắn cơ hàm chim bách thanh cao gấp 3 lần chim cùng kích cỡ. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây chính là nút thắt logic thú vị nhất trong toàn bộ hồ sơ vụ án:". Bố cục: Khu vực trưng bày vũ khí số 2: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền đứng cạnh cành cây gai bồ kết khổng lồ với nụ cười bí ẩn.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tại sao chim bách thanh phải xiên con mồi lên cành gai?". Bố cục: Dấu chấm hỏi lớn màu đỏ trên nền cành gai nhọn hoắt cắm xác con mồi giữa sương mù. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các loài chim săn mồi thực thụ như đại bàng hay cú mèo sở hữu đôi bàn chân có cơ bắp khổng lồ cùng bộ móng vuốt sắc nhọn hình lưỡi liềm để ghim chặt con mồi xuống đất trong khi mỏ xé thịt.". Bố cục: Bàn chân đại bàng lực lưỡng với những móng vuốt cong vút ghim chặt con mồi xuống tảng đá. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thế nhưng nghi phạm của chúng ta, dù sở hữu chiếc mỏ đại bàng, bàn chân của nó lại chỉ là bàn chân chim sẻ thông thường:". Bố cục: Cận cảnh bàn chân chim sẻ mảnh khảnh của chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền với các ngón nhỏ chỉ đủ để đậu cành cây.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các ngón chân mảnh khảnh chỉ đủ lực để đậu bám trên cành cây chứ tuyệt đối không thể giữ chặt một con chuột đồng hay một chú thằn lằn to lớn đang giãy giụa!". Bố cục: Hình ảnh con thằn lằn trơn trượt tuột khỏi đôi bàn chân nhỏ bé không có móng quắp. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để giải quyết nghịch lý cơ học này, Sát Thủ Đồ Tể Lừng Danh đã phát minh ra một giải pháp phỏng sinh học đỉnh cao: Sử dụng công cụ môi trường làm bàn kẹp trợ lực!". Bố cục: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền nảy ra ý tưởng phát minh thông minh, bóng đèn sáng rực trên đầu trong phòng thí nghiệm rừng.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó tha xác con mồi đến những bụi cây có gai nhọn dài như gai bồ kết, gai mận rừng, hoặc thậm chí là các hàng rào dây thép gai do con người dựng lên!". Bố cục: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền ngậm xác con mồi bay đến hàng rào dây thép gai và bụi mận gai nhọn hoắt.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó dùng toàn lực cắm phập xác nạn nhân vào chiếc gai nhọn, biến chiếc gai thành một chiếc kẹp cố định vĩnh cửu. Khi con mồi đã bị khóa cứng tại chỗ, chú chim có thể". Bố cục: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền dùng toàn lực ấn mạnh xác con mồi ghim chặt vào chiếc đinh gai nhọn như chiếc kẹp bàn thợ cơ khí.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thong thả dùng chiếc mỏ móc câu của mình để xé nhỏ từng thớ thịt một cách nhàn nhã mà không cần tốn chút sức lực nào để ghì giữ!". Bố cục: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền nhàn nhã dùng mỏ móc xé từng miếng thịt nhỏ khi con mồi đã bị cố định vững chắc trên gai.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một bằng chứng hùng hồn cho thấy trí thông minh sử dụng ngoại vật phi thường của loài chim! Nhưng hiện trường cành gai không chỉ đơn thuần là bàn ăn dã chiến, nó còn là một kho dự trữ hóa học cực kỳ tinh vi!". Bố cục: Bản vẽ phỏng sinh học: Chiếc gai nhọn biến thành cánh tay đòn cơ học ngoại vi thiên tài. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đáng kinh ngạc hơn nữa, mỗi chú chim bách thanh sở hữu một bản đồ trí nhớ không gian hoàn hảo về hàng trăm chiếc gai nhọn trong phạm vi lãnh thổ rộng hàng chục héc-ta của nó! Nó ghi nhớ chính xác vị trí nào có cành gai phù hợp với kích thước từng con mồi:". Bố cục: Bản đồ vệ tinh lãnh thổ rừng với hàng trăm điểm đánh dấu cành gai được lưu trữ trong trí nhớ của chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gai mảnh cho thằn lằn và cào cào, gai chạc ba dày dặn cho chuột đồng và chim sẻ, tạo thành một hệ thống kho tàng thực phẩm dã ngoại quy củ và bài bản!". Bố cục: Sơ đồ kho bãi tự nhiên: Phân loại gai mảnh cho cào cào và gai chạc ba cho chuột đồng béo ngậy. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Xin mời các nhà hóa nghiệm pháp y cùng phân tích mẫu vật kỳ lạ nhất tìm thấy trên giá treo gai: Đó là những chú cào cào lubber khổng lồ màu vàng đen rực rỡ! Trong tự nhiên,". Bố cục: Phòng hóa nghiệm sinh hóa: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền đeo kính bảo hộ bên cạnh các ống nghiệm chứa chất độc màu tím và xanh lục.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "loài cào cào này tích tụ hàm lượng chất độc cardenolide cực mạnh trong cơ thể, có thể làm tê liệt tim và gây nôn mửa dữ dội cho bất kỳ loài chim nào dại dột nuốt phải.". Bố cục: Cận cảnh chú cào cào lubber khổng lồ thân màu vàng sọc đen bóng bẩy nằm dưới kính lúp. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi cành gai nhọn hoắt trong lãnh địa của nó không chỉ đơn thuần là bàn ăn dã chiến, mà còn là một kho tàng bí mật ẩn chứa những bất ngờ hóa học vượt ngoài sức tưởng tượng của các nhà khoa học đương đại!". Bố cục: Công thức hóa học cardenolide phát sáng cảnh báo nguy hiểm độc tố làm ngừng tim. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mọi loài chim săn mồi khác đều phải tránh xa món ăn chết chóc này. Thế nhưng Sát Thủ Đồ Tể Lừng Danh lại thản nhiên bắt sống những con cào cào độc và". Bố cục: Các chú chim rừng khác sợ hãi bay dạt ra xa khi thấy chú cào cào độc lubber. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "xiên chúng lên cành gai nhọn hoắt phơi nắng! Tại sao nó không ăn ngay mà lại treo ở đó?". Bố cục: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền thản nhiên ghim chú cào cào độc lên cành gai cao nhất phơi dưới ánh nắng mặt trời rực rỡ.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bí mật nằm ở chỗ: Độc tố cardenolide trong cơ thể cào cào sẽ bị phân hủy sinh học và bay hơi hoàn toàn dưới tác động của ánh nắng mặt trời và gió". Bố cục: Tia nắng mặt trời và những luồng gió tự nhiên phá vỡ chuỗi phân tử độc tố cardenolide. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "sau khoảng 48 giờ đến 72 giờ phơi khô!". Bố cục: Đồng hồ cát điện tử đếm ngược từ 48 giờ đến 72 giờ: Độc tố giảm dần về 0%. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chú chim bách thanh kiên nhẫn chờ đợi đúng hai ngày đêm cho đến khi các phản ứng hóa học tự nhiên biến con mồi độc hại thành một miếng mồi khô thơm ngon và hoàn toàn vô hại rồi mới quay lại thưởng thức!". Bố cục: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền đeo khăn ăn cầm dao nĩa phong cách ẩm thực, thưởng thức món cào cào khô đã sạch độc tố.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây chẳng khác nào quy trình ủ thực phẩm lên men hoặc phơi khô thịt bò của các đầu bếp ẩm thực hàng đầu!". Bố cục: Bếp trưởng ẩm thực rừng xanh: Quy trình ủ men và phơi thịt bò khô của tự nhiên hoang dã. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vừa là kho lương thực chống đói trong mùa đông khan hiếm, vừa là nhà máy xử lý chất độc tự nhiên. Khả năng tính toán thời gian và hóa sinh của loài chim này thực sự khiến con người phải ngả mũ thán phục!". Bố cục: Cành gai phủ đầy tuyết trắng mùa đông treo các gói mồi khô thơm ngon làm lương thực dự trữ. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong mùa sinh sản vào mùa xuân, số lượng con mồi được xiên trên các cành gai nhọn xung quanh tổ chính là thước đo độ giàu có và tài năng săn mồi của con đực!". Bố cục: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền tự hào đứng cạnh hàng rào gai treo đầy thức ăn béo ngậy để khoe tài năng.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Những chú chim mái sẽ bay đi kiểm tra từng cây gai, và con đực nào sở hữu một hàng rào gai treo đầy chuột đồng, thằn lằn và cào cào béo ngậy sẽ lập tức chiếm trọn trái tim của bạn tình để cùng xây tổ ấm!". Bố cục: Cô chim bách thanh mái bay qua chấm điểm hàng rào gai đầy ắp mồi và gật đầu hài lòng. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và để khép lại bản cáo trạng điều tra,". Bố cục: Hiện trường phục kích: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền nấp sau tán lá rậm rạp, chiếc micro thu âm âm thanh rung động.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chúng ta không thể bỏ qua ngón đòn lừa đảo tâm lý đỉnh cao nhất của kẻ thủ ác: Nghệ thuật cải trang giọng hót dụ mồi! Là một thành viên xuất sắc của bộ Sẻ biết ca hót,". Bố cục: Bản vẽ phân tích tâm lý con mồi với các nốt nhạc ma thuật quyến rũ bay lơ lửng. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chim bách thanh sở hữu thanh quản cực kỳ linh hoạt có thể bắt chước tiếng kêu của hàng chục loài chim khác nhau!". Bố cục: Sơ đồ giải phẫu thanh quản syrinx linh hoạt của chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền phát ra những dải sóng âm đa dạng.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi đi săn, nó sẽ nấp kín trong tán lá rậm rạp và cất lên tiếng hót lảnh lót". Bố cục: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền hòa mình hoàn hảo vào vòm lá xanh, chỉ để lộ đôi mắt quan sát sắc lạnh.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "giả dạng tiếng chim sẻ non đang đòi ăn hoặc tiếng chim bạn tình đang gọi đàn.". Bố cục: Tiếng chim sẻ non nỉ non cầu cứu vang lên từ bụi cây, dụ dỗ những chú chim sẻ tò mò. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Những chú chim nhỏ ngây thơ nghe thấy tiếng đồng loại liền mất cảnh giác bay lại gần bụi cây để tìm kiếm bạn đồng hành.". Bố cục: Đàn chim sẻ nhỏ mất cảnh giác bay chầm chậm lại gần bụi cây tìm bạn đồng hành. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thưa Thanh tra, nghĩa là nó dùng chính giọng hót thánh thót ngọt ngào để dẫn dụ nạn nhân vào tầm ngắm tử thần mà không cần tốn công đuổi bắt?". Bố cục: Cô trợ lý pháp y giật mình kinh ngạc chỉ vào sơ đồ âm thanh bẫy mồi xảo quyệt. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chính xác 100%! Ngay khi con mồi bay vào cự ly phục kích chưa đầy hai mét, Sát Thủ Đồ Tể Lừng Danh sẽ". Bố cục: Vạch đo khoảng cách: Con mồi tiến vào vùng nguy hiểm tử thần dưới 2 mét. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "lao ra như một mũi tên xé gió, tung cú cắn bẻ cổ thần tốc trước khi nạn nhân kịp nhận ra kẻ vừa cất tiếng hát ngọt ngào lại chính là thần chết!". Bố cục: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền phóng ra như tia chớp, chiếc mỏ khóa chặt sau gáy con mồi trong chớp mắt.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Từ chiếc mặt nạ đen ngụy trang, giọng hót quyến rũ chết người, chiếc mỏ bẻ cổ siêu tốc cho đến giá treo gai nhọn đa năng, toàn bộ kế hoạch săn mồi tạo thành một chuỗi mắt xích hoàn mỹ không tì vết!". Bố cục: Bảng tổng hợp chiến thuật: Mặt nạ noir, mỏ móc bẻ cổ, cành gai cố định và âm thanh ngụy trang.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cơ quan phát âm syrinx của chim bách thanh sở hữu các bó cơ độc lập có thể kiểm soát hai luồng âm thanh cùng lúc! Điều này cho phép nó tạo ra những âm điệu phức tạp, từ tiếng chích chòe líu lo cho đến tiếng chim sẻ non nỉ non cầu cứu,". Bố cục: Mô hình hai luồng khí độc lập trong cơ quan syrinx tạo hai âm điệu hòa âm cùng một lúc. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "khiến ngay cả những kẻ quan sát dày dạn kinh nghiệm nhất cũng dễ dàng bị mắc lừa nếu chỉ lắng nghe bằng tai!". Bố cục: Các nhà điểu học đeo ống nhòm bị đánh lừa bởi tiếng hót ngọt ngào phát ra từ bụi gai. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kính thưa toàn thể ban chuyên án và quý khán giả theo dõi hồ sơ vụ án,". Bố cục: Khép lại hồ sơ vụ án: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền đứng trên bục vinh danh với huy hiệu thám tử vàng sáng chói.
```
</details>

<details><summary>L62</summary>

```text
HÌNH L62 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "sau khi làm rõ toàn bộ bốn bằng chứng từ mỏ móc câu bẻ cổ, bàn kẹp gai nhọn trợ lực, kho phân hủy độc tố 48 giờ cho đến giọng hót phục kích thiên tài, chúng tôi xin tuyên bố khép lại tập tài liệu điều tra về Chim Bách Thanh!". Bố cục: Bốn biểu tượng vàng: Mỏ móc câu, cành gai trợ lực, kho lọc độc 48 giờ và tiếng hót thiên tài. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L63</summary>

```text
HÌNH L63 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dù thói quen xiên mồi lên cành gai có phần đáng sợ trong mắt con người, nhưng đối với hệ sinh thái đồng cỏ và bìa rừng, Sát Thủ Đồ Tể Lừng Danh chính là một mắt xích kiểm soát số lượng côn trùng gây hại và các loài gặm nhấm cực kỳ hữu ích,". Bố cục: Cánh đồng cỏ xanh mướt thanh bình được bảo vệ khỏi nạn chuột đồng và sâu bệnh phá hoại. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L64</summary>

```text
HÌNH L64 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "giữ cho cán cân tự nhiên luôn ở trạng thái cân bằng hoàn hảo. Bài học phá án hôm nay nhắc nhở chúng ta rằng:". Bố cục: Biểu tượng chiếc cân công lý sinh thái cân bằng giữa các loài sinh vật trong tự nhiên. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L65</summary>

```text
HÌNH L65 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đừng bao giờ đánh giá một sinh vật chỉ qua vẻ bề ngoài dễ thương hay giọng hót ngọt ngào! Sự sinh tồn trong thế giới hoang dã luôn đòi hỏi những chiến lược thích nghi thông minh và kiên cường vượt qua mọi giới hạn của cơ thể!". Bố cục: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền nháy mắt tinh nghịch, thông điệp bài học cuộc sống hiện lên lấp lánh.
```
</details>

<details><summary>L66</summary>

```text
HÌNH L66 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong cuộc sống cũng vậy, sự nhạy bén và năng lực tận dụng tối đa những nguồn lực sẵn có xung quanh sẽ là chìa khóa mở ra cánh cửa thành công cho mỗi chúng ta!". Bố cục: Bàn tay con người vươn tới thành công bằng trí tuệ và sự tận dụng nguồn lực xung quanh. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L67</summary>

```text
HÌNH L67 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giữa kỹ thuật bẻ cổ bằng mấu răng tomial tooth và chiếc bẫy gai nhọn giải độc, tuyệt chiêu nào của chú chim bách thanh khiến bạn rùng mình và thán phục nhất?". Bố cục: Hai màn hình đối chiếu: Cú cắn bẻ tủy sống siêu tốc và cành gai giải trừ độc tố kỳ diệu. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L68</summary>

```text
HÌNH L68 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy chia sẻ suy luận phá án của bạn ngay trong phần bình luận bên dưới nhé! Và đừng quên". Bố cục: Biểu tượng khung bình luận trò chuyện cùng cộng đồng thám tử suy luận sắc sảo. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L69</summary>

```text
HÌNH L69 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nhấn nút Đăng Ký Kênh cùng chiếc chuông thông báo để không bỏ lỡ". Bố cục: Nút Đăng Ký Kênh màu đỏ rực cùng chiếc chuông thông báo rung chuyển sống động. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>L70</summary>

```text
HÌNH L70 (16:9 ngang, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tập 40: Khám phá siêu kiến trúc thế giới tự nhiên của Kiến Cắt Lá! Xin chào tạm biệt và hẹn gặp lại toàn thể các thám tử trong những vụ án tự nhiên kỳ thú tiếp theo!". Bố cục: Trailer hé lộ Tập 40: Đội quân Kiến Cắt Lá hùng hậu hành quân mang lá xanh trong rừng rậm nhiệt đới.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bạn có tin một chú chim nhỏ nặng chỉ 50g với vẻ ngoài ngây thơ lại mang danh hiệu". Bố cục: Khung cảnh mở đầu trinh thám noir: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền đứng trên cành cây với ánh mắt sắc lẹm, bên cạnh là biểu tượng hồ sơ mật vụ án màu vàng neon.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Sát Thủ Đồ Tể khét tiếng nhất thế giới tự nhiên không? Đó chính là Chim Bách Thanh!". Bố cục: Cận cảnh chân dung chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền với dải lông đen vắt ngang mắt như mặt nạ hiệp sĩ Zorro huyền bí, bộ lông xám bạc sang trọng.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bí mật rợn người nằm ở chiếc mỏ móc câu có". Bố cục: Bản vẽ phân tích pháp y: Chiếc mỏ chim quặp xuống như móc câu sắt với hai chiếc mấu răng xương nhọn hoắt được khoanh tròn bằng mực đỏ. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "hai mấu răng xương sắc bén có thể". Bố cục: Hình ảnh kính lúp quang học phóng đại cấu trúc mấu răng tomial tooth sắc lẹm của chim bách thanh. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "bẻ gãy đốt sống cổ con mồi chỉ trong chớp mắt!". Bố cục: Sơ đồ động lực học: Mỏ cắm phập vào khoảng hở giữa hai đốt sống cổ con mồi và bẻ gãy tủy sống trong chớp mắt. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Vì đôi chân chim sẻ quá yếu không thể giữ chặt mồi, nó đã". Bố cục: So sánh pháp y đối lập: Đôi bàn chân chim sẻ mảnh khảnh của chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên cạnh bàn chân móng vuốt đại bàng khổng lồ.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "sáng tạo ra một tuyệt chiêu độc nhất vô nhị:". Bố cục: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền nở nụ cười thám tử đắc thắng, chỉ mỏ về phía cành cây gai nhọn hoắt ven bìa rừng.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Xiên thủng xác con mồi lên những chiếc gai cây nhọn hoắt hoặc hàng rào dây thép gai để". Bố cục: Hiện trường cành cây gai nhọn hoắt cắm xuyên qua xác con mồi làm điểm tựa cơ học giữa không trung. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "làm điểm tựa xé thịt!". Bố cục: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền thong thả dùng mỏ móc câu xé từng thớ thịt từ con mồi đã bị cố định cứng trên cành gai.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Thậm chí những con cào cào cực độc cũng bị nó". Bố cục: Mẫu vật pháp y: Chú cào cào lubber khổng lồ sọc vàng đen chứa chất độc cardenolide nguy hiểm. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>S11</summary>

```text
HÌNH S11 (DỌC 9:16, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "treo gai phơi nắng suốt 48 giờ cho bay hết chất độc rồi mới ăn!". Bố cục: Dãy cào cào bị xiên phơi nắng dưới ánh mặt trời rực rỡ, đồng hồ đếm ngược 48 giờ giải phóng độc tố. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.
```
</details>

<details><summary>S12</summary>

```text
HÌNH S12 (DỌC 9:16, phong cách phác thảo khám nghiệm hiện trường pháp y & truyện tranh trinh thám Noir (Forensic Crime Scene Sketch) và nhân vật chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Một kho lương thực rùng rợn biến nó thành thám tử sát thủ thiên tài của bụi rậm!". Bố cục: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền đứng kiêu hãnh trên cành cây cao giữa ánh hoàng hôn, biểu tượng thám tử Sherlock Holmes của rừng sâu.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/70 của video YouTube về Chim Bách Thanh). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách bản vẽ phác thảo khám nghiệm hiện trường pháp y kết hợp truyện tranh điện ảnh trinh thám Noir (Forensic Crime Scene Sketch & Noir Pen-and-Ink): nét vẽ bút kim kỹ thuật đen trắng sắc sảo lạnh lùng, chi tiết thước đo tỉ lệ hiện trường màu vàng dạ quang neon, bảng manh mối ghim chỉ đỏ kết nối chứng cứ, vòng phấn đánh dấu hiện trường, kính lúp quang học soi vết cành gai nhọn, độ tương phản thị giác cực cao giàu tính điều tra phá án; NỀN TRẮNG TINH hoàn toàn, không watermark, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/12 của video YouTube Shorts về Chim Bách Thanh). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách bản vẽ phác thảo khám nghiệm hiện trường pháp y kết hợp truyện tranh điện ảnh trinh thám Noir (Forensic Crime Scene Sketch & Noir Pen-and-Ink): nét vẽ bút kim kỹ thuật đen trắng sắc sảo lạnh lùng, chi tiết thước đo tỉ lệ hiện trường màu vàng dạ quang neon, bảng manh mối ghim chỉ đỏ kết nối chứng cứ, vòng phấn đánh dấu hiện trường, kính lúp quang học soi vết cành gai nhọn, độ tương phản thị giác cực cao giàu tính điều tra phá án; NỀN TRẮNG TINH hoàn toàn, không watermark, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền. 
```
</details>

## 7. SEO

- **title:** Hồ Sơ Sát Thủ Bụi Rậm: Chim Bách Thanh Xiên Cọc Con Mồi Tẩm Độc Để Dự Trữ Lương Thực?! | Tập 39
- **hook_paragraph:** Chim Bách Thanh (Laniidae) được mệnh danh là Đồ tể Shrike của thế giới loài chim. Không có móng vuốt đại bàng sắc nhọn, loài chim nhỏ bé này dùng mỏ bẻ gãy đốt sống cổ con mồi rồi xiên cọc lên hàng rào gai nhọn để làm kho lương thực và phân giải chất độc. Cùng Chuyên gia hình sự giải mã hồ sơ vụ án chấn động thế giới tự nhiên!
- **question:** Giữa mấu răng mỏ Tomial bẻ gãy đốt sống và chiến thuật xiên cọc chờ phân giải độc tố, phương thức săn mồi nào của Chim Bách Thanh làm bạn ấn tượng nhất?
- **next_teaser:** đế chế kiến thợ tí hon canh tác nông nghiệp nấm ngầm 50 triệu năm
- **shorts_title:** Bí mật loài chim xiên cọc con mồi như ma cà rồng?!
- **shorts_desc:** Chim Bách Thanh xiên con mồi lên gai nhọn để treo kho lương thực và chờ độc tố phân hủy!
- **bullets:** Chiếc mỏ có mấu răng Tomial: Cú mổ bẻ gãy tủy sống con mồi trong chớp mắt 0,1 giây · Chiến thuật xiên cọc gai nhọn: Dùng gai xương rồng và dây thép gai thay cho đôi chân giữ mồi · Kho thịt dự trữ giải độc: Chờ chất độc cào cào Lubber phân hủy tự nhiên trong 3 ngày rồi mới ăn · Kỹ thuật ngụy trang âm thanh: Bắt chước tiếng hót chim non để dụ con mồi vào bẫy phục kích · Lãnh địa ma quái: Những hàng rào gai treo đầy xác thằn lằn, chuột và côn trùng rùng rợn · Ứng dụng sinh thái học: Bậc thầy kiểm soát sâu bệnh tự nhiên bảo vệ đồng ruộng không cần hóa chất
- **tags:** chim bách thanh, laniidae, chim đồ tể, hồ sơ sinh vật, vẽ chuyện hoang dã, whiteboard animation

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-39-chim-bach-thanh
python src/episode/pipeline.py tts    projects/tap-39-chim-bach-thanh     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-39-chim-bach-thanh     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-39-chim-bach-thanh     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-39-chim-bach-thanh              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-39-chim-bach-thanh --force
python scripts/beat_sheet.py projects/tap-39-chim-bach-thanh               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-39-chim-bach-thanh/audio/shorts.wav projects/tap-39-chim-bach-thanh/renders/tap-39-chim-bach-thanh_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-39-chim-bach-thanh
python src/episode/pipeline.py seo    projects/tap-39-chim-bach-thanh
python src/episode/episode_doc.py     projects/tap-39-chim-bach-thanh
```

# TẬP 19 — THẰN LẰN QUỶ GAI · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-19-than-lan-quy-gai`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-19-than-lan-quy-gai`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F4` · **Persona giọng:** `phong_vien_24h` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Thằn Lằn Quỷ Gai |
| Tiêu đề YouTube | Tại Sao Thằn Lằn Quỷ Gai Uống Nước Bằng... Bàn Chân?! \| Thằn Lằn Quỷ Gai \| Tập 19 |
| Video dài | `renders/tap-19-than-lan-quy-gai_long.mp4` — 9:51.9 (591.9s) |
| Shorts | `renders/tap-19-than-lan-quy-gai_shorts.mp4` — 0:50.5 (50.5s) |
| Thumbnail | `renders/tap-19-than-lan-quy-gai_thumbnail.jpg` |
| Số hình | dài 62 beat / 62 ảnh riêng; Shorts 11 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/62 của video YouTube về Thằn Lằn Quỷ Gai). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — 00 SÁNG: TUYỆT KỸ UỐNG SƯƠNG MAO DẪN BẰNG BÀN CHÂN
*Thẻ chương:* KỲ QUAN MAO DẪN NƯỚC NGƯỢC LÊN MIỆNG

*Badge:* `05:00 SÁNG` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene01_p0.wav` (348 ký tự) · mood `hao_hung`

```text
Bíp bíp bíp! Đồng hồ điểm không năm giờ sáng! Phóng viên truyền hình sinh tồn hai mươi tư giờ xin kính chào toàn thể quý vị khán giả! Ngay lúc này, tôi đang có mặt trực tiếp tại chảo lửa sa mạc đỏ rực miền Trung nước Úc, nơi nhiệt độ có thể chênh lệch kinh hoàng từ lạnh thấu xương lúc rạng đông lên tới bốn mươi lăm độ C khi mặt trời lên đỉnh đầu!
```
**Part 1** → `audio/vs/scene01_p1.wav` (391 ký tự) · mood `hao_hung`

```text
Trước mắt chúng ta là một sinh vật có diện mạo kỳ quái và gai góc bậc nhất thế giới tự nhiên! Thân hình chỉ dài vỏn vẹn hai mươi xăng-ti-mét nhưng từ đầu đến đuôi phủ kín hàng trăm chiếc gai nón sắc nhọn như một cỗ xe bọc thép thời Trung cổ! Xin trân trọng giới thiệu: Thằn Lằn Quỷ Gai — quái kiệt sa mạc được giới khoa học mệnh danh bằng cái tên kiêu hãnh: Chiến Binh Gai Góc! [surprise-oh]
```
**Part 2** → `audio/vs/scene01_p2.wav` (119 ký tự) · 🎭 cameo `be_con`

```text
Giáo sư ơi! Giữa biển cát khô cằn không có lấy một vũng nước thế này, chú thằn lằn này làm sao giải khát để sống sót ạ?
```
**Part 3** → `audio/vs/scene01_p3.wav` (249 ký tự) · mood `hao_hung`

```text
Khán giả nhí vừa hỏi đúng bí mật chấn động nhất của tạo hóa! Hãy nhìn chiếc camera quay siêu chậm của chúng tôi: Chiến Binh Gai Góc không hề cúi đầu tìm nước, mà nó chỉ việc thong thả bước bốn bàn chân lên nền cát còn hơi ẩm sương đêm! [surprise-wa]
```
**Part 4** → `audio/vs/scene01_p4.wav` (409 ký tự) · mood `don_dap`

```text
Toàn bộ bề mặt da của Thằn Lằn Quỷ Gai là một mạng lưới các rãnh vi mao dẫn siêu hiển vi đan xen chằng chịt giữa các vảy gai. Theo định luật mao dẫn vật lý, các rãnh này tự động tạo ra một lực hút cực mạnh, hút từng giọt nước sương từ cát ẩm chảy ngược chiều trọng lực! Nước chảy từ móng chân, men theo cẳng chân, chạy dọc bờ bụng, leo qua sống lưng và hội tụ thẳng tắp về hai khóe miệng của nó! [surprise-oh]
```
**Part 5** → `audio/vs/scene01_p5.wav` (506 ký tự) · mood `don_dap`

```text
Các nhà vật lý học thuộc Viện nghiên cứu Đức khi đưa lớp da của Thằn Lằn Quỷ Gai vào kính hiển vi điện tử quét đã phải sửng sốt: những rãnh mao dẫn này có bề rộng biến thiên từ năm đến một trăm năm mươi mi-crô-mét, được thiết kế hình học bất đối xứng để nước chỉ có thể chảy một chiều về phía trước mà tuyệt đối không thể chảy ngược lại! Không cần bất kỳ một chiếc máy bơm cơ học hay trái tim co bóp, lực hút liên kết phân tử của nước tự kéo nhau chạy thẳng vào khoang miệng một cách kỳ diệu! [surprise-wa]
```
**Part 6** → `audio/vs/scene01_p6.wav` (444 ký tự) · mood `hao_hung`

```text
Chú thằn lằn chỉ việc đứng yên một chỗ, nhấp nháy hàm dưới nhịp nhàng như đang thưởng thức cà phê sáng, thế là nước sạch tự động chảy tọt vào họng mà không cần tốn một giọt mồ hôi! Thậm chí nếu bạn nhỏ một giọt nước lên lưng nó, giọt nước ấy cũng tự động chia làn chảy ngược về miệng trong vòng vài giây! Một nhà máy lọc và hút nước tự động gắn liền trên da đỉnh cao đến mức các kỹ sư công nghệ vũ trụ NASA cũng phải ngả mũ bái phục! [laughter]
```

### scene02 — 00 SÁNG: CHIẾC LƯỠI DÍNH VÀ KỶ LỤC 2.500 CON KIẾN
*Thẻ chương:* MÁY HÚT KIẾN TỐC ĐỘ CAO SA MẠC

*Badge:* `09:00 SÁNG` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene02_p0.wav` (242 ký tự) · mood `hao_hung`

```text
Đồng hồ điểm không chín giờ sáng! Mặt trời sa mạc bắt đầu nhô cao, nhiệt độ không khí tăng vọt lên ba mươi lăm độ C. Uống đẫm nước xong xuôi, chiếc dạ dày của Chiến Binh Gai Góc bắt đầu réo vang ùng ục, báo hiệu đã đến giờ ăn sáng! [laughter]
```
**Part 1** → `audio/vs/scene02_p1.wav` (319 ký tự) · mood `don_dap`

```text
Nhưng quý vị có biết thực đơn của quái kiệt này gồm những món gì không? Rất giản dị nhưng cực kỳ khó nuốt: một trăm phần trăm khẩu phần ăn cả đời của nó chỉ là loài kiến đen nhỏ mang tên I-ri-đô-mia-mếch — loài kiến chứa đầy a-xít phoóc-mích độc hại và mùi hôi nồng nặc mà mọi loài động vật khác đều phải lắc đầu né xa!
```
**Part 2** → `audio/vs/scene02_p2.wav` (410 ký tự) · mood `don_dap`

```text
Chiến Binh Gai Góc lạch bạch bò đến bên cạnh một đường mòn kiến chạy qua bãi cát. Nó ngồi xổm xuống một cách cực kỳ kiên nhẫn hệt như một ông cụ ngồi câu cá bên bờ sông. Và ngay khi đàn kiến hành quân ngang qua, vũ khí bí mật được kích hoạt: chẹp, chẹp, chẹp! Chiếc lưỡi dày phủ đầy chất nhầy siêu dính của nó phóng ra với tốc độ tên lửa, trong một giây có thể thò ra thụt vào tới hai đến ba lần! [surprise-wa]
```
**Part 3** → `audio/vs/scene02_p3.wav` (129 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Ối cứu bọn em với! Bác này bác ấy ngồi ngay cửa hang, bác ấy lia lưỡi một cái là mất tích cả trung đội kiến nhà em rồi cà nhà ơi!
```
**Part 4** → `audio/vs/scene02_p4.wav` (499 ký tự) · mood `hao_hung`

```text
Quý vị thử nghĩ mà xem: a-xít phoóc-mích của kiến đen có thể làm bỏng rát da người và giết chết nhiều loài thú nhỏ, nhưng khi chui vào dạ dày của Chiến Binh Gai Góc thì lại bị trung hòa hoàn toàn bởi một loại dịch nhầy đệm đặc biệt! Nó tiêu hóa đàn kiến ngon lành như chúng ta ăn snack cay giòn rụm! Thậm chí chiếc đuôi của nó còn đóng vai trò như một kho dự trữ mỡ khổng lồ, tích tụ năng lượng từ đống protein kiến để giúp chú thằn lằn nhịn ăn nhiều tháng liền khi mùa khô hạn ập đến! [surprise-oh]
```
**Part 5** → `audio/vs/scene02_p5.wav` (473 ký tự) · mood `hao_hung`

```text
Tiếng kêu cứu thất thanh của bầy kiến hoàn toàn bất lực trước máy hút bụi sinh học này! Các nhà nghiên cứu sinh thái học đã đếm từng nhịp nuốt và ghi nhận con số kỷ lục: trong một bữa ăn kéo dài vài tiếng đồng hồ, một chú Thằn Lằn Quỷ Gai có thể nuốt chửng từ một ngàn đến hai ngàn năm trăm con kiến độc! Dạ dày của nó có lớp màng bảo vệ đặc biệt dày dặn để vô hiệu hóa hoàn toàn nọc độc a-xít của đàn kiến, biến chúng thành nguồn năng lượng dồi dào để sinh tồn! [laughter]
```

### scene03 — 00 TRƯA: BƯỚU GAI ĐẦU GIẢ VÀ NẮNG CHÁY 45 ĐỘ C
*Thẻ chương:* CÚ CÚI ĐẦU TỬ THỦ TRƯỚC SÁT THỦ

*Badge:* `13:00 TRƯA` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene03_p0.wav` (245 ký tự) · mood `tram_bi_an`

```text
Đồng hồ điểm mười ba giờ trưa! Ánh nắng sa mạc như trút lửa xuống mặt đất, nhiệt độ bề mặt cát đo được đã vượt ngưỡng năm mươi độ C! Giữa lúc không khí ngột ngạt đến nghẹt thở, hiểm nguy từ những kẻ săn mồi khát máu bắt đầu ập tới! [surprise-oh]
```
**Part 1** → `audio/vs/scene03_p1.wav` (305 ký tự) · mood `tram_bi_an`

```text
Trên bầu trời rực nắng, loài chim săn mồi mắt tinh như dao cạo đang lượn vòng; còn dưới mặt đất, một chú kỳ đà khổng lồ Va-ra-nút dài hai mét đang lùng sục từng bụi cỏ khô tìm kiếm con mồi. Với đôi chân ngắn ngủn di chuyển chậm chạp, Thằn Lằn Quỷ Gai chạy trốn thế nào được trước những sát thủ tốc độ này?
```
**Part 2** → `audio/vs/scene03_p2.wav` (268 ký tự) · mood `don_dap`

```text
Nó không thèm chạy trốn! Chiến Binh Gai Góc lập tức kích hoạt tuyệt chiêu đánh lừa thị giác đỉnh cao: Chiếc Đầu Giả Bằng Gai! Quý vị hãy nhìn kỹ vào sau gáy của nó: có một bướu thịt lớn mọc nhô cao với hai chiếc gai sừng to tướng trông y hệt như một chiếc đầu thứ hai!
```
**Part 3** → `audio/vs/scene03_p3.wav` (261 ký tự) · mood `don_dap`

```text
Khi kẻ địch lao vào tấn công, chú thằn lằn lập tức cúi gục chiếc đầu thật chứa não và mắt giấu kín vào giữa hai chân trước, áp sát mặt xuống đất! Đồng thời, nó ngóc chiếc đầu giả đầy gai nhọn hoắt nhô cao lên không trung để mời gọi kẻ thù cắn vào! [surprise-wa]
```
**Part 4** → `audio/vs/scene03_p4.wav` (170 ký tự) · 🎭 cameo `ga_khong_lo`

```text
Thằng nhóc con trốn đi đâu! Xem cú ngoạm sắt thép của tao cắn nát đầu mày đây... Ái chà chà! Cái đầu gì mà toàn gai nhọn đâm thủng cả lợi, chảy máu mồm rồi đau quá mẹ ơi!
```
**Part 5** → `audio/vs/scene03_p5.wav` (399 ký tự) · mood `hao_hung`

```text
Cú đớp chí mạng của kẻ săn mồi cắn trúng ngay bướu gai cứng như đá tảng, khiến kẻ tấn công đau đớn nhổ vội ra ngoài trong sự cay đắng tột cùng! Trong khi kẻ săn mồi đang ôm miệng sưng vù la oai oái, đầu thật của Chiến Binh Gai Góc vẫn nguyên vẹn một trăm phần trăm, bình thản ngóc lên nhìn kẻ thù bằng ánh mắt khinh bỉ tột độ! Một pha hy sinh đầu giả cứu đầu thật ngoạn mục không đối thủ! [laughter]
```

### scene04 — 00 HOÀNG HÔN: QUẢ CẦU GAI PHỒNG TO VÀ DÁNG ĐI LÁ KHÔ
*Thẻ chương:* CHIẾN THUẬT PHÒNG THỦ KHÔNG THỂ NUỐT TRÔI

*Badge:* `17:00 HOÀNG HÔN` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene04_p0.wav` (267 ký tự) · mood `don_dap`

```text
Mặt trời ngả về tây, đồng hồ chuyển điểm mười bảy giờ chiều hoàng hôn! Bầu trời sa mạc chuyển sang sắc cam rực lửa đầy ma mị. Nhưng một kẻ săn mồi ranh mãnh khác lại xuất hiện: loài chó hoang Đin-gô hung dữ của châu Úc đang đánh hơi lần theo dấu vết của chú thằn lằn!
```
**Part 1** → `audio/vs/scene04_p1.wav` (461 ký tự) · mood `don_dap`

```text
Nếu kẻ săn mồi cố tình nuốt trọn cả cơ thể vào bụng thì sao? Chiến Binh Gai Góc lập tức tung ra chiêu phòng thủ thứ hai: Phồng to thành quả cầu gai bọc thép! Nó hít căng không khí vào hai lá phổi, ép cơ hoành phồng to lồng ngực làm kích thước cơ thể phình to gấp đôi bình thường! Hàng trăm chiếc gai nhọn trên lưng vốn dĩ nằm xuôi nay dựng đứng vuông góc chín mươi độ, biến nó thành một quả cầu chông sắt gai góc không có bất kỳ khe hở nào để cắn! [surprise-oh]
```
**Part 2** → `audio/vs/scene04_p2.wav` (288 ký tự) · mood `hao_hung`

```text
Kẻ săn mồi há miệng to định nuốt chửng nhưng cổ họng lập tức bị những chiếc gai nhọn đâm nghẹn cứng đờ, không tài nào nuốt trôi xuống dạ dày được mà phải nhè vội ra bãi cát! Và sau khi thoát hiểm, quý vị hãy chiêm ngưỡng dáng đi độc nhất vô nhị của quái kiệt này: Dáng đi lá khô đung đưa!
```
**Part 3** → `audio/vs/scene04_p3.wav` (409 ký tự) · mood `hao_hung`

```text
Và nếu như cơn bão cát sa mạc khốc liệt bất ngờ nổi lên với những trận cuồng phong mù trời, quái kiệt này còn có một tuyệt chiêu đào hầm thần tốc! Bốn bàn chân có móng vuốt cong sắc nhọn của nó cào cát xoay tròn như bốn chiếc máy xúc mini, chỉ mất vỏn vẹn ba mươi giây là toàn bộ thân hình gai góc đã lặn mất tăm dưới lòng cát đỏ sâu mười xăng-ti-mét, bình an vô sự mặc cho bão táp gầm rú trên đầu! [laughter]
```
**Part 4** → `audio/vs/scene04_p4.wav` (449 ký tự) · mood `am_ap`

```text
Nó bước một chân lên phía trước, rồi dừng lại giật cục, lắc lư thân mình tới lui hai ba nhịp như một cành cây khô đu đưa trước gió rồi mới bước tiếp bước thứ hai! Dáng đi robot giật cục này hòa lẫn hoàn hảo vào chuyển động của cỏ cây sa mạc, làm hệ thống thị giác bắt chuyển động của chim săn mồi hoàn toàn bị mất dấu mục tiêu! Vừa bọc thép gai góc, vừa biết tàng hình bằng vũ điệu giật cục, đúng là bậc thầy phòng thủ số một thiên nhiên! [laughter]
```

### scene05 — 00 ĐÊM: ĐỔI MÀU ĐIỀU HÒA NHIỆT ĐỘ GIỮA SA MẠC LẠNH BUỐT
*Thẻ chương:* BỘ ÁO GIÁP TẮC KÈ ĐỔI MÀU THÔNG MINH

*Badge:* `21:00 ĐÊM` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene05_p0.wav` (348 ký tự) · mood `tram_bi_an`

```text
Màn đêm sa mạc buông xuống, đồng hồ điểm hai mươi mốt giờ đêm! Cát sa mạc tỏa nhiệt cực nhanh khiến nhiệt độ tụt dốc không phanh từ bốn mươi lăm độ C ban ngày rơi thẳng xuống dưới mười độ C lạnh buốt xương tủy! Giữa sự khắc nghiệt điên rồ ấy, Chiến Binh Gai Góc lại tiếp tục biểu diễn tuyệt kỹ thứ ba: Biến hóa màu sắc như tắc kè hoa! [surprise-oh]
```
**Part 1** → `audio/vs/scene05_p1.wav` (296 ký tự) · mood `am_ap`

```text
Vào buổi trưa nắng cháy, làn da của nó chuyển sang màu vàng cát nhạt hoặc xám sáng để phản xạ tối đa ánh sáng mặt trời, giúp cơ thể không bị sốc nhiệt nấu chín. Nhưng khi đêm lạnh tràn về, các tế bào sắc tố dưới da lập tức giãn nở, đổi màu toàn bộ cơ thể sang màu nâu sẫm, xám đen và đất đỏ thẫm!
```
**Part 2** → `audio/vs/scene05_p2.wav` (325 ký tự) · mood `am_ap`

```text
Màu da đen tối này giúp nó hấp thụ từng tia nhiệt lượng tàn dư cuối cùng của mặt đất, giữ ấm cho các cơ quan nội tạng suốt đêm dài. Đồng thời, màu sắc đất đỏ này ngụy trang nó hòa lẫn hoàn hảo vào màu cát sa mạc Red Centre nước Úc, khiến những con cú đêm hay rắn độc bò ngang qua cũng chỉ nhìn thấy một cục đá vô tri vô giác!
```
**Part 3** → `audio/vs/scene05_p3.wav` (441 ký tự) · mood `am_ap`

```text
Đặc biệt vào những tháng mùa đông băng giá của sa mạc miền Trung nước Úc, Thằn Lằn Quỷ Gai sẽ bước vào trạng thái ngủ đông đặc biệt. Toàn bộ quá trình trao đổi chất của nó giảm xuống mức tối thiểu, nhịp tim đập chậm lại chỉ còn vài nhịp mỗi phút để tiết kiệm từng giọt năng lượng quý giá! Nó nằm bất động dưới lòng đất cát, kiên nhẫn chờ đợi cho đến khi ánh nắng xuân ấm áp đánh thức nó bước vào một chu kỳ sinh tồn mới rực rỡ! [surprise-oh]
```
**Part 4** → `audio/vs/scene05_p4.wav` (331 ký tự) · mood `hao_hung`

```text
Và quý vị có biết nhiều người từng đồn thổi loài này có tài bắn máu từ mắt không? Khoa học xin đính chính: bắn máu từ mắt là vũ khí của thằn lằn sừng châu Mỹ; còn Thằn Lằn Quỷ Gai nước Úc hoàn toàn không cần bắn máu, vì bộ giáp gai thép và chiếc đầu giả của nó đã quá đủ để khiến mọi kẻ săn mồi phải bỏ chạy mất dép rồi! [laughter]
```

### scene06 — 00 RẠNG SÁNG: BẢN LĨNH SINH TỒN ĐỈNH CAO VÀ BÓNG ĐEN TẬP 20
*Thẻ chương:* BẬT MÍ BÓNG ĐEN BÍ ẨN CỦA QUÁI KIỆT TẬP 20

*Badge:* `03:00 RẠNG SÁNG` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (344 ký tự) · mood `am_ap`

```text
Đồng hồ điểm không ba giờ rạng sáng! Những luồng gió buốt lạnh thổi qua cồn cát hoang vu, khép lại hai mươi tư giờ tác nghiệp nghẹt thở theo chân Chiến Binh Gai Góc. Một sinh vật nhỏ bé không có nanh nhọn, không có nọc độc, chạy chậm như rùa nhưng đã kiên cường ngự trị giữa sa mạc khô cằn khắc nghiệt nhất hành tinh qua hàng triệu năm lịch sử!
```
**Part 1** → `audio/vs/scene06_p1.wav` (272 ký tự) · mood `am_ap`

```text
Biến làn da thành rãnh hút nước, biến đầu giả thành bia đỡ đạn, biết cuộn tròn phòng thủ và kiên nhẫn với con đường của riêng mình, đó chính là bài học sinh tồn vĩ đại mà tự nhiên ban tặng cho chúng ta! Chậm chạp nhưng không hề yếu đuối, gai góc để tự vệ chứ không hại ai!
```
**Part 2** → `audio/vs/scene06_p2.wav` (257 ký tự) · mood `hao_hung`

```text
Hành trình hai mươi tư giờ cùng Thằn Lằn Quỷ Gai đã chính thức khép lại! Nhưng ngay lúc này, xin mời toàn thể quý vị khán giả hãy hướng mắt lên màn hình lớn để giải mã BÓNG ĐEN BÍ ẨN của nhân vật xuất hiện trong Tập hai mươi cột mốc tiếp theo! [surprise-oh]
```
**Part 3** → `audio/vs/scene06_p3.wav` (512 ký tự) · mood `don_dap`

```text
Xin gửi tới quý vị ba manh mối chấn động về bóng đen bí ẩn này: Thứ nhất, đây là siêu xạ thủ bắn tỉa thiên tài bậc nhất thế giới loài cá, sở hữu tuyệt chiêu nén tia nước bắn hạ con mồi đang đậu trên cành cây cao cách xa tới ba mét! Thứ hai, bộ não thiên tài có khả năng tự động tính toán độ lệch khúc xạ ánh sáng giữa nước và không khí chính xác đến từng mi-li-mét! Và thứ ba, khẩu đại bác nước nén trong rãnh vòm miệng với áp lực nước cực mạnh làm rách toạc cánh côn trùng rơi tõm xuống nước làm mồi! [laughter]
```
**Part 4** → `audio/vs/scene06_p4.wav` (254 ký tự) · mood `hao_hung`

```text
Quý vị khán giả có nhận ra bóng đen xạ thủ bắn tỉa dưới nước này là loài cá nào không? Hãy để lại phán quyết và dự đoán của bạn ngay dưới phần bình luận nhé! Phóng viên sinh tồn hai mươi tư giờ xin chào tạm biệt và hẹn gặp lại quý vị trong tập tiếp theo!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Không năm giờ sáng giữa sa mạc Úc cháy bỏng! Một sinh vật không cần cúi đầu mà vẫn có thể uống nước ngọt lành chỉ bằng cách dẫm bàn chân lên cát ẩm! Đó chính là Thằn Lằn Quỷ Gai, quái kiệt bọc thép dài hai mươi xăng-ti-mét của lục địa nắng cháy. Làn da của nó phủ đầy mạng lưới rãnh mao dẫn siêu nhỏ, tự động hút từng giọt sương mai từ bàn chân chảy ngược chiều trọng lực dọc theo sống lưng chạy thẳng vào miệng! [surprise-wa] Mỗi ngày, nó kiên nhẫn nuốt chửng tới hai ngàn năm trăm con kiến đen độc hại bằng chiếc lưỡi dính siêu tốc. Khi bị kẻ săn mồi tấn công, nó cúi gục đầu thật xuống đất và chìa chiếc bướu gai đầu giả sắc nhọn sau gáy ra ngoài lừa kẻ thù cắn rách mồm! [laughter] Chưa hết, nó còn có thể hít khí phồng to cơ thể gấp đôi thành quả cầu gai bọc thép không kẻ nào nuốt trôi! Vậy là bí mật đã sáng tỏ: một cỗ xe tăng tí hon với bản lĩnh sinh tồn đỉnh cao ngự trị chảo lửa sa mạc suốt hàng triệu năm qua!
```

**Whisper prompt:** `Thằn Lằn Quỷ Gai, Chiến Binh Gai Góc, Moloch horridus, mao dẫn, Iridomyrmex, sa mạc Úc, Alice Springs, 2.500 con kiến, 45 độ C, bướu gai đầu giả, quả cầu gai, Cá Cung Thủ`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| hai mươi tư giờ | 24 giờ |
| Hai mươi tư giờ | 24 giờ |
| không năm giờ | 05:00 |
| Không năm giờ | 05:00 |
| không chín giờ | 09:00 |
| Không chín giờ | 09:00 |
| mười ba giờ | 13:00 |
| Mười ba giờ | 13:00 |
| mười bảy giờ | 17:00 |
| Mười bảy giờ | 17:00 |
| hai mươi mốt giờ | 21:00 |
| Hai mươi mốt giờ | 21:00 |
| không ba giờ | 03:00 |
| Không ba giờ | 03:00 |
| bốn mươi lăm độ C | 45°C |
| Bốn mươi lăm độ C | 45°C |
| năm mươi độ C | 50°C |
| Năm mươi độ C | 50°C |
| dưới mười độ C | dưới 10°C |
| hai ngàn năm trăm | 2.500 |
| Hai ngàn năm trăm | 2.500 |
| một ngàn | 1.000 |
| Một ngàn | 1.000 |
| năm ngàn | 5.000 |
| hai mươi xăng-ti-mét | 20cm |
| Hai mươi xăng-ti-mét | 20cm |
| mười lăm đến hai mươi xăng-ti-mét | 15-20cm |
| ba mét | 3m |
| Ba mét | 3m |
| hai mét | 2m |
| một giây | 1 giây |
| ba lần | 3 lần |
| hai lần | 2 lần |
| gấp hai lần | gấp 2 lần |
| gấp đôi | gấp đôi |
| một trăm phần trăm | 100% |
| chín mươi phần trăm | 90% |
| hàng triệu năm | hàng triệu năm |
| triệu năm | triệu năm |
| hai ngàn mười bảy | 2017 |
| một ngàn chín trăm sáu mươi hai | 1962 |
| Tập hai mươi | Tập 20 |
| Mo-lốc | Moloch |
| Hor-ri-đút | horridus |
| I-ri-đô-mia-mếch | Iridomyrmex |
| A-li-xơ Xpơ-rinh | Alice Springs |
| Đin-gô | Dingo |
| Va-ra-nút | Varanus |
| ba mươi lăm độ C | 35°C |
| Ba mươi lăm độ C | 35°C |
| ba mươi lăm | 35 |
| chín mươi độ | 90° |
| chín mươi | 90 |
| hai ba nhịp | 2-3 nhịp |
| hai ba | 2-3 |
| năm đến một trăm năm mươi mi-crô-mét | 5-150 μm |
| năm mi-crô-mét | 5 μm |
| một trăm năm mươi mi-crô-mét | 150 μm |
| ba mươi giây | 30 giây |
| mười xăng-ti-mét | 10cm |
| vài nhịp | vài nhịp |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · 00 SÁNG: TUYỆT KỸ UỐNG SƯƠNG MAO DẪN BẰNG BÀN CHÂN · 124.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:03.7 (3.7s) | L01 | Bíp bíp bíp! Đồng hồ điểm 05:00 sáng! |  | Toàn cảnh sa mạc Red Centre nước Úc lúc bình minh: BÊN TRÁI phóng viên truyền hình 24h mặc áo gile thám hiểm nhiều túi, tay cầm micro có logo '24H WILD' cầm micro phát sóng trực tiếp; Ở GIỮA đồng hồ cát khổng lồ hiện số 05:00 sáng; BÊN PHẢI những cồn cát đỏ rực trải dài vô tận. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này. |
| b02 | 00:03.7–00:18.3 (14.6s) | L02 | Phóng viên truyền hình sinh tồn 24 giờ xin kính chào toàn thể quý vị khán giả! Ngay lúc này, tôi đang có mặt trực tiếp tại chảo lửa sa mạc đỏ rực miền Trung nước Úc, nơi nhiệt độ có thể chênh lệch kinh hoàng từ lạnh thấu xương lúc rạng đông lên tới 45°C khi mặt trời lên đỉnh đầu! | **45°C** · CHẢO LỬA SA MẠC · R/380 · [0.75, 0.45] | Nhiệt kế đo nhiệt độ sa mạc: cột nhiệt độ chỉ mức lạnh thấu xương lúc sáng sớm và mũi tên đỏ chỉ mức vọt lên 45°C lúc giữa trưa gay gắt. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này. |
| b03 | 00:18.3–00:23.4 (5.1s) | L03 | Trước mắt chúng ta là một sinh vật có diện mạo kỳ quái và gai góc bậc nhất thế giới tự nhiên! |  | Cận cảnh xuất hiện của chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh: toàn thân bọc kín hàng trăm chiếc gai nón nhọn hoắt như cỗ xe bọc thép thời cổ, chiếc mũ safari kaki đội ngay ngắn, nơ đỏ nổi bật trên cổ. |
| b04 | 00:23.4–00:31.7 (8.3s) | L04 | Thân hình chỉ dài vỏn vẹn 20cm nhưng từ đầu đến đuôi phủ kín hàng trăm chiếc gai nón sắc nhọn như một cỗ xe bọc thép thời Trung cổ! | **DÀI 20CM** · CHIẾN BINH GAI GÓC · L/390 · [0.28, 0.48] | Thước đo so sánh: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh dài vỏn vẹn 20cm đứng cạnh bàn chân người; toàn thân bao bọc bởi lớp gai nhọn xù xì đe dọa. |
| b05 | 00:31.7–00:38.9 (7.3s) | L52 | Xin trân trọng giới thiệu: Thằn Lằn Quỷ Gai — quái kiệt sa mạc được giới khoa học mệnh danh bằng cái tên kiêu hãnh: Chiến Binh Gai Góc! | **QUỶ GAI** · CHIẾN BINH GAI GÓC · R/380 · [0.75, 0.45] | Chân dung hào hùng của chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh: đứng kiêu hãnh trên mỏm đá sa mạc đỏ rực, gió thổi bay dải nơ đỏ thắm, ánh mặt trời mọc rực rỡ phía sau. |
| b06 | 00:38.9–00:45.2 (6.3s) | L05 | Giáo sư ơi! Giữa biển cát khô cằn không có lấy một vũng nước thế này, chú thằn lằn này làm sao giải khát để sống sót ạ? |  | Khán giả nhí hoạt hình ngơ ngác nhìn quanh cồn cát khô cằn nứt nẻ không một giọt nước, cầm chiếc bình nước rỗng tuếch lắc lắc tuyệt vọng. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này. |
| b07 | 00:45.2–00:58.5 (13.3s) | L06 | Khán giả nhí vừa hỏi đúng bí mật chấn động nhất của tạo hóa! Hãy nhìn chiếc camera quay siêu chậm của chúng tôi: Chiến Binh Gai Góc không hề cúi đầu tìm nước, mà nó chỉ việc thong thả bước bốn bàn chân lên nền cát còn hơi ẩm sương đêm! |  | Camera quay siêu chậm: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh thong thả đặt 4 bàn chân lên lớp cát ẩm sương mai; các hạt sương đọng lấp lánh quanh móng chân sắc nhọn. |
| b08 | 00:58.5–01:04.9 (6.4s) | L07 | Toàn bộ bề mặt da của Thằn Lằn Quỷ Gai là một mạng lưới các rãnh vi mao dẫn siêu hiển vi đan xen chằng chịt giữa các vảy gai. |  | Kính hiển vi phóng đại da chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh: mạng lưới rãnh mao dẫn siêu hiển vi đan xen như mạng lưới kênh rạch thủy lợi giữa các chân gai nhọn phát sáng xanh lam. |
| b09 | 01:04.9–01:11.0 (6.1s) | L08 | Theo định luật mao dẫn vật lý, các rãnh này tự động tạo ra một lực hút cực mạnh, hút từng giọt nước sương từ cát ẩm chảy ngược chiều trọng lực! | **MAO DẪN** · HÚT NƯỚC NGƯỢC DÒNG · L/390 · [0.28, 0.48] | Mô phỏng lực mao dẫn vật lý: các giọt nước sương từ hạt cát ẩm tự động bị hút ngược chiều trọng lực, chảy thành dòng nước tí hon dọc cẳng chân và bụng. |
| b10 | 01:11.0–01:17.5 (6.6s) | L09 | Nước chảy từ móng chân, men theo cẳng chân, chạy dọc bờ bụng, leo qua sống lưng và hội tụ thẳng tắp về hai khóe miệng của nó! |  | Sơ đồ dòng chảy trên cơ thể chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh: các mũi tên nước màu xanh dương chạy dọc từ 4 chân, leo qua bờ bụng, vượt sống lưng và đổ thẳng về hai khóe miệng. |
| b11 | 01:17.5–01:23.8 (6.3s) | L10 | Các nhà vật lý học thuộc Viện nghiên cứu Đức khi đưa lớp da của Thằn Lằn Quỷ Gai vào kính hiển vi điện tử quét đã phải sửng sốt: |  | Phòng thí nghiệm Viện nghiên cứu Đức: các nhà khoa học đang phân tích lớp da thằn lằn quỷ gai trên màn hình kính hiển vi điện tử quét SEM. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này. |
| b12 | 01:23.8–01:32.7 (8.9s) | L53 | những rãnh mao dẫn này có bề rộng biến thiên từ 5-150 μm, được thiết kế hình học bất đối xứng để nước chỉ có thể chảy một chiều về phía trước mà tuyệt đối không thể chảy ngược lại! | **5-150 μM** · RÃNH MAO DẪN · R/380 · [0.75, 0.45] | Mô phỏng 3D rãnh mao dẫn bất đối xứng bề rộng 5-150 μm: nước chảy cuồn cuộn một chiều về phía trước, khóa chặt không cho chảy ngược lại. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này. |
| b13 | 01:32.7–01:40.9 (8.1s) | L11 | Không cần bất kỳ một chiếc máy bơm cơ học hay trái tim co bóp, lực hút liên kết phân tử của nước tự kéo nhau chạy thẳng vào khoang miệng một cách kỳ diệu! |  | Hình ảnh so sánh: một bên chiếc máy bơm cơ học bị gạch chéo đỏ; một bên là giọt nước tự động kết nối kéo nhau chạy trên da chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh kỳ diệu. |
| b14 | 01:40.9–01:50.2 (9.4s) | L12 | Chú thằn lằn chỉ việc đứng yên một chỗ, nhấp nháy hàm dưới nhịp nhàng như đang thưởng thức cà phê sáng, thế là nước sạch tự động chảy tọt vào họng mà không cần tốn một giọt mồ hôi! |  | chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh đứng thong dong chớp mắt, hai hàm nhấp nháy nhịp nhàng như đang thưởng thức ly nước mát lạnh; nước sạch tự động chảy tọt vào họng sảng khoái. |
| b15 | 01:50.2–02:04.2 (13.9s) | L13 | Thậm chí nếu bạn nhỏ một giọt nước lên lưng nó, giọt nước ấy cũng tự động chia làn chảy ngược về miệng trong vòng vài giây! Một nhà máy lọc và hút nước tự động gắn liền trên da đỉnh cao đến mức các kỹ sư công nghệ vũ trụ NASA cũng phải ngả mũ bái phục! |  | Thí nghiệm nhỏ giọt nước: một giọt nước rơi trúng lưng chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh, giọt nước lập tức phân nhánh chảy men theo các rãnh gai lao thẳng về miệng trong tích tắc. |

### scene02 · 00 SÁNG: CHIẾC LƯỠI DÍNH VÀ KỶ LỤC 2.500 CON KIẾN · 104.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:12.9 (12.9s) | L14 | Đồng hồ điểm 09:00 sáng! Mặt trời sa mạc bắt đầu nhô cao, nhiệt độ không khí tăng vọt lên 35°C. Uống đẫm nước xong xuôi, chiếc dạ dày của Chiến Binh Gai Góc bắt đầu réo vang ùng ục, báo hiệu đã đến giờ ăn sáng! | **35°C** · NẮNG NÓNG BẮT ĐẦU · R/380 · [0.75, 0.45] | BÊN TRÁI đồng hồ chuyển sang mốc 09:00 sáng; Ở GIỮA ánh mặt trời bắt đầu gay gắt 35°C; BÊN PHẢI chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh bụng kêu 'ùng ục' xoa bụng đói meo hài hước. |
| b02 | 00:12.9–00:27.9 (14.9s) | L15 | Nhưng quý vị có biết thực đơn của quái kiệt này gồm những món gì không? Rất giản dị nhưng cực kỳ khó nuốt: 100% khẩu phần ăn cả đời của nó chỉ là loài kiến đen nhỏ mang tên Iridomyrmex — loài kiến chứa đầy a-xít phoóc-mích độc hại và mùi hôi nồng nặc mà mọi loài động vật khác đều phải lắc đầu né xa! | **100% KIẾN** · THỰC ĐƠN ĐỘC NHẤT · L/390 · [0.28, 0.48] | Thực đơn sa mạc đặc biệt: 100% là loài kiến đen Iridomyrmex chứa đầy a-xít phoóc-mích; một con kiến đen hung hăng giơ hai càng đe dọa. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này. |
| b03 | 00:27.9–00:35.6 (7.7s) | L16 | Chiến Binh Gai Góc lạch bạch bò đến bên cạnh một đường mòn kiến chạy qua bãi cát. Nó ngồi xổm xuống một cách cực kỳ kiên nhẫn hệt như một ông cụ ngồi câu cá bên bờ |  | chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh ngồi xổm bất động bên cạnh đường mòn kiến đen chạy qua bãi cát, kiên nhẫn như ông cụ ngồi câu cá bên hồ. |
| b04 | 00:35.6–00:39.9 (4.3s) | L17 | sông. Và ngay khi đàn kiến hành quân ngang qua, vũ khí bí mật được kích hoạt: chẹp, chẹp, chẹp! |  | Đàn kiến đen nối đuôi nhau hành quân trên nền cát đỏ; bóng lưng chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh khổng lồ phủ bóng xuống như ngọn núi phục kích. |
| b05 | 00:39.9–00:46.9 (7.1s) | L18 | Chiếc lưỡi dày phủ đầy chất nhầy siêu dính của nó phóng ra với tốc độ tên lửa, trong 1 giây có thể thò ra thụt vào tới hai đến 3 lần! | **1 GIÂY** · THÒ THỤT 2-3 LẦN · R/380 · [0.75, 0.45] | Tốc độ săn mồi chớp nhoáng: chiếc lưỡi dính màu hồng của chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh phóng ra như tia chớp, 1 giây thò thụt 2-3 lần tóm gọn từng chú kiến đen. |
| b06 | 00:46.9–00:54.5 (7.5s) | L19 | Ối cứu bọn em với! Bác này bác ấy ngồi ngay cửa hang, bác ấy lia lưỡi một cái là mất tích cả trung đội kiến nhà em rồi cà nhà ơi! |  | Cảnh tượng bi hài: cả trung đội kiến đen hoảng loạn tháo chạy tán loạn khi chiếc lưỡi khổng lồ của chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh quét sạch cả hàng ngũ. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này. |
| b07 | 00:54.5–01:01.1 (6.7s) | L20 | Quý vị thử nghĩ mà xem: a-xít phoóc-mích của kiến đen có thể làm bỏng rát da người và giết chết nhiều loài thú nhỏ, |  | Bình hóa chất a-xít phoóc-mích bốc khói độc hại; so sánh bên cạnh là các loài thú nhỏ sợ hãi lùi xa né tránh đàn kiến đen. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này. |
| b08 | 01:01.1–01:09.7 (8.6s) | L54 | nhưng khi chui vào dạ dày của Chiến Binh Gai Góc thì lại bị trung hòa hoàn toàn bởi một loại dịch nhầy đệm đặc biệt! Nó tiêu hóa đàn kiến ngon lành như chúng ta ăn snack cay giòn rụm! |  | Bên trong dạ dày chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh: lớp dịch nhầy đệm đặc biệt bao bọc trung hòa toàn bộ a-xít của kiến đen, biến chúng thành năng lượng tích tụ ở chiếc đuôi mập mạp. |
| b09 | 01:09.7–01:20.5 (10.8s) | L21 | Thậm chí chiếc đuôi của nó còn đóng vai trò như một kho dự trữ mỡ khổng lồ, tích tụ năng lượng từ đống protein kiến để giúp chú thằn lằn nhịn ăn nhiều tháng liền khi mùa khô hạn ập đến! |  | Chiếc đuôi mập mạp của chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh phình to chứa các hạt mỡ năng lượng vàng óng; biểu tượng bình ắc-quy tích lũy năng lượng cho mùa hạn hán. |
| b10 | 01:20.5–01:25.2 (4.6s) | L22 | Tiếng kêu cứu thất thanh của bầy kiến hoàn toàn bất lực trước máy hút bụi sinh học này! |  | Bầy kiến đen hoảng loạn tháo chạy bất lực trước máy hút bụi sinh học của chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này. |
| b11 | 01:25.2–01:35.9 (10.8s) | L63 | Các nhà nghiên cứu sinh thái học đã đếm từng nhịp nuốt và ghi nhận con số kỷ lục: trong một bữa ăn kéo dài vài tiếng đồng hồ, một chú Thằn Lằn Quỷ Gai có thể nuốt chửng từ 1.000 đến 2.500 con kiến độc! | **2.500 CON** · KỶ LỤC KIẾN/NGÀY · R/400 · [0.75, 0.5] | Bộ đếm kỷ lục ăn kiến: con số nhảy vọt từ 1.000 đến 2.500 con kiến đen; chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh ngồi liếm mép no nê thỏa mãn giữa bãi cát. |
| b12 | 01:35.9–01:44.7 (8.8s) | L55 | Dạ dày của nó có lớp màng bảo vệ đặc biệt dày dặn để vô hiệu hóa hoàn toàn nọc độc a-xít của đàn kiến, biến chúng thành nguồn năng lượng dồi dào để sinh tồn! |  | Cấu tạo thành dạ dày bọc thép sinh học của chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh: lớp màng nhầy đệm dày dặn ngăn cách hoàn toàn các chất độc, bảo vệ cơ thể an toàn tuyệt đối. |

### scene03 · 00 TRƯA: BƯỚU GAI ĐẦU GIẢ VÀ NẮNG CHÁY 45 ĐỘ C · 82.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:12.3 (12.3s) | L23 | Đồng hồ điểm 13:00 trưa! Ánh nắng sa mạc như trút lửa xuống mặt đất, nhiệt độ bề mặt cát đo được đã vượt ngưỡng 50°C! Giữa lúc không khí ngột ngạt đến nghẹt thở, hiểm nguy từ những kẻ săn mồi khát máu bắt đầu ập tới! | **50°C** · CÁT BỐC LỬA · R/380 · [0.75, 0.45] | BÊN TRÁI đồng hồ điểm mốc 13:00 trưa; Ở GIỮA mặt cát bốc hơi nóng hầm hập vượt 50°C; BÊN PHẢI phóng viên truyền hình 24h mặc áo gile thám hiểm nhiều túi, tay cầm micro có logo '24H WILD' lau mồ hôi nhễ nhại cảnh báo nguy hiểm. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này. |
| b02 | 00:12.3–00:16.3 (4.0s) | L24 | Trên bầu trời rực nắng, loài chim săn mồi mắt tinh như dao cạo đang lượn vòng; |  | Bầu trời rực nắng chói chang: loài chim ưng săn mồi mắt sắc như dao cạo đang dang rộng cánh lượn vòng tìm kiếm con mồi. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này. |
| b03 | 00:16.3–00:28.8 (12.5s) | L56 | còn dưới mặt đất, một chú kỳ đà khổng lồ Varanus dài 2m đang lùng sục từng bụi cỏ khô tìm kiếm con mồi. Với đôi chân ngắn ngủn di chuyển chậm chạp, Thằn Lằn Quỷ Gai chạy trốn thế nào được trước những sát thủ tốc độ này? Nó không thèm chạy trốn! | **KỲ ĐÀ 2M** · SÁT THỦ SA MẠC · L/390 · [0.28, 0.48] | Chú kỳ đà chú kỳ đà sa mạc khổng lồ dài 2m da hoa văn xám đen, biểu cảm kinh ngạc lè lưỡi thụt lùi khổng lồ dài 2m da hoa văn xám đen đang bò trườn trên mặt cát sục sạo từng bụi cỏ khô tìm kiếm chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh. |
| b04 | 00:28.8–00:40.0 (11.2s) | L25 | Chiến Binh Gai Góc lập tức kích hoạt tuyệt chiêu đánh lừa thị giác đỉnh cao: Chiếc Đầu Giả Bằng Gai! Quý vị hãy nhìn kỹ vào sau gáy của nó: có một bướu thịt lớn mọc nhô cao với hai chiếc gai sừng to tướng trông y hệt như một chiếc đầu thứ hai! | **ĐẦU GIẢ** · BƯỚU GAI SAU GÁY · R/380 · [0.75, 0.45] | Cận cảnh sau gáy chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh: chiếc bướu gai thịt nhô cao với hai chiếc gai sừng to tướng trông y hệt một chiếc đầu thứ hai đầy uy hiếp. |
| b05 | 00:40.0–00:52.3 (12.4s) | L26 | Khi kẻ địch lao vào tấn công, chú thằn lằn lập tức cúi gục chiếc đầu thật chứa não và mắt giấu kín vào giữa hai chân trước, áp sát mặt xuống đất! Đồng thời, nó ngóc chiếc đầu giả đầy gai nhọn hoắt nhô cao lên không trung để mời gọi kẻ thù cắn vào! |  | Tuyệt kỹ cúi đầu: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh giấu đầu thật kín mít vào giữa hai chân trước áp sát đất; đồng thời ngóc chiếc đầu giả đầy gai nhọn lên cao làm mồi nhử. |
| b06 | 00:52.3–01:02.0 (9.7s) | L27 | Thằng nhóc con trốn đi đâu! Xem cú ngoạm sắt thép của tao cắn nát đầu mày đây... Ái chà chà! Cái đầu gì mà toàn gai nhọn đâm thủng cả lợi, chảy máu mồm rồi đau quá mẹ ơi! |  | Kỳ đà chú kỳ đà sa mạc khổng lồ dài 2m da hoa văn xám đen, biểu cảm kinh ngạc lè lưỡi thụt lùi hung hăng há miệng táp mạnh xuống chiếc đầu giả đầy gai nhọn; mắt trợn trừng vì gai đâm thủng mép. |
| b07 | 01:02.0–01:09.7 (7.6s) | L28 | Cú đớp chí mạng của kẻ săn mồi cắn trúng ngay bướu gai cứng như đá tảng, khiến kẻ tấn công đau đớn nhổ vội ra ngoài trong sự cay đắng tột cùng! |  | Hàm răng của kẻ săn mồi cắn ngập vào khối bướu gai cứng như đá tảng; răng nanh cắn phải đá toát tia lửa đau đớn. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này. |
| b08 | 01:09.7–01:22.9 (13.2s) | L29 | Trong khi kẻ săn mồi đang ôm miệng sưng vù la oai oái, đầu thật của Chiến Binh Gai Góc vẫn nguyên vẹn 100%, bình thản ngóc lên nhìn kẻ thù bằng ánh mắt khinh bỉ tột độ! Một pha hy sinh đầu giả cứu đầu thật ngoạn mục không đối thủ! | **100% LÀNH** · ĐẦU THẬT AN TOÀN · R/420 · [0.75, 0.52] | BÊN TRÁI kẻ săn mồi ôm mồm sưng vù vừa khóc vừa bỏ chạy; BÊN PHẢI chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh ngóc đầu thật lành lặn 100% lên nhếch mép cười đắc chí. |

### scene04 · 00 HOÀNG HÔN: QUẢ CẦU GAI PHỒNG TO VÀ DÁNG ĐI LÁ KHÔ · 92.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:12.8 (12.8s) | L30 | Mặt trời ngả về tây, đồng hồ chuyển điểm 17:00 chiều hoàng hôn! Bầu trời sa mạc chuyển sang sắc cam rực lửa đầy ma mị. Nhưng một kẻ săn mồi ranh mãnh khác lại xuất hiện: loài chó hoang Dingo hung dữ của châu Úc đang đánh hơi lần theo dấu vết của chú thằn lằn! |  | BÊN TRÁI đồng hồ điểm 17:00 hoàng hôn; BÊN PHẢI chú chó hoang chú chó hoang Dingo sa mạc lông vàng hung dữ, biểu cảm méo xệch ôm mõm vì cắn phải gai lông vàng hung hăng nhe nanh đánh hơi xuất hiện trên cồn cát cam rực. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này. |
| b02 | 00:12.8–00:16.2 (3.4s) | L31 | Nếu kẻ săn mồi cố tình nuốt trọn cả cơ thể vào bụng thì sao? |  | Chú chó chú chó hoang Dingo sa mạc lông vàng hung dữ, biểu cảm méo xệch ôm mõm vì cắn phải gai há toang mõm định nuốt trọn cả cơ thể thằn lằn vào bụng như một viên kẹo cứng. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này. |
| b03 | 00:16.2–00:26.0 (9.8s) | L32 | Chiến Binh Gai Góc lập tức tung ra chiêu phòng thủ thứ hai: Phồng to thành quả cầu gai bọc thép! Nó hít căng không khí vào hai lá phổi, ép cơ hoành phồng to lồng ngực làm kích thước cơ thể phình to gấp đôi bình thường! | **GẤP ĐÔI** · PHỒNG QUẢ CẦU GAI · L/380 · [0.28, 0.45] | chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh hít căng không khí vào phổi, phồng to cơ thể gấp đôi bình thường; biến thành quả cầu gai bọc thép tròn xoe. |
| b04 | 00:26.0–00:34.3 (8.3s) | L57 | Hàng trăm chiếc gai nhọn trên lưng vốn dĩ nằm xuôi nay dựng đứng vuông góc 90°, biến nó thành một quả cầu chông sắt gai góc không có bất kỳ khe hở nào để cắn! | **DỰNG 90°** · BỌC THÉP TOÀN THÂN · R/420 · [0.72, 0.5] | Cận cảnh hàng trăm chiếc gai nón trên lưng chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh dựng đứng vuông góc 90°; toàn bộ cơ thể trở thành khối chông sắt bất khả xâm phạm. |
| b05 | 00:34.3–00:43.2 (8.9s) | L33 | Kẻ săn mồi há miệng to định nuốt chửng nhưng cổ họng lập tức bị những chiếc gai nhọn đâm nghẹn cứng đờ, không tài nào nuốt trôi xuống dạ dày được mà phải nhè vội ra bãi cát! |  | Chú chó chú chó hoang Dingo sa mạc lông vàng hung dữ, biểu cảm méo xệch ôm mõm vì cắn phải gai bị gai nhọn chọc nghẹn cứng họng, vội vàng khạc nhè ra bãi cát, lắc đầu ngao ngán lè lưỡi bỏ chạy. |
| b06 | 00:43.2–00:49.5 (6.3s) | L58 | Và sau khi thoát hiểm, quý vị hãy chiêm ngưỡng dáng đi độc nhất vô nhị của quái kiệt này: Dáng đi lá khô đung đưa! |  | chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh thở phào xẹp bớt không khí, đứng chớp mắt tinh nghịch giữa hoàng hôn sa mạc chuẩn bị phô diễn dáng đi tàng hình độc nhất vô nhị. |
| b07 | 00:49.5–00:57.2 (7.7s) | L34 | Và nếu như cơn bão cát sa mạc khốc liệt bất ngờ nổi lên với những trận cuồng phong mù trời, quái kiệt này còn có một tuyệt chiêu đào hầm thần tốc! |  | Bão cát sa mạc ập đến với những cuồng phong cát đỏ rực; chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh đứng trước bão cát không hề sợ hãi. |
| b08 | 00:57.2–01:10.9 (13.7s) | L35 | Bốn bàn chân có móng vuốt cong sắc nhọn của nó cào cát xoay tròn như bốn chiếc máy xúc mini, chỉ mất vỏn vẹn 30 giây là toàn bộ thân hình gai góc đã lặn mất tăm dưới lòng cát đỏ sâu 10cm, bình an vô sự mặc cho bão táp gầm rú trên đầu! | **30 GIÂY** · ĐÀO HẦM THẦN TỐC · L/370 · [0.25, 0.45]<br>**SÂU 10CM** · LẶN DƯỚI LÒNG CÁT · L/470 · [0.25, 0.58] | Kỹ năng đào hầm thần tốc: 4 chân chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh cào cát xoay tít mù như máy xúc mini, trong 30 giây đã lặn mất tăm dưới lòng cát sâu 10cm tránh bão cát. |
| b09 | 01:10.9–01:18.4 (7.5s) | L36 | Nó bước một chân lên phía trước, rồi dừng lại giật cục, lắc lư thân mình tới lui 2-3 nhịp như một cành cây khô đu đưa trước gió rồi mới bước tiếp bước thứ hai! | **GIẬT CỤC** · DÁNG ĐI LÁ KHÔ · R/400 · [0.75, 0.5] | Vũ điệu robot lá khô: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh bước 1 chân rồi giật cục lắc lư người 2-3 nhịp như cành cây khô trước gió, làm chim săn mồi mất dấu thị giác. |
| b10 | 01:18.4–01:32.7 (14.3s) | L37 | Dáng đi robot giật cục này hòa lẫn hoàn hảo vào chuyển động của cỏ cây sa mạc, làm hệ thống thị giác bắt chuyển động của chim săn mồi hoàn toàn bị mất dấu mục tiêu! Vừa bọc thép gai góc, vừa biết tàng hình bằng vũ điệu giật cục, đúng là bậc thầy phòng thủ số một thiên nhiên! |  | Tầm nhìn từ trên cao của chim săn mồi: hình ảnh chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh nhấp nhô hòa tan vào chuyển động của bụi cỏ khô sa mạc, biến mất khỏi radar thị giác. |

### scene05 · 00 ĐÊM: ĐỔI MÀU ĐIỀU HÒA NHIỆT ĐỘ GIỮA SA MẠC LẠNH BUỐT · 86.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.4 (10.4s) | L38 | Màn đêm sa mạc buông xuống, đồng hồ điểm 21:00 đêm! Cát sa mạc tỏa nhiệt cực nhanh khiến nhiệt độ tụt dốc không phanh từ 45°C ban ngày rơi thẳng xuống dưới 10°C lạnh buốt xương tủy! | **< 10°C** · ĐÊM LẠNH THẤU XƯƠNG · L/390 · [0.28, 0.48] | BÊN TRÁI đồng hồ điểm 21:00 đêm; Ở GIỮA cát sa mạc tỏa nhiệt cực nhanh; BÊN PHẢI nhiệt kế tụt dốc thê thảm xuống dưới 10°C lạnh giá. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này. |
| b02 | 00:10.4–00:17.2 (6.8s) | L59 | Giữa sự khắc nghiệt điên rồ ấy, Chiến Binh Gai Góc lại tiếp tục biểu diễn tuyệt kỹ thứ ba: Biến hóa màu sắc như tắc kè hoa! |  | chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh đứng trên mỏm đá đêm sa mạc, cơ thể bắt đầu biến đổi màu sắc kỳ ảo như một chú tắc kè hoa thông minh. |
| b03 | 00:17.2–00:31.7 (14.4s) | L39 | Vào buổi trưa nắng cháy, làn da của nó chuyển sang màu vàng cát nhạt hoặc xám sáng để phản xạ tối đa ánh sáng mặt trời, giúp cơ thể không bị sốc nhiệt nấu chín. Nhưng khi đêm lạnh tràn về, các tế bào sắc tố dưới da lập tức giãn nở, đổi màu toàn bộ cơ thể sang màu nâu sẫm, xám đen và đất đỏ thẫm! |  | So sánh hai màu áo giáp của chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh: BÊN TRÁI màu vàng cát nhạt phản xạ nhiệt trưa hè; BÊN PHẢI màu nâu xám sẫm hấp thụ nhiệt đêm lạnh. |
| b04 | 00:31.7–00:38.3 (6.7s) | L40 | Màu da đen tối này giúp nó hấp thụ từng tia nhiệt lượng tàn dư cuối cùng của mặt đất, giữ ấm cho các cơ quan nội tạng suốt đêm dài. |  | chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh ngụy trang thành một hòn đá vô tri giữa bãi cát đỏ sa mạc Red Centre; hấp thụ từng tia nhiệt lượng tàn dư giữ ấm cơ thể. |
| b05 | 00:38.3–00:47.4 (9.0s) | L60 | Đồng thời, màu sắc đất đỏ này ngụy trang nó hòa lẫn hoàn hảo vào màu cát sa mạc Red Centre nước Úc, khiến những con cú đêm hay rắn độc bò ngang qua cũng chỉ nhìn thấy một cục đá vô tri vô giác! |  | Bóng đêm sa mạc bao trùm: một con cú đêm bay lượn sát mặt đất nhưng không tài nào phát hiện ra chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh đang ẩn mình như tảng đá sa mạc. |
| b06 | 00:47.4–01:01.1 (13.8s) | L41 | Đặc biệt vào những tháng mùa đông băng giá của sa mạc miền Trung nước Úc, Thằn Lằn Quỷ Gai sẽ bước vào trạng thái ngủ đông đặc biệt. Toàn bộ quá trình trao đổi chất của nó giảm xuống mức tối thiểu, nhịp tim đập chậm lại chỉ còn vài nhịp mỗi phút để tiết kiệm từng giọt năng lượng quý giá! | **NGỦ ĐÔNG** · NHỊP TIM TỐI THIỂU · R/390 · [0.75, 0.48] | Trạng thái ngủ đông sa mạc: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh nằm cuộn tròn dưới hang cát ấm áp, nhịp tim giảm xuống chỉ còn vài nhịp mỗi phút tiết kiệm năng lượng. |
| b07 | 01:01.1–01:08.8 (7.7s) | L42 | Nó nằm bất động dưới lòng đất cát, kiên nhẫn chờ đợi cho đến khi ánh nắng xuân ấm áp đánh thức nó bước vào một chu kỳ sinh tồn mới rực rỡ! |  | Chú thằn lằn bình yên ngủ say dưới lòng đất cát, bên trên là ánh trăng bạc rọi xuống cồn cát sa mạc tĩnh mịch huyền ảo. |
| b08 | 01:08.8–01:16.9 (8.1s) | L43 | Và quý vị có biết nhiều người từng đồn thổi loài này có tài bắn máu từ mắt không? Khoa học xin đính chính: bắn máu từ mắt là vũ khí của thằn lằn sừng châu Mỹ; |  | Thằn lằn sừng Bắc Mỹ bắn tia máu đỏ rực từ khóe mắt xua đuổi chó sói; một bức tranh tư liệu so sánh sinh động. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này. |
| b09 | 01:16.9–01:26.0 (9.1s) | L61 | còn Thằn Lằn Quỷ Gai nước Úc hoàn toàn không cần bắn máu, vì bộ giáp gai thép và chiếc đầu giả của nó đã quá đủ để khiến mọi kẻ săn mồi phải bỏ chạy mất dép rồi! |  | chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh cười tươi vỗ ngực tự hào khẳng định: 'Thằn Lằn Quỷ Gai Úc tôi có giáp gai thép và đầu giả là đủ bá chủ sa mạc rồi!'. |

### scene06 · 00 RẠNG SÁNG: BẢN LĨNH SINH TỒN ĐỈNH CAO VÀ BÓNG ĐEN TẬP 20 · 81.1s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.2 (8.2s) | L44 | Đồng hồ điểm 03:00 rạng sáng! Những luồng gió buốt lạnh thổi qua cồn cát hoang vu, khép lại 24 giờ tác nghiệp nghẹt thở theo chân Chiến Binh Gai Góc. |  | BÊN TRÁI đồng hồ điểm 03:00 rạng sáng; Ở GIỮA cồn cát lộng gió lạnh buốt; BÊN PHẢI phóng viên truyền hình 24h mặc áo gile thám hiểm nhiều túi, tay cầm micro có logo '24H WILD' đang đứng tác nghiệp những phút cuối. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này. |
| b02 | 00:08.2–00:17.0 (8.8s) | L62 | Một sinh vật nhỏ bé không có nanh nhọn, không có nọc độc, chạy chậm như rùa nhưng đã kiên cường ngự trị giữa sa mạc khô cằn khắc nghiệt nhất hành tinh qua hàng triệu năm lịch sử! |  | Chân dung kiên cường của chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh: một chú thằn lằn nhỏ bé nhưng ngự trị sa mạc khắc nghiệt nhất hành tinh suốt hàng triệu năm qua. |
| b03 | 00:17.0–00:30.3 (13.3s) | L45 | Biến làn da thành rãnh hút nước, biến đầu giả thành bia đỡ đạn, biết cuộn tròn phòng thủ và kiên nhẫn với con đường của riêng mình, đó chính là bài học sinh tồn vĩ đại mà tự nhiên ban tặng cho chúng ta! Chậm chạp nhưng không hề yếu đuối, gai góc để tự vệ chứ không hại ai! |  | Bức tranh tôn vinh bản lĩnh tự nhiên: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh đứng kiêu hãnh trên đỉnh cồn cát, biểu tượng cho sức sống kiên cường qua hàng triệu năm lịch sử. |
| b04 | 00:30.3–00:44.0 (13.7s) | L46 | Hành trình 24 giờ cùng Thằn Lằn Quỷ Gai đã chính thức khép lại! Nhưng ngay lúc này, xin mời toàn thể quý vị khán giả hãy hướng mắt lên màn hình lớn để giải mã BÓNG ĐEN BÍ ẨN của nhân vật xuất hiện trong Tập 20 cột mốc tiếp theo! |  | Màn hình chiếu khổng lồ ở trung tâm sân khấu bật sáng với ánh hào quang nước màu xanh ngọc bích lung linh huyền ảo. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này. |
| b05 | 00:44.0–00:54.9 (10.8s) | L47 | Xin gửi tới quý vị ba manh mối chấn động về bóng đen bí ẩn này: Thứ nhất, đây là siêu xạ thủ bắn tỉa thiên tài bậc nhất thế giới loài cá, sở hữu tuyệt chiêu nén tia nước bắn hạ con mồi đang đậu trên cành cây cao cách xa tới 3m! | **BÓNG ĐEN** · QUÁI KIỆT TẬP 20 · R/360 · [0.75, 0.42]<br>**BẮN XA 3M** · TIA NƯỚC NÉN CAO · L/420 · [0.25, 0.5] | Manh mối số 1: BÓNG ĐEN BÍ ẨN (solid black silhouette) của một chú cá đang ngắm bắn tỉa tia nước nén cực mạnh hạ gục con mồi cách xa 3m kèm dấu hỏi '?'. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này. |
| b06 | 00:54.9–01:08.8 (13.9s) | L48 | Thứ hai, bộ não thiên tài có khả năng tự động tính toán độ lệch khúc xạ ánh sáng giữa nước và không khí chính xác đến từng mi-li-mét! Và thứ ba, khẩu đại bác nước nén trong rãnh vòm miệng với áp lực nước cực mạnh làm rách toạc cánh côn trùng rơi tõm xuống nước làm mồi! Quý vị | **ĐẠI BÁC** · TÍNH TOÁN KHÚC XẠ · R/390 · [0.75, 0.48] | Manh mối số 2 & 3: Tia khúc xạ ánh sáng qua mặt nước được bộ não tính toán chính xác; rãnh vòm miệng nén nước xé toạc cánh côn trùng. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này. |
| b07 | 01:08.8–01:16.9 (8.1s) | L49 | khán giả có nhận ra bóng đen xạ thủ bắn tỉa dưới nước này là loài cá nào không? Hãy để lại phán quyết và dự đoán của bạn ngay dưới phần bình luận nhé! |  | BÓNG ĐEN BÍ ẨN dưới mặt nước với dấu hỏi chấm '?' nhấp nháy phát sáng; xung quanh là các bong bóng bình luận '? ? ?' kêu gọi khán giả dự đoán. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này. |
| b08 | 01:16.9–01:21.1 (4.3s) | L50 | Phóng viên sinh tồn 24 giờ xin chào tạm biệt và hẹn gặp lại quý vị trong tập tiếp theo! |  | BÊN TRÁI phóng viên truyền hình 24h mặc áo gile thám hiểm nhiều túi, tay cầm micro có logo '24H WILD' và chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh vẫy tay chào tạm biệt; BÊN PHẢI tấm biển gỗ đề chữ 'HẸN GẶP LẠI Ở TẬP 20 VỚI SIÊU XẠ THỦ BẮN TỈA DƯỚI NƯỚ |

## 5. Phân cảnh Shorts — từng beat

Banner: **UỐNG NƯỚC BẰNG CHÂN?! / QUÁI KIỆT SA MẠC ÚC** · giọng 49.0s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | 05:00 sáng giữa sa mạc Úc cháy bỏng! |  |
| s02 | 00:03.0 | S02 | Một sinh vật không cần cúi đầu mà vẫn có thể uống nước ngọt lành chỉ bằng cách dẫm bàn chân lên cát ẩm! |  |
| s03 | 00:08.7 | S03 | Đó chính là Thằn Lằn Quỷ Gai, quái kiệt bọc thép dài 20cm của lục địa nắng cháy. | **DÀI 20CM** · XE TĂNG SA MẠC · L/620 · [0.5, 0.45] |
| s04 | 00:13.7 | S04 | Làn da của nó phủ đầy mạng lưới rãnh mao dẫn siêu nhỏ, | **MAO DẪN** · RÃNH HÚT NƯỚC · R/640 · [0.55, 0.48] |
| s05 | 00:16.8 | S11 | tự động hút từng giọt sương mai từ bàn chân chảy ngược chiều trọng lực dọc theo sống lưng chạy thẳng vào miệng! |  |
| s06 | 00:22.8 | S05 | Mỗi ngày, nó kiên nhẫn nuốt chửng tới 2.500 con kiến đen độc hại bằng chiếc lưỡi dính siêu tốc. | **2.500 CON** · ĐẠI TIỆC KIẾN ĐEN · L/630 · [0.5, 0.46] |
| s07 | 00:28.5 | S06 | Khi bị kẻ săn mồi tấn công, nó cúi gục đầu thật xuống đất và chìa chiếc bướu gai đầu giả sắc nhọn sau gáy ra | **ĐẦU GIẢ** · LỪA KẺ SĂN MỒI · R/650 · [0.55, 0.5] |
| s08 | 00:34.6 | S07 | ngoài lừa kẻ thù cắn rách mồm! |  |
| s09 | 00:36.5 | S08 | Chưa hết, nó còn có thể hít khí phồng to cơ thể gấp đôi thành quả cầu gai bọc thép không kẻ nào nuốt | **GẤP ĐÔI** · QUẢ CẦU GAI BỌC THÉP · L/640 · [0.5, 0.48] |
| s10 | 00:41.6 | S09 | trôi! Vậy là bí mật đã sáng tỏ: một cỗ xe tăng tí hon với bản lĩnh sinh tồn đỉnh |  |
| s11 | 00:46.4 | S10 | cao ngự trị chảo lửa sa mạc suốt hàng triệu năm qua! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bíp bíp bíp! Đồng hồ điểm 05:00 sáng!". Bố cục: Toàn cảnh sa mạc Red Centre nước Úc lúc bình minh: BÊN TRÁI phóng viên truyền hình 24h mặc áo gile thám hiểm nhiều túi, tay cầm micro có logo '24H WILD' cầm micro phát sóng trực tiếp; Ở GIỮA đồng hồ cát khổng lồ hiện số 05:00 sáng; BÊN PHẢI những cồn cát đỏ rực trải dài vô tận. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phóng viên truyền hình sinh tồn 24 giờ xin kính chào toàn thể quý vị khán giả! Ngay lúc này, tôi đang có mặt trực tiếp tại chảo lửa sa mạc đỏ rực miền Trung nước Úc, nơi nhiệt độ có thể chênh lệch kinh hoàng từ lạnh thấu xương lúc rạng đông lên tới 45°C khi mặt trời lên đỉnh đầu!". Bố cục: Nhiệt kế đo nhiệt độ sa mạc: cột nhiệt độ chỉ mức lạnh thấu xương lúc sáng sớm và mũi tên đỏ chỉ mức vọt lên 45°C lúc giữa trưa gay gắt. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trước mắt chúng ta là một sinh vật có diện mạo kỳ quái và gai góc bậc nhất thế giới tự nhiên!". Bố cục: Cận cảnh xuất hiện của chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh: toàn thân bọc kín hàng trăm chiếc gai nón nhọn hoắt như cỗ xe bọc thép thời cổ, chiếc mũ safari kaki đội ngay ngắn, nơ đỏ nổi bật trên cổ.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thân hình chỉ dài vỏn vẹn 20cm nhưng từ đầu đến đuôi phủ kín hàng trăm chiếc gai nón sắc nhọn như một cỗ xe bọc thép thời Trung cổ!". Bố cục: Thước đo so sánh: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh dài vỏn vẹn 20cm đứng cạnh bàn chân người; toàn thân bao bọc bởi lớp gai nhọn xù xì đe dọa.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giáo sư ơi! Giữa biển cát khô cằn không có lấy một vũng nước thế này, chú thằn lằn này làm sao giải khát để sống sót ạ?". Bố cục: Khán giả nhí hoạt hình ngơ ngác nhìn quanh cồn cát khô cằn nứt nẻ không một giọt nước, cầm chiếc bình nước rỗng tuếch lắc lắc tuyệt vọng. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khán giả nhí vừa hỏi đúng bí mật chấn động nhất của tạo hóa! Hãy nhìn chiếc camera quay siêu chậm của chúng tôi: Chiến Binh Gai Góc không hề cúi đầu tìm nước, mà nó chỉ việc thong thả bước bốn bàn chân lên nền cát còn hơi ẩm sương đêm!". Bố cục: Camera quay siêu chậm: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh thong thả đặt 4 bàn chân lên lớp cát ẩm sương mai; các hạt sương đọng lấp lánh quanh móng chân sắc nhọn.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn bộ bề mặt da của Thằn Lằn Quỷ Gai là một mạng lưới các rãnh vi mao dẫn siêu hiển vi đan xen chằng chịt giữa các vảy gai.". Bố cục: Kính hiển vi phóng đại da chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh: mạng lưới rãnh mao dẫn siêu hiển vi đan xen như mạng lưới kênh rạch thủy lợi giữa các chân gai nhọn phát sáng xanh lam.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Theo định luật mao dẫn vật lý, các rãnh này tự động tạo ra một lực hút cực mạnh, hút từng giọt nước sương từ cát ẩm chảy ngược chiều trọng lực!". Bố cục: Mô phỏng lực mao dẫn vật lý: các giọt nước sương từ hạt cát ẩm tự động bị hút ngược chiều trọng lực, chảy thành dòng nước tí hon dọc cẳng chân và bụng.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nước chảy từ móng chân, men theo cẳng chân, chạy dọc bờ bụng, leo qua sống lưng và hội tụ thẳng tắp về hai khóe miệng của nó!". Bố cục: Sơ đồ dòng chảy trên cơ thể chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh: các mũi tên nước màu xanh dương chạy dọc từ 4 chân, leo qua bờ bụng, vượt sống lưng và đổ thẳng về hai khóe miệng.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà vật lý học thuộc Viện nghiên cứu Đức khi đưa lớp da của Thằn Lằn Quỷ Gai vào kính hiển vi điện tử quét đã phải sửng sốt:". Bố cục: Phòng thí nghiệm Viện nghiên cứu Đức: các nhà khoa học đang phân tích lớp da thằn lằn quỷ gai trên màn hình kính hiển vi điện tử quét SEM. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không cần bất kỳ một chiếc máy bơm cơ học hay trái tim co bóp, lực hút liên kết phân tử của nước tự kéo nhau chạy thẳng vào khoang miệng một cách kỳ diệu!". Bố cục: Hình ảnh so sánh: một bên chiếc máy bơm cơ học bị gạch chéo đỏ; một bên là giọt nước tự động kết nối kéo nhau chạy trên da chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh kỳ diệu.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chú thằn lằn chỉ việc đứng yên một chỗ, nhấp nháy hàm dưới nhịp nhàng như đang thưởng thức cà phê sáng, thế là nước sạch tự động chảy tọt vào họng mà không cần tốn một giọt mồ hôi!". Bố cục: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh đứng thong dong chớp mắt, hai hàm nhấp nháy nhịp nhàng như đang thưởng thức ly nước mát lạnh; nước sạch tự động chảy tọt vào họng sảng khoái.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thậm chí nếu bạn nhỏ một giọt nước lên lưng nó, giọt nước ấy cũng tự động chia làn chảy ngược về miệng trong vòng vài giây! Một nhà máy lọc và hút nước tự động gắn liền trên da đỉnh cao đến mức các kỹ sư công nghệ vũ trụ NASA cũng phải ngả mũ bái phục!". Bố cục: Thí nghiệm nhỏ giọt nước: một giọt nước rơi trúng lưng chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh, giọt nước lập tức phân nhánh chảy men theo các rãnh gai lao thẳng về miệng trong tích tắc.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đồng hồ điểm 09:00 sáng! Mặt trời sa mạc bắt đầu nhô cao, nhiệt độ không khí tăng vọt lên 35°C. Uống đẫm nước xong xuôi, chiếc dạ dày của Chiến Binh Gai Góc bắt đầu réo vang ùng ục, báo hiệu đã đến giờ ăn sáng!". Bố cục: BÊN TRÁI đồng hồ chuyển sang mốc 09:00 sáng; Ở GIỮA ánh mặt trời bắt đầu gay gắt 35°C; BÊN PHẢI chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh bụng kêu 'ùng ục' xoa bụng đói meo hài hước.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng quý vị có biết thực đơn của quái kiệt này gồm những món gì không? Rất giản dị nhưng cực kỳ khó nuốt: 100% khẩu phần ăn cả đời của nó chỉ là loài kiến đen nhỏ mang tên Iridomyrmex — loài kiến chứa đầy a-xít phoóc-mích độc hại và mùi hôi nồng nặc mà mọi loài động vật khác đều phải lắc đầu né xa!". Bố cục: Thực đơn sa mạc đặc biệt: 100% là loài kiến đen Iridomyrmex chứa đầy a-xít phoóc-mích; một con kiến đen hung hăng giơ hai càng đe dọa. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiến Binh Gai Góc lạch bạch bò đến bên cạnh một đường mòn kiến chạy qua bãi cát. Nó ngồi xổm xuống một cách cực kỳ kiên nhẫn hệt như một ông cụ ngồi câu cá bên bờ sông.". Bố cục: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh ngồi xổm bất động bên cạnh đường mòn kiến đen chạy qua bãi cát, kiên nhẫn như ông cụ ngồi câu cá bên hồ.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và ngay khi đàn kiến hành quân ngang qua, vũ khí bí mật được kích hoạt: chẹp, chẹp, chẹp!". Bố cục: Đàn kiến đen nối đuôi nhau hành quân trên nền cát đỏ; bóng lưng chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh khổng lồ phủ bóng xuống như ngọn núi phục kích.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiếc lưỡi dày phủ đầy chất nhầy siêu dính của nó phóng ra với tốc độ tên lửa, trong 1 giây có thể thò ra thụt vào tới hai đến 3 lần!". Bố cục: Tốc độ săn mồi chớp nhoáng: chiếc lưỡi dính màu hồng của chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh phóng ra như tia chớp, 1 giây thò thụt 2-3 lần tóm gọn từng chú kiến đen.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ối cứu bọn em với! Bác này bác ấy ngồi ngay cửa hang, bác ấy lia lưỡi một cái là mất tích cả trung đội kiến nhà em rồi cà nhà ơi!". Bố cục: Cảnh tượng bi hài: cả trung đội kiến đen hoảng loạn tháo chạy tán loạn khi chiếc lưỡi khổng lồ của chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh quét sạch cả hàng ngũ. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quý vị thử nghĩ mà xem: a-xít phoóc-mích của kiến đen có thể làm bỏng rát da người và giết chết nhiều loài thú nhỏ,". Bố cục: Bình hóa chất a-xít phoóc-mích bốc khói độc hại; so sánh bên cạnh là các loài thú nhỏ sợ hãi lùi xa né tránh đàn kiến đen. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thậm chí chiếc đuôi của nó còn đóng vai trò như một kho dự trữ mỡ khổng lồ, tích tụ năng lượng từ đống protein kiến để giúp chú thằn lằn nhịn ăn nhiều tháng liền khi mùa khô hạn ập đến!". Bố cục: Chiếc đuôi mập mạp của chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh phình to chứa các hạt mỡ năng lượng vàng óng; biểu tượng bình ắc-quy tích lũy năng lượng cho mùa hạn hán.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tiếng kêu cứu thất thanh của bầy kiến hoàn toàn bất lực trước máy hút bụi sinh học này!". Bố cục: Bầy kiến đen hoảng loạn tháo chạy bất lực trước máy hút bụi sinh học của chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đồng hồ điểm 13:00 trưa! Ánh nắng sa mạc như trút lửa xuống mặt đất, nhiệt độ bề mặt cát đo được đã vượt ngưỡng 50°C! Giữa lúc không khí ngột ngạt đến nghẹt thở, hiểm nguy từ những kẻ săn mồi khát máu bắt đầu ập tới!". Bố cục: BÊN TRÁI đồng hồ điểm mốc 13:00 trưa; Ở GIỮA mặt cát bốc hơi nóng hầm hập vượt 50°C; BÊN PHẢI phóng viên truyền hình 24h mặc áo gile thám hiểm nhiều túi, tay cầm micro có logo '24H WILD' lau mồ hôi nhễ nhại cảnh báo nguy hiểm. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trên bầu trời rực nắng, loài chim săn mồi mắt tinh như dao cạo đang lượn vòng;". Bố cục: Bầu trời rực nắng chói chang: loài chim ưng săn mồi mắt sắc như dao cạo đang dang rộng cánh lượn vòng tìm kiếm con mồi. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiến Binh Gai Góc lập tức kích hoạt tuyệt chiêu đánh lừa thị giác đỉnh cao: Chiếc Đầu Giả Bằng Gai! Quý vị hãy nhìn kỹ vào sau gáy của nó: có một bướu thịt lớn mọc nhô cao với hai chiếc gai sừng to tướng trông y hệt như một chiếc đầu thứ hai!". Bố cục: Cận cảnh sau gáy chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh: chiếc bướu gai thịt nhô cao với hai chiếc gai sừng to tướng trông y hệt một chiếc đầu thứ hai đầy uy hiếp.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi kẻ địch lao vào tấn công, chú thằn lằn lập tức cúi gục chiếc đầu thật chứa não và mắt giấu kín vào giữa hai chân trước, áp sát mặt xuống đất! Đồng thời, nó ngóc chiếc đầu giả đầy gai nhọn hoắt nhô cao lên không trung để mời gọi kẻ thù cắn vào!". Bố cục: Tuyệt kỹ cúi đầu: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh giấu đầu thật kín mít vào giữa hai chân trước áp sát đất; đồng thời ngóc chiếc đầu giả đầy gai nhọn lên cao làm mồi nhử.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thằng nhóc con trốn đi đâu! Xem cú ngoạm sắt thép của tao cắn nát đầu mày đây... Ái chà chà! Cái đầu gì mà toàn gai nhọn đâm thủng cả lợi, chảy máu mồm rồi đau quá mẹ ơi!". Bố cục: Kỳ đà chú kỳ đà sa mạc khổng lồ dài 2m da hoa văn xám đen, biểu cảm kinh ngạc lè lưỡi thụt lùi hung hăng há miệng táp mạnh xuống chiếc đầu giả đầy gai nhọn; mắt trợn trừng vì gai đâm thủng mép.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cú đớp chí mạng của kẻ săn mồi cắn trúng ngay bướu gai cứng như đá tảng, khiến kẻ tấn công đau đớn nhổ vội ra ngoài trong sự cay đắng tột cùng!". Bố cục: Hàm răng của kẻ săn mồi cắn ngập vào khối bướu gai cứng như đá tảng; răng nanh cắn phải đá toát tia lửa đau đớn. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong khi kẻ săn mồi đang ôm miệng sưng vù la oai oái, đầu thật của Chiến Binh Gai Góc vẫn nguyên vẹn 100%, bình thản ngóc lên nhìn kẻ thù bằng ánh mắt khinh bỉ tột độ! Một pha hy sinh đầu giả cứu đầu thật ngoạn mục không đối thủ!". Bố cục: BÊN TRÁI kẻ săn mồi ôm mồm sưng vù vừa khóc vừa bỏ chạy; BÊN PHẢI chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh ngóc đầu thật lành lặn 100% lên nhếch mép cười đắc chí.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mặt trời ngả về tây, đồng hồ chuyển điểm 17:00 chiều hoàng hôn! Bầu trời sa mạc chuyển sang sắc cam rực lửa đầy ma mị. Nhưng một kẻ săn mồi ranh mãnh khác lại xuất hiện: loài chó hoang Dingo hung dữ của châu Úc đang đánh hơi lần theo dấu vết của chú thằn lằn!". Bố cục: BÊN TRÁI đồng hồ điểm 17:00 hoàng hôn; BÊN PHẢI chú chó hoang chú chó hoang Dingo sa mạc lông vàng hung dữ, biểu cảm méo xệch ôm mõm vì cắn phải gai lông vàng hung hăng nhe nanh đánh hơi xuất hiện trên cồn cát cam rực. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu kẻ săn mồi cố tình nuốt trọn cả cơ thể vào bụng thì sao?". Bố cục: Chú chó chú chó hoang Dingo sa mạc lông vàng hung dữ, biểu cảm méo xệch ôm mõm vì cắn phải gai há toang mõm định nuốt trọn cả cơ thể thằn lằn vào bụng như một viên kẹo cứng. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiến Binh Gai Góc lập tức tung ra chiêu phòng thủ thứ hai: Phồng to thành quả cầu gai bọc thép! Nó hít căng không khí vào hai lá phổi, ép cơ hoành phồng to lồng ngực làm kích thước cơ thể phình to gấp đôi bình thường!". Bố cục: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh hít căng không khí vào phổi, phồng to cơ thể gấp đôi bình thường; biến thành quả cầu gai bọc thép tròn xoe.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kẻ săn mồi há miệng to định nuốt chửng nhưng cổ họng lập tức bị những chiếc gai nhọn đâm nghẹn cứng đờ, không tài nào nuốt trôi xuống dạ dày được mà phải nhè vội ra bãi cát!". Bố cục: Chú chó chú chó hoang Dingo sa mạc lông vàng hung dữ, biểu cảm méo xệch ôm mõm vì cắn phải gai bị gai nhọn chọc nghẹn cứng họng, vội vàng khạc nhè ra bãi cát, lắc đầu ngao ngán lè lưỡi bỏ chạy.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và nếu như cơn bão cát sa mạc khốc liệt bất ngờ nổi lên với những trận cuồng phong mù trời, quái kiệt này còn có một tuyệt chiêu đào hầm thần tốc!". Bố cục: Bão cát sa mạc ập đến với những cuồng phong cát đỏ rực; chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh đứng trước bão cát không hề sợ hãi.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bốn bàn chân có móng vuốt cong sắc nhọn của nó cào cát xoay tròn như bốn chiếc máy xúc mini, chỉ mất vỏn vẹn 30 giây là toàn bộ thân hình gai góc đã lặn mất tăm dưới lòng cát đỏ sâu 10cm, bình an vô sự mặc cho bão táp gầm rú trên đầu!". Bố cục: Kỹ năng đào hầm thần tốc: 4 chân chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh cào cát xoay tít mù như máy xúc mini, trong 30 giây đã lặn mất tăm dưới lòng cát sâu 10cm tránh bão cát.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó bước một chân lên phía trước, rồi dừng lại giật cục, lắc lư thân mình tới lui 2-3 nhịp như một cành cây khô đu đưa trước gió rồi mới bước tiếp bước thứ hai!". Bố cục: Vũ điệu robot lá khô: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh bước 1 chân rồi giật cục lắc lư người 2-3 nhịp như cành cây khô trước gió, làm chim săn mồi mất dấu thị giác.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dáng đi robot giật cục này hòa lẫn hoàn hảo vào chuyển động của cỏ cây sa mạc, làm hệ thống thị giác bắt chuyển động của chim săn mồi hoàn toàn bị mất dấu mục tiêu! Vừa bọc thép gai góc, vừa biết tàng hình bằng vũ điệu giật cục, đúng là bậc thầy phòng thủ số một thiên nhiên!". Bố cục: Tầm nhìn từ trên cao của chim săn mồi: hình ảnh chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh nhấp nhô hòa tan vào chuyển động của bụi cỏ khô sa mạc, biến mất khỏi radar thị giác.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Màn đêm sa mạc buông xuống, đồng hồ điểm 21:00 đêm! Cát sa mạc tỏa nhiệt cực nhanh khiến nhiệt độ tụt dốc không phanh từ 45°C ban ngày rơi thẳng xuống dưới 10°C lạnh buốt xương tủy!". Bố cục: BÊN TRÁI đồng hồ điểm 21:00 đêm; Ở GIỮA cát sa mạc tỏa nhiệt cực nhanh; BÊN PHẢI nhiệt kế tụt dốc thê thảm xuống dưới 10°C lạnh giá. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vào buổi trưa nắng cháy, làn da của nó chuyển sang màu vàng cát nhạt hoặc xám sáng để phản xạ tối đa ánh sáng mặt trời, giúp cơ thể không bị sốc nhiệt nấu chín. Nhưng khi đêm lạnh tràn về, các tế bào sắc tố dưới da lập tức giãn nở, đổi màu toàn bộ cơ thể sang màu nâu sẫm, xám đen và đất đỏ thẫm!". Bố cục: So sánh hai màu áo giáp của chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh: BÊN TRÁI màu vàng cát nhạt phản xạ nhiệt trưa hè; BÊN PHẢI màu nâu xám sẫm hấp thụ nhiệt đêm lạnh.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Màu da đen tối này giúp nó hấp thụ từng tia nhiệt lượng tàn dư cuối cùng của mặt đất, giữ ấm cho các cơ quan nội tạng suốt đêm dài.". Bố cục: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh ngụy trang thành một hòn đá vô tri giữa bãi cát đỏ sa mạc Red Centre; hấp thụ từng tia nhiệt lượng tàn dư giữ ấm cơ thể.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc biệt vào những tháng mùa đông băng giá của sa mạc miền Trung nước Úc, Thằn Lằn Quỷ Gai sẽ bước vào trạng thái ngủ đông đặc biệt. Toàn bộ quá trình trao đổi chất của nó giảm xuống mức tối thiểu, nhịp tim đập chậm lại chỉ còn vài nhịp mỗi phút để tiết kiệm từng giọt năng lượng quý giá!". Bố cục: Trạng thái ngủ đông sa mạc: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh nằm cuộn tròn dưới hang cát ấm áp, nhịp tim giảm xuống chỉ còn vài nhịp mỗi phút tiết kiệm năng lượng.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó nằm bất động dưới lòng đất cát, kiên nhẫn chờ đợi cho đến khi ánh nắng xuân ấm áp đánh thức nó bước vào một chu kỳ sinh tồn mới rực rỡ!". Bố cục: Chú thằn lằn bình yên ngủ say dưới lòng đất cát, bên trên là ánh trăng bạc rọi xuống cồn cát sa mạc tĩnh mịch huyền ảo.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và quý vị có biết nhiều người từng đồn thổi loài này có tài bắn máu từ mắt không? Khoa học xin đính chính: bắn máu từ mắt là vũ khí của thằn lằn sừng châu Mỹ;". Bố cục: Thằn lằn sừng Bắc Mỹ bắn tia máu đỏ rực từ khóe mắt xua đuổi chó sói; một bức tranh tư liệu so sánh sinh động. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đồng hồ điểm 03:00 rạng sáng! Những luồng gió buốt lạnh thổi qua cồn cát hoang vu, khép lại 24 giờ tác nghiệp nghẹt thở theo chân Chiến Binh Gai Góc.". Bố cục: BÊN TRÁI đồng hồ điểm 03:00 rạng sáng; Ở GIỮA cồn cát lộng gió lạnh buốt; BÊN PHẢI phóng viên truyền hình 24h mặc áo gile thám hiểm nhiều túi, tay cầm micro có logo '24H WILD' đang đứng tác nghiệp những phút cuối. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Biến làn da thành rãnh hút nước, biến đầu giả thành bia đỡ đạn, biết cuộn tròn phòng thủ và kiên nhẫn với con đường của riêng mình, đó chính là bài học sinh tồn vĩ đại mà tự nhiên ban tặng cho chúng ta! Chậm chạp nhưng không hề yếu đuối, gai góc để tự vệ chứ không hại ai!". Bố cục: Bức tranh tôn vinh bản lĩnh tự nhiên: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh đứng kiêu hãnh trên đỉnh cồn cát, biểu tượng cho sức sống kiên cường qua hàng triệu năm lịch sử.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hành trình 24 giờ cùng Thằn Lằn Quỷ Gai đã chính thức khép lại! Nhưng ngay lúc này, xin mời toàn thể quý vị khán giả hãy hướng mắt lên màn hình lớn để giải mã BÓNG ĐEN BÍ ẨN của nhân vật xuất hiện trong Tập 20 cột mốc tiếp theo!". Bố cục: Màn hình chiếu khổng lồ ở trung tâm sân khấu bật sáng với ánh hào quang nước màu xanh ngọc bích lung linh huyền ảo. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Xin gửi tới quý vị ba manh mối chấn động về bóng đen bí ẩn này: Thứ nhất, đây là siêu xạ thủ bắn tỉa thiên tài bậc nhất thế giới loài cá, sở hữu tuyệt chiêu nén tia nước bắn hạ con mồi đang đậu trên cành cây cao cách xa tới 3m!". Bố cục: Manh mối số 1: BÓNG ĐEN BÍ ẨN (solid black silhouette) của một chú cá đang ngắm bắn tỉa tia nước nén cực mạnh hạ gục con mồi cách xa 3m kèm dấu hỏi '?'. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thứ hai, bộ não thiên tài có khả năng tự động tính toán độ lệch khúc xạ ánh sáng giữa nước và không khí chính xác đến từng mi-li-mét! Và thứ ba, khẩu đại bác nước nén trong rãnh vòm miệng với áp lực nước cực mạnh làm rách toạc cánh côn trùng rơi tõm xuống nước làm mồi! Quý vị khán giả". Bố cục: Manh mối số 2 & 3: Tia khúc xạ ánh sáng qua mặt nước được bộ não tính toán chính xác; rãnh vòm miệng nén nước xé toạc cánh côn trùng. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "có nhận ra bóng đen xạ thủ bắn tỉa dưới nước này là loài cá nào không? Hãy để lại phán quyết và dự đoán của bạn ngay dưới phần bình luận nhé!". Bố cục: BÓNG ĐEN BÍ ẨN dưới mặt nước với dấu hỏi chấm '?' nhấp nháy phát sáng; xung quanh là các bong bóng bình luận '? ? ?' kêu gọi khán giả dự đoán. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phóng viên sinh tồn 24 giờ xin chào tạm biệt và hẹn gặp lại quý vị trong tập tiếp theo!". Bố cục: BÊN TRÁI phóng viên truyền hình 24h mặc áo gile thám hiểm nhiều túi, tay cầm micro có logo '24H WILD' và chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh vẫy tay chào tạm biệt; BÊN PHẢI tấm biển gỗ đề chữ 'HẸN GẶP LẠI Ở TẬP 20 VỚI SIÊU XẠ THỦ BẮN TỈA DƯỚI NƯỚC!'. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Xin trân trọng giới thiệu: Thằn Lằn Quỷ Gai — quái kiệt sa mạc được giới khoa học mệnh danh bằng cái tên kiêu hãnh: Chiến Binh Gai Góc!". Bố cục: Chân dung hào hùng của chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh: đứng kiêu hãnh trên mỏm đá sa mạc đỏ rực, gió thổi bay dải nơ đỏ thắm, ánh mặt trời mọc rực rỡ phía sau.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "những rãnh mao dẫn này có bề rộng biến thiên từ 5-150 μm, được thiết kế hình học bất đối xứng để nước chỉ có thể chảy một chiều về phía trước mà tuyệt đối không thể chảy ngược lại!". Bố cục: Mô phỏng 3D rãnh mao dẫn bất đối xứng bề rộng 5-150 μm: nước chảy cuồn cuộn một chiều về phía trước, khóa chặt không cho chảy ngược lại. KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nhưng khi chui vào dạ dày của Chiến Binh Gai Góc thì lại bị trung hòa hoàn toàn bởi một loại dịch nhầy đệm đặc biệt! Nó tiêu hóa đàn kiến ngon lành như chúng ta ăn snack cay giòn rụm!". Bố cục: Bên trong dạ dày chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh: lớp dịch nhầy đệm đặc biệt bao bọc trung hòa toàn bộ a-xít của kiến đen, biến chúng thành năng lượng tích tụ ở chiếc đuôi mập mạp.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dạ dày của nó có lớp màng bảo vệ đặc biệt dày dặn để vô hiệu hóa hoàn toàn nọc độc a-xít của đàn kiến, biến chúng thành nguồn năng lượng dồi dào để sinh tồn!". Bố cục: Cấu tạo thành dạ dày bọc thép sinh học của chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh: lớp màng nhầy đệm dày dặn ngăn cách hoàn toàn các chất độc, bảo vệ cơ thể an toàn tuyệt đối.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "còn dưới mặt đất, một chú kỳ đà khổng lồ Varanus dài 2m đang lùng sục từng bụi cỏ khô tìm kiếm con mồi. Với đôi chân ngắn ngủn di chuyển chậm chạp, Thằn Lằn Quỷ Gai chạy trốn thế nào được trước những sát thủ tốc độ này? Nó không thèm chạy trốn!". Bố cục: Chú kỳ đà chú kỳ đà sa mạc khổng lồ dài 2m da hoa văn xám đen, biểu cảm kinh ngạc lè lưỡi thụt lùi khổng lồ dài 2m da hoa văn xám đen đang bò trườn trên mặt cát sục sạo từng bụi cỏ khô tìm kiếm chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hàng trăm chiếc gai nhọn trên lưng vốn dĩ nằm xuôi nay dựng đứng vuông góc 90°, biến nó thành một quả cầu chông sắt gai góc không có bất kỳ khe hở nào để cắn!". Bố cục: Cận cảnh hàng trăm chiếc gai nón trên lưng chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh dựng đứng vuông góc 90°; toàn bộ cơ thể trở thành khối chông sắt bất khả xâm phạm.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và sau khi thoát hiểm, quý vị hãy chiêm ngưỡng dáng đi độc nhất vô nhị của quái kiệt này: Dáng đi lá khô đung đưa!". Bố cục: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh thở phào xẹp bớt không khí, đứng chớp mắt tinh nghịch giữa hoàng hôn sa mạc chuẩn bị phô diễn dáng đi tàng hình độc nhất vô nhị.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giữa sự khắc nghiệt điên rồ ấy, Chiến Binh Gai Góc lại tiếp tục biểu diễn tuyệt kỹ thứ ba: Biến hóa màu sắc như tắc kè hoa!". Bố cục: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh đứng trên mỏm đá đêm sa mạc, cơ thể bắt đầu biến đổi màu sắc kỳ ảo như một chú tắc kè hoa thông minh.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đồng thời, màu sắc đất đỏ này ngụy trang nó hòa lẫn hoàn hảo vào màu cát sa mạc Red Centre nước Úc, khiến những con cú đêm hay rắn độc bò ngang qua cũng chỉ nhìn thấy một cục đá vô tri vô giác!". Bố cục: Bóng đêm sa mạc bao trùm: một con cú đêm bay lượn sát mặt đất nhưng không tài nào phát hiện ra chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh đang ẩn mình như tảng đá sa mạc.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "còn Thằn Lằn Quỷ Gai nước Úc hoàn toàn không cần bắn máu, vì bộ giáp gai thép và chiếc đầu giả của nó đã quá đủ để khiến mọi kẻ săn mồi phải bỏ chạy mất dép rồi!". Bố cục: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh cười tươi vỗ ngực tự hào khẳng định: 'Thằn Lằn Quỷ Gai Úc tôi có giáp gai thép và đầu giả là đủ bá chủ sa mạc rồi!'.
```
</details>

<details><summary>L62</summary>

```text
HÌNH L62 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một sinh vật nhỏ bé không có nanh nhọn, không có nọc độc, chạy chậm như rùa nhưng đã kiên cường ngự trị giữa sa mạc khô cằn khắc nghiệt nhất hành tinh qua hàng triệu năm lịch sử!". Bố cục: Chân dung kiên cường của chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh: một chú thằn lằn nhỏ bé nhưng ngự trị sa mạc khắc nghiệt nhất hành tinh suốt hàng triệu năm qua.
```
</details>

<details><summary>L63</summary>

```text
HÌNH L63 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà nghiên cứu sinh thái học đã đếm từng nhịp nuốt và ghi nhận con số kỷ lục: trong một bữa ăn kéo dài vài tiếng đồng hồ, một chú Thằn Lằn Quỷ Gai có thể nuốt chửng từ 1.000 đến 2.500 con kiến độc!". Bố cục: Bộ đếm kỷ lục ăn kiến: con số nhảy vọt từ 1.000 đến 2.500 con kiến đen; chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh ngồi liếm mép no nê thỏa mãn giữa bãi cát.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "05:00 sáng giữa sa mạc Úc cháy bỏng!". Bố cục: KHUNG HÌNH DỌC 9:16: phóng viên truyền hình 24h mặc áo gile thám hiểm nhiều túi, tay cầm micro có logo '24H WILD' giơ chiếc đồng hồ 05:00 sáng giữa sa mạc đỏ rực, dòng chữ lớn 'UỐNG NƯỚC BẰNG BÀN CHÂN?!' xuất hiện nổi bật phía trên.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Một sinh vật không cần cúi đầu mà vẫn có thể uống nước ngọt lành chỉ bằng cách dẫm bàn chân lên cát ẩm!". Bố cục: KHUNG HÌNH DỌC 9:16: Chân dung chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh đứng trên nền cát sa mạc khô khốc, ngửa mặt lên trời cười tự tin không cần cúi đầu tìm nước.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đó chính là Thằn Lằn Quỷ Gai, quái kiệt bọc thép dài 20cm của lục địa nắng cháy.". Bố cục: KHUNG HÌNH DỌC 9:16: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh toàn thân phủ kín hàng trăm chiếc gai nón nhọn hoắt như cỗ xe tăng tí hon, chiếc mũ safari và nơ đỏ ngộ nghĩnh.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Làn da của nó phủ đầy mạng lưới rãnh mao dẫn siêu nhỏ,". Bố cục: KHUNG HÌNH DỌC 9:16: Phóng to mạng lưới rãnh mao dẫn trên da chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh: các hạt sương đọng quanh chân bắt đầu được hút vào rãnh da.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Mỗi ngày, nó kiên nhẫn nuốt chửng tới 2.500 con kiến đen độc hại bằng chiếc lưỡi dính siêu tốc.". Bố cục: KHUNG HÌNH DỌC 9:16: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh phóng chiếc lưỡi dính màu hồng siêu tốc quét sạch đàn kiến đen Iridomyrmex chạy ngang qua bãi cát.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Khi bị kẻ săn mồi tấn công, nó cúi gục đầu thật xuống đất và chìa chiếc bướu gai đầu giả sắc nhọn sau gáy ra ngoài". Bố cục: KHUNG HÌNH DỌC 9:16: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh giấu đầu thật vào giữa 2 chân trước, ngóc chiếc bướu gai đầu giả sắc nhọn sau gáy lên lừa kẻ săn mồi cắn vào.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "lừa kẻ thù cắn rách mồm!". Bố cục: KHUNG HÌNH DỌC 9:16: Chó hoang Dingo ngoạm trúng bướu gai nhọn hoắt, ôm mồm sưng vù khóc thét bỏ chạy.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Chưa hết, nó còn có thể hít khí phồng to cơ thể gấp đôi thành quả cầu gai bọc thép không kẻ nào nuốt trôi!". Bố cục: KHUNG HÌNH DỌC 9:16: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh hít khí phồng to cơ thể gấp đôi thành một quả cầu gai bọc thép tròn xoe, gai nhọn chĩa tứ phía không thể nuốt.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Vậy là bí mật đã sáng tỏ: một cỗ xe tăng tí hon với bản lĩnh sinh tồn đỉnh cao". Bố cục: KHUNG HÌNH DỌC 9:16: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh bước đi trên đỉnh cồn cát đỏ sa mạc rực rỡ ánh bình minh, biểu tượng cho cỗ xe tăng sinh tồn hoàn hảo khép lại câu chuyện.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "ngự trị chảo lửa sa mạc suốt hàng triệu năm qua!". Bố cục: KHUNG HÌNH DỌC 9:16: Toàn cảnh sa mạc Red Centre nước Úc rực rỡ ánh rạng đông, Thằn Lằn Quỷ Gai uy nghi ngự trị khép lại câu chuyện trọn vẹn.
```
</details>

<details><summary>S11</summary>

```text
HÌNH S11 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "tự động hút từng giọt sương mai từ bàn chân chảy ngược chiều trọng lực dọc theo sống lưng chạy thẳng vào miệng!". Bố cục: KHUNG HÌNH DỌC 9:16: Các giọt sương mai từ bàn chân tự động bị hút ngược chiều trọng lực chảy dọc sống lưng chạy thẳng vào miệng chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/62 của video YouTube về Thằn Lằn Quỷ Gai). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/11 của video YouTube Shorts về Thằn Lằn Quỷ Gai). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh. 
```
</details>

## 7. SEO

- **title:** Tại Sao Thằn Lằn Quỷ Gai Uống Nước Bằng... Bàn Chân?! | Thằn Lằn Quỷ Gai | Tập 19
- **hook_paragraph:** Thằn Lằn Quỷ Gai hút nước từ bàn chân chảy ngược lên miệng qua mao dẫn, nuốt 2.500 con kiến đen mỗi ngày và sở hữu chiếc đầu giả gai nhọn lừa kẻ săn mồi! Khám phá nhật ký sinh tồn 24 giờ của Chiến Binh Gai Góc giữa sa mạc nước Úc.
- **question:** Bạn có đoán ra BÓNG ĐEN BÍ ẨN ở cuối video là sinh vật nào không? (Gợi ý: Siêu xạ thủ bắn tỉa nén tia nước bắn rơi côn trùng cách 3m, tính góc khúc xạ ánh sáng). Bình luận dự đoán nhé!
- **next_teaser:** Bóng đen bí ẩn — siêu xạ thủ bắn tỉa tia nước 3m và thuật toán khúc xạ ánh sáng đỉnh cao
- **shorts_title:** Tại Sao Thằn Lằn Quỷ Gai Uống Nước Bằng... Bàn Chân?! 🦎 #shorts #thanlanquygai
- **shorts_desc:** Thằn Lằn Quỷ Gai hút nước từ chân chảy ngược lên miệng, ăn 2.500 con kiến độc và sở hữu chiếc đầu giả lừa sát thủ! Khám phá Chiến Binh Gai Góc sa mạc Úc! 🦎🌵
- **bullets:** Hiện tượng mao dẫn kỳ diệu: Da hút nước từ cát ẩm chảy ngược lên khóe miệng · Đại tiệc 2.500 con kiến đen độc hại bằng chiếc lưỡi dính siêu tốc · Chiếc bướu gai đầu giả đánh lừa kẻ săn mồi cắn rách mồm · Phồng to thành quả cầu gai bọc thép và dáng đi giật cục như lá khô
- **tags:** thằn lằn quỷ gai, than lan quy gai, thorny devil, thằn lằn uống nước bằng chân, thằn lằn quỷ gai sa mạc úc, động vật sa mạc, thế giới động vật, động vật kỳ lạ, vẽ chuyện hoang dã, whiteboard animation, khoa học thú vị, nhật ký 24 giờ
- **hashtags:** #ThanLanQuyGai #ThornyDevil #TheGioiDongVat #VeChuyenHoangDa #KhoaHoc

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-19-than-lan-quy-gai
python src/episode/pipeline.py tts    projects/tap-19-than-lan-quy-gai     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-19-than-lan-quy-gai     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-19-than-lan-quy-gai     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-19-than-lan-quy-gai              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-19-than-lan-quy-gai --force
python scripts/beat_sheet.py projects/tap-19-than-lan-quy-gai               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-19-than-lan-quy-gai/audio/shorts.wav projects/tap-19-than-lan-quy-gai/renders/tap-19-than-lan-quy-gai_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-19-than-lan-quy-gai
python src/episode/pipeline.py seo    projects/tap-19-than-lan-quy-gai
python src/episode/episode_doc.py     projects/tap-19-than-lan-quy-gai
```

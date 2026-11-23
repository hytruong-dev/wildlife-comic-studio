# TẬP 20 — CÁ CUNG THỦ · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-20-ca-cung-thu`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-20-ca-cung-thu`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F2` · **Persona giọng:** `ky_su_vu_khi` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Cá Cung Thủ |
| Tiêu đề YouTube | Cá Cung Thủ Bắn Nước 3 Mét & Thuật Toán Khúc Xạ Ánh Sáng?! \| Tập 20 |
| Video dài | `renders/tap-20-ca-cung-thu_long.mp4` — 9:21.3 (561.3s) |
| Shorts | `renders/tap-20-ca-cung-thu_shorts.mp4` — 0:52.3 (52.3s) |
| Thumbnail | `renders/tap-20-ca-cung-thu_thumbnail.jpg` |
| Số hình | dài 72 beat / 72 ảnh riêng; Shorts 13 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/72 của video YouTube về Cá Cung Thủ). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor). Nhân vật phụ cố định: chú nhện con hoạt hình nhiều mắt ngơ ngác, lông xù màu nâu, đeo ba lô tí hon bám trên lá cây; chú bọ ngựa hoạt hình màu xanh lá, hai càng sắc nhọn giương lên đầy tự tin bám trên thân cây; chú dế mèn hoạt hình màu nâu cầm chiếc ô che mưa tí hon ngơ ngác; cô trợ lý sóc hoạt hình đeo kính cận to tròn, mặc áo blouse trắng phòng thí nghiệm, cầm thước đo góc quang học. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — THIỆN XẠ ĐẦM LẦY 20CM BẮN TIA NƯỚC HẠ GỤC MỤC TIÊU CÁCH 2M
*Thẻ chương:* LOÀI CÁ BẮN NƯỚC BÁCH PHÁT BÁCH TRÚNG LÊN CẠN

*Badge:* `HỒ SƠ XẠ THỦ` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene01_p0.wav` (347 ký tự) · mood `tram_bi_an`

```text
Báo cáo thử nghiệm vũ khí tối mật số hai mươi. Toàn đội kỹ thuật hãy khóa mục tiêu và khởi động camera tốc độ cao! Chiến trường mà chúng ta khảo sát hôm nay không phải bầu trời rực lửa hay pháo đài thép kiên cố, mà là những rặng đước ngập mặn tĩnh lặng vùng Đông Nam Á. [surprise-oh] Nơi một sát thủ thầm lặng đang nằm phục kích ngay sát mặt nước!
```
**Part 1** → `audio/vs/scene01_p1.wav` (367 ký tự) · mood `hao_hung`

```text
Nhân vật đứng trước ống kính của chúng ta hôm nay có chiều dài cơ thể khiêm tốn chỉ từ mười lăm đến hai mươi xăng-ti-mét, khoác lên mình bộ vảy màu bạc ánh kim cùng những sọc đen quân sự sắc sảo. [laughter] Nhưng đừng để kích thước nhỏ bé này đánh lừa mắt thường! Trong giới quân sự tự nhiên, gã được phong tặng danh hiệu Thiện Xạ Đầm Lầy, hay còn gọi là Cá Cung Thủ!
```
**Part 2** → `audio/vs/scene01_p2.wav` (373 ký tự) · mood `don_dap`

```text
Quy tắc tác chiến của loài cá thông thường là: Muốn ăn thì phải chờ con mồi sảy chân rơi xuống nước. Nhưng Thiện Xạ Đầm Lầy của chúng ta thì tuyệt đối không có khái niệm ăn xin lòng thương hại! [surprise-wa] Nếu con mồi đậu trên cành lá cao tới một mét rưỡi, hai mét, thậm chí kỷ lục lên tới ba mét, gã sẽ tự tay phóng hỏa lực lên trời để kéo con mồi rơi thẳng xuống miệng!
```
**Part 3** → `audio/vs/scene01_p3.wav` (290 ký tự) · mood `hao_hung`

```text
Hỏa lực của gã không phải đạn chì hay thuốc nổ, mà chính là những giọt nước biển được nén áp suất cao, phụt ra từ miệng với độ chính xác đến từng mi-li-mét! Một phát bắn trúng đích đủ sức hất văng một con châu chấu to béo hay một chú nhện bám chặt trên lá cây rơi xuống nước trong nháy mắt!
```
**Part 4** → `audio/vs/scene01_p4.wav` (228 ký tự) · mood `tram_bi_an`

```text
Hôm nay, ban chỉ huy kỹ thuật sẽ cùng giải phẫu toàn diện khẩu súng sinh học này: [surprise-oh] Làm thế nào một sinh vật sống hoàn toàn dưới nước lại có thể ngắm bắn bách phát bách trúng các mục tiêu di động trên không gian cạn?
```

### scene02 — RÃNH CHỮ V VÀ KỸ THUẬT NÉN ĐẠN NƯỚC GIA TỐC ĐUÔI
*Thẻ chương:* NÒNG SÚNG RÃNH CHỮ V VÀ GIỌT ĐẠN NƯỚC KHỔNG LỒ

*Badge:* `BẢN VẼ NÒNG SÚNG` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene02_p0.wav` (317 ký tự) · mood `hao_hung`

```text
Hãy trải bản vẽ kỹ thuật khoang miệng của Thiện Xạ Đầm Lầy lên màn hình phân tích! [surprise-oh] Rất nhiều người nghĩ rằng con cá này chỉ đơn giản là ngậm nước vào miệng rồi phun phì phì ra ngoài như trẻ con nghịch nước. Sai lầm hoàn toàn! Cấu trúc nòng súng của Cá Cung Thủ là một tuyệt tác cơ khí thủy lực đỉnh cao.
```
**Part 1** → `audio/vs/scene02_p1.wav` (280 ký tự) · mood `nghiem_trang_gia`

```text
Ở vòm họng trên của cá có một đường rãnh hình chữ V sâu và hẹp. Khi chuẩn bị khai hỏa, nó áp chặt chiếc lưỡi linh hoạt của mình ép sát vào rãnh chữ V này, biến khoang miệng thành một chiếc nòng súng ống tròn hoàn hảo có đường kính nòng chỉ vỏn vẹn nửa mi-li-mét đến một mi-li-mét!
```
**Part 2** → `audio/vs/scene02_p2.wav` (322 ký tự) · mood `don_dap`

```text
Tiếp theo, hai nắp mang khổng lồ đóng sập cực mạnh lại với nhau, nén toàn bộ lượng nước trong khoang miệng và tống vọt ra ngoài qua khe nòng súng với vận tốc lên tới bốn đến năm mét một giây! Nhưng bí mật kinh hoàng nhất mà các nhà vật lý học thuộc Đại học Bayreuth ở Đức phát hiện ra lại nằm ở động lực học của dòng nước!
```
**Part 3** → `audio/vs/scene02_p3.wav` (139 ký tự) · 🎭 cameo `co_tro_ly`

```text
Báo cáo chỉ huy, cảm biến tốc độ đo được phần đuôi tia nước bay nhanh hơn phần đầu tới hai mươi phần trăm, hai phần nước đang nhập làm một!
```
**Part 4** → `audio/vs/scene02_p4.wav` (342 ký tự) · mood `don_dap`

```text
[surprise-wa] Đây chính là tuyệt kỹ làm chấn động giới cơ học chất lỏng thế giới! Cá Cung Thủ liên tục điều chỉnh chuyển động của khóe miệng trong suốt thời gian bắn kéo dài vài mili-giây, khiến phần nước phun ra sau có vận tốc lớn hơn phần nước phun ra trước. Khi bay trên không trung, phần đuôi lao vút lên đuổi kịp và đập dồn vào phần đầu!
```
**Part 5** → `audio/vs/scene02_p5.wav` (301 ký tự) · mood `hao_hung`

```text
Hiện tượng này biến một tia nước mỏng manh thành một giọt đạn nước khổng lồ cô đặc ngay trước thời điểm chạm mục tiêu! Nhờ đó, động năng và lực va đập tại điểm tiếp xúc tăng vọt gấp năm đến mười lần so với dòng nước bình thường, đủ sức đập văng cả những con bọ ngựa đang găm chặt móng vuốt vào vỏ cây!
```
**Part 6** → `audio/vs/scene02_p6.wav` (327 ký tự) · mood `don_dap`

```text
[surprise-oh] Chưa hết đâu các đồng chí! Hộp tiếp đạn của khẩu súng này cũng thuộc hàng khủng: Cá Cung Thủ có thể bắn liên thanh tới sáu đến bảy phát đạn nước liên tiếp chỉ trong vòng hai giây mà không cần ngụp xuống nạp lại nước! Mỗi phát bắn đều giữ nguyên hỏa lực chính xác tuyệt đối như một khẩu súng máy tự động dưới nước!
```

### scene03 — BỘ NÃO TỰ ĐỘNG GIẢI ĐỊNH LUẬT KHÚC XẠ SNELL
*Thẻ chương:* BỘ NÃO 0,1 GAM GIẢI BÀI TOÁN KHÚC XẠ TRONG 0,05 GIÂY

*Badge:* `THUẬT TOÁN QUANG HỌC` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene03_p0.wav` (262 ký tự) · mood `tram_bi_an`

```text
Sở hữu một khẩu đại bác uy lực là một chuyện, nhưng ngắm bắn trúng mục tiêu lại là bài toán khó hơn gấp vạn lần! Và trở ngại chết người mà mọi xạ thủ dưới nước phải đối mặt chính là: [surprise-oh] Hiện tượng khúc xạ ánh sáng qua ranh giới giữa nước và không khí!
```
**Part 1** → `audio/vs/scene03_p1.wav` (269 ký tự) · mood `nghiem_trang_gia`

```text
Bất kỳ học sinh nào từng học vật lý đều biết định luật bẻ gãy ánh sáng X-neo: Ánh sáng truyền từ không khí vào nước sẽ bị bẻ cong một góc đáng kể. Do đó, vị trí mà đôi mắt cá nhìn thấy chỉ là một ảnh ảo lơ lửng, lệch hẳn so với vị trí thực tế của con mồi trên cành cây!
```
**Part 2** → `audio/vs/scene03_p2.wav` (289 ký tự) · mood `hao_hung`

```text
Nếu bạn bắn thẳng vào vị trí bạn nhìn thấy, viên đạn nước chắc chắn sẽ bay chệch lên trời và con mồi sẽ ung dung bay mất. Nhưng bộ não của Thiện Xạ Đầm Lầy chỉ nặng chưa đầy không phẩy một gam lại có thể giải bài toán lượng giác khúc xạ phức tạp này trong vòng chưa đầy năm mươi mili-giây!
```
**Part 3** → `audio/vs/scene03_p3.wav` (117 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Alo các bác xạ thủ ơi, em đứng trên cành nghiêng bốn mươi lăm độ thế này mà tia nước bắn trúng ngay giữa trán là sao?
```
**Part 4** → `audio/vs/scene03_p4.wav` (393 ký tự) · mood `hao_hung`

```text
[laughter] Đúng như chú nhện con ngơ ngác vừa ôm đầu kêu trời! Để giảm thiểu tối đa sai số khúc xạ, Cá Cung Thủ thường bơi tới vị trí gần vuông góc dưới mục tiêu, tạo góc bắn từ bảy mươi độ đến tám mươi độ so với mặt nước. Nhưng ngay cả khi bị ép bắn ở góc nghiêng bốn mươi lăm độ, tỷ lệ bắn trúng mục tiêu ngay trong phát đạn đầu tiên của gã vẫn đạt tới chín mươi đến chín mươi lăm phần trăm!
```
**Part 5** → `audio/vs/scene03_p5.wav` (220 ký tự) · mood `hao_hung`

```text
Đôi mắt to tròn của cá có cấu tạo nhãn cầu đặc biệt với hai trục quang học độc lập, vừa giúp bù trừ tự động độ cong mặt nước, vừa tạo ra tầm nhìn lập thể ba chiều cực kỳ sắc bén xuyên qua lớp gương phản chiếu của mặt hồ!
```
**Part 6** → `audio/vs/scene03_p6.wav` (313 ký tự) · mood `hao_hung`

```text
[surprise-wa] Thậm chí võng mạc của nó còn sở hữu các tế bào cảm quang chuyên biệt có khả năng lọc sạch ánh sáng lóa mặt trời và bóc tách các vệt màu ngụy trang của bầy côn trùng ẩn nấp sau kẽ lá xanh! Một hệ thống kính ngắm quang học hồng ngoại sinh học đỉnh cao mà các nhà thiết kế vũ khí hiện đại phải ghen tị!
```

### scene04 — TÂN BINH BẮN HỤT TRĂM PHÁT VÀ NĂNG LỰC HỌC TẬP
*Thẻ chương:* KHÔNG PHẢI BẢN NĂNG CÓ SẴN MÀ PHẢI TẬP BẮN TỪ BÉ

*Badge:* `HUẤN LUYỆN TÁC CHIẾN` · *mood mặc định:* `nghiem_trang_gia`

**Part 0** → `audio/vs/scene04_p0.wav` (286 ký tự) · mood `tram_bi_an`

```text
Nhiều người lầm tưởng khả năng bắn tỉa thần sầu này là bản năng bẩm sinh được lập trình sẵn trong gen của Cá Cung Thủ. [surprise-oh] Nghiên cứu thực nghiệm chấn động của các nhà khoa học đã chứng minh điều ngược lại: Đây là một kỹ năng quân sự bắt buộc phải trải qua rèn luyện gian khổ!
```
**Part 1** → `audio/vs/scene04_p1.wav` (209 ký tự) · 🎭 cameo `phat_thanh_vien`

```text
Bản tin huấn luyện từ trường bắn tân binh: Những chú cá non mới nở chỉ có thể bắn ra những tia nước yếu ớt xa vài centimet, và chúng bắn trượt tới chín mươi chín phần trăm số mục tiêu trong những tuần đầu đời!
```
**Part 2** → `audio/vs/scene04_p2.wav` (221 ký tự) · mood `hao_hung`

```text
[laughter] Đúng là cảnh tượng bi hài của trường bắn quân sự! Cá cung thủ non phải trải qua hàng ngàn lần thử và sai, tự rút kinh nghiệm sau mỗi cú bắn lệch để não bộ dần dần học cách bù trừ góc khúc xạ theo cự ly thực tế.
```
**Part 3** → `audio/vs/scene04_p3.wav` (370 ký tự) · mood `hao_hung`

```text
Nhưng điều làm kinh ngạc giới nghiên cứu hành vi động vật là phát hiện công bố trên tạp chí Nature: Cá Cung Thủ sở hữu năng lực học tập xã hội đỉnh cao! Một con cá non nếu được bơi cạnh những xạ thủ kỳ cựu dày dặn kinh nghiệm chỉ cần đứng quan sát đàn anh bắn mồi vài lần là có thể tự điều chỉnh góc bắn của mình chuẩn xác hơn gấp nhiều lần mà không cần tự mình thử sai!
```
**Part 4** → `audio/vs/scene04_p4.wav` (285 ký tự) · mood `hao_hung`

```text
Khả năng quan sát, phân tích đường đạn của đồng loại rồi mô phỏng lại trong não bộ là một năng lực nhận thức cấp cao mà trước đây người ta ngỡ chỉ có ở các loài linh trưởng và con người! Một minh chứng hùng hồn cho thấy trí tuệ của loài cá vượt xa những định kiến nông cạn thường thấy.
```
**Part 5** → `audio/vs/scene04_p5.wav` (381 ký tự) · mood `hao_hung`

```text
Để kiểm chứng điều này, giáo sư Sơ-suýt-tơ tại Đức đã thiết lập một thí nghiệm độc lạ: Ông chiếu các điểm sáng nhân tạo di động trên màn hình máy tính với vận tốc thay đổi liên tục. [surprise-oh] Chỉ sau vài lượt thử, bầy Cá Cung Thủ đã tự tính toán được quy luật chuyển động và bắn đón đầu mục tiêu ảo cực kỳ chính xác! Một tư duy tác chiến bắn chặn ngang tầm tên lửa phòng không!
```

### scene05 — TÍNH QUỸ ĐẠO RƠI TRONG 100MS VÀ CÚ NHẢY NGOẠM MỒI
*Thẻ chương:* TÍNH TOÁN ĐIỂM RƠI TRONG 100 MILI-GIÂY VÀ CUỘC ĐUA CƯỚP MỒI

*Badge:* `ĐOÁN TRƯỚC ĐIỂM RƠI` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene05_p0.wav` (307 ký tự) · mood `tram_bi_an`

```text
Bắn trúng con mồi rớt khỏi cành lá mới chỉ là một nửa chặng đường của chiến dịch săn mồi. Trong thế giới đầm lầy cạnh tranh khốc liệt, bắn trúng mà không đớp kịp thì miếng ăn sẽ rơi ngay vào miệng đối thủ bên cạnh! [surprise-oh] Và đây là lúc bộ vi xử lý đạn đạo của Thiện Xạ Đầm Lầy phát huy uy lực tối đa.
```
**Part 1** → `audio/vs/scene05_p1.wav` (237 ký tự) · mood `don_dap`

```text
Ngay khoảnh khắc tia nước vừa rời khỏi khóe miệng trong vòng chưa đầy một trăm mili-giây, Cá Cung Thủ đã tính toán xong toàn bộ phương trình parabol đường rơi của con mồi: Nó biết chính xác vị trí và thời điểm con côn trùng sẽ tiếp nước!
```
**Part 2** → `audio/vs/scene05_p2.wav` (301 ký tự) · mood `don_dap`

```text
Không cần đợi nhìn thấy con mồi rơi tới đâu, con cá lập tức bật chế độ bơi nước rút với tốc độ xé nước, lao thẳng tới đúng tọa độ tiếp nhận trước khi con mồi chạm mặt nước chỉ trong không phẩy một giây! Một pha đoán đầu đường đạn thần tốc khiến mọi đối thủ xung quanh chỉ biết đứng nhìn trong bất lực!
```
**Part 3** → `audio/vs/scene05_p3.wav` (318 ký tự) · mood `don_dap`

```text
[surprise-wa] Cuộc đua cướp mồi trong bầy đàn khốc liệt đến mức ba đến bốn đối thủ bơi bên cạnh cũng lập tức tính toán điểm rơi để lao vào tranh cướp! Nếu tay súng chính chỉ cần chậm trễ một phần mười giây trong pha bơi nước rút, con mồi do chính mình tốn công bắn hạ sẽ biến mất tăm vào dạ dày của kẻ cơ hội đứng xem!
```
**Part 4** → `audio/vs/scene05_p4.wav` (106 ký tự) · 🎭 cameo `ga_khong_lo`

```text
Tôi bắn tỉa trong quân đội cả đời mà nhìn pha tính toán đạn đạo của chú cá này cũng phải ngả mũ chào thua!
```
**Part 5** → `audio/vs/scene05_p5.wav` (371 ký tự) · mood `hao_hung`

```text
[laughter] Thậm chí Thiện Xạ Đầm Lầy còn trang bị một phương án tác chiến dự phòng cực kỳ thực dụng: Nếu con mồi đậu ở cành lá quá thấp dưới ba mươi xăng-ti-mét, gã sẽ không thèm tốn một giọt nước nào! Con cá chỉ cần quẫy mạnh chiếc đuôi vây khỏe khoắn, phóng vút toàn bộ cơ thể bay lên khỏi mặt nước như một chiếc tên lửa mini để ngoạm gọn con mồi ngay trên không trung!
```
**Part 6** → `audio/vs/scene05_p6.wav` (271 ký tự) · mood `bi_hai`

```text
Tuy nhiên, cỗ máy săn mồi hoàn hảo này cũng có những tử huyệt kỹ thuật: Khi trời nổi gió to làm mặt nước dậy sóng cuồn cuộn hoặc khi váng dầu ô nhiễm che phủ mặt sông, thuật toán quang học bị nhiễu loạn hoàn toàn, biến tay súng cừ khôi thành một kẻ bắn trượt đáng thương!
```

### scene06 — BÀI HỌC ĐỘ CHÍNH XÁC VÀ BÓNG ĐEN WOLVERINE 860V TẬP SAU
*Thẻ chương:* BÀI HỌC VỀ ĐỘ CHÍNH XÁC VÀ BẬT MÍ BÓNG ĐEN TẬP 21

*Badge:* `BÁO CÁO THỬ NGHIỆM` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (349 ký tự) · mood `am_ap`

```text
Báo cáo tổng kết thử nghiệm kỹ thuật số hai mươi: Cá Cung Thủ chứng minh cho chúng ta thấy rằng sức mạnh hủy diệt không nhất thiết phải đến từ kích thước cơ bắp đồ sộ hay vũ khí hủy diệt hàng loạt. Sự am hiểu quy luật tự nhiên, khả năng tính toán chuẩn xác và tinh thần học hỏi không ngừng mới là chìa khóa vạn năng để sinh tồn và làm chủ cuộc chơi.
```
**Part 1** → `audio/vs/scene06_p1.wav` (276 ký tự) · mood `hao_hung`

```text
Chính cơ chế nén dòng nước gia tốc đuôi của loài cá này đang là nguồn cảm hứng vô giá để các kỹ sư hàng không vũ trụ và công nghệ in ba chiều hiện đại thiết kế ra những vòi phun hạt siêu vi mô có độ chính xác tuyệt đối mà không cần sử dụng bất kỳ pít-tông cơ học phức tạp nào!
```
**Part 2** → `audio/vs/scene06_p2.wav` (230 ký tự) · mood `hao_hung`

```text
[surprise-oh] Bạn khâm phục điều gì nhất ở Thiện Xạ Đầm Lầy Cá Cung Thủ: Khẩu đại bác nén đạn nước gia tốc đuôi, hay bộ não giải định luật khúc xạ ánh sáng trong chớp mắt? Hãy để lại ý kiến bình luận của đội kỹ thuật bên dưới nhé!
```
**Part 3** → `audio/vs/scene06_p3.wav` (758 ký tự) · mood `tram_bi_an`

```text
Và bây giờ, hãy hướng ngòi bút về phân cảnh kết thúc bí ẩn! Trong tập tiếp theo, chúng ta sẽ rời xa những cánh rừng ngập mặn châu Á để thâm nhập vào vùng rừng nhiệt đới âm u của lục địa đen Châu Phi. [surprise-wa] Hãy chiêm ngưỡng một bóng đen bí ẩn vô cùng kỳ dị! Một sinh vật lưỡng cư nhỏ bé, nhưng sở hữu cơ chế tự vệ được đánh giá là điên rồ và đau đớn nhất hành tinh: Khi bị kẻ săn mồi dồn vào chân tường, nó sẽ chủ động tự co thắt cơ bắp bẻ gãy chính đốt xương ngón chân của mình, đâm thủng lớp da thịt ra ngoài để tạo thành một bộ móng vuốt sắc nhọn như dao găm hệt như dị nhân Oen-vơ-rin trong truyện tranh! Đố các chuyên viên kỹ thuật biết danh tính của sát thủ tự bẻ xương kỳ lạ này là ai? Hãy viết ngay câu trả lời của bạn dưới phần bình luận nhé!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Cảnh báo xạ thủ bắn tỉa! Bạn có tin một con cá dưới nước lại có thể ngắm bắn bách phát bách trúng các mục tiêu đậu trên cành cây cao tới hai mét? Đây là Cá Cung Thủ, tay súng bắn tỉa cừ khôi của các rạn rừng ngập mặn! Thứ nhất, vòm họng của nó có rãnh chữ V ép chặt với lưỡi, tạo thành chiếc nòng súng tí hon nén tia nước bắn xa kỷ lục tới ba mét! Thứ hai, phần đuôi tia nước bay nhanh hơn phần đầu, đập dồn lại thành một giọt đạn nước khổng lồ làm tăng lực va đập gấp mười lần để hạ gục con mồi! Thứ ba, mặt nước luôn bẻ cong ánh sáng theo định luật khúc xạ, nhưng bộ não của loài cá này giải bài toán quang học chỉ trong năm mươi mili-giây để bắn chính xác tới chín mươi lăm phần trăm! Chưa hết, nó còn tính toán trước điểm rơi đạn đạo để bơi nước rút cướp mồi trước đối thủ chỉ trong không phẩy một giây! Độ chính xác và khả năng thích nghi phi thường, đó chính là vũ khí tối thượng giúp Thiện Xạ Đầm Lầy thống trị cả hai thế giới dưới nước và trên cạn!
```

**Whisper prompt:** `Cá Cung Thủ, Thiện Xạ Đầm Lầy, Toxotes, 20cm, 3m, 2m, 1,5m, 30cm, 5 m/s, 100 mili-giây, 50 mili-giây, 0,1 giây, 90%, 95%, 45 độ, 70 độ, 80 độ, Snell, Bayreuth, Stefan Schuster, Amazon, Châu Phi, Ếch Lông Wolverine, 860V`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| hai mươi xăng-ti-mét | 20cm |
| Hai mươi xăng-ti-mét | 20cm |
| mười lăm đến hai mươi xăng-ti-mét | 15-20cm |
| Mười lăm đến hai mươi xăng-ti-mét | 15-20cm |
| ba mươi xăng-ti-mét | 30cm |
| Ba mươi xăng-ti-mét | 30cm |
| hai lăm xăng-ti-mét | 25cm |
| ba mét | 3m |
| Ba mét | 3m |
| hai mét | 2m |
| Hai mét | 2m |
| một mét rưỡi | 1,5m |
| Một mét rưỡi | 1,5m |
| năm mét một giây | 5 m/s |
| Năm mét một giây | 5 m/s |
| bốn đến năm mét một giây | 4-5 m/s |
| Bốn đến năm mét một giây | 4-5 m/s |
| nửa mi-li-mét | 0,5mm |
| Nửa mi-li-mét | 0,5mm |
| một mi-li-mét | 1mm |
| Một mi-li-mét | 1mm |
| nửa giây | 0,5 giây |
| Nửa giây | 0,5 giây |
| không phẩy một giây | 0,1 giây |
| Không phẩy một giây | 0,1 giây |
| một trăm mili-giây | 100 mili-giây |
| Một trăm mili-giây | 100 mili-giây |
| năm mươi mili-giây | 50 mili-giây |
| Năm mươi mili-giây | 50 mili-giây |
| chín mươi lăm phần trăm | 95% |
| Chín mươi lăm phần trăm | 95% |
| chín mươi chín phần trăm | 99% |
| Chín mươi chín phần trăm | 99% |
| chín mươi phần trăm | 90% |
| Chín mươi phần trăm | 90% |
| một trăm phần trăm | 100% |
| Một trăm phần trăm | 100% |
| bốn mươi lăm độ | 45° |
| Bốn mươi lăm độ | 45° |
| bảy mươi độ | 70° |
| Bảy mươi độ | 70° |
| tám mươi độ | 80° |
| Tám mươi độ | 80° |
| chín mươi độ | 90° |
| Chín mươi độ | 90° |
| gấp năm đến mười lần | gấp 5-10 lần |
| Gấp năm đến mười lần | gấp 5-10 lần |
| gấp mười lần | gấp 10 lần |
| Gấp mười lần | gấp 10 lần |
| gấp đôi | gấp đôi |
| gấp ba | gấp 3 |
| gấp năm | gấp 5 |
| hàng trăm lần | hàng trăm lần |
| hàng ngàn lần | hàng ngàn lần |
| hàng triệu năm | hàng triệu năm |
| sáu đến bảy | 6-7 |
| Sáu đến bảy | 6-7 |
| hai giây | 2 giây |
| Hai giây | 2 giây |
| ba đến bốn | 3-4 |
| Ba đến bốn | 3-4 |
| hai mươi phần trăm | 20% |
| Hai mươi phần trăm | 20% |
| một phần mười giây | 0,1 giây |
| Một phần mười giây | 0,1 giây |
| thế kỷ hai mươi | thế kỷ 20 |
| Tập hai mươi | Tập 20 |
| Tập hai mươi mốt | Tập 21 |
| Tập mười sáu | Tập 16 |
| Tập mười lăm | Tập 15 |
| số hai mươi | số 20 |
| Số hai mươi | Số 20 |
| Tốc-xô-tét | Toxotes |
| Bay-roi-tơ | Bayreuth |
| Sơ-suýt-tơ | Schuster |
| X-neo | Snell |
| Oen-vơ-rin | Wolverine |
| hai mươi | 20 |
| ba mươi | 30 |
| bốn mươi | 40 |
| năm mươi | 50 |
| sáu mươi | 60 |
| bảy mươi | 70 |
| tám mươi | 80 |
| chín mươi | 90 |
| một trăm | 100 |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · THIỆN XẠ ĐẦM LẦY 20CM BẮN TIA NƯỚC HẠ GỤC MỤC TIÊU CÁCH 2M · 80.3s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:02.7 (2.7s) | L01 | Báo cáo thử nghiệm vũ khí tối mật số 20. |  | Phòng phân tích tác chiến quân sự: một hồ sơ mật đóng dấu đỏ thẫm 'BÁO CÁO THỬ NGHIỆM SỐ 20' đặt giữa bàn kim loại, màn hình phía sau hiển thị hình ảnh rừng đước ngập mặn rậm rạp. KHÔNG có chú Cá Cung Thủ trong cảnh này. |
| b02 | 00:02.7–00:06.0 (3.2s) | L02 | Toàn đội kỹ thuật hãy khóa mục tiêu và khởi động camera tốc độ |  | Bảng điều khiển công nghệ cao: các kỹ sư khởi động camera tốc độ cao và màn hình hiển thị thước ngắm hồng ngoại đang khóa mục tiêu. KHÔNG có chú Cá Cung Thủ trong cảnh này. |
| b03 | 00:06.0–00:13.5 (7.5s) | L03 | cao! Chiến trường mà chúng ta khảo sát hôm nay không phải bầu trời rực lửa hay pháo đài thép kiên cố, mà là những rặng đước ngập mặn tĩnh lặng vùng Đông Nam Á. |  | Rừng đước ngập mặn Đông Nam Á kỳ bí: rễ cây đước ngoằn ngoèo rủ xuống mặt nước phẳng lặng như gương; tia nắng ban mai xuyên qua kẽ lá mờ ảo. KHÔNG có chú Cá Cung Thủ trong cảnh này. |
| b04 | 00:13.5–00:17.0 (3.5s) | L04 | Nơi một sát thủ thầm lặng đang nằm phục kích ngay sát mặt nước! |  | Góc phục kích bí mật: sát mặt nước đục mờ, đôi mắt to lồi màu vàng của chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) nhô lên nhẹ nhàng không làm xao động một gợn sóng, kính ngắm laser đỏ phát sáng dò tìm mục tiêu. |
| b05 | 00:17.0–00:23.2 (6.2s) | L05 | Nhân vật đứng trước ống kính của chúng ta hôm nay có chiều dài cơ thể khiêm tốn chỉ từ 15-20cm, | **15-20cm** · chiều dài cơ thể · L/380 · [0.3, 0.55] | Chân dung oai phong: chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) bơi giữa làn nước trong xanh, thân hình vảy bạc ánh kim sọc đen quân sự, chiếc mũ beret đen kiêu hãnh, vây lưng bơi lượn điệu nghệ. |
| b06 | 00:23.2–00:30.7 (7.5s) | L06 | khoác lên mình bộ vảy màu bạc ánh kim cùng những sọc đen quân sự sắc sảo. Nhưng đừng để kích thước nhỏ bé này đánh lừa mắt thường! |  | Cận cảnh bộ giáp vảy bạc sọc đen quân sự tinh xảo của chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor), ánh kim loại lấp lánh dưới làn nước trong vắt, vây ngực chuyển động uyển chuyển. |
| b07 | 00:30.7–00:36.4 (5.6s) | L07 | Trong giới quân sự tự nhiên, gã được phong tặng danh hiệu Thiện Xạ Đầm Lầy, hay còn gọi là Cá Cung Thủ! |  | Tấm huy hiệu quân đội danh dự: chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) đứng trên bục danh dự vàng khắc dòng chữ 'THIỆN XẠ ĐẦM LẦY', vây trước chắp tay nghiêm trang, kính ngắm laser nhấp nháy chữ 'LOCKED'. |
| b08 | 00:36.4–00:41.0 (4.6s) | L08 | Quy tắc tác chiến của loài cá thông thường là: Muốn ăn thì phải chờ con mồi sảy chân rơi |  | Hình ảnh so sánh hài hước: BÊN TRÁI một chú cá thường ngửa bụng há họng chờ thức ăn rơi xuống bị gạch chéo đỏ; BÊN PHẢI chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) ngẩng cao đầu giương vây đầy khí phách chiến đấu. |
| b09 | 00:41.0–00:45.5 (4.5s) | L09 | xuống nước. Nhưng Thiện Xạ Đầm Lầy của chúng ta thì tuyệt đối không có khái niệm ăn xin lòng thương hại! |  | chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) bơi ngẩng cao đầu sát mặt nước, ánh mắt sắc lẹm kiên quyết, biểu tượng nắm đấm sắt tự lực cánh sinh phát sáng bên cạnh. |
| b10 | 00:45.5–00:53.8 (8.3s) | L10 | Nếu con mồi đậu trên cành lá cao tới 1,5m, 2m, thậm chí kỷ lục lên tới 3m, gã sẽ tự tay phóng hỏa lực lên trời để kéo con mồi rơi thẳng xuống miệng! | **2 MÉT** · tầm bắn hiệu quả · R/380 · [0.75, 0.55]<br>**3 MÉT** · kỷ lục cực đại · R/480 · [0.75, 0.55] | Thước đo cự ly bắn tỉa trên không: BÊN TRÁI chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) nằm sát mặt nước, tia ngắm laser đỏ hướng thẳng lên cành lá cao 2m có chú chú nhện con hoạt hình nhiều mắt ngơ ngác, lông xù màu nâu, đeo ba lô tí ho |
| b11 | 00:53.8–01:02.3 (8.5s) | L11 | Hỏa lực của gã không phải đạn chì hay thuốc nổ, mà chính là những giọt nước biển được nén áp suất cao, phụt ra từ miệng với độ chính xác đến từng mi-li-mét! |  | Tia nước áp suất cao bắn phụt từ miệng chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) vút lên trời như viên đạn nước phát sáng, cắt ngang mặt nước như đường kiếm laser sắc bén. |
| b12 | 01:02.3–01:09.1 (6.8s) | L12 | Một phát bắn trúng đích đủ sức hất văng một con châu chấu to béo hay một chú nhện bám chặt trên lá cây rơi xuống nước trong nháy mắt! |  | Cảnh tượng ngoạn mục: chú châu chấu béo múp bị tia nước đập văng khỏi cành lá, rơi tự do xoay vòng xuống mặt nước; chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) mở to miệng sẵn sàng đón mồi. |
| b13 | 01:09.1–01:14.0 (4.9s) | L13 | Hôm nay, ban chỉ huy kỹ thuật sẽ cùng giải phẫu toàn diện khẩu súng sinh học này: |  | Phòng giải phẫu cơ học: chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) đứng cạnh mô hình phóng to của chiếc đầu cá trong suốt, tay cầm bút chỉ vào khoang miệng và hệ thống van nén nước. |
| b14 | 01:14.0–01:20.3 (6.3s) | L14 | Làm thế nào một sinh vật sống hoàn toàn dưới nước lại có thể ngắm bắn bách phát bách trúng các mục tiêu di động trên không gian cạn? |  | Ngòi bút vẽ tay đang phác họa tia nước cắt ngang mặt phân cách nước và không khí; một dấu hỏi chấm lớn màu vàng phát sáng tò mò. |

### scene02 · RÃNH CHỮ V VÀ KỸ THUẬT NÉN ĐẠN NƯỚC GIA TỐC ĐUÔI · 99.8s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:05.4 (5.4s) | L15 | Hãy trải bản vẽ kỹ thuật khoang miệng của Thiện Xạ Đầm Lầy lên màn hình phân tích! |  | Bản vẽ thiết kế Blueprint màu xanh thẫm: sơ đồ kỹ thuật khoang miệng của chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) với các đường kích thước ống nòng, góc phun và mũi tên áp lực nước. KHÔNG có chú Cá Cung Thủ trong cảnh này. |
| b02 | 00:05.4–00:10.7 (5.3s) | L16 | Rất nhiều người nghĩ rằng con cá này chỉ đơn giản là ngậm nước vào miệng rồi phun phì phì ra ngoài như trẻ con nghịch |  | Hình ảnh minh họa sai lầm: chú cá ngậm nước phồng má rồi phun nước yếu ớt như đồ chơi bồn tắm trẻ em, bên cạnh là dấu hỏi chấm mỉa mai. KHÔNG có chú Cá Cung Thủ trong cảnh này. |
| b03 | 00:10.7–00:16.7 (6.0s) | L17 | nước. Sai lầm hoàn toàn! Cấu trúc nòng súng của Cá Cung Thủ là một tuyệt tác cơ khí thủy lực đỉnh cao. |  | Mô hình súng phun nước áp lực cao bằng kim loại sáng bóng, các ống dẫn thủy lực đan xen với van tiết lưu áp suất cao. KHÔNG có chú Cá Cung Thủ trong cảnh này. |
| b04 | 00:16.7–00:24.1 (7.4s) | L18 | Ở vòm họng trên của cá có một đường rãnh hình chữ V sâu và hẹp. Khi chuẩn bị khai hỏa, nó áp chặt chiếc lưỡi linh hoạt của mình ép sát vào rãnh chữ V này, |  | Mổ xẻ vòm họng: cận cảnh rãnh chữ V sâu và hẹp trên trần miệng cá; chiếc lưỡi cơ bắp linh hoạt ép chặt vào rãnh chuẩn bị tạo thành nòng súng. KHÔNG có chú Cá Cung Thủ trong cảnh này. |
| b05 | 00:24.1–00:29.9 (5.8s) | L19 | biến khoang miệng thành một chiếc nòng súng ống tròn hoàn hảo có đường kính nòng chỉ vỏn vẹn 0,5mm đến 1mm! | **1 mm** · đường kính nòng · L/380 · [0.3, 0.55] | Cận cảnh đầu ngòi nòng súng: khoang miệng khép kín thành chiếc nòng súng tròn xoe đường kính 1mm, vệt nước bắt đầu được dẫn hướng thẳng tắp chuẩn bị khai hỏa. KHÔNG có chú Cá Cung Thủ trong cảnh này. |
| b06 | 00:29.9–00:39.0 (9.1s) | L20 | Tiếp theo, hai nắp mang khổng lồ đóng sập cực mạnh lại với nhau, nén toàn bộ lượng nước trong khoang miệng và tống vọt ra ngoài qua khe nòng súng với vận tốc lên tới 4-5 m/s! | **4-5 m/s** · vận tốc đạn nước · R/380 · [0.75, 0.55] | Pha nén cơ học: hai nắp mang khổng lồ của chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) phồng to rồi đóng sập lại cực mạnh như hai pít-tông thủy lực, tống tia nước phụt ra với vận tốc 5 m/s kèm đồng hồ đo tốc độ. |
| b07 | 00:39.0–00:45.0 (6.0s) | L21 | Nhưng bí mật kinh hoàng nhất mà các nhà vật lý học thuộc Đại học Bayreuth ở Đức phát hiện ra lại nằm ở động lực học của dòng nước! |  | Tòa nhà Đại học Bayreuth ở Đức và các nhà vật lý học đang theo dõi camera quay chậm ghi lại từng hạt nước chuyển động trong không khí. KHÔNG có chú Cá Cung Thủ trong cảnh này. |
| b08 | 00:45.0–00:53.0 (8.0s) | L22 | Báo cáo chỉ huy, cảm biến tốc độ đo được phần đuôi tia nước bay nhanh hơn phần đầu tới 20%, hai phần nước đang nhập làm một! | **+20% SPD** · gia tốc phần đuôi · L/380 · [0.3, 0.55] | Cô cô trợ lý sóc hoạt hình đeo kính cận to tròn, mặc áo blouse trắng phòng thí nghiệm, cầm thước đo góc quang học chăm chú nhìn vào màn hình máy hiện sóng, chỉ tay vào biểu đồ hiển thị phần đuôi tia nước màu đỏ đang lao nhanh hơn phần đầu màu xanh 20%. |
| b09 | 00:53.0–01:04.3 (11.3s) | L23 | Đây chính là tuyệt kỹ làm chấn động giới cơ học chất lỏng thế giới! Cá Cung Thủ liên tục điều chỉnh chuyển động của khóe miệng trong suốt thời gian bắn kéo dài vài mili-giây, khiến phần nước phun ra sau có vận tốc lớn hơn phần nước phun ra trước. |  | Cận cảnh khóe miệng chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor): miệng cá mở rộng dần đều trong từng mili-giây, làm phần nước phun ra sau nhận lực đẩy mạnh hơn, phóng vút lên không trung xé gió. |
| b10 | 01:04.3–01:08.5 (4.2s) | L68 | Khi bay trên không trung, phần đuôi lao vút lên đuổi kịp và đập dồn vào phần đầu! |  | Pha tăng tốc kỳ diệu: trên không trung, phần đuôi tia nước lao nhanh hơn 20%, đuổi kịp và đập dồn vào phần đầu tạo thành dòng nước cuồn cuộn. |
| b11 | 01:08.5–01:17.4 (9.0s) | L24 | Hiện tượng này biến một tia nước mỏng manh thành một giọt đạn nước khổng lồ cô đặc ngay trước thời điểm chạm mục tiêu! Nhờ đó, động năng và lực va đập tại điểm |  | Pha dồn đạn nước ngoạn mục: trên không trung, phần đuôi nước đập dồn vào phần đầu, tạo thành một quả bóng nước khổng lồ cô đặc ngay trước khi va chạm chú chú bọ ngựa hoạt hình màu xanh lá, hai càng sắc nhọn giương lên đầy tự tin bám trên thân cây trên cành. |
| b12 | 01:17.4–01:25.0 (7.5s) | L25 | tiếp xúc tăng vọt gấp 5-10 lần so với dòng nước bình thường, đủ sức đập văng cả những con bọ ngựa đang găm chặt móng vuốt vào vỏ cây! | **x10 LỰC** · động năng nén tụ · R/380 · [0.75, 0.55] | Lực va chạm bùng nổ: quả cầu nước đập cực mạnh làm vỡ vụn cành lá, chú chú bọ ngựa hoạt hình màu xanh lá, hai càng sắc nhọn giương lên đầy tự tin bám trên thân cây bay tung móng vuốt ngã nhào; đồng hồ đo lực hiển thị va chạm mạnh gấp 10 lần dòng nước thường. |
| b13 | 01:25.0–01:35.3 (10.4s) | L26 | Chưa hết đâu các đồng chí! Hộp tiếp đạn của khẩu súng này cũng thuộc hàng khủng: Cá Cung Thủ có thể bắn liên thanh tới 6-7 phát đạn nước liên tiếp chỉ trong vòng 2 giây mà không cần ngụp xuống nạp lại nước! | **6-7 PHÁT** · bắn liên thanh · L/380 · [0.3, 0.55]<br>**2 GIÂY** · thời gian xả đạn · R/480 · [0.75, 0.55] | Bắn liên thanh đại bác: chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) bắn liên tiếp 6-7 phát đạn nước 'bụp bụp bụp' thành một chuỗi đạn nước bay thẳng hàng lên không trung chỉ trong vòng 2 giây như súng máy tự động. |
| b14 | 01:35.3–01:39.8 (4.5s) | L27 | Mỗi phát bắn đều giữ nguyên hỏa lực chính xác tuyệt đối như một khẩu súng máy tự động dưới nước! |  | Các bia bắn thử nghiệm trên cao: 6-7 hồng tâm lá cây đều bị đạn nước xuyên thủng tâm điểm chính xác 100%, nước bắn tung tóe như súng máy cao xạ. |

### scene03 · BỘ NÃO TỰ ĐỘNG GIẢI ĐỊNH LUẬT KHÚC XẠ SNELL · 96.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:05.8 (5.8s) | L28 | Sở hữu một khẩu đại bác uy lực là một chuyện, nhưng ngắm bắn trúng mục tiêu lại là bài toán khó hơn gấp vạn lần! |  | Bài toán ngắm bắn quang học: mặt phân cách giữa nước và không khí gợn sóng lấp lánh; một tia sáng từ con mồi chiếu xuống bị bẻ gãy góc đột ngột khi chui qua mặt nước. KHÔNG có chú Cá Cung Thủ trong cảnh này. |
| b02 | 00:05.8–00:12.9 (7.1s) | L29 | Và trở ngại chết người mà mọi xạ thủ dưới nước phải đối mặt chính là: Hiện tượng khúc xạ ánh sáng qua ranh giới giữa nước và không khí! |  | Hình ảnh phóng to lăng kính khúc xạ nước: đường đi của ánh sáng bị gãy khúc tại bề mặt phân cách, tạo ra góc lệch lớn đánh lừa thị giác. KHÔNG có chú Cá Cung Thủ trong cảnh này. |
| b03 | 00:12.9–00:19.2 (6.3s) | L30 | Bất kỳ học sinh nào từng học vật lý đều biết định luật bẻ gãy ánh sáng Snell: Ánh sáng truyền từ không khí vào nước sẽ bị bẻ cong một góc đáng kể. |  | Sơ đồ định luật khúc xạ Snell: BÊN TRÁI hình ảnh chú chú nhện con hoạt hình nhiều mắt ngơ ngác, lông xù màu nâu, đeo ba lô tí hon bám trên lá cây thực tế trên cành; BÊN PHẢI hình ảnh bóng mờ ảo của chú nhện bị lệch đi một góc lớn do ánh sáng bị bẻ cong. KHÔNG có chú Cá Cung Thủ trong cảnh này. |
| b04 | 00:19.2–00:25.2 (6.1s) | L31 | Do đó, vị trí mà đôi mắt cá nhìn thấy chỉ là một ảnh ảo lơ lửng, lệch hẳn so với vị trí thực tế của con mồi trên cành cây! |  | Mô phỏng tầm nhìn sai lệch: hình ảnh con nhện ảo trôi nổi phía trên cành cây, mũi tên chỉ rõ khoảng cách sai số giữa vị trí thực và vị trí ảo. KHÔNG có chú Cá Cung Thủ trong cảnh này. |
| b05 | 00:25.2–00:32.1 (6.9s) | L32 | Nếu bạn bắn thẳng vào vị trí bạn nhìn thấy, viên đạn nước chắc chắn sẽ bay chệch lên trời và con mồi sẽ ung dung bay mất. |  | Minh họa bắn trượt: một viên đạn nước bắn thẳng vào ảnh ảo bị bay vút lên trời chệch mục tiêu; bên cạnh là chú nhện ung dung vẫy tay chào mỉa mai. KHÔNG có chú Cá Cung Thủ trong cảnh này. |
| b06 | 00:32.1–00:40.6 (8.4s) | L33 | Nhưng bộ não của Thiện Xạ Đầm Lầy chỉ nặng chưa đầy không phẩy một gam lại có thể giải bài toán lượng giác khúc xạ phức tạp này trong vòng chưa đầy 50 mili-giây! | **50 ms** · tính toán khúc xạ · L/380 · [0.3, 0.55] | Bộ vi xử lý lượng giác sinh học: bộ não tí hon của chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) phát sáng các vi mạch thuật toán giải phương trình sin khúc xạ chỉ trong vòng 50 mili-giây. |
| b07 | 00:40.6–00:48.3 (7.8s) | L34 | Alo các bác xạ thủ ơi, em đứng trên cành nghiêng 45° thế này mà tia nước bắn trúng ngay giữa trán là sao? |  | Chú chú nhện con hoạt hình nhiều mắt ngơ ngác, lông xù màu nâu, đeo ba lô tí hon bám trên lá cây bám trên cành nghiêng 45 độ, ôm đầu ngơ ngác khi tia nước bắn trúng ngay đỉnh đầu, chiếc ba lô tí hon văng ra ngoài trong ngỡ ngàng. |
| b08 | 00:48.3–00:59.8 (11.5s) | L35 | Đúng như chú nhện con ngơ ngác vừa ôm đầu kêu trời! Để giảm thiểu tối đa sai số khúc xạ, Cá Cung Thủ thường bơi tới vị trí gần vuông góc dưới mục tiêu, tạo góc bắn từ 70° đến 80° so với mặt nước. | **70°-80°** · góc ngắm chuẩn · L/380 · [0.3, 0.55] | Chiến thuật định vị góc bắn: chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) bơi vào vị trí tạo góc ngắm tối ưu 70°-80° gần vuông góc mặt nước, sẵn sàng ngắm chuẩn. |
| b09 | 00:59.8–01:08.0 (8.1s) | L69 | Nhưng ngay cả khi bị ép bắn ở góc nghiêng 45°, tỷ lệ bắn trúng mục tiêu ngay trong phát đạn đầu tiên của gã vẫn đạt tới 90 đến 95%! | **95% HIT** · độ chính xác · R/380 · [0.75, 0.55] | Thử thách góc nghiêng cực hạn: cá bị ép bắn ở góc nghiêng 45° so với mặt nước, tia nước vẫn vút trúng đích với độ chính xác 95%. |
| b10 | 01:08.0–01:20.5 (12.5s) | L36 | Đôi mắt to tròn của cá có cấu tạo nhãn cầu đặc biệt với hai trục quang học độc lập, vừa giúp bù trừ tự động độ cong mặt nước, vừa tạo ra tầm nhìn lập thể ba chiều cực kỳ sắc bén xuyên qua lớp gương phản chiếu của mặt hồ! |  | Đặc tả đôi mắt chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor): nhãn cầu lớn màu vàng với 2 trục quang học độc lập xoay chuyển linh hoạt, xuyên qua lớp gương phản xạ mặt nước để tạo tầm nhìn 3D sắc bén. |
| b11 | 01:20.5–01:30.8 (10.3s) | L37 | Thậm chí võng mạc của nó còn sở hữu các tế bào cảm quang chuyên biệt có khả năng lọc sạch ánh sáng lóa mặt trời và bóc tách các vệt màu ngụy trang của bầy côn trùng ẩn nấp sau kẽ lá xanh! |  | Võng mạc siêu cảm biến: các tế bào cảm quang chuyên biệt trong mắt cá tự động lọc sạch ánh sáng lóa mặt trời và bóc tách màu ngụy trang của bầy côn trùng. |
| b12 | 01:30.8–01:36.0 (5.3s) | L70 | Một hệ thống kính ngắm quang học hồng ngoại sinh học đỉnh cao mà các nhà thiết kế vũ khí hiện đại phải ghen tị! |  | Kính ngắm hồng ngoại sinh học: giao diện nhìn từ mắt cá với các đường lưới ngắm màu xanh neon, đánh dấu đỏ vào mục tiêu ngụy trang trong kẽ lá. |

### scene04 · TÂN BINH BẮN HỤT TRĂM PHÁT VÀ NĂNG LỰC HỌC TẬP · 90.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:06.6 (6.6s) | L38 | Nhiều người lầm tưởng khả năng bắn tỉa thần sầu này là bản năng bẩm sinh được lập trình sẵn trong gen của Cá Cung Thủ. |  | Trường bắn tân binh dưới đáy sông: các chú cá cung thủ non bé xíu xếp hàng ngay ngắn, phía trên là các cành cây có gắn bia tập bắn bằng lá tròn. KHÔNG có chú Cá Cung Thủ trong cảnh này. |
| b02 | 00:06.6–00:14.2 (7.6s) | L39 | Nghiên cứu thực nghiệm chấn động của các nhà khoa học đã chứng minh điều ngược lại: Đây là một kỹ năng quân sự bắt buộc phải trải qua rèn luyện gian khổ! |  | Phòng thí nghiệm nghiên cứu động vật: các nhà khoa học ghi chép sổ nhật ký theo dõi quá trình tập bắn từ thuở sơ sinh của bầy cá. KHÔNG có chú Cá Cung Thủ trong cảnh này. |
| b03 | 00:14.2–00:24.9 (10.7s) | L40 | Bản tin huấn luyện từ trường bắn tân binh: Những chú cá non mới nở chỉ có thể bắn ra những tia nước yếu ớt xa vài centimet, và chúng bắn trượt tới 99% số mục tiêu trong những tuần đầu đời! | **99% TRƯỢT** · tân binh mới nở · L/380 · [0.3, 0.55] | Loa phát thanh quân sự: bảng kết quả tập bắn ghi dòng chữ 'BẮN TRƯỢT 99%'; một chú cá non bắn tia nước phì ra được 2cm rồi rơi tõm xuống nước mặt méo xẹo. KHÔNG có chú Cá Cung Thủ trong cảnh này. |
| b04 | 00:24.9–00:27.8 (2.9s) | L41 | Đúng là cảnh tượng bi hài của trường bắn quân sự! |  | Hình ảnh huấn luyện gian khổ: chú cá non kiên trì bắn hàng trăm phát đạn nước liên tục, não bộ vẽ các đường vòng cung hiệu chỉnh góc ngẩng dần đều. |
| b05 | 00:27.8–00:36.0 (8.2s) | L42 | Cá cung thủ non phải trải qua hàng ngàn lần thử và sai, tự rút kinh nghiệm sau mỗi cú bắn lệch để não bộ dần dần học cách bù trừ góc khúc xạ theo cự ly thực tế. |  | Biểu đồ tiến bộ kỹ năng: đường cong học tập đi lên dốc đứng theo số ngày rèn luyện, các tia nước bắn ngày càng xa và trúng đích nhiều hơn. |
| b06 | 00:36.0–00:44.2 (8.2s) | L43 | Nhưng điều làm kinh ngạc giới nghiên cứu hành vi động vật là phát hiện công bố trên tạp chí Nature: Cá Cung Thủ sở hữu năng lực học tập xã hội đỉnh cao! |  | Tạp chí Nature danh giá: trang bìa Nature mở ra hình ảnh một chú cá non đang bơi sát cạnh chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) kỳ cựu, chăm chú quan sát đàn anh ngắm bắn chuẩn xác. |
| b07 | 00:44.2–00:55.4 (11.2s) | L44 | Một con cá non nếu được bơi cạnh những xạ thủ kỳ cựu dày dặn kinh nghiệm chỉ cần đứng quan sát đàn anh bắn mồi vài lần là có thể tự điều chỉnh góc bắn của mình chuẩn xác hơn gấp nhiều lần mà không cần tự mình thử sai! |  | Cảnh học hỏi đàn anh: chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) giương vây bắn mẫu một phát đạn nước trúng đích, chú cá non bơi bên cạnh mở to mắt ngưỡng mộ và bắt chước tư thế ngắm bắn. |
| b08 | 00:55.4–01:05.5 (10.1s) | L45 | Khả năng quan sát, phân tích đường đạn của đồng loại rồi mô phỏng lại trong não bộ là một năng lực nhận thức cấp cao mà trước đây người ta ngỡ chỉ có ở các loài linh trưởng và con người! |  | Mô phỏng năng lực nhận thức xã hội: sơ đồ sóng não từ chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) truyền cảm hứng mô phỏng sang chú cá non, giúp tân binh bắn trúng ngay bia tập chỉ sau một lần quan sát. |
| b09 | 01:05.5–01:10.5 (5.1s) | L71 | Một minh chứng hùng hồn cho thấy trí tuệ của loài cá vượt xa những định kiến nông cạn thường thấy. |  | Biểu tượng trí tuệ vượt bậc: chú Cá Cung Thủ hoạt hình tỏa sáng rực rỡ với vương miện trí tuệ, đập tan định kiến thông thường về loài cá. |
| b10 | 01:10.5–01:20.9 (10.4s) | L46 | Để kiểm chứng điều này, giáo sư Schuster tại Đức đã thiết lập một thí nghiệm độc lạ: Ông chiếu các điểm sáng nhân tạo di động trên màn hình máy tính với vận tốc thay đổi liên tục. |  | Thí nghiệm của GS Stefan Schuster: một màn hình máy tính chiếu điểm sáng di động, chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) tính toán trước quỹ đạo và bắn tia nước đón đầu trúng phóc điểm sáng trên màn hình. |
| b11 | 01:20.9–01:30.5 (9.6s) | L47 | Chỉ sau vài lượt thử, bầy Cá Cung Thủ đã tự tính toán được quy luật chuyển động và bắn đón đầu mục tiêu ảo cực kỳ chính xác! Một tư duy tác chiến bắn chặn ngang tầm tên lửa phòng không! |  | Màn hình máy tính hiển thị điểm 'TARGET DESTROYED': điểm sáng ảo vừa xuất hiện đã bị tia nước bắn hạ gục; các nhà khoa học vỗ tay kinh ngạc. |

### scene05 · TÍNH QUỸ ĐẠO RƠI TRONG 100MS VÀ CÚ NHẢY NGOẠM MỒI · 94.1s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:04.4 (4.4s) | L48 | Bắn trúng con mồi rớt khỏi cành lá mới chỉ là một nửa chặng đường của chiến dịch săn mồi. |  | Chiến trường cạnh tranh khốc liệt: con côn trùng vừa bị bắn rơi khỏi lá, xung quanh nhiều chú cá khác trong bầy đang giương mắt thèm thuồng chuẩn bị lao vào cướp mồi. KHÔNG có chú Cá Cung Thủ trong cảnh này. |
| b02 | 00:04.4–00:15.0 (10.6s) | L49 | Trong thế giới đầm lầy cạnh tranh khốc liệt, bắn trúng mà không đớp kịp thì miếng ăn sẽ rơi ngay vào miệng đối thủ bên cạnh! Và đây là lúc bộ vi xử lý đạn đạo của Thiện Xạ Đầm Lầy phát huy uy lực tối đa. |  | Cảnh tượng bầy cá đói bụng há miệng chực chờ dưới mặt nước, mắt lăm lăm nhìn con mồi đang rơi lơ lửng. KHÔNG có chú Cá Cung Thủ trong cảnh này. |
| b03 | 00:15.0–00:26.3 (11.3s) | L50 | Ngay khoảnh khắc tia nước vừa rời khỏi khóe miệng trong vòng chưa đầy 100 mili-giây, Cá Cung Thủ đã tính toán xong toàn bộ phương trình parabol đường rơi của con mồi: Nó biết chính xác vị trí và thời điểm con côn trùng sẽ tiếp nước! | **100 ms** · tính điểm rơi · L/380 · [0.3, 0.55] | Bộ xử lý đạn đạo siêu tốc: đường parabol màu vàng vẽ từ vị trí con bọ rơi xuống mặt nước, đồng hồ bấm giờ tính toán dừng ở mốc 100 mili-giây. KHÔNG có chú Cá Cung Thủ trong cảnh này. |
| b04 | 00:26.3–00:36.1 (9.8s) | L51 | Không cần đợi nhìn thấy con mồi rơi tới đâu, con cá lập tức bật chế độ bơi nước rút với tốc độ xé nước, lao thẳng tới đúng tọa độ tiếp nhận trước khi con mồi chạm mặt nước chỉ trong 0,1 giây! | **0,1 GIÂY** · bơi nước rút · R/380 · [0.75, 0.55] | Pha bơi nước rút thần tốc: chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) bật vây bơi vút như quả ngư lôi xé toạc mặt nước, há rộng miệng đón lõng ngay vị trí con mồi chạm nước chỉ trong 0,1 giây. |
| b05 | 00:36.1–00:41.1 (4.9s) | L52 | Một pha đoán đầu đường đạn thần tốc khiến mọi đối thủ xung quanh chỉ biết đứng nhìn trong bất lực! |  | chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) đớp gọn con mồi đúng 0,1 giây khi vừa chạm mặt nước; xung quanh các chú cá đối thủ thắng gấp tạo vệt nước xoáy bất lực. |
| b06 | 00:41.1–00:47.5 (6.5s) | L53 | Cuộc đua cướp mồi trong bầy đàn khốc liệt đến mức 3-4 đối thủ bơi bên cạnh cũng lập tức tính toán điểm rơi để lao vào tranh cướp! | **3-4 CON** · lao vào tranh cướp · L/380 · [0.25, 0.55] | Cuộc đua bầy đàn náo loạn: 3-4 chú cá đối thủ cùng lao tới từ các hướng tạo sóng cuồn cuộn, nhưng chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) đã nhanh chân đớp gọn con mồi trước mũi đối thủ trong gang tấc. |
| b07 | 00:47.5–00:55.4 (7.9s) | L54 | Nếu tay súng chính chỉ cần chậm trễ 0,1 giây trong pha bơi nước rút, con mồi do chính mình tốn công bắn hạ sẽ biến mất tăm vào dạ dày của kẻ cơ hội đứng xem! |  | Hình ảnh minh họa đối thủ cướp mồi: con mồi rơi ngay sát miệng kẻ cơ hội bơi chậm 0,1s, chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) phóng vụt qua nẫng tay trên trong tích tắc. |
| b08 | 00:55.4–01:02.2 (6.7s) | L55 | Tôi bắn tỉa trong quân đội cả đời mà nhìn pha tính toán đạn đạo của chú cá này cũng phải ngả mũ chào thua! |  | Chú xạ thủ quân đội lực lưỡng mặc quân phục rằn ri ngả mũ kính phục, giơ ngón tay cái tán thưởng chiếc camera quay cảnh tính toán đạn đạo của cá. |
| b09 | 01:02.2–01:12.1 (9.9s) | L56 | Thậm chí Thiện Xạ Đầm Lầy còn trang bị một phương án tác chiến dự phòng cực kỳ thực dụng: Nếu con mồi đậu ở cành lá quá thấp dưới 30cm, gã sẽ không thèm tốn một giọt nước nào! | **30 cm** · nhảy không đối không · R/380 · [0.75, 0.55] | Phương án tác chiến cận chiến: mục tiêu ở cành lá thấp 30cm, chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) ngưng hỏa lực nước, co vây đuôi tích lũy động năng. |
| b10 | 01:12.1–01:20.8 (8.7s) | L57 | Con cá chỉ cần quẫy mạnh chiếc đuôi vây khỏe khoắn, phóng vút toàn bộ cơ thể bay lên khỏi mặt nước như một chiếc tên lửa mini để ngoạm gọn con mồi ngay trên không trung! |  | Cú nhảy không kích ngoạn mục: chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) phóng vút toàn bộ cơ thể bay lên khỏi mặt nước 30cm như tên lửa mini ngoạm trọn con mồi trên không trung. |
| b11 | 01:20.8–01:34.1 (13.3s) | L58 | Tuy nhiên, cỗ máy săn mồi hoàn hảo này cũng có những tử huyệt kỹ thuật: Khi trời nổi gió to làm mặt nước dậy sóng cuồn cuộn hoặc khi váng dầu ô nhiễm che phủ mặt sông, thuật toán quang học bị nhiễu loạn hoàn toàn, biến tay súng cừ khôi thành một kẻ bắn trượt đáng thương! |  | Tử huyệt thời tiết: mặt nước gió to nổi sóng dập dềnh cuồn cuộn, chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) ngắm bắn bị sóng làm méo hình ảnh, tia nước bắn chệch cành lá làm con mồi bay mất vẻ mặt tiếc nuối. |

### scene06 · BÀI HỌC ĐỘ CHÍNH XÁC VÀ BÓNG ĐEN WOLVERINE 860V TẬP SAU · 80.3s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.7 (9.7s) | L59 | Báo cáo tổng kết thử nghiệm kỹ thuật số 20: Cá Cung Thủ chứng minh cho chúng ta thấy rằng sức mạnh hủy diệt không nhất thiết phải đến từ kích thước cơ bắp đồ sộ hay vũ khí hủy diệt hàng loạt. |  | Bảng tổng kết đánh giá kỹ thuật số 20: biểu đồ sao radar với các chỉ số: Độ chính xác 95%, Tầm bắn 3m, Thời gian tính toán 50ms; chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) đứng trên bục chào quân sự nghiêm trang. |
| b02 | 00:09.7–00:17.2 (7.6s) | L60 | Sự am hiểu quy luật tự nhiên, khả năng tính toán chuẩn xác và tinh thần học hỏi không ngừng mới là chìa khóa vạn năng để sinh tồn và làm chủ cuộc chơi. |  | Hình ảnh triết lý thiên nhiên: đại dương bao la với những sinh vật khổng lồ bơi qua, nhưng tâm điểm ánh sáng chiếu vào chú chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) bé nhỏ phát sáng rực rỡ với khẩu đại bác uy lực. |
| b03 | 00:17.2–00:24.9 (7.6s) | L61 | Chính cơ chế nén dòng nước gia tốc đuôi của loài cá này đang là nguồn cảm hứng vô giá để các kỹ sư hàng không vũ trụ và công nghệ in ba chiều hiện đại |  | Nguồn cảm hứng vô giá: các kỹ sư hàng không vũ trụ và in 3D hiện đại say sưa nghiên cứu cơ chế đẩy dòng nước của Cá Cung Thủ trên bàn thiết kế. KHÔNG có chú Cá Cung Thủ trong cảnh này. |
| b04 | 00:24.9–00:32.5 (7.6s) | L72 | thiết kế ra những vòi phun hạt siêu vi mô có độ chính xác tuyệt đối mà không cần sử dụng bất kỳ pít-tông cơ học phức tạp nào! |  | Ứng dụng công nghệ tương lai: BÊN TRÁI vòi phun vi mô động cơ phản lực chất lỏng; BÊN PHẢI đầu in 3D sinh học siêu chính xác mô phỏng cơ chế gia tốc tia nước của Cá Cung Thủ. KHÔNG có chú Cá Cung Thủ trong cảnh này. |
| b05 | 00:32.5–00:43.8 (11.4s) | L62 | Bạn khâm phục điều gì nhất ở Thiện Xạ Đầm Lầy Cá Cung Thủ: Khẩu đại bác nén đạn nước gia tốc đuôi, hay bộ não giải định luật khúc xạ ánh sáng trong chớp mắt? Hãy để lại ý kiến bình luận của đội kỹ thuật bên dưới nhé! | **ĐẠI BÁC** · đạn nước gia tốc · L/380 · [0.25, 0.55]<br>**BỘ NÃO** · giải khúc xạ quang học · R/480 · [0.75, 0.55] | Khung bình luận tương tác: chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) cầm micro hướng về người xem, bên cạnh là hai ô lựa chọn: 'ĐẠI BÁC NÉN ĐẠN NƯỚC' và 'BỘ NÃO GIẢI KHÚC XẠ 50ms' kèm dấu hỏi chấm to lớn. |
| b06 | 00:43.8–00:54.3 (10.5s) | L63 | Và bây giờ, hãy hướng ngòi bút về phân cảnh kết thúc bí ẩn! Trong tập tiếp theo, chúng ta sẽ rời xa những cánh rừng ngập mặn châu Á để thâm nhập vào vùng rừng nhiệt đới âm u của lục địa đen Châu Phi. |  | Chuyển cảnh rừng rậm châu Phi: ngòi bút vẽ tay phác thảo khu rừng mưa nhiệt đới sương mù mờ ảo, những thân cây rêu phong cổ thụ bí ẩn. KHÔNG có chú Cá Cung Thủ trong cảnh này. |
| b07 | 00:54.3–00:56.6 (2.2s) | L64 | Hãy chiêm ngưỡng một bóng đen bí ẩn vô cùng kỳ dị! |  | BÓNG ĐEN BÍ ẨN TẬP TIẾP THEO (TASTE-68): một bóng đen tuyền hình chú ếch nhỏ bé kỳ dị trong bóng tối, từ đầu ngón chân phát ra những tia sáng kim loại sắc nhọn kèm dấu hỏi chấm khổng lồ. KHÔNG có chú Cá Cung Thủ trong cảnh này. |
| b08 | 00:56.6–01:01.4 (4.9s) | L65 | Một sinh vật lưỡng cư nhỏ bé, nhưng sở hữu cơ chế tự vệ được đánh giá là điên rồ và đau đớn nhất hành |  | Bóng đen chú ếch nhỏ bé giương mắt đỏ rực giữa đêm tối rậm rạp sương mù, thân mình phủ lớp lông gai mờ ảo đầy đe dọa. KHÔNG có chú Cá Cung Thủ trong cảnh này. |
| b09 | 01:01.4–01:13.6 (12.2s) | L66 | tinh: Khi bị kẻ săn mồi dồn vào chân tường, nó sẽ chủ động tự co thắt cơ bắp bẻ gãy chính đốt xương ngón chân của mình, đâm thủng lớp da thịt ra ngoài để tạo thành một bộ móng vuốt sắc nhọn như dao găm hệt như dị nhân Wolverine trong truyện tranh! |  | Cận cảnh bộ vuốt sắc nhọn: xương ngón chân tự đâm xuyên qua da thịt tạo thành 3 chiếc móng vuốt dài nhọn hoắt như móng vuốt Người Sói Wolverine giương lên thách thức kẻ thù. KHÔNG có chú Cá Cung Thủ trong cảnh này. |
| b10 | 01:13.6–01:20.3 (6.7s) | L67 | Đố các chuyên viên kỹ thuật biết danh tính của sát thủ tự bẻ xương kỳ lạ này là ai? Hãy viết ngay câu trả lời của bạn dưới phần bình luận nhé! |  | Khung hình tò mò kêu gọi bình luận: bóng đen chú ếch móng vuốt Wolverine bí ẩn dưới ánh trăng rọi, dấu hỏi chấm to vàng phát sáng '?', kêu gọi khán giả đoán tên con vật bên dưới. KHÔNG có chú Cá Cung Thủ trong cảnh này. |

## 5. Phân cảnh Shorts — từng beat

Banner: **BẮN TỈA 3 MÉT: / GIẢI ĐỊNH LUẬT VẬT LÝ!** · giọng 50.8s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Cảnh báo xạ thủ bắn tỉa! |  |
| s02 | 00:02.4 | S02 | Bạn có tin một con cá dưới nước lại có thể ngắm bắn bách phát bách trúng các mục tiêu đậu trên cành cây cao tới 2m? | **2 MÉT** · tầm bắn trên cạn · R/620 · [0.75, 0.55] |
| s03 | 00:07.8 | S03 | Đây là Cá Cung Thủ, tay súng bắn tỉa cừ khôi của các rạn rừng ngập mặn! |  |
| s04 | 00:11.9 | S04 | Thứ nhất, vòm họng của nó có rãnh chữ V ép chặt với lưỡi, tạo thành chiếc nòng súng tí |  |
| s05 | 00:16.6 | S05 | hon nén tia nước bắn xa kỷ lục tới 3m! | **3 MÉT** · tầm bắn kỷ lục · R/620 · [0.75, 0.55] |
| s06 | 00:18.8 | S06 | Thứ hai, phần đuôi tia nước bay nhanh hơn phần |  |
| s07 | 00:21.1 | S07 | đầu, đập dồn lại thành một giọt đạn nước khổng lồ làm tăng lực va đập gấp 10 lần để hạ gục con mồi! | **x10 LỰC** · động năng nén tụ · L/620 · [0.25, 0.55] |
| s08 | 00:26.6 | S08 | Thứ ba, mặt nước luôn bẻ cong ánh sáng theo định luật khúc xạ, |  |
| s09 | 00:29.7 | S09 | nhưng bộ não của loài cá này giải bài toán quang học chỉ trong 50 mili-giây để bắn chính xác tới 95%! | **50 ms** · giải khúc xạ Snell · L/620 · [0.25, 0.55]<br>**95% HIT** · độ chính xác · R/720 · [0.75, 0.55] |
| s10 | 00:36.1 | S10 | Chưa hết, nó còn tính toán trước điểm rơi đạn |  |
| s11 | 00:39.5 | S11 | đạo để bơi nước rút cướp mồi trước đối thủ chỉ trong 0,1 giây! | **0,1 GIÂY** · bơi nước rút · R/620 · [0.75, 0.55] |
| s12 | 00:42.9 | S12 | Độ chính xác và khả năng thích nghi phi thường, |  |
| s13 | 00:45.4 | S13 | đó chính là vũ khí tối thượng giúp Thiện Xạ Đầm Lầy thống trị cả hai thế giới dưới nước và trên cạn! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo thử nghiệm vũ khí tối mật số 20.". Bố cục: Phòng phân tích tác chiến quân sự: một hồ sơ mật đóng dấu đỏ thẫm 'BÁO CÁO THỬ NGHIỆM SỐ 20' đặt giữa bàn kim loại, màn hình phía sau hiển thị hình ảnh rừng đước ngập mặn rậm rạp. KHÔNG có chú Cá Cung Thủ trong cảnh này.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn đội kỹ thuật hãy khóa mục tiêu và khởi động camera tốc độ cao!". Bố cục: Bảng điều khiển công nghệ cao: các kỹ sư khởi động camera tốc độ cao và màn hình hiển thị thước ngắm hồng ngoại đang khóa mục tiêu. KHÔNG có chú Cá Cung Thủ trong cảnh này.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiến trường mà chúng ta khảo sát hôm nay không phải bầu trời rực lửa hay pháo đài thép kiên cố, mà là những rặng đước ngập mặn tĩnh lặng vùng Đông Nam Á.". Bố cục: Rừng đước ngập mặn Đông Nam Á kỳ bí: rễ cây đước ngoằn ngoèo rủ xuống mặt nước phẳng lặng như gương; tia nắng ban mai xuyên qua kẽ lá mờ ảo. KHÔNG có chú Cá Cung Thủ trong cảnh này.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nơi một sát thủ thầm lặng đang nằm phục kích ngay sát mặt nước!". Bố cục: Góc phục kích bí mật: sát mặt nước đục mờ, đôi mắt to lồi màu vàng của chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) nhô lên nhẹ nhàng không làm xao động một gợn sóng, kính ngắm laser đỏ phát sáng dò tìm mục tiêu.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhân vật đứng trước ống kính của chúng ta hôm nay có chiều dài cơ thể khiêm tốn chỉ từ 15-20cm,". Bố cục: Chân dung oai phong: chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) bơi giữa làn nước trong xanh, thân hình vảy bạc ánh kim sọc đen quân sự, chiếc mũ beret đen kiêu hãnh, vây lưng bơi lượn điệu nghệ.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "khoác lên mình bộ vảy màu bạc ánh kim cùng những sọc đen quân sự sắc sảo. Nhưng đừng để kích thước nhỏ bé này đánh lừa mắt thường!". Bố cục: Cận cảnh bộ giáp vảy bạc sọc đen quân sự tinh xảo của chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor), ánh kim loại lấp lánh dưới làn nước trong vắt, vây ngực chuyển động uyển chuyển.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong giới quân sự tự nhiên, gã được phong tặng danh hiệu Thiện Xạ Đầm Lầy, hay còn gọi là Cá Cung Thủ!". Bố cục: Tấm huy hiệu quân đội danh dự: chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) đứng trên bục danh dự vàng khắc dòng chữ 'THIỆN XẠ ĐẦM LẦY', vây trước chắp tay nghiêm trang, kính ngắm laser nhấp nháy chữ 'LOCKED'.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quy tắc tác chiến của loài cá thông thường là: Muốn ăn thì phải chờ con mồi sảy chân rơi xuống nước.". Bố cục: Hình ảnh so sánh hài hước: BÊN TRÁI một chú cá thường ngửa bụng há họng chờ thức ăn rơi xuống bị gạch chéo đỏ; BÊN PHẢI chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) ngẩng cao đầu giương vây đầy khí phách chiến đấu.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng Thiện Xạ Đầm Lầy của chúng ta thì tuyệt đối không có khái niệm ăn xin lòng thương hại!". Bố cục: chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) bơi ngẩng cao đầu sát mặt nước, ánh mắt sắc lẹm kiên quyết, biểu tượng nắm đấm sắt tự lực cánh sinh phát sáng bên cạnh.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu con mồi đậu trên cành lá cao tới 1,5m, 2m, thậm chí kỷ lục lên tới 3m, gã sẽ tự tay phóng hỏa lực lên trời để kéo con mồi rơi thẳng xuống miệng!". Bố cục: Thước đo cự ly bắn tỉa trên không: BÊN TRÁI chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) nằm sát mặt nước, tia ngắm laser đỏ hướng thẳng lên cành lá cao 2m có chú chú nhện con hoạt hình nhiều mắt ngơ ngác, lông xù màu nâu, đeo ba lô tí hon bám trên lá cây đang đậu, thước đo đánh dấu các vạch 1,5m, 2m và kỷ lục 3m.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hỏa lực của gã không phải đạn chì hay thuốc nổ, mà chính là những giọt nước biển được nén áp suất cao, phụt ra từ miệng với độ chính xác đến từng mi-li-mét!". Bố cục: Tia nước áp suất cao bắn phụt từ miệng chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) vút lên trời như viên đạn nước phát sáng, cắt ngang mặt nước như đường kiếm laser sắc bén.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một phát bắn trúng đích đủ sức hất văng một con châu chấu to béo hay một chú nhện bám chặt trên lá cây rơi xuống nước trong nháy mắt!". Bố cục: Cảnh tượng ngoạn mục: chú châu chấu béo múp bị tia nước đập văng khỏi cành lá, rơi tự do xoay vòng xuống mặt nước; chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) mở to miệng sẵn sàng đón mồi.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hôm nay, ban chỉ huy kỹ thuật sẽ cùng giải phẫu toàn diện khẩu súng sinh học này:". Bố cục: Phòng giải phẫu cơ học: chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) đứng cạnh mô hình phóng to của chiếc đầu cá trong suốt, tay cầm bút chỉ vào khoang miệng và hệ thống van nén nước.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Làm thế nào một sinh vật sống hoàn toàn dưới nước lại có thể ngắm bắn bách phát bách trúng các mục tiêu di động trên không gian cạn?". Bố cục: Ngòi bút vẽ tay đang phác họa tia nước cắt ngang mặt phân cách nước và không khí; một dấu hỏi chấm lớn màu vàng phát sáng tò mò.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy trải bản vẽ kỹ thuật khoang miệng của Thiện Xạ Đầm Lầy lên màn hình phân tích!". Bố cục: Bản vẽ thiết kế Blueprint màu xanh thẫm: sơ đồ kỹ thuật khoang miệng của chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) với các đường kích thước ống nòng, góc phun và mũi tên áp lực nước. KHÔNG có chú Cá Cung Thủ trong cảnh này.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Rất nhiều người nghĩ rằng con cá này chỉ đơn giản là ngậm nước vào miệng rồi phun phì phì ra ngoài như trẻ con nghịch nước.". Bố cục: Hình ảnh minh họa sai lầm: chú cá ngậm nước phồng má rồi phun nước yếu ớt như đồ chơi bồn tắm trẻ em, bên cạnh là dấu hỏi chấm mỉa mai. KHÔNG có chú Cá Cung Thủ trong cảnh này.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sai lầm hoàn toàn! Cấu trúc nòng súng của Cá Cung Thủ là một tuyệt tác cơ khí thủy lực đỉnh cao.". Bố cục: Mô hình súng phun nước áp lực cao bằng kim loại sáng bóng, các ống dẫn thủy lực đan xen với van tiết lưu áp suất cao. KHÔNG có chú Cá Cung Thủ trong cảnh này.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở vòm họng trên của cá có một đường rãnh hình chữ V sâu và hẹp. Khi chuẩn bị khai hỏa, nó áp chặt chiếc lưỡi linh hoạt của mình ép sát vào rãnh chữ V này,". Bố cục: Mổ xẻ vòm họng: cận cảnh rãnh chữ V sâu và hẹp trên trần miệng cá; chiếc lưỡi cơ bắp linh hoạt ép chặt vào rãnh chuẩn bị tạo thành nòng súng. KHÔNG có chú Cá Cung Thủ trong cảnh này.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "biến khoang miệng thành một chiếc nòng súng ống tròn hoàn hảo có đường kính nòng chỉ vỏn vẹn 0,5mm đến 1mm!". Bố cục: Cận cảnh đầu ngòi nòng súng: khoang miệng khép kín thành chiếc nòng súng tròn xoe đường kính 1mm, vệt nước bắt đầu được dẫn hướng thẳng tắp chuẩn bị khai hỏa. KHÔNG có chú Cá Cung Thủ trong cảnh này.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tiếp theo, hai nắp mang khổng lồ đóng sập cực mạnh lại với nhau, nén toàn bộ lượng nước trong khoang miệng và tống vọt ra ngoài qua khe nòng súng với vận tốc lên tới 4-5 m/s!". Bố cục: Pha nén cơ học: hai nắp mang khổng lồ của chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) phồng to rồi đóng sập lại cực mạnh như hai pít-tông thủy lực, tống tia nước phụt ra với vận tốc 5 m/s kèm đồng hồ đo tốc độ.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng bí mật kinh hoàng nhất mà các nhà vật lý học thuộc Đại học Bayreuth ở Đức phát hiện ra lại nằm ở động lực học của dòng nước!". Bố cục: Tòa nhà Đại học Bayreuth ở Đức và các nhà vật lý học đang theo dõi camera quay chậm ghi lại từng hạt nước chuyển động trong không khí. KHÔNG có chú Cá Cung Thủ trong cảnh này.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo chỉ huy, cảm biến tốc độ đo được phần đuôi tia nước bay nhanh hơn phần đầu tới 20%, hai phần nước đang nhập làm một!". Bố cục: Cô cô trợ lý sóc hoạt hình đeo kính cận to tròn, mặc áo blouse trắng phòng thí nghiệm, cầm thước đo góc quang học chăm chú nhìn vào màn hình máy hiện sóng, chỉ tay vào biểu đồ hiển thị phần đuôi tia nước màu đỏ đang lao nhanh hơn phần đầu màu xanh 20%.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây chính là tuyệt kỹ làm chấn động giới cơ học chất lỏng thế giới! Cá Cung Thủ liên tục điều chỉnh chuyển động của khóe miệng trong suốt thời gian bắn kéo dài vài mili-giây, khiến phần nước phun ra sau có vận tốc lớn hơn phần nước phun ra trước.". Bố cục: Cận cảnh khóe miệng chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor): miệng cá mở rộng dần đều trong từng mili-giây, làm phần nước phun ra sau nhận lực đẩy mạnh hơn, phóng vút lên không trung xé gió.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hiện tượng này biến một tia nước mỏng manh thành một giọt đạn nước khổng lồ cô đặc ngay trước thời điểm chạm mục tiêu! Nhờ đó, động năng và lực va đập tại điểm tiếp xúc". Bố cục: Pha dồn đạn nước ngoạn mục: trên không trung, phần đuôi nước đập dồn vào phần đầu, tạo thành một quả bóng nước khổng lồ cô đặc ngay trước khi va chạm chú chú bọ ngựa hoạt hình màu xanh lá, hai càng sắc nhọn giương lên đầy tự tin bám trên thân cây trên cành.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tăng vọt gấp 5-10 lần so với dòng nước bình thường, đủ sức đập văng cả những con bọ ngựa đang găm chặt móng vuốt vào vỏ cây!". Bố cục: Lực va chạm bùng nổ: quả cầu nước đập cực mạnh làm vỡ vụn cành lá, chú chú bọ ngựa hoạt hình màu xanh lá, hai càng sắc nhọn giương lên đầy tự tin bám trên thân cây bay tung móng vuốt ngã nhào; đồng hồ đo lực hiển thị va chạm mạnh gấp 10 lần dòng nước thường.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa hết đâu các đồng chí! Hộp tiếp đạn của khẩu súng này cũng thuộc hàng khủng: Cá Cung Thủ có thể bắn liên thanh tới 6-7 phát đạn nước liên tiếp chỉ trong vòng 2 giây mà không cần ngụp xuống nạp lại nước!". Bố cục: Bắn liên thanh đại bác: chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) bắn liên tiếp 6-7 phát đạn nước 'bụp bụp bụp' thành một chuỗi đạn nước bay thẳng hàng lên không trung chỉ trong vòng 2 giây như súng máy tự động.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi phát bắn đều giữ nguyên hỏa lực chính xác tuyệt đối như một khẩu súng máy tự động dưới nước!". Bố cục: Các bia bắn thử nghiệm trên cao: 6-7 hồng tâm lá cây đều bị đạn nước xuyên thủng tâm điểm chính xác 100%, nước bắn tung tóe như súng máy cao xạ.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sở hữu một khẩu đại bác uy lực là một chuyện, nhưng ngắm bắn trúng mục tiêu lại là bài toán khó hơn gấp vạn lần!". Bố cục: Bài toán ngắm bắn quang học: mặt phân cách giữa nước và không khí gợn sóng lấp lánh; một tia sáng từ con mồi chiếu xuống bị bẻ gãy góc đột ngột khi chui qua mặt nước. KHÔNG có chú Cá Cung Thủ trong cảnh này.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và trở ngại chết người mà mọi xạ thủ dưới nước phải đối mặt chính là: Hiện tượng khúc xạ ánh sáng qua ranh giới giữa nước và không khí!". Bố cục: Hình ảnh phóng to lăng kính khúc xạ nước: đường đi của ánh sáng bị gãy khúc tại bề mặt phân cách, tạo ra góc lệch lớn đánh lừa thị giác. KHÔNG có chú Cá Cung Thủ trong cảnh này.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bất kỳ học sinh nào từng học vật lý đều biết định luật bẻ gãy ánh sáng Snell: Ánh sáng truyền từ không khí vào nước sẽ bị bẻ cong một góc đáng kể.". Bố cục: Sơ đồ định luật khúc xạ Snell: BÊN TRÁI hình ảnh chú chú nhện con hoạt hình nhiều mắt ngơ ngác, lông xù màu nâu, đeo ba lô tí hon bám trên lá cây thực tế trên cành; BÊN PHẢI hình ảnh bóng mờ ảo của chú nhện bị lệch đi một góc lớn do ánh sáng bị bẻ cong. KHÔNG có chú Cá Cung Thủ trong cảnh này.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Do đó, vị trí mà đôi mắt cá nhìn thấy chỉ là một ảnh ảo lơ lửng, lệch hẳn so với vị trí thực tế của con mồi trên cành cây!". Bố cục: Mô phỏng tầm nhìn sai lệch: hình ảnh con nhện ảo trôi nổi phía trên cành cây, mũi tên chỉ rõ khoảng cách sai số giữa vị trí thực và vị trí ảo. KHÔNG có chú Cá Cung Thủ trong cảnh này.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu bạn bắn thẳng vào vị trí bạn nhìn thấy, viên đạn nước chắc chắn sẽ bay chệch lên trời và con mồi sẽ ung dung bay mất.". Bố cục: Minh họa bắn trượt: một viên đạn nước bắn thẳng vào ảnh ảo bị bay vút lên trời chệch mục tiêu; bên cạnh là chú nhện ung dung vẫy tay chào mỉa mai. KHÔNG có chú Cá Cung Thủ trong cảnh này.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng bộ não của Thiện Xạ Đầm Lầy chỉ nặng chưa đầy không phẩy một gam lại có thể giải bài toán lượng giác khúc xạ phức tạp này trong vòng chưa đầy 50 mili-giây!". Bố cục: Bộ vi xử lý lượng giác sinh học: bộ não tí hon của chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) phát sáng các vi mạch thuật toán giải phương trình sin khúc xạ chỉ trong vòng 50 mili-giây.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Alo các bác xạ thủ ơi, em đứng trên cành nghiêng 45° thế này mà tia nước bắn trúng ngay giữa trán là sao?". Bố cục: Chú chú nhện con hoạt hình nhiều mắt ngơ ngác, lông xù màu nâu, đeo ba lô tí hon bám trên lá cây bám trên cành nghiêng 45 độ, ôm đầu ngơ ngác khi tia nước bắn trúng ngay đỉnh đầu, chiếc ba lô tí hon văng ra ngoài trong ngỡ ngàng.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đúng như chú nhện con ngơ ngác vừa ôm đầu kêu trời! Để giảm thiểu tối đa sai số khúc xạ, Cá Cung Thủ thường bơi tới vị trí gần vuông góc dưới mục tiêu, tạo góc bắn từ 70° đến 80° so với mặt nước.". Bố cục: Chiến thuật định vị góc bắn: chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) bơi vào vị trí tạo góc ngắm tối ưu 70°-80° gần vuông góc mặt nước, sẵn sàng ngắm chuẩn.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đôi mắt to tròn của cá có cấu tạo nhãn cầu đặc biệt với hai trục quang học độc lập, vừa giúp bù trừ tự động độ cong mặt nước, vừa tạo ra tầm nhìn lập thể ba chiều cực kỳ sắc bén xuyên qua lớp gương phản chiếu của mặt hồ!". Bố cục: Đặc tả đôi mắt chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor): nhãn cầu lớn màu vàng với 2 trục quang học độc lập xoay chuyển linh hoạt, xuyên qua lớp gương phản xạ mặt nước để tạo tầm nhìn 3D sắc bén.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thậm chí võng mạc của nó còn sở hữu các tế bào cảm quang chuyên biệt có khả năng lọc sạch ánh sáng lóa mặt trời và bóc tách các vệt màu ngụy trang của bầy côn trùng ẩn nấp sau kẽ lá xanh!". Bố cục: Võng mạc siêu cảm biến: các tế bào cảm quang chuyên biệt trong mắt cá tự động lọc sạch ánh sáng lóa mặt trời và bóc tách màu ngụy trang của bầy côn trùng.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhiều người lầm tưởng khả năng bắn tỉa thần sầu này là bản năng bẩm sinh được lập trình sẵn trong gen của Cá Cung Thủ.". Bố cục: Trường bắn tân binh dưới đáy sông: các chú cá cung thủ non bé xíu xếp hàng ngay ngắn, phía trên là các cành cây có gắn bia tập bắn bằng lá tròn. KHÔNG có chú Cá Cung Thủ trong cảnh này.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nghiên cứu thực nghiệm chấn động của các nhà khoa học đã chứng minh điều ngược lại: Đây là một kỹ năng quân sự bắt buộc phải trải qua rèn luyện gian khổ!". Bố cục: Phòng thí nghiệm nghiên cứu động vật: các nhà khoa học ghi chép sổ nhật ký theo dõi quá trình tập bắn từ thuở sơ sinh của bầy cá. KHÔNG có chú Cá Cung Thủ trong cảnh này.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bản tin huấn luyện từ trường bắn tân binh: Những chú cá non mới nở chỉ có thể bắn ra những tia nước yếu ớt xa vài centimet, và chúng bắn trượt tới 99% số mục tiêu trong những tuần đầu đời!". Bố cục: Loa phát thanh quân sự: bảng kết quả tập bắn ghi dòng chữ 'BẮN TRƯỢT 99%'; một chú cá non bắn tia nước phì ra được 2cm rồi rơi tõm xuống nước mặt méo xẹo. KHÔNG có chú Cá Cung Thủ trong cảnh này.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đúng là cảnh tượng bi hài của trường bắn quân sự!". Bố cục: Hình ảnh huấn luyện gian khổ: chú cá non kiên trì bắn hàng trăm phát đạn nước liên tục, não bộ vẽ các đường vòng cung hiệu chỉnh góc ngẩng dần đều.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cá cung thủ non phải trải qua hàng ngàn lần thử và sai, tự rút kinh nghiệm sau mỗi cú bắn lệch để não bộ dần dần học cách bù trừ góc khúc xạ theo cự ly thực tế.". Bố cục: Biểu đồ tiến bộ kỹ năng: đường cong học tập đi lên dốc đứng theo số ngày rèn luyện, các tia nước bắn ngày càng xa và trúng đích nhiều hơn.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng điều làm kinh ngạc giới nghiên cứu hành vi động vật là phát hiện công bố trên tạp chí Nature: Cá Cung Thủ sở hữu năng lực học tập xã hội đỉnh cao!". Bố cục: Tạp chí Nature danh giá: trang bìa Nature mở ra hình ảnh một chú cá non đang bơi sát cạnh chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) kỳ cựu, chăm chú quan sát đàn anh ngắm bắn chuẩn xác.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một con cá non nếu được bơi cạnh những xạ thủ kỳ cựu dày dặn kinh nghiệm chỉ cần đứng quan sát đàn anh bắn mồi vài lần là có thể tự điều chỉnh góc bắn của mình chuẩn xác hơn gấp nhiều lần mà không cần tự mình thử sai!". Bố cục: Cảnh học hỏi đàn anh: chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) giương vây bắn mẫu một phát đạn nước trúng đích, chú cá non bơi bên cạnh mở to mắt ngưỡng mộ và bắt chước tư thế ngắm bắn.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khả năng quan sát, phân tích đường đạn của đồng loại rồi mô phỏng lại trong não bộ là một năng lực nhận thức cấp cao mà trước đây người ta ngỡ chỉ có ở các loài linh trưởng và con người!". Bố cục: Mô phỏng năng lực nhận thức xã hội: sơ đồ sóng não từ chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) truyền cảm hứng mô phỏng sang chú cá non, giúp tân binh bắn trúng ngay bia tập chỉ sau một lần quan sát.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để kiểm chứng điều này, giáo sư Schuster tại Đức đã thiết lập một thí nghiệm độc lạ: Ông chiếu các điểm sáng nhân tạo di động trên màn hình máy tính với vận tốc thay đổi liên tục.". Bố cục: Thí nghiệm của GS Stefan Schuster: một màn hình máy tính chiếu điểm sáng di động, chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) tính toán trước quỹ đạo và bắn tia nước đón đầu trúng phóc điểm sáng trên màn hình.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ sau vài lượt thử, bầy Cá Cung Thủ đã tự tính toán được quy luật chuyển động và bắn đón đầu mục tiêu ảo cực kỳ chính xác! Một tư duy tác chiến bắn chặn ngang tầm tên lửa phòng không!". Bố cục: Màn hình máy tính hiển thị điểm 'TARGET DESTROYED': điểm sáng ảo vừa xuất hiện đã bị tia nước bắn hạ gục; các nhà khoa học vỗ tay kinh ngạc.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bắn trúng con mồi rớt khỏi cành lá mới chỉ là một nửa chặng đường của chiến dịch săn mồi.". Bố cục: Chiến trường cạnh tranh khốc liệt: con côn trùng vừa bị bắn rơi khỏi lá, xung quanh nhiều chú cá khác trong bầy đang giương mắt thèm thuồng chuẩn bị lao vào cướp mồi. KHÔNG có chú Cá Cung Thủ trong cảnh này.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong thế giới đầm lầy cạnh tranh khốc liệt, bắn trúng mà không đớp kịp thì miếng ăn sẽ rơi ngay vào miệng đối thủ bên cạnh! Và đây là lúc bộ vi xử lý đạn đạo của Thiện Xạ Đầm Lầy phát huy uy lực tối đa.". Bố cục: Cảnh tượng bầy cá đói bụng há miệng chực chờ dưới mặt nước, mắt lăm lăm nhìn con mồi đang rơi lơ lửng. KHÔNG có chú Cá Cung Thủ trong cảnh này.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngay khoảnh khắc tia nước vừa rời khỏi khóe miệng trong vòng chưa đầy 100 mili-giây, Cá Cung Thủ đã tính toán xong toàn bộ phương trình parabol đường rơi của con mồi: Nó biết chính xác vị trí và thời điểm con côn trùng sẽ tiếp nước!". Bố cục: Bộ xử lý đạn đạo siêu tốc: đường parabol màu vàng vẽ từ vị trí con bọ rơi xuống mặt nước, đồng hồ bấm giờ tính toán dừng ở mốc 100 mili-giây. KHÔNG có chú Cá Cung Thủ trong cảnh này.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không cần đợi nhìn thấy con mồi rơi tới đâu, con cá lập tức bật chế độ bơi nước rút với tốc độ xé nước, lao thẳng tới đúng tọa độ tiếp nhận trước khi con mồi chạm mặt nước chỉ trong 0,1 giây!". Bố cục: Pha bơi nước rút thần tốc: chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) bật vây bơi vút như quả ngư lôi xé toạc mặt nước, há rộng miệng đón lõng ngay vị trí con mồi chạm nước chỉ trong 0,1 giây.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một pha đoán đầu đường đạn thần tốc khiến mọi đối thủ xung quanh chỉ biết đứng nhìn trong bất lực!". Bố cục: chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) đớp gọn con mồi đúng 0,1 giây khi vừa chạm mặt nước; xung quanh các chú cá đối thủ thắng gấp tạo vệt nước xoáy bất lực.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cuộc đua cướp mồi trong bầy đàn khốc liệt đến mức 3-4 đối thủ bơi bên cạnh cũng lập tức tính toán điểm rơi để lao vào tranh cướp!". Bố cục: Cuộc đua bầy đàn náo loạn: 3-4 chú cá đối thủ cùng lao tới từ các hướng tạo sóng cuồn cuộn, nhưng chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) đã nhanh chân đớp gọn con mồi trước mũi đối thủ trong gang tấc.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu tay súng chính chỉ cần chậm trễ 0,1 giây trong pha bơi nước rút, con mồi do chính mình tốn công bắn hạ sẽ biến mất tăm vào dạ dày của kẻ cơ hội đứng xem!". Bố cục: Hình ảnh minh họa đối thủ cướp mồi: con mồi rơi ngay sát miệng kẻ cơ hội bơi chậm 0,1s, chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) phóng vụt qua nẫng tay trên trong tích tắc.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôi bắn tỉa trong quân đội cả đời mà nhìn pha tính toán đạn đạo của chú cá này cũng phải ngả mũ chào thua!". Bố cục: Chú xạ thủ quân đội lực lưỡng mặc quân phục rằn ri ngả mũ kính phục, giơ ngón tay cái tán thưởng chiếc camera quay cảnh tính toán đạn đạo của cá.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thậm chí Thiện Xạ Đầm Lầy còn trang bị một phương án tác chiến dự phòng cực kỳ thực dụng: Nếu con mồi đậu ở cành lá quá thấp dưới 30cm, gã sẽ không thèm tốn một giọt nước nào!". Bố cục: Phương án tác chiến cận chiến: mục tiêu ở cành lá thấp 30cm, chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) ngưng hỏa lực nước, co vây đuôi tích lũy động năng.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Con cá chỉ cần quẫy mạnh chiếc đuôi vây khỏe khoắn, phóng vút toàn bộ cơ thể bay lên khỏi mặt nước như một chiếc tên lửa mini để ngoạm gọn con mồi ngay trên không trung!". Bố cục: Cú nhảy không kích ngoạn mục: chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) phóng vút toàn bộ cơ thể bay lên khỏi mặt nước 30cm như tên lửa mini ngoạm trọn con mồi trên không trung.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuy nhiên, cỗ máy săn mồi hoàn hảo này cũng có những tử huyệt kỹ thuật: Khi trời nổi gió to làm mặt nước dậy sóng cuồn cuộn hoặc khi váng dầu ô nhiễm che phủ mặt sông, thuật toán quang học bị nhiễu loạn hoàn toàn, biến tay súng cừ khôi thành một kẻ bắn trượt đáng thương!". Bố cục: Tử huyệt thời tiết: mặt nước gió to nổi sóng dập dềnh cuồn cuộn, chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) ngắm bắn bị sóng làm méo hình ảnh, tia nước bắn chệch cành lá làm con mồi bay mất vẻ mặt tiếc nuối.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo tổng kết thử nghiệm kỹ thuật số 20: Cá Cung Thủ chứng minh cho chúng ta thấy rằng sức mạnh hủy diệt không nhất thiết phải đến từ kích thước cơ bắp đồ sộ hay vũ khí hủy diệt hàng loạt.". Bố cục: Bảng tổng kết đánh giá kỹ thuật số 20: biểu đồ sao radar với các chỉ số: Độ chính xác 95%, Tầm bắn 3m, Thời gian tính toán 50ms; chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) đứng trên bục chào quân sự nghiêm trang.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sự am hiểu quy luật tự nhiên, khả năng tính toán chuẩn xác và tinh thần học hỏi không ngừng mới là chìa khóa vạn năng để sinh tồn và làm chủ cuộc chơi.". Bố cục: Hình ảnh triết lý thiên nhiên: đại dương bao la với những sinh vật khổng lồ bơi qua, nhưng tâm điểm ánh sáng chiếu vào chú chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) bé nhỏ phát sáng rực rỡ với khẩu đại bác uy lực.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chính cơ chế nén dòng nước gia tốc đuôi của loài cá này đang là nguồn cảm hứng vô giá để các kỹ sư hàng không vũ trụ và công nghệ in ba chiều hiện đại". Bố cục: Nguồn cảm hứng vô giá: các kỹ sư hàng không vũ trụ và in 3D hiện đại say sưa nghiên cứu cơ chế đẩy dòng nước của Cá Cung Thủ trên bàn thiết kế. KHÔNG có chú Cá Cung Thủ trong cảnh này.
```
</details>

<details><summary>L62</summary>

```text
HÌNH L62 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bạn khâm phục điều gì nhất ở Thiện Xạ Đầm Lầy Cá Cung Thủ: Khẩu đại bác nén đạn nước gia tốc đuôi, hay bộ não giải định luật khúc xạ ánh sáng trong chớp mắt? Hãy để lại ý kiến bình luận của đội kỹ thuật bên dưới nhé!". Bố cục: Khung bình luận tương tác: chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor) cầm micro hướng về người xem, bên cạnh là hai ô lựa chọn: 'ĐẠI BÁC NÉN ĐẠN NƯỚC' và 'BỘ NÃO GIẢI KHÚC XẠ 50ms' kèm dấu hỏi chấm to lớn.
```
</details>

<details><summary>L63</summary>

```text
HÌNH L63 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và bây giờ, hãy hướng ngòi bút về phân cảnh kết thúc bí ẩn! Trong tập tiếp theo, chúng ta sẽ rời xa những cánh rừng ngập mặn châu Á để thâm nhập vào vùng rừng nhiệt đới âm u của lục địa đen Châu Phi.". Bố cục: Chuyển cảnh rừng rậm châu Phi: ngòi bút vẽ tay phác thảo khu rừng mưa nhiệt đới sương mù mờ ảo, những thân cây rêu phong cổ thụ bí ẩn. KHÔNG có chú Cá Cung Thủ trong cảnh này.
```
</details>

<details><summary>L64</summary>

```text
HÌNH L64 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy chiêm ngưỡng một bóng đen bí ẩn vô cùng kỳ dị!". Bố cục: BÓNG ĐEN BÍ ẨN TẬP TIẾP THEO (TASTE-68): một bóng đen tuyền hình chú ếch nhỏ bé kỳ dị trong bóng tối, từ đầu ngón chân phát ra những tia sáng kim loại sắc nhọn kèm dấu hỏi chấm khổng lồ. KHÔNG có chú Cá Cung Thủ trong cảnh này.
```
</details>

<details><summary>L65</summary>

```text
HÌNH L65 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một sinh vật lưỡng cư nhỏ bé, nhưng sở hữu cơ chế tự vệ được đánh giá là điên rồ và đau đớn nhất hành tinh:". Bố cục: Bóng đen chú ếch nhỏ bé giương mắt đỏ rực giữa đêm tối rậm rạp sương mù, thân mình phủ lớp lông gai mờ ảo đầy đe dọa. KHÔNG có chú Cá Cung Thủ trong cảnh này.
```
</details>

<details><summary>L66</summary>

```text
HÌNH L66 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi bị kẻ săn mồi dồn vào chân tường, nó sẽ chủ động tự co thắt cơ bắp bẻ gãy chính đốt xương ngón chân của mình, đâm thủng lớp da thịt ra ngoài để tạo thành một bộ móng vuốt sắc nhọn như dao găm hệt như dị nhân Wolverine trong truyện tranh!". Bố cục: Cận cảnh bộ vuốt sắc nhọn: xương ngón chân tự đâm xuyên qua da thịt tạo thành 3 chiếc móng vuốt dài nhọn hoắt như móng vuốt Người Sói Wolverine giương lên thách thức kẻ thù. KHÔNG có chú Cá Cung Thủ trong cảnh này.
```
</details>

<details><summary>L67</summary>

```text
HÌNH L67 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đố các chuyên viên kỹ thuật biết danh tính của sát thủ tự bẻ xương kỳ lạ này là ai? Hãy viết ngay câu trả lời của bạn dưới phần bình luận nhé!". Bố cục: Khung hình tò mò kêu gọi bình luận: bóng đen chú ếch móng vuốt Wolverine bí ẩn dưới ánh trăng rọi, dấu hỏi chấm to vàng phát sáng '?', kêu gọi khán giả đoán tên con vật bên dưới. KHÔNG có chú Cá Cung Thủ trong cảnh này.
```
</details>

<details><summary>L68</summary>

```text
HÌNH L68 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi bay trên không trung, phần đuôi lao vút lên đuổi kịp và đập dồn vào phần đầu!". Bố cục: Pha tăng tốc kỳ diệu: trên không trung, phần đuôi tia nước lao nhanh hơn 20%, đuổi kịp và đập dồn vào phần đầu tạo thành dòng nước cuồn cuộn.
```
</details>

<details><summary>L69</summary>

```text
HÌNH L69 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng ngay cả khi bị ép bắn ở góc nghiêng 45°, tỷ lệ bắn trúng mục tiêu ngay trong phát đạn đầu tiên của gã vẫn đạt tới 90 đến 95%!". Bố cục: Thử thách góc nghiêng cực hạn: cá bị ép bắn ở góc nghiêng 45° so với mặt nước, tia nước vẫn vút trúng đích với độ chính xác 95%.
```
</details>

<details><summary>L70</summary>

```text
HÌNH L70 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một hệ thống kính ngắm quang học hồng ngoại sinh học đỉnh cao mà các nhà thiết kế vũ khí hiện đại phải ghen tị!". Bố cục: Kính ngắm hồng ngoại sinh học: giao diện nhìn từ mắt cá với các đường lưới ngắm màu xanh neon, đánh dấu đỏ vào mục tiêu ngụy trang trong kẽ lá.
```
</details>

<details><summary>L71</summary>

```text
HÌNH L71 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một minh chứng hùng hồn cho thấy trí tuệ của loài cá vượt xa những định kiến nông cạn thường thấy.". Bố cục: Biểu tượng trí tuệ vượt bậc: chú Cá Cung Thủ hoạt hình tỏa sáng rực rỡ với vương miện trí tuệ, đập tan định kiến thông thường về loài cá.
```
</details>

<details><summary>L72</summary>

```text
HÌNH L72 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thiết kế ra những vòi phun hạt siêu vi mô có độ chính xác tuyệt đối mà không cần sử dụng bất kỳ pít-tông cơ học phức tạp nào!". Bố cục: Ứng dụng công nghệ tương lai: BÊN TRÁI vòi phun vi mô động cơ phản lực chất lỏng; BÊN PHẢI đầu in 3D sinh học siêu chính xác mô phỏng cơ chế gia tốc tia nước của Cá Cung Thủ. KHÔNG có chú Cá Cung Thủ trong cảnh này.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Cảnh báo xạ thủ bắn tỉa!". Bố cục: Cảnh báo bắn tỉa giật gân: radar quân sự nhấp nháy phát hiện mục tiêu trên ngọn đước, còi báo động màu đỏ chớp sáng. KHÔNG có chú Cá Cung Thủ trong cảnh này.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bạn có tin một con cá dưới nước lại có thể ngắm bắn bách phát bách trúng các mục tiêu đậu trên cành cây cao tới 2m?". Bố cục: BÊN TRÁI cành cây cao 2m có chú chú nhện con hoạt hình nhiều mắt ngơ ngác, lông xù màu nâu, đeo ba lô tí hon bám trên lá cây đang ung dung bám lá; BÊN DƯỚI mặt nước chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ giương kính ngắm laser đỏ rực lên trời đầy thách thức.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đây là Cá Cung Thủ, tay súng bắn tỉa cừ khôi của các rạn rừng ngập mặn!". Bố cục: Chân dung oai phong: chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ bơi hiên ngang giữa rạn đước, mũ beret đen kiêu hãnh, vảy bạc sọc đen lấp lánh ánh kim, kính ngắm laser khóa chặt mục tiêu.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Thứ nhất, vòm họng của nó có rãnh chữ V ép chặt với lưỡi, tạo thành chiếc nòng súng tí hon". Bố cục: Cơ chế nòng súng chữ V: cận cảnh vòm họng ép sát với lưỡi thành nòng súng tí hon nén tia nước áp suất cao.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "nén tia nước bắn xa kỷ lục tới 3m!". Bố cục: Tia nước bắn vút lên cao xuyên thủng không gian với thước đo đạt mốc kỷ lục 3 mét.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Thứ hai, phần đuôi tia nước bay nhanh hơn phần đầu,". Bố cục: Động lực học chất lỏng: phần đuôi tia nước lao nhanh hơn phần đầu, thu hẹp khoảng cách trong không khí xé gió.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "đập dồn lại thành một giọt đạn nước khổng lồ làm tăng lực va đập gấp 10 lần để hạ gục con mồi!". Bố cục: Hiệu ứng đạn nước gia tốc: phần đuôi tia nước đập dồn vào phần đầu biến thành quả cầu nước uy lực đập văng chú chú bọ ngựa hoạt hình màu xanh lá, hai càng sắc nhọn giương lên đầy tự tin bám trên thân cây khỏi cành cây.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Thứ ba, mặt nước luôn bẻ cong ánh sáng theo định luật khúc xạ,". Bố cục: Giải mã định luật khúc xạ Snell: sơ đồ ánh sáng bị bẻ cong qua mặt nước, tạo ảnh ảo lệch vị trí con mồi. KHÔNG có chú Cá Cung Thủ trong cảnh này.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "nhưng bộ não của loài cá này giải bài toán quang học chỉ trong 50 mili-giây để bắn chính xác tới 95%!". Bố cục: Bộ não giải toán quang học: não bộ chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ tính toán góc bù trừ chỉ trong 50 mili-giây với độ chính xác 95%.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Chưa hết, nó còn tính toán trước điểm rơi đạn đạo". Bố cục: Tính toán điểm rơi đạn đạo: phương trình đạn đạo parabol nối từ cành cây xuống mặt nước trong 100ms.
```
</details>

<details><summary>S11</summary>

```text
HÌNH S11 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "để bơi nước rút cướp mồi trước đối thủ chỉ trong 0,1 giây!". Bố cục: chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ lao vút như ngư lôi đón mồi trong 0,1 giây, nẫng tay trên trước mũi bầy đối thủ.
```
</details>

<details><summary>S12</summary>

```text
HÌNH S12 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Độ chính xác và khả năng thích nghi phi thường,". Bố cục: Độ chính xác phi thường: chú chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ giương vây bơi lượn kiêu hãnh với tỷ lệ bắn trúng 95% bách phát bách trúng.
```
</details>

<details><summary>S13</summary>

```text
HÌNH S13 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "đó chính là vũ khí tối thượng giúp Thiện Xạ Đầm Lầy thống trị cả hai thế giới dưới nước và trên cạn!". Bố cục: Khoảnh khắc vinh quang trọn vẹn: chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ đớp gọn con mồi trên mặt nước, thống trị cả hai thế giới dưới nước và trên cạn giữa rặng rừng ngập mặn lung linh ánh nắng chiến thắng.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/72 của video YouTube về Cá Cung Thủ). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor). Nhân vật phụ cố định: chú nhện con hoạt hình nhiều mắt ngơ ngác, lông xù màu nâu, đeo ba lô tí hon bám trên lá cây; chú bọ ngựa hoạt hình màu xanh lá, hai càng sắc nhọn giương lên đầy tự tin bám trên thân cây; chú dế mèn hoạt hình màu nâu cầm chiếc ô che mưa tí hon ngơ ngác; cô trợ lý sóc hoạt hình đeo kính cận to tròn, mặc áo blouse trắng phòng thí nghiệm, cầm thước đo góc quang học. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/13 của video YouTube Shorts về Cá Cung Thủ). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm tròn một mắt viền đỏ ngộ nghĩnh (cute black beret and circular eye visor). Nhân vật phụ: chú nhện con hoạt hình nhiều mắt ngơ ngác, lông xù màu nâu, đeo ba lô tí hon bám trên lá cây; chú bọ ngựa hoạt hình màu xanh lá, hai càng sắc nhọn giương lên đầy tự tin bám trên thân cây. 
```
</details>

## 7. SEO

- **title:** Cá Cung Thủ Bắn Nước 3 Mét & Thuật Toán Khúc Xạ Ánh Sáng?! | Tập 20
- **hook_paragraph:** Cá Cung Thủ (Archerfish) chỉ dài 20cm nhưng sở hữu nòng súng vòm miệng nén tia nước bắn hạ con mồi cách 3m, tự động giải định luật khúc xạ ánh sáng Snell trong 50 mili-giây và tính toán trước điểm rơi đạn đạo trong 100ms! Giải mã vũ khí bắn tỉa sinh học tối thượng của Thiện Xạ Đầm Lầy.
- **question:** Bạn khâm phục điều gì nhất ở Thiện Xạ Đầm Lầy Cá Cung Thủ: Khẩu súng nén đạn nước gia tốc đuôi, hay bộ não giải định luật khúc xạ ánh sáng trong chớp mắt? Đoán xem bóng đen tập sau là loài nào nhé!
- **next_teaser:** loài ếch tự bẻ gãy xương ngón chân đâm thủng da làm móng vuốt Wolverine
- **shorts_title:** Làm Sao Con Cá Này Giải Được Định Luật Khúc Xạ Ánh Sáng?! 🎯 #shorts #cacungthu
- **shorts_desc:** Cá Cung Thủ chỉ dài 20cm nhưng nén tia nước bắn xa 3m, tự giải bài toán khúc xạ ánh sáng Snell trong 50ms và đoán trước điểm rơi đạn đạo trong 0,1s! Khám phá bí mật Thiện Xạ Đầm Lầy.
- **bullets:** Nòng súng rãnh chữ V nén tia nước vận tốc 5 m/s bắn xa kỷ lục 3 mét · Động lực học chất lỏng: Gia tốc đuôi biến tia nước thành giọt đạn nước uy lực gấp 10 lần · Bộ não giải định luật khúc xạ ánh sáng Snell trong vòng 50 mili-giây với độ chính xác 95% · Năng lực học tập xã hội: Cá non học góc bắn từ xạ thủ kỳ cựu công bố trên Nature · Đoán trước điểm rơi đạn đạo và bơi nước rút cướp mồi trong 0,1 giây · Bật mí bóng đen bí ẩn tập tiếp theo: Sát thủ tự bẻ gãy xương làm móng vuốt Wolverine
- **tags:** cá cung thủ, ca cung thu, archerfish, toxotes, cá cung thủ bắn nước, cá cung thủ săn mồi, khúc xạ ánh sáng, định luật snell, thiện xạ đầm lầy, cá bắn tỉa, động vật hài hước, thế giới động vật, vẽ chuyện hoang dã, whiteboard animation việt nam
- **hashtags:** #CaCungThu #Archerfish #TheGioiDongVat #VeChuyenHoangDa #WhiteboardAnimation

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-20-ca-cung-thu
python src/episode/pipeline.py tts    projects/tap-20-ca-cung-thu     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-20-ca-cung-thu     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-20-ca-cung-thu     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-20-ca-cung-thu              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-20-ca-cung-thu --force
python scripts/beat_sheet.py projects/tap-20-ca-cung-thu               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-20-ca-cung-thu/audio/shorts.wav projects/tap-20-ca-cung-thu/renders/tap-20-ca-cung-thu_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-20-ca-cung-thu
python src/episode/pipeline.py seo    projects/tap-20-ca-cung-thu
python src/episode/episode_doc.py     projects/tap-20-ca-cung-thu
```

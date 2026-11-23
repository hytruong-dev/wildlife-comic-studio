# TẬP 41 — NHỆN LẶN CHUÔNG · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-41-nhen-lan-chuong`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-41-nhen-lan-chuong`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F2` · **Persona giọng:** `ky_su_vu_khi` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Nhện Lặn Chuông |
| Tiêu đề YouTube | Tàu Ngầm Tơ Nhện: Bí Mật Sống 24 Giờ Dưới Đáy Hồ Của Kỹ Sư Tí Hon \| Tập 41 |
| Video dài | `renders/tap-41-nhen-lan-chuong_long.mp4` — 9:15.1 (555.1s) |
| Shorts | `renders/tap-41-nhen-lan-chuong_shorts.mp4` — 0:43.4 (43.4s) |
| Thumbnail | `renders/tap-41-nhen-lan-chuong_thumbnail.jpg` |
| Số hình | dài 57 beat / 57 ảnh riêng; Shorts 8 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.12**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/57 của video YouTube về Nhện Lặn Chuông). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon). Nhân vật phụ cố định: cô trợ lý kỹ thuật thỏ trắng đeo kính bảo hộ, cầm bảng kẹp tài liệu; chú cá con ngơ ngác mắt tròn xoe, mang vây nhỏ nhắn bơi lội. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — LOÀI NHỆN DUY NHẤT SỐNG CẢ ĐỜI DƯỚI NƯỚC
*Thẻ chương:* THỞ BẰNG PHỔI NHƯNG SỐNG CẢ ĐỜI DƯỚI ĐÁY NƯỚC

*Badge:* `HỒ SƠ TỐI MẬT` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene01_p0.wav` (406 ký tự) · mood `tram_bi_an`

```text
Báo cáo thử nghiệm kỹ thuật hàng hải sinh học tối mật cấp độ đỏ! Toàn thể đội ngũ công trình sư hãy đeo kính lặn bảo hộ và kích hoạt đồng hồ đo áp suất, bởi vì cỗ máy sinh học mà chúng ta giải mã hôm nay sẽ phá vỡ mọi quy chuẩn tiến hóa trên Trái Đất. [surprise-oh] Quên đi những tàu ngầm hạt nhân bọc thép titan ngàn tấn của con người, hãy nhìn xuống một bụi rong đuôi chó tĩnh lặng dưới đáy hồ nước ngọt!
```
**Part 1** → `audio/vs/scene01_p1.wav` (366 ký tự) · mood `hao_hung`

```text
Đối tượng mang mã định danh số bốn mươi mốt của chúng ta có tên khoa học là Ar-gy-ro-ne-ta A-qua-ti-ca, nhưng giới kỹ sư đại dương gọi gã bằng một danh xưng đầy kính nể: Thuyền Trưởng Tàu Ngầm Tơ! [surprise-wa] Đây là loài nhện duy nhất trong số hơn năm mươi ngàn loài nhện trên khắp hành tinh từ bỏ hoàn toàn cõi cạn để di cư xuống định cư vĩnh viễn dưới lòng nước!
```
**Part 2** → `audio/vs/scene01_p2.wav` (428 ký tự) · mood `don_dap`

```text
Điều gây chấn động phòng thí nghiệm là sinh vật này hoàn toàn không có mang cá, không có vây bơi, mà vẫn giữ nguyên bộ phổi sách thở khí trời của tổ tiên loài nhện cạn. [surprise-oh] Nếu bạn thả một con nhện nhà bình thường xuống nước, nó sẽ ngạt thở chìm lịm trong vài phút. Nhưng Thuyền Trưởng Tàu Ngầm Tơ lại có thể bơi lặn, săn mồi, ngủ ngáy, thậm chí giao phối và ấp trứng hai mươi tư trên bảy suốt cả cuộc đời dưới đáy hồ!
```
**Part 3** → `audio/vs/scene01_p3.wav` (112 ký tự) · 🎭 cameo `co_tro_ly`

```text
Báo cáo kỹ thuật trưởng, cảm biến sonar báo có một quả cầu thủy tinh đang phát sáng lơ lửng giữa đám rong rêu ạ!
```
**Part 4** → `audio/vs/scene01_p4.wav` (368 ký tự) · mood `hao_hung`

```text
[laughter] Đúng như cô trợ lý vừa phát hiện! Bí mật không nằm ở ma thuật siêu nhiên, mà nằm ở một công trình kiến trúc vi mô vĩ đại: Một quả chuông lặn dệt hoàn toàn bằng tơ kỵ nước, biến một kẻ thở bằng phổi thành chúa tể lòng hồ! Hôm nay, xưởng cơ khí sinh học của chúng ta sẽ tháo dỡ từng mắt tơ để xem gã kỹ sư tí hon này xây trạm không gian dưới nước như thế nào!
```

### scene02 — TÀU NGẦM TƠ KỴ NƯỚC VÀ KHOANG KHÍ ÁP SUẤT
*Thẻ chương:* TƠ NHỆN DƯỚI NƯỚC KHÔNG HỀ BỊ RÃ NƯỚC

*Badge:* `BẢN VẼ THIẾT KẾ` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene02_p0.wav` (363 ký tự) · mood `hao_hung`

```text
Hãy trải cuộn bản vẽ mặt cắt xanh Prussian lên bàn phân tích! [surprise-oh] Muốn xây một căn nhà chứa không khí dưới nước, thách thức cơ học đầu tiên là lực đẩy Ác-si-mét cực lớn sẽ thổi bay mọi cấu trúc nổi lên mặt hồ. Nhưng Thuyền Trưởng Tàu Ngầm Tơ đã giải bài toán kết cấu này bằng một giải pháp tân tiến không thua gì các kỹ sư khoan ngầm dầu khí ngoài khơi!
```
**Part 1** → `audio/vs/scene02_p1.wav` (385 ký tự) · mood `nghiem_trang_gia`

```text
Đầu tiên, gã chọn những nhánh rong rêu thủy sinh vững chắc nhất, rồi bắn hàng trăm sợi tơ neo đa hướng hình mạng nhện để cố định một khung dầm chịu lực. Điểm kỳ diệu nằm ở chỗ: Tơ của loài nhện này chứa protein kỵ nước siêu việt. Khi tiếp xúc với nước ngọt, các sợi tơ không hề bị mủn hay tan rã, mà đan kết lại thành một màng lưới dẻo dai tựa như màng cao su tổng hợp chịu áp lực cao!
```
**Part 2** → `audio/vs/scene02_p2.wav` (260 ký tự) · mood `tram_bi_an`

```text
Sau khi hệ khung neo đã căng cứng, gã bắt đầu nhả tơ dệt thành một chiếc vòm hình chuông úp ngược. Chiếc vòm tơ ban đầu xẹp lép như một chiếc dù nhảy lơ lửng giữa dòng nước. Nhưng làm thế nào để bơm đầy không khí vào một chiếc chuông ngập nước sâu dưới đáy hồ?
```
**Part 3** → `audio/vs/scene02_p3.wav` (89 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Kỹ sư ơi, tơ nhện dệt kín mít thế kia thì nước có thấm ngược vào làm ướt sũng tổ không ạ?
```
**Part 4** → `audio/vs/scene02_p4.wav` (377 ký tự) · mood `hao_hung`

```text
[laughter] Chú cá con ngơ ngác hoàn toàn yên tâm! Khoảng cách giữa các sợi nano tơ kỵ nước nhỏ đến mức sức căng bề mặt của nước biến màng tơ thành bức tường ngăn nước tuyệt đối! Nước bên ngoài không thể lọt vào một giọt, nhưng khí ga bên trong lại được giữ kín bưng. Bây giờ, chiếc chuông đã sẵn sàng, và màn vận chuyển khí thần sầu của thuyền trưởng tí hon chính thức bắt đầu!
```
**Part 5** → `audio/vs/scene02_p5.wav` (436 ký tự) · mood `nghiem_trang_gia`

```text
Chưa hết đâu nhé! Để quả chuông tơ không bị biến dạng khi dòng nước hồ chảy xiết, Thuyền Trưởng Tàu Ngầm Tơ còn dệt thêm một lớp tơ gia cường thứ hai bên trong lòng vòm. Gã dùng đầu húc thử vào thành chuông để kiểm tra độ đàn hồi, giống hệt như các chuyên viên kiểm định độ an toàn vỏ tàu ngầm trước khi hạ thủy! [surprise-wa] Một công trình xây dựng dưới đáy nước hoàn hảo không cần đến một chiếc đinh hay một giọt keo công nghiệp nào!
```

### scene03 — BỘ LÔNG QUẶP BỌT KHÍ VÀ MANG NHÂN TẠO 24 GIỜ
*Thẻ chương:* TỰ HÚT OXY TỪ NƯỚC NHƯ LÁ PHỔI NHÂN TẠO

*Badge:* `ĐỘNG CƠ SINH HỌC` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene03_p0.wav` (309 ký tự) · mood `tram_bi_an`

```text
Hãy quan sát công nghệ vận tải khí độc nhất vô nhị của Thuyền Trưởng Tàu Ngầm Tơ! [surprise-oh] Gã ngoi lên mặt nước, nhưng không thò cả người lên để hít thở như rùa hay cá voi. Gã chỉ nhô đúng phần chóp bụng và cặp chân sau lên khỏi mặt thoáng, thực hiện một cú giật mình chớp nhoáng rồi lặn ngược xuống đáy!
```
**Part 1** → `audio/vs/scene03_p1.wav` (380 ký tự) · mood `hao_hung`

```text
Toàn bộ vùng bụng và chân sau của gã được bao phủ bởi hàng triệu sợi lông kỵ nước siêu nhỏ với mật độ dày đặc. Khi gã quẫy mình giật ngược xuống nước, lớp lông này bẫy chặt một lớp không khí bao quanh bụng, biến phần thân dưới thành một quả cầu bạc lấp lánh như gương soi! [surprise-wa] Đây chính là nguồn gốc tên gọi Ar-gy-ro-ne-ta trong tiếng Hy Lạp cổ, nghĩa là kẻ dệt sợi bạc!
```
**Part 2** → `audio/vs/scene03_p2.wav` (322 ký tự) · mood `don_dap`

```text
Gã ôm quả bọt khí bạc bơi hối hả xuống đáy, luồn vào bên dưới vòm tơ xẹp lép, rồi dùng hai chân sau gạt mạnh bọt khí giải phóng vào trong chuông. Gã lặp lại chuyến xe buýt con thoi này từ hai mươi đến ba mươi chuyến liên tục, cho đến khi quả chuông căng tròn bóng loáng bằng hạt đậu phộng, tỏa sáng lung linh giữa đáy bùn!
```
**Part 3** → `audio/vs/scene03_p3.wav` (313 ký tự) · mood `nghiem_trang_gia`

```text
Nhưng điều chấn động khoa học thế giới vừa được hai giáo sư Sey-mour và Hetz công bố trên Tạp chí Sinh học Thực nghiệm: Quả chuông tơ này không chỉ là một chiếc bình dưỡng khí tĩnh! [surprise-oh] Khi nhện tiêu thụ oxy bên trong, nồng độ oxy trong chuông tụt xuống thấp hơn lượng oxy hòa tan trong nước xung quanh.
```
**Part 4** → `audio/vs/scene03_p4.wav` (422 ký tự) · mood `hao_hung`

```text
Sự chênh lệch áp suất riêng phần biến toàn bộ bề mặt quả chuông thành một chiếc mang nhân tạo khổng lồ! [surprise-wa] Oxy từ nước xung quanh tự động thẩm thấu xuyên qua màng tơ chảy vào chuông, trong khi khí cac-bo-nic thở ra tự khuếch tán ra ngoài hồ! Nhờ động cơ thẩm thấu thụ động này, một lượng khí ban đầu có thể cung cấp dưỡng khí cho nhện sống suốt hai mươi tư giờ liên tục mà không cần bơi lên mặt hồ lấy thêm khí!
```
**Part 5** → `audio/vs/scene03_p5.wav` (440 ký tự) · mood `don_dap`

```text
Tuy nhiên, động cơ mang nhân tạo này cũng có một nhược điểm vật lý không thể tránh khỏi: Khí Ni-tơ trong bọt khí cũng dần dần hòa tan và thất thoát ra ngoài nước. Khi lượng Ni-tơ giảm đi, quả chuông sẽ từ từ xẹp lại sau một đến hai ngày. [surprise-oh] Chính vì vậy, Thuyền Trưởng Tàu Ngầm Tơ phải thực hiện một chuyến tuần tra bảo dưỡng định kỳ mỗi ngày một lần, ngoi lên mặt nước mang về vài bọt khí tươi mới để nạp lại áp suất cho căn cứ!
```

### scene04 — NHỆN ĐỰC TO HƠN NHỆN CÁI 30% ĐỂ GIỮ CHUÔNG LẶN
*Thẻ chương:* LOÀI NHỆN DUY NHẤT CON ĐỰC LỚN HƠN CON CÁI

*Badge:* `NGHỊCH LÝ GIA ĐÌNH` · *mood mặc định:* `bi_hai`

**Part 0** → `audio/vs/scene04_p0.wav` (317 ký tự) · mood `bi_hai`

```text
Bây giờ, chúng ta bước vào hồ sơ gia đình đầy bi hài của Thuyền Trưởng Tàu Ngầm Tơ! [sigh] Nếu bạn đã quen với quy luật tàn khốc trên cạn của loài nhện, nơi các nàng nhện cái khổng lồ thường xơi tái chú nhện đực gầy gò ngay sau đêm tân hôn, thì dưới đáy hồ nước ngọt, tạo hóa đã lật ngược ván cờ một trăm tám mươi độ!
```
**Part 1** → `audio/vs/scene04_p1.wav` (340 ký tự) · mood `hao_hung`

```text
Ở loài nhện lặn chuông, con đực có chiều dài cơ thể từ mười đến mười lăm mi-li-mét, trong khi con cái chỉ đạt từ tám đến mười ba mi-li-mét. [surprise-oh] Nhện đực to hơn nhện cái đến ba mươi phần trăm và sở hữu sải chân dài cơ bắp vượt trội! Đây là một hiện tượng dị hình giới tính đảo ngược cực kỳ hiếm hoi trong toàn bộ thế giới tám chân!
```
**Part 2** → `audio/vs/scene04_p2.wav` (90 ký tự) · 🎭 cameo `be_con`

```text
Ủa các bác kỹ sư ơi, sao nhện đực dưới nước lại được ưu ái ăn sung mặc sướng to con thế ạ?
```
**Part 3** → `audio/vs/scene04_p3.wav` (365 ký tự) · mood `hao_hung`

```text
[laughter] Bé con thắc mắc rất chí lý! Lý do là vì di chuyển trong môi trường nước đặc quánh đòi hỏi lực cản thủy động học cực lớn. Nhện đực không chịu ngồi yên một chỗ, gã phải liên tục bơi đường dài đi tuần tra và tìm kiếm bạn gái giữa các bụi rong. Thân hình to lớn và đôi chân dài giúp gã bơi nhanh hơn, quặp được bọt khí to hơn và không bị dòng nước cuốn trôi!
```
**Part 4** → `audio/vs/scene04_p4.wav` (383 ký tự) · mood `am_ap`

```text
Khi tìm thấy chuông lặn của một nàng nhện ưng ý, chàng nhện đực không lao vào ẩu đả. Gã lịch sự xây ngay một chiếc chuông lặn phụ ngay sát vách căn hộ của nàng, rồi dệt một đường hầm tơ nối thông hai phòng khách lại với nhau! [surprise-wa] Một căn biệt thự thông tầng dưới đáy nước được hình thành lãng mạn vô cùng, nơi con đực bảo vệ đàn con mà không hề lo sợ bị người tình ăn thịt!
```
**Part 5** → `audio/vs/scene04_p5.wav` (472 ký tự) · mood `am_ap`

```text
Sau tuần trăng mật ngọt ngào, nàng nhện cái bắt đầu công việc thiêng liêng nhất của một người mẹ: Đẻ từ năm mươi đến một trăm quả trứng bọc trong một chiếc kén tơ trắng muốt, treo lơ lửng ở phần vòm cao nhất của quả chuông lặn! [surprise-oh] Nơi đây chứa lượng oxy tinh khiết nhất để nuôi dưỡng các nhện con. Khi các chú nhện con chào đời, chúng bơi lội ngay trong phòng khách dưới nước của bố mẹ, học cách quặp bọt khí đầu tiên trước khi tự lập xây dựng vương quốc riêng!
```

### scene05 — TÀU NGẦM SĂN MỒI VÀ GIẤC NGỦ ĐÔNG ĐÓNG BĂNG
*Thẻ chương:* SĂN MỒI KHÔNG CẦN RA KHỎI PHÒNG KHÁCH DƯỚI NƯỚC

*Badge:* `THỰC CHIẾN ĐÁY HỒ` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene05_p0.wav` (335 ký tự) · mood `tram_bi_an`

```text
Hãy chứng kiến cỗ máy săn ngầm hoạt động trong điều kiện chiến trường thực tế! [surprise-oh] Thuyền Trưởng Tàu Ngầm Tơ không cần bơi lội rượt đuổi con mồi cho tốn calo. Từ quả chuông lặn trung tâm, gã giăng ra hàng chục sợi tơ bẫy vô hình kết nối trực tiếp với các cành rong rêu xung quanh như những đường dây điện thoại bảo vệ căn cứ!
```
**Part 1** → `audio/vs/scene05_p1.wav` (300 ký tự) · mood `don_dap`

```text
Gã ngồi thảnh thơi bên trong quả chuông ấm áp, chỉ thò những đầu móng chân nhạy cảm ra ngoài chạm vào các sợi tơ kích hoạt. Khi một con ấu trùng chuồn chuồn, bọ gậy hay một chú cá nhỏ bơi ngang qua vô tình chạm vào sợi tơ cảm biến, xung động rung lắc truyền thẳng vào màng chuông với tốc độ ánh sáng!
```
**Part 2** → `audio/vs/scene05_p2.wav` (322 ký tự) · mood `hao_hung`

```text
Vút! Thuyền trưởng phóng vọt ra khỏi cửa hầm, tung hai chiếc kìm kẹp chứa nọc độc tiêm thẳng vào con mồi làm nạn nhân tê liệt trong tích tắc! [surprise-wa] Sau đó, gã kéo chiến lợi phẩm ngược vào bên trong quả chuông lặn khô ráo để thưởng thức bữa tiệc thịnh soạn mà không sợ bị các loài cá săn mồi khác cướp mất miếng ăn!
```
**Part 3** → `audio/vs/scene05_p3.wav` (423 ký tự) · mood `hao_hung`

```text
Nếu bất ngờ có một con cá chép đói khát bơi tới tấn công cắn rách vòm tơ, thuyền trưởng tí hon sẽ phản ứng thế nào? [surprise-oh] Gã không hề hoảng loạn! Với tốc độ cơ động cực nhanh, gã lập tức thoát hiểm qua cửa đáy khẩn cấp, núp vào khe đá ngầm. Đợi kẻ thù bỏ đi, gã quay lại hiện trường và chỉ mất chưa đầy ba mươi phút để vá lành mọi vết rách bằng những đường tơ kỵ nước mới toanh, tiếp tục làm chủ pháo đài dưới nước!
```
**Part 4** → `audio/vs/scene05_p4.wav` (401 ký tự) · mood `nghiem_trang_gia`

```text
Thậm chí vào mùa đông băng giá, khi nhiệt độ nước tụt xuống không độ C và mặt hồ đóng băng dày cộp cắt đứt hoàn toàn nguồn không khí mặt thoáng, cỗ máy sinh học này vẫn vận hành ngoan cường! [surprise-oh] Nhện lặn chuông bò xuống lớp bùn sâu nhất, dệt một chiếc kén tơ siêu dày bọc kín một túi khí nhỏ, hạ thấp thân nhiệt và nhịp tim để ngủ đông suốt nhiều tháng ròng rã cho đến khi mùa xuân tan băng!
```

### scene06 — GIỚI HẠN CHỈ LÀ DO BẠN CHƯA DỆT CHUÔNG KHÍ
*Thẻ chương:* BÀI HỌC CUỘC SỐNG VÀ THÁCH THỨC ĐOÁN TẬP 42

*Badge:* `BẢN TỔNG KẾT` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (387 ký tự) · mood `am_ap`

```text
Hồ sơ vũ khí số bốn mươi mốt chính thức khép lại với những thông số kinh ngạc! Nhện Lặn Chuông minh chứng hùng hồn cho bài học tiến hóa vĩ đại: Khi môi trường sống cạn kiệt cơ hội, bạn không nhất thiết phải thay đổi toàn bộ nội tạng để thích nghi. Thuyền Trưởng Tàu Ngầm Tơ không mọc ra mang cá, gã chỉ đơn giản dệt nên một công nghệ đem theo bầu trời của chính mình xuống đáy đại dương!
```
**Part 1** → `audio/vs/scene06_p1.wav` (293 ký tự) · mood `hao_hung`

```text
Nếu trong cuộc sống bạn cảm thấy ngột ngạt và lạc lõng giữa một môi trường xa lạ, hãy nhớ tới chú nhện lặn chuông: [laughter] Đôi khi, chỉ cần một quả chuông kiên định dệt bằng sự sáng tạo và nỗ lực, bạn hoàn toàn có thể tự tạo ra bầu không khí thành công cho riêng mình ngay giữa nghịch cảnh!
```
**Part 2** → `audio/vs/scene06_p2.wav` (190 ký tự) · mood `hao_hung`

```text
Nếu được trang bị một bộ đồ lặn bong bóng như nhện lặn chuông, bạn muốn lặn xuống đáy hồ nào để khám phá thế giới vi mô kỳ ảo? Hãy để lại ý kiến thú vị của bạn ở phần bình luận bên dưới nhé!
```
**Part 3** → `audio/vs/scene06_p3.wav` (339 ký tự) · mood `tram_bi_an`

```text
Còn bây giờ, hãy nhìn vào bóng đen bí ẩn của hồ sơ số bốn mươi hai! [surprise-oh] Một sinh vật biển kỳ dị chán ghét đại dương, bỏ nước lên cạn leo trèo trên cây ngập mặn, nếu ngâm nước quá lâu thì lại bị chết đuối, và mỗi khi nuốt mồi lại phải tụt cả hai nhãn cầu mắt xuống tận cổ họng! Bạn có đoán được quái kiệt hai mang này là ai không?
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Bạn có tin trên đời có một loài nhện thở bằng phổi nhưng cả cuộc đời lại sống dưới đáy nước? [surprise-wa] Đây là Nhện Lặn Chuông, dài chỉ mười đến mười lăm mi-li-mét nhưng sở hữu công nghệ tàu ngầm vô tiền khoáng hậu! Gã ngoi lên mặt nước, dùng bộ lông kỵ nước quặp chặt một bọt khí bạc quanh bụng rồi lặn xuống đáy hồ. Tại đây, gã dệt một chiếc vòm tơ hình chuông úp ngược vào rong rêu, bơm đầy bọt khí vào trong để làm trạm không gian dưới nước! Điều chấn động là màng tơ này hoạt động như một chiếc mang nhân tạo, tự hút oxy hòa tan từ nước xung quanh để gã thở suốt hai mươi tư giờ mà không cần ngoi lên mặt hồ! Từ ăn ngủ, săn mồi đến đẻ trứng, gã làm trọn vẹn trong bong bóng không khí kỳ diệu, chứng minh giới hạn sinh tồn chỉ là chuyện nhỏ trước kỹ nghệ đỉnh cao của thiên nhiên!
```

**Whisper prompt:** `Nhện Lặn Chuông, Thuyền Trưởng Tàu Ngầm Tơ, Argyroneta aquatica, Seymour, Hetz, mang nhân tạo, oxy, nitơ, 24 giờ, 30%, 15mm, 0°C, Cá Thòi Lòi`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| năm mươi ngàn | 50.000 |
| Năm mươi ngàn | 50.000 |
| hai mươi tư giờ | 24 giờ |
| Hai mươi tư giờ | 24 giờ |
| hai mươi tư trên bảy | 24/7 |
| Hai mươi tư trên bảy | 24/7 |
| ba mươi phần trăm | 30% |
| Ba mươi phần trăm | 30% |
| ba mươi phút | 30 phút |
| Ba mươi phút | 30 phút |
| mười đến mười lăm mi-li-mét | 10-15mm |
| Mười đến mười lăm mi-li-mét | 10-15mm |
| tám đến mười ba mi-li-mét | 8-13mm |
| Tám đến mười ba mi-li-mét | 8-13mm |
| năm mươi đến một trăm quả trứng | 50-100 trứng |
| Năm mươi đến một trăm quả trứng | 50-100 trứng |
| năm mươi đến một trăm | 50-100 |
| Năm mươi đến một trăm | 50-100 |
| một đến hai ngày | 1-2 ngày |
| Một đến hai ngày | 1-2 ngày |
| mỗi ngày một lần | mỗi ngày 1 lần |
| thứ hai | thứ 2 |
| Thứ hai | Thứ 2 |
| không độ C | 0°C |
| Không độ C | 0°C |
| bốn mươi mốt | 41 |
| Bốn mươi mốt | 41 |
| bốn mươi hai | 42 |
| Bốn mươi hai | 42 |
| Tập bốn mươi mốt | Tập 41 |
| Tập bốn mươi hai | Tập 42 |
| Tập bốn mươi | Tập 40 |
| số bốn mươi mốt | số 41 |
| Số bốn mươi mốt | Số 41 |
| Ar-gy-ro-ne-ta | Argyroneta |
| A-qua-ti-ca | aquatica |
| Sey-mour | Seymour |
| Hetz | Hetz |
| Ni-tơ | Nitơ |
| cac-bo-nic | CO2 |
| hai mươi | 20 |
| ba mươi | 30 |
| bốn mươi | 40 |
| năm mươi | 50 |
| sáu mươi | 60 |
| bảy mươi | 70 |
| tám mươi | 80 |
| chín mươi | 90 |
| một trăm | 100 |
| năm trăm | 500 |
| một ngàn | 1.000 |
| hàng ngàn | hàng ngàn |
| hàng triệu | hàng triệu |
| gấp đôi | gấp đôi |
| gấp ba | gấp ba |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · LOÀI NHỆN DUY NHẤT SỐNG CẢ ĐỜI DƯỚI NƯỚC · 84.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:13.3 (13.3s) | L01 | Báo cáo thử nghiệm kỹ thuật hàng hải sinh học tối mật cấp độ đỏ! Toàn thể đội ngũ công trình sư hãy đeo kính lặn bảo hộ và kích hoạt đồng hồ đo áp suất, bởi vì cỗ máy sinh học mà chúng ta giải mã hôm nay sẽ phá vỡ mọi quy chuẩn tiến hóa trên Trái Đất. |  | Góc làm việc xưởng thiết kế tàu ngầm viễn tưởng: Trên bàn gỗ sồi trải rộng cuộn giấy can kỹ thuật xanh Prussian vẽ sơ đồ tàu ngầm Nautilus và các ống đồng; KHÔNG có chú nhện thuyền trưởng trong cảnh này; BÊN PHẢI có một bể kính nước ngọt với đám rong đuôi chó xanh biếc. |
| b02 | 00:13.3–00:19.8 (6.5s) | L33 | Quên đi những tàu ngầm hạt nhân bọc thép titan ngàn tấn của con người, hãy nhìn xuống một bụi rong đuôi chó tĩnh lặng dưới đáy hồ nước ngọt! |  | Cận cảnh chi tiết bụi rong đuôi chó tĩnh lặng dưới đáy hồ: Những bọt khí nhỏ li ti bám trên kẽ lá xanh biếc; KHÔNG có chú nhện thuyền trưởng trong cảnh này; tia sáng mặt trời chiếu rọi từ mặt nước mờ ảo. |
| b03 | 00:19.8–00:31.6 (11.8s) | L02 | Đối tượng mang mã định danh số 41 của chúng ta có tên khoa học là Argyroneta aquatica, nhưng giới kỹ sư đại dương gọi gã bằng một danh xưng đầy kính nể: Thuyền Trưởng Tàu Ngầm Tơ! |  | Cận cảnh trong bể nước: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) đứng hiên ngang trên một nhánh rong rêu, một chân chống nạnh, một chân chỉ về phía trước, mũ thuyền trưởng đội lệch đầ |
| b04 | 00:31.6–00:39.0 (7.4s) | L34 | Đây là loài nhện duy nhất trong số hơn 50.000 loài nhện trên khắp hành tinh từ bỏ hoàn toàn cõi cạn để di cư xuống định cư vĩnh viễn dưới lòng nước! | **50.000** · loài nhện duy nhất · R/380 · [0.35, 0.5] | Bản đồ phân bố tiến hóa sinh học: Hàng ngàn chấm đỏ đại diện cho 50.000 loài nhện cạn trên các lục địa; một vệt sáng xanh dương duy nhất lao xuống đáy hồ nước ngọt; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và g |
| b05 | 00:39.0–00:47.5 (8.5s) | L03 | Điều gây chấn động phòng thí nghiệm là sinh vật này hoàn toàn không có mang cá, không có vây bơi, mà vẫn giữ nguyên bộ phổi sách thở khí trời của tổ tiên loài nhện cạn. |  | Phân chia màn hình đối chiếu: BÊN TRÁI là một chú nhện nhà thông thường đang chới với dưới nước mắt trợn tròn hoảng loạn; BÊN PHẢI là chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) ung dung |
| b06 | 00:47.5–00:59.0 (11.5s) | L35 | Nếu bạn thả một con nhện nhà bình thường xuống nước, nó sẽ ngạt thở chìm lịm trong vài phút. Nhưng Thuyền Trưởng Tàu Ngầm Tơ lại có thể bơi lặn, săn mồi, ngủ ngáy, thậm chí giao phối và ấp trứng 24/7 suốt cả cuộc đời dưới đáy hồ! | **24/7** · sống dưới nước · R/360 · [0.75, 0.5] | Cận cảnh mặt nước hồ: Một chú nhện nhà rơi xuống nước đang hoảng hốt bơi chới với; phía dưới đáy hồ sâu, chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) thong dong bơi lặn quanh những cột ro |
| b07 | 00:59.0–01:05.4 (6.3s) | L04 | Báo cáo kỹ thuật trưởng, cảm biến sonar báo có một quả cầu thủy tinh đang phát sáng lơ lửng giữa đám rong rêu ạ! |  | Trong phòng điều khiển: cô trợ lý kỹ thuật thỏ trắng đeo kính bảo hộ, cầm bảng kẹp tài liệu đang nhìn vào màn hình radar sonar phát sáng xanh lục, ngón tay chỉ vào chấm sáng hình tròn; cạnh cô là một bảng kẹp tài liệu ghi dòng chữ Mật mã Tàu ngầm Tơ. |
| b08 | 01:05.4–01:17.0 (11.6s) | L05 | Đúng như cô trợ lý vừa phát hiện! Bí mật không nằm ở ma thuật siêu nhiên, mà nằm ở một công trình kiến trúc vi mô vĩ đại: Một quả chuông lặn dệt hoàn toàn bằng tơ kỵ nước, biến một kẻ thở bằng phổi thành chúa tể lòng hồ! |  | Toàn cảnh dưới đáy hồ: Một quả chuông tơ hình vòm trong suốt sáng rực ánh ngọc trai lơ lửng giữa khóm rong; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) đang đứng ở cửa chuông vẫy tay chà |
| b09 | 01:17.0–01:24.0 (7.0s) | L36 | Hôm nay, xưởng cơ khí sinh học của chúng ta sẽ tháo dỡ từng mắt tơ để xem gã kỹ sư tí hon này xây trạm không gian dưới nước như thế nào! |  | Cận cảnh bàn mổ xẻ thiết kế: cô trợ lý kỹ thuật thỏ trắng đeo kính bảo hộ, cầm bảng kẹp tài liệu cầm kính lúp và bút chì kỹ thuật chỉ vào mô hình chuông lặn tơ nhện vi mô; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng t |

### scene02 · TÀU NGẦM TƠ KỴ NƯỚC VÀ KHOANG KHÍ ÁP SUẤT · 95.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:11.9 (11.9s) | L06 | Hãy trải cuộn bản vẽ mặt cắt xanh Prussian lên bàn phân tích! Muốn xây một căn nhà chứa không khí dưới nước, thách thức cơ học đầu tiên là lực đẩy Ác-si-mét cực lớn sẽ thổi bay mọi cấu trúc nổi lên mặt hồ. | **ÁC-SI-MÉT** · kết cấu thủy lực · L/380 · [0.5, 0.4] | Bản vẽ thiết kế cơ học: Sơ đồ hình học tính toán lực đẩy Ác-si-mét; mũi tên màu đỏ hướng lên trên chỉ lực nâng bọt khí; mũi tên màu xanh hướng xuống chỉ các dây neo tơ; KHÔNG có chú nhện thuyền trưởng trong cảnh này. |
| b02 | 00:11.9–00:19.3 (7.5s) | L37 | Nhưng Thuyền Trưởng Tàu Ngầm Tơ đã giải bài toán kết cấu này bằng một giải pháp tân tiến không thua gì các kỹ sư khoan ngầm dầu khí ngoài khơi! |  | Sơ đồ lực học thủy tĩnh: Mũi tên đỏ chỉ lực đẩy Ác-si-mét hướng lên trời; các mũi tên xanh lục neo đa hướng kéo ghì xuống đáy; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) cầm mỏ lết đồng |
| b03 | 00:19.3–00:26.0 (6.6s) | L07 | Đầu tiên, gã chọn những nhánh rong rêu thủy sinh vững chắc nhất, rồi bắn hàng trăm sợi tơ neo đa hướng hình mạng nhện để cố định một khung dầm chịu lực. |  | Dưới đáy hồ: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) đang thoan thoắt bắn các sợi tơ vàng óng ánh neo chặt vào các cọng rong đuôi chó xung quanh, tạo thành một mạng lưới khung dầm bá |
| b04 | 00:26.0–00:37.3 (11.3s) | L38 | Điểm kỳ diệu nằm ở chỗ: Tơ của loài nhện này chứa protein kỵ nước siêu việt. Khi tiếp xúc với nước ngọt, các sợi tơ không hề bị mủn hay tan rã, mà đan kết lại thành một màng lưới dẻo dai tựa như màng cao su tổng hợp chịu áp lực cao! |  | Cận cảnh cấu trúc hiển vi của sợi tơ kỵ nước: Các phân tử protein đan xen khít khao phát sáng màu xanh ngọc bích; giọt nước chạm vào màng tơ bị trượt bắn ra ngoài như trượt trên lá sen; KHÔNG có chú nhện thuyền trưởng trong cảnh này. |
| b05 | 00:37.3–00:50.2 (12.9s) | L08 | Sau khi hệ khung neo đã căng cứng, gã bắt đầu nhả tơ dệt thành một chiếc vòm hình chuông úp ngược. Chiếc vòm tơ ban đầu xẹp lép như một chiếc dù nhảy lơ lửng giữa dòng nước. Nhưng làm thế nào để bơm đầy không khí vào một chiếc chuông ngập nước sâu dưới đáy hồ? |  | Cận cảnh chiếc vòm tơ ban đầu: Màng tơ xẹp lép lơ lửng như một chiếc dù nhảy chưa bung; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) bám ở đỉnh dù kiểm tra từng mắt lưới; ánh nắng từ mặt  |
| b06 | 00:50.2–00:55.4 (5.3s) | L09 | Kỹ sư ơi, tơ nhện dệt kín mít thế kia thì nước có thấm ngược vào làm ướt sũng tổ không ạ? |  | chú cá con ngơ ngác mắt tròn xoe, mang vây nhỏ nhắn bơi lội bơi sát vào màng tơ, mắt tròn xoe ngơ ngác, vây khẽ chạm vào thành chuông tơ; giọt nước đọng bên ngoài lăn tăn; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng t |
| b07 | 00:55.4–01:05.6 (10.2s) | L10 | Chú cá con ngơ ngác hoàn toàn yên tâm! Khoảng cách giữa các sợi nano tơ kỵ nước nhỏ đến mức sức căng bề mặt của nước biến màng tơ thành bức tường ngăn nước tuyệt đối! | **KỴ NƯỚC** · ngăn nước tuyệt đối · R/360 · [0.55, 0.45] | Phóng đại kính hiển vi vi mô: Bề mặt các sợi tơ kỵ nước nano đan khít nhau; các phân tử nước đọng thành giọt tròn xoe bên ngoài không thể xuyên qua; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su t |
| b08 | 01:05.6–01:15.2 (9.6s) | L39 | Nước bên ngoài không thể lọt vào một giọt, nhưng khí ga bên trong lại được giữ kín bưng. Bây giờ, chiếc chuông đã sẵn sàng, và màn vận chuyển khí thần sầu của thuyền trưởng tí hon chính thức bắt đầu! |  | Mặt cắt vi mô thành chuông: Bên ngoài là các phân tử nước màu xanh lam bị chặn đứng hoàn toàn bởi lớp nano kỵ nước; bên trong là các phân tử khí ga màu vàng óng được giữ kín bưng; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh man |
| b09 | 01:15.2–01:23.3 (8.1s) | L11 | Chưa hết đâu nhé! Để quả chuông tơ không bị biến dạng khi dòng nước hồ chảy xiết, Thuyền Trưởng Tàu Ngầm Tơ còn dệt thêm một lớp tơ gia cường thứ 2 bên trong lòng vòm. | **LỚP THỨ 2** · chống biến dạng · L/420 · [0.4, 0.5] | Kiểm định an toàn: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) đang dệt thêm một lớp tơ gia cường thứ hai bên trong lòng chuông, dùng trán húc thử vào thành chuông làm màng tơ nảy tưng t |
| b10 | 01:23.3–01:35.5 (12.3s) | L40 | Gã dùng đầu húc thử vào thành chuông để kiểm tra độ đàn hồi, giống hệt như các chuyên viên kiểm định độ an toàn vỏ tàu ngầm trước khi hạ thủy! Một công trình xây dựng dưới đáy nước hoàn hảo không cần đến một chiếc đinh hay một giọt keo công nghiệp nào! |  | Cận cảnh kiểm tra độ bền: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) dùng đầu và hai chân trước húc mạnh vào màng tơ chuông lặn; màng tơ đàn hồi co giãn nhịp nhàng như cao su tổng hợp k |

### scene03 · BỘ LÔNG QUẶP BỌT KHÍ VÀ MANG NHÂN TẠO 24 GIỜ · 107.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.8 (8.8s) | L12 | Hãy quan sát công nghệ vận tải khí độc nhất vô nhị của Thuyền Trưởng Tàu Ngầm Tơ! Gã ngoi lên mặt nước, nhưng không thò cả người lên để hít thở như rùa hay cá voi. |  | Mặt nước hồ: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) nhô phần chóp bụng và cặp chân sau lên khỏi mặt nước, phần đầu và mắt vẫn chìm bên dưới; mặt nước lăn tăn gợn sóng phản chiếu bầu |
| b02 | 00:08.8–00:15.4 (6.5s) | L41 | Gã chỉ nhô đúng phần chóp bụng và cặp chân sau lên khỏi mặt thoáng, thực hiện một cú giật mình chớp nhoáng rồi lặn ngược xuống đáy! |  | Góc nhìn cận cảnh mặt thoáng: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) chỉ nhô đúng phần chóp bụng và cặp chân sau lên khỏi mặt hồ, thực hiện một cú giật mình chớp nhoáng tạo ra những |
| b03 | 00:15.4–00:30.2 (14.8s) | L13 | Toàn bộ vùng bụng và chân sau của gã được bao phủ bởi hàng triệu sợi lông kỵ nước siêu nhỏ với mật độ dày đặc. Khi gã quẫy mình giật ngược xuống nước, lớp lông này bẫy chặt một lớp không khí bao quanh bụng, biến phần thân dưới thành một quả cầu bạc lấp lánh như gương soi! |  | Cận cảnh cực đại: Phần bụng của chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) được bọc kín bởi một lớp bọt khí sáng loáng như phủ một lớp bạc tráng gương; chú nhện lặn chuông hoạt hình ngộ |
| b04 | 00:30.2–00:35.3 (5.1s) | L42 | Đây chính là nguồn gốc tên gọi Argyroneta trong tiếng Hy Lạp cổ, nghĩa là kẻ dệt sợi bạc! | **Argyroneta** · kẻ dệt sợi bạc · L/360 · [0.5, 0.5] | Từ điển bách khoa cổ điển: Cuốn sách cổ Hy Lạp mở trang ghi chữ Argyroneta phát sáng vàng kim; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) soi mình trước quả cầu bạc bọc quanh bụng như m |
| b05 | 00:35.3–00:42.3 (7.0s) | L14 | Gã ôm quả bọt khí bạc bơi hối hả xuống đáy, luồn vào bên dưới vòm tơ xẹp lép, rồi dùng hai chân sau gạt mạnh bọt khí giải phóng vào trong |  | Đường hầm bơi lội: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) như một quả ngư lôi bạc phóng vụt từ mặt hồ xuống đáy, hai chân sau ôm chặt bọt khí; BÊN TRÁI là quả chuông lặn đang phình  |
| b06 | 00:42.3–00:50.5 (8.2s) | L43 | chuông. Gã lặp lại chuyến xe buýt con thoi này từ 20 đến 30 chuyến liên tục, cho đến khi quả chuông căng tròn bóng loáng bằng hạt đậu phộng, tỏa sáng lung linh giữa đáy bùn! | **20-30 LẦN** · con thoi nạp khí · R/360 · [0.75, 0.5] | Hành trình xe buýt con thoi: Dãy 5 hình bóng chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) liên tiếp bơi lên bơi xuống giữa mặt hồ và đáy bùn; quả chuông tơ từ từ phồng to từ một hạt vừng  |
| b07 | 00:50.5–01:05.2 (14.7s) | L15 | Nhưng điều chấn động khoa học thế giới vừa được hai giáo sư Seymour và Hetz công bố trên Tạp chí Sinh học Thực nghiệm: Quả chuông tơ này không chỉ là một chiếc bình dưỡng khí tĩnh! Khi nhện tiêu thụ oxy bên trong, nồng độ oxy trong chuông tụt xuống thấp hơn lượng oxy hòa tan trong nước xung quanh. |  | Phòng thí nghiệm sinh học: Hai giáo sư hoạt hình mặc áo blouse trắng (Seymour và Hetz) đang cầm kính hiển vi và ống đo khí soi vào quả chuông tơ; biểu đồ nồng độ oxy hiển thị trên bảng phấn xanh. |
| b08 | 01:05.2–01:18.2 (13.0s) | L16 | Sự chênh lệch áp suất riêng phần biến toàn bộ bề mặt quả chuông thành một chiếc mang nhân tạo khổng lồ! Oxy từ nước xung quanh tự động thẩm thấu xuyên qua màng tơ chảy vào chuông, trong khi khí CO2 thở ra tự khuếch tán ra ngoài hồ! |  | Sơ đồ nguyên lý mang nhân tạo: Quả chuông tơ phát sáng; các mũi tên màu xanh dương (Oxy) từ nước tự động thẩm thấu xuyên qua màng tơ vào trong chuông; các mũi tên màu xám (CO2) khuếch tán ra ngoài hồ; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương,  |
| b09 | 01:18.2–01:27.0 (8.8s) | L44 | Nhờ động cơ thẩm thấu thụ động này, một lượng khí ban đầu có thể cung cấp dưỡng khí cho nhện sống suốt 24 giờ liên tục mà không cần bơi lên mặt hồ lấy thêm khí! | **24 GIỜ** · thở thẩm thấu · R/360 · [0.75, 0.5] | Đồng hồ sinh tồn 24 giờ: Mặt đồng hồ cơ khí bằng đồng hiển thị 24h; bên trong quả chuông lặn, chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) ung dung ngủ ngon lành trên võng tơ; các luồng o |
| b10 | 01:27.0–01:38.8 (11.8s) | L17 | Tuy nhiên, động cơ mang nhân tạo này cũng có một nhược điểm vật lý không thể tránh khỏi: Khí Nitơ trong bọt khí cũng dần dần hòa tan và thất thoát ra ngoài nước. Khi lượng Nitơ giảm đi, quả chuông sẽ từ từ xẹp lại sau 1-2 ngày. | **1-2 NGÀY** · chu kỳ nạp khí · L/420 · [0.45, 0.5] | Đồng hồ đo áp suất Nitơ: Đồng hồ đo khí gắn trên thành chuông kim đang chỉ vạch vàng cảnh báo hao hụt Nitơ; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) đeo đồng hồ bấm giờ trên cổ chân,  |
| b11 | 01:38.8–01:47.5 (8.7s) | L45 | Chính vì vậy, Thuyền Trưởng Tàu Ngầm Tơ phải thực hiện một chuyến tuần tra bảo dưỡng định kỳ mỗi ngày 1 lần, ngoi lên mặt nước mang về vài bọt khí tươi mới để nạp lại áp suất cho căn cứ! |  | Chuyến tuần tra bảo dưỡng: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) đeo túi đồ nghề sửa chữa, ngoi lên mặt nước quặp một bọt khí mới toanh mang xuống nạp vào đỉnh chuông lặn; đồng hồ  |

### scene04 · NHỆN ĐỰC TO HƠN NHỆN CÁI 30% ĐỂ GIỮ CHUÔNG LẶN · 98.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.0 (7.0s) | L18 | Bây giờ, chúng ta bước vào hồ sơ gia đình đầy bi hài của Thuyền Trưởng Tàu Ngầm Tơ! Nếu bạn đã quen với quy luật tàn khốc trên cạn của loài nhện, |  | Bức tranh hài hước so sánh: BÊN TRÁI trên cạn, một nàng nhện khổng lồ dữ tợn cầm dao nĩa đuổi theo chú nhện đực nhỏ xíu toát mồ hôi; BÊN PHẢI dưới nước, chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao  |
| b02 | 00:07.0–00:15.2 (8.2s) | L46 | nơi các nàng nhện cái khổng lồ thường xơi tái chú nhện đực gầy gò ngay sau đêm tân hôn, thì dưới đáy hồ nước ngọt, tạo hóa đã lật ngược ván cờ 100 80 độ! |  | Tương phản sinh học: BÊN TRÁI trên cạn, một nàng nhện cái khổng lồ đang hung dữ cầm nĩa; BÊN PHẢI dưới nước, chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) vạm vỡ cơ bắp đang mỉm cười nháy  |
| b03 | 00:15.2–00:23.1 (7.9s) | L19 | Ở loài nhện lặn chuông, con đực có chiều dài cơ thể từ 10-15mm, trong khi con cái chỉ đạt từ 8-13mm. | **10-15 MM** · con đực to hơn 30% · R/360 · [0.4, 0.45] | Phòng đo đạc thể hình: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) đứng trên bục cân đo đạc, cao to vạm vỡ, cơ bắp cuồn cuộn với thước đo 15mm; BÊN CẠNH là nàng nhện cái nhỏ nhắn 10mm đe |
| b04 | 00:23.1–00:32.4 (9.3s) | L47 | Nhện đực to hơn nhện cái đến 30% và sở hữu sải chân dài cơ bắp vượt trội! Đây là một hiện tượng dị hình giới tính đảo ngược cực kỳ hiếm hoi trong toàn bộ thế giới tám | **+30%** · đực lớn hơn cái · R/360 · [0.35, 0.5] | Bàn cân so sánh kích thước: BÊN TRÁI chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) (nhện đực) dài 15mm sải chân vạm vỡ; BÊN PHẢI nàng nhện cái nhỏ nhắn 12mm e ấp; chiếc thước kẹp cơ khí đo |
| b05 | 00:32.4–00:38.5 (6.1s) | L20 | chân! Ủa các bác kỹ sư ơi, sao nhện đực dưới nước lại được ưu ái ăn sung mặc sướng to con thế ạ? |  | Một đàn cá con và sinh vật đáy hồ tí hon xúm lại quanh chiếc bảng phấn, ngước nhìn lên chăm chú lắng nghe; BÊN PHẢI cô trợ lý kỹ thuật thỏ trắng đeo kính bảo hộ, cầm bảng kẹp tài liệu cầm thước chỉ vào hình vẽ nhện đực bơi lội. |
| b06 | 00:38.5–00:50.8 (12.3s) | L21 | Bé con thắc mắc rất chí lý! Lý do là vì di chuyển trong môi trường nước đặc quánh đòi hỏi lực cản thủy động học cực lớn. Nhện đực không chịu ngồi yên một chỗ, gã phải liên tục bơi đường dài đi tuần tra và tìm kiếm bạn gái giữa các bụi rong. |  | chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) đang bơi lội dũng mãnh giữa dòng nước xiết, vượt qua các xoáy nước nhỏ để mang bọt khí khổng lồ về tổ; cơ thể to lớn và sải chân dài giúp gã g |
| b07 | 00:50.8–00:56.9 (6.1s) | L48 | Thân hình to lớn và đôi chân dài giúp gã bơi nhanh hơn, quặp được bọt khí to hơn và không bị dòng nước cuốn trôi! |  | Cảnh bơi lội vượt dòng xiết: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) sải 8 chiếc chân dài cơ bắp quặp quả bọt khí khổng lồ rẽ nước bơi băng băng qua dòng chảy xiết; chú cá con ngơ ng |
| b08 | 00:56.9–01:08.8 (11.9s) | L22 | Khi tìm thấy chuông lặn của một nàng nhện ưng ý, chàng nhện đực không lao vào ẩu đả. Gã lịch sự xây ngay một chiếc chuông lặn phụ ngay sát vách căn hộ của nàng, rồi dệt một đường hầm tơ nối thông hai phòng khách lại với nhau! |  | Biệt thự thông tầng dưới đáy nước: Hai quả chuông lặn đặt cạnh nhau được nối với nhau bằng một đường ống hầm tơ trong suốt; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) và nàng nhện cái n |
| b09 | 01:08.8–01:15.5 (6.7s) | L49 | Một căn biệt thự thông tầng dưới đáy nước được hình thành lãng mạn vô cùng, nơi con đực bảo vệ đàn con mà không hề lo sợ bị người tình ăn thịt! | **2 PHÒNG** · biệt thự thông tầng · R/360 · [0.5, 0.5] | Bản vẽ phối cảnh kiến trúc: Hai quả chuông lặn nối liền nhau bằng đường hầm tơ trong suốt; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) và nàng nhện cái ngồi hai bên đường hầm cụng ly nướ |
| b10 | 01:15.5–01:27.2 (11.7s) | L23 | Sau tuần trăng mật ngọt ngào, nàng nhện cái bắt đầu công việc thiêng liêng nhất của một người mẹ: Đẻ từ 50-100 trứng bọc trong một chiếc kén tơ trắng muốt, treo lơ lửng ở phần vòm cao nhất của quả chuông lặn! | **50-100** · kén ấp trong chuông · R/380 · [0.5, 0.35] | Phòng trẻ sơ sinh dưới nước: Bên trong quả chuông lặn, một chiếc kén tơ hình cầu trắng muốt chứa đầy những quả trứng tròn nhỏ treo ở vòm trên; hàng chục chú nhện con tí hon mới nở bơi quanh với những bọt khí li ti. |
| b11 | 01:27.2–01:38.5 (11.4s) | L50 | Nơi đây chứa lượng oxy tinh khiết nhất để nuôi dưỡng các nhện con. Khi các chú nhện con chào đời, chúng bơi lội ngay trong phòng khách dưới nước của bố mẹ, học cách quặp bọt khí đầu tiên trước khi tự lập xây dựng vương quốc riêng! |  | Phòng trẻ sơ sinh dưới nước: Bên trong vòm chuông trên cao, chiếc kén tơ tròn xoe chứa hàng chục nhện con tí hon đang chui ra; các bé nhện con đeo kính bơi tí hon tập quặp những bọt khí nhỏ li ti. |

### scene05 · TÀU NGẦM SĂN MỒI VÀ GIẤC NGỦ ĐÔNG ĐÓNG BĂNG · 88.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.4 (8.4s) | L24 | Hãy chứng kiến cỗ máy săn ngầm hoạt động trong điều kiện chiến trường thực tế! Thuyền Trưởng Tàu Ngầm Tơ không cần bơi lội rượt đuổi con mồi cho tốn calo. |  | Hệ thống bẫy mạng nhện dưới nước: Từ quả chuông lặn của chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon), hàng chục sợi tơ trong suốt tỏa ra các nhánh rong rêu như một mạng nhện radar vô hình |
| b02 | 00:08.4–00:16.6 (8.2s) | L51 | Từ quả chuông lặn trung tâm, gã giăng ra hàng chục sợi tơ bẫy vô hình kết nối trực tiếp với các cành rong rêu xung quanh như những đường dây điện thoại bảo vệ căn cứ! |  | Mạng lưới radar dây tơ: Từ quả chuông lặn của chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon), hàng chục sợi tơ mảnh phát sáng chạy dài đến các bụi cây thủy sinh như mạng dây điện thoại cảnh |
| b03 | 00:16.6–00:30.7 (14.1s) | L25 | Gã ngồi thảnh thơi bên trong quả chuông ấm áp, chỉ thò những đầu móng chân nhạy cảm ra ngoài chạm vào các sợi tơ kích hoạt. Khi một con ấu trùng chuồn chuồn, bọ gậy hay một chú cá nhỏ bơi ngang qua vô tình chạm vào sợi tơ cảm biến, xung động rung lắc truyền thẳng vào màng chuông với tốc độ ánh sáng! |  | chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) ngồi thư thái trên chiếc ghế tựa bằng tơ bên trong chuông, hai chân trước thò ra mép cửa chạm nhẹ vào sợi tơ kích hoạt; ánh mắt tập trung theo |
| b04 | 00:30.7–00:38.8 (8.1s) | L26 | Vút! Thuyền trưởng phóng vọt ra khỏi cửa hầm, tung hai chiếc kìm kẹp chứa nọc độc tiêm thẳng vào con mồi làm nạn nhân tê liệt trong tích tắc! | **NỌC ĐỘC** · hạ gục tức thì · R/380 · [0.6, 0.5] | Hành động chớp nhoáng: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) phóng vụt ra khỏi chuông, hai chiếc kìm kẹp mở rộng kẹp trúng một ấu trùng chuồn chuồn bơi ngang; xung kích tỏa ra bọt  |
| b05 | 00:38.8–00:47.9 (9.1s) | L52 | Sau đó, gã kéo chiến lợi phẩm ngược vào bên trong quả chuông lặn khô ráo để thưởng thức bữa tiệc thịnh soạn mà không sợ bị các loài cá săn mồi khác cướp mất miếng ăn! |  | Phòng tiệc bên trong chuông lặn: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) ngồi thảnh thơi trên chiếc ghế bành bằng tơ, dùng dao nĩa tí hon thưởng thức món ấu trùng bọ gậy khô ráo; ngo |
| b06 | 00:47.9–00:56.4 (8.5s) | L27 | Nếu bất ngờ có một con cá chép đói khát bơi tới tấn công cắn rách vòm tơ, thuyền trưởng tí hon sẽ phản ứng thế nào? Gã không hề hoảng loạn! |  | Tình huống khẩn cấp: Một cái đầu cá chép to lớn hung dữ bơi tới cắn rách mép ngoài vòm tơ; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) nhanh như chớp luồn qua cửa đáy thoát hiểm núp vào  |
| b07 | 00:56.4–01:09.9 (13.5s) | L53 | Với tốc độ cơ động cực nhanh, gã lập tức thoát hiểm qua cửa đáy khẩn cấp, núp vào khe đá ngầm. Đợi kẻ thù bỏ đi, gã quay lại hiện trường và chỉ mất chưa đầy 30 phút để vá lành mọi vết rách bằng những đường tơ kỵ nước mới toanh, tiếp tục làm chủ pháo đài dưới nước! | **30 PHÚT** · vá lành pháo đài · R/360 · [0.75, 0.5] | Kế hoạch thoát hiểm khẩn cấp: Vòm tơ bị cá chép cắn rách, chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) phóng vọt qua cửa đáy thoát hiểm núp vào khe đá; sau khi cá bỏ đi, chú nhện lặn chuô |
| b08 | 01:09.9–01:19.2 (9.4s) | L28 | Thậm chí vào mùa đông băng giá, khi nhiệt độ nước tụt xuống 0°C và mặt hồ đóng băng dày cộp cắt đứt hoàn toàn nguồn không khí mặt thoáng, cỗ máy sinh học này vẫn vận hành ngoan cường! | **0°C** · ngủ đông đáy bùn · R/360 · [0.5, 0.55] | Mùa đông giá rét: Mặt hồ bên trên đóng băng thành tảng đá trắng xóa lạnh lẽo; sâu dưới đáy bùn ấm áp, chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) cuộn tròn ngủ say sưa bên trong chiếc ké |
| b09 | 01:19.2–01:28.4 (9.2s) | L54 | Nhện lặn chuông bò xuống lớp bùn sâu nhất, dệt một chiếc kén tơ siêu dày bọc kín một túi khí nhỏ, hạ thấp thân nhiệt và nhịp tim để ngủ đông suốt nhiều tháng ròng rã cho đến khi mùa xuân tan băng! |  | Giấc ngủ đông dưới đáy băng: Mặt hồ phủ lớp băng dày tuyết trắng; sâu dưới lớp bùn ấm áp, chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) cuộn tròn ngủ say trong kén tơ siêu dày ôm một túi k |

### scene06 · GIỚI HẠN CHỈ LÀ DO BẠN CHƯA DỆT CHUÔNG KHÍ · 60.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.2 (7.2s) | L29 | Hồ sơ vũ khí số 41 chính thức khép lại với những thông số kinh ngạc! Nhện Lặn Chuông minh chứng hùng hồn cho bài học tiến hóa vĩ đại: | **KỲ QUAN** · tàu ngầm tơ · L/380 · [0.5, 0.4] | Bức tranh toàn cảnh tổng kết: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) đứng trên đỉnh quả chuông lặn pha lê tỏa sáng lung linh giữa đáy hồ, tay cầm bánh lái tàu ngầm bằng đồng thau, x |
| b02 | 00:07.2–00:19.0 (11.9s) | L55 | Khi môi trường sống cạn kiệt cơ hội, bạn không nhất thiết phải thay đổi toàn bộ nội tạng để thích nghi. Thuyền Trưởng Tàu Ngầm Tơ không mọc ra mang cá, gã chỉ đơn giản dệt nên một công nghệ đem theo bầu trời của chính mình xuống đáy đại dương! |  | Biểu tượng triết lý tiến hóa: Hình vẽ cây tiến hóa với các nhánh cạn kiệt cơ hội; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) đứng trên đỉnh một mỏm đá ngầm, tay cầm cờ hải quân tung bay |
| b03 | 00:19.0–00:25.9 (6.8s) | L30 | Nếu trong cuộc sống bạn cảm thấy ngột ngạt và lạc lõng giữa một môi trường xa lạ, hãy nhớ tới chú nhện lặn chuông: |  | Hình ảnh ẩn dụ truyền cảm hứng: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) nhỏ bé nhưng kiên cường đang dệt một quả chuông sáng lấp lánh bao bọc lấy một trái tim màu đỏ giữa biển đêm tă |
| b04 | 00:25.9–00:34.6 (8.8s) | L56 | Đôi khi, chỉ cần một quả chuông kiên định dệt bằng sự sáng tạo và nỗ lực, bạn hoàn toàn có thể tự tạo ra bầu không khí thành công cho riêng mình ngay giữa nghịch cảnh! |  | Hình ảnh truyền cảm hứng: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) tươi cười rạng rỡ bên trong quả chuông lặn tỏa sáng lung linh giữa đáy hồ tối; xung quanh là dòng nước lạnh giá nhưn |
| b05 | 00:34.6–00:44.7 (10.1s) | L31 | Nếu được trang bị một bộ đồ lặn bong bóng như nhện lặn chuông, bạn muốn lặn xuống đáy hồ nào để khám phá thế giới vi mô kỳ ảo? Hãy để lại ý kiến thú vị của bạn ở phần bình luận bên dưới nhé! |  | Khán giả và chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon): Một bạn nhỏ hoạt hình đeo chiếc ba lô bong bóng khí bơi lội tung tăng bên cạnh chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu  |
| b06 | 00:44.7–00:52.7 (8.0s) | L32 | Còn bây giờ, hãy nhìn vào bóng đen bí ẩn của hồ sơ số 42! Một sinh vật biển kỳ dị chán ghét đại dương, bỏ nước lên cạn leo trèo trên cây ngập mặn, |  | Teaser bí ẩn bóng đen tập 42 (TASTE-68): Giữa bãi bùn rừng ngập mặn mù sương, một cái bóng đen bí ẩn (solid black silhouette) hình con cá có vây chân đang trèo lên rễ cây đước, hai con mắt lồi to tướng gắn dấu hỏi chấm '?', phía sau là đại dương xa xăm. |
| b07 | 00:52.7–01:00.9 (8.2s) | L57 | nếu ngâm nước quá lâu thì lại bị chết đuối, và mỗi khi nuốt mồi lại phải tụt cả hai nhãn cầu mắt xuống tận cổ họng! Bạn có đoán được quái kiệt hai mang này là ai không? |  | Cận cảnh hình bóng teaser tập 42 (TASTE-68): Bóng đen một con cá kỳ dị hai mắt lồi to tướng ngồi trên cành cây đước bãi lầy, một tay bịt mũi ôm cổ ho sặc sụa dưới nước với dấu hỏi '?' lớn màu vàng. |

## 5. Phân cảnh Shorts — từng beat

Banner: **TÀU NGẦM TƠ NHỆN / SỐNG 24H DƯỚI NƯỚC?!** · giọng 41.9s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Bạn có tin trên đời có một loài nhện thở bằng phổi nhưng cả cuộc đời lại sống dưới đáy nước? |  |
| s02 | 00:05.8 | S02 | Đây là Nhện Lặn Chuông, dài chỉ 10-15mm nhưng sở hữu công nghệ tàu ngầm vô tiền khoáng hậu! | **10-15 MM** · kích thước tí hon · R/520 · [0.5, 0.45] |
| s03 | 00:11.8 | S03 | Gã ngoi lên mặt nước, dùng bộ lông kỵ nước quặp chặt một bọt khí bạc quanh bụng rồi lặn xuống đáy hồ. | **BỌC BẠC** · quặp bọt khí · L/560 · [0.5, 0.55] |
| s04 | 00:17.4 | S04 | Tại đây, gã dệt một chiếc vòm tơ hình chuông úp ngược vào rong rêu, bơm đầy bọt khí vào trong để làm trạm không gian dưới nước! |  |
| s05 | 00:24.1 | S05 | Điều chấn động là màng tơ này hoạt động như một chiếc mang nhân tạo, | **MANG TƠ** · tự hút oxy từ nước · R/500 · [0.5, 0.4] |
| s06 | 00:27.1 | S08 | tự hút oxy hòa tan từ nước xung quanh để gã thở suốt 24 giờ mà không cần ngoi lên mặt hồ! | **24 GIỜ** · thở dưới nước · L/620 · [0.5, 0.5] |
| s07 | 00:32.6 | S06 | Từ ăn ngủ, săn mồi đến đẻ trứng, gã làm trọn vẹn trong bong bóng không khí kỳ diệu, |  |
| s08 | 00:37.0 | S07 | chứng minh giới hạn sinh tồn chỉ là chuyện nhỏ trước kỹ nghệ đỉnh cao của thiên nhiên! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo thử nghiệm kỹ thuật hàng hải sinh học tối mật cấp độ đỏ! Toàn thể đội ngũ công trình sư hãy đeo kính lặn bảo hộ và kích hoạt đồng hồ đo áp suất, bởi vì cỗ máy sinh học mà chúng ta giải mã hôm nay sẽ phá vỡ mọi quy chuẩn tiến hóa trên Trái Đất.". Bố cục: Góc làm việc xưởng thiết kế tàu ngầm viễn tưởng: Trên bàn gỗ sồi trải rộng cuộn giấy can kỹ thuật xanh Prussian vẽ sơ đồ tàu ngầm Nautilus và các ống đồng; KHÔNG có chú nhện thuyền trưởng trong cảnh này; BÊN PHẢI có một bể kính nước ngọt với đám rong đuôi chó xanh biếc.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đối tượng mang mã định danh số 41 của chúng ta có tên khoa học là Argyroneta aquatica, nhưng giới kỹ sư đại dương gọi gã bằng một danh xưng đầy kính nể: Thuyền Trưởng Tàu Ngầm Tơ!". Bố cục: Cận cảnh trong bể nước: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) đứng hiên ngang trên một nhánh rong rêu, một chân chống nạnh, một chân chỉ về phía trước, mũ thuyền trưởng đội lệch đầy tự tin; BÊN PHẢI là mô hình tàu ngầm viễn tưởng mini vỏ đồng thau rỉ sét.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Điều gây chấn động phòng thí nghiệm là sinh vật này hoàn toàn không có mang cá, không có vây bơi, mà vẫn giữ nguyên bộ phổi sách thở khí trời của tổ tiên loài nhện cạn.". Bố cục: Phân chia màn hình đối chiếu: BÊN TRÁI là một chú nhện nhà thông thường đang chới với dưới nước mắt trợn tròn hoảng loạn; BÊN PHẢI là chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) ung dung nằm ngửa trên chiếc võng tơ dưới đáy hồ, hai chân gác chữ ngũ, miệng ngậm cọng cỏ nước.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo kỹ thuật trưởng, cảm biến sonar báo có một quả cầu thủy tinh đang phát sáng lơ lửng giữa đám rong rêu ạ!". Bố cục: Trong phòng điều khiển: cô trợ lý kỹ thuật thỏ trắng đeo kính bảo hộ, cầm bảng kẹp tài liệu đang nhìn vào màn hình radar sonar phát sáng xanh lục, ngón tay chỉ vào chấm sáng hình tròn; cạnh cô là một bảng kẹp tài liệu ghi dòng chữ Mật mã Tàu ngầm Tơ.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đúng như cô trợ lý vừa phát hiện! Bí mật không nằm ở ma thuật siêu nhiên, mà nằm ở một công trình kiến trúc vi mô vĩ đại: Một quả chuông lặn dệt hoàn toàn bằng tơ kỵ nước, biến một kẻ thở bằng phổi thành chúa tể lòng hồ!". Bố cục: Toàn cảnh dưới đáy hồ: Một quả chuông tơ hình vòm trong suốt sáng rực ánh ngọc trai lơ lửng giữa khóm rong; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) đang đứng ở cửa chuông vẫy tay chào thân thiện; BÊN TRÁI cô trợ lý kỹ thuật thỏ trắng đeo kính bảo hộ, cầm bảng kẹp tài liệu đang đeo kính lặn ngó vào trầm trồ.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy trải cuộn bản vẽ mặt cắt xanh Prussian lên bàn phân tích! Muốn xây một căn nhà chứa không khí dưới nước, thách thức cơ học đầu tiên là lực đẩy Ác-si-mét cực lớn sẽ thổi bay mọi cấu trúc nổi lên mặt hồ.". Bố cục: Bản vẽ thiết kế cơ học: Sơ đồ hình học tính toán lực đẩy Ác-si-mét; mũi tên màu đỏ hướng lên trên chỉ lực nâng bọt khí; mũi tên màu xanh hướng xuống chỉ các dây neo tơ; KHÔNG có chú nhện thuyền trưởng trong cảnh này.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đầu tiên, gã chọn những nhánh rong rêu thủy sinh vững chắc nhất, rồi bắn hàng trăm sợi tơ neo đa hướng hình mạng nhện để cố định một khung dầm chịu lực.". Bố cục: Dưới đáy hồ: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) đang thoan thoắt bắn các sợi tơ vàng óng ánh neo chặt vào các cọng rong đuôi chó xung quanh, tạo thành một mạng lưới khung dầm bát giác vững chắc; các mối nối tơ siết chặt.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sau khi hệ khung neo đã căng cứng, gã bắt đầu nhả tơ dệt thành một chiếc vòm hình chuông úp ngược. Chiếc vòm tơ ban đầu xẹp lép như một chiếc dù nhảy lơ lửng giữa dòng nước. Nhưng làm thế nào để bơm đầy không khí vào một chiếc chuông ngập nước sâu dưới đáy hồ?". Bố cục: Cận cảnh chiếc vòm tơ ban đầu: Màng tơ xẹp lép lơ lửng như một chiếc dù nhảy chưa bung; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) bám ở đỉnh dù kiểm tra từng mắt lưới; ánh nắng từ mặt nước xuyên qua làn nước xanh rọi xuống.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kỹ sư ơi, tơ nhện dệt kín mít thế kia thì nước có thấm ngược vào làm ướt sũng tổ không ạ?". Bố cục: chú cá con ngơ ngác mắt tròn xoe, mang vây nhỏ nhắn bơi lội bơi sát vào màng tơ, mắt tròn xoe ngơ ngác, vây khẽ chạm vào thành chuông tơ; giọt nước đọng bên ngoài lăn tăn; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) đứng bên trong mỉm cười gật đầu.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chú cá con ngơ ngác hoàn toàn yên tâm! Khoảng cách giữa các sợi nano tơ kỵ nước nhỏ đến mức sức căng bề mặt của nước biến màng tơ thành bức tường ngăn nước tuyệt đối!". Bố cục: Phóng đại kính hiển vi vi mô: Bề mặt các sợi tơ kỵ nước nano đan khít nhau; các phân tử nước đọng thành giọt tròn xoe bên ngoài không thể xuyên qua; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) tự hào giơ hai ngón tay cái.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa hết đâu nhé! Để quả chuông tơ không bị biến dạng khi dòng nước hồ chảy xiết, Thuyền Trưởng Tàu Ngầm Tơ còn dệt thêm một lớp tơ gia cường thứ 2 bên trong lòng vòm.". Bố cục: Kiểm định an toàn: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) đang dệt thêm một lớp tơ gia cường thứ hai bên trong lòng chuông, dùng trán húc thử vào thành chuông làm màng tơ nảy tưng tưng như lò xo đệm nhún; BÊN PHẢI cô trợ lý kỹ thuật thỏ trắng đeo kính bảo hộ, cầm bảng kẹp tài liệu cầm bảng chấm điểm an toàn tick V.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy quan sát công nghệ vận tải khí độc nhất vô nhị của Thuyền Trưởng Tàu Ngầm Tơ! Gã ngoi lên mặt nước, nhưng không thò cả người lên để hít thở như rùa hay cá voi.". Bố cục: Mặt nước hồ: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) nhô phần chóp bụng và cặp chân sau lên khỏi mặt nước, phần đầu và mắt vẫn chìm bên dưới; mặt nước lăn tăn gợn sóng phản chiếu bầu trời mây trắng.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn bộ vùng bụng và chân sau của gã được bao phủ bởi hàng triệu sợi lông kỵ nước siêu nhỏ với mật độ dày đặc. Khi gã quẫy mình giật ngược xuống nước, lớp lông này bẫy chặt một lớp không khí bao quanh bụng, biến phần thân dưới thành một quả cầu bạc lấp lánh như gương soi!". Bố cục: Cận cảnh cực đại: Phần bụng của chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) được bọc kín bởi một lớp bọt khí sáng loáng như phủ một lớp bạc tráng gương; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) cười toe toét ngắm nhìn chiếc bụng tròn phúng phính lấp lánh của mình.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gã ôm quả bọt khí bạc bơi hối hả xuống đáy, luồn vào bên dưới vòm tơ xẹp lép, rồi dùng hai chân sau gạt mạnh bọt khí giải phóng vào trong chuông.". Bố cục: Đường hầm bơi lội: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) như một quả ngư lôi bạc phóng vụt từ mặt hồ xuống đáy, hai chân sau ôm chặt bọt khí; BÊN TRÁI là quả chuông lặn đang phình to dần sau mỗi chuyến xe buýt.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng điều chấn động khoa học thế giới vừa được hai giáo sư Seymour và Hetz công bố trên Tạp chí Sinh học Thực nghiệm: Quả chuông tơ này không chỉ là một chiếc bình dưỡng khí tĩnh! Khi nhện tiêu thụ oxy bên trong, nồng độ oxy trong chuông tụt xuống thấp hơn lượng oxy hòa tan trong nước xung quanh.". Bố cục: Phòng thí nghiệm sinh học: Hai giáo sư hoạt hình mặc áo blouse trắng (Seymour và Hetz) đang cầm kính hiển vi và ống đo khí soi vào quả chuông tơ; biểu đồ nồng độ oxy hiển thị trên bảng phấn xanh.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sự chênh lệch áp suất riêng phần biến toàn bộ bề mặt quả chuông thành một chiếc mang nhân tạo khổng lồ! Oxy từ nước xung quanh tự động thẩm thấu xuyên qua màng tơ chảy vào chuông, trong khi khí CO2 thở ra tự khuếch tán ra ngoài hồ!". Bố cục: Sơ đồ nguyên lý mang nhân tạo: Quả chuông tơ phát sáng; các mũi tên màu xanh dương (Oxy) từ nước tự động thẩm thấu xuyên qua màng tơ vào trong chuông; các mũi tên màu xám (CO2) khuếch tán ra ngoài hồ; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) thư thái hít thở bên trong.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuy nhiên, động cơ mang nhân tạo này cũng có một nhược điểm vật lý không thể tránh khỏi: Khí Nitơ trong bọt khí cũng dần dần hòa tan và thất thoát ra ngoài nước. Khi lượng Nitơ giảm đi, quả chuông sẽ từ từ xẹp lại sau 1-2 ngày.". Bố cục: Đồng hồ đo áp suất Nitơ: Đồng hồ đo khí gắn trên thành chuông kim đang chỉ vạch vàng cảnh báo hao hụt Nitơ; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) đeo đồng hồ bấm giờ trên cổ chân, chuẩn bị cho chuyến bay tuần tra nạp khí mới.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bây giờ, chúng ta bước vào hồ sơ gia đình đầy bi hài của Thuyền Trưởng Tàu Ngầm Tơ! Nếu bạn đã quen với quy luật tàn khốc trên cạn của loài nhện,". Bố cục: Bức tranh hài hước so sánh: BÊN TRÁI trên cạn, một nàng nhện khổng lồ dữ tợn cầm dao nĩa đuổi theo chú nhện đực nhỏ xíu toát mồ hôi; BÊN PHẢI dưới nước, chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) lực lưỡng to lớn bơi lội ung dung bên cạnh nàng nhện cái nhỏ nhắn dễ thương.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở loài nhện lặn chuông, con đực có chiều dài cơ thể từ 10-15mm, trong khi con cái chỉ đạt từ 8-13mm.". Bố cục: Phòng đo đạc thể hình: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) đứng trên bục cân đo đạc, cao to vạm vỡ, cơ bắp cuồn cuộn với thước đo 15mm; BÊN CẠNH là nàng nhện cái nhỏ nhắn 10mm đeo nơ hồng đang ngước nhìn ngưỡng mộ.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ủa các bác kỹ sư ơi, sao nhện đực dưới nước lại được ưu ái ăn sung mặc sướng to con thế ạ?". Bố cục: Một đàn cá con và sinh vật đáy hồ tí hon xúm lại quanh chiếc bảng phấn, ngước nhìn lên chăm chú lắng nghe; BÊN PHẢI cô trợ lý kỹ thuật thỏ trắng đeo kính bảo hộ, cầm bảng kẹp tài liệu cầm thước chỉ vào hình vẽ nhện đực bơi lội.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bé con thắc mắc rất chí lý! Lý do là vì di chuyển trong môi trường nước đặc quánh đòi hỏi lực cản thủy động học cực lớn. Nhện đực không chịu ngồi yên một chỗ, gã phải liên tục bơi đường dài đi tuần tra và tìm kiếm bạn gái giữa các bụi rong.". Bố cục: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) đang bơi lội dũng mãnh giữa dòng nước xiết, vượt qua các xoáy nước nhỏ để mang bọt khí khổng lồ về tổ; cơ thể to lớn và sải chân dài giúp gã giữ thăng bằng hoàn hảo.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi tìm thấy chuông lặn của một nàng nhện ưng ý, chàng nhện đực không lao vào ẩu đả. Gã lịch sự xây ngay một chiếc chuông lặn phụ ngay sát vách căn hộ của nàng, rồi dệt một đường hầm tơ nối thông hai phòng khách lại với nhau!". Bố cục: Biệt thự thông tầng dưới đáy nước: Hai quả chuông lặn đặt cạnh nhau được nối với nhau bằng một đường ống hầm tơ trong suốt; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) và nàng nhện cái ngồi ở hai đầu đường hầm cụng ly nước bọt khí lãng mạn.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sau tuần trăng mật ngọt ngào, nàng nhện cái bắt đầu công việc thiêng liêng nhất của một người mẹ: Đẻ từ 50-100 trứng bọc trong một chiếc kén tơ trắng muốt, treo lơ lửng ở phần vòm cao nhất của quả chuông lặn!". Bố cục: Phòng trẻ sơ sinh dưới nước: Bên trong quả chuông lặn, một chiếc kén tơ hình cầu trắng muốt chứa đầy những quả trứng tròn nhỏ treo ở vòm trên; hàng chục chú nhện con tí hon mới nở bơi quanh với những bọt khí li ti.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy chứng kiến cỗ máy săn ngầm hoạt động trong điều kiện chiến trường thực tế! Thuyền Trưởng Tàu Ngầm Tơ không cần bơi lội rượt đuổi con mồi cho tốn calo.". Bố cục: Hệ thống bẫy mạng nhện dưới nước: Từ quả chuông lặn của chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon), hàng chục sợi tơ trong suốt tỏa ra các nhánh rong rêu như một mạng nhện radar vô hình bảo vệ căn cứ ngầm; KHÔNG có chú nhện thuyền trưởng trong cảnh này.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gã ngồi thảnh thơi bên trong quả chuông ấm áp, chỉ thò những đầu móng chân nhạy cảm ra ngoài chạm vào các sợi tơ kích hoạt. Khi một con ấu trùng chuồn chuồn, bọ gậy hay một chú cá nhỏ bơi ngang qua vô tình chạm vào sợi tơ cảm biến, xung động rung lắc truyền thẳng vào màng chuông với tốc độ ánh sáng!". Bố cục: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) ngồi thư thái trên chiếc ghế tựa bằng tơ bên trong chuông, hai chân trước thò ra mép cửa chạm nhẹ vào sợi tơ kích hoạt; ánh mắt tập trung theo dõi các chấn động rung lắc.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vút! Thuyền trưởng phóng vọt ra khỏi cửa hầm, tung hai chiếc kìm kẹp chứa nọc độc tiêm thẳng vào con mồi làm nạn nhân tê liệt trong tích tắc!". Bố cục: Hành động chớp nhoáng: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) phóng vụt ra khỏi chuông, hai chiếc kìm kẹp mở rộng kẹp trúng một ấu trùng chuồn chuồn bơi ngang; xung kích tỏa ra bọt nước lung linh.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu bất ngờ có một con cá chép đói khát bơi tới tấn công cắn rách vòm tơ, thuyền trưởng tí hon sẽ phản ứng thế nào? Gã không hề hoảng loạn!". Bố cục: Tình huống khẩn cấp: Một cái đầu cá chép to lớn hung dữ bơi tới cắn rách mép ngoài vòm tơ; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) nhanh như chớp luồn qua cửa đáy thoát hiểm núp vào khe đá; tay cầm kim dệt tơ sẵn sàng phản công.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thậm chí vào mùa đông băng giá, khi nhiệt độ nước tụt xuống 0°C và mặt hồ đóng băng dày cộp cắt đứt hoàn toàn nguồn không khí mặt thoáng, cỗ máy sinh học này vẫn vận hành ngoan cường!". Bố cục: Mùa đông giá rét: Mặt hồ bên trên đóng băng thành tảng đá trắng xóa lạnh lẽo; sâu dưới đáy bùn ấm áp, chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) cuộn tròn ngủ say sưa bên trong chiếc kén tơ dày bọc kín túi khí ở 0°C.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hồ sơ vũ khí số 41 chính thức khép lại với những thông số kinh ngạc! Nhện Lặn Chuông minh chứng hùng hồn cho bài học tiến hóa vĩ đại:". Bố cục: Bức tranh toàn cảnh tổng kết: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) đứng trên đỉnh quả chuông lặn pha lê tỏa sáng lung linh giữa đáy hồ, tay cầm bánh lái tàu ngầm bằng đồng thau, xung quanh là muôn loài sinh vật biển ngưỡng mộ.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu trong cuộc sống bạn cảm thấy ngột ngạt và lạc lõng giữa một môi trường xa lạ, hãy nhớ tới chú nhện lặn chuông:". Bố cục: Hình ảnh ẩn dụ truyền cảm hứng: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) nhỏ bé nhưng kiên cường đang dệt một quả chuông sáng lấp lánh bao bọc lấy một trái tim màu đỏ giữa biển đêm tăm tối, thắp sáng cả không gian xung quanh.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu được trang bị một bộ đồ lặn bong bóng như nhện lặn chuông, bạn muốn lặn xuống đáy hồ nào để khám phá thế giới vi mô kỳ ảo? Hãy để lại ý kiến thú vị của bạn ở phần bình luận bên dưới nhé!". Bố cục: Khán giả và chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon): Một bạn nhỏ hoạt hình đeo chiếc ba lô bong bóng khí bơi lội tung tăng bên cạnh chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon), hai người cùng cười tươi chỉ tay vào khung bình luận nhấp nháy bên dưới.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn bây giờ, hãy nhìn vào bóng đen bí ẩn của hồ sơ số 42! Một sinh vật biển kỳ dị chán ghét đại dương, bỏ nước lên cạn leo trèo trên cây ngập mặn,". Bố cục: Teaser bí ẩn bóng đen tập 42 (TASTE-68): Giữa bãi bùn rừng ngập mặn mù sương, một cái bóng đen bí ẩn (solid black silhouette) hình con cá có vây chân đang trèo lên rễ cây đước, hai con mắt lồi to tướng gắn dấu hỏi chấm '?', phía sau là đại dương xa xăm.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quên đi những tàu ngầm hạt nhân bọc thép titan ngàn tấn của con người, hãy nhìn xuống một bụi rong đuôi chó tĩnh lặng dưới đáy hồ nước ngọt!". Bố cục: Cận cảnh chi tiết bụi rong đuôi chó tĩnh lặng dưới đáy hồ: Những bọt khí nhỏ li ti bám trên kẽ lá xanh biếc; KHÔNG có chú nhện thuyền trưởng trong cảnh này; tia sáng mặt trời chiếu rọi từ mặt nước mờ ảo.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây là loài nhện duy nhất trong số hơn 50.000 loài nhện trên khắp hành tinh từ bỏ hoàn toàn cõi cạn để di cư xuống định cư vĩnh viễn dưới lòng nước!". Bố cục: Bản đồ phân bố tiến hóa sinh học: Hàng ngàn chấm đỏ đại diện cho 50.000 loài nhện cạn trên các lục địa; một vệt sáng xanh dương duy nhất lao xuống đáy hồ nước ngọt; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) đứng kiêu hãnh giơ cao kính lặn đồng thau.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu bạn thả một con nhện nhà bình thường xuống nước, nó sẽ ngạt thở chìm lịm trong vài phút. Nhưng Thuyền Trưởng Tàu Ngầm Tơ lại có thể bơi lặn, săn mồi, ngủ ngáy, thậm chí giao phối và ấp trứng 24/7 suốt cả cuộc đời dưới đáy hồ!". Bố cục: Cận cảnh mặt nước hồ: Một chú nhện nhà rơi xuống nước đang hoảng hốt bơi chới với; phía dưới đáy hồ sâu, chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) thong dong bơi lặn quanh những cột rong rêu như một thợ lặn chuyên nghiệp.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hôm nay, xưởng cơ khí sinh học của chúng ta sẽ tháo dỡ từng mắt tơ để xem gã kỹ sư tí hon này xây trạm không gian dưới nước như thế nào!". Bố cục: Cận cảnh bàn mổ xẻ thiết kế: cô trợ lý kỹ thuật thỏ trắng đeo kính bảo hộ, cầm bảng kẹp tài liệu cầm kính lúp và bút chì kỹ thuật chỉ vào mô hình chuông lặn tơ nhện vi mô; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) khoanh tay đứng cạnh mỉm cười đầy tự hào.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng Thuyền Trưởng Tàu Ngầm Tơ đã giải bài toán kết cấu này bằng một giải pháp tân tiến không thua gì các kỹ sư khoan ngầm dầu khí ngoài khơi!". Bố cục: Sơ đồ lực học thủy tĩnh: Mũi tên đỏ chỉ lực đẩy Ác-si-mét hướng lên trời; các mũi tên xanh lục neo đa hướng kéo ghì xuống đáy; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) cầm mỏ lết đồng thau siết chặt các khớp neo.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Điểm kỳ diệu nằm ở chỗ: Tơ của loài nhện này chứa protein kỵ nước siêu việt. Khi tiếp xúc với nước ngọt, các sợi tơ không hề bị mủn hay tan rã, mà đan kết lại thành một màng lưới dẻo dai tựa như màng cao su tổng hợp chịu áp lực cao!". Bố cục: Cận cảnh cấu trúc hiển vi của sợi tơ kỵ nước: Các phân tử protein đan xen khít khao phát sáng màu xanh ngọc bích; giọt nước chạm vào màng tơ bị trượt bắn ra ngoài như trượt trên lá sen; KHÔNG có chú nhện thuyền trưởng trong cảnh này.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nước bên ngoài không thể lọt vào một giọt, nhưng khí ga bên trong lại được giữ kín bưng. Bây giờ, chiếc chuông đã sẵn sàng, và màn vận chuyển khí thần sầu của thuyền trưởng tí hon chính thức bắt đầu!". Bố cục: Mặt cắt vi mô thành chuông: Bên ngoài là các phân tử nước màu xanh lam bị chặn đứng hoàn toàn bởi lớp nano kỵ nước; bên trong là các phân tử khí ga màu vàng óng được giữ kín bưng; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) bơi tuần tra bên trong.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gã dùng đầu húc thử vào thành chuông để kiểm tra độ đàn hồi, giống hệt như các chuyên viên kiểm định độ an toàn vỏ tàu ngầm trước khi hạ thủy! Một công trình xây dựng dưới đáy nước hoàn hảo không cần đến một chiếc đinh hay một giọt keo công nghiệp nào!". Bố cục: Cận cảnh kiểm tra độ bền: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) dùng đầu và hai chân trước húc mạnh vào màng tơ chuông lặn; màng tơ đàn hồi co giãn nhịp nhàng như cao su tổng hợp không hề rách; đồng hồ đo áp lực vọt lên mức an toàn.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gã chỉ nhô đúng phần chóp bụng và cặp chân sau lên khỏi mặt thoáng, thực hiện một cú giật mình chớp nhoáng rồi lặn ngược xuống đáy!". Bố cục: Góc nhìn cận cảnh mặt thoáng: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) chỉ nhô đúng phần chóp bụng và cặp chân sau lên khỏi mặt hồ, thực hiện một cú giật mình chớp nhoáng tạo ra những vòng sóng tròn lan tỏa; KHÔNG có chú nhện thuyền trưởng trong cảnh này.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây chính là nguồn gốc tên gọi Argyroneta trong tiếng Hy Lạp cổ, nghĩa là kẻ dệt sợi bạc!". Bố cục: Từ điển bách khoa cổ điển: Cuốn sách cổ Hy Lạp mở trang ghi chữ Argyroneta phát sáng vàng kim; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) soi mình trước quả cầu bạc bọc quanh bụng như một tấm gương cầu lồi lấp lánh.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gã lặp lại chuyến xe buýt con thoi này từ 20 đến 30 chuyến liên tục, cho đến khi quả chuông căng tròn bóng loáng bằng hạt đậu phộng, tỏa sáng lung linh giữa đáy bùn!". Bố cục: Hành trình xe buýt con thoi: Dãy 5 hình bóng chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) liên tiếp bơi lên bơi xuống giữa mặt hồ và đáy bùn; quả chuông tơ từ từ phồng to từ một hạt vừng lên thành một hạt đậu phộng căng tròn tỏa sáng lung linh.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ động cơ thẩm thấu thụ động này, một lượng khí ban đầu có thể cung cấp dưỡng khí cho nhện sống suốt 24 giờ liên tục mà không cần bơi lên mặt hồ lấy thêm khí!". Bố cục: Đồng hồ sinh tồn 24 giờ: Mặt đồng hồ cơ khí bằng đồng hiển thị 24h; bên trong quả chuông lặn, chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) ung dung ngủ ngon lành trên võng tơ; các luồng oxy xanh biếc liên tục tự thẩm thấu vào vòm chuông.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chính vì vậy, Thuyền Trưởng Tàu Ngầm Tơ phải thực hiện một chuyến tuần tra bảo dưỡng định kỳ mỗi ngày 1 lần, ngoi lên mặt nước mang về vài bọt khí tươi mới để nạp lại áp suất cho căn cứ!". Bố cục: Chuyến tuần tra bảo dưỡng: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) đeo túi đồ nghề sửa chữa, ngoi lên mặt nước quặp một bọt khí mới toanh mang xuống nạp vào đỉnh chuông lặn; đồng hồ áp suất kim chỉ lại về vạch xanh an toàn.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nơi các nàng nhện cái khổng lồ thường xơi tái chú nhện đực gầy gò ngay sau đêm tân hôn, thì dưới đáy hồ nước ngọt, tạo hóa đã lật ngược ván cờ 100 80 độ!". Bố cục: Tương phản sinh học: BÊN TRÁI trên cạn, một nàng nhện cái khổng lồ đang hung dữ cầm nĩa; BÊN PHẢI dưới nước, chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) vạm vỡ cơ bắp đang mỉm cười nháy mắt chào đón bạn gái; KHÔNG có chú nhện thuyền trưởng trong cảnh này.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhện đực to hơn nhện cái đến 30% và sở hữu sải chân dài cơ bắp vượt trội! Đây là một hiện tượng dị hình giới tính đảo ngược cực kỳ hiếm hoi trong toàn bộ thế giới tám chân!". Bố cục: Bàn cân so sánh kích thước: BÊN TRÁI chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) (nhện đực) dài 15mm sải chân vạm vỡ; BÊN PHẢI nàng nhện cái nhỏ nhắn 12mm e ấp; chiếc thước kẹp cơ khí đo tỷ lệ chênh lệch 30% rõ nét.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thân hình to lớn và đôi chân dài giúp gã bơi nhanh hơn, quặp được bọt khí to hơn và không bị dòng nước cuốn trôi!". Bố cục: Cảnh bơi lội vượt dòng xiết: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) sải 8 chiếc chân dài cơ bắp quặp quả bọt khí khổng lồ rẽ nước bơi băng băng qua dòng chảy xiết; chú cá con ngơ ngác mắt tròn xoe, mang vây nhỏ nhắn bơi lội bơi bên cạnh nhìn theo trầm trồ thán phục.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một căn biệt thự thông tầng dưới đáy nước được hình thành lãng mạn vô cùng, nơi con đực bảo vệ đàn con mà không hề lo sợ bị người tình ăn thịt!". Bố cục: Bản vẽ phối cảnh kiến trúc: Hai quả chuông lặn nối liền nhau bằng đường hầm tơ trong suốt; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) và nàng nhện cái ngồi hai bên đường hầm cụng ly nước ngọt lãng mạn dưới ánh đèn lân tinh.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nơi đây chứa lượng oxy tinh khiết nhất để nuôi dưỡng các nhện con. Khi các chú nhện con chào đời, chúng bơi lội ngay trong phòng khách dưới nước của bố mẹ, học cách quặp bọt khí đầu tiên trước khi tự lập xây dựng vương quốc riêng!". Bố cục: Phòng trẻ sơ sinh dưới nước: Bên trong vòm chuông trên cao, chiếc kén tơ tròn xoe chứa hàng chục nhện con tí hon đang chui ra; các bé nhện con đeo kính bơi tí hon tập quặp những bọt khí nhỏ li ti.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Từ quả chuông lặn trung tâm, gã giăng ra hàng chục sợi tơ bẫy vô hình kết nối trực tiếp với các cành rong rêu xung quanh như những đường dây điện thoại bảo vệ căn cứ!". Bố cục: Mạng lưới radar dây tơ: Từ quả chuông lặn của chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon), hàng chục sợi tơ mảnh phát sáng chạy dài đến các bụi cây thủy sinh như mạng dây điện thoại cảnh báo; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) đặt chân lên nút cảm biến trung tâm.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sau đó, gã kéo chiến lợi phẩm ngược vào bên trong quả chuông lặn khô ráo để thưởng thức bữa tiệc thịnh soạn mà không sợ bị các loài cá săn mồi khác cướp mất miếng ăn!". Bố cục: Phòng tiệc bên trong chuông lặn: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) ngồi thảnh thơi trên chiếc ghế bành bằng tơ, dùng dao nĩa tí hon thưởng thức món ấu trùng bọ gậy khô ráo; ngoài thành chuông, một chú cá săn mồi bơi qua nhìn thèm thuồng.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Với tốc độ cơ động cực nhanh, gã lập tức thoát hiểm qua cửa đáy khẩn cấp, núp vào khe đá ngầm. Đợi kẻ thù bỏ đi, gã quay lại hiện trường và chỉ mất chưa đầy 30 phút để vá lành mọi vết rách bằng những đường tơ kỵ nước mới toanh, tiếp tục làm chủ pháo đài dưới nước!". Bố cục: Kế hoạch thoát hiểm khẩn cấp: Vòm tơ bị cá chép cắn rách, chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) phóng vọt qua cửa đáy thoát hiểm núp vào khe đá; sau khi cá bỏ đi, chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) thoăn thoắt phun tơ vá lành lỗ rách trong tích tắc.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhện lặn chuông bò xuống lớp bùn sâu nhất, dệt một chiếc kén tơ siêu dày bọc kín một túi khí nhỏ, hạ thấp thân nhiệt và nhịp tim để ngủ đông suốt nhiều tháng ròng rã cho đến khi mùa xuân tan băng!". Bố cục: Giấc ngủ đông dưới đáy băng: Mặt hồ phủ lớp băng dày tuyết trắng; sâu dưới lớp bùn ấm áp, chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) cuộn tròn ngủ say trong kén tơ siêu dày ôm một túi khí nhỏ; chiếc nhiệt kế cắm cạnh chỉ 0°C.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi môi trường sống cạn kiệt cơ hội, bạn không nhất thiết phải thay đổi toàn bộ bên trong cơ thể để thích nghi. Thuyền Trưởng Tàu Ngầm Tơ không mọc ra mang cá, gã chỉ đơn giản dệt nên một công nghệ đem theo bầu trời của chính mình xuống đáy đại dương!". Bố cục: Biểu tượng triết lý tiến hóa: Hình vẽ cây tiến hóa với các nhánh cạn kiệt cơ hội; chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) đứng trên đỉnh một mỏm đá ngầm, tay cầm cờ hải quân tung bay, mở ra một chân trời mới dưới đáy hồ sâu.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đôi khi, chỉ cần một quả chuông kiên định dệt bằng sự sáng tạo và nỗ lực, bạn hoàn toàn có thể tự tạo ra bầu không khí thành công cho riêng mình ngay giữa nghịch cảnh!". Bố cục: Hình ảnh truyền cảm hứng: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon) tươi cười rạng rỡ bên trong quả chuông lặn tỏa sáng lung linh giữa đáy hồ tối; xung quanh là dòng nước lạnh giá nhưng bên trong ấm áp tràn đầy dưỡng khí hy vọng.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nếu ngâm nước quá lâu thì lại bị chết đuối, và mỗi khi nuốt mồi lại phải tụt cả hai nhãn cầu mắt xuống tận cổ họng! Bạn có đoán được quái kiệt hai mang này là ai không?". Bố cục: Cận cảnh hình bóng teaser tập 42 (TASTE-68): Bóng đen một con cá kỳ dị hai mắt lồi to tướng ngồi trên cành cây đước bãi lầy, một tay bịt mũi ôm cổ ho sặc sụa dưới nước với dấu hỏi '?' lớn màu vàng.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bạn có tin trên đời có một loài nhện thở bằng phổi nhưng cả cuộc đời lại sống dưới đáy nước?". Bố cục: Cận cảnh mở đầu: chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc đeo kính lặn đồng thau và mũ thuyền trưởng, hai tay ôm một quả cầu bọt khí bạc phát sáng, mắt to tròn long lanh nhìn thẳng vào người xem.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đây là Nhện Lặn Chuông, dài chỉ 10-15mm nhưng sở hữu công nghệ tàu ngầm vô tiền khoáng hậu!". Bố cục: chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc đứng trên thước đo milimét dưới đáy nước, cơ thể tí hon nhưng phong thái đĩnh đạc như một thuyền trưởng tàu ngầm thực thụ.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Gã ngoi lên mặt nước, dùng bộ lông kỵ nước quặp chặt một bọt khí bạc quanh bụng rồi lặn xuống đáy hồ.". Bố cục: chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc thò chóp bụng lên mặt hồ, lớp lông kỵ nước bẫy chặt bọt khí biến phần thân thành quả bóng bạc lấp lánh như gương tráng bạc.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Tại đây, gã dệt một chiếc vòm tơ hình chuông úp ngược vào rong rêu, bơm đầy bọt khí vào trong để làm trạm không gian dưới nước!". Bố cục: Dưới đáy hồ: chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc đang dệt chiếc vòm tơ hình chuông úp ngược neo vào cọng rong rêu xanh biếc, chuẩn bị bơm khí vào trong.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Điều chấn động là màng tơ này hoạt động như một chiếc mang nhân tạo,". Bố cục: Sơ đồ nguyên lý: Quả chuông tơ phát sáng; oxy từ nước thẩm thấu vào trong chuông, khí CO2 khuếch tán ra ngoài; chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc ung dung thở đều.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Từ ăn ngủ, săn mồi đến đẻ trứng, gã làm trọn vẹn trong bong bóng không khí kỳ diệu,". Bố cục: Ghép 3 khung cảnh mini: chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc ngủ trên võng tơ, chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc ăn tiệc bọ gậy, và chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc chăm sóc kén trứng; tất cả diễn ra trong chuông lặn.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "chứng minh giới hạn sinh tồn chỉ là chuyện nhỏ trước kỹ nghệ đỉnh cao của thiên nhiên!". Bố cục: Hình ảnh kết thúc: chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc đứng oai vệ bên cạnh quả chuông lặn phát sáng rực rỡ, giơ ngón tay cái cười tươi đầy tự hào.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "tự hút oxy hòa tan từ nước xung quanh để gã thở suốt 24 giờ mà không cần ngoi lên mặt hồ!". Bố cục: Cận cảnh thành quả chuông: Các phân tử oxy xanh dương thẩm thấu vào trong chuông, giúp chú nhện lặn chuông hoạt hình đeo kính lặn đồng thau, mũ thuyền trưởng tí hon, bụng bọc bọt khí bạc thở suốt 24 giờ mà không cần ngoi lên mặt hồ; đồng hồ cơ khí quay tròn 24h.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/57 của video YouTube về Nhện Lặn Chuông). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon). Nhân vật phụ cố định: cô trợ lý kỹ thuật thỏ trắng đeo kính bảo hộ, cầm bảng kẹp tài liệu; chú cá con ngơ ngác mắt tròn xoe, mang vây nhỏ nhắn bơi lội. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/8 của video YouTube Shorts về Nhện Lặn Chuông). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú nhện lặn chuông hoạt hình ngộ nghĩnh (màu nâu sẫm, mắt to tròn long lanh đeo kính lặn bảo hộ viền đồng thau cổ điển, đội mũ thuyền trưởng hải quân tí hon, phần bụng dưới phủ một lớp bọc bóng bạc lấp lánh như gương, 8 chân mảnh khảnh mang găng tay và giày bốt cao su tí hon). Nhân vật phụ: chú cá con ngơ ngác mắt tròn xoe, mang vây nhỏ nhắn bơi lội. 
```
</details>

## 7. SEO

- **title:** Tàu Ngầm Tơ Nhện: Bí Mật Sống 24 Giờ Dưới Đáy Hồ Của Kỹ Sư Tí Hon | Tập 41
- **hook_paragraph:** Loài nhện duy nhất trên thế giới từ bỏ mặt đất để định cư vĩnh viễn dưới đáy hồ nước ngọt: Nhện Lặn Chuông (Argyroneta aquatica). Dù thở bằng phổi nhưng gã tự chế tạo quả chuông lặn bằng tơ kỵ nước hoạt động như mang nhân tạo, tự hút oxy từ nước để sống 24 giờ liên tục!
- **question:** Nếu được trang bị một quả chuông lặn tự hút oxy như Nhện Lặn Chuông, bạn sẽ mang nó lặn xuống đâu đầu tiên? Bình luận bên dưới nhé!
- **next_teaser:** Tập 42: Quái kiệt chán biển lên cạn leo cây, ngâm nước quá lâu thì chết đuối và thụt mắt xuống họng để nuốt mồi!
- **shorts_title:** Tàu Ngầm Tơ Nhện Độc Nhất Vô Nhị Dưới Đáy Hồ! 🫧🕷️ #độngvật #nhệnlặnchuông
- **shorts_desc:** Loài nhện duy nhất thở bằng phổi nhưng sống cả đời dưới nước nhờ quả chuông tơ tự hút oxy như mang nhân tạo!

#độngvật #nhệnlặnchuông #VẽChuyệnHoangDã
- **bullets:** Hồ sơ kỹ thuật: Loài nhện duy nhất trong 50.000 loài sống cả đời dưới nước · Bản vẽ thiết kế: Tơ nhện kỵ nước dệt thành chuông lặn không thấm nước · Động cơ sinh học: Lông bụng quặp bọt khí bạc và mang nhân tạo tự thẩm thấu oxy · Nghịch lý giới tính: Nhện đực to hơn nhện cái 30% để bơi và giữ chuông · Thực chiến săn mồi: Hệ thống dây tơ cảm biến và giấc ngủ đông ở 0 độ C
- **tags:** nhện lặn chuông, diving bell spider, argyroneta aquatica, tàu ngầm tơ nhện, thế giới động vật, vẽ chuyện hoang dã, khoa học kỳ thú, whiteboard animation, động vật kỳ lạ
- **hashtags:** #độngvật #nhệnlặnchuông #VẽChuyệnHoangDã

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-41-nhen-lan-chuong
python src/episode/pipeline.py tts    projects/tap-41-nhen-lan-chuong     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-41-nhen-lan-chuong     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-41-nhen-lan-chuong     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-41-nhen-lan-chuong              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-41-nhen-lan-chuong --force
python scripts/beat_sheet.py projects/tap-41-nhen-lan-chuong               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-41-nhen-lan-chuong/audio/shorts.wav projects/tap-41-nhen-lan-chuong/renders/tap-41-nhen-lan-chuong_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-41-nhen-lan-chuong
python src/episode/pipeline.py seo    projects/tap-41-nhen-lan-chuong
python src/episode/episode_doc.py     projects/tap-41-nhen-lan-chuong
```

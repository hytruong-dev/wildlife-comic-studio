# TẬP 17 — LƯƠN ĐIỆN · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-17-luon-dien`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-17-luon-dien`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F5` · **Persona giọng:** `nha_khoa_hoc` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Lươn Điện |
| Tiêu đề YouTube | Tại Sao Lươn Điện 860V Giật Ngất Cá Sấu Mà Không Bị Giật Chết?! \| Lươn Điện \| Tập 17 |
| Video dài | `renders/tap-17-luon-dien_long.mp4` — 9:16.4 (556.4s) |
| Shorts | `renders/tap-17-luon-dien_shorts.mp4` — 0:50.8 (50.8s) |
| Thumbnail | `renders/tap-17-luon-dien_thumbnail.jpg` |
| Số hình | dài 61 beat / 61 ảnh riêng; Shorts 12 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/61 của video YouTube về Lươn Điện). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — MẪU VẬT PIN SỐNG 860 VÔN
*Thẻ chương:* BẬT CÔNG TẮC THỬ NGHIỆM 5 CẤP ĐỘ

*Badge:* `KHỞI ĐỘNG THỬ THÁCH` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene01_p0.wav` (343 ký tự) · mood `tram_bi_an`

```text
Chào mừng tất cả các trợ lý nghiên cứu đã bước vào Phòng Thí Nghiệm Sinh Học Tối Mật! Rè rè... Xoẹt! Tiếng hồ quang điện nổ lép bép trong bóng tối, và đồng hồ đo vôn kế đang nhảy số loạn xạ. Đằng sau tấm kính cường lực chống điện dày mười phân kia, một mẫu vật thủy quái kỳ dị bậc nhất hành tinh vừa được áp giải từ lưu vực sông Amazon về đây!
```
**Part 1** → `audio/vs/scene01_p1.wav` (119 ký tự) · 🎭 cameo `co_tro_ly`

```text
Báo cáo giáo sư! Nguồn điện trong bể chứa đang tăng vọt bất thường, tất cả bóng đèn cảnh báo đều đang chớp đỏ liên tục!
```
**Part 2** → `audio/vs/scene01_p2.wav` (445 ký tự) · mood `hao_hung`

```text
Bình tĩnh nào cô trợ lý! Hãy đeo kính cách điện vào và ghi chép nhật ký thật cẩn thận! Mẫu vật số mười bảy hôm nay là một sinh vật mà cả thế giới quen miệng gọi là Lươn Điện. Nhưng tôi xin tiết lộ ngay một sự thật gây sốc đầu tiên: về mặt phả hệ sinh học, nó hoàn toàn không phải là lươn! [surprise-oh] Nó không có bất kỳ họ hàng nào với loài lươn đồng hay lươn biển, mà thuộc bộ cá dao Nam Mỹ, tức là có họ gần gũi với cá trê và cá da trơn hơn!
```
**Part 3** → `audio/vs/scene01_p3.wav` (444 ký tự) · mood `don_dap`

```text
Nhưng tại sao chúng ta lại gọi nó bằng biệt danh Nhà Máy Điện Sống? Bởi vì toàn bộ cấu trúc cơ thể của con cá này sinh ra chỉ để phục vụ một mục đích duy nhất: biến thịt da thành vũ khí sốc điện hủy diệt! Hơn tám mươi phần trăm chiều dài cơ thể của nó là những khối pin sinh học nối tiếp nhau, có khả năng kích hoạt nguồn điện lên tới tám trăm sáu mươi Vôn — tức là mạnh gấp bốn lần ổ cắm điện hai trăm hai mươi Vôn trong nhà bạn! [surprise-wa]
```
**Part 4** → `audio/vs/scene01_p4.wav` (345 ký tự) · mood `hao_hung`

```text
Hôm nay, tôi sẽ kích hoạt quy trình thí nghiệm năm cấp độ tăng dần: từ máy phát radar định vị mười Vôn, vũ khí hack hệ thần kinh con mồi từ xa, cú nhảy dí cằm điện giật ngất ngây cá sấu hai mét, cho đến bí mật vì sao nó không bị điện giật chết chính mình! Hãy siết chặt dây an toàn, chúng ta bắt đầu kích hoạt Cấp độ một ngay bây giờ! [laughter]
```

### scene02 — 6.000 TẾ BÀO PIN VÀ RADAR ĐỊNH VỊ BÙN LẦY
*Thẻ chương:* MÁY ĐO ĐIỆN VÀ RADAR DÒ TÌM CON MỒI

*Badge:* `CẤP ĐỘ 1` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene02_p0.wav` (406 ký tự) · mood `hao_hung`

```text
Khởi động Cấp độ một: Phân tích cơ chế nạp điện và hệ thống radar định vị trong bùn lầy! [laughter] Hãy nhìn kỹ vào thân hình dài tới hai mét và nặng hai mươi ki-lô-gam của mẫu vật. Tất cả các cơ quan nội tạng quan trọng nhất như tim, gan, dạ dày và mang thở đều bị dồn ép lại vỏn vẹn trong hai mươi phần trăm phần đầu phía trước! Toàn bộ phần thân dài ngoằng còn lại chính là ba cơ quan phát điện độc lập!
```
**Part 1** → `audio/vs/scene02_p1.wav` (485 ký tự) · mood `don_dap`

```text
Cơ quan phát điện chính, cơ quan Hun-tơ và cơ quan Sách! Bên trong ba khối cơ này chứa khoảng năm ngàn đến sáu ngàn tế bào phát điện hình chiếc đĩa dẹp xếp chồng khít lên nhau thành hàng trăm cột dài song song. Mỗi tế bào này giống như một cục pin cúc áo mini, tạo ra một điện thế cực nhỏ chỉ không phẩy mười lăm Vôn. Nhưng khi hàng ngàn tế bào này được thần kinh kích hoạt đồng loạt nối tiếp nhau, các điện thế cộng dồn lại tạo thành một cú sốc điện kinh thiên động địa! [surprise-oh]
```
**Part 2** → `audio/vs/scene02_p2.wav` (438 ký tự) · mood `am_ap`

```text
Nhưng ở chế độ bình thường, Nhà Máy Điện Sống không dại gì xả hết điện năng! Nó sử dụng cơ quan Sách ở đuôi để liên tục phát ra những xung điện áp thấp chỉ khoảng mười Vôn với tần số hai mươi nhịp mỗi giây. Vùng nước sông Amazon đục ngầu phù sa khiến mắt của lươn điện gần như bị mù lòa. Nhưng nhờ trường điện mười Vôn bao bọc xung quanh cơ thể, nó có thể cảm nhận mọi vật cản và con mồi bơi qua hệt như một chiếc tàu ngầm bật sóng sonar!
```
**Part 3** → `audio/vs/scene02_p3.wav` (136 ký tự) · 🎭 cameo `co_tro_ly`

```text
Giáo sư ơi! Màn hình radar vừa phát hiện một đàn cá nhỏ đang vùi mình dưới lớp bùn sâu ba mươi xăng-ti-mét! Nó làm sao bắt được chúng ạ?
```
**Part 4** → `audio/vs/scene02_p4.wav` (136 ký tự) · mood `hao_hung`

```text
Câu hỏi rất hay! Đã đến lúc chuyển giao diện thí nghiệm sang Cấp độ hai: Kỹ thuật hack não và thao túng cơ bắp con mồi từ xa! [laughter]
```

### scene03 — XUNG ĐIỆN KÉP THAO TÚNG CƠ BẮP CON MỒI TỪ XA
*Thẻ chương:* HACK HỆ THẦN KINH VÀ ÉP CƠ BẮP CO GIẬT

*Badge:* `CẤP ĐỘ 2` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene03_p0.wav` (296 ký tự) · mood `don_dap`

```text
Bước vào Cấp độ hai: Thử nghiệm vũ khí điều khiển thần kinh từ xa! Năm hai ngàn mười bốn, nhà sinh vật học lừng danh Ken-nét Ca-ta-ni-a tại Đại học Văn-đơ-bin đã công bố một nghiên cứu chấn động trên tạp chí Science danh giá, vạch trần bí mật săn mồi đỉnh cao của Nhà Máy Điện Sống! [surprise-oh]
```
**Part 1** → `audio/vs/scene03_p1.wav` (421 ký tự) · mood `don_dap`

```text
Khi nghi ngờ có con mồi đang ẩn nấp dưới đáy bùn, Lươn Điện sẽ phóng ra một cặp xung điện kép cực mạnh gồm hai cú sốc cách nhau đúng hai đến ba phần nghìn giây! Cặp xung điện này không phải để giết chết con mồi, mà nó bắt chước hoàn hảo tín hiệu điều khiển vận động của não bộ! Tín hiệu này xâm nhập thẳng vào hệ thần kinh của con cá đang nấp, ép toàn bộ các bó cơ trên cơ thể con mồi phải co giật kịch liệt ngoài ý muốn!
```
**Part 2** → `audio/vs/scene03_p2.wav` (146 ký tự) · 🎭 cameo `be_con`

```text
Ối giời ơi! Tự nhiên đuôi tôi nó giật bắn lên thế này! Tôi đâu có muốn bơi đâu mà cơ thể cứ giãy nảy lên văng cả bùn ra ngoài thế này cứu tôi với!
```
**Part 3** → `audio/vs/scene03_p3.wav` (354 ký tự) · mood `hao_hung`

```text
Chính xác là như vậy! Con cá nhỏ vừa giật bắn mình làm rung chuyển lớp bùn là vị trí ẩn nấp lập tức bị bại lộ hoàn toàn trước cảm biến của thợ săn! Và ngay trong một phần mười giây tiếp theo, Nhà Máy Điện Sống lập tức tung ra đòn kết liễu tàn nhẫn: nó xả liên tiếp hàng trăm xung điện cao thế bốn trăm Vôn với tần số bốn trăm nhịp mỗi giây! [surprise-wa]
```
**Part 4** → `audio/vs/scene03_p4.wav` (432 ký tự) · mood `am_ap`

```text
Toàn bộ cơ bắp của con mồi lập tức rơi vào trạng thái co cứng cực đại, bị đông cứng như một khúc gỗ hoàn toàn tê liệt không thể cử động hay hít thở! Và trước khi con mồi kịp hiểu chuyện gì vừa xảy ra, Lươn Điện há chiếc miệng rộng ngoác tạo ra một lực hút chân không cực mạnh nuốt chửng nạn nhân vào bụng chỉ trong chớp mắt! Một cơ chế săn mồi điều khiển từ xa tinh vi đến mức các kỹ sư quân sự cũng phải ngả mũ bái phục! [laughter]
```

### scene04 — CÚ NHẢY DÍ CẰM ĐIỆN GIẬT NGẤT CÁ SẤU 2 MÉT
*Thẻ chương:* CÚ PHÓNG LÊN KHỎI NƯỚC DÍ THẲNG VÀO TIM

*Badge:* `CẤP ĐỘ 3` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene04_p0.wav` (396 ký tự) · mood `don_dap`

```text
Cảnh báo mức độ nguy hiểm cực hạn! Chúng ta bước vào Cấp độ ba: Đối đầu với những kẻ săn mồi khổng lồ trên cạn và cú nhảy dí cằm huyền thoại! [surprise-oh] Hơn hai trăm năm trước, nhà thám hiểm vĩ đại A-lếch-xăng-đơ von Hum-bôn từng kể lại câu chuyện lươn điện phóng điện tấn công cả đàn ngựa băng qua sông, nhưng suốt hai thế kỷ giới khoa học đều nghĩ rằng ông chỉ phóng đại câu chuyện dân gian!
```
**Part 1** → `audio/vs/scene04_p1.wav` (458 ký tự) · mood `tram_bi_an`

```text
Cho đến tận năm hai ngàn mười sáu, giáo sư Ca-ta-ni-a mới chính thức giải mã được hành vi kinh hoàng này trong phòng thí nghiệm! Trong môi trường nước sâu, dòng điện phóng ra từ cơ thể lươn sẽ bị phân tán ra mọi hướng trong nước, khiến điện áp truyền vào cơ thể kẻ địch bị suy giảm đáng kể. Nhưng khi bị một kẻ săn mồi to xác như cá sấu Cai-man, báo đốm hay con người dồn vào vùng nước nông, Nhà Máy Điện Sống sẽ tung ra tuyệt chiêu cận chiến nguy hiểm nhất!
```
**Part 2** → `audio/vs/scene04_p2.wav` (440 ký tự) · mood `don_dap`

```text
Nó không nằm dưới nước phóng điện, mà dùng chiếc đuôi khỏe khoắn gập mạnh, ngóc đầu phóng vọt lên khỏi mặt nước cao tới nửa mét! Nó áp sát phần cằm dẫn điện cực dương trực tiếp vào ngực hoặc cổ họng của kẻ tấn công, trong khi phần đuôi cực âm vẫn cắm chặt dưới nước! Toàn bộ nguồn điện khủng khiếp chạy thẳng một mạch xuyên qua tim và não của kẻ săn mồi mà không hề bị tiêu hao một mi-li-vôn nào ra môi trường nước xung quanh! [surprise-wa]
```
**Part 3** → `audio/vs/scene04_p3.wav` (167 ký tự) · 🎭 cameo `ga_khong_lo`

```text
Này con lươn trơn tuột kia, nhìn tao là cá sấu chúa dài hai mét đây này, liệu hồn mà nạp mạng... Á á á! Cứu tao với! Điện giật xoắn cả đuôi, tim ngừng đập rồi trời ơi!
```
**Part 4** → `audio/vs/scene04_p4.wav` (465 ký tự) · mood `hao_hung`

```text
Cú nhảy dí cằm trực tiếp này tạo ra một dòng điện cực mạnh đủ sức làm tê liệt hoàn toàn hệ cơ tim của một con cá sấu dài hai mét hoặc một con ngựa trưởng thành, khiến chúng ngã gục ngay tại chỗ vì sốc tim và ngạt thở! Chưa hết, khi gặp con mồi quá to, nó còn uốn cong cơ thể thành hình chữ U, kẹp chặt con mồi vào giữa đầu và đuôi để nhân đôi cường độ điện trường xuyên qua cơ thể nạn nhân! Một chiến thuật chiến đấu công thủ toàn diện đến mức rùng mình! [laughter]
```

### scene05 — TẠI SAO LƯƠN ĐIỆN KHÔNG BỊ ĐIỆN GIẬT CHẾT?
*Thẻ chương:* LỚP CÁCH ĐIỆN SINH HỌC VÀ NGHỊCH LÝ CHẾT ĐUỐI

*Badge:* `CẤP ĐỘ 4` · *mood mặc định:* `nghiem_trang_gia`

**Part 0** → `audio/vs/scene05_p0.wav` (302 ký tự) · mood `hao_hung`

```text
Đến đây, chắc chắn câu hỏi lớn nhất đang sôi sục trong đầu các trợ lý là: Phóng ra nguồn điện khủng khiếp như vậy, tại sao chính con Lươn Điện lại không bị giật chết lăn quay ra đấy? Câu trả lời nằm ở ba tấm lá chắn vật lý và sinh học thiên tài mà tiến hóa đã trang bị cho Nhà Máy Điện Sống! [laughter]
```
**Part 1** → `audio/vs/scene05_p1.wav` (468 ký tự) · mood `nghiem_trang_gia`

```text
Lá chắn thứ nhất là quy luật điện trở vật lý! Cơ thể của lươn điện được bọc kín bởi một lớp da dày và các lớp mỡ dày có điện trở rất cao. Trong khi đó, dòng điện luôn có xu hướng chọn con đường có điện trở thấp nhất để di chuyển. Môi trường nước sông Amazon xung quanh cơ thể nó có điện trở thấp hơn rất nhiều so với lớp mỡ bảo vệ, nên phần lớn năng lượng điện phóng ra sẽ lập tức thoát thẳng ra nước xung quanh thay vì thâm nhập ngược vào sâu trong nội tạng của lươn!
```
**Part 2** → `audio/vs/scene05_p2.wav` (361 ký tự) · mood `am_ap`

```text
Lá chắn thứ hai là bố cục vị trí cơ quan sinh học! Như tôi đã nhấn mạnh ở đầu buổi thí nghiệm, toàn bộ não bộ, tim và các cơ quan nội tạng nhạy cảm đều được cô lập hoàn toàn ở phần đầu, cách xa khu vực ba cơ quan phát điện ở thân sau và được bao bọc bởi các lớp mô liên kết cách điện kiên cố! Dòng điện đi từ đầu tới đuôi nhưng chỉ lướt qua bề mặt ngoài cơ thể!
```
**Part 3** → `audio/vs/scene05_p3.wav` (357 ký tự) · mood `don_dap`

```text
Và lá chắn thứ ba là yếu tố kích thước! Lươn Điện trưởng thành dài tới hơn hai mét, nên mật độ dòng điện đi qua từng thớ cơ của nó bị pha loãng ra nhiều lần, trong khi những con cá nhỏ hay con mồi bị nó dí sát thì phải hứng trọn mật độ điện trường dày đặc chí mạng! Nhưng Nhà Máy Điện Sống bất khả chiến bại này lại có một điểm yếu chết người cực kỳ bi hài!
```
**Part 4** → `audio/vs/scene05_p4.wav` (408 ký tự) · mood `hao_hung`

```text
Tám mươi phần trăm lượng oxy của lươn điện được hấp thụ qua các mao mạch trong miệng chứ mang của nó gần như bị thoái hóa hoàn toàn! Cứ mười đến mười lăm phút một lần, nó bắt buộc phải ngoi đầu lên mặt nước để hít thở không khí. Nếu bạn giữ chặt con lươn này dưới nước không cho nó ngoi lên, một sát thủ điện giật ngất cá sấu sẽ... chết đuối y như con người! Một nghịch lý sinh học quá đỗi thú vị! [laughter]
```

### scene06 — SỨC MẠNH 860V VÀ BÓNG ĐEN BÍ ẨN TẬP 18
*Thẻ chương:* ĐỈNH CAO 860 VÔN VÀ BẬT MÍ QUÁI KIỆT TẬP 18

*Badge:* `CẤP ĐỘ TỐI THƯỢNG` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene06_p0.wav` (399 ký tự) · mood `hao_hung`

```text
Chào mừng quý vị bước vào Cấp độ tối thượng: Kỷ lục năng lượng mới nhất của thế giới hiện đại! Suốt hai trăm năm ròng rã, cả thế giới đinh ninh rằng hành tinh này chỉ có duy nhất một loài lươn điện với điện áp tối đa sáu trăm Vôn. Nhưng vào năm hai ngàn mười chín, nhóm nghiên cứu của tiến sĩ Đê Xan-ta-na tại Viện Xmít-xô-ni-an đã phát hiện ra loài lươn điện mới mang tên Ê-léc-trô-pho-rút Vôn-tai!
```
**Part 1** → `audio/vs/scene06_p1.wav` (419 ký tự) · mood `am_ap`

```text
Khi gắn thiết bị đo vào mẫu vật Vôn-tai này, chiếc kim đồng hồ đã vọt lên con số kỷ lục tám trăm sáu mươi Vôn! Đây chính là sinh vật phóng điện mạnh nhất từng được ghi nhận trong lịch sử Trái Đất, biến những dòng sông hoang dã Nam Mỹ trở thành những trạm biến áp tự nhiên kỳ vĩ bậc nhất hành tinh! Tiến hóa không chỉ tạo ra sự sống, mà còn tạo ra những kỳ quan công nghệ sinh học đi trước con người hàng trăm triệu năm!
```
**Part 2** → `audio/vs/scene06_p2.wav` (235 ký tự) · 🎭 cameo `co_tro_ly`

```text
Báo cáo giáo sư! Toàn bộ dữ liệu thử nghiệm của mẫu vật Lươn Điện đã được lưu trữ thành công vào hệ thống! Nhưng trên radar quét tầm xa, phòng thí nghiệm vừa bắt được tín hiệu của một quái kiệt tí hon cực kỳ nguy hiểm cho Tập mười tám!
```
**Part 3** → `audio/vs/scene06_p3.wav` (194 ký tự) · mood `hao_hung`

```text
Tuyệt vời lắm cô trợ lý! Xin mời toàn thể các nhà nghiên cứu hãy hướng mắt lên màn hình lớn trung tâm để giải mã BÓNG ĐEN BÍ ẨN của nhân vật xuất hiện trong Tập mười tám tiếp theo! [surprise-oh]
```
**Part 4** → `audio/vs/scene06_p4.wav` (568 ký tự) · mood `don_dap`

```text
Xin gửi tới các bạn ba manh mối khoa học chấn động về bóng đen bí ẩn này: Thứ nhất, đây là siêu pháo thủ tí hon sở hữu khẩu súng hóa học liên thanh nã đạn năm trăm lần mỗi giây ở nhiệt độ sôi sùng sục một trăm độ C làm bỏng rát mọi kẻ thù! Thứ hai, phản ứng hóa học hai buồng đốt chết người: buồng chứa nhiên liệu và buồng kích nổ áp suất cực cao! Và thứ ba, kỷ lục thoát chết kinh dị bậc nhất: bị cóc nuốt chửng vào bụng suốt một tiếng đồng hồ, nó nã pháo xả độc ngay trong bao tử khiến cóc buồn nôn nôn thốc nôn tháo nguyên con ra ngoài vẫn sống nhăn nhở! [laughter]
```
**Part 5** → `audio/vs/scene06_p5.wav` (266 ký tự) · mood `hao_hung`

```text
Các trợ lý khoa học có đoán ra bóng đen pháo thủ tí hon này là sinh vật nào không? Hãy để lại kết quả phân tích và dự đoán của bạn ngay dưới phần bình luận nhé! Giáo sư phòng thí nghiệm xin chào tạm biệt và hẹn gặp lại các bạn trong cuộc thử nghiệm kỳ thú tiếp theo!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Trợ lý, tăng điện áp lên mức tối đa! Một sinh vật có thể phóng ra dòng điện tám trăm sáu mươi Vôn giật ngất ngây cả cá sấu hai mét, nhưng tại sao chính nó lại không bị giật chết lăn quay? Đó chính là Lươn Điện, nhà máy điện sống khét tiếng của rừng rậm Nam Mỹ. Hơn tám mươi phần trăm cơ thể của nó là sáu ngàn tế bào pin sinh học nối tiếp nhau, tích tụ điện thế mạnh gấp bốn lần ổ cắm điện gia đình! [surprise-wa] Khi săn mồi, nó phóng xung điện kép hack thẳng vào hệ thần kinh ép cơ bắp con mồi co giật làm lộ vị trí, rồi tung cú nhảy dí cằm trực tiếp truyền trọn nguồn điện cực mạnh vào tim kẻ thù! Nhưng sở dĩ nó không bị giật chết là nhờ lớp mỡ cách điện dày cộp, toàn bộ nội tạng dồn hết lên đầu, và dòng điện luôn chọn thoát ra môi trường nước có điện trở thấp hơn! [laughter] Vậy là bí mật đã sáng tỏ: một tuyệt tác thiết kế của tự nhiên, biến thịt da thành vũ khí sốc điện tối thượng mà không hề tự thiêu rụi chính mình!
```

**Whisper prompt:** `Lươn Điện, Nhà Máy Điện Sống, Electrophorus electricus, Electrophorus voltai, Kenneth Catania, David de Santana, electrocytes, 860V, 600V, 10V, 6.000 pin, cá sấu Caiman, Amazon, Bọ Pháo Thủ`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| tám trăm sáu mươi Vôn | 860V |
| Tám trăm sáu mươi Vôn | 860V |
| tám trăm sáu mươi vôn | 860V |
| Tám trăm sáu mươi vôn | 860V |
| sáu trăm Vôn | 600V |
| Sáu trăm Vôn | 600V |
| sáu trăm vôn | 600V |
| mười Vôn | 10V |
| Mười Vôn | 10V |
| mười vôn | 10V |
| không phẩy mười lăm Vôn | 0,15V |
| hai trăm hai mươi Vôn | 220V |
| hai trăm hai mươi vôn | 220V |
| một Am-pe | 1A |
| một am-pe | 1A |
| tám trăm sáu mươi Oát | 860W |
| sáu ngàn | 6.000 |
| Sáu ngàn | 6.000 |
| năm ngàn | 5.000 |
| hai ngàn mười chín | 2019 |
| hai ngàn mười sáu | 2016 |
| hai ngàn mười bốn | 2014 |
| hai mét | 2m |
| hai mét rưỡi | 2,5m |
| hai mươi ki-lô-gam | 20kg |
| Hai mươi ki-lô-gam | 20kg |
| tám mươi phần trăm | 80% |
| Tám mươi phần trăm | 80% |
| hai mươi phần trăm | 20% |
| Hai mươi phần trăm | 20% |
| mười lăm phút | 15 phút |
| mười phút | 10 phút |
| năm phút | 5 phút |
| một mili-giây | 1 mili-giây |
| hai đến ba phần nghìn giây | 2-3 phần nghìn giây |
| gấp bốn lần | gấp 4 lần |
| gấp hai lần | gấp 2 lần |
| năm cấp độ | 5 cấp độ |
| Cấp độ một | Cấp độ 1 |
| Cấp độ hai | Cấp độ 2 |
| Cấp độ ba | Cấp độ 3 |
| Cấp độ bốn | Cấp độ 4 |
| Cấp độ năm | Cấp độ 5 |
| Tập mười tám | Tập 18 |
| năm trăm lần mỗi giây | 500 lần/giây |
| một trăm độ C | 100°C |
| một tiếng | 1 tiếng |
| Ken-nét Ca-ta-ni-a | Kenneth Catania |
| Đê Xan-ta-na | de Santana |
| Vôn-tai | voltai |
| Ê-léc-trô-pho-rút | Electrophorus |
| Văn-đơ-bin | Vanderbilt |
| Xmít-xô-ni-an | Smithsonian |
| Cai-man | Caiman |
| A-ma-dôn | Amazon |
| mười bảy | 17 |
| hai mươi | 20 |
| ba mươi | 30 |
| bốn trăm Vôn | 400V |
| bốn trăm nhịp | 400 nhịp |
| bốn trăm | 400 |
| hai trăm năm | 200 năm |
| trăm triệu năm | trăm triệu năm |
| hàng trăm triệu năm | hàng trăm triệu năm |
| nửa mét | 0,5m |
| mười phân | 10cm |
| ba mươi xăng-ti-mét | 30cm |
| Ba mươi xăng-ti-mét | 30cm |
| một phần mười giây | 1/10 giây |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · MẪU VẬT PIN SỐNG 860 VÔN · 84.1s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:05.3 (5.3s) | L01 | Chào mừng tất cả các trợ lý nghiên cứu đã bước vào Phòng Thí Nghiệm Sinh Học Tối Mật! Rè rè... Xoẹt! |  | BÊN TRÁI giáo sư nhà khoa học điên tóc bạc bù xù mặc áo blouse trắng, đeo găng tay cao su cách điện dày cộp màu đỏ, tay cầm vôn kế đo điện đang háo hức bật các công tắc nguồn; Ở GIỮA tấm biển neon khổng lồ nhấp nháy phát sáng 'PHÒNG THÍ NGHIỆM SINH HỌC TỐI MẬT'; BÊN PHẢI cô trợ lý phòng thí nghiệm đeo kính cận tròn, tóc đuôi ngựa buộc gọn, tay cầm bảng kẹp tài liệu kiểm tra thông số đang nhìn vào đồng hồ đo điện áp n |
| b02 | 00:05.3–00:09.6 (4.3s) | L02 | Tiếng hồ quang điện nổ lép bép trong bóng tối, và đồng hồ đo vôn kế đang nhảy số loạn xạ. |  | Cận cảnh bảng điều khiển phòng thí nghiệm: các tia hồ quang điện màu xanh tím nổ lách tách chói lòa; một chiếc vôn kế kim điện áp đang vọt qua vạch đỏ nguy hiểm. KHÔNG có Lươn Điện trong cảnh này. |
| b03 | 00:09.6–00:16.8 (7.2s) | L03 | Đằng sau tấm kính cường lực chống điện dày 10cm kia, một mẫu vật thủy quái kỳ dị bậc nhất hành tinh vừa được áp giải từ lưu vực sông Amazon về đây! | **KÍNH 10CM** · CHỐNG ĐIỆN CAO THẾ · L/380 · [0.25, 0.45] | Góc nhìn qua tấm kính cường lực chống điện dày 10cm: một bể nước ngầm khổng lồ tăm tối, bóng dáng dài ngoằng của chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh đang bơi lượn uốn lượn tỏa ra ánh sáng điện ma mị. |
| b04 | 00:16.8–00:22.9 (6.2s) | L04 | Báo cáo giáo sư! Nguồn điện trong bể chứa đang tăng vọt bất thường, tất cả bóng đèn cảnh báo đều đang chớp đỏ liên tục! |  | BÊN TRÁI cô trợ lý phòng thí nghiệm đeo kính cận tròn, tóc đuôi ngựa buộc gọn, tay cầm bảng kẹp tài liệu kiểm tra thông số ôm bảng kẹp tài liệu toát mồ hôi hột chỉ tay về phía bể chứa; BÊN PHẢI dàn đèn cảnh báo hình tam giác tia sét đang nhấp nháy đỏ rực khẩn cấp. KHÔNG có Lươn Điện trong cảnh này. |
| b05 | 00:22.9–00:32.0 (9.0s) | L05 | Bình tĩnh nào cô trợ lý! Hãy đeo kính cách điện vào và ghi chép nhật ký thật cẩn thận! Mẫu vật số 17 hôm nay là một sinh vật mà cả thế giới quen miệng gọi là Lươn Điện. |  | BÊN TRÁI giáo sư nhà khoa học điên tóc bạc bù xù mặc áo blouse trắng, đeo găng tay cao su cách điện dày cộp màu đỏ, tay cầm vôn kế đo điện cười lớn tự tin đưa chiếc kính cách điện màu cam cho trợ lý; BÊN PHẢI chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện  |
| b06 | 00:32.0–00:45.9 (14.0s) | L06 | Nhưng tôi xin tiết lộ ngay một sự thật gây sốc đầu tiên: về mặt phả hệ sinh học, nó hoàn toàn không phải là lươn! Nó không có bất kỳ họ hàng nào với loài lươn đồng hay lươn biển, mà thuộc bộ cá dao Nam Mỹ, tức là có họ gần gũi với cá trê và cá da trơn hơn! |  | Cây phả hệ sinh học hài hước: BÊN TRÁI hình ảnh con lươn đồng bị gạch chéo đỏ; BÊN PHẢI chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh đứng cạnh một chú cá trê da trơn có râu với dấu tích xanh xác nhận họ hàng gần gũi. |
| b07 | 00:45.9–00:55.7 (9.8s) | L07 | Nhưng tại sao chúng ta lại gọi nó bằng biệt danh Nhà Máy Điện Sống? Bởi vì toàn bộ cấu trúc cơ thể của con cá này sinh ra chỉ để phục vụ một mục đích duy nhất: biến thịt da thành vũ khí sốc điện hủy diệt! | **PIN SỐNG** · NHÀ MÁY ĐIỆN SỐNG · R/380 · [0.75, 0.45] | Chân dung phóng to của chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh: toàn thân bao bọc bởi mạng lưới mạch điện phát sáng vàng và xanh neon, bên cạnh là biểu tượng nhà máy phát điện mini đang hoạt động hết công suất. |
| b08 | 00:55.7–01:06.1 (10.4s) | L08 | Hơn 80% chiều dài cơ thể của nó là những khối pin sinh học nối tiếp nhau, có khả năng kích hoạt nguồn điện lên tới 860V — tức là mạnh gấp 4 lần ổ cắm điện 220V trong nhà bạn! | **80% PIN** · THÂN CHỨA ĐIỆN · L/420 · [0.28, 0.5]<br>**860V** · GẤP 4 LẦN 220V · R/370 · [0.72, 0.45] | Sơ đồ giải phẫu cắt lớp: 80% thân hình chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh được chia thành hàng ngàn ngăn pin xếp nối tiếp; so sánh BÊN PHẢI với 4 ổ cắm điện 220V gia đình tóe lửa. |
| b09 | 01:06.1–01:19.7 (13.6s) | L09 | Hôm nay, tôi sẽ kích hoạt quy trình thí nghiệm 5 cấp độ tăng dần: từ máy phát radar định vị 10V, vũ khí hack hệ thần kinh con mồi từ xa, cú nhảy dí cằm điện giật ngất ngây cá sấu 2m, cho đến bí mật vì sao nó không bị điện giật chết chính mình! | **5 CẤP ĐỘ** · QUY TRÌNH THÍ NGHIỆM · R/390 · [0.75, 0.45] | Bảng thang đo 5 cấp độ thử thách sáng đèn rực rỡ từ Cấp 1 đến Cấp 5; giáo sư nhà khoa học điên tóc bạc bù xù mặc áo blouse trắng, đeo găng tay cao su cách điện dày cộp màu đỏ, tay cầm vôn kế đo điện cầm chiếc cần gạt công suất chuẩn bị gạt nấc đầu tiên. KHÔNG có Lươn Điện trong cảnh này. |
| b10 | 01:19.7–01:24.1 (4.4s) | L10 | Hãy siết chặt dây an toàn, chúng ta bắt đầu kích hoạt Cấp độ 1 ngay bây giờ! |  | BÊN TRÁI giáo sư nhà khoa học điên tóc bạc bù xù mặc áo blouse trắng, đeo găng tay cao su cách điện dày cộp màu đỏ, tay cầm vôn kế đo điện và cô trợ lý phòng thí nghiệm đeo kính cận tròn, tóc đuôi ngựa buộc gọn, tay cầm bảng kẹp tài liệu kiểm tra thông số thắt dây an toàn ngồi trên ghế thí nghiệm; BÊN PHẢI dòng điện từ bể nước bắt đầu phóng ra những tia lửa sáng lóa mở màn. |

### scene02 · 6.000 TẾ BÀO PIN VÀ RADAR ĐỊNH VỊ BÙN LẦY · 79.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.8 (9.8s) | L11 | Khởi động Cấp độ 1: Phân tích cơ chế nạp điện và hệ thống radar định vị trong bùn lầy! Hãy nhìn kỹ vào thân hình dài tới 2m và nặng 20kg của mẫu vật. | **DÀI 2M** · KÍCH THƯỚC KHỦNG · R/360 · [0.75, 0.42]<br>**NẶNG 20KG** · THỂ TRỌNG KHỔNG LỒ · R/460 · [0.75, 0.55] | BÊN TRÁI tấm biển phát sáng 'CẤP ĐỘ 1: PHÂN TÍCH PIN & RADAR BÙN LẦY'; BÊN PHẢI thước đo chiều dài hiển thị 2m và chiếc cân hiển thị 20kg. KHÔNG có Lươn Điện trong cảnh này. |
| b02 | 00:09.8–00:19.6 (9.8s) | L12 | Tất cả các cơ quan nội tạng quan trọng nhất như tim, gan, dạ dày và mang thở đều bị dồn ép lại vỏn vẹn trong 20% phần đầu phía trước! Toàn bộ phần thân dài ngoằng còn lại chính là | **20% ĐẦU** · DỒN MỌI NỘI TẠNG · L/380 · [0.28, 0.45] | Sơ đồ X-quang sinh học: chỉ 20% phần đầu chứa tim, não, dạ dày nhỏ xíu được đóng khung bảo vệ; 80% còn lại là 3 cơ quan phát điện đồ sộ chiếm trọn thân thể. |
| b03 | 00:19.6–00:24.5 (4.9s) | L13 | ba cơ quan phát điện độc lập! Cơ quan phát điện chính, cơ quan Hun-tơ và cơ quan Sách! |  | Ba khối cơ quan phát điện được tô màu khác nhau: Cơ quan Chính màu đỏ cam, cơ quan Hunter màu vàng, và cơ quan Sachs màu xanh lam chạy dọc suốt thân chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh. |
| b04 | 00:24.5–00:31.0 (6.5s) | L14 | Bên trong ba khối cơ này chứa khoảng 5.000 đến 6.000 tế bào phát điện hình chiếc đĩa dẹp xếp chồng khít lên nhau thành hàng trăm cột dài song song. | **6.000 PIN** · TẾ BÀO ELECTROCYTE · L/380 · [0.28, 0.45] | Kính hiển vi phóng to hàng ngàn lần: 6.000 tế bào electrocyte hình đĩa dẹp xếp chồng ngay ngắn như cọc tiền xu pin nối tiếp nhau phát sáng điện tích âm và dương. |
| b05 | 00:31.0–00:43.8 (12.8s) | L15 | Mỗi tế bào này giống như một cục pin cúc áo mini, tạo ra một điện thế cực nhỏ chỉ 0,15V. Nhưng khi hàng ngàn tế bào này được thần kinh kích hoạt đồng loạt nối tiếp nhau, các điện thế cộng dồn lại tạo thành một cú sốc điện kinh thiên động địa! | **0,15V/PIN** · CỘNG DỒN NỐI TIẾP · R/420 · [0.72, 0.5] | Mô phỏng vật lý: một tế bào electrocyte đơn lẻ sinh ra 0,15V như pin đồng hồ cúc áo; mũi tên dẫn sang hàng ngàn tế bào cộng dồn điện áp tăng vọt theo cấp số nhân. |
| b06 | 00:43.8–00:53.8 (10.0s) | L16 | Nhưng ở chế độ bình thường, Nhà Máy Điện Sống không dại gì xả hết điện năng! Nó sử dụng cơ quan Sách ở đuôi để liên tục phát ra những xung điện áp thấp chỉ khoảng 10V với tần số 20 nhịp mỗi giây. | **10V RADAR** · ĐỊNH VỊ ĐIỆN ÁP THẤP · L/380 · [0.25, 0.45] | Chế độ radar sinh học: từ phần đuôi của chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh, những vòng sóng điện áp thấp 10V màu xanh dương lan tỏa đều đặn ra làn nước xung quanh như sóng radar quét vòng. |
| b07 | 00:53.8–01:05.2 (11.4s) | L17 | Vùng nước sông Amazon đục ngầu phù sa khiến mắt của lươn điện gần như bị mù lòa. Nhưng nhờ trường điện 10V bao bọc xung quanh cơ thể, nó có thể cảm nhận mọi vật cản và con mồi bơi qua hệt như một chiếc tàu ngầm bật sóng sonar! |  | Lòng sông Amazon đục ngầu đen kịt đầy bùn lầy; đôi mắt chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh đeo kính râm mù lòa nhưng các thụ thể điện trên đầu vẫn vẽ ra bản đồ 3D xung quanh rõ mồn một. |
| b08 | 01:05.2–01:13.5 (8.4s) | L18 | Giáo sư ơi! Màn hình radar vừa phát hiện một đàn cá nhỏ đang vùi mình dưới lớp bùn sâu 30cm! Nó làm sao bắt được chúng ạ? Câu hỏi rất hay! | **SÂU 30CM** · DƯỚI BÙN ĐẶC · R/390 · [0.75, 0.48] | Màn hình radar phòng thí nghiệm: các chấm xanh nhấp nháy phát hiện đàn cá nhỏ vùi sâu 30cm dưới lớp bùn; cô trợ lý phòng thí nghiệm đeo kính cận tròn, tóc đuôi ngựa buộc gọn, tay cầm bảng kẹp tài liệu kiểm tra thông số kinh ngạc tròn mắt theo dõi. KHÔNG có Lươn Điện trong cảnh này. |
| b09 | 01:13.5–01:19.5 (6.0s) | L19 | Đã đến lúc chuyển giao diện thí nghiệm sang Cấp độ 2: Kỹ thuật hack não và thao túng cơ bắp con mồi từ xa! |  | BÊN TRÁI giáo sư nhà khoa học điên tóc bạc bù xù mặc áo blouse trắng, đeo găng tay cao su cách điện dày cộp màu đỏ, tay cầm vôn kế đo điện giơ tay chỉ lên bảng điều khiển; bảng đèn chuyển sang màu cam sáng rực báo hiệu 'CẤP ĐỘ 2: HACK NÃO TỪ XA'. KHÔNG có Lươn Điện trong cảnh này. |

### scene03 · XUNG ĐIỆN KÉP THAO TÚNG CƠ BẮP CON MỒI TỪ XA · 80.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:03.4 (3.4s) | L20 | Bước vào Cấp độ 2: Thử nghiệm vũ khí điều khiển thần kinh từ xa! |  | BÊN TRÁI tấm biển 'CẤP ĐỘ 2: VŨ KHÍ HACK NÃO CON MỒI'; BÊN PHẢI hình minh họa một bộ não cá bị các xung điện điều khiển từ xa như con rối dây. KHÔNG có Lươn Điện trong cảnh này. |
| b02 | 00:03.4–00:14.1 (10.8s) | L21 | Năm 2014, nhà sinh vật học lừng danh Kenneth Catania tại Đại học Vanderbilt đã công bố một nghiên cứu chấn động trên tạp chí Science danh giá, vạch trần bí mật săn mồi đỉnh cao của Nhà Máy Điện Sống! | **CATANIA 14** · KHOA HỌC SCIENCE · L/400 · [0.28, 0.5] | Trang bìa tạp chí khoa học danh giá Science năm 2014: giáo sư Kenneth Catania tại Đại học Vanderbilt đang tiến hành thí nghiệm xung điện kép với máy hiện sóng. KHÔNG có Lươn Điện trong cảnh này. |
| b03 | 00:14.1–00:26.6 (12.5s) | L22 | Khi nghi ngờ có con mồi đang ẩn nấp dưới đáy bùn, Lươn Điện sẽ phóng ra một cặp xung điện kép cực mạnh gồm hai cú sốc cách nhau đúng 2-3 phần nghìn giây! Cặp xung điện này không phải để giết chết con mồi, mà nó bắt chước hoàn hảo tín hiệu điều khiển vận động của não bộ! | **XUNG KÉP** · CÁCH NHAU 2MS · R/380 · [0.75, 0.45] | chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh phóng ra hai xung điện chớp nhoáng (doublets) cách nhau chỉ 2 mili-giây; các tia sóng điện màu tím xuyên thẳng xuống lớp bùn chạm vào đàn cá đang trốn. |
| b04 | 00:26.6–00:33.6 (7.0s) | L23 | Tín hiệu này xâm nhập thẳng vào hệ thần kinh của con cá đang nấp, ép toàn bộ các bó cơ trên cơ thể con mồi phải co giật kịch liệt ngoài ý muốn! |  | Mô phỏng 3D hệ thần kinh: tín hiệu xung điện của lươn chạy dọc tủy sống con cá, chiếm quyền kiểm soát các bó cơ ép cơ thể co thắt dữ dội ngoài ý muốn. KHÔNG có Lươn Điện trong cảnh này. |
| b05 | 00:33.6–00:42.8 (9.2s) | L24 | Ối giời ơi! Tự nhiên đuôi tôi nó giật bắn lên thế này! Tôi đâu có muốn bơi đâu mà cơ thể cứ giãy nảy lên văng cả bùn ra ngoài thế này cứu tôi với! Chính xác là như vậy! |  | Cận cảnh chú cá nhỏ dưới bùn: mắt trợn ngược, toàn thân giật nảy tanh tách như bị ai giật dây cót, đuôi vẫy loạn xạ làm bùn nước văng tung tóe hài hước. KHÔNG có Lươn Điện trong cảnh này. |
| b06 | 00:42.8–00:51.2 (8.4s) | L25 | Con cá nhỏ vừa giật bắn mình làm rung chuyển lớp bùn là vị trí ẩn nấp lập tức bị bại lộ hoàn toàn trước cảm biến của thợ săn! Và ngay trong 1/10 giây tiếp |  | Vị trí con mồi phát sáng như ngọn hải đăng giữa bùn; cảm biến của chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh khóa chặt mục tiêu với tâm ngắm màu đỏ rực rỡ. |
| b07 | 00:51.2–00:59.8 (8.6s) | L26 | theo, Nhà Máy Điện Sống lập tức tung ra đòn kết liễu tàn nhẫn: nó xả liên tiếp hàng trăm xung điện cao thế 400V với tần số 400 nhịp mỗi giây! | **400V** · ĐÒN ĐIỆN TÊ LIỆT · L/370 · [0.25, 0.45]<br>**400 NHỊP/S** · TẦN SỐ TỬ THẦN · R/420 · [0.75, 0.5] | Đòn kết liễu cao thế: chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh xả ra loạt xung điện 400V với tốc độ 400 nhịp/giây; dòng điện sáng rực như sấm sét bao trùm toàn bộ đáy hồ. |
| b08 | 00:59.8–01:06.9 (7.1s) | L27 | Toàn bộ cơ bắp của con mồi lập tức rơi vào trạng thái co cứng cực đại, bị đông cứng như một khúc gỗ hoàn toàn tê liệt không thể cử động hay hít thở! |  | Con cá mồi bị đông cứng đơ như một thanh gỗ hóa đá, mắt đờ đẫn không cử động được một chiếc vây; các dòng điện nhỏ vẫn chạy râm ran trên da. KHÔNG có Lươn Điện trong cảnh này. |
| b09 | 01:06.9–01:15.2 (8.3s) | L28 | Và trước khi con mồi kịp hiểu chuyện gì vừa xảy ra, Lươn Điện há chiếc miệng rộng ngoác tạo ra một lực hút chân không cực mạnh nuốt chửng nạn nhân vào bụng chỉ trong chớp mắt! |  | chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh há toang chiếc miệng tạo ra lực xoáy hút chân không cực mạnh; con cá bị hút tọt thẳng vào miệng lươn trong một phần chớp mắt. |
| b10 | 01:15.2–01:20.7 (5.5s) | L29 | Một cơ chế săn mồi điều khiển từ xa tinh vi đến mức các kỹ sư quân sự cũng phải ngả mũ bái phục! |  | BÊN TRÁI giáo sư nhà khoa học điên tóc bạc bù xù mặc áo blouse trắng, đeo găng tay cao su cách điện dày cộp màu đỏ, tay cầm vôn kế đo điện và cô trợ lý phòng thí nghiệm đeo kính cận tròn, tóc đuôi ngựa buộc gọn, tay cầm bảng kẹp tài liệu kiểm tra thông số đứng vỗ tay tán thưởng trước màn hình phân tích; BÊN PHẢI chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chi |

### scene04 · CÚ NHẢY DÍ CẰM ĐIỆN GIẬT NGẤT CÁ SẤU 2 MÉT · 95.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.9 (7.9s) | L30 | Cảnh báo mức độ nguy hiểm cực hạn! Chúng ta bước vào Cấp độ 3: Đối đầu với những kẻ săn mồi khổng lồ trên cạn và cú nhảy dí cằm huyền thoại! |  | BÊN TRÁI bảng báo động cấp 3 màu đỏ rực 'CẤP ĐỘ 3: ĐỐI ĐẦU BẠO CHÚA CÁ SẤU'; BÊN PHẢI hình vẽ cá sấu Caiman khổng lồ với hàm răng sắc nhọn. KHÔNG có Lươn Điện trong cảnh này. |
| b02 | 00:07.9–00:18.7 (10.8s) | L31 | Hơn 200 năm trước, nhà thám hiểm vĩ đại A-lếch-xăng-đơ von Hum-bôn từng kể lại câu chuyện lươn điện phóng điện tấn công cả đàn ngựa băng qua sông, nhưng suốt hai thế kỷ giới khoa học đều nghĩ rằng ông chỉ phóng đại câu chuyện dân gian! | **200 NĂM** · BÍ ẨN VON HUMBOLDT · L/390 · [0.28, 0.48] | Bức tranh lịch sử thế kỷ 19: nhà thám hiểm Alexander von Humboldt đứng trên bờ sông vẽ lại cảnh đàn ngựa hí vang nhảy cẫng lên giữa dòng nước sông Nam Mỹ. KHÔNG có Lươn Điện trong cảnh này. |
| b03 | 00:18.7–00:32.5 (13.8s) | L32 | Cho đến tận năm 2016, giáo sư Ca-ta-ni-a mới chính thức giải mã được hành vi kinh hoàng này trong phòng thí nghiệm! Trong môi trường nước sâu, dòng điện phóng ra từ cơ thể lươn sẽ bị phân tán ra mọi hướng trong nước, khiến điện áp truyền vào cơ thể kẻ địch bị suy giảm đáng kể. |  | Phòng thí nghiệm hiện đại của giáo sư Kenneth Catania: các thiết bị cảm biến ghi lại dòng điện và camera quay siêu chậm phân tích chuyển động của lươn điện. KHÔNG có Lươn Điện trong cảnh này. |
| b04 | 00:32.5–00:40.9 (8.4s) | L33 | Nhưng khi bị một kẻ săn mồi to xác như cá sấu Caiman, báo đốm hay con người dồn vào vùng nước nông, Nhà Máy Điện Sống sẽ tung ra tuyệt chiêu cận chiến nguy hiểm nhất! |  | So sánh môi trường: BÊN TRÁI dòng điện dưới nước sâu bị rò rỉ phân tán ra bốn phương tám hướng; BÊN PHẢI lươn điện trong nước nông đang chuẩn bị bật nhảy. |
| b05 | 00:40.9–00:53.6 (12.7s) | L34 | Nó không nằm dưới nước phóng điện, mà dùng chiếc đuôi khỏe khoắn gập mạnh, ngóc đầu phóng vọt lên khỏi mặt nước cao tới 0,5m! Nó áp sát phần cằm dẫn điện cực dương trực tiếp vào ngực hoặc cổ họng của kẻ tấn công, trong khi phần đuôi cực âm vẫn cắm chặt dưới nước! | **NHẢY 0,5M** · CÚ NHẢY DÍ CẰM · L/370 · [0.25, 0.45] | Khoảnh khắc ngoạn mục: chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh uốn đuôi bật tung người phóng vọt lên khỏi mặt nước cao 0,5m; cằm dẫn điện cực dương dí sát thẳng vào ngực con cá sấu khổng lồ. |
| b06 | 00:53.6–01:01.6 (8.1s) | L35 | Toàn bộ nguồn điện khủng khiếp chạy thẳng một mạch xuyên qua tim và não của kẻ săn mồi mà không hề bị tiêu hao một mi-li-vôn nào ra môi trường nước xung quanh! |  | Mạch điện kín không suy hao: đầu lươn cực dương dí vào ngực cá sấu, đuôi lươn cực âm cắm dưới nước; toàn bộ luồng sét chạy thẳng xuyên qua tim chú cá sấu Caiman Nam Mỹ dài 2m da xanh vảy sừng, biểu cảm hoảng hốt mắt xoay tròn bị giật cháy đen xù lông. |
| b07 | 01:01.6–01:11.2 (9.6s) | L36 | Này con lươn trơn tuột kia, nhìn tao là cá sấu chúa dài 2m đây này, liệu hồn mà nạp mạng... Á á á! Cứu tao với! Điện giật xoắn cả đuôi, tim ngừng đập rồi trời ơi! | **CÁ SẤU 2M** · GIẬT TÉ KHÓI · R/420 · [0.75, 0.5] | Cảnh tượng bi hài: chú cá sấu chú cá sấu Caiman Nam Mỹ dài 2m da xanh vảy sừng, biểu cảm hoảng hốt mắt xoay tròn bị giật cháy đen xù lông dài 2m bị điện giật cứng đờ toàn thân, các vảy dựng đứng, mắt trợn tròn xoay vòng, khói bốc nghi ngút từ đầu. |
| b08 | 01:11.2–01:22.3 (11.0s) | L37 | Cú nhảy dí cằm trực tiếp này tạo ra một dòng điện cực mạnh đủ sức làm tê liệt hoàn toàn hệ cơ tim của một con cá sấu dài 2m hoặc một con ngựa trưởng thành, khiến chúng ngã gục ngay tại chỗ vì sốc tim và ngạt thở! |  | Sơ đồ giải phẫu tim cá sấu bị ngừng đập tạm thời do dòng điện cao thế xuyên qua; cá sấu ngã ngửa bất tỉnh nhân sự trên bãi bùn. KHÔNG có Lươn Điện trong cảnh này. |
| b09 | 01:22.3–01:31.5 (9.2s) | L38 | Chưa hết, khi gặp con mồi quá to, nó còn uốn cong cơ thể thành hình chữ U, kẹp chặt con mồi vào giữa đầu và đuôi để nhân đôi cường độ điện trường xuyên qua cơ thể nạn nhân! | **CHỮ U** · NHÂN ĐÔI ĐIỆN TRƯỜNG · L/380 · [0.25, 0.45] | Chiến thuật hình chữ U: chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh uốn cong người ôm trọn con mồi vào giữa đầu và đuôi; điện trường giữa hai cực nhân đôi cường độ ép chết con mồi trong gọng kìm điện. |
| b10 | 01:31.5–01:35.4 (4.0s) | L39 | Một chiến thuật chiến đấu công thủ toàn diện đến mức rùng mình! |  | BÊN TRÁI cá sấu Caiman lủi thủi bò trốn lên bờ với chiếc đuôi còn giật giật; BÊN PHẢI chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh bơi ngạo nghễ như chúa tể đầm lầy không đối thủ. |

### scene05 · TẠI SAO LƯƠN ĐIỆN KHÔNG BỊ ĐIỆN GIẬT CHẾT? · 92.6s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.4 (9.4s) | L40 | Đến đây, chắc chắn câu hỏi lớn nhất đang sôi sục trong đầu các trợ lý là: Phóng ra nguồn điện khủng khiếp như vậy, tại sao chính con Lươn Điện lại không bị giật chết lăn quay ra đấy? |  | BÊN TRÁI tấm biển 'CẤP ĐỘ 4: BÍ MẬT KHÔNG BỊ GIẬT CHẾT'; BÊN PHẢI chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh đứng khoanh tay tự tin trước tia sét với chiếc khiên bảo vệ phát sáng. KHÔNG có Lươn Điện trong cảnh này. |
| b02 | 00:09.4–00:15.8 (6.4s) | L41 | Câu trả lời nằm ở ba tấm lá chắn vật lý và sinh học thiên tài mà tiến hóa đã trang bị cho Nhà Máy Điện Sống! |  | Hình minh họa 3 tấm lá chắn năng lượng phát sáng xếp trước mặt chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh: lá chắn điện trở vật lý, lá chắn vị trí cơ quan, và lá chắn kích thước cơ thể. |
| b03 | 00:15.8–00:23.0 (7.2s) | L42 | Lá chắn thứ nhất là quy luật điện trở vật lý! Cơ thể của lươn điện được bọc kín bởi một lớp da dày và các lớp mỡ dày có điện trở rất cao. | **ĐIỆN TRỞ** · MỠ CÁCH ĐIỆN · L/390 · [0.28, 0.48] | Sơ đồ vật lý định luật Ohm: lớp da và mỡ của lươn có điện trở cực cao R-cao; mô phỏng dòng điện gặp vật cản cách điện an toàn. |
| b04 | 00:23.0–00:37.5 (14.4s) | L43 | Trong khi đó, dòng điện luôn có xu hướng chọn con đường có điện trở thấp nhất để di chuyển. Môi trường nước sông Amazon xung quanh cơ thể nó có điện trở thấp hơn rất nhiều so với lớp mỡ bảo vệ, nên phần lớn năng lượng điện phóng ra sẽ lập tức thoát thẳng ra nước xung quanh thay vì thâm nhập ngược vào sâu trong nội tạng của lươn! |  | Đường đi của dòng điện: dòng điện chọn con đường nước sông Amazon có điện trở cực thấp, thoát ào ạt ra ngoài làn nước xung quanh mà không đi vào nội tạng lươn. KHÔNG có Lươn Điện trong cảnh này. |
| b05 | 00:37.5–00:50.9 (13.5s) | L44 | Lá chắn thứ hai là bố cục vị trí cơ quan sinh học! Như tôi đã nhấn mạnh ở đầu buổi thí nghiệm, toàn bộ não bộ, tim và các cơ quan nội tạng nhạy cảm đều được cô lập hoàn toàn ở phần đầu, cách xa khu vực ba cơ quan phát điện ở thân sau và được bao bọc bởi các lớp mô liên kết cách điện kiên |  | Bản đồ phân vùng an toàn sinh học: phần đầu chứa não và tim được bọc trong kén cách điện chuyên dụng; cách xa khu vực 3 cơ quan phát điện ở thân sau. |
| b06 | 00:50.9–00:54.7 (3.8s) | L45 | cố! Dòng điện đi từ đầu tới đuôi nhưng chỉ lướt qua bề mặt ngoài cơ thể! |  | Dòng điện cao thế chạy từ cực dương ở đầu tới cực âm ở đuôi nhưng chỉ lướt trên bề mặt mô cơ ngoài; nội tạng bên trong hoàn toàn bình an vô sự. |
| b07 | 00:54.7–01:02.0 (7.3s) | L46 | Và lá chắn thứ ba là yếu tố kích thước! Lươn Điện trưởng thành dài tới hơn 2m, nên mật độ dòng điện đi qua từng thớ cơ của nó bị pha loãng ra nhiều lần, |  | So sánh kích thước: thân hình lươn dài 2m làm loãng mật độ điện trường; các thớ cơ của lươn chỉ chịu một phần rất nhỏ dòng điện. |
| b08 | 01:02.0–01:11.3 (9.3s) | L47 | trong khi những con cá nhỏ hay con mồi bị nó dí sát thì phải hứng trọn mật độ điện trường dày đặc chí mạng! Nhưng Nhà Máy Điện Sống bất khả chiến bại này lại có một điểm yếu chết người cực kỳ bi hài! |  | Con cá nhỏ đối diện hứng trọn mật độ điện dày đặc hàng chục nghìn vôn/m2; cơ thể cá nhỏ sáng rực lên vì điện trường tập trung cực cao. KHÔNG có Lươn Điện trong cảnh này. |
| b09 | 01:11.3–01:17.8 (6.5s) | L48 | 80% lượng oxy của lươn điện được hấp thụ qua các mao mạch trong miệng chứ mang của nó gần như bị thoái hóa hoàn toàn! | **80% OXY** · THỞ BẰNG MIỆNG · R/380 · [0.75, 0.45] | Điểm yếu chết người: khoang miệng chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh chứa đầy mao mạch đỏ rực hấp thụ 80% oxy không khí; mang cá teo nhỏ không thể thở trong nước. |
| b10 | 01:17.8–01:22.7 (4.9s) | L49 | Cứ mười đến 15 phút một lần, nó bắt buộc phải ngoi đầu lên mặt nước để hít thở không khí. | **10-15 PHÚT** · PHẢI NGOI LÊN THỞ · L/410 · [0.25, 0.5] | chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh thò đầu lên khỏi mặt nước hít một hơi không khí sảng khoái; đồng hồ đếm ngược 10-15 phút báo hiệu chu kỳ ngoi lên mặt nước bắt buộc. |
| b11 | 01:22.7–01:32.6 (9.9s) | L50 | Nếu bạn giữ chặt con lươn này dưới nước không cho nó ngoi lên, một sát thủ điện giật ngất cá sấu sẽ... chết đuối y như con người! Một nghịch lý sinh học quá đỗi thú vị! |  | Nghịch lý bi hài: một quả tạ giữ lươn dưới nước, chú lươn điện sặc nước ho sặc sụa với bóng thoại 'Cứu tôi, tôi chết đuối mất!'; giáo sư nhà khoa học điên tóc bạc bù xù mặc áo blouse trắng, đeo găng tay cao su cách điện dày cộp màu đỏ, tay cầm vôn kế đo điện và cô trợ lý phòng thí nghiệm đeo kính cận tròn, tóc đuôi ngựa buộc gọn, tay cầm bảng kẹp tài liệu kiểm tra thông số cười nghiêng ngả. |

### scene06 · SỨC MẠNH 860V VÀ BÓNG ĐEN BÍ ẨN TẬP 18 · 103.8s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:11.7 (11.7s) | L51 | Chào mừng quý vị bước vào Cấp độ tối thượng: Kỷ lục năng lượng mới nhất của thế giới hiện đại! Suốt 200 năm ròng rã, cả thế giới đinh ninh rằng hành tinh này chỉ có duy nhất một loài lươn điện với điện áp tối đa 600V. |  | BÊN TRÁI bảng đèn sáng rực rỡ 'CẤP ĐỘ TỐI THƯỢNG: KỶ LỤC 860 VÔN'; BÊN PHẢI hình ảnh các nhà khoa học đang đo đạc nguồn điện kỷ lục trên sông Amazon. KHÔNG có Lươn Điện trong cảnh này. |
| b02 | 00:11.7–00:21.1 (9.3s) | L52 | Nhưng vào năm 2019, nhóm nghiên cứu của tiến sĩ de Santana tại Viện Smithsonian đã phát hiện ra loài lươn điện mới mang tên Electrophorus voltai! | **2019** · DE SANTANA NATURE · R/380 · [0.75, 0.45] | Bài báo khoa học Nature Communications năm 2019 của tiến sĩ de Santana tại Viện Smithsonian, công bố phát hiện loài lươn điện mới Electrophorus voltai. KHÔNG có Lươn Điện trong cảnh này. |
| b03 | 00:21.1–00:35.4 (14.3s) | L53 | Khi gắn thiết bị đo vào mẫu vật voltai này, chiếc kim đồng hồ đã vọt lên con số kỷ lục 860V! Đây chính là sinh vật phóng điện mạnh nhất từng được ghi nhận trong lịch sử Trái Đất, biến những dòng sông hoang dã Nam Mỹ trở thành những trạm biến áp tự nhiên kỳ vĩ bậc nhất hành tinh! | **KỶ LỤC** · MẠNH NHẤT HÀNH TINH · L/370 · [0.25, 0.45] | Cận cảnh chiếc vôn kế đo điện tử hiện số 860V màu vàng rực; chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh loài Electrophorus voltai tỏa ra các luồng sét cực quang tuyệt đẹp khắp bể nước. |
| b04 | 00:35.4–00:41.4 (6.1s) | L54 | Tiến hóa không chỉ tạo ra sự sống, mà còn tạo ra những kỳ quan công nghệ sinh học đi trước con người hàng trăm triệu năm! |  | Bức tranh hoang dã sông rừng Amazon: lươn điện bơi lượn như vị thần sấm sét dưới làn nước, biểu tượng cho kỳ quan công nghệ sinh học vĩ đại của tự nhiên. |
| b05 | 00:41.4–00:53.4 (12.0s) | L55 | Báo cáo giáo sư! Toàn bộ dữ liệu thử nghiệm của mẫu vật Lươn Điện đã được lưu trữ thành công vào hệ thống! Nhưng trên radar quét tầm xa, phòng thí nghiệm vừa bắt được tín hiệu của một quái kiệt tí hon cực kỳ nguy hiểm cho Tập 18! |  | cô trợ lý phòng thí nghiệm đeo kính cận tròn, tóc đuôi ngựa buộc gọn, tay cầm bảng kẹp tài liệu kiểm tra thông số bấm nút lưu trữ dữ liệu; màn hình radar góc phòng thí nghiệm đột nhiên phát tín hiệu cảnh báo nhấp nháy màu đỏ tía dữ dội. KHÔNG có Lươn Điện trong cảnh này. |
| b06 | 00:53.4–01:03.7 (10.3s) | L56 | Tuyệt vời lắm cô trợ lý! Xin mời toàn thể các nhà nghiên cứu hãy hướng mắt lên màn hình lớn trung tâm để giải mã BÓNG ĐEN BÍ ẨN của nhân vật xuất hiện trong Tập 18 tiếp theo! |  | Ánh đèn phòng thí nghiệm dịu xuống; chiếc màn hình chiếu khổng lồ ở trung tâm bật sáng với ánh hào quang màu cam lửa rực cháy kịch tính. KHÔNG có Lươn Điện trong cảnh này. |
| b07 | 01:03.7–01:14.4 (10.7s) | L57 | Xin gửi tới các bạn ba manh mối khoa học chấn động về bóng đen bí ẩn này: Thứ nhất, đây là siêu pháo thủ tí hon sở hữu khẩu súng hóa học liên thanh nã đạn 500 lần/giây ở nhiệt độ sôi sùng sục 100°C làm bỏng rát mọi kẻ thù! | **BÓNG ĐEN** · QUÁI KIỆT TẬP 18 · R/360 · [0.75, 0.42]<br>**500 PHÁT/S** · NÃ ĐẠN LIÊN THANH · L/420 · [0.25, 0.5] | Manh mối số 1: BÓNG ĐEN BÍ ẨN của một chú bọ cánh cứng tí hon đang nã pháo liên thanh 500 phát/giây ở 100°C kèm dấu hỏi chấm '?' màu đỏ phát sáng. KHÔNG có Lươn Điện trong cảnh này. |
| b08 | 01:14.4–01:19.6 (5.2s) | L58 | Thứ hai, phản ứng hóa học hai buồng đốt chết người: buồng chứa nhiên liệu và buồng kích nổ áp suất cực cao! | **2 BUỒNG** · ĐỘNG CƠ TÊN LỬA MINI · R/400 · [0.75, 0.48] | Manh mối số 2: Sơ đồ cấu tạo hệ thống 2 buồng đốt áp suất cực cao bên trong cơ thể bọ cánh cứng đẩy lùi kẻ thù. KHÔNG có Lươn Điện trong cảnh này. |
| b09 | 01:19.6–01:30.0 (10.4s) | L59 | Và thứ ba, kỷ lục thoát chết kinh dị bậc nhất: bị cóc nuốt chửng vào bụng suốt 1 tiếng đồng hồ, nó nã pháo xả độc ngay trong bao tử khiến cóc buồn nôn nôn thốc nôn tháo nguyên con ra ngoài vẫn sống nhăn nhở! | **SỐNG 1 GIỜ** · XẢ ĐỘC THOÁT CHẾT · L/400 · [0.25, 0.5] | Manh mối số 3: Một con cóc khổng lồ ôm bụng nôn thốc nôn tháo; BÓNG ĐEN BÍ ẨN chui từ miệng cóc ra ngoài sau 1 tiếng vẫn sống nhăn nhở giơ hai càng ăn mừng. KHÔNG có Lươn Điện trong cảnh này. |
| b10 | 01:30.0–01:38.7 (8.7s) | L60 | Các trợ lý khoa học có đoán ra bóng đen pháo thủ tí hon này là sinh vật nào không? Hãy để lại kết quả phân tích và dự đoán của bạn ngay dưới phần bình luận nhé! |  | BÓNG ĐEN BÍ ẨN đứng sừng sững giữa màn hình với dấu hỏi chấm '?' khổng lồ; xung quanh là các bong bóng bình luận '? ? ?' kêu gọi khán giả dự đoán. KHÔNG có Lươn Điện trong cảnh này. |
| b11 | 01:38.7–01:43.8 (5.0s) | L61 | Giáo sư phòng thí nghiệm xin chào tạm biệt và hẹn gặp lại các bạn trong cuộc thử nghiệm kỳ thú tiếp theo! |  | BÊN TRÁI giáo sư nhà khoa học điên tóc bạc bù xù mặc áo blouse trắng, đeo găng tay cao su cách điện dày cộp màu đỏ, tay cầm vôn kế đo điện và cô trợ lý phòng thí nghiệm đeo kính cận tròn, tóc đuôi ngựa buộc gọn, tay cầm bảng kẹp tài liệu kiểm tra thông số vẫy tay chào tạm biệt; BÊN PHẢI tấm biển gỗ đề chữ 'HẸN GẶP LẠI Ở TẬP 18 VỚI SIÊU PHÁO THỦ TÍ HON!'. KHÔNG có Lươn Điện trong cảnh này. |

## 5. Phân cảnh Shorts — từng beat

Banner: **860 VÔN GIẬT CÁ SẤU?! / VÌ SAO KHÔNG TỰ GIẬT?** · giọng 49.3s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Trợ lý, tăng điện áp lên mức tối đa! |  |
| s02 | 00:03.0 | S02 | Một sinh vật có thể phóng ra dòng điện 860V giật ngất ngây cả cá sấu 2m, | **860V** · GIẬT NGẤT CÁ SẤU · L/620 · [0.5, 0.45] |
| s03 | 00:07.6 | S03 | nhưng tại sao chính nó lại không bị giật chết lăn quay? |  |
| s04 | 00:10.4 | S04 | Đó chính là Lươn Điện, nhà máy điện sống khét tiếng của rừng rậm Nam Mỹ. |  |
| s05 | 00:14.5 | S05 | Hơn 80% cơ thể của nó là 6.000 tế bào pin sinh học nối tiếp nhau, | **80% PIN** · 6.000 TẾ BÀO ĐIỆN · L/640 · [0.5, 0.48] |
| s06 | 00:18.7 | S06 | tích tụ điện thế mạnh gấp 4 lần ổ cắm điện gia đình! | **GẤP 4 LẦN** · Ổ CẮM 220V · R/740 · [0.55, 0.55] |
| s07 | 00:22.0 | S07 | Khi săn mồi, nó phóng xung điện kép hack thẳng vào hệ thần kinh ép cơ bắp con mồi co giật làm lộ vị trí, | **HACK NÃO** · ÉP CO GIẬT TỪ XA · L/630 · [0.5, 0.46] |
| s08 | 00:27.9 | S08 | rồi tung cú nhảy dí cằm trực tiếp truyền trọn nguồn điện cực mạnh vào tim kẻ thù! | **DÍ CẰM** · TRUYỀN TRỰC TIẾP · R/650 · [0.55, 0.5] |
| s09 | 00:32.3 | S09 | Nhưng sở dĩ nó không bị giật chết là nhờ lớp mỡ cách điện dày cộp, toàn bộ nội tạng dồn hết lên đầu, | **CÁCH ĐIỆN** · BẢO VỆ NỘI TẠNG · L/640 · [0.5, 0.48] |
| s10 | 00:37.8 | S10 | và dòng điện luôn chọn thoát ra môi trường nước có điện trở thấp hơn! |  |
| s11 | 00:41.6 | S11 | Vậy là bí mật đã sáng tỏ: một tuyệt tác thiết kế của tự nhiên, |  |
| s12 | 00:45.1 | S12 | biến thịt da thành vũ khí sốc điện tối thượng mà không hề tự thiêu rụi chính mình! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chào mừng tất cả các trợ lý nghiên cứu đã bước vào Phòng Thí Nghiệm Sinh Học Tối Mật! Rè rè... Xoẹt!". Bố cục: BÊN TRÁI giáo sư nhà khoa học điên tóc bạc bù xù mặc áo blouse trắng, đeo găng tay cao su cách điện dày cộp màu đỏ, tay cầm vôn kế đo điện đang háo hức bật các công tắc nguồn; Ở GIỮA tấm biển neon khổng lồ nhấp nháy phát sáng 'PHÒNG THÍ NGHIỆM SINH HỌC TỐI MẬT'; BÊN PHẢI cô trợ lý phòng thí nghiệm đeo kính cận tròn, tóc đuôi ngựa buộc gọn, tay cầm bảng kẹp tài liệu kiểm tra thông số đang nhìn vào đồng hồ đo điện áp nhảy số điên cuồng. KHÔNG có Lươn Điện trong cảnh này.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tiếng hồ quang điện nổ lép bép trong bóng tối, và đồng hồ đo vôn kế đang nhảy số loạn xạ.". Bố cục: Cận cảnh bảng điều khiển phòng thí nghiệm: các tia hồ quang điện màu xanh tím nổ lách tách chói lòa; một chiếc vôn kế kim điện áp đang vọt qua vạch đỏ nguy hiểm. KHÔNG có Lươn Điện trong cảnh này.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đằng sau tấm kính cường lực chống điện dày 10cm kia, một mẫu vật thủy quái kỳ dị bậc nhất hành tinh vừa được áp giải từ lưu vực sông Amazon về đây!". Bố cục: Góc nhìn qua tấm kính cường lực chống điện dày 10cm: một bể nước ngầm khổng lồ tăm tối, bóng dáng dài ngoằng của chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh đang bơi lượn uốn lượn tỏa ra ánh sáng điện ma mị.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo giáo sư! Nguồn điện trong bể chứa đang tăng vọt bất thường, tất cả bóng đèn cảnh báo đều đang chớp đỏ liên tục!". Bố cục: BÊN TRÁI cô trợ lý phòng thí nghiệm đeo kính cận tròn, tóc đuôi ngựa buộc gọn, tay cầm bảng kẹp tài liệu kiểm tra thông số ôm bảng kẹp tài liệu toát mồ hôi hột chỉ tay về phía bể chứa; BÊN PHẢI dàn đèn cảnh báo hình tam giác tia sét đang nhấp nháy đỏ rực khẩn cấp. KHÔNG có Lươn Điện trong cảnh này.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bình tĩnh nào cô trợ lý! Hãy đeo kính cách điện vào và ghi chép nhật ký thật cẩn thận! Mẫu vật số 17 hôm nay là một sinh vật mà cả thế giới quen miệng gọi là Lươn Điện.". Bố cục: BÊN TRÁI giáo sư nhà khoa học điên tóc bạc bù xù mặc áo blouse trắng, đeo găng tay cao su cách điện dày cộp màu đỏ, tay cầm vôn kế đo điện cười lớn tự tin đưa chiếc kính cách điện màu cam cho trợ lý; BÊN PHẢI chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh bơi sát mặt kính nhếch mép chào một cách tinh quái.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng tôi xin tiết lộ ngay một sự thật gây sốc đầu tiên: về mặt phả hệ sinh học, nó hoàn toàn không phải là lươn! Nó không có bất kỳ họ hàng nào với loài lươn đồng hay lươn biển, mà thuộc bộ cá dao Nam Mỹ, tức là có họ gần gũi với cá trê và cá da trơn hơn!". Bố cục: Cây phả hệ sinh học hài hước: BÊN TRÁI hình ảnh con lươn đồng bị gạch chéo đỏ; BÊN PHẢI chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh đứng cạnh một chú cá trê da trơn có râu với dấu tích xanh xác nhận họ hàng gần gũi.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng tại sao chúng ta lại gọi nó bằng biệt danh Nhà Máy Điện Sống? Bởi vì toàn bộ cấu trúc cơ thể của con cá này sinh ra chỉ để phục vụ một mục đích duy nhất: biến thịt da thành vũ khí sốc điện hủy diệt!". Bố cục: Chân dung phóng to của chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh: toàn thân bao bọc bởi mạng lưới mạch điện phát sáng vàng và xanh neon, bên cạnh là biểu tượng nhà máy phát điện mini đang hoạt động hết công suất.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hơn 80% chiều dài cơ thể của nó là những khối pin sinh học nối tiếp nhau, có khả năng kích hoạt nguồn điện lên tới 860V — tức là mạnh gấp 4 lần ổ cắm điện 220V trong nhà bạn!". Bố cục: Sơ đồ giải phẫu cắt lớp: 80% thân hình chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh được chia thành hàng ngàn ngăn pin xếp nối tiếp; so sánh BÊN PHẢI với 4 ổ cắm điện 220V gia đình tóe lửa.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hôm nay, tôi sẽ kích hoạt quy trình thí nghiệm 5 cấp độ tăng dần: từ máy phát radar định vị 10V, vũ khí hack hệ thần kinh con mồi từ xa, cú nhảy dí cằm điện giật ngất ngây cá sấu 2m, cho đến bí mật vì sao nó không bị điện giật chết chính mình!". Bố cục: Bảng thang đo 5 cấp độ thử thách sáng đèn rực rỡ từ Cấp 1 đến Cấp 5; giáo sư nhà khoa học điên tóc bạc bù xù mặc áo blouse trắng, đeo găng tay cao su cách điện dày cộp màu đỏ, tay cầm vôn kế đo điện cầm chiếc cần gạt công suất chuẩn bị gạt nấc đầu tiên. KHÔNG có Lươn Điện trong cảnh này.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy siết chặt dây an toàn, chúng ta bắt đầu kích hoạt Cấp độ 1 ngay bây giờ!". Bố cục: BÊN TRÁI giáo sư nhà khoa học điên tóc bạc bù xù mặc áo blouse trắng, đeo găng tay cao su cách điện dày cộp màu đỏ, tay cầm vôn kế đo điện và cô trợ lý phòng thí nghiệm đeo kính cận tròn, tóc đuôi ngựa buộc gọn, tay cầm bảng kẹp tài liệu kiểm tra thông số thắt dây an toàn ngồi trên ghế thí nghiệm; BÊN PHẢI dòng điện từ bể nước bắt đầu phóng ra những tia lửa sáng lóa mở màn.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khởi động Cấp độ 1: Phân tích cơ chế nạp điện và hệ thống radar định vị trong bùn lầy! Hãy nhìn kỹ vào thân hình dài tới 2m và nặng 20kg của mẫu vật.". Bố cục: BÊN TRÁI tấm biển phát sáng 'CẤP ĐỘ 1: PHÂN TÍCH PIN & RADAR BÙN LẦY'; BÊN PHẢI thước đo chiều dài hiển thị 2m và chiếc cân hiển thị 20kg. KHÔNG có Lươn Điện trong cảnh này.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tất cả các cơ quan nội tạng quan trọng nhất như tim, gan, dạ dày và mang thở đều bị dồn ép lại vỏn vẹn trong 20% phần đầu phía trước! Toàn bộ phần thân dài ngoằng còn lại chính là ba". Bố cục: Sơ đồ X-quang sinh học: chỉ 20% phần đầu chứa tim, não, dạ dày nhỏ xíu được đóng khung bảo vệ; 80% còn lại là 3 cơ quan phát điện đồ sộ chiếm trọn thân thể.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cơ quan phát điện độc lập! Cơ quan phát điện chính, cơ quan Hun-tơ và cơ quan Sách!". Bố cục: Ba khối cơ quan phát điện được tô màu khác nhau: Cơ quan Chính màu đỏ cam, cơ quan Hunter màu vàng, và cơ quan Sachs màu xanh lam chạy dọc suốt thân chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bên trong ba khối cơ này chứa khoảng 5.000 đến 6.000 tế bào phát điện hình chiếc đĩa dẹp xếp chồng khít lên nhau thành hàng trăm cột dài song song.". Bố cục: Kính hiển vi phóng to hàng ngàn lần: 6.000 tế bào electrocyte hình đĩa dẹp xếp chồng ngay ngắn như cọc tiền xu pin nối tiếp nhau phát sáng điện tích âm và dương.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi tế bào này giống như một cục pin cúc áo mini, tạo ra một điện thế cực nhỏ chỉ 0,15V. Nhưng khi hàng ngàn tế bào này được thần kinh kích hoạt đồng loạt nối tiếp nhau, các điện thế cộng dồn lại tạo thành một cú sốc điện kinh thiên động địa!". Bố cục: Mô phỏng vật lý: một tế bào electrocyte đơn lẻ sinh ra 0,15V như pin đồng hồ cúc áo; mũi tên dẫn sang hàng ngàn tế bào cộng dồn điện áp tăng vọt theo cấp số nhân.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng ở chế độ bình thường, Nhà Máy Điện Sống không dại gì xả hết điện năng! Nó sử dụng cơ quan Sách ở đuôi để liên tục phát ra những xung điện áp thấp chỉ khoảng 10V với tần số 20 nhịp mỗi giây.". Bố cục: Chế độ radar sinh học: từ phần đuôi của chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh, những vòng sóng điện áp thấp 10V màu xanh dương lan tỏa đều đặn ra làn nước xung quanh như sóng radar quét vòng.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vùng nước sông Amazon đục ngầu phù sa khiến mắt của lươn điện gần như bị mù lòa. Nhưng nhờ trường điện 10V bao bọc xung quanh cơ thể, nó có thể cảm nhận mọi vật cản và con mồi bơi qua hệt như một chiếc tàu ngầm bật sóng sonar!". Bố cục: Lòng sông Amazon đục ngầu đen kịt đầy bùn lầy; đôi mắt chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh đeo kính râm mù lòa nhưng các thụ thể điện trên đầu vẫn vẽ ra bản đồ 3D xung quanh rõ mồn một.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giáo sư ơi! Màn hình radar vừa phát hiện một đàn cá nhỏ đang vùi mình dưới lớp bùn sâu 30cm! Nó làm sao bắt được chúng ạ? Câu hỏi rất hay!". Bố cục: Màn hình radar phòng thí nghiệm: các chấm xanh nhấp nháy phát hiện đàn cá nhỏ vùi sâu 30cm dưới lớp bùn; cô trợ lý phòng thí nghiệm đeo kính cận tròn, tóc đuôi ngựa buộc gọn, tay cầm bảng kẹp tài liệu kiểm tra thông số kinh ngạc tròn mắt theo dõi. KHÔNG có Lươn Điện trong cảnh này.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đã đến lúc chuyển giao diện thí nghiệm sang Cấp độ 2: Kỹ thuật hack não và thao túng cơ bắp con mồi từ xa!". Bố cục: BÊN TRÁI giáo sư nhà khoa học điên tóc bạc bù xù mặc áo blouse trắng, đeo găng tay cao su cách điện dày cộp màu đỏ, tay cầm vôn kế đo điện giơ tay chỉ lên bảng điều khiển; bảng đèn chuyển sang màu cam sáng rực báo hiệu 'CẤP ĐỘ 2: HACK NÃO TỪ XA'. KHÔNG có Lươn Điện trong cảnh này.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bước vào Cấp độ 2: Thử nghiệm vũ khí điều khiển thần kinh từ xa!". Bố cục: BÊN TRÁI tấm biển 'CẤP ĐỘ 2: VŨ KHÍ HACK NÃO CON MỒI'; BÊN PHẢI hình minh họa một bộ não cá bị các xung điện điều khiển từ xa như con rối dây. KHÔNG có Lươn Điện trong cảnh này.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 2014, nhà sinh vật học lừng danh Kenneth Catania tại Đại học Vanderbilt đã công bố một nghiên cứu chấn động trên tạp chí Science danh giá, vạch trần bí mật săn mồi đỉnh cao của Nhà Máy Điện Sống!". Bố cục: Trang bìa tạp chí khoa học danh giá Science năm 2014: giáo sư Kenneth Catania tại Đại học Vanderbilt đang tiến hành thí nghiệm xung điện kép với máy hiện sóng. KHÔNG có Lươn Điện trong cảnh này.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi nghi ngờ có con mồi đang ẩn nấp dưới đáy bùn, Lươn Điện sẽ phóng ra một cặp xung điện kép cực mạnh gồm hai cú sốc cách nhau đúng 2-3 phần nghìn giây! Cặp xung điện này không phải để giết chết con mồi, mà nó bắt chước hoàn hảo tín hiệu điều khiển vận động của não bộ!". Bố cục: chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh phóng ra hai xung điện chớp nhoáng (doublets) cách nhau chỉ 2 mili-giây; các tia sóng điện màu tím xuyên thẳng xuống lớp bùn chạm vào đàn cá đang trốn.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tín hiệu này xâm nhập thẳng vào hệ thần kinh của con cá đang nấp, ép toàn bộ các bó cơ trên cơ thể con mồi phải co giật kịch liệt ngoài ý muốn!". Bố cục: Mô phỏng 3D hệ thần kinh: tín hiệu xung điện của lươn chạy dọc tủy sống con cá, chiếm quyền kiểm soát các bó cơ ép cơ thể co thắt dữ dội ngoài ý muốn. KHÔNG có Lươn Điện trong cảnh này.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ối giời ơi! Tự nhiên đuôi tôi nó giật bắn lên thế này! Tôi đâu có muốn bơi đâu mà cơ thể cứ giãy nảy lên văng cả bùn ra ngoài thế này cứu tôi với! Chính xác là như vậy!". Bố cục: Cận cảnh chú cá nhỏ dưới bùn: mắt trợn ngược, toàn thân giật nảy tanh tách như bị ai giật dây cót, đuôi vẫy loạn xạ làm bùn nước văng tung tóe hài hước. KHÔNG có Lươn Điện trong cảnh này.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Con cá nhỏ vừa giật bắn mình làm rung chuyển lớp bùn là vị trí ẩn nấp lập tức bị bại lộ hoàn toàn trước cảm biến của thợ săn! Và ngay trong 1/10 giây tiếp theo,". Bố cục: Vị trí con mồi phát sáng như ngọn hải đăng giữa bùn; cảm biến của chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh khóa chặt mục tiêu với tâm ngắm màu đỏ rực rỡ.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhà Máy Điện Sống lập tức tung ra đòn kết liễu tàn nhẫn: nó xả liên tiếp hàng trăm xung điện cao thế 400V với tần số 400 nhịp mỗi giây!". Bố cục: Đòn kết liễu cao thế: chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh xả ra loạt xung điện 400V với tốc độ 400 nhịp/giây; dòng điện sáng rực như sấm sét bao trùm toàn bộ đáy hồ.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn bộ cơ bắp của con mồi lập tức rơi vào trạng thái co cứng cực đại, bị đông cứng như một khúc gỗ hoàn toàn tê liệt không thể cử động hay hít thở!". Bố cục: Con cá mồi bị đông cứng đơ như một thanh gỗ hóa đá, mắt đờ đẫn không cử động được một chiếc vây; các dòng điện nhỏ vẫn chạy râm ran trên da. KHÔNG có Lươn Điện trong cảnh này.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và trước khi con mồi kịp hiểu chuyện gì vừa xảy ra, Lươn Điện há chiếc miệng rộng ngoác tạo ra một lực hút chân không cực mạnh nuốt chửng nạn nhân vào bụng chỉ trong chớp mắt!". Bố cục: chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh há toang chiếc miệng tạo ra lực xoáy hút chân không cực mạnh; con cá bị hút tọt thẳng vào miệng lươn trong một phần chớp mắt.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một cơ chế săn mồi điều khiển từ xa tinh vi đến mức các kỹ sư quân sự cũng phải ngả mũ bái phục!". Bố cục: BÊN TRÁI giáo sư nhà khoa học điên tóc bạc bù xù mặc áo blouse trắng, đeo găng tay cao su cách điện dày cộp màu đỏ, tay cầm vôn kế đo điện và cô trợ lý phòng thí nghiệm đeo kính cận tròn, tóc đuôi ngựa buộc gọn, tay cầm bảng kẹp tài liệu kiểm tra thông số đứng vỗ tay tán thưởng trước màn hình phân tích; BÊN PHẢI chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh xoa bụng no nê chớp mắt tinh nghịch.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cảnh báo mức độ nguy hiểm cực hạn! Chúng ta bước vào Cấp độ 3: Đối đầu với những kẻ săn mồi khổng lồ trên cạn và cú nhảy dí cằm huyền thoại!". Bố cục: BÊN TRÁI bảng báo động cấp 3 màu đỏ rực 'CẤP ĐỘ 3: ĐỐI ĐẦU BẠO CHÚA CÁ SẤU'; BÊN PHẢI hình vẽ cá sấu Caiman khổng lồ với hàm răng sắc nhọn. KHÔNG có Lươn Điện trong cảnh này.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hơn 200 năm trước, nhà thám hiểm vĩ đại A-lếch-xăng-đơ von Hum-bôn từng kể lại câu chuyện lươn điện phóng điện tấn công cả đàn ngựa băng qua sông, nhưng suốt hai thế kỷ giới khoa học đều nghĩ rằng ông chỉ phóng đại câu chuyện dân gian!". Bố cục: Bức tranh lịch sử thế kỷ 19: nhà thám hiểm Alexander von Humboldt đứng trên bờ sông vẽ lại cảnh đàn ngựa hí vang nhảy cẫng lên giữa dòng nước sông Nam Mỹ. KHÔNG có Lươn Điện trong cảnh này.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cho đến tận năm 2016, giáo sư Ca-ta-ni-a mới chính thức giải mã được hành vi kinh hoàng này trong phòng thí nghiệm! Trong môi trường nước sâu, dòng điện phóng ra từ cơ thể lươn sẽ bị phân tán ra mọi hướng trong nước, khiến điện áp truyền vào cơ thể kẻ địch bị suy giảm đáng kể.". Bố cục: Phòng thí nghiệm hiện đại của giáo sư Kenneth Catania: các thiết bị cảm biến ghi lại dòng điện và camera quay siêu chậm phân tích chuyển động của lươn điện. KHÔNG có Lươn Điện trong cảnh này.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng khi bị một kẻ săn mồi to xác như cá sấu Caiman, báo đốm hay con người dồn vào vùng nước nông, Nhà Máy Điện Sống sẽ tung ra tuyệt chiêu cận chiến nguy hiểm nhất!". Bố cục: So sánh môi trường: BÊN TRÁI dòng điện dưới nước sâu bị rò rỉ phân tán ra bốn phương tám hướng; BÊN PHẢI lươn điện trong nước nông đang chuẩn bị bật nhảy.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó không nằm dưới nước phóng điện, mà dùng chiếc đuôi khỏe khoắn gập mạnh, ngóc đầu phóng vọt lên khỏi mặt nước cao tới 0,5m! Nó áp sát phần cằm dẫn điện cực dương trực tiếp vào ngực hoặc cổ họng của kẻ tấn công, trong khi phần đuôi cực âm vẫn cắm chặt dưới nước!". Bố cục: Khoảnh khắc ngoạn mục: chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh uốn đuôi bật tung người phóng vọt lên khỏi mặt nước cao 0,5m; cằm dẫn điện cực dương dí sát thẳng vào ngực con cá sấu khổng lồ.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn bộ nguồn điện khủng khiếp chạy thẳng một mạch xuyên qua tim và não của kẻ săn mồi mà không hề bị tiêu hao một mi-li-vôn nào ra môi trường nước xung quanh!". Bố cục: Mạch điện kín không suy hao: đầu lươn cực dương dí vào ngực cá sấu, đuôi lươn cực âm cắm dưới nước; toàn bộ luồng sét chạy thẳng xuyên qua tim chú cá sấu Caiman Nam Mỹ dài 2m da xanh vảy sừng, biểu cảm hoảng hốt mắt xoay tròn bị giật cháy đen xù lông.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Này con lươn trơn tuột kia, nhìn tao là cá sấu chúa dài 2m đây này, liệu hồn mà nạp mạng... Á á á! Cứu tao với! Điện giật xoắn cả đuôi, tim ngừng đập rồi trời ơi!". Bố cục: Cảnh tượng bi hài: chú cá sấu chú cá sấu Caiman Nam Mỹ dài 2m da xanh vảy sừng, biểu cảm hoảng hốt mắt xoay tròn bị giật cháy đen xù lông dài 2m bị điện giật cứng đờ toàn thân, các vảy dựng đứng, mắt trợn tròn xoay vòng, khói bốc nghi ngút từ đầu.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cú nhảy dí cằm trực tiếp này tạo ra một dòng điện cực mạnh đủ sức làm tê liệt hoàn toàn hệ cơ tim của một con cá sấu dài 2m hoặc một con ngựa trưởng thành, khiến chúng ngã gục ngay tại chỗ vì sốc tim và ngạt thở!". Bố cục: Sơ đồ giải phẫu tim cá sấu bị ngừng đập tạm thời do dòng điện cao thế xuyên qua; cá sấu ngã ngửa bất tỉnh nhân sự trên bãi bùn. KHÔNG có Lươn Điện trong cảnh này.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa hết, khi gặp con mồi quá to, nó còn uốn cong cơ thể thành hình chữ U, kẹp chặt con mồi vào giữa đầu và đuôi để nhân đôi cường độ điện trường xuyên qua cơ thể nạn nhân!". Bố cục: Chiến thuật hình chữ U: chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh uốn cong người ôm trọn con mồi vào giữa đầu và đuôi; điện trường giữa hai cực nhân đôi cường độ ép chết con mồi trong gọng kìm điện.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một chiến thuật chiến đấu công thủ toàn diện đến mức rùng mình!". Bố cục: BÊN TRÁI cá sấu Caiman lủi thủi bò trốn lên bờ với chiếc đuôi còn giật giật; BÊN PHẢI chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh bơi ngạo nghễ như chúa tể đầm lầy không đối thủ.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đến đây, chắc chắn câu hỏi lớn nhất đang sôi sục trong đầu các trợ lý là: Phóng ra nguồn điện khủng khiếp như vậy, tại sao chính con Lươn Điện lại không bị giật chết lăn quay ra đấy?". Bố cục: BÊN TRÁI tấm biển 'CẤP ĐỘ 4: BÍ MẬT KHÔNG BỊ GIẬT CHẾT'; BÊN PHẢI chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh đứng khoanh tay tự tin trước tia sét với chiếc khiên bảo vệ phát sáng. KHÔNG có Lươn Điện trong cảnh này.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Câu trả lời nằm ở ba tấm lá chắn vật lý và sinh học thiên tài mà tiến hóa đã trang bị cho Nhà Máy Điện Sống!". Bố cục: Hình minh họa 3 tấm lá chắn năng lượng phát sáng xếp trước mặt chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh: lá chắn điện trở vật lý, lá chắn vị trí cơ quan, và lá chắn kích thước cơ thể.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lá chắn thứ nhất là quy luật điện trở vật lý! Cơ thể của lươn điện được bọc kín bởi một lớp da dày và các lớp mỡ dày có điện trở rất cao.". Bố cục: Sơ đồ vật lý định luật Ohm: lớp da và mỡ của lươn có điện trở cực cao R-cao; mô phỏng dòng điện gặp vật cản cách điện an toàn.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong khi đó, dòng điện luôn có xu hướng chọn con đường có điện trở thấp nhất để di chuyển. Môi trường nước sông Amazon xung quanh cơ thể nó có điện trở thấp hơn rất nhiều so với lớp mỡ bảo vệ, nên phần lớn năng lượng điện phóng ra sẽ lập tức thoát thẳng ra nước xung quanh thay vì thâm nhập ngược vào sâu trong nội tạng của lươn!". Bố cục: Đường đi của dòng điện: dòng điện chọn con đường nước sông Amazon có điện trở cực thấp, thoát ào ạt ra ngoài làn nước xung quanh mà không đi vào nội tạng lươn. KHÔNG có Lươn Điện trong cảnh này.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lá chắn thứ hai là bố cục vị trí cơ quan sinh học! Như tôi đã nhấn mạnh ở đầu buổi thí nghiệm, toàn bộ não bộ, tim và các cơ quan nội tạng nhạy cảm đều được cô lập hoàn toàn ở phần đầu, cách xa khu vực ba cơ quan phát điện ở thân sau và được bao bọc bởi các lớp mô liên kết cách điện kiên cố!". Bố cục: Bản đồ phân vùng an toàn sinh học: phần đầu chứa não và tim được bọc trong kén cách điện chuyên dụng; cách xa khu vực 3 cơ quan phát điện ở thân sau.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dòng điện đi từ đầu tới đuôi nhưng chỉ lướt qua bề mặt ngoài cơ thể!". Bố cục: Dòng điện cao thế chạy từ cực dương ở đầu tới cực âm ở đuôi nhưng chỉ lướt trên bề mặt mô cơ ngoài; nội tạng bên trong hoàn toàn bình an vô sự.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và lá chắn thứ ba là yếu tố kích thước! Lươn Điện trưởng thành dài tới hơn 2m, nên mật độ dòng điện đi qua từng thớ cơ của nó bị pha loãng ra nhiều lần,". Bố cục: So sánh kích thước: thân hình lươn dài 2m làm loãng mật độ điện trường; các thớ cơ của lươn chỉ chịu một phần rất nhỏ dòng điện.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "trong khi những con cá nhỏ hay con mồi bị nó dí sát thì phải hứng trọn mật độ điện trường dày đặc chí mạng! Nhưng Nhà Máy Điện Sống bất khả chiến bại này lại có một điểm yếu chết người cực kỳ bi hài!". Bố cục: Con cá nhỏ đối diện hứng trọn mật độ điện dày đặc hàng chục nghìn vôn/m2; cơ thể cá nhỏ sáng rực lên vì điện trường tập trung cực cao. KHÔNG có Lươn Điện trong cảnh này.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "80% lượng oxy của lươn điện được hấp thụ qua các mao mạch trong miệng chứ mang của nó gần như bị thoái hóa hoàn toàn!". Bố cục: Điểm yếu chết người: khoang miệng chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh chứa đầy mao mạch đỏ rực hấp thụ 80% oxy không khí; mang cá teo nhỏ không thể thở trong nước.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cứ mười đến 15 phút một lần, nó bắt buộc phải ngoi đầu lên mặt nước để hít thở không khí.". Bố cục: chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh thò đầu lên khỏi mặt nước hít một hơi không khí sảng khoái; đồng hồ đếm ngược 10-15 phút báo hiệu chu kỳ ngoi lên mặt nước bắt buộc.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu bạn giữ chặt con lươn này dưới nước không cho nó ngoi lên, một sát thủ điện giật ngất cá sấu sẽ... chết đuối y như con người! Một nghịch lý sinh học quá đỗi thú vị!". Bố cục: Nghịch lý bi hài: một quả tạ giữ lươn dưới nước, chú lươn điện sặc nước ho sặc sụa với bóng thoại 'Cứu tôi, tôi chết đuối mất!'; giáo sư nhà khoa học điên tóc bạc bù xù mặc áo blouse trắng, đeo găng tay cao su cách điện dày cộp màu đỏ, tay cầm vôn kế đo điện và cô trợ lý phòng thí nghiệm đeo kính cận tròn, tóc đuôi ngựa buộc gọn, tay cầm bảng kẹp tài liệu kiểm tra thông số cười nghiêng ngả.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chào mừng quý vị bước vào Cấp độ tối thượng: Kỷ lục năng lượng mới nhất của thế giới hiện đại! Suốt 200 năm ròng rã, cả thế giới đinh ninh rằng hành tinh này chỉ có duy nhất một loài lươn điện với điện áp tối đa 600V.". Bố cục: BÊN TRÁI bảng đèn sáng rực rỡ 'CẤP ĐỘ TỐI THƯỢNG: KỶ LỤC 860 VÔN'; BÊN PHẢI hình ảnh các nhà khoa học đang đo đạc nguồn điện kỷ lục trên sông Amazon. KHÔNG có Lươn Điện trong cảnh này.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng vào năm 2019, nhóm nghiên cứu của tiến sĩ de Santana tại Viện Smithsonian đã phát hiện ra loài lươn điện mới mang tên Electrophorus voltai!". Bố cục: Bài báo khoa học Nature Communications năm 2019 của tiến sĩ de Santana tại Viện Smithsonian, công bố phát hiện loài lươn điện mới Electrophorus voltai. KHÔNG có Lươn Điện trong cảnh này.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi gắn thiết bị đo vào mẫu vật voltai này, chiếc kim đồng hồ đã vọt lên con số kỷ lục 860V! Đây chính là sinh vật phóng điện mạnh nhất từng được ghi nhận trong lịch sử Trái Đất, biến những dòng sông hoang dã Nam Mỹ trở thành những trạm biến áp tự nhiên kỳ vĩ bậc nhất hành tinh!". Bố cục: Cận cảnh chiếc vôn kế đo điện tử hiện số 860V màu vàng rực; chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh loài Electrophorus voltai tỏa ra các luồng sét cực quang tuyệt đẹp khắp bể nước.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tiến hóa không chỉ tạo ra sự sống, mà còn tạo ra những kỳ quan công nghệ sinh học đi trước con người hàng trăm triệu năm!". Bố cục: Bức tranh hoang dã sông rừng Amazon: lươn điện bơi lượn như vị thần sấm sét dưới làn nước, biểu tượng cho kỳ quan công nghệ sinh học vĩ đại của tự nhiên.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo giáo sư! Toàn bộ dữ liệu thử nghiệm của mẫu vật Lươn Điện đã được lưu trữ thành công vào hệ thống! Nhưng trên radar quét tầm xa, phòng thí nghiệm vừa bắt được tín hiệu của một quái kiệt tí hon cực kỳ nguy hiểm cho Tập 18!". Bố cục: cô trợ lý phòng thí nghiệm đeo kính cận tròn, tóc đuôi ngựa buộc gọn, tay cầm bảng kẹp tài liệu kiểm tra thông số bấm nút lưu trữ dữ liệu; màn hình radar góc phòng thí nghiệm đột nhiên phát tín hiệu cảnh báo nhấp nháy màu đỏ tía dữ dội. KHÔNG có Lươn Điện trong cảnh này.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyệt vời lắm cô trợ lý! Xin mời toàn thể các nhà nghiên cứu hãy hướng mắt lên màn hình lớn trung tâm để giải mã BÓNG ĐEN BÍ ẨN của nhân vật xuất hiện trong Tập 18 tiếp theo!". Bố cục: Ánh đèn phòng thí nghiệm dịu xuống; chiếc màn hình chiếu khổng lồ ở trung tâm bật sáng với ánh hào quang màu cam lửa rực cháy kịch tính. KHÔNG có Lươn Điện trong cảnh này.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Xin gửi tới các bạn ba manh mối khoa học chấn động về bóng đen bí ẩn này: Thứ nhất, đây là siêu pháo thủ tí hon sở hữu khẩu súng hóa học liên thanh nã đạn 500 lần/giây ở nhiệt độ sôi sùng sục 100°C làm bỏng rát mọi kẻ thù!". Bố cục: Manh mối số 1: BÓNG ĐEN BÍ ẨN của một chú bọ cánh cứng tí hon đang nã pháo liên thanh 500 phát/giây ở 100°C kèm dấu hỏi chấm '?' màu đỏ phát sáng. KHÔNG có Lươn Điện trong cảnh này.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thứ hai, phản ứng hóa học hai buồng đốt chết người: buồng chứa nhiên liệu và buồng kích nổ áp suất cực cao!". Bố cục: Manh mối số 2: Sơ đồ cấu tạo hệ thống 2 buồng đốt áp suất cực cao bên trong cơ thể bọ cánh cứng đẩy lùi kẻ thù. KHÔNG có Lươn Điện trong cảnh này.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và thứ ba, kỷ lục thoát chết kinh dị bậc nhất: bị cóc nuốt chửng vào bụng suốt 1 tiếng đồng hồ, nó nã pháo xả độc ngay trong bao tử khiến cóc buồn nôn nôn thốc nôn tháo nguyên con ra ngoài vẫn sống nhăn nhở!". Bố cục: Manh mối số 3: Một con cóc khổng lồ ôm bụng nôn thốc nôn tháo; BÓNG ĐEN BÍ ẨN chui từ miệng cóc ra ngoài sau 1 tiếng vẫn sống nhăn nhở giơ hai càng ăn mừng. KHÔNG có Lươn Điện trong cảnh này.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các trợ lý khoa học có đoán ra bóng đen pháo thủ tí hon này là sinh vật nào không? Hãy để lại kết quả phân tích và dự đoán của bạn ngay dưới phần bình luận nhé!". Bố cục: BÓNG ĐEN BÍ ẨN đứng sừng sững giữa màn hình với dấu hỏi chấm '?' khổng lồ; xung quanh là các bong bóng bình luận '? ? ?' kêu gọi khán giả dự đoán. KHÔNG có Lươn Điện trong cảnh này.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giáo sư phòng thí nghiệm xin chào tạm biệt và hẹn gặp lại các bạn trong cuộc thử nghiệm kỳ thú tiếp theo!". Bố cục: BÊN TRÁI giáo sư nhà khoa học điên tóc bạc bù xù mặc áo blouse trắng, đeo găng tay cao su cách điện dày cộp màu đỏ, tay cầm vôn kế đo điện và cô trợ lý phòng thí nghiệm đeo kính cận tròn, tóc đuôi ngựa buộc gọn, tay cầm bảng kẹp tài liệu kiểm tra thông số vẫy tay chào tạm biệt; BÊN PHẢI tấm biển gỗ đề chữ 'HẸN GẶP LẠI Ở TẬP 18 VỚI SIÊU PHÁO THỦ TÍ HON!'. KHÔNG có Lươn Điện trong cảnh này.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Trợ lý, tăng điện áp lên mức tối đa!". Bố cục: KHUNG HÌNH DỌC 9:16: giáo sư nhà khoa học điên tóc bạc bù xù mặc áo blouse trắng, đeo găng tay cao su cách điện dày cộp màu đỏ, tay cầm vôn kế đo điện đeo kính bảo hộ giơ cần gạt công suất, dòng chữ lớn 'TRỢ LÝ, TĂNG ĐIỆN ÁP TỐI ĐA!' xuất hiện rực rỡ phía trên.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Một sinh vật có thể phóng ra dòng điện 860V giật ngất ngây cả cá sấu 2m,". Bố cục: KHUNG HÌNH DỌC 9:16: Dòng điện 860V màu xanh neon nổ lách tách chói lòa trong hồ nước, con cá sấu Caiman 2m bên cạnh bị giật cứng đơ người.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "nhưng tại sao chính nó lại không bị giật chết lăn quay?". Bố cục: KHUNG HÌNH DỌC 9:16: Chú Lươn Điện bơi ung dung bình an vô sự trong vầng hào quang điện, đôi mắt tròn xoe ngây thơ chớp chớp.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đó chính là Lươn Điện, nhà máy điện sống khét tiếng của rừng rậm Nam Mỹ.". Bố cục: KHUNG HÌNH DỌC 9:16: Chân dung chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh uốn lượn uy dũng giữa dòng nước Amazon, cơ thể tỏa ra các tia sét màu vàng và xanh neon tuyệt đẹp.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Hơn 80% cơ thể của nó là 6.000 tế bào pin sinh học nối tiếp nhau,". Bố cục: KHUNG HÌNH DỌC 9:16: Sơ đồ cơ thể chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh: 80% thân chứa 6.000 tế bào pin sinh học electrocyte nối tiếp nhau phát sáng rực rỡ.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "tích tụ điện thế mạnh gấp 4 lần ổ cắm điện gia đình!". Bố cục: KHUNG HÌNH DỌC 9:16: So sánh điện áp: cột điện thế của lươn vọt cao gấp 4 lần ổ cắm điện gia đình 220V đang tóe lửa.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Khi săn mồi, nó phóng xung điện kép hack thẳng vào hệ thần kinh ép cơ bắp con mồi co giật làm lộ vị trí,". Bố cục: KHUNG HÌNH DỌC 9:16: Xung điện kép phóng ra từ chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh chạm vào con cá nhỏ dưới bùn, ép toàn bộ cơ bắp con cá giật nảy phát lộ vị trí.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "rồi tung cú nhảy dí cằm trực tiếp truyền trọn nguồn điện cực mạnh vào tim kẻ thù!". Bố cục: KHUNG HÌNH DỌC 9:16: chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh phóng vọt lên khỏi mặt nước dí cằm trực tiếp vào ngực kẻ thù; luồng sét chạy thẳng xuyên qua tim không bị phân tán.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Nhưng sở dĩ nó không bị giật chết là nhờ lớp mỡ cách điện dày cộp, toàn bộ nội tạng dồn hết lên đầu,". Bố cục: KHUNG HÌNH DỌC 9:16: Sơ đồ giải phẫu cắt ngang: lớp mỡ dày cách điện bảo vệ nội tạng, não và tim dồn hết lên đầu an toàn tuyệt đối.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "và dòng điện luôn chọn thoát ra môi trường nước có điện trở thấp hơn!". Bố cục: KHUNG HÌNH DỌC 9:16: Dòng điện chọn thoát thẳng ra nước có điện trở thấp hơn thay vì đi vào cơ thể lươn, tạo thành vầng hào quang điện rực rỡ.
```
</details>

<details><summary>S11</summary>

```text
HÌNH S11 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Vậy là bí mật đã sáng tỏ: một tuyệt tác thiết kế của tự nhiên,". Bố cục: KHUNG HÌNH DỌC 9:16: chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh bơi kiêu hãnh giữa dòng nước sông Amazon rạng rỡ ánh bình minh, biểu tượng cho vũ khí sinh học hoàn hảo của tự nhiên.
```
</details>

<details><summary>S12</summary>

```text
HÌNH S12 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "biến thịt da thành vũ khí sốc điện tối thượng mà không hề tự thiêu rụi chính mình!". Bố cục: KHUNG HÌNH DỌC 9:16: Toàn cảnh dòng sông rừng Amazon tuyệt đẹp lúc rạng đông, Lươn Điện lướt sóng uy nghi khép lại câu chuyện trọn vẹn.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/61 của video YouTube về Lươn Điện). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/12 của video YouTube Shorts về Lươn Điện). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh. 
```
</details>

## 7. SEO

- **title:** Tại Sao Lươn Điện 860V Giật Ngất Cá Sấu Mà Không Bị Giật Chết?! | Lươn Điện | Tập 17
- **hook_paragraph:** Lươn Điện phóng dòng điện kỷ lục 860V mạnh gấp 4 lần điện gia đình, hack hệ thần kinh con mồi từ xa và dí cằm giật ngất cá sấu 2m! Nhưng tại sao chính nó không bị điện giật chết? Khám phá phòng thí nghiệm 5 cấp độ sinh học của Nhà Máy Điện Sống.
- **question:** Bạn có đoán ra BÓNG ĐEN BÍ ẨN ở cuối video là sinh vật nào không? (Gợi ý: Pháo thủ nã đạn 500 lần/giây ở 100°C, bị cóc nuốt 1 tiếng vẫn nã độc thoát ra). Bình luận dự đoán nhé!
- **next_teaser:** Bóng đen bí ẩn — siêu pháo thủ nã đạn 500 lần/giây ở 100°C bị cóc nuốt vẫn thoát thân
- **shorts_title:** Tại Sao Lươn Điện 860V Giật Cá Sấu Mà Không Tự Giật Chết?! ⚡ #shorts #luondien
- **shorts_desc:** Lươn Điện phóng ra 860V giật ngất cá sấu 2 mét nhưng tại sao chính nó không bị điện giật chết? Khám phá tuyệt tác cách điện sinh học của Nhà Máy Điện Sống! ⚡🔋
- **bullets:** Nguồn điện kỷ lục 860V từ 6.000 tế bào pin sinh học nối tiếp · Vũ khí hack thần kinh: Xung điện kép ép cơ bắp con mồi co giật lộ vị trí · Cú nhảy dí cằm huyền thoại giật ngất cá sấu Caiman và ngựa trưởng thành · Bí mật lớp mỡ cách điện sinh học và nghịch lý 80% thở bằng miệng
- **tags:** lươn điện, luon dien, electric eel, tại sao lươn điện không bị giật, lươn điện giật cá sấu, lươn điện 860v, thế giới động vật, động vật kỳ lạ, vẽ chuyện hoang dã, whiteboard animation, khoa học thú vị, phòng thí nghiệm động vật
- **hashtags:** #LuonDien #ElectricEel #TheGioiDongVat #VeChuyenHoangDa #KhoaHoc

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-17-luon-dien
python src/episode/pipeline.py tts    projects/tap-17-luon-dien     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-17-luon-dien     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-17-luon-dien     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-17-luon-dien              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-17-luon-dien --force
python scripts/beat_sheet.py projects/tap-17-luon-dien               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-17-luon-dien/audio/shorts.wav projects/tap-17-luon-dien/renders/tap-17-luon-dien_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-17-luon-dien
python src/episode/pipeline.py seo    projects/tap-17-luon-dien
python src/episode/episode_doc.py     projects/tap-17-luon-dien
```

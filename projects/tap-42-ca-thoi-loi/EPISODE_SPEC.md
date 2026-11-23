# TẬP 42 — CÁ THÒI LÒI · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-42-ca-thoi-loi`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-42-ca-thoi-loi`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F1` · **Persona giọng:** `bac_si` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Cá Thòi Lòi |
| Tiêu đề YouTube | Cá Thòi Lòi: Con Cá Chết Đuối Dưới Nước & Bí Thuật Thụt Mắt Nuốt Mồi \| Tập 42 |
| Video dài | `renders/tap-42-ca-thoi-loi_long.mp4` — 8:48.3 (528.3s) |
| Shorts | `renders/tap-42-ca-thoi-loi_shorts.mp4` — 0:42.4 (42.4s) |
| Thumbnail | `renders/tap-42-ca-thoi-loi_thumbnail.jpg` |
| Số hình | dài 62 beat / 62 ảnh riêng; Shorts 8 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.12**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/57 của video YouTube về Cá Thòi Lòi). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C). Nhân vật phụ cố định: bác sĩ cú mèo đeo kính lão, mặc áo blouse trắng cầm ống nghe và bảng chẩn đoán; cô y tá thỏ trắng tai cụp đeo mũ chữ thập đỏ; chú còng gió nhỏ giơ hai càng cười nhe răng. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — CON CÁ CHÁN BIỂN LÊN CẠN LEO TRÈO
*Thẻ chương:* CÁ BIỂN LÊN BỜ ĐI DẠO VÀ LEO CÂY NHƯ VƯỢN

*Badge:* `BỆNH ÁN #01` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene01_p0.wav` (395 ký tự) · mood `tram_bi_an`

```text
Mời bệnh nhân tiếp theo bước vào phòng khám đa khoa tiến hóa sinh vật! Y tá đâu, chuẩn bị cho tôi một chiếc chậu bùn lầy và cặp kính hiển vi đo nhãn cầu khẩn cấp! [surprise-oh] Bệnh nhân hôm nay của chúng ta là một ca bệnh tâm lý và giải phẫu kỳ dị bậc nhất trong lịch sử y khoa động vật: Một sinh vật thuộc lớp cá mang vây đàng hoàng, nhưng lại mắc chứng sợ nước và chán ghét đại dương sâu sắc!
```
**Part 1** → `audio/vs/scene01_p1.wav` (421 ký tự) · mood `hao_hung`

```text
Bệnh nhân mang mã số bốn mươi hai của chúng ta có tên trong sổ khám bệnh là Cá Thòi Lòi, hay còn gọi là cá bống biển nhiệt đới Pe-ri-oph-thal-mus! [surprise-wa] Tôi thường gọi thân mật ca bệnh khó đỡ này là: Bệnh nhân chán biển! Trong khi hàng triệu loài cá khác ngày đêm hoảng loạn vùng vẫy tìm đường trở về với nước ngọt hay đại dương bao la, thì bệnh nhân này lại thích trèo lên bãi bùn lội bộ phơi nắng suốt ngày đêm!
```
**Part 2** → `audio/vs/scene01_p2.wav` (374 ký tự) · mood `don_dap`

```text
Chiều dài cơ thể của bệnh nhân dao động từ mười lăm đến hai mươi xăng-ti-mét, với lớp da nhớt nhầy nhụa màu nâu xám lốm đốm bùn đất. [surprise-oh] Nhưng nhìn vào hai mắt của gã mà xem: Hai nhãn cầu lồi to tướng nằm chễm chệ ngay trên đỉnh sọ đầu, có thể xoay độc lập ba trăm sáu mươi độ như hai kính tiềm vọng tàu ngầm, liên tục liếc ngang liếc dọc dò xét khắp bãi ngập mặn!
```
**Part 3** → `audio/vs/scene01_p3.wav` (114 ký tự) · 🎭 cameo `co_tro_ly`

```text
Bác sĩ ơi, con cá này nó nhảy tưng tưng lên tận ngọn rễ cây đước rồi thò đầu dòm vào cửa sổ phòng khám kìa bác ơi!
```
**Part 4** → `audio/vs/scene01_p4.wav` (378 ký tự) · mood `hao_hung`

```text
[laughter] Đúng như cô trợ lý vừa la toáng lên! Bệnh nhân chán biển không những đi bộ trên mặt bùn, mà còn dùng hai chiếc vây ngực leo thoăn thoắt lên rễ cây ngập mặn ngồi ngắm hoàng hôn chẳng khác nào một chú vượn con! Hôm nay, hồ sơ bệnh án của chúng ta sẽ phẫu thuật từng triệu chứng kỳ quặc để xem tại sao tạo hóa lại nặn ra một con cá dở dở ương ương kỳ thú đến nhường này!
```

### scene02 — NGHỊCH LÝ CON CÁ CÓ THỂ CHẾT ĐUỐI DƯỚI NƯỚC
*Thẻ chương:* BỊ ÉP Ở DƯỚI NƯỚC SẼ BỊ NGẠT THỞ CHẾT ĐUỐI

*Badge:* `BỆNH ÁN #02` · *mood mặc định:* `nghiem_trang_gia`

**Part 0** → `audio/vs/scene02_p0.wav` (416 ký tự) · mood `nghiem_trang_gia`

```text
Triệu chứng chẩn đoán số hai sẽ khiến toàn thể giới sinh học đại dương phải dụi mắt hoài nghi! [surprise-oh] Nếu bạn bắt một con cá chép hay cá hồi thả xuống nước, chúng sẽ bơi lội tung tăng như gặp lại thiên đường. Nhưng nếu bạn nhốt một con Cá Thòi Lòi vào một lồng lưới kín chìm sâu dưới đáy nước tù đọng và không cho gã ngoi lên cạn, thì điều gì sẽ xảy ra? Gã sẽ ngạt thở và chết đuối như một con người thực thụ!
```
**Part 1** → `audio/vs/scene02_p1.wav` (319 ký tự) · mood `tram_bi_an`

```text
Nguyên nhân y khoa nằm ở cấu tạo hệ hô hấp đã bị thoái hóa mang trầm trọng của Bệnh nhân chán biển! [surprise-wa] Trong quá trình tiến hóa hơn ba trăm triệu năm, các lá mang dưới nước của gã đã teo nhỏ và dính chặt vào nhau, không còn đủ diện tích tiếp xúc để lọc đủ oxy hòa tan trong nước như các loài cá thông thường.
```
**Part 2** → `audio/vs/scene02_p2.wav` (316 ký tự) · mood `don_dap`

```text
Để sinh tồn trên cạn, gã đã phát triển một công nghệ hô hấp lưỡng cư thần sầu: Lớp da nhầy của gã chứa mạng lưới mao mạch máu dày đặc, kết hợp với niêm mạc ẩm ướt trong vòm họng. [surprise-oh] Toàn bộ bề mặt da và cổ họng của gã hấp thụ trực tiếp từ năm mươi đến sáu mươi phần trăm lượng oxy từ không khí ngoài trời!
```
**Part 3** → `audio/vs/scene02_p3.wav` (86 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Ủa bác sĩ ơi, thế lúc gã leo lên bờ cát khô queo thì hai cái mang cá dùng để làm gì ạ?
```
**Part 4** → `audio/vs/scene02_p4.wav` (396 ký tự) · mood `hao_hung`

```text
[laughter] Chú cá con hỏi câu hỏi trúng ngay điểm mười sinh học! Hai nắp mang phồng to của Cá Thòi Lòi không dùng để thở nước, mà dùng làm hai chiếc bình giữ nước di động! Trước khi trèo lên cạn, gã hớp một ngụm nước thật đầy nhốt chặt trong khoang mang đóng kín bưng. Lượng nước dự trữ này liên tục làm ẩm các sợi mang mỏng manh, giúp gã lang thang trên bờ hàng giờ liền mà không sợ bị khô mang!
```
**Part 5** → `audio/vs/scene02_p5.wav` (296 ký tự) · mood `nghiem_trang_gia`

```text
Thậm chí trong khoang miệng của gã, hệ thống van niêm mạc hoạt động như một nắp van cao su chống trào ngược. Bất kể gã lộn nhào hay nhảy cao trên bùn lầy, ngụm nước quý giá trong má vẫn không hề bị rỉ ra ngoài một giọt! [surprise-wa] Một công nghệ khóa kín nước dã ngoại đỉnh cao của thế giới cá!
```
**Part 6** → `audio/vs/scene02_p6.wav` (408 ký tự) · mood `hao_hung`

```text
Đặc biệt hơn nữa, chiếc đuôi của bệnh nhân này còn có khả năng hô hấp phụ trợ vô cùng độc đáo! Khi ngồi phơi nắng trên rễ cây, gã thường thả lỏng chóp đuôi nhúng ngập trong vũng nước bên dưới. Lớp biểu bì đuôi siêu mỏng có thể trao đổi khí liên tục, vừa làm mát cơ thể vừa bơm thêm dưỡng khí cho máu! [surprise-wa] Một sự thích nghi lưỡng thê hoàn hảo đến mức khiến các loài bò sát cũng phải ngả mũ bái phục!
```

### scene03 — TUYỆT KỸ CHỚP MẮT TỤT XUỐNG HỌNG ĐỂ NUỐT MỒI
*Thẻ chương:* DÙNG NHÃN CẦU MẮT LÀM PIT-TÔNG ĐẨY THỨC ĂN

*Badge:* `BỆNH ÁN #03` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene03_p0.wav` (301 ký tự) · mood `tram_bi_an`

```text
Bây giờ, hãy đeo kính lúp phóng đại để kiểm tra vùng mặt kỳ dị nhất hành tinh của Bệnh nhân chán biển! [surprise-oh] Cá thông thường sinh ra vốn dĩ không có mí mắt, và mắt của chúng nằm cố định hai bên má. Nhưng Cá Thòi Lòi lại sở hữu đôi mắt lồi nhô cao hẳn lên đỉnh đầu như hai quả bóng bàn đồ chơi!
```
**Part 1** → `audio/vs/scene03_p1.wav` (283 ký tự) · mood `don_dap`

```text
Vì sống trên cạn giữa cái nắng gay gắt ba mươi lăm đến bốn mươi độ C của rừng ngập mặn nhiệt đới, đôi mắt của gã đối mặt với nguy cơ bị khô giác mạc và mù lòa bất cứ lúc nào. Nhưng gã không hề có tuyến nước mắt! [surprise-wa] Vậy gã giải quyết bài toán chống khô mắt này như thế nào?
```
**Part 2** → `audio/vs/scene03_p2.wav` (290 ký tự) · mood `hao_hung`

```text
Gã co rút cơ mặt, kéo tụt cả hai nhãn cầu mắt lặn sâu xuống bên trong hốc đầu! Phía dưới đáy hốc mắt có một chiếc túi chứa nước dịch ẩm ướt. Mỗi khi gã thụt mắt xuống, nhãn cầu được nhúng ngập trong bể nước làm ẩm tức thì, rồi lại ngoi bật lên sáng long lanh như vừa được tra thuốc nhỏ mắt!
```
**Part 3** → `audio/vs/scene03_p3.wav` (342 ký tự) · mood `nghiem_trang_gia`

```text
Nhưng phát hiện chấn động vừa được nhóm nghiên cứu của tiến sĩ Michel công bố trên Tạp chí Sinh học Thực nghiệm: Cú thụt mắt này còn kiêm luôn chức năng nuốt thức ăn! [surprise-oh] Vì sống trên cạn nên Cá Thòi Lòi không thể dùng dòng nước xoáy để cuốn mồi vào bụng như cá dưới biển, và lưỡi của gã cũng không có cơ bắp linh hoạt như ếch nhái.
```
**Part 4** → `audio/vs/scene03_p4.wav` (362 ký tự) · mood `hao_hung`

```text
Mỗi khi đớp được một chú còng gió hay bọ gậy trên bùn, gã đồng thời thụt mạnh cả hai nhãn cầu mắt thụt sâu xuống vòm miệng! [surprise-wa] Đáy nhãn cầu đóng vai trò như một chiếc pit-tông cơ khí ép chặt xuống khoang họng, đẩy phăng con mồi trôi tuột xuống thực quản! Nghĩa là trên đời này, chỉ có duy nhất loài cá thòi lòi là nuốt mồi bằng chính đôi mắt của mình!
```
**Part 5** → `audio/vs/scene03_p5.wav` (301 ký tự) · mood `don_dap`

```text
Chưa dừng lại ở đó, đôi mắt lồi này còn là hệ thống radar cảnh giới ba trăm sáu mươi độ hoàn hảo! Một mắt có thể nhìn chăm chú xuống bùn để rình mồi, trong khi mắt kia ngước ngược lên trời để canh chừng chim bói cá săn mồi. Bất kỳ kẻ thù nào lọt vào bán kính ba mét đều bị gã phát hiện trong tích tắc!
```

### scene04 — ĐÔI VÂY NGỰC BIẾN TÍNH THÀNH HAI CÁNH TAY LEO TRÈO
*Thẻ chương:* VÂY NGỰC CÓ KHỚP KHUỶU TAY NHƯ ĐỘNG VẬT BỐN CHÂN

*Badge:* `BỆNH ÁN #04` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene04_p0.wav` (338 ký tự) · mood `hao_hung`

```text
Hãy chuyển sang kiểm tra hệ cơ xương vận động của bệnh nhân số bốn mươi hai! [surprise-oh] Nếu bạn quan sát kỹ cặp vây ngực của Cá Thòi Lòi, bạn sẽ kinh ngạc nhận ra đây hoàn toàn không phải là những nan vây quạt nước mỏng manh của loài cá biển. Cấu trúc xương bên trong đã tiến hóa thành các khớp xương khuỷu tay và cơ bắp bám chắc chắn!
```
**Part 1** → `audio/vs/scene04_p1.wav` (366 ký tự) · mood `don_dap`

```text
Cặp vây ngực này có thể xoay gập linh hoạt, cho phép Bệnh nhân chán biển chống hai tay xuống bùn rồi đẩy toàn bộ trọng lượng cơ thể tiến về phía trước theo nhịp điệu nhịp nhàng như một anh lính bò trườn! [surprise-wa] Dưới bụng của gã còn có một chiếc đĩa hút hình thành từ hai vây bụng dính liền nhau, tạo lực bám dính chắc nịch trên những thân cây đước trơn trượt!
```
**Part 2** → `audio/vs/scene04_p2.wav` (89 ký tự) · 🎭 cameo `be_con`

```text
Bác sĩ ơi, em thấy nó co đuôi một phát là bay vèo qua mặt em xa tít mù tắp luôn á bác sĩ!
```
**Part 3** → `audio/vs/scene04_p3.wav` (336 ký tự) · mood `hao_hung`

```text
[laughter] Bé con vừa chứng kiến tuyệt kỹ búng đuôi thần sầu của gã đấy! Khi cần tẩu thoát khỏi chim bói cá hay kỳ đà đói khát, Cá Thòi Lòi gập cong chiếc đuôi cơ bắp hình chữ C rồi bung mạnh như một chiếc lò xo thép! Cú phóng này hất tung gã bay xa gấp bốn lần chiều dài cơ thể, tương đương cú nhảy xa gần một mét trên mặt bùn lầy lội!
```
**Part 4** → `audio/vs/scene04_p4.wav` (345 ký tự) · mood `don_dap`

```text
Vào mùa giao phối, tuyệt kỹ nhảy xa này biến thành màn biểu diễn võ thuật đường phố đỉnh cao! Các chàng cá thòi lòi dựng đứng vây lưng sặc sỡ như những lá cờ chiến, há to miệng thị uy rồi bật nhảy liên tục trên không trung để tranh giành lãnh thổ và thu hút các nàng cá mái. Kẻ nào nhảy cao hơn và có vây lưng lòe loẹt hơn sẽ làm bá chủ bãi lầy!
```
**Part 5** → `audio/vs/scene04_p5.wav` (283 ký tự) · mood `am_ap`

```text
Một con cá dài hai mươi xăng-ti-mét nhưng vừa biết chạy bộ, vừa biết leo cây, vừa biết nhảy xa bay trên không trung! [surprise-oh] Nếu đem so tỷ lệ cơ thể với các vận động viên điền kinh Olympic, thành tích bay nhảy của bệnh nhân này đủ sức giật huy chương vàng môn nhảy xa phối hợp!
```

### scene05 — CÔNG TRÌNH HANG BÙN HÌNH CHỮ Y VÀ TÚI KHÍ NUÔI CON
*Thẻ chương:* ĐÀO HANG SÂU 2 MÉT VÀ NỞ TRỨNG TRONG TÚI KHÍ NGẦM

*Badge:* `BỆNH ÁN #05` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene05_p0.wav` (355 ký tự) · mood `tram_bi_an`

```text
Chẩn đoán bệnh án cuối cùng dẫn chúng ta xuống lòng đất ngầm của bãi lầy ngập mặn! [surprise-oh] Khi mùa sinh sản đến, Bệnh nhân chán biển không hề đẻ trứng trôi nổi vô trách nhiệm trên mặt nước để làm mồi cho cá lớn. Gã dùng chính chiếc miệng của mình cạp từng búng bùn đất ngậm nhổ ra ngoài để đào một công trình địa đạo ngầm hình chữ Y sâu tới hai mét!
```
**Part 1** → `audio/vs/scene05_p1.wav` (301 ký tự) · mood `nghiem_trang_gia`

```text
Để miệng hang không bị sạt lở khi thủy triều dâng lên, gã còn khéo léo đắp những ụ bùn tròn xung quanh miệng hang như những tháp canh pháo đài mini. Đáy hang ngập ngụa trong nước bùn yếm khí hoàn toàn không có một phân tử oxy nào hòa tan. Nếu trứng cá đẻ ở đây, trứng sẽ thối rữa và chết ngạt tức thì.
```
**Part 2** → `audio/vs/scene05_p2.wav` (292 ký tự) · mood `don_dap`

```text
Nhưng chú cá thòi lòi bố đã giải quyết thảm họa này bằng một kỳ tích kỹ thuật ngầm khiến các nhà khoa học Nhật Bản phải kinh ngạc! [surprise-oh] Gã bơi lên mặt cạn, há to miệng đớp một búng không khí căng tràn rồi lặn ngược xuống đáy hang sâu hai mét nhả vào một căn phòng phụ trên trần hang!
```
**Part 3** → `audio/vs/scene05_p3.wav` (413 ký tự) · mood `am_ap`

```text
Gã miệt mài thực hiện hàng trăm chuyến bơi con thoi ngậm không khí như một chú thợ lặn cần mẫn, cho đến khi tạo ra một chiếc túi khí ngầm lơ lửng dưới lòng bùn! [surprise-wa] Nàng cá mẹ dán hàng ngàn quả trứng lên trần phòng túi khí khô ráo giàu dưỡng khí này. Suốt nhiều tuần lễ ấp trứng, cá bố liên tục thay phiên tuần tra canh giữ cửa hang và lặn xuống thay mới túi khí, cho đến khi đàn cá con nở ra khỏe mạnh!
```

### scene06 — DỞ DANG NHƯNG LÀ BƯỚC CHUYỂN MÌNH LỊCH SỬ
*Thẻ chương:* BÀI HỌC CUỘC SỐNG VÀ THÁCH THỨC ĐOÁN TẬP 43

*Badge:* `BẢN TỔNG KẾT` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (336 ký tự) · mood `am_ap`

```text
Hồ sơ bệnh án số bốn mươi hai chính thức hoàn tất với kết luận chẩn đoán: Cá Thòi Lòi hoàn toàn khỏe mạnh và là một tuyệt tác chuyển giao sinh học vĩ đại! Gã là hình bóng sống động của tổ tiên bốn chân xa xưa cách đây ba trăm triệu năm, những sinh vật dũng cảm đầu tiên dám thò đầu ra khỏi biển cả tăm tối để chinh phục lục địa khô cằn!
```
**Part 1** → `audio/vs/scene06_p1.wav` (335 ký tự) · mood `hao_hung`

```text
Đôi khi trong cuộc sống, bạn có thể bị người đời chê cười là kẻ dở dở ương ương, không giống ai và không thuộc về một khuôn mẫu nào: [laughter] Nhưng hãy nhớ tới chú cá thòi lòi! Chính sự khác biệt nửa nạc nửa mỡ, dám bơi ngược dòng quy chuẩn và mở lối đi riêng mới là khởi đầu cho những bước nhảy vọt tiến hóa vĩ đại nhất của lịch sử!
```
**Part 2** → `audio/vs/scene06_p2.wav` (215 ký tự) · mood `hao_hung`

```text
Nếu được sinh ra với một siêu năng lực kỳ lạ của cá thòi lòi, bạn muốn sở hữu đôi mắt xoay ba trăm sáu mươi độ thụt nuốt mồi hay cặp tay leo cây chạy bộ trên bùn? Hãy để lại bình luận chẩn đoán của bạn bên dưới nhé!
```
**Part 3** → `audio/vs/scene06_p3.wav` (451 ký tự) · mood `tram_bi_an`

```text
Còn bây giờ, hãy chuẩn bị tinh thần bước vào phiên tòa xét xử rùng rợn của hồ sơ số bốn mươi ba! [surprise-oh] Một kẻ sát nhân khoác tấm áo choàng ngọc bích lấp lánh, một bác sĩ phẫu thuật thần kinh tàn độc chuyên thực hiện ca châm kim vi phẫu chuẩn xác đến từng mi-li-mét vào hạch não của loài gián, tước đoạt toàn bộ ý chí tự do và biến nạn nhân thành một xác sống Zombie ngoan ngoãn tự đi vào mồ chôn! Bạn có biết sát thủ ngọc bích này là ai không?
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Bạn có tin trên đời có một con cá nếu bị ép ở dưới nước quá lâu thì sẽ bị... chết đuối? [surprise-wa] Đây là Cá Thòi Lòi, loài cá chán biển lên cạn sống rải rác khắp các cánh rừng ngập mặn! Mang của gã đã bị thoái hóa nặng, nhưng bù lại gã hô hấp trực tiếp qua da và vòm họng ẩm ướt để hấp thụ hơn năm mươi phần trăm lượng oxy ngoài trời. Để không bị khô mang, gã hớp đầy nước vào hai má phồng to như hai bình dưỡng khí di động! Chưa hết, cặp vây ngực của gã biến tính thành hai cánh tay có khớp khuỷu để chống bùn chạy bộ và leo thoăn thoắt lên rễ cây đước. Nhưng dị nhất là đôi mắt lồi trên đỉnh sọ: Mỗi khi đớp mồi trên cạn, gã co cơ kéo tụt cả hai nhãn cầu mắt xuống cổ họng để làm chiếc pit-tông ép thức ăn trôi xuống dạ dày, vừa làm ẩm mắt vừa nuốt mồi trong tích tắc!
```

**Whisper prompt:** `Cá Thòi Lòi, Bệnh nhân chán biển, Periophthalmus, rừng ngập mặn, rễ cây đước, khoang mang, thụt mắt nuốt mồi, 50-60%, 4 lần, 20cm, Bác sĩ, Ong Bắp Cày Ngọc`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| bốn mươi hai | 42 |
| Bốn mươi hai | 42 |
| bốn mươi mốt | 41 |
| Bốn mươi mốt | 41 |
| bốn mươi ba | 43 |
| Bốn mươi ba | 43 |
| Tập bốn mươi hai | Tập 42 |
| Tập bốn mươi ba | Tập 43 |
| Tập bốn mươi mốt | Tập 41 |
| số bốn mươi hai | số 42 |
| Số bốn mươi hai | Số 42 |
| mười lăm đến hai mươi xăng-ti-mét | 15-20cm |
| Mười lăm đến hai mươi xăng-ti-mét | 15-20cm |
| năm mươi đến sáu mươi phần trăm | 50-60% |
| Năm mươi đến sáu mươi phần trăm | 50-60% |
| năm mươi phần trăm | 50% |
| sáu mươi phần trăm | 60% |
| bốn lần | 4 lần |
| Bốn lần | 4 lần |
| hai mươi xăng-ti-mét | 20cm |
| Hai mươi xăng-ti-mét | 20cm |
| mười lăm xăng-ti-mét | 15cm |
| Mười lăm xăng-ti-mét | 15cm |
| mười lăm | 15 |
| ba mét | 3 mét |
| Ba mét | 3 mét |
| hai mét | 2 mét |
| Hai mét | 2 mét |
| một mét | 1 mét |
| Một mét | 1 mét |
| bốn mươi độ C | 40°C |
| Bốn mươi độ C | 40°C |
| ba mươi lăm độ C | 35°C |
| Ba mươi lăm độ C | 35°C |
| ba trăm sáu mươi độ | 360° |
| Ba trăm sáu mươi độ | 360° |
| hàng triệu năm | hàng triệu năm |
| triệu năm | triệu năm |
| ba trăm triệu năm | 300 triệu năm |
| Pe-ri-oph-thal-mus | Periophthalmus |
| hai mươi | 20 |
| ba mươi | 30 |
| bốn mươi | 40 |
| năm mươi | 50 |
| sáu mươi | 60 |
| bảy mươi | 70 |
| tám mươi | 80 |
| chín mươi | 90 |
| một trăm | 100 |
| gấp đôi | gấp đôi |
| gấp ba | gấp ba |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · CON CÁ CHÁN BIỂN LÊN CẠN LEO TRÈO · 84.3s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.9 (8.9s) | L01 | Mời bệnh nhân tiếp theo bước vào phòng khám đa khoa tiến hóa sinh vật! Y tá đâu, chuẩn bị cho tôi một chiếc chậu bùn lầy và cặp kính hiển vi đo nhãn cầu khẩn cấp! |  | Góc phòng khám bệnh viện sinh học nhiệt đới: Bàn khám gỗ dán đầy các tiêu bản rễ cây đước và vỏ ốc; KHÔNG có chú cá thòi lòi trong cảnh này; BÊN PHẢI bác sĩ cú mèo đeo kính lão, mặc áo blouse trắng cầm ống nghe và bảng chẩn đoán đang lắc đầu khó hiểu trước một chiếc chậu bùn lầy đặt trên ghế bệnh nhân. |
| b02 | 00:08.9–00:19.2 (10.3s) | L02 | Bệnh nhân hôm nay của chúng ta là một ca bệnh tâm lý và giải phẫu kỳ dị bậc nhất trong lịch sử y khoa động vật: Một sinh vật thuộc lớp cá mang vây đàng hoàng, nhưng lại mắc chứng sợ nước và chán ghét đại dương sâu sắc! |  | Bức tranh chẩn đoán tâm lý sinh học: Biểu tượng một chú cá mang vây nhưng gương mặt hoảng sợ khi nhìn thấy đại dương xanh thẳm; mũi tên chỉ hướng cá chạy trốn lên bờ cát; KHÔNG có chú cá thòi lòi trong cảnh này. |
| b03 | 00:19.2–00:32.0 (12.8s) | L03 | Bệnh nhân mang mã số 42 của chúng ta có tên trong sổ khám bệnh là Cá Thòi Lòi, hay còn gọi là cá bống biển nhiệt đới Periophthalmus! Tôi thường gọi thân mật ca bệnh khó đỡ này là: Bệnh nhân chán biển! | **SỐ 42** · bệnh nhân chán biển · R/380 · [0.75, 0.5] | Cận cảnh chiếc ghế bệnh nhân: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) ngồi chồm hổm hai tay chống nạnh trên đống bùn ướt, hai mắt lồi to tướng liếc nhìn trần nhà đầy ngơ ngác; BÊN CẠNH là biển tên Bệnh nhân chán biển. |
| b04 | 00:32.0–00:41.2 (9.2s) | L04 | Trong khi hàng triệu loài cá khác ngày đêm hoảng loạn vùng vẫy tìm đường trở về với nước ngọt hay đại dương bao la, thì bệnh nhân này lại thích trèo lên bãi bùn lội bộ phơi nắng suốt ngày đêm! |  | Tương phản sinh học kỳ dị: BÊN TRÁI hàng ngàn chú cá biển hoảng loạn quẫy nước tìm về biển cả; BÊN PHẢI chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) ung dung nằm ngửa phơi nắng trên bãi bùn lầy, hai tay gác sau gáy huýt sáo. |
| b05 | 00:41.2–00:48.0 (6.8s) | L05 | Chiều dài cơ thể của bệnh nhân dao động từ 15-20cm, với lớp da nhớt nhầy nhụa màu nâu xám lốm đốm bùn đất. | **15-20 CM** · chiều dài cơ thể · R/360 · [0.75, 0.5] | Khám nghiệm kích thước: bác sĩ cú mèo đeo kính lão, mặc áo blouse trắng cầm ống nghe và bảng chẩn đoán cầm thước dây đo dọc cơ thể chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C); thước hiển thị 15-20cm; lớp da nhớt màu nâu xám lấm lem  |
| b06 | 00:48.0–00:58.7 (10.7s) | L06 | Nhưng nhìn vào hai mắt của gã mà xem: Hai nhãn cầu lồi to tướng nằm chễm chệ ngay trên đỉnh sọ đầu, có thể xoay độc lập 360° như hai kính tiềm vọng tàu ngầm, liên tục liếc ngang liếc dọc dò xét khắp bãi ngập mặn! |  | Phóng to đầu của chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C): Hai nhãn cầu mắt lồi to tướng như hai quả bóng bàn nằm trên đỉnh sọ; một mắt xoay sang trái nhìn que kem, một mắt xoay ngược sang phải nhìn con ruồi bay qua. |
| b07 | 00:58.7–01:05.2 (6.6s) | L06b | Bác sĩ ơi, con cá này nó nhảy tưng tưng lên tận ngọn rễ cây đước rồi thò đầu dòm vào cửa sổ phòng khám kìa bác ơi! |  | Mangrove Impressionist Gouache & Satirical Field Diary style, muddy olive green and ochre tones, fluid gouache brushstrokes, hand-annotated field diary aesthetic, sharp contours, textured creamy watercolor paper background: chú cá thòi lòi hoạt hình mắt lồi to tướng đang nhảy tưng tưng bám trên ngọn rễ cây đước, thò cái đầu ngộ nghĩnh dòm thẳng vào khung cửa sổ phòng khám với ánh mắt tò mò láu lỉnh. |
| b08 | 01:05.2–01:16.1 (10.9s) | L07 | Đúng như cô trợ lý vừa la toáng lên! Bệnh nhân chán biển không những đi bộ trên mặt bùn, mà còn dùng hai chiếc vây ngực leo thoăn thoắt lên rễ cây ngập mặn ngồi ngắm hoàng hôn chẳng khác nào một chú vượn con! |  | Bên ngoài cửa sổ phòng khám: cô y tá thỏ trắng tai cụp đeo mũ chữ thập đỏ hốt hoảng chỉ tay ra cành cây đước bên ngoài; chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) đang dùng hai vây ngực bám chặt cành cây ngồi vắt vẻo như một chú ch |
| b09 | 01:16.1–01:24.3 (8.2s) | L08 | Hôm nay, hồ sơ bệnh án của chúng ta sẽ phẫu thuật từng triệu chứng kỳ quặc để xem tại sao tạo hóa lại nặn ra một con cá dở dở ương ương kỳ thú đến nhường này! |  | Toàn cảnh bãi bùn rừng ngập mặn lúc hoàng hôn: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) ngồi thong dong trên rễ cây đước ngoằn ngoèo, miệng huýt sáo ngắm mặt trời lặn; BÊN TRÁI bác sĩ cú mèo đeo kính lão, mặc áo blouse trắng cầm  |

### scene02 · NGHỊCH LÝ CON CÁ CÓ THỂ CHẾT ĐUỐI DƯỚI NƯỚC · 110.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.6 (9.6s) | L09 | Triệu chứng chẩn đoán số hai sẽ khiến toàn thể giới sinh học đại dương phải dụi mắt hoài nghi! Nếu bạn bắt một con cá chép hay cá hồi thả xuống nước, chúng sẽ bơi lội tung tăng như gặp lại thiên đường. |  | Thí nghiệm y khoa đối chứng: BÊN TRÁI là chú cá vàng bơi tung tăng trong bể nước trong suốt; BÊN PHẢI là chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) bị nhốt trong lồng dưới nước đang ôm cổ ho sặc sụa; KHÔNG có chú cá thòi lòi trong  |
| b02 | 00:09.6–00:16.9 (7.2s) | L09b | Nhưng nếu bạn nhốt một con Cá Thòi Lòi vào một lồng lưới kín chìm sâu dưới đáy nước tù đọng và không cho gã ngoi lên cạn, thì điều gì sẽ xảy ra? |  | Mangrove Impressionist Gouache & Satirical Field Diary style, muddy olive green and ochre tones, fluid gouache brushstrokes, hand-annotated field diary aesthetic, sharp contours, textured creamy watercolor paper background: chú cá thòi lòi hoạt hình bị nhốt trong một chiếc lồng lưới sắt chìm sâu dưới đáy nước đục, biểu cảm hốt hoảng ôm cổ họng ngạt thở vì không được ngoi lên mặt nước hít thở không khí. |
| b03 | 00:16.9–00:19.6 (2.7s) | L10 | Gã sẽ ngạt thở và chết đuối như một con người thực thụ! |  | Bảng cảnh báo y khoa: Hình ảnh chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) bị ngạt thở dưới đáy nước sâu; chiếc đồng hồ cát đếm ngược hiển thị nguy cơ ngạt khí; bác sĩ cú mèo đeo kính lão, mặc áo blouse trắng cầm ống nghe và bảng ch |
| b04 | 00:19.6–00:27.5 (8.0s) | L11 | Nguyên nhân y khoa nằm ở cấu tạo hệ hô hấp đã bị thoái hóa mang trầm trọng của Bệnh nhân chán biển! Trong quá trình tiến hóa hơn 300 triệu năm, |  | Phim chụp X-quang mang cá: Mô hình mang cá của chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) teo nhỏ xíu dính chặt vào nhau; mũi tên đỏ chỉ vào diện tích tiếp xúc kém; bác sĩ cú mèo đeo kính lão, mặc áo blouse trắng cầm ống nghe và bả |
| b05 | 00:27.5–00:35.1 (7.6s) | L11b | các lá mang dưới nước của gã đã teo nhỏ và dính chặt vào nhau, không còn đủ diện tích tiếp xúc để lọc đủ oxy hòa tan trong nước như các loài cá thông thường. |  | Mangrove Impressionist Gouache & Satirical Field Diary style, muddy olive green and ochre tones, fluid gouache brushstrokes, hand-annotated field diary aesthetic, sharp contours, textured creamy watercolor paper background: sơ đồ giải phẫu phóng đại chiếc mang cá thòi lòi bị thoái hóa: các lá mang teo tóp dính bẹp vào nhau so sánh với mang cá chép xòe rộng đỏ tươi, có thước đo y khoa đánh dấu cảnh báo thoái hóa nghiê |
| b06 | 00:35.1–00:44.2 (9.1s) | L12 | Để sinh tồn trên cạn, gã đã phát triển một công nghệ hô hấp lưỡng cư thần sầu: Lớp da nhầy của gã chứa mạng lưới mao mạch máu dày đặc, kết hợp với niêm mạc ẩm ướt trong vòm họng. |  | Sơ đồ giải phẫu hô hấp da: Lớp da nhầy của chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) phát sáng màu xanh dương rực rỡ; các phân tử oxy ngoài không khí thẩm thấu trực tiếp qua da và niêm mạc vòm họng vào mạch nước màu. |
| b07 | 00:44.2–00:55.5 (11.3s) | L13 | Toàn bộ bề mặt da và cổ họng của gã hấp thụ trực tiếp từ 50-60% lượng oxy từ không khí ngoài trời! Ủa bác sĩ ơi, thế lúc gã leo lên bờ cát khô queo thì hai cái mang cá dùng để làm gì ạ? | **50-60%** · oxy hấp thụ qua da · L/360 · [0.25, 0.5] | Cận cảnh dòng nước màu giàu dưỡng khí: Các hạt oxy màu xanh ngọc bích từ không khí tràn qua màng da ẩm ướt, biến dòng nước màu đỏ thẫm thành đỏ tươi tràn đầy sinh lực; chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) tươi cười rạng rỡ. |
| b08 | 00:55.5–00:58.4 (2.8s) | L14 | Chú cá con hỏi câu hỏi trúng ngay điểm mười sinh học! |  | Phòng học giải phẫu sinh vật: cô y tá thỏ trắng tai cụp đeo mũ chữ thập đỏ và chú còng gió nhỏ giơ hai càng cười nhe răng đứng cạnh chiếc bảng phấn vẽ hình mang cá, mắt chớp chớp ngơ ngác khó hiểu. |
| b09 | 00:58.4–01:08.6 (10.2s) | L15 | Hai nắp mang phồng to của Cá Thòi Lòi không dùng để thở nước, mà dùng làm hai chiếc bình giữ nước di động! Trước khi trèo lên cạn, gã hớp một ngụm nước thật đầy nhốt chặt trong khoang mang đóng kín bưng. |  | Cận cảnh hai má phồng to: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) phồng hai má to như hai quả bóng nước, nhốt chặt ngụm nước trong nắp mang đóng kín bưng; các bọt nước lấp lánh giữ ẩm sợi mang. |
| b10 | 01:08.6–01:15.7 (7.1s) | L16 | Lượng nước dự trữ này liên tục làm ẩm các sợi mang mỏng manh, giúp gã lang thang trên bờ hàng giờ liền mà không sợ bị khô mang! |  | Bình dưỡng khí di động: Hai khoang mang của chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) đóng vai trò như hai bình nước dã ngoại; chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn x |
| b11 | 01:15.7–01:26.6 (10.9s) | L17 | Thậm chí trong khoang miệng của gã, hệ thống van niêm mạc hoạt động như một nắp van cao su chống trào ngược. Bất kể gã lộn nhào hay nhảy cao trên bùn lầy, ngụm nước quý giá trong má vẫn không hề bị rỉ ra ngoài một giọt! |  | Cơ chế van cao su chống trào ngược: Cắt lớp miệng cá thòi lòi; nắp van niêm mạc khóa chặt cổ họng; giọt nước trong má không hề rỉ ra dù chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) đang lộn nhào biểu diễn. |
| b12 | 01:26.6–01:29.6 (3.0s) | L18 | Một công nghệ khóa kín nước dã ngoại đỉnh cao của thế giới cá! |  | Vũ điệu nhào lộn trên bùn: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) lộn nhào trên không trung, hai má phồng tròn nước vẫn nguyên vẹn; chú còng gió nhỏ giơ hai càng cười nhe răng giơ hai càng vỗ tay tán thưởng cuồng nhiệt. |
| b13 | 01:29.6–01:36.7 (7.1s) | L19 | Đặc biệt hơn nữa, chiếc đuôi của bệnh nhân này còn có khả năng hô hấp phụ trợ vô cùng độc đáo! Khi ngồi phơi nắng trên rễ cây, |  | Góc thư giãn bãi lầy: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) ngồi vắt vẻo trên rễ cây khô, thả lỏng chóp đuôi nhúng ngập trong vũng nước bùn mát rượi; các tia dưỡng khí lấp lánh chạy dọc từ đuôi lên lưng. |
| b14 | 01:36.7–01:46.2 (9.5s) | L19b | gã thường thả lỏng chóp đuôi nhúng ngập trong vũng nước bên dưới. Lớp biểu bì đuôi siêu mỏng có thể trao đổi khí liên tục, vừa làm mát cơ thể vừa bơm thêm dưỡng khí cho máu! |  | Mangrove Impressionist Gouache & Satirical Field Diary style, muddy olive green and ochre tones, fluid gouache brushstrokes, hand-annotated field diary aesthetic, sharp contours, textured creamy watercolor paper background: chú cá thòi lòi hoạt hình ngồi vắt vẻo trên rễ cây đước phơi nắng, chóp đuôi thả lỏng nhúng sâu vào vũng nước trong veo bên dưới với hiệu ứng bọt khí oxy phát sáng thẩm thấu qua da đuôi. |
| b15 | 01:46.2–01:50.9 (4.7s) | L20 | Một sự thích nghi lưỡng thê hoàn hảo đến mức khiến các loài bò sát cũng phải ngả mũ bái phục! |  | Hội đồng bò sát thán phục: Một chú kỳ đà và một chú rùa ngồi dưới tán cây ngả mũ chào chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) đang thong thả thở bằng chóp đuôi trên rễ đước. |

### scene03 · TUYỆT KỸ CHỚP MẮT TỤT XUỐNG HỌNG ĐỂ NUỐT MỒI · 92.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.1 (10.1s) | L21 | Bây giờ, hãy đeo kính lúp phóng đại để kiểm tra vùng mặt kỳ dị nhất hành tinh của Bệnh nhân chán biển! Cá thông thường sinh ra vốn dĩ không có mí mắt, và mắt của chúng nằm cố định hai bên má. |  | Góc nghiên cứu nhãn khoa: Mô hình hộp sọ cá thòi lòi bằng thạch cao; hai nhãn cầu lồi to tướng đặt trên giá đỡ đo đạc; KHÔNG có chú cá thòi lòi trong cảnh này; ánh nắng chói chang chiếu rọi gay gắt. |
| b02 | 00:10.1–00:14.9 (4.8s) | L22 | Nhưng Cá Thòi Lòi lại sở hữu đôi mắt lồi nhô cao hẳn lên đỉnh đầu như hai quả bóng bàn đồ chơi! |  | Đôi mắt kính tiềm vọng: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) lặn dưới vũng bùn chỉ thò đúng hai nhãn cầu mắt lồi to tướng lên khỏi mặt bùn như hai kính tiềm vọng tàu ngầm quét bốn phương; KHÔNG có chú cá thòi lòi trong cảnh n |
| b03 | 00:14.9–00:28.1 (13.2s) | L23 | Vì sống trên cạn giữa cái nắng gay gắt 30 lăm đến 40°C của rừng ngập mặn nhiệt đới, đôi mắt của gã đối mặt với nguy cơ bị khô giác mạc và mù lòa bất cứ lúc nào. Nhưng gã không hề có tuyến nước mắt! Vậy gã giải quyết bài toán chống khô mắt này như thế nào? | **40°C** · nắng gắt bãi lầy · R/360 · [0.75, 0.5] | Thời tiết khắc nghiệt: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) đứng giữa bãi bùn nắng gắt chiếu rọi, chiếc nhiệt kế cắm cạnh chỉ 40°C; hai mắt lồi toát mồ hôi lo sợ bị khô mắt. |
| b04 | 00:28.1–00:35.5 (7.3s) | L24 | Gã co rút cơ mặt, kéo tụt cả hai nhãn cầu mắt lặn sâu xuống bên trong hốc đầu! Phía dưới đáy hốc mắt có một chiếc túi chứa nước dịch ẩm |  | Khoảnh khắc kỳ thú thụt mắt: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) co cơ kéo tụt cả hai nhãn cầu mắt lặn sâu xuống bên trong đầu, biến mất khỏi đỉnh sọ; dưới đáy hốc mắt có chiếc túi nước bôi trơn nhãn cầu sáng loáng. |
| b05 | 00:35.5–00:43.4 (7.9s) | L25 | ướt. Mỗi khi gã thụt mắt xuống, nhãn cầu được nhúng ngập trong bể nước làm ẩm tức thì, rồi lại ngoi bật lên sáng long lanh như vừa được tra thuốc nhỏ mắt! |  | Cú tra thuốc nhỏ mắt tự nhiên: Hai nhãn cầu mắt ngoi bật trở lại đỉnh đầu sáng long lanh như hai viên ngọc; chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) chớp mắt lia lịa khoái chí. |
| b06 | 00:43.4–00:51.5 (8.1s) | L26 | Nhưng phát hiện chấn động vừa được nhóm nghiên cứu của tiến sĩ Michel công bố trên Tạp chí Sinh học Thực nghiệm: Cú thụt mắt này còn kiêm luôn chức năng nuốt thức ăn! |  | Phòng thí nghiệm quốc tế: Nhóm nhà khoa học hoạt hình đang reo hò trước màn hình máy quay siêu chậm ghi lại khoảnh khắc cá thòi lòi đớp mồi trên bùn; KHÔNG có chú cá thòi lòi trong cảnh này. |
| b07 | 00:51.5–00:59.4 (7.8s) | L27 | Vì sống trên cạn nên Cá Thòi Lòi không thể dùng dòng nước xoáy để cuốn mồi vào bụng như cá dưới biển, và lưỡi của gã cũng không có cơ bắp linh hoạt như ếch nhái. |  | Thách thức nuốt mồi không có nước: So sánh một chú cá biển hút dòng nước nuốt mồi với chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) đứng trơ trên cạn lưỡi ngắn cũn không cơ bắp; KHÔNG có chú cá thòi lòi trong cảnh này. |
| b08 | 00:59.4–01:07.0 (7.7s) | L28 | Mỗi khi đớp được một chú còng gió hay bọ gậy trên bùn, gã đồng thời thụt mạnh cả hai nhãn cầu mắt thụt sâu xuống vòm miệng! |  | Cơ chế pit-tông nuốt mồi: Cắt lớp miệng chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C); hai đáy nhãn cầu tụt sâu xuống ép chặt vòm miệng, đẩy chú còng gió trôi tuột xuống thực quản; mặt chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (mà |
| b09 | 01:07.0–01:13.2 (6.2s) | L29 | Đáy nhãn cầu đóng vai trò như một chiếc pit-tông cơ khí ép chặt xuống khoang họng, đẩy phăng con mồi trôi tuột xuống thực quản! |  | Mô hình pit-tông cơ khí: Hình vẽ kỹ thuật minh họa hai nhãn cầu đóng vai trò như hai xi-lanh pit-tông máy nén ép thức ăn trôi thẳng vào dạ dày; KHÔNG có chú cá thòi lòi trong cảnh này. |
| b10 | 01:13.2–01:18.4 (5.2s) | L30 | Nghĩa là trên đời này, chỉ có duy nhất loài cá thòi lòi là nuốt mồi bằng chính đôi mắt của mình! |  | Kỳ quan nuốt mồi bằng mắt: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) xoa bụng no tròn, giơ ngón tay cái cười tự hào; phía sau là tấm biển NUỐT MỒI BẰNG ĐÔI MẮT ĐỘC NHẤT VÔ NHỊ. |
| b11 | 01:18.4–01:28.8 (10.3s) | L31 | Chưa dừng lại ở đó, đôi mắt lồi này còn là hệ thống radar cảnh giới 360° hoàn hảo! Một mắt có thể nhìn chăm chú xuống bùn để rình mồi, trong khi mắt kia ngước ngược lên trời để canh chừng chim bói cá săn mồi. |  | Hệ thống radar 360 độ: Hình tròn tầm nhìn quét toàn cảnh; một mắt của chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) soi xuống bãi bùn thấy chú sâu béo ngậy, mắt kia ngước lên trời thấy bóng chim bói cá lượn lờ. |
| b12 | 01:28.8–01:32.4 (3.6s) | L32 | Bất kỳ kẻ thù nào lọt vào bán kính 3 mét đều bị gã phát hiện trong tích tắc! | **3 MÉT** · bán kính radar 360° · R/360 · [0.75, 0.5] | Cảnh giới tối cao: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) phát hiện chim bói cá từ xa 3 mét, lập tức cúi rạp người chuẩn bị tẩu thoát; radar trên đầu nhấp nháy đèn xanh an toàn. |

### scene04 · ĐÔI VÂY NGỰC BIẾN TÍNH THÀNH HAI CÁNH TAY LEO TRÈO · 87.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:12.8 (12.8s) | L33 | Hãy chuyển sang kiểm tra hệ cơ xương vận động của bệnh nhân số 42! Nếu bạn quan sát kỹ cặp vây ngực của Cá Thòi Lòi, bạn sẽ kinh ngạc nhận ra đây hoàn toàn không phải là những nan vây quạt nước mỏng manh của loài cá biển. |  | Bản vẽ giải phẫu vây ngực: Sơ đồ xương vây ngực có khớp khuỷu tay và bó cơ vận động giống hệt cánh tay người; KHÔNG có chú cá thòi lòi trong cảnh này; bên cạnh là chiếc thước đo góc xoay. |
| b02 | 00:12.8–00:18.0 (5.2s) | L34 | Cấu trúc xương bên trong đã tiến hóa thành các khớp xương khuỷu tay và cơ bắp bám chắc chắn! |  | So sánh khớp xương: BÊN TRÁI nan vây mỏng manh của cá trích; BÊN PHẢI vây ngực cơ bắp có khớp khuỷu tay của chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C); mũi tên chỉ vào bó cơ nâng đỡ trọng lượng cơ thể. |
| b03 | 00:18.0–00:28.6 (10.6s) | L35 | Cặp vây ngực này có thể xoay gập linh hoạt, cho phép Bệnh nhân chán biển chống hai tay xuống bùn rồi đẩy toàn bộ trọng lượng cơ thể tiến về phía trước theo nhịp điệu nhịp nhàng như một anh lính bò trườn! |  | Hành trình việt dã trên bùn: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) chống hai vây ngực xuống bùn bước đi mạnh mẽ như chú vượn con; dưới bụng lộ rõ chiếc đĩa hút tròn xoe bám dính trên rễ cây. |
| b04 | 00:28.6–00:40.5 (11.9s) | L36 | Dưới bụng của gã còn có một chiếc đĩa hút hình thành từ hai vây bụng dính liền nhau, tạo lực bám dính chắc nịch trên những thân cây đước trơn trượt! Bác sĩ ơi, em thấy nó co đuôi một phát là bay vèo qua mặt em xa tít mù tắp luôn á bác sĩ! |  | Cận cảnh đĩa hút bụng: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) treo ngược người dưới cành cây đước nhờ chiếc đĩa hút bụng dính chặt như giác hút cao su; hai tay vẫy chào bác sĩ cú mèo đeo kính lão, mặc áo blouse trắng cầm ống ng |
| b05 | 00:40.5–00:51.1 (10.6s) | L37 | Bé con vừa chứng kiến tuyệt kỹ búng đuôi thần sầu của gã đấy! Khi cần tẩu thoát khỏi chim bói cá hay kỳ đà đói khát, Cá Thòi Lòi gập cong chiếc đuôi cơ bắp hình chữ C rồi bung mạnh như một chiếc lò xo thép! |  | Cú nhảy lò xo ngoạn mục: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) gập cong đuôi hình chữ C búng mạnh bay vút lên không trung; vệt nước bắn tung tóe phía sau; thước đo khoảng cách ghi 1 mét. |
| b06 | 00:51.1–00:57.5 (6.5s) | L38 | Cú phóng này hất tung gã bay xa gấp 4 lần chiều dài cơ thể, tương đương cú nhảy xa gần 1 mét trên mặt bùn lầy lội! | **GẤP 4 LẦN** · khoảng cách nhảy xa · L/360 · [0.25, 0.5]<br>**1 MÉT** · cú búng đuôi lò xo · R/360 · [0.75, 0.5] | Bay trên mặt bùn lầy: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) lượn một đường parabol trên không trung qua đầu chú còng gió nhỏ giơ hai càng cười nhe răng; chú còng gió nhỏ giơ hai càng cười nhe răng ngước nhìn há hốc mồm kinh ng |
| b07 | 00:57.5–01:09.9 (12.4s) | L39 | Vào mùa giao phối, tuyệt kỹ nhảy xa này biến thành màn biểu diễn võ thuật đường phố đỉnh cao! Các chàng cá thòi lòi dựng đứng vây lưng sặc sỡ như những lá cờ chiến, há to miệng thị uy rồi bật nhảy liên tục trên không trung để tranh giành lãnh thổ và thu hút các nàng cá mái. |  | Vũ đài tình yêu bãi bùn: Hai chú cá thòi lòi đực bật nhảy cao trên không trung, vây lưng giương cao sặc sỡ như cánh buồm ngũ sắc, miệng há to thị uy; một nàng cá mái ngồi dưới tán cây vỗ vây tán thưởng. |
| b08 | 01:09.9–01:13.8 (3.8s) | L40 | Kẻ nào nhảy cao hơn và có vây lưng lòe loẹt hơn sẽ làm bá chủ bãi lầy! |  | Bá chủ bãi lầy ngập mặn: Chú cá thòi lòi đực chiến thắng giương vây cờ ngũ sắc đứng trên đỉnh cồn bùn, đeo vòng nguyệt quế; các đối thủ cúi đầu thần phục. |
| b09 | 01:13.8–01:20.4 (6.7s) | L41 | Một con cá dài 20cm nhưng vừa biết chạy bộ, vừa biết leo cây, vừa biết nhảy xa bay trên không trung! | **20 CM** · chiều dài cơ thể · L/360 · [0.25, 0.5] | Huy chương vàng Olympic điền kinh: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) đứng trên bục vinh quang số 1 đeo huy chương vàng môn điền kinh phối hợp leo cây chạy bộ nhảy xa; khán giả vỗ tay cuồng nhiệt. |
| b10 | 01:20.4–01:27.5 (7.1s) | L42 | Nếu đem so tỷ lệ cơ thể với các vận động viên điền kinh Olympic, thành tích bay nhảy của bệnh nhân này đủ sức giật huy chương vàng môn nhảy xa phối hợp! |  | So sánh tỷ lệ vận động viên: Biểu đồ so sánh tỷ lệ nhảy xa của chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) với vận động viên Olympic; mũi tên chỉ số thành tích vượt trội; KHÔNG có chú cá thòi lòi trong cảnh này. |

### scene05 · CÔNG TRÌNH HANG BÙN HÌNH CHỮ Y VÀ TÚI KHÍ NUÔI CON · 65.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.7 (10.7s) | L43 | Chẩn đoán bệnh án cuối cùng dẫn chúng ta xuống lòng đất ngầm của bãi lầy ngập mặn! Khi mùa sinh sản đến, Bệnh nhân chán biển không hề đẻ trứng trôi nổi vô trách nhiệm trên mặt nước để làm mồi cho cá lớn. |  | Mặt cắt địa đạo bùn ngập mặn: Sơ đồ hang bùn hình chữ Y sâu 2 mét dưới đáy lầy; các nhánh hang ngoằn ngoèo có tháp bùn tròn bảo vệ miệng hang; KHÔNG có chú cá thòi lòi trong cảnh này. |
| b02 | 00:10.7–00:17.5 (6.9s) | L44 | Gã dùng chính chiếc miệng của mình cạp từng búng bùn đất ngậm nhổ ra ngoài để đào một công trình địa đạo ngầm hình chữ Y sâu tới 2 mét! | **2 MÉT** · địa đạo ngầm chữ Y · L/360 · [0.25, 0.5] | Công trường xây dựng ngầm: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) miệng ngậm từng búng bùn đất ngoi lên nhổ ra ngoài bờ, đào sâu địa đạo hình chữ Y kiên cố. |
| b03 | 00:17.5–00:24.4 (6.8s) | L45 | Để miệng hang không bị sạt lở khi thủy triều dâng lên, gã còn khéo léo đắp những ụ bùn tròn xung quanh miệng hang như những tháp canh pháo đài mini. |  | Pháo đài chắn thủy triều: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) khéo léo đắp ụ bùn tròn xoe xung quanh miệng hang như tháp canh thành quách chắn sóng triều dâng; KHÔNG có chú cá thòi lòi trong cảnh này. |
| b04 | 00:24.4–00:31.8 (7.4s) | L46 | Đáy hang ngập ngụa trong nước bùn yếm khí hoàn toàn không có một phân tử oxy nào hòa tan. Nếu trứng cá đẻ ở đây, trứng sẽ thối rữa và chết ngạt tức thì. |  | Nguy cơ yếm khí đáy bùn: Đáy hang tối đen ngập nước không có oxy; các bọt khí yếm khí độc hại bao quanh; hình ảnh nguy hiểm cho trứng cá; KHÔNG có chú cá thòi lòi trong cảnh này. |
| b05 | 00:31.8–00:38.1 (6.3s) | L47 | Nhưng chú cá thòi lòi bố đã giải quyết thảm họa này bằng một kỳ tích kỹ thuật ngầm khiến các nhà khoa học Nhật Bản phải kinh ngạc! |  | Kỳ tích kỹ thuật ngậm khí: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) ngoi lên mặt cạn há to miệng ngậm một búng không khí căng phồng hai má, chuẩn bị lặn ngược xuống đáy hang sâu. |
| b06 | 00:38.1–00:45.6 (7.5s) | L48 | Gã bơi lên mặt cạn, há to miệng đớp một búng không khí căng tràn rồi lặn ngược xuống đáy hang sâu 2 mét nhả vào một căn phòng phụ trên trần hang! |  | Chuyến xe buýt con thoi ngậm khí: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) lặn sâu xuống đáy hang 2 mét, nhả búng không khí vào căn phòng phụ trên trần hang tối. |
| b07 | 00:45.6–00:57.9 (12.2s) | L49 | Gã miệt mài thực hiện hàng trăm chuyến bơi con thoi ngậm không khí như một chú thợ lặn cần mẫn, cho đến khi tạo ra một chiếc túi khí ngầm lơ lửng dưới lòng bùn! Nàng cá mẹ dán hàng ngàn quả trứng lên trần phòng túi khí khô ráo giàu dưỡng khí này. |  | Căn phòng túi khí ngầm: Dưới đáy hang bùn, một túi khí trong suốt lơ lửng trên trần hang; hàng ngàn quả trứng cá nhỏ bám trên trần sáng lấp lánh; chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) bơi quanh canh gác với ánh mắt trìu mến. |
| b08 | 00:57.9–01:05.7 (7.8s) | L50 | Suốt nhiều tuần lễ ấp trứng, cá bố liên tục thay phiên tuần tra canh giữ cửa hang và lặn xuống thay mới túi khí, cho đến khi đàn cá con nở ra khỏe mạnh! |  | Đàn cá con chào đời: Hàng trăm chú cá thòi lòi con mắt tí hon bơi lội quanh túi khí ngầm trong hang; chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) ông bố cần mẫn tươi cười vẫy chào đàn con. |

### scene06 · DỞ DANG NHƯNG LÀ BƯỚC CHUYỂN MÌNH LỊCH SỬ · 67.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.6 (7.6s) | L51 | Hồ sơ bệnh án số 42 chính thức hoàn tất với kết luận chẩn đoán: Cá Thòi Lòi hoàn toàn khỏe mạnh và là một tuyệt tác chuyển giao sinh học vĩ đại! |  | Bức tranh chuyển giao lịch sử: Cây phả hệ tiến hóa sinh học; chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) đứng ở mắt xích trung tâm chuyển giao giữa cá dưới biển và động vật bốn chân trên cạn cách đây 300 triệu năm; ánh hào quang chi |
| b02 | 00:07.6–00:16.5 (8.9s) | L52 | Gã là hình bóng sống động của tổ tiên bốn chân xa xưa cách đây 300 triệu năm, những sinh vật dũng cảm đầu tiên dám thò đầu ra khỏi biển cả tăm tối để chinh phục lục địa khô cằn! |  | Tổ tiên bốn chân chinh phục đất liền: Hình ảnh tái hiện cách đây 300 triệu năm, những sinh vật đầu tiên dũng cảm thò đầu lên khỏi biển cả bước đi trên bùn lầy; KHÔNG có chú cá thòi lòi trong cảnh này. |
| b03 | 00:16.5–00:25.9 (9.5s) | L53 | Đôi khi trong cuộc sống, bạn có thể bị người đời chê cười là kẻ dở dở ương ương, không giống ai và không thuộc về một khuôn mẫu nào: Nhưng hãy nhớ tới chú cá thòi lòi! |  | Hình ảnh ẩn dụ truyền cảm hứng: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) tươi cười tự tin đứng trên mỏm đá ngập mặn, một vây vẫy chào biển cả, một vây chỉ về phía đất liền rộng lớn đầy nắng ấm. |
| b04 | 00:25.9–00:34.0 (8.0s) | L54 | Chính sự khác biệt nửa nạc nửa mỡ, dám bơi ngược dòng quy chuẩn và mở lối đi riêng mới là khởi đầu cho những bước nhảy vọt tiến hóa vĩ đại nhất của lịch sử! |  | Con đường tiên phong mở lối: Dấu chân vây cá của chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) in dài trên bãi bùn hướng về ánh bình minh rạng rỡ; biểu tượng của sự kiên định khác biệt. |
| b05 | 00:34.0–00:45.3 (11.4s) | L55 | Nếu được sinh ra với một siêu năng lực kỳ lạ của cá thòi lòi, bạn muốn sở hữu đôi mắt xoay 360° thụt nuốt mồi hay cặp tay leo cây chạy bộ trên bùn? Hãy để lại bình luận chẩn đoán của bạn bên dưới nhé! |  | Tương tác người xem: bác sĩ cú mèo đeo kính lão, mặc áo blouse trắng cầm ống nghe và bảng chẩn đoán cùng cô y tá thỏ trắng tai cụp đeo mũ chữ thập đỏ và chú còng gió nhỏ giơ hai càng cười nhe răng đứng bên cạnh chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa |
| b06 | 00:45.3–00:51.1 (5.8s) | L56 | Còn bây giờ, hãy chuẩn bị tinh thần bước vào phiên tòa xét xử rùng rợn của hồ sơ số 43! |  | Cận cảnh hình bóng teaser tập 43 (TASTE-68): Trong phòng phẫu thuật tối mờ kỳ bí, một cái bóng đen bí ẩn (solid black silhouette) hình con ong bắp cày với chiếc kim tiêm nhọn hoắt sau lưng gắn dấu hỏi '?', phía trước là bóng một con gián đang ngoan ngoãn cúi đầu bước đi như xác sống. |
| b07 | 00:51.1–00:55.2 (4.1s) | L57 | Một kẻ sát nhân khoác tấm áo choàng ngọc bích lấp lánh, một bác sĩ phẫu thuật thần kinh tàn |  | Poster đóng dấu hồ sơ 43: Chữ TẬP 43 phát sáng xanh ngọc bích trên nền tím than; bóng đen sát thủ ngọc bích cầm kim tiêm laser; KHÔNG có chú cá thòi lòi trong cảnh này. |
| b08 | 00:55.2–01:07.2 (12.0s) | L57b | độc chuyên thực hiện ca châm kim vi phẫu chuẩn xác đến từng mi-li-mét vào hạch não của loài gián, tước đoạt toàn bộ ý chí tự do và biến nạn nhân thành một xác sống Zombie ngoan ngoãn tự đi vào mồ chôn! Bạn có biết sát thủ ngọc bích này là ai không? |  | Mangrove Impressionist Gouache & Satirical Field Diary style, muddy olive green and ochre tones, fluid gouache brushstrokes, hand-annotated field diary aesthetic, sharp contours, textured creamy watercolor paper background: poster nghệ thuật hé lộ sát thủ tập tiếp theo: một chú ong bắp cày ngọc lục bảo phát sáng lấp lánh đang dùng chiếc kim châm vi phẫu đâm chuẩn xác vào hạch não chú gián khổng lồ biến thành zombie n |

## 5. Phân cảnh Shorts — từng beat

Banner: **CÁ NGẠT THỞ DƯỚI NƯỚC?! / THỤT MẮT ĐỂ NUỐT MỒI** · giọng 40.9s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Bạn có tin trên đời có một con cá nếu bị ép ở dưới nước quá lâu thì sẽ bị... chết đuối? |  |
| s02 | 00:05.9 | S02 | Đây là Cá Thòi Lòi, loài cá chán biển lên cạn sống rải rác khắp các cánh rừng ngập mặn! Mang của gã đã bị thoái hóa nặng, |  |
| s03 | 00:12.1 | S02b | nhưng bù lại gã hô hấp trực tiếp qua da và vòm họng ẩm ướt để hấp thụ hơn 50% lượng oxy ngoài trời. |  |
| s04 | 00:18.1 | S03 | Để không bị khô mang, gã hớp đầy nước vào hai má phồng to như hai bình dưỡng khí di động! Chưa hết, |  |
| s05 | 00:23.4 | S04 | cặp vây ngực của gã biến tính thành hai cánh tay có khớp khuỷu để chống bùn chạy bộ và leo thoăn thoắt lên rễ cây đước. |  |
| s06 | 00:29.1 | S05 | Nhưng dị nhất là đôi mắt lồi trên đỉnh sọ: |  |
| s07 | 00:31.6 | S06 | Mỗi khi đớp mồi trên cạn, gã co cơ kéo tụt cả hai nhãn cầu mắt xuống cổ họng để làm chiếc pit-tông ép thức ăn trôi xuống dạ dày, |  |
| s08 | 00:38.5 | S07 | vừa làm ẩm mắt vừa nuốt mồi trong tích tắc! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mời bệnh nhân tiếp theo bước vào phòng khám đa khoa tiến hóa sinh vật! Y tá đâu, chuẩn bị cho tôi một chiếc chậu bùn lầy và cặp kính hiển vi đo nhãn cầu khẩn cấp!". Bố cục: Góc phòng khám bệnh viện sinh học nhiệt đới: Bàn khám gỗ dán đầy các tiêu bản rễ cây đước và vỏ ốc; KHÔNG có chú cá thòi lòi trong cảnh này; BÊN PHẢI bác sĩ cú mèo đeo kính lão, mặc áo blouse trắng cầm ống nghe và bảng chẩn đoán đang lắc đầu khó hiểu trước một chiếc chậu bùn lầy đặt trên ghế bệnh nhân.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bệnh nhân hôm nay của chúng ta là một ca bệnh tâm lý và giải phẫu kỳ dị bậc nhất trong lịch sử y khoa động vật: Một sinh vật thuộc lớp cá mang vây đàng hoàng, nhưng lại mắc chứng sợ nước và chán ghét đại dương sâu sắc!". Bố cục: Bức tranh chẩn đoán tâm lý sinh học: Biểu tượng một chú cá mang vây nhưng gương mặt hoảng sợ khi nhìn thấy đại dương xanh thẳm; mũi tên chỉ hướng cá chạy trốn lên bờ cát; KHÔNG có chú cá thòi lòi trong cảnh này.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bệnh nhân mang mã số 42 của chúng ta có tên trong sổ khám bệnh là Cá Thòi Lòi, hay còn gọi là cá bống biển nhiệt đới Periophthalmus! Tôi thường gọi thân mật ca bệnh khó đỡ này là: Bệnh nhân chán biển!". Bố cục: Cận cảnh chiếc ghế bệnh nhân: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) ngồi chồm hổm hai tay chống nạnh trên đống bùn ướt, hai mắt lồi to tướng liếc nhìn trần nhà đầy ngơ ngác; BÊN CẠNH là biển tên Bệnh nhân chán biển.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong khi hàng triệu loài cá khác ngày đêm hoảng loạn vùng vẫy tìm đường trở về với nước ngọt hay đại dương bao la, thì bệnh nhân này lại thích trèo lên bãi bùn lội bộ phơi nắng suốt ngày đêm!". Bố cục: Tương phản sinh học kỳ dị: BÊN TRÁI hàng ngàn chú cá biển hoảng loạn quẫy nước tìm về biển cả; BÊN PHẢI chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) ung dung nằm ngửa phơi nắng trên bãi bùn lầy, hai tay gác sau gáy huýt sáo.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiều dài cơ thể của bệnh nhân dao động từ 15-20cm, với lớp da nhớt nhầy nhụa màu nâu xám lốm đốm bùn đất.". Bố cục: Khám nghiệm kích thước: bác sĩ cú mèo đeo kính lão, mặc áo blouse trắng cầm ống nghe và bảng chẩn đoán cầm thước dây đo dọc cơ thể chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C); thước hiển thị 15-20cm; lớp da nhớt màu nâu xám lấm lem bùn đất.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng nhìn vào hai mắt của gã mà xem: Hai nhãn cầu lồi to tướng nằm chễm chệ ngay trên đỉnh sọ đầu, có thể xoay độc lập 360° như hai kính tiềm vọng tàu ngầm, liên tục liếc ngang liếc dọc dò xét khắp bãi ngập mặn! Bác sĩ ơi, con cá này nó nhảy tưng tưng lên tận ngọn rễ cây đước rồi thò đầu dòm vào cửa sổ phòng khám kìa bác ơi!". Bố cục: Phóng to đầu của chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C): Hai nhãn cầu mắt lồi to tướng như hai quả bóng bàn nằm trên đỉnh sọ; một mắt xoay sang trái nhìn que kem, một mắt xoay ngược sang phải nhìn con ruồi bay qua.
```
</details>

<details><summary>L06b</summary>

```text
Mangrove Impressionist Gouache & Satirical Field Diary style, muddy olive green and ochre tones, fluid gouache brushstrokes, hand-annotated field diary aesthetic, sharp contours, textured creamy watercolor paper background: chú cá thòi lòi hoạt hình mắt lồi to tướng đang nhảy tưng tưng bám trên ngọn rễ cây đước, thò cái đầu ngộ nghĩnh dòm thẳng vào khung cửa sổ phòng khám với ánh mắt tò mò láu lỉnh.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đúng như cô trợ lý vừa la toáng lên! Bệnh nhân chán biển không những đi bộ trên mặt bùn, mà còn dùng hai chiếc vây ngực leo thoăn thoắt lên rễ cây ngập mặn ngồi ngắm hoàng hôn chẳng khác nào một chú vượn con!". Bố cục: Bên ngoài cửa sổ phòng khám: cô y tá thỏ trắng tai cụp đeo mũ chữ thập đỏ hốt hoảng chỉ tay ra cành cây đước bên ngoài; chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) đang dùng hai vây ngực bám chặt cành cây ngồi vắt vẻo như một chú chim non ngắm cảnh.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hôm nay, hồ sơ bệnh án của chúng ta sẽ phẫu thuật từng triệu chứng kỳ quặc để xem tại sao tạo hóa lại nặn ra một con cá dở dở ương ương kỳ thú đến nhường này!". Bố cục: Toàn cảnh bãi bùn rừng ngập mặn lúc hoàng hôn: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) ngồi thong dong trên rễ cây đước ngoằn ngoèo, miệng huýt sáo ngắm mặt trời lặn; BÊN TRÁI bác sĩ cú mèo đeo kính lão, mặc áo blouse trắng cầm ống nghe và bảng chẩn đoán cầm hồ sơ bệnh án đứng ngắm nhìn.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Triệu chứng chẩn đoán số hai sẽ khiến toàn thể giới sinh học đại dương phải dụi mắt hoài nghi! Nếu bạn bắt một con cá chép hay cá hồi thả xuống nước, chúng sẽ bơi lội tung tăng như gặp lại thiên đường. Nhưng nếu bạn nhốt một con Cá Thòi Lòi vào một lồng lưới kín chìm sâu dưới đáy nước tù đọng và không cho gã ngoi lên cạn, thì điều gì sẽ xảy ra?". Bố cục: Thí nghiệm y khoa đối chứng: BÊN TRÁI là chú cá vàng bơi tung tăng trong bể nước trong suốt; BÊN PHẢI là chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) bị nhốt trong lồng dưới nước đang ôm cổ ho sặc sụa; KHÔNG có chú cá thòi lòi trong cảnh này.
```
</details>

<details><summary>L09b</summary>

```text
Mangrove Impressionist Gouache & Satirical Field Diary style, muddy olive green and ochre tones, fluid gouache brushstrokes, hand-annotated field diary aesthetic, sharp contours, textured creamy watercolor paper background: chú cá thòi lòi hoạt hình bị nhốt trong một chiếc lồng lưới sắt chìm sâu dưới đáy nước đục, biểu cảm hốt hoảng ôm cổ họng ngạt thở vì không được ngoi lên mặt nước hít thở không khí.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gã sẽ ngạt thở và chết đuối như một con người thực thụ!". Bố cục: Bảng cảnh báo y khoa: Hình ảnh chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) bị ngạt thở dưới đáy nước sâu; chiếc đồng hồ cát đếm ngược hiển thị nguy cơ ngạt khí; bác sĩ cú mèo đeo kính lão, mặc áo blouse trắng cầm ống nghe và bảng chẩn đoán giơ tay cảnh báo khẩn cấp.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nguyên nhân y khoa nằm ở cấu tạo hệ hô hấp đã bị thoái hóa mang trầm trọng của Bệnh nhân chán biển! Trong quá trình tiến hóa hơn 300 triệu năm, các lá mang dưới nước của gã đã teo nhỏ và dính chặt vào nhau, không còn đủ diện tích tiếp xúc để lọc đủ oxy hòa tan trong nước như các loài cá thông thường.". Bố cục: Phim chụp X-quang mang cá: Mô hình mang cá của chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) teo nhỏ xíu dính chặt vào nhau; mũi tên đỏ chỉ vào diện tích tiếp xúc kém; bác sĩ cú mèo đeo kính lão, mặc áo blouse trắng cầm ống nghe và bảng chẩn đoán cầm kính lúp chỉ vào phim X-quang.
```
</details>

<details><summary>L11b</summary>

```text
Mangrove Impressionist Gouache & Satirical Field Diary style, muddy olive green and ochre tones, fluid gouache brushstrokes, hand-annotated field diary aesthetic, sharp contours, textured creamy watercolor paper background: sơ đồ giải phẫu phóng đại chiếc mang cá thòi lòi bị thoái hóa: các lá mang teo tóp dính bẹp vào nhau so sánh với mang cá chép xòe rộng đỏ tươi, có thước đo y khoa đánh dấu cảnh báo thoái hóa nghiêm trọng.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để sinh tồn trên cạn, gã đã phát triển một công nghệ hô hấp lưỡng cư thần sầu: Lớp da nhầy của gã chứa mạng lưới mao mạch nước màu dày đặc, kết hợp với niêm mạc ẩm ướt trong vòm họng.". Bố cục: Sơ đồ giải phẫu hô hấp da: Lớp da nhầy của chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) phát sáng màu xanh dương rực rỡ; các phân tử oxy ngoài không khí thẩm thấu trực tiếp qua da và niêm mạc vòm họng vào mạch nước màu.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn bộ bề mặt da và cổ họng của gã hấp thụ trực tiếp từ 50-60% lượng oxy từ không khí ngoài trời! Ủa bác sĩ ơi, thế lúc gã leo lên bờ cát khô queo thì hai cái mang cá dùng để làm gì ạ?". Bố cục: Cận cảnh dòng nước màu giàu dưỡng khí: Các hạt oxy màu xanh ngọc bích từ không khí tràn qua màng da ẩm ướt, biến dòng nước màu đỏ thẫm thành đỏ tươi tràn đầy sinh lực; chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) tươi cười rạng rỡ.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chú cá con hỏi câu hỏi trúng ngay điểm mười sinh học!". Bố cục: Phòng học giải phẫu sinh vật: cô y tá thỏ trắng tai cụp đeo mũ chữ thập đỏ và chú còng gió nhỏ giơ hai càng cười nhe răng đứng cạnh chiếc bảng phấn vẽ hình mang cá, mắt chớp chớp ngơ ngác khó hiểu.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hai nắp mang phồng to của Cá Thòi Lòi không dùng để thở nước, mà dùng làm hai chiếc bình giữ nước di động! Trước khi trèo lên cạn, gã hớp một ngụm nước thật đầy nhốt chặt trong khoang mang đóng kín bưng.". Bố cục: Cận cảnh hai má phồng to: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) phồng hai má to như hai quả bóng nước, nhốt chặt ngụm nước trong nắp mang đóng kín bưng; các bọt nước lấp lánh giữ ẩm sợi mang.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lượng nước dự trữ này liên tục làm ẩm các sợi mang mỏng manh, giúp gã lang thang trên bờ hàng giờ liền mà không sợ bị khô mang!". Bố cục: Bình dưỡng khí di động: Hai khoang mang của chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) đóng vai trò như hai bình nước dã ngoại; chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) đeo kính râm đi dạo trên bờ cát nắng chói mà mang vẫn ướt sũng mát rượi.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thậm chí trong khoang miệng của gã, hệ thống van niêm mạc hoạt động như một nắp van cao su chống trào ngược. Bất kể gã lộn nhào hay nhảy cao trên bùn lầy, ngụm nước quý giá trong má vẫn không hề bị rỉ ra ngoài một giọt!". Bố cục: Cơ chế van cao su chống trào ngược: Cắt lớp miệng cá thòi lòi; nắp van niêm mạc khóa chặt cổ họng; giọt nước trong má không hề rỉ ra dù chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) đang lộn nhào biểu diễn.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một công nghệ khóa kín nước dã ngoại đỉnh cao của thế giới cá!". Bố cục: Vũ điệu nhào lộn trên bùn: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) lộn nhào trên không trung, hai má phồng tròn nước vẫn nguyên vẹn; chú còng gió nhỏ giơ hai càng cười nhe răng giơ hai càng vỗ tay tán thưởng cuồng nhiệt.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc biệt hơn nữa, chiếc đuôi của bệnh nhân này còn có khả năng hô hấp phụ trợ vô cùng độc đáo! Khi ngồi phơi nắng trên rễ cây, gã thường thả lỏng chóp đuôi nhúng ngập trong vũng nước bên dưới. Lớp biểu bì đuôi siêu mỏng có thể trao đổi khí liên tục, vừa làm mát cơ thể vừa bơm thêm dưỡng khí cho nước màu!". Bố cục: Góc thư giãn bãi lầy: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) ngồi vắt vẻo trên rễ cây khô, thả lỏng chóp đuôi nhúng ngập trong vũng nước bùn mát rượi; các tia dưỡng khí lấp lánh chạy dọc từ đuôi lên lưng.
```
</details>

<details><summary>L19b</summary>

```text
Mangrove Impressionist Gouache & Satirical Field Diary style, muddy olive green and ochre tones, fluid gouache brushstrokes, hand-annotated field diary aesthetic, sharp contours, textured creamy watercolor paper background: chú cá thòi lòi hoạt hình ngồi vắt vẻo trên rễ cây đước phơi nắng, chóp đuôi thả lỏng nhúng sâu vào vũng nước trong veo bên dưới với hiệu ứng bọt khí oxy phát sáng thẩm thấu qua da đuôi.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một sự thích nghi lưỡng thê hoàn hảo đến mức khiến các loài bò sát cũng phải ngả mũ bái phục!". Bố cục: Hội đồng bò sát thán phục: Một chú kỳ đà và một chú rùa ngồi dưới tán cây ngả mũ chào chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) đang thong thả thở bằng chóp đuôi trên rễ đước.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bây giờ, hãy đeo kính lúp phóng đại để kiểm tra vùng mặt kỳ dị nhất hành tinh của Bệnh nhân chán biển! Cá thông thường sinh ra vốn dĩ không có mí mắt, và mắt của chúng nằm cố định hai bên má.". Bố cục: Góc nghiên cứu nhãn khoa: Mô hình hộp sọ cá thòi lòi bằng thạch cao; hai nhãn cầu lồi to tướng đặt trên giá đỡ đo đạc; KHÔNG có chú cá thòi lòi trong cảnh này; ánh nắng chói chang chiếu rọi gay gắt.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng Cá Thòi Lòi lại sở hữu đôi mắt lồi nhô cao hẳn lên đỉnh đầu như hai quả bóng bàn đồ chơi!". Bố cục: Đôi mắt kính tiềm vọng: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) lặn dưới vũng bùn chỉ thò đúng hai nhãn cầu mắt lồi to tướng lên khỏi mặt bùn như hai kính tiềm vọng tàu ngầm quét bốn phương; KHÔNG có chú cá thòi lòi trong cảnh này.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vì sống trên cạn giữa cái nắng gay gắt 30 lăm đến 40°C của rừng ngập mặn nhiệt đới, đôi mắt của gã đối mặt với nguy cơ bị khô giác mạc và mù lòa bất cứ lúc nào. Nhưng gã không hề có tuyến nước mắt! Vậy gã giải quyết bài toán chống khô mắt này như thế nào?". Bố cục: Thời tiết khắc nghiệt: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) đứng giữa bãi bùn nắng gắt chiếu rọi, chiếc nhiệt kế cắm cạnh chỉ 40°C; hai mắt lồi toát mồ hôi lo sợ bị khô mắt.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gã co rút cơ mặt, kéo tụt cả hai nhãn cầu mắt lặn sâu xuống bên trong hốc đầu! Phía dưới đáy hốc mắt có một chiếc túi chứa nước dịch ẩm ướt.". Bố cục: Khoảnh khắc kỳ thú thụt mắt: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) co cơ kéo tụt cả hai nhãn cầu mắt lặn sâu xuống bên trong đầu, biến mất khỏi đỉnh sọ; dưới đáy hốc mắt có chiếc túi nước bôi trơn nhãn cầu sáng loáng.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi khi gã thụt mắt xuống, nhãn cầu được nhúng ngập trong bể nước làm ẩm tức thì, rồi lại ngoi bật lên sáng long lanh như vừa được tra thuốc nhỏ mắt!". Bố cục: Cú tra thuốc nhỏ mắt tự nhiên: Hai nhãn cầu mắt ngoi bật trở lại đỉnh đầu sáng long lanh như hai viên ngọc; chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) chớp mắt lia lịa khoái chí.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng phát hiện chấn động vừa được nhóm nghiên cứu của tiến sĩ Michel công bố trên Tạp chí Sinh học Thực nghiệm: Cú thụt mắt này còn kiêm luôn chức năng nuốt thức ăn!". Bố cục: Phòng thí nghiệm quốc tế: Nhóm nhà khoa học hoạt hình đang reo hò trước màn hình máy quay siêu chậm ghi lại khoảnh khắc cá thòi lòi đớp mồi trên bùn; KHÔNG có chú cá thòi lòi trong cảnh này.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vì sống trên cạn nên Cá Thòi Lòi không thể dùng dòng nước xoáy để cuốn mồi vào bụng như cá dưới biển, và lưỡi của gã cũng không có cơ bắp linh hoạt như ếch nhái.". Bố cục: Thách thức nuốt mồi không có nước: So sánh một chú cá biển hút dòng nước nuốt mồi với chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) đứng trơ trên cạn lưỡi ngắn cũn không cơ bắp; KHÔNG có chú cá thòi lòi trong cảnh này.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi khi đớp được một chú còng gió hay bọ gậy trên bùn, gã đồng thời thụt mạnh cả hai nhãn cầu mắt thụt sâu xuống vòm miệng!". Bố cục: Cơ chế pit-tông nuốt mồi: Cắt lớp miệng chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C); hai đáy nhãn cầu tụt sâu xuống ép chặt vòm miệng, đẩy chú còng gió trôi tuột xuống thực quản; mặt chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) chớp mắt đầy thỏa mãn.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đáy nhãn cầu đóng vai trò như một chiếc pit-tông cơ khí ép chặt xuống khoang họng, đẩy phăng con mồi trôi tuột xuống thực quản!". Bố cục: Mô hình pit-tông cơ khí: Hình vẽ kỹ thuật minh họa hai nhãn cầu đóng vai trò như hai xi-lanh pit-tông máy nén ép thức ăn trôi thẳng vào dạ dày; KHÔNG có chú cá thòi lòi trong cảnh này.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nghĩa là trên đời này, chỉ có duy nhất loài cá thòi lòi là nuốt mồi bằng chính đôi mắt của mình!". Bố cục: Kỳ quan nuốt mồi bằng mắt: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) xoa bụng no tròn, giơ ngón tay cái cười tự hào; phía sau là tấm biển NUỐT MỒI BẰNG ĐÔI MẮT ĐỘC NHẤT VÔ NHỊ.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa dừng lại ở đó, đôi mắt lồi này còn là hệ thống radar cảnh giới 360° hoàn hảo! Một mắt có thể nhìn chăm chú xuống bùn để rình mồi, trong khi mắt kia ngước ngược lên trời để canh chừng chim bói cá săn mồi.". Bố cục: Hệ thống radar 360 độ: Hình tròn tầm nhìn quét toàn cảnh; một mắt của chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) soi xuống bãi bùn thấy chú sâu béo ngậy, mắt kia ngước lên trời thấy bóng chim bói cá lượn lờ.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bất kỳ kẻ thù nào lọt vào bán kính 3 mét đều bị gã phát hiện trong tích tắc!". Bố cục: Cảnh giới tối cao: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) phát hiện chim bói cá từ xa 3 mét, lập tức cúi rạp người chuẩn bị tẩu thoát; radar trên đầu nhấp nháy đèn xanh an toàn.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy chuyển sang kiểm tra hệ cơ xương vận động của bệnh nhân số 42! Nếu bạn quan sát kỹ cặp vây ngực của Cá Thòi Lòi, bạn sẽ kinh ngạc nhận ra đây hoàn toàn không phải là những nan vây quạt nước mỏng manh của loài cá biển.". Bố cục: Bản vẽ giải phẫu vây ngực: Sơ đồ xương vây ngực có khớp khuỷu tay và bó cơ vận động giống hệt cánh tay người; KHÔNG có chú cá thòi lòi trong cảnh này; bên cạnh là chiếc thước đo góc xoay.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cấu trúc xương bên trong đã tiến hóa thành các khớp xương khuỷu tay và cơ bắp bám chắc chắn!". Bố cục: So sánh khớp xương: BÊN TRÁI nan vây mỏng manh của cá trích; BÊN PHẢI vây ngực cơ bắp có khớp khuỷu tay của chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C); mũi tên chỉ vào bó cơ nâng đỡ trọng lượng cơ thể.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cặp vây ngực này có thể xoay gập linh hoạt, cho phép Bệnh nhân chán biển chống hai tay xuống bùn rồi đẩy toàn bộ trọng lượng cơ thể tiến về phía trước theo nhịp điệu nhịp nhàng như một anh lính bò trườn!". Bố cục: Hành trình việt dã trên bùn: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) chống hai vây ngực xuống bùn bước đi mạnh mẽ như chú vượn con; dưới bụng lộ rõ chiếc đĩa hút tròn xoe bám dính trên rễ cây.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dưới bụng của gã còn có một chiếc đĩa hút hình thành từ hai vây bụng dính liền nhau, tạo lực bám dính chắc nịch trên những thân cây đước trơn trượt! Bác sĩ ơi, em thấy nó co đuôi một phát là bay vèo qua mặt em xa tít mù tắp luôn á bác sĩ!". Bố cục: Cận cảnh đĩa hút bụng: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) treo ngược người dưới cành cây đước nhờ chiếc đĩa hút bụng dính chặt như giác hút cao su; hai tay vẫy chào bác sĩ cú mèo đeo kính lão, mặc áo blouse trắng cầm ống nghe và bảng chẩn đoán.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bé con vừa chứng kiến tuyệt kỹ búng đuôi thần sầu của gã đấy! Khi cần tẩu thoát khỏi chim bói cá hay kỳ đà đói khát, Cá Thòi Lòi gập cong chiếc đuôi cơ bắp hình chữ C rồi bung mạnh như một chiếc lò xo thép!". Bố cục: Cú nhảy lò xo ngoạn mục: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) gập cong đuôi hình chữ C búng mạnh bay vút lên không trung; vệt nước bắn tung tóe phía sau; thước đo khoảng cách ghi 1 mét.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cú phóng này hất tung gã bay xa gấp 4 lần chiều dài cơ thể, tương đương cú nhảy xa gần 1 mét trên mặt bùn lầy lội!". Bố cục: Bay trên mặt bùn lầy: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) lượn một đường parabol trên không trung qua đầu chú còng gió nhỏ giơ hai càng cười nhe răng; chú còng gió nhỏ giơ hai càng cười nhe răng ngước nhìn há hốc mồm kinh ngạc.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vào mùa giao phối, tuyệt kỹ nhảy xa này biến thành màn biểu diễn võ thuật đường phố đỉnh cao! Các chàng cá thòi lòi dựng đứng vây lưng sặc sỡ như những lá cờ chiến, há to miệng thị uy rồi bật nhảy liên tục trên không trung để tranh giành lãnh thổ và thu hút các nàng cá mái.". Bố cục: Vũ đài tình yêu bãi bùn: Hai chú cá thòi lòi đực bật nhảy cao trên không trung, vây lưng giương cao sặc sỡ như cánh buồm ngũ sắc, miệng há to thị uy; một nàng cá mái ngồi dưới tán cây vỗ vây tán thưởng.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kẻ nào nhảy cao hơn và có vây lưng lòe loẹt hơn sẽ làm bá chủ bãi lầy!". Bố cục: Bá chủ bãi lầy ngập mặn: Chú cá thòi lòi đực chiến thắng giương vây cờ ngũ sắc đứng trên đỉnh cồn bùn, đeo vòng nguyệt quế; các đối thủ cúi đầu thần phục.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một con cá dài 20cm nhưng vừa biết chạy bộ, vừa biết leo cây, vừa biết nhảy xa bay trên không trung!". Bố cục: Huy chương vàng Olympic điền kinh: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) đứng trên bục vinh quang số 1 đeo huy chương vàng môn điền kinh phối hợp leo cây chạy bộ nhảy xa; khán giả vỗ tay cuồng nhiệt.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu đem so tỷ lệ cơ thể với các vận động viên điền kinh Olympic, thành tích bay nhảy của bệnh nhân này đủ sức giật huy chương vàng môn nhảy xa phối hợp!". Bố cục: So sánh tỷ lệ vận động viên: Biểu đồ so sánh tỷ lệ nhảy xa của chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) với vận động viên Olympic; mũi tên chỉ số thành tích vượt trội; KHÔNG có chú cá thòi lòi trong cảnh này.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chẩn đoán bệnh án cuối cùng dẫn chúng ta xuống lòng đất ngầm của bãi lầy ngập mặn! Khi mùa sinh sản đến, Bệnh nhân chán biển không hề đẻ trứng trôi nổi vô trách nhiệm trên mặt nước để làm mồi cho cá lớn.". Bố cục: Mặt cắt địa đạo bùn ngập mặn: Sơ đồ hang bùn hình chữ Y sâu 2 mét dưới đáy lầy; các nhánh hang ngoằn ngoèo có tháp bùn tròn bảo vệ miệng hang; KHÔNG có chú cá thòi lòi trong cảnh này.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gã dùng chính chiếc miệng của mình cạp từng búng bùn đất ngậm nhổ ra ngoài để đào một công trình địa đạo ngầm hình chữ Y sâu tới 2 mét!". Bố cục: Công trường xây dựng ngầm: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) miệng ngậm từng búng bùn đất ngoi lên nhổ ra ngoài bờ, đào sâu địa đạo hình chữ Y kiên cố.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để miệng hang không bị sạt lở khi thủy triều dâng lên, gã còn khéo léo đắp những ụ bùn tròn xung quanh miệng hang như những tháp canh pháo đài mini.". Bố cục: Pháo đài chắn thủy triều: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) khéo léo đắp ụ bùn tròn xoe xung quanh miệng hang như tháp canh thành quách chắn sóng triều dâng; KHÔNG có chú cá thòi lòi trong cảnh này.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đáy hang ngập ngụa trong nước bùn yếm khí hoàn toàn không có một phân tử oxy nào hòa tan. Nếu trứng cá đẻ ở đây, trứng sẽ thối rữa và chết ngạt tức thì.". Bố cục: Nguy cơ yếm khí đáy bùn: Đáy hang tối đen ngập nước không có oxy; các bọt khí yếm khí độc hại bao quanh; hình ảnh nguy hiểm cho trứng cá; KHÔNG có chú cá thòi lòi trong cảnh này.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng chú cá thòi lòi bố đã giải quyết thảm họa này bằng một kỳ tích kỹ thuật ngầm khiến các nhà khoa học Nhật Bản phải kinh ngạc!". Bố cục: Kỳ tích kỹ thuật ngậm khí: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) ngoi lên mặt cạn há to miệng ngậm một búng không khí căng phồng hai má, chuẩn bị lặn ngược xuống đáy hang sâu.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gã bơi lên mặt cạn, há to miệng đớp một búng không khí căng tràn rồi lặn ngược xuống đáy hang sâu 2 mét nhả vào một căn phòng phụ trên trần hang!". Bố cục: Chuyến xe buýt con thoi ngậm khí: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) lặn sâu xuống đáy hang 2 mét, nhả búng không khí vào căn phòng phụ trên trần hang tối.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gã miệt mài thực hiện hàng trăm chuyến bơi con thoi ngậm không khí như một chú thợ lặn cần mẫn, cho đến khi tạo ra một chiếc túi khí ngầm lơ lửng dưới lòng bùn! Nàng cá mẹ dán hàng ngàn quả trứng lên trần phòng túi khí khô ráo giàu dưỡng khí này.". Bố cục: Căn phòng túi khí ngầm: Dưới đáy hang bùn, một túi khí trong suốt lơ lửng trên trần hang; hàng ngàn quả trứng cá nhỏ bám trên trần sáng lấp lánh; chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) bơi quanh canh gác với ánh mắt trìu mến.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Suốt nhiều tuần lễ ấp trứng, cá bố liên tục thay phiên tuần tra canh giữ cửa hang và lặn xuống thay mới túi khí, cho đến khi đàn cá con nở ra khỏe mạnh!". Bố cục: Đàn cá con chào đời: Hàng trăm chú cá thòi lòi con mắt tí hon bơi lội quanh túi khí ngầm trong hang; chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) ông bố cần mẫn tươi cười vẫy chào đàn con.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hồ sơ bệnh án số 42 chính thức hoàn tất với kết luận chẩn đoán: Cá Thòi Lòi hoàn toàn khỏe mạnh và là một tuyệt tác chuyển giao sinh học vĩ đại!". Bố cục: Bức tranh chuyển giao lịch sử: Cây phả hệ tiến hóa sinh học; chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) đứng ở mắt xích trung tâm chuyển giao giữa cá dưới biển và động vật bốn chân trên cạn cách đây 300 triệu năm; ánh hào quang chiếu rọi.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gã là hình bóng sống động của tổ tiên bốn chân xa xưa cách đây 300 triệu năm, những sinh vật dũng cảm đầu tiên dám thò đầu ra khỏi biển cả tăm tối để chinh phục lục địa khô cằn!". Bố cục: Tổ tiên bốn chân chinh phục đất liền: Hình ảnh tái hiện cách đây 300 triệu năm, những sinh vật đầu tiên dũng cảm thò đầu lên khỏi biển cả bước đi trên bùn lầy; KHÔNG có chú cá thòi lòi trong cảnh này.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đôi khi trong cuộc sống, bạn có thể bị người đời chê cười là kẻ dở dở ương ương, không giống ai và không thuộc về một khuôn mẫu nào: Nhưng hãy nhớ tới chú cá thòi lòi!". Bố cục: Hình ảnh ẩn dụ truyền cảm hứng: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) tươi cười tự tin đứng trên mỏm đá ngập mặn, một vây vẫy chào biển cả, một vây chỉ về phía đất liền rộng lớn đầy nắng ấm.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chính sự khác biệt nửa nạc nửa mỡ, dám bơi ngược dòng quy chuẩn và mở lối đi riêng mới là khởi đầu cho những bước nhảy vọt tiến hóa vĩ đại nhất của lịch sử!". Bố cục: Con đường tiên phong mở lối: Dấu chân vây cá của chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C) in dài trên bãi bùn hướng về ánh bình minh rạng rỡ; biểu tượng của sự kiên định khác biệt.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu được sinh ra với một siêu năng lực kỳ lạ của cá thòi lòi, bạn muốn sở hữu đôi mắt xoay 360° thụt nuốt mồi hay cặp tay leo cây chạy bộ trên bùn? Hãy để lại bình luận chẩn đoán của bạn bên dưới nhé!". Bố cục: Tương tác người xem: bác sĩ cú mèo đeo kính lão, mặc áo blouse trắng cầm ống nghe và bảng chẩn đoán cùng cô y tá thỏ trắng tai cụp đeo mũ chữ thập đỏ và chú còng gió nhỏ giơ hai càng cười nhe răng đứng bên cạnh chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C), cùng chỉ tay vào chiếc bảng bình luận nhấp nháy chữ Chẩn đoán của bạn.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn bây giờ, hãy chuẩn bị tinh thần bước vào phiên tòa xét xử rùng rợn của hồ sơ số 43!". Bố cục: Cận cảnh hình bóng teaser tập 43 (TASTE-68): Trong phòng phẫu thuật tối mờ kỳ bí, một cái bóng đen bí ẩn (solid black silhouette) hình con ong bắp cày với chiếc kim tiêm nhọn hoắt sau lưng gắn dấu hỏi '?', phía trước là bóng một con gián đang ngoan ngoãn cúi đầu bước đi như xác sống.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một kẻ sát nhân khoác tấm áo choàng ngọc bích lấp lánh, một bác sĩ phẫu thuật thần kinh tàn độc chuyên thực hiện ca châm kim vi phẫu chuẩn xác đến từng mi-li-mét vào hạch não của loài gián, tước đoạt toàn bộ ý chí tự do và biến nạn nhân thành một xác sống Zombie ngoan ngoãn tự đi vào mồ chôn! Bạn có biết sát thủ ngọc bích này là ai không?". Bố cục: Poster đóng dấu hồ sơ 43: Chữ TẬP 43 phát sáng xanh ngọc bích trên nền tím than; bóng đen sát thủ ngọc bích cầm kim tiêm laser; KHÔNG có chú cá thòi lòi trong cảnh này.
```
</details>

<details><summary>L57b</summary>

```text
Mangrove Impressionist Gouache & Satirical Field Diary style, muddy olive green and ochre tones, fluid gouache brushstrokes, hand-annotated field diary aesthetic, sharp contours, textured creamy watercolor paper background: poster nghệ thuật hé lộ sát thủ tập tiếp theo: một chú ong bắp cày ngọc lục bảo phát sáng lấp lánh đang dùng chiếc kim châm vi phẫu đâm chuẩn xác vào hạch não chú gián khổng lồ biến thành zombie ngoan ngoãn.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bạn có tin trên đời có một con cá nếu bị ép ở dưới nước quá lâu thì sẽ bị... chết đuối?". Bố cục: Cận cảnh mở đầu: chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn ngồi trên tảng bùn ướt, hai mắt lồi to tướng chớp chớp thụt xuống đầu rồi ngoi lên, miệng ngậm cọng cỏ cười toe toét nhìn thẳng vào người xem.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đây là Cá Thòi Lòi, loài cá chán biển lên cạn sống rải rác khắp các cánh rừng ngập mặn! Mang của gã đã bị thoái hóa nặng, nhưng bù lại gã hô hấp trực tiếp qua da và vòm họng ẩm ướt để hấp thụ hơn 50% lượng oxy ngoài trời.". Bố cục: chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn hai tay chống bùn đi lại như một chú vượn con, hai má phồng to như hai quả bóng nước tròn phúng phính.
```
</details>

<details><summary>S02b</summary>

```text
HÌNH DỌC 9:16, Mangrove Impressionist Gouache & Satirical Field Diary style, muddy olive green and ochre tones, fluid gouache brushstrokes, hand-annotated field diary aesthetic, sharp contours, textured creamy watercolor paper background: chú cá thòi lòi hoạt hình há to miệng khoe vòm họng ẩm ướt phát sáng các hạt oxy, toàn bộ bề mặt da ẩm ướt đang hấp thụ khí trời với mũi tên chỉ số 50% OXY nổi bật.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Để không bị khô mang, gã hớp đầy nước vào hai má phồng to như hai bình dưỡng khí di động!". Bố cục: Cận cảnh hai má phồng to: Dòng nước mát lấp lánh trong khoang mang giữ ẩm cho các lá mang nhỏ xíu.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Chưa hết, cặp vây ngực của gã biến tính thành hai cánh tay có khớp khuỷu để chống bùn chạy bộ và leo thoăn thoắt lên rễ cây đước.". Bố cục: chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn đang dùng hai vây ngực leo thoăn thoắt lên rễ cây đước ngoằn ngoèo, miệng huýt sáo ngắm cảnh bãi lầy.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Nhưng dị nhất là đôi mắt lồi trên đỉnh sọ: Mỗi khi đớp mồi trên cạn, gã co cơ kéo tụt cả hai nhãn cầu mắt xuống cổ họng để làm chiếc pit-tông ép thức ăn trôi xuống dạ dày,". Bố cục: Khoảnh khắc nuốt mồi kinh điển: chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn đớp chú bọ gậy, hai nhãn cầu mắt kéo tụt sâu xuống đầu làm pit-tông ép mồi trôi tuột xuống cổ họng.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "vừa làm ẩm mắt vừa". Bố cục: chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn chớp mắt long lanh sau cú nuốt mồi, xoa bụng no tròn mãn nguyện.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "nuốt mồi trong tích tắc!". Bố cục: Hình ảnh kết thúc: chú cá thòi lòi hoạt hình mắt lồi to tướng, hai vây ngực như hai tay, da lấm bùn co đuôi búng nhảy vút lên không trung với nụ cười rạng rỡ, giơ hai ngón tay cái chào tạm biệt khán giả.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/57 của video YouTube về Cá Thòi Lòi). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C). Nhân vật phụ cố định: bác sĩ cú mèo đeo kính lão, mặc áo blouse trắng cầm ống nghe và bảng chẩn đoán; cô y tá thỏ trắng tai cụp đeo mũ chữ thập đỏ; chú còng gió nhỏ giơ hai càng cười nhe răng. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/7 của video YouTube Shorts về Cá Thòi Lòi). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú cá thòi lòi hoạt hình hài hước ngộ nghĩnh (màu nâu xám lấm lem bùn đất, hai mắt lồi to tướng tròn xoe trên đỉnh sọ có thể xoay đảo độc lập ngơ ngác, đôi vây ngực cơ bắp như hai cánh tay búp bê, bụng có đĩa hút, đuôi cong chữ C). Nhân vật phụ: chú còng gió nhỏ giơ hai càng cười nhe răng. 
```
</details>

## 7. SEO

- **title:** Cá Thòi Lòi: Con Cá Chết Đuối Dưới Nước & Bí Thuật Thụt Mắt Nuốt Mồi | Tập 42
- **hook_paragraph:** Loài cá kỳ dị nhất hành tinh: Cá Thòi Lòi (Periophthalmus). Mang thoái hóa khiến gã thở bằng da và ngậm nước trong má để đi dạo trên cạn, vây ngực biến thành đôi tay leo trèo rễ cây, và đôi mắt lồi biết thụt xuống họng làm pit-tông nuốt mồi!
- **question:** Nếu được chọn một tuyệt kỹ của Cá Thòi Lòi, bạn chọn mắt xoay 360 độ thụt nuốt mồi hay đôi tay leo cây chạy bộ? Bình luận bên dưới nhé!
- **next_teaser:** Tập 43: Sát thủ phẫu thuật não châm kim biến gián thành xác sống Zombie ngoan ngoãn tự đi vào huyệt mộ!
- **shorts_title:** Con Cá Chết Đuối Dưới Nước Và Thụt Mắt Để Nuốt Mồi?! 🐟👀 #độngvật #cáthòilòi
- **shorts_desc:** Loài cá chán biển leo trèo cây đước, thở bằng da ngậm nước trong má và dùng đôi mắt thụt xuống họng làm pit-tông nuốt mồi!

#độngvật #cáthòilòi #VẽChuyệnHoangDã
- **bullets:** Bệnh án số 1: Con cá chán biển lên cạn đi dạo và leo trèo như vượn · Bệnh án số 2: Nghịch lý cá chết đuối dưới nước vì mang teo nhỏ · Bệnh án số 3: Tuyệt kỹ co cơ thụt nhãn cầu mắt xuống họng để nuốt mồi · Bệnh án số 4: Cặp vây ngực tiến hóa thành hai cánh tay chống bùn nhảy xa · Bệnh án số 5: Kỳ tích đào hang ngầm sâu 2 mét và bơm túi khí nuôi trứng
- **tags:** cá thòi lòi, mudskipper, periophthalmus, thế giới động vật, vẽ chuyện hoang dã, khoa học kỳ thú, whiteboard animation, động vật kỳ lạ
- **hashtags:** #độngvật #cáthòilòi #VẽChuyệnHoangDã

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-42-ca-thoi-loi
python src/episode/pipeline.py tts    projects/tap-42-ca-thoi-loi     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-42-ca-thoi-loi     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-42-ca-thoi-loi     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-42-ca-thoi-loi              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-42-ca-thoi-loi --force
python scripts/beat_sheet.py projects/tap-42-ca-thoi-loi               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-42-ca-thoi-loi/audio/shorts.wav projects/tap-42-ca-thoi-loi/renders/tap-42-ca-thoi-loi_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-42-ca-thoi-loi
python src/episode/pipeline.py seo    projects/tap-42-ca-thoi-loi
python src/episode/episode_doc.py     projects/tap-42-ca-thoi-loi
```

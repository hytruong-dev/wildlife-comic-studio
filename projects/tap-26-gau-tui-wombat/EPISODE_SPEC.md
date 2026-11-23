# TẬP 26 — GẤU TÚI WOMBAT · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-26-gau-tui-wombat`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-26-gau-tui-wombat`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F2` · **Persona giọng:** `ky_su_vu_khi` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Gấu Túi Wombat |
| Tiêu đề YouTube | Cỗ Xe Tăng Nước Úc Có Mông Bọc Thép & Đi Vệ Sinh Ra Hình Lập Phương?! |
| Video dài | `renders/tap-26-gau-tui-wombat_long.mp4` — 8:49.5 (529.5s) |
| Shorts | `renders/tap-26-gau-tui-wombat_shorts.mp4` — 0:50.9 (50.9s) |
| Thumbnail | `renders/tap-26-gau-tui-wombat_thumbnail.jpg` |
| Số hình | dài 56 beat / 56 ảnh riêng; Shorts 10 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/56 của video YouTube về Gấu Túi Wombat). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng. Nhân vật phụ cố định: người kỹ sư trưởng hoạt hình mặc áo phản quang cam cầm bản vẽ kỹ thuật cuộn tròn và thước đo; cô trợ lý kỹ thuật hoạt hình mặc áo phản quang vàng; chú chó hoang Dingo lông vàng hung dữ răng nanh nhọn hoắt nhưng bị bầm dập hài hước. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — CHIẾN XA ĐÀO HẦM NẶNG 35KG CỦA NƯỚC ÚC
*Badge:* `HỒ SƠ VŨ KHÍ` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene01_p0.wav` (437 ký tự) · mood `hao_hung`

```text
Hồ sơ mật cấp độ đỏ. Mở khóa dữ liệu kỹ thuật! Toàn thể đội kỹ thuật tập trung trước màn hình mô phỏng ba đê. Hôm nay chúng ta giải mã một trong những bản thiết kế cơ khí sinh học kỳ dị và thực dụng bậc nhất của giới tự nhiên nước Úc: một cỗ máy đào hầm sống nặng từ hai mươi lăm đến ba mươi lăm ki-lô-gam, thân hình lùn tịt tròn quay như thùng rượu, nhưng sở hữu lớp giáp phòng ngự phía sau khiến cả loài chó hoang Đin-gô phải gãy răng!
```
**Part 1** → `audio/vs/scene01_p1.wav` (137 ký tự) · 🎭 cameo `phat_thanh_vien`

```text
Báo cáo chỉ huy, radar ghi nhận mục tiêu đang di chuyển với tốc độ bất thường, nhìn như cục đá biết đi nhưng đào hầm nhanh ngang máy xúc!
```
**Part 2** → `audio/vs/scene01_p2.wav` (536 ký tự) · mood `hao_hung`

```text
[surprise-oh] Báo cáo rất chuẩn xác! Xin giới thiệu với cả đội: đây là Gấu Túi Uôm-bát, thú có túi đặc hữu của châu Đại Dương, họ hàng thân cận nhất của loài Cô-a-la ôm cây. Nhưng khác với người anh em Cô-a-la suốt ngày ngủ gật ngơ ngác, sinh vật này được trang bị đầy đủ bộ giáp công thủ toàn diện: hàm răng mọc dài liên tục đục thủng rễ cây, móng vuốt xẻng đào hầm xuyên qua đất đá, và chiếc mông bọc thép dày cộp hoạt động như một tấm khiên chống đạn! Trong phòng thiết kế, chúng tôi gọi thẳng tên nó bằng biệt danh: Xe Tăng Đào Hầm!
```
**Part 3** → `audio/vs/scene01_p3.wav` (364 ký tự) · mood `nghiem_trang_gia`

```text
Chưa dừng lại ở đó, cỗ xe tăng này còn nắm giữ một kỷ lục vô tiền khoáng hậu khiến các kỹ sư thủy lực và vật lý học toàn cầu phải ôm đầu thán phục: sinh vật duy nhất trên hành tinh có khả năng đúc ra những khối phân vuông vức hình lập phương chuẩn xác đến từng góc cạnh! Đêm nay, tôi mời toàn đội cùng mổ xẻ bốn module kỹ thuật tối mật trên cơ thể Xe Tăng Đào Hầm!
```

### scene02 — TẤM KHIÊN MÔNG BỌC THÉP 3CM VÀ TÚI MỞ NGƯỢC
*Thẻ chương:* TẤM KHIÊN MÔNG CHỊU MỌI CÚ CẮN CỦA DINGO

*Badge:* `BẢN VẼ CƠ KHÍ` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene02_p0.wav` (362 ký tự) · mood `hao_hung`

```text
Module kỹ thuật số một: Bản vẽ tấm khiên mông và kết cấu túi ngầm! Nhìn từ góc nhìn công trình, điểm hiểm yếu nhất của mọi cỗ máy đào hầm ngầm là phần đuôi phía sau: khi chúi đầu vào lòng đất đào bới, phần mông lộ ra ngoài sẽ là miếng mồi ngon cho bất kỳ kẻ săn mồi nào rình rập. Nhưng tạo hóa đã trang bị cho Xe Tăng Đào Hầm một giải pháp giáp đuôi không tưởng!
```
**Part 1** → `audio/vs/scene02_p1.wav` (411 ký tự) · mood `don_dap`

```text
Hãy quan sát mặt cắt giải phẫu vùng mông của Uôm-bát: phần đuôi của nó tiêu biến hoàn toàn chỉ còn một mấu cụt nhỏ xíu. Thay vào đó, toàn bộ vùng xương chậu và xương cụt được phủ một lớp mô mạc sợi dày từ hai đến ba xăng-ti-mét, đan kết chặt chẽ với các tấm sụn cứng cáp như thép tấm gia cường! Phía trên là lớp da siêu dày bọc lông rậm rạp, tạo thành một chiếc nắp cống sinh học bất khả xâm phạm! [surprise-wa]
```
**Part 2** → `audio/vs/scene02_p2.wav` (320 ký tự) · mood `hao_hung`

```text
Khi bị chó hoang Đin-gô truy đuổi ráo riết, Uôm-bát lập tức lao đầu vào cửa hang ngầm và... quay chiếc mông bọc thép ra ngoài để bịt kín miệng hang! Chó hoang lao tới cắn xé điên cuồng, nhưng hàm răng sắc nhọn chỉ cắn trúng tấm khiên sụn cứng trơn trượt, cắn mãi không xuyên thủng mà chỉ tổ mòn răng gãy móng! [laughter]
```
**Part 3** → `audio/vs/scene02_p3.wav` (495 ký tự) · mood `don_dap`

```text
Chưa hết, các kỹ sư hãy nhìn xuống vùng bụng của nó: là loài thú có túi giống chuột túi Canh-gu-ru, nhưng nếu cửa túi của chuột túi hướng lên trên, thì cửa túi của Uôm-bát lại quay ngược hoàn toàn về phía sau! [surprise-oh] Đây là giải pháp công học thiên tài: khi gã dùng hai bàn chân trước có móng vuốt thép cào đất tung tóe đào những đường hầm sâu hai mươi đến ba mươi mét, toàn bộ đất cát bắn ra phía sau mà không hề có một hạt bụi nào lọt vào túi làm nghẹt thở đứa con non bé nhỏ bên trong!
```
**Part 4** → `audio/vs/scene02_p4.wav` (449 ký tự) · mood `hao_hung`

```text
Phía trước đầu xe tăng còn được lắp đặt một cặp mũi khoan sinh học thượng hạng: bốn chiếc răng cửa to bản mọc dài liên tục suốt đời giống hệt loài gặm nhấm! Lớp men răng trước dày cứng cọ sát với lớp ngà mềm phía sau tạo thành lưỡi đục tự mài sắc bén, có thể gặm đứt phăng rễ cây bạch đàn cổ thụ và cắn thủng cả ống nhựa công trình của con người! Đầu là máy khoan mũi nhọn, đuôi là khiên thép chống đạn, đúng là cỗ máy đào công binh hoàn hảo kín kẽ!
```

### scene03 — 8% RUỘT GIÀ ĐÚC 100 KHỐI LẬP PHƯƠNG MỖI NGÀY
*Thẻ chương:* SINH VẬT DUY NHẤT ĐÚC ĐƯỢC HÌNH LẬP PHƯƠNG TỰ NHIÊN

*Badge:* `DÂY CHUYỀN ĐÚC` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene03_p0.wav` (403 ký tự) · mood `tram_bi_an`

```text
Module kỹ thuật số hai: Dây chuyền cơ học đúc phân hình khối lập phương! Đây là bí ẩn cơ học từng làm đau đầu giới khoa học suốt hàng thế kỷ. Mọi loài vật từ voi, bò, chim cho đến con người khi thải phân đều tạo ra hình trụ tròn hoặc khối dẹt elip do sự co thắt đồng tâm của cơ vòng hậu môn. Nhưng Xe Tăng Đào Hầm của chúng ta thì đi vệ sinh ra... những viên xúc xắc vuông chằn chặn có đủ sáu mặt phẳng!
```
**Part 1** → `audio/vs/scene03_p1.wav` (94 ký tự) · 🎭 cameo `co_tro_ly`

```text
Trời đất ơi chỉ huy ơi, có phải hậu môn của nó có hình vuông giống như khuôn làm bánh không ạ?
```
**Part 2** → `audio/vs/scene03_p2.wav` (362 ký tự) · mood `hao_hung`

```text
[laughter] Trợ lý đoán sai bét rồi nhé! Năm hai ngàn mười chín, nhóm nghiên cứu của tiến sĩ Pa-tri-xi-a Dăng tại Viện Công nghệ Georgia đã đưa một chú Uôm-bát vào máy chụp cắt lớp CT và đoạt luôn giải Nobel Vật lý I-gơ Nô-ben danh giá! Hậu môn của nó vẫn tròn xoe như mọi loài vật khác. Bí mật cơ khí thực sự nằm ở tám phần trăm chiều dài cuối cùng của ruột già!
```
**Part 3** → `audio/vs/scene03_p3.wav` (505 ký tự) · mood `don_dap`

```text
Trong công bố chi tiết trên tạp chí Soft Matter năm hai ngàn hai mươi mốt, các nhà vật lý phát hiện thành ruột già của Uôm-bát có tính đàn hồi không đồng nhất: có hai dải cơ cứng đối diện nhau và hai dải cơ mềm linh hoạt xen kẽ! Suốt hành trình tiêu hóa kéo dài hai tuần, chất xơ thô ráp được vắt kiệt nước và nén chặt lại. Khi khối chất thải đi qua đoạn ruột đặc biệt này, các đợt co bóp nhịp nhàng tác động lực ép khác nhau, nặn khối phân thành những cạnh sắc và bốn mặt phẳng đều tăm tắp! [surprise-wa]
```
**Part 4** → `audio/vs/scene03_p4.wav` (515 ký tự) · mood `hao_hung`

```text
Mỗi đêm, một chú Uôm-bát sản xuất đều đặn từ tám mươi đến một trăm viên gạch phân hình khối lập phương! Tại sao tạo hóa lại bắt nó làm việc như dây chuyền nhà máy gạch? [question-oh] Câu trả lời là để đánh dấu lãnh thổ! Uôm-bát có thị lực cực kém, nó dùng mùi phân để giao tiếp và đặt phân lên trên những tảng đá cao hoặc thân cây đổ. Nếu phân hình tròn, nó sẽ lăn tọt xuống rãnh; nhưng phân hình khối lập phương thì nằm im bất động không lăn đi đâu được! Đúng là thiết kế chống lăn đỉnh cao của tạo hóa! [laughter]
```
**Part 5** → `audio/vs/scene03_p5.wav` (394 ký tự) · mood `hao_hung`

```text
Hiện tượng cơ học này kỳ diệu đến mức các kỹ sư vật liệu tại viện nghiên cứu đang mô phỏng cấu trúc ruột của Uôm-bát để chế tạo các khuôn đúc công nghiệp thế hệ mới: chế tạo các sản phẩm đất sét, gốm sứ và linh kiện hình khối rỗng mà không cần dùng đến dao cắt cơ học! Một chú gấu túi béo ục ịch lại đang dạy cho các kỹ sư hàng đầu thế giới bài học vỡ lòng về thủy lực học và tạo hình vật liệu!
```

### scene04 — CÚ ĐÁ LỪA NGƯỢC VÀ ÉP NÁT SỌ KẺ THÙ VÀO TRẦN HANG
*Thẻ chương:* GỒNG MÔNG BỌC THÉP NGHIỀN NÁT HỘP SỌ KẺ SĂN MỒI

*Badge:* `THỰC CHIẾN` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene04_p0.wav` (262 ký tự) · mood `tram_bi_an`

```text
Module kỹ thuật số ba: Kịch bản tác chiến phòng ngự phản công! Đừng nghĩ tấm khiên mông của Xe Tăng Đào Hầm chỉ biết đứng im chịu đòn bị động. Khi bị dồn vào đường hầm tối tăm, cỗ máy nặng ba mươi lăm ki-lô-gam này sẽ kích hoạt bài phản công sát thương hủy diệt!
```
**Part 1** → `audio/vs/scene04_p1.wav` (335 ký tự) · mood `don_dap`

```text
Chiến thuật bẫy mồi kinh điển: Uôm-bát cố tình bò thụt lùi vào trong lòng hang hẹp, hơi hạ thấp phần mông xuống tạo ra một khe hở vừa đủ trên đầu. Con chó hoang Đin-gô háo thắng tưởng con mồi đã cùng đường liền thò đầu vào khe hở định ngoạm lấy cổ họng đối phương. Đúng khoảnh khắc chiếc đầu chó hoang chui lọt vào bẫy... [surprise-oh]
```
**Part 2** → `audio/vs/scene04_p2.wav` (402 ký tự) · mood `don_dap`

```text
Bùm! Uôm-bát dùng hai chân sau gồng cực mạnh toàn bộ cơ bắp, bật chiếc mông bọc thép đội thẳng lên trên! Lực đẩy bằng khối cơ bắp ba mươi lăm ki-lô-gam ép chặt chiếc đầu của kẻ săn mồi nghiền nát vào trần hang đá hoa cương cứng ngắc! Bảo tàng Úc ghi nhận nhiều xác chó hoang Dingo được tìm thấy ngoài cửa hang với hộp sọ bị nghiền nát vụn chính là tác phẩm của cú gồng mông chết chóc này! [surprise-wa]
```
**Part 3** → `audio/vs/scene04_p3.wav` (98 ký tự) · 🎭 cameo `ga_khong_lo`

```text
Gâu gâu! Ta tưởng tóm được miếng mồi béo bở, ai ngờ đụng phải tảng đá hoa cương nghiền nát cả đầu!
```
**Part 4** → `audio/vs/scene04_p4.wav` (507 ký tự) · mood `hao_hung`

```text
Nếu phải đánh nhau ngoài bãi cỏ trống trải, gã xe tăng này cũng không ngán đối thủ nào: gã tung ra cú đá lừa ngược bằng hai chân sau uy lực như cú đá của ngựa chứng, hất văng kẻ địch ra xa! Và đừng khinh thường ngoại hình tròn béo lù đù: khi cần tháo chạy nước rút về hang, Uôm-bát có thể tăng tốc lên tới bốn mươi cây số một giờ trong vòng chín mươi giây — nhanh ngang ngửa một vận động viên điền kinh Olympic! [laughter] Kẻ thù chưa kịp định thần thì bóng chiếc mông bọc thép đã biến mất tăm vào lòng đất!
```

### scene05 — BỆNH GHẺ LỞ, CẬN THỊ NẶNG VÀ TAI NẠN GIAO THÔNG
*Thẻ chương:* TỬ HUYỆT BỆNH GHẺ VÀ SỨ MỆNH ĐƯỢC CHIA SẺ HANG NGẦM

*Badge:* `ĐIỂM YẾU KỸ THUẬT` · *mood mặc định:* `bi_hai`

**Part 0** → `audio/vs/scene05_p0.wav` (306 ký tự) · mood `nghiem_trang_gia`

```text
Module kỹ thuật số bốn: Phân tích điểm yếu và mối đe dọa sinh tồn! Một cỗ xe tăng có giáp mông chống đạn, chân đào máy xúc, hàm răng gặm gỗ và chạy nhanh bốn mươi cây số một giờ liệu có bất khả chiến bại trên thảo nguyên hoang dã? Đội kỹ thuật chúng tôi phải chỉ ra ba tử huyệt nghiêm trọng trong thiết kế!
```
**Part 1** → `audio/vs/scene05_p1.wav` (302 ký tự) · mood `bi_hai`

```text
Thứ nhất là thị lực cực kỳ tệ hại: mắt của Uôm-bát bị cận thị nặng, ban đêm đi kiếm ăn chỉ dựa vào khứu giác và thính giác, nên gã rất hay húc đầu vào gốc cây hoặc lững thững băng qua đường cao tốc mà không nhìn thấy đèn xe tải từ xa, biến tai nạn giao thông ban đêm thành nguyên nhân tử vong hàng đầu!
```
**Part 2** → `audio/vs/scene05_p2.wav` (496 ký tự) · mood `am_ap`

```text
Thứ hai là thảm họa ký sinh trùng: căn bệnh ghẻ lở do ve ký sinh làm gã ngứa ngáy dữ dội, rụng lông và suy kiệt cơ thể là mối đe dọa lớn nhất đối với các đàn Uôm-bát hoang dã. [sigh] Nhưng điều làm người dân Úc yêu quý sinh vật này nhất là nghĩa cử cao đẹp trong những trận đại hạn và cháy rừng lịch sử: mạng lưới hang ngầm dài ba mươi mét mát mẻ của Uôm-bát đã trở thành những hầm trú ẩn sinh tồn cứu sống hàng ngàn sinh vật nhỏ như thú có túi, thằn lằn và chim chóc cùng trốn chung một mái nhà!
```
**Part 3** → `audio/vs/scene05_p3.wav` (344 ký tự) · mood `am_ap`

```text
Mạng lưới hang ngầm của Uôm-bát đồ sộ như một mê cung tàu điện ngầm dưới lòng đất: mỗi hang có tới năm sáu cửa thoát hiểm, chiều dài ngoằn ngoèo tới ba mươi mét và sâu hơn ba mét dưới lòng đất. Nhờ độ sâu này, nhiệt độ bên trong hang luôn mát rượi vào mùa hè và ấm áp vào mùa đông, tạo nên một công trình kiến trúc sinh thái bền vững tuyệt đối!
```

### scene06 — CHIẾC XE TĂNG LẦY LỘI VÀ BÓNG ĐEN 22 XÚC TU KỲ SAU
*Thẻ chương:* BÁO CÁO KỸ THUẬT VÀ BÓNG ĐEN CHIẾC MŨI 22 XÚC TU

*Badge:* `BÁO CÁO KỸ THUẬT` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (317 ký tự) · mood `am_ap`

```text
Tổng kết báo cáo kỹ thuật số hai mươi sáu. Từ một khối thịt tròn ủm lù đù nặng ba mươi lăm ki-lô-gam, Gấu Túi Uôm-bát đã chứng minh một chân lý cơ học vĩ đại: không cần nanh vuốt dữ tợn, một chiếc mông bọc thép kiên cường cùng một chiến thuật đào hầm thông minh đủ sức giúp nó đứng vững trước mọi kẻ thù tàn bạo nhất!
```
**Part 1** → `audio/vs/scene06_p1.wav` (194 ký tự) · mood `hao_hung`

```text
Báo cáo nghiệm thu vũ khí: Đạt điểm mười tuyệt đối cho cỗ máy công thủ toàn diện và danh hiệu nhà máy đúc gạch phân độc nhất vô nhị hành tinh! Ký tên: kỹ sư trưởng đội giải mã vũ khí! [laughter]
```
**Part 2** → `audio/vs/scene06_p2.wav` (265 ký tự) · mood `hao_hung`

```text
Còn đội kỹ thuật thì sao? Nếu được chế tạo một bộ giáp công nghệ lấy cảm hứng từ Uôm-bát: chiếc khiên mông chống đạn nghiền nát mọi kẻ bám đuôi, hay dây chuyền đúc phân lập phương chống lăn siêu tiện lợi, anh em chọn trang bị nào? Hãy để lại bình luận bên dưới nhé!
```
**Part 3** → `audio/vs/scene06_p3.wav` (619 ký tự) · mood `am_ap`

```text
Hồ sơ vũ khí số hai mươi sáu xin chính thức đóng lại. Nhưng tập sau, chúng ta sẽ chuyển thẳng sang chương trình phóng sự trực tiếp hai mươi bốn giờ để theo chân một cỗ máy săn mồi tốc độ bàn thờ dưới lòng đất tăm tối! Một sinh vật bé nhỏ chỉ nặng năm mươi gam, hai mắt mù tịt, nhưng sở hữu chiếc mũi quái đản hình bông hoa gồm hai mươi hai xúc tu đỏ hồng rung rinh! Tốc độ ăn tối của nó nhanh đến mức khó tin: chỉ mất đúng không phẩy mười hai giây để nhận diện và nuốt chửng con mồi, nhanh hơn cả một cái chớp mắt của con người! Đố các bạn biết bóng đen bí ẩn kỳ sau là loài vật nào? Hãy đoán ngay ở phần bình luận nhé!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Sinh vật này sở hữu chiếc mông bọc thép cứng như bê tông, chuyên bẫy lừa chó hoang chui đầu vào hang rồi gồng mông dập nát hộp sọ kẻ thù vào trần đá! [laughter] Xin giới thiệu Gấu Túi Wombat, xe tăng đào hầm nặng ba mươi lăm ki-lô-gam của nước Úc. Toàn bộ vùng mông của nó được gia cố bằng một tấm khiên sụn và mô sợi dày tới ba xăng-ti-mét, khi bị rượt đuổi, nó chui tọt vào hang và lấy chiếc mông sắt bịt kín cửa hang khiến kẻ săn mồi cắn gãy răng! [surprise-wa] Chưa hết, nó là sinh vật duy nhất trên thế giới đi vệ sinh ra những viên phân hình khối lập phương vuông vức như viên xúc xắc! Nhờ đoạn ruột già có độ co giãn không đồng đều, mỗi đêm nó đúc ra một trăm viên gạch phân vuông để đánh dấu lãnh thổ trên mỏm đá mà không sợ bị lăn xuống rãnh! Khi cần chạy trốn, gã xe tăng tròn béo này có thể phóng nước rút tới bốn mươi cây số một giờ! Một cỗ xe bọc thép vừa lầy lội, vừa sở hữu thiết kế cơ khí đỉnh cao nhất hành tinh!
```

**Whisper prompt:** `Gấu Túi Wombat, Xe Tăng Đào Hầm, Vombatidae, Pa-tri-xi-a Dăng, Patricia Yang, I-gơ Nô-ben, Ig Nobel, chó hoang Đin-gô, Dingo, mông bọc thép, khối lập phương, ruột già, túi mở ngược, 2-3cm, 80-100 viên, 40km/h, 30m, 35kg, 8%`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| ba đê | 3D |
| ba mét | 3m |
| năm sáu | 5-6 |
| hai mươi sáu | 26 |
| hai mươi bảy | 27 |
| hai mươi lăm | 25 |
| ba mươi lăm | 35 |
| ba mươi lăm ki-lô-gam | 35kg |
| hai mươi lăm đến ba mươi lăm ki-lô-gam | 25-35kg |
| hai mươi đến ba mươi mét | 20-30m |
| ba mươi mét | 30m |
| hai đến ba xăng-ti-mét | 2-3cm |
| ba xăng-ti-mét | 3cm |
| tám mươi đến một trăm viên | 80-100 viên |
| một trăm viên | 100 viên |
| tám mươi viên | 80 viên |
| tám phần trăm | 8% |
| bốn mươi cây số một giờ | 40km/h |
| chín mươi giây | 90 giây |
| bốn mặt phẳng | 4 mặt phẳng |
| sáu mặt phẳng | 6 mặt phẳng |
| men răng | men răng |
| hai tuần | 2 tuần |
| ba mươi mốt | 31 |
| ba mươi | 30 |
| sáu mươi | 60 |
| hai mươi bốn giờ | 24 giờ |
| năm mươi gam | 50g |
| hai mươi hai xúc tu | 22 xúc tu |
| mười hai | 12 |
| không phẩy mười hai giây | 0,12 giây |
| hai ngàn mười chín | 2019 |
| hai ngàn hai mươi mốt | 2021 |
| một trăm phần trăm | 100% |
| hàng trăm | hàng trăm |
| hàng ngàn | hàng ngàn |
| hàng chục mét | hàng chục mét |
| hàng chục | hàng chục |
| bốn hạng mục | 4 hạng mục |
| năm cấp độ | 5 cấp độ |
| thứ nhất | thứ 1 |
| thứ hai | thứ 2 |
| thứ ba | thứ 3 |
| thứ tư | thứ 4 |
| thứ năm | thứ 5 |
| điểm mười | điểm 10 |
| Uôm-bát | Wombat |
| Đin-gô | Dingo |
| Canh-gu-ru | Kangaroo |
| Cô-a-la | Koala |
| I-gơ Nô-ben | Ig Nobel |
| Pa-tri-xi-a Dăng | Patricia Yang |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · CHIẾN XA ĐÀO HẦM NẶNG 35KG CỦA NƯỚC ÚC · 74.3s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:06.5 (6.5s) | L01 | Hồ sơ mật cấp độ đỏ. Mở khóa dữ liệu kỹ thuật! Toàn thể đội kỹ thuật tập trung trước màn hình mô phỏng 3D. |  | Phòng thiết kế cơ khí quân sự tối tân: người kỹ sư trưởng hoạt hình mặc áo phản quang cam cầm bản vẽ kỹ thuật cuộn tròn và thước đo mở màn hình mô phỏng 3D màu đỏ rực giữa căn phòng công nghệ cao. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này. |
| b02 | 00:06.5–00:12.4 (5.8s) | L02 | Hôm nay chúng ta giải mã một trong những bản thiết kế cơ khí sinh học kỳ dị và thực dụng bậc nhất của giới tự nhiên nước Úc: |  | Bản vẽ thiết kế cơ khí sinh học: một cỗ máy đào hầm sống của giới tự nhiên nước Úc hiện lên từng chi tiết bánh xích và động cơ. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này. |
| b03 | 00:12.4–00:22.8 (10.4s) | L03 | một cỗ máy đào hầm sống nặng từ 25-35kg, thân hình lùn tịt tròn quay như thùng rượu, nhưng sở hữu lớp giáp phòng ngự phía sau khiến cả loài chó hoang Dingo phải gãy răng! | **25-35 KG** · cân nặng xe tăng · R/350 · [0.65, 0.5] | chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng lù đù bước ra, thân hình tròn quay lùn tịt như chiếc thùng rượu nhỏ bọc lông nâu xám, chiếc mông phía sau phát sáng hào qu |
| b04 | 00:22.8–00:29.6 (6.7s) | L04 | Báo cáo chỉ huy, radar ghi nhận mục tiêu đang di chuyển với tốc độ bất thường, nhìn như cục đá biết đi nhưng đào hầm nhanh ngang máy xúc! |  | Màn hình radar quét địa chấn hiển thị một mục tiêu di chuyển thần tốc xuyên lòng đất đào những đường hầm ngầm nhanh như máy xúc bánh xích. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này. |
| b05 | 00:29.6–00:38.8 (9.2s) | L05 | Báo cáo rất chuẩn xác! Xin giới thiệu với cả đội: đây là Gấu Túi Wombat, thú có túi đặc hữu của châu Đại Dương, họ hàng thân cận nhất của loài Koala ôm cây. |  | Bản đồ nước Úc xinh đẹp: chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng đứng cạnh người anh em gấu Koala đang ôm cây ngủ gật lờ đờ, đối chiếu hai tính cách trái ngược ho |
| b06 | 00:38.8–00:44.9 (6.1s) | L06 | Nhưng khác với người anh em Koala suốt ngày ngủ gật ngơ ngác, sinh vật này được trang bị đầy đủ bộ giáp công thủ toàn diện: |  | chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng tự tin tạo dáng thể hiện bộ giáp công thủ toàn diện khắp cơ thể, dáng đứng dũng mãnh và kiên cường. |
| b07 | 00:44.9–00:52.5 (7.6s) | L07 | hàm răng mọc dài liên tục đục thủng rễ cây, móng vuốt xẻng đào hầm xuyên qua đất đá, và chiếc mông bọc thép dày cộp hoạt động như một tấm khiên chống |  | Sơ đồ vũ khí toàn thân của chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng: răng cửa đục rễ cây, chân trước vuốt xẻng máy đào đất đá, và chiếc mông bọc thép dày cộp như t |
| b08 | 00:52.5–00:57.5 (5.0s) | L08 | đạn! Trong phòng thiết kế, chúng tôi gọi thẳng tên nó bằng biệt danh: Xe Tăng Đào Hầm! |  | chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng oai vệ đứng trên bệ bánh xích cỗ xe công trình mini, đeo kính bảo hộ công trình với dải băng danh hiệu Chiến Binh Đào Hầm. |
| b09 | 00:57.5–01:09.5 (12.0s) | L09 | Chưa dừng lại ở đó, cỗ xe tăng này còn nắm giữ một kỷ lục vô tiền khoáng hậu khiến các kỹ sư thủy lực và vật lý học toàn cầu phải ôm đầu thán phục: sinh vật duy nhất trên hành tinh có khả năng đúc ra những khối phân vuông vức hình lập phương chuẩn xác đến từng góc cạnh! |  | Các kỹ sư thủy lực và vật lý học thế giới ôm đầu sửng sốt trước mô hình những viên phân hình khối lập phương vuông vức như viên xúc xắc. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này. |
| b10 | 01:09.5–01:14.3 (4.8s) | L10 | Đêm nay, tôi mời toàn đội cùng mổ xẻ bốn module kỹ thuật tối mật trên cơ thể Xe Tăng Đào Hầm! |  | người kỹ sư trưởng hoạt hình mặc áo phản quang cam cầm bản vẽ kỹ thuật cuộn tròn và thước đo lật mở tập hồ sơ bản vẽ kỹ thuật dày cộp có dấu mật; chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công n |

### scene02 · TẤM KHIÊN MÔNG BỌC THÉP 3CM VÀ TÚI MỞ NGƯỢC · 101.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.0 (9.0s) | L11 | Module kỹ thuật số một: Bản vẽ tấm khiên mông và kết cấu túi ngầm! Nhìn từ góc nhìn công trình, điểm hiểm yếu nhất của mọi cỗ máy đào hầm ngầm là phần đuôi phía sau: |  | Bảng bản vẽ kỹ thuật hiện MODULE 1: BẢN VẼ TẤM KHIÊN MÔNG VÀ TÚI NGẦM; mô hình điểm hiểm yếu phía sau của cỗ máy đào hầm. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này. |
| b02 | 00:09.0–00:19.1 (10.1s) | L12 | khi chúi đầu vào lòng đất đào bới, phần mông lộ ra ngoài sẽ là miếng mồi ngon cho bất kỳ kẻ săn mồi nào rình rập. Nhưng tạo hóa đã trang bị cho Xe Tăng Đào Hầm một giải pháp giáp đuôi không tưởng! |  | Mô hình cỗ máy đào ngầm chúi đầu vào đất, phần mông lộ ra ngoài có dấu cảnh báo mục tiêu nguy hiểm bị kẻ thù nhắm tới. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này. |
| b03 | 00:19.1–00:32.6 (13.5s) | L13 | Hãy quan sát mặt cắt giải phẫu vùng mông của Wombat: phần đuôi của nó tiêu biến hoàn toàn chỉ còn một mấu cụt nhỏ xíu. Thay vào đó, toàn bộ vùng xương chậu và xương cụt được phủ một lớp mô mạc sợi dày từ 2-3cm, đan kết chặt chẽ với các tấm sụn cứng cáp như thép tấm gia cường! | **DÀY 2-3 CM** · khiên sụn bọc thép · R/350 · [0.65, 0.48] | Mặt cắt giải phẫu X-quang vùng mông chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng: xương chậu và xương cụt bọc lớp mô mạc sợi và các tấm sụn dày cộp như thép tấm gia cư |
| b04 | 00:32.6–00:38.3 (5.7s) | L14 | Phía trên là lớp da siêu dày bọc lông rậm rạp, tạo thành một chiếc nắp cống sinh học bất khả xâm phạm! |  | Mặt cắt lớp da siêu dày phủ lông rậm rạp của chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng trông như một chiếc nắp cống kim loại tròn xoe kiên cố chốt chặn cửa hang. |
| b05 | 00:38.3–00:46.1 (7.8s) | L15 | Khi bị chó hoang Dingo truy đuổi ráo riết, Wombat lập tức lao đầu vào cửa hang ngầm và... quay chiếc mông bọc thép ra ngoài để bịt kín miệng hang! |  | chú chó hoang Dingo lông vàng hung dữ răng nanh nhọn hoắt nhưng bị bầm dập hài hước hung dữ nhe răng đuổi theo chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng; chú Gấu Tú |
| b06 | 00:46.1–00:55.3 (9.2s) | L16 | Chó hoang lao tới cắn xé điên cuồng, nhưng hàm răng sắc nhọn chỉ cắn trúng tấm khiên sụn cứng trơn trượt, cắn mãi không xuyên thủng mà chỉ tổ mòn răng gãy móng! |  | chú chó hoang Dingo lông vàng hung dữ răng nanh nhọn hoắt nhưng bị bầm dập hài hước cắn phập vào mông chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng nhưng răng nanh bị t |
| b07 | 00:55.3–01:07.1 (11.8s) | L17 | Chưa hết, các kỹ sư hãy nhìn xuống vùng bụng của nó: là loài thú có túi giống chuột túi Kangaroo, nhưng nếu cửa túi của chuột túi hướng lên trên, thì cửa túi của Wombat lại quay ngược hoàn toàn về phía sau! Đây là giải pháp công học thiên tài: |  | So sánh chiếc túi có túi: BÊN TRÁI chuột túi Kangaroo có miệng túi mở hướng lên trên; BÊN PHẢI chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng có miệng túi quay ngược hoà |
| b08 | 01:07.1–01:18.3 (11.2s) | L18 | khi gã dùng hai bàn chân trước có móng vuốt thép cào đất tung tóe đào những đường hầm sâu 20-30m, toàn bộ đất cát bắn ra phía sau mà không hề có một hạt bụi nào lọt vào túi làm nghẹt thở đứa con non bé nhỏ bên trong! | **SÂU 20-30M** · mạng lưới hang ngầm · L/350 · [0.35, 0.45] | chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng dùng hai bàn chân trước cào đất tung tóe đào đường hầm sâu 20-30m, đất cát bắn ra phía sau nhưng đứa con non trong túi vẫn |
| b09 | 01:18.3–01:31.5 (13.2s) | L19 | Phía trước đầu xe tăng còn được lắp đặt một cặp mũi khoan sinh học thượng hạng: bốn chiếc răng cửa to bản mọc dài liên tục suốt đời giống hệt loài gặm nhấm! Lớp men răng trước dày cứng cọ sát với lớp ngà mềm phía sau tạo thành lưỡi đục tự mài sắc bén, |  | Cận cảnh hàm răng trước của chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng: bốn chiếc răng cửa to bản sắc như lưỡi đục kim loại, men răng trước dày cứng tự mài sắc bén. |
| b10 | 01:31.5–01:36.3 (4.9s) | L20 | có thể gặm đứt phăng rễ cây bạch đàn cổ thụ và cắn thủng cả ống nhựa công trình của con người! |  | chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng gặm đứt đôi rễ cây bạch đàn cổ thụ to bằng bắp tay và gặm thủng cả ống nhựa công trình một cách dễ dàng. |
| b11 | 01:36.3–01:41.7 (5.4s) | L21 | Đầu là máy khoan mũi nhọn, đuôi là khiên thép chống đạn, đúng là cỗ máy đào công binh hoàn hảo kín kẽ! |  | Mô hình tổng thể xe bọc thép: đầu là mũi khoan đục rễ cây, thân là máy xúc, đuôi là khiên chống đạn; bảng Module 1 bật PASS. |

### scene03 · 8% RUỘT GIÀ ĐÚC 100 KHỐI LẬP PHƯƠNG MỖI NGÀY · 114.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.0 (7.0s) | L22 | Module kỹ thuật số hai: Dây chuyền cơ học đúc phân hình khối lập phương! Đây là bí ẩn cơ học từng làm đau đầu giới khoa học suốt hàng thế kỷ. |  | Bảng bản vẽ kỹ thuật hiện MODULE 2: DÂY CHUYỀN ĐÚC PHÂN KHỐI LẬP PHƯƠNG; mô hình các hình khối phân tròn elip của loài vật khác. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này. |
| b02 | 00:07.0–00:14.2 (7.2s) | L23 | Mọi loài vật từ voi, bò, chim cho đến con người khi thải phân đều tạo ra hình trụ tròn hoặc khối dẹt elip do sự co thắt đồng tâm của cơ vòng hậu môn. |  | Mô hình các khối phân tròn hoặc elip của động vật có vú do cơ vòng hậu môn đồng tâm co bóp. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này. |
| b03 | 00:14.2–00:19.5 (5.3s) | L24 | Nhưng Xe Tăng Đào Hầm của chúng ta thì đi vệ sinh ra... những viên xúc xắc vuông chằn chặn có đủ 6 mặt phẳng! | **6 MẶT** · khối lập phương · R/350 · [0.65, 0.5] | chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng ngồi thảnh thơi trên tảng đá, phía sau thải ra những viên phân hình khối lập phương vuông vức có đủ 6 mặt phẳng như những  |
| b04 | 00:19.5–00:27.2 (7.7s) | L25 | Trời đất ơi chỉ huy ơi, có phải hậu môn của nó có hình vuông giống như khuôn làm bánh không ạ? Trợ lý đoán sai bét rồi nhé! |  | cô trợ lý kỹ thuật hoạt hình mặc áo phản quang vàng cầm chiếc khuôn làm bánh hình vuông ngơ ngác hỏi chỉ huy; người kỹ sư trưởng hoạt hình mặc áo phản quang cam cầm bản vẽ kỹ thuật cuộn tròn và thước đo bật cười giải thích bí ẩn. |
| b05 | 00:27.2–00:39.8 (12.6s) | L26 | Năm 2019, nhóm nghiên cứu của tiến sĩ Patricia Yang tại Viện Công nghệ Georgia đã đưa một chú Wombat vào máy chụp cắt lớp CT và đoạt luôn giải Nobel Vật lý Ig Nobel danh giá! Hậu môn của nó vẫn tròn xoe như mọi loài vật khác. | **IG NOBEL** · Patricia Yang 2019 · L/350 · [0.35, 0.45] | Máy chụp cắt lớp CT của tiến sĩ Patricia Yang và cúp giải thưởng Ig Nobel 2019 rực rỡ; hậu môn của Wombat vẫn tròn xoe như bình thường. |
| b06 | 00:39.8–00:43.5 (3.8s) | L27 | Bí mật cơ khí thực sự nằm ở 8% chiều dài cuối cùng của ruột già! | **8% CUỐI** · ruột già đúc gạch · R/350 · [0.68, 0.48] | Sơ đồ đường ruột của chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng: mũi tên chỉ vào 8% chiều dài cuối cùng của ruột già nơi diễn ra quá trình đúc nén hình học kỳ diệu. |
| b07 | 00:43.5–00:54.5 (10.9s) | L28 | Trong công bố chi tiết trên tạp chí Soft Matter năm 2021, các nhà vật lý phát hiện thành ruột già của Wombat có tính đàn hồi không đồng nhất: có hai dải cơ cứng đối diện nhau và hai dải cơ mềm linh hoạt xen kẽ! |  | Mặt cắt ruột già trên tạp chí Soft Matter 2021: hai dải cơ cứng đối diện nhau và hai dải cơ mềm linh hoạt co bóp nhịp nhàng. |
| b08 | 00:54.5–01:07.1 (12.6s) | L29 | Suốt hành trình tiêu hóa kéo dài 2 tuần, chất xơ thô ráp được vắt kiệt nước và nén chặt lại. Khi khối chất thải đi qua đoạn ruột đặc biệt này, các đợt co bóp nhịp nhàng tác động lực ép khác nhau, nặn khối phân thành những cạnh sắc và 4 mặt phẳng đều tăm tắp! | **2 TUẦN** · thời gian tiêu hóa · R/350 · [0.65, 0.5]<br>**4 MẶT** · áp lực co bóp thành · L/480 · [0.35, 0.45] | Timeline tiêu hóa 2 tuần: chất xơ thô ráp được vắt kiệt nước và nén chặt nặn thành 4 mặt phẳng đều tăm tắp như khuôn gạch. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này. |
| b09 | 01:07.1–01:18.3 (11.2s) | L30 | Mỗi đêm, một chú Wombat sản xuất đều đặn từ 80-100 viên gạch phân hình khối lập phương! Tại sao tạo hóa lại bắt nó làm việc như dây chuyền nhà máy gạch? Câu trả lời là để đánh dấu lãnh | **80-100 V** · sản xuất mỗi đêm · R/350 · [0.65, 0.5] | chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng đứng cạnh một chồng tháp gồm 80-100 viên gạch phân lập phương vuông vức xếp ngay ngắn như công trường xây dựng mini. |
| b10 | 01:18.3–01:23.5 (5.2s) | L31 | thổ! Wombat có thị lực cực kém, nó dùng mùi phân để giao tiếp và đặt phân lên trên những tảng đá cao hoặc thân cây |  | chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng với cặp kính cận dày cộp cẩn thận đặt viên phân vuông lên đỉnh mỏm đá nhọn và thân cây đổ để đánh dấu ranh giới mùi hương. |
| b11 | 01:23.5–01:33.7 (10.2s) | L32 | đổ. Nếu phân hình tròn, nó sẽ lăn tọt xuống rãnh; nhưng phân hình khối lập phương thì nằm im bất động không lăn đi đâu được! Đúng là thiết kế chống lăn đỉnh cao của tạo hóa! |  | So sánh hai hình thái: viên phân hình tròn lăn tọt xuống rãnh nước; còn viên phân hình khối lập phương nằm im bất động trên gờ đá, thiết kế chống lăn đỉnh cao. |
| b12 | 01:33.7–01:47.2 (13.5s) | L33 | Hiện tượng cơ học này kỳ diệu đến mức các kỹ sư vật liệu tại viện nghiên cứu đang mô phỏng cấu trúc ruột của Wombat để chế tạo các khuôn đúc công nghiệp thế hệ mới: chế tạo các sản phẩm đất sét, gốm sứ và linh kiện hình khối rỗng mà không cần dùng đến dao cắt cơ học! |  | Các kỹ sư công nghiệp tại viện nghiên cứu mô phỏng ruột Uôm-bát để chế tạo khuôn đúc gốm sứ và linh kiện rỗng không cần dao cắt. |
| b13 | 01:47.2–01:54.2 (7.0s) | L34 | Một chú gấu túi béo ục ịch lại đang dạy cho các kỹ sư hàng đầu thế giới bài học vỡ lòng về thủy lực học và tạo hình vật liệu! |  | chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng đứng trên bục giảng đường đại học đội mũ cử nhân, giảng bài cho các kỹ sư hàng đầu thế giới về thủy lực học và tạo hình vậ |

### scene04 · CÚ ĐÁ LỪA NGƯỢC VÀ ÉP NÁT SỌ KẺ THÙ VÀO TRẦN HANG · 79.3s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:06.9 (6.9s) | L35 | Module kỹ thuật số ba: Kịch bản tác chiến phòng ngự phản công! Đừng nghĩ tấm khiên mông của Xe Tăng Đào Hầm chỉ biết đứng im chịu đòn bị động. |  | Bảng bản vẽ hiện MODULE 3: KỊCH BẢN TÁC CHIẾN PHÒNG NGỰ PHẢN CÔNG; người kỹ sư trưởng hoạt hình mặc áo phản quang cam cầm bản vẽ kỹ thuật cuộn tròn và thước đo mở sơ đồ mặt cắt lòng hang hẹp. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này. |
| b02 | 00:06.9–00:13.0 (6.1s) | L36 | Khi bị dồn vào đường hầm tối tăm, cỗ máy nặng 35kg này sẽ kích hoạt bài phản công sát thương hủy diệt! |  | chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng nặng 35kg đứng trong đường hầm tối tăm, đôi mắt nhỏ ánh lên vẻ tự tin chuẩn bị kích hoạt đòn phản công sát thương hủy diệt |
| b03 | 00:13.0–00:25.8 (12.8s) | L37 | Chiến thuật bẫy mồi kinh điển: Wombat cố tình bò thụt lùi vào trong lòng hang hẹp, hơi hạ thấp phần mông xuống tạo ra một khe hở vừa đủ trên đầu. Con chó hoang Dingo háo thắng tưởng con mồi đã cùng đường liền thò đầu vào khe hở định ngoạm lấy cổ họng đối phương. |  | Trong lòng hang đá hẹp: chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng bò thụt lùi vào trong, hơi hạ thấp mông tạo khe hở vừa khít; chú chó hoang Dingo lông vàng hung dữ |
| b04 | 00:25.8–00:28.9 (3.1s) | L38 | Đúng khoảnh khắc chiếc đầu chó hoang chui lọt vào bẫy... |  | Chiếc đầu của chú chó hoang Dingo lông vàng hung dữ răng nanh nhọn hoắt nhưng bị bầm dập hài hước chui lọt vào khe hở bên trên mông chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình |
| b05 | 00:28.9–00:40.0 (11.1s) | L39 | Bùm! Wombat dùng hai chân sau gồng cực mạnh toàn bộ cơ bắp, bật chiếc mông bọc thép đội thẳng lên trên! Lực đẩy bằng khối cơ bắp 35kg ép chặt chiếc đầu của kẻ săn mồi nghiền nát vào trần hang đá hoa cương cứng ngắc! | **35 KG ÉP** · nghiền nát hộp sọ · R/350 · [0.62, 0.45] | Bùm! chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng dùng hai chân sau gồng cực mạnh bật chiếc mông thép đội thẳng lên trần hang, ép chặt nghiền nát đầu chú chó hoang Din |
| b06 | 00:40.0–00:47.9 (7.9s) | L40 | Bảo tàng Úc ghi nhận nhiều xác chó hoang Dingo được tìm thấy ngoài cửa hang với hộp sọ bị nghiền nát vụn chính là tác phẩm của cú gồng mông chết chóc này! |  | Bên ngoài cửa hang đá: các nhà nghiên cứu bảo tàng Úc ghi nhận dấu vết xương hộp sọ bị nghiền nát của loài chó hoang, minh chứng cho cú gồng mông uy lực. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này. |
| b07 | 00:47.9–00:52.9 (5.0s) | L41 | Gâu gâu! Ta tưởng tóm được miếng mồi béo bở, ai ngờ đụng phải tảng đá hoa cương nghiền nát cả đầu! |  | chú chó hoang Dingo lông vàng hung dữ răng nanh nhọn hoắt nhưng bị bầm dập hài hước ôm đầu bầm dập hoa mắt chóng mặt với những ngôi sao quay cuồng quanh đầu, vừa khóc vừa lồm cồm bò ra khỏi miệng hang. |
| b08 | 00:52.9–01:05.5 (12.6s) | L42 | Nếu phải đánh nhau ngoài bãi cỏ trống trải, gã xe tăng này cũng không ngán đối thủ nào: gã tung ra cú đá lừa ngược bằng hai chân sau uy lực như cú đá của ngựa chứng, hất văng kẻ địch ra xa! Và đừng khinh thường ngoại hình tròn béo lù đù: |  | Trên bãi cỏ ngoài hang: chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng tung cú đá lừa ngược bằng hai chân sau cực mạnh hất văng một con cáo săn mồi bay lên không trung. |
| b09 | 01:05.5–01:19.3 (13.8s) | L43 | khi cần tháo chạy nước rút về hang, Wombat có thể tăng tốc lên tới 40km/h trong vòng 90 giây — nhanh ngang ngửa một vận động viên điền kinh Olympic! Kẻ thù chưa kịp định thần thì bóng chiếc mông bọc thép đã biến mất tăm vào lòng đất! | **40 KM/H** · nước rút trong 90s · L/350 · [0.35, 0.45] | chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng phi nước rút với tốc độ 40km/h trong 90 giây như viên đạn đại bác lao vun vút về cửa hang; bảng Module 3 bật PASS. |

### scene05 · BỆNH GHẺ LỞ, CẬN THỊ NẶNG VÀ TAI NẠN GIAO THÔNG · 69.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:14.5 (14.5s) | L44 | Module kỹ thuật số bốn: Phân tích điểm yếu và mối đe dọa sinh tồn! Một cỗ xe tăng có giáp mông chống đạn, chân đào máy xúc, hàm răng gặm gỗ và chạy nhanh 40km/h liệu có bất khả chiến bại trên thảo nguyên hoang dã? Đội kỹ thuật chúng tôi phải chỉ ra ba tử huyệt nghiêm trọng trong thiết kế! |  | Bảng bản vẽ hiện MODULE 4: PHÂN TÍCH ĐIỂM YẾU VÀ TỬ HUYỆT; người kỹ sư trưởng hoạt hình mặc áo phản quang cam cầm bản vẽ kỹ thuật cuộn tròn và thước đo khoanh vùng các mối đe dọa sinh tồn. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này. |
| b02 | 00:14.5–00:29.2 (14.7s) | L45 | Thứ nhất là thị lực cực kỳ tệ hại: mắt của Wombat bị cận thị nặng, ban đêm đi kiếm ăn chỉ dựa vào khứu giác và thính giác, nên gã rất hay húc đầu vào gốc cây hoặc lững thững băng qua đường cao tốc mà không nhìn thấy đèn xe tải từ xa, biến tai nạn giao thông ban đêm thành nguyên nhân tử vong hàng đầu! |  | chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng đeo kính cận dày cộp lững thững đi đêm, suýt húc đầu vào gốc cây to bên đường do thị lực kém. |
| b03 | 00:29.2–00:43.9 (14.7s) | L46 | Thứ hai là thảm họa ký sinh trùng: căn bệnh ghẻ lở do ve ký sinh làm gã ngứa ngáy dữ dội, rụng lông và suy kiệt cơ thể là mối đe dọa lớn nhất đối với các đàn Wombat hoang dã. Nhưng điều làm người dân Úc yêu quý sinh vật này nhất là nghĩa cử cao đẹp trong những trận đại hạn và cháy rừng lịch sử: |  | Kính lúp phóng to con ve ghẻ ký sinh gây ngứa ngáy rụng lông; bên cạnh là dấu chấm than cảnh báo dịch bệnh đối với gấu túi. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này. |
| b04 | 00:43.9–00:54.5 (10.6s) | L47 | mạng lưới hang ngầm dài 30m mát mẻ của Wombat đã trở thành những hầm trú ẩn sinh tồn cứu sống hàng ngàn sinh vật nhỏ như thú có túi, thằn lằn và chim chóc cùng trốn chung một mái nhà! Mạng lưới hang ngầm của |  | Khung cảnh ấm áp bình yên: bên trong mạng lưới hang ngầm mát mẻ của chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng, hàng chục con thú nhỏ như thằn lằn, chim chóc cùng ng |
| b05 | 00:54.5–01:02.8 (8.3s) | L48 | Wombat đồ sộ như một mê cung tàu điện ngầm dưới lòng đất: mỗi hang có tới 5-6 cửa thoát hiểm, chiều dài ngoằn ngoèo tới 30m và sâu hơn 3m dưới lòng đất. | **DÀI 30 MÉT** · sâu 3m mát rượi · R/350 · [0.65, 0.48] | Sơ đồ kiến trúc ngầm 3D: hệ thống hang dài 30m, sâu hơn 3m dưới lòng đất với 5-6 cửa thoát hiểm như mạng lưới tàu điện ngầm sinh thái. |
| b06 | 01:02.8–01:09.9 (7.1s) | L49 | Nhờ độ sâu này, nhiệt độ bên trong hang luôn mát rượi vào mùa hè và ấm áp vào mùa đông, tạo nên một công trình kiến trúc sinh thái bền vững tuyệt đối! |  | Biểu đồ nhiệt độ bên trong hang luôn mát rượi vào mùa hè và ấm áp vào mùa đông, tạo nên công trình kiến trúc sinh thái bền vững; bảng Module 4 bật PASS. |

### scene06 · CHIẾC XE TĂNG LẦY LỘI VÀ BÓNG ĐEN 22 XÚC TU KỲ SAU · 69.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.5 (8.5s) | L50 | Tổng kết báo cáo kỹ thuật số 26. Từ một khối thịt tròn ủm lù đù nặng 35kg, Gấu Túi Wombat đã chứng minh một chân lý cơ học vĩ đại: |  | người kỹ sư trưởng hoạt hình mặc áo phản quang cam cầm bản vẽ kỹ thuật cuộn tròn và thước đo đứng cạnh bàn điều khiển tổng kết báo cáo kỹ thuật số 26, ngắm nhìn mô hình Xe Tăng Đào Hầm với sự nể phục tuyệt đối. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này. |
| b02 | 00:08.5–00:15.6 (7.1s) | L51 | không cần nanh vuốt dữ tợn, một chiếc mông bọc thép kiên cường cùng một chiến thuật đào hầm thông minh đủ sức giúp nó đứng vững trước mọi kẻ thù tàn bạo nhất! |  | chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng kiên cường đứng vững giữa thảo nguyên hoang dã với chiếc mông bọc thép kiên cố trước mọi kẻ thù. |
| b03 | 00:15.6–00:26.0 (10.4s) | L52 | Báo cáo nghiệm thu vũ khí: Đạt điểm 10 tuyệt đối cho cỗ máy công thủ toàn diện và danh hiệu nhà máy đúc gạch phân độc nhất vô nhị hành tinh! Ký tên: kỹ sư trưởng đội giải mã vũ khí! | **ĐIỂM 10** · nghiệm thu vũ khí · R/350 · [0.58, 0.45] | người kỹ sư trưởng hoạt hình mặc áo phản quang cam cầm bản vẽ kỹ thuật cuộn tròn và thước đo đóng dấu NGHIỆM THU ĐẠT ĐIỂM 10 màu đỏ chót lên bản vẽ; chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ côn |
| b04 | 00:26.0–00:40.0 (14.1s) | L53 | Còn đội kỹ thuật thì sao? Nếu được chế tạo một bộ giáp công nghệ lấy cảm hứng từ Wombat: chiếc khiên mông chống đạn nghiền nát mọi kẻ bám đuôi, hay dây chuyền đúc phân lập phương chống lăn siêu tiện lợi, anh em chọn trang bị nào? Hãy để lại bình luận bên dưới nhé! |  | Hai bàn cân lựa chọn: BÊN TRÁI biểu tượng chiếc khiên mông chống đạn nghiền sọ; BÊN PHẢI biểu tượng khuôn đúc phân lập phương chống lăn, khán giả giơ thẻ bình chọn. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này. |
| b05 | 00:40.0–00:50.0 (9.9s) | L54 | Hồ sơ vũ khí số 26 xin chính thức đóng lại. Nhưng tập sau, chúng ta sẽ chuyển thẳng sang chương trình phóng sự trực tiếp 24 giờ để theo chân một cỗ máy săn mồi tốc độ bàn thờ dưới lòng đất tăm |  | người kỹ sư trưởng hoạt hình mặc áo phản quang cam cầm bản vẽ kỹ thuật cuộn tròn và thước đo cuộn tròn bản vẽ số 26 lại cất vào hòm sắt, trên màn hình chuyển sang đồng hồ 24 giờ phóng sự điều tra trực tiếp dưới lòng đất tăm tối. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này. |
| b06 | 00:50.0–00:57.5 (7.5s) | L55 | tối! Một sinh vật bé nhỏ chỉ nặng 50g, hai mắt mù tịt, nhưng sở hữu chiếc mũi quái đản hình bông hoa gồm 22 xúc tu đỏ hồng rung | **NẶNG 50G** · chuột chũi sao · L/350 · [0.35, 0.45]<br>**22 XÚC TU** · mũi hình bông hoa · R/480 · [0.68, 0.55] | Một sinh vật bí ẩn được vẽ hoàn toàn bằng BÓNG ĐEN ĐẶC TUYỀN (solid black silhouette) nhỏ xíu nặng 50g, chiếc mũi xòe ra 22 xúc tu đỏ hồng như bông hoa sao lấp lánh; có dấu hỏi chấm vàng to tướng; KHÔNG vẽ mắt mũi lông. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này. |
| b07 | 00:57.5–01:09.9 (12.4s) | L56 | rinh! Tốc độ ăn tối của nó nhanh đến mức khó tin: chỉ mất đúng 0,12 giây để nhận diện và nuốt chửng con mồi, nhanh hơn cả một cái chớp mắt của con người! Đố các bạn biết bóng đen bí ẩn kỳ sau là loài vật nào? Hãy đoán ngay ở phần bình luận nhé! | **0,12 GIÂY** · ăn nhanh nhất thế giới · L/350 · [0.35, 0.45] | Đồng hồ siêu tốc đếm 0,12 giây phát sáng: sinh vật bóng đen nuốt chửng con mồi nhanh hơn cái chớp mắt của con người; ba dấu hỏi chấm lớn lấp lánh vàng cam mời gọi khán giả đoán tên. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này. |

## 5. Phân cảnh Shorts — từng beat

Banner: **MÔNG BỌC THÉP ÉP / NÁT SỌ CHÓ HOANG?!** · giọng 49.4s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Sinh vật này sở hữu chiếc mông bọc thép cứng như bê tông, |  |
| s02 | 00:03.1 | S02 | chuyên bẫy lừa chó hoang chui đầu vào hang rồi gồng mông dập nát hộp sọ kẻ thù vào trần đá! |  |
| s03 | 00:08.7 | S03 | Xin giới thiệu Gấu Túi Wombat, xe tăng đào hầm nặng 35kg của nước Úc. | **35 KG** · xe tăng đào hầm · R/620 · [0.6, 0.5] |
| s04 | 00:13.8 | S04 | Toàn bộ vùng mông của nó được gia cố bằng một tấm khiên sụn và mô sợi dày tới 3cm, | **DÀY 3CM** · khiên sụn bọc thép · L/620 · [0.4, 0.5] |
| s05 | 00:18.4 | S05 | khi bị rượt đuổi, nó chui tọt vào hang và lấy chiếc mông sắt bịt kín cửa hang khiến kẻ săn mồi cắn gãy răng! |  |
| s06 | 00:24.7 | S06 | Chưa hết, nó là sinh vật duy nhất trên thế giới đi vệ sinh ra những viên phân hình khối lập phương vuông vức như viên xúc xắc! |  |
| s07 | 00:31.4 | S07 | Nhờ đoạn ruột già có độ co giãn không đồng đều, |  |
| s08 | 00:34.4 | S08 | mỗi đêm nó đúc ra 100 viên gạch phân vuông để đánh dấu lãnh thổ trên mỏm đá mà không sợ bị lăn xuống rãnh! | **100 VIÊN** · gạch phân lập phương · R/650 · [0.62, 0.5] |
| s09 | 00:40.0 | S09 | Khi cần chạy trốn, gã xe tăng tròn béo này có thể phóng nước rút tới 40km/h! | **40 KM/H** · nước rút thần tốc · L/680 · [0.38, 0.5] |
| s10 | 00:44.8 | S10 | Một cỗ xe bọc thép vừa lầy lội, vừa sở hữu thiết kế cơ khí đỉnh cao nhất hành tinh! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hồ sơ mật cấp độ đỏ. Mở khóa dữ liệu kỹ thuật! Toàn thể đội kỹ thuật tập trung trước màn hình mô phỏng 3D.". Bố cục: Phòng thiết kế cơ khí quân sự tối tân: người kỹ sư trưởng hoạt hình mặc áo phản quang cam cầm bản vẽ kỹ thuật cuộn tròn và thước đo mở màn hình mô phỏng 3D màu đỏ rực giữa căn phòng công nghệ cao. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hôm nay chúng ta giải mã một trong những bản thiết kế cơ khí sinh học kỳ dị và thực dụng bậc nhất của giới tự nhiên nước Úc:". Bố cục: Bản vẽ thiết kế cơ khí sinh học: một cỗ máy đào hầm sống của giới tự nhiên nước Úc hiện lên từng chi tiết bánh xích và động cơ. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "một cỗ máy đào hầm sống nặng từ 25-35kg, thân hình lùn tịt tròn quay như thùng rượu, nhưng sở hữu lớp giáp phòng ngự phía sau khiến cả loài chó hoang Dingo phải gãy răng!". Bố cục: chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng lù đù bước ra, thân hình tròn quay lùn tịt như chiếc thùng rượu nhỏ bọc lông nâu xám, chiếc mông phía sau phát sáng hào quang kim loại cứng cáp.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo chỉ huy, radar ghi nhận mục tiêu đang di chuyển với tốc độ bất thường, nhìn như cục đá biết đi nhưng đào hầm nhanh ngang máy xúc!". Bố cục: Màn hình radar quét địa chấn hiển thị một mục tiêu di chuyển thần tốc xuyên lòng đất đào những đường hầm ngầm nhanh như máy xúc bánh xích. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo rất chuẩn xác! Xin giới thiệu với cả đội: đây là Gấu Túi Wombat, thú có túi đặc hữu của châu Đại Dương, họ hàng thân cận nhất của loài Koala ôm cây.". Bố cục: Bản đồ nước Úc xinh đẹp: chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng đứng cạnh người anh em gấu Koala đang ôm cây ngủ gật lờ đờ, đối chiếu hai tính cách trái ngược hoàn toàn.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng khác với người anh em Koala suốt ngày ngủ gật ngơ ngác, sinh vật này được trang bị đầy đủ bộ giáp công thủ toàn diện:". Bố cục: chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng tự tin tạo dáng thể hiện bộ giáp công thủ toàn diện khắp cơ thể, dáng đứng dũng mãnh và kiên cường.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hàm răng mọc dài liên tục đục thủng rễ cây, móng vuốt xẻng đào hầm xuyên qua đất đá, và chiếc mông bọc thép dày cộp hoạt động như một tấm khiên chống đạn!". Bố cục: Sơ đồ vũ khí toàn thân của chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng: răng cửa đục rễ cây, chân trước vuốt xẻng máy đào đất đá, và chiếc mông bọc thép dày cộp như tấm khiên chống đạn.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong phòng thiết kế, chúng tôi gọi thẳng tên nó bằng biệt danh: Chiến Binh Đào Hầm!". Bố cục: chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng oai vệ đứng trên bệ bánh xích cỗ xe công trình mini, đeo kính bảo hộ công trình với dải băng danh hiệu Chiến Binh Đào Hầm.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa dừng lại ở đó, cỗ xe tăng này còn nắm giữ một kỷ lục vô tiền khoáng hậu khiến các kỹ sư thủy lực và vật lý học toàn cầu phải ôm đầu thán phục: sinh vật duy nhất trên hành tinh có khả năng đúc ra những khối phân vuông vức hình lập phương chuẩn xác đến từng góc cạnh!". Bố cục: Các kỹ sư thủy lực và vật lý học thế giới ôm đầu sửng sốt trước mô hình những viên phân hình khối lập phương vuông vức như viên xúc xắc. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đêm nay, tôi mời toàn đội cùng mổ xẻ bốn module kỹ thuật tối mật trên cơ thể Xe Tăng Đào Hầm!". Bố cục: người kỹ sư trưởng hoạt hình mặc áo phản quang cam cầm bản vẽ kỹ thuật cuộn tròn và thước đo lật mở tập hồ sơ bản vẽ kỹ thuật dày cộp có dấu mật; chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng giơ hai bàn chân có móng vuốt thép sẵn sàng khởi động.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Module kỹ thuật số một: Bản vẽ tấm khiên mông và kết cấu túi ngầm! Nhìn từ góc nhìn công trình, điểm hiểm yếu nhất của mọi cỗ máy đào hầm ngầm là phần đuôi phía sau:". Bố cục: Bảng bản vẽ kỹ thuật hiện MODULE 1: BẢN VẼ TẤM KHIÊN MÔNG VÀ TÚI NGẦM; mô hình điểm hiểm yếu phía sau của cỗ máy đào hầm. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "khi chúi đầu vào lòng đất đào bới, phần mông lộ ra ngoài sẽ là miếng mồi ngon cho bất kỳ kẻ săn mồi nào rình rập. Nhưng tạo hóa đã trang bị cho Xe Tăng Đào Hầm một giải pháp giáp đuôi không tưởng!". Bố cục: Mô hình cỗ máy đào ngầm chúi đầu vào đất, phần mông lộ ra ngoài có dấu cảnh báo mục tiêu nguy hiểm bị kẻ thù nhắm tới. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy quan sát mặt cắt giải phẫu vùng mông của Wombat: phần đuôi của nó tiêu biến hoàn toàn chỉ còn một mấu cụt nhỏ xíu. Thay vào đó, toàn bộ vùng xương chậu và xương cụt được phủ một lớp mô mạc sợi dày từ 2-3cm, đan kết chặt chẽ với các tấm sụn cứng cáp như thép tấm gia cường!". Bố cục: Mặt cắt giải phẫu X-quang vùng mông chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng: xương chậu và xương cụt bọc lớp mô mạc sợi và các tấm sụn dày cộp như thép tấm gia cường cứng cáp.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phía trên là lớp da siêu dày bọc lông rậm rạp, tạo thành một chiếc nắp cống sinh học bất khả xâm phạm!". Bố cục: Mặt cắt lớp da siêu dày phủ lông rậm rạp của chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng trông như một chiếc nắp cống kim loại tròn xoe kiên cố chốt chặn cửa hang.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi bị chó hoang Dingo truy đuổi ráo riết, Wombat lập tức lao đầu vào cửa hang ngầm và... quay chiếc mông bọc thép ra ngoài để bịt kín miệng hang!". Bố cục: chú chó hoang Dingo lông vàng hung dữ răng nanh nhọn hoắt nhưng bị bầm dập hài hước hung dữ nhe răng đuổi theo chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng; chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng nhanh như chớp lao đầu vào hang đất và quay chiếc mông tròn xoe ra ngoài bịt kín miệng hang.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chó hoang lao tới cắn xé điên cuồng, nhưng hàm răng sắc nhọn chỉ cắn trúng tấm khiên sụn cứng trơn trượt, cắn mãi không xuyên thủng mà chỉ tổ mòn răng gãy móng!". Bố cục: chú chó hoang Dingo lông vàng hung dữ răng nanh nhọn hoắt nhưng bị bầm dập hài hước cắn phập vào mông chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng nhưng răng nanh bị trượt ra ngoài, ôm mõm kêu ăng ẳng gãy răng đau đớn.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa hết, các kỹ sư hãy nhìn xuống vùng bụng của nó: là loài thú có túi giống chuột túi Kangaroo, nhưng nếu cửa túi của chuột túi hướng lên trên, thì cửa túi của Wombat lại quay ngược hoàn toàn về phía sau! Đây là giải pháp công học thiên tài:". Bố cục: So sánh chiếc túi có túi: BÊN TRÁI chuột túi Kangaroo có miệng túi mở hướng lên trên; BÊN PHẢI chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng có miệng túi quay ngược hoàn toàn về phía sau.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "khi gã dùng hai bàn chân trước có móng vuốt thép cào đất tung tóe đào những đường hầm sâu 20-30m, toàn bộ đất cát bắn ra phía sau mà không hề có một hạt bụi nào lọt vào túi làm nghẹt thở đứa con non bé nhỏ bên trong!". Bố cục: chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng dùng hai bàn chân trước cào đất tung tóe đào đường hầm sâu 20-30m, đất cát bắn ra phía sau nhưng đứa con non trong túi vẫn ngủ ngon lành.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phía trước đầu xe tăng còn được lắp đặt một cặp mũi khoan sinh học thượng hạng: bốn chiếc răng cửa to bản mọc dài liên tục suốt đời giống hệt loài gặm nhấm! Lớp men răng trước dày cứng cọ sát với lớp ngà mềm phía sau tạo thành lưỡi đục tự mài sắc bén,". Bố cục: Cận cảnh hàm răng trước của chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng: bốn chiếc răng cửa to bản sắc như lưỡi đục kim loại, men răng trước dày cứng tự mài sắc bén.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "có thể gặm đứt phăng rễ cây bạch đàn cổ thụ và cắn thủng cả ống nhựa công trình của con người!". Bố cục: chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng gặm đứt đôi rễ cây bạch đàn cổ thụ to bằng bắp tay và gặm thủng cả ống nhựa công trình một cách dễ dàng.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đầu là máy khoan mũi nhọn, đuôi là khiên thép chống đạn, đúng là cỗ máy đào công binh hoàn hảo kín kẽ!". Bố cục: Mô hình tổng thể xe bọc thép: đầu là mũi khoan đục rễ cây, thân là máy xúc, đuôi là khiên chống đạn; bảng Module 1 bật PASS.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Module kỹ thuật số hai: Dây chuyền cơ học đúc phân hình khối lập phương! Đây là bí ẩn cơ học từng làm đau đầu giới khoa học suốt hàng thế kỷ.". Bố cục: Bảng bản vẽ kỹ thuật hiện MODULE 2: DÂY CHUYỀN ĐÚC PHÂN KHỐI LẬP PHƯƠNG; mô hình các hình khối phân tròn elip của loài vật khác. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mọi loài vật từ voi, bò, chim cho đến con người khi thải phân đều tạo ra hình trụ tròn hoặc khối dẹt elip do sự co thắt đồng tâm của cơ vòng hậu môn.". Bố cục: Mô hình các khối phân tròn hoặc elip của động vật có vú do cơ vòng hậu môn đồng tâm co bóp. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng Xe Tăng Đào Hầm của chúng ta thì đi vệ sinh ra... những viên xúc xắc vuông chằn chặn có đủ 6 mặt phẳng!". Bố cục: chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng ngồi thảnh thơi trên tảng đá, phía sau thải ra những viên phân hình khối lập phương vuông vức có đủ 6 mặt phẳng như những viên xúc xắc.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trời đất ơi chỉ huy ơi, có phải hậu môn của nó có hình vuông giống như khuôn làm bánh không ạ? Trợ lý đoán sai bét rồi nhé!". Bố cục: cô trợ lý kỹ thuật hoạt hình mặc áo phản quang vàng cầm chiếc khuôn làm bánh hình vuông ngơ ngác hỏi chỉ huy; người kỹ sư trưởng hoạt hình mặc áo phản quang cam cầm bản vẽ kỹ thuật cuộn tròn và thước đo bật cười giải thích bí ẩn.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 2019, nhóm nghiên cứu của tiến sĩ Patricia Yang tại Viện Công nghệ Georgia đã đưa một chú Wombat vào máy chụp cắt lớp CT và đoạt luôn giải Nobel Vật lý Ig Nobel danh giá! Hậu môn của nó vẫn tròn xoe như mọi loài vật khác.". Bố cục: Máy chụp cắt lớp CT của tiến sĩ Patricia Yang và cúp giải thưởng Ig Nobel 2019 rực rỡ; hậu môn của Wombat vẫn tròn xoe như bình thường.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bí mật cơ khí thực sự nằm ở 8% chiều dài cuối cùng của ruột già!". Bố cục: Sơ đồ đường ruột của chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng: mũi tên chỉ vào 8% chiều dài cuối cùng của ruột già nơi diễn ra quá trình đúc nén hình học kỳ diệu.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong công bố chi tiết trên tạp chí Soft Matter năm 2021, các nhà vật lý phát hiện thành ruột già của Wombat có tính đàn hồi không đồng nhất: có hai dải cơ cứng đối diện nhau và hai dải cơ mềm linh hoạt xen kẽ!". Bố cục: Mặt cắt ruột già trên tạp chí Soft Matter 2021: hai dải cơ cứng đối diện nhau và hai dải cơ mềm linh hoạt co bóp nhịp nhàng.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Suốt hành trình tiêu hóa kéo dài 2 tuần, chất xơ thô ráp được vắt kiệt nước và nén chặt lại. Khi khối chất thải đi qua đoạn ruột đặc biệt này, các đợt co bóp nhịp nhàng tác động lực ép khác nhau, nặn khối phân thành những cạnh sắc và 4 mặt phẳng đều tăm tắp!". Bố cục: Timeline tiêu hóa 2 tuần: chất xơ thô ráp được vắt kiệt nước và nén chặt nặn thành 4 mặt phẳng đều tăm tắp như khuôn gạch. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi đêm, một chú Wombat sản xuất đều đặn từ 80-100 viên gạch phân hình khối lập phương! Tại sao tạo hóa lại bắt nó làm việc như dây chuyền nhà máy gạch? Câu trả lời là để đánh dấu lãnh thổ!". Bố cục: chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng đứng cạnh một chồng tháp gồm 80-100 viên gạch phân lập phương vuông vức xếp ngay ngắn như công trường xây dựng mini.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Wombat có thị lực cực kém, nó dùng mùi phân để giao tiếp và đặt phân lên trên những tảng đá cao hoặc thân cây đổ.". Bố cục: chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng với cặp kính cận dày cộp cẩn thận đặt viên phân vuông lên đỉnh mỏm đá nhọn và thân cây đổ để đánh dấu ranh giới mùi hương.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu phân hình tròn, nó sẽ lăn tọt xuống rãnh; nhưng phân hình khối lập phương thì nằm im bất động không lăn đi đâu được! Đúng là thiết kế chống lăn đỉnh cao của tạo hóa!". Bố cục: So sánh hai hình thái: viên phân hình tròn lăn tọt xuống rãnh nước; còn viên phân hình khối lập phương nằm im bất động trên gờ đá, thiết kế chống lăn đỉnh cao.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hiện tượng cơ học này kỳ diệu đến mức các kỹ sư vật liệu tại viện nghiên cứu đang mô phỏng cấu trúc ruột của Wombat để chế tạo các khuôn đúc công nghiệp thế hệ mới: chế tạo các sản phẩm đất sét, gốm sứ và linh kiện hình khối rỗng mà không cần dùng đến dao cắt cơ học!". Bố cục: Các kỹ sư công nghiệp tại viện nghiên cứu mô phỏng ruột Uôm-bát để chế tạo khuôn đúc gốm sứ và linh kiện rỗng không cần dao cắt.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một chú gấu túi béo ục ịch lại đang dạy cho các kỹ sư hàng đầu thế giới bài học vỡ lòng về thủy lực học và tạo hình vật liệu!". Bố cục: chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng đứng trên bục giảng đường đại học đội mũ cử nhân, giảng bài cho các kỹ sư hàng đầu thế giới về thủy lực học và tạo hình vật liệu; bảng Module 2 bật PASS.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Module kỹ thuật số ba: Kịch bản tác chiến phòng ngự phản công! Đừng nghĩ tấm khiên mông của Xe Tăng Đào Hầm chỉ biết đứng im chịu đòn bị động.". Bố cục: Bảng bản vẽ hiện MODULE 3: KỊCH BẢN TÁC CHIẾN PHÒNG NGỰ PHẢN CÔNG; người kỹ sư trưởng hoạt hình mặc áo phản quang cam cầm bản vẽ kỹ thuật cuộn tròn và thước đo mở sơ đồ mặt cắt lòng hang hẹp. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi bị dồn vào đường hầm tối tăm, cỗ máy nặng 35kg này sẽ kích hoạt bài phản công sát thương hủy diệt!". Bố cục: chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng nặng 35kg đứng trong đường hầm tối tăm, đôi mắt nhỏ ánh lên vẻ tự tin chuẩn bị kích hoạt đòn phản công sát thương hủy diệt.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiến thuật bẫy mồi kinh điển: Wombat cố tình bò thụt lùi vào trong lòng hang hẹp, hơi hạ thấp phần mông xuống tạo ra một khe hở vừa đủ trên đầu. Con chó hoang Dingo háo thắng tưởng con mồi đã cùng đường liền thò đầu vào khe hở định ngoạm lấy cổ họng đối phương.". Bố cục: Trong lòng hang đá hẹp: chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng bò thụt lùi vào trong, hơi hạ thấp mông tạo khe hở vừa khít; chú chó hoang Dingo lông vàng hung dữ răng nanh nhọn hoắt nhưng bị bầm dập hài hước thò đầu vào khe hở định ngoạm mồi.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đúng khoảnh khắc chiếc đầu chó hoang chui lọt vào bẫy...". Bố cục: Chiếc đầu của chú chó hoang Dingo lông vàng hung dữ răng nanh nhọn hoắt nhưng bị bầm dập hài hước chui lọt vào khe hở bên trên mông chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng, ánh mắt háo thắng đắc ý tưởng đã thắng thế.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bùm! Wombat dùng hai chân sau gồng cực mạnh toàn bộ cơ bắp, bật chiếc mông bọc thép đội thẳng lên trên! Lực đẩy bằng khối cơ bắp 35kg ép chặt chiếc đầu của kẻ săn mồi nghiền nát vào trần hang đá hoa cương cứng ngắc!". Bố cục: Bùm! chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng dùng hai chân sau gồng cực mạnh bật chiếc mông thép đội thẳng lên trần hang, ép chặt nghiền nát đầu chú chó hoang Dingo lông vàng hung dữ răng nanh nhọn hoắt nhưng bị bầm dập hài hước vào trần đá hoa cương cứng ngắc.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bảo tàng Úc ghi nhận mẫu vật xương hóa thạch được tìm thấy ngoài cửa hang với hộp sọ bị nghiền nát vụn chính là tác phẩm của cú gồng mông uy lực này!". Bố cục: Bên ngoài cửa hang đá: các nhà nghiên cứu bảo tàng Úc ghi nhận dấu vết xương hộp sọ bị nghiền nát của loài chó hoang, minh chứng cho cú gồng mông uy lực. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gâu gâu! Ta tưởng tóm được miếng mồi béo bở, ai ngờ đụng phải tảng đá hoa cương nghiền nát cả đầu!". Bố cục: chú chó hoang Dingo lông vàng hung dữ răng nanh nhọn hoắt nhưng bị bầm dập hài hước ôm đầu bầm dập hoa mắt chóng mặt với những ngôi sao quay cuồng quanh đầu, vừa khóc vừa lồm cồm bò ra khỏi miệng hang.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu phải đánh nhau ngoài bãi cỏ trống trải, gã xe tăng này cũng không ngán đối thủ nào: gã tung ra cú đá lừa ngược bằng hai chân sau uy lực như cú đá của ngựa chứng, hất văng kẻ địch ra xa! Và đừng khinh thường ngoại hình tròn béo lù đù:". Bố cục: Trên bãi cỏ ngoài hang: chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng tung cú đá lừa ngược bằng hai chân sau cực mạnh hất văng một con cáo săn mồi bay lên không trung.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "khi cần tháo chạy nước rút về hang, Wombat có thể tăng tốc lên tới 40km/h trong vòng 90 giây — nhanh ngang ngửa một vận động viên điền kinh Olympic! Kẻ thù chưa kịp định thần thì bóng chiếc mông bọc thép đã biến mất tăm vào lòng đất!". Bố cục: chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng phi nước rút với tốc độ 40km/h trong 90 giây như viên đạn đại bác lao vun vút về cửa hang; bảng Module 3 bật PASS.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Module kỹ thuật số bốn: Phân tích điểm yếu và mối đe dọa sinh tồn! Một cỗ xe tăng có giáp mông chống đạn, chân đào máy xúc, hàm răng gặm gỗ và chạy nhanh 40km/h liệu có bất khả chiến bại trên thảo nguyên hoang dã? Đội kỹ thuật chúng tôi phải chỉ ra ba tử huyệt nghiêm trọng trong thiết kế!". Bố cục: Bảng bản vẽ hiện MODULE 4: PHÂN TÍCH ĐIỂM YẾU VÀ TỬ HUYỆT; người kỹ sư trưởng hoạt hình mặc áo phản quang cam cầm bản vẽ kỹ thuật cuộn tròn và thước đo khoanh vùng các mối đe dọa sinh tồn. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thứ nhất là thị lực cực kỳ tệ hại: mắt của Wombat bị cận thị nặng, ban đêm đi kiếm ăn chỉ dựa vào khứu giác và thính giác, nên gã rất hay húc đầu vào gốc cây hoặc lững thững băng qua đường cao tốc mà không nhìn thấy đèn xe tải từ xa, biến tai nạn giao thông ban đêm thành nguyên nhân tử vong hàng đầu!". Bố cục: chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng đeo kính cận dày cộp lững thững đi đêm, suýt húc đầu vào gốc cây to bên đường do thị lực kém.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thứ hai là thảm họa ký sinh trùng: căn bệnh ghẻ lở do ve ký sinh làm gã ngứa ngáy dữ dội, rụng lông và suy kiệt cơ thể là mối đe dọa lớn nhất đối với các đàn Wombat hoang dã. Nhưng điều làm người dân Úc yêu quý sinh vật này nhất là nghĩa cử cao đẹp trong những trận đại hạn và cháy rừng lịch sử:". Bố cục: Kính lúp phóng to con ve ghẻ ký sinh gây ngứa ngáy rụng lông; bên cạnh là dấu chấm than cảnh báo dịch bệnh đối với gấu túi. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "mạng lưới hang ngầm dài 30m mát mẻ của Wombat đã trở thành những hầm trú ẩn sinh tồn cứu sống hàng ngàn sinh vật nhỏ như thú có túi, thằn lằn và chim chóc cùng trốn chung một mái nhà! Mạng lưới hang ngầm của Wombat". Bố cục: Khung cảnh ấm áp bình yên: bên trong mạng lưới hang ngầm mát mẻ của chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng, hàng chục con thú nhỏ như thằn lằn, chim chóc cùng ngồi trú ẩn an toàn.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đồ sộ như một mê cung tàu điện ngầm dưới lòng đất: mỗi hang có tới 5-6 cửa thoát hiểm, chiều dài ngoằn ngoèo tới 30m và sâu hơn 3m dưới lòng đất.". Bố cục: Sơ đồ kiến trúc ngầm 3D: hệ thống hang dài 30m, sâu hơn 3m dưới lòng đất với 5-6 cửa thoát hiểm như mạng lưới tàu điện ngầm sinh thái.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ độ sâu này, nhiệt độ bên trong hang luôn mát rượi vào mùa hè và ấm áp vào mùa đông, tạo nên một công trình kiến trúc sinh thái bền vững tuyệt đối!". Bố cục: Biểu đồ nhiệt độ bên trong hang luôn mát rượi vào mùa hè và ấm áp vào mùa đông, tạo nên công trình kiến trúc sinh thái bền vững; bảng Module 4 bật PASS.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tổng kết báo cáo kỹ thuật số 26. Từ một khối thịt tròn ủm lù đù nặng 35kg, Gấu Túi Wombat đã chứng minh một chân lý cơ học vĩ đại:". Bố cục: người kỹ sư trưởng hoạt hình mặc áo phản quang cam cầm bản vẽ kỹ thuật cuộn tròn và thước đo đứng cạnh bàn điều khiển tổng kết báo cáo kỹ thuật số 26, ngắm nhìn mô hình Xe Tăng Đào Hầm với sự nể phục tuyệt đối. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "không cần nanh vuốt dữ tợn, một chiếc mông bọc thép kiên cường cùng một chiến thuật đào hầm thông minh đủ sức giúp nó đứng vững trước mọi kẻ thù tàn bạo nhất!". Bố cục: chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng kiên cường đứng vững giữa thảo nguyên hoang dã với chiếc mông bọc thép kiên cố trước mọi kẻ thù.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo nghiệm thu vũ khí: Đạt điểm 10 tuyệt đối cho cỗ máy công thủ toàn diện và danh hiệu nhà máy đúc gạch phân độc nhất vô nhị hành tinh! Ký tên: kỹ sư trưởng đội giải mã vũ khí!". Bố cục: người kỹ sư trưởng hoạt hình mặc áo phản quang cam cầm bản vẽ kỹ thuật cuộn tròn và thước đo đóng dấu NGHIỆM THU ĐẠT ĐIỂM 10 màu đỏ chót lên bản vẽ; chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng giơ chân trước chào kiểu công binh công trình.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn đội kỹ thuật thì sao? Nếu được chế tạo một bộ giáp công nghệ lấy cảm hứng từ Wombat: chiếc khiên mông chống đạn nghiền nát mọi kẻ bám đuôi, hay dây chuyền đúc phân lập phương chống lăn siêu tiện lợi, anh em chọn trang bị nào? Hãy để lại bình luận bên dưới nhé!". Bố cục: Hai bàn cân lựa chọn: BÊN TRÁI biểu tượng chiếc khiên mông chống đạn nghiền sọ; BÊN PHẢI biểu tượng khuôn đúc phân lập phương chống lăn, khán giả giơ thẻ bình chọn. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hồ sơ vũ khí số 26 xin chính thức đóng lại. Nhưng tập sau, chúng ta sẽ chuyển thẳng sang chương trình phóng sự trực tiếp 24 giờ để theo chân một cỗ máy săn mồi tốc độ bàn thờ dưới lòng đất tăm tối!". Bố cục: người kỹ sư trưởng hoạt hình mặc áo phản quang cam cầm bản vẽ kỹ thuật cuộn tròn và thước đo cuộn tròn bản vẽ số 26 lại cất vào hòm sắt, trên màn hình chuyển sang đồng hồ 24 giờ phóng sự điều tra trực tiếp dưới lòng đất tăm tối. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một sinh vật bé nhỏ chỉ nặng 50g, hai mắt mù tịt, nhưng sở hữu chiếc mũi quái đản hình bông hoa gồm 22 xúc tu đỏ hồng rung rinh!". Bố cục: Một sinh vật bí ẩn được vẽ hoàn toàn bằng BÓNG ĐEN ĐẶC TUYỀN (solid black silhouette) nhỏ xíu nặng 50g, chiếc mũi xòe ra 22 xúc tu đỏ hồng như bông hoa sao lấp lánh; có dấu hỏi chấm vàng to tướng; KHÔNG vẽ mắt mũi lông. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tốc độ ăn tối của nó nhanh đến mức khó tin: chỉ mất đúng 0,12 giây để nhận diện và nuốt chửng con mồi, nhanh hơn cả một cái chớp mắt của con người! Đố các bạn biết bóng đen bí ẩn kỳ sau là loài vật nào? Hãy đoán ngay ở phần bình luận nhé!". Bố cục: Đồng hồ siêu tốc đếm 0,12 giây phát sáng: sinh vật bóng đen nuốt chửng con mồi nhanh hơn cái chớp mắt của con người; ba dấu hỏi chấm lớn lấp lánh vàng cam mời gọi khán giả đoán tên. KHÔNG có chú gấu túi đội mũ bảo hộ vàng trong cảnh này.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Sinh vật này sở hữu chiếc mông bọc thép cứng như bê tông,". Bố cục: Khung dọc: chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng khoe chiếc mông bọc thép dày cộp phát sáng hào quang cứng như bê tông.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "chuyên bẫy lừa chó hoang chui đầu vào hang rồi gồng mông dập nát hộp sọ kẻ thù vào trần đá!". Bố cục: chú chó hoang Dingo lông vàng hung dữ răng nanh nhọn hoắt nhưng bị bầm dập hài hước thò đầu vào hang đá, chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng gồng mông dập nát hộp sọ kẻ thù vào trần đá hoa cương.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Xin giới thiệu Gấu Túi Wombat, xe tăng đào hầm nặng 35kg của nước Úc.". Bố cục: chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng mập mạp mũm mĩm đứng cạnh chiếc cân đo 35kg và thước đo chiều cao màu vàng.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Toàn bộ vùng mông của nó được gia cố bằng một tấm khiên sụn và mô sợi dày tới 3cm,". Bố cục: Mặt cắt giải phẫu khung dọc: tấm khiên sụn dày 3cm bảo vệ vùng mông chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng, chú chó hoang Dingo lông vàng hung dữ răng nanh nhọn hoắt nhưng bị bầm dập hài hước cắn vào bị trượt cộp cộp gãy răng.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "khi bị rượt đuổi, nó chui tọt vào hang và lấy chiếc mông sắt bịt kín cửa hang khiến kẻ săn mồi cắn gãy răng!". Bố cục: chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng chui tọt vào hang quay mông bịt kín cửa hang khiến chú chó hoang Dingo lông vàng hung dữ răng nanh nhọn hoắt nhưng bị bầm dập hài hước cắn trúng khiên sụn gãy nanh.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Chưa hết, nó là sinh vật duy nhất trên thế giới đi vệ sinh ra những viên phân hình khối lập phương vuông vức như viên xúc xắc!". Bố cục: chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng ngồi trên mỏm đá khoe các khối phân lập phương có đủ 6 mặt phẳng đều tăm tắp như viên xúc xắc.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Nhờ đoạn ruột già có độ co giãn không đồng đều,". Bố cục: Sơ đồ ruột già co bóp với các dải cơ đàn hồi không đồng nhất tạo cạnh sắc cho khối phân.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "mỗi đêm nó đúc ra 100 viên gạch phân vuông để đánh dấu lãnh thổ trên mỏm đá mà không sợ bị lăn xuống rãnh!". Bố cục: chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng xếp tháp 100 viên gạch phân lập phương vuông vức trên mỏm đá chống lăn xuống rãnh.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Khi cần chạy trốn, gã xe tăng tròn béo này có thể phóng nước rút tới 40km/h!". Bố cục: chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng phi nước rút với tốc độ 40km/h trên bãi cỏ lao vun vút về cửa hang.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Túi Wombat mũm mĩm lông nâu xám, móng vuốt đào đất, mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Một cỗ xe bọc thép vừa lầy lội, vừa sở hữu thiết kế cơ khí đỉnh cao nhất hành tinh!". Bố cục: Chân dung chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng đội mũ bảo hộ vàng giơ ngón tay like bên cạnh tháp gạch phân lập phương ngộ nghĩnh.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/56 của video YouTube về Gấu Túi Wombat). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng. Nhân vật phụ cố định: người kỹ sư trưởng hoạt hình mặc áo phản quang cam cầm bản vẽ kỹ thuật cuộn tròn và thước đo; cô trợ lý kỹ thuật hoạt hình mặc áo phản quang vàng; chú chó hoang Dingo lông vàng hung dữ răng nanh nhọn hoắt nhưng bị bầm dập hài hước. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/10 của video YouTube Shorts về Gấu Túi Wombat). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Gấu Túi Wombat (Vombatidae) hoạt hình lông màu nâu xám dày mượt, thân hình mũm mĩm tròn lẳn lù đù như chiếc thùng rượu nhỏ, đầu to mũi xám lớn, hai mắt tròn xoe hiền lành nhưng lầy lội, hai chân trước có móng vuốt đào đất màu đen cứng cáp, đầu đội chiếc mũ bảo hộ công nhân công trình màu vàng. Nhân vật phụ: chú chó hoang Dingo lông vàng hung dữ răng nanh nhọn hoắt nhưng bị bầm dập hài hước. 
```
</details>

## 7. SEO

- **title:** Cỗ Xe Tăng Nước Úc Có Mông Bọc Thép & Đi Vệ Sinh Ra Hình Lập Phương?!
- **hook_paragraph:** Gấu Túi Wombat (Vombatidae) nặng 35kg sở hữu chiếc mông bọc thép dày 3cm có thể nghiền nát hộp sọ chó hoang Dingo vào trần hang, túi mở ngược về sau chống đất cát và là loài duy nhất đúc ra 100 viên phân hình lập phương mỗi ngày!
- **question:** Nếu được sở hữu 1 trang bị của Gấu Túi Wombat: tấm khiên mông bọc thép hay khả năng đúc phân lập phương chống lăn, bạn chọn cái nào? Và đoán xem bóng đen tập sau là loài nào?
- **next_teaser:** Bóng đen chiếc mũi 22 xúc tu đỏ hồng: tốc độ ăn mồi 0,12 giây nhanh hơn cả chớp mắt!
- **shorts_title:** Cỗ Xe Tăng Có Mông Bọc Thép & Phân Hình Lập Phương?! 🐻 #độngvật #gấutúiwombat
- **shorts_desc:** Gấu Túi Wombat nặng 35kg sở hữu mông bọc thép dày 3cm dập nát sọ Dingo, túi mở ngược và đi vệ sinh ra 100 viên phân hình lập phương mỗi ngày! Giải mã cỗ xe tăng đào hầm nước Úc.
- **bullets:** Bản vẽ cơ khí: Tấm khiên mông bọc thép dày 2-3cm gồm mô mạc sợi và sụn chống mọi cú cắn · Túi mở ngược: Giải pháp công học giúp đất cát không lọt vào con non khi đào hầm 30m · Dây chuyền đúc phân: 8% cuối ruột già nén đúc 80-100 viên phân hình lập phương chống lăn (Ig Nobel 2019) · Thực chiến: Cú đá lừa ngược và kỹ thuật gồng mông nghiền nát hộp sọ Dingo vào trần hang
- **tags:** gấu túi wombat, gau tui wombat, wombat, phân hình lập phương, mông bọc thép, vombatidae, động vật nước úc, động vật kỳ lạ, thế giới động vật, động vật hài hước, vẽ chuyện hoang dã, whiteboard animation, khoa học thú vị
- **hashtags:** #độngvật #gấutúiwombat #VẽChuyệnHoangDã

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-26-gau-tui-wombat
python src/episode/pipeline.py tts    projects/tap-26-gau-tui-wombat     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-26-gau-tui-wombat     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-26-gau-tui-wombat     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-26-gau-tui-wombat              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-26-gau-tui-wombat --force
python scripts/beat_sheet.py projects/tap-26-gau-tui-wombat               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-26-gau-tui-wombat/audio/shorts.wav projects/tap-26-gau-tui-wombat/renders/tap-26-gau-tui-wombat_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-26-gau-tui-wombat
python src/episode/pipeline.py seo    projects/tap-26-gau-tui-wombat
python src/episode/episode_doc.py     projects/tap-26-gau-tui-wombat
```

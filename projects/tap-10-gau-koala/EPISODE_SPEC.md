# TẬP 10 — GẤU KOALA · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-10-gau-koala`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-10-gau-koala`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F1` · **Persona giọng:** `bac_si` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Gấu Koala |
| Tiêu đề YouTube | Bày Đồ Ăn Ra Đĩa Nhưng Thà Nhịn Đói?! \| Gấu Koala \| Tập 10 |
| Video dài | `renders/tap-10-gau-koala_long.mp4` — 9:16.3 (556.3s) |
| Shorts | `renders/tap-10-gau-koala_shorts.mp4` — 0:49.9 (49.9s) |
| Thumbnail | `renders/tap-10-gau-koala_thumbnail.jpg` |
| Số hình | dài 69 beat / 69 ảnh riêng; Shorts 11 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/69 của video YouTube về Gấu Koala). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái. Nhân vật phụ cố định: ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ; cô y tá trợ lý hoạt hình dễ thương đeo kính, mặc đồng phục y tế màu xanh pastel, kẹp bảng hồ sơ. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — THÍ NGHIỆM CHIẾC ĐĨA & CÚ LỪA HỌ NHÀ GẤU
*Thẻ chương:* BÀY SẴN ĐỒ ĂN NHƯNG THÀ NHỊN ĐÓI

*Badge:* `BỆNH ÁN #01` · *mood mặc định:* `nghiem_trang_gia`

**Part 0** → `audio/vs/scene01_p0.wav` (789 ký tự) · mood `nghiem_trang_gia`

```text
Bệnh nhân số mười, mời vào phòng khám! Hồ sơ bệnh án hôm nay dày cộp một cách bất thường, và ca bệnh này khiến toàn bộ hội đồng y bác sĩ của kênh Vẽ Chuyện Hoang Dã phải ôm trán bất lực. Tên bệnh nhân: Cô-a-la. Nghề nghiệp: ôm cây ngủ gật toàn thời gian. Tình trạng bảo hiểm: không có! Điều gì sẽ xảy ra nếu bạn hái một nắm lá khuynh diệp tươi ngon nhất, xếp ngay ngắn lên một chiếc đĩa sứ trắng tinh rồi đặt ngay trước mũi một chú Gấu Cô-a-la đang đói meo bụng sôi sùng sục? Bất kỳ loài thú nào khác trên hành tinh này cũng sẽ đánh chén sạch sành sanh trong một nốt nhạc. Nhưng Bệnh nhân ngơ ngác của chúng ta thì không! Nó sẽ ngồi nhìn chằm chằm vào chiếc đĩa với ánh mắt vô hồn, bất động như tượng đá, và... thà chịu chết đói chứ nhất quyết không chịu thò mồm ăn một cọng lá! [laughter]
```
**Part 1** → `audio/vs/scene01_p1.wav` (71 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Ủa bác sĩ ơi, lá cây mà bứt rời để lên đĩa thì đâu phải là đồ ăn đâu ạ?
```
**Part 2** → `audio/vs/scene01_p2.wav` (885 ký tự) · mood `hao_hung`

```text
[surprise-oh] Các đồng nghiệp nghe thấy câu trả lời ngây thơ của bệnh nhân chưa? Lý do ngớ ngẩn đến mức khó tin: chỉ vì lá cây đã bị bứt rời khỏi cành, bộ não của nó hoàn toàn không nhận diện được đó là thức ăn! Đối với nó, đồ ăn bắt buộc phải mọc dính trên cành cây đung đưa trước gió, còn đặt trên đĩa thì... chắc chắn là đồ chơi hoặc rác rưởi! [laughter] Chưa hết, bệnh nhân này còn thực hiện một cú lừa ngoạn mục đối với toàn nhân loại suốt hơn hai trăm năm qua ngay từ cái tên. Dù từ trẻ con đến người lớn ai cũng gọi là Gấu Cô-a-la, nhưng sinh vật này chẳng có lấy một giọt máu họ hàng nào với loài gấu cả! Chúng là thú có túi chính hiệu của nước Úc, họ hàng ruột thịt gần nhất với loài Uôm-bát mông bọc thép và Chuột túi Canh-gu-ru nhảy lò cò. Hôm nay, phòng khám của chúng ta sẽ bật đèn công suất lớn để mổ xẻ bốn hạng mục kỳ dị nhất từ đầu đến chân của Bệnh nhân ngơ ngác này!
```

### scene02 — HỘP SỌ 40% NƯỚC VÀ BỘ NÃO PHẲNG LÌ NHƯ ỨC GÀ
*Thẻ chương:* HỘP SỌ CHỨA 40% NƯỚC LỎNG

*Badge:* `CHỤP X-QUANG` · *mood mặc định:* `nghiem_trang_gia`

**Part 0** → `audio/vs/scene02_p0.wav` (700 ký tự) · mood `nghiem_trang_gia`

```text
Hạng mục khám đầu tiên: Chụp cắt lớp hộp sọ! Nhìn từ bên ngoài, Bệnh nhân ngơ ngác sở hữu chiếc đầu to tròn, hai tai bông xù cực kỳ bệ vệ và đáng yêu như gấu bông bước ra từ tiệm đồ chơi. Nhưng khi cắm tấm phim chụp X-quang lên bảng đèn soi, bác sĩ chúng tôi suýt nữa ngã ngửa khỏi ghế vì không tin vào mắt mình! [surprise-ah] Bộ não của Cô-a-la chỉ nặng vỏn vẹn khoảng mười bảy gam, chiếm đúng không phẩy hai phần trăm trọng lượng cơ thể — tức là một trong những tỷ lệ não trên cơ thể nhỏ nhất trong toàn bộ thế giới động vật có vú! [laughter] Tới bốn mươi phần trăm thể tích bên trong hộp sọ hoàn toàn không có mô não, mà chỉ ngập đầy chất dịch lỏng bồng bềnh chẳng khác nào một bể cá mini di động!
```
**Part 1** → `audio/vs/scene02_p1.wav` (116 ký tự) · 🎭 cameo `co_tro_ly`

```text
Bác sĩ ơi, em kiểm tra máy chụp X-quang ba lần rồi, não bệnh nhân thực sự... nhẵn bóng không có nếp nhăn nào luôn ạ!
```
**Part 2** → `audio/vs/scene02_p2.wav` (1031 ký tự) · mood `hao_hung`

```text
Đúng thế các đồng nghiệp ạ! Ở các loài thú thông minh như cá heo hay tinh tinh, bề mặt vỏ não chằng chịt hàng ngàn nếp nhăn gấp khúc để tăng diện tích xử lý thông tin phức tạp. Riêng bộ não của Cô-a-la thì... phẳng lì, trơn tuột chẳng khác nào hai miếng ức gà luộc bóc vỏ! [laughter] Sự thiếu vắng nếp nhăn giải thích tại sao Bệnh nhân ngơ ngác mất hoàn toàn khả năng thích ứng: nếu trời đổ mưa bão sấm chớp, nó không biết tìm chỗ trú mà chỉ ngồi im trên cành cây chịu ướt sũng run cầm cập; nếu lá cây rụng xuống đất, nó đứng nhìn đăm đăm như nhìn vật thể ngoài hành tinh! Nhưng chớ vội chê tạo hóa thiết kế lỗi! Việc thu nhỏ não bộ giúp nó tiết kiệm tới hai mươi phần trăm năng lượng cơ thể quý giá. Và đặc biệt nhất, lớp dịch lỏng bốn mươi phần trăm kia hoạt động như một chiếc mũ bảo hiểm đệm nước cực xịn! Vì tính tình ngơ ngác, Cô-a-la rất hay ngủ gật rồi ngã tự do từ ngọn cây cao chót vót xuống đất, và nhờ có bể nước giảm chấn trong đầu, não nó nảy tưng tưng như bóng cao su mà không hề bị chấn thương sọ não! [surprise-oh]
```

### scene03 — RUỘT THỪA 2 MÉT VÀ MÓN CHÁO PHÂN KỲ DỊ
*Thẻ chương:* LÁ ĐỘC XYANUA & CHÁO PHÂN ĐẶC BIỆT

*Badge:* `NỘI SOI DẠ DÀY` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene03_p0.wav` (772 ký tự) · mood `don_dap`

```text
Chuyển sang hạng mục khám thứ hai: Nội soi hệ tiêu hóa! Các đồng nghiệp có từng thắc mắc tại sao Cô-a-la có thể sống ung dung tự tại cả đời trên ngọn cây mà không bao giờ bị bất kỳ loài thú ăn cỏ nào khác tranh giành thức ăn không? [question-ah] Bởi vì thực đơn duy nhất của nó là lá cây khuynh diệp — một kho vũ khí hóa học chết người thực sự! Thứ lá này cứng quai hàm như miếng da thuộc, nghèo calo đến mức tuyệt vọng, lại chứa đầy tinh dầu độc và hợp chất Xy-a-nua đủ sức hạ gục hầu hết các loài động vật khác nếu dám ăn thử vài miếng! Để nhai thứ thuốc độc này trừ cơm ngày qua ngày, Cô-a-la trang bị một lá gan siêu cấp chuyên phân tách độc tố, kết hợp với chiếc manh tràng — tức phần ruột thừa — dài tới hai mét, gấp ba lần chiều dài toàn bộ cơ thể nó! [surprise-wa]
```
**Part 1** → `audio/vs/scene03_p1.wav` (966 ký tự) · mood `hao_hung`

```text
Bên trong đoạn ruột thừa hai mét khổng lồ đó, hàng tỷ vi khuẩn chuyên dụng phải làm việc cật lực suốt bốn ngày liền mới vắt kiệt được từng giọt năng lượng ít ỏi từ lá cây. Và xin đính chính ngay một lời đồn thất thiệt: Cô-a-la không hề ngủ nhiều vì bị say chất kích thích trong lá cây đâu nhé! Chúng bắt buộc phải ngủ li bì tới hai mươi hai tiếng mỗi ngày đơn giản vì cơ thể quá kiệt quệ calo, nếu thức thêm vài tiếng nữa để đi dạo là chúng sẽ... kiệt sức lăn đùng ra vì hết pin! [laughter] Ngay cả cái tên Cô-a-la trong ngôn ngữ thổ dân Đa-rúc cổ xưa cũng có nghĩa là không uống nước. Chúng hấp thụ chín mươi phần trăm lượng nước trực tiếp từ lá cây, và chỉ trong những đợt nắng nóng kỷ lục trên bốn mươi độ C, người ta mới thấy cảnh những chú gấu ngơ ngác mò xuống đất xin nước từ bình cứu hỏa hoặc vòi nước rửa xe của người dân! [surprise-oh] Nhưng ly kỳ nhất là khi Cô-a-la non mới sinh ra, đường ruột hoàn toàn vô trùng, ăn phải lá độc là toi mạng ngay lập tức.
```
**Part 2** → `audio/vs/scene03_p2.wav` (69 ký tự) · 🎭 cameo `be_con`

```text
Mẹ ơi, con đói bụng rồi, cháo của con hôm nay có màu xanh lá đẹp quá!
```
**Part 3** → `audio/vs/scene03_p3.wav` (630 ký tự) · mood `bi_hai`

```text
Bác sĩ đề nghị các đồng nghiệp đang vừa xem video vừa ăn cơm hãy tạm dừng đũa vài giây! Khi con non được sáu tháng tuổi, Cô-a-la mẹ sẽ tiết ra từ hậu môn một loại phân nhão đặc biệt màu xanh lá gọi là cháo Páp. Chú con sẽ thò đầu ra khỏi túi bụng và ăn thứ cháo phân này liên tục suốt một tháng trời ròng rã! [dissatisfaction-hnn] Nghe thì rùng mình rợn tóc gáy, nhưng đó lại là thần dược sinh tồn vĩ đại nhất: nhờ ăn cháo phân của mẹ, ruột con non mới được cấy đầy đủ đội quân vi sinh vật sống để giải độc, sẵn sàng cho cuộc đời nhai lá độc sau này! Đúng là tình mẫu tử thiêng liêng theo phong cách... không ai đỡ nổi! [laughter]
```

### scene04 — BÀN TAY 2 NGÓN CÁI VÀ MÔNG ĐỆM SỤN CHỐNG Ê
*Thẻ chương:* BÀN TAY KÌM SẮT 2 NGÓN CÁI ĐỐI DIỆN

*Badge:* `GIÁM ĐỊNH TỨ CHI` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene04_p0.wav` (734 ký tự) · mood `hao_hung`

```text
Hạng mục khám thứ ba: Tứ chi và cặp mông! Làm thế nào mà một kẻ ngủ gật tới hai mươi hai tiếng mỗi ngày trên ngọn cây cao chót vót đung đưa trong gió bão lại không bao giờ bị rơi cắm đầu xuống đất trong lúc ngáy khò khò? [question-oh] Câu trả lời nằm ở cấu tạo bàn tay quái đản bậc nhất tự nhiên: bàn tay trước của Cô-a-la không có một ngón cái như con người, mà tiến hóa thành hai ngón cái nằm đối diện với ba ngón còn lại! [surprise-oh] Cấu trúc hai ngón cái này biến bàn tay nó thành một chiếc kìm bấm chết cơ khí tự động, khóa chặt vào thân cây ngay cả khi toàn bộ cơ bắp đã ngủ say như chết! Thậm chí bàn chân sau của nó còn có hai ngón dính liền nhau thành một chiếc lược chải lông chuyên dụng để gãi ngứa và bắt bọ chét nữa cơ!
```
**Part 1** → `audio/vs/scene04_p1.wav` (805 ký tự) · mood `nghiem_trang_gia`

```text
Chưa dừng lại ở đó, hãy nhìn xuống phía dưới bàn tọa của Bệnh nhân ngơ ngác! Loài vật này hoàn toàn không có đuôi, nhưng thay vào đó, phần xương cụt của nó phát triển thành một tấm đệm sụn cực dày, bọc thêm lớp lông mông rậm rạp chẳng khác nào một chiếc ghế sô-pha cao cấp gắn liền vào cơ thể. Nhờ có chiếc đệm mông êm ái này, Cô-a-la có thể ngồi kẹp giữa hai chạc cây cứng ngắc suốt hai mươi hai tiếng mỗi ngày mà không hề biết cảm giác ê mông hay mỏi lưng là gì! [laughter] Bộ lông của nó còn có cấu tạo chống thấm nước như một chiếc áo mưa lông cừu, trời mưa xối xả thì nước trượt đi hết, bên trong da vẫn khô ráo ấm áp. Bác sĩ chúng tôi mà ngồi phòng khám liên tục vài tiếng là đã muốn gãy cả cột sống, thế mới thấy trang bị của Bệnh nhân ngơ ngác này quả thực là đỉnh cao của sự lười biếng hưởng thụ!
```

### scene05 — DẤU VÂN TAY GIỐNG NGƯỜI VÀ TIẾNG GẦM QUÁI VẬT
*Thẻ chương:* DẤU VÂN TAY GIỐNG CON NGƯỜI 100%

*Badge:* `GIÁM ĐỊNH PHÁP Y` · *mood mặc định:* `nghiem_trang_gia`

**Part 0** → `audio/vs/scene05_p0.wav` (155 ký tự) · 🎭 cameo `co_tro_ly`

```text
Bác sĩ ơi, đội cảnh sát hình sự vừa gửi sang một mẫu vân tay thu được tại hiện trường vụ trộm, nhìn qua kính hiển vi... giống vân tay con người y đúc luôn!
```
**Part 1** → `audio/vs/scene05_p1.wav` (710 ký tự) · mood `hao_hung`

```text
Báo cáo với các đồng nghiệp, đây là vụ bê bối pháp y chấn động và đau đầu nhất lịch sử nước Úc! [surprise-wa] Dù cách xa loài người tới bảy mươi triệu năm tiến hóa độc lập, nhưng đầu ngón tay của Cô-a-la lại sở hữu những đường vân xoắn ốc giống hệt dấu vân tay của con người! Giống đến mức ngay cả khi đưa vào máy quét kính hiển vi điện tử độ phân giải cao nhất, các chuyên gia giám định hình sự cũng không tài nào phân biệt nổi đâu là dấu vân tay của tên trộm đột nhập và đâu là dấu tay của Bệnh nhân ngơ ngác vừa trèo qua cửa sổ hái trộm lá cây! [laughter] Nếu có một vụ án bí ẩn xảy ra trong rừng khuynh diệp, chắc chắn nghi can số một bị triệu tập lấy lời khai sẽ là một chú Cô-a-la đang ngáp ngủ trên cây!
```
**Part 2** → `audio/vs/scene05_p2.wav` (842 ký tự) · mood `don_dap`

```text
Con đực trưởng thành còn có một tuyến mùi màu nâu nhớp nháp ngay giữa ngực, tỏa ra mùi dầu gió khuynh diệp nồng nặc để cọ vào thân cây đánh dấu lãnh thổ. Nhưng nếu bạn nghĩ một sinh vật mũm mĩm như thú nhồi bông sẽ kêu những tiếng chít chít đáng yêu, thì bạn sắp bị sốc toàn tập rồi đấy! Vào mùa giao phối, những chú Cô-a-la đực phát ra những tiếng rống trầm đục, khàn đặc như tiếng gầm của quái vật thời tiền sử, vang vọng hàng cây số xuyên qua rừng đêm tĩnh mịch! Các nhà giải phẫu phát hiện ngoài thanh quản bình thường, Cô-a-la sở hữu thêm một cặp dây thanh âm khổng lồ nằm ở vòm họng mềm, phát ra âm thanh tần số thấp tới hai mươi bảy Héc — trầm thấp gấp hai mươi lần kích thước cơ thể nhỏ bé của nó! Ngoại hình gấu bông ngây thơ, nhưng khi cất giọng thì rung chuyển cả rừng già khiến du khách cắm trại phải lạnh sống lưng! [surprise-oh]
```

### scene06 — BÁC SĨ BẤT LỰC VÀ BÀI HỌC SINH TỒN
*Thẻ chương:* BÁC SĨ KÊ ĐƠN BẤT LỰC TRƯỚC TẠO HÓA

*Badge:* `KẾT LUẬN Y KHOA` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (897 ký tự) · mood `am_ap`

```text
Kết thúc bản bệnh án hôm nay, bác sĩ chúng tôi phải đưa ra một chẩn đoán đầy xót xa: chính sự thích nghi cực đoan vào cây khuynh diệp đã đẩy Bệnh nhân ngơ ngác vào hai tử huyệt sinh tồn nghiệt ngã của tạo hóa. Thứ nhất, vì lá khuynh diệp chứa nhiều tinh thể cát mịn, sau khoảng mười lăm năm nhai liên tục không ngừng nghỉ, toàn bộ hàm răng của Cô-a-la sẽ bị mài mòn phẳng lì tới tận chân nướu. Và vì không có khả năng thay răng mới như loài chuột, những cá thể già yếu sẽ chết vì đói ngay giữa một rừng cây đầy ắp lá xanh non mơn mởn! [sigh] Thứ hai, bản năng triệu năm dạy chúng rằng mọi kẻ thù nguy hiểm đều bò dưới mặt đất, nên khi xảy ra cháy rừng thảm khốc, phản xạ duy nhất của Cô-a-la là... trèo tọt lên ngọn cây cao nhất rồi ngồi cuộn tròn nhắm mắt chờ đợi, biến chúng thành nạn nhân vô cùng dễ bị tổn thương nếu không có bàn tay giải cứu kịp thời của các tình nguyện viên và lính cứu hỏa.
```
**Part 1** → `audio/vs/scene06_p1.wav` (311 ký tự) · mood `hao_hung`

```text
Tập sau, phòng khám của chúng ta sẽ đón một bệnh nhân ăn chay khổng lồ nhưng lại sở hữu bộ ruột của thú ăn thịt hung dữ: Gấu Trúc Lớn! Nhai tre mười bốn tiếng mỗi ngày, đi vệ sinh bốn mươi lần một ngày, và leo cây ngã lộn cổ như nghệ sĩ xiếc nghiệp dư! Hẹn gặp lại các đồng nghiệp trong hồ sơ bệnh án tiếp theo!
```
**Part 2** → `audio/vs/scene06_p2.wav` (70 ký tự) · 🎭 cameo `co_tro_ly`

```text
Bác sĩ ơi, vậy cuối cùng đơn thuốc của Bệnh nhân ngơ ngác này là gì ạ?
```
**Part 3** → `audio/vs/scene06_p3.wav` (299 ký tự) · mood `hao_hung`

```text
Kê đơn: Cho bệnh nhân ôm cây ngủ tiếp hai mươi hai tiếng mỗi ngày, tuyệt đối đừng ai hái lá bỏ vào đĩa sứ nữa nhé! Ký tên: bác sĩ đã hoàn toàn bất lực! [laughter] Còn bạn, bạn ấn tượng nhất với nét ngớ ngẩn nào của Bệnh nhân ngơ ngác này? Hãy để lại phán quyết của bạn ở phần bình luận bên dưới nhé!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Bày sẵn một đĩa lá tươi ngon ngay trước mặt, nhưng chú Gấu Cô-a-la này thà chịu chết đói chứ nhất quyết không ăn! Lý do là vì lá cây đã bị bứt rời khỏi cành, bộ não của nó hoàn toàn không nhận diện được đó là thức ăn! [laughter] Khi chụp X-quang hộp sọ của Bệnh nhân ngơ ngác này, các bác sĩ đã ngã ngửa: tới bốn mươi phần trăm hộp sọ chỉ chứa toàn nước lỏng, còn bộ não bên trong thì phẳng lì như hai miếng ức gà luộc, không có lấy một nếp nhăn! Nó ăn thứ lá khuynh diệp chứa đầy độc tố Xy-a-nua, sở hữu đoạn ruột thừa dài tới hai mét, và phải ngủ li bì tới hai mươi hai tiếng mỗi ngày để tiết kiệm pin! [surprise-wa] Chưa hết, đầu ngón tay của nó còn có dấu vân tay giống hệt con người khiến cảnh sát hình sự cũng phải bó tay! [question-ah] Bạn có tin một loài vật não phẳng như thế này lại sống sót được hàng triệu năm không? Xem trọn bộ hồ sơ bệnh án trong video dài bên dưới nhé, vì bệnh nhân này...
```

**Whisper prompt:** `Gấu Koala, Bệnh nhân ngơ ngác, thú có túi, Wombat, Kangaroo, X-quang, não phẳng lì, lá khuynh diệp, Xyanua, manh tràng, cháo Pap, 2 ngón cái, vân tay người, dây thanh âm phụ, cháy rừng, Dharug, 90%, 40°C`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| bốn hạng mục | 4 hạng mục |
| hai trăm năm | 200 năm |
| không phẩy hai phần trăm | 0,2% |
| mười bảy gam | 17g |
| bốn mươi phần trăm | 40% |
| năm phần trăm | 5% |
| hai mươi phần trăm | 20% |
| hai mét | 2m |
| ba lần | 3 lần |
| bốn ngày | 4 ngày |
| hai mươi hai tiếng | 22 tiếng |
| sáu tháng | 6 tháng |
| một tháng | 1 tháng |
| hai ngón cái | 2 ngón cái |
| ba ngón | 3 ngón |
| bảy mươi triệu năm | 70 triệu năm |
| hai mươi lần | 20 lần |
| hai mươi bảy Héc | 27 Hz |
| mười lăm năm | 15 năm |
| chín mươi phần trăm | 90% |
| bốn mươi độ C | 40°C |
| mười bốn tiếng | 14 tiếng |
| bốn mươi lần | 40 lần |
| hàng triệu năm | hàng triệu năm |
| triệu năm | triệu năm |
| Cô-a-la | Koala |
| Uôm-bát | Wombat |
| Canh-gu-ru | Kangaroo |
| Xy-a-nua | Xyanua |
| cháo Páp | cháo Pap |
| Đa-rúc | Dharug |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · THÍ NGHIỆM CHIẾC ĐĨA & CÚ LỪA HỌ NHÀ GẤU · 86.3s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:02.3 (2.3s) | L01 | Bệnh nhân số mười, mời vào phòng khám! |  | Phòng khám bệnh viện thú y sáng sủa: Ở GIỮA là bàn khám bệnh bằng kim loại sáng bóng, ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ ngồi bên trái đang lật mở một cuốn sổ bệnh án dày cộp; chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy  |
| b02 | 00:02.3–00:09.5 (7.2s) | L02 | Hồ sơ bệnh án hôm nay dày cộp một cách bất thường, và ca bệnh này khiến toàn bộ hội đồng y bác sĩ của kênh Vẽ Chuyện Hoang Dã phải ôm trán bất lực. Tên bệnh nhân: Koala. |  | ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ đứng BÊN TRÁI giơ tay ôm trán vẻ mặt bất lực, mồ hôi chảy ròng ròng; trên bàn là tập hồ sơ bệnh án dày cộp có dán tấm ảnh chụp chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ng |
| b03 | 00:09.5–00:13.3 (3.8s) | L04 | Nghề nghiệp: ôm cây ngủ gật toàn thời gian. Tình trạng bảo hiểm: không có! |  | chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái đang đu chặt trên một chạc cây khuynh diệp, hai mắt nhắm nghiền ngáy khò khò, bóng chữ 'Zzz' bay lên; một biển hiệu nhỏ cắm bên cạnh ghi hì |
| b04 | 00:13.3–00:21.8 (8.5s) | L06 | Điều gì sẽ xảy ra nếu bạn hái một nắm lá khuynh diệp tươi ngon nhất, xếp ngay ngắn lên một chiếc đĩa sứ trắng tinh rồi đặt ngay trước mũi một chú Gấu Koala đang đói meo bụng sôi sùng |  | Một bàn ăn sang trọng trải khăn trắng: BÊN PHẢI chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái ngồi thắt khăn ăn ở cổ, trước mặt là một chiếc đĩa sứ trắng tinh bày đầy những cành lá khuy |
| b05 | 00:21.8–00:26.5 (4.7s) | L07 | sục? Bất kỳ loài thú nào khác trên hành tinh này cũng sẽ đánh chén sạch sành sanh trong một nốt nhạc. |  | Chia đôi khung hình: BÊN TRÁI một chú thỏ và chú hươu hoạt hình đang há miệng ăn ngấu nghiến đĩa rau củ trong tích tắc; BÊN PHẢI chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái vẫn ngồi b |
| b06 | 00:26.5–00:32.3 (5.8s) | L08 | Nhưng Bệnh nhân ngơ ngác của chúng ta thì không! Nó sẽ ngồi nhìn chằm chằm vào chiếc đĩa với ánh mắt vô hồn, bất động như tượng đá, |  | Cận cảnh biểu cảm cực hài của chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái: ngồi nhìn chằm chằm vào chiếc đĩa sứ trắng trước mặt, ánh mắt vô hồn trống rỗng, trên đầu là một đám mây suy |
| b07 | 00:32.3–00:36.5 (4.2s) | L09 | và... thà chịu chết đói chứ nhất quyết không chịu thò mồm ăn một cọng lá! |  | chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái quay ngoắt mặt đi, hai tay khoanh trước ngực, môi bĩu ra kiên quyết từ chối chiếc đĩa lá; chiếc đĩa lá để trước mặt vẫn nguyên vẹn; bóng dá |
| b08 | 00:36.5–00:41.4 (4.8s) | L10 | Ủa bác sĩ ơi, lá cây mà bứt rời để lên đĩa thì đâu phải là đồ ăn đâu ạ? |  | chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái nhướng mày, một tay chỉ vào chiếc đĩa sứ, miệng há to hỏi ngơ ngác; BÊN TRÁI ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blou |
| b09 | 00:41.4–00:51.5 (10.1s) | L11 | Các đồng nghiệp nghe thấy câu trả lời ngây thơ của bệnh nhân chưa? Lý do ngớ ngẩn đến mức khó tin: chỉ vì lá cây đã bị bứt rời khỏi cành, bộ não của nó hoàn toàn không nhận diện được đó là thức ăn! |  | ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ quay người hướng ra phía người xem, hai tay giơ lên trời vẻ mặt cạn lời sâu sắc; trên bảng đen phía sau vẽ một cành cây có lá mọc dính và dấu tích xanh, bên cạnh là chiếc đĩa đựng lá rời có dấu gạch chéo đỏ. |
| b10 | 00:51.5–00:59.5 (8.0s) | L12 | Đối với nó, đồ ăn bắt buộc phải mọc dính trên cành cây đung đưa trước gió, còn đặt trên đĩa thì... chắc chắn là đồ chơi hoặc rác rưởi! |  | Tâm trí của Koala: một cành cây khuynh diệp xanh tốt đung đưa trong gió có hào quang phát sáng lấp lánh (đồ ăn hợp lệ); bên cạnh chiếc đĩa sứ đựng lá rụng bị vẽ hình thùng rác đồ chơi bốc mùi. |
| b11 | 00:59.5–01:12.4 (12.9s) | L13 | Chưa hết, bệnh nhân này còn thực hiện một cú lừa ngoạn mục đối với toàn nhân loại suốt hơn 200 năm qua ngay từ cái tên. Dù từ trẻ con đến người lớn ai cũng gọi là Gấu Koala, nhưng sinh vật này chẳng có lấy một giọt máu họ hàng nào với loài gấu cả! | **200 NĂM** · cú lừa mạo danh gấu · L/380 · [0.35, 0.5] | chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái đang kéo khóa cởi bỏ bộ đồ hóa trang Gấu Nâu lông dày, lộ ra chiếc túi trước bụng có chú Koala con đang thò đầu ra; KHÔNG có chú Koala áo b |
| b12 | 01:12.4–01:19.6 (7.2s) | L14 | Chúng là thú có túi chính hiệu của nước Úc, họ hàng ruột thịt gần nhất với loài Wombat mông bọc thép và Chuột túi Kangaroo nhảy lò cò. |  | chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái đứng giữa hai người họ hàng: BÊN TRÁI là chú Wombat béo tròn mông bọc thép, BÊN PHẢI là chú Kangaroo chuột túi đang đứng trên hai chân sau; |
| b13 | 01:19.6–01:26.3 (6.7s) | L15 | Hôm nay, phòng khám của chúng ta sẽ bật đèn công suất lớn để mổ xẻ 4 hạng mục kỳ dị nhất từ đầu đến chân của Bệnh nhân ngơ ngác này! | **4 HẠNG MỤC** · khám nghiệm tiến hóa · R/400 · [0.72, 0.45] | ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ bật công tắc đèn mổ sáng rực; trên tường chiếu 4 biểu tượng khám bệnh: một hộp sọ X-quang, một dạ dày cuốn ruột dài, bàn tay 2 ngón cái và cặp vân tay xoắn ốc; chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, m |

### scene02 · HỘP SỌ 40% NƯỚC VÀ BỘ NÃO PHẲNG LÌ NHƯ ỨC GÀ · 91.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:02.2 (2.2s) | L16 | Hạng mục khám đầu tiên: Chụp cắt lớp hộp sọ! |  | Phòng chụp X-quang: cô y tá trợ lý hoạt hình dễ thương đeo kính, mặc đồng phục y tế màu xanh pastel, kẹp bảng hồ sơ đang điều chỉnh chiếc máy chụp X-quang khổng lồ hướng vào đầu chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có i |
| b02 | 00:02.2–00:08.7 (6.4s) | L17 | Nhìn từ bên ngoài, Bệnh nhân ngơ ngác sở hữu chiếc đầu to tròn, hai tai bông xù cực kỳ bệ vệ và đáng yêu như gấu bông bước ra từ tiệm đồ chơi. |  | Cận cảnh chiếc đầu to bự của chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái: đầu tròn xoe, hai tai xù lông to như hai chiếc quạt con, chiếc mũi đen bóng nổi bật; một chiếc thước kẹp đo v |
| b03 | 00:08.7–00:15.0 (6.4s) | L18 | Nhưng khi cắm tấm phim chụp X-quang lên bảng đèn soi, bác sĩ chúng tôi suýt nữa ngã ngửa khỏi ghế vì không tin vào mắt mình! |  | ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ cắm tấm phim chụp X-quang lên bảng đèn sáng: phim chụp cho thấy một hộp sọ to lớn nhưng bên trong chứa đầy chất lỏng màu xanh nước biển, ở giữa chỉ có một bộ não bé xíu như hạt nho đang nổi lơ lửng. |
| b04 | 00:15.0–00:24.8 (9.8s) | L19 | Bộ não của Koala chỉ nặng vỏn vẹn khoảng 17g, chiếm đúng 0,2% trọng lượng cơ thể — tức là một trong những tỷ lệ não trên cơ thể nhỏ nhất trong toàn bộ thế giới động vật có vú! | **17 GAM** · khối lượng não · L/350 · [0.3, 0.55]<br>**0,2%** · tỷ lệ não trên cơ thể · R/480 · [0.7, 0.5] | BÊN TRÁI là một chiếc cân tiểu ly điện tử đặt bộ não Koala bé tí; BÊN PHẢI chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái ngồi nhìn chiếc cân ngạc nhiên. |
| b05 | 00:24.8–00:32.4 (7.6s) | L20 | Tới 40% thể tích bên trong hộp sọ hoàn toàn không có mô não, mà chỉ ngập đầy chất dịch lỏng bồng bềnh chẳng khác nào một bể cá mini di động! | **40%** · hộp sọ là dịch lỏng · L/360 · [0.45, 0.5] | Mô hình cắt ngang hộp sọ Koala: chiếc hộp sọ được vẽ như một bể cá cảnh mini chứa đầy nước xanh lỏng, bên trong có bộ não nhỏ nổi bồng bềnh, vài chú cá nhỏ hoạt hình bơi lượn quanh não; KHÔNG có chú Koala áo bệnh nhân trong cảnh này. |
| b06 | 00:32.4–00:38.6 (6.2s) | L21 | Bác sĩ ơi, em kiểm tra máy chụp X-quang 3 lần rồi, não bệnh nhân thực sự... nhẵn bóng không có nếp nhăn nào luôn ạ! |  | cô y tá trợ lý hoạt hình dễ thương đeo kính, mặc đồng phục y tế màu xanh pastel, kẹp bảng hồ sơ cầm tấm phim chụp X-quang soi lên trước mắt, vẻ mặt sửng sốt lắc đầu; bên cạnh chiếc máy chụp X-quang phát ra tia sáng quét. |
| b07 | 00:38.6–00:53.2 (14.7s) | L22 | Đúng thế các đồng nghiệp ạ! Ở các loài thú thông minh như cá heo hay tinh tinh, bề mặt vỏ não chằng chịt hàng ngàn nếp nhăn gấp khúc để tăng diện tích xử lý thông tin phức tạp. Riêng bộ não của Koala thì... phẳng lì, trơn tuột chẳng khác nào hai miếng ức gà luộc bóc vỏ! |  | So sánh đối đầu giữa 2 bộ não: BÊN TRÁI là bộ não cá heo/con người chằng chịt nếp nhăn lấp lánh tia sét trí tuệ; BÊN PHẢI là bộ não Koala nhẵn bóng, phẳng lì như hai miếng ức gà luộc màu hồng phấn. |
| b08 | 00:53.2–01:03.1 (9.9s) | L23 | Sự thiếu vắng nếp nhăn giải thích tại sao Bệnh nhân ngơ ngác mất hoàn toàn khả năng thích ứng: nếu trời đổ mưa bão sấm chớp, nó không biết tìm chỗ trú mà chỉ ngồi im trên cành cây chịu ướt sũng run |  | Cảnh trời mưa bão sấm chớp ầm ĩ: các loài thú khác chạy tìm hang trú ẩn, riêng chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái vẫn ngồi đơ trên chạc cây ướt sũng như chuột lột, mắt mở to  |
| b09 | 01:03.1–01:07.6 (4.5s) | L24 | cầm cập; nếu lá cây rụng xuống đất, nó đứng nhìn đăm đăm như nhìn vật thể ngoài hành tinh! |  | Một chiếc lá khuynh diệp rụng từ cành cây xuống mặt đất ngay trước chân chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái; chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, h |
| b10 | 01:07.6–01:14.4 (6.8s) | L25 | Nhưng chớ vội chê tạo hóa thiết kế lỗi! Việc thu nhỏ não bộ giúp nó tiết kiệm tới 20% năng lượng cơ thể quý giá. | **20%** · tiết kiệm pin cơ thể · L/380 · [0.35, 0.45] | Biểu đồ năng lượng cơ thể: trên đầu chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái là biểu tượng cục pin cạn đáy nhấp nháy màu đỏ 5%; bộ não thu nhỏ được khoanh vùng tiết kiệm năng lượng |
| b11 | 01:14.4–01:20.0 (5.6s) | L26 | Và đặc biệt nhất, lớp dịch lỏng 40% kia hoạt động như một chiếc mũ bảo hiểm đệm nước cực xịn! | **ĐỆM NƯỚC** · chống chấn thương sọ · R/380 · [0.65, 0.45] | Hộp sọ Koala được vẽ như một chiếc mũ bảo hiểm có túi khí đệm nước dày cộp bao quanh não; một chiếc búa đồ chơi gõ vào mũ bảo hiểm bị bật nảy ra ngoài êm ái. |
| b12 | 01:20.0–01:31.7 (11.7s) | L27 | Vì tính tình ngơ ngác, Koala rất hay ngủ gật rồi ngã tự do từ ngọn cây cao chót vót xuống đất, và nhờ có bể nước giảm chấn trong đầu, não nó nảy tưng tưng như bóng cao su mà không hề bị chấn thương sọ não! |  | chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái đang ngủ gật ôm cành cây thì trượt tay ngã lộn cổ từ trên cao xuống đất; đầu chạm đất nảy tưng tưng như quả bóng cao su, chú đứng dậy chớp  |

### scene03 · RUỘT THỪA 2 MÉT VÀ MÓN CHÁO PHÂN KỲ DỊ · 119.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:11.1 (11.1s) | L28 | Chuyển sang hạng mục khám thứ hai: Nội soi hệ tiêu hóa! Các đồng nghiệp có từng thắc mắc tại sao Koala có thể sống ung dung tự tại cả đời trên ngọn cây mà không bao giờ bị bất kỳ loài thú ăn cỏ nào khác tranh giành thức ăn không? |  | Phòng nội soi tiêu hóa: ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ cầm ống nội soi mềm có camera gắn đèn soi vào bụng chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hì |
| b02 | 00:11.1–00:15.7 (4.6s) | L29 | Bởi vì thực đơn duy nhất của nó là lá cây khuynh diệp — một kho vũ khí hóa học chết người thực sự! |  | Cây khuynh diệp tỏa ra luồng khói xanh hình đầu lâu xương chéo độc hại; các loài thỏ rừng, chuột túi chạy dạt ra xa bịt mũi ho sặc sụa; chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái vắt |
| b03 | 00:15.7–00:24.8 (9.1s) | L30 | Thứ lá này cứng quai hàm như miếng da thuộc, nghèo calo đến mức tuyệt vọng, lại chứa đầy tinh dầu độc và hợp chất Xyanua đủ sức hạ gục hầu hết các loài động vật khác nếu dám ăn thử vài miếng! |  | BÊN TRÁI lá khuynh diệp được vẽ cứng như một tấm da thuộc đóng đinh gỉ sét, bên cạnh có lọ độc chất Xyanua; BÊN PHẢI chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái ngoạm chiếc lá nghe ti |
| b04 | 00:24.8–00:35.8 (11.0s) | L31 | Để nhai thứ thuốc độc này trừ cơm ngày qua ngày, Koala trang bị một lá gan siêu cấp chuyên phân tách độc tố, kết hợp với chiếc manh tràng — tức phần ruột thừa — dài tới 2m, gấp 3 lần chiều dài toàn bộ cơ thể nó! | **2 MÉT** · chiều dài ruột thừa · R/360 · [0.72, 0.5]<br>**3 LẦN** · dài gấp 3 cơ thể · L/480 · [0.3, 0.6] | Sơ đồ giải phẫu dạ dày Koala: BÊN TRÁI lá gan đeo mặt nạ phòng độc lọc hóa chất; BÊN PHẢI đoạn manh tràng (ruột thừa) dài ngoằn ngoèo 2 mét uốn lượn như con trăn khổng lồ. |
| b05 | 00:35.8–00:44.1 (8.3s) | L32 | Bên trong đoạn ruột thừa 2m khổng lồ đó, hàng tỷ vi khuẩn chuyên dụng phải làm việc cật lực suốt 4 ngày liền mới vắt kiệt được từng giọt năng lượng ít ỏi từ lá | **4 NGÀY** · thời gian tiêu hóa · L/380 · [0.45, 0.5] | Bên trong lòng ruột Koala: hàng ngàn chú vi khuẩn tí hon đội mũ công nhân, cầm búa và kéo mini miệt mài cắt nhỏ và nghiền nát các phiến lá độc suốt 4 ngày đêm. |
| b06 | 00:44.1–00:50.9 (6.9s) | L33 | cây. Và xin đính chính ngay một lời đồn thất thiệt: Koala không hề ngủ nhiều vì bị say chất kích thích trong lá cây đâu |  | chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái nằm dài trên chạc cây ngáy khò khò, ôm chặt thân cây, cục pin trên đầu báo cạn 0%; không có chất kích thích nào, chỉ là cơ thể đang tắt ngu |
| b07 | 00:50.9–01:01.1 (10.1s) | L69 | nhé! Chúng bắt buộc phải ngủ li bì tới 22 tiếng mỗi ngày đơn giản vì cơ thể quá kiệt quệ calo, nếu thức thêm vài tiếng nữa để đi dạo là chúng sẽ... kiệt sức lăn đùng ra vì hết pin! | **22 TIẾNG** · ngủ li bì mỗi ngày · R/360 · [0.65, 0.45] | Koala ngủ li bì 22 tiếng mỗi ngày trên cây vì cơ thể kiệt quệ calo; chiếc đồng hồ chỉ 22 giờ ngủ. |
| b08 | 01:01.1–01:08.9 (7.8s) | L34 | Ngay cả cái tên Koala trong ngôn ngữ thổ dân Dharug cổ xưa cũng có nghĩa là không uống nước. Chúng hấp thụ 90% lượng nước trực tiếp từ lá | **90% NƯỚC** · hấp thụ từ lá cây · R/400 · [0.68, 0.5] | Bản đồ sa mạc Úc dưới cái nắng chói chang: BÊN TRÁI một thổ dân Úc cổ xưa giơ tay vẽ biểu tượng 'không uống nước'; BÊN PHẢI chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái ngồi trên cây n |
| b09 | 01:08.9–01:18.5 (9.6s) | L35 | cây, và chỉ trong những đợt nắng nóng kỷ lục trên 40°C, người ta mới thấy cảnh những chú gấu ngơ ngác mò xuống đất xin nước từ bình cứu hỏa hoặc vòi nước rửa xe của người dân! | **40°C** · nắng nóng kỷ lục · L/360 · [0.3, 0.4] | Ngày hè nắng gắt bốc hơi: chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái tụt xuống đất đứng cạnh chiếc xe đạp, hai tay ôm bình nước của một vận động viên đạp xe đang tươi cười dốc nước c |
| b10 | 01:18.5–01:25.5 (7.0s) | L36 | Nhưng ly kỳ nhất là khi Koala non mới sinh ra, đường ruột hoàn toàn vô trùng, ăn phải lá độc là toi mạng ngay lập tức. |  | Một chú Koala sơ sinh bé xíu chỉ bằng hạt đậu đỏ nằm trong túi mẹ màu hồng nhạt, cơ thể trong suốt vô trùng; phía trên chiếc lá độc đe dọa. |
| b11 | 01:25.5–01:29.5 (4.0s) | L37 | Mẹ ơi, con đói bụng rồi, cháo của con hôm nay có màu xanh lá đẹp quá! |  | Chú Koala con lông tơ thò đầu ra khỏi túi bụng của Koala mẹ, hai mắt to long lanh há mỏ chờ đợi; Koala mẹ cúi đầu âu yếm. |
| b12 | 01:29.5–01:33.8 (4.3s) | L38 | Bác sĩ đề nghị các đồng nghiệp đang vừa xem video vừa ăn cơm hãy tạm dừng đũa vài giây! |  | ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ hốt hoảng giơ hai tay ra hiệu 'dừng đũa' về phía màn hình; trên bàn ăn bên cạnh là bát cơm và đôi đũa bị gác lại. |
| b13 | 01:33.8–01:44.9 (11.1s) | L39 | Khi con non được 6 tháng tuổi, Koala mẹ sẽ tiết ra từ hậu môn một loại phân nhão đặc biệt màu xanh lá gọi là cháo Pap. Chú con sẽ thò đầu ra khỏi túi bụng và ăn thứ cháo phân này liên tục suốt 1 tháng trời ròng rã! | **6 THÁNG** · bắt đầu ăn dặm · L/360 · [0.3, 0.45]<br>**1 THÁNG** · ăn cháo phân mẹ · R/480 · [0.7, 0.6] | Bữa ăn dặm kỳ lạ: Koala mẹ tiết ra chất sệt màu xanh lá cây từ phía sau; Koala con thò đầu ra ăn ngon lành, khuôn mặt rạng rỡ hạnh phúc. |
| b14 | 01:44.9–01:59.9 (15.0s) | L40 | Nghe thì rùng mình rợn tóc gáy, nhưng đó lại là thần dược sinh tồn vĩ đại nhất: nhờ ăn cháo phân của mẹ, ruột con non mới được cấy đầy đủ đội quân vi sinh vật sống để giải độc, sẵn sàng cho cuộc đời nhai lá độc sau này! Đúng là tình mẫu tử thiêng liêng theo phong cách... không ai đỡ nổi! |  | Các chú vi khuẩn có lợi thân thiện màu xanh ngọc nhảy múa diễu hành từ bát cháo phân đi thẳng vào dạ dày của Koala con, tạo nên tấm khiên bảo vệ phát sáng chống lại độc tố lá cây. |

### scene04 · BÀN TAY 2 NGÓN CÁI VÀ MÔNG ĐỆM SỤN CHỐNG Ê · 75.1s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:12.1 (12.1s) | L41 | Hạng mục khám thứ ba: Tứ chi và cặp mông! Làm thế nào mà một kẻ ngủ gật tới 22 tiếng mỗi ngày trên ngọn cây cao chót vót đung đưa trong gió bão lại không bao giờ bị rơi cắm đầu xuống đất trong lúc ngáy khò khò? |  | Phòng khám kiểm tra chi: ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ cầm kính lúp to soi vào bàn tay trước của chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ t |
| b02 | 00:12.1–00:22.8 (10.8s) | L42 | Câu trả lời nằm ở cấu tạo bàn tay quái đản bậc nhất tự nhiên: bàn tay trước của Koala không có một ngón cái như con người, mà tiến hóa thành 2 ngón cái nằm đối diện với 3 ngón còn lại! | **2 NGÓN CÁI** · đối diện 3 ngón · L/350 · [0.35, 0.5]<br>**3 NGÓN** · gọng kìm kẹp cây · R/480 · [0.65, 0.5] | Cận cảnh bàn tay trước của Koala như một bản vẽ kỹ thuật: bàn tay có 2 ngón cái đối diện với 3 ngón thường, tạo thành chiếc gọng kìm kẹp chặt lấy thân cành cây tròn. |
| b03 | 00:22.8–00:31.0 (8.2s) | L43 | Cấu trúc 2 ngón cái này biến bàn tay nó thành một chiếc kìm bấm chết cơ khí tự động, khóa chặt vào thân cây ngay cả khi toàn bộ cơ bắp đã ngủ say như chết! |  | Hình minh họa chiếc kìm bấm chết cơ khí bằng thép kẹp cứng ngắc vào ống cành cây; bên cạnh bàn tay Koala bấm ngập móng vuốt vào vỏ cây, không thể lay chuyển. |
| b04 | 00:31.0–00:38.3 (7.3s) | L44 | Thậm chí bàn chân sau của nó còn có hai ngón dính liền nhau thành một chiếc lược chải lông chuyên dụng để gãi ngứa và bắt bọ chét nữa cơ! |  | Cận cảnh bàn chân sau của Koala: ngón số 2 và ngón số 3 dính liền nhau có hai chiếc móng vuốt song song như răng lược, đang chải chuốt lớp lông tơ mượt mà gạt bọ chét rơi lả tả. |
| b05 | 00:38.3–00:51.8 (13.5s) | L45 | Chưa dừng lại ở đó, hãy nhìn xuống phía dưới bàn tọa của Bệnh nhân ngơ ngác! Loài vật này hoàn toàn không có đuôi, nhưng thay vào đó, phần xương cụt của nó phát triển thành một tấm đệm sụn cực dày, bọc thêm lớp lông mông rậm rạp chẳng khác nào một chiếc ghế sô-pha cao cấp gắn liền vào cơ thể. |  | Mặt sau của chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái: chú không hề có đuôi, vùng mông tròn trĩnh có một lớp sụn cứng lót đệm dày như chiếc gối sofa êm ái. |
| b06 | 00:51.8–00:60.0 (8.2s) | L46 | Nhờ có chiếc đệm mông êm ái này, Koala có thể ngồi kẹp giữa hai chạc cây cứng ngắc suốt 22 tiếng mỗi ngày mà không hề biết cảm giác ê mông hay mỏi lưng là gì! | **22 TIẾNG** · ngồi không biết mỏi · L/380 · [0.45, 0.5] | chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái ngồi lọt thỏm êm ru trên chạc cây chữ V cứng nhọn, mặt thư giãn nhắm nghiền mắt mỉm cười như đang ngồi ghế massage hạng thương gia. |
| b07 | 00:60.0–01:07.3 (7.3s) | L47 | Bộ lông của nó còn có cấu tạo chống thấm nước như một chiếc áo mưa lông cừu, trời mưa xối xả thì nước trượt đi hết, bên trong da vẫn khô ráo ấm áp. |  | Cơn mưa rào trút nước xuống: những giọt nước mưa rơi vào lưng chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái lập tức trượt tròn lăn ra ngoài như nước đổ lá khoai; bên trong lớp lông vẫn  |
| b08 | 01:07.3–01:15.1 (7.8s) | L48 | Bác sĩ chúng tôi mà ngồi phòng khám liên tục vài tiếng là đã muốn gãy cả cột sống, thế mới thấy trang bị của Bệnh nhân ngơ ngác này quả thực là đỉnh cao của sự lười biếng hưởng thụ! |  | ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ ngồi còng lưng trên chiếc ghế xoay phòng khám, tay đấm lưng 'thùm thụp' vì đau cột sống; quay sang nhìn chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng |

### scene05 · DẤU VÂN TAY GIỐNG NGƯỜI VÀ TIẾNG GẦM QUÁI VẬT · 84.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.2 (8.2s) | L49 | Bác sĩ ơi, đội cảnh sát hình sự vừa gửi sang một mẫu vân tay thu được tại hiện trường vụ trộm, nhìn qua kính hiển vi... giống vân tay con người y đúc luôn! |  | cô y tá trợ lý hoạt hình dễ thương đeo kính, mặc đồng phục y tế màu xanh pastel, kẹp bảng hồ sơ chạy vội vào phòng khám cầm theo một bìa hồ sơ cảnh sát có dấu mộc đỏ 'TỐI MẬT' và một tấm kính soi dấu vân tay màu đen. |
| b02 | 00:08.2–00:14.2 (6.0s) | L50 | Báo cáo với các đồng nghiệp, đây là vụ bê bối pháp y chấn động và đau đầu nhất lịch sử nước Úc! |  | Bản tin pháp y chấn động: hai thám tử cảnh sát mặc áo măng-tô cầm kính lúp soi dấu vân tay xoắn ốc trên khung cửa sổ hiện trường vụ án trộm cắp. |
| b03 | 00:14.2–00:22.7 (8.4s) | L51 | Dù cách xa loài người tới 70 triệu năm tiến hóa độc lập, nhưng đầu ngón tay của Koala lại sở hữu những đường vân xoắn ốc giống hệt dấu vân tay của con người! | **70 TR NĂM** · tiến hóa độc lập · L/380 · [0.5, 0.4] | So sánh vân tay dưới kính hiển vi điện tử: BÊN TRÁI dấu vân tay người xoắn ốc; BÊN PHẢI dấu vân tay đầu ngón tay Koala có các đường vân, vòng xoáy và móc giống hệt nhau đến từng chi tiết. |
| b04 | 00:22.7–00:36.7 (14.1s) | L70 | Giống đến mức ngay cả khi đưa vào máy quét kính hiển vi điện tử độ phân giải cao nhất, các chuyên gia giám định hình sự cũng không tài nào phân biệt nổi đâu là dấu vân tay của tên trộm đột nhập và đâu là dấu tay của Bệnh nhân ngơ ngác vừa trèo qua cửa sổ hái trộm lá cây! |  | Các chuyên gia giám định hình sự cảnh sát Úc cầm kính hiển vi và máy tính quét vân tay hiện trường bối rối không phân biệt nổi vân tay người hay Koala. |
| b05 | 00:36.7–00:45.2 (8.5s) | L52 | Nếu có một vụ án bí ẩn xảy ra trong rừng khuynh diệp, chắc chắn nghi can số một bị triệu tập lấy lời khai sẽ là một chú Koala đang ngáp ngủ trên cây! |  | Phòng thẩm vấn cảnh sát: một thám tử cảnh sát ngồi đối diện chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái dưới ánh đèn bàn thẩm vấn; chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông mà |
| b06 | 00:45.2–00:51.9 (6.7s) | L53 | Con đực trưởng thành còn có một tuyến mùi màu nâu nhớp nháp ngay giữa ngực, tỏa ra mùi dầu gió khuynh diệp nồng nặc để cọ vào thân cây đánh dấu lãnh |  | Một chú Koala đực lực lưỡng đứng cọ ngực vào thân cây khuynh diệp: giữa ngực có một vệt màu nâu sẫm tiết ra tinh dầu thơm ngát mùi kẹo ngậm bạc hà lan tỏa khắp không gian. |
| b07 | 00:51.9–00:58.7 (6.8s) | L54 | thổ. Nhưng nếu bạn nghĩ một sinh vật mũm mĩm như thú nhồi bông sẽ kêu những tiếng chít chít đáng yêu, thì bạn sắp bị sốc toàn tập rồi đấy! |  | BÊN TRÁI hình ảnh chú Koala thú nhồi bông kêu 'chít chít' dễ thương bị gạch chéo đỏ; BÊN PHẢI chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái đang hít một hơi thật sâu phồng to lồng ngực  |
| b08 | 00:58.7–01:07.1 (8.4s) | L55 | Vào mùa giao phối, những chú Koala đực phát ra những tiếng rống trầm đục, khàn đặc như tiếng gầm của quái vật thời tiền sử, vang vọng hàng cây số xuyên qua rừng đêm tĩnh mịch! |  | chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái mở toang mồm phát ra luồng sóng âm khổng lồ hình đầu quái vật bạo chúa gầm rú; một du khách cắm trại trong lều phía dưới giật nảy mình dựng |
| b09 | 01:07.1–01:17.4 (10.4s) | L56 | Các nhà giải phẫu phát hiện ngoài thanh quản bình thường, Koala sở hữu thêm một cặp dây thanh âm khổng lồ nằm ở vòm họng mềm, phát ra âm thanh tần số thấp tới 27 Hz — trầm thấp gấp 20 lần kích thước cơ thể nhỏ bé của nó! | **27 HZ** · tần số siêu trầm · R/360 · [0.72, 0.45]<br>**GẤP 20 LẦN** · uy lực âm thanh · L/480 · [0.3, 0.6] | Sơ đồ cấu tạo họng Koala: ngoài thanh quản thông thường, phía trên vòm họng mềm có một cặp dây thanh âm phụ khổng lồ màu đỏ phát ra các vòng sóng âm thanh tần số siêu trầm 27 Hz. |
| b10 | 01:17.4–01:24.2 (6.7s) | L71 | Ngoại hình gấu bông ngây thơ, nhưng khi cất giọng thì rung chuyển cả rừng già khiến du khách cắm trại phải lạnh sống lưng! |  | Ngoại hình gấu bông ngây thơ nhưng phát ra tiếng gầm rung chuyển cả khu rừng rậm đêm khiến du khách cắm trại bên dưới rùng mình hoảng hốt. |

### scene06 · BÁC SĨ BẤT LỰC VÀ BÀI HỌC SINH TỒN · 78.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.0 (10.0s) | L57 | Kết thúc bản bệnh án hôm nay, bác sĩ chúng tôi phải đưa ra một chẩn đoán đầy xót xa: chính sự thích nghi cực đoan vào cây khuynh diệp đã đẩy Bệnh nhân ngơ ngác vào hai tử huyệt sinh tồn nghiệt ngã của tạo hóa. |  | ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ đứng bên bảng chẩn đoán y khoa, vẻ mặt trầm ngâm thương cảm; chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ |
| b02 | 00:10.0–00:18.8 (8.8s) | L58 | Thứ nhất, vì lá khuynh diệp chứa nhiều tinh thể cát mịn, sau khoảng 15 năm nhai liên tục không ngừng nghỉ, toàn bộ hàm răng của Koala sẽ bị mài mòn phẳng lì tới tận chân nướu. | **15 NĂM** · răng mòn phẳng lì · L/380 · [0.4, 0.5] | Cận cảnh hàm răng Koala già: những chiếc răng hàm bị mài phẳng lì trơ trụi như đá mài mòn, không còn gờ nhọn để nghiền nát phiến lá cứng; xung quanh là các hạt cát silicat nhỏ li ti. |
| b03 | 00:18.8–00:25.7 (6.8s) | L59 | Và vì không có khả năng thay răng mới như loài chuột, những cá thể già yếu sẽ chết vì đói ngay giữa một rừng cây đầy ắp lá xanh non mơn mởn! |  | Cảnh thương cảm: một chú Koala già ngồi ôm cành cây giữa rừng lá xanh bạt ngàn nhưng không thể nhai được, chiếc bụng đói xẹp xuống; bóng hoàng hôn buông dịu dàng. |
| b04 | 00:25.7–00:36.8 (11.1s) | L60 | Thứ hai, bản năng triệu năm dạy chúng rằng mọi kẻ thù nguy hiểm đều bò dưới mặt đất, nên khi xảy ra cháy rừng thảm khốc, phản xạ duy nhất của Koala là... trèo tọt lên ngọn cây cao nhất rồi ngồi cuộn tròn nhắm mắt chờ đợi, |  | Cảnh báo cháy rừng: phía dưới chân cây là ngọn lửa đỏ rực bốc khói; thay vì chạy xuống đất, chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái lại leo tót lên ngọn cây cao nhất rồi cuộn tròn |
| b05 | 00:36.8–00:43.5 (6.7s) | L61 | biến chúng thành nạn nhân vô cùng dễ bị tổn thương nếu không có bàn tay giải cứu kịp thời của các tình nguyện viên và lính cứu hỏa. |  | Người lính cứu hỏa Úc tốt bụng mặc áo bảo hộ vàng quỳ xuống cạnh gốc cây, ân cần đưa chai nước mát cho chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái vừa được cứu thoát; ánh mắt biết ơn  |
| b06 | 00:43.5–00:50.8 (7.4s) | L62 | Tập sau, phòng khám của chúng ta sẽ đón một bệnh nhân ăn chay khổng lồ nhưng lại sở hữu bộ ruột của thú ăn thịt hung dữ: Gấu Trúc Lớn! |  | Phòng khám hé mở cánh cửa tiếp theo: một chú Gấu Trúc Lớn mập mạp đen trắng đang ngồi bệt dưới đất nhai cây tre rôm rốp, mắt đeo kính cận, vẻ mặt hề hước. |
| b07 | 00:50.8–00:56.7 (5.9s) | L63 | Nhai tre 14 tiếng mỗi ngày, đi vệ sinh 40 lần một ngày, và leo cây ngã lộn cổ như nghệ sĩ xiếc nghiệp dư! | **14 TIẾNG** · nhai tre mỗi ngày · L/360 · [0.35, 0.45]<br>**40 LẦN** · đi vệ sinh/ngày · R/480 · [0.65, 0.5] | Chia 2 nửa: BÊN TRÁI Gấu Trúc nhai tre đống tre cao ngất; BÊN PHẢI chú trèo cây bị gãy cành ngã lộn nhào chổng vó lên trời như diễn viên xiếc. |
| b08 | 00:56.7–00:59.6 (2.9s) | L64 | Hẹn gặp lại các đồng nghiệp trong hồ sơ bệnh án tiếp theo! |  | ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ đứng vẫy tay chào tạm biệt cùng chú Gấu Trúc đang ngậm cành tre; tấm biển 'HẸN GẶP LẠI TẬP 11' treo phía trên. |
| b09 | 00:59.6–01:03.6 (4.0s) | L65 | Bác sĩ ơi, vậy cuối cùng đơn thuốc của Bệnh nhân ngơ ngác này là gì ạ? |  | cô y tá trợ lý hoạt hình dễ thương đeo kính, mặc đồng phục y tế màu xanh pastel, kẹp bảng hồ sơ cầm cây bút bi và cuốn sổ đơn thuốc đưa cho ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ, nghiêng đầu mỉm cười hỏi ý kiến. |
| b10 | 01:03.6–01:09.3 (5.7s) | L66 | Kê đơn: Cho bệnh nhân ôm cây ngủ tiếp 22 tiếng mỗi ngày, tuyệt đối đừng ai hái lá bỏ vào đĩa sứ nữa nhé! | **22 TIẾNG** · đơn thuốc ngủ ngon · R/380 · [0.65, 0.5] | ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ ký ngoáy lên tờ đơn thuốc có ghi dòng chữ hài hước; bên cạnh chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ |
| b11 | 01:09.3–01:12.2 (2.9s) | L67 | Ký tên: bác sĩ đã hoàn toàn bất lực! |  | ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ giơ hai tay ra hiệu chào thua; chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái hé một bê |
| b12 | 01:12.2–01:18.9 (6.6s) | L68 | Còn bạn, bạn ấn tượng nhất với nét ngớ ngẩn nào của Bệnh nhân ngơ ngác này? Hãy để lại phán quyết của bạn ở phần bình luận bên dưới nhé! |  | Hàng ghế khán giả các bạn nhỏ và gia đình đang giơ các biểu tượng mặt cười, trái tim và bóng bình luận sáng rực; chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái ngồi ở giữa mỉm cười thân  |

## 5. Phân cảnh Shorts — từng beat

Banner: **BÀY ĐỒ ĂN RA ĐĨA / NHƯNG THÀ NHỊN ĐÓI?!** · giọng 48.4s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Bày sẵn một đĩa lá tươi ngon ngay trước mặt, nhưng chú Gấu Koala này thà chịu chết đói chứ nhất quyết không ăn! |  |
| s02 | 00:06.5 | S02 | Lý do là vì lá cây đã bị bứt rời khỏi cành, bộ não của nó hoàn toàn không nhận diện được đó là thức ăn! |  |
| s03 | 00:12.5 | S03 | Khi chụp X-quang hộp sọ của Bệnh nhân ngơ ngác này, các bác sĩ đã ngã ngửa: |  |
| s04 | 00:16.6 | S04 | tới 40% hộp sọ chỉ chứa toàn nước lỏng, | **40% NƯỚC** · hộp sọ đệm lỏng · L/650 · [0.5, 0.45] |
| s05 | 00:19.4 | S05 | còn bộ não bên trong thì phẳng lì như hai miếng ức gà luộc, không có lấy một nếp |  |
| s06 | 00:23.6 | S06 | nhăn! Nó ăn thứ lá khuynh diệp chứa đầy độc tố Xyanua, |  |
| s07 | 00:26.9 | S07 | sở hữu đoạn ruột thừa dài tới 2m, | **RUỘT 2M** · lọc độc Xyanua · R/580 · [0.65, 0.5] |
| s08 | 00:28.8 | S08 | và phải ngủ li bì tới 22 tiếng mỗi ngày để tiết kiệm pin! | **NGỦ 22H** · tiết kiệm pin · L/850 · [0.35, 0.7] |
| s09 | 00:32.6 | S09 | Chưa hết, đầu ngón tay của nó còn có dấu vân tay giống hệt con người khiến cảnh sát hình sự cũng phải bó tay! |  |
| s10 | 00:39.3 | S10 | Bạn có tin một loài vật não phẳng như thế này lại sống sót được hàng triệu năm không? |  |
| s11 | 00:43.6 | S11 | Xem trọn bộ hồ sơ bệnh án trong video dài bên dưới nhé, vì bệnh nhân này... |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bệnh nhân số mười, mời vào phòng khám!". Bố cục: Phòng khám bệnh viện thú y sáng sủa: Ở GIỮA là bàn khám bệnh bằng kim loại sáng bóng, ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ ngồi bên trái đang lật mở một cuốn sổ bệnh án dày cộp; chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái ngồi trên bàn khám, vẻ mặt ngơ ngác đờ đẫn.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hồ sơ bệnh án hôm nay dày cộp một cách bất thường, và ca bệnh này khiến toàn bộ hội đồng y bác sĩ của kênh Vẽ Chuyện Hoang Dã phải ôm trán bất lực. Tên bệnh nhân: Koala.". Bố cục: ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ đứng BÊN TRÁI giơ tay ôm trán vẻ mặt bất lực, mồ hôi chảy ròng ròng; trên bàn là tập hồ sơ bệnh án dày cộp có dán tấm ảnh chụp chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái đang ôm cây ngủ gật.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nghề nghiệp: ôm cây ngủ gật toàn thời gian. Tình trạng bảo hiểm: không có!". Bố cục: chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái đang đu chặt trên một chạc cây khuynh diệp, hai mắt nhắm nghiền ngáy khò khò, bóng chữ 'Zzz' bay lên; một biển hiệu nhỏ cắm bên cạnh ghi hình vẽ chiếc đồng hồ 24/7.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Điều gì sẽ xảy ra nếu bạn hái một nắm lá khuynh diệp tươi ngon nhất, xếp ngay ngắn lên một chiếc đĩa sứ trắng tinh rồi đặt ngay trước mũi một chú Gấu Koala đang đói meo bụng sôi sùng sục?". Bố cục: Một bàn ăn sang trọng trải khăn trắng: BÊN PHẢI chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái ngồi thắt khăn ăn ở cổ, trước mặt là một chiếc đĩa sứ trắng tinh bày đầy những cành lá khuynh diệp xanh tươi bóng bẩy; bụng chú réo lên biểu tượng sóng âm đói bụng.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bất kỳ loài thú nào khác trên hành tinh này cũng sẽ đánh chén sạch sành sanh trong một nốt nhạc.". Bố cục: Chia đôi khung hình: BÊN TRÁI một chú thỏ và chú hươu hoạt hình đang há miệng ăn ngấu nghiến đĩa rau củ trong tích tắc; BÊN PHẢI chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái vẫn ngồi bất động nhìn chiếc đĩa lá, không hề nhúc nhích.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng Bệnh nhân ngơ ngác của chúng ta thì không! Nó sẽ ngồi nhìn chằm chằm vào chiếc đĩa với ánh mắt vô hồn, bất động như tượng đá, và...". Bố cục: Cận cảnh biểu cảm cực hài của chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái: ngồi nhìn chằm chằm vào chiếc đĩa sứ trắng trước mặt, ánh mắt vô hồn trống rỗng, trên đầu là một đám mây suy nghĩ rỗng tuếch có một chú ruồi bay qua và một dấu chấm hỏi to tướng.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thà chịu chết đói chứ nhất quyết không chịu thò mồm ăn một cọng lá!". Bố cục: chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái quay ngoắt mặt đi, hai tay khoanh trước ngực, môi bĩu ra kiên quyết từ chối chiếc đĩa lá; chiếc đĩa lá để trước mặt vẫn nguyên vẹn; bóng dáng bộ xương nhỏ hoạt hình mờ ảo phía sau trêu đùa sự nhịn đói.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ủa bác sĩ ơi, lá cây mà bứt rời để lên đĩa thì đâu phải là đồ ăn đâu ạ?". Bố cục: chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái nhướng mày, một tay chỉ vào chiếc đĩa sứ, miệng há to hỏi ngơ ngác; BÊN TRÁI ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ trố mắt kinh ngạc làm rơi chiếc bút chì xuống đất.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các đồng nghiệp nghe thấy câu trả lời ngây thơ của bệnh nhân chưa? Lý do ngớ ngẩn đến mức khó tin: chỉ vì lá cây đã bị bứt rời khỏi cành, bộ não của nó hoàn toàn không nhận diện được đó là thức ăn!". Bố cục: ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ quay người hướng ra phía người xem, hai tay giơ lên trời vẻ mặt cạn lời sâu sắc; trên bảng đen phía sau vẽ một cành cây có lá mọc dính và dấu tích xanh, bên cạnh là chiếc đĩa đựng lá rời có dấu gạch chéo đỏ.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đối với nó, đồ ăn bắt buộc phải mọc dính trên cành cây đung đưa trước gió, còn đặt trên đĩa thì... chắc chắn là đồ chơi hoặc rác rưởi!". Bố cục: Tâm trí của Koala: một cành cây khuynh diệp xanh tốt đung đưa trong gió có hào quang phát sáng lấp lánh (đồ ăn hợp lệ); bên cạnh chiếc đĩa sứ đựng lá rụng bị vẽ hình thùng rác đồ chơi bốc mùi.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa hết, bệnh nhân này còn thực hiện một cú lừa ngoạn mục đối với toàn nhân loại suốt hơn 200 năm qua ngay từ cái tên. Dù từ trẻ con đến người lớn ai cũng gọi là Gấu Koala, nhưng sinh vật này chẳng có lấy một giọt máu họ hàng nào với loài gấu cả!". Bố cục: chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái đang kéo khóa cởi bỏ bộ đồ hóa trang Gấu Nâu lông dày, lộ ra chiếc túi trước bụng có chú Koala con đang thò đầu ra; KHÔNG có chú Koala áo bệnh nhân trong cảnh này.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chúng là thú có túi chính hiệu của nước Úc, họ hàng ruột thịt gần nhất với loài Wombat mông bọc thép và Chuột túi Kangaroo nhảy lò cò.". Bố cục: chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái đứng giữa hai người họ hàng: BÊN TRÁI là chú Wombat béo tròn mông bọc thép, BÊN PHẢI là chú Kangaroo chuột túi đang đứng trên hai chân sau; cả ba đều có chiếc túi trước bụng.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hôm nay, phòng khám của chúng ta sẽ bật đèn công suất lớn để mổ xẻ 4 hạng mục kỳ dị nhất từ đầu đến chân của Bệnh nhân ngơ ngác này!". Bố cục: ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ bật công tắc đèn mổ sáng rực; trên tường chiếu 4 biểu tượng khám bệnh: một hộp sọ X-quang, một dạ dày cuốn ruột dài, bàn tay 2 ngón cái và cặp vân tay xoắn ốc; chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái nằm trên bàn khám ôm gối.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hạng mục khám đầu tiên: Chụp cắt lớp hộp sọ!". Bố cục: Phòng chụp X-quang: cô y tá trợ lý hoạt hình dễ thương đeo kính, mặc đồng phục y tế màu xanh pastel, kẹp bảng hồ sơ đang điều chỉnh chiếc máy chụp X-quang khổng lồ hướng vào đầu chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái; chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái ngồi ngay ngắn, hai tai rung rung, mắt tò mò nhìn ống kính máy chụp.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhìn từ bên ngoài, Bệnh nhân ngơ ngác sở hữu chiếc đầu to tròn, hai tai bông xù cực kỳ bệ vệ và đáng yêu như gấu bông bước ra từ tiệm đồ chơi.". Bố cục: Cận cảnh chiếc đầu to bự của chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái: đầu tròn xoe, hai tai xù lông to như hai chiếc quạt con, chiếc mũi đen bóng nổi bật; một chiếc thước kẹp đo vòng đầu to đùng đang đo quanh sọ.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng khi cắm tấm phim chụp X-quang lên bảng đèn soi, bác sĩ chúng tôi suýt nữa ngã ngửa khỏi ghế vì không tin vào mắt mình!". Bố cục: ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ cắm tấm phim chụp X-quang lên bảng đèn sáng: phim chụp cho thấy một hộp sọ to lớn nhưng bên trong chứa đầy chất lỏng màu xanh nước biển, ở giữa chỉ có một bộ não bé xíu như hạt nho đang nổi lơ lửng.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bộ não của Koala chỉ nặng vỏn vẹn khoảng 17g, chiếm đúng 0,2% trọng lượng cơ thể — tức là một trong những tỷ lệ não trên cơ thể nhỏ nhất trong toàn bộ thế giới động vật có vú!". Bố cục: BÊN TRÁI là một chiếc cân tiểu ly điện tử đặt bộ não Koala bé tí; BÊN PHẢI chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái ngồi nhìn chiếc cân ngạc nhiên.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tới 40% thể tích bên trong hộp sọ hoàn toàn không có mô não, mà chỉ ngập đầy chất dịch lỏng bồng bềnh chẳng khác nào một bể cá mini di động!". Bố cục: Mô hình cắt ngang hộp sọ Koala: chiếc hộp sọ được vẽ như một bể cá cảnh mini chứa đầy nước xanh lỏng, bên trong có bộ não nhỏ nổi bồng bềnh, vài chú cá nhỏ hoạt hình bơi lượn quanh não; KHÔNG có chú Koala áo bệnh nhân trong cảnh này.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bác sĩ ơi, em kiểm tra máy chụp X-quang 3 lần rồi, não bệnh nhân thực sự... nhẵn bóng không có nếp nhăn nào luôn ạ!". Bố cục: cô y tá trợ lý hoạt hình dễ thương đeo kính, mặc đồng phục y tế màu xanh pastel, kẹp bảng hồ sơ cầm tấm phim chụp X-quang soi lên trước mắt, vẻ mặt sửng sốt lắc đầu; bên cạnh chiếc máy chụp X-quang phát ra tia sáng quét.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đúng thế các đồng nghiệp ạ! Ở các loài thú thông minh như cá heo hay tinh tinh, bề mặt vỏ não chằng chịt hàng ngàn nếp nhăn gấp khúc để tăng diện tích xử lý thông tin phức tạp. Riêng bộ não của Koala thì... phẳng lì, trơn tuột chẳng khác nào hai miếng ức gà luộc bóc vỏ!". Bố cục: So sánh đối đầu giữa 2 bộ não: BÊN TRÁI là bộ não cá heo/con người chằng chịt nếp nhăn lấp lánh tia sét trí tuệ; BÊN PHẢI là bộ não Koala nhẵn bóng, phẳng lì như hai miếng ức gà luộc màu hồng phấn.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sự thiếu vắng nếp nhăn giải thích tại sao Bệnh nhân ngơ ngác mất hoàn toàn khả năng thích ứng: nếu trời đổ mưa bão sấm chớp, nó không biết tìm chỗ trú mà chỉ ngồi im trên cành cây chịu ướt sũng run cầm cập;". Bố cục: Cảnh trời mưa bão sấm chớp ầm ĩ: các loài thú khác chạy tìm hang trú ẩn, riêng chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái vẫn ngồi đơ trên chạc cây ướt sũng như chuột lột, mắt mở to nhìn trời mưa không hiểu chuyện gì xảy ra.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nếu lá cây rụng xuống đất, nó đứng nhìn đăm đăm như nhìn vật thể ngoài hành tinh!". Bố cục: Một chiếc lá khuynh diệp rụng từ cành cây xuống mặt đất ngay trước chân chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái; chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái cúi đầu nhìn chiếc lá với biểu cảm hoang mang như nhìn thấy đĩa bay của người ngoài hành tinh.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng chớ vội chê tạo hóa thiết kế lỗi! Việc thu nhỏ não bộ giúp nó tiết kiệm tới 20% năng lượng cơ thể quý giá.". Bố cục: Biểu đồ năng lượng cơ thể: trên đầu chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái là biểu tượng cục pin cạn đáy nhấp nháy màu đỏ 5%; bộ não thu nhỏ được khoanh vùng tiết kiệm năng lượng.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và đặc biệt nhất, lớp dịch lỏng 40% kia hoạt động như một chiếc mũ bảo hiểm đệm nước cực xịn!". Bố cục: Hộp sọ Koala được vẽ như một chiếc mũ bảo hiểm có túi khí đệm nước dày cộp bao quanh não; một chiếc búa đồ chơi gõ vào mũ bảo hiểm bị bật nảy ra ngoài êm ái.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vì tính tình ngơ ngác, Koala rất hay ngủ gật rồi ngã tự do từ ngọn cây cao chót vót xuống đất, và nhờ có bể nước giảm chấn trong đầu, não nó nảy tưng tưng như bóng cao su mà không hề bị chấn thương sọ não!". Bố cục: chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái đang ngủ gật ôm cành cây thì trượt tay ngã lộn cổ từ trên cao xuống đất; đầu chạm đất nảy tưng tưng như quả bóng cao su, chú đứng dậy chớp mắt tỉnh bơ không hề hấn gì.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chuyển sang hạng mục khám thứ hai: Nội soi hệ tiêu hóa! Các đồng nghiệp có từng thắc mắc tại sao Koala có thể sống ung dung tự tại cả đời trên ngọn cây mà không bao giờ bị bất kỳ loài thú ăn cỏ nào khác tranh giành thức ăn không?". Bố cục: Phòng nội soi tiêu hóa: ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ cầm ống nội soi mềm có camera gắn đèn soi vào bụng chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái; trên màn hình máy tính hiển thị hình ảnh đoạn ruột dài ngoằn ngoèo.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bởi vì thực đơn duy nhất của nó là lá cây khuynh diệp — một kho vũ khí hóa học chết người thực sự!". Bố cục: Cây khuynh diệp tỏa ra luồng khói xanh hình đầu lâu xương chéo độc hại; các loài thỏ rừng, chuột túi chạy dạt ra xa bịt mũi ho sặc sụa; chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái vắt vẻo trên cành nhai lá ngon lành.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thứ lá này cứng quai hàm như miếng da thuộc, nghèo calo đến mức tuyệt vọng, lại chứa đầy tinh dầu độc và hợp chất Xyanua đủ sức hạ gục hầu hết các loài động vật khác nếu dám ăn thử vài miếng!". Bố cục: BÊN TRÁI lá khuynh diệp được vẽ cứng như một tấm da thuộc đóng đinh gỉ sét, bên cạnh có lọ độc chất Xyanua; BÊN PHẢI chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái ngoạm chiếc lá nghe tiếng 'răng rắc' mà miệng vẫn cười.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để nhai thứ thuốc độc này trừ cơm ngày qua ngày, Koala trang bị một lá gan siêu cấp chuyên phân tách độc tố, kết hợp với chiếc manh tràng — tức phần ruột thừa — dài tới 2m, gấp 3 lần chiều dài toàn bộ cơ thể nó!". Bố cục: Sơ đồ giải phẫu dạ dày Koala: BÊN TRÁI lá gan đeo mặt nạ phòng độc lọc hóa chất; BÊN PHẢI đoạn manh tràng (ruột thừa) dài ngoằn ngoèo 2 mét uốn lượn như con trăn khổng lồ.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bên trong đoạn ruột thừa 2m khổng lồ đó, hàng tỷ vi khuẩn chuyên dụng phải làm việc cật lực suốt 4 ngày liền mới vắt kiệt được từng giọt năng lượng ít ỏi từ lá cây.". Bố cục: Bên trong lòng ruột Koala: hàng ngàn chú vi khuẩn tí hon đội mũ công nhân, cầm búa và kéo mini miệt mài cắt nhỏ và nghiền nát các phiến lá độc suốt 4 ngày đêm.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và xin đính chính ngay một lời đồn thất thiệt: Koala không hề ngủ nhiều vì bị say chất kích thích trong lá cây đâu nhé!". Bố cục: chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái nằm dài trên chạc cây ngáy khò khò, ôm chặt thân cây, cục pin trên đầu báo cạn 0%; không có chất kích thích nào, chỉ là cơ thể đang tắt nguồn để nạp lại calo.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngay cả cái tên Koala trong ngôn ngữ thổ dân Dharug cổ xưa cũng có nghĩa là không uống nước. Chúng hấp thụ 90% lượng nước trực tiếp từ lá cây,". Bố cục: Bản đồ sa mạc Úc dưới cái nắng chói chang: BÊN TRÁI một thổ dân Úc cổ xưa giơ tay vẽ biểu tượng 'không uống nước'; BÊN PHẢI chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái ngồi trên cây nhai lá tươi ngậm đầy giọt nước tinh khiết.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "và chỉ trong những đợt nắng nóng kỷ lục trên 40°C, người ta mới thấy cảnh những chú gấu ngơ ngác mò xuống đất xin nước từ bình cứu hỏa hoặc vòi nước rửa xe của người dân!". Bố cục: Ngày hè nắng gắt bốc hơi: chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái tụt xuống đất đứng cạnh chiếc xe đạp, hai tay ôm bình nước của một vận động viên đạp xe đang tươi cười dốc nước cho chú uống từng ngụm lớn.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng ly kỳ nhất là khi Koala non mới sinh ra, đường ruột hoàn toàn vô trùng, ăn phải lá độc là toi mạng ngay lập tức.". Bố cục: Một chú Koala sơ sinh bé xíu chỉ bằng hạt đậu đỏ nằm trong túi mẹ màu hồng nhạt, cơ thể trong suốt vô trùng; phía trên chiếc lá độc đe dọa.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mẹ ơi, con đói bụng rồi, cháo của con hôm nay có màu xanh lá đẹp quá!". Bố cục: Chú Koala con lông tơ thò đầu ra khỏi túi bụng của Koala mẹ, hai mắt to long lanh há mỏ chờ đợi; Koala mẹ cúi đầu âu yếm.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bác sĩ đề nghị các đồng nghiệp đang vừa xem video vừa ăn cơm hãy tạm dừng đũa vài giây!". Bố cục: ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ hốt hoảng giơ hai tay ra hiệu 'dừng đũa' về phía màn hình; trên bàn ăn bên cạnh là bát cơm và đôi đũa bị gác lại.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi con non được 6 tháng tuổi, Koala mẹ sẽ tiết ra từ hậu môn một loại phân nhão đặc biệt màu xanh lá gọi là cháo Pap. Chú con sẽ thò đầu ra khỏi túi bụng và ăn thứ cháo phân này liên tục suốt 1 tháng trời ròng rã!". Bố cục: Bữa ăn dặm kỳ lạ: Koala mẹ tiết ra chất sệt màu xanh lá cây từ phía sau; Koala con thò đầu ra ăn ngon lành, khuôn mặt rạng rỡ hạnh phúc.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nghe thì rùng mình rợn tóc gáy, nhưng đó lại là thần dược sinh tồn vĩ đại nhất: nhờ ăn cháo phân của mẹ, ruột con non mới được cấy đầy đủ đội quân vi sinh vật sống để giải độc, sẵn sàng cho cuộc đời nhai lá độc sau này! Đúng là tình mẫu tử thiêng liêng theo phong cách... không ai đỡ nổi!". Bố cục: Các chú vi khuẩn có lợi thân thiện màu xanh ngọc nhảy múa diễu hành từ bát cháo phân đi thẳng vào dạ dày của Koala con, tạo nên tấm khiên bảo vệ phát sáng chống lại độc tố lá cây.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hạng mục khám thứ ba: Tứ chi và cặp mông! Làm thế nào mà một kẻ ngủ gật tới 22 tiếng mỗi ngày trên ngọn cây cao chót vót đung đưa trong gió bão lại không bao giờ bị rơi cắm đầu xuống đất trong lúc ngáy khò khò?". Bố cục: Phòng khám kiểm tra chi: ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ cầm kính lúp to soi vào bàn tay trước của chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái; chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái giơ hai bàn tay xòe các ngón ra khoe móng vuốt sắc nhọn.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Câu trả lời nằm ở cấu tạo bàn tay quái đản bậc nhất tự nhiên: bàn tay trước của Koala không có một ngón cái như con người, mà tiến hóa thành 2 ngón cái nằm đối diện với 3 ngón còn lại!". Bố cục: Cận cảnh bàn tay trước của Koala như một bản vẽ kỹ thuật: bàn tay có 2 ngón cái đối diện với 3 ngón thường, tạo thành chiếc gọng kìm kẹp chặt lấy thân cành cây tròn.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cấu trúc 2 ngón cái này biến bàn tay nó thành một chiếc kìm bấm chết cơ khí tự động, khóa chặt vào thân cây ngay cả khi toàn bộ cơ bắp đã ngủ say như chết!". Bố cục: Hình minh họa chiếc kìm bấm chết cơ khí bằng thép kẹp cứng ngắc vào ống cành cây; bên cạnh bàn tay Koala bấm ngập móng vuốt vào vỏ cây, không thể lay chuyển.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thậm chí bàn chân sau của nó còn có hai ngón dính liền nhau thành một chiếc lược chải lông chuyên dụng để gãi ngứa và bắt bọ chét nữa cơ!". Bố cục: Cận cảnh bàn chân sau của Koala: ngón số 2 và ngón số 3 dính liền nhau có hai chiếc móng vuốt song song như răng lược, đang chải chuốt lớp lông tơ mượt mà gạt bọ chét rơi lả tả.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa dừng lại ở đó, hãy nhìn xuống phía dưới bàn tọa của Bệnh nhân ngơ ngác! Loài vật này hoàn toàn không có đuôi, nhưng thay vào đó, phần xương cụt của nó phát triển thành một tấm đệm sụn cực dày, bọc thêm lớp lông mông rậm rạp chẳng khác nào một chiếc ghế sô-pha cao cấp gắn liền vào cơ thể.". Bố cục: Mặt sau của chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái: chú không hề có đuôi, vùng mông tròn trĩnh có một lớp sụn cứng lót đệm dày như chiếc gối sofa êm ái.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ có chiếc đệm mông êm ái này, Koala có thể ngồi kẹp giữa hai chạc cây cứng ngắc suốt 22 tiếng mỗi ngày mà không hề biết cảm giác ê mông hay mỏi lưng là gì!". Bố cục: chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái ngồi lọt thỏm êm ru trên chạc cây chữ V cứng nhọn, mặt thư giãn nhắm nghiền mắt mỉm cười như đang ngồi ghế massage hạng thương gia.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bộ lông của nó còn có cấu tạo chống thấm nước như một chiếc áo mưa lông cừu, trời mưa xối xả thì nước trượt đi hết, bên trong da vẫn khô ráo ấm áp.". Bố cục: Cơn mưa rào trút nước xuống: những giọt nước mưa rơi vào lưng chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái lập tức trượt tròn lăn ra ngoài như nước đổ lá khoai; bên trong lớp lông vẫn khô ráo ấm cúng.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bác sĩ chúng tôi mà ngồi phòng khám liên tục vài tiếng là đã muốn gãy cả cột sống, thế mới thấy trang bị của Bệnh nhân ngơ ngác này quả thực là đỉnh cao của sự lười biếng hưởng thụ!". Bố cục: ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ ngồi còng lưng trên chiếc ghế xoay phòng khám, tay đấm lưng 'thùm thụp' vì đau cột sống; quay sang nhìn chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái ngồi ung dung trên cây với ánh mắt ghen tị.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bác sĩ ơi, đội cảnh sát hình sự vừa gửi sang một mẫu vân tay thu được tại hiện trường vụ trộm, nhìn qua kính hiển vi... giống vân tay con người y đúc luôn!". Bố cục: cô y tá trợ lý hoạt hình dễ thương đeo kính, mặc đồng phục y tế màu xanh pastel, kẹp bảng hồ sơ chạy vội vào phòng khám cầm theo một bìa hồ sơ cảnh sát có dấu mộc đỏ 'TỐI MẬT' và một tấm kính soi dấu vân tay màu đen.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo với các đồng nghiệp, đây là vụ bê bối pháp y chấn động và đau đầu nhất lịch sử nước Úc!". Bố cục: Bản tin pháp y chấn động: hai thám tử cảnh sát mặc áo măng-tô cầm kính lúp soi dấu vân tay xoắn ốc trên khung cửa sổ hiện trường vụ án trộm cắp.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dù cách xa loài người tới 70 triệu năm tiến hóa độc lập, nhưng đầu ngón tay của Koala lại sở hữu những đường vân xoắn ốc giống hệt dấu vân tay của con người!". Bố cục: So sánh vân tay dưới kính hiển vi điện tử: BÊN TRÁI dấu vân tay người xoắn ốc; BÊN PHẢI dấu vân tay đầu ngón tay Koala có các đường vân, vòng xoáy và móc giống hệt nhau đến từng chi tiết.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu có một vụ án bí ẩn xảy ra trong rừng khuynh diệp, chắc chắn nghi can số một bị triệu tập lấy lời khai sẽ là một chú Koala đang ngáp ngủ trên cây!". Bố cục: Phòng thẩm vấn cảnh sát: một thám tử cảnh sát ngồi đối diện chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái dưới ánh đèn bàn thẩm vấn; chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái ngồi trên ghế bị cáo hai tai xù ngáp ngủ dài ngoẵng.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Con đực trưởng thành còn có một tuyến mùi màu nâu nhớp nháp ngay giữa ngực, tỏa ra mùi dầu gió khuynh diệp nồng nặc để cọ vào thân cây đánh dấu lãnh thổ.". Bố cục: Một chú Koala đực lực lưỡng đứng cọ ngực vào thân cây khuynh diệp: giữa ngực có một vệt màu nâu sẫm tiết ra tinh dầu thơm ngát mùi kẹo ngậm bạc hà lan tỏa khắp không gian.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng nếu bạn nghĩ một sinh vật mũm mĩm như thú nhồi bông sẽ kêu những tiếng chít chít đáng yêu, thì bạn sắp bị sốc toàn tập rồi đấy!". Bố cục: BÊN TRÁI hình ảnh chú Koala thú nhồi bông kêu 'chít chít' dễ thương bị gạch chéo đỏ; BÊN PHẢI chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái đang hít một hơi thật sâu phồng to lồng ngực chuẩn bị gầm.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vào mùa giao phối, những chú Koala đực phát ra những tiếng rống trầm đục, khàn đặc như tiếng gầm của quái vật thời tiền sử, vang vọng hàng cây số xuyên qua rừng đêm tĩnh mịch!". Bố cục: chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái mở toang mồm phát ra luồng sóng âm khổng lồ hình đầu quái vật bạo chúa gầm rú; một du khách cắm trại trong lều phía dưới giật nảy mình dựng đứng tóc gáy, rơi cốc trà.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà giải phẫu phát hiện ngoài thanh quản bình thường, Koala sở hữu thêm một cặp dây thanh âm khổng lồ nằm ở vòm họng mềm, phát ra âm thanh tần số thấp tới 27 Hz — trầm thấp gấp 20 lần kích thước cơ thể nhỏ bé của nó!". Bố cục: Sơ đồ cấu tạo họng Koala: ngoài thanh quản thông thường, phía trên vòm họng mềm có một cặp dây thanh âm phụ khổng lồ màu đỏ phát ra các vòng sóng âm thanh tần số siêu trầm 27 Hz.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kết thúc bản bệnh án hôm nay, bác sĩ chúng tôi phải đưa ra một chẩn đoán đầy xót xa: chính sự thích nghi cực đoan vào cây khuynh diệp đã đẩy Bệnh nhân ngơ ngác vào hai tử huyệt sinh tồn nghiệt ngã của tạo hóa.". Bố cục: ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ đứng bên bảng chẩn đoán y khoa, vẻ mặt trầm ngâm thương cảm; chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái ngồi cạnh bàn ôm một cành lá khuynh diệp.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thứ nhất, vì lá khuynh diệp chứa nhiều tinh thể cát mịn, sau khoảng 15 năm nhai liên tục không ngừng nghỉ, toàn bộ hàm răng của Koala sẽ bị mài mòn phẳng lì tới tận chân nướu.". Bố cục: Cận cảnh hàm răng Koala già: những chiếc răng hàm bị mài phẳng lì trơ trụi như đá mài mòn, không còn gờ nhọn để nghiền nát phiến lá cứng; xung quanh là các hạt cát silicat nhỏ li ti.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và vì không có khả năng thay răng mới như loài chuột, những cá thể già yếu sẽ chết vì đói ngay giữa một rừng cây đầy ắp lá xanh non mơn mởn!". Bố cục: Cảnh thương cảm: một chú Koala già ngồi ôm cành cây giữa rừng lá xanh bạt ngàn nhưng không thể nhai được, chiếc bụng đói xẹp xuống; bóng hoàng hôn buông dịu dàng.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thứ hai, bản năng triệu năm dạy chúng rằng mọi kẻ thù nguy hiểm đều bò dưới mặt đất, nên khi xảy ra cháy rừng thảm khốc, phản xạ duy nhất của Koala là... trèo tọt lên ngọn cây cao nhất rồi ngồi cuộn tròn nhắm mắt chờ đợi,". Bố cục: Cảnh báo cháy rừng: phía dưới chân cây là ngọn lửa đỏ rực bốc khói; thay vì chạy xuống đất, chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái lại leo tót lên ngọn cây cao nhất rồi cuộn tròn nhắm tịt mắt chờ đợi trong sợ hãi.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "biến chúng thành nạn nhân vô cùng dễ bị tổn thương nếu không có bàn tay giải cứu kịp thời của các tình nguyện viên và lính cứu hỏa.". Bố cục: Người lính cứu hỏa Úc tốt bụng mặc áo bảo hộ vàng quỳ xuống cạnh gốc cây, ân cần đưa chai nước mát cho chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái vừa được cứu thoát; ánh mắt biết ơn ấm áp.
```
</details>

<details><summary>L62</summary>

```text
HÌNH L62 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tập sau, phòng khám của chúng ta sẽ đón một bệnh nhân ăn chay khổng lồ nhưng lại sở hữu bộ ruột của thú ăn thịt hung dữ: Gấu Trúc Lớn!". Bố cục: Phòng khám hé mở cánh cửa tiếp theo: một chú Gấu Trúc Lớn mập mạp đen trắng đang ngồi bệt dưới đất nhai cây tre rôm rốp, mắt đeo kính cận, vẻ mặt hề hước.
```
</details>

<details><summary>L63</summary>

```text
HÌNH L63 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhai tre 14 tiếng mỗi ngày, đi vệ sinh 40 lần một ngày, và leo cây ngã lộn cổ như nghệ sĩ xiếc nghiệp dư!". Bố cục: Chia 2 nửa: BÊN TRÁI Gấu Trúc nhai tre đống tre cao ngất; BÊN PHẢI chú trèo cây bị gãy cành ngã lộn nhào chổng vó lên trời như diễn viên xiếc.
```
</details>

<details><summary>L64</summary>

```text
HÌNH L64 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hẹn gặp lại các đồng nghiệp trong hồ sơ bệnh án tiếp theo!". Bố cục: ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ đứng vẫy tay chào tạm biệt cùng chú Gấu Trúc đang ngậm cành tre; tấm biển 'HẸN GẶP LẠI TẬP 11' treo phía trên.
```
</details>

<details><summary>L65</summary>

```text
HÌNH L65 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bác sĩ ơi, vậy cuối cùng đơn thuốc của Bệnh nhân ngơ ngác này là gì ạ?". Bố cục: cô y tá trợ lý hoạt hình dễ thương đeo kính, mặc đồng phục y tế màu xanh pastel, kẹp bảng hồ sơ cầm cây bút bi và cuốn sổ đơn thuốc đưa cho ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ, nghiêng đầu mỉm cười hỏi ý kiến.
```
</details>

<details><summary>L66</summary>

```text
HÌNH L66 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kê đơn: Cho bệnh nhân ôm cây ngủ tiếp 22 tiếng mỗi ngày, tuyệt đối đừng ai hái lá bỏ vào đĩa sứ nữa nhé!". Bố cục: ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ ký ngoáy lên tờ đơn thuốc có ghi dòng chữ hài hước; bên cạnh chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái đã ôm cành cây ngủ tít mít tự bao giờ, chiếc đĩa sứ để xa tít tắp.
```
</details>

<details><summary>L67</summary>

```text
HÌNH L67 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ký tên: bác sĩ đã hoàn toàn bất lực!". Bố cục: ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ giơ hai tay ra hiệu chào thua; chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái hé một bên mắt ngơ ngác nhìn khán giả, hai tai vẫy vẫy dễ thương.
```
</details>

<details><summary>L68</summary>

```text
HÌNH L68 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn bạn, bạn ấn tượng nhất với nét ngớ ngẩn nào của Bệnh nhân ngơ ngác này? Hãy để lại phán quyết của bạn ở phần bình luận bên dưới nhé!". Bố cục: Hàng ghế khán giả các bạn nhỏ và gia đình đang giơ các biểu tượng mặt cười, trái tim và bóng bình luận sáng rực; chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái ngồi ở giữa mỉm cười thân thiện.
```
</details>

<details><summary>L69</summary>

```text
HÌNH L69 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chúng bắt buộc phải ngủ li bì tới 22 tiếng mỗi ngày đơn giản vì cơ thể quá kiệt quệ calo, nếu thức thêm vài tiếng nữa để đi dạo là chúng sẽ... kiệt sức lăn đùng ra vì hết pin!". Bố cục: Koala ngủ li bì 22 tiếng mỗi ngày trên cây vì cơ thể kiệt quệ calo; chiếc đồng hồ chỉ 22 giờ ngủ.
```
</details>

<details><summary>L70</summary>

```text
HÌNH L70 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giống đến mức ngay cả khi đưa vào máy quét kính hiển vi điện tử độ phân giải cao nhất, các chuyên gia giám định hình sự cũng không tài nào phân biệt nổi đâu là dấu vân tay của tên trộm đột nhập và đâu là dấu tay của Bệnh nhân ngơ ngác vừa trèo qua cửa sổ hái trộm lá cây!". Bố cục: Các chuyên gia giám định hình sự cảnh sát Úc cầm kính hiển vi và máy tính quét vân tay hiện trường bối rối không phân biệt nổi vân tay người hay Koala.
```
</details>

<details><summary>L71</summary>

```text
HÌNH L71 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngoại hình gấu bông ngây thơ, nhưng khi cất giọng thì rung chuyển cả rừng già khiến du khách cắm trại phải lạnh sống lưng!". Bố cục: Ngoại hình gấu bông ngây thơ nhưng phát ra tiếng gầm rung chuyển cả khu rừng rậm đêm khiến du khách cắm trại bên dưới rùng mình hoảng hốt.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bày sẵn một đĩa lá tươi ngon ngay trước mặt, nhưng chú Gấu Koala này thà chịu chết đói chứ nhất quyết không ăn!". Bố cục: Phòng khám dọc 9:16: chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái ngồi trên bàn ăn trước một chiếc đĩa sứ trắng đựng lá khuynh diệp tươi ngon nhưng mặt đờ đẫn quay đi thà chết đói; ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ đứng bên cạnh ôm trán.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Lý do là vì lá cây đã bị bứt rời khỏi cành, bộ não của nó hoàn toàn không nhận diện được đó là thức ăn!". Bố cục: Cận cảnh đầu chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái: trên đầu là đám mây suy nghĩ rỗng tuếch có hình một cành cây (thức ăn ✓) và một chiếc đĩa sứ (rác rưởi ✗), vẻ mặt ngơ ngác không nhận diện được.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Khi chụp X-quang hộp sọ của Bệnh nhân ngơ ngác này, các bác sĩ đã ngã ngửa:". Bố cục: Phòng chụp X-quang dọc: ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ và cô y tá trợ lý hoạt hình dễ thương đeo kính, mặc đồng phục y tế màu xanh pastel, kẹp bảng hồ sơ trố mắt ngã ngửa khi nhìn vào máy quét X-quang đầu Koala phát sáng xanh.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "tới 40% hộp sọ chỉ chứa toàn nước lỏng,". Bố cục: Tấm phim X-quang đầu Koala dọc khung hình: chiếc sọ to đùng chứa 40% nước xanh, bên trong bộ não nhỏ xíu bồng bềnh như bể cá.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "còn bộ não bên trong thì phẳng lì như hai miếng ức gà luộc, không có lấy một nếp nhăn!". Bố cục: So sánh bộ não phẳng lì như hai miếng ức gà luộc bóc vỏ, trơn nhẵn không có lấy một nếp nhăn; dấu hỏi chấm to tướng.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Nó ăn thứ lá khuynh diệp chứa đầy độc tố Xyanua,". Bố cục: Cây khuynh diệp bốc khói độc Xyanua màu xanh lá hình đầu lâu; chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái ngồi vắt vẻo trên ngọn cây nhai lá ngon lành.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "sở hữu đoạn ruột thừa dài tới 2m,". Bố cục: Sơ đồ cơ thể Koala dọc màn hình: đoạn ruột thừa dài ngoằn ngoèo 2 mét uốn lượn như con trăn, các công nhân vi khuẩn tí hon đang làm việc.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "và phải ngủ li bì tới 22 tiếng mỗi ngày để tiết kiệm pin!". Bố cục: chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái nằm ôm cành cây ngủ say sưa, cục pin trên đầu báo cạn đáy 0% nhấp nháy, tiếng ngáy khò khò.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Chưa hết, đầu ngón tay của nó còn có dấu vân tay giống hệt con người khiến cảnh sát hình sự cũng phải bó tay!". Bố cục: So sánh dấu vân tay dọc: phía trên là dấu vân tay người, phía dưới là bàn tay chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái có các đường vân xoắn ốc giống hệt 100%, kính lúp phóng đại soi chi tiết.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bạn có tin một loài vật não phẳng như thế này lại sống sót được hàng triệu năm không?". Bố cục: chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái ngồi ôm cành cây giữa rừng khuynh diệp bạt ngàn nước Úc, ánh nắng xuyên qua kẽ lá lấp lánh; chú chớp mắt ngơ ngác đáng yêu như muốn hỏi 'sao mọi người nhìn tớ thế?'.
```
</details>

<details><summary>S11</summary>

```text
HÌNH S11 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Koala mập lông xám, tai tròn xù, mũi đen to ngơ ngác, áo bệnh nhân trắng chữ thập đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Xem trọn bộ hồ sơ bệnh án trong video dài bên dưới nhé, vì bệnh nhân này...". Bố cục: ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ đứng cạnh chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái đang giơ ngón tay cái chỉ xuống phía dưới màn hình; mũi tên vàng nhấp nháy chỉ link video dài phía dưới; phong cách vui nhộn mời gọi.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/69 của video YouTube về Gấu Koala). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái. Nhân vật phụ cố định: ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ; cô y tá trợ lý hoạt hình dễ thương đeo kính, mặc đồng phục y tế màu xanh pastel, kẹp bảng hồ sơ. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/11 của video YouTube Shorts về Gấu Koala). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú gấu Koala hoạt hình mập mạp tròn xoe: bộ lông màu xám ấm áp, hai tai tròn to xù lông màu trắng ở mép tai, chiếc mũi to hình quả lê màu đen bóng ngộ nghĩnh, mắt to tròn đen láy luôn mở ngơ ngác, mặc chiếc áo choàng bệnh nhân màu trắng có in hình chữ thập đỏ nhỏ xíu ở ngực trái. Nhân vật phụ: ông bác sĩ thú y hoạt hình đeo kính tròn gọng đen, mặc áo blouse trắng, đeo ống nghe y tế quanh cổ. 
```
</details>

## 7. SEO

- **title:** Bày Đồ Ăn Ra Đĩa Nhưng Thà Nhịn Đói?! | Gấu Koala | Tập 10
- **hook_paragraph:** Gấu Koala sở hữu bộ não phẳng lì không một nếp nhăn, 40% hộp sọ chứa đầy dịch lỏng, ruột thừa dài 2m để tiêu hóa lá độc Xyanua và dấu vân tay giống hệt con người 100%! Khám phá hồ sơ bệnh án tiến hóa bi hài của loài thú có túi lười biếng nhất nước Úc.
- **question:** Nếu được chọn một siêu năng lực của Gấu Koala: ngủ 22 tiếng hay mông đệm sụn ngồi không biết ê, bạn chọn cái nào? Bình luận bên dưới nhé!
- **next_teaser:** Gấu Trúc Lớn — mang bộ ruột của thú ăn thịt nhưng ngày nào cũng ngồi nhai tre 14 tiếng
- **shorts_title:** Bày Đồ Ăn Ra Đĩa Nhưng Thà Nhịn Đói?! 🐨 #shorts #koala
- **shorts_desc:** Gấu Koala thà nhịn đói chết trước đĩa lá tươi chỉ vì lá bị bứt khỏi cành! Bộ não 40% là nước và phẳng lì không nếp nhăn! 🐨🌿
👉 Xem trọn bộ hồ sơ bệnh án tiến hóa — video Tập 10 trên kênh Vẽ Chuyện Hoang Dã.
- **bullets:** Hạng mục 1: 40% hộp sọ là nước lỏng, não trơn nhẵn như ức gà luộc · Hạng mục 2: Ăn lá độc Xyanua, ruột thừa dài 2m và ngủ 22 tiếng/ngày · Hạng mục 3: Bàn tay kìm sắt 2 ngón cái và mông bọc đệm sụn chống ê · Hạng mục 4: Dấu vân tay giống hệt người và tiếng gầm quái vật 27 Hz
- **tags:** gấu koala, gau koala, koala, koala úc, não phẳng, tiến hóa lỗi, lá khuynh diệp, thú có túi, vân tay koala, thế giới động vật, động vật hài hước, vẽ chuyện hoang dã, whiteboard animation, khoa học thú vị, bệnh án tiến hóa
- **hashtags:** #GauKoala #Koala #TheGioiDongVat #VeChuyenHoangDa #KhoaHoc

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-10-gau-koala
python src/episode/pipeline.py tts    projects/tap-10-gau-koala     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-10-gau-koala     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-10-gau-koala     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-10-gau-koala              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-10-gau-koala --force
python scripts/beat_sheet.py projects/tap-10-gau-koala               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-10-gau-koala/audio/shorts.wav projects/tap-10-gau-koala/renders/tap-10-gau-koala_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-10-gau-koala
python src/episode/pipeline.py seo    projects/tap-10-gau-koala
python src/episode/episode_doc.py     projects/tap-10-gau-koala
```

# TẬP 15 — CHUỘT LANG NƯỚC (CAPYBARA) · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-15-capybara`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-15-capybara`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F6` · **Persona giọng:** `ong_trum` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Chuột Lang Nước (Capybara) |
| Tiêu đề YouTube | Bố Già 65kg Khiến Cá Sấu Phải Nể & Bữa Sáng Ăn Lại... Phân?! \| Capybara \| Tập 15 |
| Video dài | `renders/tap-15-capybara_long.mp4` — 8:52.1 (532.1s) |
| Shorts | `renders/tap-15-capybara_shorts.mp4` — 0:51.8 (51.8s) |
| Thumbnail | `renders/tap-15-capybara_thumbnail.jpg` |
| Số hình | dài 80 beat / 80 ảnh riêng; Shorts 11 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/80 của video YouTube về Chuột Lang Nước (Capybara)). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi. Nhân vật phụ cố định: chú cá sấu Caiman hoạt hình màu xanh rêu, hàm răng nhọn hoắt lởm chởm, mắt to tròn ngơ ngác; chú khỉ sóc nhỏ xíu hoạt hình lông vàng, đuôi dài, tinh nghịch; chú chim bồ nông hoạt hình mỏ vàng khổng lồ, túi da dưới mỏ xệ xuống; chú báo đốm Jaguar dũng mãnh lông vàng đốm hoa mai đen, nanh vuốt nhọn. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — GÃ BÉO 65KG GIA TỘC GẶM NHẤM LÀM CÁ SẤU PHẢI NỂ
*Thẻ chương:* GÃ BÉO NẶNG 65KG ĐƯỢC MỌI SÁT THỦ NỂ SỢ

*Badge:* `HỒ SƠ BỐ GIÀ` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene01_p0.wav` (345 ký tự) · mood `tram_bi_an`

```text
Trong thế giới ngầm đầm lầy Pantanal Nam Mỹ, nơi cá sấu Caiman rình rập dưới dòng nước đục, trăn khổng lồ Anaconda siết nghẹt bùn lầy, và báo đốm Jaguar rình rập trên cành cây... [surprise-oh] bạn nghĩ ai mới là kẻ nắm giữ quyền lực tối thượng? Quên hết những bộ nanh vuốt đẫm máu đi! Hãy mở tập hồ sơ mật mang mã số mười lăm của Bố Già Đầm Lầy.
```
**Part 1** → `audio/vs/scene01_p1.wav` (312 ký tự) · mood `hao_hung`

```text
Nhân vật đứng đầu danh sách theo dõi của chúng ta hôm nay không phải sát thủ săn mồi nào cả, mà là một gã béo ục ịch nặng tới sáu mươi lăm cân, mang họ nhà chuột, suốt ngày ngâm mình trong nước với vẻ mặt đơ toàn tập không hề biến sắc: Chuột Lang Nước, hay còn gọi bằng danh xưng giang hồ quốc tế là Ca-py-ba-ra!
```
**Part 2** → `audio/vs/scene01_p2.wav` (439 ký tự) · mood `hao_hung`

```text
Gia tộc gặm nhấm trên khắp Trái Đất thường bị gắn mác là những kẻ lấm lét trốn chui trốn lủi trong góc bếp. [laughter] Nhưng Bố Già Đầm Lầy của chúng ta thì ở một đẳng cấp hoàn toàn khác! Với chiều dài cơ thể lên tới một mét ba và chiều cao vai sáu mươi xăng-ti-mét, gã chính là loài gặm nhấm lớn nhất thế giới còn tồn tại. Cá thể lập kỷ lục từng được ghi nhận tại Brazil nặng tới chín mươi mốt cân, to ngang một con lợn rừng trưởng thành!
```
**Part 3** → `audio/vs/scene01_p3.wav` (419 ký tự) · mood `nghiem_trang_gia`

```text
Quy tắc thép đầu tiên của gia tộc này khiến mọi nhà sinh vật học phải ngả mũ kinh ngạc: [surprise-wa] Tuyệt đối không bao giờ hoảng loạn! Cho dù trời long đất lở, cho dù lũ quét dâng cao hay một con cá sấu khổng lồ đang bò sát sạt bên hông, gương mặt của Ca-py-ba-ra vẫn giữ nguyên một nụ cười mỉm thiền định như thể vừa đắc đạo. Đây không phải là sự dũng cảm bộc phát, mà là đỉnh cao của nghệ thuật ngoại giao đầm lầy!
```

### scene02 — TẠI SAO CÁ SẤU CAIMAN KHÔNG DÁM ĂN THỊT BỐ GIÀ?
*Thẻ chương:* CÁ SẤU CAIMAN NẰM PHƠI NẮNG KẾ BÊN

*Badge:* `TRẠM DỊCH VỤ` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene02_p0.wav` (323 ký tự) · mood `hao_hung`

```text
Nếu bạn gõ từ khóa Ca-py-ba-ra trên mạng, bức ảnh kinh điển nhất đập vào mắt chắc chắn là cảnh gã béo này nằm phơi bụng ngủ say sưa, trong khi ngay bên cạnh là ba đến bốn con cá sấu Caiman răng nhọn hoắt đang nằm phơi nắng. [surprise-oh] Cảnh tượng phi lý đến mức người ta tưởng đây là sản phẩm của công nghệ chỉnh sửa ảnh!
```
**Part 1** → `audio/vs/scene02_p1.wav` (198 ký tự) · mood `tram_bi_an`

```text
Tại sao một kẻ săn mồi khét tiếng vùng đầm lầy lại bỏ qua một khối thịt sáu mươi lăm cân béo múp míp đang nằm ngay trước mũi? Hãy nghe chính đại diện giới săn mồi lên tiếng giải thích lý do thực tế.
```
**Part 2** → `audio/vs/scene02_p2.wav` (157 ký tự) · 🎭 cameo `ga_khong_lo`

```text
Tôi mà đụng vào gã béo này là gãy cả hàm đấy! Vừa to vừa nặng, da thì dai nhách, mà còn là trạm cảnh báo động đất của cả khu vực, dại gì nuốt cho nghẹn họng!
```
**Part 3** → `audio/vs/scene02_p3.wav` (380 ký tự) · mood `nghiem_trang_gia`

```text
[laughter] Đúng như lời gã cá sấu thú nhận! Cá sấu Caiman ở vùng Pantanal thường chỉ dài một mét rưỡi đến hai mét, chuyên săn cá và chim nhỏ. Nuốt một con Bố Già Đầm Lầy trưởng thành là canh bạc nguy hiểm có thể làm chúng rách họng chết ngạt. Chưa kể, gã béo này sở hữu cặp răng cửa sắc như xẻng sắt, nếu bị dồn vào đường cùng thì một cú cắn tự vệ cũng đủ bẻ gãy xương mõm cá sấu!
```
**Part 4** → `audio/vs/scene02_p4.wav` (381 ký tự) · mood `hao_hung`

```text
Chưa dừng lại ở đó, gã chuột lang nước này còn kiêm luôn chức vụ Giám đốc trạm dịch vụ giao thông công cộng lớn nhất rừng nhiệt đới. Lưng của Ca-py-ba-ra phẳng lì và rộng thênh thang như chiếc ghế sô-pha di động. Chim chóc đầm lầy đậu lên lưng để rỉa bọ ve ký sinh, đàn rùa nước năm đến sáu con trèo lên mai nằm sưởi ấm, và bầy khỉ sóc thì biến gã thành chiếc phà an toàn qua sông!
```
**Part 5** → `audio/vs/scene02_p5.wav` (82 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Bác bồ nông ơi, mông tôi là thịt chứ không phải con cá đâu, kẹp hoài không chán à?
```
**Part 6** → `audio/vs/scene02_p6.wav` (305 ký tự) · mood `bi_hai`

```text
[laughter] Thậm chí cả loài chim bồ nông tham ăn nổi tiếng cũng từng há mỏ kẹp thử vào mông Ca-py-ba-ra trong vô vọng, còn gã chuột lang thì chỉ ngoái đầu lại nhìn với vẻ mặt thương hại rồi... ngủ tiếp! Một mối quan hệ cộng sinh đôi bên cùng có lợi mà giới khoa học gọi là tuyệt tác hòa bình của tự nhiên.
```

### scene03 — TUYẾN MÙI MORILLO TRÊN MŨI VÀ TIẾNG SỦA BÁO ĐỘNG
*Thẻ chương:* BÍ MẬT KHỐI U MORILLO TRÊN ĐỈNH MŨI

*Badge:* `VŨ KHÍ MÙI HƯƠNG` · *mood mặc định:* `nghiem_trang_gia`

**Part 0** → `audio/vs/scene03_p0.wav` (363 ký tự) · mood `tram_bi_an`

```text
Bất kỳ đế chế nào muốn tồn tại lâu dài cũng phải xây dựng một mạng lưới liên lạc bí mật hoàn hảo. Và vũ khí ngoại giao lợi hại nhất của Bố Già Đầm Lầy nằm ngay trên chóp mũi! [surprise-oh] Nếu quan sát kỹ một con đực đầu đàn, bạn sẽ thấy một khối u màu đen sẫm, trơn bóng nổi rõ trên sống mũi. Trong giới sinh học, khối u quyền lực này được gọi là tuyến Mo-ri-lô.
```
**Part 1** → `audio/vs/scene03_p1.wav` (375 ký tự) · mood `hao_hung`

```text
Tuyến Mo-ri-lô liên tục tiết ra một chất dịch sáp màu trắng chứa hỗn hợp xạ hương cực mạnh. Mỗi khi đi tuần tra qua các gốc sậy hay thân cây gãy, Bố Già chỉ cần quẹt nhẹ chiếc mũi quyền lực của mình lên vỏ cây để ký tên đóng dấu lãnh thổ. [laughter] Kết hợp với hai túi tuyến mùi hương ở hai bên hậu môn, mỗi cá thể Ca-py-ba-ra sở hữu một bản mã hóa sinh học độc nhất vô nhị!
```
**Part 2** → `audio/vs/scene03_p2.wav` (262 ký tự) · mood `hao_hung`

```text
Nhờ hệ thống chữ ký mùi hương này, các thành viên trong gia tộc chỉ cần hít nhẹ một cái là biết ngay đối phương thuộc phe nào, địa vị xã hội cao hay thấp, thậm chí cả tình trạng sức khỏe hôm nay ra sao mà không cần phí một giọt máu để đấm đá tranh giành thứ bậc!
```
**Part 3** → `audio/vs/scene03_p3.wav` (100 ký tự) · 🎭 cameo `ong_gia_ke`

```text
Lão sống ở Pantanal tám mươi năm rồi, chưa thấy chiếc xe buýt nào êm ái và đúng giờ như lưng gã này!
```
**Part 4** → `audio/vs/scene03_p4.wav` (375 ký tự) · mood `hao_hung`

```text
[surprise-wa] Nhưng đỉnh cao nhất trong kho vũ khí của gia tộc này chính là hệ thống điện đàm âm thanh! Đôi tai hình bán nguyệt của Ca-py-ba-ra có thể xoay một trăm tám mươi độ độc lập, bắt trọn tiếng chân rón rén của kẻ thù từ khoảng cách hơn một trăm mét. Khi vui vẻ thư giãn, chúng phát ra tiếng rên hừ hừ như mèo. Khi gọi đàn con, chúng huýt sáo lảnh lót như chim sơn ca.
```
**Part 5** → `audio/vs/scene03_p5.wav` (298 ký tự) · mood `don_dap`

```text
Nhưng một khi phát hiện bóng dáng sát thủ báo đốm, con đầu đàn sẽ tung ra một cú sủa đanh thép như chó săn chuyên nghiệp! Cú sủa báo động này có tần số đặc biệt làm chấn động cả đầm lầy, khiến từ bầy khỉ trên ngọn cây đến lũ hươu bờ sông đều lập tức nhảy dựng lên bỏ chạy thoát thân trong gang tấc!
```

### scene04 — TẬP TÍNH ĂN LẠI PHÂN SÁNG SỚM ĐỂ HẤP THỤ PROTEIN
*Thẻ chương:* GÓC KHUẤT BỮA SÁNG KHOẢNG 06:00 ĐẾN 08:00

*Badge:* `BỮA SÁNG KỲ DỊ` · *mood mặc định:* `bi_hai`

**Part 0** → `audio/vs/scene04_p0.wav` (353 ký tự) · mood `bi_hai`

```text
[sigh] Nào, bây giờ là lúc chúng ta phải lật mở trang hồ sơ đen tối và nhạy cảm nhất của Bố Già Đầm Lầy. Nếu bạn đang ăn sáng hay vừa nhâm nhi cốc trà sữa, tôi chân thành khuyên bạn hãy tạm đặt cốc xuống trong hai phút tới! Bởi vì món ăn khoái khẩu giúp gã béo này duy trì thân hình hộ pháp sáu mươi lăm cân... chính là sản phẩm do chính gã vừa thải ra!
```
**Part 1** → `audio/vs/scene04_p1.wav` (385 ký tự) · mood `nghiem_trang_gia`

```text
Khoan vội bịt mũi phán xét! Dưới góc nhìn của khoa học dinh dưỡng, đây là một tuyệt tác tiến hóa sinh tồn bậc thầy mang tên Xê-cô-tơ-rô-phi, hay tập tính ăn phân có chọn lọc! Khẩu phần ăn của Ca-py-ba-ra chiếm tới bảy mươi lăm phần trăm là cỏ đầm lầy và thực vật thủy sinh thô ráp. Cỏ nghèo dinh dưỡng đến mức chất xơ xen-lu-lô-zơ gần như không thể bị phân hủy bởi dạ dày thông thường.
```
**Part 2** → `audio/vs/scene04_p2.wav` (422 ký tự) · mood `hao_hung`

```text
Để giải quyết bài toán hóc búa này, tạo hóa trang bị cho Ca-py-ba-ra một chiếc ruột tịt khổng lồ chứa hàng tỷ vi khuẩn lên men đặc chủng. [surprise-oh] Cứ vào khoảng từ sáu giờ sáng đến tám giờ sáng mỗi ngày, sau một đêm dài vi khuẩn cật lực làm việc, cơ thể gã sẽ thải ra một loại phân mềm đặc biệt màu xanh lục gọi là phân manh tràng. Loại phân này chứa hàm lượng protein gấp đôi phân thường và ngập tràn vitamin nhóm B!
```
**Part 3** → `audio/vs/scene04_p3.wav` (320 ký tự) · mood `hao_hung`

```text
Thay vì lãng phí nguồn tài nguyên quý giá trôi theo dòng nước, Bố Già lập tức cúi xuống ăn lại toàn bộ chỗ phân mềm này để hệ tiêu hóa hấp thụ dưỡng chất lần thứ hai! Ngay từ khi mới được hai tuần tuổi, những chú chuột lang nước con đã bắt đầu học tập thói quen này từ mẹ để cấy hệ vi sinh đường ruột quý giá vào cơ thể.
```
**Part 4** → `audio/vs/scene04_p4.wav` (287 ký tự) · mood `hao_hung`

```text
[laughter] Phải đến buổi chiều, sau khi đã bòn rút sạch sẽ đến phân tử protein cuối cùng, gã mới thải ra những viên phân khô cứng hình bầu dục không còn giá trị dinh dưỡng. Kỳ dị, khó ngửi, nhưng chính món súp vi khuẩn tái chế này đã nuôi sống cả đế chế gặm nhấm suốt hàng triệu năm qua!
```

### scene05 — TÀU NGẦM NÍN THỞ 5 PHÚT VÀ CÚ BỨT TỐC 35 KM/H
*Thẻ chương:* BỐ TRÍ MẮT MŨI TAI THẲNG HÀNG TRÊN ĐỈNH ĐẦU

*Badge:* `TÀU NGẦM 5 PHÚT` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene05_p0.wav` (330 ký tự) · mood `don_dap`

```text
Đừng bao giờ để dáng vẻ chậm chạp ung dung của Bố Già đánh lừa thị giác! Trong thế giới giang hồ, kẻ sống sót lâu nhất không phải kẻ to mồm nhất, mà là kẻ sở hữu lối thoát hiểm tinh quái nhất. Một khi sát thủ đỉnh chóp Báo Đốm Giác-goa xuất hiện với cặp móng vuốt chết chóc, Ca-py-ba-ra lập tức kích hoạt chế độ đào tẩu cấp độ đỏ!
```
**Part 1** → `audio/vs/scene05_p1.wav` (75 ký tự) · 🎭 cameo `ba_trum`

```text
Cả bầy trật tự! Báo đốm Jaguar hướng hai giờ, lặn ngầm rút lui hết cho tôi!
```
**Part 2** → `audio/vs/scene05_p2.wav` (407 ký tự) · mood `don_dap`

```text
[surprise-wa] Tuyệt chiêu số một: Chế độ tàu ngầm quân sự! Bạn có nhận thấy mắt, mũi và tai của Ca-py-ba-ra đều nằm thẳng hàng trên một mặt phẳng ở đỉnh đầu không? Thiết kế giải phẫu này giống hệt loài hà mã và cá sấu! Khi ngâm mình dưới nước, toàn bộ thân xác hộ pháp sáu mươi lăm cân chìm nghỉm dưới dòng nước đục, chỉ để lộ ba giác quan nhô lên mặt nước để thở và nghe ngóng mà không để lại một gợn sóng!
```
**Part 3** → `audio/vs/scene05_p3.wav` (259 ký tự) · mood `hao_hung`

```text
Bàn chân của Ca-py-ba-ra có bốn ngón ở chân trước và ba ngón ở chân sau, tất cả đều được nối liền bởi lớp màng bơi tự nhiên. Dưới nước, gã có thể nín thở lặn sâu hoàn toàn suốt năm phút đồng hồ, luồn lách qua các thảm cỏ ngầm để thoát khỏi tầm mắt kẻ săn mồi!
```
**Part 4** → `audio/vs/scene05_p4.wav` (347 ký tự) · mood `don_dap`

```text
Còn nếu bị dồn lên bờ cạn thì sao? [surprise-oh] Hãy chuẩn bị tinh thần cho cú sốc tiếp theo: Gã béo ục ịch này có thể bứt tốc chạy nước rút với vận tốc lên tới ba mươi lăm cây số một giờ! Tốc độ xé gió ngang ngửa một con chó săn chuyên nghiệp, đủ sức bỏ xa hầu hết các loài thú săn mồi trong cự ly ngắn trước khi phóng thẳng xuống nước tẩu thoát!
```

### scene06 — CÚ LỪA GIÁO HỘI VATICAN VÀ BÀI HỌC SỐNG CHILL
*Thẻ chương:* CÚ LỪA ĐƯỢC CÔNG NHẬN LÀ CÁ ĐỂ ĂN MÙA CHAY

*Badge:* `BÀI HỌC SINH TỒN` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (442 ký tự) · mood `hao_hung`

```text
Sự kỳ diệu của Ca-py-ba-ra lớn đến mức từng tạo nên một trong những vụ nhầm lẫn hài hước nhất lịch sử tôn giáo thế giới! Vào thế kỷ mười sáu, khi các nhà truyền giáo Tây Ban Nha đến vùng đầm lầy Venezuela, họ nhìn thấy loài thú này suốt ngày bơi lội dưới nước, chân lại có màng như vịt. Thế là họ gửi thư về Tòa thánh Va-ti-căng để xin phép... [laughter] được xếp Ca-py-ba-ra vào loài cá, để giáo dân có thể ăn thịt trong Mùa Chay kiêng khem!
```
**Part 1** → `audio/vs/scene06_p1.wav` (256 ký tự) · mood `nghiem_trang_gia`

```text
Và thật khó tin, các giám mục thời bấy giờ đã chính thức gật đầu phê chuẩn sắc lệnh coi một con thú gặm nhấm sáu mươi lăm cân có bốn chân và bộ lông xơ cứng là... một loài thủy sản! Một cú lừa tiến hóa vĩ đại mà chính Bố Già Đầm Lầy cũng chẳng thể ngờ tới.
```
**Part 2** → `audio/vs/scene06_p2.wav` (368 ký tự) · mood `am_ap`

```text
Trải qua hàng triệu năm thăng trầm, triết lý sinh tồn mà loài Ca-py-ba-ra để lại cho chúng ta thật sâu sắc: Trong một thế giới đầy rẫy hiểm nguy và áp lực, kẻ chiến thắng sau cùng không phải kẻ cố gồng mình lên thị uy nanh vuốt, mà là kẻ biết giữ cho tâm trí mình luôn phẳng lặng như mặt nước hồ thu, hòa hợp với mọi loài xung quanh để biến kẻ thù thành bạn đồng hành.
```
**Part 3** → `audio/vs/scene06_p3.wav` (184 ký tự) · mood `hao_hung`

```text
[surprise-oh] Bạn ấn tượng nhất với điều gì ở Bố Già Đầm Lầy Ca-py-ba-ra: Khả năng biến cá sấu thành bạn thân, hay bữa sáng tái chế có một không hai? Hãy để lại bình luận bên dưới nhé!
```
**Part 4** → `audio/vs/scene06_p4.wav` (682 ký tự) · mood `tram_bi_an`

```text
Và bây giờ, hãy hướng ngòi bút về phân cảnh kết thúc bí ẩn! Trong tập tiếp theo, chúng ta sẽ lặn xuống đáy đại dương sâu thẳm để diện kiến một bóng đen tí hon vô cùng nguy hiểm. [surprise-wa] Một sinh vật nhỏ bé dài chưa đầy năm xăng-ti-mét, nhưng sở hữu chiếc càng quái đản có thể búng ra âm thanh kinh hoàng lên tới hai trăm mười tám đề-xi-ben, to hơn cả tiếng súng trường và làm nhiễu loạn cả hệ thống sóng siêu âm của tàu ngầm quân sự! Cú búng càng tạo ra luồng nhiệt độ hàng ngàn độ C xé toạc mặt nước, làm con mồi chết đứng từ xa mà không cần chạm vào người! Đố bạn biết danh tính của sát thủ vũ khí âm thanh tí hon này là ai? Hãy đoán tên con vật bên dưới phần bình luận nhé!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Tại sao một gã chuột béo nặng sáu mươi lăm cân lại có thể ngồi uống trà cạnh đàn cá sấu săn mồi mà không mất một cọng lông? Đây là Chuột Lang Nước Ca-py-ba-ra, loài gặm nhấm lớn nhất thế giới sinh sống tại đầm lầy Nam Mỹ! Thứ nhất, kích thước sáu mươi lăm cân cùng lớp da dai và hàm răng cửa sắc như xẻng sắt khiến cá sấu Caiman biết rằng tấn công gã là một canh bạc có thể rách họng chết ngạt. Thứ hai, lưng Ca-py-ba-ra là trạm xe buýt di động: chim rỉa bọ ve, rùa sưởi nắng, bầy khỉ đi nhờ qua sông, biến gã thành bộ trưởng ngoại giao hòa bình của muôn loài. Thứ ba, gã là tàu ngầm sinh học có màng bơi, nín thở lặn sâu năm phút và bứt tốc chạy nước rút ba mươi lăm cây số một giờ ngang chó săn! Nhưng bí mật gây sốc nhất là vào mỗi sáng sớm, Ca-py-ba-ra ăn lại chính phân mềm của mình để hấp thụ trọn vẹn protein lên men! Giữ tâm tĩnh lặng giữa giông bão, đó chính là bí thuật giúp Bố Già Ca-py-ba-ra sống sót ung dung giữa bầy sát thủ đầm lầy!
```

**Whisper prompt:** `Chuột Lang Nước, Capybara, Bố Già Đầm Lầy, Pantanal, 65kg, 91kg, 1,3m, 60cm, 50cm, 35km/h, 5 phút, Morillo, Cecotrophy, Caiman, Jaguar, Anaconda, Vatican, Tupi, 06:00 sáng, 08:00 sáng, 75%, 218 dB, 5cm, Tôm Súng`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| sáu mươi lăm cân | 65kg |
| Sáu mươi lăm cân | 65kg |
| sáu mươi lăm ki-lô-gam | 65kg |
| ba mươi lăm đến sáu mươi sáu cân | 35-66kg |
| Ba mươi lăm đến sáu mươi sáu cân | 35-66kg |
| chín mươi mốt cân | 91kg |
| Chín mươi mốt cân | 91kg |
| một mét ba | 1,3m |
| Một mét ba | 1,3m |
| năm mươi đến sáu mươi xăng-ti-mét | 50-60cm |
| sáu mươi xăng-ti-mét | 60cm |
| năm mươi xăng-ti-mét | 50cm |
| Năm mươi xăng-ti-mét | 50cm |
| một mét rưỡi | 1,5m |
| hai mét | 2m |
| Hai mét | 2m |
| năm phút | 5 phút |
| Năm phút | 5 phút |
| hai tuần tuổi | 2 tuần tuổi |
| Hai tuần tuổi | 2 tuần tuổi |
| ba mươi lăm cây số một giờ | 35km/h |
| Ba mươi lăm cây số một giờ | 35km/h |
| hai mươi cây số một giờ | 20km/h |
| bốn ngón | 4 ngón |
| Bốn ngón | 4 ngón |
| ba ngón | 3 ngón |
| Ba ngón | 3 ngón |
| bảy mươi lăm phần trăm | 75% |
| Bảy mươi lăm phần trăm | 75% |
| một trăm phần trăm | 100% |
| Một trăm phần trăm | 100% |
| bốn mươi phần trăm | 40% |
| năm mươi phần trăm | 50% |
| gấp đôi | gấp đôi |
| hai mươi | 20 |
| ba mươi | 30 |
| bốn mươi | 40 |
| năm mươi | 50 |
| sáu mươi | 60 |
| bảy mươi | 70 |
| tám mươi | 80 |
| chín mươi | 90 |
| một trăm mét | 100m |
| Một trăm mét | 100m |
| một trăm tám mươi độ | 180° |
| Một trăm tám mươi độ | 180° |
| một ngàn | 1.000 |
| hai ngàn | 2.000 |
| thế kỷ mười sáu | thế kỷ 16 |
| Thế kỷ mười sáu | thế kỷ 16 |
| thế kỷ mười tám | thế kỷ 18 |
| Thế kỷ mười tám | thế kỷ 18 |
| sáu giờ sáng | 06:00 sáng |
| Sáu giờ sáng | 06:00 sáng |
| tám giờ sáng | 08:00 sáng |
| Tám giờ sáng | 08:00 sáng |
| mười giờ trưa | 10:00 trưa |
| hai tiếng | 2 tiếng |
| ba tiếng | 3 tiếng |
| hai lần | 2 lần |
| Hai lần | 2 lần |
| ba đến bốn | 3-4 |
| năm đến sáu | 5-6 |
| mười lăm | 15 |
| Mười lăm | 15 |
| hai trăm mười tám đề-xi-ben | 218 dB |
| Hai trăm mười tám đề-xi-ben | 218 dB |
| năm xăng-ti-mét | 5cm |
| Năm xăng-ti-mét | 5cm |
| hàng ngàn độ | hàng ngàn độ |
| Tập mười lăm | Tập 15 |
| Tập mười sáu | Tập 16 |
| Tập mười bốn | Tập 14 |
| Tập mười ba | Tập 13 |
| Ca-py-ba-ra | Capybara |
| Ca-pi-ba-ra | Capybara |
| Mo-ri-lô | Morillo |
| Cát-phát-thơ | Capfather |
| Giác-goa | Jaguar |
| A-na-con-đa | Anaconda |
| Cay-man | Caiman |
| Va-ti-căng | Vatican |
| Tông nhái | Tupi |
| Xê-cô-tơ-rô-phi | Cecotrophy |
| Cơ-rốt-xô-phai | Crossfire |
| P-S-I | PSI |
| hàng triệu năm | hàng triệu năm |
| triệu năm | triệu năm |
| một không hai | 1-0-2 |
| độc nhất vô nhị | độc nhất vô nhị |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · GÃ BÉO 65KG GIA TỘC GẶM NHẤM LÀM CÁ SẤU PHẢI NỂ · 75.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.6 (9.6s) | L01 | Trong thế giới ngầm đầm lầy Pantanal Nam Mỹ, nơi cá sấu Caiman rình rập dưới dòng nước đục, trăn khổng lồ Anaconda siết nghẹt bùn lầy, và báo đốm Jaguar rình rập trên cành cây... |  | Toàn cảnh đầm lầy Pantanal Nam Mỹ bí ẩn và u ám: rặng cây đước rủ rễ, mặt nước đục mờ ảo. BÊN TRÁI một chú chú cá sấu Caiman hoạt hình màu xanh rêu, hàm răng nhọn hoắt lởm chởm, mắt to tròn ngơ ngác đang rình rập thò mắt lên khỏi mặt nước; BÊN PHẢI một con trăn Anaconda khổng lồ đang quấn quanh cành cây ngập nước. KHÔNG có chú Capybara đeo kính râm trong cảnh này. |
| b02 | 00:09.6–00:13.8 (4.2s) | L02 | bạn nghĩ ai mới là kẻ nắm giữ quyền lực tối thượng? Quên hết những bộ nanh vuốt đẫm máu đi! |  | Bầu trời đầm lầy phủ bóng mây kịch tính: BÊN PHẢI trên cành cây cao, một chú chú báo đốm Jaguar dũng mãnh lông vàng đốm hoa mai đen, nanh vuốt nhọn mắt phát sáng vàng rực, móng vuốt giương ra đầy sát khí như chuẩn bị vồ mồi; các cành cây rung chuyển. KHÔNG có chú Capybara đeo kính râm trong cảnh này. |
| b03 | 00:13.8–00:17.0 (3.3s) | L04 | Hãy mở tập hồ sơ mật mang mã số 15 của Bố Già Đầm Lầy. | **HỒ SƠ 15** · tài liệu tối mật · R/380 · [0.75, 0.55] | Cận cảnh một tập hồ sơ mật bìa da màu nâu cũ kỹ, góc trên có đóng dấu triện sáp đỏ ghi chữ 'HỒ SƠ MẬT BỐ GIÀ ĐẦM LẦY'; bên cạnh là một chiếc kính lúp phóng to vào ảnh thẻ của chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi. |
| b04 | 00:17.0–00:25.2 (8.2s) | L05 | Nhân vật đứng đầu danh sách theo dõi của chúng ta hôm nay không phải sát thủ săn mồi nào cả, mà là một gã béo ục ịch nặng tới 65kg, mang họ nhà chuột, | **65kg** · Bố Già đầm lầy · L/380 · [0.3, 0.55] | Chân dung uy quyền hài hước của chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi: ngồi tựa lưng thư thái trên một ụ đất đầm lầy như ngai vàng, ngâm nửa mình dưới dòng nước mát, hai chân trước chắp lại bụng bự, kính râm đen bóng, vẻ mặ |
| b05 | 00:25.2–00:33.4 (8.1s) | L83 | suốt ngày ngâm mình trong nước với vẻ mặt đơ toàn tập không hề biến sắc: Chuột Lang Nước, hay còn gọi bằng danh xưng giang hồ quốc tế là Capybara! |  | Cận cảnh chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi mập mạp béo tròn đang ngâm mình thư thái trong làn nước đầm lầy mát rượi, chiếc mũi nhô lên với cặp kính râm đen nhỏ bóng loáng, mặt đơ toàn tập không hề biến sắc. |
| b06 | 00:33.4–00:39.4 (6.0s) | L06 | Gia tộc gặm nhấm trên khắp Trái Đất thường bị gắn mác là những kẻ lấm lét trốn chui trốn lủi trong góc bếp. |  | BÊN TRÁI là góc bếp tối tăm với ba chú chuột nhắt bé tí đang lấm lét ôm mẩu phô mai run rẩy; tương phản hoàn toàn với BÊN PHẢI là ánh hào quang rực rỡ chiếu xuống chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi oai vệ. |
| b07 | 00:39.4–00:43.2 (3.8s) | L07 | Nhưng Bố Già Đầm Lầy của chúng ta thì ở một đẳng cấp hoàn toàn khác! |  | Ở GIỮA là chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi dáng đứng bệ vệ, khoác hờ một chiếc áo choàng trùm phong cách mafia trên vai; hai bên là các loài chim nhỏ đứng xếp hàng cúi chào cung kính. |
| b08 | 00:43.2–00:50.3 (7.2s) | L08 | Với chiều dài cơ thể lên tới 1,3m và chiều cao vai 60cm, gã chính là loài gặm nhấm lớn nhất thế giới còn tồn tại. | **1,3m** · chiều dài cơ thể · L/360 · [0.35, 0.55]<br>**60cm** · chiều cao vai · R/420 · [0.72, 0.58] | Bố cục so sánh kích thước khoa học: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi đứng cạnh một chiếc thước dây khổng lồ đo chiều dài 1,3m từ mũi đến đuôi; và một chiếc cọc đo chiều cao vai đạt đúng 60cm; mắt chú chuột lang nước Ca |
| b09 | 00:50.3–00:56.4 (6.1s) | L09 | Cá thể lập kỷ lục từng được ghi nhận tại Brazil nặng tới 91kg, to ngang một con lợn rừng trưởng thành! | **91kg** · kỷ lục cân nặng · L/340 · [0.28, 0.52] | Một chiếc cân bàn lò xo cỡ lớn bằng sắt: BÊN TRÁI chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi đứng trên đĩa cân làm kim đồng hồ chỉ vọt tới 91kg; BÊN PHẢI một chú lợn rừng đực to béo há hốc mồm kinh ngạc so sánh kích thước. |
| b10 | 00:56.4–01:02.2 (5.8s) | L10 | Quy tắc thép đầu tiên của gia tộc này khiến mọi nhà sinh vật học phải ngả mũ kinh ngạc: Tuyệt đối không bao giờ hoảng |  | Một bức vẽ phong cách thiền định phương Đông: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi ngồi kiết già trên một bông hoa sen khổng lồ nổi trên mặt nước đầm lầy, xung quanh có vòng hào quang vàng ấm áp tỏa ra; chữ 'ZEN' viết tay  |
| b11 | 01:02.2–01:11.0 (8.9s) | L11 | loạn! Cho dù trời long đất lở, cho dù lũ quét dâng cao hay một con cá sấu khổng lồ đang bò sát sạt bên hông, gương mặt của Capybara vẫn giữ nguyên một nụ cười mỉm thiền định như thể vừa |  | Cảnh tượng hỗn loạn hài hước: bầu trời giông bão sấm chớp đùng đùng, sóng nước dâng cuồn cuộn, một chú chú cá sấu Caiman hoạt hình màu xanh rêu, hàm răng nhọn hoắt lởm chởm, mắt to tròn ngơ ngác to xác đang há hốc mồm bò sát sạt bên cạnh; ở GIỮA chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh |
| b12 | 01:11.0–01:15.7 (4.6s) | L12 | đắc đạo. Đây không phải là sự dũng cảm bộc phát, mà là đỉnh cao của nghệ thuật ngoại giao đầm lầy! |  | Bàn hội nghị ngoại giao đầm lầy: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi ngồi ở đầu bàn, hai bên là cá sấu, báo đốm, trăn anaconda và bồ nông đang ngồi nghe giảng giải; chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, |

### scene02 · TẠI SAO CÁ SẤU CAIMAN KHÔNG DÁM ĂN THỊT BỐ GIÀ? · 93.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:12.7 (12.7s) | L13 | Nếu bạn gõ từ khóa Capybara trên mạng, bức ảnh kinh điển nhất đập vào mắt chắc chắn là cảnh gã béo này nằm phơi bụng ngủ say sưa, trong khi ngay bên cạnh là 3-4 con cá sấu Caiman răng nhọn hoắt đang nằm phơi nắng. | **3-4 con** · cá sấu nằm cạnh · R/360 · [0.75, 0.62] | Bờ cát thoải bên dòng sông đầm lầy: BÊN TRÁI chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi nằm phơi bụng ngửa mặt lên trời ngủ tít mít; BÊN PHẢI là ba đến bốn chú chú cá sấu Caiman hoạt hình màu xanh rêu, hàm răng nhọn hoắt lởm chở |
| b02 | 00:12.7–00:17.1 (4.4s) | L14 | Cảnh tượng phi lý đến mức người ta tưởng đây là sản phẩm của công nghệ chỉnh sửa ảnh! |  | Một chiếc màn hình máy tính hoạt hình đang mở phần mềm chỉnh sửa ảnh, con trỏ chuột phóng to vào bức ảnh chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi và cá sấu; một con dấu 'ẢNH THẬT 100%' màu xanh lá đóng xuống góc ảnh. |
| b03 | 00:17.1–00:23.3 (6.2s) | L15 | Tại sao một kẻ săn mồi khét tiếng vùng đầm lầy lại bỏ qua một khối thịt 65kg béo múp míp đang nằm ngay trước mũi? | **65kg** · khối thịt béo múp · L/380 · [0.28, 0.58] | Dưới góc nhìn của chú chú cá sấu Caiman hoạt hình màu xanh rêu, hàm răng nhọn hoắt lởm chởm, mắt to tròn ngơ ngác: nhìn sang chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi béo mập tròn trịa sáu mươi lăm cân; phía trên đầu chú cá sấu |
| b04 | 00:23.3–00:26.9 (3.6s) | L16 | Hãy nghe chính đại diện giới săn mồi lên tiếng giải thích lý do thực tế. |  | Khung cảnh phỏng vấn truyền hình: Một chiếc micro có logo đài truyền hình đầm lầy chìa vào sát mõm chú chú cá sấu Caiman hoạt hình màu xanh rêu, hàm răng nhọn hoắt lởm chởm, mắt to tròn ngơ ngác; chú cá sấu Caiman hoạt hình màu xanh rêu, hàm răng nhọn hoắt lởm chởm, mắt to tròn ngơ ngác đeo cà vạt hoa văn da sấu, giơ hai tay lên phân trần đầy bối rối. |
| b05 | 00:26.9–00:29.8 (2.9s) | L17 | Tôi mà đụng vào gã béo này là gãy cả hàm đấy! |  | Góc quay cận cảnh hài hước: Chú chú cá sấu Caiman hoạt hình màu xanh rêu, hàm răng nhọn hoắt lởm chởm, mắt to tròn ngơ ngác cầm một chiếc hàm răng giả bằng nhựa bị gãy đôi ba chiếc răng nanh, vẻ mặt méo mó đau khổ; phía sau là hình bóng chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo |
| b06 | 00:29.8–00:38.0 (8.2s) | L18 | Vừa to vừa nặng, da thì dai nhách, mà còn là trạm cảnh báo động đất của cả khu vực, dại gì nuốt cho nghẹn họng! Đúng như lời gã cá sấu thú nhận! |  | Hình ảnh tia X-quang hài hước: chú cá sấu Caiman hoạt hình màu xanh rêu, hàm răng nhọn hoắt lởm chởm, mắt to tròn ngơ ngác đang há to mồm cố nuốt một khối thịt hình tròn khổng lồ nhưng bị mắc nghẹn ngang cổ họng, hai mắt lồi ra nghẹt thở; bên cạnh là biểu tượng cảnh báo dấu chéo đỏ. |
| b07 | 00:38.0–00:42.7 (4.7s) | L20 | Cá sấu Caiman ở vùng Pantanal thường chỉ dài 1,5m đến 2m, chuyên săn cá và chim nhỏ. | **1,5m-2m** · chiều dài Caiman · L/360 · [0.32, 0.6] | BÊN TRÁI là chú chú cá sấu Caiman hoạt hình màu xanh rêu, hàm răng nhọn hoắt lởm chởm, mắt to tròn ngơ ngác kích thước khiêm tốn dài 1,5m đang há mồm đớp một con cá nhỏ bơi qua; BÊN PHẢI là chiếc thước đo chiều dài 2m thể hiện giới hạn cơ thể của loài cá sấu này. |
| b08 | 00:42.7–00:46.9 (4.2s) | L21 | Nuốt một con Bố Già Đầm Lầy trưởng thành là canh bạc nguy hiểm có thể làm chúng rách họng chết ngạt. |  | Một chiếc cân đong rủi ro: BÊN TRÁI là phần thưởng một bữa ăn; BÊN PHẢI là chiếc xương hàm cá sấu bị nứt gãy và nguy cơ rách thực quản nặng nề nghiêng hẳn cán cân xuống. |
| b09 | 00:46.9–00:53.5 (6.6s) | L22 | Chưa kể, gã béo này sở hữu cặp răng cửa sắc như xẻng sắt, nếu bị dồn vào đường cùng thì một cú cắn tự vệ cũng đủ bẻ gãy xương mõm cá sấu! |  | Đặc tả hàm răng đáng sợ của chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, |
| b10 | 00:53.5–00:59.9 (6.4s) | L23 | Chưa dừng lại ở đó, gã chuột lang nước này còn kiêm luôn chức vụ Giám đốc trạm dịch vụ giao thông công cộng lớn nhất rừng nhiệt đới. |  | Biển hiệu hoạt hình lớn: 'TRẠM XE BUÝT CÔNG CỘNG PANTANAL'; chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi đội chiếc mũ tài xế xe buýt màu xanh, hai bên sườn vẽ họa tiết xe buýt số 15 chạy tuyến đầm lầy. |
| b11 | 00:59.9–01:04.3 (4.4s) | L24 | Lưng của Capybara phẳng lì và rộng thênh thang như chiếc ghế sô-pha di động. |  | Lưng của chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi biến thành chiếc ghế sô-pha nhung màu xanh êm ái: một chú chim đầm lầy chân dài đang đi dạo trên lưng, nhặt từng con bọ ve nhỏ xíu bỏ vào mồm ngon lành. |
| b12 | 01:04.3–01:13.5 (9.2s) | L25 | Chim chóc đầm lầy đậu lên lưng để rỉa bọ ve ký sinh, đàn rùa nước 5-6 con trèo lên mai nằm sưởi ấm, và bầy khỉ sóc thì biến gã thành chiếc phà an toàn qua sông! | **5-6 con** · rùa nằm trên mai · R/380 · [0.65, 0.48] | Cảnh tượng siêu đông đúc vui nhộn: Trên lưng chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi có đàn rùa nước năm đến sáu con xếp hàng nằm phơi mai; trên đỉnh đầu chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu và |
| b13 | 01:13.5–01:18.5 (4.9s) | L26 | Bác bồ nông ơi, mông tôi là thịt chứ không phải con cá đâu, kẹp hoài không chán à? |  | Cận cảnh tình huống hài hước: Chú chú chim bồ nông hoạt hình mỏ vàng khổng lồ, túi da dưới mỏ xệ xuống mỏ vàng khổng lồ đang há to mồm kẹp trọn mông tròn trịa của chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi; chú chuột lang nước C |
| b14 | 01:18.5–01:28.7 (10.2s) | L27 | Thậm chí cả loài chim bồ nông tham ăn nổi tiếng cũng từng há mỏ kẹp thử vào mông Capybara trong vô vọng, còn gã chuột lang thì chỉ ngoái đầu lại nhìn với vẻ mặt thương hại rồi... ngủ tiếp! |  | Chú chú chim bồ nông hoạt hình mỏ vàng khổng lồ, túi da dưới mỏ xệ xuống cố hết sức nuốt nhưng chiếc mỏ căng phồng biến dạng thành hình cái mông tròn trịa của chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi, hai mắt bồ nông xoay vòng |
| b15 | 01:28.7–01:33.4 (4.7s) | L28 | Một mối quan hệ cộng sinh đôi bên cùng có lợi mà giới khoa học gọi là tuyệt tác hòa bình của tự nhiên. |  | Toàn cảnh bình yên đầm lầy: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi cùng đàn con, rùa, cá sấu và chim chóc cùng quây quần bên bờ nước dưới ánh hoàng hôn ấm áp; biểu tượng hai bàn tay bắt chặt nhau lấp lánh ở GIỮA. |

### scene03 · TUYẾN MÙI MORILLO TRÊN MŨI VÀ TIẾNG SỦA BÁO ĐỘNG · 89.8s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:04.2 (4.2s) | L29 | Bất kỳ đế chế nào muốn tồn tại lâu dài cũng phải xây dựng một mạng lưới liên lạc bí mật hoàn |  | Sơ đồ mạng lưới tình báo thế giới ngầm: Một tấm bản đồ rừng rậm Pantanal có các đường dây nối mạng từ mũi của các Bố Già; các biểu tượng mùi hương lan tỏa khắp các ngóc ngách đầm lầy. |
| b02 | 00:04.2–00:08.8 (4.7s) | L30 | hảo. Và vũ khí ngoại giao lợi hại nhất của Bố Già Đầm Lầy nằm ngay trên chóp mũi! |  | Cận cảnh đặc tả chiếc đầu của chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi: một mũi tên vàng rực chỉ thẳng vào đỉnh sống mũi vuông vức; nơi có một khối u nổi gồ lên như viên ngọc đen quyền lực. |
| b03 | 00:08.8–00:14.0 (5.2s) | L31 | Nếu quan sát kỹ một con đực đầu đàn, bạn sẽ thấy một khối u màu đen sẫm, trơn bóng nổi rõ trên sống mũi. |  | Phóng to kính hiển vi vào khối u trên mũi của chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi: bề mặt da trơn nhẵn, sẫm màu, không có lông; các hạt tinh thể sáp màu trắng lấp lánh đang tiết ra từ lỗ chân lông. |
| b04 | 00:14.0–00:17.7 (3.6s) | L32 | Trong giới sinh học, khối u quyền lực này được gọi là tuyến Morillo. | **MORILLO** · tuyến mùi quyền lực · R/380 · [0.68, 0.45] | Bảng giải phẫu sinh học: Nhãn tên lớn viết chữ 'TUYẾN MORILLO' trên nền thẻ màu đỏ uy quyền; bên cạnh là sơ đồ ống dẫn dịch tiết xạ hương nối thẳng vào tuyến mũi. |
| b05 | 00:17.7–00:22.3 (4.6s) | L33 | Tuyến Morillo liên tục tiết ra một chất dịch sáp màu trắng chứa hỗn hợp xạ hương cực mạnh. |  | Một chiếc lọ thủy tinh cổ cong đựng dung dịch sáp màu trắng đang bốc hơi xạ hương thơm ngát màu tím; chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi đứng bên cạnh như một nhà pha chế nước hoa cao cấp của đầm lầy. |
| b06 | 00:22.3–00:30.2 (7.9s) | L34 | Mỗi khi đi tuần tra qua các gốc sậy hay thân cây gãy, Bố Già chỉ cần quẹt nhẹ chiếc mũi quyền lực của mình lên vỏ cây để ký tên đóng dấu lãnh thổ. |  | chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi cúi đầu cọ nhẹ chiếc mũi có tuyến Morillo vào một thân cây sậy gãy; vết cọ để lại một vệt sáp trắng phát sáng hình con dấu Bố Già 'CAPFATHER SIGNATURE'. |
| b07 | 00:30.2–00:37.2 (7.0s) | L35 | Kết hợp với hai túi tuyến mùi hương ở hai bên hậu môn, mỗi cá thể Capybara sở hữu một bản mã hóa sinh học độc nhất vô nhị! |  | Sơ đồ hai đầu phát tín hiệu: Một mũi tên chỉ vào tuyến mũi Morillo ở đầu; và một mũi tên chỉ vào hai túi tuyến mùi hậu môn ở đuôi; tạo thành hệ thống mã vạch sinh học hai đầu hoàn chỉnh. |
| b08 | 00:37.2–00:51.0 (13.8s) | L36 | Nhờ hệ thống chữ ký mùi hương này, các thành viên trong gia tộc chỉ cần hít nhẹ một cái là biết ngay đối phương thuộc phe nào, địa vị xã hội cao hay thấp, thậm chí cả tình trạng sức khỏe hôm nay ra sao mà không cần phí một giọt máu để đấm đá tranh giành thứ bậc! |  | Hai chú Capybara đối diện nhau: một chú hít nhẹ mũi vào thân cây; phía trên đầu chú hiện lên màn hình thông số HUD hiển thị đầy đủ: 'BỐ GIÀ KHU BẮC - ĐỘI TRƯỞNG - SỨC KHỎE 100%'. |
| b09 | 00:51.0–00:56.8 (5.8s) | L37 | Lão sống ở Pantanal 80 năm rồi, chưa thấy chiếc xe buýt nào êm ái và đúng giờ như lưng gã này! | **80 NĂM** · tuổi thọ chứng nhân · L/360 · [0.3, 0.52] | Một chú rùa già đeo kính lão, mai phủ đầy rêu phong cổ kính đang gật gù hài lòng; phía trước là chiếc mai chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi chở rùa điềm đạm rẽ nước qua đầm lầy. |
| b10 | 00:56.8–01:01.0 (4.2s) | L38 | Nhưng đỉnh cao nhất trong kho vũ khí của gia tộc này chính là hệ thống điện đàm âm thanh! |  | Chiếc đài radio vệ tinh đầm lầy: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi đeo tai nghe phi công, các dải sóng âm thanh đủ màu sắc phát ra từ miệng: sóng nhạc êm dịu, sóng huýt sáo và sóng còi báo động. |
| b11 | 01:01.0–01:08.9 (7.9s) | L39 | Đôi tai hình bán nguyệt của Capybara có thể xoay 180° độc lập, bắt trọn tiếng chân rón rén của kẻ thù từ khoảng cách hơn 100m. | **180°** · tai xoay độc lập · L/360 · [0.35, 0.42]<br>**100m** · khoảng cách nghe · R/420 · [0.72, 0.58] | Cận cảnh đôi tai tròn nhỏ của chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi: tai trái xoay về hướng 90 độ, tai phải xoay về hướng 180 độ độc lập; chiếc radar quét sóng phát hiện bước chân kẻ thù cách xa 100m. |
| b12 | 01:08.9–01:12.3 (3.4s) | L40 | Khi vui vẻ thư giãn, chúng phát ra tiếng rên hừ hừ như mèo. |  | chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi nằm cuộn tròn trên thảm cỏ, miệng phát ra tiếng rên hừ hừ như mèo con; những nốt nhạc nốt son nốt mi màu hồng bay bổng xung quanh. |
| b13 | 01:12.3–01:15.8 (3.5s) | L41 | Khi gọi đàn con, chúng huýt sáo lảnh lót như chim sơn ca. |  | chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi chu mỏ huýt sáo vang dội như chú chim hót líu lo; phía sau là đàn bốn chú chuột lang con chân ngắn lon ton chạy ùa lại ríu rít. |
| b14 | 01:15.8–01:21.7 (5.9s) | L42 | Nhưng một khi phát hiện bóng dáng sát thủ báo đốm, con đầu đàn sẽ tung ra một cú sủa đanh thép như chó săn chuyên nghiệp! |  | Ánh mắt chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi đột ngột sắc lẹm: Phía xa trong bụi rậm lộ ra đôi mắt vằn vện của chú chú báo đốm Jaguar dũng mãnh lông vàng đốm hoa mai đen, nanh vuốt nhọn; chú chuột lang nước Capybara hoạt h |
| b15 | 01:21.7–01:29.8 (8.0s) | L43 | Cú sủa báo động này có tần số đặc biệt làm chấn động cả đầm lầy, khiến từ bầy khỉ trên ngọn cây đến lũ hươu bờ sông đều lập tức nhảy dựng lên bỏ chạy thoát thân trong gang tấc! |  | chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi há to mồm tung cú sủa 'GÂU! GÂU!' chấn động: luồng sóng âm màu đỏ bùng nổ như loa phát thanh; đàn khỉ trên cây nhảy dựng bắn người lên cành cao, đàn hươu lao thục mạng. |

### scene04 · TẬP TÍNH ĂN LẠI PHÂN SÁNG SỚM ĐỂ HẤP THỤ PROTEIN · 88.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:04.5 (4.5s) | L44 | Nào, bây giờ là lúc chúng ta phải lật mở trang hồ sơ đen tối và nhạy cảm nhất của Bố Già Đầm |  | Khung cảnh phòng thẩm vấn bí mật: Một chiếc bàn gỗ với một chiếc đèn chụp chiếu thẳng xuống một phong bì màu đen niêm phong dấu đỏ 'TUYỆT MẬT - GÓC KHUẤT BỐ GIÀ'. |
| b02 | 00:04.5–00:10.5 (5.9s) | L45 | Lầy. Nếu bạn đang ăn sáng hay vừa nhâm nhi cốc trà sữa, tôi chân thành khuyên bạn hãy tạm đặt cốc xuống trong hai phút tới! |  | BÊN TRÁI một khán giả hoạt hình đang cầm cốc trà sữa bỗng sững sờ dừng lại, mắt trợn tròn; BÊN PHẢI một biển báo cảnh báo hài hước hình nĩa và thìa bị gạch chéo đỏ. |
| b03 | 00:10.5–00:14.6 (4.1s) | L46 | Bởi vì món ăn khoái khẩu giúp gã béo này duy trì thân hình hộ pháp 65kg... | **65kg** · thân hình hộ pháp · L/380 · [0.32, 0.58] | chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi thân hình hộ pháp béo tròn sáu mươi lăm cân đang đứng cạnh một chiếc đĩa bạc sang trọng có nắp đậy kiểu nhà hàng năm sao; nắp đậy bắt đầu rung rinh hé mở. |
| b04 | 00:14.6–00:18.4 (3.8s) | L47 | chính là sản phẩm do chính gã vừa thải ra! Khoan vội bịt mũi phán |  | Chiếc nắp đĩa bạc mở tung: bên trong là những viên phân màu xanh lục mềm mại bốc khói nhẹ; chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi đeo khăn ăn ở cổ, cầm dao nĩa sẵn sàng thưởng thức với vẻ mặt thỏa mãn. |
| b05 | 00:18.4–00:25.2 (6.8s) | L49 | xét! Dưới góc nhìn của khoa học dinh dưỡng, đây là một tuyệt tác tiến hóa sinh tồn bậc thầy mang tên Cecotrophy, hay tập tính ăn phân có chọn |  | Một cuốn bách khoa toàn thư sinh học mở toang trang sách có hình vẽ danh xưng khoa học 'CECOTROPHY - TẬP TÍNH ĂN PHÂN CÓ CHỌN LỌC' cùng huy chương vàng tiến hóa. |
| b06 | 00:25.2–00:30.1 (4.9s) | L50 | lọc! Khẩu phần ăn của Capybara chiếm tới 75% là cỏ đầm lầy và thực vật thủy sinh thô ráp. | **75%** · khẩu phần cỏ thô · R/360 · [0.68, 0.48] | Biểu đồ tròn dinh dưỡng: Bảy mươi lăm phần trăm chiếc đĩa là bó cỏ đầm lầy và rong rêu thô ráp; hai mươi lăm phần trăm còn lại là vỏ cây khô; chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi nhai cỏ cật lực như máy cắt cỏ. |
| b07 | 00:30.1–00:34.9 (4.8s) | L51 | Cỏ nghèo dinh dưỡng đến mức chất xơ xen-lu-lô-zơ gần như không thể bị phân hủy bởi dạ dày thông thường. |  | Cận cảnh phân tử sợi xen-lu-lô-zơ cứng như những thanh thép đan lưới; dịch axit dạ dày thông thường dội vào đều bị bật ngược trở ra bất lực. |
| b08 | 00:34.9–00:42.8 (7.9s) | L52 | Để giải quyết bài toán hóc búa này, tạo hóa trang bị cho Capybara một chiếc ruột tịt khổng lồ chứa hàng tỷ vi khuẩn lên men đặc chủng. |  | Hình ảnh giải phẫu bộ máy tiêu hóa của chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi: Một chiếc ruột tịt khổng lồ màu hồng như nhà máy lên men hóa chất; bên trong hàng triệu chú vi khuẩn hoạt hình tí hon đeo kính bảo hộ đang cầm bú |
| b09 | 00:42.8–00:52.3 (9.5s) | L53 | Cứ vào khoảng từ 06:00 sáng đến 08:00 sáng mỗi ngày, sau một đêm dài vi khuẩn cật lực làm việc, cơ thể gã sẽ thải ra một loại phân mềm đặc biệt màu xanh lục gọi là phân manh tràng. | **06h - 08h** · giờ ăn phân mềm · L/360 · [0.28, 0.52] | Một chiếc đồng hồ báo thức chỉ đúng khung giờ từ 06:00 sáng đến 08:00 sáng; ánh ban mai rọi xuống chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi vừa thức giấc sau giấc ngủ đêm dài. |
| b10 | 00:52.3–00:57.1 (4.8s) | L54 | Loại phân này chứa hàm lượng protein gấp đôi phân thường và ngập tràn vitamin nhóm B! | **2X PROTEIN** · dinh dưỡng đậm đặc · R/380 · [0.72, 0.55] | Ống nghiệm phân tích mẫu phân mềm manh tràng: cột đo chỉ số protein vọt lên gấp đôi so với mẫu phân thường; các viên vitamin B1, B12 màu vàng lấp lánh bay quanh ống nghiệm. |
| b11 | 00:57.1–01:05.8 (8.7s) | L55 | Thay vì lãng phí nguồn tài nguyên quý giá trôi theo dòng nước, Bố Già lập tức cúi xuống ăn lại toàn bộ chỗ phân mềm này để hệ tiêu hóa hấp thụ dưỡng chất lần thứ hai! |  | chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi cúi đầu xuống gặm lại món phân mềm giàu dưỡng chất vừa thải ra trên thảm cỏ ướt sương; biểu tượng tái chế mũi tên xanh xoay vòng tròn ba cạnh hoàn hảo. |
| b12 | 01:05.8–01:14.0 (8.2s) | L56 | Ngay từ khi mới được 2 tuần tuổi, những chú chuột lang nước con đã bắt đầu học tập thói quen này từ mẹ để cấy hệ vi sinh đường ruột quý giá vào cơ thể. | **2 TUẦN** · chuột con học mẹ · L/380 · [0.32, 0.58] | Chú Capybara con bé xíu mới hai tuần tuổi đứng cạnh mẹ, lon ton bắt chước mẹ cúi xuống ăn phân mềm để đón nhận vi khuẩn đường ruột quý giá; mẹ mỉm cười xoa đầu con. |
| b13 | 01:14.0–01:22.8 (8.7s) | L57 | Phải đến buổi chiều, sau khi đã bòn rút sạch sẽ đến phân tử protein cuối cùng, gã mới thải ra những viên phân khô cứng hình bầu dục không còn giá trị dinh dưỡng. |  | Bầu trời chuyển sang ánh hoàng hôn tím: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi thải ra những viên phân hình bầu dục màu nâu sẫm, khô cứng như hạt ô-liu; chiếc máy đo dinh dưỡng quét qua báo '0% PROTEIN'. |
| b14 | 01:22.8–01:28.7 (6.0s) | L58 | Kỳ dị, khó ngửi, nhưng chính món súp vi khuẩn tái chế này đã nuôi sống cả đế chế gặm nhấm suốt hàng triệu năm qua! |  | Cả bầy Capybara mập mạp béo tốt đứng vững chãi trên bờ đầm lầy qua hàng triệu năm lịch sử; bên cạnh là một bát súp vi khuẩn vàng óng tượng trưng cho nguồn năng lượng sinh tồn. |

### scene05 · TÀU NGẦM NÍN THỞ 5 PHÚT VÀ CÚ BỨT TỐC 35 KM/H · 68.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.9 (8.9s) | L59 | Đừng bao giờ để dáng vẻ chậm chạp ung dung của Bố Già đánh lừa thị giác! Trong thế giới giang hồ, kẻ sống sót lâu nhất không phải kẻ to mồm nhất, mà là kẻ sở hữu lối thoát hiểm tinh quái nhất. |  | Bờ đầm lầy căng thẳng: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi đang thong thả ăn cỏ thì từ bụi rậm phía sau, đôi mắt vàng rực của chú chú báo đốm Jaguar dũng mãnh lông vàng đốm hoa mai đen, nanh vuốt nhọn nhô ra; tiếng còi bá |
| b02 | 00:08.9–00:15.6 (6.7s) | L84 | Một khi sát thủ đỉnh chóp Báo Đốm Jaguar xuất hiện với cặp móng vuốt chết chóc, Capybara lập tức kích hoạt chế độ đào tẩu cấp độ đỏ! |  | Một chú chú báo đốm Jaguar dũng mãnh lông vàng đốm hoa mai đen, nanh vuốt nhọn mắt sáng rực giương cặp móng vuốt vồ xuống từ cành cây; chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi ở GIỮA bật chế độ báo động khẩn cấp màu đỏ, bụi nư |
| b03 | 00:15.6–00:22.7 (7.1s) | L60 | Cả bầy trật tự! Báo đốm Jaguar hướng hai giờ, lặn ngầm rút lui hết cho tôi! Tuyệt chiêu số một: Chế độ tàu ngầm |  | Một cô Capybara mẹ đầu đàn đeo nơ hoa trên đầu, hai chân trước giơ cờ hiệu chỉ huy; cả đàn chuột con lập tức nối đuôi nhau nhảy ào xuống dòng nước đục. |
| b04 | 00:22.7–00:27.9 (5.2s) | L62 | quân sự! Bạn có nhận thấy mắt, mũi và tai của Capybara đều nằm thẳng hàng trên một mặt phẳng ở đỉnh đầu không? |  | Bản vẽ giải phẫu kỹ thuật quân sự: Ba đường gióng màu vàng nối thẳng tắp từ Mắt qua Mũi đến Tai trên đỉnh đầu chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi; mặt nước ngang đúng đường gióng này như kính tiềm vọng tàu ngầm. |
| b05 | 00:27.9–00:30.4 (2.5s) | L63 | Thiết kế giải phẫu này giống hệt loài hà mã và cá sấu! |  | Bố cục so sánh ba loài thủy quái đầm lầy: BÊN TRÁI là đầu Hà Mã, Ở GIỮA là đầu chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi, BÊN PHẢI là đầu Cá Sấu; cả ba đều có mắt mũi tai thẳng hàng trên đỉnh đầu giống hệt nhau. |
| b06 | 00:30.4–00:39.0 (8.6s) | L64 | Khi ngâm mình dưới nước, toàn bộ thân xác hộ pháp 65kg chìm nghỉm dưới dòng nước đục, chỉ để lộ ba giác quan nhô lên mặt nước để thở và nghe ngóng mà không để lại một gợn sóng! | **65kg** · tàu ngầm bọc thịt · L/380 · [0.35, 0.62] | Góc nhìn cắt ngang dưới nước: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi trôi bồng bềnh dưới lòng sông đục như một chiếc tàu ngầm hạt nhân màu nâu; bên trên mặt nước chú chú báo đốm Jaguar dũng mãnh lông vàng đốm hoa mai đen, na |
| b07 | 00:39.0–00:45.3 (6.3s) | L65 | Bàn chân của Capybara có 4 ngón ở chân trước và 3 ngón ở chân sau, tất cả đều được nối liền bởi lớp màng bơi tự nhiên. | **4 NGÓN** · chân trước có màng · L/360 · [0.3, 0.52]<br>**3 NGÓN** · chân sau có màng · R/420 · [0.72, 0.58] | Phóng to bàn chân đặc biệt của chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi: chân trước có bốn ngón xòe rộng, chân sau có ba ngón; giữa các kẽ ngón chân là lớp màng bơi mỏng dai như chân vịt; chiếc móng vuốt ngắn bám chắc vào bùn. |
| b08 | 00:45.3–00:52.6 (7.3s) | L66 | Dưới nước, gã có thể nín thở lặn sâu hoàn toàn suốt 5 phút đồng hồ, luồn lách qua các thảm cỏ ngầm để thoát khỏi tầm mắt kẻ săn mồi! | **5 PHÚT** · nín thở lặn sâu · R/360 · [0.75, 0.48] | Cảnh lặn ngầm sâu dưới đáy sông: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi khép chặt tai và lỗ mũi lại, bơi lướt êm ái giữa rừng rong rêu thủy sinh; một chiếc đồng hồ bấm giờ đếm ngược 5 phút đặt ở góc phải. |
| b09 | 00:52.6–00:55.1 (2.5s) | L67 | Còn nếu bị dồn lên bờ cạn thì sao? |  | chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi đang đứng trên bờ bãi cỏ khô, phía sau là bờ vực cát; chú chú báo đốm Jaguar dũng mãnh lông vàng đốm hoa mai đen, nanh vuốt nhọn từ từ tiến lại gần với vẻ mặt đắc thắng tưởng chừng đã b |
| b10 | 00:55.1–01:01.8 (6.7s) | L68 | Hãy chuẩn bị tinh thần cho cú sốc tiếp theo: Gã béo ục ịch này có thể bứt tốc chạy nước rút với vận tốc lên tới 35km/h! | **35 km/h** · tốc độ bứt phá · R/360 · [0.72, 0.52] | Khoảnh khắc bứt tốc không tưởng: Bốn chân chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi đạp mạnh tung tóe bùn đất, cơ thể béo tròn biến thành một viên đạn đại bác màu nâu lao vút đi với tốc độ 35 km/h, bụi mù mịt bốc lên phía sau. |
| b11 | 01:01.8–01:08.7 (6.9s) | L69 | Tốc độ xé gió ngang ngửa một con chó săn chuyên nghiệp, đủ sức bỏ xa hầu hết các loài thú săn mồi trong cự ly ngắn trước khi phóng thẳng xuống nước tẩu thoát! |  | Cuộc đua tốc độ trên thảo nguyên: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi chạy song song vượt mặt một chú chó săn đang thở hồng hộc; máy đo tốc độ bắn tia laser xác nhận bỏ xa kẻ săn mồi. |

### scene06 · CÚ LỪA GIÁO HỘI VATICAN VÀ BÀI HỌC SỐNG CHILL · 95.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:14.6 (14.6s) | L70 | Sự kỳ diệu của Capybara lớn đến mức từng tạo nên một trong những vụ nhầm lẫn hài hước nhất lịch sử tôn giáo thế giới! Vào thế kỷ 16, khi các nhà truyền giáo Tây Ban Nha đến vùng đầm lầy Venezuela, họ nhìn thấy loài thú này suốt ngày bơi lội dưới nước, chân lại có màng như vịt. | **THẾ KỶ 16** · nhầm lẫn lịch sử · L/360 · [0.28, 0.5] | Khung cảnh lịch sử thế kỷ 16: Một chiếc thuyền buồm Tây Ban Nha cập bến bờ đầm lầy Venezuela; các nhà truyền giáo mặc áo choàng nâu đang kinh ngạc chỉ tay vào đàn chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi bơi lội dưới nước. |
| b02 | 00:14.6–00:18.1 (3.6s) | L71 | Thế là họ gửi thư về Tòa thánh Vatican để xin phép... |  | Một lá thư cổ viết tay bằng mực lông ngỗng có gắn con dấu sáp đỏ gửi qua đường biển về tòa thánh Vatican ở Rome; bức thư vẽ hình chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi có thêm chiếc đuôi cá ngộ nghĩnh. |
| b03 | 00:18.1–00:23.1 (4.9s) | L72 | được xếp Capybara vào loài cá, để giáo dân có thể ăn thịt trong Mùa Chay kiêng khem! |  | Bàn tiệc Mùa Chay của các giáo sĩ: Giữa bàn là một chiếc đĩa lớn bày món thịt nướng; một tấm biển ghi 'THỰC ĐƠN MÙA CHAY: CÁ ĐẦM LẦY' với hình chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi bơi lội kế bên. |
| b04 | 00:23.1–00:31.4 (8.3s) | L73 | Và thật khó tin, các giám mục thời bấy giờ đã chính thức gật đầu phê chuẩn sắc lệnh coi một con thú gặm nhấm 65kg có bốn chân và bộ lông xơ cứng là... một loài thủy sản! | **CÁ 65KG?!** · sắc lệnh kỳ quặc · R/380 · [0.72, 0.55] | Tòa thánh Vatican trang nghiêm: Các giám mục mặc áo choàng đỏ đang đồng loạt đặt bút ký tên và đóng dấu triện vàng lên sắc lệnh công nhận chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi sáu mươi lăm cân chính thức là loài cá. |
| b05 | 00:31.4–00:35.0 (3.6s) | L74 | Một cú lừa tiến hóa vĩ đại mà chính Bố Già Đầm Lầy cũng chẳng thể ngờ tới. |  | chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi đang đội một chiếc vương miện hình con cá nhỏ trên đầu, đeo kính râm cười toe toét; phía sau là tấm bảng phả hệ động vật có vú bị sửa thành bộ Cá. |
| b06 | 00:35.0–00:43.0 (8.0s) | L75 | Trải qua hàng triệu năm thăng trầm, triết lý sinh tồn mà loài Capybara để lại cho chúng ta thật sâu sắc: Trong một thế giới đầy rẫy hiểm nguy và áp lực, |  | Bức tranh nghệ thuật hoàng hôn tuyệt đẹp trên đầm lầy: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi ngồi thảnh thơi bên bờ nước tĩnh lặng như gương, chim chóc bay lượn, gió lay rặng lau sậy; ánh sáng vàng cam chiếu rọi bình yên. |
| b07 | 00:43.0–00:53.6 (10.6s) | L85 | kẻ chiến thắng sau cùng không phải kẻ cố gồng mình lên thị uy nanh vuốt, mà là kẻ biết giữ cho tâm trí mình luôn phẳng lặng như mặt nước hồ thu, hòa hợp với mọi loài xung quanh để biến kẻ thù thành bạn đồng hành. |  | Bức tranh triết lý thiền định: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi ngồi tĩnh tâm như tượng Phật giữa đầm lầy, mặt nước xung quanh phẳng lặng như gương; phản chiếu bầu trời xanh và mây trắng yên bình. |
| b08 | 00:53.6–01:02.6 (9.0s) | L76 | Bạn ấn tượng nhất với điều gì ở Bố Già Đầm Lầy Capybara: Khả năng biến cá sấu thành bạn thân, hay bữa sáng tái chế có 1-0-2? Hãy để lại bình luận bên dưới nhé! |  | Khung hình tương tác hai lựa chọn vui nhộn: BÊN TRÁI là biểu tượng bắt tay làm bạn với cá sấu; BÊN PHẢI là biểu tượng chiếc đĩa ăn phân tái chế protein; chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi ở GIỮA chỉ tay mời khán giả bình |
| b09 | 01:02.6–01:05.6 (3.0s) | L78 | Và bây giờ, hãy hướng ngòi bút về phân cảnh kết thúc bí |  | Bàn vẽ hoạt hình chuyển sang tông màu xanh thẳm của đáy đại dương sâu; ánh sáng đèn pin quét qua mặt giấy trắng hé lộ một bí mật mới sắp bắt đầu. |
| b10 | 01:05.6–01:12.0 (6.4s) | L79 | ẩn! Trong tập tiếp theo, chúng ta sẽ lặn xuống đáy đại dương sâu thẳm để diện kiến một bóng đen tí hon vô cùng nguy hiểm. |  | Khung cảnh đáy biển sâu thẳm đầy bí ẩn: San hô và đá ngầm mờ ảo; ở GIỮA là BÓNG ĐEN HOÀN TOÀN (solid black silhouette) của một sinh vật nhỏ bé có một chiếc càng khổng lồ bất cân xứng, viền hào quang phát sáng cyan. |
| b11 | 01:12.0–01:23.4 (11.4s) | L80 | Một sinh vật nhỏ bé dài chưa đầy 5cm, nhưng sở hữu chiếc càng quái đản có thể búng ra âm thanh kinh hoàng lên tới 218 dB, to hơn cả tiếng súng trường và làm nhiễu loạn cả hệ thống sóng siêu âm của tàu ngầm quân | **5cm** · kích thước tí hon · L/360 · [0.3, 0.52]<br>**218 dB** · tiếng nổ xé nước · R/420 · [0.72, 0.58] | Đặc tả chiếc càng bóng đen bí ẩn: một chiếc càng lớn gấp đôi thân mình đang mở hé; bên cạnh là chiếc thước đo 5cm và đồng hồ đo âm thanh vọt lên mức 218 dB đỏ rực. |
| b12 | 01:23.4–01:29.7 (6.3s) | L81 | sự! Cú búng càng tạo ra luồng nhiệt độ hàng ngàn độ C xé toạc mặt nước, làm con mồi chết đứng từ xa mà không cần chạm |  | Vụ nổ sóng xung kích dưới biển: Cú búng càng tạo ra một bọt khí phát sáng rực rỡ như tia chớp nhỏ, sóng xung kích tỏa ra làm một chú cá bơi gần choáng váng; phía xa một chiếc tàu ngầm quân sự bị nhiễu sóng sonar. |
| b13 | 01:29.7–01:35.7 (6.0s) | L82 | vào người! Đố bạn biết danh tính của sát thủ vũ khí âm thanh tí hon này là ai? Hãy đoán tên con vật bên dưới phần bình luận nhé! |  | BÓNG ĐEN BÍ ẨN (solid black silhouette) của sát thủ tí hon nổi bật ở GIỮA, phía trên đầu là một DẤU HỎI CHẤM LỚN MÀU VÀNG óng ánh; dòng chữ 'ĐOÁN TÊN CON VẬT TẬP 16' phát sáng lung linh. |

## 5. Phân cảnh Shorts — từng beat

Banner: **BỐ GIÀ 65KG ĐẦM LẦY: / CÁ SẤU CŨNG PHẢI NỂ!** · giọng 50.3s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Tại sao một gã chuột béo nặng 65kg lại có thể ngồi uống trà cạnh đàn cá sấu săn mồi mà không mất một cọng lông? | **65kg** · Bố Già đầm lầy · L/580 · [0.35, 0.55] |
| s02 | 00:07.0 | S02 | Đây là Chuột Lang Nước Capybara, loài gặm nhấm lớn nhất thế giới sinh sống tại đầm lầy Nam Mỹ! |  |
| s03 | 00:12.2 | S03 | Thứ nhất, kích thước 65kg cùng lớp da |  |
| s04 | 00:14.7 | S04 | dai và hàm răng cửa sắc như xẻng sắt khiến cá sấu Caiman biết rằng tấn công gã là một canh bạc có thể rách họng chết |  |
| s05 | 00:20.4 | S05 | ngạt. Thứ hai, lưng Capybara là trạm xe buýt di động: |  |
| s06 | 00:23.6 | S06 | chim rỉa bọ ve, rùa sưởi nắng, bầy khỉ đi nhờ qua sông, biến gã thành bộ trưởng ngoại giao hòa bình của muôn loài. |  |
| s07 | 00:29.7 | S07 | Thứ ba, gã là tàu ngầm sinh học có màng bơi, nín thở lặn sâu 5 | **5 PHÚT** · nín thở lặn sâu · R/560 · [0.65, 0.48] |
| s08 | 00:33.5 | S08 | phút và bứt tốc chạy nước rút 35km/h ngang chó săn! | **35 km/h** · chạy ngang chó săn · R/620 · [0.68, 0.55] |
| s09 | 00:37.2 | S09 | Nhưng bí mật gây sốc nhất là vào mỗi sáng sớm, Capybara ăn lại chính phân mềm |  |
| s10 | 00:41.4 | S10 | của mình để hấp thụ trọn vẹn protein lên men! Giữ tâm tĩnh lặng giữa giông bão, |  |
| s11 | 00:45.4 | S11 | đó chính là bí thuật giúp Bố Già Capybara sống sót ung dung giữa bầy sát thủ đầm lầy! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong thế giới ngầm đầm lầy Pantanal Nam Mỹ, nơi cá sấu Caiman rình rập dưới dòng nước đục, trăn khổng lồ Anaconda siết nghẹt bùn lầy, và báo đốm Jaguar rình rập trên cành cây...". Bố cục: Toàn cảnh đầm lầy Pantanal Nam Mỹ bí ẩn và u ám: rặng cây đước rủ rễ, mặt nước đục mờ ảo. BÊN TRÁI một chú chú cá sấu Caiman hoạt hình màu xanh rêu, hàm răng nhọn hoắt lởm chởm, mắt to tròn ngơ ngác đang rình rập thò mắt lên khỏi mặt nước; BÊN PHẢI một con trăn Anaconda khổng lồ đang quấn quanh cành cây ngập nước. KHÔNG có chú Capybara đeo kính râm trong cảnh này.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bạn nghĩ ai mới là kẻ nắm giữ quyền lực tối thượng? Quên hết những bộ nanh vuốt đẫm máu đi!". Bố cục: Bầu trời đầm lầy phủ bóng mây kịch tính: BÊN PHẢI trên cành cây cao, một chú chú báo đốm Jaguar dũng mãnh lông vàng đốm hoa mai đen, nanh vuốt nhọn mắt phát sáng vàng rực, móng vuốt giương ra đầy sát khí như chuẩn bị vồ mồi; các cành cây rung chuyển. KHÔNG có chú Capybara đeo kính râm trong cảnh này.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy mở tập hồ sơ mật mang mã số 15 của Bố Già Đầm Lầy.". Bố cục: Cận cảnh một tập hồ sơ mật bìa da màu nâu cũ kỹ, góc trên có đóng dấu triện sáp đỏ ghi chữ 'HỒ SƠ MẬT BỐ GIÀ ĐẦM LẦY'; bên cạnh là một chiếc kính lúp phóng to vào ảnh thẻ của chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhân vật đứng đầu danh sách theo dõi của chúng ta hôm nay không phải sát thủ săn mồi nào cả, mà là một gã béo ục ịch nặng tới 65kg, mang họ nhà chuột,". Bố cục: Chân dung uy quyền hài hước của chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi: ngồi tựa lưng thư thái trên một ụ đất đầm lầy như ngai vàng, ngâm nửa mình dưới dòng nước mát, hai chân trước chắp lại bụng bự, kính râm đen bóng, vẻ mặt điềm đạm cực hạn.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gia tộc gặm nhấm trên khắp Trái Đất thường bị gắn mác là những kẻ lấm lét trốn chui trốn lủi trong góc bếp.". Bố cục: BÊN TRÁI là góc bếp tối tăm với ba chú chuột nhắt bé tí đang lấm lét ôm mẩu phô mai run rẩy; tương phản hoàn toàn với BÊN PHẢI là ánh hào quang rực rỡ chiếu xuống chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi oai vệ.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng Bố Già Đầm Lầy của chúng ta thì ở một đẳng cấp hoàn toàn khác!". Bố cục: Ở GIỮA là chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi dáng đứng bệ vệ, khoác hờ một chiếc áo choàng trùm phong cách mafia trên vai; hai bên là các loài chim nhỏ đứng xếp hàng cúi chào cung kính.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Với chiều dài cơ thể lên tới 1,3m và chiều cao vai 60cm, gã chính là loài gặm nhấm lớn nhất thế giới còn tồn tại.". Bố cục: Bố cục so sánh kích thước khoa học: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi đứng cạnh một chiếc thước dây khổng lồ đo chiều dài 1,3m từ mũi đến đuôi; và một chiếc cọc đo chiều cao vai đạt đúng 60cm; mắt chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi vẫn lim dim thư thái.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cá thể lập kỷ lục từng được ghi nhận tại Brazil nặng tới 91kg, to ngang một con lợn rừng trưởng thành!". Bố cục: Một chiếc cân bàn lò xo cỡ lớn bằng sắt: BÊN TRÁI chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi đứng trên đĩa cân làm kim đồng hồ chỉ vọt tới 91kg; BÊN PHẢI một chú lợn rừng đực to béo há hốc mồm kinh ngạc so sánh kích thước.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quy tắc thép đầu tiên của gia tộc này khiến mọi nhà sinh vật học phải ngả mũ kinh ngạc: Tuyệt đối không bao giờ hoảng loạn!". Bố cục: Một bức vẽ phong cách thiền định phương Đông: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi ngồi kiết già trên một bông hoa sen khổng lồ nổi trên mặt nước đầm lầy, xung quanh có vòng hào quang vàng ấm áp tỏa ra; chữ 'ZEN' viết tay mờ ảo phía sau.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cho dù trời long đất lở, cho dù lũ quét dâng cao hay một con cá sấu khổng lồ đang bò sát sạt bên hông, gương mặt của Capybara vẫn giữ nguyên một nụ cười mỉm thiền định như thể vừa đắc đạo.". Bố cục: Cảnh tượng hỗn loạn hài hước: bầu trời giông bão sấm chớp đùng đùng, sóng nước dâng cuồn cuộn, một chú chú cá sấu Caiman hoạt hình màu xanh rêu, hàm răng nhọn hoắt lởm chởm, mắt to tròn ngơ ngác to xác đang há hốc mồm bò sát sạt bên cạnh; ở GIỮA chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi vẫn ngồi yên uống tách trà nóng từ tốn.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây không phải là sự dũng cảm bộc phát, mà là đỉnh cao của nghệ thuật ngoại giao đầm lầy!". Bố cục: Bàn hội nghị ngoại giao đầm lầy: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi ngồi ở đầu bàn, hai bên là cá sấu, báo đốm, trăn anaconda và bồ nông đang ngồi nghe giảng giải; chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi giơ một ngón tay lên chỉ bảo đầy phong thái Bố Già.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu bạn gõ từ khóa Capybara trên mạng, bức ảnh kinh điển nhất đập vào mắt chắc chắn là cảnh gã béo này nằm phơi bụng ngủ say sưa, trong khi ngay bên cạnh là 3-4 con cá sấu Caiman răng nhọn hoắt đang nằm phơi nắng.". Bố cục: Bờ cát thoải bên dòng sông đầm lầy: BÊN TRÁI chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi nằm phơi bụng ngửa mặt lên trời ngủ tít mít; BÊN PHẢI là ba đến bốn chú chú cá sấu Caiman hoạt hình màu xanh rêu, hàm răng nhọn hoắt lởm chởm, mắt to tròn ngơ ngác nằm san sát phơi nắng cạnh nhau, mõm cá sấu gần như chạm vào lưng chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cảnh tượng phi lý đến mức người ta tưởng đây là sản phẩm của công nghệ chỉnh sửa ảnh!". Bố cục: Một chiếc màn hình máy tính hoạt hình đang mở phần mềm chỉnh sửa ảnh, con trỏ chuột phóng to vào bức ảnh chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi và cá sấu; một con dấu 'ẢNH THẬT 100%' màu xanh lá đóng xuống góc ảnh.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tại sao một kẻ săn mồi khét tiếng vùng đầm lầy lại bỏ qua một khối thịt 65kg béo múp míp đang nằm ngay trước mũi?". Bố cục: Dưới góc nhìn của chú chú cá sấu Caiman hoạt hình màu xanh rêu, hàm răng nhọn hoắt lởm chởm, mắt to tròn ngơ ngác: nhìn sang chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi béo mập tròn trịa sáu mươi lăm cân; phía trên đầu chú cá sấu Caiman hoạt hình màu xanh rêu, hàm răng nhọn hoắt lởm chởm, mắt to tròn ngơ ngác hiện lên bóng mây suy nghĩ với một dấu hỏi chấm khổng lồ màu đỏ và hình đĩa bít tết bốc khói.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy nghe chính đại diện giới săn mồi lên tiếng giải thích lý do thực tế.". Bố cục: Khung cảnh phỏng vấn truyền hình: Một chiếc micro có logo đài truyền hình đầm lầy chìa vào sát mõm chú chú cá sấu Caiman hoạt hình màu xanh rêu, hàm răng nhọn hoắt lởm chởm, mắt to tròn ngơ ngác; chú cá sấu Caiman hoạt hình màu xanh rêu, hàm răng nhọn hoắt lởm chởm, mắt to tròn ngơ ngác đeo cà vạt hoa văn da sấu, giơ hai tay lên phân trần đầy bối rối.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôi mà đụng vào gã béo này là gãy cả hàm đấy!". Bố cục: Góc quay cận cảnh hài hước: Chú chú cá sấu Caiman hoạt hình màu xanh rêu, hàm răng nhọn hoắt lởm chởm, mắt to tròn ngơ ngác cầm một chiếc hàm răng giả bằng nhựa bị gãy đôi ba chiếc răng nanh, vẻ mặt méo mó đau khổ; phía sau là hình bóng chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi lưng tròn như tảng đá hoa cương.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vừa to vừa nặng, da thì dai nhách, mà còn là trạm cảnh báo động đất của cả khu vực, dại gì nuốt cho nghẹn họng! Đúng như lời gã cá sấu thú nhận!". Bố cục: Hình ảnh tia X-quang hài hước: chú cá sấu Caiman hoạt hình màu xanh rêu, hàm răng nhọn hoắt lởm chởm, mắt to tròn ngơ ngác đang há to mồm cố nuốt một khối thịt hình tròn khổng lồ nhưng bị mắc nghẹn ngang cổ họng, hai mắt lồi ra nghẹt thở; bên cạnh là biểu tượng cảnh báo dấu chéo đỏ.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cá sấu Caiman ở vùng Pantanal thường chỉ dài 1,5m đến 2m, chuyên săn cá và chim nhỏ.". Bố cục: BÊN TRÁI là chú chú cá sấu Caiman hoạt hình màu xanh rêu, hàm răng nhọn hoắt lởm chởm, mắt to tròn ngơ ngác kích thước khiêm tốn dài 1,5m đang há mồm đớp một con cá nhỏ bơi qua; BÊN PHẢI là chiếc thước đo chiều dài 2m thể hiện giới hạn cơ thể của loài cá sấu này.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nuốt một con Bố Già Đầm Lầy trưởng thành là canh bạc nguy hiểm có thể làm chúng rách họng chết ngạt.". Bố cục: Một chiếc cân đong rủi ro: BÊN TRÁI là phần thưởng một bữa ăn; BÊN PHẢI là chiếc xương hàm cá sấu bị nứt gãy và nguy cơ rách thực quản nặng nề nghiêng hẳn cán cân xuống.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa kể, gã béo này sở hữu cặp răng cửa sắc như xẻng sắt, nếu bị dồn vào đường cùng thì một cú cắn tự vệ cũng đủ bẻ gãy xương mõm cá sấu!". Bố cục: Đặc tả hàm răng đáng sợ của chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi há mồm cười khoe cặp răng cửa màu cam dài và sắc lẹm như hai chiếc xẻng sắt sắc bén; phía trước là một khúc gỗ đầm lầy bị cắn nứt đôi ngọt xớt.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa dừng lại ở đó, gã chuột lang nước này còn kiêm luôn chức vụ Giám đốc trạm dịch vụ giao thông công cộng lớn nhất rừng nhiệt đới.". Bố cục: Biển hiệu hoạt hình lớn: 'TRẠM XE BUÝT CÔNG CỘNG PANTANAL'; chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi đội chiếc mũ tài xế xe buýt màu xanh, hai bên sườn vẽ họa tiết xe buýt số 15 chạy tuyến đầm lầy.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lưng của Capybara phẳng lì và rộng thênh thang như chiếc ghế sô-pha di động.". Bố cục: Lưng của chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi biến thành chiếc ghế sô-pha nhung màu xanh êm ái: một chú chim đầm lầy chân dài đang đi dạo trên lưng, nhặt từng con bọ ve nhỏ xíu bỏ vào mồm ngon lành.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chim chóc đầm lầy đậu lên lưng để rỉa bọ ve ký sinh, đàn rùa nước 5-6 con trèo lên mai nằm sưởi ấm, và bầy khỉ sóc thì biến gã thành chiếc phà an toàn qua sông!". Bố cục: Cảnh tượng siêu đông đúc vui nhộn: Trên lưng chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi có đàn rùa nước năm đến sáu con xếp hàng nằm phơi mai; trên đỉnh đầu chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi là chú chú khỉ sóc nhỏ xíu hoạt hình lông vàng, đuôi dài, tinh nghịch nhỏ xíu đang ngồi vẫy tay; chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi lững thững bơi qua sông.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bác bồ nông ơi, mông tôi là thịt chứ không phải con cá đâu, kẹp hoài không chán à?". Bố cục: Cận cảnh tình huống hài hước: Chú chú chim bồ nông hoạt hình mỏ vàng khổng lồ, túi da dưới mỏ xệ xuống mỏ vàng khổng lồ đang há to mồm kẹp trọn mông tròn trịa của chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi; chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi quay đầu lại nhìn với vẻ mặt ngơ ngác tĩnh tâm không thèm phản kháng.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thậm chí cả loài chim bồ nông tham ăn nổi tiếng cũng từng há mỏ kẹp thử vào mông Capybara trong vô vọng, còn gã chuột lang thì chỉ ngoái đầu lại nhìn với vẻ mặt thương hại rồi... ngủ tiếp!". Bố cục: Chú chú chim bồ nông hoạt hình mỏ vàng khổng lồ, túi da dưới mỏ xệ xuống cố hết sức nuốt nhưng chiếc mỏ căng phồng biến dạng thành hình cái mông tròn trịa của chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi, hai mắt bồ nông xoay vòng tròn hoa mắt bất lực.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một mối quan hệ cộng sinh đôi bên cùng có lợi mà giới khoa học gọi là tuyệt tác hòa bình của tự nhiên.". Bố cục: Toàn cảnh bình yên đầm lầy: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi cùng đàn con, rùa, cá sấu và chim chóc cùng quây quần bên bờ nước dưới ánh hoàng hôn ấm áp; biểu tượng hai bàn tay bắt chặt nhau lấp lánh ở GIỮA.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bất kỳ đế chế nào muốn tồn tại lâu dài cũng phải xây dựng một mạng lưới liên lạc bí mật hoàn hảo.". Bố cục: Sơ đồ mạng lưới tình báo thế giới ngầm: Một tấm bản đồ rừng rậm Pantanal có các đường dây nối mạng từ mũi của các Bố Già; các biểu tượng mùi hương lan tỏa khắp các ngóc ngách đầm lầy.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và vũ khí ngoại giao lợi hại nhất của Bố Già Đầm Lầy nằm ngay trên chóp mũi!". Bố cục: Cận cảnh đặc tả chiếc đầu của chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi: một mũi tên vàng rực chỉ thẳng vào đỉnh sống mũi vuông vức; nơi có một khối u nổi gồ lên như viên ngọc đen quyền lực.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu quan sát kỹ một con đực đầu đàn, bạn sẽ thấy một khối u màu đen sẫm, trơn bóng nổi rõ trên sống mũi.". Bố cục: Phóng to kính hiển vi vào khối u trên mũi của chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi: bề mặt da trơn nhẵn, sẫm màu, không có lông; các hạt tinh thể sáp màu trắng lấp lánh đang tiết ra từ lỗ chân lông.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong giới sinh học, khối u quyền lực này được gọi là tuyến Morillo.". Bố cục: Bảng giải phẫu sinh học: Nhãn tên lớn viết chữ 'TUYẾN MORILLO' trên nền thẻ màu đỏ uy quyền; bên cạnh là sơ đồ ống dẫn dịch tiết xạ hương nối thẳng vào tuyến mũi.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyến Morillo liên tục tiết ra một chất dịch sáp màu trắng chứa hỗn hợp xạ hương cực mạnh.". Bố cục: Một chiếc lọ thủy tinh cổ cong đựng dung dịch sáp màu trắng đang bốc hơi xạ hương thơm ngát màu tím; chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi đứng bên cạnh như một nhà pha chế nước hoa cao cấp của đầm lầy.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi khi đi tuần tra qua các gốc sậy hay thân cây gãy, Bố Già chỉ cần quẹt nhẹ chiếc mũi quyền lực của mình lên vỏ cây để ký tên đóng dấu lãnh thổ.". Bố cục: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi cúi đầu cọ nhẹ chiếc mũi có tuyến Morillo vào một thân cây sậy gãy; vết cọ để lại một vệt sáp trắng phát sáng hình con dấu Bố Già 'CAPFATHER SIGNATURE'.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kết hợp với hai túi tuyến mùi hương ở hai bên hậu môn, mỗi cá thể Capybara sở hữu một bản mã hóa sinh học độc nhất vô nhị!". Bố cục: Sơ đồ hai đầu phát tín hiệu: Một mũi tên chỉ vào tuyến mũi Morillo ở đầu; và một mũi tên chỉ vào hai túi tuyến mùi hậu môn ở đuôi; tạo thành hệ thống mã vạch sinh học hai đầu hoàn chỉnh.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ hệ thống chữ ký mùi hương này, các thành viên trong gia tộc chỉ cần hít nhẹ một cái là biết ngay đối phương thuộc phe nào, địa vị xã hội cao hay thấp, thậm chí cả tình trạng sức khỏe hôm nay ra sao mà không cần phí một giọt máu để đấm đá tranh giành thứ bậc!". Bố cục: Hai chú Capybara đối diện nhau: một chú hít nhẹ mũi vào thân cây; phía trên đầu chú hiện lên màn hình thông số HUD hiển thị đầy đủ: 'BỐ GIÀ KHU BẮC - ĐỘI TRƯỞNG - SỨC KHỎE 100%'.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lão sống ở Pantanal 80 năm rồi, chưa thấy chiếc xe buýt nào êm ái và đúng giờ như lưng gã này!". Bố cục: Một chú rùa già đeo kính lão, mai phủ đầy rêu phong cổ kính đang gật gù hài lòng; phía trước là chiếc mai chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi chở rùa điềm đạm rẽ nước qua đầm lầy.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng đỉnh cao nhất trong kho vũ khí của gia tộc này chính là hệ thống điện đàm âm thanh!". Bố cục: Chiếc đài radio vệ tinh đầm lầy: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi đeo tai nghe phi công, các dải sóng âm thanh đủ màu sắc phát ra từ miệng: sóng nhạc êm dịu, sóng huýt sáo và sóng còi báo động.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đôi tai hình bán nguyệt của Capybara có thể xoay 180° độc lập, bắt trọn tiếng chân rón rén của kẻ thù từ khoảng cách hơn 100m.". Bố cục: Cận cảnh đôi tai tròn nhỏ của chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi: tai trái xoay về hướng 90 độ, tai phải xoay về hướng 180 độ độc lập; chiếc radar quét sóng phát hiện bước chân kẻ thù cách xa 100m.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi vui vẻ thư giãn, chúng phát ra tiếng rên hừ hừ như mèo.". Bố cục: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi nằm cuộn tròn trên thảm cỏ, miệng phát ra tiếng rên hừ hừ như mèo con; những nốt nhạc nốt son nốt mi màu hồng bay bổng xung quanh.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi gọi đàn con, chúng huýt sáo lảnh lót như chim sơn ca.". Bố cục: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi chu mỏ huýt sáo vang dội như chú chim hót líu lo; phía sau là đàn bốn chú chuột lang con chân ngắn lon ton chạy ùa lại ríu rít.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng một khi phát hiện bóng dáng sát thủ báo đốm, con đầu đàn sẽ tung ra một cú sủa đanh thép như chó săn chuyên nghiệp!". Bố cục: Ánh mắt chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi đột ngột sắc lẹm: Phía xa trong bụi rậm lộ ra đôi mắt vằn vện của chú chú báo đốm Jaguar dũng mãnh lông vàng đốm hoa mai đen, nanh vuốt nhọn; chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi đứng thẳng người chuẩn bị phát tín hiệu cảnh báo tối cao.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cú sủa báo động này có tần số đặc biệt làm chấn động cả đầm lầy, khiến từ bầy khỉ trên ngọn cây đến lũ hươu bờ sông đều lập tức nhảy dựng lên bỏ chạy thoát thân trong gang tấc!". Bố cục: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi há to mồm tung cú sủa 'GÂU! GÂU!' chấn động: luồng sóng âm màu đỏ bùng nổ như loa phát thanh; đàn khỉ trên cây nhảy dựng bắn người lên cành cao, đàn hươu lao thục mạng.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nào, bây giờ là lúc chúng ta phải lật mở trang hồ sơ đen tối và nhạy cảm nhất của Bố Già Đầm Lầy.". Bố cục: Khung cảnh phòng thẩm vấn bí mật: Một chiếc bàn gỗ với một chiếc đèn chụp chiếu thẳng xuống một phong bì màu đen niêm phong dấu đỏ 'TUYỆT MẬT - GÓC KHUẤT BỐ GIÀ'.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu bạn đang ăn sáng hay vừa nhâm nhi cốc trà sữa, tôi chân thành khuyên bạn hãy tạm đặt cốc xuống trong hai phút tới!". Bố cục: BÊN TRÁI một khán giả hoạt hình đang cầm cốc trà sữa bỗng sững sờ dừng lại, mắt trợn tròn; BÊN PHẢI một biển báo cảnh báo hài hước hình nĩa và thìa bị gạch chéo đỏ.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bởi vì món ăn khoái khẩu giúp gã béo này duy trì thân hình hộ pháp 65kg...". Bố cục: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi thân hình hộ pháp béo tròn sáu mươi lăm cân đang đứng cạnh một chiếc đĩa bạc sang trọng có nắp đậy kiểu nhà hàng năm sao; nắp đậy bắt đầu rung rinh hé mở.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chính là sản phẩm do chính gã vừa thải ra! Khoan vội bịt mũi phán xét!". Bố cục: Chiếc nắp đĩa bạc mở tung: bên trong là những viên phân màu xanh lục mềm mại bốc khói nhẹ; chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi đeo khăn ăn ở cổ, cầm dao nĩa sẵn sàng thưởng thức với vẻ mặt thỏa mãn.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dưới góc nhìn của khoa học dinh dưỡng, đây là một tuyệt tác tiến hóa sinh tồn bậc thầy mang tên Cecotrophy, hay tập tính ăn phân có chọn lọc!". Bố cục: Một cuốn bách khoa toàn thư sinh học mở toang trang sách có hình vẽ danh xưng khoa học 'CECOTROPHY - TẬP TÍNH ĂN PHÂN CÓ CHỌN LỌC' cùng huy chương vàng tiến hóa.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khẩu phần ăn của Capybara chiếm tới 75% là cỏ đầm lầy và thực vật thủy sinh thô ráp.". Bố cục: Biểu đồ tròn dinh dưỡng: Bảy mươi lăm phần trăm chiếc đĩa là bó cỏ đầm lầy và rong rêu thô ráp; hai mươi lăm phần trăm còn lại là vỏ cây khô; chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi nhai cỏ cật lực như máy cắt cỏ.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cỏ nghèo dinh dưỡng đến mức chất xơ xen-lu-lô-zơ gần như không thể bị phân hủy bởi dạ dày thông thường.". Bố cục: Cận cảnh phân tử sợi xen-lu-lô-zơ cứng như những thanh thép đan lưới; dịch axit dạ dày thông thường dội vào đều bị bật ngược trở ra bất lực.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để giải quyết bài toán hóc búa này, tạo hóa trang bị cho Capybara một chiếc ruột tịt khổng lồ chứa hàng tỷ vi khuẩn lên men đặc chủng.". Bố cục: Hình ảnh giải phẫu bộ máy tiêu hóa của chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi: Một chiếc ruột tịt khổng lồ màu hồng như nhà máy lên men hóa chất; bên trong hàng triệu chú vi khuẩn hoạt hình tí hon đeo kính bảo hộ đang cầm búa đập vỡ sợi cỏ.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cứ vào khoảng từ 06:00 sáng đến 08:00 sáng mỗi ngày, sau một đêm dài vi khuẩn cật lực làm việc, cơ thể gã sẽ thải ra một loại phân mềm đặc biệt màu xanh lục gọi là phân manh tràng.". Bố cục: Một chiếc đồng hồ báo thức chỉ đúng khung giờ từ 06:00 sáng đến 08:00 sáng; ánh ban mai rọi xuống chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi vừa thức giấc sau giấc ngủ đêm dài.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Loại phân này chứa hàm lượng protein gấp đôi phân thường và ngập tràn vitamin nhóm B!". Bố cục: Ống nghiệm phân tích mẫu phân mềm manh tràng: cột đo chỉ số protein vọt lên gấp đôi so với mẫu phân thường; các viên vitamin B1, B12 màu vàng lấp lánh bay quanh ống nghiệm.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thay vì lãng phí nguồn tài nguyên quý giá trôi theo dòng nước, Bố Già lập tức cúi xuống ăn lại toàn bộ chỗ phân mềm này để hệ tiêu hóa hấp thụ dưỡng chất lần thứ hai!". Bố cục: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi cúi đầu xuống gặm lại món phân mềm giàu dưỡng chất vừa thải ra trên thảm cỏ ướt sương; biểu tượng tái chế mũi tên xanh xoay vòng tròn ba cạnh hoàn hảo.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngay từ khi mới được 2 tuần tuổi, những chú chuột lang nước con đã bắt đầu học tập thói quen này từ mẹ để cấy hệ vi sinh đường ruột quý giá vào cơ thể.". Bố cục: Chú Capybara con bé xíu mới hai tuần tuổi đứng cạnh mẹ, lon ton bắt chước mẹ cúi xuống ăn phân mềm để đón nhận vi khuẩn đường ruột quý giá; mẹ mỉm cười xoa đầu con.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phải đến buổi chiều, sau khi đã bòn rút sạch sẽ đến phân tử protein cuối cùng, gã mới thải ra những viên phân khô cứng hình bầu dục không còn giá trị dinh dưỡng.". Bố cục: Bầu trời chuyển sang ánh hoàng hôn tím: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi thải ra những viên phân hình bầu dục màu nâu sẫm, khô cứng như hạt ô-liu; chiếc máy đo dinh dưỡng quét qua báo '0% PROTEIN'.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kỳ dị, khó ngửi, nhưng chính món súp vi khuẩn tái chế này đã nuôi sống cả đế chế gặm nhấm suốt hàng triệu năm qua!". Bố cục: Cả bầy Capybara mập mạp béo tốt đứng vững chãi trên bờ đầm lầy qua hàng triệu năm lịch sử; bên cạnh là một bát súp vi khuẩn vàng óng tượng trưng cho nguồn năng lượng sinh tồn.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đừng bao giờ để dáng vẻ chậm chạp ung dung của Bố Già đánh lừa thị giác! Trong thế giới giang hồ, kẻ sống sót lâu nhất không phải kẻ to mồm nhất, mà là kẻ sở hữu lối thoát hiểm tinh quái nhất.". Bố cục: Bờ đầm lầy căng thẳng: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi đang thong thả ăn cỏ thì từ bụi rậm phía sau, đôi mắt vàng rực của chú chú báo đốm Jaguar dũng mãnh lông vàng đốm hoa mai đen, nanh vuốt nhọn nhô ra; tiếng còi báo động khẩn cấp màu đỏ chớp nháy liên hồi.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cả bầy trật tự! Báo đốm Jaguar hướng hai giờ, lặn ngầm rút lui hết cho tôi! Tuyệt chiêu số một: Chế độ tàu ngầm quân sự!". Bố cục: Một cô Capybara mẹ đầu đàn đeo nơ hoa trên đầu, hai chân trước giơ cờ hiệu chỉ huy; cả đàn chuột con lập tức nối đuôi nhau nhảy ào xuống dòng nước đục.
```
</details>

<details><summary>L62</summary>

```text
HÌNH L62 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bạn có nhận thấy mắt, mũi và tai của Capybara đều nằm thẳng hàng trên một mặt phẳng ở đỉnh đầu không?". Bố cục: Bản vẽ giải phẫu kỹ thuật quân sự: Ba đường gióng màu vàng nối thẳng tắp từ Mắt qua Mũi đến Tai trên đỉnh đầu chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi; mặt nước ngang đúng đường gióng này như kính tiềm vọng tàu ngầm.
```
</details>

<details><summary>L63</summary>

```text
HÌNH L63 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thiết kế giải phẫu này giống hệt loài hà mã và cá sấu!". Bố cục: Bố cục so sánh ba loài thủy quái đầm lầy: BÊN TRÁI là đầu Hà Mã, Ở GIỮA là đầu chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi, BÊN PHẢI là đầu Cá Sấu; cả ba đều có mắt mũi tai thẳng hàng trên đỉnh đầu giống hệt nhau.
```
</details>

<details><summary>L64</summary>

```text
HÌNH L64 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi ngâm mình dưới nước, toàn bộ thân xác hộ pháp 65kg chìm nghỉm dưới dòng nước đục, chỉ để lộ ba giác quan nhô lên mặt nước để thở và nghe ngóng mà không để lại một gợn sóng!". Bố cục: Góc nhìn cắt ngang dưới nước: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi trôi bồng bềnh dưới lòng sông đục như một chiếc tàu ngầm hạt nhân màu nâu; bên trên mặt nước chú chú báo đốm Jaguar dũng mãnh lông vàng đốm hoa mai đen, nanh vuốt nhọn ngơ ngác nhìn quanh không thấy bóng dáng con mồi đâu.
```
</details>

<details><summary>L65</summary>

```text
HÌNH L65 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bàn chân của Capybara có 4 ngón ở chân trước và 3 ngón ở chân sau, tất cả đều được nối liền bởi lớp màng bơi tự nhiên.". Bố cục: Phóng to bàn chân đặc biệt của chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi: chân trước có bốn ngón xòe rộng, chân sau có ba ngón; giữa các kẽ ngón chân là lớp màng bơi mỏng dai như chân vịt; chiếc móng vuốt ngắn bám chắc vào bùn.
```
</details>

<details><summary>L66</summary>

```text
HÌNH L66 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dưới nước, gã có thể nín thở lặn sâu hoàn toàn suốt 5 phút đồng hồ, luồn lách qua các thảm cỏ ngầm để thoát khỏi tầm mắt kẻ săn mồi!". Bố cục: Cảnh lặn ngầm sâu dưới đáy sông: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi khép chặt tai và lỗ mũi lại, bơi lướt êm ái giữa rừng rong rêu thủy sinh; một chiếc đồng hồ bấm giờ đếm ngược 5 phút đặt ở góc phải.
```
</details>

<details><summary>L67</summary>

```text
HÌNH L67 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn nếu bị dồn lên bờ cạn thì sao?". Bố cục: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi đang đứng trên bờ bãi cỏ khô, phía sau là bờ vực cát; chú chú báo đốm Jaguar dũng mãnh lông vàng đốm hoa mai đen, nanh vuốt nhọn từ từ tiến lại gần với vẻ mặt đắc thắng tưởng chừng đã bắt gọn được con mồi chậm chạp.
```
</details>

<details><summary>L68</summary>

```text
HÌNH L68 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy chuẩn bị tinh thần cho cú sốc tiếp theo: Gã béo ục ịch này có thể bứt tốc chạy nước rút với vận tốc lên tới 35km/h!". Bố cục: Khoảnh khắc bứt tốc không tưởng: Bốn chân chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi đạp mạnh tung tóe bùn đất, cơ thể béo tròn biến thành một viên đạn đại bác màu nâu lao vút đi với tốc độ 35 km/h, bụi mù mịt bốc lên phía sau.
```
</details>

<details><summary>L69</summary>

```text
HÌNH L69 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tốc độ xé gió ngang ngửa một con chó săn chuyên nghiệp, đủ sức bỏ xa hầu hết các loài thú săn mồi trong cự ly ngắn trước khi phóng thẳng xuống nước tẩu thoát!". Bố cục: Cuộc đua tốc độ trên thảo nguyên: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi chạy song song vượt mặt một chú chó săn đang thở hồng hộc; máy đo tốc độ bắn tia laser xác nhận bỏ xa kẻ săn mồi.
```
</details>

<details><summary>L70</summary>

```text
HÌNH L70 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sự kỳ diệu của Capybara lớn đến mức từng tạo nên một trong những vụ nhầm lẫn hài hước nhất lịch sử tôn giáo thế giới! Vào thế kỷ 16, khi các nhà truyền giáo Tây Ban Nha đến vùng đầm lầy Venezuela, họ nhìn thấy loài thú này suốt ngày bơi lội dưới nước, chân lại có màng như vịt.". Bố cục: Khung cảnh lịch sử thế kỷ 16: Một chiếc thuyền buồm Tây Ban Nha cập bến bờ đầm lầy Venezuela; các nhà truyền giáo mặc áo choàng nâu đang kinh ngạc chỉ tay vào đàn chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi bơi lội dưới nước.
```
</details>

<details><summary>L71</summary>

```text
HÌNH L71 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thế là họ gửi thư về Tòa thánh Vatican để xin phép...". Bố cục: Một lá thư cổ viết tay bằng mực lông ngỗng có gắn con dấu sáp đỏ gửi qua đường biển về tòa thánh Vatican ở Rome; bức thư vẽ hình chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi có thêm chiếc đuôi cá ngộ nghĩnh.
```
</details>

<details><summary>L72</summary>

```text
HÌNH L72 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "được xếp Capybara vào loài cá, để giáo dân có thể ăn thịt trong Mùa Chay kiêng khem!". Bố cục: Bàn tiệc Mùa Chay của các giáo sĩ: Giữa bàn là một chiếc đĩa lớn bày món thịt nướng; một tấm biển ghi 'THỰC ĐƠN MÙA CHAY: CÁ ĐẦM LẦY' với hình chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi bơi lội kế bên.
```
</details>

<details><summary>L73</summary>

```text
HÌNH L73 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và thật khó tin, các giám mục thời bấy giờ đã chính thức gật đầu phê chuẩn sắc lệnh coi một con thú gặm nhấm 65kg có bốn chân và bộ lông xơ cứng là... một loài thủy sản!". Bố cục: Tòa thánh Vatican trang nghiêm: Các giám mục mặc áo choàng đỏ đang đồng loạt đặt bút ký tên và đóng dấu triện vàng lên sắc lệnh công nhận chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi sáu mươi lăm cân chính thức là loài cá.
```
</details>

<details><summary>L74</summary>

```text
HÌNH L74 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một cú lừa tiến hóa vĩ đại mà chính Bố Già Đầm Lầy cũng chẳng thể ngờ tới.". Bố cục: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi đang đội một chiếc vương miện hình con cá nhỏ trên đầu, đeo kính râm cười toe toét; phía sau là tấm bảng phả hệ động vật có vú bị sửa thành bộ Cá.
```
</details>

<details><summary>L75</summary>

```text
HÌNH L75 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trải qua hàng triệu năm thăng trầm, triết lý sinh tồn mà loài Capybara để lại cho chúng ta thật sâu sắc: Trong một thế giới đầy rẫy hiểm nguy và áp lực,". Bố cục: Bức tranh nghệ thuật hoàng hôn tuyệt đẹp trên đầm lầy: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi ngồi thảnh thơi bên bờ nước tĩnh lặng như gương, chim chóc bay lượn, gió lay rặng lau sậy; ánh sáng vàng cam chiếu rọi bình yên.
```
</details>

<details><summary>L76</summary>

```text
HÌNH L76 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bạn ấn tượng nhất với điều gì ở Bố Già Đầm Lầy Capybara: Khả năng biến cá sấu thành bạn thân, hay bữa sáng tái chế có 1-0-2? Hãy để lại bình luận bên dưới nhé!". Bố cục: Khung hình tương tác hai lựa chọn vui nhộn: BÊN TRÁI là biểu tượng bắt tay làm bạn với cá sấu; BÊN PHẢI là biểu tượng chiếc đĩa ăn phân tái chế protein; chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi ở GIỮA chỉ tay mời khán giả bình luận.
```
</details>

<details><summary>L78</summary>

```text
HÌNH L78 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và bây giờ, hãy hướng ngòi bút về phân cảnh kết thúc bí ẩn!". Bố cục: Bàn vẽ hoạt hình chuyển sang tông màu xanh thẳm của đáy đại dương sâu; ánh sáng đèn pin quét qua mặt giấy trắng hé lộ một bí mật mới sắp bắt đầu.
```
</details>

<details><summary>L79</summary>

```text
HÌNH L79 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong tập tiếp theo, chúng ta sẽ lặn xuống đáy đại dương sâu thẳm để diện kiến một bóng đen tí hon vô cùng nguy hiểm.". Bố cục: Khung cảnh đáy biển sâu thẳm đầy bí ẩn: San hô và đá ngầm mờ ảo; ở GIỮA là BÓNG ĐEN HOÀN TOÀN (solid black silhouette) của một sinh vật nhỏ bé có một chiếc càng khổng lồ bất cân xứng, viền hào quang phát sáng cyan.
```
</details>

<details><summary>L80</summary>

```text
HÌNH L80 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một sinh vật nhỏ bé dài chưa đầy 5cm, nhưng sở hữu chiếc càng quái đản có thể búng ra âm thanh kinh hoàng lên tới 218 dB, to hơn cả tiếng súng trường và làm nhiễu loạn cả hệ thống sóng siêu âm của tàu ngầm quân sự!". Bố cục: Đặc tả chiếc càng bóng đen bí ẩn: một chiếc càng lớn gấp đôi thân mình đang mở hé; bên cạnh là chiếc thước đo 5cm và đồng hồ đo âm thanh vọt lên mức 218 dB đỏ rực.
```
</details>

<details><summary>L81</summary>

```text
HÌNH L81 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cú búng càng tạo ra luồng nhiệt độ hàng ngàn độ C xé toạc mặt nước, làm con mồi chết đứng từ xa mà không cần chạm vào người!". Bố cục: Vụ nổ sóng xung kích dưới biển: Cú búng càng tạo ra một bọt khí phát sáng rực rỡ như tia chớp nhỏ, sóng xung kích tỏa ra làm một chú cá bơi gần choáng váng; phía xa một chiếc tàu ngầm quân sự bị nhiễu sóng sonar.
```
</details>

<details><summary>L82</summary>

```text
HÌNH L82 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đố bạn biết danh tính của sát thủ vũ khí âm thanh tí hon này là ai? Hãy đoán tên con vật bên dưới phần bình luận nhé!". Bố cục: BÓNG ĐEN BÍ ẨN (solid black silhouette) của sát thủ tí hon nổi bật ở GIỮA, phía trên đầu là một DẤU HỎI CHẤM LỚN MÀU VÀNG óng ánh; dòng chữ 'ĐOÁN TÊN CON VẬT TẬP 16' phát sáng lung linh.
```
</details>

<details><summary>L83</summary>

```text
HÌNH L83 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "suốt ngày ngâm mình trong nước với vẻ mặt đơ toàn tập không hề biến sắc: Chuột Lang Nước, hay còn gọi bằng danh xưng giang hồ quốc tế là Capybara!". Bố cục: Cận cảnh chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi mập mạp béo tròn đang ngâm mình thư thái trong làn nước đầm lầy mát rượi, chiếc mũi nhô lên với cặp kính râm đen nhỏ bóng loáng, mặt đơ toàn tập không hề biến sắc.
```
</details>

<details><summary>L84</summary>

```text
HÌNH L84 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một khi sát thủ đỉnh chóp Báo Đốm Jaguar xuất hiện với cặp móng vuốt chết chóc, Capybara lập tức kích hoạt chế độ đào tẩu cấp độ đỏ!". Bố cục: Một chú chú báo đốm Jaguar dũng mãnh lông vàng đốm hoa mai đen, nanh vuốt nhọn mắt sáng rực giương cặp móng vuốt vồ xuống từ cành cây; chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi ở GIỮA bật chế độ báo động khẩn cấp màu đỏ, bụi nước bắn tung tóe chuẩn bị lặn ngầm.
```
</details>

<details><summary>L85</summary>

```text
HÌNH L85 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "kẻ chiến thắng sau cùng không phải kẻ cố gồng mình lên thị uy nanh vuốt, mà là kẻ biết giữ cho tâm trí mình luôn phẳng lặng như mặt nước hồ thu, hòa hợp với mọi loài xung quanh để biến kẻ thù thành bạn đồng hành.". Bố cục: Bức tranh triết lý thiền định: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi ngồi tĩnh tâm như tượng Phật giữa đầm lầy, mặt nước xung quanh phẳng lặng như gương; phản chiếu bầu trời xanh và mây trắng yên bình.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Tại sao một gã chuột béo nặng 65kg lại có thể ngồi uống trà cạnh đàn cá sấu săn mồi mà không mất một cọng lông?". Bố cục: Bờ đầm lầy Nam Mỹ: chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ ngồi uống tách trà đá thư thái bên cạnh một chú chú cá sấu Caiman hoạt hình màu xanh rêu, hàm răng nhọn hoắt lởm chởm, mắt to tròn ngơ ngác to xác đang há mồm phơi nắng, hai bên hòa bình như đôi bạn thân lâu năm.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đây là Chuột Lang Nước Capybara, loài gặm nhấm lớn nhất thế giới sinh sống tại đầm lầy Nam Mỹ!". Bố cục: chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ đứng bệ vệ trên bãi cỏ đầm lầy, đeo kính râm đen nhỏ sành điệu; chiếc thước đo ghi nhận danh hiệu 'LOÀI GẶM NHẤM LỚN NHẤT THẾ GIỚI'.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Thứ nhất, kích thước 65kg cùng lớp da dai". Bố cục: Góc quay cận cảnh: chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ to béo hộ pháp 65kg với lớp da dày dai nhách như áo giáp; chú chú cá sấu Caiman hoạt hình màu xanh rêu, hàm răng nhọn hoắt lởm chởm, mắt to tròn ngơ ngác bên cạnh cắn thử vào không khí rồi lắc đầu ngao ngán.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "và hàm răng cửa sắc như xẻng sắt khiến cá sấu Caiman biết rằng tấn công gã là một canh bạc có thể rách họng chết ngạt.". Bố cục: Cận cảnh hàm răng sắc bén của chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ: Cặp răng cửa màu cam dài như hai lưỡi xẻng sắt sắc lẹm, cắn đứt đôi cành cây; chú chú cá sấu Caiman hoạt hình màu xanh rêu, hàm răng nhọn hoắt lởm chởm, mắt to tròn ngơ ngác toát mồ hôi hột lùi lại.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Thứ hai, lưng Capybara là trạm xe buýt di động:". Bố cục: Lưng chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ phẳng lì rộng thênh thang như chiếc ghế sô-pha di động giữa đầm lầy; chim chóc đậu lên rỉa bọ ve.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "chim rỉa bọ ve, rùa sưởi nắng, bầy khỉ đi nhờ qua sông, biến gã thành bộ trưởng ngoại giao hòa bình của muôn loài.". Bố cục: Cảnh tượng trạm xe buýt đông vui: một chú rùa ngồi phơi mai trên lưng chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ, chú khỉ con bám vào cổ vẫy tay đi nhờ qua sông; chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ ung dung rẽ sóng.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Thứ ba, gã là tàu ngầm sinh học có màng bơi, nín thở lặn sâu 5 phút". Bố cục: chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ lặn chìm dưới dòng nước đục như chiếc tàu ngầm quân sự, chỉ thò đúng mắt, mũi và tai thẳng hàng trên mặt nước; đồng hồ đếm ngược 5 phút lặn sâu.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "và bứt tốc chạy nước rút 35km/h ngang chó săn!". Bố cục: chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ bứt tốc chạy nước rút xé gió trên đồng cỏ với tốc độ 35 km/h, phóng vượt mặt một chú chó săn đang thở dốc; bụi đất tung mù mịt.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Nhưng bí mật gây sốc nhất là vào mỗi sáng sớm, Capybara ăn lại chính phân mềm của mình". Bố cục: Chiếc đồng hồ điểm đúng 06:00 sáng: chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ cúi xuống ăn lại chỗ phân mềm xanh lục giàu protein vừa thải ra; một đĩa thức ăn tái chế có huy hiệu dinh dưỡng.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "để hấp thụ trọn vẹn protein lên men! Giữ tâm tĩnh lặng giữa giông bão,". Bố cục: Sơ đồ dinh dưỡng hoạt hình: Viên phân mềm manh tràng tan thành các hạt protein và vitamin B màu vàng kim hấp thụ ngược trở lại vào cơ thể chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ béo khỏe.
```
</details>

<details><summary>S11</summary>

```text
HÌNH S11 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "đó chính là bí thuật giúp Bố Già Capybara sống sót ung dung giữa bầy sát thủ đầm lầy!". Bố cục: Khung cảnh kết thúc bình yên trọn vẹn: chú chuột lang nước Capybara mập mạp lông nâu, đeo kính râm đen nhỏ ngồi thiền thư thái trên thảm hoa sen nở giữa hồ nước hoàng hôn tuyệt đẹp, xung quanh là muông thú và cá sấu cùng nằm quây quần hòa bình.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/80 của video YouTube về Chuột Lang Nước (Capybara)). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi. Nhân vật phụ cố định: chú cá sấu Caiman hoạt hình màu xanh rêu, hàm răng nhọn hoắt lởm chởm, mắt to tròn ngơ ngác; chú khỉ sóc nhỏ xíu hoạt hình lông vàng, đuôi dài, tinh nghịch; chú chim bồ nông hoạt hình mỏ vàng khổng lồ, túi da dưới mỏ xệ xuống; chú báo đốm Jaguar dũng mãnh lông vàng đốm hoa mai đen, nanh vuốt nhọn. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/11 của video YouTube Shorts về Chuột Lang Nước (Capybara)). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú chuột lang nước Capybara hoạt hình mập mạp béo tròn, bộ lông nâu vàng xơ mượt, mõm vuông vắn đặc trưng, mắt híp lim dim thư thái tĩnh tâm không cảm xúc, tai tròn nhỏ vểnh nhẹ, đeo một chiếc kính râm đen nhỏ sành điệu trên sống mũi. Nhân vật phụ: chú cá sấu Caiman hoạt hình màu xanh rêu, hàm răng nhọn hoắt lởm chởm, mắt to tròn ngơ ngác; chú chim bồ nông hoạt hình mỏ vàng khổng lồ, túi da dưới mỏ xệ xuống. 
```
</details>

## 7. SEO

- **title:** Bố Già 65kg Khiến Cá Sấu Phải Nể & Bữa Sáng Ăn Lại... Phân?! | Capybara | Tập 15
- **hook_paragraph:** Chuột Lang Nước (Capybara) nặng tới 65kg sở hữu vẻ mặt điềm đạm khiến cả cá sấu Caiman cũng phải nằm cạnh phơi nắng, chân có màng bơi nín thở lặn 5 phút, chạy nước rút 35km/h nhưng lại có bí mật đen tối ăn lại phân sáng sớm để hấp thụ protein! Khám phá hồ sơ đế chế đầm lầy của Bố Già Nam Mỹ.
- **question:** Bạn nể phục khả năng ngoại giao làm bạn với cá sấu hay cú sốc bữa sáng tái chế của Bố Già Capybara hơn? Đoán xem bóng đen tập sau là loài nào nhé!
- **next_teaser:** sát thủ đại dương búng càng nổ 218 dB làm điếc sóng sonar tàu ngầm
- **shorts_title:** Tại Sao Cá Sấu Cũng Phải Nể Sợ Bố Già 65kg Này?! 🐾 #shorts #capybara
- **shorts_desc:** Chuột Lang Nước Capybara nặng 65kg là gã béo điềm tĩnh nhất đầm lầy Nam Mỹ: cá sấu nằm cạnh, bầy khỉ cưỡi lưng, lặn 5 phút và chạy 35km/h! Khám phá bí mật Bố Già đầm lầy.
- **bullets:** Tại sao cá sấu Caiman và muông thú đều thích nằm cạnh Capybara? · Vũ khí ngoại giao: Khối u Morillo trên mũi và tiếng sủa báo động đầm lầy · Bí mật đen tối: Tập tính ăn phân Cecotrophy sáng sớm để hấp thụ protein · Tàu ngầm sinh học: Chân màng bơi, lặn 5 phút và chạy nước rút 35km/h · Cú lừa lịch sử: Giáo hội Vatican thế kỷ 16 từng công nhận Capybara là... cá! · Bật mí bóng đen bí ẩn tập tiếp theo: Sát thủ vũ khí âm thanh 218 dB
- **tags:** chuột lang nước, chuot lang nuoc, capybara, capybara và cá sấu, tại sao capybara thân thiện, bố già đầm lầy, bộ trưởng ngoại giao đầm lầy, capybara ăn phân, cecotrophy, tuyến morillo, động vật hài hước, thế giới động vật, vẽ chuyện hoang dã, whiteboard animation việt nam, vatican coi capybara là cá
- **hashtags:** #Capybara #ChuotLangNuoc #TheGioiDongVat #VeChuyenHoangDa #WhiteboardAnimation

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-15-capybara
python src/episode/pipeline.py tts    projects/tap-15-capybara     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-15-capybara     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-15-capybara     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-15-capybara              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-15-capybara --force
python scripts/beat_sheet.py projects/tap-15-capybara               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-15-capybara/audio/shorts.wav projects/tap-15-capybara/renders/tap-15-capybara_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-15-capybara
python src/episode/pipeline.py seo    projects/tap-15-capybara
python src/episode/episode_doc.py     projects/tap-15-capybara
```

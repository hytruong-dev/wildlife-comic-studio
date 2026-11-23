# TẬP ĐẶC BIỆT ĐẠI HỘI SINH TỒN #3 (SAU 10 TẬP TIẾP THEO: TẬP 21-30) — 10 QUÁI KIỆT — ĐẠI HỘI SINH TỒN MÙA 3 · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`mega-03-dai-hoi-sinh-ton`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/mega-03-dai-hoi-sinh-ton`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F_SPECIAL` · **Persona giọng:** `giai_dau` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | 10 quái kiệt — Đại Hội Sinh Tồn Mùa 3 |
| Tiêu đề YouTube | [TẬP ĐẶC BIỆT] 10 Quái Kiệt Dị Nhân Phá Vỡ Mọi Định Luật Sinh Học: Ai Lên Ngôi Vô Địch?! |
| Video dài | `renders/mega-03-dai-hoi-sinh-ton_long.mp4` — 60:01.0 (3601.0s) |
| Shorts | `renders/mega-03-dai-hoi-sinh-ton_shorts.mp4` — 0:54.5 (54.5s) |
| Thumbnail | `renders/mega-03-dai-hoi-sinh-ton_thumbnail.jpg` |
| Số hình | dài 502 beat / 502 ảnh riêng; Shorts 12 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 60:00.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/502 của video YouTube về 10 quái kiệt — Đại Hội Sinh Tồn Mùa 3). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: anh MC dẫn chương trình hoạt hình vui tính: tóc vuốt dựng, mặc bộ vest đỏ tươi, thắt nơ bướm vàng, cầm chiếc micro vàng, nụ cười rộng. Nhân vật phụ cố định: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — 10 QUÁI KIỆT DỊ NHÂN BƯỚC VÀO ĐẤU TRƯỜNG
*Thẻ chương:* ĐẤU TRƯỜNG DỊ NHÂN MÙA 3

*Badge:* `KHAI MẠC MÙA 3` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene01_p0.wav` (776 ký tự) · mood `tram_bi_an`

```text
Màn đêm buông xuống một đấu trường cổ kính được bao quanh bởi những rạn san hô phát quang và rừng rậm nguyên sinh bí ẩn... Ở chính giữa sàn đấu, một chiếc vương miện hoàng gia nạm ngọc phát ra ánh sáng lung linh kỳ ảo, chờ đợi chủ nhân mới của Mùa ba. Đêm nay, mười sinh vật dị thường nhất từ Tập hai mươi mốt đến Tập ba mươi của kênh Vẽ Chuyện Hoang Dã sẽ chính thức hội ngộ! Họ không đến để nhắc lại những câu chuyện cũ, mà để đọ sức trực tiếp bằng hàng loạt bí mật sinh học chấn động thế giới! Mỗi loài mang theo một siêu năng lực quái dị dường như bước ra từ những trang truyện tranh siêu anh hùng viễn tưởng. Từ khả năng mọc lại cả não bộ và trái tim không tì vết, tấm khiên mông bọc thép dập nát sọ kẻ thù, cho tới bộ gen đảo ngược dòng thời gian để trường sinh bất lão!
```
**Part 1** → `audio/vs/scene01_p1.wav` (908 ký tự) · mood `hao_hung`

```text
[surprise-oh] Bật toàn bộ hệ thống đèn pha! Chào mừng toàn thể muôn loài đã đến với Đại Hội Sinh Tồn Mùa ba: Đấu Trường Dị Nhân! Tôi là người dẫn chương trình đêm nay, và tôi xin cam kết danh dự: những phát hiện khoa học bạn sắp nghe đều mới toanh một trăm phần trăm! Từ việc tơ nhớt Cá Mút Đá dai hơn áo giáp chống đạn, Kỳ Nhông Axolotl mang bộ gen ba mươi hai tỷ cặp base chống ung thư, cho đến Sứa Bất Tử tự đảo ngược thời gian tế bào! [laughter] Đại hội không tổ chức chỉ để so kè nắm đấm, mà là nơi tôn vinh những kỳ tích thích nghi đỉnh cao mà mẹ thiên nhiên đã dày công kiến tạo suốt hàng trăm triệu năm qua! Luật thi đấu Mùa ba cực kỳ cam go: tám vòng đấu chính thức, xen kẽ giờ giải lao hậu trường, trao giải phụ và vòng phúc khảo tin đồn thế kỷ. Mỗi vòng thi, ban giám khảo sẽ trao ba tấm huy chương: Vàng được ba điểm, Bạc hai điểm, và Đồng một điểm. Riêng Vòng Chung Kết sẽ được nhân đôi điểm số!
```
**Part 2** → `audio/vs/scene01_p2.wav` (560 ký tự) · mood `hao_hung`

```text
Khắp các khán đài, muông thú từ khắp năm châu bốn biển đang giương cao những biểu ngữ cổ vũ vô cùng huyên náo và hài hước! Đội cổ động viên rái cá biển vừa gõ sò vừa reo hò, trong khi các bạn chồn Gulo ngồi ở hàng ghế danh dự chăm chú theo dõi từng động thái của mười dị nhân! Hải Ly thậm chí còn ngứa răng cắn nhẹ vào chân chiếc bàn ban tổ chức làm bà Cú giám khảo phải vội vàng lấy thước gõ can ngăn! [laughter] Còn anh chàng Wombat thì tranh thủ tựa chiếc mông bọc thép ba xăng-ti-mét vào cây cột thép chịu lực để ngủ gật một giấc ngắn trước giờ khai chiến!
```
**Part 3** → `audio/vs/scene01_p3.wav` (155 ký tự) · 🎭 cameo `tham_phan`

```text
Giám khảo xin nhắc nhở nghiêm túc: nghiêm cấm phóng ruột vào mặt đối thủ, cấm xả nhớt làm trơn sàn thi đấu và cấm nổ bụng lung tung trong khu vực khán đài!
```
**Part 4** → `audio/vs/scene01_p4.wav` (231 ký tự) · mood `hao_hung`

```text
Các tuyển thủ đã nghe rõ chưa? Nhất là anh chàng Hải Sâm và bạn Kiến Nổ đang lén lút nhìn quanh đằng kia! [laughter] Và bây giờ, xin mời toàn thể khán đài cùng đứng dậy nhiệt liệt hoan nghênh mười quái kiệt bước ra thảm đỏ danh dự!
```
**Part 5** → `audio/vs/scene01_p5.wav` (639 ký tự) · mood `don_dap`

```text
Tuyển thủ số một! Chiến binh móng vuốt Tây Phi tự bẻ xương ngón chân xuyên thủng da chân để nghênh chiến! Ếch Lông Wolverine! Tuyển thủ số hai! Đại sứ tái sinh của hồ nước ngọt Mexico có thể mọc lại cả trái tim và não bộ không vết sẹo! Kỳ Nhông Axolotl! Tuyển thủ số ba! Sinh vật lầy lội không xương đáy biển sẵn sàng xả trọn bộ ruột qua hậu môn để tẩu thoát! Hải Sâm! Tuyển thủ số bốn! Cổ vật sống ba trăm triệu năm tiết ra hai mươi lít keo nhớt trong chớp mắt làm nghẹt thở cá mập! Cá Mút Đá Hagfish! Tuyển thủ số năm! Bậc thầy phân thân sở hữu chín bộ não và có thể cải trang thành mười lăm loài kịch độc đáy đại dương! Bạch Tuộc Mimic!
```
**Part 6** → `audio/vs/scene01_p6.wav` (472 ký tự) · mood `hao_hung`

```text
Tuyển thủ số sáu! Chiến xa đào hầm nước Úc sở hữu tấm mông bọc thép ba xăng-ti-mét đập nát sọ kẻ thù! Gấu Túi Wombat! Tuyển thủ số bảy! Cỗ máy săn mồi mù lòa mang hai mươi hai xúc tu hồng đớp mồi nhanh nhất hành tinh! Chuột Chũi Mũi Sao! Tuyển thủ số tám! Nữ chiến binh cảm tử sẵn sàng kích nổ cơ thể phun keo dính bảo vệ an toàn cho tổ ấm! Kiến Nổ Cảm Tử! Tuyển thủ số chín! Tổng công trình sư thiên tài sở hữu răng cam bọc sắt đốn ngã cổ thụ xây đập nước vĩ đại! Hải Ly!
```
**Part 7** → `audio/vs/scene01_p7.wav` (141 ký tự) · mood `nghiem_trang_gia`

```text
Và tuyển thủ số mười... xin mời ban tổ chức đưa kính lúp quang học ra sân vì bạn ấy đang trôi lơ lửng trong ly nước của giám khảo! [laughter]
```
**Part 8** → `audio/vs/scene01_p8.wav` (122 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Dạ em ở đây nè anh MC ơi! Em chỉ dài bốn phẩy năm mi-li-mét thôi nhưng tuổi thọ của em thì bằng cả vũ trụ cộng lại đó nha!
```
**Part 9** → `audio/vs/scene01_p9.wav` (247 ký tự) · mood `hao_hung`

```text
Một tràng pháo tay cho sự có mặt của mười dũng sĩ dị nhân! Và theo truyền thống, mời tất cả bước vào Lễ Cân Ký Đo Đạc khởi động! Mười tuyển thủ lần lượt bước lên đĩa cân kiểm tra thể trọng dưới sự giám sát chặt chẽ của các trọng tài thú y quốc tế!
```
**Part 10** → `audio/vs/scene01_p10.wav` (496 ký tự) · mood `don_dap`

```text
Chiến xa Wombat bước lên đầu tiên! Rầm! Ba mươi lăm ki-lô-gam cơ bắp chắc nịch đè nặng mặt cân thép! Tuyển thủ hạng nặng số một của đại hội! Tiếp theo là kỹ sư Hải Ly: hai mươi lăm ki-lô-gam lông dày và cơ hàm sắt thép, sẵn sàng cho mọi cuộc đọ sức thể lực! Nhóm hạng trung gồm Cá Mút Đá Hagfish nặng một ký, Hải Sâm nửa ký, và Bạch Tuộc Mimic ba trăm gam uốn lượn trên đĩa cân thủy tinh! Ếch Wolverine nặng tám mươi gam, Kỳ Nhông Axolotl bảy mươi gam, và Chuột Chũi Mũi Sao vỏn vẹn năm mươi gam!
```
**Part 11** → `audio/vs/scene01_p11.wav` (403 ký tự) · mood `nghiem_trang_gia`

```text
Và đỉnh điểm chênh lệch: Kiến Nổ chỉ nặng nửa miligram, còn Sứa Bất Tử chỉ nặng đúng một miligram bé như hạt bụi nước! Gấu Wombat nặng gấp... ba mươi lăm triệu lần Sứa Bất Tử! Chiếc máy tính của ban tổ chức suýt bốc khói vì tỷ lệ lệch pha này! [laughter] Sự chênh lệch khủng khiếp giữa cỗ xe bọc thép ba mươi lăm ký và chú sứa một miligram lập tức thổi bùng lên các cuộc tranh cãi nảy lửa khắp khán đài!
```
**Part 12** → `audio/vs/scene01_p12.wav` (389 ký tự) · mood `hao_hung`

```text
Sau lễ cân ký, bảng dự đoán ban đầu nghiêng hẳn về hai gã cơ bắp Wombat và Hải Ly cùng sát thủ móng vuốt Ếch Wolverine! Còn Sứa Bất Tử một miligram và Hải Sâm mềm nhũn? Giới chuyên môn ghi chú lạnh lùng: đề nghị mua sẵn bảo hiểm trọn gói! [laughter] Nhưng lịch sử hai mùa giải trước đã dạy chúng ta bài học xương máu: kẻ tí hon thường là kẻ tung ra cú đấm quyết định khiến tất cả ngã ngửa!
```
**Part 13** → `audio/vs/scene01_p13.wav` (393 ký tự) · mood `tram_bi_an`

```text
Mỗi ứng viên mang theo một bộ mã gen dị thường được tôi luyện qua hàng trăm triệu năm tiến hóa khắc nghiệt của tự nhiên! Không có sàn đấu nào trên hành tinh này có thể quy tụ cùng lúc những kỳ tích sinh học phá vỡ mọi quy luật vật lý và y học đến như vậy! Trong thế giới tự nhiên kỳ thú, cơ bắp chưa bao giờ là thước đo duy nhất cho sự sinh tồn! Đêm nay, mười dị nhân sẽ chứng minh chân lý đó!
```

### scene02 — ĐẠI CHIẾN NÂNG CẤP VŨ KHÍ & ÁO GIÁP SINH HỌC
*Thẻ chương:* ĐẠI CHIẾN VŨ KHÍ TỰ THÂN

*Badge:* `VÒNG 1: VŨ KHÍ TỰ THÂN` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene02_p0.wav` (439 ký tự) · mood `hao_hung`

```text
[surprise-oh] Tiếng còi khai cuộc vang lên! Chào mừng quý vị đến với Vòng một: Đọ Sức Vũ Khí Tự Thân và Áo Giáp Sinh Học! Tại vòng đấu này, mười tuyển thủ sẽ phô diễn những trang bị cơ thể dị thường nhất được tôi luyện qua hàng trăm triệu năm tiến hóa khắc nghiệt của thế giới hoang dã! Không có súng đạn cơ khí của con người, nhưng vũ khí sinh học tự nhiên lại sở hữu độ bền và hiệu năng vượt xa mọi phòng thí nghiệm quân sự tối tân nhất!
```
**Part 1** → `audio/vs/scene02_p1.wav` (816 ký tự) · mood `don_dap`

```text
Ứng cử viên số một bước ra sàn đấu: Gấu Túi Wombat mang chiếc mông bọc thép huyền thoại tiến thẳng vào mô hình hang đất hẹp với phong thái vô cùng tự tin! Các nhà khoa học tại đại học Adelaide đã phát hiện: lớp giáp mông này không phải là xương đặc thông thường, mà là sự kết hợp hoàn hảo giữa sụn dày và các dải mô mạc sợi kết nối siêu bền! Độ dày của tấm khiên lên tới ba xăng-ti-mét, có khả năng triệt tiêu toàn bộ lực cắn chết người từ hàm răng sắc nhọn của chó hoang Dingo một cách dễ dàng! Chưa dừng lại ở đó, Wombat tung ra tuyệt kỹ cú đá lừa ngược: dùng bốn chân gồng cứng đẩy toàn bộ sức nặng cơ thể ép nát hộp sọ kẻ tấn công lên trần hang đá hoa cương! Cơ chế đập nát sọ bằng mông biến nơi dễ tổn thương nhất của động vật thành một chiếc bẫy kẹp thủy lực nghiền nát mọi kẻ săn mồi liều lĩnh trong chớp mắt!
```
**Part 2** → `audio/vs/scene02_p2.wav` (254 ký tự) · mood `hao_hung`

```text
Tuyệt chiêu phòng thủ biến thành đòn tấn công chí mạng! Khán đài vỗ tay sấm dậy trước cỗ xe tăng đào hầm kiên cố của hoang dã nước Úc! Nhưng đối thủ của Wombat không hề chịu lép vế! Xin mời kỹ sư Hải Ly tiến vào sàn đọ sức với bộ răng cửa màu cam rực rỡ!
```
**Part 3** → `audio/vs/scene02_p3.wav` (764 ký tự) · mood `don_dap`

```text
Tại sao răng của Hải Ly lại có màu cam kỳ lạ như vậy? Một công trình nghiên cứu trên tạp chí Science đã làm sáng tỏ bí mật này! Men răng của Hải Ly được gia cố bằng các hạt nano hợp chất giàu sắt vô định hình, giúp răng của chúng cứng hơn cả men răng người và kháng hoàn toàn axit ăn mòn! Nhờ vũ khí bọc sắt này, Hải Ly có thể gặm đứt một thân cây gỗ cứng đường kính bốn mươi xăng-ti-mét chỉ trong vài giờ đồng hồ mà răng không hề bị mẻ hay gãy! Hơn thế nữa, răng của chúng mọc liên tục suốt đời, càng gặm gỗ nhiều thì hai mặt răng càng tự mài vào nhau thành lưỡi đục sắc như dao mổ phẫu thuật tinh vi! Nếu con người sở hữu hàm răng bọc sắt như Hải Ly, các nha sĩ trên toàn cầu chắc chắn sẽ thất nghiệp tập thể vì sâu răng không bao giờ có cửa tấn công! [laughter]
```
**Part 4** → `audio/vs/scene02_p4.wav` (769 ký tự) · mood `tram_bi_an`

```text
Đến lượt sát thủ rừng rậm Tây Phi xuất trận: Ếch Lông Wolverine! Khi bị đe dọa, chú ếch này tự gồng các bó cơ chân sau, bẻ gãy khớp nối sụn của đốt xương ngón chân cuối cùng! Mũi xương nhọn hoắt đâm xuyên thủng lớp da đệm thịt dưới lòng bàn chân, phóng ra ngoài như những chiếc móng vuốt tự chế chết người! Và điều kỳ diệu nhất theo công bố của tạp chí Biology Letters: sau khi chiến đấu xong, các cơ thả lỏng, móng xương tự thụt vào bên trong! Chỉ sau bốn mươi tám giờ, lớp mô da bị đâm rách sẽ tự động tái tạo và lành lặn hoàn toàn mà không hề bị nhiễm trùng nhờ các hợp chất kháng khuẩn cực mạnh tiết ra từ tuyến da! Một cơ chế bẻ xương tự thân có một không hai trong thế giới động vật có xương sống, kết hợp giữa vũ khí sát thương và khả năng tự chữa lành siêu tốc!
```
**Part 5** → `audio/vs/scene02_p5.wav` (0 ký tự) · mood `hao_hung`

```text

```
**Part 6** → `audio/vs/scene02_p6.wav` (752 ký tự) · mood `hao_hung`

```text
Không chỉ có bốn tuyển thủ trên, nữ chiến binh tí hon Kiến Nổ Cảm Tử cũng khiến ban giám khảo phải giật mình trước cơ chế tự hủy bảo vệ tổ! Nghiên cứu của tiến sĩ Alice Laciny tại Borneo phát hiện: cặp tuyến hàm dưới của kiến thợ phình to bất thường, kéo dài dọc toàn bộ khoang bụng! Khi đối mặt với kẻ thù xâm lược tổ, kiến thợ gồng toàn bộ các cơ bụng làm nứt vỡ lớp vỏ kitin, phóng thích dòng keo độc tố dính chặt và làm mù mắt kẻ tấn công! Một sự hy sinh quả cảm của tầng lớp thợ già để bảo toàn sự sống cho toàn bộ đàn ấu trùng và kiến chúa non trẻ! Và Bạch Tuộc Mimic cũng thể hiện vũ khí cận chiến: các giác hút trên tám xúc tu có thể siết chặt với lực hút hàng chục kilopascal, đồng thời tiết ra độc tố tetrodotoxin gây tê liệt tức thì con mồi!
```
**Part 7** → `audio/vs/scene02_p7.wav` (482 ký tự) · mood `tram_bi_an`

```text
Bên cạnh đó, lớp da nhầy đặc biệt của Kỳ Nhông Axolotl cũng là một tấm áo giáp sinh học vô hình chống lại mọi mầm bệnh nấm mốc nước ngọt! Lớp chất nhầy kháng khuẩn phủ kín bề mặt cơ thể Axolotl chứa hàng chục loại enzym lysozyme tự nhiên, tiêu diệt vi khuẩn gram âm ngay khi chúng vừa tiếp xúc với biểu bì! Nhờ vậy, ngay cả khi bị thương rách toạc da thịt trong các cuộc đụng độ dưới đáy hồ đục, cơ thể chúng vẫn duy trì trạng thái vô trùng tuyệt đối để phục vụ tiến trình tái sinh!
```
**Part 8** → `audio/vs/scene02_p8.wav` (1279 ký tự) · mood `don_dap`

```text
Thậm chí khi nghiên cứu kỹ lưỡng về cơ học va chạm, các nhà vật lý nhận thấy cấu trúc mông của Wombat hoạt động như một hệ thống giảm xóc thủy lực tự nhiên! Lực cắn chết người từ kẻ săn mồi bị phân tán đều ra toàn bộ vùng chậu và cột sống vững chãi, biến áp lực tập trung thành một lực nén nhẹ nhàng không gây tổn thương! Còn chiếc càng súng của Tôm Súng có thể chịu được áp lực nổ tương đương hàng chục bầu khí quyển mà lớp vỏ kitin bên ngoài không hề bị rạn nứt một sợi tóc! Ban giám khảo tròn mắt chấm điểm! Và cuối cùng là màn trình diễn của cụ tổ ba trăm triệu năm: Cá Mút Đá Hagfish! Khi một mô hình cá mập giả lao vào cắn, Hagfish ngay lập tức tiết ra một lượng chất nhầy nhỏ hòa tan vào nước biển xung quanh! Viện nghiên cứu sinh học vật liệu phát hiện: bên trong chất nhầy của Hagfish chứa hàng vạn sợi protein tơ cuộn tròn siêu nhỏ! Khi gặp nước biển, các sợi tơ này bung dài ra tới mười lăm xăng-ti-mét, tạo thành một mạng lưới sợi bền gấp mười lần tơ nhện và dai hơn cả sợi Kevlar dùng may áo giáp chống đạn! Để không bị chính chất nhầy của mình bít nghẹt, Hagfish tự uốn cong cơ thể thắt thành một nút số tám hoàn hảo, gạt phăng lớp nhớt từ đầu đến đuôi chỉ trong nháy mắt! Một vòng đọ sức vũ khí đỉnh cao khiến thang điểm của ban giám khảo suýt chạm trần tuyệt đối!
```
**Part 9** → `audio/vs/scene02_p9.wav` (281 ký tự) · mood `don_dap`

```text
Các nhà khoa học tại đại học Guelph phát hiện: độ đàn hồi của sợi tơ Hagfish khi kéo giãn còn vượt trội hơn cả sợi tơ nhện mạng tròn cự phách! Cấu trúc xoắn ốc của các vi sợi protein hoạt động như những chiếc lò xo giảm chấn phân tử, hấp thụ toàn bộ lực xé rách của dòng nước xoáy!
```
**Part 10** → `audio/vs/scene02_p10.wav` (266 ký tự) · 🎭 cameo `tham_phan`

```text
Ban giám khảo đã hội ý xong! Vòng một: Huy chương Đồng thuộc về Hải Ly với hàm răng bọc sắt! Huy chương Bạc thuộc về Cá Mút Đá với mạng lưới tơ nhớt siêu bền! Và Huy chương Vàng ba điểm xuất sắc thuộc về Gấu Túi Wombat với tấm khiên mông bọc thép công thủ toàn diện!
```
**Part 11** → `audio/vs/scene02_p11.wav` (129 ký tự) · mood `hao_hung`

```text
Một vòng đấu mở màn mãn nhãn! Bảng điểm Mùa ba chính thức nhảy số: Wombat dẫn đầu với ba điểm, Hagfish hai điểm, Hải Ly một điểm!
```

### scene03 — BẢN LĨNH TÁI SINH & NGHỆ THUẬT THOÁT CHẾT KỲ DỊ
*Thẻ chương:* BẢN LĨNH TÁI SINH THOÁT HIỂM

*Badge:* `VÒNG 2: TÁI SINH THOÁT HIỂM` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene03_p0.wav` (460 ký tự) · mood `hao_hung`

```text
[surprise-oh] Không để khán giả phải chờ lâu, chúng ta bước ngay vào Vòng hai: Bản Lĩnh Tái Sinh và Nghệ Thuật Thoát Hiểm Khó Tin! Nếu như Vòng một là cuộc đọ sức của giáp sắt và móng vuốt cơ học, thì Vòng hai là nơi quy luật sinh học thông thường bị bẻ gãy hoàn toàn! Đối với đa phần sinh vật sống trên Trái Đất, mất đi một cơ quan nội tạng quan trọng đồng nghĩa với cái chết cận kề. Nhưng với các quái kiệt đêm nay, đó chỉ là một sự cố nhỏ trên đường đi dạo!
```
**Part 1** → `audio/vs/scene03_p1.wav` (910 ký tự) · mood `don_dap`

```text
Tuyển thủ đầu tiên xuất trận với nụ cười thiên thần: Kỳ Nhông Axolotl của đất nước Mexico! Khán giả đều biết Axolotl có thể mọc lại chân tay, nhưng công trình nghiên cứu trên tạp chí Nature năm hai ngàn lẻ chín đã phát hiện một sự thật chấn động hơn nhiều! Các tế bào tại mầm tái sinh không hề quay về trạng thái tế bào gốc vô định, mà chúng lưu giữ một bộ nhớ danh tính dòng dõi cực kỳ chuẩn xác! Nhờ cơ chế này, Axolotl có thể tái tạo hoàn chỉnh một phần ba quả tim bị tổn thương, mọc lại các thùy não và nối liền tủy sống bị đứt đoạn mà không để lại bất kỳ vết sẹo xơ hóa nào! Đặc biệt hơn, chúng có khả năng tiếp nhận cấy ghép nội tạng từ bất kỳ cá thể Axolotl nào khác mà hệ miễn dịch hoàn toàn không hề có phản ứng đào thải mô ghép! Bạn có thể ghép mắt, ghép chân hay thậm chí ghép cả nửa bộ não từ một chú kỳ nhông khác sang, và cơ thể chúng vẫn tiếp nhận êm ru như đồ chính hãng của mình! [surprise-oh]
```
**Part 2** → `audio/vs/scene03_p2.wav` (229 ký tự) · mood `hao_hung`

```text
Cả khán đài ồ lên thán phục trước cỗ máy tái sinh hoàn hảo của thiên nhiên! Nhưng tiếng chuông ma thuật bất ngờ ngân vang từ chiếc ly thủy tinh nhỏ! Xin mời nữ hoàng đảo ngược thời gian: Sứa Bất Tử dài chỉ bốn phẩy năm mi-li-mét!
```
**Part 3** → `audio/vs/scene03_p3.wav` (845 ký tự) · mood `don_dap`

```text
Điều gì sẽ xảy ra khi một sinh vật già cỗi, bị bỏ đói hoặc chịu tổn thương thể xác nghiêm trọng? Thông thường cái chết sẽ là điểm kết thúc. Nhưng với Sứa Bất Tử, chúng kích hoạt một tiến trình sinh học kỳ diệu gọi là chuyển biệt hóa tế bào: toàn bộ các tế bào chuông sứa tự phân giải và chuyển hóa ngược! Khối mô này chìm xuống đáy biển, tự biến đổi trở lại thành một quần thể polyp sơ sinh hoàn toàn non trẻ, rồi từ đó lại nảy chồi sinh ra hàng trăm chú sứa con mới! Chu trình này có thể lặp đi lặp lại vô tận mà không bị giới hạn bởi tuổi già sinh học, biến chúng thành sinh vật duy nhất trên Trái Đất nắm giữ chìa khóa bất tử thực thụ! Giống như một người già tám mươi tuổi khi cảm thấy mệt mỏi có thể tự biến ngược thành một đứa bé sơ sinh trong nôi rồi lớn lên tiếp tục cuộc đời mới! Một quyền năng làm đảo lộn hoàn toàn định luật sinh học!
```
**Part 4** → `audio/vs/scene03_p4.wav` (657 ký tự) · mood `tram_bi_an`

```text
Đến lượt bậc thầy lầy lội dưới đáy đại dương bước ra: Hải Sâm! Khi bị một con cua biển khổng lồ kẹp chặt, Hải Sâm không bỏ chạy mà sử dụng chiêu thức tống xuất nội tạng kinh hoàng qua đường hậu môn! Đó là chùm ống Cuvier chứa đầy chất keo độc tố dính chặt khiến kẻ săn mồi tê liệt, trong khi Hải Sâm ung dung trườn đi thoát nạn! Và điều không tưởng là chỉ sau năm tuần lễ, Hải Sâm sẽ tự nuôi dưỡng và mọc lại nguyên vẹn một hệ tiêu hóa và buồng phổi nước hoàn toàn mới toanh! Chưa hết, các nhà sinh học tại đại học Bỉ còn phát hiện: loài cá ngọc trai tí hon Carapidae thường xuyên bơi chui vào tận sâu bên trong hậu môn của Hải Sâm để làm tổ trú ẩn an toàn!
```
**Part 5** → `audio/vs/scene03_p5.wav` (168 ký tự) · mood `hao_hung`

```text
Một chiếc khách sạn đáy biển kỳ quái nhất hành tinh khiến cả đấu trường cười nghiêng ngả! [laughter] Và cuối cùng là màn ảo thuật biến hóa thần tốc của Bạch Tuộc Mimic!
```
**Part 6** → `audio/vs/scene03_p6.wav` (570 ký tự) · mood `don_dap`

```text
Không cần ẩn nấp dưới cát, Bạch Tuộc Mimic sở hữu các túi sắc tố và hệ cơ papillae vi mô có thể thay đổi màu sắc và kết cấu bề mặt da chỉ trong hai trăm mili-giây! Tùy theo kẻ thù đang đối diện là ai, chúng có thể tự điều khiển tám xúc tu để giả dạng thành mười lăm loài kịch độc khác nhau: từ rắn biển sọc đen, cá sư tử xòe gai độc, cá bơn ẩn mình, đến cả sứa biển trôi nổi! Một năng lực ngụy trang động đạt đỉnh cao của trí tuệ đại dương! Kẻ thù nhìn vào chỉ thấy một bãi mìn sinh học đầy gai độc chết người chứ không hề nhận ra chú bạch tuộc đang cười thầm bên trong!
```
**Part 7** → `audio/vs/scene03_p7.wav` (824 ký tự) · mood `hao_hung`

```text
Nói về khả năng chịu đựng và thoát hiểm, Ếch Wolverine cũng sở hữu một cơ chế bảo vệ mối nối gân vô cùng kỳ lạ! Khác với các loài động vật có móng vuốt cố định, đầu mút xương ngón chân của ếch được giữ chặt bởi một khối mô collagen dạng sợi đàn hồi cực cao! Khi áp lực co cơ vượt qua ngưỡng chịu đựng, khối mô này tự đứt ra có kiểm soát, giải phóng móng xương đâm ra ngoài mà không làm rách các mạch máu chính! Điều này giải thích vì sao vết thương sau đó tự hàn gắn rất nhanh mà ếch không hề bị mất máu quá nhiều! Và tại sao chú cá ngọc trai sống trong hậu môn Hải Sâm cả tuần mà không hề bị ngạt thở hay chết chìm? Bởi vì Hải Sâm hô hấp bằng cách liên tục hút và xả hàng lít nước biển giàu oxy qua hậu môn vào hai nhánh phổi nước, biến nơi này thành một phòng khách sạn có điều hòa nhiệt độ và bình oxy tươi mới quanh năm!
```
**Part 8** → `audio/vs/scene03_p8.wav` (435 ký tự) · mood `tram_bi_an`

```text
Và ngay cả khi đối mặt với những cơn lũ quét ngập úng bất ngờ dưới lòng đất, Gấu Wombat cũng sở hữu bản lĩnh sinh tồn kỳ diệu để bảo toàn tính mạng! Khi nước lũ dâng ngập các cửa hang chính, Wombat không hề hoảng loạn mà bình tĩnh di chuyển lên các ngách hang cao hơn được thiết kế theo hình chữ U ngược! Những túi khí tự nhiên này giúp chúng sống sót ngon lành dưới lòng đất suốt nhiều ngày liền chờ cho đến khi nước lũ rút hoàn toàn!
```
**Part 9** → `audio/vs/scene03_p9.wav` (466 ký tự) · mood `don_dap`

```text
Không chỉ có khả năng mọc lại chi và nội tạng, Kỳ Nhông Axolotl còn có thể tái tạo hoàn chỉnh tế bào võng mạc mắt và thấu kính quang học tinh khiết! Khi bị tổn thương thị giác, các tế bào sắc tố biểu mô mống mắt tự động chuyển hóa thành tế bào gốc phôi thai để dệt lại một thấu kính mắt mới toanh không hề có vết mờ đục! Còn Hải Sâm thì sở hữu khả năng tái tạo tế bào tuyến sinh dục và mô bài tiết chỉ trong vòng vài tuần lễ sau các cuộc giải phẫu tự thân khốc liệt!
```
**Part 10** → `audio/vs/scene03_p10.wav` (259 ký tự) · mood `don_dap`

```text
Điều kinh ngạc nhất là hệ thống tái sinh của Hải Sâm được kích hoạt bởi các phân tử tín hiệu hóa học peptide vô cùng đặc biệt! Chỉ trong vòng hai mươi tư giờ sau khi tự phóng nội tạng, các tế bào gốc biểu mô ruột đã kết tụ thành mầm mô tạng non trẻ khỏe mạnh!
```
**Part 11** → `audio/vs/scene03_p11.wav` (328 ký tự) · 🎭 cameo `tham_phan`

```text
Kết quả Vòng hai của ban giám khảo: Huy chương Đồng thuộc về Bạch Tuộc Mimic với màn biến hình mười lăm loài kịch độc! Huy chương Bạc thuộc về Kỳ Nhông Axolotl với bộ nhớ tái sinh mô hoàn hảo không sẹo! Và Huy chương Vàng ba điểm xuất sắc thuộc về tuyển thủ bé hạt tiêu Sứa Bất Tử với vòng lặp đảo ngược thời gian tế bào vô cực!
```
**Part 12** → `audio/vs/scene03_p12.wav` (148 ký tự) · mood `hao_hung`

```text
Bảng điểm sau hai vòng thi đấu đảo chiều ngoạn mục: Wombat và Sứa Bất Tử cùng chia sẻ ngôi đầu với ba điểm, Hagfish và Axolotl bám sát với hai điểm!
```

### scene04 — PHẢN XẠ SIÊU TỐC & GIÁC QUAN VƯỢT TRỘI DƯỚI LÒNG ĐẤT
*Thẻ chương:* PHẢN XẠ GIÁC QUAN SIÊU TỐC

*Badge:* `VÒNG 3: PHẢN XẠ GIÁC QUAN` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene04_p0.wav` (428 ký tự) · mood `hao_hung`

```text
[surprise-oh] Đấu trường lại rực lửa! Chào mừng quý vị đến với Vòng ba: Phản Xạ Siêu Tốc và Những Giác Quan Kỳ Dị Vượt Trội! Nếu bạn nghĩ mắt là cửa sổ tâm hồn duy nhất để quan sát thế giới, thì các tuyển thủ Vòng ba sẽ khiến bạn phải suy nghĩ lại từ đầu! Ở thế giới bóng tối dưới lòng đất hay đáy biển sâu đục ngầu, thị giác thông thường hoàn toàn trở nên vô dụng, nhường chỗ cho những giác quan cơ học và sóng âm tinh vi nhất!
```
**Part 1** → `audio/vs/scene04_p1.wav` (1217 ký tự) · mood `don_dap`

```text
Tiến vào đường hầm thử nghiệm bóng tối: sát thủ săn mồi đầm lầy Bắc Mỹ, Chuột Chũi Mũi Sao! Mặc dù đôi mắt bị thoái hóa gần như mù lòa, chiếc mũi chứa hai mươi lăm ngàn cơ quan thụ cảm của Chuột Chũi Mũi Sao lại là cơ quan xúc giác nhạy bén nhất từng được ghi nhận trong lịch sử khoa học! Hai mươi lăm ngàn cơ quan Eimer này chứa mạng lưới dây thần kinh cảm giác dày đặc đến mức: hơn năm mươi phần trăm diện tích vỏ não của chú chuột chũi này chỉ dùng để giải mã tín hiệu từ chiếc mũi sao! Và khi một ấu trùng côn trùng xuất hiện, chiếc đồng hồ đếm mili-giây của ban tổ chức bắt đầu đếm ngược! Chạm! Nhận diện! Nuốt chửng! Toàn bộ tiến trình chỉ diễn ra trong đúng không phẩy mười hai giây đồng hồ! Nhanh hơn một cái chớp mắt của con người tới ba lần! Chưa hết, giáo sư Kenneth Catania tại đại học Vanderbilt còn phát hiện một tuyệt kỹ không tưởng: Chuột Chũi Mũi Sao có thể ngửi được mùi thức ăn dưới nước! Bằng cách liên tục thổi các bong bóng khí từ lỗ mũi chạm vào vật thể rồi hít ngược bong bóng trở lại xoang mũi, chúng thu gom các phân tử mùi lơ lửng trong nước để ngửi chính xác tuyệt đối! Động vật có vú duy nhất trên Trái Đất có thể hít thở và ngửi mùi thức ăn trong môi trường ngập nước mà không hề bị sặc!
```
**Part 2** → `audio/vs/scene04_p2.wav` (239 ký tự) · mood `hao_hung`

```text
Động vật có vú đầu tiên trên thế giới ngửi được mùi khi đang ngụp lặn dưới nước! Một tràng pháo tay cho Chuột Chũi Mũi Sao! Nhưng đối thủ của chú ta, Bạch Tuộc Mimic, lập tức bước lên với hệ thần kinh phân tán dị thường bậc nhất đại dương!
```
**Part 3** → `audio/vs/scene04_p3.wav` (628 ký tự) · mood `don_dap`

```text
Các nhà khoa học thần kinh phát hiện: hai phần ba tổng số nơ-ron não bộ của bạch tuộc không hề nằm ở hộp sọ trung tâm, mà trải dài dọc theo tám xúc tu! Điều này có nghĩa là mỗi xúc tu của Bạch Tuộc Mimic giống như một bộ não thu nhỏ: có thể tự nếm vị giác qua các giác hút, tự sờ chạm, tự suy nghĩ và giải quyết chướng ngại vật mà không cần chờ lệnh từ não bộ! Khi bị săn đuổi, tám xúc tu có thể tự động phối hợp điều phối các bước chạy mà não trung tâm chỉ cần tập trung tính toán đường thoát hiểm! Mỗi xúc tu vừa là cánh tay, vừa là con mắt xúc giác, vừa là chiếc lưỡi nếm vị thức ăn! Một mạng lưới trí tuệ phân tán siêu việt!
```
**Part 4** → `audio/vs/scene04_p4.wav` (568 ký tự) · mood `tram_bi_an`

```text
Đến lượt Ếch Lông Wolverine thể hiện giác quan thích nghi dòng suối chảy xiết! Lớp lông tơ kỳ lạ ở hai bên hông của ếch đực chứa đầy mạng lưới mao mạch máu và các tế bào thụ cảm cơ học vi mô! Khi ngồi dưới đáy suối đục ngầu cuồn cuộn bùn cát, lớp lông này vừa hấp thụ oxy hòa tan trong nước, vừa cảm nhận được sự thay đổi áp suất dòng chảy nhỏ nhất từ kẻ săn mồi bơi qua! Và kỹ sư Hải Ly cũng sở hữu đôi mắt bơi lặn siêu việt: lớp mí mắt thứ ba trong suốt hoạt động như chiếc kính bơi chuyên nghiệp, giúp chúng quan sát rõ mồn một từng cành cây dưới đáy sông đục ngầu!
```
**Part 5** → `audio/vs/scene04_p5.wav` (742 ký tự) · mood `hao_hung`

```text
Cá Mút Đá Hagfish dù sống dưới đáy biển tăm tối một ngàn mét và mắt thoái hóa hoàn toàn thành vệt sắc tố dưới da, nhưng chúng sở hữu chiếc mũi thính nhạy số một đại dương! Khác với mọi loài cá có hai lỗ mũi, Hagfish chỉ có một lỗ mũi duy nhất dẫn thẳng nước biển vào một túi khứu giác khổng lồ kết nối trực tiếp với thùy khứu giác của não bộ! Chúng có thể đánh hơi thấy mùi một xác cá voi chìm cách xa hàng chục cây số giữa đại dương bao la, rồi bơi thẳng tới đích mà không cần đến một tia sáng nào! Còn Kiến Nổ Cảm Tử thì sở hữu cặp râu cảm biến hóa học phát hiện tín hiệu pheromone xâm nhập chỉ trong năm mươi mili-giây! Chẳng có một tên gián điệp hay kẻ săn mồi nào có thể lén lút tiếp cận cửa tổ mà không bị cặp râu siêu nhạy này lật tẩy!
```
**Part 6** → `audio/vs/scene04_p6.wav` (441 ký tự) · mood `don_dap`

```text
Không chỉ có đôi mắt mí thứ ba, Hải Ly còn sở hữu hệ thống cảnh báo sớm bằng sóng âm mặt nước vô cùng lợi hại! Mỗi khi phát hiện bóng dáng kẻ săn mồi như chó sói hay gấu xám từ xa, Hải Ly dùng chiếc đuôi dẹt nặng nề đập cực mạnh xuống mặt nước tạo nên tiếng nổ rầm vang dội khắp thung lũng! Âm thanh đập đuôi này truyền đi cả trong không khí lẫn dưới đáy nước, cảnh báo cho toàn bộ bầy đàn lặn sâu xuống đáy bùn trốn thoát chỉ trong ba giây!
```
**Part 7** → `audio/vs/scene04_p7.wav` (476 ký tự) · mood `don_dap`

```text
Để phối hợp nhịp nhàng giữa hai mươi hai xúc tu, não bộ của Chuột Chũi Mũi Sao xử lý các xung thần kinh cảm giác với tốc độ nhanh gấp mười lần dây thần kinh mắt người! Mỗi khi xúc tu chạm nhẹ vào một vật thể lạ, bộ não phân tích lập tức cấu trúc vật liệu, độ ẩm, độ nhớt và nhiệt độ của đối tượng trong vòng vài phần nghìn giây! Đó là lý do vì sao chúng có thể phân biệt chính xác đâu là thức ăn bổ dưỡng và đâu là hạt cát vô giá trị trong nháy mắt mà không bao giờ nuốt nhầm!
```
**Part 8** → `audio/vs/scene04_p8.wav` (458 ký tự) · mood `don_dap`

```text
Các nhà khoa học tại đại học Vanderbilt phát hiện: vùng vỏ não cảm giác của Chuột Chũi Mũi Sao dành tới năm mươi phần trăm diện tích chỉ để xử lý tín hiệu từ chiếc mũi! Độ phân giải xúc giác trên chiếc mũi này chi tiết và sắc nét đến mức tương đương với độ nhạy thị giác của mắt đại bàng trên bầu trời! Nhờ đó, dù sống cả đời trong lòng đất đen đặc chẳng hề có tia sáng, Chuột Chũi Mũi Sao vẫn nhìn thấy thế giới bằng xúc giác với độ chân thực đến kinh ngạc!
```
**Part 9** → `audio/vs/scene04_p9.wav` (387 ký tự) · 🎭 cameo `tham_phan`

```text
Ban giám khảo xin công bố điểm số Vòng ba! Huy chương Đồng thuộc về Ếch Lông Wolverine với bộ lông tơ thụ cảm áp suất dòng suối! Huy chương Bạc thuộc về Bạch Tuộc Mimic với tám xúc tu mang trí tuệ nơ-ron độc lập phi thường! Và Huy chương Vàng ba điểm xuất sắc thuộc về Chuột Chũi Mũi Sao với kỷ lục săn mồi không phẩy mười hai giây cùng tuyệt chiêu ngửi mùi dưới nước bằng bong bóng khí!
```
**Part 10** → `audio/vs/scene04_p10.wav` (160 ký tự) · mood `hao_hung`

```text
Cục diện bảng tổng sắp sau ba vòng đấu vô cùng gay cấn: Wombat, Sứa Bất Tử và Chuột Chũi Mũi Sao cùng nắm giữ ba điểm! Đấu trường ngày càng kịch tính nghẹt thở!
```

### scene05 — GIỜ GIẢI LAO HẬU TRƯỜNG & NHỮNG PHA KHÓ ĐỠ CỦA DỊ NHÂN
*Thẻ chương:* NHỮNG PHA HẬU TRƯỜNG KHÓ ĐỠ

*Badge:* `GIỜ GIẢI LAO HẬU TRƯỜNG` · *mood mặc định:* `bi_hai`

**Part 0** → `audio/vs/scene05_p0.wav` (391 ký tự) · mood `hao_hung`

```text
Sau ba vòng thi đấu căng như dây đàn, ban tổ chức xin thông báo: toàn thể đấu trường bước vào ba mươi phút giải lao hậu trường! Các tuyển thủ tạm lui về khu vực phòng thay đồ để nạp năng lượng và chuẩn bị cho các vòng đấu khốc liệt tiếp theo. Nhưng ngay lúc này, camera giấu kín của ban tổ chức đã ghi lại hàng loạt khoảnh khắc dở khóc dở cười khiến bà Cú giám khảo suýt ngất xỉu! [laughter]
```
**Part 1** → `audio/vs/scene05_p1.wav` (679 ký tự) · mood `bi_hai`

```text
Ở phòng nghỉ số một của kỹ sư Hải Ly: bồn rửa mặt của ban tổ chức bị rò rỉ nước, phát ra tiếng róc rách nho nhỏ! Một nghiên cứu của giáo sư Dietrich Müller-Schwarze đã chứng minh: Hải Ly bị một chứng ám ảnh cưỡng chế sinh học cực nặng với tiếng nước chảy! Chúng không hề bận tâm xem nước chảy ở đâu, chỉ cần nghe thấy tiếng róc rách là bản năng lập tức ra lệnh: phải đắp đập bịt kín ngay tức khắc! Thậm chí khi chiếc loa thông báo của anh MC phát ra tiếng nhạc nền suối reo, Hải Ly đã phi ra vác nguyên một khúc gỗ to đùng chèn cứng họng loa! [laughter] Các nhân viên hậu đài phải mất nửa tiếng đồng hồ dùng búa nhổ đinh để cạy con đập mini trong nhà vệ sinh của Hải Ly ra ngoài!
```
**Part 2** → `audio/vs/scene05_p2.wav` (710 ký tự) · mood `hao_hung`

```text
Trong khi đó, ở khu vực phòng chờ của Ếch Wolverine và Kỳ Nhông Axolotl, một cuộc tranh luận nảy lửa của hai đại diện lưỡng cư đang nổ ra! Ếch Wolverine khoe móng xương bảo: Bẻ xương làm vuốt mới là đỉnh cao chiến binh ngầu lòi! Kỳ Nhông Axolotl mỉm cười lắc đầu đáp lại: Tự làm đau mình làm chi anh ơi, cứ để đối thủ cắn một miếng rồi mình mọc lại cái mới xinh xắn có phải nhàn nhã hơn không! [laughter] Còn ở góc phòng khách, chú Bạch Tuộc Mimic đang rảnh rỗi trổ tài biến hình thành một chiếc gối ôm sofa bằng nhung nâu sọc trắng! Bà Cú giám khảo bước vào mệt mỏi định ngồi phịch xuống nghỉ lưng, thì chiếc gối ôm bỗng thò ra tám cái xúc tu ôm chầm lấy bà Cú làm bà thét lên một tiếng kinh hoàng! [laughter]
```
**Part 3** → `audio/vs/scene05_p3.wav` (100 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Dạ em chỉ muốn thử xem khả năng ngụy trang của em có lừa được mắt cú vọ của giám khảo không thôi mà!
```
**Part 4** → `audio/vs/scene05_p4.wav` (422 ký tự) · mood `bi_hai`

```text
Ở một góc sân khác, Kỳ Nhông Axolotl đang tận hưởng dịch vụ tắm bùn khoáng nóng do ban tổ chức chu cấp với vẻ mặt thỏa mãn vô cùng! Chú kỳ nhông cười tít mắt bảo: Đấu trường sinh tồn gì mà sướng như đi nghỉ dưỡng năm sao thế này, em muốn ở đây thi đấu quanh năm luôn quá! [laughter] Trong khi đó, anh chàng Ếch Wolverine đang miệt mài ngồi mài lại bộ móng vuốt xương vào mép bàn đá cẩm thạch kêu ken két nghe rợn cả người!
```
**Part 5** → `audio/vs/scene05_p5.wav` (332 ký tự) · mood `bi_hai`

```text
Thậm chí chú cá ngọc trai Carapidae trong hậu môn Hải Sâm còn gọi thêm cả đàn bạn bè bơi vào tổ chức một buổi hòa nhạc mini dưới nước! [laughter] Hải Sâm bèn thử gồng các cơ co thắt để tống cổ đàn khách trọ ồn ào ra ngoài, nhưng đàn cá ngọc trai lại tưởng đó là dịch vụ mát-xa thủy lực miễn phí nên càng khoái chí nằm im! [laughter]
```
**Part 6** → `audio/vs/scene05_p6.wav` (107 ký tự) · 🎭 cameo `tham_phan`

```text
Thí sinh Hải Ly! Tôi cấm anh biến phòng vệ sinh của ban giám khảo thành công trường xây dựng thủy điện nhé!
```
**Part 7** → `audio/vs/scene05_p7.wav` (862 ký tự) · mood `bi_hai`

```text
Bà Cú giám khảo vừa bước sang phòng số hai của Gấu Wombat thì lại đụng phải một cảnh tượng kỳ quặc không kém! Anh chàng Wombat đang thong thả ngồi trên bồn cầu, chăm chú xếp từng khối phân hình lập phương thành một kim tự tháp vuông vức cực kỳ nghệ thuật! [laughter] Tại sao phân của Wombat lại có hình lập phương độc nhất vô nhị trên thế giới? Nghiên cứu đoạt giải Ig Nobel vật lý của tiến sĩ Patricia Yang đã giải mã bí ẩn này! Chỉ có tám phần trăm đoạn ruột già cuối cùng của Wombat sở hữu cấu trúc mô cơ đàn hồi không đồng đều: hai rãnh cơ cứng chắc và hai rãnh cơ mềm dẻo! Mỗi ngày, Wombat đúc ra từ tám mươi đến một trăm viên phân lập phương sắc cạnh như xúc xắc để đánh dấu lãnh thổ trên các tảng đá mà không sợ bị lăn xuống dốc! Khả năng đúc hình học chuẩn xác tới mức các nhà sản xuất gạch xây dựng của con người cũng phải trầm trồ xin bí quyết học hỏi!
```
**Part 8** → `audio/vs/scene05_p8.wav` (89 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Dạ thưa cô giám khảo, em vừa đúc xong mẻ mới nóng hổi tặng ban tổ chức làm kỷ niệm nè cô!
```
**Part 9** → `audio/vs/scene05_p9.wav` (530 ký tự) · mood `bi_hai`

```text
Sang đến phòng của Kiến Nổ Cảm Tử, không khí lại căng thẳng như một kho thuốc súng sắp nổ! Chú kiến nhỏ nơm nớp lo sợ ai đó vô tình vỗ mạnh vào vai làm vỡ tuyến keo dính trên bụng, kích nổ ba lô độc tố màu vàng sáng rực! Còn ở góc bể nước của Hải Sâm, một chú cá ngọc trai Carapidae vừa chui tọt vào hậu môn của Hải Sâm để ngủ trưa rồi thò đầu ra ngoài ngáp một cái thật dài! [laughter] Chú cá này thậm chí còn rủ thêm hai người bạn cá ngọc trai khác vào cùng trú ngụ, biến cơ thể Hải Sâm thành một căn hộ chung cư mini dưới nước!
```
**Part 10** → `audio/vs/scene05_p10.wav` (119 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Cứu em với anh MC ơi! Tên khách trọ này ở ké cả tuần nay không trả một xu tiền phòng mà còn ngáy to quá làm em mất ngủ!
```
**Part 11** → `audio/vs/scene05_p11.wav` (218 ký tự) · mood `hao_hung`

```text
[laughter] Và đỉnh điểm khó đỡ: anh MC vừa cầm ly nước chanh lên định uống một ngụm giải khát thì phát hiện Sứa Bất Tử đang tung tăng bơi lội bên trong! May mà chưa nuốt chửng tân vương tiềm năng của Mùa ba! [laughter]
```
**Part 12** → `audio/vs/scene05_p12.wav` (585 ký tự) · mood `don_dap`

```text
Dưới kính hiển vi điện tử, da của Bạch Tuộc Mimic là một màn hình chấm lượng tử sinh học với hàng triệu tế bào sắc tố chromatophore và iridophore! Mỗi tế bào sắc tố được điều khiển bởi một sợi dây thần kinh riêng biệt, cho phép chúng thay đổi màu sắc và kết cấu bề mặt da chỉ trong hai trăm mili-giây! Trong khi đó, Sứa Bất Tử cũng tận dụng thời gian nghỉ giữa hiệp để kích hoạt quá trình tái lập trình nơ-ron thần kinh vô cùng kỳ diệu! Cơ thể sứa tí hon này không bao giờ biết mệt mỏi, bởi mỗi khi căng thẳng, chúng chỉ việc đảo ngược tế bào để trở lại trạng thái thanh xuân sung mãn!
```
**Part 13** → `audio/vs/scene05_p13.wav` (372 ký tự) · mood `don_dap`

```text
Không khí phòng nghỉ ngơi của Ếch Lông Wolverine thì tràn ngập tiếng gầm gừ tập luyện cơ bắp cuồn cuộn! Chú ếch liên tục kiểm tra khớp móng vuốt để đảm bảo các mũi xương đã thu gọn hoàn toàn vào bao gân trước khi bước vào các vòng đấu quyết định! Giờ giải lao kết thúc trong những tiếng cười sảng khoái! Tất cả mười tuyển thủ đã sẵn sàng quay trở lại đấu trường khốc liệt!
```

### scene06 — CÔNG TRÌNH ĐỊA HÌNH & XÃ HỘI BẦY ĐÀN KỶ LUẬT
*Thẻ chương:* CÔNG TRÌNH ĐỊA HÌNH VĨ ĐẠI

*Badge:* `VÒNG 4: KỸ SƯ ĐỊA HÌNH` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene06_p0.wav` (426 ký tự) · mood `hao_hung`

```text
[surprise-oh] Chào mừng quý vị quay trở lại với Vòng bốn: Kỹ Sư Địa Hình và Những Xã Hội Động Vật Kỷ Luật Thép! Tại vòng đấu này, chúng ta sẽ được chứng kiến cách những sinh vật hoang dã tái định hình cả cảnh quan thiên nhiên và bảo vệ giống nòi! Không phải máy xúc, xe ủi hay xi măng cốt thép của con người, chính những chiếc đuôi dẹt, móng vuốt đào hầm và tinh thần kỷ luật bầy đàn đã tạo nên những kỳ quan sinh thái vĩ đại!
```
**Part 1** → `audio/vs/scene06_p1.wav` (947 ký tự) · mood `don_dap`

```text
Không ai xứng đáng mở màn vòng đấu này hơn kỹ sư Hải Ly: kiến trúc sư thiên tài số một của thế giới tự nhiên! Khán giả thường nghĩ Hải Ly xây đập chỉ để bảo vệ hang ở của mình, nhưng một nghiên cứu năm hai ngàn không trăm hai mươi trên tạp chí Ecological Applications đã chỉ ra tầm vóc vĩ đại hơn nhiều! Khi những trận cháy rừng kinh hoàng quét qua Bắc Mỹ thiêu rụi toàn bộ thung lũng xung quanh, chính những con đập của Hải Ly đã tạo ra các ốc đảo ngập nước xanh tươi bất khả xâm phạm! Độ ẩm cao và mực nước ngầm dồi dào từ đập Hải Ly chặn đứng hoàn toàn bước tiến của ngọn lửa hung tàn, cứu sống hàng vạn sinh mạng hoang dã! Hơn thế nữa, đập Hải Ly giữ lại tới tám mươi phần trăm lượng bùn đất xói mòn và kim loại nặng, thanh lọc nguồn nước uống trong lành cho toàn bộ hạ lưu! Những con đập của Hải Ly có thể tồn tại qua hàng thế kỷ, thậm chí có con đập cổ xưa dài tới tám trăm mét tại Canada nhìn thấy rõ mồn một từ ảnh chụp vệ tinh không gian!
```
**Part 2** → `audio/vs/scene06_p2.wav` (258 ký tự) · mood `hao_hung`

```text
Một cỗ máy thanh lọc môi trường sống tự nhiên không tốn một xu tiền điện của Trái Đất! Cả khán đài cúi mình thán phục trước Hải Ly! Tiếp theo, hãy cùng nhìn sâu xuống lòng đất nước Úc nơi Gấu Túi Wombat làm nên điều kỳ diệu trong các trận thảm họa cháy rừng!
```
**Part 3** → `audio/vs/scene06_p3.wav` (730 ký tự) · mood `don_dap`

```text
Mỗi hệ thống hang của Wombat có thể kéo dài tới ba mươi mét với hàng chục ngách rẽ và nhiều cửa thoát hiểm được đào kiên cố! Trong các trận hỏa hoạn lịch sử tại rừng nước Úc khi nhiệt độ mặt đất lên tới hàng trăm độ C, nhiệt độ dưới hang Wombat vẫn duy trì ổn định ở mức hai mươi độ mát mẻ! Camera của các nhà khoa học bảo tồn đã ghi lại những thước phim xúc động: chuột túi Wallaby, kỳ đà, chim sẻ và thú có túi cùng lũ lượt kéo nhau xuống hang Wombat để lánh nạn! Wombat không hề xua đuổi hay tấn công mà hào phóng chia sẻ nơi trú ẩn an toàn, trở thành những người hùng cứu hỏa thầm lặng của đại lục Úc! Hệ thống hang ngầm này hoạt động như một boongke chống thảm họa thiên nhiên hoàn hảo nhất mà không cần đến bê tông cốt thép!
```
**Part 4** → `audio/vs/scene06_p4.wav` (562 ký tự) · mood `tram_bi_an`

```text
Và cuối cùng là cấu trúc xã hội kỷ luật thép của Kiến Nổ Cảm Tử trên các tán rừng nhiệt đới Đông Nam Á! Tiến sĩ Alice Laciny phát hiện: trong tổ của Kiến Nổ có một tầng lớp lính gác cửa đặc biệt sở hữu hộp sọ biến đổi phẳng lì như một chiếc nút chai! Chúng dùng chính chiếc đầu bọc giáp của mình làm chiếc cửa chống đạn bịt kín hoàn toàn lối vào, ngăn chặn mọi kẻ xâm lược từ bên ngoài! Chiếc cửa sống này chỉ mở ra khi kiến thợ đi kiếm ăn về gõ đúng mật mã râu pheromone đặc trưng của bầy đàn! Một hệ thống an ninh sinh học bảo mật tuyệt đối không thể phá khóa!
```
**Part 5** → `audio/vs/scene06_p5.wav` (721 ký tự) · mood `hao_hung`

```text
Để xây dựng những con đập dài hàng trăm mét, Hải Ly còn sở hữu kỹ năng đào kênh dẫn nước kỳ tài không kém các kỹ sư thủy lợi La Mã! Chúng tự đào các tuyến kênh ngập nước dài tới hai trăm mét đâm sâu vào các khu rừng gỗ cứng, để thả nổi các khúc gỗ nặng hàng chục ký trôi theo dòng nước về vị trí đắp đập mà không tốn sức kéo lê trên cạn! Đặc biệt, thân đập của Hải Ly được thiết kế uốn cong hình cánh cung hướng ngược về phía dòng chảy, mô phỏng hoàn hảo nguyên lý chịu lực của các con đập thủy điện vòm bê tông hiện đại nhất! Hệ thống kiến trúc tự nhiên này có thể điều tiết lưu lượng nước của cả một lưu vực sông rộng lớn, biến Hải Ly thành loài động vật duy nhất có thể thay đổi địa hình Trái Đất ngang ngửa con người!
```
**Part 6** → `audio/vs/scene06_p6.wav` (433 ký tự) · mood `don_dap`

```text
Để chuẩn bị cho mùa đông băng giá Bắc Mỹ khi mặt hồ đóng băng dày hàng mét, Hải Ly còn xây dựng những kho lương thực ngập nước ngầm vô cùng thông minh! Chúng cắm chặt hàng trăm cành cây gỗ tươi giàu dinh dưỡng xuống lớp bùn sâu dưới đáy hồ ngay cạnh cửa hang ngầm! Khi mặt hồ đóng băng kín mít, Hải Ly chỉ việc bơi ra cửa hang ngầm, rút một cành cây tươi dưới bùn mang vào hang thưởng thức mà không cần thò đầu lên mặt băng lạnh giá!
```
**Part 7** → `audio/vs/scene06_p7.wav` (422 ký tự) · mood `don_dap`

```text
Một công trình đập của Hải Ly có thể nâng mực nước ngầm của toàn bộ lưu vực xung quanh lên cao thêm từ một đến hai mét suốt mùa khô hạn! Nhờ nguồn nước ngầm dồi dào này, thảm thực vật ven bờ phát triển xanh tốt quanh năm, tạo nguồn thức ăn dồi dào nuôi sống các đàn hươu nai và chim muông vượt qua mùa đông khắc nghiệt! Hải Ly thực sự là một kỹ sư kiến tạo cảnh quan sinh thái có tầm ảnh hưởng sâu rộng bậc nhất hành tinh!
```
**Part 8** → `audio/vs/scene06_p8.wav` (703 ký tự) · mood `don_dap`

```text
Không dừng lại ở việc đắp đập, những kiến trúc sư Hải Ly tài ba còn đào những con kênh dẫn nước dài tới năm trăm mét sâu vào giữa rừng già! Những con kênh này cho phép Hải Ly thả trôi những khúc gỗ nặng hàng trăm cân về tổ một cách nhẹ nhàng, giảm thiểu tối đa nguy cơ bị thú dữ mai phục trên cạn! Còn tấm khiên sụn mông của Wombat cứng đến mức những cú cắn của chó rừng Dingo hay đại bàng đuôi nhọn chỉ để lại những vết xước mờ nhạt không đáng kể! Hải Ly còn sở hữu lớp lông dày tới mười ngàn sợi trên một xen-ti-mét vuông da, được bôi trơn bởi lớp dầu castoreum chống thấm nước tuyệt đối! Nhờ đó, ngay cả khi bơi lội dưới lớp băng dày vào mùa đông Bắc Mỹ, da của Hải Ly vẫn hoàn toàn khô ráo và ấm áp!
```
**Part 9** → `audio/vs/scene06_p9.wav` (341 ký tự) · 🎭 cameo `tham_phan`

```text
Ban giám khảo xin công bố kết quả Vòng bốn! Huy chương Đồng thuộc về Kiến Nổ Cảm Tử với cánh cửa sọ nút chai an ninh pheromone! Huy chương Bạc thuộc về Gấu Túi Wombat với mạng lưới hang ngầm cứu trợ muông thú trong thảm họa! Và Huy chương Vàng ba điểm xứng đáng thuộc về kỹ sư Hải Ly với công trình đập nước chống hạn hán và đẩy lùi bão lửa!
```
**Part 10** → `audio/vs/scene06_p10.wav` (128 ký tự) · mood `hao_hung`

```text
Bảng điểm sau bốn vòng đấu tiếp tục có biến động lớn: Wombat vươn lên dẫn đầu với năm điểm! Hải Ly bứt phá mạnh mẽ lên bốn điểm!
```

### scene07 — KHÁNG THỂ SIÊU CẤP & BỘ GEN BẤT TỬ ĐỘT BIẾN
*Thẻ chương:* KHÁNG THỂ & BỘ GEN ĐỘT BIẾN

*Badge:* `VÒNG 5: BỘ GEN ĐỘT BIẾN` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene07_p0.wav` (413 ký tự) · mood `hao_hung`

```text
[surprise-oh] Tiến vào chặng đua thứ năm! Chào mừng quý vị đến với Vòng năm: Kháng Thể Siêu Cấp và Những Bộ Gen Đột Biến Kỳ Vĩ! Ở vòng đấu này, cuộc cạnh tranh không còn diễn ra ở tầm cơ bắp hay móng vuốt, mà đi sâu vào tận cấp độ phân tử và tế bào vi mô! Những bí mật di truyền được mã hóa qua hàng tỷ cặp base nitơ chính là tấm bản đồ thần kỳ giúp các dị nhân vượt qua những nghịch lý sinh tồn khắc nghiệt nhất!
```
**Part 1** → `audio/vs/scene07_p1.wav` (963 ký tự) · mood `don_dap`

```text
Tuyển thủ đầu tiên bước lên bục phân tích di truyền: Kỳ Nhông Axolotl của hồ Xochimilco! Một công trình nghiên cứu quy mô toàn cầu đăng tải trên tạp chí Nature năm hai ngàn mười tám đã giải mã thành công toàn bộ hệ gen của Axolotl! Kết quả khiến giới khoa học sững sờ: bộ gen của chú kỳ nhông này dài tới ba mươi hai tỷ cặp base nitơ, tức là gấp mười lần toàn bộ hệ gen của một con người trưởng thành! Ẩn sâu trong ba mươi hai tỷ cặp base này là những đoạn gen kiểm soát phân bào độc nhất vô nhị: các tế bào mọc lại chi phân chia với tốc độ tên lửa nhưng tuyệt đối không bao giờ phát triển thành khối u ác tính! Axolotl sở hữu khả năng kháng ung thư tự nhiên gần như tuyệt đối, trở thành hình mẫu vàng cho các nhà nghiên cứu y học di truyền thế giới! Cơ chế kiểm soát chu kỳ tế bào nghiêm ngặt đến mức ngay cả khi các nhà khoa học cố tình tiêm các hoạt chất gây ung thư cực mạnh, cơ thể Axolotl vẫn tự động đào thải và tái tạo lại mô tế bào khỏe mạnh bình thường!
```
**Part 2** → `audio/vs/scene07_p2.wav` (124 ký tự) · mood `hao_hung`

```text
Mười điểm cho sự kỳ diệu của bộ gen Axolotl! Nhưng ngay lập tức, Sứa Bất Tử bay lơ lửng bước vào vòng đo lường gen telomere!
```
**Part 3** → `audio/vs/scene07_p3.wav` (779 ký tự) · mood `don_dap`

```text
Năm hai ngàn không trăm hai mươi hai, một nhóm nghiên cứu tại đại học Oviedo Tây Ban Nha đã công bố bản giải mã di truyền của Sứa Bất Tử trên kỷ yếu Viện Hàn lâm Khoa học Quốc gia Hoa Kỳ! Họ phát hiện Sứa Bất Tử sở hữu số lượng gen nhân đôi gấp đôi ở các cụm gen chịu trách nhiệm bảo vệ và duy trì độ dài của telomere: chiếc nắp bảo vệ ở đầu mút nhiễm sắc thể! Mỗi khi cơ thể bị lão hóa, hệ enzym telomerase và cơ chế sửa chữa lỗi sao chép DNA tự động kích hoạt ở mức tối đa, xóa sạch mọi dấu vết già nua và tái thiết lập đồng hồ sinh học về số không! Một bộ gen bất tử thực thụ theo đúng nghĩa đen di truyền học! Chúng không chỉ sửa chữa DNA bị đứt gãy mà còn sao chép dự phòng hàng trăm bản sao gen chống stress oxy hóa, giúp tế bào luôn duy trì trạng thái thanh xuân vĩnh cửu!
```
**Part 4** → `audio/vs/scene07_p4.wav` (497 ký tự) · mood `tram_bi_an`

```text
Và không thể bỏ qua Ếch Lông Wolverine với lá chắn kháng sinh sinh học trên da suối xiết! Sau khi tự bẻ xương đâm rách toạc da chân để nghênh chiến, làm thế nào chú ếch này không bị nhiễm trùng huyết trong môi trường bùn lầy dơ bẩn? Các tuyến da của ếch đực tiết ra hàng loạt chuỗi peptide kháng khuẩn phổ rộng có khả năng tiêu diệt lập tức các loại nấm sát thủ và vi khuẩn gây hoại tử chỉ trong vài phút tiếp xúc! Nhờ vậy, vết rách tự lành thần tốc mà không cần đến một viên thuốc kháng sinh nào!
```
**Part 5** → `audio/vs/scene07_p5.wav` (617 ký tự) · mood `hao_hung`

```text
Bên cạnh bộ gen khổng lồ của Axolotl và Sứa, Bạch Tuộc Mimic cũng khiến các nhà di truyền học kinh ngạc với cơ chế chỉnh sửa ARN độc nhất vô nhị! Nghiên cứu công bố trên tạp chí Science năm hai ngàn mười bảy của nhóm tiến sĩ Eli Eisenberg phát hiện: loài bạch tuộc này không cần thay đổi chuỗi D-N-A gốc mà trực tiếp biên tập lại các phân tử ARN thông tin! Hơn sáu mươi phần trăm các bản phiên mã thần kinh của chúng được tái cấu trúc linh hoạt theo nhiệt độ nước và nồng độ oxy của môi trường! Một khả năng lập trình phần mềm sinh học theo thời gian thực vượt xa mọi hệ điều hành máy tính tinh vi nhất của nhân loại!
```
**Part 6** → `audio/vs/scene07_p6.wav` (524 ký tự) · mood `tram_bi_an`

```text
Và điều kỳ lạ nhất trong bộ gen của Cá Mút Đá Hagfish vừa được các nhà di truyền học đại học Tokyo làm sáng tỏ: hiện tượng đào thải D-N-A có lập trình trong tế bào soma! Khi Hagfish phát triển từ phôi thai thành cá thể trưởng thành, các tế bào cơ thể của chúng tự động loại bỏ tới hai mươi phần trăm lượng D-N-A không cần thiết trong nhân tế bào! Chúng chỉ giữ lại trọn vẹn toàn bộ bộ gen gốc trong các tế bào sinh dục mầm, giúp cơ thể tiết kiệm tối đa năng lượng sao chép và duy trì sự sống bền bỉ suốt hàng trăm triệu năm!
```
**Part 7** → `audio/vs/scene07_p7.wav` (470 ký tự) · mood `don_dap`

```text
Trong khi đó, hệ enzym sửa chữa D-N-A của Sứa Bất Tử hoạt động với độ chính xác tuyệt đối, loại bỏ tới chín mươi chín phẩy chín phần trăm các đột biến sai hỏng trong quá trình sao chép! Nhờ khả năng tự sửa lỗi di truyền liên tục này, Sứa Bất Tử không bao giờ tích lũy các đột biến gây thoái hóa hay lão hóa sớm như các sinh vật bậc cao khác! Một bí mật sinh học phi thường mà các nhà khoa học đang nỗ lực giải mã để áp dụng vào công nghệ kéo dài tuổi xuân cho con người!
```
**Part 8** → `audio/vs/scene07_p8.wav` (488 ký tự) · mood `don_dap`

```text
Bí mật đằng sau khả năng chữa lành không để lại sẹo của Axolotl nằm ở các cụm tế bào gốc blastema: chúng có thể biến đổi thành bất kỳ loại mô tế bào nào của cơ thể! Khi bị tổn thương, các đại thực bào của Axolotl dập tắt phản ứng viêm trong vài giờ, ngăn chặn triệt để sự hình thành mô xơ sẹo thường thấy ở động vật có vú! Còn enzyme telomerase của Sứa Bất Tử liên tục nối dài các đầu mút nhiễm sắc thể, giúp tế bào phân chia vĩnh viễn mà không bao giờ chạm tới giới hạn lão hóa Hayflick!
```
**Part 9** → `audio/vs/scene07_p9.wav` (369 ký tự) · 🎭 cameo `tham_phan`

```text
Ban giám khảo xin công bố bảng điểm Vòng năm! Huy chương Đồng thuộc về Ếch Lông Wolverine với lớp peptide kháng khuẩn tự chữa lành vết thương hở! Huy chương Bạc thuộc về Sứa Bất Tử với bộ gen bảo vệ telomere và xóa bỏ lão hóa tế bào! Và Huy chương Vàng ba điểm xứng đáng thuộc về Kỳ Nhông Axolotl với bộ gen ba mươi hai tỷ cặp base kháng ung thư và tái sinh mô thần kỳ!
```
**Part 10** → `audio/vs/scene07_p10.wav` (197 ký tự) · mood `hao_hung`

```text
Bảng tổng sắp sau năm vòng thi đấu tiếp tục bùng nổ dữ dội: Sứa Bất Tử và Axolotl cùng vươn lên chia sẻ vị trí dẫn đầu với năm điểm! Gấu Wombat cũng đồng hạng năm điểm! Hải Ly bám sát với bốn điểm!
```

### scene08 — NGƯỜI HÙNG BẢO VỆ SINH THÁI ĐẠI DƯƠNG & RỪNG XANH
*Thẻ chương:* NGƯỜI HÙNG BẢO VỆ SINH THÁI

*Badge:* `VÒNG 6: NGƯỜI HÙNG SINH THÁI` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene08_p0.wav` (393 ký tự) · mood `hao_hung`

```text
[surprise-oh] Tiến vào Vòng thi đấu thứ sáu: Người Hùng Bảo Vệ Hệ Sinh Thái Đại Dương và Rừng Xanh! Ở vòng thi này, chúng ta không nhìn vào sức mạnh cá nhân, mà đo lường đóng góp sinh thái vĩ đại mà các tuyển thủ âm thầm cống hiến cho hành tinh xanh! Mỗi sinh vật dù nhỏ bé hay mang vẻ ngoài kỳ dị đều nắm giữ một mắt xích sống còn, duy trì sự cân bằng mong manh của toàn bộ mạng lưới sự sống!
```
**Part 1** → `audio/vs/scene08_p1.wav` (437 ký tự) · mood `don_dap`

```text
Tuyển thủ bước lên sàn đầu tiên khiến tất cả bất ngờ: chú Hải Sâm lầy lội từng bị coi là kẻ lười biếng nhất đáy biển! Các nhà hải dương học tại đại học New South Wales đã công bố một báo cáo gây chấn động: Hải Sâm chính là chiếc máy hút bụi sinh học quan trọng bậc nhất của các rạn san hô nhiệt đới! Mỗi năm, quần thể hải sâm trên một cây số vuông đáy biển tiêu hóa và thanh lọc tới một trăm ba mươi tấn cát và trầm tích hữu cơ thối rữa!
```
**Part 2** → `audio/vs/scene08_p2.wav` (451 ký tự) · mood `don_dap`

```text
Quan trọng hơn thế, chất thải sau khi tiêu hóa của Hải Sâm chứa hàm lượng Canxi Cacbonat kiềm tính cực cao! Dòng chất kiềm tự nhiên này làm tăng độ pH của nước biển xung quanh, giúp trung hòa hiện tượng axit hóa đại dương do biến đổi khí hậu và bảo vệ san hô khỏi nguy cơ bị tẩy trắng hủy diệt! Các nhà khoa học tính toán: nếu loại bỏ hoàn toàn Hải Sâm khỏi một rạn san hô, tốc độ suy thoái của san hô sẽ tăng vọt gấp ba lần chỉ sau vài năm ngắn ngủi!
```
**Part 3** → `audio/vs/scene08_p3.wav` (281 ký tự) · mood `hao_hung`

```text
Không có Hải Sâm hút bụi và cân bằng độ pH, các rạn san hô lộng lẫy của hành tinh sẽ dần chết mòn thành bãi tha ma đá vôi! Cả khán đài nghiêng mình thán phục trước Hải Sâm! Tiếp theo, hãy cùng nhìn lên các con đập của Hải Ly: chiếc bẫy lưu giữ carbon tự nhiên khổng lồ của lục địa!
```
**Part 4** → `audio/vs/scene08_p4.wav` (627 ký tự) · mood `don_dap`

```text
Các nhà sinh thái học phát hiện: lớp trầm tích giàu hữu cơ đọng lại phía sau những con đập của Hải Ly lưu giữ hàng triệu tấn carbon hữu cơ, ngăn không cho chúng thoát vào khí quyển! Nhờ có vùng ngập nước của Hải Ly, độ đa dạng sinh học của các loài chim di cư, cá nước ngọt và động vật lưỡng cư tăng vọt tới ba mươi ba phần trăm so với các dòng suối thông thường! Hải Ly không chỉ xây nhà cho mình, chúng xây dựng cả một thiên đường sinh thái nuôi dưỡng muôn loài! Những vùng đất ngập nước này duy trì dòng chảy mát mẻ vào mùa hè và ngăn lũ quét vào mùa mưa bão, trở thành tấm khiên phòng hộ tự nhiên vô giá của lục địa Bắc Mỹ!
```
**Part 5** → `audio/vs/scene08_p5.wav` (589 ký tự) · mood `tram_bi_an`

```text
Và cuối cùng là đóng góp âm thầm của cụ tổ Cá Mút Đá Hagfish dưới đáy vực sâu một ngàn mét lạnh giá! Khi xác cá voi chìm xuống vùng biển sâu không có ánh sáng, hàng ngàn con Hagfish sẽ vùi mình vào xác thịt, hấp thụ chất dinh dưỡng trực tiếp qua da và tiêu hóa sạch sẽ các mô mỡ thối rữa! Họ phân giải và hoàn trả nguồn nitơ và phốt-pho quý giá trở lại chuỗi thức ăn đáy biển, nuôi sống cả một quần xã sinh vật biển sâu tăm tối suốt hàng chục năm ròng! Nếu không có đội dọn dẹp Hagfish, đáy biển sâu sẽ bị ngạt thở bởi lớp chất béo tích tụ, cắt đứt chu trình tuần hoàn dinh dưỡng toàn cầu!
```
**Part 6** → `audio/vs/scene08_p6.wav` (532 ký tự) · mood `hao_hung`

```text
Không chỉ có Hải Sâm và Hải Ly, Gấu Túi Wombat và Ếch Wolverine cũng đóng góp những mắt xích sinh thái vô giá cho lục địa của mình! Những viên phân hình lập phương của Wombat chứa đầy các hạt giống cỏ bản địa và hàng tỷ bào tử nấm rễ cộng sinh mycorrhiza! Khi phân rã, chúng làm tơi xốp các tầng đất cằn cỗi và giữ nước ngầm cho thảo nguyên khô hạn nước Úc sau các đợt hạn hán kéo dài! Còn Ếch Lông Wolverine là loài săn mồi đầu bảng kiểm soát mật độ ấu trùng muỗi vằn và ruồi đen truyền bệnh dịch ở các dòng suối nhiệt đới Tây Phi!
```
**Part 7** → `audio/vs/scene08_p7.wav` (450 ký tự) · mood `don_dap`

```text
Ở trên các tầng tán rừng nhiệt đới, Kiến Nổ Cảm Tử cũng đóng vai trò là những vệ sĩ sinh thái bảo vệ sức khỏe cho các cây cổ thụ nguyên sinh! Chúng tiêu diệt sạch sẽ các loài sâu róm phá hoại lá non và ngăn chặn các loài rệp sáp hút nhựa cây xâm lấn, duy trì sự xanh tốt cho tán rừng nhiệt đới đại ngàn! Sự hy sinh của từng cá thể kiến thợ không chỉ bảo vệ tổ ấm, mà gián tiếp gìn giữ lá phổi xanh khổng lồ cho toàn bộ hệ sinh thái rừng mưa xích đạo!
```
**Part 8** → `audio/vs/scene08_p8.wav` (335 ký tự) · mood `don_dap`

```text
Các nhà khoa học ước tính: lượng Canxi Cacbonat kiềm tính mà quần thể Hải Sâm bài tiết ra ngoài có thể bù đắp lại tới hai mươi phần trăm lượng vôi hóa bị mất đi của rạn san hô do biến đổi khí hậu! Chúng hoạt động như những người thợ hồ cần mẫn trát từng lớp vữa kiềm bảo vệ pháo đài san hô trước sự bào mòn của dòng nước biển axit hóa!
```
**Part 9** → `audio/vs/scene08_p9.wav` (461 ký tự) · mood `hao_hung`

```text
Trong các trận đại hỏa hoạn cháy rừng lịch sử tại nước Úc, hệ thống hầm ngầm của Wombat đã trở thành pháo đài cứu mạng cho hàng ngàn sinh vật bé nhỏ! Chim chóc, thú có túi nhỏ, thằn lằn và ếch nhái đều chạy vào nương náu trong các ngóc ngách hầm Wombat mát mẻ với nhiệt độ luôn duy trì ổn định hai mươi độ C! Wombat không hề xua đuổi những kẻ tị nạn bất đắc dĩ, chúng hào hiệp chia sẻ lãnh thổ ngầm, trở thành người hùng cứu sinh thầm lặng của châu Úc hoang dã!
```
**Part 10** → `audio/vs/scene08_p10.wav` (320 ký tự) · 🎭 cameo `tham_phan`

```text
Ban giám khảo xin tuyên bố kết quả Vòng sáu! Huy chương Đồng thuộc về Cá Mút Đá Hagfish với vai trò dọn sạch xác cá đáy vực sâu! Huy chương Bạc thuộc về kỹ sư Hải Ly với bẫy carbon và chiếc nôi nâng đỡ đa dạng sinh thái! Và Huy chương Vàng ba điểm vô cùng xứng đáng thuộc về chiếc máy hút bụi bảo vệ rạn san hô: Hải Sâm!
```
**Part 11** → `audio/vs/scene08_p11.wav` (184 ký tự) · mood `hao_hung`

```text
Bảng điểm sau sáu vòng đấu cực kỳ gay cấn và biến ảo: Hải Ly vươn lên đồng hạng sáu điểm cùng Wombat! Sứa Bất Tử và Axolotl bám sát với năm điểm! Hải Sâm bứt phá ngoạn mục lên ba điểm!
```

### scene09 — CÁC CỤ TỔ CỔ ĐẠI 300 TRIỆU NĂM & TỔ TIÊN KHỔNG LỒ
*Thẻ chương:* CÁC CỤ TỔ CỔ ĐẠI & TỔ TIÊN KHỔNG LỒ

*Badge:* `GIẢI THƯỞNG PHỤ: CỤ TỔ CỔ ĐẠI` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene09_p0.wav` (504 ký tự) · mood `hao_hung`

```text
[surprise-oh] Trước khi bước vào hai vòng đấu cuối cùng, ban tổ chức xin trân trọng giới thiệu: Lễ Trao Giải Phụ Đặc Biệt — Tri Ân Các Cụ Tổ Cổ Đại và Tổ Tiên Khổng Lồ! Để có mặt trên sàn đấu Mùa ba ngày hôm nay, mười dòng giống dị nhân đã phải trải qua hàng trăm triệu năm đấu tranh sinh tồn trước thiên thạch và các kỷ băng hà khốc liệt! Những mẫu hóa thạch khai quật từ các tầng địa chất sâu thẳm đã chứng minh: các dị nhân của chúng ta từng sở hữu những phiên bản tổ tiên hoành tráng đến mức khó tin!
```
**Part 1** → `audio/vs/scene09_p1.wav` (857 ký tự) · mood `don_dap`

```text
Tấm cúp danh dự đầu tiên thuộc về cụ tổ không xương sống: Cá Mút Đá Hagfish! Năm hai ngàn mười chín, các nhà cổ sinh vật học tại Canada đã phát hiện hóa thạch của loài Tethymyxine có niên đại ba trăm triệu năm từ kỷ Than Đá! Điều kinh ngạc là cấu trúc cơ thể của Hagfish ba trăm triệu năm trước giống hệt với Hagfish đang bơi lội ngày hôm nay! Chúng đã sống sót qua bốn cuộc đại tuyệt chủng hàng loạt của Trái Đất, chứng kiến loài khủng long bạo chúa T-Rex xuất hiện rồi biến mất hoàn toàn, trong khi Hagfish vẫn ung dung thắt nút thân số tám dưới đáy biển! Chưa hết, Hagfish sở hữu tới bốn quả tim độc lập rải rác khắp cơ thể: một tim chính và ba tim phụ tự đập hàng giờ mà không cần oxy từ não bộ! Hệ tuần hoàn phụ này giúp chúng sống sót ngon lành trong những vùng nước đáy biển thiếu oxy đến mức mọi loài cá có xương sống khác đều phải ngạt thở bỏ mạng!
```
**Part 2** → `audio/vs/scene09_p2.wav` (264 ký tự) · mood `hao_hung`

```text
Một cỗ máy sinh học bất tử trước thời gian! Cả hội trường đồng loạt cúi đầu kính cẩn chào cụ tổ Hagfish! Nhưng hãy nhìn sang tổ tiên của hai gã thợ mộc và đào hầm: Hải Ly và Wombat! Họ từng sở hữu những phiên bản quái thú khổng lồ khiến ai nhìn cũng phải khiếp sợ!
```
**Part 3** → `audio/vs/scene09_p3.wav` (597 ký tự) · mood `don_dap`

```text
Trong kỷ băng hà Bắc Mỹ cách đây mười ngàn năm, tổ tiên của Hải Ly là loài Castoroides nặng tới một trăm ki-lô-gam, to lớn ngang ngửa một chú gấu đen khổng lồ! Tuy nhiên, điều bi hài là chú hải ly khổng lồ này lại không biết xây đập và chỉ thích ăn cỏ dại dưới nước, nên đã bị tuyệt chủng khi khí hậu biến đổi! Còn ở nước Úc, tổ tiên của Wombat là loài quái thú Diprotodon: loài thú có túi lớn nhất từng bước đi trên Trái Đất, nặng tới gần ba tấn và dài hơn ba mét! Chiếc mông bọc thép của Wombat ngày nay chính là di sản thu nhỏ được kế thừa từ cỗ xe tăng bọc thép Diprotodon ba tấn thời tiền sử!
```
**Part 4** → `audio/vs/scene09_p4.wav` (451 ký tự) · mood `tram_bi_an`

```text
Và giải thưởng danh dự cuối cùng thuộc về dòng dõi của Hải Sâm: sinh vật đã có mặt trên Trái Đất từ kỷ Cambri cách đây hơn năm trăm triệu năm! Năm trăm triệu năm trước, khi sinh vật trên cạn còn chưa kịp hình thành, tổ tiên của Hải Sâm đã cặm cụi hút bụi lọc sạch cát biển cho hành tinh chúng ta! Họ đã chứng kiến sự thăng trầm của hàng vạn loài sinh vật, bình thản vượt qua mọi biến cố địa chất vĩ đại bằng triết lý lầy lội không xương sống của mình!
```
**Part 5** → `audio/vs/scene09_p5.wav` (579 ký tự) · mood `hao_hung`

```text
Và nhìn vào cây phả hệ của Sứa Bất Tử, dòng giống ruột khoang Cnidaria của chúng thậm chí đã xuất hiện từ kỷ Ediacara cách đây hơn sáu trăm triệu năm! Sáu trăm triệu năm trước, khi Trái Đất chỉ là một quả cầu băng tuyết lạnh giá bao phủ khắp các đại dương, tổ tiên của loài sứa đã trôi dạt lơ lửng dưới lớp băng dày! Họ đã vượt qua cuộc đại tuyệt chủng Permi-Triat thảm khốc nhất lịch sử khi chín mươi lăm phần trăm sinh vật biển bị quét sạch hoàn toàn! Sự trường sinh của Sứa Bất Tử không chỉ nằm ở từng cá thể, mà là sự kiên cường của cả một dòng dõi cổ xưa bậc nhất hành tinh!
```
**Part 6** → `audio/vs/scene09_p6.wav` (509 ký tự) · mood `don_dap`

```text
Còn nhìn về phả hệ của Kỳ Nhông Axolotl, chúng là hậu duệ trực tiếp của nhóm lưỡng cư cổ đại Temnospondyli từng thống trị Trái Đất từ ba trăm triệu năm trước! Vào thời kỳ khủng long còn chưa xuất hiện, những cụ tổ lưỡng cư khổng lồ này đã làm chủ các đầm lầy than đá bằng khả năng tái sinh chi và thích nghi môi trường nước ngọt đỉnh cao! Trải qua hàng trăm triệu năm tiến hóa thu nhỏ lại thành chú kỳ nhông bảy mươi gam xinh xắn, Axolotl vẫn lưu giữ trọn vẹn chiếc chìa khóa tái sinh cổ đại của tổ tiên mình!
```
**Part 7** → `audio/vs/scene09_p7.wav` (369 ký tự) · mood `don_dap`

```text
Thậm chí trong các lớp đá trầm tích kỷ Than Đá, người ta còn tìm thấy những dấu vết hóa thạch của chất keo nhớt Hagfish được bảo tồn nguyên vẹn qua ba trăm triệu năm thời gian! Điều này chứng minh rằng công thức phân tử của sợi tơ protein Hagfish hoàn hảo đến mức mẹ thiên nhiên không cần phải chỉnh sửa hay nâng cấp thêm bất kỳ chi tiết nào suốt ba trăm triệu năm qua!
```
**Part 8** → `audio/vs/scene09_p8.wav` (441 ký tự) · mood `don_dap`

```text
Không chỉ vậy, Cá Mút Đá Hagfish còn có thể sống sót kỳ diệu suốt ba mươi sáu giờ trong môi trường hoàn toàn không có khí oxy dưới lớp bùn đáy biển sâu! Chúng chuyển hóa lượng đường glycogen dự trữ trong các mô cơ mà không cần oxy, giữ cho bốn quả tim vẫn hoạt động nhịp nhàng qua cơn thiếu thốn! Đó là minh chứng cho sức sống bền bỉ đã giúp Hagfish vượt qua năm đại tuyệt chủng lớn nhất của lịch sử Trái Đất mà không cần biến đổi hình dạng!
```
**Part 9** → `audio/vs/scene09_p9.wav` (152 ký tự) · 🎭 cameo `tham_phan`

```text
Ban tổ chức xin trao tặng Cúp Vinh Danh Cổ Vật Sống Danh Dự cho Cá Mút Đá Hagfish và Hải Sâm! Một tràng pháo tay cho sự trường tồn vĩ đại của muôn loài!
```
**Part 10** → `audio/vs/scene09_p10.wav` (149 ký tự) · mood `hao_hung`

```text
Lễ trao giải phụ khép lại trong niềm tự hào vô bờ bến! Bây giờ, hãy hít một hơi thật sâu vì chúng ta sắp bước vào Vòng bảy: Phúc Khảo Tin Đồn Thế Kỷ!
```

### scene10 — PHÚC KHẢO TIN ĐỒN THẾ KỶ & ĐẬP TAN NHỮNG LẦM TƯỞNG
*Thẻ chương:* PHÚC KHẢO TIN ĐỒN THẾ KỶ

*Badge:* `VÒNG 7: PHÚC KHẢO TIN ĐỒN` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene10_p0.wav` (435 ký tự) · mood `hao_hung`

```text
[surprise-oh] Đèn sân khấu đổi màu rực rỡ! Chào mừng quý vị đến với Vòng bảy: Phúc Khảo Tin Đồn Thế Kỷ và Đập Tan Những Lầm Tưởng! Đây là vòng thi nơi ban giám khảo sẽ đưa ra hàng loạt tin đồn nổi tiếng trên mạng xã hội về mười tuyển thủ để đối chất bằng khoa học thực nghiệm! Trong thời đại thông tin bùng nổ, nhiều sinh vật bị đồn thổi thành những vị thần bất khả chiến bại hoặc bị gán cho những thói quen ăn uống hoàn toàn sai lệch!
```
**Part 1** → `audio/vs/scene10_p1.wav` (864 ký tự) · mood `don_dap`

```text
Tin đồn số một: Sứa Bất Tử là sinh vật trường sinh bất lão tuyệt đối, không có bất kỳ thứ gì trên đời có thể tiêu diệt được chúng?! Sự thật khoa học là gì? Bà Cú giám khảo lập tức gõ búa đính chính: Sứa Bất Tử chỉ bất tử về mặt lão hóa sinh học tự nhiên mà thôi! Trong môi trường biển khơi, kích thước chỉ bốn phẩy năm mi-li-mét biến chúng thành món tráng miệng khoái khẩu tuyệt vời cho rùa biển, cá mặt trăng và các loài sứa lớn khác! Hơn nữa, nếu gặp một đợt sóng thần đánh dạt lên bãi cát khô nóng hoặc bị nhiễm khuẩn nấm đại dương, chú sứa bất tử này vẫn sẽ hóa thành một vũng nước khô queo trên bờ biển! Khái niệm bất tử ở đây là không chết vì tuổi già, chứ không phải là mình đồng da sắt chống lại kẻ săn mồi! [laughter] Nếu không có chuỗi thức ăn kiểm soát số lượng, chỉ sau vài năm loài sứa bất tử này có thể nhân bản tràn ngập mọi đại dương trên Trái Đất!
```
**Part 2** → `audio/vs/scene10_p2.wav` (139 ký tự) · mood `hao_hung`

```text
Một pha bẻ lái định nghĩa khoa học cực kỳ chuẩn xác! Tiếp tục với tin đồn số hai: Hải Ly là loài động vật kỳ quặc thích ăn gỗ mục để sống?!
```
**Part 3** → `audio/vs/scene10_p3.wav` (605 ký tự) · mood `don_dap`

```text
Đây là một sự hiểu lầm tai hại lớn nhất về loài Hải Ly! Đường ruột của Hải Ly hoàn toàn không thể tiêu hóa được phần gỗ lõi cứng chắc của thân cây! Khẩu phần ăn thật sự của chúng là lớp mô mềm màu xanh giàu đường và dinh dưỡng nằm ngay sát dưới lớp vỏ cây, cùng với chồi non và lá cây tươi! Những khúc gỗ cứng cáp bị đốn ngã chỉ được Hải Ly tận dụng làm vật liệu xây dựng con đập kiên cố ngăn dòng nước lũ, chứ không phải thức ăn trong thực đơn hàng ngày! Chúng ta đã oan uổng gán cho Hải Ly cái mác thèm ăn gỗ suốt hàng thế kỷ qua, trong khi chúng chỉ là những người sành ăn vỏ cây dinh dưỡng! [laughter]
```
**Part 4** → `audio/vs/scene10_p4.wav` (715 ký tự) · mood `tram_bi_an`

```text
Đến tin đồn số ba: Ếch Wolverine tự bẻ xương xuyên qua thịt chân như vậy thì có cảm thấy đau đớn đến thấu xương hay không? Các nhà thần kinh học động vật xác nhận: loài ếch này có đầy đủ các thụ thể cảm nhận đau đớn nociceptor dưới da! Tuy nhiên, trong khoảnh khắc cận kề cái chết trước kẻ thù, tuyến thượng thận của chúng lập tức giải phóng một lượng khổng lồ hormone adrenaline và các peptit giảm đau nội sinh! Cơ chế này tạm thời gây tê liệt cảm giác đau đớn cục bộ, giúp chú ếch tập trung trọn vẹn một trăm phần trăm sức lực để tung đòn móng vuốt sinh tử hạ gục kẻ săn mồi! Và sau khi hiểm nguy qua đi, cảm giác ê ẩm xuất hiện chính là tín hiệu kích hoạt chu trình tiết dịch kháng khuẩn làm lành mô da thần tốc!
```
**Part 5** → `audio/vs/scene10_p5.wav` (627 ký tự) · mood `hao_hung`

```text
Thêm một tin đồn nổi tiếng khác về Bạch Tuộc Mimic: liệu chúng có thật sự nhận thức được mình đang bắt chước loài nào hay chỉ là phản xạ đổi màu ngẫu nhiên? Các thí nghiệm của tiến sĩ Mark Norman tại Indonesia đã chứng minh: Bạch Tuộc Mimic sở hữu trí nhớ thị giác và tư duy phân tích chiến thuật đỉnh cao! Chúng quan sát chính xác đối thủ đang tiếp cận là ai, nhớ lại kẻ thù tự nhiên của đối thủ đó trong tự nhiên, rồi mới quyết định hóa thân thành loài khắc chế phù hợp nhất! Một sự tính toán chiến thuật hoàn toàn chủ động chứ không hề là phản xạ vô thức may rủi! Cả khán đài gật gù khâm phục trí tuệ loài động vật thân mềm!
```
**Part 6** → `audio/vs/scene10_p6.wav` (511 ký tự) · mood `don_dap`

```text
Và một tin đồn thú vị khác về Gấu Wombat: có phải chúng dùng hai chân sau để nặn phân thành hình khối lập phương hay không? [laughter] Bà Cú giám khảo cười lớn đính chính: hoàn toàn không phải do nặn bằng tay hay chân! Đó là một trăm phần trăm kết quả của cơ chế thủy lực và áp suất đường ruột tự nhiên! Phân của Wombat đi vào đoạn ruột già ở thể lỏng sệt, và qua quá trình hút nước cực mạnh kết hợp lực co bóp đàn hồi không đều, chúng tự động đông cứng thành các khối hộp vuông vức hoàn hảo trước khi ra ngoài!
```
**Part 7** → `audio/vs/scene10_p7.wav` (343 ký tự) · mood `don_dap`

```text
Và sự thật về chiếc móng vuốt của Ếch Wolverine: xương ngón chân tự bẻ gãy không hề làm đứt gãy mạch máu lớn hay gây hoại tử nhờ một lớp vỏ bọc collagen dạng sợi cực kỳ dẻo dai! Khi móng vuốt thụt vào, lớp vỏ này đóng vai trò như một chiếc băng gạc sinh học ép chặt vết rách, ngăn chặn máu chảy và kích thích tế bào biểu mô phân chia thần tốc!
```
**Part 8** → `audio/vs/scene10_p8.wav` (412 ký tự) · mood `don_dap`

```text
Viện nghiên cứu sinh học quốc tế cũng xác nhận: chất nhầy của Hagfish khi sấy khô có thể dệt thành sợi tơ nhân tạo bền gấp mười lần sợi nylon tổng hợp! Sợi tơ sinh học này có khả năng tự phân hủy hoàn toàn trong môi trường tự nhiên, mở ra cuộc cách mạng thời trang xanh không rác thải nhựa! Thiên nhiên đã trao tặng cho những dị nhân này những giải pháp sinh học đi trước công nghệ con người hàng trăm triệu năm!
```
**Part 9** → `audio/vs/scene10_p9.wav` (360 ký tự) · 🎭 cameo `tham_phan`

```text
Ban giám khảo xin công bố kết quả Vòng bảy! Huy chương Đồng thuộc về Kỳ Nhông Axolotl với bí ẩn trạng thái ấu trùng neoteny suốt đời! Huy chương Bạc thuộc về kỹ sư Hải Ly với lời minh oan đanh thép cho khẩu phần ăn vỏ cây dinh dưỡng! Và Huy chương Vàng ba điểm xuất sắc thuộc về Sứa Bất Tử với bài học phân biệt giữa bất tử sinh học và chuỗi thức ăn đại dương!
```
**Part 10** → `audio/vs/scene10_p10.wav` (176 ký tự) · mood `hao_hung`

```text
Bảng tổng sắp sau bảy vòng đấu chính thức đã chứng kiến sự bứt phá ngoạn mục: Sứa Bất Tử và Hải Ly cùng dẫn đầu với tám điểm! Gấu Wombat bám sát với năm điểm! Axolotl sáu điểm!
```

### scene11 — THÍ NGHIỆM TƯƠNG LAI
*Thẻ chương:* PHÒNG THÍ NGHIỆM TƯƠNG LAI

*Badge:* `BÁN KẾT: PHÒNG THÍ NGHIỆM` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene11_p0.wav` (413 ký tự) · mood `hao_hung`

```text
[surprise-oh] Căng thẳng tột cùng! Chào mừng quý vị đến với Vòng Bán Kết: Soi Kính Hiển Vi Điện Tử và Máy Gia Tốc Hạt Đồng Bộ! Đây là vòng thi nơi khoa học đỉnh cao của con người dùng các thiết bị đắt giá hàng triệu đô la để vén màn những kết cấu vật liệu vi mô không tưởng! Những bí mật cấu trúc tinh thể nano ẩn sâu trong tế bào các dị nhân chính là nguồn cảm hứng vô tận cho cuộc cách mạng công nghệ tương lai!
```
**Part 1** → `audio/vs/scene11_p1.wav` (714 ký tự) · mood `don_dap`

```text
Mẫu thử nghiệm đầu tiên được đưa vào buồng chân không: sợi tơ nhớt protein của Cá Mút Đá Hagfish! Dưới chùm tia X cực mạnh của máy gia tốc hạt, các nhà nghiên cứu vật liệu tại đại học Guelph đã phát hiện ra cấu trúc tinh thể siêu việt của sợi tơ này! Bên trong mỗi tế bào nhớt chứa một cuộn tơ dài tới mười lăm xăng-ti-mét nhưng được quấn tròn thành một viên nang nhỏ chỉ một trăm micro-mét! Khi bung ra trong nước biển, các chuỗi axit amin kỵ nước lập tức hút chặt lấy nhau, biến thể lỏng thành thể gel siêu đàn hồi có thể kéo dài gấp ba lần mà không hề bị đứt gãy! Độ bền kéo của sợi tơ này đạt mức một trăm tám mươi megapascal, tương đương với độ bền của các sợi gân nhân tạo tốt nhất mà con người từng chế tạo!
```
**Part 2** → `audio/vs/scene11_p2.wav` (174 ký tự) · mood `hao_hung`

```text
Một kỳ quan công nghệ nano của biển sâu có tuổi đời ba trăm triệu năm! Cả hội trường vỗ tay rầm rộ! Tiếp theo, hãy đưa lớp da của Hải Sâm vào máy thử nghiệm cơ học biến dạng!
```
**Part 3** → `audio/vs/scene11_p3.wav` (710 ký tự) · mood `don_dap`

```text
Các nhà sinh học phát hiện: da của Hải Sâm được cấu tạo từ một loại mô liên kết biến đổi đặc biệt gọi tắt là M-T-C! Hải Sâm không hề sử dụng cơ bắp hay tiêu tốn năng lượng A-T-P để gồng cứng cơ thể như các loài động vật thông thường! Thay vào đó, các tế bào thần kinh chỉ cần tiết ra một lượng nhỏ phân tử điều hòa để khóa chặt hoặc tháo rời các cầu nối giữa các sợi collagen trong vài trăm mili-giây! Và khi cần thoát thân qua khe đá hẹp, các cầu nối tự bung ra, toàn bộ cơ thể Hải Sâm hóa lỏng mềm nhũn như một khối thạch rau câu trôi tuột qua kẽ hở! Các kỹ sư y sinh đang ứng dụng cơ chế hóa lỏng này để chế tạo các điện cực cấy ghép não bộ: mềm dẻo khi luồn vào mô não nhưng cứng cáp khi định vị chính xác!
```
**Part 4** → `audio/vs/scene11_p4.wav` (385 ký tự) · mood `tram_bi_an`

```text
Và cuối cùng là màn soi siêu vi cơ quan Eimer trên chiếc mũi sao của Chuột Chũi! Mỗi chiếc nhú Eimer hình nấm tí hon chứa một cụm đầu dây thần kinh Merkel cực kỳ tinh vi, có thể nhận biết sự biến dạng bề mặt đất chỉ ở mức... một nanomet! Một nanomet nhỏ hơn cả đường kính của chuỗi xoắn kép D-N-A! Chuột Chũi Mũi Sao không chỉ sờ thấy con mồi, chúng sờ thấy cả kết cấu phân tử của đất!
```
**Part 5** → `audio/vs/scene11_p5.wav` (442 ký tự) · mood `hao_hung`

```text
Để kiểm tra độ bền của chiếc mông bọc thép Wombat, ban giám khảo đã đưa tấm khiên sụn vào máy thử nghiệm búa tạ thủy lực công nghiệp! Rầm! Chiếc búa nảy ngược trở lại trong khi lớp sụn mô mạc sợi của Wombat chỉ lún nhẹ xuống rồi lập tức đàn hồi trở lại hình dáng ban đầu không hề nứt vỡ! Các kỹ sư chế tạo xe hơi bọc thép và mũ bảo hiểm phi hành gia đang nghiên cứu cấu trúc sụn đan sợi này để phát triển vật liệu hấp thụ xung lực thế hệ mới!
```
**Part 6** → `audio/vs/scene11_p6.wav` (508 ký tự) · mood `don_dap`

```text
Tại phòng thí nghiệm công nghệ sinh học, các nhà khoa học đã dùng protein phát quang xanh lá cây G-F-P để theo dõi đường đi của từng tế bào tái sinh trong cơ thể Axolotl! Họ phát hiện một tín hiệu điều khiển thần kỳ: các tế bào thần kinh ngoại biên liên tục phát ra dòng điện sinh học vi mô dẫn đường cho các tế bào cơ di chuyển chính xác đến từng micromet! Công nghệ lập bản đồ tế bào này đang mở ra hướng đi đột phá trong việc chế tạo các chi giả sinh học thông minh kết nối trực tiếp với não bộ con người!
```
**Part 7** → `audio/vs/scene11_p7.wav` (372 ký tự) · mood `don_dap`

```text
Máy đo phổ tán xạ tia X còn cho thấy: các sợi tơ Hagfish có thể tự sắp xếp lại cấu trúc tinh thể khi chịu lực kéo giật đột ngột, biến lực kéo nguy hiểm thành nhiệt lượng khuếch tán ra môi trường nước! Khả năng hấp thụ xung lực tuyệt đỉnh này chính là chìa khóa vàng giúp chiếc bẫy nhớt Hagfish không bao giờ bị xé rách bởi những cú giãy giụa điên cuồng của cá mập săn mồi!
```
**Part 8** → `audio/vs/scene11_p8.wav` (431 ký tự) · mood `hao_hung`

```text
Cuộc chạm trán nảy lửa giữa công nghệ tái sinh của Axolotl và cơ chế đảo ngược thời gian của Sứa Bất Tử đã làm nổ tung cầu trường! Một bên là khả năng mọc lại mô tạng thần tốc chỉ sau vài tuần ngắn ngủi, một bên là thuật chuyển hóa tế bào đưa toàn bộ cơ thể trở về tuổi ấu thơ! Các nhà khoa học trên khán đài không ngừng ghi chép dữ liệu, đây chính là hai chìa khóa vàng mở toang cánh cửa chữa lành bách bệnh cho nhân loại mai sau!
```
**Part 9** → `audio/vs/scene11_p9.wav` (355 ký tự) · 🎭 cameo `tham_phan`

```text
Ban giám khảo xin công bố bảng điểm Vòng Bán Kết! Huy chương Đồng thuộc về Chuột Chũi Mũi Sao với cảm biến xúc giác nhạy tới một nanomet! Huy chương Bạc thuộc về Hải Sâm với mô liên kết biến đổi M-T-C tự hóa lỏng cơ thể không tốn năng lượng! Và Huy chương Vàng ba điểm xuất sắc thuộc về cụ tổ Cá Mút Đá Hagfish với kiến trúc tinh thể tơ protein siêu việt!
```
**Part 10** → `audio/vs/scene11_p10.wav` (211 ký tự) · mood `hao_hung`

```text
Bảng điểm sau vòng Bán Kết tạo nên một cơn địa chấn chưa từng có: Sứa Bất Tử và Hải Ly cùng dẫn đầu với tám điểm! Hagfish bứt phá thần tốc lên sáu điểm ngang hàng với Axolotl! Wombat và Hải Sâm cùng có năm điểm!
```

### scene12 — MÓN QUÀ CHO NHÂN LOẠI — CÔNG NGHỆ TƯƠNG LAI ĐỘT PHÁ (ĐIỂM NHÂN ĐÔI)
*Thẻ chương:* MÓN QUÀ CHO NHÂN LOẠI — ĐIỂM NHÂN ĐÔI

*Badge:* `CHUNG KẾT: MÓN QUÀ CHO NHÂN LOẠI` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene12_p0.wav` (611 ký tự) · mood `hao_hung`

```text
[surprise-oh] Giờ khắc lịch sử đã điểm! Toàn thể đấu trường nín thở chào đón Vòng Chung Kết: Món Quà Cho Nhân Loại và Những Đột Phá Công Nghệ Tương Lai! Đây là vòng thi quyết định số phận chiếc vương miện tối cao: Huy chương Đồng được hai điểm, Huy chương Bạc bốn điểm, và Huy chương Vàng lên tới sáu điểm tròn! Ở vòng đấu này, chúng ta đánh giá tiềm năng ứng dụng thực tiễn của mười tuyển thủ trong việc giải cứu y học, công nghệ và tương lai của loài người! Không phải danh hiệu hão huyền, những món quà tiến hóa mà muôn loài trao tặng cho nền văn minh nhân loại chính là giá trị bất tử đích thực của sự sống!
```
**Part 1** → `audio/vs/scene12_p1.wav` (596 ký tự) · mood `don_dap`

```text
Ứng cử viên đầu tiên tiến vào vòng đánh giá: cụ tổ Cá Mút Đá Hagfish với cuộc cách mạng vật liệu sinh thái! Hiện nay, sợi Kevlar dùng để may áo giáp chống đạn quân sự được sản xuất từ dầu mỏ với quy trình hóa học độc hại và đắt đỏ. Nhưng tơ của Hagfish hoàn toàn có thể tự tổng hợp bằng vi khuẩn lên men sinh học, tạo ra các tấm giáp chống đạn nhẹ hơn một nửa, dai gấp mười lần và hoàn toàn tự phân hủy sinh học trong môi trường tự nhiên! Hơn thế nữa, gel nhớt của Hagfish đang được nghiên cứu làm chất chữa cháy khẩn cấp cho các đám cháy giàn khoan dầu ngoài khơi nhờ khả năng ngậm nước cực lớn!
```
**Part 2** → `audio/vs/scene12_p2.wav` (166 ký tự) · mood `hao_hung`

```text
Một giải pháp vật liệu xanh hoàn hảo cho tương lai quốc phòng và môi trường! Nhưng hãy nhìn sang Kỳ Nhông Axolotl với chiếc chìa khóa vàng của y học tái tạo mô người!
```
**Part 3** → `audio/vs/scene12_p3.wav` (690 ký tự) · mood `don_dap`

```text
Mỗi năm trên thế giới có hàng triệu bệnh nhân chịu cảnh tàn phế do đột quỵ tim hoặc chấn thương đứt tủy sống không thể phục hồi. Các nhà nghiên cứu tại Viện Max Planck Đức đã phân lập được các yếu tố sinh trưởng tế bào mầm chi từ Axolotl! Khi ứng dụng các tín hiệu phân tử này vào tế bào người, các nhà khoa học đã thành công trong việc kích thích tế bào cơ tim người tự phân chia bù đắp vào vùng mô tim bị hoại tử sau cơn nhồi máu! Axolotl đang thắp lên hy vọng có thật về một ngày con người có thể tự mọc lại các ngón tay và chữa lành hoàn toàn các chấn thương cột sống! Đây không còn là khoa học viễn tưởng, mà là lộ trình y học tái sinh có thể trở thành hiện thực trong vài thập kỷ tới!
```
**Part 4** → `audio/vs/scene12_p4.wav` (747 ký tự) · mood `tram_bi_an`

```text
Và cuối cùng, chiếc ly thủy tinh nhỏ xíu của Sứa Bất Tử bay vút lên giữa trung tâm sân vận động! Căn bệnh đáng sợ nhất của nhân loại không phải là vi khuẩn hay virus, mà chính là sự thoái hóa và lão hóa không thể đảo ngược của các tế bào não trong bệnh Alzheimer và Parkinson! Nhưng cơ chế chuyển biệt hóa tế bào của Sứa Bất Tử đã chứng minh một chân lý vĩ đại: tế bào hoàn toàn có thể được tái lập trình trở lại trạng thái non trẻ ban đầu! Giải mã cơ chế telomerase của loài sứa bốn phẩy năm mi-li-mét này đang giúp các nhà khoa học mở ra kỷ nguyên mới của thuốc đảo ngược tuổi sinh học, trẻ hóa tế bào gốc và kéo dài tuổi thọ khỏe mạnh cho loài người! Một giấc mơ trường thọ không bệnh tật mà nhân loại hằng khao khát suốt hàng ngàn năm lịch sử!
```
**Part 5** → `audio/vs/scene12_p5.wav` (485 ký tự) · mood `hao_hung`

```text
Và một món quà bất ngờ khác đến từ Kiến Nổ Cảm Tử: chất keo dính phenolic tiết ra từ cơ thể chúng đang được các nhà dược học nghiên cứu làm keo dán vết mổ nội tạng sinh học! Loại keo này có khả năng đông kết tức thì ngay trong môi trường ẩm ướt đầy máu, dính chặt vết mổ mà không gây độc hại và tự tiêu biến sau khi mô cơ lành lặn! Từ một hành động tự hủy bảo vệ tổ, thiên nhiên đã trao tặng cho y học loài người một phương pháp cầm máu phẫu thuật đột phá cứu sống hàng ngàn sinh mạng!
```
**Part 6** → `audio/vs/scene12_p6.wav` (459 ký tự) · mood `don_dap`

```text
Chiếc mũi sao của Chuột Chũi Mũi Sao cũng đang truyền cảm hứng cho việc chế tạo các robot cứu hộ động đất thế hệ mới! Trong môi trường khói bụi mù mịt và bóng tối sập đổ của các tòa nhà sau thảm họa, camera quang học hoàn toàn bị vô hiệu hóa, nhưng các xúc tu cảm biến Eimer có thể dò tìm thấy nhịp thở và sự sống của nạn nhân chỉ trong tích tắc! Một phát minh lấy cảm hứng từ sinh vật mù lòa đầm lầy đang cứu sống hàng ngàn con người khỏi thảm họa thiên tai!
```
**Part 7** → `audio/vs/scene12_p7.wav` (337 ký tự) · mood `don_dap`

```text
Hơn thế nữa, các nhà khoa học vật liệu tại Viện Công nghệ Massachusetts đang phát triển loại da nhân tạo thông minh mô phỏng cơ chế M-T-C của Hải Sâm! Vật liệu này có thể dùng làm lớp vỏ ngoài cho robot mềm thám hiểm không gian: mềm dẻo để luồn lách qua các khe nứt thiên thạch nhưng lập tức cứng như thép khi cần khoan sâu vào lòng đất!
```
**Part 8** → `audio/vs/scene12_p8.wav` (406 ký tự) · mood `tram_bi_an`

```text
Trận chung kết diễn ra trong bầu không khí trang trọng và xúc động chưa từng có giữa ba đỉnh cao tiến hóa của tự nhiên! Hải Ly đại diện cho sức mạnh kiến tạo làm thay đổi cả một vùng địa lý rộng lớn, mang lại sự trù phú và nước ngọt cho muôn loài sinh vật! Axolotl đại diện cho kỳ tích tái sinh thể xác phi thường, còn Sứa Bất Tử là biểu tượng bất diệt cho sự chiến thắng quy luật nghiệt ngã của thời gian!
```
**Part 9** → `audio/vs/scene12_p9.wav` (405 ký tự) · 🎭 cameo `tham_phan`

```text
Ban giám khảo đã hoàn tất việc chấm điểm Vòng Chung Kết! Huy chương Đồng hai điểm thuộc về cụ tổ Cá Mút Đá Hagfish với vật liệu tơ chống đạn sinh thái! Huy chương Bạc bốn điểm thuộc về Kỳ Nhông Axolotl với cuộc cách mạng tái tạo mô tim và tủy sống con người! Và Huy chương Vàng sáu điểm tối cao của Vòng Chung Kết thuộc về Sứa Bất Tử với giấc mơ trẻ hóa tế bào và đảo ngược lão hóa cho toàn thể nhân loại!
```
**Part 10** → `audio/vs/scene12_p10.wav` (166 ký tự) · mood `hao_hung`

```text
Một màn lội ngược dòng không tưởng trong lịch sử Đại Hội Sinh Tồn! Tổng điểm của Sứa Bất Tử đã nhảy vọt lên con số mười bốn điểm, chính thức xô đổ mọi kỷ lục điểm số!
```

### scene13 — LỄ BẾ MẠC & TRAO VƯƠNG MIỆN ĐẠI HỘI SINH TỒN MÙA 3
*Thẻ chương:* LỄ TRAO VƯƠNG MIỆN MÙA 3

*Badge:* `LỄ BẾ MẠC & TRAO VƯƠNG MIỆN` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene13_p0.wav` (696 ký tự) · mood `hao_hung`

```text
[surprise-oh] Âm nhạc vinh quang rộn rã vang lên! Thưa toàn thể muôn loài muôn thú, chúng ta chính thức bước vào Lễ Bế Mạc và Trao Vương Miện Đại Hội Sinh Tồn Mùa ba! Sau tám vòng thi đấu nghẹt thở với hàng loạt kỷ lục khoa học được thiết lập, bảng tổng sắp chung cuộc đã chính thức chốt hạ! Mỗi tuyển thủ đều đã cống hiến hết mình, phô diễn những vũ khí sinh học và kỳ tích thích nghi làm rạng danh thế giới hoang dã! Đồng hạng ba giành Huy chương Đồng chung cuộc của Mùa ba là hai tuyển thủ: kỹ sư Hải Ly và cụ tổ Cá Mút Đá Hagfish với tám điểm xuất sắc! Ngôi vị Á quân giành Huy chương Bạc chung cuộc thuộc về thiên thần tái sinh của đất nước Mexico: Kỳ Nhông Axolotl với mười điểm tròn trĩnh!
```
**Part 1** → `audio/vs/scene13_p1.wav` (529 ký tự) · mood `tram_bi_an`

```text
Và chiếc vương miện vàng nạm đá quý tối cao của Đại Hội Sinh Tồn Mùa ba... đã tìm thấy chủ nhân xứng đáng nhất! Kẻ từng bị các chuyên gia đánh giá là yếu ớt nhất, chỉ nặng một miligram và dài bốn phẩy năm mi-li-mét trong buổi lễ cân ký đo đạc đầu tiên! Nhưng bằng năng lực đảo ngược dòng thời gian sinh học vô tận, sinh vật nhỏ bé này đã chứng minh cho toàn vũ trụ thấy: kích thước không bao giờ là giới hạn của sự sống! Một thắng lợi của sự kiên trì, của sự dẻo dai và của phép màu tái sinh vô tận trong lòng đại dương sâu thẳm!
```
**Part 2** → `audio/vs/scene13_p2.wav` (178 ký tự) · mood `hao_hung`

```text
Xin nhiệt liệt chúc mừng tân vương của Mùa ba: SỨA BẤT TỬ! Khán đài hàng vạn muông thú đồng loạt đứng dậy hò reo vang dội, vẫy cờ hoa chúc mừng chiến thắng lịch sử của tân vương!
```
**Part 3** → `audio/vs/scene13_p3.wav` (139 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Dạ em cảm ơn toàn thể muôn loài đã ủng hộ em! Em xin hứa sẽ tiếp tục bơi lội bất tử thêm vài triệu năm nữa để bảo vệ sự sống hành tinh nha!
```
**Part 4** → `audio/vs/scene13_p4.wav` (485 ký tự) · mood `hao_hung`

```text
Tất cả các tuyển thủ đều đã nhận được những chiếc cúp danh dự và huy chương tương xứng với những cống hiến khoa học phi thường của mình! Anh chàng Wombat mỉm cười tự hào với tấm huy chương vàng Vòng một, kỹ sư Hải Ly rạng rỡ với ba tấm huy chương danh giá, và cụ tổ Hagfish uy nghi với giải thưởng cổ vật sống trường tồn! Nhưng đỉnh cao vinh quang và chiếc vương miện tối cao vẫn thuộc về chú sứa nhỏ một miligram: biểu tượng của sức sống mãnh liệt vượt lên trên mọi giới hạn vật chất!
```
**Part 5** → `audio/vs/scene13_p5.wav` (280 ký tự) · mood `hao_hung`

```text
Toàn thể mười tuyển thủ cùng bước lên bục vinh quang chung, quây quần bên chiếc cúp vàng danh giá của Đại Hội Sinh Tồn Mùa ba! Chiếc máy ảnh toàn cảnh của ban tổ chức lóe sáng, ghi lại bức ảnh lịch sử của mười dị nhân vĩ đại nhất hành tinh trong sự hò reo không dứt của muôn loài!
```
**Part 6** → `audio/vs/scene13_p6.wav` (284 ký tự) · mood `hao_hung`

```text
Những tiếng hò reo vang dội khắp bốn bề đấu trường khi chiếc vương miện Mùa ba tỏa ánh sáng lộng lẫy trên đỉnh chuông sứa nhỏ bé! Đó là một khoảnh khắc xúc động nhắc nhở muôn loài về sự kỳ diệu khôn cùng của tạo hóa, nơi sinh vật nhỏ bé nhất lại nắm giữ bí mật trường tồn vĩ đại nhất!
```
**Part 7** → `audio/vs/scene13_p7.wav` (307 ký tự) · mood `hao_hung`

```text
Mỗi chiếc huy chương được trao hôm nay là sự ghi nhận xứng đáng cho hàng trăm triệu năm bền bỉ tiến hóa và thích nghi phi thường của thế giới tự nhiên! Dù mang vẻ ngoài kỳ dị hay tập tính khác thường, mỗi sinh vật đều là một kiệt tác hoàn hảo của tạo hóa, mang trong mình những giá trị vô giá cho hành tinh!
```
**Part 8** → `audio/vs/scene13_p8.wav` (267 ký tự) · mood `hao_hung`

```text
Mười tuyển thủ cùng bước lên sàn đấu chung, ôm lấy nhau trong tình thân ái muôn loài: không có ai là kẻ thua cuộc, tất cả đều là những kiệt tác tiến hóa vĩ đại của Trái Đất! Chiếc cúp Mùa ba đã tìm thấy chủ nhân, khép lại một mùa giải kịch tính nhất từ trước đến nay!
```

### scene14 — BÀI HỌC BẢO TỒN, CÂU HỎI BÌNH LUẬN & HÉ LỘ MÙA 4
*Thẻ chương:* BÀI HỌC BẢO TỒN & HÉ LỘ MÙA 4

*Badge:* `BẢO TỒN SINH THÁI & HÉ LỘ MÙA 4` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene14_p0.wav` (1103 ký tự) · mood `am_ap`

```text
Khi ánh đèn sân khấu dần dịu lại và tiếng reo hò lắng xuống, một thông điệp sâu sắc hơn bao giờ hết đang chờ đợi chúng ta lắng đọng... Mỗi loài sinh vật xuất hiện trong Mùa ba hôm nay đều là kết tinh của hàng trăm triệu năm thử nghiệm và chọn lọc tự nhiên khắc nghiệt. Nhưng dù sở hữu những siêu năng lực bẻ gãy mọi quy luật sinh học, chúng vẫn vô cùng mong manh trước sự tàn phá môi trường do con người gây ra. Kỳ Nhông Axolotl dù có thể mọc lại cả não bộ và trái tim, nhưng chúng không thể tự tái tạo lại hồ nước Xochimilco đang bị ô nhiễm và thu hẹp từng ngày, đẩy chúng đến bờ vực tuyệt chủng ngoài tự nhiên! Sứa Bất Tử có thể đảo ngược chu trình già nua vô tận, nhưng chúng vẫn tan rã bất lực trước những vùng biển ngập tràn hạt vi nhựa và hiện tượng axit hóa đại dương! Bảo vệ những sinh vật dị thường này không chỉ là bảo vệ tự nhiên hoang dã, mà chính là bảo vệ kho báu tri thức vô giá cho tương lai y học và sự tồn vong của chính loài người chúng ta! Chúng ta không thể học được bí quyết tái tạo mô tim từ Axolotl hay đảo ngược lão hóa từ Sứa nếu để chúng biến mất vĩnh viễn khỏi hành tinh này!
```
**Part 1** → `audio/vs/scene14_p1.wav` (485 ký tự) · mood `hao_hung`

```text
Và trước khi khép lại tập đặc biệt Mùa ba, anh MC xin gửi tới toàn thể quý vị khán giả một câu hỏi giao lưu đầy thú vị: Nếu được chọn sở hữu một siêu năng lực của mười quái kiệt Mùa ba: tái sinh không sẹo của Axolotl, mông bọc thép của Wombat, đớp mồi không phẩy mười hai giây của Chuột Chũi, hay khả năng đảo ngược thời gian của Sứa Bất Tử, bạn sẽ chọn năng lực nào? Hãy chia sẻ suy nghĩ và bình luận của bạn ngay bên dưới video này để cùng bàn luận với cộng đồng yêu thiên nhiên nhé!
```
**Part 2** → `audio/vs/scene14_p2.wav` (409 ký tự) · mood `don_dap`

```text
Và đừng quên nhấn nút Đăng ký kênh Vẽ Chuyện Hoang Dã ngay hôm nay để không bỏ lỡ tập ba mươi mốt: Chim Cắt Lớn Peregrine Falcon — sát thủ bầu trời bổ nhào với vận tốc ba trăm chín mươi cây số một giờ xé gió săn mồi! Cùng với đó là sự khởi động của Đại Hội Sinh Tồn Mùa bốn trong tương lai, nơi các dũng sĩ săn mồi đỉnh chóp như Cá Voi Sát Thủ Orca, Quạ Đen thiên tài và Chó Sói Xám sẽ chính thức tuyên chiến!
```
**Part 3** → `audio/vs/scene14_p3.wav` (406 ký tự) · mood `hao_hung`

```text
Hành trình Mùa ba khép lại nhưng những bài học về tình yêu thiên nhiên và sự trân trọng từng sự sống nhỏ bé sẽ còn đọng lại mãi trong trái tim chúng ta. Mỗi dòng suối mát lành, mỗi rạn san hô rực rỡ và mỗi cánh rừng nguyên sinh đều là ngôi nhà chung thiêng liêng mà con người và muôn thú cùng chia sẻ. Chúng ta hãy cùng nhau chung tay gìn giữ và bảo vệ những kỳ quan sinh học vô giá này trước khi quá muộn!
```
**Part 4** → `audio/vs/scene14_p4.wav` (339 ký tự) · mood `am_ap`

```text
Mỗi hành động nhỏ bé của chúng ta hôm nay: tiết kiệm một giọt nước sạch, giảm bớt một chiếc túi nilon thải ra đại dương, hay trồng thêm một mầm cây xanh nơi góc phố đều là sự tiếp sức cho sự trường tồn của muôn loài! Hãy cùng kênh Vẽ Chuyện Hoang Dã lan tỏa tình yêu thiên nhiên và lòng trân trọng sự sống đến mọi người xung quanh bạn nhé!
```
**Part 5** → `audio/vs/scene14_p5.wav` (286 ký tự) · mood `am_ap`

```text
Những thông điệp yêu thương và bài học bảo tồn thiên nhiên sâu sắc của Đại Hội Sinh Tồn Mùa ba sẽ tiếp tục lan tỏa, thắp sáng niềm hy vọng cho một Trái Đất xanh tươi muôn màu muôn vẻ! Một cuộc chạm trán nảy lửa trên không trung và đại dương bao la đang đón chờ quý vị khán giả thân yêu!
```
**Part 6** → `audio/vs/scene14_p6.wav` (285 ký tự) · mood `am_ap`

```text
Bảo vệ những loài sinh vật kỳ diệu này chính là bảo vệ kho tàng tri thức sinh học vô giá mà thiên nhiên đã dày công tích lũy qua hàng ngàn triệu năm! Nếu để mất đi dù chỉ một mắt xích nhỏ bé, nhân loại có thể vĩnh viễn đánh mất những chìa khóa y học quý báu không bao giờ tìm lại được!
```
**Part 7** → `audio/vs/scene14_p7.wav` (130 ký tự) · mood `hao_hung`

```text
Xin chào tạm biệt, xin cảm ơn toàn thể quý vị đã đồng hành, và hẹn gặp lại tất cả trong những chuyến phiêu lưu hoang dã tiếp theo!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Mười dị nhân mới. Tám vòng đấu sinh tử. Một chiếc vương miện tối cao! Gấu Wombat ba mươi lăm ki-lô-gam và Hải Ly răng sắt được đặt cược sẽ thắng. Còn Sứa Bất Tử một miligram... chuyên gia bảo tham gia cho vui! [laughter] Vòng một: Cá Mút Đá Hagfish sở hữu sợi tơ nhớt bền gấp mười lần tơ nhện và dai hơn sợi Kevlar! Vòng hai: Chuột Chũi Mũi Sao đớp mồi trong không phẩy mười hai giây và ngửi mùi dưới nước bằng bong bóng khí! Vòng ba: Kỳ Nhông Axolotl sở hữu bộ gen ba mươi hai tỷ cặp base tái sinh não tim mà không để lại sẹo! Vòng bốn: Đập nước Hải Ly tạo vùng ngập nước kỳ diệu ngăn chặn bão lửa và hạn hán cả thung lũng! Vòng năm: Hải Sâm lầy lội tiêu hóa một trăm ba mươi tấn trầm tích mỗi năm để bảo vệ rạn san hô! Vòng sáu: Bạch Tuộc Mimic chín bộ não biến hình mười lăm loài kịch độc chỉ trong hai trăm mili-giây! Chung kết: ai mang lại công nghệ vĩ đại nhất cho loài người? Y học tái tạo mô của Axolotl hay gen telomere bất tử của Sứa? [surprise-wa] Và tân vương Mùa ba là... sinh vật tí hon một miligram từng bị xem là mồi ngon dưới đáy biển! [question-ah] Bạn có đồng ý không? Xem trọn tám vòng đấu kịch tính trong video dài nhé, vì ở đây có mười dị nhân mới, tám vòng đấu sinh tử, và một chiếc vương miện tối cao!
```

**Whisper prompt:** `Đại Hội Sinh Tồn, Mùa 3, Vẽ Chuyện Hoang Dã, Ếch Lông Wolverine, Kỳ Nhông Axolotl, Hải Sâm, Cá Mút Đá Hagfish, Bạch Tuộc Mimic, Gấu Túi Wombat, Chuột Chũi Mũi Sao, Kiến Nổ Cảm Tử, Sứa Bất Tử, Hải Ly, 32 tỷ cặp base, 22 xúc tu, 25.000 cơ quan Eimer, 0,12 giây, 300 triệu năm, 20 lít nhớt, 3cm mông bọc thép, 100 viên phân lập phương, 130 tấn trầm tích, transdifferentiation, Kevlar, telomere, neoteny`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| hai mươi tư giờ | 24 giờ |
| Hai mươi tư giờ | 24 giờ |
| bốn mươi tám giờ | 48 giờ |
| Bốn mươi tám giờ | 48 giờ |
| ba mươi hai tỷ | 32 tỷ |
| Ba mươi hai tỷ | 32 tỷ |
| ba trăm triệu năm | 300 triệu năm |
| Ba trăm triệu năm | 300 triệu năm |
| năm trăm triệu năm | 500 triệu năm |
| Năm trăm triệu năm | 500 triệu năm |
| hai mươi lít | 20 lít |
| Hai mươi lít | 20 lít |
| một trăm ba mươi tấn | 130 tấn |
| Một trăm ba mươi tấn | 130 tấn |
| ba mươi lăm ki-lô-gam | 35kg |
| Ba mươi lăm ki-lô-gam | 35kg |
| hai mươi lăm ki-lô-gam | 25kg |
| Hai mươi lăm ki-lô-gam | 25kg |
| bốn mươi ki-lô-mét một giờ | 40 km/h |
| Bốn mươi ki-lô-mét một giờ | 40 km/h |
| không phẩy mười hai giây | 0,12 giây |
| Không phẩy mười hai giây | 0,12 giây |
| hai mươi hai xúc tu | 22 xúc tu |
| Hai mươi hai xúc tu | 22 xúc tu |
| hai mươi lăm ngàn | 25.000 |
| Hai mươi lăm ngàn | 25.000 |
| bốn phẩy năm mi-li-mét | 4,5mm |
| Bốn phẩy năm mi-li-mét | 4,5mm |
| ba xăng-ti-mét | 3cm |
| Ba xăng-ti-mét | 3cm |
| ba mươi mét | 30m |
| Ba mươi mét | 30m |
| một trăm viên | 100 viên |
| Một trăm viên | 100 viên |
| hai trăm mili-giây | 200 mili-giây |
| Hai trăm mili-giây | 200 mili-giây |
| mười lăm loài | 15 loài |
| Mười lăm loài | 15 loài |
| chín bộ não | 9 bộ não |
| Chín bộ não | 9 bộ não |
| ba quả tim | 3 quả tim |
| Ba quả tim | 3 quả tim |
| bốn quả tim | 4 quả tim |
| Bốn quả tim | 4 quả tim |
| gấp mười lần | gấp 10 lần |
| Gấp mười lần | gấp 10 lần |
| gấp ba lần | gấp 3 lần |
| Gấp ba lần | gấp 3 lần |
| một phần mười giây | 1/10 giây |
| một miligram | 1 miligram |
| nửa miligram | 0,5 miligram |
| năm mươi phần trăm | 50% |
| Năm mươi phần trăm | 50% |
| tám mươi phần trăm | 80% |
| Tám mươi phần trăm | 80% |
| một trăm phần trăm | 100% |
| Một trăm phần trăm | 100% |
| hai mươi mốt | 21 |
| ba mươi | 30 |
| bảy mươi | 70 |
| tám mươi | 80 |
| ba trăm | 300 |
| ba mươi lăm triệu lần | 35 triệu lần |
| triệu năm | triệu năm |
| bốn mươi | 40 |
| bốn mươi xăng-ti-mét | 40cm |
| một không hai | 1-0-2 |
| mười lăm xăng-ti-mét | 15cm |
| mười lăm | 15 |
| năm hai ngàn lẻ chín | 2009 |
| ba mươi phút | 30 phút |
| tám phần trăm | 8% |
| năm hai ngàn không trăm hai mươi | 2020 |
| trăm độ C | 100°C |
| năm hai ngàn mười tám | 2018 |
| Năm hai ngàn không trăm hai mươi hai | 2022 |
| năm hai ngàn không trăm hai mươi hai | 2022 |
| một cây số | 1 km² |
| ba mươi ba phần trăm | 33% |
| một ngàn mét | 1.000m |
| ngàn con | 1.000 con |
| Năm hai ngàn mười chín | 2019 |
| năm hai ngàn mười chín | 2019 |
| mười ngàn năm | 10.000 năm |
| một trăm ki-lô-gam | 100kg |
| một trăm | 100 |
| ba mét | 3m |
| mười bốn | 14 |
| ba mươi mốt | 31 |
| ba trăm chín mươi cây số | 390 km/h |
| ba trăm chín mươi | 390 |
| hai ngàn mười chín | 2019 |
| hai ngàn mười tám | 2018 |
| hai ngàn không trăm hai mươi hai | 2022 |
| hai ngàn không trăm hai mươi | 2020 |
| hai ngàn lẻ chín | 2009 |
| hai phần ba | 2/3 |
| ba mươi ba | 33 |
| năm mươi | 50 |
| Năm mươi | 50 |
| tám trăm | 800 |
| Tám trăm | 800 |
| hai mươi | 20 |
| Hai mươi | 20 |
| hai trăm | 200 |
| Hai trăm | 200 |
| hai ngàn mười bảy | 2017 |
| sáu mươi | 60 |
| Sáu mươi | 60 |
| sáu trăm | 600 |
| Sáu trăm | 600 |
| chín mươi lăm | 95% |
| Chín mươi lăm | 95% |
| ngàn năm | 1.000 năm |
| ba ngày | 3 ngày |
| hai tấn | 2 tấn |
| ba giây | 3 giây |
| chín mươi chín | 99 |
| Chín mươi chín | 99 |
| chín mươi chín phẩy chín | 99,9% |
| Chín mươi chín phẩy chín | 99,9% |
| chín mươi chín phần trăm | 99% |
| Chín mươi chín phần trăm | 99% |
| hai mươi phần trăm | 20% |
| Hai mươi phần trăm | 20% |
| Ba mươi ba phần trăm | 33% |
| mười lăm phần trăm | 15% |
| Mười lăm phần trăm | 15% |
| bốn mươi lăm phần trăm | 45% |
| Bốn mươi lăm phần trăm | 45% |
| hai mươi độ C | 20°C |
| Hai mươi độ C | 20°C |
| tám mili-giây | 8 mili-giây |
| Tám mili-giây | 8 mili-giây |
| bốn mươi triệu | 40 triệu |
| Bốn mươi triệu | 40 triệu |
| năm trăm mét | 500m |
| Năm trăm mét | 500m |
| mười ngàn lần | 10.000 lần |
| Mười ngàn lần | 10.000 lần |
| ba mươi sáu giờ | 36 giờ |
| Ba mươi sáu giờ | 36 giờ |
| tỷ năm | tỷ năm |
| Tỷ năm | tỷ năm |
| hàng tỷ năm | hàng tỷ năm |
| Hàng tỷ năm | hàng tỷ năm |
| mười ngàn sợi | 10.000 sợi |
| Mười ngàn sợi | 10.000 sợi |
| mười ngàn | 10.000 |
| Mười ngàn | 10.000 |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · 10 QUÁI KIỆT DỊ NHÂN BƯỚC VÀO ĐẤU TRƯỜNG · 297.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:05.7 (5.7s) | L01 | Màn đêm buông xuống một đấu trường cổ kính được bao quanh bởi những rạn san hô phát quang và rừng rậm nguyên sinh bí ẩn... |  | Toàn cảnh đấu trường hoạt hình khổng lồ nửa trên cạn nửa dưới nước chìm trong màn sương đêm kỳ bí, mười chiếc bục tròn phát sáng bao quanh một bục vinh quang trung tâm; KHÔNG có anh MC trong cảnh này. |
| b02 | 00:05.7–00:12.0 (6.4s) | L02 | Ở chính giữa sàn đấu, một chiếc vương miện hoàng gia nạm ngọc phát ra ánh sáng lung linh kỳ ảo, chờ đợi chủ nhân mới của Mùa ba. |  | Cận cảnh chiếc vương miện nạm ngọc lấp lánh xoay tròn trên bệ đá cẩm thạch giữa sân khấu; KHÔNG có anh MC trong cảnh này. |
| b03 | 00:12.0–00:18.4 (6.4s) | L03 | Đêm nay, mười sinh vật dị thường nhất từ Tập 21 đến Tập 30 của kênh Vẽ Chuyện Hoang Dã sẽ chính thức hội ngộ! |  | Mười chiếc bóng đen bí ẩn của 10 con vật (Ếch dị nhân móng vuốt hoạt hình đáng yêu, Axolotl, Hải Sâm, Cá Mút Đá, Bạch Tuộc Mimic, Wombat, Chuột Chũi Mũi Sao, Kiến Nổ, Sứa Bất Tử, Hải Ly) xuất hiện tại cửa hầm; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:18.4–00:23.6 (5.2s) | L04 | Họ không đến để nhắc lại những câu chuyện cũ, mà để đọ sức trực tiếp bằng hàng loạt bí mật sinh học chấn động thế |  | Mười đôi mắt hoạt hình rực sáng trong bóng tối với đủ phong thái: ngầu lạnh lùng, ngây thơ, lầy lội, bí hiểm và kiên cường; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:23.6–00:29.5 (5.8s) | L05 | giới! Mỗi loài mang theo một siêu năng lực quái dị dường như bước ra từ những trang truyện tranh siêu anh hùng viễn tưởng. |  | Những biểu tượng siêu năng lực phát sáng lơ lửng quanh cửa hầm: vuốt xương bọc thép, nhánh tái sinh, tơ nhớt siêu bền, vòng lặp vô cực và con đập gỗ; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:29.5–00:38.5 (9.0s) | L06 | Từ khả năng mọc lại cả não bộ và trái tim không tì vết, tấm khiên mông bọc thép dập nát sọ kẻ thù, cho tới bộ gen đảo ngược dòng thời gian để trường sinh bất lão! |  | Hình vẽ minh họa 4 siêu năng lực tỏa sáng trên màn hình lớn: trái tim tự liền sẹo, mông bọc giáp titan, tơ nhớt bẫy cá mập và vòng lặp vô cực; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:38.5–00:44.5 (6.1s) | L07 | Bật toàn bộ hệ thống đèn pha! Chào mừng toàn thể muôn loài đã đến với Đại Hội Sinh Tồn Mùa ba: Đấu Trường Dị Nhân! |  | Dàn đèn pha công suất lớn rọi sáng rực rỡ toàn bộ đấu trường, pháo hoa nổ tung trên bầu trời đêm; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vest đỏ tươi giơ micro vàng nở nụ cười rạng rỡ. |
| b08 | 00:44.5–00:50.9 (6.4s) | L08 | Tôi là người dẫn chương trình đêm nay, và tôi xin cam kết danh dự: những phát hiện khoa học bạn sắp nghe đều mới toanh 100%! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đặt tay lên ngực cam kết, phía sau là màn hình lớn chiếu biểu tượng các tạp chí khoa học uy tín Nature, Science và PNAS (không chữ). |
| b09 | 00:50.9–01:00.9 (9.9s) | L09 | Từ việc tơ nhớt Cá Mút Đá dai hơn áo giáp chống đạn, Kỳ Nhông Axolotl mang bộ gen 32 tỷ cặp base chống ung thư, cho đến Sứa Bất Tử tự đảo ngược thời gian tế bào! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng nháy mắt hóm hỉnh, tay kia giơ tập tài liệu dày cộm có hình chuỗi xoắn DNA và bánh răng cơ khí; khán đài thú rừng reo hò náo nhiệt. |
| b10 | 01:00.9–01:09.2 (8.3s) | L10 | Đại hội không tổ chức chỉ để so kè nắm đấm, mà là nơi tôn vinh những kỳ tích thích nghi đỉnh cao mà mẹ thiên nhiên đã dày công kiến tạo suốt hàng trăm triệu năm qua! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng giơ micro lên cao, pháo sáng hình vương miện lấp lánh trên không trung; khán giả muôn loài vẫy cờ hoa rộn ràng. |
| b11 | 01:09.2–01:16.6 (7.4s) | L11 | Luật thi đấu Mùa ba cực kỳ cam go: tám vòng đấu chính thức, xen kẽ giờ giải lao hậu trường, trao giải phụ và vòng phúc khảo tin đồn thế kỷ. |  | tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) hiện lên giữa sân với 8 ô thử thách: vũ khí tự thân, tái sinh thoát hiểm, phản xạ giác quan, công trình địa hình, bộ gen đột biến, bảo vệ sinh thái, cụ tổ cổ đại và món quà nhân loại. |
| b12 | 01:16.6–01:24.7 (8.2s) | L12 | Mỗi vòng thi, ban giám khảo sẽ trao ba tấm huy chương: Vàng được ba điểm, Bạc hai điểm, và Đồng một điểm. Riêng Vòng Chung Kết sẽ được nhân đôi điểm số! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ ngồi ở bàn giám khảo trên cao gõ búa gỗ, trước mặt là khay nhung đỏ bày ba chiếc huy chương vàng, bạc, đồng sáng loáng. |
| b13 | 01:24.7–01:30.9 (6.2s) | L13 | Khắp các khán đài, muông thú từ khắp năm châu bốn biển đang giương cao những biểu ngữ cổ vũ vô cùng huyên náo và hài hước! |  | Khán đài hoạt hình rực rỡ cờ hoa, đàn gấu trúc vác băng rôn vẽ hình chiếc vương miện, bầy chim cánh cụt mặc áo phông cổ vũ nhiệt tình; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:30.9–01:39.4 (8.5s) | L14 | Đội cổ động viên rái cá biển vừa gõ sò vừa reo hò, trong khi các bạn chồn Gulo ngồi ở hàng ghế danh dự chăm chú theo dõi từng động thái của mười dị nhân! |  | Đàn rái cá biển gõ hai vỏ sò vào nhau kêu canh cách vui nhộn, các chú chồn Gulo đeo kính râm vỗ tay phấn khích; KHÔNG có anh MC trong cảnh này. |
| b15 | 01:39.4–01:46.4 (6.9s) | L15 | Hải Ly thậm chí còn ngứa răng cắn nhẹ vào chân chiếc bàn ban tổ chức làm bà Cú giám khảo phải vội vàng lấy thước gõ can ngăn! |  | chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo đang định há miệng gặm góc bàn cẩm thạch, bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ cầm thước gỗ gõ nhẹ lên trán Hải Ly làm chú ta rụt cổ cười trừ; KHÔNG có anh MC trong cảnh này. |
| b16 | 01:46.4–01:54.2 (7.8s) | L16 | Còn anh chàng Wombat thì tranh thủ tựa chiếc mông bọc thép 3cm vào cây cột thép chịu lực để ngủ gật một giấc ngắn trước giờ khai chiến! |  | chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường đứng dựa mông vào cột thép ngáy khò khò ngon lành, miệng mỉm cười như đang mơ thấy cánh đồng cỏ tươi xanh; KHÔNG có anh MC trong cảnh này. |
| b17 | 01:54.2–02:03.0 (8.8s) | L17 | Giám khảo xin nhắc nhở nghiêm túc: nghiêm cấm phóng ruột vào mặt đối thủ, cấm xả nhớt làm trơn sàn thi đấu và cấm nổ bụng lung tung trong khu vực khán đài! |  | Cận cảnh bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ cúi đầu nhìn qua gọng kính tròn, vẻ mặt nghiêm nghị đưa cánh ra lệnh chỉ đạo. |
| b18 | 02:03.0–02:08.5 (5.5s) | L18 | Các tuyển thủ đã nghe rõ chưa? Nhất là anh chàng Hải Sâm và bạn Kiến Nổ đang lén lút nhìn quanh |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng liếc nhìn sang chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù và chú Kiến Nổ dũng cảm bảo vệ tổ hoạt hình màu đỏ cam, đeo ba lô chứa chất lỏng vàng phát sáng, đội mũ bảo hộ chống độc, ánh mắt quả cảm kiên cường đang giả vờ gãi đầu cười trừ ngây thơ vô số tội. |
| b19 | 02:08.5–02:15.4 (6.9s) | L19 | đằng kia! Và bây giờ, xin mời toàn thể khán đài cùng đứng dậy nhiệt liệt hoan nghênh mười quái kiệt bước ra thảm đỏ danh dự! |  | Cửa hầm mở toang, ánh đèn flash chớp sáng liên hồi, khói lạnh cuồn cuộn thổi qua lối đi chính; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:15.4–02:20.6 (5.3s) | L20 | Tuyển thủ số một! Chiến binh móng vuốt Tây Phi tự bẻ xương ngón chân xuyên thủng da chân để nghênh chiến! Ếch Lông Wolverine! |  | chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng bước ra thảm đỏ, hai bên sườn phủ lớp lông tơ nâu sậm, đầu ngón chân sau xòe ra những móng vuốt xương nhọn hoắt cực ngầu; KHÔNG có anh MC trong cảnh này. |
| b21 | 02:20.6–02:26.9 (6.3s) | L21 | Tuyển thủ số hai! Đại sứ tái sinh của hồ nước ngọt Mexico có thể mọc lại cả trái tim và não bộ không vết sẹo! Kỳ Nhông Axolotl! |  | chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói bơi lượn trong bồn nước ngọt trong suốt, sáu nhánh mang hồng xòe rộng như cánh hoa, nụ cười ngây thơ đốn tim khán giả; KHÔNG có anh MC trong cảnh này. |
| b22 | 02:26.9–02:32.2 (5.3s) | L22 | Tuyển thủ số ba! Sinh vật lầy lội không xương đáy biển sẵn sàng xả trọn bộ ruột qua hậu môn để tẩu thoát! |  | chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù mập mạp màu cam sần sùi trườn ra sân khấu, tay phe phẩy chiếc quạt giấy mini trông vô cùng hài hước; KHÔNG có anh MC trong cảnh này. |
| b23 | 02:32.2–02:38.4 (6.2s) | L23 | Hải Sâm! Tuyển thủ số bốn! Cổ vật sống 300 triệu năm tiết ra 20 lít keo nhớt trong chớp mắt làm nghẹt thở cá mập! Cá Mút Đá Hagfish! | **20 LÍT** · Khóa chặt mang kẻ thù · R/390 · [0.65, 0.48] | chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện thân trơn tuột màu xám tím quấn quanh cột thủy tinh, toàn thân phủ các vệt bọt nhớt lấp lánh, thắt nút thân số 8 điêu luyện; KHÔNG có anh MC trong cảnh này. |
| b24 | 02:38.4–02:45.1 (6.7s) | L24 | Tuyển thủ số năm! Bậc thầy phân thân sở hữu 9 bộ não và có thể cải trang thành 15 loài kịch độc đáy đại dương! Bạch Tuộc Mimic! | **9 BỘ NÃO** · Trí tuệ phân tán · L/400 · [0.35, 0.72] | chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình sọc vằn nâu trắng uốn lượn biến ảo thành hình dáng rắn biển rồi lại hóa thành cá sư tử đầy gai góc; KHÔNG có anh MC trong cảnh này. |
| b25 | 02:45.1–02:50.8 (5.7s) | L25 | Tuyển thủ số sáu! Chiến xa đào hầm nước Úc sở hữu tấm mông bọc thép 3cm đập nát sọ kẻ thù! Gấu Túi Wombat! |  | chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường mập mạp bệ vệ bước ra, quay chiếc mông bọc thép titan chống cắn về phía khán giả khoe sức mạnh, tay cầm xẻng xúc đất mini; KHÔNG có anh MC trong cảnh này. |
| b26 | 02:50.8–02:57.0 (6.2s) | L26 | Tuyển thủ số bảy! Cỗ máy săn mồi mù lòa mang 22 xúc tu hồng đớp mồi nhanh nhất hành tinh! Chuột Chũi Mũi Sao! | **22 XÚC TU** · Cơ quan Eimer nhạy · R/410 · [0.62, 0.52] | chú Chuột Chũi Mũi Sao hoạt hình lông đen nhung mượt mà, mũi xòe ra 22 xúc tu đỏ hồng như bông hoa sao biển, đeo kính râm mù lòa nhưng phản xạ siêu thanh đeo kính râm ngầu, chiếc mũi sao biển đỏ hồng nhấp nháy liên hồi quét tín hiệu không gian; KHÔNG có anh MC trong cảnh này. |
| b27 | 02:57.0–03:02.7 (5.7s) | L27 | Tuyển thủ số tám! Nữ chiến binh cảm tử sẵn sàng kích nổ cơ thể phun keo dính bảo vệ an toàn cho tổ ấm! |  | chú Kiến Nổ dũng cảm bảo vệ tổ hoạt hình màu đỏ cam, đeo ba lô chứa chất lỏng vàng phát sáng, đội mũ bảo hộ chống độc, ánh mắt quả cảm kiên cường đội mũ bảo hộ chống độc, đeo ba lô chứa chất lỏng vàng phát quang, bước đi đầy quả cảm kiên định; KHÔNG có anh MC trong cảnh này. |
| b28 | 03:02.7–03:09.5 (6.8s) | L28 | Kiến Nổ Cảm Tử! Tuyển thủ số chín! Tổng công trình sư thiên tài sở hữu răng cam bọc sắt đốn ngã cổ thụ xây đập nước vĩ đại! Hải Ly! |  | chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo đội mũ bảo hộ công trình vàng, vác khúc gỗ lớn trên vai, chiếc đuôi dẹt đập bôm bốp xuống sàn chào khán giả; KHÔNG có anh MC trong cảnh này. |
| b29 | 03:09.5–03:16.4 (6.9s) | L29 | Và tuyển thủ số mười... xin mời ban tổ chức đưa kính lúp quang học ra sân vì bạn ấy đang trôi lơ lửng trong ly nước của giám khảo! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cúi người nhìn chăm chú vào chiếc ly thủy tinh nhỏ trên bàn giám khảo; KHÔNG có anh MC trong cảnh này. |
| b30 | 03:16.4–03:23.7 (7.3s) | L30 | Dạ em ở đây nè anh MC ơi! Em chỉ dài 4,5mm thôi nhưng tuổi thọ của em thì bằng cả vũ trụ cộng lại đó nha! |  | Cận cảnh phóng to qua kính hiển vi: chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực trong suốt hình chuông nhỏ xíu phát ánh sáng hồng tím ma thuật, đeo bùa hộ mệnh vô cực vẫy xúc tu tí hon; KHÔNG có anh MC trong cảnh này. |
| b31 | 03:23.7–03:30.4 (6.7s) | L31 | Một tràng pháo tay cho sự có mặt của mười dũng sĩ dị nhân! Và theo truyền thống, mời tất cả bước vào Lễ Cân Ký Đo Đạc |  | Chiếc bàn cân điện tử khổng lồ giữa đấu trường sáng đèn, các kỹ thuật viên đeo găng tay chuẩn bị ghi nhận số liệu; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cầm micro đứng bên cạnh. |
| b32 | 03:30.4–03:36.7 (6.3s) | L32 | khởi động! Mười tuyển thủ lần lượt bước lên đĩa cân kiểm tra thể trọng dưới sự giám sát chặt chẽ của các trọng tài thú y quốc tế! |  | Nhân viên kỹ thuật cầm bảng kẹp tài liệu kiểm tra trọng lượng từng đấu sĩ; KHÔNG có anh MC trong cảnh này. |
| b33 | 03:36.7–03:43.0 (6.3s) | L33 | Chiến xa Wombat bước lên đầu tiên! Rầm! 35kg cơ bắp chắc nịch đè nặng mặt cân thép! Tuyển thủ hạng nặng số một của đại hội! | **35KG** · Wombat nặng nhất · R/380 · [0.72, 0.45] | chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường đứng lên bàn cân, kim đồng hồ điện tử nhảy vọt lên con số 35kg; KHÔNG có anh MC trong cảnh này. |
| b34 | 03:43.0–03:48.3 (5.3s) | L34 | Tiếp theo là kỹ sư Hải Ly: 25kg lông dày và cơ hàm sắt thép, sẵn sàng cho mọi cuộc đọ sức thể lực! | **25KG** · Hải Ly công trình · L/380 · [0.38, 0.78] | chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo ngồi nghiêm túc lên cân, màn hình điện tử hiện số 25kg, tay vẫn cầm chắc thanh gỗ đo đạc; KHÔNG có anh MC trong cảnh này. |
| b35 | 03:48.3–03:54.5 (6.2s) | L35 | Nhóm hạng trung gồm Cá Mút Đá Hagfish nặng một ký, Hải Sâm nửa ký, và Bạch Tuộc Mimic 300 gam uốn lượn trên đĩa cân thủy tinh! |  | Ba chiếc cân đặt cạnh nhau: chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện trườn trên cân 1kg, chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù nằm ườn 500g, chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến |
| b36 | 03:54.5–03:59.8 (5.3s) | L36 | Ếch Wolverine nặng 80 gam, Kỳ Nhông Axolotl 70 gam, và Chuột Chũi Mũi Sao vỏn vẹn 50 gam! |  | Ba tuyển thủ tí hon đứng trên cân phân tích chính xác: chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng, chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói và chú Chuột Chũi Mũi Sao hoạt hình l |
| b37 | 03:59.8–04:05.7 (6.0s) | L37 | Và đỉnh điểm chênh lệch: Kiến Nổ chỉ nặng 0,5 miligram, còn Sứa Bất Tử chỉ nặng đúng 1 miligram bé như hạt bụi nước! |  | Bảng so sánh đồ họa: một bên là chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường khổng lồ như xe bọc thép, một bên là chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực chỉ là chấm sáng li ti; nhân viên kỹ thuật há hốc mồm kinh ngạc; KHÔNG có anh MC tr |
| b38 | 04:05.7–04:11.9 (6.2s) | L38 | Gấu Wombat nặng gấp... 35 triệu lần Sứa Bất Tử! Chiếc máy tính của ban tổ chức suýt bốc khói vì tỷ lệ lệch pha này! |  | Kỹ thuật viên ôm đầu trước màn hình máy tính hoạt hình hiện biểu tượng bốc khói quá tải dữ liệu; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cười lớn vỗ tay. |
| b39 | 04:11.9–04:18.7 (6.8s) | L39 | Sự chênh lệch khủng khiếp giữa cỗ xe bọc thép 30 lăm ký và chú sứa 1 miligram lập tức thổi bùng lên các cuộc tranh cãi nảy lửa khắp khán đài! |  | Khán giả chia thành hai phe cãi nhau chí chóe: phe ủng hộ cơ bắp khổng lồ và phe đặt cược vào siêu năng lực vi mô; KHÔNG có anh MC trong cảnh này. |
| b40 | 04:18.7–04:24.9 (6.2s) | L40 | Sau lễ cân ký, bảng dự đoán ban đầu nghiêng hẳn về hai gã cơ bắp Wombat và Hải Ly cùng sát thủ móng vuốt Ếch Wolverine! |  | Màn hình chiếu cột dự đoán: các cột cao vút gắn hình đầu chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường, chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo, chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần  |
| b41 | 04:24.9–04:32.1 (7.3s) | L41 | Còn Sứa Bất Tử 1 miligram và Hải Sâm mềm nhũn? Giới chuyên môn ghi chú lạnh lùng: đề nghị mua sẵn bảo hiểm trọn gói! |  | Cột dự đoán thấp tè gắn hình chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực và chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù; chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ  |
| b42 | 04:32.1–04:39.1 (6.9s) | L42 | Nhưng lịch sử hai mùa giải trước đã dạy chúng ta bài học xương máu: kẻ tí hon thường là kẻ tung ra cú đấm quyết định khiến tất cả ngã ngửa! |  | Bức ảnh hồi tưởng Thú Mỏ Vịt Mùa một và Bọ Pháo Thủ Mùa hai giơ cao cúp vô địch trong sự ngỡ ngàng của giới chuyên gia; KHÔNG có anh MC trong cảnh này. |
| b43 | 04:39.1–04:43.8 (4.8s) | L43 | Mỗi ứng viên mang theo một bộ mã gen dị thường được tôi luyện qua hàng trăm triệu năm tiến hóa khắc nghiệt của tự |  | Mô hình chuỗi xoắn kép D-N-A khổng lồ xoay tròn giữa sàn đấu, từng đoạn gen phát quang rực rỡ mang tên mười loài sinh vật; KHÔNG có anh MC trong cảnh này. |
| b44 | 04:43.8–04:50.2 (6.4s) | L44 | nhiên! Không có sàn đấu nào trên hành tinh này có thể quy tụ cùng lúc những kỳ tích sinh học phá vỡ mọi quy luật vật lý và y học đến như |  | Toàn cảnh đấu trường tràn ngập ánh sáng laser và màn hình holographic phân tích chỉ số sinh học của các tuyển thủ; KHÔNG có anh MC trong cảnh này. |
| b45 | 04:50.2–04:57.9 (7.7s) | L45 | vậy! Trong thế giới tự nhiên kỳ thú, cơ bắp chưa bao giờ là thước đo duy nhất cho sự sinh tồn! Đêm nay, mười dị nhân sẽ chứng minh chân lý đó! |  | Cận cảnh ánh mắt rực lửa của mười tuyển thủ trong ánh sáng laser huyền ảo, sẵn sàng bước vào vòng đấu súng đầu tiên; KHÔNG có anh MC trong cảnh này. |

### scene02 · ĐẠI CHIẾN NÂNG CẤP VŨ KHÍ & ÁO GIÁP SINH HỌC · 301.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:06.9 (6.9s) | L46 | Tiếng còi khai cuộc vang lên! Chào mừng quý vị đến với Vòng một: Đọ Sức Vũ Khí Tự Thân và Áo Giáp Sinh Học! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng giơ tay phất cờ hiệu màu đỏ, pháo hoa bắn sáng rực hai bên sân khấu; tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) nhấp nháy sáng ô thử thách số một. |
| b02 | 00:06.9–00:15.3 (8.4s) | L47 | Tại vòng đấu này, mười tuyển thủ sẽ phô diễn những trang bị cơ thể dị thường nhất được tôi luyện qua hàng trăm triệu năm tiến hóa khắc nghiệt của thế giới hoang dã! |  | Màn hình lớn chiếu đồ họa các loại giáp và vũ khí sinh học: móng vuốt xương, tấm khiên sụn, răng sắt và màng keo chống đạn; KHÔNG có anh MC trong cảnh này. |
| b03 | 00:15.3–00:23.1 (7.8s) | L48 | Không có súng đạn cơ khí của con người, nhưng vũ khí sinh học tự nhiên lại sở hữu độ bền và hiệu năng vượt xa mọi phòng thí nghiệm quân sự tối tân nhất! |  | Hình ảnh minh họa áo giáp sắt của con người bị rỉ sét nứt vỡ so sánh với bộ giáp sinh học tự phục hồi nguyên vẹn; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:23.1–00:29.2 (6.1s) | L49 | Ứng cử viên số một bước ra sàn đấu: Gấu Túi Wombat mang chiếc mông bọc thép huyền thoại tiến thẳng vào mô hình hang đất hẹp với |  | chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường chui đầu vào cửa hang đất mô phỏng, quay trọn vẹn phần mông bọc thép dày cộm ra ngoài đối diện kẻ thù; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:29.2–00:38.1 (8.9s) | L50 | phong thái vô cùng tự tin! Các nhà khoa học tại đại học Adelaide đã phát hiện: lớp giáp mông này không phải là xương đặc thông thường, mà là sự kết hợp hoàn hảo giữa sụn dày và các dải mô mạc sợi kết nối siêu bền! |  | Sơ đồ giải phẫu cắt lớp hoạt hình: lớp da dày, lớp sụn đàn hồi và dải collagen đan chéo chịu lực va đập cực đại; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:38.1–00:43.7 (5.6s) | L51 | Độ dày của tấm khiên lên tới 3cm, có khả năng triệt tiêu toàn bộ lực cắn chết người từ hàm răng sắc nhọn của chó hoang Dingo một cách | **DÀY 3CM** · Khiên sụn mô mạc sợi · R/420 · [0.65, 0.48] | Mô hình chó hoang Dingo cắn ngập răng vào mông chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường nhưng răng trượt kêu ken két, chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường vẫn thản nhiên nhai cỏ; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:43.7–00:51.3 (7.6s) | L52 | dễ dàng! Chưa dừng lại ở đó, Wombat tung ra tuyệt kỹ cú đá lừa ngược: dùng bốn chân gồng cứng đẩy toàn bộ sức nặng cơ thể ép nát hộp sọ kẻ tấn công lên trần hang đá hoa |  | chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường dùng hai chân sau đạp mạnh đẩy tấm khiên mông dập mạnh lên trần hang, tiếng sọ kẻ thù nứt toác trong mô phỏng hoạt hình; KHÔNG có anh MC trong cảnh này. |
| b08 | 00:51.3–00:57.6 (6.3s) | L53 | cương! Cơ chế đập nát sọ bằng mông biến nơi dễ tổn thương nhất của động vật thành một chiếc bẫy kẹp thủy lực nghiền nát mọi kẻ săn mồi liều lĩnh trong |  | Mô phỏng chiếc máy ép thủy lực hoạt hình kẹp nát tảng đá cứng để minh họa sức mạnh cú thúc mông của chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường; KHÔNG có anh MC trong cảnh này. |
| b09 | 00:57.6–01:04.3 (6.7s) | L54 | chớp mắt! Tuyệt chiêu phòng thủ biến thành đòn tấn công chí mạng! Khán đài vỗ tay sấm dậy trước cỗ xe tăng đào hầm kiên cố của hoang dã nước Úc! |  | Khán đài thú rừng đồng loạt giơ bảng chấm điểm chín và mười reo hò; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng giơ micro thán phục. |
| b10 | 01:04.3–01:11.1 (6.8s) | L55 | Nhưng đối thủ của Wombat không hề chịu lép vế! Xin mời kỹ sư Hải Ly tiến vào sàn đọ sức với bộ răng cửa màu cam rực rỡ! |  | chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo bước lên bục gỗ, ngoác miệng khoe hai chiếc răng cửa trên dưới màu cam sáng chói như thanh kim loại nung nóng; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:11.1–01:17.0 (5.9s) | L56 | Tại sao răng của Hải Ly lại có màu cam kỳ lạ như vậy? Một công trình nghiên cứu trên tạp chí Science đã làm sáng tỏ bí mật này! |  | Phóng to hình ảnh hiển vi điện tử: các hạt nano hợp chất sắt vô định hình xen kẽ giữa các trụ khoáng men răng; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:17.0–01:24.4 (7.4s) | L57 | Men răng của Hải Ly được gia cố bằng các hạt nano hợp chất giàu sắt vô định hình, giúp răng của chúng cứng hơn cả men răng người và kháng hoàn toàn axit ăn mòn! |  | Hình vẽ minh họa so sánh: axit nhỏ vào răng thường bị xủi bọt, còn nhỏ vào răng của chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo thì trôi tuột như nước trên lá sen; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:24.4–01:31.6 (7.1s) | L58 | Nhờ vũ khí bọc sắt này, Hải Ly có thể gặm đứt một thân cây gỗ cứng đường kính 40cm chỉ trong vài giờ đồng hồ mà răng không hề bị mẻ hay gãy! | **40CM** · Đốn ngã thân cây cứng · L/400 · [0.45, 0.72] | chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo ngoạm răng vào thân cây cổ thụ dày cộp, dăm gỗ bay tung tóe, thân cây đổ rầm trong sự kinh ngạc của khán giả; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:31.6–01:38.2 (6.6s) | L59 | Hơn thế nữa, răng của chúng mọc liên tục suốt đời, càng gặm gỗ nhiều thì hai mặt răng càng tự mài vào nhau thành lưỡi đục sắc như dao mổ |  | Hai chiếc răng trên và dưới cọ xát vào nhau tóe ra những tia lửa hoạt hình sắc lẹm; KHÔNG có anh MC trong cảnh này. |
| b15 | 01:38.2–01:46.1 (8.0s) | L60 | phẫu thuật tinh vi! Nếu con người sở hữu hàm răng bọc sắt như Hải Ly, các nha sĩ trên toàn cầu chắc chắn sẽ thất nghiệp tập thể vì sâu răng không bao giờ có cửa tấn công! |  | Hình ảnh bác sĩ nha khoa hoạt hình ngồi ngáp dài đóng cửa phòng khám vì ai nấy đều có hàm răng sắt cam lấp lánh; KHÔNG có anh MC trong cảnh này. |
| b16 | 01:46.1–01:49.6 (3.4s) | L61 | Đến lượt sát thủ rừng rậm Tây Phi xuất trận: Ếch Lông Wolverine! |  | chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng ngồi thu mình trên bệ đá rêu phong, ánh mắt sắc lẹm nhìn thẳng vào ống kính; KHÔNG có anh MC trong cảnh này. |
| b17 | 01:49.6–01:54.8 (5.3s) | L62 | Khi bị đe dọa, chú ếch này tự gồng các bó cơ chân sau, bẻ gãy khớp nối sụn của đốt xương ngón chân cuối cùng! |  | Đồ họa X-quang hoạt hình: khớp xương ngón chân tách rời khỏi đốt sụn, cơ co rút kéo xương dịch chuyển; KHÔNG có anh MC trong cảnh này. |
| b18 | 01:54.8–02:00.8 (6.0s) | L63 | Mũi xương nhọn hoắt đâm xuyên thủng lớp da đệm thịt dưới lòng bàn chân, phóng ra ngoài như những chiếc móng vuốt tự chế chết người! |  | Cận cảnh bàn chân sau: ba chiếc vuốt xương trắng muốt nhọn hoắt đâm xuyên qua da thịt phóng ra ngoài kêu cách cách; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:00.8–02:07.4 (6.5s) | L64 | Và điều kỳ diệu nhất theo công bố của tạp chí Biology Letters: sau khi chiến đấu xong, các cơ thả lỏng, móng xương tự thụt vào bên trong! |  | Móng xương từ từ rút lui vào trong lớp thịt đệm bàn chân; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:07.4–02:16.2 (8.8s) | L65 | Chỉ sau 48 giờ, lớp mô da bị đâm rách sẽ tự động tái tạo và lành lặn hoàn toàn mà không hề bị nhiễm trùng nhờ các hợp chất kháng khuẩn cực mạnh tiết ra từ tuyến da! | **48 GIỜ** · Mô da tự lành · R/390 · [0.68, 0.52] | Vết rách trên da liền lại trơn tru chỉ sau 48 giờ, chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng nhếch mép cười đắc thắng; KHÔNG có anh MC trong cảnh này. |
| b21 | 02:16.2–02:24.0 (7.8s) | L66 | Một cơ chế bẻ xương tự thân có 1-0-2 trong thế giới động vật có xương sống, kết hợp giữa vũ khí sát thương và khả năng tự chữa lành siêu tốc! |  | chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng đứng thẳng vươn vai khoe bộ vuốt xương lấp lánh như chiến binh dũng mãnh; KHÔNG có anh MC trong cảnh này. |
| b22 | 02:24.0–02:31.3 (7.3s) | L67 | Không chỉ có bốn tuyển thủ trên, nữ chiến binh tí hon Kiến Nổ Cảm Tử cũng khiến ban giám khảo phải giật mình trước cơ chế tự hủy bảo vệ tổ! |  | chú Kiến Nổ dũng cảm bảo vệ tổ hoạt hình màu đỏ cam, đeo ba lô chứa chất lỏng vàng phát sáng, đội mũ bảo hộ chống độc, ánh mắt quả cảm kiên cường bước lên bục kính bọc thép, cơ thể màu đỏ cam ánh lên dưới đèn pha; KHÔNG có anh MC trong cảnh này. |
| b23 | 02:31.3–02:38.8 (7.4s) | L68 | Nghiên cứu của tiến sĩ Alice Laciny tại Borneo phát hiện: cặp tuyến hàm dưới của kiến thợ phình to bất thường, kéo dài dọc toàn bộ khoang bụng! |  | Đồ họa giải phẫu kiến thợ: hai dải tuyến độc màu vàng óng phình to chiếm trọn khoang bụng phát sáng; KHÔNG có anh MC trong cảnh này. |
| b24 | 02:38.8–02:46.5 (7.8s) | L69 | Khi đối mặt với kẻ thù xâm lược tổ, kiến thợ gồng toàn bộ các cơ bụng làm nứt vỡ lớp vỏ kitin, phóng thích dòng keo độc tố dính chặt và làm mù mắt kẻ tấn |  | Vỏ bụng nứt toác phóng ra dòng keo dính màu vàng bao trùm con bọ hung xâm lược, con bọ ngã gục dính chặt vào mặt sàn; KHÔNG có anh MC trong cảnh này. |
| b25 | 02:46.5–02:52.5 (6.0s) | L70 | công! Một sự hy sinh quả cảm của tầng lớp thợ già để bảo toàn sự sống cho toàn bộ đàn ấu trùng và kiến chúa non trẻ! |  | Khán đài im lặng xúc động trước tinh thần hy sinh của chú Kiến Nổ dũng cảm bảo vệ tổ hoạt hình màu đỏ cam, đeo ba lô chứa chất lỏng vàng phát sáng, đội mũ bảo hộ chống độc, ánh mắt quả cảm kiên cường, bà Cú gật đầu chấm điểm danh dự; KHÔNG có anh MC trong cảnh này. |
| b26 | 02:52.5–03:03.2 (10.7s) | L71 | Và Bạch Tuộc Mimic cũng thể hiện vũ khí cận chiến: các giác hút trên tám xúc tu có thể siết chặt với lực hút hàng chục kilopascal, đồng thời tiết ra độc tố tetrodotoxin gây tê liệt tức thì con mồi! |  | chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình giơ xúc tu siết chặt con cua biển mô phỏng, dòng độc tố phát sáng xanh lam làm con cua đông cứng; KHÔNG có anh MC trong cảnh này. |
| b27 | 03:03.2–03:09.9 (6.7s) | L72 | Bên cạnh đó, lớp da nhầy đặc biệt của Kỳ Nhông Axolotl cũng là một tấm áo giáp sinh học vô hình chống lại mọi mầm bệnh nấm mốc nước |  | chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói bơi lượn trong làn nước mát, toàn thân phát ra ánh sáng dịu nhẹ của lớp màng gel bảo vệ tự nhiên; KHÔNG có anh MC trong cảnh này. |
| b28 | 03:09.9–03:18.2 (8.2s) | L73 | ngọt! Lớp chất nhầy kháng khuẩn phủ kín bề mặt cơ thể Axolotl chứa hàng chục loại enzym lysozyme tự nhiên, tiêu diệt vi khuẩn gram âm ngay khi chúng vừa tiếp xúc với biểu |  | Kính hiển vi soi vào bề mặt da: các phân tử enzym lysozyme phá vỡ màng tế bào vi khuẩn có hại một cách chớp nhoáng; KHÔNG có anh MC trong cảnh này. |
| b29 | 03:18.2–03:26.9 (8.7s) | L74 | bì! Nhờ vậy, ngay cả khi bị thương rách toạc da thịt trong các cuộc đụng độ dưới đáy hồ đục, cơ thể chúng vẫn duy trì trạng thái vô trùng tuyệt đối để phục vụ tiến trình tái sinh! |  | Vết thương rách trên thân chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói được lớp gel kháng khuẩn bảo vệ kín mít, không hề bị sưng tấy hay nhiễm trùng; KHÔNG có anh MC trong cảnh này. |
| b30 | 03:26.9–03:33.4 (6.6s) | L75 | Thậm chí khi nghiên cứu kỹ lưỡng về cơ học va chạm, các nhà vật lý nhận thấy cấu trúc mông của Wombat hoạt động như một hệ thống giảm xóc thủy lực tự |  | Mô hình đồ họa 3D mô phỏng xung lực va chạm bị tiêu tán qua mạng lưới vi sợi sụn của chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường; KHÔNG có anh MC trong cảnh này. |
| b31 | 03:33.4–03:41.4 (8.0s) | L76 | nhiên! Lực cắn chết người từ kẻ săn mồi bị phân tán đều ra toàn bộ vùng chậu và cột sống vững chãi, biến áp lực tập trung thành một lực nén nhẹ nhàng không gây tổn |  | Các đường phản lực màu đỏ phân tán thành làn sóng xanh êm dịu chạy dọc khung xương chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường; KHÔNG có anh MC trong cảnh này. |
| b32 | 03:41.4–03:48.6 (7.2s) | L77 | thương! Còn chiếc càng súng của Tôm Súng có thể chịu được áp lực nổ tương đương hàng chục bầu khí quyển mà lớp vỏ kitin bên ngoài không hề bị rạn nứt một sợi tóc! |  | Lớp vỏ càng tôm bóng loáng chống chịu sóng xung tạo bong bóng dính rực rỡ dưới đáy nước; KHÔNG có anh MC trong cảnh này. |
| b33 | 03:48.6–03:56.9 (8.3s) | L78 | Ban giám khảo tròn mắt chấm điểm! |  | chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện trườn vào bể nước kính cường lực trước ánh mắt tò mò của toàn bộ khán đài; KHÔNG có anh MC trong cảnh này. |
| b34 | 03:56.9–04:00.2 (3.3s) | L79 | Và cuối cùng là màn trình diễn của cụ tổ 300 triệu năm: Cá Mút Đá Hagfish! Khi một mô hình cá mập giả lao vào cắn, Hagfish ngay lập tức tiết ra một lượng chất nhầy nhỏ hòa tan vào nước biển xung quanh! |  | Mô hình cá mập ngậm trúng chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện, nhưng chỉ trong một phần mười giây, một khối keo nhớt khổng lồ bung ra bít kín mang cá mập; KHÔNG có anh MC trong cảnh này. |
| b35 | 04:00.2–04:05.6 (5.4s) | L80 | Viện nghiên cứu sinh học vật liệu phát hiện: bên trong chất nhầy của Hagfish chứa hàng vạn sợi protein tơ cuộn tròn siêu |  | Hình ảnh hiển vi: các cuộn sợi protein bung ra như những sợi dây thừng nano đan kết chặt chẽ vào nhau; KHÔNG có anh MC trong cảnh này. |
| b36 | 04:05.6–04:13.7 (8.2s) | L81 | nhỏ! Khi gặp nước biển, các sợi tơ này bung dài ra tới 15cm, tạo thành một mạng lưới sợi bền gấp 10 lần tơ nhện và dai hơn cả sợi Kevlar dùng may áo giáp chống | **15CM** · Sợi tơ protein bung nở · L/410 · [0.35, 0.65] | Bảng so sánh hoạt hình: sợi tơ Hagfish kéo căng chịu lực kéo gấp 10 lần tơ nhện và vượt xa độ bền của sợi Kevlar thế giới tự nhiên; KHÔNG có anh MC trong cảnh này. |
| b37 | 04:13.7–04:21.9 (8.2s) | L82 | đạn! Để không bị chính chất nhầy của mình bít nghẹt, Hagfish tự uốn cong cơ thể thắt thành một nút số tám hoàn hảo, gạt phăng lớp nhớt từ đầu đến đuôi chỉ trong nháy mắt! |  | chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện thắt nút thân hình số 8 trượt dọc thân gạt sạch bọt nhớt ra ngoài cực kỳ điêu luyện; KHÔNG có anh MC trong cảnh này. |
| b38 | 04:21.9–04:26.3 (4.4s) | L83 | Một vòng đọ sức vũ khí đỉnh cao khiến thang điểm của ban giám khảo suýt chạm trần tuyệt đối! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vung tay hào hứng, màn hình hiển thị hàng loạt điểm số chín và mười rực rỡ; KHÔNG có anh MC trong cảnh này. |
| b39 | 04:26.3–04:33.1 (6.8s) | L84 | Các nhà khoa học tại đại học Guelph phát hiện: độ đàn hồi của sợi tơ Hagfish khi kéo giãn còn vượt trội hơn cả sợi tơ nhện mạng tròn cự phách! |  | Kính hiển vi lực nguyên tử kéo giãn sợi protein chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện đàn hồi uốn lượn không hề đứt đoạn; KHÔNG có anh MC trong cảnh này. |
| b40 | 04:33.1–04:39.7 (6.6s) | L85 | Cấu trúc xoắn ốc của các vi sợi protein hoạt động như những chiếc lò xo giảm chấn phân tử, hấp thụ toàn bộ lực xé rách của dòng nước xoáy! |  | Mô hình các cuộn protein xoắn lò xo co giãn linh hoạt trong làn nước biển cuộn xoáy; KHÔNG có anh MC trong cảnh này. |
| b41 | 04:39.7–04:49.1 (9.5s) | L86 | Ban giám khảo đã hội ý xong! Vòng một: Huy chương Đồng thuộc về Hải Ly với hàm răng bọc sắt! Huy chương Bạc thuộc về Cá Mút Đá với mạng lưới tơ nhớt siêu bền! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ búa gỗ công bố, khay huy chương phát sáng bay về phía các tuyển thủ. |
| b42 | 04:49.1–04:54.6 (5.4s) | L87 | Và Huy chương Vàng ba điểm xuất sắc thuộc về Gấu Túi Wombat với tấm khiên mông bọc thép công thủ toàn diện! |  | chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường tươi cười đeo chiếc huy chương vàng lấp lánh vào cổ, giơ tay chào khán giả trong tiếng reo hò rền vang. |
| b43 | 04:54.6–05:01.5 (6.9s) | L88 | Một vòng đấu mở màn mãn nhãn! Bảng điểm Mùa ba chính thức nhảy số: Wombat dẫn đầu với ba điểm, Hagfish hai điểm, Hải Ly một điểm! |  | tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng đèn: cột điểm của Wombat vươn lên 3 điểm, Hagfish 2 điểm, Hải Ly 1 điểm; các tuyển thủ khác quyết tâm lội ngược dòng. |

### scene03 · BẢN LĨNH TÁI SINH & NGHỆ THUẬT THOÁT CHẾT KỲ DỊ · 309.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:06.3 (6.3s) | L89 | Không để khán giả phải chờ lâu, chúng ta bước ngay vào Vòng hai: Bản Lĩnh Tái Sinh và Nghệ Thuật Thoát Hiểm Khó Tin! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vung micro chỉ tay về phía sàn đấu, pháo hoa nước bắn tóe rực rỡ; tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng ô thử thách số hai mang biểu tượng vòng lặp vô cực. |
| b02 | 00:06.3–00:13.2 (6.9s) | L90 | Nếu như Vòng một là cuộc đọ sức của giáp sắt và móng vuốt cơ học, thì Vòng hai là nơi quy luật sinh học thông thường bị bẻ gãy hoàn toàn! |  | Màn hình chiếu biểu tượng tái sinh: tế bào phân chia, các nhánh mô mọc dài, và chuông sứa biến ngược thành mầm phôi; KHÔNG có anh MC trong cảnh này. |
| b03 | 00:13.2–00:23.5 (10.3s) | L91 | Đối với đa phần sinh vật sống trên Trái Đất, mất đi một cơ quan nội tạng quan trọng đồng nghĩa với cái chết cận kề. Nhưng với các quái kiệt đêm nay, đó chỉ là một sự cố nhỏ trên đường đi dạo! |  | Hình ảnh trái tim hoạt hình bị rách rồi tự đan dệt lại nguyên vẹn phát ra ánh sáng kỳ diệu; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:23.5–00:28.4 (4.9s) | L92 | Tuyển thủ đầu tiên xuất trận với nụ cười thiên thần: Kỳ Nhông Axolotl của đất nước Mexico! |  | chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói bơi nhẹ nhàng trong bể nước ngọt, sáu nhánh mang hồng xòe rộng rung rinh như cánh quạt, đôi mắt đen láy nhìn khán giả; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:28.4–00:35.7 (7.3s) | L93 | Khán giả đều biết Axolotl có thể mọc lại chân tay, nhưng công trình nghiên cứu trên tạp chí Nature 2009 đã phát hiện một sự thật chấn động hơn nhiều! |  | Mô hình hiển vi phóng to chồi tái sinh mầm chi: các tế bào màu sắc khác nhau phát sáng di chuyển có trật tự; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:35.7–00:42.1 (6.4s) | L94 | Các tế bào tại mầm tái sinh không hề quay về trạng thái tế bào gốc vô định, mà chúng lưu giữ một bộ nhớ danh tính dòng dõi cực kỳ chuẩn xác! |  | Tế bào cơ màu đỏ chỉ phân chia tạo thành cơ mới, tế bào sụn màu xanh chỉ đúc thành sụn mới, không hề bị nhầm lẫn; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:42.1–00:50.5 (8.5s) | L95 | Nhờ cơ chế này, Axolotl có thể tái tạo hoàn chỉnh một phần 3 quả tim bị tổn thương, mọc lại các thùy não và nối liền tủy sống bị đứt đoạn mà không để lại bất kỳ vết sẹo xơ hóa nào! |  | Hình ảnh đồ họa trái tim bị rách tự khép kín cơ tim đập nhịp nhàng, tủy sống nối liền các xung thần kinh phát sáng; KHÔNG có anh MC trong cảnh này. |
| b08 | 00:50.5–00:57.6 (7.0s) | L96 | Đặc biệt hơn, chúng có khả năng tiếp nhận cấy ghép nội tạng từ bất kỳ cá thể Axolotl nào khác mà hệ miễn dịch hoàn toàn không hề có phản ứng đào thải mô ghép! |  | Hai cá thể chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói bơi cạnh nhau, cấy ghép mang hồng sang nhau phát triển tự nhiên hoàn hảo; KHÔNG có anh MC trong cảnh này. |
| b09 | 00:57.6–01:05.7 (8.2s) | L97 | Bạn có thể ghép mắt, ghép chân hay thậm chí ghép cả nửa bộ não từ một chú kỳ nhông khác sang, và cơ thể chúng vẫn tiếp nhận êm ru như đồ chính hãng của mình! |  | Hình ảnh chú kỳ nhông lắp ráp các bộ phận phát sáng hoạt động trơn tru không hề bị xung đột phần mềm sinh học; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:05.7–01:12.6 (6.9s) | L98 | Cả khán đài ồ lên thán phục trước cỗ máy tái sinh hoàn hảo của thiên nhiên! Nhưng tiếng chuông ma thuật bất ngờ ngân vang từ chiếc ly thủy tinh |  | Dưới bàn giám khảo, chiếc ly phát ra ánh sáng hồng tím lung linh huyền ảo; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cúi xuống quan sát thích thú. |
| b11 | 01:12.6–01:17.9 (5.3s) | L99 | nhỏ! Xin mời nữ hoàng đảo ngược thời gian: Sứa Bất Tử dài chỉ 4,5mm! | **4,5MM** · Kích thước nhỏ bé · L/430 · [0.38, 0.72] | Hình ảnh phóng đại cực đại trên màn hình lớn: chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực trôi lơ lửng, các xúc tu mềm mại buông rủ như tơ trời; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:17.9–01:24.2 (6.3s) | L100 | Điều gì sẽ xảy ra khi một sinh vật già cỗi, bị bỏ đói hoặc chịu tổn thương thể xác nghiêm trọng? Thông thường cái chết sẽ là điểm |  | Hình ảnh đồng hồ cát chảy xuống giọt cát cuối cùng tượng trưng cho vòng đời sinh học hữu hạn; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:24.2–01:31.7 (7.5s) | L101 | kết thúc. Nhưng với Sứa Bất Tử, chúng kích hoạt một tiến trình sinh học kỳ diệu gọi là chuyển biệt hóa tế bào: toàn bộ các tế bào chuông sứa tự phân giải và chuyển |  | Chuông sứa co rút lại thành một khối mô tròn nhỏ màu hồng tím không biệt hóa; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:31.7–01:39.2 (7.5s) | L102 | hóa ngược! Khối mô này chìm xuống đáy biển, tự biến đổi trở lại thành một quần thể polyp sơ sinh hoàn toàn non trẻ, rồi từ đó lại nảy chồi sinh ra hàng trăm chú sứa con |  | Từ khối mô mọc lên các chồi polyp như rễ cây non, rồi bung nở thành đàn sứa con bơi lượn tự do; KHÔNG có anh MC trong cảnh này. |
| b15 | 01:39.2–01:47.0 (7.9s) | L103 | mới! Chu trình này có thể lặp đi lặp lại vô tận mà không bị giới hạn bởi tuổi già sinh học, biến chúng thành sinh vật duy nhất trên Trái Đất nắm giữ chìa khóa bất tử thực |  | Biểu tượng vòng lặp vô cực phát sáng rực rỡ lồng vào hình dáng của chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực; KHÔNG có anh MC trong cảnh này. |
| b16 | 01:47.0–01:57.2 (10.1s) | L104 | thụ! Giống như một người già 80 tuổi khi cảm thấy mệt mỏi có thể tự biến ngược thành một đứa bé sơ sinh trong nôi rồi lớn lên tiếp tục cuộc đời mới! Một quyền năng làm đảo lộn hoàn toàn định luật sinh học! |  | Hình minh họa hài hước: ông cụ râu tóc bạc phơ bước vào cánh cửa ma thuật biến ra thành em bé bụ bẫm cười toe toét; KHÔNG có anh MC trong cảnh này. |
| b17 | 01:57.2–02:00.1 (2.9s) | L105 | Đến lượt bậc thầy lầy lội dưới đáy đại dương bước ra: Hải |  | chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù trườn tới mép bể thi đấu, toàn thân da cam bóng lưỡng không hề có một mẩu xương cứng nào; KHÔNG có anh MC trong cảnh này. |
| b18 | 02:00.1–02:06.5 (6.4s) | L106 | Sâm! Khi bị một con cua biển khổng lồ kẹp chặt, Hải Sâm không bỏ chạy mà sử dụng chiêu thức tống xuất nội tạng kinh hoàng qua đường hậu môn! |  | Mô hình cua biển lao vào cắn, chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù quay đuôi lại phóng ra một chùm sợi trắng xóa dính nhớt như mạng nhện bủa vây cua; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:06.5–02:12.6 (6.1s) | L107 | Đó là chùm ống Cuvier chứa đầy chất keo độc tố dính chặt khiến kẻ săn mồi tê liệt, trong khi Hải Sâm ung dung trườn đi thoát |  | Con cua bị dính chặt hai càng không cử động được, chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù thong thả trườn đi với chiếc quạt giấy xua đuổi ruồi muỗi; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:12.6–02:19.9 (7.3s) | L108 | nạn! Và điều không tưởng là chỉ sau năm tuần lễ, Hải Sâm sẽ tự nuôi dưỡng và mọc lại nguyên vẹn một hệ tiêu hóa và buồng phổi nước hoàn toàn mới toanh! |  | Bên trong cơ thể chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù, bộ ruột mới mọc dần từ thành mô và hoạt động trơn tru sau 5 tuần lễ; KHÔNG có anh MC trong cảnh này. |
| b21 | 02:19.9–02:29.1 (9.2s) | L109 | Chưa hết, các nhà sinh học tại đại học Bỉ còn phát hiện: loài cá ngọc trai tí hon Carapidae thường xuyên bơi chui vào tận sâu bên trong hậu môn của Hải Sâm để làm tổ trú ẩn an toàn! |  | Chú cá ngọc trai nhỏ bơi lượn chui đầu vào phần đuôi chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù như chui vào khách sạn ngầm, chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù chỉ biết thở dài cam chịu; KHÔNG có anh MC trong cảnh này. |
| b22 | 02:29.1–02:34.1 (5.0s) | L110 | Một chiếc khách sạn đáy biển kỳ quái nhất hành tinh khiến cả đấu trường cười nghiêng ngả! |  | Khán giả ôm bụng cười ngặt nghẽo trước cảnh tượng bi hài của chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng lau nước mắt vì cười quá nhiều. |
| b23 | 02:34.1–02:38.4 (4.3s) | L111 | Và cuối cùng là màn ảo thuật biến hóa thần tốc của Bạch Tuộc Mimic! |  | chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình bơi ra giữa sân cát đáy biển, toàn thân sọc nâu trắng chuyển động nhịp nhàng; KHÔNG có anh MC trong cảnh này. |
| b24 | 02:38.4–02:45.6 (7.2s) | L112 | Không cần ẩn nấp dưới cát, Bạch Tuộc Mimic sở hữu các túi sắc tố và hệ cơ papillae vi mô có thể thay đổi màu sắc và kết cấu bề mặt da chỉ trong 200 mili-giây! | **200MS** · Biến đổi da thần tốc · R/400 · [0.62, 0.48] | Cận cảnh lớp da của chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình: từ trơn nhẵn biến thành sần sùi gai nhọn chỉ trong chớp mắt 200 mili-giây; KHÔNG có anh MC trong cảnh này. |
| b25 | 02:45.6–02:55.8 (10.2s) | L113 | Tùy theo kẻ thù đang đối diện là ai, chúng có thể tự điều khiển tám xúc tu để giả dạng thành 15 loài kịch độc khác nhau: từ rắn biển sọc đen, cá sư tử xòe gai độc, cá bơn ẩn mình, đến cả sứa biển trôi nổi! | **15 LOÀI** · Giả dạng kịch độc · L/410 · [0.38, 0.68] | Bốn khung hình biến hóa liên tiếp: chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình hóa thành rắn biển đầu đen, cá sư tử gai góc, cá bơn dẹt và sứa biển bơi lượn; KHÔNG có anh MC trong cảnh này. |
| b26 | 02:55.8–03:04.8 (8.9s) | L114 | Một năng lực ngụy trang động đạt đỉnh cao của trí tuệ đại dương! Kẻ thù nhìn vào chỉ thấy một bãi mìn sinh học đầy gai độc chết người chứ không hề nhận ra chú bạch tuộc đang cười thầm bên trong! |  | chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình nháy mắt hóm hỉnh khoe tài biến hình khiến con cá săn mồi hoảng sợ bơi lui; KHÔNG có anh MC trong cảnh này. |
| b27 | 03:04.8–03:11.1 (6.3s) | L115 | Nói về khả năng chịu đựng và thoát hiểm, Ếch Wolverine cũng sở hữu một cơ chế bảo vệ mối nối gân vô cùng kỳ lạ! |  | chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng ngồi trên bệ đá, các khớp ngón chân sau được chiếu tia laser phóng đại; KHÔNG có anh MC trong cảnh này. |
| b28 | 03:11.1–03:18.4 (7.3s) | L116 | Khác với các loài động vật có móng vuốt cố định, đầu mút xương ngón chân của ếch được giữ chặt bởi một khối mô collagen dạng sợi đàn hồi cực cao! |  | Phóng to đầu ngón chân: khối mô collagen ôm trọn lấy đốt xương nhọn như chiếc bao da tự nhiên; KHÔNG có anh MC trong cảnh này. |
| b29 | 03:18.4–03:26.2 (7.8s) | L117 | Khi áp lực co cơ vượt qua ngưỡng chịu đựng, khối mô này tự đứt ra có kiểm soát, giải phóng móng xương đâm ra ngoài mà không làm rách các mạch máu chính! |  | Xương ngón chân phóng ra ngoài trong khi các mạch nước màu lớn uốn lượn né sang hai bên an toàn; KHÔNG có anh MC trong cảnh này. |
| b30 | 03:26.2–03:31.5 (5.3s) | L118 | Điều này giải thích vì sao vết thương sau đó tự hàn gắn rất nhanh mà ếch không hề bị mất máu quá nhiều! |  | Đồ họa dòng nước màu lưu thông êm ả nuôi dưỡng vết rách mau lành; KHÔNG có anh MC trong cảnh này. |
| b31 | 03:31.5–03:36.8 (5.3s) | L119 | Và tại sao chú cá ngọc trai sống trong hậu môn Hải Sâm cả tuần mà không hề bị ngạt thở hay chết chìm? |  | Hình ảnh hiển vi soi vào buồng phổi nước bên trong phần đuôi của chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù; KHÔNG có anh MC trong cảnh này. |
| b32 | 03:36.8–03:47.8 (11.0s) | L120 | Bởi vì Hải Sâm hô hấp bằng cách liên tục hút và xả hàng lít nước biển giàu oxy qua hậu môn vào hai nhánh phổi nước, biến nơi này thành một phòng khách sạn có điều hòa nhiệt độ và bình oxy tươi mới quanh năm! |  | Dòng nước biển trong vắt giàu oxy liên tục tuần hoàn qua cơ thể chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù, chú cá nhỏ ngửa bụng bơi lội sảng khoái; KHÔNG có anh MC trong cảnh này. |
| b33 | 03:47.8–03:55.7 (7.9s) | L121 | Và ngay cả khi đối mặt với những cơn lũ quét ngập úng bất ngờ dưới lòng đất, Gấu Wombat cũng sở hữu bản lĩnh sinh tồn kỳ diệu để bảo toàn tính mạng! |  | Sa bàn mặt đất với dòng nước lũ tràn vào miệng hang ngầm sâu của chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường; KHÔNG có anh MC trong cảnh này. |
| b34 | 03:55.7–04:02.8 (7.1s) | L122 | Khi nước lũ dâng ngập các cửa hang chính, Wombat không hề hoảng loạn mà bình tĩnh di chuyển lên các ngách hang cao hơn được thiết kế theo hình chữ U ngược! |  | Mặt cắt hang ngầm: ngách hang chữ U giữ lại một túi khí oxy khổng lồ giúp chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường ngồi khô ráo an toàn; KHÔNG có anh MC trong cảnh này. |
| b35 | 04:02.8–04:09.1 (6.4s) | L123 | Những túi khí tự nhiên này giúp chúng sống sót ngon lành dưới lòng đất suốt nhiều ngày liền chờ cho đến khi nước lũ rút hoàn toàn! |  | chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường ung dung ngồi trong túi khí hang ngầm nhai cỏ khô dự trữ, bên ngoài dòng nước lũ chảy xiết vô hại; KHÔNG có anh MC trong cảnh này. |
| b36 | 04:09.1–04:16.5 (7.4s) | L124 | Không chỉ có khả năng mọc lại chi và nội tạng, Kỳ Nhông Axolotl còn có thể tái tạo hoàn chỉnh tế bào võng mạc mắt và thấu kính quang học tinh khiết! |  | Nhãn cầu của chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói phát sáng trong suốt, các tế bào thụ cảm thị giác tự sắp xếp ngay ngắn; KHÔNG có anh MC trong cảnh này. |
| b37 | 04:16.5–04:23.9 (7.4s) | L125 | Khi bị tổn thương thị giác, các tế bào sắc tố biểu mô mống mắt tự động chuyển hóa thành tế bào gốc phôi thai để dệt lại một thấu kính mắt mới toanh không hề có vết mờ đục! |  | Thấu kính mắt trong veo như giọt pha lê phản chiếu ánh sáng rực rỡ, chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói chớp mắt nhìn rõ mồn một; KHÔNG có anh MC trong cảnh này. |
| b38 | 04:23.9–04:30.9 (7.0s) | L126 | Còn Hải Sâm thì sở hữu khả năng tái tạo tế bào tuyến sinh dục và mô bài tiết chỉ trong vòng vài tuần lễ sau các cuộc giải phẫu tự thân khốc liệt! |  | Các cơ quan sinh học bên trong chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù tự nảy mầm và hoàn thiện trơn tru như một phép màu tự nhiên; KHÔNG có anh MC trong cảnh này. |
| b39 | 04:30.9–04:35.9 (5.1s) | L127 | Điều kinh ngạc nhất là hệ thống tái sinh của Hải Sâm được kích hoạt bởi các phân tử tín hiệu hóa học peptide vô cùng đặc |  | Kính hiển vi hiển thị các chuỗi phân tử peptide tín hiệu tỏa ra từ mô tổn thương của chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù kích thích tế bào gốc phân chia; KHÔNG có anh MC trong cảnh này. |
| b40 | 04:35.9–04:43.1 (7.1s) | L128 | biệt! Chỉ trong vòng 24 giờ sau khi tự phóng nội tạng, các tế bào gốc biểu mô ruột đã kết tụ thành mầm mô tạng non trẻ khỏe mạnh! |  | Mô phỏng mầm ruột non màu hồng nhạt hình thành dọc theo khoang cơ thể chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù; KHÔNG có anh MC trong cảnh này. |
| b41 | 04:43.1–04:49.8 (6.7s) | L129 | Kết quả Vòng hai của ban giám khảo: Huy chương Đồng thuộc về Bạch Tuộc Mimic với màn biến hình 15 loài kịch độc! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ búa, trao huy chương đồng phát sáng cho chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình. |
| b42 | 04:49.8–04:55.1 (5.3s) | L130 | Huy chương Bạc thuộc về Kỳ Nhông Axolotl với bộ nhớ tái sinh mô hoàn hảo không sẹo! |  | chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói mỉm cười nhận tấm huy chương bạc đeo quanh cổ rạng rỡ. |
| b43 | 04:55.1–05:01.5 (6.4s) | L131 | Và Huy chương Vàng ba điểm xuất sắc thuộc về tuyển thủ bé hạt tiêu Sứa Bất Tử với vòng lặp đảo ngược thời gian tế bào vô cực! |  | chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực nhận huy chương vàng lơ lửng, cả đấu trường reo hò rực rỡ pháo hoa. |
| b44 | 05:01.5–05:09.5 (8.0s) | L132 | Bảng điểm sau hai vòng thi đấu đảo chiều ngoạn mục: Wombat và Sứa Bất Tử cùng chia sẻ ngôi đầu với ba điểm, Hagfish và Axolotl bám sát với hai điểm! |  | tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) cập nhật điểm số: Wombat 3, Sứa Bất Tử 3, Hagfish 2, Axolotl 2, Hải Ly 1, Bạch Tuộc Mimic 1; cuộc đua vương miện ngày càng nóng bỏng! |

### scene04 · PHẢN XẠ SIÊU TỐC & GIÁC QUAN VƯỢT TRỘI DƯỚI LÒNG ĐẤT · 280.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:06.6 (6.6s) | L133 | Đấu trường lại rực lửa! Chào mừng quý vị đến với Vòng ba: Phản Xạ Siêu Tốc và Những Giác Quan Kỳ Dị Vượt Trội! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vung tay kích hoạt hệ thống đồng hồ bấm giờ kỹ thuật số tốc độ cao trên trần nhà; tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng ô thử thách số ba mang hình tia chớp và xúc tu. |
| b02 | 00:06.6–00:13.6 (7.0s) | L134 | Nếu bạn nghĩ mắt là cửa sổ tâm hồn duy nhất để quan sát thế giới, thì các tuyển thủ Vòng ba sẽ khiến bạn phải suy nghĩ lại từ đầu! |  | Màn hình chiếu biểu tượng sóng âm, xung xúc giác và các bong bóng khí dò tìm mục tiêu; KHÔNG có anh MC trong cảnh này. |
| b03 | 00:13.6–00:22.3 (8.7s) | L135 | Ở thế giới bóng tối dưới lòng đất hay đáy biển sâu đục ngầu, thị giác thông thường hoàn toàn trở nên vô dụng, nhường chỗ cho những giác quan cơ học và sóng âm tinh vi nhất! |  | Đồ họa bóng tối bao trùm, các tia quét rada sinh học tỏa ra từ mũi và xúc tu của các tuyển thủ; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:22.3–00:26.6 (4.3s) | L136 | Tiến vào đường hầm thử nghiệm bóng tối: sát thủ săn mồi đầm lầy Bắc Mỹ, Chuột Chũi Mũi Sao! |  | chú Chuột Chũi Mũi Sao hoạt hình lông đen nhung mượt mà, mũi xòe ra 22 xúc tu đỏ hồng như bông hoa sao biển, đeo kính râm mù lòa nhưng phản xạ siêu thanh đeo kính râm đen ngầu, bước vào căn phòng tối tăm phủ đầy bùn ẩm, hai mươi hai chiếc xúc tu đỏ hồng trên mũi xòe rộng rung rinh; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:26.6–00:35.9 (9.3s) | L137 | Mặc dù đôi mắt bị thoái hóa gần như mù lòa, chiếc mũi chứa 25.000 cơ quan thụ cảm của Chuột Chũi Mũi Sao lại là cơ quan xúc giác nhạy bén nhất từng được ghi nhận trong lịch sử khoa học! | **25.000 DÂY** · Cơ quan Eimer · R/410 · [0.65, 0.48] | Hình ảnh giải phẫu hiển vi chiếc mũi: hai mươi hai xúc tu hồng chứa hai mươi lăm ngàn cơ quan Eimer siêu nhỏ; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:35.9–00:44.4 (8.5s) | L138 | 25.000 cơ quan Eimer này chứa mạng lưới dây thần kinh cảm giác dày đặc đến mức: hơn 50% diện tích vỏ não của chú chuột chũi này chỉ dùng để giải mã tín hiệu từ chiếc mũi | **50% NÃO** · Dành riêng cho mũi sao · L/400 · [0.35, 0.72] | Đồ họa bán cầu não bộ hoạt hình: một nửa bán cầu não phát sáng màu vàng rực rỡ tương ứng với hình dạng chiếc mũi sao 22 cánh; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:44.4–00:49.3 (4.9s) | L139 | sao! Và khi một ấu trùng côn trùng xuất hiện, chiếc đồng hồ đếm mili-giây của ban tổ chức bắt đầu đếm ngược! |  | Một chú ấu trùng nhỏ rơi xuống mặt bùn phát ra tín hiệu rung động vi mô; KHÔNG có anh MC trong cảnh này. |
| b08 | 00:49.3–00:57.1 (7.7s) | L140 | Chạm! Nhận diện! Nuốt chửng! Toàn bộ tiến trình chỉ diễn ra trong đúng 0,12 giây đồng hồ! Nhanh hơn một cái chớp mắt của con người tới ba lần! | **0,12 GIÂY** · Ăn nhanh nhất · R/420 · [0.62, 0.55] | Chuột Chũi chú Chuột Chũi Mũi Sao hoạt hình lông đen nhung mượt mà, mũi xòe ra 22 xúc tu đỏ hồng như bông hoa sao biển, đeo kính râm mù lòa nhưng phản xạ siêu thanh lao tới đớp gọn ấu trùng, đồng hồ dừng ở con số 0,12 giây, đạt kỷ lục Guiness thế giới hoạt hình; KHÔNG có anh MC trong cảnh này. |
| b09 | 00:57.1–01:04.3 (7.2s) | L141 | Chưa hết, giáo sư Kenneth Catania tại đại học Vanderbilt còn phát hiện một tuyệt kỹ không tưởng: Chuột Chũi Mũi Sao có thể ngửi được mùi thức ăn dưới nước! |  | chú Chuột Chũi Mũi Sao hoạt hình lông đen nhung mượt mà, mũi xòe ra 22 xúc tu đỏ hồng như bông hoa sao biển, đeo kính râm mù lòa nhưng phản xạ siêu thanh lặn dưới làn nước trong, chiếc mũi thổi ra hai quả bong bóng khí tròn xoe chạm vào con mồi; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:04.3–01:13.3 (9.0s) | L142 | Bằng cách liên tục thổi các bong bóng khí từ lỗ mũi chạm vào vật thể rồi hít ngược bong bóng trở lại xoang mũi, chúng thu gom các phân tử mùi lơ lửng trong nước để ngửi chính xác tuyệt đối! |  | Bong bóng khí hút ngược lại mũi, các thụ thể khứu giác phát sáng tín hiệu thức ăn ngon lành; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:13.3–01:18.9 (5.6s) | L143 | Động vật có vú duy nhất trên Trái Đất có thể hít thở và ngửi mùi thức ăn trong môi trường ngập nước mà không hề bị sặc! |  | chú Chuột Chũi Mũi Sao hoạt hình lông đen nhung mượt mà, mũi xòe ra 22 xúc tu đỏ hồng như bông hoa sao biển, đeo kính râm mù lòa nhưng phản xạ siêu thanh giơ ngón tay cái tự tin dưới nước, bọt khí lấp lánh quanh mũi sao rực rỡ; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:18.9–01:25.6 (6.7s) | L144 | Động vật có vú đầu tiên trên thế giới ngửi được mùi khi đang ngụp lặn dưới nước! Một tràng pháo tay cho Chuột Chũi Mũi Sao! |  | Khán đài vỗ tay rào rào kinh ngạc trước pha trình diễn ảo diệu; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng giơ micro tròn mắt ngỡ ngàng. |
| b13 | 01:25.6–01:31.7 (6.1s) | L145 | Nhưng đối thủ của chú ta, Bạch Tuộc Mimic, lập tức bước lên với hệ thần kinh phân tán dị thường bậc nhất đại dương! |  | chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình bơi lượn trong bể kính, tám chiếc xúc tu múa lượn tự do theo các quỹ đạo độc lập hoàn toàn; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:31.7–01:39.0 (7.2s) | L146 | Các nhà khoa học thần kinh phát hiện: 2/3 tổng số nơ-ron não bộ của bạch tuộc không hề nằm ở hộp sọ trung tâm, mà trải dài dọc theo tám xúc tu! |  | Sơ đồ thần kinh phát sáng: não trung tâm nhỏ, trong khi 8 xúc tu tỏa sáng rực rỡ với hàng triệu nơ-ron hoạt động độc lập; KHÔNG có anh MC trong cảnh này. |
| b15 | 01:39.0–01:48.5 (9.6s) | L147 | Điều này có nghĩa là mỗi xúc tu của Bạch Tuộc Mimic giống như một bộ não thu nhỏ: có thể tự nếm vị giác qua các giác hút, tự sờ chạm, tự suy nghĩ và giải quyết chướng ngại vật mà không cần chờ lệnh từ não bộ! |  | Một xúc tu mở nắp chai, một xúc tu thò vào hốc đá bắt cua, một xúc tu khác tự uốn éo xua đuổi cá nhỏ; KHÔNG có anh MC trong cảnh này. |
| b16 | 01:48.5–01:54.0 (5.4s) | L148 | Khi bị săn đuổi, tám xúc tu có thể tự động phối hợp điều phối các bước chạy mà não trung tâm chỉ cần tập trung tính toán đường thoát |  | chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình uốn 8 xúc tu thoăn thoắt vượt qua mê cung đá ngầm cực kỳ mượt mà; KHÔNG có anh MC trong cảnh này. |
| b17 | 01:54.0–02:00.7 (6.7s) | L149 | hiểm! Mỗi xúc tu vừa là cánh tay, vừa là con mắt xúc giác, vừa là chiếc lưỡi nếm vị thức ăn! Một mạng lưới trí tuệ phân tán siêu việt! |  | Đồ họa phóng to giác hút trên xúc tu chứa các thụ thể hóa học phát sáng khi nếm chất hữu cơ trong nước; KHÔNG có anh MC trong cảnh này. |
| b18 | 02:00.7–02:04.7 (4.1s) | L150 | Đến lượt Ếch Lông Wolverine thể hiện giác quan thích nghi dòng suối chảy xiết! |  | chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng ngồi dưới dòng thác nước nhân tạo đổ ào ào; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:04.7–02:10.4 (5.7s) | L151 | Lớp lông tơ kỳ lạ ở hai bên hông của ếch đực chứa đầy mạng lưới mao mạch máu và các tế bào thụ cảm cơ |  | Phóng to các sợi lông tơ bên hông: các mao mạch nước màu đỏ li ti đan xen với các sợi thần kinh thụ cảm dòng chảy; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:10.4–02:18.5 (8.1s) | L152 | học vi mô! Khi ngồi dưới đáy suối đục ngầu cuồn cuộn bùn cát, lớp lông này vừa hấp thụ oxy hòa tan trong nước, vừa cảm nhận được sự thay đổi áp suất dòng chảy nhỏ nhất từ kẻ săn mồi bơi |  | Dòng nước cuộn sóng mang các đường xung áp suất chạm vào lông tơ, chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng né tránh cú đớp của cá dữ trong gang tấc; KHÔNG có anh MC trong cảnh này. |
| b21 | 02:18.5–02:28.2 (9.7s) | L153 | qua! Và kỹ sư Hải Ly cũng sở hữu đôi mắt bơi lặn siêu việt: lớp mí mắt thứ ba trong suốt hoạt động như chiếc kính bơi chuyên nghiệp, giúp chúng quan sát rõ mồn một từng cành cây dưới đáy sông đục ngầu! |  | Cận cảnh mắt của chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo: mí mắt thứ ba khép lại như màng kính bảo hộ trong suốt, van tai và mũi tự động đóng kín; KHÔNG có anh MC trong cảnh này. |
| b22 | 02:28.2–02:36.8 (8.6s) | L154 | Cá Mút Đá Hagfish dù sống dưới đáy biển tăm tối 1.000m và mắt thoái hóa hoàn toàn thành vệt sắc tố dưới da, nhưng chúng sở hữu chiếc mũi thính nhạy số một đại dương! |  | chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện bơi trong làn nước đen thẳm, một lỗ mũi duy nhất trên đỉnh đầu mở rộng hút nước biển; KHÔNG có anh MC trong cảnh này. |
| b23 | 02:36.8–02:45.9 (9.1s) | L155 | Khác với mọi loài cá có hai lỗ mũi, Hagfish chỉ có một lỗ mũi duy nhất dẫn thẳng nước biển vào một túi khứu giác khổng lồ kết nối trực tiếp với thùy khứu giác của não bộ! |  | Cắt lớp đầu Hagfish: luồng nước biển mang phân tử mùi đi thẳng vào túi khứu giác phát sáng tín hiệu thần kinh; KHÔNG có anh MC trong cảnh này. |
| b24 | 02:45.9–02:53.9 (8.0s) | L156 | Chúng có thể đánh hơi thấy mùi một xác cá voi chìm cách xa hàng chục cây số giữa đại dương bao la, rồi bơi thẳng tới đích mà không cần đến một tia sáng nào! |  | Các đường sóng khứu giác dẫn đường cho đàn chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện bơi xuyên qua bóng đêm đại dương tìm tới xác cá voi chính xác tuyệt đối; KHÔNG có anh MC trong cảnh này. |
| b25 | 02:53.9–03:00.2 (6.4s) | L157 | Còn Kiến Nổ Cảm Tử thì sở hữu cặp râu cảm biến hóa học phát hiện tín hiệu pheromone xâm nhập chỉ trong 50 mili-giây! |  | Cặp râu của chú Kiến Nổ dũng cảm bảo vệ tổ hoạt hình màu đỏ cam, đeo ba lô chứa chất lỏng vàng phát sáng, đội mũ bảo hộ chống độc, ánh mắt quả cảm kiên cường rung rinh bắt trọn từng phân tử mùi lạ trong không khí báo động toàn tổ kiến; KHÔNG có anh MC trong cảnh này. |
| b26 | 03:00.2–03:06.7 (6.5s) | L158 | Chẳng có một tên gián điệp hay kẻ săn mồi nào có thể lén lút tiếp cận cửa tổ mà không bị cặp râu siêu nhạy này lật tẩy! |  | Chú kiến gác cửa lập tức vào vị trí sẵn sàng chiến đấu trước khi kẻ thù kịp nhìn thấy lối vào; KHÔNG có anh MC trong cảnh này. |
| b27 | 03:06.7–03:12.7 (6.0s) | L159 | Không chỉ có đôi mắt mí thứ ba, Hải Ly còn sở hữu hệ thống cảnh báo sớm bằng sóng âm mặt nước vô cùng lợi hại! |  | chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo nổi trên mặt hồ phẳng lặng, chiếc đuôi dẹt to bản giơ cao chuẩn bị đập nước; KHÔNG có anh MC trong cảnh này. |
| b28 | 03:12.7–03:20.3 (7.6s) | L160 | Mỗi khi phát hiện bóng dáng kẻ săn mồi như chó sói hay gấu xám từ xa, Hải Ly dùng chiếc đuôi dẹt nặng nề đập cực mạnh xuống mặt nước tạo nên tiếng nổ rầm vang dội khắp thung lũng! |  | Chiếc đuôi đập mạnh xuống nước tung bọt trắng xóa, âm thanh phát ra to như tiếng súng nổ vang xa cả cây số; KHÔNG có anh MC trong cảnh này. |
| b29 | 03:20.3–03:27.1 (6.8s) | L161 | Âm thanh đập đuôi này truyền đi cả trong không khí lẫn dưới đáy nước, cảnh báo cho toàn bộ bầy đàn lặn sâu xuống đáy bùn trốn thoát chỉ trong 3 giây! |  | Đàn hải ly con lập tức lặn ngụp biến mất dưới dòng nước sâu mát lạnh an toàn tuyệt đối; KHÔNG có anh MC trong cảnh này. |
| b30 | 03:27.1–03:34.6 (7.5s) | L162 | Để phối hợp nhịp nhàng giữa 22 xúc tu, não bộ của Chuột Chũi Mũi Sao xử lý các xung thần kinh cảm giác với tốc độ nhanh gấp 10 lần dây thần kinh mắt người! |  | Các tia sáng xung thần kinh chạy dọc từ 22 xúc tu về trung tâm vỏ não với tốc độ ánh sáng; KHÔNG có anh MC trong cảnh này. |
| b31 | 03:34.6–03:41.8 (7.2s) | L163 | Mỗi khi xúc tu chạm nhẹ vào một vật thể lạ, bộ não phân tích lập tức cấu trúc vật liệu, độ ẩm, độ nhớt và nhiệt độ của đối tượng trong vòng vài phần nghìn giây! |  | Màn hình hiển thị bảng phân tích phổ vật liệu chi tiết hiện ra trong nháy mắt khi chiếc mũi chạm nhẹ; KHÔNG có anh MC trong cảnh này. |
| b32 | 03:41.8–03:49.3 (7.5s) | L164 | Đó là lý do vì sao chúng có thể phân biệt chính xác đâu là thức ăn bổ dưỡng và đâu là hạt cát vô giá trị trong nháy mắt mà không bao giờ nuốt nhầm! |  | chú Chuột Chũi Mũi Sao hoạt hình lông đen nhung mượt mà, mũi xòe ra 22 xúc tu đỏ hồng như bông hoa sao biển, đeo kính râm mù lòa nhưng phản xạ siêu thanh nhổ hạt sỏi ra ngoài và nuốt trọn chú giun đất béo ngậy một cách điêu luyện; KHÔNG có anh MC trong cảnh này. |
| b33 | 03:49.3–03:57.4 (8.1s) | L165 | Các nhà khoa học tại đại học Vanderbilt phát hiện: vùng vỏ não cảm giác của Chuột Chũi Mũi Sao dành tới 50% diện tích chỉ để xử lý tín hiệu từ chiếc mũi! |  | Đồ họa bản đồ não bộ hiển thị một nửa bán cầu não phát sáng rực rỡ để giải mã xúc giác của 22 xúc tu; KHÔNG có anh MC trong cảnh này. |
| b34 | 03:57.4–04:03.3 (6.0s) | L166 | Độ phân giải xúc giác trên chiếc mũi này chi tiết và sắc nét đến mức tương đương với độ nhạy thị giác của mắt đại bàng trên bầu trời! |  | Hình ảnh so sánh chiếc mũi sao phóng to như một ống kính hiển vi điện tử siêu phân giải dò tìm từng hạt phân tử; KHÔNG có anh MC trong cảnh này. |
| b35 | 04:03.3–04:10.7 (7.3s) | L167 | Nhờ đó, dù sống cả đời trong lòng đất đen đặc chẳng hề có tia sáng, Chuột Chũi Mũi Sao vẫn nhìn thấy thế giới bằng xúc giác với độ chân thực đến kinh ngạc! |  | Mô hình 3D đường hầm tối đen bỗng bừng sáng các đường vân địa hình khi chú Chuột Chũi Mũi Sao hoạt hình lông đen nhung mượt mà, mũi xòe ra 22 xúc tu đỏ hồng như bông hoa sao biển, đeo kính râm mù lòa nhưng phản xạ siêu thanh quét nhẹ xúc tu; KHÔNG có anh MC trong cảnh này. |
| b36 | 04:10.7–04:18.2 (7.5s) | L168 | Ban giám khảo xin công bố điểm số Vòng ba! Huy chương Đồng thuộc về Ếch Lông Wolverine với bộ lông tơ thụ cảm áp suất dòng suối! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ búa, trao huy chương đồng phát sáng cho chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng. |
| b37 | 04:18.2–04:23.7 (5.5s) | L169 | Huy chương Bạc thuộc về Bạch Tuộc Mimic với tám xúc tu mang trí tuệ nơ-ron độc lập phi thường! |  | chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình dùng một xúc tu đón lấy tấm huy chương bạc lấp lánh rồi đeo lên cổ. |
| b38 | 04:23.7–04:31.9 (8.2s) | L170 | Và Huy chương Vàng ba điểm xuất sắc thuộc về Chuột Chũi Mũi Sao với kỷ lục săn mồi 0,12 giây cùng tuyệt chiêu ngửi mùi dưới nước bằng bong bóng khí! |  | chú Chuột Chũi Mũi Sao hoạt hình lông đen nhung mượt mà, mũi xòe ra 22 xúc tu đỏ hồng như bông hoa sao biển, đeo kính râm mù lòa nhưng phản xạ siêu thanh đứng trên bục vinh quang nhận huy chương vàng, 22 xúc tu đỏ hồng nhấp nháy ăn mừng kiêu hãnh. |
| b39 | 04:31.9–04:40.5 (8.6s) | L171 | Cục diện bảng tổng sắp sau ba vòng đấu vô cùng gay cấn: Wombat, Sứa Bất Tử và Chuột Chũi Mũi Sao cùng nắm giữ ba điểm! Đấu trường ngày càng kịch tính nghẹt thở! |  | tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) cập nhật: Wombat 3, Sứa Bất Tử 3, Chuột Chũi Sao 3, Bạch Tuộc Mimic 2, Hagfish 2, Axolotl 2, Hải Ly 1, Ếch dị nhân móng vuốt hoạt hình đáng yêu 1; khoảng cách điểm số sít sao chưa từng thấy! |

### scene05 · GIỜ GIẢI LAO HẬU TRƯỜNG & NHỮNG PHA KHÓ ĐỠ CỦA DỊ NHÂN · 277.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:06.5 (6.5s) | L172 | Sau ba vòng thi đấu căng như dây đàn, ban tổ chức xin thông báo: toàn thể đấu trường bước vào 30 phút giải lao hậu |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng lau mồ hôi trên trán, đưa tay ra hiệu tiếng chuông nghỉ giải lao ngân vang rộn rã; tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) hiện chữ giải lao hoạt hình. |
| b02 | 00:06.5–00:12.3 (5.8s) | L173 | trường! Các tuyển thủ tạm lui về khu vực phòng thay đồ để nạp năng lượng và chuẩn bị cho các vòng đấu khốc liệt tiếp theo. |  | Hành lang phòng thay đồ hoạt hình với mười cánh cửa gắn bảng tên mười con vật; KHÔNG có anh MC trong cảnh này. |
| b03 | 00:12.3–00:20.8 (8.5s) | L174 | Nhưng ngay lúc này, camera giấu kín của ban tổ chức đã ghi lại hàng loạt khoảnh khắc dở khóc dở cười khiến bà Cú giám khảo suýt ngất xỉu! |  | Màn hình hậu trường sáng lên, bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ đeo kính tròn cầm đèn pin đi kiểm tra an ninh từng phòng; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:20.8–00:26.6 (5.8s) | L175 | Ở phòng nghỉ số một của kỹ sư Hải Ly: bồn rửa mặt của ban tổ chức bị rò rỉ nước, phát ra tiếng róc rách nho nhỏ! |  | Vòi nước trong phòng rửa tay chảy róc rách từng giọt xuống bồn sứ trắng; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:26.6–00:33.4 (6.8s) | L176 | Một nghiên cứu của giáo sư Dietrich Müller-Schwarze đã chứng minh: Hải Ly bị một chứng ám ảnh cưỡng chế sinh học cực nặng với tiếng nước chảy! |  | chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo đang ôm đầu bứt tai, đôi mắt mở to hoảng hốt trước âm thanh nước chảy; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:33.4–00:39.9 (6.5s) | L177 | Chúng không hề bận tâm xem nước chảy ở đâu, chỉ cần nghe thấy tiếng róc rách là bản năng lập tức ra lệnh: phải đắp đập bịt kín ngay tức khắc! |  | chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo vớ lấy thảm lau chân, xà phòng, khăn tắm và bùn đất trát kín mít chiếc bồn rửa mặt thành một con đập cao ngất ngưởng; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:39.9–00:47.6 (7.8s) | L178 | Thậm chí khi chiếc loa thông báo của anh MC phát ra tiếng nhạc nền suối reo, Hải Ly đã phi ra vác nguyên một khúc gỗ to đùng chèn cứng họng loa! |  | chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo nhét khúc gỗ vào loa phóng thanh trần nhà, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng dưới ngơ ngác không nói nên lời; KHÔNG có anh MC trong cảnh này. |
| b08 | 00:47.6–00:53.8 (6.2s) | L179 | Các nhân viên hậu đài phải mất nửa tiếng đồng hồ dùng búa nhổ đinh để cạy con đập mini trong nhà vệ sinh của Hải Ly ra ngoài! |  | Hai kỹ thuật viên toát mồ hôi hì hục dọn bùn đất và cành cây khỏi bồn rửa mặt trong sự bất lực; KHÔNG có anh MC trong cảnh này. |
| b09 | 00:53.8–01:01.3 (7.6s) | L180 | Trong khi đó, ở khu vực phòng chờ của Ếch Wolverine và Kỳ Nhông Axolotl, một cuộc tranh luận nảy lửa của hai đại diện lưỡng cư đang nổ ra! |  | chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng và chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói ngồi đối diện nhau qua chiếc bàn kính, hai bên vung tay vung chân tranh cãi sôi nổi; KHÔNG |
| b10 | 01:01.3–01:06.0 (4.6s) | L181 | Ếch Wolverine khoe móng xương bảo: Bẻ xương làm vuốt mới là đỉnh cao chiến binh ngầu lòi! |  | chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng giơ ngón chân có vuốt xương trắng muốt nhọn hoắt khoe dáng; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:06.0–01:14.2 (8.3s) | L182 | Kỳ Nhông Axolotl mỉm cười lắc đầu đáp lại: Tự làm đau mình làm chi anh ơi, cứ để đối thủ cắn một miếng rồi mình mọc lại cái mới xinh xắn có phải nhàn nhã hơn |  | chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói xòe nhánh mang hồng rung rinh cười tít mắt, khiến Ếch dị nhân móng vuốt hoạt hình đáng yêu gãi đầu cạn lời; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:14.2–01:21.9 (7.7s) | L183 | không! Còn ở góc phòng khách, chú Bạch Tuộc Mimic đang rảnh rỗi trổ tài biến hình thành một chiếc gối ôm sofa bằng nhung nâu sọc trắng! |  | Chiếc ghế sofa phòng khách bỗng có một chiếc gối ôm mềm mại sọc vằn nâu trắng; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:21.9–01:31.1 (9.2s) | L184 | Bà Cú giám khảo bước vào mệt mỏi định ngồi phịch xuống nghỉ lưng, thì chiếc gối ôm bỗng thò ra tám cái xúc tu ôm chầm lấy bà Cú làm bà thét lên một tiếng kinh hoàng! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ giật bắn mình nhảy dựng lên trần nhà, chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình hiện nguyên hình cười khanh khách xin lỗi rối rít; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:31.1–01:37.3 (6.2s) | L185 | Dạ em chỉ muốn thử xem khả năng ngụy trang của em có lừa được mắt cú vọ của giám khảo không thôi mà! |  | chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình gãi đầu bối rối thu xúc tu lại ngoan ngoãn; KHÔNG có anh MC trong cảnh này. |
| b15 | 01:37.3–01:43.8 (6.4s) | L186 | Ở một góc sân khác, Kỳ Nhông Axolotl đang tận hưởng dịch vụ tắm bùn khoáng nóng do ban tổ chức chu cấp với vẻ mặt thỏa mãn vô cùng! |  | chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói ngâm mình trong bồn bùn khoáng sủi bọt ấm áp, hai tay nhỏ đặt lên mép bồn thư giãn tuyệt đối; KHÔNG có anh MC trong cảnh này. |
| b16 | 01:43.8–01:51.0 (7.3s) | L187 | Chú kỳ nhông cười tít mắt bảo: Đấu trường sinh tồn gì mà sướng như đi nghỉ dưỡng năm sao thế này, em muốn ở đây thi đấu quanh năm luôn quá! |  | chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói đắp hai lát dưa leo lên mắt thư giãn, xung quanh là bong bóng xà phòng bay lơ lửng ngộ nghĩnh; KHÔNG có anh MC trong cảnh này. |
| b17 | 01:51.0–01:58.0 (7.0s) | L188 | Trong khi đó, anh chàng Ếch Wolverine đang miệt mài ngồi mài lại bộ móng vuốt xương vào mép bàn đá cẩm thạch kêu ken két nghe rợn cả người! |  | chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng ngồi co chân sau tỉ mỉ mài sắc từng chiếc vuốt xương trắng muốt, ánh mắt lóe lên tia sáng quyết tâm; KHÔNG có anh MC trong cảnh này. |
| b18 | 01:58.0–02:05.2 (7.2s) | L189 | Thậm chí chú cá ngọc trai Carapidae trong hậu môn Hải Sâm còn gọi thêm cả đàn bạn bè bơi vào tổ chức một buổi hòa nhạc mini dưới nước! |  | Ba chú cá ngọc trai nhỏ đeo kính râm cầm nhạc cụ mini chơi nhạc trong bụng chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù, làm chú ta run rẩy lắc lư cười ra nước mắt; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:05.2–02:14.4 (9.2s) | L190 | Hải Sâm bèn thử gồng các cơ co thắt để tống cổ đàn khách trọ ồn ào ra ngoài, nhưng đàn cá ngọc trai lại tưởng đó là dịch vụ mát-xa thủy lực miễn phí nên càng khoái chí nằm im! |  | chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù thở dài ngao ngán phẩy quạt giấy, mặt biểu cảm bất lực tột cùng khiến cả hội trường cười nghiêng ngả; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:14.4–02:20.6 (6.2s) | L191 | Thí sinh Hải Ly! Tôi cấm anh biến phòng vệ sinh của ban giám khảo thành công trường xây dựng thủy điện nhé! |  | Cận cảnh bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ chống hai cánh ngang hông, mặt đỏ bừng gắt gỏng chỉ vào bãi chiến trường đắp đập. |
| b21 | 02:20.6–02:26.2 (5.6s) | L192 | Bà Cú giám khảo vừa bước sang phòng số hai của Gấu Wombat thì lại đụng phải một cảnh tượng kỳ quặc không kém! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ hé cửa nhìn vào phòng số hai, ánh mắt mở to đầy nghi hoặc; KHÔNG có anh MC trong cảnh này. |
| b22 | 02:26.2–02:33.5 (7.3s) | L193 | Anh chàng Wombat đang thong thả ngồi trên bồn cầu, chăm chú xếp từng khối phân hình lập phương thành một kim tự tháp vuông vức cực kỳ nghệ thuật! |  | chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường ngồi nghiêm túc xếp từng viên phân hình khối lập phương sắc cạnh như những viên gạch xếp hình Lego; KHÔNG có anh MC trong cảnh này. |
| b23 | 02:33.5–02:41.5 (8.0s) | L194 | Tại sao phân của Wombat lại có hình lập phương độc nhất vô nhị trên thế giới? Nghiên cứu đoạt giải Ig Nobel vật lý của tiến sĩ Patricia Yang đã giải mã bí ẩn |  | Sơ đồ giải phẫu đường ruột hoạt hình: phần ruột già dài dằng dặc, đoạn cuối cùng sáng lên; KHÔNG có anh MC trong cảnh này. |
| b24 | 02:41.5–02:48.6 (7.1s) | L195 | này! Chỉ có 8% đoạn ruột già cuối cùng của Wombat sở hữu cấu trúc mô cơ đàn hồi không đồng đều: hai rãnh cơ cứng chắc và hai rãnh cơ mềm | **8% RUỘT** · Co giãn đàn hồi · R/410 · [0.65, 0.48] | Đồ họa ruột già ép phân: các vách cơ co bóp nén chất thải thành các cạnh góc vuông chín mươi độ hoàn hảo; KHÔNG có anh MC trong cảnh này. |
| b25 | 02:48.6–02:56.0 (7.4s) | L196 | dẻo! Mỗi ngày, Wombat đúc ra từ 80 đến 100 viên phân lập phương sắc cạnh như xúc xắc để đánh dấu lãnh thổ trên các tảng đá mà không sợ bị lăn xuống | **100 VIÊN** · Phân hình lập phương · L/430 · [0.35, 0.72] | chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường giơ ngón tay cái tự hào chỉ vào kim tự tháp 100 viên gạch vuông vức không hề lăn lóc; KHÔNG có anh MC trong cảnh này. |
| b26 | 02:56.0–03:02.6 (6.7s) | L197 | dốc! Khả năng đúc hình học chuẩn xác tới mức các nhà sản xuất gạch xây dựng của con người cũng phải trầm trồ xin bí quyết học hỏi! |  | Kỹ sư xây dựng hoạt hình cầm thước đo góc 90 độ của viên phân vuông vức thán phục; KHÔNG có anh MC trong cảnh này. |
| b27 | 03:02.6–03:08.2 (5.5s) | L198 | Dạ thưa cô giám khảo, em vừa đúc xong mẻ mới nóng hổi tặng ban tổ chức làm kỷ niệm nè cô! |  | chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường bê khay phân vuông vức chìa ra mời mọc với vẻ mặt chân chất thật thà; bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ bịt mũi lùi lại ba bước; KHÔNG có anh MC trong cảnh này. |
| b28 | 03:08.2–03:12.2 (4.1s) | L199 | Sang đến phòng của Kiến Nổ Cảm Tử, không khí lại căng thẳng như một kho thuốc súng sắp |  | chú Kiến Nổ dũng cảm bảo vệ tổ hoạt hình màu đỏ cam, đeo ba lô chứa chất lỏng vàng phát sáng, đội mũ bảo hộ chống độc, ánh mắt quả cảm kiên cường ngồi thiền trên chiếc nệm bông mềm, hai tay chắp trước ngực hít thở sâu; KHÔNG có anh MC trong cảnh này. |
| b29 | 03:12.2–03:18.6 (6.4s) | L200 | nổ! Chú kiến nhỏ nơm nớp lo sợ ai đó vô tình vỗ mạnh vào vai làm vỡ tuyến keo dính trên bụng, kích nổ ba lô độc tố màu vàng sáng rực! |  | Đồ họa tia sét cảnh báo quanh ba lô keo dính của chú Kiến Nổ dũng cảm bảo vệ tổ hoạt hình màu đỏ cam, đeo ba lô chứa chất lỏng vàng phát sáng, đội mũ bảo hộ chống độc, ánh mắt quả cảm kiên cường, mỗi cử động nhỏ đều phải thật nhẹ nhàng rón rén; KHÔNG có anh MC trong cảnh này. |
| b30 | 03:18.6–03:26.5 (7.9s) | L201 | Còn ở góc bể nước của Hải Sâm, một chú cá ngọc trai Carapidae vừa chui tọt vào hậu môn của Hải Sâm để ngủ trưa rồi thò đầu ra ngoài ngáp một cái thật dài! |  | Chú cá ngọc trai thò đầu ra khỏi đuôi chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù ngáp ngủ, chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù cầm quạt giấy phẩy lia lịa mặt méo xệch; KHÔNG có anh MC trong cảnh này. |
| b31 | 03:26.5–03:33.6 (7.1s) | L202 | Chú cá này thậm chí còn rủ thêm hai người bạn cá ngọc trai khác vào cùng trú ngụ, biến cơ thể Hải Sâm thành một căn hộ chung cư mini dưới nước! |  | Ba chú cá ngọc trai nhỏ thò đầu ra vẫy đuôi trong sự ngao ngán của chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù; KHÔNG có anh MC trong cảnh này. |
| b32 | 03:33.6–03:41.6 (8.0s) | L203 | Cứu em với anh MC ơi! Tên khách trọ này ở ké cả tuần nay không trả một xu tiền phòng mà còn ngáy to quá làm em mất ngủ! |  | Cận cảnh chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù giơ quạt giấy khóc mếu máo kêu cứu; KHÔNG có anh MC trong cảnh này. |
| b33 | 03:41.6–03:48.5 (6.9s) | L204 | Và đỉnh điểm khó đỡ: anh MC vừa cầm ly nước chanh lên định uống một ngụm giải khát thì phát hiện Sứa Bất Tử đang tung tăng bơi lội bên |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng há hốc miệng dừng ly nước chanh ngay trước môi, bên trong ly chú sứa chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực nhỏ xíu đang nháy mắt cười toe toét; KHÔNG có anh MC trong cảnh này. |
| b34 | 03:48.5–03:52.5 (4.0s) | L205 | trong! May mà chưa nuốt chửng tân vương tiềm năng của Mùa ba! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng thở phào nhẹ nhõm dùng thìa vớt chú sứa cẩn thận thả lại vào bể thi đấu an toàn. |
| b35 | 03:52.5–03:59.8 (7.2s) | L206 | Dưới kính hiển vi điện tử, da của Bạch Tuộc Mimic là một màn hình chấm lượng tử sinh học với hàng triệu tế bào sắc tố chromatophore và iridophore! |  | Phóng to bề mặt da chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình: hàng triệu tế bào sắc tố co giãn nhịp nhàng như các điểm ảnh O-L-E-D siêu nét; KHÔNG có anh MC trong cảnh này. |
| b36 | 03:59.8–04:06.6 (6.9s) | L207 | Mỗi tế bào sắc tố được điều khiển bởi một sợi dây thần kinh riêng biệt, cho phép chúng thay đổi màu sắc và kết cấu bề mặt da chỉ trong 200 mili-giây! |  | Đồ họa các xung thần kinh kích hoạt tế bào sắc tố đổi từ màu cát vàng sang vân vằn rắn biển trong chớp mắt; KHÔNG có anh MC trong cảnh này. |
| b37 | 04:06.6–04:12.8 (6.1s) | L208 | Trong khi đó, Sứa Bất Tử cũng tận dụng thời gian nghỉ giữa hiệp để kích hoạt quá trình tái lập trình nơ-ron thần kinh vô cùng kỳ diệu! |  | chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực phát quang lung linh trong bể nước, các tế bào gốc phân chia và tái cấu trúc mạng lưới thần kinh non trẻ; KHÔNG có anh MC trong cảnh này. |
| b38 | 04:12.8–04:20.0 (7.3s) | L209 | Cơ thể sứa tí hon này không bao giờ biết mệt mỏi, bởi mỗi khi căng thẳng, chúng chỉ việc đảo ngược tế bào để trở lại trạng thái thanh xuân sung mãn! |  | Đồ họa đồng hồ sinh học của chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực quay ngược về vạch số 0, cơ thể trong veo không tì vết; KHÔNG có anh MC trong cảnh này. |
| b39 | 04:20.0–04:24.7 (4.7s) | L210 | Không khí phòng nghỉ ngơi của Ếch Lông Wolverine thì tràn ngập tiếng gầm gừ tập luyện cơ bắp cuồn |  | chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng hít đất bằng hai chi trước, gân cốt cơ bắp nổi rõ từng múi dưới lớp lông tơ rậm rạp; KHÔNG có anh MC trong cảnh này. |
| b40 | 04:24.7–04:31.5 (6.8s) | L211 | cuộn! Chú ếch liên tục kiểm tra khớp móng vuốt để đảm bảo các mũi xương đã thu gọn hoàn toàn vào bao gân trước khi bước vào các vòng đấu quyết định! |  | Cận cảnh bàn chân chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng: các móng xương thu gọn vào rãnh gân collagen đàn hồi an toàn; KHÔNG có anh MC trong cảnh này. |
| b41 | 04:31.5–04:37.5 (6.0s) | L212 | Giờ giải lao kết thúc trong những tiếng cười sảng khoái! Tất cả mười tuyển thủ đã sẵn sàng quay trở lại đấu trường khốc liệt! |  | Dàn đèn pha rọi sáng trở lại sàn đấu, mười tuyển thủ bước ra vị trí thi đấu trong tiếng cổ vũ náo nhiệt của khán giả; KHÔNG có anh MC trong cảnh này. |

### scene06 · CÔNG TRÌNH ĐỊA HÌNH & XÃ HỘI BẦY ĐÀN KỶ LUẬT · 276.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:06.0 (6.0s) | L213 | Chào mừng quý vị quay trở lại với Vòng bốn: Kỹ Sư Địa Hình và Những Xã Hội Động Vật Kỷ Luật Thép! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng giơ micro hướng về một sa bàn địa hình rộng lớn được dựng giữa sân vận động; tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng ô thử thách số bốn mang biểu tượng con đập và mạng lưới hang ngầm. |
| b02 | 00:06.0–00:12.3 (6.3s) | L214 | Tại vòng đấu này, chúng ta sẽ được chứng kiến cách những sinh vật hoang dã tái định hình cả cảnh quan thiên nhiên và bảo vệ giống nòi! |  | Mô hình sa bàn chiếu dòng sông uốn lượn, rừng cây nguyên sinh và lòng đất sâu nhiều tầng; KHÔNG có anh MC trong cảnh này. |
| b03 | 00:12.3–00:21.8 (9.5s) | L215 | Không phải máy xúc, xe ủi hay xi măng cốt thép của con người, chính những chiếc đuôi dẹt, móng vuốt đào hầm và tinh thần kỷ luật bầy đàn đã tạo nên những kỳ quan sinh thái vĩ đại! |  | Hình ảnh so sánh máy ủi khổng lồ gầm rú với các kỹ sư động vật nhỏ bé đang miệt mài kiến tạo thiên nhiên; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:21.8–00:27.1 (5.3s) | L216 | Không ai xứng đáng mở màn vòng đấu này hơn kỹ sư Hải Ly: kiến trúc sư thiên tài số một của thế giới tự nhiên! |  | chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo vác thước đo gỗ và xẻng nhỏ tiến vào sa bàn sông suối, ánh mắt tràn đầy nhiệt huyết công trình; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:27.1–00:36.6 (9.5s) | L217 | Khán giả thường nghĩ Hải Ly xây đập chỉ để bảo vệ hang ở của mình, nhưng một nghiên cứu 2020 trên tạp chí Ecological Applications đã chỉ ra tầm vóc vĩ đại hơn nhiều! |  | Đồ họa từ vệ tinh nhìn xuống: con đập ngăn nước tạo thành một vùng đất ngập nước xanh mướt rộng hàng chục héc-ta; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:36.6–00:43.9 (7.4s) | L218 | Khi những trận cháy rừng kinh hoàng quét qua Bắc Mỹ thiêu rụi toàn bộ thung lũng xung quanh, chính những con đập của Hải Ly đã tạo ra các ốc đảo ngập nước xanh tươi bất khả xâm |  | Bão lửa đỏ rực thiêu rụi rừng cây khô xung quanh, nhưng vùng đầm lầy của chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo vẫn xanh rì, muông thú tụ tập trú ẩn an toàn; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:43.9–00:50.7 (6.8s) | L219 | phạm! Độ ẩm cao và mực nước ngầm dồi dào từ đập Hải Ly chặn đứng hoàn toàn bước tiến của ngọn lửa hung tàn, cứu sống hàng vạn sinh mạng hoang dã! |  | Ranh giới rõ rệt: một bên tro tàn đen ngòm, một bên là ốc đảo nước trong xanh mát rượi do chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo kiến tạo; KHÔNG có anh MC trong cảnh này. |
| b08 | 00:50.7–00:57.8 (7.2s) | L220 | Hơn thế nữa, đập Hải Ly giữ lại tới 80% lượng bùn đất xói mòn và kim loại nặng, thanh lọc nguồn nước uống trong lành cho toàn bộ hạ lưu! | **80% BÙN** · Lọc sạch trầm tích · R/410 · [0.65, 0.48] | Dòng nước đục ngầu chảy qua đập gỗ lắng cặn lại, dòng nước chảy ra hạ lưu trong vắt như gương; KHÔNG có anh MC trong cảnh này. |
| b09 | 00:57.8–01:05.8 (8.0s) | L221 | Những con đập của Hải Ly có thể tồn tại qua hàng thế kỷ, thậm chí có con đập cổ xưa dài tới 800 mét tại Canada nhìn thấy rõ mồn một từ ảnh chụp vệ tinh không gian! |  | Ảnh vệ tinh không gian hiển thị con đập Hải Ly vắt ngang thung lũng dài 800m khổng lồ; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:05.8–01:12.6 (6.8s) | L222 | Một cỗ máy thanh lọc môi trường sống tự nhiên không tốn một xu tiền điện của Trái Đất! Cả khán đài cúi mình thán phục trước Hải Ly! |  | Khán giả và ban giám khảo đồng loạt vỗ tay tán thưởng; chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo mỉm cười gật đầu tự hào. |
| b11 | 01:12.6–01:19.6 (7.0s) | L223 | Tiếp theo, hãy cùng nhìn sâu xuống lòng đất nước Úc nơi Gấu Túi Wombat làm nên điều kỳ diệu trong các trận thảm họa cháy rừng! |  | Sa bàn mặt đất lật mở để lộ mạng lưới đường hầm ngầm phức tạp của chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường sâu hai mét dưới lòng đất; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:19.6–01:25.6 (6.0s) | L224 | Mỗi hệ thống hang của Wombat có thể kéo dài tới 30m với hàng chục ngách rẽ và nhiều cửa thoát hiểm được đào kiên cố! | **DÀI 30M** · Hang ngầm kiên cố · L/400 · [0.35, 0.72] | Sơ đồ kiến trúc hang ngầm dài 30m với các phòng ngủ lót cỏ khô và hệ thống thông gió tự nhiên; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:25.6–01:33.0 (7.5s) | L225 | Trong các trận hỏa hoạn lịch sử tại rừng nước Úc khi nhiệt độ mặt đất lên tới hàng 100°C, nhiệt độ dưới hang Wombat vẫn duy trì ổn định ở mức 20 độ mát mẻ! |  | Đồng hồ nhiệt độ so sánh: mặt đất nóng rực 100°C đỏ lửa, dưới hang chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường mát mẻ 20°C dịu nhẹ; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:33.0–01:41.3 (8.3s) | L226 | Camera của các nhà khoa học bảo tồn đã ghi lại những thước phim xúc động: chuột túi Wallaby, kỳ đà, chim sẻ và thú có túi cùng lũ lượt kéo nhau xuống hang Wombat để lánh nạn! |  | Các loài động vật chạy trốn ngọn lửa cùng chui xuống cửa hang của chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường, ngồi hòa bình bên cạnh chú gấu túi hiền lành; KHÔNG có anh MC trong cảnh này. |
| b15 | 01:41.3–01:48.0 (6.7s) | L227 | Wombat không hề xua đuổi hay tấn công mà hào phóng chia sẻ nơi trú ẩn an toàn, trở thành những người hùng cứu hỏa thầm lặng của đại lục Úc! |  | chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường ngồi gặm cỏ ở cửa hang, xung quanh là bạn bè muông thú được cứu sống vẫy tay cảm ơn; KHÔNG có anh MC trong cảnh này. |
| b16 | 01:48.0–01:53.5 (5.5s) | L228 | Hệ thống hang ngầm này hoạt động như một boongke chống thảm họa thiên nhiên hoàn hảo nhất mà không cần đến bê tông cốt thép! |  | Mặt cắt lòng đất: hang ngầm kiên cố chở che cho muông thú bình yên vượt qua thảm họa; KHÔNG có anh MC trong cảnh này. |
| b17 | 01:53.5–01:58.2 (4.6s) | L229 | Và cuối cùng là cấu trúc xã hội kỷ luật thép của Kiến Nổ Cảm Tử trên các tán rừng nhiệt đới Đông Nam |  | Cành cây cổ thụ với lối vào tổ kiến chỉ nhỏ bằng đầu que tăm; KHÔNG có anh MC trong cảnh này. |
| b18 | 01:58.2–02:05.2 (7.0s) | L230 | Á! Tiến sĩ Alice Laciny phát hiện: trong tổ của Kiến Nổ có một tầng lớp lính gác cửa đặc biệt sở hữu hộp sọ biến đổi phẳng lì như một chiếc nút chai! |  | Phóng to chú kiến gác cửa: đầu hình đĩa tròn phẳng lì vừa khít tuyệt đối với miệng lỗ tổ tròn xoe; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:05.2–02:11.8 (6.6s) | L231 | Chúng dùng chính chiếc đầu bọc giáp của mình làm chiếc cửa chống đạn bịt kín hoàn toàn lối vào, ngăn chặn mọi kẻ xâm lược từ bên ngoài! |  | Một con nhện độc hung dữ cắn vào cửa tổ nhưng chỉ cắn trúng bề mặt sọ phẳng cứng như đá của kiến lính gác; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:11.8–02:17.5 (5.7s) | L232 | Chiếc cửa sống này chỉ mở ra khi kiến thợ đi kiếm ăn về gõ đúng mật mã râu pheromone đặc trưng của bầy đàn! |  | Chú kiến thợ dùng hai chiếc râu chạm nhẹ vào đầu kiến gác cửa theo nhịp điệu mật mã, chiếc đầu thụt vào mở lối đi; KHÔNG có anh MC trong cảnh này. |
| b21 | 02:17.5–02:20.9 (3.5s) | L233 | Một hệ thống an ninh sinh học bảo mật tuyệt đối không thể phá khóa! |  | chú Kiến Nổ dũng cảm bảo vệ tổ hoạt hình màu đỏ cam, đeo ba lô chứa chất lỏng vàng phát sáng, đội mũ bảo hộ chống độc, ánh mắt quả cảm kiên cường đứng nghiêm trang gác cửa như một người lính bảo vệ tổ quốc quả cảm; KHÔNG có anh MC trong cảnh này. |
| b22 | 02:20.9–02:28.1 (7.1s) | L234 | Để xây dựng những con đập dài hàng trăm mét, Hải Ly còn sở hữu kỹ năng đào kênh dẫn nước kỳ tài không kém các kỹ sư thủy lợi La Mã! |  | Sa bàn rừng rậm hiện lên các con kênh đào thẳng tắp sâu một mét do chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo đào bới; KHÔNG có anh MC trong cảnh này. |
| b23 | 02:28.1–02:38.6 (10.5s) | L235 | Chúng tự đào các tuyến kênh ngập nước dài tới 200 mét đâm sâu vào các khu rừng gỗ cứng, để thả nổi các khúc gỗ nặng hàng chục ký trôi theo dòng nước về vị trí đắp đập mà không tốn sức kéo lê trên cạn! |  | Khúc gỗ to trôi nhẹ nhàng trên dòng kênh đào nhân tạo về phía con đập chính, chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo bơi theo đẩy lái chuyên nghiệp; KHÔNG có anh MC trong cảnh này. |
| b24 | 02:38.6–02:48.1 (9.5s) | L236 | Đặc biệt, thân đập của Hải Ly được thiết kế uốn cong hình cánh cung hướng ngược về phía dòng chảy, mô phỏng hoàn hảo nguyên lý chịu lực của các con đập thủy điện vòm bê tông hiện đại nhất! |  | Con đập gỗ uốn cong cánh cung cản phá sức ép khủng khiếp của dòng nước lũ mùa xuân một cách ngoạn mục; KHÔNG có anh MC trong cảnh này. |
| b25 | 02:48.1–02:58.5 (10.4s) | L237 | Hệ thống kiến trúc tự nhiên này có thể điều tiết lưu lượng nước của cả một lưu vực sông rộng lớn, biến Hải Ly thành loài động vật duy nhất có thể thay đổi địa hình Trái Đất ngang ngửa con người! |  | Hình ảnh vệ tinh so sánh công trình thành phố của con người và hệ thống đầm lầy do chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo kiến tạo hài hòa tuyệt mỹ; KHÔNG có anh MC trong cảnh này. |
| b26 | 02:58.5–03:05.7 (7.2s) | L238 | Để chuẩn bị cho mùa đông băng giá Bắc Mỹ khi mặt hồ đóng băng dày hàng mét, Hải Ly còn xây dựng những kho lương thực ngập nước ngầm vô cùng thông minh! |  | Đáy hồ nước mùa đông: lớp băng dày phủ trên mặt hồ, bên dưới chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo bơi lội trong làn nước mát; KHÔNG có anh MC trong cảnh này. |
| b27 | 03:05.7–03:10.7 (4.9s) | L239 | Chúng cắm chặt hàng trăm cành cây gỗ tươi giàu dinh dưỡng xuống lớp bùn sâu dưới đáy hồ ngay cạnh cửa hang ngầm! |  | Các cành cây tươi được cắm ngay ngắn thành từng hàng dưới đáy bùn như một kho thực phẩm đông lạnh tự nhiên; KHÔNG có anh MC trong cảnh này. |
| b28 | 03:10.7–03:18.9 (8.2s) | L240 | Khi mặt hồ đóng băng kín mít, Hải Ly chỉ việc bơi ra cửa hang ngầm, rút một cành cây tươi dưới bùn mang vào hang thưởng thức mà không cần thò đầu lên mặt băng lạnh giá! |  | chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo ngồi trong hang ấm áp gặm cành cây tươi ngon lành, bên ngoài gió tuyết gầm rú dữ dội; KHÔNG có anh MC trong cảnh này. |
| b29 | 03:18.9–03:25.7 (6.8s) | L241 | Một công trình đập của Hải Ly có thể nâng mực nước ngầm của toàn bộ lưu vực xung quanh lên cao thêm từ một đến hai mét suốt mùa khô hạn! |  | Sơ đồ địa chất cắt lớp: mực nước ngầm dưới rễ cây rừng dâng cao màu xanh ngọc bích màu mỡ; KHÔNG có anh MC trong cảnh này. |
| b30 | 03:25.7–03:33.5 (7.8s) | L242 | Nhờ nguồn nước ngầm dồi dào này, thảm thực vật ven bờ phát triển xanh tốt quanh năm, tạo nguồn thức ăn dồi dào nuôi sống các đàn hươu nai và chim muông vượt qua mùa đông khắc nghiệt! |  | Đàn hươu rừng và thỏ tuyết tìm đến mép hồ của chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo uống nước và gặm cỏ tươi tốt thanh bình; KHÔNG có anh MC trong cảnh này. |
| b31 | 03:33.5–03:38.8 (5.2s) | L243 | Hải Ly thực sự là một kỹ sư kiến tạo cảnh quan sinh thái có tầm ảnh hưởng sâu rộng bậc nhất hành tinh! |  | chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo đứng tự hào bên con đập gỗ vững chãi ngắm nhìn thung lũng xanh tươi bạt ngàn; KHÔNG có anh MC trong cảnh này. |
| b32 | 03:38.8–03:45.8 (7.0s) | L244 | Không dừng lại ở việc đắp đập, những kiến trúc sư Hải Ly tài ba còn đào những con kênh dẫn nước dài tới 500m sâu vào giữa rừng già! |  | Sa bàn đồ họa hiển thị mạng lưới kênh đào chằng chịt của chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo tỏa sâu vào rừng già như hệ thống giao thông thủy lợi hoàn hảo; KHÔNG có anh MC trong cảnh này. |
| b33 | 03:45.8–03:53.1 (7.3s) | L245 | Những con kênh này cho phép Hải Ly thả trôi những khúc gỗ nặng hàng trăm cân về tổ một cách nhẹ nhàng, giảm thiểu tối đa nguy cơ bị thú dữ mai phục trên cạn! |  | chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo đẩy khúc gỗ trôi êm ả trên dòng kênh đào mát rượi, thảnh thơi bơi về tổ ấm an toàn; KHÔNG có anh MC trong cảnh này. |
| b34 | 03:53.1–03:59.6 (6.5s) | L246 | Còn tấm khiên sụn mông của Wombat cứng đến mức những cú cắn của chó rừng Dingo hay đại bàng đuôi nhọn chỉ để lại những vết xước mờ nhạt không đáng kể! |  | Chó rừng Dingo cắn mạnh vào mông chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường nhưng bị gãy răng nhe nanh đau đớn, tấm khiên sụn không hề suy chuyển; KHÔNG có anh MC trong cảnh này. |
| b35 | 03:59.6–04:05.9 (6.3s) | L247 | Hải Ly còn sở hữu lớp lông dày tới 10.000 sợi trên một xen-ti-mét vuông da, được bôi trơn bởi lớp dầu castoreum chống thấm nước tuyệt đối! |  | Kính hiển vi phóng to lớp lông dày mượt mà của chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo: các bọt khí bị bẫy lại giữ ấm cơ thể trong làn nước băng giá; KHÔNG có anh MC trong cảnh này. |
| b36 | 04:05.9–04:11.4 (5.5s) | L248 | Nhờ đó, ngay cả khi bơi lội dưới lớp băng dày vào mùa đông Bắc Mỹ, da của Hải Ly vẫn hoàn toàn khô ráo và ấm áp! |  | chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo lặn ngụp dưới tảng băng trôi mà không hề run rẩy, cơ thể tỏa nhiệt hồng ấm áp; KHÔNG có anh MC trong cảnh này. |
| b37 | 04:11.4–04:18.2 (6.9s) | L249 | Ban giám khảo xin công bố kết quả Vòng bốn! Huy chương Đồng thuộc về Kiến Nổ Cảm Tử với cánh cửa sọ nút chai an ninh pheromone! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ búa, trao huy chương đồng phát sáng cho chú Kiến Nổ dũng cảm bảo vệ tổ hoạt hình màu đỏ cam, đeo ba lô chứa chất lỏng vàng phát sáng, đội mũ bảo hộ chống độc, ánh mắt quả cảm kiên cường. |
| b38 | 04:18.2–04:23.6 (5.4s) | L250 | Huy chương Bạc thuộc về Gấu Túi Wombat với mạng lưới hang ngầm cứu trợ muông thú trong thảm họa! |  | chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường vui vẻ đón nhận tấm huy chương bạc lấp lánh thứ hai của mình. |
| b39 | 04:23.6–04:29.9 (6.3s) | L251 | Và Huy chương Vàng ba điểm xứng đáng thuộc về kỹ sư Hải Ly với công trình đập nước chống hạn hán và đẩy lùi bão lửa! |  | chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo đứng trên bục số một giơ cao huy chương vàng, khán đài tung hoa giấy rực rỡ chúc mừng. |
| b40 | 04:29.9–04:36.9 (7.0s) | L252 | Bảng điểm sau bốn vòng đấu tiếp tục có biến động lớn: Wombat vươn lên dẫn đầu với năm điểm! Hải Ly bứt phá mạnh mẽ lên bốn điểm! |  | tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) cập nhật điểm số: Wombat 5 điểm, Hải Ly 4 điểm, Sứa Bất Tử 3 điểm, Chuột Chũi Sao 3 điểm, Hagfish 2 điểm, Axolotl 2 điểm, Bạch Tuộc Mimic 2 điểm, Ếch dị nhân móng vuốt hoạt hình đáng yêu 1 điểm, Kiến Nổ 1 điểm; cuộc rượt đuổi điểm số vô cùng nghẹt thở! |

### scene07 · KHÁNG THỂ SIÊU CẤP & BỘ GEN BẤT TỬ ĐỘT BIẾN · 267.6s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.1 (7.1s) | L253 | Tiến vào chặng đua thứ năm! Chào mừng quý vị đến với Vòng năm: Kháng Thể Siêu Cấp và Những Bộ Gen Đột Biến Kỳ Vĩ! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng bước lên bục chỉ tay vào màn hình hiển thị đồ họa chuỗi xoắn kép DNA ba chiều rực rỡ; tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng ô thử thách số năm mang biểu tượng phân tử gen. |
| b02 | 00:07.1–00:13.3 (6.2s) | L254 | Ở vòng đấu này, cuộc cạnh tranh không còn diễn ra ở tầm cơ bắp hay móng vuốt, mà đi sâu vào tận cấp độ phân tử và tế bào vi mô! |  | Mô hình kính hiển vi điện tử chiếu rọi vào nhân tế bào phát sáng lung linh; KHÔNG có anh MC trong cảnh này. |
| b03 | 00:13.3–00:21.4 (8.0s) | L255 | Những bí mật di truyền được mã hóa qua hàng tỷ cặp base nitơ chính là tấm bản đồ thần kỳ giúp các dị nhân vượt qua những nghịch lý sinh tồn khắc nghiệt nhất! |  | Các chuỗi mã hóa di truyền ACGT chạy rực rỡ như dòng thác ma trận số học sinh học; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:21.4–00:25.8 (4.4s) | L256 | Tuyển thủ đầu tiên bước lên bục phân tích di truyền: Kỳ Nhông Axolotl của hồ Xochimilco! |  | chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói bơi đến trước màn hình chiếu bộ gen, nụ cười rạng rỡ và sáu mang lông vũ đỏ đung đưa uyển chuyển; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:25.8–00:31.8 (6.0s) | L257 | Một công trình nghiên cứu quy mô toàn cầu đăng tải trên tạp chí Nature 2018 đã giải mã thành công toàn bộ hệ gen của Axolotl! |  | Hình ảnh chuỗi DNA khổng lồ kéo dài vô tận qua hàng trăm trang màn hình dữ liệu; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:31.8–00:40.2 (8.4s) | L258 | Kết quả khiến giới khoa học sững sờ: bộ gen của chú kỳ nhông này dài tới 32 tỷ cặp base nitơ, tức là gấp 10 lần toàn bộ hệ gen của một con người trưởng thành! | **32 TỶ BASE** · Gấp 10 lần gen người · R/410 · [0.65, 0.48] | Đồ họa so sánh hai chuỗi DNA: chuỗi gen người 3,2 tỷ base ngắn bằng một gang tay, chuỗi gen của chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói dài 32 tỷ base cuộn thành nhiều vòng khổng lồ; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:40.2–00:50.1 (9.9s) | L259 | Ẩn sâu trong 32 tỷ cặp base này là những đoạn gen kiểm soát phân bào độc nhất vô nhị: các tế bào mọc lại chi phân chia với tốc độ tên lửa nhưng tuyệt đối không bao giờ phát triển thành khối u ác tính! |  | Các tế bào phân chia nhanh chóng nhưng xếp hàng ngay ngắn trật tự dưới sự kiểm soát của gen ức chế ung thư; KHÔNG có anh MC trong cảnh này. |
| b08 | 00:50.1–00:56.2 (6.1s) | L260 | Axolotl sở hữu khả năng kháng ung thư tự nhiên gần như tuyệt đối, trở thành hình mẫu vàng cho các nhà nghiên cứu y học di truyền thế giới! |  | Chú kỳ nhông chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói khoác áo choàng bác sĩ nhỏ, cầm ống nghiệm tỏa sáng lấp lánh; KHÔNG có anh MC trong cảnh này. |
| b09 | 00:56.2–01:06.2 (10.0s) | L261 | Cơ chế kiểm soát chu kỳ tế bào nghiêm ngặt đến mức ngay cả khi các nhà khoa học cố tình tiêm các hoạt chất gây ung thư cực mạnh, cơ thể Axolotl vẫn tự động đào thải và tái tạo lại mô tế bào khỏe mạnh bình thường! |  | Khối u thí nghiệm vừa manh nha lập tức bị các đại thực bào và enzym của chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói tiêu diệt sạch sẽ; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:06.2–01:13.5 (7.3s) | L262 | Mười điểm cho sự kỳ diệu của bộ gen Axolotl! Nhưng ngay lập tức, Sứa Bất Tử bay lơ lửng bước vào vòng đo lường gen telomere! |  | chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực trôi dạt vào buồng soi gen, vương miện nhỏ xíu lấp lánh ánh hào quang hồng tím; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:13.5–01:22.0 (8.5s) | L263 | 2022, một nhóm nghiên cứu tại đại học Oviedo Tây Ban Nha đã công bố bản giải mã di truyền của Sứa Bất Tử trên kỷ yếu Viện Hàn lâm Khoa học Quốc gia Hoa Kỳ! |  | Bìa bài báo PNAS 2022 hiện lên với biểu đồ so sánh giữa Sứa Bất Tử và các loài sứa thông thường; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:22.0–01:29.6 (7.6s) | L264 | Họ phát hiện Sứa Bất Tử sở hữu số lượng gen nhân đôi gấp đôi ở các cụm gen chịu trách nhiệm bảo vệ và duy trì độ dài của telomere: chiếc nắp bảo vệ ở đầu mút nhiễm sắc thể! |  | Cận cảnh đầu mút nhiễm sắc thể: nắp telomere của sinh vật thường ngắn dần theo tuổi tác, còn của chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực liên tục được đắp dài thêm nguyên vẹn; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:29.6–01:38.9 (9.3s) | L265 | Mỗi khi cơ thể bị lão hóa, hệ enzym telomerase và cơ chế sửa chữa lỗi sao chép DNA tự động kích hoạt ở mức tối đa, xóa sạch mọi dấu vết già nua và tái thiết lập đồng hồ sinh học về số không! |  | Chiếc đồng hồ sinh học quay ngược kim thời gian về vạch xuất phát, chuỗi DNA sáng bóng như mới xuất xưởng; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:38.9–01:41.3 (2.5s) | L266 | Một bộ gen bất tử thực thụ theo đúng nghĩa đen di truyền học! |  | chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực xoay tròn giữa các phân tử DNA phát sáng lung linh; KHÔNG có anh MC trong cảnh này. |
| b15 | 01:41.3–01:49.2 (7.9s) | L267 | Chúng không chỉ sửa chữa DNA bị đứt gãy mà còn sao chép dự phòng hàng trăm bản sao gen chống stress oxy hóa, giúp tế bào luôn duy trì trạng thái thanh xuân vĩnh cửu! |  | Mô hình tế bào chuông sứa trẻ hóa phát sáng như những viên ngọc bích lung linh dưới đáy biển; KHÔNG có anh MC trong cảnh này. |
| b16 | 01:49.2–01:53.5 (4.3s) | L268 | Và không thể bỏ qua Ếch Lông Wolverine với lá chắn kháng sinh sinh học trên da suối |  | chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng ngồi trong dòng nước đục ngầu chứa đầy vi khuẩn và nấm mốc; KHÔNG có anh MC trong cảnh này. |
| b17 | 01:53.5–02:00.3 (6.8s) | L269 | xiết! Sau khi tự bẻ xương đâm rách toạc da chân để nghênh chiến, làm thế nào chú ếch này không bị nhiễm trùng huyết trong môi trường bùn lầy dơ bẩn? |  | Vết thương hở trên ngón chân tiếp xúc với dòng nước bùn đầy vi khuẩn hoạt hình hung dữ; KHÔNG có anh MC trong cảnh này. |
| b18 | 02:00.3–02:09.5 (9.2s) | L270 | Các tuyến da của ếch đực tiết ra hàng loạt chuỗi peptide kháng khuẩn phổ rộng có khả năng tiêu diệt lập tức các loại nấm sát thủ và vi khuẩn gây hoại tử chỉ trong vài phút tiếp xúc! |  | Lớp gel kháng khuẩn từ da tiết ra tạo thành màng bảo vệ vô hình, các vi khuẩn chạm vào liền tan rã biến mất; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:09.5–02:13.7 (4.2s) | L271 | Nhờ vậy, vết rách tự lành thần tốc mà không cần đến một viên thuốc kháng sinh nào! |  | chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng nhấc bàn chân lành lặn lên khoe trước ống kính với nụ cười tự tin; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:13.7–02:21.5 (7.9s) | L272 | Bên cạnh bộ gen khổng lồ của Axolotl và Sứa, Bạch Tuộc Mimic cũng khiến các nhà di truyền học kinh ngạc với cơ chế chỉnh sửa ARN độc nhất vô nhị! |  | Mô hình chuỗi thông tin di truyền ARN thông tin phát sáng lung linh bên trong nhân tế bào thần kinh bạch tuộc; KHÔNG có anh MC trong cảnh này. |
| b21 | 02:21.5–02:33.1 (11.5s) | L273 | Nghiên cứu công bố trên tạp chí Science năm 2017 của nhóm tiến sĩ Eli Eisenberg phát hiện: loài bạch tuộc này không cần thay đổi chuỗi D-N-A gốc mà trực tiếp biên tập lại các phân tử ARN thông tin! |  | Các enzym biên tập hoạt hình cắt dán và thay thế các mã base trên chuỗi ARN một cách linh hoạt; KHÔNG có anh MC trong cảnh này. |
| b22 | 02:33.1–02:39.6 (6.6s) | L274 | Hơn 60 phần trăm các bản phiên mã thần kinh của chúng được tái cấu trúc linh hoạt theo nhiệt độ nước và nồng độ oxy của môi trường! |  | Khi nước biển lạnh đi hoặc ấm lên, các kênh ion thần kinh tự động thích nghi tối ưu mà không cần chờ đợi hàng ngàn năm tiến hóa gen; KHÔNG có anh MC trong cảnh này. |
| b23 | 02:39.6–02:46.2 (6.6s) | L275 | Một khả năng lập trình phần mềm sinh học theo thời gian thực vượt xa mọi hệ điều hành máy tính tinh vi nhất của nhân loại! |  | Hình ảnh chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình phát sáng các vi mạch sinh học tự động cập nhật phần mềm thích nghi đại dương; KHÔNG có anh MC trong cảnh này. |
| b24 | 02:46.2–02:55.2 (9.0s) | L276 | Và điều kỳ lạ nhất trong bộ gen của Cá Mút Đá Hagfish vừa được các nhà di truyền học đại học Tokyo làm sáng tỏ: hiện tượng đào thải D-N-A có lập trình trong tế bào soma! |  | Sơ đồ nhân tế bào của Hagfish: các đoạn nhiễm sắc thể tự động phân cắt và đào thải một cách có trật tự; KHÔNG có anh MC trong cảnh này. |
| b25 | 02:55.2–03:02.8 (7.5s) | L277 | Khi Hagfish phát triển từ phôi thai thành cá thể trưởng thành, các tế bào cơ thể của chúng tự động loại bỏ tới 20% lượng D-N-A không cần thiết trong nhân tế bào! |  | Chiếc kéo sinh học hoạt hình cắt tỉa các đoạn gen thừa thãi vứt bỏ ra ngoài, giúp bộ gen cơ thể gọn nhẹ tối đa; KHÔNG có anh MC trong cảnh này. |
| b26 | 03:02.8–03:11.7 (8.9s) | L278 | Chúng chỉ giữ lại trọn vẹn toàn bộ bộ gen gốc trong các tế bào sinh dục mầm, giúp cơ thể tiết kiệm tối đa năng lượng sao chép và duy trì sự sống bền bỉ suốt hàng trăm triệu năm! |  | Tế bào sinh dục phát sáng trọn vẹn, còn tế bào cơ thể chạy ở phiên bản tinh giản siêu tiết kiệm năng lượng; KHÔNG có anh MC trong cảnh này. |
| b27 | 03:11.7–03:20.5 (8.8s) | L279 | Trong khi đó, hệ enzym sửa chữa D-N-A của Sứa Bất Tử hoạt động với độ chính xác tuyệt đối, loại bỏ tới 99,9% phần trăm các đột biến sai hỏng trong quá trình sao chép! |  | Robot phân tử enzym kiểm tra chuỗi DNA phát hiện lỗi và dán bản vá hoàn hảo; KHÔNG có anh MC trong cảnh này. |
| b28 | 03:20.5–03:27.6 (7.1s) | L280 | Nhờ khả năng tự sửa lỗi di truyền liên tục này, Sứa Bất Tử không bao giờ tích lũy các đột biến gây thoái hóa hay lão hóa sớm như các sinh vật bậc cao khác! |  | Chuỗi xoắn kép DNA của chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực luôn sáng bóng và thẳng tắp như vừa mới được tạo tác; KHÔNG có anh MC trong cảnh này. |
| b29 | 03:27.6–03:33.7 (6.0s) | L281 | Một bí mật sinh học phi thường mà các nhà khoa học đang nỗ lực giải mã để áp dụng vào công nghệ kéo dài tuổi xuân cho con người! |  | Nhà khoa học mỉm cười nâng niu chuỗi DNA mô phỏng của sứa dưới ánh đèn phòng thí nghiệm; KHÔNG có anh MC trong cảnh này. |
| b30 | 03:33.7–03:41.4 (7.7s) | L282 | Bí mật đằng sau khả năng chữa lành không để lại sẹo của Axolotl nằm ở các cụm tế bào gốc blastema: chúng có thể biến đổi thành bất kỳ loại mô tế bào nào của cơ thể! |  | Kính hiển vi soi các tế bào gốc blastema của chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói phân chia tạo thành cơ xương, mạch nước màu và dây thần kinh hoàn hảo; KHÔNG có anh MC trong cảnh này. |
| b31 | 03:41.4–03:48.6 (7.3s) | L283 | Khi bị tổn thương, các đại thực bào của Axolotl dập tắt phản ứng viêm trong vài giờ, ngăn chặn triệt để sự hình thành mô xơ sẹo thường thấy ở động vật có vú! |  | Đồ họa đại thực bào quét sạch tế bào chết và kích hoạt tái sinh mô nguyên bản không tì vết; KHÔNG có anh MC trong cảnh này. |
| b32 | 03:48.6–03:56.5 (7.9s) | L284 | Còn enzyme telomerase của Sứa Bất Tử liên tục nối dài các đầu mút nhiễm sắc thể, giúp tế bào phân chia vĩnh viễn mà không bao giờ chạm tới giới hạn lão hóa Hayflick! |  | Chuỗi xoắn kép D-N-A của chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực được enzyme telomerase gắn thêm các đoạn mũ bảo vệ phát sáng rực rỡ; KHÔNG có anh MC trong cảnh này. |
| b33 | 03:56.5–04:04.2 (7.8s) | L285 | Ban giám khảo xin công bố bảng điểm Vòng năm! Huy chương Đồng thuộc về Ếch Lông Wolverine với lớp peptide kháng khuẩn tự chữa lành vết thương hở! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ búa, trao huy chương đồng phát sáng cho chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng. |
| b34 | 04:04.2–04:09.4 (5.1s) | L286 | Huy chương Bạc thuộc về Sứa Bất Tử với bộ gen bảo vệ telomere và xóa bỏ lão hóa tế bào! |  | chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực đón nhận thêm tấm huy chương bạc lấp lánh thứ hai. |
| b35 | 04:09.4–04:17.2 (7.8s) | L287 | Và Huy chương Vàng ba điểm xứng đáng thuộc về Kỳ Nhông Axolotl với bộ gen 32 tỷ cặp base kháng ung thư và tái sinh mô thần kỳ! |  | chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói đội vòng nguyệt quế nhận huy chương vàng rực rỡ trong tiếng pháo hoa nổ vang. |
| b36 | 04:17.2–04:27.6 (10.4s) | L288 | Bảng tổng sắp sau năm vòng thi đấu tiếp tục bùng nổ dữ dội: Sứa Bất Tử và Axolotl cùng vươn lên chia sẻ vị trí dẫn đầu với năm điểm! Gấu Wombat cũng đồng hạng năm điểm! Hải Ly bám sát với bốn điểm! |  | tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) cập nhật điểm số: Wombat 5 điểm, Sứa Bất Tử 5 điểm, Axolotl 5 điểm, Hải Ly 4 điểm, Chuột Chũi Sao 3 điểm, Hagfish 2 điểm, Bạch Tuộc Mimic 2 điểm, Ếch dị nhân móng vuốt hoạt hình đáng yêu 2 điểm, Kiến Nổ 1 điểm; cuộc tranh đua ngôi vương tam mã nghẹt thở! |

### scene08 · NGƯỜI HÙNG BẢO VỆ SINH THÁI ĐẠI DƯƠNG & RỪNG XANH · 251.3s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:04.9 (4.9s) | L289 | Tiến vào Vòng thi đấu thứ sáu: Người Hùng Bảo Vệ Hệ Sinh Thái Đại Dương và Rừng Xanh! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vung micro kích hoạt sa bàn mô phỏng hệ sinh thái rạn san hô và đầm lầy rực rỡ sắc màu; tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng ô thử thách số sáu mang biểu tượng giọt nước và mầm cây xanh. |
| b02 | 00:04.9–00:12.6 (7.7s) | L290 | Ở vòng thi này, chúng ta không nhìn vào sức mạnh cá nhân, mà đo lường đóng góp sinh thái vĩ đại mà các tuyển thủ âm thầm cống hiến cho hành tinh xanh! |  | Mô hình Trái Đất quay tròn, các luồng oxy và khoáng chất tuần hoàn lấp lánh; KHÔNG có anh MC trong cảnh này. |
| b03 | 00:12.6–00:20.6 (7.9s) | L291 | Mỗi sinh vật dù nhỏ bé hay mang vẻ ngoài kỳ dị đều nắm giữ một mắt xích sống còn, duy trì sự cân bằng mong manh của toàn bộ mạng lưới sự sống! |  | Hình ảnh mạng nhện sinh thái khổng lồ kết nối hàng triệu loài sinh vật, các điểm nút phát sáng; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:20.6–00:26.2 (5.7s) | L292 | Tuyển thủ bước lên sàn đầu tiên khiến tất cả bất ngờ: chú Hải Sâm lầy lội từng bị coi là kẻ lười biếng nhất đáy |  | chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù trườn ra giữa sa bàn rạn san hô ngập tràn sắc màu cá bơi lượn; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:26.2–00:34.4 (8.2s) | L293 | biển! Các nhà hải dương học tại đại học New South Wales đã công bố một báo cáo gây chấn động: Hải Sâm chính là chiếc máy hút bụi sinh học quan trọng bậc nhất của các rạn san hô nhiệt đới! |  | chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù dùng các xúc tu quanh miệng quét sạch từng lớp cát bẩn dưới đáy biển nuốt vào bụng; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:34.4–00:40.6 (6.2s) | L294 | Mỗi năm, quần thể hải sâm trên 1 km² vuông đáy biển tiêu hóa và thanh lọc tới 130 tấn cát và trầm tích hữu cơ thối rữa! | **130 TẤN** · Hút bụi rạn san hô · R/410 · [0.65, 0.48] | Mô hình đồ họa 130 tấn cát bẩn đi qua đường ruột của Hải Sâm được phân giải sạch sẽ vi khuẩn có hại; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:40.6–00:46.2 (5.6s) | L295 | Quan trọng hơn thế, chất thải sau khi tiêu hóa của Hải Sâm chứa hàm lượng Canxi Cacbonat kiềm tính cực |  | Các tinh thể Canxi Cacbonat màu trắng sáng phát quang tỏa ra từ chất thải nuôi dưỡng các nhánh san hô lớn nhanh; KHÔNG có anh MC trong cảnh này. |
| b08 | 00:46.2–00:54.3 (8.0s) | L296 | cao! Dòng chất kiềm tự nhiên này làm tăng độ pH của nước biển xung quanh, giúp trung hòa hiện tượng axit hóa đại dương do biến đổi khí hậu và bảo vệ san hô khỏi nguy cơ bị tẩy trắng hủy |  | Môi trường nước axit bị trung hòa trở lại màu xanh ngọc bích trong lành, rạn san hô phát triển rực rỡ; KHÔNG có anh MC trong cảnh này. |
| b09 | 00:54.3–01:02.1 (7.8s) | L297 | diệt! Các nhà khoa học tính toán: nếu loại bỏ hoàn toàn Hải Sâm khỏi một rạn san hô, tốc độ suy thoái của san hô sẽ tăng vọt gấp 3 lần chỉ sau vài năm ngắn ngủi! |  | Hình ảnh rạn san hô không có chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù bị phủ đầy bùn đen và rêu tảo độc hại chết dần mòn; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:02.1–01:11.2 (9.1s) | L298 | Không có Hải Sâm hút bụi và cân bằng độ pH, các rạn san hô lộng lẫy của hành tinh sẽ dần chết mòn thành bãi tha ma đá vôi! Cả khán đài nghiêng mình thán phục trước Hải Sâm! |  | Khán đài đồng loạt đứng dậy vỗ tay vang dội; chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù mỉm cười sung sướng phẩy quạt giấy tít mù; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:11.2–01:16.8 (5.6s) | L299 | Tiếp theo, hãy cùng nhìn lên các con đập của Hải Ly: chiếc bẫy lưu giữ carbon tự nhiên khổng lồ của lục địa! |  | Sa bàn rừng ôn đới Bắc Mỹ hiện lên với hệ thống đầm lầy ngập nước của chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:16.8–01:25.3 (8.5s) | L300 | Các nhà sinh thái học phát hiện: lớp trầm tích giàu hữu cơ đọng lại phía sau những con đập của Hải Ly lưu giữ hàng triệu tấn carbon hữu cơ, ngăn không cho chúng thoát vào khí quyển! |  | Đồ họa mũi tên khí nhà kính bị giữ chặt dưới lớp bùn sâu mát lạnh của đáy hồ nước chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:25.3–01:33.9 (8.7s) | L301 | Nhờ có vùng ngập nước của Hải Ly, độ đa dạng sinh học của các loài chim di cư, cá nước ngọt và động vật lưỡng cư tăng vọt tới 33% so với các dòng suối thông thường! | **33% TĂNG** · Làm giàu sinh thái · L/400 · [0.35, 0.72] | Đàn vịt trời, cá hồi và ếch nhái bơi lội rộn ràng xung quanh hang của chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:33.9–01:38.7 (4.8s) | L302 | Hải Ly không chỉ xây nhà cho mình, chúng xây dựng cả một thiên đường sinh thái nuôi dưỡng muôn loài! |  | chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo vẫy chiếc đuôi dẹt chào các bạn động vật thân thiện; KHÔNG có anh MC trong cảnh này. |
| b15 | 01:38.7–01:46.1 (7.4s) | L303 | Những vùng đất ngập nước này duy trì dòng chảy mát mẻ vào mùa hè và ngăn lũ quét vào mùa mưa bão, trở thành tấm khiên phòng hộ tự nhiên vô giá của lục địa Bắc Mỹ! |  | Mô hình dòng nước lũ cuồn cuộn đổ về bị con đập chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo hãm chậm lại, dòng nước chảy ra hạ lưu hiền hòa êm ả; KHÔNG có anh MC trong cảnh này. |
| b16 | 01:46.1–01:50.7 (4.6s) | L304 | Và cuối cùng là đóng góp âm thầm của cụ tổ Cá Mút Đá Hagfish dưới đáy vực sâu 1.000m lạnh |  | Đáy đại dương tăm tối nơi một xác cá voi khổng lồ chìm xuống đáy biển (whale fall); KHÔNG có anh MC trong cảnh này. |
| b17 | 01:50.7–01:59.6 (8.9s) | L305 | giá! Khi xác cá voi chìm xuống vùng biển sâu không có ánh sáng, hàng 1.000 con Hagfish sẽ vùi mình vào xác thịt, hấp thụ chất dinh dưỡng trực tiếp qua da và tiêu hóa sạch sẽ các mô mỡ thối |  | Đàn chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện quấn quanh xác cá voi dọn dẹp sạch sẽ trong làn nước sâu thẳm; KHÔNG có anh MC trong cảnh này. |
| b18 | 01:59.6–02:07.3 (7.7s) | L306 | rữa! Họ phân giải và hoàn trả nguồn nitơ và phốt-pho quý giá trở lại chuỗi thức ăn đáy biển, nuôi sống cả một quần xã sinh vật biển sâu tăm tối suốt hàng chục năm |  | Các dưỡng chất tỏa sáng phân tán nuôi sống tôm cua biển sâu và vi khuẩn hóa dưỡng; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:07.3–02:14.7 (7.4s) | L307 | ròng! Nếu không có đội dọn dẹp Hagfish, đáy biển sâu sẽ bị ngạt thở bởi lớp chất béo tích tụ, cắt đứt chu trình tuần hoàn dinh dưỡng toàn cầu! |  | Đồ họa dòng hải lưu mang chất dinh dưỡng từ đáy sâu dâng lên bề mặt nuôi sống các tầng sinh vật phù du; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:14.7–02:21.8 (7.1s) | L308 | Không chỉ có Hải Sâm và Hải Ly, Gấu Túi Wombat và Ếch Wolverine cũng đóng góp những mắt xích sinh thái vô giá cho lục địa của mình! |  | Sa bàn rừng cây Tây Phi và thảo nguyên cằn cỗi nước Úc hiện lên rực rỡ; KHÔNG có anh MC trong cảnh này. |
| b21 | 02:21.8–02:28.2 (6.4s) | L309 | Những viên phân hình lập phương của Wombat chứa đầy các hạt giống cỏ bản địa và hàng tỷ bào tử nấm rễ cộng sinh mycorrhiza! |  | Cận cảnh viên phân lập phương vùi trong đất: hạt giống cỏ xanh nảy mầm tươi tốt nhờ nguồn dinh dưỡng hữu cơ màu mỡ; KHÔNG có anh MC trong cảnh này. |
| b22 | 02:28.2–02:34.9 (6.7s) | L310 | Khi phân rã, chúng làm tơi xốp các tầng đất cằn cỗi và giữ nước ngầm cho thảo nguyên khô hạn nước Úc sau các đợt hạn hán kéo dài! |  | Thảo nguyên khô cằn mọc lên những mảng cỏ xanh tươi mơn mởn xung quanh các tổ hang Wombat; KHÔNG có anh MC trong cảnh này. |
| b23 | 02:34.9–02:42.8 (7.9s) | L311 | Còn Ếch Lông Wolverine là loài săn mồi đầu bảng kiểm soát mật độ ấu trùng muỗi vằn và ruồi đen truyền bệnh dịch ở các dòng suối nhiệt đới Tây Phi! |  | chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng đớp gọn đàn muỗi vằn truyền bệnh, bảo vệ sức khỏe cho các cộng đồng dân cư ven rừng nguyên sinh; KHÔNG có anh MC trong cảnh này. |
| b24 | 02:42.8–02:49.2 (6.4s) | L312 | Ở trên các tầng tán rừng nhiệt đới, Kiến Nổ Cảm Tử cũng đóng vai trò là những vệ sĩ sinh thái bảo vệ sức khỏe cho các cây cổ thụ nguyên sinh! |  | Cành cây rừng nhiệt đới xum xuê lá xanh mướt, đàn chú Kiến Nổ dũng cảm bảo vệ tổ hoạt hình màu đỏ cam, đeo ba lô chứa chất lỏng vàng phát sáng, đội mũ bảo hộ chống độc, ánh mắt quả cảm kiên cường diễu hành tuần tra trật tự; KHÔNG có anh MC trong cảnh này. |
| b25 | 02:49.2–02:56.8 (7.5s) | L313 | Chúng tiêu diệt sạch sẽ các loài sâu róm phá hoại lá non và ngăn chặn các loài rệp sáp hút nhựa cây xâm lấn, duy trì sự xanh tốt cho tán rừng nhiệt đới đại ngàn! |  | Đàn kiến phối hợp xua đuổi các loài sâu bọ gây hại khỏi cành lá, giúp cây cổ thụ phát triển khỏe mạnh; KHÔNG có anh MC trong cảnh này. |
| b26 | 02:56.8–03:03.7 (7.0s) | L314 | Sự hy sinh của từng cá thể kiến thợ không chỉ bảo vệ tổ ấm, mà gián tiếp gìn giữ lá phổi xanh khổng lồ cho toàn bộ hệ sinh thái rừng mưa xích đạo! |  | Toàn cảnh tán rừng nhiệt đới xanh bạt ngàn dưới ánh nắng ban mai rực rỡ; KHÔNG có anh MC trong cảnh này. |
| b27 | 03:03.7–03:13.1 (9.4s) | L315 | Các nhà khoa học ước tính: lượng Canxi Cacbonat kiềm tính mà quần thể Hải Sâm bài tiết ra ngoài có thể bù đắp lại tới 20% lượng vôi hóa bị mất đi của rạn san hô do biến đổi khí hậu! |  | Các phân tử Canxi Cacbonat lấp lánh kết tinh hàn gắn lại các nhánh san hô bị gãy vụn; KHÔNG có anh MC trong cảnh này. |
| b28 | 03:13.1–03:19.6 (6.5s) | L316 | Chúng hoạt động như những người thợ hồ cần mẫn trát từng lớp vữa kiềm bảo vệ pháo đài san hô trước sự bào mòn của dòng nước biển axit hóa! |  | chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù trườn qua các khối san hô để lại những vệt kiềm trắng sáng nuôi dưỡng rạn san hô xanh tốt; KHÔNG có anh MC trong cảnh này. |
| b29 | 03:19.6–03:26.9 (7.3s) | L317 | Trong các trận đại hỏa hoạn cháy rừng lịch sử tại nước Úc, hệ thống hầm ngầm của Wombat đã trở thành pháo đài cứu mạng cho hàng ngàn sinh vật bé nhỏ! |  | Đồ họa mặt cắt lòng đất: ngọn lửa cháy dữ dội trên mặt đất nhưng dưới đường hầm của chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường, nhiệt độ mát mẻ an toàn; KHÔNG có anh MC trong cảnh này. |
| b30 | 03:26.9–03:35.6 (8.8s) | L318 | Chim chóc, thú có túi nhỏ, thằn lằn và ếch nhái đều chạy vào nương náu trong các ngóc ngách hầm Wombat mát mẻ với nhiệt độ luôn duy trì ổn định 20°C! |  | Các loài thú nhỏ nép mình trong ngách hầm của chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường, bình yên thoát khỏi biển lửa thiêu rụi trên mặt đất; KHÔNG có anh MC trong cảnh này. |
| b31 | 03:35.6–03:43.8 (8.1s) | L319 | Wombat không hề xua đuổi những kẻ tị nạn bất đắc dĩ, chúng hào hiệp chia sẻ lãnh thổ ngầm, trở thành người hùng cứu sinh thầm lặng của châu Úc hoang dã! |  | chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường gật đầu thân thiện chia sẻ đường hầm cho các bạn nhỏ tị nạn, ánh mắt ấm áp tình đồng loại; KHÔNG có anh MC trong cảnh này. |
| b32 | 03:43.8–03:50.5 (6.8s) | L320 | Ban giám khảo xin tuyên bố kết quả Vòng sáu! Huy chương Đồng thuộc về Cá Mút Đá Hagfish với vai trò dọn sạch xác cá đáy vực |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ búa, trao huy chương đồng phát sáng cho chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện. |
| b33 | 03:50.5–03:55.9 (5.3s) | L321 | sâu! Huy chương Bạc thuộc về kỹ sư Hải Ly với bẫy carbon và chiếc nôi nâng đỡ đa dạng sinh thái! |  | chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo vui mừng đón nhận tấm huy chương bạc lấp lánh thứ hai. |
| b34 | 03:55.9–04:01.5 (5.6s) | L322 | Và Huy chương Vàng ba điểm vô cùng xứng đáng thuộc về chiếc máy hút bụi bảo vệ rạn san hô: Hải Sâm! |  | chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù xúc động đeo chiếc huy chương vàng đầu tiên của mình, cả đấu trường reo hò chúc mừng nồng nhiệt. |
| b35 | 04:01.5–04:11.3 (9.8s) | L323 | Bảng điểm sau sáu vòng đấu cực kỳ gay cấn và biến ảo: Hải Ly vươn lên đồng hạng sáu điểm cùng Wombat! Sứa Bất Tử và Axolotl bám sát với năm điểm! Hải Sâm bứt phá ngoạn mục lên ba điểm! |  | tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) cập nhật: Hải Ly 6 điểm, Wombat 5 điểm, Sứa Bất Tử 5 điểm, Axolotl 5 điểm, Chuột Chũi Sao 3 điểm, Hải Sâm 3 điểm, Hagfish 3 điểm, Bạch Tuộc Mimic 2 điểm, Ếch dị nhân móng vuốt hoạt hình đáng yêu 2 điểm, Kiến Nổ 1 điểm; bảng tổng sắp sít sao chưa từng thấy! |

### scene09 · CÁC CỤ TỔ CỔ ĐẠI 300 TRIỆU NĂM & TỔ TIÊN KHỔNG LỒ · 239.8s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.5 (9.5s) | L324 | Trước khi bước vào hai vòng đấu cuối cùng, ban tổ chức xin trân trọng giới thiệu: Lễ Trao Giải Phụ Đặc Biệt — Tri Ân Các Cụ Tổ Cổ Đại và Tổ Tiên Khổng Lồ! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng bước lên thảm đỏ nhung, hai bên là các tượng đài đá hóa thạch cổ đại sừng sững; tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) hiện chữ giải thưởng danh dự hoạt hình. |
| b02 | 00:09.5–00:18.0 (8.6s) | L325 | Để có mặt trên sàn đấu Mùa 3 ngày hôm nay, mười dòng giống dị nhân đã phải trải qua hàng trăm triệu năm đấu tranh sinh tồn trước thiên thạch và các kỷ băng hà khốc liệt! |  | Màn hình chiếu cảnh Trái Đất kỷ Than Đá và kỷ Băng Hà với các quái thú cổ đại khổng lồ; KHÔNG có anh MC trong cảnh này. |
| b03 | 00:18.0–00:26.4 (8.3s) | L326 | Những mẫu hóa thạch khai quật từ các tầng địa chất sâu thẳm đã chứng minh: các dị nhân của chúng ta từng sở hữu những phiên bản tổ tiên hoành tráng đến mức khó tin! |  | Nhà cổ sinh vật học hoạt hình cầm búa địa chất gõ vào vách đá lộ ra các bộ xương hóa thạch phát sáng; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:26.4–00:30.2 (3.9s) | L327 | Tấm cúp danh dự đầu tiên thuộc về cụ tổ không xương sống: Cá |  | chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện bơi lên bục danh dự, bên cạnh là một phiến đá hóa thạch ba trăm triệu năm tuổi; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:30.2–00:37.1 (6.9s) | L328 | Mút Đá Hagfish! 2019, các nhà cổ sinh vật học tại Canada đã phát hiện hóa thạch của loài Tethymyxine có niên đại 300 triệu năm từ kỷ Than Đá! | **300 TR NĂM** · Cổ vật sống cổ đại · R/410 · [0.65, 0.48] | Cận cảnh phiến đá hóa thạch Tethymyxine ba trăm triệu năm tuổi hiện rõ từng đường nét thân trơn và tuyến chất nhầy; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:37.1–00:42.8 (5.7s) | L329 | Điều kinh ngạc là cấu trúc cơ thể của Hagfish 300 triệu năm trước giống hệt với Hagfish đang bơi lội ngày hôm nay! |  | Hình ảnh so sánh hóa thạch 300 triệu năm và chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện hiện đại: không hề có sự thay đổi lớn nào; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:42.8–00:51.8 (9.0s) | L330 | Chúng đã sống sót qua bốn cuộc đại tuyệt chủng hàng loạt của Trái Đất, chứng kiến loài khủng long bạo chúa T-Rex xuất hiện rồi biến mất hoàn toàn, trong khi Hagfish vẫn ung dung thắt nút thân số tám dưới |  | Khủng long T-Rex gầm rú rồi hóa thạch dưới lòng đất, còn chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện bơi tung tăng dưới đáy biển sâu; KHÔNG có anh MC trong cảnh này. |
| b08 | 00:51.8–00:59.0 (7.2s) | L331 | đáy biển! Chưa hết, Hagfish sở hữu tới 4 quả tim độc lập rải rác khắp cơ thể: một tim chính và ba tim phụ tự đập hàng giờ mà không cần oxy từ não bộ! | **4 QUẢ TIM** · Đập không cần oxy · L/400 · [0.35, 0.72] | Sơ đồ giải phẫu 4 quả tim hoạt hình phát sáng nhịp nhàng dọc thân mình; KHÔNG có anh MC trong cảnh này. |
| b09 | 00:59.0–01:06.5 (7.5s) | L332 | Hệ tuần hoàn phụ này giúp chúng sống sót ngon lành trong những vùng nước đáy biển thiếu oxy đến mức mọi loài cá có xương sống khác đều phải ngạt thở bỏ mạng! |  | Đàn cá thông thường nổi bụng vì thiếu oxy, trong khi chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện vẫn khoan thai bơi lượn nhờ 4 quả tim độc lập; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:06.5–01:12.1 (5.6s) | L333 | Một cỗ máy sinh học bất tử trước thời gian! Cả hội trường đồng loạt cúi đầu kính cẩn chào cụ tổ Hagfish! |  | Khán giả và anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cùng cúi mình chào kính phục; chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện ngoe nguẩy chiếc đuôi đáp lễ; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:12.1–01:20.5 (8.4s) | L334 | Nhưng hãy nhìn sang tổ tiên của hai gã thợ mộc và đào hầm: Hải Ly và Wombat! Họ từng sở hữu những phiên bản quái thú khổng lồ khiến ai nhìn cũng phải khiếp sợ! |  | Bức màn nhung kéo lên để lộ hai bộ xương hóa thạch khổng lồ cao sừng sững; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:20.5–01:28.3 (7.9s) | L335 | Trong kỷ băng hà Bắc Mỹ cách đây 10.000 năm, tổ tiên của Hải Ly là loài Castoroides nặng tới 100kg, to lớn ngang ngửa một chú gấu đen khổng lồ! | **100KG** · Hải ly kỷ băng hà · R/420 · [0.62, 0.52] | Hình vẽ phục dựng Castoroides to lớn sừng sững, hai chiếc răng cửa cong vút dài mười lăm xăng-ti-mét; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:28.3–01:34.7 (6.3s) | L336 | Tuy nhiên, điều bi hài là chú hải ly khổng lồ này lại không biết xây đập và chỉ thích ăn cỏ dại dưới nước, nên đã bị tuyệt chủng khi khí hậu biến đổi! |  | Chú hải ly 100kg ngồi ngơ ngác ăn cỏ, trong khi chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo hiện đại thông minh biết đắp đập gỗ sinh tồn mãnh liệt; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:34.7–01:41.5 (6.9s) | L337 | Còn ở nước Úc, tổ tiên của Wombat là loài quái thú Diprotodon: loài thú có túi lớn nhất từng bước đi trên Trái Đất, nặng tới gần ba tấn và dài hơn | **DÀI 3M** · Quái thú Diprotodon Úc · L/400 · [0.35, 0.72] | Phục dựng quái thú Diprotodon to như chiếc xe tải thế giới tự nhiên, bước đi rung chuyển mặt đất cổ đại Úc; KHÔNG có anh MC trong cảnh này. |
| b15 | 01:41.5–01:48.3 (6.8s) | L338 | 3m! Chiếc mông bọc thép của Wombat ngày nay chính là di sản thu nhỏ được kế thừa từ cỗ xe tăng bọc thép Diprotodon ba tấn thời tiền sử! |  | chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường đứng cạnh chiếc bóng khổng lồ của Diprotodon vỗ mông đầy tự hào; KHÔNG có anh MC trong cảnh này. |
| b16 | 01:48.3–01:55.4 (7.1s) | L339 | Và giải thưởng danh dự cuối cùng thuộc về dòng dõi của Hải Sâm: sinh vật đã có mặt trên Trái Đất từ kỷ Cambri cách đây hơn 500 triệu năm! | **500 TR NĂM** · Kỷ Cambri cổ đại · R/410 · [0.65, 0.48] | Đồ họa biển kỷ Cambri 500 triệu năm trước rực rỡ sắc màu sinh vật cổ sơ; KHÔNG có anh MC trong cảnh này. |
| b17 | 01:55.4–02:02.9 (7.6s) | L340 | 500 triệu năm trước, khi sinh vật trên cạn còn chưa kịp hình thành, tổ tiên của Hải Sâm đã cặm cụi hút bụi lọc sạch cát biển cho hành tinh chúng ta! |  | chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù đứng trên bục danh dự nhận chiếc cúp vàng vinh quang hình hóa thạch cổ đại; KHÔNG có anh MC trong cảnh này. |
| b18 | 02:02.9–02:10.4 (7.4s) | L341 | Họ đã chứng kiến sự thăng trầm của hàng vạn loài sinh vật, bình thản vượt qua mọi biến cố địa chất vĩ đại bằng triết lý lầy lội không xương sống của mình! |  | Hình ảnh Trái Đất xoay vần qua các kỷ địa chất, chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù vẫn ung dung trườn dưới đáy biển xanh mát; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:10.4–02:19.0 (8.6s) | L342 | Và nhìn vào cây phả hệ của Sứa Bất Tử, dòng giống ruột khoang Cnidaria của chúng thậm chí đã xuất hiện từ kỷ Ediacara cách đây hơn 600 triệu năm! |  | Đồ họa biển kỷ Ediacara nguyên thủy 600 triệu năm trước với các sinh vật thân mềm phát quang ma thuật; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:19.0–02:27.4 (8.4s) | L343 | 600 triệu năm trước, khi Trái Đất chỉ là một quả cầu băng tuyết lạnh giá bao phủ khắp các đại dương, tổ tiên của loài sứa đã trôi dạt lơ lửng dưới lớp băng dày! |  | Đàn sứa cổ xưa bơi lội dưới mái vòm băng tuyết nguyên thủy của Trái Đất cổ đại; KHÔNG có anh MC trong cảnh này. |
| b21 | 02:27.4–02:34.2 (6.8s) | L344 | Họ đã vượt qua cuộc đại tuyệt chủng Permi-Triat thảm khốc nhất lịch sử khi 95% phần trăm sinh vật biển bị quét sạch hoàn toàn! |  | Biển cả ngập tràn tro bụi núi lửa và axit, nhưng dòng dõi sứa vẫn bền bỉ hồi sinh và trường tồn tới tận ngày nay; KHÔNG có anh MC trong cảnh này. |
| b22 | 02:34.2–02:40.8 (6.7s) | L345 | Sự trường sinh của Sứa Bất Tử không chỉ nằm ở từng cá thể, mà là sự kiên cường của cả một dòng dõi cổ xưa bậc nhất hành tinh! |  | chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực trôi lơ lửng trên bục danh dự, ánh sáng hào quang tỏa ra như ngôi sao cổ đại lấp lánh; KHÔNG có anh MC trong cảnh này. |
| b23 | 02:40.8–02:48.7 (7.9s) | L346 | Còn nhìn về phả hệ của Kỳ Nhông Axolotl, chúng là hậu duệ trực tiếp của nhóm lưỡng cư cổ đại Temnospondyli từng thống trị Trái Đất từ 300 triệu năm trước! |  | Phục dựng quái thú lưỡng cư cổ đại Temnospondyli dài hai mét với chiếc đầu dẹt to bản và hàm răng sắc bén; KHÔNG có anh MC trong cảnh này. |
| b24 | 02:48.7–02:56.5 (7.8s) | L347 | Vào thời kỳ khủng long còn chưa xuất hiện, những cụ tổ lưỡng cư khổng lồ này đã làm chủ các đầm lầy than đá bằng khả năng tái sinh chi và thích nghi môi trường nước ngọt đỉnh cao! |  | Chú lưỡng cư khổng lồ bơi lội săn cá trong đầm lầy kỷ Than Đá nguyên sơ; KHÔNG có anh MC trong cảnh này. |
| b25 | 02:56.5–03:04.8 (8.3s) | L348 | Trải qua hàng trăm triệu năm tiến hóa thu nhỏ lại thành chú kỳ nhông 70 gam xinh xắn, Axolotl vẫn lưu giữ trọn vẹn chiếc chìa khóa tái sinh cổ đại của tổ tiên mình! |  | Chú kỳ nhông chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói nhỏ bé đứng cạnh chiếc bóng vĩ đại của cụ tổ Temnospondyli mỉm cười tự hào; KHÔNG có anh MC trong cảnh này. |
| b26 | 03:04.8–03:12.9 (8.1s) | L349 | Thậm chí trong các lớp đá trầm tích kỷ Than Đá, người ta còn tìm thấy những dấu vết hóa thạch của chất keo nhớt Hagfish được bảo tồn nguyên vẹn qua 300 triệu năm thời |  | Phiến đá cổ đại hiển thị vệt hóa thạch của sợi tơ nhớt protein nguyên thủy phát sáng huỳnh quang; KHÔNG có anh MC trong cảnh này. |
| b27 | 03:12.9–03:22.4 (9.5s) | L350 | gian! Điều này chứng minh rằng công thức phân tử của sợi tơ protein Hagfish hoàn hảo đến mức mẹ thiên nhiên không cần phải chỉnh sửa hay nâng cấp thêm bất kỳ chi tiết nào suốt 300 triệu năm qua! |  | Hình ảnh cụ tổ chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện bơi qua thời gian từ quá khứ đến hiện tại với vẹn nguyên sức mạnh; KHÔNG có anh MC trong cảnh này. |
| b28 | 03:22.4–03:29.5 (7.1s) | L351 | Không chỉ vậy, Cá Mút Đá Hagfish còn có thể sống sót kỳ diệu suốt 36 giờ trong môi trường hoàn toàn không có khí oxy dưới lớp bùn đáy biển sâu! |  | Mô hình chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện vùi sâu trong lớp bùn đen kịt thiếu oxy nhưng tim vẫn đập chậm rãi bền bỉ; KHÔNG có anh MC trong cảnh này. |
| b29 | 03:29.5–03:36.5 (7.0s) | L352 | Chúng chuyển hóa lượng đường glycogen dự trữ trong các mô cơ mà không cần oxy, giữ cho 4 quả tim vẫn hoạt động nhịp nhàng qua cơn thiếu thốn! |  | Đồ họa chu trình đường phân kỵ khí thắp sáng bốn quả tim của chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện dưới đáy vực sâu; KHÔNG có anh MC trong cảnh này. |
| b30 | 03:36.5–03:43.1 (6.6s) | L353 | Đó là minh chứng cho sức sống bền bỉ đã giúp Hagfish vượt qua năm đại tuyệt chủng lớn nhất của lịch sử Trái Đất mà không cần biến đổi hình dạng! |  | Mô hình dòng thời gian năm đại tuyệt chủng lướt qua, chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện vẫn ung dung bơi lội từ thời kỷ Cambri đến nay; KHÔNG có anh MC trong cảnh này. |
| b31 | 03:43.1–03:51.8 (8.7s) | L354 | Ban tổ chức xin trao tặng Cúp Vinh Danh Cổ Vật Sống Danh Dự cho Cá Mút Đá Hagfish và Hải Sâm! Một tràng pháo tay cho sự trường tồn vĩ đại của muôn loài! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao hai chiếc cúp đá cẩm thạch phát sáng cho chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện và chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù t |
| b32 | 03:51.8–03:59.8 (8.0s) | L355 | Lễ trao giải phụ khép lại trong niềm tự hào vô bờ bến! Bây giờ, hãy hít một hơi thật sâu vì chúng ta sắp bước vào Vòng bảy: Phúc Khảo Tin Đồn Thế Kỷ! |  | Đèn sân khấu chuyển sang màu xanh neon bí ẩn, chuẩn bị cho những màn bẻ lái sự thật ngoạn mục; KHÔNG có anh MC trong cảnh này. |

### scene10 · PHÚC KHẢO TIN ĐỒN THẾ KỶ & ĐẬP TAN NHỮNG LẦM TƯỞNG · 255.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.9 (7.9s) | L356 | Đèn sân khấu đổi màu rực rỡ! Chào mừng quý vị đến với Vòng bảy: Phúc Khảo Tin Đồn Thế Kỷ và Đập Tan Những Lầm Tưởng! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng bước ra giữa sàn đấu, phía sau là màn hình lớn chiếu biểu tượng chiếc kính lúp vạch trần tin giả; tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng ô thử thách số bảy. |
| b02 | 00:07.9–00:14.5 (6.6s) | L357 | Đây là vòng thi nơi ban giám khảo sẽ đưa ra hàng loạt tin đồn nổi tiếng trên mạng xã hội về mười tuyển thủ để đối chất bằng khoa học thực nghiệm! |  | Màn hình hiện lên các bài báo mạng giật gân hoạt hình với dấu chấm hỏi to đùng; KHÔNG có anh MC trong cảnh này. |
| b03 | 00:14.5–00:22.9 (8.4s) | L358 | Trong thời đại thông tin bùng nổ, nhiều sinh vật bị đồn thổi thành những vị thần bất khả chiến bại hoặc bị gán cho những thói quen ăn uống hoàn toàn sai lệch! |  | Hình ảnh biểu tượng tin giả mạng xã hội bị một chiếc búa công lý gõ vỡ tan tành; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:22.9–00:28.8 (5.9s) | L359 | Tin đồn số một: Sứa Bất Tử là sinh vật trường sinh bất lão tuyệt đối, không có bất kỳ thứ gì trên đời có thể tiêu diệt được chúng?! |  | Hình ảnh một chú sứa phát hào quang bất tử lơ lửng giữa vũ trụ như vị thần bất khả chiến bại; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:28.8–00:34.6 (5.8s) | L360 | Sự thật khoa học là gì? Bà Cú giám khảo lập tức gõ búa đính chính: Sứa Bất Tử chỉ bất tử về mặt lão hóa sinh học tự nhiên |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ búa, hình ảnh thần thánh biến mất, thay bằng thực tế đại dương khắc nghiệt; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:34.6–00:42.8 (8.2s) | L361 | mà thôi! Trong môi trường biển khơi, kích thước chỉ 4,5mm biến chúng thành món tráng miệng khoái khẩu tuyệt vời cho rùa biển, cá mặt trăng và các loài sứa lớn khác! |  | Một chú rùa biển hoạt hình bơi qua hả miệng đớp trọn cả đàn sứa nhỏ như nuốt kẹo thạch ngon lành; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:42.8–00:51.2 (8.3s) | L362 | Hơn nữa, nếu gặp một đợt sóng thần đánh dạt lên bãi cát khô nóng hoặc bị nhiễm khuẩn nấm đại dương, chú sứa bất tử này vẫn sẽ hóa thành một vũng nước khô queo trên bờ biển! |  | Chú sứa nằm trên bãi cát nắng gắt rên rỉ, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vội cầm bình xịt tưới nước giải cứu; KHÔNG có anh MC trong cảnh này. |
| b08 | 00:51.2–00:56.3 (5.2s) | L363 | Khái niệm bất tử ở đây là không chết vì tuổi già, chứ không phải là mình đồng da sắt chống lại kẻ săn mồi! |  | chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực cười trừ gãi đầu công nhận sự thật trần trụi; KHÔNG có anh MC trong cảnh này. |
| b09 | 00:56.3–01:02.9 (6.6s) | L364 | Nếu không có chuỗi thức ăn kiểm soát số lượng, chỉ sau vài năm loài sứa bất tử này có thể nhân bản tràn ngập mọi đại dương trên Trái Đất! |  | Đồ họa biển ngập tràn sứa nhỏ lấp lánh để minh họa tầm quan trọng của rùa biển trong việc cân bằng sinh thái; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:02.9–01:10.4 (7.5s) | L365 | Một pha bẻ lái định nghĩa khoa học cực kỳ chuẩn xác! Tiếp tục với tin đồn số hai: Hải Ly là loài động vật kỳ quặc thích ăn gỗ mục để sống?! |  | Hình ảnh chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo ngồi gặm một khúc gỗ khô cứng ngắc như nhai bánh quy giòn tan; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:10.4–01:17.6 (7.2s) | L366 | Đây là một sự hiểu lầm tai hại lớn nhất về loài Hải Ly! Đường ruột của Hải Ly hoàn toàn không thể tiêu hóa được phần gỗ lõi cứng chắc của thân cây! |  | Sơ đồ đường ruột của chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo: khúc gỗ lõi cứng bị chặn lại ở dạ dày không tiêu hóa được; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:17.6–01:24.2 (6.6s) | L367 | Khẩu phần ăn thật sự của chúng là lớp mô mềm màu xanh giàu đường và dinh dưỡng nằm ngay sát dưới lớp vỏ cây, cùng với chồi non và lá cây tươi! |  | chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo khéo léo dùng răng bóc tách lớp vỏ xanh non mềm mại ăn ngon lành, bỏ lại phần lõi gỗ cứng sang một bên; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:24.2–01:31.3 (7.1s) | L368 | Những khúc gỗ cứng cáp bị đốn ngã chỉ được Hải Ly tận dụng làm vật liệu xây dựng con đập kiên cố ngăn dòng nước lũ, chứ không phải thức ăn trong thực đơn hàng ngày! |  | chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo vác khúc gỗ cứng xếp vào thân đập, tay kia cầm cành lá xanh nhai nhóp nhép khoái chí; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:31.3–01:38.6 (7.3s) | L369 | Chúng ta đã oan uổng gán cho Hải Ly cái mác thèm ăn gỗ suốt hàng thế kỷ qua, trong khi chúng chỉ là những người sành ăn vỏ cây dinh dưỡng! |  | chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo ôm bụng cười, tay giơ đĩa thức ăn gồm chồi non và lá cây xanh mướt; KHÔNG có anh MC trong cảnh này. |
| b15 | 01:38.6–01:44.8 (6.2s) | L370 | Đến tin đồn số ba: Ếch Wolverine tự bẻ xương xuyên qua thịt chân như vậy thì có cảm thấy đau đớn đến thấu xương hay không? |  | chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng giơ ngón chân có vuốt xương lên, biểu cảm suy tư bí hiểm; KHÔNG có anh MC trong cảnh này. |
| b16 | 01:44.8–01:50.0 (5.3s) | L371 | Các nhà thần kinh học động vật xác nhận: loài ếch này có đầy đủ các thụ thể cảm nhận đau đớn nociceptor dưới da! |  | Đồ họa xung thần kinh cảm giác đau chạy dọc từ ngón chân lên não bộ của ếch; KHÔNG có anh MC trong cảnh này. |
| b17 | 01:50.0–01:58.6 (8.6s) | L372 | Tuy nhiên, trong khoảnh khắc cận kề cái chết trước kẻ thù, tuyến thượng thận của chúng lập tức giải phóng một lượng khổng lồ hormone adrenaline và các peptit giảm đau nội sinh! |  | Dòng hormone phát sáng tràn ngập cơ thể, khóa chặt các cổng tiếp nhận tín hiệu đau ở tủy sống; KHÔNG có anh MC trong cảnh này. |
| b18 | 01:58.6–02:07.2 (8.5s) | L373 | Cơ chế này tạm thời gây tê liệt cảm giác đau đớn cục bộ, giúp chú ếch tập trung trọn vẹn 100% sức lực để tung đòn móng vuốt sinh tử hạ gục kẻ săn mồi! |  | chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng tung cú đá vuốt xương uy lực hạ gục con rắn săn mồi trong sự thán phục của khán giả; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:07.2–02:13.5 (6.4s) | L374 | Và sau khi hiểm nguy qua đi, cảm giác ê ẩm xuất hiện chính là tín hiệu kích hoạt chu trình tiết dịch kháng khuẩn làm lành mô da thần tốc! |  | Vết thương khép miệng, chú ếch ngồi nghỉ ngơi dưới bóng râm dòng suối bình yên; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:13.5–02:22.0 (8.4s) | L375 | Thêm một tin đồn nổi tiếng khác về Bạch Tuộc Mimic: liệu chúng có thật sự nhận thức được mình đang bắt chước loài nào hay chỉ là phản xạ đổi màu ngẫu nhiên? |  | chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình đứng trước màn hình đối chất, xung quanh là các nhà khoa học đang theo dõi; KHÔNG có anh MC trong cảnh này. |
| b21 | 02:22.0–02:30.2 (8.2s) | L376 | Các thí nghiệm của tiến sĩ Mark Norman tại Indonesia đã chứng minh: Bạch Tuộc Mimic sở hữu trí nhớ thị giác và tư duy phân tích chiến thuật đỉnh cao! |  | Phòng thí nghiệm đại dương: khi thả một con cá bơn săn mồi vào, chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình không đổi màu ngẫu nhiên mà lập tức biến hình thành rắn biển đầu đen chuyên ăn thịt cá bơn! KHÔNG có anh MC trong cảnh này. |
| b22 | 02:30.2–02:38.7 (8.5s) | L377 | Chúng quan sát chính xác đối thủ đang tiếp cận là ai, nhớ lại kẻ thù tự nhiên của đối thủ đó trong tự nhiên, rồi mới quyết định hóa thân thành loài khắc chế phù hợp nhất! |  | Sơ đồ tư duy logic của bạch tuộc: nhận diện đối thủ -> tra cứu hồ sơ khắc tinh -> kích hoạt hệ cơ biến hình chuẩn xác; KHÔNG có anh MC trong cảnh này. |
| b23 | 02:38.7–02:46.5 (7.9s) | L378 | Một sự tính toán chiến thuật hoàn toàn chủ động chứ không hề là phản xạ vô thức may rủi! Cả khán đài gật gù khâm phục trí tuệ loài động vật thân mềm! |  | chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình giơ một xúc tu nháy mắt chào khán giả đầy tinh tế; KHÔNG có anh MC trong cảnh này. |
| b24 | 02:46.5–02:53.5 (7.0s) | L379 | Và một tin đồn thú vị khác về Gấu Wombat: có phải chúng dùng hai chân sau để nặn phân thành hình khối lập phương hay không? |  | Hình ảnh hoạt hình hài hước: chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường ngồi nặn phân như nặn bánh bột lọc bằng hai tay; KHÔNG có anh MC trong cảnh này. |
| b25 | 02:53.5–03:00.8 (7.2s) | L380 | Bà Cú giám khảo cười lớn đính chính: hoàn toàn không phải do nặn bằng tay hay chân! Đó là 100% kết quả của cơ chế thủy lực và áp suất đường ruột tự nhiên! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ giơ biểu đồ động lực học chất lưu giải thích cơ chế ép góc 90 độ của các múi cơ ruột già; KHÔNG có anh MC trong cảnh này. |
| b26 | 03:00.8–03:10.4 (9.7s) | L381 | Phân của Wombat đi vào đoạn ruột già ở thể lỏng sệt, và qua quá trình hút nước cực mạnh kết hợp lực co bóp đàn hồi không đều, chúng tự động đông cứng thành các khối hộp vuông vức hoàn hảo trước khi ra ngoài! |  | Đồ họa ruột co bóp nén ép tự động nhả ra từng viên gạch phân lập phương vuông chằn chặn; KHÔNG có anh MC trong cảnh này. |
| b27 | 03:10.4–03:18.9 (8.5s) | L382 | Và sự thật về chiếc móng vuốt của Ếch Wolverine: xương ngón chân tự bẻ gãy không hề làm đứt gãy mạch máu lớn hay gây hoại tử nhờ một lớp vỏ bọc collagen dạng sợi cực kỳ dẻo |  | Đồ họa bàn chân sau của ếch: bao xơ collagen co giãn nhẹ nhàng ôm lấy đầu xương nhọn bảo vệ tế bào mô; KHÔNG có anh MC trong cảnh này. |
| b28 | 03:18.9–03:26.6 (7.7s) | L383 | dai! Khi móng vuốt thụt vào, lớp vỏ này đóng vai trò như một chiếc băng gạc sinh học ép chặt vết rách, ngăn chặn máu chảy và kích thích tế bào biểu mô phân chia thần tốc! |  | Vết rách khép miệng nhanh như một chiếc khóa kéo tự động kéo lại mượt mà; KHÔNG có anh MC trong cảnh này. |
| b29 | 03:26.6–03:34.3 (7.8s) | L384 | Viện nghiên cứu sinh học quốc tế cũng xác nhận: chất nhầy của Hagfish khi sấy khô có thể dệt thành sợi tơ nhân tạo bền gấp 10 lần sợi nylon tổng hợp! |  | Cuộn tơ dệt từ protein chất nhầy chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện sáng bóng, mảnh mai nhưng bền chắc nâng được vật nặng; KHÔNG có anh MC trong cảnh này. |
| b30 | 03:34.3–03:41.0 (6.7s) | L385 | Sợi tơ sinh học này có khả năng tự phân hủy hoàn toàn trong môi trường tự nhiên, mở ra cuộc cách mạng thời trang xanh không rác thải nhựa! |  | Sợi vải sinh thái tan biến nhẹ nhàng trong đất bón cho cây non xanh tốt; KHÔNG có anh MC trong cảnh này. |
| b31 | 03:41.0–03:46.1 (5.1s) | L386 | Thiên nhiên đã trao tặng cho những dị nhân này những giải pháp sinh học đi trước công nghệ con người hàng trăm triệu năm! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vung tay chỉ lên màn hình so sánh giữa công nghệ hiện đại và cấu trúc sinh học tuyệt mỹ của các sinh vật; tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng rực các dữ liệu khoa học. |
| b32 | 03:46.1–03:54.0 (8.0s) | L387 | Ban giám khảo xin công bố kết quả Vòng bảy! Huy chương Đồng thuộc về Kỳ Nhông Axolotl với bí ẩn trạng thái ấu trùng neoteny suốt đời! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ búa trao huy chương đồng cho chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói. |
| b33 | 03:54.0–03:59.4 (5.4s) | L388 | Huy chương Bạc thuộc về kỹ sư Hải Ly với lời minh oan đanh thép cho khẩu phần ăn vỏ cây dinh dưỡng! |  | chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo nhận tấm huy chương bạc thứ ba của mình trong tiếng reo hò. |
| b34 | 03:59.4–04:06.0 (6.6s) | L389 | Và Huy chương Vàng ba điểm xuất sắc thuộc về Sứa Bất Tử với bài học phân biệt giữa bất tử sinh học và chuỗi thức ăn đại dương! |  | chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực bay lượn đón nhận chiếc huy chương vàng thứ hai, tỏa ánh hào quang hồng tím rực rỡ. |
| b35 | 04:06.0–04:15.4 (9.4s) | L390 | Bảng tổng sắp sau bảy vòng đấu chính thức đã chứng kiến sự bứt phá ngoạn mục: Sứa Bất Tử và Hải Ly cùng dẫn đầu với tám điểm! Gấu Wombat bám sát với năm điểm! Axolotl sáu điểm! |  | tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) cập nhật điểm số: Sứa Bất Tử 8 điểm, Hải Ly 8 điểm, Axolotl 6 điểm, Wombat 5 điểm, Hải Sâm 3 điểm, Chuột Chũi Sao 3 điểm, Hagfish 3 điểm, Bạch Tuộc Mimic 2 điểm, Ếch dị nhân móng vuốt hoạt hình đáng yêu 2 điểm, Kiến Nổ 1 điểm; cuộc soán ngôi vương đang đến hồi nghẹt thở nhất! |

### scene11 · THÍ NGHIỆM TƯƠNG LAI · 234.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.4 (7.4s) | L391 | Căng thẳng tột cùng! Chào mừng quý vị đến với Vòng Bán Kết: Soi Kính Hiển Vi Điện Tử và Máy Gia Tốc Hạt Đồng Bộ! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng khoác áo blouse trắng của nhà khoa học, dẫn đầu đoàn giám khảo bước vào phòng thí nghiệm tối tân với các máy móc lượng tử phát sáng; tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng ô bán kết mang hình kính hiển vi. |
| b02 | 00:07.4–00:14.7 (7.3s) | L392 | Đây là vòng thi nơi khoa học đỉnh cao của con người dùng các thiết bị đắt giá hàng triệu đô la để vén màn những kết cấu vật liệu vi mô không tưởng! |  | Màn hình lớn kết nối trực tiếp với kính hiển vi điện tử quét và máy quét synchrotron; KHÔNG có anh MC trong cảnh này. |
| b03 | 00:14.7–00:21.7 (7.1s) | L393 | Những bí mật cấu trúc tinh thể nano ẩn sâu trong tế bào các dị nhân chính là nguồn cảm hứng vô tận cho cuộc cách mạng công nghệ tương lai! |  | Đồ họa mạng lưới tinh thể phân tử chuyển động quay ba chiều sắc nét; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:21.7–00:26.4 (4.7s) | L394 | Mẫu thử nghiệm đầu tiên được đưa vào buồng chân không: sợi tơ nhớt protein của Cá Mút Đá Hagfish! |  | Kỹ thuật viên dùng kẹp gắp một sợi tơ trong suốt của chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện đặt lên đĩa soi điện tử; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:26.4–00:33.6 (7.2s) | L395 | Dưới chùm tia X cực mạnh của máy gia tốc hạt, các nhà nghiên cứu vật liệu tại đại học Guelph đã phát hiện ra cấu trúc tinh thể siêu việt của sợi tơ này! |  | Đồ họa nguyên tử phóng to: các chuỗi protein cuộn xoắn thành các tấm gấp beta đan kết chéo vô cùng chặt chẽ; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:33.6–00:39.7 (6.1s) | L396 | Bên trong mỗi tế bào nhớt chứa một cuộn tơ dài tới 15cm nhưng được quấn tròn thành một viên nang nhỏ chỉ 100 micro-mét! |  | Cuộn tơ mở ra như chiếc lò xo nén cực đại bung ra thành mạng lưới sợi dày đặc trong nước; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:39.7–00:48.4 (8.7s) | L397 | Khi bung ra trong nước biển, các chuỗi axit amin kỵ nước lập tức hút chặt lấy nhau, biến thể lỏng thành thể gel siêu đàn hồi có thể kéo dài gấp 3 lần mà không hề bị đứt gãy! | **GẤP 3 LẦN** · Độ đàn hồi cực cao · R/410 · [0.65, 0.48] | Cánh tay robot kéo giãn sợi tơ ra gấp ba lần độ dài ban đầu rồi thả ra, sợi tơ co lại đàn hồi hoàn hảo; KHÔNG có anh MC trong cảnh này. |
| b08 | 00:48.4–00:55.1 (6.8s) | L398 | Độ bền kéo của sợi tơ này đạt mức 100 80 megapascal, tương đương với độ bền của các sợi gân nhân tạo tốt nhất mà con người từng chế tạo! |  | Đồ thị đo lực kéo đứt: đường cong của tơ Hagfish vượt xa sợi nylon và tiệm cận độ dai của hợp kim nhẹ; KHÔNG có anh MC trong cảnh này. |
| b09 | 00:55.1–01:00.5 (5.4s) | L399 | Một kỳ quan công nghệ nano của biển sâu có tuổi đời 300 triệu năm! Cả hội trường vỗ tay rầm rộ! |  | Các nhà khoa học hoạt hình giơ ngón tay cái tán thưởng trước số liệu hiển thị trên màn hình; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng mỉm cười thán phục. |
| b10 | 01:00.5–01:04.5 (4.0s) | L400 | Tiếp theo, hãy đưa lớp da của Hải Sâm vào máy thử nghiệm cơ học biến dạng! |  | Một mẩu mô da của chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù được đặt vào máy đo lực nén và độ đàn hồi; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:04.5–01:10.2 (5.7s) | L401 | Các nhà sinh học phát hiện: da của Hải Sâm được cấu tạo từ một loại mô liên kết biến đổi đặc biệt gọi tắt là M-T-C! |  | Cấu trúc sợi collagen hoạt hình liên kết với nhau bằng các cầu nối hóa học màu xanh lá cây; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:10.2–01:15.2 (5.0s) | L402 | Hải Sâm không hề sử dụng cơ bắp hay tiêu tốn năng lượng A-T-P để gồng cứng cơ thể như các loài động vật thông thường! |  | Đồ họa các hạt truyền tín hiệu thần kinh phóng thích vào mô liên kết; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:15.2–01:22.2 (7.0s) | L403 | Thay vào đó, các tế bào thần kinh chỉ cần tiết ra một lượng nhỏ phân tử điều hòa để khóa chặt hoặc tháo rời các cầu nối giữa các sợi collagen trong vài trăm mili-giây! |  | Khi cần cứng, các cầu nối khóa chặt, mẩu da biến thành tảng đá cứng ngắc đập búa vào kêu keng keng; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:22.2–01:29.8 (7.6s) | L404 | Và khi cần thoát thân qua khe đá hẹp, các cầu nối tự bung ra, toàn bộ cơ thể Hải Sâm hóa lỏng mềm nhũn như một khối thạch rau câu trôi tuột qua kẽ hở! |  | Cơ thể chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù mềm nhũn như giọt nước chảy luồn qua khe đá hẹp chỉ rộng một xăng-ti-mét rồi đông cứng trở lại; KHÔNG có anh MC trong cảnh này. |
| b15 | 01:29.8–01:37.2 (7.4s) | L405 | Các kỹ sư y sinh đang ứng dụng cơ chế hóa lỏng này để chế tạo các điện cực cấy ghép não bộ: mềm dẻo khi luồn vào mô não nhưng cứng cáp khi định vị chính xác! |  | Mô hình điện cực nano lấy cảm hứng từ da Hải Sâm cấy vào mô thần kinh một cách an toàn hoàn hảo; KHÔNG có anh MC trong cảnh này. |
| b16 | 01:37.2–01:40.8 (3.6s) | L406 | Và cuối cùng là màn soi siêu vi cơ quan Eimer trên chiếc mũi sao của Chuột |  | Đầu xúc tu hồng của chú Chuột Chũi Mũi Sao hoạt hình lông đen nhung mượt mà, mũi xòe ra 22 xúc tu đỏ hồng như bông hoa sao biển, đeo kính râm mù lòa nhưng phản xạ siêu thanh được phóng đại mười ngàn lần trên kính hiển vi điện tử quét; KHÔNG có anh MC trong cảnh này. |
| b17 | 01:40.8–01:47.8 (7.1s) | L407 | Chũi! Mỗi chiếc nhú Eimer hình nấm tí hon chứa một cụm đầu dây thần kinh Merkel cực kỳ tinh vi, có thể nhận biết sự biến dạng bề mặt đất chỉ ở mức... một nanomet! |  | Mô hình nguyên tử: một hạt bụi nhỏ xíu chạm vào bề mặt nhú nấm làm phát ra xung điện thần kinh cực nhạy; KHÔNG có anh MC trong cảnh này. |
| b18 | 01:47.8–01:56.0 (8.1s) | L408 | Một nanomet nhỏ hơn cả đường kính của chuỗi xoắn kép D-N-A! Chuột Chũi Mũi Sao không chỉ sờ thấy con mồi, chúng sờ thấy cả kết cấu phân tử của đất! |  | chú Chuột Chũi Mũi Sao hoạt hình lông đen nhung mượt mà, mũi xòe ra 22 xúc tu đỏ hồng như bông hoa sao biển, đeo kính râm mù lòa nhưng phản xạ siêu thanh đeo kính râm nhếch mép ngầu, chiếc mũi sao biển phát ra các vòng sóng quét laser chính xác tuyệt đối; KHÔNG có anh MC trong cảnh này. |
| b19 | 01:56.0–02:03.4 (7.4s) | L409 | Để kiểm tra độ bền của chiếc mông bọc thép Wombat, ban giám khảo đã đưa tấm khiên sụn vào máy thử nghiệm búa tạ thủy lực công nghiệp! |  | Một chiếc búa đập thủy lực khổng lồ giáng thẳng xuống tấm giáp mẫu của chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường với lực ép lên tới hai tấn; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:03.4–02:11.1 (7.7s) | L410 | Rầm! Chiếc búa nảy ngược trở lại trong khi lớp sụn mô mạc sợi của Wombat chỉ lún nhẹ xuống rồi lập tức đàn hồi trở lại hình dáng ban đầu không hề nứt vỡ! |  | Máy đo áp lực hiển thị chỉ số triệt tiêu lực đạt chín mươi lăm phần trăm, bảo vệ hoàn toàn bên trong cơ thể bên trong khỏi chấn thương; KHÔNG có anh MC trong cảnh này. |
| b21 | 02:11.1–02:19.0 (7.9s) | L411 | Các kỹ sư chế tạo xe hơi bọc thép và mũ bảo hiểm phi hành gia đang nghiên cứu cấu trúc sụn đan sợi này để phát triển vật liệu hấp thụ xung lực thế hệ mới! |  | Bản thiết kế mũ bảo hiểm công nghệ cao lấy cảm hứng từ cấu trúc mông bọc thép của chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường; KHÔNG có anh MC trong cảnh này. |
| b22 | 02:19.0–02:27.8 (8.8s) | L412 | Tại phòng thí nghiệm công nghệ sinh học, các nhà khoa học đã dùng protein phát quang xanh lá cây G-F-P để theo dõi đường đi của từng tế bào tái sinh trong cơ thể Axolotl! |  | Kính hiển vi huỳnh quang rọi vào mầm tái sinh của chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói: từng tế bào phát sáng xanh neon di chuyển dệt nên mô cơ mới; KHÔNG có anh MC trong cảnh này. |
| b23 | 02:27.8–02:35.8 (8.0s) | L413 | Họ phát hiện một tín hiệu điều khiển thần kỳ: các tế bào thần kinh ngoại biên liên tục phát ra dòng điện sinh học vi mô dẫn đường cho các tế bào cơ di chuyển chính xác đến từng micromet! |  | Dòng xung điện xanh lam chạy dọc sợi thần kinh chỉ đường cho các tế bào ghép nối hoàn hảo không một sai sót; KHÔNG có anh MC trong cảnh này. |
| b24 | 02:35.8–02:42.7 (6.9s) | L414 | Công nghệ lập bản đồ tế bào này đang mở ra hướng đi đột phá trong việc chế tạo các chi giả sinh học thông minh kết nối trực tiếp với não bộ con người! |  | Cánh tay robot công nghệ cao cử động nhịp nhàng theo ý nghĩ của con người trong phòng thử nghiệm; KHÔNG có anh MC trong cảnh này. |
| b25 | 02:42.7–02:52.0 (9.3s) | L415 | Máy đo phổ tán xạ tia X còn cho thấy: các sợi tơ Hagfish có thể tự sắp xếp lại cấu trúc tinh thể khi chịu lực kéo giật đột ngột, biến lực kéo nguy hiểm thành nhiệt lượng khuếch tán ra môi trường nước! |  | Đồ thị phổ tán xạ tia X: các liên kết hydro tự sắp xếp lại hấp thụ trọn vẹn năng lượng va đập; KHÔNG có anh MC trong cảnh này. |
| b26 | 02:52.0–03:00.3 (8.3s) | L416 | Khả năng hấp thụ xung lực tuyệt đỉnh này chính là chìa khóa vàng giúp chiếc bẫy nhớt Hagfish không bao giờ bị xé rách bởi những cú giãy giụa điên cuồng của cá mập săn mồi! |  | Con cá mập giãy giụa dữ dội trong khối keo nhớt nhưng màng tơ càng siết chặt đàn hồi không thể phá vỡ; KHÔNG có anh MC trong cảnh này. |
| b27 | 03:00.3–03:07.1 (6.8s) | L417 | Cuộc chạm trán nảy lửa giữa công nghệ tái sinh của Axolotl và cơ chế đảo ngược thời gian của Sứa Bất Tử đã làm nổ tung cầu trường! |  | chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói và chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực cùng tỏa sáng trên hai cột năng lượng mô phỏng của phòng thí nghiệm tương lai; KHÔNG có anh MC trong cảnh này. |
| b28 | 03:07.1–03:15.4 (8.3s) | L418 | Một bên là khả năng mọc lại mô tạng thần tốc chỉ sau vài tuần ngắn ngủi, một bên là thuật chuyển hóa tế bào đưa toàn bộ cơ thể trở về tuổi ấu thơ! |  | Đồ họa phân đôi màn hình: cánh tay chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói tái tạo cơ bắp hoàn chỉnh bên cạnh chu trình trẻ hóa không hồi kết của chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực; KHÔNG có anh MC trong cảnh này. |
| b29 | 03:15.4–03:23.0 (7.6s) | L419 | Các nhà khoa học trên khán đài không ngừng ghi chép dữ liệu, đây chính là hai chìa khóa vàng mở toang cánh cửa chữa lành bách bệnh cho nhân loại mai sau! |  | Các nhà khoa học vỗ tay nồng nhiệt, màn hình máy tính nhảy hàng triệu chuỗi mã gen quý giá; KHÔNG có anh MC trong cảnh này. |
| b30 | 03:23.0–03:30.3 (7.3s) | L420 | Ban giám khảo xin công bố bảng điểm Vòng Bán Kết! Huy chương Đồng thuộc về Chuột Chũi Mũi Sao với cảm biến xúc giác nhạy tới một nanomet! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ búa, trao huy chương đồng phát sáng cho chú Chuột Chũi Mũi Sao hoạt hình lông đen nhung mượt mà, mũi xòe ra 22 xúc tu đỏ hồng như bông hoa sao biển, đeo kính râm mù lòa nhưng phản xạ siêu thanh. |
| b31 | 03:30.3–03:36.2 (5.9s) | L421 | Huy chương Bạc thuộc về Hải Sâm với mô liên kết biến đổi M-T-C tự hóa lỏng cơ thể không tốn năng lượng! |  | chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù vui mừng đón nhận tấm huy chương bạc quý giá thứ hai của mình. |
| b32 | 03:36.2–03:42.7 (6.6s) | L422 | Và Huy chương Vàng ba điểm xuất sắc thuộc về cụ tổ Cá Mút Đá Hagfish với kiến trúc tinh thể tơ protein siêu việt! |  | chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện đứng trên bục vinh quang nhận huy chương vàng, toàn thân phát sáng lấp lánh giữa tiếng reo hò rền vang. |
| b33 | 03:42.7–03:54.0 (11.3s) | L423 | Bảng điểm sau vòng Bán Kết tạo nên một cơn địa chấn chưa từng có: Sứa Bất Tử và Hải Ly cùng dẫn đầu với tám điểm! Hagfish bứt phá thần tốc lên sáu điểm ngang hàng với Axolotl! Wombat và Hải Sâm cùng có năm điểm! |  | tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) cập nhật điểm số: Sứa Bất Tử 8 điểm, Hải Ly 8 điểm, Axolotl 6 điểm, Hagfish 6 điểm, Wombat 5 điểm, Hải Sâm 5 điểm, Chuột Chũi Sao 4 điểm, Bạch Tuộc Mimic 2 điểm, Ếch dị nhân móng vuốt hoạt hình đáng yêu 2 điểm, Kiến Nổ 1 điểm; mọi ánh mắt đang hướng về Vòng Chung Kết Điểm Nhân |

### scene12 · MÓN QUÀ CHO NHÂN LOẠI — CÔNG NGHỆ TƯƠNG LAI ĐỘT PHÁ (ĐIỂM NHÂN ĐÔI) · 251.8s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.4 (8.4s) | L424 | Giờ khắc lịch sử đã điểm! Toàn thể đấu trường nín thở chào đón Vòng Chung Kết: Món Quà Cho Nhân Loại và Những Đột Phá Công Nghệ Tương Lai! |  | Dàn pháo sáng rực rỡ bùng nổ quanh đấu trường, âm nhạc giao hưởng hào hùng vang lên; tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) nhấp nháy sáng rực ô Chung Kết mang chữ Điểm Nhân Đôi. |
| b02 | 00:08.4–00:16.8 (8.4s) | L425 | Đây là vòng thi quyết định số phận chiếc vương miện tối cao: Huy chương Đồng được hai điểm, Huy chương Bạc bốn điểm, và Huy chương Vàng lên tới sáu điểm tròn! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ giơ cao ba chiếc huy chương đại hội khổng lồ phát ánh hào quang chói lọi; KHÔNG có anh MC trong cảnh này. |
| b03 | 00:16.8–00:24.2 (7.4s) | L426 | Ở vòng đấu này, chúng ta đánh giá tiềm năng ứng dụng thực tiễn của mười tuyển thủ trong việc giải cứu y học, công nghệ và tương lai của loài người! |  | Màn hình lớn chiếu các mô hình bệnh viện tương lai, tàu không gian và robot sinh học; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:24.2–00:32.3 (8.0s) | L427 | Không phải danh hiệu hão huyền, những món quà tiến hóa mà muôn loài trao tặng cho nền văn minh nhân loại chính là giá trị bất tử đích thực của sự sống! |  | Hình ảnh bàn tay con người nâng niu địa cầu, các nhánh công nghệ sinh học tỏa sáng rực rỡ; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:32.3–00:37.4 (5.1s) | L428 | Ứng cử viên đầu tiên tiến vào vòng đánh giá: cụ tổ Cá Mút Đá Hagfish với cuộc cách mạng vật liệu sinh thái! |  | chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện bơi trong buồng thí nghiệm, bên cạnh là các kỹ sư vật liệu của Hải quân Hoa Kỳ đang thử nghiệm sợi tơ; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:37.4–00:43.2 (5.8s) | L429 | Hiện nay, sợi Kevlar dùng để may áo giáp chống đạn quân sự được sản xuất từ dầu mỏ với quy trình hóa học độc hại và đắt đỏ. |  | Áo giáp chống đạn thông thường bị bắn vào để lại vết rách và tỏa khói đen ô nhiễm; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:43.2–00:52.1 (8.9s) | L430 | Nhưng tơ của Hagfish hoàn toàn có thể tự tổng hợp bằng vi khuẩn lên men sinh học, tạo ra các tấm giáp chống đạn nhẹ hơn một nửa, dai gấp 10 lần và hoàn toàn tự phân hủy sinh học trong môi trường tự |  | Mô hình áo giáp dệt từ tơ Hagfish siêu mỏng nhẹ nhưng chặn đứng viên đạn bay tới kêu cái keng, không hề thủng rách; KHÔNG có anh MC trong cảnh này. |
| b08 | 00:52.1–01:00.1 (8.1s) | L431 | nhiên! Hơn thế nữa, gel nhớt của Hagfish đang được nghiên cứu làm chất chữa cháy khẩn cấp cho các đám cháy giàn khoan dầu ngoài khơi nhờ khả năng ngậm nước cực lớn! |  | Bọt gel trắng xóa từ nhớt chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện dập tắt ngọn lửa bùng cháy dữ dội trên mô hình giàn khoan biển; KHÔNG có anh MC trong cảnh này. |
| b09 | 01:00.1–01:09.3 (9.2s) | L432 | Một giải pháp vật liệu xanh hoàn hảo cho tương lai quốc phòng và môi trường! Nhưng hãy nhìn sang Kỳ Nhông Axolotl với chiếc chìa khóa vàng của y học tái tạo mô người! |  | chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói bơi đến trước các bác sĩ phẫu thuật đang nghiên cứu mô tim và tủy sống; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:09.3–01:15.5 (6.2s) | L433 | Mỗi năm trên thế giới có hàng triệu bệnh nhân chịu cảnh tàn phế do đột quỵ tim hoặc chấn thương đứt tủy sống không thể phục hồi. |  | Hình ảnh bệnh nhân ngồi xe lăn nhìn về phía trước với ánh mắt hy vọng; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:15.5–01:20.5 (5.0s) | L434 | Các nhà nghiên cứu tại Viện Max Planck Đức đã phân lập được các yếu tố sinh trưởng tế bào mầm chi từ Axolotl! |  | Ống nghiệm phát sáng màu xanh lam chứa các phân tử protein kích hoạt mầm tái sinh tế bào; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:20.5–01:29.8 (9.3s) | L435 | Khi ứng dụng các tín hiệu phân tử này vào tế bào người, các nhà khoa học đã thành công trong việc kích thích tế bào cơ tim người tự phân chia bù đắp vào vùng mô tim bị hoại tử sau cơn nhồi máu! |  | Vùng mô tim hoại tử màu xám sẫm dần hồng hào trở lại, các mạch nước màu mới mọc ra nuôi tim đập khỏe mạnh; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:29.8–01:36.2 (6.4s) | L436 | Axolotl đang thắp lên hy vọng có thật về một ngày con người có thể tự mọc lại các ngón tay và chữa lành hoàn toàn các chấn thương cột sống! |  | Chú kỳ nhông chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói mỉm cười giơ bàn tay nhỏ bé chạm vào bàn tay một em bé đang bình phục; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:36.2–01:41.6 (5.4s) | L437 | Đây không còn là khoa học viễn tưởng, mà là lộ trình y học tái sinh có thể trở thành hiện thực trong vài thập kỷ tới! |  | Đồ họa cánh tay robot kết hợp tế bào sinh học mọc da thịt mềm mại tự nhiên; KHÔNG có anh MC trong cảnh này. |
| b15 | 01:41.6–01:46.0 (4.4s) | L438 | Và cuối cùng, chiếc ly thủy tinh nhỏ xíu của Sứa Bất Tử bay vút lên giữa trung tâm sân |  | chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực trôi lơ lửng giữa một quả cầu ánh sáng ba chiều mô phỏng tế bào gốc người; KHÔNG có anh MC trong cảnh này. |
| b16 | 01:46.0–01:54.9 (8.9s) | L439 | vận động! Căn bệnh đáng sợ nhất của nhân loại không phải là vi khuẩn hay virus, mà chính là sự thoái hóa và lão hóa không thể đảo ngược của các tế bào não trong bệnh Alzheimer và Parkinson! |  | Hình ảnh các tế bào thần kinh não người bị teo tóp và đứt gãy kết nối theo tuổi tác; KHÔNG có anh MC trong cảnh này. |
| b17 | 01:54.9–02:02.5 (7.6s) | L440 | Nhưng cơ chế chuyển biệt hóa tế bào của Sứa Bất Tử đã chứng minh một chân lý vĩ đại: tế bào hoàn toàn có thể được tái lập trình trở lại trạng thái non trẻ ban |  | Các tế bào thần kinh già nua được kích hoạt enzym sứa, tự hồi sinh và nối lại các khớp thần kinh phát sáng rực rỡ; KHÔNG có anh MC trong cảnh này. |
| b18 | 02:02.5–02:12.7 (10.2s) | L441 | đầu! Giải mã cơ chế telomerase của loài sứa 4,5mm này đang giúp các nhà khoa học mở ra kỷ nguyên mới của thuốc đảo ngược tuổi sinh học, trẻ hóa tế bào gốc và kéo dài tuổi thọ khỏe mạnh cho |  | Một cụ già hoạt hình uống giọt nước tinh chất sứa bỗng trẻ trung yêu đời, nụ cười rạng rỡ hạnh phúc; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:12.7–02:18.0 (5.3s) | L442 | loài người! Một giấc mơ trường thọ không bệnh tật mà nhân loại hằng khao khát suốt hàng 1.000 năm lịch sử! |  | Ánh sáng hồng tím của chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực lan tỏa bao bọc lấy toàn bộ sân vận động trong sự trầm trồ nghẹn ngào; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:18.0–02:27.5 (9.5s) | L443 | Và một món quà bất ngờ khác đến từ Kiến Nổ Cảm Tử: chất keo dính phenolic tiết ra từ cơ thể chúng đang được các nhà dược học nghiên cứu làm keo dán vết mổ nội tạng sinh học! |  | Bác sĩ phẫu thuật dùng một giọt gel sinh học lấy cảm hứng từ keo của chú Kiến Nổ dũng cảm bảo vệ tổ hoạt hình màu đỏ cam, đeo ba lô chứa chất lỏng vàng phát sáng, đội mũ bảo hộ chống độc, ánh mắt quả cảm kiên cường để dán vết rách mạch nước màu tim; KHÔNG có anh MC trong cảnh này. |
| b21 | 02:27.5–02:35.8 (8.3s) | L444 | Loại keo này có khả năng đông kết tức thì ngay trong môi trường ẩm ướt đầy máu, dính chặt vết mổ mà không gây độc hại và tự tiêu biến sau khi mô cơ lành lặn! |  | Vết mổ được dán kín hoàn hảo chỉ trong ba giây, không cần dùng chỉ khâu thông thường; KHÔNG có anh MC trong cảnh này. |
| b22 | 02:35.8–02:43.3 (7.6s) | L445 | Từ một hành động tự hủy bảo vệ tổ, thiên nhiên đã trao tặng cho y học loài người một phương pháp cầm máu phẫu thuật đột phá cứu sống hàng ngàn sinh mạng! |  | Hình ảnh bàn tay bác sĩ bắt tay với chú kiến chú Kiến Nổ dũng cảm bảo vệ tổ hoạt hình màu đỏ cam, đeo ba lô chứa chất lỏng vàng phát sáng, đội mũ bảo hộ chống độc, ánh mắt quả cảm kiên cường nhỏ bé đầy lòng tri ân; KHÔNG có anh MC trong cảnh này. |
| b23 | 02:43.3–02:48.8 (5.4s) | L446 | Chiếc mũi sao của Chuột Chũi Mũi Sao cũng đang truyền cảm hứng cho việc chế tạo các robot cứu hộ động đất thế hệ mới! |  | Mô hình robot cứu hộ mini trang bị 22 cánh xúc tu cảm biến cơ học tiến vào đống đổ nát cứu hộ; KHÔNG có anh MC trong cảnh này. |
| b24 | 02:48.8–02:59.3 (10.5s) | L447 | Trong môi trường khói bụi mù mịt và bóng tối sập đổ của các tòa nhà sau thảm họa, camera quang học hoàn toàn bị vô hiệu hóa, nhưng các xúc tu cảm biến Eimer có thể dò tìm thấy nhịp thở và sự sống của nạn nhân chỉ trong tích tắc! |  | Robot phát hiện tín hiệu sự sống của nạn nhân dưới đống gạch đá và phát tín hiệu cấp cứu giải cứu kịp thời; KHÔNG có anh MC trong cảnh này. |
| b25 | 02:59.3–03:04.9 (5.6s) | L448 | Một phát minh lấy cảm hứng từ sinh vật mù lòa đầm lầy đang cứu sống hàng 1.000 con người khỏi thảm họa thiên tai! |  | Hình ảnh chú chuột chũi chú Chuột Chũi Mũi Sao hoạt hình lông đen nhung mượt mà, mũi xòe ra 22 xúc tu đỏ hồng như bông hoa sao biển, đeo kính râm mù lòa nhưng phản xạ siêu thanh đeo kính râm bắt tay với người lính cứu hộ trong sự ấm áp; KHÔNG có anh MC trong cảnh này. |
| b26 | 03:04.9–03:12.1 (7.2s) | L449 | Hơn thế nữa, các nhà khoa học vật liệu tại Viện Công nghệ Massachusetts đang phát triển loại da nhân tạo thông minh mô phỏng cơ chế M-T-C của Hải Sâm! |  | Tấm da nhân tạo thông minh đổi từ mềm mại sang cứng cáp khi có dòng điện nhỏ chạy qua; KHÔNG có anh MC trong cảnh này. |
| b27 | 03:12.1–03:20.9 (8.8s) | L450 | Vật liệu này có thể dùng làm lớp vỏ ngoài cho robot mềm thám hiểm không gian: mềm dẻo để luồn lách qua các khe nứt thiên thạch nhưng lập tức cứng như thép khi cần khoan sâu vào lòng đất! |  | Robot thám hiểm vũ trụ hoạt hình luồn qua khe đá hẹp rồi khoan sâu lấy mẫu đất phát sáng; KHÔNG có anh MC trong cảnh này. |
| b28 | 03:20.9–03:26.2 (5.4s) | L451 | Trận chung kết diễn ra trong bầu không khí trang trọng và xúc động chưa từng có giữa ba đỉnh cao tiến hóa của tự nhiên! |  | Cả khán đài nín thở theo dõi ánh đèn rọi vào chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực, chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói và chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc b |
| b29 | 03:26.2–03:33.6 (7.4s) | L452 | Hải Ly đại diện cho sức mạnh kiến tạo làm thay đổi cả một vùng địa lý rộng lớn, mang lại sự trù phú và nước ngọt cho muôn loài sinh vật! |  | Hình ảnh đại ngàn xanh biếc với những hồ nước trong veo do chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo tạo dựng hiện lên hùng vĩ; KHÔNG có anh MC trong cảnh này. |
| b30 | 03:33.6–03:40.7 (7.1s) | L453 | Axolotl đại diện cho kỳ tích tái sinh thể xác phi thường, còn Sứa Bất Tử là biểu tượng bất diệt cho sự chiến thắng quy luật nghiệt ngã của thời gian! |  | Ba vầng hào quang vàng, xanh lam và hồng phấn tỏa sáng rực rỡ quanh ba tuyển thủ vĩ đại; KHÔNG có anh MC trong cảnh này. |
| b31 | 03:40.7–03:49.2 (8.5s) | L454 | Ban giám khảo đã hoàn tất việc chấm điểm Vòng Chung Kết! Huy chương Đồng hai điểm thuộc về cụ tổ Cá Mút Đá Hagfish với vật liệu tơ chống đạn sinh thái! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương đồng hai điểm cho chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện. |
| b32 | 03:49.2–03:55.4 (6.2s) | L455 | Huy chương Bạc bốn điểm thuộc về Kỳ Nhông Axolotl với cuộc cách mạng tái tạo mô tim và tủy sống con người! |  | chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói nhận tấm huy chương bạc bốn điểm, đưa tổng điểm của mình chạm mốc mười điểm tròn! |
| b33 | 03:55.4–04:02.9 (7.5s) | L456 | Và Huy chương Vàng sáu điểm tối cao của Vòng Chung Kết thuộc về Sứa Bất Tử với giấc mơ trẻ hóa tế bào và đảo ngược lão hóa cho toàn thể nhân loại! |  | chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực bay lên bục cao nhất đón nhận huy chương vàng sáu điểm khổng lồ trong ánh pháo hoa rực rỡ ngập trời! |
| b34 | 04:02.9–04:11.8 (8.9s) | L457 | Một màn lội ngược dòng không tưởng trong lịch sử Đại Hội Sinh Tồn! Tổng điểm của Sứa Bất Tử đã nhảy vọt lên con số 14 điểm, chính thức xô đổ mọi kỷ lục điểm số! |  | tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) bùng nổ hiệu ứng ánh sáng: Sứa Bất Tử 14 điểm, Axolotl 10 điểm, Hải Ly 8 điểm, Hagfish 8 điểm, Wombat 5 điểm, Hải Sâm 5 điểm, Chuột Chũi Sao 4 điểm, Bạch Tuộc Mimic 2 điểm, Ếch dị nhân móng vuốt hoạt hình đáng yêu 2 điểm, Kiến Nổ 1 điểm; toàn bộ khán trường vỡ òa sung sướng! |

### scene13 · LỄ BẾ MẠC & TRAO VƯƠNG MIỆN ĐẠI HỘI SINH TỒN MÙA 3 · 166.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.2 (9.2s) | L458 | Âm nhạc vinh quang rộn rã vang lên! Thưa toàn thể muôn loài muôn thú, chúng ta chính thức bước vào Lễ Bế Mạc và Trao Vương Miện Đại Hội Sinh Tồn Mùa ba! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vest đỏ tươi đứng trên bục danh dự giữa sân, tay cầm chiếc micro vàng lấp lánh; xung quanh là dàn pháo hoa kim tuyến bay rợp trời; tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng rực bảng tổng sắp. |
| b02 | 00:09.2–00:15.6 (6.4s) | L459 | Sau tám vòng thi đấu nghẹt thở với hàng loạt kỷ lục khoa học được thiết lập, bảng tổng sắp chung cuộc đã chính thức chốt hạ! |  | Màn hình lớn hiện bảng tổng sắp mười bậc thang vinh quang từ hạng mười đến ngôi vô địch; KHÔNG có anh MC trong cảnh này. |
| b03 | 00:15.6–00:22.1 (6.5s) | L460 | Mỗi tuyển thủ đều đã cống hiến hết mình, phô diễn những vũ khí sinh học và kỳ tích thích nghi làm rạng danh thế giới hoang dã! |  | Hình ảnh mười chiếc cúp lưu niệm phát sáng lấp lánh trên khay nhung đỏ; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:22.1–00:29.7 (7.6s) | L461 | Đồng hạng ba giành Huy chương Đồng chung cuộc của Mùa ba là hai tuyển thủ: kỹ sư Hải Ly và cụ tổ Cá Mút Đá Hagfish với tám điểm xuất sắc! |  | chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo và chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện cùng bước lên bục số ba, đeo tấm huy chương đồng chung cuộc nặng trĩu và mỉm cười bắt tay nhau; KHÔNG có anh MC trong cảnh |
| b05 | 00:29.7–00:36.7 (7.0s) | L462 | Ngôi vị Á quân giành Huy chương Bạc chung cuộc thuộc về thiên thần tái sinh của đất nước Mexico: Kỳ Nhông Axolotl với mười điểm tròn trĩnh! |  | chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói bước lên bục số hai, sáu nhánh mang hồng rung rinh xúc động, nụ cười ngây thơ đón nhận tấm huy chương bạc quý phái; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:36.7–00:41.7 (5.1s) | L463 | Và chiếc vương miện vàng nạm đá quý tối cao của Đại Hội Sinh Tồn Mùa ba... đã tìm thấy chủ nhân xứng |  | Một chùm ánh sáng laser vàng rực rọi thẳng vào chiếc vương miện đang hạ dần từ trên không trung; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:41.7–00:48.5 (6.7s) | L464 | đáng nhất! Kẻ từng bị các chuyên gia đánh giá là yếu ớt nhất, chỉ nặng 1 miligram và dài 4,5mm trong buổi lễ cân ký đo đạc đầu |  | Hình ảnh hồi tưởng lúc cân ký: chiếc ly thủy tinh nhỏ bé bị lãng quên bên cạnh cỗ xe tăng Wombat 35kg; KHÔNG có anh MC trong cảnh này. |
| b08 | 00:48.5–00:56.5 (8.0s) | L465 | tiên! Nhưng bằng năng lực đảo ngược dòng thời gian sinh học vô tận, sinh vật nhỏ bé này đã chứng minh cho toàn vũ trụ thấy: kích thước không bao giờ là giới hạn của sự sống! |  | chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực bay lơ lửng bước lên bục cao nhất số một, phát ra ánh hào quang hồng tím lung linh huyền ảo; KHÔNG có anh MC trong cảnh này. |
| b09 | 00:56.5–01:02.3 (5.8s) | L466 | Một thắng lợi của sự kiên trì, của sự dẻo dai và của phép màu tái sinh vô tận trong lòng đại dương sâu thẳm! |  | Toàn cảnh chú sứa nhỏ phát sáng giữa vòng vây của các đấu sĩ khổng lồ đang ngước nhìn thán phục; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:02.3–01:05.4 (3.1s) | L467 | Xin nhiệt liệt chúc mừng tân vương của Mùa ba: SỨA |  | Chiếc vương miện vàng nhỏ xíu vừa vặn được đặt nhẹ nhàng lên đỉnh chuông trong suốt của chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực, pháo hoa bùng nổ rực sáng cả bầu trời đêm; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:05.4–01:11.8 (6.4s) | L468 | BẤT TỬ! Khán đài hàng vạn muông thú đồng loạt đứng dậy hò reo vang dội, vẫy cờ hoa chúc mừng chiến thắng lịch sử của tân vương! |  | Toàn thể khán giả rừng già và đại dương cùng reo hò, ném mũ và hoa giấy chúc mừng; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng và bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ vỗ tay chúc mừng nồng nhiệt. |
| b12 | 01:11.8–01:20.0 (8.3s) | L469 | Dạ em cảm ơn toàn thể muôn loài đã ủng hộ em! Em xin hứa sẽ tiếp tục bơi lội bất tử thêm vài triệu năm nữa để bảo vệ sự sống hành tinh nha! |  | Cận cảnh chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực đội vương miện vàng, nhấp nháy phát sáng xúc động phát biểu; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:20.0–01:26.4 (6.4s) | L470 | Tất cả các tuyển thủ đều đã nhận được những chiếc cúp danh dự và huy chương tương xứng với những cống hiến khoa học phi thường của mình! |  | Toàn cảnh lễ trao giải rực rỡ, khay huy chương vàng bạc đồng lấp lánh trên bục vinh quang; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:26.4–01:36.8 (10.4s) | L471 | Anh chàng Wombat mỉm cười tự hào với tấm huy chương vàng Vòng một, kỹ sư Hải Ly rạng rỡ với ba tấm huy chương danh giá, và cụ tổ Hagfish uy nghi với giải thưởng cổ vật sống trường tồn! |  | chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường, chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo và chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt  |
| b15 | 01:36.8–01:45.7 (9.0s) | L472 | Nhưng đỉnh cao vinh quang và chiếc vương miện tối cao vẫn thuộc về chú sứa nhỏ 1 miligram: biểu tượng của sức sống mãnh liệt vượt lên trên mọi giới hạn vật chất! |  | Chiếc vương miện vàng nạm đá quý phát ánh hào quang lung linh trên đỉnh chuông trong suốt của chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực; KHÔNG có anh MC trong cảnh này. |
| b16 | 01:45.7–01:52.5 (6.8s) | L473 | Toàn thể mười tuyển thủ cùng bước lên bục vinh quang chung, quây quần bên chiếc cúp vàng danh giá của Đại Hội Sinh Tồn Mùa ba! |  | Mười tuyển thủ ôm vai nhau tươi cười rạng rỡ, pháo hoa nổ vang trời, khán đài tung hoa giấy rực rỡ; KHÔNG có anh MC trong cảnh này. |
| b17 | 01:52.5–02:00.7 (8.1s) | L474 | Chiếc máy ảnh toàn cảnh của ban tổ chức lóe sáng, ghi lại bức ảnh lịch sử của mười dị nhân vĩ đại nhất hành tinh trong sự hò reo không dứt của muôn loài! |  | Bức ảnh chụp chung toàn đoàn phát sáng khung vàng lưu niệm tuyệt đẹp giữa sân khấu tràn ngập niềm vui; KHÔNG có anh MC trong cảnh này. |
| b18 | 02:00.7–02:07.6 (6.9s) | L475 | Những tiếng hò reo vang dội khắp bốn bề đấu trường khi chiếc vương miện Mùa ba tỏa ánh sáng lộng lẫy trên đỉnh chuông sứa nhỏ bé! |  | Pháo hoa hình vòng lặp vô cực nổ tung trên bầu trời đêm rực rỡ, toàn thể muông thú vẫy cờ hoa chúc mừng tân vương; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:07.6–02:15.7 (8.2s) | L476 | Đó là một khoảnh khắc xúc động nhắc nhở muôn loài về sự kỳ diệu khôn cùng của tạo hóa, nơi sinh vật nhỏ bé nhất lại nắm giữ bí mật trường tồn vĩ đại nhất! |  | Chú sứa chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực phát sáng dịu dàng soi sáng nụ cười hạnh phúc của toàn bộ mười tuyển thủ; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:15.7–02:23.7 (7.9s) | L477 | Mỗi chiếc huy chương được trao hôm nay là sự ghi nhận xứng đáng cho hàng trăm triệu năm bền bỉ tiến hóa và thích nghi phi thường của thế giới tự nhiên! |  | Các tuyển thủ cùng bước lên bục danh dự, ôm nhau ăn mừng thắm thiết dưới mưa pháo hoa rực rỡ; KHÔNG có anh MC trong cảnh này. |
| b21 | 02:23.7–02:32.1 (8.4s) | L478 | Dù mang vẻ ngoài kỳ dị hay tập tính khác thường, mỗi sinh vật đều là một kiệt tác hoàn hảo của tạo hóa, mang trong mình những giá trị vô giá cho hành tinh! |  | Toàn cảnh mười dị nhân cùng nâng cúp và vẫy tay chào khán giả trong ánh sáng hoàng kim lộng lẫy; KHÔNG có anh MC trong cảnh này. |
| b22 | 02:32.1–02:41.2 (9.2s) | L479 | Mười tuyển thủ cùng bước lên sàn đấu chung, ôm lấy nhau trong tình thân ái muôn loài: không có ai là kẻ thua cuộc, tất cả đều là những kiệt tác tiến hóa vĩ đại của Trái Đất! |  | Mười tuyển thủ (Ếch dị nhân móng vuốt hoạt hình đáng yêu, Axolotl, Hải Sâm, Hagfish, Bạch Tuộc Mimic, Wombat, Chuột Chũi Mũi Sao, Kiến Nổ, Sứa Bất Tử, Hải Ly) đứng quây quần bên nhau giơ cúp vinh quang; KHÔNG có anh MC trong cảnh này. |
| b23 | 02:41.2–02:46.2 (4.9s) | L480 | Chiếc cúp Mùa ba đã tìm thấy chủ nhân, khép lại một mùa giải kịch tính nhất từ trước đến nay! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng giơ micro nở nụ cười rạng rỡ, toàn cảnh sân vận động bế mạc tràn ngập niềm vui và hạnh phúc; KHÔNG có anh MC trong cảnh này. |

### scene14 · BÀI HỌC BẢO TỒN, CÂU HỎI BÌNH LUẬN & HÉ LỘ MÙA 4 · 170.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:06.9 (6.9s) | L481 | Khi ánh đèn sân khấu dần dịu lại và tiếng reo hò lắng xuống, một thông điệp sâu sắc hơn bao giờ hết đang chờ đợi chúng ta lắng đọng... |  | Toàn cảnh đấu trường chuyển sang ánh sáng hoàng hôn ấm áp dịu nhẹ, mười tuyển thủ ngồi bên nhau ngắm nhìn bầu trời đêm; KHÔNG có anh MC trong cảnh này. |
| b02 | 00:06.9–00:12.9 (6.0s) | L482 | Mỗi loài sinh vật xuất hiện trong Mùa ba hôm nay đều là kết tinh của hàng trăm triệu năm thử nghiệm và chọn lọc tự nhiên khắc nghiệt. |  | Hình ảnh cây phả hệ tiến hóa phát sáng tỏa ra muôn nhánh sinh mệnh rực rỡ từ cội nguồn Trái Đất; KHÔNG có anh MC trong cảnh này. |
| b03 | 00:12.9–00:19.5 (6.6s) | L483 | Nhưng dù sở hữu những siêu năng lực bẻ gãy mọi quy luật sinh học, chúng vẫn vô cùng mong manh trước sự tàn phá môi trường do con người gây ra. |  | Bức tranh tương phản: một bên là dòng suối trong xanh của Axolotl, một bên là cống nước ô nhiễm và rác thải nhựa đe dọa; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:19.5–00:29.5 (10.0s) | L484 | Kỳ Nhông Axolotl dù có thể mọc lại cả não bộ và trái tim, nhưng chúng không thể tự tái tạo lại hồ nước Xochimilco đang bị ô nhiễm và thu hẹp từng ngày, đẩy chúng đến bờ vực tuyệt chủng ngoài tự nhiên! |  | Chú kỳ nhông chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói ngồi buồn bã nhìn vào vũng nước cạn dần giữa lòng thành phố; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:29.5–00:37.6 (8.1s) | L485 | Sứa Bất Tử có thể đảo ngược chu trình già nua vô tận, nhưng chúng vẫn tan rã bất lực trước những vùng biển ngập tràn hạt vi nhựa và hiện tượng axit hóa đại dương! |  | chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực trôi dạt giữa những túi nilon và hạt vi nhựa lơ lửng trong làn nước biển sẫm màu; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:37.6–00:45.9 (8.2s) | L486 | Bảo vệ những sinh vật dị thường này không chỉ là bảo vệ tự nhiên hoang dã, mà chính là bảo vệ kho báu tri thức vô giá cho tương lai y học và sự tồn vong của chính loài người chúng |  | Bàn tay con người nhẹ nhàng nâng niu giọt nước chứa chú sứa nhỏ và nhành cây xanh của chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:45.9–00:53.6 (7.7s) | L487 | ta! Chúng ta không thể học được bí quyết tái tạo mô tim từ Axolotl hay đảo ngược lão hóa từ Sứa nếu để chúng biến mất vĩnh viễn khỏi hành tinh này! |  | Hình ảnh Trái Đất xanh tươi được bao bọc trong vòng tay bảo vệ của con người và muôn thú; KHÔNG có anh MC trong cảnh này. |
| b08 | 00:53.6–01:00.0 (6.4s) | L488 | Và trước khi khép lại tập đặc biệt Mùa ba, anh MC xin gửi tới toàn thể quý vị khán giả một câu hỏi giao lưu đầy |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vest đỏ tươi bước ra phía trước màn hình, nở nụ cười ấm áp giơ micro về phía người xem; KHÔNG có anh MC trong cảnh này. |
| b09 | 01:00.0–01:13.2 (13.2s) | L489 | thú vị: Nếu được chọn sở hữu một siêu năng lực của mười quái kiệt Mùa ba: tái sinh không sẹo của Axolotl, mông bọc thép của Wombat, đớp mồi 0,12 giây của Chuột Chũi, hay khả năng đảo ngược thời gian của Sứa Bất Tử, bạn sẽ chọn năng lực nào? |  | Bốn khung hình hoạt hình vui nhộn hiện lên quanh anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng tượng trưng cho 4 siêu năng lực dị nhân; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:13.2–01:19.0 (5.8s) | L490 | Hãy chia sẻ suy nghĩ và bình luận của bạn ngay bên dưới video này để cùng bàn luận với cộng đồng yêu thiên nhiên nhé! |  | Biểu tượng khung bình luận hoạt hình nhấp nháy phát sáng rực rỡ; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:19.0–01:28.7 (9.7s) | L491 | Và đừng quên nhấn nút Đăng ký kênh Vẽ Chuyện Hoang Dã ngay hôm nay để không bỏ lỡ tập 31: Chim Cắt Lớn Peregrine Falcon — sát thủ bầu trời bổ nhào với vận tốc 390 km/h một giờ xé gió săn mồi! |  | Cửa hầm mở ra hé lộ bóng đen chú chim cắt lao vút xuống như tên lửa siêu thanh trên bầu trời mây trắng; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:28.7–01:37.6 (8.9s) | L492 | Cùng với đó là sự khởi động của Đại Hội Sinh Tồn Mùa bốn trong tương lai, nơi các dũng sĩ săn mồi đỉnh chóp như Cá Voi Sát Thủ Orca, Quạ Đen thiên tài và Chó Sói Xám sẽ chính thức tuyên chiến! |  | Các bóng đen dũng mãnh của Cá Voi Sát Thủ Orca, Quạ Đen đội mũ thám tử và Chó Sói hú dưới trăng hiện lên đầy uy lực; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:37.6–01:45.0 (7.4s) | L493 | Hành trình Mùa ba khép lại nhưng những bài học về tình yêu thiên nhiên và sự trân trọng từng sự sống nhỏ bé sẽ còn đọng lại mãi trong trái tim chúng |  | Bầu trời đêm trên đấu trường bừng sáng bởi muôn vì sao lấp lánh, mười tuyển thủ cùng ngước nhìn về tương lai xanh; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:45.0–01:53.2 (8.2s) | L494 | ta. Mỗi dòng suối mát lành, mỗi rạn san hô rực rỡ và mỗi cánh rừng nguyên sinh đều là ngôi nhà chung thiêng liêng mà con người và muôn thú cùng chia |  | Bức tranh Trái Đất xanh ngắt tươi đẹp, biển cả trong lành và rừng xanh bát ngát trải dài vô tận; KHÔNG có anh MC trong cảnh này. |
| b15 | 01:53.2–01:59.0 (5.8s) | L495 | sẻ. Chúng ta hãy cùng nhau chung tay gìn giữ và bảo vệ những kỳ quan sinh học vô giá này trước khi quá muộn! |  | Biểu tượng bàn tay con người kết nối với dấu chân muông thú tạo thành vòng tròn bảo vệ bền vững; KHÔNG có anh MC trong cảnh này. |
| b16 | 01:59.0–02:10.2 (11.1s) | L496 | Mỗi hành động nhỏ bé của chúng ta hôm nay: tiết kiệm một giọt nước sạch, giảm bớt một chiếc túi nilon thải ra đại dương, hay trồng thêm một mầm cây xanh nơi góc phố đều là sự tiếp sức cho sự trường tồn của muôn loài! |  | Hình ảnh em bé tưới mầm cây non xanh tốt, dòng suối mát lành chảy uốn lượn qua khu rừng bình yên; KHÔNG có anh MC trong cảnh này. |
| b17 | 02:10.2–02:15.9 (5.7s) | L497 | Hãy cùng kênh Vẽ Chuyện Hoang Dã lan tỏa tình yêu thiên nhiên và lòng trân trọng sự sống đến mọi người xung quanh bạn nhé! |  | Biểu tượng trái tim xanh phát sáng kết nối hàng triệu người xem trên toàn cầu cùng chung tay bảo vệ môi trường; KHÔNG có anh MC trong cảnh này. |
| b18 | 02:15.9–02:24.8 (9.0s) | L498 | Những thông điệp yêu thương và bài học bảo tồn thiên nhiên sâu sắc của Đại Hội Sinh Tồn Mùa ba sẽ tiếp tục lan tỏa, thắp sáng niềm hy vọng cho một Trái Đất xanh tươi muôn màu muôn vẻ! |  | Toàn cảnh Trái Đất quay chậm rãi trong không gian, được bao bọc bởi tình yêu thương và sự chở che của con người và muôn loài; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:24.8–02:30.0 (5.2s) | L499 | Một cuộc chạm trán nảy lửa trên không trung và đại dương bao la đang đón chờ quý vị khán giả thân yêu! |  | Dòng chữ hẹn gặp lại ở Mùa bốn bừng sáng trên nền trời đầy sao; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:30.0–02:37.2 (7.2s) | L500 | Bảo vệ những loài sinh vật kỳ diệu này chính là bảo vệ kho tàng tri thức sinh học vô giá mà thiên nhiên đã dày công tích lũy qua hàng ngàn triệu năm! |  | Bàn tay con người nâng niu giọt nước trong vắt chứa chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực và mầm cây xanh của chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo; KHÔNG có anh MC trong cảnh này. |
| b21 | 02:37.2–02:44.0 (6.8s) | L501 | Nếu để mất đi dù chỉ một mắt xích nhỏ bé, nhân loại có thể vĩnh viễn đánh mất những chìa khóa y học quý báu không bao giờ tìm lại được! |  | Mạng lưới sự sống tỏa sáng bao bọc lấy hành tinh xanh, biểu tượng của sự hòa hợp vĩnh cửu giữa con người và thiên nhiên; KHÔNG có anh MC trong cảnh này. |
| b22 | 02:44.0–02:50.9 (6.8s) | L502 | Xin chào tạm biệt, xin cảm ơn toàn thể quý vị đã đồng hành, và hẹn gặp lại tất cả trong những chuyến phiêu lưu hoang dã tiếp theo! |  | Toàn thể mười tuyển thủ cùng anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng và bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ vẫy tay chào tạm biệt khán giả trong tiếng pháo hoa rực rỡ bế mạc; KHÔNG có anh MC trong cảnh này. |

## 5. Phân cảnh Shorts — từng beat

Banner: **ĐẠI HỘI SINH TỒN #3 / 10 DỊ NHÂN ĐẠI CHIẾN!** · giọng 53.0s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Mười dị nhân mới. Tám vòng đấu sinh tử. Một chiếc vương |  |
| s02 | 00:02.6 | S02 | miện tối cao! Gấu Wombat 35kg và Hải Ly răng sắt được đặt cược sẽ thắng. Còn Sứa Bất Tử 1 miligram... chuyên gia bảo tham gia cho vui! |  |
| s03 | 00:09.6 | S03 | Vòng một: Cá Mút Đá Hagfish sở hữu sợi tơ nhớt bền gấp 10 lần tơ nhện và dai hơn sợi Kevlar! | **GẤP 10 LẦN** · Bền hơn tơ nhện · R/640 · [0.54, 0.52] |
| s04 | 00:14.4 | S04 | Vòng hai: Chuột Chũi Mũi Sao đớp mồi trong 0,12 giây và ngửi mùi dưới nước bằng bong | **0,12 GIÂY** · Ăn nhanh nhất quả đất · L/620 · [0.58, 0.28] |
| s05 | 00:18.4 | S05 | bóng khí! Vòng ba: Kỳ Nhông Axolotl sở hữu bộ gen 32 tỷ cặp base tái sinh não tim mà không để lại | **32 TỶ BASE** · Gen tái sinh không sẹo · R/600 · [0.48, 0.72] |
| s06 | 00:23.2 | S06 | sẹo! Vòng bốn: Đập nước Hải Ly tạo vùng ngập nước kỳ diệu ngăn chặn bão lửa và hạn hán cả |  |
| s07 | 00:26.9 | S07 | thung lũng! Vòng năm: Hải Sâm lầy lội tiêu hóa 130 tấn trầm tích mỗi năm để bảo vệ rạn san hô! | **130 TẤN** · Lọc sạch trầm tích · L/610 · [0.52, 0.35] |
| s08 | 00:31.5 | S08 | Vòng sáu: Bạch Tuộc Mimic 9 bộ não biến hình 15 loài kịch độc chỉ trong 200 mili-giây! |  |
| s09 | 00:35.5 | S09 | Chung kết: ai mang lại công nghệ vĩ đại nhất cho loài người? Y học tái tạo mô của Axolotl hay gen telomere bất tử của Sứa? |  |
| s10 | 00:42.2 | S10 | Và tân vương Mùa ba là... sinh vật tí hon 1 miligram từng bị xem là mồi ngon dưới đáy |  |
| s11 | 00:46.1 | S11 | biển! Bạn có đồng ý không? Xem trọn tám vòng đấu kịch tính trong video dài nhé, |  |
| s12 | 00:49.4 | S12 | vì ở đây có mười dị nhân mới, tám vòng đấu sinh tử, và một chiếc vương miện tối cao! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Màn đêm buông xuống một đấu trường cổ kính được bao quanh bởi những rạn san hô phát quang và rừng rậm nguyên sinh bí ẩn...". Bố cục: Toàn cảnh đấu trường hoạt hình khổng lồ nửa trên cạn nửa dưới nước chìm trong màn sương đêm kỳ bí, mười chiếc bục tròn phát sáng bao quanh một bục vinh quang trung tâm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Ở chính giữa sàn đấu, một chiếc vương miện hoàng gia nạm ngọc phát ra ánh sáng lung linh kỳ ảo, chờ đợi chủ nhân mới của Mùa ba.". Bố cục: Cận cảnh chiếc vương miện nạm ngọc lấp lánh xoay tròn trên bệ đá cẩm thạch giữa sân khấu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Đêm nay, mười sinh vật dị thường nhất từ Tập 21 đến Tập 30 của kênh Vẽ Chuyện Hoang Dã sẽ chính thức hội ngộ!". Bố cục: Mười chiếc bóng đen bí ẩn của 10 con vật (Ếch dị nhân móng vuốt hoạt hình đáng yêu, Axolotl, Hải Sâm, Cá Mút Đá, Bạch Tuộc Mimic, Wombat, Chuột Chũi Mũi Sao, Kiến Nổ, Sứa Bất Tử, Hải Ly) xuất hiện tại cửa hầm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Họ không đến để nhắc lại những câu chuyện cũ, mà để đọ sức trực tiếp bằng hàng loạt bí mật sinh học chấn động thế giới!". Bố cục: Mười đôi mắt hoạt hình rực sáng trong bóng tối với đủ phong thái: ngầu lạnh lùng, ngây thơ, lầy lội, bí hiểm và kiên cường; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Mỗi loài mang theo một siêu năng lực quái dị dường như bước ra từ những trang truyện tranh siêu anh hùng viễn tưởng.". Bố cục: Những biểu tượng siêu năng lực phát sáng lơ lửng quanh cửa hầm: vuốt xương bọc thép, nhánh tái sinh, tơ nhớt siêu bền, vòng lặp vô cực và con đập gỗ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Từ khả năng mọc lại cả não bộ và trái tim không tì vết, tấm khiên mông bọc thép dập nát sọ kẻ thù, cho tới bộ gen đảo ngược dòng thời gian để trường sinh bất lão!". Bố cục: Hình vẽ minh họa 4 siêu năng lực tỏa sáng trên màn hình lớn: trái tim tự liền sẹo, mông bọc giáp titan, tơ nhớt bẫy cá mập và vòng lặp vô cực; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Bật toàn bộ hệ thống đèn pha! Chào mừng toàn thể muôn loài đã đến với Đại Hội Sinh Tồn Mùa ba: Đấu Trường Dị Nhân!". Bố cục: Dàn đèn pha công suất lớn rọi sáng rực rỡ toàn bộ đấu trường, pháo hoa nổ tung trên bầu trời đêm; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vest đỏ tươi giơ micro vàng nở nụ cười rạng rỡ.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tôi là người dẫn chương trình đêm nay, và tôi xin cam kết danh dự: những phát hiện khoa học bạn sắp nghe đều mới toanh 100%!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đặt tay lên ngực cam kết, phía sau là màn hình lớn chiếu biểu tượng các tạp chí khoa học uy tín Nature, Science và PNAS (không chữ).
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Từ việc tơ nhớt Cá Mút Đá dai hơn áo giáp chống đạn, Kỳ Nhông Axolotl mang bộ gen 32 tỷ cặp base chống ung thư, cho đến Sứa Bất Tử tự đảo ngược thời gian tế bào!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng nháy mắt hóm hỉnh, tay kia giơ tập tài liệu dày cộm có hình chuỗi xoắn DNA và bánh răng cơ khí; khán đài thú rừng reo hò náo nhiệt.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Đại hội không tổ chức chỉ để so kè nắm đấm, mà là nơi tôn vinh những kỳ tích thích nghi đỉnh cao mà mẹ thiên nhiên đã dày công kiến tạo suốt hàng trăm triệu năm qua!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng giơ micro lên cao, pháo sáng hình vương miện lấp lánh trên không trung; khán giả muôn loài vẫy cờ hoa rộn ràng.
```
</details>

<details><summary>L100</summary>

```text
HÌNH L100 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Điều gì sẽ xảy ra khi một sinh vật già cỗi, bị bỏ đói hoặc chịu tổn thương thể xác nghiêm trọng? Thông thường cái chết sẽ là điểm kết thúc.". Bố cục: Hình ảnh đồng hồ cát chảy xuống giọt cát cuối cùng tượng trưng cho vòng đời sinh học hữu hạn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L101</summary>

```text
HÌNH L101 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nhưng với Sứa Bất Tử, chúng kích hoạt một tiến trình sinh học kỳ diệu gọi là chuyển biệt hóa tế bào: toàn bộ các tế bào chuông sứa tự phân giải và chuyển hóa ngược!". Bố cục: Chuông sứa co rút lại thành một khối mô tròn nhỏ màu hồng tím không biệt hóa; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L102</summary>

```text
HÌNH L102 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khối mô này chìm xuống đáy biển, tự biến đổi trở lại thành một quần thể polyp sơ sinh hoàn toàn non trẻ, rồi từ đó lại nảy chồi sinh ra hàng trăm chú sứa con mới!". Bố cục: Từ khối mô mọc lên các chồi polyp như rễ cây non, rồi bung nở thành đàn sứa con bơi lượn tự do; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L103</summary>

```text
HÌNH L103 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chu trình này có thể lặp đi lặp lại vô tận mà không bị giới hạn bởi tuổi già sinh học, biến chúng thành sinh vật duy nhất trên Trái Đất nắm giữ chìa khóa bất tử thực thụ!". Bố cục: Biểu tượng vòng lặp vô cực phát sáng rực rỡ lồng vào hình dáng của chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L104</summary>

```text
HÌNH L104 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Giống như một người già 80 tuổi khi cảm thấy mệt mỏi có thể tự biến ngược thành một đứa bé sơ sinh trong nôi rồi lớn lên tiếp tục cuộc đời mới! Một quyền năng làm đảo lộn hoàn toàn định luật sinh học!". Bố cục: Hình minh họa hài hước: ông cụ râu tóc bạc phơ bước vào cánh cửa ma thuật biến ra thành em bé bụ bẫm cười toe toét; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L105</summary>

```text
HÌNH L105 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Đến lượt bậc thầy lầy lội dưới đáy đại dương bước ra: Hải Sâm!". Bố cục: chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù trườn tới mép bể thi đấu, toàn thân da cam bóng lưỡng không hề có một mẩu xương cứng nào; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L106</summary>

```text
HÌNH L106 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khi bị một con cua biển khổng lồ kẹp chặt, Hải Sâm không bỏ chạy mà sử dụng chiêu thức tống xuất bên trong cơ thể kinh hoàng qua đường phần đuôi!". Bố cục: Mô hình cua biển lao vào cắn, chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù quay đuôi lại phóng ra một chùm sợi trắng xóa dính nhớt như mạng nhện bủa vây cua; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L107</summary>

```text
HÌNH L107 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Đó là chùm ống Cuvier chứa đầy chất keo độc tố dính chặt khiến kẻ săn mồi tê liệt, trong khi Hải Sâm ung dung trườn đi thoát nạn!". Bố cục: Con cua bị dính chặt hai càng không cử động được, chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù thong thả trườn đi với chiếc quạt giấy xua đuổi ruồi muỗi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L108</summary>

```text
HÌNH L108 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và điều không tưởng là chỉ sau năm tuần lễ, Hải Sâm sẽ tự nuôi dưỡng và mọc lại nguyên vẹn một hệ tiêu hóa và buồng phổi nước hoàn toàn mới toanh!". Bố cục: Bên trong cơ thể chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù, bộ ruột mới mọc dần từ thành mô và hoạt động trơn tru sau 5 tuần lễ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L109</summary>

```text
HÌNH L109 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chưa hết, các nhà sinh học tại đại học Bỉ còn phát hiện: loài cá ngọc trai tí hon Carapidae thường xuyên bơi chui vào tận sâu bên trong phần đuôi của Hải Sâm để làm tổ trú ẩn an toàn!". Bố cục: Chú cá ngọc trai nhỏ bơi lượn chui đầu vào phần đuôi chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù như chui vào khách sạn ngầm, chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù chỉ biết thở dài cam chịu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Luật thi đấu Mùa ba cực kỳ cam go: tám vòng đấu chính thức, xen kẽ giờ giải lao hậu trường, trao giải phụ và vòng phúc khảo tin đồn thế kỷ.". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) hiện lên giữa sân với 8 ô thử thách: vũ khí tự thân, tái sinh thoát hiểm, phản xạ giác quan, công trình địa hình, bộ gen đột biến, bảo vệ sinh thái, cụ tổ cổ đại và món quà nhân loại.
```
</details>

<details><summary>L110</summary>

```text
HÌNH L110 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Một chiếc khách sạn đáy biển kỳ quái nhất hành tinh khiến cả đấu trường cười nghiêng ngả!". Bố cục: Khán giả ôm bụng cười ngặt nghẽo trước cảnh tượng bi hài của chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng lau nước mắt vì cười quá nhiều.
```
</details>

<details><summary>L111</summary>

```text
HÌNH L111 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và cuối cùng là màn ảo thuật biến hóa thần tốc của Bạch Tuộc Mimic!". Bố cục: chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình bơi ra giữa sân cát đáy biển, toàn thân sọc nâu trắng chuyển động nhịp nhàng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L112</summary>

```text
HÌNH L112 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Không cần ẩn nấp dưới cát, Bạch Tuộc Mimic sở hữu các túi sắc tố và hệ cơ papillae vi mô có thể thay đổi màu sắc và kết cấu bề mặt da chỉ trong 200 mili-giây!". Bố cục: Cận cảnh lớp da của chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình: từ trơn nhẵn biến thành sần sùi gai nhọn chỉ trong chớp mắt 200 mili-giây; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L113</summary>

```text
HÌNH L113 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tùy theo kẻ thù đang đối diện là ai, chúng có thể tự điều khiển tám xúc tu để giả dạng thành 15 loài kịch độc khác nhau: từ rắn biển sọc đen, cá sư tử xòe gai độc, cá bơn ẩn mình, đến cả sứa biển trôi nổi!". Bố cục: Bốn khung hình biến hóa liên tiếp: chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình hóa thành rắn biển đầu đen, cá sư tử gai góc, cá bơn dẹt và sứa biển bơi lượn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L114</summary>

```text
HÌNH L114 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Một năng lực ngụy trang động đạt đỉnh cao của trí tuệ đại dương! Kẻ thù nhìn vào chỉ thấy một bãi mìn sinh học đầy gai độc chết người chứ không hề nhận ra chú bạch tuộc đang cười thầm bên trong!". Bố cục: chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình nháy mắt hóm hỉnh khoe tài biến hình khiến con cá săn mồi hoảng sợ bơi lui; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L115</summary>

```text
HÌNH L115 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nói về khả năng chịu đựng và thoát hiểm, Ếch dị nhân móng vuốt hoạt hình đáng yêu cũng sở hữu một cơ chế bảo vệ mối nối gân vô cùng kỳ lạ!". Bố cục: chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng ngồi trên bệ đá, các khớp ngón chân sau được chiếu tia laser phóng đại; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L116</summary>

```text
HÌNH L116 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khác với các loài động vật có móng vuốt cố định, đầu mút xương ngón chân của ếch được giữ chặt bởi một khối mô collagen dạng sợi đàn hồi cực cao!". Bố cục: Phóng to đầu ngón chân: khối mô collagen ôm trọn lấy đốt xương nhọn như chiếc bao da tự nhiên; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L117</summary>

```text
HÌNH L117 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khi áp lực co cơ vượt qua ngưỡng chịu đựng, khối mô này tự đứt ra có kiểm soát, giải phóng móng xương đâm ra ngoài mà không làm rách các mạch nước màu chính!". Bố cục: Xương ngón chân phóng ra ngoài trong khi các mạch nước màu lớn uốn lượn né sang hai bên an toàn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L118</summary>

```text
HÌNH L118 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Điều này giải thích vì sao vết thương sau đó tự hàn gắn rất nhanh mà ếch không hề bị mất nước màu quá nhiều!". Bố cục: Đồ họa dòng nước màu lưu thông êm ả nuôi dưỡng vết rách mau lành; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L119</summary>

```text
HÌNH L119 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và tại sao chú cá ngọc trai sống trong phần đuôi Hải Sâm cả tuần mà không hề bị ngạt thở hay chết chìm?". Bố cục: Hình ảnh hiển vi soi vào buồng phổi nước bên trong phần đuôi của chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Mỗi vòng thi, ban giám khảo sẽ trao ba tấm huy chương: Vàng được ba điểm, Bạc hai điểm, và Đồng một điểm. Riêng Vòng Chung Kết sẽ được nhân đôi điểm số!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ ngồi ở bàn giám khảo trên cao gõ búa gỗ, trước mặt là khay nhung đỏ bày ba chiếc huy chương vàng, bạc, đồng sáng loáng.
```
</details>

<details><summary>L120</summary>

```text
HÌNH L120 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Bởi vì Hải Sâm hô hấp bằng cách liên tục hút và xả hàng lít nước biển giàu oxy qua phần đuôi vào hai nhánh phổi nước, biến nơi này thành một phòng khách sạn có điều hòa nhiệt độ và bình oxy tươi mới quanh năm!". Bố cục: Dòng nước biển trong vắt giàu oxy liên tục tuần hoàn qua cơ thể chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù, chú cá nhỏ ngửa bụng bơi lội sảng khoái; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L121</summary>

```text
HÌNH L121 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và ngay cả khi đối mặt với những cơn lũ quét ngập úng bất ngờ dưới lòng đất, Gấu Wombat cũng sở hữu bản lĩnh sinh tồn kỳ diệu để bảo toàn tính mạng!". Bố cục: Sa bàn mặt đất với dòng nước lũ tràn vào miệng hang ngầm sâu của chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L122</summary>

```text
HÌNH L122 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khi nước lũ dâng ngập các cửa hang chính, Wombat không hề hoảng loạn mà bình tĩnh di chuyển lên các ngách hang cao hơn được thiết kế theo hình chữ U ngược!". Bố cục: Mặt cắt hang ngầm: ngách hang chữ U giữ lại một túi khí oxy khổng lồ giúp chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường ngồi khô ráo an toàn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L123</summary>

```text
HÌNH L123 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Những túi khí tự nhiên này giúp chúng sống sót ngon lành dưới lòng đất suốt nhiều ngày liền chờ cho đến khi nước lũ rút hoàn toàn!". Bố cục: chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường ung dung ngồi trong túi khí hang ngầm nhai cỏ khô dự trữ, bên ngoài dòng nước lũ chảy xiết vô hại; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L124</summary>

```text
HÌNH L124 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Không chỉ có khả năng mọc lại chi và bên trong cơ thể, Kỳ Nhông Axolotl còn có thể tái tạo hoàn chỉnh tế bào võng mạc mắt và thấu kính quang học tinh khiết!". Bố cục: Nhãn cầu của chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói phát sáng trong suốt, các tế bào thụ cảm thị giác tự sắp xếp ngay ngắn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L125</summary>

```text
HÌNH L125 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khi bị tổn thương thị giác, các tế bào sắc tố biểu mô mống mắt tự động chuyển hóa thành tế bào gốc phôi thai để dệt lại một thấu kính mắt mới toanh không hề có vết mờ đục!". Bố cục: Thấu kính mắt trong veo như giọt pha lê phản chiếu ánh sáng rực rỡ, chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói chớp mắt nhìn rõ mồn một; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L126</summary>

```text
HÌNH L126 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Còn Hải Sâm thì sở hữu khả năng tái tạo tế bào tuyến sinh dục và mô bài tiết chỉ trong vòng vài tuần lễ sau các cuộc giải phẫu tự thân khốc liệt!". Bố cục: Các cơ quan sinh học bên trong chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù tự nảy mầm và hoàn thiện trơn tru như một phép màu tự nhiên; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L127</summary>

```text
HÌNH L127 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Điều kinh ngạc nhất là hệ thống tái sinh của Hải Sâm được kích hoạt bởi các phân tử tín hiệu hóa học peptide vô cùng đặc biệt!". Bố cục: Kính hiển vi hiển thị các chuỗi phân tử peptide tín hiệu tỏa ra từ mô tổn thương của chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù kích thích tế bào gốc phân chia; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L128</summary>

```text
HÌNH L128 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chỉ trong vòng 24 giờ sau khi tự phóng bên trong cơ thể, các tế bào gốc biểu mô ruột đã kết tụ thành mầm mô tạng non trẻ khỏe mạnh!". Bố cục: Mô phỏng mầm ruột non màu hồng nhạt hình thành dọc theo khoang cơ thể chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L129</summary>

```text
HÌNH L129 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Kết quả Vòng hai của ban giám khảo: Huy chương Đồng thuộc về Bạch Tuộc Mimic với màn biến hình 15 loài kịch độc!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ búa, trao huy chương đồng phát sáng cho chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khắp các khán đài, muông thú từ khắp năm châu bốn biển đang giương cao những biểu ngữ cổ vũ vô cùng huyên náo và hài hước!". Bố cục: Khán đài hoạt hình rực rỡ cờ hoa, đàn gấu trúc vác băng rôn vẽ hình chiếc vương miện, bầy chim cánh cụt mặc áo phông cổ vũ nhiệt tình; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L130</summary>

```text
HÌNH L130 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Huy chương Bạc thuộc về Kỳ Nhông Axolotl với bộ nhớ tái sinh mô hoàn hảo không sẹo!". Bố cục: chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói mỉm cười nhận tấm huy chương bạc đeo quanh cổ rạng rỡ.
```
</details>

<details><summary>L131</summary>

```text
HÌNH L131 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và Huy chương Vàng ba điểm xuất sắc thuộc về tuyển thủ bé hạt tiêu Sứa Bất Tử với vòng lặp đảo ngược thời gian tế bào vô cực!". Bố cục: chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực nhận huy chương vàng lơ lửng, cả đấu trường reo hò rực rỡ pháo hoa.
```
</details>

<details><summary>L132</summary>

```text
HÌNH L132 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Bảng điểm sau hai vòng thi đấu đảo chiều ngoạn mục: Wombat và Sứa Bất Tử cùng chia sẻ ngôi đầu với ba điểm, Hagfish và Axolotl bám sát với hai điểm!". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) cập nhật điểm số: Wombat 3, Sứa Bất Tử 3, Hagfish 2, Axolotl 2, Hải Ly 1, Bạch Tuộc Mimic 1; cuộc đua vương miện ngày càng nóng bỏng!
```
</details>

<details><summary>L133</summary>

```text
HÌNH L133 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Đấu trường lại rực lửa! Chào mừng quý vị đến với Vòng ba: Phản Xạ Siêu Tốc và Những Giác Quan Kỳ Dị Vượt Trội!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vung tay kích hoạt hệ thống đồng hồ bấm giờ kỹ thuật số tốc độ cao trên trần nhà; tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng ô thử thách số ba mang hình tia chớp và xúc tu.
```
</details>

<details><summary>L134</summary>

```text
HÌNH L134 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nếu bạn nghĩ mắt là cửa sổ tâm hồn duy nhất để quan sát thế giới, thì các tuyển thủ Vòng ba sẽ khiến bạn phải suy nghĩ lại từ đầu!". Bố cục: Màn hình chiếu biểu tượng sóng âm, xung xúc giác và các bong bóng khí dò tìm mục tiêu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L135</summary>

```text
HÌNH L135 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Ở thế giới bóng tối dưới lòng đất hay đáy biển sâu đục ngầu, thị giác thông thường hoàn toàn trở nên vô dụng, nhường chỗ cho những giác quan cơ học và sóng âm tinh vi nhất!". Bố cục: Đồ họa bóng tối bao trùm, các tia quét rada sinh học tỏa ra từ mũi và xúc tu của các tuyển thủ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L136</summary>

```text
HÌNH L136 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tiến vào đường hầm thử nghiệm bóng tối: sát thủ săn mồi đầm lầy Bắc Mỹ, Chuột Chũi Mũi Sao!". Bố cục: chú Chuột Chũi Mũi Sao hoạt hình lông đen nhung mượt mà, mũi xòe ra 22 xúc tu đỏ hồng như bông hoa sao biển, đeo kính râm mù lòa nhưng phản xạ siêu thanh đeo kính râm đen ngầu, bước vào căn phòng tối tăm phủ đầy bùn ẩm, hai mươi hai chiếc xúc tu đỏ hồng trên mũi xòe rộng rung rinh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L137</summary>

```text
HÌNH L137 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Mặc dù đôi mắt bị thoái hóa gần như mù lòa, chiếc mũi chứa 25.000 cơ quan thụ cảm của Chuột Chũi Mũi Sao lại là cơ quan xúc giác nhạy bén nhất từng được ghi nhận trong lịch sử khoa học!". Bố cục: Hình ảnh giải phẫu hiển vi chiếc mũi: hai mươi hai xúc tu hồng chứa hai mươi lăm ngàn cơ quan Eimer siêu nhỏ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L138</summary>

```text
HÌNH L138 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "25.000 cơ quan Eimer này chứa mạng lưới dây thần kinh cảm giác dày đặc đến mức: hơn 50% diện tích vỏ não của chú chuột chũi này chỉ dùng để giải mã tín hiệu từ chiếc mũi sao!". Bố cục: Đồ họa bán cầu não bộ hoạt hình: một nửa bán cầu não phát sáng màu vàng rực rỡ tương ứng với hình dạng chiếc mũi sao 22 cánh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L139</summary>

```text
HÌNH L139 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và khi một ấu trùng côn trùng xuất hiện, chiếc đồng hồ đếm mili-giây của ban tổ chức bắt đầu đếm ngược!". Bố cục: Một chú ấu trùng nhỏ rơi xuống mặt bùn phát ra tín hiệu rung động vi mô; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Đội cổ động viên rái cá biển vừa gõ sò vừa reo hò, trong khi các bạn chồn Gulo ngồi ở hàng ghế danh dự chăm chú theo dõi từng động thái của mười dị nhân!". Bố cục: Đàn rái cá biển gõ hai vỏ sò vào nhau kêu canh cách vui nhộn, các chú chồn Gulo đeo kính râm vỗ tay phấn khích; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L140</summary>

```text
HÌNH L140 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chạm! Nhận diện! Nuốt chửng! Toàn bộ tiến trình chỉ diễn ra trong đúng 0,12 giây đồng hồ! Nhanh hơn một cái chớp mắt của con người tới ba lần!". Bố cục: Chuột Chũi chú Chuột Chũi Mũi Sao hoạt hình lông đen nhung mượt mà, mũi xòe ra 22 xúc tu đỏ hồng như bông hoa sao biển, đeo kính râm mù lòa nhưng phản xạ siêu thanh lao tới đớp gọn ấu trùng, đồng hồ dừng ở con số 0,12 giây, đạt kỷ lục Guiness thế giới hoạt hình; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L141</summary>

```text
HÌNH L141 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chưa hết, giáo sư Kenneth Catania tại đại học Vanderbilt còn phát hiện một tuyệt kỹ không tưởng: Chuột Chũi Mũi Sao có thể ngửi được mùi thức ăn dưới nước!". Bố cục: chú Chuột Chũi Mũi Sao hoạt hình lông đen nhung mượt mà, mũi xòe ra 22 xúc tu đỏ hồng như bông hoa sao biển, đeo kính râm mù lòa nhưng phản xạ siêu thanh lặn dưới làn nước trong, chiếc mũi thổi ra hai quả bong bóng khí tròn xoe chạm vào con mồi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L142</summary>

```text
HÌNH L142 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Bằng cách liên tục thổi các bong bóng khí từ lỗ mũi chạm vào vật thể rồi hít ngược bong bóng trở lại xoang mũi, chúng thu gom các phân tử mùi lơ lửng trong nước để ngửi chính xác tuyệt đối!". Bố cục: Bong bóng khí hút ngược lại mũi, các thụ thể khứu giác phát sáng tín hiệu thức ăn ngon lành; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L143</summary>

```text
HÌNH L143 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Động vật có vú duy nhất trên Trái Đất có thể hít thở và ngửi mùi thức ăn trong môi trường ngập nước mà không hề bị sặc!". Bố cục: chú Chuột Chũi Mũi Sao hoạt hình lông đen nhung mượt mà, mũi xòe ra 22 xúc tu đỏ hồng như bông hoa sao biển, đeo kính râm mù lòa nhưng phản xạ siêu thanh giơ ngón tay cái tự tin dưới nước, bọt khí lấp lánh quanh mũi sao rực rỡ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L144</summary>

```text
HÌNH L144 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Động vật có vú đầu tiên trên thế giới ngửi được mùi khi đang ngụp lặn dưới nước! Một tràng pháo tay cho Chuột Chũi Mũi Sao!". Bố cục: Khán đài vỗ tay rào rào kinh ngạc trước pha trình diễn ảo diệu; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng giơ micro tròn mắt ngỡ ngàng.
```
</details>

<details><summary>L145</summary>

```text
HÌNH L145 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nhưng đối thủ của chú ta, Bạch Tuộc Mimic, lập tức bước lên với hệ thần kinh phân tán dị thường bậc nhất đại dương!". Bố cục: chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình bơi lượn trong bể kính, tám chiếc xúc tu múa lượn tự do theo các quỹ đạo độc lập hoàn toàn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L146</summary>

```text
HÌNH L146 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Các nhà khoa học thần kinh phát hiện: 2/3 tổng số nơ-ron não bộ của bạch tuộc không hề nằm ở hộp sọ trung tâm, mà trải dài dọc theo tám xúc tu!". Bố cục: Sơ đồ thần kinh phát sáng: não trung tâm nhỏ, trong khi 8 xúc tu tỏa sáng rực rỡ với hàng triệu nơ-ron hoạt động độc lập; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L147</summary>

```text
HÌNH L147 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Điều này có nghĩa là mỗi xúc tu của Bạch Tuộc Mimic giống như một bộ não thu nhỏ: có thể tự nếm vị giác qua các giác hút, tự sờ chạm, tự suy nghĩ và giải quyết chướng ngại vật mà không cần chờ lệnh từ não bộ!". Bố cục: Một xúc tu mở nắp chai, một xúc tu thò vào hốc đá bắt cua, một xúc tu khác tự uốn éo xua đuổi cá nhỏ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L148</summary>

```text
HÌNH L148 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khi bị săn đuổi, tám xúc tu có thể tự động phối hợp điều phối các bước chạy mà não trung tâm chỉ cần tập trung tính toán đường thoát hiểm!". Bố cục: chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình uốn 8 xúc tu thoăn thoắt vượt qua mê cung đá ngầm cực kỳ mượt mà; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L149</summary>

```text
HÌNH L149 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Mỗi xúc tu vừa là cánh tay, vừa là con mắt xúc giác, vừa là chiếc lưỡi nếm vị thức ăn! Một mạng lưới trí tuệ phân tán siêu việt!". Bố cục: Đồ họa phóng to giác hút trên xúc tu chứa các thụ thể hóa học phát sáng khi nếm chất hữu cơ trong nước; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Hải Ly thậm chí còn ngứa răng cắn nhẹ vào chân chiếc bàn ban tổ chức làm bà Cú giám khảo phải vội vàng lấy thước gõ can ngăn!". Bố cục: chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo đang định há miệng gặm góc bàn cẩm thạch, bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ cầm thước gỗ gõ nhẹ lên trán Hải Ly làm chú ta rụt cổ cười trừ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L150</summary>

```text
HÌNH L150 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Đến lượt Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu thể hiện giác quan thích nghi dòng suối chảy xiết!". Bố cục: chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng ngồi dưới dòng thác nước nhân tạo đổ ào ào; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L151</summary>

```text
HÌNH L151 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Lớp lông tơ kỳ lạ ở hai bên hông của ếch đực chứa đầy mạng lưới mao mạch nước màu và các tế bào thụ cảm cơ học vi mô!". Bố cục: Phóng to các sợi lông tơ bên hông: các mao mạch nước màu đỏ li ti đan xen với các sợi thần kinh thụ cảm dòng chảy; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L152</summary>

```text
HÌNH L152 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khi ngồi dưới đáy suối đục ngầu cuồn cuộn bùn cát, lớp lông này vừa hấp thụ oxy hòa tan trong nước, vừa cảm nhận được sự thay đổi áp suất dòng chảy nhỏ nhất từ kẻ săn mồi bơi qua!". Bố cục: Dòng nước cuộn sóng mang các đường xung áp suất chạm vào lông tơ, chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng né tránh cú đớp của cá dữ trong gang tấc; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L153</summary>

```text
HÌNH L153 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và kỹ sư Hải Ly cũng sở hữu đôi mắt bơi lặn siêu việt: lớp mí mắt thứ ba trong suốt hoạt động như chiếc kính bơi chuyên nghiệp, giúp chúng quan sát rõ mồn một từng cành cây dưới đáy sông đục ngầu!". Bố cục: Cận cảnh mắt của chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo: mí mắt thứ ba khép lại như màng kính bảo hộ trong suốt, van tai và mũi tự động đóng kín; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L154</summary>

```text
HÌNH L154 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Cá Mút Đá Hagfish dù sống dưới đáy biển tăm tối 1.000m và mắt thoái hóa hoàn toàn thành vệt sắc tố dưới da, nhưng chúng sở hữu chiếc mũi thính nhạy số một đại dương!". Bố cục: chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện bơi trong làn nước đen thẳm, một lỗ mũi duy nhất trên đỉnh đầu mở rộng hút nước biển; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L155</summary>

```text
HÌNH L155 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khác với mọi loài cá có hai lỗ mũi, Hagfish chỉ có một lỗ mũi duy nhất dẫn thẳng nước biển vào một túi khứu giác khổng lồ kết nối trực tiếp với thùy khứu giác của não bộ!". Bố cục: Cắt lớp đầu Hagfish: luồng nước biển mang phân tử mùi đi thẳng vào túi khứu giác phát sáng tín hiệu thần kinh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L156</summary>

```text
HÌNH L156 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chúng có thể đánh hơi thấy mùi một xác cá voi chìm cách xa hàng chục cây số giữa đại dương bao la, rồi bơi thẳng tới đích mà không cần đến một tia sáng nào!". Bố cục: Các đường sóng khứu giác dẫn đường cho đàn chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện bơi xuyên qua bóng đêm đại dương tìm tới xác cá voi chính xác tuyệt đối; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L157</summary>

```text
HÌNH L157 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Còn Kiến Nổ dũng cảm bảo vệ tổ thì sở hữu cặp râu cảm biến hóa học phát hiện tín hiệu pheromone xâm nhập chỉ trong 50 mili-giây!". Bố cục: Cặp râu của chú Kiến Nổ dũng cảm bảo vệ tổ hoạt hình màu đỏ cam, đeo ba lô chứa chất lỏng vàng phát sáng, đội mũ bảo hộ chống độc, ánh mắt quả cảm kiên cường rung rinh bắt trọn từng phân tử mùi lạ trong không khí báo động toàn tổ kiến; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L158</summary>

```text
HÌNH L158 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chẳng có một tên gián điệp hay kẻ săn mồi nào có thể lén lút tiếp cận cửa tổ mà không bị cặp râu siêu nhạy này lật tẩy!". Bố cục: Chú kiến gác cửa lập tức vào vị trí sẵn sàng chiến đấu trước khi kẻ thù kịp nhìn thấy lối vào; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L159</summary>

```text
HÌNH L159 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Không chỉ có đôi mắt mí thứ ba, Hải Ly còn sở hữu hệ thống cảnh báo sớm bằng sóng âm mặt nước vô cùng lợi hại!". Bố cục: chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo nổi trên mặt hồ phẳng lặng, chiếc đuôi dẹt to bản giơ cao chuẩn bị đập nước; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Còn anh chàng Wombat thì tranh thủ tựa chiếc mông bọc thép 3cm vào cây cột thép chịu lực để ngủ gật một giấc ngắn trước giờ khai chiến!". Bố cục: chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường đứng dựa mông vào cột thép ngáy khò khò ngon lành, miệng mỉm cười như đang mơ thấy cánh đồng cỏ tươi xanh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L160</summary>

```text
HÌNH L160 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Mỗi khi phát hiện bóng dáng kẻ săn mồi như chó sói hay gấu xám từ xa, Hải Ly dùng chiếc đuôi dẹt nặng nề đập cực mạnh xuống mặt nước tạo nên tiếng nổ rầm vang dội khắp thung lũng!". Bố cục: Chiếc đuôi đập mạnh xuống nước tung bọt trắng xóa, âm thanh phát ra to như tiếng súng nổ vang xa cả cây số; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L161</summary>

```text
HÌNH L161 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Âm thanh đập đuôi này truyền đi cả trong không khí lẫn dưới đáy nước, cảnh báo cho toàn bộ bầy đàn lặn sâu xuống đáy bùn trốn thoát chỉ trong 3 giây!". Bố cục: Đàn hải ly con lập tức lặn ngụp biến mất dưới dòng nước sâu mát lạnh an toàn tuyệt đối; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L162</summary>

```text
HÌNH L162 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Để phối hợp nhịp nhàng giữa 22 xúc tu, não bộ của Chuột Chũi Mũi Sao xử lý các xung thần kinh cảm giác với tốc độ nhanh gấp 10 lần dây thần kinh mắt người!". Bố cục: Các tia sáng xung thần kinh chạy dọc từ 22 xúc tu về trung tâm vỏ não với tốc độ ánh sáng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L163</summary>

```text
HÌNH L163 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Mỗi khi xúc tu chạm nhẹ vào một vật thể lạ, bộ não phân tích lập tức cấu trúc vật liệu, độ ẩm, độ nhớt và nhiệt độ của đối tượng trong vòng vài phần nghìn giây!". Bố cục: Màn hình hiển thị bảng phân tích phổ vật liệu chi tiết hiện ra trong nháy mắt khi chiếc mũi chạm nhẹ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L164</summary>

```text
HÌNH L164 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Đó là lý do vì sao chúng có thể phân biệt chính xác đâu là thức ăn bổ dưỡng và đâu là hạt cát vô giá trị trong nháy mắt mà không bao giờ nuốt nhầm!". Bố cục: chú Chuột Chũi Mũi Sao hoạt hình lông đen nhung mượt mà, mũi xòe ra 22 xúc tu đỏ hồng như bông hoa sao biển, đeo kính râm mù lòa nhưng phản xạ siêu thanh nhổ hạt sỏi ra ngoài và nuốt trọn chú giun đất béo ngậy một cách điêu luyện; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L165</summary>

```text
HÌNH L165 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Các nhà khoa học tại đại học Vanderbilt phát hiện: vùng vỏ não cảm giác của Chuột Chũi Mũi Sao dành tới 50% diện tích chỉ để xử lý tín hiệu từ chiếc mũi!". Bố cục: Đồ họa bản đồ não bộ hiển thị một nửa bán cầu não phát sáng rực rỡ để giải mã xúc giác của 22 xúc tu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L166</summary>

```text
HÌNH L166 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Độ phân giải xúc giác trên chiếc mũi này chi tiết và sắc nét đến mức tương đương với độ nhạy thị giác của mắt đại bàng trên bầu trời!". Bố cục: Hình ảnh so sánh chiếc mũi sao phóng to như một ống kính hiển vi điện tử siêu phân giải dò tìm từng hạt phân tử; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L167</summary>

```text
HÌNH L167 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nhờ đó, dù sống cả đời trong lòng đất đen đặc chẳng hề có tia sáng, Chuột Chũi Mũi Sao vẫn nhìn thấy thế giới bằng xúc giác với độ chân thực đến kinh ngạc!". Bố cục: Mô hình 3D đường hầm tối đen bỗng bừng sáng các đường vân địa hình khi chú Chuột Chũi Mũi Sao hoạt hình lông đen nhung mượt mà, mũi xòe ra 22 xúc tu đỏ hồng như bông hoa sao biển, đeo kính râm mù lòa nhưng phản xạ siêu thanh quét nhẹ xúc tu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L168</summary>

```text
HÌNH L168 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Ban giám khảo xin công bố điểm số Vòng ba! Huy chương Đồng thuộc về Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu với bộ lông tơ thụ cảm áp suất dòng suối!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ búa, trao huy chương đồng phát sáng cho chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng.
```
</details>

<details><summary>L169</summary>

```text
HÌNH L169 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Huy chương Bạc thuộc về Bạch Tuộc Mimic với tám xúc tu mang trí tuệ nơ-ron độc lập phi thường!". Bố cục: chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình dùng một xúc tu đón lấy tấm huy chương bạc lấp lánh rồi đeo lên cổ.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Giám khảo xin nhắc nhở nghiêm túc: nghiêm cấm phóng ruột vào mặt đối thủ, cấm xả nhớt làm trơn sàn thi đấu và cấm nổ bụng lung tung trong khu vực khán đài!". Bố cục: Cận cảnh bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ cúi đầu nhìn qua gọng kính tròn, vẻ mặt nghiêm nghị đưa cánh ra lệnh chỉ đạo.
```
</details>

<details><summary>L170</summary>

```text
HÌNH L170 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và Huy chương Vàng ba điểm xuất sắc thuộc về Chuột Chũi Mũi Sao với kỷ lục săn mồi 0,12 giây cùng tuyệt chiêu ngửi mùi dưới nước bằng bong bóng khí!". Bố cục: chú Chuột Chũi Mũi Sao hoạt hình lông đen nhung mượt mà, mũi xòe ra 22 xúc tu đỏ hồng như bông hoa sao biển, đeo kính râm mù lòa nhưng phản xạ siêu thanh đứng trên bục vinh quang nhận huy chương vàng, 22 xúc tu đỏ hồng nhấp nháy ăn mừng kiêu hãnh.
```
</details>

<details><summary>L171</summary>

```text
HÌNH L171 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Cục diện bảng tổng sắp sau ba vòng đấu vô cùng gay cấn: Wombat, Sứa Bất Tử và Chuột Chũi Mũi Sao cùng nắm giữ ba điểm! Đấu trường ngày càng kịch tính nghẹt thở!". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) cập nhật: Wombat 3, Sứa Bất Tử 3, Chuột Chũi Sao 3, Bạch Tuộc Mimic 2, Hagfish 2, Axolotl 2, Hải Ly 1, Ếch dị nhân móng vuốt hoạt hình đáng yêu 1; khoảng cách điểm số sít sao chưa từng thấy!
```
</details>

<details><summary>L172</summary>

```text
HÌNH L172 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Sau ba vòng thi đấu căng như dây đàn, ban tổ chức xin thông báo: toàn thể đấu trường bước vào 30 phút giải lao hậu trường!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng lau mồ hôi trên trán, đưa tay ra hiệu tiếng chuông nghỉ giải lao ngân vang rộn rã; tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) hiện chữ giải lao hoạt hình.
```
</details>

<details><summary>L173</summary>

```text
HÌNH L173 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Các tuyển thủ tạm lui về khu vực phòng thay đồ để nạp năng lượng và chuẩn bị cho các vòng đấu khốc liệt tiếp theo.". Bố cục: Hành lang phòng thay đồ hoạt hình với mười cánh cửa gắn bảng tên mười con vật; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L174</summary>

```text
HÌNH L174 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nhưng ngay lúc này, camera giấu kín của ban tổ chức đã ghi lại hàng loạt khoảnh khắc dở khóc dở cười khiến bà Cú giám khảo suýt ngất xỉu!". Bố cục: Màn hình hậu trường sáng lên, bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ đeo kính tròn cầm đèn pin đi kiểm tra an ninh từng phòng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L175</summary>

```text
HÌNH L175 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Ở phòng nghỉ số một của kỹ sư Hải Ly: bồn rửa mặt của ban tổ chức bị rò rỉ nước, phát ra tiếng róc rách nho nhỏ!". Bố cục: Vòi nước trong phòng rửa tay chảy róc rách từng giọt xuống bồn sứ trắng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L176</summary>

```text
HÌNH L176 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Một nghiên cứu của giáo sư Dietrich Müller-Schwarze đã chứng minh: Hải Ly bị một chứng ám ảnh cưỡng chế sinh học cực nặng với tiếng nước chảy!". Bố cục: chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo đang ôm đầu bứt tai, đôi mắt mở to hoảng hốt trước âm thanh nước chảy; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L177</summary>

```text
HÌNH L177 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chúng không hề bận tâm xem nước chảy ở đâu, chỉ cần nghe thấy tiếng róc rách là bản năng lập tức ra lệnh: phải đắp đập bịt kín ngay tức khắc!". Bố cục: chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo vớ lấy thảm lau chân, xà phòng, khăn tắm và bùn đất trát kín mít chiếc bồn rửa mặt thành một con đập cao ngất ngưởng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L178</summary>

```text
HÌNH L178 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Thậm chí khi chiếc loa thông báo của anh MC phát ra tiếng nhạc nền suối reo, Hải Ly đã phi ra vác nguyên một khúc gỗ to đùng chèn cứng họng loa!". Bố cục: chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo nhét khúc gỗ vào loa phóng thanh trần nhà, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng dưới ngơ ngác không nói nên lời; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L179</summary>

```text
HÌNH L179 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Các nhân viên hậu đài phải mất nửa tiếng đồng hồ dùng búa nhổ đinh để cạy con đập mini trong nhà vệ sinh của Hải Ly ra ngoài!". Bố cục: Hai kỹ thuật viên toát mồ hôi hì hục dọn bùn đất và cành cây khỏi bồn rửa mặt trong sự bất lực; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Các tuyển thủ đã nghe rõ chưa? Nhất là anh chàng Hải Sâm và bạn Kiến Nổ đang lén lút nhìn quanh đằng kia!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng liếc nhìn sang chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù và chú Kiến Nổ dũng cảm bảo vệ tổ hoạt hình màu đỏ cam, đeo ba lô chứa chất lỏng vàng phát sáng, đội mũ bảo hộ chống độc, ánh mắt quả cảm kiên cường đang giả vờ gãi đầu cười trừ ngây thơ vô số tội.
```
</details>

<details><summary>L180</summary>

```text
HÌNH L180 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Trong khi đó, ở khu vực phòng chờ của Ếch dị nhân móng vuốt hoạt hình đáng yêu và Kỳ Nhông Axolotl, một cuộc tranh luận nảy lửa của hai đại diện lưỡng cư đang nổ ra!". Bố cục: chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng và chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói ngồi đối diện nhau qua chiếc bàn kính, hai bên vung tay vung chân tranh cãi sôi nổi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L181</summary>

```text
HÌNH L181 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Ếch dị nhân móng vuốt hoạt hình đáng yêu khoe móng xương bảo: Bẻ xương làm vuốt mới là đỉnh cao chiến binh ngầu lòi!". Bố cục: chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng giơ ngón chân có vuốt xương trắng muốt nhọn hoắt khoe dáng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L182</summary>

```text
HÌNH L182 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Kỳ Nhông Axolotl mỉm cười lắc đầu đáp lại: Tự làm đau mình làm chi anh ơi, cứ để đối thủ cắn một miếng rồi mình mọc lại cái mới xinh xắn có phải nhàn nhã hơn không!". Bố cục: chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói xòe nhánh mang hồng rung rinh cười tít mắt, khiến Ếch dị nhân móng vuốt hoạt hình đáng yêu gãi đầu cạn lời; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L183</summary>

```text
HÌNH L183 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Còn ở góc phòng khách, chú Bạch Tuộc Mimic đang rảnh rỗi trổ tài biến hình thành một chiếc gối ôm sofa bằng nhung nâu sọc trắng!". Bố cục: Chiếc ghế sofa phòng khách bỗng có một chiếc gối ôm mềm mại sọc vằn nâu trắng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L184</summary>

```text
HÌNH L184 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Bà Cú giám khảo bước vào mệt mỏi định ngồi phịch xuống nghỉ lưng, thì chiếc gối ôm bỗng thò ra tám cái xúc tu ôm chầm lấy bà Cú làm bà thét lên một tiếng kinh hoàng!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ giật bắn mình nhảy dựng lên trần nhà, chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình hiện nguyên hình cười khanh khách xin lỗi rối rít; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L185</summary>

```text
HÌNH L185 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Dạ em chỉ muốn thử xem khả năng ngụy trang của em có lừa được mắt cú vọ của giám khảo không thôi mà!". Bố cục: chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình gãi đầu bối rối thu xúc tu lại ngoan ngoãn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L186</summary>

```text
HÌNH L186 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Ở một góc sân khác, Kỳ Nhông Axolotl đang tận hưởng dịch vụ tắm bùn khoáng nóng do ban tổ chức chu cấp với vẻ mặt thỏa mãn vô cùng!". Bố cục: chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói ngâm mình trong bồn bùn khoáng sủi bọt ấm áp, hai tay nhỏ đặt lên mép bồn thư giãn tuyệt đối; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L187</summary>

```text
HÌNH L187 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chú kỳ nhông cười tít mắt bảo: Đấu trường sinh tồn gì mà sướng như đi nghỉ dưỡng năm sao thế này, em muốn ở đây thi đấu quanh năm luôn quá!". Bố cục: chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói đắp hai lát dưa leo lên mắt thư giãn, xung quanh là bong bóng xà phòng bay lơ lửng ngộ nghĩnh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L188</summary>

```text
HÌNH L188 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Trong khi đó, anh chàng Ếch dị nhân móng vuốt hoạt hình đáng yêu đang miệt mài ngồi mài lại bộ móng vuốt xương vào mép bàn đá cẩm thạch kêu ken két nghe rợn cả người!". Bố cục: chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng ngồi co chân sau tỉ mỉ mài sắc từng chiếc vuốt xương trắng muốt, ánh mắt lóe lên tia sáng quyết tâm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L189</summary>

```text
HÌNH L189 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Thậm chí chú cá ngọc trai Carapidae trong phần đuôi Hải Sâm còn gọi thêm cả đàn bạn bè bơi vào tổ chức một buổi hòa nhạc mini dưới nước!". Bố cục: Ba chú cá ngọc trai nhỏ đeo kính râm cầm nhạc cụ mini chơi nhạc trong bụng chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù, làm chú ta run rẩy lắc lư cười ra nước mắt; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và bây giờ, xin mời toàn thể khán đài cùng đứng dậy nhiệt liệt hoan nghênh mười quái kiệt bước ra thảm đỏ danh dự!". Bố cục: Cửa hầm mở toang, ánh đèn flash chớp sáng liên hồi, khói lạnh cuồn cuộn thổi qua lối đi chính; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L190</summary>

```text
HÌNH L190 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Hải Sâm bèn thử gồng các cơ co thắt để tống cổ đàn khách trọ ồn ào ra ngoài, nhưng đàn cá ngọc trai lại tưởng đó là dịch vụ mát-xa thủy lực miễn phí nên càng khoái chí nằm im!". Bố cục: chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù thở dài ngao ngán phẩy quạt giấy, mặt biểu cảm bất lực tột cùng khiến cả hội trường cười nghiêng ngả; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L191</summary>

```text
HÌNH L191 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Thí sinh Hải Ly! Tôi cấm anh biến phòng vệ sinh của ban giám khảo thành công trường xây dựng thủy điện nhé!". Bố cục: Cận cảnh bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ chống hai cánh ngang hông, mặt đỏ bừng gắt gỏng chỉ vào bãi chiến trường đắp đập.
```
</details>

<details><summary>L192</summary>

```text
HÌNH L192 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Bà Cú giám khảo vừa bước sang phòng số hai của Gấu Wombat thì lại đụng phải một cảnh tượng kỳ quặc không kém!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ hé cửa nhìn vào phòng số hai, ánh mắt mở to đầy nghi hoặc; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L193</summary>

```text
HÌNH L193 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Anh chàng Wombat đang thong thả ngồi trên bồn cầu, chăm chú xếp từng khối phân hình lập phương thành một kim tự tháp vuông vức cực kỳ nghệ thuật!". Bố cục: chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường ngồi nghiêm túc xếp từng viên phân hình khối lập phương sắc cạnh như những viên gạch xếp hình Lego; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L194</summary>

```text
HÌNH L194 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tại sao phân của Wombat lại có hình lập phương độc nhất vô nhị trên thế giới? Nghiên cứu đoạt giải Ig Nobel vật lý của tiến sĩ Patricia Yang đã giải mã bí ẩn này!". Bố cục: Sơ đồ giải phẫu đường ruột hoạt hình: phần ruột già dài dằng dặc, đoạn cuối cùng sáng lên; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L195</summary>

```text
HÌNH L195 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chỉ có 8% đoạn ruột già cuối cùng của Wombat sở hữu cấu trúc mô cơ đàn hồi không đồng đều: hai rãnh cơ cứng chắc và hai rãnh cơ mềm dẻo!". Bố cục: Đồ họa ruột già ép phân: các vách cơ co bóp nén chất thải thành các cạnh góc vuông chín mươi độ hoàn hảo; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L196</summary>

```text
HÌNH L196 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Mỗi ngày, Wombat đúc ra từ 80 đến 100 viên phân lập phương sắc cạnh như xúc xắc để đánh dấu lãnh thổ trên các tảng đá mà không sợ bị lăn xuống dốc!". Bố cục: chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường giơ ngón tay cái tự hào chỉ vào kim tự tháp 100 viên gạch vuông vức không hề lăn lóc; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L197</summary>

```text
HÌNH L197 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khả năng đúc hình học chuẩn xác tới mức các nhà sản xuất gạch xây dựng của con người cũng phải trầm trồ xin bí quyết học hỏi!". Bố cục: Kỹ sư xây dựng hoạt hình cầm thước đo góc 90 độ của viên phân vuông vức thán phục; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L198</summary>

```text
HÌNH L198 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Dạ thưa cô giám khảo, em vừa đúc xong mẻ mới nóng hổi tặng ban tổ chức làm kỷ niệm nè cô!". Bố cục: chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường bê khay phân vuông vức chìa ra mời mọc với vẻ mặt chân chất thật thà; bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ bịt mũi lùi lại ba bước; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L199</summary>

```text
HÌNH L199 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Sang đến phòng của Kiến Nổ dũng cảm bảo vệ tổ, không khí lại căng thẳng như một kho thuốc súng sắp nổ!". Bố cục: chú Kiến Nổ dũng cảm bảo vệ tổ hoạt hình màu đỏ cam, đeo ba lô chứa chất lỏng vàng phát sáng, đội mũ bảo hộ chống độc, ánh mắt quả cảm kiên cường ngồi thiền trên chiếc nệm bông mềm, hai tay chắp trước ngực hít thở sâu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tuyển thủ số một! Chiến binh móng vuốt Tây Phi tự bẻ xương ngón chân xuyên thủng da chân để nghênh chiến! Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu!". Bố cục: chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng bước ra thảm đỏ, hai bên sườn phủ lớp lông tơ nâu sậm, đầu ngón chân sau xòe ra những móng vuốt xương nhọn hoắt cực ngầu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L200</summary>

```text
HÌNH L200 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chú kiến nhỏ nơm nớp lo sợ ai đó vô tình vỗ mạnh vào vai làm vỡ tuyến keo dính trên bụng, tạo bong bóng dính ba lô độc tố màu vàng sáng rực!". Bố cục: Đồ họa tia sét cảnh báo quanh ba lô keo dính của chú Kiến Nổ dũng cảm bảo vệ tổ hoạt hình màu đỏ cam, đeo ba lô chứa chất lỏng vàng phát sáng, đội mũ bảo hộ chống độc, ánh mắt quả cảm kiên cường, mỗi cử động nhỏ đều phải thật nhẹ nhàng rón rén; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L201</summary>

```text
HÌNH L201 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Còn ở góc bể nước của Hải Sâm, một chú cá ngọc trai Carapidae vừa chui tọt vào phần đuôi của Hải Sâm để ngủ trưa rồi thò đầu ra ngoài ngáp một cái thật dài!". Bố cục: Chú cá ngọc trai thò đầu ra khỏi đuôi chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù ngáp ngủ, chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù cầm quạt giấy phẩy lia lịa mặt méo xệch; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L202</summary>

```text
HÌNH L202 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chú cá này thậm chí còn rủ thêm hai người bạn cá ngọc trai khác vào cùng trú ngụ, biến cơ thể Hải Sâm thành một căn hộ chung cư mini dưới nước!". Bố cục: Ba chú cá ngọc trai nhỏ thò đầu ra vẫy đuôi trong sự ngao ngán của chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L203</summary>

```text
HÌNH L203 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Cứu em với anh MC ơi! Tên khách trọ này ở ké cả tuần nay không trả một xu tiền phòng mà còn ngáy to quá làm em mất ngủ!". Bố cục: Cận cảnh chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù giơ quạt giấy khóc mếu máo kêu cứu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L204</summary>

```text
HÌNH L204 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và đỉnh điểm khó đỡ: anh MC vừa cầm ly nước chanh lên định uống một ngụm giải khát thì phát hiện Sứa Bất Tử đang tung tăng bơi lội bên trong!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng há hốc miệng dừng ly nước chanh ngay trước môi, bên trong ly chú sứa chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực nhỏ xíu đang nháy mắt cười toe toét; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L205</summary>

```text
HÌNH L205 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "May mà chưa nuốt chửng tân vương tiềm năng của Mùa ba!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng thở phào nhẹ nhõm dùng thìa vớt chú sứa cẩn thận thả lại vào bể thi đấu an toàn.
```
</details>

<details><summary>L206</summary>

```text
HÌNH L206 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Dưới kính hiển vi điện tử, da của Bạch Tuộc Mimic là một màn hình chấm lượng tử sinh học với hàng triệu tế bào sắc tố chromatophore và iridophore!". Bố cục: Phóng to bề mặt da chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình: hàng triệu tế bào sắc tố co giãn nhịp nhàng như các điểm ảnh O-L-E-D siêu nét; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L207</summary>

```text
HÌNH L207 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Mỗi tế bào sắc tố được điều khiển bởi một sợi dây thần kinh riêng biệt, cho phép chúng thay đổi màu sắc và kết cấu bề mặt da chỉ trong 200 mili-giây!". Bố cục: Đồ họa các xung thần kinh kích hoạt tế bào sắc tố đổi từ màu cát vàng sang vân vằn rắn biển trong chớp mắt; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L208</summary>

```text
HÌNH L208 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Trong khi đó, Sứa Bất Tử cũng tận dụng thời gian nghỉ giữa hiệp để kích hoạt quá trình tái lập trình nơ-ron thần kinh vô cùng kỳ diệu!". Bố cục: chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực phát quang lung linh trong bể nước, các tế bào gốc phân chia và tái cấu trúc mạng lưới thần kinh non trẻ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L209</summary>

```text
HÌNH L209 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Cơ thể sứa tí hon này không bao giờ biết mệt mỏi, bởi mỗi khi căng thẳng, chúng chỉ việc đảo ngược tế bào để trở lại trạng thái thanh xuân sung mãn!". Bố cục: Đồ họa đồng hồ sinh học của chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực quay ngược về vạch số 0, cơ thể trong veo không tì vết; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tuyển thủ số hai! Đại sứ tái sinh của hồ nước ngọt Mexico có thể mọc lại cả trái tim và não bộ không vết sẹo! Kỳ Nhông Axolotl!". Bố cục: chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói bơi lượn trong bồn nước ngọt trong suốt, sáu nhánh mang hồng xòe rộng như cánh hoa, nụ cười ngây thơ đốn tim khán giả; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L210</summary>

```text
HÌNH L210 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Không khí phòng nghỉ ngơi của Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu thì tràn ngập tiếng gầm gừ tập luyện cơ bắp cuồn cuộn!". Bố cục: chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng hít đất bằng hai chi trước, gân cốt cơ bắp nổi rõ từng múi dưới lớp lông tơ rậm rạp; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L211</summary>

```text
HÌNH L211 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chú ếch liên tục kiểm tra khớp móng vuốt để đảm bảo các mũi xương đã thu gọn hoàn toàn vào bao gân trước khi bước vào các vòng đấu quyết định!". Bố cục: Cận cảnh bàn chân chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng: các móng xương thu gọn vào rãnh gân collagen đàn hồi an toàn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L212</summary>

```text
HÌNH L212 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Giờ giải lao kết thúc trong những tiếng cười sảng khoái! Tất cả mười tuyển thủ đã sẵn sàng quay trở lại đấu trường khốc liệt!". Bố cục: Dàn đèn pha rọi sáng trở lại sàn đấu, mười tuyển thủ bước ra vị trí thi đấu trong tiếng cổ vũ náo nhiệt của khán giả; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L213</summary>

```text
HÌNH L213 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chào mừng quý vị quay trở lại với Vòng bốn: Kỹ Sư Địa Hình và Những Xã Hội Động Vật Kỷ Luật Thép!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng giơ micro hướng về một sa bàn địa hình rộng lớn được dựng giữa sân vận động; tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng ô thử thách số bốn mang biểu tượng con đập và mạng lưới hang ngầm.
```
</details>

<details><summary>L214</summary>

```text
HÌNH L214 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tại vòng đấu này, chúng ta sẽ được chứng kiến cách những sinh vật hoang dã tái định hình cả cảnh quan thiên nhiên và bảo vệ giống nòi!". Bố cục: Mô hình sa bàn chiếu dòng sông uốn lượn, rừng cây nguyên sinh và lòng đất sâu nhiều tầng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L215</summary>

```text
HÌNH L215 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Không phải máy xúc, xe ủi hay xi măng cốt thép của con người, chính những chiếc đuôi dẹt, móng vuốt đào hầm và tinh thần kỷ luật bầy đàn đã tạo nên những kỳ quan sinh thái vĩ đại!". Bố cục: Hình ảnh so sánh máy ủi khổng lồ gầm rú với các kỹ sư động vật nhỏ bé đang miệt mài kiến tạo thiên nhiên; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L216</summary>

```text
HÌNH L216 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Không ai xứng đáng mở màn vòng đấu này hơn kỹ sư Hải Ly: kiến trúc sư thiên tài số một của thế giới tự nhiên!". Bố cục: chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo vác thước đo gỗ và xẻng nhỏ tiến vào sa bàn sông suối, ánh mắt tràn đầy nhiệt huyết công trình; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L217</summary>

```text
HÌNH L217 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khán giả thường nghĩ Hải Ly xây đập chỉ để bảo vệ hang ở của mình, nhưng một nghiên cứu 2020 trên tạp chí Ecological Applications đã chỉ ra tầm vóc vĩ đại hơn nhiều!". Bố cục: Đồ họa từ vệ tinh nhìn xuống: con đập ngăn nước tạo thành một vùng đất ngập nước xanh mướt rộng hàng chục héc-ta; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L218</summary>

```text
HÌNH L218 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khi những trận cháy rừng kinh hoàng quét qua Bắc Mỹ thiêu rụi toàn bộ thung lũng xung quanh, chính những con đập của Hải Ly đã tạo ra các ốc đảo ngập nước xanh tươi bất khả xâm phạm!". Bố cục: Bão lửa đỏ rực thiêu rụi rừng cây khô xung quanh, nhưng vùng đầm lầy của chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo vẫn xanh rì, muông thú tụ tập trú ẩn an toàn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L219</summary>

```text
HÌNH L219 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Độ ẩm cao và mực nước ngầm dồi dào từ đập Hải Ly chặn đứng hoàn toàn bước tiến của ngọn lửa hung tàn, cứu sống hàng vạn sinh mạng hoang dã!". Bố cục: Ranh giới rõ rệt: một bên tro tàn đen ngòm, một bên là ốc đảo nước trong xanh mát rượi do chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo kiến tạo; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tuyển thủ số ba! Sinh vật lầy lội không xương đáy biển sẵn sàng xả trọn bộ ruột qua phần đuôi để tẩu thoát! Hải Sâm!". Bố cục: chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù mập mạp màu cam sần sùi trườn ra sân khấu, tay phe phẩy chiếc quạt giấy mini trông vô cùng hài hước; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L220</summary>

```text
HÌNH L220 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Hơn thế nữa, đập Hải Ly giữ lại tới 80% lượng bùn đất xói mòn và kim loại nặng, thanh lọc nguồn nước uống trong lành cho toàn bộ hạ lưu!". Bố cục: Dòng nước đục ngầu chảy qua đập gỗ lắng cặn lại, dòng nước chảy ra hạ lưu trong vắt như gương; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L221</summary>

```text
HÌNH L221 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Những con đập của Hải Ly có thể tồn tại qua hàng thế kỷ, thậm chí có con đập cổ xưa dài tới 800 mét tại Canada nhìn thấy rõ mồn một từ ảnh chụp vệ tinh không gian!". Bố cục: Ảnh vệ tinh không gian hiển thị con đập Hải Ly vắt ngang thung lũng dài 800m khổng lồ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L222</summary>

```text
HÌNH L222 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Một cỗ máy thanh lọc môi trường sống tự nhiên không tốn một xu tiền điện của Trái Đất! Cả khán đài cúi mình thán phục trước Hải Ly!". Bố cục: Khán giả và ban giám khảo đồng loạt vỗ tay tán thưởng; chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo mỉm cười gật đầu tự hào.
```
</details>

<details><summary>L223</summary>

```text
HÌNH L223 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tiếp theo, hãy cùng nhìn sâu xuống lòng đất nước Úc nơi Gấu Túi Wombat làm nên điều kỳ diệu trong các trận thảm họa cháy rừng!". Bố cục: Sa bàn mặt đất lật mở để lộ mạng lưới đường hầm ngầm phức tạp của chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường sâu hai mét dưới lòng đất; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L224</summary>

```text
HÌNH L224 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Mỗi hệ thống hang của Wombat có thể kéo dài tới 30m với hàng chục ngách rẽ và nhiều cửa thoát hiểm được đào kiên cố!". Bố cục: Sơ đồ kiến trúc hang ngầm dài 30m với các phòng ngủ lót cỏ khô và hệ thống thông gió tự nhiên; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L225</summary>

```text
HÌNH L225 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Trong các trận hỏa hoạn lịch sử tại rừng nước Úc khi nhiệt độ mặt đất lên tới hàng 100°C, nhiệt độ dưới hang Wombat vẫn duy trì ổn định ở mức 20 độ mát mẻ!". Bố cục: Đồng hồ nhiệt độ so sánh: mặt đất nóng rực 100°C đỏ lửa, dưới hang chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường mát mẻ 20°C dịu nhẹ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L226</summary>

```text
HÌNH L226 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Camera của các nhà khoa học bảo tồn đã ghi lại những thước phim xúc động: chuột túi Wallaby, kỳ đà, chim sẻ và thú có túi cùng lũ lượt kéo nhau xuống hang Wombat để lánh nạn!". Bố cục: Các loài động vật chạy trốn ngọn lửa cùng chui xuống cửa hang của chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường, ngồi hòa bình bên cạnh chú gấu túi hiền lành; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L227</summary>

```text
HÌNH L227 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Wombat không hề xua đuổi hay tấn công mà hào phóng chia sẻ nơi trú ẩn an toàn, trở thành những người hùng cứu hỏa thầm lặng của đại lục Úc!". Bố cục: chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường ngồi gặm cỏ ở cửa hang, xung quanh là bạn bè muông thú được cứu sống vẫy tay cảm ơn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L228</summary>

```text
HÌNH L228 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Hệ thống hang ngầm này hoạt động như một boongke chống thảm họa thiên nhiên hoàn hảo nhất mà không cần đến bê tông cốt thép!". Bố cục: Mặt cắt lòng đất: hang ngầm kiên cố chở che cho muông thú bình yên vượt qua thảm họa; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L229</summary>

```text
HÌNH L229 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và cuối cùng là cấu trúc xã hội kỷ luật thép của Kiến Nổ dũng cảm bảo vệ tổ trên các tán rừng nhiệt đới Đông Nam Á!". Bố cục: Cành cây cổ thụ với lối vào tổ kiến chỉ nhỏ bằng đầu que tăm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tuyển thủ số bốn! Cổ vật sống 300 triệu năm tiết ra 20 lít keo nhớt trong chớp mắt làm nghẹt thở cá mập! Cá Mút Đá Hagfish!". Bố cục: chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện thân trơn tuột màu xám tím quấn quanh cột thủy tinh, toàn thân phủ các vệt bọt nhớt lấp lánh, thắt nút thân số 8 điêu luyện; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L230</summary>

```text
HÌNH L230 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tiến sĩ Alice Laciny phát hiện: trong tổ của Kiến Nổ có một tầng lớp lính gác cửa đặc biệt sở hữu hộp sọ biến đổi phẳng lì như một chiếc nút chai!". Bố cục: Phóng to chú kiến gác cửa: đầu hình đĩa tròn phẳng lì vừa khít tuyệt đối với miệng lỗ tổ tròn xoe; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L231</summary>

```text
HÌNH L231 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chúng dùng chính chiếc đầu bọc giáp của mình làm chiếc cửa chống đạn bịt kín hoàn toàn lối vào, ngăn chặn mọi kẻ xâm lược từ bên ngoài!". Bố cục: Một con nhện độc hung dữ cắn vào cửa tổ nhưng chỉ cắn trúng bề mặt sọ phẳng cứng như đá của kiến lính gác; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L232</summary>

```text
HÌNH L232 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chiếc cửa sống này chỉ mở ra khi kiến thợ đi kiếm ăn về gõ đúng mật mã râu pheromone đặc trưng của bầy đàn!". Bố cục: Chú kiến thợ dùng hai chiếc râu chạm nhẹ vào đầu kiến gác cửa theo nhịp điệu mật mã, chiếc đầu thụt vào mở lối đi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L233</summary>

```text
HÌNH L233 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Một hệ thống an ninh sinh học bảo mật tuyệt đối không thể phá khóa!". Bố cục: chú Kiến Nổ dũng cảm bảo vệ tổ hoạt hình màu đỏ cam, đeo ba lô chứa chất lỏng vàng phát sáng, đội mũ bảo hộ chống độc, ánh mắt quả cảm kiên cường đứng nghiêm trang gác cửa như một người lính bảo vệ tổ quốc quả cảm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L234</summary>

```text
HÌNH L234 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Để xây dựng những con đập dài hàng trăm mét, Hải Ly còn sở hữu kỹ năng đào kênh dẫn nước kỳ tài không kém các kỹ sư thủy lợi La Mã!". Bố cục: Sa bàn rừng rậm hiện lên các con kênh đào thẳng tắp sâu một mét do chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo đào bới; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L235</summary>

```text
HÌNH L235 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chúng tự đào các tuyến kênh ngập nước dài tới 200 mét đâm sâu vào các khu rừng gỗ cứng, để thả nổi các khúc gỗ nặng hàng chục ký trôi theo dòng nước về vị trí đắp đập mà không tốn sức kéo lê trên cạn!". Bố cục: Khúc gỗ to trôi nhẹ nhàng trên dòng kênh đào nhân tạo về phía con đập chính, chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo bơi theo đẩy lái chuyên nghiệp; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L236</summary>

```text
HÌNH L236 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Đặc biệt, thân đập của Hải Ly được thiết kế uốn cong hình cánh cung hướng ngược về phía dòng chảy, mô phỏng hoàn hảo nguyên lý chịu lực của các con đập thủy điện vòm bê tông hiện đại nhất!". Bố cục: Con đập gỗ uốn cong cánh cung cản phá sức ép khủng khiếp của dòng nước lũ mùa xuân một cách ngoạn mục; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L237</summary>

```text
HÌNH L237 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Hệ thống kiến trúc tự nhiên này có thể điều tiết lưu lượng nước của cả một lưu vực sông rộng lớn, biến Hải Ly thành loài động vật duy nhất có thể thay đổi địa hình Trái Đất ngang ngửa con người!". Bố cục: Hình ảnh vệ tinh so sánh công trình thành phố của con người và hệ thống đầm lầy do chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo kiến tạo hài hòa tuyệt mỹ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L238</summary>

```text
HÌNH L238 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Để chuẩn bị cho mùa đông băng giá Bắc Mỹ khi mặt hồ đóng băng dày hàng mét, Hải Ly còn xây dựng những kho lương thực ngập nước ngầm vô cùng thông minh!". Bố cục: Đáy hồ nước mùa đông: lớp băng dày phủ trên mặt hồ, bên dưới chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo bơi lội trong làn nước mát; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L239</summary>

```text
HÌNH L239 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chúng cắm chặt hàng trăm cành cây gỗ tươi giàu dinh dưỡng xuống lớp bùn sâu dưới đáy hồ ngay cạnh cửa hang ngầm!". Bố cục: Các cành cây tươi được cắm ngay ngắn thành từng hàng dưới đáy bùn như một kho thực phẩm đông lạnh tự nhiên; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tuyển thủ số năm! Bậc thầy phân thân sở hữu 9 bộ não và có thể cải trang thành 15 loài kịch độc đáy đại dương! Bạch Tuộc Mimic!". Bố cục: chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình sọc vằn nâu trắng uốn lượn biến ảo thành hình dáng rắn biển rồi lại hóa thành cá sư tử đầy gai góc; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L240</summary>

```text
HÌNH L240 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khi mặt hồ đóng băng kín mít, Hải Ly chỉ việc bơi ra cửa hang ngầm, rút một cành cây tươi dưới bùn mang vào hang thưởng thức mà không cần thò đầu lên mặt băng lạnh giá!". Bố cục: chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo ngồi trong hang ấm áp gặm cành cây tươi ngon lành, bên ngoài gió tuyết gầm rú dữ dội; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L241</summary>

```text
HÌNH L241 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Một công trình đập của Hải Ly có thể nâng mực nước ngầm của toàn bộ lưu vực xung quanh lên cao thêm từ một đến hai mét suốt mùa khô hạn!". Bố cục: Sơ đồ địa chất cắt lớp: mực nước ngầm dưới rễ cây rừng dâng cao màu xanh ngọc bích màu mỡ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L242</summary>

```text
HÌNH L242 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nhờ nguồn nước ngầm dồi dào này, thảm thực vật ven bờ phát triển xanh tốt quanh năm, tạo nguồn thức ăn dồi dào nuôi sống các đàn hươu nai và chim muông vượt qua mùa đông khắc nghiệt!". Bố cục: Đàn hươu rừng và thỏ tuyết tìm đến mép hồ của chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo uống nước và gặm cỏ tươi tốt thanh bình; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L243</summary>

```text
HÌNH L243 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Hải Ly thực sự là một kỹ sư kiến tạo cảnh quan sinh thái có tầm ảnh hưởng sâu rộng bậc nhất hành tinh!". Bố cục: chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo đứng tự hào bên con đập gỗ vững chãi ngắm nhìn thung lũng xanh tươi bạt ngàn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L244</summary>

```text
HÌNH L244 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Không dừng lại ở việc đắp đập, những kiến trúc sư Hải Ly tài ba còn đào những con kênh dẫn nước dài tới 500m sâu vào giữa rừng già!". Bố cục: Sa bàn đồ họa hiển thị mạng lưới kênh đào chằng chịt của chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo tỏa sâu vào rừng già như hệ thống giao thông thủy lợi hoàn hảo; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L245</summary>

```text
HÌNH L245 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Những con kênh này cho phép Hải Ly thả trôi những khúc gỗ nặng hàng trăm cân về tổ một cách nhẹ nhàng, giảm thiểu tối đa nguy cơ bị thú dữ mai phục trên cạn!". Bố cục: chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo đẩy khúc gỗ trôi êm ả trên dòng kênh đào mát rượi, thảnh thơi bơi về tổ ấm an toàn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L246</summary>

```text
HÌNH L246 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Còn tấm khiên sụn mông của Wombat cứng đến mức những cú cắn của chó rừng Dingo hay đại bàng đuôi nhọn chỉ để lại những vết xước mờ nhạt không đáng kể!". Bố cục: Chó rừng Dingo cắn mạnh vào mông chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường nhưng bị gãy răng nhe nanh đau đớn, tấm khiên sụn không hề suy chuyển; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L247</summary>

```text
HÌNH L247 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Hải Ly còn sở hữu lớp lông dày tới 10.000 sợi trên một xen-ti-mét vuông da, được bôi trơn bởi lớp dầu castoreum chống thấm nước tuyệt đối!". Bố cục: Kính hiển vi phóng to lớp lông dày mượt mà của chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo: các bọt khí bị bẫy lại giữ ấm cơ thể trong làn nước băng giá; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L248</summary>

```text
HÌNH L248 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nhờ đó, ngay cả khi bơi lội dưới lớp băng dày vào mùa đông Bắc Mỹ, da của Hải Ly vẫn hoàn toàn khô ráo và ấm áp!". Bố cục: chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo lặn ngụp dưới tảng băng trôi mà không hề run rẩy, cơ thể tỏa nhiệt hồng ấm áp; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L249</summary>

```text
HÌNH L249 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Ban giám khảo xin công bố kết quả Vòng bốn! Huy chương Đồng thuộc về Kiến Nổ dũng cảm bảo vệ tổ với cánh cửa sọ nút chai an ninh pheromone!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ búa, trao huy chương đồng phát sáng cho chú Kiến Nổ dũng cảm bảo vệ tổ hoạt hình màu đỏ cam, đeo ba lô chứa chất lỏng vàng phát sáng, đội mũ bảo hộ chống độc, ánh mắt quả cảm kiên cường.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tuyển thủ số sáu! Chiến xa đào hầm nước Úc sở hữu tấm mông bọc thép 3cm đập nát sọ kẻ thù! Gấu Túi Wombat!". Bố cục: chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường mập mạp bệ vệ bước ra, quay chiếc mông bọc thép titan chống cắn về phía khán giả khoe sức mạnh, tay cầm xẻng xúc đất mini; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L250</summary>

```text
HÌNH L250 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Huy chương Bạc thuộc về Gấu Túi Wombat với mạng lưới hang ngầm cứu trợ muông thú trong thảm họa!". Bố cục: chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường vui vẻ đón nhận tấm huy chương bạc lấp lánh thứ hai của mình.
```
</details>

<details><summary>L251</summary>

```text
HÌNH L251 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và Huy chương Vàng ba điểm xứng đáng thuộc về kỹ sư Hải Ly với công trình đập nước chống hạn hán và đẩy lùi bão lửa!". Bố cục: chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo đứng trên bục số một giơ cao huy chương vàng, khán đài tung hoa giấy rực rỡ chúc mừng.
```
</details>

<details><summary>L252</summary>

```text
HÌNH L252 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Bảng điểm sau bốn vòng đấu tiếp tục có biến động lớn: Wombat vươn lên dẫn đầu với năm điểm! Hải Ly bứt phá mạnh mẽ lên bốn điểm!". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) cập nhật điểm số: Wombat 5 điểm, Hải Ly 4 điểm, Sứa Bất Tử 3 điểm, Chuột Chũi Sao 3 điểm, Hagfish 2 điểm, Axolotl 2 điểm, Bạch Tuộc Mimic 2 điểm, Ếch dị nhân móng vuốt hoạt hình đáng yêu 1 điểm, Kiến Nổ 1 điểm; cuộc rượt đuổi điểm số vô cùng nghẹt thở!
```
</details>

<details><summary>L253</summary>

```text
HÌNH L253 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tiến vào chặng đua thứ năm! Chào mừng quý vị đến với Vòng năm: Kháng Thể Siêu Cấp và Những Bộ Gen Đột Biến Kỳ Vĩ!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng bước lên bục chỉ tay vào màn hình hiển thị đồ họa chuỗi xoắn kép DNA ba chiều rực rỡ; tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng ô thử thách số năm mang biểu tượng phân tử gen.
```
</details>

<details><summary>L254</summary>

```text
HÌNH L254 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Ở vòng đấu này, cuộc cạnh tranh không còn diễn ra ở tầm cơ bắp hay móng vuốt, mà đi sâu vào tận cấp độ phân tử và tế bào vi mô!". Bố cục: Mô hình kính hiển vi điện tử chiếu rọi vào nhân tế bào phát sáng lung linh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L255</summary>

```text
HÌNH L255 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Những bí mật di truyền được mã hóa qua hàng tỷ cặp base nitơ chính là tấm bản đồ thần kỳ giúp các dị nhân vượt qua những nghịch lý sinh tồn khắc nghiệt nhất!". Bố cục: Các chuỗi mã hóa di truyền ACGT chạy rực rỡ như dòng thác ma trận số học sinh học; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L256</summary>

```text
HÌNH L256 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tuyển thủ đầu tiên bước lên bục phân tích di truyền: Kỳ Nhông Axolotl của hồ Xochimilco!". Bố cục: chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói bơi đến trước màn hình chiếu bộ gen, nụ cười rạng rỡ và sáu mang lông vũ đỏ đung đưa uyển chuyển; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L257</summary>

```text
HÌNH L257 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Một công trình nghiên cứu quy mô toàn cầu đăng tải trên tạp chí Nature 2018 đã giải mã thành công toàn bộ hệ gen của Axolotl!". Bố cục: Hình ảnh chuỗi DNA khổng lồ kéo dài vô tận qua hàng trăm trang màn hình dữ liệu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L258</summary>

```text
HÌNH L258 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Kết quả khiến giới khoa học sững sờ: bộ gen của chú kỳ nhông này dài tới 32 tỷ cặp base nitơ, tức là gấp 10 lần toàn bộ hệ gen của một con người trưởng thành!". Bố cục: Đồ họa so sánh hai chuỗi DNA: chuỗi gen người 3,2 tỷ base ngắn bằng một gang tay, chuỗi gen của chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói dài 32 tỷ base cuộn thành nhiều vòng khổng lồ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L259</summary>

```text
HÌNH L259 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Ẩn sâu trong 32 tỷ cặp base này là những đoạn gen kiểm soát phân bào độc nhất vô nhị: các tế bào mọc lại chi phân chia với tốc độ tên lửa nhưng tuyệt đối không bao giờ phát triển thành khối u ác tính!". Bố cục: Các tế bào phân chia nhanh chóng nhưng xếp hàng ngay ngắn trật tự dưới sự kiểm soát của gen ức chế ung thư; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tuyển thủ số bảy! Cỗ máy săn mồi mù lòa mang 22 xúc tu hồng đớp mồi nhanh nhất hành tinh! Chuột Chũi Mũi Sao!". Bố cục: chú Chuột Chũi Mũi Sao hoạt hình lông đen nhung mượt mà, mũi xòe ra 22 xúc tu đỏ hồng như bông hoa sao biển, đeo kính râm mù lòa nhưng phản xạ siêu thanh đeo kính râm ngầu, chiếc mũi sao biển đỏ hồng nhấp nháy liên hồi quét tín hiệu không gian; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L260</summary>

```text
HÌNH L260 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Axolotl sở hữu khả năng kháng ung thư tự nhiên gần như tuyệt đối, trở thành hình mẫu vàng cho các nhà nghiên cứu y học di truyền thế giới!". Bố cục: Chú kỳ nhông chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói khoác áo choàng bác sĩ nhỏ, cầm ống nghiệm tỏa sáng lấp lánh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L261</summary>

```text
HÌNH L261 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Cơ chế kiểm soát chu kỳ tế bào nghiêm ngặt đến mức ngay cả khi các nhà khoa học cố tình tiêm các hoạt chất gây ung thư cực mạnh, cơ thể Axolotl vẫn tự động đào thải và tái tạo lại mô tế bào khỏe mạnh bình thường!". Bố cục: Khối u thí nghiệm vừa manh nha lập tức bị các đại thực bào và enzym của chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói tiêu diệt sạch sẽ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L262</summary>

```text
HÌNH L262 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Mười điểm cho sự kỳ diệu của bộ gen Axolotl! Nhưng ngay lập tức, Sứa Bất Tử bay lơ lửng bước vào vòng đo lường gen telomere!". Bố cục: chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực trôi dạt vào buồng soi gen, vương miện nhỏ xíu lấp lánh ánh hào quang hồng tím; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L263</summary>

```text
HÌNH L263 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "2022, một nhóm nghiên cứu tại đại học Oviedo Tây Ban Nha đã công bố bản giải mã di truyền của Sứa Bất Tử trên kỷ yếu Viện Hàn lâm Khoa học Quốc gia Hoa Kỳ!". Bố cục: Bìa bài báo PNAS 2022 hiện lên với biểu đồ so sánh giữa Sứa Bất Tử và các loài sứa thông thường; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L264</summary>

```text
HÌNH L264 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Họ phát hiện Sứa Bất Tử sở hữu số lượng gen nhân đôi gấp đôi ở các cụm gen chịu trách nhiệm bảo vệ và duy trì độ dài của telomere: chiếc nắp bảo vệ ở đầu mút nhiễm sắc thể!". Bố cục: Cận cảnh đầu mút nhiễm sắc thể: nắp telomere của sinh vật thường ngắn dần theo tuổi tác, còn của chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực liên tục được đắp dài thêm nguyên vẹn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L265</summary>

```text
HÌNH L265 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Mỗi khi cơ thể bị lão hóa, hệ enzym telomerase và cơ chế sửa chữa lỗi sao chép DNA tự động kích hoạt ở mức tối đa, xóa sạch mọi dấu vết già nua và tái thiết lập đồng hồ sinh học về số không!". Bố cục: Chiếc đồng hồ sinh học quay ngược kim thời gian về vạch xuất phát, chuỗi DNA sáng bóng như mới xuất xưởng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L266</summary>

```text
HÌNH L266 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Một bộ gen bất tử thực thụ theo đúng nghĩa đen di truyền học!". Bố cục: chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực xoay tròn giữa các phân tử DNA phát sáng lung linh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L267</summary>

```text
HÌNH L267 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chúng không chỉ sửa chữa DNA bị đứt gãy mà còn sao chép dự phòng hàng trăm bản sao gen chống stress oxy hóa, giúp tế bào luôn duy trì trạng thái thanh xuân vĩnh cửu!". Bố cục: Mô hình tế bào chuông sứa trẻ hóa phát sáng như những viên ngọc bích lung linh dưới đáy biển; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L268</summary>

```text
HÌNH L268 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và không thể bỏ qua Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu với lá chắn kháng sinh sinh học trên da suối xiết!". Bố cục: chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng ngồi trong dòng nước đục ngầu chứa đầy vi khuẩn và nấm mốc; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L269</summary>

```text
HÌNH L269 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Sau khi tự bẻ xương đâm rách toạc da chân để nghênh chiến, làm thế nào chú ếch này không bị nhiễm trùng huyết trong môi trường bùn lầy dơ bẩn?". Bố cục: Vết thương hở trên ngón chân tiếp xúc với dòng nước bùn đầy vi khuẩn hoạt hình hung dữ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tuyển thủ số tám! Nữ chiến binh dũng cảm bảo vệ tổ sẵn sàng tạo bong bóng dính cơ thể phun keo dính bảo vệ an toàn cho tổ ấm! Kiến Nổ dũng cảm bảo vệ tổ!". Bố cục: chú Kiến Nổ dũng cảm bảo vệ tổ hoạt hình màu đỏ cam, đeo ba lô chứa chất lỏng vàng phát sáng, đội mũ bảo hộ chống độc, ánh mắt quả cảm kiên cường đội mũ bảo hộ chống độc, đeo ba lô chứa chất lỏng vàng phát quang, bước đi đầy quả cảm kiên định; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L270</summary>

```text
HÌNH L270 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Các tuyến da của ếch đực tiết ra hàng loạt chuỗi peptide kháng khuẩn phổ rộng có khả năng tiêu diệt lập tức các loại nấm sát thủ và vi khuẩn gây hoại tử chỉ trong vài phút tiếp xúc!". Bố cục: Lớp gel kháng khuẩn từ da tiết ra tạo thành màng bảo vệ vô hình, các vi khuẩn chạm vào liền tan rã biến mất; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L271</summary>

```text
HÌNH L271 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nhờ vậy, vết rách tự lành thần tốc mà không cần đến một viên thuốc kháng sinh nào!". Bố cục: chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng nhấc bàn chân lành lặn lên khoe trước ống kính với nụ cười tự tin; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L272</summary>

```text
HÌNH L272 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Bên cạnh bộ gen khổng lồ của Axolotl và Sứa, Bạch Tuộc Mimic cũng khiến các nhà di truyền học kinh ngạc với cơ chế chỉnh sửa ARN độc nhất vô nhị!". Bố cục: Mô hình chuỗi thông tin di truyền ARN thông tin phát sáng lung linh bên trong nhân tế bào thần kinh bạch tuộc; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L273</summary>

```text
HÌNH L273 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nghiên cứu công bố trên tạp chí Science năm 2017 của nhóm tiến sĩ Eli Eisenberg phát hiện: loài bạch tuộc này không cần thay đổi chuỗi D-N-A gốc mà trực tiếp biên tập lại các phân tử ARN thông tin!". Bố cục: Các enzym biên tập hoạt hình cắt dán và thay thế các mã base trên chuỗi ARN một cách linh hoạt; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L274</summary>

```text
HÌNH L274 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Hơn 60 phần trăm các bản phiên mã thần kinh của chúng được tái cấu trúc linh hoạt theo nhiệt độ nước và nồng độ oxy của môi trường!". Bố cục: Khi nước biển lạnh đi hoặc ấm lên, các kênh ion thần kinh tự động thích nghi tối ưu mà không cần chờ đợi hàng ngàn năm tiến hóa gen; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L275</summary>

```text
HÌNH L275 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Một khả năng lập trình phần mềm sinh học theo thời gian thực vượt xa mọi hệ điều hành máy tính tinh vi nhất của nhân loại!". Bố cục: Hình ảnh chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình phát sáng các vi mạch sinh học tự động cập nhật phần mềm thích nghi đại dương; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L276</summary>

```text
HÌNH L276 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và điều kỳ lạ nhất trong bộ gen của Cá Mút Đá Hagfish vừa được các nhà di truyền học đại học Tokyo làm sáng tỏ: hiện tượng đào thải D-N-A có lập trình trong tế bào soma!". Bố cục: Sơ đồ nhân tế bào của Hagfish: các đoạn nhiễm sắc thể tự động phân cắt và đào thải một cách có trật tự; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L277</summary>

```text
HÌNH L277 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khi Hagfish phát triển từ phôi thai thành cá thể trưởng thành, các tế bào cơ thể của chúng tự động loại bỏ tới 20% lượng D-N-A không cần thiết trong nhân tế bào!". Bố cục: Chiếc kéo sinh học hoạt hình cắt tỉa các đoạn gen thừa thãi vứt bỏ ra ngoài, giúp bộ gen cơ thể gọn nhẹ tối đa; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L278</summary>

```text
HÌNH L278 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chúng chỉ giữ lại trọn vẹn toàn bộ bộ gen gốc trong các tế bào sinh dục mầm, giúp cơ thể tiết kiệm tối đa năng lượng sao chép và duy trì sự sống bền bỉ suốt hàng trăm triệu năm!". Bố cục: Tế bào sinh dục phát sáng trọn vẹn, còn tế bào cơ thể chạy ở phiên bản tinh giản siêu tiết kiệm năng lượng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L279</summary>

```text
HÌNH L279 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Trong khi đó, hệ enzym sửa chữa D-N-A của Sứa Bất Tử hoạt động với độ chính xác tuyệt đối, loại bỏ tới 99,9% phần trăm các đột biến sai hỏng trong quá trình sao chép!". Bố cục: Robot phân tử enzym kiểm tra chuỗi DNA phát hiện lỗi và dán bản vá hoàn hảo; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tuyển thủ số chín! Tổng công trình sư thiên tài sở hữu răng cam bọc sắt đốn ngã cổ thụ xây đập nước vĩ đại! Hải Ly!". Bố cục: chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo đội mũ bảo hộ công trình vàng, vác khúc gỗ lớn trên vai, chiếc đuôi dẹt đập bôm bốp xuống sàn chào khán giả; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L280</summary>

```text
HÌNH L280 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nhờ khả năng tự sửa lỗi di truyền liên tục này, Sứa Bất Tử không bao giờ tích lũy các đột biến gây thoái hóa hay lão hóa sớm như các sinh vật bậc cao khác!". Bố cục: Chuỗi xoắn kép DNA của chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực luôn sáng bóng và thẳng tắp như vừa mới được tạo tác; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L281</summary>

```text
HÌNH L281 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Một bí mật sinh học phi thường mà các nhà khoa học đang nỗ lực giải mã để áp dụng vào công nghệ kéo dài tuổi xuân cho con người!". Bố cục: Nhà khoa học mỉm cười nâng niu chuỗi DNA mô phỏng của sứa dưới ánh đèn phòng thí nghiệm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L282</summary>

```text
HÌNH L282 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Bí mật đằng sau khả năng chữa lành không để lại sẹo của Axolotl nằm ở các cụm tế bào gốc blastema: chúng có thể biến đổi thành bất kỳ loại mô tế bào nào của cơ thể!". Bố cục: Kính hiển vi soi các tế bào gốc blastema của chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói phân chia tạo thành cơ xương, mạch nước màu và dây thần kinh hoàn hảo; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L283</summary>

```text
HÌNH L283 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khi bị tổn thương, các đại thực bào của Axolotl dập tắt phản ứng viêm trong vài giờ, ngăn chặn triệt để sự hình thành mô xơ sẹo thường thấy ở động vật có vú!". Bố cục: Đồ họa đại thực bào quét sạch tế bào chết và kích hoạt tái sinh mô nguyên bản không tì vết; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L284</summary>

```text
HÌNH L284 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Còn enzyme telomerase của Sứa Bất Tử liên tục nối dài các đầu mút nhiễm sắc thể, giúp tế bào phân chia vĩnh viễn mà không bao giờ chạm tới giới hạn lão hóa Hayflick!". Bố cục: Chuỗi xoắn kép D-N-A của chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực được enzyme telomerase gắn thêm các đoạn mũ bảo vệ phát sáng rực rỡ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L285</summary>

```text
HÌNH L285 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Ban giám khảo xin công bố bảng điểm Vòng năm! Huy chương Đồng thuộc về Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu với lớp peptide kháng khuẩn tự chữa lành vết thương hở!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ búa, trao huy chương đồng phát sáng cho chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng.
```
</details>

<details><summary>L286</summary>

```text
HÌNH L286 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Huy chương Bạc thuộc về Sứa Bất Tử với bộ gen bảo vệ telomere và xóa bỏ lão hóa tế bào!". Bố cục: chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực đón nhận thêm tấm huy chương bạc lấp lánh thứ hai.
```
</details>

<details><summary>L287</summary>

```text
HÌNH L287 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và Huy chương Vàng ba điểm xứng đáng thuộc về Kỳ Nhông Axolotl với bộ gen 32 tỷ cặp base kháng ung thư và tái sinh mô thần kỳ!". Bố cục: chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói đội vòng nguyệt quế nhận huy chương vàng rực rỡ trong tiếng pháo hoa nổ vang.
```
</details>

<details><summary>L288</summary>

```text
HÌNH L288 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Bảng tổng sắp sau năm vòng thi đấu tiếp tục bùng nổ dữ dội: Sứa Bất Tử và Axolotl cùng vươn lên chia sẻ vị trí dẫn đầu với năm điểm! Gấu Wombat cũng đồng hạng năm điểm! Hải Ly bám sát với bốn điểm!". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) cập nhật điểm số: Wombat 5 điểm, Sứa Bất Tử 5 điểm, Axolotl 5 điểm, Hải Ly 4 điểm, Chuột Chũi Sao 3 điểm, Hagfish 2 điểm, Bạch Tuộc Mimic 2 điểm, Ếch dị nhân móng vuốt hoạt hình đáng yêu 2 điểm, Kiến Nổ 1 điểm; cuộc tranh đua ngôi vương tam mã nghẹt thở!
```
</details>

<details><summary>L289</summary>

```text
HÌNH L289 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tiến vào Vòng thi đấu thứ sáu: Người Hùng Bảo Vệ Hệ Sinh Thái Đại Dương và Rừng Xanh!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vung micro kích hoạt sa bàn mô phỏng hệ sinh thái rạn san hô và đầm lầy rực rỡ sắc màu; tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng ô thử thách số sáu mang biểu tượng giọt nước và mầm cây xanh.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và tuyển thủ số mười... xin mời ban tổ chức đưa kính lúp quang học ra sân vì bạn ấy đang trôi lơ lửng trong ly nước của giám khảo!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cúi người nhìn chăm chú vào chiếc ly thủy tinh nhỏ trên bàn giám khảo; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L290</summary>

```text
HÌNH L290 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Ở vòng thi này, chúng ta không nhìn vào sức mạnh cá nhân, mà đo lường đóng góp sinh thái vĩ đại mà các tuyển thủ âm thầm cống hiến cho hành tinh xanh!". Bố cục: Mô hình Trái Đất quay tròn, các luồng oxy và khoáng chất tuần hoàn lấp lánh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L291</summary>

```text
HÌNH L291 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Mỗi sinh vật dù nhỏ bé hay mang vẻ ngoài kỳ dị đều nắm giữ một mắt xích sống còn, duy trì sự cân bằng mong manh của toàn bộ mạng lưới sự sống!". Bố cục: Hình ảnh mạng nhện sinh thái khổng lồ kết nối hàng triệu loài sinh vật, các điểm nút phát sáng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L292</summary>

```text
HÌNH L292 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tuyển thủ bước lên sàn đầu tiên khiến tất cả bất ngờ: chú Hải Sâm lầy lội từng bị coi là kẻ lười biếng nhất đáy biển!". Bố cục: chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù trườn ra giữa sa bàn rạn san hô ngập tràn sắc màu cá bơi lượn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L293</summary>

```text
HÌNH L293 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Các nhà hải dương học tại đại học New South Wales đã công bố một báo cáo gây chấn động: Hải Sâm chính là chiếc máy hút bụi sinh học quan trọng bậc nhất của các rạn san hô nhiệt đới!". Bố cục: chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù dùng các xúc tu quanh miệng quét sạch từng lớp cát bẩn dưới đáy biển nuốt vào bụng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L294</summary>

```text
HÌNH L294 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Mỗi năm, quần thể hải sâm trên 1 km² vuông đáy biển tiêu hóa và thanh lọc tới 130 tấn cát và trầm tích hữu cơ thối rữa!". Bố cục: Mô hình đồ họa 130 tấn cát bẩn đi qua đường ruột của Hải Sâm được phân giải sạch sẽ vi khuẩn có hại; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L295</summary>

```text
HÌNH L295 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Quan trọng hơn thế, chất thải sau khi tiêu hóa của Hải Sâm chứa hàm lượng Canxi Cacbonat kiềm tính cực cao!". Bố cục: Các tinh thể Canxi Cacbonat màu trắng sáng phát quang tỏa ra từ chất thải nuôi dưỡng các nhánh san hô lớn nhanh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L296</summary>

```text
HÌNH L296 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Dòng chất kiềm tự nhiên này làm tăng độ pH của nước biển xung quanh, giúp trung hòa hiện tượng axit hóa đại dương do biến đổi khí hậu và bảo vệ san hô khỏi nguy cơ bị tẩy trắng hủy diệt!". Bố cục: Môi trường nước axit bị trung hòa trở lại màu xanh ngọc bích trong lành, rạn san hô phát triển rực rỡ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L297</summary>

```text
HÌNH L297 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Các nhà khoa học tính toán: nếu loại bỏ hoàn toàn Hải Sâm khỏi một rạn san hô, tốc độ suy thoái của san hô sẽ tăng vọt gấp 3 lần chỉ sau vài năm ngắn ngủi!". Bố cục: Hình ảnh rạn san hô không có chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù bị phủ đầy bùn đen và rêu tảo độc hại chết dần mòn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L298</summary>

```text
HÌNH L298 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Không có Hải Sâm hút bụi và cân bằng độ pH, các rạn san hô lộng lẫy của hành tinh sẽ dần chết mòn thành bãi tha ma đá vôi! Cả khán đài nghiêng mình thán phục trước Hải Sâm!". Bố cục: Khán đài đồng loạt đứng dậy vỗ tay vang dội; chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù mỉm cười sung sướng phẩy quạt giấy tít mù; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L299</summary>

```text
HÌNH L299 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tiếp theo, hãy cùng nhìn lên các con đập của Hải Ly: chiếc bẫy lưu giữ carbon tự nhiên khổng lồ của lục địa!". Bố cục: Sa bàn rừng ôn đới Bắc Mỹ hiện lên với hệ thống đầm lầy ngập nước của chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Dạ em ở đây nè anh MC ơi! Em chỉ dài 4,5mm thôi nhưng tuổi thọ của em thì bằng cả vũ trụ cộng lại đó nha!". Bố cục: Cận cảnh phóng to qua kính hiển vi: chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực trong suốt hình chuông nhỏ xíu phát ánh sáng hồng tím ma thuật, đeo bùa hộ mệnh vô cực vẫy xúc tu tí hon; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L300</summary>

```text
HÌNH L300 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Các nhà sinh thái học phát hiện: lớp trầm tích giàu hữu cơ đọng lại phía sau những con đập của Hải Ly lưu giữ hàng triệu tấn carbon hữu cơ, ngăn không cho chúng thoát vào khí quyển!". Bố cục: Đồ họa mũi tên khí nhà kính bị giữ chặt dưới lớp bùn sâu mát lạnh của đáy hồ nước chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L301</summary>

```text
HÌNH L301 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nhờ có vùng ngập nước của Hải Ly, độ đa dạng sinh học của các loài chim di cư, cá nước ngọt và động vật lưỡng cư tăng vọt tới 33% so với các dòng suối thông thường!". Bố cục: Đàn vịt trời, cá hồi và ếch nhái bơi lội rộn ràng xung quanh hang của chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L302</summary>

```text
HÌNH L302 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Hải Ly không chỉ xây nhà cho mình, chúng xây dựng cả một thiên đường sinh thái nuôi dưỡng muôn loài!". Bố cục: chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo vẫy chiếc đuôi dẹt chào các bạn động vật thân thiện; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L303</summary>

```text
HÌNH L303 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Những vùng đất ngập nước này duy trì dòng chảy mát mẻ vào mùa hè và ngăn lũ quét vào mùa mưa bão, trở thành tấm khiên phòng hộ tự nhiên vô giá của lục địa Bắc Mỹ!". Bố cục: Mô hình dòng nước lũ cuồn cuộn đổ về bị con đập chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo hãm chậm lại, dòng nước chảy ra hạ lưu hiền hòa êm ả; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L304</summary>

```text
HÌNH L304 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và cuối cùng là đóng góp âm thầm của cụ tổ Cá Mút Đá Hagfish dưới đáy vực sâu 1.000m lạnh giá!". Bố cục: Đáy đại dương tăm tối nơi một xác cá voi khổng lồ chìm xuống đáy biển (whale fall); KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L305</summary>

```text
HÌNH L305 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khi xác cá voi chìm xuống vùng biển sâu không có ánh sáng, hàng 1.000 con Hagfish sẽ vùi mình vào xác thịt, hấp thụ chất dinh dưỡng trực tiếp qua da và tiêu hóa sạch sẽ các mô mỡ thối rữa!". Bố cục: Đàn chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện quấn quanh xác cá voi dọn dẹp sạch sẽ trong làn nước sâu thẳm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L306</summary>

```text
HÌNH L306 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Họ phân giải và hoàn trả nguồn nitơ và phốt-pho quý giá trở lại chuỗi thức ăn đáy biển, nuôi sống cả một quần xã sinh vật biển sâu tăm tối suốt hàng chục năm ròng!". Bố cục: Các dưỡng chất tỏa sáng phân tán nuôi sống tôm cua biển sâu và vi khuẩn hóa dưỡng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L307</summary>

```text
HÌNH L307 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nếu không có đội dọn dẹp Hagfish, đáy biển sâu sẽ bị ngạt thở bởi lớp chất béo tích tụ, cắt đứt chu trình tuần hoàn dinh dưỡng toàn cầu!". Bố cục: Đồ họa dòng hải lưu mang chất dinh dưỡng từ đáy sâu dâng lên bề mặt nuôi sống các tầng sinh vật phù du; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L308</summary>

```text
HÌNH L308 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Không chỉ có Hải Sâm và Hải Ly, Gấu Túi Wombat và Ếch dị nhân móng vuốt hoạt hình đáng yêu cũng đóng góp những mắt xích sinh thái vô giá cho lục địa của mình!". Bố cục: Sa bàn rừng cây Tây Phi và thảo nguyên cằn cỗi nước Úc hiện lên rực rỡ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L309</summary>

```text
HÌNH L309 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Những viên phân hình lập phương của Wombat chứa đầy các hạt giống cỏ bản địa và hàng tỷ bào tử nấm rễ cộng sinh mycorrhiza!". Bố cục: Cận cảnh viên phân lập phương vùi trong đất: hạt giống cỏ xanh nảy mầm tươi tốt nhờ nguồn dinh dưỡng hữu cơ màu mỡ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Một tràng pháo tay cho sự có mặt của mười dũng sĩ dị nhân! Và theo truyền thống, mời tất cả bước vào Lễ Cân Ký Đo Đạc khởi động!". Bố cục: Chiếc bàn cân điện tử khổng lồ giữa đấu trường sáng đèn, các kỹ thuật viên đeo găng tay chuẩn bị ghi nhận số liệu; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cầm micro đứng bên cạnh.
```
</details>

<details><summary>L310</summary>

```text
HÌNH L310 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khi phân rã, chúng làm tơi xốp các tầng đất cằn cỗi và giữ nước ngầm cho thảo nguyên khô hạn nước Úc sau các đợt hạn hán kéo dài!". Bố cục: Thảo nguyên khô cằn mọc lên những mảng cỏ xanh tươi mơn mởn xung quanh các tổ hang Wombat; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L311</summary>

```text
HÌNH L311 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Còn Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu là loài săn mồi đầu bảng kiểm soát mật độ ấu trùng muỗi vằn và ruồi đen truyền bệnh dịch ở các dòng suối nhiệt đới Tây Phi!". Bố cục: chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng đớp gọn đàn muỗi vằn truyền bệnh, bảo vệ sức khỏe cho các cộng đồng dân cư ven rừng nguyên sinh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L312</summary>

```text
HÌNH L312 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Ở trên các tầng tán rừng nhiệt đới, Kiến Nổ dũng cảm bảo vệ tổ cũng đóng vai trò là những vệ sĩ sinh thái bảo vệ sức khỏe cho các cây cổ thụ nguyên sinh!". Bố cục: Cành cây rừng nhiệt đới xum xuê lá xanh mướt, đàn chú Kiến Nổ dũng cảm bảo vệ tổ hoạt hình màu đỏ cam, đeo ba lô chứa chất lỏng vàng phát sáng, đội mũ bảo hộ chống độc, ánh mắt quả cảm kiên cường diễu hành tuần tra trật tự; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L313</summary>

```text
HÌNH L313 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chúng tiêu diệt sạch sẽ các loài sâu róm phá hoại lá non và ngăn chặn các loài rệp sáp hút nhựa cây xâm lấn, duy trì sự xanh tốt cho tán rừng nhiệt đới đại ngàn!". Bố cục: Đàn kiến phối hợp xua đuổi các loài sâu bọ gây hại khỏi cành lá, giúp cây cổ thụ phát triển khỏe mạnh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L314</summary>

```text
HÌNH L314 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Sự hy sinh của từng cá thể kiến thợ không chỉ bảo vệ tổ ấm, mà gián tiếp gìn giữ lá phổi xanh khổng lồ cho toàn bộ hệ sinh thái rừng mưa xích đạo!". Bố cục: Toàn cảnh tán rừng nhiệt đới xanh bạt ngàn dưới ánh nắng ban mai rực rỡ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L315</summary>

```text
HÌNH L315 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Các nhà khoa học ước tính: lượng Canxi Cacbonat kiềm tính mà quần thể Hải Sâm bài tiết ra ngoài có thể bù đắp lại tới 20% lượng vôi hóa bị mất đi của rạn san hô do biến đổi khí hậu!". Bố cục: Các phân tử Canxi Cacbonat lấp lánh kết tinh hàn gắn lại các nhánh san hô bị gãy vụn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L316</summary>

```text
HÌNH L316 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chúng hoạt động như những người thợ hồ cần mẫn trát từng lớp vữa kiềm bảo vệ pháo đài san hô trước sự bào mòn của dòng nước biển axit hóa!". Bố cục: chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù trườn qua các khối san hô để lại những vệt kiềm trắng sáng nuôi dưỡng rạn san hô xanh tốt; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L317</summary>

```text
HÌNH L317 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Trong các trận đại hỏa hoạn cháy rừng lịch sử tại nước Úc, hệ thống hầm ngầm của Wombat đã trở thành pháo đài cứu mạng cho hàng ngàn sinh vật bé nhỏ!". Bố cục: Đồ họa mặt cắt lòng đất: ngọn lửa cháy dữ dội trên mặt đất nhưng dưới đường hầm của chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường, nhiệt độ mát mẻ an toàn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L318</summary>

```text
HÌNH L318 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chim chóc, thú có túi nhỏ, thằn lằn và ếch nhái đều chạy vào nương náu trong các ngóc ngách hầm Wombat mát mẻ với nhiệt độ luôn duy trì ổn định 20°C!". Bố cục: Các loài thú nhỏ nép mình trong ngách hầm của chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường, bình yên thoát khỏi biển lửa thiêu rụi trên mặt đất; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L319</summary>

```text
HÌNH L319 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Wombat không hề xua đuổi những kẻ tị nạn bất đắc dĩ, chúng hào hiệp chia sẻ lãnh thổ ngầm, trở thành người hùng cứu sinh thầm lặng của châu Úc hoang dã!". Bố cục: chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường gật đầu thân thiện chia sẻ đường hầm cho các bạn nhỏ tị nạn, ánh mắt ấm áp tình đồng loại; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Mười tuyển thủ lần lượt bước lên đĩa cân kiểm tra thể trọng dưới sự giám sát chặt chẽ của các trọng tài thú y quốc tế!". Bố cục: Nhân viên kỹ thuật cầm bảng kẹp tài liệu kiểm tra trọng lượng từng đấu sĩ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L320</summary>

```text
HÌNH L320 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Ban giám khảo xin tuyên bố kết quả Vòng sáu! Huy chương Đồng thuộc về Cá Mút Đá Hagfish với vai trò dọn sạch xác cá đáy vực sâu!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ búa, trao huy chương đồng phát sáng cho chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện.
```
</details>

<details><summary>L321</summary>

```text
HÌNH L321 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Huy chương Bạc thuộc về kỹ sư Hải Ly với bẫy carbon và chiếc nôi nâng đỡ đa dạng sinh thái!". Bố cục: chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo vui mừng đón nhận tấm huy chương bạc lấp lánh thứ hai.
```
</details>

<details><summary>L322</summary>

```text
HÌNH L322 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và Huy chương Vàng ba điểm vô cùng xứng đáng thuộc về chiếc máy hút bụi bảo vệ rạn san hô: Hải Sâm!". Bố cục: chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù xúc động đeo chiếc huy chương vàng đầu tiên của mình, cả đấu trường reo hò chúc mừng nồng nhiệt.
```
</details>

<details><summary>L323</summary>

```text
HÌNH L323 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Bảng điểm sau sáu vòng đấu cực kỳ gay cấn và biến ảo: Hải Ly vươn lên đồng hạng sáu điểm cùng Wombat! Sứa Bất Tử và Axolotl bám sát với năm điểm! Hải Sâm bứt phá ngoạn mục lên ba điểm!". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) cập nhật: Hải Ly 6 điểm, Wombat 5 điểm, Sứa Bất Tử 5 điểm, Axolotl 5 điểm, Chuột Chũi Sao 3 điểm, Hải Sâm 3 điểm, Hagfish 3 điểm, Bạch Tuộc Mimic 2 điểm, Ếch dị nhân móng vuốt hoạt hình đáng yêu 2 điểm, Kiến Nổ 1 điểm; bảng tổng sắp sít sao chưa từng thấy!
```
</details>

<details><summary>L324</summary>

```text
HÌNH L324 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Trước khi bước vào hai vòng đấu cuối cùng, ban tổ chức xin trân trọng giới thiệu: Lễ Trao Giải Phụ Đặc Biệt — Tri Ân Các Cụ Tổ Cổ Đại và Tổ Tiên Khổng Lồ!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng bước lên thảm đỏ nhung, hai bên là các tượng đài đá hóa thạch cổ đại sừng sững; tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) hiện chữ giải thưởng danh dự hoạt hình.
```
</details>

<details><summary>L325</summary>

```text
HÌNH L325 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Để có mặt trên sàn đấu Mùa 3 ngày hôm nay, mười dòng giống dị nhân đã phải trải qua hàng trăm triệu năm đấu tranh sinh tồn trước thiên thạch và các kỷ băng hà khốc liệt!". Bố cục: Màn hình chiếu cảnh Trái Đất kỷ Than Đá và kỷ Băng Hà với các quái thú cổ đại khổng lồ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L326</summary>

```text
HÌNH L326 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Những mẫu hóa thạch khai quật từ các tầng địa chất sâu thẳm đã chứng minh: các dị nhân của chúng ta từng sở hữu những phiên bản tổ tiên hoành tráng đến mức khó tin!". Bố cục: Nhà cổ sinh vật học hoạt hình cầm búa địa chất gõ vào vách đá lộ ra các bộ xương hóa thạch phát sáng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L327</summary>

```text
HÌNH L327 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tấm cúp danh dự đầu tiên thuộc về cụ tổ không xương sống: Cá Mút Đá Hagfish!". Bố cục: chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện bơi lên bục danh dự, bên cạnh là một phiến đá hóa thạch ba trăm triệu năm tuổi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L328</summary>

```text
HÌNH L328 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "2019, các nhà cổ sinh vật học tại Canada đã phát hiện hóa thạch của loài Tethymyxine có niên đại 300 triệu năm từ kỷ Than Đá!". Bố cục: Cận cảnh phiến đá hóa thạch Tethymyxine ba trăm triệu năm tuổi hiện rõ từng đường nét thân trơn và tuyến chất nhầy; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L329</summary>

```text
HÌNH L329 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Điều kinh ngạc là cấu trúc cơ thể của Hagfish 300 triệu năm trước giống hệt với Hagfish đang bơi lội ngày hôm nay!". Bố cục: Hình ảnh so sánh hóa thạch 300 triệu năm và chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện hiện đại: không hề có sự thay đổi lớn nào; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chiến xa Wombat bước lên đầu tiên! Rầm! 35kg cơ bắp chắc nịch đè nặng mặt cân thép! Tuyển thủ hạng nặng số một của đại hội!". Bố cục: chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường đứng lên bàn cân, kim đồng hồ điện tử nhảy vọt lên con số 35kg; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L330</summary>

```text
HÌNH L330 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chúng đã sống sót qua bốn cuộc đại tuyệt chủng hàng loạt của Trái Đất, chứng kiến loài khủng long bạo chúa T-Rex xuất hiện rồi biến mất hoàn toàn, trong khi Hagfish vẫn ung dung thắt nút thân số tám dưới đáy biển!". Bố cục: Khủng long T-Rex gầm rú rồi hóa thạch dưới lòng đất, còn chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện bơi tung tăng dưới đáy biển sâu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L331</summary>

```text
HÌNH L331 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chưa hết, Hagfish sở hữu tới 4 quả tim độc lập rải rác khắp cơ thể: một tim chính và ba tim phụ tự đập hàng giờ mà không cần oxy từ não bộ!". Bố cục: Sơ đồ giải phẫu 4 quả tim hoạt hình phát sáng nhịp nhàng dọc thân mình; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L332</summary>

```text
HÌNH L332 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Hệ tuần hoàn phụ này giúp chúng sống sót ngon lành trong những vùng nước đáy biển thiếu oxy đến mức mọi loài cá có xương sống khác đều phải ngạt thở bỏ mạng!". Bố cục: Đàn cá thông thường nổi bụng vì thiếu oxy, trong khi chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện vẫn khoan thai bơi lượn nhờ 4 quả tim độc lập; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L333</summary>

```text
HÌNH L333 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Một cỗ máy sinh học bất tử trước thời gian! Cả hội trường đồng loạt cúi đầu kính cẩn chào cụ tổ Hagfish!". Bố cục: Khán giả và anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cùng cúi mình chào kính phục; chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện ngoe nguẩy chiếc đuôi đáp lễ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L334</summary>

```text
HÌNH L334 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nhưng hãy nhìn sang tổ tiên của hai gã thợ mộc và đào hầm: Hải Ly và Wombat! Họ từng sở hữu những phiên bản quái thú khổng lồ khiến ai nhìn cũng phải khiếp sợ!". Bố cục: Bức màn nhung kéo lên để lộ hai bộ xương hóa thạch khổng lồ cao sừng sững; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L335</summary>

```text
HÌNH L335 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Trong kỷ băng hà Bắc Mỹ cách đây 10.000 năm, tổ tiên của Hải Ly là loài Castoroides nặng tới 100kg, to lớn ngang ngửa một chú gấu đen khổng lồ!". Bố cục: Hình vẽ phục dựng Castoroides to lớn sừng sững, hai chiếc răng cửa cong vút dài mười lăm xăng-ti-mét; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L336</summary>

```text
HÌNH L336 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tuy nhiên, điều bi hài là chú hải ly khổng lồ này lại không biết xây đập và chỉ thích ăn cỏ dại dưới nước, nên đã bị tuyệt chủng khi khí hậu biến đổi!". Bố cục: Chú hải ly 100kg ngồi ngơ ngác ăn cỏ, trong khi chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo hiện đại thông minh biết đắp đập gỗ sinh tồn mãnh liệt; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L337</summary>

```text
HÌNH L337 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Còn ở nước Úc, tổ tiên của Wombat là loài quái thú Diprotodon: loài thú có túi lớn nhất từng bước đi trên Trái Đất, nặng tới gần ba tấn và dài hơn 3m!". Bố cục: Phục dựng quái thú Diprotodon to như chiếc xe tải thế giới tự nhiên, bước đi rung chuyển mặt đất cổ đại Úc; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L338</summary>

```text
HÌNH L338 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chiếc mông bọc thép của Wombat ngày nay chính là di sản thu nhỏ được kế thừa từ cỗ xe tăng bọc thép Diprotodon ba tấn thời tiền sử!". Bố cục: chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường đứng cạnh chiếc bóng khổng lồ của Diprotodon vỗ mông đầy tự hào; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L339</summary>

```text
HÌNH L339 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và giải thưởng danh dự cuối cùng thuộc về dòng dõi của Hải Sâm: sinh vật đã có mặt trên Trái Đất từ kỷ Cambri cách đây hơn 500 triệu năm!". Bố cục: Đồ họa biển kỷ Cambri 500 triệu năm trước rực rỡ sắc màu sinh vật cổ sơ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tiếp theo là kỹ sư Hải Ly: 25kg lông dày và cơ hàm sắt thép, sẵn sàng cho mọi cuộc đọ sức thể lực!". Bố cục: chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo ngồi nghiêm túc lên cân, màn hình điện tử hiện số 25kg, tay vẫn cầm chắc thanh gỗ đo đạc; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L340</summary>

```text
HÌNH L340 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "500 triệu năm trước, khi sinh vật trên cạn còn chưa kịp hình thành, tổ tiên của Hải Sâm đã cặm cụi hút bụi lọc sạch cát biển cho hành tinh chúng ta!". Bố cục: chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù đứng trên bục danh dự nhận chiếc cúp vàng vinh quang hình hóa thạch cổ đại; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L341</summary>

```text
HÌNH L341 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Họ đã chứng kiến sự thăng trầm của hàng vạn loài sinh vật, bình thản vượt qua mọi biến cố địa chất vĩ đại bằng triết lý lầy lội không xương sống của mình!". Bố cục: Hình ảnh Trái Đất xoay vần qua các kỷ địa chất, chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù vẫn ung dung trườn dưới đáy biển xanh mát; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L342</summary>

```text
HÌNH L342 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và nhìn vào cây phả hệ của Sứa Bất Tử, dòng giống ruột khoang Cnidaria của chúng thậm chí đã xuất hiện từ kỷ Ediacara cách đây hơn 600 triệu năm!". Bố cục: Đồ họa biển kỷ Ediacara nguyên thủy 600 triệu năm trước với các sinh vật thân mềm phát quang ma thuật; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L343</summary>

```text
HÌNH L343 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "600 triệu năm trước, khi Trái Đất chỉ là một quả cầu băng tuyết lạnh giá bao phủ khắp các đại dương, tổ tiên của loài sứa đã trôi dạt lơ lửng dưới lớp băng dày!". Bố cục: Đàn sứa cổ xưa bơi lội dưới mái vòm băng tuyết nguyên thủy của Trái Đất cổ đại; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L344</summary>

```text
HÌNH L344 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Họ đã vượt qua cuộc đại tuyệt chủng Permi-Triat thảm khốc nhất lịch sử khi 95% phần trăm sinh vật biển bị quét sạch hoàn toàn!". Bố cục: Biển cả ngập tràn tro bụi núi lửa và axit, nhưng dòng dõi sứa vẫn bền bỉ hồi sinh và trường tồn tới tận ngày nay; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L345</summary>

```text
HÌNH L345 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Sự trường sinh của Sứa Bất Tử không chỉ nằm ở từng cá thể, mà là sự kiên cường của cả một dòng dõi cổ xưa bậc nhất hành tinh!". Bố cục: chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực trôi lơ lửng trên bục danh dự, ánh sáng hào quang tỏa ra như ngôi sao cổ đại lấp lánh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L346</summary>

```text
HÌNH L346 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Còn nhìn về phả hệ của Kỳ Nhông Axolotl, chúng là hậu duệ trực tiếp của nhóm lưỡng cư cổ đại Temnospondyli từng thống trị Trái Đất từ 300 triệu năm trước!". Bố cục: Phục dựng quái thú lưỡng cư cổ đại Temnospondyli dài hai mét với chiếc đầu dẹt to bản và hàm răng sắc bén; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L347</summary>

```text
HÌNH L347 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Vào thời kỳ khủng long còn chưa xuất hiện, những cụ tổ lưỡng cư khổng lồ này đã làm chủ các đầm lầy than đá bằng khả năng tái sinh chi và thích nghi môi trường nước ngọt đỉnh cao!". Bố cục: Chú lưỡng cư khổng lồ bơi lội săn cá trong đầm lầy kỷ Than Đá nguyên sơ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L348</summary>

```text
HÌNH L348 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Trải qua hàng trăm triệu năm tiến hóa thu nhỏ lại thành chú kỳ nhông 70 gam xinh xắn, Axolotl vẫn lưu giữ trọn vẹn chiếc chìa khóa tái sinh cổ đại của tổ tiên mình!". Bố cục: Chú kỳ nhông chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói nhỏ bé đứng cạnh chiếc bóng vĩ đại của cụ tổ Temnospondyli mỉm cười tự hào; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L349</summary>

```text
HÌNH L349 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Thậm chí trong các lớp đá trầm tích kỷ Than Đá, người ta còn tìm thấy những dấu vết hóa thạch của chất keo nhớt Hagfish được bảo tồn nguyên vẹn qua 300 triệu năm thời gian!". Bố cục: Phiến đá cổ đại hiển thị vệt hóa thạch của sợi tơ nhớt protein nguyên thủy phát sáng huỳnh quang; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nhóm hạng trung gồm Cá Mút Đá Hagfish nặng một ký, Hải Sâm nửa ký, và Bạch Tuộc Mimic 300 gam uốn lượn trên đĩa cân thủy tinh!". Bố cục: Ba chiếc cân đặt cạnh nhau: chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện trườn trên cân 1kg, chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù nằm ườn 500g, chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình cuộn 8 xúc tu 300g; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L350</summary>

```text
HÌNH L350 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Điều này chứng minh rằng công thức phân tử của sợi tơ protein Hagfish hoàn hảo đến mức mẹ thiên nhiên không cần phải chỉnh sửa hay nâng cấp thêm bất kỳ chi tiết nào suốt 300 triệu năm qua!". Bố cục: Hình ảnh cụ tổ chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện bơi qua thời gian từ quá khứ đến hiện tại với vẹn nguyên sức mạnh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L351</summary>

```text
HÌNH L351 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Không chỉ vậy, Cá Mút Đá Hagfish còn có thể sống sót kỳ diệu suốt 36 giờ trong môi trường hoàn toàn không có khí oxy dưới lớp bùn đáy biển sâu!". Bố cục: Mô hình chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện vùi sâu trong lớp bùn đen kịt thiếu oxy nhưng tim vẫn đập chậm rãi bền bỉ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L352</summary>

```text
HÌNH L352 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chúng chuyển hóa lượng đường glycogen dự trữ trong các mô cơ mà không cần oxy, giữ cho 4 quả tim vẫn hoạt động nhịp nhàng qua cơn thiếu thốn!". Bố cục: Đồ họa chu trình đường phân kỵ khí thắp sáng bốn quả tim của chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện dưới đáy vực sâu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L353</summary>

```text
HÌNH L353 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Đó là minh chứng cho sức sống bền bỉ đã giúp Hagfish vượt qua năm đại tuyệt chủng lớn nhất của lịch sử Trái Đất mà không cần biến đổi hình dạng!". Bố cục: Mô hình dòng thời gian năm đại tuyệt chủng lướt qua, chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện vẫn ung dung bơi lội từ thời kỷ Cambri đến nay; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L354</summary>

```text
HÌNH L354 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Ban tổ chức xin trao tặng Cúp Vinh Danh Cổ Vật Sống Danh Dự cho Cá Mút Đá Hagfish và Hải Sâm! Một tràng pháo tay cho sự trường tồn vĩ đại của muôn loài!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao hai chiếc cúp đá cẩm thạch phát sáng cho chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện và chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù trong tiếng vỗ tay rền vang.
```
</details>

<details><summary>L355</summary>

```text
HÌNH L355 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Lễ trao giải phụ khép lại trong niềm tự hào vô bờ bến! Bây giờ, hãy hít một hơi thật sâu vì chúng ta sắp bước vào Vòng bảy: Phúc Khảo Tin Đồn Thế Kỷ!". Bố cục: Đèn sân khấu chuyển sang màu xanh neon bí ẩn, chuẩn bị cho những màn bẻ lái sự thật ngoạn mục; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L356</summary>

```text
HÌNH L356 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Đèn sân khấu đổi màu rực rỡ! Chào mừng quý vị đến với Vòng bảy: Phúc Khảo Tin Đồn Thế Kỷ và Đập Tan Những Lầm Tưởng!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng bước ra giữa sàn đấu, phía sau là màn hình lớn chiếu biểu tượng chiếc kính lúp vạch trần tin giả; tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng ô thử thách số bảy.
```
</details>

<details><summary>L357</summary>

```text
HÌNH L357 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Đây là vòng thi nơi ban giám khảo sẽ đưa ra hàng loạt tin đồn nổi tiếng trên mạng xã hội về mười tuyển thủ để đối chất bằng khoa học thực nghiệm!". Bố cục: Màn hình hiện lên các bài báo mạng giật gân hoạt hình với dấu chấm hỏi to đùng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L358</summary>

```text
HÌNH L358 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Trong thời đại thông tin bùng nổ, nhiều sinh vật bị đồn thổi thành những vị thần bất khả chiến bại hoặc bị gán cho những thói quen ăn uống hoàn toàn sai lệch!". Bố cục: Hình ảnh biểu tượng tin giả mạng xã hội bị một chiếc búa công lý gõ vỡ tan tành; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L359</summary>

```text
HÌNH L359 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tin đồn số một: Sứa Bất Tử là sinh vật trường sinh bất lão tuyệt đối, không có bất kỳ thứ gì trên đời có thể tiêu diệt được chúng?!". Bố cục: Hình ảnh một chú sứa phát hào quang bất tử lơ lửng giữa vũ trụ như vị thần bất khả chiến bại; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Ếch dị nhân móng vuốt hoạt hình đáng yêu nặng 80 gam, Kỳ Nhông Axolotl 70 gam, và Chuột Chũi Mũi Sao vỏn vẹn 50 gam!". Bố cục: Ba tuyển thủ tí hon đứng trên cân phân tích chính xác: chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng, chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói và chú Chuột Chũi Mũi Sao hoạt hình lông đen nhung mượt mà, mũi xòe ra 22 xúc tu đỏ hồng như bông hoa sao biển, đeo kính râm mù lòa nhưng phản xạ siêu thanh nhìn nhau đầy thách thức; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L360</summary>

```text
HÌNH L360 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Sự thật khoa học là gì? Bà Cú giám khảo lập tức gõ búa đính chính: Sứa Bất Tử chỉ bất tử về mặt lão hóa sinh học tự nhiên mà thôi!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ búa, hình ảnh thần thánh biến mất, thay bằng thực tế đại dương khắc nghiệt; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L361</summary>

```text
HÌNH L361 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Trong môi trường biển khơi, kích thước chỉ 4,5mm biến chúng thành món tráng miệng khoái khẩu tuyệt vời cho rùa biển, cá mặt trăng và các loài sứa lớn khác!". Bố cục: Một chú rùa biển hoạt hình bơi qua hả miệng đớp trọn cả đàn sứa nhỏ như nuốt kẹo thạch ngon lành; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L362</summary>

```text
HÌNH L362 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Hơn nữa, nếu gặp một đợt sóng thần đánh dạt lên bãi cát khô nóng hoặc bị nhiễm khuẩn nấm đại dương, chú sứa bất tử này vẫn sẽ hóa thành một vũng nước khô queo trên bờ biển!". Bố cục: Chú sứa nằm trên bãi cát nắng gắt rên rỉ, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vội cầm bình xịt tưới nước giải cứu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L363</summary>

```text
HÌNH L363 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khái niệm bất tử ở đây là không chết vì tuổi già, chứ không phải là mình đồng da sắt chống lại kẻ săn mồi!". Bố cục: chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực cười trừ gãi đầu công nhận sự thật trần trụi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L364</summary>

```text
HÌNH L364 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nếu không có chuỗi thức ăn kiểm soát số lượng, chỉ sau vài năm loài sứa bất tử này có thể nhân bản tràn ngập mọi đại dương trên Trái Đất!". Bố cục: Đồ họa biển ngập tràn sứa nhỏ lấp lánh để minh họa tầm quan trọng của rùa biển trong việc cân bằng sinh thái; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L365</summary>

```text
HÌNH L365 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Một pha bẻ lái định nghĩa khoa học cực kỳ chuẩn xác! Tiếp tục với tin đồn số hai: Hải Ly là loài động vật kỳ quặc thích ăn gỗ mục để sống?!". Bố cục: Hình ảnh chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo ngồi gặm một khúc gỗ khô cứng ngắc như nhai bánh quy giòn tan; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L366</summary>

```text
HÌNH L366 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Đây là một sự hiểu lầm tai hại lớn nhất về loài Hải Ly! Đường ruột của Hải Ly hoàn toàn không thể tiêu hóa được phần gỗ lõi cứng chắc của thân cây!". Bố cục: Sơ đồ đường ruột của chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo: khúc gỗ lõi cứng bị chặn lại ở dạ dày không tiêu hóa được; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L367</summary>

```text
HÌNH L367 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khẩu phần ăn thật sự của chúng là lớp mô mềm màu xanh giàu đường và dinh dưỡng nằm ngay sát dưới lớp vỏ cây, cùng với chồi non và lá cây tươi!". Bố cục: chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo khéo léo dùng răng bóc tách lớp vỏ xanh non mềm mại ăn ngon lành, bỏ lại phần lõi gỗ cứng sang một bên; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L368</summary>

```text
HÌNH L368 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Những khúc gỗ cứng cáp bị đốn ngã chỉ được Hải Ly tận dụng làm vật liệu xây dựng con đập kiên cố ngăn dòng nước lũ, chứ không phải thức ăn trong thực đơn hàng ngày!". Bố cục: chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo vác khúc gỗ cứng xếp vào thân đập, tay kia cầm cành lá xanh nhai nhóp nhép khoái chí; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L369</summary>

```text
HÌNH L369 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chúng ta đã oan uổng gán cho Hải Ly cái mác thèm ăn gỗ suốt hàng thế kỷ qua, trong khi chúng chỉ là những người sành ăn vỏ cây dinh dưỡng!". Bố cục: chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo ôm bụng cười, tay giơ đĩa thức ăn gồm chồi non và lá cây xanh mướt; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và đỉnh điểm chênh lệch: Kiến Nổ chỉ nặng 0,5 miligram, còn Sứa Bất Tử chỉ nặng đúng 1 miligram bé như hạt bụi nước!". Bố cục: Bảng so sánh đồ họa: một bên là chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường khổng lồ như xe bọc thép, một bên là chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực chỉ là chấm sáng li ti; nhân viên kỹ thuật há hốc mồm kinh ngạc; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L370</summary>

```text
HÌNH L370 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Đến tin đồn số ba: Ếch dị nhân móng vuốt hoạt hình đáng yêu tự bẻ xương xuyên qua thịt chân như vậy thì có cảm thấy đau đớn đến thấu xương hay không?". Bố cục: chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng giơ ngón chân có vuốt xương lên, biểu cảm suy tư bí hiểm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L371</summary>

```text
HÌNH L371 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Các nhà thần kinh học động vật xác nhận: loài ếch này có đầy đủ các thụ thể cảm nhận đau đớn nociceptor dưới da!". Bố cục: Đồ họa xung thần kinh cảm giác đau chạy dọc từ ngón chân lên não bộ của ếch; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L372</summary>

```text
HÌNH L372 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tuy nhiên, trong khoảnh khắc cận kề cái chết trước kẻ thù, tuyến thượng thận của chúng lập tức giải phóng một lượng khổng lồ hormone adrenaline và các peptit giảm đau nội sinh!". Bố cục: Dòng hormone phát sáng tràn ngập cơ thể, khóa chặt các cổng tiếp nhận tín hiệu đau ở tủy sống; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L373</summary>

```text
HÌNH L373 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Cơ chế này tạm thời gây tê liệt cảm giác đau đớn cục bộ, giúp chú ếch tập trung trọn vẹn 100% sức lực để tung đòn móng vuốt sinh tử hạ gục kẻ săn mồi!". Bố cục: chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng tung cú đá vuốt xương uy lực hạ gục con rắn săn mồi trong sự thán phục của khán giả; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L374</summary>

```text
HÌNH L374 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và sau khi hiểm nguy qua đi, cảm giác ê ẩm xuất hiện chính là tín hiệu kích hoạt chu trình tiết dịch kháng khuẩn làm lành mô da thần tốc!". Bố cục: Vết thương khép miệng, chú ếch ngồi nghỉ ngơi dưới bóng râm dòng suối bình yên; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L375</summary>

```text
HÌNH L375 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Thêm một tin đồn nổi tiếng khác về Bạch Tuộc Mimic: liệu chúng có thật sự nhận thức được mình đang bắt chước loài nào hay chỉ là phản xạ đổi màu ngẫu nhiên?". Bố cục: chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình đứng trước màn hình đối chất, xung quanh là các nhà khoa học đang theo dõi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L376</summary>

```text
HÌNH L376 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Các thí nghiệm của tiến sĩ Mark Norman tại Indonesia đã chứng minh: Bạch Tuộc Mimic sở hữu trí nhớ thị giác và tư duy phân tích chiến thuật đỉnh cao!". Bố cục: Phòng thí nghiệm đại dương: khi thả một con cá bơn săn mồi vào, chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình không đổi màu ngẫu nhiên mà lập tức biến hình thành rắn biển đầu đen chuyên ăn thịt cá bơn! KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L377</summary>

```text
HÌNH L377 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chúng quan sát chính xác đối thủ đang tiếp cận là ai, nhớ lại kẻ thù tự nhiên của đối thủ đó trong tự nhiên, rồi mới quyết định hóa thân thành loài khắc chế phù hợp nhất!". Bố cục: Sơ đồ tư duy logic của bạch tuộc: nhận diện đối thủ -> tra cứu hồ sơ khắc tinh -> kích hoạt hệ cơ biến hình chuẩn xác; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L378</summary>

```text
HÌNH L378 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Một sự tính toán chiến thuật hoàn toàn chủ động chứ không hề là phản xạ vô thức may rủi! Cả khán đài gật gù khâm phục trí tuệ loài động vật thân mềm!". Bố cục: chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình giơ một xúc tu nháy mắt chào khán giả đầy tinh tế; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L379</summary>

```text
HÌNH L379 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và một tin đồn thú vị khác về Gấu Wombat: có phải chúng dùng hai chân sau để nặn phân thành hình khối lập phương hay không?". Bố cục: Hình ảnh hoạt hình hài hước: chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường ngồi nặn phân như nặn bánh bột lọc bằng hai tay; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Gấu Wombat nặng gấp... 35 triệu lần Sứa Bất Tử! Chiếc máy tính của ban tổ chức suýt bốc khói vì tỷ lệ lệch pha này!". Bố cục: Kỹ thuật viên ôm đầu trước màn hình máy tính hoạt hình hiện biểu tượng bốc khói quá tải dữ liệu; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cười lớn vỗ tay.
```
</details>

<details><summary>L380</summary>

```text
HÌNH L380 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Bà Cú giám khảo cười lớn đính chính: hoàn toàn không phải do nặn bằng tay hay chân! Đó là 100% kết quả của cơ chế thủy lực và áp suất đường ruột tự nhiên!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ giơ biểu đồ động lực học chất lưu giải thích cơ chế ép góc 90 độ của các múi cơ ruột già; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L381</summary>

```text
HÌNH L381 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Phân của Wombat đi vào đoạn ruột già ở thể lỏng sệt, và qua quá trình hút nước cực mạnh kết hợp lực co bóp đàn hồi không đều, chúng tự động đông cứng thành các khối hộp vuông vức hoàn hảo trước khi ra ngoài!". Bố cục: Đồ họa ruột co bóp nén ép tự động nhả ra từng viên gạch phân lập phương vuông chằn chặn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L382</summary>

```text
HÌNH L382 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và sự thật về chiếc móng vuốt của Ếch dị nhân móng vuốt hoạt hình đáng yêu: xương ngón chân tự bẻ gãy không hề làm đứt gãy mạch nước màu lớn hay gây hoại tử nhờ một lớp vỏ bọc collagen dạng sợi cực kỳ dẻo dai!". Bố cục: Đồ họa bàn chân sau của ếch: bao xơ collagen co giãn nhẹ nhàng ôm lấy đầu xương nhọn bảo vệ tế bào mô; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L383</summary>

```text
HÌNH L383 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khi móng vuốt thụt vào, lớp vỏ này đóng vai trò như một chiếc băng gạc sinh học ép chặt vết rách, ngăn chặn nước màu chảy và kích thích tế bào biểu mô phân chia thần tốc!". Bố cục: Vết rách khép miệng nhanh như một chiếc khóa kéo tự động kéo lại mượt mà; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L384</summary>

```text
HÌNH L384 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Viện nghiên cứu sinh học quốc tế cũng xác nhận: chất nhầy của Hagfish khi sấy khô có thể dệt thành sợi tơ nhân tạo bền gấp 10 lần sợi nylon tổng hợp!". Bố cục: Cuộn tơ dệt từ protein chất nhầy chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện sáng bóng, mảnh mai nhưng bền chắc nâng được vật nặng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L385</summary>

```text
HÌNH L385 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Sợi tơ sinh học này có khả năng tự phân hủy hoàn toàn trong môi trường tự nhiên, mở ra cuộc cách mạng thời trang xanh không rác thải nhựa!". Bố cục: Sợi vải sinh thái tan biến nhẹ nhàng trong đất bón cho cây non xanh tốt; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L386</summary>

```text
HÌNH L386 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Thiên nhiên đã trao tặng cho những dị nhân này những giải pháp sinh học đi trước công nghệ con người hàng trăm triệu năm!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vung tay chỉ lên màn hình so sánh giữa công nghệ hiện đại và cấu trúc sinh học tuyệt mỹ của các sinh vật; tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng rực các dữ liệu khoa học.
```
</details>

<details><summary>L387</summary>

```text
HÌNH L387 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Ban giám khảo xin công bố kết quả Vòng bảy! Huy chương Đồng thuộc về Kỳ Nhông Axolotl với bí ẩn trạng thái ấu trùng neoteny suốt đời!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ búa trao huy chương đồng cho chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói.
```
</details>

<details><summary>L388</summary>

```text
HÌNH L388 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Huy chương Bạc thuộc về kỹ sư Hải Ly với lời minh oan đanh thép cho khẩu phần ăn vỏ cây dinh dưỡng!". Bố cục: chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo nhận tấm huy chương bạc thứ ba của mình trong tiếng reo hò.
```
</details>

<details><summary>L389</summary>

```text
HÌNH L389 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và Huy chương Vàng ba điểm xuất sắc thuộc về Sứa Bất Tử với bài học phân biệt giữa bất tử sinh học và chuỗi thức ăn đại dương!". Bố cục: chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực bay lượn đón nhận chiếc huy chương vàng thứ hai, tỏa ánh hào quang hồng tím rực rỡ.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Sự chênh lệch khủng khiếp giữa cỗ xe bọc thép 30 lăm ký và chú sứa 1 miligram lập tức thổi bùng lên các cuộc tranh cãi nảy lửa khắp khán đài!". Bố cục: Khán giả chia thành hai phe cãi nhau chí chóe: phe ủng hộ cơ bắp khổng lồ và phe đặt cược vào siêu năng lực vi mô; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L390</summary>

```text
HÌNH L390 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Bảng tổng sắp sau bảy vòng đấu chính thức đã chứng kiến sự bứt phá ngoạn mục: Sứa Bất Tử và Hải Ly cùng dẫn đầu với tám điểm! Gấu Wombat bám sát với năm điểm! Axolotl sáu điểm!". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) cập nhật điểm số: Sứa Bất Tử 8 điểm, Hải Ly 8 điểm, Axolotl 6 điểm, Wombat 5 điểm, Hải Sâm 3 điểm, Chuột Chũi Sao 3 điểm, Hagfish 3 điểm, Bạch Tuộc Mimic 2 điểm, Ếch dị nhân móng vuốt hoạt hình đáng yêu 2 điểm, Kiến Nổ 1 điểm; cuộc soán ngôi vương đang đến hồi nghẹt thở nhất!
```
</details>

<details><summary>L391</summary>

```text
HÌNH L391 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Căng thẳng tột cùng! Chào mừng quý vị đến với Vòng Bán Kết: Soi Kính Hiển Vi Điện Tử và Máy Gia Tốc Hạt Đồng Bộ!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng khoác áo blouse trắng của nhà khoa học, dẫn đầu đoàn giám khảo bước vào phòng thí nghiệm tối tân với các máy móc lượng tử phát sáng; tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng ô bán kết mang hình kính hiển vi.
```
</details>

<details><summary>L392</summary>

```text
HÌNH L392 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Đây là vòng thi nơi khoa học đỉnh cao của con người dùng các thiết bị đắt giá hàng triệu đô la để vén màn những kết cấu vật liệu vi mô không tưởng!". Bố cục: Màn hình lớn kết nối trực tiếp với kính hiển vi điện tử quét và máy quét synchrotron; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L393</summary>

```text
HÌNH L393 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Những bí mật cấu trúc tinh thể nano ẩn sâu trong tế bào các dị nhân chính là nguồn cảm hứng vô tận cho cuộc cách mạng công nghệ tương lai!". Bố cục: Đồ họa mạng lưới tinh thể phân tử chuyển động quay ba chiều sắc nét; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L394</summary>

```text
HÌNH L394 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Mẫu thử nghiệm đầu tiên được đưa vào buồng chân không: sợi tơ nhớt protein của Cá Mút Đá Hagfish!". Bố cục: Kỹ thuật viên dùng kẹp gắp một sợi tơ trong suốt của chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện đặt lên đĩa soi điện tử; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L395</summary>

```text
HÌNH L395 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Dưới chùm tia X cực mạnh của máy gia tốc hạt, các nhà nghiên cứu vật liệu tại đại học Guelph đã phát hiện ra cấu trúc tinh thể siêu việt của sợi tơ này!". Bố cục: Đồ họa nguyên tử phóng to: các chuỗi protein cuộn xoắn thành các tấm gấp beta đan kết chéo vô cùng chặt chẽ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L396</summary>

```text
HÌNH L396 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Bên trong mỗi tế bào nhớt chứa một cuộn tơ dài tới 15cm nhưng được quấn tròn thành một viên nang nhỏ chỉ 100 micro-mét!". Bố cục: Cuộn tơ mở ra như chiếc lò xo nén cực đại bung ra thành mạng lưới sợi dày đặc trong nước; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L397</summary>

```text
HÌNH L397 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khi bung ra trong nước biển, các chuỗi axit amin kỵ nước lập tức hút chặt lấy nhau, biến thể lỏng thành thể gel siêu đàn hồi có thể kéo dài gấp 3 lần mà không hề bị đứt gãy!". Bố cục: Cánh tay robot kéo giãn sợi tơ ra gấp ba lần độ dài ban đầu rồi thả ra, sợi tơ co lại đàn hồi hoàn hảo; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L398</summary>

```text
HÌNH L398 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Độ bền kéo của sợi tơ này đạt mức 100 80 megapascal, tương đương với độ bền của các sợi gân nhân tạo tốt nhất mà con người từng chế tạo!". Bố cục: Đồ thị đo lực kéo đứt: đường cong của tơ Hagfish vượt xa sợi nylon và tiệm cận độ dai của hợp kim nhẹ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L399</summary>

```text
HÌNH L399 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Một kỳ quan công nghệ nano của biển sâu có tuổi đời 300 triệu năm! Cả hội trường vỗ tay rầm rộ!". Bố cục: Các nhà khoa học hoạt hình giơ ngón tay cái tán thưởng trước số liệu hiển thị trên màn hình; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng mỉm cười thán phục.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Sau lễ cân ký, bảng dự đoán ban đầu nghiêng hẳn về hai gã cơ bắp Wombat và Hải Ly cùng sát thủ móng vuốt Ếch dị nhân móng vuốt hoạt hình đáng yêu!". Bố cục: Màn hình chiếu cột dự đoán: các cột cao vút gắn hình đầu chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường, chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo, chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng sáng rực trên bục hạt giống vô địch; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L400</summary>

```text
HÌNH L400 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tiếp theo, hãy đưa lớp da của Hải Sâm vào máy thử nghiệm cơ học biến dạng!". Bố cục: Một mẩu mô da của chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù được đặt vào máy đo lực nén và độ đàn hồi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L401</summary>

```text
HÌNH L401 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Các nhà sinh học phát hiện: da của Hải Sâm được cấu tạo từ một loại mô liên kết biến đổi đặc biệt gọi tắt là M-T-C!". Bố cục: Cấu trúc sợi collagen hoạt hình liên kết với nhau bằng các cầu nối hóa học màu xanh lá cây; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L402</summary>

```text
HÌNH L402 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Hải Sâm không hề sử dụng cơ bắp hay tiêu tốn năng lượng A-T-P để gồng cứng cơ thể như các loài động vật thông thường!". Bố cục: Đồ họa các hạt truyền tín hiệu thần kinh phóng thích vào mô liên kết; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L403</summary>

```text
HÌNH L403 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Thay vào đó, các tế bào thần kinh chỉ cần tiết ra một lượng nhỏ phân tử điều hòa để khóa chặt hoặc tháo rời các cầu nối giữa các sợi collagen trong vài trăm mili-giây!". Bố cục: Khi cần cứng, các cầu nối khóa chặt, mẩu da biến thành tảng đá cứng ngắc đập búa vào kêu keng keng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L404</summary>

```text
HÌNH L404 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và khi cần thoát thân qua khe đá hẹp, các cầu nối tự bung ra, toàn bộ cơ thể Hải Sâm hóa lỏng mềm nhũn như một khối thạch rau câu trôi tuột qua kẽ hở!". Bố cục: Cơ thể chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù mềm nhũn như giọt nước chảy luồn qua khe đá hẹp chỉ rộng một xăng-ti-mét rồi đông cứng trở lại; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L405</summary>

```text
HÌNH L405 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Các kỹ sư y sinh đang ứng dụng cơ chế hóa lỏng này để chế tạo các điện cực cấy ghép não bộ: mềm dẻo khi luồn vào mô não nhưng cứng cáp khi định vị chính xác!". Bố cục: Mô hình điện cực nano lấy cảm hứng từ da Hải Sâm cấy vào mô thần kinh một cách an toàn hoàn hảo; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L406</summary>

```text
HÌNH L406 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và cuối cùng là màn soi siêu vi cơ quan Eimer trên chiếc mũi sao của Chuột Chũi!". Bố cục: Đầu xúc tu hồng của chú Chuột Chũi Mũi Sao hoạt hình lông đen nhung mượt mà, mũi xòe ra 22 xúc tu đỏ hồng như bông hoa sao biển, đeo kính râm mù lòa nhưng phản xạ siêu thanh được phóng đại mười ngàn lần trên kính hiển vi điện tử quét; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L407</summary>

```text
HÌNH L407 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Mỗi chiếc nhú Eimer hình nấm tí hon chứa một cụm đầu dây thần kinh Merkel cực kỳ tinh vi, có thể nhận biết sự biến dạng bề mặt đất chỉ ở mức... một nanomet!". Bố cục: Mô hình nguyên tử: một hạt bụi nhỏ xíu chạm vào bề mặt nhú nấm làm phát ra xung điện thần kinh cực nhạy; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L408</summary>

```text
HÌNH L408 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Một nanomet nhỏ hơn cả đường kính của chuỗi xoắn kép D-N-A! Chuột Chũi Mũi Sao không chỉ sờ thấy con mồi, chúng sờ thấy cả kết cấu phân tử của đất!". Bố cục: chú Chuột Chũi Mũi Sao hoạt hình lông đen nhung mượt mà, mũi xòe ra 22 xúc tu đỏ hồng như bông hoa sao biển, đeo kính râm mù lòa nhưng phản xạ siêu thanh đeo kính râm nhếch mép ngầu, chiếc mũi sao biển phát ra các vòng sóng quét laser chính xác tuyệt đối; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L409</summary>

```text
HÌNH L409 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Để kiểm tra độ bền của chiếc mông bọc thép Wombat, ban giám khảo đã đưa tấm khiên sụn vào máy thử nghiệm búa tạ thủy lực công nghiệp!". Bố cục: Một chiếc búa đập thủy lực khổng lồ giáng thẳng xuống tấm giáp mẫu của chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường với lực ép lên tới hai tấn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Còn Sứa Bất Tử 1 miligram và Hải Sâm mềm nhũn? Giới chuyên môn ghi chú lạnh lùng: đề nghị mua sẵn bảo hiểm trọn gói!". Bố cục: Cột dự đoán thấp tè gắn hình chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực và chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù; chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù lắc đầu ngán ngẩm còn chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực nhấp nháy phát sáng kiêu hãnh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L410</summary>

```text
HÌNH L410 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Rầm! Chiếc búa nảy ngược trở lại trong khi lớp sụn mô mạc sợi của Wombat chỉ lún nhẹ xuống rồi lập tức đàn hồi trở lại hình dáng ban đầu không hề nứt vỡ!". Bố cục: Máy đo áp lực hiển thị chỉ số triệt tiêu lực đạt chín mươi lăm phần trăm, bảo vệ hoàn toàn bên trong cơ thể bên trong khỏi chấn thương; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L411</summary>

```text
HÌNH L411 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Các kỹ sư chế tạo xe hơi bọc thép và mũ bảo hiểm phi hành gia đang nghiên cứu cấu trúc sụn đan sợi này để phát triển vật liệu hấp thụ xung lực thế hệ mới!". Bố cục: Bản thiết kế mũ bảo hiểm công nghệ cao lấy cảm hứng từ cấu trúc mông bọc thép của chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L412</summary>

```text
HÌNH L412 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tại phòng thí nghiệm công nghệ sinh học, các nhà khoa học đã dùng protein phát quang xanh lá cây G-F-P để theo dõi đường đi của từng tế bào tái sinh trong cơ thể Axolotl!". Bố cục: Kính hiển vi huỳnh quang rọi vào mầm tái sinh của chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói: từng tế bào phát sáng xanh neon di chuyển dệt nên mô cơ mới; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L413</summary>

```text
HÌNH L413 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Họ phát hiện một tín hiệu điều khiển thần kỳ: các tế bào thần kinh ngoại biên liên tục phát ra dòng điện sinh học vi mô dẫn đường cho các tế bào cơ di chuyển chính xác đến từng micromet!". Bố cục: Dòng xung điện xanh lam chạy dọc sợi thần kinh chỉ đường cho các tế bào ghép nối hoàn hảo không một sai sót; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L414</summary>

```text
HÌNH L414 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Công nghệ lập bản đồ tế bào này đang mở ra hướng đi đột phá trong việc chế tạo các chi giả sinh học thông minh kết nối trực tiếp với não bộ con người!". Bố cục: Cánh tay robot công nghệ cao cử động nhịp nhàng theo ý nghĩ của con người trong phòng thử nghiệm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L415</summary>

```text
HÌNH L415 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Máy đo phổ tán xạ tia X còn cho thấy: các sợi tơ Hagfish có thể tự sắp xếp lại cấu trúc tinh thể khi chịu lực kéo giật đột ngột, biến lực kéo nguy hiểm thành nhiệt lượng khuếch tán ra môi trường nước!". Bố cục: Đồ thị phổ tán xạ tia X: các liên kết hydro tự sắp xếp lại hấp thụ trọn vẹn năng lượng va đập; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L416</summary>

```text
HÌNH L416 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khả năng hấp thụ xung lực tuyệt đỉnh này chính là chìa khóa vàng giúp chiếc bẫy nhớt Hagfish không bao giờ bị xé rách bởi những cú giãy giụa điên cuồng của cá mập săn mồi!". Bố cục: Con cá mập giãy giụa dữ dội trong khối keo nhớt nhưng màng tơ càng siết chặt đàn hồi không thể phá vỡ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L417</summary>

```text
HÌNH L417 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Cuộc chạm trán nảy lửa giữa công nghệ tái sinh của Axolotl và cơ chế đảo ngược thời gian của Sứa Bất Tử đã làm nổ tung cầu trường!". Bố cục: chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói và chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực cùng tỏa sáng trên hai cột năng lượng mô phỏng của phòng thí nghiệm tương lai; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L418</summary>

```text
HÌNH L418 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Một bên là khả năng mọc lại mô tạng thần tốc chỉ sau vài tuần ngắn ngủi, một bên là thuật chuyển hóa tế bào đưa toàn bộ cơ thể trở về tuổi ấu thơ!". Bố cục: Đồ họa phân đôi màn hình: cánh tay chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói tái tạo cơ bắp hoàn chỉnh bên cạnh chu trình trẻ hóa không hồi kết của chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L419</summary>

```text
HÌNH L419 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Các nhà khoa học trên khán đài không ngừng ghi chép dữ liệu, đây chính là hai chìa khóa vàng mở toang cánh cửa chữa lành bách bệnh cho nhân loại mai sau!". Bố cục: Các nhà khoa học vỗ tay nồng nhiệt, màn hình máy tính nhảy hàng triệu chuỗi mã gen quý giá; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nhưng lịch sử hai mùa giải trước đã dạy chúng ta bài học xương nước màu: kẻ tí hon thường là kẻ tung ra cú đấm quyết định khiến tất cả ngã ngửa!". Bố cục: Bức ảnh hồi tưởng Thú Mỏ Vịt Mùa một và Bọ Pháo Thủ Mùa hai giơ cao cúp vô địch trong sự ngỡ ngàng của giới chuyên gia; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L420</summary>

```text
HÌNH L420 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Ban giám khảo xin công bố bảng điểm Vòng Bán Kết! Huy chương Đồng thuộc về Chuột Chũi Mũi Sao với cảm biến xúc giác nhạy tới một nanomet!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ búa, trao huy chương đồng phát sáng cho chú Chuột Chũi Mũi Sao hoạt hình lông đen nhung mượt mà, mũi xòe ra 22 xúc tu đỏ hồng như bông hoa sao biển, đeo kính râm mù lòa nhưng phản xạ siêu thanh.
```
</details>

<details><summary>L421</summary>

```text
HÌNH L421 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Huy chương Bạc thuộc về Hải Sâm với mô liên kết biến đổi M-T-C tự hóa lỏng cơ thể không tốn năng lượng!". Bố cục: chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù vui mừng đón nhận tấm huy chương bạc quý giá thứ hai của mình.
```
</details>

<details><summary>L422</summary>

```text
HÌNH L422 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và Huy chương Vàng ba điểm xuất sắc thuộc về cụ tổ Cá Mút Đá Hagfish với kiến trúc tinh thể tơ protein siêu việt!". Bố cục: chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện đứng trên bục vinh quang nhận huy chương vàng, toàn thân phát sáng lấp lánh giữa tiếng reo hò rền vang.
```
</details>

<details><summary>L423</summary>

```text
HÌNH L423 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Bảng điểm sau vòng Bán Kết tạo nên một cơn địa chấn chưa từng có: Sứa Bất Tử và Hải Ly cùng dẫn đầu với tám điểm! Hagfish bứt phá thần tốc lên sáu điểm ngang hàng với Axolotl! Wombat và Hải Sâm cùng có năm điểm!". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) cập nhật điểm số: Sứa Bất Tử 8 điểm, Hải Ly 8 điểm, Axolotl 6 điểm, Hagfish 6 điểm, Wombat 5 điểm, Hải Sâm 5 điểm, Chuột Chũi Sao 4 điểm, Bạch Tuộc Mimic 2 điểm, Ếch dị nhân móng vuốt hoạt hình đáng yêu 2 điểm, Kiến Nổ 1 điểm; mọi ánh mắt đang hướng về Vòng Chung Kết Điểm Nhân Đôi!
```
</details>

<details><summary>L424</summary>

```text
HÌNH L424 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Giờ khắc lịch sử đã điểm! Toàn thể đấu trường nín thở chào đón Vòng Chung Kết: Món Quà Cho Nhân Loại và Những Đột Phá Công Nghệ Tương Lai!". Bố cục: Dàn pháo sáng rực rỡ bùng nổ quanh đấu trường, âm nhạc giao hưởng hào hùng vang lên; tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) nhấp nháy sáng rực ô Chung Kết mang chữ Điểm Nhân Đôi.
```
</details>

<details><summary>L425</summary>

```text
HÌNH L425 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Đây là vòng thi quyết định số phận chiếc vương miện tối cao: Huy chương Đồng được hai điểm, Huy chương Bạc bốn điểm, và Huy chương Vàng lên tới sáu điểm tròn!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ giơ cao ba chiếc huy chương đại hội khổng lồ phát ánh hào quang chói lọi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L426</summary>

```text
HÌNH L426 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Ở vòng đấu này, chúng ta đánh giá tiềm năng ứng dụng thực tiễn của mười tuyển thủ trong việc giải cứu y học, công nghệ và tương lai của loài người!". Bố cục: Màn hình lớn chiếu các mô hình bệnh viện tương lai, tàu không gian và robot sinh học; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L427</summary>

```text
HÌNH L427 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Không phải danh hiệu hão huyền, những món quà tiến hóa mà muôn loài trao tặng cho nền văn minh nhân loại chính là giá trị bất tử đích thực của sự sống!". Bố cục: Hình ảnh bàn tay con người nâng niu địa cầu, các nhánh công nghệ sinh học tỏa sáng rực rỡ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L428</summary>

```text
HÌNH L428 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Ứng cử viên đầu tiên tiến vào vòng đánh giá: cụ tổ Cá Mút Đá Hagfish với cuộc cách mạng vật liệu sinh thái!". Bố cục: chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện bơi trong buồng thí nghiệm, bên cạnh là các kỹ sư vật liệu của Hải quân Hoa Kỳ đang thử nghiệm sợi tơ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L429</summary>

```text
HÌNH L429 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Hiện nay, sợi Kevlar dùng để may áo giáp chống đạn thế giới tự nhiên được sản xuất từ dầu mỏ với quy trình hóa học độc hại và đắt đỏ.". Bố cục: Áo giáp chống đạn thông thường bị bắn vào để lại vết rách và tỏa khói đen ô nhiễm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Mỗi ứng viên mang theo một bộ mã gen dị thường được tôi luyện qua hàng trăm triệu năm tiến hóa khắc nghiệt của tự nhiên!". Bố cục: Mô hình chuỗi xoắn kép D-N-A khổng lồ xoay tròn giữa sàn đấu, từng đoạn gen phát quang rực rỡ mang tên mười loài sinh vật; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L430</summary>

```text
HÌNH L430 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nhưng tơ của Hagfish hoàn toàn có thể tự tổng hợp bằng vi khuẩn lên men sinh học, tạo ra các tấm giáp chống đạn nhẹ hơn một nửa, dai gấp 10 lần và hoàn toàn tự phân hủy sinh học trong môi trường tự nhiên!". Bố cục: Mô hình áo giáp dệt từ tơ Hagfish siêu mỏng nhẹ nhưng chặn đứng viên đạn bay tới kêu cái keng, không hề thủng rách; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L431</summary>

```text
HÌNH L431 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Hơn thế nữa, gel nhớt của Hagfish đang được nghiên cứu làm chất chữa cháy khẩn cấp cho các đám cháy giàn khoan dầu ngoài khơi nhờ khả năng ngậm nước cực lớn!". Bố cục: Bọt gel trắng xóa từ nhớt chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện dập tắt ngọn lửa bùng cháy dữ dội trên mô hình giàn khoan biển; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L432</summary>

```text
HÌNH L432 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Một giải pháp vật liệu xanh hoàn hảo cho tương lai quốc phòng và môi trường! Nhưng hãy nhìn sang Kỳ Nhông Axolotl với chiếc chìa khóa vàng của y học tái tạo mô người!". Bố cục: chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói bơi đến trước các bác sĩ phẫu thuật đang nghiên cứu mô tim và tủy sống; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L433</summary>

```text
HÌNH L433 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Mỗi năm trên thế giới có hàng triệu bệnh nhân chịu cảnh tàn phế do đột quỵ tim hoặc chấn thương đứt tủy sống không thể phục hồi.". Bố cục: Hình ảnh bệnh nhân ngồi xe lăn nhìn về phía trước với ánh mắt hy vọng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L434</summary>

```text
HÌNH L434 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Các nhà nghiên cứu tại Viện Max Planck Đức đã phân lập được các yếu tố sinh trưởng tế bào mầm chi từ Axolotl!". Bố cục: Ống nghiệm phát sáng màu xanh lam chứa các phân tử protein kích hoạt mầm tái sinh tế bào; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L435</summary>

```text
HÌNH L435 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khi ứng dụng các tín hiệu phân tử này vào tế bào người, các nhà khoa học đã thành công trong việc kích thích tế bào cơ tim người tự phân chia bù đắp vào vùng mô tim bị hoại tử sau cơn nhồi nước màu!". Bố cục: Vùng mô tim hoại tử màu xám sẫm dần hồng hào trở lại, các mạch nước màu mới mọc ra nuôi tim đập khỏe mạnh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L436</summary>

```text
HÌNH L436 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Axolotl đang thắp lên hy vọng có thật về một ngày con người có thể tự mọc lại các ngón tay và chữa lành hoàn toàn các chấn thương cột sống!". Bố cục: Chú kỳ nhông chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói mỉm cười giơ bàn tay nhỏ bé chạm vào bàn tay một em bé đang bình phục; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L437</summary>

```text
HÌNH L437 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Đây không còn là khoa học viễn tưởng, mà là lộ trình y học tái sinh có thể trở thành hiện thực trong vài thập kỷ tới!". Bố cục: Đồ họa cánh tay robot kết hợp tế bào sinh học mọc da thịt mềm mại tự nhiên; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L438</summary>

```text
HÌNH L438 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và cuối cùng, chiếc ly thủy tinh nhỏ xíu của Sứa Bất Tử bay vút lên giữa trung tâm sân vận động!". Bố cục: chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực trôi lơ lửng giữa một quả cầu ánh sáng ba chiều mô phỏng tế bào gốc người; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L439</summary>

```text
HÌNH L439 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Căn bệnh đáng sợ nhất của nhân loại không phải là vi khuẩn hay virus, mà chính là sự thoái hóa và lão hóa không thể đảo ngược của các tế bào não trong bệnh Alzheimer và Parkinson!". Bố cục: Hình ảnh các tế bào thần kinh não người bị teo tóp và đứt gãy kết nối theo tuổi tác; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Không có sàn đấu nào trên hành tinh này có thể quy tụ cùng lúc những kỳ tích sinh học phá vỡ mọi quy luật vật lý và y học đến như vậy!". Bố cục: Toàn cảnh đấu trường tràn ngập ánh sáng laser và màn hình holographic phân tích chỉ số sinh học của các tuyển thủ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L440</summary>

```text
HÌNH L440 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nhưng cơ chế chuyển biệt hóa tế bào của Sứa Bất Tử đã chứng minh một chân lý vĩ đại: tế bào hoàn toàn có thể được tái lập trình trở lại trạng thái non trẻ ban đầu!". Bố cục: Các tế bào thần kinh già nua được kích hoạt enzym sứa, tự hồi sinh và nối lại các khớp thần kinh phát sáng rực rỡ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L441</summary>

```text
HÌNH L441 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Giải mã cơ chế telomerase của loài sứa 4,5mm này đang giúp các nhà khoa học mở ra kỷ nguyên mới của thuốc đảo ngược tuổi sinh học, trẻ hóa tế bào gốc và kéo dài tuổi thọ khỏe mạnh cho loài người!". Bố cục: Một cụ già hoạt hình uống giọt nước tinh chất sứa bỗng trẻ trung yêu đời, nụ cười rạng rỡ hạnh phúc; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L442</summary>

```text
HÌNH L442 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Một giấc mơ trường thọ không bệnh tật mà nhân loại hằng khao khát suốt hàng 1.000 năm lịch sử!". Bố cục: Ánh sáng hồng tím của chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực lan tỏa bao bọc lấy toàn bộ sân vận động trong sự trầm trồ nghẹn ngào; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L443</summary>

```text
HÌNH L443 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và một món quà bất ngờ khác đến từ Kiến Nổ dũng cảm bảo vệ tổ: chất keo dính phenolic tiết ra từ cơ thể chúng đang được các nhà dược học nghiên cứu làm keo dán vết mổ bên trong cơ thể sinh học!". Bố cục: Bác sĩ phẫu thuật dùng một giọt gel sinh học lấy cảm hứng từ keo của chú Kiến Nổ dũng cảm bảo vệ tổ hoạt hình màu đỏ cam, đeo ba lô chứa chất lỏng vàng phát sáng, đội mũ bảo hộ chống độc, ánh mắt quả cảm kiên cường để dán vết rách mạch nước màu tim; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L444</summary>

```text
HÌNH L444 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Loại keo này có khả năng đông kết tức thì ngay trong môi trường ẩm ướt đầy nước màu, dính chặt vết mổ mà không gây độc hại và tự tiêu biến sau khi mô cơ lành lặn!". Bố cục: Vết mổ được dán kín hoàn hảo chỉ trong ba giây, không cần dùng chỉ khâu thông thường; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L445</summary>

```text
HÌNH L445 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Từ một hành động tự hủy bảo vệ tổ, thiên nhiên đã trao tặng cho y học loài người một phương pháp cầm nước màu phẫu thuật đột phá cứu sống hàng ngàn sinh mạng!". Bố cục: Hình ảnh bàn tay bác sĩ bắt tay với chú kiến chú Kiến Nổ dũng cảm bảo vệ tổ hoạt hình màu đỏ cam, đeo ba lô chứa chất lỏng vàng phát sáng, đội mũ bảo hộ chống độc, ánh mắt quả cảm kiên cường nhỏ bé đầy lòng tri ân; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L446</summary>

```text
HÌNH L446 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chiếc mũi sao của Chuột Chũi Mũi Sao cũng đang truyền cảm hứng cho việc chế tạo các robot cứu hộ động đất thế hệ mới!". Bố cục: Mô hình robot cứu hộ mini trang bị 22 cánh xúc tu cảm biến cơ học tiến vào đống đổ nát cứu hộ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L447</summary>

```text
HÌNH L447 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Trong môi trường khói bụi mù mịt và bóng tối sập đổ của các tòa nhà sau thảm họa, camera quang học hoàn toàn bị vô hiệu hóa, nhưng các xúc tu cảm biến Eimer có thể dò tìm thấy nhịp thở và sự sống của nạn nhân chỉ trong tích tắc!". Bố cục: Robot phát hiện tín hiệu sự sống của nạn nhân dưới đống gạch đá và phát tín hiệu cấp cứu giải cứu kịp thời; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L448</summary>

```text
HÌNH L448 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Một phát minh lấy cảm hứng từ sinh vật mù lòa đầm lầy đang cứu sống hàng 1.000 con người khỏi thảm họa thiên tai!". Bố cục: Hình ảnh chú chuột chũi chú Chuột Chũi Mũi Sao hoạt hình lông đen nhung mượt mà, mũi xòe ra 22 xúc tu đỏ hồng như bông hoa sao biển, đeo kính râm mù lòa nhưng phản xạ siêu thanh đeo kính râm bắt tay với người lính cứu hộ trong sự ấm áp; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L449</summary>

```text
HÌNH L449 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Hơn thế nữa, các nhà khoa học vật liệu tại Viện Công nghệ Massachusetts đang phát triển loại da nhân tạo thông minh mô phỏng cơ chế M-T-C của Hải Sâm!". Bố cục: Tấm da nhân tạo thông minh đổi từ mềm mại sang cứng cáp khi có dòng điện nhỏ chạy qua; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Trong thế giới tự nhiên kỳ thú, cơ bắp chưa bao giờ là thước đo duy nhất cho sự sinh tồn! Đêm nay, mười dị nhân sẽ chứng minh chân lý đó!". Bố cục: Cận cảnh ánh mắt rực lửa của mười tuyển thủ trong ánh sáng laser huyền ảo, sẵn sàng bước vào vòng đấu súng đầu tiên; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L450</summary>

```text
HÌNH L450 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Vật liệu này có thể dùng làm lớp vỏ ngoài cho robot mềm thám hiểm không gian: mềm dẻo để luồn lách qua các khe nứt thiên thạch nhưng lập tức cứng như thép khi cần khoan sâu vào lòng đất!". Bố cục: Robot thám hiểm vũ trụ hoạt hình luồn qua khe đá hẹp rồi khoan sâu lấy mẫu đất phát sáng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L451</summary>

```text
HÌNH L451 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Trận chung kết diễn ra trong bầu không khí trang trọng và xúc động chưa từng có giữa ba đỉnh cao tiến hóa của tự nhiên!". Bố cục: Cả khán đài nín thở theo dõi ánh đèn rọi vào chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực, chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói và chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo trên ba bục danh dự; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L452</summary>

```text
HÌNH L452 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Hải Ly đại diện cho sức mạnh kiến tạo làm thay đổi cả một vùng địa lý rộng lớn, mang lại sự trù phú và nước ngọt cho muôn loài sinh vật!". Bố cục: Hình ảnh đại ngàn xanh biếc với những hồ nước trong veo do chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo tạo dựng hiện lên hùng vĩ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L453</summary>

```text
HÌNH L453 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Axolotl đại diện cho kỳ tích tái sinh thể xác phi thường, còn Sứa Bất Tử là biểu tượng bất diệt cho sự chiến thắng quy luật nghiệt ngã của thời gian!". Bố cục: Ba vầng hào quang vàng, xanh lam và hồng phấn tỏa sáng rực rỡ quanh ba tuyển thủ vĩ đại; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L454</summary>

```text
HÌNH L454 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Ban giám khảo đã hoàn tất việc chấm điểm Vòng Chung Kết! Huy chương Đồng hai điểm thuộc về cụ tổ Cá Mút Đá Hagfish với vật liệu tơ chống đạn sinh thái!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương đồng hai điểm cho chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện.
```
</details>

<details><summary>L455</summary>

```text
HÌNH L455 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Huy chương Bạc bốn điểm thuộc về Kỳ Nhông Axolotl với cuộc cách mạng tái tạo mô tim và tủy sống con người!". Bố cục: chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói nhận tấm huy chương bạc bốn điểm, đưa tổng điểm của mình chạm mốc mười điểm tròn!
```
</details>

<details><summary>L456</summary>

```text
HÌNH L456 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và Huy chương Vàng sáu điểm tối cao của Vòng Chung Kết thuộc về Sứa Bất Tử với giấc mơ trẻ hóa tế bào và đảo ngược lão hóa cho toàn thể nhân loại!". Bố cục: chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực bay lên bục cao nhất đón nhận huy chương vàng sáu điểm khổng lồ trong ánh pháo hoa rực rỡ ngập trời!
```
</details>

<details><summary>L457</summary>

```text
HÌNH L457 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Một màn lội ngược dòng không tưởng trong lịch sử Đại Hội Sinh Tồn! Tổng điểm của Sứa Bất Tử đã nhảy vọt lên con số 14 điểm, chính thức xô đổ mọi kỷ lục điểm số!". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) bùng nổ hiệu ứng ánh sáng: Sứa Bất Tử 14 điểm, Axolotl 10 điểm, Hải Ly 8 điểm, Hagfish 8 điểm, Wombat 5 điểm, Hải Sâm 5 điểm, Chuột Chũi Sao 4 điểm, Bạch Tuộc Mimic 2 điểm, Ếch dị nhân móng vuốt hoạt hình đáng yêu 2 điểm, Kiến Nổ 1 điểm; toàn bộ khán trường vỡ òa sung sướng!
```
</details>

<details><summary>L458</summary>

```text
HÌNH L458 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Âm nhạc vinh quang rộn rã vang lên! Thưa toàn thể muôn loài muôn thú, chúng ta chính thức bước vào Lễ Bế Mạc và Trao Vương Miện Đại Hội Sinh Tồn Mùa ba!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vest đỏ tươi đứng trên bục danh dự giữa sân, tay cầm chiếc micro vàng lấp lánh; xung quanh là dàn pháo hoa kim tuyến bay rợp trời; tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng rực bảng tổng sắp.
```
</details>

<details><summary>L459</summary>

```text
HÌNH L459 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Sau tám vòng thi đấu nghẹt thở với hàng loạt kỷ lục khoa học được thiết lập, bảng tổng sắp chung cuộc đã chính thức chốt hạ!". Bố cục: Màn hình lớn hiện bảng tổng sắp mười bậc thang vinh quang từ hạng mười đến ngôi vô địch; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tiếng còi khai cuộc vang lên! Chào mừng quý vị đến với Vòng một: Đọ Sức Vũ Khí Tự Thân và Áo Giáp Sinh Học!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng giơ tay phất cờ hiệu màu đỏ, pháo hoa bắn sáng rực hai bên sân khấu; tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) nhấp nháy sáng ô thử thách số một.
```
</details>

<details><summary>L460</summary>

```text
HÌNH L460 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Mỗi tuyển thủ đều đã cống hiến hết mình, phô diễn những vũ khí sinh học và kỳ tích thích nghi làm rạng danh thế giới hoang dã!". Bố cục: Hình ảnh mười chiếc cúp lưu niệm phát sáng lấp lánh trên khay nhung đỏ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L461</summary>

```text
HÌNH L461 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Đồng hạng ba giành Huy chương Đồng chung cuộc của Mùa ba là hai tuyển thủ: kỹ sư Hải Ly và cụ tổ Cá Mút Đá Hagfish với tám điểm xuất sắc!". Bố cục: chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo và chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện cùng bước lên bục số ba, đeo tấm huy chương đồng chung cuộc nặng trĩu và mỉm cười bắt tay nhau; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L462</summary>

```text
HÌNH L462 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Ngôi vị Á quân giành Huy chương Bạc chung cuộc thuộc về thiên thần tái sinh của đất nước Mexico: Kỳ Nhông Axolotl với mười điểm tròn trĩnh!". Bố cục: chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói bước lên bục số hai, sáu nhánh mang hồng rung rinh xúc động, nụ cười ngây thơ đón nhận tấm huy chương bạc quý phái; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L463</summary>

```text
HÌNH L463 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và chiếc vương miện vàng nạm đá quý tối cao của Đại Hội Sinh Tồn Mùa ba... đã tìm thấy chủ nhân xứng đáng nhất!". Bố cục: Một chùm ánh sáng laser vàng rực rọi thẳng vào chiếc vương miện đang hạ dần từ trên không trung; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L464</summary>

```text
HÌNH L464 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Kẻ từng bị các chuyên gia đánh giá là yếu ớt nhất, chỉ nặng 1 miligram và dài 4,5mm trong buổi lễ cân ký đo đạc đầu tiên!". Bố cục: Hình ảnh hồi tưởng lúc cân ký: chiếc ly thủy tinh nhỏ bé bị lãng quên bên cạnh cỗ xe tăng Wombat 35kg; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L465</summary>

```text
HÌNH L465 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nhưng bằng năng lực đảo ngược dòng thời gian sinh học vô tận, sinh vật nhỏ bé này đã chứng minh cho toàn vũ trụ thấy: kích thước không bao giờ là giới hạn của sự sống!". Bố cục: chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực bay lơ lửng bước lên bục cao nhất số một, phát ra ánh hào quang hồng tím lung linh huyền ảo; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L466</summary>

```text
HÌNH L466 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Một thắng lợi của sự kiên trì, của sự dẻo dai và của phép màu tái sinh vô tận trong lòng đại dương sâu thẳm!". Bố cục: Toàn cảnh chú sứa nhỏ phát sáng giữa vòng vây của các đấu sĩ khổng lồ đang ngước nhìn thán phục; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L467</summary>

```text
HÌNH L467 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Xin nhiệt liệt chúc mừng tân vương của Mùa ba: SỨA BẤT TỬ!". Bố cục: Chiếc vương miện vàng nhỏ xíu vừa vặn được đặt nhẹ nhàng lên đỉnh chuông trong suốt của chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực, pháo hoa bùng nổ rực sáng cả bầu trời đêm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L468</summary>

```text
HÌNH L468 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khán đài hàng vạn muông thú đồng loạt đứng dậy hò reo vang dội, vẫy cờ hoa chúc mừng chiến thắng lịch sử của tân vương!". Bố cục: Toàn thể khán giả rừng già và đại dương cùng reo hò, ném mũ và hoa giấy chúc mừng; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng và bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ vỗ tay chúc mừng nồng nhiệt.
```
</details>

<details><summary>L469</summary>

```text
HÌNH L469 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Dạ em cảm ơn toàn thể muôn loài đã ủng hộ em! Em xin hứa sẽ tiếp tục bơi lội bất tử thêm vài triệu năm nữa để bảo vệ sự sống hành tinh nha!". Bố cục: Cận cảnh chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực đội vương miện vàng, nhấp nháy phát sáng xúc động phát biểu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tại vòng đấu này, mười tuyển thủ sẽ phô diễn những trang bị cơ thể dị thường nhất được tôi luyện qua hàng triệu năm tiến hóa.". Bố cục: Màn hình lớn chiếu đồ họa các loại giáp và vũ khí sinh học: móng vuốt xương, tấm khiên sụn, răng sắt và màng keo chống đạn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L470</summary>

```text
HÌNH L470 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tất cả các tuyển thủ đều đã nhận được những chiếc cúp danh dự và huy chương tương xứng với những cống hiến khoa học phi thường của mình!". Bố cục: Toàn cảnh lễ trao giải rực rỡ, khay huy chương vàng bạc đồng lấp lánh trên bục vinh quang; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L471</summary>

```text
HÌNH L471 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Anh chàng Wombat mỉm cười tự hào với tấm huy chương vàng Vòng một, kỹ sư Hải Ly rạng rỡ với ba tấm huy chương danh giá, và cụ tổ Hagfish uy nghi với giải thưởng cổ vật sống trường tồn!". Bố cục: chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường, chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo và chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện đứng cạnh nhau khoe huy chương trong tiếng nhạc rộn rã; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L472</summary>

```text
HÌNH L472 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nhưng đỉnh cao vinh quang và chiếc vương miện tối cao vẫn thuộc về chú sứa nhỏ 1 miligram: biểu tượng của sức sống mãnh liệt vượt lên trên mọi giới hạn vật chất!". Bố cục: Chiếc vương miện vàng nạm đá quý phát ánh hào quang lung linh trên đỉnh chuông trong suốt của chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L473</summary>

```text
HÌNH L473 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Toàn thể mười tuyển thủ cùng bước lên bục vinh quang chung, quây quần bên chiếc cúp vàng danh giá của Đại Hội Sinh Tồn Mùa ba!". Bố cục: Mười tuyển thủ ôm vai nhau tươi cười rạng rỡ, pháo hoa nổ vang trời, khán đài tung hoa giấy rực rỡ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L474</summary>

```text
HÌNH L474 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chiếc máy ảnh toàn cảnh của ban tổ chức lóe sáng, ghi lại bức ảnh lịch sử của mười dị nhân vĩ đại nhất hành tinh trong sự hò reo không dứt của muôn loài!". Bố cục: Bức ảnh chụp chung toàn đoàn phát sáng khung vàng lưu niệm tuyệt đẹp giữa sân khấu tràn ngập niềm vui; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L475</summary>

```text
HÌNH L475 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Những tiếng hò reo vang dội khắp bốn bề đấu trường khi chiếc vương miện Mùa ba tỏa ánh sáng lộng lẫy trên đỉnh chuông sứa nhỏ bé!". Bố cục: Pháo hoa hình vòng lặp vô cực nổ tung trên bầu trời đêm rực rỡ, toàn thể muông thú vẫy cờ hoa chúc mừng tân vương; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L476</summary>

```text
HÌNH L476 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Đó là một khoảnh khắc xúc động nhắc nhở muôn loài về sự kỳ diệu khôn cùng của tạo hóa, nơi sinh vật nhỏ bé nhất lại nắm giữ bí mật trường tồn vĩ đại nhất!". Bố cục: Chú sứa chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực phát sáng dịu dàng soi sáng nụ cười hạnh phúc của toàn bộ mười tuyển thủ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L477</summary>

```text
HÌNH L477 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Mỗi chiếc huy chương được trao hôm nay là sự ghi nhận xứng đáng cho hàng trăm triệu năm bền bỉ tiến hóa và thích nghi phi thường của thế giới tự nhiên!". Bố cục: Các tuyển thủ cùng bước lên bục danh dự, ôm nhau ăn mừng thắm thiết dưới mưa pháo hoa rực rỡ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L478</summary>

```text
HÌNH L478 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Dù mang vẻ ngoài kỳ dị hay tập tính khác thường, mỗi sinh vật đều là một kiệt tác hoàn hảo của tạo hóa, mang trong mình những giá trị vô giá cho hành tinh!". Bố cục: Toàn cảnh mười dị nhân cùng nâng cúp và vẫy tay chào khán giả trong ánh sáng hoàng kim lộng lẫy; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L479</summary>

```text
HÌNH L479 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Mười tuyển thủ cùng bước lên sàn đấu chung, ôm lấy nhau trong tình thân ái muôn loài: không có ai là kẻ thua cuộc, tất cả đều là những kiệt tác tiến hóa vĩ đại của Trái Đất!". Bố cục: Mười tuyển thủ (Ếch dị nhân móng vuốt hoạt hình đáng yêu, Axolotl, Hải Sâm, Hagfish, Bạch Tuộc Mimic, Wombat, Chuột Chũi Mũi Sao, Kiến Nổ, Sứa Bất Tử, Hải Ly) đứng quây quần bên nhau giơ cúp vinh quang; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Không có súng đạn cơ khí của con người, nhưng vũ khí sinh học tự nhiên lại sở hữu độ bền và hiệu năng vượt xa mọi phòng thí nghiệm thế giới tự nhiên tối tân nhất!". Bố cục: Hình ảnh minh họa áo giáp sắt của con người bị rỉ sét nứt vỡ so sánh với bộ giáp sinh học tự phục hồi nguyên vẹn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L480</summary>

```text
HÌNH L480 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chiếc cúp Mùa ba đã tìm thấy chủ nhân, khép lại một mùa giải kịch tính nhất từ trước đến nay!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng giơ micro nở nụ cười rạng rỡ, toàn cảnh sân vận động bế mạc tràn ngập niềm vui và hạnh phúc; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L481</summary>

```text
HÌNH L481 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khi ánh đèn sân khấu dần dịu lại và tiếng reo hò lắng xuống, một thông điệp sâu sắc hơn bao giờ hết đang chờ đợi chúng ta lắng đọng...". Bố cục: Toàn cảnh đấu trường chuyển sang ánh sáng hoàng hôn ấm áp dịu nhẹ, mười tuyển thủ ngồi bên nhau ngắm nhìn bầu trời đêm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L482</summary>

```text
HÌNH L482 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Mỗi loài sinh vật xuất hiện trong Mùa ba hôm nay đều là kết tinh của hàng trăm triệu năm thử nghiệm và chọn lọc tự nhiên khắc nghiệt.". Bố cục: Hình ảnh cây phả hệ tiến hóa phát sáng tỏa ra muôn nhánh sinh mệnh rực rỡ từ cội nguồn Trái Đất; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L483</summary>

```text
HÌNH L483 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nhưng dù sở hữu những siêu năng lực bẻ gãy mọi quy luật sinh học, chúng vẫn vô cùng mong manh trước sự tàn phá môi trường do con người gây ra.". Bố cục: Bức tranh tương phản: một bên là dòng suối trong xanh của Axolotl, một bên là cống nước ô nhiễm và rác thải nhựa đe dọa; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L484</summary>

```text
HÌNH L484 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Kỳ Nhông Axolotl dù có thể mọc lại cả não bộ và trái tim, nhưng chúng không thể tự tái tạo lại hồ nước Xochimilco đang bị ô nhiễm và thu hẹp từng ngày, đẩy chúng đến bờ vực tuyệt chủng ngoài tự nhiên!". Bố cục: Chú kỳ nhông chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói ngồi buồn bã nhìn vào vũng nước cạn dần giữa lòng thành phố; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L485</summary>

```text
HÌNH L485 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Sứa Bất Tử có thể đảo ngược chu trình già nua vô tận, nhưng chúng vẫn tan rã bất lực trước những vùng biển ngập tràn hạt vi nhựa và hiện tượng axit hóa đại dương!". Bố cục: chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực trôi dạt giữa những túi nilon và hạt vi nhựa lơ lửng trong làn nước biển sẫm màu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L486</summary>

```text
HÌNH L486 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Bảo vệ những sinh vật dị thường này không chỉ là bảo vệ tự nhiên hoang dã, mà chính là bảo vệ kho báu tri thức vô giá cho tương lai y học và sự tồn vong của chính loài người chúng ta!". Bố cục: Bàn tay con người nhẹ nhàng nâng niu giọt nước chứa chú sứa nhỏ và nhành cây xanh của chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L487</summary>

```text
HÌNH L487 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chúng ta không thể học được bí quyết tái tạo mô tim từ Axolotl hay đảo ngược lão hóa từ Sứa nếu để chúng biến mất vĩnh viễn khỏi hành tinh này!". Bố cục: Hình ảnh Trái Đất xanh tươi được bao bọc trong vòng tay bảo vệ của con người và muôn thú; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L488</summary>

```text
HÌNH L488 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và trước khi khép lại tập đặc biệt Mùa ba, anh MC xin gửi tới toàn thể quý vị khán giả một câu hỏi giao lưu đầy thú vị:". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vest đỏ tươi bước ra phía trước màn hình, nở nụ cười ấm áp giơ micro về phía người xem; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L489</summary>

```text
HÌNH L489 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nếu được chọn sở hữu một siêu năng lực của mười quái kiệt Mùa ba: tái sinh không sẹo của Axolotl, mông bọc thép của Wombat, đớp mồi 0,12 giây của Chuột Chũi, hay khả năng đảo ngược thời gian của Sứa Bất Tử, bạn sẽ chọn năng lực nào?". Bố cục: Bốn khung hình hoạt hình vui nhộn hiện lên quanh anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng tượng trưng cho 4 siêu năng lực dị nhân; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Ứng cử viên số một bước ra sàn đấu: Gấu Túi Wombat mang chiếc mông bọc thép huyền thoại tiến thẳng vào mô hình hang đất hẹp!". Bố cục: chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường chui đầu vào cửa hang đất mô phỏng, quay trọn vẹn phần mông bọc thép dày cộm ra ngoài đối diện kẻ thù; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L490</summary>

```text
HÌNH L490 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Hãy chia sẻ suy nghĩ và bình luận của bạn ngay bên dưới video này để cùng bàn luận với cộng đồng yêu thiên nhiên nhé!". Bố cục: Biểu tượng khung bình luận hoạt hình nhấp nháy phát sáng rực rỡ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L491</summary>

```text
HÌNH L491 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và đừng quên nhấn nút Đăng ký kênh Vẽ Chuyện Hoang Dã ngay hôm nay để không bỏ lỡ tập 31: Chim Cắt Lớn Peregrine Falcon — sát thủ bầu trời bổ nhào với vận tốc 390 km/h một giờ xé gió săn mồi!". Bố cục: Cửa hầm mở ra hé lộ bóng đen chú chim cắt lao vút xuống như tên lửa siêu thanh trên bầu trời mây trắng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L492</summary>

```text
HÌNH L492 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Cùng với đó là sự khởi động của Đại Hội Sinh Tồn Mùa bốn trong tương lai, nơi các dũng sĩ săn mồi đỉnh chóp như Cá Voi Sát Thủ Orca, Quạ Đen thiên tài và Chó Sói Xám sẽ chính thức tuyên chiến!". Bố cục: Các bóng đen dũng mãnh của Cá Voi Sát Thủ Orca, Quạ Đen đội mũ thám tử và Chó Sói hú dưới trăng hiện lên đầy uy lực; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L493</summary>

```text
HÌNH L493 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Hành trình Mùa ba khép lại nhưng những bài học về tình yêu thiên nhiên và sự trân trọng từng sự sống nhỏ bé sẽ còn đọng lại mãi trong trái tim chúng ta.". Bố cục: Bầu trời đêm trên đấu trường bừng sáng bởi muôn vì sao lấp lánh, mười tuyển thủ cùng ngước nhìn về tương lai xanh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L494</summary>

```text
HÌNH L494 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Mỗi dòng suối mát lành, mỗi rạn san hô rực rỡ và mỗi cánh rừng nguyên sinh đều là ngôi nhà chung thiêng liêng mà con người và muôn thú cùng chia sẻ.". Bố cục: Bức tranh Trái Đất xanh ngắt tươi đẹp, biển cả trong lành và rừng xanh bát ngát trải dài vô tận; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L495</summary>

```text
HÌNH L495 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chúng ta hãy cùng nhau chung tay gìn giữ và bảo vệ những kỳ quan sinh học vô giá này trước khi quá muộn!". Bố cục: Biểu tượng bàn tay con người kết nối với dấu chân muông thú tạo thành vòng tròn bảo vệ bền vững; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L496</summary>

```text
HÌNH L496 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Mỗi hành động nhỏ bé của chúng ta hôm nay: tiết kiệm một giọt nước sạch, giảm bớt một chiếc túi nilon thải ra đại dương, hay trồng thêm một mầm cây xanh nơi góc phố đều là sự tiếp sức cho sự trường tồn của muôn loài!". Bố cục: Hình ảnh em bé tưới mầm cây non xanh tốt, dòng suối mát lành chảy uốn lượn qua khu rừng bình yên; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L497</summary>

```text
HÌNH L497 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Hãy cùng kênh Vẽ Chuyện Hoang Dã lan tỏa tình yêu thiên nhiên và lòng trân trọng sự sống đến mọi người xung quanh bạn nhé!". Bố cục: Biểu tượng trái tim xanh phát sáng kết nối hàng triệu người xem trên toàn cầu cùng chung tay bảo vệ môi trường; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L498</summary>

```text
HÌNH L498 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Những thông điệp yêu thương và bài học bảo tồn thiên nhiên sâu sắc của Đại Hội Sinh Tồn Mùa ba sẽ tiếp tục lan tỏa, thắp sáng niềm hy vọng cho một Trái Đất xanh tươi muôn màu muôn vẻ!". Bố cục: Toàn cảnh Trái Đất quay chậm rãi trong không gian, được bao bọc bởi tình yêu thương và sự chở che của con người và muôn loài; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L499</summary>

```text
HÌNH L499 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Một cuộc chạm trán nảy lửa trên không trung và đại dương bao la đang đón chờ quý vị khán giả thân yêu!". Bố cục: Dòng chữ hẹn gặp lại ở Mùa bốn bừng sáng trên nền trời đầy sao; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Các nhà khoa học tại đại học Adelaide đã phát hiện: lớp giáp mông này không phải là xương đặc thông thường, mà là sự kết hợp hoàn hảo giữa sụn dày và các dải mô mạc sợi kết nối siêu bền!". Bố cục: Sơ đồ giải phẫu cắt lớp hoạt hình: lớp da dày, lớp sụn đàn hồi và dải collagen đan chéo chịu lực va đập cực đại; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L500</summary>

```text
HÌNH L500 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Bảo vệ những loài sinh vật kỳ diệu này chính là bảo vệ kho tàng tri thức sinh học vô giá mà thiên nhiên đã dày công tích lũy qua hàng ngàn triệu năm!". Bố cục: Bàn tay con người nâng niu giọt nước trong vắt chứa chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực và mầm cây xanh của chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L501</summary>

```text
HÌNH L501 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nếu để mất đi dù chỉ một mắt xích nhỏ bé, nhân loại có thể vĩnh viễn đánh mất những chìa khóa y học quý báu không bao giờ tìm lại được!". Bố cục: Mạng lưới sự sống tỏa sáng bao bọc lấy hành tinh xanh, biểu tượng của sự hòa hợp vĩnh cửu giữa con người và thiên nhiên; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L502</summary>

```text
HÌNH L502 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Xin chào tạm biệt, xin cảm ơn toàn thể quý vị đã đồng hành, và hẹn gặp lại tất cả trong những chuyến phiêu lưu hoang dã tiếp theo!". Bố cục: Toàn thể mười tuyển thủ cùng anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng và bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ vẫy tay chào tạm biệt khán giả trong tiếng pháo hoa rực rỡ bế mạc; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Độ dày của tấm khiên lên tới 3cm, có khả năng triệt tiêu toàn bộ lực cắn chết người từ hàm răng sắc nhọn của chó hoang Dingo!". Bố cục: Mô hình chó hoang Dingo cắn ngập răng vào mông chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường nhưng răng trượt kêu ken két, chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường vẫn thản nhiên nhai cỏ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chưa dừng lại ở đó, Wombat tung ra tuyệt kỹ cú đá lừa ngược: dùng bốn chân gồng cứng đẩy toàn bộ sức nặng cơ thể ép nát hộp sọ kẻ tấn công lên trần hang đá!". Bố cục: chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường dùng hai chân sau đạp mạnh đẩy tấm khiên mông dập mạnh lên trần hang, tiếng sọ kẻ thù nứt toác trong mô phỏng hoạt hình; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Cơ chế đập nát sọ bằng mông biến nơi dễ tổn thương nhất của động vật thành một chiếc bẫy kẹp thủy lực nghiền nát mọi kẻ săn mồi liều lĩnh!". Bố cục: Mô phỏng chiếc máy ép thủy lực hoạt hình kẹp nát tảng đá cứng để minh họa sức mạnh cú thúc mông của chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tuyệt chiêu phòng thủ biến thành đòn tấn công chí mạng! Khán đài vỗ tay sấm dậy trước cỗ xe tăng đào hầm nước Úc!". Bố cục: Khán đài thú rừng đồng loạt giơ bảng chấm điểm chín và mười reo hò; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng giơ micro thán phục.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nhưng đối thủ của Wombat không hề chịu lép vế! Xin mời kỹ sư Hải Ly tiến vào sàn đọ sức với bộ răng cửa màu cam rực rỡ!". Bố cục: chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo bước lên bục gỗ, ngoác miệng khoe hai chiếc răng cửa trên dưới màu cam sáng chói như thanh kim loại nung nóng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tại sao răng của Hải Ly lại có màu cam kỳ lạ như vậy? Một công trình nghiên cứu trên tạp chí Science đã làm sáng tỏ bí mật này!". Bố cục: Phóng to hình ảnh hiển vi điện tử: các hạt nano hợp chất sắt vô định hình xen kẽ giữa các trụ khoáng men răng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Men răng của Hải Ly được gia cố bằng các hạt nano hợp chất giàu sắt vô định hình, giúp răng của chúng cứng hơn cả men răng người và kháng hoàn toàn axit ăn mòn!". Bố cục: Hình vẽ minh họa so sánh: axit nhỏ vào răng thường bị xủi bọt, còn nhỏ vào răng của chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo thì trôi tuột như nước trên lá sen; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nhờ vũ khí bọc sắt này, Hải Ly có thể gặm đứt một thân cây gỗ cứng đường kính 40cm chỉ trong vài giờ đồng hồ mà răng không hề bị mẻ hay gãy!". Bố cục: chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo ngoạm răng vào thân cây cổ thụ dày cộp, dăm gỗ bay tung tóe, thân cây đổ rầm trong sự kinh ngạc của khán giả; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Hơn thế nữa, răng của chúng mọc liên tục suốt đời, càng gặm gỗ nhiều thì hai mặt răng càng tự mài vào nhau thành lưỡi đục sắc như dao mổ!". Bố cục: Hai chiếc răng trên và dưới cọ xát vào nhau tóe ra những tia lửa hoạt hình sắc lẹm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nếu con người sở hữu hàm răng bọc sắt như Hải Ly, các nha sĩ trên toàn cầu chắc chắn sẽ thất nghiệp tập thể vì sâu răng không bao giờ có cửa tấn công!". Bố cục: Hình ảnh bác sĩ nha khoa hoạt hình ngồi ngáp dài đóng cửa phòng khám vì ai nấy đều có hàm răng sắt cam lấp lánh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Đến lượt sát thủ rừng rậm Tây Phi xuất trận: Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu!". Bố cục: chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng ngồi thu mình trên bệ đá rêu phong, ánh mắt sắc lẹm nhìn thẳng vào ống kính; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L62</summary>

```text
HÌNH L62 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khi bị đe dọa, chú ếch này tự gồng các bó cơ chân sau, bẻ gãy khớp nối sụn của đốt xương ngón chân cuối cùng!". Bố cục: Đồ họa X-quang hoạt hình: khớp xương ngón chân tách rời khỏi đốt sụn, cơ co rút kéo xương dịch chuyển; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L63</summary>

```text
HÌNH L63 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Mũi xương nhọn hoắt đâm xuyên thủng lớp da đệm thịt dưới lòng bàn chân, phóng ra ngoài như những chiếc móng vuốt tự chế chết người!". Bố cục: Cận cảnh bàn chân sau: ba chiếc vuốt xương trắng muốt nhọn hoắt đâm xuyên qua da thịt phóng ra ngoài kêu cách cách; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L64</summary>

```text
HÌNH L64 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và điều kỳ diệu nhất theo công bố của tạp chí Biology Letters: sau khi chiến đấu xong, các cơ thả lỏng, móng xương tự thụt vào bên trong!". Bố cục: Móng xương từ từ rút lui vào trong lớp thịt đệm bàn chân; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L65</summary>

```text
HÌNH L65 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chỉ sau 48 giờ, lớp mô da bị đâm rách sẽ tự động tái tạo và lành lặn hoàn toàn mà không hề bị nhiễm trùng nhờ các hợp chất kháng khuẩn cực mạnh tiết ra từ tuyến da!". Bố cục: Vết rách trên da liền lại trơn tru chỉ sau 48 giờ, chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng nhếch mép cười đắc thắng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L66</summary>

```text
HÌNH L66 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Một cơ chế bẻ xương tự thân có 1-0-2 trong thế giới động vật có xương sống, kết hợp giữa vũ khí sát thương và khả năng tự chữa lành siêu tốc!". Bố cục: chú Ếch Lông dị nhân móng vuốt hoạt hình đáng yêu hoạt hình màu nâu sần sùi có lông tơ ở hai bên sườn, móng vuốt xương nhọn hoắt đâm ra từ đầu ngón chân sau, vẻ mặt ngầu lạnh lùng đứng thẳng vươn vai khoe bộ vuốt xương lấp lánh như chiến binh dũng mãnh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L67</summary>

```text
HÌNH L67 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Không chỉ có bốn tuyển thủ trên, nữ chiến binh tí hon Kiến Nổ dũng cảm bảo vệ tổ cũng khiến ban giám khảo phải giật mình trước cơ chế tự hủy bảo vệ tổ!". Bố cục: chú Kiến Nổ dũng cảm bảo vệ tổ hoạt hình màu đỏ cam, đeo ba lô chứa chất lỏng vàng phát sáng, đội mũ bảo hộ chống độc, ánh mắt quả cảm kiên cường bước lên bục kính bọc thép, cơ thể màu đỏ cam ánh lên dưới đèn pha; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L68</summary>

```text
HÌNH L68 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nghiên cứu của tiến sĩ Alice Laciny tại Borneo phát hiện: cặp tuyến hàm dưới của kiến thợ phình to bất thường, kéo dài dọc toàn bộ khoang bụng!". Bố cục: Đồ họa giải phẫu kiến thợ: hai dải tuyến độc màu vàng óng phình to chiếm trọn khoang bụng phát sáng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L69</summary>

```text
HÌNH L69 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khi đối mặt với kẻ thù xâm lược tổ, kiến thợ gồng toàn bộ các cơ bụng làm nứt vỡ lớp vỏ kitin, phóng thích dòng keo độc tố dính chặt và làm mù mắt kẻ tấn công!". Bố cục: Vỏ bụng nứt toác phóng ra dòng keo dính màu vàng bao trùm con bọ hung xâm lược, con bọ ngã gục dính chặt vào mặt sàn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L70</summary>

```text
HÌNH L70 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Một sự hy sinh quả cảm của tầng lớp thợ già để bảo toàn sự sống cho toàn bộ đàn ấu trùng và kiến chúa non trẻ!". Bố cục: Khán đài im lặng xúc động trước tinh thần hy sinh của chú Kiến Nổ dũng cảm bảo vệ tổ hoạt hình màu đỏ cam, đeo ba lô chứa chất lỏng vàng phát sáng, đội mũ bảo hộ chống độc, ánh mắt quả cảm kiên cường, bà Cú gật đầu chấm điểm danh dự; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L71</summary>

```text
HÌNH L71 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và Bạch Tuộc Mimic cũng thể hiện vũ khí cận chiến: các giác hút trên tám xúc tu có thể siết chặt với lực hút hàng chục kilopascal, đồng thời tiết ra độc tố tetrodotoxin gây tê liệt tức thì con mồi!". Bố cục: chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình giơ xúc tu siết chặt con cua biển mô phỏng, dòng độc tố phát sáng xanh lam làm con cua đông cứng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L72</summary>

```text
HÌNH L72 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Bên cạnh đó, lớp da nhầy đặc biệt của Kỳ Nhông Axolotl cũng là một tấm áo giáp sinh học vô hình chống lại mọi mầm bệnh nấm mốc nước ngọt!". Bố cục: chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói bơi lượn trong làn nước mát, toàn thân phát ra ánh sáng dịu nhẹ của lớp màng gel bảo vệ tự nhiên; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L73</summary>

```text
HÌNH L73 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Lớp chất nhầy kháng khuẩn phủ kín bề mặt cơ thể Axolotl chứa hàng chục loại enzym lysozyme tự nhiên, tiêu diệt vi khuẩn gram âm ngay khi chúng vừa tiếp xúc với biểu bì!". Bố cục: Kính hiển vi soi vào bề mặt da: các phân tử enzym lysozyme phá vỡ màng tế bào vi khuẩn có hại một cách chớp nhoáng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L74</summary>

```text
HÌNH L74 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nhờ vậy, ngay cả khi bị thương rách toạc da thịt trong các cuộc đụng độ dưới đáy hồ đục, cơ thể chúng vẫn duy trì trạng thái vô trùng tuyệt đối để phục vụ tiến trình tái sinh!". Bố cục: Vết thương rách trên thân chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói được lớp gel kháng khuẩn bảo vệ kín mít, không hề bị sưng tấy hay nhiễm trùng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L75</summary>

```text
HÌNH L75 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Thậm chí khi nghiên cứu kỹ lưỡng về cơ học va chạm, các nhà vật lý nhận thấy cấu trúc mông của Wombat hoạt động như một hệ thống giảm xóc thủy lực tự nhiên!". Bố cục: Mô hình đồ họa 3D mô phỏng xung lực va chạm bị tiêu tán qua mạng lưới vi sợi sụn của chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L76</summary>

```text
HÌNH L76 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Lực cắn chết người từ kẻ săn mồi bị phân tán đều ra toàn bộ vùng chậu và cột sống vững chãi, biến áp lực tập trung thành một lực nén nhẹ nhàng không gây tổn thương!". Bố cục: Các đường phản lực màu đỏ phân tán thành làn sóng xanh êm dịu chạy dọc khung xương chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L77</summary>

```text
HÌNH L77 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Còn chiếc càng súng của Tôm Súng có thể chịu được áp lực nổ tương đương hàng chục bầu khí quyển mà lớp vỏ kitin bên ngoài không hề bị rạn nứt một sợi tóc!". Bố cục: Lớp vỏ càng tôm bóng loáng chống chịu sóng xung tạo bong bóng dính rực rỡ dưới đáy nước; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L78</summary>

```text
HÌNH L78 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Ban giám khảo tròn mắt chấm điểm! Và cuối cùng là màn trình diễn của cụ tổ 300 triệu năm: Cá Mút Đá Hagfish!". Bố cục: chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện trườn vào bể nước kính cường lực trước ánh mắt tò mò của toàn bộ khán đài; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L79</summary>

```text
HÌNH L79 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khi một mô hình cá mập giả lao vào cắn, Hagfish ngay lập tức tiết ra một lượng chất nhầy nhỏ hòa tan vào nước biển xung quanh!". Bố cục: Mô hình cá mập ngậm trúng chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện, nhưng chỉ trong một phần mười giây, một khối keo nhớt khổng lồ bung ra bít kín mang cá mập; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L80</summary>

```text
HÌNH L80 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Viện nghiên cứu sinh học vật liệu phát hiện: bên trong chất nhầy của Hagfish chứa hàng vạn sợi protein tơ cuộn tròn siêu nhỏ!". Bố cục: Hình ảnh hiển vi: các cuộn sợi protein bung ra như những sợi dây thừng nano đan kết chặt chẽ vào nhau; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L81</summary>

```text
HÌNH L81 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khi gặp nước biển, các sợi tơ này bung dài ra tới 15cm, tạo thành một mạng lưới sợi bền gấp 10 lần tơ nhện và dai hơn cả sợi Kevlar dùng may áo giáp chống đạn!". Bố cục: Bảng so sánh hoạt hình: sợi tơ Hagfish kéo căng chịu lực kéo gấp 10 lần tơ nhện và vượt xa độ bền của sợi Kevlar thế giới tự nhiên; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L82</summary>

```text
HÌNH L82 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Để không bị chính chất nhầy của mình bít nghẹt, Hagfish tự uốn cong cơ thể thắt thành một nút số tám hoàn hảo, gạt phăng lớp nhớt từ đầu đến đuôi chỉ trong nháy mắt!". Bố cục: chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện thắt nút thân hình số 8 trượt dọc thân gạt sạch bọt nhớt ra ngoài cực kỳ điêu luyện; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L83</summary>

```text
HÌNH L83 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Một vòng đọ sức vũ khí đỉnh cao khiến thang điểm của ban giám khảo suýt chạm trần tuyệt đối!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vung tay hào hứng, màn hình hiển thị hàng loạt điểm số chín và mười rực rỡ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L84</summary>

```text
HÌNH L84 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Các nhà khoa học tại đại học Guelph phát hiện: độ đàn hồi của sợi tơ Hagfish khi kéo giãn còn vượt trội hơn cả sợi tơ nhện mạng tròn cự phách!". Bố cục: Kính hiển vi lực nguyên tử kéo giãn sợi protein chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện đàn hồi uốn lượn không hề đứt đoạn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L85</summary>

```text
HÌNH L85 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Cấu trúc xoắn ốc của các vi sợi protein hoạt động như những chiếc lò xo giảm chấn phân tử, hấp thụ toàn bộ lực xé rách của dòng nước xoáy!". Bố cục: Mô hình các cuộn protein xoắn lò xo co giãn linh hoạt trong làn nước biển cuộn xoáy; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L86</summary>

```text
HÌNH L86 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Ban giám khảo đã hội ý xong! Vòng một: Huy chương Đồng thuộc về Hải Ly với hàm răng bọc sắt! Huy chương Bạc thuộc về Cá Mút Đá với mạng lưới tơ nhớt siêu bền!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ búa gỗ công bố, khay huy chương phát sáng bay về phía các tuyển thủ.
```
</details>

<details><summary>L87</summary>

```text
HÌNH L87 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và Huy chương Vàng ba điểm xuất sắc thuộc về Gấu Túi Wombat với tấm khiên mông bọc thép công thủ toàn diện!". Bố cục: chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường tươi cười đeo chiếc huy chương vàng lấp lánh vào cổ, giơ tay chào khán giả trong tiếng reo hò rền vang.
```
</details>

<details><summary>L88</summary>

```text
HÌNH L88 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Một vòng đấu mở màn mãn nhãn! Bảng điểm Mùa ba chính thức nhảy số: Wombat dẫn đầu với ba điểm, Hagfish hai điểm, Hải Ly một điểm!". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng đèn: cột điểm của Wombat vươn lên 3 điểm, Hagfish 2 điểm, Hải Ly 1 điểm; các tuyển thủ khác quyết tâm lội ngược dòng.
```
</details>

<details><summary>L89</summary>

```text
HÌNH L89 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Không để khán giả phải chờ lâu, chúng ta bước ngay vào Vòng hai: Bản Lĩnh Tái Sinh và Nghệ Thuật Thoát Hiểm Khó Tin!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vung micro chỉ tay về phía sàn đấu, pháo hoa nước bắn tóe rực rỡ; tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng ô thử thách số hai mang biểu tượng vòng lặp vô cực.
```
</details>

<details><summary>L90</summary>

```text
HÌNH L90 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nếu như Vòng một là cuộc đọ sức của giáp sắt và móng vuốt cơ học, thì Vòng hai là nơi quy luật sinh học thông thường bị bẻ gãy hoàn toàn!". Bố cục: Màn hình chiếu biểu tượng tái sinh: tế bào phân chia, các nhánh mô mọc dài, và chuông sứa biến ngược thành mầm phôi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L91</summary>

```text
HÌNH L91 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Đối với đa phần sinh vật sống trên Trái Đất, mất đi một cơ quan bên trong cơ thể quan trọng đồng nghĩa với cái chết cận kề. Nhưng với các quái kiệt đêm nay, đó chỉ là một sự cố nhỏ trên đường đi dạo!". Bố cục: Hình ảnh trái tim hoạt hình bị rách rồi tự đan dệt lại nguyên vẹn phát ra ánh sáng kỳ diệu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L92</summary>

```text
HÌNH L92 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tuyển thủ đầu tiên xuất trận với nụ cười thiên thần: Kỳ Nhông Axolotl của đất nước Mexico!". Bố cục: chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói bơi nhẹ nhàng trong bể nước ngọt, sáu nhánh mang hồng xòe rộng rung rinh như cánh quạt, đôi mắt đen láy nhìn khán giả; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L93</summary>

```text
HÌNH L93 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khán giả đều biết Axolotl có thể mọc lại chân tay, nhưng công trình nghiên cứu trên tạp chí Nature 2009 đã phát hiện một sự thật chấn động hơn nhiều!". Bố cục: Mô hình hiển vi phóng to chồi tái sinh mầm chi: các tế bào màu sắc khác nhau phát sáng di chuyển có trật tự; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L94</summary>

```text
HÌNH L94 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Các tế bào tại mầm tái sinh không hề quay về trạng thái tế bào gốc vô định, mà chúng lưu giữ một bộ nhớ danh tính dòng dõi cực kỳ chuẩn xác!". Bố cục: Tế bào cơ màu đỏ chỉ phân chia tạo thành cơ mới, tế bào sụn màu xanh chỉ đúc thành sụn mới, không hề bị nhầm lẫn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L95</summary>

```text
HÌNH L95 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nhờ cơ chế này, Axolotl có thể tái tạo hoàn chỉnh một phần 3 quả tim bị tổn thương, mọc lại các thùy não và nối liền tủy sống bị đứt đoạn mà không để lại bất kỳ vết sẹo xơ hóa nào!". Bố cục: Hình ảnh đồ họa trái tim bị rách tự khép kín cơ tim đập nhịp nhàng, tủy sống nối liền các xung thần kinh phát sáng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L96</summary>

```text
HÌNH L96 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Đặc biệt hơn, chúng có khả năng tiếp nhận cấy ghép bên trong cơ thể từ bất kỳ cá thể Axolotl nào khác mà hệ miễn dịch hoàn toàn không hề có phản ứng đào thải mô ghép!". Bố cục: Hai cá thể chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói bơi cạnh nhau, cấy ghép mang hồng sang nhau phát triển tự nhiên hoàn hảo; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L97</summary>

```text
HÌNH L97 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Bạn có thể ghép mắt, ghép chân hay thậm chí ghép cả nửa bộ não từ một chú kỳ nhông khác sang, và cơ thể chúng vẫn tiếp nhận êm ru như đồ chính hãng của mình!". Bố cục: Hình ảnh chú kỳ nhông lắp ráp các bộ phận phát sáng hoạt động trơn tru không hề bị xung đột phần mềm sinh học; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L98</summary>

```text
HÌNH L98 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Cả khán đài ồ lên thán phục trước cỗ máy tái sinh hoàn hảo của thiên nhiên! Nhưng tiếng chuông ma thuật bất ngờ ngân vang từ chiếc ly thủy tinh nhỏ!". Bố cục: Dưới bàn giám khảo, chiếc ly phát ra ánh sáng hồng tím lung linh huyền ảo; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cúi xuống quan sát thích thú.
```
</details>

<details><summary>L99</summary>

```text
HÌNH L99 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Xin mời nữ hoàng đảo ngược thời gian: Sứa Bất Tử dài chỉ 4,5mm!". Bố cục: Hình ảnh phóng đại cực đại trên màn hình lớn: chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực trôi lơ lửng, các xúc tu mềm mại buông rủ như tơ trời; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Mười dị nhân mới. Tám vòng đấu sinh tử. Một chiếc vương miện tối cao!". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) dựng giữa sân vận động rực lửa ban đêm, phía trên lơ lửng chiếc vương miện vàng phát sáng, mười chiếc bóng tuyển thủ đứng bên dưới.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Gấu Wombat 35kg và Hải Ly răng sắt được đặt cược sẽ thắng. Còn Sứa Bất Tử 1 miligram... chuyên gia bảo tham gia cho vui!". Bố cục: chú Gấu Túi Wombat hoạt hình mập tròn 35kg màu nâu xám, chiếc mông bọc thép titan chống cắn, cầm xẻng đào hầm mini, vẻ mặt lì lợm kiên cường và chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo đứng oai vệ trên hai cột điểm cao vút rực lửa, bên dưới chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực và chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù đứng cạnh cột điểm thấp lè tè.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Vòng một: Cá Mút Đá Hagfish sở hữu sợi tơ nhớt bền gấp 10 lần tơ nhện và dai hơn sợi Kevlar!". Bố cục: chú Cá Mút Đá Hagfish hoạt hình trơn tuột màu xám tím nhạt, miệng tròn có râu xúc giác, toàn thân quấn bọt nhớt lấp lánh, thắt nút thân điêu luyện thắt nút thân số 8 phun ra luồng bọt nhớt phát sáng lấp lánh ngăn chặn kẻ thù dưới đáy biển.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Vòng hai: Chuột Chũi Mũi Sao đớp mồi trong 0,12 giây và ngửi mùi dưới nước bằng bong bóng khí!". Bố cục: chú Chuột Chũi Mũi Sao hoạt hình lông đen nhung mượt mà, mũi xòe ra 22 xúc tu đỏ hồng như bông hoa sao biển, đeo kính râm mù lòa nhưng phản xạ siêu thanh đeo kính râm xòe 22 xúc tu đỏ hồng hớp trọn ấu trùng trong nháy mắt.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Vòng ba: Kỳ Nhông Axolotl sở hữu bộ gen 32 tỷ cặp base tái sinh não tim mà không để lại sẹo!". Bố cục: chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói mỉm cười ngây thơ tỏa ánh hào quang hồng phấn, trái tim nhỏ lấp lánh phục hồi nguyên vẹn.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Vòng bốn: Đập nước Hải Ly tạo vùng ngập nước kỳ diệu ngăn chặn bão lửa và hạn hán cả thung lũng!". Bố cục: chú Hải Ly hoạt hình lông nâu hạt dẻ, chiếc đuôi dẹt như mái chèo, răng cửa màu cam phủ sắt sắc bén, đội mũ bảo hộ công trình màu vàng cầm thước đo đội mũ bảo hộ vàng tự hào đứng trên con đập gỗ vững chãi giữ dòng nước trong xanh.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Vòng năm: Hải Sâm lầy lội tiêu hóa 130 tấn trầm tích mỗi năm để bảo vệ rạn san hô!". Bố cục: chú Hải Sâm hoạt hình mập mạp màu nâu cam sần sùi không xương, vẻ mặt lầy lội bi hài, luôn cầm chiếc quạt giấy mini xua đuổi kẻ thù ung dung hút cát lọc sạch đáy biển rực rỡ sắc màu san hô.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Vòng sáu: Bạch Tuộc Mimic 9 bộ não biến hình 15 loài kịch độc chỉ trong 200 mili-giây!". Bố cục: chú Bạch Tuộc Mimic hoạt hình sọc vằn nâu trắng nghệ sĩ, 8 xúc tu uốn lượn biến ảo thành đủ hình dáng kỳ lạ, cầm chiếc mặt nạ biến hình uốn 8 xúc tu chuyển đổi từ rắn biển sang cá sư tử gai góc trong tích tắc.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Chung kết: ai mang lại công nghệ vĩ đại nhất cho loài người? Y học tái tạo mô của Axolotl hay gen telomere bất tử của Sứa?". Bố cục: Nhà khoa học hoạt hình soi kính hiển vi chiêm ngưỡng chuỗi DNA phát sáng của chú Kỳ Nhông Axolotl hoạt hình màu hồng phấn dễ thương, 6 nhánh mang ngoài xòe lông vũ màu đỏ hồng như chiếc vương miện, nụ cười ngây thơ tươi rói và chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Và tân vương Mùa ba là... sinh vật tí hon 1 miligram từng bị xem là mồi ngon dưới đáy biển!". Bố cục: chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực bay lơ lửng trên bục cao nhất đội chiếc vương miện vàng rực rỡ giữa pháo hoa nổ vang trời.
```
</details>

<details><summary>S11</summary>

```text
HÌNH S11 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bạn có đồng ý không? Xem trọn tám vòng đấu kịch tính trong video dài nhé,". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ và mười tuyển thủ cùng quay sang nhìn thẳng ra người xem, chú Sứa Bất Tử hoạt hình trong suốt hình chuông nhỏ xíu 4.5mm phát ánh sáng ma thuật hồng tím, đeo bùa hộ mệnh vòng lặp vô cực ở giữa giơ cúp vô địch lên.
```
</details>

<details><summary>S12</summary>

```text
HÌNH S12 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 3; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "vì ở đây có mười dị nhân mới, tám vòng đấu sinh tử, và một chiếc vương miện tối cao!". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) dựng giữa sân vận động rực lửa ban đêm, phía trên lơ lửng chiếc vương miện vàng phát sáng, mười chiếc bóng tuyển thủ đứng bên dưới.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/502 của video YouTube về 10 quái kiệt — Đại Hội Sinh Tồn Mùa 3). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: anh MC dẫn chương trình hoạt hình vui tính: tóc vuốt dựng, mặc bộ vest đỏ tươi, thắt nơ bướm vàng, cầm chiếc micro vàng, nụ cười rộng. Nhân vật phụ cố định: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/12 của video YouTube Shorts về 10 quái kiệt — Đại Hội Sinh Tồn Mùa 3). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: anh MC dẫn chương trình hoạt hình vui tính: tóc vuốt dựng, mặc bộ vest đỏ tươi, thắt nơ bướm vàng, cầm chiếc micro vàng, nụ cười rộng. Nhân vật phụ: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ. 
```
</details>

## 7. SEO

- **title:** [TẬP ĐẶC BIỆT] 10 Quái Kiệt Dị Nhân Phá Vỡ Mọi Định Luật Sinh Học: Ai Lên Ngôi Vô Địch?!
- **hook_paragraph:** Trọn bộ 10 sinh vật dị biệt nhất từ Tập 21 đến Tập 30 của kênh Vẽ Chuyện Hoang Dã chính thức quy tụ trong Đại Hội Sinh Tồn Mùa 3! 100% nội dung mới toanh đã kiểm chứng qua các tạp chí khoa học hàng đầu: từ Kỳ Nhông Axolotl mang bộ gen 32 tỷ base kháng ung thư, Cá Mút Đá Hagfish sở hữu sợi tơ nhớt bền gấp 10 lần tơ nhện và dai hơn Kevlar, Chuột Chũi Mũi Sao đớp mồi 0,12 giây và ngửi dưới nước, đến Sứa Bất Tử đảo ngược thời gian tế bào. Ai sẽ là nhà vô địch vĩ đại của Đấu Trường Dị Nhân?
- **question:** Nếu được sở hữu 1 siêu năng lực của 10 quái kiệt Mùa 3: tái sinh không sẹo của Axolotl, mông bọc thép của Wombat, hay khả năng đảo ngược thời gian của Sứa Bất Tử, bạn sẽ chọn năng lực nào? Hãy bình luận bên dưới nhé!
- **next_teaser:** Đại Hội Sinh Tồn Mùa 4 — 10 dũng sĩ săn mồi trên không và thảo nguyên (Chim Cắt Lớn Peregrine Falcon, Cá Voi Sát Thủ, Quạ Đen...)
- **shorts_title:** Đại Hội Sinh Tồn Mùa 3: 10 Dị Nhân Động Vật – Ai Vô Địch?! 👑 #shorts #dongvat
- **shorts_desc:** Axolotl mọc lại tim não, Hagfish 20 lít keo nhớt, Wombat mông bọc thép hay Sứa Bất Tử 4,5mm? Đấu trường siêu năng lực điên rồ nhất thế giới tự nhiên — nhà vô địch sẽ khiến bạn ngã ngửa! 👑
👉 Xem trọn bộ Đại Hội Sinh Tồn Mùa 3 trên kênh Vẽ Chuyện Hoang Dã.
- **bullets:** Vòng 1 – Vũ khí tự thân: Mông bọc thép 3cm Wombat nghiền sọ Dingo, Răng phủ sắt Hải Ly đốn hạ cổ thụ, Móng xương Wolverine đâm thủng da · Vòng 2 – Nghệ thuật thoát hiểm: Axolotl tái sinh não tim không sẹo, Hải Sâm xả ruột dính nhớt qua hậu môn, Bạch Tuộc Mimic biến hình 15 loài kịch độc trong 1 giây · Vòng 3 – Tốc độ phản xạ: Chuột Chũi Mũi Sao ăn mồi 0,12s nhanh nhất hành tinh & ngửi mùi dưới nước, Bạch Tuộc 8 xúc tu tư duy độc lập · Vòng 4 – Kỹ sư địa hình: Đập nước Hải Ly cứu hạn hán và chống cháy rừng, Mạng lưới hang ngầm Wombat 30m, Kiến nút chai bịt cửa tổ · Vòng 5 – Kháng thể siêu cấp: Bộ gen 32 tỷ cặp base chống ung thư của Axolotl, Gen bảo vệ telomere của Sứa Bất Tử, Lông ếch hô hấp dưới suối xiết · Vòng 6 – Người hùng sinh thái: Hải Sâm tiêu hóa 130 tấn trầm tích bảo vệ san hô, Tơ hagfish dọn sạch đáy biển sâu 1.000m · Vòng 7 – Cụ tổ cổ đại: Cá Mút Đá Hagfish sống trước khủng long 300 triệu năm, Hải Ly khổng lồ 100kg kỷ băng hà · Vòng 8 – Phúc khảo tin đồn: Sứa bất tử có thực sự bất tử trước rùa biển? Hải Ly có thích ăn gỗ? Ếch tự bẻ xương có thấy đau? · Chung kết – Món quà nhân loại: Tơ hagfish dệt áo chống đạn thế hệ mới, Y học tái tạo mô người từ Axolotl, Dược phẩm đảo ngược lão hóa từ Sứa
- **tags:** vẽ chuyện hoang dã, đại hội sinh tồn, đại hội sinh tồn mùa 3, thế giới động vật, động vật kỳ lạ, ếch lông wolverine, kỳ nhông axolotl, hải sâm, cá mút đá hagfish, bạch tuộc mimic, gấu túi wombat, chuột chũi mũi sao, kiến nổ cảm tử, sứa bất tử, hải ly, siêu năng lực động vật, khoa học thú vị, whiteboard animation, nghe trước khi ngủ
- **hashtags:** #VeChuyenHoangDa #TheGioiDongVat #DaiHoiSinhTon #MegaCompilation #DongVatKyLa #KhoaHoc

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/mega-03-dai-hoi-sinh-ton
python src/episode/pipeline.py tts    projects/mega-03-dai-hoi-sinh-ton     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/mega-03-dai-hoi-sinh-ton     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/mega-03-dai-hoi-sinh-ton     # phải in 'spec OK'
python scripts/audit_beats.py projects/mega-03-dai-hoi-sinh-ton              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/mega-03-dai-hoi-sinh-ton --force
python scripts/beat_sheet.py projects/mega-03-dai-hoi-sinh-ton               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/mega-03-dai-hoi-sinh-ton/audio/shorts.wav projects/mega-03-dai-hoi-sinh-ton/renders/mega-03-dai-hoi-sinh-ton_shorts.mp4
python src/episode/pipeline.py qa     projects/mega-03-dai-hoi-sinh-ton
python src/episode/pipeline.py seo    projects/mega-03-dai-hoi-sinh-ton
python src/episode/episode_doc.py     projects/mega-03-dai-hoi-sinh-ton
```

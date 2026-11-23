# TẬP 37 — LẠC ĐÀ SA MẠC · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-37-lac-da-sa-mac`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-37-lac-da-sa-mac`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F1` · **Persona giọng:** `bac_si` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Lạc Đà Sa Mạc |
| Tiêu đề YouTube | Bệnh Án Sinh Tồn Sa Mạc: Uống 200 Lít Nước Trong 3 Phút Và Bướu Mỡ Chống Nóng 50°C?! \| Tập 37 |
| Video dài | `renders/tap-37-lac-da-sa-mac_long.mp4` — 8:57.7 (537.7s) |
| Shorts | `renders/tap-37-lac-da-sa-mac_shorts.mp4` — 0:41.4 (41.4s) |
| Thumbnail | `renders/tap-37-lac-da-sa-mac_thumbnail.jpg` |
| Số hình | dài 70 beat / 70 ảnh riêng; Shorts 12 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.11**, Shorts tempo tự tính (≥ 1.12) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/70 của video YouTube về Lạc Đà Sa Mạc). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh màu nước thám hiểm sa mạc Ả Rập kết hợp ký họa thực vật học & giải phẫu Ba Tư (Mirage Oasis Botanical & Anatomical Watercolor): nét cọ ướt loang màu nước mềm mại giàu cảm xúc, lớp phủ cát vàng rực rỡ, chi tiết hoa văn Ả Rập tinh xảo, bình nước cổ, nhiệt kế sa mạc và đồ thị nhịp tim lâm sàng, phối màu vàng đất son ấm, hổ phách rực rỡ điểm xuyết lam ngọc turquoise quý phái; NỀN TRẮNG TINH hoàn toàn, không watermark, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng. Nhân vật phụ cố định: Cô y tá Cáo Sa Mạc Fennec tai to mặc áo blouse trắng cầm bảng kẹp nhiệt độ; Bác sĩ nội trú Chuột Nhảy Gerbil đeo kính tròn cầm ống tiêm mini; Bác sĩ Kền Kền già đeo kính lão cầm biểu đồ điện tâm đồ; Người du mục Bedouin mặc áo choàng thong dong nhóm lửa. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — BÀI TOÁN SỐC NHIỆT VÀ MẤT NƯỚC NĂM MƯƠI ĐỘ C
*Thẻ chương:* Bệnh nhân lạc đà bình thản bước qua chảo lửa tử thần

*Badge:* `CA CẤP CỨU` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene01_p0.wav` (523 ký tự) · mood `hao_hung`

```text
Chào mừng các y bác sĩ, các điều dưỡng viên và toàn thể thực tập sinh bước vào Ca trực cấp cứu đặc biệt của Bệnh viện Dã chiến Sa Mạc Sahara! [laughter] Hôm nay, chúng ta vừa tiếp nhận một bệnh nhân vô cùng kỳ lạ và bất quy tắc. Một đối tượng lang thang giữa chảo lửa năm mươi độ C, cát bỏng rát chân, không hề có giọt nước uống nào suốt hai tuần ròng rã, nhưng khi bước vào phòng khám, mạch đập vẫn đều đặn, huyết áp ổn định tuyệt đối và ánh mắt thì thảnh thơi nhai cỏ khô như thể đang đi nghỉ dưỡng tại bờ biển nhiệt đới!
```
**Part 1** → `audio/vs/scene01_p1.wav` (420 ký tự) · mood `don_dap`

```text
Đối tượng trên bàn hội chẩn của chúng ta hôm nay mang tên khoa học Camelus dromedarius, nhưng trong toàn bộ giới y khoa tự nhiên, chúng tôi gọi nó bằng một mật danh đầy kính nể: Cỗ Máy Lọc Nước Sa Mạc! Nếu một con người bình thường rơi vào hoàn cảnh này, cơ thể chúng ta sẽ nhanh chóng rơi vào trạng thái sốc nhiệt cấp độ bốn, máu đông đặc lại như thạch, suy đa tạng và tử vong chỉ sau chưa đầy bốn mươi tám giờ đồng hồ!
```
**Part 2** → `audio/vs/scene01_p2.wav` (182 ký tự) · 🎭 cameo `co_tro_ly`

```text
[surprise-oh] Báo cáo Bác sĩ trưởng khoa, chỉ số sinh tồn của bệnh nhân ghi nhận mất nước vượt ngưỡng hai mươi lăm phần trăm trọng lượng cơ thể mà không hề có dấu hiệu trụy tim mạch!
```
**Part 3** → `audio/vs/scene01_p3.wav` (371 ký tự) · mood `tram_bi_an`

```text
Báo cáo rất chính xác thưa y tá trưởng! Đối với cơ thể người, chỉ cần mất mười lăm phần trăm lượng nước trong cơ thể là tim đã ngừng đập vì thể tích máu sụt giảm nghiêm trọng. Thế nhưng Cỗ Máy Lọc Nước Sa Mạc có thể mất tới ba mươi phần trăm, thậm chí bốn mươi phần trăm lượng nước trong cơ thể mà vẫn bước đi hiên ngang vượt qua những cồn cát bỏng cháy hàng ngàn cây số!
```
**Part 4** → `audio/vs/scene01_p4.wav` (218 ký tự) · mood `hao_hung`

```text
Vậy đâu là những vũ khí y sinh học tối mật giúp sinh vật này thách thức mọi định luật sinh lý học truyền thống? Mời toàn thể hội đồng bác sĩ mở tập hồ sơ bệnh án số một để cùng tôi bóc tách phép màu giải phẫu đầu tiên!
```

### scene02 — CHIẾC BƯỚU MỠ NĂNG LƯỢNG CHỨ KHÔNG PHẢI TÚI NƯỚC
*Thẻ chương:* Giải mã lầm tưởng kinh điển về kho chứa nước trên lưng

*Badge:* `BỆNH ÁN SỐ 1` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene02_p0.wav` (427 ký tự) · mood `hao_hung`

```text
Hãy bắt đầu với chẩn đoán sai lầm phổ biến nhất trong lịch sử nhân loại: Chiếc bướu khổng lồ trên lưng lạc đà! Hàng triệu người từ xưa đến nay vẫn ngây thơ tin rằng bên trong chiếc bướu đó là một bồn chứa nước di động khổng lồ, nơi lạc đà tích trữ hàng chục lít nước tinh khiết để uống dần khi khát. [laughter] Nếu bác sĩ nào chẩn đoán như vậy trong phòng thi chuyên khoa, tôi xin phép thu hồi chứng chỉ hành nghề ngay lập tức!
```
**Part 1** → `audio/vs/scene02_p1.wav` (378 ký tự) · mood `tram_bi_an`

```text
Dưới lát cắt chụp cộng hưởng từ và sinh thiết giải phẫu, chiếc bướu này không chứa bất kỳ giọt nước lỏng nào cả! Toàn bộ chiếc bướu nặng tới bốn mươi kilôgam, thậm chí tám mươi kilôgam ở những con đực trưởng thành, là một khối mỡ đậm đặc tinh khiết! Đây là một kho dự trữ năng lượng sinh hóa siêu cô đặc giúp Cỗ Máy Lọc Nước Sa Mạc sinh tồn suốt cả tháng trời không cần ăn uống.
```
**Part 2** → `audio/vs/scene02_p2.wav` (133 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
[surprise-oh] Ủa Bác sĩ ơi, vậy tại sao mỡ lại tập trung hết lên lưng mà không phân bố đều khắp cơ thể như động vật khác thưa bác sĩ?
```
**Part 3** → `audio/vs/scene02_p3.wav` (379 ký tự) · mood `don_dap`

```text
Một câu hỏi chẩn đoán cực kỳ thông minh thưa bác sĩ nội trú! Nếu lớp mỡ dày cộp đó phân bố đều dưới da như loài gấu bắc cực hay hải cẩu, cơ thể lạc đà sẽ bị bọc kín trong một chiếc áo phao cách nhiệt dày cộp. Dưới cái nắng năm mươi độ C của sa mạc, nhiệt lượng bên trong cơ thể sẽ hoàn toàn không thể thoát ra ngoài và lạc đà sẽ bị nấu chín từ bên trong chỉ sau vài giờ vận động!
```
**Part 4** → `audio/vs/scene02_p4.wav` (351 ký tự) · mood `tram_bi_an`

```text
Bằng cách gom toàn bộ lượng mỡ cách nhiệt tập trung duy nhất lên đỉnh lưng, chiếc bướu đóng vai trò như một chiếc dù che nắng tự nhiên, hấp thụ trực tiếp ánh nắng mặt trời rọi thẳng từ trên cao xuống đỉnh đầu, trong khi toàn bộ phần cơ thể còn lại hoàn toàn không có mỡ dưới da, cho phép nhiệt lượng tỏa thẳng ra môi trường xung quanh một cách tối đa!
```
**Part 5** → `audio/vs/scene02_p5.wav` (261 ký tự) · mood `am_ap`

```text
Chưa dừng lại ở đó đâu các đồng nghiệp trẻ! Khi quá trình oxy hóa chất béo diễn ra, mỗi gam mỡ trong bướu sẽ giải phóng hơn một gam nước chuyển hóa nội sinh, giúp lạc đà tự cấp ẩm cho từng tế bào ngay từ bên trong mà chẳng cần một giọt nước mưa nào từ bầu trời!
```

### scene03 — TẾ BÀO HỒNG CẦU HÌNH OVAL CO GIÃN VÔ HẠN
*Thẻ chương:* Tuyệt tác tế bào học chống vỡ tan và chống đông máu

*Badge:* `BỆNH ÁN SỐ 2` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene03_p0.wav` (485 ký tự) · mood `hao_hung`

```text
Bây giờ, xin mời các chuyên gia huyết học bước vào phòng xét nghiệm tế bào học, nơi cất giữ bí mật y sinh tinh xảo nhất của Cỗ Máy Lọc Nước Sa Mạc: Những tế bào hồng cầu hình oval kỳ dị! Ở toàn bộ các loài động vật có vú khác, bao gồm cả con người, tế bào hồng cầu luôn có hình đĩa lõm hai mặt tròn trịa. Khi chúng ta mất nước nặng, máu trở nên đặc quánh và các tế bào hồng cầu hình tròn sẽ bị mắc kẹt tại các mao mạch nhỏ hẹp, gây tắc nghẽn tuần hoàn và dẫn đến tử vong ngay tức khắc.
```
**Part 1** → `audio/vs/scene03_p1.wav` (269 ký tự) · mood `don_dap`

```text
Thế nhưng hồng cầu của lạc đà lại có hình oval bầu dục thuôn dài! Cấu trúc khí động học đặc biệt này cho phép chúng trượt lướt qua các mao mạch siêu nhỏ một cách trơn tru ngay cả khi máu của lạc đà đã đặc quánh lại như si-rô vì mất nước kéo dài suốt nhiều ngày ròng rã!
```
**Part 2** → `audio/vs/scene03_p2.wav` (127 ký tự) · 🎭 cameo `co_tro_ly`

```text
[surprise-oh] Thưa Giáo sư, khi tìm thấy nguồn nước, bệnh nhân có thể uống một lượng nước khổng lồ trong tích tắc đúng không ạ?
```
**Part 3** → `audio/vs/scene03_p3.wav` (415 ký tự) · mood `hao_hung`

```text
Chính xác là một kỳ tích tiếp nước ngoạn mục! Khi tìm thấy một vũng nước hay ốc đảo, Cỗ Máy Lọc Nước Sa Mạc có thể nốc cạn một trăm ba mươi lít nước, thậm chí hai trăm lít nước chỉ trong vòng chưa đầy mười lăm phút! [laughter] Nếu là người bình thường uống ngần ấy nước, hiện tượng ngộ độc nước sẽ xảy ra tức khắc: Áp suất thẩm thấu tụt giảm khiến các tế bào hồng cầu tròn vỡ tung hàng loạt và tử vong ngay tại chỗ!
```
**Part 4** → `audio/vs/scene03_p4.wav` (314 ký tự) · mood `tram_bi_an`

```text
Nhưng màng tế bào hồng cầu hình oval của lạc đà có khả năng co giãn phi thường: Chúng có thể phồng to gấp hai trăm bốn mươi phần trăm thể tích ban đầu mà không hề bị vỡ! Chúng nở ra như những quả bóng bay co giãn vô hạn, nhẹ nhàng hấp thụ toàn bộ lượng nước khổng lồ đó vào hệ tuần hoàn một cách an toàn tuyệt đối!
```
**Part 5** → `audio/vs/scene03_p5.wav` (136 ký tự) · mood `don_dap`

```text
Nghĩa là thể tích máu của nó có thể tăng vọt gấp đôi trong mười lăm phút mà thành mạch máu không hề bị vỡ hay rách toác sao thưa Bác sĩ?
```
**Part 6** → `audio/vs/scene03_p6.wav` (226 ký tự) · mood `hao_hung`

```text
Hoàn toàn chính xác thưa trợ lý! Các mạch máu của lạc đà sở hữu lớp cơ trơn đàn hồi siêu đẳng, kết hợp cùng áp lực thẩm thấu nội bào cân bằng hoàn mỹ, biến toàn bộ hệ tuần hoàn của nó thành một hồ chứa di động đàn hồi vô song!
```

### scene04 — QUẢ THẬN SIÊU LỌC CÔ ĐẶC NƯỚC TIỂU THÀNH SI-RÔ
*Thẻ chương:* Hệ thống tái hấp thu nước hiệu suất chín mươi chín phần trăm

*Badge:* `BỆNH ÁN SỐ 3` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene04_p0.wav` (405 ký tự) · mood `hao_hung`

```text
Tiếp theo, xin mời hội đồng kiểm tra hệ thống cơ quan nội tạng đắt giá nhất của bệnh nhân: Đôi quả thận siêu lọc! Khi nước là thứ quý hơn vàng ròng giữa sa mạc, việc bài tiết lãng phí dù chỉ một giọt nước cũng đồng nghĩa với bản án tử hình. Thận của Cỗ Máy Lọc Nước Sa Mạc sở hữu quai Henle dài gấp nhiều lần so với các loài động vật thông thường, tạo ra một gradient nồng độ thẩm thấu cực kỳ khủng khiếp.
```
**Part 1** → `audio/vs/scene04_p1.wav` (355 ký tự) · mood `tram_bi_an`

```text
Hệ thống ống thận này vắt kiệt từng phân tử nước từ dịch lọc trước khi bài tiết ra ngoài. Kết quả là nước tiểu của lạc đà cô đặc đến mức sánh đặc như si-rô đặc quẹt, có nồng độ muối và khoáng chất cao gấp đôi nước biển tự nhiên! [laughter] Rất hiếm có một loài động vật có vú nào có thể bài xuất nước tiểu đậm đặc đến mức đó mà không bị suy thận cấp tính!
```
**Part 2** → `audio/vs/scene04_p2.wav` (124 ký tự) · 🎭 cameo `co_tro_ly`

```text
[surprise-oh] Báo cáo Bác sĩ trưởng, chất thải rắn của bệnh nhân khô khốc đến mức có thể đốt cháy làm chất đốt ngay lập tức!
```
**Part 3** → `audio/vs/scene04_p3.wav` (264 ký tự) · mood `hao_hung`

```text
Báo cáo hoàn toàn trùng khớp với thực nghiệm lâm sàng! Ruột già của lạc đà tái hấp thu nước triệt để đến mức phân của chúng thải ra khô cong như những viên sỏi gỗ, đến mức người du mục Bedouin có thể nhặt lên và nhóm lửa đun nấu ngay tại chỗ mà không cần phơi khô!
```
**Part 4** → `audio/vs/scene04_p4.wav` (204 ký tự) · mood `don_dap`

```text
Mọi giọt ẩm đi vào cơ thể đều bị giữ lại và tuần hoàn khép kín với hiệu suất tái sử dụng lên tới chín mươi chín phần trăm, biến cơ thể lạc đà thành một nhà máy xử lý nước tuần hoàn hoàn hảo nhất Trái Đất!
```
**Part 5** → `audio/vs/scene04_p5.wav` (253 ký tự) · mood `tram_bi_an`

```text
Thậm chí dạ dày của lạc đà còn có cấu trúc ba ngăn chuyên biệt với các tuyến tiết chất nhầy đặc thù, cho phép nó nhai ngấu nghiến những cành cây gai góc nhọn hoắt và cây xương rồng sa mạc chứa đầy độc tố mà niêm mạc không hề bị xước xát lấy một vết nhỏ!
```

### scene05 — ỐNG THỞ NGƯNG TỤ HƠI NƯỚC VÀ LỖ MŨI VAN MỘT CHIỀU
*Thẻ chương:* Hệ thống làm mát điều hòa và khóa bụi cát sa mạc

*Badge:* `BỆNH ÁN SỐ 4` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene05_p0.wav` (357 ký tự) · mood `hao_hung`

```text
Nếu các bạn nghĩ rằng kiểm soát bài tiết là đã chặn đứng mọi lối thoát của nước, thì các bác sĩ đã bỏ quên con đường bốc hơi vô hình nhưng cực kỳ nguy hiểm: Đường hô hấp! Mỗi hơi thở ra của con người mang theo một lượng hơi nước ấm áp bốc hơi vào không khí. Giữa sa mạc khô hạn, nếu thở ra lượng hơi ẩm đó, cơ thể sẽ bị rút cạn kiệt chỉ sau vài giờ thở dốc.
```
**Part 1** → `audio/vs/scene05_p1.wav` (378 ký tự) · mood `tram_bi_an`

```text
Để giải bài toán này, khoang mũi của Cỗ Máy Lọc Nước Sa Mạc được cấu tạo từ các vách xoắn ốc cuộn nhiều tầng phủ đầy niêm mạc hút ẩm đặc biệt. Khi lạc đà thở ra, không khí ấm và ẩm từ phổi đi qua khoang mũi lạnh sẽ bị ngưng tụ hơi nước lại lập tức! Lượng nước ngưng tụ này thấm ngược trở lại niêm mạc mũi để tái hấp thu vào máu, chỉ có luồng không khí khô ráo được thở ra ngoài!
```
**Part 2** → `audio/vs/scene05_p2.wav` (113 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
[surprise-oh] Bác sĩ ơi, còn khi bão cát ập đến thì sao ạ? Bụi cát có tràn vào phổi làm ngạt thở bệnh nhân không?
```
**Part 3** → `audio/vs/scene05_p3.wav` (342 ký tự) · mood `hao_hung`

```text
Một cơ chế bảo hộ đường thở hoàn mỹ thưa trợ lý! Lỗ mũi của lạc đà được trang bị các cơ vòng van một chiều có thể tự động khép chặt lại hoàn toàn khi có gió cát! Kết hợp cùng đôi hàng mi dày hai tầng đan xen và lớp màng chớp trong suốt bảo vệ mắt, lạc đà có thể thản nhiên bước đi giữa tâm bão cát mù mịt mà không hề hít phải một hạt bụi nào!
```
**Part 4** → `audio/vs/scene05_p4.wav` (299 ký tự) · mood `don_dap`

```text
Thậm chí thân nhiệt của lạc đà còn có khả năng dao động linh hoạt từ ba mươi bốn độ C vào ban đêm lên tới bốn mươi mốt độ C vào ban ngày! Bằng cách tự nâng nhiệt độ cơ thể lên ngang bằng nhiệt độ môi trường, chúng hoàn toàn không cần đổ mồ hôi để làm mát, tiết kiệm thêm hàng chục lít nước mỗi ngày!
```
**Part 5** → `audio/vs/scene05_p5.wav` (181 ký tự) · mood `am_ap`

```text
Một hệ thống điều hòa sinh học tự cân bằng quá đỗi diệu kỳ! Bệnh nhân không chống lại cái nóng thiêu đốt của sa mạc, mà chọn cách hòa làm một với nhịp điệu nhiệt độ của thiên nhiên!
```

### scene06 — TINH HOA Y HỌC PHỎNG SINH HỌC GIỮA BIỂN CÁT
*Thẻ chương:* Bài học sinh tồn vĩ đại cho tương lai loài người

*Badge:* `XUẤT VIỆN` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene06_p0.wav` (308 ký tự) · mood `hao_hung`

```text
Thưa toàn thể hội đồng y khoa, sau khi khám nghiệm toàn diện từ bướu mỡ chống sốc nhiệt, tế bào hồng cầu hình oval co giãn vô hạn, quả thận siêu lọc cho đến khoang mũi ngưng tụ hơi thở, chúng tôi xin long trọng ký giấy xuất viện cho bệnh nhân Lạc Đà Sa Mạc với xếp loại thể lực phi thường xuất sắc tuyệt đối!
```
**Part 1** → `audio/vs/scene06_p1.wav` (363 ký tự) · mood `tram_bi_an`

```text
Cỗ Máy Lọc Nước Sa Mạc không đơn thuần là một con thú thồ hàng nhẫn nại, mà là đỉnh cao của công nghệ phỏng sinh học mà nền y học hiện đại của thế kỷ hai mươi mốt vẫn đang ngày đêm nghiên cứu ứng dụng. Các nhà khoa học NASA đang dựa trên cấu trúc hồng cầu co giãn của lạc đà để nghiên cứu các loại dịch truyền nhân tạo cho các phi hành gia bay vào không gian sâu.
```
**Part 2** → `audio/vs/scene06_p2.wav` (143 ký tự) · mood `am_ap`

```text
[laughter] Quả là một bậc thầy sinh tồn vĩ đại của tự nhiên thưa Bác sĩ trưởng! Thiên nhiên luôn là người thầy thuốc thông thái và vĩ đại nhất!
```
**Part 3** → `audio/vs/scene06_p3.wav` (375 ký tự) · mood `hao_hung`

```text
Hoàn toàn chuẩn xác! Lần tới khi bạn nhìn thấy hình ảnh chú lạc đà thong dong sải bước trên những đồi cát sa mạc hoang vu, hãy nhớ rằng bạn đang chiêm ngưỡng một cỗ máy sinh học tinh vi bậc nhất mà tạo hóa từng tạo tác! Còn bây giờ, giữa chiếc bướu mỡ năng lượng và tế bào hồng cầu oval co giãn, giải pháp y sinh nào làm bạn kinh ngạc nhất? Hãy để lại bình luận bên dưới nhé!
```
**Part 4** → `audio/vs/scene06_p4.wav` (218 ký tự) · mood `am_ap`

```text
Và đừng quên bấm đăng ký kênh để đón xem Tập ba mươi tám khám phá cỗ máy leo núi trọng lực chín mươi độ của Dê Núi Bắc Mỹ! Hẹn gặp lại toàn thể các bạn trong chuyến hành trình khám phá những kỳ quan sinh học tiếp theo!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Bạn có biết loài động vật nào có thể uống cạn hai trăm lít nước chỉ trong mười lăm phút mà không bị vỡ hồng cầu chết ngay lập tức không? [laughter] Đó chính là Lạc Đà Sa Mạc — Cỗ Máy Lọc Nước siêu cấp của thiên nhiên! Trái ngược với hiểu lầm của hàng triệu người, chiếc bướu trên lưng nó không hề chứa một giọt nước nào mà là một khối bướu mỡ nặng tới bốn mươi kilôgam giúp chống sốc nhiệt năm mươi độ C! [dissatisfaction-hnn] Bí mật sinh tử thực sự nằm ở tế bào hồng cầu hình oval độc nhất vô nhị: Chúng có thể phồng to gấp hai trăm bốn mươi phần trăm thể tích để nạp nước tức thì, kết hợp cùng quả thận siêu lọc cô đặc nước tiểu thành si-rô đặc quẹt! Nhờ đó, sinh vật phi thường này có thể nhịn uống suốt ba mươi ngày giữa chảo lửa sa mạc mà vẫn sống khỏe re!
```

**Whisper prompt:** `Lạc Đà Sa Mạc, Camelus dromedarius, Cỗ Máy Lọc Nước Sa Mạc, bướu mỡ, hồng cầu oval, siêu lọc thận, 50 độ C, 200 lít nước, Henle`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| Tập ba mươi bảy | Tập 37 |
| Tập ba mươi tám | Tập 38 |
| năm mươi độ C | 50°C |
| bốn mươi mốt độ C | 41°C |
| ba mươi bốn độ C | 34°C |
| ba mươi độ C | 30°C |
| chín mươi độ | 90° |
| hai trăm lít nước | 200 lít nước |
| một trăm ba mươi lít nước | 130 lít nước |
| bốn mươi tám giờ | 48 giờ |
| hai mươi bốn giờ | 24 giờ |
| mười lăm phút | 15 phút |
| ba phút | 3 phút |
| bốn mươi ngày | 40 ngày |
| ba mươi ngày | 30 ngày |
| hai tuần | 2 tuần |
| mười lăm phần trăm | 15% |
| hai mươi lăm phần trăm | 25% |
| ba mươi phần trăm | 30% |
| bốn mươi phần trăm | 40% |
| chín mươi chín phần trăm | 99% |
| hai trăm bốn mươi phần trăm | 240% |
| tám mươi kilôgam | 80 kg |
| bốn mươi kilôgam | 40 kg |
| năm trăm kilôgam | 500 kg |
| hai ngàn | 2.000 |
| một ngàn dặm | 1.000 dặm |
| thế kỷ hai mươi mốt | thế kỷ 21 |
| hàng triệu năm | hàng triệu năm |
| triệu năm | triệu năm |
| Camelus | Camelus |
| dromedarius | dromedarius |
| Henle | Henle |
| NASA | NASA |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · BÀI TOÁN SỐC NHIỆT VÀ MẤT NƯỚC NĂM MƯƠI ĐỘ C · 86.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.3 (9.3s) | L01 | Chào mừng các y bác sĩ, các điều dưỡng viên và toàn thể thực tập sinh bước vào Ca trực cấp cứu đặc biệt của Bệnh viện Dã chiến Sa Mạc Sahara! Hôm nay, chúng |  | Phòng cấp cứu dã chiến Sahara mở ra: Bác sĩ trưởng chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng đứng bên bàn hội chẩn, tay chỉ vào biểu đồ điện tâm đồ sa mạc màu nước lung linh. |
| b02 | 00:09.3–00:13.2 (4.0s) | L02 | ta vừa tiếp nhận một bệnh nhân vô cùng kỳ lạ và bất quy tắc. Một đối tượng lang thang |  | Bệnh nhân lạc đà thong dong bước vào lều y tế dã chiến, xung quanh là cồn cát sa mạc vàng rực phản chiếu ánh mặt trời. chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc. |
| b03 | 00:13.2–00:17.6 (4.4s) | L03 | giữa chảo lửa 50°C, cát bỏng rát chân, không hề có giọt nước uống nào | **50°C** · chảo lửa sa mạc · R/360 · [0.65, 0.45] | Nhiệt kế sa mạc thủy ngân dâng cao chạm mốc 50 độ C đỏ rực: Cát bốc hơi nóng hầm hập. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b04 | 00:17.6–00:21.5 (3.9s) | L04 | suốt 2 tuần ròng rã, nhưng khi bước vào phòng khám, mạch đập vẫn đều đặn, | **2 TUẦN** · nhịn nước liên tục · L/400 · [0.35, 0.45] | Bản đồ vệ tinh sa mạc Sahara kéo dài hai tuần không có bóng một giọt nước: chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng vẫn nhai cỏ khô thảnh thơi. |
| b05 | 00:21.5–00:29.5 (8.0s) | L05 | huyết áp ổn định tuyệt đối và ánh mắt thì thảnh thơi nhai cỏ khô như thể đang đi nghỉ dưỡng tại bờ biển nhiệt đới! Đối tượng trên bàn hội chẩn của chúng ta |  | Máy đo huyết áp y tế kim chỉ vạch xanh an toàn tuyệt đối: chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng mỉm cười nháy mắt với các bác sĩ. |
| b06 | 00:29.5–00:35.8 (6.3s) | L06 | hôm nay mang tên khoa học Camelus dromedarius, nhưng trong toàn bộ giới y khoa tự nhiên, chúng tôi gọi nó bằng một mật danh đầy kính nể: |  | Hồ sơ bệnh án bìa da cổ phong cách Ả Rập mở ra, ghi rõ danh pháp khoa học Camelus dromedarius với hoa văn màu nước lam ngọc. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b07 | 00:35.8–00:40.6 (4.8s) | L07 | Cỗ Máy Lọc Nước Sa Mạc! Nếu một con người bình thường rơi vào hoàn cảnh này, cơ thể chúng ta sẽ nhanh |  | chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng tạo dáng kiêu hãnh với chiếc ống nghe bác sĩ lấp lánh dưới ánh nắng sa mạc rực rỡ. |
| b08 | 00:40.6–00:45.7 (5.1s) | L08 | chóng rơi vào trạng thái sốc nhiệt cấp độ bốn, máu đông đặc lại như thạch, suy đa tạng và tử vong chỉ sau |  | Một anh chàng người que ngất lịm trên cát nóng vì kiệt nước, trên đầu hiện biểu tượng giọt nước cạn kiệt màu đỏ báo động. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b09 | 00:45.7–01:00.7 (15.0s) | L09 | chưa đầy 48 giờ đồng hồ! Báo cáo Bác sĩ trưởng khoa, chỉ số sinh tồn của bệnh nhân ghi nhận mất nước vượt ngưỡng 25% trọng lượng cơ thể mà không hề có dấu hiệu trụy tim mạch! Báo cáo rất chính xác thưa y tá trưởng! Đối với cơ thể người, chỉ cần | **48 GIỜ** · giới hạn người tử vong · R/380 · [0.68, 0.45] | Đồng hồ cát thời gian 48 giờ chảy xiết: Mô hình tim người que ngừng đập vì trụy tuần hoàn. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b10 | 01:00.7–01:07.2 (6.5s) | L10 | mất 15% lượng nước trong cơ thể là tim đã ngừng đập vì thể tích máu sụt giảm nghiêm trọng. Thế nhưng Cỗ Máy Lọc Nước Sa Mạc | **15%** · người ngừng đập · L/390 · [0.35, 0.45] | Cô y tá Cáo Fennec tai to cầm bảng kẹp hồ sơ báo cáo chỉ số mất nước vượt ngưỡng 25% an toàn. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b11 | 01:07.2–01:21.7 (14.5s) | L11 | có thể mất tới 30%, thậm chí 40% lượng nước trong cơ thể mà vẫn bước đi hiên ngang vượt qua những cồn cát bỏng cháy hàng ngàn cây số! Vậy đâu là những vũ khí y sinh học tối mật giúp sinh vật này thách thức mọi định luật sinh lý học truyền thống? Mời toàn thể hội đồng bác | **30%** · lạc đà chịu tải · R/370 · [0.65, 0.45]<br>**40%** · giới hạn tối đa · L/420 · [0.35, 0.5] | Cột mốc so sánh tử vong: Người ngừng thở ở mức mất nước 15%, còn lạc đà vẫn chịu tải tới 40% trọng lượng. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b12 | 01:21.7–01:26.2 (4.5s) | L12 | sĩ mở tập hồ sơ bệnh án số một để cùng tôi bóc tách phép màu giải phẫu đầu tiên! |  | chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng lật giở trang hồ sơ bệnh án số 1 có con dấu sáp đỏ uy tín, chuẩn bị bóc tách bí ẩn chiếc bướu. |

### scene02 · CHIẾC BƯỚU MỠ NĂNG LƯỢNG CHỨ KHÔNG PHẢI TÚI NƯỚC · 95.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.5 (10.5s) | L13 | Hãy bắt đầu với chẩn đoán sai lầm phổ biến nhất trong lịch sử nhân loại: Chiếc bướu khổng lồ trên lưng lạc đà! Hàng triệu người từ xưa đến nay vẫn ngây thơ tin rằng bên trong chiếc bướu đó |  | Bức tranh giải phẫu bướu lạc đà màu nước phong cách cổ điển: Chiếc bướu cao sừng sững phát sáng màu vàng kim ấm áp. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b02 | 00:10.5–00:23.1 (12.6s) | L14 | là một bồn chứa nước di động khổng lồ, nơi lạc đà tích trữ hàng chục lít nước tinh khiết để uống dần khi khát. Nếu bác sĩ nào chẩn đoán như vậy trong phòng thi chuyên khoa, tôi xin phép thu hồi chứng chỉ hành nghề ngay lập tức! Dưới |  | Hình vẽ hài hước một chiếc bồn inox chứa nước gắn trên lưng lạc đà bị đánh dấu gạch chéo màu đỏ to tướng: Lầm tưởng kinh điển. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b03 | 00:23.1–00:28.6 (5.5s) | L15 | lát cắt chụp cộng hưởng từ và sinh thiết giải phẫu, chiếc bướu này không chứa bất kỳ giọt nước lỏng nào cả! Toàn bộ chiếc |  | Màn hình máy MRI y tế chiếu rõ cấu trúc bên trong chiếc bướu: Toàn bộ là mô mỡ lipid vàng óng, không hề có giọt nước nào. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b04 | 00:28.6–00:38.2 (9.6s) | L16 | bướu nặng tới 40 kg, thậm chí 80 kg ở những con đực trưởng thành, là một khối mỡ đậm đặc tinh khiết! Đây là một kho dự trữ năng lượng sinh hóa siêu cô đặc giúp Cỗ Máy Lọc Nước Sa | **40 KG** · khối lượng bướu mỡ · R/370 · [0.65, 0.45] | Cân y tế đo trọng lượng bướu mỡ nhảy số từ 40 kg đến 80 kg: chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng đứng vỗ vỗ chiếc bướu kiêu hãnh. |
| b05 | 00:38.2–00:43.5 (5.3s) | L17 | Mạc sinh tồn suốt cả tháng trời không cần ăn uống. Ủa Bác sĩ ơi, | **30 NGÀY** · nhịn ăn liên tục · L/390 · [0.35, 0.45] | chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng thong thả bước đi trên con đường tơ lụa giữa sa mạc mênh mông suốt 30 ngày đêm không cần dừng ăn. chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc. |
| b06 | 00:43.5–00:52.2 (8.7s) | L18 | vậy tại sao mỡ lại tập trung hết lên lưng mà không phân bố đều khắp cơ thể như động vật khác thưa bác sĩ? Một câu hỏi chẩn đoán cực kỳ thông minh thưa bác sĩ nội trú! Nếu lớp mỡ dày |  | Bác sĩ nội trú Chuột Nhảy Gerbil đeo kính tròn thắc mắc chỉ tay vào lưng chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng. |
| b07 | 00:52.2–01:03.5 (11.2s) | L19 | cộp đó phân bố đều dưới da như loài gấu bắc cực hay hải cẩu, cơ thể lạc đà sẽ bị bọc kín trong một chiếc áo phao cách nhiệt dày cộp. Dưới cái nắng 50°C của sa mạc, nhiệt lượng bên trong cơ thể sẽ hoàn toàn không thể thoát ra ngoài và lạc đà |  | Hình ảnh chú gấu bắc cực béo múp míp mặc áo phao dày cộp toát mồ hôi đầm đìa dưới nắng sa mạc. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b08 | 01:03.5–01:06.3 (2.9s) | L20 | sẽ bị nấu chín từ bên trong chỉ sau vài giờ vận động! Bằng |  | Mô phỏng nhiệt học: Cơ thể bị om nhiệt màu đỏ rực như nồi áp suất nếu mỡ bao quanh toàn thân. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b09 | 01:06.3–01:20.0 (13.7s) | L21 | cách gom toàn bộ lượng mỡ cách nhiệt tập trung duy nhất lên đỉnh lưng, chiếc bướu đóng vai trò như một chiếc dù che nắng tự nhiên, hấp thụ trực tiếp ánh nắng mặt trời rọi thẳng từ trên cao xuống đỉnh đầu, trong khi toàn bộ phần cơ thể còn lại hoàn toàn không có mỡ dưới da, cho |  | Sơ đồ luồng nhiệt: Bướu mỡ trên lưng hoạt động như chiếc ô dù phản xạ toàn bộ tia nắng mặt trời gay gắt. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b10 | 01:20.0–01:25.9 (5.9s) | L22 | phép nhiệt lượng tỏa thẳng ra môi trường xung quanh một cách tối đa! Chưa dừng lại ở đó đâu các đồng nghiệp trẻ! Khi |  | Vùng bụng và bốn chân của chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng tỏa ra các luồng khí mát màu xanh lam, giúp cơ thể tản nhiệt siêu tốc. |
| b11 | 01:25.9–01:31.3 (5.3s) | L23 | quá trình oxy hóa chất béo diễn ra, mỗi gam mỡ trong bướu sẽ giải phóng hơn một gam nước chuyển hóa nội sinh, giúp lạc |  | Phương trình phản ứng sinh hóa phát sáng: 1 gam mỡ lipid phân giải tạo ra 1,1 gam nước chuyển hóa nội sinh. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b12 | 01:31.3–01:35.9 (4.6s) | L24 | đà tự cấp ẩm cho từng tế bào ngay từ bên trong mà chẳng cần một giọt nước mưa nào từ bầu trời! |  | chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng mỉm cười sảng khoái như vừa được uống một ly nước mát ngọt lành ngay giữa biển cát. |

### scene03 · TẾ BÀO HỒNG CẦU HÌNH OVAL CO GIÃN VÔ HẠN · 99.8s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:14.1 (14.1s) | L25 | Bây giờ, xin mời các chuyên gia huyết học bước vào phòng xét nghiệm tế bào học, nơi cất giữ bí mật y sinh tinh xảo nhất của Cỗ Máy Lọc Nước Sa Mạc: Những tế bào hồng cầu hình oval kỳ dị! Ở toàn bộ các loài động vật có vú khác, bao gồm cả con người, tế bào hồng cầu luôn |  | Kính hiển vi y khoa phóng đại giọt nước màu màu nước đỏ thắm: Các tế bào hồng cầu hình oval bơi lội mềm mại. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b02 | 00:14.1–00:25.7 (11.6s) | L26 | có hình đĩa lõm hai mặt tròn trịa. Khi chúng ta mất nước nặng, máu trở nên đặc quánh và các tế bào hồng cầu hình tròn sẽ bị mắc kẹt tại các mao mạch nhỏ hẹp, gây tắc nghẽn tuần hoàn và dẫn đến tử vong ngay tức khắc. Thế |  | Hồng cầu hình tròn của con người bị vón cục tắc nghẽn trong lòng mao mạch nước màu hẹp màu đỏ sẫm. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b03 | 00:25.7–00:34.3 (8.6s) | L27 | nhưng hồng cầu của lạc đà lại có hình oval bầu dục thuôn dài! Cấu trúc khí động học đặc biệt này cho phép chúng trượt lướt qua các mao mạch siêu nhỏ một cách trơn tru ngay cả khi máu của lạc |  | Cận cảnh tế bào hồng cầu hình oval của chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng lướt nhẹ nhàng qua ngã ba mao mạch như những chiếc ca nô siêu tốc. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b04 | 00:34.3–00:41.8 (7.5s) | L28 | đà đã đặc quánh lại như si-rô vì mất nước kéo dài suốt nhiều ngày ròng rã! Thưa Giáo sư, khi tìm thấy nguồn nước, bệnh nhân có |  | Ống nghiệm chứa nước màu sánh đặc màu đỏ thẫm nhưng các hồng cầu oval vẫn tự do chuyển động không hề đông tụ. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b05 | 00:41.8–00:50.7 (8.9s) | L29 | thể uống một lượng nước khổng lồ trong tích tắc đúng không ạ? Chính xác là một kỳ tích tiếp nước ngoạn mục! Khi tìm thấy một vũng nước hay ốc đảo, Cỗ Máy Lọc Nước Sa Mạc có thể |  | Cô y tá Fennec mở to mắt kinh ngạc trước bể nước 200 lít khổng lồ đang cạn dần. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b06 | 00:50.7–00:58.6 (7.9s) | L30 | nốc cạn 130 lít nước, thậm chí 200 lít nước chỉ trong vòng chưa đầy 15 phút! Nếu là người bình thường uống ngần ấy nước, | **130 LÍT** · uống trong tích tắc · R/360 · [0.65, 0.45]<br>**15 PHÚT** · thời gian uống · L/420 · [0.35, 0.5] | chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng cúi đầu uống nước ừng ực tại ốc đảo xanh tươi, đồng hồ bấm giờ nhảy vọt đến con số 200 lít nước chỉ trong 15 phút. |
| b07 | 00:58.6–01:10.5 (12.0s) | L31 | hiện tượng ngộ độc nước sẽ xảy ra tức khắc: Áp suất thẩm thấu tụt giảm khiến các tế bào hồng cầu tròn vỡ tung hàng loạt và tử vong ngay tại chỗ! Nhưng màng tế bào hồng cầu hình oval của lạc đà có khả năng co giãn phi thường: Chúng |  | Mô hình tế bào hồng cầu người bị nạp nước quá nhanh căng phồng rồi vỡ bùm như bong bóng nước. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b08 | 01:10.5–01:15.1 (4.6s) | L32 | có thể phồng to gấp 240% thể tích ban đầu mà không hề bị vỡ! Chúng nở ra | **240%** · độ giãn nở hồng cầu · R/370 · [0.68, 0.45] | Hồng cầu hình oval của lạc đà giãn nở đàn hồi kỳ diệu từ kích thước nhỏ phồng to gấp 240% vẫn nguyên vẹn. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b09 | 01:15.1–01:22.0 (7.0s) | L33 | như những quả bóng bay co giãn vô hạn, nhẹ nhàng hấp thụ toàn bộ lượng nước khổng lồ đó vào hệ tuần hoàn một cách an toàn tuyệt đối! Nghĩa |  | Đồ họa so sánh: Hồng cầu oval như những quả bóng cao su siêu dẻo bảo vệ toàn diện hệ tuần hoàn. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b10 | 01:22.0–01:31.7 (9.7s) | L34 | là thể tích máu của nó có thể tăng vọt gấp đôi trong 15 phút mà thành mạch máu không hề bị vỡ hay rách toác sao thưa Bác sĩ? Hoàn toàn chính xác thưa trợ lý! Các mạch máu của lạc đà sở |  | Bác sĩ Chuột Nhảy Gerbil kiểm tra biểu đồ dung tích tuần hoàn dâng cao ngoạn mục. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b11 | 01:31.7–01:37.7 (6.0s) | L35 | hữu lớp cơ trơn đàn hồi siêu đẳng, kết hợp cùng áp lực thẩm thấu nội bào cân bằng hoàn mỹ, biến toàn bộ hệ tuần hoàn của nó thành |  | Mặt cắt động mạch chủ co giãn nhịp nhàng, hấp thụ trọn vẹn lưu lượng nước màu khổng lồ mà không hề tăng huyết áp. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b12 | 01:37.7–01:39.8 (2.1s) | L36 | một hồ chứa di động đàn hồi vô song! |  | chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng tràn đầy sinh lực sau khi uống no nước, đôi mắt sáng bừng sẵn sàng cho chuyến vượt sa mạc mới. |

### scene04 · QUẢ THẬN SIÊU LỌC CÔ ĐẶC NƯỚC TIỂU THÀNH SI-RÔ · 80.1s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:14.7 (14.7s) | L37 | Tiếp theo, xin mời hội đồng kiểm tra hệ thống cơ quan nội tạng đắt giá nhất của bệnh nhân: Đôi quả thận siêu lọc! Khi nước là thứ quý hơn vàng ròng giữa sa mạc, việc bài tiết lãng phí dù chỉ một giọt nước cũng đồng nghĩa với bản án tử hình. Thận của Cỗ Máy Lọc Nước Sa Mạc sở |  | Sơ đồ giải phẫu hệ tiết niệu màu nước: Hai quả thận của lạc đà phát sáng màu lam ngọc turquoise với cấu trúc siêu lọc phức tạp. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b02 | 00:14.7–00:21.7 (7.0s) | L38 | hữu quai Henle dài gấp nhiều lần so với các loài động vật thông thường, tạo ra một gradient nồng độ thẩm thấu cực kỳ khủng khiếp. Hệ thống ống thận |  | Kính hiển vi bóc tách ống thận: Quai Henle kéo dài sâu vào tủy thận tạo gradient nồng độ muối cực cao. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b03 | 00:21.7–00:27.0 (5.3s) | L39 | này vắt kiệt từng phân tử nước từ dịch lọc trước khi bài tiết ra ngoài. Kết quả là nước tiểu của lạc đà cô đặc |  | Mô phỏng 3D dòng dịch lọc: Từng giọt nước li ti bị hút ngược trở lại mao mạch nước màu, chỉ giữ lại cặn bã đậm đặc. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b04 | 00:27.0–00:39.9 (12.8s) | L40 | đến mức sánh đặc như si-rô đặc quẹt, có nồng độ muối và khoáng chất cao gấp đôi nước biển tự nhiên! Rất hiếm có một loài động vật có vú nào có thể bài xuất nước tiểu đậm đặc đến mức đó mà không bị suy thận cấp tính! Báo cáo Bác sĩ trưởng, |  | Ống nghiệm hứng giọt nước tiểu cô đặc sánh như mật ong với nồng độ muối gấp đôi nước biển. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b05 | 00:39.9–00:50.8 (10.9s) | L41 | chất thải rắn của bệnh nhân khô khốc đến mức có thể đốt cháy làm chất đốt ngay lập tức! Báo cáo hoàn toàn trùng khớp với thực nghiệm lâm sàng! Ruột già của lạc đà tái hấp thu nước triệt để đến mức phân của chúng thải |  | Cô y tá Fennec nhặt một viên phân lạc đà khô cong như viên sỏi tròn không hề dính tay. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b06 | 00:50.8–01:01.7 (10.9s) | L42 | ra khô cong như những viên sỏi gỗ, đến mức người du mục Bedouin có thể nhặt lên và nhóm lửa đun nấu ngay tại chỗ mà không cần phơi khô! Mọi giọt ẩm đi vào cơ thể đều bị giữ lại và tuần hoàn khép kín |  | Người du mục Bedouin dùng phân lạc đà khô nhóm bếp lửa bập bùng đun ấm trà sa mạc nghi ngút khói. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b07 | 01:01.7–01:05.1 (3.4s) | L43 | với hiệu suất tái sử dụng lên tới 99%, biến cơ thể lạc đà | **99%** · tái hấp thu nước · R/380 · [0.65, 0.45] | chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng đứng bên biểu đồ tuần hoàn nước khép kín đạt hiệu suất tái hấp thu 99% kỷ lục. chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc. |
| b08 | 01:05.1–01:09.5 (4.4s) | L44 | thành một nhà máy xử lý nước tuần hoàn hoàn hảo nhất Trái Đất! Thậm chí dạ dày của lạc đà |  | Mô hình đồ họa nhà máy lọc nước vi mô lồng ghép bên trong cơ thể khỏe mạnh của chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng. |
| b09 | 01:09.5–01:15.4 (5.9s) | L45 | còn có cấu trúc ba ngăn chuyên biệt với các tuyến tiết chất nhầy đặc thù, cho phép nó nhai ngấu nghiến những cành cây gai góc nhọn hoắt và |  | Dạ dày 3 ngăn của lạc đà với lớp niêm mạc dày cộp tiết chất nhầy bảo vệ chống gai góc đâm thủng. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b10 | 01:15.4–01:17.5 (2.1s) | L46 | cây xương rồng sa mạc chứa đầy độc tố |  | chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng thản nhiên nhai cành xương rồng đầy gai nhọn hoắt như đang thưởng thức món kẹo giòn tan. |
| b11 | 01:17.5–01:20.1 (2.6s) | L47 | mà niêm mạc không hề bị xước xát lấy một vết nhỏ! |  | Cận cảnh khoang miệng khỏe khoắn của chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng với những gai thịt sừng hóa bền chắc như da thuộc. |

### scene05 · ỐNG THỞ NGƯNG TỤ HƠI NƯỚC VÀ LỖ MŨI VAN MỘT CHIỀU · 83.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.7 (8.7s) | L48 | Nếu các bạn nghĩ rằng kiểm soát bài tiết là đã chặn đứng mọi lối thoát của nước, thì các bác sĩ đã bỏ quên con đường bốc hơi vô hình nhưng cực kỳ nguy hiểm: Đường hô hấp! |  | Hình ảnh giải phẫu đường hô hấp: Khoang mũi và khí quản của lạc đà được vẽ bằng nét màu nước mềm mại tinh xảo. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b02 | 00:08.7–00:22.4 (13.7s) | L49 | Mỗi hơi thở ra của con người mang theo một lượng hơi nước ấm áp bốc hơi vào không khí. Giữa sa mạc khô hạn, nếu thở ra lượng hơi ẩm đó, cơ thể sẽ bị rút cạn kiệt chỉ sau vài giờ thở dốc. Để giải bài toán này, khoang mũi của Cỗ Máy Lọc Nước Sa Mạc được cấu tạo |  | Hơi thở người que phả ra làn sương trắng mang theo hơi ẩm quý giá bốc hơi tan biến vào không khí sa mạc. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b03 | 00:22.4–00:29.2 (6.7s) | L50 | từ các vách xoắn ốc cuộn nhiều tầng phủ đầy niêm mạc hút ẩm đặc biệt. Khi lạc đà thở ra, không khí ấm và ẩm từ phổi đi qua khoang mũi lạnh sẽ |  | Mặt cắt khoang mũi lạc đà: Mê cung xương xoăn phủ lớp niêm mạc hút ẩm phức tạp nhiều tầng như tổ ong. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b04 | 00:29.2–00:33.2 (4.0s) | L51 | bị ngưng tụ hơi nước lại lập tức! Lượng nước ngưng tụ này thấm ngược trở lại niêm mạc |  | Hơi nước ấm trong luồng khí thở ra chạm vào vách mũi lạnh ngưng tụ thành các giọt nước li ti lăn ngược vào trong. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b05 | 00:33.2–00:40.4 (7.2s) | L52 | mũi để tái hấp thu vào máu, chỉ có luồng không khí khô ráo được thở ra ngoài! Bác sĩ ơi, còn khi bão cát ập đến thì sao ạ? |  | Mạng lưới mao mạch niêm mạc mũi hút trọn các giọt nước ngưng tụ, chỉ thải khí khô ra ngoài. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b06 | 00:40.4–00:47.8 (7.4s) | L53 | Bụi cát có tràn vào phổi làm ngạt thở bệnh nhân không? Một cơ chế bảo hộ đường thở hoàn mỹ thưa trợ lý! Lỗ mũi của lạc đà được trang |  | Bão cát sa mạc cuồn cuộn đỏ rực ập đến che khuất cả bầu trời, gió rít dữ dội. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b07 | 00:47.8–00:52.6 (4.8s) | L54 | bị các cơ vòng van một chiều có thể tự động khép chặt lại hoàn toàn khi có gió cát! Kết hợp cùng |  | Cận cảnh mũi chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng: Hai lỗ mũi tự động khép chặt lại như chiếc van khí nén ngăn mọi hạt cát lọt vào. |
| b08 | 00:52.6–01:03.0 (10.4s) | L55 | đôi hàng mi dày hai tầng đan xen và lớp màng chớp trong suốt bảo vệ mắt, lạc đà có thể thản nhiên bước đi giữa tâm bão cát mù mịt mà không hề hít phải một hạt bụi nào! Thậm chí thân nhiệt của lạc đà còn có khả |  | Đôi mắt to tròn của chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng chớp nhẹ với hai tầng lông mi dài rậm rạp và màng chớp trong suốt chắn bụi. chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc. |
| b09 | 01:03.0–01:10.6 (7.6s) | L56 | năng dao động linh hoạt từ 34°C vào ban đêm lên tới 41°C vào ban ngày! Bằng cách tự nâng nhiệt độ cơ thể lên ngang bằng nhiệt độ môi trường, | **34°C** · thân nhiệt ban đêm · L/380 · [0.35, 0.45]<br>**41°C** · thân nhiệt trưa hè · R/380 · [0.65, 0.45] | Đồ thị thân nhiệt sinh học: Đường cong nhiệt độ cơ thể dao động từ 34°C đêm lạnh lên 41°C trưa hè bỏng rát. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b10 | 01:10.6–01:15.2 (4.6s) | L57 | chúng hoàn toàn không cần đổ mồ hôi để làm mát, tiết kiệm thêm hàng chục lít nước mỗi ngày! |  | chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng bước đi khô ráo mát mẻ, tiết kiệm hàng chục lít nước mồ hôi quý giá mỗi ngày. |
| b11 | 01:15.2–01:21.4 (6.1s) | L58 | Một hệ thống điều hòa sinh học tự cân bằng quá đỗi diệu kỳ! Bệnh nhân không chống lại cái nóng thiêu đốt của sa mạc, mà chọn |  | Biểu tượng âm dương cân bằng giữa ánh nắng mặt trời và làn gió sa mạc ôn hòa bao quanh chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng. |
| b12 | 01:21.4–01:23.9 (2.5s) | L59 | cách hòa làm một với nhịp điệu nhiệt độ của thiên nhiên! |  | chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng ung dung rảo bước trên đỉnh cồn cát vàng óng ả, toát lên phong thái bậc thầy sinh tồn. |

### scene06 · TINH HOA Y HỌC PHỎNG SINH HỌC GIỮA BIỂN CÁT · 71.6s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:11.4 (11.4s) | L60 | Thưa toàn thể hội đồng y khoa, sau khi khám nghiệm toàn diện từ bướu mỡ chống sốc nhiệt, tế bào hồng cầu hình oval co giãn vô hạn, quả thận siêu lọc cho đến khoang mũi ngưng tụ hơi thở, chúng tôi xin long |  | Phòng hội đồng y khoa trang nghiêm: Toàn thể y bác sĩ đứng nghiêm chào đón buổi lễ ký kết giấy xuất viện danh dự. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b02 | 00:11.4–00:20.5 (9.1s) | L61 | trọng ký giấy xuất viện cho bệnh nhân Lạc Đà Sa Mạc với xếp loại thể lực phi thường xuất sắc tuyệt đối! Cỗ Máy Lọc Nước Sa Mạc không đơn thuần là một con thú thồ hàng nhẫn nại, mà |  | Dấu mộc y tế đỏ thắm đóng cộp chữ 'XUẤT VIỆN — THỂ LỰC PHI THƯỜNG' xuống hồ sơ bệnh án của chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng. |
| b03 | 00:20.5–00:26.3 (5.8s) | L62 | là đỉnh cao của công nghệ phỏng sinh học mà nền y học hiện đại của thế kỷ 21 vẫn đang ngày đêm nghiên cứu ứng dụng. |  | Mô hình nghiên cứu y học hiện đại kết hợp hình ảnh vi mô tế bào hồng cầu lạc đà trên màn hình số 3D. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b04 | 00:26.3–00:35.0 (8.6s) | L63 | Các nhà khoa học NASA đang dựa trên cấu trúc hồng cầu co giãn của lạc đà để nghiên cứu các loại dịch truyền nhân tạo cho các phi hành gia bay vào không gian sâu. Quả |  | Tàu con thoi vũ trụ bay vào không gian sâu: Túi dịch truyền nhân tạo phỏng sinh học mô phỏng hồng cầu oval lạc đà. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b05 | 00:35.0–00:44.8 (9.9s) | L64 | là một bậc thầy sinh tồn vĩ đại của tự nhiên thưa Bác sĩ trưởng! Thiên nhiên luôn là người thầy thuốc thông thái và vĩ đại nhất! Hoàn toàn chuẩn xác! Lần tới khi bạn nhìn thấy hình ảnh chú lạc |  | Bác sĩ Kền Kền già nâng ly trà thảo mộc sa mạc chúc mừng kỳ tích sinh học của chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng. |
| b06 | 00:44.8–00:49.4 (4.5s) | L65 | đà thong dong sải bước trên những đồi cát sa mạc hoang vu, hãy nhớ rằng bạn đang chiêm |  | Toàn cảnh đoàn lữ hành lạc đà bước đi thong thả lúc hoàng hôn sa mạc buông xuống đỏ rực tuyệt đẹp. chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc. |
| b07 | 00:49.4–00:56.9 (7.5s) | L66 | ngưỡng một cỗ máy sinh học tinh vi bậc nhất mà tạo hóa từng tạo tác! Còn bây giờ, giữa chiếc bướu mỡ năng lượng và tế bào hồng cầu oval co giãn, |  | Hình bóng chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng in bóng trên cồn cát mênh mông, tỏa sáng hào quang của thiên tài tạo hóa. |
| b08 | 00:56.9–00:59.4 (2.6s) | L67 | giải pháp y sinh nào làm bạn kinh ngạc nhất? Hãy |  | Mô hình đồ họa tổng hợp 4 vũ khí: Bướu mỡ, Hồng cầu oval, Thận siêu lọc và Mũi ngưng tụ hơi thở. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b09 | 00:59.4–01:01.6 (2.2s) | L68 | để lại bình luận bên dưới nhé! Và đừng |  | chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng mỉm cười cầm chiếc bảng kẹp hồ sơ chỉ vào ô bình luận mời gọi khán giả tương tác. |
| b10 | 01:01.6–01:08.6 (7.0s) | L69 | quên bấm đăng ký kênh để đón xem Tập 38 khám phá cỗ máy leo núi trọng lực 90° của Dê Núi Bắc Mỹ! Hẹn gặp lại toàn thể các |  | Banner giới thiệu bí ẩn của Tập 38: Bóng dáng chú Dê Núi Bắc Mỹ đứng thăng bằng trên vách đá 90 độ thẳng đứng. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này. |
| b11 | 01:08.6–01:11.6 (2.9s) | L70 | bạn trong chuyến hành trình khám phá những kỳ quan sinh học tiếp theo! |  | chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng cùng toàn thể đội ngũ y bác sĩ sa mạc vẫy tay chào tạm biệt khán giả trong ánh hoàng hôn ấm áp. |

## 5. Phân cảnh Shorts — từng beat

Banner: **CỖ MÁY LỌC NƯỚC / SA MẠC 50°C** · giọng 39.9s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Bạn có biết loài động vật nào có thể uống cạn 200 lít nước chỉ trong 15 phút mà không | **200 LÍT** · dung tích uống · R/620 · [0.65, 0.45] |
| s02 | 00:04.9 | S02 | bị vỡ hồng cầu chết ngay lập tức không? |  |
| s03 | 00:07.4 | S03 | Đó chính là Lạc Đà Sa Mạc — Cỗ Máy Lọc Nước siêu cấp của thiên nhiên! |  |
| s04 | 00:11.8 | S04 | Trái ngược với hiểu lầm của hàng triệu người, chiếc bướu trên lưng nó không hề chứa một giọt nước nào mà |  |
| s05 | 00:17.0 | S05 | là một khối bướu mỡ nặng tới 40 kg giúp chống sốc nhiệt 50°C! Bí mật sinh tử thực sự nằm | **40 KG** · bướu mỡ năng lượng · R/600 · [0.65, 0.45]<br>**50°C** · nhiệt độ môi trường · L/620 · [0.35, 0.45] |
| s06 | 00:23.4 | S06 | ở tế bào hồng cầu hình oval độc nhất vô nhị: Chúng |  |
| s07 | 00:26.6 | S07 | có thể phồng to gấp 240% thể tích để nạp nước tức thì, kết hợp | **240%** · giãn nở hồng cầu · R/620 · [0.68, 0.45] |
| s08 | 00:30.8 | S08 | cùng quả thận siêu |  |
| s09 | 00:31.6 | S09 | lọc cô đặc nước tiểu thành si-rô đặc quẹt! Nhờ đó, sinh vật phi thường này có |  |
| s10 | 00:35.9 | S10 | thể nhịn uống suốt 30 | **30 NGÀY** · nhịn uống tối đa · L/620 · [0.35, 0.45] |
| s11 | 00:37.2 | S11 | ngày giữa chảo lửa sa mạc |  |
| s12 | 00:38.5 | S12 | mà vẫn sống khỏe re! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chào mừng các y bác sĩ, các điều dưỡng viên và toàn thể thực tập sinh bước vào Ca trực cấp cứu đặc biệt của Bệnh viện Dã chiến Sa Mạc Sahara! Hôm nay, chúng ta vừa". Bố cục: Phòng cấp cứu dã chiến Sahara mở ra: Bác sĩ trưởng chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng đứng bên bàn hội chẩn, tay chỉ vào biểu đồ điện tâm đồ sa mạc màu nước lung linh.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tiếp nhận một bệnh nhân vô cùng kỳ lạ và bất quy tắc. Một đối tượng lang thang giữa". Bố cục: Bệnh nhân lạc đà thong dong bước vào lều y tế dã chiến, xung quanh là cồn cát sa mạc vàng rực phản chiếu ánh mặt trời. chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chảo lửa 50°C, cát bỏng rát chân, không hề có giọt nước uống nào suốt". Bố cục: Nhiệt kế sa mạc thủy ngân dâng cao chạm mốc 50 độ C đỏ rực: Cát bốc hơi nóng hầm hập. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "2 tuần ròng rã, nhưng khi bước vào phòng khám, mạch đập vẫn đều đặn,". Bố cục: Bản đồ vệ tinh sa mạc Sahara kéo dài hai tuần không có bóng một giọt nước: chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng vẫn nhai cỏ khô thảnh thơi.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "huyết áp ổn định tuyệt đối và ánh mắt thì thảnh thơi nhai cỏ khô như thể đang đi nghỉ dưỡng tại bờ biển nhiệt đới! Đối tượng trên bàn hội chẩn của chúng ta hôm nay". Bố cục: Máy đo huyết áp y tế kim chỉ vạch xanh an toàn tuyệt đối: chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng mỉm cười nháy mắt với các bác sĩ.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "mang tên khoa học Camelus dromedarius, nhưng trong toàn bộ giới y khoa tự nhiên, chúng tôi gọi nó bằng một mật danh đầy kính nể:". Bố cục: Hồ sơ bệnh án bìa da cổ phong cách Ả Rập mở ra, ghi rõ danh pháp khoa học Camelus dromedarius với hoa văn màu nước lam ngọc. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cỗ Máy Lọc Nước Sa Mạc! Nếu một con người bình thường rơi vào hoàn cảnh này, cơ thể chúng ta sẽ nhanh chóng". Bố cục: chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng tạo dáng kiêu hãnh với chiếc ống nghe bác sĩ lấp lánh dưới ánh nắng sa mạc rực rỡ.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "rơi vào trạng thái sốc nhiệt cấp độ bốn, nước màu đông đặc lại như thạch, suy đa tạng và tử vong chỉ sau chưa đầy". Bố cục: Một anh chàng người que ngất lịm trên cát nóng vì kiệt nước, trên đầu hiện biểu tượng giọt nước cạn kiệt màu đỏ báo động. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "48 giờ đồng hồ! Báo cáo Bác sĩ trưởng khoa, chỉ số sinh tồn của bệnh nhân ghi nhận mất nước vượt ngưỡng 25% trọng lượng cơ thể mà không hề có dấu hiệu trụy tim mạch! Báo cáo rất chính xác thưa y tá trưởng! Đối với cơ thể người, chỉ cần mất". Bố cục: Đồng hồ cát thời gian 48 giờ chảy xiết: Mô hình tim người que ngừng đập vì trụy tuần hoàn. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "15% lượng nước trong cơ thể là tim đã ngừng đập vì thể tích nước màu sụt giảm nghiêm trọng. Thế nhưng Cỗ Máy Lọc Nước Sa Mạc có thể". Bố cục: Cô y tá Cáo Fennec tai to cầm bảng kẹp hồ sơ báo cáo chỉ số mất nước vượt ngưỡng 25% an toàn. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "mất tới 30%, thậm chí 40% lượng nước trong cơ thể mà vẫn bước đi hiên ngang vượt qua những cồn cát bỏng cháy hàng ngàn cây số! Vậy đâu là những vũ khí y sinh học tối mật giúp sinh vật này thách thức mọi định luật sinh lý học truyền thống? Mời toàn thể hội đồng bác sĩ". Bố cục: Cột mốc so sánh tử vong: Người ngừng thở ở mức mất nước 15%, còn lạc đà vẫn chịu tải tới 40% trọng lượng. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "mở tập hồ sơ bệnh án số một để cùng tôi bóc tách phép màu giải phẫu đầu tiên!". Bố cục: chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng lật giở trang hồ sơ bệnh án số 1 có con dấu sáp đỏ uy tín, chuẩn bị bóc tách bí ẩn chiếc bướu.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy bắt đầu với chẩn đoán sai lầm phổ biến nhất trong lịch sử nhân loại: Chiếc bướu khổng lồ trên lưng lạc đà! Hàng triệu người từ xưa đến nay vẫn ngây thơ tin rằng bên trong chiếc bướu đó là một". Bố cục: Bức tranh giải phẫu bướu lạc đà màu nước phong cách cổ điển: Chiếc bướu cao sừng sững phát sáng màu vàng kim ấm áp. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bồn chứa nước di động khổng lồ, nơi lạc đà tích trữ hàng chục lít nước tinh khiết để uống dần khi khát. Nếu bác sĩ nào chẩn đoán như vậy trong phòng thi chuyên khoa, tôi xin phép thu hồi chứng chỉ hành nghề ngay lập tức! Dưới lát cắt". Bố cục: Hình vẽ hài hước một chiếc bồn inox chứa nước gắn trên lưng lạc đà bị đánh dấu gạch chéo màu đỏ to tướng: Lầm tưởng kinh điển. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chụp cộng hưởng từ và sinh thiết giải phẫu, chiếc bướu này không chứa bất kỳ giọt nước lỏng nào cả! Toàn bộ chiếc bướu". Bố cục: Màn hình máy MRI y tế chiếu rõ cấu trúc bên trong chiếc bướu: Toàn bộ là mô mỡ lipid vàng óng, không hề có giọt nước nào. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nặng tới 40 kg, thậm chí 80 kg ở những con đực trưởng thành, là một khối mỡ đậm đặc tinh khiết! Đây là một kho dự trữ năng lượng sinh hóa siêu cô đặc giúp Cỗ Máy Lọc Nước Sa Mạc". Bố cục: Cân y tế đo trọng lượng bướu mỡ nhảy số từ 40 kg đến 80 kg: chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng đứng vỗ vỗ chiếc bướu kiêu hãnh.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "sinh tồn suốt cả tháng trời không cần ăn uống. Ủa Bác sĩ ơi, vậy". Bố cục: chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng thong thả bước đi trên con đường tơ lụa giữa sa mạc mênh mông suốt 30 ngày đêm không cần dừng ăn. chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tại sao mỡ lại tập trung hết lên lưng mà không phân bố đều khắp cơ thể như động vật khác thưa bác sĩ? Một câu hỏi chẩn đoán cực kỳ thông minh thưa bác sĩ nội trú! Nếu lớp mỡ dày cộp đó". Bố cục: Bác sĩ nội trú Chuột Nhảy Gerbil đeo kính tròn thắc mắc chỉ tay vào lưng chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "phân bố đều dưới da như loài gấu bắc cực hay hải cẩu, cơ thể lạc đà sẽ bị bọc kín trong một chiếc áo phao cách nhiệt dày cộp. Dưới cái nắng 50°C của sa mạc, nhiệt lượng bên trong cơ thể sẽ hoàn toàn không thể thoát ra ngoài và lạc đà sẽ bị". Bố cục: Hình ảnh chú gấu bắc cực béo múp míp mặc áo phao dày cộp toát mồ hôi đầm đìa dưới nắng sa mạc. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nấu chín từ bên trong chỉ sau vài giờ vận động! Bằng cách". Bố cục: Mô phỏng nhiệt học: Cơ thể bị om nhiệt màu đỏ rực như nồi áp suất nếu mỡ bao quanh toàn thân. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "gom toàn bộ lượng mỡ cách nhiệt tập trung duy nhất lên đỉnh lưng, chiếc bướu đóng vai trò như một chiếc dù che nắng tự nhiên, hấp thụ trực tiếp ánh nắng mặt trời rọi thẳng từ trên cao xuống đỉnh đầu, trong khi toàn bộ phần cơ thể còn lại hoàn toàn không có mỡ dưới da, cho phép". Bố cục: Sơ đồ luồng nhiệt: Bướu mỡ trên lưng hoạt động như chiếc ô dù phản xạ toàn bộ tia nắng mặt trời gay gắt. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nhiệt lượng tỏa thẳng ra môi trường xung quanh một cách tối đa! Chưa dừng lại ở đó đâu các đồng nghiệp trẻ! Khi quá trình". Bố cục: Vùng bụng và bốn chân của chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng tỏa ra các luồng khí mát màu xanh lam, giúp cơ thể tản nhiệt siêu tốc.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "oxy hóa chất béo diễn ra, mỗi gam mỡ trong bướu sẽ giải phóng hơn một gam nước chuyển hóa nội sinh, giúp lạc đà". Bố cục: Phương trình phản ứng sinh hóa phát sáng: 1 gam mỡ lipid phân giải tạo ra 1,1 gam nước chuyển hóa nội sinh. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tự cấp ẩm cho từng tế bào ngay từ bên trong mà chẳng cần một giọt nước mưa nào từ bầu trời!". Bố cục: chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng mỉm cười sảng khoái như vừa được uống một ly nước mát ngọt lành ngay giữa biển cát.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bây giờ, xin mời các chuyên gia huyết học bước vào phòng xét nghiệm tế bào học, nơi cất giữ bí mật y sinh tinh xảo nhất của Cỗ Máy Lọc Nước Sa Mạc: Những tế bào hồng cầu hình oval kỳ dị! Ở toàn bộ các loài động vật có vú khác, bao gồm cả con người, tế bào hồng cầu luôn có". Bố cục: Kính hiển vi y khoa phóng đại giọt nước màu màu nước đỏ thắm: Các tế bào hồng cầu hình oval bơi lội mềm mại. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hình đĩa lõm hai mặt tròn trịa. Khi chúng ta mất nước nặng, nước màu trở nên đặc quánh và các tế bào hồng cầu hình tròn sẽ bị mắc kẹt tại các mao mạch nhỏ hẹp, gây tắc nghẽn tuần hoàn và dẫn đến tử vong ngay tức khắc. Thế nhưng". Bố cục: Hồng cầu hình tròn của con người bị vón cục tắc nghẽn trong lòng mao mạch nước màu hẹp màu đỏ sẫm. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hồng cầu của lạc đà lại có hình oval bầu dục thuôn dài! Cấu trúc khí động học đặc biệt này cho phép chúng trượt lướt qua các mao mạch siêu nhỏ một cách trơn tru ngay cả khi nước màu của lạc đà đã". Bố cục: Cận cảnh tế bào hồng cầu hình oval của chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng lướt nhẹ nhàng qua ngã ba mao mạch như những chiếc ca nô siêu tốc. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đặc quánh lại như si-rô vì mất nước kéo dài suốt nhiều ngày ròng rã! Thưa Giáo sư, khi tìm thấy nguồn nước, bệnh nhân có thể". Bố cục: Ống nghiệm chứa nước màu sánh đặc màu đỏ thẫm nhưng các hồng cầu oval vẫn tự do chuyển động không hề đông tụ. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "uống một lượng nước khổng lồ trong tích tắc đúng không ạ? Chính xác là một kỳ tích tiếp nước ngoạn mục! Khi tìm thấy một vũng nước hay ốc đảo, Cỗ Máy Lọc Nước Sa Mạc có thể nốc cạn". Bố cục: Cô y tá Fennec mở to mắt kinh ngạc trước bể nước 200 lít khổng lồ đang cạn dần. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "130 lít nước, thậm chí 200 lít nước chỉ trong vòng chưa đầy 15 phút! Nếu là người bình thường uống ngần ấy nước, hiện tượng". Bố cục: chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng cúi đầu uống nước ừng ực tại ốc đảo xanh tươi, đồng hồ bấm giờ nhảy vọt đến con số 200 lít nước chỉ trong 15 phút.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "ngộ độc nước sẽ xảy ra tức khắc: Áp suất thẩm thấu tụt giảm khiến các tế bào hồng cầu tròn vỡ tung hàng loạt và tử vong ngay tại chỗ! Nhưng màng tế bào hồng cầu hình oval của lạc đà có khả năng co giãn phi thường: Chúng có thể". Bố cục: Mô hình tế bào hồng cầu người bị nạp nước quá nhanh căng phồng rồi vỡ bùm như bong bóng nước. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "phồng to gấp 240% thể tích ban đầu mà không hề bị vỡ! Chúng nở ra như". Bố cục: Hồng cầu hình oval của lạc đà giãn nở đàn hồi kỳ diệu từ kích thước nhỏ phồng to gấp 240% vẫn nguyên vẹn. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "những quả bóng bay co giãn vô hạn, nhẹ nhàng hấp thụ toàn bộ lượng nước khổng lồ đó vào hệ tuần hoàn một cách an toàn tuyệt đối! Nghĩa là". Bố cục: Đồ họa so sánh: Hồng cầu oval như những quả bóng cao su siêu dẻo bảo vệ toàn diện hệ tuần hoàn. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thể tích nước màu của nó có thể tăng vọt gấp đôi trong 15 phút mà thành mạch nước màu không hề bị vỡ hay rách toác sao thưa Bác sĩ? Hoàn toàn chính xác thưa trợ lý! Các mạch nước màu của lạc đà sở hữu". Bố cục: Bác sĩ Chuột Nhảy Gerbil kiểm tra biểu đồ dung tích tuần hoàn dâng cao ngoạn mục. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "lớp cơ trơn đàn hồi siêu đẳng, kết hợp cùng áp lực thẩm thấu nội bào cân bằng hoàn mỹ, biến toàn bộ hệ tuần hoàn của nó thành một". Bố cục: Mặt cắt động mạch chủ co giãn nhịp nhàng, hấp thụ trọn vẹn lưu lượng nước màu khổng lồ mà không hề tăng huyết áp. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hồ chứa di động đàn hồi vô song!". Bố cục: chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng tràn đầy sinh lực sau khi uống no nước, đôi mắt sáng bừng sẵn sàng cho chuyến vượt sa mạc mới.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tiếp theo, xin mời hội đồng kiểm tra hệ thống cơ quan bên trong cơ thể đắt giá nhất của bệnh nhân: Đôi quả thận siêu lọc! Khi nước là thứ quý hơn vàng ròng giữa sa mạc, việc bài tiết lãng phí dù chỉ một giọt nước cũng đồng nghĩa với bản án tử hình. Thận của Cỗ Máy Lọc Nước Sa Mạc sở hữu". Bố cục: Sơ đồ giải phẫu hệ tiết niệu màu nước: Hai quả thận của lạc đà phát sáng màu lam ngọc turquoise với cấu trúc siêu lọc phức tạp. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "quai Henle dài gấp nhiều lần so với các loài động vật thông thường, tạo ra một gradient nồng độ thẩm thấu cực kỳ khủng khiếp. Hệ thống ống thận này". Bố cục: Kính hiển vi bóc tách ống thận: Quai Henle kéo dài sâu vào tủy thận tạo gradient nồng độ muối cực cao. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "vắt kiệt từng phân tử nước từ dịch lọc trước khi bài tiết ra ngoài. Kết quả là nước tiểu của lạc đà cô đặc đến mức". Bố cục: Mô phỏng 3D dòng dịch lọc: Từng giọt nước li ti bị hút ngược trở lại mao mạch nước màu, chỉ giữ lại cặn bã đậm đặc. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "sánh đặc như si-rô đặc quẹt, có nồng độ muối và khoáng chất cao gấp đôi nước biển tự nhiên! Rất hiếm có một loài động vật có vú nào có thể bài xuất nước tiểu đậm đặc đến mức đó mà không bị suy thận cấp tính! Báo cáo Bác sĩ trưởng,". Bố cục: Ống nghiệm hứng giọt nước tiểu cô đặc sánh như mật ong với nồng độ muối gấp đôi nước biển. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chất thải rắn của bệnh nhân khô khốc đến mức có thể đốt cháy làm chất đốt ngay lập tức! Báo cáo hoàn toàn trùng khớp với thực nghiệm lâm sàng! Ruột già của lạc đà tái hấp thu nước triệt để đến mức phân của chúng thải ra". Bố cục: Cô y tá Fennec nhặt một viên phân lạc đà khô cong như viên sỏi tròn không hề dính tay. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "khô cong như những viên sỏi gỗ, đến mức người du mục Bedouin có thể nhặt lên và nhóm lửa đun nấu ngay tại chỗ mà không cần phơi khô! Mọi giọt ẩm đi vào cơ thể đều bị giữ lại và tuần hoàn khép kín với". Bố cục: Người du mục Bedouin dùng phân lạc đà khô nhóm bếp lửa bập bùng đun ấm trà sa mạc nghi ngút khói. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hiệu suất tái sử dụng lên tới 99%, biến cơ thể lạc đà thành một". Bố cục: chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng đứng bên biểu đồ tuần hoàn nước khép kín đạt hiệu suất tái hấp thu 99% kỷ lục. chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nhà máy xử lý nước tuần hoàn hoàn hảo nhất Trái Đất! Thậm chí dạ dày của lạc đà còn có". Bố cục: Mô hình đồ họa nhà máy lọc nước vi mô lồng ghép bên trong cơ thể khỏe mạnh của chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cấu trúc ba ngăn chuyên biệt với các tuyến tiết chất nhầy đặc thù, cho phép nó nhai ngấu nghiến những cành cây gai góc nhọn hoắt và". Bố cục: Dạ dày 3 ngăn của lạc đà với lớp niêm mạc dày cộp tiết chất nhầy bảo vệ chống gai góc đâm thủng. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cây xương rồng sa mạc chứa đầy độc tố mà". Bố cục: chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng thản nhiên nhai cành xương rồng đầy gai nhọn hoắt như đang thưởng thức món kẹo giòn tan.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "niêm mạc không hề bị xước xát lấy một vết nhỏ!". Bố cục: Cận cảnh khoang miệng khỏe khoắn của chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng với những gai thịt sừng hóa bền chắc như da thuộc.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu các bạn nghĩ rằng kiểm soát bài tiết là đã chặn đứng mọi lối thoát của nước, thì các bác sĩ đã bỏ quên con đường bốc hơi vô hình nhưng cực kỳ nguy hiểm: Đường hô hấp!". Bố cục: Hình ảnh giải phẫu đường hô hấp: Khoang mũi và khí quản của lạc đà được vẽ bằng nét màu nước mềm mại tinh xảo. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi hơi thở ra của con người mang theo một lượng hơi nước ấm áp bốc hơi vào không khí. Giữa sa mạc khô hạn, nếu thở ra lượng hơi ẩm đó, cơ thể sẽ bị rút cạn kiệt chỉ sau vài giờ thở dốc. Để giải bài toán này, khoang mũi của Cỗ Máy Lọc Nước Sa Mạc được cấu tạo từ các". Bố cục: Hơi thở người que phả ra làn sương trắng mang theo hơi ẩm quý giá bốc hơi tan biến vào không khí sa mạc. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "vách xoắn ốc cuộn nhiều tầng phủ đầy niêm mạc hút ẩm đặc biệt. Khi lạc đà thở ra, không khí ấm và ẩm từ phổi đi qua khoang mũi lạnh sẽ bị". Bố cục: Mặt cắt khoang mũi lạc đà: Mê cung xương xoăn phủ lớp niêm mạc hút ẩm phức tạp nhiều tầng như tổ ong. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "ngưng tụ hơi nước lại lập tức! Lượng nước ngưng tụ này thấm ngược trở lại niêm mạc mũi để". Bố cục: Hơi nước ấm trong luồng khí thở ra chạm vào vách mũi lạnh ngưng tụ thành các giọt nước li ti lăn ngược vào trong. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tái hấp thu vào nước màu, chỉ có luồng không khí khô ráo được thở ra ngoài! Bác sĩ ơi, còn khi bão cát ập đến thì sao ạ?". Bố cục: Mạng lưới mao mạch niêm mạc mũi hút trọn các giọt nước ngưng tụ, chỉ thải khí khô ra ngoài. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bụi cát có tràn vào phổi làm ngạt thở bệnh nhân không? Một cơ chế bảo hộ đường thở hoàn mỹ thưa trợ lý! Lỗ mũi của lạc đà được trang bị các". Bố cục: Bão cát sa mạc cuồn cuộn đỏ rực ập đến che khuất cả bầu trời, gió rít dữ dội. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cơ vòng van một chiều có thể tự động khép chặt lại hoàn toàn khi có gió cát! Kết hợp cùng đôi". Bố cục: Cận cảnh mũi chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng: Hai lỗ mũi tự động khép chặt lại như chiếc van khí nén ngăn mọi hạt cát lọt vào.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hàng mi dày hai tầng đan xen và lớp màng chớp trong suốt bảo vệ mắt, lạc đà có thể thản nhiên bước đi giữa tâm bão cát mù mịt mà không hề hít phải một hạt bụi nào! Thậm chí thân nhiệt của lạc đà còn có khả năng". Bố cục: Đôi mắt to tròn của chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng chớp nhẹ với hai tầng lông mi dài rậm rạp và màng chớp trong suốt chắn bụi. chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "dao động linh hoạt từ 34°C vào ban đêm lên tới 41°C vào ban ngày! Bằng cách tự nâng nhiệt độ cơ thể lên ngang bằng nhiệt độ môi trường, chúng". Bố cục: Đồ thị thân nhiệt sinh học: Đường cong nhiệt độ cơ thể dao động từ 34°C đêm lạnh lên 41°C trưa hè bỏng rát. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hoàn toàn không cần đổ mồ hôi để làm mát, tiết kiệm thêm hàng chục lít nước mỗi ngày! Một". Bố cục: chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng bước đi khô ráo mát mẻ, tiết kiệm hàng chục lít nước mồ hôi quý giá mỗi ngày.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hệ thống điều hòa sinh học tự cân bằng quá đỗi diệu kỳ! Bệnh nhân không chống lại cái nóng thiêu đốt của sa mạc, mà chọn cách". Bố cục: Biểu tượng âm dương cân bằng giữa ánh nắng mặt trời và làn gió sa mạc ôn hòa bao quanh chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hòa làm một với nhịp điệu nhiệt độ của thiên nhiên!". Bố cục: chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng ung dung rảo bước trên đỉnh cồn cát vàng óng ả, toát lên phong thái bậc thầy sinh tồn.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thưa toàn thể hội đồng y khoa, sau khi khám nghiệm toàn diện từ bướu mỡ chống sốc nhiệt, tế bào hồng cầu hình oval co giãn vô hạn, quả thận siêu lọc cho đến khoang mũi ngưng tụ hơi thở, chúng tôi xin long trọng". Bố cục: Phòng hội đồng y khoa trang nghiêm: Toàn thể y bác sĩ đứng nghiêm chào đón buổi lễ ký kết giấy xuất viện danh dự. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "ký giấy xuất viện cho bệnh nhân Lạc Đà Sa Mạc với xếp loại thể lực phi thường xuất sắc tuyệt đối! Cỗ Máy Lọc Nước Sa Mạc không đơn thuần là một con thú thồ hàng nhẫn nại, mà là". Bố cục: Dấu mộc y tế đỏ thắm đóng cộp chữ 'XUẤT VIỆN — THỂ LỰC PHI THƯỜNG' xuống hồ sơ bệnh án của chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng.
```
</details>

<details><summary>L62</summary>

```text
HÌNH L62 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đỉnh cao của công nghệ phỏng sinh học mà nền y học hiện đại của thế kỷ 21 vẫn đang ngày đêm nghiên cứu ứng dụng. Các". Bố cục: Mô hình nghiên cứu y học hiện đại kết hợp hình ảnh vi mô tế bào hồng cầu lạc đà trên màn hình số 3D. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L63</summary>

```text
HÌNH L63 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nhà khoa học NASA đang dựa trên cấu trúc hồng cầu co giãn của lạc đà để nghiên cứu các loại dịch truyền nhân tạo cho các phi hành gia bay vào không gian sâu. Quả là một". Bố cục: Tàu con thoi vũ trụ bay vào không gian sâu: Túi dịch truyền nhân tạo phỏng sinh học mô phỏng hồng cầu oval lạc đà. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L64</summary>

```text
HÌNH L64 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bậc thầy sinh tồn vĩ đại của tự nhiên thưa Bác sĩ trưởng! Thiên nhiên luôn là người thầy thuốc thông thái và vĩ đại nhất! Hoàn toàn chuẩn xác! Lần tới khi bạn nhìn thấy hình ảnh chú lạc đà". Bố cục: Bác sĩ Kền Kền già nâng ly trà thảo mộc sa mạc chúc mừng kỳ tích sinh học của chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng.
```
</details>

<details><summary>L65</summary>

```text
HÌNH L65 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thong dong sải bước trên những đồi cát sa mạc hoang vu, hãy nhớ rằng bạn đang chiêm ngưỡng một". Bố cục: Toàn cảnh đoàn lữ hành lạc đà bước đi thong thả lúc hoàng hôn sa mạc buông xuống đỏ rực tuyệt đẹp. chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc.
```
</details>

<details><summary>L66</summary>

```text
HÌNH L66 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cỗ máy sinh học tinh vi bậc nhất mà tạo hóa từng tạo tác! Còn bây giờ, giữa chiếc bướu mỡ năng lượng và tế bào hồng cầu oval co giãn,". Bố cục: Hình bóng chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng in bóng trên cồn cát mênh mông, tỏa sáng hào quang của thiên tài tạo hóa.
```
</details>

<details><summary>L67</summary>

```text
HÌNH L67 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "giải pháp y sinh nào làm bạn kinh ngạc nhất? Hãy để lại". Bố cục: Mô hình đồ họa tổng hợp 4 vũ khí: Bướu mỡ, Hồng cầu oval, Thận siêu lọc và Mũi ngưng tụ hơi thở. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L68</summary>

```text
HÌNH L68 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bình luận bên dưới nhé! Và đừng quên". Bố cục: chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng mỉm cười cầm chiếc bảng kẹp hồ sơ chỉ vào ô bình luận mời gọi khán giả tương tác.
```
</details>

<details><summary>L69</summary>

```text
HÌNH L69 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bấm đăng ký kênh để đón xem Tập 38 khám phá cỗ máy leo núi trọng lực 90° của Dê Núi Bắc Mỹ! Hẹn gặp lại toàn thể các bạn trong". Bố cục: Banner giới thiệu bí ẩn của Tập 38: Bóng dáng chú Dê Núi Bắc Mỹ đứng thăng bằng trên vách đá 90 độ thẳng đứng. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>L70</summary>

```text
HÌNH L70 (16:9 ngang, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chuyến hành trình khám phá những kỳ quan sinh học tiếp theo!". Bố cục: chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng cùng toàn thể đội ngũ y bác sĩ sa mạc vẫy tay chào tạm biệt khán giả trong ánh hoàng hôn ấm áp.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bạn có biết loài động vật nào có thể uống cạn 200 lít nước chỉ trong 15 phút mà không bị". Bố cục: Cận cảnh hồ nước sa mạc với đồng hồ đếm ngược: Lạc đà há miệng uống nước như vòi rồng cuốn sạch 200 lít nước.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "vỡ hồng cầu chết ngay lập tức không?". Bố cục: Tế bào hồng cầu người bị nổ tung từng mảnh với tia sét cảnh báo tử vong ngay tức khắc. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đó chính là Lạc Đà Sa Mạc — Cỗ Máy Lọc Nước siêu cấp của thiên nhiên!". Bố cục: chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng xuất hiện oai vệ, quàng khăn rằn Ả Rập đỏ-trắng và đeo ống nghe bác sĩ lấp lánh.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Trái ngược với hiểu lầm của hàng triệu người, chiếc bướu trên lưng nó không hề chứa một giọt nước nào mà là một". Bố cục: Chiếc bướu trên lưng được bóc tách tia X: Một khối mỡ năng lượng 40 kg màu vàng óng chống sốc nhiệt. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "khối bướu mỡ nặng tới 40 kg giúp chống sốc nhiệt 50°C! Bí mật sinh tử thực sự nằm ở". Bố cục: Nhiệt kế sa mạc chạm ngưỡng 50 độ C bỏng rát: Cát sa mạc bốc hơi nóng nhưng chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng vẫn nhai cỏ thảnh thơi.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "tế bào hồng cầu hình oval độc nhất vô nhị: Chúng có thể". Bố cục: Kính hiển vi bóc tách các tế bào hồng cầu hình oval thuôn dài lướt nhẹ nhàng qua mao mạch nước màu. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "phồng to gấp 240% thể tích để nạp nước tức thì, kết hợp cùng". Bố cục: Hồng cầu oval phồng to gấp 240% như quả bóng cao su hấp thụ nước an toàn tuyệt đối. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "quả thận siêu lọc". Bố cục: Mô phỏng quả thận siêu lọc với quai Henle dài vắt kiệt từng giọt ẩm quý giá. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "cô đặc nước tiểu thành si-rô đặc quẹt! Nhờ đó, sinh vật phi thường này có thể". Bố cục: Ống nghiệm nước tiểu sánh đặc như si-rô chứng minh khả năng giữ nước tuyệt đỉnh. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "nhịn uống suốt 30 ngày". Bố cục: chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng bước đi hiên ngang giữa chảo lửa sa mạc suốt 30 ngày đêm không cần uống một giọt nước.
```
</details>

<details><summary>S11</summary>

```text
HÌNH S11 (DỌC 9:16, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "giữa chảo lửa sa mạc mà". Bố cục: Toàn cảnh cồn cát Sahara trải dài vô tận dưới ánh hoàng hôn sa mạc rực rỡ tuyệt mỹ. KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này.
```
</details>

<details><summary>S12</summary>

```text
HÌNH S12 (DỌC 9:16, phong cách tranh màu nước thám hiểm sa mạc Ả Rập & giải phẫu thực vật Ba Tư (Mirage Oasis Watercolor) và nhân vật chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "vẫn sống khỏe re!". Bố cục: chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng mỉm cười giơ ngón tay cái số một khẳng định danh hiệu Cỗ Máy Lọc Nước vô địch thiên nhiên.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/70 của video YouTube về Lạc Đà Sa Mạc). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh màu nước thám hiểm sa mạc Ả Rập kết hợp ký họa thực vật học & giải phẫu Ba Tư (Mirage Oasis Botanical & Anatomical Watercolor): nét cọ ướt loang màu nước mềm mại giàu cảm xúc, lớp phủ cát vàng rực rỡ, chi tiết hoa văn Ả Rập tinh xảo, bình nước cổ, nhiệt kế sa mạc và đồ thị nhịp tim lâm sàng, phối màu vàng đất son ấm, hổ phách rực rỡ điểm xuyết lam ngọc turquoise quý phái; NỀN TRẮNG TINH hoàn toàn, không watermark, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng. Nhân vật phụ cố định: Cô y tá Cáo Sa Mạc Fennec tai to mặc áo blouse trắng cầm bảng kẹp nhiệt độ; Bác sĩ nội trú Chuột Nhảy Gerbil đeo kính tròn cầm ống tiêm mini; Bác sĩ Kền Kền già đeo kính lão cầm biểu đồ điện tâm đồ; Người du mục Bedouin mặc áo choàng thong dong nhóm lửa. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/12 của video YouTube Shorts về Lạc Đà Sa Mạc). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh màu nước thám hiểm sa mạc Ả Rập kết hợp ký họa thực vật học & giải phẫu Ba Tư (Mirage Oasis Botanical & Anatomical Watercolor): nét cọ ướt loang màu nước mềm mại giàu cảm xúc, lớp phủ cát vàng rực rỡ, chi tiết hoa văn Ả Rập tinh xảo, bình nước cổ, nhiệt kế sa mạc và đồ thị nhịp tim lâm sàng, phối màu vàng đất son ấm, hổ phách rực rỡ điểm xuyết lam ngọc turquoise quý phái; NỀN TRẮNG TINH hoàn toàn, không watermark, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng. Nhân vật phụ: Bệnh nhân người que choáng váng vì sốc nhiệt sa mạc; Bác sĩ cấp cứu hối hả đo nhịp tim. 
```
</details>

## 7. SEO

- **title:** Bệnh Án Sinh Tồn Sa Mạc: Uống 200 Lít Nước Trong 3 Phút Và Bướu Mỡ Chống Nóng 50°C?! | Tập 37
- **hook_paragraph:** Lạc Đà Sa Mạc (Camelus dromedarius) tồn tại giữa cái nóng thiêu đốt 50°C mà không cần giọt nước suốt nhiều tuần. Bướu lạc đà chứa nước hay mỡ? Làm thế nào chúng có thể uống cạn 200 lít nước trong 3 phút mà tế bào máu không phát nổ? Cùng Bác sĩ trưởng phòng giải mã cỗ máy lọc nước sinh học tối thượng!
- **question:** Giữa hồng cầu hình bầu dục giãn nở 240% và mũi ngưng tụ tái chế 60% độ ẩm hơi thở, cỗ máy y sinh nào của Lạc Đà khiến bạn thán phục nhất?
- **next_teaser:** bậc thầy leo vách đá dựng đứng 90 độ ở độ cao 4.000 mét
- **shorts_title:** Lạc đà uống 200 lít nước trong 3 phút mà máu không vỡ?!
- **shorts_desc:** Hồng cầu hình oval co giãn tới 240% giúp lạc đà uống 200 lít nước chỉ trong 3 phút!
- **bullets:** Hồng cầu hình oval co giãn 240%: Uống 200 lít nước trong 3 phút mà không hề vỡ hồng cầu · Bướu mỡ chống nóng 50°C: Tập trung toàn bộ mỡ lên lưng để toàn thân thoát nhiệt tức thì · Mất 30% trọng lượng cơ thể vì mất nước mà máu vẫn duy trì áp suất lưu thông hoàn hảo · Thận siêu cô đặc: Tái hấp thu nước tối đa, thải nước tiểu sánh như si-rô đậm đặc · Mũi lọc hơi thở ngưng tụ 60% độ ẩm: Thở ra không khí khô hoàn toàn để giữ lại từng phân tử nước · Màng tế bào vòm miệng hóa sừng: Nhai nuốt gai nhọn xương rồng dài 5cm như ăn kẹo dẻo
- **tags:** lạc đà sa mạc, camelus dromedarius, sinh tồn sa mạc, y sinh học kỳ thú, vẽ chuyện hoang dã, whiteboard animation

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-37-lac-da-sa-mac
python src/episode/pipeline.py tts    projects/tap-37-lac-da-sa-mac     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-37-lac-da-sa-mac     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-37-lac-da-sa-mac     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-37-lac-da-sa-mac              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-37-lac-da-sa-mac --force
python scripts/beat_sheet.py projects/tap-37-lac-da-sa-mac               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-37-lac-da-sa-mac/audio/shorts.wav projects/tap-37-lac-da-sa-mac/renders/tap-37-lac-da-sa-mac_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-37-lac-da-sa-mac
python src/episode/pipeline.py seo    projects/tap-37-lac-da-sa-mac
python src/episode/episode_doc.py     projects/tap-37-lac-da-sa-mac
```

# MEGA COMPILATION #05 — 10 BỆNH NHÂN QUÁI KIỆT — PHÒNG CẤP CỨU TẠO HÓA · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`mega-05-phong-cap-cuu-tao-hoa`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/mega-05-phong-cap-cuu-tao-hoa`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F_SPECIAL` · **Persona giọng:** `bac_si_truong_khoa` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | 10 bệnh nhân quái kiệt — Phòng Cấp Cứu Tạo Hóa |
| Tiêu đề YouTube | [TẬP ĐẶC BIỆT] Phòng Cấp Cứu Tạo Hóa: Bác Sĩ Khám 10 Sinh Vật Kỳ Lạ Nhất Trái Đất |
| Video dài | `renders/mega-05-phong-cap-cuu-tao-hoa_long.mp4` — 60:19.6 (3619.6s) |
| Shorts | `renders/mega-05-phong-cap-cuu-tao-hoa_shorts.mp4` — 0:53.4 (53.4s) |
| Thumbnail | `renders/mega-05-phong-cap-cuu-tao-hoa_thumbnail.jpg` |
| Số hình | dài 542 beat / 542 ảnh riêng; Shorts 11 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 60:00.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/542 của video YouTube về 10 bệnh nhân quái kiệt — Phòng Cấp Cứu Tạo Hóa). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: ông Bác Sĩ Trưởng Khoa hoạt hình trung niên râu quai nón tỉa gọn, mặc áo blouse trắng có ống nghe y tế quàng qua cổ, kẹp bảng bệnh án bìa da, nét mặt sắc sảo mỉa mai nhưng ánh mắt tinh anh. Nhân vật phụ cố định: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng; ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — BÃO ĐÊM VÀ MƯỜI CA BỆNH
*Thẻ chương:* MƯỜI BỆNH NHÂN DỊ THƯỜNG NHẬP VIỆN

*Badge:* `CA TRỰC ĐÊM` · *mood mặc định:* `nghiem_trang_gia`

**Part 0** → `audio/vs/scene01_p0.wav` (761 ký tự) · mood `nghiem_trang_gia`

```text
Mười hai giờ đêm. Cơn bão giông nhiệt đới cấp mười hai đang gào thét dữ dội ngoài khung cửa kính phòng cấp cứu. Những vệt sét trắng xóa liên tục xé toạc bầu trời, rọi sáng tấm biển đồng cổ kính treo trước cổng lớn: Phòng Cấp Cứu Tạo Hóa. Tôi là Bác Sĩ Trưởng Khoa, người đã cầm dao mổ và ống nghe suốt ba mươi năm qua giữa những ca bệnh nghẹt thở nhất của tự nhiên. Nhưng linh cảm nghề nghiệp mách bảo tôi rằng, đêm nay sẽ là ca trực điên rồ và kỳ quặc nhất trong toàn bộ sự nghiệp y khoa của mình. Chiếc bàn làm việc bằng gỗ sồi của tôi chất đầy những xấp bệnh án ngả vàng, cùng chiếc ống nghe bằng đồng thau sáng bóng. Một ca trực đêm chuẩn mực đòi hỏi tinh thần thép, đôi bàn tay không bao giờ run rẩy và một lượng caffeine đủ để vận hành một đầu máy xe lửa!
```
**Part 1** → `audio/vs/scene01_p1.wav` (398 ký tự) · 🎭 cameo `co_tro_ly`

```text
Bác sĩ trưởng khoa ơi! Nguy to rồi bác sĩ ơi! Toàn bộ chuông báo động ở mười phòng khám chuyên khoa đang reo inh ỏi cùng một lúc kìa! Hệ thống đường dây nóng khẩn cấp của bệnh viện vừa bị nghẽn mạch hoàn toàn vì hàng loạt cuộc gọi cấp cứu dồn dập từ khắp các châu lục! Mười bệnh nhân quái đản nhất hành tinh đang cùng lúc đổ bộ vào sảnh cấp cứu của chúng ta trên đủ mọi loại phương tiện vận chuyển!
```
**Part 2** → `audio/vs/scene01_p2.wav` (826 ký tự) · mood `don_dap`

```text
Bình tĩnh nào cô y tá! Quy tắc số một của phòng cấp cứu: Càng hoảng loạn thì càng phải pha một tách cà phê thật đậm và kiểm tra lại danh sách bệnh nhân! Để tôi đọc to danh sách phân loại bệnh nhân đêm nay cho toàn thể kíp trực cùng nghe xem tạo hóa vừa gửi tới những ca hóc búa nào! Ca số một: Một anh chàng Khỉ Đột Lưng Bạc nặng hai trăm cân, sở hữu cú đấm ngàn cân nhưng đang nằm ôm bụng khóc thét vì ứ đọng khí gas! Ca số hai: Một chú Nhện Lặn Chuông tí hon đang cố tình nhảy ra khỏi mặt nạ thở oxy nhi khoa để lao đầu xuống chậu nước! Ca số ba: Một vận động viên bơi lội có tên Cá Thòi Lòi kiên quyết không chịu nằm yên trong bồn nước mà cứ đòi leo lên bàn khám để chống đẩy! Ca số bốn: Một nữ phẫu thuật viên tí hon mang tên Ong Bắp Cày Ngọc đang dẫn giải một con gián khổng lồ đi vào phòng mổ thần kinh như dắt thú cưng!
```
**Part 3** → `audio/vs/scene01_p3.wav` (812 ký tự) · mood `hao_hung`

```text
Ca số năm: Một khối thịt khổng lồ nặng hai tấn mang tên Cá Mặt Trăng vừa làm sập gãy hoàn toàn chiếc bàn nâng thủy lực của đội vận chuyển! Ca số sáu: Một chàng Vẹt Kakapo béo tròn bốn cân rưỡi chẳng hề biết bay, vừa rơi từ trên cây cao xuống đất vì tưởng mình là đại bàng! Ca số bảy: Một chú Lợn Hươu Babirusa với bốn chiếc răng nanh cong vút dị thường đang có nguy cơ tự đâm thủng hộp sọ của chính mình! Ca số tám: Một quý cô Hươu Cao Cổ cao năm mét đang choáng váng ngất xỉu với chỉ số huyết áp tâm thu vọt lên ngưỡng gần ba trăm mi-li-mét thủy ngân! Ca số chín: Một chú Nhím Lông Nhọn Bắc Mỹ vừa ngã từ cây thông xuống đất và tự cắm hàng trăm chiếc gai sắc nhọn vào đùi của chính mình! Và ca số mười: Một pho tượng đá sống mang tên Cò Mỏ Giày đứng bất động năm tiếng đồng hồ không thèm chớp mắt giữa sảnh chờ!
```
**Part 4** → `audio/vs/scene01_p4.wav` (547 ký tự) · mood `bi_hai`

```text
[laughter] Trời đất ơi! Nhìn vào bảng tiếp nhận này thì đây không phải là một bệnh viện thông thường nữa, mà là một viện bảo tàng giải phẫu học kỳ dị nhất vũ trụ! Bác sĩ trưởng khoa đã từng thấy ca trực nào mà toàn bộ sách giáo khoa giải phẫu kinh điển đều phải xé bỏ viết lại từ đầu như đêm nay chưa? Chưa từng có một tiền lệ nào tương tự trong suốt ba thập kỷ làm nghề y của tôi cả cô y tá thân mến ạ! Mỗi sinh vật đang nằm ngoài kia là một bài toán hóc búa, một nghịch lý cơ thể học thách thức mọi định luật sinh học mà con người từng biết đến!
```
**Part 5** → `audio/vs/scene01_p5.wav` (470 ký tự) · mood `don_dap`

```text
Rầm! Rầm! Rầm! Tiếng đập cửa kính sảnh đón tiếp dồn dập vang lên át cả tiếng sấm rền ngoài trời! Đoàn xe cứu thương chuyên dụng nối đuôi nhau rọi đèn pha vàng rực vào sảnh bệnh viện, còi hụ vang rền xé toạc màn đêm u tối! Các nhân viên điều dưỡng đang hối hả đẩy những chiếc cáng cứu thương quá khổ vào bên trong hành lang lát gạch men sáng loáng! Mùi cồn sát trùng hòa lẫn với mùi ẩm ướt của bùn lầy, mùi tinh dầu thông và hơi muối biển mặn mòi tràn ngập bầu không khí!
```
**Part 6** → `audio/vs/scene01_p6.wav` (514 ký tự) · mood `bi_hai`

```text
Mọi người chú ý giữ trật tự! Xin mời các bệnh nhân không chen lấn xô đẩy tại quầy tiếp đón khẩn cấp! Anh khỉ đột xin vui lòng không dựa lưng vào vách kính tủ thuốc kẻo vỡ kính! Và chú nhím lông nhọn làm ơn giữ khoảng cách an toàn với dép xốp của các cô y tá! [laughter] Toàn thể đội ngũ y bác sĩ nội trú mau chóng vào vị trí trực chiến! Chuẩn bị máy chụp X-quang, máy siêu âm và các bộ dụng cụ vi phẫu ngay lập tức! Đêm nay chúng ta sẽ không chợp mắt dù chỉ một giây để giải mã toàn bộ mười kỳ quan cơ thể học này!
```
**Part 7** → `audio/vs/scene01_p7.wav` (486 ký tự) · mood `nghiem_trang_gia`

```text
Bởi vì nguyên lý tối thượng tại Phòng Cấp Cứu Tạo Hóa của chúng ta luôn luôn là: Không có sinh vật nào trên Trái Đất này sinh ra với một nét giải phẫu thừa thãi hay một cấu trúc sai lầm! Những gì mắt thường nhìn vào tưởng như dị tật, bệnh hoạn hay ngớ ngẩn, thực chất lại là tuyệt tác đỉnh cao của hàng triệu năm chọn lọc tự nhiên khốc liệt! Và nhiệm vụ của người thầy thuốc đêm nay là lắng nghe câu chuyện sinh tồn kỳ diệu được khắc ghi sâu bên trong từng thớ cơ và mạch máu của chúng!
```
**Part 8** → `audio/vs/scene01_p8.wav` (186 ký tự) · 🎭 cameo `phat_thanh_vien`

```text
Thông báo khẩn cấp từ tổng đài bệnh viện: Bệnh nhân số một tại Khoa Cấp Cứu Tổng Hợp đang có dấu hiệu quá tải áp suất ổ bụng nghiêm trọng! Đề nghị Bác Sĩ Trưởng Khoa có mặt ngay lập tức!
```
**Part 9** → `audio/vs/scene01_p9.wav` (126 ký tự) · mood `hao_hung`

```text
Được rồi! Đội ngũ y tế theo tôi bước vào phòng khám số một ngay! Cuộc chiến cứu hộ mười quái kiệt sinh học chính thức bắt đầu!
```

### scene02 — BỤNG ĐẦY KHÍ GAS
*Thẻ chương:* CÚ ĐẤM MỘT TẤN BA VÀ KHÍ GAS

*Badge:* `KHOA CẤP CỨU` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene02_p0.wav` (944 ký tự) · mood `hao_hung`

```text
Bệnh nhân số một, mời vào bàn khám! Khỉ Đột Lưng Bạc, cân nặng hai trăm ki-lô-gam, cơ bắp cuồn cuộn như lực sĩ thể hình hạng nặng! Tôi nhìn vào các chỉ số thể chất ghi trên phiếu tiếp nhận mà không khỏi trầm trồ trước sức mạnh phi thường của loài linh trưởng vĩ đại này. Theo các nghiên cứu cơ sinh học hiện đại, một cú đấm toàn lực của một con khỉ đột đực trưởng thành có lực tác động lên tới một ngàn ba trăm ki-lô-gam! Lực va chạm khủng khiếp đó thừa sức làm bẹp dúm phần đầu của một chiếc xe hơi bốn chỗ hoặc bẻ gãy một thân cây gỗ lim trong nháy mắt! Xương khớp tay chân của khỉ đột dày gấp ba lần xương người, mật độ khoáng chất cao đến mức gần như miễn nhiễm với các chấn thương gãy xương thông thường. Thế nhưng hiện tại, cỗ máy chiến đấu vô địch của những cánh rừng mưa nhiệt đới này lại đang nằm co quắp rên rỉ như một đứa trẻ con! Gương mặt nhăn nhó tội nghiệp của chú khỉ đột to lớn làm cô y tá vừa buồn cười vừa thương cảm vô cùng!
```
**Part 1** → `audio/vs/scene02_p1.wav` (713 ký tự) · mood `nghiem_trang_gia`

```text
Y tá, đặt ống nghe vào góc phần tư ổ bụng bên phải cho tôi! Cẩn thận kẻo anh chàng giật mình lại tung một đòn thì bay cả phòng khám đấy! Tôi áp đầu ống nghe vào lớp da bụng dày cộp căng tròn như chiếc trống đồng của bệnh nhân. Âm thanh truyền vào tai tôi không phải tiếng sôi ruột bình thường, mà là tiếng ùng ục ùng ục rền vang như một lò phản ứng hóa học đang sôi sục! [laughter] Cảm giác như có một cơn lốc xoáy khí gas đang cuộn trào bên trong đường ruột của anh chàng lực sĩ này vậy! Tôi lập tức cho chụp X-quang ổ bụng toàn phần để tìm ra nguyên nhân gốc rễ của cơn đau quằn quại này. Và kết quả trên tấm phim rọi sáng làm cả phòng cấp cứu phải trố mắt kinh ngạc vì sự đồ sộ của hệ thống tiêu hóa bên trong!
```
**Part 2** → `audio/vs/scene02_p2.wav` (336 ký tự) · 🎭 cameo `co_tro_ly`

```text
Bác sĩ ơi, cái bụng anh này chứa toàn là khí gas! Có phải anh ấy ăn nhầm thuốc nổ hay ăn trúng nấm độc gì trong rừng sâu không ạ? Nhìn tấm phim chụp mà em tưởng như đang nhìn vào một quả bóng bay khí cầu khổng lồ sắp nổ tung tới nơi rồi bác sĩ ơi! Em có nên chuẩn bị một chiếc kim chọc hút khí màng bụng để giải áp ngay bây giờ không ạ?
```
**Part 3** → `audio/vs/scene02_p3.wav` (654 ký tự) · mood `hao_hung`

```text
Tuyệt đối không được chọc kim vào bụng bệnh nhân cô y tá nhé! Không hề có chất độc hay thuốc nổ nào ở đây cả! Đây chính là bí mật sinh học vĩ đại nhất của loài khỉ đột mà sách giáo khoa ít khi nhắc tới! Anh chàng này không hề bị ngộ độc dạ dày, mà ổ bụng của anh ấy thực chất là một nhà máy lên men vi sinh vật ruột sau khổng lồ hoạt động ngày đêm! Hãy nhìn vào chế độ ăn uống hàng ngày của loài khỉ đột trong tự nhiên mà xem: một thực đơn làm bất kỳ loài động vật ăn thịt nào cũng phải lắc đầu lè lưỡi! Hàng ngày, một con khỉ đột lưng bạc trưởng thành phải nạp vào cơ thể tới hai mươi đến ba mươi cân lá cây, vỏ cây, thân cây tầm ma và cành non xơ cứng.
```
**Part 4** → `audio/vs/scene02_p4.wav` (591 ký tự) · mood `tram_bi_an`

```text
Đặc biệt là những cây tầm ma có đầy gai châm chứa độc tố histamine và axit formic gây ngứa rát buốt da người, nhưng chú khỉ đột lại nhai ngấu nghiến ngon lành! Bởi vì tuyến nước bọt của khỉ đột tiết ra các enzym đặc biệt có tính kiềm cao, nhanh chóng trung hòa toàn bộ các phân tử độc tố gây bỏng rát trước khi lá trôi xuống dạ dày! Hệ tiêu hóa thông thường của con người hay các loài ăn quả hoàn toàn bất lực trước lượng chất xơ thô cellulose khổng lồ và dai nhách này. Nếu chúng ta ăn đống lá cây xơ xác đó vào bụng, dạ dày sẽ bị thủng hoặc tắc ruột ngay lập tức vì không thể tiêu hóa nổi!
```
**Part 5** → `audio/vs/scene02_p5.wav` (1207 ký tự) · mood `don_dap`

```text
Nhưng tạo hóa đã trang bị cho khỉ đột một chiếc manh tràng và đại tràng với dung tích khổng lồ, chứa hàng nghìn tỷ vi khuẩn kỵ khí chuyên biệt! Các vi khuẩn cộng sinh này làm việc miệt mài ngày đêm để bẻ gãy các liên kết phân tử cellulose cứng rắn nhất thành các hợp chất đơn giản hơn. Thời gian lưu chuyển thức ăn trong đại tràng của khỉ đột kéo dài từ ba mươi lăm đến hơn bốn mươi giờ liên tục, đủ để vi khuẩn phân giải triệt để từng sợi xơ thực vật! Quá trình lên men vi sinh vật tự nhiên này giải phóng ra một lượng khí gas khổng lồ, đồng thời tổng hợp nên các axit béo chuỗi ngắn cực kỳ giàu năng lượng! Nghiên cứu dinh dưỡng đột phá trong công trình khoa học nổi tiếng của tiến sĩ Popovich trên Tạp Chí Dinh Dưỡng học đã chứng minh một sự thật chấn động toàn cầu: Tới bảy mươi phần trăm tổng năng lượng calo mỗi ngày của khỉ đột không đến từ đường hay tinh bột, mà đến từ chính quá trình lên men chất xơ này! Các axit béo chuỗi ngắn sau khi lên men được hấp thu trực tiếp qua thành đại tràng, đi thẳng vào máu và nuôi dưỡng toàn bộ khối cơ bắp khổng lồ của con vật! Chúng hoạt động tương tự như loài bò hay ngựa, nhưng thay vì lên men ở dạ cỏ phía trước thì khỉ đột lên men ở ruột sau vô cùng tinh vi!
```
**Part 6** → `audio/vs/scene02_p6.wav` (701 ký tự) · mood `am_ap`

```text
Nói cách khác, cái bụng bự phình to của anh chàng không phải là mỡ thừa lười biếng, mà là một cỗ máy sinh học siêu đẳng biến cỏ rác thành cơ bắp cuồn cuộn! Nhưng hôm nay, do ăn hơi nhiều mầm tre non lên men nhanh vào buổi chiều nên lượng khí gas sinh ra quá mức làm căng tức thành bụng tạm thời mà thôi! Được rồi anh bạn cơ bắp, tôi kê đơn cho anh hai viên men tiêu hóa thảo dược và một tách trà gừng ấm để tống bớt lượng khí thừa ra ngoài nhé! Chỉ cần ợ hơi vài tiếng sấm sét là anh lại có thể đấm vỡ đá và vỗ ngực vang rền khắp thảo nguyên được rồi! [laughter] Ca cấp cứu số một của Phòng Cấp Cứu Tạo Hóa hoàn thành xuất sắc! Giờ thì y tá, chuyển ngay hồ sơ ca số hai sang Khoa Hô Hấp Ngược cho tôi!
```

### scene03 — BÌNH DƯỠNG KHÍ TỰ DỆT
*Thẻ chương:* LẶN HAI MƯƠI TƯ GIỜ DƯỚI NƯỚC

*Badge:* `KHOA HÔ HẤP` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene03_p0.wav` (600 ký tự) · mood `tram_bi_an`

```text
Cánh cửa phòng khám Khoa Hô Hấp Ngược mở ra với một bầu không khí ẩm ướt lạ thường. Và bệnh nhân số hai đang nằm trong một tình huống dở khóc dở cười nhất từ trước tới nay trong lịch sử cấp cứu của chúng tôi. Chú Nhện Lặn Chuông tí hon dài chưa đầy hai xăng-ti-mét đang dùng hết sức bình sinh để trốn khỏi chiếc mặt nạ thở oxy nhi khoa! Mỗi lần cô y tá đưa chiếc ống thở tới gần mũi, chú nhện lại cắn phăng một nhát rồi lặn một hơi mất tăm xuống tận đáy chậu nước! Chiếc đuôi nhỏ xíu của nó khẽ lắc lư, để lộ một vầng hào quang lấp lánh như viên ngọc trai bọc quanh phần bụng dưới làn nước trong vắt.
```
**Part 1** → `audio/vs/scene03_p1.wav` (337 ký tự) · 🎭 cameo `co_tro_ly`

```text
Bác sĩ ơi em chụp mặt nạ oxy vào mặt nó mà nó cứ cắn đứt dây rồi nhảy xuống nước! Con nhện này bị trầm cảm muốn tự vẫn hay sao ấy ạ? Em vớt nó lên thở không khí bình thường thì nó cứ nằm đờ đẫn ra, thế mà vừa thả vào nước là nó bơi nhanh như một chiếc tàu ngầm mini! Có khi nào con nhện này bị đột biến gen thành loài cá không bác sĩ ơi?
```
**Part 2** → `audio/vs/scene03_p2.wav` (812 ký tự) · mood `hao_hung`

```text
[laughter] Bình tĩnh nào cô y tá! Nó không hề muốn tự vẫn đâu, mà chúng ta đang ép một thợ lặn chuyên nghiệp thở theo cách của người đi bộ trên cạn đấy! Đây là loài nhện duy nhất trong số hơn năm mươi ngàn loài nhện đã được phát hiện trên Trái Đất dành toàn bộ cuộc đời của mình dưới đáy nước ngọt! Nó sinh ra dưới nước, săn mồi dưới nước, giao phối dưới nước, đẻ trứng dưới nước và thậm chí ngủ đông cũng ở dưới đáy bùn nước! Thế nhưng về mặt nguồn gốc giải phẫu, nhện lặn chuông vẫn là một loài chân khớp thở bằng phổi sách và hệ thống ống khí quản trên cạn. Nghĩa là nó bắt buộc phải hít thở khí oxy dạng phân tử tự do trong không khí chứ mang của nó hoàn toàn không thể lọc oxy hòa tan như loài cá! Vậy làm thế nào mà một sinh vật thở bằng không khí lại có thể sống cả đời dưới nước mà không hề bị chết đuối?
```
**Part 3** → `audio/vs/scene03_p3.wav` (866 ký tự) · mood `don_dap`

```text
Câu trả lời nằm ở một phát minh công nghệ nano sinh học độc nhất vô nhị mà loài nhện này đã hoàn thiện qua hàng triệu năm tiến hóa! Toàn bộ vùng bụng và các kẽ chân của nhện lặn chuông được bao phủ bởi hàng triệu sợi lông kỵ nước siêu nhỏ với mật độ dày đặc phi thường. Mỗi khi cần dưỡng khí, chú nhện chỉ việc nhô phần đuôi lên khỏi mặt nước trong đúng một phần mười giây rồi lặn nhanh xuống. Lớp lông kỵ nước lập tức bẫy chặt một lớp màng không khí bao quanh toàn bộ cơ thể, biến con nhện thành một thợ lặn bọc trong một chiếc áo giáp khí óng ánh như bạc! Hai chiếc chân sau của nó được cấu tạo như những chiếc bàn chải chuyên dụng, thường xuyên chải chuốt các sợi lông để loại bỏ cặn bẩn bám dính, giữ cho lớp áo giáp khí luôn thông thoáng! Không chỉ dừng lại ở chiếc áo giáp khí di động đó, con nhện còn tiến hành xây dựng cả một căn cứ quân sự ngầm dưới đáy hồ!
```
**Part 4** → `audio/vs/scene03_p4.wav` (801 ký tự) · mood `tram_bi_an`

```text
Kỳ quan thực sự nằm ở chiếc chuông lặn mà chú nhện dệt nên dưới đáy hồ bằng chính những sợi tơ chuyên dụng của mình! Nó nhả ra những sợi tơ nhện không thấm nước đặc biệt, đan kết chúng thành một mái vòm hình chiếc chuông úp ngược neo chặt vào các thân rong rêu thủy sinh. Sau đó, nhện liên tục ngoi lên mặt nước, dùng bụng vận chuyển từng bọt khí lớn lặn xuống nhả vào bên trong mái vòm tơ. Mái vòm tơ căng phồng lên như một quả bóng khí trong suốt, chú nhện thong thả chui vào bên trong ngồi nghỉ ngơi khô ráo! Và đây là điều kỳ diệu nhất mà nghiên cứu kinh điển của giáo sư Seymour công bố trên Tạp Chí Sinh Học Thực Nghiệm đã chứng minh: Chiếc chuông lặn bằng tơ này không chỉ là một cái kho chứa khí thụ động, mà nó hoạt động chính xác như một lá phổi vật lý hay một chiếc mang nhân tạo siêu việt!
```
**Part 5** → `audio/vs/scene03_p5.wav` (849 ký tự) · mood `don_dap`

```text
Khi nhện tiêu thụ oxy bên trong chuông, nồng độ oxy trong chuông giảm xuống thấp hơn nồng độ oxy hòa tan trong nước xung quanh chiếc chuông. Chênh lệch áp suất riêng phần này thúc đẩy các phân tử oxy từ nước tự động khuếch tán thẩm thấu xuyên qua màng tơ mỏng đi vào bên trong chuông! Đồng thời, khí các-bô-níc độc hại do con nhện thở ra sẽ dễ dàng hòa tan và khuếch tán ngược ra ngoài dòng nước chảy xung quanh. Nhờ cơ chế trao đổi khí thần kỳ đó, lượng oxy khuếch tán vào chuông có thể đáp ứng đủ nhu cầu hô hấp của chú nhện suốt hơn hai mươi tư giờ liên tục! Con nhện có thể nằm ngủ say sưa, ăn thịt con mồi và chăm sóc bầy con non trong chiếc chuông lặn suốt cả ngày đêm mà không cần phải ngoi lên mặt nước một lần nào! Thậm chí chú nhện đực còn dệt chiếc chuông lặn lớn hơn con cái ba mươi phần trăm để làm phòng tân hôn lãng mạn dưới đáy nước!
```
**Part 6** → `audio/vs/scene03_p6.wav` (447 ký tự) · mood `hao_hung`

```text
Vào mùa đông băng giá khi mặt hồ đóng băng dày đặc, nhện chỉ việc rút sâu xuống đáy bùn, gia cố chuông tơ thật kín và ngủ đông yên bình ở nhiệt độ không độ C! Lớp màng tơ nhện bảo vệ nó khỏi các tinh thể băng giá sắc nhọn và giữ cho áp suất dưỡng khí bên trong luôn ở mức ổn định suốt nhiều tháng ròng! Thử hỏi có chiếc tàu ngầm hạt nhân hay bộ đồ lặn hiện đại nào của loài người có thể hoạt động bền bỉ và thông minh đến mức độ như thế này không?
```
**Part 7** → `audio/vs/scene03_p7.wav` (478 ký tự) · mood `am_ap`

```text
Chẩn đoán Khoa Hô Hấp Ngược của Phòng Cấp Cứu Tạo Hóa: Bệnh nhân sở hữu hệ hô hấp dưới nước hiện đại và tiết kiệm năng lượng nhất hành tinh! Đơn thuốc cho bệnh nhân: một bể thủy tinh nước ngọt sâu ba mươi xăng-ti-mét, bổ sung vài cành rong đuôi chó tươi ngon và tuyệt đối cấm dùng mặt nạ thở oxy! [laughter] Bệnh nhân số hai đã tìm lại được bầu không khí quen thuộc! Giờ thì mời toàn đội di chuyển sang Khoa Chấn Thương Chỉnh Hình để đón tiếp một vận động viên điền kinh có vây!
```

### scene04 — VÂY BIẾN THÀNH CHÂN ĐIỀN KINH
*Thẻ chương:* MẮT KÍNH TIỀM VỌNG VÀ CÚ NHẢY SÁU MƯƠI PHÂN

*Badge:* `CHẤN THƯƠNG` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene04_p0.wav` (678 ký tự) · mood `don_dap`

```text
Huỳnh huỵch! Bẹp bẹp bẹp! Tiếng đập sàn dồn dập vang lên ngay khi chúng tôi vừa mở cửa phòng khám Khoa Chấn Thương Chỉnh Hình! Và cảnh tượng trước mắt làm các bác sĩ ngoại khoa phải đứng hình trong kinh ngạc! Một chú Cá Thòi Lòi dài hai mươi xăng-ti-mét, mình mẩy lấm lem bùn đất, đang dùng hai chiếc vây ngực cơ bắp chống thẳng đứng trên mặt bàn như một lực sĩ đang hít đất! Đôi mắt to tròn như hai chiếc kính tiềm vọng nhô hẳn lên trên đỉnh đầu, xoay tít ba trăm sáu mươi độ quét nhìn khắp lượt các bác sĩ trong phòng khám! Cứ mỗi lần cô y tá cầm chiếc khăn ẩm tiến lại gần, chú cá lại quẫy đuôi một cú đánh tách, phóng bổng người lên không trung cao tới sáu mươi xăng-ti-mét!
```
**Part 1** → `audio/vs/scene04_p1.wav` (349 ký tự) · 🎭 cameo `co_tro_ly`

```text
Bác sĩ ơi bắt nó lại giùm em với! Con cá này bị co giật động kinh hay bị gãy xương chậu mà nó cứ nhảy lung tung khắp phòng thế này ạ? Nó là loài cá mà sao nó không chịu ở dưới nước, lại cứ thích leo lên bậc cửa sổ rồi leo lên bàn làm việc ngồi nhìn ra ngoài đường thế này? Có khi nào xương vây của nó bị biến dạng thành chân khỉ rồi không bác sĩ ơi?
```
**Part 2** → `audio/vs/scene04_p2.wav` (1012 ký tự) · mood `hao_hung`

```text
[laughter] Hãy cất chiếc vợt lưới đi cô y tá! Đây không phải là cá bị co giật, mà là sinh vật chuyển tiếp vĩ đại nhất còn sống sót từ kỷ Devon cách đây gần bốn trăm triệu năm! Cá Thòi Lòi là loài cá lưỡng cư độc nhất vô nhị có thể dành tới chín mươi phần trăm thời gian trong ngày sống hoàn toàn trên cạn! Nó có thể đi bộ, chạy nước rút trên bùn lầy, trèo thoăn thoắt lên các rễ cây đước và thậm chí nhảy cao gấp ba lần chiều dài cơ thể mình! Hãy nhìn vào cấu trúc giải phẫu của hai chiếc vây ngực này trên phim chụp X-quang: Đây chính là tiền thân của đôi cánh tay và đôi chân động vật bốn chân trên cạn! Các xương vây ngực đã tiến hóa thành các khớp xương trục có cơ bắp khỏe khoắn nâng đỡ, hoạt động tương tự như khuỷu tay và cổ tay của động vật trên cạn! Hai vây bụng của nó hợp nhất lại ở phía dưới tạo thành một giác hút hình chiếc cốc vô cùng chắc chắn! Vào mùa giao phối, các chàng cá đực còn dựng đứng chiếc vây lưng sặc sỡ như một cánh buồm ngũ sắc, nhảy múa tưng bừng trên bãi bùn để thu hút bạn tình!
```
**Part 3** → `audio/vs/scene04_p3.wav` (717 ký tự) · mood `don_dap`

```text
Nhưng bí ẩn lớn nhất khiến các nhà sinh lý học hô hấp phải kinh ngạc là: Làm thế nào một con cá có thể thở trên cạn suốt nhiều giờ liền mà không bị ngạt thở? Bởi vì mang cá thông thường khi lên cạn sẽ bị khô ráp, các phiến mang dính bết lại với nhau làm mất diện tích tiếp xúc với không khí và con cá sẽ chết ngạt nhanh chóng! Thế nhưng cá thòi lòi lại sở hữu hai khoang mang khổng lồ có van đóng mở kín mít như hai chiếc bình dưỡng khí của thợ lặn! Trước khi rời khỏi mặt nước để bò lên bãi bùn, nó ngậm đầy một họng nước và không khí rồi siết chặt van nắp mang lại! Bằng cách đó, các phiến mang bên trong luôn luôn được ngâm ngập trong nước giàu dưỡng khí, cho phép nó hô hấp bình thường ngay giữa bãi cạn khô khốc!
```
**Part 4** → `audio/vs/scene04_p4.wav` (971 ký tự) · mood `tram_bi_an`

```text
Chưa hết đâu nhé! Cá thòi lòi còn có khả năng hô hấp qua da và niêm mạc miệng cực kỳ tinh vi! Hơn năm mươi phần trăm lượng oxy của nó được hấp thu trực tiếp qua lớp da mỏng giàu mạch máu, miễn là da của nó luôn được giữ ẩm ướt! Đó là lý do tại sao anh chàng này thỉnh thoảng lại lăn lộn trên bùn nhão để tráng một lớp bùn bảo vệ giữ ẩm cho làn da của mình! Và các bạn hãy nhìn vào đôi mắt kỳ diệu nhô cao trên đỉnh đầu của nó mà xem! Đó là hai chiếc kính tiềm vọng thực thụ giúp nó vừa ngâm mình dưới nước vừa quan sát được toàn bộ con mồi và kẻ thù trên cạn! Mỗi khi mắt bị khô do gió biển, cá thòi lòi chỉ việc thụt hai mắt vào trong hốc đầu, nơi có một túi nước đặc biệt để rửa sạch và cấp ẩm cho giác mạc rồi lại đẩy mắt nhô lên! Thật là một cơ chế chớp mắt độc nhất vô nhị không hề giống bất kỳ loài động vật có xương sống nào trên Trái Đất! Cá thòi lòi còn có một tập tính kỳ lạ là trèo lên các thân cây đước cao để phơi nắng và tránh thủy triều dâng cao cuốn trôi!
```
**Part 5** → `audio/vs/scene04_p5.wav` (950 ký tự) · mood `don_dap`

```text
Vào mùa sinh sản, những chú cá thòi lòi đực còn đào những chiếc hang bùn sâu tới một mét rưỡi có cấu trúc hình chữ U vô cùng phức tạp! Đáy hang là một túi khí ngầm hoàn toàn kỵ khí và không có dưỡng khí tự nhiên. Để bảo vệ bầy trứng non, cá bố liên tục ngoi lên mặt nước ngậm từng ngụm không khí rồi lặn xuống đáy hang nhả vào buồng ấp trứng! Nó thực hiện hàng trăm chuyến lặn tiếp oxy như một thợ lặn chuyên nghiệp để nuôi dưỡng bầy con thơ! Thật là một người cha mẫu mực và một chiến binh sinh học kiên cường bậc nhất của thế giới ngập mặn! Chúng còn đắp những bức tường thành bằng bùn cao tới mười phân quanh miệng hang để phân chia ranh giới lãnh thổ với hàng xóm! Khi có kẻ thù xâm phạm bờ cõi, chàng cá lập tức dựng vây lưng lên thách đấu và búng người tung cú húc đầu sấm sét để đuổi kẻ lạ mặt! Các nhà cổ sinh vật học coi cá thòi lòi như một hóa thạch sống phản chiếu chính xác bước chuyển mình vĩ đại của sinh giới từ đại dương lên đất liền!
```
**Part 6** → `audio/vs/scene04_p6.wav` (462 ký tự) · mood `am_ap`

```text
Chẩn đoán Khoa Chấn Thương Chỉnh Hình của Phòng Cấp Cứu Tạo Hóa: Không có gãy xương hay dị tật nào cả! Đây là một vận động viên điền kinh lưỡng cư khỏe mạnh tròn trăm phần trăm! Đơn thuốc cho bệnh nhân: Một khay bùn ngập mặn ẩm ướt pha chút muối biển và vài nhánh rễ cây để anh chàng tha hồ tập hít đất và leo trèo! [laughter] Vừa dứt lời thì từ sảnh chính bỗng vang lên một tiếng rầm chấn động cả sàn nhà! Báo động đỏ: Phòng chờ cấp cứu vừa bị sập một mảng sàn!
```

### scene05 — HAI TẤN THỊT ĐÈ BẸP BÀN NÂNG
*Thẻ chương:* CƠ CƠN BÁO ĐỘNG ĐỎ VÀ KHỐI SỤN HAI TẤN

*Badge:* `PHÒNG CHỜ NÁO LOẠN` · *mood mặc định:* `bi_hai`

**Part 0** → `audio/vs/scene05_p0.wav` (889 ký tự) · mood `bi_hai`

```text
[sigh] Một giờ ba mươi phút sáng. Tôi vừa bước chân ra khỏi Khoa Chấn Thương thì một tiếng rầm long trời lở đất vang lên làm rung chuyển cả tòa nhà bệnh viện! Các giá thuốc thủy tinh rung lên bần bật kêu leng keng, sàn gạch men dưới chân tôi nứt toác ra một đường dài ba mét! Tiếng còi báo động khẩn cấp rú lên từng hồi chói tai, hòa lẫn với tiếng thét thất thanh của đội điều dưỡng tiếp đón ngoài cửa sảnh! Trời đất quỷ thần ơi! Chuyện gì vừa xảy ra thế này? Xe tải chở đá tảng đâm sập cổng bệnh viện hay có thiên thạch vừa rơi trúng phòng tiếp đón vậy? Cả bệnh viện rung chuyển như vừa trải qua một trận động đất bảy độ richter giữa đêm khuya thanh vắng! Hàng loạt hồ sơ bệnh án bay tứ tung giữa làn khói bụi mịt mù, tiếng chuông điện thoại bàn reo inh ỏi không dứt! Tiếng la hét hỗn loạn của đội vận chuyển làm cả tòa nhà như biến thành một công trường xây dựng gặp sự cố sập giàn giáo!
```
**Part 1** → `audio/vs/scene05_p1.wav` (0 ký tự) · mood `bi_hai`

```text

```
**Part 2** → `audio/vs/scene05_p2.wav` (519 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Bác sĩ trưởng khoa ơi cứu tụi em với! Cái bàn nâng thủy lực tải trọng hai tấn của đội vận chuyển vừa bị gãy đôi làm đôi mảnh rồi! Chúng em vừa khiêng bệnh nhân số bốn từ xe tải thùng bạt xuống cáng thì cái cáng sắt gãy đánh rắc một cái, đè bẹp dúm luôn cả chiếc xe đẩy thuốc bên dưới! Bệnh nhân này to như một gian nhà lá, trơn tuột như cục xà bông khổng lồ và không có cổ, không có đuôi gì hết trơn bác sĩ ơi! Chúng em đã phải huy động tới sáu người đàn ông lực lưỡng mà vẫn không thể nhích nổi nó một xăng-ti-mét nào!
```
**Part 3** → `audio/vs/scene05_p3.wav` (942 ký tự) · mood `don_dap`

```text
Tôi vội vàng rẽ đám đông bước tới hiện trường, và một cảnh tượng choáng ngợp hiện ra làm tôi phải dụi mắt ba lần! Nằm sừng sững giữa sảnh đón tiếp của Phòng Cấp Cứu Tạo Hóa là một chiếc bánh kếp sinh học khổng lồ hình tròn dẹt, dài hơn ba mét và cao gần bốn mét! Đó là Cá Mặt Trăng đại dương Mola mola, loài cá có xương nặng nhất hành tinh, với cân nặng đo được tại chỗ lên tới hai tấn tròn trĩnh! Toàn bộ cơ thể của nó dường như chỉ có một cái đầu khổng lồ gắn liền với hai chiếc vây dài ngoằng dựng đứng lên trời và chỉa xuống đất! Không hề có vây đuôi bình thường như các loài cá khác, phần đuôi của nó bị tiêu giảm thành một dải diềm lượn sóng ngắn ngủn nhìn như bị ai đó dùng dao cắt cụt! Bộ xương sống của nó đã tiêu giảm gần hết, chỉ còn lại đúng mười sáu đốt sống lưng, ít nhất trong toàn bộ thế giới các loài cá! Hai chiếc vây lưng và vây hậu môn dài ngoằng đập so le nhịp nhàng như đôi cánh chim bay lượn giữa lòng đại dương bao la!
```
**Part 4** → `audio/vs/scene05_p4.wav` (1023 ký tự) · mood `hao_hung`

```text
Và điều làm cô y tá hoảng sợ nhất chính là cái miệng của nó: Cái miệng tròn vo hình chữ O đang há hốc ra ngơ ngác, hoàn toàn không thể khép lại được! Đôi mắt to tròn như hai chiếc đĩa sứ chớp chớp chậm rãi nhìn trần nhà với vẻ mặt ngơ ngác đến mức tội nghiệp! Bác sĩ ơi, có phải nó bị tai biến mạch máu não làm liệt cơ hàm méo miệng rồi không? Sao cái miệng nó cứ há toang hoác ra thế kia mà không chịu ngậm lại? Không hề có tai biến hay liệt cơ nào ở đây cả cô y tá thân mến! Đó là cấu trúc hàm hợp nhất tự nhiên của bộ cá nóc mà loài cá này thuộc về! Răng của nó đã tiêu biến và hợp nhất lại thành một chiếc mỏ sừng sắc bén, dùng để hút và nghiền nát những con sứa biển trơn tuột dưới đại dương sâu thẳm! Thức ăn ưa thích của nó là các loài động vật thân mềm bồng bềnh chứa tới chín mươi lăm phần trăm là nước và cực kỳ ít calo, khiến con vật phải ăn liên tục suốt ngày đêm! Lớp sụn xơ dày cộp bao bọc quanh người hoạt động như một lớp đệm hấp thu xung lực va đập tự nhiên, giúp nó an toàn trước các đợt sóng biển dữ dội!
```
**Part 5** → `audio/vs/scene05_p5.wav` (563 ký tự) · mood `tram_bi_an`

```text
Nhưng điều làm tôi lo ngại nhất lúc này không phải là chiếc miệng, mà là áp lực trọng lực đang đè nén lên các cơ quan nội tạng của con vật! Dưới đáy đại dương, lực đẩy Ác-si-mét nâng đỡ toàn bộ khối cơ thể hai tấn này một cách nhẹ nhàng êm ái. Nhưng khi bị đưa lên cạn, trọng lượng khổng lồ sẽ ép bẹp các mạch máu và làm suy hô hấp nghiêm trọng nếu không được giải phóng kịp thời! Hơn nữa, trên lớp da dày tới bảy xăng-ti-mét rưỡi bằng sụn xơ của nó đang có hơn bốn mươi loài ký sinh trùng khác nhau đang bám dính dày đặc như một viện bảo tàng ký sinh trùng sống!
```
**Part 6** → `audio/vs/scene05_p6.wav` (179 ký tự) · 🎭 cameo `co_tro_ly`

```text
Bác sĩ trưởng khoa ơi, da nó dày cứng như lốp xe tải thế này thì kim tiêm nào đâm cho thủng được ạ? Chúng ta phải làm sao để cứu anh chàng khổng lồ ngơ ngác này bây giờ bác sĩ ơi?
```
**Part 7** → `audio/vs/scene05_p7.wav` (520 ký tự) · mood `bi_hai`

```text
Nhìn vẻ mặt ngơ ngác vô tội của nó giữa sảnh bệnh viện mà tôi vừa buồn cười vừa xót xa cho sinh vật đại dương này! Trong lịch sử hàng hải cổ đại, các thủy thủ từng lầm tưởng chiếc vây lưng nhô cao của cá mặt trăng là thủy quái kraken khổng lồ! Thế nhưng thực tế nó lại là sinh vật hiền lành và ngờ nghệch bậc nhất đại dương, thậm chí để mặc cho hải cẩu và cá kình rỉa vây mà chẳng hề buồn chống cự! Đã có những trường hợp cá mặt trăng trôi dạt vào bãi tắm làm cả bờ biển náo loạn vì tưởng quái vật ngoài hành tinh đổ bộ!
```
**Part 8** → `audio/vs/scene05_p8.wav` (481 ký tự) · mood `nghiem_trang_gia`

```text
Đội cứu hộ khẩn cấp nghe lệnh tôi! Lập tức điều động chiếc xe cẩu chuyên dụng mười tấn và dây đai bạt cứu hộ vào sảnh đón tiếp ngay lập tức! Chúng ta không thể khám bệnh cho khối thịt hai tấn này trên sàn nhà cứng ngắc này được! Mở van nước xả đầy chiếc bể ngâm nước muối sinh lý dung tích năm mươi mét khối ở Khoa Hồi Sức Cấp Cứu Đại Dương! Dùng dây đai bạt luồn nhẹ nhàng dưới bụng cá mặt trăng, cẩu bổng anh chàng lên và chuyển thẳng vào bể hồi sức ngay trong mười lăm phút tới!
```
**Part 9** → `audio/vs/scene05_p9.wav` (397 ký tự) · mood `don_dap`

```text
Một, hai, ba, nâng! Dưới sự điều khiển nhịp nhàng của kíp trực, khối sinh vật hai tấn từ từ được nhấc bổng lên không trung trong sự reo hò thán phục của toàn thể bệnh nhân trong sảnh! Sàn sảnh đón tiếp tạm thời được giải tỏa an toàn! Nhưng đừng vội mừng, vì ngay cạnh phòng mổ số hai, tiếng kêu thất thanh của một chú gián đang báo hiệu ca phẫu thuật thần kinh dị thường nhất trần đời vừa bắt đầu!
```

### scene06 — BÁC SĨ TÍ HON THÔI MIÊN GIÁN
*Thẻ chương:* HAI MŨI TIÊM THẦN KINH VÀ ZOMBIE

*Badge:* `PHẪU THUẬT NÃO` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene06_p0.wav` (774 ký tự) · mood `tram_bi_an`

```text
Cánh cửa phòng mổ thần kinh số hai mở ra trong một bầu không khí lạnh ngắt và tĩnh lặng đến gai người. Trên bàn mổ chính bọc khăn vải xanh vô trùng, một cảnh tượng rùng rợn và kỳ quái làm bất kỳ ai chứng kiến cũng phải sởn gai ốc từ đầu đến chân! Một chú gián Mỹ khổng lồ dài năm xăng-ti-mét, to gấp sáu lần một con ong, đang đứng im phăng phắc như một pho tượng gỗ vô hồn! Hai chiếc râu dài của nó bị cắt cụt một nửa, đôi mắt kép đờ đẫn mất hoàn toàn phản xạ trốn chạy hay phòng vệ tự nhiên! Và đứng kiêu hãnh trên lưng chú gián khổng lồ là bệnh nhân số năm của chúng ta: Cô Ong Bắp Cày Ngọc Ampulex compressa! Cô ong đang dùng chiếc vòi miệng tí hon của mình bình thản gặm nhấm vết cắt ở râu chú gián để hút dịch bạch huyết như đang thưởng thức một ly nước ngọt giải khát!
```
**Part 1** → `audio/vs/scene06_p1.wav` (331 ký tự) · 🎭 cameo `co_tro_ly`

```text
Bác sĩ trưởng khoa ơi cứu em với! Con ong xanh lấp lánh kia nó vừa làm phép phù thủy biến con gián thành thây ma sống kìa! Con gián to gấp sáu lần con ong, chân cẳng khỏe như lực sĩ mà sao nó không thèm đá văng con ong ra để chạy trốn hả bác sĩ? Có phải con ong này biết thuật thôi miên tà đạo hay dùng bùa ngải gì không bác sĩ ơi?
```
**Part 2** → `audio/vs/scene06_p2.wav` (564 ký tự) · mood `hao_hung`

```text
[laughter] Không hề có bùa ngải hay phép thuật phù thủy nào ở đây cả cô y tá thân mến! Đây chính là nữ phẫu thuật viên thần kinh lỗi lạc và tàn nhẫn nhất trong toàn bộ lịch sử tiến hóa của giới côn trùng! Loài ong bắp cày ngọc này không hề giết chết con gián, mà nó thực hiện một ca phẫu thuật não bộ hai giai đoạn với độ chính xác cơ học vượt xa tay nghề của các giáo sư ngoại thần kinh hàng đầu loài người! Hãy nhìn vào quy trình hai mũi tiêm thần kinh chết người mà nghiên cứu kinh điển của giáo sư Libersat công bố trên Tạp Chí Sinh Học Thực Nghiệm đã giải mã!
```
**Part 3** → `audio/vs/scene06_p3.wav` (803 ký tự) · mood `don_dap`

```text
Mũi tiêm thứ nhất: Khi bắt gặp con gián, ong bắp cày lao tới vật ngửa con mồi ra và cắm ngập chiếc ngòi sắc bén vào hạch thần kinh ngực đầu tiên của con gián! Mũi tiêm đầu tiên này chứa một lượng lớn chất dẫn truyền thần kinh ức chế GABA và các chất làm tê liệt cơ bắp tạm thời. Trong đúng hai phút đồng hồ, hai chân trước của con gián bị tê liệt hoàn toàn, khiến nó không thể giơ chân lên gạt đòn hay phản kháng được nữa! Và đây mới là đỉnh cao giải phẫu học làm rung chuyển giới y khoa: Mũi tiêm thứ hai xuyên thẳng qua lớp vỏ kitin cứng ở cổ, chọc sâu vào tận hạch thần kinh dưới thực quản bên trong não bộ con gián! Chiếc ngòi của ong được trang bị các cơ quan thụ cảm cơ học và hóa học siêu nhỏ, cho phép nó cảm nhận và định vị chính xác hạch não trong bóng tối tăm mù mịt bên trong hộp sọ con mồi!
```
**Part 4** → `audio/vs/scene06_p4.wav` (530 ký tự) · mood `tram_bi_an`

```text
Nọc độc của mũi tiêm thứ hai là một ly cocktail hóa sinh phức tạp bậc nhất tự nhiên, chứa các chất ức chế thụ thể dopamine và octopamine chuyên biệt! Chất octopamine là chất kích hoạt phản xạ trốn chạy khi gặp nguy hiểm ở loài côn trùng. Khi bị nọc độc khóa chặt thụ thể này, con gián hoàn toàn mất đi ý chí sinh tồn và phản xạ tự vệ, biến thành một thây ma sống đúng nghĩa đen! Chú gián vẫn thở bình thường, tim vẫn đập, chân cẳng vẫn hoạt động tốt, nhưng động lực tự bước đi để cứu lấy bản thân đã bị xóa sổ tròn trăm phần trăm!
```
**Part 5** → `audio/vs/scene06_p5.wav` (703 ký tự) · mood `tram_bi_an`

```text
Sau đó, cô ong cắt bớt hai chiếc râu dài của gián để uống dịch bạch huyết bù đắp năng lượng tiêu hao sau trận đấu vật căng thẳng! Rồi cô ong ngậm lấy phần gốc râu còn lại, dắt con gián to lớn lững thững đi theo mình về chiếc tổ ngầm dưới lòng đất như dắt một chú cún ngoan ngoãn đi dạo phố! Tại chiếc tổ đó, ong sẽ đẻ một quả trứng duy nhất lên bụng con gián, niêm phong cửa hang lại bằng đất đá. Sau khi đẻ trứng xong, cô ong mẹ còn tỉ mỉ nhặt từng viên sỏi nhỏ và cành cây khô che phủ kín miệng hang để ngụy trang tuyệt đối trước các loài săn mồi khác! Con gián sống thực vật này đóng vai trò như một kho thực phẩm tươi sống hoàn hảo, nuôi dưỡng ấu trùng ong lớn lên cho tới ngày lột xác bay ra ngoài!
```
**Part 6** → `audio/vs/scene06_p6.wav` (645 ký tự) · mood `tram_bi_an`

```text
Cơ quan thị giác và xúc giác ở chân của cô ong bắp cày ngọc tinh vi đến mức có thể nếm được mùi vị dịch mô của con mồi qua lớp lông cảm ứng! Bằng cách cọ nhẹ bàn chân lên đầu chú gián, cô ong có thể đo đạc chính xác nồng độ độc tố thần kinh còn tồn đọng trong mô não con mồi! Nếu liều lượng thuốc tê quá nhẹ, con gián có thể hồi phục phản xạ và đá văng quả trứng của ong ra khỏi bụng! Nhưng nếu liều lượng quá mạnh, con gián sẽ chết ngay lập tức và phân hủy thối rữa trước khi ấu trùng ong kịp nở ra để thưởng thức thịt tươi! Độ chuẩn xác tuyệt đối đến từng nano gam nọc độc này là một kiệt tác vi sinh hóa học mà loài người còn lâu mới bắt kịp!
```
**Part 7** → `audio/vs/scene06_p7.wav` (631 ký tự) · mood `hao_hung`

```text
Đó là sự tàn nhẫn lạnh lùng nhưng cũng là sự tinh vi cơ học tuyệt đối của tự nhiên: Giữ cho con mồi sống tươi nguyên suốt nhiều tuần lễ mà không cần tủ lạnh bảo quản! Cô ong của chúng ta hôm nay nhập viện không phải vì bị bệnh, mà vì vô tình bay lạc vào phòng mổ bệnh viện qua lỗ thông gió trong khi đang dẫn giải con gián đi tìm tổ! Toàn bộ hệ thống ngòi tiêm và tuyến nọc độc của cô nàng hoạt động hoàn hảo tuyệt đối không tì vết, phản xạ vận động đạt điểm mười trên mười! Các nhà dược lý học hiện đại đang nghiên cứu công thức nọc độc của ong bắp cày ngọc để điều chế các loại thuốc gây mê thần kinh thế hệ mới không gây nghiện!
```
**Part 8** → `audio/vs/scene06_p8.wav` (326 ký tự) · mood `bi_hai`

```text
Thôi được rồi cô nàng phẫu thuật viên tí hon lộng lẫy ơi! Phòng mổ của tôi là nơi cứu người chứ không phải nơi cô mở lò đào tạo thây ma gián nhé! [laughter] Chúng tôi sẽ chuyển cả hai bạn sang Viện Nghiên Cứu Côn Trùng Học Quốc Gia để các nhà thần kinh học tiếp tục học hỏi công thức chế tạo thuốc tê thần kinh từ cô nàng nhé!
```
**Part 9** → `audio/vs/scene06_p9.wav` (183 ký tự) · mood `am_ap`

```text
Hồ sơ Khoa Phẫu Thuật Não hoàn tất xuất sắc! Giờ thì nghe kìa, tiếng máy bơm nước từ Khoa Hồi Sức Đại Dương báo hiệu bể ngâm cá mặt trăng hai tấn đã sẵn sàng! Toàn đội chạy nhanh nào!
```

### scene07 — BỂ NGÂM NƯỚC MUỐI SINH LÝ
*Thẻ chương:* BỘ NÃO BỐN GAM VÀ BA TRĂM TRIỆU TRỨNG

*Badge:* `HỒI SỨC CẤP CỨU` · *mood mặc định:* `nghiem_trang_gia`

**Part 0** → `audio/vs/scene07_p0.wav` (700 ký tự) · mood `nghiem_trang_gia`

```text
Ùng oàng! Bùm! Khối cơ thể khổng lồ hai tấn của chú Cá Mặt Trăng Mola mola được cần cẩu hạ cánh an toàn xuống bể ngâm nước muối sinh lý dung tích năm mươi mét khối! Lực đẩy Ác-si-mét của dòng nước mặn lập tức nâng bổng khối cơ thể nặng ngàn cân lên một cách nhẹ nhàng như một chiếc lá trôi bồng bềnh. Các đường ống sục khí oxy công suất lớn sủi bọt cuồn cuộn quanh các lá mang của chú cá, cung cấp nguồn dưỡng khí dồi dào tức thì. Tôi cùng kíp trực Khoa Hồi Sức Cấp Cứu Đại Dương bước lên cầu quan sát bằng kính chịu lực bắc ngang qua mặt bể để tiến hành thăm khám toàn diện. Nhịp tim của chú cá qua máy theo dõi điện tâm đồ thủy sinh dao động ở mức ba mươi nhịp mỗi phút, vô cùng ổn định và đều đặn!
```
**Part 1** → `audio/vs/scene07_p1.wav` (388 ký tự) · 🎭 cameo `co_tro_ly`

```text
Bác sĩ trưởng khoa ơi em vừa chạy xong bản quét cộng hưởng từ MRI toàn thân cho khối thịt hai tấn này! Em tìm mỏi cả mắt mà không thấy bóng hơi hay bong bóng cá ở đâu cả bác sĩ ơi! Và đây nữa nè: Hộp sọ của nó to bằng chiếc thùng phi mười lít, nhưng bộ não bên trong của nó... trời đất ơi, nó chỉ nhỏ bằng hạt đậu phộng thôi bác sĩ ơi! Có phải máy quét MRI của em bị lỗi kỹ thuật không ạ?
```
**Part 2** → `audio/vs/scene07_p2.wav` (744 ký tự) · mood `don_dap`

```text
[laughter] Máy quét của cô hoàn toàn chính xác tròn trăm phần trăm không hề có một lỗi kỹ thuật nào cô y tá thân mến! Chào mừng toàn thể kíp trực đến với nghịch lý giải phẫu vĩ đại nhất của đại dương bao la: Bệnh nhân sở hữu tỷ lệ não bộ trên trọng lượng cơ thể nhỏ nhất trong toàn bộ giới động vật có xương sống! Một con cá mặt trăng trưởng thành nặng tới hai tấn tròn trĩnh, nhưng toàn bộ khối lượng bộ não của nó chỉ vỏn vẹn đúng... bốn gam! Nghĩa là bộ não của nó chỉ chiếm một phần năm trăm ngàn tổng trọng lượng cơ thể! Nhỏ hơn cả bộ não của một con mèo con hay một chú chuột nhắt tí hon! Thế nhưng với bộ não bốn gam đó, nó vẫn điều khiển thành công cỗ máy sinh học hai tấn vượt qua hàng ngàn hải lý đại dương suốt hàng chục năm ròng rã!
```
**Part 3** → `audio/vs/scene07_p3.wav` (789 ký tự) · mood `hao_hung`

```text
Và tại sao nó lại không hề có bóng hơi để bơi lội như các loài cá thông thường? Bởi vì môi trường kiếm ăn chính của cá mặt trăng là vùng nước sâu tăm tối twilight zone ở độ sâu từ bốn trăm đến tận tám trăm mét dưới đáy biển! Ở độ sâu tám trăm mét, áp suất nước biển lên tới tám mươi át-mốt-phe, thừa sức bóp bẹp rúm bất kỳ chiếc bóng hơi nào trong chớp mắt! Nếu có bóng hơi, cá mặt trăng sẽ không thể lao nhanh từ độ sâu tám trăm mét lên mặt nước mà không bị vỡ nội tạng do giảm áp đột ngột! Vì vậy, tiến hóa đã thay thế toàn bộ bóng khí bằng một lớp sụn xơ gelatin dày tới bảy phân rưỡi nằm ngay dưới lớp da của nó! Lớp mô gelatin kỳ diệu này có tỷ trọng gần như tương đương với nước biển, giúp con cá đạt trạng thái trôi nổi trung tính ở bất kỳ độ sâu nào mà không sợ áp suất nghiền nát!
```
**Part 4** → `audio/vs/scene07_p4.wav` (856 ký tự) · mood `tram_bi_an`

```text
Sau mỗi chuyến lặn sâu tám trăm mét xuống vùng nước băng giá bốn độ C để săn sứa, thân nhiệt của chú cá bị hạ xuống mức báo động nguy hiểm. Đó là lý do tại sao nó phải bơi lên mặt biển, nằm nghiêng hoàn toàn thân hình dẹt hai mét của mình phơi nắng trên mặt nước như một chiếc đĩa bay tắm nắng! Hành vi tắm nắng này giúp hấp thu tối đa năng lượng mặt trời để sưởi ấm lại các thớ cơ và mạch máu bị đông cứng dưới đáy sâu! Đồng thời, khi nằm phơi nắng trên mặt nước, các đàn chim biển và cá nhỏ sẽ bu lại rỉa sạch hơn bốn mươi loài ký sinh trùng bám trên da cho nó như một dịch vụ spa biển khơi miễn phí! Nhịp tim của cá mặt trăng khi lặn sâu chỉ khoảng hai mươi nhịp mỗi phút để tiết kiệm oxy tối đa giữa vùng nước thiếu dưỡng khí! Cơ quan thị giác của nó phát triển vượt trội với đôi mắt to lớn có khả năng nhìn thấu màn đêm đen kịt dưới đáy biển sâu thẳm!
```
**Part 5** → `audio/vs/scene07_p5.wav` (666 ký tự) · mood `hao_hung`

```text
Đặc biệt hơn nữa, hệ thống cơ bắp vây lưng của cá mặt trăng tạo ra một lượng nhiệt nội sinh đáng kể trong quá trình bơi lội liên tục! Mặc dù là loài cá biến nhiệt, nhưng đôi mắt và não bộ của nó được bao bọc bởi một lớp mỡ cách nhiệt đặc biệt giúp giữ ấm cho trung khu thần kinh giữa làn nước buốt giá! Nhờ lớp mỡ cách nhiệt này, thị lực và phản xạ săn sứa của nó dưới độ sâu tám trăm mét chẳng hề bị tê liệt vì giá lạnh! Khi bơi lên mặt nước phơi nắng, dòng máu ấm từ các mạch máu dưới da sẽ được phân phối ngược vào các cơ quan nội tạng bên trong! Đó là một hệ thống sưởi ấm năng lượng mặt trời tuần hoàn tự nhiên hoàn mỹ không tốn một xu tiền điện nào! [laughter]
```
**Part 6** → `audio/vs/scene07_p6.wav` (689 ký tự) · mood `hao_hung`

```text
Chưa hết đâu nhé! Cá mặt trăng cái còn nắm giữ kỷ lục vô địch tuyệt đối về khả năng sinh sản trong toàn bộ vương quốc động vật có xương sống! Mỗi lần sinh sản, một con cá mặt trăng mẹ có thể phóng thích vào đại dương tới ba trăm triệu quả trứng cùng một lúc! Khi mới nở, con non chỉ dài vỏn vẹn hai mi-li-mét, tròn xoe và có gai nhọn bao quanh trông như một chú cá nóc mini tí hon ngộ nghĩnh! Từ một chấm nhỏ hai mi-li-mét đó, nó lớn lên và tăng trọng lượng tới sáu mươi triệu lần để đạt kích thước khổng lồ hai tấn như bệnh nhân đang nằm trước mặt chúng ta! Sự gia tăng kích thước tới sáu mươi triệu lần này là kỷ lục tăng trưởng vĩ đại nhất trong toàn bộ thế giới động vật trên Trái Đất!
```
**Part 7** → `audio/vs/scene07_p7.wav` (538 ký tự) · mood `am_ap`

```text
Chẩn đoán Khoa Hồi Sức Cấp Cứu Đại Dương: Bệnh nhân hoàn toàn khỏe mạnh, nhịp tim ổn định, bộ não bốn gam đang vận hành cỗ máy hai tấn ở hiệu suất tuyệt hảo! Đơn thuốc cho bệnh nhân: Tiếp tục ngâm mình thư giãn trong bể nước muối sinh lý, bổ sung một bữa tiệc sứa biển tươi sống và chuẩn bị xe cẩu đưa anh chàng ra vịnh biển lúc rạng đông! [laughter] Hai giờ bốn mươi phút sáng! Chúng ta đã vượt qua được nửa chặng đường của ca trực đêm kinh hoàng! Toàn đội chuyển ngay sang Khoa Hộp Sọ và Răng Hàm Mặt để xử lý ca bệnh nanh dài đâm trán!
```

### scene08 — NANH DÀI TỰ ĐÂM THỦNG TRÁN
*Thẻ chương:* BỐN CHIẾC NANH CONG BỐN MƯƠI PHÂN

*Badge:* `NHA KHOA DỊ TẬT` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene08_p0.wav` (960 ký tự) · mood `hao_hung`

```text
Mời bệnh nhân số năm bước vào ghế nha khoa chuyên dụng! Một ca bệnh răng hàm mặt dị thường đến mức làm các nha sĩ lành nghề nhất cũng phải toát mồ hôi hột! Đó là Lợn Hươu Babirusa đến từ những cánh rừng nhiệt đới ẩm ướt trên đảo Sulawesi hoang sơ thuộc đất nước Indonesia! Chú lợn rụt rè ngồi lên chiếc ghế nha khoa bọc da êm ái, đưa hai móng trước lên xoa xoa vầng trán nhăn nheo với vẻ mặt đầy lo lắng. Hãy nhìn vào bộ hàm của anh chàng này mà xem! Đây không phải là răng nanh mọc bình thường, mà là một sự nổi loạn giải phẫu hoàn toàn đi ngược lại mọi quy luật tự nhiên! Hai chiếc răng nanh hàm dưới mọc chìa ra ngoài mép môi nhọn hoắt như hai lưỡi gươm ngắn đã đủ làm kẻ thù khiếp vía rồi. Hai chiếc nanh dưới này sắc như dao cạo, dùng để tự vệ và gạt phăng các đòn tấn công của đối thủ trong những cuộc chiến tranh giành lãnh thổ. Không chỉ dùng để tự vệ, chiếc nanh dưới còn là công cụ hữu hiệu để cắt đứt các dây leo dai nhách khi đi xuyên qua rừng rậm!
```
**Part 1** → `audio/vs/scene08_p1.wav` (952 ký tự) · mood `tram_bi_an`

```text
Nhưng điều làm cả giới y học kinh ngạc tột cùng lại nằm ở hai chiếc răng nanh của hàm trên! Thay vì mọc chúc xuống dưới để cắn xé thức ăn như loài lợn rừng hay hổ báo, hai chiếc răng nanh trên này lại mọc ngược hướng lên trời! Khi bắt đầu phát triển ở độ tuổi trưởng thành, chúng đâm xuyên thẳng qua vòm miệng, xuyên thủng lớp da sống mũi của chính con lợn rồi uốn cong ngược về phía sau trán! Chiếc nanh cong vút này có thể đạt chiều dài kỷ lục lên tới bốn mươi xăng-ti-mét, tạo thành một vòng cung hoàn mỹ ngay trước trán hộp sọ! Không hề có men răng bao bọc bên ngoài, chiếc nanh này là ngà răng đặc quánh, tiếp tục mọc dài ra liên tục trong suốt toàn bộ cuộc đời của con vật! Tốc độ mọc của ngà răng có thể đạt vài xăng-ti-mét mỗi năm, đòi hỏi con vật phải có chế độ mài mòn tự nhiên liên tục. Khác với loài voi có ngà mọc từ răng cửa biến tính, ngà của lợn babirusa thực chất là chiếc răng nanh biến dị độc nhất vô nhị trong toàn bộ lớp thú có vú!
```
**Part 2** → `audio/vs/scene08_p2.wav` (797 ký tự) · mood `tram_bi_an`

```text
Và đây là điều thú vị về mặt di truyền học: Hiện tượng nanh mọc xuyên mũi này chỉ xuất hiện duy nhất ở những con đực trưởng thành! Những con lợn cái hoàn toàn không hề có nanh trên mọc ngược, nanh dưới của chúng cũng rất nhỏ và nằm gọn gàng bên trong mép môi! Điều này chứng tỏ cặp nanh trên là một đặc điểm sinh dục thứ cấp đặc trưng, chịu sự điều khiển trực tiếp của nội tiết tố testosterone! Đồng thời, cấu tạo dạ dày của lợn babirusa cũng vô cùng kỳ lạ, chia thành nhiều ngăn phức tạp tương tự loài động vật nhai lại! Nhờ hệ vi sinh vật lên men dạ dày này, lợn babirusa có thể ăn và tiêu hóa được các loại rễ cây rừng chứa nhiều chất xơ dai và độc tố tự nhiên! Để bảo vệ mô mềm quanh sống mũi khỏi bị nhiễm trùng, con lợn thường xuyên đầm mình trong bùn khoáng núi lửa chứa lưu huỳnh tự nhiên!
```
**Part 3** → `audio/vs/scene08_p3.wav` (349 ký tự) · 🎭 cameo `co_tro_ly`

```text
Bác sĩ trưởng khoa ơi em chụp cắt lớp vi tính hộp sọ cho nó mà hai tay em run bần bật! Đầu nhọn của cái nanh hàm trên nó cong sát sạt vào xương trán rồi! Chỉ cần nó gật đầu mạnh một cái là cái nanh tự cắm phập vào hộp sọ tự sát mất thôi bác sĩ ơi! Em có nên chuẩn bị một chiếc cưa nha khoa cầm tay để cưa bớt hai phân chóp nanh ngay bây giờ không ạ?
```
**Part 4** → `audio/vs/scene08_p4.wav` (981 ký tự) · mood `don_dap`

```text
Mối lo ngại của cô y tá hoàn toàn có cơ sở khoa học đàng hoàng! Nghiên cứu của nhà nhân chủng học Colin Groves đã ghi nhận những trường hợp cá biệt ngoài tự nhiên: Ở những con lợn hươu đực sống quá thọ trong điều kiện nuôi nhốt hoặc hoang dã, răng nanh của chúng không ngừng mọc dài ra mỗi ngày. Nếu độ cong của nanh quá hẹp, chóp nanh sắc nhọn có thể chạm vào xương trán, chèn ép mô sọ và thậm chí xuyên thủng hộp sọ gây tổn thương não bộ nghiêm trọng! Đó là lý do nhiều nhà khoa học thế kỷ trước từng gọi loài lợn này là sinh vật sở hữu vũ khí tự sát ngớ ngẩn nhất của tự nhiên! Tuy nhiên những trường hợp tự đâm thủng sọ não đó vô cùng hiếm gặp trong tự nhiên hoang dã! Trong môi trường rừng nguyên sinh, những cú cọ xát đầu vào thân cây gỗ mun và các cuộc giao đấu liên tục sẽ tự nhiên mài mòn và làm cùn đầu nhọn của chiếc nanh! Nghiên cứu của giáo sư Macdonald còn chỉ ra rằng lớp da quanh chân nanh của lợn babirusa ôm khít lấy thân ngà như một chiếc gioăng cao su sinh học!
```
**Part 5** → `audio/vs/scene08_p5.wav` (977 ký tự) · mood `hao_hung`

```text
Vậy tại sao tiến hóa lại ban tặng cho loài lợn này một bộ răng nanh nguy hiểm đến mức độ như thế này? Câu trả lời nằm ở quy luật chọn lọc giới tính khốc liệt suốt hàng triệu năm qua! Các nghiên cứu thực địa gần đây đã chứng minh: lợn babirusa không hề dùng nanh trên để cắn hay đào bới thức ăn dưới đất! Khi hai con đực giao đấu giành bạn tình, chúng đứng thẳng bằng hai chân sau như hai võ sĩ quyền anh, dùng mõm tì đè và gạt đòn của đối phương! Cặp nanh cong vút trên mặt đóng vai trò như một chiếc khiên chắn bảo vệ đôi mắt và cổ họng của con đực trước những cú cắn hiểm ác của đối thủ! Đồng thời, con đực nào sở hữu cặp nanh dài và cong hoàn mỹ nhất sẽ chứng minh cho con cái thấy nó có bộ gen kiên cường và sức sống bền bỉ phi thường! Nó giống như chiếc đuôi xòe lộng lẫy của chim công hay cặp sừng đồ sộ của loài hươu đực vậy! Càng sở hữu cặp nanh đối xứng và uốn cong chuẩn mực, con đực càng khẳng định được sức khỏe dẻo dai và khả năng sinh sản vượt trội trong bầy đàn!
```
**Part 6** → `audio/vs/scene08_p6.wav` (700 ký tự) · mood `am_ap`

```text
[laughter] May mắn thay cho bệnh nhân của chúng ta hôm nay: chóp nanh vẫn cách xương trán tận hai xăng-ti-mét rưỡi, hoàn toàn an toàn và chưa cần phải mài bớt một mi-li-mét nào! Chẩn đoán của Phòng Cấp Cứu Tạo Hóa: Hàm răng kỳ dị nhưng là biểu tượng kiêu hãnh của tình yêu và lòng dũng cảm thảo nguyên nhiệt đới! Tôi chỉ cần vệ sinh sạch sẽ vùng chân răng xuyên qua sống mũi và bôi một lớp thuốc sát trùng nhẹ là anh chàng có thể tự tin đi tìm bạn gái được rồi! Anh bạn lợn hươu hãy nhớ thường xuyên đầm mình trong bùn khoáng để sát trùng tự nhiên cho hai bên sống mũi nhé! Hồ sơ Khoa Nha Khoa Dị Tật hoàn tất mỹ mãn! Giờ thì nghe kìa, tiếng la hét ngoài sảnh báo hiệu đợt náo loạn thứ hai vừa nổ ra!
```

### scene09 — BA MƯƠI NGÀN MŨI KIM TIÊM
*Thẻ chương:* NHÍM LÔNG NHỌN RẢI CHÔNG HÀNH LANG

*Badge:* `PHÒNG CHỜ NÁO LOẠN` · *mood mặc định:* `bi_hai`

**Part 0** → `audio/vs/scene09_p0.wav` (924 ký tự) · mood `bi_hai`

```text
[sigh] Ba giờ ba mươi phút sáng. Cơn buồn ngủ bắt đầu kéo sụp hai mí mắt của tôi xuống, thì một tiếng thét thất thanh lại vang lên từ phía cuối hành lang! Tôi giật bắn mình đánh rơi chiếc bút bi xuống bàn, vội vàng đứng bật dậy chạy ra ngoài xem chuyện gì vừa xảy ra. Ái da da! Đau điếng người thế này! Cứu em với bác sĩ ơi! Có ai vừa rải một bãi chông sắt khắp sàn nhà hành lang bệnh viện thế này! Cô y tá vừa ôm một bên chân vừa nhảy lò cò trên một chân còn lại, khuôn mặt mếu máo đau đớn như vừa dẫm phải bẫy chông thời cổ đại! Thủ phạm của vụ rải chông liên hoàn này không ai khác chính là chú Nhím Lông Nhọn Bắc Mỹ béo tròn đang lững thững đi dạo cạnh các dãy ghế! Chú nhím vừa đi vừa cọ cọ chiếc lưng béo ú vào mép tường bê tông, làm rụng lả tả hàng chục chiếc gai nhọn cắm phập xuống sàn gạch men! Các bệnh nhân khác xung quanh hoảng hốt nhảy tót lên ghế băng, co chân lên cao để tránh bãi mìn sinh học đang lan rộng!
```
**Part 1** → `audio/vs/scene09_p1.wav` (973 ký tự) · mood `don_dap`

```text
Đứng yên! Tất cả nhân viên và bệnh nhân trong sảnh đứng yên tại chỗ không được bước thêm một bước nào! Tôi lập tức bật chiếc đèn pin y tế công suất lớn quét dọc mặt sàn, rọi sáng một bãi mìn sinh học dày đặc trải dài từ quầy thuốc tới cửa phòng khám! Mọi người nghe cho rõ đây: Tuyệt đối không ai được dùng tay không để nhổ những chiếc gai này ra khỏi da thịt hay đế giày! Nhiều người xem phim hoạt hình thường lầm tưởng rằng nhím có khả năng co cơ phóng gai bay vèo vèo như tên bắn về phía kẻ thù. Điều đó hoàn toàn sai sự thật tròn trăm phần trăm! Nhím không hề có bất kỳ bó cơ nào có thể bắn gai ra ngoài không gian! Nhưng cơ chế tháo rời lông gai thụ động của nó thì tinh vi và nguy hiểm hơn súng đạn gấp trăm lần! Trước khi rụng gai, con nhím thường phát ra những tiếng nghiến răng ken két như tiếng cảnh báo gầm gừ để xua đuổi đối thủ! Cú quất đuôi của nhím có thể đạt vận tốc tới hai mươi mét mỗi giây, cắm phập hàng chục mũi chông vào mõm kẻ săn mồi trong chớp mắt!
```
**Part 2** → `audio/vs/scene09_p2.wav` (1071 ký tự) · mood `tram_bi_an`

```text
Gốc nang lông của chiếc gai gắn vào lớp da con nhím vô cùng lỏng lẻo, chỉ cần một va quẹt nhẹ như một cái phẩy tay là chiếc gai tự động rụng ra ngay lập tức. Toàn bộ cơ thể của một con nhím lông nhọn Bắc Mỹ trưởng thành được bao bọc bởi hơn ba mươi ngàn chiếc lông gai sắc nhọn! Mỗi chiếc gai thực chất là một sợi lông biến tính rỗng ruột bên trong, cực kỳ nhẹ nhưng lại cứng cáp phi thường nhờ cấu trúc vách xốp tổ ong. Nhờ cấu trúc rỗng xốp chứa đầy không khí này, hàng chục ngàn chiếc gai còn đóng vai trò như một chiếc áo phao cứu sinh tự nhiên hoàn hảo! Khi gặp lũ quét rừng hay cần vượt sông tìm thức ăn, con nhím có thể bơi qua những khúc sông rộng mà không sợ bị chìm nghỉm! Và đây là bí mật khủng khiếp nhất khiến các bác sĩ ngoại khoa phải rùng mình kinh hãi: Cấu trúc vi cơ học ở phần chóp nhọn của mỗi chiếc gai! Ở phần đầu của mỗi chiếc gai có chứa tới bảy trăm đến tám trăm chiếc vi ngạnh ngược siêu nhỏ xếp tầng tầng lớp lớp như vảy cá mập! Những chiếc vi ngạnh này nhỏ đến mức mắt thường không thể nhìn thấy, nhưng chúng sắc bén vô song và cực kỳ dẻo dai!
```
**Part 3** → `audio/vs/scene09_p3.wav` (824 ký tự) · mood `don_dap`

```text
Nghiên cứu của tiến sĩ Cho công bố trên tạp chí Viện Hàn Lâm Khoa Học Hoa Kỳ PNAS đã đo đạc chính xác lực tác động cơ học này: Khi đâm vào da thịt, các vi ngạnh ngược này nằm ép sát xuôi chiều vào thân gai, giúp giảm tới năm mươi tư phần trăm lực đâm so với kim tiêm y tế thông thường! Nhờ đó, chiếc gai có thể xuyên ngọt lịm qua lớp da thịt dày cộp của kẻ thù chỉ bằng một cú quẫy đuôi nhẹ nhàng! Nhưng một khi đã cắm sâu vào trong cơ thịt, các vi ngạnh này lập tức hút ẩm từ dịch mô cơ thể rồi xòe bung ra như những chiếc mỏ neo mini! Lực cần thiết để rút chiếc gai ra tăng vọt lên gấp ba lần so với lực đâm vào, gây đau đớn dữ dội và xé rách các mô xung quanh nếu cố giật mạnh bằng tay! Chất keratin ở chóp gai khi ngậm nước mô còn trương nở nhẹ, khiến độ bám dính của các ngạnh ngược càng thêm chắc chắn và khó tách rời!
```
**Part 4** → `audio/vs/scene09_p4.wav` (791 ký tự) · mood `hao_hung`

```text
Thậm chí, nếu không được gắp ra đúng kỹ thuật ngoại khoa, sự co bóp tự nhiên của các thớ cơ sẽ khiến chiếc gai tự động di chuyển sâu hơn vào trong cơ thể mỗi ngày vài mi-li-mét! Đã từng có những con gấu hay báo sư tử bị gai nhím cắm vào mõm, chiếc gai tự trườn xuyên qua má, đâm vào mạch máu lớn hoặc mắt gây tử vong thương tâm! Nên cô y tá hãy ngồi yên trên ghế để tôi dùng kìm kẹp y tế chuyên dụng xoay nhẹ góc bốn mươi lăm độ rồi rút dứt khoát theo trục thẳng đứng nhé! Thao tác xoay nhẹ góc bốn mươi lăm độ này giúp các vi ngạnh ngược uốn cong mềm mại theo thớ cơ, giải phóng lực móc neo mà không làm rách mô tế bào! Tách! Chiếc gai cuối cùng đã được đưa vào khay nhôm vô trùng. Sảnh phòng chờ của Phòng Cấp Cứu Tạo Hóa thở phào nhẹ nhõm như vừa vượt qua một bãi mìn sinh học! [laughter]
```
**Part 5** → `audio/vs/scene09_p5.wav` (554 ký tự) · mood `am_ap`

```text
Được rồi anh bạn nhím béo tròn, mời anh vào phòng khám Khoa Da Liễu ngay để kiểm tra xem lớp kháng sinh tự nhiên trên lưng anh còn đủ dùng không nhé! Tôi yêu cầu chú nhím phải đi theo đường kẻ vạch cách ly màu vàng để không làm rụng gai thêm một lần nào nữa! Bốn chiếc bàn chân bọc gai thịt xù xì của chú nhím bước đi lẹp xẹp ngoan ngoãn theo sau lưng bác sĩ, không dám cọ lưng vào tường thêm một lần nào! Ca trực đêm vẫn còn hai chuyên khoa hóc búa nhất đang chờ đón: Khoa Tuần Hoàn Áp Suất Cao và Khoa Rối Loạn Hành Vi! Toàn đội tiếp tục chiến đấu nào!
```

### scene10 — HUYẾT ÁP TÂM THU HAI TRĂM TÁM
*Thẻ chương:* TRÁI TIM MƯỜI MỘT CÂN VÀ LƯỚI MẠCH SỌ

*Badge:* `TUẦN HOÀN CAO ÁP` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene10_p0.wav` (763 ký tự) · mood `don_dap`

```text
Bíp! Bíp! Bíp! Tiếng còi báo động quá tải áp suất từ chiếc máy đo huyết áp kỹ thuật số vang lên dồn dập ngay khi chúng tôi bước vào phòng khám tuần hoàn! Bệnh nhân số bảy của chúng ta đang đứng gục đầu bên cửa sổ: Quý cô Hươu Cao Cổ cao tới năm mét, chiếc cổ dài hai mét buông thõng vẻ mệt mỏi rã rời! Chỉ số huyết áp hiển thị trên màn hình điện tử làm toàn thể các bác sĩ tim mạch phải lạnh gáy kinh hoàng: Hai trăm tám mươi trên một trăm tám mươi mi-li-mét thủy ngân! Mức huyết áp tâm thu lên tới hai trăm tám mươi mi-li-mét thủy ngân! Cao gấp hơn hai lần chỉ số huyết áp bình thường của một người trưởng thành khỏe mạnh! Ở một người bình thường, mức huyết áp khủng khiếp này sẽ làm vỡ tan các mạch máu não, gây xuất huyết não và tử vong tức thì trong vài phút!
```
**Part 1** → `audio/vs/scene10_p1.wav` (500 ký tự) · mood `tram_bi_an`

```text
Thế nhưng quý cô hươu cao cổ của chúng ta vẫn đứng vững vàng, chỉ hơi hoa mắt và chóng mặt nhẹ sau khi vừa cúi gập người xuống uống nước suối bên ngoài sảnh! Nhịp tim của bệnh nhân đập mạnh đến mức tôi có thể nhìn thấy từng đợt sóng máu dâng lên cuồn cuộn dọc theo tĩnh mạch cổ dài hai mét! Bác sĩ ơi, có phải cô hươu này bị cơn bão tăng huyết áp kịch phát ác tính không ạ? Em có nên tiêm ngay một liều thuốc chẹn kênh canxi liều cao để hạ huyết áp của cô ấy xuống mức một trăm hai mươi không bác sĩ?
```
**Part 2** → `audio/vs/scene10_p2.wav` (415 ký tự) · 🎭 cameo `co_tro_ly`

```text
Bác sĩ trưởng khoa ơi nếu cô ấy cúi đầu xuống uống nước một lần nữa thì huyết áp có dồn lên làm nổ tung não bộ của cô ấy không ạ? Nhìn chiếc cổ dài hai mét ngoằn ngoèo kia mà em tưởng tượng như một đường ống dẫn dầu cao áp xuyên lục địa vậy bác sĩ ơi! Và còn một điều kỳ lạ nữa bác sĩ ơi: Dây thần kinh điều khiển thanh quản của cô ấy dài tới bốn mét rưỡi lận đó bác sĩ, sao tiến hóa lại đi đường vòng xa xôi thế ạ?
```
**Part 3** → `audio/vs/scene10_p3.wav` (833 ký tự) · mood `hao_hung`

```text
Tuyệt đối cấm tiêm thuốc hạ áp cô y tá nhé! Nếu hạ huyết áp của cô ấy xuống một trăm hai mươi thì cô ấy sẽ đột tử vì thiếu máu não ngay lập tức đấy! Đây là mức huyết áp hoàn toàn bình thường và bắt buộc phải có để duy trì sự sống cho sinh vật cao nhất trên cạn này! Hãy làm một bài toán vật lý thủy tĩnh đơn giản mà bất kỳ kỹ sư nào cũng phải thán phục: Trái tim của hươu cao cổ nằm cách bộ não ở trên đỉnh đầu một khoảng cách xa tới hai mét theo phương thẳng đứng! Để bơm được máu thắng được trọng lực Trái Đất và đẩy dòng máu lên tới đỉnh đầu với áp lực tưới máu não đủ một trăm mi-li-mét thủy ngân, trái tim bắt buộc phải tạo ra một áp suất bơm tại gốc lên tới hai trăm tám mươi! Nếu huyết áp hạ xuống một trăm hai mươi như người, áp lực cột nước sẽ khiến dòng máu không thể leo lên tới hộp sọ, làm con vật ngất xỉu ngay tức khắc!
```
**Part 4** → `audio/vs/scene10_p4.wav` (731 ký tự) · mood `don_dap`

```text
Để thực hiện được kỳ tích thủy lực đó, tạo hóa đã trang bị cho hươu cao cổ một trái tim quái vật nặng tới mười một ki-lô-gam! Thành tâm thất trái của nó dày tới bảy xăng-ti-mét rưỡi, dày gấp ba lần tâm thất người, tạo ra lực bóp mạnh như một chiếc máy bơm piston công nghiệp! Thế nhưng câu hỏi hóc búa nhất mà giới sinh lý học từng đau đầu là: Khi hươu cao cổ cúi gập đầu xuống đất uống nước, điều gì ngăn dòng máu áp suất cực đại đó tràn xuống làm nổ tung các mạch máu não? Bởi vì khi cúi đầu, trọng lực sẽ cộng dồn với áp lực bơm tim, đẩy áp suất máu tại não vọt lên hơn bốn trăm mi-li-mét thủy ngân trong tích tắc! Và khi đứng thẳng dậy đột ngột, áp lực máu lại tụt dốc không phanh, đe dọa gây thiếu máu não cục bộ nghiêm trọng!
```
**Part 5** → `audio/vs/scene10_p5.wav` (992 ký tự) · mood `tram_bi_an`

```text
Câu trả lời nằm ở một tuyệt tác vi mạch sinh học tại đáy hộp sọ mang tên: Mạng lưới mạch kỳ diệu Rete mirabile! Ngay trước khi dòng máu đi vào não bộ, động mạch cảnh phân nhánh thành hàng ngàn tiểu động mạch đàn hồi đan xen chằng chịt như một miếng bọt biển sinh học. Mạng lưới này hoạt động chính xác như một bể giảm áp thủy lực, hấp thu và triệt tiêu toàn bộ sóng áp suất cao đột ngột khi con vật cúi đầu! Đồng thời, trong các tĩnh mạch cảnh dài hai mét ở cổ có chứa hàng loạt van một chiều đóng kín lại, ngăn không cho máu tĩnh mạch chảy ngược về não bộ! Và ở phần chân dưới, lớp da dày cộp và các cân cơ siết chặt hoạt động y hệt như bộ đồ bay chống quá tải trọng trường G-suit của các phi công chiến đấu phản lực! Nhờ lớp da chân bó chặt này, áp lực máu cao không thể làm vỡ mao mạch hay gây phù nề chân dù con vật đứng liên tục suốt cả ngày đêm! Cơ quan Hàng Không Vũ Trụ Hoa Kỳ NASA đã nghiên cứu cấu trúc da chân này để chế tạo trang phục kháng áp cho các phi hành gia bay vào vũ trụ!
```
**Part 6** → `audio/vs/scene10_p6.wav` (625 ký tự) · mood `tram_bi_an`

```text
Và về câu hỏi của cô y tá về dây thần kinh thanh quản quặt ngược dài bốn mét rưỡi: đó chính là dấu tích tiến hóa kinh điển từ tổ tiên loài cá cổ đại! Khi cổ của loài hươu ngày càng vươn dài ra qua hàng triệu năm, dây thần kinh bị quai động mạch chủ níu giữ nên phải kéo dài theo thành một vòng lặp ngoạn mục dài bốn mét rưỡi! Hơn nữa, vì phải luôn cảnh giác trước các loài thú săn mồi và duy trì áp suất tuần hoàn phức tạp, hươu cao cổ chỉ ngủ chợp mắt khoảng ba mươi phút mỗi ngày! Những giấc ngủ ngắn ngủi kéo dài từ năm đến mười phút chia làm nhiều lần trong ngày giúp nó vừa phục hồi năng lượng vừa giữ an toàn tuyệt đối!
```
**Part 7** → `audio/vs/scene10_p7.wav` (610 ký tự) · mood `am_ap`

```text
Chẩn đoán Khoa Tuần Hoàn Áp Suất Cao của Phòng Cấp Cứu Tạo Hóa: Bệnh nhân sở hữu hệ thống thủy lực tuần hoàn hoàn hảo nhất thế giới động vật! Đơn thuốc cho bệnh nhân: Một bó cành lá keo tươi non gắn trên giá treo cao ba mét và dặn bệnh nhân mỗi lần cúi đầu uống nước thì nhớ đứng dạng chân chậm rãi thôi nhé! [laughter] Chiếc lưỡi dài màu xanh đen chứa đầy sắc tố melanin giúp bảo vệ mô lưỡi không bị cháy nắng khi vươn lên đón lá cây giữa trời nắng gắt! Bốn giờ sáng! Chỉ còn một tiếng nữa là đến giờ giao ban bình minh! Chúng ta chuyển ngay sang Khoa Da Liễu để kiểm tra vết thương của chú nhím béo tròn nào!
```

### scene11 — KHÁNG SINH TỰ NHIÊN TRÊN GAI
*Thẻ chương:* VI NGẠNH NGƯỢC VÀ LỚP MỠ TỰ CHỮA

*Badge:* `KHOA DA LIỄU` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene11_p0.wav` (1100 ký tự) · mood `hao_hung`

```text
Bệnh nhân số tám, mời bước vào phòng khám Khoa Da Liễu và Dị Hóa Sinh! Chú Nhím Lông Nhọn béo tròn đang chầm chậm bước vào với mùi tinh dầu thông ngào ngạt! Tôi nhìn chú nhím đang ngơ ngác ngồi giữa phòng khám mà vừa thương vừa buồn cười trước sự vụng về của loài động vật này. Các đồng nghiệp có biết một nghịch lý trớ trêu nhất trong đời sống của loài nhím lông nhọn Bắc Mỹ là gì không? Trong khi cả khu rừng và cả phòng cấp cứu ai cũng khiếp sợ ba mươi ngàn chiếc gai sắc nhọn trên lưng nó, thì bản thân con nhím lại là kẻ ngã cây nhiều nhất trong vương quốc động vật! [laughter] Nhím lông nhọn Bắc Mỹ là một loài gặm nhấm rất thích ăn vỏ cây thông, vỏ cây bạch dương và chồi non ngọt ngào trên các ngọn cây cao. Thế nhưng thân hình nó thì béo múp míp, bốn chân ngắn ngủn và không hề có đuôi cuốn linh hoạt như loài khỉ hay sóc! Khi mải mê vươn người ra những cành cây nhỏ ngoài rìa tán lá để gặm chồi non, những cú trượt chân tai hại thường xuyên khiến con nhím rơi tự do từ độ cao mười mét xuống đất! Cú va chạm mạnh vào đá sỏi hay rễ cây làm gãy vụn hàng chục sợi gai bảo vệ quanh sườn con vật!
```
**Part 1** → `audio/vs/scene11_p1.wav` (777 ký tự) · mood `tram_bi_an`

```text
Và khi rơi xuống mặt đất cứng ngắc từ độ cao của một tòa nhà ba tầng, điều không thể tránh khỏi là: Hàng chục chiếc gai sắc nhọn trên lưng nó sẽ bị gãy vụn và cắm phập ngược vào chính các thớ cơ thịt ở đùi, bụng và chân của con nhím! Các bạn hãy nhớ lại xem: những chiếc gai này chứa hàng trăm vi ngạnh ngược siêu nhỏ, găm chặt vào thớ thịt và cực kỳ khó rút ra ngoài! Nếu là một con thú săn mồi bị dính gai nhím, vết thương sẽ nhanh chóng bị nhiễm trùng, mưng mủ hoại tử và thậm chí dẫn tới cái chết đau đớn. Vậy tại sao với hàng ngàn chiếc gai tự đâm vào thịt mình sau mỗi cú ngã cây như vậy, loài nhím lại không bao giờ bị nhiễm trùng máu hay chết vì hoại tử? Thậm chí các vết đâm tự thân này còn lành lặn thần tốc chỉ sau vài ngày mà không để lại bất kỳ di chứng áp xe nào!
```
**Part 2** → `audio/vs/scene11_p2.wav` (1081 ký tự) · mood `don_dap`

```text
Công trình nghiên cứu kinh điển của giáo sư Uldis Roze về loài nhím Bắc Mỹ đã làm sáng tỏ một cơ chế dược lý phi thường: Toàn bộ bề mặt ngoài của ba mươi ngàn chiếc lông gai nhím được bao phủ bởi một lớp màng chất béo mỏng chứa đầy các axit béo tự do có tính kháng sinh cực mạnh! Các axit béo này bao gồm axit butyric, axit hexanoic và nhiều hợp chất lipid tự nhiên có khả năng diệt khuẩn phổ rộng. Chúng có khả năng tiêu diệt và ức chế sự phát triển của hầu hết các loài vi khuẩn Gram dương, đặc biệt là vi khuẩn tụ cầu vàng Staphylococcus aureus cực kỳ nguy hiểm! Đây thực chất là một lớp kem bôi kháng sinh tự nhiên mà tạo hóa đã hào phóng bôi sẵn lên từng chiếc mũi kim tiêm trên lưng con nhím! Mỗi khi con nhím trượt chân ngã cây và tự đâm trúng gai của chính mình, lớp kháng sinh này sẽ lập tức khử trùng vết thương ngay tại chỗ! Nó hoạt động như một hệ thống an toàn tự động, đảm bảo rằng nếu vũ khí tự vệ phản chủ thì chủ nhân của nó vẫn hoàn toàn bình an vô sự! Lớp sáp mỡ này được tiết ra liên tục từ các tuyến bã nhờn chuyên biệt nằm ngay cạnh nang lông dưới lớp da dày!
```
**Part 3** → `audio/vs/scene11_p3.wav` (732 ký tự) · mood `hao_hung`

```text
Chưa hết đâu nhé! Lớp mỡ kháng sinh này còn phát tán một mùi hương hăng nồng đặc trưng vào không khí mỗi khi nhím dựng đứng các sợi gai lên cảnh cáo kẻ thù! Đó là lời nhắn nhủ rõ ràng của tự nhiên gửi tới các loài săn mồi: Tránh xa ra! Ở đây có ba mươi ngàn mũi kim tiêm tẩm thuốc tê và kháng sinh sẵn sàng phục vụ các bạn đấy! [laughter] Tôi đã lấy mẫu chất béo trên lưng bệnh nhân để nuôi cấy vi sinh vật trong đĩa thạch thí nghiệm suốt hai mươi tư giờ qua. Và kết quả thu được hoàn toàn vô trùng tròn trăm phần trăm! Không có một khóm vi khuẩn gây hại nào có thể sống sót trên bộ lông gai này! Vòng vô khuẩn xung quanh mẫu gai nhím trên đĩa thạch thậm chí còn rộng hơn cả vòng ức chế của thuốc kháng sinh penicillin thông thường!
```
**Part 4** → `audio/vs/scene11_p4.wav` (0 ký tự) · mood `tram_bi_an`

```text

```
**Part 5** → `audio/vs/scene11_p5.wav` (745 ký tự) · mood `tram_bi_an`

```text
Các nhà nghiên cứu còn thử nghiệm với các chủng vi nấm gây bệnh ngoài da cứng đầu nhất như nấm mốc sợi và nấm men candida. Và kết quả thật đáng kinh ngạc: Lớp axit béo tự nhiên trên gai nhím ức chế tới chín mươi chín phần trăm sự phát triển của các bào tử nấm mốc! Điều này lý giải tại sao dù sống ở những vùng đầm lầy ẩm ướt hay rừng rậm nhiệt đới ẩm thấp, da của loài nhím không bao giờ bị viêm da hay nấm ngứa! Nó sở hữu một hệ sinh thái da hoàn toàn tự cân bằng và tự kháng khuẩn độc nhất vô nhị trong lớp động vật có vú! Lớp sáp kháng sinh này thậm chí còn không bị rửa trôi bởi nước mưa hay băng tuyết suốt cả mùa đông lạnh giá! Thật là một phòng thí nghiệm dược phẩm di động hoàn mỹ được tích hợp ngay trên lưng một chú gặm nhấm béo tròn!
```
**Part 6** → `audio/vs/scene11_p6.wav` (544 ký tự) · mood `am_ap`

```text
Chẩn đoán Khoa Da Liễu của Phòng Cấp Cứu Tạo Hóa: Bệnh nhân sở hữu nhà máy sản xuất thuốc mỡ kháng sinh xịn nhất thế giới động vật! Cho phép xuất viện! Nhưng dặn bệnh nhân lần sau leo trèo hái quả thì nhớ thắt dây an toàn cẩn thận nhé, ngã hoài làm bệnh viện tốn bông băng lắm đấy! [laughter] Anh bạn nhím hãy nhớ rằng kháng sinh dù xịn đến mấy cũng không thể chữa lành bệnh lười đeo dây an toàn đâu nhé! Giờ thì chuyển ngay sang phòng khám cuối cùng: Khoa Tâm Thần và Rối Loạn Hành Vi! Bệnh nhân số chín đang đứng như tượng đá ngoài hành lang!
```

### scene12 — TƯỢNG ĐÁ BIẾT XẢ SÚNG
*Thẻ chương:* TIẾNG GÕ MỎ MỘT TRĂM MƯỜI LĂM ĐB

*Badge:* `TÂM THẦN HỌC` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene12_p0.wav` (802 ký tự) · mood `tram_bi_an`

```text
Bốn giờ ba mươi phút sáng. Căn phòng khám Khoa Tâm Thần và Rối Loạn Hành Vi chìm trong bầu không khí yên ắng đến rợn người. Bên ngoài cửa sổ, những cơn gió lạnh rít nhẹ qua khe kính, chỉ có tiếng kim đồng hồ tíc tắc gõ nhịp chậm rãi giữa căn phòng tĩnh mịch. Bệnh nhân số chín: Cò Mỏ Giày, sinh vật thời tiền sử còn sót lại giữa những đầm lầy hoang sơ miền Trung châu Phi xa xôi. Từ lúc nhập viện lúc mười hai giờ đêm cho tới tận thời điểm này, bệnh nhân này không hề nhấc chân lên một lần nào! Hai mắt màu vàng nhạt nhìn trừng trừng vào một điểm vô định trên tường, mi mắt hoàn toàn không chớp, nhịp thở chậm đến mức mắt thường không thể nhận biết được! Chiếc mỏ guốc khổng lồ chúc xuống góc bốn mươi lăm độ, toát ra một vẻ mặt nghiêm nghị và đăm chiêu như một triết gia cổ đại đang trầm tư mặc tưởng.
```
**Part 1** → `audio/vs/scene12_p1.wav` (0 ký tự) · mood `bi_hai`

```text

```
**Part 2** → `audio/vs/scene12_p2.wav` (439 ký tự) · 🎭 cameo `co_tro_ly`

```text
Bác sĩ trưởng khoa ơi em mang hồ sơ vào mà hai hàm răng em va vào nhau lập cập! Có phải con chim khổng lồ này bị trầm cảm phân liệt giai đoạn cuối hay bị đông cứng cơ thể kiểu mèo liệt cứng không bác sĩ? Nó cứ nhìn em trừng trừng từ nửa đêm đến giờ, em cảm giác như linh hồn mình sắp bị chiếc mỏ kia nuốt chửng mất rồi bác sĩ ơi! Và chân cẳng của nó trắng phau như quét vôi thế kia có phải bị nấm da hoại tử giai đoạn nặng không bác sĩ ơi?
```
**Part 3** → `audio/vs/scene12_p3.wav` (783 ký tự) · mood `don_dap`

```text
Không hề có chứng liệt cứng hay trầm cảm nào ở đây cả cô y tá thân mến! Đây chính là trạng thái thiền định săn mồi đỉnh cao của kẻ phục kích kiên nhẫn nhất thế giới tự nhiên hoang dã! Vệt trắng trên chân nó thực chất là thói quen xả nước tiểu làm mát chân độc đáo mang tên urohidrosis! Nước bay hơi sẽ làm mát các mạch máu ở chân, giúp nó duy trì thân nhiệt ổn định giữa những đầm lầy châu Phi nóng tới bốn mươi độ C! Và khi tôi vừa bước tới trước mặt nó cách nửa mét... Cạch! Cạch! Cạch! Tách tách tách tách tách! Tiếng va đập của hai hàm mỏ guốc khổng lồ vang lên rầm rầm như một khẩu súng máy liên thanh đang xả đạn liên hồi giữa chiến hào! [laughter] Chuỗi âm thanh kim loại đanh thép xé toạc bầu không khí yên tĩnh, làm rung rinh cả những chiếc chai lọ thủy tinh trên giá thuốc!
```
**Part 4** → `audio/vs/scene12_p4.wav` (733 ký tự) · mood `tram_bi_an`

```text
Đó chính là nghi thức gõ mỏ bill-clattering độc nhất vô nhị của loài cò mỏ giày! Nghiên cứu của tiến sĩ Tomita công bố trên Tạp Chí Tập Tính Học Động Vật đã đo được: Cường độ âm thanh của tràng gõ mỏ này có thể đạt ngưỡng lên tới một trăm mười lăm đê-xi-ben! Ngang ngửa với tiếng còi xe cứu thương hụ còi ở cự ly gần! Tiếng gõ mỏ đanh thép này có thể truyền xa hàng cây số qua những thảm cói đầm lầy rậm rạp, dùng để chào hỏi bạn tình và xua đuổi các đối thủ xâm phạm lãnh thổ! Chiếc mỏ khổng lồ dài tới hai mươi tư xăng-ti-mét của nó kết thúc bằng một chiếc móc câu sắc lẹm như mũi mác thép! Khi kẹp chặt lại, lực ép cơ hàm của nó thừa sức nghiền nát lớp vảy giáp cứng như đá của loài cá phổi châu Phi và rùa đầm lầy trong nháy mắt!
```
**Part 5** → `audio/vs/scene12_p5.wav` (301 ký tự) · mood `hao_hung`

```text
Đôi mắt của nó có màng chớp trong suốt nhắm lại theo chiều ngang trong đúng một phần nghìn giây khi tấn công con mồi dưới bùn lầy để bảo vệ giác mạc! Bàn chân khổng lồ của nó có sải ngón dài tới ba mươi xăng-ti-mét, phân tán áp lực giúp con chim bước đi thanh thoát trên thảm bèo nổi mà không bị chìm!
```
**Part 6** → `audio/vs/scene12_p6.wav` (848 ký tự) · mood `bi_hai`

```text
[sigh] Nhưng phía sau sự kiên nhẫn và uy lực đáng sợ đó là một hiện tượng sinh học khốc liệt làm xót xa lòng người: Hiện tượng sát hại con thứ Cainism! Nghiên cứu thực địa của Mullers và Amar trên Tạp Chí Điểu Học The Ostrich đã ghi nhận: Cò mỏ giày mẹ thường đẻ hai quả trứng trong mỗi mùa sinh sản để dự phòng trường hợp quả trứng đầu tiên bị hỏng hoặc con non bị chết yểu. Thế nhưng nguồn thức ăn ở các đầm lầy nhiệt đới luôn biến động vô cùng khan hiếm, chim bố mẹ chỉ đủ sức kiếm mồi nuôi sống một đứa con duy nhất. Con non đầu lòng to lớn hơn sẽ liên tục dùng chiếc mỏ nhọn mổ và xua đuổi đứa em nhỏ yếu ớt ra khỏi tổ cho tới khi con thứ chết đói trong sự bất lực của chim mẹ! Đó là sự tàn nhẫn đến lạnh lùng của quy luật chọn lọc tự nhiên: thà bảo toàn một cá thể khỏe mạnh nhất còn hơn để cả hai cùng chết đói giữa vùng đầm lầy khắc nghiệt!
```
**Part 7** → `audio/vs/scene12_p7.wav` (583 ký tự) · mood `tram_bi_an`

```text
Mặc dù sở hữu sải cánh rộng tới hai mét rưỡi, nhưng loài cò mỏ giày rất hiếm khi bay lượn trên bầu trời cao. Do trọng lượng cơ thể nặng nề từ bốn đến bảy cân, mỗi lần cất cánh nó phải chạy đà vài bước nặng nhọc trên thảm bèo nổi tương tự một chiếc máy bay ném bom hạng nặng! Nó chỉ bay những chặng ngắn từ một trăm đến năm trăm mét giữa các vũng nước đầm lầy để tìm kiếm những đàn cá phổi ngon lành! Mỗi khi thời tiết quá oi bức, ngoài thói quen xả nước làm mát chân, nó còn ngậm từng ngụm nước lớn trong chiếc mỏ guốc rồi tưới ướt đẫm các quả trứng trong tổ để duy trì độ ẩm tối ưu!
```
**Part 8** → `audio/vs/scene12_p8.wav` (646 ký tự) · mood `am_ap`

```text
Bệnh nhân Cò Mỏ Giày không hề có bất kỳ rối loạn tâm thần nào! Mọi hành vi bất động và tiếng gõ mỏ súng máy đều là bản năng sinh tồn hoàn mỹ của kẻ thống trị đầm lầy! Chẩn đoán của Phòng Cấp Cứu Tạo Hóa: Tinh thần thép, sự kiên nhẫn vô địch và phản xạ săn mồi đạt cấp độ sát thủ hoàn hảo! Toàn bộ mười ca bệnh nhân dị thường của ca trực đêm đã được khám nghiệm toàn diện và chuẩn xác tròn trăm phần trăm! Chúng ta đã vượt qua ca trực đêm cam go nhất mà không hề có bất kỳ ca tử vong hay biến chứng y khoa nào xảy ra! Đồng hồ điểm đúng năm giờ sáng! Đã đến lúc toàn thể y bác sĩ tập hợp tại hội trường lớn cho buổi giao ban kịch tính nhất lịch sử!
```

### scene13 — ĐÁNH GIÁ MƯỜI QUÁI KIỆT
*Thẻ chương:* BÀN GIAO CA TRỰC NĂM GIỜ SÁNG

*Badge:* `GIAO BAN BÌNH MINH` · *mood mặc định:* `nghiem_trang_gia`

**Part 0** → `audio/vs/scene13_p0.wav` (679 ký tự) · mood `nghiem_trang_gia`

```text
Năm giờ sáng. Căn phòng họp giao ban lớn của bệnh viện rực sáng ánh đèn chùm pha lê cổ kính. Toàn thể hội đồng y khoa và kíp trực đêm tề tựu đông đủ quanh chiếc bàn dài bằng gỗ gụ, trên tay mỗi người là một tách cà phê nóng hổi. Tôi trịnh trọng mở chiếc cặp da màu nâu, xếp mười tập hồ sơ bệnh án đã được ký tên và đóng dấu đỏ chót ngay ngắn lên mặt bàn trước mặt hội đồng. Thưa toàn thể các đồng nghiệp và các bác sĩ nội trú thân mến: Chúng ta vừa trải qua ca trực đêm điên rồ và kỳ diệu nhất trong toàn bộ lịch sử y học! Mười bệnh nhân, mười căn bệnh tưởng chừng như vô phương cứu chữa hay dị tật quái gở, thực chất lại là mười phát minh cơ thể học phi thường nhất của tạo hóa!
```
**Part 1** → `audio/vs/scene13_p1.wav` (698 ký tự) · mood `bi_hai`

```text
[laughter] Hãy cùng tôi điểm lại bản tóm tắt lâm sàng mười ca bệnh độc nhất vô nhị đêm nay: Anh chàng Khỉ Đột Lưng Bạc không hề bị viêm dạ dày ruột, mà mang trong bụng một nhà máy lên men vi sinh vật tạo ra bảy mươi phần trăm năng lượng cơ bắp! Chú Nhện Lặn Chuông tí hon không hề muốn tự tử, mà đã tự dệt nên chiếc bình dưỡng khí nano cho phép nó thở oxy dưới nước suốt hai mươi tư giờ! Chú Cá Thòi Lòi không hề bị gãy xương chậu, mà dùng vây ngực làm chân đi bộ và ngậm nước trong mang để chinh phục đất cạn suốt chín mươi phần trăm cuộc đời! Cô Ong Bắp Cày Ngọc không hề dùng bùa ngải ma thuật, mà thực hiện ca phẫu thuật thần kinh chính xác tuyệt đối để điều khiển con gián to gấp sáu lần mình!
```
**Part 2** → `audio/vs/scene13_p2.wav` (934 ký tự) · mood `don_dap`

```text
Chú Cá Mặt Trăng hai tấn không hề bị liệt hàm méo miệng, mà sở hữu bộ não bốn gam siêu tiết kiệm năng lượng và đẻ tới ba trăm triệu trứng mỗi mùa! Chàng Vẹt Kakapo béo tròn không hề bị dị tật cánh cụt, mà đã hoàn thiện chiến lược sinh tồn đi bộ dưới mặt đất và tỏa mùi thơm thảo mộc mê đắm! Chú Lợn Hươu Babirusa không hề sở hữu vũ khí tự sát ngớ ngẩn, mà chiếc nanh cong bốn mươi phân là tấm khiên hộ mệnh và chiếc vương miện kiêu hãnh của tình yêu! Quý cô Hươu Cao Cổ không hề bị cơn bão cao huyết áp ác tính, mà mức huyết áp hai trăm tám mươi là điều kiện sống còn để nuôi dưỡng bộ não cách mặt đất năm mét! Chú Nhím Lông Nhọn không hề bị nhiễm trùng sau mỗi cú ngã cây, mà sở hữu lớp sáp kháng sinh tự nhiên diệt khuẩn tụ cầu vàng hoàn hảo nhất Trái Đất! Và chú Cò Mỏ Giày không hề bị trầm cảm hay đông cứng tâm thần, mà trạng thái bất động là tuyệt đỉnh thiền định của sát thủ đầm lầy với tiếng gõ mỏ một trăm mười lăm đê-xi-ben!
```
**Part 3** → `audio/vs/scene13_p3.wav` (950 ký tự) · mood `hao_hung`

```text
Mỗi một nét giải phẫu kỳ dị của chúng đều là một giải pháp cơ sinh học thiên tài mà hàng trăm viện nghiên cứu công nghệ hiện đại nhất của loài người vẫn đang phải miệt mài học hỏi! Từ vật liệu dệt tơ nhện siêu bền đến kim tiêm giảm đau mô phỏng vi ngạnh nhím, từ bộ đồ bay G-suit mô phỏng da hươu cao cổ đến thuốc tê thần kinh từ nọc ong ngọc! Các kỹ sư hàng không vũ trụ hiện nay đang ứng dụng cơ chế van tĩnh mạch cổ của hươu cao cổ để thiết kế trang phục kháng áp cho phi hành gia bay vào vũ trụ! Và các nhà khoa học vật liệu nano đang nghiên cứu cấu trúc sợi tơ không thấm nước của nhện lặn chuông để sản xuất các thiết bị lọc khí nhân tạo dưới đáy đại dương! Các chuyên gia dược phẩm đang tổng hợp hoạt chất kháng khuẩn từ lớp mỡ gai nhím để bào chế các loại thuốc xịt khử trùng vết thương thế hệ mới! Còn các kỹ sư cơ khí chính xác thì nghiên cứu cơ cấu ngàm kẹp của mỏ cò giày để tạo ra các kẹp gắp thủy lực siêu khỏe trong phẫu thuật nội soi!
```
**Part 4** → `audio/vs/scene13_p4.wav` (617 ký tự) · mood `tram_bi_an`

```text
Ngành điện toán sinh học cũng đang học hỏi cách bộ não bốn gam của cá mặt trăng quản lý khối cơ thể hai tấn để tối ưu hóa thuật toán tiết kiệm năng lượng cho trí tuệ nhân tạo! Và các nhà sinh thái học bảo tồn đang nhân bản mùi hương thảo mộc đặc trưng của vẹt kakapo để chế tạo các bẫy pheromone theo dõi động vật quý hiếm! Hàng triệu năm tiến hóa của tự nhiên chính là phòng nghiên cứu và phát triển vĩ đại nhất, bền bỉ nhất mà loài người từng được thừa hưởng! Không có một phát minh nào của con người lại không tìm thấy nguyên mẫu hoàn hảo đã tồn tại từ hàng triệu năm trước trong cơ thể các loài sinh vật hoang dã!
```
**Part 5** → `audio/vs/scene13_p5.wav` (532 ký tự) · mood `hao_hung`

```text
Biết đâu trong tương lai không xa, các giải thưởng Nobel Y Học danh giá sẽ được trao cho những công trình giải mã thành công các bí mật giải phẫu học này! Một loại thuốc điều trị đột quỵ và chống hình thành cục máu đông dựa trên cơ chế van tĩnh mạch cổ của hươu cao cổ! Một loại màng lọc không khí thông minh tự làm sạch và bẫy oxy mô phỏng cấu trúc chuông lặn của nhện nước! Hay một loại kháng sinh peptide tự nhiên điều chế từ màng mỡ gai nhím có thể dập tắt hoàn toàn các chủng siêu vi khuẩn kháng thuốc nguy hiểm nhất hành tinh!
```
**Part 6** → `audio/vs/scene13_p6.wav` (740 ký tự) · mood `am_ap`

```text
[sigh] Bài học y khoa vĩ đại nhất mà ca trực đêm kinh hoàng này để lại cho toàn thể chúng ta là: Trong y học tiến hóa của tự nhiên, khái niệm dị tật hay khiếm khuyết chỉ là góc nhìn hạn hẹp của những kẻ chưa thấu hiểu trọn vẹn quy luật sinh tồn! Khi một cánh cửa giải phẫu truyền thống khép lại, tạo hóa sẽ mở ra một cánh cửa tiến hóa kỳ diệu khác đưa sinh vật vươn tới đỉnh cao thích nghi! Chúng ta không đến đây để sửa chữa tự nhiên, mà đến đây để chiêm ngưỡng, học hỏi và bảo bọc sự đa dạng sinh học vô giá của hành tinh này! Tôi xin tuyên bố: Ca trực đêm lịch sử của Phòng Cấp Cứu Tạo Hóa chính thức kết thúc thành công rực rỡ! Chuẩn bị ký giấy xuất viện và tiễn mười người bạn đặc biệt của chúng ta trở về với thiên nhiên hoang dã nào!
```

### scene14 — TẠM BIỆT MƯỜI QUÁI KIỆT
*Thẻ chương:* HỒ SƠ MẬT CHUYẾN TÀU TỐC HÀNH

*Badge:* `XUẤT VIỆN` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene14_p0.wav` (718 ký tự) · mood `am_ap`

```text
Sáu giờ sáng. Bầu trời ngoài kia đã trong xanh trở lại sau cơn mưa bão đêm qua, những giọt sương mai đọng lấp lánh trên từng phiến lá ngoài sân bệnh viện. Không khí buổi sớm mai ngọt ngào và mát rượi, xua tan đi toàn bộ sự mệt mỏi và căng thẳng của ca trực cấp cứu nghẹt thở vừa qua. Cửa sảnh lớn của Phòng Cấp Cứu Tạo Hóa mở toang đón ánh nắng bình minh ấm áp. Và giờ phút chia tay đầy xúc động đã chính thức điểm. Mười bệnh nhân quái kiệt của chúng ta đã xếp thành một hàng ngay ngắn trước thềm sảnh lớn, mỗi người mang một vẻ mặt rạng rỡ và tự tin hơn bao giờ hết! Chú Khỉ Đột Lưng Bạc ôm một giỏ táo tươi ngon, cái bụng vẫn tròn vo nhưng đã hết đau hoàn toàn, vẫy cánh tay cơ bắp lực sĩ chào tạm biệt các y bác sĩ!
```
**Part 1** → `audio/vs/scene14_p1.wav` (622 ký tự) · mood `hao_hung`

```text
Chú Cá Thòi Lòi nhảy chồm chồm trên khay bùn tạm biệt, nháy đôi mắt lồi tinh nghịch rồi lặn tọt vào chiếc xe bồn nước chuyên dụng để về lại rừng Cà Mau! Cô Ong Bắp Cày Ngọc bay lượn một vòng quanh đầu tôi như một lời cảm ơn duyên dáng, chiếc thân xanh ngọc bích lấp lánh dưới ánh bình minh trước khi bay vút lên bầu trời! Chú Cá Mặt Trăng hai tấn được cần cẩu nhẹ nhàng nâng bổng lên xe chuyên dụng chuyển thẳng ra vịnh biển để tiếp tục những chuyến lặn sâu tám trăm mét! Chú Vẹt Kakapo béo tròn được tặng một chiếc ba-lô nhỏ chứa đầy hạt thông, lon ton đi bộ theo các nhân viên bảo tồn New Zealand với nụ cười mãn nguyện!
```
**Part 2** → `audio/vs/scene14_p2.wav` (567 ký tự) · mood `tram_bi_an`

```text
Chú Lợn Hươu Babirusa kiêu hãnh khoe bốn chiếc răng nanh cong vút đã được làm sạch sáng bóng, bước đi tự tin về lại hòn đảo nhiệt đới hoang dã! Quý cô Hươu Cao Cổ sải những bước chân thanh tao qua cổng bệnh viện, chiếc cổ dài hai mét vươn cao đón những làn gió mát lành của thảo nguyên! Chú Cò Mỏ Giày khẽ cúi đầu chào lịch thiệp, rồi đột ngột xòe đôi cánh rộng hai mét rưỡi bay vút lên không trung xé toạc làn sương sớm! Và chú Nhím Lông Nhọn cùng chú Nhện Lặn Chuông tí hon cũng đã yên vị trong những chiếc lồng sinh thái an toàn để trở về với thiên nhiên hoang dã!
```
**Part 3** → `audio/vs/scene14_p3.wav` (742 ký tự) · mood `am_ap`

```text
[sigh] Tôi hít một hơi thật sâu làn không khí trong lành của buổi sớm mai, cất chiếc ống nghe y tế vào túi áo khoác. Ca trực đêm kinh hoàng nhất cuộc đời làm bác sĩ của tôi tại Phòng Cấp Cứu Tạo Hóa đã chính thức khép lại trong niềm vui trọn vẹn. Nhưng bài học sâu sắc mà mười sinh vật kỳ dị này để lại sẽ mãi mãi in đậm trong tâm trí của mỗi chúng ta: Trong thế giới tự nhiên kỳ diệu này, không có sinh vật nào là sai sót, không có nét giải phẫu nào là vô nghĩa. Mọi sự sống đều là một kiệt tác hoàn mỹ của mẹ Trái Đất! Hàng triệu năm tiến hóa đã đẽo gọt nên những cơ chế sinh tồn tinh xảo vượt xa trí tưởng tượng phong phú nhất của con người! Mỗi sinh vật là một nốt nhạc độc đáo trong bản giao hưởng vĩ đại của sự sống trên hành tinh xanh!
```
**Part 4** → `audio/vs/scene14_p4.wav` (565 ký tự) · mood `am_ap`

```text
Tôi cùng cô y tá trao từng túi thuốc bổ vitamin và cẩm nang chăm sóc sức khỏe sinh thái cho người đại diện của từng đoàn cứu hộ. Chúng tôi dặn dò kỹ lưỡng: Anh khỉ đột nhớ giảm ăn lá cây có mủ đắng, chú cá thòi lòi nhớ bôi kem giữ ẩm mang cá khi leo cây, còn chú vẹt kakapo thì nhớ tập thể dục đi bộ đều đặn nhé! [laughter] Cả mười bệnh nhân cùng hòa giọng tạo nên một bản hợp xướng rộn rã làm bừng sáng cả khoảng sân bệnh viện trong nắng sớm! Một ca trực đêm đầy ắp tiếng cười, những giọt mồ hôi và sự kính phục vô bờ trước sức sáng tạo không giới hạn của tạo hóa!
```
**Part 5** → `audio/vs/scene14_p5.wav` (986 ký tự) · mood `tram_bi_an`

```text
Tu... tu... tuuuu! Bất thình lình, một tiếng còi tàu hơi nước trầm đục và ma mị từ đâu vang vọng lại qua thung lũng sương mù dày đặc! Tiếng còi tàu hú lên từng hồi dồn dập, báo hiệu chuyến tàu tốc hành xuyên đêm chở mười hành khách bí ẩn nhất hành tinh sắp lăn bánh vào ga! Một vụ án mất tích bí ẩn vừa xảy ra trên chuyến tàu tốc hành vượt bão tuyết! Và thám tử tài ba sẽ phải vào cuộc để vén màn mười bí mật sinh học gây sốc tiếp theo! Những manh mối dấu vết của Rắn Hổ Mang Chúa, Cá Sấu Nước Mặn và Cá Mập Trắng đã bắt đầu lộ diện trên các toa tàu sương mù! Ai trong số mười quái thú đầm lầy và đại dương này là thủ phạm thực sự của vụ án chấn động đường ray xe lửa đêm đông giá rét? Một hành trình phá án nghẹt thở kết hợp giữa tư duy trinh thám cổ điển và những bí mật giải phẫu học rợn người đang chờ đón quý khán giả trong siêu phẩm Mega số sáu tiếp theo! Chiếc vali da cổ điển khóa số đang chứa bản hồ sơ mật về độc tố và lực cắn của mười hung thần đầm lầy đang đợi được giải mã!
```
**Part 6** → `audio/vs/scene14_p6.wav` (600 ký tự) · mood `tram_bi_an`

```text
Ngoài kia, những bông tuyết đầu mùa bắt đầu rơi lả tả trên những mái vòm toa tàu hỏa bằng kim loại sáng loáng. Tiếng chuông đồng hồ quả quýt của vị thám tử bí ẩn vang lên từng tiếng tích tắc điểm đúng mười hai giờ đêm! Một bức mật thư viết tay bằng mực tím bị kẹp dưới chân chiếc đèn bàn cổ, hé lộ danh sách mười hành khách mang những vũ khí sinh học nguy hiểm bậc nhất tự nhiên! Liệu vị thám tử tài ba có kịp phá giải mười vụ án mạng bí ẩn trước khi chuyến tàu hơi nước cập bến bình minh hay không? Một bầu không khí nghẹt thở, ly kỳ và đậm chất trinh thám cổ điển đang đón đợi các bạn ở phía trước!
```
**Part 7** → `audio/vs/scene14_p7.wav` (439 ký tự) · mood `hao_hung`

```text
Cảm ơn toàn thể các đồng nghiệp và quý khán giả đã đồng hành cùng tôi qua ca trực đêm đáng nhớ này tại Phòng Cấp Cứu Tạo Hóa! Đừng quên bấm đăng ký kênh và nhấn chuông thông báo để không bỏ lỡ hành trình phá án tiếp theo trên Chuyến Tàu Tốc Hành Bí Ẩn nhé! Xin chào và hẹn gặp lại! Hãy để lại bình luận bên dưới xem ca bệnh nào đêm nay làm các bạn kinh ngạc và thán phục nhất nhé! Bác Sĩ Trưởng Khoa xin chào và hẹn gặp lại tất cả các bạn!
```

### Shorts → `audio/vs/shorts.wav`

```text
Mười hai giờ đêm tại Phòng Cấp Cứu Tạo Hóa! Còi báo động đỏ réo vang khi mười ca bệnh kỳ dị nhất hành tinh cùng lúc tràn vào sảnh! Anh Khỉ Đột Lưng Bạc đấm bẹp đầu xe hơi nhưng đang khóc ròng vì bụng đầy hơi men! Chú Cá Thòi Lòi nhảy chồm chồm kiên quyết không thở dưới nước, dùng vây leo tót lên rèm cửa! Cô Ong Bắp Cày Ngọc đòi chích nọc thôi miên não gián thành zombie ngoan ngoãn! Khối thịt hai tấn Cá Mặt Trăng nằm bẹp dí ngơ ngác, chỉ đang tắm nắng sau chuyến lặn sâu tám trăm mét! Vẹt Kakapo béo tròn bốn cân biểu diễn nhảy dù úp bụng xuống đống gối bông của y tá! Lợn Babirusa với bốn nanh cong vút xuyên sống mũi uốn ngược sát sạt hộp sọ! Hươu Cao Cổ huyết áp vọt lên gần ba trăm, tim mười một cân bơm máu ngược trọng lực lên chiếc cổ hai mét! Nhím Lông Nhọn rụng ba mươi ngàn chiếc gai có ngạnh, nhưng tẩm sẵn lớp mỡ kháng sinh tự chữa lành thần tốc! Và Cò Mỏ Giày đứng như tượng đá rồi bất thần gõ mỏ súng máy một trăm mười lăm đê-xi-ben vang dội! Bấm ngay vào video dài để cùng Bác Sĩ Trưởng Khoa khám phá ca trực đêm kinh hoàng này nhé!
```

**Whisper prompt:** `Phòng Cấp Cứu Tạo Hóa, Bệnh Viện Đa Khoa Tiến Hóa, Bác Sĩ Trưởng Khoa, Khỉ Đột Lưng Bạc, Nhện Lặn Chuông, Cá Thòi Lòi, Ong Bắp Cày Ngọc, Cá Mặt Trăng, Vẹt Kakapo, Lợn Hươu Babirusa, Hươu Cao Cổ, Cò Mỏ Giày, Nhím Lông Nhọn, X-quang, điện tâm đồ, huyết áp, manh tràng, chuông lặn, zombie, clavus, Rete Mirabile, súng máy, vi ngạnh, kháng sinh`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| hai trăm tám mươi | 280 |
| hai trăm tám mươi đến ba trăm | 280-300 |
| ba trăm | 300 |
| ba trăm mi-li-mét thủy ngân | 300 mmHg |
| hai trăm tám mươi mi-li-mét thủy ngân | 280 mmHg |
| hai trăm tám mươi đến ba trăm mi-li-mét thủy ngân | 280-300 mmHg |
| ba mươi ngàn | 30.000 |
| ba mươi nghìn | 30.000 |
| ba mươi ngàn chiếc gai | 30.000 chiếc gai |
| ba mươi ngàn chiếc | 30.000 chiếc |
| ba trăm triệu trứng | 300 triệu trứng |
| ba trăm triệu | 300 triệu |
| sáu mươi triệu | 60 triệu |
| hai tấn | 2 tấn |
| bốn ki-lô-gam | 4 kg |
| bốn cân | 4 kg |
| hai trăm ki-lô-gam | 200 kg |
| hai trăm cân | 200 kg |
| hai mươi tư giờ | 24 giờ |
| hai mươi tư | 24 |
| năm mươi đến sáu mươi phần trăm | 50-60% |
| bảy mươi phần trăm | 70% |
| năm mươi tư phần trăm | 54% |
| ba mươi phần trăm | 30% |
| chín mươi tám phần trăm | 98% |
| bốn mươi xăng-ti-mét | 40 cm |
| hai mươi tư xăng-ti-mét | 24 cm |
| tám trăm mét | 800 m |
| hai mươi mét | 20 m |
| mười mét | 10 m |
| năm cây số | 5 km |
| năm ki-lô-mét | 5 km |
| ba phẩy hai cây số một giờ | 3,2 km/h |
| ba phẩy hai ki-lô-mét một giờ | 3,2 km/h |
| một ngàn ba trăm ki-lô-gam | 1300 kg |
| một trăm mười lăm đê-xi-ben | 115 dB |
| mười một ki-lô-gam | 11 kg |
| mười một cân | 11 kg |
| không độ C | 0°C |
| bốn độ C | 4°C |
| nghìn tỷ | nghìn tỷ |
| năm mươi ngàn | 50.000 |
| triệu năm | triệu năm |
| trăm triệu năm | trăm triệu năm |
| tám trăm | 800 |
| chín mươi tám | 98 |
| mươi triệu | mươi triệu |
| bốn mươi lăm | 45 |
| chín mươi | 90 |
| trăm năm mươi | 150 |
| hai trăm | 200 |
| hai | 2 |
| ba | 3 |
| bốn | 4 |
| năm | 5 |
| sáu | 6 |
| bảy | 7 |
| tám | 8 |
| chín | 9 |
| mười | 10 |
| mười hai | 12 |
| mười tám | 18 |
| hai mươi | 20 |
| một trăm | 100 |
| Một trăm | 100 |
| Hai trăm | 200 |
| Ba trăm | 300 |
| bốn trăm | 400 |
| Bốn trăm | 400 |
| năm trăm | 500 |
| một trăm hai mươi | 120 |
| một trăm tám mươi | 180 |
| hai trăm tám mươi trên một trăm tám mươi | 280/180 |
| hai trăm tám mươi trên một trăm tám mươi mi-li-mét thủy ngân | 280/180 mmHg |
| bốn gam | 4 g |
| mười tấn | 10 tấn |
| năm mươi mét khối | 50 m³ |
| bảy phân rưỡi | 7,5 cm |
| hai phân rưỡi | 2,5 cm |
| hai phân | 2 cm |
| mười phân | 10 cm |
| bốn mươi phân | 40 cm |
| sáu mươi phân | 60 cm |
| bảy xăng-ti-mét rưỡi | 7,5 cm |
| hai xăng-ti-mét rưỡi | 2,5 cm |
| sáu mươi xăng-ti-mét | 60 cm |
| ba mươi xăng-ti-mét | 30 cm |
| hai mươi xăng-ti-mét | 20 cm |
| hai xăng-ti-mét | 2 cm |
| năm xăng-ti-mét | 5 cm |
| hai mi-li-mét | 2 mm |
| một phần mười | 1/10 |
| một phần nghìn | 1/1000 |
| một phần năm trăm ngàn | 1/500.000 |
| một ngàn ba trăm | 1300 |
| tám mươi át-mốt-phe | 80 atm |
| bốn mươi giờ | 40 giờ |
| mười lăm phút | 15 phút |
| hai phút | 2 phút |
| năm tiếng | 5 tiếng |
| ba mươi năm | 30 năm |
| bốn trăm triệu năm | 400 triệu năm |
| hàng triệu năm | hàng triệu năm |
| năm mươi phần trăm | 50% |
| chín mươi phần trăm | 90% |
| tròn trăm phần trăm | 100% |
| bốn cân rưỡi | 4,5 kg |
| hai mươi đến ba mươi cân | 20-30 kg |
| năm mét | 5 m |
| ba mét | 3 m |
| bốn mét | 4 m |
| hai mét rưỡi | 2,5 m |
| hai mét | 2 m |
| một mét rưỡi | 1,5 m |
| một mét hai | 1,2 m |
| một mét | 1 m |
| nửa mét | 0,5 m |
| bốn trăm đến tám trăm mét | 400-800 m |
| hàng ngàn hải lý | hàng ngàn hải lý |
| hàng ngàn cây số | hàng ngàn km |
| mươi lăm | mươi lăm |
| ba mươi lăm | 35 |
| ba mươi lăm đến hơn bốn mươi giờ | 35-40 giờ |
| ba mươi lăm đến bốn mươi giờ | 35-40 giờ |
| bốn mét rưỡi | 4,5 m |
| hai mươi đến ba mươi | 20-30 |
| ba mươi nhịp | 30 nhịp |
| hai mươi nhịp | 20 nhịp |
| sáu giờ | 6 giờ |
| năm giờ | 5 giờ |
| bốn giờ | 4 giờ |
| ba giờ | 3 giờ |
| hai giờ | 2 giờ |
| một giờ | 1 giờ |
| mười hai giờ | 12 giờ |
| ba mươi phút | 30 phút |
| bốn mươi phút | 40 phút |
| sáu tiếng | 6 tiếng |
| mười sáu | 16 |
| chín mươi lăm phần trăm | 95% |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · BÃO ĐÊM VÀ MƯỜI CA BỆNH · 246.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:04.8 (4.8s) | L01 | Mười 2 giờ đêm. Cơn bão giông nhiệt đới cấp 12 đang gào thét dữ dội ngoài khung cửa kính phòng cấp |  | Bầu trời đêm đen kịt vần vũ mây bão, tia sét ngoằn ngoèo xé toạc màn đêm chiếu rọi tòa nhà bệnh viện cổ kính phong cách retro thập niên 1950; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b02 | 00:04.8–00:10.9 (6.1s) | L02 | cứu. Những vệt sét trắng xóa liên tục xé toạc bầu trời, rọi sáng tấm biển đồng cổ kính treo trước cổng lớn: Phòng Cấp Cứu Tạo |  | Tấm biển đồng thau cổ điển khắc chìm dòng chữ PHÒNG CẤP CỨU TẠO HÓA phát sáng dưới ánh chớp bão đêm; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b03 | 00:10.9–00:16.6 (5.7s) | L03 | Hóa. Tôi là Bác Sĩ Trưởng Khoa, người đã cầm dao mổ và ống nghe suốt 30 5 qua giữa những ca bệnh nghẹt thở nhất của tự |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đứng bên cửa sổ phòng làm việc, tay cầm tách cà phê đen nóng bốc khói nghi ngút, ánh mắt trầm tư nhìn ra màn mưa bão trắng xóa. |
| b04 | 00:16.6–00:22.8 (6.2s) | L04 | nhiên. Nhưng linh cảm nghề nghiệp mách bảo tôi rằng, đêm nay sẽ là ca trực điên rồ và kỳ quặc nhất trong toàn bộ sự nghiệp y khoa |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án nhấp một ngụm cà phê đắng, quay lại nhìn chiếc đồng hồ quả lắc bằng đồng đang gõ nhịp tích tắc trên tường. |
| b05 | 00:22.8–00:28.7 (6.0s) | L05 | của mình. Chiếc bàn làm việc bằng gỗ sồi của tôi chất đầy những xấp bệnh án ngả vàng, cùng chiếc ống nghe bằng đồng thau sáng bóng. |  | Bàn làm việc ngổn ngang hồ sơ bệnh án cổ điển, kính lúp y khoa, ống nghe bằng đồng và ngọn đèn bàn chụp xanh phong cách retro; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b06 | 00:28.7–00:35.4 (6.7s) | L06 | Một ca trực đêm chuẩn mực đòi hỏi tinh thần thép, đôi bàn tay không bao giờ run rẩy và một lượng caffeine đủ để vận hành một đầu máy xe lửa! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án với tay rót thêm một tách cà phê đen sánh mịn từ chiếc bình thủy tinh cổ điển bốc khói nghi ngút. |
| b07 | 00:35.4–00:43.0 (7.6s) | L07 | Bác sĩ trưởng khoa ơi! Nguy to rồi bác sĩ ơi! Toàn bộ chuông báo động ở 10 phòng khám chuyên khoa đang reo inh ỏi cùng một lúc kìa! |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng hớt hải đẩy tung cánh cửa gỗ đôi chạy vào phòng, hai tai thỏ dài rung lên bần bật, tay ôm xấp hồ sơ dày cộp. |
| b08 | 00:43.0–00:49.4 (6.4s) | L08 | Hệ thống đường dây nóng khẩn cấp của bệnh viện vừa bị nghẽn mạch hoàn toàn vì hàng loạt cuộc gọi cấp cứu dồn dập từ khắp các châu lục! |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng chỉ tay về phía bảng tổng đài điện thoại cổ điển sau lưng đang nhấp nháy đèn đỏ liên hồi kèm chuông reo dồn dập; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b09 | 00:49.4–00:55.3 (5.9s) | L09 | Mười bệnh nhân quái đản nhất hành tinh đang cùng lúc đổ bộ vào sảnh cấp cứu của chúng ta trên đủ mọi loại phương tiện vận chuyển! |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng run rẩy giơ xấp giấy bệnh án có dán mười bức ảnh sinh vật kỳ dị ra trước mặt bác sĩ trưởng khoa; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b10 | 00:55.3–01:02.5 (7.2s) | L10 | Bình tĩnh nào cô y tá! Quy tắc số một của phòng cấp cứu: Càng hoảng loạn thì càng phải pha một tách cà phê thật đậm và kiểm tra lại danh sách bệnh nhân! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đặt tách cà phê xuống đĩa sứ, kéo chiếc kính lão đồi mồi xuống sống mũi rồi đón lấy tập hồ sơ từ tay y tá. |
| b11 | 01:02.5–01:07.8 (5.3s) | L11 | Để tôi đọc to danh sách phân loại bệnh nhân đêm nay cho toàn thể kíp trực cùng nghe xem tạo hóa vừa gửi tới những ca hóc búa nào! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án lật giở từng trang hồ sơ bệnh án kẹp trên chiếc bảng kẹp bệnh án y khoa khổng lồ (clipboard) kẹp trên giá đỡ kim loại, hiển thị 10 hồ sơ bệnh án hoạt hình với nhãn đơn thuốc phát sáng và sóng nhịp tim ECG màu đỏ nhấp nháy (không có chữ, không có số), ánh mắt sáng lên vẻ thích thú và tò mò cao độ. |
| b12 | 01:07.8–01:14.0 (6.2s) | L12 | Ca số một: Một anh chàng Khỉ Đột Lưng Bạc nặng 200 kg, sở hữu cú đấm ngàn cân nhưng đang nằm ôm bụng khóc thét vì ứ đọng khí |  | chú Khỉ Đột Lưng Bạc hoạt hình cơ bắp cuồn cuộn vạm vỡ, mảng lông bạc sáng chói dọc sống lưng, bụng to tròn căng phồng vì chứa đầy lá cây lên men, ngồi xếp bằng trên giường bệnh ôm bụng thở dài nằm co ro trên giường bệnh dã chiến, hai tay ôm chiếc bụng tròn ủng căng phồng vẻ mặt mếu máo tội nghiệp; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b13 | 01:14.0–01:19.7 (5.7s) | L13 | gas! Ca số 2: Một chú Nhện Lặn Chuông tí hon đang cố tình nhảy ra khỏi mặt nạ thở oxy nhi khoa để lao đầu xuống |  | chú Nhện Lặn Chuông (diving bell spider) hoạt hình màu nâu đen nhiều lông mịn, tám chân ôm một chiếc bóng khí lấp lánh như viên ngọc trong suốt dưới bụng, đang ngâm mình trong bể nước dã chiến tám chân thoăn thoắt bò trốn khỏi chiếc mặt nạ dưỡng khí mini, nhảy ùm vào bình nước thủy tinh; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b14 | 01:19.7–01:26.4 (6.6s) | L14 | chậu nước! Ca số 3: Một vận động viên bơi lội có tên Cá Thòi Lòi kiên quyết không chịu nằm yên trong bồn nước mà cứ đòi leo lên bàn khám để chống |  | chú Cá Thòi Lòi hoạt hình màu nâu xám lấm chấm xanh ngọc, hai mắt to tròn lồi hẳn trên đỉnh đầu chớp chớp ngộ nghĩnh, hai vây ngực bè to như đôi tay đang chống nạng gỗ mini đòi nhảy khỏi cáng cứu thương dùng hai vây ngực cơ bắp chống thẳng đứng trên mặt bàn khám, đôi mắt lồi đảo tròn tinh nghịch; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b15 | 01:26.4–01:33.2 (6.8s) | L15 | đẩy! Ca số 4: Một nữ phẫu thuật viên tí hon mang tên Ong Bắp Cày Ngọc đang dẫn giải một con gián khổng lồ đi vào phòng mổ thần kinh như dắt thú cưng! |  | cô Ong Bắp Cày Ngọc (emerald cockroach wasp) hoạt hình thân thon dài phát sáng xanh ngọc bích kim loại lộng lẫy, chân dài thanh mảnh, tay cầm chiếc dao mổ phẫu thuật thần kinh siêu nhỏ giơ lên đầy tự tin màu xanh ngọc bích óng ánh đang dùng râu kéo lê một chú gián to lớn ngoan ngoãn bước từng bước vô hồn; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b16 | 01:33.2–01:39.9 (6.7s) | L16 | Ca số 5: Một khối thịt khổng lồ nặng 2 tấn mang tên Cá Mặt Trăng vừa làm sập gãy hoàn toàn chiếc bàn nâng thủy lực của đội vận chuyển! |  | chú Cá Mặt Trăng (ocean sunfish) hoạt hình khổng lồ hình đĩa tròn dẹt màu xám bạc, không có cuống đuôi, hai vây lưng và vây phần đuôi dựng đứng dài ngoằng, nằm ngửa trên chiếc cáng cứu thương quá khổ mắt to tròn ngơ ngác tròn xoe như chiếc bánh kếp khổng lồ nằm bẹp trên sàn sảnh đón tiếp, đôi mắt tròn xoe ngơ ngác chớp chớp; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b17 | 01:39.9–01:46.8 (6.9s) | L17 | Ca số 6: Một chàng Vẹt Kakapo béo tròn 4,5 kg chẳng hề biết bay, vừa rơi từ trên cây cao xuống đất vì tưởng mình là đại |  | chú Vẹt Kakapo hoạt hình béo múp míp lông xanh rêu pha đốm nâu đen, mặt tròn lông tơ như chim cú mèo, mắt ngơ ngác dễ thương, hai cánh ngắn cũn cố vỗ lạch bạch trèo lên nóc tủ thuốc lông xanh rêu béo múp míp đang ngồi xoa chiếc mông tròn xoe giữa đống lông vũ rụng tơi bời; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b18 | 01:46.8–01:53.4 (6.6s) | L18 | bàng! Ca số 7: Một chú Lợn Hươu Babirusa với 4 chiếc răng nanh cong vút dị thường đang có nguy cơ tự đâm thủng hộp sọ của |  | chú Lợn Hươu Babirusa hoạt hình da xám nhăn nheo ít lông, mõm dài, bốn chiếc răng nanh cong vút dị thường trong đó hai nanh trên mọc xuyên qua sống mũi uốn ngược về phía trán, vẻ mặt lo lắng sờ trán với cặp nanh trên mọc ngược xuyên qua sống mũi uốn cong sát trán, vẻ mặt đầy bối rối lo âu; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b19 | 01:53.4–02:01.2 (7.8s) | L19 | chính mình! Ca số 8: Một quý cô Hươu Cao Cổ cao 5 m đang choáng váng ngất xỉu với chỉ số huyết áp tâm thu vọt lên ngưỡng gần 300 mmHg! |  | chú Hươu Cao Cổ hoạt hình cao lêu nghêu có đốm hoa văn nâu vàng, chiếc cổ dài thẳng tắp quấn dải băng đo huyết áp y tế to bản màu đỏ, mắt to hiền từ chớp chớp gục chiếc cổ dài hai mét lên thành quầy tiếp nhận bệnh nhân, mắt hoa lên nhìn những vòng tròn xoay tít; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b20 | 02:01.2–02:07.9 (6.7s) | L20 | Ca số 9: Một chú Nhím Lông Nhọn Bắc Mỹ vừa ngã từ cây thông xuống đất và tự cắm hàng trăm chiếc gai sắc nhọn vào đùi của |  | chú Nhím Lông Nhọn Bắc Mỹ hoạt hình béo tròn xù xì, toàn thân phủ kín ba mươi ngàn chiếc gai nhọn trắng đen, đang ôm chặt một thân cây gỗ gặm vỏ thuốc, người tỏa mùi tinh dầu thơm nhẹ xù lông gai lởm chởm, một bên chân ngắn cũn cắm đầy những mảnh gai gãy nhăn nhó gãi đầu; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b21 | 02:07.9–02:15.2 (7.3s) | L21 | chính mình! Và ca số 10: Một pho tượng đá sống mang tên Cò Mỏ Giày đứng bất động 5 tiếng đồng hồ không thèm chớp mắt giữa sảnh chờ! |  | chú Cò Mỏ Giày hoạt hình lông xám tro, dáng đứng sừng sững bất động như tượng đá, chiếc mỏ khổng lồ màu vàng xám phình to hình chiếc guốc gỗ, ánh mắt lạnh như tiền đứng canh cửa phòng cấp cứu đứng sừng sững như tượng đá xám giữa sảnh bệnh viện, chiếc mỏ guốc khổng lồ chúc xuống góc bốn mươi lăm độ đầy ma mị; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b22 | 02:15.2–02:23.0 (7.8s) | L22 | Trời đất ơi! Nhìn vào bảng tiếp nhận này thì đây không phải là một bệnh viện thông thường nữa, mà là một viện bảo tàng giải phẫu học kỳ dị nhất vũ trụ! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án bật cười thành tiếng, lắc đầu thán phục trước danh sách bệnh nhân vô tiền khoáng hậu đang hiện diện trước mắt. |
| b23 | 02:23.0–02:29.2 (6.2s) | L23 | Bác sĩ trưởng khoa đã từng thấy ca trực nào mà toàn bộ sách giáo khoa giải phẫu kinh điển đều phải xé bỏ viết lại từ đầu như đêm nay chưa? |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng đưa tay lên trán thở dài thườn thượt, gương mặt thỏ trắng lộ rõ vẻ mệt mỏi nhưng cũng đầy hồi hộp chờ đợi; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b24 | 02:29.2–02:34.6 (5.4s) | L24 | Chưa từng có một tiền lệ nào tương tự trong suốt 3 thập kỷ làm nghề y của tôi cả cô y tá thân mến ạ! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười đôn hậu, bước tới tủ thuốc lấy ra chiếc áo choàng phẫu thuật màu xanh ngọc bích quen thuộc. |
| b25 | 02:34.6–02:41.8 (7.2s) | L25 | Mỗi sinh vật đang nằm ngoài kia là một bài toán hóc búa, một nghịch lý cơ thể học thách thức mọi định luật sinh học mà con người từng biết đến! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án khoác chiếc áo blouse trắng tinh tươm, đeo găng tay cao su vô trùng và chỉnh lại chiếc ống nghe trên cổ. |
| b26 | 02:41.8–02:47.3 (5.5s) | L26 | Rầm! Rầm! Rầm! Tiếng đập cửa kính sảnh đón tiếp dồn dập vang lên át cả tiếng sấm rền ngoài trời! |  | Cánh cửa kính lớn rung bần bật dưới áp lực xô đẩy từ bên ngoài, bóng đen đồ sộ của các loài vật in dài trên nền sàn gạch hoa cương; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b27 | 02:47.3–02:53.0 (5.7s) | L27 | Đoàn xe cứu thương chuyên dụng nối đuôi nhau rọi đèn pha vàng rực vào sảnh bệnh viện, còi hụ vang rền xé toạc màn đêm u tối! |  | Dãy xe cứu thương cổ điển bật đèn chớp xoay tròn màu đỏ rực, tiếng còi hụ khẩn cấp inh ỏi ngoài sân bệnh viện; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b28 | 02:53.0–02:57.5 (4.5s) | L28 | Các nhân viên điều dưỡng đang hối hả đẩy những chiếc cáng cứu thương quá khổ vào bên trong hành lang lát gạch men sáng loáng! |  | Hàng chục nhân viên y tế hối hả chạy dọc hành lang đẩy các cáng cứu hộ chuyên dụng có gắn bình dưỡng khí và máy đo nhịp tim; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b29 | 02:57.5–03:03.7 (6.2s) | L29 | Mùi cồn sát trùng hòa lẫn với mùi ẩm ướt của bùn lầy, mùi tinh dầu thông và hơi muối biển mặn mòi tràn ngập bầu không khí! |  | Khung cảnh nhộn nhịp khẩn trương của sảnh cấp cứu với làn khói thuốc sát trùng mờ ảo và ánh đèn neon rực rỡ; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b30 | 03:03.7–03:08.8 (5.1s) | L30 | Mọi người chú ý giữ trật tự! Xin mời các bệnh nhân không chen lấn xô đẩy tại quầy tiếp đón khẩn cấp! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án bước ra sảnh lớn, cất giọng vang ấm dõng dạc trấn an toàn bộ đám đông đang nhốn nháo ngoài sảnh. |
| b31 | 03:08.8–03:16.3 (7.5s) | L31 | Anh khỉ đột xin vui lòng không dựa lưng vào vách kính tủ thuốc kẻo vỡ kính! Và chú nhím lông nhọn làm ơn giữ khoảng cách an toàn với dép xốp của các cô y tá! |  | chú Khỉ Đột Lưng Bạc hoạt hình cơ bắp cuồn cuộn vạm vỡ, mảng lông bạc sáng chói dọc sống lưng, bụng to tròn căng phồng vì chứa đầy lá cây lên men, ngồi xếp bằng trên giường bệnh ôm bụng thở dài ngượng ngùng né người khỏi tủ thuốc, chú chú Nhím Lông Nhọn Bắc Mỹ hoạt hình béo tròn xù xì, toàn thân phủ kín ba mươi ngàn chiếc gai nhọn trắng đen, đang ôm chặt một thân cây gỗ gặm vỏ thuốc, người tỏa mùi tinh dầu thơm nhẹ c |
| b32 | 03:16.3–03:22.7 (6.4s) | L32 | Toàn thể đội ngũ y bác sĩ nội trú mau chóng vào vị trí trực chiến! Chuẩn bị máy chụp X-quang, máy siêu âm và các bộ dụng cụ vi phẫu ngay |  | Các bác sĩ trẻ trong trang phục y tế hối hả mở các tủ đồ nghề kim loại sáng loáng, chuẩn bị sẵn sàng cho ca trực đêm; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b33 | 03:22.7–03:28.4 (5.7s) | L33 | lập tức! Đêm nay chúng ta sẽ không chợp mắt dù chỉ một giây để giải mã toàn bộ 10 kỳ quan cơ thể học này! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án nhìn quanh toàn thể đội ngũ y tế với ánh mắt kiên định và đầy nhiệt huyết của người thầy thuốc dày dạn kinh nghiệm. |
| b34 | 03:28.4–03:32.5 (4.1s) | L34 | Bởi vì nguyên lý tối thượng tại Phòng Cấp Cứu Tạo Hóa của chúng ta luôn luôn là: |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án chỉ tay lên dòng khẩu hiệu bằng chữ mạ vàng gắn trang trọng trên vòm cửa sảnh đón tiếp. |
| b35 | 03:32.5–03:37.2 (4.7s) | L35 | Không có sinh vật nào trên Trái Đất này sinh ra với một nét giải phẫu thừa thãi hay một cấu trúc sai lầm! |  | Cận cảnh gương mặt thông thái và nghiêm nghị của ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án toát lên niềm tin mãnh liệt vào sự hoàn mỹ của tự nhiên. |
| b36 | 03:37.2–03:44.1 (6.9s) | L36 | Những gì mắt thường nhìn vào tưởng như dị tật, bệnh hoạn hay ngớ ngẩn, thực chất lại là tuyệt tác đỉnh cao của hàng triệu 5 chọn lọc tự nhiên khốc liệt! |  | Bức tranh toàn cảnh hội tụ mười sinh vật kỳ dị dưới ánh sáng rực rỡ của đèn phòng mổ, mỗi loài mang một cấu trúc cơ thể phi thường; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b37 | 03:44.1–03:50.9 (6.8s) | L37 | Và nhiệm vụ của người thầy thuốc đêm nay là lắng nghe câu chuyện sinh tồn kỳ diệu được khắc ghi sâu bên trong từng thớ cơ và mạch máu của chúng! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười đầy xúc động, nhẹ nhàng mở chiếc cặp da đựng dụng cụ y tế chuyên dụng. |
| b38 | 03:50.9–03:59.9 (8.9s) | L38 | Thông báo khẩn cấp từ tổng đài bệnh viện: Bệnh nhân số một tại Khoa Cấp Cứu Tổng Hợp đang có dấu hiệu quá tải áp suất ổ bụng nghiêm trọng! Đề nghị Bác Sĩ Trưởng Khoa có mặt ngay lập tức! |  | Chiếc loa phát thanh bằng kim loại gắn trên góc tường rung lên phát ra giọng thông báo khẩn thiết của nhân viên tổng đài trực ban; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b39 | 03:59.9–04:06.7 (6.9s) | L39 | Được rồi! Đội ngũ y tế theo tôi bước vào phòng khám số một ngay! Cuộc chiến cứu hộ 10 quái kiệt sinh học chính thức bắt đầu! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án cùng cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng sải những bước chân dứt khoát hướng thẳng về phía cánh cửa phòng khám chuyên khoa đang mở rộng đón chờ. |

### scene02 · BỤNG ĐẦY KHÍ GAS · 251.1s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.1 (7.1s) | L40 | Bệnh nhân số một, mời vào bàn khám! Khỉ Đột Lưng Bạc, cân nặng 200 kg, cơ bắp cuồn cuộn như lực sĩ thể hình hạng nặng! |  | chú Khỉ Đột Lưng Bạc hoạt hình cơ bắp cuồn cuộn vạm vỡ, mảng lông bạc sáng chói dọc sống lưng, bụng to tròn căng phồng vì chứa đầy lá cây lên men, ngồi xếp bằng trên giường bệnh ôm bụng thở dài ngồi trên giường bệnh khám inox, cơ bắp cánh tay to như cột nhà nổi gân cuồn cuộn, nhưng hai tay lại ôm cái bụng phình to vẻ mặt mếu máo; ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án |
| b02 | 00:07.1–00:14.0 (6.9s) | L41 | Tôi nhìn vào các chỉ số thể chất ghi trên phiếu tiếp nhận mà không khỏi trầm trồ trước sức mạnh phi thường của loài linh trưởng vĩ đại này. |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án cầm bảng theo dõi chỉ số sinh tồn, ngước nhìn khối cơ bắp vai đồ sộ của chú khỉ đột đang ngồi co ro trên giường. |
| b03 | 00:14.0–00:21.8 (7.9s) | L42 | Theo các nghiên cứu cơ sinh học hiện đại, một cú đấm toàn lực của một con khỉ đột đực trưởng thành có lực tác động lên tới 1300 kg! |  | Bức tranh giải phẫu cơ xương tay của khỉ đột với các bó cơ delta và cơ nhị đầu đồ sộ chịu lực va đập cực đại; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b04 | 00:21.8–00:28.8 (7.0s) | L43 | Lực va chạm khủng khiếp đó thừa sức làm bẹp dúm phần đầu của một chiếc xe hơi 4 chỗ hoặc bẻ gãy một thân cây gỗ lim trong nháy mắt! |  | Hình ảnh mô phỏng cú đấm uy lực của khỉ đột làm nứt toác tấm bia thử nghiệm lực cơ học trong phòng thí nghiệm; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b05 | 00:28.8–00:36.6 (7.8s) | L44 | Xương khớp tay chân của khỉ đột dày gấp 3 lần xương người, mật độ khoáng chất cao đến mức gần như miễn nhiễm với các chấn thương gãy xương thông thường. |  | Bản chụp X-quang xương cẳng tay của khỉ đột sáng trắng cho thấy cấu trúc vỏ xương đặc quánh và các khớp nối vững chãi; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b06 | 00:36.6–00:43.6 (6.9s) | L45 | Thế nhưng hiện tại, cỗ máy chiến đấu vô địch của những cánh rừng mưa nhiệt đới này lại đang nằm co quắp rên rỉ như một đứa trẻ con! |  | chú Khỉ Đột Lưng Bạc hoạt hình cơ bắp cuồn cuộn vạm vỡ, mảng lông bạc sáng chói dọc sống lưng, bụng to tròn căng phồng vì chứa đầy lá cây lên men, ngồi xếp bằng trên giường bệnh ôm bụng thở dài nằm nghiêng trên giường bệnh, ôm hai đầu gối vào ngực, miệng thở hắt ra từng hơi vẻ bất lực; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b07 | 00:43.6–00:49.1 (5.6s) | L46 | Gương mặt nhăn nhó tội nghiệp của chú khỉ đột to lớn làm cô y tá vừa buồn cười vừa thương cảm vô cùng! |  | Cận cảnh gương mặt nhiều nếp nhăn của chú khỉ đột đang chớp mắt cầu cứu bác sĩ trưởng khoa; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b08 | 00:49.1–00:55.9 (6.8s) | L47 | Y tá, đặt ống nghe vào góc phần tư ổ bụng bên phải cho tôi! Cẩn thận kẻo anh chàng giật mình lại tung một đòn thì bay cả phòng khám đấy! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án ấn đầu ống nghe kim loại lạnh ngắt vào bụng khỉ đột, mắt chăm chú lắng nghe từng tiếng động bên trong. |
| b09 | 00:55.9–00:59.9 (4.0s) | L48 | Tôi áp đầu ống nghe vào lớp da bụng dày cộp căng tròn như chiếc trống đồng của bệnh nhân. |  | Cận cảnh đầu ống nghe y tế bằng kim loại sáng loáng áp sát vào lớp da lông đen nhánh của khỉ đột; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b10 | 00:59.9–01:06.8 (6.9s) | L49 | Âm thanh truyền vào tai tôi không phải tiếng sôi ruột bình thường, mà là tiếng ùng ục ùng ục rền vang như một lò phản ứng hóa học đang sôi sục! |  | Hình ảnh đồ họa mô phỏng bên trong ổ bụng khỉ đột với chiếc manh tràng khổng lồ đang sủi bọt khí gas liên hồi; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b11 | 01:06.8–01:11.2 (4.4s) | L50 | Cảm giác như có một cơn lốc xoáy khí gas đang cuộn trào bên trong đường ruột của anh chàng lực sĩ |  | Đồ họa sóng âm thanh hiển thị các dao động áp suất khí gas tăng vọt liên hồi trong khoang bụng bệnh nhân; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b12 | 01:11.2–01:16.2 (5.0s) | L51 | này vậy! Tôi lập tức cho chụp X-quang ổ bụng toàn phần để tìm ra nguyên nhân gốc rễ của cơn đau quằn quại này. |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án bấm nút điều khiển máy chụp X-quang kỹ thuật số công suất lớn quét qua toàn bộ thân hình đồ sộ của khỉ đột. |
| b13 | 01:16.2–01:22.0 (5.8s) | L52 | Và kết quả trên tấm phim rọi sáng làm cả phòng cấp cứu phải trố mắt kinh ngạc vì sự đồ sộ của hệ thống tiêu hóa bên trong! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án kẹp tấm phim X-quang to bản lên hộp đèn sáng trắng trên tường, chỉ tay vào vùng khoang bụng khổng lồ chứa đầy bóng khí. |
| b14 | 01:22.0–01:28.7 (6.7s) | L53 | Bác sĩ ơi, cái bụng anh này chứa toàn là khí gas! Có phải anh ấy ăn nhầm thuốc nổ hay ăn trúng nấm độc gì trong rừng sâu không ạ? |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng đứng bên cạnh nhìn tấm phim X-quang, hai tay ôm má hốt hoảng kêu lên. |
| b15 | 01:28.7–01:34.2 (5.5s) | L54 | Nhìn tấm phim chụp mà em tưởng như đang nhìn vào một quả bóng bay khí cầu khổng lồ sắp nổ tung tới nơi rồi bác sĩ ơi! |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng run run chỉ ngón tay vào những khoảng sáng rực của các túi khí gas phân bố khắp ổ bụng khỉ đột; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b16 | 01:34.2–01:38.7 (4.4s) | L55 | Em có nên chuẩn bị một chiếc kim chọc hút khí màng bụng để giải áp ngay bây giờ không ạ? |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng cầm chiếc kim tiêm dài vẻ lo lắng ngước nhìn bác sĩ trưởng khoa xin ý kiến; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b17 | 01:38.7–01:44.3 (5.7s) | L56 | Tuyệt đối không được chọc kim vào bụng bệnh nhân cô y tá nhé! Không hề có chất độc hay thuốc nổ nào ở đây cả! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười lắc đầu, quay lại vỗ nhẹ vào vai bệnh nhân khỉ đột đang lo lắng. |
| b18 | 01:44.3–01:49.2 (4.8s) | L57 | Đây chính là bí mật sinh học vĩ đại nhất của loài khỉ đột mà sách giáo khoa ít khi nhắc tới! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án tháo kính mắt, dùng khăn lau nhẹ rồi hướng dẫn các bác sĩ nội trú quan sát cấu trúc đường ruột trên phim chụp. |
| b19 | 01:49.2–01:56.6 (7.4s) | L58 | Anh chàng này không hề bị ngộ độc dạ dày, mà ổ bụng của anh ấy thực chất là một nhà máy lên men vi sinh vật ruột sau khổng lồ hoạt động ngày đêm! |  | Sơ đồ sinh học minh họa đường tiêu hóa của khỉ đột, nổi bật là phần manh tràng phình đại gấp nhiều lần so với con người; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b20 | 01:56.6–02:04.5 (8.0s) | L59 | Hãy nhìn vào chế độ ăn uống hàng ngày của loài khỉ đột trong tự nhiên mà xem: một thực đơn làm bất kỳ loài động vật ăn thịt nào cũng phải lắc đầu lè lưỡi! |  | Bức tranh miêu tả rừng mưa rậm rạp nhiệt đới châu Phi, nơi bầy khỉ đột đang thong thả hái lượm thức ăn giữa thảm thực vật hoang sơ; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b21 | 02:04.5–02:12.3 (7.8s) | L60 | Hàng ngày, một con khỉ đột lưng bạc trưởng thành phải nạp vào cơ thể tới 20-30 kg lá cây, vỏ cây, thân cây tầm ma và cành non xơ cứng. |  | chú Khỉ Đột Lưng Bạc hoạt hình cơ bắp cuồn cuộn vạm vỡ, mảng lông bạc sáng chói dọc sống lưng, bụng to tròn căng phồng vì chứa đầy lá cây lên men, ngồi xếp bằng trên giường bệnh ôm bụng thở dài ngồi giữa một đống lá cây rừng to như ngọn đồi nhỏ, nhồm nhoàm nhai từng bó lá xơ ráp đầy ngon lành; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b22 | 02:12.3–02:20.0 (7.7s) | L61 | Đặc biệt là những cây tầm ma có đầy gai châm chứa độc tố histamine và axit formic gây ngứa rát buốt da người, nhưng chú khỉ đột lại nhai ngấu nghiến ngon |  | Cận cảnh hàm răng khỉ đột nhai nát những nhánh cây tầm ma đầy lông ngứa mà niêm mạc miệng không hề bị sưng tấy tổn thương; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b23 | 02:20.0–02:28.1 (8.1s) | L62 | lành! Bởi vì tuyến nước bọt của khỉ đột tiết ra các enzym đặc biệt có tính kiềm cao, nhanh chóng trung hòa toàn bộ các phân tử độc tố gây bỏng rát trước khi lá trôi xuống dạ |  | Sơ đồ tuyến nước bọt khỉ đột giải phóng dòng enzym trung hòa màu xanh bảo vệ lớp niêm mạc thực quản; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b24 | 02:28.1–02:34.4 (6.3s) | L63 | dày! Hệ tiêu hóa thông thường của con người hay các loài ăn quả hoàn toàn bất lực trước lượng chất xơ thô cellulose khổng lồ và dai nhách |  | Kính hiển vi quang học phóng đại cấu trúc sợi cellulose cứng như sợi thép đan xen chằng chịt trong phiến lá cây; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b25 | 02:34.4–02:41.1 (6.7s) | L64 | này. Nếu chúng ta ăn đống lá cây xơ xác đó vào bụng, dạ dày sẽ bị thủng hoặc tắc ruột ngay lập tức vì không thể tiêu hóa nổi! |  | Hình ảnh so sánh dạ dày đơn giản của người với đường ruột đồ sộ dài ngoằng của khỉ đột; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b26 | 02:41.1–02:48.2 (7.1s) | L65 | Nhưng tạo hóa đã trang bị cho khỉ đột một chiếc manh tràng và đại tràng với dung tích khổng lồ, chứa hàng nghìn tỷ vi khuẩn kỵ khí chuyên biệt! |  | Cận cảnh các cụm vi khuẩn đường ruột có ích màu xanh ngọc bích đang bám quanh các sợi lá và phân hủy cellulose; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b27 | 02:48.2–02:55.1 (6.9s) | L66 | Các vi khuẩn cộng sinh này làm việc miệt mài ngày đêm để bẻ gãy các liên kết phân tử cellulose cứng rắn nhất thành các hợp chất đơn giản hơn. |  | Minh họa các enzym vi sinh vật cắt đứt các chuỗi phân tử đường phức tạp trong thành tế bào thực vật; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b28 | 02:55.1–03:01.9 (6.9s) | L67 | Thời gian lưu chuyển thức ăn trong đại tràng của khỉ đột kéo dài từ 35-40 giờ liên tục, đủ để vi khuẩn phân giải triệt để từng sợi xơ |  | bảng kẹp bệnh án y khoa khổng lồ (clipboard) kẹp trên giá đỡ kim loại, hiển thị 10 hồ sơ bệnh án hoạt hình với nhãn đơn thuốc phát sáng và sóng nhịp tim ECG màu đỏ nhấp nháy (không có chữ, không có số) hiển thị con số 40 giờ lưu chuyển thức ăn cùng sơ đồ đường ruột dài gấp sáu lần chiều dài cơ thể; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b29 | 03:01.9–03:09.6 (7.6s) | L68 | thực vật! Quá trình lên men vi sinh vật tự nhiên này giải phóng ra một lượng khí gas khổng lồ, đồng thời tổng hợp nên các axit béo chuỗi ngắn cực kỳ giàu năng lượng! |  | Đồ họa hóa học hiển thị các phân tử axit béo chuỗi ngắn acetate và propionate phát sáng vàng kim hấp thu qua thành ruột; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b30 | 03:09.6–03:17.2 (7.6s) | L69 | Nghiên cứu dinh dưỡng đột phá trong công trình khoa học nổi tiếng của tiến sĩ Popovich trên Tạp Chí Dinh Dưỡng học đã chứng minh một sự thật chấn động toàn cầu: |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án giơ bản báo cáo khoa học của tiến sĩ Popovich lên trước ánh đèn, chỉ vào bảng số liệu phân tích calo đường ruột. |
| b31 | 03:17.2–03:23.8 (6.6s) | L70 | Tới 70% tổng năng lượng calo mỗi ngày của khỉ đột không đến từ đường hay tinh bột, mà đến từ chính quá trình lên men chất xơ này! |  | bảng kẹp bệnh án y khoa khổng lồ (clipboard) kẹp trên giá đỡ kim loại, hiển thị 10 hồ sơ bệnh án hoạt hình với nhãn đơn thuốc phát sáng và sóng nhịp tim ECG màu đỏ nhấp nháy (không có chữ, không có số) bật sáng dòng chữ số 70% calo phát sáng rực rỡ bên cạnh biểu tượng chiếc lá cây biến thành năng lượng cơ bắp; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b32 | 03:23.8–03:30.9 (7.1s) | L71 | Các axit béo chuỗi ngắn sau khi lên men được hấp thu trực tiếp qua thành đại tràng, đi thẳng vào máu và nuôi dưỡng toàn bộ khối cơ bắp khổng lồ của con vật! |  | Dòng năng lượng màu vàng ánh kim từ thành ruột lan tỏa khắp các bó cơ bắp cuồn cuộn trên lưng và cánh tay khỉ đột; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b33 | 03:30.9–03:37.3 (6.4s) | L72 | Chúng hoạt động tương tự như loài bò hay ngựa, nhưng thay vì lên men ở dạ cỏ phía trước thì khỉ đột lên men ở ruột sau vô cùng tinh vi! |  | Sơ đồ so sánh cơ chế lên men dạ cỏ của bò với cơ chế lên men ruột sau của khỉ đột; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b34 | 03:37.3–03:44.7 (7.4s) | L73 | Nói cách khác, cái bụng bự phình to của anh chàng không phải là mỡ thừa lười biếng, mà là một cỗ máy sinh học siêu đẳng biến cỏ rác thành cơ bắp cuồn cuộn! |  | chú Khỉ Đột Lưng Bạc hoạt hình cơ bắp cuồn cuộn vạm vỡ, mảng lông bạc sáng chói dọc sống lưng, bụng to tròn căng phồng vì chứa đầy lá cây lên men, ngồi xếp bằng trên giường bệnh ôm bụng thở dài đứng dậy ưỡn ngực đấm thùm thụp vào ngực khoe cơ bắp rắn chắc, bụng phình to đầy tự hào; ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười gật đầu tán thưởng. |
| b35 | 03:44.7–03:51.7 (7.0s) | L74 | Nhưng hôm nay, do ăn hơi nhiều mầm tre non lên men nhanh vào buổi chiều nên lượng khí gas sinh ra quá mức làm căng tức thành bụng tạm thời |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án cười xòa, giải thích cặn kẽ cho chú khỉ đột đang lắng nghe từng lời của bác sĩ. |
| b36 | 03:51.7–03:58.6 (6.9s) | L75 | mà thôi! Được rồi anh bạn cơ bắp, tôi kê đơn cho anh 2 viên men tiêu hóa thảo dược và một tách trà gừng ấm để tống bớt lượng khí thừa ra ngoài |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án xé một tờ đơn thuốc nhỏ đưa cho chú Khỉ Đột Lưng Bạc hoạt hình cơ bắp cuồn cuộn vạm vỡ, mảng lông bạc sáng chói dọc sống lưng, bụng to tròn căng phồng vì chứa đầy lá cây lên men, ngồi xếp bằng trên giường bệnh ôm bụng thở dài, anh chàng khỉ đột mừng rỡ nhận lấy rồi cúi đầu cảm ơn rối rít. |
| b37 | 03:58.6–04:03.7 (5.1s) | L76 | nhé! Chỉ cần ợ hơi vài tiếng sấm sét là anh lại có thể đấm vỡ đá và vỗ ngực vang rền khắp thảo nguyên được |  | Chú chú Khỉ Đột Lưng Bạc hoạt hình cơ bắp cuồn cuộn vạm vỡ, mảng lông bạc sáng chói dọc sống lưng, bụng to tròn căng phồng vì chứa đầy lá cây lên men, ngồi xếp bằng trên giường bệnh ôm bụng thở dài uống cạn cốc nước ấm y tá đưa, phát ra một tiếng ợ hơi trầm đục làm rung rinh cả rèm cửa phòng khám trong tiếng cười vui vẻ. |
| b38 | 04:03.7–04:11.1 (7.4s) | L77 | rồi! Ca cấp cứu số một của Phòng Cấp Cứu Tạo Hóa hoàn thành xuất sắc! Giờ thì y tá, chuyển ngay hồ sơ ca số 2 sang Khoa Hô Hấp Ngược cho tôi! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đóng sập tập bệnh án số một lại, bước nhanh sang phòng khám chuyên khoa bên cạnh. |

### scene03 · BÌNH DƯỠNG KHÍ TỰ DỆT · 253.3s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:04.3 (4.3s) | L78 | Cánh cửa phòng khám Khoa Hô Hấp Ngược mở ra với một bầu không khí ẩm ướt lạ thường. |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đẩy cửa bước vào phòng khám hô hấp có các bồn nước và ống dẫn oxy, cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng đang đứng bối rối bên cạnh một chiếc chậu thủy tinh trong suốt. |
| b02 | 00:04.3–00:10.3 (5.9s) | L79 | Và bệnh nhân số 2 đang nằm trong một tình huống dở khóc dở cười nhất từ trước tới nay trong lịch sử cấp cứu của chúng tôi. |  | Khung cảnh căn phòng khám chuyên khoa với các bình dưỡng khí cao áp xếp hàng, nhưng giữa bàn khám lại là một chậu nước đầy rong rêu; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b03 | 00:10.3–00:16.3 (6.1s) | L80 | Chú Nhện Lặn Chuông tí hon dài chưa đầy 2 cm đang dùng hết sức bình sinh để trốn khỏi chiếc mặt nạ thở oxy nhi khoa! |  | Cận cảnh chú Nhện Lặn Chuông (diving bell spider) hoạt hình màu nâu đen nhiều lông mịn, tám chân ôm một chiếc bóng khí lấp lánh như viên ngọc trong suốt dưới bụng, đang ngâm mình trong bể nước dã chiến màu nâu đen tám chân thoăn thoắt bò qua mép chiếc mặt nạ dưỡng khí mini, lao thẳng vào làn nước trong veo; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b04 | 00:16.3–00:22.1 (5.7s) | L81 | Mỗi lần cô y tá đưa chiếc ống thở tới gần mũi, chú nhện lại cắn phăng một nhát rồi lặn một hơi mất tăm xuống tận đáy |  | chú Nhện Lặn Chuông (diving bell spider) hoạt hình màu nâu đen nhiều lông mịn, tám chân ôm một chiếc bóng khí lấp lánh như viên ngọc trong suốt dưới bụng, đang ngâm mình trong bể nước dã chiến bơi thoăn thoắt xuống đáy chậu, chui tọt vào giữa đám rong đuôi chó xanh biếc, giương tám chiếc mắt nhỏ xíu nhìn lên vẻ đề phòng; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b05 | 00:22.1–00:29.1 (7.1s) | L82 | chậu nước! Chiếc đuôi nhỏ xíu của nó khẽ lắc lư, để lộ một vầng hào quang lấp lánh như viên ngọc trai bọc quanh phần bụng dưới làn nước trong vắt. |  | Cận cảnh bọt khí tròn xoe ôm lấy phần bụng của chú nhện lặn chuông dưới đáy chậu nước; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b06 | 00:29.1–00:36.1 (7.0s) | L83 | Bác sĩ ơi em chụp mặt nạ oxy vào mặt nó mà nó cứ cắn đứt dây rồi nhảy xuống nước! Con nhện này bị trầm cảm muốn tự vẫn hay sao ấy ạ? |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng giơ sợi dây thở oxy bị cắn cụt lủn lên, vẻ mặt vừa thương cảm vừa bất lực tột cùng. |
| b07 | 00:36.1–00:42.2 (6.1s) | L84 | Em vớt nó lên thở không khí bình thường thì nó cứ nằm đờ đẫn ra, thế mà vừa thả vào nước là nó bơi nhanh như một chiếc tàu ngầm mini! |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng chỉ tay vào chậu nước, nơi chú nhện đang bơi lội tung tăng như cá cảnh giữa đàn rong xanh; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b08 | 00:42.2–00:46.4 (4.2s) | L85 | Có khi nào con nhện này bị đột biến gen thành loài cá không bác sĩ ơi? |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng ngước nhìn bác sĩ với đôi mắt thỏ tròn xoe ngây thơ; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b09 | 00:46.4–00:53.4 (7.0s) | L86 | Bình tĩnh nào cô y tá! Nó không hề muốn tự vẫn đâu, mà chúng ta đang ép một thợ lặn chuyên nghiệp thở theo cách của người đi bộ trên cạn |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án bật cười bước tới bên bình nước, cúi sát mặt quan sát từng cử động tinh vi của chú nhện dưới làn nước trong vắt. |
| b10 | 00:53.4–01:00.5 (7.1s) | L87 | đấy! Đây là loài nhện duy nhất trong số hơn 50.000 loài nhện đã được phát hiện trên Trái Đất dành toàn bộ cuộc đời của mình dưới đáy nước |  | chú Nhện Lặn Chuông (diving bell spider) hoạt hình màu nâu đen nhiều lông mịn, tám chân ôm một chiếc bóng khí lấp lánh như viên ngọc trong suốt dưới bụng, đang ngâm mình trong bể nước dã chiến bơi lội uyển chuyển giữa các nhánh rong xanh biếc, thân mình phủ một lớp ánh bạc lấp lánh như được dát kim loại; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b11 | 01:00.5–01:07.9 (7.4s) | L88 | ngọt! Nó sinh ra dưới nước, săn mồi dưới nước, giao phối dưới nước, đẻ trứng dưới nước và thậm chí ngủ đông cũng ở dưới đáy bùn |  | Hình ảnh một chú nhện lặn chuông đang bắt một ấu trùng muỗi nước dưới đáy hồ trong suốt; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b12 | 01:07.9–01:15.7 (7.8s) | L89 | nước! Thế nhưng về mặt nguồn gốc giải phẫu, nhện lặn chuông vẫn là một loài chân khớp thở bằng phổi sách và hệ thống ống khí quản trên cạn. |  | Sơ đồ giải phẫu hiển vi của nhện hiển thị hệ thống phổi sách và các lỗ thở nhỏ li ti xếp dọc hai bên bụng; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b13 | 01:15.7–01:22.4 (6.7s) | L90 | Nghĩa là nó bắt buộc phải hít thở khí oxy dạng phân tử tự do trong không khí chứ mang của nó hoàn toàn không thể lọc oxy hòa tan như loài cá! |  | Hình vẽ so sánh lá mang của cá với hệ thống phổi sách nhiều nếp gấp của nhện lặn chuông; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b14 | 01:22.4–01:28.0 (5.6s) | L91 | Vậy làm thế nào mà một sinh vật thở bằng không khí lại có thể sống cả đời dưới nước mà không hề bị chết đuối? |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án khoanh tay trước ngực, đặt câu hỏi đầy gợi mở nhìn về phía các bác sĩ nội trú đang vây quanh bàn khám. |
| b15 | 01:28.0–01:34.4 (6.3s) | L92 | Câu trả lời nằm ở một phát minh công nghệ nano sinh học độc nhất vô nhị mà loài nhện này đã hoàn thiện qua hàng triệu 5 tiến hóa! |  | Kính hiển vi điện tử quét phóng đại hàng triệu sợi lông tơ nano có cấu trúc rãnh khía đặc biệt đẩy lùi các phân tử nước; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b16 | 01:34.4–01:40.2 (5.8s) | L93 | Toàn bộ vùng bụng và các kẽ chân của nhện lặn chuông được bao phủ bởi hàng triệu sợi lông kỵ nước siêu nhỏ với mật độ dày đặc phi |  | Các sợi lông nano xếp nghiêng góc chính xác, tạo ra một sức căng bề mặt cực lớn ngăn không cho các phân tử nước chạm vào lớp da bụng; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b17 | 01:40.2–01:45.9 (5.7s) | L94 | thường. Mỗi khi cần dưỡng khí, chú nhện chỉ việc nhô phần đuôi lên khỏi mặt nước trong đúng 1/10 giây rồi lặn nhanh |  | chú Nhện Lặn Chuông (diving bell spider) hoạt hình màu nâu đen nhiều lông mịn, tám chân ôm một chiếc bóng khí lấp lánh như viên ngọc trong suốt dưới bụng, đang ngâm mình trong bể nước dã chiến ngoi phần chóp bụng lên mặt nước trong chớp mắt rồi lặn nhanh xuống, kéo theo một khối bong bóng khí tròn xoe; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b18 | 01:45.9–01:53.9 (8.0s) | L95 | xuống. Lớp lông kỵ nước lập tức bẫy chặt một lớp màng không khí bao quanh toàn bộ cơ thể, biến con nhện thành một thợ lặn bọc trong một chiếc áo giáp khí óng ánh như bạc! |  | Cơ thể chú nhện phát sáng lung linh dưới nước nhờ lớp bọt khí bạc bao phủ toàn thân như một bộ đồ lặn vũ trụ mini; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b19 | 01:53.9–02:02.7 (8.7s) | L96 | Hai chiếc chân sau của nó được cấu tạo như những chiếc bàn chải chuyên dụng, thường xuyên chải chuốt các sợi lông để loại bỏ cặn bẩn bám dính, giữ cho lớp áo giáp khí luôn thông thoáng! |  | Chú chú Nhện Lặn Chuông (diving bell spider) hoạt hình màu nâu đen nhiều lông mịn, tám chân ôm một chiếc bóng khí lấp lánh như viên ngọc trong suốt dưới bụng, đang ngâm mình trong bể nước dã chiến dùng hai chân sau vuốt ve các sợi lông trên bụng một cách tỉ mỉ để duy trì sức căng bề mặt tối ưu; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b20 | 02:02.7–02:08.3 (5.7s) | L97 | Không chỉ dừng lại ở chiếc áo giáp khí di động đó, con nhện còn tiến hành xây dựng cả một căn cứ quân sự ngầm dưới đáy hồ! |  | Chú chú Nhện Lặn Chuông (diving bell spider) hoạt hình màu nâu đen nhiều lông mịn, tám chân ôm một chiếc bóng khí lấp lánh như viên ngọc trong suốt dưới bụng, đang ngâm mình trong bể nước dã chiến bắt đầu kéo những sợi tơ trong suốt đan dệt giữa hai nhánh rong rêu thủy sinh; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b21 | 02:08.3–02:13.9 (5.5s) | L98 | Kỳ quan thực sự nằm ở chiếc chuông lặn mà chú nhện dệt nên dưới đáy hồ bằng chính những sợi tơ chuyên dụng của mình! |  | Dưới đáy nước, chiếc chuông lặn bằng tơ nhện hình chiếc chuông úp ngược phát sáng trắng bạc, chứa đầy không khí trong suốt; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b22 | 02:13.9–02:21.0 (7.2s) | L99 | Nó nhả ra những sợi tơ nhện không thấm nước đặc biệt, đan kết chúng thành một mái vòm hình chiếc chuông úp ngược neo chặt vào các thân rong rêu thủy sinh. |  | Chú chú Nhện Lặn Chuông (diving bell spider) hoạt hình màu nâu đen nhiều lông mịn, tám chân ôm một chiếc bóng khí lấp lánh như viên ngọc trong suốt dưới bụng, đang ngâm mình trong bể nước dã chiến thoăn thoắt dùng các chân sau dệt từng đường tơ trắng muốt đan xen chằng chit thành một mạng lưới vô cùng bền chắc; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b23 | 02:21.0–02:27.4 (6.4s) | L100 | Sau đó, nhện liên tục ngoi lên mặt nước, dùng bụng vận chuyển từng bọt khí lớn lặn xuống nhả vào bên trong mái vòm tơ. |  | Từng bọt khí được nhả ra tích tụ dần bên dưới mái vòm, đẩy toàn bộ nước ra ngoài và biến chiếc vòm tơ thành một căn phòng chứa đầy không khí khô ráo; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b24 | 02:27.4–02:33.1 (5.7s) | L101 | Mái vòm tơ căng phồng lên như một quả bóng khí trong suốt, chú nhện thong thả chui vào bên trong ngồi nghỉ ngơi khô ráo! |  | chú Nhện Lặn Chuông (diving bell spider) hoạt hình màu nâu đen nhiều lông mịn, tám chân ôm một chiếc bóng khí lấp lánh như viên ngọc trong suốt dưới bụng, đang ngâm mình trong bể nước dã chiến ngồi vắt vẻo bên trong chiếc chuông lặn khô ráo, tám chân buông thõng thư giãn giữa làn nước sâu; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b25 | 02:33.1–02:39.4 (6.2s) | L102 | Và đây là điều kỳ diệu nhất mà nghiên cứu kinh điển của giáo sư Seymour công bố trên Tạp Chí Sinh Học Thực Nghiệm đã chứng minh: |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án giơ ngón tay chỉ lên màn hình hiển thị đồ thị nồng độ oxy hòa tan trong nước. |
| b26 | 02:39.4–02:47.2 (7.9s) | L103 | Chiếc chuông lặn bằng tơ này không chỉ là một cái kho chứa khí thụ động, mà nó hoạt động chính xác như một lá phổi vật lý hay một chiếc mang nhân tạo siêu việt! |  | Hình ảnh đồ họa mô phỏng các phân tử oxy hòa tan trong nước xung quanh tự động khuếch tán thẩm thấu qua màng tơ mỏng đi vào trong chuông; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b27 | 02:47.2–02:53.7 (6.4s) | L104 | Khi nhện tiêu thụ oxy bên trong chuông, nồng độ oxy trong chuông giảm xuống thấp hơn nồng độ oxy hòa tan trong nước xung quanh chiếc |  | Mũi tên đồ họa màu xanh lục mô phỏng dòng oxy tự động chảy ngược từ nước vào chuông qua chênh lệch áp suất; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b28 | 02:53.7–03:00.0 (6.3s) | L105 | chuông. Chênh lệch áp suất riêng phần này thúc đẩy các phân tử oxy từ nước tự động khuếch tán thẩm thấu xuyên qua màng tơ mỏng đi vào bên trong |  | Dòng dưỡng khí oxy liên tục được bổ sung tự động từ môi trường nước vào trong không gian sống của chú nhện; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b29 | 03:00.0–03:06.4 (6.4s) | L106 | chuông! Đồng thời, khí các-bô-níc độc hại do con nhện thở ra sẽ dễ dàng hòa tan và khuếch tán ngược ra ngoài dòng nước chảy xung quanh. |  | Các bọt khí CO2 màu xám li ti thẩm thấu xuyên qua lớp màng tơ trôi dạt ra ngoài dòng nước; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b30 | 03:06.4–03:12.7 (6.3s) | L107 | Nhờ cơ chế trao đổi khí thần kỳ đó, lượng oxy khuếch tán vào chuông có thể đáp ứng đủ nhu cầu hô hấp của chú nhện suốt hơn 24 giờ |  | bảng kẹp bệnh án y khoa khổng lồ (clipboard) kẹp trên giá đỡ kim loại, hiển thị 10 hồ sơ bệnh án hoạt hình với nhãn đơn thuốc phát sáng và sóng nhịp tim ECG màu đỏ nhấp nháy (không có chữ, không có số) hiển thị con số 24 giờ cùng biểu tượng đồng hồ cát phát sáng xanh bên cạnh chiếc chuông lặn; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b31 | 03:12.7–03:20.3 (7.6s) | L108 | liên tục! Con nhện có thể nằm ngủ say sưa, ăn thịt con mồi và chăm sóc bầy con non trong chiếc chuông lặn suốt cả ngày đêm mà không cần phải ngoi lên mặt nước một lần |  | Cảnh gia đình nhện lặn chuông sum vầy ấm cúng bên trong mái vòm khí sáng rực dưới đáy hồ trong vắt; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b32 | 03:20.3–03:26.8 (6.5s) | L109 | nào! Thậm chí chú nhện đực còn dệt chiếc chuông lặn lớn hơn con cái 30% để làm phòng tân hôn lãng mạn dưới đáy nước! |  | Hai chú nhện lặn chuông bơi lội quấn quýt bên nhau trong chiếc chuông lặn rộng rãi dưới làn nước trong xanh; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b33 | 03:26.8–03:34.8 (8.0s) | L110 | Vào mùa đông băng giá khi mặt hồ đóng băng dày đặc, nhện chỉ việc rút sâu xuống đáy bùn, gia cố chuông tơ thật kín và ngủ đông yên bình ở nhiệt độ 0°C! |  | Cảnh mặt hồ phủ băng tuyết trắng xóa, phía sâu dưới đáy bùn chú chú Nhện Lặn Chuông (diving bell spider) hoạt hình màu nâu đen nhiều lông mịn, tám chân ôm một chiếc bóng khí lấp lánh như viên ngọc trong suốt dưới bụng, đang ngâm mình trong bể nước dã chiến cuộn tròn ngủ say sưa bên trong chiếc chuông tơ ấm áp; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b34 | 03:34.8–03:42.9 (8.1s) | L111 | Lớp màng tơ nhện bảo vệ nó khỏi các tinh thể băng giá sắc nhọn và giữ cho áp suất dưỡng khí bên trong luôn ở mức ổn định suốt nhiều tháng ròng! |  | Lớp băng tuyết bao phủ bên trên nhưng chiếc chuông lặn dưới đáy bùn vẫn nguyên vẹn ấm áp như một chiếc kén sinh học kỳ diệu; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b35 | 03:42.9–03:50.0 (7.1s) | L112 | Thử hỏi có chiếc tàu ngầm hạt nhân hay bộ đồ lặn hiện đại nào của loài người có thể hoạt động bền bỉ và thông minh đến mức độ như thế này không? |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án nháy mắt cười hóm hỉnh nhìn toàn thể hội đồng y khoa đang gật gù thán phục. |
| b36 | 03:50.0–03:56.1 (6.1s) | L113 | Chẩn đoán Khoa Hô Hấp Ngược của Phòng Cấp Cứu Tạo Hóa: Bệnh nhân sở hữu hệ hô hấp dưới nước hiện đại và tiết kiệm năng lượng nhất hành |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án cất chiếc ống nghe vào túi áo, mỉm cười nhìn chú chú Nhện Lặn Chuông (diving bell spider) hoạt hình màu nâu đen nhiều lông mịn, tám chân ôm một chiếc bóng khí lấp lánh như viên ngọc trong suốt dưới bụng, đang ngâm mình trong bể nước dã chiến đang tung tăng bơi lượn trong bể nước mới. |
| b37 | 03:56.1–04:05.5 (9.4s) | L114 | tinh! Đơn thuốc cho bệnh nhân: một bể thủy tinh nước ngọt sâu 30 cm, bổ sung vài cành rong đuôi chó tươi ngon và tuyệt đối cấm dùng mặt nạ thở oxy! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án ký xoẹt một chữ ký sắc sảo vào bệnh án số hai, đưa cho y tá đi chuẩn bị chỗ nghỉ ngơi cho chú nhện. |
| b38 | 04:05.5–04:13.3 (7.8s) | L115 | Bệnh nhân số 2 đã tìm lại được bầu không khí quen thuộc! Giờ thì mời toàn đội di chuyển sang Khoa Chấn Thương Chỉnh Hình để đón tiếp một vận động viên điền kinh có vây! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án sải bước ra khỏi phòng khám hô hấp, hướng thẳng về phía phòng chỉnh hình đang có tiếng đập huỳnh huỵch ngoài cửa. |

### scene04 · VÂY BIẾN THÀNH CHÂN ĐIỀN KINH · 247.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:05.9 (5.9s) | L116 | Huỳnh huỵch! Bẹp bẹp bẹp! Tiếng đập sàn dồn dập vang lên ngay khi chúng tôi vừa mở cửa phòng khám Khoa Chấn Thương Chỉnh |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mở cửa bước vào, một bóng đen nhỏ xíu nhảy vèo qua đầu bác sĩ rồi đáp bẹp xuống chiếc bàn khám kim loại sáng bóng. |
| b02 | 00:05.9–00:09.5 (3.6s) | L117 | Hình! Và cảnh tượng trước mắt làm các bác sĩ ngoại khoa phải đứng hình trong kinh ngạc! |  | Căn phòng khám chỉnh hình với các nẹp xương và mô hình xương khớp, nhưng giữa phòng là một chú cá đang nhảy nhót tưng bừng; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b03 | 00:09.5–00:17.9 (8.4s) | L118 | Một chú Cá Thòi Lòi dài 20 cm, mình mẩy lấm lem bùn đất, đang dùng 2 chiếc vây ngực cơ bắp chống thẳng đứng trên mặt bàn như một lực sĩ đang hít đất! |  | Cận cảnh chú Cá Thòi Lòi hoạt hình màu nâu xám lấm chấm xanh ngọc, hai mắt to tròn lồi hẳn trên đỉnh đầu chớp chớp ngộ nghĩnh, hai vây ngực bè to như đôi tay đang chống nạng gỗ mini đòi nhảy khỏi cáng cứu thương da xám đốm hoa văn bùn lầy, hai vây ngực to bè như đôi tay lực lưỡng đang chống đỡ toàn bộ nửa thân trước; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b04 | 00:17.9–00:24.7 (6.8s) | L119 | Đôi mắt to tròn như 2 chiếc kính tiềm vọng nhô hẳn lên trên đỉnh đầu, xoay tít 300 6 mươi độ quét nhìn khắp lượt các bác sĩ trong phòng khám! |  | Đôi mắt lồi ngộ nghĩnh của cá thòi lòi xoay độc lập hai hướng, con ngươi đen láy chớp chớp đầy cảnh giác; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b05 | 00:24.7–00:31.7 (7.1s) | L120 | Cứ mỗi lần cô y tá cầm chiếc khăn ẩm tiến lại gần, chú cá lại quẫy đuôi một cú đánh tách, phóng bổng người lên không trung cao tới 60 cm! |  | Chú cá búng mạnh chiếc đuôi cơ bắp, bay bổng lên cao vượt qua đầu y tá rồi đáp xuống khay nhôm y tế kêu leng keng; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b06 | 00:31.7–00:39.0 (7.3s) | L121 | Bác sĩ ơi bắt nó lại giùm em với! Con cá này bị co giật động kinh hay bị gãy xương chậu mà nó cứ nhảy lung tung khắp phòng thế này ạ? |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng hai tay cầm chiếc vợt lưới y tế mini rượt đuổi chú cá quanh bàn khám, thở hổn hển mặt đỏ bừng bừng. |
| b07 | 00:39.0–00:45.1 (6.1s) | L122 | Nó là loài cá mà sao nó không chịu ở dưới nước, lại cứ thích leo lên bậc cửa sổ rồi leo lên bàn làm việc ngồi nhìn ra ngoài đường thế này? |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng chỉ tay lên gờ cửa sổ gỗ, nơi chú cá vừa nhảy tót lên bám chặt vào mép gỗ bằng giác hút ở bụng; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b08 | 00:45.1–00:49.4 (4.3s) | L123 | Có khi nào xương vây của nó bị biến dạng thành chân khỉ rồi không bác sĩ ơi? |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng tròn xoe mắt thỏ ngơ ngác nhìn chú cá đang trố mắt nhìn lại mình; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b09 | 00:49.4–00:58.2 (8.8s) | L124 | Hãy cất chiếc vợt lưới đi cô y tá! Đây không phải là cá bị co giật, mà là sinh vật chuyển tiếp vĩ đại nhất còn sống sót từ kỷ Devon cách đây gần 400 triệu 5! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án bật cười giơ tay ra hiệu cho y tá dừng lại, bước tới quan sát gần chú cá đang hiên ngang chống vây trên bàn. |
| b10 | 00:58.2–01:04.7 (6.5s) | L125 | Cá Thòi Lòi là loài cá lưỡng cư độc nhất vô nhị có thể dành tới 90% thời gian trong ngày sống hoàn toàn trên cạn! |  | chú Cá Thòi Lòi hoạt hình màu nâu xám lấm chấm xanh ngọc, hai mắt to tròn lồi hẳn trên đỉnh đầu chớp chớp ngộ nghĩnh, hai vây ngực bè to như đôi tay đang chống nạng gỗ mini đòi nhảy khỏi cáng cứu thương đứng hiên ngang trên bờ bùn đất ven rừng ngập mặn Cà Mau, xung quanh là những rễ cây đước ngoằn ngoèo nhô lên khỏi mặt nước; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b11 | 01:04.7–01:12.1 (7.4s) | L126 | Nó có thể đi bộ, chạy nước rút trên bùn lầy, trèo thoăn thoắt lên các rễ cây đước và thậm chí nhảy cao gấp 3 lần chiều dài cơ thể mình! |  | Chú cá thòi lòi dùng hai vây ngực bám vào rễ cây đước cao nửa mét trên mặt nước, ngẩng cao đầu đón gió biển; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b12 | 01:12.1–01:20.4 (8.3s) | L127 | Hãy nhìn vào cấu trúc giải phẫu của 2 chiếc vây ngực này trên phim chụp X-quang: Đây chính là tiền thân của đôi cánh tay và đôi chân động vật 4 chân trên cạn! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án bật đèn soi phim X-quang, chỉ vào các khớp xương vây ngực có cấu trúc xương cánh tay và xương quay nguyên thủy. |
| b13 | 01:20.4–01:28.1 (7.7s) | L128 | Các xương vây ngực đã tiến hóa thành các khớp xương trục có cơ bắp khỏe khoắn nâng đỡ, hoạt động tương tự như khuỷu tay và cổ tay của động vật trên cạn! |  | Sơ đồ giải phẫu ba chiều hiển thị bó cơ bắp dày đặc liên kết giữa xương bả vai nguyên thủy và các tia vây biến tính của cá thòi lòi; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b14 | 01:28.1–01:33.7 (5.6s) | L129 | Hai vây bụng của nó hợp nhất lại ở phía dưới tạo thành một giác hút hình chiếc cốc vô cùng chắc chắn! |  | Cận cảnh mặt bụng của cá thòi lòi với giác hút tròn xoe giúp nó bám chặt như keo dính vào các thân cây trơn trượt; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b15 | 01:33.7–01:41.4 (7.7s) | L130 | Vào mùa giao phối, các chàng cá đực còn dựng đứng chiếc vây lưng sặc sỡ như một cánh buồm ngũ sắc, nhảy múa tưng bừng trên bãi bùn để thu hút bạn tình! |  | Chú cá thòi lòi đực xòe chiếc vây lưng màu xanh lam viền đỏ rực rỡ, uốn lượn nhảy múa giữa thảm bùn rừng đước; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b16 | 01:41.4–01:48.7 (7.3s) | L131 | Nhưng bí ẩn lớn nhất khiến các nhà sinh lý học hô hấp phải kinh ngạc là: Làm thế nào một con cá có thể thở trên cạn suốt nhiều giờ liền mà không bị ngạt thở? |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đưa ngón tay trỏ nhẹ nhàng nâng phần nắp mang phồng to của chú cá lên để kiểm tra. |
| b17 | 01:48.7–01:56.2 (7.5s) | L132 | Bởi vì mang cá thông thường khi lên cạn sẽ bị khô ráp, các phiến mang dính bết lại với nhau làm mất diện tích tiếp xúc với không khí và con cá sẽ chết ngạt nhanh chóng! |  | Hình ảnh so sánh lá mang cá bình thường bị bết dính trên cạn với khoang mang phồng tròn căng mọng của cá thòi lòi; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b18 | 01:56.2–02:01.8 (5.6s) | L133 | Thế nhưng cá thòi lòi lại sở hữu 2 khoang mang khổng lồ có van đóng mở kín mít như 2 chiếc bình dưỡng khí của |  | Sơ đồ giải phẫu khoang mang của cá thòi lòi hiển thị van cơ vòng đóng chặt giữ lại một lượng nước biển giàu oxy bên trong; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b19 | 02:01.8–02:07.9 (6.1s) | L134 | thợ lặn! Trước khi rời khỏi mặt nước để bò lên bãi bùn, nó ngậm đầy một họng nước và không khí rồi siết chặt van nắp mang lại! |  | Chú chú Cá Thòi Lòi hoạt hình màu nâu xám lấm chấm xanh ngọc, hai mắt to tròn lồi hẳn trên đỉnh đầu chớp chớp ngộ nghĩnh, hai vây ngực bè to như đôi tay đang chống nạng gỗ mini đòi nhảy khỏi cáng cứu thương ngụp đầu xuống nước hút căng khoang miệng rồi bò lên bãi bùn với hai bên má phồng to như hai quả bóng bàn; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b20 | 02:07.9–02:14.7 (6.7s) | L135 | Bằng cách đó, các phiến mang bên trong luôn luôn được ngâm ngập trong nước giàu dưỡng khí, cho phép nó hô hấp bình thường ngay giữa bãi cạn khô khốc! |  | Hình ảnh minh họa các tia nước giàu oxy luân chuyển liên tục bên trong khoang mang kín mít nuôi dưỡng các tế bào; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b21 | 02:14.7–02:18.8 (4.2s) | L136 | Chưa hết đâu nhé! Cá thòi lòi còn có khả năng hô hấp qua da và niêm mạc miệng cực kỳ |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án dùng kính lúp soi lớp da nhầy bóng loáng phủ đầy các mao mạch nước màu li ti của chú cá. |
| b22 | 02:18.8–02:25.1 (6.3s) | L137 | tinh vi! Hơn 50% lượng oxy của nó được hấp thu trực tiếp qua lớp da mỏng giàu mạch máu, miễn là da của nó luôn được giữ ẩm |  | Sơ đồ mạng lưới mao mạch nước màu dày đặc nằm ngay dưới lớp biểu bì da cá thòi lòi đang hấp thu các phân tử oxy tự do từ không khí; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b23 | 02:25.1–02:31.2 (6.1s) | L138 | ướt! Đó là lý do tại sao anh chàng này thỉnh thoảng lại lăn lộn trên bùn nhão để tráng một lớp bùn bảo vệ giữ ẩm cho làn da của |  | Chú cá thòi lòi thích thú nằm lăn qua lăn lại trên lớp bùn mịn màng như đang tắm bùn khoáng spa; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b24 | 02:31.2–02:34.9 (3.6s) | L139 | mình! Và các bạn hãy nhìn vào đôi mắt kỳ diệu nhô cao trên đỉnh đầu của nó mà |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án chỉ đầu bút vào đôi mắt lồi to tướng đang chớp chớp liên hồi của chú cá. |
| b25 | 02:34.9–02:40.8 (5.9s) | L140 | xem! Đó là 2 chiếc kính tiềm vọng thực thụ giúp nó vừa ngâm mình dưới nước vừa quan sát được toàn bộ con mồi và kẻ thù trên |  | Hình ảnh chú cá ẩn mình dưới nước chỉ để lộ hai con mắt nhô lên khỏi mặt bùn quan sát xung quanh; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b26 | 02:40.8–02:49.3 (8.6s) | L141 | cạn! Mỗi khi mắt bị khô do gió biển, cá thòi lòi chỉ việc thụt 2 mắt vào trong hốc đầu, nơi có một túi nước đặc biệt để rửa sạch và cấp ẩm cho giác mạc rồi lại đẩy mắt nhô |  | Đồ họa chuyển động chậm mô phỏng mắt cá thụt xuống hốc nước dưới đáy mắt để chớp mắt rồi bật ngược trở lại; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b27 | 02:49.3–02:54.7 (5.3s) | L142 | lên! Thật là một cơ chế chớp mắt độc nhất vô nhị không hề giống bất kỳ loài động vật có xương sống nào trên Trái |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án thích thú dùng đèn soi phản xạ giác mạc của chú cá đang thụt mắt xuống hốc nước rồi đẩy lên đầy ngộ nghĩnh. |
| b28 | 02:54.7–03:01.2 (6.5s) | L143 | Đất! Cá thòi lòi còn có một tập tính kỳ lạ là trèo lên các thân cây đước cao để phơi nắng và tránh thủy triều dâng cao cuốn trôi! |  | Chú cá thòi lòi dùng vây ngực khỏe khoắn bám chặt vào thân cây đước, leo thoăn thoắt lên cao như một chú thằn lằn; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b29 | 03:01.2–03:07.4 (6.2s) | L144 | Vào mùa sinh sản, những chú cá thòi lòi đực còn đào những chiếc hang bùn sâu tới 1,5 m có cấu trúc hình chữ U vô cùng phức tạp! |  | Bản vẽ mặt cắt địa chất đáy rừng ngập mặn hiển thị chiếc hang bùn hình chữ U sâu một mét rưỡi dưới đáy bãi lầy; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b30 | 03:07.4–03:10.9 (3.5s) | L145 | Đáy hang là một túi khí ngầm hoàn toàn kỵ khí và không có dưỡng khí tự nhiên. |  | Sơ đồ buồng ấp trứng ngầm dưới đáy hang sâu tăm tối; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b31 | 03:10.9–03:17.2 (6.3s) | L146 | Để bảo vệ bầy trứng non, cá bố liên tục ngoi lên mặt nước ngậm từng ngụm không khí rồi lặn xuống đáy hang nhả vào buồng ấp trứng! |  | Chú cá thòi lòi bố cần mẫn ngậm không khí lặn xuống nhả bóng khí vào buồng ấp trứng cho đến khi buồng chứa đầy dưỡng khí; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b32 | 03:17.2–03:21.4 (4.2s) | L147 | Nó thực hiện hàng trăm chuyến lặn tiếp oxy như một thợ lặn chuyên nghiệp để nuôi dưỡng bầy con |  | Hình ảnh cảm động về chú cá bố túc trực bên bầy trứng non phát sáng lấp lánh dưới đáy hang ngầm; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b33 | 03:21.4–03:26.4 (5.0s) | L148 | thơ! Thật là một người cha mẫu mực và một chiến binh sinh học kiên cường bậc nhất của thế giới ngập mặn! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án vỗ nhẹ lên lưng chú cá, ánh mắt ánh lên niềm khâm phục chân thành. |
| b34 | 03:26.4–03:31.7 (5.3s) | L149 | Chúng còn đắp những bức tường thành bằng bùn cao tới 10 cm quanh miệng hang để phân chia ranh giới lãnh thổ với hàng xóm! |  | Chú cá thòi lòi cần mẫn ngoạm từng viên bùn đắp thành bờ lũy kiên cố quanh tổ ấm của mình; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b35 | 03:31.7–03:38.6 (6.9s) | L150 | Khi có kẻ thù xâm phạm bờ cõi, chàng cá lập tức dựng vây lưng lên thách đấu và búng người tung cú húc đầu sấm sét để đuổi kẻ lạ mặt! |  | Hai chú cá thòi lòi đối đầu nảy lửa trên bờ bùn, giương vây búng đuôi tranh giành từng tấc đất; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b36 | 03:38.6–03:45.3 (6.7s) | L151 | Các nhà cổ sinh vật học coi cá thòi lòi như một hóa thạch sống phản chiếu chính xác bước chuyển mình vĩ đại của sinh giới từ đại dương lên đất liền! |  | Mô hình hóa thạch loài cá cổ đại Tiktaalik đặt cạnh chú cá thòi lòi hiện đại cho thấy sự tương đồng kỳ diệu về cấu trúc xương chi; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b37 | 03:45.3–03:53.3 (8.0s) | L152 | Chẩn đoán Khoa Chấn Thương Chỉnh Hình của Phòng Cấp Cứu Tạo Hóa: Không có gãy xương hay dị tật nào cả! Đây là một vận động viên điền kinh lưỡng cư khỏe mạnh 100%! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đóng dấu ĐẠT CHUẨN XUẤT SẮC lên bệnh án số ba, đưa cho chú cá một miếng tôm nhỏ tươi ngon. |
| b38 | 03:53.3–04:00.7 (7.5s) | L153 | Đơn thuốc cho bệnh nhân: Một khay bùn ngập mặn ẩm ướt pha chút muối biển và vài nhánh rễ cây để anh chàng tha hồ tập hít đất và leo trèo! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đặt chú cá vào khay bùn chuyên dụng, chú chú Cá Thòi Lòi hoạt hình màu nâu xám lấm chấm xanh ngọc, hai mắt to tròn lồi hẳn trên đỉnh đầu chớp chớp ngộ nghĩnh, hai vây ngực bè to như đôi tay đang chống nạng gỗ mini đòi nhảy khỏi cáng cứu thương híp mắt nhai miếng tôm rồi búng đuôi một cái như lời cảm ơn sâu sắc. |
| b39 | 04:00.7–04:07.7 (6.9s) | L154 | Vừa dứt lời thì từ sảnh chính bỗng vang lên một tiếng rầm chấn động cả sàn nhà! Báo động đỏ: Phòng chờ cấp cứu vừa bị sập một mảng sàn! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án và y tá giật bắn người, lập tức lao nhanh ra sảnh chính xem chuyện gì đang xảy ra. |

### scene05 · HAI TẤN THỊT ĐÈ BẸP BÀN NÂNG · 268.6s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.6 (7.6s) | L155 | Một giờ 30 phút sáng. Tôi vừa bước chân ra khỏi Khoa Chấn Thương thì một tiếng rầm long trời lở đất vang lên làm rung chuyển cả tòa nhà bệnh viện! |  | Bụi vôi trắng từ trần nhà rơi lả tả xuống sàn hành lang, các bóng đèn neon trên trần chao đảo dữ dội, tiếng kim loại gãy vụn rền vang từ sảnh lớn; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b02 | 00:07.6–00:13.2 (5.6s) | L156 | Các giá thuốc thủy tinh rung lên bần bật kêu leng keng, sàn gạch men dưới chân tôi nứt toác ra một đường dài 3 m! |  | Cận cảnh đường nứt trên sàn gạch men hoa cương sảnh bệnh viện dưới sức nặng ngàn cân đè nén; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b03 | 00:13.2–00:19.2 (6.0s) | L157 | Tiếng còi báo động khẩn cấp rú lên từng hồi chói tai, hòa lẫn với tiếng thét thất thanh của đội điều dưỡng tiếp đón ngoài cửa sảnh! |  | Đèn báo động màu đỏ rực trên tường nhấp nháy liên hồi, các nhân viên bảo vệ và y tá chạy tán loạn; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b04 | 00:19.2–00:26.8 (7.6s) | L158 | Trời đất quỷ thần ơi! Chuyện gì vừa xảy ra thế này? Xe tải chở đá tảng đâm sập cổng bệnh viện hay có thiên thạch vừa rơi trúng phòng tiếp đón vậy? |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án hớt hải chạy vội ra sảnh lớn, tay vịn vào lan can cầu thang nhìn xuống sảnh đón tiếp đầy khói bụi. |
| b05 | 00:26.8–00:31.7 (4.9s) | L159 | Cả bệnh viện rung chuyển như vừa trải qua một trận động đất 7 độ richter giữa đêm khuya thanh vắng! |  | Khung cảnh hỗn loạn nơi sảnh đón tiếp với các y bác sĩ ôm chặt cột nhà để giữ thăng bằng; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b06 | 00:31.7–00:37.2 (5.4s) | L160 | Hàng loạt hồ sơ bệnh án bay tứ tung giữa làn khói bụi mịt mù, tiếng chuông điện thoại bàn reo inh ỏi không dứt! |  | Các xấp giấy bệnh án bay lượn trong không trung như đàn bướm trắng giữa sảnh bệnh viện ngổn ngang; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b07 | 00:37.2–00:43.0 (5.9s) | L161 | Tiếng la hét hỗn loạn của đội vận chuyển làm cả tòa nhà như biến thành một công trường xây dựng gặp sự cố sập giàn giáo! |  | Đội ngũ bảo vệ và hộ lý cầm đèn pin chạy đôn chạy đáo giữa màn bụi vôi trắng xóa bao phủ sảnh lớn; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b08 | 00:43.0–00:48.4 (5.4s) | L162 | Bác sĩ trưởng khoa ơi cứu tụi em với! Cái bàn nâng thủy lực tải trọng 2 tấn của đội vận chuyển vừa bị gãy đôi làm đôi mảnh |  | Chú bảo vệ gấu đen lực lưỡng mặc áo đồng phục bảo vệ đang ôm chiếc kích thủy lực bị bẹp rúm, mặt mày tái mét hoảng hốt kêu cứu. |
| b09 | 00:48.4–00:56.7 (8.3s) | L163 | rồi! Chúng em vừa khiêng bệnh nhân số 4 từ xe tải thùng bạt xuống cáng thì cái cáng sắt gãy đánh rắc một cái, đè bẹp dúm luôn cả chiếc xe đẩy thuốc bên |  | Chiếc bàn nâng thủy lực bằng thép dày mười phân bị cong vênh gãy đôi, dầu thủy lực màu đỏ chảy lênh láng trên sàn nhà; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b10 | 00:56.7–01:04.1 (7.4s) | L164 | dưới! Bệnh nhân này to như một gian nhà lá, trơn tuột như cục xà bông khổng lồ và không có cổ, không có đuôi gì hết trơn bác sĩ ơi! |  | Chú bảo vệ giơ hai tay miêu tả kích thước khổng lồ của sinh vật lạ đang nằm chắn ngang sảnh đón tiếp; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b11 | 01:04.1–01:10.0 (5.9s) | L165 | Chúng em đã phải huy động tới 6 người đàn ông lực lưỡng mà vẫn không thể nhích nổi nó một xăng-ti-mét nào! |  | Sáu nhân viên bảo vệ to béo đang hò dô đẩy khối thịt khổng lồ nhưng bệnh nhân vẫn nằm ì ra như một tảng đá hoa cương; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b12 | 01:10.0–01:15.2 (5.2s) | L166 | Tôi vội vàng rẽ đám đông bước tới hiện trường, và một cảnh tượng choáng ngợp hiện ra làm tôi phải dụi mắt 3 lần! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án sải bước dài tới trước đống đổ nát của chiếc bàn nâng thủy lực, ngước nhìn khối sinh vật khổng lồ đang nằm bẹp trên sàn. |
| b13 | 01:15.2–01:22.1 (6.9s) | L167 | Nằm sừng sững giữa sảnh đón tiếp của Phòng Cấp Cứu Tạo Hóa là một chiếc bánh kếp sinh học khổng lồ hình tròn dẹt, dài hơn 3 m và cao gần 4 m! |  | Toàn cảnh chú Cá Mặt Trăng (ocean sunfish) hoạt hình khổng lồ hình đĩa tròn dẹt màu xám bạc, không có cuống đuôi, hai vây lưng và vây phần đuôi dựng đứng dài ngoằng, nằm ngửa trên chiếc cáng cứu thương quá khổ mắt to tròn ngơ ngác khổng lồ da màu xám bạc loang lổ, thân hình tròn dẹt như chiếc đĩa bay khổng lồ nằm choán hết hai phần ba diện tích sảnh đón tiếp; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b14 | 01:22.1–01:29.1 (6.9s) | L168 | Đó là Cá Mặt Trăng đại dương Mola mola, loài cá có xương nặng nhất hành tinh, với cân nặng đo được tại chỗ lên tới 2 tấn tròn trĩnh! |  | bảng kẹp bệnh án y khoa khổng lồ (clipboard) kẹp trên giá đỡ kim loại, hiển thị 10 hồ sơ bệnh án hoạt hình với nhãn đơn thuốc phát sáng và sóng nhịp tim ECG màu đỏ nhấp nháy (không có chữ, không có số) bật sáng con số 2.000 kg nhấp nháy đỏ rực bên cạnh hình vẽ mô phỏng kích thước của cá mặt trăng so với một chiếc xe hơi bốn chỗ; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b15 | 01:29.1–01:34.7 (5.7s) | L169 | Toàn bộ cơ thể của nó dường như chỉ có một cái đầu khổng lồ gắn liền với 2 chiếc vây dài ngoằng dựng đứng lên trời và chỉa xuống đất! |  | Chiếc vây lưng và vây phần đuôi dài hơn một mét của cá mặt trăng dựng đứng như hai cánh buồm lớn; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b16 | 01:34.7–01:41.7 (7.0s) | L170 | Không hề có vây đuôi bình thường như các loài cá khác, phần đuôi của nó bị tiêu giảm thành một dải diềm lượn sóng ngắn ngủn nhìn như bị ai đó dùng dao cắt cụt! |  | Cận cảnh phần đuôi cụt ngủn kỳ dị của cá mặt trăng có gờ lượn sóng tròn viền quanh thân sau; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b17 | 01:41.7–01:47.8 (6.1s) | L171 | Bộ xương sống của nó đã tiêu giảm gần hết, chỉ còn lại đúng 16 đốt sống lưng, ít nhất trong toàn bộ thế giới các loài cá! |  | Bản chụp X-quang toàn thân cá mặt trăng cho thấy cột sống ngắn ngủn bất thường chỉ có mười sáu đốt sống thô ráp; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b18 | 01:47.8–01:53.5 (5.7s) | L172 | Hai chiếc vây lưng và vây hậu môn dài ngoằng đập so le nhịp nhàng như đôi cánh chim bay lượn giữa lòng đại dương bao la! |  | Đồ họa cơ sinh học mô phỏng chuyển động đập vây của cá mặt trăng tương tự chuyển động bay lượn của loài chim cánh cụt dưới nước; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b19 | 01:53.5–02:01.7 (8.2s) | L173 | Và điều làm cô y tá hoảng sợ nhất chính là cái miệng của nó: Cái miệng tròn vo hình chữ O đang há hốc ra ngơ ngác, hoàn toàn không thể khép lại được! |  | Cận cảnh chiếc miệng nhỏ xíu tròn xoe như chiếc ống hút của cá mặt trăng, hai hàm răng hợp nhất thành một mỏ cứng như mỏ vẹt; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b20 | 02:01.7–02:07.1 (5.3s) | L174 | Đôi mắt to tròn như 2 chiếc đĩa sứ chớp chớp chậm rãi nhìn trần nhà với vẻ mặt ngơ ngác đến mức tội nghiệp! |  | Đôi mắt tròn xoe vô hồn của cá mặt trăng chớp chớp ngây thơ giữa gương mặt phẳng lì xám xịt; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b21 | 02:07.1–02:14.8 (7.7s) | L175 | Bác sĩ ơi, có phải nó bị tai biến mạch máu não làm liệt cơ hàm méo miệng rồi không? Sao cái miệng nó cứ há toang hoác ra thế kia mà không chịu ngậm lại? |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng run rẩy cầm chiếc đèn pin y tế soi vào trong khoang miệng cá mặt trăng, vẻ mặt đầy bối rối lo âu; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b22 | 02:14.8–02:22.0 (7.2s) | L176 | Không hề có tai biến hay liệt cơ nào ở đây cả cô y tá thân mến! Đó là cấu trúc hàm hợp nhất tự nhiên của bộ cá nóc mà loài cá này thuộc về! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười giải thích, đưa tay sờ vào lớp da dày cộp xù xì như giấy ráp của bệnh nhân khổng lồ. |
| b23 | 02:22.0–02:29.9 (7.9s) | L177 | Răng của nó đã tiêu biến và hợp nhất lại thành một chiếc mỏ sừng sắc bén, dùng để hút và nghiền nát những con sứa biển trơn tuột dưới đại dương sâu thẳm! |  | Hình ảnh mô phỏng bộ hàm hợp nhất hình chiếc mỏ chim của cá mặt trăng đang hút trọn một đàn sứa phát sáng dưới làn nước biển xanh thẳm; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b24 | 02:29.9–02:38.7 (8.7s) | L178 | Thức ăn ưa thích của nó là các loài động vật thân mềm bồng bềnh chứa tới 95% là nước và cực kỳ ít calo, khiến con vật phải ăn liên tục suốt ngày đêm! |  | Đồ họa chuỗi thức ăn hiển thị hàng trăm con sứa trong suốt bị hút gọn vào khoang miệng cá mặt trăng; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b25 | 02:38.7–02:46.2 (7.6s) | L179 | Lớp sụn xơ dày cộp bao bọc quanh người hoạt động như một lớp đệm hấp thu xung lực va đập tự nhiên, giúp nó an toàn trước các đợt sóng biển dữ dội! |  | Bản vẽ mô phỏng các sợi collagen đan chéo dày đặc trong lớp da tạo nên một tấm áo giáp sinh học đàn hồi tuyệt hảo; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b26 | 02:46.2–02:52.8 (6.5s) | L180 | Nhưng điều làm tôi lo ngại nhất lúc này không phải là chiếc miệng, mà là áp lực trọng lực đang đè nén lên các cơ quan nội tạng của con vật! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án áp ống nghe vào lớp da dày cộp của con cá, lắng nghe nhịp tim đập chậm rãi của khối cơ thể hai tấn. |
| b27 | 02:52.8–02:58.0 (5.2s) | L181 | Dưới đáy đại dương, lực đẩy Ác-si-mét nâng đỡ toàn bộ khối cơ thể 2 tấn này một cách nhẹ nhàng êm ái. |  | Bức tranh miêu tả cá mặt trăng đang bơi lội thanh thoát giữa đại dương bao la, ánh nắng mặt trời chiếu xuyên qua làn nước trong vắt; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b28 | 02:58.0–03:03.8 (5.9s) | L182 | Nhưng khi bị đưa lên cạn, trọng lượng khổng lồ sẽ ép bẹp các mạch máu và làm suy hô hấp nghiêm trọng nếu không được giải phóng kịp thời! |  | Đồ họa y học hiển thị áp lực cơ học đè nặng lên các cơ quan bên trong cơ thể bên trong khi cá mặt trăng nằm trên mặt phẳng cứng; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b29 | 03:03.8–03:13.5 (9.6s) | L183 | Hơn nữa, trên lớp da dày tới 7,5 cm bằng sụn xơ của nó đang có hơn 4 mươi loài ký sinh trùng khác nhau đang bám dính dày đặc như một viện bảo tàng ký sinh trùng sống! |  | Kính lúp y khoa soi bề mặt da cá mặt trăng với hàng chục loài ký sinh trùng giáp xác và giun dẹp bám chặt vào lớp biểu bì; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b30 | 03:13.5–03:18.7 (5.2s) | L184 | Bác sĩ trưởng khoa ơi, da nó dày cứng như lốp xe tải thế này thì kim tiêm nào đâm cho thủng được ạ? |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng cầm chiếc kim tiêm chuyên dụng ấn thử vào da cá nhưng mũi kim bị uốn cong queo không thể xuyên qua lớp sụn xơ dày cộp. |
| b31 | 03:18.7–03:22.6 (3.8s) | L185 | Chúng ta phải làm sao để cứu anh chàng khổng lồ ngơ ngác này bây giờ bác sĩ ơi? |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng lo lắng nhìn khối thịt hai tấn đang thở phì phò trên sàn sảnh đón tiếp; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b32 | 03:22.6–03:28.0 (5.5s) | L186 | Nhìn vẻ mặt ngơ ngác vô tội của nó giữa sảnh bệnh viện mà tôi vừa buồn cười vừa xót xa cho sinh vật đại dương này! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án lắc đầu thở dài, cúi xuống nhìn đôi mắt tròn xoe phẳng lặng không chút sát khí của chú cá mặt trăng. |
| b33 | 03:28.0–03:34.5 (6.5s) | L187 | Trong lịch sử hàng hải cổ đại, các thủy thủ từng lầm tưởng chiếc vây lưng nhô cao của cá mặt trăng là thủy quái kraken khổng lồ! |  | Bức tranh khắc gỗ thời Phục hưng vẽ cảnh con tàu buồm cổ đối mặt với chiếc vây lưng nhô cao của cá mặt trăng giữa sóng gió biển khơi; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b34 | 03:34.5–03:41.1 (6.6s) | L188 | Thế nhưng thực tế nó lại là sinh vật hiền lành và ngờ nghệch bậc nhất đại dương, thậm chí để mặc cho hải cẩu và cá kình rỉa vây mà chẳng hề buồn chống |  | Chú hải cẩu nghịch ngợm bơi quanh chú cá mặt trăng đang trôi lơ lửng, chú cá chẳng hề có phản ứng né tránh nào; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b35 | 03:41.1–03:47.7 (6.5s) | L189 | cự! Đã có những trường hợp cá mặt trăng trôi dạt vào bãi tắm làm cả bờ biển náo loạn vì tưởng quái vật ngoài hành tinh đổ bộ! |  | Cảnh người dân trên bãi biển tụ tập vây quanh khối thịt tròn dẹt khổng lồ với vẻ kinh ngạc tò mò; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b36 | 03:47.7–03:54.2 (6.5s) | L190 | Đội cứu hộ khẩn cấp nghe lệnh tôi! Lập tức điều động chiếc xe cẩu chuyên dụng 10 tấn và dây đai bạt cứu hộ vào sảnh đón tiếp ngay lập tức! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án cầm bộ đàm ra lệnh dõng dạc, ánh mắt quyết đoán và bình tĩnh điều phối toàn bộ hiện trường cấp cứu. |
| b37 | 03:54.2–03:58.0 (3.8s) | L191 | Chúng ta không thể khám bệnh cho khối thịt 2 tấn này trên sàn nhà cứng ngắc này được! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án chỉ huy đội bảo vệ căng các tấm đệm hơi cao su quanh thân cá mặt trăng để giảm áp lực tì đè cơ học. |
| b38 | 03:58.0–04:02.9 (4.9s) | L192 | Mở van nước xả đầy chiếc bể ngâm nước muối sinh lý dung tích 50 m³ ở Khoa Hồi Sức Cấp Cứu Đại |  | Chiếc bể bơi y tế khổng lồ lát gạch xanh ngọc bích bắt đầu được bơm đầy nước muối biển nhân tạo có hệ thống sục khí oxy cực mạnh; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b39 | 04:02.9–04:10.0 (7.1s) | L193 | Dương! Dùng dây đai bạt luồn nhẹ nhàng dưới bụng cá mặt trăng, cẩu bổng anh chàng lên và chuyển thẳng vào bể hồi sức ngay trong 15 phút tới! |  | Chiếc cần cẩu y tế màu vàng từ từ hạ móc cáp thép xuống, các điều dưỡng viên cẩn thận luồn những dải đai bạt mềm mại quanh thân cá mặt trăng; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b40 | 04:10.0–04:18.8 (8.9s) | L194 | Một, 2, 3, nâng! Dưới sự điều khiển nhịp nhàng của kíp trực, khối sinh vật 2 tấn từ từ được nhấc bổng lên không trung trong sự reo hò thán phục của toàn thể bệnh nhân trong sảnh! |  | Khối cơ thể khổng lồ của chú Cá Mặt Trăng (ocean sunfish) hoạt hình khổng lồ hình đĩa tròn dẹt màu xám bạc, không có cuống đuôi, hai vây lưng và vây phần đuôi dựng đứng dài ngoằng, nằm ngửa trên chiếc cáng cứu thương quá khổ mắt to tròn ngơ ngác lơ lửng trên không trung giữa sảnh bệnh viện, đôi mắt tròn xoe ngơ ngác nhìn đám đông bên dưới chớp chớp như đang đi du lịch; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b41 | 04:18.8–04:28.6 (9.8s) | L195 | Sàn sảnh đón tiếp tạm thời được giải tỏa an toàn! Nhưng đừng vội mừng, vì ngay cạnh phòng mổ số 2, tiếng kêu thất thanh của một chú gián đang báo hiệu ca phẫu thuật thần kinh dị thường nhất trần đời vừa bắt đầu! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án lau mồ hôi trên trán, rảo bước chạy vội về phía phòng phẫu thuật thần kinh nơi có ánh đèn huỳnh quang màu xanh ngọc bích đang chiếu sáng. |

### scene06 · BÁC SĨ TÍ HON THÔI MIÊN GIÁN · 269.6s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:04.5 (4.5s) | L196 | Cánh cửa phòng mổ thần kinh số 2 mở ra trong một bầu không khí lạnh ngắt và tĩnh lặng đến gai |  | Căn phòng mổ vô trùng sáng choang ánh đèn phẫu thuật, các khay dao mổ siêu vi sáng loáng xếp hàng ngay ngắn trên bàn inox; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b02 | 00:04.5–00:11.6 (7.1s) | L197 | người. Trên bàn mổ chính bọc khăn vải xanh vô trùng, một cảnh tượng rùng rợn và kỳ quái làm bất kỳ ai chứng kiến cũng phải sởn gai ốc từ đầu đến |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đeo kính hiển vi phẫu thuật phóng đại, cúi nhìn chăm chú vào bàn mổ; cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng đứng nép một góc run rẩy ôm chặt tập hồ sơ bệnh án. |
| b03 | 00:11.6–00:17.9 (6.3s) | L198 | chân! Một chú gián Mỹ khổng lồ dài 5 cm, to gấp 6 lần một con ong, đang đứng im phăng phắc như một pho tượng gỗ vô hồn! |  | Một chú gián Mỹ màu nâu cánh gián to lớn đứng bất động trên tấm khăn mổ vô trùng, hai sợi râu dài buông thõng rũ rượi; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b04 | 00:17.9–00:23.6 (5.7s) | L199 | Hai chiếc râu dài của nó bị cắt cụt một nửa, đôi mắt kép đờ đẫn mất hoàn toàn phản xạ trốn chạy hay phòng vệ tự nhiên! |  | Cận cảnh đôi mắt kép màu đen đục vô hồn của chú gián, hoàn toàn không có bất kỳ phản xạ giật mình nào khi có bóng người lướt qua; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b05 | 00:23.6–00:29.5 (5.9s) | L200 | Và đứng kiêu hãnh trên lưng chú gián khổng lồ là bệnh nhân số 5 của chúng ta: Cô Ong Bắp Cày Ngọc Ampulex compressa! |  | cô Ong Bắp Cày Ngọc (emerald cockroach wasp) hoạt hình thân thon dài phát sáng xanh ngọc bích kim loại lộng lẫy, chân dài thanh mảnh, tay cầm chiếc dao mổ phẫu thuật thần kinh siêu nhỏ giơ lên đầy tự tin toàn thân phát sáng màu xanh ngọc bích ánh kim lộng lẫy như một viên đá quý, sải chân dài thanh mảnh kiêu hãnh đứng trên lưng chú gián; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b06 | 00:29.5–00:37.5 (8.0s) | L201 | Cô ong đang dùng chiếc vòi miệng tí hon của mình bình thản gặm nhấm vết cắt ở râu chú gián để hút dịch bạch huyết như đang thưởng thức một ly nước ngọt giải khát! |  | Cận cảnh vòi miệng của ong bắp cày ngọc đang hút giọt dịch bạch huyết màu trắng trong suốt rỉ ra từ gốc râu chú gián; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b07 | 00:37.5–00:43.8 (6.2s) | L202 | Bác sĩ trưởng khoa ơi cứu em với! Con ong xanh lấp lánh kia nó vừa làm phép phù thủy biến con gián thành thây ma sống kìa! |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng hai tay ôm mặt run lẩy bẩy, chỉ ngón tay vào chú gián to lớn đang đứng ngoan ngoãn như một chú cún con. |
| b08 | 00:43.8–00:50.0 (6.2s) | L203 | Con gián to gấp 6 lần con ong, chân cẳng khỏe như lực sĩ mà sao nó không thèm đá văng con ong ra để chạy trốn hả bác sĩ? |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng ngạc nhiên tột cùng nhìn chú gián to lớn hoàn toàn đủ sức đè bẹp chú ong nhỏ bé nhưng lại đứng im chịu trận; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b09 | 00:50.0–00:54.7 (4.7s) | L204 | Có phải con ong này biết thuật thôi miên tà đạo hay dùng bùa ngải gì không bác sĩ ơi? |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng ngước nhìn bác sĩ với ánh mắt đầy khiếp hãi và tò mò cao độ; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b10 | 00:54.7–00:59.2 (4.5s) | L205 | Không hề có bùa ngải hay phép thuật phù thủy nào ở đây cả cô y tá thân mến! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười chỉnh lại độ nét của chiếc kính hiển vi phẫu thuật, say mê quan sát từng chi tiết giải phẫu tinh vi của cô ong ngọc bích. |
| b11 | 00:59.2–01:04.8 (5.7s) | L206 | Đây chính là nữ phẫu thuật viên thần kinh lỗi lạc và tàn nhẫn nhất trong toàn bộ lịch sử tiến hóa của giới côn trùng! |  | cô Ong Bắp Cày Ngọc (emerald cockroach wasp) hoạt hình thân thon dài phát sáng xanh ngọc bích kim loại lộng lẫy, chân dài thanh mảnh, tay cầm chiếc dao mổ phẫu thuật thần kinh siêu nhỏ giơ lên đầy tự tin vươn đôi cánh mỏng trong suốt màu khói, ánh xanh lục bảo lấp lánh phản chiếu rực rỡ dưới ánh đèn mổ phẫu thuật; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b12 | 01:04.8–01:15.4 (10.5s) | L207 | Loài ong bắp cày ngọc này không hề giết chết con gián, mà nó thực hiện một ca phẫu thuật não bộ 2 giai đoạn với độ chính xác cơ học vượt xa tay nghề của các giáo sư ngoại thần kinh hàng đầu loài người! |  | Sơ đồ giải phẫu hệ thần kinh của gián với các hạch thần kinh ngực và hạch thần kinh dưới thực quản phát sáng dưới tia tử ngoại; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b13 | 01:15.4–01:23.7 (8.3s) | L208 | Hãy nhìn vào quy trình 2 mũi tiêm thần kinh chết người mà nghiên cứu kinh điển của giáo sư Libersat công bố trên Tạp Chí Sinh Học Thực Nghiệm đã giải mã! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án giơ bản đồ giải phẫu thần kinh côn trùng lên trước ánh đèn, chỉ vào từng vị trí đâm kim chính xác đến từng mi-crô-mét. |
| b14 | 01:23.7–01:30.9 (7.1s) | L209 | Mũi tiêm thứ nhất: Khi bắt gặp con gián, ong bắp cày lao tới vật ngửa con mồi ra và cắm ngập chiếc ngòi sắc bén vào hạch thần kinh ngực đầu tiên của con gián! |  | Hình ảnh mô phỏng ong bắp cày dùng hàm kẹp chặt gián, uốn cong bụng cắm chiếc ngòi nhọn hoắt vào phần ngực dưới của con mồi; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b15 | 01:30.9–01:36.7 (5.9s) | L210 | Mũi tiêm đầu tiên này chứa một lượng lớn chất dẫn truyền thần kinh ức chế GABA và các chất làm tê liệt cơ bắp tạm thời. |  | Đồ họa hóa học hiển thị các phân tử nọc độc khóa chặt các thụ thể thần kinh vận động ở hai chân trước của con gián; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b16 | 01:36.7–01:42.6 (5.9s) | L211 | Trong đúng 2 phút đồng hồ, 2 chân trước của con gián bị tê liệt hoàn toàn, khiến nó không thể giơ chân lên gạt đòn hay phản kháng |  | Con gián giãy giụa bất lực khi hai chân trước rũ liệt hoàn toàn, tạo điều kiện thuận lợi tuyệt đối cho mũi tiêm quyết định thứ hai; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b17 | 01:42.6–01:52.2 (9.6s) | L212 | được nữa! Và đây mới là đỉnh cao giải phẫu học làm rung chuyển giới y khoa: Mũi tiêm thứ 2 xuyên thẳng qua lớp vỏ kitin cứng ở cổ, chọc sâu vào tận hạch thần kinh dưới thực quản bên trong não bộ con gián! |  | Đồ họa cắt lớp hiển thị chiếc ngòi ong uốn lượn luồn lách qua các mô mềm ở cổ gián, đâm chính xác tuyệt đối vào hạch não điều khiển hành vi; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b18 | 01:52.2–02:00.8 (8.7s) | L213 | Chiếc ngòi của ong được trang bị các cơ quan thụ cảm cơ học và hóa học siêu nhỏ, cho phép nó cảm nhận và định vị chính xác hạch não trong bóng tối tăm mù mịt bên trong hộp sọ con mồi! |  | Đầu ngòi ong phóng đại hiển thị các sợi cảm biến nano đang dò tìm tín hiệu hóa học của mô não gián với độ sai lệch bằng không; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b19 | 02:00.8–02:08.4 (7.5s) | L214 | Nọc độc của mũi tiêm thứ 2 là một ly cocktail hóa sinh phức tạp bậc nhất tự nhiên, chứa các chất ức chế thụ thể dopamine và octopamine chuyên |  | Các phân tử độc tố màu đỏ thẫm len lỏi phong tỏa hoàn toàn các thụ thể dopamine trong trung khu điều khiển vận động chủ động của não gián; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b20 | 02:08.4–02:11.9 (3.5s) | L215 | biệt! Chất octopamine là chất kích hoạt phản xạ trốn chạy khi gặp nguy hiểm ở loài côn |  | Đồ họa thần kinh hiển thị đường dẫn truyền tín hiệu phản xạ trốn chạy của gián bị cắt đứt hoàn toàn như sợi dây điện bị ngắt cầu dao; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b21 | 02:11.9–02:18.7 (6.8s) | L216 | trùng. Khi bị nọc độc khóa chặt thụ thể này, con gián hoàn toàn mất đi ý chí sinh tồn và phản xạ tự vệ, biến thành một thây ma sống đúng nghĩa đen! |  | Cận cảnh chú gián đứng im như pho tượng, dù có tiếng động lớn hay bị chạm vào người cũng không hề buồn nhúc nhích; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b22 | 02:18.7–02:26.6 (7.9s) | L217 | Chú gián vẫn thở bình thường, tim vẫn đập, chân cẳng vẫn hoạt động tốt, nhưng động lực tự bước đi để cứu lấy bản thân đã bị xóa sổ 100%! |  | Đồ họa sinh lý học hiển thị các chức năng sống cơ bản của gián duy trì bình thường nhưng mất hoàn toàn khả năng tự chủ vận động; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b23 | 02:26.6–02:32.4 (5.8s) | L218 | Sau đó, cô ong cắt bớt 2 chiếc râu dài của gián để uống dịch bạch huyết bù đắp năng lượng tiêu hao sau trận đấu vật căng |  | Cô ong dùng đôi hàm sắc như kéo cắt đứt ngọt ngào hai sợi râu của chú gián trước sự sững sờ của các bác sĩ; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b24 | 02:32.4–02:40.6 (8.2s) | L219 | thẳng! Rồi cô ong ngậm lấy phần gốc râu còn lại, dắt con gián to lớn lững thững đi theo mình về chiếc tổ ngầm dưới lòng đất như dắt một chú cún ngoan ngoãn đi dạo phố! |  | Bức tranh miêu tả cô cô Ong Bắp Cày Ngọc (emerald cockroach wasp) hoạt hình thân thon dài phát sáng xanh ngọc bích kim loại lộng lẫy, chân dài thanh mảnh, tay cầm chiếc dao mổ phẫu thuật thần kinh siêu nhỏ giơ lên đầy tự tin nhỏ bé ngậm râu dắt chú gián khổng lồ ngoan ngoãn bước từng bước theo sau đi vào chiếc hang tối; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b25 | 02:40.6–02:45.4 (4.8s) | L220 | Tại chiếc tổ đó, ong sẽ đẻ một quả trứng duy nhất lên bụng con gián, niêm phong cửa hang lại bằng đất |  | Ấu trùng ong bắp cày màu trắng ngà phát triển bên cạnh chú gián sống trong chiếc tổ ngầm kiên cố; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b26 | 02:45.4–02:52.8 (7.5s) | L221 | đá. Sau khi đẻ trứng xong, cô ong mẹ còn tỉ mỉ nhặt từng viên sỏi nhỏ và cành cây khô che phủ kín miệng hang để ngụy trang tuyệt đối trước các loài săn |  | Chú cô Ong Bắp Cày Ngọc (emerald cockroach wasp) hoạt hình thân thon dài phát sáng xanh ngọc bích kim loại lộng lẫy, chân dài thanh mảnh, tay cầm chiếc dao mổ phẫu thuật thần kinh siêu nhỏ giơ lên đầy tự tin cần mẫn gắp từng hạt cát hạt sỏi nhỏ lấp kín lối vào căn hầm ngầm bí mật; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b27 | 02:52.8–03:00.6 (7.8s) | L222 | mồi khác! Con gián sống thực vật này đóng vai trò như một kho thực phẩm tươi sống hoàn hảo, nuôi dưỡng ấu trùng ong lớn lên cho tới ngày lột xác bay ra ngoài! |  | Ấu trùng ong bọc kén tơ mỏng, chuẩn bị cho quá trình biến thái hoàn toàn dưới lòng đất ẩm ướt; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b28 | 03:00.6–03:07.1 (6.4s) | L223 | Cơ quan thị giác và xúc giác ở chân của cô ong bắp cày ngọc tinh vi đến mức có thể nếm được mùi vị dịch mô của con mồi qua lớp lông cảm |  | Kính hiển vi điện tử quét hiển thị các thụ thể hóa học hình nón li ti trên các đốt bàn chân của ong bắp cày ngọc; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b29 | 03:07.1–03:13.8 (6.8s) | L224 | ứng! Bằng cách cọ nhẹ bàn chân lên đầu chú gián, cô ong có thể đo đạc chính xác nồng độ độc tố thần kinh còn tồn đọng trong mô não con mồi! |  | Đồ họa hóa sinh hiển thị các tín hiệu điện sinh học từ thụ thể chân ong truyền về hạch thần kinh trung ương xử lý dữ liệu; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b30 | 03:13.8–03:19.4 (5.5s) | L225 | Nếu liều lượng thuốc tê quá nhẹ, con gián có thể hồi phục phản xạ và đá văng quả trứng của ong ra khỏi bụng! |  | Hình ảnh mô phỏng chú gián giật mình đá mạnh chân sau nếu không bị phong tỏa thần kinh hoàn toàn; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b31 | 03:19.4–03:25.5 (6.1s) | L226 | Nhưng nếu liều lượng quá mạnh, con gián sẽ chết ngay lập tức và phân hủy thối rữa trước khi ấu trùng ong kịp nở ra để thưởng thức thịt |  | Đồ họa sinh học đối chiếu mức liều lượng nọc độc chuẩn xác đến từng nano gam giúp con mồi sống thực vật hoàn hảo; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b32 | 03:25.5–03:31.8 (6.3s) | L227 | tươi! Độ chuẩn xác tuyệt đối đến từng nano gam nọc độc này là một kiệt tác vi sinh hóa học mà loài người còn lâu mới bắt kịp! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án nghiêng đầu thán phục nhìn chiếc ngòi ong thép thu gọn tinh xảo bên dưới lớp giáp ngọc bích. |
| b33 | 03:31.8–03:40.8 (9.0s) | L228 | Đó là sự tàn nhẫn lạnh lùng nhưng cũng là sự tinh vi cơ học tuyệt đối của tự nhiên: Giữ cho con mồi sống tươi nguyên suốt nhiều tuần lễ mà không cần tủ lạnh bảo quản! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án thở dài thán phục, gật đầu công nhận sự hoàn mỹ của cơ chế ký sinh thần kinh độc nhất vô nhị này. |
| b34 | 03:40.8–03:48.8 (8.1s) | L229 | Cô ong của chúng ta hôm nay nhập viện không phải vì bị bệnh, mà vì vô tình bay lạc vào phòng mổ bệnh viện qua lỗ thông gió trong khi đang dẫn giải con gián đi tìm |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười nhìn cô ong ngọc bích đang nghiêng đầu làm duyên trên lưng chú gián. |
| b35 | 03:48.8–03:55.9 (7.1s) | L230 | tổ! Toàn bộ hệ thống ngòi tiêm và tuyến nọc độc của cô nàng hoạt động hoàn hảo tuyệt đối không tì vết, phản xạ vận động đạt điểm 10 trên |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án dùng kính hiển vi soi kỹ phần bụng dưới của cô Ong Bắp Cày Ngọc (emerald cockroach wasp) hoạt hình thân thon dài phát sáng xanh ngọc bích kim loại lộng lẫy, chân dài thanh mảnh, tay cầm chiếc dao mổ phẫu thuật thần kinh siêu nhỏ giơ lên đầy tự tin, nơi chiếc ngòi thép thu gọn an toàn bên trong bao trùm kitin sáng bóng. |
| b36 | 03:55.9–04:04.7 (8.7s) | L231 | 10! Các nhà dược lý học hiện đại đang nghiên cứu công thức nọc độc của ong bắp cày ngọc để điều chế các loại thuốc gây mê thần kinh thế hệ mới không gây nghiện! |  | Mô hình phân tử hóa học của các hợp chất giảm đau thế hệ mới lấy cảm hứng từ nọc ong ngọc bích phát sáng trên màn hình máy tính; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b37 | 04:04.7–04:12.4 (7.7s) | L232 | Thôi được rồi cô nàng phẫu thuật viên tí hon lộng lẫy ơi! Phòng mổ của tôi là nơi cứu người chứ không phải nơi cô mở lò đào tạo thây ma gián nhé! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án bật cười lắc đầu, dùng một chiếc hộp mica trong suốt chuyên dụng nhẹ nhàng chụp lấy cả cô ong lẫn chú gián. |
| b38 | 04:12.4–04:20.6 (8.2s) | L233 | Chúng tôi sẽ chuyển cả 2 bạn sang Viện Nghiên Cứu Côn Trùng Học Quốc Gia để các nhà thần kinh học tiếp tục học hỏi công thức chế tạo thuốc tê thần kinh từ cô nàng nhé! |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng cẩn thận dán nhãn chuyển viện lên chiếc hộp mica, thở phào nhẹ nhõm khi tiễn được ca bệnh thần kinh rùng rợn này ra khỏi phòng mổ. |
| b39 | 04:20.6–04:29.6 (9.0s) | L234 | Hồ sơ Khoa Phẫu Thuật Não hoàn tất xuất sắc! Giờ thì nghe kìa, tiếng máy bơm nước từ Khoa Hồi Sức Đại Dương báo hiệu bể ngâm cá mặt trăng 2 tấn đã sẵn sàng! Toàn đội chạy nhanh nào! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án cởi áo choàng phẫu thuật, chạy vội về phía khu hồi sức cấp cứu đại dương. |

### scene07 · BỂ NGÂM NƯỚC MUỐI SINH LÝ · 265.1s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.0 (8.0s) | L235 | Ùng oàng! Bùm! Khối cơ thể khổng lồ 2 tấn của chú Cá Mặt Trăng Mola mola được cần cẩu hạ cánh an toàn xuống bể ngâm nước muối sinh lý dung tích 50 m³! |  | Sóng nước màu xanh ngọc bích bắn tung tóe lên thành bể kính dày mười phân, bọt khí sủi tăm trắng xóa bao bọc quanh thân hình tròn dẹt khổng lồ của chú Cá Mặt Trăng (ocean sunfish) hoạt hình khổng lồ hình đĩa tròn dẹt màu xám bạc, không có cuống đuôi, hai vây lưng và vây phần đuôi dựng đứng dài ngoằng, nằm ngửa trên chiếc cáng cứu thương quá khổ mắt to tròn ngơ ngác; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b02 | 00:08.0–00:14.0 (6.0s) | L236 | Lực đẩy Ác-si-mét của dòng nước mặn lập tức nâng bổng khối cơ thể nặng ngàn cân lên một cách nhẹ nhàng như một chiếc lá trôi bồng bềnh. |  | Khối cơ thể hai tấn trôi lơ lửng nhẹ nhàng giữa làn nước trong suốt, các áp lực cơ học đè nặng lên tim phổi được giải phóng hoàn toàn; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b03 | 00:14.0–00:19.7 (5.7s) | L237 | Các đường ống sục khí oxy công suất lớn sủi bọt cuồn cuộn quanh các lá mang của chú cá, cung cấp nguồn dưỡng khí dồi dào |  | Hệ thống ống dẫn oxy sục bọt trắng xóa quanh hai nắp mang nhỏ xíu của cá mặt trăng, chú cá bắt đầu thở phập phồng nhịp nhàng; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b04 | 00:19.7–00:26.7 (7.0s) | L238 | tức thì. Tôi cùng kíp trực Khoa Hồi Sức Cấp Cứu Đại Dương bước lên cầu quan sát bằng kính chịu lực bắc ngang qua mặt bể để tiến hành thăm khám toàn diện. |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đứng trên cầu kính quan sát, tay cầm bảng ghi chép chỉ số sinh tồn; cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng cầm chiếc máy đo nồng độ muối và nhiệt độ nước theo dõi sát sao. |
| b05 | 00:26.7–00:32.6 (5.9s) | L239 | Nhịp tim của chú cá qua máy theo dõi điện tâm đồ thủy sinh dao động ở mức 30 nhịp mỗi phút, vô cùng ổn định và đều đặn! |  | Màn hình điện tâm đồ nhấp nháy những đường sóng P-Q-R-S màu xanh lá cây hiển thị nhịp tim ba mươi lần một phút nhịp nhàng; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b06 | 00:32.6–00:37.1 (4.5s) | L240 | Bác sĩ trưởng khoa ơi em vừa chạy xong bản quét cộng hưởng từ MRI toàn thân cho khối thịt 2 tấn |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng giơ tập phim chụp cộng hưởng từ MRI kích thước khổng lồ lên trước màn hình rọi sáng, vẻ mặt đầy bàng hoàng không tin vào mắt mình. |
| b07 | 00:37.1–00:41.1 (4.0s) | L241 | này! Em tìm mỏi cả mắt mà không thấy bóng hơi hay bong bóng cá ở đâu cả bác |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng chỉ tay vào khoảng trống rỗng nơi đáng lẽ phải có bóng khí bơi lội của các loài cá thông thường; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b08 | 00:41.1–00:52.5 (11.4s) | L242 | sĩ ơi! Và đây nữa nè: Hộp sọ của nó to bằng chiếc thùng phi 10 lít, nhưng bộ não bên trong của nó... trời đất ơi, nó chỉ nhỏ bằng hạt đậu phộng thôi bác sĩ ơi! Có phải máy quét MRI của em bị lỗi kỹ thuật không ạ? |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng mở to mắt chỉ vào chấm nhỏ xíu phát sáng màu cam nằm cô độc giữa khoang sọ khổng lồ của cá mặt trăng; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b09 | 00:52.5–00:57.1 (4.6s) | L243 | Máy quét của cô hoàn toàn chính xác 100% không hề có một lỗi kỹ thuật nào cô y tá thân |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án bật cười giơ tấm phim chụp lên trước ánh sáng đèn soi, chỉ vào cấu trúc sọ não kỳ lạ của chú cá. |
| b10 | 00:57.1–01:05.7 (8.6s) | L244 | mến! Chào mừng toàn thể kíp trực đến với nghịch lý giải phẫu vĩ đại nhất của đại dương bao la: Bệnh nhân sở hữu tỷ lệ não bộ trên trọng lượng cơ thể nhỏ nhất trong toàn bộ giới động vật có xương |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án chỉ đầu bút vào điểm sáng li ti của bộ não trên phim chụp MRI. |
| b11 | 01:05.7–01:12.2 (6.6s) | L245 | sống! Một con cá mặt trăng trưởng thành nặng tới 2 tấn tròn trĩnh, nhưng toàn bộ khối lượng bộ não của nó chỉ vỏn vẹn đúng... 4 g! |  | bảng kẹp bệnh án y khoa khổng lồ (clipboard) kẹp trên giá đỡ kim loại, hiển thị 10 hồ sơ bệnh án hoạt hình với nhãn đơn thuốc phát sáng và sóng nhịp tim ECG màu đỏ nhấp nháy (không có chữ, không có số) bật sáng con số 4 gam bên cạnh con số 2.000 kg với dấu chấm than đỏ chót biểu thị tỷ lệ một phần năm trăm ngàn không tưởng; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b12 | 01:12.2–01:18.7 (6.4s) | L246 | Nghĩa là bộ não của nó chỉ chiếm 1/500.000 tổng trọng lượng cơ thể! Nhỏ hơn cả bộ não của một con mèo con hay một chú chuột nhắt |  | Hình ảnh so sánh hạt đậu phộng nhỏ xíu đặt cạnh khối thịt hai tấn đồ sộ của cá mặt trăng; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b13 | 01:18.7–01:26.3 (7.6s) | L247 | tí hon! Thế nhưng với bộ não 4 g đó, nó vẫn điều khiển thành công cỗ máy sinh học 2 tấn vượt qua hàng ngàn hải lý đại dương suốt hàng chục 5 ròng rã! |  | Bản đồ vệ tinh hiển thị lộ trình di cư xuyên đại dương hàng chục ngàn cây số của các chú cá mặt trăng gắn máy định vị vệ tinh; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b14 | 01:26.3–01:30.6 (4.3s) | L248 | Và tại sao nó lại không hề có bóng hơi để bơi lội như các loài cá thông thường? |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đặt câu hỏi đầy hào hứng nhìn về phía các bác sĩ nội trú đang chăm chú lắng nghe từng lời phân tích. |
| b15 | 01:30.6–01:37.7 (7.2s) | L249 | Bởi vì môi trường kiếm ăn chính của cá mặt trăng là vùng nước sâu tăm tối twilight zone ở độ sâu từ 400 đến tận 800 m dưới đáy biển! |  | Bức tranh miêu tả vùng biển sâu thăm thẳm lạnh ngắt tăm tối nơi ánh sáng mặt trời không thể chiếu tới, chú chú Cá Mặt Trăng (ocean sunfish) hoạt hình khổng lồ hình đĩa tròn dẹt màu xám bạc, không có cuống đuôi, hai vây lưng và vây phần đuôi dựng đứng dài ngoằng, nằm ngửa trên chiếc cáng cứu thương quá khổ mắt to tròn ngơ ngác đang bơi lội kiếm ăn giữa đàn sứa phát sáng; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b16 | 01:37.7–01:44.3 (6.5s) | L250 | Ở độ sâu 800 m, áp suất nước biển lên tới 80 atm, thừa sức bóp bẹp rúm bất kỳ chiếc bóng hơi nào trong chớp mắt! |  | Hình ảnh mô phỏng quả bóng hơi bằng cao su bị áp lực nước sâu bóp nát vụn thành mảnh vụn nhỏ; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b17 | 01:44.3–01:50.8 (6.5s) | L251 | Nếu có bóng hơi, cá mặt trăng sẽ không thể lao nhanh từ độ sâu 800 m lên mặt nước mà không bị vỡ nội tạng do giảm áp |  | Sơ đồ y học hiển thị hiện tượng thuyên tắc khí nguy hiểm nếu động vật có bóng hơi nổi lên quá nhanh từ đáy sâu; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b18 | 01:50.8–01:58.2 (7.4s) | L252 | đột ngột! Vì vậy, tiến hóa đã thay thế toàn bộ bóng khí bằng một lớp sụn xơ gelatin dày tới 7,5 cm nằm ngay dưới lớp da của nó! |  | Bản vẽ cắt ngang lớp da cá mặt trăng hiển thị lớp mô liên kết gelatin xốp màu trắng ngà nhẹ hơn nước biển; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b19 | 01:58.2–02:07.1 (8.9s) | L253 | Lớp mô gelatin kỳ diệu này có tỷ trọng gần như tương đương với nước biển, giúp con cá đạt trạng thái trôi nổi trung tính ở bất kỳ độ sâu nào mà không sợ áp suất nghiền nát! |  | Chú cá mặt trăng trôi lơ lửng tự nhiên trong nước mà không cần tốn một chút năng lượng nào để duy trì độ sâu; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b20 | 02:07.1–02:13.7 (6.6s) | L254 | Sau mỗi chuyến lặn sâu 800 m xuống vùng nước băng giá 4°C để săn sứa, thân nhiệt của chú cá bị hạ xuống mức báo động nguy hiểm. |  | Đồ thị đo thân nhiệt của cá mặt trăng lao dốc xuống vùng màu xanh băng giá bốn độ C sau chuyến lặn sâu; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b21 | 02:13.7–02:21.2 (7.5s) | L255 | Đó là lý do tại sao nó phải bơi lên mặt biển, nằm nghiêng hoàn toàn thân hình dẹt 2 m của mình phơi nắng trên mặt nước như một chiếc đĩa bay tắm nắng! |  | Chú chú Cá Mặt Trăng (ocean sunfish) hoạt hình khổng lồ hình đĩa tròn dẹt màu xám bạc, không có cuống đuôi, hai vây lưng và vây phần đuôi dựng đứng dài ngoằng, nằm ngửa trên chiếc cáng cứu thương quá khổ mắt to tròn ngơ ngác nằm ngang trên mặt biển phẳng lặng như gương, ánh nắng vàng rực rỡ sưởi ấm toàn bộ thân hình tròn dẹt lấp lánh; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b22 | 02:21.2–02:27.1 (5.8s) | L256 | Hành vi tắm nắng này giúp hấp thu tối đa năng lượng mặt trời để sưởi ấm lại các thớ cơ và mạch máu bị đông cứng dưới đáy |  | Dòng nhiệt lượng màu đỏ ấm áp từ ánh nắng mặt trời thẩm thấu qua lớp da làm ấm các mạch nước màu nuôi tim và não bộ; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b23 | 02:27.1–02:36.4 (9.4s) | L257 | sâu! Đồng thời, khi nằm phơi nắng trên mặt nước, các đàn chim biển và cá nhỏ sẽ bu lại rỉa sạch hơn 4 mươi loài ký sinh trùng bám trên da cho nó như một dịch vụ spa biển khơi miễn phí! |  | Đàn mòng biển trắng muốt đậu lên thân cá mặt trăng đang nằm nổi trên mặt nước rỉa sạch các con rận biển bám trên da; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b24 | 02:36.4–02:42.5 (6.0s) | L258 | Nhịp tim của cá mặt trăng khi lặn sâu chỉ khoảng 20 nhịp mỗi phút để tiết kiệm oxy tối đa giữa vùng nước thiếu dưỡng khí! |  | Sơ đồ theo dõi nhịp tim lặn sâu của cá mặt trăng với nhịp đập chậm rãi tiết kiệm năng lượng tuyệt hảo; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b25 | 02:42.5–02:48.6 (6.1s) | L259 | Cơ quan thị giác của nó phát triển vượt trội với đôi mắt to lớn có khả năng nhìn thấu màn đêm đen kịt dưới đáy biển sâu thẳm! |  | Cận cảnh đôi mắt to tròn của cá mặt trăng phản chiếu ánh sáng lân tinh của đàn sứa dưới đáy đại dương; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b26 | 02:48.6–02:55.1 (6.5s) | L260 | Đặc biệt hơn nữa, hệ thống cơ bắp vây lưng của cá mặt trăng tạo ra một lượng nhiệt nội sinh đáng kể trong quá trình bơi lội liên tục! |  | Sơ đồ nhiệt động lực học hiển thị các thớ cơ vây lưng màu đỏ thẫm phát ra luồng nhiệt lượng màu cam sưởi ấm các mô lân cận; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b27 | 02:55.1–03:04.2 (9.1s) | L261 | Mặc dù là loài cá biến nhiệt, nhưng đôi mắt và não bộ của nó được bao bọc bởi một lớp mỡ cách nhiệt đặc biệt giúp giữ ấm cho trung khu thần kinh giữa làn nước buốt giá! |  | Bản vẽ cắt lớp hộp sọ cá mặt trăng hiển thị lớp đệm lipid dày bao quanh hốc mắt và não bộ bảo vệ khỏi cái lạnh âm độ; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b28 | 03:04.2–03:10.0 (5.8s) | L262 | Nhờ lớp mỡ cách nhiệt này, thị lực và phản xạ săn sứa của nó dưới độ sâu 800 m chẳng hề bị tê liệt vì giá |  | Chú cá mặt trăng lướt đi trong bóng tối đại dương lạnh ngắt, đôi mắt vẫn mở to định vị chính xác từng bóng sứa phát quang; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b29 | 03:10.0–03:17.0 (7.0s) | L263 | lạnh! Khi bơi lên mặt nước phơi nắng, dòng máu ấm từ các mạch máu dưới da sẽ được phân phối ngược vào các cơ quan nội tạng bên trong! |  | Đồ họa tuần hoàn nước màu hiển thị các dòng nước màu đỏ ấm áp từ biểu bì chảy ngược vào tim và gan giúp kích hoạt lại quá trình trao đổi chất; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b30 | 03:17.0–03:23.2 (6.2s) | L264 | Đó là một hệ thống sưởi ấm năng lượng mặt trời tuần hoàn tự nhiên hoàn mỹ không tốn một xu tiền điện nào! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án bật cười giơ ngón tay cái tán thưởng cơ chế điều nhiệt độc đáo của người bạn khổng lồ. |
| b31 | 03:23.2–03:30.6 (7.4s) | L265 | Chưa hết đâu nhé! Cá mặt trăng cái còn nắm giữ kỷ lục vô địch tuyệt đối về khả năng sinh sản trong toàn bộ vương quốc động vật có xương sống! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án giơ ngón tay cái lên tỏ vẻ thán phục đỉnh cao trước con số thống kê sinh học phi thường. |
| b32 | 03:30.6–03:36.6 (6.0s) | L266 | Mỗi lần sinh sản, một con cá mặt trăng mẹ có thể phóng thích vào đại dương tới 300 triệu quả trứng cùng một lúc! |  | bảng kẹp bệnh án y khoa khổng lồ (clipboard) kẹp trên giá đỡ kim loại, hiển thị 10 hồ sơ bệnh án hoạt hình với nhãn đơn thuốc phát sáng và sóng nhịp tim ECG màu đỏ nhấp nháy (không có chữ, không có số) rực sáng con số 300.000.000 quả trứng với biểu tượng hàng ngàn tia sáng lấp lánh phát tán khắp đại dương; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b33 | 03:36.6–03:43.3 (6.8s) | L267 | Khi mới nở, con non chỉ dài vỏn vẹn 2 mm, tròn xoe và có gai nhọn bao quanh trông như một chú cá nóc mini tí hon ngộ nghĩnh! |  | Kính hiển vi hiển thị chú cá mặt trăng sơ sinh dài hai mi-li-mét có các gai nhọn bao quanh trông như một ngôi sao biển mini; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b34 | 03:43.3–03:52.2 (8.9s) | L268 | Từ một chấm nhỏ 2 mm đó, nó lớn lên và tăng trọng lượng tới 60 triệu lần để đạt kích thước khổng lồ 2 tấn như bệnh nhân đang nằm trước mặt chúng ta! |  | Sơ đồ tiến hóa kích thước từ ấu trùng hai mi-li-mét phóng đại vọt lên con cá khổng lồ dài ba mét nặng hai tấn; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b35 | 03:52.2–03:59.0 (6.8s) | L269 | Sự gia tăng kích thước tới 60 triệu lần này là kỷ lục tăng trưởng vĩ đại nhất trong toàn bộ thế giới động vật trên Trái Đất! |  | Biểu đồ tăng trưởng dốc đứng hình tên lửa chứng minh sức sống mãnh liệt của loài cá mặt trăng qua hàng triệu năm sóng gió; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b36 | 03:59.0–04:07.0 (8.0s) | L270 | Chẩn đoán Khoa Hồi Sức Cấp Cứu Đại Dương: Bệnh nhân hoàn toàn khỏe mạnh, nhịp tim ổn định, bộ não 4 g đang vận hành cỗ máy 2 tấn ở hiệu suất tuyệt hảo! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười gật đầu hài lòng, đưa tay vỗ nhẹ vào chiếc vây lưng nhô lên khỏi mặt nước của chú chú Cá Mặt Trăng (ocean sunfish) hoạt hình khổng lồ hình đĩa tròn dẹt màu xám bạc, không có cuống đuôi, hai vây lưng và vây phần đuôi dựng đứng dài ngoằng, nằm ngửa trên chiếc cáng cứu thương quá khổ mắt to tròn ngơ ngác. |
| b37 | 04:07.0–04:15.5 (8.5s) | L271 | Đơn thuốc cho bệnh nhân: Tiếp tục ngâm mình thư giãn trong bể nước muối sinh lý, bổ sung một bữa tiệc sứa biển tươi sống và chuẩn bị xe cẩu đưa anh chàng ra vịnh biển lúc rạng đông! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án ký tên vào bệnh án số bốn, chú cá mặt trăng quẫy nhẹ hai chiếc vây làm bọt nước tung tóe như một lời cảm ơn ngây ngô. |
| b38 | 04:15.5–04:25.1 (9.6s) | L272 | Hai giờ 40 phút sáng! Chúng ta đã vượt qua được nửa chặng đường của ca trực đêm kinh hoàng! Toàn đội chuyển ngay sang Khoa Hộp Sọ và Răng Hàm Mặt để xử lý ca bệnh nanh dài đâm trán! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án cùng y tá rảo bước rời khỏi khu hồi sức đại dương, hướng về phía phòng khám nha khoa chuyên dụng. |

### scene08 · NANH DÀI TỰ ĐÂM THỦNG TRÁN · 281.3s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.4 (8.4s) | L273 | Mời bệnh nhân số 5 bước vào ghế nha khoa chuyên dụng! Một ca bệnh răng hàm mặt dị thường đến mức làm các nha sĩ lành nghề nhất cũng phải toát mồ hôi hột! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đứng bên cạnh chiếc ghế nha khoa chuyên dụng có đèn rọi sáng rực rỡ, chú Lợn Hươu Babirusa hoạt hình da xám nhăn nheo ít lông, mõm dài, bốn chiếc răng nanh cong vút dị thường trong đó hai nanh trên mọc xuyên qua sống mũi uốn ngược về phía trán, vẻ mặt lo lắng sờ trán đang ngượng ngùng bước vào phòng khám. |
| b02 | 00:08.4–00:14.9 (6.5s) | L274 | Đó là Lợn Hươu Babirusa đến từ những cánh rừng nhiệt đới ẩm ướt trên đảo Sulawesi hoang sơ thuộc đất nước Indonesia! |  | Cận cảnh gương mặt da xám nhăn nheo của chú Lợn Hươu Babirusa hoạt hình da xám nhăn nheo ít lông, mõm dài, bốn chiếc răng nanh cong vút dị thường trong đó hai nanh trên mọc xuyên qua sống mũi uốn ngược về phía trán, vẻ mặt lo lắng sờ trán, nổi bật là bốn chiếc răng nanh khổng lồ cong vút dị thường nhô ra ngoài; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b03 | 00:14.9–00:21.4 (6.5s) | L275 | Chú lợn rụt rè ngồi lên chiếc ghế nha khoa bọc da êm ái, đưa 2 móng trước lên xoa xoa vầng trán nhăn nheo với vẻ mặt đầy lo lắng. |  | chú Lợn Hươu Babirusa hoạt hình da xám nhăn nheo ít lông, mõm dài, bốn chiếc răng nanh cong vút dị thường trong đó hai nanh trên mọc xuyên qua sống mũi uốn ngược về phía trán, vẻ mặt lo lắng sờ trán ngồi ngay ngắn trên ghế nha khoa, bốn chiếc nanh nhô cao chĩa thẳng vào bóng đèn soi sáng; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b04 | 00:21.4–00:30.1 (8.7s) | L276 | Hãy nhìn vào bộ hàm của anh chàng này mà xem! Đây không phải là răng nanh mọc bình thường, mà là một sự nổi loạn giải phẫu hoàn toàn đi ngược lại mọi quy luật tự nhiên! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án dùng kẹp nha khoa nhẹ nhàng nâng môi trên của bệnh nhân để kiểm tra chân răng. |
| b05 | 00:30.1–00:36.1 (6.0s) | L277 | Hai chiếc răng nanh hàm dưới mọc chìa ra ngoài mép môi nhọn hoắt như 2 lưỡi gươm ngắn đã đủ làm kẻ thù khiếp vía rồi. |  | Bản chụp X-quang xương hàm dưới của lợn babirusa với hai chiếc răng nanh cắm sâu vào xương hàm vững chắc; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b06 | 00:36.1–00:43.3 (7.2s) | L278 | Hai chiếc nanh dưới này sắc như dao cạo, dùng để tự vệ và gạt phăng các đòn tấn công của đối thủ trong những cuộc chiến tranh giành lãnh thổ. |  | Cận cảnh cạnh sắc của chiếc nanh hàm dưới mài mòn tự nhiên tạo thành mép cắt sắc bén; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b07 | 00:43.3–00:50.1 (6.8s) | L279 | Không chỉ dùng để tự vệ, chiếc nanh dưới còn là công cụ hữu hiệu để cắt đứt các dây leo dai nhách khi đi xuyên qua rừng rậm! |  | Chú lợn dùng nanh dưới ngoạm đứt một sợi dây leo vắt ngang lối đi trong rừng già; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b08 | 00:50.1–00:54.1 (4.1s) | L280 | Nhưng điều làm cả giới y học kinh ngạc tột cùng lại nằm ở 2 chiếc răng nanh của hàm |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án chỉ đầu kẹp y tế vào phần sống mũi của chú lợn, nơi hai chiếc nanh trên đâm xuyên qua lớp da mặt. |
| b09 | 00:54.1–01:00.8 (6.7s) | L281 | trên! Thay vì mọc chúc xuống dưới để cắn xé thức ăn như loài lợn rừng hay hổ báo, 2 chiếc răng nanh trên này lại mọc ngược hướng lên |  | Sơ đồ giải phẫu ba chiều hiển thị mầm răng nanh hàm trên xoay ngược một trăm tám mươi độ trong xương hàm; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b10 | 01:00.8–01:09.2 (8.4s) | L282 | trời! Khi bắt đầu phát triển ở độ tuổi trưởng thành, chúng đâm xuyên thẳng qua vòm miệng, xuyên thủng lớp da sống mũi của chính con lợn rồi uốn cong ngược về phía sau trán! |  | Hình ảnh mô phỏng quá trình hai chiếc nanh nhọn hoắt xuyên thủng lớp da thịt sống mũi mọc trồi lên không trung; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b11 | 01:09.2–01:15.4 (6.2s) | L283 | Chiếc nanh cong vút này có thể đạt chiều dài kỷ lục lên tới 40 cm, tạo thành một vòng cung hoàn mỹ ngay trước trán hộp |  | bảng kẹp bệnh án y khoa khổng lồ (clipboard) kẹp trên giá đỡ kim loại, hiển thị 10 hồ sơ bệnh án hoạt hình với nhãn đơn thuốc phát sáng và sóng nhịp tim ECG màu đỏ nhấp nháy (không có chữ, không có số) hiển thị con số 40 cm cùng hình vẽ chiếc nanh cong vút phát sáng vàng kim; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b12 | 01:15.4–01:22.3 (6.9s) | L284 | sọ! Không hề có men răng bao bọc bên ngoài, chiếc nanh này là ngà răng đặc quánh, tiếp tục mọc dài ra liên tục trong suốt toàn bộ cuộc đời của |  | Kính hiển vi soi cấu trúc vi mô của ngà răng lợn babirusa với các ống ngà xếp khít nhau bền vững; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b13 | 01:22.3–01:28.1 (5.8s) | L285 | con vật! Tốc độ mọc của ngà răng có thể đạt vài xăng-ti-mét mỗi 5, đòi hỏi con vật phải có chế độ mài mòn tự nhiên liên |  | Mô hình mặt cắt ngà răng hiển thị các vòng sinh trưởng hàng năm xếp lớp như vân gỗ thân cây; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b14 | 01:28.1–01:36.1 (8.0s) | L286 | tục. Khác với loài voi có ngà mọc từ răng cửa biến tính, ngà của lợn babirusa thực chất là chiếc răng nanh biến dị độc nhất vô nhị trong toàn bộ lớp thú có vú! |  | Sơ đồ so sánh nguồn gốc răng cửa của ngà voi với mầm răng nanh xoay ngược của lợn babirusa; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b15 | 01:36.1–01:42.4 (6.3s) | L287 | Và đây là điều thú vị về mặt di truyền học: Hiện tượng nanh mọc xuyên mũi này chỉ xuất hiện duy nhất ở những con đực trưởng thành! |  | Hình ảnh so sánh hộp sọ của lợn babirusa đực với bốn chiếc nanh khổng lồ bên cạnh hộp sọ lợn cái trơn nhẵn không có nanh trên; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b16 | 01:42.4–01:48.7 (6.3s) | L288 | Những con lợn cái hoàn toàn không hề có nanh trên mọc ngược, nanh dưới của chúng cũng rất nhỏ và nằm gọn gàng bên trong mép môi! |  | Chú lợn cái babirusa gặm lá cây trong rừng với khuôn mặt hiền lành trơn tru không có nanh cong; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b17 | 01:48.7–01:55.0 (6.2s) | L289 | Điều này chứng tỏ cặp nanh trên là một đặc điểm sinh dục thứ cấp đặc trưng, chịu sự điều khiển trực tiếp của nội tiết tố testosterone! |  | Sơ đồ nội tiết hiển thị nồng độ hormone testosterone kích hoạt sự phát triển của mầm ngà xoay ngược ở tuổi dậy thì; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b18 | 01:55.0–02:01.0 (6.1s) | L290 | Đồng thời, cấu tạo dạ dày của lợn babirusa cũng vô cùng kỳ lạ, chia thành nhiều ngăn phức tạp tương tự loài động vật nhai |  | Bản vẽ giải phẫu hệ tiêu hóa của lợn babirusa với dạ dày nhiều túi chứa hàng tỷ vi khuẩn lên men cellulose; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b19 | 02:01.0–02:08.8 (7.8s) | L291 | lại! Nhờ hệ vi sinh vật lên men dạ dày này, lợn babirusa có thể ăn và tiêu hóa được các loại rễ cây rừng chứa nhiều chất xơ dai và độc tố tự nhiên! |  | Chú lợn thản nhiên gặm những nhánh rễ cây có nhựa đắng trong rừng mà không hề bị rối loạn tiêu hóa; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b20 | 02:08.8–02:14.8 (6.0s) | L292 | Để bảo vệ mô mềm quanh sống mũi khỏi bị nhiễm trùng, con lợn thường xuyên đầm mình trong bùn khoáng núi lửa chứa lưu huỳnh tự nhiên! |  | Chú lợn babirusa ngâm mình trong hố bùn khoáng ấm áp, lớp bùn bao bọc quanh chân nanh tạo thành lớp màng bảo vệ vô trùng; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b21 | 02:14.8–02:19.4 (4.6s) | L293 | Bác sĩ trưởng khoa ơi em chụp cắt lớp vi tính hộp sọ cho nó mà 2 tay em run bần bật! |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng cầm tấm phim chụp cắt lớp vi tính CT hộp sọ giơ lên trước hộp đèn sáng, vẻ mặt đầy lo âu sợ hãi. |
| b22 | 02:19.4–02:27.3 (7.9s) | L294 | Đầu nhọn của cái nanh hàm trên nó cong sát sạt vào xương trán rồi! Chỉ cần nó gật đầu mạnh một cái là cái nanh tự cắm phập vào hộp sọ tự sát mất thôi bác sĩ ơi! |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng dùng ngón tay chỉ vào khoảng cách hẹp nghèo nàn giữa chóp nanh nhọn hoắt và bề mặt xương trán của chú lợn; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b23 | 02:27.3–02:32.0 (4.8s) | L295 | Em có nên chuẩn bị một chiếc cưa nha khoa cầm tay để cưa bớt 2 cm chóp nanh ngay bây giờ không ạ? |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng cầm chiếc cưa mini khử trùng bằng cồn giơ lên ngơ ngác hỏi ý kiến bác sĩ; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b24 | 02:32.0–02:39.5 (7.4s) | L296 | Mối lo ngại của cô y tá hoàn toàn có cơ sở khoa học đàng hoàng! Nghiên cứu của nhà nhân chủng học Colin Groves đã ghi nhận những trường hợp cá biệt ngoài tự |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án kẹp tấm phim chụp cắt lớp sọ não lên bảng đèn, dùng bút dạ đỏ khoanh tròn khoảng cách giữa đầu nanh và xương trán. |
| b25 | 02:39.5–02:45.9 (6.4s) | L297 | nhiên: Ở những con lợn hươu đực sống quá thọ trong điều kiện nuôi nhốt hoặc hoang dã, răng nanh của chúng không ngừng mọc dài ra mỗi ngày. |  | Bản vẽ giải phẫu hộp sọ lợn babirusa cổ đại cho thấy đầu răng nanh cong chạm vào bề mặt xương trán; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b26 | 02:45.9–02:52.8 (6.9s) | L298 | Nếu độ cong của nanh quá hẹp, chóp nanh sắc nhọn có thể chạm vào xương trán, chèn ép mô sọ và thậm chí xuyên thủng hộp sọ gây tổn thương não bộ nghiêm |  | Hình ảnh quét ba chiều hộp sọ hiển thị áp lực tiếp xúc giữa chóp răng nanh và bản xương ngoài của hộp sọ; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b27 | 02:52.8–02:59.1 (6.4s) | L299 | trọng! Đó là lý do nhiều nhà khoa học thế kỷ trước từng gọi loài lợn này là sinh vật sở hữu vũ khí tự sát ngớ ngẩn nhất của tự nhiên! |  | Hình vẽ minh họa biếm họa chú lợn tự đâm nanh vào trán bị gạch dấu hỏi chấm to tướng; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b28 | 02:59.1–03:03.4 (4.2s) | L300 | Tuy nhiên những trường hợp tự đâm thủng sọ não đó vô cùng hiếm gặp trong tự nhiên hoang dã! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án chỉ vào cấu trúc xương trán dày dặn có gờ nổi ngăn cản lực đâm của chiếc nanh; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b29 | 03:03.4–03:10.4 (7.0s) | L301 | Trong môi trường rừng nguyên sinh, những cú cọ xát đầu vào thân cây gỗ mun và các cuộc giao đấu liên tục sẽ tự nhiên mài mòn và làm cùn đầu nhọn của chiếc nanh! |  | Chú lợn babirusa cọ mạnh chiếc nanh trên vào thân cây cổ thụ để làm cùn chóp nanh sắc nhọn; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b30 | 03:10.4–03:17.6 (7.2s) | L302 | Nghiên cứu của giáo sư Macdonald còn chỉ ra rằng lớp da quanh chân nanh của lợn babirusa ôm khít lấy thân ngà như một chiếc gioăng cao su sinh học! |  | Kính hiển vi hiển thị mô liên kết biểu bì bám chặt vào chân răng ngăn ngừa hoàn toàn vi khuẩn xâm nhập; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b31 | 03:17.6–03:23.2 (5.6s) | L303 | Vậy tại sao tiến hóa lại ban tặng cho loài lợn này một bộ răng nanh nguy hiểm đến mức độ như thế này? |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án khoanh tay trước ngực, đặt câu hỏi tu từ nhìn thẳng về phía các bác sĩ nội trú đang lắng nghe say mê. |
| b32 | 03:23.2–03:27.5 (4.3s) | L304 | Câu trả lời nằm ở quy luật chọn lọc giới tính khốc liệt suốt hàng triệu 5 qua! |  | Cảnh hai chú lợn babirusa đực đứng thẳng bằng hai chân sau giữa rừng nhiệt đới, dùng mõm và nanh gạt nhau trong cuộc chiến giành bạn tình; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b33 | 03:27.5–03:33.7 (6.2s) | L305 | Các nghiên cứu thực địa gần đây đã chứng minh: lợn babirusa không hề dùng nanh trên để cắn hay đào bới thức ăn dưới đất! |  | Chú lợn dùng mõm dẻo ủi nhẹ lớp lá mục tìm củ rễ cây chứ tuyệt đối không dùng nanh cày xới; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b34 | 03:33.7–03:40.3 (6.6s) | L306 | Khi 2 con đực giao đấu giành bạn tình, chúng đứng thẳng bằng 2 chân sau như 2 võ sĩ quyền anh, dùng mõm tì đè và gạt đòn của |  | Hai chú lợn đứng bằng hai chân sau giằng co quyết liệt giữa bụi cây rậm rạp; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b35 | 03:40.3–03:47.9 (7.5s) | L307 | đối phương! Cặp nanh cong vút trên mặt đóng vai trò như một chiếc khiên chắn bảo vệ đôi mắt và cổ họng của con đực trước những cú cắn hiểm ác của đối thủ! |  | Đồ họa chuyển động chậm mô phỏng chiếc nanh trên gạt phăng cú đâm từ nanh dưới của đối thủ bảo vệ vùng mắt nhạy cảm; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b36 | 03:47.9–03:55.9 (8.0s) | L308 | Đồng thời, con đực nào sở hữu cặp nanh dài và cong hoàn mỹ nhất sẽ chứng minh cho con cái thấy nó có bộ gen kiên cường và sức sống bền bỉ phi thường! |  | Chú chú Lợn Hươu Babirusa hoạt hình da xám nhăn nheo ít lông, mõm dài, bốn chiếc răng nanh cong vút dị thường trong đó hai nanh trên mọc xuyên qua sống mũi uốn ngược về phía trán, vẻ mặt lo lắng sờ trán đực kiêu hãnh ngẩng cao đầu khoe cặp nanh uốn lượn dưới ánh hoàng hôn rừng nhiệt đới; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b37 | 03:55.9–04:00.8 (4.9s) | L309 | Nó giống như chiếc đuôi xòe lộng lẫy của chim công hay cặp sừng đồ sộ của loài hươu đực vậy! |  | Hình ảnh so sánh nanh lợn babirusa với chiếc đuôi rực rỡ sắc màu của chim công đực; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b38 | 04:00.8–04:08.3 (7.5s) | L310 | Càng sở hữu cặp nanh đối xứng và uốn cong chuẩn mực, con đực càng khẳng định được sức khỏe dẻo dai và khả năng sinh sản vượt trội trong bầy đàn! |  | Chú lợn cái ngước nhìn cặp nanh cong tuyệt đẹp của con đực với vẻ say đắm giữa thảm rừng nhiệt đới; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b39 | 04:08.3–04:16.0 (7.7s) | L311 | May mắn thay cho bệnh nhân của chúng ta hôm nay: chóp nanh vẫn cách xương trán tận 2,5 cm, hoàn toàn an toàn và chưa cần phải mài bớt một mi-li-mét nào! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười dùng thước đo y tế kiểm tra khoảng cách, vỗ nhẹ vào bờ vai dày dặn của chú chú Lợn Hươu Babirusa hoạt hình da xám nhăn nheo ít lông, mõm dài, bốn chiếc răng nanh cong vút dị thường trong đó hai nanh trên mọc xuyên qua sống mũi uốn ngược về phía trán, vẻ mặt lo lắng sờ trán. |
| b40 | 04:16.0–04:22.7 (6.8s) | L312 | Chẩn đoán của Phòng Cấp Cứu Tạo Hóa: Hàm răng kỳ dị nhưng là biểu tượng kiêu hãnh của tình yêu và lòng dũng cảm thảo nguyên nhiệt đới! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đóng dấu ĐẠT CHUẨN lên bệnh án số năm, đưa cho chú lợn một túi quả ngọt tráng miệng. |
| b41 | 04:22.7–04:29.4 (6.6s) | L313 | Tôi chỉ cần vệ sinh sạch sẽ vùng chân răng xuyên qua sống mũi và bôi một lớp thuốc sát trùng nhẹ là anh chàng có thể tự tin đi tìm bạn gái được |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án dùng tăm bông thấm thuốc sát trùng màu vàng lau nhẹ chân răng cho chú lợn, chú lợn híp mắt kêu ụt ịt tỏ vẻ hài lòng. |
| b42 | 04:29.4–04:34.6 (5.2s) | L314 | rồi! Anh bạn lợn hươu hãy nhớ thường xuyên đầm mình trong bùn khoáng để sát trùng tự nhiên cho 2 bên sống mũi nhé! |  | Chú chú Lợn Hươu Babirusa hoạt hình da xám nhăn nheo ít lông, mõm dài, bốn chiếc răng nanh cong vút dị thường trong đó hai nanh trên mọc xuyên qua sống mũi uốn ngược về phía trán, vẻ mặt lo lắng sờ trán gật gù hiểu ý, hai tai vẫy vẫy vui mừng chuẩn bị rời ghế nha khoa; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b43 | 04:34.6–04:41.3 (6.7s) | L315 | Hồ sơ Khoa Nha Khoa Dị Tật hoàn tất mỹ mãn! Giờ thì nghe kìa, tiếng la hét ngoài sảnh báo hiệu đợt náo loạn thứ 2 vừa nổ ra! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án cất chiếc panh nha khoa, chạy vội ra hành lang xem chuyện gì đang xảy ra tiếp theo. |

### scene09 · BA MƯƠI NGÀN MŨI KIM TIÊM · 247.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.3 (7.3s) | L316 | Ba giờ 30 phút sáng. Cơn buồn ngủ bắt đầu kéo sụp 2 mí mắt của tôi xuống, thì một tiếng thét thất thanh lại vang lên từ phía cuối hành lang! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đang ngồi ghi chép bệnh án tại quầy trực thì giật mình đánh rơi chiếc bút bi, tiếng kêu la hoảng hốt vọng lại từ sảnh chờ. |
| b02 | 00:07.3–00:12.5 (5.2s) | L317 | Tôi giật bắn mình đánh rơi chiếc bút bi xuống bàn, vội vàng đứng bật dậy chạy ra ngoài xem chuyện gì vừa xảy ra. |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mở tung cửa phòng nha khoa, sải bước dài hướng về phía sảnh phòng chờ đang ồn ào như ong vỡ tổ. |
| b03 | 00:12.5–00:18.6 (6.0s) | L318 | Ái da da! Đau điếng người thế này! Cứu em với bác sĩ ơi! Có ai vừa rải một bãi chông sắt khắp sàn nhà hành lang bệnh viện |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng một tay ôm một bên chân đang co lên nhảy lò cò, dưới đế dép cao su cắm chi chít năm sáu chiếc gai nhọn trắng đen; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b04 | 00:18.6–00:25.6 (7.0s) | L319 | thế này! Cô y tá vừa ôm một bên chân vừa nhảy lò cò trên một chân còn lại, khuôn mặt mếu máo đau đớn như vừa dẫm phải bẫy chông thời cổ đại! |  | Cận cảnh chiếc dép y tế màu xanh bằng cao su xốp bị đâm thủng bởi những chiếc gai nhọn có hai màu đen trắng đan xen; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b05 | 00:25.6–00:31.9 (6.3s) | L320 | Thủ phạm của vụ rải chông liên hoàn này không ai khác chính là chú Nhím Lông Nhọn Bắc Mỹ béo tròn đang lững thững đi dạo cạnh các dãy ghế! |  | chú Nhím Lông Nhọn Bắc Mỹ hoạt hình béo tròn xù xì, toàn thân phủ kín ba mươi ngàn chiếc gai nhọn trắng đen, đang ôm chặt một thân cây gỗ gặm vỏ thuốc, người tỏa mùi tinh dầu thơm nhẹ béo ú tròn xoe như quả bóng gai, vẻ mặt ngây thơ vô tội đang gặm dở một khúc gỗ mục của chiếc ghế băng bệnh viện; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b06 | 00:31.9–00:38.2 (6.3s) | L321 | Chú nhím vừa đi vừa cọ cọ chiếc lưng béo ú vào mép tường bê tông, làm rụng lả tả hàng chục chiếc gai nhọn cắm phập xuống sàn gạch |  | Những chiếc gai nhọn cắm thẳng đứng trên sàn nhà như những chiếc đinh ba mini, phản chiếu ánh sáng đèn tuýp lấp lánh; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b07 | 00:38.2–00:44.6 (6.4s) | L322 | men! Các bệnh nhân khác xung quanh hoảng hốt nhảy tót lên ghế băng, co chân lên cao để tránh bãi mìn sinh học đang lan rộng! |  | Chú khỉ đột ngồi co ro trên lưng ghế sắt, hai mắt tròn xoe nhìn bãi gai nhọn dưới sàn vẻ đầy kiêng dè; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b08 | 00:44.6–00:49.3 (4.7s) | L323 | Đứng yên! Tất cả nhân viên và bệnh nhân trong sảnh đứng yên tại chỗ không được bước thêm một bước nào! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án cầm chiếc đèn pin y tế bật sáng quét dọc sàn nhà, ánh sáng rọi lên hàng chục chiếc gai nhọn cắm lởm chởm trên sàn gạch men như một bãi mìn chông; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b09 | 00:49.3–00:56.3 (7.0s) | L324 | Tôi lập tức bật chiếc đèn pin y tế công suất lớn quét dọc mặt sàn, rọi sáng một bãi mìn sinh học dày đặc trải dài từ quầy thuốc tới cửa phòng khám! |  | Luồng ánh sáng trắng của đèn pin quét qua mặt sàn gạch, làm lộ rõ hàng trăm chiếc gai nhọn cắm chi chít khắp lối đi; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b10 | 00:56.3–01:02.0 (5.8s) | L325 | Mọi người nghe cho rõ đây: Tuyệt đối không ai được dùng tay không để nhổ những chiếc gai này ra khỏi da thịt hay đế giày! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án nghiêm giọng cảnh báo, dùng một chiếc kẹp y tế chuyên dụng gắp nhẹ một chiếc gai nhọn lên đưa vào dưới ánh đèn soi. |
| b11 | 01:02.0–01:07.4 (5.3s) | L326 | Nhiều người xem phim hoạt hình thường lầm tưởng rằng nhím có khả năng co cơ phóng gai bay vèo vèo như tên bắn về phía kẻ |  | Hình ảnh biếm họa chú nhím bắn gai vèo vèo bị gạch một dấu chéo đỏ to tướng biểu thị tin đồn sai lệch; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b12 | 01:07.4–01:13.5 (6.2s) | L327 | thù. Điều đó hoàn toàn sai sự thật 100%! Nhím không hề có bất kỳ bó cơ nào có thể bắn gai ra ngoài không gian! |  | Chú nhím cuộn tròn thành quả cầu gai xù xì, các cơ dưới da chỉ có tác dụng dựng đứng các sợi gai lên dựng ngược; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b13 | 01:13.5–01:17.6 (4.1s) | L328 | Nhưng cơ chế tháo rời lông gai thụ động của nó thì tinh vi và nguy hiểm hơn súng đạn gấp trăm |  | Cận cảnh gốc nang lông của nhím gắn hờ hững vào lớp da, chỉ cần một va chạm nhẹ là gốc gai lập tức tách rời khỏi cơ thể con nhím; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b14 | 01:17.6–01:23.6 (6.0s) | L329 | lần! Trước khi rụng gai, con nhím thường phát ra những tiếng nghiến răng ken két như tiếng cảnh báo gầm gừ để xua đuổi đối thủ! |  | Chú nhím nghiến răng ken két, hai má phập phồng đe dọa trước khi vung chiếc đuôi ngắn cắm đầy gai; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b15 | 01:23.6–01:29.7 (6.1s) | L330 | Cú quất đuôi của nhím có thể đạt vận tốc tới 20 m mỗi giây, cắm phập hàng chục mũi chông vào mõm kẻ săn mồi trong chớp mắt! |  | Đồ họa chuyển động chậm mô phỏng chiếc đuôi nhím quất ngang với gia tốc cực lớn cắm gai vào mục tiêu; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b16 | 01:29.7–01:37.3 (7.6s) | L331 | Gốc nang lông của chiếc gai gắn vào lớp da con nhím vô cùng lỏng lẻo, chỉ cần một va quẹt nhẹ như một cái phẩy tay là chiếc gai tự động rụng ra ngay lập tức. |  | Hình vẽ giải phẫu gốc nang lông hình củ hành siêu nhỏ gắn hờ hững vào biểu bì da của chú nhím lông nhọn; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b17 | 01:37.3–01:43.1 (5.8s) | L332 | Toàn bộ cơ thể của một con nhím lông nhọn Bắc Mỹ trưởng thành được bao bọc bởi hơn 30.000 chiếc lông gai sắc nhọn! |  | bảng kẹp bệnh án y khoa khổng lồ (clipboard) kẹp trên giá đỡ kim loại, hiển thị 10 hồ sơ bệnh án hoạt hình với nhãn đơn thuốc phát sáng và sóng nhịp tim ECG màu đỏ nhấp nháy (không có chữ, không có số) bật sáng con số 30.000 chiếc gai rực rỡ bên cạnh hình ảnh đồ họa chiếc lông nhím; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b18 | 01:43.1–01:50.0 (6.9s) | L333 | Mỗi chiếc gai thực chất là một sợi lông biến tính rỗng ruột bên trong, cực kỳ nhẹ nhưng lại cứng cáp phi thường nhờ cấu trúc vách xốp tổ ong. |  | Bản vẽ cắt ngang sợi lông nhím hiển thị cấu trúc tổ ong xốp bên trong giúp tăng độ cứng và giảm trọng lượng tối đa; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b19 | 01:50.0–01:56.3 (6.3s) | L334 | Nhờ cấu trúc rỗng xốp chứa đầy không khí này, hàng chục ngàn chiếc gai còn đóng vai trò như một chiếc áo phao cứu sinh tự nhiên hoàn |  | Chú nhím bơi lội ung dung trên mặt nước sông, toàn bộ cơ thể nổi bồng bềnh nhờ lớp gai rỗng xốp nâng đỡ; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b20 | 01:56.3–02:02.3 (6.1s) | L335 | hảo! Khi gặp lũ quét rừng hay cần vượt sông tìm thức ăn, con nhím có thể bơi qua những khúc sông rộng mà không sợ bị chìm |  | Hình ảnh chú nhím thản nhiên bơi qua dòng suối cuồn cuộn giữa rừng già Bắc Mỹ; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b21 | 02:02.3–02:09.0 (6.7s) | L336 | nghỉm! Và đây là bí mật khủng khiếp nhất khiến các bác sĩ ngoại khoa phải rùng mình kinh hãi: Cấu trúc vi cơ học ở phần chóp nhọn của mỗi chiếc |  | Kính hiển vi điện tử phóng đại chóp nhọn của chiếc gai nhím lên hàng nghìn lần, làm lộ ra một cấu trúc cơ học đáng sợ; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b22 | 02:09.0–02:15.6 (6.6s) | L337 | gai! Ở phần đầu của mỗi chiếc gai có chứa tới 7 trăm đến 800 chiếc vi ngạnh ngược siêu nhỏ xếp tầng tầng lớp lớp như vảy cá mập! |  | Hàng trăm chiếc vảy ngạnh ngược sắc lẹm nhô ra hướng về phía sau như những chiếc lưỡi câu mini đan kết dày đặc; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b23 | 02:15.6–02:21.5 (5.9s) | L338 | Những chiếc vi ngạnh này nhỏ đến mức mắt thường không thể nhìn thấy, nhưng chúng sắc bén vô song và cực kỳ dẻo dai! |  | Kính hiển vi điện tử quét màu hiển thị các lưỡi ngạnh ngược bằng chất sừng keratin cứng cáp như mũi kim thép; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b24 | 02:21.5–02:27.8 (6.3s) | L339 | Nghiên cứu của tiến sĩ Cho công bố trên tạp chí Viện Hàn Lâm Khoa Học Hoa Kỳ PNAS đã đo đạc chính xác lực tác động cơ học này: |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án giơ bản đồ thị lực kéo và lực đâm của lông nhím lên trước mặt toàn thể y bác sĩ. |
| b25 | 02:27.8–02:34.5 (6.7s) | L340 | Khi đâm vào da thịt, các vi ngạnh ngược này nằm ép sát xuôi chiều vào thân gai, giúp giảm tới 54% lực đâm so với kim tiêm y tế thông thường! |  | Mũi tên đồ họa màu xanh mô phỏng chiếc gai xuyên ngọt ngào qua lớp da với lực cản cực thấp; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b26 | 02:34.5–02:39.6 (5.1s) | L341 | Nhờ đó, chiếc gai có thể xuyên ngọt lịm qua lớp da thịt dày cộp của kẻ thù chỉ bằng một cú quẫy đuôi nhẹ |  | Hình ảnh chiếc gai nhọn đâm xuyên qua lớp lông dày của một chú sói rừng đang cố tấn công con nhím; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b27 | 02:39.6–02:46.3 (6.7s) | L342 | nhàng! Nhưng một khi đã cắm sâu vào trong cơ thịt, các vi ngạnh này lập tức hút ẩm từ dịch mô cơ thể rồi xòe bung ra như những chiếc mỏ neo mini! |  | Khi có lực kéo ngược ra ngoài, hàng trăm chiếc vảy ngạnh lập tức móc chặt vào các sợi cơ thịt xung quanh; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b28 | 02:46.3–02:53.1 (6.8s) | L343 | Lực cần thiết để rút chiếc gai ra tăng vọt lên gấp 3 lần so với lực đâm vào, gây đau đớn dữ dội và xé rách các mô xung quanh nếu cố giật mạnh bằng tay! |  | Đồ thị lực kéo nhảy vọt lên đỉnh đỏ rực, mô phỏng cảm giác đau đớn khi cố tình giật chiếc gai ra bằng tay không; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b29 | 02:53.1–02:59.5 (6.4s) | L344 | Chất keratin ở chóp gai khi ngậm nước mô còn trương nở nhẹ, khiến độ bám dính của các ngạnh ngược càng thêm chắc chắn và khó tách rời! |  | Kính hiển vi điện tử quét hiển thị các phiến ngạnh ngậm nước nở to khóa chặt lấy các thớ cơ thịt; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b30 | 02:59.5–03:08.5 (9.0s) | L345 | Thậm chí, nếu không được gắp ra đúng kỹ thuật ngoại khoa, sự co bóp tự nhiên của các thớ cơ sẽ khiến chiếc gai tự động di chuyển sâu hơn vào trong cơ thể mỗi ngày vài mi-li-mét! |  | Sơ đồ y học minh họa chiếc gai nhím tự trườn sâu vào mô mỡ theo nhịp co bóp của cơ bắp; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b31 | 03:08.5–03:16.7 (8.2s) | L346 | Đã từng có những con gấu hay báo sư tử bị gai nhím cắm vào mõm, chiếc gai tự trườn xuyên qua má, đâm vào mạch máu lớn hoặc mắt gây tử vong thương tâm! |  | Bản vẽ hộp sọ của loài dã thú săn mồi với những chiếc gai nhím đâm sâu vào các hốc mô mềm; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b32 | 03:16.7–03:24.0 (7.3s) | L347 | Nên cô y tá hãy ngồi yên trên ghế để tôi dùng kìm kẹp y tế chuyên dụng xoay nhẹ góc 45 độ rồi rút dứt khoát theo trục thẳng đứng nhé! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án quỳ một chân xuống, thao tác khéo léo dùng kìm kẹp từng chiếc gai cắm trên đế dép và gấu quần của y tá gắp ra an toàn. |
| b33 | 03:24.0–03:31.1 (7.1s) | L348 | Thao tác xoay nhẹ góc 45 độ này giúp các vi ngạnh ngược uốn cong mềm mại theo thớ cơ, giải phóng lực móc neo mà không làm rách mô tế |  | Mô hình 3D minh họa động tác xoay kẹp y tế làm gập các vảy ngạnh ngược giúp rút gai ra êm ái; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b34 | 03:31.1–03:40.5 (9.4s) | L349 | bào! Tách! Chiếc gai cuối cùng đã được đưa vào khay nhôm vô trùng. Sảnh phòng chờ của Phòng Cấp Cứu Tạo Hóa thở phào nhẹ nhõm như vừa vượt qua một bãi mìn sinh học! |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng xoa xoa gấu quần thở phào, các bệnh nhân xung quanh vỗ tay hoan hô tài nghệ của Bác Sĩ Trưởng Khoa. |
| b35 | 03:40.5–03:47.0 (6.5s) | L350 | Được rồi anh bạn nhím béo tròn, mời anh vào phòng khám Khoa Da Liễu ngay để kiểm tra xem lớp kháng sinh tự nhiên trên lưng anh còn đủ dùng không |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án dùng một chiếc chổi y tế gom các sợi gai rụng trên sàn, vỗ nhẹ vào chiếc mõm tròn của chú chú Nhím Lông Nhọn Bắc Mỹ hoạt hình béo tròn xù xì, toàn thân phủ kín ba mươi ngàn chiếc gai nhọn trắng đen, đang ôm chặt một thân cây gỗ gặm vỏ thuốc, người tỏa mùi tinh dầu thơm nhẹ đang chớp mắt ngây thơ. |
| b36 | 03:47.0–03:51.6 (4.6s) | L351 | nhé! Tôi yêu cầu chú nhím phải đi theo đường kẻ vạch cách ly màu vàng để không làm rụng gai thêm một lần nào |  | Chú chú Nhím Lông Nhọn Bắc Mỹ hoạt hình béo tròn xù xì, toàn thân phủ kín ba mươi ngàn chiếc gai nhọn trắng đen, đang ôm chặt một thân cây gỗ gặm vỏ thuốc, người tỏa mùi tinh dầu thơm nhẹ ngoan ngoãn đi theo vạch sơn vàng trên sàn nhà, hai mắt chớp chớp vẻ hối lỗi ngộ nghĩnh; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b37 | 03:51.6–03:58.9 (7.3s) | L352 | nữa! Bốn chiếc bàn chân bọc gai thịt xù xì của chú nhím bước đi lẹp xẹp ngoan ngoãn theo sau lưng bác sĩ, không dám cọ lưng vào tường thêm một lần |  | Chú nhím bước từng bước chậm rãi trên thảm trải cách ly, các y bác sĩ khẽ mỉm cười trước dáng đi vụng về đáng yêu; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b38 | 03:58.9–04:07.4 (8.5s) | L353 | nào! Ca trực đêm vẫn còn 2 chuyên khoa hóc búa nhất đang chờ đón: Khoa Tuần Hoàn Áp Suất Cao và Khoa Rối Loạn Hành Vi! Toàn đội tiếp tục chiến đấu nào! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án cất chiếc kìm vào túi áo, hướng thẳng bước chân về phía phòng khám tuần hoàn áp lực cao ở cuối hành lang. |

### scene10 · HUYẾT ÁP TÂM THU HAI TRĂM TÁM · 265.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.2 (7.2s) | L354 | Bíp! Bíp! Bíp! Tiếng còi báo động quá tải áp suất từ chiếc máy đo huyết áp kỹ thuật số vang lên dồn dập ngay khi chúng tôi bước vào phòng khám tuần hoàn! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án cùng cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng bước nhanh vào phòng khám có trang bị hệ thống máy đo huyết áp áp lực cao, kim đồng hồ đo áp lực nhảy vọt lên vạch đỏ chót; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b02 | 00:07.2–00:14.6 (7.4s) | L355 | Bệnh nhân số 7 của chúng ta đang đứng gục đầu bên cửa sổ: Quý cô Hươu Cao Cổ cao tới 5 m, chiếc cổ dài 2 m buông thõng vẻ mệt mỏi rã rời! |  | Toàn cảnh chú Hươu Cao Cổ hoạt hình cao lêu nghêu có đốm hoa văn nâu vàng, chiếc cổ dài thẳng tắp quấn dải băng đo huyết áp y tế to bản màu đỏ, mắt to hiền từ chớp chớp cao năm mét với bộ lông hoa văn màu hạt dẻ tuyệt đẹp, chiếc cổ dài cong cong gục đầu tựa vào khung cửa sổ kính phòng khám; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b03 | 00:14.6–00:22.0 (7.4s) | L356 | Chỉ số huyết áp hiển thị trên màn hình điện tử làm toàn thể các bác sĩ tim mạch phải lạnh gáy kinh hoàng: 200 8 mươi trên 180 mi-li-mét thủy ngân! |  | bảng kẹp bệnh án y khoa khổng lồ (clipboard) kẹp trên giá đỡ kim loại, hiển thị 10 hồ sơ bệnh án hoạt hình với nhãn đơn thuốc phát sáng và sóng nhịp tim ECG màu đỏ nhấp nháy (không có chữ, không có số) bật sáng chỉ số huyết áp 280/180 mmHg nhấp nháy đỏ rực kèm theo tiếng còi cảnh báo cấp cứu khẩn cấp; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b04 | 00:22.0–00:28.9 (6.9s) | L357 | Mức huyết áp tâm thu lên tới 280 mmHg! Cao gấp hơn 2 lần chỉ số huyết áp bình thường của một người trưởng thành khỏe mạnh! |  | Màn hình điện tâm đồ hiển thị các đường sóng áp lực cao vút như những đỉnh núi nhọn hoắt; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b05 | 00:28.9–00:35.5 (6.6s) | L358 | Ở một người bình thường, mức huyết áp khủng khiếp này sẽ làm vỡ tan các mạch máu não, gây xuất huyết não và tử vong tức thì trong vài phút! |  | Sơ đồ y học hiển thị nguy cơ vỡ phình mạch nước màu não ở người khi huyết áp vượt ngưỡng hai trăm mi-li-mét thủy ngân; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b06 | 00:35.5–00:43.0 (7.4s) | L359 | Thế nhưng quý cô hươu cao cổ của chúng ta vẫn đứng vững vàng, chỉ hơi hoa mắt và chóng mặt nhẹ sau khi vừa cúi gập người xuống uống nước suối bên ngoài sảnh! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án ngước nhìn lên đỉnh đầu chú hươu cao cổ cách mặt đất hơn ba mét, đưa ống nghe chuyên dụng lên kiểm tra nhịp đập động mạch cảnh. |
| b07 | 00:43.0–00:49.0 (6.0s) | L360 | Nhịp tim của bệnh nhân đập mạnh đến mức tôi có thể nhìn thấy từng đợt sóng máu dâng lên cuồn cuộn dọc theo tĩnh mạch cổ dài 2 m! |  | Cận cảnh chiếc cổ thon dài của hươu cao cổ với các mạch nước màu lớn phập phồng nhịp nhàng dưới lớp da lông ngắn mịn; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b08 | 00:49.0–00:53.6 (4.6s) | L361 | Bác sĩ ơi, có phải cô hươu này bị cơn bão tăng huyết áp kịch phát ác tính không ạ? |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng cầm chiếc ống tiêm thuốc hạ áp khẩn cấp run run ngước nhìn bác sĩ trưởng khoa xin chỉ thị; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b09 | 00:53.6–00:59.7 (6.1s) | L362 | Em có nên tiêm ngay một liều thuốc chẹn kênh canxi liều cao để hạ huyết áp của cô ấy xuống mức 120 không bác sĩ? |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng băn khoăn giơ lọ thuốc hạ áp ra trước mặt bác sĩ với vẻ mặt đầy lo lắng; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b10 | 00:59.7–01:05.9 (6.2s) | L363 | Bác sĩ trưởng khoa ơi nếu cô ấy cúi đầu xuống uống nước một lần nữa thì huyết áp có dồn lên làm nổ tung não bộ của cô ấy không ạ? |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng ôm chiếc máy đo huyết áp, ánh mắt tròn xoe nhìn chiếc cổ dài miên man của chú hươu cao cổ; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b11 | 01:05.9–01:11.9 (6.0s) | L364 | Nhìn chiếc cổ dài 2 m ngoằn ngoèo kia mà em tưởng tượng như một đường ống dẫn dầu cao áp xuyên lục địa vậy bác sĩ ơi! |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng giơ hai tay miêu tả độ cao chót vót của đầu hươu cao cổ so với mặt đất; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b12 | 01:11.9–01:20.1 (8.2s) | L365 | Và còn một điều kỳ lạ nữa bác sĩ ơi: Dây thần kinh điều khiển thanh quản của cô ấy dài tới 4,5 m lận đó bác sĩ, sao tiến hóa lại đi đường vòng xa xôi thế ạ? |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng chỉ vào sơ đồ giải phẫu thần kinh cổ hươu cao cổ với đường chạy ngoằn ngoèo bất thường; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b13 | 01:20.1–01:27.9 (7.8s) | L366 | Tuyệt đối cấm tiêm thuốc hạ áp cô y tá nhé! Nếu hạ huyết áp của cô ấy xuống 120 thì cô ấy sẽ đột tử vì thiếu máu não ngay lập tức đấy! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án nghiêm giọng ra lệnh, nhẹ nhàng gạt ống tiêm thuốc hạ áp sang một bên. |
| b14 | 01:27.9–01:34.1 (6.2s) | L367 | Đây là mức huyết áp hoàn toàn bình thường và bắt buộc phải có để duy trì sự sống cho sinh vật cao nhất trên cạn này! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án dùng phấn vẽ lên bảng sơ đồ cột áp thủy tĩnh của cột nước màu cao hai mét từ tim lên não hươu cao cổ. |
| b15 | 01:34.1–01:38.4 (4.3s) | L368 | Hãy làm một bài toán vật lý thủy tĩnh đơn giản mà bất kỳ kỹ sư nào cũng phải thán phục: |  | Sơ đồ vật lý cơ học hiển thị cột chất lỏng cao hai mét cần một áp suất bơm tối thiểu một trăm mi-li-mét thủy ngân chỉ để thắng trọng lực Trái Đất; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b16 | 01:38.4–01:43.8 (5.4s) | L369 | Trái tim của hươu cao cổ nằm cách bộ não ở trên đỉnh đầu một khoảng cách xa tới 2 m theo phương thẳng |  | Hình ảnh giải phẫu vị trí trái tim khổng lồ trong lồng ngực hươu cao cổ nối với bộ não trên cao bằng động mạch cảnh dài hai mét; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b17 | 01:43.8–01:55.2 (11.4s) | L370 | đứng! Để bơm được máu thắng được trọng lực Trái Đất và đẩy dòng máu lên tới đỉnh đầu với áp lực tưới máu não đủ 100 mi-li-mét thủy ngân, trái tim bắt buộc phải tạo ra một áp suất bơm tại gốc lên tới 280! |  | Đồ họa dòng nước màu đỏ tươi được bơm vọt lên cao qua động mạch cảnh như một chiếc máy bơm nước tăng áp; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b18 | 01:55.2–02:03.2 (7.9s) | L371 | Nếu huyết áp hạ xuống 120 như người, áp lực cột nước sẽ khiến dòng máu không thể leo lên tới hộp sọ, làm con vật ngất xỉu ngay tức khắc! |  | Đồ họa minh họa não bộ hươu cao cổ bị thiếu nước màu trắng bệch nếu áp lực bơm tim không đủ mạnh; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b19 | 02:03.2–02:09.2 (6.0s) | L372 | Để thực hiện được kỳ tích thủy lực đó, tạo hóa đã trang bị cho hươu cao cổ một trái tim quái vật nặng tới 11 kg! |  | bảng kẹp bệnh án y khoa khổng lồ (clipboard) kẹp trên giá đỡ kim loại, hiển thị 10 hồ sơ bệnh án hoạt hình với nhãn đơn thuốc phát sáng và sóng nhịp tim ECG màu đỏ nhấp nháy (không có chữ, không có số) hiển thị con số 11 kg cùng hình ảnh quả tim khổng lồ đập thình thịch với sức mạnh phi thường; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b20 | 02:09.2–02:16.0 (6.8s) | L373 | Thành tâm thất trái của nó dày tới 7,5 cm, dày gấp 3 lần tâm thất người, tạo ra lực bóp mạnh như một chiếc máy bơm piston công nghiệp! |  | Bản chụp cắt lớp tim hươu cao cổ cho thấy lớp cơ tim tâm thất trái dày cộp đặc quánh chịu được áp lực cực đại; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b21 | 02:16.0–02:24.6 (8.5s) | L374 | Thế nhưng câu hỏi hóc búa nhất mà giới sinh lý học từng đau đầu là: Khi hươu cao cổ cúi gập đầu xuống đất uống nước, điều gì ngăn dòng máu áp suất cực đại đó tràn xuống làm nổ tung các mạch máu |  | Hình ảnh mô phỏng hươu cao cổ dạng hai chân trước cúi đầu xuống mặt nước suối uống nước; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b22 | 02:24.6–02:31.6 (7.1s) | L375 | não? Bởi vì khi cúi đầu, trọng lực sẽ cộng dồn với áp lực bơm tim, đẩy áp suất máu tại não vọt lên hơn 400 mi-li-mét thủy ngân trong tích tắc! |  | Mũi tên đỏ đồ họa hiển thị áp lực thủy tĩnh tăng vọt dồn về phía hộp sọ khi đầu hạ thấp xuống mặt đất; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b23 | 02:31.6–02:37.0 (5.3s) | L376 | Và khi đứng thẳng dậy đột ngột, áp lực máu lại tụt dốc không phanh, đe dọa gây thiếu máu não cục bộ nghiêm trọng! |  | Đồ thị áp suất nhấp nháy chuyển màu xanh dương biểu thị nguy cơ tụt huyết áp tư thế khi đầu ngẩng cao; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b24 | 02:37.0–02:43.4 (6.5s) | L377 | Câu trả lời nằm ở một tuyệt tác vi mạch sinh học tại đáy hộp sọ mang tên: Mạng lưới mạch kỳ diệu Rete mirabile! |  | Sơ đồ giải phẫu đáy sọ hươu cao cổ hiển thị một búi mạch nước màu dày đặc đan xen chằng chịt như mạng nhện phát sáng vàng rực; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b25 | 02:43.4–02:50.2 (6.8s) | L378 | Ngay trước khi dòng máu đi vào não bộ, động mạch cảnh phân nhánh thành hàng ngàn tiểu động mạch đàn hồi đan xen chằng chịt như một miếng bọt biển sinh học. |  | Búi mạch nước màu Rete mirabile hoạt động như một hồ chứa đệm hấp thu và phân tán toàn bộ xung lực áp suất dư thừa; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b26 | 02:50.2–02:56.6 (6.4s) | L379 | Mạng lưới này hoạt động chính xác như một bể giảm áp thủy lực, hấp thu và triệt tiêu toàn bộ sóng áp suất cao đột ngột khi con vật cúi |  | Đồ họa mô phỏng dòng nước màu áp lực cao bị phân tán chậm rãi qua mạng lưới vi mạch, áp suất tại mô não được duy trì ổn định tuyệt đối; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b27 | 02:56.6–03:04.1 (7.5s) | L380 | đầu! Đồng thời, trong các tĩnh mạch cảnh dài 2 m ở cổ có chứa hàng loạt van một chiều đóng kín lại, ngăn không cho máu tĩnh mạch chảy ngược về não bộ! |  | Cận cảnh các van tĩnh mạch một chiều hình bán nguyệt đóng chặt lại ngăn chặn dòng nước màu trào ngược; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b28 | 03:04.1–03:11.4 (7.4s) | L381 | Và ở phần chân dưới, lớp da dày cộp và các cân cơ siết chặt hoạt động y hệt như bộ đồ bay chống quá tải trọng trường G-suit của các phi công chiến đấu phản lực! |  | Đồ họa so sánh lớp da chân căng cứng của hươu cao cổ với bộ đồ bay kháng áp G-suit của phi công tiêm kích; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b29 | 03:11.4–03:17.8 (6.4s) | L382 | Nhờ lớp da chân bó chặt này, áp lực máu cao không thể làm vỡ mao mạch hay gây phù nề chân dù con vật đứng liên tục suốt cả ngày |  | Chú hươu cao cổ sải những bước chân thanh thoát và vững chãi trên mặt đất mà không hề bị sưng phù mắt cá chân; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b30 | 03:17.8–03:25.0 (7.2s) | L383 | đêm! Cơ quan Hàng Không Vũ Trụ Hoa Kỳ NASA đã nghiên cứu cấu trúc da chân này để chế tạo trang phục kháng áp cho các phi hành gia bay vào vũ trụ! |  | Bản thiết kế bộ đồ phi hành gia của NASA đặt cạnh sơ đồ cấu trúc da chân hươu cao cổ phát sáng công nghệ cao; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b31 | 03:25.0–03:32.3 (7.4s) | L384 | Và về câu hỏi của cô y tá về dây thần kinh thanh quản quặt ngược dài 4,5 m: đó chính là dấu tích tiến hóa kinh điển từ tổ tiên loài cá cổ đại! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười giải thích, vẽ sơ đồ tiến hóa cung động mạch mang cá biến đổi thành quai động mạch chủ ở động vật có vú. |
| b32 | 03:32.3–03:40.9 (8.6s) | L385 | Khi cổ của loài hươu ngày càng vươn dài ra qua hàng triệu 5, dây thần kinh bị quai động mạch chủ níu giữ nên phải kéo dài theo thành một vòng lặp ngoạn mục dài 4,5 m! |  | Sơ đồ chuyển động đồ họa hiển thị dây thần kinh chạy từ não xuống tận tim rồi vòng ngược lên thanh quản ở cổ; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b33 | 03:40.9–03:47.8 (6.9s) | L386 | Hơn nữa, vì phải luôn cảnh giác trước các loài thú săn mồi và duy trì áp suất tuần hoàn phức tạp, hươu cao cổ chỉ ngủ chợp mắt khoảng 30 phút mỗi |  | Chú hươu cao cổ đứng tựa đầu vào thân cây chợp mắt năm phút giữa bóng đêm thảo nguyên tĩnh mịch; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b34 | 03:47.8–03:55.3 (7.5s) | L387 | ngày! Những giấc ngủ ngắn ngủi kéo dài từ 5 đến 10 phút chia làm nhiều lần trong ngày giúp nó vừa phục hồi năng lượng vừa giữ an toàn tuyệt đối! |  | Biểu đồ theo dõi sóng não giấc ngủ của hươu cao cổ với các chu kỳ ngủ nông ngắn ngủi luân phiên; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b35 | 03:55.3–04:02.2 (6.9s) | L388 | Chẩn đoán Khoa Tuần Hoàn Áp Suất Cao của Phòng Cấp Cứu Tạo Hóa: Bệnh nhân sở hữu hệ thống thủy lực tuần hoàn hoàn hảo nhất thế giới động vật! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười gật đầu tán thưởng, xoa nhẹ chiếc cằm dài của quý cô hươu cao cổ đang chớp đôi mắt to tròn có hàng mi rợp bóng. |
| b36 | 04:02.2–04:11.4 (9.2s) | L389 | Đơn thuốc cho bệnh nhân: Một bó cành lá keo tươi non gắn trên giá treo cao 3 m và dặn bệnh nhân mỗi lần cúi đầu uống nước thì nhớ đứng dạng chân chậm rãi thôi nhé! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án treo bó lá keo xanh mướt lên móc cao, chú chú Hươu Cao Cổ hoạt hình cao lêu nghêu có đốm hoa văn nâu vàng, chiếc cổ dài thẳng tắp quấn dải băng đo huyết áp y tế to bản màu đỏ, mắt to hiền từ chớp chớp thích thú vươn chiếc lưỡi dài màu xanh đen dài bốn mươi phân cuốn lấy nhai ngon lành. |
| b37 | 04:11.4–04:16.9 (5.4s) | L390 | Chiếc lưỡi dài màu xanh đen chứa đầy sắc tố melanin giúp bảo vệ mô lưỡi không bị cháy nắng khi vươn lên đón lá cây giữa trời |  | Cận cảnh chiếc lưỡi dài dẻo dai của hươu cao cổ cuốn chặt cành lá keo mà không hề bị gai nhọn đâm thủng; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b38 | 04:16.9–04:25.0 (8.1s) | L391 | nắng gắt! Bốn giờ sáng! Chỉ còn một tiếng nữa là đến giờ giao ban bình minh! Chúng ta chuyển ngay sang Khoa Da Liễu để kiểm tra vết thương của chú nhím béo tròn nào! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án cất chiếc ống nghe cao áp, cùng y tá rảo bước sang phòng khám da liễu bên cạnh. |

### scene11 · KHÁNG SINH TỰ NHIÊN TRÊN GAI · 246.3s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.3 (8.3s) | L392 | Bệnh nhân số 8, mời bước vào phòng khám Khoa Da Liễu và Dị Hóa Sinh! Chú Nhím Lông Nhọn béo tròn đang chầm chậm bước vào với mùi tinh dầu thông ngào ngạt! |  | chú Nhím Lông Nhọn Bắc Mỹ hoạt hình béo tròn xù xì, toàn thân phủ kín ba mươi ngàn chiếc gai nhọn trắng đen, đang ôm chặt một thân cây gỗ gặm vỏ thuốc, người tỏa mùi tinh dầu thơm nhẹ lặc lè bước vào phòng khám da liễu có kệ tủ chứa đầy các lọ cồn sát trùng và ống nghiệm hóa học, ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đang cầm một chiếc kính lúp soi nổi. |
| b02 | 00:08.3–00:14.9 (6.6s) | L393 | Tôi nhìn chú nhím đang ngơ ngác ngồi giữa phòng khám mà vừa thương vừa buồn cười trước sự vụng về của loài động vật này. |  | chú Nhím Lông Nhọn Bắc Mỹ hoạt hình béo tròn xù xì, toàn thân phủ kín ba mươi ngàn chiếc gai nhọn trắng đen, đang ôm chặt một thân cây gỗ gặm vỏ thuốc, người tỏa mùi tinh dầu thơm nhẹ ngồi bệt xuống đất, ngửa mặt lên nhìn trần nhà rồi gãi đầu bằng chiếc chân sau ngắn cũn cỡn; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b03 | 00:14.9–00:20.5 (5.6s) | L394 | Các đồng nghiệp có biết một nghịch lý trớ trêu nhất trong đời sống của loài nhím lông nhọn Bắc Mỹ là gì không? |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười đặt câu hỏi, đưa tay chỉ vào bộ lông gai dựng đứng lởm chởm trên lưng bệnh nhân. |
| b04 | 00:20.5–00:30.4 (9.9s) | L395 | Trong khi cả khu rừng và cả phòng cấp cứu ai cũng khiếp sợ 30.000 chiếc gai sắc nhọn trên lưng nó, thì bản thân con nhím lại là kẻ ngã cây nhiều nhất trong vương quốc động vật! |  | Cảnh một chú nhím đang bám vào cành cây thông cao mười mét gặm vỏ cây, bỗng nhiên cành cây gãy đánh rắc một cái; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b05 | 00:30.4–00:37.1 (6.7s) | L396 | Nhím lông nhọn Bắc Mỹ là một loài gặm nhấm rất thích ăn vỏ cây thông, vỏ cây bạch dương và chồi non ngọt ngào trên các ngọn cây cao. |  | Chú nhím dùng các móng vuốt cong khỏe khoắn bám vào thân cây thông phủ đầy tuyết trắng giữa mùa đông; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b06 | 00:37.1–00:43.3 (6.2s) | L397 | Thế nhưng thân hình nó thì béo múp míp, 4 chân ngắn ngủn và không hề có đuôi cuốn linh hoạt như loài khỉ hay sóc! |  | Cận cảnh bốn chiếc chân ngắn và chiếc bụng tròn xoe của chú nhím lắc lư chênh vênh trên cành cây khẳng khiu; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b07 | 00:43.3–00:52.0 (8.7s) | L398 | Khi mải mê vươn người ra những cành cây nhỏ ngoài rìa tán lá để gặm chồi non, những cú trượt chân tai hại thường xuyên khiến con nhím rơi tự do từ độ cao 10 m xuống |  | Chú nhím rơi từ trên cành cây cao xuống đất rậm rạp bụi cây gai, lăn lông lốc mấy vòng dưới thảm cỏ rừng; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b08 | 00:52.0–00:57.3 (5.3s) | L399 | đất! Cú va chạm mạnh vào đá sỏi hay rễ cây làm gãy vụn hàng chục sợi gai bảo vệ quanh sườn con vật! |  | Hình ảnh những đoạn gai nhọn bị gãy đôi cắm lộn xộn quanh vùng hông của con nhím sau cú ngã đau đớn; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b09 | 00:57.3–01:01.8 (4.5s) | L400 | Và khi rơi xuống mặt đất cứng ngắc từ độ cao của một tòa nhà 3 tầng, điều không thể tránh khỏi |  | Hình ảnh mô phỏng một vài chiếc gai nhọn cắm xuyên qua lớp da dày ở đùi và bụng của chính chú nhím sau cú ngã đau điếng; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b10 | 01:01.8–01:08.5 (6.7s) | L401 | là: Hàng chục chiếc gai sắc nhọn trên lưng nó sẽ bị gãy vụn và cắm phập ngược vào chính các thớ cơ thịt ở đùi, bụng và chân của con nhím! |  | Các mảnh gai nhọn cắm sâu vào lớp da thịt của chú nhím sau cú va đập mạnh với mặt đất; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b11 | 01:08.5–01:15.2 (6.7s) | L402 | Các bạn hãy nhớ lại xem: những chiếc gai này chứa hàng trăm vi ngạnh ngược siêu nhỏ, găm chặt vào thớ thịt và cực kỳ khó rút ra ngoài! |  | Kính hiển vi quang học phóng đại vi ngạnh ngược của gai nhím đang găm chặt vào mô cơ liên kết; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b12 | 01:15.2–01:21.9 (6.7s) | L403 | Nếu là một con thú săn mồi bị dính gai nhím, vết thương sẽ nhanh chóng bị nhiễm trùng, mưng mủ hoại tử và thậm chí dẫn tới cái chết đau đớn. |  | Hình ảnh vết thương nhiễm trùng mưng mủ trên mõm một chú chó sói sau khi bị nhím quẫy đuôi trúng; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b13 | 01:21.9–01:29.1 (7.2s) | L404 | Vậy tại sao với hàng ngàn chiếc gai tự đâm vào thịt mình sau mỗi cú ngã cây như vậy, loài nhím lại không bao giờ bị nhiễm trùng máu hay chết vì hoại tử? |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án dùng kẹp y tế gắp một sợi lông gai nhím đưa vào ống nghiệm chứa dung dịch hóa chất trong suốt để làm phản ứng phân tích. |
| b14 | 01:29.1–01:34.8 (5.7s) | L405 | Thậm chí các vết đâm tự thân này còn lành lặn thần tốc chỉ sau vài ngày mà không để lại bất kỳ di chứng áp xe nào! |  | Vết đâm trên đùi chú nhím khô miệng nhanh chóng, các tế bào biểu bì mới mọc lên bao bọc an toàn; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b15 | 01:34.8–01:40.6 (5.8s) | L406 | Công trình nghiên cứu kinh điển của giáo sư Uldis Roze về loài nhím Bắc Mỹ đã làm sáng tỏ một cơ chế dược lý phi thường: |  | Bảng phân tích sắc ký chất béo hiển thị các đỉnh phổ phân tử của các axit béo tự do mạch tự nhiên; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b16 | 01:40.6–01:47.5 (6.9s) | L407 | Toàn bộ bề mặt ngoài của 30.000 chiếc lông gai nhím được bao phủ bởi một lớp màng chất béo mỏng chứa đầy các axit béo tự do có tính kháng sinh cực mạnh! |  | Kính hiển vi quang học soi lớp màng mỡ mỏng màu vàng óng ánh bao bọc quanh thân sợi gai nhím; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b17 | 01:47.5–01:53.2 (5.7s) | L408 | Các axit béo này bao gồm axit butyric, axit hexanoic và nhiều hợp chất lipid tự nhiên có khả năng diệt khuẩn phổ |  | Mô hình phân tử hóa học của các chuỗi axit béo tự do phát sáng lấp lánh bao bọc quanh cấu trúc chitin của sợi lông; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b18 | 01:53.2–02:01.3 (8.1s) | L409 | rộng. Chúng có khả năng tiêu diệt và ức chế sự phát triển của hầu hết các loài vi khuẩn Gram dương, đặc biệt là vi khuẩn tụ cầu vàng Staphylococcus aureus cực kỳ nguy hiểm! |  | Đồ họa vi sinh vật hiển thị các tế bào vi khuẩn tụ cầu vàng bị lớp axit béo trên gai nhím phá hủy màng tế bào vỡ vụn; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b19 | 02:01.3–02:07.4 (6.1s) | L410 | Đây thực chất là một lớp kem bôi kháng sinh tự nhiên mà tạo hóa đã hào phóng bôi sẵn lên từng chiếc mũi kim tiêm trên lưng con nhím! |  | Hình ảnh minh họa sợi gai nhím được nhúng vào một lớp sáp kháng khuẩn tự nhiên trước khi mọc ra ngoài lớp da; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b20 | 02:07.4–02:13.3 (5.9s) | L411 | Mỗi khi con nhím trượt chân ngã cây và tự đâm trúng gai của chính mình, lớp kháng sinh này sẽ lập tức khử trùng vết thương ngay tại |  | Vết đâm trên da nhím không hề bị sưng tấy mưng mủ, các tế bào biểu bì mau chóng phục hồi và lành lặn thần tốc; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b21 | 02:13.3–02:19.9 (6.6s) | L412 | chỗ! Nó hoạt động như một hệ thống an toàn tự động, đảm bảo rằng nếu vũ khí tự vệ phản chủ thì chủ nhân của nó vẫn hoàn toàn bình an vô sự! |  | chú Nhím Lông Nhọn Bắc Mỹ hoạt hình béo tròn xù xì, toàn thân phủ kín ba mươi ngàn chiếc gai nhọn trắng đen, đang ôm chặt một thân cây gỗ gặm vỏ thuốc, người tỏa mùi tinh dầu thơm nhẹ thản nhiên rũ lông một cái đánh xào xạc, không hề tỏ ra đau đớn hay khó chịu trước vết gai cũ; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b22 | 02:19.9–02:25.1 (5.2s) | L413 | Lớp sáp mỡ này được tiết ra liên tục từ các tuyến bã nhờn chuyên biệt nằm ngay cạnh nang lông dưới lớp da dày! |  | Sơ đồ giải phẫu tuyến bã nhờn nang lông nhím tiết dịch mỡ kháng sinh bao bọc thân sợi gai; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b23 | 02:25.1–02:32.8 (7.7s) | L414 | Chưa hết đâu nhé! Lớp mỡ kháng sinh này còn phát tán một mùi hương hăng nồng đặc trưng vào không khí mỗi khi nhím dựng đứng các sợi gai lên cảnh cáo kẻ thù! |  | Luồng phân tử mùi hương màu tím nhạt tỏa ra từ các sợi gai dựng đứng cảnh báo các loài thú ăn thịt xung quanh; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b24 | 02:32.8–02:42.9 (10.1s) | L415 | Đó là lời nhắn nhủ rõ ràng của tự nhiên gửi tới các loài săn mồi: Tránh xa ra! Ở đây có 30.000 mũi kim tiêm tẩm thuốc tê và kháng sinh sẵn sàng phục vụ các bạn đấy! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án nháy mắt mỉm cười nhìn chú chú Nhím Lông Nhọn Bắc Mỹ hoạt hình béo tròn xù xì, toàn thân phủ kín ba mươi ngàn chiếc gai nhọn trắng đen, đang ôm chặt một thân cây gỗ gặm vỏ thuốc, người tỏa mùi tinh dầu thơm nhẹ đang tò mò ngửi chiếc ống nghe trên bàn khám. |
| b25 | 02:42.9–02:48.8 (5.9s) | L416 | Tôi đã lấy mẫu chất béo trên lưng bệnh nhân để nuôi cấy vi sinh vật trong đĩa thạch thí nghiệm suốt 24 giờ qua. |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án giơ chiếc đĩa petri thí nghiệm trong suốt lên dưới ánh đèn soi kiểm tra độ tinh sạch của mẫu cấy. |
| b26 | 02:48.8–02:56.1 (7.3s) | L417 | Và kết quả thu được hoàn toàn vô trùng 100%! Không có một khóm vi khuẩn gây hại nào có thể sống sót trên bộ lông gai này! |  | Đĩa thạch trong veo không hề có một vết vẩn đục hay khuẩn lạc nào phát triển chứng minh hoạt tính kháng sinh tuyệt hảo; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b27 | 02:56.1–03:03.8 (7.7s) | L418 | Vòng vô khuẩn xung quanh mẫu gai nhím trên đĩa thạch thậm chí còn rộng hơn cả vòng ức chế của thuốc kháng sinh penicillin thông thường! |  | Thước đo y tế đo đường kính vòng vô khuẩn trong suốt quanh sợi gai nhím vượt trội so với đĩa giấy thấm penicillin; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b28 | 03:03.8–03:09.7 (6.0s) | L419 | Các nhà nghiên cứu còn thử nghiệm với các chủng vi nấm gây bệnh ngoài da cứng đầu nhất như nấm mốc sợi và nấm men candida. |  | Đĩa thạch thí nghiệm vi nấm bị màng axit béo tự nhiên từ gai nhím tiêu diệt hoàn toàn không thể phát triển; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b29 | 03:09.7–03:16.6 (6.8s) | L420 | Và kết quả thật đáng kinh ngạc: Lớp axit béo tự nhiên trên gai nhím ức chế tới 90 9 phần trăm sự phát triển của các bào tử nấm mốc! |  | Biểu đồ tỷ lệ ức chế vi nấm chạm mốc chín mươi chín phần trăm phát sáng màu xanh lá cây hy vọng; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b30 | 03:16.6–03:23.6 (7.0s) | L421 | Điều này lý giải tại sao dù sống ở những vùng đầm lầy ẩm ướt hay rừng rậm nhiệt đới ẩm thấp, da của loài nhím không bao giờ bị viêm da hay nấm ngứa! |  | Chú nhím lông nhọn thong dong đi qua thảm rêu ẩm ướt đầy nấm mốc trong rừng già mà không hề bị tổn thương da; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b31 | 03:23.6–03:29.1 (5.5s) | L422 | Nó sở hữu một hệ sinh thái da hoàn toàn tự cân bằng và tự kháng khuẩn độc nhất vô nhị trong lớp động vật có vú! |  | Hình ảnh mô phỏng cấu trúc vi sinh vật có lợi trên bề mặt da nhím bảo vệ nang lông khỏi mọi tác nhân gây hại; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b32 | 03:29.1–03:34.7 (5.6s) | L423 | Lớp sáp kháng sinh này thậm chí còn không bị rửa trôi bởi nước mưa hay băng tuyết suốt cả mùa đông lạnh giá! |  | Giọt nước mưa trượt tròn lăn khỏi bề mặt sợi gai nhím mà không làm phai mờ lớp màng kháng sinh bao phủ; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b33 | 03:34.7–03:39.8 (5.2s) | L424 | Thật là một phòng thí nghiệm dược phẩm di động hoàn mỹ được tích hợp ngay trên lưng một chú gặm nhấm béo tròn! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án gật gù khen ngợi, cất chiếc đĩa thạch vào tủ ủ ấm vi sinh. |
| b34 | 03:39.8–03:45.8 (5.9s) | L425 | Chẩn đoán Khoa Da Liễu của Phòng Cấp Cứu Tạo Hóa: Bệnh nhân sở hữu nhà máy sản xuất thuốc mỡ kháng sinh xịn nhất thế giới động |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án gật đầu hài lòng, xoa nhẹ cái mũi ươn ướt của chú nhím và ký tên vào hồ sơ bệnh án số tám. |
| b35 | 03:45.8–03:53.6 (7.8s) | L426 | vật! Cho phép xuất viện! Nhưng dặn bệnh nhân lần sau leo trèo hái quả thì nhớ thắt dây an toàn cẩn thận nhé, ngã hoài làm bệnh viện tốn bông băng lắm đấy! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án trao chiếc túi đựng vài củ cà rốt tươi ngon cho chú nhím làm quà xuất viện, chú nhím ôm chặt củ cà rốt mừng rỡ lon ton bước ra ngoài. |
| b36 | 03:53.6–03:58.9 (5.4s) | L427 | Anh bạn nhím hãy nhớ rằng kháng sinh dù xịn đến mấy cũng không thể chữa lành bệnh lười đeo dây an toàn đâu nhé! |  | Chú chú Nhím Lông Nhọn Bắc Mỹ hoạt hình béo tròn xù xì, toàn thân phủ kín ba mươi ngàn chiếc gai nhọn trắng đen, đang ôm chặt một thân cây gỗ gặm vỏ thuốc, người tỏa mùi tinh dầu thơm nhẹ ôm chặt củ cà rốt gật gù đắc ý, lon ton đi theo lối hành lang riêng biệt; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b37 | 03:58.9–04:06.3 (7.3s) | L428 | Giờ thì chuyển ngay sang phòng khám cuối cùng: Khoa Tâm Thần và Rối Loạn Hành Vi! Bệnh nhân số 9 đang đứng như tượng đá ngoài hành lang! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án cởi chiếc áo găng tay da liễu, bước thẳng về phía cửa phòng khám tâm thần nơi chú cò mỏ giày đang đợi. |

### scene12 · TƯỢNG ĐÁ BIẾT XẢ SÚNG · 249.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:05.5 (5.5s) | L429 | Bốn giờ 30 phút sáng. Căn phòng khám Khoa Tâm Thần và Rối Loạn Hành Vi chìm trong bầu không khí yên ắng đến rợn |  | Căn phòng khám có ánh sáng mờ ảo, chú Cò Mỏ Giày hoạt hình lông xám tro, dáng đứng sừng sững bất động như tượng đá, chiếc mỏ khổng lồ màu vàng xám phình to hình chiếc guốc gỗ, ánh mắt lạnh như tiền đứng canh cửa phòng cấp cứu đứng sừng sững giữa phòng như một bức tượng điêu khắc bằng đá hoa cương xám, ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án ngồi đối diện trên chiếc ghế |
| b02 | 00:05.5–00:11.9 (6.3s) | L430 | người. Bên ngoài cửa sổ, những cơn gió lạnh rít nhẹ qua khe kính, chỉ có tiếng kim đồng hồ tíc tắc gõ nhịp chậm rãi giữa căn phòng tĩnh |  | Chiếc đồng hồ treo tường tròn xoe bằng đồng thau nhảy từng giây một, bóng kim đồng hồ in dài trên bức tường xám; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b03 | 00:11.9–00:18.9 (7.0s) | L431 | mịch. Bệnh nhân số 9: Cò Mỏ Giày, sinh vật thời tiền sử còn sót lại giữa những đầm lầy hoang sơ miền Trung châu Phi xa xôi. |  | Toàn cảnh chú chú Cò Mỏ Giày hoạt hình lông xám tro, dáng đứng sừng sững bất động như tượng đá, chiếc mỏ khổng lồ màu vàng xám phình to hình chiếc guốc gỗ, ánh mắt lạnh như tiền đứng canh cửa phòng cấp cứu cao một mét hai, sải cánh dài hơn hai mét rưỡi, bộ lông màu xám tro cổ kính như một con khủng long bay bước ra từ kỷ Phấn Trắng; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b04 | 00:18.9–00:23.9 (5.0s) | L432 | Từ lúc nhập viện lúc 12 giờ đêm cho tới tận thời điểm này, bệnh nhân này không hề nhấc chân lên một lần |  | Cận cảnh đôi chân dài khẳng khiu với những chiếc ngón chân xòe rộng bám chặt xuống sàn gạch men không hề lay chuyển một mi-li-mét; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b05 | 00:23.9–00:31.2 (7.3s) | L433 | nào! Hai mắt màu vàng nhạt nhìn trừng trừng vào một điểm vô định trên tường, mi mắt hoàn toàn không chớp, nhịp thở chậm đến mức mắt thường không thể nhận |  | Cận cảnh đôi mắt lạnh lùng không chút cảm xúc của cò mỏ giày, chiếc mỏ guốc khổng lồ dài hai mươi tư xăng-ti-mét chúc xuống đầy uy nghi; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b06 | 00:31.2–00:39.6 (8.4s) | L434 | biết được! Chiếc mỏ guốc khổng lồ chúc xuống góc 45 độ, toát ra một vẻ mặt nghiêm nghị và đăm chiêu như một triết gia cổ đại đang trầm tư mặc tưởng. |  | Gương mặt vuông vức bằng chất sừng cứng ngắc của chú cò mỏ giày, đầu có một túm lông tơ dựng ngược ngộ nghĩnh; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b07 | 00:39.6–00:44.0 (4.4s) | L435 | Bác sĩ trưởng khoa ơi em mang hồ sơ vào mà 2 hàm răng em va vào nhau lập cập! |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng rón rén bước vào phòng, tay ôm tập hồ sơ nép sát vào lưng bác sĩ thì thầm lo sợ. |
| b08 | 00:44.0–00:49.7 (5.7s) | L436 | Có phải con chim khổng lồ này bị trầm cảm phân liệt giai đoạn cuối hay bị đông cứng cơ thể kiểu mèo liệt cứng không bác sĩ? |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng ngước nhìn đôi mắt màu vàng nhạt bất động của con chim, hai tay xoa xoa bắp tay vì ớn lạnh; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b09 | 00:49.7–00:56.1 (6.4s) | L437 | Nó cứ nhìn em trừng trừng từ nửa đêm đến giờ, em cảm giác như linh hồn mình sắp bị chiếc mỏ kia nuốt chửng mất rồi bác sĩ ơi! |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng run rẩy giơ chiếc đèn soi phản xạ đồng tử ra trước mắt con chim nhưng đồng tử của nó không hề co giãn; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b10 | 00:56.1–01:01.3 (5.2s) | L438 | Và chân cẳng của nó trắng phau như quét vôi thế kia có phải bị nấm da hoại tử giai đoạn nặng không bác sĩ ơi? |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng chỉ ngón tay run rẩy vào đôi chân dài dính đầy vệt trắng kỳ lạ của chú chim; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b11 | 01:01.3–01:05.0 (3.7s) | L439 | Không hề có chứng liệt cứng hay trầm cảm nào ở đây cả cô y tá thân mến! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đứng dậy bước chậm rãi quanh chú chim, quan sát kỹ từng đường nét giải phẫu trên chiếc đầu to lớn khác thường. |
| b12 | 01:05.0–01:10.0 (5.0s) | L440 | Đây chính là trạng thái thiền định săn mồi đỉnh cao của kẻ phục kích kiên nhẫn nhất thế giới tự nhiên hoang dã! |  | Sơ đồ thần kinh trung ương của cò mỏ giày hiển thị các vùng kiểm soát phản xạ ức chế vận động hoạt động ở mức tối ưu; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b13 | 01:10.0–01:14.9 (4.9s) | L441 | Vệt trắng trên chân nó thực chất là thói quen xả nước tiểu làm mát chân độc đáo mang tên urohidrosis! |  | Đồ họa sinh lý học hiển thị nước bay hơi từ bề mặt chân chim giúp hạ nhiệt độ dòng nước màu tuần hoàn khi trời nóng bức; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b14 | 01:14.9–01:20.8 (5.9s) | L442 | Nước bay hơi sẽ làm mát các mạch máu ở chân, giúp nó duy trì thân nhiệt ổn định giữa những đầm lầy châu Phi nóng tới 4 mươi độ C! |  | Chú cò mỏ giày đứng giữa đầm lầy nắng gắt, làn gió thổi qua làm mát đôi chân dài khẳng khiu; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b15 | 01:20.8–01:24.9 (4.1s) | L443 | Và khi tôi vừa bước tới trước mặt nó cách 0,5 m... Cạch! Cạch! Cạch! Tách tách tách |  | Đột nhiên chú Cò Mỏ Giày hoạt hình lông xám tro, dáng đứng sừng sững bất động như tượng đá, chiếc mỏ khổng lồ màu vàng xám phình to hình chiếc guốc gỗ, ánh mắt lạnh như tiền đứng canh cửa phòng cấp cứu ngửa cổ lên trời rồi đập liên hồi hai hàm mỏ vào nhau với tốc độ chóng mặt, tạo nên một chuỗi âm thanh đanh thép rền vang khắp phòng khám! |
| b16 | 01:24.9–01:31.5 (6.6s) | L444 | tách tách! Tiếng va đập của 2 hàm mỏ guốc khổng lồ vang lên rầm rầm như một khẩu súng máy liên thanh đang xả đạn liên hồi giữa chiến hào! |  | Sóng âm thanh cực mạnh phát ra từ chiếc mỏ làm rung chuyển cửa kính phòng khám, các y tá giật bắn người bịt chặt hai tai; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b17 | 01:31.5–01:37.7 (6.2s) | L445 | Chuỗi âm thanh kim loại đanh thép xé toạc bầu không khí yên tĩnh, làm rung rinh cả những chiếc chai lọ thủy tinh trên giá thuốc! |  | Các dụng cụ y tế trên khay inox nảy nhẹ lên theo từng nhịp gõ mỏ vang dội của chú chim; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b18 | 01:37.7–01:42.0 (4.3s) | L446 | Đó chính là nghi thức gõ mỏ bill-clattering độc nhất vô nhị của loài cò mỏ giày! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án bình tĩnh giơ chiếc máy đo độ ồn decibel lên đo cường độ âm thanh của tràng gõ mỏ vừa dứt. |
| b19 | 01:42.0–01:45.8 (3.8s) | L447 | Nghiên cứu của tiến sĩ Tomita công bố trên Tạp Chí Tập Tính Học Động Vật đã đo |  | Máy đo âm thanh kỹ thuật số hiển thị các đỉnh sóng âm thanh hình gai nhọn chạm ngưỡng cảnh báo độ ồn cực đại; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b20 | 01:45.8–01:53.2 (7.4s) | L448 | được: Cường độ âm thanh của tràng gõ mỏ này có thể đạt ngưỡng lên tới 115 dB! Ngang ngửa với tiếng còi xe cứu thương hụ còi ở cự ly gần! |  | bảng kẹp bệnh án y khoa khổng lồ (clipboard) kẹp trên giá đỡ kim loại, hiển thị 10 hồ sơ bệnh án hoạt hình với nhãn đơn thuốc phát sáng và sóng nhịp tim ECG màu đỏ nhấp nháy (không có chữ, không có số) bật sáng con số 115 dB cùng biểu tượng khẩu súng máy phát ra sóng âm thanh nhấp nháy đỏ rực; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b21 | 01:53.2–02:00.3 (7.1s) | L449 | Tiếng gõ mỏ đanh thép này có thể truyền xa hàng cây số qua những thảm cói đầm lầy rậm rạp, dùng để chào hỏi bạn tình và xua đuổi các đối thủ xâm phạm |  | Cảnh đầm lầy châu Phi mênh mông lúc rạng đông, tiếng gõ mỏ vang rền làm bầy linh dương và chim nước bay toán loạn; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b22 | 02:00.3–02:05.7 (5.4s) | L450 | lãnh thổ! Chiếc mỏ khổng lồ dài tới 24 cm của nó kết thúc bằng một chiếc móc câu sắc lẹm như mũi |  | Hình ảnh phóng to chóp mỏ của cò mỏ giày với chiếc móc cong nhọn hoắt có thể chém đứt đôi một con cá phổi dài một mét; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b23 | 02:05.7–02:13.0 (7.3s) | L451 | mác thép! Khi kẹp chặt lại, lực ép cơ hàm của nó thừa sức nghiền nát lớp vảy giáp cứng như đá của loài cá phổi châu Phi và rùa đầm lầy trong nháy mắt! |  | Bản vẽ cơ hàm của cò mỏ giày với các bó cơ nhai khổng lồ gắn vào gờ xương hộp sọ tạo lực kẹp nghiền nát con mồi; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b24 | 02:13.0–02:20.7 (7.7s) | L452 | Đôi mắt của nó có màng chớp trong suốt nhắm lại theo chiều ngang trong đúng 1/1000 giây khi tấn công con mồi dưới bùn lầy để bảo vệ giác mạc! |  | Cận cảnh đôi mắt chim với màng chớp trong suốt đóng mở thần tốc bảo vệ mắt khỏi bùn đất và răng cá sắc nhọn; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b25 | 02:20.7–02:29.0 (8.3s) | L453 | Bàn chân khổng lồ của nó có sải ngón dài tới 30 cm, phân tán áp lực giúp con chim bước đi thanh thoát trên thảm bèo nổi mà không bị chìm! |  | Cận cảnh bàn chân bốn ngón xòe rộng của cò mỏ giày đạp vững chãi trên lớp thảm thực vật nổi giữa đầm lầy; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b26 | 02:29.0–02:36.5 (7.5s) | L454 | Nhưng phía sau sự kiên nhẫn và uy lực đáng sợ đó là một hiện tượng sinh học khốc liệt làm xót xa lòng người: Hiện tượng sát hại con thứ Cainism! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án trầm giọng, ánh mắt thoáng buồn khi lật giở trang tài liệu sinh thái học của loài chim này. |
| b27 | 02:36.5–02:40.8 (4.3s) | L455 | Nghiên cứu thực địa của Mullers và Amar trên Tạp Chí Điểu Học The Ostrich đã ghi nhận: |  | Hình ảnh tư liệu trắng đen về chiếc tổ chim khổng lồ nằm cô độc giữa đầm lầy Bangweulu hoang vắng; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b28 | 02:40.8–02:47.6 (6.8s) | L456 | Cò mỏ giày mẹ thường đẻ 2 quả trứng trong mỗi mùa sinh sản để dự phòng trường hợp quả trứng đầu tiên bị hỏng hoặc con non bị chết yểu. |  | Chiếc tổ chim khổng lồ bằng cỏ khô nổi giữa đầm lầy, bên trong có hai chú chim non lông tơ màu xám vừa nở; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b29 | 02:47.6–02:53.8 (6.2s) | L457 | Thế nhưng nguồn thức ăn ở các đầm lầy nhiệt đới luôn biến động vô cùng khan hiếm, chim bố mẹ chỉ đủ sức kiếm mồi nuôi sống một đứa con duy |  | Chim bố mẹ bay về tổ ngậm một con cá nhỏ, hai chú chim non há mỏ tranh giành thức ăn quyết liệt; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b30 | 02:53.8–03:01.8 (8.0s) | L458 | nhất. Con non đầu lòng to lớn hơn sẽ liên tục dùng chiếc mỏ nhọn mổ và xua đuổi đứa em nhỏ yếu ớt ra khỏi tổ cho tới khi con thứ chết đói trong sự bất lực của chim mẹ! |  | Con non đầu lòng to lớn hơn liên tục mổ và xua đuổi đứa em nhỏ yếu ớt ra khỏi tổ cho tới khi con thứ chết đói trong sự bất lực của chim mẹ; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b31 | 03:01.8–03:10.0 (8.2s) | L459 | Đó là sự tàn nhẫn đến lạnh lùng của quy luật chọn lọc tự nhiên: thà bảo toàn một cá thể khỏe mạnh nhất còn hơn để cả 2 cùng chết đói giữa vùng đầm lầy khắc nghiệt! |  | Cảnh chim non đầu lòng giương đôi cánh xám đứng kiêu hãnh trên tổ dưới ánh hoàng hôn đầm lầy; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b32 | 03:10.0–03:15.1 (5.0s) | L460 | Mặc dù sở hữu sải cánh rộng tới 2,5 m, nhưng loài cò mỏ giày rất hiếm khi bay lượn trên bầu trời |  | Chú cò mỏ giày dang rộng đôi cánh dài hai mét rưỡi bay là là trên mặt nước đầm lầy phủ đầy hoa súng tím; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b33 | 03:15.1–03:23.1 (8.1s) | L461 | cao. Do trọng lượng cơ thể nặng nề từ 4 đến 7 cân, mỗi lần cất cánh nó phải chạy đà vài bước nặng nhọc trên thảm bèo nổi tương tự một chiếc máy bay ném bom hạng nặng! |  | Con chim sải chân chạy đà trên thảm cỏ nước, đập cánh mạnh mẽ tạo nên những luồng gió rẽ sóng nước xung quanh; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b34 | 03:23.1–03:28.8 (5.6s) | L462 | Nó chỉ bay những chặng ngắn từ 100 đến 500 mét giữa các vũng nước đầm lầy để tìm kiếm những đàn cá phổi ngon |  | Cảnh cò mỏ giày bay là là trên những ngọn cây cói lau sậy, đôi cánh đập chậm rãi nhưng đầy uy lực; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b35 | 03:28.8–03:38.2 (9.5s) | L463 | lành! Mỗi khi thời tiết quá oi bức, ngoài thói quen xả nước làm mát chân, nó còn ngậm từng ngụm nước lớn trong chiếc mỏ guốc rồi tưới ướt đẫm các quả trứng trong tổ để duy trì độ ẩm tối ưu! |  | Chú cò mỏ giày dùng chiếc mỏ guốc múc nước suối tưới nhẹ nhàng lên chiếc tổ có hai quả trứng trắng ngà giữa đầm lầy; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b36 | 03:38.2–03:46.2 (8.0s) | L464 | Bệnh nhân Cò Mỏ Giày không hề có bất kỳ rối loạn tâm thần nào! Mọi hành vi bất động và tiếng gõ mỏ súng máy đều là bản năng sinh tồn hoàn mỹ của kẻ thống trị đầm lầy! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án khẽ cúi đầu chào theo nghi thức cúi chào bill-bobbing của loài chim này, chú chú Cò Mỏ Giày hoạt hình lông xám tro, dáng đứng sừng sững bất động như tượng đá, chiếc mỏ khổng lồ màu vàng xám phình to hình chiếc guốc gỗ, ánh mắt lạnh như tiền đứng canh cửa phòng cấp cứu cũng từ từ gật đầu đáp lễ một cách lịch thiệp lạ kỳ. |
| b37 | 03:46.2–03:52.3 (6.1s) | L465 | Chẩn đoán của Phòng Cấp Cứu Tạo Hóa: Tinh thần thép, sự kiên nhẫn vô địch và phản xạ săn mồi đạt cấp độ sát thủ hoàn hảo! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án ký tên đóng dấu xuất viện vào hồ sơ bệnh án số chín, khẽ mỉm cười nhìn chú chim cúi đầu chào từ biệt. |
| b38 | 03:52.3–03:57.2 (5.0s) | L466 | Toàn bộ 10 ca bệnh nhân dị thường của ca trực đêm đã được khám nghiệm toàn diện và chuẩn xác 100%! |  | Mười tập hồ sơ bệnh án dày cộp được xếp ngay ngắn trong chiếc cặp da màu nâu của Bác Sĩ Trưởng Khoa; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b39 | 03:57.2–04:02.9 (5.7s) | L467 | Chúng ta đã vượt qua ca trực đêm cam go nhất mà không hề có bất kỳ ca tử vong hay biến chứng y khoa nào xảy ra! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án siết chặt khóa chiếc cặp da y tế, ánh mắt rạng ngời niềm hãnh diện của người thầy thuốc; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b40 | 04:02.9–04:09.4 (6.5s) | L468 | Đồng hồ điểm đúng 5 giờ sáng! Đã đến lúc toàn thể y bác sĩ tập hợp tại hội trường lớn cho buổi giao ban kịch tính nhất lịch sử! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án tháo ống nghe, cùng y tá sải bước về phía hội trường trung tâm của bệnh viện. |

### scene13 · ĐÁNH GIÁ MƯỜI QUÁI KIỆT · 251.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:04.7 (4.7s) | L469 | Năm giờ sáng. Căn phòng họp giao ban lớn của bệnh viện rực sáng ánh đèn chùm pha lê cổ kính. |  | Toàn cảnh phòng họp giao ban lớn của bệnh viện với bàn hội nghị bằng gỗ gụ hình bầu dục dài mười mét, các giáo sư và bác sĩ nội trú ngồi kín các dãy ghế; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b02 | 00:04.7–00:10.8 (6.1s) | L470 | Toàn thể hội đồng y khoa và kíp trực đêm tề tựu đông đủ quanh chiếc bàn dài bằng gỗ gụ, trên tay mỗi người là một tách cà phê nóng hổi. |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đứng ở đầu bàn hội nghị trong chiếc áo blouse trắng tinh tươm, hai tay chống lên mặt bàn gỗ, ánh mắt rạng ngời niềm tự hào nghề nghiệp. |
| b03 | 00:10.8–00:17.3 (6.5s) | L471 | Tôi trịnh trọng mở chiếc cặp da màu nâu, xếp 10 tập hồ sơ bệnh án đã được ký tên và đóng dấu đỏ chót ngay ngắn lên mặt bàn trước mặt hội đồng. |  | Mười tập hồ sơ bệnh án bìa cứng dập nổi dấu mộc đỏ ĐÃ XỬ LÝ XUẤT SẮC xếp thẳng hàng trên bàn hội nghị; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b04 | 00:17.3–00:24.0 (6.7s) | L472 | Thưa toàn thể các đồng nghiệp và các bác sĩ nội trú thân mến: Chúng ta vừa trải qua ca trực đêm điên rồ và kỳ diệu nhất trong toàn bộ lịch sử y học! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án cất giọng vang ấm đĩnh đạc, nhìn quanh phòng họp nơi các bác sĩ trẻ đang lắng nghe như nuốt từng lời. |
| b05 | 00:24.0–00:32.5 (8.5s) | L473 | Mười bệnh nhân, 10 căn bệnh tưởng chừng như vô phương cứu chữa hay dị tật quái gở, thực chất lại là 10 phát minh cơ thể học phi thường nhất của tạo hóa! |  | Màn hình chiếu máy chiếu rọi sáng hình ảnh mười loài vật kỳ dị với các đường nét giải phẫu vàng rực rỡ; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b06 | 00:32.5–00:36.3 (3.8s) | L474 | Hãy cùng tôi điểm lại bản tóm tắt lâm sàng 10 ca bệnh độc nhất vô nhị đêm nay: |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án bật máy chiếu slide cổ điển, từng hình ảnh minh họa ngộ nghĩnh hiện lên trên tấm phông trắng lớn. |
| b07 | 00:36.3–00:43.5 (7.2s) | L475 | Anh chàng Khỉ Đột Lưng Bạc không hề bị viêm dạ dày ruột, mà mang trong bụng một nhà máy lên men vi sinh vật tạo ra 70% năng lượng cơ bắp! |  | Slide chiếu hình ảnh biếm họa chú khỉ đột cơ bắp lực lưỡng đang ôm cái bụng phình to đầy tự hào bên cạnh biểu đồ calo; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b08 | 00:43.5–00:50.1 (6.6s) | L476 | Chú Nhện Lặn Chuông tí hon không hề muốn tự tử, mà đã tự dệt nên chiếc bình dưỡng khí nano cho phép nó thở oxy dưới nước suốt 24 giờ! |  | Slide chiếu chú nhện lặn chuông bơi lội ung dung bên trong quả cầu khí bạc dưới đáy hồ; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b09 | 00:50.1–00:57.8 (7.7s) | L477 | Chú Cá Thòi Lòi không hề bị gãy xương chậu, mà dùng vây ngực làm chân đi bộ và ngậm nước trong mang để chinh phục đất cạn suốt 90% cuộc đời! |  | Slide chiếu chú cá thòi lòi giương đôi mắt kính tiềm vọng đứng chống vây hiên ngang trên rễ đước; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b10 | 00:57.8–01:05.3 (7.6s) | L478 | Cô Ong Bắp Cày Ngọc không hề dùng bùa ngải ma thuật, mà thực hiện ca phẫu thuật thần kinh chính xác tuyệt đối để điều khiển con gián to gấp 6 lần mình! |  | Slide chiếu cô ong ngọc bích lấp lánh dắt chú gián đi dạo như dắt cún con; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b11 | 01:05.3–01:12.0 (6.7s) | L479 | Chú Cá Mặt Trăng 2 tấn không hề bị liệt hàm méo miệng, mà sở hữu bộ não 4 g siêu tiết kiệm năng lượng và đẻ tới 300 triệu trứng mỗi mùa! |  | Slide chiếu cá mặt trăng tròn dẹt đang nằm phơi nắng trên mặt biển sưởi ấm thân nhiệt; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b12 | 01:12.0–01:18.8 (6.8s) | L480 | Chàng Vẹt Kakapo béo tròn không hề bị dị tật cánh cụt, mà đã hoàn thiện chiến lược sinh tồn đi bộ dưới mặt đất và tỏa mùi thơm thảo mộc mê đắm! |  | Slide chiếu chú vẹt kakapo lông xanh rêu đang lon ton đi bộ trên thảm rêu New Zealand; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b13 | 01:18.8–01:25.8 (7.0s) | L481 | Chú Lợn Hươu Babirusa không hề sở hữu vũ khí tự sát ngớ ngẩn, mà chiếc nanh cong 40 cm là tấm khiên hộ mệnh và chiếc vương miện kiêu hãnh của tình |  | Slide chiếu chú lợn babirusa đứng thẳng trên hai chân sau khoe cặp nanh uốn lượn trước ánh bình minh rừng nhiệt đới; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b14 | 01:25.8–01:33.6 (7.7s) | L482 | yêu! Quý cô Hươu Cao Cổ không hề bị cơn bão cao huyết áp ác tính, mà mức huyết áp 280 là điều kiện sống còn để nuôi dưỡng bộ não cách mặt đất 5 m! |  | Slide chiếu hệ thống bơm tăng áp thủy lực và mạng lưới mạch Rete mirabile dưới đáy sọ hươu cao cổ; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b15 | 01:33.6–01:40.3 (6.7s) | L483 | Chú Nhím Lông Nhọn không hề bị nhiễm trùng sau mỗi cú ngã cây, mà sở hữu lớp sáp kháng sinh tự nhiên diệt khuẩn tụ cầu vàng hoàn hảo nhất Trái Đất! |  | Slide chiếu sợi lông nhím bọc màng mỡ kháng sinh óng ánh vàng tiêu diệt vi khuẩn; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b16 | 01:40.3–01:48.5 (8.2s) | L484 | Và chú Cò Mỏ Giày không hề bị trầm cảm hay đông cứng tâm thần, mà trạng thái bất động là tuyệt đỉnh thiền định của sát thủ đầm lầy với tiếng gõ mỏ 115 dB! |  | Slide chiếu chú cò mỏ giày uy nghi với chiếc mỏ guốc khổng lồ ngửa cổ lên trời gõ mỏ súng máy; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b17 | 01:48.5–01:57.4 (8.9s) | L485 | Mỗi một nét giải phẫu kỳ dị của chúng đều là một giải pháp cơ sinh học thiên tài mà hàng trăm viện nghiên cứu công nghệ hiện đại nhất của loài người vẫn đang phải miệt mài học hỏi! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đập tay nhẹ lên bàn, ánh mắt bừng sáng trước vẻ đẹp trí tuệ vô tận của tự nhiên. |
| b18 | 01:57.4–02:06.5 (9.1s) | L486 | Từ vật liệu dệt tơ nhện siêu bền đến kim tiêm giảm đau mô phỏng vi ngạnh nhím, từ bộ đồ bay G-suit mô phỏng da hươu cao cổ đến thuốc tê thần kinh từ nọc ong ngọc! |  | Sơ đồ công nghệ phỏng sinh học hiển thị các phát minh y sinh học hiện đại được lấy cảm hứng từ cấu trúc cơ thể của mười sinh vật này; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b19 | 02:06.5–02:13.6 (7.1s) | L487 | Các kỹ sư hàng không vũ trụ hiện nay đang ứng dụng cơ chế van tĩnh mạch cổ của hươu cao cổ để thiết kế trang phục kháng áp cho phi hành gia bay vào vũ |  | Hình ảnh minh họa bộ đồ phi hành gia thế hệ mới lấy cảm hứng từ cấu trúc da và mạch nước màu hươu cao cổ; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b20 | 02:13.6–02:22.7 (9.1s) | L488 | trụ! Và các nhà khoa học vật liệu nano đang nghiên cứu cấu trúc sợi tơ không thấm nước của nhện lặn chuông để sản xuất các thiết bị lọc khí nhân tạo dưới đáy đại dương! |  | Mô hình 3D vật liệu sợi nano nhân tạo mô phỏng cấu trúc chuông lặn của nhện nước phát sáng lấp lánh; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b21 | 02:22.7–02:30.1 (7.4s) | L489 | Các chuyên gia dược phẩm đang tổng hợp hoạt chất kháng khuẩn từ lớp mỡ gai nhím để bào chế các loại thuốc xịt khử trùng vết thương thế hệ mới! |  | Hình ảnh lọ thuốc xịt y tế nano kháng khuẩn lấy cảm hứng từ gai nhím bắc mỹ; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b22 | 02:30.1–02:37.7 (7.6s) | L490 | Còn các kỹ sư cơ khí chính xác thì nghiên cứu cơ cấu ngàm kẹp của mỏ cò giày để tạo ra các kẹp gắp thủy lực siêu khỏe trong phẫu thuật nội soi! |  | Sơ đồ kẹp phẫu thuật nội soi vi phẫu mô phỏng chuyển động khớp mỏ của loài cò mỏ giày; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b23 | 02:37.7–02:46.2 (8.5s) | L491 | Ngành điện toán sinh học cũng đang học hỏi cách bộ não 4 g của cá mặt trăng quản lý khối cơ thể 2 tấn để tối ưu hóa thuật toán tiết kiệm năng lượng cho trí tuệ nhân tạo! |  | Đồ họa chip bán dẫn sinh học lấy cảm hứng từ mạng lưới nơ-ron tiết kiệm điện của cá mặt trăng; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b24 | 02:46.2–02:54.0 (7.8s) | L492 | Và các nhà sinh thái học bảo tồn đang nhân bản mùi hương thảo mộc đặc trưng của vẹt kakapo để chế tạo các bẫy pheromone theo dõi động vật quý hiếm! |  | Chai tinh dầu sinh học tỏa mùi xạ hương hoa cỏ tự nhiên của vẹt kakapo đặt trong phòng thí nghiệm; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b25 | 02:54.0–02:59.7 (5.7s) | L493 | Hàng triệu 5 tiến hóa của tự nhiên chính là phòng nghiên cứu và phát triển vĩ đại nhất, bền bỉ nhất mà loài người từng được thừa |  | Bức tranh toàn cảnh cây tiến hóa với các nhánh loài tỏa ra như những vệt pháo hoa rực rỡ; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b26 | 02:59.7–03:07.9 (8.2s) | L494 | hưởng! Không có một phát minh nào của con người lại không tìm thấy nguyên mẫu hoàn hảo đã tồn tại từ hàng triệu 5 trước trong cơ thể các loài sinh vật hoang dã! |  | Biểu đồ đối chiếu các công trình kiến trúc và cơ khí hiện đại với hình thái sinh học tự nhiên; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b27 | 03:07.9–03:16.0 (8.1s) | L495 | Biết đâu trong tương lai không xa, các giải thưởng Nobel Y Học danh giá sẽ được trao cho những công trình giải mã thành công các bí mật giải phẫu học này! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười giơ cao tấm huy chương vàng Nobel mô phỏng lấp lánh dưới ánh đèn hội nghị. |
| b28 | 03:16.0–03:22.0 (6.0s) | L496 | Một loại thuốc điều trị đột quỵ và chống hình thành cục máu đông dựa trên cơ chế van tĩnh mạch cổ của hươu cao cổ! |  | Mô hình phân tử thuốc chống đột quỵ thế hệ mới lấy cảm hứng từ hệ tuần hoàn hươu cao cổ phát sáng trên màn hình máy chiếu; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b29 | 03:22.0–03:27.6 (5.6s) | L497 | Một loại màng lọc không khí thông minh tự làm sạch và bẫy oxy mô phỏng cấu trúc chuông lặn của nhện nước! |  | Bản vẽ thiết kế màng lọc khí nano đa tầng mô phỏng sợi tơ kỵ nước của nhện lặn chuông; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b30 | 03:27.6–03:35.8 (8.2s) | L498 | Hay một loại kháng sinh peptide tự nhiên điều chế từ màng mỡ gai nhím có thể dập tắt hoàn toàn các chủng siêu vi khuẩn kháng thuốc nguy hiểm nhất hành tinh! |  | Hình ảnh phân tử kháng sinh sinh học gắn vào màng tế bào vi khuẩn kháng thuốc tiêu diệt tận gốc mầm bệnh; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b31 | 03:35.8–03:40.3 (4.5s) | L499 | Bài học y khoa vĩ đại nhất mà ca trực đêm kinh hoàng này để lại cho toàn thể chúng ta |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án bước lại gần cửa sổ lớn hội trường, nơi ánh nắng bình minh đầu tiên đang rọi những vệt sáng vàng óng ả qua khung kính. |
| b32 | 03:40.3–03:47.5 (7.2s) | L500 | là: Trong y học tiến hóa của tự nhiên, khái niệm dị tật hay khiếm khuyết chỉ là góc nhìn hạn hẹp của những kẻ chưa thấu hiểu trọn vẹn quy luật sinh tồn! |  | Toàn cảnh hội trường giao ban im phăng phắc, các bác sĩ trẻ xúc động lắng nghe từng lời tâm huyết của người thầy thuốc tiền bối. |
| b33 | 03:47.5–03:54.3 (6.8s) | L501 | Khi một cánh cửa giải phẫu truyền thống khép lại, tạo hóa sẽ mở ra một cánh cửa tiến hóa kỳ diệu khác đưa sinh vật vươn tới đỉnh cao thích nghi! |  | Bức tranh nghệ thuật cách điệu biểu tượng cây sự sống vươn cành lá tỏa bóng che chở cho muôn loài sinh vật kỳ thú; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b34 | 03:54.3–04:01.0 (6.8s) | L502 | Chúng ta không đến đây để sửa chữa tự nhiên, mà đến đây để chiêm ngưỡng, học hỏi và bảo bọc sự đa dạng sinh học vô giá của hành tinh này! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đặt tay lên ngực áo, ánh mắt tràn đầy tình yêu thương và sự kính trọng đối với muôn loài muôn thú. |
| b35 | 04:01.0–04:06.3 (5.3s) | L503 | Tôi xin tuyên bố: Ca trực đêm lịch sử của Phòng Cấp Cứu Tạo Hóa chính thức kết thúc thành công rực rỡ! |  | Toàn thể hội trường đứng bật dậy vỗ tay vang dội, tiếng reo hò chúc mừng rộn rã khắp các dãy bàn hội nghị; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b36 | 04:06.3–04:11.4 (5.1s) | L504 | Chuẩn bị ký giấy xuất viện và tiễn 10 người bạn đặc biệt của chúng ta trở về với thiên nhiên hoang dã nào! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười rạng rỡ, cùng toàn thể kíp trực bước ra sảnh lớn để đón ánh nắng sớm mai. |

### scene14 · TẠM BIỆT MƯỜI QUÁI KIỆT · 256.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.9 (7.9s) | L505 | Sáu giờ sáng. Bầu trời ngoài kia đã trong xanh trở lại sau cơn mưa bão đêm qua, những giọt sương mai đọng lấp lánh trên từng phiến lá ngoài sân bệnh viện. |  | Khung cảnh sân bệnh viện buổi sáng sớm trong lành, chim hót líu lo trên cành cây, những vạt nắng vàng tươi chiếu rọi lên các bậc thềm đá hoa cương; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b02 | 00:07.9–00:14.1 (6.2s) | L506 | Không khí buổi sớm mai ngọt ngào và mát rượi, xua tan đi toàn bộ sự mệt mỏi và căng thẳng của ca trực cấp cứu nghẹt thở vừa qua. |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án tháo chiếc khẩu trang y tế, hít một hơi thật sâu làn gió mát lành thổi vào qua khung cửa sổ lớn sảnh đón tiếp. |
| b03 | 00:14.1–00:20.1 (6.0s) | L507 | Cửa sảnh lớn của Phòng Cấp Cứu Tạo Hóa mở toang đón ánh nắng bình minh ấm áp. Và giờ phút chia tay đầy xúc động đã chính thức |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án trong chiếc áo blouse trắng tinh tươm cùng cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng đứng ở bậc thềm sảnh lớn, trên tay cầm mười tấm giấy chứng nhận xuất viện danh dự. |
| b04 | 00:20.1–00:27.6 (7.5s) | L508 | điểm. Mười bệnh nhân quái kiệt của chúng ta đã xếp thành một hàng ngay ngắn trước thềm sảnh lớn, mỗi người mang một vẻ mặt rạng rỡ và tự tin hơn bao giờ hết! |  | Toàn cảnh ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện đứng tề tựu đông đủ bên nhau trên sân cỏ xanh mướt của bệnh viện, ánh ban mai chiếu rực rỡ lên từng gương mặt ngộ nghĩnh. |
| b05 | 00:27.6–00:34.9 (7.3s) | L509 | Chú Khỉ Đột Lưng Bạc ôm một giỏ táo tươi ngon, cái bụng vẫn tròn vo nhưng đã hết đau hoàn toàn, vẫy cánh tay cơ bắp lực sĩ chào tạm biệt các y bác sĩ! |  | chú Khỉ Đột Lưng Bạc hoạt hình cơ bắp cuồn cuộn vạm vỡ, mảng lông bạc sáng chói dọc sống lưng, bụng to tròn căng phồng vì chứa đầy lá cây lên men, ngồi xếp bằng trên giường bệnh ôm bụng thở dài đứng thẳng người, một tay xách giỏ táo, tay kia vẫy chào vui vẻ với nụ cười thân thiện; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b06 | 00:34.9–00:42.6 (7.7s) | L510 | Chú Cá Thòi Lòi nhảy chồm chồm trên khay bùn tạm biệt, nháy đôi mắt lồi tinh nghịch rồi lặn tọt vào chiếc xe bồn nước chuyên dụng để về lại rừng Cà Mau! |  | chú Cá Thòi Lòi hoạt hình màu nâu xám lấm chấm xanh ngọc, hai mắt to tròn lồi hẳn trên đỉnh đầu chớp chớp ngộ nghĩnh, hai vây ngực bè to như đôi tay đang chống nạng gỗ mini đòi nhảy khỏi cáng cứu thương nhảy một cú ngoạn mục lên mép bồn xe nước cứu hộ, vẫy vây ngực chào tạm biệt mọi người; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b07 | 00:42.6–00:52.0 (9.4s) | L511 | Cô Ong Bắp Cày Ngọc bay lượn một vòng quanh đầu tôi như một lời cảm ơn duyên dáng, chiếc thân xanh ngọc bích lấp lánh dưới ánh bình minh trước khi bay vút lên bầu trời! |  | cô Ong Bắp Cày Ngọc (emerald cockroach wasp) hoạt hình thân thon dài phát sáng xanh ngọc bích kim loại lộng lẫy, chân dài thanh mảnh, tay cầm chiếc dao mổ phẫu thuật thần kinh siêu nhỏ giơ lên đầy tự tin chao lượn trên nền trời xanh biếc, để lại một vệt sáng lung linh trong không trung; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b08 | 00:52.0–00:59.2 (7.2s) | L512 | Chú Cá Mặt Trăng 2 tấn được cần cẩu nhẹ nhàng nâng bổng lên xe chuyên dụng chuyển thẳng ra vịnh biển để tiếp tục những chuyến lặn sâu 800 |  | chú Cá Mặt Trăng (ocean sunfish) hoạt hình khổng lồ hình đĩa tròn dẹt màu xám bạc, không có cuống đuôi, hai vây lưng và vây phần đuôi dựng đứng dài ngoằng, nằm ngửa trên chiếc cáng cứu thương quá khổ mắt to tròn ngơ ngác nằm trên võng bạt cứu hộ của cần cẩu, đôi mắt to tròn chớp chớp ngơ ngác chào khán giả trước khi xe khởi hành; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b09 | 00:59.2–01:07.7 (8.4s) | L513 | m! Chú Vẹt Kakapo béo tròn được tặng một chiếc ba-lô nhỏ chứa đầy hạt thông, lon ton đi bộ theo các nhân viên bảo tồn New Zealand với nụ cười mãn nguyện! |  | chú Vẹt Kakapo hoạt hình béo múp míp lông xanh rêu pha đốm nâu đen, mặt tròn lông tơ như chim cú mèo, mắt ngơ ngác dễ thương, hai cánh ngắn cũn cố vỗ lạch bạch trèo lên nóc tủ thuốc đeo chiếc ba-lô mini màu đỏ, đi lạch bạch từng bước vững chãi trên thảm cỏ, thỉnh thoảng quay đầu lại vẫy cánh; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b10 | 01:07.7–01:15.1 (7.4s) | L514 | Chú Lợn Hươu Babirusa kiêu hãnh khoe 4 chiếc răng nanh cong vút đã được làm sạch sáng bóng, bước đi tự tin về lại hòn đảo nhiệt đới hoang dã! |  | chú Lợn Hươu Babirusa hoạt hình da xám nhăn nheo ít lông, mõm dài, bốn chiếc răng nanh cong vút dị thường trong đó hai nanh trên mọc xuyên qua sống mũi uốn ngược về phía trán, vẻ mặt lo lắng sờ trán ngẩng cao đầu sải bước dũng mãnh, ánh sáng phản chiếu lấp lánh trên cặp nanh cong hoàn mỹ; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b11 | 01:15.1–01:21.5 (6.5s) | L515 | Quý cô Hươu Cao Cổ sải những bước chân thanh tao qua cổng bệnh viện, chiếc cổ dài 2 m vươn cao đón những làn gió mát lành của thảo nguyên! |  | chú Hươu Cao Cổ hoạt hình cao lêu nghêu có đốm hoa văn nâu vàng, chiếc cổ dài thẳng tắp quấn dải băng đo huyết áp y tế to bản màu đỏ, mắt to hiền từ chớp chớp bước đi uyển chuyển trong nắng mai, bóng dáng cao lều nghều in dài trên con đường rợp bóng cây; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b12 | 01:21.5–01:27.6 (6.0s) | L516 | Chú Cò Mỏ Giày khẽ cúi đầu chào lịch thiệp, rồi đột ngột xòe đôi cánh rộng 2,5 m bay vút lên không trung xé toạc làn sương |  | chú Cò Mỏ Giày hoạt hình lông xám tro, dáng đứng sừng sững bất động như tượng đá, chiếc mỏ khổng lồ màu vàng xám phình to hình chiếc guốc gỗ, ánh mắt lạnh như tiền đứng canh cửa phòng cấp cứu dang rộng đôi cánh khổng lồ màu xám tro, bay lượn uy nghi trên nền trời bình minh rực rỡ; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b13 | 01:27.6–01:35.8 (8.2s) | L517 | sớm! Và chú Nhím Lông Nhọn cùng chú Nhện Lặn Chuông tí hon cũng đã yên vị trong những chiếc lồng sinh thái an toàn để trở về với thiên nhiên hoang dã! |  | chú Nhím Lông Nhọn Bắc Mỹ hoạt hình béo tròn xù xì, toàn thân phủ kín ba mươi ngàn chiếc gai nhọn trắng đen, đang ôm chặt một thân cây gỗ gặm vỏ thuốc, người tỏa mùi tinh dầu thơm nhẹ và chú Nhện Lặn Chuông (diving bell spider) hoạt hình màu nâu đen nhiều lông mịn, tám chân ôm một chiếc bóng khí lấp lánh như viên ngọc trong suốt dưới bụng, đang ngâm mình trong bể nước dã chiến trong bể thủy tinh mini được các tình ng |
| b14 | 01:35.8–01:41.2 (5.4s) | L518 | Tôi hít một hơi thật sâu làn không khí trong lành của buổi sớm mai, cất chiếc ống nghe y tế vào túi áo khoác. |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đứng trên bậc thềm nhìn theo đoàn xe khuất dần sau rặng cây xanh, một nụ cười ấm áp nở trên môi. |
| b15 | 01:41.2–01:47.3 (6.1s) | L519 | Ca trực đêm kinh hoàng nhất cuộc đời làm bác sĩ của tôi tại Phòng Cấp Cứu Tạo Hóa đã chính thức khép lại trong niềm vui trọn vẹn. |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng đứng bên cạnh mỉm cười, trao cho bác sĩ một tách cà phê mới thơm lừng nóng hổi; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b16 | 01:47.3–01:52.3 (5.1s) | L520 | Nhưng bài học sâu sắc mà 10 sinh vật kỳ dị này để lại sẽ mãi mãi in đậm trong tâm trí của mỗi chúng ta: |  | Cận cảnh gương mặt đôn hậu và ánh mắt tràn đầy cảm xúc của ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án nhìn thẳng vào ống kính máy quay. |
| b17 | 01:52.3–01:59.9 (7.6s) | L521 | Trong thế giới tự nhiên kỳ diệu này, không có sinh vật nào là sai sót, không có nét giải phẫu nào là vô nghĩa. Mọi sự sống đều là một kiệt tác hoàn mỹ của mẹ Trái |  | Bức tranh toàn cảnh thiên nhiên bao la với rừng rậm, đại dương, thảo nguyên và bầu trời xanh ngắt nơi muôn loài cùng chung sống hòa hợp; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b18 | 01:59.9–02:06.4 (6.4s) | L522 | Đất! Hàng triệu 5 tiến hóa đã đẽo gọt nên những cơ chế sinh tồn tinh xảo vượt xa trí tưởng tượng phong phú nhất của con người! |  | Hình ảnh biểu tượng Trái Đất xanh tươi quay chầm chậm giữa không gian bao la lấp lánh muôn ngàn vì sao; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b19 | 02:06.4–02:11.1 (4.8s) | L523 | Mỗi sinh vật là một nốt nhạc độc đáo trong bản giao hưởng vĩ đại của sự sống trên hành tinh xanh! |  | Nốt nhạc ánh sáng phát ra từ hình vẽ các loài vật kết nối thành một bản tổng phổ âm nhạc lấp lánh; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b20 | 02:11.1–02:16.8 (5.6s) | L524 | Tôi cùng cô y tá trao từng túi thuốc bổ vitamin và cẩm nang chăm sóc sức khỏe sinh thái cho người đại diện của từng đoàn cứu |  | cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng cẩn thận xếp các túi thuốc bổ thảo dược đóng gói đẹp mắt trao vào tay các tình nguyện viên bảo tồn thiên nhiên hoang dã; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b21 | 02:16.8–02:26.2 (9.4s) | L525 | hộ. Chúng tôi dặn dò kỹ lưỡng: Anh khỉ đột nhớ giảm ăn lá cây có mủ đắng, chú cá thòi lòi nhớ bôi kem giữ ẩm mang cá khi leo cây, còn chú vẹt kakapo thì nhớ tập thể dục đi bộ đều đặn nhé! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười dặn dò từng bệnh nhân, các con vật đồng loạt gật đầu kêu líu lo ụt ịt như những lời chào cảm ơn chân thành. |
| b22 | 02:26.2–02:31.7 (5.5s) | L526 | Cả 10 bệnh nhân cùng hòa giọng tạo nên một bản hợp xướng rộn rã làm bừng sáng cả khoảng sân bệnh viện trong nắng |  | Tiếng hót của vẹt kakapo, tiếng gõ mỏ của cò mỏ giày và tiếng gầm trầm ấm của khỉ đột vang lên rộn rã giữa bình minh rực rỡ; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b23 | 02:31.7–02:38.3 (6.7s) | L527 | sớm! Một ca trực đêm đầy ắp tiếng cười, những giọt mồ hôi và sự kính phục vô bờ trước sức sáng tạo không giới hạn của tạo hóa! |  | Toàn cảnh đội ngũ y bác sĩ đứng vẫy tay chào tạm biệt đoàn xe cứu hộ đang lăn bánh qua cổng bệnh viện rợp bóng cây xanh; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b24 | 02:38.3–02:44.0 (5.7s) | L528 | Tu... tu... tuuuu! Bất thình lình, một tiếng còi tàu hơi nước trầm đục và ma mị từ đâu vang vọng lại qua thung lũng sương mù dày |  | Xa xa nơi đường ray xe lửa cổ uốn lượn quanh chân núi, một vệt khói trắng bốc lên cuồn cuộn giữa màn sương sớm bảng lảng; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b25 | 02:44.0–02:50.6 (6.6s) | L529 | đặc! Tiếng còi tàu hú lên từng hồi dồn dập, báo hiệu chuyến tàu tốc hành xuyên đêm chở 10 hành khách bí ẩn nhất hành tinh sắp lăn bánh vào |  | Cận cảnh đầu máy xe lửa hơi nước khổng lồ màu đen tuyền phong cách Art Deco thập niên 1930 với đèn pha vàng rực chiếu sáng đường ray; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b26 | 02:50.6–02:58.1 (7.5s) | L530 | ga! Một vụ án mất tích bí ẩn vừa xảy ra trên chuyến tàu tốc hành vượt bão tuyết! Và thám tử tài 3 sẽ phải vào cuộc để vén màn 10 bí mật sinh học gây sốc tiếp |  | Tấm vé tàu hỏa cổ điển đục lỗ mang dòng chữ HỒ SƠ MẬT MEGA 06: CHUYẾN TÀU TỐC HÀNH XUYÊN ĐÊM hiện lên trên màn hình trước khi khép lại; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b27 | 02:58.1–03:04.2 (6.0s) | L531 | theo! Những manh mối dấu vết của Rắn Hổ Mang Chúa, Cá Sấu Nước Mặn và Cá Mập Trắng đã bắt đầu lộ diện trên các toa tàu sương |  | Hình ảnh bóng đen của mười sinh vật bí ẩn trên chuyến tàu đêm đang lướt qua khung cửa sổ toa tàu hơi nước; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b28 | 03:04.2–03:10.2 (6.0s) | L532 | mù! Ai trong số 10 quái thú đầm lầy và đại dương này là thủ phạm thực sự của vụ án chấn động đường ray xe lửa đêm đông giá |  | Hình ảnh chiếc kính lúp thám tử soi vào dấu chân khổng lồ bí ẩn trên sàn toa tàu phủ đầy sương lạnh; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b29 | 03:10.2–03:18.8 (8.6s) | L533 | rét? Một hành trình phá án nghẹt thở kết hợp giữa tư duy trinh thám cổ điển và những bí mật giải phẫu học rợn người đang chờ đón quý khán giả trong siêu phẩm Mega số 6 tiếp theo! |  | Bức tranh poster giới thiệu MEGA 06 với hình ảnh đầu tàu hỏa hơi nước xuyên qua màn sương đêm ma mị; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b30 | 03:18.8–03:25.3 (6.5s) | L534 | Chiếc vali da cổ điển khóa số đang chứa bản hồ sơ mật về độc tố và lực cắn của 10 hung thần đầm lầy đang đợi được giải mã! |  | Cận cảnh chiếc vali da có gắn nhãn niêm phong hồ sơ mật đặt trên bàn gỗ toa tàu hỏa; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b31 | 03:25.3–03:30.5 (5.3s) | L535 | Ngoài kia, những bông tuyết đầu mùa bắt đầu rơi lả tả trên những mái vòm toa tàu hỏa bằng kim loại sáng |  | Những bông tuyết trắng muốt rơi nhẹ nhàng phủ kín mui tàu hỏa hơi nước đang đỗ tại sân ga cổ kính giữa thung lũng tuyết; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b32 | 03:30.5–03:35.6 (5.1s) | L536 | loáng. Tiếng chuông đồng hồ quả quýt của vị thám tử bí ẩn vang lên từng tiếng tích tắc điểm đúng 12 giờ |  | Bàn tay đeo găng da màu đen mở nắp chiếc đồng hồ quả quýt mạ vàng chạm khắc tinh xảo, kim đồng hồ chỉ đúng nửa đêm; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b33 | 03:35.6–03:43.7 (8.1s) | L537 | đêm! Một bức mật thư viết tay bằng mực tím bị kẹp dưới chân chiếc đèn bàn cổ, hé lộ danh sách 10 hành khách mang những vũ khí sinh học nguy hiểm bậc nhất tự nhiên! |  | Bức thư niêm phong sáp đỏ có in hình đầu lâu và dấu chân thú bí ẩn nằm trên bàn gỗ gụ toa tàu hạng nhất; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b34 | 03:43.7–03:49.1 (5.4s) | L538 | Liệu vị thám tử tài 3 có kịp phá giải 10 vụ án mạng bí ẩn trước khi chuyến tàu hơi nước cập bến bình minh hay |  | Chiếc bóng cao lớn của vị thám tử mặc áo măng tô dài và đội mũ phớt đứng sừng sững bên cửa sổ toa tàu nhìn vào màn sương tuyết; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b35 | 03:49.1–03:54.4 (5.4s) | L539 | không? Một bầu không khí nghẹt thở, ly kỳ và đậm chất trinh thám cổ điển đang đón đợi các bạn ở phía trước! |  | Ánh đèn vàng mờ ảo hắt ra từ các ô cửa kính toa tàu hơi nước đang lăn bánh xuyên qua hẻm núi tuyết phủ trắng xóa; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b36 | 03:54.4–04:01.2 (6.8s) | L540 | Cảm ơn toàn thể các đồng nghiệp và quý khán giả đã đồng hành cùng tôi qua ca trực đêm đáng nhớ này tại Phòng Cấp Cứu Tạo Hóa! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười giơ tay vẫy chào tạm biệt khán giả trong khi nền nhạc tươi vui vang lên khép lại tập phim. |
| b37 | 04:01.2–04:08.2 (7.0s) | L541 | Đừng quên bấm đăng ký kênh và nhấn chuông thông báo để không bỏ lỡ hành trình phá án tiếp theo trên Chuyến Tàu Tốc Hành Bí Ẩn nhé! Xin chào và hẹn gặp lại! |  | Dòng chữ VẼ CHUYỆN HOANG DÃ cùng biểu tượng nút đăng ký phát sáng rực rỡ trên màn hình kết thúc; KHÔNG có ông Bác Sĩ trong cảnh này. |
| b38 | 04:08.2–04:16.4 (8.1s) | L542 | Hãy để lại bình luận bên dưới xem ca bệnh nào đêm nay làm các bạn kinh ngạc và thán phục nhất nhé! Bác Sĩ Trưởng Khoa xin chào và hẹn gặp lại tất cả các bạn! |  | ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án cùng cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng vẫy tay chào với nụ cười rạng rỡ, màn hình mờ dần trong tiếng nhạc vui tươi; KHÔNG có ông Bác Sĩ trong cảnh này. |

## 5. Phân cảnh Shorts — từng beat

Banner: **PHÒNG CẤP CỨU TẠO HÓA / 10 BỆNH NHÂN DỊ THƯỜNG** · giọng 51.9s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Mười 2 giờ đêm tại Phòng Cấp Cứu Tạo Hóa! Còi báo động đỏ réo vang khi 10 ca bệnh kỳ dị nhất hành tinh cùng lúc tràn vào sảnh! |  |
| s02 | 00:06.6 | S02 | Anh Khỉ Đột Lưng Bạc đấm bẹp đầu xe hơi nhưng đang khóc ròng vì bụng đầy hơi men! |  |
| s03 | 00:10.6 | S03 | Chú Cá Thòi Lòi nhảy chồm chồm kiên quyết không thở dưới nước, dùng vây leo tót lên rèm cửa! |  |
| s04 | 00:15.6 | S04 | Cô Ong Bắp Cày Ngọc đòi chích nọc thôi miên não gián thành zombie ngoan ngoãn! |  |
| s05 | 00:18.9 | S05 | Khối thịt 2 tấn Cá Mặt Trăng nằm bẹp dí ngơ ngác, chỉ đang tắm nắng sau chuyến lặn sâu 800 m! |  |
| s06 | 00:24.1 | S06 | Vẹt Kakapo béo tròn 4 kg biểu diễn nhảy dù úp bụng xuống đống gối bông của y tá! |  |
| s07 | 00:28.5 | S07 | Lợn Babirusa với 4 nanh cong vút xuyên sống mũi uốn ngược sát sạt hộp sọ! |  |
| s08 | 00:32.3 | S08 | Hươu Cao Cổ huyết áp vọt lên gần 300, tim 11 kg bơm máu ngược trọng lực lên chiếc cổ 2 m! |  |
| s09 | 00:36.9 | S09 | Nhím Lông Nhọn rụng 30.000 chiếc gai có ngạnh, nhưng tẩm sẵn lớp mỡ kháng sinh tự chữa lành thần tốc! |  |
| s10 | 00:42.5 | S10 |  |  |
| s11 | 00:47.4 | S11 | Và Cò Mỏ Giày đứng như tượng đá rồi bất thần gõ mỏ súng máy 115 dB vang dội! Bấm ngay vào video dài để cùng Bác Sĩ Trưởng Khoa khám phá ca trực đêm kinh hoàng này nhé! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mười 2 giờ đêm. Cơn bão giông nhiệt đới cấp 12 đang gào thét dữ dội ngoài khung cửa kính phòng cấp cứu.". Bố cục: Bầu trời đêm đen kịt vần vũ mây bão, tia sét ngoằn ngoèo xé toạc màn đêm chiếu rọi tòa nhà bệnh viện cổ kính phong cách retro thập niên 1950; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Những vệt sét trắng xóa liên tục xé toạc bầu trời, rọi sáng tấm biển đồng cổ kính treo trước cổng lớn: Phòng Cấp Cứu Tạo Hóa.". Bố cục: Tấm biển đồng thau cổ điển khắc chìm dòng chữ PHÒNG CẤP CỨU TẠO HÓA phát sáng dưới ánh chớp bão đêm; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôi là Bác Sĩ Trưởng Khoa, người đã cầm dao mổ và ống nghe suốt 30 5 qua giữa những ca bệnh nghẹt thở nhất của tự nhiên.". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đứng bên cửa sổ phòng làm việc, tay cầm tách cà phê đen nóng bốc khói nghi ngút, ánh mắt trầm tư nhìn ra màn mưa bão trắng xóa.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng linh cảm nghề nghiệp mách bảo tôi rằng, đêm nay sẽ là ca trực điên rồ và kỳ quặc nhất trong toàn bộ sự nghiệp y khoa của mình.". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án nhấp một ngụm cà phê đắng, quay lại nhìn chiếc đồng hồ quả lắc bằng đồng đang gõ nhịp tích tắc trên tường.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiếc bàn làm việc bằng gỗ sồi của tôi chất đầy những xấp bệnh án ngả vàng, cùng chiếc ống nghe bằng đồng thau sáng bóng.". Bố cục: Bàn làm việc ngổn ngang hồ sơ bệnh án cổ điển, kính lúp y khoa, ống nghe bằng đồng và ngọn đèn bàn chụp xanh phong cách retro; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một ca trực đêm chuẩn mực đòi hỏi tinh thần thép, đôi bàn tay không bao giờ run rẩy và một lượng caffeine đủ để vận hành một đầu máy xe lửa!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án với tay rót thêm một tách cà phê đen sánh mịn từ chiếc bình thủy tinh cổ điển bốc khói nghi ngút.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bác sĩ trưởng khoa ơi! Nguy to rồi bác sĩ ơi! Toàn bộ chuông báo động ở 10 phòng khám chuyên khoa đang reo inh ỏi cùng một lúc kìa!". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng hớt hải đẩy tung cánh cửa gỗ đôi chạy vào phòng, hai tai thỏ dài rung lên bần bật, tay ôm xấp hồ sơ dày cộp.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hệ thống đường dây nóng khẩn cấp của bệnh viện vừa bị nghẽn mạch hoàn toàn vì hàng loạt cuộc gọi cấp cứu dồn dập từ khắp các châu lục!". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng chỉ tay về phía bảng tổng đài điện thoại cổ điển sau lưng đang nhấp nháy đèn đỏ liên hồi kèm chuông reo dồn dập; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mười bệnh nhân quái đản nhất hành tinh đang cùng lúc đổ bộ vào sảnh cấp cứu của chúng ta trên đủ mọi loại phương tiện vận chuyển!". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng run rẩy giơ xấp giấy bệnh án có dán mười bức ảnh sinh vật kỳ dị ra trước mặt bác sĩ trưởng khoa; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bình tĩnh nào cô y tá! Quy tắc số một của phòng cấp cứu: Càng hoảng loạn thì càng phải pha một tách cà phê thật đậm và kiểm tra lại danh sách bệnh nhân!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đặt tách cà phê xuống đĩa sứ, kéo chiếc kính lão đồi mồi xuống sống mũi rồi đón lấy tập hồ sơ từ tay y tá.
```
</details>

<details><summary>L100</summary>

```text
HÌNH L100 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sau đó, nhện liên tục ngoi lên mặt nước, dùng bụng vận chuyển từng bọt khí lớn lặn xuống nhả vào bên trong mái vòm tơ.". Bố cục: Từng bọt khí được nhả ra tích tụ dần bên dưới mái vòm, đẩy toàn bộ nước ra ngoài và biến chiếc vòm tơ thành một căn phòng chứa đầy không khí khô ráo; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L101</summary>

```text
HÌNH L101 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mái vòm tơ căng phồng lên như một quả bóng khí trong suốt, chú nhện thong thả chui vào bên trong ngồi nghỉ ngơi khô ráo!". Bố cục: chú Nhện Lặn Chuông (diving bell spider) hoạt hình màu nâu đen nhiều lông mịn, tám chân ôm một chiếc bóng khí lấp lánh như viên ngọc trong suốt dưới bụng, đang ngâm mình trong bể nước dã chiến ngồi vắt vẻo bên trong chiếc chuông lặn khô ráo, tám chân buông thõng thư giãn giữa làn nước sâu; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L102</summary>

```text
HÌNH L102 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và đây là điều kỳ diệu nhất mà nghiên cứu kinh điển của giáo sư Seymour công bố trên Tạp Chí Sinh Học Thực Nghiệm đã chứng minh:". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án giơ ngón tay chỉ lên màn hình hiển thị đồ thị nồng độ oxy hòa tan trong nước.
```
</details>

<details><summary>L103</summary>

```text
HÌNH L103 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiếc chuông lặn bằng tơ này không chỉ là một cái kho chứa khí thụ động, mà nó hoạt động chính xác như một lá phổi vật lý hay một chiếc mang nhân tạo siêu việt!". Bố cục: Hình ảnh đồ họa mô phỏng các phân tử oxy hòa tan trong nước xung quanh tự động khuếch tán thẩm thấu qua màng tơ mỏng đi vào trong chuông; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L104</summary>

```text
HÌNH L104 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi nhện tiêu thụ oxy bên trong chuông, nồng độ oxy trong chuông giảm xuống thấp hơn nồng độ oxy hòa tan trong nước xung quanh chiếc chuông.". Bố cục: Mũi tên đồ họa màu xanh lục mô phỏng dòng oxy tự động chảy ngược từ nước vào chuông qua chênh lệch áp suất; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L105</summary>

```text
HÌNH L105 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chênh lệch áp suất riêng phần này thúc đẩy các phân tử oxy từ nước tự động khuếch tán thẩm thấu xuyên qua màng tơ mỏng đi vào bên trong chuông!". Bố cục: Dòng dưỡng khí oxy liên tục được bổ sung tự động từ môi trường nước vào trong không gian sống của chú nhện; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L106</summary>

```text
HÌNH L106 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đồng thời, khí các-bô-níc độc hại do con nhện thở ra sẽ dễ dàng hòa tan và khuếch tán ngược ra ngoài dòng nước chảy xung quanh.". Bố cục: Các bọt khí CO2 màu xám li ti thẩm thấu xuyên qua lớp màng tơ trôi dạt ra ngoài dòng nước; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L107</summary>

```text
HÌNH L107 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ cơ chế trao đổi khí thần kỳ đó, lượng oxy khuếch tán vào chuông có thể đáp ứng đủ nhu cầu hô hấp của chú nhện suốt hơn 24 giờ liên tục!". Bố cục: bảng kẹp bệnh án y khoa khổng lồ (clipboard) kẹp trên giá đỡ kim loại, hiển thị 10 hồ sơ bệnh án hoạt hình với nhãn đơn thuốc phát sáng và sóng nhịp tim ECG màu đỏ nhấp nháy (không có chữ, không có số) hiển thị con số 24 giờ cùng biểu tượng đồng hồ cát phát sáng xanh bên cạnh chiếc chuông lặn; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L108</summary>

```text
HÌNH L108 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Con nhện có thể nằm ngủ say sưa, ăn thịt con mồi và chăm sóc bầy con non trong chiếc chuông lặn suốt cả ngày đêm mà không cần phải ngoi lên mặt nước một lần nào!". Bố cục: Cảnh gia đình nhện lặn chuông sum vầy ấm cúng bên trong mái vòm khí sáng rực dưới đáy hồ trong vắt; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L109</summary>

```text
HÌNH L109 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thậm chí chú nhện đực còn dệt chiếc chuông lặn lớn hơn con cái 30% để làm phòng tân hôn lãng mạn dưới đáy nước!". Bố cục: Hai chú nhện lặn chuông bơi lội quấn quýt bên nhau trong chiếc chuông lặn rộng rãi dưới làn nước trong xanh; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để tôi đọc to danh sách phân loại bệnh nhân đêm nay cho toàn thể kíp trực cùng nghe xem tạo hóa vừa gửi tới những ca hóc búa nào!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án lật giở từng trang hồ sơ bệnh án kẹp trên chiếc bảng kẹp bệnh án y khoa khổng lồ (clipboard) kẹp trên giá đỡ kim loại, hiển thị 10 hồ sơ bệnh án hoạt hình với nhãn đơn thuốc phát sáng và sóng nhịp tim ECG màu đỏ nhấp nháy (không có chữ, không có số), ánh mắt sáng lên vẻ thích thú và tò mò cao độ.
```
</details>

<details><summary>L110</summary>

```text
HÌNH L110 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vào mùa đông băng giá khi mặt hồ đóng băng dày đặc, nhện chỉ việc rút sâu xuống đáy bùn, gia cố chuông tơ thật kín và ngủ đông yên bình ở nhiệt độ 0°C!". Bố cục: Cảnh mặt hồ phủ băng tuyết trắng xóa, phía sâu dưới đáy bùn chú chú Nhện Lặn Chuông (diving bell spider) hoạt hình màu nâu đen nhiều lông mịn, tám chân ôm một chiếc bóng khí lấp lánh như viên ngọc trong suốt dưới bụng, đang ngâm mình trong bể nước dã chiến cuộn tròn ngủ say sưa bên trong chiếc chuông tơ ấm áp; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L111</summary>

```text
HÌNH L111 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lớp màng tơ nhện bảo vệ nó khỏi các tinh thể băng giá sắc nhọn và giữ cho áp suất dưỡng khí bên trong luôn ở mức ổn định suốt nhiều tháng ròng!". Bố cục: Lớp băng tuyết bao phủ bên trên nhưng chiếc chuông lặn dưới đáy bùn vẫn nguyên vẹn ấm áp như một chiếc kén sinh học kỳ diệu; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L112</summary>

```text
HÌNH L112 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thử hỏi có chiếc tàu ngầm hạt nhân hay bộ đồ lặn hiện đại nào của loài người có thể hoạt động bền bỉ và thông minh đến mức độ như thế này không?". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án nháy mắt cười hóm hỉnh nhìn toàn thể hội đồng y khoa đang gật gù thán phục.
```
</details>

<details><summary>L113</summary>

```text
HÌNH L113 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chẩn đoán Khoa Hô Hấp Ngược của Phòng Cấp Cứu Tạo Hóa: Bệnh nhân sở hữu hệ hô hấp dưới nước hiện đại và tiết kiệm năng lượng nhất hành tinh!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án cất chiếc ống nghe vào túi áo, mỉm cười nhìn chú chú Nhện Lặn Chuông (diving bell spider) hoạt hình màu nâu đen nhiều lông mịn, tám chân ôm một chiếc bóng khí lấp lánh như viên ngọc trong suốt dưới bụng, đang ngâm mình trong bể nước dã chiến đang tung tăng bơi lượn trong bể nước mới.
```
</details>

<details><summary>L114</summary>

```text
HÌNH L114 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đơn thuốc cho bệnh nhân: một bể thủy tinh nước ngọt sâu 30 cm, bổ sung vài cành rong đuôi chó tươi ngon và tuyệt đối cấm dùng mặt nạ thở oxy!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án ký xoẹt một chữ ký sắc sảo vào bệnh án số hai, đưa cho y tá đi chuẩn bị chỗ nghỉ ngơi cho chú nhện.
```
</details>

<details><summary>L115</summary>

```text
HÌNH L115 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bệnh nhân số 2 đã tìm lại được bầu không khí quen thuộc! Giờ thì mời toàn đội di chuyển sang Khoa Chấn Thương Chỉnh Hình để đón tiếp một vận động viên điền kinh có vây!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án sải bước ra khỏi phòng khám hô hấp, hướng thẳng về phía phòng chỉnh hình đang có tiếng đập huỳnh huỵch ngoài cửa.
```
</details>

<details><summary>L116</summary>

```text
HÌNH L116 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Huỳnh huỵch! Bẹp bẹp bẹp! Tiếng đập sàn dồn dập vang lên ngay khi chúng tôi vừa mở cửa phòng khám Khoa Chấn Thương Chỉnh Hình!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mở cửa bước vào, một bóng đen nhỏ xíu nhảy vèo qua đầu bác sĩ rồi đáp bẹp xuống chiếc bàn khám kim loại sáng bóng.
```
</details>

<details><summary>L117</summary>

```text
HÌNH L117 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và cảnh tượng trước mắt làm các bác sĩ ngoại khoa phải đứng hình trong kinh ngạc!". Bố cục: Căn phòng khám chỉnh hình với các nẹp xương và mô hình xương khớp, nhưng giữa phòng là một chú cá đang nhảy nhót tưng bừng; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L118</summary>

```text
HÌNH L118 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một chú Cá Thòi Lòi dài 20 cm, mình mẩy lấm lem bùn đất, đang dùng 2 chiếc vây ngực cơ bắp chống thẳng đứng trên mặt bàn như một lực sĩ đang hít đất!". Bố cục: Cận cảnh chú Cá Thòi Lòi hoạt hình màu nâu xám lấm chấm xanh ngọc, hai mắt to tròn lồi hẳn trên đỉnh đầu chớp chớp ngộ nghĩnh, hai vây ngực bè to như đôi tay đang chống nạng gỗ mini đòi nhảy khỏi cáng cứu thương da xám đốm hoa văn bùn lầy, hai vây ngực to bè như đôi tay lực lưỡng đang chống đỡ toàn bộ nửa thân trước; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L119</summary>

```text
HÌNH L119 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đôi mắt to tròn như 2 chiếc kính tiềm vọng nhô hẳn lên trên đỉnh đầu, xoay tít 300 6 mươi độ quét nhìn khắp lượt các bác sĩ trong phòng khám!". Bố cục: Đôi mắt lồi ngộ nghĩnh của cá thòi lòi xoay độc lập hai hướng, con ngươi đen láy chớp chớp đầy cảnh giác; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ca số một: Một anh chàng Khỉ Đột Lưng Bạc nặng 200 kg, sở hữu cú đấm ngàn cân nhưng đang nằm ôm bụng khóc thét vì ứ đọng khí gas!". Bố cục: chú Khỉ Đột Lưng Bạc hoạt hình cơ bắp cuồn cuộn vạm vỡ, mảng lông bạc sáng chói dọc sống lưng, bụng to tròn căng phồng vì chứa đầy lá cây lên men, ngồi xếp bằng trên giường bệnh ôm bụng thở dài nằm co ro trên giường bệnh dã chiến, hai tay ôm chiếc bụng tròn ủng căng phồng vẻ mặt mếu máo tội nghiệp; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L120</summary>

```text
HÌNH L120 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cứ mỗi lần cô y tá cầm chiếc khăn ẩm tiến lại gần, chú cá lại quẫy đuôi một cú đánh tách, phóng bổng người lên không trung cao tới 60 cm!". Bố cục: Chú cá búng mạnh chiếc đuôi cơ bắp, bay bổng lên cao vượt qua đầu y tá rồi đáp xuống khay nhôm y tế kêu leng keng; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L121</summary>

```text
HÌNH L121 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bác sĩ ơi bắt nó lại giùm em với! Con cá này bị co giật động kinh hay bị gãy xương chậu mà nó cứ nhảy lung tung khắp phòng thế này ạ?". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng hai tay cầm chiếc vợt lưới y tế mini rượt đuổi chú cá quanh bàn khám, thở hổn hển mặt đỏ bừng bừng.
```
</details>

<details><summary>L122</summary>

```text
HÌNH L122 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó là loài cá mà sao nó không chịu ở dưới nước, lại cứ thích leo lên bậc cửa sổ rồi leo lên bàn làm việc ngồi nhìn ra ngoài đường thế này?". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng chỉ tay lên gờ cửa sổ gỗ, nơi chú cá vừa nhảy tót lên bám chặt vào mép gỗ bằng giác hút ở bụng; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L123</summary>

```text
HÌNH L123 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Có khi nào xương vây của nó bị biến dạng thành chân khỉ rồi không bác sĩ ơi?". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng tròn xoe mắt thỏ ngơ ngác nhìn chú cá đang trố mắt nhìn lại mình; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L124</summary>

```text
HÌNH L124 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy cất chiếc vợt lưới đi cô y tá! Đây không phải là cá bị co giật, mà là sinh vật chuyển tiếp vĩ đại nhất còn sống sót từ kỷ Devon cách đây gần 400 triệu 5!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án bật cười giơ tay ra hiệu cho y tá dừng lại, bước tới quan sát gần chú cá đang hiên ngang chống vây trên bàn.
```
</details>

<details><summary>L125</summary>

```text
HÌNH L125 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cá Thòi Lòi là loài cá lưỡng cư độc nhất vô nhị có thể dành tới 90% thời gian trong ngày sống hoàn toàn trên cạn!". Bố cục: chú Cá Thòi Lòi hoạt hình màu nâu xám lấm chấm xanh ngọc, hai mắt to tròn lồi hẳn trên đỉnh đầu chớp chớp ngộ nghĩnh, hai vây ngực bè to như đôi tay đang chống nạng gỗ mini đòi nhảy khỏi cáng cứu thương đứng hiên ngang trên bờ bùn đất ven rừng ngập mặn Cà Mau, xung quanh là những rễ cây đước ngoằn ngoèo nhô lên khỏi mặt nước; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L126</summary>

```text
HÌNH L126 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó có thể đi bộ, chạy nước rút trên bùn lầy, trèo thoăn thoắt lên các rễ cây đước và thậm chí nhảy cao gấp 3 lần chiều dài cơ thể mình!". Bố cục: Chú cá thòi lòi dùng hai vây ngực bám vào rễ cây đước cao nửa mét trên mặt nước, ngẩng cao đầu đón gió biển; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L127</summary>

```text
HÌNH L127 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy nhìn vào cấu trúc giải phẫu của 2 chiếc vây ngực này trên phim chụp X-quang: Đây chính là tiền thân của đôi cánh tay và đôi chân động vật 4 chân trên cạn!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án bật đèn soi phim X-quang, chỉ vào các khớp xương vây ngực có cấu trúc xương cánh tay và xương quay nguyên thủy.
```
</details>

<details><summary>L128</summary>

```text
HÌNH L128 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các xương vây ngực đã tiến hóa thành các khớp xương trục có cơ bắp khỏe khoắn nâng đỡ, hoạt động tương tự như khuỷu tay và cổ tay của động vật trên cạn!". Bố cục: Sơ đồ giải phẫu ba chiều hiển thị bó cơ bắp dày đặc liên kết giữa xương bả vai nguyên thủy và các tia vây biến tính của cá thòi lòi; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L129</summary>

```text
HÌNH L129 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hai vây bụng của nó hợp nhất lại ở phía dưới tạo thành một giác hút hình chiếc cốc vô cùng chắc chắn!". Bố cục: Cận cảnh mặt bụng của cá thòi lòi với giác hút tròn xoe giúp nó bám chặt như keo dính vào các thân cây trơn trượt; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ca số 2: Một chú Nhện Lặn Chuông tí hon đang cố tình nhảy ra khỏi mặt nạ thở oxy nhi khoa để lao đầu xuống chậu nước!". Bố cục: chú Nhện Lặn Chuông (diving bell spider) hoạt hình màu nâu đen nhiều lông mịn, tám chân ôm một chiếc bóng khí lấp lánh như viên ngọc trong suốt dưới bụng, đang ngâm mình trong bể nước dã chiến tám chân thoăn thoắt bò trốn khỏi chiếc mặt nạ dưỡng khí mini, nhảy ùm vào bình nước thủy tinh; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L130</summary>

```text
HÌNH L130 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vào mùa giao phối, các chàng cá đực còn dựng đứng chiếc vây lưng sặc sỡ như một cánh buồm ngũ sắc, nhảy múa tưng bừng trên bãi bùn để thu hút bạn tình!". Bố cục: Chú cá thòi lòi đực xòe chiếc vây lưng màu xanh lam viền đỏ rực rỡ, uốn lượn nhảy múa giữa thảm bùn rừng đước; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L131</summary>

```text
HÌNH L131 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng bí ẩn lớn nhất khiến các nhà sinh lý học hô hấp phải kinh ngạc là: Làm thế nào một con cá có thể thở trên cạn suốt nhiều giờ liền mà không bị ngạt thở?". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đưa ngón tay trỏ nhẹ nhàng nâng phần nắp mang phồng to của chú cá lên để kiểm tra.
```
</details>

<details><summary>L132</summary>

```text
HÌNH L132 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bởi vì mang cá thông thường khi lên cạn sẽ bị khô ráp, các phiến mang dính bết lại với nhau làm mất diện tích tiếp xúc với không khí và con cá sẽ chết ngạt nhanh chóng!". Bố cục: Hình ảnh so sánh lá mang cá bình thường bị bết dính trên cạn với khoang mang phồng tròn căng mọng của cá thòi lòi; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L133</summary>

```text
HÌNH L133 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thế nhưng cá thòi lòi lại sở hữu 2 khoang mang khổng lồ có van đóng mở kín mít như 2 chiếc bình dưỡng khí của thợ lặn!". Bố cục: Sơ đồ giải phẫu khoang mang của cá thòi lòi hiển thị van cơ vòng đóng chặt giữ lại một lượng nước biển giàu oxy bên trong; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L134</summary>

```text
HÌNH L134 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trước khi rời khỏi mặt nước để bò lên bãi bùn, nó ngậm đầy một họng nước và không khí rồi siết chặt van nắp mang lại!". Bố cục: Chú chú Cá Thòi Lòi hoạt hình màu nâu xám lấm chấm xanh ngọc, hai mắt to tròn lồi hẳn trên đỉnh đầu chớp chớp ngộ nghĩnh, hai vây ngực bè to như đôi tay đang chống nạng gỗ mini đòi nhảy khỏi cáng cứu thương ngụp đầu xuống nước hút căng khoang miệng rồi bò lên bãi bùn với hai bên má phồng to như hai quả bóng bàn; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L135</summary>

```text
HÌNH L135 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bằng cách đó, các phiến mang bên trong luôn luôn được ngâm ngập trong nước giàu dưỡng khí, cho phép nó hô hấp bình thường ngay giữa bãi cạn khô khốc!". Bố cục: Hình ảnh minh họa các tia nước giàu oxy luân chuyển liên tục bên trong khoang mang kín mít nuôi dưỡng các tế bào; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L136</summary>

```text
HÌNH L136 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa hết đâu nhé! Cá thòi lòi còn có khả năng hô hấp qua da và niêm mạc miệng cực kỳ tinh vi!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án dùng kính lúp soi lớp da nhầy bóng loáng phủ đầy các mao mạch nước màu li ti của chú cá.
```
</details>

<details><summary>L137</summary>

```text
HÌNH L137 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hơn 50% lượng oxy của nó được hấp thu trực tiếp qua lớp da mỏng giàu mạch nước màu, miễn là da của nó luôn được giữ ẩm ướt!". Bố cục: Sơ đồ mạng lưới mao mạch nước màu dày đặc nằm ngay dưới lớp biểu bì da cá thòi lòi đang hấp thu các phân tử oxy tự do từ không khí; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L138</summary>

```text
HÌNH L138 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đó là lý do tại sao anh chàng này thỉnh thoảng lại lăn lộn trên bùn nhão để tráng một lớp bùn bảo vệ giữ ẩm cho làn da của mình!". Bố cục: Chú cá thòi lòi thích thú nằm lăn qua lăn lại trên lớp bùn mịn màng như đang tắm bùn khoáng spa; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L139</summary>

```text
HÌNH L139 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và các bạn hãy nhìn vào đôi mắt kỳ diệu nhô cao trên đỉnh đầu của nó mà xem!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án chỉ đầu bút vào đôi mắt lồi to tướng đang chớp chớp liên hồi của chú cá.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ca số 3: Một vận động viên bơi lội có tên Cá Thòi Lòi kiên quyết không chịu nằm yên trong bồn nước mà cứ đòi leo lên bàn khám để chống đẩy!". Bố cục: chú Cá Thòi Lòi hoạt hình màu nâu xám lấm chấm xanh ngọc, hai mắt to tròn lồi hẳn trên đỉnh đầu chớp chớp ngộ nghĩnh, hai vây ngực bè to như đôi tay đang chống nạng gỗ mini đòi nhảy khỏi cáng cứu thương dùng hai vây ngực cơ bắp chống thẳng đứng trên mặt bàn khám, đôi mắt lồi đảo tròn tinh nghịch; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L140</summary>

```text
HÌNH L140 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đó là 2 chiếc kính tiềm vọng thực thụ giúp nó vừa ngâm mình dưới nước vừa quan sát được toàn bộ con mồi và kẻ thù trên cạn!". Bố cục: Hình ảnh chú cá ẩn mình dưới nước chỉ để lộ hai con mắt nhô lên khỏi mặt bùn quan sát xung quanh; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L141</summary>

```text
HÌNH L141 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi khi mắt bị khô do gió biển, cá thòi lòi chỉ việc thụt 2 mắt vào trong hốc đầu, nơi có một túi nước đặc biệt để rửa sạch và cấp ẩm cho giác mạc rồi lại đẩy mắt nhô lên!". Bố cục: Đồ họa chuyển động chậm mô phỏng mắt cá thụt xuống hốc nước dưới đáy mắt để chớp mắt rồi bật ngược trở lại; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L142</summary>

```text
HÌNH L142 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thật là một cơ chế chớp mắt độc nhất vô nhị không hề giống bất kỳ loài động vật có xương sống nào trên Trái Đất!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án thích thú dùng đèn soi phản xạ giác mạc của chú cá đang thụt mắt xuống hốc nước rồi đẩy lên đầy ngộ nghĩnh.
```
</details>

<details><summary>L143</summary>

```text
HÌNH L143 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cá thòi lòi còn có một tập tính kỳ lạ là trèo lên các thân cây đước cao để phơi nắng và tránh thủy triều dâng cao cuốn trôi!". Bố cục: Chú cá thòi lòi dùng vây ngực khỏe khoắn bám chặt vào thân cây đước, leo thoăn thoắt lên cao như một chú thằn lằn; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L144</summary>

```text
HÌNH L144 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vào mùa sinh sản, những chú cá thòi lòi đực còn đào những chiếc hang bùn sâu tới 1,5 m có cấu trúc hình chữ U vô cùng phức tạp!". Bố cục: Bản vẽ mặt cắt địa chất đáy rừng ngập mặn hiển thị chiếc hang bùn hình chữ U sâu một mét rưỡi dưới đáy bãi lầy; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L145</summary>

```text
HÌNH L145 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đáy hang là một túi khí ngầm hoàn toàn kỵ khí và không có dưỡng khí tự nhiên.". Bố cục: Sơ đồ buồng ấp trứng ngầm dưới đáy hang sâu tăm tối; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L146</summary>

```text
HÌNH L146 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để bảo vệ bầy trứng non, cá bố liên tục ngoi lên mặt nước ngậm từng ngụm không khí rồi lặn xuống đáy hang nhả vào buồng ấp trứng!". Bố cục: Chú cá thòi lòi bố cần mẫn ngậm không khí lặn xuống nhả bóng khí vào buồng ấp trứng cho đến khi buồng chứa đầy dưỡng khí; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L147</summary>

```text
HÌNH L147 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó thực hiện hàng trăm chuyến lặn tiếp oxy như một thợ lặn chuyên nghiệp để nuôi dưỡng bầy con thơ!". Bố cục: Hình ảnh cảm động về chú cá bố túc trực bên bầy trứng non phát sáng lấp lánh dưới đáy hang ngầm; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L148</summary>

```text
HÌNH L148 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thật là một người cha mẫu mực và một chiến binh sinh học kiên cường bậc nhất của thế giới ngập mặn!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án vỗ nhẹ lên lưng chú cá, ánh mắt ánh lên niềm khâm phục chân thành.
```
</details>

<details><summary>L149</summary>

```text
HÌNH L149 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chúng còn đắp những bức tường thành bằng bùn cao tới 10 cm quanh miệng hang để phân chia ranh giới lãnh thổ với hàng xóm!". Bố cục: Chú cá thòi lòi cần mẫn ngoạm từng viên bùn đắp thành bờ lũy kiên cố quanh tổ ấm của mình; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ca số 4: Một nữ phẫu thuật viên tí hon mang tên Ong Bắp Cày Ngọc đang dẫn giải một con gián khổng lồ đi vào phòng mổ thần kinh như dắt thú cưng!". Bố cục: cô Ong Bắp Cày Ngọc (emerald cockroach wasp) hoạt hình thân thon dài phát sáng xanh ngọc bích kim loại lộng lẫy, chân dài thanh mảnh, tay cầm chiếc dao mổ phẫu thuật thần kinh siêu nhỏ giơ lên đầy tự tin màu xanh ngọc bích óng ánh đang dùng râu kéo lê một chú gián to lớn ngoan ngoãn bước từng bước vô hồn; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L150</summary>

```text
HÌNH L150 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi có kẻ thù xâm phạm bờ cõi, chàng cá lập tức dựng vây lưng lên thách đấu và búng người tung cú húc đầu sấm sét để đuổi kẻ lạ mặt!". Bố cục: Hai chú cá thòi lòi đối đầu nảy lửa trên bờ bùn, giương vây búng đuôi tranh giành từng tấc đất; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L151</summary>

```text
HÌNH L151 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà cổ sinh vật học coi cá thòi lòi như một hóa thạch sống phản chiếu chính xác bước chuyển mình vĩ đại của sinh giới từ đại dương lên đất liền!". Bố cục: Mô hình hóa thạch loài cá cổ đại Tiktaalik đặt cạnh chú cá thòi lòi hiện đại cho thấy sự tương đồng kỳ diệu về cấu trúc xương chi; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L152</summary>

```text
HÌNH L152 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chẩn đoán Khoa Chấn Thương Chỉnh Hình của Phòng Cấp Cứu Tạo Hóa: Không có gãy xương hay dị tật nào cả! Đây là một vận động viên điền kinh lưỡng cư khỏe mạnh 100%!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đóng dấu ĐẠT CHUẨN XUẤT SẮC lên bệnh án số ba, đưa cho chú cá một miếng tôm nhỏ tươi ngon.
```
</details>

<details><summary>L153</summary>

```text
HÌNH L153 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đơn thuốc cho bệnh nhân: Một khay bùn ngập mặn ẩm ướt pha chút muối biển và vài nhánh rễ cây để anh chàng tha hồ tập hít đất và leo trèo!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đặt chú cá vào khay bùn chuyên dụng, chú chú Cá Thòi Lòi hoạt hình màu nâu xám lấm chấm xanh ngọc, hai mắt to tròn lồi hẳn trên đỉnh đầu chớp chớp ngộ nghĩnh, hai vây ngực bè to như đôi tay đang chống nạng gỗ mini đòi nhảy khỏi cáng cứu thương híp mắt nhai miếng tôm rồi búng đuôi một cái như lời cảm ơn sâu sắc.
```
</details>

<details><summary>L154</summary>

```text
HÌNH L154 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vừa dứt lời thì từ sảnh chính bỗng vang lên một tiếng rầm chấn động cả sàn nhà! Báo động đỏ: Phòng chờ cấp cứu vừa bị sập một mảng sàn!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án và y tá giật bắn người, lập tức lao nhanh ra sảnh chính xem chuyện gì đang xảy ra.
```
</details>

<details><summary>L155</summary>

```text
HÌNH L155 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một giờ 30 phút sáng. Tôi vừa bước chân ra khỏi Khoa Chấn Thương thì một tiếng rầm long trời lở đất vang lên làm rung chuyển cả tòa nhà bệnh viện!". Bố cục: Bụi vôi trắng từ trần nhà rơi lả tả xuống sàn hành lang, các bóng đèn neon trên trần chao đảo dữ dội, tiếng kim loại gãy vụn rền vang từ sảnh lớn; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L156</summary>

```text
HÌNH L156 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các giá thuốc thủy tinh rung lên bần bật kêu leng keng, sàn gạch men dưới chân tôi nứt toác ra một đường dài 3 m!". Bố cục: Cận cảnh đường nứt trên sàn gạch men hoa cương sảnh bệnh viện dưới sức nặng ngàn cân đè nén; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L157</summary>

```text
HÌNH L157 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tiếng còi báo động khẩn cấp rú lên từng hồi chói tai, hòa lẫn với tiếng thét thất thanh của đội điều dưỡng tiếp đón ngoài cửa sảnh!". Bố cục: Đèn báo động màu đỏ rực trên tường nhấp nháy liên hồi, các nhân viên bảo vệ và y tá chạy tán loạn; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L158</summary>

```text
HÌNH L158 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trời đất quỷ thần ơi! Chuyện gì vừa xảy ra thế này? Xe tải chở đá tảng đâm sập cổng bệnh viện hay có thiên thạch vừa rơi trúng phòng tiếp đón vậy?". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án hớt hải chạy vội ra sảnh lớn, tay vịn vào lan can cầu thang nhìn xuống sảnh đón tiếp đầy khói bụi.
```
</details>

<details><summary>L159</summary>

```text
HÌNH L159 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cả bệnh viện rung chuyển như vừa trải qua một trận động đất 7 độ richter giữa đêm khuya thanh vắng!". Bố cục: Khung cảnh hỗn loạn nơi sảnh đón tiếp với các y bác sĩ ôm chặt cột nhà để giữ thăng bằng; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ca số 5: Một khối thịt khổng lồ nặng 2 tấn mang tên Cá Mặt Trăng vừa làm sập gãy hoàn toàn chiếc bàn nâng thủy lực của đội vận chuyển!". Bố cục: chú Cá Mặt Trăng (ocean sunfish) hoạt hình khổng lồ hình đĩa tròn dẹt màu xám bạc, không có cuống đuôi, hai vây lưng và vây phần đuôi dựng đứng dài ngoằng, nằm ngửa trên chiếc cáng cứu thương quá khổ mắt to tròn ngơ ngác tròn xoe như chiếc bánh kếp khổng lồ nằm bẹp trên sàn sảnh đón tiếp, đôi mắt tròn xoe ngơ ngác chớp chớp; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L160</summary>

```text
HÌNH L160 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hàng loạt hồ sơ bệnh án bay tứ tung giữa làn khói bụi mịt mù, tiếng chuông điện thoại bàn reo inh ỏi không dứt!". Bố cục: Các xấp giấy bệnh án bay lượn trong không trung như đàn bướm trắng giữa sảnh bệnh viện ngổn ngang; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L161</summary>

```text
HÌNH L161 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tiếng la hét hỗn loạn của đội vận chuyển làm cả tòa nhà như biến thành một công trường xây dựng gặp sự cố sập giàn giáo!". Bố cục: Đội ngũ bảo vệ và hộ lý cầm đèn pin chạy đôn chạy đáo giữa màn bụi vôi trắng xóa bao phủ sảnh lớn; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L162</summary>

```text
HÌNH L162 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bác sĩ trưởng khoa ơi cứu tụi em với! Cái bàn nâng thủy lực tải trọng 2 tấn của đội vận chuyển vừa bị gãy đôi làm đôi mảnh rồi!". Bố cục: Chú bảo vệ gấu đen lực lưỡng mặc áo đồng phục bảo vệ đang ôm chiếc kích thủy lực bị bẹp rúm, mặt mày tái mét hoảng hốt kêu cứu.
```
</details>

<details><summary>L163</summary>

```text
HÌNH L163 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chúng em vừa khiêng bệnh nhân số 4 từ xe tải thùng bạt xuống cáng thì cái cáng sắt gãy đánh rắc một cái, đè bẹp dúm luôn cả chiếc xe đẩy thuốc bên dưới!". Bố cục: Chiếc bàn nâng thủy lực bằng thép dày mười phân bị cong vênh gãy đôi, dầu thủy lực màu đỏ chảy lênh láng trên sàn nhà; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L164</summary>

```text
HÌNH L164 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bệnh nhân này to như một gian nhà lá, trơn tuột như cục xà bông khổng lồ và không có cổ, không có đuôi gì hết trơn bác sĩ ơi!". Bố cục: Chú bảo vệ giơ hai tay miêu tả kích thước khổng lồ của sinh vật lạ đang nằm chắn ngang sảnh đón tiếp; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L165</summary>

```text
HÌNH L165 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chúng em đã phải huy động tới 6 người đàn ông lực lưỡng mà vẫn không thể nhích nổi nó một xăng-ti-mét nào!". Bố cục: Sáu nhân viên bảo vệ to béo đang hò dô đẩy khối thịt khổng lồ nhưng bệnh nhân vẫn nằm ì ra như một tảng đá hoa cương; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L166</summary>

```text
HÌNH L166 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôi vội vàng rẽ đám đông bước tới hiện trường, và một cảnh tượng choáng ngợp hiện ra làm tôi phải dụi mắt 3 lần!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án sải bước dài tới trước đống đổ nát của chiếc bàn nâng thủy lực, ngước nhìn khối sinh vật khổng lồ đang nằm bẹp trên sàn.
```
</details>

<details><summary>L167</summary>

```text
HÌNH L167 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nằm sừng sững giữa sảnh đón tiếp của Phòng Cấp Cứu Tạo Hóa là một chiếc bánh kếp sinh học khổng lồ hình tròn dẹt, dài hơn 3 m và cao gần 4 m!". Bố cục: Toàn cảnh chú Cá Mặt Trăng (ocean sunfish) hoạt hình khổng lồ hình đĩa tròn dẹt màu xám bạc, không có cuống đuôi, hai vây lưng và vây phần đuôi dựng đứng dài ngoằng, nằm ngửa trên chiếc cáng cứu thương quá khổ mắt to tròn ngơ ngác khổng lồ da màu xám bạc loang lổ, thân hình tròn dẹt như chiếc đĩa bay khổng lồ nằm choán hết hai phần ba diện tích sảnh đón tiếp; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L168</summary>

```text
HÌNH L168 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đó là Cá Mặt Trăng đại dương Mola mola, loài cá có xương nặng nhất hành tinh, với cân nặng đo được tại chỗ lên tới 2 tấn tròn trĩnh!". Bố cục: bảng kẹp bệnh án y khoa khổng lồ (clipboard) kẹp trên giá đỡ kim loại, hiển thị 10 hồ sơ bệnh án hoạt hình với nhãn đơn thuốc phát sáng và sóng nhịp tim ECG màu đỏ nhấp nháy (không có chữ, không có số) bật sáng con số 2.000 kg nhấp nháy đỏ rực bên cạnh hình vẽ mô phỏng kích thước của cá mặt trăng so với một chiếc xe hơi bốn chỗ; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L169</summary>

```text
HÌNH L169 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn bộ cơ thể của nó dường như chỉ có một cái đầu khổng lồ gắn liền với 2 chiếc vây dài ngoằng dựng đứng lên trời và chỉa xuống đất!". Bố cục: Chiếc vây lưng và vây phần đuôi dài hơn một mét của cá mặt trăng dựng đứng như hai cánh buồm lớn; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ca số 6: Một chàng Vẹt Kakapo béo tròn 4,5 kg chẳng hề biết bay, vừa rơi từ trên cây cao xuống đất vì tưởng mình là đại bàng!". Bố cục: chú Vẹt Kakapo hoạt hình béo múp míp lông xanh rêu pha đốm nâu đen, mặt tròn lông tơ như chim cú mèo, mắt ngơ ngác dễ thương, hai cánh ngắn cũn cố vỗ lạch bạch trèo lên nóc tủ thuốc lông xanh rêu béo múp míp đang ngồi xoa chiếc mông tròn xoe giữa đống lông vũ rụng tơi bời; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L170</summary>

```text
HÌNH L170 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không hề có vây đuôi bình thường như các loài cá khác, phần đuôi của nó bị tiêu giảm thành một dải diềm lượn sóng ngắn ngủn nhìn như bị ai đó dùng dao cắt cụt!". Bố cục: Cận cảnh phần đuôi cụt ngủn kỳ dị của cá mặt trăng có gờ lượn sóng tròn viền quanh thân sau; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L171</summary>

```text
HÌNH L171 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bộ xương sống của nó đã tiêu giảm gần hết, chỉ còn lại đúng 16 đốt sống lưng, ít nhất trong toàn bộ thế giới các loài cá!". Bố cục: Bản chụp X-quang toàn thân cá mặt trăng cho thấy cột sống ngắn ngủn bất thường chỉ có mười sáu đốt sống thô ráp; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L172</summary>

```text
HÌNH L172 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hai chiếc vây lưng và vây phần đuôi dài ngoằng đập so le nhịp nhàng như đôi cánh chim bay lượn giữa lòng đại dương bao la!". Bố cục: Đồ họa cơ sinh học mô phỏng chuyển động đập vây của cá mặt trăng tương tự chuyển động bay lượn của loài chim cánh cụt dưới nước; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L173</summary>

```text
HÌNH L173 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và điều làm cô y tá hoảng sợ nhất chính là cái miệng của nó: Cái miệng tròn vo hình chữ O đang há hốc ra ngơ ngác, hoàn toàn không thể khép lại được!". Bố cục: Cận cảnh chiếc miệng nhỏ xíu tròn xoe như chiếc ống hút của cá mặt trăng, hai hàm răng hợp nhất thành một mỏ cứng như mỏ vẹt; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L174</summary>

```text
HÌNH L174 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đôi mắt to tròn như 2 chiếc đĩa sứ chớp chớp chậm rãi nhìn trần nhà với vẻ mặt ngơ ngác đến mức tội nghiệp!". Bố cục: Đôi mắt tròn xoe vô hồn của cá mặt trăng chớp chớp ngây thơ giữa gương mặt phẳng lì xám xịt; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L175</summary>

```text
HÌNH L175 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bác sĩ ơi, có phải nó bị tai biến mạch nước màu não làm liệt cơ hàm méo miệng rồi không? Sao cái miệng nó cứ há toang hoác ra thế kia mà không chịu ngậm lại?". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng run rẩy cầm chiếc đèn pin y tế soi vào trong khoang miệng cá mặt trăng, vẻ mặt đầy bối rối lo âu; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L176</summary>

```text
HÌNH L176 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không hề có tai biến hay liệt cơ nào ở đây cả cô y tá thân mến! Đó là cấu trúc hàm hợp nhất tự nhiên của bộ cá nóc mà loài cá này thuộc về!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười giải thích, đưa tay sờ vào lớp da dày cộp xù xì như giấy ráp của bệnh nhân khổng lồ.
```
</details>

<details><summary>L177</summary>

```text
HÌNH L177 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Răng của nó đã tiêu biến và hợp nhất lại thành một chiếc mỏ sừng sắc bén, dùng để hút và nghiền nát những con sứa biển trơn tuột dưới đại dương sâu thẳm!". Bố cục: Hình ảnh mô phỏng bộ hàm hợp nhất hình chiếc mỏ chim của cá mặt trăng đang hút trọn một đàn sứa phát sáng dưới làn nước biển xanh thẳm; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L178</summary>

```text
HÌNH L178 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thức ăn ưa thích của nó là các loài động vật thân mềm bồng bềnh chứa tới 95% là nước và cực kỳ ít calo, khiến con vật phải ăn liên tục suốt ngày đêm!". Bố cục: Đồ họa chuỗi thức ăn hiển thị hàng trăm con sứa trong suốt bị hút gọn vào khoang miệng cá mặt trăng; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L179</summary>

```text
HÌNH L179 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lớp sụn xơ dày cộp bao bọc quanh người hoạt động như một lớp đệm hấp thu xung lực va đập tự nhiên, giúp nó an toàn trước các đợt sóng biển dữ dội!". Bố cục: Bản vẽ mô phỏng các sợi collagen đan chéo dày đặc trong lớp da tạo nên một tấm áo giáp sinh học đàn hồi tuyệt hảo; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ca số 7: Một chú Lợn Hươu Babirusa với 4 chiếc răng nanh cong vút dị thường đang có nguy cơ tự đâm thủng hộp sọ của chính mình!". Bố cục: chú Lợn Hươu Babirusa hoạt hình da xám nhăn nheo ít lông, mõm dài, bốn chiếc răng nanh cong vút dị thường trong đó hai nanh trên mọc xuyên qua sống mũi uốn ngược về phía trán, vẻ mặt lo lắng sờ trán với cặp nanh trên mọc ngược xuyên qua sống mũi uốn cong sát trán, vẻ mặt đầy bối rối lo âu; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L180</summary>

```text
HÌNH L180 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng điều làm tôi lo ngại nhất lúc này không phải là chiếc miệng, mà là áp lực trọng lực đang đè nén lên các cơ quan bên trong cơ thể của con vật!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án áp ống nghe vào lớp da dày cộp của con cá, lắng nghe nhịp tim đập chậm rãi của khối cơ thể hai tấn.
```
</details>

<details><summary>L181</summary>

```text
HÌNH L181 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dưới đáy đại dương, lực đẩy Ác-si-mét nâng đỡ toàn bộ khối cơ thể 2 tấn này một cách nhẹ nhàng êm ái.". Bố cục: Bức tranh miêu tả cá mặt trăng đang bơi lội thanh thoát giữa đại dương bao la, ánh nắng mặt trời chiếu xuyên qua làn nước trong vắt; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L182</summary>

```text
HÌNH L182 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng khi bị đưa lên cạn, trọng lượng khổng lồ sẽ ép bẹp các mạch nước màu và làm suy hô hấp nghiêm trọng nếu không được giải phóng kịp thời!". Bố cục: Đồ họa y học hiển thị áp lực cơ học đè nặng lên các cơ quan bên trong cơ thể bên trong khi cá mặt trăng nằm trên mặt phẳng cứng; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L183</summary>

```text
HÌNH L183 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hơn nữa, trên lớp da dày tới 7,5 cm bằng sụn xơ của nó đang có hơn 4 mươi loài ký sinh trùng khác nhau đang bám dính dày đặc như một viện bảo tàng ký sinh trùng sống!". Bố cục: Kính lúp y khoa soi bề mặt da cá mặt trăng với hàng chục loài ký sinh trùng giáp xác và giun dẹp bám chặt vào lớp biểu bì; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L184</summary>

```text
HÌNH L184 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bác sĩ trưởng khoa ơi, da nó dày cứng như lốp xe tải thế này thì kim tiêm nào đâm cho thủng được ạ?". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng cầm chiếc kim tiêm chuyên dụng ấn thử vào da cá nhưng mũi kim bị uốn cong queo không thể xuyên qua lớp sụn xơ dày cộp.
```
</details>

<details><summary>L185</summary>

```text
HÌNH L185 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chúng ta phải làm sao để cứu anh chàng khổng lồ ngơ ngác này bây giờ bác sĩ ơi?". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng lo lắng nhìn khối thịt hai tấn đang thở phì phò trên sàn sảnh đón tiếp; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L186</summary>

```text
HÌNH L186 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhìn vẻ mặt ngơ ngác vô tội của nó giữa sảnh bệnh viện mà tôi vừa buồn cười vừa xót xa cho sinh vật đại dương này!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án lắc đầu thở dài, cúi xuống nhìn đôi mắt tròn xoe phẳng lặng không chút sát khí của chú cá mặt trăng.
```
</details>

<details><summary>L187</summary>

```text
HÌNH L187 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong lịch sử hàng hải cổ đại, các thủy thủ từng lầm tưởng chiếc vây lưng nhô cao của cá mặt trăng là thủy quái kraken khổng lồ!". Bố cục: Bức tranh khắc gỗ thời Phục hưng vẽ cảnh con tàu buồm cổ đối mặt với chiếc vây lưng nhô cao của cá mặt trăng giữa sóng gió biển khơi; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L188</summary>

```text
HÌNH L188 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thế nhưng thực tế nó lại là sinh vật hiền lành và ngờ nghệch bậc nhất đại dương, thậm chí để mặc cho hải cẩu và cá kình rỉa vây mà chẳng hề buồn chống cự!". Bố cục: Chú hải cẩu nghịch ngợm bơi quanh chú cá mặt trăng đang trôi lơ lửng, chú cá chẳng hề có phản ứng né tránh nào; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L189</summary>

```text
HÌNH L189 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đã có những trường hợp cá mặt trăng trôi dạt vào bãi tắm làm cả bờ biển náo loạn vì tưởng quái vật ngoài hành tinh đổ bộ!". Bố cục: Cảnh người dân trên bãi biển tụ tập vây quanh khối thịt tròn dẹt khổng lồ với vẻ kinh ngạc tò mò; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ca số 8: Một quý cô Hươu Cao Cổ cao 5 m đang choáng váng ngất xỉu với chỉ số huyết áp tâm thu vọt lên ngưỡng gần 300 mmHg!". Bố cục: chú Hươu Cao Cổ hoạt hình cao lêu nghêu có đốm hoa văn nâu vàng, chiếc cổ dài thẳng tắp quấn dải băng đo huyết áp y tế to bản màu đỏ, mắt to hiền từ chớp chớp gục chiếc cổ dài hai mét lên thành quầy tiếp nhận bệnh nhân, mắt hoa lên nhìn những vòng tròn xoay tít; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L190</summary>

```text
HÌNH L190 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đội cứu hộ khẩn cấp nghe lệnh tôi! Lập tức điều động chiếc xe cẩu chuyên dụng 10 tấn và dây đai bạt cứu hộ vào sảnh đón tiếp ngay lập tức!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án cầm bộ đàm ra lệnh dõng dạc, ánh mắt quyết đoán và bình tĩnh điều phối toàn bộ hiện trường cấp cứu.
```
</details>

<details><summary>L191</summary>

```text
HÌNH L191 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chúng ta không thể khám bệnh cho khối thịt 2 tấn này trên sàn nhà cứng ngắc này được!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án chỉ huy đội bảo vệ căng các tấm đệm hơi cao su quanh thân cá mặt trăng để giảm áp lực tì đè cơ học.
```
</details>

<details><summary>L192</summary>

```text
HÌNH L192 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mở van nước xả đầy chiếc bể ngâm nước muối sinh lý dung tích 50 m³ ở Khoa Hồi Sức Cấp Cứu Đại Dương!". Bố cục: Chiếc bể bơi y tế khổng lồ lát gạch xanh ngọc bích bắt đầu được bơm đầy nước muối biển nhân tạo có hệ thống sục khí oxy cực mạnh; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L193</summary>

```text
HÌNH L193 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dùng dây đai bạt luồn nhẹ nhàng dưới bụng cá mặt trăng, cẩu bổng anh chàng lên và chuyển thẳng vào bể hồi sức ngay trong 15 phút tới!". Bố cục: Chiếc cần cẩu y tế màu vàng từ từ hạ móc cáp thép xuống, các điều dưỡng viên cẩn thận luồn những dải đai bạt mềm mại quanh thân cá mặt trăng; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L194</summary>

```text
HÌNH L194 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một, 2, 3, nâng! Dưới sự điều khiển nhịp nhàng của kíp trực, khối sinh vật 2 tấn từ từ được nhấc bổng lên không trung trong sự reo hò thán phục của toàn thể bệnh nhân trong sảnh!". Bố cục: Khối cơ thể khổng lồ của chú Cá Mặt Trăng (ocean sunfish) hoạt hình khổng lồ hình đĩa tròn dẹt màu xám bạc, không có cuống đuôi, hai vây lưng và vây phần đuôi dựng đứng dài ngoằng, nằm ngửa trên chiếc cáng cứu thương quá khổ mắt to tròn ngơ ngác lơ lửng trên không trung giữa sảnh bệnh viện, đôi mắt tròn xoe ngơ ngác nhìn đám đông bên dưới chớp chớp như đang đi du lịch; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L195</summary>

```text
HÌNH L195 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sàn sảnh đón tiếp tạm thời được giải tỏa an toàn! Nhưng đừng vội mừng, vì ngay cạnh phòng mổ số 2, tiếng kêu thất thanh của một chú gián đang báo hiệu ca phẫu thuật thần kinh dị thường nhất trần đời vừa bắt đầu!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án lau mồ hôi trên trán, rảo bước chạy vội về phía phòng phẫu thuật thần kinh nơi có ánh đèn huỳnh quang màu xanh ngọc bích đang chiếu sáng.
```
</details>

<details><summary>L196</summary>

```text
HÌNH L196 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cánh cửa phòng mổ thần kinh số 2 mở ra trong một bầu không khí lạnh ngắt và tĩnh lặng đến gai người.". Bố cục: Căn phòng mổ vô trùng sáng choang ánh đèn phẫu thuật, các khay dao mổ siêu vi sáng loáng xếp hàng ngay ngắn trên bàn inox; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L197</summary>

```text
HÌNH L197 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trên bàn mổ chính bọc khăn vải xanh vô trùng, một cảnh tượng rùng rợn và kỳ quái làm bất kỳ ai chứng kiến cũng phải sởn gai ốc từ đầu đến chân!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đeo kính hiển vi phẫu thuật phóng đại, cúi nhìn chăm chú vào bàn mổ; cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng đứng nép một góc run rẩy ôm chặt tập hồ sơ bệnh án.
```
</details>

<details><summary>L198</summary>

```text
HÌNH L198 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một chú gián Mỹ khổng lồ dài 5 cm, to gấp 6 lần một con ong, đang đứng im phăng phắc như một pho tượng gỗ vô hồn!". Bố cục: Một chú gián Mỹ màu nâu cánh gián to lớn đứng bất động trên tấm khăn mổ vô trùng, hai sợi râu dài buông thõng rũ rượi; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L199</summary>

```text
HÌNH L199 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hai chiếc râu dài của nó bị cắt cụt một nửa, đôi mắt kép đờ đẫn mất hoàn toàn phản xạ trốn chạy hay phòng vệ tự nhiên!". Bố cục: Cận cảnh đôi mắt kép màu đen đục vô hồn của chú gián, hoàn toàn không có bất kỳ phản xạ giật mình nào khi có bóng người lướt qua; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ca số 9: Một chú Nhím Lông Nhọn Bắc Mỹ vừa ngã từ cây thông xuống đất và tự cắm hàng trăm chiếc gai sắc nhọn vào đùi của chính mình!". Bố cục: chú Nhím Lông Nhọn Bắc Mỹ hoạt hình béo tròn xù xì, toàn thân phủ kín ba mươi ngàn chiếc gai nhọn trắng đen, đang ôm chặt một thân cây gỗ gặm vỏ thuốc, người tỏa mùi tinh dầu thơm nhẹ xù lông gai lởm chởm, một bên chân ngắn cũn cắm đầy những mảnh gai gãy nhăn nhó gãi đầu; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L200</summary>

```text
HÌNH L200 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và đứng kiêu hãnh trên lưng chú gián khổng lồ là bệnh nhân số 5 của chúng ta: Cô Ong Bắp Cày Ngọc Ampulex compressa!". Bố cục: cô Ong Bắp Cày Ngọc (emerald cockroach wasp) hoạt hình thân thon dài phát sáng xanh ngọc bích kim loại lộng lẫy, chân dài thanh mảnh, tay cầm chiếc dao mổ phẫu thuật thần kinh siêu nhỏ giơ lên đầy tự tin toàn thân phát sáng màu xanh ngọc bích ánh kim lộng lẫy như một viên đá quý, sải chân dài thanh mảnh kiêu hãnh đứng trên lưng chú gián; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L201</summary>

```text
HÌNH L201 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cô ong đang dùng chiếc vòi miệng tí hon của mình bình thản gặm nhấm vết cắt ở râu chú gián để hút dịch bạch huyết như đang thưởng thức một ly nước ngọt giải khát!". Bố cục: Cận cảnh vòi miệng của ong bắp cày ngọc đang hút giọt dịch bạch huyết màu trắng trong suốt rỉ ra từ gốc râu chú gián; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L202</summary>

```text
HÌNH L202 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bác sĩ trưởng khoa ơi cứu em với! Con ong xanh lấp lánh kia nó vừa làm phép phù thủy biến con gián thành thây ma sống kìa!". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng hai tay ôm mặt run lẩy bẩy, chỉ ngón tay vào chú gián to lớn đang đứng ngoan ngoãn như một chú cún con.
```
</details>

<details><summary>L203</summary>

```text
HÌNH L203 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Con gián to gấp 6 lần con ong, chân cẳng khỏe như lực sĩ mà sao nó không thèm đá văng con ong ra để chạy trốn hả bác sĩ?". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng ngạc nhiên tột cùng nhìn chú gián to lớn hoàn toàn đủ sức đè bẹp chú ong nhỏ bé nhưng lại đứng im chịu trận; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L204</summary>

```text
HÌNH L204 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Có phải con ong này biết thuật thôi miên tà đạo hay dùng bùa ngải gì không bác sĩ ơi?". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng ngước nhìn bác sĩ với ánh mắt đầy khiếp hãi và tò mò cao độ; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L205</summary>

```text
HÌNH L205 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không hề có bùa ngải hay phép thuật phù thủy nào ở đây cả cô y tá thân mến!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười chỉnh lại độ nét của chiếc kính hiển vi phẫu thuật, say mê quan sát từng chi tiết giải phẫu tinh vi của cô ong ngọc bích.
```
</details>

<details><summary>L206</summary>

```text
HÌNH L206 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây chính là nữ phẫu thuật viên thần kinh lỗi lạc và tàn nhẫn nhất trong toàn bộ lịch sử tiến hóa của giới côn trùng!". Bố cục: cô Ong Bắp Cày Ngọc (emerald cockroach wasp) hoạt hình thân thon dài phát sáng xanh ngọc bích kim loại lộng lẫy, chân dài thanh mảnh, tay cầm chiếc dao mổ phẫu thuật thần kinh siêu nhỏ giơ lên đầy tự tin vươn đôi cánh mỏng trong suốt màu khói, ánh xanh lục bảo lấp lánh phản chiếu rực rỡ dưới ánh đèn mổ phẫu thuật; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L207</summary>

```text
HÌNH L207 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Loài ong bắp cày ngọc này không hề chiến thắng con gián, mà nó thực hiện một ca phẫu thuật não bộ 2 giai đoạn với độ chính xác cơ học vượt xa tay nghề của các giáo sư ngoại thần kinh hàng đầu loài người!". Bố cục: Sơ đồ giải phẫu hệ thần kinh của gián với các hạch thần kinh ngực và hạch thần kinh dưới thực quản phát sáng dưới tia tử ngoại; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L208</summary>

```text
HÌNH L208 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy nhìn vào quy trình 2 mũi tiêm thần kinh chết người mà nghiên cứu kinh điển của giáo sư Libersat công bố trên Tạp Chí Sinh Học Thực Nghiệm đã giải mã!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án giơ bản đồ giải phẫu thần kinh côn trùng lên trước ánh đèn, chỉ vào từng vị trí đâm kim chính xác đến từng mi-crô-mét.
```
</details>

<details><summary>L209</summary>

```text
HÌNH L209 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mũi tiêm thứ nhất: Khi bắt gặp con gián, ong bắp cày lao tới vật ngửa con mồi ra và cắm ngập chiếc ngòi sắc bén vào hạch thần kinh ngực đầu tiên của con gián!". Bố cục: Hình ảnh mô phỏng ong bắp cày dùng hàm kẹp chặt gián, uốn cong bụng cắm chiếc ngòi nhọn hoắt vào phần ngực dưới của con mồi; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và ca số 10: Một pho tượng đá sống mang tên Cò Mỏ Giày đứng bất động 5 tiếng đồng hồ không thèm chớp mắt giữa sảnh chờ!". Bố cục: chú Cò Mỏ Giày hoạt hình lông xám tro, dáng đứng sừng sững bất động như tượng đá, chiếc mỏ khổng lồ màu vàng xám phình to hình chiếc guốc gỗ, ánh mắt lạnh như tiền đứng canh cửa phòng cấp cứu đứng sừng sững như tượng đá xám giữa sảnh bệnh viện, chiếc mỏ guốc khổng lồ chúc xuống góc bốn mươi lăm độ đầy ma mị; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L210</summary>

```text
HÌNH L210 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mũi tiêm đầu tiên này chứa một lượng lớn chất dẫn truyền thần kinh ức chế GABA và các chất làm tê liệt cơ bắp tạm thời.". Bố cục: Đồ họa hóa học hiển thị các phân tử nọc độc khóa chặt các thụ thể thần kinh vận động ở hai chân trước của con gián; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L211</summary>

```text
HÌNH L211 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong đúng 2 phút đồng hồ, 2 chân trước của con gián bị tê liệt hoàn toàn, khiến nó không thể giơ chân lên gạt đòn hay phản kháng được nữa!". Bố cục: Con gián giãy giụa bất lực khi hai chân trước rũ liệt hoàn toàn, tạo điều kiện thuận lợi tuyệt đối cho mũi tiêm quyết định thứ hai; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L212</summary>

```text
HÌNH L212 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và đây mới là đỉnh cao giải phẫu học làm rung chuyển giới y khoa: Mũi tiêm thứ 2 xuyên thẳng qua lớp vỏ kitin cứng ở cổ, chọc sâu vào tận hạch thần kinh dưới thực quản bên trong não bộ con gián!". Bố cục: Đồ họa cắt lớp hiển thị chiếc ngòi ong uốn lượn luồn lách qua các mô mềm ở cổ gián, đâm chính xác tuyệt đối vào hạch não điều khiển hành vi; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L213</summary>

```text
HÌNH L213 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiếc ngòi của ong được trang bị các cơ quan thụ cảm cơ học và hóa học siêu nhỏ, cho phép nó cảm nhận và định vị chính xác hạch não trong bóng tối tăm mù mịt bên trong hộp sọ con mồi!". Bố cục: Đầu ngòi ong phóng đại hiển thị các sợi cảm biến nano đang dò tìm tín hiệu hóa học của mô não gián với độ sai lệch bằng không; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L214</summary>

```text
HÌNH L214 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nọc độc của mũi tiêm thứ 2 là một ly cocktail hóa sinh phức tạp bậc nhất tự nhiên, chứa các chất ức chế thụ thể dopamine và octopamine chuyên biệt!". Bố cục: Các phân tử độc tố màu đỏ thẫm len lỏi phong tỏa hoàn toàn các thụ thể dopamine trong trung khu điều khiển vận động chủ động của não gián; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L215</summary>

```text
HÌNH L215 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chất octopamine là chất kích hoạt phản xạ trốn chạy khi gặp nguy hiểm ở loài côn trùng.". Bố cục: Đồ họa thần kinh hiển thị đường dẫn truyền tín hiệu phản xạ trốn chạy của gián bị cắt đứt hoàn toàn như sợi dây điện bị ngắt cầu dao; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L216</summary>

```text
HÌNH L216 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi bị nọc độc khóa chặt thụ thể này, con gián hoàn toàn mất đi ý chí sinh tồn và phản xạ tự vệ, biến thành một thây ma sống đúng nghĩa đen!". Bố cục: Cận cảnh chú gián đứng im như pho tượng, dù có tiếng động lớn hay bị chạm vào người cũng không hề buồn nhúc nhích; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L217</summary>

```text
HÌNH L217 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chú gián vẫn thở bình thường, tim vẫn đập, chân cẳng vẫn hoạt động tốt, nhưng động lực tự bước đi để cứu lấy bản thân đã bị xóa sổ 100%!". Bố cục: Đồ họa sinh lý học hiển thị các chức năng sống cơ bản của gián duy trì bình thường nhưng mất hoàn toàn khả năng tự chủ vận động; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L218</summary>

```text
HÌNH L218 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sau đó, cô ong cắt bớt 2 chiếc râu dài của gián để uống dịch bạch huyết bù đắp năng lượng tiêu hao sau trận đấu vật căng thẳng!". Bố cục: Cô ong dùng đôi hàm sắc như kéo cắt đứt ngọt ngào hai sợi râu của chú gián trước sự sững sờ của các bác sĩ; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L219</summary>

```text
HÌNH L219 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Rồi cô ong ngậm lấy phần gốc râu còn lại, dắt con gián to lớn lững thững đi theo mình về chiếc tổ ngầm dưới lòng đất như dắt một chú cún ngoan ngoãn đi dạo phố!". Bố cục: Bức tranh miêu tả cô cô Ong Bắp Cày Ngọc (emerald cockroach wasp) hoạt hình thân thon dài phát sáng xanh ngọc bích kim loại lộng lẫy, chân dài thanh mảnh, tay cầm chiếc dao mổ phẫu thuật thần kinh siêu nhỏ giơ lên đầy tự tin nhỏ bé ngậm râu dắt chú gián khổng lồ ngoan ngoãn bước từng bước theo sau đi vào chiếc hang tối; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trời đất ơi! Nhìn vào bảng tiếp nhận này thì đây không phải là một bệnh viện thông thường nữa, mà là một viện bảo tàng giải phẫu học kỳ dị nhất vũ trụ!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án bật cười thành tiếng, lắc đầu thán phục trước danh sách bệnh nhân vô tiền khoáng hậu đang hiện diện trước mắt.
```
</details>

<details><summary>L220</summary>

```text
HÌNH L220 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tại chiếc tổ đó, ong sẽ đẻ một quả trứng duy nhất lên bụng con gián, niêm phong cửa hang lại bằng đất đá.". Bố cục: Ấu trùng ong bắp cày màu trắng ngà phát triển bên cạnh chú gián sống trong chiếc tổ ngầm kiên cố; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L221</summary>

```text
HÌNH L221 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sau khi đẻ trứng xong, cô ong mẹ còn tỉ mỉ nhặt từng viên sỏi nhỏ và cành cây khô che phủ kín miệng hang để ngụy trang tuyệt đối trước các loài săn mồi khác!". Bố cục: Chú cô Ong Bắp Cày Ngọc (emerald cockroach wasp) hoạt hình thân thon dài phát sáng xanh ngọc bích kim loại lộng lẫy, chân dài thanh mảnh, tay cầm chiếc dao mổ phẫu thuật thần kinh siêu nhỏ giơ lên đầy tự tin cần mẫn gắp từng hạt cát hạt sỏi nhỏ lấp kín lối vào căn hầm ngầm bí mật; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L222</summary>

```text
HÌNH L222 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Con gián sống thực vật này đóng vai trò như một kho thực phẩm tươi sống hoàn hảo, nuôi dưỡng ấu trùng ong lớn lên cho tới ngày lột xác bay ra ngoài!". Bố cục: Ấu trùng ong bọc kén tơ mỏng, chuẩn bị cho quá trình biến thái hoàn toàn dưới lòng đất ẩm ướt; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L223</summary>

```text
HÌNH L223 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cơ quan thị giác và xúc giác ở chân của cô ong bắp cày ngọc tinh vi đến mức có thể nếm được mùi vị dịch mô của con mồi qua lớp lông cảm ứng!". Bố cục: Kính hiển vi điện tử quét hiển thị các thụ thể hóa học hình nón li ti trên các đốt bàn chân của ong bắp cày ngọc; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L224</summary>

```text
HÌNH L224 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bằng cách cọ nhẹ bàn chân lên đầu chú gián, cô ong có thể đo đạc chính xác nồng độ độc tố thần kinh còn tồn đọng trong mô não con mồi!". Bố cục: Đồ họa hóa sinh hiển thị các tín hiệu điện sinh học từ thụ thể chân ong truyền về hạch thần kinh trung ương xử lý dữ liệu; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L225</summary>

```text
HÌNH L225 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu liều lượng thuốc tê quá nhẹ, con gián có thể hồi phục phản xạ và đá văng quả trứng của ong ra khỏi bụng!". Bố cục: Hình ảnh mô phỏng chú gián giật mình đá mạnh chân sau nếu không bị phong tỏa thần kinh hoàn toàn; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L226</summary>

```text
HÌNH L226 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng nếu liều lượng quá mạnh, con gián sẽ chết ngay lập tức và phân hủy thối rữa trước khi ấu trùng ong kịp nở ra để thưởng thức thịt tươi!". Bố cục: Đồ họa sinh học đối chiếu mức liều lượng nọc độc chuẩn xác đến từng nano gam giúp con mồi sống thực vật hoàn hảo; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L227</summary>

```text
HÌNH L227 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Độ chuẩn xác tuyệt đối đến từng nano gam nọc độc này là một kiệt tác vi sinh hóa học mà loài người còn lâu mới bắt kịp!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án nghiêng đầu thán phục nhìn chiếc ngòi ong thép thu gọn tinh xảo bên dưới lớp giáp ngọc bích.
```
</details>

<details><summary>L228</summary>

```text
HÌNH L228 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đó là sự tàn nhẫn lạnh lùng nhưng cũng là sự tinh vi cơ học tuyệt đối của tự nhiên: Giữ cho con mồi sống tươi nguyên suốt nhiều tuần lễ mà không cần tủ lạnh bảo quản!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án thở dài thán phục, gật đầu công nhận sự hoàn mỹ của cơ chế ký sinh thần kinh độc nhất vô nhị này.
```
</details>

<details><summary>L229</summary>

```text
HÌNH L229 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cô ong của chúng ta hôm nay nhập viện không phải vì bị bệnh, mà vì vô tình bay lạc vào phòng mổ bệnh viện qua lỗ thông gió trong khi đang dẫn giải con gián đi tìm tổ!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười nhìn cô ong ngọc bích đang nghiêng đầu làm duyên trên lưng chú gián.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bác sĩ trưởng khoa đã từng thấy ca trực nào mà toàn bộ sách giáo khoa giải phẫu kinh điển đều phải xé bỏ viết lại từ đầu như đêm nay chưa?". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng đưa tay lên trán thở dài thườn thượt, gương mặt thỏ trắng lộ rõ vẻ mệt mỏi nhưng cũng đầy hồi hộp chờ đợi; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L230</summary>

```text
HÌNH L230 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn bộ hệ thống ngòi tiêm và tuyến nọc độc của cô nàng hoạt động hoàn hảo tuyệt đối không tì vết, phản xạ vận động đạt điểm 10 trên 10!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án dùng kính hiển vi soi kỹ phần bụng dưới của cô Ong Bắp Cày Ngọc (emerald cockroach wasp) hoạt hình thân thon dài phát sáng xanh ngọc bích kim loại lộng lẫy, chân dài thanh mảnh, tay cầm chiếc dao mổ phẫu thuật thần kinh siêu nhỏ giơ lên đầy tự tin, nơi chiếc ngòi thép thu gọn an toàn bên trong bao trùm kitin sáng bóng.
```
</details>

<details><summary>L231</summary>

```text
HÌNH L231 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà dược lý học hiện đại đang nghiên cứu công thức nọc độc của ong bắp cày ngọc để điều chế các loại thuốc gây mê thần kinh thế hệ mới không gây nghiện!". Bố cục: Mô hình phân tử hóa học của các hợp chất giảm đau thế hệ mới lấy cảm hứng từ nọc ong ngọc bích phát sáng trên màn hình máy tính; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L232</summary>

```text
HÌNH L232 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thôi được rồi cô nàng phẫu thuật viên tí hon lộng lẫy ơi! Phòng mổ của tôi là nơi cứu người chứ không phải nơi cô mở lò đào tạo thây ma gián nhé!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án bật cười lắc đầu, dùng một chiếc hộp mica trong suốt chuyên dụng nhẹ nhàng chụp lấy cả cô ong lẫn chú gián.
```
</details>

<details><summary>L233</summary>

```text
HÌNH L233 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chúng tôi sẽ chuyển cả 2 bạn sang Viện Nghiên Cứu Côn Trùng Học Quốc Gia để các nhà thần kinh học tiếp tục học hỏi công thức chế tạo thuốc tê thần kinh từ cô nàng nhé!". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng cẩn thận dán nhãn chuyển viện lên chiếc hộp mica, thở phào nhẹ nhõm khi tiễn được ca bệnh thần kinh rùng rợn này ra khỏi phòng mổ.
```
</details>

<details><summary>L234</summary>

```text
HÌNH L234 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hồ sơ Khoa Phẫu Thuật Não hoàn tất xuất sắc! Giờ thì nghe kìa, tiếng máy bơm nước từ Khoa Hồi Sức Đại Dương báo hiệu bể ngâm cá mặt trăng 2 tấn đã sẵn sàng! Toàn đội chạy nhanh nào!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án cởi áo choàng phẫu thuật, chạy vội về phía khu hồi sức cấp cứu đại dương.
```
</details>

<details><summary>L235</summary>

```text
HÌNH L235 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ùng oàng! Bùm! Khối cơ thể khổng lồ 2 tấn của chú Cá Mặt Trăng Mola mola được cần cẩu hạ cánh an toàn xuống bể ngâm nước muối sinh lý dung tích 50 m³!". Bố cục: Sóng nước màu xanh ngọc bích bắn tung tóe lên thành bể kính dày mười phân, bọt khí sủi tăm trắng xóa bao bọc quanh thân hình tròn dẹt khổng lồ của chú Cá Mặt Trăng (ocean sunfish) hoạt hình khổng lồ hình đĩa tròn dẹt màu xám bạc, không có cuống đuôi, hai vây lưng và vây phần đuôi dựng đứng dài ngoằng, nằm ngửa trên chiếc cáng cứu thương quá khổ mắt to tròn ngơ ngác; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L236</summary>

```text
HÌNH L236 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lực đẩy Ác-si-mét của dòng nước mặn lập tức nâng bổng khối cơ thể nặng ngàn cân lên một cách nhẹ nhàng như một chiếc lá trôi bồng bềnh.". Bố cục: Khối cơ thể hai tấn trôi lơ lửng nhẹ nhàng giữa làn nước trong suốt, các áp lực cơ học đè nặng lên tim phổi được giải phóng hoàn toàn; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L237</summary>

```text
HÌNH L237 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các đường ống sục khí oxy công suất lớn sủi bọt cuồn cuộn quanh các lá mang của chú cá, cung cấp nguồn dưỡng khí dồi dào tức thì.". Bố cục: Hệ thống ống dẫn oxy sục bọt trắng xóa quanh hai nắp mang nhỏ xíu của cá mặt trăng, chú cá bắt đầu thở phập phồng nhịp nhàng; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L238</summary>

```text
HÌNH L238 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôi cùng kíp trực Khoa Hồi Sức Cấp Cứu Đại Dương bước lên cầu quan sát bằng kính chịu lực bắc ngang qua mặt bể để tiến hành thăm khám toàn diện.". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đứng trên cầu kính quan sát, tay cầm bảng ghi chép chỉ số sinh tồn; cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng cầm chiếc máy đo nồng độ muối và nhiệt độ nước theo dõi sát sao.
```
</details>

<details><summary>L239</summary>

```text
HÌNH L239 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhịp tim của chú cá qua máy theo dõi điện tâm đồ thủy sinh dao động ở mức 30 nhịp mỗi phút, vô cùng ổn định và đều đặn!". Bố cục: Màn hình điện tâm đồ nhấp nháy những đường sóng P-Q-R-S màu xanh lá cây hiển thị nhịp tim ba mươi lần một phút nhịp nhàng; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa từng có một tiền lệ nào tương tự trong suốt 3 thập kỷ làm nghề y của tôi cả cô y tá thân mến ạ!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười đôn hậu, bước tới tủ thuốc lấy ra chiếc áo choàng phẫu thuật màu xanh ngọc bích quen thuộc.
```
</details>

<details><summary>L240</summary>

```text
HÌNH L240 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bác sĩ trưởng khoa ơi em vừa chạy xong bản quét cộng hưởng từ MRI toàn thân cho khối thịt 2 tấn này!". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng giơ tập phim chụp cộng hưởng từ MRI kích thước khổng lồ lên trước màn hình rọi sáng, vẻ mặt đầy bàng hoàng không tin vào mắt mình.
```
</details>

<details><summary>L241</summary>

```text
HÌNH L241 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Em tìm mỏi cả mắt mà không thấy bóng hơi hay bong bóng cá ở đâu cả bác sĩ ơi!". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng chỉ tay vào khoảng trống rỗng nơi đáng lẽ phải có bóng khí bơi lội của các loài cá thông thường; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L242</summary>

```text
HÌNH L242 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và đây nữa nè: Hộp sọ của nó to bằng chiếc thùng phi 10 lít, nhưng bộ não bên trong của nó... trời đất ơi, nó chỉ nhỏ bằng hạt đậu phộng thôi bác sĩ ơi! Có phải máy quét MRI của em bị lỗi kỹ thuật không ạ?". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng mở to mắt chỉ vào chấm nhỏ xíu phát sáng màu cam nằm cô độc giữa khoang sọ khổng lồ của cá mặt trăng; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L243</summary>

```text
HÌNH L243 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Máy quét của cô hoàn toàn chính xác 100% không hề có một lỗi kỹ thuật nào cô y tá thân mến!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án bật cười giơ tấm phim chụp lên trước ánh sáng đèn soi, chỉ vào cấu trúc sọ não kỳ lạ của chú cá.
```
</details>

<details><summary>L244</summary>

```text
HÌNH L244 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chào mừng toàn thể kíp trực đến với nghịch lý giải phẫu vĩ đại nhất của đại dương bao la: Bệnh nhân sở hữu tỷ lệ não bộ trên trọng lượng cơ thể nhỏ nhất trong toàn bộ giới động vật có xương sống!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án chỉ đầu bút vào điểm sáng li ti của bộ não trên phim chụp MRI.
```
</details>

<details><summary>L245</summary>

```text
HÌNH L245 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một con cá mặt trăng trưởng thành nặng tới 2 tấn tròn trĩnh, nhưng toàn bộ khối lượng bộ não của nó chỉ vỏn vẹn đúng... 4 g!". Bố cục: bảng kẹp bệnh án y khoa khổng lồ (clipboard) kẹp trên giá đỡ kim loại, hiển thị 10 hồ sơ bệnh án hoạt hình với nhãn đơn thuốc phát sáng và sóng nhịp tim ECG màu đỏ nhấp nháy (không có chữ, không có số) bật sáng con số 4 gam bên cạnh con số 2.000 kg với dấu chấm than đỏ chót biểu thị tỷ lệ một phần năm trăm ngàn không tưởng; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L246</summary>

```text
HÌNH L246 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nghĩa là bộ não của nó chỉ chiếm 1/500.000 tổng trọng lượng cơ thể! Nhỏ hơn cả bộ não của một con mèo con hay một chú chuột nhắt tí hon!". Bố cục: Hình ảnh so sánh hạt đậu phộng nhỏ xíu đặt cạnh khối thịt hai tấn đồ sộ của cá mặt trăng; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L247</summary>

```text
HÌNH L247 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thế nhưng với bộ não 4 g đó, nó vẫn điều khiển thành công cỗ máy sinh học 2 tấn vượt qua hàng ngàn hải lý đại dương suốt hàng chục 5 ròng rã!". Bố cục: Bản đồ vệ tinh hiển thị lộ trình di cư xuyên đại dương hàng chục ngàn cây số của các chú cá mặt trăng gắn máy định vị vệ tinh; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L248</summary>

```text
HÌNH L248 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và tại sao nó lại không hề có bóng hơi để bơi lội như các loài cá thông thường?". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đặt câu hỏi đầy hào hứng nhìn về phía các bác sĩ nội trú đang chăm chú lắng nghe từng lời phân tích.
```
</details>

<details><summary>L249</summary>

```text
HÌNH L249 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bởi vì môi trường kiếm ăn chính của cá mặt trăng là vùng nước sâu tăm tối twilight zone ở độ sâu từ 400 đến tận 800 m dưới đáy biển!". Bố cục: Bức tranh miêu tả vùng biển sâu thăm thẳm lạnh ngắt tăm tối nơi ánh sáng mặt trời không thể chiếu tới, chú chú Cá Mặt Trăng (ocean sunfish) hoạt hình khổng lồ hình đĩa tròn dẹt màu xám bạc, không có cuống đuôi, hai vây lưng và vây phần đuôi dựng đứng dài ngoằng, nằm ngửa trên chiếc cáng cứu thương quá khổ mắt to tròn ngơ ngác đang bơi lội kiếm ăn giữa đàn sứa phát sáng; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi sinh vật đang nằm ngoài kia là một bài toán hóc búa, một nghịch lý cơ thể học thách thức mọi định luật sinh học mà con người từng biết đến!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án khoác chiếc áo blouse trắng tinh tươm, đeo găng tay cao su vô trùng và chỉnh lại chiếc ống nghe trên cổ.
```
</details>

<details><summary>L250</summary>

```text
HÌNH L250 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở độ sâu 800 m, áp suất nước biển lên tới 80 atm, thừa sức bóp bẹp rúm bất kỳ chiếc bóng hơi nào trong chớp mắt!". Bố cục: Hình ảnh mô phỏng quả bóng hơi bằng cao su bị áp lực nước sâu bóp nát vụn thành mảnh vụn nhỏ; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L251</summary>

```text
HÌNH L251 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu có bóng hơi, cá mặt trăng sẽ không thể lao nhanh từ độ sâu 800 m lên mặt nước mà không bị vỡ bên trong cơ thể do giảm áp đột ngột!". Bố cục: Sơ đồ y học hiển thị hiện tượng thuyên tắc khí nguy hiểm nếu động vật có bóng hơi nổi lên quá nhanh từ đáy sâu; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L252</summary>

```text
HÌNH L252 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vì vậy, tiến hóa đã thay thế toàn bộ bóng khí bằng một lớp sụn xơ gelatin dày tới 7,5 cm nằm ngay dưới lớp da của nó!". Bố cục: Bản vẽ cắt ngang lớp da cá mặt trăng hiển thị lớp mô liên kết gelatin xốp màu trắng ngà nhẹ hơn nước biển; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L253</summary>

```text
HÌNH L253 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lớp mô gelatin kỳ diệu này có tỷ trọng gần như tương đương với nước biển, giúp con cá đạt trạng thái trôi nổi trung tính ở bất kỳ độ sâu nào mà không sợ áp suất nghiền nát!". Bố cục: Chú cá mặt trăng trôi lơ lửng tự nhiên trong nước mà không cần tốn một chút năng lượng nào để duy trì độ sâu; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L254</summary>

```text
HÌNH L254 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sau mỗi chuyến lặn sâu 800 m xuống vùng nước băng giá 4°C để săn sứa, thân nhiệt của chú cá bị hạ xuống mức báo động nguy hiểm.". Bố cục: Đồ thị đo thân nhiệt của cá mặt trăng lao dốc xuống vùng màu xanh băng giá bốn độ C sau chuyến lặn sâu; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L255</summary>

```text
HÌNH L255 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đó là lý do tại sao nó phải bơi lên mặt biển, nằm nghiêng hoàn toàn thân hình dẹt 2 m của mình phơi nắng trên mặt nước như một chiếc đĩa bay tắm nắng!". Bố cục: Chú chú Cá Mặt Trăng (ocean sunfish) hoạt hình khổng lồ hình đĩa tròn dẹt màu xám bạc, không có cuống đuôi, hai vây lưng và vây phần đuôi dựng đứng dài ngoằng, nằm ngửa trên chiếc cáng cứu thương quá khổ mắt to tròn ngơ ngác nằm ngang trên mặt biển phẳng lặng như gương, ánh nắng vàng rực rỡ sưởi ấm toàn bộ thân hình tròn dẹt lấp lánh; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L256</summary>

```text
HÌNH L256 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hành vi tắm nắng này giúp hấp thu tối đa năng lượng mặt trời để sưởi ấm lại các thớ cơ và mạch nước màu bị đông cứng dưới đáy sâu!". Bố cục: Dòng nhiệt lượng màu đỏ ấm áp từ ánh nắng mặt trời thẩm thấu qua lớp da làm ấm các mạch nước màu nuôi tim và não bộ; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L257</summary>

```text
HÌNH L257 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đồng thời, khi nằm phơi nắng trên mặt nước, các đàn chim biển và cá nhỏ sẽ bu lại rỉa sạch hơn 4 mươi loài ký sinh trùng bám trên da cho nó như một dịch vụ spa biển khơi miễn phí!". Bố cục: Đàn mòng biển trắng muốt đậu lên thân cá mặt trăng đang nằm nổi trên mặt nước rỉa sạch các con rận biển bám trên da; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L258</summary>

```text
HÌNH L258 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhịp tim của cá mặt trăng khi lặn sâu chỉ khoảng 20 nhịp mỗi phút để tiết kiệm oxy tối đa giữa vùng nước thiếu dưỡng khí!". Bố cục: Sơ đồ theo dõi nhịp tim lặn sâu của cá mặt trăng với nhịp đập chậm rãi tiết kiệm năng lượng tuyệt hảo; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L259</summary>

```text
HÌNH L259 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cơ quan thị giác của nó phát triển vượt trội với đôi mắt to lớn có khả năng nhìn thấu màn đêm đen kịt dưới đáy biển sâu thẳm!". Bố cục: Cận cảnh đôi mắt to tròn của cá mặt trăng phản chiếu ánh sáng lân tinh của đàn sứa dưới đáy đại dương; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Rầm! Rầm! Rầm! Tiếng đập cửa kính sảnh đón tiếp dồn dập vang lên át cả tiếng sấm rền ngoài trời!". Bố cục: Cánh cửa kính lớn rung bần bật dưới áp lực xô đẩy từ bên ngoài, bóng đen đồ sộ của các loài vật in dài trên nền sàn gạch hoa cương; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L260</summary>

```text
HÌNH L260 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc biệt hơn nữa, hệ thống cơ bắp vây lưng của cá mặt trăng tạo ra một lượng nhiệt nội sinh đáng kể trong quá trình bơi lội liên tục!". Bố cục: Sơ đồ nhiệt động lực học hiển thị các thớ cơ vây lưng màu đỏ thẫm phát ra luồng nhiệt lượng màu cam sưởi ấm các mô lân cận; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L261</summary>

```text
HÌNH L261 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mặc dù là loài cá biến nhiệt, nhưng đôi mắt và não bộ của nó được bao bọc bởi một lớp mỡ cách nhiệt đặc biệt giúp giữ ấm cho trung khu thần kinh giữa làn nước buốt giá!". Bố cục: Bản vẽ cắt lớp hộp sọ cá mặt trăng hiển thị lớp đệm lipid dày bao quanh hốc mắt và não bộ bảo vệ khỏi cái lạnh âm độ; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L262</summary>

```text
HÌNH L262 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ lớp mỡ cách nhiệt này, thị lực và phản xạ săn sứa của nó dưới độ sâu 800 m chẳng hề bị tê liệt vì giá lạnh!". Bố cục: Chú cá mặt trăng lướt đi trong bóng tối đại dương lạnh ngắt, đôi mắt vẫn mở to định vị chính xác từng bóng sứa phát quang; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L263</summary>

```text
HÌNH L263 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi bơi lên mặt nước phơi nắng, dòng nước màu ấm từ các mạch nước màu dưới da sẽ được phân phối ngược vào các cơ quan bên trong cơ thể bên trong!". Bố cục: Đồ họa tuần hoàn nước màu hiển thị các dòng nước màu đỏ ấm áp từ biểu bì chảy ngược vào tim và gan giúp kích hoạt lại quá trình trao đổi chất; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L264</summary>

```text
HÌNH L264 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đó là một hệ thống sưởi ấm năng lượng mặt trời tuần hoàn tự nhiên hoàn mỹ không tốn một xu tiền điện nào!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án bật cười giơ ngón tay cái tán thưởng cơ chế điều nhiệt độc đáo của người bạn khổng lồ.
```
</details>

<details><summary>L265</summary>

```text
HÌNH L265 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa hết đâu nhé! Cá mặt trăng cái còn nắm giữ kỷ lục vô địch tuyệt đối về khả năng sinh sản trong toàn bộ vương quốc động vật có xương sống!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án giơ ngón tay cái lên tỏ vẻ thán phục đỉnh cao trước con số thống kê sinh học phi thường.
```
</details>

<details><summary>L266</summary>

```text
HÌNH L266 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi lần sinh sản, một con cá mặt trăng mẹ có thể phóng thích vào đại dương tới 300 triệu quả trứng cùng một lúc!". Bố cục: bảng kẹp bệnh án y khoa khổng lồ (clipboard) kẹp trên giá đỡ kim loại, hiển thị 10 hồ sơ bệnh án hoạt hình với nhãn đơn thuốc phát sáng và sóng nhịp tim ECG màu đỏ nhấp nháy (không có chữ, không có số) rực sáng con số 300.000.000 quả trứng với biểu tượng hàng ngàn tia sáng lấp lánh phát tán khắp đại dương; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L267</summary>

```text
HÌNH L267 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi mới nở, con non chỉ dài vỏn vẹn 2 mm, tròn xoe và có gai nhọn bao quanh trông như một chú cá nóc mini tí hon ngộ nghĩnh!". Bố cục: Kính hiển vi hiển thị chú cá mặt trăng sơ sinh dài hai mi-li-mét có các gai nhọn bao quanh trông như một ngôi sao biển mini; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L268</summary>

```text
HÌNH L268 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Từ một chấm nhỏ 2 mm đó, nó lớn lên và tăng trọng lượng tới 60 triệu lần để đạt kích thước khổng lồ 2 tấn như bệnh nhân đang nằm trước mặt chúng ta!". Bố cục: Sơ đồ tiến hóa kích thước từ ấu trùng hai mi-li-mét phóng đại vọt lên con cá khổng lồ dài ba mét nặng hai tấn; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L269</summary>

```text
HÌNH L269 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sự gia tăng kích thước tới 60 triệu lần này là kỷ lục tăng trưởng vĩ đại nhất trong toàn bộ thế giới động vật trên Trái Đất!". Bố cục: Biểu đồ tăng trưởng dốc đứng hình tên lửa chứng minh sức sống mãnh liệt của loài cá mặt trăng qua hàng triệu năm sóng gió; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đoàn xe cứu thương chuyên dụng nối đuôi nhau rọi đèn pha vàng rực vào sảnh bệnh viện, còi hụ vang rền xé toạc màn đêm u tối!". Bố cục: Dãy xe cứu thương cổ điển bật đèn chớp xoay tròn màu đỏ rực, tiếng còi hụ khẩn cấp inh ỏi ngoài sân bệnh viện; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L270</summary>

```text
HÌNH L270 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chẩn đoán Khoa Hồi Sức Cấp Cứu Đại Dương: Bệnh nhân hoàn toàn khỏe mạnh, nhịp tim ổn định, bộ não 4 g đang vận hành cỗ máy 2 tấn ở hiệu suất tuyệt hảo!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười gật đầu hài lòng, đưa tay vỗ nhẹ vào chiếc vây lưng nhô lên khỏi mặt nước của chú chú Cá Mặt Trăng (ocean sunfish) hoạt hình khổng lồ hình đĩa tròn dẹt màu xám bạc, không có cuống đuôi, hai vây lưng và vây phần đuôi dựng đứng dài ngoằng, nằm ngửa trên chiếc cáng cứu thương quá khổ mắt to tròn ngơ ngác.
```
</details>

<details><summary>L271</summary>

```text
HÌNH L271 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đơn thuốc cho bệnh nhân: Tiếp tục ngâm mình thư giãn trong bể nước muối sinh lý, bổ sung một bữa tiệc sứa biển tươi sống và chuẩn bị xe cẩu đưa anh chàng ra vịnh biển lúc rạng đông!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án ký tên vào bệnh án số bốn, chú cá mặt trăng quẫy nhẹ hai chiếc vây làm bọt nước tung tóe như một lời cảm ơn ngây ngô.
```
</details>

<details><summary>L272</summary>

```text
HÌNH L272 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hai giờ 40 phút sáng! Chúng ta đã vượt qua được nửa chặng đường của ca trực đêm kinh hoàng! Toàn đội chuyển ngay sang Khoa Hộp Sọ và Răng Hàm Mặt để xử lý ca bệnh nanh dài đâm trán!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án cùng y tá rảo bước rời khỏi khu hồi sức đại dương, hướng về phía phòng khám nha khoa chuyên dụng.
```
</details>

<details><summary>L273</summary>

```text
HÌNH L273 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mời bệnh nhân số 5 bước vào ghế nha khoa chuyên dụng! Một ca bệnh răng hàm mặt dị thường đến mức làm các nha sĩ lành nghề nhất cũng phải toát mồ hôi hột!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đứng bên cạnh chiếc ghế nha khoa chuyên dụng có đèn rọi sáng rực rỡ, chú Lợn Hươu Babirusa hoạt hình da xám nhăn nheo ít lông, mõm dài, bốn chiếc răng nanh cong vút dị thường trong đó hai nanh trên mọc xuyên qua sống mũi uốn ngược về phía trán, vẻ mặt lo lắng sờ trán đang ngượng ngùng bước vào phòng khám.
```
</details>

<details><summary>L274</summary>

```text
HÌNH L274 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đó là Lợn Hươu Babirusa đến từ những cánh rừng nhiệt đới ẩm ướt trên đảo Sulawesi hoang sơ thuộc đất nước Indonesia!". Bố cục: Cận cảnh gương mặt da xám nhăn nheo của chú Lợn Hươu Babirusa hoạt hình da xám nhăn nheo ít lông, mõm dài, bốn chiếc răng nanh cong vút dị thường trong đó hai nanh trên mọc xuyên qua sống mũi uốn ngược về phía trán, vẻ mặt lo lắng sờ trán, nổi bật là bốn chiếc răng nanh khổng lồ cong vút dị thường nhô ra ngoài; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L275</summary>

```text
HÌNH L275 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chú lợn rụt rè ngồi lên chiếc ghế nha khoa bọc da êm ái, đưa 2 móng trước lên xoa xoa vầng trán nhăn nheo với vẻ mặt đầy lo lắng.". Bố cục: chú Lợn Hươu Babirusa hoạt hình da xám nhăn nheo ít lông, mõm dài, bốn chiếc răng nanh cong vút dị thường trong đó hai nanh trên mọc xuyên qua sống mũi uốn ngược về phía trán, vẻ mặt lo lắng sờ trán ngồi ngay ngắn trên ghế nha khoa, bốn chiếc nanh nhô cao chĩa thẳng vào bóng đèn soi sáng; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L276</summary>

```text
HÌNH L276 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy nhìn vào bộ hàm của anh chàng này mà xem! Đây không phải là răng nanh mọc bình thường, mà là một sự nổi loạn giải phẫu hoàn toàn đi ngược lại mọi quy luật tự nhiên!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án dùng kẹp nha khoa nhẹ nhàng nâng môi trên của bệnh nhân để kiểm tra chân răng.
```
</details>

<details><summary>L277</summary>

```text
HÌNH L277 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hai chiếc răng nanh hàm dưới mọc chìa ra ngoài mép môi nhọn hoắt như 2 lưỡi gươm ngắn đã đủ làm kẻ thù khiếp vía rồi.". Bố cục: Bản chụp X-quang xương hàm dưới của lợn babirusa với hai chiếc răng nanh cắm sâu vào xương hàm vững chắc; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L278</summary>

```text
HÌNH L278 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hai chiếc nanh dưới này sắc như dao cạo, dùng để tự vệ và gạt phăng các đòn tấn công của đối thủ trong những cuộc trò chơi đuổi bắt giành lãnh thổ.". Bố cục: Cận cảnh cạnh sắc của chiếc nanh hàm dưới mài mòn tự nhiên tạo thành mép cắt sắc bén; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L279</summary>

```text
HÌNH L279 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không chỉ dùng để tự vệ, chiếc nanh dưới còn là công cụ hữu hiệu để cắt đứt các dây leo dai nhách khi đi xuyên qua rừng rậm!". Bố cục: Chú lợn dùng nanh dưới ngoạm đứt một sợi dây leo vắt ngang lối đi trong rừng già; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhân viên điều dưỡng đang hối hả đẩy những chiếc cáng cứu thương quá khổ vào bên trong hành lang lát gạch men sáng loáng!". Bố cục: Hàng chục nhân viên y tế hối hả chạy dọc hành lang đẩy các cáng cứu hộ chuyên dụng có gắn bình dưỡng khí và máy đo nhịp tim; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L280</summary>

```text
HÌNH L280 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng điều làm cả giới y học kinh ngạc tột cùng lại nằm ở 2 chiếc răng nanh của hàm trên!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án chỉ đầu kẹp y tế vào phần sống mũi của chú lợn, nơi hai chiếc nanh trên đâm xuyên qua lớp da mặt.
```
</details>

<details><summary>L281</summary>

```text
HÌNH L281 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thay vì mọc chúc xuống dưới để cắn xé thức ăn như loài lợn rừng hay hổ báo, 2 chiếc răng nanh trên này lại mọc ngược hướng lên trời!". Bố cục: Sơ đồ giải phẫu ba chiều hiển thị mầm răng nanh hàm trên xoay ngược một trăm tám mươi độ trong xương hàm; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L282</summary>

```text
HÌNH L282 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi bắt đầu phát triển ở độ tuổi trưởng thành, chúng đâm xuyên thẳng qua vòm miệng, xuyên thủng lớp da sống mũi của chính con lợn rồi uốn cong ngược về phía sau trán!". Bố cục: Hình ảnh mô phỏng quá trình hai chiếc nanh nhọn hoắt xuyên thủng lớp da thịt sống mũi mọc trồi lên không trung; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L283</summary>

```text
HÌNH L283 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiếc nanh cong vút này có thể đạt chiều dài kỷ lục lên tới 40 cm, tạo thành một vòng cung hoàn mỹ ngay trước trán hộp sọ!". Bố cục: bảng kẹp bệnh án y khoa khổng lồ (clipboard) kẹp trên giá đỡ kim loại, hiển thị 10 hồ sơ bệnh án hoạt hình với nhãn đơn thuốc phát sáng và sóng nhịp tim ECG màu đỏ nhấp nháy (không có chữ, không có số) hiển thị con số 40 cm cùng hình vẽ chiếc nanh cong vút phát sáng vàng kim; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L284</summary>

```text
HÌNH L284 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không hề có men răng bao bọc bên ngoài, chiếc nanh này là ngà răng đặc quánh, tiếp tục mọc dài ra liên tục trong suốt toàn bộ cuộc đời của con vật!". Bố cục: Kính hiển vi soi cấu trúc vi mô của ngà răng lợn babirusa với các ống ngà xếp khít nhau bền vững; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L285</summary>

```text
HÌNH L285 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tốc độ mọc của ngà răng có thể đạt vài xăng-ti-mét mỗi 5, đòi hỏi con vật phải có chế độ mài mòn tự nhiên liên tục.". Bố cục: Mô hình mặt cắt ngà răng hiển thị các vòng sinh trưởng hàng năm xếp lớp như vân gỗ thân cây; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L286</summary>

```text
HÌNH L286 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khác với loài voi có ngà mọc từ răng cửa biến tính, ngà của lợn babirusa thực chất là chiếc răng nanh biến dị độc nhất vô nhị trong toàn bộ lớp thú có vú!". Bố cục: Sơ đồ so sánh nguồn gốc răng cửa của ngà voi với mầm răng nanh xoay ngược của lợn babirusa; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L287</summary>

```text
HÌNH L287 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và đây là điều thú vị về mặt di truyền học: Hiện tượng nanh mọc xuyên mũi này chỉ xuất hiện duy nhất ở những con đực trưởng thành!". Bố cục: Hình ảnh so sánh hộp sọ của lợn babirusa đực với bốn chiếc nanh khổng lồ bên cạnh hộp sọ lợn cái trơn nhẵn không có nanh trên; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L288</summary>

```text
HÌNH L288 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Những con lợn cái hoàn toàn không hề có nanh trên mọc ngược, nanh dưới của chúng cũng rất nhỏ và nằm gọn gàng bên trong mép môi!". Bố cục: Chú lợn cái babirusa gặm lá cây trong rừng với khuôn mặt hiền lành trơn tru không có nanh cong; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L289</summary>

```text
HÌNH L289 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Điều này chứng tỏ cặp nanh trên là một đặc điểm sinh dục thứ cấp đặc trưng, chịu sự điều khiển trực tiếp của nội tiết tố testosterone!". Bố cục: Sơ đồ nội tiết hiển thị nồng độ hormone testosterone kích hoạt sự phát triển của mầm ngà xoay ngược ở tuổi dậy thì; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mùi cồn sát trùng hòa lẫn với mùi ẩm ướt của bùn lầy, mùi tinh dầu thông và hơi muối biển mặn mòi tràn ngập bầu không khí!". Bố cục: Khung cảnh nhộn nhịp khẩn trương của sảnh cấp cứu với làn khói thuốc sát trùng mờ ảo và ánh đèn neon rực rỡ; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L290</summary>

```text
HÌNH L290 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đồng thời, cấu tạo dạ dày của lợn babirusa cũng vô cùng kỳ lạ, chia thành nhiều ngăn phức tạp tương tự loài động vật nhai lại!". Bố cục: Bản vẽ giải phẫu hệ tiêu hóa của lợn babirusa với dạ dày nhiều túi chứa hàng tỷ vi khuẩn lên men cellulose; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L291</summary>

```text
HÌNH L291 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ hệ vi sinh vật lên men dạ dày này, lợn babirusa có thể ăn và tiêu hóa được các loại rễ cây rừng chứa nhiều chất xơ dai và độc tố tự nhiên!". Bố cục: Chú lợn thản nhiên gặm những nhánh rễ cây có nhựa đắng trong rừng mà không hề bị rối loạn tiêu hóa; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L292</summary>

```text
HÌNH L292 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để bảo vệ mô mềm quanh sống mũi khỏi bị nhiễm trùng, con lợn thường xuyên đầm mình trong bùn khoáng núi lửa chứa lưu huỳnh tự nhiên!". Bố cục: Chú lợn babirusa ngâm mình trong hố bùn khoáng ấm áp, lớp bùn bao bọc quanh chân nanh tạo thành lớp màng bảo vệ vô trùng; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L293</summary>

```text
HÌNH L293 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bác sĩ trưởng khoa ơi em chụp cắt lớp vi tính hộp sọ cho nó mà 2 tay em run bần bật!". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng cầm tấm phim chụp cắt lớp vi tính CT hộp sọ giơ lên trước hộp đèn sáng, vẻ mặt đầy lo âu sợ hãi.
```
</details>

<details><summary>L294</summary>

```text
HÌNH L294 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đầu nhọn của cái nanh hàm trên nó cong sát sạt vào xương trán rồi! Chỉ cần nó gật đầu mạnh một cái là cái nanh tự cắm phập vào hộp sọ hi sinh bảo vệ tổ mất thôi bác sĩ ơi!". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng dùng ngón tay chỉ vào khoảng cách hẹp nghèo nàn giữa chóp nanh nhọn hoắt và bề mặt xương trán của chú lợn; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L295</summary>

```text
HÌNH L295 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Em có nên chuẩn bị một chiếc cưa nha khoa cầm tay để cưa bớt 2 cm chóp nanh ngay bây giờ không ạ?". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng cầm chiếc cưa mini khử trùng bằng cồn giơ lên ngơ ngác hỏi ý kiến bác sĩ; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L296</summary>

```text
HÌNH L296 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mối lo ngại của cô y tá hoàn toàn có cơ sở khoa học đàng hoàng! Nghiên cứu của nhà nhân chủng học Colin Groves đã ghi nhận những trường hợp cá biệt ngoài tự nhiên:". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án kẹp tấm phim chụp cắt lớp sọ não lên bảng đèn, dùng bút dạ đỏ khoanh tròn khoảng cách giữa đầu nanh và xương trán.
```
</details>

<details><summary>L297</summary>

```text
HÌNH L297 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở những con lợn hươu đực sống quá thọ trong điều kiện nuôi nhốt hoặc hoang dã, răng nanh của chúng không ngừng mọc dài ra mỗi ngày.". Bố cục: Bản vẽ giải phẫu hộp sọ lợn babirusa cổ đại cho thấy đầu răng nanh cong chạm vào bề mặt xương trán; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L298</summary>

```text
HÌNH L298 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu độ cong của nanh quá hẹp, chóp nanh sắc nhọn có thể chạm vào xương trán, chèn ép mô sọ và thậm chí xuyên thủng hộp sọ gây tổn thương não bộ nghiêm trọng!". Bố cục: Hình ảnh quét ba chiều hộp sọ hiển thị áp lực tiếp xúc giữa chóp răng nanh và bản xương ngoài của hộp sọ; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L299</summary>

```text
HÌNH L299 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đó là lý do nhiều nhà khoa học thế kỷ trước từng gọi loài lợn này là sinh vật sở hữu vũ khí hi sinh bảo vệ tổ ngớ ngẩn nhất của tự nhiên!". Bố cục: Hình vẽ minh họa biếm họa chú lợn tự đâm nanh vào trán bị gạch dấu hỏi chấm to tướng; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mọi người chú ý giữ trật tự! Xin mời các bệnh nhân không chen lấn xô đẩy tại quầy tiếp đón khẩn cấp!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án bước ra sảnh lớn, cất giọng vang ấm dõng dạc trấn an toàn bộ đám đông đang nhốn nháo ngoài sảnh.
```
</details>

<details><summary>L300</summary>

```text
HÌNH L300 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuy nhiên những trường hợp tự đâm thủng sọ não đó vô cùng hiếm gặp trong tự nhiên hoang dã!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án chỉ vào cấu trúc xương trán dày dặn có gờ nổi ngăn cản lực đâm của chiếc nanh; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L301</summary>

```text
HÌNH L301 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong môi trường rừng nguyên sinh, những cú cọ xát đầu vào thân cây gỗ mun và các cuộc giao đấu liên tục sẽ tự nhiên mài mòn và làm cùn đầu nhọn của chiếc nanh!". Bố cục: Chú lợn babirusa cọ mạnh chiếc nanh trên vào thân cây cổ thụ để làm cùn chóp nanh sắc nhọn; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L302</summary>

```text
HÌNH L302 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nghiên cứu của giáo sư Macdonald còn chỉ ra rằng lớp da quanh chân nanh của lợn babirusa ôm khít lấy thân ngà như một chiếc gioăng cao su sinh học!". Bố cục: Kính hiển vi hiển thị mô liên kết biểu bì bám chặt vào chân răng ngăn ngừa hoàn toàn vi khuẩn xâm nhập; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L303</summary>

```text
HÌNH L303 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vậy tại sao tiến hóa lại ban tặng cho loài lợn này một bộ răng nanh nguy hiểm đến mức độ như thế này?". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án khoanh tay trước ngực, đặt câu hỏi tu từ nhìn thẳng về phía các bác sĩ nội trú đang lắng nghe say mê.
```
</details>

<details><summary>L304</summary>

```text
HÌNH L304 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Câu trả lời nằm ở quy luật chọn lọc giới tính khốc liệt suốt hàng triệu 5 qua!". Bố cục: Cảnh hai chú lợn babirusa đực đứng thẳng bằng hai chân sau giữa rừng nhiệt đới, dùng mõm và nanh gạt nhau trong cuộc chiến giành bạn tình; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L305</summary>

```text
HÌNH L305 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nghiên cứu thực địa gần đây đã chứng minh: lợn babirusa không hề dùng nanh trên để cắn hay đào bới thức ăn dưới đất!". Bố cục: Chú lợn dùng mõm dẻo ủi nhẹ lớp lá mục tìm củ rễ cây chứ tuyệt đối không dùng nanh cày xới; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L306</summary>

```text
HÌNH L306 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi 2 con đực giao đấu giành bạn tình, chúng đứng thẳng bằng 2 chân sau như 2 võ sĩ quyền anh, dùng mõm tì đè và gạt đòn của đối phương!". Bố cục: Hai chú lợn đứng bằng hai chân sau giằng co quyết liệt giữa bụi cây rậm rạp; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L307</summary>

```text
HÌNH L307 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cặp nanh cong vút trên mặt đóng vai trò như một chiếc khiên chắn bảo vệ đôi mắt và cổ họng của con đực trước những cú cắn hiểm ác của đối thủ!". Bố cục: Đồ họa chuyển động chậm mô phỏng chiếc nanh trên gạt phăng cú đâm từ nanh dưới của đối thủ bảo vệ vùng mắt nhạy cảm; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L308</summary>

```text
HÌNH L308 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đồng thời, con đực nào sở hữu cặp nanh dài và cong hoàn mỹ nhất sẽ chứng minh cho con cái thấy nó có bộ gen kiên cường và sức sống bền bỉ phi thường!". Bố cục: Chú chú Lợn Hươu Babirusa hoạt hình da xám nhăn nheo ít lông, mõm dài, bốn chiếc răng nanh cong vút dị thường trong đó hai nanh trên mọc xuyên qua sống mũi uốn ngược về phía trán, vẻ mặt lo lắng sờ trán đực kiêu hãnh ngẩng cao đầu khoe cặp nanh uốn lượn dưới ánh hoàng hôn rừng nhiệt đới; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L309</summary>

```text
HÌNH L309 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó giống như chiếc đuôi xòe lộng lẫy của chim công hay cặp sừng đồ sộ của loài hươu đực vậy!". Bố cục: Hình ảnh so sánh nanh lợn babirusa với chiếc đuôi rực rỡ sắc màu của chim công đực; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Anh khỉ đột xin vui lòng không dựa lưng vào vách kính tủ thuốc kẻo vỡ kính! Và chú nhím lông nhọn làm ơn giữ khoảng cách an toàn với dép xốp của các cô y tá!". Bố cục: chú Khỉ Đột Lưng Bạc hoạt hình cơ bắp cuồn cuộn vạm vỡ, mảng lông bạc sáng chói dọc sống lưng, bụng to tròn căng phồng vì chứa đầy lá cây lên men, ngồi xếp bằng trên giường bệnh ôm bụng thở dài ngượng ngùng né người khỏi tủ thuốc, chú chú Nhím Lông Nhọn Bắc Mỹ hoạt hình béo tròn xù xì, toàn thân phủ kín ba mươi ngàn chiếc gai nhọn trắng đen, đang ôm chặt một thân cây gỗ gặm vỏ thuốc, người tỏa mùi tinh dầu thơm nhẹ chớp mắt ngơ ngác lùi lại phía sau hàng ghế chờ.
```
</details>

<details><summary>L310</summary>

```text
HÌNH L310 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Càng sở hữu cặp nanh đối xứng và uốn cong chuẩn mực, con đực càng khẳng định được sức khỏe dẻo dai và khả năng sinh sản vượt trội trong bầy đàn!". Bố cục: Chú lợn cái ngước nhìn cặp nanh cong tuyệt đẹp của con đực với vẻ say đắm giữa thảm rừng nhiệt đới; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L311</summary>

```text
HÌNH L311 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "May mắn thay cho bệnh nhân của chúng ta hôm nay: chóp nanh vẫn cách xương trán tận 2,5 cm, hoàn toàn an toàn và chưa cần phải mài bớt một mi-li-mét nào!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười dùng thước đo y tế kiểm tra khoảng cách, vỗ nhẹ vào bờ vai dày dặn của chú chú Lợn Hươu Babirusa hoạt hình da xám nhăn nheo ít lông, mõm dài, bốn chiếc răng nanh cong vút dị thường trong đó hai nanh trên mọc xuyên qua sống mũi uốn ngược về phía trán, vẻ mặt lo lắng sờ trán.
```
</details>

<details><summary>L312</summary>

```text
HÌNH L312 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chẩn đoán của Phòng Cấp Cứu Tạo Hóa: Hàm răng kỳ dị nhưng là biểu tượng kiêu hãnh của tình yêu và lòng dũng cảm thảo nguyên nhiệt đới!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đóng dấu ĐẠT CHUẨN lên bệnh án số năm, đưa cho chú lợn một túi quả ngọt tráng miệng.
```
</details>

<details><summary>L313</summary>

```text
HÌNH L313 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôi chỉ cần vệ sinh sạch sẽ vùng chân răng xuyên qua sống mũi và bôi một lớp thuốc sát trùng nhẹ là anh chàng có thể tự tin đi tìm bạn gái được rồi!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án dùng tăm bông thấm thuốc sát trùng màu vàng lau nhẹ chân răng cho chú lợn, chú lợn híp mắt kêu ụt ịt tỏ vẻ hài lòng.
```
</details>

<details><summary>L314</summary>

```text
HÌNH L314 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Anh bạn lợn hươu hãy nhớ thường xuyên đầm mình trong bùn khoáng để sát trùng tự nhiên cho 2 bên sống mũi nhé!". Bố cục: Chú chú Lợn Hươu Babirusa hoạt hình da xám nhăn nheo ít lông, mõm dài, bốn chiếc răng nanh cong vút dị thường trong đó hai nanh trên mọc xuyên qua sống mũi uốn ngược về phía trán, vẻ mặt lo lắng sờ trán gật gù hiểu ý, hai tai vẫy vẫy vui mừng chuẩn bị rời ghế nha khoa; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L315</summary>

```text
HÌNH L315 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hồ sơ Khoa Nha Khoa Dị Tật hoàn tất mỹ mãn! Giờ thì nghe kìa, tiếng la hét ngoài sảnh báo hiệu đợt náo loạn thứ 2 vừa nổ ra!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án cất chiếc panh nha khoa, chạy vội ra hành lang xem chuyện gì đang xảy ra tiếp theo.
```
</details>

<details><summary>L316</summary>

```text
HÌNH L316 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ba giờ 30 phút sáng. Cơn buồn ngủ bắt đầu kéo sụp 2 mí mắt của tôi xuống, thì một tiếng thét thất thanh lại vang lên từ phía cuối hành lang!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đang ngồi ghi chép bệnh án tại quầy trực thì giật mình đánh rơi chiếc bút bi, tiếng kêu la hoảng hốt vọng lại từ sảnh chờ.
```
</details>

<details><summary>L317</summary>

```text
HÌNH L317 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôi giật bắn mình đánh rơi chiếc bút bi xuống bàn, vội vàng đứng bật dậy chạy ra ngoài xem chuyện gì vừa xảy ra.". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mở tung cửa phòng nha khoa, sải bước dài hướng về phía sảnh phòng chờ đang ồn ào như ong vỡ tổ.
```
</details>

<details><summary>L318</summary>

```text
HÌNH L318 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ái da da! Đau điếng người thế này! Cứu em với bác sĩ ơi! Có ai vừa rải một bãi chông sắt khắp sàn nhà hành lang bệnh viện thế này!". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng một tay ôm một bên chân đang co lên nhảy lò cò, dưới đế dép cao su cắm chi chít năm sáu chiếc gai nhọn trắng đen; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L319</summary>

```text
HÌNH L319 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cô y tá vừa ôm một bên chân vừa nhảy lò cò trên một chân còn lại, khuôn mặt mếu máo đau đớn như vừa dẫm phải bẫy chông thời cổ đại!". Bố cục: Cận cảnh chiếc dép y tế màu xanh bằng cao su xốp bị đâm thủng bởi những chiếc gai nhọn có hai màu đen trắng đan xen; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn thể đội ngũ y bác sĩ nội trú mau chóng vào vị trí trực chiến! Chuẩn bị máy chụp X-quang, máy siêu âm và các bộ dụng cụ vi phẫu ngay lập tức!". Bố cục: Các bác sĩ trẻ trong trang phục y tế hối hả mở các tủ đồ nghề kim loại sáng loáng, chuẩn bị sẵn sàng cho ca trực đêm; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L320</summary>

```text
HÌNH L320 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thủ phạm của vụ rải chông liên hoàn này không ai khác chính là chú Nhím Lông Nhọn Bắc Mỹ béo tròn đang lững thững đi dạo cạnh các dãy ghế!". Bố cục: chú Nhím Lông Nhọn Bắc Mỹ hoạt hình béo tròn xù xì, toàn thân phủ kín ba mươi ngàn chiếc gai nhọn trắng đen, đang ôm chặt một thân cây gỗ gặm vỏ thuốc, người tỏa mùi tinh dầu thơm nhẹ béo ú tròn xoe như quả bóng gai, vẻ mặt ngây thơ vô tội đang gặm dở một khúc gỗ mục của chiếc ghế băng bệnh viện; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L321</summary>

```text
HÌNH L321 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chú nhím vừa đi vừa cọ cọ chiếc lưng béo ú vào mép tường bê tông, làm rụng lả tả hàng chục chiếc gai nhọn cắm phập xuống sàn gạch men!". Bố cục: Những chiếc gai nhọn cắm thẳng đứng trên sàn nhà như những chiếc đinh ba mini, phản chiếu ánh sáng đèn tuýp lấp lánh; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L322</summary>

```text
HÌNH L322 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các bệnh nhân khác xung quanh hoảng hốt nhảy tót lên ghế băng, co chân lên cao để tránh bãi mìn sinh học đang lan rộng!". Bố cục: Chú khỉ đột ngồi co ro trên lưng ghế sắt, hai mắt tròn xoe nhìn bãi gai nhọn dưới sàn vẻ đầy kiêng dè; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L323</summary>

```text
HÌNH L323 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đứng yên! Tất cả nhân viên và bệnh nhân trong sảnh đứng yên tại chỗ không được bước thêm một bước nào!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án cầm chiếc đèn pin y tế bật sáng quét dọc sàn nhà, ánh sáng rọi lên hàng chục chiếc gai nhọn cắm lởm chởm trên sàn gạch men như một bãi mìn chông; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L324</summary>

```text
HÌNH L324 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôi lập tức bật chiếc đèn pin y tế công suất lớn quét dọc mặt sàn, rọi sáng một bãi mìn sinh học dày đặc trải dài từ quầy thuốc tới cửa phòng khám!". Bố cục: Luồng ánh sáng trắng của đèn pin quét qua mặt sàn gạch, làm lộ rõ hàng trăm chiếc gai nhọn cắm chi chít khắp lối đi; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L325</summary>

```text
HÌNH L325 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mọi người nghe cho rõ đây: Tuyệt đối không ai được dùng tay không để nhổ những chiếc gai này ra khỏi da thịt hay đế giày!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án nghiêm giọng cảnh báo, dùng một chiếc kẹp y tế chuyên dụng gắp nhẹ một chiếc gai nhọn lên đưa vào dưới ánh đèn soi.
```
</details>

<details><summary>L326</summary>

```text
HÌNH L326 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhiều người xem phim hoạt hình thường lầm tưởng rằng nhím có khả năng co cơ phóng gai bay vèo vèo như tên bắn về phía kẻ thù.". Bố cục: Hình ảnh biếm họa chú nhím bắn gai vèo vèo bị gạch một dấu chéo đỏ to tướng biểu thị tin đồn sai lệch; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L327</summary>

```text
HÌNH L327 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Điều đó hoàn toàn sai sự thật 100%! Nhím không hề có bất kỳ bó cơ nào có thể bắn gai ra ngoài không gian!". Bố cục: Chú nhím cuộn tròn thành quả cầu gai xù xì, các cơ dưới da chỉ có tác dụng dựng đứng các sợi gai lên dựng ngược; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L328</summary>

```text
HÌNH L328 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng cơ chế tháo rời lông gai thụ động của nó thì tinh vi và nguy hiểm hơn súng đạn gấp trăm lần!". Bố cục: Cận cảnh gốc nang lông của nhím gắn hờ hững vào lớp da, chỉ cần một va chạm nhẹ là gốc gai lập tức tách rời khỏi cơ thể con nhím; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L329</summary>

```text
HÌNH L329 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trước khi rụng gai, con nhím thường phát ra những tiếng nghiến răng ken két như tiếng cảnh báo gầm gừ để xua đuổi đối thủ!". Bố cục: Chú nhím nghiến răng ken két, hai má phập phồng đe dọa trước khi vung chiếc đuôi ngắn cắm đầy gai; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đêm nay chúng ta sẽ không chợp mắt dù chỉ một giây để giải mã toàn bộ 10 kỳ quan cơ thể học này!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án nhìn quanh toàn thể đội ngũ y tế với ánh mắt kiên định và đầy nhiệt huyết của người thầy thuốc dày dạn kinh nghiệm.
```
</details>

<details><summary>L330</summary>

```text
HÌNH L330 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cú quất đuôi của nhím có thể đạt vận tốc tới 20 m mỗi giây, cắm phập hàng chục mũi chông vào mõm kẻ săn mồi trong chớp mắt!". Bố cục: Đồ họa chuyển động chậm mô phỏng chiếc đuôi nhím quất ngang với gia tốc cực lớn cắm gai vào mục tiêu; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L331</summary>

```text
HÌNH L331 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gốc nang lông của chiếc gai gắn vào lớp da con nhím vô cùng lỏng lẻo, chỉ cần một va quẹt nhẹ như một cái phẩy tay là chiếc gai tự động rụng ra ngay lập tức.". Bố cục: Hình vẽ giải phẫu gốc nang lông hình củ hành siêu nhỏ gắn hờ hững vào biểu bì da của chú nhím lông nhọn; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L332</summary>

```text
HÌNH L332 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn bộ cơ thể của một con nhím lông nhọn Bắc Mỹ trưởng thành được bao bọc bởi hơn 30.000 chiếc lông gai sắc nhọn!". Bố cục: bảng kẹp bệnh án y khoa khổng lồ (clipboard) kẹp trên giá đỡ kim loại, hiển thị 10 hồ sơ bệnh án hoạt hình với nhãn đơn thuốc phát sáng và sóng nhịp tim ECG màu đỏ nhấp nháy (không có chữ, không có số) bật sáng con số 30.000 chiếc gai rực rỡ bên cạnh hình ảnh đồ họa chiếc lông nhím; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L333</summary>

```text
HÌNH L333 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi chiếc gai thực chất là một sợi lông biến tính rỗng ruột bên trong, cực kỳ nhẹ nhưng lại cứng cáp phi thường nhờ cấu trúc vách xốp tổ ong.". Bố cục: Bản vẽ cắt ngang sợi lông nhím hiển thị cấu trúc tổ ong xốp bên trong giúp tăng độ cứng và giảm trọng lượng tối đa; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L334</summary>

```text
HÌNH L334 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ cấu trúc rỗng xốp chứa đầy không khí này, hàng chục ngàn chiếc gai còn đóng vai trò như một chiếc áo phao cứu sinh tự nhiên hoàn hảo!". Bố cục: Chú nhím bơi lội ung dung trên mặt nước sông, toàn bộ cơ thể nổi bồng bềnh nhờ lớp gai rỗng xốp nâng đỡ; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L335</summary>

```text
HÌNH L335 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi gặp lũ quét rừng hay cần vượt sông tìm thức ăn, con nhím có thể bơi qua những khúc sông rộng mà không sợ bị chìm nghỉm!". Bố cục: Hình ảnh chú nhím thản nhiên bơi qua dòng suối cuồn cuộn giữa rừng già Bắc Mỹ; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L336</summary>

```text
HÌNH L336 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và đây là bí mật khủng khiếp nhất khiến các bác sĩ ngoại khoa phải rùng mình kinh hãi: Cấu trúc vi cơ học ở phần chóp nhọn của mỗi chiếc gai!". Bố cục: Kính hiển vi điện tử phóng đại chóp nhọn của chiếc gai nhím lên hàng nghìn lần, làm lộ ra một cấu trúc cơ học đáng sợ; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L337</summary>

```text
HÌNH L337 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở phần đầu của mỗi chiếc gai có chứa tới 7 trăm đến 800 chiếc vi ngạnh ngược siêu nhỏ xếp tầng tầng lớp lớp như vảy cá mập!". Bố cục: Hàng trăm chiếc vảy ngạnh ngược sắc lẹm nhô ra hướng về phía sau như những chiếc lưỡi câu mini đan kết dày đặc; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L338</summary>

```text
HÌNH L338 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Những chiếc vi ngạnh này nhỏ đến mức mắt thường không thể nhìn thấy, nhưng chúng sắc bén vô song và cực kỳ dẻo dai!". Bố cục: Kính hiển vi điện tử quét màu hiển thị các lưỡi ngạnh ngược bằng chất sừng keratin cứng cáp như mũi kim thép; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L339</summary>

```text
HÌNH L339 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nghiên cứu của tiến sĩ Cho công bố trên tạp chí Viện Hàn Lâm Khoa Học Hoa Kỳ PNAS đã đo đạc chính xác lực tác động cơ học này:". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án giơ bản đồ thị lực kéo và lực đâm của lông nhím lên trước mặt toàn thể y bác sĩ.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bởi vì nguyên lý tối thượng tại Phòng Cấp Cứu Tạo Hóa của chúng ta luôn luôn là:". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án chỉ tay lên dòng khẩu hiệu bằng chữ mạ vàng gắn trang trọng trên vòm cửa sảnh đón tiếp.
```
</details>

<details><summary>L340</summary>

```text
HÌNH L340 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi đâm vào da thịt, các vi ngạnh ngược này nằm ép sát xuôi chiều vào thân gai, giúp giảm tới 54% lực đâm so với kim tiêm y tế thông thường!". Bố cục: Mũi tên đồ họa màu xanh mô phỏng chiếc gai xuyên ngọt ngào qua lớp da với lực cản cực thấp; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L341</summary>

```text
HÌNH L341 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ đó, chiếc gai có thể xuyên ngọt lịm qua lớp da thịt dày cộp của kẻ thù chỉ bằng một cú quẫy đuôi nhẹ nhàng!". Bố cục: Hình ảnh chiếc gai nhọn đâm xuyên qua lớp lông dày của một chú sói rừng đang cố tấn công con nhím; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L342</summary>

```text
HÌNH L342 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng một khi đã cắm sâu vào trong cơ thịt, các vi ngạnh này lập tức hút ẩm từ dịch mô cơ thể rồi xòe bung ra như những chiếc mỏ neo mini!". Bố cục: Khi có lực kéo ngược ra ngoài, hàng trăm chiếc vảy ngạnh lập tức móc chặt vào các sợi cơ thịt xung quanh; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L343</summary>

```text
HÌNH L343 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lực cần thiết để rút chiếc gai ra tăng vọt lên gấp 3 lần so với lực đâm vào, gây đau đớn dữ dội và xé rách các mô xung quanh nếu cố giật mạnh bằng tay!". Bố cục: Đồ thị lực kéo nhảy vọt lên đỉnh đỏ rực, mô phỏng cảm giác đau đớn khi cố tình giật chiếc gai ra bằng tay không; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L344</summary>

```text
HÌNH L344 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chất keratin ở chóp gai khi ngậm nước mô còn trương nở nhẹ, khiến độ bám dính của các ngạnh ngược càng thêm chắc chắn và khó tách rời!". Bố cục: Kính hiển vi điện tử quét hiển thị các phiến ngạnh ngậm nước nở to khóa chặt lấy các thớ cơ thịt; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L345</summary>

```text
HÌNH L345 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thậm chí, nếu không được gắp ra đúng kỹ thuật ngoại khoa, sự co bóp tự nhiên của các thớ cơ sẽ khiến chiếc gai tự động di chuyển sâu hơn vào trong cơ thể mỗi ngày vài mi-li-mét!". Bố cục: Sơ đồ y học minh họa chiếc gai nhím tự trườn sâu vào mô mỡ theo nhịp co bóp của cơ bắp; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L346</summary>

```text
HÌNH L346 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đã từng có những con gấu hay báo sư tử bị gai nhím cắm vào mõm, chiếc gai tự trườn xuyên qua má, đâm vào mạch nước màu lớn hoặc mắt gây tử vong thương tâm!". Bố cục: Bản vẽ hộp sọ của loài dã thú săn mồi với những chiếc gai nhím đâm sâu vào các hốc mô mềm; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L347</summary>

```text
HÌNH L347 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nên cô y tá hãy ngồi yên trên ghế để tôi dùng kìm kẹp y tế chuyên dụng xoay nhẹ góc 45 độ rồi rút dứt khoát theo trục thẳng đứng nhé!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án quỳ một chân xuống, thao tác khéo léo dùng kìm kẹp từng chiếc gai cắm trên đế dép và gấu quần của y tá gắp ra an toàn.
```
</details>

<details><summary>L348</summary>

```text
HÌNH L348 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thao tác xoay nhẹ góc 45 độ này giúp các vi ngạnh ngược uốn cong mềm mại theo thớ cơ, giải phóng lực móc neo mà không làm rách mô tế bào!". Bố cục: Mô hình 3D minh họa động tác xoay kẹp y tế làm gập các vảy ngạnh ngược giúp rút gai ra êm ái; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L349</summary>

```text
HÌNH L349 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tách! Chiếc gai cuối cùng đã được đưa vào khay nhôm vô trùng. Sảnh phòng chờ của Phòng Cấp Cứu Tạo Hóa thở phào nhẹ nhõm như vừa vượt qua một bãi mìn sinh học!". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng xoa xoa gấu quần thở phào, các bệnh nhân xung quanh vỗ tay hoan hô tài nghệ của Bác Sĩ Trưởng Khoa.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không có sinh vật nào trên Trái Đất này sinh ra với một nét giải phẫu thừa thãi hay một cấu trúc sai lầm!". Bố cục: Cận cảnh gương mặt thông thái và nghiêm nghị của ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án toát lên niềm tin mãnh liệt vào sự hoàn mỹ của tự nhiên.
```
</details>

<details><summary>L350</summary>

```text
HÌNH L350 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Được rồi anh bạn nhím béo tròn, mời anh vào phòng khám Khoa Da Liễu ngay để kiểm tra xem lớp kháng sinh tự nhiên trên lưng anh còn đủ dùng không nhé!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án dùng một chiếc chổi y tế gom các sợi gai rụng trên sàn, vỗ nhẹ vào chiếc mõm tròn của chú chú Nhím Lông Nhọn Bắc Mỹ hoạt hình béo tròn xù xì, toàn thân phủ kín ba mươi ngàn chiếc gai nhọn trắng đen, đang ôm chặt một thân cây gỗ gặm vỏ thuốc, người tỏa mùi tinh dầu thơm nhẹ đang chớp mắt ngây thơ.
```
</details>

<details><summary>L351</summary>

```text
HÌNH L351 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôi yêu cầu chú nhím phải đi theo đường kẻ vạch cách ly màu vàng để không làm rụng gai thêm một lần nào nữa!". Bố cục: Chú chú Nhím Lông Nhọn Bắc Mỹ hoạt hình béo tròn xù xì, toàn thân phủ kín ba mươi ngàn chiếc gai nhọn trắng đen, đang ôm chặt một thân cây gỗ gặm vỏ thuốc, người tỏa mùi tinh dầu thơm nhẹ ngoan ngoãn đi theo vạch sơn vàng trên sàn nhà, hai mắt chớp chớp vẻ hối lỗi ngộ nghĩnh; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L352</summary>

```text
HÌNH L352 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bốn chiếc bàn chân bọc gai thịt xù xì của chú nhím bước đi lẹp xẹp ngoan ngoãn theo sau lưng bác sĩ, không dám cọ lưng vào tường thêm một lần nào!". Bố cục: Chú nhím bước từng bước chậm rãi trên thảm trải cách ly, các y bác sĩ khẽ mỉm cười trước dáng đi vụng về đáng yêu; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L353</summary>

```text
HÌNH L353 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ca trực đêm vẫn còn 2 chuyên khoa hóc búa nhất đang chờ đón: Khoa Tuần Hoàn Áp Suất Cao và Khoa Rối Loạn Hành Vi! Toàn đội tiếp tục chiến đấu nào!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án cất chiếc kìm vào túi áo, hướng thẳng bước chân về phía phòng khám tuần hoàn áp lực cao ở cuối hành lang.
```
</details>

<details><summary>L354</summary>

```text
HÌNH L354 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bíp! Bíp! Bíp! Tiếng còi báo động quá tải áp suất từ chiếc máy đo huyết áp kỹ thuật số vang lên dồn dập ngay khi chúng tôi bước vào phòng khám tuần hoàn!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án cùng cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng bước nhanh vào phòng khám có trang bị hệ thống máy đo huyết áp áp lực cao, kim đồng hồ đo áp lực nhảy vọt lên vạch đỏ chót; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L355</summary>

```text
HÌNH L355 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bệnh nhân số 7 của chúng ta đang đứng gục đầu bên cửa sổ: Quý cô Hươu Cao Cổ cao tới 5 m, chiếc cổ dài 2 m buông thõng vẻ mệt mỏi rã rời!". Bố cục: Toàn cảnh chú Hươu Cao Cổ hoạt hình cao lêu nghêu có đốm hoa văn nâu vàng, chiếc cổ dài thẳng tắp quấn dải băng đo huyết áp y tế to bản màu đỏ, mắt to hiền từ chớp chớp cao năm mét với bộ lông hoa văn màu hạt dẻ tuyệt đẹp, chiếc cổ dài cong cong gục đầu tựa vào khung cửa sổ kính phòng khám; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L356</summary>

```text
HÌNH L356 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ số huyết áp hiển thị trên màn hình điện tử làm toàn thể các bác sĩ tim mạch phải lạnh gáy kinh hoàng: 200 8 mươi trên 180 mi-li-mét thủy ngân!". Bố cục: bảng kẹp bệnh án y khoa khổng lồ (clipboard) kẹp trên giá đỡ kim loại, hiển thị 10 hồ sơ bệnh án hoạt hình với nhãn đơn thuốc phát sáng và sóng nhịp tim ECG màu đỏ nhấp nháy (không có chữ, không có số) bật sáng chỉ số huyết áp 280/180 mmHg nhấp nháy đỏ rực kèm theo tiếng còi cảnh báo cấp cứu khẩn cấp; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L357</summary>

```text
HÌNH L357 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mức huyết áp tâm thu lên tới 280 mmHg! Cao gấp hơn 2 lần chỉ số huyết áp bình thường của một người trưởng thành khỏe mạnh!". Bố cục: Màn hình điện tâm đồ hiển thị các đường sóng áp lực cao vút như những đỉnh núi nhọn hoắt; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L358</summary>

```text
HÌNH L358 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở một người bình thường, mức huyết áp khủng khiếp này sẽ làm vỡ tan các mạch nước màu não, gây xuất huyết não và tử vong tức thì trong vài phút!". Bố cục: Sơ đồ y học hiển thị nguy cơ vỡ phình mạch nước màu não ở người khi huyết áp vượt ngưỡng hai trăm mi-li-mét thủy ngân; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L359</summary>

```text
HÌNH L359 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thế nhưng quý cô hươu cao cổ của chúng ta vẫn đứng vững vàng, chỉ hơi hoa mắt và chóng mặt nhẹ sau khi vừa cúi gập người xuống uống nước suối bên ngoài sảnh!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án ngước nhìn lên đỉnh đầu chú hươu cao cổ cách mặt đất hơn ba mét, đưa ống nghe chuyên dụng lên kiểm tra nhịp đập động mạch cảnh.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Những gì mắt thường nhìn vào tưởng như dị tật, bệnh hoạn hay ngớ ngẩn, thực chất lại là tuyệt tác đỉnh cao của hàng triệu 5 chọn lọc tự nhiên khốc liệt!". Bố cục: Bức tranh toàn cảnh hội tụ mười sinh vật kỳ dị dưới ánh sáng rực rỡ của đèn phòng mổ, mỗi loài mang một cấu trúc cơ thể phi thường; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L360</summary>

```text
HÌNH L360 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhịp tim của bệnh nhân đập mạnh đến mức tôi có thể nhìn thấy từng đợt sóng nước màu dâng lên cuồn cuộn dọc theo tĩnh mạch cổ dài 2 m!". Bố cục: Cận cảnh chiếc cổ thon dài của hươu cao cổ với các mạch nước màu lớn phập phồng nhịp nhàng dưới lớp da lông ngắn mịn; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L361</summary>

```text
HÌNH L361 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bác sĩ ơi, có phải cô hươu này bị cơn bão tăng huyết áp kịch phát ác tính không ạ?". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng cầm chiếc ống tiêm thuốc hạ áp khẩn cấp run run ngước nhìn bác sĩ trưởng khoa xin chỉ thị; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L362</summary>

```text
HÌNH L362 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Em có nên tiêm ngay một liều thuốc chẹn kênh canxi liều cao để hạ huyết áp của cô ấy xuống mức 120 không bác sĩ?". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng băn khoăn giơ lọ thuốc hạ áp ra trước mặt bác sĩ với vẻ mặt đầy lo lắng; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L363</summary>

```text
HÌNH L363 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bác sĩ trưởng khoa ơi nếu cô ấy cúi đầu xuống uống nước một lần nữa thì huyết áp có dồn lên làm nổ tung não bộ của cô ấy không ạ?". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng ôm chiếc máy đo huyết áp, ánh mắt tròn xoe nhìn chiếc cổ dài miên man của chú hươu cao cổ; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L364</summary>

```text
HÌNH L364 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhìn chiếc cổ dài 2 m ngoằn ngoèo kia mà em tưởng tượng như một đường ống dẫn dầu cao áp xuyên lục địa vậy bác sĩ ơi!". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng giơ hai tay miêu tả độ cao chót vót của đầu hươu cao cổ so với mặt đất; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L365</summary>

```text
HÌNH L365 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và còn một điều kỳ lạ nữa bác sĩ ơi: Dây thần kinh điều khiển thanh quản của cô ấy dài tới 4,5 m lận đó bác sĩ, sao tiến hóa lại đi đường vòng xa xôi thế ạ?". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng chỉ vào sơ đồ giải phẫu thần kinh cổ hươu cao cổ với đường chạy ngoằn ngoèo bất thường; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L366</summary>

```text
HÌNH L366 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyệt đối cấm tiêm thuốc hạ áp cô y tá nhé! Nếu hạ huyết áp của cô ấy xuống 120 thì cô ấy sẽ đột tử vì thiếu nước màu não ngay lập tức đấy!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án nghiêm giọng ra lệnh, nhẹ nhàng gạt ống tiêm thuốc hạ áp sang một bên.
```
</details>

<details><summary>L367</summary>

```text
HÌNH L367 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây là mức huyết áp hoàn toàn bình thường và bắt buộc phải có để duy trì sự sống cho sinh vật cao nhất trên cạn này!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án dùng phấn vẽ lên bảng sơ đồ cột áp thủy tĩnh của cột nước màu cao hai mét từ tim lên não hươu cao cổ.
```
</details>

<details><summary>L368</summary>

```text
HÌNH L368 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy làm một bài toán vật lý thủy tĩnh đơn giản mà bất kỳ kỹ sư nào cũng phải thán phục:". Bố cục: Sơ đồ vật lý cơ học hiển thị cột chất lỏng cao hai mét cần một áp suất bơm tối thiểu một trăm mi-li-mét thủy ngân chỉ để thắng trọng lực Trái Đất; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L369</summary>

```text
HÌNH L369 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trái tim của hươu cao cổ nằm cách bộ não ở trên đỉnh đầu một khoảng cách xa tới 2 m theo phương thẳng đứng!". Bố cục: Hình ảnh giải phẫu vị trí trái tim khổng lồ trong lồng ngực hươu cao cổ nối với bộ não trên cao bằng động mạch cảnh dài hai mét; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và nhiệm vụ của người thầy thuốc đêm nay là lắng nghe câu chuyện sinh tồn kỳ diệu được khắc ghi sâu bên trong từng thớ cơ và mạch nước màu của chúng!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười đầy xúc động, nhẹ nhàng mở chiếc cặp da đựng dụng cụ y tế chuyên dụng.
```
</details>

<details><summary>L370</summary>

```text
HÌNH L370 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để bơm được nước màu thắng được trọng lực Trái Đất và đẩy dòng nước màu lên tới đỉnh đầu với áp lực tưới nước màu não đủ 100 mi-li-mét thủy ngân, trái tim bắt buộc phải tạo ra một áp suất bơm tại gốc lên tới 280!". Bố cục: Đồ họa dòng nước màu đỏ tươi được bơm vọt lên cao qua động mạch cảnh như một chiếc máy bơm nước tăng áp; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L371</summary>

```text
HÌNH L371 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu huyết áp hạ xuống 120 như người, áp lực cột nước sẽ khiến dòng nước màu không thể leo lên tới hộp sọ, làm con vật ngất xỉu ngay tức khắc!". Bố cục: Đồ họa minh họa não bộ hươu cao cổ bị thiếu nước màu trắng bệch nếu áp lực bơm tim không đủ mạnh; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L372</summary>

```text
HÌNH L372 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để thực hiện được kỳ tích thủy lực đó, tạo hóa đã trang bị cho hươu cao cổ một trái tim quái vật nặng tới 11 kg!". Bố cục: bảng kẹp bệnh án y khoa khổng lồ (clipboard) kẹp trên giá đỡ kim loại, hiển thị 10 hồ sơ bệnh án hoạt hình với nhãn đơn thuốc phát sáng và sóng nhịp tim ECG màu đỏ nhấp nháy (không có chữ, không có số) hiển thị con số 11 kg cùng hình ảnh quả tim khổng lồ đập thình thịch với sức mạnh phi thường; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L373</summary>

```text
HÌNH L373 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thành tâm thất trái của nó dày tới 7,5 cm, dày gấp 3 lần tâm thất người, tạo ra lực bóp mạnh như một chiếc máy bơm piston công nghiệp!". Bố cục: Bản chụp cắt lớp tim hươu cao cổ cho thấy lớp cơ tim tâm thất trái dày cộp đặc quánh chịu được áp lực cực đại; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L374</summary>

```text
HÌNH L374 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thế nhưng câu hỏi hóc búa nhất mà giới sinh lý học từng đau đầu là: Khi hươu cao cổ cúi gập đầu xuống đất uống nước, điều gì ngăn dòng nước màu áp suất cực đại đó tràn xuống làm nổ tung các mạch nước màu não?". Bố cục: Hình ảnh mô phỏng hươu cao cổ dạng hai chân trước cúi đầu xuống mặt nước suối uống nước; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L375</summary>

```text
HÌNH L375 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bởi vì khi cúi đầu, trọng lực sẽ cộng dồn với áp lực bơm tim, đẩy áp suất nước màu tại não vọt lên hơn 400 mi-li-mét thủy ngân trong tích tắc!". Bố cục: Mũi tên đỏ đồ họa hiển thị áp lực thủy tĩnh tăng vọt dồn về phía hộp sọ khi đầu hạ thấp xuống mặt đất; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L376</summary>

```text
HÌNH L376 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và khi đứng thẳng dậy đột ngột, áp lực nước màu lại tụt dốc không phanh, đe dọa gây thiếu nước màu não cục bộ nghiêm trọng!". Bố cục: Đồ thị áp suất nhấp nháy chuyển màu xanh dương biểu thị nguy cơ tụt huyết áp tư thế khi đầu ngẩng cao; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L377</summary>

```text
HÌNH L377 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Câu trả lời nằm ở một tuyệt tác vi mạch sinh học tại đáy hộp sọ mang tên: Mạng lưới mạch kỳ diệu Rete mirabile!". Bố cục: Sơ đồ giải phẫu đáy sọ hươu cao cổ hiển thị một búi mạch nước màu dày đặc đan xen chằng chịt như mạng nhện phát sáng vàng rực; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L378</summary>

```text
HÌNH L378 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngay trước khi dòng nước màu đi vào não bộ, động mạch cảnh phân nhánh thành hàng ngàn tiểu động mạch đàn hồi đan xen chằng chịt như một miếng bọt biển sinh học.". Bố cục: Búi mạch nước màu Rete mirabile hoạt động như một hồ chứa đệm hấp thu và phân tán toàn bộ xung lực áp suất dư thừa; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L379</summary>

```text
HÌNH L379 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mạng lưới này hoạt động chính xác như một bể giảm áp thủy lực, hấp thu và triệt tiêu toàn bộ sóng áp suất cao đột ngột khi con vật cúi đầu!". Bố cục: Đồ họa mô phỏng dòng nước màu áp lực cao bị phân tán chậm rãi qua mạng lưới vi mạch, áp suất tại mô não được duy trì ổn định tuyệt đối; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thông báo khẩn cấp từ tổng đài bệnh viện: Bệnh nhân số một tại Khoa Cấp Cứu Tổng Hợp đang có dấu hiệu quá tải áp suất ổ bụng nghiêm trọng! Đề nghị Bác Sĩ Trưởng Khoa có mặt ngay lập tức!". Bố cục: Chiếc loa phát thanh bằng kim loại gắn trên góc tường rung lên phát ra giọng thông báo khẩn thiết của nhân viên tổng đài trực ban; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L380</summary>

```text
HÌNH L380 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đồng thời, trong các tĩnh mạch cảnh dài 2 m ở cổ có chứa hàng loạt van một chiều đóng kín lại, ngăn không cho nước màu tĩnh mạch chảy ngược về não bộ!". Bố cục: Cận cảnh các van tĩnh mạch một chiều hình bán nguyệt đóng chặt lại ngăn chặn dòng nước màu trào ngược; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L381</summary>

```text
HÌNH L381 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và ở phần chân dưới, lớp da dày cộp và các cân cơ siết chặt hoạt động y hệt như bộ đồ bay chống quá tải trọng trường G-suit của các phi công chiến đấu phản lực!". Bố cục: Đồ họa so sánh lớp da chân căng cứng của hươu cao cổ với bộ đồ bay kháng áp G-suit của phi công tiêm kích; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L382</summary>

```text
HÌNH L382 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ lớp da chân bó chặt này, áp lực nước màu cao không thể làm vỡ mao mạch hay gây phù nề chân dù con vật đứng liên tục suốt cả ngày đêm!". Bố cục: Chú hươu cao cổ sải những bước chân thanh thoát và vững chãi trên mặt đất mà không hề bị sưng phù mắt cá chân; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L383</summary>

```text
HÌNH L383 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cơ quan Hàng Không Vũ Trụ Hoa Kỳ NASA đã nghiên cứu cấu trúc da chân này để chế tạo trang phục kháng áp cho các phi hành gia bay vào vũ trụ!". Bố cục: Bản thiết kế bộ đồ phi hành gia của NASA đặt cạnh sơ đồ cấu trúc da chân hươu cao cổ phát sáng công nghệ cao; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L384</summary>

```text
HÌNH L384 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và về câu hỏi của cô y tá về dây thần kinh thanh quản quặt ngược dài 4,5 m: đó chính là dấu tích tiến hóa kinh điển từ tổ tiên loài cá cổ đại!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười giải thích, vẽ sơ đồ tiến hóa cung động mạch mang cá biến đổi thành quai động mạch chủ ở động vật có vú.
```
</details>

<details><summary>L385</summary>

```text
HÌNH L385 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi cổ của loài hươu ngày càng vươn dài ra qua hàng triệu 5, dây thần kinh bị quai động mạch chủ níu giữ nên phải kéo dài theo thành một vòng lặp ngoạn mục dài 4,5 m!". Bố cục: Sơ đồ chuyển động đồ họa hiển thị dây thần kinh chạy từ não xuống tận tim rồi vòng ngược lên thanh quản ở cổ; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L386</summary>

```text
HÌNH L386 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hơn nữa, vì phải luôn cảnh giác trước các loài thú săn mồi và duy trì áp suất tuần hoàn phức tạp, hươu cao cổ chỉ ngủ chợp mắt khoảng 30 phút mỗi ngày!". Bố cục: Chú hươu cao cổ đứng tựa đầu vào thân cây chợp mắt năm phút giữa bóng đêm thảo nguyên tĩnh mịch; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L387</summary>

```text
HÌNH L387 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Những giấc ngủ ngắn ngủi kéo dài từ 5 đến 10 phút chia làm nhiều lần trong ngày giúp nó vừa phục hồi năng lượng vừa giữ an toàn tuyệt đối!". Bố cục: Biểu đồ theo dõi sóng não giấc ngủ của hươu cao cổ với các chu kỳ ngủ nông ngắn ngủi luân phiên; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L388</summary>

```text
HÌNH L388 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chẩn đoán Khoa Tuần Hoàn Áp Suất Cao của Phòng Cấp Cứu Tạo Hóa: Bệnh nhân sở hữu hệ thống thủy lực tuần hoàn hoàn hảo nhất thế giới động vật!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười gật đầu tán thưởng, xoa nhẹ chiếc cằm dài của quý cô hươu cao cổ đang chớp đôi mắt to tròn có hàng mi rợp bóng.
```
</details>

<details><summary>L389</summary>

```text
HÌNH L389 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đơn thuốc cho bệnh nhân: Một bó cành lá keo tươi non gắn trên giá treo cao 3 m và dặn bệnh nhân mỗi lần cúi đầu uống nước thì nhớ đứng dạng chân chậm rãi thôi nhé!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án treo bó lá keo xanh mướt lên móc cao, chú chú Hươu Cao Cổ hoạt hình cao lêu nghêu có đốm hoa văn nâu vàng, chiếc cổ dài thẳng tắp quấn dải băng đo huyết áp y tế to bản màu đỏ, mắt to hiền từ chớp chớp thích thú vươn chiếc lưỡi dài màu xanh đen dài bốn mươi phân cuốn lấy nhai ngon lành.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Được rồi! Đội ngũ y tế theo tôi bước vào phòng khám số một ngay! Cuộc chiến cứu hộ 10 quái kiệt sinh học chính thức bắt đầu!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án cùng cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng sải những bước chân dứt khoát hướng thẳng về phía cánh cửa phòng khám chuyên khoa đang mở rộng đón chờ.
```
</details>

<details><summary>L390</summary>

```text
HÌNH L390 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiếc lưỡi dài màu xanh đen chứa đầy sắc tố melanin giúp bảo vệ mô lưỡi không bị cháy nắng khi vươn lên đón lá cây giữa trời nắng gắt!". Bố cục: Cận cảnh chiếc lưỡi dài dẻo dai của hươu cao cổ cuốn chặt cành lá keo mà không hề bị gai nhọn đâm thủng; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L391</summary>

```text
HÌNH L391 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bốn giờ sáng! Chỉ còn một tiếng nữa là đến giờ giao ban bình minh! Chúng ta chuyển ngay sang Khoa Da Liễu để kiểm tra vết thương của chú nhím béo tròn nào!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án cất chiếc ống nghe cao áp, cùng y tá rảo bước sang phòng khám da liễu bên cạnh.
```
</details>

<details><summary>L392</summary>

```text
HÌNH L392 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bệnh nhân số 8, mời bước vào phòng khám Khoa Da Liễu và Dị Hóa Sinh! Chú Nhím Lông Nhọn béo tròn đang chầm chậm bước vào với mùi tinh dầu thông ngào ngạt!". Bố cục: chú Nhím Lông Nhọn Bắc Mỹ hoạt hình béo tròn xù xì, toàn thân phủ kín ba mươi ngàn chiếc gai nhọn trắng đen, đang ôm chặt một thân cây gỗ gặm vỏ thuốc, người tỏa mùi tinh dầu thơm nhẹ lặc lè bước vào phòng khám da liễu có kệ tủ chứa đầy các lọ cồn sát trùng và ống nghiệm hóa học, ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đang cầm một chiếc kính lúp soi nổi.
```
</details>

<details><summary>L393</summary>

```text
HÌNH L393 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôi nhìn chú nhím đang ngơ ngác ngồi giữa phòng khám mà vừa thương vừa buồn cười trước sự vụng về của loài động vật này.". Bố cục: chú Nhím Lông Nhọn Bắc Mỹ hoạt hình béo tròn xù xì, toàn thân phủ kín ba mươi ngàn chiếc gai nhọn trắng đen, đang ôm chặt một thân cây gỗ gặm vỏ thuốc, người tỏa mùi tinh dầu thơm nhẹ ngồi bệt xuống đất, ngửa mặt lên nhìn trần nhà rồi gãi đầu bằng chiếc chân sau ngắn cũn cỡn; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L394</summary>

```text
HÌNH L394 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các đồng nghiệp có biết một nghịch lý trớ trêu nhất trong đời sống của loài nhím lông nhọn Bắc Mỹ là gì không?". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười đặt câu hỏi, đưa tay chỉ vào bộ lông gai dựng đứng lởm chởm trên lưng bệnh nhân.
```
</details>

<details><summary>L395</summary>

```text
HÌNH L395 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong khi cả khu rừng và cả phòng cấp cứu ai cũng khiếp sợ 30.000 chiếc gai sắc nhọn trên lưng nó, thì bản thân con nhím lại là kẻ ngã cây nhiều nhất trong vương quốc động vật!". Bố cục: Cảnh một chú nhím đang bám vào cành cây thông cao mười mét gặm vỏ cây, bỗng nhiên cành cây gãy đánh rắc một cái; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L396</summary>

```text
HÌNH L396 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhím lông nhọn Bắc Mỹ là một loài gặm nhấm rất thích ăn vỏ cây thông, vỏ cây bạch dương và chồi non ngọt ngào trên các ngọn cây cao.". Bố cục: Chú nhím dùng các móng vuốt cong khỏe khoắn bám vào thân cây thông phủ đầy tuyết trắng giữa mùa đông; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L397</summary>

```text
HÌNH L397 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thế nhưng thân hình nó thì béo múp míp, 4 chân ngắn ngủn và không hề có đuôi cuốn linh hoạt như loài khỉ hay sóc!". Bố cục: Cận cảnh bốn chiếc chân ngắn và chiếc bụng tròn xoe của chú nhím lắc lư chênh vênh trên cành cây khẳng khiu; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L398</summary>

```text
HÌNH L398 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi mải mê vươn người ra những cành cây nhỏ ngoài rìa tán lá để gặm chồi non, những cú trượt chân tai hại thường xuyên khiến con nhím rơi tự do từ độ cao 10 m xuống đất!". Bố cục: Chú nhím rơi từ trên cành cây cao xuống đất rậm rạp bụi cây gai, lăn lông lốc mấy vòng dưới thảm cỏ rừng; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L399</summary>

```text
HÌNH L399 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cú va chạm mạnh vào đá sỏi hay rễ cây làm gãy vụn hàng chục sợi gai bảo vệ quanh sườn con vật!". Bố cục: Hình ảnh những đoạn gai nhọn bị gãy đôi cắm lộn xộn quanh vùng hông của con nhím sau cú ngã đau đớn; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bệnh nhân số một, mời vào bàn khám! Khỉ Đột Lưng Bạc, cân nặng 200 kg, cơ bắp cuồn cuộn như lực sĩ thể hình hạng nặng!". Bố cục: chú Khỉ Đột Lưng Bạc hoạt hình cơ bắp cuồn cuộn vạm vỡ, mảng lông bạc sáng chói dọc sống lưng, bụng to tròn căng phồng vì chứa đầy lá cây lên men, ngồi xếp bằng trên giường bệnh ôm bụng thở dài ngồi trên giường bệnh khám inox, cơ bắp cánh tay to như cột nhà nổi gân cuồn cuộn, nhưng hai tay lại ôm cái bụng phình to vẻ mặt mếu máo; ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đứng bên cạnh cầm ống nghe.
```
</details>

<details><summary>L400</summary>

```text
HÌNH L400 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và khi rơi xuống mặt đất cứng ngắc từ độ cao của một tòa nhà 3 tầng, điều không thể tránh khỏi là:". Bố cục: Hình ảnh mô phỏng một vài chiếc gai nhọn cắm xuyên qua lớp da dày ở đùi và bụng của chính chú nhím sau cú ngã đau điếng; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L401</summary>

```text
HÌNH L401 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hàng chục chiếc gai sắc nhọn trên lưng nó sẽ bị gãy vụn và cắm phập ngược vào chính các thớ cơ thịt ở đùi, bụng và chân của con nhím!". Bố cục: Các mảnh gai nhọn cắm sâu vào lớp da thịt của chú nhím sau cú va đập mạnh với mặt đất; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L402</summary>

```text
HÌNH L402 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các bạn hãy nhớ lại xem: những chiếc gai này chứa hàng trăm vi ngạnh ngược siêu nhỏ, găm chặt vào thớ thịt và cực kỳ khó rút ra ngoài!". Bố cục: Kính hiển vi quang học phóng đại vi ngạnh ngược của gai nhím đang găm chặt vào mô cơ liên kết; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L403</summary>

```text
HÌNH L403 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu là một con thú săn mồi bị dính gai nhím, vết thương sẽ nhanh chóng bị nhiễm trùng, mưng mủ hoại tử và thậm chí dẫn tới cái chết đau đớn.". Bố cục: Hình ảnh vết thương nhiễm trùng mưng mủ trên mõm một chú chó sói sau khi bị nhím quẫy đuôi trúng; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L404</summary>

```text
HÌNH L404 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vậy tại sao với hàng ngàn chiếc gai tự đâm vào thịt mình sau mỗi cú ngã cây như vậy, loài nhím lại không bao giờ bị nhiễm trùng nước màu hay chết vì hoại tử?". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án dùng kẹp y tế gắp một sợi lông gai nhím đưa vào ống nghiệm chứa dung dịch hóa chất trong suốt để làm phản ứng phân tích.
```
</details>

<details><summary>L405</summary>

```text
HÌNH L405 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thậm chí các vết đâm tự thân này còn lành lặn thần tốc chỉ sau vài ngày mà không để lại bất kỳ di chứng áp xe nào!". Bố cục: Vết đâm trên đùi chú nhím khô miệng nhanh chóng, các tế bào biểu bì mới mọc lên bao bọc an toàn; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L406</summary>

```text
HÌNH L406 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Công trình nghiên cứu kinh điển của giáo sư Uldis Roze về loài nhím Bắc Mỹ đã làm sáng tỏ một cơ chế dược lý phi thường:". Bố cục: Bảng phân tích sắc ký chất béo hiển thị các đỉnh phổ phân tử của các axit béo tự do mạch tự nhiên; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L407</summary>

```text
HÌNH L407 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn bộ bề mặt ngoài của 30.000 chiếc lông gai nhím được bao phủ bởi một lớp màng chất béo mỏng chứa đầy các axit béo tự do có tính kháng sinh cực mạnh!". Bố cục: Kính hiển vi quang học soi lớp màng mỡ mỏng màu vàng óng ánh bao bọc quanh thân sợi gai nhím; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L408</summary>

```text
HÌNH L408 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các axit béo này bao gồm axit butyric, axit hexanoic và nhiều hợp chất lipid tự nhiên có khả năng diệt khuẩn phổ rộng.". Bố cục: Mô hình phân tử hóa học của các chuỗi axit béo tự do phát sáng lấp lánh bao bọc quanh cấu trúc chitin của sợi lông; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L409</summary>

```text
HÌNH L409 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chúng có khả năng tiêu diệt và ức chế sự phát triển của hầu hết các loài vi khuẩn Gram dương, đặc biệt là vi khuẩn tụ cầu vàng Staphylococcus aureus cực kỳ nguy hiểm!". Bố cục: Đồ họa vi sinh vật hiển thị các tế bào vi khuẩn tụ cầu vàng bị lớp axit béo trên gai nhím phá hủy màng tế bào vỡ vụn; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôi nhìn vào các chỉ số thể chất ghi trên phiếu tiếp nhận mà không khỏi trầm trồ trước sức mạnh phi thường của loài linh trưởng vĩ đại này.". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án cầm bảng theo dõi chỉ số sinh tồn, ngước nhìn khối cơ bắp vai đồ sộ của chú khỉ đột đang ngồi co ro trên giường.
```
</details>

<details><summary>L410</summary>

```text
HÌNH L410 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây thực chất là một lớp kem bôi kháng sinh tự nhiên mà tạo hóa đã hào phóng bôi sẵn lên từng chiếc mũi kim tiêm trên lưng con nhím!". Bố cục: Hình ảnh minh họa sợi gai nhím được nhúng vào một lớp sáp kháng khuẩn tự nhiên trước khi mọc ra ngoài lớp da; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L411</summary>

```text
HÌNH L411 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi khi con nhím trượt chân ngã cây và tự đâm trúng gai của chính mình, lớp kháng sinh này sẽ lập tức khử trùng vết thương ngay tại chỗ!". Bố cục: Vết đâm trên da nhím không hề bị sưng tấy mưng mủ, các tế bào biểu bì mau chóng phục hồi và lành lặn thần tốc; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L412</summary>

```text
HÌNH L412 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó hoạt động như một hệ thống an toàn tự động, đảm bảo rằng nếu vũ khí tự vệ phản chủ thì chủ nhân của nó vẫn hoàn toàn bình an vô sự!". Bố cục: chú Nhím Lông Nhọn Bắc Mỹ hoạt hình béo tròn xù xì, toàn thân phủ kín ba mươi ngàn chiếc gai nhọn trắng đen, đang ôm chặt một thân cây gỗ gặm vỏ thuốc, người tỏa mùi tinh dầu thơm nhẹ thản nhiên rũ lông một cái đánh xào xạc, không hề tỏ ra đau đớn hay khó chịu trước vết gai cũ; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L413</summary>

```text
HÌNH L413 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lớp sáp mỡ này được tiết ra liên tục từ các tuyến bã nhờn chuyên biệt nằm ngay cạnh nang lông dưới lớp da dày!". Bố cục: Sơ đồ giải phẫu tuyến bã nhờn nang lông nhím tiết dịch mỡ kháng sinh bao bọc thân sợi gai; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L414</summary>

```text
HÌNH L414 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa hết đâu nhé! Lớp mỡ kháng sinh này còn phát tán một mùi hương hăng nồng đặc trưng vào không khí mỗi khi nhím dựng đứng các sợi gai lên cảnh cáo kẻ thù!". Bố cục: Luồng phân tử mùi hương màu tím nhạt tỏa ra từ các sợi gai dựng đứng cảnh báo các loài thú ăn thịt xung quanh; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L415</summary>

```text
HÌNH L415 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đó là lời nhắn nhủ rõ ràng của tự nhiên gửi tới các loài săn mồi: Tránh xa ra! Ở đây có 30.000 mũi kim tiêm tẩm thuốc tê và kháng sinh sẵn sàng phục vụ các bạn đấy!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án nháy mắt mỉm cười nhìn chú chú Nhím Lông Nhọn Bắc Mỹ hoạt hình béo tròn xù xì, toàn thân phủ kín ba mươi ngàn chiếc gai nhọn trắng đen, đang ôm chặt một thân cây gỗ gặm vỏ thuốc, người tỏa mùi tinh dầu thơm nhẹ đang tò mò ngửi chiếc ống nghe trên bàn khám.
```
</details>

<details><summary>L416</summary>

```text
HÌNH L416 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôi đã lấy mẫu chất béo trên lưng bệnh nhân để nuôi cấy vi sinh vật trong đĩa thạch thí nghiệm suốt 24 giờ qua.". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án giơ chiếc đĩa petri thí nghiệm trong suốt lên dưới ánh đèn soi kiểm tra độ tinh sạch của mẫu cấy.
```
</details>

<details><summary>L417</summary>

```text
HÌNH L417 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và kết quả thu được hoàn toàn vô trùng 100%! Không có một khóm vi khuẩn gây hại nào có thể sống sót trên bộ lông gai này!". Bố cục: Đĩa thạch trong veo không hề có một vết vẩn đục hay khuẩn lạc nào phát triển chứng minh hoạt tính kháng sinh tuyệt hảo; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L418</summary>

```text
HÌNH L418 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vòng vô khuẩn xung quanh mẫu gai nhím trên đĩa thạch thậm chí còn rộng hơn cả vòng ức chế của thuốc kháng sinh penicillin thông thường!". Bố cục: Thước đo y tế đo đường kính vòng vô khuẩn trong suốt quanh sợi gai nhím vượt trội so với đĩa giấy thấm penicillin; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L419</summary>

```text
HÌNH L419 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà nghiên cứu còn thử nghiệm với các chủng vi nấm gây bệnh ngoài da cứng đầu nhất như nấm mốc sợi và nấm men candida.". Bố cục: Đĩa thạch thí nghiệm vi nấm bị màng axit béo tự nhiên từ gai nhím tiêu diệt hoàn toàn không thể phát triển; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Theo các nghiên cứu cơ sinh học hiện đại, một cú đấm toàn lực của một con khỉ đột đực trưởng thành có lực tác động lên tới 1300 kg!". Bố cục: Bức tranh giải phẫu cơ xương tay của khỉ đột với các bó cơ delta và cơ nhị đầu đồ sộ chịu lực va đập cực đại; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L420</summary>

```text
HÌNH L420 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và kết quả thật đáng kinh ngạc: Lớp axit béo tự nhiên trên gai nhím ức chế tới 90 9 phần trăm sự phát triển của các bào tử nấm mốc!". Bố cục: Biểu đồ tỷ lệ ức chế vi nấm chạm mốc chín mươi chín phần trăm phát sáng màu xanh lá cây hy vọng; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L421</summary>

```text
HÌNH L421 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Điều này lý giải tại sao dù sống ở những vùng đầm lầy ẩm ướt hay rừng rậm nhiệt đới ẩm thấp, da của loài nhím không bao giờ bị viêm da hay nấm ngứa!". Bố cục: Chú nhím lông nhọn thong dong đi qua thảm rêu ẩm ướt đầy nấm mốc trong rừng già mà không hề bị tổn thương da; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L422</summary>

```text
HÌNH L422 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó sở hữu một hệ sinh thái da hoàn toàn tự cân bằng và tự kháng khuẩn độc nhất vô nhị trong lớp động vật có vú!". Bố cục: Hình ảnh mô phỏng cấu trúc vi sinh vật có lợi trên bề mặt da nhím bảo vệ nang lông khỏi mọi tác nhân gây hại; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L423</summary>

```text
HÌNH L423 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lớp sáp kháng sinh này thậm chí còn không bị rửa trôi bởi nước mưa hay băng tuyết suốt cả mùa đông lạnh giá!". Bố cục: Giọt nước mưa trượt tròn lăn khỏi bề mặt sợi gai nhím mà không làm phai mờ lớp màng kháng sinh bao phủ; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L424</summary>

```text
HÌNH L424 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thật là một phòng thí nghiệm dược phẩm di động hoàn mỹ được tích hợp ngay trên lưng một chú gặm nhấm béo tròn!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án gật gù khen ngợi, cất chiếc đĩa thạch vào tủ ủ ấm vi sinh.
```
</details>

<details><summary>L425</summary>

```text
HÌNH L425 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chẩn đoán Khoa Da Liễu của Phòng Cấp Cứu Tạo Hóa: Bệnh nhân sở hữu nhà máy sản xuất thuốc mỡ kháng sinh xịn nhất thế giới động vật!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án gật đầu hài lòng, xoa nhẹ cái mũi ươn ướt của chú nhím và ký tên vào hồ sơ bệnh án số tám.
```
</details>

<details><summary>L426</summary>

```text
HÌNH L426 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cho phép xuất viện! Nhưng dặn bệnh nhân lần sau leo trèo hái quả thì nhớ thắt dây an toàn cẩn thận nhé, ngã hoài làm bệnh viện tốn bông băng lắm đấy!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án trao chiếc túi đựng vài củ cà rốt tươi ngon cho chú nhím làm quà xuất viện, chú nhím ôm chặt củ cà rốt mừng rỡ lon ton bước ra ngoài.
```
</details>

<details><summary>L427</summary>

```text
HÌNH L427 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Anh bạn nhím hãy nhớ rằng kháng sinh dù xịn đến mấy cũng không thể chữa lành bệnh lười đeo dây an toàn đâu nhé!". Bố cục: Chú chú Nhím Lông Nhọn Bắc Mỹ hoạt hình béo tròn xù xì, toàn thân phủ kín ba mươi ngàn chiếc gai nhọn trắng đen, đang ôm chặt một thân cây gỗ gặm vỏ thuốc, người tỏa mùi tinh dầu thơm nhẹ ôm chặt củ cà rốt gật gù đắc ý, lon ton đi theo lối hành lang riêng biệt; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L428</summary>

```text
HÌNH L428 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giờ thì chuyển ngay sang phòng khám cuối cùng: Khoa Tâm Thần và Rối Loạn Hành Vi! Bệnh nhân số 9 đang đứng như tượng đá ngoài hành lang!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án cởi chiếc áo găng tay da liễu, bước thẳng về phía cửa phòng khám tâm thần nơi chú cò mỏ giày đang đợi.
```
</details>

<details><summary>L429</summary>

```text
HÌNH L429 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bốn giờ 30 phút sáng. Căn phòng khám Khoa Tâm Thần và Rối Loạn Hành Vi chìm trong bầu không khí yên ắng đến rợn người.". Bố cục: Căn phòng khám có ánh sáng mờ ảo, chú Cò Mỏ Giày hoạt hình lông xám tro, dáng đứng sừng sững bất động như tượng đá, chiếc mỏ khổng lồ màu vàng xám phình to hình chiếc guốc gỗ, ánh mắt lạnh như tiền đứng canh cửa phòng cấp cứu đứng sừng sững giữa phòng như một bức tượng điêu khắc bằng đá hoa cương xám, ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án ngồi đối diện trên chiếc ghế xoay.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lực va chạm khủng khiếp đó thừa sức làm bẹp dúm phần đầu của một chiếc xe hơi 4 chỗ hoặc bẻ gãy một thân cây gỗ lim trong nháy mắt!". Bố cục: Hình ảnh mô phỏng cú đấm uy lực của khỉ đột làm nứt toác tấm bia thử nghiệm lực cơ học trong phòng thí nghiệm; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L430</summary>

```text
HÌNH L430 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bên ngoài cửa sổ, những cơn gió lạnh rít nhẹ qua khe kính, chỉ có tiếng kim đồng hồ tíc tắc gõ nhịp chậm rãi giữa căn phòng tĩnh mịch.". Bố cục: Chiếc đồng hồ treo tường tròn xoe bằng đồng thau nhảy từng giây một, bóng kim đồng hồ in dài trên bức tường xám; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L431</summary>

```text
HÌNH L431 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bệnh nhân số 9: Cò Mỏ Giày, sinh vật thời tiền sử còn sót lại giữa những đầm lầy hoang sơ miền Trung châu Phi xa xôi.". Bố cục: Toàn cảnh chú chú Cò Mỏ Giày hoạt hình lông xám tro, dáng đứng sừng sững bất động như tượng đá, chiếc mỏ khổng lồ màu vàng xám phình to hình chiếc guốc gỗ, ánh mắt lạnh như tiền đứng canh cửa phòng cấp cứu cao một mét hai, sải cánh dài hơn hai mét rưỡi, bộ lông màu xám tro cổ kính như một con khủng long bay bước ra từ kỷ Phấn Trắng; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L432</summary>

```text
HÌNH L432 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Từ lúc nhập viện lúc 12 giờ đêm cho tới tận thời điểm này, bệnh nhân này không hề nhấc chân lên một lần nào!". Bố cục: Cận cảnh đôi chân dài khẳng khiu với những chiếc ngón chân xòe rộng bám chặt xuống sàn gạch men không hề lay chuyển một mi-li-mét; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L433</summary>

```text
HÌNH L433 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hai mắt màu vàng nhạt nhìn trừng trừng vào một điểm vô định trên tường, mi mắt hoàn toàn không chớp, nhịp thở chậm đến mức mắt thường không thể nhận biết được!". Bố cục: Cận cảnh đôi mắt lạnh lùng không chút cảm xúc của cò mỏ giày, chiếc mỏ guốc khổng lồ dài hai mươi tư xăng-ti-mét chúc xuống đầy uy nghi; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L434</summary>

```text
HÌNH L434 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiếc mỏ guốc khổng lồ chúc xuống góc 45 độ, toát ra một vẻ mặt nghiêm nghị và đăm chiêu như một triết gia cổ đại đang trầm tư mặc tưởng.". Bố cục: Gương mặt vuông vức bằng chất sừng cứng ngắc của chú cò mỏ giày, đầu có một túm lông tơ dựng ngược ngộ nghĩnh; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L435</summary>

```text
HÌNH L435 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bác sĩ trưởng khoa ơi em mang hồ sơ vào mà 2 hàm răng em va vào nhau lập cập!". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng rón rén bước vào phòng, tay ôm tập hồ sơ nép sát vào lưng bác sĩ thì thầm lo sợ.
```
</details>

<details><summary>L436</summary>

```text
HÌNH L436 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Có phải con chim khổng lồ này bị trầm cảm phân liệt giai đoạn cuối hay bị đông cứng cơ thể kiểu mèo liệt cứng không bác sĩ?". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng ngước nhìn đôi mắt màu vàng nhạt bất động của con chim, hai tay xoa xoa bắp tay vì ớn lạnh; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L437</summary>

```text
HÌNH L437 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó cứ nhìn em trừng trừng từ nửa đêm đến giờ, em cảm giác như linh hồn mình sắp bị chiếc mỏ kia nuốt chửng mất rồi bác sĩ ơi!". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng run rẩy giơ chiếc đèn soi phản xạ đồng tử ra trước mắt con chim nhưng đồng tử của nó không hề co giãn; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L438</summary>

```text
HÌNH L438 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và chân cẳng của nó trắng phau như quét vôi thế kia có phải bị nấm da hoại tử giai đoạn nặng không bác sĩ ơi?". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng chỉ ngón tay run rẩy vào đôi chân dài dính đầy vệt trắng kỳ lạ của chú chim; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L439</summary>

```text
HÌNH L439 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không hề có chứng liệt cứng hay trầm cảm nào ở đây cả cô y tá thân mến!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đứng dậy bước chậm rãi quanh chú chim, quan sát kỹ từng đường nét giải phẫu trên chiếc đầu to lớn khác thường.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Xương khớp tay chân của khỉ đột dày gấp 3 lần xương người, mật độ khoáng chất cao đến mức gần như miễn nhiễm với các chấn thương gãy xương thông thường.". Bố cục: Bản chụp X-quang xương cẳng tay của khỉ đột sáng trắng cho thấy cấu trúc vỏ xương đặc quánh và các khớp nối vững chãi; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L440</summary>

```text
HÌNH L440 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây chính là trạng thái thiền định săn mồi đỉnh cao của kẻ phục kích kiên nhẫn nhất thế giới tự nhiên hoang dã!". Bố cục: Sơ đồ thần kinh trung ương của cò mỏ giày hiển thị các vùng kiểm soát phản xạ ức chế vận động hoạt động ở mức tối ưu; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L441</summary>

```text
HÌNH L441 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vệt trắng trên chân nó thực chất là thói quen xả nước tiểu làm mát chân độc đáo mang tên urohidrosis!". Bố cục: Đồ họa sinh lý học hiển thị nước bay hơi từ bề mặt chân chim giúp hạ nhiệt độ dòng nước màu tuần hoàn khi trời nóng bức; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L442</summary>

```text
HÌNH L442 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nước bay hơi sẽ làm mát các mạch nước màu ở chân, giúp nó duy trì thân nhiệt ổn định giữa những đầm lầy châu Phi nóng tới 4 mươi độ C!". Bố cục: Chú cò mỏ giày đứng giữa đầm lầy nắng gắt, làn gió thổi qua làm mát đôi chân dài khẳng khiu; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L443</summary>

```text
HÌNH L443 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và khi tôi vừa bước tới trước mặt nó cách 0,5 m... Cạch! Cạch! Cạch! Tách tách tách tách tách!". Bố cục: Đột nhiên chú Cò Mỏ Giày hoạt hình lông xám tro, dáng đứng sừng sững bất động như tượng đá, chiếc mỏ khổng lồ màu vàng xám phình to hình chiếc guốc gỗ, ánh mắt lạnh như tiền đứng canh cửa phòng cấp cứu ngửa cổ lên trời rồi đập liên hồi hai hàm mỏ vào nhau với tốc độ chóng mặt, tạo nên một chuỗi âm thanh đanh thép rền vang khắp phòng khám!
```
</details>

<details><summary>L444</summary>

```text
HÌNH L444 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tiếng va đập của 2 hàm mỏ guốc khổng lồ vang lên rầm rầm như một khẩu súng máy liên thanh đang xả đạn liên hồi giữa chiến hào!". Bố cục: Sóng âm thanh cực mạnh phát ra từ chiếc mỏ làm rung chuyển cửa kính phòng khám, các y tá giật bắn người bịt chặt hai tai; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L445</summary>

```text
HÌNH L445 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chuỗi âm thanh kim loại đanh thép xé toạc bầu không khí yên tĩnh, làm rung rinh cả những chiếc chai lọ thủy tinh trên giá thuốc!". Bố cục: Các dụng cụ y tế trên khay inox nảy nhẹ lên theo từng nhịp gõ mỏ vang dội của chú chim; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L446</summary>

```text
HÌNH L446 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đó chính là nghi thức gõ mỏ bill-clattering độc nhất vô nhị của loài cò mỏ giày!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án bình tĩnh giơ chiếc máy đo độ ồn decibel lên đo cường độ âm thanh của tràng gõ mỏ vừa dứt.
```
</details>

<details><summary>L447</summary>

```text
HÌNH L447 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nghiên cứu của tiến sĩ Tomita công bố trên Tạp Chí Tập Tính Học Động Vật đã đo được:". Bố cục: Máy đo âm thanh kỹ thuật số hiển thị các đỉnh sóng âm thanh hình gai nhọn chạm ngưỡng cảnh báo độ ồn cực đại; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L448</summary>

```text
HÌNH L448 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cường độ âm thanh của tràng gõ mỏ này có thể đạt ngưỡng lên tới 115 dB! Ngang ngửa với tiếng còi xe cứu thương hụ còi ở cự ly gần!". Bố cục: bảng kẹp bệnh án y khoa khổng lồ (clipboard) kẹp trên giá đỡ kim loại, hiển thị 10 hồ sơ bệnh án hoạt hình với nhãn đơn thuốc phát sáng và sóng nhịp tim ECG màu đỏ nhấp nháy (không có chữ, không có số) bật sáng con số 115 dB cùng biểu tượng khẩu súng máy phát ra sóng âm thanh nhấp nháy đỏ rực; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L449</summary>

```text
HÌNH L449 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tiếng gõ mỏ đanh thép này có thể truyền xa hàng cây số qua những thảm cói đầm lầy rậm rạp, dùng để chào hỏi bạn tình và xua đuổi các đối thủ xâm phạm lãnh thổ!". Bố cục: Cảnh đầm lầy châu Phi mênh mông lúc rạng đông, tiếng gõ mỏ vang rền làm bầy linh dương và chim nước bay toán loạn; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thế nhưng hiện tại, cỗ máy chiến đấu vô địch của những cánh rừng mưa nhiệt đới này lại đang nằm co quắp rên rỉ như một đứa trẻ con!". Bố cục: chú Khỉ Đột Lưng Bạc hoạt hình cơ bắp cuồn cuộn vạm vỡ, mảng lông bạc sáng chói dọc sống lưng, bụng to tròn căng phồng vì chứa đầy lá cây lên men, ngồi xếp bằng trên giường bệnh ôm bụng thở dài nằm nghiêng trên giường bệnh, ôm hai đầu gối vào ngực, miệng thở hắt ra từng hơi vẻ bất lực; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L450</summary>

```text
HÌNH L450 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiếc mỏ khổng lồ dài tới 24 cm của nó kết thúc bằng một chiếc móc câu sắc lẹm như mũi mác thép!". Bố cục: Hình ảnh phóng to chóp mỏ của cò mỏ giày với chiếc móc cong nhọn hoắt có thể chém đứt đôi một con cá phổi dài một mét; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L451</summary>

```text
HÌNH L451 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi kẹp chặt lại, lực ép cơ hàm của nó thừa sức nghiền nát lớp vảy giáp cứng như đá của loài cá phổi châu Phi và rùa đầm lầy trong nháy mắt!". Bố cục: Bản vẽ cơ hàm của cò mỏ giày với các bó cơ nhai khổng lồ gắn vào gờ xương hộp sọ tạo lực kẹp nghiền nát con mồi; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L452</summary>

```text
HÌNH L452 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đôi mắt của nó có màng chớp trong suốt nhắm lại theo chiều ngang trong đúng 1/1000 giây khi tấn công con mồi dưới bùn lầy để bảo vệ giác mạc!". Bố cục: Cận cảnh đôi mắt chim với màng chớp trong suốt đóng mở thần tốc bảo vệ mắt khỏi bùn đất và răng cá sắc nhọn; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L453</summary>

```text
HÌNH L453 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bàn chân khổng lồ của nó có sải ngón dài tới 30 cm, phân tán áp lực giúp con chim bước đi thanh thoát trên thảm bèo nổi mà không bị chìm!". Bố cục: Cận cảnh bàn chân bốn ngón xòe rộng của cò mỏ giày đạp vững chãi trên lớp thảm thực vật nổi giữa đầm lầy; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L454</summary>

```text
HÌNH L454 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng phía sau sự kiên nhẫn và uy lực đáng sợ đó là một hiện tượng sinh học khốc liệt làm xót xa lòng người: Hiện tượng sát hại con thứ Cainism!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án trầm giọng, ánh mắt thoáng buồn khi lật giở trang tài liệu sinh thái học của loài chim này.
```
</details>

<details><summary>L455</summary>

```text
HÌNH L455 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nghiên cứu thực địa của Mullers và Amar trên Tạp Chí Điểu Học The Ostrich đã ghi nhận:". Bố cục: Hình ảnh tư liệu trắng đen về chiếc tổ chim khổng lồ nằm cô độc giữa đầm lầy Bangweulu hoang vắng; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L456</summary>

```text
HÌNH L456 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cò mỏ giày mẹ thường đẻ 2 quả trứng trong mỗi mùa sinh sản để dự phòng trường hợp quả trứng đầu tiên bị hỏng hoặc con non bị chết yểu.". Bố cục: Chiếc tổ chim khổng lồ bằng cỏ khô nổi giữa đầm lầy, bên trong có hai chú chim non lông tơ màu xám vừa nở; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L457</summary>

```text
HÌNH L457 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thế nhưng nguồn thức ăn ở các đầm lầy nhiệt đới luôn biến động vô cùng khan hiếm, chim bố mẹ chỉ đủ sức kiếm mồi nuôi sống một đứa con duy nhất.". Bố cục: Chim bố mẹ bay về tổ ngậm một con cá nhỏ, hai chú chim non há mỏ tranh giành thức ăn quyết liệt; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L458</summary>

```text
HÌNH L458 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Con non đầu lòng to lớn hơn sẽ liên tục dùng chiếc mỏ nhọn mổ và xua đuổi đứa em nhỏ yếu ớt ra khỏi tổ cho tới khi con thứ chết đói trong sự bất lực của chim mẹ!". Bố cục: Con non đầu lòng to lớn hơn liên tục mổ và xua đuổi đứa em nhỏ yếu ớt ra khỏi tổ cho tới khi con thứ chết đói trong sự bất lực của chim mẹ; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L459</summary>

```text
HÌNH L459 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đó là sự tàn nhẫn đến lạnh lùng của quy luật chọn lọc tự nhiên: thà bảo toàn một cá thể khỏe mạnh nhất còn hơn để cả 2 cùng chết đói giữa vùng đầm lầy khắc nghiệt!". Bố cục: Cảnh chim non đầu lòng giương đôi cánh xám đứng kiêu hãnh trên tổ dưới ánh hoàng hôn đầm lầy; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gương mặt nhăn nhó tội nghiệp của chú khỉ đột to lớn làm cô y tá vừa buồn cười vừa thương cảm vô cùng!". Bố cục: Cận cảnh gương mặt nhiều nếp nhăn của chú khỉ đột đang chớp mắt cầu cứu bác sĩ trưởng khoa; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L460</summary>

```text
HÌNH L460 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mặc dù sở hữu sải cánh rộng tới 2,5 m, nhưng loài cò mỏ giày rất hiếm khi bay lượn trên bầu trời cao.". Bố cục: Chú cò mỏ giày dang rộng đôi cánh dài hai mét rưỡi bay là là trên mặt nước đầm lầy phủ đầy hoa súng tím; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L461</summary>

```text
HÌNH L461 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Do trọng lượng cơ thể nặng nề từ 4 đến 7 cân, mỗi lần cất cánh nó phải chạy đà vài bước nặng nhọc trên thảm bèo nổi tương tự một chiếc máy bay ném bom hạng nặng!". Bố cục: Con chim sải chân chạy đà trên thảm cỏ nước, đập cánh mạnh mẽ tạo nên những luồng gió rẽ sóng nước xung quanh; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L462</summary>

```text
HÌNH L462 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó chỉ bay những chặng ngắn từ 100 đến 500 mét giữa các vũng nước đầm lầy để tìm kiếm những đàn cá phổi ngon lành!". Bố cục: Cảnh cò mỏ giày bay là là trên những ngọn cây cói lau sậy, đôi cánh đập chậm rãi nhưng đầy uy lực; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L463</summary>

```text
HÌNH L463 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi khi thời tiết quá oi bức, ngoài thói quen xả nước làm mát chân, nó còn ngậm từng ngụm nước lớn trong chiếc mỏ guốc rồi tưới ướt đẫm các quả trứng trong tổ để duy trì độ ẩm tối ưu!". Bố cục: Chú cò mỏ giày dùng chiếc mỏ guốc múc nước suối tưới nhẹ nhàng lên chiếc tổ có hai quả trứng trắng ngà giữa đầm lầy; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L464</summary>

```text
HÌNH L464 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bệnh nhân Cò Mỏ Giày không hề có bất kỳ rối loạn tâm thần nào! Mọi hành vi bất động và tiếng gõ mỏ súng máy đều là bản năng sinh tồn hoàn mỹ của kẻ thống trị đầm lầy!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án khẽ cúi đầu chào theo nghi thức cúi chào bill-bobbing của loài chim này, chú chú Cò Mỏ Giày hoạt hình lông xám tro, dáng đứng sừng sững bất động như tượng đá, chiếc mỏ khổng lồ màu vàng xám phình to hình chiếc guốc gỗ, ánh mắt lạnh như tiền đứng canh cửa phòng cấp cứu cũng từ từ gật đầu đáp lễ một cách lịch thiệp lạ kỳ.
```
</details>

<details><summary>L465</summary>

```text
HÌNH L465 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chẩn đoán của Phòng Cấp Cứu Tạo Hóa: Tinh thần thép, sự kiên nhẫn vô địch và phản xạ săn mồi đạt cấp độ sát thủ hoàn hảo!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án ký tên đóng dấu xuất viện vào hồ sơ bệnh án số chín, khẽ mỉm cười nhìn chú chim cúi đầu chào từ biệt.
```
</details>

<details><summary>L466</summary>

```text
HÌNH L466 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn bộ 10 ca bệnh nhân dị thường của ca trực đêm đã được khám nghiệm toàn diện và chuẩn xác 100%!". Bố cục: Mười tập hồ sơ bệnh án dày cộp được xếp ngay ngắn trong chiếc cặp da màu nâu của Bác Sĩ Trưởng Khoa; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L467</summary>

```text
HÌNH L467 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chúng ta đã vượt qua ca trực đêm cam go nhất mà không hề có bất kỳ ca tử vong hay biến chứng y khoa nào xảy ra!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án siết chặt khóa chiếc cặp da y tế, ánh mắt rạng ngời niềm hãnh diện của người thầy thuốc; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L468</summary>

```text
HÌNH L468 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đồng hồ điểm đúng 5 giờ sáng! Đã đến lúc toàn thể y bác sĩ tập hợp tại hội trường lớn cho buổi giao ban kịch tính nhất lịch sử!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án tháo ống nghe, cùng y tá sải bước về phía hội trường trung tâm của bệnh viện.
```
</details>

<details><summary>L469</summary>

```text
HÌNH L469 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm giờ sáng. Căn phòng họp giao ban lớn của bệnh viện rực sáng ánh đèn chùm pha lê cổ kính.". Bố cục: Toàn cảnh phòng họp giao ban lớn của bệnh viện với bàn hội nghị bằng gỗ gụ hình bầu dục dài mười mét, các giáo sư và bác sĩ nội trú ngồi kín các dãy ghế; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Y tá, đặt ống nghe vào góc phần tư ổ bụng bên phải cho tôi! Cẩn thận kẻo anh chàng giật mình lại tung một đòn thì bay cả phòng khám đấy!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án ấn đầu ống nghe kim loại lạnh ngắt vào bụng khỉ đột, mắt chăm chú lắng nghe từng tiếng động bên trong.
```
</details>

<details><summary>L470</summary>

```text
HÌNH L470 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn thể hội đồng y khoa và kíp trực đêm tề tựu đông đủ quanh chiếc bàn dài bằng gỗ gụ, trên tay mỗi người là một tách cà phê nóng hổi.". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đứng ở đầu bàn hội nghị trong chiếc áo blouse trắng tinh tươm, hai tay chống lên mặt bàn gỗ, ánh mắt rạng ngời niềm tự hào nghề nghiệp.
```
</details>

<details><summary>L471</summary>

```text
HÌNH L471 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôi trịnh trọng mở chiếc cặp da màu nâu, xếp 10 tập hồ sơ bệnh án đã được ký tên và đóng dấu đỏ chót ngay ngắn lên mặt bàn trước mặt hội đồng.". Bố cục: Mười tập hồ sơ bệnh án bìa cứng dập nổi dấu mộc đỏ ĐÃ XỬ LÝ XUẤT SẮC xếp thẳng hàng trên bàn hội nghị; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L472</summary>

```text
HÌNH L472 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thưa toàn thể các đồng nghiệp và các bác sĩ nội trú thân mến: Chúng ta vừa trải qua ca trực đêm điên rồ và kỳ diệu nhất trong toàn bộ lịch sử y học!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án cất giọng vang ấm đĩnh đạc, nhìn quanh phòng họp nơi các bác sĩ trẻ đang lắng nghe như nuốt từng lời.
```
</details>

<details><summary>L473</summary>

```text
HÌNH L473 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mười bệnh nhân, 10 căn bệnh tưởng chừng như vô phương cứu chữa hay dị tật quái gở, thực chất lại là 10 phát minh cơ thể học phi thường nhất của tạo hóa!". Bố cục: Màn hình chiếu máy chiếu rọi sáng hình ảnh mười loài vật kỳ dị với các đường nét giải phẫu vàng rực rỡ; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L474</summary>

```text
HÌNH L474 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy cùng tôi điểm lại bản tóm tắt lâm sàng 10 ca bệnh độc nhất vô nhị đêm nay:". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án bật máy chiếu slide cổ điển, từng hình ảnh minh họa ngộ nghĩnh hiện lên trên tấm phông trắng lớn.
```
</details>

<details><summary>L475</summary>

```text
HÌNH L475 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Anh chàng Khỉ Đột Lưng Bạc không hề bị viêm dạ dày ruột, mà mang trong bụng một nhà máy lên men vi sinh vật tạo ra 70% năng lượng cơ bắp!". Bố cục: Slide chiếu hình ảnh biếm họa chú khỉ đột cơ bắp lực lưỡng đang ôm cái bụng phình to đầy tự hào bên cạnh biểu đồ calo; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L476</summary>

```text
HÌNH L476 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chú Nhện Lặn Chuông tí hon không hề muốn tự tử, mà đã tự dệt nên chiếc bình dưỡng khí nano cho phép nó thở oxy dưới nước suốt 24 giờ!". Bố cục: Slide chiếu chú nhện lặn chuông bơi lội ung dung bên trong quả cầu khí bạc dưới đáy hồ; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L477</summary>

```text
HÌNH L477 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chú Cá Thòi Lòi không hề bị gãy xương chậu, mà dùng vây ngực làm chân đi bộ và ngậm nước trong mang để chinh phục đất cạn suốt 90% cuộc đời!". Bố cục: Slide chiếu chú cá thòi lòi giương đôi mắt kính tiềm vọng đứng chống vây hiên ngang trên rễ đước; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L478</summary>

```text
HÌNH L478 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cô Ong Bắp Cày Ngọc không hề dùng bùa ngải ma thuật, mà thực hiện ca phẫu thuật thần kinh chính xác tuyệt đối để điều khiển con gián to gấp 6 lần mình!". Bố cục: Slide chiếu cô ong ngọc bích lấp lánh dắt chú gián đi dạo như dắt cún con; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L479</summary>

```text
HÌNH L479 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chú Cá Mặt Trăng 2 tấn không hề bị liệt hàm méo miệng, mà sở hữu bộ não 4 g siêu tiết kiệm năng lượng và đẻ tới 300 triệu trứng mỗi mùa!". Bố cục: Slide chiếu cá mặt trăng tròn dẹt đang nằm phơi nắng trên mặt biển sưởi ấm thân nhiệt; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôi áp đầu ống nghe vào lớp da bụng dày cộp căng tròn như chiếc trống đồng của bệnh nhân.". Bố cục: Cận cảnh đầu ống nghe y tế bằng kim loại sáng loáng áp sát vào lớp da lông đen nhánh của khỉ đột; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L480</summary>

```text
HÌNH L480 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chàng Vẹt Kakapo béo tròn không hề bị dị tật cánh cụt, mà đã hoàn thiện chiến lược sinh tồn đi bộ dưới mặt đất và tỏa mùi thơm thảo mộc mê đắm!". Bố cục: Slide chiếu chú vẹt kakapo lông xanh rêu đang lon ton đi bộ trên thảm rêu New Zealand; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L481</summary>

```text
HÌNH L481 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chú Lợn Hươu Babirusa không hề sở hữu vũ khí hi sinh bảo vệ tổ ngớ ngẩn, mà chiếc nanh cong 40 cm là tấm khiên hộ mệnh và chiếc vương miện kiêu hãnh của tình yêu!". Bố cục: Slide chiếu chú lợn babirusa đứng thẳng trên hai chân sau khoe cặp nanh uốn lượn trước ánh bình minh rừng nhiệt đới; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L482</summary>

```text
HÌNH L482 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quý cô Hươu Cao Cổ không hề bị cơn bão cao huyết áp ác tính, mà mức huyết áp 280 là điều kiện sống còn để nuôi dưỡng bộ não cách mặt đất 5 m!". Bố cục: Slide chiếu hệ thống bơm tăng áp thủy lực và mạng lưới mạch Rete mirabile dưới đáy sọ hươu cao cổ; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L483</summary>

```text
HÌNH L483 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chú Nhím Lông Nhọn không hề bị nhiễm trùng sau mỗi cú ngã cây, mà sở hữu lớp sáp kháng sinh tự nhiên diệt khuẩn tụ cầu vàng hoàn hảo nhất Trái Đất!". Bố cục: Slide chiếu sợi lông nhím bọc màng mỡ kháng sinh óng ánh vàng tiêu diệt vi khuẩn; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L484</summary>

```text
HÌNH L484 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và chú Cò Mỏ Giày không hề bị trầm cảm hay đông cứng tâm thần, mà trạng thái bất động là tuyệt đỉnh thiền định của sát thủ đầm lầy với tiếng gõ mỏ 115 dB!". Bố cục: Slide chiếu chú cò mỏ giày uy nghi với chiếc mỏ guốc khổng lồ ngửa cổ lên trời gõ mỏ súng máy; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L485</summary>

```text
HÌNH L485 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi một nét giải phẫu kỳ dị của chúng đều là một giải pháp cơ sinh học thiên tài mà hàng trăm viện nghiên cứu công nghệ hiện đại nhất của loài người vẫn đang phải miệt mài học hỏi!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đập tay nhẹ lên bàn, ánh mắt bừng sáng trước vẻ đẹp trí tuệ vô tận của tự nhiên.
```
</details>

<details><summary>L486</summary>

```text
HÌNH L486 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Từ vật liệu dệt tơ nhện siêu bền đến kim tiêm giảm đau mô phỏng vi ngạnh nhím, từ bộ đồ bay G-suit mô phỏng da hươu cao cổ đến thuốc tê thần kinh từ nọc ong ngọc!". Bố cục: Sơ đồ công nghệ phỏng sinh học hiển thị các phát minh y sinh học hiện đại được lấy cảm hứng từ cấu trúc cơ thể của mười sinh vật này; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L487</summary>

```text
HÌNH L487 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các kỹ sư hàng không vũ trụ hiện nay đang ứng dụng cơ chế van tĩnh mạch cổ của hươu cao cổ để thiết kế trang phục kháng áp cho phi hành gia bay vào vũ trụ!". Bố cục: Hình ảnh minh họa bộ đồ phi hành gia thế hệ mới lấy cảm hứng từ cấu trúc da và mạch nước màu hươu cao cổ; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L488</summary>

```text
HÌNH L488 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và các nhà khoa học vật liệu nano đang nghiên cứu cấu trúc sợi tơ không thấm nước của nhện lặn chuông để sản xuất các thiết bị lọc khí nhân tạo dưới đáy đại dương!". Bố cục: Mô hình 3D vật liệu sợi nano nhân tạo mô phỏng cấu trúc chuông lặn của nhện nước phát sáng lấp lánh; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L489</summary>

```text
HÌNH L489 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các chuyên gia dược phẩm đang tổng hợp hoạt chất kháng khuẩn từ lớp mỡ gai nhím để bào chế các loại thuốc xịt khử trùng vết thương thế hệ mới!". Bố cục: Hình ảnh lọ thuốc xịt y tế nano kháng khuẩn lấy cảm hứng từ gai nhím bắc mỹ; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Âm thanh truyền vào tai tôi không phải tiếng sôi ruột bình thường, mà là tiếng ùng ục ùng ục rền vang như một lò phản ứng hóa học đang sôi sục!". Bố cục: Hình ảnh đồ họa mô phỏng bên trong ổ bụng khỉ đột với chiếc manh tràng khổng lồ đang sủi bọt khí gas liên hồi; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L490</summary>

```text
HÌNH L490 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn các kỹ sư cơ khí chính xác thì nghiên cứu cơ cấu ngàm kẹp của mỏ cò giày để tạo ra các kẹp gắp thủy lực siêu khỏe trong phẫu thuật nội soi!". Bố cục: Sơ đồ kẹp phẫu thuật nội soi vi phẫu mô phỏng chuyển động khớp mỏ của loài cò mỏ giày; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L491</summary>

```text
HÌNH L491 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngành điện toán sinh học cũng đang học hỏi cách bộ não 4 g của cá mặt trăng quản lý khối cơ thể 2 tấn để tối ưu hóa thuật toán tiết kiệm năng lượng cho trí tuệ nhân tạo!". Bố cục: Đồ họa chip bán dẫn sinh học lấy cảm hứng từ mạng lưới nơ-ron tiết kiệm điện của cá mặt trăng; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L492</summary>

```text
HÌNH L492 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và các nhà sinh thái học bảo tồn đang nhân bản mùi hương thảo mộc đặc trưng của vẹt kakapo để chế tạo các bẫy pheromone theo dõi động vật quý hiếm!". Bố cục: Chai tinh dầu sinh học tỏa mùi xạ hương hoa cỏ tự nhiên của vẹt kakapo đặt trong phòng thí nghiệm; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L493</summary>

```text
HÌNH L493 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hàng triệu 5 tiến hóa của tự nhiên chính là phòng nghiên cứu và phát triển vĩ đại nhất, bền bỉ nhất mà loài người từng được thừa hưởng!". Bố cục: Bức tranh toàn cảnh cây tiến hóa với các nhánh loài tỏa ra như những vệt pháo hoa rực rỡ; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L494</summary>

```text
HÌNH L494 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không có một phát minh nào của con người lại không tìm thấy nguyên mẫu hoàn hảo đã tồn tại từ hàng triệu 5 trước trong cơ thể các loài sinh vật hoang dã!". Bố cục: Biểu đồ đối chiếu các công trình kiến trúc và cơ khí hiện đại với hình thái sinh học tự nhiên; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L495</summary>

```text
HÌNH L495 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Biết đâu trong tương lai không xa, các giải thưởng Nobel Y Học danh giá sẽ được trao cho những công trình giải mã thành công các bí mật giải phẫu học này!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười giơ cao tấm huy chương vàng Nobel mô phỏng lấp lánh dưới ánh đèn hội nghị.
```
</details>

<details><summary>L496</summary>

```text
HÌNH L496 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một loại thuốc điều trị đột quỵ và chống hình thành cục nước màu đông dựa trên cơ chế van tĩnh mạch cổ của hươu cao cổ!". Bố cục: Mô hình phân tử thuốc chống đột quỵ thế hệ mới lấy cảm hứng từ hệ tuần hoàn hươu cao cổ phát sáng trên màn hình máy chiếu; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L497</summary>

```text
HÌNH L497 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một loại màng lọc không khí thông minh tự làm sạch và bẫy oxy mô phỏng cấu trúc chuông lặn của nhện nước!". Bố cục: Bản vẽ thiết kế màng lọc khí nano đa tầng mô phỏng sợi tơ kỵ nước của nhện lặn chuông; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L498</summary>

```text
HÌNH L498 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hay một loại kháng sinh peptide tự nhiên điều chế từ màng mỡ gai nhím có thể dập tắt hoàn toàn các chủng siêu vi khuẩn kháng thuốc nguy hiểm nhất hành tinh!". Bố cục: Hình ảnh phân tử kháng sinh sinh học gắn vào màng tế bào vi khuẩn kháng thuốc tiêu diệt tận gốc mầm bệnh; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L499</summary>

```text
HÌNH L499 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bài học y khoa vĩ đại nhất mà ca trực đêm kinh hoàng này để lại cho toàn thể chúng ta là:". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án bước lại gần cửa sổ lớn hội trường, nơi ánh nắng bình minh đầu tiên đang rọi những vệt sáng vàng óng ả qua khung kính.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cảm giác như có một cơn lốc xoáy khí gas đang cuộn trào bên trong đường ruột của anh chàng lực sĩ này vậy!". Bố cục: Đồ họa sóng âm thanh hiển thị các dao động áp suất khí gas tăng vọt liên hồi trong khoang bụng bệnh nhân; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L500</summary>

```text
HÌNH L500 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong y học tiến hóa của tự nhiên, khái niệm dị tật hay khiếm khuyết chỉ là góc nhìn hạn hẹp của những kẻ chưa thấu hiểu trọn vẹn quy luật sinh tồn!". Bố cục: Toàn cảnh hội trường giao ban im phăng phắc, các bác sĩ trẻ xúc động lắng nghe từng lời tâm huyết của người thầy thuốc tiền bối.
```
</details>

<details><summary>L501</summary>

```text
HÌNH L501 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi một cánh cửa giải phẫu truyền thống khép lại, tạo hóa sẽ mở ra một cánh cửa tiến hóa kỳ diệu khác đưa sinh vật vươn tới đỉnh cao thích nghi!". Bố cục: Bức tranh nghệ thuật cách điệu biểu tượng cây sự sống vươn cành lá tỏa bóng che chở cho muôn loài sinh vật kỳ thú; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L502</summary>

```text
HÌNH L502 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chúng ta không đến đây để sửa chữa tự nhiên, mà đến đây để chiêm ngưỡng, học hỏi và bảo bọc sự đa dạng sinh học vô giá của hành tinh này!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đặt tay lên ngực áo, ánh mắt tràn đầy tình yêu thương và sự kính trọng đối với muôn loài muôn thú.
```
</details>

<details><summary>L503</summary>

```text
HÌNH L503 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôi xin tuyên bố: Ca trực đêm lịch sử của Phòng Cấp Cứu Tạo Hóa chính thức kết thúc thành công rực rỡ!". Bố cục: Toàn thể hội trường đứng bật dậy vỗ tay vang dội, tiếng reo hò chúc mừng rộn rã khắp các dãy bàn hội nghị; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L504</summary>

```text
HÌNH L504 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chuẩn bị ký giấy xuất viện và tiễn 10 người bạn đặc biệt của chúng ta trở về với thiên nhiên hoang dã nào!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười rạng rỡ, cùng toàn thể kíp trực bước ra sảnh lớn để đón ánh nắng sớm mai.
```
</details>

<details><summary>L505</summary>

```text
HÌNH L505 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sáu giờ sáng. Bầu trời ngoài kia đã trong xanh trở lại sau cơn mưa bão đêm qua, những giọt sương mai đọng lấp lánh trên từng phiến lá ngoài sân bệnh viện.". Bố cục: Khung cảnh sân bệnh viện buổi sáng sớm trong lành, chim hót líu lo trên cành cây, những vạt nắng vàng tươi chiếu rọi lên các bậc thềm đá hoa cương; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L506</summary>

```text
HÌNH L506 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không khí buổi sớm mai ngọt ngào và mát rượi, xua tan đi toàn bộ sự mệt mỏi và căng thẳng của ca trực cấp cứu nghẹt thở vừa qua.". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án tháo chiếc khẩu trang y tế, hít một hơi thật sâu làn gió mát lành thổi vào qua khung cửa sổ lớn sảnh đón tiếp.
```
</details>

<details><summary>L507</summary>

```text
HÌNH L507 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cửa sảnh lớn của Phòng Cấp Cứu Tạo Hóa mở toang đón ánh nắng bình minh ấm áp. Và giờ phút chia tay đầy xúc động đã chính thức điểm.". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án trong chiếc áo blouse trắng tinh tươm cùng cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng đứng ở bậc thềm sảnh lớn, trên tay cầm mười tấm giấy chứng nhận xuất viện danh dự.
```
</details>

<details><summary>L508</summary>

```text
HÌNH L508 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mười bệnh nhân quái kiệt của chúng ta đã xếp thành một hàng ngay ngắn trước thềm sảnh lớn, mỗi người mang một vẻ mặt rạng rỡ và tự tin hơn bao giờ hết!". Bố cục: Toàn cảnh ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện đứng tề tựu đông đủ bên nhau trên sân cỏ xanh mướt của bệnh viện, ánh ban mai chiếu rực rỡ lên từng gương mặt ngộ nghĩnh.
```
</details>

<details><summary>L509</summary>

```text
HÌNH L509 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chú Khỉ Đột Lưng Bạc ôm một giỏ táo tươi ngon, cái bụng vẫn tròn vo nhưng đã hết đau hoàn toàn, vẫy cánh tay cơ bắp lực sĩ chào tạm biệt các y bác sĩ!". Bố cục: chú Khỉ Đột Lưng Bạc hoạt hình cơ bắp cuồn cuộn vạm vỡ, mảng lông bạc sáng chói dọc sống lưng, bụng to tròn căng phồng vì chứa đầy lá cây lên men, ngồi xếp bằng trên giường bệnh ôm bụng thở dài đứng thẳng người, một tay xách giỏ táo, tay kia vẫy chào vui vẻ với nụ cười thân thiện; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôi lập tức cho chụp X-quang ổ bụng toàn phần để tìm ra nguyên nhân gốc rễ của cơn đau quằn quại này.". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án bấm nút điều khiển máy chụp X-quang kỹ thuật số công suất lớn quét qua toàn bộ thân hình đồ sộ của khỉ đột.
```
</details>

<details><summary>L510</summary>

```text
HÌNH L510 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chú Cá Thòi Lòi nhảy chồm chồm trên khay bùn tạm biệt, nháy đôi mắt lồi tinh nghịch rồi lặn tọt vào chiếc xe bồn nước chuyên dụng để về lại rừng Cà Mau!". Bố cục: chú Cá Thòi Lòi hoạt hình màu nâu xám lấm chấm xanh ngọc, hai mắt to tròn lồi hẳn trên đỉnh đầu chớp chớp ngộ nghĩnh, hai vây ngực bè to như đôi tay đang chống nạng gỗ mini đòi nhảy khỏi cáng cứu thương nhảy một cú ngoạn mục lên mép bồn xe nước cứu hộ, vẫy vây ngực chào tạm biệt mọi người; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L511</summary>

```text
HÌNH L511 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cô Ong Bắp Cày Ngọc bay lượn một vòng quanh đầu tôi như một lời cảm ơn duyên dáng, chiếc thân xanh ngọc bích lấp lánh dưới ánh bình minh trước khi bay vút lên bầu trời!". Bố cục: cô Ong Bắp Cày Ngọc (emerald cockroach wasp) hoạt hình thân thon dài phát sáng xanh ngọc bích kim loại lộng lẫy, chân dài thanh mảnh, tay cầm chiếc dao mổ phẫu thuật thần kinh siêu nhỏ giơ lên đầy tự tin chao lượn trên nền trời xanh biếc, để lại một vệt sáng lung linh trong không trung; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L512</summary>

```text
HÌNH L512 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chú Cá Mặt Trăng 2 tấn được cần cẩu nhẹ nhàng nâng bổng lên xe chuyên dụng chuyển thẳng ra vịnh biển để tiếp tục những chuyến lặn sâu 800 m!". Bố cục: chú Cá Mặt Trăng (ocean sunfish) hoạt hình khổng lồ hình đĩa tròn dẹt màu xám bạc, không có cuống đuôi, hai vây lưng và vây phần đuôi dựng đứng dài ngoằng, nằm ngửa trên chiếc cáng cứu thương quá khổ mắt to tròn ngơ ngác nằm trên võng bạt cứu hộ của cần cẩu, đôi mắt to tròn chớp chớp ngơ ngác chào khán giả trước khi xe khởi hành; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L513</summary>

```text
HÌNH L513 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chú Vẹt Kakapo béo tròn được tặng một chiếc ba-lô nhỏ chứa đầy hạt thông, lon ton đi bộ theo các nhân viên bảo tồn New Zealand với nụ cười mãn nguyện!". Bố cục: chú Vẹt Kakapo hoạt hình béo múp míp lông xanh rêu pha đốm nâu đen, mặt tròn lông tơ như chim cú mèo, mắt ngơ ngác dễ thương, hai cánh ngắn cũn cố vỗ lạch bạch trèo lên nóc tủ thuốc đeo chiếc ba-lô mini màu đỏ, đi lạch bạch từng bước vững chãi trên thảm cỏ, thỉnh thoảng quay đầu lại vẫy cánh; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L514</summary>

```text
HÌNH L514 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chú Lợn Hươu Babirusa kiêu hãnh khoe 4 chiếc răng nanh cong vút đã được làm sạch sáng bóng, bước đi tự tin về lại hòn đảo nhiệt đới hoang dã!". Bố cục: chú Lợn Hươu Babirusa hoạt hình da xám nhăn nheo ít lông, mõm dài, bốn chiếc răng nanh cong vút dị thường trong đó hai nanh trên mọc xuyên qua sống mũi uốn ngược về phía trán, vẻ mặt lo lắng sờ trán ngẩng cao đầu sải bước dũng mãnh, ánh sáng phản chiếu lấp lánh trên cặp nanh cong hoàn mỹ; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L515</summary>

```text
HÌNH L515 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quý cô Hươu Cao Cổ sải những bước chân thanh tao qua cổng bệnh viện, chiếc cổ dài 2 m vươn cao đón những làn gió mát lành của thảo nguyên!". Bố cục: chú Hươu Cao Cổ hoạt hình cao lêu nghêu có đốm hoa văn nâu vàng, chiếc cổ dài thẳng tắp quấn dải băng đo huyết áp y tế to bản màu đỏ, mắt to hiền từ chớp chớp bước đi uyển chuyển trong nắng mai, bóng dáng cao lều nghều in dài trên con đường rợp bóng cây; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L516</summary>

```text
HÌNH L516 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chú Cò Mỏ Giày khẽ cúi đầu chào lịch thiệp, rồi đột ngột xòe đôi cánh rộng 2,5 m bay vút lên không trung xé toạc làn sương sớm!". Bố cục: chú Cò Mỏ Giày hoạt hình lông xám tro, dáng đứng sừng sững bất động như tượng đá, chiếc mỏ khổng lồ màu vàng xám phình to hình chiếc guốc gỗ, ánh mắt lạnh như tiền đứng canh cửa phòng cấp cứu dang rộng đôi cánh khổng lồ màu xám tro, bay lượn uy nghi trên nền trời bình minh rực rỡ; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L517</summary>

```text
HÌNH L517 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và chú Nhím Lông Nhọn cùng chú Nhện Lặn Chuông tí hon cũng đã yên vị trong những chiếc lồng sinh thái an toàn để trở về với thiên nhiên hoang dã!". Bố cục: chú Nhím Lông Nhọn Bắc Mỹ hoạt hình béo tròn xù xì, toàn thân phủ kín ba mươi ngàn chiếc gai nhọn trắng đen, đang ôm chặt một thân cây gỗ gặm vỏ thuốc, người tỏa mùi tinh dầu thơm nhẹ và chú Nhện Lặn Chuông (diving bell spider) hoạt hình màu nâu đen nhiều lông mịn, tám chân ôm một chiếc bóng khí lấp lánh như viên ngọc trong suốt dưới bụng, đang ngâm mình trong bể nước dã chiến trong bể thủy tinh mini được các tình nguyện viên cẩn thận đưa lên xe chuyên dụng; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L518</summary>

```text
HÌNH L518 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôi hít một hơi thật sâu làn không khí trong lành của buổi sớm mai, cất chiếc ống nghe y tế vào túi áo khoác.". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đứng trên bậc thềm nhìn theo đoàn xe khuất dần sau rặng cây xanh, một nụ cười ấm áp nở trên môi.
```
</details>

<details><summary>L519</summary>

```text
HÌNH L519 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ca trực đêm kinh hoàng nhất cuộc đời làm bác sĩ của tôi tại Phòng Cấp Cứu Tạo Hóa đã chính thức khép lại trong niềm vui trọn vẹn.". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng đứng bên cạnh mỉm cười, trao cho bác sĩ một tách cà phê mới thơm lừng nóng hổi; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và kết quả trên tấm phim rọi sáng làm cả phòng cấp cứu phải trố mắt kinh ngạc vì sự đồ sộ của hệ thống tiêu hóa bên trong!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án kẹp tấm phim X-quang to bản lên hộp đèn sáng trắng trên tường, chỉ tay vào vùng khoang bụng khổng lồ chứa đầy bóng khí.
```
</details>

<details><summary>L520</summary>

```text
HÌNH L520 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng bài học sâu sắc mà 10 sinh vật kỳ dị này để lại sẽ mãi mãi in đậm trong tâm trí của mỗi chúng ta:". Bố cục: Cận cảnh gương mặt đôn hậu và ánh mắt tràn đầy cảm xúc của ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án nhìn thẳng vào ống kính máy quay.
```
</details>

<details><summary>L521</summary>

```text
HÌNH L521 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong thế giới tự nhiên kỳ diệu này, không có sinh vật nào là sai sót, không có nét giải phẫu nào là vô nghĩa. Mọi sự sống đều là một kiệt tác hoàn mỹ của mẹ Trái Đất!". Bố cục: Bức tranh toàn cảnh thiên nhiên bao la với rừng rậm, đại dương, thảo nguyên và bầu trời xanh ngắt nơi muôn loài cùng chung sống hòa hợp; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L522</summary>

```text
HÌNH L522 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hàng triệu 5 tiến hóa đã đẽo gọt nên những cơ chế sinh tồn tinh xảo vượt xa trí tưởng tượng phong phú nhất của con người!". Bố cục: Hình ảnh biểu tượng Trái Đất xanh tươi quay chầm chậm giữa không gian bao la lấp lánh muôn ngàn vì sao; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L523</summary>

```text
HÌNH L523 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi sinh vật là một nốt nhạc độc đáo trong bản giao hưởng vĩ đại của sự sống trên hành tinh xanh!". Bố cục: Nốt nhạc ánh sáng phát ra từ hình vẽ các loài vật kết nối thành một bản tổng phổ âm nhạc lấp lánh; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L524</summary>

```text
HÌNH L524 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôi cùng cô y tá trao từng túi thuốc bổ vitamin và cẩm nang chăm sóc sức khỏe sinh thái cho người đại diện của từng đoàn cứu hộ.". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng cẩn thận xếp các túi thuốc bổ thảo dược đóng gói đẹp mắt trao vào tay các tình nguyện viên bảo tồn thiên nhiên hoang dã; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L525</summary>

```text
HÌNH L525 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chúng tôi dặn dò kỹ lưỡng: Anh khỉ đột nhớ giảm ăn lá cây có mủ đắng, chú cá thòi lòi nhớ bôi kem giữ ẩm mang cá khi leo cây, còn chú vẹt kakapo thì nhớ tập thể dục đi bộ đều đặn nhé!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười dặn dò từng bệnh nhân, các con vật đồng loạt gật đầu kêu líu lo ụt ịt như những lời chào cảm ơn chân thành.
```
</details>

<details><summary>L526</summary>

```text
HÌNH L526 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cả 10 bệnh nhân cùng hòa giọng tạo nên một bản hợp xướng rộn rã làm bừng sáng cả khoảng sân bệnh viện trong nắng sớm!". Bố cục: Tiếng hót của vẹt kakapo, tiếng gõ mỏ của cò mỏ giày và tiếng gầm trầm ấm của khỉ đột vang lên rộn rã giữa bình minh rực rỡ; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L527</summary>

```text
HÌNH L527 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một ca trực đêm đầy ắp tiếng cười, những giọt mồ hôi và sự kính phục vô bờ trước sức sáng tạo không giới hạn của tạo hóa!". Bố cục: Toàn cảnh đội ngũ y bác sĩ đứng vẫy tay chào tạm biệt đoàn xe cứu hộ đang lăn bánh qua cổng bệnh viện rợp bóng cây xanh; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L528</summary>

```text
HÌNH L528 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tu... tu... tuuuu! Bất thình lình, một tiếng còi tàu hơi nước trầm đục và ma mị từ đâu vang vọng lại qua thung lũng sương mù dày đặc!". Bố cục: Xa xa nơi đường ray xe lửa cổ uốn lượn quanh chân núi, một vệt khói trắng bốc lên cuồn cuộn giữa màn sương sớm bảng lảng; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L529</summary>

```text
HÌNH L529 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tiếng còi tàu hú lên từng hồi dồn dập, báo hiệu chuyến tàu tốc hành xuyên đêm chở 10 hành khách bí ẩn nhất hành tinh sắp lăn bánh vào ga!". Bố cục: Cận cảnh đầu máy xe lửa hơi nước khổng lồ màu đen tuyền phong cách Art Deco thập niên 1930 với đèn pha vàng rực chiếu sáng đường ray; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bác sĩ ơi, cái bụng anh này chứa toàn là khí gas! Có phải anh ấy ăn nhầm thuốc nổ hay ăn trúng nấm độc gì trong rừng sâu không ạ?". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng đứng bên cạnh nhìn tấm phim X-quang, hai tay ôm má hốt hoảng kêu lên.
```
</details>

<details><summary>L530</summary>

```text
HÌNH L530 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một vụ án mất tích bí ẩn vừa xảy ra trên chuyến tàu tốc hành vượt bão tuyết! Và thám tử tài 3 sẽ phải vào cuộc để vén màn 10 bí mật sinh học gây sốc tiếp theo!". Bố cục: Tấm vé tàu hỏa cổ điển đục lỗ mang dòng chữ HỒ SƠ MẬT MEGA 06: CHUYẾN TÀU TỐC HÀNH XUYÊN ĐÊM hiện lên trên màn hình trước khi khép lại; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L531</summary>

```text
HÌNH L531 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Những manh mối dấu vết của Rắn Hổ Mang Chúa, Cá Sấu Nước Mặn và Cá Mập Trắng đã bắt đầu lộ diện trên các toa tàu sương mù!". Bố cục: Hình ảnh bóng đen của mười sinh vật bí ẩn trên chuyến tàu đêm đang lướt qua khung cửa sổ toa tàu hơi nước; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L532</summary>

```text
HÌNH L532 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ai trong số 10 quái thú đầm lầy và đại dương này là thủ phạm thực sự của vụ án chấn động đường ray xe lửa đêm đông giá rét?". Bố cục: Hình ảnh chiếc kính lúp thám tử soi vào dấu chân khổng lồ bí ẩn trên sàn toa tàu phủ đầy sương lạnh; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L533</summary>

```text
HÌNH L533 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một hành trình phá án nghẹt thở kết hợp giữa tư duy trinh thám cổ điển và những bí mật giải phẫu học rợn người đang chờ đón quý khán giả trong siêu phẩm Mega số 6 tiếp theo!". Bố cục: Bức tranh poster giới thiệu MEGA 06 với hình ảnh đầu tàu hỏa hơi nước xuyên qua màn sương đêm ma mị; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L534</summary>

```text
HÌNH L534 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiếc vali da cổ điển khóa số đang chứa bản hồ sơ mật về độc tố và lực cắn của 10 hung thần đầm lầy đang đợi được giải mã!". Bố cục: Cận cảnh chiếc vali da có gắn nhãn niêm phong hồ sơ mật đặt trên bàn gỗ toa tàu hỏa; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L535</summary>

```text
HÌNH L535 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngoài kia, những bông tuyết đầu mùa bắt đầu rơi lả tả trên những mái vòm toa tàu hỏa bằng kim loại sáng loáng.". Bố cục: Những bông tuyết trắng muốt rơi nhẹ nhàng phủ kín mui tàu hỏa hơi nước đang đỗ tại sân ga cổ kính giữa thung lũng tuyết; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L536</summary>

```text
HÌNH L536 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tiếng chuông đồng hồ quả quýt của vị thám tử bí ẩn vang lên từng tiếng tích tắc điểm đúng 12 giờ đêm!". Bố cục: Bàn tay đeo găng da màu đen mở nắp chiếc đồng hồ quả quýt mạ vàng chạm khắc tinh xảo, kim đồng hồ chỉ đúng nửa đêm; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L537</summary>

```text
HÌNH L537 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một bức mật thư viết tay bằng mực tím bị kẹp dưới chân chiếc đèn bàn cổ, hé lộ danh sách 10 hành khách mang những vũ khí sinh học nguy hiểm bậc nhất tự nhiên!". Bố cục: Bức thư niêm phong sáp đỏ có in hình đầu lâu và dấu chân thú bí ẩn nằm trên bàn gỗ gụ toa tàu hạng nhất; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L538</summary>

```text
HÌNH L538 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Liệu vị thám tử tài 3 có kịp phá giải 10 vụ án mạng bí ẩn trước khi chuyến tàu hơi nước cập bến bình minh hay không?". Bố cục: Chiếc bóng cao lớn của vị thám tử mặc áo măng tô dài và đội mũ phớt đứng sừng sững bên cửa sổ toa tàu nhìn vào màn sương tuyết; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L539</summary>

```text
HÌNH L539 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một bầu không khí nghẹt thở, ly kỳ và đậm chất trinh thám cổ điển đang đón đợi các bạn ở phía trước!". Bố cục: Ánh đèn vàng mờ ảo hắt ra từ các ô cửa kính toa tàu hơi nước đang lăn bánh xuyên qua hẻm núi tuyết phủ trắng xóa; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhìn tấm phim chụp mà em tưởng như đang nhìn vào một quả bóng bay khí cầu khổng lồ sắp nổ tung tới nơi rồi bác sĩ ơi!". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng run run chỉ ngón tay vào những khoảng sáng rực của các túi khí gas phân bố khắp ổ bụng khỉ đột; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L540</summary>

```text
HÌNH L540 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cảm ơn toàn thể các đồng nghiệp và quý khán giả đã đồng hành cùng tôi qua ca trực đêm đáng nhớ này tại Phòng Cấp Cứu Tạo Hóa!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười giơ tay vẫy chào tạm biệt khán giả trong khi nền nhạc tươi vui vang lên khép lại tập phim.
```
</details>

<details><summary>L541</summary>

```text
HÌNH L541 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đừng quên bấm đăng ký kênh và nhấn chuông thông báo để không bỏ lỡ hành trình phá án tiếp theo trên Chuyến Tàu Tốc Hành Bí Ẩn nhé! Xin chào và hẹn gặp lại!". Bố cục: Dòng chữ VẼ CHUYỆN HOANG DÃ cùng biểu tượng nút đăng ký phát sáng rực rỡ trên màn hình kết thúc; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L542</summary>

```text
HÌNH L542 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy để lại bình luận bên dưới xem ca bệnh nào đêm nay làm các bạn kinh ngạc và thán phục nhất nhé! Bác Sĩ Trưởng Khoa xin chào và hẹn gặp lại tất cả các bạn!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án cùng cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng vẫy tay chào với nụ cười rạng rỡ, màn hình mờ dần trong tiếng nhạc vui tươi; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Em có nên chuẩn bị một chiếc kim chọc hút khí màng bụng để giải áp ngay bây giờ không ạ?". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng cầm chiếc kim tiêm dài vẻ lo lắng ngước nhìn bác sĩ trưởng khoa xin ý kiến; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyệt đối không được chọc kim vào bụng bệnh nhân cô y tá nhé! Không hề có chất độc hay thuốc nổ nào ở đây cả!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười lắc đầu, quay lại vỗ nhẹ vào vai bệnh nhân khỉ đột đang lo lắng.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây chính là bí mật sinh học vĩ đại nhất của loài khỉ đột mà sách giáo khoa ít khi nhắc tới!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án tháo kính mắt, dùng khăn lau nhẹ rồi hướng dẫn các bác sĩ nội trú quan sát cấu trúc đường ruột trên phim chụp.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Anh chàng này không hề bị ngộ độc dạ dày, mà ổ bụng của anh ấy thực chất là một nhà máy lên men vi sinh vật ruột sau khổng lồ hoạt động ngày đêm!". Bố cục: Sơ đồ sinh học minh họa đường tiêu hóa của khỉ đột, nổi bật là phần manh tràng phình đại gấp nhiều lần so với con người; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy nhìn vào chế độ ăn uống hàng ngày của loài khỉ đột trong tự nhiên mà xem: một thực đơn làm bất kỳ loài động vật ăn thịt nào cũng phải lắc đầu lè lưỡi!". Bố cục: Bức tranh miêu tả rừng mưa rậm rạp nhiệt đới châu Phi, nơi bầy khỉ đột đang thong thả hái lượm thức ăn giữa thảm thực vật hoang sơ; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hàng ngày, một con khỉ đột lưng bạc trưởng thành phải nạp vào cơ thể tới 20-30 kg lá cây, vỏ cây, thân cây tầm ma và cành non xơ cứng.". Bố cục: chú Khỉ Đột Lưng Bạc hoạt hình cơ bắp cuồn cuộn vạm vỡ, mảng lông bạc sáng chói dọc sống lưng, bụng to tròn căng phồng vì chứa đầy lá cây lên men, ngồi xếp bằng trên giường bệnh ôm bụng thở dài ngồi giữa một đống lá cây rừng to như ngọn đồi nhỏ, nhồm nhoàm nhai từng bó lá xơ ráp đầy ngon lành; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc biệt là những cây tầm ma có đầy gai châm chứa độc tố histamine và axit formic gây ngứa rát buốt da người, nhưng chú khỉ đột lại nhai ngấu nghiến ngon lành!". Bố cục: Cận cảnh hàm răng khỉ đột nhai nát những nhánh cây tầm ma đầy lông ngứa mà niêm mạc miệng không hề bị sưng tấy tổn thương; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L62</summary>

```text
HÌNH L62 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bởi vì tuyến nước bọt của khỉ đột tiết ra các enzym đặc biệt có tính kiềm cao, nhanh chóng trung hòa toàn bộ các phân tử độc tố gây bỏng rát trước khi lá trôi xuống dạ dày!". Bố cục: Sơ đồ tuyến nước bọt khỉ đột giải phóng dòng enzym trung hòa màu xanh bảo vệ lớp niêm mạc thực quản; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L63</summary>

```text
HÌNH L63 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hệ tiêu hóa thông thường của con người hay các loài ăn quả hoàn toàn bất lực trước lượng chất xơ thô cellulose khổng lồ và dai nhách này.". Bố cục: Kính hiển vi quang học phóng đại cấu trúc sợi cellulose cứng như sợi thép đan xen chằng chịt trong phiến lá cây; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L64</summary>

```text
HÌNH L64 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu chúng ta ăn đống lá cây xơ xác đó vào bụng, dạ dày sẽ bị thủng hoặc tắc ruột ngay lập tức vì không thể tiêu hóa nổi!". Bố cục: Hình ảnh so sánh dạ dày đơn giản của người với đường ruột đồ sộ dài ngoằng của khỉ đột; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L65</summary>

```text
HÌNH L65 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng tạo hóa đã trang bị cho khỉ đột một chiếc manh tràng và đại tràng với dung tích khổng lồ, chứa hàng nghìn tỷ vi khuẩn kỵ khí chuyên biệt!". Bố cục: Cận cảnh các cụm vi khuẩn đường ruột có ích màu xanh ngọc bích đang bám quanh các sợi lá và phân hủy cellulose; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L66</summary>

```text
HÌNH L66 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các vi khuẩn cộng sinh này làm việc miệt mài ngày đêm để bẻ gãy các liên kết phân tử cellulose cứng rắn nhất thành các hợp chất đơn giản hơn.". Bố cục: Minh họa các enzym vi sinh vật cắt đứt các chuỗi phân tử đường phức tạp trong thành tế bào thực vật; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L67</summary>

```text
HÌNH L67 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thời gian lưu chuyển thức ăn trong đại tràng của khỉ đột kéo dài từ 35-40 giờ liên tục, đủ để vi khuẩn phân giải triệt để từng sợi xơ thực vật!". Bố cục: bảng kẹp bệnh án y khoa khổng lồ (clipboard) kẹp trên giá đỡ kim loại, hiển thị 10 hồ sơ bệnh án hoạt hình với nhãn đơn thuốc phát sáng và sóng nhịp tim ECG màu đỏ nhấp nháy (không có chữ, không có số) hiển thị con số 40 giờ lưu chuyển thức ăn cùng sơ đồ đường ruột dài gấp sáu lần chiều dài cơ thể; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L68</summary>

```text
HÌNH L68 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quá trình lên men vi sinh vật tự nhiên này giải phóng ra một lượng khí gas khổng lồ, đồng thời tổng hợp nên các axit béo chuỗi ngắn cực kỳ giàu năng lượng!". Bố cục: Đồ họa hóa học hiển thị các phân tử axit béo chuỗi ngắn acetate và propionate phát sáng vàng kim hấp thu qua thành ruột; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L69</summary>

```text
HÌNH L69 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nghiên cứu dinh dưỡng đột phá trong công trình khoa học nổi tiếng của tiến sĩ Popovich trên Tạp Chí Dinh Dưỡng học đã chứng minh một sự thật chấn động toàn cầu:". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án giơ bản báo cáo khoa học của tiến sĩ Popovich lên trước ánh đèn, chỉ vào bảng số liệu phân tích calo đường ruột.
```
</details>

<details><summary>L70</summary>

```text
HÌNH L70 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tới 70% tổng năng lượng calo mỗi ngày của khỉ đột không đến từ đường hay tinh bột, mà đến từ chính quá trình lên men chất xơ này!". Bố cục: bảng kẹp bệnh án y khoa khổng lồ (clipboard) kẹp trên giá đỡ kim loại, hiển thị 10 hồ sơ bệnh án hoạt hình với nhãn đơn thuốc phát sáng và sóng nhịp tim ECG màu đỏ nhấp nháy (không có chữ, không có số) bật sáng dòng chữ số 70% calo phát sáng rực rỡ bên cạnh biểu tượng chiếc lá cây biến thành năng lượng cơ bắp; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L71</summary>

```text
HÌNH L71 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các axit béo chuỗi ngắn sau khi lên men được hấp thu trực tiếp qua thành đại tràng, đi thẳng vào nước màu và nuôi dưỡng toàn bộ khối cơ bắp khổng lồ của con vật!". Bố cục: Dòng năng lượng màu vàng ánh kim từ thành ruột lan tỏa khắp các bó cơ bắp cuồn cuộn trên lưng và cánh tay khỉ đột; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L72</summary>

```text
HÌNH L72 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chúng hoạt động tương tự như loài bò hay ngựa, nhưng thay vì lên men ở dạ cỏ phía trước thì khỉ đột lên men ở ruột sau vô cùng tinh vi!". Bố cục: Sơ đồ so sánh cơ chế lên men dạ cỏ của bò với cơ chế lên men ruột sau của khỉ đột; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L73</summary>

```text
HÌNH L73 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nói cách khác, cái bụng bự phình to của anh chàng không phải là mỡ thừa lười biếng, mà là một cỗ máy sinh học siêu đẳng biến cỏ rác thành cơ bắp cuồn cuộn!". Bố cục: chú Khỉ Đột Lưng Bạc hoạt hình cơ bắp cuồn cuộn vạm vỡ, mảng lông bạc sáng chói dọc sống lưng, bụng to tròn căng phồng vì chứa đầy lá cây lên men, ngồi xếp bằng trên giường bệnh ôm bụng thở dài đứng dậy ưỡn ngực đấm thùm thụp vào ngực khoe cơ bắp rắn chắc, bụng phình to đầy tự hào; ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án mỉm cười gật đầu tán thưởng.
```
</details>

<details><summary>L74</summary>

```text
HÌNH L74 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng hôm nay, do ăn hơi nhiều mầm tre non lên men nhanh vào buổi chiều nên lượng khí gas sinh ra quá mức làm căng tức thành bụng tạm thời mà thôi!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án cười xòa, giải thích cặn kẽ cho chú khỉ đột đang lắng nghe từng lời của bác sĩ.
```
</details>

<details><summary>L75</summary>

```text
HÌNH L75 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Được rồi anh bạn cơ bắp, tôi kê đơn cho anh 2 viên men tiêu hóa thảo dược và một tách trà gừng ấm để tống bớt lượng khí thừa ra ngoài nhé!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án xé một tờ đơn thuốc nhỏ đưa cho chú Khỉ Đột Lưng Bạc hoạt hình cơ bắp cuồn cuộn vạm vỡ, mảng lông bạc sáng chói dọc sống lưng, bụng to tròn căng phồng vì chứa đầy lá cây lên men, ngồi xếp bằng trên giường bệnh ôm bụng thở dài, anh chàng khỉ đột mừng rỡ nhận lấy rồi cúi đầu cảm ơn rối rít.
```
</details>

<details><summary>L76</summary>

```text
HÌNH L76 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ cần ợ hơi vài tiếng sấm sét là anh lại có thể đấm vỡ đá và vỗ ngực vang rền khắp thảo nguyên được rồi!". Bố cục: Chú chú Khỉ Đột Lưng Bạc hoạt hình cơ bắp cuồn cuộn vạm vỡ, mảng lông bạc sáng chói dọc sống lưng, bụng to tròn căng phồng vì chứa đầy lá cây lên men, ngồi xếp bằng trên giường bệnh ôm bụng thở dài uống cạn cốc nước ấm y tá đưa, phát ra một tiếng ợ hơi trầm đục làm rung rinh cả rèm cửa phòng khám trong tiếng cười vui vẻ.
```
</details>

<details><summary>L77</summary>

```text
HÌNH L77 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ca cấp cứu số một của Phòng Cấp Cứu Tạo Hóa hoàn thành xuất sắc! Giờ thì y tá, chuyển ngay hồ sơ ca số 2 sang Khoa Hô Hấp Ngược cho tôi!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đóng sập tập bệnh án số một lại, bước nhanh sang phòng khám chuyên khoa bên cạnh.
```
</details>

<details><summary>L78</summary>

```text
HÌNH L78 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cánh cửa phòng khám Khoa Hô Hấp Ngược mở ra với một bầu không khí ẩm ướt lạ thường.". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án đẩy cửa bước vào phòng khám hô hấp có các bồn nước và ống dẫn oxy, cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng đang đứng bối rối bên cạnh một chiếc chậu thủy tinh trong suốt.
```
</details>

<details><summary>L79</summary>

```text
HÌNH L79 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và bệnh nhân số 2 đang nằm trong một tình huống dở khóc dở cười nhất từ trước tới nay trong lịch sử cấp cứu của chúng tôi.". Bố cục: Khung cảnh căn phòng khám chuyên khoa với các bình dưỡng khí cao áp xếp hàng, nhưng giữa bàn khám lại là một chậu nước đầy rong rêu; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L80</summary>

```text
HÌNH L80 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chú Nhện Lặn Chuông tí hon dài chưa đầy 2 cm đang dùng hết sức bình sinh để trốn khỏi chiếc mặt nạ thở oxy nhi khoa!". Bố cục: Cận cảnh chú Nhện Lặn Chuông (diving bell spider) hoạt hình màu nâu đen nhiều lông mịn, tám chân ôm một chiếc bóng khí lấp lánh như viên ngọc trong suốt dưới bụng, đang ngâm mình trong bể nước dã chiến màu nâu đen tám chân thoăn thoắt bò qua mép chiếc mặt nạ dưỡng khí mini, lao thẳng vào làn nước trong veo; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L81</summary>

```text
HÌNH L81 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi lần cô y tá đưa chiếc ống thở tới gần mũi, chú nhện lại cắn phăng một nhát rồi lặn một hơi mất tăm xuống tận đáy chậu nước!". Bố cục: chú Nhện Lặn Chuông (diving bell spider) hoạt hình màu nâu đen nhiều lông mịn, tám chân ôm một chiếc bóng khí lấp lánh như viên ngọc trong suốt dưới bụng, đang ngâm mình trong bể nước dã chiến bơi thoăn thoắt xuống đáy chậu, chui tọt vào giữa đám rong đuôi chó xanh biếc, giương tám chiếc mắt nhỏ xíu nhìn lên vẻ đề phòng; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L82</summary>

```text
HÌNH L82 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiếc đuôi nhỏ xíu của nó khẽ lắc lư, để lộ một vầng hào quang lấp lánh như viên ngọc trai bọc quanh phần bụng dưới làn nước trong vắt.". Bố cục: Cận cảnh bọt khí tròn xoe ôm lấy phần bụng của chú nhện lặn chuông dưới đáy chậu nước; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L83</summary>

```text
HÌNH L83 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bác sĩ ơi em chụp mặt nạ oxy vào mặt nó mà nó cứ cắn đứt dây rồi nhảy xuống nước! Con nhện này bị trầm cảm muốn tự vẫn hay sao ấy ạ?". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng giơ sợi dây thở oxy bị cắn cụt lủn lên, vẻ mặt vừa thương cảm vừa bất lực tột cùng.
```
</details>

<details><summary>L84</summary>

```text
HÌNH L84 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Em vớt nó lên thở không khí bình thường thì nó cứ nằm đờ đẫn ra, thế mà vừa thả vào nước là nó bơi nhanh như một chiếc tàu ngầm mini!". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng chỉ tay vào chậu nước, nơi chú nhện đang bơi lội tung tăng như cá cảnh giữa đàn rong xanh; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L85</summary>

```text
HÌNH L85 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Có khi nào con nhện này bị đột biến gen thành loài cá không bác sĩ ơi?". Bố cục: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng ngước nhìn bác sĩ với đôi mắt thỏ tròn xoe ngây thơ; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L86</summary>

```text
HÌNH L86 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bình tĩnh nào cô y tá! Nó không hề muốn tự vẫn đâu, mà chúng ta đang ép một thợ lặn chuyên nghiệp thở theo cách của người đi bộ trên cạn đấy!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án bật cười bước tới bên bình nước, cúi sát mặt quan sát từng cử động tinh vi của chú nhện dưới làn nước trong vắt.
```
</details>

<details><summary>L87</summary>

```text
HÌNH L87 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây là loài nhện duy nhất trong số hơn 50.000 loài nhện đã được phát hiện trên Trái Đất dành toàn bộ cuộc đời của mình dưới đáy nước ngọt!". Bố cục: chú Nhện Lặn Chuông (diving bell spider) hoạt hình màu nâu đen nhiều lông mịn, tám chân ôm một chiếc bóng khí lấp lánh như viên ngọc trong suốt dưới bụng, đang ngâm mình trong bể nước dã chiến bơi lội uyển chuyển giữa các nhánh rong xanh biếc, thân mình phủ một lớp ánh bạc lấp lánh như được dát kim loại; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L88</summary>

```text
HÌNH L88 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó sinh ra dưới nước, săn mồi dưới nước, giao phối dưới nước, đẻ trứng dưới nước và thậm chí ngủ đông cũng ở dưới đáy bùn nước!". Bố cục: Hình ảnh một chú nhện lặn chuông đang bắt một ấu trùng muỗi nước dưới đáy hồ trong suốt; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L89</summary>

```text
HÌNH L89 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thế nhưng về mặt nguồn gốc giải phẫu, nhện lặn chuông vẫn là một loài chân khớp thở bằng phổi sách và hệ thống ống khí quản trên cạn.". Bố cục: Sơ đồ giải phẫu hiển vi của nhện hiển thị hệ thống phổi sách và các lỗ thở nhỏ li ti xếp dọc hai bên bụng; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L90</summary>

```text
HÌNH L90 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nghĩa là nó bắt buộc phải hít thở khí oxy dạng phân tử tự do trong không khí chứ mang của nó hoàn toàn không thể lọc oxy hòa tan như loài cá!". Bố cục: Hình vẽ so sánh lá mang của cá với hệ thống phổi sách nhiều nếp gấp của nhện lặn chuông; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L91</summary>

```text
HÌNH L91 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vậy làm thế nào mà một sinh vật thở bằng không khí lại có thể sống cả đời dưới nước mà không hề bị chết đuối?". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án khoanh tay trước ngực, đặt câu hỏi đầy gợi mở nhìn về phía các bác sĩ nội trú đang vây quanh bàn khám.
```
</details>

<details><summary>L92</summary>

```text
HÌNH L92 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Câu trả lời nằm ở một phát minh công nghệ nano sinh học độc nhất vô nhị mà loài nhện này đã hoàn thiện qua hàng triệu 5 tiến hóa!". Bố cục: Kính hiển vi điện tử quét phóng đại hàng triệu sợi lông tơ nano có cấu trúc rãnh khía đặc biệt đẩy lùi các phân tử nước; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L93</summary>

```text
HÌNH L93 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn bộ vùng bụng và các kẽ chân của nhện lặn chuông được bao phủ bởi hàng triệu sợi lông kỵ nước siêu nhỏ với mật độ dày đặc phi thường.". Bố cục: Các sợi lông nano xếp nghiêng góc chính xác, tạo ra một sức căng bề mặt cực lớn ngăn không cho các phân tử nước chạm vào lớp da bụng; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L94</summary>

```text
HÌNH L94 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi khi cần dưỡng khí, chú nhện chỉ việc nhô phần đuôi lên khỏi mặt nước trong đúng 1/10 giây rồi lặn nhanh xuống.". Bố cục: chú Nhện Lặn Chuông (diving bell spider) hoạt hình màu nâu đen nhiều lông mịn, tám chân ôm một chiếc bóng khí lấp lánh như viên ngọc trong suốt dưới bụng, đang ngâm mình trong bể nước dã chiến ngoi phần chóp bụng lên mặt nước trong chớp mắt rồi lặn nhanh xuống, kéo theo một khối bong bóng khí tròn xoe; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L95</summary>

```text
HÌNH L95 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lớp lông kỵ nước lập tức bẫy chặt một lớp màng không khí bao quanh toàn bộ cơ thể, biến con nhện thành một thợ lặn bọc trong một chiếc áo giáp khí óng ánh như bạc!". Bố cục: Cơ thể chú nhện phát sáng lung linh dưới nước nhờ lớp bọt khí bạc bao phủ toàn thân như một bộ đồ lặn vũ trụ mini; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L96</summary>

```text
HÌNH L96 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hai chiếc chân sau của nó được cấu tạo như những chiếc bàn chải chuyên dụng, thường xuyên chải chuốt các sợi lông để loại bỏ cặn bẩn bám dính, giữ cho lớp áo giáp khí luôn thông thoáng!". Bố cục: Chú chú Nhện Lặn Chuông (diving bell spider) hoạt hình màu nâu đen nhiều lông mịn, tám chân ôm một chiếc bóng khí lấp lánh như viên ngọc trong suốt dưới bụng, đang ngâm mình trong bể nước dã chiến dùng hai chân sau vuốt ve các sợi lông trên bụng một cách tỉ mỉ để duy trì sức căng bề mặt tối ưu; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L97</summary>

```text
HÌNH L97 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không chỉ dừng lại ở chiếc áo giáp khí di động đó, con nhện còn tiến hành xây dựng cả một căn cứ thế giới tự nhiên ngầm dưới đáy hồ!". Bố cục: Chú chú Nhện Lặn Chuông (diving bell spider) hoạt hình màu nâu đen nhiều lông mịn, tám chân ôm một chiếc bóng khí lấp lánh như viên ngọc trong suốt dưới bụng, đang ngâm mình trong bể nước dã chiến bắt đầu kéo những sợi tơ trong suốt đan dệt giữa hai nhánh rong rêu thủy sinh; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L98</summary>

```text
HÌNH L98 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kỳ quan thực sự nằm ở chiếc chuông lặn mà chú nhện dệt nên dưới đáy hồ bằng chính những sợi tơ chuyên dụng của mình!". Bố cục: Dưới đáy nước, chiếc chuông lặn bằng tơ nhện hình chiếc chuông úp ngược phát sáng trắng bạc, chứa đầy không khí trong suốt; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>L99</summary>

```text
HÌNH L99 (16:9 ngang, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó nhả ra những sợi tơ nhện không thấm nước đặc biệt, đan kết chúng thành một mái vòm hình chiếc chuông úp ngược neo chặt vào các thân rong rêu thủy sinh.". Bố cục: Chú chú Nhện Lặn Chuông (diving bell spider) hoạt hình màu nâu đen nhiều lông mịn, tám chân ôm một chiếc bóng khí lấp lánh như viên ngọc trong suốt dưới bụng, đang ngâm mình trong bể nước dã chiến thoăn thoắt dùng các chân sau dệt từng đường tơ trắng muốt đan xen chằng chit thành một mạng lưới vô cùng bền chắc; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Mười 2 giờ đêm tại Phòng Cấp Cứu Tạo Hóa! Còi báo động đỏ réo vang khi 10 ca bệnh kỳ dị nhất hành tinh cùng lúc tràn vào sảnh!". Bố cục: Còi báo động đỏ chớp nháy liên hồi, ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án quàng vội ống nghe lao ra sảnh cấp cứu đón mười cáng bệnh nhân xếp hàng chen chúc.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Anh Khỉ Đột Lưng Bạc đấm bẹp đầu xe hơi nhưng đang khóc ròng vì bụng đầy hơi men!". Bố cục: chú Khỉ Đột Lưng Bạc hoạt hình cơ bắp cuồn cuộn vạm vỡ, mảng lông bạc sáng chói dọc sống lưng, bụng to tròn căng phồng vì chứa đầy lá cây lên men, ngồi xếp bằng trên giường bệnh ôm bụng thở dài ôm cái bụng tròn ủng như quả bóng bay rên rỉ, bên cạnh là tấm phim X-quang chụp ổ bụng chứa toàn bọt khí lên men; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Chú Cá Thòi Lòi nhảy chồm chồm kiên quyết không thở dưới nước, dùng vây leo tót lên rèm cửa!". Bố cục: chú Cá Thòi Lòi hoạt hình màu nâu xám lấm chấm xanh ngọc, hai mắt to tròn lồi hẳn trên đỉnh đầu chớp chớp ngộ nghĩnh, hai vây ngực bè to như đôi tay đang chống nạng gỗ mini đòi nhảy khỏi cáng cứu thương dùng hai vây ngực chống nạng nhảy lóc chóc quanh chân bác sĩ rồi leo tót lên mép rèm cửa trố mắt nhìn; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Cô Ong Bắp Cày Ngọc đòi chích nọc thôi miên não gián thành zombie ngoan ngoãn!". Bố cục: cô Ong Bắp Cày Ngọc (emerald cockroach wasp) hoạt hình thân thon dài phát sáng xanh ngọc bích kim loại lộng lẫy, chân dài thanh mảnh, tay cầm chiếc dao mổ phẫu thuật thần kinh siêu nhỏ giơ lên đầy tự tin cầm dao vi phẫu thuật bay lượn tự tin, phía dưới là chú gián ngoan ngoãn cúi đầu bước theo sau; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Khối thịt 2 tấn Cá Mặt Trăng nằm bẹp dí ngơ ngác, chỉ đang tắm nắng sau chuyến lặn sâu 800 m!". Bố cục: chú Cá Mặt Trăng (ocean sunfish) hoạt hình khổng lồ hình đĩa tròn dẹt màu xám bạc, không có cuống đuôi, hai vây lưng và vây phần đuôi dựng đứng dài ngoằng, nằm ngửa trên chiếc cáng cứu thương quá khổ mắt to tròn ngơ ngác khổng lồ nằm ngửa trên cáng cứu thương mắt to tròn ngơ ngác, monitor ECG bên cạnh nhảy số nhịp tim chậm rì; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Vẹt Kakapo béo tròn 4 kg biểu diễn nhảy dù úp bụng xuống đống gối bông của y tá!". Bố cục: chú Vẹt Kakapo hoạt hình béo múp míp lông xanh rêu pha đốm nâu đen, mặt tròn lông tơ như chim cú mèo, mắt ngơ ngác dễ thương, hai cánh ngắn cũn cố vỗ lạch bạch trèo lên nóc tủ thuốc xòe hai cánh ngắn cũn rơi tự do úp nguyên cái bụng mỡ tròn vo xuống đống gối y tế trắng tinh; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Lợn Babirusa với 4 nanh cong vút xuyên sống mũi uốn ngược sát sạt hộp sọ!". Bố cục: chú Lợn Hươu Babirusa hoạt hình da xám nhăn nheo ít lông, mõm dài, bốn chiếc răng nanh cong vút dị thường trong đó hai nanh trên mọc xuyên qua sống mũi uốn ngược về phía trán, vẻ mặt lo lắng sờ trán giơ móng vuốt ve hai chiếc nanh hàm trên mọc ngược uốn cong chạm sát xương trán chụp trên phim CT; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Hươu Cao Cổ huyết áp vọt lên gần 300, tim 11 kg bơm nước màu ngược trọng lực lên chiếc cổ 2 m!". Bố cục: chú Hươu Cao Cổ hoạt hình cao lêu nghêu có đốm hoa văn nâu vàng, chiếc cổ dài thẳng tắp quấn dải băng đo huyết áp y tế to bản màu đỏ, mắt to hiền từ chớp chớp quấn dải băng đo huyết áp đỏ quanh cổ dài, đồng hồ áp suất nhảy mốc ba trăm mi-li-mét thủy ngân rung bần bật; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Nhím Lông Nhọn rụng 30.000 chiếc gai có ngạnh, nhưng tẩm sẵn lớp mỡ kháng sinh tự chữa lành thần tốc!". Bố cục: chú Nhím Lông Nhọn Bắc Mỹ hoạt hình béo tròn xù xì, toàn thân phủ kín ba mươi ngàn chiếc gai nhọn trắng đen, đang ôm chặt một thân cây gỗ gặm vỏ thuốc, người tỏa mùi tinh dầu thơm nhẹ xù ba mươi ngàn chiếc gai nhọn trắng đen, một sợi gai phóng to dưới kính hiển vi lộ rõ lớp màng mỡ kháng khuẩn; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Và Cò Mỏ Giày đứng như tượng đá rồi bất thần gõ mỏ súng máy 115 dB vang dội!". Bố cục: chú Cò Mỏ Giày hoạt hình lông xám tro, dáng đứng sừng sững bất động như tượng đá, chiếc mỏ khổng lồ màu vàng xám phình to hình chiếc guốc gỗ, ánh mắt lạnh như tiền đứng canh cửa phòng cấp cứu ngửa cổ đập hai hàm mỏ guốc khổng lồ vào nhau phát ra tia lửa và âm thanh súng máy làm y tá giật bắn người; KHÔNG có ông Bác Sĩ trong cảnh này.
```
</details>

<details><summary>S11</summary>

```text
HÌNH S11 (DỌC 9:16, Vintage Anatomical Atlas & 1950s Retro Hospital Illustration và nhân vật ông Bác Sĩ Trưởng Khoa áo blouse trắng cùng 10 bệnh nhân động vật hoạt hình kỳ lạ trong phòng cấp cứu bệnh viện; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bấm ngay vào video dài để cùng Bác Sĩ Trưởng Khoa khám phá ca trực đêm kinh hoàng này nhé!". Bố cục: ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án giơ bảng kẹp bệnh án da đen chỉ tay vào liên kết video dài với nụ cười sắc sảo đầy lôi cuốn.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/542 của video YouTube về 10 bệnh nhân quái kiệt — Phòng Cấp Cứu Tạo Hóa). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: ông Bác Sĩ Trưởng Khoa hoạt hình trung niên râu quai nón tỉa gọn, mặc áo blouse trắng có ống nghe y tế quàng qua cổ, kẹp bảng bệnh án bìa da, nét mặt sắc sảo mỉa mai nhưng ánh mắt tinh anh. Nhân vật phụ cố định: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng; ông Bác Sĩ Trưởng Khoa hoạt hình áo blouse trắng quàng ống nghe y tế và kẹp bảng bệnh án. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/11 của video YouTube Shorts về 10 bệnh nhân quái kiệt — Phòng Cấp Cứu Tạo Hóa). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: ông Bác Sĩ Trưởng Khoa hoạt hình trung niên râu quai nón tỉa gọn, mặc áo blouse trắng có ống nghe y tế quàng qua cổ, kẹp bảng bệnh án bìa da, nét mặt sắc sảo mỉa mai nhưng ánh mắt tinh anh. Nhân vật phụ: cô y tá thỏ hoạt hình mặc đồng phục y tá màu xanh phẫu thuật, đội mũ y tá chữ thập đỏ nhỏ nhắn, tay cầm khay thuốc và nhiệt kế, vẻ mặt hốt hoảng cuống cuồng. 
```
</details>

## 7. SEO

- **title:** [TẬP ĐẶC BIỆT] Phòng Cấp Cứu Tạo Hóa: Bác Sĩ Khám 10 Sinh Vật Kỳ Lạ Nhất Trái Đất
- **hook_paragraph:** Mười sinh vật sở hữu cơ thể kỳ dị nhất hành tinh — Khỉ Đột Lưng Bạc, Nhện Lặn Chuông, Cá Thòi Lòi, Ong Bắp Cày Ngọc, Cá Mặt Trăng, Vẹt Kakapo, Lợn Hươu Babirusa, Hươu Cao Cổ, Nhím Lông Nhọn và Cò Mỏ Giày — cùng lúc nhập viện cấp cứu lúc nửa đêm tại Phòng Cấp Cứu Tạo Hóa! Toàn bộ là kiến thức giải phẫu học và sinh lý học MỚI 100% chưa từng kể trong các tập lẻ: Khỉ đột lên men 70% calo từ ruột tịt, nhện dệt bình lặn khí nano thở 24h, cá thòi lòi ngậm nước mang đi bộ, ong ngọc châm kim vô hiệu hóa dopamine của gián, cá mặt trăng não 4 gam nặng 2 tấn đẻ 300 triệu trứng, babirusa nanh cong 40 phân xuyên trán, hươu cao cổ huyết áp 280 mmHg có tim 11kg và lưới Rete mirabile, nhím lông nhọn bôi kem mỡ kháng sinh diệt tụ cầu vàng, và cò mỏ giày gõ súng máy 115 dB! Mọi bí mật giải phẫu học rợn người sẽ được Bác Sĩ Trưởng Khoa giải phẫu toàn diện!
- **question:** Trong mười ca bệnh dị thường đêm nay, bạn thán phục cơ chế giải phẫu của sinh vật nào nhất? Hãy để lại bình luận cho Bác Sĩ Trưởng Khoa biết nhé!
- **next_teaser:** Mega 06: Chuyến Tàu Tốc Hành Xuyên Đêm — Vụ án mất tích bí ẩn giữa bão tuyết với 10 sát thủ thiên nhiên!
- **shorts_title:** Phòng Cấp Cứu 10 Sinh Vật Kỳ Lạ Nhất Trái Đất! 🏥 #shorts #dongvat
- **shorts_desc:** Còi báo động đỏ réo vang khi 10 sinh vật kỳ dị nhất hành tinh cùng nhập viện lúc nửa đêm! Bác Sĩ Trưởng Khoa sẽ giải phẫu ca trực đêm kinh hoàng này ra sao? 🏥\n👉 Xem trọn tập đặc biệt Mega 05 trên kênh Vẽ Chuyện Hoang Dã!
- **bullets:** Khỉ Đột Lưng Bạc: Bụng phình như trống vì nhà máy vi sinh vật lên men cellulose tạo 70% calo cơ bắp · Nhện Lặn Chuông: Chiếc bình dưỡng khí nano bằng bọt khí bạc bẫy oxy dưới nước suốt 24 giờ · Cá Thòi Lòi: Vây ngực chống nạng leo cây đước và khoang mang ngậm nước đóng kín đi dạo trên bùn · Ong Bắp Cày Ngọc: Nữ phẫu thuật viên thần kinh 2 mũi tiêm khóa dopamine biến gián thành zombie sống · Cá Mặt Trăng: Bộ não 4 gam điều khiển khối thịt 2 tấn, đẻ 300 triệu trứng và lớp áo giáp sụn gelatin · Vẹt Kakapo: Béo tròn 4 cân không biết bay, chạy bộ trên rêu và tỏa mùi hương xạ thảo mộc quyến rũ · Lợn Babirusa: Bốn chiếc nanh cong 40 phân đâm xuyên da mũi mọc ngược bảo vệ mắt trong tình yêu · Hươu Cao Cổ: Huyết áp tâm thu 280 mmHg, tim quái vật 11 cân và lưới mạch Rete mirabile chống nổ mạch não · Nhím Lông Nhọn: 30 ngàn mũi chông vi ngạnh ngược bọc lớp kem mỡ kháng sinh diệt tụ cầu vàng · Cò Mỏ Giày: Cú gõ mỏ súng máy 115 đê-xi-ben xé toạc màn đêm và tuyệt đỉnh thiền định săn mồi đầm lầy
- **tags:** sinh vật kỳ lạ nhất thế giới, động vật kỳ lạ nhất hành tinh, phòng cấp cứu tạo hóa, khỉ đột lưng bạc, cá thòi lòi cà mau, cá mặt trăng, vẹt kakapo, ong bắp cày ngọc, hươu cao cổ huyết áp, cò mỏ giày, nhím lông nhọn, lợn hươu babirusa, nhện lặn chuông, tiến hóa động vật, khoa học hài hước, vẽ chuyện hoang dã

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/mega-05-phong-cap-cuu-tao-hoa
python src/episode/pipeline.py tts    projects/mega-05-phong-cap-cuu-tao-hoa     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/mega-05-phong-cap-cuu-tao-hoa     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/mega-05-phong-cap-cuu-tao-hoa     # phải in 'spec OK'
python scripts/audit_beats.py projects/mega-05-phong-cap-cuu-tao-hoa              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/mega-05-phong-cap-cuu-tao-hoa --force
python scripts/beat_sheet.py projects/mega-05-phong-cap-cuu-tao-hoa               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/mega-05-phong-cap-cuu-tao-hoa/audio/shorts.wav projects/mega-05-phong-cap-cuu-tao-hoa/renders/mega-05-phong-cap-cuu-tao-hoa_shorts.mp4
python src/episode/pipeline.py qa     projects/mega-05-phong-cap-cuu-tao-hoa
python src/episode/pipeline.py seo    projects/mega-05-phong-cap-cuu-tao-hoa
python src/episode/episode_doc.py     projects/mega-05-phong-cap-cuu-tao-hoa
```

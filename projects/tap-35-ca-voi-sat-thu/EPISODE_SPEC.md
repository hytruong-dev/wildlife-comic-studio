# TẬP 35 — CÁ VOI SÁT THỦ · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-35-ca-voi-sat-thu`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-35-ca-voi-sat-thu`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F6` · **Persona giọng:** `ong_trum` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Cá Voi Sát Thủ |
| Tiêu đề YouTube | Bố Già Đại Dương: Chiến Thuật Sóng Thần & Bí Mật Khiến Cá Mập Trắng Tháo Chạy?! \| Tập 35 |
| Video dài | `renders/tap-35-ca-voi-sat-thu_long.mp4` — 9:55.0 (595.0s) |
| Shorts | `renders/tap-35-ca-voi-sat-thu_shorts.mp4` — 0:41.3 (41.3s) |
| Thumbnail | `renders/tap-35-ca-voi-sat-thu_thumbnail.jpg` |
| Số hình | dài 70 beat / 70 ảnh riêng; Shorts 12 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.11**, Shorts tempo tự tính (≥ 1.12) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/70 của video YouTube về Cá Voi Sát Thủ). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh khắc gỗ hàng hải Baroque cổ điển kết hợp huy hiệu Mafia biển sâu (Oceanic Syndicate & Nautical Baroque Woodcut): nét cọ mực tàu dày dặn sắc lạnh như tranh khắc kim loại thế kỷ 18, những ngọn sóng đại dương cuộn xoáy hoa văn baroque cổ điển, điểm nhấn huy hiệu mạ vàng vương giả và dấu ấn sáp đỏ quyền lực, tông màu xanh biển thẳm kết hợp đen tuyền uy quyền; NỀN TRẮNG TINH hoàn toàn, không watermark, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses). Nhân vật phụ cố định: Nữ Hoàng Bố Già Cá Voi Sát Thủ khổng lồ đeo chuỗi ngọc trai biển và vương miện cổ đại uy quyền; chú hải cẩu béo tròn ngơ ngác đeo kính râm nằm tắm nắng trên tảng băng trôi; chúa tể cá mập trắng to lớn hung dữ nhưng vẻ mặt đang hoảng loạn tột độ tháo chạy; người mẹ cá voi sát thủ Tahlequah ánh mắt chan chứa tình mẫu tử đang dùng trán nâng đứa con bé bỏng. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — GIA TỘC MẪU HỆ TỐI THƯỢNG VÀ QUYỀN LỰC ĐEN TRẮNG
*Thẻ chương:* BỐ GIÀ ĐẠI DƯƠNG XUẤT ĐẦU LỘ DIỆN: ĐẾ CHẾ THỐNG TRỊ BIỂN KHẢI HOÀN TOÀN KHÔNG CÓ KẺ THÙ TỰ NHIÊN

*Badge:* `LỜI MỜI GIA TỘC` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene01_p0.wav` (559 ký tự) · mood `tram_bi_an`

```text
Chào mừng các bạn bước vào thế giới ngầm không ánh sáng của đại dương bao la, nơi trật tự không được thiết lập bằng may rủi mà bằng quyền lực gia tộc tuyệt đối. [laughter] Trong thế giới đó, bất kỳ sinh vật nào cũng phải cúi đầu nép mình trước kẻ mang hai màu đen trắng huyền thoại. Người ta thường gọi chúng là Cá Voi Sát Thủ, nhưng trong từ điển sinh học, đây thực chất là loài cá heo lớn nhất hành tinh với chiều dài tới chín mét và nặng hơn sáu tấn. Chúng đứng đầu chuỗi thức ăn đại dương và hoàn toàn không có bất kỳ kẻ thù tự nhiên nào trên cõi đời này!
```
**Part 1** → `audio/vs/scene01_p1.wav` (61 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Dạ thưa Bố Già, cho cháu xin vào gia tộc bảo kê được không ạ?
```
**Part 2** → `audio/vs/scene01_p2.wav` (685 ký tự) · mood `hao_hung`

```text
[laughter] Chú cá con ngây thơ này muốn xin một chân trong gia tộc ư? Gia tộc của chúng ta đâu phải cái chợ mà ai thích bơi vào thì bơi! Điều thú vị nhất của đế chế này nằm ở chỗ, nó hoàn toàn không do những gã đực to xác cơ bắp thống trị. Quyền lực tối cao thuộc về các Nữ Hoàng Bố Già sống thọ tới tám mươi năm hoặc chín mươi năm. Chế độ mẫu hệ Matriarchy này đã vận hành bền vững suốt hàng triệu năm qua. Những vị Bố Già Đại Dương lão làng này nắm giữ toàn bộ bản đồ hải lưu, kinh nghiệm săn mồi, đường đi nước bước và mật mã bí mật của dòng tộc truyền qua nhiều thế hệ. Đừng dại dột nghĩ rằng bạn có thể làm loạn trong lãnh địa của một gia tộc mà Nữ Hoàng đã trị vì gần một thế kỷ!
```
**Part 3** → `audio/vs/scene01_p3.wav` (626 ký tự) · mood `don_dap`

```text
Các nhà khoa học thần kinh biển đã chứng minh: Trong mỗi bầy cá voi sát thủ, các Nữ Hoàng Bố Già đóng vai trò là kho tàng tri thức sống còn của cả dòng họ. Khi biển động, băng tan hay nguồn thức ăn khan hiếm, cả bầy hàng chục con lớn nhỏ đều nhất mực bơi theo sự dẫn dắt của bà trùm lão luyện. Khác với hầu hết các loài động vật đực thường rời đàn khi trưởng thành, những gã đực cá voi sát thủ dẫu có to lớn đến chín mét vẫn ngoan ngoãn bơi bên cạnh mẹ suốt cả cuộc đời! Sự kỷ luật thép và lòng trung thành gia tộc tuyệt đối chính là nền tảng biến loài săn mồi này thành những ông trùm bất khả chiến bại của toàn bộ đại dương!
```
**Part 4** → `audio/vs/scene01_p4.wav` (440 ký tự) · mood `hao_hung`

```text
Hơn thế nữa, vây lưng của những gã đực cao tới gần hai mét sừng sững như một chiếc cột buồm đen tuyền xé toạc mặt nước biển. Tốc độ bơi tối đa của chúng có thể đạt tới năm mươi lăm kilômét trên giờ, nhanh như một chiếc ca nô cao tốc quân sự! Kết hợp giữa sức mạnh thể chất áp đảo và bộ óc chiến lược siêu việt của Nữ Hoàng, không có bất kỳ mục tiêu nào trong đại dương có thể thoát khỏi tầm ngắm một khi gia tộc Bố Già đã quyết định ra tay!
```

### scene02 — ĐÒN SÓNG THẦN ĐỒNG BỘ HẠ GỤC HẢI CẨU
*Thẻ chương:* PHI ĐỘI TIÊM KÍCH ĐẠI DƯƠNG: PHỐI HỢP BƠI ĐỒNG BỘ TẠO CỘT SÓNG CHÉM NỨT ĐÔI TẢNG BĂNG TRÔI

*Badge:* `CHIẾN THUẬT SÓNG THẦN` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene02_p0.wav` (458 ký tự) · mood `tram_bi_an`

```text
Hãy quan sát một phi vụ đi săn điển hình tại vùng biển băng giá Nam Cực để thấy được đỉnh cao của sự phối hợp quân sự. Khi một chú hải cẩu đang nằm ung dung sưởi nắng trên tảng băng trôi kiên cố giữa đại dương, nó cứ ngỡ mình đã an toàn tuyệt đối trước mọi kẻ săn mồi. [laughter] Nhưng đàn cá voi sát thủ không bao giờ lao vào húc bừa bãi như những kẻ thiếu học thức. Bố Già Đại Dương luôn hành động với sự chuẩn xác lạnh lùng của những tay sát thủ nhà nghề!
```
**Part 1** → `audio/vs/scene02_p1.wav` (71 ký tự) · 🎭 cameo `ga_khong_lo`

```text
Ủa tôi nằm trên tảng băng to đùng thế này mà sao nước dâng tới cổ rồi?!
```
**Part 2** → `audio/vs/scene02_p2.wav` (577 ký tự) · mood `hao_hung`

```text
[surprise-oh] Nước dâng tới cổ là còn may đấy, lát nữa sẽ rơi thẳng vào miệng trùm sò! Các bạn hãy nhìn đội hình tác chiến của chúng: Bốn thành viên bơi dàn hàng ngang hoàn hảo như một phi đội tiêm kích tàng hình, giữ cự ly đều đặn từng centimet dưới mặt nước trong vắt. Khi cách tảng băng khoảng mười lăm mét, Nữ Hoàng phát lệnh lặn xuống cùng lúc và dùng những chiếc đuôi khổng lồ quạt mạnh tạo nên một cơn sóng thần nhân tạo cực lớn! [laughter] Cột sóng quét ngang làm nứt đôi tảng băng trôi kiên cố, hất tung chú hải cẩu rơi tõm xuống nước ngay trước hàm răng đang chờ sẵn!
```
**Part 3** → `audio/vs/scene02_p3.wav` (407 ký tự) · mood `don_dap`

```text
Nhưng điều đáng kinh ngạc hơn cả là sau khi con mồi rơi xuống biển, không hề có bất kỳ sự tranh giành cắn xé hỗn loạn nào. Nữ Hoàng Bố Già cùng các thành viên phối hợp ghìm giữ con mồi, dạy cho những chú cá voi con cách thức ra đòn, rồi chia sẻ miếng ăn sòng phẳng cho từng thành viên trong gia đình theo đúng tôn ti trật tự gia tộc. Đó là một bài học quân sự kinh điển về sức mạnh đồng đội và kỷ luật thép!
```
**Part 4** → `audio/vs/scene02_p4.wav` (405 ký tự) · mood `hao_hung`

```text
Thậm chí các nhà làm phim tài liệu của đài BBC đã từng ghi lại cảnh tượng khó tin: Nếu con mồi rơi xuống nước nhưng chưa bị thương nặng, các sát thủ trưởng thành sẽ dùng mõm đẩy nhẹ con hải cẩu trở lại tảng băng để đàn con thực hành lại đợt tạo sóng lần thứ hai! Đây không đơn thuần là hành vi săn mồi để sinh tồn, mà là một trường học huấn luyện quân sự thực thụ được truyền lại từ đời này sang đời khác!
```

### scene03 — CA PHẪU THUẬT CHÍNH XÁC CỦA BỘ ĐÔI PORT VÀ STARBOARD
*Thẻ chương:* CHÚA TỂ CÁ MẬP TRẮNG THÁO CHẠY HÀNG NĂM TRỜI TRƯỚC BỘ ĐÔI SÁT THỦ XÉ GAN TẠI NAM PHI

*Badge:* `HỒ SƠ KHÉP LẠI` · *mood mặc định:* `nghiem_trang_gia`

**Part 0** → `audio/vs/scene03_p0.wav` (492 ký tự) · mood `tram_bi_an`

```text
Nếu bạn từng xem các bộ phim kinh dị bom tấn của Hollywood và đinh ninh rằng Cá Mập Trắng là hung thần vô địch thống trị biển cả, thì bạn đã bị truyền thông đánh lừa một cú ngoạn mục rồi! [laughter] Đối với Bố Già Đại Dương, cá mập trắng khét tiếng chỉ là một món ăn vặt bổ dưỡng có lá gan béo ngậy. Năm hai ngàn không trăm hai mươi hai, tại vùng vịnh Gansbaai ở Nam Phi, giới khoa học chấn động khi phát hiện xác hàng loạt cá mập trắng dạt vào bờ với đúng một vết rách tinh vi dưới vây ngực!
```
**Part 1** → `audio/vs/scene03_p1.wav` (72 ký tự) · 🎭 cameo `cong_to_vien`

```text
Thưa quý tòa, chứng cứ hiện trường cho thấy đây là vụ giải phẫu tinh vi!
```
**Part 2** → `audio/vs/scene03_p2.wav` (665 ký tự) · mood `hao_hung`

```text
[surprise-oh] Quá chính xác thưa công tố viên! Hiện trường vụ án kỳ lạ tới mức khó tin: Toàn bộ phần thịt thăn thơm ngon của cá mập trắng hoàn toàn nguyên vẹn, chỉ riêng lá gan nặng hàng trăm kilogram giàu lipid đã bị xé sạch không còn một mảnh vụn! Thủ phạm chính là bộ đôi sát thủ lừng danh mang tên Port và Starboard. Chúng nắm rõ điểm yếu sinh học chí mạng của loài cá mập: chỉ cần tung cú húc lật ngửa con cá mập khiến nó rơi vào trạng thái bất động trương lực cơ bắp, cá mập sẽ tê liệt hoàn toàn và ngạt thở trong vài phút. Sau đó, chúng rạch một đường chính xác đến từng milimét dưới vây ngực để rút trọn buồng gan béo bở rồi vứt bỏ toàn bộ phần xác còn lại!
```
**Part 3** → `audio/vs/scene03_p3.wav` (375 ký tự) · mood `don_dap`

```text
Đòn thanh trừng thị uy này khủng khiếp đến mức toàn bộ quần thể cá mập trắng tại vùng biển Nam Phi khiếp vía bỏ chạy, sơ tán khẩn cấp hàng trăm dặm và không dám bén mảng quay lại vùng biển suốt cả năm trời! Các nhà sinh học biển phải thốt lên rằng: Đây không phải là sự săn mồi ngẫu nhiên, mà là sự thống trị tuyệt đối về mặt tâm lý và kỹ năng tác chiến của Bố Già Đại Dương!
```
**Part 4** → `audio/vs/scene03_p4.wav` (423 ký tự) · mood `tram_bi_an`

```text
Trước khi bộ đôi Port và Starboard xuất hiện, vịnh Gansbaai từng là thủ phủ ngắm cá mập trắng nổi tiếng thế giới thu hút hàng triệu du khách. Nhưng kể từ khi hai sát thủ vây lưng cong ghé thăm, các thiết bị định vị vệ tinh gắn trên mình cá mập trắng ghi nhận sự hoảng loạn tột độ. Chúng lặn sâu xuống hàng trăm mét và tháo chạy tán loạn khắp đại dương, chứng minh ai mới thực sự là kẻ nắm giữ quyền lực sinh sát tối thượng!
```

### scene04 — TIẾNG LÓNG ÂM THANH VÀ THỰC ĐƠN GIA TRUYỀN
*Thẻ chương:* BĂNG ĐẢNG MAFIA ĐẠI DƯƠNG: MỖI GIA TỘC CÓ PHƯƠNG NGỮ RIÊNG VÀ KHÔNG BAO GIỜ ĂN CHUNG THỰC ĐƠN

*Badge:* `VĂN HÓA GIA TỘC` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene04_p0.wav` (391 ký tự) · mood `tram_bi_an`

```text
Điều khiến các nhà sinh vật học hành vi kinh ngạc nhất về cá voi sát thủ chính là tính biệt lập văn hóa sâu sắc giữa các dòng tộc. Chúng phân hóa thành nhiều chủng loại sinh thái khác nhau và tuyệt đối không bao giờ giao lưu, bơi chung hay kết hôn bừa bãi. [laughter] Giống như các gia tộc quyền quý thời xưa, mỗi chi nhánh đều giữ gìn danh dự và bản sắc ẩm thực riêng biệt của dòng họ mình!
```
**Part 1** → `audio/vs/scene04_p1.wav` (73 ký tự) · 🎭 cameo `co_tro_ly`

```text
Báo cáo Bố Già, chi nhánh miền Bắc chỉ ăn cá hồi, không chịu ăn thịt thú!
```
**Part 2** → `audio/vs/scene04_p2.wav` (611 ký tự) · mood `hao_hung`

```text
[laughter] Rất đúng chất dòng tộc quý tộc! Chi nhánh cá voi cư trú ven bờ chỉ trung thành với món cá hồi béo ngậy. Chúng nhìn chi nhánh du cư chuyên đi săn hải cẩu và cá voi con bằng nửa con mắt, xem đó là những kẻ ăn thịt man rợ cục súc! Ngược lại, nhóm ngoài khơi xa chỉ đam mê lùng sục các loài cá mập đại dương. Chưa dừng lại ở đó, mỗi gia tộc sở hữu một hệ thống phương ngữ âm thanh độc nhất vô nhị. [surprise-oh] Giống như tiếng lóng của các băng đảng Mafia ở New York, những âm thanh lách cách và tiếng huýt sáo của gia tộc này thì gia tộc hàng xóm hoàn toàn nghe như ngoại ngữ và không thể nào hiểu nổi!
```
**Part 3** → `audio/vs/scene04_p3.wav` (345 ký tự) · mood `don_dap`

```text
Những chú cá voi con mới sinh phải mất nhiều năm trời theo mẹ học tập từng ngữ điệu âm thanh của dòng tộc, tiếp thu toàn bộ danh mục ẩm thực gia truyền và quy tắc ứng xử trước khi được giao phó trọng trách săn mồi. Đây chính là bằng chứng xác thực về sự tồn tại của văn hóa truyền miệng và truyền thống gia đình trong thế giới động vật hoang dã!
```
**Part 4** → `audio/vs/scene04_p4.wav` (383 ký tự) · mood `hao_hung`

```text
Các nghiên cứu giải mã tần số âm thanh kéo dài hơn ba mươi năm tại bờ biển Bắc Mỹ cho thấy: Ngay cả khi hai gia tộc bơi ngang qua nhau trong cùng một eo biển hẹp, chúng chỉ giữ khoảng cách lịch sự và không bao giờ hòa lẫn tiếng gọi bầy. Mỗi gia tộc tự hào với phương ngữ riêng biệt của mình, tạo nên một bức tranh đa văn hóa vô cùng phong phú và độc bản dưới lòng đại dương sâu thẳm!
```

### scene05 — TÌNH MẪU TỬ MƯỜI BẢY NGÀY LAY ĐỘNG ĐẠI DƯƠNG
*Thẻ chương:* KHỐI NÃO NẶNG NĂM KILOGRAM SỞ HỮU THÙY PARALIMBIC PHỨC TẠP HƠN CẢ NÃO BỘ CON NGƯỜI

*Badge:* `TRÁI TIM BỐ GIÀ` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene05_p0.wav` (463 ký tự) · mood `tram_bi_an`

```text
Phía sau lớp vỏ bọc lạnh lùng của những tay săn mồi tàn bạo nhất đại dương, não bộ của cá voi sát thủ sở hữu một bí mật làm rúng động giới khoa học thần kinh. Khối não nặng tới năm kilôgam của chúng có hệ thống thùy paralimbic phát triển vượt bậc, thậm chí còn phân nhánh phức tạp hơn cả cấu trúc tương ứng trong não bộ con người chúng ta! Đây chính là trung tâm chi phối các kết nối xã hội sâu sắc, sự thấu cảm, lòng vị tha và cả nỗi đau buồn mất mát khôn nguôi.
```
**Part 1** → `audio/vs/scene05_p1.wav` (71 ký tự) · 🎭 cameo `ong_gia_ke`

```text
Mười bảy ngày ròng rã đẩy xác con... tình mẹ làm lay động cả đại dương!
```
**Part 2** → `audio/vs/scene05_p2.wav` (575 ký tự) · mood `am_ap`

```text
[sigh] Đúng vậy thưa các bạn. Vào Năm hai ngàn không trăm mười tám, cả thế giới đã rơi nước mắt trước hình ảnh người mẹ cá voi mang tên Tahlequah. Khi đứa con sơ sinh không may qua đời chỉ sau nửa giờ chào đời, thay vì để xác con chìm xuống đáy biển lạnh giá, người mẹ đau thương ấy đã dùng trán nâng xác con, bơi ròng rã suốt mười bảy ngày qua quãng đường hơn một ngàn dặm trên biển Thái Bình Dương! Suốt mười bảy ngày đêm tang tóc đó, các thành viên trong gia tộc đã lặng lẽ bơi bên cạnh hộ tống, thay phiên nhau nhường thức ăn và hỗ trợ người mẹ vượt qua nỗi đau tột cùng.
```
**Part 3** → `audio/vs/scene05_p3.wav` (270 ký tự) · mood `don_dap`

```text
Hình ảnh đó đã chứng minh cho toàn thể nhân loại thấy rằng: Bố Già Đại Dương không chỉ có sức mạnh cơ bắp và sự tàn bạo trên bàn tiệc săn mồi, mà sâu thẳm bên trong là một trái tim tràn ngập tình yêu thương mẫu tử và sự gắn kết gia đình thiêng liêng lay động lòng người!
```
**Part 4** → `audio/vs/scene05_p4.wav` (365 ký tự) · mood `am_ap`

```text
Đặc biệt hơn, cá voi sát thủ là một trong số cực kỳ ít ỏi các loài sinh vật trên Trái Đất cùng với con người trải qua giai đoạn mãn kinh. Sau khi hết khả năng sinh sản ở bốn mươi tuổi, các bà mẹ tiếp tục sống thêm tới bốn mươi năm hay năm mươi năm nữa chỉ để làm nhiệm vụ bà ngoại, chăm sóc các cháu và hướng dẫn con cháu vượt qua những thời khắc bão tố hiểm nghèo!
```

### scene06 — ĐIỀU RĂN CẤM TUYỆT ĐỐI KHÔNG CHẠM VÀO LOÀI NGƯỜI
*Thẻ chương:* BẢN HIỆP ƯỚC HÒA BÌNH TRIỆU NĂM: TẠI SAO CÁ VOI SÁT THỦ NGOÀI TỰ NHIÊN CHƯA TỪNG TẤN CÔNG CON NGƯỜI?

*Badge:* `ĐIỀU RĂN CẤM TỐI CAO` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (362 ký tự) · mood `tram_bi_an`

```text
Có một nghịch lý vĩ đại đã làm đau đầu các nhà sinh thái học suốt nhiều thế kỷ qua: Tại sao một loài động vật ăn thịt có thể xé xác cá voi xanh khổng lồ bốn mươi tấn, giết cá mập trắng trong nháy mắt, nhưng trong toàn bộ lịch sử nhân loại chưa từng ghi nhận một vụ tấn công giết người nào ngoài tự nhiên hoang dã? [laughter] Đúng vậy, bạn không hề nghe nhầm đâu!
```
**Part 1** → `audio/vs/scene06_p1.wav` (66 ký tự) · 🎭 cameo `ba_trum`

```text
Hãy nhớ lấy điều luật số một của gia tộc: Cấm đụng vào loài người!
```
**Part 2** → `audio/vs/scene06_p2.wav` (455 ký tự) · mood `hao_hung`

```text
[laughter] Lời dặn dò nghiêm khắc của Bà Trùm lão làng chính là sự thật! Ngoại trừ những thảm kịch đáng tiếc xảy ra tại các bể xiếc giam cầm do cá voi bị trầm cảm và căng thẳng tâm lý tột độ, thì ngoài đại dương tự do, cá voi sát thủ đối xử với con người vô cùng kỳ lạ. Chúng sẵn sàng hợp tác cùng các ngư dân vịnh Eden ở nước Úc để lùa cá voi vào bờ chia phần, hoặc tò mò bơi sát mạn thuyền ngoi lên nhìn ngắm con người bằng ánh mắt ôn hòa và thân thiện!
```
**Part 3** → `audio/vs/scene06_p3.wav` (621 ký tự) · mood `don_dap`

```text
Dường như trong bộ luật bất thành văn của Bố Già Đại Dương, có một điều răn cấm tối cao đã được khắc sâu qua hàng triệu năm tiến hóa: Loài hai chân trên cạn là đối tác hòa bình, tuyệt đối không được coi là thức ăn! Sự tôn trọng kỳ lạ đó chính là nét quý tộc vương giả của những kẻ cai trị biển cả. Còn bây giờ, giữa chiến thuật sóng thần chém nứt tảng băng và ca phẫu thuật xé gan Cá Mập Trắng, bạn nể phục quyền lực nào nhất của Bố Già Đại Dương? Hãy để lại ý kiến bình luận bên dưới nhé! Và đừng quên bấm đăng ký kênh để đón xem Tập ba mươi sáu khám phá cỗ máy giảm chấn sọ não một ngàn hai trăm G của Chim Gõ Kiến nhé!
```
**Part 4** → `audio/vs/scene06_p4.wav` (189 ký tự) · mood `am_ap`

```text
Hãy cùng lan tỏa thông điệp bảo vệ các đại dương và tôn trọng những gia tộc cá voi sát thủ kỳ diệu này, để tiếng huýt sáo của Bố Già Đại Dương mãi mãi ngân vang tự do giữa biển khơi bao la!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Bạn có biết tại sao chúa tể săn mồi Cá Mập Trắng lại phải hoảng loạn bỏ chạy suốt cả năm trời chỉ vì đánh hơi thấy bóng dáng của Cá Voi Sát Thủ không? [dissatisfaction-hnn] Tại vùng biển Nam Phi, hai sát thủ mang tên Port và Starboard đã thực hiện những phi vụ trừng phạt chấn động giới sinh vật biển. Chúng không thèm ăn thịt cá mập mà dùng chiến thuật húc lật ngửa con mồi để kích hoạt trạng thái tê liệt bất động, sau đó rạch một đường chính xác đến từng milimét chỉ để xé lấy buồng gan giàu chất béo rồi vứt bỏ toàn bộ phần xác còn lại! [laughter] Cuộc phẫu thuật tinh vi đến mức khiến toàn bộ đàn cá mập trắng trong bán kính hàng trăm dặm lập tức sơ tán khẩn cấp không dám quay lại suốt cả năm trời. Đó chính là uy quyền tuyệt đối của Bố Già Đại Dương!
```

**Whisper prompt:** `Cá Voi Sát Thủ, Bố Già Đại Dương, Orca, Orcinus orca, Port và Starboard, Nam Phi, Nam Cực, Matriarchy, Hải cẩu, Cá Mập Trắng, Tahlequah, Gansbaai`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| Năm hai ngàn không trăm hai mươi hai | Năm 2022 |
| Năm hai ngàn không trăm mười tám | Năm 2018 |
| Năm hai ngàn không trăm mười hai | Năm 2012 |
| Tập ba mươi lăm | Tập 35 |
| Tập ba mươi sáu | Tập 36 |
| tám mươi năm | 80 năm |
| chín mươi năm | 90 năm |
| mười bảy ngày | 17 ngày |
| Mười bảy ngày | 17 ngày |
| mười lăm mét | 15m |
| chín mét | 9m |
| hai mét | 2m |
| sáu tấn | 6 tấn |
| bốn mươi tấn | 40 tấn |
| năm mươi lăm kilômét trên giờ | 55 km/h |
| một ngàn dặm | 1.000 dặm |
| một ngàn hai trăm | 1.200 |
| năm kilôgam | 5kg |
| sáu mươi phần trăm | 60% |
| một trăm phần trăm | 100% |
| bốn loài | 4 loài |
| bốn thành viên | 4 thành viên |
| hai mươi phút | 20 phút |
| hai mươi lăm năm | 25 năm |
| ba mươi năm | 30 năm |
| bốn mươi tuổi | 40 tuổi |
| bốn mươi năm | 40 năm |
| năm mươi năm | 50 năm |
| triệu năm | triệu năm |
| hàng triệu năm | hàng triệu năm |
| Port | Port |
| Starboard | Starboard |
| Tahlequah | Tahlequah |
| Orcinus | Orcinus |
| Delphinidae | Delphinidae |
| Matriarchy | Matriarchy |
| Gangs of New York | Gangs of New York |
| Godfather | Godfather |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · GIA TỘC MẪU HỆ TỐI THƯỢNG VÀ QUYỀN LỰC ĐEN TRẮNG · 118.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:05.9 (5.9s) | L01 | Chào mừng các bạn bước vào thế giới ngầm không ánh sáng của đại dương bao la, nơi trật tự không được thiết lập bằng may rủi |  | Đại dương sâu thẳm mở ra với cánh cổng Mafia huyền bí: chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) đứng sừng sững ở vị trí trung tâm, hai ta |
| b02 | 00:05.9–00:13.3 (7.3s) | L02 | mà bằng quyền lực gia tộc tuyệt đối. Trong thế giới đó, bất kỳ sinh vật nào cũng phải cúi đầu nép mình trước kẻ mang hai màu đen trắng huyền thoại. |  | Cận cảnh ánh mắt sắc lạnh đeo kính râm của chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses), phản chiếu hình ảnh muôn loài sinh vật biển đang cúi |
| b03 | 00:13.3–00:22.0 (8.7s) | L03 | Người ta thường gọi chúng là Cá Voi Sát Thủ, nhưng trong từ điển sinh học, đây thực chất là loài cá heo lớn nhất hành tinh với chiều dài tới 9m và nặng hơn 6 tấn. | **9 MÉT** · chiều dài cơ thể · L/280 · [0.35, 0.45]<br>**6 TẤN** · trọng lượng áp đảo · R/280 · [0.65, 0.45] | Sơ đồ giải phẫu kích thước khổng lồ: chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) bơi ngang thước đo 9m và cán cân 6 tấn, bên cạnh là một chú |
| b04 | 00:22.0–00:31.6 (9.6s) | L04 | Chúng đứng đầu chuỗi thức ăn đại dương và hoàn toàn không có bất kỳ kẻ thù tự nhiên nào trên cõi đời này! Dạ thưa Bố Già, cho cháu xin vào gia tộc bảo kê được không ạ? |  | Kim tự tháp sinh thái đại dương: chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) ngự trị trên đỉnh cao nhất, bên dưới là cá mập, hải cẩu, cá voi |
| b05 | 00:31.6–00:44.6 (13.0s) | L05 | Chú cá con ngây thơ này muốn xin một chân trong gia tộc ư? Gia tộc của chúng ta đâu phải cái chợ mà ai thích bơi vào thì bơi! Điều thú vị nhất của đế chế này nằm ở chỗ, nó hoàn toàn không do những gã đực to xác cơ bắp thống trị. Quyền lực tối cao thuộc |  | Khung cảnh hài hước: Chú cá con bé xíu run rẩy chắp tay xin việc trước bàn làm việc gỗ gụ khổng lồ của chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sungl |
| b06 | 00:44.6–00:54.4 (9.8s) | L06 | về các Nữ Hoàng Bố Già sống thọ tới 80 năm hoặc 90 năm. Chế độ mẫu hệ Matriarchy này đã vận hành bền vững suốt hàng triệu năm qua. Những vị Bố Già Đại Dương lão làng này nắm giữ toàn | **90 NĂM** · tuổi thọ Nữ Hoàng · R/280 · [0.6, 0.5] | Chân dung tráng lệ của Nữ Hoàng Bố Già Cá Voi Sát Thủ khổng lồ đeo chuỗi ngọc trai biển và vương miện cổ đại uy quyền: Thọ 90 năm, ánh mắt thông tuệ nắm giữ tấm bản đồ hải lưu bí truyền dẫn đường cho cả gia tộc vượt bão tố. |
| b07 | 00:54.4–01:04.4 (10.0s) | L07 | bộ bản đồ hải lưu, kinh nghiệm săn mồi, đường đi nước bước và mật mã bí mật của dòng tộc truyền qua nhiều thế hệ. Đừng dại dột nghĩ rằng bạn có thể làm loạn trong lãnh địa của một gia tộc mà Nữ |  | Bản đồ gia phả Mafia đại dương vẽ theo phong cách gia tộc cổ điển: Nữ Hoàng Bố Già Cá Voi Sát Thủ khổng lồ đeo chuỗi ngọc trai biển và vương miện cổ đại uy quyền uy nghi tọa lạc ở đỉnh cao nhất, xung quanh là các thế hệ con cháu quy phục. |
| b08 | 01:04.4–01:11.0 (6.6s) | L08 | Hoàng đã trị vì gần một thế kỷ! Các nhà khoa học thần kinh biển đã chứng minh: Trong mỗi bầy cá voi sát thủ, các Nữ Hoàng Bố Già đóng vai trò |  | Bố Già lão làng đội vương miện ngọc trai biển ngồi trên ngai san hô, tay cầm quyền trượng san hô chỉ huy dòng hải lưu. |
| b09 | 01:11.0–01:25.6 (14.6s) | L09 | là kho tàng tri thức sống còn của cả dòng họ. Khi biển động, băng tan hay nguồn thức ăn khan hiếm, cả bầy hàng chục con lớn nhỏ đều nhất mực bơi theo sự dẫn dắt của bà trùm lão luyện. Khác với hầu hết các loài động vật đực thường rời đàn khi trưởng thành, những gã đực cá voi sát thủ dẫu có to lớn đến 9m |  | Cảnh tượng bão tố biển động dữ dội: Cả bầy hàng chục con cá voi sát thủ bơi rẽ sóng răm rắp theo sau đường bơi của Nữ Hoàng Bố Già Cá Voi Sát Thủ khổng lồ đeo chuỗi ngọc trai biển và vương miện cổ đại uy quyền. |
| b10 | 01:25.6–01:36.3 (10.8s) | L10 | vẫn ngoan ngoãn bơi bên cạnh mẹ suốt cả cuộc đời! Sự kỷ luật thép và lòng trung thành gia tộc tuyệt đối chính là nền tảng biến loài săn mồi này thành những ông trùm bất khả chiến bại của toàn bộ đại dương! Hơn thế nữa, |  | Cảnh tượng hài hước ấm áp: Một gã cá voi đực to lớn lực lưỡng cao 9m nhưng bơi nép sát bên cạnh cá voi mẹ, ngoan ngoãn lắng nghe lời dạy bảo. |
| b11 | 01:36.3–01:46.2 (9.9s) | L11 | vây lưng của những gã đực cao tới gần 2m sừng sững như một chiếc cột buồm đen tuyền xé toạc mặt nước biển. Tốc độ bơi tối đa của chúng có thể đạt tới 55 km/h, nhanh | **2 MÉT** · chiều cao vây lưng · L/280 · [0.45, 0.4]<br>**55 KM/H** · tốc độ tối đa · R/280 · [0.6, 0.55] | Chiếc vây lưng hình tam giác khổng lồ cao 2m của chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) nhô thẳng đứng khỏi mặt nước biển rẽ sóng, bên  |
| b12 | 01:46.2–01:58.2 (12.0s) | L12 | như một chiếc ca nô cao tốc quân sự! Kết hợp giữa sức mạnh thể chất áp đảo và bộ óc chiến lược siêu việt của Nữ Hoàng, không có bất kỳ mục tiêu nào trong đại dương có thể thoát khỏi tầm ngắm một khi gia tộc Bố Già đã quyết định ra tay! |  | Toàn cảnh gia tộc cá voi sát thủ bơi rẽ sóng đại dương, chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) dẫn đầu giương cao lá cờ gia huy mạ vàng |

### scene02 · ĐÒN SÓNG THẦN ĐỒNG BỘ HẠ GỤC HẢI CẨU · 96.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:14.9 (14.9s) | L13 | Hãy quan sát một phi vụ đi săn điển hình tại vùng biển băng giá Nam Cực để thấy được đỉnh cao của sự phối hợp quân sự. Khi một chú hải cẩu đang nằm ung dung sưởi nắng trên tảng băng trôi kiên cố giữa đại dương, nó cứ ngỡ mình đã an toàn tuyệt đối trước mọi kẻ săn mồi. Nhưng đàn cá voi |  | Cảnh tượng băng giá Nam Cực trắng xóa: chú hải cẩu béo tròn ngơ ngác đeo kính râm nằm tắm nắng trên tảng băng trôi đang nằm phơi bụng sưởi nắng trên một tảng băng trôi kiên cố, vẻ mặt lười biếng tận hưởng cuộc sống. |
| b02 | 00:14.9–00:19.6 (4.7s) | L14 | sát thủ không bao giờ lao vào húc bừa bãi như những kẻ thiếu học thức. Bố Già Đại Dương luôn hành động |  | Dưới làn nước biển trong vắt: chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) cùng 3 thành viên gia tộc bơi dàn hàng ngang tàng hình như một phi |
| b03 | 00:19.6–00:26.9 (7.3s) | L15 | với sự chuẩn xác lạnh lùng của những tay sát thủ nhà nghề! Ủa tôi nằm trên tảng băng to đùng thế này mà sao nước dâng tới cổ rồi?! |  | Góc nhìn từ trên cao xuống mặt biển xanh ngắt: 4 cái bóng đen khổng lồ lướt đi song song tuyệt đối dưới lớp băng mỏng. |
| b04 | 00:26.9–00:40.8 (13.8s) | L16 | Nước dâng tới cổ là còn may đấy, lát nữa sẽ rơi thẳng vào miệng trùm sò! Các bạn hãy nhìn đội hình tác chiến của chúng: Bốn thành viên bơi dàn hàng ngang hoàn hảo như một phi đội tiêm kích tàng hình, giữ cự ly đều đặn từng centimet dưới mặt nước trong vắt. |  | Sơ đồ khí động học sóng biển: 4 chiếc đuôi khổng lồ quạt mạnh đồng bộ dưới nước, đẩy lên một luồng áp suất cực đại hướng thẳng về phía tảng băng. |
| b05 | 00:40.8–00:49.4 (8.6s) | L17 | Khi cách tảng băng khoảng 15m, Nữ Hoàng phát lệnh lặn xuống cùng lúc và dùng những chiếc đuôi khổng lồ quạt mạnh tạo nên một cơn sóng thần nhân tạo cực lớn! | **15 MÉT** · cự ly tạo sóng · R/280 · [0.5, 0.6] | Thước đo cự ly tác chiến: Điểm đánh dấu cách mép băng đúng 15m, nơi hiệu lệnh đồng bộ được phát ra. |
| b06 | 00:49.4–00:54.5 (5.1s) | L18 | Cột sóng quét ngang làm nứt đôi tảng băng trôi kiên cố, hất tung chú hải cẩu rơi tõm |  | Cơn sóng thần dâng cao đánh sập mép băng: Tảng băng nứt toác làm đôi, chú hải cẩu béo tròn ngơ ngác đeo kính râm nằm tắm nắng trên tảng băng trôi hoảng hốt trượt chân rơi thẳng xuống mặt nước sủi bọt trắng xóa. |
| b07 | 00:54.5–00:59.6 (5.1s) | L19 | xuống nước ngay trước hàm răng đang chờ sẵn! Nhưng điều đáng kinh ngạc hơn cả là sau khi con mồi rơi xuống biển, |  | Cận cảnh khoảnh khắc kịch tính: Hàm răng sắc nhọn hé mở dưới làn nước sủi bọt, chú hải cẩu hoảng hốt mở to mắt. |
| b08 | 00:59.6–01:07.3 (7.8s) | L20 | không hề có bất kỳ sự tranh giành cắn xé hỗn loạn nào. Nữ Hoàng Bố Già cùng các thành viên phối hợp ghìm giữ con mồi, dạy cho những chú cá voi con cách thức ra đòn, |  | Vòng tròn gia đình kỷ luật: chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) cùng các thành viên nhẹ nhàng vây quanh con mồi, chia sẻ thức ăn the |
| b09 | 01:07.3–01:15.4 (8.1s) | L21 | rồi chia sẻ miếng ăn sòng phẳng cho từng thành viên trong gia đình theo đúng tôn ti trật tự gia tộc. Đó là một bài học quân sự kinh điển về sức mạnh đồng đội và kỷ luật thép! |  | Lớp học săn mồi của Bố Già: chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) dùng mõm đẩy nhẹ chú hải cẩu lên mép băng để hướng dẫn 2 chú cá voi  |
| b10 | 01:15.4–01:22.9 (7.5s) | L22 | Thậm chí các nhà làm phim tài liệu của đài BBC đã từng ghi lại cảnh tượng khó tin: Nếu con mồi rơi xuống nước nhưng chưa bị thương nặng, |  | Bảng tổng kết chiến thuật sóng thần Nam Cực: Sơ đồ tác chiến phối hợp 4 bước hoàn hảo của Bố Già Đại Dương. |
| b11 | 01:22.9–01:36.5 (13.6s) | L23 | các sát thủ trưởng thành sẽ dùng mõm đẩy nhẹ con hải cẩu trở lại tảng băng để đàn con thực hành lại đợt tạo sóng lần thứ hai! Đây không đơn thuần là hành vi săn mồi để sinh tồn, mà là một trường học huấn luyện quân sự thực thụ được truyền lại từ đời này sang đời khác! |  | Hình ảnh thế hệ con cháu kế thừa: Hai chú cá voi con bơi theo sát vây lưng mẹ, thực hiện động tác quạt đuôi điêu luyện. |

### scene03 · CA PHẪU THUẬT CHÍNH XÁC CỦA BỘ ĐÔI PORT VÀ STARBOARD · 100.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:11.1 (11.1s) | L24 | Nếu bạn từng xem các bộ phim kinh dị bom tấn của Hollywood và đinh ninh rằng Cá Mập Trắng là hung thần vô địch thống trị biển cả, thì bạn đã bị truyền thông đánh lừa một cú ngoạn mục rồi! Đối với Bố Già Đại Dương, |  | Bức tranh châm biếm Hollywood: chúa tể cá mập trắng to lớn hung dữ nhưng vẻ mặt đang hoảng loạn tột độ tháo chạy với hàm răng nhọn hoắt đang nhìn thấy bóng lưng đen trắng của chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss |
| b02 | 00:11.1–00:14.6 (3.5s) | L25 | cá mập trắng khét tiếng chỉ là một món ăn vặt bổ dưỡng có lá gan béo ngậy. |  | Bàn tiệc Mafia sang trọng dưới đáy biển: chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) đeo khăn ăn kẻ sọc, tay cầm nĩa chỉ vào mô hình lá gan  |
| b03 | 00:14.6–00:26.1 (11.5s) | L26 | Năm 2022, tại vùng vịnh Gansbaai ở Nam Phi, giới khoa học chấn động khi phát hiện xác hàng loạt cá mập trắng dạt vào bờ với đúng một vết rách tinh vi dưới vây ngực! Thưa quý tòa, chứng cứ hiện trường cho thấy đây | **NĂM 2022** · vụ án Gansbaai · L/280 · [0.4, 0.5] | Hiện trường bờ biển vịnh Gansbaai Năm 2022: Dấu vết hiện trường được căng dây phong tỏa vàng đen, xác cá mập dạt vào bờ với duy nhất một vết rách phẫu thuật. |
| b04 | 00:26.1–00:35.9 (9.7s) | L27 | là vụ giải phẫu tinh vi! Quá chính xác thưa công tố viên! Hiện trường vụ án kỳ lạ tới mức khó tin: Toàn bộ phần thịt thăn thơm ngon của cá mập trắng hoàn toàn nguyên vẹn, |  | Kính lúp điều tra phóng to vết rạch dưới vây ngực: Một đường cắt sắc ngọt chính xác như dao mổ laser. |
| b05 | 00:35.9–00:47.6 (11.8s) | L28 | chỉ riêng lá gan nặng hàng trăm kilogram giàu lipid đã bị xé sạch không còn một mảnh vụn! Thủ phạm chính là bộ đôi sát thủ lừng danh mang tên Port và Starboard. Chúng nắm rõ điểm yếu sinh học chí mạng của loài cá mập: chỉ |  | Chân dung bộ đôi sát thủ Port và Starboard: Hai chú cá voi với chiếc vây lưng cong đặc trưng đang phối hợp kẹp chặt chúa tể cá mập trắng to lớn hung dữ nhưng vẻ mặt đang hoảng loạn tột độ tháo chạy. |
| b06 | 00:47.6–00:55.9 (8.2s) | L29 | cần tung cú húc lật ngửa con cá mập khiến nó rơi vào trạng thái bất động trương lực cơ bắp, cá mập sẽ tê liệt hoàn toàn và ngạt thở trong vài phút. Sau đó, | **BẤT ĐỘNG** · tê liệt trương lực · R/280 · [0.5, 0.55] | Cơ chế bất động trương lực học: chúa tể cá mập trắng to lớn hung dữ nhưng vẻ mặt đang hoảng loạn tột độ tháo chạy bị lật ngửa bụng lên trời, hai mắt đờ đẫn rơi vào trạng thái hôn mê ngạt thở hoàn toàn không thể phản kháng. |
| b07 | 00:55.9–01:04.6 (8.7s) | L30 | chúng rạch một đường chính xác đến từng milimét dưới vây ngực để rút trọn buồng gan béo bở rồi vứt bỏ toàn bộ phần xác còn lại! Đòn thanh trừng thị uy này khủng khiếp đến mức toàn |  | Vết cắt phẫu thuật hoàn hảo: Chiếc vây ngực cá mập được rạch chuẩn xác, buồng gan khổng lồ nặng hàng trăm kg được lấy ra nguyên vẹn. |
| b08 | 01:04.6–01:08.9 (4.3s) | L31 | bộ quần thể cá mập trắng tại vùng biển Nam Phi khiếp vía bỏ chạy, sơ tán khẩn cấp hàng trăm dặm |  | Bản đồ radar sơ tán đại dương: Hàng chục chú cá mập trắng gắn máy định vị bơi tháo chạy tán loạn ra khỏi vịnh Nam Phi. |
| b09 | 01:08.9–01:23.0 (14.1s) | L32 | và không dám bén mảng quay lại vùng biển suốt cả năm trời! Các nhà sinh học biển phải thốt lên rằng: Đây không phải là sự săn mồi ngẫu nhiên, mà là sự thống trị tuyệt đối về mặt tâm lý và kỹ năng tác chiến của Bố Già Đại Dương! Trước khi bộ đôi Port và Starboard xuất hiện, vịnh Gansbaai |  | Vịnh biển hoang vắng: Biển cảnh báo cấm cá mập trắng xuất hiện, trên mặt biển chỉ còn lại bộ đôi Port và Starboard bơi tuần tra. |
| b10 | 01:23.0–01:29.8 (6.8s) | L33 | từng là thủ phủ ngắm cá mập trắng nổi tiếng thế giới thu hút hàng triệu du khách. Nhưng kể từ khi hai sát thủ vây lưng cong ghé thăm, các thiết bị định |  | Lồng sắt ngắm cá mập của khách du lịch trống rỗng dưới nước, bên ngoài chỉ có chú rùa biển bơi qua nhún vai. |
| b11 | 01:29.8–01:33.8 (4.0s) | L34 | vị vệ tinh gắn trên mình cá mập trắng ghi nhận sự hoảng loạn tột độ. |  | Biểu đồ độ sâu: Cá mập trắng lặn trốn sâu dưới đáy vực thẳm 300 mét trong nỗi ám ảnh kinh hoàng. |
| b12 | 01:33.8–01:40.4 (6.6s) | L35 | Chúng lặn sâu xuống hàng trăm mét và tháo chạy tán loạn khắp đại dương, chứng minh ai mới thực sự là kẻ nắm giữ quyền lực sinh sát tối thượng! |  | Ngai vàng đáy biển: chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) uy nghiêm ngự trị trên mỏm đá ngầm, bên dưới là vùng biển sạch bóng cá mập t |

### scene04 · TIẾNG LÓNG ÂM THANH VÀ THỰC ĐƠN GIA TRUYỀN · 91.1s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:12.7 (12.7s) | L36 | Điều khiến các nhà sinh vật học hành vi kinh ngạc nhất về cá voi sát thủ chính là tính biệt lập văn hóa sâu sắc giữa các dòng tộc. Chúng phân hóa thành nhiều chủng loại sinh thái khác nhau và tuyệt đối không bao giờ giao lưu, bơi chung hay kết hôn bừa bãi. |  | Hai gia tộc cá voi đối mặt nhưng không hòa lẫn: Gia tộc ven bờ đội mũ đầu bếp cá hồi, gia tộc du cư khoác áo lông thú săn mồi oai vệ. |
| b02 | 00:12.7–00:26.5 (13.8s) | L37 | Giống như các gia tộc quyền quý thời xưa, mỗi chi nhánh đều giữ gìn danh dự và bản sắc ẩm thực riêng biệt của dòng họ mình! Báo cáo Bố Già, chi nhánh miền Bắc chỉ ăn cá hồi, không chịu ăn thịt thú! Rất đúng chất dòng tộc quý tộc! Chi nhánh cá voi cư trú ven |  | Thực đơn ẩm thực gia truyền: Bảng menu khắc gỗ hiển thị thực đơn cá hồi thượng hạng của dòng tộc ven bờ đối lập với thực đơn hải cẩu của dòng tộc du cư. |
| b03 | 00:26.5–00:33.3 (6.7s) | L38 | bờ chỉ trung thành với món cá hồi béo ngậy. Chúng nhìn chi nhánh du cư chuyên đi săn hải cẩu và cá voi con bằng nửa con mắt, xem đó |  | Bàn tiệc sashimi cá hồi tươi rói của chi nhánh ven bờ, các chú cá voi thưởng thức thanh lịch như quý tộc Anh quốc. |
| b04 | 00:33.3–00:42.2 (9.0s) | L39 | là những kẻ ăn thịt man rợ cục súc! Ngược lại, nhóm ngoài khơi xa chỉ đam mê lùng sục các loài cá mập đại dương. Chưa dừng lại ở đó, mỗi gia tộc sở hữu |  | Ánh mắt khinh khỉnh liếc nhìn sang bên: Gia tộc quý tộc cầm khăn lau miệng chê bai nhóm thợ săn thú biển ngoài khơi. |
| b05 | 00:42.2–00:47.8 (5.6s) | L40 | một hệ thống phương ngữ âm thanh độc nhất vô nhị. Giống như tiếng lóng của các băng đảng Mafia ở New York, |  | Sóng âm thanh phổ học: Tần số sóng âm tiếng lách cách và huýt sáo của chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) hiển thị thành các nốt nhạ |
| b06 | 00:47.8–00:57.7 (9.9s) | L41 | những âm thanh lách cách và tiếng huýt sáo của gia tộc này thì gia tộc hàng xóm hoàn toàn nghe như ngoại ngữ và không thể nào hiểu nổi! Những chú cá voi con mới sinh phải mất nhiều năm trời |  | Cảnh tượng hài hước: Chú cá voi gia tộc hàng xóm đeo tai nghe dịch thuật nhưng trên đầu hiện ra vô số dấu hỏi chấm vì không hiểu tiếng lóng. |
| b07 | 00:57.7–00:59.9 (2.2s) | L42 | theo mẹ học tập từng ngữ điệu âm thanh của dòng tộc, |  | Trường học ngôn ngữ gia đình: chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) kiên nhẫn phát âm từng tần số sóng siêu âm để dạy cho chú cá con đ |
| b08 | 00:59.9–01:13.2 (13.3s) | L43 | tiếp thu toàn bộ danh mục ẩm thực gia truyền và quy tắc ứng xử trước khi được giao phó trọng trách săn mồi. Đây chính là bằng chứng xác thực về sự tồn tại của văn hóa truyền miệng và truyền thống gia đình trong thế giới động vật hoang dã! Các nghiên cứu giải mã tần số âm |  | Cuốn sách bí kíp gia truyền: Bìa da khắc chữ vàng danh mục các món ăn truyền thống được trao cho chú cá con tốt nghiệp. |
| b09 | 01:13.2–01:21.4 (8.1s) | L44 | thanh kéo dài hơn 30 năm tại bờ biển Bắc Mỹ cho thấy: Ngay cả khi hai gia tộc bơi ngang qua nhau trong cùng một eo biển hẹp, chúng chỉ giữ khoảng cách lịch sự | **30 NĂM** · nghiên cứu âm học · L/280 · [0.45, 0.5] | Trạm nghiên cứu hải dương học Bắc Mỹ: Các nhà khoa học cắm micro thu âm dưới nước suốt 30 năm phân tích tiếng lóng cá voi. |
| b10 | 01:21.4–01:26.8 (5.4s) | L45 | và không bao giờ hòa lẫn tiếng gọi bầy. Mỗi gia tộc tự hào với phương ngữ riêng biệt của mình, tạo nên một bức |  | Hai luồng sóng âm khác màu lướt song song trong cùng một eo biển nhưng hoàn toàn tách biệt, không hề giao thoa nhiễu sóng. |
| b11 | 01:26.8–01:31.1 (4.3s) | L46 | tranh đa văn hóa vô cùng phong phú và độc bản dưới lòng đại dương sâu thẳm! |  | Bản đồ văn hóa các dòng tộc đại dương: Biểu đồ phân bố các vùng lãnh thổ và phương ngữ độc lập của các gia tộc Bố Già trên toàn cầu. |

### scene05 · TÌNH MẪU TỬ MƯỜI BẢY NGÀY LAY ĐỘNG ĐẠI DƯƠNG · 85.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.8 (7.8s) | L47 | Phía sau lớp vỏ bọc lạnh lùng của những tay săn mồi tàn bạo nhất đại dương, não bộ của cá voi sát thủ sở hữu một bí mật làm rúng động giới khoa học thần kinh. |  | Sơ đồ não bộ 5kg phát sáng: Hình ảnh đồ họa cấu tạo hệ thần kinh thùy paralimbic phân nhánh phức tạp hơn não bộ con người. |
| b02 | 00:07.8–00:18.7 (11.0s) | L48 | Khối não nặng tới 5kg của chúng có hệ thống thùy paralimbic phát triển vượt bậc, thậm chí còn phân nhánh phức tạp hơn cả cấu trúc tương ứng trong não bộ con người chúng ta! Đây chính là trung tâm chi phối các kết nối xã hội sâu sắc, | **5 KG** · trọng lượng não bộ · L/280 · [0.4, 0.5]<br>**CẢM XÚC** · thùy paralimbic · R/280 · [0.6, 0.48] | Cận cảnh ánh mắt sâu thẳm chan chứa tình cảm của chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses), toát lên vẻ trầm tư và lòng trắc ẩn của những  |
| b03 | 00:18.7–00:28.6 (9.8s) | L49 | sự thấu cảm, lòng vị tha và cả nỗi đau buồn mất mát khôn nguôi. 17 ngày ròng rã đẩy xác con... tình mẹ làm lay động cả đại dương! Đúng vậy thưa các bạn. |  | Bầu không khí u buồn dưới đáy đại dương: Trái tim phát sáng xanh ngọc bên trong lồng ngực cá voi đập nhịp đong đầy cảm xúc. |
| b04 | 00:28.6–00:37.9 (9.4s) | L50 | Vào Năm 2018, cả thế giới đã rơi nước mắt trước hình ảnh người mẹ cá voi mang tên Tahlequah. Khi đứa con sơ sinh không may qua đời chỉ sau nửa giờ chào đời, | **NĂM 2018** · hồ sơ Tahlequah · L/280 · [0.4, 0.5] | Bức tranh lay động triệu trái tim Năm 2018: người mẹ cá voi sát thủ Tahlequah ánh mắt chan chứa tình mẫu tử đang dùng trán nâng đứa con bé bỏng dùng trán nâng đứa con bé bỏng bơi giữa biển Thái Bình Dương mênh mông bão tuyết. |
| b05 | 00:37.9–00:40.4 (2.5s) | L51 | thay vì để xác con chìm xuống đáy biển lạnh giá, người |  | Tình mẫu tử bất diệt: Mỗi lần xác đứa con chìm dần, người mẹ lại kiên nhẫn lặn xuống dùng mũi nâng con lên mặt nước đón ánh bình minh. |
| b06 | 00:40.4–00:49.0 (8.6s) | L52 | mẹ đau thương ấy đã dùng trán nâng xác con, bơi ròng rã suốt 17 ngày qua quãng đường hơn 1.000 dặm trên biển Thái Bình Dương! Suốt 17 ngày đêm tang tóc đó, các thành viên trong gia tộc | **17 NGÀY** · hành trình tang tóc · L/280 · [0.35, 0.5]<br>**1.000 DẶM** · vượt biển Thái Bình · R/280 · [0.65, 0.5] | Hành trình 17 ngày và 1.000 dặm: Bản đồ hải trình di chuyển của người mẹ cá voi sát thủ Tahlequah ánh mắt chan chứa tình mẫu tử đang dùng trán nâng đứa con bé bỏng cùng sự hộ tống sát cánh của toàn bộ các thành viên trong bầy đàn. |
| b07 | 00:49.0–00:51.1 (2.2s) | L53 | đã lặng lẽ bơi bên cạnh hộ tống, thay phiên |  | Đội hình danh dự trong tang lễ biển cả: Đàn cá voi bơi xếp thành hai hàng danh dự trang nghiêm che chở cho người mẹ đau thương. |
| b08 | 00:51.1–01:01.4 (10.2s) | L54 | nhau nhường thức ăn và hỗ trợ người mẹ vượt qua nỗi đau tột cùng. Hình ảnh đó đã chứng minh cho toàn thể nhân loại thấy rằng: Bố Già Đại Dương không chỉ có sức mạnh cơ bắp và sự tàn bạo trên bàn tiệc săn mồi, mà |  | Sự đoàn kết gia đình: Các thành viên bơi song song mang thức ăn tiếp tế cho người mẹ đau thương, chia sẻ nỗi mất mát thiêng liêng. |
| b09 | 01:01.4–01:09.8 (8.4s) | L55 | sâu thẳm bên trong là một trái tim tràn ngập tình yêu thương mẫu tử và sự gắn kết gia đình thiêng liêng lay động lòng người! Đặc biệt hơn, cá voi sát thủ là một trong |  | Tượng đài tình mẫu tử: Hình ảnh hai mẹ con cá voi được khắc họa lung linh dưới làn ánh sáng huyền ảo rọi từ mặt biển. |
| b10 | 01:09.8–01:14.5 (4.8s) | L56 | số cực kỳ ít ỏi các loài sinh vật trên Trái Đất cùng với con người trải qua giai đoạn mãn kinh. |  | Biểu đồ tuổi thọ sinh học: Cá voi sát thủ và con người là hai loài hiếm hoi có tuổi thọ bà ngoại kéo dài hàng chục năm sau tuổi sinh sản. |
| b11 | 01:14.5–01:23.0 (8.4s) | L57 | Sau khi hết khả năng sinh sản ở 40 tuổi, các bà mẹ tiếp tục sống thêm tới 40 năm hay 50 năm nữa chỉ để làm nhiệm vụ bà ngoại, chăm sóc các cháu và hướng dẫn con cháu | **40 TUỔI** · cột mốc mãn kinh · L/280 · [0.4, 0.5]<br>**50 NĂM** · tuổi thọ bà ngoại · R/280 · [0.6, 0.5] | Thế hệ bà ngoại 50 năm kinh nghiệm: Bà cá voi già hiền từ dẫn dắt bầy cháu nhỏ vượt qua rạn san hô hiểm trở. |
| b12 | 01:23.0–01:25.2 (2.2s) | L58 | vượt qua những thời khắc bão tố hiểm nghèo! |  | Bà trùm lão luyện hướng dẫn đàn con cháu tìm thấy vùng nước ấm áp trù phú thức ăn giữa mùa đông băng giá. |

### scene06 · ĐIỀU RĂN CẤM TUYỆT ĐỐI KHÔNG CHẠM VÀO LOÀI NGƯỜI · 83.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:11.5 (11.5s) | L59 | Có một nghịch lý vĩ đại đã làm đau đầu các nhà sinh thái học suốt nhiều thế kỷ qua: Tại sao một loài động vật ăn thịt có thể xé xác cá voi xanh khổng lồ 40 tấn, giết cá mập trắng trong nháy mắt, nhưng trong toàn bộ lịch sử nhân | **40 TẤN** · hạ gục cá voi xanh · L/280 · [0.45, 0.5] | Cán cân so sánh sức mạnh: Một bên là hình ảnh chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) dễ dàng quật ngã cá voi xanh khổng lồ 40 tấn, bên  |
| b02 | 00:11.5–00:17.7 (6.2s) | L60 | loại chưa từng ghi nhận một vụ tấn công giết người nào ngoài tự nhiên hoang dã? Đúng vậy, bạn không hề nghe nhầm đâu! |  | Bản hiệp ước hòa bình cổ xưa: Cuộn giấy da cổ khắc điều khoản liên minh giữa Bố Già Đại Dương và loài người hai chân. |
| b03 | 00:17.7–00:28.0 (10.3s) | L61 | Hãy nhớ lấy điều luật số một của gia tộc: Cấm đụng vào loài người! Lời dặn dò nghiêm khắc của Bà Trùm lão làng chính là sự thật! Ngoại trừ những thảm kịch đáng tiếc xảy ra |  | Bà Trùm lão làng uy nghiêm giơ vây chỉ vào điều luật số 1: 'CẤM ĐỤNG VÀO LOÀI NGƯỜI' khắc bằng chữ vàng nổi trên phiến đá san hô. |
| b04 | 00:28.0–00:35.8 (7.8s) | L62 | tại các bể xiếc giam cầm do cá voi bị trầm cảm và căng thẳng tâm lý tột độ, thì ngoài đại dương tự do, cá voi sát thủ đối xử với con người vô cùng kỳ lạ. Chúng sẵn |  | Hình ảnh tương phản đối lập: Góc tối là bể xiếc bê tông tù túng u uất, góc sáng là đại dương bao la tự do ngập tràn ánh nắng. |
| b05 | 00:35.8–00:40.4 (4.6s) | L63 | sàng hợp tác cùng các ngư dân vịnh Eden ở nước Úc để lùa cá voi vào bờ chia phần, |  | Huyền thoại vịnh Eden nước Úc: Cá voi sát thủ Old Tom dẫn đầu bầy đàn quẫy đuôi báo hiệu cho thuyền ngư dân ra khơi hợp tác đánh bắt. |
| b06 | 00:40.4–00:48.3 (7.9s) | L64 | hoặc tò mò bơi sát mạn thuyền ngoi lên nhìn ngắm con người bằng ánh mắt ôn hòa và thân thiện! Dường như trong bộ luật bất thành văn của Bố Già Đại Dương, |  | Khung cảnh thanh bình: chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) ngoi đầu khỏi mặt nước trong xanh, mỉm cười hiền hòa vẫy vây chào người c |
| b07 | 00:48.3–00:56.8 (8.5s) | L65 | có một điều răn cấm tối cao đã được khắc sâu qua hàng triệu năm tiến hóa: Loài hai chân trên cạn là đối tác hòa bình, tuyệt đối không được coi là thức ăn! Sự tôn trọng kỳ lạ đó |  | Biểu tượng hòa bình vĩnh cửu: Bàn tay con người chạm nhẹ vào vây cá voi sát thủ giữa mặt biển hoàng hôn ấm áp. |
| b08 | 00:56.8–00:60.0 (3.2s) | L66 | chính là nét quý tộc vương giả của những kẻ cai trị biển cả. Còn bây giờ, |  | Tượng đài vinh danh Bố Già Đại Dương: chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) đội vương miện đứng giữa đại dương bao la, ngẩng cao đầu t |
| b09 | 00:60.0–01:09.2 (9.2s) | L67 | giữa chiến thuật sóng thần chém nứt tảng băng và ca phẫu thuật xé gan Cá Mập Trắng, bạn nể phục quyền lực nào nhất của Bố Già Đại Dương? Hãy để lại ý kiến bình luận bên dưới nhé! Và đừng quên bấm đăng ký |  | Hai chiến công hiển hách đặt cạnh nhau: Bên trái là đòn sóng thần đánh rách băng, bên phải là ca phẫu thuật xé gan cá mập. |
| b10 | 01:09.2–01:14.9 (5.7s) | L68 | kênh để đón xem Tập 36 khám phá cỗ máy giảm chấn sọ não 1.200 G của Chim Gõ Kiến nhé! Hãy cùng lan |  | Teaser Tập 36 hấp dẫn: Hình ảnh chú Chim Gõ Kiến ngầu lòi đeo kính bảo hộ cơ khí, cầm búa đập đầu vào thân cây gỗ tạo sóng xung kích. |
| b11 | 01:14.9–01:21.1 (6.1s) | L69 | tỏa thông điệp bảo vệ các đại dương và tôn trọng những gia tộc cá voi sát thủ kỳ diệu này, để tiếng huýt sáo của Bố Già Đại Dương mãi |  | Lá cờ bảo vệ đại dương xanh: chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) cùng đàn con cháu tung tăng bơi lượn trong làn nước trong vắt sạch  |
| b12 | 01:21.1–01:23.4 (2.3s) | L70 | mãi ngân vang tự do giữa biển khơi bao la! |  | Khung cảnh kết thúc hùng vĩ: Đàn cá voi sát thủ đồng loạt nhảy vọt lên khỏi mặt nước biển hoàng hôn rực rỡ, pháo hoa nổ chúc mừng. |

## 5. Phân cảnh Shorts — từng beat

Banner: **ĐẾ CHẾ MAFIA: / CÁ VOI SÁT THỦ!** · giọng 39.8s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Bạn có biết tại sao chúa tể săn mồi Cá Mập Trắng lại phải hoảng loạn bỏ chạy suốt cả năm trời chỉ vì đánh hơi thấy bóng dáng |  |
| s02 | 00:06.8 | S02 | của Cá Voi Sát Thủ không? |  |
| s03 | 00:08.8 | S03 | Tại vùng biển Nam Phi, |  |
| s04 | 00:10.6 | S04 | hai sát thủ mang tên Port và Starboard đã thực hiện những phi vụ trừng phạt chấn động giới sinh vật biển. |  |
| s05 | 00:16.8 | S05 | Chúng không thèm ăn thịt cá mập mà |  |
| s06 | 00:18.3 | S06 | dùng chiến thuật húc lật ngửa con mồi để kích |  |
| s07 | 00:20.5 | S07 | hoạt trạng thái tê liệt bất động, sau |  |
| s08 | 00:22.6 | S08 | đó rạch một đường chính xác đến từng milimét chỉ để |  |
| s09 | 00:25.4 | S09 | xé lấy buồng gan giàu chất béo rồi vứt bỏ toàn bộ phần xác còn lại! |  |
| s10 | 00:29.2 | S10 | Cuộc phẫu thuật tinh vi đến mức khiến toàn bộ đàn cá mập trắng trong bán kính hàng trăm dặm lập |  |
| s11 | 00:33.8 | S11 | tức sơ tán khẩn cấp không dám quay lại suốt cả năm trời. Đó chính |  |
| s12 | 00:37.6 | S12 | là uy quyền tuyệt đối của Bố Già Đại Dương! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chào mừng các bạn bước vào thế giới ngầm không ánh sáng của đại dương bao la, nơi trật tự không được thiết lập bằng may rủi mà bằng". Bố cục: Đại dương sâu thẳm mở ra với cánh cổng Mafia huyền bí: chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) đứng sừng sững ở vị trí trung tâm, hai tay đút túi áo vest, toát lên phong thái quyền lực tuyệt đối. KHÔNG có Cá Voi Sát Thủ trong cảnh này.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "quyền lực gia tộc tuyệt đối. Trong thế giới đó, bất kỳ sinh vật nào cũng phải cúi đầu nép mình trước kẻ mang hai màu đen trắng huyền thoại.". Bố cục: Cận cảnh ánh mắt sắc lạnh đeo kính râm của chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses), phản chiếu hình ảnh muôn loài sinh vật biển đang cúi mình kính cẩn trước Bố Già.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Người ta thường gọi chúng là Cá Voi Sát Thủ, nhưng trong từ điển sinh học, đây thực chất là loài cá heo lớn nhất hành tinh với chiều dài tới 9m và nặng hơn 6 tấn. Chúng". Bố cục: Sơ đồ giải phẫu kích thước khổng lồ: chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) bơi ngang thước đo 9m và cán cân 6 tấn, bên cạnh là một chú cá heo nhỏ bé để so sánh độ tương phản kích cỡ.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đứng đầu chuỗi thức ăn đại dương và hoàn toàn không có bất kỳ kẻ thù tự nhiên nào trên cõi đời này! Dạ thưa Bố Già, cho cháu xin vào gia tộc bảo kê được không ạ?". Bố cục: Kim tự tháp sinh thái đại dương: chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) ngự trị trên đỉnh cao nhất, bên dưới là cá mập, hải cẩu, cá voi tấm sừng hàm đều ở bậc thang dưới.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chú cá con ngây thơ này muốn xin một chân trong gia tộc ư? Gia tộc của chúng ta đâu phải cái chợ mà ai thích bơi vào thì bơi! Điều thú vị nhất của đế chế này nằm ở chỗ, nó hoàn toàn không do những gã đực to xác cơ bắp thống trị. Quyền lực tối cao thuộc về các". Bố cục: Khung cảnh hài hước: Chú cá con bé xíu run rẩy chắp tay xin việc trước bàn làm việc gỗ gụ khổng lồ của chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses).
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nữ Hoàng Bố Già sống thọ tới 80 năm hoặc 90 năm. Chế độ mẫu hệ Matriarchy này đã vận hành bền vững suốt hàng triệu năm qua. Những vị Bố Già Đại Dương lão làng này nắm giữ toàn bộ". Bố cục: Chân dung tráng lệ của Nữ Hoàng Bố Già Cá Voi Sát Thủ khổng lồ đeo chuỗi ngọc trai biển và vương miện cổ đại uy quyền: Thọ 90 năm, ánh mắt thông tuệ nắm giữ tấm bản đồ hải lưu bí truyền dẫn đường cho cả gia tộc vượt bão tố.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bản đồ hải lưu, kinh nghiệm săn mồi, đường đi nước bước và mật mã bí mật của dòng tộc truyền qua nhiều thế hệ. Đừng dại dột nghĩ rằng bạn có thể làm loạn trong lãnh địa của một gia tộc mà Nữ Hoàng đã". Bố cục: Bản đồ gia phả Mafia đại dương vẽ theo phong cách gia tộc cổ điển: Nữ Hoàng Bố Già Cá Voi Sát Thủ khổng lồ đeo chuỗi ngọc trai biển và vương miện cổ đại uy quyền uy nghi tọa lạc ở đỉnh cao nhất, xung quanh là các thế hệ con cháu quy phục.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "trị vì gần một thế kỷ! Các nhà khoa học thần kinh biển đã chứng minh: Trong mỗi bầy cá voi sát thủ, các Nữ Hoàng Bố Già đóng vai trò là". Bố cục: Bố Già lão làng đội vương miện ngọc trai biển ngồi trên ngai san hô, tay cầm quyền trượng san hô chỉ huy dòng hải lưu.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "kho tàng tri thức sống còn của cả dòng họ. Khi biển động, băng tan hay nguồn thức ăn khan hiếm, cả bầy hàng chục con lớn nhỏ đều nhất mực bơi theo sự dẫn dắt của bà trùm lão luyện. Khác với hầu hết các loài động vật đực thường rời đàn khi trưởng thành, những gã đực cá voi sát thủ dẫu có to lớn đến 9m vẫn". Bố cục: Cảnh tượng bão tố biển động dữ dội: Cả bầy hàng chục con cá voi sát thủ bơi rẽ sóng răm rắp theo sau đường bơi của Nữ Hoàng Bố Già Cá Voi Sát Thủ khổng lồ đeo chuỗi ngọc trai biển và vương miện cổ đại uy quyền.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "ngoan ngoãn bơi bên cạnh mẹ suốt cả cuộc đời! Sự kỷ luật thép và lòng trung thành gia tộc tuyệt đối chính là nền tảng biến loài săn mồi này thành những ông trùm bất khả chiến bại của toàn bộ đại dương! Hơn thế nữa,". Bố cục: Cảnh tượng hài hước ấm áp: Một gã cá voi đực to lớn lực lưỡng cao 9m nhưng bơi nép sát bên cạnh cá voi mẹ, ngoan ngoãn lắng nghe lời dạy bảo.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "vây lưng của những gã đực cao tới gần 2m sừng sững như một chiếc cột buồm đen tuyền xé toạc mặt nước biển. Tốc độ bơi tối đa của chúng có thể đạt tới 55 km/h, nhanh như một". Bố cục: Chiếc vây lưng hình tam giác khổng lồ cao 2m của chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) nhô thẳng đứng khỏi mặt nước biển rẽ sóng, bên cạnh là đồng hồ đo tốc độ 55 km/h rực lửa.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chiếc ca nô cao tốc thế giới tự nhiên! Kết hợp giữa sức mạnh thể chất áp đảo và bộ óc chiến lược siêu việt của Nữ Hoàng, không có bất kỳ mục tiêu nào trong đại dương có thể thoát khỏi tầm ngắm một khi gia tộc Bố Già đã quyết định ra tay!". Bố cục: Toàn cảnh gia tộc cá voi sát thủ bơi rẽ sóng đại dương, chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) dẫn đầu giương cao lá cờ gia huy mạ vàng quyền lực.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy quan sát một phi vụ đi săn điển hình tại vùng biển băng giá Nam Cực để thấy được đỉnh cao của sự phối hợp thế giới tự nhiên. Khi một chú hải cẩu đang nằm ung dung sưởi nắng trên tảng băng trôi kiên cố giữa đại dương, nó cứ ngỡ mình đã an toàn tuyệt đối trước mọi kẻ săn mồi. Nhưng đàn cá voi sát thủ". Bố cục: Cảnh tượng băng giá Nam Cực trắng xóa: chú hải cẩu béo tròn ngơ ngác đeo kính râm nằm tắm nắng trên tảng băng trôi đang nằm phơi bụng sưởi nắng trên một tảng băng trôi kiên cố, vẻ mặt lười biếng tận hưởng cuộc sống.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "không bao giờ lao vào húc bừa bãi như những kẻ thiếu học thức. Bố Già Đại Dương luôn hành động với sự". Bố cục: Dưới làn nước biển trong vắt: chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) cùng 3 thành viên gia tộc bơi dàn hàng ngang tàng hình như một phi đội máy bay tiêm kích, giữ cự ly thẳng tắp.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chuẩn xác lạnh lùng của những tay sát thủ nhà nghề! Ủa tôi nằm trên tảng băng to đùng thế này mà sao nước dâng tới cổ rồi?!". Bố cục: Góc nhìn từ trên cao xuống mặt biển xanh ngắt: 4 cái bóng đen khổng lồ lướt đi song song tuyệt đối dưới lớp băng mỏng.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nước dâng tới cổ là còn may đấy, lát nữa sẽ rơi thẳng vào miệng trùm sò! Các bạn hãy nhìn đội hình tác chiến của chúng: Bốn thành viên bơi dàn hàng ngang hoàn hảo như một phi đội tiêm kích tàng hình, giữ cự ly đều đặn từng centimet dưới mặt nước trong vắt. Khi". Bố cục: Sơ đồ khí động học sóng biển: 4 chiếc đuôi khổng lồ quạt mạnh đồng bộ dưới nước, đẩy lên một luồng áp suất cực đại hướng thẳng về phía tảng băng.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cách tảng băng khoảng 15m, Nữ Hoàng phát lệnh lặn xuống cùng lúc và dùng những chiếc đuôi khổng lồ quạt mạnh tạo nên một cơn sóng thần nhân tạo cực lớn!". Bố cục: Thước đo cự ly tác chiến: Điểm đánh dấu cách mép băng đúng 15m, nơi hiệu lệnh đồng bộ được phát ra.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cột sóng quét ngang làm nứt đôi tảng băng trôi kiên cố, hất tung chú hải cẩu rơi tõm xuống nước". Bố cục: Cơn sóng thần dâng cao đánh sập mép băng: Tảng băng nứt toác làm đôi, chú hải cẩu béo tròn ngơ ngác đeo kính râm nằm tắm nắng trên tảng băng trôi hoảng hốt trượt chân rơi thẳng xuống mặt nước sủi bọt trắng xóa.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "ngay trước hàm răng đang chờ sẵn! Nhưng điều đáng kinh ngạc hơn cả là sau khi con mồi rơi xuống biển,". Bố cục: Cận cảnh khoảnh khắc kịch tính: Hàm răng sắc nhọn hé mở dưới làn nước sủi bọt, chú hải cẩu hoảng hốt mở to mắt.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "không hề có bất kỳ sự tranh giành cắn xé hỗn loạn nào. Nữ Hoàng Bố Già cùng các thành viên phối hợp ghìm giữ con mồi, dạy cho những chú cá voi con cách thức ra đòn, rồi". Bố cục: Vòng tròn gia đình kỷ luật: chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) cùng các thành viên nhẹ nhàng vây quanh con mồi, chia sẻ thức ăn theo đúng tôn ti trật tự gia tộc.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chia sẻ miếng ăn sòng phẳng cho từng thành viên trong gia đình theo đúng tôn ti trật tự gia tộc. Đó là một bài học thế giới tự nhiên kinh điển về sức mạnh đồng đội và kỷ luật thép!". Bố cục: Lớp học săn mồi của Bố Già: chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) dùng mõm đẩy nhẹ chú hải cẩu lên mép băng để hướng dẫn 2 chú cá voi con tập bơi tạo sóng lần hai.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thậm chí các nhà làm phim tài liệu của đài BBC đã từng ghi lại cảnh tượng khó tin: Nếu con mồi rơi xuống nước nhưng chưa bị thương nặng,". Bố cục: Bảng tổng kết chiến thuật sóng thần Nam Cực: Sơ đồ tác chiến phối hợp 4 bước hoàn hảo của Bố Già Đại Dương.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "các sát thủ trưởng thành sẽ dùng mõm đẩy nhẹ con hải cẩu trở lại tảng băng để đàn con thực hành lại đợt tạo sóng lần thứ hai! Đây không đơn thuần là hành vi săn mồi để sinh tồn, mà là một trường học huấn luyện thế giới tự nhiên thực thụ được truyền lại từ đời này sang đời khác!". Bố cục: Hình ảnh thế hệ con cháu kế thừa: Hai chú cá voi con bơi theo sát vây lưng mẹ, thực hiện động tác quạt đuôi điêu luyện.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu bạn từng xem các bộ phim kinh dị bom tấn của Hollywood và đinh ninh rằng Cá Mập Trắng là hung thần vô địch thống trị biển cả, thì bạn đã bị truyền thông đánh lừa một cú ngoạn mục rồi! Đối với Bố Già Đại Dương,". Bố cục: Bức tranh châm biếm Hollywood: chúa tể cá mập trắng to lớn hung dữ nhưng vẻ mặt đang hoảng loạn tột độ tháo chạy với hàm răng nhọn hoắt đang nhìn thấy bóng lưng đen trắng của chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) liền toát mồ hôi hột run rẩy.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cá mập trắng khét tiếng chỉ là một món ăn vặt bổ dưỡng có lá gan béo ngậy.". Bố cục: Bàn tiệc Mafia sang trọng dưới đáy biển: chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) đeo khăn ăn kẻ sọc, tay cầm nĩa chỉ vào mô hình lá gan cá mập béo ngậy.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 2022, tại vùng vịnh Gansbaai ở Nam Phi, giới khoa học chấn động khi phát hiện xác hàng loạt cá mập trắng dạt vào bờ với đúng một vết rách tinh vi dưới vây ngực! Thưa quý tòa, chứng cứ hiện trường cho thấy đây là". Bố cục: Hiện trường bờ biển vịnh Gansbaai Năm 2022: Dấu vết hiện trường được căng dây phong tỏa vàng đen, xác cá mập dạt vào bờ với duy nhất một vết rách phẫu thuật.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "vụ giải phẫu tinh vi! Quá chính xác thưa công tố viên! Hiện trường vụ án kỳ lạ tới mức khó tin: Toàn bộ phần thịt thăn thơm ngon của cá mập trắng hoàn toàn nguyên vẹn,". Bố cục: Kính lúp điều tra phóng to vết rạch dưới vây ngực: Một đường cắt sắc ngọt chính xác như dao mổ laser.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chỉ riêng lá gan nặng hàng trăm kilogram giàu lipid đã bị xé sạch không còn một mảnh vụn! Thủ phạm chính là bộ đôi sát thủ lừng danh mang tên Port và Starboard. Chúng nắm rõ điểm yếu sinh học chí mạng của loài cá mập: chỉ cần". Bố cục: Chân dung bộ đôi sát thủ Port và Starboard: Hai chú cá voi với chiếc vây lưng cong đặc trưng đang phối hợp kẹp chặt chúa tể cá mập trắng to lớn hung dữ nhưng vẻ mặt đang hoảng loạn tột độ tháo chạy.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tung cú húc lật ngửa con cá mập khiến nó rơi vào trạng thái bất động trương lực cơ bắp, cá mập sẽ tê liệt hoàn toàn và ngạt thở trong vài phút. Sau đó, chúng". Bố cục: Cơ chế bất động trương lực học: chúa tể cá mập trắng to lớn hung dữ nhưng vẻ mặt đang hoảng loạn tột độ tháo chạy bị lật ngửa bụng lên trời, hai mắt đờ đẫn rơi vào trạng thái hôn mê ngạt thở hoàn toàn không thể phản kháng.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "rạch một đường chính xác đến từng milimét dưới vây ngực để rút trọn buồng gan béo bở rồi vứt bỏ toàn bộ phần xác còn lại! Đòn thanh trừng thị uy này khủng khiếp đến mức toàn bộ". Bố cục: Vết cắt phẫu thuật hoàn hảo: Chiếc vây ngực cá mập được rạch chuẩn xác, buồng gan khổng lồ nặng hàng trăm kg được lấy ra nguyên vẹn.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "quần thể cá mập trắng tại vùng biển Nam Phi khiếp vía bỏ chạy, sơ tán khẩn cấp hàng trăm dặm và". Bố cục: Bản đồ radar sơ tán đại dương: Hàng chục chú cá mập trắng gắn máy định vị bơi tháo chạy tán loạn ra khỏi vịnh Nam Phi.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "không dám bén mảng quay lại vùng biển suốt cả năm trời! Các nhà sinh học biển phải thốt lên rằng: Đây không phải là sự săn mồi ngẫu nhiên, mà là sự thống trị tuyệt đối về mặt tâm lý và kỹ năng tác chiến của Bố Già Đại Dương! Trước khi bộ đôi Port và Starboard xuất hiện, vịnh Gansbaai từng là". Bố cục: Vịnh biển hoang vắng: Biển cảnh báo cấm cá mập trắng xuất hiện, trên mặt biển chỉ còn lại bộ đôi Port và Starboard bơi tuần tra.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thủ phủ ngắm cá mập trắng nổi tiếng thế giới thu hút hàng triệu du khách. Nhưng kể từ khi hai sát thủ vây lưng cong ghé thăm, các thiết bị định vị". Bố cục: Lồng sắt ngắm cá mập của khách du lịch trống rỗng dưới nước, bên ngoài chỉ có chú rùa biển bơi qua nhún vai.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "vệ tinh gắn trên mình cá mập trắng ghi nhận sự hoảng loạn tột độ. Chúng". Bố cục: Biểu đồ độ sâu: Cá mập trắng lặn trốn sâu dưới đáy vực thẳm 300 mét trong nỗi ám ảnh kinh hoàng.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "lặn sâu xuống hàng trăm mét và tháo chạy tán loạn khắp đại dương, chứng minh ai mới thực sự là kẻ nắm giữ quyền lực sinh sát tối thượng!". Bố cục: Ngai vàng đáy biển: chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) uy nghiêm ngự trị trên mỏm đá ngầm, bên dưới là vùng biển sạch bóng cá mập trắng suốt cả năm trời.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Điều khiến các nhà sinh vật học hành vi kinh ngạc nhất về cá voi sát thủ chính là tính biệt lập văn hóa sâu sắc giữa các dòng tộc. Chúng phân hóa thành nhiều chủng loại sinh thái khác nhau và tuyệt đối không bao giờ giao lưu, bơi chung hay kết hôn bừa bãi.". Bố cục: Hai gia tộc cá voi đối mặt nhưng không hòa lẫn: Gia tộc ven bờ đội mũ đầu bếp cá hồi, gia tộc du cư khoác áo lông thú săn mồi oai vệ.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giống như các gia tộc quyền quý thời xưa, mỗi chi nhánh đều giữ gìn danh dự và bản sắc ẩm thực riêng biệt của dòng họ mình! Báo cáo Bố Già, chi nhánh miền Bắc chỉ ăn cá hồi, không chịu ăn thịt thú! Rất đúng chất dòng tộc quý tộc! Chi nhánh cá voi cư trú ven bờ chỉ". Bố cục: Thực đơn ẩm thực gia truyền: Bảng menu khắc gỗ hiển thị thực đơn cá hồi thượng hạng của dòng tộc ven bờ đối lập với thực đơn hải cẩu của dòng tộc du cư.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "trung thành với món cá hồi béo ngậy. Chúng nhìn chi nhánh du cư chuyên đi săn hải cẩu và cá voi con bằng nửa con mắt, xem đó là". Bố cục: Bàn tiệc sashimi cá hồi tươi rói của chi nhánh ven bờ, các chú cá voi thưởng thức thanh lịch như quý tộc Anh quốc.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "những kẻ ăn thịt man rợ cục súc! Ngược lại, nhóm ngoài khơi xa chỉ đam mê lùng sục các loài cá mập đại dương. Chưa dừng lại ở đó, mỗi gia tộc sở hữu một". Bố cục: Ánh mắt khinh khỉnh liếc nhìn sang bên: Gia tộc quý tộc cầm khăn lau miệng chê bai nhóm thợ săn thú biển ngoài khơi.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hệ thống phương ngữ âm thanh độc nhất vô nhị. Giống như tiếng lóng của các băng đảng Mafia ở New York,". Bố cục: Sóng âm thanh phổ học: Tần số sóng âm tiếng lách cách và huýt sáo của chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) hiển thị thành các nốt nhạc mật mã Mafia độc bản.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "những âm thanh lách cách và tiếng huýt sáo của gia tộc này thì gia tộc hàng xóm hoàn toàn nghe như ngoại ngữ và không thể nào hiểu nổi! Những chú cá voi con mới sinh phải mất nhiều năm trời theo mẹ". Bố cục: Cảnh tượng hài hước: Chú cá voi gia tộc hàng xóm đeo tai nghe dịch thuật nhưng trên đầu hiện ra vô số dấu hỏi chấm vì không hiểu tiếng lóng.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "học tập từng ngữ điệu âm thanh của dòng tộc,". Bố cục: Trường học ngôn ngữ gia đình: chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) kiên nhẫn phát âm từng tần số sóng siêu âm để dạy cho chú cá con đang chăm chú lắng nghe.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tiếp thu toàn bộ danh mục ẩm thực gia truyền và quy tắc ứng xử trước khi được giao phó trọng trách săn mồi. Đây chính là bằng chứng xác thực về sự tồn tại của văn hóa truyền miệng và truyền thống gia đình trong thế giới động vật hoang dã! Các nghiên cứu giải mã tần số âm thanh". Bố cục: Cuốn sách bí kíp gia truyền: Bìa da khắc chữ vàng danh mục các món ăn truyền thống được trao cho chú cá con tốt nghiệp.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "kéo dài hơn 30 năm tại bờ biển Bắc Mỹ cho thấy: Ngay cả khi hai gia tộc bơi ngang qua nhau trong cùng một eo biển hẹp, chúng chỉ giữ khoảng cách lịch sự và". Bố cục: Trạm nghiên cứu hải dương học Bắc Mỹ: Các nhà khoa học cắm micro thu âm dưới nước suốt 30 năm phân tích tiếng lóng cá voi.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "không bao giờ hòa lẫn tiếng gọi bầy. Mỗi gia tộc tự hào với phương ngữ riêng biệt của mình, tạo nên một bức tranh". Bố cục: Hai luồng sóng âm khác màu lướt song song trong cùng một eo biển nhưng hoàn toàn tách biệt, không hề giao thoa nhiễu sóng.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đa văn hóa vô cùng phong phú và độc bản dưới lòng đại dương sâu thẳm!". Bố cục: Bản đồ văn hóa các dòng tộc đại dương: Biểu đồ phân bố các vùng lãnh thổ và phương ngữ độc lập của các gia tộc Bố Già trên toàn cầu.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phía sau lớp vỏ bọc lạnh lùng của những tay săn mồi tàn bạo nhất đại dương, não bộ của cá voi sát thủ sở hữu một bí mật làm rúng động giới khoa học thần kinh.". Bố cục: Sơ đồ não bộ 5kg phát sáng: Hình ảnh đồ họa cấu tạo hệ thần kinh thùy paralimbic phân nhánh phức tạp hơn não bộ con người.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khối não nặng tới 5kg của chúng có hệ thống thùy paralimbic phát triển vượt bậc, thậm chí còn phân nhánh phức tạp hơn cả cấu trúc tương ứng trong não bộ con người chúng ta! Đây chính là trung tâm chi phối các kết nối xã hội sâu sắc,". Bố cục: Cận cảnh ánh mắt sâu thẳm chan chứa tình cảm của chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses), toát lên vẻ trầm tư và lòng trắc ẩn của những kẻ cai trị có tâm hồn.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "sự thấu cảm, lòng vị tha và cả nỗi đau buồn mất mát khôn nguôi. 17 ngày ròng rã đẩy xác con... tình mẹ làm lay động cả đại dương! Đúng vậy thưa các bạn. Vào". Bố cục: Bầu không khí u buồn dưới đáy đại dương: Trái tim phát sáng xanh ngọc bên trong lồng ngực cá voi đập nhịp đong đầy cảm xúc.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 2018, cả thế giới đã rơi nước mắt trước hình ảnh người mẹ cá voi mang tên Tahlequah. Khi đứa con sơ sinh không may qua đời chỉ sau nửa giờ chào đời,". Bố cục: Bức tranh lay động triệu trái tim Năm 2018: người mẹ cá voi sát thủ Tahlequah ánh mắt chan chứa tình mẫu tử đang dùng trán nâng đứa con bé bỏng dùng trán nâng đứa con bé bỏng bơi giữa biển Thái Bình Dương mênh mông bão tuyết.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thay vì để xác con chìm xuống đáy biển lạnh giá, người mẹ đau thương ấy đã dùng trán nâng xác con,". Bố cục: Tình mẫu tử bất diệt: Mỗi lần xác đứa con chìm dần, người mẹ lại kiên nhẫn lặn xuống dùng mũi nâng con lên mặt nước đón ánh bình minh.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bơi ròng rã suốt 17 ngày qua quãng đường hơn 1.000 dặm trên biển Thái Bình Dương! Suốt 17 ngày đêm tang tóc đó, các thành viên trong gia tộc đã". Bố cục: Hành trình 17 ngày và 1.000 dặm: Bản đồ hải trình di chuyển của người mẹ cá voi sát thủ Tahlequah ánh mắt chan chứa tình mẫu tử đang dùng trán nâng đứa con bé bỏng cùng sự hộ tống sát cánh của toàn bộ các thành viên trong bầy đàn.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "lặng lẽ bơi bên cạnh hộ tống, thay phiên nhau". Bố cục: Đội hình danh dự trong tang lễ biển cả: Đàn cá voi bơi xếp thành hai hàng danh dự trang nghiêm che chở cho người mẹ đau thương.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nhường thức ăn và hỗ trợ người mẹ vượt qua nỗi đau tột cùng. Hình ảnh đó đã chứng minh cho toàn thể nhân loại thấy rằng: Bố Già Đại Dương không chỉ có sức mạnh cơ bắp và sự tàn bạo trên bàn tiệc săn mồi, mà". Bố cục: Sự đoàn kết gia đình: Các thành viên bơi song song mang thức ăn tiếp tế cho người mẹ đau thương, chia sẻ nỗi mất mát thiêng liêng.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "sâu thẳm bên trong là một trái tim tràn ngập tình yêu thương mẫu tử và sự gắn kết gia đình thiêng liêng lay động lòng người! Đặc biệt hơn, cá voi sát thủ là một trong số". Bố cục: Tượng đài tình mẫu tử: Hình ảnh hai mẹ con cá voi được khắc họa lung linh dưới làn ánh sáng huyền ảo rọi từ mặt biển.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cực kỳ ít ỏi các loài sinh vật trên Trái Đất cùng với con người trải qua giai đoạn mãn kinh.". Bố cục: Biểu đồ tuổi thọ sinh học: Cá voi sát thủ và con người là hai loài hiếm hoi có tuổi thọ bà ngoại kéo dài hàng chục năm sau tuổi sinh sản.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sau khi hết khả năng sinh sản ở 40 tuổi, các bà mẹ tiếp tục sống thêm tới 40 năm hay 50 năm nữa chỉ để làm nhiệm vụ bà ngoại, chăm sóc các cháu và hướng dẫn con cháu". Bố cục: Thế hệ bà ngoại 50 năm kinh nghiệm: Bà cá voi già hiền từ dẫn dắt bầy cháu nhỏ vượt qua rạn san hô hiểm trở.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "vượt qua những thời khắc bão tố hiểm nghèo!". Bố cục: Bà trùm lão luyện hướng dẫn đàn con cháu tìm thấy vùng nước ấm áp trù phú thức ăn giữa mùa đông băng giá.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Có một nghịch lý vĩ đại đã làm đau đầu các nhà sinh thái học suốt nhiều thế kỷ qua: Tại sao một loài động vật ăn thịt có thể chinh phục cá voi xanh khổng lồ 40 tấn, giết cá mập trắng trong nháy mắt, nhưng trong toàn bộ lịch sử nhân loại". Bố cục: Cán cân so sánh sức mạnh: Một bên là hình ảnh chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) dễ dàng quật ngã cá voi xanh khổng lồ 40 tấn, bên kia là hình ảnh con người nhỏ bé trên thuyền buồm.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chưa từng ghi nhận một vụ tấn công giết người nào ngoài tự nhiên hoang dã? Đúng vậy, bạn không hề nghe nhầm đâu!". Bố cục: Bản hiệp ước hòa bình cổ xưa: Cuộn giấy da cổ khắc điều khoản liên minh giữa Bố Già Đại Dương và loài người hai chân.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy nhớ lấy điều luật số một của gia tộc: Cấm đụng vào loài người! Lời dặn dò nghiêm khắc của Bà Trùm lão làng chính là sự thật! Ngoại trừ những thảm kịch đáng tiếc xảy ra tại các". Bố cục: Bà Trùm lão làng uy nghiêm giơ vây chỉ vào điều luật số 1: 'CẤM ĐỤNG VÀO LOÀI NGƯỜI' khắc bằng chữ vàng nổi trên phiến đá san hô.
```
</details>

<details><summary>L62</summary>

```text
HÌNH L62 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bể xiếc giam cầm do cá voi bị trầm cảm và căng thẳng tâm lý tột độ, thì ngoài đại dương tự do, cá voi sát thủ đối xử với con người vô cùng kỳ lạ. Chúng sẵn sàng". Bố cục: Hình ảnh tương phản đối lập: Góc tối là bể xiếc bê tông tù túng u uất, góc sáng là đại dương bao la tự do ngập tràn ánh nắng.
```
</details>

<details><summary>L63</summary>

```text
HÌNH L63 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hợp tác cùng các ngư dân vịnh Eden ở nước Úc để lùa cá voi vào bờ chia phần, hoặc". Bố cục: Huyền thoại vịnh Eden nước Úc: Cá voi sát thủ Old Tom dẫn đầu bầy đàn quẫy đuôi báo hiệu cho thuyền ngư dân ra khơi hợp tác đánh bắt.
```
</details>

<details><summary>L64</summary>

```text
HÌNH L64 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tò mò bơi sát mạn thuyền ngoi lên nhìn ngắm con người bằng ánh mắt ôn hòa và thân thiện! Dường như trong bộ luật bất thành văn của Bố Già Đại Dương, có một". Bố cục: Khung cảnh thanh bình: chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) ngoi đầu khỏi mặt nước trong xanh, mỉm cười hiền hòa vẫy vây chào người chèo thuyền kayak.
```
</details>

<details><summary>L65</summary>

```text
HÌNH L65 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "điều răn cấm tối cao đã được khắc sâu qua hàng triệu năm tiến hóa: Loài hai chân trên cạn là đối tác hòa bình, tuyệt đối không được coi là thức ăn! Sự tôn trọng kỳ lạ đó chính là". Bố cục: Biểu tượng hòa bình vĩnh cửu: Bàn tay con người chạm nhẹ vào vây cá voi sát thủ giữa mặt biển hoàng hôn ấm áp.
```
</details>

<details><summary>L66</summary>

```text
HÌNH L66 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nét quý tộc vương giả của những kẻ cai trị biển cả. Còn bây giờ, giữa". Bố cục: Tượng đài vinh danh Bố Già Đại Dương: chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) đội vương miện đứng giữa đại dương bao la, ngẩng cao đầu tự hào về nền văn minh biển cả.
```
</details>

<details><summary>L67</summary>

```text
HÌNH L67 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chiến thuật sóng thần chém nứt tảng băng và ca phẫu thuật xé gan Cá Mập Trắng, bạn nể phục quyền lực nào nhất của Bố Già Đại Dương? Hãy để lại ý kiến bình luận bên dưới nhé! Và đừng quên bấm đăng ký kênh để". Bố cục: Hai chiến công hiển hách đặt cạnh nhau: Bên trái là đòn sóng thần đánh rách băng, bên phải là ca phẫu thuật xé gan cá mập.
```
</details>

<details><summary>L68</summary>

```text
HÌNH L68 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đón xem Tập 36 khám phá cỗ máy giảm chấn sọ não 1.200 G của Chim Gõ Kiến nhé! Hãy cùng lan tỏa". Bố cục: Teaser Tập 36 hấp dẫn: Hình ảnh chú Chim Gõ Kiến ngầu lòi đeo kính bảo hộ cơ khí, cầm búa đập đầu vào thân cây gỗ tạo sóng xung kích.
```
</details>

<details><summary>L69</summary>

```text
HÌNH L69 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thông điệp bảo vệ các đại dương và tôn trọng những gia tộc cá voi sát thủ kỳ diệu này, để tiếng huýt sáo của Bố Già Đại Dương mãi mãi". Bố cục: Lá cờ bảo vệ đại dương xanh: chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses) cùng đàn con cháu tung tăng bơi lượn trong làn nước trong vắt sạch rác thải nhựa.
```
</details>

<details><summary>L70</summary>

```text
HÌNH L70 (16:9 ngang, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "ngân vang tự do giữa biển khơi bao la!". Bố cục: Khung cảnh kết thúc hùng vĩ: Đàn cá voi sát thủ đồng loạt nhảy vọt lên khỏi mặt nước biển hoàng hôn rực rỡ, pháo hoa nổ chúc mừng.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bạn có biết tại sao chúa tể săn mồi Cá Mập Trắng lại phải hoảng loạn bỏ chạy suốt cả năm trời chỉ vì đánh hơi thấy bóng dáng của". Bố cục: Chúa tể cá mập trắng kinh hoàng tháo chạy: chúa tể cá mập trắng to lớn hung dữ nhưng vẻ mặt đang hoảng loạn tột độ tháo chạy toát mồ hôi hột bỏ chạy tán loạn khi nhìn thấy bóng đen khổng lồ dưới biển.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Cá Voi Sát Thủ không?". Bố cục: Bóng đen bí ẩn lộ diện: chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng lướt qua ống kính máy quay với ánh mắt lạnh lùng của một Bố Già thế giới ngầm.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Tại vùng biển Nam Phi,". Bố cục: Bản đồ vịnh biển Nam Phi dậy sóng: Sóng biển cuộn xoáy phong cách cổ điển, đánh dấu vùng lãnh địa của Bố Già.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "hai sát thủ mang tên Port và Starboard đã thực hiện những phi vụ trừng phạt chấn động giới sinh vật biển. Chúng". Bố cục: Bộ đôi sát thủ khét tiếng: Port và Starboard với chiếc vây cong đặc trưng bơi ép sát hai bên sườn chúa tể cá mập trắng to lớn hung dữ nhưng vẻ mặt đang hoảng loạn tột độ tháo chạy.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "không thèm ăn thịt cá mập mà dùng". Bố cục: Bàn tiệc Mafia sang trọng kén chọn: chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng lắc đầu chê bai phần thịt thăn thông thường của cá mập.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "chiến thuật húc lật ngửa con mồi để kích hoạt". Bố cục: Cú húc lật ngửa tử thần: chúa tể cá mập trắng to lớn hung dữ nhưng vẻ mặt đang hoảng loạn tột độ tháo chạy bị lật úp bụng lên trên, mắt đờ đẫn rơi vào trạng thái tê liệt trương lực không thể cử động.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "trạng thái tê liệt bất động, sau đó". Bố cục: Cơ chế sinh học bất động trương lực: chúa tể cá mập trắng to lớn hung dữ nhưng vẻ mặt đang hoảng loạn tột độ tháo chạy cứng đờ bất động, ngạt thở hoàn toàn dưới nước.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "rạch một đường chính xác đến từng milimét chỉ để xé lấy". Bố cục: Đường phẫu thuật siêu việt: Vết rạch chuẩn xác dưới vây ngực lấy ra buồng gan béo ngậy giàu chất béo.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "buồng gan giàu chất béo rồi vứt bỏ toàn bộ phần xác còn lại!". Bố cục: Chiến lợi phẩm thượng hạng: Buồng gan béo ngậy phát sáng vàng óng ánh trên tay Bố Già đại dương.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Cuộc phẫu thuật tinh vi đến mức khiến toàn bộ đàn cá mập trắng trong bán kính hàng trăm dặm lập tức". Bố cục: Thực đơn kén chọn của Bố Già: chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng thong thả thưởng thức buồng gan ngon lành, hoàn toàn bỏ qua phần thịt còn lại.
```
</details>

<details><summary>S11</summary>

```text
HÌNH S11 (DỌC 9:16, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "sơ tán khẩn cấp không dám quay lại suốt cả năm trời. Đó chính là". Bố cục: Cuộc sơ tán hàng loạt: Hàng trăm chú cá mập trắng hoảng sợ tháo chạy tán loạn khỏi vùng biển Nam Phi suốt một năm.
```
</details>

<details><summary>S12</summary>

```text
HÌNH S12 (DỌC 9:16, phong cách tranh khắc gỗ hàng hải Baroque & huy hiệu Mafia biển sâu (Oceanic Syndicate Woodcut) và nhân vật chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "uy quyền tuyệt đối của Bố Già Đại Dương!". Bố cục: Vương quyền biển cả: chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng ngự trị trên ngai vàng san hô đáy biển, khẳng định vị thế chúa tể bất khả xâm phạm.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/70 của video YouTube về Cá Voi Sát Thủ). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh khắc gỗ hàng hải Baroque cổ điển kết hợp huy hiệu Mafia biển sâu (Oceanic Syndicate & Nautical Baroque Woodcut): nét cọ mực tàu dày dặn sắc lạnh như tranh khắc kim loại thế kỷ 18, những ngọn sóng đại dương cuộn xoáy hoa văn baroque cổ điển, điểm nhấn huy hiệu mạ vàng vương giả và dấu ấn sáp đỏ quyền lực, tông màu xanh biển thẳm kết hợp đen tuyền uy quyền; NỀN TRẮNG TINH hoàn toàn, không watermark, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses). Nhân vật phụ cố định: Nữ Hoàng Bố Già Cá Voi Sát Thủ khổng lồ đeo chuỗi ngọc trai biển và vương miện cổ đại uy quyền; chú hải cẩu béo tròn ngơ ngác đeo kính râm nằm tắm nắng trên tảng băng trôi; chúa tể cá mập trắng to lớn hung dữ nhưng vẻ mặt đang hoảng loạn tột độ tháo chạy; người mẹ cá voi sát thủ Tahlequah ánh mắt chan chứa tình mẫu tử đang dùng trán nâng đứa con bé bỏng. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/12 của video YouTube Shorts về Cá Voi Sát Thủ). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh khắc gỗ hàng hải Baroque cổ điển kết hợp huy hiệu Mafia biển sâu (Oceanic Syndicate & Nautical Baroque Woodcut): nét cọ mực tàu dày dặn sắc lạnh như tranh khắc kim loại thế kỷ 18, những ngọn sóng đại dương cuộn xoáy hoa văn baroque cổ điển, điểm nhấn huy hiệu mạ vàng vương giả và dấu ấn sáp đỏ quyền lực, tông màu xanh biển thẳm kết hợp đen tuyền uy quyền; NỀN TRẮNG TINH hoàn toàn, không watermark, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses). Nhân vật phụ: chúa tể cá mập trắng to lớn hung dữ nhưng vẻ mặt đang hoảng loạn tột độ tháo chạy. 
```
</details>

## 7. SEO

- **title:** Bố Già Đại Dương: Chiến Thuật Sóng Thần & Bí Mật Khiến Cá Mập Trắng Tháo Chạy?! | Tập 35
- **hook_paragraph:** Cá Voi Sát Thủ (Orcinus orca) không chỉ là loài cá heo lớn nhất thế giới nặng hơn sáu tấn, mà còn là đế chế Mafia tối thượng của đại dương. Chúng sở hữu những gia tộc mẫu hệ cai trị gần một thế kỷ, chiến thuật tạo sóng thần đồng bộ hạ gục hải cẩu trên băng, và ca phẫu thuật xé gan khiến chúa tể Cá Mập Trắng phải hoảng loạn bỏ chạy suốt cả năm trời!
- **question:** Giữa chiến thuật tạo sóng thần chém nứt tảng băng và ca phẫu thuật xé gan Cá Mập Trắng, bạn nể phục quyền lực nào nhất của Bố Già Đại Dương?
- **next_teaser:** kỹ sư cơ khí của rừng xanh sở hữu hộp sọ chịu lực một ngàn hai trăm G nhờ chiếc lưỡi kỳ dị
- **shorts_title:** Bí Mật Khiến Cá Mập Trắng Tháo Chạy Khỏi Bố Già Đại Dương?!
- **shorts_desc:** Cá Voi Sát Thủ không thèm ăn thịt cá mập mà lật ngửa con mồi để kích hoạt trạng thái tê liệt, chỉ xé lấy buồng gan béo ngậy rồi bỏ xác!
- **bullets:** Đế chế mẫu hệ Matriarchy: Nữ Hoàng Bố Già thọ chín mươi năm nắm giữ toàn bộ bản đồ hải lưu và bí kíp gia tộc · Chiến thuật sóng thần bầy đàn: Bơi dàn hàng ngang quạt đuôi tạo sóng chém nứt đôi tảng băng Nam Cực · Ca phẫu thuật lấy gan kinh điển: Cú húc lật ngửa gây tê liệt trương lực khiến Cá Mập Trắng Nam Phi khiếp sợ · Phương ngữ âm thanh độc nhất: Mỗi gia tộc có tiếng lóng riêng biệt và thực đơn gia truyền không ai giống ai · Trái tim và thùy paralimbic vĩ đại: Nỗi đau mất con kéo dài mười bảy ngày và một ngàn dặm của người mẹ Tahlequah · Điều răn cấm tối cao: Bản hiệp ước hòa bình không bao giờ săn giết con người ngoài tự nhiên hoang dã
- **tags:** cá voi sát thủ, orca, bố già đại dương, cá mập trắng, hải cẩu, khoa học kỳ thú, vẽ chuyện hoang dã, whiteboard animation

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-35-ca-voi-sat-thu
python src/episode/pipeline.py tts    projects/tap-35-ca-voi-sat-thu     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-35-ca-voi-sat-thu     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-35-ca-voi-sat-thu     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-35-ca-voi-sat-thu              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-35-ca-voi-sat-thu --force
python scripts/beat_sheet.py projects/tap-35-ca-voi-sat-thu               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-35-ca-voi-sat-thu/audio/shorts.wav projects/tap-35-ca-voi-sat-thu/renders/tap-35-ca-voi-sat-thu_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-35-ca-voi-sat-thu
python src/episode/pipeline.py seo    projects/tap-35-ca-voi-sat-thu
python src/episode/episode_doc.py     projects/tap-35-ca-voi-sat-thu
```

# TẬP 11 — GẤU TRÚC LỚN · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-11-gau-truc-lon`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-11-gau-truc-lon`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F4` · **Persona giọng:** `phong_vien_24h` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Gấu Trúc Lớn |
| Tiêu đề YouTube | Ruột Ăn Thịt Nhưng Ngồi Nhai Tre 14 Tiếng/Ngày?! \| Gấu Trúc Lớn \| Tập 11 |
| Video dài | `renders/tap-11-gau-truc-lon_long.mp4` — 8:51.5 (531.5s) |
| Shorts | `renders/tap-11-gau-truc-lon_shorts.mp4` — 0:47.5 (47.5s) |
| Thumbnail | `renders/tap-11-gau-truc-lon_thumbnail.jpg` |
| Số hình | dài 66 beat / 66 ảnh riêng; Shorts 11 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/66 của video YouTube về Gấu Trúc Lớn). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay. Nhân vật phụ cố định: anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H, đeo ba lô tác nghiệp; cô phát thanh viên tin tức hoạt hình xinh đẹp ngồi sau bàn trường quay tin tức thời sự; ông cụ nhân chứng râu tóc bạc phơ chống gậy trúc. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — 00 SÁNG: BẮT ĐẦU CA NHAI TRE CẬT LỰC CỦA KẺ PHẢN BỘI TỔ TIÊN
*Thẻ chương:* BẮT ĐẦU CA NHAI TRE CỦA KẺ PHẢN BỘI TỔ TIÊN

*Badge:* `06:00 SÁNG` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene01_p0.wav` (555 ký tự) · mood `hao_hung`

```text
Bây giờ là không sáu giờ sáng! Kính thưa quý vị khán giả, chúng tôi đang có mặt trực tiếp tại khu rừng tre mù sương tỉnh Tứ Xuyên để tường thuật lại một ngày làm việc cật lực của sinh vật lười biếng bậc nhất hành tinh: Gấu Trúc Lớn! Chiếc đồng hồ sinh học vừa điểm hồi chuông báo thức, và nhân vật chính của chúng ta — Chiến thần ăn chay — đã lập tức ngồi bật dậy vào vị trí làm việc quen thuộc. Không tập thể dục, không đánh răng, công việc đầu tiên và duy nhất trong ngày của gã béo này là... bốc một thanh tre cho thẳng vào mồm nhai rôm rốp! [laughter]
```
**Part 1** → `audio/vs/scene01_p1.wav` (87 ký tự) · 🎭 cameo `phat_thanh_vien`

```text
Alo trường quay nghe rõ không? Phóng viên cho hỏi gã này định nhai tre đến bao giờ thế?
```
**Part 2** → `audio/vs/scene01_p2.wav` (675 ký tự) · mood `don_dap`

```text
[surprise-oh] Báo cáo trường quay, gã này sẽ ngồi nhai liên tục từ mười đến mười bốn tiếng mỗi ngày, không ngừng nghỉ! Điều nghịch lý đến phát điên là: xét về mặt sinh học và phả hệ tiến hóa mười chín triệu năm, Gấu Trúc thuộc bộ thú ăn thịt chính hiệu, cùng một tổ tiên với gấu xám, sư tử và chó sói! Hộp sọ của nó có cơ hàm cực khỏe, răng nanh sắc nhọn và đường ruột ngắn cũn cỡn chuyên dùng để tiêu hóa thịt tươi béo ngậy. Nhưng không hiểu vì một pha bẻ lái lịch sử nào của tạo hóa, khoảng hai triệu năm trước, tổ tiên của nó bỗng nhiên... mất đi cảm nhận vị umami của thịt, chán ăn thịt chuyển hẳn sang ăn chay chín mươi chín phần trăm bằng lá tre và thân tre! [laughter]
```
**Part 3** → `audio/vs/scene01_p3.wav` (471 ký tự) · mood `hao_hung`

```text
Các nhà khoa học phát hiện đột biến trên gen Tát-một-rờ-một đã biến chiếc lưỡi sành ăn thịt của tổ tiên nó thành kẻ mù vị giác với món bít-tết! Đối với Chiến thần ăn chay, một tảng thịt bò thơm phức béo ngậy bây giờ cũng nhạt toẹt và vô vị y hệt một miếng bìa các-tông ngâm nước! Thà rằng ngồi gặm cành tre tươi đẫm sương sớm còn cảm thấy thanh tao và hợp khẩu vị hơn gấp vạn lần! Hãy cùng chúng tôi đếm ngược từng mốc giờ để xem cỗ máy ăn chay này vận hành kỳ dị ra sao!
```

### scene02 — 00 TRƯA: GIẢI MÃ NGÓN TAY CÁI THỨ SÁU VÀ HÀM NGHIỀN XƯƠNG
*Thẻ chương:* XƯƠNG CỔ TAY BIẾN DỊ THÀNH NGÓN TAY CÁI BÓC VỎ TRE

*Badge:* `10:00 TRƯA` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene02_p0.wav` (588 ký tự) · mood `don_dap`

```text
Đồng hồ điểm mười giờ trưa! Cập nhật mới nhất từ hiện trường: sau bốn tiếng nhai tre không ngừng nghỉ, Chiến thần ăn chay đã xử lý gọn gàng hơn mười cân cành tre cứng như gỗ lim! Quý vị có bao giờ thắc mắc tại sao một con gấu to béo vụng về lại có thể cầm nắm từng nhánh tre thanh thoát, bóc lớp vỏ cứng một cách điệu nghệ chẳng khác nào một đầu bếp chuyên nghiệp bóc vỏ mía không? [question-ah] Camera góc siêu cận của chúng tôi vừa ghi lại một bí mật giải phẫu kinh ngạc: bàn tay trước của Gấu Trúc không phải có năm ngón như các loài gấu khác, mà sở hữu tới sáu ngón tay! [surprise-wa]
```
**Part 1** → `audio/vs/scene02_p1.wav` (98 ký tự) · 🎭 cameo `ong_gia_ke`

```text
Này phóng viên ơi, làm gì có loài thú nào mọc sáu ngón tay thật, chắc chắn là đạo cụ gắn thêm rồi!
```
**Part 2** → `audio/vs/scene02_p2.wav` (423 ký tự) · mood `hao_hung`

```text
Bác nhân chứng nói gần đúng rồi đấy! Trên thực tế, ngón tay cái phụ này không phải là một ngón tay thật, mà là xương vừng cổ tay phình to dị thường, bọc một lớp đệm thịt dày cộp bên ngoài. Tiến hóa đã biến chiếc xương cổ tay này thành một ngón tay cái giả hoạt động linh hoạt đối diện với năm ngón còn lại, giúp nó kẹp chặt từng thân tre tròn lẳn và tước bỏ lớp vỏ đắng ngắt một cách chuẩn xác từng mi-li-mét! [surprise-oh]
```
**Part 3** → `audio/vs/scene02_p3.wav` (614 ký tự) · mood `don_dap`

```text
Chưa dừng lại ở bàn tay khéo léo, hãy nhìn vào khuôn mặt tròn xoe phúng phính đáng yêu như chiếc bánh bao của nó! Quý vị đừng để vẻ dễ thương đánh lừa: hai bên má phúng phính thực chất là hai khối cơ cắn khổng lồ neo thẳng lên gờ đỉnh sọ! Lực cắn của Chiến thần ăn chay mạnh tới mức chỉ đứng sau loài linh cẩu đốm nghiền xương, đủ sức bẻ vụn thân tre già dày cộp như nhai bim bim! Toàn bộ niêm mạc vòm họng và thực quản của nó còn được lót một lớp màng nhầy siêu dày để các dằm tre sắc nhọn không thể đâm thủng nội tạng khi nuốt! Vũ khí của mãnh thú săn mồi thượng thừa, nhưng dùng vào việc nhai cỏ cây! [laughter]
```

### scene03 — 00 CHIỀU: CỖ MÁY TIÊU HÓA CHỈ HẤP THỤ 17% VÀ THẢI 25KG PHÂN
*Thẻ chương:* TIÊU HÓA SIÊU KÉM CHỈ HẤP THỤ 17% DINH DƯỠNG

*Badge:* `14:00 CHIỀU` · *mood mặc định:* `nghiem_trang_gia`

**Part 0** → `audio/vs/scene03_p0.wav` (606 ký tự) · mood `nghiem_trang_gia`

```text
Bây giờ là mười bốn giờ chiều! Chúng tôi vừa phải lùi xa hiện trường mười bước vì một kỷ lục sinh học vô tiền khoáng hậu sắp diễn ra. Quý vị hãy giữ chặt mũ: mỗi ngày, một chú Gấu Trúc trưởng thành phải nạp từ mười hai cân đến ba mươi tám cân tre tươi. Nhưng vì mang ruột thú ăn thịt ngắn ngủn, không có bốn ngăn dạ dày như trâu bò, cũng chẳng có vi khuẩn lên men phân giải chất xơ như loài ngựa, hệ tiêu hóa của nó chỉ hấp thụ vỏn vẹn đúng mười bảy phần trăm chất dinh dưỡng! Tới tám mươi ba phần trăm lượng tre nuốt vào bụng sẽ trôi tuột ra ngoài nguyên vẹn hình sợi chỉ sau hai tiếng đồng hồ! [laughter]
```
**Part 1** → `audio/vs/scene03_p1.wav` (609 ký tự) · mood `don_dap`

```text
Và hệ quả tất yếu là gì? Xin thông báo một con số kỷ lục: Chiến thần ăn chay phải đi vệ sinh tới bốn mươi lần mỗi ngày! [surprise-ah] Đúng vậy, quý vị không hề nghe nhầm đâu, bốn mươi lần một ngày, thải ra từ hai mươi cân đến hai mươi lăm cân phân tre tươi! Vừa ngồi nhai cành tre đằng trước, đằng sau đã xả ra đống bã tre thơm mùi cỏ non. Các nhà sinh vật học khi vào rừng chỉ cần đếm số lượng bãi thải là biết ngay gã béo này đã ngồi ở gốc cây đó bao nhiêu phút. Đây chính xác là một cỗ máy nghiền tre di động: năng suất nghiền cực cao, tiêu hóa cực kém, và xả thải liên tục hai mươi tư trên bảy! [laughter]
```
**Part 2** → `audio/vs/scene03_p2.wav` (561 ký tự) · mood `hao_hung`

```text
Điều bi hài nhất là phân của nó sạch đến mức người ta không thể nhịn cười! Vì chín mươi chín phần trăm thức ăn là tre trúc và thời gian lưu trong ruột quá ngắn, phân gấu trúc hầu như không có mùi hôi thối mà thơm dịu mùi lá tre lên men thoang thoảng như trà xanh! Tại Tứ Xuyên, người ta đã tận dụng loại phân giàu chất xơ này để tẩy sạch làm giấy thủ công mỹ nghệ cao cấp, thậm chí dùng bã phân ủ trà xanh bán với giá hàng ngàn đô-la một cân! Ai mà ngờ chất thải của kẻ ăn chay lười biếng lại biến thành mỏ vàng sinh thái độc lạ bậc nhất thế giới! [surprise-wa]
```

### scene04 — 00 HOÀNG HÔN: NHỮNG PHA NGÃ CÂY KINH ĐIỂN VÀ NGỦ BẤT CHẤP TƯ THẾ
*Thẻ chương:* NGỦ BẤT CHẤP TƯ THẾ VÀ LĂN LỘN TỰ NHIÊN

*Badge:* `18:00 HOÀNG HÔN` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene04_p0.wav` (579 ký tự) · mood `tram_bi_an`

```text
Ánh hoàng hôn buông xuống rừng tre, đồng hồ điểm mười tám giờ tối! Sau một ca làm việc cật lực ăn uống và xả thải, Chiến thần ăn chay quyết định leo lên ngọn cây cao để nghỉ ngơi thư giãn. Và đây chính là khoảnh khắc chương trình biểu diễn xiếc hài hước nhất tự nhiên bắt đầu! [laughter] Quý vị hãy nhìn lên chạc cây: thân hình tròn xoe nặng hơn một tạ của nó đang vắt vẻo trên một cành cây nhỏ chỉ to bằng cổ tay. Nó ngủ trong những tư thế không tưởng: đầu chúc xuống đất, bốn chân buông thõng đung đưa, hoặc nằm ngửa bụng phơi nắng như một bao tải gạo bị bỏ quên trên ngọn cây!
```
**Part 1** → `audio/vs/scene04_p1.wav` (59 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Ối ối bác phóng viên ơi, cành cây gãy rồi kìa, đỡ cháu với!
```
**Part 2** → `audio/vs/scene04_p2.wav` (539 ký tự) · mood `hao_hung`

```text
Rắc! Bịch! Một pha tiếp đất đỉnh cao không thể đỡ nổi! [laughter] Cành cây gãy đôi và Chiến thần ăn chay rơi tự do từ độ cao vài mét đập mông xuống đất. Nhưng quý vị đừng lo lắng! Nhờ có lớp mỡ dày, bộ lông rậm rạp và khung xương sườn tròn đàn hồi cực tốt, nó lập tức cuộn tròn lăn lông lốc vài vòng như quả bóng bowling rồi ngồi dậy gãi tai tỉnh queo! Các nhà khoa học phát hiện hành vi lăn lộn này không chỉ giúp chúng giảm chấn động khi ngã cây, mà còn là một bài tập xả stress tuyệt vời để làm sạch lớp lông dính bùn đất! [surprise-oh]
```
**Part 3** → `audio/vs/scene04_p3.wav` (649 ký tự) · mood `don_dap`

```text
Ngay cả bộ lông hai màu đen trắng của nó cũng là một tuyệt tác ngụy trang! Mảng lông trắng giúp nó ẩn mình hoàn hảo giữa các vách đá đóng tuyết mùa đông, còn các khoanh lông đen quanh mắt, tai và bốn chân giúp nó hòa tan vào bóng râm rậm rạp của rừng trúc mùa hè! Đốm đen quanh mắt to như cặp kính râm còn giúp làm giảm độ chói lóa của ánh nắng mặt trời phản chiếu từ tuyết trắng! Chiếc đuôi ngắn ngủn mười lăm xăng-ti-mét ép sát mông hoạt động như một chiếc chổi quét bụi, giữ cho bàn tọa của gã béo luôn khô ráo ấm áp khi ngồi bệt xuống đất lạnh! Ngã cây như cơm bữa, lăn lộn như nghệ sĩ xiếc, nhưng tạo hóa đã bọc giáp từ đầu đến đuôi! [laughter]
```

### scene05 — 00 ĐÊM: CỬA SỔ THỤ THAI 48 GIỜ VÀ CỤC BÔNG 100G BÉ NHƯ THỎI SON
*Thẻ chương:* CỬA SỔ THỤ THAI DUY NHẤT 24-72 GIỜ MỖI NĂM

*Badge:* `22:00 ĐÊM` · *mood mặc định:* `nghiem_trang_gia`

**Part 0** → `audio/vs/scene05_p0.wav` (624 ký tự) · mood `nghiem_trang_gia`

```text
Màn đêm bao trùm rừng thẳm, đồng hồ điểm hai mươi hai giờ đêm! Không khí tĩnh mịch bỗng bị khuấy động bởi những âm thanh bí ẩn. Chúng tôi xin chuyển sang bản tin thời sự đặc biệt về sự tồn vong của loài: cuộc đua sinh sản nghẹt thở nhất hành tinh! Quý vị có biết tại sao Gấu Trúc lại từng đứng trước bờ vực tuyệt chủng không? [question-oh] Không chỉ vì phá hủy rừng tre, mà chính tạo hóa đã cài đặt cho chúng một chiếc đồng hồ sinh học cực kỳ khắt khe: mỗi năm, con cái chỉ có đúng một chu kỳ rụng trứng duy nhất, và cánh cửa màu mỡ để giao phối chỉ mở ra vỏn vẹn từ hai mươi tư đến bảy mươi hai tiếng đồng hồ! [surprise-wa]
```
**Part 1** → `audio/vs/scene05_p1.wav` (714 ký tự) · mood `don_dap`

```text
Đúng thế thưa quý vị! Đúng bốn mươi tám tiếng ngắn ngủi trong suốt ba trăm sáu mươi lăm ngày! Nếu trong hai ngày đó mà hai bên không tìm thấy nhau, hoặc chàng gấu mải ngồi nhai tre quên mất việc lớn, thì coi như mất trắng một năm! [laughter] Thậm chí các chuyên gia bảo tồn tại các trung tâm nhân giống từng phải mở cả video hướng dẫn giao phối cho chúng xem để học hỏi. Và điều kỳ diệu nhất diễn ra sau đó: khi một chú Gấu Trúc con chào đời, nó chỉ nặng đúng một trăm gam — tức là nhẹ bằng một phần chín trăm trọng lượng của gấu mẹ! Nhỏ thó bằng một thỏi son, đỏ hỏn, mù lòa và không có lấy một cọng lông! Sinh ra một cục bông tí hon mỏng manh giữa tự nhiên khắc nghiệt là một bài toán sinh tồn gian nan tột cùng!
```
**Part 2** → `audio/vs/scene05_p2.wav` (537 ký tự) · mood `hao_hung`

```text
Chưa kể, các cô gấu trúc còn nổi tiếng với màn kịch mang thai giả tinh quái khiến cả đội ngũ bác sĩ thú y phải toát mồ hôi hột! Khi nhận thấy những con gấu mang thai được chuyển vào phòng máy lạnh, được phục vụ táo ngon và bánh bao hảo hạng, một số cô nàng tinh ranh đã cố tình bắt chước triệu chứng ốm nghén: đi lại chậm chạp, ăn ít, ngủ nhiều để được hưởng chế độ chăm sóc năm sao suốt mấy tháng trời! Cho đến khi siêu âm không thấy em bé đâu, các bác sĩ mới té ngửa nhận ra mình vừa bị một diễn viên kịch gấu lừa ngoạn mục! [laughter]
```

### scene06 — 00 RẠNG SÁNG: KẾT THÚC 24H SINH TỒN VÀ BÀI HỌC TỪ CHÚ GẤU BÉO
*Thẻ chương:* BÀI HỌC SINH TỒN VÀ BẮC CẦU SANG TẬP 12 HÀ MÃ

*Badge:* `04:00 SÁNG` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (757 ký tự) · mood `am_ap`

```text
Bây giờ là không bốn giờ rạng sáng! Tiếng sương đêm nhỏ giọt trên những tán lá tre xào xạc, khép lại hành trình hai mươi tư giờ theo chân sinh vật đáng yêu nhất hành tinh. Nhiều người từng chế giễu Gấu Trúc là loài vật quyết tâm tự hủy, nhưng thực tế chứng minh điều ngược lại: Chiến thần ăn chay đã kiên cường vượt qua hơn hai triệu năm biến đổi khí hậu khắc nghiệt, sống sót qua cả kỷ băng hà khi các loài mãnh thú to lớn khác đều đã tuyệt chủng! [surprise-oh] Bằng cách hạ thấp nhu cầu năng lượng xuống mức tối thiểu, không tranh giành con mồi với ai, và biến sự vụng về thành nét đáng yêu khiến cả nhân loại phải chung tay bảo vệ, Gấu Trúc đã chọn cho mình một triết lý sinh tồn vô cùng độc đáo: chậm rãi, bình thản và hòa hợp tuyệt đối với thiên nhiên.
```
**Part 1** → `audio/vs/scene06_p1.wav` (415 ký tự) · mood `hao_hung`

```text
Đồng hồ lại sắp điểm không sáu giờ sáng, và một chu kỳ nhai tre mới lại chuẩn bị bắt đầu! Ở tập tiếp theo, chúng ta sẽ tạm biệt rừng tre Trung Quốc để bay thẳng sang những dòng sông châu Phi rực lửa, nơi một cỗ xe tăng bọc thịt đang chờ đợi: Hà Mã! Tuyệt đối không biết bơi nhưng chạy bộ dưới đáy sông với lực cắn một ngàn tám trăm PSI nghiền nát cá sấu! Hẹn gặp lại quý vị trong bản tin sinh tồn rực lửa tiếp theo!
```
**Part 2** → `audio/vs/scene06_p2.wav` (89 ký tự) · 🎭 cameo `phat_thanh_vien`

```text
Báo cáo trường quay, phóng viên xin phép ngắt sóng để đi ngủ một giấc như Gấu Trúc đây ạ!
```
**Part 3** → `audio/vs/scene06_p3.wav` (185 ký tự) · mood `hao_hung`

```text
Kính chúc quý vị một ngày tràn đầy năng lượng tích cực! Còn bạn, bạn ấn tượng nhất với mốc thời gian nào trong hai mươi tư giờ của Chiến thần ăn chay? Hãy để lại bình luận bên dưới nhé!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Sáu giờ sáng ở rừng tre Tứ Xuyên, một con gấu mang bộ ruột của thú ăn thịt lại bắt đầu ca nhai tre kéo dài mười bốn tiếng! Đó là Gấu Trúc Lớn, họ hàng của gấu xám, nặng cả tạ, chỉ sống ở vùng núi Trung Quốc. Hai triệu năm trước, tổ tiên nó mất vị giác với thịt nên chuyển hẳn sang ăn tre chín mươi chín phần trăm! [laughter] Nhưng ruột ngắn của thú ăn thịt chỉ hấp thụ được mười bảy phần trăm dinh dưỡng, nên mỗi ngày nó phải nạp tới ba mươi tám cân tre. [surprise-wa] Hậu quả là đi vệ sinh kỷ lục bốn mươi lần một ngày! Để bóc vỏ tre, xương cổ tay của nó phình to thành ngón tay cái thứ sáu, kẹp tre chắc như gọng kìm. Ăn ít năng lượng thì phải tiết kiệm: nó lười di chuyển, ngủ ngay trên cây, ngã xuống thì cuộn tròn lăn lông lốc rồi ăn tiếp. Vậy là bí mật đã rõ: không phải gấu trúc lười, mà nó đang sống đúng chế độ tiết kiệm pin của một kẻ ăn chay mang ruột ăn thịt!
```

**Whisper prompt:** `Gấu Trúc Lớn, Chiến thần ăn chay, Giant Panda, 06:00, 10:00, 14:00, 18:00, 22:00, 04:00, Tứ Xuyên, tre trúc, ngón tay cái giả, xương vừng, radial sesamoid, Xyanua, 17%, 40 lần, 24-72 giờ, 100g, 1/900, Hà Mã, Tas1r1`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| không sáu giờ | 06:00 |
| mười giờ | 10:00 |
| mười bốn giờ | 14:00 |
| mười tám giờ | 18:00 |
| hai mươi hai giờ | 22:00 |
| không bốn giờ | 04:00 |
| hai mươi tư tiếng | 24 tiếng |
| hai mươi tư trên bảy | 24/7 |
| mười bốn tiếng | 14 tiếng |
| mười sáu tiếng | 16 tiếng |
| mười tiếng | 10 tiếng |
| hai tiếng | 2 tiếng |
| bốn tiếng | 4 tiếng |
| bốn mươi lần | 40 lần |
| bốn mươi cân | 40kg |
| bốn mươi lăm cân | 45kg |
| mười hai cân | 12kg |
| ba mươi tám cân | 38kg |
| hai mươi lăm cân | 25kg |
| hai mươi cân | 20kg |
| mười cân | 10kg |
| mười bảy phần trăm | 17% |
| tám mươi ba phần trăm | 83% |
| chín mươi chín phần trăm | 99% |
| sáu ngón tay | 6 ngón tay |
| thứ sáu | thứ 6 |
| hai mươi tư đến bảy mươi hai tiếng | 24-72 giờ |
| hai mươi tư | 24 |
| bốn mươi tám tiếng | 48 tiếng |
| bảy mươi hai tiếng | 72 tiếng |
| ba trăm sáu mươi lăm ngày | 365 ngày |
| một năm | 1 năm |
| một trăm gam | 100g |
| một trăm ba mươi gam | 130g |
| chín mươi gam | 90g |
| một phần chín trăm | 1/900 |
| hai triệu năm | 2 triệu năm |
| Hai triệu năm | 2 triệu năm |
| Sáu giờ sáng | 6 giờ sáng |
| mười chín triệu năm | 19 triệu năm |
| hai ngàn | 2.000 |
| ba trăm ngàn | 300.000 |
| một ngàn tám trăm | 1.800 |
| mười lăm xăng-ti-mét | 15cm |
| hai trăm cân | 200kg |
| hàng triệu năm | hàng triệu năm |
| triệu năm | triệu năm |
| Tứ Xuyên | Tứ Xuyên |
| Xy-a-nua | Xyanua |
| Xương vừng | Xương vừng |
| xương vừng | xương vừng |
| Pan-đa | Panda |
| Tát-một-rờ-một | Tas1r1 |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · 00 SÁNG: BẮT ĐẦU CA NHAI TRE CẬT LỰC CỦA KẺ PHẢN BỘI TỔ TIÊN · 89.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:02.5 (2.5s) | L01 | Bây giờ là 06:00 sáng! |  | Rừng tre Tứ Xuyên mờ sương lúc 06:00 sáng: sương sớm lãng đãng quanh các rặng tre xanh ngắt; chiếc đồng hồ báo thức quả lắc khổng lồ cắm trên gờ đá; anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H, đeo ba lô tác nghiệp mặc áo khoác dã ngoại cầm micro phát biểu trước ống kính máy quay. |
| b02 | 00:02.5–00:12.5 (10.0s) | L02 | Kính thưa quý vị khán giả, chúng tôi đang có mặt trực tiếp tại khu rừng tre mù sương tỉnh Tứ Xuyên để tường thuật lại một ngày làm việc cật lực của sinh vật lười biếng bậc nhất hành tinh: Gấu Trúc Lớn! |  | anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H, đeo ba lô tác nghiệp chỉ tay về phía bụi tre lớn: chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo mộ |
| b03 | 00:12.5–00:20.5 (8.0s) | L03 | Chiếc đồng hồ sinh học vừa điểm hồi chuông báo thức, và nhân vật chính của chúng ta — Chiến thần ăn chay — đã lập tức ngồi bật dậy vào vị trí làm việc quen thuộc. |  | Chiếc đồng hồ báo thức khổng lồ rung bần bật chuông reo inh ỏi; chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay bật dậy ôm chân ngồi vào vị trí bệt quen  |
| b04 | 00:20.5–00:25.8 (5.3s) | L04 | Không tập thể dục, không đánh răng, công việc đầu tiên và duy nhất trong ngày của gã béo này là... |  | Chia đôi khung hình: BÊN TRÁI người tập thể hình hoạt hình chạy bộ mồ hôi nhễ nhại bị gạch chéo đỏ; BÊN PHẢI chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ  |
| b05 | 00:25.8–00:29.0 (3.2s) | L05 | bốc một thanh tre cho thẳng vào mồm nhai rôm rốp! |  | Cận cảnh chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay bốc cành tre to tướng cho thẳng vào mồm nhai rôm rốp; dăm tre và lá tre xanh bắn tung tóe quanh  |
| b06 | 00:29.0–00:34.0 (5.0s) | L06 | Alo trường quay nghe rõ không? Phóng viên cho hỏi gã này định nhai tre đến bao giờ thế? |  | Trường quay tin tức hiện đại: cô phát thanh viên tin tức hoạt hình xinh đẹp ngồi sau bàn trường quay tin tức thời sự ngồi sau bàn phát thanh viên đeo tai nghe, tay cầm bút chỉ vào màn hình hiện trường ngạc nhiên hỏi phóng viên. |
| b07 | 00:34.0–00:38.9 (4.8s) | L07 | Báo cáo trường quay, gã này sẽ ngồi nhai liên tục từ mười đến 14 tiếng mỗi ngày, không ngừng nghỉ! | **14 TIẾNG** · nhai tre liên tục · R/360 · [0.7, 0.45] | Biểu đồ đồng hồ 24h: dải màu xanh lá kéo dài từ 10 tiếng đến 14 tiếng có hình cành tre nhai liên tục; chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay ngồ |
| b08 | 00:38.9–00:48.1 (9.2s) | L08 | Điều nghịch lý đến phát điên là: xét về mặt sinh học và phả hệ tiến hóa 19 triệu năm, Gấu Trúc thuộc bộ thú ăn thịt chính hiệu, cùng một tổ tiên với gấu xám, sư tử và chó sói! | **19 TR NĂM** · tổ tiên thú ăn thịt · L/380 · [0.35, 0.45] | Cây phả hệ tiến hóa 19 triệu năm: nhánh trên là sư tử oai vệ, gấu xám hung tợn và chó sói đang gầm gừ; nhánh dưới rẽ nhánh là chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay  |
| b09 | 00:48.1–00:56.0 (7.9s) | L09 | Hộp sọ của nó có cơ hàm cực khỏe, răng nanh sắc nhọn và đường ruột ngắn cũn cỡn chuyên dùng để tiêu hóa thịt tươi béo ngậy. Nhưng không hiểu vì một pha bẻ lái lịch sử nào của tạo |  | Sơ đồ giải phẫu X-quang: hộp sọ có hàm răng nanh sắc nhọn và đường ruột ngắn cũn cỡn màu đỏ đặc trưng của thú ăn thịt; KHÔNG có chú Gấu Trúc trong cảnh này. |
| b10 | 00:56.0–00:58.4 (2.4s) | L10 | hóa, khoảng 2 triệu năm trước, tổ tiên của nó bỗng | **2 TR NĂM** · pha bẻ lái ăn chay · R/380 · [0.65, 0.5] | Cỗ máy thời gian quay ngược 2 triệu năm trước: gấu tổ tiên quay ngoắt 180 độ quay lưng từ chối đùi thịt nướng bốc khói, chạy sang ôm chặt bụi tre xanh. |
| b11 | 00:58.4–01:04.8 (6.5s) | L11 | nhiên... mất đi cảm nhận vị umami của thịt, chán ăn thịt chuyển hẳn sang ăn chay 99% bằng lá tre và thân tre! | **99%** · khẩu phần là tre · L/360 · [0.3, 0.5] | chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay ngồi lọt thỏm giữa núi tre trúc xanh mướt cao ngất, cười toe toét ngắt từng phiến lá tre nhét đầy mồm. |
| b12 | 01:04.8–01:12.1 (7.2s) | L12 | Các nhà khoa học phát hiện đột biến trên gen Tas1r1 đã biến chiếc lưỡi sành ăn thịt của tổ tiên nó thành kẻ mù vị giác với món bít-tết! |  | Mô hình chuỗi xoắn ADN phát sáng: đoạn gen Tas1r1 bị đứt gãy tia sét đỏ; bên cạnh là chiếc lưỡi gấu trúc có dấu gạch chéo đỏ trên đĩa thịt bò bít-tết. |
| b13 | 01:12.1–01:24.3 (12.3s) | L13 | Đối với Chiến thần ăn chay, một tảng thịt bò thơm phức béo ngậy bây giờ cũng nhạt toẹt và vô vị y hệt một miếng bìa các-tông ngâm nước! Thà rằng ngồi gặm cành tre tươi đẫm sương sớm còn cảm thấy thanh tao và hợp khẩu vị hơn gấp vạn lần! |  | Bàn ăn đối chiếu bi hài: BÊN TRÁI đĩa thịt bò bít-tết hảo hạng thơm phức bị chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay đẩy phũ phàng ra xa chê nhạt  |
| b14 | 01:24.3–01:29.4 (5.0s) | L14 | Hãy cùng chúng tôi đếm ngược từng mốc giờ để xem cỗ máy ăn chay này vận hành kỳ dị ra sao! |  | anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H, đeo ba lô tác nghiệp giơ ngón tay ra hiệu đếm ngược, phía sau là chiếc đồng hồ cát đang chảy và kim đồng hồ 24h quay tít mù báo hiệu hành trình kỳ thú. |

### scene02 · 00 TRƯA: GIẢI MÃ NGÓN TAY CÁI THỨ SÁU VÀ HÀM NGHIỀN XƯƠNG · 83.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.7 (8.7s) | L15 | Đồng hồ điểm 10:00 trưa! Cập nhật mới nhất từ hiện trường: sau 4 tiếng nhai tre không ngừng nghỉ, Chiến thần ăn chay đã xử lý gọn gàng hơn 10kg cành tre cứng như gỗ lim! | **10 KG** · xử lý trong 4 tiếng · L/380 · [0.4, 0.55] | Đồng hồ hiện số 10:00 trưa; chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay ngồi lọt thỏm giữa đống vỏ tre đã bị tước bỏ chất cao như núi nhỏ, tay vẫn th |
| b02 | 00:08.7–00:18.9 (10.1s) | L17 | Quý vị có bao giờ thắc mắc tại sao một con gấu to béo vụng về lại có thể cầm nắm từng nhánh tre thanh thoát, bóc lớp vỏ cứng một cách điệu nghệ chẳng khác nào một đầu bếp chuyên nghiệp bóc vỏ mía không? |  | Cận cảnh bàn tay chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay bóc vỏ cành tre điệu nghệ như nghệ nhân gọt mía; bên cạnh là một người đầu bếp chuyên ng |
| b03 | 00:18.9–00:27.6 (8.8s) | L18 | Camera góc siêu cận của chúng tôi vừa ghi lại một bí mật giải phẫu kinh ngạc: bàn tay trước của Gấu Trúc không phải có năm ngón như các loài gấu khác, mà sở hữu tới 6 ngón tay! | **6 NGÓN TAY** · bàn tay bóc vỏ tre · R/360 · [0.65, 0.45] | Bàn tay trước của Gấu Trúc xòe rộng dưới ống kính phóng đại: đếm rõ 5 ngón móng vuốt nhọn hoắt và ngón thứ 6 nhô ra bên cạnh ngón cái. |
| b04 | 00:27.6–00:32.9 (5.3s) | L19 | Này phóng viên ơi, làm gì có loài thú nào mọc 6 ngón tay thật, chắc chắn là đạo cụ gắn thêm rồi! |  | ông cụ nhân chứng râu tóc bạc phơ chống gậy trúc chống gậy trúc bước vào khung hình, nheo mắt chỉ tay vào bàn tay gấu trúc vẻ mặt nghi ngờ bảo đạo cụ giả. |
| b05 | 00:32.9–00:35.3 (2.4s) | L20 | Bác nhân chứng nói gần đúng rồi đấy! |  | anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H, đeo ba lô tác nghiệp cầm bảng sơ đồ giải phẫu gật đầu giải thích thân thiện; chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nh |
| b06 | 00:35.3–00:48.4 (13.1s) | L21 | Trên thực tế, ngón tay cái phụ này không phải là một ngón tay thật, mà là xương vừng cổ tay phình to dị thường, bọc một lớp đệm thịt dày cộp bên ngoài. Tiến hóa đã biến chiếc xương cổ tay này thành một ngón tay cái giả hoạt động linh hoạt đối diện với năm ngón còn lại, | **XƯƠNG VỪNG** · ngón tay cái giả · L/380 · [0.4, 0.5] | Bản vẽ X-quang xương bàn tay: xương vừng cổ tay (radial sesamoid) phình to dài ra bọc đệm thịt dẻo dai thành ngón cái giả linh hoạt; KHÔNG có chú Gấu Trúc trong cảnh này. |
| b07 | 00:48.4–00:55.0 (6.6s) | L22 | giúp nó kẹp chặt từng thân tre tròn lẳn và tước bỏ lớp vỏ đắng ngắt một cách chuẩn xác từng mi-li-mét! |  | Hình minh họa kỹ thuật cơ khí: ngón cái giả kẹp đối diện 5 ngón kia như gọng kìm thợ máy, tước phăng dải vỏ tre đắng ngắt chuẩn xác từng milimet. |
| b08 | 00:55.0–01:02.0 (7.0s) | L23 | Chưa dừng lại ở bàn tay khéo léo, hãy nhìn vào khuôn mặt tròn xoe phúng phính đáng yêu như chiếc bánh bao của nó! Quý vị đừng để vẻ dễ thương đánh lừa: |  | Cận cảnh khuôn mặt bánh bao tròn xoe của chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay: má phồng to phúng phính, hai mắt khoanh đen chớp chớp ngây thơ  |
| b09 | 01:02.0–01:12.7 (10.7s) | L24 | hai bên má phúng phính thực chất là hai khối cơ cắn khổng lồ neo thẳng lên gờ đỉnh sọ! Lực cắn của Chiến thần ăn chay mạnh tới mức chỉ đứng sau loài linh cẩu đốm nghiền xương, đủ sức bẻ vụn thân tre già dày cộp như nhai bim bim! |  | Sơ đồ cơ giải phẫu đầu gấu: hai búi cơ cắn khổng lồ màu đỏ kéo từ xương hàm dưới neo thẳng lên đỉnh sọ gấu trúc; lực cắn cực mạnh nghiền nát thân tre cứng. |
| b10 | 01:12.7–01:19.2 (6.5s) | L25 | Toàn bộ niêm mạc vòm họng và thực quản của nó còn được lót một lớp màng nhầy siêu dày để các dằm tre sắc nhọn không thể đâm thủng nội tạng khi nuốt! |  | Mặt cắt phóng đại ống thực quản: lớp màng nhầy dày cộp tráng men bảo vệ, các mảnh dằm tre nhọn hoắt trượt tuột xuống dạ dày mà không gây xước xát; KHÔNG có chú Gấu Trúc trong cảnh này. |
| b11 | 01:19.2–01:23.5 (4.3s) | L26 | Vũ khí của mãnh thú săn mồi thượng thừa, nhưng dùng vào việc nhai cỏ cây! |  | Hình ảnh hài hước: chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay mặc giáp chiến binh hầm hố cơ bắp cuồn cuộn như đấu sĩ La Mã, nhưng tay lại cầm nhánh  |

### scene03 · 00 CHIỀU: CỖ MÁY TIÊU HÓA CHỈ HẤP THỤ 17% VÀ THẢI 25KG PHÂN · 85.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:06.5 (6.5s) | L27 | Bây giờ là 14:00 chiều! Chúng tôi vừa phải lùi xa hiện trường mười bước vì một kỷ lục sinh học vô tiền khoáng hậu sắp diễn ra. |  | Đồng hồ chỉ 14:00 chiều; anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H, đeo ba lô tác nghiệp đeo khẩu trang bảo hộ lùi lại phía sau vài bước, tay cầm thước dây đo khoảng cách an toàn. |
| b02 | 00:06.5–00:12.0 (5.4s) | L28 | Quý vị hãy giữ chặt mũ: mỗi ngày, một chú Gấu Trúc trưởng thành phải nạp từ 12kg đến 38kg tre tươi. | **38 KG** · tre nạp mỗi ngày · R/360 · [0.72, 0.5] | chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay ngồi trước một xe cút kít chở đầy 38kg tre tươi xanh mướt; bụng chú phình to tròn xoe như quả bóng bay. |
| b03 | 00:12.0–00:22.0 (10.1s) | L29 | Nhưng vì mang ruột thú ăn thịt ngắn ngủn, không có bốn ngăn dạ dày như trâu bò, cũng chẳng có vi khuẩn lên men phân giải chất xơ như loài ngựa, hệ tiêu hóa của nó chỉ hấp thụ vỏn vẹn đúng 17% chất dinh dưỡng! | **17%** · hấp thụ dinh dưỡng · L/380 · [0.35, 0.5] | Sơ đồ đối chiếu hệ tiêu hóa: BÊN TRÁI ruột trâu bò 4 ngăn dài 40m tiêu hóa 80%; BÊN PHẢI ruột Gấu Trúc ngắn ngủn thẳng tuột chỉ tiêu hóa được 17%. |
| b04 | 00:22.0–00:30.7 (8.6s) | L30 | Tới 83% lượng tre nuốt vào bụng sẽ trôi tuột ra ngoài nguyên vẹn hình sợi chỉ sau 2 tiếng đồng hồ! Và hệ quả tất yếu là gì? | **83%** · thải ra ngoài · R/380 · [0.65, 0.5] | Ống tiêu hóa như máng trượt nước siêu tốc: thân tre đi vào miệng và trượt tuột ra ngoài thành các sợi tre nguyên vẹn chỉ trong 2 tiếng đồng hồ. |
| b05 | 00:30.7–00:37.5 (6.9s) | L31 | Xin thông báo một con số kỷ lục: Chiến thần ăn chay phải đi vệ sinh tới 40 lần mỗi ngày! Đúng vậy, quý vị không hề nghe nhầm đâu, 40 lần một ngày, | **40 LẦN** · đi vệ sinh mỗi ngày · L/360 · [0.4, 0.45] | Bảng đếm kỷ lục số điện tử nhảy số liên tục: con số 40 nhấp nháy phát sáng rực rỡ; chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay ngồi trên bô vệ sinh h |
| b06 | 00:37.5–00:40.3 (2.7s) | L32 | thải ra từ 20kg đến 25kg phân tre tươi! | **25 KG** · phân tre mỗi ngày · R/360 · [0.68, 0.5] | Một chiếc cân tải trọng lớn chất đầy các viên phân tre màu xanh lá nặng 25kg; chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay đứng cạnh giơ hai ngón tay  |
| b07 | 00:40.3–00:44.5 (4.3s) | L33 | Vừa ngồi nhai cành tre đằng trước, đằng sau đã xả ra đống bã tre thơm mùi cỏ non. |  | Cảnh bi hài: miệng phía trước chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay nhai tre nhồm nhoàm, phía sau đùn ra từng nắm phân tre cuộn tròn sạch sẽ. |
| b08 | 00:44.5–00:49.2 (4.7s) | L34 | Các nhà sinh vật học khi vào rừng chỉ cần đếm số lượng bãi thải là biết ngay gã béo này đã ngồi ở gốc cây đó bao |  | Nhà khoa học hoạt hình đeo kính lúp đi trong rừng tre, vừa đếm từng bãi phân tre vừa bấm đồng hồ bấm giờ tính thời gian gấu ngồi ở gốc cây. |
| b09 | 00:49.2–00:59.9 (10.6s) | L35 | nhiêu phút. Đây chính xác là một cỗ máy nghiền tre di động: năng suất nghiền cực cao, tiêu hóa cực kém, và xả thải liên tục 24/7! Điều bi hài nhất là phân của nó sạch đến mức người ta không thể nhịn |  | Biểu tượng cỗ máy nghiền tre chạy bằng xích: đầu vào là tre cây, đầu ra là các cuộn bã xơ tre đóng gói liên tục 24/7. |
| b10 | 00:59.9–01:09.7 (9.8s) | L36 | cười! Vì 99% thức ăn là tre trúc và thời gian lưu trong ruột quá ngắn, phân gấu trúc hầu như không có mùi hôi thối mà thơm dịu mùi lá tre lên men thoang thoảng như trà xanh! |  | Cận cảnh viên phân tre: xơ lá tre xanh ép chặt thơm ngát, tỏa ra các làn khói hương thảo mộc và lá trà xanh thoang thoảng; đàn bướm bay lượn xung quanh. |
| b11 | 01:09.7–01:19.4 (9.7s) | L37 | Tại Tứ Xuyên, người ta đã tận dụng loại phân giàu chất xơ này để tẩy sạch làm giấy thủ công mỹ nghệ cao cấp, thậm chí dùng bã phân ủ trà xanh bán với giá hàng ngàn đô-la một cân! |  | Xưởng thủ công mỹ nghệ: người thợ đang ép bã phân tre làm các tờ giấy mỹ thuật vàng nhạt cao cấp; bên cạnh là hộp trà phân gấu trúc gắn thẻ giá đô-la đắt đỏ. |
| b12 | 01:19.4–01:25.5 (6.1s) | L38 | Ai mà ngờ chất thải của kẻ ăn chay lười biếng lại biến thành mỏ vàng sinh thái độc lạ bậc nhất thế giới! |  | chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay ngồi trên ngai vàng làm bằng búp măng tre, hai tay ôm các thỏi vàng sinh thái cười khoái chí tột độ. |

### scene04 · 00 HOÀNG HÔN: NHỮNG PHA NGÃ CÂY KINH ĐIỂN VÀ NGỦ BẤT CHẤP TƯ THẾ · 89.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:13.3 (13.3s) | L39 | Ánh hoàng hôn buông xuống rừng tre, đồng hồ điểm 18:00 tối! Sau một ca làm việc cật lực ăn uống và xả thải, Chiến thần ăn chay quyết định leo lên ngọn cây cao để nghỉ ngơi thư giãn. Và đây chính là khoảnh khắc chương trình biểu diễn xiếc hài hước nhất tự nhiên bắt đầu! |  | Rừng tre chuyển sang màu hoàng hôn cam đỏ rực rỡ, đồng hồ chỉ 18:00 tối; chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay lạch bạch trèo lên một cây tre c |
| b02 | 00:13.3–00:19.8 (6.5s) | L40 | Quý vị hãy nhìn lên chạc cây: thân hình tròn xoe nặng hơn một tạ của nó đang vắt vẻo trên một cành cây nhỏ chỉ to bằng cổ tay. |  | Cành cây nhỏ cong oằn mình dưới sức nặng hơn một tạ của chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay; chú vắt vẻo ngủ say sưa bất chấp độ cao. |
| b03 | 00:19.8–00:27.9 (8.1s) | L41 | Nó ngủ trong những tư thế không tưởng: đầu chúc xuống đất, bốn chân buông thõng đung đưa, hoặc nằm ngửa bụng phơi nắng như một bao tải gạo bị bỏ quên trên ngọn cây! |  | Ghép 3 tư thế ngủ quái đản của chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay: đầu chúc xuống đất như con dơi, nằm ngửa bụng chân gác lên trời, và vắt n |
| b04 | 00:27.9–00:31.6 (3.6s) | L42 | Ối ối bác phóng viên ơi, cành cây gãy rồi kìa, đỡ cháu với! |  | chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay tỉnh giấc thấy cành cây uốn cong kêu rắc rắc, mặt hoảng hốt chới với kêu cứu anh chàng phóng viên truyền  |
| b05 | 00:31.6–00:40.4 (8.8s) | L43 | Rắc! Bịch! Một pha tiếp đất đỉnh cao không thể đỡ nổi! Cành cây gãy đôi và Chiến thần ăn chay rơi tự do từ độ cao vài mét đập mông xuống đất. Nhưng quý vị đừng lo lắng! |  | Cành cây gãy đôi kêu rắc, chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay rơi tự do từ ngọn cây xuống đất, mặt méo xệch hài hước giơ 4 chân lên trời. |
| b06 | 00:40.4–00:50.0 (9.7s) | L44 | Nhờ có lớp mỡ dày, bộ lông rậm rạp và khung xương sườn tròn đàn hồi cực tốt, nó lập tức cuộn tròn lăn lông lốc vài vòng như quả bóng bowling rồi ngồi dậy gãi tai tỉnh queo! |  | chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay tiếp đất cuộn tròn tròn xoe lăn lông lốc như quả bóng bowling đâm ngã mấy khúc gỗ mục, rồi bật dậy gãi ta |
| b07 | 00:50.0–00:59.5 (9.5s) | L65 | Các nhà khoa học phát hiện hành vi lăn lộn này không chỉ giúp chúng giảm chấn động khi ngã cây, mà còn là một bài tập xả stress tuyệt vời để làm sạch lớp lông dính bùn đất! |  | Các nhà khoa học mỉm cười gật gù ghi chép: hành vi lăn lộn giảm chấn và làm sạch lông dính bùn đất. |
| b08 | 00:59.5–01:11.9 (12.4s) | L45 | Ngay cả bộ lông hai màu đen trắng của nó cũng là một tuyệt tác ngụy trang! Mảng lông trắng giúp nó ẩn mình hoàn hảo giữa các vách đá đóng tuyết mùa đông, còn các khoanh lông đen quanh mắt, tai và bốn chân giúp nó hòa tan vào bóng râm rậm rạp của rừng trúc mùa hè! |  | Phân tích trang phục ngụy trang: nửa trái nền tuyết trắng xóa chú hòa vào tuyết; nửa phải bụi râm tối chú hòa vào bóng râm rừng cây. |
| b09 | 01:11.9–01:17.5 (5.6s) | L46 | Đốm đen quanh mắt to như cặp kính râm còn giúp làm giảm độ chói lóa của ánh nắng mặt trời phản chiếu từ tuyết trắng! |  | Cận cảnh đôi mắt chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay: hai khoanh đen quanh mắt như cặp kính râm thời trang giúp chống chói lóa ánh nắng phản  |
| b10 | 01:17.5–01:24.9 (7.4s) | L47 | Chiếc đuôi ngắn ngủn 15cm ép sát mông hoạt động như một chiếc chổi quét bụi, giữ cho bàn tọa của gã béo luôn khô ráo ấm áp khi ngồi bệt xuống đất lạnh! | **15 CM** · chiếc đuôi chổi quét · L/380 · [0.4, 0.5] | Phía sau mông chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay: chiếc đuôi cụt 15cm hoạt động như chiếc chổi phủi sạch tuyết ướt trên chạc cây trước khi n |
| b11 | 01:24.9–01:29.7 (4.8s) | L48 | Ngã cây như cơm bữa, lăn lộn như nghệ sĩ xiếc, nhưng tạo hóa đã bọc giáp từ đầu đến đuôi! |  | chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay đứng dang hai tay chào như vận động viên xiếc vừa hoàn thành bài biểu diễn tiếp đất hoàn hảo, khán giả vỗ |

### scene05 · 00 ĐÊM: CỬA SỔ THỤ THAI 48 GIỜ VÀ CỤC BÔNG 100G BÉ NHƯ THỎI SON · 90.1s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:06.1 (6.1s) | L49 | Màn đêm bao trùm rừng thẳm, đồng hồ điểm 22:00 đêm! Không khí tĩnh mịch bỗng bị khuấy động bởi những âm thanh bí ẩn. |  | Rừng tre đêm tĩnh mịch ánh trăng le lói, đồng hồ chỉ 22:00 đêm; anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H, đeo ba lô tác nghiệp cầm đèn pin soi vào lối mòn trong rừng bí ẩn. |
| b02 | 00:06.1–00:20.9 (14.8s) | L50 | Chúng tôi xin chuyển sang bản tin thời sự đặc biệt về sự tồn vong của loài: cuộc đua sinh sản nghẹt thở nhất hành tinh! Quý vị có biết tại sao Gấu Trúc lại từng đứng trước bờ vực tuyệt chủng không? Không chỉ vì phá hủy rừng tre, mà chính tạo hóa đã cài đặt cho chúng một chiếc đồng hồ sinh học cực kỳ khắt khe: |  | Bảng tin thời sự khẩn: biểu đồ đếm ngược nhấp nháy dòng chữ báo động đỏ về mùa sinh sản của Gấu Trúc. |
| b03 | 00:20.9–00:29.1 (8.2s) | L51 | mỗi năm, con cái chỉ có đúng một chu kỳ rụng trứng duy nhất, và cánh cửa màu mỡ để giao phối chỉ mở ra vỏn vẹn từ 24-72 giờ đồng hồ! | **24-72 GIỜ** · cửa sổ thụ thai · R/360 · [0.68, 0.45] | Tờ lịch 365 ngày rơi rụng, chỉ còn lại đúng một tờ giấy nhỏ khoanh tròn đỏ với chiếc đồng hồ đếm ngược 24 đến 72 giờ thụ thai duy nhất. |
| b04 | 00:29.1–00:40.3 (11.2s) | L52 | Đúng thế thưa quý vị! Đúng 48 tiếng ngắn ngủi trong suốt 365 ngày! Nếu trong hai ngày đó mà hai bên không tìm thấy nhau, hoặc chàng gấu mải ngồi nhai tre quên mất việc lớn, thì coi như mất trắng 1 năm! | **365 NGÀY** · chỉ có 1 cơ hội · L/380 · [0.35, 0.5] | Cảnh bi hài: chàng Gấu Trúc ngồi mải mê nhai tre ở góc trái; cô Gấu Trúc ngồi chờ đợi ở góc phải thở dài, đồng hồ cát chảy hết cát. |
| b05 | 00:40.3–00:45.8 (5.5s) | L53 | Thậm chí các chuyên gia bảo tồn tại các trung tâm nhân giống từng phải mở cả video hướng dẫn giao phối cho chúng xem để học hỏi. |  | Trong trung tâm bảo tồn: chiếc tivi phát cảnh hai chú gấu trúc hẹn hò; bên dưới hai chú gấu trúc ngồi xem vừa cắn búp măng vừa ngơ ngác không hiểu gì. |
| b06 | 00:45.8–00:53.4 (7.5s) | L54 | Và điều kỳ diệu nhất diễn ra sau đó: khi một chú Gấu Trúc con chào đời, nó chỉ nặng đúng 100g — tức là nhẹ bằng 1/900 trọng lượng của gấu | **100 GAM** · bé như thỏi son · L/360 · [0.35, 0.45]<br>**1/900** · trọng lượng mẹ · R/480 · [0.65, 0.55] | Cận cảnh bàn tay to lớn của gấu mẹ: trong lòng bàn tay là chú gấu trúc sơ sinh bé tí hin màu hồng, không có lông, nhỏ thó như thỏi son môi. |
| b07 | 00:53.4–01:02.1 (8.8s) | L66 | mẹ! Nhỏ thó bằng một thỏi son, đỏ hỏn, mù lòa và không có lấy một cọng lông! Sinh ra một cục bông tí hon mỏng manh giữa tự nhiên khắc nghiệt là một bài toán sinh tồn gian nan tột cùng! |  | Gấu trúc con đỏ hỏn mù lòa nằm lọt thỏm cạnh thỏi son môi và cục bơ nhỏ để so sánh kích thước tí hon kỳ lạ. |
| b08 | 01:02.1–01:09.3 (7.2s) | L55 | Chưa kể, các cô gấu trúc còn nổi tiếng với màn kịch mang thai giả tinh quái khiến cả đội ngũ bác sĩ thú y phải toát mồ hôi hột! |  | Phòng điều hòa VIP trong viện bảo tồn: một cô gấu trúc giả vờ nằm rên rỉ ốm nghén, được bác sĩ bưng đĩa táo đỏ và bánh bao ngọt phục vụ tận mồm. |
| b09 | 01:09.3–01:22.7 (13.3s) | L67 | Khi nhận thấy những con gấu mang thai được chuyển vào phòng máy lạnh, được phục vụ táo ngon và bánh bao hảo hạng, một số cô nàng tinh ranh đã cố tình bắt chước triệu chứng ốm nghén: đi lại chậm chạp, ăn ít, ngủ nhiều để được hưởng chế độ chăm sóc năm sao suốt mấy tháng |  | Cô nàng gấu trúc tinh ranh giả vờ đi lại chậm chạp ốm nghén để được tận hưởng dịch vụ khách sạn 5 sao ăn ngon ngủ kỹ. |
| b10 | 01:22.7–01:30.1 (7.4s) | L56 | trời! Cho đến khi siêu âm không thấy em bé đâu, các bác sĩ mới té ngửa nhận ra mình vừa bị một diễn viên kịch gấu lừa ngoạn mục! |  | Bác sĩ cầm máy siêu âm rà bụng gấu trúc, màn hình siêu âm chỉ toàn là lá tre và hơi gas, không có em bé; cô gấu trúc nháy mắt cười tinh quái. |

### scene06 · 00 RẠNG SÁNG: KẾT THÚC 24H SINH TỒN VÀ BÀI HỌC TỪ CHÚ GẤU BÉO · 73.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.7 (8.7s) | L57 | Bây giờ là 04:00 rạng sáng! Tiếng sương đêm nhỏ giọt trên những tán lá tre xào xạc, khép lại hành trình 24 giờ theo chân sinh vật đáng yêu nhất hành tinh. |  | Bầu trời rạng sáng 04:00 sương đọng trên lá tre lung linh; chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay ngồi bình thản ngắm bình minh trên đỉnh núi đá |
| b02 | 00:08.7–00:22.7 (14.0s) | L58 | Nhiều người từng chế giễu Gấu Trúc là loài vật quyết tâm tự hủy, nhưng thực tế chứng minh điều ngược lại: Chiến thần ăn chay đã kiên cường vượt qua hơn 2 triệu năm biến đổi khí hậu khắc nghiệt, sống sót qua cả kỷ băng hà khi các loài mãnh thú to lớn khác đều đã tuyệt chủng! | **2 TR NĂM** · chiến thần sinh tồn · L/380 · [0.35, 0.5] | Dòng thời gian 2 triệu năm: các loài hổ răng kiếm, voi ma-mút to xác ngã gục tuyệt chủng; riêng chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay vẫn ung d |
| b03 | 00:22.7–00:36.9 (14.3s) | L59 | Bằng cách hạ thấp nhu cầu năng lượng xuống mức tối thiểu, không tranh giành con mồi với ai, và biến sự vụng về thành nét đáng yêu khiến cả nhân loại phải chung tay bảo vệ, Gấu Trúc đã chọn cho mình một triết lý sinh tồn vô cùng độc đáo: chậm rãi, bình thản và hòa hợp tuyệt đối với thiên nhiên. |  | Triết lý sống an nhiên: chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay ngồi thiền trên tảng đá phẳng, biểu tượng thái cực và hoa sen tre tỏa sáng; chậm  |
| b04 | 00:36.9–00:42.0 (5.0s) | L60 | Đồng hồ lại sắp điểm 06:00 sáng, và một chu kỳ nhai tre mới lại chuẩn bị bắt đầu! |  | Chiếc đồng hồ 24h quay trọn một vòng trở về vạch 06:00 sáng; chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay vươn vai ngáp một cái thật to rồi với tay lấ |
| b05 | 00:42.0–00:49.2 (7.3s) | L61 | Ở tập tiếp theo, chúng ta sẽ tạm biệt rừng tre Trung Quốc để bay thẳng sang những dòng sông châu Phi rực lửa, nơi một cỗ xe tăng bọc thịt đang |  | Bản đồ dịch chuyển từ rừng tre Trung Quốc sang dòng sông châu Phi rực lửa: một chú Hà Mã khổng lồ đang chạy bộ thình thịch dưới đáy sông nước cuồn cuộn. |
| b06 | 00:49.2–00:58.6 (9.4s) | L62 | chờ đợi: Hà Mã! Tuyệt đối không biết bơi nhưng chạy bộ dưới đáy sông với lực cắn 1.800 PSI nghiền nát cá sấu! Hẹn gặp lại quý vị trong bản tin sinh tồn rực lửa tiếp theo! | **1.800 PSI** · lực cắn xe tăng · R/360 · [0.7, 0.5] | Cận cảnh Hà Mã há ngoác mồm 150 độ lộ cặp răng nanh khủng khiếp cắn nát một khúc gỗ mục; lực cắn 1.800 PSI khủng khiếp. |
| b07 | 00:58.6–01:03.2 (4.5s) | L63 | Báo cáo trường quay, phóng viên xin phép ngắt sóng để đi ngủ một giấc như Gấu Trúc đây ạ! |  | anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H, đeo ba lô tác nghiệp tháo tai nghe, ngả lưng vào đống lá tre ngáy khò khò; màn hình TV hiển thị chữ 'TẠM BIỆT & HẸN GẶP LẠI'. |
| b08 | 01:03.2–01:13.0 (9.8s) | L64 | Kính chúc quý vị một ngày tràn đầy năng lượng tích cực! Còn bạn, bạn ấn tượng nhất với mốc thời gian nào trong 24 giờ của Chiến thần ăn chay? Hãy để lại bình luận bên dưới nhé! |  | chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay và anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H, đe |

## 5. Phân cảnh Shorts — từng beat

Banner: **RUỘT ĂN THỊT NHƯNG / NHAI TRE 14 TIẾNG?!** · giọng 46.0s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | 6 giờ sáng ở rừng tre Tứ Xuyên, một con gấu mang bộ ruột của thú ăn thịt lại bắt đầu ca nhai tre kéo dài 14 tiếng! | **14 TIẾNG** · nhai tre mỗi ngày · R/600 · [0.6, 0.5] |
| s02 | 00:06.8 | S13 | Đó là Gấu Trúc Lớn, họ hàng của gấu xám, nặng cả tạ, chỉ sống ở vùng núi Trung Quốc. |  |
| s03 | 00:11.3 | S12 | 2 triệu năm trước, tổ tiên nó mất vị giác với thịt nên chuyển hẳn sang ăn tre 99%! | **2 TR NĂM** · đổi sang ăn tre · L/650 · [0.4, 0.45]<br>**99%** · khẩu phần là tre · R/900 · [0.6, 0.6] |
| s04 | 00:16.4 | S04 | Nhưng ruột ngắn của thú ăn thịt chỉ hấp thụ được 17% dinh dưỡng, | **17%** · hấp thụ ít ỏi · R/580 · [0.65, 0.45] |
| s05 | 00:21.6 | S14 | nên mỗi ngày nó phải nạp tới 38kg tre. | **38 KG** · tre mỗi ngày · L/600 · [0.45, 0.4] |
| s06 | 00:25.1 | S05 | Hậu quả là đi vệ sinh kỷ lục 40 lần một ngày! | **40 LẦN** · vệ sinh/ngày · R/820 · [0.65, 0.65] |
| s07 | 00:27.6 | S06 | Để bóc vỏ tre, xương cổ tay của nó phình to thành ngón tay cái thứ 6, kẹp tre chắc như gọng kìm. | **NGÓN THỨ 6** · ngón cái giả · L/650 · [0.45, 0.5] |
| s08 | 00:32.6 | S15 | Ăn ít năng lượng thì phải tiết kiệm: nó lười di chuyển, ngủ ngay trên cây, |  |
| s09 | 00:36.9 | S08 | ngã xuống thì cuộn tròn lăn lông lốc rồi ăn tiếp. |  |
| s10 | 00:39.5 | S17 | Vậy là bí mật đã rõ: không phải gấu trúc lười, |  |
| s11 | 00:42.2 | S16 | mà nó đang sống đúng chế độ tiết kiệm pin của một kẻ ăn chay mang ruột ăn thịt! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bây giờ là 06:00 sáng!". Bố cục: Rừng tre Tứ Xuyên mờ sương lúc 06:00 sáng: sương sớm lãng đãng quanh các rặng tre xanh ngắt; chiếc đồng hồ báo thức quả lắc khổng lồ cắm trên gờ đá; anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H, đeo ba lô tác nghiệp mặc áo khoác dã ngoại cầm micro phát biểu trước ống kính máy quay.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kính thưa quý vị khán giả, chúng tôi đang có mặt trực tiếp tại khu rừng tre mù sương tỉnh Tứ Xuyên để tường thuật lại một ngày làm việc cật lực của sinh vật lười biếng bậc nhất hành tinh: Gấu Trúc Lớn!". Bố cục: anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H, đeo ba lô tác nghiệp chỉ tay về phía bụi tre lớn: chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay đang ngồi bệt dưới đất, hai mắt thâm quầng lim dim ngơ ngác, chiếc bụng mỡ tròn xoe lắc lư.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiếc đồng hồ sinh học vừa điểm hồi chuông báo thức, và nhân vật chính của chúng ta — Chiến thần ăn chay — đã lập tức ngồi bật dậy vào vị trí làm việc quen thuộc.". Bố cục: Chiếc đồng hồ báo thức khổng lồ rung bần bật chuông reo inh ỏi; chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay bật dậy ôm chân ngồi vào vị trí bệt quen thuộc, mắt còn dính gỉ ngủ ngơ ngác.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không tập thể dục, không đánh răng, công việc đầu tiên và duy nhất trong ngày của gã béo này là...". Bố cục: Chia đôi khung hình: BÊN TRÁI người tập thể hình hoạt hình chạy bộ mồ hôi nhễ nhại bị gạch chéo đỏ; BÊN PHẢI chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay ngồi bệt bụng mỡ rung rinh lười biếng tận hưởng.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bốc một thanh tre cho thẳng vào mồm nhai rôm rốp!". Bố cục: Cận cảnh chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay bốc cành tre to tướng cho thẳng vào mồm nhai rôm rốp; dăm tre và lá tre xanh bắn tung tóe quanh mép, mặt khoan khoái ngập tràn hạnh phúc.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Alo trường quay nghe rõ không? Phóng viên cho hỏi gã này định nhai tre đến bao giờ thế?". Bố cục: Trường quay tin tức hiện đại: cô phát thanh viên tin tức hoạt hình xinh đẹp ngồi sau bàn trường quay tin tức thời sự ngồi sau bàn phát thanh viên đeo tai nghe, tay cầm bút chỉ vào màn hình hiện trường ngạc nhiên hỏi phóng viên.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo trường quay, gã này sẽ ngồi nhai liên tục từ mười đến 14 tiếng mỗi ngày, không ngừng nghỉ!". Bố cục: Biểu đồ đồng hồ 24h: dải màu xanh lá kéo dài từ 10 tiếng đến 14 tiếng có hình cành tre nhai liên tục; chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay ngồi nhai tre bên cạnh chiếc đồng hồ.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Điều nghịch lý đến phát điên là: xét về mặt sinh học và phả hệ tiến hóa 19 triệu năm, Gấu Trúc thuộc bộ thú ăn thịt chính hiệu, cùng một tổ tiên với gấu xám, sư tử và chó sói!". Bố cục: Cây phả hệ tiến hóa 19 triệu năm: nhánh trên là sư tử oai vệ, gấu xám hung tợn và chó sói đang gầm gừ; nhánh dưới rẽ nhánh là chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay đang ngồi nhai lá tre hiền khô.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hộp sọ của nó có cơ hàm cực khỏe, răng nanh sắc nhọn và đường ruột ngắn cũn cỡn chuyên dùng để tiêu hóa thịt tươi béo ngậy. Nhưng không hiểu vì một pha bẻ lái lịch sử nào của tạo hóa,". Bố cục: Sơ đồ giải phẫu X-quang: hộp sọ có hàm răng nanh sắc nhọn và đường ruột ngắn cũn cỡn màu đỏ đặc trưng của thú ăn thịt; KHÔNG có chú Gấu Trúc trong cảnh này.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "khoảng 2 triệu năm trước, tổ tiên của nó bỗng nhiên...". Bố cục: Cỗ máy thời gian quay ngược 2 triệu năm trước: gấu tổ tiên quay ngoắt 180 độ quay lưng từ chối đùi thịt nướng bốc khói, chạy sang ôm chặt bụi tre xanh.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "mất đi cảm nhận vị umami của thịt, chán ăn thịt chuyển hẳn sang ăn chay 99% bằng lá tre và thân tre!". Bố cục: chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay ngồi lọt thỏm giữa núi tre trúc xanh mướt cao ngất, cười toe toét ngắt từng phiến lá tre nhét đầy mồm.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học phát hiện đột biến trên gen Tas1r1 đã biến chiếc lưỡi sành ăn thịt của tổ tiên nó thành kẻ mù vị giác với món bít-tết!". Bố cục: Mô hình chuỗi xoắn ADN phát sáng: đoạn gen Tas1r1 bị đứt gãy tia sét đỏ; bên cạnh là chiếc lưỡi gấu trúc có dấu gạch chéo đỏ trên đĩa thịt bò bít-tết.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đối với Chiến thần ăn chay, một tảng thịt bò thơm phức béo ngậy bây giờ cũng nhạt toẹt và vô vị y hệt một miếng bìa các-tông ngâm nước! Thà rằng ngồi gặm cành tre tươi đẫm sương sớm còn cảm thấy thanh tao và hợp khẩu vị hơn gấp vạn lần!". Bố cục: Bàn ăn đối chiếu bi hài: BÊN TRÁI đĩa thịt bò bít-tết hảo hạng thơm phức bị chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay đẩy phũ phàng ra xa chê nhạt như bìa các-tông; BÊN PHẢI cành tre tươi được ôm chặt vào lòng.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy cùng chúng tôi đếm ngược từng mốc giờ để xem cỗ máy ăn chay này vận hành kỳ dị ra sao!". Bố cục: anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H, đeo ba lô tác nghiệp giơ ngón tay ra hiệu đếm ngược, phía sau là chiếc đồng hồ cát đang chảy và kim đồng hồ 24h quay tít mù báo hiệu hành trình kỳ thú.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đồng hồ điểm 10:00 trưa! Cập nhật mới nhất từ hiện trường: sau 4 tiếng nhai tre không ngừng nghỉ, Chiến thần ăn chay đã xử lý gọn gàng hơn 10kg cành tre cứng như gỗ lim!". Bố cục: Đồng hồ hiện số 10:00 trưa; chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay ngồi lọt thỏm giữa đống vỏ tre đã bị tước bỏ chất cao như núi nhỏ, tay vẫn thoăn thoắt bóc cành tre mới.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quý vị có bao giờ thắc mắc tại sao một con gấu to béo vụng về lại có thể cầm nắm từng nhánh tre thanh thoát, bóc lớp vỏ cứng một cách điệu nghệ chẳng khác nào một đầu bếp chuyên nghiệp bóc vỏ mía không?". Bố cục: Cận cảnh bàn tay chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay bóc vỏ cành tre điệu nghệ như nghệ nhân gọt mía; bên cạnh là một người đầu bếp chuyên nghiệp đội mũ trắng kinh ngạc há hốc mồm học hỏi.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Camera góc siêu cận của chúng tôi vừa ghi lại một bí mật giải phẫu kinh ngạc: bàn tay trước của Gấu Trúc không phải có năm ngón như các loài gấu khác, mà sở hữu tới 6 ngón tay!". Bố cục: Bàn tay trước của Gấu Trúc xòe rộng dưới ống kính phóng đại: đếm rõ 5 ngón móng vuốt nhọn hoắt và ngón thứ 6 nhô ra bên cạnh ngón cái.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Này phóng viên ơi, làm gì có loài thú nào mọc 6 ngón tay thật, chắc chắn là đạo cụ gắn thêm rồi!". Bố cục: ông cụ nhân chứng râu tóc bạc phơ chống gậy trúc chống gậy trúc bước vào khung hình, nheo mắt chỉ tay vào bàn tay gấu trúc vẻ mặt nghi ngờ bảo đạo cụ giả.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bác nhân chứng nói gần đúng rồi đấy!". Bố cục: anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H, đeo ba lô tác nghiệp cầm bảng sơ đồ giải phẫu gật đầu giải thích thân thiện; chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay ngồi bên cạnh giơ bàn tay xòe 6 ngón vẫy chào vui vẻ.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trên thực tế, ngón tay cái phụ này không phải là một ngón tay thật, mà là xương vừng cổ tay phình to dị thường, bọc một lớp đệm thịt dày cộp bên ngoài. Tiến hóa đã biến chiếc xương cổ tay này thành một ngón tay cái giả hoạt động linh hoạt đối diện với năm ngón còn lại,". Bố cục: Bản vẽ X-quang xương bàn tay: xương vừng cổ tay (radial sesamoid) phình to dài ra bọc đệm thịt dẻo dai thành ngón cái giả linh hoạt; KHÔNG có chú Gấu Trúc trong cảnh này.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "giúp nó kẹp chặt từng thân tre tròn lẳn và tước bỏ lớp vỏ đắng ngắt một cách chuẩn xác từng mi-li-mét!". Bố cục: Hình minh họa kỹ thuật cơ khí: ngón cái giả kẹp đối diện 5 ngón kia như gọng kìm thợ máy, tước phăng dải vỏ tre đắng ngắt chuẩn xác từng milimet.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa dừng lại ở bàn tay khéo léo, hãy nhìn vào khuôn mặt tròn xoe phúng phính đáng yêu như chiếc bánh bao của nó! Quý vị đừng để vẻ dễ thương đánh lừa:". Bố cục: Cận cảnh khuôn mặt bánh bao tròn xoe của chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay: má phồng to phúng phính, hai mắt khoanh đen chớp chớp ngây thơ đáng yêu.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hai bên má phúng phính thực chất là hai khối cơ cắn khổng lồ neo thẳng lên gờ đỉnh sọ! Lực cắn của Chiến thần ăn chay mạnh tới mức chỉ đứng sau loài linh cẩu đốm nghiền xương, đủ sức bẻ vụn thân tre già dày cộp như nhai bim bim!". Bố cục: Sơ đồ cơ giải phẫu đầu gấu: hai búi cơ cắn khổng lồ màu đỏ kéo từ xương hàm dưới neo thẳng lên đỉnh sọ gấu trúc; lực cắn cực mạnh nghiền nát thân tre cứng.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn bộ niêm mạc vòm họng và thực quản của nó còn được lót một lớp màng nhầy siêu dày để các dằm tre sắc nhọn không thể đâm thủng nội tạng khi nuốt!". Bố cục: Mặt cắt phóng đại ống thực quản: lớp màng nhầy dày cộp tráng men bảo vệ, các mảnh dằm tre nhọn hoắt trượt tuột xuống dạ dày mà không gây xước xát; KHÔNG có chú Gấu Trúc trong cảnh này.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vũ khí của mãnh thú săn mồi thượng thừa, nhưng dùng vào việc nhai cỏ cây!". Bố cục: Hình ảnh hài hước: chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay mặc giáp chiến binh hầm hố cơ bắp cuồn cuộn như đấu sĩ La Mã, nhưng tay lại cầm nhánh tre ngồi nhai thảnh thơi.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bây giờ là 14:00 chiều! Chúng tôi vừa phải lùi xa hiện trường mười bước vì một kỷ lục sinh học vô tiền khoáng hậu sắp diễn ra.". Bố cục: Đồng hồ chỉ 14:00 chiều; anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H, đeo ba lô tác nghiệp đeo khẩu trang bảo hộ lùi lại phía sau vài bước, tay cầm thước dây đo khoảng cách an toàn.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quý vị hãy giữ chặt mũ: mỗi ngày, một chú Gấu Trúc trưởng thành phải nạp từ 12kg đến 38kg tre tươi.". Bố cục: chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay ngồi trước một xe cút kít chở đầy 38kg tre tươi xanh mướt; bụng chú phình to tròn xoe như quả bóng bay.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng vì mang ruột thú ăn thịt ngắn ngủn, không có bốn ngăn dạ dày như trâu bò, cũng chẳng có vi khuẩn lên men phân giải chất xơ như loài ngựa, hệ tiêu hóa của nó chỉ hấp thụ vỏn vẹn đúng 17% chất dinh dưỡng!". Bố cục: Sơ đồ đối chiếu hệ tiêu hóa: BÊN TRÁI ruột trâu bò 4 ngăn dài 40m tiêu hóa 80%; BÊN PHẢI ruột Gấu Trúc ngắn ngủn thẳng tuột chỉ tiêu hóa được 17%.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tới 83% lượng tre nuốt vào bụng sẽ trôi tuột ra ngoài nguyên vẹn hình sợi chỉ sau 2 tiếng đồng hồ! Và hệ quả tất yếu là gì?". Bố cục: Ống tiêu hóa như máng trượt nước siêu tốc: thân tre đi vào miệng và trượt tuột ra ngoài thành các sợi tre nguyên vẹn chỉ trong 2 tiếng đồng hồ.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Xin thông báo một con số kỷ lục: Chiến thần ăn chay phải đi vệ sinh tới 40 lần mỗi ngày! Đúng vậy, quý vị không hề nghe nhầm đâu, 40 lần một ngày,". Bố cục: Bảng đếm kỷ lục số điện tử nhảy số liên tục: con số 40 nhấp nháy phát sáng rực rỡ; chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay ngồi trên bô vệ sinh hoạt hình đọc báo tỉnh queo.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thải ra từ 20kg đến 25kg phân tre tươi!". Bố cục: Một chiếc cân tải trọng lớn chất đầy các viên phân tre màu xanh lá nặng 25kg; chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay đứng cạnh giơ hai ngón tay chiến thắng chữ V.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vừa ngồi nhai cành tre đằng trước, đằng sau đã xả ra đống bã tre thơm mùi cỏ non.". Bố cục: Cảnh bi hài: miệng phía trước chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay nhai tre nhồm nhoàm, phía sau đùn ra từng nắm phân tre cuộn tròn sạch sẽ.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà sinh vật học khi vào rừng chỉ cần đếm số lượng bãi thải là biết ngay gã béo này đã ngồi ở gốc cây đó bao nhiêu phút.". Bố cục: Nhà khoa học hoạt hình đeo kính lúp đi trong rừng tre, vừa đếm từng bãi phân tre vừa bấm đồng hồ bấm giờ tính thời gian gấu ngồi ở gốc cây.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây chính xác là một cỗ máy nghiền tre di động: năng suất nghiền cực cao, tiêu hóa cực kém, và xả thải liên tục 24/7! Điều bi hài nhất là phân của nó sạch đến mức người ta không thể nhịn cười!". Bố cục: Biểu tượng cỗ máy nghiền tre chạy bằng xích: đầu vào là tre cây, đầu ra là các cuộn bã xơ tre đóng gói liên tục 24/7.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vì 99% thức ăn là tre trúc và thời gian lưu trong ruột quá ngắn, phân gấu trúc hầu như không có mùi hôi thối mà thơm dịu mùi lá tre lên men thoang thoảng như trà xanh!". Bố cục: Cận cảnh viên phân tre: xơ lá tre xanh ép chặt thơm ngát, tỏa ra các làn khói hương thảo mộc và lá trà xanh thoang thoảng; đàn bướm bay lượn xung quanh.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tại Tứ Xuyên, người ta đã tận dụng loại phân giàu chất xơ này để tẩy sạch làm giấy thủ công mỹ nghệ cao cấp, thậm chí dùng bã phân ủ trà xanh bán với giá hàng ngàn đô-la một cân!". Bố cục: Xưởng thủ công mỹ nghệ: người thợ đang ép bã phân tre làm các tờ giấy mỹ thuật vàng nhạt cao cấp; bên cạnh là hộp trà phân gấu trúc gắn thẻ giá đô-la đắt đỏ.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ai mà ngờ chất thải của kẻ ăn chay lười biếng lại biến thành mỏ vàng sinh thái độc lạ bậc nhất thế giới!". Bố cục: chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay ngồi trên ngai vàng làm bằng búp măng tre, hai tay ôm các thỏi vàng sinh thái cười khoái chí tột độ.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ánh hoàng hôn buông xuống rừng tre, đồng hồ điểm 18:00 tối! Sau một ca làm việc cật lực ăn uống và xả thải, Chiến thần ăn chay quyết định leo lên ngọn cây cao để nghỉ ngơi thư giãn. Và đây chính là khoảnh khắc chương trình biểu diễn xiếc hài hước nhất tự nhiên bắt đầu!". Bố cục: Rừng tre chuyển sang màu hoàng hôn cam đỏ rực rỡ, đồng hồ chỉ 18:00 tối; chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay lạch bạch trèo lên một cây tre cao vút tìm chỗ ngủ.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quý vị hãy nhìn lên chạc cây: thân hình tròn xoe nặng hơn một tạ của nó đang vắt vẻo trên một cành cây nhỏ chỉ to bằng cổ tay.". Bố cục: Cành cây nhỏ cong oằn mình dưới sức nặng hơn một tạ của chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay; chú vắt vẻo ngủ say sưa bất chấp độ cao.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó ngủ trong những tư thế không tưởng: đầu chúc xuống đất, bốn chân buông thõng đung đưa, hoặc nằm ngửa bụng phơi nắng như một bao tải gạo bị bỏ quên trên ngọn cây!". Bố cục: Ghép 3 tư thế ngủ quái đản của chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay: đầu chúc xuống đất như con dơi, nằm ngửa bụng chân gác lên trời, và vắt ngang chạc cây như bao tải gạo.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ối ối bác phóng viên ơi, cành cây gãy rồi kìa, đỡ cháu với!". Bố cục: chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay tỉnh giấc thấy cành cây uốn cong kêu rắc rắc, mặt hoảng hốt chới với kêu cứu anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H, đeo ba lô tác nghiệp đang đứng quay phim bên dưới.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Rắc! Bịch! Một pha tiếp đất đỉnh cao không thể đỡ nổi! Cành cây gãy đôi và Chiến thần ăn chay rơi tự do từ độ cao vài mét đập mông xuống đất. Nhưng quý vị đừng lo lắng!". Bố cục: Cành cây gãy đôi kêu rắc, chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay rơi tự do từ ngọn cây xuống đất, mặt méo xệch hài hước giơ 4 chân lên trời.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ có lớp mỡ dày, bộ lông rậm rạp và khung xương sườn tròn đàn hồi cực tốt, nó lập tức cuộn tròn lăn lông lốc vài vòng như quả bóng bowling rồi ngồi dậy gãi tai tỉnh queo!". Bố cục: chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay tiếp đất cuộn tròn tròn xoe lăn lông lốc như quả bóng bowling đâm ngã mấy khúc gỗ mục, rồi bật dậy gãi tai cười toe toét tỉnh bơ.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngay cả bộ lông hai màu đen trắng của nó cũng là một tuyệt tác ngụy trang! Mảng lông trắng giúp nó ẩn mình hoàn hảo giữa các vách đá đóng tuyết mùa đông, còn các khoanh lông đen quanh mắt, tai và bốn chân giúp nó hòa tan vào bóng râm rậm rạp của rừng trúc mùa hè!". Bố cục: Phân tích trang phục ngụy trang: nửa trái nền tuyết trắng xóa chú hòa vào tuyết; nửa phải bụi râm tối chú hòa vào bóng râm rừng cây.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đốm đen quanh mắt to như cặp kính râm còn giúp làm giảm độ chói lóa của ánh nắng mặt trời phản chiếu từ tuyết trắng!". Bố cục: Cận cảnh đôi mắt chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay: hai khoanh đen quanh mắt như cặp kính râm thời trang giúp chống chói lóa ánh nắng phản chiếu từ tuyết trắng.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiếc đuôi ngắn ngủn 15cm ép sát mông hoạt động như một chiếc chổi quét bụi, giữ cho bàn tọa của gã béo luôn khô ráo ấm áp khi ngồi bệt xuống đất lạnh!". Bố cục: Phía sau mông chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay: chiếc đuôi cụt 15cm hoạt động như chiếc chổi phủi sạch tuyết ướt trên chạc cây trước khi ngồi bệt xuống.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngã cây như cơm bữa, lăn lộn như nghệ sĩ xiếc, nhưng tạo hóa đã bọc giáp từ đầu đến đuôi!". Bố cục: chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay đứng dang hai tay chào như vận động viên xiếc vừa hoàn thành bài biểu diễn tiếp đất hoàn hảo, khán giả vỗ tay rào rào khen ngợi.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Màn đêm bao trùm rừng thẳm, đồng hồ điểm 22:00 đêm! Không khí tĩnh mịch bỗng bị khuấy động bởi những âm thanh bí ẩn.". Bố cục: Rừng tre đêm tĩnh mịch ánh trăng le lói, đồng hồ chỉ 22:00 đêm; anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H, đeo ba lô tác nghiệp cầm đèn pin soi vào lối mòn trong rừng bí ẩn.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chúng tôi xin chuyển sang bản tin thời sự đặc biệt về sự tồn vong của loài: cuộc đua sinh sản nghẹt thở nhất hành tinh! Quý vị có biết tại sao Gấu Trúc lại từng đứng trước bờ vực tuyệt chủng không? Không chỉ vì phá hủy rừng tre, mà chính tạo hóa đã cài đặt cho chúng một chiếc đồng hồ sinh học cực kỳ khắt khe:". Bố cục: Bảng tin thời sự khẩn: biểu đồ đếm ngược nhấp nháy dòng chữ báo động đỏ về mùa sinh sản của Gấu Trúc.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "mỗi năm, con cái chỉ có đúng một chu kỳ rụng trứng duy nhất, và cánh cửa màu mỡ để giao phối chỉ mở ra vỏn vẹn từ 24-72 giờ đồng hồ!". Bố cục: Tờ lịch 365 ngày rơi rụng, chỉ còn lại đúng một tờ giấy nhỏ khoanh tròn đỏ với chiếc đồng hồ đếm ngược 24 đến 72 giờ thụ thai duy nhất.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đúng thế thưa quý vị! Đúng 48 tiếng ngắn ngủi trong suốt 365 ngày! Nếu trong hai ngày đó mà hai bên không tìm thấy nhau, hoặc chàng gấu mải ngồi nhai tre quên mất việc lớn, thì coi như mất trắng 1 năm!". Bố cục: Cảnh bi hài: chàng Gấu Trúc ngồi mải mê nhai tre ở góc trái; cô Gấu Trúc ngồi chờ đợi ở góc phải thở dài, đồng hồ cát chảy hết cát.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thậm chí các chuyên gia bảo tồn tại các trung tâm nhân giống từng phải mở cả video hướng dẫn giao phối cho chúng xem để học hỏi.". Bố cục: Trong trung tâm bảo tồn: chiếc tivi phát cảnh hai chú gấu trúc hẹn hò; bên dưới hai chú gấu trúc ngồi xem vừa cắn búp măng vừa ngơ ngác không hiểu gì.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và điều kỳ diệu nhất diễn ra sau đó: khi một chú Gấu Trúc con chào đời, nó chỉ nặng đúng 100g — tức là nhẹ bằng 1/900 trọng lượng của gấu mẹ!". Bố cục: Cận cảnh bàn tay to lớn của gấu mẹ: trong lòng bàn tay là chú gấu trúc sơ sinh bé tí hin màu hồng, không có lông, nhỏ thó như thỏi son môi.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa kể, các cô gấu trúc còn nổi tiếng với màn kịch mang thai giả tinh quái khiến cả đội ngũ bác sĩ thú y phải toát mồ hôi hột!". Bố cục: Phòng điều hòa VIP trong viện bảo tồn: một cô gấu trúc giả vờ nằm rên rỉ ốm nghén, được bác sĩ bưng đĩa táo đỏ và bánh bao ngọt phục vụ tận mồm.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cho đến khi siêu âm không thấy em bé đâu, các bác sĩ mới té ngửa nhận ra mình vừa bị một diễn viên kịch gấu lừa ngoạn mục!". Bố cục: Bác sĩ cầm máy siêu âm rà bụng gấu trúc, màn hình siêu âm chỉ toàn là lá tre và hơi gas, không có em bé; cô gấu trúc nháy mắt cười tinh quái.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bây giờ là 04:00 rạng sáng! Tiếng sương đêm nhỏ giọt trên những tán lá tre xào xạc, khép lại hành trình 24 giờ theo chân sinh vật đáng yêu nhất hành tinh.". Bố cục: Bầu trời rạng sáng 04:00 sương đọng trên lá tre lung linh; chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay ngồi bình thản ngắm bình minh trên đỉnh núi đá tĩnh lặng.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhiều người từng chế giễu Gấu Trúc là loài vật quyết tâm tự hủy, nhưng thực tế chứng minh điều ngược lại: Chiến thần ăn chay đã kiên cường vượt qua hơn 2 triệu năm biến đổi khí hậu khắc nghiệt, sống sót qua cả kỷ băng hà khi các loài mãnh thú to lớn khác đều đã tuyệt chủng!". Bố cục: Dòng thời gian 2 triệu năm: các loài hổ răng kiếm, voi ma-mút to xác ngã gục tuyệt chủng; riêng chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay vẫn ung dung ngồi gặm tre sống sót qua kỷ băng hà.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bằng cách hạ thấp nhu cầu năng lượng xuống mức tối thiểu, không tranh giành con mồi với ai, và biến sự vụng về thành nét đáng yêu khiến cả nhân loại phải chung tay bảo vệ, Gấu Trúc đã chọn cho mình một triết lý sinh tồn vô cùng độc đáo: chậm rãi, bình thản và hòa hợp tuyệt đối với thiên nhiên.". Bố cục: Triết lý sống an nhiên: chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay ngồi thiền trên tảng đá phẳng, biểu tượng thái cực và hoa sen tre tỏa sáng; chậm rãi, bình thản và yêu đời.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đồng hồ lại sắp điểm 06:00 sáng, và một chu kỳ nhai tre mới lại chuẩn bị bắt đầu!". Bố cục: Chiếc đồng hồ 24h quay trọn một vòng trở về vạch 06:00 sáng; chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay vươn vai ngáp một cái thật to rồi với tay lấy cành tre mới.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở tập tiếp theo, chúng ta sẽ tạm biệt rừng tre Trung Quốc để bay thẳng sang những dòng sông châu Phi rực lửa, nơi một cỗ xe tăng bọc thịt đang chờ đợi:". Bố cục: Bản đồ dịch chuyển từ rừng tre Trung Quốc sang dòng sông châu Phi rực lửa: một chú Hà Mã khổng lồ đang chạy bộ thình thịch dưới đáy sông nước cuồn cuộn.
```
</details>

<details><summary>L62</summary>

```text
HÌNH L62 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hà Mã! Tuyệt đối không biết bơi nhưng chạy bộ dưới đáy sông với lực cắn 1.800 PSI nghiền nát cá sấu! Hẹn gặp lại quý vị trong bản tin sinh tồn rực lửa tiếp theo!". Bố cục: Cận cảnh Hà Mã há ngoác mồm 150 độ lộ cặp răng nanh khủng khiếp cắn nát một khúc gỗ mục; lực cắn 1.800 PSI khủng khiếp.
```
</details>

<details><summary>L63</summary>

```text
HÌNH L63 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo trường quay, phóng viên xin phép ngắt sóng để đi ngủ một giấc như Gấu Trúc đây ạ!". Bố cục: anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H, đeo ba lô tác nghiệp tháo tai nghe, ngả lưng vào đống lá tre ngáy khò khò; màn hình TV hiển thị chữ 'TẠM BIỆT & HẸN GẶP LẠI'.
```
</details>

<details><summary>L64</summary>

```text
HÌNH L64 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kính chúc quý vị một ngày tràn đầy năng lượng tích cực! Còn bạn, bạn ấn tượng nhất với mốc thời gian nào trong 24 giờ của Chiến thần ăn chay? Hãy để lại bình luận bên dưới nhé!". Bố cục: chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay và anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H, đeo ba lô tác nghiệp cùng vẫy tay chào khán giả; các bóng bong bóng bình luận trái tim bay lên rực rỡ tươi vui.
```
</details>

<details><summary>L65</summary>

```text
HÌNH L65 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học phát hiện hành vi lăn lộn này không chỉ giúp chúng giảm chấn động khi ngã cây, mà còn là một bài tập xả stress tuyệt vời để làm sạch lớp lông dính bùn đất!". Bố cục: Các nhà khoa học mỉm cười gật gù ghi chép: hành vi lăn lộn giảm chấn và làm sạch lông dính bùn đất.
```
</details>

<details><summary>L66</summary>

```text
HÌNH L66 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhỏ thó bằng một thỏi son, đỏ hỏn, mù lòa và không có lấy một cọng lông! Sinh ra một cục bông tí hon mỏng manh giữa tự nhiên khắc nghiệt là một bài toán sinh tồn gian nan tột cùng!". Bố cục: Gấu trúc con đỏ hỏn mù lòa nằm lọt thỏm cạnh thỏi son môi và cục bơ nhỏ để so sánh kích thước tí hon kỳ lạ.
```
</details>

<details><summary>L67</summary>

```text
HÌNH L67 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi nhận thấy những con gấu mang thai được chuyển vào phòng máy lạnh, được phục vụ táo ngon và bánh bao hảo hạng, một số cô nàng tinh ranh đã cố tình bắt chước triệu chứng ốm nghén: đi lại chậm chạp, ăn ít, ngủ nhiều để được hưởng chế độ chăm sóc năm sao suốt mấy tháng trời!". Bố cục: Cô nàng gấu trúc tinh ranh giả vờ đi lại chậm chạp ốm nghén để được tận hưởng dịch vụ khách sạn 5 sao ăn ngon ngủ kỹ.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "6 giờ sáng ở rừng tre Tứ Xuyên, một con gấu mang bộ ruột của thú ăn thịt lại bắt đầu ca nhai tre kéo dài 14 tiếng!". Bố cục: Rừng tre dọc 9:16 lúc bình minh, đồng hồ báo thức chỉ 6 giờ: chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay to béo ngồi ôm đống cành tre to nhai rôm rốp; anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H, đeo ba lô tác nghiệp cầm micro đứng cạnh.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Nhưng ruột ngắn của thú ăn thịt chỉ hấp thụ được 17% dinh dưỡng,". Bố cục: Máng trượt tiêu hóa: cành tre đi vào miệng và trôi tuột ra ngoài trong 2 tiếng, chỉ giữ lại 17% dinh dưỡng ít ỏi.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Hậu quả là đi vệ sinh kỷ lục 40 lần một ngày!". Bố cục: Một bên xe cút kít chở 38kg tre, một bên đống phân tre 40 bãi chất cao ngất; chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay ngồi ở giữa vừa nhai vừa xả.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Để bóc vỏ tre, xương cổ tay của nó phình to thành ngón tay cái thứ 6, kẹp tre chắc như gọng kìm.". Bố cục: Cận cảnh bàn tay 6 ngón: ngón cái giả từ xương cổ tay kẹp chặt thân tre tước phăng vỏ như thợ bóc mía lành nghề.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "ngã xuống thì cuộn tròn lăn lông lốc rồi ăn tiếp.". Bố cục: chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay cuộn tròn lăn lông lốc như quả bóng bowling rồi bật dậy gãi tai nhai tre tỉnh queo như không có chuyện gì.
```
</details>

<details><summary>S12</summary>

```text
HÌNH S12 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "2 triệu năm trước, tổ tiên nó mất vị giác với thịt nên chuyển hẳn sang ăn tre 99%!". Bố cục: Gấu trúc vứt miếng thịt sang một bên ôm chặt lấy thân tre xanh mát ăn chay 99%.
```
</details>

<details><summary>S13</summary>

```text
HÌNH S13 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đó là Gấu Trúc Lớn, họ hàng của gấu xám, nặng cả tạ, chỉ sống ở vùng núi Trung Quốc.". Bố cục: Giới thiệu dọc: chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay đứng giữa vùng núi rừng tre Trung Quốc mờ sương; bên cạnh là một con gấu xám to lớn thân thiện như người họ hàng; một chiếc cân bàn dưới chân gấu trúc.
```
</details>

<details><summary>S14</summary>

```text
HÌNH S14 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "nên mỗi ngày nó phải nạp tới 38kg tre.". Bố cục: Dọc: chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay hì hục đẩy một chiếc xe cút kít chất đầy tre xanh cao ngất, mồ hôi nhễ nhại nhưng mặt vẫn hớn hở.
```
</details>

<details><summary>S15</summary>

```text
HÌNH S15 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Ăn ít năng lượng thì phải tiết kiệm: nó lười di chuyển, ngủ ngay trên cây,". Bố cục: Dọc: chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay nằm ngủ vắt vẻo trên chạc cây tre, phía trên đầu là biểu tượng cục pin yếu màu đỏ đang ở chế độ tiết kiệm năng lượng.
```
</details>

<details><summary>S16</summary>

```text
HÌNH S16 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "mà nó đang sống đúng chế độ tiết kiệm pin của một kẻ ăn chay mang ruột ăn thịt!". Bố cục: Dọc: chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay ngồi thư thái giữa rừng tre, ôm cành tre mỉm cười mãn nguyện; trên đầu là biểu tượng cục pin màu xanh lá đầy đủ với chiếc lá tre nhỏ (chế độ tiết kiệm pin); ánh nắng ấm áp.
```
</details>

<details><summary>S17</summary>

```text
HÌNH S17 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Gấu Trúc béo tròn đen trắng, mắt thâm quầng kính râm, đeo đồng hồ nhỏ trên tay; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Vậy là bí mật đã rõ: không phải gấu trúc lười,". Bố cục: Dọc: chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay ngồi giữa rừng tre, một tay gãi đầu ngượng ngùng, bên cạnh là dấu ngoặc kép to và biểu tượng chữ Zzz bị gạch chéo: không phải lười.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/66 của video YouTube về Gấu Trúc Lớn). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay. Nhân vật phụ cố định: anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H, đeo ba lô tác nghiệp; cô phát thanh viên tin tức hoạt hình xinh đẹp ngồi sau bàn trường quay tin tức thời sự; ông cụ nhân chứng râu tóc bạc phơ chống gậy trúc. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/11 của video YouTube Shorts về Gấu Trúc Lớn). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú gấu trúc Panda hoạt hình béo tròn mập mạp: bộ lông hai màu đen trắng tương phản rõ nét, hai mắt có khoanh tròn đen to xoe như đeo kính râm, hai tai đen tròn dựng đứng, thân hình tròn ủng mũm mĩm, biểu cảm ngơ ngác đáng yêu nhưng đôi lúc nhếch mép tinh nghịch, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ tay. Nhân vật phụ: anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H, đeo ba lô tác nghiệp. 
```
</details>

## 7. SEO

- **title:** Ruột Ăn Thịt Nhưng Ngồi Nhai Tre 14 Tiếng/Ngày?! | Gấu Trúc Lớn | Tập 11
- **hook_paragraph:** Gấu Trúc Lớn sở hữu bộ ruột của thú ăn thịt nhưng lại nhai tre 14 tiếng/ngày, chỉ hấp thụ 17% dinh dưỡng, đi vệ sinh 40 lần/ngày, bàn tay 6 ngón bóc vỏ tre và cửa sổ giao phối chỉ vỏn vẹn 24-72 giờ/năm! Khám phá nhật ký sinh tồn 24 giờ của Chiến thần ăn chay xứ Tứ Xuyên.
- **question:** Nếu được hoán đổi cuộc sống với Gấu Trúc 1 ngày: nhai tre 14 tiếng hay ngủ lăn lộn trên cây, bạn chọn cái nào? Bình luận bên dưới nhé!
- **next_teaser:** Hà Mã — cỗ xe tăng không biết bơi nhưng chạy bộ dưới đáy sông với lực cắn 1.800 PSI
- **shorts_title:** Ruột Ăn Thịt Nhưng Nhai Tre 14 Tiếng/Ngày?! 🐼 #shorts #gautruc
- **shorts_desc:** Gấu Trúc Lớn mang ruột thú ăn thịt nhưng ăn tre 99%: chỉ hấp thụ 17% dinh dưỡng nên phải nhai tre 14 tiếng/ngày, ăn 38kg tre và đi vệ sinh 40 lần/ngày. Ngón tay cái thứ 6 giúp nó bóc vỏ tre, còn lối sống chậm rãi chính là chế độ tiết kiệm năng lượng! 🐼🎋
- **bullets:** 06:00 Sáng: Mang ruột thú ăn thịt nhưng phản bội tổ tiên nhai tre 14 tiếng · 10:00 Trưa: Ngón tay cái giả thứ 6 biến dị từ xương cổ tay để bóc vỏ tre · 14:00 Chiều: Kỷ lục đi vệ sinh 40 lần/ngày, thải 25kg bã tre · 22:00 Đêm: Cửa sổ thụ thai duy nhất 24-72 giờ/năm và con non 100g như thỏi son
- **tags:** gấu trúc lớn, gau truc lon, giant panda, gấu trúc tứ xuyên, gấu trúc ăn tre, tiến hóa gấu trúc, ngón tay giả gấu trúc, thế giới động vật, động vật hài hước, vẽ chuyện hoang dã, whiteboard animation, khoa học thú vị, nhật ký 24 giờ
- **hashtags:** #GauTrucLon #GiantPanda #TheGioiDongVat #VeChuyenHoangDa #KhoaHoc

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-11-gau-truc-lon
python src/episode/pipeline.py tts    projects/tap-11-gau-truc-lon     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-11-gau-truc-lon     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-11-gau-truc-lon     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-11-gau-truc-lon              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-11-gau-truc-lon --force
python scripts/beat_sheet.py projects/tap-11-gau-truc-lon               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-11-gau-truc-lon/audio/shorts.wav projects/tap-11-gau-truc-lon/renders/tap-11-gau-truc-lon_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-11-gau-truc-lon
python src/episode/pipeline.py seo    projects/tap-11-gau-truc-lon
python src/episode/episode_doc.py     projects/tap-11-gau-truc-lon
```

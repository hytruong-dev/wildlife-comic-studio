# TẬP 14 — CHIM TU HÚ · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-14-chim-tu-hu`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-14-chim-tu-hu`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F3` · **Persona giọng:** `phien_toa` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Chim Tu Hú |
| Tiêu đề YouTube | Bản Năng Sát Thủ Của Chim Non Chưa Mở Mắt?! \| Chim Tu Hú \| Tập 14 |
| Video dài | `renders/tap-14-chim-tu-hu_long.mp4` — 9:23.1 (563.1s) |
| Shorts | `renders/tap-14-chim-tu-hu_shorts.mp4` — 0:52.5 (52.5s) |
| Thumbnail | `renders/tap-14-chim-tu-hu_thumbnail.jpg` |
| Số hình | dài 67 beat / 67 ảnh riêng; Shorts 13 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/67 của video YouTube về Chim Tu Hú). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú chim Tu Hú trưởng thành hoạt hình lông đốm hoa râm xám tro, mắt đỏ tròn tinh ranh, đeo chiếc nơ bướm màu tím than trên cổ, biểu cảm tự tin láu cá. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — BỊ CÁO SIÊU TRỘM 10 GIÂY
*Thẻ chương:* PHIÊN TÒA HÌNH SỰ XÉT XỬ CHIM TU HÚ

*Badge:* `VỤ ÁN TỔ ẤM` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene01_p0.wav` (270 ký tự) · mood `tram_bi_an`

```text
Tòa án tối cao thế giới tự nhiên! Cốc, cốc, cốc! Tiếng búa gõ vang dội giữa rừng già trong một buổi sáng đầy căng thẳng. Trên cành cây cổ thụ râm mát, một vụ án hình sự đặc biệt nghiêm trọng đang được đưa ra xét xử công khai trước sự chứng kiến của muôn loài chim muông!
```
**Part 1** → `audio/vs/scene01_p1.wav` (57 ký tự) · 🎭 cameo `tham_phan`

```text
Trật tự phiên tòa! Đề nghị công tố viên đọc to cáo trạng!
```
**Part 2** → `audio/vs/scene01_p2.wav` (361 ký tự) · mood `hao_hung`

```text
Kính thưa quý tòa và hội đồng bồi thẩm đoàn! Kẻ đang đứng trước vành móng ngựa hôm nay là một kẻ có hành tung thoắt ẩn thoắt hiện, sở hữu bộ lông hoa râm đốm xám và tiếng kêu tu hú vang vọng khắp các cánh đồng mỗi mùa vải chín! Vâng, đó chính là chim Tu Hú — loài chim được giang hồ thế giới tự nhiên đặt cho biệt danh khét tiếng: Siêu Trộm Tổ Ấm! [surprise-oh]
```
**Part 3** → `audio/vs/scene01_p3.wav` (299 ký tự) · mood `nghiem_trang_gia`

```text
Bị cáo trông bề ngoài thì có vẻ phong nhã, hiền lành, nhưng lật giở hồ sơ tiền án tiền sự của Siêu Trộm Tổ Ấm thì ai nấy đều phải rùng mình kinh hãi! Không xây tổ, không ấp trứng, không nuôi con, lười biếng đến mức tận cùng nhưng lại sở hữu những ngón nghề lừa đảo tinh vi bậc nhất lịch sử tiến hóa!
```
**Part 4** → `audio/vs/scene01_p4.wav` (487 ký tự) · mood `don_dap`

```text
Hôm nay, công tố viên tôi xin đại diện cho hàng vạn nạn nhân chim chích, chim sáo, chim chích chòe đệ trình lên tòa bốn bằng chứng không thể chối cãi: Đột nhập đẻ trộm trứng trong mười giây; Sát thủ sơ sinh mù mắt đẩy trứng chủ nhà rơi xuống đất; Thao túng tâm lý bắt cha mẹ nuôi bón mồi cho đứa con to gấp ba lần; Và chiến thuật mafia đập phá tổ để trả thù! Liệu một kẻ mang đầy tội trạng rợn người như thế này có xứng đáng nhận án phạt thích đáng? Kính mời bồi thẩm đoàn cùng theo dõi!
```

### scene02 — VỤ CƯỚP TRỨNG THẦN TỐC TRONG 10 GIÂY
*Thẻ chương:* ĐỘT NHẬP VÀ ĐẺ TRỘM TRỨNG THẦN TỐC

*Badge:* `BẰNG CHỨNG #1` · *mood mặc định:* `nghiem_trang_gia`

**Part 0** → `audio/vs/scene02_p0.wav` (333 ký tự) · mood `nghiem_trang_gia`

```text
Bằng chứng số một: Hành vi xâm nhập gia cư bất hợp pháp và đánh tráo tài sản với tốc độ kinh hoàng chỉ trong mười giây! Thông thường, một cô chim mái cần từ hai mươi phút đến nửa tiếng đồng hồ tĩnh tâm để đẻ xong một quả trứng. Nhưng với Siêu Trộm Tổ Ấm, việc sinh nở diễn ra nhanh như một tên trộm giật túi xách trên phố! [laughter]
```
**Part 1** → `audio/vs/scene02_p1.wav` (381 ký tự) · mood `don_dap`

```text
Để thực hiện phi vụ hoàn hảo, vợ chồng Tu Hú đã phối hợp tác chiến với kịch bản ăn ý đến từng mi-li-giây! Chim Tu Hú bố sở hữu bộ lông đen tuyền bóng bẩy sẽ bay lượn sát tổ của nạn nhân, phát ra những tiếng kêu khiêu khích chói tai làm chim chủ nhà nổi giận bay ra đuổi đánh. Và ngay khi chim chủ nhà vừa rời khỏi tổ, chim Tu Hú mẹ lập tức từ bụi cây lao vút xuống như một bóng ma!
```
**Part 2** → `audio/vs/scene02_p2.wav` (457 ký tự) · mood `hao_hung`

```text
Bấm đồng hồ: Một giây đáp xuống tổ! Hai giây cúi xuống dùng mỏ ngoạm lấy một quả trứng của chim chủ nhà nuốt chửng hoặc vứt văng ra ngoài! Ba giây ép sát bụng xuống đáy tổ và rặn đẻ đúng một quả trứng của mình thay vào vị trí đó! Năm giây tiếp theo: đập cánh bay biến vào tán lá rậm rạp! Toàn bộ vụ đột nhập đánh tráo diễn ra vỏn vẹn đúng mười giây đồng hồ, đến nỗi chiếc lá trên tổ còn chưa kịp ngừng rung rinh thì kẻ gian đã cao chạy xa bay! [surprise-wa]
```
**Part 3** → `audio/vs/scene02_p3.wav` (388 ký tự) · mood `am_ap`

```text
Nhưng tại sao chim chủ nhà khi quay về lại không phát hiện ra quả trứng lạ? Đây chính là đỉnh cao của công nghệ làm giả trong tự nhiên: trứng của Tu Hú có màu sắc, đốm hoa văn và kích thước giống trứng của chim chủ tới chín mươi chín phần trăm! Nếu gửi mẫu trứng này đi giám định ở phòng thí nghiệm hình sự, bảo đảm các chuyên gia cũng phải hoa mắt chóng mặt mới phân biệt nổi! [laughter]
```
**Part 4** → `audio/vs/scene02_p4.wav` (373 ký tự) · mood `hao_hung`

```text
Chưa dừng lại ở đó, vỏ trứng của Siêu Trộm Tổ Ấm còn tiến hóa dày hơn và cứng hơn trứng bình thường gấp hai lần! Để làm gì quý vị biết không? Một là để khi chim mẹ thả rơi vội vã từ trên cao xuống đáy tổ lót đá nó không bị nứt vỡ; và hai là nếu chim chủ nhà có sinh nghi dùng mỏ mổ thử, quả trứng Tu Hú vẫn trơ trơ như đá tảng khiến chim chủ đành bất lực chấp nhận ấp tiếp!
```

### scene03 — SÁT THỦ SƠ SINH VÀ CHIẾC LƯNG LÕM TỬ THẦN
*Thẻ chương:* BẢN NĂNG SÁT THỦ NGAY KHI VỪA NỞ

*Badge:* `BẰNG CHỨNG #2` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene03_p0.wav` (199 ký tự) · mood `tram_bi_an`

```text
Kính thưa quý tòa! Tội ác của chim mẹ mới chỉ là màn dạo đầu. Cáo trạng thứ hai mới thực sự là nỗi ám ảnh kinh hoàng nhất trong lịch sử sinh học: Tội ác của sát thủ sơ sinh chưa mở mắt! [surprise-oh]
```
**Part 1** → `audio/vs/scene03_p1.wav` (381 ký tự) · mood `nghiem_trang_gia`

```text
Trứng của Tu Hú luôn được thiên nhiên ban cho đặc quyền nở sớm hơn trứng của chim chủ nhà từ hai mươi tư giờ đến bốn mươi tám giờ. Lý do là vì phôi thai của Tu Hú đã bắt đầu phát triển ngay từ khi còn nằm trong ống dẫn trứng của chim mẹ! Khi chui ra khỏi vỏ, chú chim Tu Hú non chỉ nặng vỏn vẹn hai gam, trần trụi chẳng có cọng lông nào, mắt nhắm nghiền tịt mít như một hạt đậu đỏ!
```
**Part 2** → `audio/vs/scene03_p2.wav` (297 ký tự) · mood `don_dap`

```text
Nhưng đừng để vẻ ngoài yếu ớt ấy đánh lừa! Trên lưng của quái kiệt sơ sinh này có một vết lõm bẩm sinh hình chiếc thìa, tập trung hàng vạn đầu dây thần kinh cực kỳ nhạy cảm. Chỉ cần bất kỳ vật thể nào chạm nhẹ vào chiếc lưng lõm ấy, một công tắc sát thủ man rợ trong não bộ lập tức được kích hoạt!
```
**Part 3** → `audio/vs/scene03_p3.wav` (459 ký tự) · mood `don_dap`

```text
Chú chim non đỏ hỏn lùi dần từng bước về phía những quả trứng của chim chủ nhà. Nó dùng đôi cánh cụt ngủn quặp chặt lấy quả trứng, gồng hai chân non nớt quắp chặt vào thành tổ, rồi từ từ nâng quả trứng to bằng cả cơ thể mình lên trên lưng! Nó bước lùi từng xăng-ti-mét một, thở dốc vì kiệt sức, leo lên tận mép tổ rồi... Hất mạnh một cú dứt khoát! Quả trứng của chim chủ nhà rơi thẳng từ trên ngọn cây xuống đất, vỡ tan tành thành từng mảnh vụn! [surprise-wa]
```
**Part 4** → `audio/vs/scene03_p4.wav` (120 ký tự) · 🎭 cameo `be_con`

```text
Trời ơi! Con tôi! Trứng của tôi! Tôi đi kiếm mồi về thấy tổ trống trơn, chỉ còn mỗi cục thịt đỏ lòm này nằm thở phì phò!
```
**Part 5** → `audio/vs/scene03_p5.wav` (412 ký tự) · mood `hao_hung`

```text
Tiếng khóc xé lòng của nạn nhân chim chích chính là minh chứng đanh thép nhất! Quái vật sơ sinh ấy không chỉ hất một quả, mà nó lặp đi lặp lại hành động tàn nhẫn này suốt hai đến ba ngày đêm ròng rã, hất sạch toàn bộ trứng hoặc chim non của chủ nhà rơi xuống vực thẳm cho đến khi trong tổ chỉ còn lại duy nhất một mình nó độc chiếm ngai vàng! Quả là một bản năng sinh tồn lạnh lùng đến rợn tóc gáy! [surprise-oh]
```

### scene04 — THAO TÚNG TÂM LÝ VÀ ĐỨA CON TO GẤP 3 LẦN
*Thẻ chương:* THAO TÚNG BỐ MẸ NUÔI BẰNG SIÊU KÍCH THÍCH

*Badge:* `BẰNG CHỨNG #3` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene04_p0.wav` (196 ký tự) · mood `hao_hung`

```text
Sau khi đã thanh trừng sạch sẽ mọi đối thủ trong tổ, Siêu Trộm Tổ Ấm bước sang giai đoạn phạm tội thứ ba: Thao túng tâm lý đỉnh cao và bóc lột sức lao động của cha mẹ nuôi đến kiệt quệ! [laughter]
```
**Part 1** → `audio/vs/scene04_p1.wav` (396 ký tự) · mood `am_ap`

```text
Chỉ sau hai tuần được chăm bẵm độc quyền, chú Tu Hú non lớn nhanh như thổi, béo tròn núc ních và phổng phao gấp mười lần lúc mới sinh. Đến tuần thứ ba, nó to gấp ba lần, thậm chí gấp bốn lần thân hình còi cọc của đôi chim bố mẹ nuôi! Đứng trong chiếc tổ nhỏ xíu, thân hình hộ pháp của nó làm chiếc tổ muốn gãy làm đôi, còn chim bố mẹ đứng cạnh trông chẳng khác nào hạt tiêu đứng cạnh quả dưa hấu!
```
**Part 2** → `audio/vs/scene04_p2.wav` (107 ký tự) · 🎭 cameo `ga_khong_lo`

```text
Tôi phản đối! Tôi lớn con là do gen di truyền, chứ tôi đâu có ép bố mẹ nuôi phải đi bắt sâu cho tôi ăn đâu!
```
**Part 3** → `audio/vs/scene04_p3.wav` (455 ký tự) · mood `don_dap`

```text
Bị cáo cãi cùn rất trắng trợn! Nhưng khoa học đã lật tẩy mánh khóe ma quái của bị cáo! Các nhà sinh học thần kinh gọi đây là hiện tượng Siêu Kích Thích. Mỗi khi chim bố mẹ mang mồi về, Tu Hú non liền há toang chiếc miệng rộng ngoác màu đỏ tươi viền vàng rực rỡ như một cái hố ga không đáy! Vòm họng đỏ rực ấy phát ra tín hiệu thị giác mãnh liệt đến mức thôi miên não bộ của chim bố mẹ, khiến chúng không tài nào cưỡng lại được mệnh lệnh phải nhét mồi vào!
```
**Part 4** → `audio/vs/scene04_p4.wav` (550 ký tự) · mood `hao_hung`

```text
Chưa hết, tiếng kêu đòi ăn chíp chíp liên hồi của một con Tu Hú non có tần số rung động tương đương với tiếng kêu gào thảm thiết của cả một đàn bốn con chim non cộng lại! Chim bố mẹ nuôi bị tra tấn màng nhĩ, hoảng hốt bay đi lùng sục sâu bọ suốt mười bốn tiếng mỗi ngày, bay hàng trăm chuyến từ sáng sớm tới tối mịt chỉ để lấp đầy cái dạ dày không đáy của đứa con nuôi trời đánh! Thậm chí chim mẹ nhỏ xíu phải đậu hẳn lên đầu, lên lưng của con Tu Hú khổng lồ để với tới cái mỏ há to của nó, tạo nên một cảnh tượng bi hài bậc nhất trần đời! [laughter]
```

### scene05 — CHIẾN THUẬT MAFIA TRẢ THÙ TÀN ĐỘC
*Thẻ chương:* BẢO KÊ TỐNG TIỀN VÀ ĐẬP PHÁ TRẢ THÙ

*Badge:* `BẰNG CHỨNG #4` · *mood mặc định:* `nghiem_trang_gia`

**Part 0** → `audio/vs/scene05_p0.wav` (395 ký tự) · mood `nghiem_trang_gia`

```text
Đến đây, chắc hẳn quý vị trong bồi thẩm đoàn sẽ đặt câu hỏi: Chẳng lẽ loài chim chủ nhà ngốc nghếch đến mức không bao giờ nhận ra đứa con quái vật này sao? Câu trả lời là: Có! Nhiều loài chim chủ có đôi mắt tinh tường đã phát hiện ra quả trứng lạ và dùng mỏ hất quả trứng Tu Hú ra khỏi tổ! Nhưng quý vị có biết hậu quả sau đó là gì không? Đó chính là Cáo trạng thứ tư: Chiến thuật mafia tàn độc!
```
**Part 1** → `audio/vs/scene05_p1.wav` (321 ký tự) · mood `tram_bi_an`

```text
Năm hai ngàn lẻ bảy, hai nhà khoa học Hu-vơ và Rô-bin-xơn đã công bố một nghiên cứu chấn động trên tạp chí khoa học danh tiếng PNAS. Hóa ra, sau khi đẻ trộm trứng vào tổ người khác, chim Tu Hú mẹ không hề bỏ đi xa mà luôn lén lút nấp ở cành cây gần đó để theo dõi diễn biến, y hệt một tên trùm mafia đang giám sát đàn em!
```
**Part 2** → `audio/vs/scene05_p2.wav` (373 ký tự) · mood `don_dap`

```text
Nếu chim chủ nhà ngoan ngoãn ấp trứng Tu Hú, tổ của chúng sẽ hoàn toàn bình yên vô sự. Nhưng nếu phát hiện quả trứng của mình bị vứt bỏ hoặc bị đục thủng, chim Tu Hú mẹ sẽ lập tức dẫn theo đồng bọn lao tới tấn công điên cuồng! Nó mổ nát toàn bộ số trứng còn lại của chim chủ nhà, cắn chết những con chim non vừa nở và giật sập tan tành cả chiếc tổ để dằn mặt! [surprise-wa]
```
**Part 3** → `audio/vs/scene05_p3.wav` (500 ký tự) · mood `hao_hung`

```text
Các số liệu nghiên cứu đã chỉ ra: những chiếc tổ dám vứt bỏ trứng ký sinh có tỷ lệ bị đập phá tan hoang lên tới hơn năm mươi sáu phần trăm, trong khi những chiếc tổ cam chịu ấp hộ chỉ bị quấy rầy dưới mười phần trăm! Đây chính là chiến thuật tống tiền bảo kê kinh điển: Mày nuôi con tao thì tổ mày còn, mày dám vứt con tao thì cả gia đình mày tuyệt diệt! Đối mặt với họng súng mafia tàn nhẫn như vậy, chim chủ nhà đành phải ngậm đắng nuốt cay nuôi giùm con kẻ thù để bảo toàn tính mạng! [surprise-oh]
```

### scene06 — PHÁN QUYẾT CỦA TỰ NHIÊN VÀ BÓNG ĐEN BÍ ẨN TẬP 15
*Thẻ chương:* LỜI BÀO CHỮA BẤT NGỜ VÀ PHÁN QUYẾT TỐI CAO

*Badge:* `PHÁN QUYẾT` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (215 ký tự) · mood `am_ap`

```text
Kính thưa quý tòa! Bốn cáo trạng vừa nêu tưởng chừng đã đóng đinh tội danh của Siêu Trộm Tổ Ấm. Nhưng ngay trước giờ tuyên án, luật sư bào chữa xin được đưa ra một góc nhìn hoàn toàn bất ngờ từ đại cục của tự nhiên!
```
**Part 1** → `audio/vs/scene06_p1.wav` (120 ký tự) · 🎭 cameo `ong_gia_ke`

```text
Xin các bác tòa nương tay! Bị cáo này ăn sâu róm độc giỏi lắm, mùa màng nhà tôi nhờ nó mà không bị sâu bọ cắn nát đấy ạ!
```
**Part 2** → `audio/vs/scene06_p2.wav` (435 ký tự) · mood `hao_hung`

```text
Lời làm chứng của bác nông dân hoàn toàn có cơ sở khoa học vững chắc! Trong thế giới loài chim, sâu róm độc có lông ngứa chứa đầy độc tố là món ăn cấm kỵ mà chín mươi chín phần trăm các loài chim khác đều phải tránh xa. Nhưng chim Tu Hú trưởng thành lại là khắc tinh số một của loài sâu độc này! Dạ dày của Tu Hú có một lớp niêm mạc đặc biệt có thể tự bong tróc để đào thải toàn bộ đống lông sâu độc ra ngoài mà không hề bị tổn thương!
```
**Part 3** → `audio/vs/scene06_p3.wav` (462 ký tự) · mood `am_ap`

```text
Chính vì được giải phóng hoàn toàn khỏi gánh nặng ấp trứng và mớm mồi, Tu Hú trưởng thành mới có thể dành trọn vẹn một trăm phần trăm thời gian bay khắp các cánh rừng để săn lùng sâu róm, dập tắt những đại dịch sâu hại bảo vệ thảm thực vật cho toàn bộ hệ sinh thái! Đồng thời, sự lừa đảo tinh vi của Tu Hú cũng chính là động lực thúc đẩy các loài chim chủ tiến hóa thị giác tinh tường hơn và bộ não nhạy bén hơn qua hàng triệu năm qua chạy đua vũ trang tiến hóa!
```
**Part 4** → `audio/vs/scene06_p4.wav` (109 ký tự) · 🎭 cameo `tham_phan`

```text
Tòa tuyên án: Bị cáo Chim Tu Hú không có tội! Đó là quy luật sinh tồn nghiệt ngã nhưng hoàn hảo của tự nhiên!
```
**Part 5** → `audio/vs/scene06_p5.wav` (265 ký tự) · mood `hao_hung`

```text
Vụ án thế kỷ của Siêu Trộm Tổ Ấm đã chính thức khép lại với phán quyết đầy tính nhân văn! Nhưng ngay lúc này, xin mời quý vị khán giả hãy hướng mắt lên màn hình lớn để chiêm ngưỡng BÓNG ĐEN BÍ ẨN của nhân vật sẽ xuất hiện trong Tập mười lăm tiếp theo! [surprise-oh]
```
**Part 6** → `audio/vs/scene06_p6.wav` (588 ký tự) · mood `don_dap`

```text
Xin gửi tới quý vị ba manh mối chấn động về nhân vật bí ẩn này: Thứ nhất, đây là vị Bộ trưởng Ngoại giao hòa bình nhất hành tinh, dù nằm giữa đàn cá sấu ăn thịt khổng lồ hay đàn trăn gấm Nam Mỹ thì vẫn thảnh thơi nằm ngửa bụng ngủ ngon lành mà chẳng có ai thèm tấn công! Thứ hai, đây là siêu quái kiệt gặm nhấm lớn nhất thế giới với cân nặng lên tới sáu mươi lăm ki-lô-gam, sở hữu tài bơi lặn cừ khôi và có thể nín thở dưới đáy sông suốt năm phút đồng hồ! Và thứ ba, một nghịch lý cực kỳ khó đỡ: thói quen ăn lại chính phân của mình vào mỗi buổi sáng sớm để hấp thu dinh dưỡng! [laughter]
```
**Part 7** → `audio/vs/scene06_p7.wav` (229 ký tự) · mood `hao_hung`

```text
Quý vị khán giả có nhận ra bóng đen bí ẩn mang phong thái ung dung tự tại này là ai không? Hãy để lại dự đoán của bạn ngay dưới phần bình luận nhé! Phóng viên phiên tòa xin chào tạm biệt và hẹn gặp lại quý vị trong tập tiếp theo!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Bị cáo, mời đứng lên! Một loài chim không bao giờ xây tổ, không ấp trứng, không nuôi con, nhưng lại sở hữu bản năng sát thủ ngay từ giây phút đầu tiên chui ra khỏi vỏ! Đó chính là Chim Tu Hú, kẻ lừa đảo khét tiếng bậc nhất thế giới tự nhiên. Chim mẹ chỉ mất đúng mười giây để đột nhập tổ chim chích, nuốt chửng một quả trứng của chủ nhà và đẻ thay vào đó quả trứng của mình với hoa văn giả mạo giống tới chín mươi chín phần trăm! [surprise-wa] Đáng sợ hơn cả, con non vừa nở chỉ nặng hai gam, mắt còn nhắm nghiền chưa mở, nhưng đã dùng chiếc lưng lõm bẩm sinh gồng mình hất tung toàn bộ trứng của chim chủ nhà rơi xuống đất vỡ nát! Để rồi sau đó, đứa con nuôi khổng lồ lớn nhanh như thổi, to gấp ba lần chim bố mẹ, há to chiếc miệng đỏ lòm như hố ga thôi miên cha mẹ nuôi phải hầu hạ mớm mồi suốt ngày đêm! [laughter] Vậy là vụ án đã sáng tỏ: một chiến thuật ký sinh tàn nhẫn nhưng là cách sinh tồn hoàn hảo giúp loài chim này trường tồn qua hàng triệu năm qua!
```

**Whisper prompt:** `Chim Tu Hú, biệt danh, tên riêng phiên âm, số liệu khó (giúp Whisper nghe đúng)`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| hai mươi xăng-ti-mét | 20cm |
| Ma-ri-a-na | Mariana |
| mười giây | 10 giây |
| mười lăm giây | 15 giây |
| hai mươi tư giờ | 24 giờ |
| bốn mươi tám giờ | 48 giờ |
| hai đến ba ngày | 2-3 ngày |
| hai mươi phút | 20 phút |
| nửa tiếng | 30 phút |
| ba đến bốn lần | 3-4 lần |
| gấp ba lần | gấp 3 lần |
| gấp bốn lần | gấp 4 lần |
| gấp hai lần | gấp 2 lần |
| gấp mười lần | gấp 10 lần |
| năm phút | 5 phút |
| mười bốn tiếng | 14 tiếng |
| chín mươi chín phần trăm | 99% |
| hai gam | 2g |
| sáu mươi lăm ki-lô-gam | 65kg |
| năm mươi sáu phần trăm | 56% |
| dưới mười phần trăm | dưới 10% |
| một trăm phần trăm | 100% |
| Hu-vơ | Hoover |
| Rô-bin-xơn | Robinson |
| P-N-A-S | PNAS |
| Bằng chứng số một | Bằng chứng số 1 |
| Bằng chứng số hai | Bằng chứng số 2 |
| Bằng chứng số ba | Bằng chứng số 3 |
| Bằng chứng số bốn | Bằng chứng số 4 |
| Cáo trạng thứ nhất | Cáo trạng thứ 1 |
| Cáo trạng thứ hai | Cáo trạng thứ 2 |
| Cáo trạng thứ ba | Cáo trạng thứ 3 |
| Cáo trạng thứ tư | Cáo trạng thứ 4 |
| Tập mười lăm | Tập 15 |
| Một giây | 1 giây |
| Hai giây | 2 giây |
| Ba giây | 3 giây |
| Năm giây | 5 giây |
| hai tuần | 2 tuần |
| thứ ba | thứ 3 |
| hai ngàn lẻ bảy | 2007 |
| hàng triệu năm qua | hàng triệu năm qua |
| hàng triệu năm | hàng triệu năm |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · BỊ CÁO SIÊU TRỘM 10 GIÂY · 72.1s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:03.0 (3.0s) | L01 | Tòa án tối cao thế giới tự nhiên! Cốc, cốc, cốc! |  | BÊN TRÁI chú cú mèo già thẩm phán đội tóc giả trắng tòa án Anh, mặc áo choàng đen, tay cầm búa gỗ đang nghiêm nghị gõ búa gỗ xuống bàn; Ở GIỮA tấm biển lớn đề chữ 'TÒA ÁN TỐI CAO THẾ GIỚI TỰ NHIÊN' treo giữa rừng già; BÊN PHẢI hàng loạt muôn loài chim muông đang ngồi trên các cành cây theo dõi hồi hộp. KHÔNG có chim Tu Hú trưởng thành trong cảnh này. |
| b02 | 00:03.0–00:06.2 (3.2s) | L02 | Tiếng búa gõ vang dội giữa rừng già trong một buổi sáng đầy căng thẳng. |  | Toàn cảnh góc rộng khu rừng rậm: ánh nắng sớm rọi qua kẽ lá, các loài chim chích, chim sáo, chim quạ tụ tập đông đúc quanh cành cây cổ thụ nghe ngóng xôn xao. KHÔNG có chim Tu Hú trưởng thành trong cảnh này. |
| b03 | 00:06.2–00:13.0 (6.8s) | L03 | Trên cành cây cổ thụ râm mát, một vụ án hình sự đặc biệt nghiêm trọng đang được đưa ra xét xử công khai trước sự chứng kiến của muôn loài chim muông! |  | Góc nhìn cận cảnh cành cây cổ thụ: một chiếc tổ chim nhỏ bị bỏ trống, bên cạnh là hồ sơ vụ án viền đỏ đóng dấu 'ÁP GIẢI TỘI PHẠM'. KHÔNG có chim Tu Hú trưởng thành trong cảnh này. |
| b04 | 00:13.0–00:16.7 (3.7s) | L04 | Trật tự phiên tòa! Đề nghị công tố viên đọc to cáo trạng! |  | BÊN TRÁI chú cú mèo già thẩm phán đội tóc giả trắng tòa án Anh, mặc áo choàng đen, tay cầm búa gỗ đứng nghiêm nghị giơ tay ra lệnh trật tự; Ở GIỮA bục công tố viên lót tài liệu; BÊN PHẢI cả hội đồng chim chóc im phăng phắc nín thở. KHÔNG có chim Tu Hú trưởng thành trong cảnh này. |
| b05 | 00:16.7–00:28.9 (12.2s) | L05 | Kính thưa quý tòa và hội đồng bồi thẩm đoàn! Kẻ đang đứng trước vành móng ngựa hôm nay là một kẻ có hành tung thoắt ẩn thoắt hiện, sở hữu bộ lông hoa râm đốm xám và tiếng kêu tu hú vang vọng khắp các cánh đồng mỗi mùa vải chín! |  | BÊN TRÁI công tố viên chỉ tay đanh thép về phía vành móng ngựa; BÊN PHẢI chú chim Tu Hú trưởng thành hoạt hình lông đốm hoa râm xám tro, mắt đỏ tròn tinh ranh, đeo chiếc nơ bướm màu tím than trên cổ, biểu cảm tự tin láu cá đang đứng ung dung trong vành móng ngựa gỗ, mắt đỏ nhếch mép huýt sáo. |
| b06 | 00:28.9–00:35.6 (6.7s) | L06 | Vâng, đó chính là chim Tu Hú — loài chim được giang hồ thế giới tự nhiên đặt cho biệt danh khét tiếng: Siêu Trộm Tổ Ấm! |  | Cận cảnh chân dung chú chim Tu Hú trưởng thành hoạt hình lông đốm hoa râm xám tro, mắt đỏ tròn tinh ranh, đeo chiếc nơ bướm màu tím than trên cổ, biểu cảm tự tin láu cá: bộ lông đốm hoa râm xám tro, nơ tím than chỉnh tề, mỏ nhọn đang kêu 'Tu hú! Tu hú!' vang dội giữa những chùm quả vải chín đỏ mọng xung quanh. |
| b07 | 00:35.6–00:42.6 (7.0s) | L07 | Bị cáo trông bề ngoài thì có vẻ phong nhã, hiền lành, nhưng lật giở hồ sơ tiền án tiền sự của Siêu Trộm Tổ Ấm thì ai nấy đều phải rùng mình kinh hãi! | **LỪA ĐẢO** · TIỀN ÁN ĐẦY MÌNH · R/380 · [0.75, 0.45] | So sánh hai mặt đối lập: BÊN TRÁI chú chim Tu Hú trưởng thành hoạt hình lông đốm hoa râm xám tro, mắt đỏ tròn tinh ranh, đeo chiếc nơ bướm màu tím than trên cổ, biểu cảm tự tin láu cá trông lịch lãm như quý ông; BÊN PHẢI một cuốn sổ đen tiền án tiền sự dày cộm dán ảnh truy nã đề chữ 'SIÊU TRỘM TỔ ẤM'. |
| b08 | 00:42.6–00:49.5 (6.9s) | L08 | Không xây tổ, không ấp trứng, không nuôi con, lười biếng đến mức tận cùng nhưng lại sở hữu những ngón nghề lừa đảo tinh vi bậc nhất lịch sử tiến hóa! |  | Hình ảnh châm biếm: Ở GIỮA chú chim Tu Hú trưởng thành hoạt hình lông đốm hoa râm xám tro, mắt đỏ tròn tinh ranh, đeo chiếc nơ bướm màu tím than trên cổ, biểu cảm tự tin láu cá nằm đung đưa trên võng lá ngủ khò, một cánh gối đầu, một cánh phẩy quạt; xung quanh các loài chim khác đang hì hục tha rơm xây tổ toát mồ hôi. |
| b09 | 00:49.5–00:56.2 (6.7s) | L09 | Hôm nay, công tố viên tôi xin đại diện cho hàng vạn nạn nhân chim chích, chim sáo, chim chích chòe đệ trình lên tòa bốn bằng chứng không thể chối cãi: | **4 TỘI** · BẰNG CHỨNG THÉP · R/420 · [0.72, 0.5] | BÊN TRÁI hàng trăm chú chim chích, chim sáo nhỏ bé cầm biểu ngữ 'TRẢ LẠI CON CHO TÔI!'; BÊN PHẢI công tố viên mở tập tài liệu 4 cáo trạng hình sự phát sáng đỏ rực. KHÔNG có chim Tu Hú trưởng thành trong cảnh này. |
| b10 | 00:56.2–01:05.8 (9.6s) | L69 | Đột nhập đẻ trộm trứng trong 10 giây; Sát thủ sơ sinh mù mắt đẩy trứng chủ nhà rơi xuống đất; Thao túng tâm lý bắt cha mẹ nuôi bón mồi cho đứa con to gấp 3 lần; Và chiến thuật mafia đập phá tổ để trả thù! |  | Cận cảnh 4 tội danh được chiếu đèn pha đỏ: hình minh họa đẻ trộm 10 giây, hất vỡ trứng, con nuôi khổng lồ và đập phá tổ mafia dằn mặt. KHÔNG có chim Tu Hú trưởng thành trong cảnh này. |
| b11 | 01:05.8–01:12.1 (6.3s) | L10 | Liệu một kẻ mang đầy tội trạng rợn người như thế này có xứng đáng nhận án phạt thích đáng? Kính mời bồi thẩm đoàn cùng theo dõi! |  | BÊN TRÁI chú chim Tu Hú trưởng thành hoạt hình lông đốm hoa râm xám tro, mắt đỏ tròn tinh ranh, đeo chiếc nơ bướm màu tím than trên cổ, biểu cảm tự tin láu cá đứng trong bóng tối với nụ cười bí hiểm; BÊN PHẢI cán cân công lý bằng vàng rực rỡ đang nghiêng ngả trước hàng loạt bằng chứng tội trạng. |

### scene02 · VỤ CƯỚP TRỨNG THẦN TỐC TRONG 10 GIÂY · 95.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:05.8 (5.8s) | L11 | Bằng chứng số 1: Hành vi xâm nhập gia cư bất hợp pháp và đánh tráo tài sản với tốc độ kinh hoàng chỉ trong 10 giây! | **10 GIÂY** · ĐẺ TRỨNG KỶ LỤC · R/380 · [0.75, 0.45] | BÊN TRÁI tấm bảng lớn ghi chữ 'BẰNG CHỨNG SỐ 1: VỤ CƯỚP TRỨNG 10 GIÂY'; BÊN PHẢI một chiếc đồng hồ bấm giờ thể thao đang điểm số 00:10 nhấp nháy phát sáng. KHÔNG có chim Tu Hú trưởng thành trong cảnh này. |
| b02 | 00:05.8–00:15.7 (9.9s) | L12 | Thông thường, một cô chim mái cần từ 20 phút đến 30 phút đồng hồ tĩnh tâm để đẻ xong một quả trứng. Nhưng với Siêu Trộm Tổ Ấm, việc sinh nở diễn ra nhanh như một tên trộm giật túi xách trên phố! | **20-30 PHÚT** · CHIM BÌNH THƯỜNG · L/400 · [0.28, 0.5] | So sánh tốc độ sinh nở: BÊN TRÁI cô chim sẻ ngồi tĩnh tâm trên tổ với đồng hồ đếm ngược 20-30 phút; BÊN PHẢI một tên trộm bịt mặt chạy vút qua như tia chớp giật lấy quả trứng hài hước. KHÔNG có chim Tu Hú trưởng thành trong cảnh này. |
| b03 | 00:15.7–00:20.9 (5.2s) | L13 | Để thực hiện phi vụ hoàn hảo, vợ chồng Tu Hú đã phối hợp tác chiến với kịch bản ăn ý đến từng mi-li-giây! |  | Bản vẽ chiến thuật quân sự: sơ đồ tác chiến chia làm hai mũi tấn công; mũi tên đỏ chỉ hướng chim bố nghi binh dụ địch, mũi tên xanh chỉ hướng chim mẹ đột kích lén lút vào tổ chim chích. |
| b04 | 00:20.9–00:28.2 (7.3s) | L14 | Chim Tu Hú bố sở hữu bộ lông đen tuyền bóng bẩy sẽ bay lượn sát tổ của nạn nhân, phát ra những tiếng kêu khiêu khích chói tai làm chim chủ nhà nổi giận bay ra đuổi đánh. |  | BÊN TRÁI chim Tu Hú trống lông đen tuyền bay lượn khiêu khích nhổ lông trêu chọc; BÊN PHẢI đôi chim chủ nhà tức giận đỏ mặt xù lông bay ra khỏi tổ rượt đuổi quyết liệt. |
| b05 | 00:28.2–00:33.4 (5.2s) | L15 | Và ngay khi chim chủ nhà vừa rời khỏi tổ, chim Tu Hú mẹ lập tức từ bụi cây lao vút xuống như một bóng ma! |  | Cận cảnh tổ chim chích trơ trọi không ai canh giữ: từ cành cây rậm rạp phía trên, chim Tu Hú mẹ mắt đỏ lao thẳng xuống tổ nhanh như một mũi tên xé gió. |
| b06 | 00:33.4–00:35.9 (2.5s) | L16 | Bấm đồng hồ: 1 giây đáp xuống tổ! | **GIÂY THỨ 1** · ĐÁP XUỐNG TỔ · L/360 · [0.25, 0.42] | Mốc 1 giây: chim Tu Hú mẹ đáp nhẹ nhàng xuống mép tổ chim chích; một chiếc đồng hồ bấm giờ góc trái hiển thị con số 00:01. |
| b07 | 00:35.9–00:40.6 (4.6s) | L17 | 2 giây cúi xuống dùng mỏ ngoạm lấy một quả trứng của chim chủ nhà nuốt chửng hoặc vứt văng ra ngoài! | **GIÂY THỨ 2** · CƯỚP TRỨNG CHỦ · L/360 · [0.25, 0.42] | Mốc 2 giây: chim Tu Hú mẹ cúi mỏ ngoạm lấy một quả trứng của chim chủ nhà hất văng ra khỏi tổ rơi tự do; đồng hồ góc trái hiển thị 00:02. |
| b08 | 00:40.6–00:45.3 (4.7s) | L18 | 3 giây ép sát bụng xuống đáy tổ và rặn đẻ đúng một quả trứng của mình thay vào vị trí đó! | **GIÂY THỨ 3** · ĐẺ TRỨNG THAY THẾ · L/360 · [0.25, 0.42] | Mốc 3 giây: chim Tu Hú mẹ ép sát bụng xuống đáy tổ rặn đẻ quả trứng của mình thay vào đúng vị trí quả trứng vừa mất; đồng hồ hiển thị 00:03. |
| b09 | 00:45.3–00:57.3 (12.0s) | L19 | 5 giây tiếp theo: đập cánh bay biến vào tán lá rậm rạp! Toàn bộ vụ đột nhập đánh tráo diễn ra vỏn vẹn đúng 10 giây đồng hồ, đến nỗi chiếc lá trên tổ còn chưa kịp ngừng rung rinh thì kẻ gian đã cao chạy xa bay! | **10 GIÂY** · CHỚP NHOÁNG HOÀN TẤT · R/390 · [0.75, 0.48] | Mốc 5 giây tiếp theo: chim Tu Hú mẹ đập cánh bay vút đi để lại làn khói mờ ảo; chiếc lá trên mép tổ vẫn còn đung đưa chưa kịp đứng yên. |
| b10 | 00:57.3–01:01.0 (3.7s) | L20 | Nhưng tại sao chim chủ nhà khi quay về lại không phát hiện ra quả trứng lạ? |  | BÊN TRÁI đôi đôi chim chích nhỏ xíu màu nâu vàng ngơ ngác, biểu cảm hoảng hốt còng lưng bay về tổ đứng nhìn ngơ ngác gãi đầu; Ở GIỮA tổ chim có 4 quả trứng trông giống hệt nhau không một chút khác biệt. |
| b11 | 01:01.0–01:08.8 (7.8s) | L21 | Đây chính là đỉnh cao của công nghệ làm giả trong tự nhiên: trứng của Tu Hú có màu sắc, đốm hoa văn và kích thước giống trứng của chim chủ tới 99%! | **GIỐNG 99%** · NGỤY TRANG HOÀN HẢO · R/380 · [0.75, 0.45] | Cận cảnh phóng đại hai quả trứng đặt cạnh nhau: BÊN TRÁI trứng chim chích; BÊN PHẢI trứng chim Tu Hú; cả hai đều có vỏ màu xanh nhạt đốm nâu giống nhau 99%. |
| b12 | 01:08.8–01:16.3 (7.5s) | L60 | Nếu gửi mẫu trứng này đi giám định ở phòng thí nghiệm hình sự, bảo đảm các chuyên gia cũng phải hoa mắt chóng mặt mới phân biệt nổi! |  | Phòng giám định hình sự thế giới tự nhiên: một bác chim cú đeo kính lúp soi từng chấm đốm trên hai quả trứng, toát mồ hôi vì quá khó phân biệt. KHÔNG có chim Tu Hú trưởng thành trong cảnh này. |
| b13 | 01:16.3–01:24.1 (7.8s) | L22 | Chưa dừng lại ở đó, vỏ trứng của Siêu Trộm Tổ Ấm còn tiến hóa dày hơn và cứng hơn trứng bình thường gấp 2 lần! Để làm gì quý vị biết không? | **DÀY GẤP 2** · VỎ CỨNG NHƯ ĐÁ · R/420 · [0.7, 0.52] | Thí nghiệm đo độ cứng vỏ trứng: quả trứng Tu Hú được đặt dưới một chiếc búa nhỏ đập vào mà không vỡ, vỏ trứng dày gấp đôi vỏ trứng bình thường. KHÔNG có chim Tu Hú trưởng thành trong cảnh này. |
| b14 | 01:24.1–01:35.5 (11.4s) | L61 | Một là để khi chim mẹ thả rơi vội vã từ trên cao xuống đáy tổ lót đá nó không bị nứt vỡ; và hai là nếu chim chủ nhà có sinh nghi dùng mỏ mổ thử, quả trứng Tu Hú vẫn trơ trơ như đá tảng khiến chim chủ đành bất lực chấp nhận ấp tiếp! |  | Chim Tu Hú mẹ thả rơi quả trứng từ trên cao xuống đáy tổ lót đầy đá cuội mà quả trứng vẫn nguyên vẹn không sứt mẻ; chim chủ nhà mổ mỏ vào kêu 'cốp cốp' bất lực. KHÔNG có chim Tu Hú trưởng thành trong cảnh này. |

### scene03 · SÁT THỦ SƠ SINH VÀ CHIẾC LƯNG LÕM TỬ THẦN · 90.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.2 (9.2s) | L23 | Kính thưa quý tòa! Tội ác của chim mẹ mới chỉ là màn dạo đầu. Cáo trạng thứ 2 mới thực sự là nỗi ám ảnh kinh hoàng nhất trong lịch sử sinh học: Tội ác của sát thủ sơ sinh chưa mở mắt! |  | BÊN TRÁI tấm biển lớn đề 'BẰNG CHỨNG SỐ 2: SÁT THỦ CHƯA MỞ MẮT'; BÊN PHẢI hình bóng đen một chú chim non sơ sinh đỏ hỏn toát ra luồng khí lạnh lùng rợn người. KHÔNG có chim Tu Hú trưởng thành trong cảnh này. |
| b02 | 00:09.2–00:20.2 (11.0s) | L24 | Trứng của Tu Hú luôn được thiên nhiên ban cho đặc quyền nở sớm hơn trứng của chim chủ nhà từ 24 giờ đến 48 giờ. Lý do là vì phôi thai của Tu Hú đã bắt đầu phát triển ngay từ khi còn nằm trong ống dẫn trứng của chim mẹ! | **NỞ SỚM** · ĐẶC QUYỀN TIẾN HÓA · L/380 · [0.28, 0.45] | Sơ đồ thời gian ấp trứng: quả trứng Tu Hú nứt vỏ nở trước 24-48 giờ; bên cạnh là những quả trứng chim chủ nhà vẫn còn nằm im lìm chưa kịp cựa quậy. KHÔNG có chim Tu Hú trưởng thành trong cảnh này. |
| b03 | 00:20.2–00:29.9 (9.7s) | L25 | Khi chui ra khỏi vỏ, chú chim Tu Hú non chỉ nặng vỏn vẹn 2g, trần trụi chẳng có cọng lông nào, mắt nhắm nghiền tịt mít như một hạt đậu đỏ! Nhưng đừng để vẻ ngoài yếu ớt ấy đánh lừa! | **NẶNG 2G** · ĐỎ HỎN KHÔNG LÔNG · R/420 · [0.72, 0.5] | Cận cảnh chú chim Tu Hú non sơ sinh đỏ hỏn không một cọng lông, mắt nhắm nghiền, trên lưng có vết lõm rõ rệt hình chiếc thìa nằm trên một chiếc cân tiểu ly điện tử hiển thị con số vỏn vẹn 2g; cơ thể đỏ hỏn không cọng lông, mắt nhắm nghiền như hạt đỗ. |
| b04 | 00:29.9–00:41.5 (11.6s) | L26 | Trên lưng của quái kiệt sơ sinh này có một vết lõm bẩm sinh hình chiếc thìa, tập trung hàng vạn đầu dây thần kinh cực kỳ nhạy cảm. Chỉ cần bất kỳ vật thể nào chạm nhẹ vào chiếc lưng lõm ấy, một công tắc sát thủ man rợ trong não bộ lập tức được kích hoạt! | **LƯNG LÕM** · VŨ KHÍ BẨM SINH · R/390 · [0.7, 0.45] | Phóng to cận cảnh chiếc lưng của chú chim Tu Hú non sơ sinh đỏ hỏn không một cọng lông, mắt nhắm nghiền, trên lưng có vết lõm rõ rệt hình chiếc thìa: một vết lõm bẩm sinh hình chiếc thìa sâu hoắm, các dây thần kinh xung quanh phát sáng màu xanh neon nhạy cảm. |
| b05 | 00:41.5–00:52.2 (10.8s) | L27 | Chú chim non đỏ hỏn lùi dần từng bước về phía những quả trứng của chim chủ nhà. Nó dùng đôi cánh cụt ngủn quặp chặt lấy quả trứng, gồng hai chân non nớt quắp chặt vào thành tổ, rồi từ từ nâng quả trứng to bằng cả cơ thể mình lên trên lưng! |  | chú chim Tu Hú non sơ sinh đỏ hỏn không một cọng lông, mắt nhắm nghiền, trên lưng có vết lõm rõ rệt hình chiếc thìa lùi lũi đi lùi từng bước trong tổ, hai cánh cụt ngủn ôm ghì lấy một quả trứng chim chủ to bằng cả người nó, đặt quả trứng lọt thỏm vào chiếc lưng lõm. |
| b06 | 00:52.2–00:58.5 (6.2s) | L28 | Nó bước lùi từng xăng-ti-mét một, thở dốc vì kiệt sức, leo lên tận mép tổ rồi... Hất mạnh một cú dứt khoát! Quả trứng của chim |  | chú chim Tu Hú non sơ sinh đỏ hỏn không một cọng lông, mắt nhắm nghiền, trên lưng có vết lõm rõ rệt hình chiếc thìa dùng hai chân non nớt quắp chặt thành tổ, gồng mình đẩy quả trứng leo dần lên mép tổ; những giọt mồ hôi hoạt hình văng ra vì gắng sức. |
| b07 | 00:58.5–01:02.8 (4.3s) | L29 | chủ nhà rơi thẳng từ trên ngọn cây xuống đất, vỡ tan tành thành từng mảnh vụn! |  | Khoảnh khắc kịch tính: chú chim Tu Hú non sơ sinh đỏ hỏn không một cọng lông, mắt nhắm nghiền, trên lưng có vết lõm rõ rệt hình chiếc thìa ưỡn mạnh lưng hất tung quả trứng chim chủ văng qua mép tổ; quả trứng rơi tự do theo đường parabol xuống vực thẳm. |
| b08 | 01:02.8–01:09.1 (6.3s) | L30 | Trời ơi! Con tôi! Trứng của tôi! Tôi đi kiếm mồi về thấy tổ trống trơn, chỉ còn mỗi cục thịt đỏ lòm này nằm thở phì phò! |  | BÊN TRÁI cô đôi chim chích nhỏ xíu màu nâu vàng ngơ ngác, biểu cảm hoảng hốt còng lưng đậu trên mép tổ ôm đầu khóc ròng ròng nước mắt tuôn như mưa; BÊN PHẢI chú chim Tu Hú non sơ sinh đỏ hỏn không một cọng lông, mắt nhắm nghiền, trên lưng có vết lõm rõ rệt hình chiếc thìa nằm phơi bụng giữa tổ thở phì phò ung dung. |
| b09 | 01:09.1–01:17.5 (8.4s) | L31 | Tiếng khóc xé lòng của nạn nhân chim chích chính là minh chứng đanh thép nhất! Quái vật sơ sinh ấy không chỉ hất một quả, mà nó lặp đi lặp lại hành động tàn nhẫn này |  | Bi kịch tổ chim: toàn bộ 3 quả trứng của chủ nhà đã bị hất sạch xuống đất; trong tổ chỉ còn lại duy nhất một mình chú chim Tu Hú non sơ sinh đỏ hỏn không một cọng lông, mắt nhắm nghiền, trên lưng có vết lõm rõ rệt hình chiếc thìa độc chiếm toàn bộ chiếc tổ. |
| b10 | 01:17.5–01:30.7 (13.2s) | L62 | suốt 2-3 ngày đêm ròng rã, hất sạch toàn bộ trứng hoặc chim non của chủ nhà rơi xuống vực thẳm cho đến khi trong tổ chỉ còn lại duy nhất một mình nó độc chiếm ngai vàng! Quả là một bản năng sinh tồn lạnh lùng đến rợn tóc gáy! | **2-3 NGÀY** · HẤT SẠCH CẢ TỔ · L/420 · [0.28, 0.52] | Chú chim non chú chim Tu Hú non sơ sinh đỏ hỏn không một cọng lông, mắt nhắm nghiền, trên lưng có vết lõm rõ rệt hình chiếc thìa một mình nằm thảnh thơi chiếm trọn chiếc tổ êm ấm; xung quanh là vương miện nhỏ tượng trưng cho vị vua độc tôn của chiếc tổ. |

### scene04 · THAO TÚNG TÂM LÝ VÀ ĐỨA CON TO GẤP 3 LẦN · 85.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.6 (10.6s) | L32 | Sau khi đã thanh trừng sạch sẽ mọi đối thủ trong tổ, Siêu Trộm Tổ Ấm bước sang giai đoạn phạm tội thứ 3: Thao túng tâm lý đỉnh cao và bóc lột sức lao động của cha mẹ nuôi đến kiệt quệ! |  | BÊN TRÁI tấm biển lớn ghi 'BẰNG CHỨNG SỐ 3: CON NUÔI KHỔNG LỒ & SIÊU KÍCH THÍCH'; BÊN PHẢI chiếc gương phản chiếu đứa con nuôi to đùng ngã ngửa. KHÔNG có chim Tu Hú trưởng thành trong cảnh này. |
| b02 | 00:10.6–00:17.3 (6.7s) | L33 | Chỉ sau 2 tuần được chăm bẵm độc quyền, chú Tu Hú non lớn nhanh như thổi, béo tròn núc ních và phổng phao gấp 10 lần lúc mới sinh. | **LỚN GẤP 10** · SAU 2 TUẦN BÓN MỒI · R/380 · [0.75, 0.45] | Tốc độ lớn kinh ngạc: sau 2 tuần, chú chim Tu Hú non khổng lồ béo tròn lông xù to gấp 3 lần chim bố mẹ, mỏ há toang đỏ rực viền vàng như hố ga béo múp míp lông xù màu nâu xám, chiếc tổ nhỏ xíu bị nén bẹp dúm dưới thân hình hộ pháp của nó. |
| b03 | 00:17.3–00:29.8 (12.5s) | L34 | Đến tuần thứ 3, nó to gấp 3 lần, thậm chí gấp 4 lần thân hình còi cọc của đôi chim bố mẹ nuôi! Đứng trong chiếc tổ nhỏ xíu, thân hình hộ pháp của nó làm chiếc tổ muốn gãy làm đôi, còn chim bố mẹ đứng cạnh trông chẳng khác nào hạt tiêu đứng cạnh quả dưa hấu! | **GẤP 3 LẦN** · NGHỊCH LÝ CON NUÔI · R/420 · [0.72, 0.5] | Nghịch lý kích thước: BÊN TRÁI đôi chim chích nhỏ xíu màu nâu vàng ngơ ngác, biểu cảm hoảng hốt còng lưng nhỏ xíu như hạt tiêu; BÊN PHẢI chú chim Tu Hú non khổng lồ béo tròn lông xù to gấp 3 lần chim bố mẹ, mỏ há toang đỏ rực viền vàng như hố ga to khổng lồ gấp 3 lần chim bố mẹ, ngồi chễm chệ chiếm trọn màn hình. |
| b04 | 00:29.8–00:41.0 (11.2s) | L35 | Tôi phản đối! Tôi lớn con là do gen di truyền, chứ tôi đâu có ép bố mẹ nuôi phải đi bắt sâu cho tôi ăn đâu! Bị cáo cãi cùn rất trắng trợn! Nhưng khoa học đã lật tẩy mánh khóe ma quái của bị cáo! |  | Tại tòa án: chú chim Tu Hú non khổng lồ béo tròn lông xù to gấp 3 lần chim bố mẹ, mỏ há toang đỏ rực viền vàng như hố ga đứng trên bục nhân chứng giơ hai cánh lên cãi cùn; bồi thẩm đoàn xung quanh ai nấy ôm bụng cười nghiêng ngả. |
| b05 | 00:41.0–00:50.0 (8.9s) | L36 | Các nhà sinh học thần kinh gọi đây là hiện tượng Siêu Kích Thích. Mỗi khi chim bố mẹ mang mồi về, Tu Hú non liền há toang chiếc miệng rộng ngoác màu đỏ tươi viền vàng rực rỡ như một cái hố ga không đáy! | **KÍCH THÍCH** · HỌNG ĐỎ THÔI MIÊN · R/380 · [0.75, 0.45] | Cận cảnh hiện tượng Siêu Kích Thích: chú chim Tu Hú non khổng lồ béo tròn lông xù to gấp 3 lần chim bố mẹ, mỏ há toang đỏ rực viền vàng như hố ga há ngoác chiếc miệng to đùng, vòm họng đỏ rực như đèn pha ô tô viền vàng sáng chói chiếu thẳng vào mắt chim bố mẹ. |
| b06 | 00:50.0–00:57.3 (7.3s) | L63 | Vòm họng đỏ rực ấy phát ra tín hiệu thị giác mãnh liệt đến mức thôi miên não bộ của chim bố mẹ, khiến chúng không tài nào cưỡng lại được mệnh lệnh phải nhét mồi vào! |  | Tia sóng thị giác màu đỏ và vàng phóng ra từ vòm họng chú chim Tu Hú non khổng lồ béo tròn lông xù to gấp 3 lần chim bố mẹ, mỏ há toang đỏ rực viền vàng như hố ga làm hai mắt của đôi chim bố mẹ xoay tròn như bị thôi miên mê mẩn. |
| b07 | 00:57.3–01:06.8 (9.5s) | L37 | Chưa hết, tiếng kêu đòi ăn chíp chíp liên hồi của một con Tu Hú non có tần số rung động tương đương với tiếng kêu gào thảm thiết của cả một đàn bốn con chim non cộng lại! Chim bố mẹ | **BẰNG 4 CON** · TIẾNG GÀO THÔI MIÊN · L/410 · [0.28, 0.5] | So sánh âm thanh: BÊN TRÁI sóng âm thanh của 1 con chú chim Tu Hú non khổng lồ béo tròn lông xù to gấp 3 lần chim bố mẹ, mỏ há toang đỏ rực viền vàng như hố ga gào thét; BÊN PHẢI bằng tổng sóng âm thanh của 4 con chim non chủ nhà cộng lại cùng lúc. |
| b08 | 01:06.8–01:16.8 (10.0s) | L38 | nuôi bị tra tấn màng nhĩ, hoảng hốt bay đi lùng sục sâu bọ suốt 14 tiếng mỗi ngày, bay hàng trăm chuyến từ sáng sớm tới tối mịt chỉ để lấp đầy cái dạ dày không đáy của đứa con nuôi trời đánh! | **14 TIẾNG** · BÓN MỒI KIỆT SỨC · L/380 · [0.25, 0.45] | Cảnh tượng còng lưng phục vụ: đôi chim chích nhỏ xíu màu nâu vàng ngơ ngác, biểu cảm hoảng hốt còng lưng mệt lử bay đi tha sâu bọ liên tục suốt 14 tiếng; mồ hôi chảy ròng ròng quanh chiếc tổ. |
| b09 | 01:16.8–01:25.7 (9.0s) | L64 | Thậm chí chim mẹ nhỏ xíu phải đậu hẳn lên đầu, lên lưng của con Tu Hú khổng lồ để với tới cái mỏ há to của nó, tạo nên một cảnh tượng bi hài bậc nhất trần đời! |  | Cảnh tượng bi hài: cô chim mẹ nhỏ xíu phải đậu hẳn lên đỉnh đầu con Tu Hú khổng lồ chú chim Tu Hú non khổng lồ béo tròn lông xù to gấp 3 lần chim bố mẹ, mỏ há toang đỏ rực viền vàng như hố ga để cúi xuống nhét con sâu béo múp vào mỏ nó. |

### scene05 · CHIẾN THUẬT MAFIA TRẢ THÙ TÀN ĐỘC · 77.3s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.9 (7.9s) | L39 | Đến đây, chắc hẳn quý vị trong bồi thẩm đoàn sẽ đặt câu hỏi: Chẳng lẽ loài chim chủ nhà ngốc nghếch đến mức không bao giờ nhận ra đứa con quái vật này sao? Câu trả lời là: Có! |  | BÊN TRÁI tấm biển ghi 'BẰNG CHỨNG SỐ 4: CHIẾN THUẬT MAFIA RỪNG RẬM'; BÊN PHẢI hình chiếc mũ phớt đen mafia và chiếc kính râm đặt cạnh tổ chim. KHÔNG có chim Tu Hú trưởng thành trong cảnh này. |
| b02 | 00:07.9–00:18.2 (10.4s) | L40 | Nhiều loài chim chủ có đôi mắt tinh tường đã phát hiện ra quả trứng lạ và dùng mỏ hất quả trứng Tu Hú ra khỏi tổ! Nhưng quý vị có biết hậu quả sau đó là gì không? Đó chính là Cáo trạng thứ 4: Chiến thuật mafia tàn độc! |  | BÊN TRÁI một chú chim chủ mắt đeo kính lúp phát hiện quả trứng lạ và dùng mỏ hất văng quả trứng Tu Hú ra khỏi tổ thành công. KHÔNG có chim Tu Hú trưởng thành trong cảnh này. |
| b03 | 00:18.2–00:24.7 (6.5s) | L41 | Năm 2007, hai nhà khoa học Hoover và Robinson đã công bố một nghiên cứu chấn động trên tạp chí khoa học danh tiếng PNAS. | **HOOVER 07** · NGHIÊN CỨU 2007 PNAS · L/400 · [0.28, 0.5] | Bìa tạp chí khoa học PNAS năm 2007: hai nhà khoa học Hoover và Robinson đang quan sát qua ống nhòm; phía xa chim Tu Hú mẹ đang đậu rình rập trên cành cây theo dõi chiếc tổ. |
| b04 | 00:24.7–00:33.9 (9.2s) | L65 | Hóa ra, sau khi đẻ trộm trứng vào tổ người khác, chim Tu Hú mẹ không hề bỏ đi xa mà luôn lén lút nấp ở cành cây gần đó để theo dõi diễn biến, y hệt một tên trùm mafia đang giám sát đàn em! |  | Cận cảnh chim Tu Hú mẹ nấp sau chùm lá rậm rạp, mắt đỏ rực nhìn chăm chú xuống chiếc tổ chim chích như trùm mafia đang giám sát mục tiêu. |
| b05 | 00:33.9–00:44.1 (10.3s) | L42 | Nếu chim chủ nhà ngoan ngoãn ấp trứng Tu Hú, tổ của chúng sẽ hoàn toàn bình yên vô sự. Nhưng nếu phát hiện quả trứng của mình bị vứt bỏ hoặc bị đục thủng, chim Tu Hú mẹ sẽ lập tức dẫn theo đồng bọn lao tới tấn công điên cuồng! |  | So sánh hai số phận: BÊN TRÁI chiếc tổ cam chịu ấp hộ được an toàn yên ấm; BÊN PHẢI chim Tu Hú mẹ lao xuống mổ nát trứng và giật sập tổ của kẻ dám phản kháng. |
| b06 | 00:44.1–00:51.3 (7.1s) | L66 | Nó mổ nát toàn bộ số trứng còn lại của chim chủ nhà, cắn chết những con chim non vừa nở và giật sập tan tành cả chiếc tổ để dằn mặt! |  | Cảnh tượng hung bạo: chim Tu Hú mẹ đập cánh điên cuồng, dùng mỏ nhọn mổ nát trứng chim chủ và hất tung cành rơm giật sập tan tành chiếc tổ. |
| b07 | 00:51.3–01:01.7 (10.4s) | L43 | Các số liệu nghiên cứu đã chỉ ra: những chiếc tổ dám vứt bỏ trứng ký sinh có tỷ lệ bị đập phá tan hoang lên tới hơn 56%, trong khi những chiếc tổ cam chịu ấp hộ chỉ bị quấy rầy dưới 10%! | **56% BỊ PHÁ** · NẾU VỨT BỎ TRỨNG · L/370 · [0.28, 0.45]<br>**DƯỚI 10%** · NẾU CHỊU ẤP HỘ · R/420 · [0.72, 0.52] | Biểu đồ cột tỷ lệ bị phá tổ: CỘT ĐỎ 56% tổ dám vứt trứng bị đập phá tan hoang; CỘT XANH dưới 10% tổ cam chịu ấp hộ bị tấn công. KHÔNG có chim Tu Hú trưởng thành trong cảnh này. |
| b08 | 01:01.7–01:09.2 (7.5s) | L44 | Đây chính là chiến thuật tống tiền bảo kê kinh điển: Mày nuôi con tao thì tổ mày còn, mày dám vứt con tao thì cả gia đình mày tuyệt diệt! |  | Hình minh họa hài hước: chim Tu Hú mẹ khoác áo măng-tô đen, đeo kính râm chìa bản hợp đồng bảo kê 'NUÔI CON TAO HOẶC MẤT TỔ' trước mặt đôi chim chích run rẩy. |
| b09 | 01:09.2–01:17.3 (8.1s) | L67 | Đối mặt với họng súng mafia tàn nhẫn như vậy, chim chủ nhà đành phải ngậm đắng nuốt cay nuôi giùm con kẻ thù để bảo toàn tính mạng! |  | Đôi chim chích ngậm đắng nuốt cay đứng canh tổ với vẻ mặt cam chịu, bên trên là bóng lưng chim Tu Hú mẹ đậu lù lù bảo kê đe dọa. KHÔNG có chim Tu Hú trưởng thành trong cảnh này. |

### scene06 · PHÁN QUYẾT CỦA TỰ NHIÊN VÀ BÓNG ĐEN BÍ ẨN TẬP 15 · 121.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.6 (10.6s) | L45 | Kính thưa quý tòa! Bốn cáo trạng vừa nêu tưởng chừng đã đóng đinh tội danh của Siêu Trộm Tổ Ấm. Nhưng ngay trước giờ tuyên án, luật sư bào chữa xin được đưa ra một góc nhìn hoàn toàn bất ngờ từ đại cục của tự nhiên! |  | Tại tòa án: không khí im lặng căng thẳng; luật sư bào chữa bước lên bục giơ tập hồ sơ mới trước mặt chú cú mèo già thẩm phán đội tóc giả trắng tòa án Anh, mặc áo choàng đen, tay cầm búa gỗ và hội đồng bồi thẩm đoàn. KHÔNG có chim Tu Hú trưởng thành trong cảnh này. |
| b02 | 00:10.6–00:20.8 (10.2s) | L46 | Xin các bác tòa nương tay! Bị cáo này ăn sâu róm độc giỏi lắm, mùa màng nhà tôi nhờ nó mà không bị sâu bọ cắn nát đấy ạ! Lời làm chứng của bác nông dân hoàn toàn có cơ sở khoa học vững chắc! |  | BÊN TRÁI bác nông dân đội nón lá đứng trước bục nhân chứng chắp tay xin tòa nương tay; BÊN PHẢI một cánh đồng lúa xanh tốt không một bóng sâu hại. KHÔNG có chim Tu Hú trưởng thành trong cảnh này. |
| b03 | 00:20.8–00:28.3 (7.5s) | L47 | Trong thế giới loài chim, sâu róm độc có lông ngứa chứa đầy độc tố là món ăn cấm kỵ mà 99% các loài chim khác đều phải tránh xa. |  | Cận cảnh loài sâu róm độc: những con sâu róm đầy gai nhọn lông ngứa gớm ghiếc bò lổm ngổm trên cành lá, các loài chim khác nhìn thấy đều khiếp vía bay xa. KHÔNG có chim Tu Hú trưởng thành trong cảnh này. |
| b04 | 00:28.3–00:39.6 (11.3s) | L48 | Nhưng chim Tu Hú trưởng thành lại là khắc tinh số một của loài sâu độc này! Dạ dày của Tu Hú có một lớp niêm mạc đặc biệt có thể tự bong tróc để đào thải toàn bộ đống lông sâu độc ra ngoài mà không hề bị tổn thương! | **DẠ DÀY** · ĐÀO THẢI LÔNG ĐỘC · R/400 · [0.72, 0.5] | BÊN TRÁI chú chim Tu Hú trưởng thành hoạt hình lông đốm hoa râm xám tro, mắt đỏ tròn tinh ranh, đeo chiếc nơ bướm màu tím than trên cổ, biểu cảm tự tin láu cá đang thong thả nuốt chửng từng con sâu róm độc ngon lành; BÊN PHẢI hình vẽ dạ dày đặc biệt của Tu Hú có lớp niêm mạc tự bong tróc đẩy đống lông độc ra ngoài an toàn. |
| b05 | 00:39.6–00:52.2 (12.6s) | L49 | Chính vì được giải phóng hoàn toàn khỏi gánh nặng ấp trứng và mớm mồi, Tu Hú trưởng thành mới có thể dành trọn vẹn 100% thời gian bay khắp các cánh rừng để săn lùng sâu róm, dập tắt những đại dịch sâu hại bảo vệ thảm thực vật cho toàn bộ hệ sinh thái! | **100% DIỆT** · DIỆT SÂU BẢO VỆ RỪNG · L/380 · [0.28, 0.45] | Bức tranh toàn cảnh hệ sinh thái: chim Tu Hú bay lượn bảo vệ cánh rừng xanh ngát khỏi đại dịch sâu bọ; bên dưới các loài chim chủ tiến hóa đôi mắt tinh tường hơn qua các thế hệ. |
| b06 | 00:52.2–01:02.2 (9.9s) | L68 | Đồng thời, sự lừa đảo tinh vi của Tu Hú cũng chính là động lực thúc đẩy các loài chim chủ tiến hóa thị giác tinh tường hơn và bộ não nhạy bén hơn qua hàng triệu năm qua chạy đua vũ trang tiến hóa! |  | Cuộc chạy đua vũ trang tiến hóa: một bên chim Tu Hú cầm bảng vẽ hoa văn trứng giả mạo ngày càng tinh xảo, một bên chim chủ nhà đeo kính viễn vọng soi xét ngày càng tinh tường. |
| b07 | 01:02.2–01:08.5 (6.3s) | L50 | Tòa tuyên án: Bị cáo Chim Tu Hú không có tội! Đó là quy luật sinh tồn nghiệt ngã nhưng hoàn hảo của tự nhiên! |  | chú cú mèo già thẩm phán đội tóc giả trắng tòa án Anh, mặc áo choàng đen, tay cầm búa gỗ gõ búa dứt khoát mỉm cười; chú chim Tu Hú trưởng thành hoạt hình lông đốm hoa râm xám tro, mắt đỏ tròn tinh ranh, đeo chiếc nơ bướm màu tím than trên cổ, biểu cảm tự tin láu cá mừng rỡ vỗ cánh thở phào nhẹ nhõm; cả tòa án vỗ tay rộn rã trước phán quyết công bằng. |
| b08 | 01:08.5–01:13.4 (4.9s) | L51 | Vụ án thế kỷ của Siêu Trộm Tổ Ấm đã chính thức khép lại với phán quyết đầy tính nhân văn! |  | Khung cảnh phiên tòa mờ dần về sau; ánh đèn sân khấu tập trung vào một chiếc màn hình chiếu lớn ở chính giữa sân khấu mang màu sắc bí ẩn kịch tính. KHÔNG có chim Tu Hú trưởng thành trong cảnh này. |
| b09 | 01:13.4–01:22.5 (9.1s) | L52 | Nhưng ngay lúc này, xin mời quý vị khán giả hãy hướng mắt lên màn hình lớn để chiêm ngưỡng BÓNG ĐEN BÍ ẨN của nhân vật sẽ xuất hiện trong Tập 15 tiếp theo! | **BÓNG ĐEN** · BẬT MÍ QUÁI KIỆT · R/360 · [0.75, 0.42] | Chiếc màn hình lớn bật sáng với hào quang màu vàng hổ phách huyền ảo: Ở GIỮA là BÓNG ĐEN BÍ ẨN (solid black silhouette) hình dáng một loài động vật gặm nhấm to tròn mũm mĩm kèm một dấu hỏi chấm '?' khổng lồ. KHÔNG có chim Tu Hú trưởng thành trong cảnh này. |
| b10 | 01:22.5–01:34.7 (12.2s) | L53 | Xin gửi tới quý vị ba manh mối chấn động về nhân vật bí ẩn này: Thứ nhất, đây là vị Bộ trưởng Ngoại giao hòa bình nhất hành tinh, dù nằm giữa đàn cá sấu ăn thịt khổng lồ hay đàn trăn gấm Nam Mỹ thì vẫn thảnh thơi nằm ngửa bụng ngủ ngon lành mà chẳng có ai thèm tấn công! | **MANH MỐI 1** · BỘ TRƯỞNG NGOẠI GIAO · L/390 · [0.25, 0.48] | Manh mối số 1: BÓNG ĐEN BÍ ẨN đang nằm thảnh thơi nhắm mắt ngủ ngon lành ngay giữa bầy cá sấu ăn thịt khổng lồ đang há miệng mà không con nào thèm cắn. KHÔNG có chim Tu Hú trưởng thành trong cảnh này. |
| b11 | 01:34.7–01:42.5 (7.8s) | L54 | Thứ hai, đây là siêu quái kiệt gặm nhấm lớn nhất thế giới với cân nặng lên tới 65kg, sở hữu tài bơi lặn cừ khôi và có thể nín thở dưới đáy sông suốt 5 phút đồng | **65KG** · GẶM NHẤM KHỔNG LỒ · R/370 · [0.75, 0.45]<br>**NÍN THỞ 5P** · BƠI LẶN SIÊU ĐẲNG · R/470 · [0.75, 0.58] | Manh mối số 2: BÓNG ĐEN BÍ ẨN đứng trên bàn cân hiển thị 65kg, đang bơi lặn thong thả dưới đáy sông với đôi chân màng và đồng hồ đếm nín thở 5 phút. KHÔNG có chim Tu Hú trưởng thành trong cảnh này. |
| b12 | 01:42.5–01:50.5 (8.0s) | L55 | hồ! Và thứ 3, một nghịch lý cực kỳ khó đỡ: thói quen ăn lại chính phân của mình vào mỗi buổi sáng sớm để hấp thu dinh dưỡng! Quý vị khán | **MANH MỐI 3** · NGHỊCH LÝ BUỔI SÁNG · L/400 · [0.25, 0.5] | Manh mối số 3: BÓNG ĐEN BÍ ẨN với biểu cảm 'tĩnh tâm khó đỡ' bên tách trà sáng sớm, góc dưới một chi tiết hài hước tái hấp thu dinh dưỡng để sinh tồn. KHÔNG có chim Tu Hú trưởng thành trong cảnh này. |
| b13 | 01:50.5–01:57.7 (7.2s) | L56 | giả có nhận ra bóng đen bí ẩn mang phong thái ung dung tự tại này là ai không? Hãy để lại dự đoán của bạn ngay dưới phần bình luận nhé! |  | BÓNG ĐEN BÍ ẨN to lớn đứng giữa màn hình với dấu hỏi chấm '?' nhấp nháy phát sáng; xung quanh là các bong bóng bình luận '? ? ?' kêu gọi khán giả trổ tài dự đoán. KHÔNG có chim Tu Hú trưởng thành trong cảnh này. |
| b14 | 01:57.7–02:01.4 (3.8s) | L57 | Phóng viên phiên tòa xin chào tạm biệt và hẹn gặp lại quý vị trong tập tiếp theo! |  | BÊN TRÁI thẩm phán và các nhân vật chim vẫy cánh chào tạm biệt; BÊN PHẢI tấm biển gỗ đề chữ 'HẸN GẶP LẠI Ở TẬP 15 VỚI VỊ BỘ TRƯỞNG NGOẠI GIAO!'. KHÔNG có chim Tu Hú trưởng thành trong cảnh này. |

## 5. Phân cảnh Shorts — từng beat

Banner: **SÁT THỦ 10 GIÂY?! / BẢN NĂNG KINH HOÀNG** · giọng 51.0s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Bị cáo, mời đứng lên! |  |
| s02 | 00:01.9 | S02 | Một loài chim không bao giờ xây tổ, không ấp trứng, không nuôi con, |  |
| s03 | 00:05.5 | S12 | nhưng lại sở hữu bản năng sát thủ ngay từ giây phút đầu tiên chui ra khỏi vỏ! |  |
| s04 | 00:09.3 | S03 | Đó chính là Chim Tu Hú, kẻ lừa đảo khét tiếng bậc nhất thế giới tự nhiên. |  |
| s05 | 00:13.4 | S04 | Chim mẹ chỉ mất đúng 10 giây để đột nhập tổ chim chích, nuốt chửng một quả trứng của chủ | **10 GIÂY** · CƯỚP VÀ ĐẺ TRỨNG · L/620 · [0.5, 0.45] |
| s06 | 00:17.9 | S05 | nhà và đẻ thay vào đó quả trứng của mình với hoa văn giả mạo giống tới 99%! | **GIỐNG 99%** · HOA VĂN GIẢ MẠO · R/640 · [0.55, 0.48] |
| s07 | 00:23.5 | S06 | Đáng sợ hơn cả, con non vừa nở chỉ nặng 2g, mắt còn nhắm nghiền chưa mở, | **NẶNG 2G** · MÙ MẮT KHÔNG LÔNG · L/620 · [0.5, 0.45] |
| s08 | 00:28.1 | S07 | nhưng đã dùng chiếc lưng lõm bẩm sinh gồng | **LƯNG LÕM** · BẢN NĂNG SÁT THỦ · R/660 · [0.55, 0.5] |
| s09 | 00:30.2 | S08 | mình hất tung toàn bộ trứng của chim chủ nhà rơi xuống đất vỡ nát! |  |
| s10 | 00:33.2 | S09 | Để rồi sau đó, đứa con nuôi khổng lồ lớn nhanh như thổi, to gấp 3 lần chim bố mẹ, | **GẤP 3 LẦN** · CON NUÔI KHỔNG LỒ · L/640 · [0.5, 0.48] |
| s11 | 00:38.1 | S10 | há to chiếc miệng đỏ lòm như hố ga thôi miên cha mẹ nuôi phải hầu hạ mớm mồi suốt ngày đêm! | **HỌNG ĐỎ** · THÔI MIÊN BỐ MẸ · R/650 · [0.55, 0.5] |
| s12 | 00:43.6 | S11 | Vậy là vụ án đã sáng tỏ: một chiến thuật ký sinh tàn nhẫn |  |
| s13 | 00:47.1 | S13 | nhưng là cách sinh tồn hoàn hảo giúp loài chim này trường tồn qua hàng triệu năm qua! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tòa án tối cao thế giới tự nhiên! Cốc, cốc, cốc!". Bố cục: BÊN TRÁI chú cú mèo già thẩm phán đội tóc giả trắng tòa án Anh, mặc áo choàng đen, tay cầm búa gỗ đang nghiêm nghị gõ búa gỗ xuống bàn; Ở GIỮA tấm biển lớn đề chữ 'TÒA ÁN TỐI CAO THẾ GIỚI TỰ NHIÊN' treo giữa rừng già; BÊN PHẢI hàng loạt muôn loài chim muông đang ngồi trên các cành cây theo dõi hồi hộp. KHÔNG có chim Tu Hú trưởng thành trong cảnh này.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tiếng búa gõ vang dội giữa rừng già trong một buổi sáng đầy căng thẳng.". Bố cục: Toàn cảnh góc rộng khu rừng rậm: ánh nắng sớm rọi qua kẽ lá, các loài chim chích, chim sáo, chim quạ tụ tập đông đúc quanh cành cây cổ thụ nghe ngóng xôn xao. KHÔNG có chim Tu Hú trưởng thành trong cảnh này.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trên cành cây cổ thụ râm mát, một vụ án hình sự đặc biệt nghiêm trọng đang được đưa ra xét xử công khai trước sự chứng kiến của muôn loài chim muông!". Bố cục: Góc nhìn cận cảnh cành cây cổ thụ: một chiếc tổ chim nhỏ bị bỏ trống, bên cạnh là hồ sơ vụ án viền đỏ đóng dấu 'ÁP GIẢI TỘI PHẠM'. KHÔNG có chim Tu Hú trưởng thành trong cảnh này.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trật tự phiên tòa! Đề nghị công tố viên đọc to cáo trạng!". Bố cục: BÊN TRÁI chú cú mèo già thẩm phán đội tóc giả trắng tòa án Anh, mặc áo choàng đen, tay cầm búa gỗ đứng nghiêm nghị giơ tay ra lệnh trật tự; Ở GIỮA bục công tố viên lót tài liệu; BÊN PHẢI cả hội đồng chim chóc im phăng phắc nín thở. KHÔNG có chim Tu Hú trưởng thành trong cảnh này.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kính thưa quý tòa và hội đồng bồi thẩm đoàn! Kẻ đang đứng trước vành móng ngựa hôm nay là một kẻ có hành tung thoắt ẩn thoắt hiện, sở hữu bộ lông hoa râm đốm xám và tiếng kêu tu hú vang vọng khắp các cánh đồng mỗi mùa vải chín!". Bố cục: BÊN TRÁI công tố viên chỉ tay đanh thép về phía vành móng ngựa; BÊN PHẢI chú chim Tu Hú trưởng thành hoạt hình lông đốm hoa râm xám tro, mắt đỏ tròn tinh ranh, đeo chiếc nơ bướm màu tím than trên cổ, biểu cảm tự tin láu cá đang đứng ung dung trong vành móng ngựa gỗ, mắt đỏ nhếch mép huýt sáo.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vâng, đó chính là chim Tu Hú — loài chim được giang hồ thế giới tự nhiên đặt cho biệt danh khét tiếng: Siêu Trộm Tổ Ấm!". Bố cục: Cận cảnh chân dung chú chim Tu Hú trưởng thành hoạt hình lông đốm hoa râm xám tro, mắt đỏ tròn tinh ranh, đeo chiếc nơ bướm màu tím than trên cổ, biểu cảm tự tin láu cá: bộ lông đốm hoa râm xám tro, nơ tím than chỉnh tề, mỏ nhọn đang kêu 'Tu hú! Tu hú!' vang dội giữa những chùm quả vải chín đỏ mọng xung quanh.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bị cáo trông bề ngoài thì có vẻ phong nhã, hiền lành, nhưng lật giở hồ sơ tiền án tiền sự của Siêu Trộm Tổ Ấm thì ai nấy đều phải rùng mình kinh hãi!". Bố cục: So sánh hai mặt đối lập: BÊN TRÁI chú chim Tu Hú trưởng thành hoạt hình lông đốm hoa râm xám tro, mắt đỏ tròn tinh ranh, đeo chiếc nơ bướm màu tím than trên cổ, biểu cảm tự tin láu cá trông lịch lãm như quý ông; BÊN PHẢI một cuốn sổ đen tiền án tiền sự dày cộm dán ảnh truy nã đề chữ 'SIÊU TRỘM TỔ ẤM'.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không xây tổ, không ấp trứng, không nuôi con, lười biếng đến mức tận cùng nhưng lại sở hữu những ngón nghề lừa đảo tinh vi bậc nhất lịch sử tiến hóa!". Bố cục: Hình ảnh châm biếm: Ở GIỮA chú chim Tu Hú trưởng thành hoạt hình lông đốm hoa râm xám tro, mắt đỏ tròn tinh ranh, đeo chiếc nơ bướm màu tím than trên cổ, biểu cảm tự tin láu cá nằm đung đưa trên võng lá ngủ khò, một cánh gối đầu, một cánh phẩy quạt; xung quanh các loài chim khác đang hì hục tha rơm xây tổ toát mồ hôi.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hôm nay, công tố viên tôi xin đại diện cho hàng vạn nạn nhân chim chích, chim sáo, chim chích chòe đệ trình lên tòa bốn bằng chứng không thể chối cãi:". Bố cục: BÊN TRÁI hàng trăm chú chim chích, chim sáo nhỏ bé cầm biểu ngữ 'TRẢ LẠI CON CHO TÔI!'; BÊN PHẢI công tố viên mở tập tài liệu 4 cáo trạng hình sự phát sáng đỏ rực. KHÔNG có chim Tu Hú trưởng thành trong cảnh này.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Liệu một kẻ mang đầy tội trạng rợn người như thế này có xứng đáng nhận án phạt thích đáng? Kính mời bồi thẩm đoàn cùng theo dõi!". Bố cục: BÊN TRÁI chú chim Tu Hú trưởng thành hoạt hình lông đốm hoa râm xám tro, mắt đỏ tròn tinh ranh, đeo chiếc nơ bướm màu tím than trên cổ, biểu cảm tự tin láu cá đứng trong bóng tối với nụ cười bí hiểm; BÊN PHẢI cán cân công lý bằng vàng rực rỡ đang nghiêng ngả trước hàng loạt bằng chứng tội trạng.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bằng chứng số 1: Hành vi xâm nhập gia cư bất hợp pháp và đánh tráo tài sản với tốc độ kinh hoàng chỉ trong 10 giây!". Bố cục: BÊN TRÁI tấm bảng lớn ghi chữ 'BẰNG CHỨNG SỐ 1: VỤ CƯỚP TRỨNG 10 GIÂY'; BÊN PHẢI một chiếc đồng hồ bấm giờ thể thao đang điểm số 00:10 nhấp nháy phát sáng. KHÔNG có chim Tu Hú trưởng thành trong cảnh này.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thông thường, một cô chim mái cần từ 20 phút đến 30 phút đồng hồ tĩnh tâm để đẻ xong một quả trứng. Nhưng với Siêu Trộm Tổ Ấm, việc sinh nở diễn ra nhanh như một tên trộm giật túi xách trên phố!". Bố cục: So sánh tốc độ sinh nở: BÊN TRÁI cô chim sẻ ngồi tĩnh tâm trên tổ với đồng hồ đếm ngược 20-30 phút; BÊN PHẢI một tên trộm bịt mặt chạy vút qua như tia chớp giật lấy quả trứng hài hước. KHÔNG có chim Tu Hú trưởng thành trong cảnh này.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để thực hiện phi vụ hoàn hảo, vợ chồng Tu Hú đã phối hợp tác chiến với kịch bản ăn ý đến từng mi-li-giây!". Bố cục: Bản vẽ chiến thuật quân sự: sơ đồ tác chiến chia làm hai mũi tấn công; mũi tên đỏ chỉ hướng chim bố nghi binh dụ địch, mũi tên xanh chỉ hướng chim mẹ đột kích lén lút vào tổ chim chích.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chim Tu Hú bố sở hữu bộ lông đen tuyền bóng bẩy sẽ bay lượn sát tổ của nạn nhân, phát ra những tiếng kêu khiêu khích chói tai làm chim chủ nhà nổi giận bay ra đuổi đánh.". Bố cục: BÊN TRÁI chim Tu Hú trống lông đen tuyền bay lượn khiêu khích nhổ lông trêu chọc; BÊN PHẢI đôi chim chủ nhà tức giận đỏ mặt xù lông bay ra khỏi tổ rượt đuổi quyết liệt.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và ngay khi chim chủ nhà vừa rời khỏi tổ, chim Tu Hú mẹ lập tức từ bụi cây lao vút xuống như một bóng ma!". Bố cục: Cận cảnh tổ chim chích trơ trọi không ai canh giữ: từ cành cây rậm rạp phía trên, chim Tu Hú mẹ mắt đỏ lao thẳng xuống tổ nhanh như một mũi tên xé gió.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bấm đồng hồ: 1 giây đáp xuống tổ!". Bố cục: Mốc 1 giây: chim Tu Hú mẹ đáp nhẹ nhàng xuống mép tổ chim chích; một chiếc đồng hồ bấm giờ góc trái hiển thị con số 00:01.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "2 giây cúi xuống dùng mỏ ngoạm lấy một quả trứng của chim chủ nhà nuốt chửng hoặc vứt văng ra ngoài!". Bố cục: Mốc 2 giây: chim Tu Hú mẹ cúi mỏ ngoạm lấy một quả trứng của chim chủ nhà hất văng ra khỏi tổ rơi tự do; đồng hồ góc trái hiển thị 00:02.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "3 giây ép sát bụng xuống đáy tổ và rặn đẻ đúng một quả trứng của mình thay vào vị trí đó!". Bố cục: Mốc 3 giây: chim Tu Hú mẹ ép sát bụng xuống đáy tổ rặn đẻ quả trứng của mình thay vào đúng vị trí quả trứng vừa mất; đồng hồ hiển thị 00:03.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "5 giây tiếp theo: đập cánh bay biến vào tán lá rậm rạp! Toàn bộ vụ đột nhập đánh tráo diễn ra vỏn vẹn đúng 10 giây đồng hồ, đến nỗi chiếc lá trên tổ còn chưa kịp ngừng rung rinh thì kẻ gian đã cao chạy xa bay!". Bố cục: Mốc 5 giây tiếp theo: chim Tu Hú mẹ đập cánh bay vút đi để lại làn khói mờ ảo; chiếc lá trên mép tổ vẫn còn đung đưa chưa kịp đứng yên.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng tại sao chim chủ nhà khi quay về lại không phát hiện ra quả trứng lạ?". Bố cục: BÊN TRÁI đôi đôi chim chích nhỏ xíu màu nâu vàng ngơ ngác, biểu cảm hoảng hốt còng lưng bay về tổ đứng nhìn ngơ ngác gãi đầu; Ở GIỮA tổ chim có 4 quả trứng trông giống hệt nhau không một chút khác biệt.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây chính là đỉnh cao của công nghệ làm giả trong tự nhiên: trứng của Tu Hú có màu sắc, đốm hoa văn và kích thước giống trứng của chim chủ tới 99%!". Bố cục: Cận cảnh phóng đại hai quả trứng đặt cạnh nhau: BÊN TRÁI trứng chim chích; BÊN PHẢI trứng chim Tu Hú; cả hai đều có vỏ màu xanh nhạt đốm nâu giống nhau 99%.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa dừng lại ở đó, vỏ trứng của Siêu Trộm Tổ Ấm còn tiến hóa dày hơn và cứng hơn trứng bình thường gấp 2 lần! Để làm gì quý vị biết không?". Bố cục: Thí nghiệm đo độ cứng vỏ trứng: quả trứng Tu Hú được đặt dưới một chiếc búa nhỏ đập vào mà không vỡ, vỏ trứng dày gấp đôi vỏ trứng bình thường. KHÔNG có chim Tu Hú trưởng thành trong cảnh này.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kính thưa quý tòa! Tội ác của chim mẹ mới chỉ là màn dạo đầu. Cáo trạng thứ 2 mới thực sự là nỗi ám ảnh kinh hoàng nhất trong lịch sử sinh học: Tội ác của sát thủ sơ sinh chưa mở mắt!". Bố cục: BÊN TRÁI tấm biển lớn đề 'BẰNG CHỨNG SỐ 2: SÁT THỦ CHƯA MỞ MẮT'; BÊN PHẢI hình bóng đen một chú chim non sơ sinh đỏ hỏn toát ra luồng khí lạnh lùng rợn người. KHÔNG có chim Tu Hú trưởng thành trong cảnh này.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trứng của Tu Hú luôn được thiên nhiên ban cho đặc quyền nở sớm hơn trứng của chim chủ nhà từ 24 giờ đến 48 giờ. Lý do là vì phôi thai của Tu Hú đã bắt đầu phát triển ngay từ khi còn nằm trong ống dẫn trứng của chim mẹ!". Bố cục: Sơ đồ thời gian ấp trứng: quả trứng Tu Hú nứt vỏ nở trước 24-48 giờ; bên cạnh là những quả trứng chim chủ nhà vẫn còn nằm im lìm chưa kịp cựa quậy. KHÔNG có chim Tu Hú trưởng thành trong cảnh này.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi chui ra khỏi vỏ, chú chim Tu Hú non chỉ nặng vỏn vẹn 2g, trần trụi chẳng có cọng lông nào, mắt nhắm nghiền tịt mít như một hạt đậu đỏ! Nhưng đừng để vẻ ngoài yếu ớt ấy đánh lừa!". Bố cục: Cận cảnh chú chim Tu Hú non sơ sinh đỏ hỏn không một cọng lông, mắt nhắm nghiền, trên lưng có vết lõm rõ rệt hình chiếc thìa nằm trên một chiếc cân tiểu ly điện tử hiển thị con số vỏn vẹn 2g; cơ thể đỏ hỏn không cọng lông, mắt nhắm nghiền như hạt đỗ.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trên lưng của quái kiệt sơ sinh này có một vết lõm bẩm sinh hình chiếc thìa, tập trung hàng vạn đầu dây thần kinh cực kỳ nhạy cảm. Chỉ cần bất kỳ vật thể nào chạm nhẹ vào chiếc lưng lõm ấy, một công tắc sát thủ man rợ trong não bộ lập tức được kích hoạt!". Bố cục: Phóng to cận cảnh chiếc lưng của chú chim Tu Hú non sơ sinh đỏ hỏn không một cọng lông, mắt nhắm nghiền, trên lưng có vết lõm rõ rệt hình chiếc thìa: một vết lõm bẩm sinh hình chiếc thìa sâu hoắm, các dây thần kinh xung quanh phát sáng màu xanh neon nhạy cảm.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chú chim non đỏ hỏn lùi dần từng bước về phía những quả trứng của chim chủ nhà. Nó dùng đôi cánh cụt ngủn quặp chặt lấy quả trứng, gồng hai chân non nớt quắp chặt vào thành tổ, rồi từ từ nâng quả trứng to bằng cả cơ thể mình lên trên lưng!". Bố cục: chú chim Tu Hú non sơ sinh đỏ hỏn không một cọng lông, mắt nhắm nghiền, trên lưng có vết lõm rõ rệt hình chiếc thìa lùi lũi đi lùi từng bước trong tổ, hai cánh cụt ngủn ôm ghì lấy một quả trứng chim chủ to bằng cả người nó, đặt quả trứng lọt thỏm vào chiếc lưng lõm.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó bước lùi từng xăng-ti-mét một, thở dốc vì kiệt sức, leo lên tận mép tổ rồi... Hất mạnh một cú dứt khoát! Quả trứng của chim chủ nhà". Bố cục: chú chim Tu Hú non sơ sinh đỏ hỏn không một cọng lông, mắt nhắm nghiền, trên lưng có vết lõm rõ rệt hình chiếc thìa dùng hai chân non nớt quắp chặt thành tổ, gồng mình đẩy quả trứng leo dần lên mép tổ; những giọt mồ hôi hoạt hình văng ra vì gắng sức.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "rơi thẳng từ trên ngọn cây xuống đất, vỡ tan tành thành từng mảnh vụn!". Bố cục: Khoảnh khắc kịch tính: chú chim Tu Hú non sơ sinh đỏ hỏn không một cọng lông, mắt nhắm nghiền, trên lưng có vết lõm rõ rệt hình chiếc thìa ưỡn mạnh lưng hất tung quả trứng chim chủ văng qua mép tổ; quả trứng rơi tự do theo đường parabol xuống vực thẳm.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trời ơi! Con tôi! Trứng của tôi! Tôi đi kiếm mồi về thấy tổ trống trơn, chỉ còn mỗi cục thịt đỏ lòm này nằm thở phì phò!". Bố cục: BÊN TRÁI cô đôi chim chích nhỏ xíu màu nâu vàng ngơ ngác, biểu cảm hoảng hốt còng lưng đậu trên mép tổ ôm đầu khóc ròng ròng nước mắt tuôn như mưa; BÊN PHẢI chú chim Tu Hú non sơ sinh đỏ hỏn không một cọng lông, mắt nhắm nghiền, trên lưng có vết lõm rõ rệt hình chiếc thìa nằm phơi bụng giữa tổ thở phì phò ung dung.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tiếng khóc xé lòng của nạn nhân chim chích chính là minh chứng đanh thép nhất! Quái vật sơ sinh ấy không chỉ hất một quả, mà nó lặp đi lặp lại hành động tàn nhẫn này". Bố cục: Bi kịch tổ chim: toàn bộ 3 quả trứng của chủ nhà đã bị hất sạch xuống đất; trong tổ chỉ còn lại duy nhất một mình chú chim Tu Hú non sơ sinh đỏ hỏn không một cọng lông, mắt nhắm nghiền, trên lưng có vết lõm rõ rệt hình chiếc thìa độc chiếm toàn bộ chiếc tổ.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sau khi đã thanh trừng sạch sẽ mọi đối thủ trong tổ, Siêu Trộm Tổ Ấm bước sang giai đoạn phạm tội thứ 3: Thao túng tâm lý đỉnh cao và bóc lột sức lao động của cha mẹ nuôi đến kiệt quệ!". Bố cục: BÊN TRÁI tấm biển lớn ghi 'BẰNG CHỨNG SỐ 3: CON NUÔI KHỔNG LỒ & SIÊU KÍCH THÍCH'; BÊN PHẢI chiếc gương phản chiếu đứa con nuôi to đùng ngã ngửa. KHÔNG có chim Tu Hú trưởng thành trong cảnh này.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ sau 2 tuần được chăm bẵm độc quyền, chú Tu Hú non lớn nhanh như thổi, béo tròn núc ních và phổng phao gấp 10 lần lúc mới sinh.". Bố cục: Tốc độ lớn kinh ngạc: sau 2 tuần, chú chim Tu Hú non khổng lồ béo tròn lông xù to gấp 3 lần chim bố mẹ, mỏ há toang đỏ rực viền vàng như hố ga béo múp míp lông xù màu nâu xám, chiếc tổ nhỏ xíu bị nén bẹp dúm dưới thân hình hộ pháp của nó.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đến tuần thứ 3, nó to gấp 3 lần, thậm chí gấp 4 lần thân hình còi cọc của đôi chim bố mẹ nuôi! Đứng trong chiếc tổ nhỏ xíu, thân hình hộ pháp của nó làm chiếc tổ muốn gãy làm đôi, còn chim bố mẹ đứng cạnh trông chẳng khác nào hạt tiêu đứng cạnh quả dưa hấu!". Bố cục: Nghịch lý kích thước: BÊN TRÁI đôi chim chích nhỏ xíu màu nâu vàng ngơ ngác, biểu cảm hoảng hốt còng lưng nhỏ xíu như hạt tiêu; BÊN PHẢI chú chim Tu Hú non khổng lồ béo tròn lông xù to gấp 3 lần chim bố mẹ, mỏ há toang đỏ rực viền vàng như hố ga to khổng lồ gấp 3 lần chim bố mẹ, ngồi chễm chệ chiếm trọn màn hình.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôi phản đối! Tôi lớn con là do gen di truyền, chứ tôi đâu có ép bố mẹ nuôi phải đi bắt sâu cho tôi ăn đâu! Bị cáo cãi cùn rất trắng trợn! Nhưng khoa học đã lật tẩy mánh khóe ma quái của bị cáo!". Bố cục: Tại tòa án: chú chim Tu Hú non khổng lồ béo tròn lông xù to gấp 3 lần chim bố mẹ, mỏ há toang đỏ rực viền vàng như hố ga đứng trên bục nhân chứng giơ hai cánh lên cãi cùn; bồi thẩm đoàn xung quanh ai nấy ôm bụng cười nghiêng ngả.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà sinh học thần kinh gọi đây là hiện tượng Siêu Kích Thích. Mỗi khi chim bố mẹ mang mồi về, Tu Hú non liền há toang chiếc miệng rộng ngoác màu đỏ tươi viền vàng rực rỡ như một cái hố ga không đáy!". Bố cục: Cận cảnh hiện tượng Siêu Kích Thích: chú chim Tu Hú non khổng lồ béo tròn lông xù to gấp 3 lần chim bố mẹ, mỏ há toang đỏ rực viền vàng như hố ga há ngoác chiếc miệng to đùng, vòm họng đỏ rực như đèn pha ô tô viền vàng sáng chói chiếu thẳng vào mắt chim bố mẹ.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa hết, tiếng kêu đòi ăn chíp chíp liên hồi của một con Tu Hú non có tần số rung động tương đương với tiếng kêu gào thảm thiết của cả một đàn bốn con chim non cộng lại! Chim bố mẹ nuôi". Bố cục: So sánh âm thanh: BÊN TRÁI sóng âm thanh của 1 con chú chim Tu Hú non khổng lồ béo tròn lông xù to gấp 3 lần chim bố mẹ, mỏ há toang đỏ rực viền vàng như hố ga gào thét; BÊN PHẢI bằng tổng sóng âm thanh của 4 con chim non chủ nhà cộng lại cùng lúc.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bị tra tấn màng nhĩ, hoảng hốt bay đi lùng sục sâu bọ suốt 14 tiếng mỗi ngày, bay hàng trăm chuyến từ sáng sớm tới tối mịt chỉ để lấp đầy cái dạ dày không đáy của đứa con nuôi trời đánh!". Bố cục: Cảnh tượng còng lưng phục vụ: đôi chim chích nhỏ xíu màu nâu vàng ngơ ngác, biểu cảm hoảng hốt còng lưng mệt lử bay đi tha sâu bọ liên tục suốt 14 tiếng; mồ hôi chảy ròng ròng quanh chiếc tổ.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đến đây, chắc hẳn quý vị trong bồi thẩm đoàn sẽ đặt câu hỏi: Chẳng lẽ loài chim chủ nhà ngốc nghếch đến mức không bao giờ nhận ra đứa con quái vật này sao? Câu trả lời là: Có!". Bố cục: BÊN TRÁI tấm biển ghi 'BẰNG CHỨNG SỐ 4: CHIẾN THUẬT MAFIA RỪNG RẬM'; BÊN PHẢI hình chiếc mũ phớt đen mafia và chiếc kính râm đặt cạnh tổ chim. KHÔNG có chim Tu Hú trưởng thành trong cảnh này.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhiều loài chim chủ có đôi mắt tinh tường đã phát hiện ra quả trứng lạ và dùng mỏ hất quả trứng Tu Hú ra khỏi tổ! Nhưng quý vị có biết hậu quả sau đó là gì không? Đó chính là Cáo trạng thứ 4: Chiến thuật mafia tàn độc!". Bố cục: BÊN TRÁI một chú chim chủ mắt đeo kính lúp phát hiện quả trứng lạ và dùng mỏ hất văng quả trứng Tu Hú ra khỏi tổ thành công. KHÔNG có chim Tu Hú trưởng thành trong cảnh này.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 2007, hai nhà khoa học Hoover và Robinson đã công bố một nghiên cứu chấn động trên tạp chí khoa học danh tiếng PNAS.". Bố cục: Bìa tạp chí khoa học PNAS năm 2007: hai nhà khoa học Hoover và Robinson đang quan sát qua ống nhòm; phía xa chim Tu Hú mẹ đang đậu rình rập trên cành cây theo dõi chiếc tổ.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu chim chủ nhà ngoan ngoãn ấp trứng Tu Hú, tổ của chúng sẽ hoàn toàn bình yên vô sự. Nhưng nếu phát hiện quả trứng của mình bị vứt bỏ hoặc bị đục thủng, chim Tu Hú mẹ sẽ lập tức dẫn theo đồng bọn lao tới tấn công điên cuồng!". Bố cục: So sánh hai số phận: BÊN TRÁI chiếc tổ cam chịu ấp hộ được an toàn yên ấm; BÊN PHẢI chim Tu Hú mẹ lao xuống mổ nát trứng và giật sập tổ của kẻ dám phản kháng.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các số liệu nghiên cứu đã chỉ ra: những chiếc tổ dám vứt bỏ trứng ký sinh có tỷ lệ bị đập phá tan hoang lên tới hơn 56%, trong khi những chiếc tổ cam chịu ấp hộ chỉ bị quấy rầy dưới 10%!". Bố cục: Biểu đồ cột tỷ lệ bị phá tổ: CỘT ĐỎ 56% tổ dám vứt trứng bị đập phá tan hoang; CỘT XANH dưới 10% tổ cam chịu ấp hộ bị tấn công. KHÔNG có chim Tu Hú trưởng thành trong cảnh này.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây chính là chiến thuật tống tiền bảo kê kinh điển: Mày nuôi con tao thì tổ mày còn, mày dám vứt con tao thì cả gia đình mày tuyệt diệt!". Bố cục: Hình minh họa hài hước: chim Tu Hú mẹ khoác áo măng-tô đen, đeo kính râm chìa bản hợp đồng bảo kê 'NUÔI CON TAO HOẶC MẤT TỔ' trước mặt đôi chim chích run rẩy.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kính thưa quý tòa! Bốn cáo trạng vừa nêu tưởng chừng đã đóng đinh tội danh của Siêu Trộm Tổ Ấm. Nhưng ngay trước giờ tuyên án, luật sư bào chữa xin được đưa ra một góc nhìn hoàn toàn bất ngờ từ đại cục của tự nhiên!". Bố cục: Tại tòa án: không khí im lặng căng thẳng; luật sư bào chữa bước lên bục giơ tập hồ sơ mới trước mặt chú cú mèo già thẩm phán đội tóc giả trắng tòa án Anh, mặc áo choàng đen, tay cầm búa gỗ và hội đồng bồi thẩm đoàn. KHÔNG có chim Tu Hú trưởng thành trong cảnh này.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Xin các bác tòa nương tay! Bị cáo này ăn sâu róm độc giỏi lắm, mùa màng nhà tôi nhờ nó mà không bị sâu bọ cắn nát đấy ạ! Lời làm chứng của bác nông dân hoàn toàn có cơ sở khoa học vững chắc!". Bố cục: BÊN TRÁI bác nông dân đội nón lá đứng trước bục nhân chứng chắp tay xin tòa nương tay; BÊN PHẢI một cánh đồng lúa xanh tốt không một bóng sâu hại. KHÔNG có chim Tu Hú trưởng thành trong cảnh này.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong thế giới loài chim, sâu róm độc có lông ngứa chứa đầy độc tố là món ăn cấm kỵ mà 99% các loài chim khác đều phải tránh xa.". Bố cục: Cận cảnh loài sâu róm độc: những con sâu róm đầy gai nhọn lông ngứa gớm ghiếc bò lổm ngổm trên cành lá, các loài chim khác nhìn thấy đều khiếp vía bay xa. KHÔNG có chim Tu Hú trưởng thành trong cảnh này.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng chim Tu Hú trưởng thành lại là khắc tinh số một của loài sâu độc này! Dạ dày của Tu Hú có một lớp niêm mạc đặc biệt có thể tự bong tróc để đào thải toàn bộ đống lông sâu độc ra ngoài mà không hề bị tổn thương!". Bố cục: BÊN TRÁI chú chim Tu Hú trưởng thành hoạt hình lông đốm hoa râm xám tro, mắt đỏ tròn tinh ranh, đeo chiếc nơ bướm màu tím than trên cổ, biểu cảm tự tin láu cá đang thong thả nuốt chửng từng con sâu róm độc ngon lành; BÊN PHẢI hình vẽ dạ dày đặc biệt của Tu Hú có lớp niêm mạc tự bong tróc đẩy đống lông độc ra ngoài an toàn.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chính vì được giải phóng hoàn toàn khỏi gánh nặng ấp trứng và mớm mồi, Tu Hú trưởng thành mới có thể dành trọn vẹn 100% thời gian bay khắp các cánh rừng để săn lùng sâu róm, dập tắt những đại dịch sâu hại bảo vệ thảm thực vật cho toàn bộ hệ sinh thái!". Bố cục: Bức tranh toàn cảnh hệ sinh thái: chim Tu Hú bay lượn bảo vệ cánh rừng xanh ngát khỏi đại dịch sâu bọ; bên dưới các loài chim chủ tiến hóa đôi mắt tinh tường hơn qua các thế hệ.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tòa tuyên án: Bị cáo Chim Tu Hú không có tội! Đó là quy luật sinh tồn nghiệt ngã nhưng hoàn hảo của tự nhiên!". Bố cục: chú cú mèo già thẩm phán đội tóc giả trắng tòa án Anh, mặc áo choàng đen, tay cầm búa gỗ gõ búa dứt khoát mỉm cười; chú chim Tu Hú trưởng thành hoạt hình lông đốm hoa râm xám tro, mắt đỏ tròn tinh ranh, đeo chiếc nơ bướm màu tím than trên cổ, biểu cảm tự tin láu cá mừng rỡ vỗ cánh thở phào nhẹ nhõm; cả tòa án vỗ tay rộn rã trước phán quyết công bằng.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vụ án thế kỷ của Siêu Trộm Tổ Ấm đã chính thức khép lại với phán quyết đầy tính nhân văn!". Bố cục: Khung cảnh phiên tòa mờ dần về sau; ánh đèn sân khấu tập trung vào một chiếc màn hình chiếu lớn ở chính giữa sân khấu mang màu sắc bí ẩn kịch tính. KHÔNG có chim Tu Hú trưởng thành trong cảnh này.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng ngay lúc này, xin mời quý vị khán giả hãy hướng mắt lên màn hình lớn để chiêm ngưỡng BÓNG ĐEN BÍ ẨN của nhân vật sẽ xuất hiện trong Tập 15 tiếp theo!". Bố cục: Chiếc màn hình lớn bật sáng với hào quang màu vàng hổ phách huyền ảo: Ở GIỮA là BÓNG ĐEN BÍ ẨN (solid black silhouette) hình dáng một loài động vật gặm nhấm to tròn mũm mĩm kèm một dấu hỏi chấm '?' khổng lồ. KHÔNG có chim Tu Hú trưởng thành trong cảnh này.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Xin gửi tới quý vị ba manh mối chấn động về nhân vật bí ẩn này: Thứ nhất, đây là vị Bộ trưởng Ngoại giao hòa bình nhất hành tinh, dù nằm giữa đàn cá sấu ăn thịt khổng lồ hay đàn trăn gấm Nam Mỹ thì vẫn thảnh thơi nằm ngửa bụng ngủ ngon lành mà chẳng có ai thèm tấn công!". Bố cục: Manh mối số 1: BÓNG ĐEN BÍ ẨN đang nằm thảnh thơi nhắm mắt ngủ ngon lành ngay giữa bầy cá sấu ăn thịt khổng lồ đang há miệng mà không con nào thèm cắn. KHÔNG có chim Tu Hú trưởng thành trong cảnh này.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thứ hai, đây là siêu quái kiệt gặm nhấm lớn nhất thế giới với cân nặng lên tới 65kg, sở hữu tài bơi lặn cừ khôi và có thể nín thở dưới đáy sông suốt 5 phút đồng hồ!". Bố cục: Manh mối số 2: BÓNG ĐEN BÍ ẨN đứng trên bàn cân hiển thị 65kg, đang bơi lặn thong thả dưới đáy sông với đôi chân màng và đồng hồ đếm nín thở 5 phút. KHÔNG có chim Tu Hú trưởng thành trong cảnh này.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và thứ 3, một nghịch lý cực kỳ khó đỡ: thói quen ăn lại chính phân của mình vào mỗi buổi sáng sớm để hấp thu dinh dưỡng! Quý vị khán giả". Bố cục: Manh mối số 3: BÓNG ĐEN BÍ ẨN với biểu cảm 'tĩnh tâm khó đỡ' bên tách trà sáng sớm, góc dưới một chi tiết hài hước tái hấp thu dinh dưỡng để sinh tồn. KHÔNG có chim Tu Hú trưởng thành trong cảnh này.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "có nhận ra bóng đen bí ẩn mang phong thái ung dung tự tại này là ai không? Hãy để lại dự đoán của bạn ngay dưới phần bình luận nhé!". Bố cục: BÓNG ĐEN BÍ ẨN to lớn đứng giữa màn hình với dấu hỏi chấm '?' nhấp nháy phát sáng; xung quanh là các bong bóng bình luận '? ? ?' kêu gọi khán giả trổ tài dự đoán. KHÔNG có chim Tu Hú trưởng thành trong cảnh này.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phóng viên phiên tòa xin chào tạm biệt và hẹn gặp lại quý vị trong tập tiếp theo!". Bố cục: BÊN TRÁI thẩm phán và các nhân vật chim vẫy cánh chào tạm biệt; BÊN PHẢI tấm biển gỗ đề chữ 'HẸN GẶP LẠI Ở TẬP 15 VỚI VỊ BỘ TRƯỞNG NGOẠI GIAO!'. KHÔNG có chim Tu Hú trưởng thành trong cảnh này.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu gửi mẫu trứng này đi giám định ở phòng thí nghiệm hình sự, bảo đảm các chuyên gia cũng phải hoa mắt chóng mặt mới phân biệt nổi!". Bố cục: Phòng giám định hình sự thế giới tự nhiên: một bác chim cú đeo kính lúp soi từng chấm đốm trên hai quả trứng, toát mồ hôi vì quá khó phân biệt. KHÔNG có chim Tu Hú trưởng thành trong cảnh này.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một là để khi chim mẹ thả rơi vội vã từ trên cao xuống đáy tổ lót đá nó không bị nứt vỡ; và hai là nếu chim chủ nhà có sinh nghi dùng mỏ mổ thử, quả trứng Tu Hú vẫn trơ trơ như đá tảng khiến chim chủ đành bất lực chấp nhận ấp tiếp!". Bố cục: Chim Tu Hú mẹ thả rơi quả trứng từ trên cao xuống đáy tổ lót đầy đá cuội mà quả trứng vẫn nguyên vẹn không sứt mẻ; chim chủ nhà mổ mỏ vào kêu 'cốp cốp' bất lực. KHÔNG có chim Tu Hú trưởng thành trong cảnh này.
```
</details>

<details><summary>L62</summary>

```text
HÌNH L62 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "suốt 2-3 ngày đêm ròng rã, hất sạch toàn bộ trứng hoặc chim non của chủ nhà rơi xuống vực thẳm cho đến khi trong tổ chỉ còn lại duy nhất một mình nó độc chiếm ngai vàng! Quả là một bản năng sinh tồn lạnh lùng đến rợn tóc gáy!". Bố cục: Chú chim non chú chim Tu Hú non sơ sinh đỏ hỏn không một cọng lông, mắt nhắm nghiền, trên lưng có vết lõm rõ rệt hình chiếc thìa một mình nằm thảnh thơi chiếm trọn chiếc tổ êm ấm; xung quanh là vương miện nhỏ tượng trưng cho vị vua độc tôn của chiếc tổ.
```
</details>

<details><summary>L63</summary>

```text
HÌNH L63 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vòm họng đỏ rực ấy phát ra tín hiệu thị giác mãnh liệt đến mức thôi miên não bộ của chim bố mẹ, khiến chúng không tài nào cưỡng lại được mệnh lệnh phải nhét mồi vào!". Bố cục: Tia sóng thị giác màu đỏ và vàng phóng ra từ vòm họng chú chim Tu Hú non khổng lồ béo tròn lông xù to gấp 3 lần chim bố mẹ, mỏ há toang đỏ rực viền vàng như hố ga làm hai mắt của đôi chim bố mẹ xoay tròn như bị thôi miên mê mẩn.
```
</details>

<details><summary>L64</summary>

```text
HÌNH L64 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thậm chí chim mẹ nhỏ xíu phải đậu hẳn lên đầu, lên lưng của con Tu Hú khổng lồ để với tới cái mỏ há to của nó, tạo nên một cảnh tượng bi hài bậc nhất trần đời!". Bố cục: Cảnh tượng bi hài: cô chim mẹ nhỏ xíu phải đậu hẳn lên đỉnh đầu con Tu Hú khổng lồ chú chim Tu Hú non khổng lồ béo tròn lông xù to gấp 3 lần chim bố mẹ, mỏ há toang đỏ rực viền vàng như hố ga để cúi xuống nhét con sâu béo múp vào mỏ nó.
```
</details>

<details><summary>L65</summary>

```text
HÌNH L65 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hóa ra, sau khi đẻ trộm trứng vào tổ người khác, chim Tu Hú mẹ không hề bỏ đi xa mà luôn lén lút nấp ở cành cây gần đó để theo dõi diễn biến, y hệt một tên trùm mafia đang giám sát đàn em!". Bố cục: Cận cảnh chim Tu Hú mẹ nấp sau chùm lá rậm rạp, mắt đỏ rực nhìn chăm chú xuống chiếc tổ chim chích như trùm mafia đang giám sát mục tiêu.
```
</details>

<details><summary>L66</summary>

```text
HÌNH L66 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó mổ nát toàn bộ số trứng còn lại của chim chủ nhà, cắn chết những con chim non vừa nở và giật sập tan tành cả chiếc tổ để dằn mặt!". Bố cục: Cảnh tượng hung bạo: chim Tu Hú mẹ đập cánh điên cuồng, dùng mỏ nhọn mổ nát trứng chim chủ và hất tung cành rơm giật sập tan tành chiếc tổ.
```
</details>

<details><summary>L67</summary>

```text
HÌNH L67 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đối mặt với họng súng mafia tàn nhẫn như vậy, chim chủ nhà đành phải ngậm đắng nuốt cay nuôi giùm con kẻ thù để bảo toàn tính mạng!". Bố cục: Đôi chim chích ngậm đắng nuốt cay đứng canh tổ với vẻ mặt cam chịu, bên trên là bóng lưng chim Tu Hú mẹ đậu lù lù bảo kê đe dọa. KHÔNG có chim Tu Hú trưởng thành trong cảnh này.
```
</details>

<details><summary>L68</summary>

```text
HÌNH L68 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đồng thời, sự lừa đảo tinh vi của Tu Hú cũng chính là động lực thúc đẩy các loài chim chủ tiến hóa thị giác tinh tường hơn và bộ não nhạy bén hơn qua hàng triệu năm qua chạy đua vũ trang tiến hóa!". Bố cục: Cuộc chạy đua vũ trang tiến hóa: một bên chim Tu Hú cầm bảng vẽ hoa văn trứng giả mạo ngày càng tinh xảo, một bên chim chủ nhà đeo kính viễn vọng soi xét ngày càng tinh tường.
```
</details>

<details><summary>L69</summary>

```text
HÌNH L69 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đột nhập đẻ trộm trứng trong 10 giây; Sát thủ sơ sinh mù mắt đẩy trứng chủ nhà rơi xuống đất; Thao túng tâm lý bắt cha mẹ nuôi bón mồi cho đứa con to gấp 3 lần; Và chiến thuật mafia đập phá tổ để trả thù!". Bố cục: Cận cảnh 4 tội danh được chiếu đèn pha đỏ: hình minh họa đẻ trộm 10 giây, hất vỡ trứng, con nuôi khổng lồ và đập phá tổ mafia dằn mặt. KHÔNG có chim Tu Hú trưởng thành trong cảnh này.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bị cáo, mời đứng lên!". Bố cục: KHUNG HÌNH DỌC 9:16: chú cú mèo già thẩm phán đội tóc giả trắng tòa án Anh, mặc áo choàng đen, tay cầm búa gỗ gõ mạnh búa gỗ xuống bàn tòa án uy nghiêm, dòng chữ lớn 'BỊ CÁO, MỜI ĐỨNG LÊN!' xuất hiện nổi bật phía trên.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Một loài chim không bao giờ xây tổ, không ấp trứng, không nuôi con,". Bố cục: KHUNG HÌNH DỌC 9:16: chú chim Tu Hú trưởng thành hoạt hình lông đốm hoa râm xám tro, mắt đỏ tròn tinh ranh, đeo chiếc nơ bướm màu tím than trên cổ, biểu cảm tự tin láu cá đứng trên cành cây với nụ cười bí hiểm, xung quanh là những chiếc tổ chim trống trơn không ấp trứng.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đó chính là Chim Tu Hú, kẻ lừa đảo khét tiếng bậc nhất thế giới tự nhiên.". Bố cục: KHUNG HÌNH DỌC 9:16: Chân dung chú chim Tu Hú trưởng thành hoạt hình lông đốm hoa râm xám tro, mắt đỏ tròn tinh ranh, đeo chiếc nơ bướm màu tím than trên cổ, biểu cảm tự tin láu cá lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, bên cạnh là tấm lệnh truy nã 'SIÊU TRỘM TỔ ẤM'.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Chim mẹ chỉ mất đúng 10 giây để đột nhập tổ chim chích, nuốt chửng một quả trứng của chủ nhà". Bố cục: KHUNG HÌNH DỌC 9:16: Chim Tu Hú mẹ sà xuống tổ chim chích, một đồng hồ bấm giờ đếm ngược 10 giây phát sáng chớp nhoáng.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "và đẻ thay vào đó quả trứng của mình với hoa văn giả mạo giống tới 99%!". Bố cục: KHUNG HÌNH DỌC 9:16: So sánh hai quả trứng đặt cạnh nhau trong tổ, hoa văn đốm nâu giống nhau 99% đến mắt thường không phân biệt nổi.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đáng sợ hơn cả, con non vừa nở chỉ nặng 2g, mắt còn nhắm nghiền chưa mở,". Bố cục: KHUNG HÌNH DỌC 9:16: chú chim Tu Hú non sơ sinh đỏ hỏn không một cọng lông, mắt nhắm nghiền, trên lưng có vết lõm rõ rệt hình chiếc thìa sơ sinh đỏ hỏn nặng 2g nằm trong tổ, mắt nhắm nghiền nhưng toát ra luồng khí sát thủ rùng mình.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "nhưng đã dùng chiếc lưng lõm bẩm sinh gồng mình". Bố cục: KHUNG HÌNH DỌC 9:16: Cận cảnh chiếc lưng lõm hình thìa của chú chim Tu Hú non sơ sinh đỏ hỏn không một cọng lông, mắt nhắm nghiền, trên lưng có vết lõm rõ rệt hình chiếc thìa đang cõng một quả trứng chim chủ to đùng leo lên thành tổ.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "hất tung toàn bộ trứng của chim chủ nhà rơi xuống đất vỡ nát!". Bố cục: KHUNG HÌNH DỌC 9:16: chú chim Tu Hú non sơ sinh đỏ hỏn không một cọng lông, mắt nhắm nghiền, trên lưng có vết lõm rõ rệt hình chiếc thìa ưỡn lưng hất văng quả trứng chim chủ rơi tự do xuống dưới vực vỡ tan tành thành từng mảnh.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Để rồi sau đó, đứa con nuôi khổng lồ lớn nhanh như thổi, to gấp 3 lần chim bố mẹ,". Bố cục: KHUNG HÌNH DỌC 9:16: chú chim Tu Hú non khổng lồ béo tròn lông xù to gấp 3 lần chim bố mẹ, mỏ há toang đỏ rực viền vàng như hố ga khổng lồ lông xù to gấp 3 lần chim bố mẹ, ngồi chật ních làm tổ chim muốn gãy đôi.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "há to chiếc miệng đỏ lòm như hố ga thôi miên cha mẹ nuôi phải hầu hạ mớm mồi suốt ngày đêm!". Bố cục: KHUNG HÌNH DỌC 9:16: chú chim Tu Hú non khổng lồ béo tròn lông xù to gấp 3 lần chim bố mẹ, mỏ há toang đỏ rực viền vàng như hố ga há ngoác chiếc miệng đỏ rực viền vàng như hố ga; chim mẹ nhỏ xíu đậu trên đầu sợ hãi nhét mồi vào.
```
</details>

<details><summary>S11</summary>

```text
HÌNH S11 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Vậy là vụ án đã sáng tỏ: một chiến thuật ký sinh tàn nhẫn". Bố cục: KHUNG HÌNH DỌC 9:16: chú chim Tu Hú trưởng thành hoạt hình lông đốm hoa râm xám tro, mắt đỏ tròn tinh ranh, đeo chiếc nơ bướm màu tím than trên cổ, biểu cảm tự tin láu cá đứng kiêu hãnh trên cành cây cổ thụ giữa rừng già xanh ngát, nhìn về phía chân trời xa xôi suy tư.
```
</details>

<details><summary>S12</summary>

```text
HÌNH S12 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "nhưng lại sở hữu bản năng sát thủ ngay từ giây phút đầu tiên chui ra khỏi vỏ!". Bố cục: KHUNG HÌNH DỌC 9:16: Cận cảnh chú chim Tu Hú non sơ sinh toát ra ánh hào quang sát thủ sắc bén ngay khi vừa phá vỏ trứng.
```
</details>

<details><summary>S13</summary>

```text
HÌNH S13 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú chim Tu Hú lông đốm xám tro nơ tím than; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "nhưng là cách sinh tồn hoàn hảo giúp loài chim này trường tồn qua hàng triệu năm qua!". Bố cục: KHUNG HÌNH DỌC 9:16: Toàn cảnh rừng già rạng ngời ánh bình minh, muôn loài chim cùng chung sống hòa hợp khép lại câu chuyện trọn vẹn.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/67 của video YouTube về Chim Tu Hú). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú chim Tu Hú trưởng thành hoạt hình lông đốm hoa râm xám tro, mắt đỏ tròn tinh ranh, đeo chiếc nơ bướm màu tím than trên cổ, biểu cảm tự tin láu cá. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/13 của video YouTube Shorts về Chim Tu Hú). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú chim Tu Hú trưởng thành hoạt hình lông đốm hoa râm xám tro, mắt đỏ tròn tinh ranh, đeo chiếc nơ bướm màu tím than trên cổ, biểu cảm tự tin láu cá. 
```
</details>

## 7. SEO

- **title:** Bản Năng Sát Thủ Của Chim Non Chưa Mở Mắt?! | Chim Tu Hú | Tập 14
- **hook_paragraph:** Chim Tu Hú đẻ trộm trứng trong 10 giây, ngụy trang hoa văn 99%, con non mù mắt hất vỡ toàn bộ trứng chủ nhà và còng lưng nuôi con to gấp 3 lần! Khám phá hồ sơ vụ án chấn động của Siêu Trộm Tổ Ấm tại Tòa án Tối cao thế giới tự nhiên.
- **question:** Bạn có đoán ra BÓNG ĐEN BÍ ẨN ở cuối video là quái kiệt nào không? (Gợi ý: Bộ trưởng Ngoại giao hòa bình, nằm cạnh cá sấu, nặng 65kg). Bình luận dự đoán nhé!
- **next_teaser:** Bóng đen bí ẩn — vị Bộ trưởng Ngoại giao hòa bình nằm cạnh cá sấu và quái kiệt gặm nhấm 65kg
- **shorts_title:** Bản Năng Sát Thủ Của Chim Non Chưa Mở Mắt?! 🐣 #shorts #chimtuhu
- **shorts_desc:** Chim Tu Hú đẻ trộm trứng trong 10 giây và chim non mới nở chưa mở mắt đã biết hất sạch trứng chủ nhà khỏi tổ! Khám phá bí mật sinh tồn của Siêu Trộm Tổ Ấm! 🐣⚖️
- **bullets:** Đột nhập và đẻ trộm trứng thần tốc chỉ trong 10 giây · Sát thủ sơ sinh chưa mở mắt dùng lưng lõm hất trứng rơi tự do · Thao túng tâm lý bằng siêu kích thích họng đỏ, con to gấp 3 lần cha mẹ nuôi · Chiến thuật mafia bảo kê đập phá tổ nếu chim chủ dám vứt trứng
- **tags:** chim tu hú, chim tu hu, cuckoo, chim tu hú đẻ trộm trứng, bản năng sát thủ chim non, chim tu hú nuôi con, thế giới động vật, động vật kỳ lạ, vẽ chuyện hoang dã, whiteboard animation, khoa học thú vị, phiên tòa động vật
- **hashtags:** #ChimTuHu #Cuckoo #TheGioiDongVat #VeChuyenHoangDa #KhoaHoc

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-14-chim-tu-hu
python src/episode/pipeline.py tts    projects/tap-14-chim-tu-hu     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-14-chim-tu-hu     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-14-chim-tu-hu     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-14-chim-tu-hu              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-14-chim-tu-hu --force
python scripts/beat_sheet.py projects/tap-14-chim-tu-hu               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-14-chim-tu-hu/audio/shorts.wav projects/tap-14-chim-tu-hu/renders/tap-14-chim-tu-hu_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-14-chim-tu-hu
python src/episode/pipeline.py seo    projects/tap-14-chim-tu-hu
python src/episode/episode_doc.py     projects/tap-14-chim-tu-hu
```

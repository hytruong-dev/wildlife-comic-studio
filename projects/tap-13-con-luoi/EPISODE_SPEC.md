# TẬP 13 — CON LƯỜI · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-13-con-luoi`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-13-con-luoi`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F4` · **Persona giọng:** `phong_vien_24h` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Con Lười |
| Tiêu đề YouTube | Tại Sao 50% Cái Chết Của Con Lười Xảy Ra Lúc Đi Vệ Sinh?! \| Con Lười \| Tập 13 |
| Video dài | `renders/tap-13-con-luoi_long.mp4` — 9:18.1 (558.1s) |
| Shorts | `renders/tap-13-con-luoi_shorts.mp4` — 0:48.6 (48.6s) |
| Thumbnail | `renders/tap-13-con-luoi_thumbnail.jpg` |
| Số hình | dài 61 beat / 61 ảnh riêng; Shorts 12 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/61 của video YouTube về Con Lười). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân. Nhân vật phụ cố định: anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H; cô phát thanh viên tin tức hoạt hình xinh đẹp ngồi sau bàn trường quay thời sự. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — 00 SÁNG: TỐC ĐỘ 0,24 KM/H VÀ KỶ LỤC 30 NGÀY TIÊU HÓA 1 CHIẾC LÁ
*Thẻ chương:* BẮT ĐẦU NGÀY MỚI CỦA THÁNH SỐNG CHẬM

*Badge:* `06:00 SÁNG` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene01_p0.wav` (535 ký tự) · mood `hao_hung`

```text
Bây giờ là không sáu giờ sáng! Kính thưa quý vị khán giả, chúng tôi đang có mặt trực tiếp tại tán rừng rậm nhiệt đới Cô-xta Ri-ca để tường thuật lại một ngày làm việc siêu chậm chạp của sinh vật lười biếng nhất hành tinh: Con Lười ba ngón! Chiếc đồng hồ báo thức vừa rung chuông điểm sáng, và nhân vật chính của chúng ta — Thánh sống chậm — dường như vẫn bất động hoàn toàn như một bọc rơm khô treo trên cành cây! Để di chuyển được một bước chân ngắn ngủn vài xăng-ti-mét, gã này mất tới vài phút đồng hồ suy nghĩ và đắn đo! [laughter]
```
**Part 1** → `audio/vs/scene01_p1.wav` (96 ký tự) · 🎭 cameo `phat_thanh_vien`

```text
Alo trường quay nghe rõ không? Phóng viên cho hỏi sinh vật này bò nhanh nhất được bao nhiêu vậy?
```
**Part 2** → `audio/vs/scene01_p2.wav` (666 ký tự) · mood `don_dap`

```text
[surprise-oh] Báo cáo trường quay, tốc độ kỷ lục của nó trên ngọn cây chỉ đạt vỏn vẹn không phẩy hai mươi tư cây số một giờ — tức là khoảng bốn mét mỗi phút! Còn nếu rơi xuống đất thì chỉ lết được chừng hai mét một phút, chậm đến mức một con ốc sên bò qua mặt cũng có thể bấm còi vượt mặt dễ dàng! [laughter] Nhưng điều kinh ngạc nhất nằm ở bộ máy tiêu hóa bên trong: dạ dày của Thánh sống chậm có cấu tạo bốn ngăn phức tạp y hệt loài trâu bò, nhưng quá trình trao đổi chất lại chậm nhất thế giới động vật có vú. Để tiêu hóa hết một chiếc lá cây duy nhất, dạ dày của nó phải làm việc cật lực ròng rã suốt ba mươi ngày trời, thậm chí có thể kéo dài tới năm mươi ngày!
```
**Part 3** → `audio/vs/scene01_p3.wav` (431 ký tự) · mood `hao_hung`

```text
Chính vì tiêu hóa chậm kỷ lục như vậy, nhiệt độ cơ thể của Con Lười dao động thất thường từ ba mươi đến ba mươi bốn độ C, phụ thuộc hoàn toàn vào ánh nắng mặt trời y như các loài bò sát! Nếu thức ăn trong dạ dày không kịp lên men mà gặp trời lạnh giá, Con Lười thậm chí có thể... chết đói ngay khi chiếc bụng vẫn đang căng tròn đầy ắp lá cây! Hãy cùng chúng tôi đếm ngược từng mốc giờ để chứng kiến cuộc đời kỳ lạ của sinh vật này!
```

### scene02 — 00 TRƯA: CHIẾC CỔ XOAY 270 ĐỘ VÀ BÀN TAY KHÓA TỰ ĐỘNG KHI CHẾT
*Thẻ chương:* CHIẾC CỔ CÚ VỌ VÀ MÓNG VUỐT KHÓA CHẾT

*Badge:* `12:00 TRƯA` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene02_p0.wav` (439 ký tự) · mood `don_dap`

```text
Đồng hồ điểm mười hai giờ trưa! Ánh nắng nhiệt đới chiếu rọi thẳng đứng qua kẽ lá, và đây là lúc Thánh sống chậm bắt đầu phơi mình sưởi nắng để kích hoạt lò tiêu hóa trong bụng. Quý vị hãy nhìn vào chuyển động đầu của nó: trong khi toàn bộ cơ thể vẫn giữ nguyên tư thế treo ngược bất động, chiếc đầu của Con Lười bỗng nhiên quay tít một góc hai trăm bảy mươi độ cực kỳ mượt mà chẳng khác nào một chú chim cú vọ giữa ban ngày! [surprise-wa]
```
**Part 1** → `audio/vs/scene02_p1.wav` (108 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Bác phóng viên ơi, cổ con người chỉ quay được chín mươi độ thôi, sao gã này quay gần trọn vòng tròn hay vậy?
```
**Part 2** → `audio/vs/scene02_p2.wav` (485 ký tự) · mood `hao_hung`

```text
Bí mật nằm ở bộ xương cổ độc nhất vô nhị các bạn nhỏ ạ! Trong khi hầu hết các loài động vật có vú trên Trái Đất — từ con chuột nhắt bé tí cho đến hươu cao cổ dài ngoằng — đều chỉ có đúng bảy đốt sống cổ, thì loài lười ba ngón lại tiến hóa sở hữu từ tám đến mười đốt sống cổ! Cấu trúc xương cổ kỳ lạ này cho phép nó quay đầu hai trăm bảy mươi độ ra sau lưng để gặm những chiếc lá non xung quanh mà không cần phải tốn chút sức lực nào để xoay chuyển cả thân mình cồng kềnh! [surprise-oh]
```
**Part 3** → `audio/vs/scene02_p3.wav` (708 ký tự) · mood `don_dap`

```text
Chưa dừng lại ở chiếc cổ cú vọ, hãy nhìn vào bốn bàn chân với những chiếc móng vuốt cong vút dài mười xăng-ti-mét! Đôi chân này không dùng để đi bộ, mà hoạt động như những chiếc móc sắt cứu hộ! Các nhà giải phẫu học phát hiện cơ bắp của Con Lười chiếm chưa đầy ba mươi phần trăm trọng lượng cơ thể, nhưng các đường gân ở ngón chân lại có cơ chế khóa ngàm tự động cực kỳ tinh vi: khi treo lên cành cây, trọng lượng cơ thể tự kéo căng các gân móng bấm chặt vào cành gỗ mà không hề tiêu tốn một chút calo cơ bắp nào! Lực khóa này mạnh đến mức ngay cả khi một con lười đã qua đời vì tuổi già, cơ thể của nó vẫn tiếp tục treo ngược lơ lửng trên cành cây nhiều ngày liền mà không hề bị rơi xuống đất! [surprise-wa]
```
**Part 4** → `audio/vs/scene02_p4.wav` (537 ký tự) · mood `hao_hung`

```text
Không những thế, Thánh sống chậm còn sở hữu siêu năng lực chịu đòn ngã cây vô địch! Vì thường xuyên leo trèo trên những cành cây mục ướt sũng, các nhà nghiên cứu ghi nhận mỗi con lười trong đời bị ngã từ độ cao mười lăm mét đến ba mươi mét xuống đất cả chục lần! Nhưng nhờ các khớp xương dẻo dai và khung xương sườn đàn hồi kỳ lạ, chúng ngã rơi tự do đánh bịch xuống đất mà hầu như không bao giờ bị gãy xương! Ngã xong, chú lười chỉ việc chớp chớp mắt rồi lại từ từ lết lên thân cây leo tiếp như chưa từng có chuyện gì xảy ra! [laughter]
```

### scene03 — 00 HOÀNG HÔN: HỆ SINH THÁI DI ĐỘNG TRÊN LƯNG VÀ BIỆT TÀI BƠI LỘI
*Thẻ chương:* MẢNH VƯỜN SINH THÁI TỰ NHIÊN TRÊN BỘ LÔNG

*Badge:* `18:00 HOÀNG HÔN` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene03_p0.wav` (508 ký tự) · mood `tram_bi_an`

```text
Bầu trời hoàng hôn buông sắc tím thẫm trên dòng sông, đồng hồ điểm mười tám giờ tối! Khi nhìn cận cảnh vào lớp lông xơ xác màu xám bùn của Thánh sống chậm, chúng tôi phải thốt lên kinh ngạc: đây không phải là một con vật đơn thuần, mà là cả một hệ sinh thái rừng rậm thu nhỏ đang di động! [surprise-oh] Quý vị có thấy những vệt màu xanh lục phủ kín khắp lưng và đầu của nó không? Đó không phải là màu lông bẩm sinh, mà là một thảm tảo xanh sống ký sinh ngay trên các rãnh nứt siêu nhỏ của từng sợi lông lười!
```
**Part 1** → `audio/vs/scene03_p1.wav` (628 ký tự) · mood `hao_hung`

```text
Thảm tảo xanh này được bón phân và chăm sóc bởi một đội quân cư dân đặc quyền: loài bướm đêm Cờ-ríp-tô-xét — sinh vật chỉ sống duy nhất trên bộ lông của Con Lười mà không thể tìm thấy ở bất kỳ nơi nào khác trên hành tinh! Hàng trăm con bướm đêm làm tổ, sinh sống và thải phân đạm nuôi dưỡng cho vườn tảo xanh mọc um tùm. Đổi lại, thảm tảo xanh biến Con Lười thành một búi lá cây ngụy trang hoàn hảo chống lại tầm mắt của kẻ thù từ trên cao, và những lúc đói lòng, chú lười chỉ việc liếm láp lớp tảo giàu chất béo này trên lông như một món ăn vặt bổ dưỡng! Một phi vụ làm ăn đôi bên cùng có lợi kéo dài hàng triệu năm! [laughter]
```
**Part 2** → `audio/vs/scene03_p2.wav` (561 ký tự) · mood `don_dap`

```text
Nhưng cú sốc lớn nhất buổi chiều hôm nay chính là khả năng thể thao bất ngờ của gã lười! Khi muốn di chuyển qua bờ bên kia, Thánh sống chậm buông tay thả mình rơi tõm xuống dòng sông. Quý vị tin được không: sinh vật lết trên cạn chậm như rùa này lại bơi lội cực kỳ cừ khôi, tốc độ bơi dưới nước nhanh gấp ba đến bốn lần lúc bò trên cạn! Nó có thể nhịn thở dưới nước tới bốn mươi phút đồng hồ nhờ khả năng làm chậm nhịp tim xuống còn một phần ba! Từ một kẻ tàn tật trên cạn, nó biến thành một tay bơi lội cừ khôi vượt sông ngầu chẳng kém gì rái cá! [surprise-wa]
```

### scene04 — 00 ĐÊM: NGHI LỄ ĐI VỆ SINH TỬ THẦN VÀ CÚ GIẢM 1/3 CÂN NẶNG
*Thẻ chương:* CHUYẾN ĐI VỆ SINH SINH TỬ KÉO DÀI CẢ TIẾNG ĐỒNG HỒ

*Badge:* `22:00 ĐÊM` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene04_p0.wav` (521 ký tự) · mood `don_dap`

```text
Màn đêm bao trùm tĩnh mịch, đồng hồ điểm hai mươi hai giờ đêm! Và đây chính là khoảnh khắc hồi hộp, căng thẳng và nguy hiểm bậc nhất trong cả tuần lễ của Thánh sống chậm: chuyến hành hương xuống mặt đất để đi vệ sinh! Trong khi các loài thú khác trên cành cây chỉ việc xả phân tự do xuống đất từ trên cao, thì loài lười ba ngón lại kiên quyết tuân theo một nghi thức kỳ quặc đến mức khó hiểu: cứ đều đặn một tuần một lần, nó bắt buộc phải bò từ ngọn cây cao chót vót xuống tận mặt đất ẩm ướt để đi đại tiện! [surprise-oh]
```
**Part 1** → `audio/vs/scene04_p1.wav` (545 ký tự) · mood `bi_hai`

```text
Chuyến đi này tiêu tốn tới mười phần trăm năng lượng ít ỏi cả ngày của nó, nhưng cái giá phải trả lớn hơn thế gấp ngàn lần! Vì di chuyển quá vụng về trên mặt đất, Con Lười hoàn toàn mất đi khả năng tự vệ trước các loài thú săn mồi mặt đất. Báo cáo nghiên cứu thực địa chấn động của các nhà sinh vật học tại Cô-xta Ri-ca chỉ ra rằng: hơn năm mươi phần trăm số cái chết trong toàn bộ cuộc đời của loài lười đều diễn ra đúng vào thời điểm nó mò xuống đất đi vệ sinh! Một cái chết lãng xẹt và bi hài bậc nhất thế giới tự nhiên! [dissatisfaction-hnn]
```
**Part 2** → `audio/vs/scene04_p2.wav` (90 ký tự) · 🎭 cameo `be_con`

```text
Bác phóng viên ơi, nguy hiểm đến mất mạng như thế sao nó không ị luôn trên cây cho khỏe ạ?
```
**Part 3** → `audio/vs/scene04_p3.wav` (852 ký tự) · mood `hao_hung`

```text
Câu hỏi tuyệt vời của khán giả nhí cũng chính là điều khiến các nhà khoa học vò đầu bứt tai suốt nhiều thập kỷ! Khi xuống tới gốc cây, Con Lười dùng chiếc đuôi ngắn ngủn ngoáy một chiếc hố nhỏ trên nền đất rồi bắt đầu xả thải. Quý vị hãy chuẩn bị tinh thần: vì nhịn suốt một tuần lễ, lượng phân và nước tiểu xả ra trong một lần đi vệ sinh có thể nặng tới một phần ba trọng lượng toàn bộ cơ thể nó! Đi vệ sinh xong một cái là chú lười nhẹ bẫng đi ba mươi phần trăm cân nặng! Và mục đích sinh tử của chuyến đi này chính là để phục vụ bạn bè: khi lười đi vệ sinh, những cô bướm đêm trên lông sẽ bò xuống đẻ trứng vào đống phân tươi để ấu trùng phát triển, hoàn thành chu trình duy trì bộ lông xanh cho thế hệ lười tiếp theo! Chấp nhận đối mặt tử thần năm mươi phần trăm chỉ để giữ lời hứa với đàn bướm đêm, quả là một tình bạn sinh tử cảm động! [laughter]
```

### scene05 — 00 ĐÊM: CUỘC CHẠM TRÁN SÁT THỦ ĐẠI BÀNG HARPY VÀ CÚ CÀO TỰ VỆ
*Thẻ chương:* ĐỐI ĐẦU BẠO CHÚA BẦU TRỜI ĐẠI BÀNG HARPY

*Badge:* `02:00 ĐÊM` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene05_p0.wav` (419 ký tự) · mood `tram_bi_an`

```text
Màn đêm chuyển về khuya, đồng hồ điểm không hai giờ rạng sáng! Sau chuyến đi vệ sinh hú vía dưới mặt đất, Thánh sống chậm đã leo trở lại chạc cây an toàn. Nhưng hiểm nguy từ bầu trời lại bắt đầu rình rập! Trên tầng tán rừng nhiệt đới, kẻ thù truyền kiếp đáng sợ nhất của loài lười đã xuất hiện: Đại bàng Hác-pi — bạo chúa bầu trời châu Mỹ với sải cánh dài hơn hai mét và bộ móng vuốt to bằng móng gấu xám! [surprise-wa]
```
**Part 1** → `audio/vs/scene05_p1.wav` (667 ký tự) · mood `don_dap`

```text
Đại bàng Hác-pi chuyên lượn sát các ngọn cây để săn lùng khỉ và lười. Nhưng chính tốc độ rùa bò và bộ lông mọc rêu xanh lại trở thành tấm áo giáp tàng hình siêu việt cứu mạng Thánh sống chậm! Đại bàng bay lướt qua phía trên chỉ thấy một búi lá cây đung đưa bất động trong gió đêm. Và quý vị đừng tưởng chú lười hiền lành này không biết phản kháng nhé! Khi bị dồn vào chân tường, Con Lười có thể tung ra những cú cào vuốt móng thép sắc lẹm với tốc độ cực nhanh, đủ sức rạch toạc da thịt của kẻ săn mồi khiến báo đốm hay đại bàng cũng phải dè chừng lùi bước! Chậm chạp có tính toán, bất động để sinh tồn, đó là bản lĩnh của kẻ sống sót qua hàng triệu năm! [surprise-oh]
```
**Part 2** → `audio/vs/scene05_p2.wav` (482 ký tự) · mood `am_ap`

```text
Và tình mẫu tử của loài lười cũng cảm động không kém! Chú lười con sinh ra chỉ nhỏ xíu bằng nắm tay, bám chặt vào ngực mẹ suốt sáu tháng trời ròng rã không rời nửa bước! Người mẹ lười dù chậm chạp đến đâu cũng sẽ bảo vệ con mình trước nanh vuốt của thú dữ, sẵn sàng giơ những chiếc móng vuốt mười xăng-ti-mét sắc nhọn rạch toạc mặt bất kỳ kẻ săn mồi nào dám đụng vào đứa con bé bỏng! Chậm chạp nhưng không hề yếu hèn, đó chính là bản lĩnh sinh tồn của Thánh sống chậm! [surprise-oh]
```

### scene06 — 00 RẠNG SÁNG: TRIẾT LÝ SỐNG CHẬM ĐỈNH CAO VÀ BÓNG ĐEN BÍ ẨN TẬP 14
*Thẻ chương:* BẬT MÍ BÓNG ĐEN BÍ ẨN CỦA QUÁI KIỆT TẬP 14

*Badge:* `04:00 SÁNG` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (603 ký tự) · mood `am_ap`

```text
Bây giờ là không bốn giờ rạng sáng! Ánh bình minh le lói bắt đầu rọi xuống tán rừng già, khép lại hai mươi tư giờ tác nghiệp đầy cảm xúc theo chân Thánh sống chậm. Nhiều người thường lấy con lười ra làm biểu tượng cho sự lười nhác và thụt lùi, nhưng thực tế tiến hóa đã chứng minh: lối sống chậm rãi, tối giản hóa năng lượng và không tranh giành thức ăn với bất kỳ ai đã giúp Con Lười tồn tại bền bỉ qua hơn ba mươi triệu năm lịch sử! Đôi khi trong cuộc sống hối hả, biết sống chậm lại, tĩnh tâm và kiên định với con đường của riêng mình lại là cách sinh tồn thông minh và khôn ngoan nhất! [surprise-oh]
```
**Part 1** → `audio/vs/scene06_p1.wav` (243 ký tự) · mood `hao_hung`

```text
Hành trình hai mươi tư giờ của Thánh sống chậm đã chính thức khép lại! Nhưng ngay bây giờ, xin mời quý vị khán giả hãy hướng mắt lên màn hình lớn để chiêm ngưỡng BÓNG ĐEN BÍ ẨN của nhân vật xuất hiện trong Tập mười bốn tiếp theo! [surprise-oh]
```
**Part 2** → `audio/vs/scene06_p2.wav` (551 ký tự) · mood `don_dap`

```text
Xin gửi tới quý vị ba manh mối chấn động về bóng đen bí ẩn này: Thứ nhất, đây là siêu tội phạm lừa đảo khét tiếng bậc nhất thế giới loài chim, với tuyệt kỹ đẻ trộm trứng vào tổ của loài chim khác chỉ trong vỏn vẹn mười giây! Thứ hai, bản năng sát thủ tàn nhẫn đến rợn người: con non vừa chui ra khỏi vỏ trứng, mắt còn chưa mở, nhưng đã dùng chiếc lưng lõm hất tung toàn bộ trứng của chim chủ nhà rơi xuống đất vỡ nát! Và thứ ba, nghịch lý bi hài: đôi chim bố mẹ nuôi còng lưng bón mồi cho một đứa con nuôi khổng lồ to gấp ba lần chính mình! [laughter]
```
**Part 3** → `audio/vs/scene06_p3.wav` (244 ký tự) · mood `hao_hung`

```text
Quý vị khán giả có đoán ra bóng đen bí ẩn này là quái kiệt nào không? Hãy để lại phán quyết và dự đoán của bạn ngay dưới phần bình luận nhé! Phóng viên truyền hình xin chào tạm biệt và hẹn gặp lại quý vị trong bản tin sinh tồn kỳ thú tiếp theo!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Một sinh vật lười biếng đến mức mất cả tháng trời chỉ để tiêu hóa một chiếc lá cây, nhưng mỗi tuần lại chấp nhận mạo hiểm tính mạng để làm một việc kỳ quặc! Đó chính là Con Lười ba ngón, thánh sống chậm của rừng rậm Nam Mỹ với tốc độ chỉ không phẩy hai cây số một giờ. Dạ dày bốn ngăn trao đổi chất cực chậm khiến một chiếc lá phải mất ba mươi ngày mới tiêu hóa xong, còn bộ lông phủ đầy tảo xanh biến nó thành một khu rừng di động cho hàng trăm con bướm đêm sinh sống. [surprise-wa] Nhưng kỳ lạ nhất là cứ đúng một tuần một lần, nó bắt buộc phải bò từ ngọn cây xuống đất để đi vệ sinh, xả tới một phần ba trọng lượng cơ thể! [laughter] Do di chuyển quá vụng về dưới đất, hơn năm mươi phần trăm số cái chết của loài lười đều diễn ra đúng vào thời điểm đi vệ sinh này! Vậy là bí mật đã rõ: con lười chấp nhận đối mặt với tử thần chỉ để bướm đêm trên lưng có chỗ đẻ trứng vào phân, giữ cho bộ lông luôn xanh ngụy trang để sinh tồn qua hàng triệu năm!
```

**Whisper prompt:** `Con Lười, Thánh sống chậm, Sloth, Bradypus, 06:00, 12:00, 18:00, 22:00, 02:00, 04:00, 0.24km/h, 270 độ, 30 ngày, 1/3 trọng lượng, bướm đêm Cryptoses, tảo xanh, đại bàng Harpy, Costa Rica, bóng đen bí ẩn, Chim Tu Hú`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| không sáu giờ | 06:00 |
| mười hai giờ | 12:00 |
| mười tám giờ | 18:00 |
| hai mươi hai giờ | 22:00 |
| không hai giờ | 02:00 |
| không bốn giờ | 04:00 |
| hai mươi tư tiếng | 24 tiếng |
| hai mươi tư trên bảy | 24/7 |
| không phẩy hai mươi tư cây số một giờ | 0,24km/h |
| không phẩy hai cây số một giờ | 0,2km/h |
| bốn mét | 4m |
| hai mét | 2m |
| ba đến bốn lần | 3-4 lần |
| ba lần | 3 lần |
| bốn lần | 4 lần |
| bốn ngăn | 4 ngăn |
| một tháng | 1 tháng |
| ba mươi ngày | 30 ngày |
| năm mươi ngày | 50 ngày |
| bảy ngày | 7 ngày |
| tám ngày | 8 ngày |
| một tuần | 1 tuần |
| một lần | 1 lần |
| một phần ba | 1/3 |
| ba mươi phần trăm | 30% |
| ba mươi lăm phần trăm | 35% |
| năm mươi phần trăm | 50% |
| mười phần trăm | 10% |
| bốn mươi phút | 40 phút |
| hai trăm bảy mươi độ | 270° |
| tám đến mười | 8-10 |
| bảy đốt | 7 đốt |
| hàng trăm | hàng trăm |
| mười giây | 10 giây |
| Tập mười ba | Tập 13 |
| Tập mười bốn | Tập 14 |
| hàng triệu năm | hàng triệu năm |
| triệu năm | triệu năm |
| Hác-pi | Harpy |
| Cô-xta Ri-ca | Costa Rica |
| Bra-đi-pút | Bradypus |
| Cờ-ríp-tô-xét | Cryptoses |
| A-ma-dôn | Amazon |
| ba mươi đến ba mươi bốn độ C | 30-34°C |
| ba mươi độ C | 30°C |
| ba mươi bốn độ C | 34°C |
| chín mươi độ | 90° |
| hai mươi tư giờ | 24 giờ |
| ba mươi triệu năm | 30 triệu năm |
| ba mươi mét | 30m |
| mười lăm mét | 15m |
| sáu tháng | 6 tháng |
| mười xăng-ti-mét | 10cm |
| năm xăng-ti-mét | 5cm |
| năm đến tám ngày | 5-8 ngày |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · 00 SÁNG: TỐC ĐỘ 0,24 KM/H VÀ KỶ LỤC 30 NGÀY TIÊU HÓA 1 CHIẾC LÁ · 86.1s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:02.4 (2.4s) | L01 | Bây giờ là 06:00 sáng! |  | Rừng rậm nhiệt đới Costa Rica mù sương lúc 06:00 sáng: chiếc đồng hồ báo thức khổng lồ rung chuông reo sáng rực; anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H mặc áo dã ngoại cầm micro phát biểu trước máy quay. |
| b02 | 00:02.4–00:13.0 (10.5s) | L02 | Kính thưa quý vị khán giả, chúng tôi đang có mặt trực tiếp tại tán rừng rậm nhiệt đới Costa Rica để tường thuật lại một ngày làm việc siêu chậm chạp của sinh vật lười biếng nhất hành tinh: Con Lười ba ngón! |  | anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H chỉ tay lên cành cây cao: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo mộ |
| b03 | 00:13.0–00:21.9 (8.9s) | L03 | Chiếc đồng hồ báo thức vừa rung chuông điểm sáng, và nhân vật chính của chúng ta — Thánh sống chậm — dường như vẫn bất động hoàn toàn như một bọc rơm khô treo trên cành cây! |  | Đồng hồ rung chuông reo inh ỏi; chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân hé mở một bên mắt ngơ ngác, khóe miệng vẫn giữ  |
| b04 | 00:21.9–00:28.2 (6.4s) | L04 | Để di chuyển được một bước chân ngắn ngủn vài xăng-ti-mét, gã này mất tới vài phút đồng hồ suy nghĩ và đắn đo! |  | Cận cảnh bàn chân chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân nhấc lên chậm chạp từng milimet; đám mây suy nghĩ đầy các phé |
| b05 | 00:28.2–00:33.8 (5.6s) | L05 | Alo trường quay nghe rõ không? Phóng viên cho hỏi sinh vật này bò nhanh nhất được bao nhiêu vậy? |  | Trường quay thời sự: cô phát thanh viên tin tức hoạt hình xinh đẹp ngồi sau bàn trường quay thời sự đeo tai nghe ngạc nhiên chỉ vào màn hình kết nối hiện trường đặt câu hỏi. |
| b06 | 00:33.8–00:40.4 (6.6s) | L06 | Báo cáo trường quay, tốc độ kỷ lục của nó trên ngọn cây chỉ đạt vỏn vẹn 0,24km/h — tức là khoảng 4m mỗi phút! | **0,24 KM/H** · tốc độ rùa bò · R/360 · [0.65, 0.45]<br>**4M / PHÚT** · trên ngọn cây · L/480 · [0.35, 0.55] | chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân bò trên cành cây với tốc độ 0,24km/h; đồng hồ đo tốc độ xe hơi bên cạnh kim chỉ |
| b07 | 00:40.4–00:47.2 (6.8s) | L07 | Còn nếu rơi xuống đất thì chỉ lết được chừng 2m một phút, chậm đến mức một con ốc sên bò qua mặt cũng có thể bấm còi vượt mặt dễ dàng! | **2M / PHÚT** · lết dưới mặt đất · L/380 · [0.4, 0.5] | chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân lết vụng về trên mặt đất với tốc độ 2m/phút; một chú ốc sên đeo kính mát bấm cò |
| b08 | 00:47.2–00:56.4 (9.1s) | L08 | Nhưng điều kinh ngạc nhất nằm ở bộ máy tiêu hóa bên trong: dạ dày của Thánh sống chậm có cấu tạo 4 ngăn phức tạp y hệt loài trâu bò, nhưng quá trình trao đổi chất lại chậm nhất thế giới động vật có vú. |  | Sơ đồ giải phẫu dạ dày 4 ngăn phức tạp như trâu bò của lười; bên trong các mẩu lá cây nằm yên bất động, vi khuẩn lên men lười biếng. |
| b09 | 00:56.4–01:03.8 (7.5s) | L09 | Để tiêu hóa hết một chiếc lá cây duy nhất, dạ dày của nó phải làm việc cật lực ròng rã suốt 30 ngày trời, thậm chí có thể kéo dài tới 50 ngày! | **30 NGÀY** · tiêu hóa 1 chiếc lá · R/360 · [0.68, 0.5]<br>**50 NGÀY** · kéo dài tối đa · L/480 · [0.35, 0.55] | Chiếc lá cây duy nhất nằm trong dạ dày lười; tờ lịch 30 ngày rơi lả tả; một chiếc đồng hồ cát chảy cực chậm. |
| b10 | 01:03.8–01:13.5 (9.7s) | L10 | Chính vì tiêu hóa chậm kỷ lục như vậy, nhiệt độ cơ thể của Con Lười dao động thất thường từ 30-34°C, phụ thuộc hoàn toàn vào ánh nắng mặt trời y như các loài bò sát! | **30-34°C** · thân nhiệt bất ổn · L/380 · [0.35, 0.45] | chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân nằm phơi bụng trên cành cây sưởi nắng; nhiệt kế cắm bên cạnh dao động từ 30°C đ |
| b11 | 01:13.5–01:21.6 (8.0s) | L11 | Nếu thức ăn trong dạ dày không kịp lên men mà gặp trời lạnh giá, Con Lười thậm chí có thể... chết đói ngay khi chiếc bụng vẫn đang căng tròn đầy ắp lá cây! |  | Cảnh trời mưa lạnh giá bão tuyết: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân ngồi co ro run rẩy nhưng chiếc bụng vẫn tròn  |
| b12 | 01:21.6–01:26.1 (4.5s) | L12 | Hãy cùng chúng tôi đếm ngược từng mốc giờ để chứng kiến cuộc đời kỳ lạ của sinh vật này! |  | anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H giơ ngón tay đếm ngược, kim đồng hồ 24h quay tít mù báo hiệu hành trình kỳ thú. |

### scene02 · 00 TRƯA: CHIẾC CỔ XOAY 270 ĐỘ VÀ BÀN TAY KHÓA TỰ ĐỘNG KHI CHẾT · 113.1s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.8 (8.8s) | L13 | Đồng hồ điểm 12:00 trưa! Ánh nắng nhiệt đới chiếu rọi thẳng đứng qua kẽ lá, và đây là lúc Thánh sống chậm bắt đầu phơi mình sưởi nắng để kích hoạt lò tiêu hóa trong bụng. |  | Đồng hồ hiện số 12:00 trưa; nắng vàng rực rỡ chiếu qua tán lá; chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân treo ngược dang  |
| b02 | 00:08.8–00:21.3 (12.5s) | L14 | Quý vị hãy nhìn vào chuyển động đầu của nó: trong khi toàn bộ cơ thể vẫn giữ nguyên tư thế treo ngược bất động, chiếc đầu của Con Lười bỗng nhiên quay tít một góc 270° cực kỳ mượt mà chẳng khác nào một chú chim cú vọ giữa ban ngày! | **270 ĐỘ** · xoay đầu như cú · R/360 · [0.65, 0.45] | Toàn thân chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân treo ngược bất động, nhưng chiếc đầu bỗng quay tít 270 độ ra sau lưng |
| b03 | 00:21.3–00:27.4 (6.1s) | L15 | Bác phóng viên ơi, cổ con người chỉ quay được 90° thôi, sao gã này quay gần trọn vòng tròn hay vậy? |  | Chú bé con hoạt hình ngơ ngác hỏi, tay làm động tác vặn cổ 90 độ bị vướng cứng đờ. |
| b04 | 00:27.4–00:41.3 (13.9s) | L16 | Bí mật nằm ở bộ xương cổ độc nhất vô nhị các bạn nhỏ ạ! Trong khi hầu hết các loài động vật có vú trên Trái Đất — từ con chuột nhắt bé tí cho đến hươu cao cổ dài ngoằng — đều chỉ có đúng 7 đốt sống cổ, thì loài lười ba ngón lại tiến hóa sở hữu từ 8-10 đốt sống cổ! | **8-10 ĐỐT** · đốt sống cổ siêu dị · R/360 · [0.68, 0.45]<br>**7 ĐỐT** · hươu cao cổ · L/480 · [0.35, 0.55] | Sơ đồ so sánh đốt sống cổ: BÊN TRÁI hươu cao cổ chỉ có 7 đốt sống cổ; BÊN PHẢI chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân  |
| b05 | 00:41.3–00:52.1 (10.8s) | L17 | Cấu trúc xương cổ kỳ lạ này cho phép nó quay đầu 270° ra sau lưng để gặm những chiếc lá non xung quanh mà không cần phải tốn chút sức lực nào để xoay chuyển cả thân mình cồng kềnh! |  | chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân quay đầu 270 độ gặm những chiếc lá non mọc phía sau lưng mà không cần nhúc nhíc |
| b06 | 00:52.1–00:57.5 (5.5s) | L18 | Chưa dừng lại ở chiếc cổ cú vọ, hãy nhìn vào bốn bàn chân với những chiếc móng vuốt cong vút dài 10cm! | **10 CM** · móng vuốt móc sắt · L/380 · [0.4, 0.5] | Bàn chân chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân với 3 móng vuốt cong vút dài 10cm sắc nhọn móc chặt vào cành gỗ; thước |
| b07 | 00:57.5–01:01.3 (3.8s) | L19 | Đôi chân này không dùng để đi bộ, mà hoạt động như những chiếc móc sắt cứu hộ! |  | Cận cảnh móng vuốt móc như chiếc móc sắt cần cẩu cứu hộ; hoạt động cứu hộ đu cành. |
| b08 | 01:01.3–01:15.5 (14.2s) | L20 | Các nhà giải phẫu học phát hiện cơ bắp của Con Lười chiếm chưa đầy 30% trọng lượng cơ thể, nhưng các đường gân ở ngón chân lại có cơ chế khóa ngàm tự động cực kỳ tinh vi: khi treo lên cành cây, trọng lượng cơ thể tự kéo căng các gân móng bấm chặt vào cành gỗ mà không hề tiêu tốn một chút calo cơ | **30%** · tỷ lệ cơ bắp · R/380 · [0.65, 0.5] | Sơ đồ gân khóa ngàm tự động: cơ bắp chỉ chiếm 30% cơ thể nhưng trọng lượng cơ thể tự kéo căng các sợi gân khóa cứng móng vuốt vào cành cây không tốn năng lượng. |
| b09 | 01:15.5–01:25.0 (9.5s) | L21 | bắp nào! Lực khóa này mạnh đến mức ngay cả khi một con lười đã qua đời vì tuổi già, cơ thể của nó vẫn tiếp tục treo ngược lơ lửng trên cành cây nhiều ngày liền mà không hề bị rơi xuống đất! |  | Một chú lười đã qua đời vì tuổi già nhưng thân thể vẫn treo ngược an nhiên trên cành cây cao nhiều ngày liền không rơi xuống đất. |
| b10 | 01:25.0–01:38.6 (13.6s) | L22 | Không những thế, Thánh sống chậm còn sở hữu siêu năng lực chịu đòn ngã cây vô địch! Vì thường xuyên leo trèo trên những cành cây mục ướt sũng, các nhà nghiên cứu ghi nhận mỗi con lười trong đời bị ngã từ độ cao 15m đến 30m xuống đất cả chục lần! | **15-30M** · ngã không gãy xương · L/380 · [0.4, 0.5] | chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân trượt tay rơi tự do từ độ cao 15m đến 30m từ ngọn cây xuống đất đánh bịch một t |
| b11 | 01:38.6–01:53.1 (14.5s) | L23 | Nhưng nhờ các khớp xương dẻo dai và khung xương sườn đàn hồi kỳ lạ, chúng ngã rơi tự do đánh bịch xuống đất mà hầu như không bao giờ bị gãy xương! Ngã xong, chú lười chỉ việc chớp chớp mắt rồi lại từ từ lết lên thân cây leo tiếp như chưa từng có chuyện gì xảy ra! |  | chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân tiếp đất mông chạm cỏ, chớp chớp mắt tỉnh bơ không gãy xương nào rồi từ từ bò l |

### scene03 · 00 HOÀNG HÔN: HỆ SINH THÁI DI ĐỘNG TRÊN LƯNG VÀ BIỆT TÀI BƠI LỘI · 83.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:04.1 (4.1s) | L24 | Bầu trời hoàng hôn buông sắc tím thẫm trên dòng sông, đồng hồ điểm 18:00 |  | Bầu trời hoàng hôn 18:00 tím biếc, chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân treo ngược trên cành cây ven sông; anh chàng |
| b02 | 00:04.1–00:14.2 (10.1s) | L25 | tối! Khi nhìn cận cảnh vào lớp lông xơ xác màu xám bùn của Thánh sống chậm, chúng tôi phải thốt lên kinh ngạc: đây không phải là một con vật đơn thuần, mà là cả một hệ sinh thái rừng rậm thu nhỏ đang di động! |  | Kính lúp phóng đại lớp lông xơ xác phủ đầy các vệt màu xanh lục mộc mạc; cả một khu rừng sinh thái thu nhỏ đang di động. |
| b03 | 00:14.2–00:24.5 (10.3s) | L26 | Quý vị có thấy những vệt màu xanh lục phủ kín khắp lưng và đầu của nó không? Đó không phải là màu lông bẩm sinh, mà là một thảm tảo xanh sống ký sinh ngay trên các rãnh nứt siêu nhỏ của từng sợi lông lười! |  | Cận cảnh từng sợi lông lười: trên thân sợi lông có các rãnh nứt siêu nhỏ chứa đầy tảo xanh sống ký sinh xanh mướt. |
| b04 | 00:24.5–00:35.9 (11.3s) | L27 | Thảm tảo xanh này được bón phân và chăm sóc bởi một đội quân cư dân đặc quyền: loài bướm đêm Cryptoses — sinh vật chỉ sống duy nhất trên bộ lông của Con Lười mà không thể tìm thấy ở bất kỳ nơi nào khác trên hành tinh! |  | Hàng trăm chú bướm đêm Cryptoses nhỏ xíu bay lượn quanh bộ lông lười như một vương quốc côn trùng náo nhiệt. |
| b05 | 00:35.9–00:41.2 (5.3s) | L28 | Hàng trăm con bướm đêm làm tổ, sinh sống và thải phân đạm nuôi dưỡng cho vườn tảo xanh mọc um tùm. |  | Bướm đêm thải phân đạm bón cho thảm tảo xanh mọc tươi tốt; khu vườn trên lưng xanh ngắt. |
| b06 | 00:41.2–00:53.1 (11.9s) | L61 | Đổi lại, thảm tảo xanh biến Con Lười thành một búi lá cây ngụy trang hoàn hảo chống lại tầm mắt của kẻ thù từ trên cao, và những lúc đói lòng, chú lười chỉ việc liếm láp lớp tảo giàu chất béo này trên lông như một món ăn vặt bổ dưỡng! |  | chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân hòa tan vào tán lá rừng ngụy trang tàng hình chống lại kẻ thù; thè lưỡi liếm lớ |
| b07 | 00:53.1–00:57.1 (4.0s) | L29 | Một phi vụ làm ăn đôi bên cùng có lợi kéo dài hàng triệu năm! |  | chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân mỉm cười bắt tay với chú bướm đêm hoạt hình; ký kết hợp đồng cộng sinh hàng tri |
| b08 | 00:57.1–01:05.6 (8.5s) | L30 | Nhưng cú sốc lớn nhất buổi chiều hôm nay chính là khả năng thể thao bất ngờ của gã lười! Khi muốn di chuyển qua bờ bên kia, Thánh sống chậm buông tay thả mình rơi tõm xuống dòng sông. |  | chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân buông tay thả mình rơi tõm xuống dòng sông nước bắn tung tóe; anh chàng phóng v |
| b09 | 01:05.6–01:12.9 (7.3s) | L31 | Quý vị tin được không: sinh vật lết trên cạn chậm như rùa này lại bơi lội cực kỳ cừ khôi, tốc độ bơi dưới nước nhanh gấp 3-4 lần lúc bò trên cạn! | **GẤP 3-4X** · tốc độ bơi vượt sông · L/380 · [0.4, 0.5] | chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân bơi sải điêu luyện dưới nước với tốc độ nhanh gấp 3-4 lần lúc lết trên cạn; bọt |
| b10 | 01:12.9–01:17.0 (4.1s) | L32 | Nó có thể nhịn thở dưới nước tới 40 phút đồng hồ nhờ khả năng làm chậm nhịp tim xuống còn 1/3! | **40 PHÚT** · nhịn thở dưới nước · R/360 · [0.65, 0.45]<br>**1/3** · nhịp tim chậm lại · L/480 · [0.35, 0.55] | chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân lặn dưới nước nhịn thở 40 phút, nhịp tim giảm xuống còn 1/3; đồng hồ bấm giờ 40 |
| b11 | 01:17.0–01:23.7 (6.7s) | L33 | Từ một kẻ tàn tật trên cạn, nó biến thành một tay bơi lội cừ khôi vượt sông ngầu chẳng kém gì rái cá! |  | chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân bơi sang bờ bên kia ngầu như một kình ngư rái cá, mặt lạnh lùng kiêu hãnh vẫy t |

### scene04 · 00 ĐÊM: NGHI LỄ ĐI VỆ SINH TỬ THẦN VÀ CÚ GIẢM 1/3 CÂN NẶNG · 99.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:03.5 (3.5s) | L34 | Màn đêm bao trùm tĩnh mịch, đồng hồ điểm 22:00 đêm! |  | Rừng rậm 22:00 đêm tĩnh mịch, ánh trăng bạc chiếu rọi; chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân từ từ nhích từng bước từ |
| b02 | 00:03.5–00:09.4 (6.0s) | L35 | Và đây chính là khoảnh khắc hồi hộp, căng thẳng và nguy hiểm bậc nhất trong cả tuần lễ của Thánh sống chậm: chuyến hành hương xuống mặt đất để đi vệ sinh! |  | Chuyến hành hương nguy hiểm trong tuần của Thánh sống chậm: chuẩn bị bò xuống mặt đất ẩm ướt để đi vệ sinh. |
| b03 | 00:09.4–00:24.1 (14.6s) | L36 | Trong khi các loài thú khác trên cành cây chỉ việc xả phân tự do xuống đất từ trên cao, thì loài lười ba ngón lại kiên quyết tuân theo một nghi thức kỳ quặc đến mức khó hiểu: cứ đều đặn 1 tuần 1 lần, nó bắt buộc phải bò từ ngọn cây cao chót vót xuống tận mặt đất ẩm ướt để đi đại tiện! | **1 TUẦN/LẦN** · nghi lễ đi vệ sinh · R/380 · [0.65, 0.5] | Khỉ và chim trên cây xả phân tự do rơi xuống đất; chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân lắc đầu nghiêm trang quyết tâ |
| b04 | 00:24.1–00:29.8 (5.7s) | L37 | Chuyến đi này tiêu tốn tới 10% năng lượng ít ỏi cả ngày của nó, nhưng cái giá phải trả lớn hơn thế gấp ngàn lần! | **10% PIN** · năng lượng tiêu tốn · L/380 · [0.4, 0.5] | Chuyến hành hương nguy hiểm: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân bò xuống đất mất 10% năng lượng cả ngày; biển báo  |
| b05 | 00:29.8–00:35.8 (6.0s) | L38 | Vì di chuyển quá vụng về trên mặt đất, Con Lười hoàn toàn mất đi khả năng tự vệ trước các loài thú săn mồi mặt đất. |  | chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân lết chậm chạp trên mặt đất bùn lầy, các móng vuốt cản trở bước đi; trong bụi rậ |
| b06 | 00:35.8–00:50.5 (14.7s) | L39 | Báo cáo nghiên cứu thực địa chấn động của các nhà sinh vật học tại Costa Rica chỉ ra rằng: hơn 50% số cái chết trong toàn bộ cuộc đời của loài lười đều diễn ra đúng vào thời điểm nó mò xuống đất đi vệ sinh! Một cái chết lãng xẹt và bi hài bậc nhất thế giới tự nhiên! | **50% CHẾT** · khi đi vệ sinh · L/380 · [0.4, 0.5] | Biểu đồ thống kê giật mình: hơn 50% cái chết của loài lười xảy ra ngay lúc đi vệ sinh dưới đất; bóng báo đốm và chó hoang. |
| b07 | 00:50.5–01:01.5 (11.0s) | L40 | Bác phóng viên ơi, nguy hiểm đến mất mạng như thế sao nó không ị luôn trên cây cho khỏe ạ? Câu hỏi tuyệt vời của khán giả nhí cũng chính là điều khiến các nhà khoa học vò đầu bứt tai suốt nhiều thập kỷ! |  | Chú bé con hoạt hình gãi đầu ngơ ngác hỏi tại sao không ị luôn trên cây cho an toàn. |
| b08 | 01:01.5–01:07.1 (5.6s) | L41 | Khi xuống tới gốc cây, Con Lười dùng chiếc đuôi ngắn ngủn ngoáy một chiếc hố nhỏ trên nền đất rồi bắt đầu xả thải. |  | chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân dùng chiếc đuôi ngắn ngủn ngoáy một chiếc hố nhỏ dưới đất rồi ngồi xổm xả thải  |
| b09 | 01:07.1–01:19.9 (12.8s) | L42 | Quý vị hãy chuẩn bị tinh thần: vì nhịn suốt 1 tuần lễ, lượng phân và nước tiểu xả ra trong 1 lần đi vệ sinh có thể nặng tới 1/3 trọng lượng toàn bộ cơ thể nó! Đi vệ sinh xong một cái là chú lười nhẹ bẫng đi 30% cân nặng! | **1/3** · trọng lượng cơ thể · R/360 · [0.65, 0.45]<br>**30%** · giảm cân tức thì · L/480 · [0.35, 0.55] | Cân đo tải trọng: đống phân thải ra nặng tới 1/3 trọng lượng cơ thể; chiếc cân giảm 30% cân nặng ngay tức khắc. |
| b10 | 01:19.9–01:32.6 (12.7s) | L43 | Và mục đích sinh tử của chuyến đi này chính là để phục vụ bạn bè: khi lười đi vệ sinh, những cô bướm đêm trên lông sẽ bò xuống đẻ trứng vào đống phân tươi để ấu trùng phát triển, hoàn thành chu trình duy trì bộ lông xanh cho thế hệ lười tiếp theo! |  | Khi chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân xả phân, các cô bướm đêm Cryptoses từ trên lông bò túa xuống đẻ trứng vào đ |
| b11 | 01:32.6–01:39.4 (6.8s) | L44 | Chấp nhận đối mặt tử thần 50% chỉ để giữ lời hứa với đàn bướm đêm, quả là một tình bạn sinh tử cảm động! |  | chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân vẫy tay chào đàn bướm đêm rồi chậm rãi leo trở lại cây; tình bạn sinh tử 50% ng |

### scene05 · 00 ĐÊM: CUỘC CHẠM TRÁN SÁT THỦ ĐẠI BÀNG HARPY VÀ CÚ CÀO TỰ VỆ · 75.1s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.2 (10.2s) | L45 | Màn đêm chuyển về khuya, đồng hồ điểm 02:00 rạng sáng! Sau chuyến đi vệ sinh hú vía dưới mặt đất, Thánh sống chậm đã leo trở lại chạc cây an toàn. Nhưng hiểm nguy từ bầu trời lại bắt đầu rình rập! |  | Đồng hồ chỉ 02:00 rạng sáng; chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân đã leo lên chạc cây cao ngủ tiếp; trên bầu trời mộ |
| b02 | 00:10.2–00:24.1 (13.8s) | L46 | Trên tầng tán rừng nhiệt đới, kẻ thù truyền kiếp đáng sợ nhất của loài lười đã xuất hiện: Đại bàng Harpy — bạo chúa bầu trời châu Mỹ với sải cánh dài hơn 2m và bộ móng vuốt to bằng móng gấu xám! Đại bàng Harpy chuyên lượn sát các ngọn cây để săn lùng khỉ và lười. | **2 MÉT** · sải cánh đại bàng · R/380 · [0.65, 0.45] | Bạo chúa bầu trời Đại bàng Harpy sải cánh hơn 2m với bộ móng vuốt to bằng móng gấu xám lượn sát cành cây. |
| b03 | 00:24.1–00:33.7 (9.7s) | L47 | Nhưng chính tốc độ rùa bò và bộ lông mọc rêu xanh lại trở thành tấm áo giáp tàng hình siêu việt cứu mạng Thánh sống chậm! Đại bàng bay lướt qua phía trên chỉ thấy một búi lá cây đung đưa bất động trong gió đêm. |  | Áo giáp tàng hình: bộ lông rêu xanh và sự bất động tuyệt đối của chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân biến chú thành |
| b04 | 00:33.7–00:46.1 (12.4s) | L48 | Và quý vị đừng tưởng chú lười hiền lành này không biết phản kháng nhé! Khi bị dồn vào chân tường, Con Lười có thể tung ra những cú cào vuốt móng thép sắc lẹm với tốc độ cực nhanh, đủ sức rạch toạc da thịt của kẻ săn mồi khiến báo đốm hay đại bàng cũng phải dè chừng lùi bước! |  | Cận cảnh cú phản đòn bất ngờ: khi bị đại bàng lao tới sát, chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân vung móng vuốt cào x |
| b05 | 00:46.1–00:51.5 (5.4s) | L49 | Chậm chạp có tính toán, bất động để sinh tồn, đó là bản lĩnh của kẻ sống sót qua hàng triệu năm! |  | chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân thu móng vuốt lại, mỉm cười bình thản trên cây; đại bàng ôm mặt bay đi; bản lĩn |
| b06 | 00:51.5–01:00.1 (8.6s) | L50 | Và tình mẫu tử của loài lười cũng cảm động không kém! Chú lười con sinh ra chỉ nhỏ xíu bằng nắm tay, bám chặt vào ngực mẹ suốt 6 tháng trời ròng rã không rời nửa bước! | **6 THÁNG** · ôm ngực mẹ bám chặt · R/380 · [0.65, 0.5] | Chú lười con bé xíu bám chặt vào ngực lười mẹ suốt 6 tháng ròng rã; lười mẹ ôm con âu yếm. |
| b07 | 01:00.1–01:15.1 (14.9s) | L51 | Người mẹ lười dù chậm chạp đến đâu cũng sẽ bảo vệ con mình trước nanh vuốt của thú dữ, sẵn sàng giơ những chiếc móng vuốt 10cm sắc nhọn rạch toạc mặt bất kỳ kẻ săn mồi nào dám đụng vào đứa con bé bỏng! Chậm chạp nhưng không hề yếu hèn, đó chính là bản lĩnh sinh tồn của Thánh sống chậm! | **10 CM** · móng vuốt tự vệ · L/380 · [0.4, 0.5] | Lười mẹ xòe móng vuốt sắc nhọn gầm gừ che chắn cho đứa con trước bóng một con mèo rừng gấm; ánh mắt người mẹ kiên cường. |

### scene06 · 00 RẠNG SÁNG: TRIẾT LÝ SỐNG CHẬM ĐỈNH CAO VÀ BÓNG ĐEN BÍ ẨN TẬP 14 · 80.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.5 (8.5s) | L52 | Bây giờ là 04:00 rạng sáng! Ánh bình minh le lói bắt đầu rọi xuống tán rừng già, khép lại 24 giờ tác nghiệp đầy cảm xúc theo chân Thánh sống chậm. |  | Rừng già lúc 04:00 rạng sáng, ánh bình minh le lói qua sương sớm; chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân ngồi thiền an |
| b02 | 00:08.5–00:20.8 (12.3s) | L53 | Nhiều người thường lấy con lười ra làm biểu tượng cho sự lười nhác và thụt lùi, nhưng thực tế tiến hóa đã chứng minh: lối sống chậm rãi, tối giản hóa năng lượng và không tranh giành thức ăn với bất kỳ ai đã giúp Con Lười tồn tại bền bỉ qua hơn 30 triệu năm lịch sử! | **30 TR NĂM** · sinh tồn bền bỉ · L/380 · [0.35, 0.5] | Dòng thời gian 30 triệu năm: các loài thú hung hăng to lớn đều tuyệt chủng; riêng chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ ch |
| b03 | 00:20.8–00:29.6 (8.8s) | L54 | Đôi khi trong cuộc sống hối hả, biết sống chậm lại, tĩnh tâm và kiên định với con đường của riêng mình lại là cách sinh tồn thông minh và khôn ngoan nhất! |  | Triết lý sống: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân ngồi tĩnh tâm giữa dòng đời hối hả, xung quanh là biểu tượng hoa |
| b04 | 00:29.6–00:33.5 (3.9s) | L55 | Hành trình 24 giờ của Thánh sống chậm đã chính thức khép lại! |  | Đồng hồ 24h quay trọn một vòng; anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H chào tạm biệt khán giả khép lại nhật ký 24h. |
| b05 | 00:33.5–00:42.5 (9.0s) | L56 | Nhưng ngay bây giờ, xin mời quý vị khán giả hãy hướng mắt lên màn hình lớn để chiêm ngưỡng BÓNG ĐEN BÍ ẨN của nhân vật xuất hiện trong Tập 14 tiếp theo! |  | Màn hình lớn bỗng đổi màu tím thẫm bí ẩn; phông nền rực lửa Đấu Trường Sinh Tồn chuyển sang bóng tối; khán giả tò mò nghển cổ. |
| b06 | 00:42.5–00:52.4 (9.9s) | L57 | Xin gửi tới quý vị ba manh mối chấn động về bóng đen bí ẩn này: Thứ nhất, đây là siêu tội phạm lừa đảo khét tiếng bậc nhất thế giới loài chim, với tuyệt kỹ đẻ trộm trứng vào tổ của loài chim khác chỉ trong vỏn vẹn 10 giây! | **10 GIÂY** · đẻ trộm trứng · R/380 · [0.65, 0.45] | BÓNG ĐEN BÍ ẨN (Solid Black Silhouette): Trên màn hình lớn hiện ra một cái bóng đen hoàn toàn của một loài chim bí ẩn đang lén lút thả một quả trứng vào tổ chim khác; dấu hỏi chấm màu vàng khổng lồ phát sáng rực rỡ ở giữa. KHÔNG có chú Con Lười trong cảnh này. |
| b07 | 00:52.4–01:01.2 (8.8s) | L58 | Thứ hai, bản năng sát thủ tàn nhẫn đến rợn người: con non vừa chui ra khỏi vỏ trứng, mắt còn chưa mở, nhưng đã dùng chiếc lưng lõm hất tung toàn bộ trứng của chim chủ nhà rơi xuống đất vỡ nát! |  | BÓNG ĐEN BÍ ẨN (Solid Black Silhouette): Bóng đen của một chú chim non vừa chui ra khỏi vỏ trứng, mắt nhắm nghiền nhưng dùng chiếc lưng lõm hất văng quả trứng của chim chủ nhà rơi xuống vỡ toang; dấu hỏi chấm xoay tròn. KHÔNG có chú Con Lười trong cảnh này. |
| b08 | 01:01.2–01:08.3 (7.1s) | L59 | Và thứ ba, nghịch lý bi hài: đôi chim bố mẹ nuôi còng lưng bón mồi cho một đứa con nuôi khổng lồ to gấp 3 lần chính mình! Quý | **GẤP 3 LẦN** · con nuôi khổng lồ · R/380 · [0.65, 0.5] | BÓNG ĐEN BÍ ẨN (Solid Black Silhouette): Bóng đen của hai chú chim bố mẹ bé tí hon đang kiệt sức bón mồi cho một con chim non khổng lồ to gấp 3 lần chính mình; dấu hỏi chấm nhấp nháy. KHÔNG có chú Con Lười trong cảnh này. |
| b09 | 01:08.3–01:20.5 (12.2s) | L60 | vị khán giả có đoán ra bóng đen bí ẩn này là quái kiệt nào không? Hãy để lại phán quyết và dự đoán của bạn ngay dưới phần bình luận nhé! Phóng viên truyền hình xin chào tạm biệt và hẹn gặp lại quý vị trong bản tin sinh tồn kỳ thú tiếp theo! |  | Khán đài xôn xao háo hức: các bạn nhỏ và muông thú giơ biển dấu hỏi chấm tranh luận đoán tên quái kiệt; anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H giơ tay mời khán giả bình luận. |

## 5. Phân cảnh Shorts — từng beat

Banner: **TẠI SAO 50% CÁI CHẾT / LÚC ĐI VỆ SINH?!** · giọng 47.1s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Một sinh vật lười biếng đến mức mất cả tháng trời chỉ để tiêu hóa một chiếc lá cây, | **1 THÁNG** · tiêu hóa 1 chiếc lá · L/560 · [0.35, 0.4] |
| s02 | 00:04.5 | S12 | nhưng mỗi tuần lại chấp nhận mạo hiểm tính mạng để làm một việc kỳ quặc! |  |
| s03 | 00:07.9 | S02 | Đó chính là Con Lười ba ngón, thánh sống chậm của rừng rậm Nam Mỹ với tốc độ chỉ 0,2km/h. | **0,2 KM/H** · tốc độ rùa bò · R/580 · [0.65, 0.45] |
| s04 | 00:14.1 | S03 | Dạ dày 4 ngăn trao đổi chất cực chậm khiến một chiếc lá phải mất 30 ngày mới tiêu hóa xong, | **30 NGÀY** · trao đổi chất chậm · L/650 · [0.4, 0.5] |
| s05 | 00:18.7 | S04 | còn bộ lông phủ đầy tảo xanh biến nó thành một khu rừng di động cho hàng trăm con bướm đêm sinh sống. |  |
| s06 | 00:23.8 | S05 | Nhưng kỳ lạ nhất là cứ đúng 1 tuần 1 lần, nó bắt buộc phải bò từ ngọn cây xuống đất để đi vệ sinh, | **1 TUẦN/LẦN** · nghi lễ đi vệ sinh · R/600 · [0.65, 0.45] |
| s07 | 00:28.8 | S06 | xả tới 1/3 trọng lượng cơ thể! | **1/3** · trọng lượng cơ thể · L/650 · [0.4, 0.5] |
| s08 | 00:31.6 | S07 | Do di chuyển quá vụng về dưới đất, |  |
| s09 | 00:33.5 | S08 | hơn 50% số cái chết của loài lười đều diễn ra đúng vào thời điểm đi vệ sinh này! | **50% CHẾT** · khi đi vệ sinh · R/650 · [0.65, 0.5] |
| s10 | 00:37.8 | S09 | Vậy là bí mật đã rõ: con lười chấp nhận đối mặt với tử thần chỉ để bướm đêm trên lưng có chỗ đẻ trứng vào phân, |  |
| s11 | 00:43.6 | S10 | giữ cho bộ lông luôn xanh ngụy trang |  |
| s12 | 00:45.3 | S11 | để sinh tồn qua hàng triệu năm! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bây giờ là 06:00 sáng!". Bố cục: Rừng rậm nhiệt đới Costa Rica mù sương lúc 06:00 sáng: chiếc đồng hồ báo thức khổng lồ rung chuông reo sáng rực; anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H mặc áo dã ngoại cầm micro phát biểu trước máy quay.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kính thưa quý vị khán giả, chúng tôi đang có mặt trực tiếp tại tán rừng rậm nhiệt đới Costa Rica để tường thuật lại một ngày làm việc siêu chậm chạp của sinh vật lười biếng nhất hành tinh: Con Lười ba ngón!". Bố cục: anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H chỉ tay lên cành cây cao: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân treo ngược bất động như một bọc rơm khô giữa cành lá xanh.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiếc đồng hồ báo thức vừa rung chuông điểm sáng, và nhân vật chính của chúng ta — Thánh sống chậm — dường như vẫn bất động hoàn toàn như một bọc rơm khô treo trên cành cây!". Bố cục: Đồng hồ rung chuông reo inh ỏi; chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân hé mở một bên mắt ngơ ngác, khóe miệng vẫn giữ nụ cười tủm tỉm an nhiên không buồn nhúc nhích.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để di chuyển được một bước chân ngắn ngủn vài xăng-ti-mét, gã này mất tới vài phút đồng hồ suy nghĩ và đắn đo!". Bố cục: Cận cảnh bàn chân chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân nhấc lên chậm chạp từng milimet; đám mây suy nghĩ đầy các phép tính toán chỉ để bước một bước; một chú ốc sên bò bên cạnh nhìn ngạc nhiên.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Alo trường quay nghe rõ không? Phóng viên cho hỏi sinh vật này bò nhanh nhất được bao nhiêu vậy?". Bố cục: Trường quay thời sự: cô phát thanh viên tin tức hoạt hình xinh đẹp ngồi sau bàn trường quay thời sự đeo tai nghe ngạc nhiên chỉ vào màn hình kết nối hiện trường đặt câu hỏi.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo trường quay, tốc độ kỷ lục của nó trên ngọn cây chỉ đạt vỏn vẹn 0,24km/h — tức là khoảng 4m mỗi phút!". Bố cục: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân bò trên cành cây với tốc độ 0,24km/h; đồng hồ đo tốc độ xe hơi bên cạnh kim chỉ sát vạch số 0; nhãn 0,24km/h và 4m/phút.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn nếu rơi xuống đất thì chỉ lết được chừng 2m một phút, chậm đến mức một con ốc sên bò qua mặt cũng có thể bấm còi vượt mặt dễ dàng!". Bố cục: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân lết vụng về trên mặt đất với tốc độ 2m/phút; một chú ốc sên đeo kính mát bấm còi vượt mặt dễ dàng; nhãn 2m.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng điều kinh ngạc nhất nằm ở bộ máy tiêu hóa bên trong: dạ dày của Thánh sống chậm có cấu tạo 4 ngăn phức tạp y hệt loài trâu bò, nhưng quá trình trao đổi chất lại chậm nhất thế giới động vật có vú.". Bố cục: Sơ đồ giải phẫu dạ dày 4 ngăn phức tạp như trâu bò của lười; bên trong các mẩu lá cây nằm yên bất động, vi khuẩn lên men lười biếng.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để tiêu hóa hết một chiếc lá cây duy nhất, dạ dày của nó phải làm việc cật lực ròng rã suốt 30 ngày trời, thậm chí có thể kéo dài tới 50 ngày!". Bố cục: Chiếc lá cây duy nhất nằm trong dạ dày lười; tờ lịch 30 ngày rơi lả tả; một chiếc đồng hồ cát chảy cực chậm.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chính vì tiêu hóa chậm kỷ lục như vậy, nhiệt độ cơ thể của Con Lười dao động thất thường từ 30-34°C, phụ thuộc hoàn toàn vào ánh nắng mặt trời y như các loài bò sát!". Bố cục: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân nằm phơi bụng trên cành cây sưởi nắng; nhiệt kế cắm bên cạnh dao động từ 30°C đến 34°C như loài bò sát; mặt trời chiếu rọi.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu thức ăn trong dạ dày không kịp lên men mà gặp trời lạnh giá, Con Lười thậm chí có thể... chết đói ngay khi chiếc bụng vẫn đang căng tròn đầy ắp lá cây!". Bố cục: Cảnh trời mưa lạnh giá bão tuyết: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân ngồi co ro run rẩy nhưng chiếc bụng vẫn tròn căng đầy ắp lá cây.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy cùng chúng tôi đếm ngược từng mốc giờ để chứng kiến cuộc đời kỳ lạ của sinh vật này!". Bố cục: anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H giơ ngón tay đếm ngược, kim đồng hồ 24h quay tít mù báo hiệu hành trình kỳ thú.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đồng hồ điểm 12:00 trưa! Ánh nắng nhiệt đới chiếu rọi thẳng đứng qua kẽ lá, và đây là lúc Thánh sống chậm bắt đầu phơi mình sưởi nắng để kích hoạt lò tiêu hóa trong bụng.". Bố cục: Đồng hồ hiện số 12:00 trưa; nắng vàng rực rỡ chiếu qua tán lá; chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân treo ngược dang tay chân phơi nắng sưởi ấm dạ dày.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quý vị hãy nhìn vào chuyển động đầu của nó: trong khi toàn bộ cơ thể vẫn giữ nguyên tư thế treo ngược bất động, chiếc đầu của Con Lười bỗng nhiên quay tít một góc 270° cực kỳ mượt mà chẳng khác nào một chú chim cú vọ giữa ban ngày!". Bố cục: Toàn thân chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân treo ngược bất động, nhưng chiếc đầu bỗng quay tít 270 độ ra sau lưng như chim cú vọ giữa ban ngày.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bác phóng viên ơi, cổ con người chỉ quay được 90° thôi, sao gã này quay gần trọn vòng tròn hay vậy?". Bố cục: Chú bé con hoạt hình ngơ ngác hỏi, tay làm động tác vặn cổ 90 độ bị vướng cứng đờ.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bí mật nằm ở bộ xương cổ độc nhất vô nhị các bạn nhỏ ạ! Trong khi hầu hết các loài động vật có vú trên Trái Đất — từ con chuột nhắt bé tí cho đến hươu cao cổ dài ngoằng — đều chỉ có đúng 7 đốt sống cổ, thì loài lười ba ngón lại tiến hóa sở hữu từ 8-10 đốt sống cổ!". Bố cục: Sơ đồ so sánh đốt sống cổ: BÊN TRÁI hươu cao cổ chỉ có 7 đốt sống cổ; BÊN PHẢI chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân có 8-10 đốt sống cổ đặc biệt.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cấu trúc xương cổ kỳ lạ này cho phép nó quay đầu 270° ra sau lưng để gặm những chiếc lá non xung quanh mà không cần phải tốn chút sức lực nào để xoay chuyển cả thân mình cồng kềnh!". Bố cục: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân quay đầu 270 độ gặm những chiếc lá non mọc phía sau lưng mà không cần nhúc nhích thân mình cồng kềnh.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa dừng lại ở chiếc cổ cú vọ, hãy nhìn vào bốn bàn chân với những chiếc móng vuốt cong vút dài 10cm!". Bố cục: Bàn chân chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân với 3 móng vuốt cong vút dài 10cm sắc nhọn móc chặt vào cành gỗ; thước dây đo độ dài móng.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đôi chân này không dùng để đi bộ, mà hoạt động như những chiếc móc sắt cứu hộ!". Bố cục: Cận cảnh móng vuốt móc như chiếc móc sắt cần cẩu cứu hộ; hoạt động cứu hộ đu cành.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà giải phẫu học phát hiện cơ bắp của Con Lười chiếm chưa đầy 30% trọng lượng cơ thể, nhưng các đường gân ở ngón chân lại có cơ chế khóa ngàm tự động cực kỳ tinh vi: khi treo lên cành cây, trọng lượng cơ thể tự kéo căng các gân móng bấm chặt vào cành gỗ mà không hề tiêu tốn một chút calo cơ bắp nào!". Bố cục: Sơ đồ gân khóa ngàm tự động: cơ bắp chỉ chiếm 30% cơ thể nhưng trọng lượng cơ thể tự kéo căng các sợi gân khóa cứng móng vuốt vào cành cây không tốn năng lượng.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lực khóa này mạnh đến mức ngay cả khi một con lười đã qua đời vì tuổi già, cơ thể của nó vẫn tiếp tục treo ngược lơ lửng trên cành cây nhiều ngày liền mà không hề bị rơi xuống đất!". Bố cục: Một chú lười đã qua đời vì tuổi già nhưng thân thể vẫn treo ngược an nhiên trên cành cây cao nhiều ngày liền không rơi xuống đất.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không những thế, Thánh sống chậm còn sở hữu siêu năng lực chịu đòn ngã cây vô địch! Vì thường xuyên leo trèo trên những cành cây mục ướt sũng, các nhà nghiên cứu ghi nhận mỗi con lười trong đời bị ngã từ độ cao 15m đến 30m xuống đất cả chục lần!". Bố cục: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân trượt tay rơi tự do từ độ cao 15m đến 30m từ ngọn cây xuống đất đánh bịch một tiếng; thước đo độ cao rơi.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng nhờ các khớp xương dẻo dai và khung xương sườn đàn hồi kỳ lạ, chúng ngã rơi tự do đánh bịch xuống đất mà hầu như không bao giờ bị gãy xương! Ngã xong, chú lười chỉ việc chớp chớp mắt rồi lại từ từ lết lên thân cây leo tiếp như chưa từng có chuyện gì xảy ra!". Bố cục: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân tiếp đất mông chạm cỏ, chớp chớp mắt tỉnh bơ không gãy xương nào rồi từ từ bò lên cây leo tiếp.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bầu trời hoàng hôn buông sắc tím thẫm trên dòng sông, đồng hồ điểm 18:00 tối!". Bố cục: Bầu trời hoàng hôn 18:00 tím biếc, chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân treo ngược trên cành cây ven sông; anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H cầm kính lúp soi vào lưng lười.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi nhìn cận cảnh vào lớp lông xơ xác màu xám bùn của Thánh sống chậm, chúng tôi phải thốt lên kinh ngạc: đây không phải là một con vật đơn thuần, mà là cả một hệ sinh thái rừng rậm thu nhỏ đang di động!". Bố cục: Kính lúp phóng đại lớp lông xơ xác phủ đầy các vệt màu xanh lục mộc mạc; cả một khu rừng sinh thái thu nhỏ đang di động.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quý vị có thấy những vệt màu xanh lục phủ kín khắp lưng và đầu của nó không? Đó không phải là màu lông bẩm sinh, mà là một thảm tảo xanh sống ký sinh ngay trên các rãnh nứt siêu nhỏ của từng sợi lông lười!". Bố cục: Cận cảnh từng sợi lông lười: trên thân sợi lông có các rãnh nứt siêu nhỏ chứa đầy tảo xanh sống ký sinh xanh mướt.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thảm tảo xanh này được bón phân và chăm sóc bởi một đội quân cư dân đặc quyền: loài bướm đêm Cryptoses — sinh vật chỉ sống duy nhất trên bộ lông của Con Lười mà không thể tìm thấy ở bất kỳ nơi nào khác trên hành tinh!". Bố cục: Hàng trăm chú bướm đêm Cryptoses nhỏ xíu bay lượn quanh bộ lông lười như một vương quốc côn trùng náo nhiệt.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hàng trăm con bướm đêm làm tổ, sinh sống và thải phân đạm nuôi dưỡng cho vườn tảo xanh mọc um tùm.". Bố cục: Bướm đêm thải phân đạm bón cho thảm tảo xanh mọc tươi tốt; khu vườn trên lưng xanh ngắt.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một phi vụ làm ăn đôi bên cùng có lợi kéo dài hàng triệu năm!". Bố cục: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân mỉm cười bắt tay với chú bướm đêm hoạt hình; ký kết hợp đồng cộng sinh hàng triệu năm đôi bên cùng có lợi.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng cú sốc lớn nhất buổi chiều hôm nay chính là khả năng thể thao bất ngờ của gã lười! Khi muốn di chuyển qua bờ bên kia, Thánh sống chậm buông tay thả mình rơi tõm xuống dòng sông.". Bố cục: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân buông tay thả mình rơi tõm xuống dòng sông nước bắn tung tóe; anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H há hốc mồm kinh ngạc.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quý vị tin được không: sinh vật lết trên cạn chậm như rùa này lại bơi lội cực kỳ cừ khôi, tốc độ bơi dưới nước nhanh gấp 3-4 lần lúc bò trên cạn!". Bố cục: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân bơi sải điêu luyện dưới nước với tốc độ nhanh gấp 3-4 lần lúc lết trên cạn; bọt nước rẽ sóng ngầu như kình ngư.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó có thể nhịn thở dưới nước tới 40 phút đồng hồ nhờ khả năng làm chậm nhịp tim xuống còn 1/3!". Bố cục: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân lặn dưới nước nhịn thở 40 phút, nhịp tim giảm xuống còn 1/3; đồng hồ bấm giờ 40 phút.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Từ một kẻ tàn tật trên cạn, nó biến thành một tay bơi lội cừ khôi vượt sông ngầu chẳng kém gì rái cá!". Bố cục: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân bơi sang bờ bên kia ngầu như một kình ngư rái cá, mặt lạnh lùng kiêu hãnh vẫy tay chào khán giả.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Màn đêm bao trùm tĩnh mịch, đồng hồ điểm 22:00 đêm!". Bố cục: Rừng rậm 22:00 đêm tĩnh mịch, ánh trăng bạc chiếu rọi; chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân từ từ nhích từng bước từ ngọn cây cao leo xuống gốc đất; anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H nín thở theo dõi.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và đây chính là khoảnh khắc hồi hộp, căng thẳng và nguy hiểm bậc nhất trong cả tuần lễ của Thánh sống chậm: chuyến hành hương xuống mặt đất để đi vệ sinh!". Bố cục: Chuyến hành hương nguy hiểm trong tuần của Thánh sống chậm: chuẩn bị bò xuống mặt đất ẩm ướt để đi vệ sinh.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong khi các loài thú khác trên cành cây chỉ việc xả phân tự do xuống đất từ trên cao, thì loài lười ba ngón lại kiên quyết tuân theo một nghi thức kỳ quặc đến mức khó hiểu: cứ đều đặn 1 tuần 1 lần, nó bắt buộc phải bò từ ngọn cây cao chót vót xuống tận mặt đất ẩm ướt để đi đại tiện!". Bố cục: Khỉ và chim trên cây xả phân tự do rơi xuống đất; chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân lắc đầu nghiêm trang quyết tâm leo xuống đất 1 tuần 1 lần.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chuyến đi này tiêu tốn tới 10% năng lượng ít ỏi cả ngày của nó, nhưng cái giá phải trả lớn hơn thế gấp ngàn lần!". Bố cục: Chuyến hành hương nguy hiểm: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân bò xuống đất mất 10% năng lượng cả ngày; biển báo nguy hiểm toilet cắm ở gốc cây.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vì di chuyển quá vụng về trên mặt đất, Con Lười hoàn toàn mất đi khả năng tự vệ trước các loài thú săn mồi mặt đất.". Bố cục: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân lết chậm chạp trên mặt đất bùn lầy, các móng vuốt cản trở bước đi; trong bụi rậm có hai đốm mắt thú dữ phát sáng rình rập.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo nghiên cứu thực địa chấn động của các nhà sinh vật học tại Costa Rica chỉ ra rằng: hơn 50% số cái chết trong toàn bộ cuộc đời của loài lười đều diễn ra đúng vào thời điểm nó mò xuống đất đi vệ sinh! Một cái chết lãng xẹt và bi hài bậc nhất thế giới tự nhiên!". Bố cục: Biểu đồ thống kê giật mình: hơn 50% cái chết của loài lười xảy ra ngay lúc đi vệ sinh dưới đất; bóng báo đốm và chó hoang.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bác phóng viên ơi, nguy hiểm đến mất mạng như thế sao nó không ị luôn trên cây cho khỏe ạ? Câu hỏi tuyệt vời của khán giả nhí cũng chính là điều khiến các nhà khoa học vò đầu bứt tai suốt nhiều thập kỷ!". Bố cục: Chú bé con hoạt hình gãi đầu ngơ ngác hỏi tại sao không ị luôn trên cây cho an toàn.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi xuống tới gốc cây, Con Lười dùng chiếc đuôi ngắn ngủn ngoáy một chiếc hố nhỏ trên nền đất rồi bắt đầu xả thải.". Bố cục: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân dùng chiếc đuôi ngắn ngủn ngoáy một chiếc hố nhỏ dưới đất rồi ngồi xổm xả thải với vẻ mặt cực kỳ mãn nguyện nhẹ nhõm.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quý vị hãy chuẩn bị tinh thần: vì nhịn suốt 1 tuần lễ, lượng phân và nước tiểu xả ra trong 1 lần đi vệ sinh có thể nặng tới 1/3 trọng lượng toàn bộ cơ thể nó! Đi vệ sinh xong một cái là chú lười nhẹ bẫng đi 30% cân nặng!". Bố cục: Cân đo tải trọng: đống phân thải ra nặng tới 1/3 trọng lượng cơ thể; chiếc cân giảm 30% cân nặng ngay tức khắc.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và mục đích sinh tử của chuyến đi này chính là để phục vụ bạn bè: khi lười đi vệ sinh, những cô bướm đêm trên lông sẽ bò xuống đẻ trứng vào đống phân tươi để ấu trùng phát triển, hoàn thành chu trình duy trì bộ lông xanh cho thế hệ lười tiếp theo!". Bố cục: Khi chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân xả phân, các cô bướm đêm Cryptoses từ trên lông bò túa xuống đẻ trứng vào đống phân tươi dưới đất để ấu trùng phát triển.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chấp nhận đối mặt tử thần 50% chỉ để giữ lời hứa với đàn bướm đêm, quả là một tình bạn sinh tử cảm động!". Bố cục: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân vẫy tay chào đàn bướm đêm rồi chậm rãi leo trở lại cây; tình bạn sinh tử 50% nguy hiểm cảm động.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Màn đêm chuyển về khuya, đồng hồ điểm 02:00 rạng sáng! Sau chuyến đi vệ sinh hú vía dưới mặt đất, Thánh sống chậm đã leo trở lại chạc cây an toàn. Nhưng hiểm nguy từ bầu trời lại bắt đầu rình rập!". Bố cục: Đồng hồ chỉ 02:00 rạng sáng; chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân đã leo lên chạc cây cao ngủ tiếp; trên bầu trời một bóng chim săn mồi khổng lồ lướt qua ánh trăng.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trên tầng tán rừng nhiệt đới, kẻ thù truyền kiếp đáng sợ nhất của loài lười đã xuất hiện: Đại bàng Harpy — bạo chúa bầu trời châu Mỹ với sải cánh dài hơn 2m và bộ móng vuốt to bằng móng gấu xám! Đại bàng Harpy chuyên lượn sát các ngọn cây để săn lùng khỉ và lười.". Bố cục: Bạo chúa bầu trời Đại bàng Harpy sải cánh hơn 2m với bộ móng vuốt to bằng móng gấu xám lượn sát cành cây.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng chính tốc độ rùa bò và bộ lông mọc rêu xanh lại trở thành tấm áo giáp tàng hình siêu việt cứu mạng Thánh sống chậm! Đại bàng bay lướt qua phía trên chỉ thấy một búi lá cây đung đưa bất động trong gió đêm.". Bố cục: Áo giáp tàng hình: bộ lông rêu xanh và sự bất động tuyệt đối của chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân biến chú thành một búi lá cây tự nhiên; đại bàng bay lướt qua không hề phát hiện.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và quý vị đừng tưởng chú lười hiền lành này không biết phản kháng nhé! Khi bị dồn vào chân tường, Con Lười có thể tung ra những cú cào vuốt móng thép sắc lẹm với tốc độ cực nhanh, đủ sức rạch toạc da thịt của kẻ săn mồi khiến báo đốm hay đại bàng cũng phải dè chừng lùi bước!". Bố cục: Cận cảnh cú phản đòn bất ngờ: khi bị đại bàng lao tới sát, chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân vung móng vuốt cào xé cực nhanh tóe lửa rạch rách móng kẻ thù.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chậm chạp có tính toán, bất động để sinh tồn, đó là bản lĩnh của kẻ sống sót qua hàng triệu năm!". Bố cục: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân thu móng vuốt lại, mỉm cười bình thản trên cây; đại bàng ôm mặt bay đi; bản lĩnh sinh tồn triệu năm.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và tình mẫu tử của loài lười cũng cảm động không kém! Chú lười con sinh ra chỉ nhỏ xíu bằng nắm tay, bám chặt vào ngực mẹ suốt 6 tháng trời ròng rã không rời nửa bước!". Bố cục: Chú lười con bé xíu bám chặt vào ngực lười mẹ suốt 6 tháng ròng rã; lười mẹ ôm con âu yếm.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Người mẹ lười dù chậm chạp đến đâu cũng sẽ bảo vệ con mình trước nanh vuốt của thú dữ, sẵn sàng giơ những chiếc móng vuốt 10cm sắc nhọn rạch toạc mặt bất kỳ kẻ săn mồi nào dám đụng vào đứa con bé bỏng! Chậm chạp nhưng không hề yếu hèn, đó chính là bản lĩnh sinh tồn của Thánh sống chậm!". Bố cục: Lười mẹ xòe móng vuốt sắc nhọn gầm gừ che chắn cho đứa con trước bóng một con mèo rừng gấm; ánh mắt người mẹ kiên cường.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bây giờ là 04:00 rạng sáng! Ánh bình minh le lói bắt đầu rọi xuống tán rừng già, khép lại 24 giờ tác nghiệp đầy cảm xúc theo chân Thánh sống chậm.". Bố cục: Rừng già lúc 04:00 rạng sáng, ánh bình minh le lói qua sương sớm; chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân ngồi thiền an nhiên trên chạc cây đón ngày mới.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhiều người thường lấy con lười ra làm biểu tượng cho sự lười nhác và thụt lùi, nhưng thực tế tiến hóa đã chứng minh: lối sống chậm rãi, tối giản hóa năng lượng và không tranh giành thức ăn với bất kỳ ai đã giúp Con Lười tồn tại bền bỉ qua hơn 30 triệu năm lịch sử!". Bố cục: Dòng thời gian 30 triệu năm: các loài thú hung hăng to lớn đều tuyệt chủng; riêng chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân vẫn ung dung sinh tồn qua 30 triệu năm.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đôi khi trong cuộc sống hối hả, biết sống chậm lại, tĩnh tâm và kiên định với con đường của riêng mình lại là cách sinh tồn thông minh và khôn ngoan nhất!". Bố cục: Triết lý sống: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân ngồi tĩnh tâm giữa dòng đời hối hả, xung quanh là biểu tượng hoa sen và năng lượng bình yên.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hành trình 24 giờ của Thánh sống chậm đã chính thức khép lại!". Bố cục: Đồng hồ 24h quay trọn một vòng; anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H chào tạm biệt khán giả khép lại nhật ký 24h.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng ngay bây giờ, xin mời quý vị khán giả hãy hướng mắt lên màn hình lớn để chiêm ngưỡng BÓNG ĐEN BÍ ẨN của nhân vật xuất hiện trong Tập 14 tiếp theo!". Bố cục: Màn hình lớn bỗng đổi màu tím thẫm bí ẩn; phông nền rực lửa Đấu Trường Sinh Tồn chuyển sang bóng tối; khán giả tò mò nghển cổ.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Xin gửi tới quý vị ba manh mối chấn động về bóng đen bí ẩn này: Thứ nhất, đây là siêu tội phạm lừa đảo khét tiếng bậc nhất thế giới loài chim, với tuyệt kỹ đẻ trộm trứng vào tổ của loài chim khác chỉ trong vỏn vẹn 10 giây!". Bố cục: BÓNG ĐEN BÍ ẨN (Solid Black Silhouette): Trên màn hình lớn hiện ra một cái bóng đen hoàn toàn của một loài chim bí ẩn đang lén lút thả một quả trứng vào tổ chim khác; dấu hỏi chấm màu vàng khổng lồ phát sáng rực rỡ ở giữa. KHÔNG có chú Con Lười trong cảnh này.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thứ hai, bản năng sát thủ tàn nhẫn đến rợn người: con non vừa chui ra khỏi vỏ trứng, mắt còn chưa mở, nhưng đã dùng chiếc lưng lõm hất tung toàn bộ trứng của chim chủ nhà rơi xuống đất vỡ nát!". Bố cục: BÓNG ĐEN BÍ ẨN (Solid Black Silhouette): Bóng đen của một chú chim non vừa chui ra khỏi vỏ trứng, mắt nhắm nghiền nhưng dùng chiếc lưng lõm hất văng quả trứng của chim chủ nhà rơi xuống vỡ toang; dấu hỏi chấm xoay tròn. KHÔNG có chú Con Lười trong cảnh này.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và thứ ba, nghịch lý bi hài: đôi chim bố mẹ nuôi còng lưng bón mồi cho một đứa con nuôi khổng lồ to gấp 3 lần chính mình! Quý vị". Bố cục: BÓNG ĐEN BÍ ẨN (Solid Black Silhouette): Bóng đen của hai chú chim bố mẹ bé tí hon đang kiệt sức bón mồi cho một con chim non khổng lồ to gấp 3 lần chính mình; dấu hỏi chấm nhấp nháy. KHÔNG có chú Con Lười trong cảnh này.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "khán giả có đoán ra bóng đen bí ẩn này là quái kiệt nào không? Hãy để lại phán quyết và dự đoán của bạn ngay dưới phần bình luận nhé! Phóng viên truyền hình xin chào tạm biệt và hẹn gặp lại quý vị trong bản tin sinh tồn kỳ thú tiếp theo!". Bố cục: Khán đài xôn xao háo hức: các bạn nhỏ và muông thú giơ biển dấu hỏi chấm tranh luận đoán tên quái kiệt; anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H giơ tay mời khán giả bình luận.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đổi lại, thảm tảo xanh biến Con Lười thành một búi lá cây ngụy trang hoàn hảo chống lại tầm mắt của kẻ thù từ trên cao, và những lúc đói lòng, chú lười chỉ việc liếm láp lớp tảo giàu chất béo này trên lông như một món ăn vặt bổ dưỡng!". Bố cục: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân hòa tan vào tán lá rừng ngụy trang tàng hình chống lại kẻ thù; thè lưỡi liếm lớp tảo giàu chất béo trên lông như món ăn vặt bổ dưỡng.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Một sinh vật lười biếng đến mức mất cả tháng trời chỉ để tiêu hóa một chiếc lá cây,". Bố cục: Dọc 9:16: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân treo ngược trên cành cây chậm rãi nhai một chiếc lá; anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H cầm micro kinh ngạc chỉ vào tờ lịch 1 tháng.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đó chính là Con Lười ba ngón, thánh sống chậm của rừng rậm Nam Mỹ với tốc độ chỉ 0,2km/h.". Bố cục: Giới thiệu dọc: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân mập mạp lông xám bùn có vệt rêu xanh, lười biếng bò trên cành với tốc độ 0,2km/h giữa rừng rậm Nam Mỹ.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Dạ dày 4 ngăn trao đổi chất cực chậm khiến một chiếc lá phải mất 30 ngày mới tiêu hóa xong,". Bố cục: Sơ đồ dạ dày 4 ngăn tiêu hóa 1 chiếc lá mất 30 ngày; tờ lịch 30 ngày bay lả tả.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "còn bộ lông phủ đầy tảo xanh biến nó thành một khu rừng di động cho hàng trăm con bướm đêm sinh sống.". Bố cục: Kính lúp soi cận cảnh lớp lông mọc rêu xanh thành khu rừng di động cho hàng trăm con bướm đêm Cryptoses bay lượn.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Nhưng kỳ lạ nhất là cứ đúng 1 tuần 1 lần, nó bắt buộc phải bò từ ngọn cây xuống đất để đi vệ sinh,". Bố cục: Đồng hồ báo thức đêm: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân bò từ ngọn cây xuống mặt đất ẩm ướt để đi vệ sinh 1 tuần 1 lần.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "xả tới 1/3 trọng lượng cơ thể!". Bố cục: Chiếc cân đo trọng lượng sụt giảm 1/3 ngay sau khi xả thải; chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân nhẹ bẫng đi 30% cân nặng.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Do di chuyển quá vụng về dưới đất,". Bố cục: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân lết chậm chạp vụng về dưới đất, bóng báo đốm và chó rừng nhe răng rình rập trong bóng đêm.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "hơn 50% số cái chết của loài lười đều diễn ra đúng vào thời điểm đi vệ sinh này!". Bố cục: Biển cảnh báo đầu lâu: con số 50% cái chết của loài lười đều diễn ra lúc đi vệ sinh dưới đất.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Vậy là bí mật đã rõ: con lười chấp nhận đối mặt với tử thần chỉ để bướm đêm trên lưng có chỗ đẻ trứng vào phân,". Bố cục: Các cô bướm đêm từ trên lông chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân bò xuống đẻ trứng vào đống phân tươi dưới đất để ấu trùng phát triển.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "giữ cho bộ lông luôn xanh ngụy trang". Bố cục: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân ngẩng mặt mỉm cười mãn nguyện, bộ lông rêu xanh hòa tan hoàn hảo vào tán lá rừng ngụy trang bất khả chiến bại.
```
</details>

<details><summary>S11</summary>

```text
HÌNH S11 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "để sinh tồn qua hàng triệu năm!". Bố cục: Cận cảnh chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân nháy mắt tươi cười an nhiên treo ngược trên cành cây cao, câu chốt trọn vẹn kết thúc video!
```
</details>

<details><summary>S12</summary>

```text
HÌNH S12 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Con Lười ba ngón lông vệt rêu xanh, mặt cười tủm tỉm ngơ ngác, đeo đồng hồ nhỏ ở cổ chân; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "nhưng mỗi tuần lại chấp nhận mạo hiểm tính mạng để làm một việc kỳ quặc!". Bố cục: Dọc: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân ngơ ngác chuẩn bị chuyến hành hương sinh tử xuống mặt đất; biển báo nguy hiểm toilet cắm ở gốc cây.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/61 của video YouTube về Con Lười). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân. Nhân vật phụ cố định: anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H; cô phát thanh viên tin tức hoạt hình xinh đẹp ngồi sau bàn trường quay thời sự. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/12 của video YouTube Shorts về Con Lười). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Con Lười ba ngón hoạt hình ngộ nghĩnh: bộ lông xơ xác màu xám bùn pha vệt xanh rêu mộc mạc, khuôn mặt tròn bè với quầng mắt sẫm màu như đeo kính râm hề hước, khóe miệng luôn nở nụ cười tủm tỉm an nhiên vô cực, hai mắt lim dim ngơ ngác, bốn bàn chân có móng vuốt cong vút dài sắc nhọn, đeo một chiếc đồng hồ đeo tay nhỏ xinh trên cổ chân. Nhân vật phụ: anh chàng phóng viên truyền hình hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H. 
```
</details>

## 7. SEO

- **title:** Tại Sao 50% Cái Chết Của Con Lười Xảy Ra Lúc Đi Vệ Sinh?! | Con Lười | Tập 13
- **hook_paragraph:** Con Lười di chuyển 0.24km/h, mất 30 ngày để tiêu hóa 1 chiếc lá, cổ xoay 270 độ và hệ sinh thái bướm đêm sống trên lông! Nhưng tại sao hơn 50% cái chết trong đời nó lại diễn ra đúng lúc mò xuống đất đi vệ sinh 1 tuần/lần? Khám phá nhật ký sinh tồn 24 giờ của Thánh sống chậm rừng Amazon.
- **question:** Bạn có đoán ra BÓNG ĐEN BÍ ẨN ở cuối video là quái kiệt nào không? (Gợi ý: đẻ trộm trứng trong 10 giây, con non hất vỡ trứng chủ nhà). Bình luận dự đoán nhé!
- **next_teaser:** Bóng đen bí ẩn — kẻ đẻ trộm trứng 10 giây và sát thủ chưa mở mắt đẩy vỡ trứng chủ nhà
- **shorts_title:** Tại Sao 50% Cái Chết Của Con Lười Xảy Ra Lúc Đi Vệ Sinh?! 🦥 #shorts #conluoi
- **shorts_desc:** Con Lười chậm 0.2km/h, mất 1 tháng tiêu hóa 1 chiếc lá và hơn 50% cái chết trong đời xảy ra đúng lúc đi vệ sinh 1 tuần/lần! Khám phá bí mật sinh tồn của thánh sống chậm rừng Amazon! 🦥🌿
- **bullets:** Tốc độ kỷ lục 0.24km/h, 1 tháng tiêu hóa 1 chiếc lá · Cổ xoay 270 độ nhờ 8-10 đốt sống cổ và móng vuốt khóa chết trên cây · Hệ sinh thái di động: Hàng trăm con bướm đêm và tảo xanh nuôi dưỡng nhau trên lông · Nghi lễ đi vệ sinh tử thần 1 tuần/lần: Xả 1/3 trọng lượng cơ thể và hơn 50% bị săn mồi
- **tags:** con lười, con luoi, sloth, con lười đi vệ sinh, tại sao con lười chậm, con lười bơi lội, thế giới động vật, động vật kỳ lạ, vẽ chuyện hoang dã, whiteboard animation, khoa học thú vị, nhật ký 24 giờ
- **hashtags:** #ConLuoi #Sloth #TheGioiDongVat #VeChuyenHoangDa #KhoaHoc

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-13-con-luoi
python src/episode/pipeline.py tts    projects/tap-13-con-luoi     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-13-con-luoi     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-13-con-luoi     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-13-con-luoi              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-13-con-luoi --force
python scripts/beat_sheet.py projects/tap-13-con-luoi               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-13-con-luoi/audio/shorts.wav projects/tap-13-con-luoi/renders/tap-13-con-luoi_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-13-con-luoi
python src/episode/pipeline.py seo    projects/tap-13-con-luoi
python src/episode/episode_doc.py     projects/tap-13-con-luoi
```

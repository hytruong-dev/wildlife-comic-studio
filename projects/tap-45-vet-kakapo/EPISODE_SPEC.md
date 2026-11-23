# TẬP 45 — VẸT KAKAPO · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-45-vet-kakapo`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-45-vet-kakapo`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F4` · **Persona giọng:** `phong_vien_24h` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Vẹt Kakapo |
| Tiêu đề YouTube | Quên Mình Không Biết Bay: Chú Vẹt Béo 4kg Leo Cây Nhảy Đập Bụng?! \| Vẹt Kakapo \| Tập 45 |
| Video dài | `renders/tap-45-vet-kakapo_long.mp4` — 8:59.4 (539.4s) |
| Shorts | `renders/tap-45-vet-kakapo_shorts.mp4` — 0:42.0 (42.0s) |
| Thumbnail | `renders/tap-45-vet-kakapo_thumbnail.jpg` |
| Số hình | dài 57 beat / 57 ảnh riêng; Shorts 8 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/57 của video YouTube về Vẹt Kakapo). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — 00 SÁNG — ĐI TÌM CHÚ VẸT BÉO QUÊN BAY TẠI NEW ZEALAND
*Thẻ chương:* BÂY GIỜ LÀ SÁU GIỜ SÁNG VÀ CUỘC ĐUA SINH TỒN HAI MƯƠI TƯ GIỜ BẮT ĐẦU

*Badge:* `06:00 SÁNG` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene01_p0.wav` (543 ký tự) · mood `hao_hung`

```text
Bây giờ là sáu giờ sáng! Và cuộc đua sinh tồn hai mươi tư giờ bắt đầu! Trực tiếp từ hiện trường rừng nguyên sinh đảo Codfish, miền nam New Zealand! Chúng tôi đang có mặt tại một trong những khu bảo tồn thiên nhiên nghiêm ngặt nhất hành tinh, nơi những thảm rêu xanh lục bảo phủ kín mặt đất và những thân cây cổ thụ ngút ngàn sương mù mờ ảo! Mục tiêu theo dõi hôm nay của chúng tôi là một nhân vật vô cùng đặc biệt: Một sinh vật có đôi cánh lộng lẫy của loài chim, nhưng lại hoàn toàn quên mất cách thức sử dụng chúng để bay lượn trên bầu trời!
```
**Part 1** → `audio/vs/scene01_p1.wav` (104 ký tự) · 🎭 cameo `phat_thanh_vien`

```text
Alo trường quay xin nghe! Phóng viên hiện trường đã bắt được tín hiệu định vị của nhân vật chính chưa ạ?
```
**Part 2** → `audio/vs/scene01_p2.wav` (437 ký tự) · mood `hao_hung`

```text
[surprise-wa] Báo cáo trường quay, tín hiệu máy dò sóng vô tuyến vừa reo vang inh ỏi! Hãy chĩa ống kính máy quay xuống dưới hốc rễ cây đước cổ thụ kia! Một khối lông tròn ung ủng màu xanh rêu đốm vàng đang ngủ say sưa, phát ra những tiếng ngáy khò khò rung rinh cả vạt cỏ! Đây chính là Kakapo, tên khoa học là Strigops habroptilus! Nhưng cả đoàn làm phim chúng tôi đều gọi thân mật anh bạn này là: Gã béo vô tri quên cách bay! [laughter]
```
**Part 3** → `audio/vs/scene01_p3.wav` (495 ký tự) · mood `tram_bi_an`

```text
Để quý vị dễ hình dung sự kỳ cục của nhân vật này: Trong khi toàn bộ các loài vẹt trên thế giới đều là những bậc thầy nhào lộn trên không trung, thì gã bạn này lại quyết định sống cả đời dưới mặt đất như một chú gà béo! Cơ thể gã nặng tới bốn cân, sở hữu gương mặt tròn xoe tấu hài giống hệt như một chú chim cú mèo lai với trái bơ khổng lồ! Đồng hồ sinh tồn của chúng ta vừa điểm những giây phút đầu tiên, và hãy cùng theo dõi xem gã béo này sẽ xoay xở thế nào trong suốt một ngày đêm sinh tồn!
```

### scene02 — 00 SÁNG — CẤU TẠO XƯƠNG ỨC PHẲNG LÌ VÀ ĐÔI CÁNH PHẾ LIỆU
*Thẻ chương:* MƯỜI GIỜ SÁNG MỔ XẺ GIẢI PHẪU ĐÔI CÁNH VÔ DỤNG NHẤT HÀNH TINH

*Badge:* `10:00 SÁNG` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene02_p0.wav` (487 ký tự) · mood `don_dap`

```text
Đồng hồ hiện trường điểm mười giờ sáng! Gã béo vô tri quên cách bay của chúng ta cuối cùng cũng chịu cựa quậy tỉnh giấc sau một giấc ngủ nướng kéo dài! Hãy cùng chuyên gia sinh học của chúng tôi kiểm tra cận cảnh giải phẫu thể trọng của nhân vật này! Chiều dài từ mỏ đến chóp đuôi của gã đạt khoảng sáu mươi xăng-ti-mét, nhưng khi đặt lên bàn cân kiểm tra, con số hiển thị khiến máy quay phải rung chuyển: Bốn cân tròn trĩnh! Đây chính là loài vẹt nặng nhất trên toàn bộ bề mặt Trái Đất!
```
**Part 1** → `audio/vs/scene02_p1.wav` (445 ký tự) · mood `don_dap`

```text
Nhưng tại sao một con chim to lớn nhường này lại không thể bay nổi dù chỉ một mét? Hãy nhìn vào tấm phim chụp X-quang lồng ngực: Ở loài chim biết bay thông thường, xương ức phát triển một chiếc gờ lưỡi hái nhô cao vút, đóng vai trò như điểm tựa vững chắc để neo giữ khối cơ ngực khổng lồ tạo lực đập cánh. Nhưng ở gã béo Kakapo, chiếc gờ lưỡi hái này đã thoái hóa phẳng lì như một tấm phản gỗ! Cơ ngực teo tóp đến mức gần như biến mất hoàn toàn!
```
**Part 2** → `audio/vs/scene02_p2.wav` (501 ký tự) · mood `hao_hung`

```text
[surprise-oh] Hậu quả của thảm họa giải phẫu này là gì? Đôi cánh của gã dù lông vũ vẫn mượt mà xanh biếc, nhưng chúng quá ngắn và yếu ớt so với thân hình bốn cân nặng nề! Chúng hoàn toàn không có khả năng nâng đỡ cơ thể gã bay lên khỏi mặt đất! Mỗi khi gã thử xòe cánh đập phành phạch trong tuyệt vọng, luồng gió tạo ra chỉ đủ làm bay vài sợi rêu khô dưới chân, còn cơ thể béo múp thì vẫn đứng chôn chân một chỗ! [laughter] Tiến hóa đã biến đôi cánh của gã thành một món phụ kiện trang trí đúng nghĩa!
```
**Part 3** → `audio/vs/scene02_p3.wav` (481 ký tự) · mood `tram_bi_an`

```text
Nguyên nhân sâu xa bắt nguồn từ lịch sử hàng triệu năm cô lập của quần đảo New Zealand! Trước khi con người đặt chân đến, hòn đảo này hoàn toàn không có bất kỳ loài thú ăn thịt mặt đất nào như hổ, báo, cáo, chồn. Kakapo sống trong một thiên đường ngập tràn thức ăn dưới chân mà không sợ bị săn đuổi. Tạo hóa đã thì thầm vào tai gã rằng: Cần gì phải tốn năng lượng bay lượn cho mệt nhọc? Cứ ăn no ngủ kỹ rồi đi bộ túc tắc là đủ sống rồi! Và thế là gã đã vứt bỏ khả năng bay quý giá!
```

### scene03 — 00 CHIỀU — CƠ CHẾ GIẢ LÀM BỤI CÂY VÀ MÙI HƯƠNG PHẢN CHỦ
*Thẻ chương:* MƯỜI LĂM GIỜ CHIỀU BÁO ĐỘNG ĐỎ VỀ CƠ CHẾ ĐỨNG HÌNH VÔ TRI

*Badge:* `15:00 CHIỀU` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene03_p0.wav` (468 ký tự) · mood `don_dap`

```text
Đồng hồ bấm giờ điểm mười lăm giờ chiều! Hiện trường rừng rậm đột ngột rơi vào tình trạng báo động khẩn cấp! Một bóng đen lướt qua tán lá rậm rạp, và chiếc máy quay tầm nhiệt của chúng tôi vừa ghi nhận một khoảnh khắc thót tim: Gã béo vô tri quên cách bay phát hiện ra mối nguy hiểm rình rập! Quý vị đoán xem gã sẽ làm gì? Chạy thục mạng? Trốn vào hang sâu? Không hề! Gã lập tức đứng hình phăng phắc, kéo đầu thụt vào cổ và giả vờ mình là một tảng đá bám đầy rêu xanh!
```
**Part 1** → `audio/vs/scene03_p1.wav` (86 ký tự) · 🎭 cameo `phat_thanh_vien`

```text
Trời ơi phóng viên ơi, con vẹt nó đứng đơ như pho tượng vậy có bị làm sao không đấy ạ?
```
**Part 2** → `audio/vs/scene03_p2.wav` (419 ký tự) · mood `hao_hung`

```text
[surprise-wa] Báo cáo trường quay, đây chính là cơ chế phản xạ sinh tồn độc nhất vô nhị mang tên phản xạ đứng hình của Kakapo! Suốt hàng triệu năm đối đầu với loài đại bàng Haast khổng lồ thời tiền sử vốn săn mồi bằng thị giác trên không, chiến thuật đứng im bất động giữa thảm rêu xanh đốm vàng từng giúp tổ tiên gã tàng hình hoàn hảo! Kẻ săn mồi từ trên trời nhìn xuống sẽ chỉ thấy một bụi rêu vô hại và bay qua luôn!
```
**Part 3** → `audio/vs/scene03_p3.wav` (516 ký tự) · mood `nghiem_trang_gia`

```text
Nhưng bi kịch ập đến khi người định cư mang theo chuột, mèo hoang và chồn ec-min lên đảo! Những kẻ săn mồi ngoại lai này không dùng mắt để săn chim, mà dùng khứu giác cực kỳ thính nhạy! Và oái oăm thay, Gã béo vô tri quên cách bay lại sở hữu một mùi hương cơ thể vô cùng ngọt ngào, thơm phức mùi mật ong rừng quyện với hoa quả chín nồng nàn! Đứng im bất động mà lại tỏa hương ngào ngạt chẳng khác nào gã đang bật đèn pha tín hiệu thông báo: Tôi là một bữa ăn bốn cân béo ngậy đang đợi các bạn tới xơi đây! [laughter]
```
**Part 4** → `audio/vs/scene03_p4.wav` (461 ký tự) · mood `tram_bi_an`

```text
Bù lại cho cơ chế tự vệ tấu hài đầy rủi ro này, Gã béo vô tri quên cách bay lại sở hữu một chỉ số sinh học đáng kinh ngạc: Tuổi thọ trung bình của Kakapo lên tới sáu mươi đến chín mươi năm! Đây là một trong những loài chim sống thọ nhất trên toàn bộ hành tinh Trái Đất! Các nhà sinh học giải thích rằng do không tốn năng lượng cho việc bay lượn trên trời, nhịp trao đổi chất của gã chậm rãi tựa như một chú rùa cạn, giúp các tế bào cơ thể lão hóa cực kỳ từ tốn!
```

### scene04 — 00 TỐI — THỢ LEO TRÈO CỪ KHÔI VÀ MÀN RƠI TỰ DO ĐẬP BỤNG
*Thẻ chương:* MƯỜI CHÍN GIỜ TỐI CHỨNG KIẾN PHA NHẢY DÙ TỰ SÁT TỪ CÂY CAO

*Badge:* `19:00 TỐI` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene04_p0.wav` (477 ký tự) · mood `hao_hung`

```text
Hoàng hôn buông xuống, đồng hồ hiện trường điểm mười chín giờ tối! Sau một ngày dài ngủ nướng và đứng đơ giả vờ làm bụi rêu, chiếc bụng đói cồn cào đã thúc giục gã béo thức tỉnh hoàn toàn! Lúc này, camera hồng ngoại của chúng tôi bắt trọn một kỹ năng bất ngờ: Dù không biết bay, nhưng Gã béo vô tri quên cách bay lại là một chuyên gia leo trèo cừ khôi bậc nhất cánh rừng! Gã dùng chiếc mỏ quặp cứng như móc sắt và đôi bàn chân bốn ngón khỏe khoắn để bám chặt vào vỏ cây cổ thụ!
```
**Part 1** → `audio/vs/scene04_p1.wav` (324 ký tự) · mood `hao_hung`

```text
Đặc biệt hơn nữa, chiếc mỏ quặp màu xám ngà của gã hoạt động chẳng khác nào một chiếc chân thứ ba thần thánh! Khi hai bàn chân bám vào vỏ cây xù xì, gã cắm phập chiếc mỏ cứng vào thân cây như chiếc móc leo núi chuyên nghiệp của vận động viên leo vách đá, đu toàn bộ khối thân bốn cân lên cành cao một cách vô cùng điệu nghệ!
```
**Part 2** → `audio/vs/scene04_p2.wav` (359 ký tự) · mood `hao_hung`

```text
Từng bước túc tắc chậm rãi nhưng cực kỳ chắc chắn, gã trèo thoăn thoắt lên thân cây rimu cao vút tới hai mươi mét! Mục tiêu của gã là những chùm quả rimu chín mọng ngọt ngào trên ngọn cây, món ăn khoái khẩu giàu dinh dưỡng chỉ nở rộ vài năm một lần! Nhìn gã ngồi vắt vẻo trên cành cao nhai nhồm nhoàm từng chùm quả quả thật trông vô cùng bình yên và thỏa mãn!
```
**Part 3** → `audio/vs/scene04_p3.wav` (410 ký tự) · mood `don_dap`

```text
[surprise-oh] Nhưng thưa quý vị, kịch tính hài hước nhất của bản tin hiện trường xảy ra ngay lúc này! Sau khi chén đẫy bụng quả rimu, thay vì tốn công leo ngược trở xuống từng bước một, gã béo nhìn xuống mặt đất sâu hun hút và dường như... quên mất bản thân mình hoàn toàn không biết bay! Gã ưỡn ngực, lấy đà, xòe rộng đôi cánh ngắn tũn rồi dũng cảm lao mình vút vào không trung như một chú đại bàng dũng mãnh!
```
**Part 4** → `audio/vs/scene04_p4.wav` (488 ký tự) · mood `hao_hung`

```text
Và điều gì phải đến đã đến: Lực nâng của không khí bằng không, trọng lực kéo khối thân bốn cân rơi tự do không phanh vùn vụt xuống dưới! Chiếc cánh chỉ hoạt động như một chiếc dù rách lắc lư loạng choạng, và BẸP! Gã đập thẳng bụng và mặt xuống đệm rêu dày cộp dưới gốc cây! Bụi rêu và lá khô bắn tung tóe mù mịt! Máy quay chúng tôi vội lao tới cấp cứu, nhưng gã béo chỉ lồm cồm bò dậy, lắc lắc cái đầu ngơ ngác chớp chớp mắt tự hỏi: Quái lạ, sao hôm nay trời cản gió dữ vậy ta? [laughter]
```

### scene05 — 00 ĐÊM — CUỘC ĐI BỘ VIỆT DÃ VÀ TIẾNG BOOMING VANG XA 5KM
*Thẻ chương:* HAI MƯƠI BA GIỜ ĐÊM ĐẠI NHẠC HỘI KHUẾCH ĐẠI ÂM THANH NĂM CÂY SỐ

*Badge:* `23:00 ĐÊM` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene05_p0.wav` (437 ký tự) · mood `don_dap`

```text
Đồng hồ sinh tồn đếm ngược điểm hai mươi ba giờ đêm! Toàn bộ khu rừng chìm vào bóng tối đặc quánh, và đây mới chính là thời khắc sân khấu đỉnh cao của Gã béo vô tri quên cách bay! Sau cú tiếp đất đập bụng tấu hài, gã bắt đầu một hành trình thể thao phi thường: Đi bộ việt dã xuyên đêm! Với đôi chân cơ bắp to lớn, gã có thể lầm lũi đi bộ hàng chục cây số đường rừng, leo qua các sườn đồi dốc đứng để tiến về đấu trường tán tỉnh bạn tình!
```
**Part 1** → `audio/vs/scene05_p1.wav` (96 ký tự) · 🎭 cameo `phat_thanh_vien`

```text
Ủa phóng viên ơi, trong đêm tối mù mịt thế này thì làm sao vẹt đực tìm được vẹt cái để hẹn hò ạ?
```
**Part 2** → `audio/vs/scene05_p2.wav` (478 ký tự) · mood `hao_hung`

```text
[surprise-wa] Câu hỏi tuyệt vời từ trường quay! Hãy nhìn vào công trình kiến trúc độc nhất vô nhị mà gã béo vừa tạo ra trên đỉnh đồi: Gã dùng móng vuốt cào bới tạo thành một chiếc hố hình lòng chảo sâu khoảng mười xăng-ti-mét! Chiếc hố đất này đóng vai trò như một chiếc phễu loa bát khuếch đại âm thanh sinh học! Gã bước xuống đáy hố, hít một hơi thật sâu làm phồng căng túi khí ở ngực như một quả bóng bay khổng lồ, rồi phát ra những tiếng kêu ồm ồm trầm đục mang tên booming!
```
**Part 3** → `audio/vs/scene05_p3.wav` (410 ký tự) · mood `tram_bi_an`

```text
Âm thanh tần số thấp này dội vào thành hố lòng chảo, được khuếch đại cực đại và truyền sóng âm xuyên qua màn đêm mù sương, vang xa tới năm cây số khắp các thung lũng xung quanh! Gã kiên trì phát loa phóng thanh suốt tám tiếng đồng hồ mỗi đêm, liên tục trong ba đến bốn tháng ròng rã chỉ để hy vọng một nàng vẹt cái nghe thấy và tìm đến! Một nỗ lực tình yêu vĩ đại và nhẫn nại bậc nhất trong thế giới loài chim!
```

### scene06 — 00 SÁNG HÔM SAU — KHÉP LẠI 24H VÀ BÀI HỌC GIỮ GÌN SỰ NGÂY THƠ
*Thẻ chương:* ĐỒNG HỒ LẠI ĐIỂM SÁU GIỜ SÁNG VÀ MỌI THỨ LÀM LẠI TỪ ĐẦU

*Badge:* `06:00 SÁNG HÔM SAU` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (498 ký tự) · mood `am_ap`

```text
Đồng hồ lại điểm sáu giờ sáng! Ánh nắng bình minh le lói xuyên qua màn sương sớm, và bản tin nhật ký hai mươi tư giờ của chúng tôi chính thức khép lại trọn vẹn một vòng quay sinh tồn! Gã béo vô tri quên cách bay lúc này đã mệt lử sau một đêm gào thét phát loa, lững thững bước về lại chiếc hốc rễ cây quen thuộc, cuộn tròn bộ lông xanh rêu lại để chuẩn bị cho một giấc ngủ nướng mới! Một ngày đầy ắp những cú ngã đập bụng, những pha đứng hình ngơ ngác, nhưng ngập tràn vẻ đẹp hồn nhiên của tạo hóa!
```
**Part 1** → `audio/vs/scene06_p1.wav` (456 ký tự) · mood `am_ap`

```text
Hiện nay trên toàn thế giới, quần thể loài vẹt Kakapo chỉ còn vỏn vẹn khoảng hai trăm năm mươi cá thể, mỗi chú vẹt đều được các nhà khoa học New Zealand gắn thiết bị theo dõi và chăm sóc từng quả trứng như bảo vật quốc gia! Câu chuyện của Kakapo dạy chúng ta một bài học sâu sắc: Sự ngây thơ không có lỗi, nhưng khi thế giới xung quanh biến đổi quá nhanh, những tâm hồn thuần khiết nhất lại chính là những sinh linh cần được nâng niu và chở che nhiều nhất!
```
**Part 2** → `audio/vs/scene06_p2.wav` (178 ký tự) · mood `hao_hung`

```text
Nếu được gửi một lời nhắn nhủ đến chú vẹt béo Kakapo, bạn sẽ khuyên chú bớt ăn quả rimu hay tập bay nhảy cẩn thận hơn? Hãy để lại bình luận chia sẻ cảm nghĩ của bạn bên dưới nhé!
```
**Part 3** → `audio/vs/scene06_p3.wav` (415 ký tự) · mood `tram_bi_an`

```text
Còn bây giờ, chiếc đồng hồ hai mươi tư giờ đang chuẩn bị đưa chúng ta đến với hồ sơ kỳ dị tiếp theo của tập bốn mươi sáu! Một loài động vật bí ẩn đến từ những cánh rừng nhiệt đới Indonesia hoang dã, sở hữu cặp răng nanh kỳ quái mọc ngược đâm xuyên qua cả sống mũi, uốn cong vòng lại và chực chờ đâm thủng chính hộp sọ của nó! Bạn có đoán được sinh vật mang nghịch lý tiến hóa tự sát rùng mình này là loài nào không?
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Quên mất mình không biết bay nhưng vẫn leo tót lên ngọn cây cao hai mươi mét rồi xòe cánh nhảy ùm xuống đập bụng bẹp dí! Đây là Kakapo, loài vẹt nặng nhất thế giới với thể trọng lên tới bốn cân, và cũng là loài vẹt duy nhất trên Trái Đất hoàn toàn quên mất cách bay! Sống hàng triệu năm ở New Zealand không có thú săn mồi, xương ức của gã thoái hóa phẳng lì khiến đôi cánh chỉ còn là vật trang trí. Khi gặp nguy hiểm, gã đứng hình phăng phắc giả làm bụi rêu, nhưng cơ thể lại tỏa ra mùi mật ong thơm phức mời gọi kẻ thù! Ban đêm, gã đi bộ hàng chục cây số, đào hố lòng chảo khuếch đại tiếng kêu vang xa tới năm cây số để gọi bạn tình. Đáng yêu và ngơ ngác vô số tội, hiện cả hành tinh chỉ còn vỏn vẹn khoảng hai trăm năm mươi cá thể được bảo tồn nghiêm ngặt!
```

**Whisper prompt:** `Vẹt Kakapo, Strigops habroptilus, Gã béo vô tri quên cách bay, đảo Codfish, New Zealand, 4 kg, không biết bay, quả rimu, booming, 5 km, Phóng viên 24h`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| bốn mươi lăm | 45 |
| Bốn mươi lăm | 45 |
| Tập bốn mươi lăm | Tập 45 |
| bốn mươi tư | 44 |
| Bốn mươi tư | 44 |
| bốn mươi sáu | 46 |
| Bốn mươi sáu | 46 |
| số bốn mươi lăm | số 45 |
| Số bốn mươi lăm | Số 45 |
| bốn cân | 4 kg |
| Bốn cân | 4 kg |
| sáu mươi xăng-ti-mét | 60 cm |
| Sáu mươi xăng-ti-mét | 60 cm |
| hai mươi mét | 20 mét |
| Hai mươi mét | 20 mét |
| năm cây số | 5 km |
| Năm cây số | 5 km |
| hai mươi tư giờ | 24 giờ |
| Hai mươi tư giờ | 24 giờ |
| sáu giờ sáng | 6:00 sáng |
| Sáu giờ sáng | 6:00 sáng |
| mười giờ sáng | 10:00 sáng |
| Mười giờ sáng | 10:00 sáng |
| mười lăm giờ chiều | 15:00 chiều |
| Mười lăm giờ chiều | 15:00 chiều |
| mười chín giờ tối | 19:00 tối |
| Mười chín giờ tối | 19:00 tối |
| hai mươi ba giờ đêm | 23:00 đêm |
| Hai mươi ba giờ đêm | 23:00 đêm |
| hai trăm năm mươi | 250 |
| Hai trăm năm mươi | 250 |
| hàng triệu năm | hàng triệu năm |
| Hàng triệu năm | Hàng triệu năm |
| hàng chục cây số | hàng chục km |
| Hàng chục cây số | Hàng chục km |
| hàng ngàn | hàng 1.000 |
| Hàng ngàn | Hàng 1.000 |
| chục cây số | chục km |
| không một | không 1 |
| Không một | Không 1 |
| triệu năm | triệu năm |
| một chú | 1 chú |
| Một chú | 1 chú |
| một loài | 1 loài |
| Một loài | 1 loài |
| một con | 1 con |
| Một con | 1 con |
| một chiếc | 1 chiếc |
| Một chiếc | 1 chiếc |
| một hòn đá | 1 hòn đá |
| Một hòn đá | 1 hòn đá |
| một bụi cây | 1 bụi cây |
| Một bụi cây | 1 bụi cây |
| một mùi hương | 1 mùi hương |
| Một mùi hương | 1 mùi hương |
| một cú nhảy | 1 cú nhảy |
| Một cú nhảy | 1 cú nhảy |
| một cái hố | 1 cái hố |
| Một cái hố | 1 cái hố |
| một hệ thống | 1 hệ thống |
| Một hệ thống | 1 hệ thống |
| một bài học | 1 bài học |
| Một bài học | 1 bài học |
| một phần | 1 phần |
| Một phần | 1 phần |
| một tiếng | 1 tiếng |
| Một tiếng | 1 tiếng |
| hai ngàn | 2.000 |
| Hai ngàn | 2.000 |
| vài năm một lần | vài năm 1 lần |
| năm một | năm 1 |
| sáu mươi | 60 |
| chín mươi | 90 |
| chân thứ ba | chân thứ 3 |
| ba đến bốn | 3 đến 4 |
| tám tiếng | 8 tiếng |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · 00 SÁNG — ĐI TÌM CHÚ VẸT BÉO QUÊN BAY TẠI NEW ZEALAND · 80.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.6 (10.6s) | L01 | Bây giờ là 6:00 sáng! Và cuộc đua sinh tồn 24 giờ bắt đầu! Trực tiếp từ hiện trường rừng nguyên sinh đảo Codfish, miền nam New Zealand! Chúng tôi đang có mặt tại một trong |  | Trực tiếp từ hiện trường rừng nguyên sinh New Zealand: chú chim bói cá phóng viên đeo kính cận, cổ đeo thẻ nhà báo dã ngoại và tay cầm micro đài truyền hình đang cầm micro nói trước ống kính, xung quanh là thảm rêu xanh ngọc và thân cây cổ thụ sương mù mờ ảo. |
| b02 | 00:10.6–00:19.3 (8.7s) | L02 | những khu bảo tồn thiên nhiên nghiêm ngặt nhất hành tinh, nơi những thảm rêu xanh lục bảo phủ kín mặt đất và những thân cây cổ thụ ngút ngàn sương mù mờ ảo! Mục tiêu theo dõi |  | Màn hình tín hiệu kết nối trường quay: phát thanh viên đài truyền hình cú tuyết đeo tai nghe ngồi trong trường quay tin tức thời sự đeo tai nghe đang theo dõi bản tin hiện trường trực tiếp; bản đồ New Zealand phát sáng điểm đỏ đảo Codfish. |
| b03 | 00:19.3–00:27.8 (8.5s) | L03 | hôm nay của chúng tôi là một nhân vật vô cùng đặc biệt: Một sinh vật có đôi cánh lộng lẫy của loài chim, nhưng lại hoàn toàn quên mất cách thức sử dụng chúng để bay lượn trên |  | chú chim bói cá phóng viên đeo kính cận, cổ đeo thẻ nhà báo dã ngoại và tay cầm micro đài truyền hình cầm máy dò sóng vô tuyến reo vang bíp bíp, chỉ tay về phía hốc rễ cây cổ thụ rêu phong rậm rạp. |
| b04 | 00:27.8–00:37.4 (9.6s) | L04 | bầu trời! Alo trường quay xin nghe! Phóng viên hiện trường đã bắt được tín hiệu định vị của nhân vật chính chưa ạ? Báo cáo trường quay, tín hiệu máy dò sóng vô tuyến vừa reo |  | Cận cảnh hốc cây: chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand tròn vo như một trái bơ khổng lồ đang ngủ say sưa, phát ra tiếng ngáy khò khò làm rung rinh vạt cỏ. |
| b05 | 00:37.4–00:46.1 (8.7s) | L05 | vang inh ỏi! Hãy chĩa ống kính máy quay xuống dưới hốc rễ cây đước cổ thụ kia! Một khối lông tròn ung ủng màu xanh rêu đốm vàng đang ngủ say sưa, phát ra những tiếng ngáy khò |  | chú chim bói cá phóng viên đeo kính cận, cổ đeo thẻ nhà báo dã ngoại và tay cầm micro đài truyền hình há hốc miệng kinh ngạc trước thân hình béo múp míp của chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand; nhãn tên khoa học Strigop |
| b06 | 00:46.1–00:57.1 (11.0s) | L06 | khò rung rinh cả vạt cỏ! Đây chính là Kakapo, tên khoa học là Strigops habroptilus! Nhưng cả đoàn làm phim chúng tôi đều gọi thân mật anh bạn này là: Gã béo vô tri quên cách bay! |  | So sánh tương phản hài hước: BÊN TRÁI là đàn vẹt sặc sỡ đang bay lượn nhào lộn điệu nghệ; BÊN PHẢI là chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand ngồi bẹp dí dưới đất ngơ ngác như một chú gà béo. |
| b07 | 00:57.1–01:04.2 (7.1s) | L07 | Để quý vị dễ hình dung sự kỳ cục của nhân vật này: Trong khi toàn bộ các loài vẹt trên thế giới đều là những bậc thầy nhào lộn trên không trung, thì gã bạn này |  | Bàn cân trọng lượng dã ngoại: chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand đứng lên khiến kim cân nhảy vọt qua vạch bốn cân; gương mặt tròn xoe tấu hài không chút bận tâm. |
| b08 | 01:04.2–01:12.4 (8.2s) | L08 | lại quyết định sống cả đời dưới mặt đất như 1 chú gà béo! Cơ thể gã nặng tới 4 kg, sở hữu gương mặt tròn xoe tấu hài giống hệt như 1 chú chim cú mèo lai | **4 KG** · thể trọng kỷ lục · R/360 · [0.75, 0.5] | Cận cảnh khuôn mặt ngây thơ: Đôi mắt tròn xoe đờ đẫn và chòm râu ria quanh mỏ của chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand trông vừa giống cú mèo vừa giống trái bơ chín. |
| b09 | 01:12.4–01:20.7 (8.3s) | L09 | với trái bơ khổng lồ! Đồng hồ sinh tồn của chúng ta vừa điểm những giây phút đầu tiên, và hãy cùng theo dõi xem gã béo này sẽ xoay xở thế nào trong suốt một ngày đêm sinh tồn! |  | Đồng hồ bấm giờ sinh tồn hai mươi tư giờ bắt đầu đếm ngược những giây đầu tiên; chú chim bói cá phóng viên đeo kính cận, cổ đeo thẻ nhà báo dã ngoại và tay cầm micro đài truyền hình nín thở rón rén đi theo dấu chân chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám r |

### scene02 · 00 SÁNG — CẤU TẠO XƯƠNG ỨC PHẲNG LÌ VÀ ĐÔI CÁNH PHẾ LIỆU · 93.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.9 (8.9s) | L10 | Đồng hồ hiện trường điểm 10:00 sáng! Gã béo vô tri quên cách bay của chúng ta cuối cùng cũng chịu cựa quậy tỉnh giấc sau một giấc ngủ nướng kéo dài! Hãy cùng chuyên gia sinh học của chúng tôi |  | Đồng hồ hiện trường điểm mười giờ sáng: chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand bắt đầu vươn vai cựa quậy tỉnh giấc sau một giấc ngủ nướng dài; chú chim bói cá phóng viên đeo kính cận, cổ đeo thẻ nhà báo dã ngoại và tay cầm |
| b02 | 00:08.9–00:18.5 (9.6s) | L11 | kiểm tra cận cảnh giải phẫu thể trọng của nhân vật này! Chiều dài từ mỏ đến chóp đuôi của gã đạt khoảng 60 cm, nhưng khi đặt lên bàn cân kiểm tra, con số hiển thị khiến máy quay phải rung | **60 CM** · chiều dài cơ thể · L/380 · [0.28, 0.5] | Thước đo chiều dài sinh học: chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand đứng nghiêm chỉnh từ mỏ đến chóp đuôi đạt sáu mươi xăng-ti-mét trên nền giấy kẻ ô cổ tích. |
| b03 | 00:18.5–00:27.7 (9.2s) | L12 | chuyển: 4 kg tròn trĩnh! Đây chính là loài vẹt nặng nhất trên toàn bộ bề mặt Trái Đất! Nhưng tại sao 1 con chim to lớn nhường này lại không thể bay nổi dù chỉ một mét? Hãy nhìn vào | **4 KG** · loài vẹt nặng nhất · R/360 · [0.75, 0.5] | Cúp vàng vinh danh: chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand đứng cạnh chiếc cúp loài vẹt nặng nhất thế giới; con số bốn cân vàng son nổi bật. |
| b04 | 00:27.7–00:35.6 (8.0s) | L13 | tấm phim chụp X-quang lồng ngực: Ở loài chim biết bay thông thường, xương ức phát triển 1 chiếc gờ lưỡi hái nhô cao vút, đóng vai trò như điểm tựa vững chắc để neo giữ khối cơ ngực khổng lồ tạo |  | Tấm phim chụp X-quang so sánh giải phẫu: Khung xương chim đại bàng với gờ xương ức nhô cao như lưỡi kiếm; bên cạnh là khung xương chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand với xương ức phẳng lì như tấm thớt. |
| b05 | 00:35.6–00:46.1 (10.5s) | L14 | lực đập cánh. Nhưng ở gã béo Kakapo, chiếc gờ lưỡi hái này đã thoái hóa phẳng lì như một tấm phản gỗ! Cơ ngực teo tóp đến mức gần như biến mất hoàn toàn! Hậu quả của thảm họa giải phẫu |  | Mô phỏng cơ sinh học: Cơ ngực của chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand teo nhỏ xíu không thể tạo lực vỗ cánh; chú chim bói cá phóng viên đeo kính cận, cổ đeo thẻ nhà báo dã ngoại và tay cầm micro đài truyền hình cầm bảng |
| b06 | 00:46.1–00:55.2 (9.1s) | L15 | này là gì? Đôi cánh của gã dù lông vũ vẫn mượt mà xanh biếc, nhưng chúng quá ngắn và yếu ớt so với thân hình 4 kg nặng nề! Chúng hoàn toàn không có khả năng nâng đỡ cơ thể gã |  | chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand cố gắng xòe cánh đập phành phạch trong vô vọng; gió chỉ làm bay vài sợi rêu khô dưới chân, khối thân bốn cân vẫn dính chặt mặt đất. |
| b07 | 00:55.2–01:06.1 (10.9s) | L16 | bay lên khỏi mặt đất! Mỗi khi gã thử xòe cánh đập phành phạch trong tuyệt vọng, luồng gió tạo ra chỉ đủ làm bay vài sợi rêu khô dưới chân, còn cơ thể béo múp thì vẫn đứng chôn chân một chỗ! Tiến |  | Tiến hóa chơi khăm: Đôi cánh của chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand được vẽ biến tấu thành một chiếc áo choàng lông vũ thời trang làm cảnh; chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm |
| b08 | 01:06.1–01:15.6 (9.5s) | L17 | hóa đã biến đôi cánh của gã thành một món phụ kiện trang trí đúng nghĩa! Nguyên nhân sâu xa bắt nguồn từ lịch sử hàng triệu năm cô lập của quần đảo New Zealand! Trước khi con người đặt chân đến, |  | Bức tranh tiền sử New Zealand: Thung lũng rêu phong màu ngọc bích ngập tràn hoa quả rụng, không hề có bóng dáng bất kỳ loài thú ăn thịt nào rình rập. |
| b09 | 01:15.6–01:24.1 (8.5s) | L18 | hòn đảo này hoàn toàn không có bất kỳ loài thú ăn thịt mặt đất nào như hổ, báo, cáo, chồn. Kakapo sống trong một thiên đường ngập tràn thức ăn dưới chân mà không sợ bị săn đuổi. Tạo |  | Tổ tiên Kakapo ung dung nhai quả dưới bóng râm, tự nhủ không cần bay lượn tốn sức; đôi cánh dần dần thoái hóa theo thời gian. |
| b10 | 01:24.1–01:33.0 (8.9s) | L19 | hóa đã thì thầm vào tai gã rằng: Cần gì phải tốn năng lượng bay lượn cho mệt nhọc? Cứ ăn no ngủ kỹ rồi đi bộ túc tắc là đủ sống rồi! Và thế là gã đã vứt bỏ khả năng bay quý giá! |  | chú chim bói cá phóng viên đeo kính cận, cổ đeo thẻ nhà báo dã ngoại và tay cầm micro đài truyền hình nhún vai cảm thán trước lựa chọn tiến hóa kỳ lạ của loài vẹt độc nhất vô nhị này. |

### scene03 · 00 CHIỀU — CƠ CHẾ GIẢ LÀM BỤI CÂY VÀ MÙI HƯƠNG PHẢN CHỦ · 94.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.6 (8.6s) | L20 | Đồng hồ bấm giờ điểm 15:00 chiều! Hiện trường rừng rậm đột ngột rơi vào tình trạng báo động khẩn cấp! Một bóng đen lướt qua tán lá rậm rạp, và chiếc máy quay tầm nhiệt của chúng tôi vừa ghi |  | Đồng hồ bấm giờ điểm mười lăm giờ chiều: Khu rừng đột ngột xào xạc lá cây báo động nguy hiểm; chú chim bói cá phóng viên đeo kính cận, cổ đeo thẻ nhà báo dã ngoại và tay cầm micro đài truyền hình nép mình sau thân cây thì thào. |
| b02 | 00:08.6–00:18.0 (9.4s) | L21 | nhận một khoảnh khắc thót tim: Gã béo vô tri quên cách bay phát hiện ra mối nguy hiểm rình rập! Quý vị đoán xem gã sẽ làm gì? Chạy thục mạng? Trốn vào hang sâu? Không hề! Gã lập tức đứng hình phăng phắc, |  | chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand phát hiện tiếng động lạ, lập tức rụt cổ thụt đầu, đứng đơ phăng phắc như một hòn đá bọc rêu không hề chớp mắt. |
| b03 | 00:18.0–00:28.2 (10.2s) | L22 | kéo đầu thụt vào cổ và giả vờ mình là một tảng đá bám đầy rêu xanh! Trời ơi phóng viên ơi, con vẹt nó đứng đơ như pho tượng vậy có bị làm sao không đấy ạ? Báo cáo trường quay, |  | phát thanh viên đài truyền hình cú tuyết đeo tai nghe ngồi trong trường quay tin tức thời sự trên màn hình truyền hình ôm trán dở khóc dở cười trước tư thế đứng hình tấu hài của chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand. |
| b04 | 00:28.2–00:37.6 (9.4s) | L23 | đây chính là cơ chế phản xạ sinh tồn độc nhất vô nhị mang tên phản xạ đứng hình của Kakapo! Suốt hàng triệu năm đối đầu với loài đại bàng Haast khổng lồ thời tiền sử vốn săn mồi bằng thị |  | Bầu trời thời tiền sử: bóng đen khổng lồ của đại bàng Haast thời tiền sử sải cánh 3 mét trên bầu trời đang lượn vòng săn mồi bằng mắt; phía dưới chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand đứng bất động hòa lẫn hoàn hảo vào thả |
| b05 | 00:37.6–00:48.5 (10.9s) | L24 | giác trên không, chiến thuật đứng im bất động giữa thảm rêu xanh đốm vàng từng giúp tổ tiên gã tàng hình hoàn hảo! Kẻ săn mồi từ trên trời nhìn xuống sẽ chỉ thấy một bụi rêu vô hại và bay qua luôn! Nhưng |  | Chiến thuật tàng hình thành công trước đại bàng: Đại bàng bay qua không nhìn thấy gì; chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand hé một bên mắt tinh quái cười thầm. |
| b06 | 00:48.5–00:56.9 (8.4s) | L25 | bi kịch ập đến khi người định cư mang theo chuột, mèo hoang và chồn ec-min lên đảo! Những kẻ săn mồi ngoại lai này không dùng mắt để săn chim, mà dùng khứu giác cực kỳ thính nhạy! Và oái |  | Con thuyền người định cư cập bến: Các loài động vật ngoại lai chuột, mèo và chú chồn ec-min nâu nhọn mũi đang hít hà đánh hơi mùi mật ong rừng tràn lên hòn đảo thiên đường. |
| b07 | 00:56.9–01:05.7 (8.8s) | L26 | oăm thay, Gã béo vô tri quên cách bay lại sở hữu 1 mùi hương cơ thể vô cùng ngọt ngào, thơm phức mùi mật ong rừng quyện với hoa quả chín nồng nàn! Đứng im bất động mà lại tỏa hương ngào ngạt |  | chú chồn ec-min nâu nhọn mũi đang hít hà đánh hơi mùi mật ong rừng dùng chiếc mũi thính nhạy hít hà đánh hơi; những dải hương thơm màu hồng phấn hình bông hoa bay lơ lửng từ người chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand. |
| b08 | 01:05.7–01:15.5 (9.8s) | L27 | chẳng khác nào gã đang bật đèn pha tín hiệu thông báo: Tôi là một bữa ăn 4 kg béo ngậy đang đợi các bạn tới xơi đây! Bù lại cho cơ chế tự vệ tấu hài đầy rủi ro này, Gã béo vô tri |  | Minh họa lọ nước hoa mật ong rừng và quả chín gắn trên lưng chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand; cơ chế tỏa hương ngọt ngào trở thành chiếc bẫy hi sinh bảo vệ tổ. |
| b09 | 01:15.5–01:24.9 (9.4s) | L28 | quên cách bay lại sở hữu một chỉ số sinh học đáng kinh ngạc: Tuổi thọ trung bình của Kakapo lên tới 60 đến 90 năm! Đây là một trong những loài chim sống thọ nhất trên toàn bộ hành tinh Trái Đất! | **60-90 NĂM** · tuổi thọ kỷ lục · L/380 · [0.3, 0.5] | Biểu đồ tuổi thọ sinh học: chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand rùa bò thong thả bên cột mốc sáu mươi đến chín mươi năm; loài chim sống thọ kỷ lục nhờ nhịp sống chậm rãi. |
| b10 | 01:24.9–01:34.0 (9.2s) | L29 | Các nhà sinh học giải thích rằng do không tốn năng lượng cho việc bay lượn trên trời, nhịp trao đổi chất của gã chậm rãi tựa như 1 chú rùa cạn, giúp các tế bào cơ thể lão hóa cực kỳ từ tốn! |  | chú chim bói cá phóng viên đeo kính cận, cổ đeo thẻ nhà báo dã ngoại và tay cầm micro đài truyền hình kiểm tra camera nhiệt, thở phào khi thấy mối nguy hiểm vừa đi qua; chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand bắt đầu nhúc n |

### scene04 · 00 TỐI — THỢ LEO TRÈO CỪ KHÔI VÀ MÀN RƠI TỰ DO ĐẬP BỤNG · 105.3s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.7 (9.7s) | L30 | Hoàng hôn buông xuống, đồng hồ hiện trường điểm 19:00 tối! Sau một ngày dài ngủ nướng và đứng đơ giả vờ làm bụi rêu, chiếc bụng đói cồn cào đã thúc giục gã béo thức tỉnh hoàn toàn! Lúc |  | Đồng hồ hiện trường điểm mười chín giờ tối hoàng hôn: Bầu trời nhuộm màu tím than và vàng cam; chiếc bụng đói của chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand sôi réo ùng ục. |
| b02 | 00:09.7–00:19.5 (9.8s) | L31 | này, camera hồng ngoại của chúng tôi bắt trọn một kỹ năng bất ngờ: Dù không biết bay, nhưng Gã béo vô tri quên cách bay lại là một chuyên gia leo trèo cừ khôi bậc nhất cánh rừng! Gã dùng |  | Kỹ năng leo trèo bất ngờ: chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand cắm phập chiếc mỏ quặp cứng như móc leo núi vào thân cây, đôi chân cơ bắp bám chắc đu người lên cao. |
| b03 | 00:19.5–00:28.9 (9.4s) | L32 | chiếc mỏ quặp cứng như móc sắt và đôi bàn chân bốn ngón khỏe khoắn để bám chặt vào vỏ cây cổ thụ! Đặc biệt hơn nữa, chiếc mỏ quặp màu xám ngà của gã hoạt động chẳng khác nào |  | chú chim bói cá phóng viên đeo kính cận, cổ đeo thẻ nhà báo dã ngoại và tay cầm micro đài truyền hình lia máy quay theo bước chân thoăn thoắt của chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand đang trèo lên thân cây ngọn cây cổ th |
| b04 | 00:28.9–00:38.4 (9.5s) | L33 | 1 chiếc chân thứ 3 thần thánh! Khi hai bàn chân bám vào vỏ cây xù xì, gã cắm phập chiếc mỏ cứng vào thân cây như chiếc móc leo núi chuyên nghiệp của vận động viên leo vách đá, đu |  | Đỉnh ngọn cây rimu cao hai mươi mét: chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand ngồi vắt vẻo trên cành cao, nhai nhồm nhoàm từng chùm quả rimu chín mọng ngọt ngào. |
| b05 | 00:38.4–00:48.6 (10.2s) | L34 | toàn bộ khối thân 4 kg lên cành cao một cách vô cùng điệu nghệ! Từng bước túc tắc chậm rãi nhưng cực kỳ chắc chắn, gã trèo thoăn thoắt lên thân cây rimu cao vút tới 20 mét! Mục | **20 MÉT** · độ cao ngọn cây · R/360 · [0.75, 0.5] | Khuôn mặt thỏa mãn tột cùng của chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand khi được no nê quả chín; vệt nước quả vàng ươm dính quanh mép mỏ. |
| b06 | 00:48.6–00:58.3 (9.7s) | L35 | tiêu của gã là những chùm quả rimu chín mọng ngọt ngào trên ngọn cây, món ăn khoái khẩu giàu dinh dưỡng chỉ nở rộ vài năm 1 lần! Nhìn gã ngồi vắt vẻo trên cành cao nhai nhồm nhoàm từng chùm |  | chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand đứng trên đầu cành cây nhìn xuống mặt đất hun hút bên dưới, ưỡn ngực xòe cánh tự tin như một chú đại bàng sắp cất cánh. |
| b07 | 00:58.3–01:07.8 (9.5s) | L36 | quả quả thật trông vô cùng bình yên và thỏa mãn! Nhưng thưa quý vị, kịch tính hài hước nhất của bản tin hiện trường xảy ra ngay lúc này! Sau khi chén đẫy bụng quả rimu, thay vì tốn công |  | Pha nhảy dù dũng cảm bảo vệ tổ: chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand lao mình vút vào không trung; đôi cánh ngắn tũn xòe ra loạng choạng như chiếc dù rách. |
| b08 | 01:07.8–01:16.9 (9.1s) | L37 | leo ngược trở xuống từng bước một, gã béo nhìn xuống mặt đất sâu hun hút và dường như... quên mất bản thân mình hoàn toàn không biết bay! Gã ưỡn ngực, lấy đà, xòe rộng đôi cánh ngắn tũn rồi |  | Trọng lực kéo khối thân bốn cân rơi tự do vùn vụt; chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand hoảng hốt mở to hai mắt, chiếc mỏ há hốc kêu quàng quạc. |
| b09 | 01:16.9–01:26.0 (9.1s) | L38 | dũng cảm lao mình vút vào không trung như 1 chú đại bàng dũng mãnh! Và điều gì phải đến đã đến: Lực nâng của không khí bằng không, trọng lực kéo khối thân 4 kg rơi tự do không phanh |  | Cú tiếp đất kinh thiên động địa: chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand đập thẳng bụng và mặt xuống thảm rêu dày đánh BẸP một tiếng; bụi lá và rêu bắn tung tóe. |
| b10 | 01:26.0–01:34.8 (8.7s) | L39 | vùn vụt xuống dưới! Chiếc cánh chỉ hoạt động như 1 chiếc dù rách lắc lư loạng choạng, và BẸP! Gã đập thẳng bụng và mặt xuống đệm rêu dày cộp dưới gốc cây! Bụi rêu và lá khô bắn tung |  | chú chim bói cá phóng viên đeo kính cận, cổ đeo thẻ nhà báo dã ngoại và tay cầm micro đài truyền hình ôm miệng nín cười khi thấy chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand lồm cồm bò dậy, lắc lắc đầu cho tỉnh táo với những chú |
| b11 | 01:34.8–01:45.3 (10.5s) | L40 | tóe mù mịt! Máy quay chúng tôi vội lao tới cấp cứu, nhưng gã béo chỉ lồm cồm bò dậy, lắc lắc cái đầu ngơ ngác chớp chớp mắt tự hỏi: Quái lạ, sao hôm nay trời cản gió dữ vậy ta? |  | chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand phủi phủi lông ngực, ung dung bước tiếp như chưa từng có pha đập mặt thảm họa nào xảy ra. |

### scene05 · 00 ĐÊM — CUỘC ĐI BỘ VIỆT DÃ VÀ TIẾNG BOOMING VANG XA 5KM · 70.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.2 (8.2s) | L41 | Đồng hồ sinh tồn đếm ngược điểm 23:00 đêm! Toàn bộ khu rừng chìm vào bóng tối đặc quánh, và đây mới chính là thời khắc sân khấu đỉnh cao của Gã béo vô tri quên cách bay! |  | Đồng hồ hiện trường điểm hai mươi ba giờ đêm: Rừng rậm tối đen như mực; chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand bắt đầu sải bước việt dã mạnh mẽ xuyên qua các lối mòn. |
| b02 | 00:08.2–00:15.7 (7.4s) | L42 | Sau cú tiếp đất đập bụng tấu hài, gã bắt đầu một hành trình thể thao phi thường: Đi bộ việt dã xuyên đêm! Với đôi chân cơ bắp to lớn, gã có thể lầm lũi đi bộ |  | phát thanh viên đài truyền hình cú tuyết đeo tai nghe ngồi trong trường quay tin tức thời sự đặt câu hỏi thắc mắc làm sao các chú vẹt tìm thấy nhau trong màn đêm mịt mù của cánh rừng nguyên sinh. |
| b03 | 00:15.7–00:23.9 (8.3s) | L43 | hàng chục km đường rừng, leo qua các sườn đồi dốc đứng để tiến về đấu trường tán tỉnh bạn tình! Ủa phóng viên ơi, trong đêm tối mù mịt thế này thì làm sao vẹt đực tìm được vẹt |  | chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand đứng trên đỉnh đồi lộng gió, dùng móng vuốt cào bới tạo thành một chiếc hố hình lòng chảo sâu mười xăng-ti-mét trên nền đất mềm. |
| b04 | 00:23.9–00:33.5 (9.6s) | L44 | cái để hẹn hò ạ? Câu hỏi tuyệt vời từ trường quay! Hãy nhìn vào công trình kiến trúc độc nhất vô nhị mà gã béo vừa tạo ra trên đỉnh đồi: Gã dùng móng vuốt cào bới |  | Sơ đồ âm học phễu loa: Chiếc hố đất hoạt động như bộ khuếch đại sóng âm; chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand đứng giữa hố hít căng lồng ngực phồng to như quả bóng. |
| b05 | 00:33.5–00:43.1 (9.6s) | L45 | tạo thành 1 chiếc hố hình lòng chảo sâu khoảng mười xăng-ti-mét! Chiếc hố đất này đóng vai trò như 1 chiếc phễu loa bát khuếch đại âm thanh sinh học! Gã bước xuống đáy hố, hít một hơi thật |  | Đại nhạc hội xuyên đêm: Những đợt sóng âm tần số thấp booming ồm ồm lan tỏa từ chiếc hố, rung chuyển cả màn đêm yên tĩnh. |
| b06 | 00:43.1–00:52.9 (9.7s) | L46 | sâu làm phồng căng túi khí ở ngực như một quả bóng bay khổng lồ, rồi phát ra những tiếng kêu ồm ồm trầm đục mang tên booming! Âm thanh tần số thấp này dội vào thành hố lòng chảo, |  | Bản đồ radar âm thanh: Vòng tròn sóng âm lan tỏa bao phủ bán kính năm cây số khắp các thung lũng xung quanh. |
| b07 | 00:52.9–01:01.2 (8.4s) | L47 | được khuếch đại cực đại và truyền sóng âm xuyên qua màn đêm mù sương, vang xa tới 5 km khắp các thung lũng xung quanh! Gã kiên trì phát loa phóng thanh suốt 8 tiếng đồng | **5 KM** · bán kính âm thanh · R/360 · [0.75, 0.5] | chú chim bói cá phóng viên đeo kính cận, cổ đeo thẻ nhà báo dã ngoại và tay cầm micro đài truyền hình đeo tai nghe âm thanh chuyên dụng, giơ micro thu lại những tiếng booming kiên trì suốt tám tiếng của chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguy |
| b08 | 01:01.2–01:10.0 (8.8s) | L48 | hồ mỗi đêm, liên tục trong 3 đến 4 tháng ròng rã chỉ để hy vọng một nàng vẹt cái nghe thấy và tìm đến! Một nỗ lực tình yêu vĩ đại và nhẫn nại bậc nhất trong thế giới loài chim! |  | Bóng dáng một nàng vẹt cái e ấp từ xa đang lần theo tiếng gọi tình yêu bước về phía đỉnh đồi trong niềm hy vọng. |

### scene06 · 00 SÁNG HÔM SAU — KHÉP LẠI 24H VÀ BÀI HỌC GIỮ GÌN SỰ NGÂY THƠ · 76.1s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.6 (8.6s) | L49 | Đồng hồ lại điểm 6:00 sáng! Ánh nắng bình minh le lói xuyên qua màn sương sớm, và bản tin nhật ký 24 giờ của chúng tôi chính thức khép lại trọn vẹn một vòng quay |  | Đồng hồ lại điểm sáu giờ sáng hôm sau: Ánh nắng bình minh vàng dịu chiếu qua màn sương sớm; bản tin hai mươi tư giờ khép lại một vòng quay. |
| b02 | 00:08.6–00:16.4 (7.7s) | L50 | sinh tồn! Gã béo vô tri quên cách bay lúc này đã mệt lử sau một đêm gào thét phát loa, lững thững bước về lại chiếc hốc rễ cây quen thuộc, cuộn tròn bộ lông xanh |  | chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand mệt lử sau đêm dài phát loa, lững thững bước về chiếc hốc rễ cây quen thuộc, cuộn tròn bộ lông xanh rêu đi ngủ nướng. |
| b03 | 00:16.4–00:24.8 (8.4s) | L51 | rêu lại để chuẩn bị cho một giấc ngủ nướng mới! Một ngày đầy ắp những cú ngã đập bụng, những pha đứng hình ngơ ngác, nhưng ngập tràn vẻ đẹp hồn nhiên của tạo hóa! Hiện |  | Trung tâm bảo tồn New Zealand: Các nhà khoa học nâng niu chăm sóc từng quả trứng và gắn thiết bị bảo vệ cho chú vẹt béo quý giá. |
| b04 | 00:24.8–00:33.5 (8.8s) | L52 | nay trên toàn thế giới, quần thể loài vẹt Kakapo chỉ còn vỏn vẹn khoảng 250 cá thể, mỗi chú vẹt đều được các nhà khoa học New Zealand gắn thiết bị theo dõi và chăm sóc | **250 CÁ THỂ** · quần thể toàn cầu · R/360 · [0.75, 0.5] | Tấm bảng thống kê bảo tồn: Con số hai trăm năm mươi cá thể ít ỏi được khoanh tròn trang trọng như những báu vật của Trái Đất. |
| b05 | 00:33.5–00:42.2 (8.7s) | L53 | từng quả trứng như bảo vật quốc gia! Câu chuyện của Kakapo dạy chúng ta 1 bài học sâu sắc: Sự ngây thơ không có lỗi, nhưng khi thế giới xung quanh biến đổi quá nhanh, những tâm |  | chú chim bói cá phóng viên đeo kính cận, cổ đeo thẻ nhà báo dã ngoại và tay cầm micro đài truyền hình khép sổ tay hiện trường, mỉm cười nhìn chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand đang say ngủ với thông điệp trân trọng sự  |
| b06 | 00:42.2–00:50.8 (8.5s) | L54 | hồn thuần khiết nhất lại chính là những sinh linh cần được nâng niu và chở che nhiều nhất! Nếu được gửi một lời nhắn nhủ đến chú vẹt béo Kakapo, bạn sẽ khuyên chú bớt |  | Màn hình tương tác người xem: Khung bình luận mở ra mời khán giả chia sẻ lời nhắn nhủ yêu thương đến chú vẹt béo Kakapo. |
| b07 | 00:50.8–00:59.1 (8.4s) | L55 | ăn quả rimu hay tập bay nhảy cẩn thận hơn? Hãy để lại bình luận chia sẻ cảm nghĩ của bạn bên dưới nhé! Còn bây giờ, chiếc đồng hồ 24 giờ đang chuẩn bị đưa chúng ta |  | Hồ sơ mật tập bốn mươi sáu hé lộ: Một chú lợn rừng kỳ lạ Babirusa giữa rừng rậm nhiệt đới Indonesia với cặp răng nanh uốn cong đâm xuyên sống mũi. |
| b08 | 00:59.1–01:07.7 (8.6s) | L56 | đến với hồ sơ kỳ dị tiếp theo của tập 46! 1 loài động vật bí ẩn đến từ những cánh rừng nhiệt đới Indonesia hoang dã, sở hữu cặp răng nanh kỳ quái mọc ngược đâm |  | Cận cảnh cặp răng nanh nhọn hoắt tự đâm ngược vào trán hộp sọ một cách bí hiểm; dấu hỏi chấm xoay quanh sinh vật hi sinh bảo vệ tổ tiến hóa. |
| b09 | 01:07.7–01:16.1 (8.4s) | L57 | xuyên qua cả sống mũi, uốn cong vòng lại và chực chờ đâm thủng chính hộp sọ của nó! Bạn có đoán được sinh vật mang nghịch lý tiến hóa tự sát rùng mình này là loài nào không? |  | Màn hình kết thúc: Dòng chữ HẸN GẶP LẠI Ở TẬP 46 LỢN HƯƠU BABIRUSA lung linh với lời kêu gọi đăng ký kênh theo dõi. |

## 5. Phân cảnh Shorts — từng beat

Banner: **QUÊN MÌNH KHÔNG BIẾT BAY / LEO 20M NHẢY ĐẬP BỤNG?!** · giọng 40.5s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Quên mất mình không biết bay nhưng vẫn leo tót lên ngọn cây cao 20 mét rồi xòe cánh |  |
| s02 | 00:05.1 | S02 | nhảy ùm xuống đập bụng bẹp dí! Đây là Kakapo, loài vẹt nặng nhất thế giới với thể trọng lên | **4 KG** · vẹt nặng nhất · L/500 · [0.3, 0.5] |
| s03 | 00:10.2 | S03 | tới 4 kg, và cũng là loài vẹt duy nhất trên Trái Đất hoàn toàn quên mất cách bay! Sống hàng |  |
| s04 | 00:15.3 | S04 | triệu năm ở New Zealand không có thú săn mồi, xương ức của gã thoái hóa phẳng lì khiến đôi cánh |  |
| s05 | 00:20.2 | S05 | chỉ còn là vật trang trí. Khi gặp nguy hiểm, gã đứng hình phăng phắc giả làm bụi rêu, nhưng cơ |  |
| s06 | 00:25.3 | S06 | thể lại tỏa ra mùi mật ong thơm phức mời gọi kẻ thù! Ban đêm, gã đi bộ hàng chục km, |  |
| s07 | 00:30.1 | S07 | đào hố lòng chảo khuếch đại tiếng kêu vang xa tới 5 km để gọi bạn tình. Đáng yêu và ngơ ngác vô số tội, hiện | **5 KM** · loa phóng thanh · R/520 · [0.7, 0.5] |
| s08 | 00:36.0 | S08 | cả hành tinh chỉ còn vỏn vẹn khoảng 250 cá thể được bảo tồn nghiêm ngặt! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bây giờ là 6:00 sáng! Và cuộc đua sinh tồn 24 giờ bắt đầu! Trực tiếp từ hiện trường rừng nguyên sinh đảo Codfish, miền nam New Zealand! Chúng tôi đang có mặt tại một trong những khu". Bố cục: Trực tiếp từ hiện trường rừng nguyên sinh New Zealand: chú chim bói cá phóng viên đeo kính cận, cổ đeo thẻ nhà báo dã ngoại và tay cầm micro đài truyền hình đang cầm micro nói trước ống kính, xung quanh là thảm rêu xanh ngọc và thân cây cổ thụ sương mù mờ ảo.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bảo tồn thiên nhiên nghiêm ngặt nhất hành tinh, nơi những thảm rêu xanh lục bảo phủ kín mặt đất và những thân cây cổ thụ ngút ngàn sương mù mờ ảo! Mục tiêu theo dõi hôm nay". Bố cục: Màn hình tín hiệu kết nối trường quay: phát thanh viên đài truyền hình cú tuyết đeo tai nghe ngồi trong trường quay tin tức thời sự đeo tai nghe đang theo dõi bản tin hiện trường trực tiếp; bản đồ New Zealand phát sáng điểm đỏ đảo Codfish.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "của chúng tôi là một nhân vật vô cùng đặc biệt: Một sinh vật có đôi cánh lộng lẫy của loài chim, nhưng lại hoàn toàn quên mất cách thức sử dụng chúng để bay lượn trên bầu". Bố cục: chú chim bói cá phóng viên đeo kính cận, cổ đeo thẻ nhà báo dã ngoại và tay cầm micro đài truyền hình cầm máy dò sóng vô tuyến reo vang bíp bíp, chỉ tay về phía hốc rễ cây cổ thụ rêu phong rậm rạp.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "trời! Alo trường quay xin nghe! Phóng viên hiện trường đã bắt được tín hiệu định vị của nhân vật chính chưa ạ? Báo cáo trường quay, tín hiệu máy dò sóng vô tuyến vừa reo vang inh". Bố cục: Cận cảnh hốc cây: chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand tròn vo như một trái bơ khổng lồ đang ngủ say sưa, phát ra tiếng ngáy khò khò làm rung rinh vạt cỏ.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "ỏi! Hãy chĩa ống kính máy quay xuống dưới hốc rễ cây đước cổ thụ kia! Một khối lông tròn ung ủng màu xanh rêu đốm vàng đang ngủ say sưa, phát ra những tiếng ngáy khò khò". Bố cục: chú chim bói cá phóng viên đeo kính cận, cổ đeo thẻ nhà báo dã ngoại và tay cầm micro đài truyền hình há hốc miệng kinh ngạc trước thân hình béo múp míp của chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand; nhãn tên khoa học Strigops habroptilus và biệt danh GÃ BÉO VÔ TRI QUÊN CÁCH BAY hiện lên.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "rung rinh cả vạt cỏ! Đây chính là Kakapo, tên khoa học là Strigops habroptilus! Nhưng cả đoàn làm phim chúng tôi đều gọi thân mật anh bạn này là: Gã béo vô tri quên cách bay! Để". Bố cục: So sánh tương phản hài hước: BÊN TRÁI là đàn vẹt sặc sỡ đang bay lượn nhào lộn điệu nghệ; BÊN PHẢI là chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand ngồi bẹp dí dưới đất ngơ ngác như một chú gà béo.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "quý vị dễ hình dung sự kỳ cục của nhân vật này: Trong khi toàn bộ các loài vẹt trên thế giới đều là những bậc thầy nhào lộn trên không trung, thì gã bạn này lại quyết". Bố cục: Bàn cân trọng lượng dã ngoại: chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand đứng lên khiến kim cân nhảy vọt qua vạch bốn cân; gương mặt tròn xoe tấu hài không chút bận tâm.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "định sống cả đời dưới mặt đất như 1 chú gà béo! Cơ thể gã nặng tới 4 kg, sở hữu gương mặt tròn xoe tấu hài giống hệt như 1 chú chim cú mèo lai với trái". Bố cục: Cận cảnh khuôn mặt ngây thơ: Đôi mắt tròn xoe đờ đẫn và chòm râu ria quanh mỏ của chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand trông vừa giống cú mèo vừa giống trái bơ chín.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bơ khổng lồ! Đồng hồ sinh tồn của chúng ta vừa điểm những giây phút đầu tiên, và hãy cùng theo dõi xem gã béo này sẽ xoay xở thế nào trong suốt một ngày đêm sinh tồn!". Bố cục: Đồng hồ bấm giờ sinh tồn hai mươi tư giờ bắt đầu đếm ngược những giây đầu tiên; chú chim bói cá phóng viên đeo kính cận, cổ đeo thẻ nhà báo dã ngoại và tay cầm micro đài truyền hình nín thở rón rén đi theo dấu chân chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đồng hồ hiện trường điểm 10:00 sáng! Gã béo vô tri quên cách bay của chúng ta cuối cùng cũng chịu cựa quậy tỉnh giấc sau một giấc ngủ nướng kéo dài! Hãy cùng chuyên gia sinh học của chúng tôi kiểm". Bố cục: Đồng hồ hiện trường điểm mười giờ sáng: chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand bắt đầu vươn vai cựa quậy tỉnh giấc sau một giấc ngủ nướng dài; chú chim bói cá phóng viên đeo kính cận, cổ đeo thẻ nhà báo dã ngoại và tay cầm micro đài truyền hình quan sát ghi chép.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tra cận cảnh giải phẫu thể trọng của nhân vật này! Chiều dài từ mỏ đến chóp đuôi của gã đạt khoảng 60 cm, nhưng khi đặt lên bàn cân kiểm tra, con số hiển thị khiến máy quay phải rung chuyển:". Bố cục: Thước đo chiều dài sinh học: chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand đứng nghiêm chỉnh từ mỏ đến chóp đuôi đạt sáu mươi xăng-ti-mét trên nền giấy kẻ ô cổ tích.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "4 kg tròn trĩnh! Đây chính là loài vẹt nặng nhất trên toàn bộ bề mặt Trái Đất! Nhưng tại sao 1 con chim to lớn nhường này lại không thể bay nổi dù chỉ một mét? Hãy nhìn vào tấm phim". Bố cục: Cúp vàng vinh danh: chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand đứng cạnh chiếc cúp loài vẹt nặng nhất thế giới; con số bốn cân vàng son nổi bật.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chụp X-quang lồng ngực: Ở loài chim biết bay thông thường, xương ức phát triển 1 chiếc gờ lưỡi hái nhô cao vút, đóng vai trò như điểm tựa vững chắc để neo giữ khối cơ ngực khổng lồ tạo lực đập". Bố cục: Tấm phim chụp X-quang so sánh giải phẫu: Khung xương chim đại bàng với gờ xương ức nhô cao như lưỡi kiếm; bên cạnh là khung xương chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand với xương ức phẳng lì như tấm thớt.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cánh. Nhưng ở gã béo Kakapo, chiếc gờ lưỡi hái này đã thoái hóa phẳng lì như một tấm phản gỗ! Cơ ngực teo tóp đến mức gần như biến mất hoàn toàn! Hậu quả của thảm họa giải phẫu này là". Bố cục: Mô phỏng cơ sinh học: Cơ ngực của chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand teo nhỏ xíu không thể tạo lực vỗ cánh; chú chim bói cá phóng viên đeo kính cận, cổ đeo thẻ nhà báo dã ngoại và tay cầm micro đài truyền hình cầm bảng chẩn đoán chỉ tay giải thích.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "gì? Đôi cánh của gã dù lông vũ vẫn mượt mà xanh biếc, nhưng chúng quá ngắn và yếu ớt so với thân hình 4 kg nặng nề! Chúng hoàn toàn không có khả năng nâng đỡ cơ thể gã bay lên". Bố cục: chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand cố gắng xòe cánh đập phành phạch trong vô vọng; gió chỉ làm bay vài sợi rêu khô dưới chân, khối thân bốn cân vẫn dính chặt mặt đất.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "khỏi mặt đất! Mỗi khi gã thử xòe cánh đập phành phạch trong tuyệt vọng, luồng gió tạo ra chỉ đủ làm bay vài sợi rêu khô dưới chân, còn cơ thể béo múp thì vẫn đứng chôn chân một chỗ! Tiến". Bố cục: Tiến hóa chơi khăm: Đôi cánh của chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand được vẽ biến tấu thành một chiếc áo choàng lông vũ thời trang làm cảnh; chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand xoay người tạo dáng hài hước.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hóa đã biến đôi cánh của gã thành một món phụ kiện trang trí đúng nghĩa! Nguyên nhân sâu xa bắt nguồn từ lịch sử hàng triệu năm cô lập của quần đảo New Zealand! Trước khi con người đặt chân đến,". Bố cục: Bức tranh tiền sử New Zealand: Thung lũng rêu phong màu ngọc bích ngập tràn hoa quả rụng, không hề có bóng dáng bất kỳ loài thú ăn thịt nào rình rập.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hòn đảo này hoàn toàn không có bất kỳ loài thú ăn thịt mặt đất nào như hổ, báo, cáo, chồn. Kakapo sống trong một thiên đường ngập tràn thức ăn dưới chân mà không sợ bị săn đuổi. Tạo hóa đã". Bố cục: Tổ tiên Kakapo ung dung nhai quả dưới bóng râm, tự nhủ không cần bay lượn tốn sức; đôi cánh dần dần thoái hóa theo thời gian.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thì thầm vào tai gã rằng: Cần gì phải tốn năng lượng bay lượn cho mệt nhọc? Cứ ăn no ngủ kỹ rồi đi bộ túc tắc là đủ sống rồi! Và thế là gã đã vứt bỏ khả năng bay quý giá!". Bố cục: chú chim bói cá phóng viên đeo kính cận, cổ đeo thẻ nhà báo dã ngoại và tay cầm micro đài truyền hình nhún vai cảm thán trước lựa chọn tiến hóa kỳ lạ của loài vẹt độc nhất vô nhị này.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đồng hồ bấm giờ điểm 15:00 chiều! Hiện trường rừng rậm đột ngột rơi vào tình trạng báo động khẩn cấp! Một bóng đen lướt qua tán lá rậm rạp, và chiếc máy quay tầm nhiệt của chúng tôi vừa ghi nhận một". Bố cục: Đồng hồ bấm giờ điểm mười lăm giờ chiều: Khu rừng đột ngột xào xạc lá cây báo động nguy hiểm; chú chim bói cá phóng viên đeo kính cận, cổ đeo thẻ nhà báo dã ngoại và tay cầm micro đài truyền hình nép mình sau thân cây thì thào.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "khoảnh khắc thót tim: Gã béo vô tri quên cách bay phát hiện ra mối nguy hiểm rình rập! Quý vị đoán xem gã sẽ làm gì? Chạy thục mạng? Trốn vào hang sâu? Không hề! Gã lập tức đứng hình phăng phắc,". Bố cục: chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand phát hiện tiếng động lạ, lập tức rụt cổ thụt đầu, đứng đơ phăng phắc như một hòn đá bọc rêu không hề chớp mắt.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "kéo đầu thụt vào cổ và giả vờ mình là một tảng đá bám đầy rêu xanh! Trời ơi phóng viên ơi, con vẹt nó đứng đơ như pho tượng vậy có bị làm sao không đấy ạ? Báo cáo trường quay, đây". Bố cục: phát thanh viên đài truyền hình cú tuyết đeo tai nghe ngồi trong trường quay tin tức thời sự trên màn hình truyền hình ôm trán dở khóc dở cười trước tư thế đứng hình tấu hài của chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chính là cơ chế phản xạ sinh tồn độc nhất vô nhị mang tên phản xạ đứng hình của Kakapo! Suốt hàng triệu năm đối đầu với loài đại bàng Haast khổng lồ thời tiền sử vốn săn mồi bằng thị giác trên". Bố cục: Bầu trời thời tiền sử: bóng đen khổng lồ của đại bàng Haast thời tiền sử sải cánh 3 mét trên bầu trời đang lượn vòng săn mồi bằng mắt; phía dưới chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand đứng bất động hòa lẫn hoàn hảo vào thảm thực vật màu xanh rêu.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "không, chiến thuật đứng im bất động giữa thảm rêu xanh đốm vàng từng giúp tổ tiên gã tàng hình hoàn hảo! Kẻ săn mồi từ trên trời nhìn xuống sẽ chỉ thấy một bụi rêu vô hại và bay qua luôn! Nhưng bi". Bố cục: Chiến thuật tàng hình thành công trước đại bàng: Đại bàng bay qua không nhìn thấy gì; chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand hé một bên mắt tinh quái cười thầm.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "kịch ập đến khi người định cư mang theo chuột, mèo hoang và chồn ec-min lên đảo! Những kẻ săn mồi ngoại lai này không dùng mắt để săn chim, mà dùng khứu giác cực kỳ thính nhạy! Và oái oăm". Bố cục: Con thuyền người định cư cập bến: Các loài động vật ngoại lai chuột, mèo và chú chồn ec-min nâu nhọn mũi đang hít hà đánh hơi mùi mật ong rừng tràn lên hòn đảo thiên đường.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thay, Gã béo vô tri quên cách bay lại sở hữu 1 mùi hương cơ thể vô cùng ngọt ngào, thơm phức mùi mật ong rừng quyện với hoa quả chín nồng nàn! Đứng im bất động mà lại tỏa hương ngào ngạt chẳng khác". Bố cục: chú chồn ec-min nâu nhọn mũi đang hít hà đánh hơi mùi mật ong rừng dùng chiếc mũi thính nhạy hít hà đánh hơi; những dải hương thơm màu hồng phấn hình bông hoa bay lơ lửng từ người chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nào gã đang bật đèn pha tín hiệu thông báo: Tôi là một bữa ăn 4 kg béo ngậy đang đợi các bạn tới xơi đây! Bù lại cho cơ chế tự vệ tấu hài đầy rủi ro này, Gã béo vô tri quên cách". Bố cục: Minh họa lọ nước hoa mật ong rừng và quả chín gắn trên lưng chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand; cơ chế tỏa hương ngọt ngào trở thành chiếc bẫy hi sinh bảo vệ tổ.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bay lại sở hữu một chỉ số sinh học đáng kinh ngạc: Tuổi thọ trung bình của Kakapo lên tới 60 đến 90 năm! Đây là một trong những loài chim sống thọ nhất trên toàn bộ hành tinh Trái Đất!". Bố cục: Biểu đồ tuổi thọ sinh học: chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand rùa bò thong thả bên cột mốc sáu mươi đến chín mươi năm; loài chim sống thọ kỷ lục nhờ nhịp sống chậm rãi.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà sinh học giải thích rằng do không tốn năng lượng cho việc bay lượn trên trời, nhịp trao đổi chất của gã chậm rãi tựa như 1 chú rùa cạn, giúp các tế bào cơ thể lão hóa cực kỳ từ tốn!". Bố cục: chú chim bói cá phóng viên đeo kính cận, cổ đeo thẻ nhà báo dã ngoại và tay cầm micro đài truyền hình kiểm tra camera nhiệt, thở phào khi thấy mối nguy hiểm vừa đi qua; chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand bắt đầu nhúc nhích cử động trở lại.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hoàng hôn buông xuống, đồng hồ hiện trường điểm 19:00 tối! Sau một ngày dài ngủ nướng và đứng đơ giả vờ làm bụi rêu, chiếc bụng đói cồn cào đã thúc giục gã béo thức tỉnh hoàn toàn! Lúc". Bố cục: Đồng hồ hiện trường điểm mười chín giờ tối hoàng hôn: Bầu trời nhuộm màu tím than và vàng cam; chiếc bụng đói của chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand sôi réo ùng ục.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "này, camera hồng ngoại của chúng tôi bắt trọn một kỹ năng bất ngờ: Dù không biết bay, nhưng Gã béo vô tri quên cách bay lại là một chuyên gia leo trèo cừ khôi bậc nhất cánh rừng! Gã dùng". Bố cục: Kỹ năng leo trèo bất ngờ: chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand cắm phập chiếc mỏ quặp cứng như móc leo núi vào thân cây, đôi chân cơ bắp bám chắc đu người lên cao.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chiếc mỏ quặp cứng như móc sắt và đôi bàn chân bốn ngón khỏe khoắn để bám chặt vào vỏ cây cổ thụ! Đặc biệt hơn nữa, chiếc mỏ quặp màu xám ngà của gã hoạt động chẳng khác nào 1". Bố cục: chú chim bói cá phóng viên đeo kính cận, cổ đeo thẻ nhà báo dã ngoại và tay cầm micro đài truyền hình lia máy quay theo bước chân thoăn thoắt của chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand đang trèo lên thân cây ngọn cây cổ thụ rimu New Zealand cao vút 20 mét trĩu quả chín mọng vàng ươm cao chót vót.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chiếc chân thứ 3 thần thánh! Khi hai bàn chân bám vào vỏ cây xù xì, gã cắm phập chiếc mỏ cứng vào thân cây như chiếc móc leo núi chuyên nghiệp của vận động viên leo vách đá, đu toàn". Bố cục: Đỉnh ngọn cây rimu cao hai mươi mét: chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand ngồi vắt vẻo trên cành cao, nhai nhồm nhoàm từng chùm quả rimu chín mọng ngọt ngào.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bộ khối thân 4 kg lên cành cao một cách vô cùng điệu nghệ! Từng bước túc tắc chậm rãi nhưng cực kỳ chắc chắn, gã trèo thoăn thoắt lên thân cây rimu cao vút tới 20 mét! Mục tiêu của". Bố cục: Khuôn mặt thỏa mãn tột cùng của chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand khi được no nê quả chín; vệt nước quả vàng ươm dính quanh mép mỏ.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "gã là những chùm quả rimu chín mọng ngọt ngào trên ngọn cây, món ăn khoái khẩu giàu dinh dưỡng chỉ nở rộ vài năm 1 lần! Nhìn gã ngồi vắt vẻo trên cành cao nhai nhồm nhoàm từng chùm quả". Bố cục: chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand đứng trên đầu cành cây nhìn xuống mặt đất hun hút bên dưới, ưỡn ngực xòe cánh tự tin như một chú đại bàng sắp cất cánh.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "quả thật trông vô cùng bình yên và thỏa mãn! Nhưng thưa quý vị, kịch tính hài hước nhất của bản tin hiện trường xảy ra ngay lúc này! Sau khi chén đẫy bụng quả rimu, thay vì tốn công leo". Bố cục: Pha nhảy dù dũng cảm bảo vệ tổ: chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand lao mình vút vào không trung; đôi cánh ngắn tũn xòe ra loạng choạng như chiếc dù rách.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "ngược trở xuống từng bước một, gã béo nhìn xuống mặt đất sâu hun hút và dường như... quên mất bản thân mình hoàn toàn không biết bay! Gã ưỡn ngực, lấy đà, xòe rộng đôi cánh ngắn tũn rồi dũng". Bố cục: Trọng lực kéo khối thân bốn cân rơi tự do vùn vụt; chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand hoảng hốt mở to hai mắt, chiếc mỏ há hốc kêu quàng quạc.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cảm lao mình vút vào không trung như 1 chú đại bàng dũng mãnh! Và điều gì phải đến đã đến: Lực nâng của không khí bằng không, trọng lực kéo khối thân 4 kg rơi tự do không phanh vùn". Bố cục: Cú tiếp đất kinh thiên động địa: chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand đập thẳng bụng và mặt xuống thảm rêu dày đánh BẸP một tiếng; bụi lá và rêu bắn tung tóe.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "vụt xuống dưới! Chiếc cánh chỉ hoạt động như 1 chiếc dù rách lắc lư loạng choạng, và BẸP! Gã đập thẳng bụng và mặt xuống đệm rêu dày cộp dưới gốc cây! Bụi rêu và lá khô bắn tung tóe". Bố cục: chú chim bói cá phóng viên đeo kính cận, cổ đeo thẻ nhà báo dã ngoại và tay cầm micro đài truyền hình ôm miệng nín cười khi thấy chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand lồm cồm bò dậy, lắc lắc đầu cho tỉnh táo với những chú chim quay quanh đầu.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "mù mịt! Máy quay chúng tôi vội lao tới cấp cứu, nhưng gã béo chỉ lồm cồm bò dậy, lắc lắc cái đầu ngơ ngác chớp chớp mắt tự hỏi: Quái lạ, sao hôm nay trời cản gió dữ vậy ta?". Bố cục: chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand phủi phủi lông ngực, ung dung bước tiếp như chưa từng có pha đập mặt thảm họa nào xảy ra.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đồng hồ sinh tồn đếm ngược điểm 23:00 đêm! Toàn bộ khu rừng chìm vào bóng tối đặc quánh, và đây mới chính là thời khắc sân khấu đỉnh cao của Gã béo vô tri quên cách bay! Sau". Bố cục: Đồng hồ hiện trường điểm hai mươi ba giờ đêm: Rừng rậm tối đen như mực; chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand bắt đầu sải bước việt dã mạnh mẽ xuyên qua các lối mòn.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cú tiếp đất đập bụng tấu hài, gã bắt đầu một hành trình thể thao phi thường: Đi bộ việt dã xuyên đêm! Với đôi chân cơ bắp to lớn, gã có thể lầm lũi đi bộ hàng chục". Bố cục: phát thanh viên đài truyền hình cú tuyết đeo tai nghe ngồi trong trường quay tin tức thời sự đặt câu hỏi thắc mắc làm sao các chú vẹt tìm thấy nhau trong màn đêm mịt mù của cánh rừng nguyên sinh.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "km đường rừng, leo qua các sườn đồi dốc đứng để tiến về đấu trường tán tỉnh bạn tình! Ủa phóng viên ơi, trong đêm tối mù mịt thế này thì làm sao vẹt đực tìm được vẹt cái". Bố cục: chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand đứng trên đỉnh đồi lộng gió, dùng móng vuốt cào bới tạo thành một chiếc hố hình lòng chảo sâu mười xăng-ti-mét trên nền đất mềm.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "để hẹn hò ạ? Câu hỏi tuyệt vời từ trường quay! Hãy nhìn vào công trình kiến trúc độc nhất vô nhị mà gã béo vừa tạo ra trên đỉnh đồi: Gã dùng móng vuốt cào bới tạo thành". Bố cục: Sơ đồ âm học phễu loa: Chiếc hố đất hoạt động như bộ khuếch đại sóng âm; chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand đứng giữa hố hít căng lồng ngực phồng to như quả bóng.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "1 chiếc hố hình lòng chảo sâu khoảng mười xăng-ti-mét! Chiếc hố đất này đóng vai trò như 1 chiếc phễu loa bát khuếch đại âm thanh sinh học! Gã bước xuống đáy hố, hít một hơi thật sâu". Bố cục: Đại nhạc hội xuyên đêm: Những đợt sóng âm tần số thấp booming ồm ồm lan tỏa từ chiếc hố, rung chuyển cả màn đêm yên tĩnh.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "làm phồng căng túi khí ở ngực như một quả bóng bay khổng lồ, rồi phát ra những tiếng kêu ồm ồm trầm đục mang tên booming! Âm thanh tần số thấp này dội vào thành hố lòng chảo,". Bố cục: Bản đồ radar âm thanh: Vòng tròn sóng âm lan tỏa bao phủ bán kính năm cây số khắp các thung lũng xung quanh.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "được khuếch đại cực đại và truyền sóng âm xuyên qua màn đêm mù sương, vang xa tới 5 km khắp các thung lũng xung quanh! Gã kiên trì phát loa phóng thanh suốt 8 tiếng đồng hồ mỗi". Bố cục: chú chim bói cá phóng viên đeo kính cận, cổ đeo thẻ nhà báo dã ngoại và tay cầm micro đài truyền hình đeo tai nghe âm thanh chuyên dụng, giơ micro thu lại những tiếng booming kiên trì suốt tám tiếng của chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đêm, liên tục trong 3 đến 4 tháng ròng rã chỉ để hy vọng một nàng vẹt cái nghe thấy và tìm đến! Một nỗ lực tình yêu vĩ đại và nhẫn nại bậc nhất trong thế giới loài chim!". Bố cục: Bóng dáng một nàng vẹt cái e ấp từ xa đang lần theo tiếng gọi tình yêu bước về phía đỉnh đồi trong niềm hy vọng.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đồng hồ lại điểm 6:00 sáng! Ánh nắng bình minh le lói xuyên qua màn sương sớm, và bản tin nhật ký 24 giờ của chúng tôi chính thức khép lại trọn vẹn một vòng quay sinh". Bố cục: Đồng hồ lại điểm sáu giờ sáng hôm sau: Ánh nắng bình minh vàng dịu chiếu qua màn sương sớm; bản tin hai mươi tư giờ khép lại một vòng quay.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tồn! Gã béo vô tri quên cách bay lúc này đã mệt lử sau một đêm gào thét phát loa, lững thững bước về lại chiếc hốc rễ cây quen thuộc, cuộn tròn bộ lông xanh rêu". Bố cục: chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand mệt lử sau đêm dài phát loa, lững thững bước về chiếc hốc rễ cây quen thuộc, cuộn tròn bộ lông xanh rêu đi ngủ nướng.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "lại để chuẩn bị cho một giấc ngủ nướng mới! Một ngày đầy ắp những cú ngã đập bụng, những pha đứng hình ngơ ngác, nhưng ngập tràn vẻ đẹp hồn nhiên của tạo hóa! Hiện nay". Bố cục: Trung tâm bảo tồn New Zealand: Các nhà khoa học nâng niu chăm sóc từng quả trứng và gắn thiết bị bảo vệ cho chú vẹt béo quý giá.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "trên toàn thế giới, quần thể loài vẹt Kakapo chỉ còn vỏn vẹn khoảng 250 cá thể, mỗi chú vẹt đều được các nhà khoa học New Zealand gắn thiết bị theo dõi và chăm sóc từng". Bố cục: Tấm bảng thống kê bảo tồn: Con số hai trăm năm mươi cá thể ít ỏi được khoanh tròn trang trọng như những báu vật của Trái Đất.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "quả trứng như bảo vật quốc gia! Câu chuyện của Kakapo dạy chúng ta 1 bài học sâu sắc: Sự ngây thơ không có lỗi, nhưng khi thế giới xung quanh biến đổi quá nhanh, những tâm hồn". Bố cục: chú chim bói cá phóng viên đeo kính cận, cổ đeo thẻ nhà báo dã ngoại và tay cầm micro đài truyền hình khép sổ tay hiện trường, mỉm cười nhìn chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand đang say ngủ với thông điệp trân trọng sự ngây thơ thuần khiết của thiên nhiên.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thuần khiết nhất lại chính là những sinh linh cần được nâng niu và chở che nhiều nhất! Nếu được gửi một lời nhắn nhủ đến chú vẹt béo Kakapo, bạn sẽ khuyên chú bớt ăn quả". Bố cục: Màn hình tương tác người xem: Khung bình luận mở ra mời khán giả chia sẻ lời nhắn nhủ yêu thương đến chú vẹt béo Kakapo.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "rimu hay tập bay nhảy cẩn thận hơn? Hãy để lại bình luận chia sẻ cảm nghĩ của bạn bên dưới nhé! Còn bây giờ, chiếc đồng hồ 24 giờ đang chuẩn bị đưa chúng ta đến". Bố cục: Hồ sơ mật tập bốn mươi sáu hé lộ: Một chú lợn rừng kỳ lạ Babirusa giữa rừng rậm nhiệt đới Indonesia với cặp răng nanh uốn cong đâm xuyên sống mũi.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "với hồ sơ kỳ dị tiếp theo của tập 46! 1 loài động vật bí ẩn đến từ những cánh rừng nhiệt đới Indonesia hoang dã, sở hữu cặp răng nanh kỳ quái mọc ngược đâm xuyên". Bố cục: Cận cảnh cặp răng nanh nhọn hoắt tự đâm ngược vào trán hộp sọ một cách bí hiểm; dấu hỏi chấm xoay quanh sinh vật hi sinh bảo vệ tổ tiến hóa.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "qua cả sống mũi, uốn cong vòng lại và chực chờ đâm thủng chính hộp sọ của nó! Bạn có đoán được sinh vật mang nghịch lý tiến hóa hi sinh bảo vệ tổ rùng mình này là loài nào không?". Bố cục: Màn hình kết thúc: Dòng chữ HẸN GẶP LẠI Ở TẬP 46 LỢN HƯƠU BABIRUSA lung linh với lời kêu gọi đăng ký kênh theo dõi.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Quên mất mình không biết bay nhưng vẫn leo tót lên ngọn cây cao 20 mét rồi xòe cánh nhảy". Bố cục: Cận cảnh mở đầu: chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác béo múp 4kg leo lên ngọn cây cao hai mươi mét, xòe cánh nhảy ùm xuống rơi tự do đập bụng bẹp dí xuống thảm rêu.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "ùm xuống đập bụng bẹp dí! Đây là Kakapo, loài vẹt nặng nhất thế giới với thể trọng lên tới 4". Bố cục: chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác là loài vẹt nặng nhất thế giới và loài vẹt duy nhất quên mất cách bay; cơ thể tròn ủng như trái bơ khổng lồ.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "kg, và cũng là loài vẹt duy nhất trên Trái Đất hoàn toàn quên mất cách bay! Sống hàng triệu". Bố cục: Khung xương X-quang: Xương ức phẳng lì khiến đôi cánh lông vũ chỉ còn là món đồ trang trí vô dụng.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "năm ở New Zealand không có thú săn mồi, xương ức của gã thoái hóa phẳng lì khiến đôi cánh chỉ". Bố cục: chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác đứng hình phăng phắc như pho tượng giả làm bụi rêu khi gặp nguy hiểm giữa rừng già.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "còn là vật trang trí. Khi gặp nguy hiểm, gã đứng hình phăng phắc giả làm bụi rêu, nhưng cơ thể". Bố cục: Những làn hương mật ong rừng và quả chín ngọt ngào bay ra từ người chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác, vô tình mời gọi kẻ săn mồi tới xơi.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "lại tỏa ra mùi mật ong thơm phức mời gọi kẻ thù! Ban đêm, gã đi bộ hàng chục km,". Bố cục: Ban đêm chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác đi bộ hàng chục cây số, đào chiếc hố lòng chảo khuếch đại tiếng kêu booming vang xa năm cây số tìm bạn tình.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "đào hố lòng chảo khuếch đại tiếng kêu vang xa tới 5 km để gọi bạn tình. Đáng yêu và ngơ". Bố cục: Nàng vẹt cái e ấp bước tới bên miệng hố; nỗ lực tình yêu nhẫn nại suốt hàng tháng trời được đền đáp.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "ngác vô số tội, hiện cả hành tinh chỉ còn vỏn vẹn khoảng 250 cá thể được bảo tồn nghiêm ngặt!". Bố cục: Hiện cả thế giới chỉ còn hai trăm năm mươi cá thể vẹt Kakapo được bảo vệ nghiêm ngặt; mời đăng ký kênh xem trọn bộ tập 45.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/57 của video YouTube về Vẹt Kakapo). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/8 của video YouTube Shorts về Vẹt Kakapo). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand. 
```
</details>

## 7. SEO

- **title:** Quên Mình Không Biết Bay: Chú Vẹt Béo 4kg Leo Cây Nhảy Đập Bụng?! | Vẹt Kakapo | Tập 45
- **hook_paragraph:** Nhật ký 24h đầy tấu hài của Vẹt Kakapo (Strigops habroptilus) — loài vẹt nặng nhất thế giới 4kg quên cách bay, leo ngọn cây 20m nhảy đập bụng, đứng hình giả bụi cây và tiếng gọi bạn tình vang xa 5km!
- **question:** Nếu được nuôi một chú vẹt béo Kakapo, bạn sẽ khuyên chú bớt ăn quả rimu hay mua đệm đỡ cho chú nhảy cây?
- **next_teaser:** Tập 46: Lợn Hươu Babirusa — loài lợn có cặp răng nanh tự đâm thủng hộp sọ chính mình!
- **shorts_title:** Quên mình không biết bay leo cây 20m nhảy đập bụng?! 🦜 #shorts #kakapo
- **shorts_desc:** Khám phá Vẹt Kakapo — loài vẹt nặng 4kg duy nhất trên Trái Đất không biết bay, leo ngọn cây 20m nhảy dù đập bụng và tiếng gọi bạn tình vang xa 5km!
- **bullets:** Loài vẹt nặng nhất thế giới (4kg) và duy nhất không biết bay do xương ức phẳng lì · Cơ chế tự vệ 'đứng hình' giả làm bụi rêu nhưng cơ thể tỏa mùi mật ong ngọt ngào · Leo ngọn cây rimu cao 20m ăn quả rồi xòe cánh nhảy dù đập mặt xuống đất · Đào hố lòng chảo khuếch đại tiếng kêu booming vang xa 5km trong đêm tìm bạn tình
- **tags:** vet kakapo, kakapo parrot, strigops habroptilus, vet khong biet bay, vet beo 4kg, the gioi dong vat, ve chuyen hoang da, dong vat hai huoc, whiteboard animation
- **hashtags:** #VetKakapo #Kakapo #TheGioiDongVat #VeChuyenHoangDa #KhoaHoc

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-45-vet-kakapo
python src/episode/pipeline.py tts    projects/tap-45-vet-kakapo     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-45-vet-kakapo     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-45-vet-kakapo     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-45-vet-kakapo              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-45-vet-kakapo --force
python scripts/beat_sheet.py projects/tap-45-vet-kakapo               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-45-vet-kakapo/audio/shorts.wav projects/tap-45-vet-kakapo/renders/tap-45-vet-kakapo_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-45-vet-kakapo
python src/episode/pipeline.py seo    projects/tap-45-vet-kakapo
python src/episode/episode_doc.py     projects/tap-45-vet-kakapo
```

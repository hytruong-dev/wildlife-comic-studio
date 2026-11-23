# TẬP 34 — QUẠ ĐEN · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-34-qua-den`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-34-qua-den`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F3` · **Persona giọng:** `phien_toa` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Quạ Đen |
| Tiêu đề YouTube | Trí Tuệ Quái Vật: Nhờ Xe Ô Tô Cán Hạt Cứng & Nhớ Mặt Kẻ Thù 5 Năm?! \| Tập 34 |
| Video dài | `renders/tap-34-qua-den_long.mp4` — 10:02.4 (602.4s) |
| Shorts | `renders/tap-34-qua-den_shorts.mp4` — 0:46.7 (46.7s) |
| Thumbnail | `renders/tap-34-qua-den_thumbnail.jpg` |
| Số hình | dài 77 beat / 77 ảnh riêng; Shorts 12 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.11**, Shorts tempo tự tính (≥ 1.12) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/77 của video YouTube về Quạ Đen). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage London thập niên 1920 (Vintage Newspaper Woodcut & Crosshatch Engraving): nét bút sắt crosshatch điêu luyện, độ tương phản đen trắng kịch tính điện ảnh noir, chi tiết kính lúp điều tra, dấu vết hiện trường tinh xảo, vệt sáp niêm phong đỏ, hồ sơ mật giấy kraft hoài cổ điểm xuyết vàng kim sang trọng; NỀN TRẮNG TINH hoàn toàn, không watermark, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat). Nhân vật phụ cố định: thẩm phán cú mèo hoạt hình nghiêm nghị đội tóc giả cổ điển trắng, tay cầm chiếc búa gỗ tòa án; chiếc xe tải lớn màu xanh đang lao qua vạch đường giao thông ngã tư phố; ống nghiệm thủy tinh hẹp chứa nước trong và miếng mồi thịt thơm nổi trên mặt; giáo sư già nghiên cứu sinh vật học đeo chiếc mặt nạ quái vật cau có ngộ nghĩnh. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — VỤ ÁN DÙNG XE Ô TÔ LÀM CÔNG CỤ BÓC HẠT DẺ
*Thẻ chương:* CÔNG TỐ VIÊN CÔNG BỐ HỒ SƠ TỘI PHẠM LÔNG VŨ SỞ HỮU TRÍ NÃO CỦA ĐỨA TRẺ BẢY TUỔI

*Badge:* `KHỞI TỐ VỤ ÁN` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene01_p0.wav` (756 ký tự) · mood `tram_bi_an`

```text
Trật tự! Toàn thể phòng xử án hãy giữ im lặng! Hôm nay, Viện kiểm sát Tự nhiên chính thức mở phiên tòa xét xử một trong những bộ óc mưu mô, quỷ quyệt và sở hữu chỉ số thông minh gây kinh hoàng bậc nhất hành tinh hoang dã. [surprise-oh] Bị cáo đứng trước vành móng ngựa hôm nay không ai khác chính là Quạ Đen, hay còn được giới giang hồ lông vũ gọi bằng mật danh Thiên Tài Cánh Đen! Nhìn vẻ ngoài đen nhánh từ đầu đến chân cùng tiếng kêu quạ quạ chói tai, nhiều người cứ ngỡ đây chỉ là một loài chim chuyên đi nhặt rác hôi thối hoặc mang lại điềm xui xẻo. Nhưng các vị thẩm phán và bồi thẩm đoàn hãy mở tập hồ sơ trinh sát số một ra mà xem! Đây không phải là một con chim bình thường, mà là một bậc thầy thao túng công nghệ và hành vi của xã hội loài người!
```
**Part 1** → `audio/vs/scene01_p1.wav` (103 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Lời khai của nhân chứng: Bị cáo mang quả óc chó vỏ cứng, đặt ngay trước lốp xe tải rồi đứng đợi đèn đỏ!
```
**Part 2** → `audio/vs/scene01_p2.wav` (1003 ký tự) · mood `hao_hung`

```text
[surprise-oh] Quá chính xác thưa nhân chứng! Các bạn hãy tưởng tượng xem: Một quả óc chó rừng dày cộp và cứng như đá cuội, mỏ chim có mổ gãy đôi cũng không tài nào nứt nổi. Thiên Tài Cánh Đen làm gì? Nó không hề tốn công dùng sức đập đá mù quáng. Nó bay vút lên cột đèn tín hiệu giao thông, kiên nhẫn đợi đèn xanh bật lên cho dòng xe cộ lao vun vút qua, rồi thả chính xác quả hạt xuống đúng làn bánh xe tải để lốp xe nghiền nát lớp vỏ cứng hộ mình! Nhưng điều ranh ma chưa dừng lại ở đó. Nó không hề lao xuống nhặt hạt ngay vì biết xe đang chạy sẽ cán chết mình. Nó bình thản đậu trên cành cây cao, quan sát thật kỹ và chờ đúng lúc đèn đỏ bật sáng, toàn bộ dòng xe dừng lại hẳn, mới ung dung sà xuống vạch sang đường dành cho người đi bộ để thưởng thức bữa tiệc béo ngậy! [laughter] Một chiến thuật hoàn hảo, không tốn lấy một giọt mồ hôi mà lại an toàn tuyệt đối. Thưa quý tòa, đây rõ ràng là hành vi lợi dụng phương tiện giao thông hiện đại của loài người mà không chịu nộp một đồng phí cầu đường nào!
```
**Part 3** → `audio/vs/scene01_p3.wav` (494 ký tự) · mood `don_dap`

```text
Các nhà khoa học thần kinh tại Đại học Cambridge đã từng đo đạc tỷ lệ thể tích não bộ so với trọng lượng cơ thể của loài quạ. Kết quả cho thấy tỷ lệ này tương đương hoàn toàn với loài tinh tinh, và mật độ tế bào nơ-ron thần kinh ở vùng não trước của chúng cô đặc đến mức tương đương trí tuệ của một đứa trẻ bảy tuổi! Đừng bao giờ vội coi thường những sinh vật có cánh này, bởi vì ngay sau đây, công tố viên sẽ phơi bày bốn chuỗi bằng chứng không thể chối cãi về siêu trí tuệ đáng sợ của bị cáo!
```

### scene02 — THÍ NGHIỆM AESOP DÂNG NƯỚC VÀ KHẢ NĂNG TÍNH TOÁN THỂ TÍCH
*Thẻ chương:* QUẠ ĐEN THỰC HÀNH VẬT LÝ NỔI: THẢ SỎI CHÌM DÂNG MỰC NƯỚC ĐỂ LẤY MỒI TRONG ỐNG NGHIỆM

*Badge:* `BẰNG CHỨNG #1` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene02_p0.wav` (566 ký tự) · mood `tram_bi_an`

```text
Thưa hội đồng xét xử, chúng ta đều từng được nghe câu chuyện ngụ ngôn Aesop thời thơ ấu về chú quạ khát nước thông minh biết gắp từng viên sỏi thả vào bình để mực nước dâng lên miệng. Suốt hàng thế kỷ, con người chúng ta chỉ coi đó là một câu chuyện cổ tích mang tính phóng đại nhằm răn dạy trẻ nhỏ. Nhưng vào Năm hai ngàn không trăm mười bốn, một nhóm các nhà sinh vật học hành vi quốc tế đã quyết định đưa Thiên Tài Cánh Đen vào phòng thí nghiệm với một bài kiểm tra vật lý thủy động học cực kỳ hóc búa để xem truyền thuyết cổ tích có thật hay không! [surprise-oh]
```
**Part 1** → `audio/vs/scene02_p1.wav` (117 ký tự) · 🎭 cameo `tham_phan`

```text
Báo cáo giám định: Chúng tôi thả miếng thịt trong ống nghiệm sâu mười lăm centimet, mỏ quạ không tài nào thò tới đáy!
```
**Part 2** → `audio/vs/scene02_p2.wav` (915 ký tự) · mood `hao_hung`

```text
[surprise-oh] Và chuyện gì đã diễn ra thưa quý tòa? Các nhà khoa học bày sẵn bên cạnh hai đống vật thể: một đống sỏi đá đặc nặng trĩu chìm nghỉm trong nước, và một đống xốp nhẹ nổi lơ lửng trên mặt nước. Một đứa trẻ dưới năm tuổi nếu không được người lớn chỉ dẫn từ trước rất có thể sẽ nhặt bừa bãi cả xốp lẫn sỏi ném vào ống nghiệm. Nhưng Thiên Tài Cánh Đen thì không! Nó nghiêng đầu quan sát cấu trúc ống trong đúng mười giây, rồi dùng chiếc mỏ sắc nhọn nhặt từng viên sỏi đặc thả tõm vào ống nghiệm. Nó hoàn toàn phớt lờ những miếng xốp nổi vô dụng vì hiểu rõ rằng xốp nhẹ không thể chiếm chỗ để làm thể tích nước dâng lên! [laughter] Từng viên sỏi nặng rơi xuống đáy, mực nước dâng cao dần từng milimét, và chỉ sau sáu lượt thả sỏi chuẩn xác, miếng thịt thơm lừng đã trôi lên tận miệng ống. Bị cáo thong thả gắp lấy miếng mồi ngon lành trước ánh mắt kinh ngạc tột độ của toàn bộ giáo sư tiến sĩ trong phòng lab!
```
**Part 3** → `audio/vs/scene02_p3.wav` (625 ký tự) · mood `don_dap`

```text
Chưa dừng lại ở đó, các nhà nghiên cứu tiếp tục nâng độ khó lên cấp độ tiến sĩ: Họ chuẩn bị đồng thời hai ống nghiệm, một ống chứa nước trong suốt và một ống chứa đầy cát đặc quánh. Thiên Tài Cánh Đen chỉ thả sỏi vào chiếc ống có nước, tuyệt đối không phí một chút sức lực nào để ném sỏi vào ống cát vì nó hiểu rõ cát không có tính chất chuyển động dâng lên như chất lỏng! Thưa tòa, đây chính là nhận thức trực quan phi thường về thể tích và khối lượng riêng của vật chất. Một giống loài chưa từng học qua một tiết vật lý đại cương nào lại có thể vận dụng nguyên lý Archimedes một cách nhuần nhuyễn như một bản năng tự nhiên!
```

### scene03 — ĐỌC VỊ TÂM LÝ ĐỒNG LOẠI VÀ MÀN KỊCH CHÔN MỒI GIẢ MẠO
*Thẻ chương:* CÚ LỪA KINH ĐIỂN: GIẢ VỜ CHÔN THỨC ĂN DƯỚI ĐẤT RỒI MANG ĐI CHỖ KHÁC PHÒNG BỊ KẺ CƯỚP

*Badge:* `BẰNG CHỨNG #2` · *mood mặc định:* `nghiem_trang_gia`

**Part 0** → `audio/vs/scene03_p0.wav` (626 ký tự) · mood `tram_bi_an`

```text
Nếu việc thả sỏi dâng nước mới chỉ chứng minh bị cáo am hiểu sâu sắc môn vật lý cơ bản, thì chuỗi chứng cứ số hai này sẽ chứng minh Thiên Tài Cánh Đen còn là một bậc thầy lão luyện về tâm lý học hành vi và điều tra tội phạm! Trong giới động vật học hiện đại, có một khái niệm nhận thức cực kỳ cao cấp gọi là Thuyết tâm trí. Đó là khả năng nhận biết rằng kẻ khác cũng có suy nghĩ, góc nhìn riêng và ý đồ cướp đoạt, từ đó dự đoán trước hành vi của đối phương để tung đòn lừa gạt hoặc thiết lập phòng thủ. Trên cõi đời này, ngoài con người và loài tinh tinh, hầu như chưa có loài chim nào chạm tới đẳng cấp tư duy trừu tượng này!
```
**Part 1** → `audio/vs/scene03_p1.wav` (104 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Lời tố cáo: Bị cáo rất hay diễn trò đào bới giả vờ cất giấu kho báu nhằm lừa gạt sự chú ý của chúng tôi!
```
**Part 2** → `audio/vs/scene03_p2.wav` (855 ký tự) · mood `hao_hung`

```text
[surprise-oh] Lời tố cáo hoàn toàn chính xác đến từng chi tiết! Khi một con quạ kiếm được một miếng mồi béo bở, nó sẽ lập tức đảo mắt lia lịa quan sát xung quanh xem có kẻ nào đang rình mò ăn trộm hay không. Nếu phát hiện có một con quạ khác đang lén lút dòm ngó từ cành cây đối diện, nó sẽ làm gì? Nó không hề bỏ chạy hoảng loạn. Nó giả vờ ung dung đáp xuống một bụi cỏ rậm rạp, dùng mỏ cặm cụi đào một cái hố thật sâu, làm động tác nhét miếng mồi vào rồi phủ lá cây khô lên ngụy trang thật cẩn thận. Nhưng thực chất, miếng mồi ngon lành vẫn được giấu kín mít sâu dưới cuống họng của nó! [laughter] Đợi đến khi kẻ rình mò hăm hở lao xuống đào bới điên cuồng cái hố rỗng tuếch kia trong sự thất vọng tột cùng, thì Thiên Tài Cánh Đen đã sải cánh bay tít sang một khu rừng hoang vắng khác, nơi không có lấy một ánh mắt dòm ngó, để chôn giấu kho báu thực sự!
```
**Part 3** → `audio/vs/scene03_p3.wav` (378 ký tự) · mood `don_dap`

```text
Điều này chứng minh điều gì thưa quý tòa? Bị cáo hiểu rõ ràng như ban ngày rằng kẻ kia đang có dã tâm cướp mồi của mình, và bị cáo biết cách tạo ra một thông tin giả mạo đánh lừa thị giác để điều khiển hành vi của đối thủ theo ý mình. Chỉ có những bộ não sở hữu chỉ số mưu mô cực kỳ tinh quái mới có thể dàn dựng một kịch bản tình báo hai mang xuất sắc và lạnh lùng đến như vậy!
```

### scene04 — CHẾ TẠO CÔNG CỤ LIÊN HOÀN VÀ UỐN CONG DÂY THÉP LÀM LƯỠI CÂU
*Thẻ chương:* QUẠ NEW CALEDONIA UỐN CONG DÂY THÉP THÀNH MÓC CÂU LẤY THỨC ĂN NGOÀI TẦM VỚI

*Badge:* `BẰNG CHỨNG #3` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene04_p0.wav` (534 ký tự) · mood `tram_bi_an`

```text
Thưa quý tòa, trong thế giới động vật, nhiều loài như rái cá biển biết dùng đá đập vỡ vỏ ốc, hay chim sẻ biết dùng cọng cỏ khều sâu trong kẽ nứt. Nhưng sử dụng một công cụ có sẵn trong tự nhiên là một chuyện, còn biết tự tay chế tạo và biến đổi hình dạng của một vật thể hoàn toàn mới theo ý đồ riêng lại là một nấc thang tiến hóa trí tuệ vượt bậc! Vào Năm hai ngàn không trăm lẻ hai, một cá thể quạ New Caledonia mang tên Betty tại phòng thí nghiệm Đại học Oxford đã tạo nên một cơn địa chấn chấn động toàn bộ giới khoa học thế giới!
```
**Part 1** → `audio/vs/scene04_p1.wav` (112 ký tự) · 🎭 cameo `tham_phan`

```text
Báo cáo thực nghiệm: Betty được đưa cho sợi dây kẽm thẳng và chiếc xô thịt nhỏ ở đáy ống hẹp không thể móc được!
```
**Part 2** → `audio/vs/scene04_p2.wav` (722 ký tự) · mood `hao_hung`

```text
[surprise-oh] Các bạn có hình dung được chú quạ này đã làm gì không? Betty không hề cắn xé hay vẫy cánh bất lực. Nó bình tĩnh dùng móng chân kẹp chặt một đầu sợi dây kẽm xuống sàn, dùng chiếc mỏ cứng cáp ngậm lấy đầu kia và kéo gập một góc chín mươi độ, tạo thành một chiếc móc câu cong vút hình chữ J vô cùng hoàn hảo! Sau đó, nó ngậm chiếc móc câu tự chế này, thọc thẳng xuống khe hẹp, móc chuẩn xác vào quai xô và nhấc bổng miếng thịt ngon lành lên miệng trước sự sững sờ kinh ngạc của các nhà nghiên cứu! [laughter] Đây là lần đầu tiên trong lịch sử nhân loại, một loài sinh vật không thuộc bộ linh trưởng lại có khả năng tự biến đổi một vật liệu kim loại nhân tạo thành công cụ chuyên dụng chính xác đến từng milimét!
```
**Part 3** → `audio/vs/scene04_p3.wav` (423 ký tự) · mood `don_dap`

```text
Và chưa dừng lại ở đó đâu thưa hội đồng, loài quạ còn giải được câu đố công cụ tám bước liên hoàn trong các bài kiểm tra logic phức tạp: Dùng chiếc que ngắn gắp chiếc que vừa, dùng chiếc que vừa lấy chiếc que dài nhất, và cuối cùng dùng chiếc que dài nhất để chọc thủng ổ khóa lấy miếng thức ăn béo ngậy. Chúng có khả năng lập kế hoạch tương lai tuần tự trong não bộ trước khi thực hiện từng hành động cụ thể ngoài thực tế!
```

### scene05 — NHẬN DIỆN KHUÔN MẶT CON NGƯỜI VÀ BẢN ÁN TRẢ THÙ KÉO DÀI 5 NĂM
*Thẻ chương:* BỘ NHỚ KHỦNG KHIẾP: NHẬN DIỆN MẶT KẺ THÙ VÀ TRUYỀN NỖI HẬN THÙ CHO CẢ ĐÀN QUA NHIỀU NĂM

*Badge:* `BẰNG CHỨNG #4` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene05_p0.wav` (410 ký tự) · mood `tram_bi_an`

```text
Và đây chính là bản cáo trạng rùng rợn và gây sốc nhất trong toàn bộ phiên tòa hôm nay: Khả năng ghi nhớ khuôn mặt con người và lòng thù hận truyền kiếp của Thiên Tài Cánh Đen! Nếu bạn từng trót dại ném một hòn đá, phá tổ hay xua đuổi một con quạ trên đường phố, lời khuyên chân thành và cấp thiết nhất của công tố viên là hãy lập tức chuyển nhà sang một thành phố khác sinh sống ngay đi! [dissatisfaction-hnn]
```
**Part 1** → `audio/vs/scene05_p1.wav` (105 ký tự) · 🎭 cameo `ong_gia_ke`

```text
Lời khai của giáo sư: Tôi từng đeo mặt nạ quái vật để gắn thẻ nhận dạng vài con quạ trong trường đại học!
```
**Part 2** → `audio/vs/scene05_p2.wav` (866 ký tự) · mood `hao_hung`

```text
[surprise-oh] Và hậu quả sau đó thật là một cơn ác mộng kinh hoàng kéo dài suốt nhiều năm! Dù giáo sư có thay đổi toàn bộ quần áo, thay đổi dáng đi hay thậm chí đi lẫn giữa hàng ngàn sinh viên tấp nập, chỉ cần ông đeo chiếc mặt nạ đó bước ra sân trường, toàn bộ bầy quạ xung quanh lập tức gầm rú tiếng kêu báo động đặc biệt, đồng loạt lao bổ xuống mổ tới tấp vào đầu và phóng uế liên hồi lên người ông! Điều đáng sợ đến lạnh gáy nhất là: suốt năm năm sau đó, ngay cả những con quạ non mới sinh ra, chưa từng bị bắt giữ hay nhìn thấy mặt nạ bao giờ, cũng lập tức tham gia vào cuộc tập kích báo thù điên cuồng này! [laughter] Bằng một hệ thống ngôn ngữ tiếng kêu phức tạp chưa được con người giải mã hoàn toàn, quạ bố mẹ đã miêu tả chi tiết từng đặc điểm khuôn mặt của kẻ thù cho quạ con và cả những bầy quạ láng giềng xung quanh biết để cùng nhau đi trừng phạt kẻ ác!
```
**Part 3** → `audio/vs/scene05_p3.wav` (326 ký tự) · mood `don_dap`

```text
Ngược lại, nếu một người đàn ông đeo mặt nạ Tổng thống Dick Cheney luôn mang đồ ăn ngon đến cho chúng, bầy quạ sẽ tỏ ra vô cùng thân thiện, sà xuống quấn quýt và bay lượn chào đón nồng nhiệt. Loài quạ không chỉ nhớ mặt bạn đến từng chi tiết nhỏ, mà chúng còn nhớ bạn đã từng đối xử tử tế hay độc ác với chúng suốt nửa thập kỷ!
```

### scene06 — PHÁN QUYẾT CỦA TÒA ÁN TỰ NHIÊN & CÂU ĐỐ LINH THÚ TẬP 35
*Thẻ chương:* BẢN ÁN TRỌN ĐỜI: TRAO HUY CHƯƠNG TRÍ TUỆ ĐỈNH CAO CHO THIÊN TÀI LÔNG VŨ CỦA BẦU TRỜI

*Badge:* `PHÁN QUYẾT` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (386 ký tự) · mood `tram_bi_an`

```text
Thưa quý tòa, thưa các vị bồi thẩm đoàn và toàn thể các bạn khán giả thân mến! Sau khi xem xét toàn diện chuỗi bằng chứng từ việc mượn lốp xe ô tô bóc hạt dẻ, thả sỏi dâng nước, đóng kịch giấu mồi cho đến tự chế tạo móc câu và nhớ mặt kẻ thù suốt năm năm, Viện kiểm sát nhận thấy: Hành vi của bị cáo không phải là tội ác, mà là đỉnh cao của sự thích nghi và trí tuệ sinh tồn phi thường!
```
**Part 1** → `audio/vs/scene06_p1.wav` (105 ký tự) · 🎭 cameo `tham_phan`

```text
Tuyên án: Bị cáo Quạ Đen được tuyên trắng án và được trao danh hiệu Kẻ Thông Minh Nhất Bầu Trời Tự Nhiên!
```
**Part 2** → `audio/vs/scene06_p2.wav` (547 ký tự) · mood `am_ap`

```text
[laughter] Một tràng pháo tay nồng nhiệt cho Thiên Tài Cánh Đen! Chúng nhắc nhở loài người chúng ta một bài học sâu sắc rằng: Trí tuệ và khả năng tư duy không phải là đặc quyền duy nhất của bộ linh trưởng, và sự sống hoang dã luôn ẩn chứa những kỳ quan não bộ vượt xa trí tưởng tượng tầm thường của con người. Lần tới nếu bạn vô tình bắt gặp một chú quạ đen bên đường, hãy cúi đầu chào nó thật lịch sự và ném cho nó một vài hạt dẻ thơm ngon nhé, vì rất có thể đôi mắt tinh anh đó đang âm thầm ghi nhớ khuôn mặt của bạn suốt năm năm đấy! [laughter]
```
**Part 3** → `audio/vs/scene06_p3.wav` (550 ký tự) · mood `hao_hung`

```text
Còn bây giờ, giữa tài mượn lốp xe ô tô bóc vỏ hạt và khả năng nhớ mặt kẻ thù suốt năm năm truyền lại cho đời con, bạn thấy siêu trí tuệ nào của Quạ Đen đáng kinh ngạc và gây sốc hơn? Hãy để lại ý kiến bình luận của bạn ngay bên dưới nhé! Và các bạn hãy chuẩn bị tinh thần cho Tập ba mươi lăm: Chúng ta sẽ tạm rời bầu trời để lặn xuống đáy đại dương sâu thẳm, đối đầu với một gia tộc Mafia khét tiếng nhất biển cả, kẻ có biệt danh Sát Thủ Biển Đen sở hữu tuyệt chiêu tạo sóng hất văng hải cẩu và dám phẫu thuật hạ gục cả Cá Mập Trắng! Hãy đón xem nhé!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Đừng bao giờ đắc tội với một con Quạ Đen nếu bạn không muốn bị cả dòng họ nhà nó truy sát suốt năm năm trời! [dissatisfaction-hnn] Quạ Đen sở hữu bộ não có mật độ nơ-ron dày đặc ngang loài tinh tinh, đạt trí thông minh tương đương một đứa trẻ bảy tuổi. Ở Nhật Bản, khi gặp quả óc chó vỏ quá cứng, quạ thản nhiên thả hạt trước bánh xe tải lúc đèn xanh để xe nghiền nát hộ, rồi ung dung đợi đèn đỏ xe dừng hẳn mới sà xuống vạch đi bộ nhặt ăn ngon lành! Trong phòng thí nghiệm, chúng biết thả từng viên sỏi đặc vào ống nghiệm để dâng mực nước lấy thức ăn y hệt ngụ ngôn Aesop. Đặc biệt, nghiên cứu tại Đại học Washington chứng minh: Quạ có thể ghi nhớ chính xác từng đường nét trên khuôn mặt kẻ thù suốt năm năm, rồi tả lại mặt kẻ đó cho cả bầy đàn cùng quạ con mới sinh để cùng nhau kéo đến trả thù! [laughter] Hãy đối xử thật tử tế với những thiên tài lông vũ này nhé!
```

**Whisper prompt:** `Quạ Đen, Thiên Tài Cánh Đen, New Caledonia, Aesop, Marzluff, Corvus, Seattle, Washington, IQ trẻ em 7 tuổi`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| Năm hai ngàn không trăm mười bốn | Năm 2014 |
| Năm hai ngàn không trăm lẻ hai | Năm 2002 |
| Tập ba mươi lăm | Tập 35 |
| bảy tuổi | 7 tuổi |
| năm năm | 5 năm |
| mười giây | 10 giây |
| mười lăm centimet | 15cm |
| sáu lượt | 6 lượt |
| tám bước | 8 bước |
| chín mươi độ | 90° |
| đèn đỏ | Đèn đỏ |
| đèn xanh | Đèn xanh |
| Archimedes | Archimedes |
| Dick Cheney | Dick Cheney |
| John Marzluff | John Marzluff |
| New Caledonia | New Caledonia |
| Cambridge | Cambridge |
| Oxford | Oxford |
| Shibuya | Shibuya |
| Tokyo | Tokyo |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · VỤ ÁN DÙNG XE Ô TÔ LÀM CÔNG CỤ BÓC HẠT DẺ · 117.6s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:04.5 (4.5s) | L01 | Trật tự! Toàn thể phòng xử án hãy giữ im lặng! Hôm nay, Viện kiểm sát Tự |  | Toàn cảnh phòng xử án Tự nhiên cổ điển trang nghiêm: thẩm phán cú mèo hoạt hình nghiêm nghị đội tóc giả cổ điển trắng, tay cầm chiếc búa gỗ tòa án ngồi trên bục cao gõ mạnh chiếc búa gỗ xét xử. KHÔNG có chú Quạ Đen trong cảnh này. |
| b02 | 00:04.5–00:18.4 (13.9s) | L02 | nhiên chính thức mở phiên tòa xét xử một trong những bộ óc mưu mô, quỷ quyệt và sở hữu chỉ số thông minh gây kinh hoàng bậc nhất hành tinh hoang dã. Bị cáo đứng trước vành móng ngựa hôm nay không ai khác chính là Quạ Đen, hay còn được giới giang hồ lông vũ gọi bằng mật danh Thiên Tài Cánh Đen! |  | Khung cảnh vành móng ngựa phòng xử án: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) đứng khoanh cánh ngạo nghễ, nhếch mép cười khẩy trước ánh mắt dò xét của bồi thẩm đoàn. |
| b03 | 00:18.4–00:31.3 (12.9s) | L03 | Nhìn vẻ ngoài đen nhánh từ đầu đến chân cùng tiếng kêu quạ quạ chói tai, nhiều người cứ ngỡ đây chỉ là một loài chim chuyên đi nhặt rác hôi thối hoặc mang lại điềm xui xẻo. Nhưng các vị thẩm phán và bồi thẩm đoàn hãy mở tập hồ sơ trinh sát số một ra mà xem! |  | Hình ảnh so sánh đối lập: Bên trái là một chú quạ đen bình thường nhặt rác trong thùng rác, bên phải là sơ đồ não bộ phát sáng rực rỡ của chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat). |
| b04 | 00:31.3–00:36.8 (5.5s) | L04 | Đây không phải là một con chim bình thường, mà là một bậc thầy thao túng công nghệ và hành vi của xã hội loài người! |  | Bảng hồ sơ mật thám tử dán ghim giấy kraft: Tấm ảnh chụp lén chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) đang đứng trên cột đèn giao thông quan sát xã hội loài người. KHÔNG có chú Quạ Đ |
| b05 | 00:36.8–00:40.1 (3.3s) | L05 | Lời khai của nhân chứng: Bị cáo mang quả óc chó vỏ |  | Hiện trường ngã tư đường phố Tokyo đông đúc: Một chú chim bồ câu ngơ ngác giơ cánh khai báo trước tòa, phía sau là dòng xe cộ tấp nập. KHÔNG có chú Quạ Đen trong cảnh này. |
| b06 | 00:40.1–00:45.9 (5.8s) | L06 | cứng, đặt ngay trước lốp xe tải rồi đứng đợi Đèn đỏ! Quá chính xác thưa nhân chứng! Các bạn hãy tưởng tượng |  | Cận cảnh góc thấp mặt đường: Quả óc chó rừng vỏ cứng như đá cuội đặt ngay trước bánh lốp khổng lồ của chiếc xe tải lớn màu xanh đang lao qua vạch đường giao thông ngã tư phố. KHÔNG có chú Quạ Đen trong cảnh này. |
| b07 | 00:45.9–00:55.7 (9.8s) | L07 | xem: Một quả óc chó rừng dày cộp và cứng như đá cuội, mỏ chim có mổ gãy đôi cũng không tài nào nứt nổi. Thiên Tài Cánh Đen làm gì? Nó không hề tốn công dùng sức đập đá mù quáng. |  | chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) đậu trên biển báo giao thông, mỏ ngậm quả óc chó to tướng, nghiêng đầu quan sát dòng xe đang chạy với ánh mắt đầy mưu tính. |
| b08 | 00:55.7–01:03.8 (8.1s) | L08 | Nó bay vút lên cột đèn tín hiệu giao thông, kiên nhẫn đợi Đèn xanh bật lên cho dòng xe cộ lao vun vút qua, rồi thả chính xác quả hạt xuống đúng làn bánh xe tải | **ĐÈN XANH** · thả hạt xuống · R/280 · [0.65, 0.42] | Đèn tín hiệu giao thông ngã tư chuyển sang Đèn xanh: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) thả quả óc chó rơi chuẩn xác xuống đúng làn bánh xe tải đang lăn bánh. |
| b09 | 01:03.8–01:11.5 (7.7s) | L09 | để lốp xe nghiền nát lớp vỏ cứng hộ mình! Nhưng điều ranh ma chưa dừng lại ở đó. Nó không hề lao xuống nhặt hạt ngay vì biết xe đang chạy sẽ cán chết mình. |  | Hiệu ứng va chạm mạnh mẽ: Bánh xe tải nặng nề cán qua làm vỏ quả óc chó nứt toác thành nhiều mảnh vỡ, để lộ phần nhân béo ngậy bên trong. KHÔNG có chú Quạ Đen trong cảnh này. |
| b10 | 01:11.5–01:14.9 (3.5s) | L10 | Nó bình thản đậu trên cành cây cao, quan sát thật kỹ và chờ đúng |  | chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) kiên nhẫn đậu trên cành cây ven đường, bình thản nhìn đồng hồ đeo tay đếm ngược chờ đợi thời cơ chín muồi. |
| b11 | 01:14.9–01:18.0 (3.1s) | L11 | lúc Đèn đỏ bật sáng, toàn bộ dòng xe dừng lại hẳn, | **ĐÈN ĐỎ** · xe dừng hẳn · L/280 · [0.35, 0.42] | Đèn tín hiệu chuyển sang Đèn đỏ rực: Toàn bộ dòng xe dừng bánh thẳng hàng trước vạch sơn trắng. KHÔNG có chú Quạ Đen trong cảnh này. |
| b12 | 01:18.0–01:23.0 (5.0s) | L12 | mới ung dung sà xuống vạch sang đường dành cho người đi bộ để thưởng thức bữa tiệc béo ngậy! |  | chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) thong thả sải cánh đáp xuống vạch kẻ sang đường cho người đi bộ, khoan thai gắp từng miếng nhân óc chó thơm bùi ăn ngon lành. |
| b13 | 01:23.0–01:34.7 (11.7s) | L13 | Một chiến thuật hoàn hảo, không tốn lấy một giọt mồ hôi mà lại an toàn tuyệt đối. Thưa quý tòa, đây rõ ràng là hành vi lợi dụng phương tiện giao thông hiện đại của loài người mà không chịu nộp một đồng phí cầu đường nào! |  | chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) vừa nhai hạt dẻ thơm ngon vừa nháy mắt cười hóm hỉnh với bác tài xế xe tải đang nhìn qua kính chắn gió. |
| b14 | 01:34.7–01:43.8 (9.1s) | L14 | Các nhà khoa học thần kinh tại Đại học Cambridge đã từng đo đạc tỷ lệ thể tích não bộ so với trọng lượng cơ thể của loài quạ. Kết quả cho thấy tỷ lệ này tương đương hoàn toàn với loài tinh tinh, và |  | Sơ đồ giải phẫu thần kinh so sánh kích thước não bộ: Não của chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) và não của tinh tinh đặt cạnh nhau với tỷ lệ trọng lượng cơ thể cân bằng tuyệt đ |
| b15 | 01:43.8–01:53.9 (10.1s) | L15 | mật độ tế bào nơ-ron thần kinh ở vùng não trước của chúng cô đặc đến mức tương đương trí tuệ của một đứa trẻ 7 tuổi! Đừng bao giờ vội coi thường những sinh vật có cánh này, bởi vì ngay sau đây, công tố viên sẽ phơi | **IQ 7 TUỔI** · ngang trẻ em · R/320 · [0.68, 0.5] | Kính hiển vi phóng to cấu trúc tế bào thần kinh vùng não trước của chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat): Hàng triệu nơ-ron liên kết phát sáng như một mạng lưới internet siêu tốc. |
| b16 | 01:53.9–01:57.6 (3.7s) | L16 | bày bốn chuỗi bằng chứng không thể chối cãi về siêu trí tuệ đáng sợ của bị cáo! |  | Tập hồ sơ án mạng mở ra: Bốn con dấu đỏ đánh số 1, 2, 3, 4 đóng lên các trang tài liệu điều tra giật gân. KHÔNG có chú Quạ Đen trong cảnh này. |

### scene02 · THÍ NGHIỆM AESOP DÂNG NƯỚC VÀ KHẢ NĂNG TÍNH TOÁN THỂ TÍCH · 111.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.1 (9.1s) | L17 | Thưa hội đồng xét xử, chúng ta đều từng được nghe câu chuyện ngụ ngôn Aesop thời thơ ấu về chú quạ khát nước thông minh biết gắp từng viên sỏi thả vào bình để mực nước dâng lên miệng. |  | Trang sách tranh ngụ ngôn cổ tích Aesop mở ra với hình minh họa chú quạ cổ điển đứng cạnh chiếc bình gốm khát nước. KHÔNG có chú Quạ Đen trong cảnh này. |
| b02 | 00:09.1–00:15.7 (6.5s) | L18 | Suốt hàng thế kỷ, con người chúng ta chỉ coi đó là một câu chuyện cổ tích mang tính phóng đại nhằm răn dạy trẻ nhỏ. |  | Một nhà bác học cổ xưa ngồi dưới ngọn đèn dầu đang vẽ lại sơ đồ chiếc bình Aesop vào cuốn da cừu ố vàng. KHÔNG có chú Quạ Đen trong cảnh này. |
| b03 | 00:15.7–00:27.7 (12.0s) | L19 | Nhưng vào Năm 2014, một nhóm các nhà sinh vật học hành vi quốc tế đã quyết định đưa Thiên Tài Cánh Đen vào phòng thí nghiệm với một bài kiểm tra vật lý thủy động học cực kỳ hóc búa để xem truyền thuyết cổ tích có thật hay không! | **NĂM 2014** · thí nghiệm aesop · L/300 · [0.3, 0.45] | Phòng thí nghiệm vật lý hiện đại: Các nhà khoa học mang áo blouse trắng chuẩn bị dàn ống nghiệm thí nghiệm thủy động học cho chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat). |
| b04 | 00:27.7–00:37.1 (9.4s) | L20 | Báo cáo giám định: Chúng tôi thả miếng thịt trong ống nghiệm sâu 15cm, mỏ quạ không tài nào thò tới đáy! Và chuyện gì đã diễn ra thưa quý tòa? | **15CM** · độ sâu ống · R/320 · [0.65, 0.52] | Cận cảnh ống nghiệm thủy tinh cao mười lăm centimet chứa nước: Miếng thịt thơm phức nổi lơ lửng ở giữa, mỏ quạ thò vào bị kẹt ở miệng ống. |
| b05 | 00:37.1–00:45.3 (8.2s) | L21 | Các nhà khoa học bày sẵn bên cạnh hai đống vật thể: một đống sỏi đá đặc nặng trĩu chìm nghỉm trong nước, và một đống xốp nhẹ nổi lơ lửng trên mặt nước. |  | Hai khay vật liệu đặt cạnh ống nghiệm: Bên trái là khay sỏi đá nặng trĩu màu xám, bên phải là khay xốp nhẹ bồng bềnh màu trắng. KHÔNG có chú Quạ Đen trong cảnh này. |
| b06 | 00:45.3–00:54.0 (8.6s) | L22 | Một đứa trẻ dưới năm tuổi nếu không được người lớn chỉ dẫn từ trước rất có thể sẽ nhặt bừa bãi cả xốp lẫn sỏi ném vào ống nghiệm. Nhưng Thiên Tài Cánh Đen thì không! |  | Hình ảnh so sánh hài hước: Một em bé hoạt hình đang lúng túng ném lung tung các khối xốp vào nước làm nước bắn tung tóe. KHÔNG có chú Quạ Đen trong cảnh này. |
| b07 | 00:54.0–00:57.1 (3.1s) | L23 | Nó nghiêng đầu quan sát cấu trúc ống trong đúng 10 giây, | **10 GIÂY** · thời gian tính toán · L/320 · [0.38, 0.5] | chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) nghiêng đầu góc bốn mươi lăm độ, dùng kính monocle soi xét trọng lượng từng viên sỏi đá trên bàn trong đúng mười giây. |
| b08 | 00:57.1–01:00.0 (3.0s) | L24 | rồi dùng chiếc mỏ sắc nhọn nhặt từng viên sỏi đặc thả tõm vào ống |  | chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) cắp lấy một viên sỏi đá nặng đặc, cẩn thận thả rơi thẳng đứng xuống đáy ống nghiệm thủy tinh. |
| b09 | 01:00.0–01:07.5 (7.4s) | L25 | nghiệm. Nó hoàn toàn phớt lờ những miếng xốp nổi vô dụng vì hiểu rõ rằng xốp nhẹ không thể chiếm chỗ để làm thể tích nước dâng lên! |  | chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) dùng chân gạt phăng đống mẩu xốp nhẹ sang một bên với vẻ mặt coi thường, hoàn toàn không chạm vào chúng. |
| b10 | 01:07.5–01:12.2 (4.7s) | L26 | Từng viên sỏi nặng rơi xuống đáy, mực nước dâng cao dần từng milimét, và chỉ |  | Mặt cắt ống nghiệm: Dưới đáy ống nghiệm là lớp sỏi đá dâng cao, đẩy cột nước dâng lên từng milimét mang theo miếng thịt mồi. |
| b11 | 01:12.2–01:24.0 (11.8s) | L27 | sau 6 lượt thả sỏi chuẩn xác, miếng thịt thơm lừng đã trôi lên tận miệng ống. Bị cáo thong thả gắp lấy miếng mồi ngon lành trước ánh mắt kinh ngạc tột độ của toàn bộ giáo sư tiến sĩ trong phòng lab! Chưa dừng lại ở đó, các nhà nghiên | **6 LƯỢT** · thả sỏi chuẩn xác · R/320 · [0.72, 0.45] | Miếng thịt trôi lên tới sát miệng ống nghiệm: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) ung dung dùng mỏ ngoạm lấy miếng mồi ngon lành trong tiếng vỗ tay tán thưởng. |
| b12 | 01:24.0–01:31.4 (7.4s) | L28 | cứu tiếp tục nâng độ khó lên cấp độ tiến sĩ: Họ chuẩn bị đồng thời hai ống nghiệm, một ống chứa nước trong suốt và một ống chứa đầy cát đặc quánh. Thiên Tài |  | Bài kiểm tra nâng cao: Hai chiếc ống nghiệm đặt song song, một ống chứa nước trong veo, chiếc ống còn lại chứa đầy cát vàng đặc quánh. KHÔNG có chú Quạ Đen trong cảnh này. |
| b13 | 01:31.4–01:40.5 (9.1s) | L29 | Cánh Đen chỉ thả sỏi vào chiếc ống có nước, tuyệt đối không phí một chút sức lực nào để ném sỏi vào ống cát vì nó hiểu rõ cát không có tính chất chuyển động dâng lên như chất lỏng! Thưa tòa, |  | chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) chỉ thả sỏi vào ống nước, hoàn toàn ngó lơ ống cát bên cạnh vì nhận thức được tính chất vật lý của chất lỏng so với chất rắn. |
| b14 | 01:40.5–01:48.4 (7.9s) | L30 | đây chính là nhận thức trực quan phi thường về thể tích và khối lượng riêng của vật chất. Một giống loài chưa từng học qua một tiết vật lý đại cương nào lại có thể vận dụng |  | Bảng công thức tính toán thể tích vật lý nổi: Hình vẽ minh họa thể tích nước dâng lên đúng bằng thể tích viên sỏi chìm. KHÔNG có chú Quạ Đen trong cảnh này. |
| b15 | 01:48.4–01:51.4 (3.0s) | L31 | nguyên lý Archimedes một cách nhuần nhuyễn như một bản năng tự nhiên! | **VẬT LÝ NỔI** · định luật acsimet · L/300 · [0.4, 0.45] | Chân dung nhà bác học Archimedes hoạt hình trong bồn tắm giơ tay hô Eureka, bên cạnh là chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) nháy mắt đầy tự tin. |

### scene03 · ĐỌC VỊ TÂM LÝ ĐỒNG LOẠI VÀ MÀN KỊCH CHÔN MỒI GIẢ MẠO · 98.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:14.4 (14.4s) | L32 | Nếu việc thả sỏi dâng nước mới chỉ chứng minh bị cáo am hiểu sâu sắc môn vật lý cơ bản, thì chuỗi chứng cứ số hai này sẽ chứng minh Thiên Tài Cánh Đen còn là một bậc thầy lão luyện về tâm lý học hành vi và điều tra tội phạm! Trong giới động vật học hiện đại, có một khái niệm nhận thức cực kỳ cao cấp gọi |  | Bảng hồ sơ phân tích tâm lý học tội phạm: Sơ đồ não bộ với hai luồng suy nghĩ đan xen giữa kẻ lừa gạt và kẻ rình mò. KHÔNG có chú Quạ Đen trong cảnh này. |
| b02 | 00:14.4–00:20.0 (5.6s) | L33 | là Thuyết tâm trí. Đó là khả năng nhận biết rằng kẻ khác cũng có suy nghĩ, góc nhìn riêng và ý đồ cướp đoạt, | **TÂM LÝ HỌC** · đọc vị đối phương · R/320 · [0.7, 0.45] | Biểu tượng Thuyết tâm trí: Hai chiếc bóng đầu người và đầu quạ đối diện nhau, bên trong là những bánh răng suy luận logic xoay tròn. KHÔNG có chú Quạ Đen trong cảnh này. |
| b03 | 00:20.0–00:30.2 (10.2s) | L34 | từ đó dự đoán trước hành vi của đối phương để tung đòn lừa gạt hoặc thiết lập phòng thủ. Trên cõi đời này, ngoài con người và loài tinh tinh, hầu như chưa có loài chim nào chạm tới đẳng cấp tư duy trừu tượng này! |  | Kỳ thủ cờ vua thám tử: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) ngồi đối diện bàn cờ vua, tính toán trước ba nước đi tiếp theo của đối thủ một cách lạnh lùng. |
| b04 | 00:30.2–00:39.6 (9.4s) | L35 | Lời tố cáo: Bị cáo rất hay diễn trò đào bới giả vờ cất giấu kho báu nhằm lừa gạt sự chú ý của chúng tôi! Lời tố cáo hoàn toàn chính xác đến từng chi tiết! |  | Tại tòa án: Nhân chứng chim bồ câu đang run rẩy chỉ cánh về phía chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat), tố cáo chiêu trò giấu thức ăn giả mạo tinh vi. |
| b05 | 00:39.6–00:47.0 (7.4s) | L36 | Khi một con quạ kiếm được một miếng mồi béo bở, nó sẽ lập tức đảo mắt lia lịa quan sát xung quanh xem có kẻ nào đang rình mò ăn trộm hay không. |  | chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) cắp một miếng thịt mồi béo bở, mắt liếc sang cành cây đối diện nơi có một con quạ khác đang lén lút dòm ngó. |
| b06 | 00:47.0–00:53.1 (6.2s) | L37 | Nếu phát hiện có một con quạ khác đang lén lút dòm ngó từ cành cây đối diện, nó sẽ làm gì? Nó không hề bỏ chạy hoảng loạn. |  | Góc nhìn qua lăng kính thám tử: Kẻ rình mò núp sau tán lá cây bị khoanh vùng vòng tròn đỏ nét đứt phát hiện tức thì. KHÔNG có chú Quạ Đen trong cảnh này. |
| b07 | 00:53.1–00:58.5 (5.3s) | L38 | Nó giả vờ ung dung đáp xuống một bụi cỏ rậm rạp, dùng mỏ cặm cụi đào một cái hố thật sâu, làm động |  | chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) hạ cánh xuống bụi cỏ ven đường, dùng mỏ hì hục đào một cái hố sâu, làm điệu bộ vô cùng vất vả và chân thực. |
| b08 | 00:58.5–01:02.0 (3.6s) | L39 | tác nhét miếng mồi vào rồi phủ lá cây khô lên ngụy trang thật cẩn thận. |  | Động tác ngụy trang điêu luyện: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) phủ lá cây và cành khô lên miệng hố rồi dậm chân lên thật chặt như vừa chôn kho báu xong. |
| b09 | 01:02.0–01:07.9 (5.9s) | L40 | Nhưng thực chất, miếng mồi ngon lành vẫn được giấu kín mít sâu dưới cuống họng của nó! Đợi |  | Tia X-quang soi chiếu cổ họng chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat): Miếng mồi thịt béo ngậy vẫn được giấu kín mít an toàn sâu dưới đáy cuống họng. |
| b10 | 01:07.9–01:14.0 (6.2s) | L41 | đến khi kẻ rình mò hăm hở lao xuống đào bới điên cuồng cái hố rỗng tuếch kia trong sự thất vọng tột cùng, thì Thiên Tài Cánh Đen |  | Con quạ rình mò hăm hở lao xuống đào bới tung bụi cỏ, vẻ mặt ngơ ngác tột độ khi thấy chiếc hố rỗng không chẳng có gì. KHÔNG có chú Quạ Đen trong cảnh này. |
| b11 | 01:14.0–01:20.5 (6.5s) | L42 | đã sải cánh bay tít sang một khu rừng hoang vắng khác, nơi không có lấy một ánh mắt dòm ngó, để chôn giấu kho báu thực sự! |  | chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) sải cánh bay lượn trên bầu trời xanh, hướng về một cánh rừng già bí mật và vắng vẻ không bóng người. |
| b12 | 01:20.5–01:29.2 (8.7s) | L43 | Điều này chứng minh điều gì thưa quý tòa? Bị cáo hiểu rõ ràng như ban ngày rằng kẻ kia đang có dã tâm cướp mồi của mình, và bị cáo biết cách tạo ra một thông tin giả mạo đánh lừa thị giác |  | Sơ đồ chiến thuật tình báo hai mang: Quân cờ vua Vua đen trên bàn cờ đang thực hiện nước đi chiếu tướng kẻ thù. KHÔNG có chú Quạ Đen trong cảnh này. |
| b13 | 01:29.2–01:38.0 (8.8s) | L44 | để điều khiển hành vi của đối thủ theo ý mình. Chỉ có những bộ não sở hữu chỉ số mưu mô cực kỳ tinh quái mới có thể dàn dựng một kịch bản tình báo hai mang xuất sắc và lạnh lùng đến như vậy! |  | chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) đứng trên cành cây cao, tay cầm những sợi dây điều khiển con rối hoạt hình mô phỏng kẻ đối thủ đang bị dắt mũi. |

### scene04 · CHẾ TẠO CÔNG CỤ LIÊN HOÀN VÀ UỐN CONG DÂY THÉP LÀM LƯỠI CÂU · 89.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.3 (7.3s) | L45 | Thưa quý tòa, trong thế giới động vật, nhiều loài như rái cá biển biết dùng đá đập vỡ vỏ ốc, hay chim sẻ biết dùng cọng cỏ khều sâu trong kẽ nứt. |  | Bảng tiến hóa công cụ lao động: Rái cá dùng đá, chim sẻ dùng cọng cỏ, và phía trước là bục danh dự dành cho bộ óc của chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat). |
| b02 | 00:07.3–00:17.0 (9.7s) | L46 | Nhưng sử dụng một công cụ có sẵn trong tự nhiên là một chuyện, còn biết tự tay chế tạo và biến đổi hình dạng của một vật thể hoàn toàn mới theo ý đồ riêng lại là một nấc thang tiến hóa trí tuệ vượt bậc! |  | Bản vẽ phân loại công cụ: Bên trái là cành cây đá cuội tự nhiên, bên phải là bản vẽ thiết kế công cụ kim loại uốn cong tinh xảo. KHÔNG có chú Quạ Đen trong cảnh này. |
| b03 | 00:17.0–00:26.0 (9.0s) | L47 | Vào Năm 2002, một cá thể quạ New Caledonia mang tên Betty tại phòng thí nghiệm Đại học Oxford đã tạo nên một cơn địa chấn chấn động toàn bộ giới khoa học thế giới! | **NĂM 2002** · đại học oxford · L/300 · [0.35, 0.45] | Phòng nghiên cứu Đại học Oxford: Giáo sư khoa học đặt đoạn dây kim loại thẳng đứng và chiếc xô nhỏ đựng thịt trước mặt chú quạ Betty. KHÔNG có chú Quạ Đen trong cảnh này. |
| b04 | 00:26.0–00:35.2 (9.3s) | L48 | Báo cáo thực nghiệm: Betty được đưa cho sợi dây kẽm thẳng và chiếc xô thịt nhỏ ở đáy ống hẹp không thể móc được! Các bạn có hình dung được chú quạ này đã làm gì không? |  | Cận cảnh chiếc xô kim loại nhỏ đựng mồi nằm kẹt dưới đáy ống hẹp, sợi dây kẽm thẳng đuột trơn tuột không tài nào móc được quai xô. KHÔNG có chú Quạ Đen trong cảnh này. |
| b05 | 00:35.2–00:43.5 (8.2s) | L49 | Betty không hề cắn xé hay vẫy cánh bất lực. Nó bình tĩnh dùng móng chân kẹp chặt một đầu sợi dây kẽm xuống sàn, dùng chiếc mỏ cứng cáp ngậm lấy đầu kia |  | Quạ Betty dùng móng chân kẹp chặt một đầu sợi dây kẽm xuống mặt bàn gỗ, dùng mỏ ngậm đầu kia chuẩn bị uốn cong. KHÔNG có chú Quạ Đen trong cảnh này. |
| b06 | 00:43.5–00:51.3 (7.8s) | L50 | và kéo gập một góc 90°, tạo thành một chiếc móc câu cong vút hình chữ J vô cùng hoàn hảo! Sau đó, nó ngậm chiếc móc câu tự chế này, | **GÓC 90°** · uốn cong móc câu · R/320 · [0.65, 0.5] | Quá trình chế tạo kỳ diệu: Chiếc mỏ quạ bẻ gập sợi dây kẽm một góc chín mươi độ, biến thanh kẽm thẳng thành một chiếc móc câu chữ J hoàn hảo. KHÔNG có chú Quạ Đen trong cảnh này. |
| b07 | 00:51.3–00:59.6 (8.3s) | L51 | thọc thẳng xuống khe hẹp, móc chuẩn xác vào quai xô và nhấc bổng miếng thịt ngon lành lên miệng trước sự sững sờ kinh ngạc của các nhà nghiên cứu! |  | Chiếc móc câu tự chế móc chuẩn xác vào quai xô thịt, nhấc bổng chiếc xô lên khỏi miệng ống hẹp trong sự kinh ngạc của các nhà khoa học. KHÔNG có chú Quạ Đen trong cảnh này. |
| b08 | 00:59.6–01:13.6 (14.0s) | L52 | Đây là lần đầu tiên trong lịch sử nhân loại, một loài sinh vật không thuộc bộ linh trưởng lại có khả năng tự biến đổi một vật liệu kim loại nhân tạo thành công cụ chuyên dụng chính xác đến từng milimét! Và chưa dừng lại ở đó đâu thưa hội đồng, loài quạ còn giải được câu đố công |  | Tờ báo khoa học danh tiếng Nature in trang nhất hình ảnh chú quạ tự chế tạo công cụ kim loại với hàng tít giật gân. KHÔNG có chú Quạ Đen trong cảnh này. |
| b09 | 01:13.6–01:16.6 (3.1s) | L53 | cụ 8 bước liên hoàn trong các bài kiểm tra logic phức tạp: | **8 BƯỚC** · logic liên hoàn · L/320 · [0.35, 0.48] | Mê cung giải đố công cụ tám bước: Dãy que ngắn, que vừa và que dài xếp thành chuỗi mắt xích liên hoàn giải mã câu đố hóc búa. KHÔNG có chú Quạ Đen trong cảnh này. |
| b10 | 01:16.6–01:21.7 (5.1s) | L54 | Dùng chiếc que ngắn gắp chiếc que vừa, dùng chiếc que vừa lấy chiếc que dài nhất, và cuối cùng dùng chiếc que dài |  | chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) ngậm que ngắn để lấy que vừa, dùng que vừa khều lấy que dài nhất đặt trong chiếc hộp trong suốt. |
| b11 | 01:21.7–01:24.7 (3.0s) | L55 | nhất để chọc thủng ổ khóa lấy miếng thức ăn béo ngậy. Chúng có |  | chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) dùng chiếc que dài nhất chọc bật then cài ổ khóa, hộp thức ăn bật mở bung ra phần thưởng thơm lừng. |
| b12 | 01:24.7–01:29.5 (4.8s) | L56 | khả năng lập kế hoạch tương lai tuần tự trong não bộ trước khi thực hiện từng hành động cụ thể ngoài thực tế! |  | Sơ đồ não bộ dự báo tương lai: Bản đồ lộ trình từng bước đi trong đầu chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) hiển thị rõ nét trước khi chú quạ bắt tay hành động. |

### scene05 · NHẬN DIỆN KHUÔN MẶT CON NGƯỜI VÀ BẢN ÁN TRẢ THÙ KÉO DÀI 5 NĂM · 85.8s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.4 (8.4s) | L57 | Và đây chính là bản cáo trạng rùng rợn và gây sốc nhất trong toàn bộ phiên tòa hôm nay: Khả năng ghi nhớ khuôn mặt con người và lòng thù hận truyền kiếp của Thiên Tài Cánh |  | Hồ sơ đen tối thù hận truyền kiếp: Dấu vân tay và hồ sơ nhận diện các hình vẽ hoạt hình ngộ nghĩnh tội phạm được dán lên bảng điều tra trinh thám. KHÔNG có chú Quạ Đen trong cảnh này. |
| b02 | 00:08.4–00:20.3 (11.9s) | L58 | Đen! Nếu bạn từng trót dại ném một hòn đá, phá tổ hay xua đuổi một con quạ trên đường phố, lời khuyên chân thành và cấp thiết nhất của công tố viên là hãy lập tức chuyển nhà sang một thành phố khác sinh sống ngay đi! |  | Một người đàn ông hoạt hình đang ném sỏi xua đuổi chú quạ trên vỉa hè, ánh mắt chú quạ nhìn lại sắc như dao cạo. |
| b03 | 00:20.3–00:30.2 (9.9s) | L59 | Lời khai của giáo sư: Tôi từng đeo mặt nạ quái vật để gắn thẻ nhận dạng vài con quạ trong trường đại học! Và hậu quả sau đó thật là một cơn ác mộng kinh hoàng kéo dài suốt nhiều năm! |  | giáo sư già nghiên cứu sinh vật học đeo chiếc mặt nạ quái vật cau có ngộ nghĩnh đứng trước bục làm chứng, tay cầm chiếc mặt nạ quái vật bằng cao su xù xì đáng sợ từng dùng để bắt quạ. KHÔNG có chú Quạ Đen trong cảnh này. |
| b04 | 00:30.2–00:36.2 (6.0s) | L60 | Dù giáo sư có thay đổi toàn bộ quần áo, thay đổi dáng đi hay thậm chí đi lẫn giữa hàng ngàn sinh viên tấp nập, |  | Giáo sư thay đổi sang trang phục áo khoác dài khác, đi lẫn giữa đám đông sinh viên trường đại học tấp nập. KHÔNG có chú Quạ Đen trong cảnh này. |
| b05 | 00:36.2–00:42.3 (6.1s) | L61 | chỉ cần ông đeo chiếc mặt nạ đó bước ra sân trường, toàn bộ bầy quạ xung quanh lập tức gầm rú tiếng kêu báo động đặc biệt, |  | Giáo sư vừa đeo chiếc mặt nạ lên: Một chú quạ trên cây lập tức rướn cổ kêu tiếng báo động đỏ chói tai vang vọng khắp khuôn viên. |
| b06 | 00:42.3–00:47.5 (5.2s) | L62 | đồng loạt lao bổ xuống mổ tới tấp vào đầu và phóng uế liên hồi lên người ông! Điều đáng sợ đến lạnh gáy nhất |  | Cơn ác mộng bầu trời: Cả đàn quạ đen đông đúc từ tứ phía lao xuống bổ nhào, mổ túi bụi vào chiếc mặt nạ của vị giáo sư hoảng loạn. |
| b07 | 00:47.5–00:57.9 (10.4s) | L63 | là: suốt 5 năm sau đó, ngay cả những con quạ non mới sinh ra, chưa từng bị bắt giữ hay nhìn thấy mặt nạ bao giờ, cũng lập tức tham gia vào cuộc tập kích báo thù điên cuồng này! | **5 NĂM** · thù dai truyền kiếp · L/320 · [0.4, 0.48] | Tờ lịch lật qua các năm: Dòng chữ năm năm trôi qua in đậm trên nền khung cảnh mùa thu sân trường đại học. KHÔNG có chú Quạ Đen trong cảnh này. |
| b08 | 00:57.9–01:10.6 (12.6s) | L64 | Bằng một hệ thống ngôn ngữ tiếng kêu phức tạp chưa được con người giải mã hoàn toàn, quạ bố mẹ đã miêu tả chi tiết từng đặc điểm khuôn mặt của kẻ thù cho quạ con và cả những bầy quạ láng giềng xung quanh biết để cùng nhau đi trừng phạt kẻ ác! |  | Quạ bố mẹ đứng trên tổ chỉ mỏ vào bức vẽ khuôn mặt kẻ thù, giảng dạy truyền khẩu cho những chú quạ con non nớt mới nở. |
| b09 | 01:10.6–01:12.8 (2.2s) | L65 | Ngược lại, nếu một người đàn ông đeo mặt nạ |  | Sự đối lập rõ rệt: Một bên là người đàn ông đeo mặt nạ quái vật bị tấn công, một bên là người đeo mặt nạ tổng thống hiền từ được chào đón. KHÔNG có chú Quạ Đen trong cảnh này. |
| b10 | 01:12.8–01:19.3 (6.5s) | L66 | Tổng thống Dick Cheney luôn mang đồ ăn ngon đến cho chúng, bầy quạ sẽ tỏ ra vô cùng thân thiện, sà xuống quấn quýt và bay lượn chào đón nồng nhiệt. |  | Người đàn ông đeo mặt nạ tổng thống hiền từ rải hạt đậu phộng ngon lành, bầy quạ bay quanh thân thiện và đậu lên vai ông. KHÔNG có chú Quạ Đen trong cảnh này. |
| b11 | 01:19.3–01:25.8 (6.5s) | L67 | Loài quạ không chỉ nhớ mặt bạn đến từng chi tiết nhỏ, mà chúng còn nhớ bạn đã từng đối xử tử tế hay độc ác với chúng suốt nửa thập kỷ! |  | chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) cầm chiếc kính lúp soi rọi cuốn sổ thù oán và sổ ân nghĩa, nở nụ cười thám tử đầy thâm thúy. |

### scene06 · PHÁN QUYẾT CỦA TÒA ÁN TỰ NHIÊN & CÂU ĐỐ LINH THÚ TẬP 35 · 79.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:13.6 (13.6s) | L68 | Thưa quý tòa, thưa các vị bồi thẩm đoàn và toàn thể các bạn khán giả thân mến! Sau khi xem xét toàn diện chuỗi bằng chứng từ việc mượn lốp xe ô tô bóc hạt dẻ, thả sỏi dâng nước, đóng kịch giấu mồi cho đến tự chế tạo móc câu và nhớ mặt kẻ thù suốt 5 năm, Viện kiểm sát nhận thấy: |  | Toàn cảnh phòng xử án ấm áp: Ánh nắng vàng rọi qua cửa sổ kính lớn, không khí căng thẳng biến mất thay bằng sự khâm phục. KHÔNG có chú Quạ Đen trong cảnh này. |
| b02 | 00:13.6–00:18.8 (5.1s) | L69 | Hành vi của bị cáo không phải là tội ác, mà là đỉnh cao của sự thích nghi và trí tuệ sinh tồn phi thường! |  | chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) đứng trên vành móng ngựa, ánh mắt ngời sáng tự tin, ngẩng cao đầu trước toàn thể hội đồng xét xử. |
| b03 | 00:18.8–00:25.7 (6.9s) | L70 | Tuyên án: Bị cáo Quạ Đen được tuyên trắng án và được trao danh hiệu Kẻ Thông Minh Nhất Bầu Trời Tự Nhiên! |  | thẩm phán cú mèo hoạt hình nghiêm nghị đội tóc giả cổ điển trắng, tay cầm chiếc búa gỗ tòa án mỉm cười gõ nhẹ chiếc búa gỗ tuyên án trắng án, trên bàn là tấm huy chương vàng lấp lánh danh dự. |
| b04 | 00:25.7–00:31.3 (5.6s) | L71 | Một tràng pháo tay nồng nhiệt cho Thiên Tài Cánh Đen! Chúng nhắc nhở loài người chúng ta một bài học sâu sắc rằng: |  | chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) được trao tấm huy chương vàng danh dự Kẻ Thông Minh Nhất Bầu Trời Tự Nhiên, pháo hoa giấy tung bay rực rỡ. |
| b05 | 00:31.3–00:38.9 (7.6s) | L72 | Trí tuệ và khả năng tư duy không phải là đặc quyền duy nhất của bộ linh trưởng, và sự sống hoang dã luôn ẩn chứa những kỳ quan não bộ vượt xa trí tưởng tượng tầm thường của con |  | Bức tranh biểu tượng sự hòa hợp: Con người và loài quạ đen cùng đứng ngắm nhìn bầu trời bao la rộng lớn. KHÔNG có chú Quạ Đen trong cảnh này. |
| b06 | 00:38.9–00:51.5 (12.7s) | L73 | người. Lần tới nếu bạn vô tình bắt gặp một chú quạ đen bên đường, hãy cúi đầu chào nó thật lịch sự và ném cho nó một vài hạt dẻ thơm ngon nhé, vì rất có thể đôi mắt tinh anh đó đang âm thầm ghi nhớ khuôn mặt của bạn suốt 5 năm đấy! |  | Một cô bé hoạt hình mỉm cười cúi chào và đặt vài quả óc chó lên bậc thềm cho chú quạ đen đứng gần đó. KHÔNG có chú Quạ Đen trong cảnh này. |
| b07 | 00:51.5–01:01.5 (10.0s) | L74 | Còn bây giờ, giữa tài mượn lốp xe ô tô bóc vỏ hạt và khả năng nhớ mặt kẻ thù suốt 5 năm truyền lại cho đời con, bạn thấy siêu trí tuệ nào của Quạ Đen đáng kinh ngạc và gây sốc hơn? Hãy |  | Cân đo so sánh hai siêu năng lực: Một bên là bánh xe ô tô bóc hạt óc chó, một bên là bộ nhớ khuôn mặt năm năm truyền kiếp. KHÔNG có chú Quạ Đen trong cảnh này. |
| b08 | 01:01.5–01:05.3 (3.8s) | L75 | để lại ý kiến bình luận của bạn ngay bên dưới nhé! Và các bạn hãy chuẩn bị tinh |  | chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) giơ chiếc kính lúp thám tử chỉ vào ô bình luận nhấp nháy bên dưới màn hình, mời gọi khán giả thảo luận. |
| b09 | 01:05.3–01:13.5 (8.2s) | L76 | thần cho Tập 35: Chúng ta sẽ tạm rời bầu trời để lặn xuống đáy đại dương sâu thẳm, đối đầu với một gia tộc Mafia khét tiếng nhất biển cả, kẻ có biệt | **TẬP 35** · cá voi sát thủ · R/300 · [0.7, 0.45] | Khung cảnh đại dương sâu thẳm: Chiếc bóng khổng lồ của Kẻ Thống Trị Đại Dương Cá Voi Sát Thủ lao vút qua với hàm răng sắc nhọn. KHÔNG có chú Quạ Đen trong cảnh này. |
| b10 | 01:13.5–01:19.9 (6.4s) | L77 | danh Sát Thủ Biển Đen sở hữu tuyệt chiêu tạo sóng hất văng hải cẩu và dám phẫu thuật hạ gục cả Cá Mập Trắng! Hãy đón xem nhé! |  | Cảnh quay rượt đuổi nghẹt thở dưới biển: Bầy Cá Voi Sát Thủ bơi đồng bộ tạo nên ngọn sóng thần hất văng tảng băng trôi. KHÔNG có chú Quạ Đen trong cảnh này. |

## 5. Phân cảnh Shorts — từng beat

Banner: **TRÍ TUỆ QUÁI VẬT: / QUẠ ĐEN BÁO THÙ?!** · giọng 45.2s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Đừng bao giờ đắc tội với một con Quạ Đen nếu bạn không muốn bị cả dòng họ nhà |  |
| s02 | 00:04.4 | S02 | nó truy sát suốt 5 năm trời! | **5 NĂM** · thù dai truyền kiếp · L/450 · [0.35, 0.45] |
| s03 | 00:06.7 | S03 | Quạ Đen sở hữu bộ não có mật độ nơ-ron dày đặc ngang loài tinh tinh, đạt trí thông minh tương đương một đứa trẻ 7 tuổi. | **IQ 7 TUỔI** · ngang trẻ em · R/420 · [0.65, 0.48] |
| s04 | 00:13.4 | S04 | Ở Nhật Bản, khi gặp quả óc chó vỏ quá cứng, quạ thản nhiên thả hạt trước bánh xe tải |  |
| s05 | 00:17.6 | S05 | lúc Đèn xanh để xe nghiền nát hộ, rồi ung dung | **ĐÈN XANH** · nhờ xe cán hộ · L/420 · [0.3, 0.45] |
| s06 | 00:20.4 | S06 | đợi Đèn đỏ xe dừng hẳn mới sà xuống vạch đi bộ nhặt ăn ngon | **ĐÈN ĐỎ** · an toàn tuyệt đối · R/420 · [0.7, 0.45] |
| s07 | 00:23.2 | S07 | lành! Trong phòng thí nghiệm, chúng biết thả từng viên sỏi đặc vào ống nghiệm để dâng mực nước lấy thức ăn y |  |
| s08 | 00:28.8 | S08 | hệt ngụ ngôn Aesop. |  |
| s09 | 00:30.0 | S09 | Đặc biệt, nghiên cứu tại Đại học Washington chứng minh: |  |
| s10 | 00:33.0 | S10 | Quạ có thể ghi nhớ chính xác từng đường nét trên khuôn mặt kẻ thù suốt 5 năm, |  |
| s11 | 00:37.3 | S11 | rồi tả lại mặt kẻ đó cho cả bầy đàn cùng quạ con mới sinh để cùng nhau kéo đến trả thù! |  |
| s12 | 00:42.0 | S12 | Hãy đối xử thật tử tế với những thiên tài lông vũ này nhé! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trật tự! Toàn thể phòng xử án hãy giữ im lặng! Hôm nay, Viện kiểm sát Tự nhiên". Bố cục: Toàn cảnh phòng xử án Tự nhiên cổ điển trang nghiêm: thẩm phán cú mèo hoạt hình nghiêm nghị đội tóc giả cổ điển trắng, tay cầm chiếc búa gỗ tòa án ngồi trên bục cao gõ mạnh chiếc búa gỗ xét xử. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chính thức mở phiên tòa xét xử một trong những bộ óc mưu mô, quỷ quyệt và sở hữu chỉ số thông minh gây kinh hoàng bậc nhất hành tinh hoang dã. Bị cáo đứng trước vành móng ngựa hôm nay không ai khác chính là Quạ Đen, hay còn được giới giang hồ lông vũ gọi bằng mật danh Thiên Tài Cánh Đen!". Bố cục: Khung cảnh vành móng ngựa phòng xử án: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) đứng khoanh cánh ngạo nghễ, nhếch mép cười khẩy trước ánh mắt dò xét của bồi thẩm đoàn.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhìn vẻ ngoài đen nhánh từ đầu đến chân cùng tiếng kêu quạ quạ chói tai, nhiều người cứ ngỡ đây chỉ là một loài chim chuyên đi nhặt rác hôi thối hoặc mang lại điềm xui xẻo. Nhưng các vị thẩm phán và bồi thẩm đoàn hãy mở tập hồ sơ trinh sát số một ra mà xem!". Bố cục: Hình ảnh so sánh đối lập: Bên trái là một chú quạ đen bình thường nhặt rác trong thùng rác, bên phải là sơ đồ não bộ phát sáng rực rỡ của chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat).
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây không phải là một con chim bình thường, mà là một bậc thầy thao túng công nghệ và hành vi của xã hội loài người!". Bố cục: Bảng hồ sơ mật thám tử dán ghim giấy kraft: Tấm ảnh chụp lén chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) đang đứng trên cột đèn giao thông quan sát xã hội loài người. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lời khai của nhân chứng: Bị cáo mang quả óc chó vỏ cứng,". Bố cục: Hiện trường ngã tư đường phố Tokyo đông đúc: Một chú chim bồ câu ngơ ngác giơ cánh khai báo trước tòa, phía sau là dòng xe cộ tấp nập. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đặt ngay trước lốp xe tải rồi đứng đợi Đèn đỏ! Quá chính xác thưa nhân chứng! Các bạn hãy tưởng tượng xem:". Bố cục: Cận cảnh góc thấp mặt đường: Quả óc chó rừng vỏ cứng như đá cuội đặt ngay trước bánh lốp khổng lồ của chiếc xe tải lớn màu xanh đang lao qua vạch đường giao thông ngã tư phố. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một quả óc chó rừng dày cộp và cứng như đá cuội, mỏ chim có mổ gãy đôi cũng không tài nào nứt nổi. Thiên Tài Cánh Đen làm gì? Nó không hề tốn công dùng sức đập đá mù quáng.". Bố cục: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) đậu trên biển báo giao thông, mỏ ngậm quả óc chó to tướng, nghiêng đầu quan sát dòng xe đang chạy với ánh mắt đầy mưu tính.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó bay vút lên cột đèn tín hiệu giao thông, kiên nhẫn đợi Đèn xanh bật lên cho dòng xe cộ lao vun vút qua, rồi thả chính xác quả hạt xuống đúng làn bánh xe tải để". Bố cục: Đèn tín hiệu giao thông ngã tư chuyển sang Đèn xanh: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) thả quả óc chó rơi chuẩn xác xuống đúng làn bánh xe tải đang lăn bánh.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "lốp xe nghiền nát lớp vỏ cứng hộ mình! Nhưng điều ranh ma chưa dừng lại ở đó. Nó không hề lao xuống nhặt hạt ngay vì biết xe đang chạy sẽ cán chết mình.". Bố cục: Hiệu ứng va chạm mạnh mẽ: Bánh xe tải nặng nề cán qua làm vỏ quả óc chó nứt toác thành nhiều mảnh vỡ, để lộ phần nhân béo ngậy bên trong. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó bình thản đậu trên cành cây cao, quan sát thật kỹ và chờ đúng lúc". Bố cục: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) kiên nhẫn đậu trên cành cây ven đường, bình thản nhìn đồng hồ đeo tay đếm ngược chờ đợi thời cơ chín muồi.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đèn đỏ bật sáng, toàn bộ dòng xe dừng lại hẳn, mới". Bố cục: Đèn tín hiệu chuyển sang Đèn đỏ rực: Toàn bộ dòng xe dừng bánh thẳng hàng trước vạch sơn trắng. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "ung dung sà xuống vạch sang đường dành cho người đi bộ để thưởng thức bữa tiệc béo ngậy!". Bố cục: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) thong thả sải cánh đáp xuống vạch kẻ sang đường cho người đi bộ, khoan thai gắp từng miếng nhân óc chó thơm bùi ăn ngon lành.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một chiến thuật hoàn hảo, không tốn lấy một giọt mồ hôi mà lại an toàn tuyệt đối. Thưa quý tòa, đây rõ ràng là hành vi lợi dụng phương tiện giao thông hiện đại của loài người mà không chịu nộp một đồng phí cầu đường nào!". Bố cục: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) vừa nhai hạt dẻ thơm ngon vừa nháy mắt cười hóm hỉnh với bác tài xế xe tải đang nhìn qua kính chắn gió.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học thần kinh tại Đại học Cambridge đã từng đo đạc tỷ lệ thể tích não bộ so với trọng lượng cơ thể của loài quạ. Kết quả cho thấy tỷ lệ này tương đương hoàn toàn với loài tinh tinh, và". Bố cục: Sơ đồ giải phẫu thần kinh so sánh kích thước não bộ: Não của chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) và não của tinh tinh đặt cạnh nhau với tỷ lệ trọng lượng cơ thể cân bằng tuyệt đối.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "mật độ tế bào nơ-ron thần kinh ở vùng não trước của chúng cô đặc đến mức tương đương trí tuệ của một đứa trẻ 7 tuổi! Đừng bao giờ vội coi thường những sinh vật có cánh này, bởi vì ngay sau đây, công tố viên sẽ phơi bày". Bố cục: Kính hiển vi phóng to cấu trúc tế bào thần kinh vùng não trước của chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat): Hàng triệu nơ-ron liên kết phát sáng như một mạng lưới internet siêu tốc. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bốn chuỗi bằng chứng không thể chối cãi về siêu trí tuệ đáng sợ của bị cáo!". Bố cục: Tập hồ sơ án mạng mở ra: Bốn con dấu đỏ đánh số 1, 2, 3, 4 đóng lên các trang tài liệu điều tra giật gân. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thưa hội đồng xét xử, chúng ta đều từng được nghe câu chuyện ngụ ngôn Aesop thời thơ ấu về chú quạ khát nước thông minh biết gắp từng viên sỏi thả vào bình để mực nước dâng lên miệng.". Bố cục: Trang sách tranh ngụ ngôn cổ tích Aesop mở ra với hình minh họa chú quạ cổ điển đứng cạnh chiếc bình gốm khát nước. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Suốt hàng thế kỷ, con người chúng ta chỉ coi đó là một câu chuyện cổ tích mang tính phóng đại nhằm răn dạy trẻ nhỏ. Nhưng vào". Bố cục: Một nhà bác học cổ xưa ngồi dưới ngọn đèn dầu đang vẽ lại sơ đồ chiếc bình Aesop vào cuốn da cừu ố vàng. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 2014, một nhóm các nhà sinh vật học hành vi quốc tế đã quyết định đưa Thiên Tài Cánh Đen vào phòng thí nghiệm với một bài kiểm tra vật lý thủy động học cực kỳ hóc búa để xem truyền thuyết cổ tích có thật hay không!". Bố cục: Phòng thí nghiệm vật lý hiện đại: Các nhà khoa học mang áo blouse trắng chuẩn bị dàn ống nghiệm thí nghiệm thủy động học cho chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat).
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo giám định: Chúng tôi thả miếng thịt trong ống nghiệm sâu 15cm, mỏ quạ không tài nào thò tới đáy! Và chuyện gì đã diễn ra thưa quý tòa?". Bố cục: Cận cảnh ống nghiệm thủy tinh cao mười lăm centimet chứa nước: Miếng thịt thơm phức nổi lơ lửng ở giữa, mỏ quạ thò vào bị kẹt ở miệng ống.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học bày sẵn bên cạnh hai đống vật thể: một đống sỏi đá đặc nặng trĩu chìm nghỉm trong nước, và một đống xốp nhẹ nổi lơ lửng trên mặt nước.". Bố cục: Hai khay vật liệu đặt cạnh ống nghiệm: Bên trái là khay sỏi đá nặng trĩu màu xám, bên phải là khay xốp nhẹ bồng bềnh màu trắng. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một đứa trẻ dưới năm tuổi nếu không được người lớn chỉ dẫn từ trước rất có thể sẽ nhặt bừa bãi cả xốp lẫn sỏi ném vào ống nghiệm. Nhưng Thiên Tài Cánh Đen thì không!". Bố cục: Hình ảnh so sánh hài hước: Một em bé hoạt hình đang lúng túng ném lung tung các khối xốp vào nước làm nước bắn tung tóe. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó nghiêng đầu quan sát cấu trúc ống trong đúng 10 giây, rồi". Bố cục: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) nghiêng đầu góc bốn mươi lăm độ, dùng kính monocle soi xét trọng lượng từng viên sỏi đá trên bàn trong đúng mười giây.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "dùng chiếc mỏ sắc nhọn nhặt từng viên sỏi đặc thả tõm vào ống nghiệm.". Bố cục: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) cắp lấy một viên sỏi đá nặng đặc, cẩn thận thả rơi thẳng đứng xuống đáy ống nghiệm thủy tinh.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó hoàn toàn phớt lờ những miếng xốp nổi vô dụng vì hiểu rõ rằng xốp nhẹ không thể chiếm chỗ để làm thể tích nước dâng lên!". Bố cục: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) dùng chân gạt phăng đống mẩu xốp nhẹ sang một bên với vẻ mặt coi thường, hoàn toàn không chạm vào chúng.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Từng viên sỏi nặng rơi xuống đáy, mực nước dâng cao dần từng milimét, và chỉ sau". Bố cục: Mặt cắt ống nghiệm: Dưới đáy ống nghiệm là lớp sỏi đá dâng cao, đẩy cột nước dâng lên từng milimét mang theo miếng thịt mồi.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "6 lượt thả sỏi chuẩn xác, miếng thịt thơm lừng đã trôi lên tận miệng ống. Bị cáo thong thả gắp lấy miếng mồi ngon lành trước ánh mắt kinh ngạc tột độ của toàn bộ giáo sư tiến sĩ trong phòng lab! Chưa dừng lại ở đó, các nhà nghiên cứu". Bố cục: Miếng thịt trôi lên tới sát miệng ống nghiệm: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) ung dung dùng mỏ ngoạm lấy miếng mồi ngon lành trong tiếng vỗ tay tán thưởng.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tiếp tục nâng độ khó lên cấp độ tiến sĩ: Họ chuẩn bị đồng thời hai ống nghiệm, một ống chứa nước trong suốt và một ống chứa đầy cát đặc quánh. Thiên Tài Cánh Đen". Bố cục: Bài kiểm tra nâng cao: Hai chiếc ống nghiệm đặt song song, một ống chứa nước trong veo, chiếc ống còn lại chứa đầy cát vàng đặc quánh. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chỉ thả sỏi vào chiếc ống có nước, tuyệt đối không phí một chút sức lực nào để ném sỏi vào ống cát vì nó hiểu rõ cát không có tính chất chuyển động dâng lên như chất lỏng! Thưa tòa,". Bố cục: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) chỉ thả sỏi vào ống nước, hoàn toàn ngó lơ ống cát bên cạnh vì nhận thức được tính chất vật lý của chất lỏng so với chất rắn.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đây chính là nhận thức trực quan phi thường về thể tích và khối lượng riêng của vật chất. Một giống loài chưa từng học qua một tiết vật lý đại cương nào lại có thể vận dụng nguyên lý". Bố cục: Bảng công thức tính toán thể tích vật lý nổi: Hình vẽ minh họa thể tích nước dâng lên đúng bằng thể tích viên sỏi chìm. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Archimedes một cách nhuần nhuyễn như một bản năng tự nhiên!". Bố cục: Chân dung nhà bác học Archimedes hoạt hình trong bồn tắm giơ tay hô Eureka, bên cạnh là chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) nháy mắt đầy tự tin.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu việc thả sỏi dâng nước mới chỉ chứng minh bị cáo am hiểu sâu sắc môn vật lý cơ bản, thì chuỗi chứng cứ số hai này sẽ chứng minh Thiên Tài Cánh Đen còn là một bậc thầy lão luyện về tâm lý học hành vi và điều tra tội phạm! Trong giới động vật học hiện đại, có một khái niệm nhận thức cực kỳ cao cấp gọi là". Bố cục: Bảng hồ sơ phân tích tâm lý học tội phạm: Sơ đồ não bộ với hai luồng suy nghĩ đan xen giữa kẻ lừa gạt và kẻ rình mò. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thuyết tâm trí. Đó là khả năng nhận biết rằng kẻ khác cũng có suy nghĩ, góc nhìn riêng và ý đồ cướp đoạt,". Bố cục: Biểu tượng Thuyết tâm trí: Hai chiếc bóng đầu người và đầu quạ đối diện nhau, bên trong là những bánh răng suy luận logic xoay tròn. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "từ đó dự đoán trước hành vi của đối phương để tung đòn lừa gạt hoặc thiết lập phòng thủ. Trên cõi đời này, ngoài con người và loài tinh tinh, hầu như chưa có loài chim nào chạm tới đẳng cấp tư duy trừu tượng này!". Bố cục: Kỳ thủ cờ vua thám tử: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) ngồi đối diện bàn cờ vua, tính toán trước ba nước đi tiếp theo của đối thủ một cách lạnh lùng.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lời tố cáo: Bị cáo rất hay diễn trò đào bới giả vờ cất giấu kho báu nhằm lừa gạt sự chú ý của chúng tôi! Lời tố cáo hoàn toàn chính xác đến từng chi tiết!". Bố cục: Tại tòa án: Nhân chứng chim bồ câu đang run rẩy chỉ cánh về phía chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat), tố cáo chiêu trò giấu thức ăn giả mạo tinh vi.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi một con quạ kiếm được một miếng mồi béo bở, nó sẽ lập tức đảo mắt lia lịa quan sát xung quanh xem có kẻ nào đang rình mò ăn trộm hay không.". Bố cục: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) cắp một miếng thịt mồi béo bở, mắt liếc sang cành cây đối diện nơi có một con quạ khác đang lén lút dòm ngó.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu phát hiện có một con quạ khác đang lén lút dòm ngó từ cành cây đối diện, nó sẽ làm gì? Nó không hề bỏ chạy hoảng loạn.". Bố cục: Góc nhìn qua lăng kính thám tử: Kẻ rình mò núp sau tán lá cây bị khoanh vùng vòng tròn đỏ nét đứt phát hiện tức thì. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó giả vờ ung dung đáp xuống một bụi cỏ rậm rạp, dùng mỏ cặm cụi đào một cái hố thật sâu, làm động tác". Bố cục: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) hạ cánh xuống bụi cỏ ven đường, dùng mỏ hì hục đào một cái hố sâu, làm điệu bộ vô cùng vất vả và chân thực.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nhét miếng mồi vào rồi phủ lá cây khô lên ngụy trang thật cẩn thận.". Bố cục: Động tác ngụy trang điêu luyện: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) phủ lá cây và cành khô lên miệng hố rồi dậm chân lên thật chặt như vừa chôn kho báu xong.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng thực chất, miếng mồi ngon lành vẫn được giấu kín mít sâu dưới cuống họng của nó! Đợi đến khi". Bố cục: Tia X-quang soi chiếu cổ họng chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat): Miếng mồi thịt béo ngậy vẫn được giấu kín mít an toàn sâu dưới đáy cuống họng.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "kẻ rình mò hăm hở lao xuống đào bới điên cuồng cái hố rỗng tuếch kia trong sự thất vọng tột cùng, thì Thiên Tài Cánh Đen đã". Bố cục: Con quạ rình mò hăm hở lao xuống đào bới tung bụi cỏ, vẻ mặt ngơ ngác tột độ khi thấy chiếc hố rỗng không chẳng có gì. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "sải cánh bay tít sang một khu rừng hoang vắng khác, nơi không có lấy một ánh mắt dòm ngó, để chôn giấu kho báu thực sự!". Bố cục: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) sải cánh bay lượn trên bầu trời xanh, hướng về một cánh rừng già bí mật và vắng vẻ không bóng người.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Điều này chứng minh điều gì thưa quý tòa? Bị cáo hiểu rõ ràng như ban ngày rằng kẻ kia đang có dã tâm cướp mồi của mình, và bị cáo biết cách tạo ra một thông tin giả mạo đánh lừa thị giác để". Bố cục: Sơ đồ chiến thuật tình báo hai mang: Quân cờ vua Vua đen trên bàn cờ đang thực hiện nước đi chiếu tướng kẻ thù. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "điều khiển hành vi của đối thủ theo ý mình. Chỉ có những bộ não sở hữu chỉ số mưu mô cực kỳ tinh quái mới có thể dàn dựng một kịch bản tình báo hai mang xuất sắc và lạnh lùng đến như vậy!". Bố cục: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) đứng trên cành cây cao, tay cầm những sợi dây điều khiển con rối hoạt hình mô phỏng kẻ đối thủ đang bị dắt mũi.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thưa quý tòa, trong thế giới động vật, nhiều loài như rái cá biển biết dùng đá đập vỡ vỏ ốc, hay chim sẻ biết dùng cọng cỏ khều sâu trong kẽ nứt.". Bố cục: Bảng tiến hóa công cụ lao động: Rái cá dùng đá, chim sẻ dùng cọng cỏ, và phía trước là bục danh dự dành cho bộ óc của chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat).
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng sử dụng một công cụ có sẵn trong tự nhiên là một chuyện, còn biết tự tay chế tạo và biến đổi hình dạng của một vật thể hoàn toàn mới theo ý đồ riêng lại là một nấc thang tiến hóa trí tuệ vượt bậc! Vào". Bố cục: Bản vẽ phân loại công cụ: Bên trái là cành cây đá cuội tự nhiên, bên phải là bản vẽ thiết kế công cụ kim loại uốn cong tinh xảo. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 2002, một cá thể quạ New Caledonia mang tên Betty tại phòng thí nghiệm Đại học Oxford đã tạo nên một cơn địa chấn chấn động toàn bộ giới khoa học thế giới!". Bố cục: Phòng nghiên cứu Đại học Oxford: Giáo sư khoa học đặt đoạn dây kim loại thẳng đứng và chiếc xô nhỏ đựng thịt trước mặt chú quạ Betty. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo thực nghiệm: Betty được đưa cho sợi dây kẽm thẳng và chiếc xô thịt nhỏ ở đáy ống hẹp không thể móc được! Các bạn có hình dung được chú quạ này đã làm gì không?". Bố cục: Cận cảnh chiếc xô kim loại nhỏ đựng mồi nằm kẹt dưới đáy ống hẹp, sợi dây kẽm thẳng đuột trơn tuột không tài nào móc được quai xô. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Betty không hề cắn xé hay vẫy cánh bất lực. Nó bình tĩnh dùng móng chân kẹp chặt một đầu sợi dây kẽm xuống sàn, dùng chiếc mỏ cứng cáp ngậm lấy đầu kia và". Bố cục: Quạ Betty dùng móng chân kẹp chặt một đầu sợi dây kẽm xuống mặt bàn gỗ, dùng mỏ ngậm đầu kia chuẩn bị uốn cong. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "kéo gập một góc 90°, tạo thành một chiếc móc câu cong vút hình chữ J vô cùng hoàn hảo! Sau đó, nó ngậm chiếc móc câu tự chế này,". Bố cục: Quá trình chế tạo kỳ diệu: Chiếc mỏ quạ bẻ gập sợi dây kẽm một góc chín mươi độ, biến thanh kẽm thẳng thành một chiếc móc câu chữ J hoàn hảo. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thọc thẳng xuống khe hẹp, móc chuẩn xác vào quai xô và nhấc bổng miếng thịt ngon lành lên miệng trước sự sững sờ kinh ngạc của các nhà nghiên cứu!". Bố cục: Chiếc móc câu tự chế móc chuẩn xác vào quai xô thịt, nhấc bổng chiếc xô lên khỏi miệng ống hẹp trong sự kinh ngạc của các nhà khoa học. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây là lần đầu tiên trong lịch sử nhân loại, một loài sinh vật không thuộc bộ linh trưởng lại có khả năng tự biến đổi một vật liệu kim loại nhân tạo thành công cụ chuyên dụng chính xác đến từng milimét! Và chưa dừng lại ở đó đâu thưa hội đồng, loài quạ còn giải được câu đố công cụ". Bố cục: Tờ báo khoa học danh tiếng Nature in trang nhất hình ảnh chú quạ tự chế tạo công cụ kim loại với hàng tít giật gân. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "8 bước liên hoàn trong các bài kiểm tra logic phức tạp:". Bố cục: Mê cung giải đố công cụ tám bước: Dãy que ngắn, que vừa và que dài xếp thành chuỗi mắt xích liên hoàn giải mã câu đố hóc búa. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dùng chiếc que ngắn gắp chiếc que vừa, dùng chiếc que vừa lấy chiếc que dài nhất, và cuối cùng dùng chiếc que dài nhất để". Bố cục: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) ngậm que ngắn để lấy que vừa, dùng que vừa khều lấy que dài nhất đặt trong chiếc hộp trong suốt.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chọc thủng ổ khóa lấy miếng thức ăn béo ngậy. Chúng có khả năng". Bố cục: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) dùng chiếc que dài nhất chọc bật then cài ổ khóa, hộp thức ăn bật mở bung ra phần thưởng thơm lừng.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "lập kế hoạch tương lai tuần tự trong não bộ trước khi thực hiện từng hành động cụ thể ngoài thực tế!". Bố cục: Sơ đồ não bộ dự báo tương lai: Bản đồ lộ trình từng bước đi trong đầu chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) hiển thị rõ nét trước khi chú quạ bắt tay hành động.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và đây chính là bản cáo trạng rùng rợn và gây sốc nhất trong toàn bộ phiên tòa hôm nay: Khả năng ghi nhớ khuôn mặt con người và lòng thù hận truyền kiếp của Thiên Tài Cánh Đen!". Bố cục: Hồ sơ đen tối thù hận truyền kiếp: Dấu vân tay và hồ sơ nhận diện các hình vẽ hoạt hình ngộ nghĩnh tội phạm được dán lên bảng điều tra trinh thám. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu bạn từng trót dại ném một hòn đá, phá tổ hay xua đuổi một con quạ trên đường phố, lời khuyên chân thành và cấp thiết nhất của công tố viên là hãy lập tức chuyển nhà sang một thành phố khác sinh sống ngay đi!". Bố cục: Một người đàn ông hoạt hình đang ném sỏi xua đuổi chú quạ trên vỉa hè, ánh mắt chú quạ nhìn lại sắc như dao cạo.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lời khai của giáo sư: Tôi từng đeo mặt nạ quái vật để gắn thẻ nhận dạng vài con quạ trong trường đại học! Và hậu quả sau đó thật là một cơn ác mộng kinh hoàng kéo dài suốt nhiều năm!". Bố cục: giáo sư già nghiên cứu sinh vật học đeo chiếc mặt nạ quái vật cau có ngộ nghĩnh đứng trước bục làm chứng, tay cầm chiếc mặt nạ quái vật bằng cao su xù xì đáng sợ từng dùng để bắt quạ. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dù giáo sư có thay đổi toàn bộ quần áo, thay đổi dáng đi hay thậm chí đi lẫn giữa hàng ngàn sinh viên tấp nập,". Bố cục: Giáo sư thay đổi sang trang phục áo khoác dài khác, đi lẫn giữa đám đông sinh viên trường đại học tấp nập. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chỉ cần ông đeo chiếc mặt nạ đó bước ra sân trường, toàn bộ bầy quạ xung quanh lập tức gầm rú tiếng kêu báo động đặc biệt,". Bố cục: Giáo sư vừa đeo chiếc mặt nạ lên: Một chú quạ trên cây lập tức rướn cổ kêu tiếng báo động đỏ chói tai vang vọng khắp khuôn viên.
```
</details>

<details><summary>L62</summary>

```text
HÌNH L62 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đồng loạt lao bổ xuống mổ tới tấp vào đầu và phóng uế liên hồi lên người ông! Điều đáng sợ đến lạnh gáy nhất là:". Bố cục: Cơn ác mộng bầu trời: Cả đàn quạ đen đông đúc từ tứ phía lao xuống bổ nhào, mổ túi bụi vào chiếc mặt nạ của vị giáo sư hoảng loạn.
```
</details>

<details><summary>L63</summary>

```text
HÌNH L63 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "suốt 5 năm sau đó, ngay cả những con quạ non mới sinh ra, chưa từng bị bắt giữ hay nhìn thấy mặt nạ bao giờ, cũng lập tức tham gia vào cuộc tập kích báo thù điên cuồng này!". Bố cục: Tờ lịch lật qua các năm: Dòng chữ năm năm trôi qua in đậm trên nền khung cảnh mùa thu sân trường đại học. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L64</summary>

```text
HÌNH L64 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bằng một hệ thống ngôn ngữ tiếng kêu phức tạp chưa được con người giải mã hoàn toàn, quạ bố mẹ đã miêu tả chi tiết từng đặc điểm khuôn mặt của kẻ thù cho quạ con và cả những bầy quạ láng giềng xung quanh biết để cùng nhau đi trừng phạt kẻ ác!". Bố cục: Quạ bố mẹ đứng trên tổ chỉ mỏ vào bức vẽ khuôn mặt kẻ thù, giảng dạy truyền khẩu cho những chú quạ con non nớt mới nở.
```
</details>

<details><summary>L65</summary>

```text
HÌNH L65 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngược lại, nếu một người đàn ông đeo mặt nạ Tổng thống". Bố cục: Sự đối lập rõ rệt: Một bên là người đàn ông đeo mặt nạ quái vật bị tấn công, một bên là người đeo mặt nạ tổng thống hiền từ được chào đón. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L66</summary>

```text
HÌNH L66 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dick Cheney luôn mang đồ ăn ngon đến cho chúng, bầy quạ sẽ tỏ ra vô cùng thân thiện, sà xuống quấn quýt và bay lượn chào đón nồng nhiệt.". Bố cục: Người đàn ông đeo mặt nạ tổng thống hiền từ rải hạt đậu phộng ngon lành, bầy quạ bay quanh thân thiện và đậu lên vai ông. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L67</summary>

```text
HÌNH L67 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Loài quạ không chỉ nhớ mặt bạn đến từng chi tiết nhỏ, mà chúng còn nhớ bạn đã từng đối xử tử tế hay độc ác với chúng suốt nửa thập kỷ!". Bố cục: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) cầm chiếc kính lúp soi rọi cuốn sổ thù oán và sổ ân nghĩa, nở nụ cười thám tử đầy thâm thúy.
```
</details>

<details><summary>L68</summary>

```text
HÌNH L68 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thưa quý tòa, thưa các vị bồi thẩm đoàn và toàn thể các bạn khán giả thân mến! Sau khi xem xét toàn diện chuỗi bằng chứng từ việc mượn lốp xe ô tô bóc hạt dẻ, thả sỏi dâng nước, đóng kịch giấu mồi cho đến tự chế tạo móc câu và nhớ mặt kẻ thù suốt 5 năm, Viện kiểm sát nhận thấy:". Bố cục: Toàn cảnh phòng xử án ấm áp: Ánh nắng vàng rọi qua cửa sổ kính lớn, không khí căng thẳng biến mất thay bằng sự khâm phục. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L69</summary>

```text
HÌNH L69 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hành vi của bị cáo không phải là tội ác, mà là đỉnh cao của sự thích nghi và trí tuệ sinh tồn phi thường!". Bố cục: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) đứng trên vành móng ngựa, ánh mắt ngời sáng tự tin, ngẩng cao đầu trước toàn thể hội đồng xét xử.
```
</details>

<details><summary>L70</summary>

```text
HÌNH L70 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyên án: Bị cáo Quạ Đen được tuyên trắng án và được trao danh hiệu Kẻ Thông Minh Nhất Bầu Trời Tự Nhiên!". Bố cục: thẩm phán cú mèo hoạt hình nghiêm nghị đội tóc giả cổ điển trắng, tay cầm chiếc búa gỗ tòa án mỉm cười gõ nhẹ chiếc búa gỗ tuyên án trắng án, trên bàn là tấm huy chương vàng lấp lánh danh dự.
```
</details>

<details><summary>L71</summary>

```text
HÌNH L71 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một tràng pháo tay nồng nhiệt cho Thiên Tài Cánh Đen! Chúng nhắc nhở loài người chúng ta một bài học sâu sắc rằng:". Bố cục: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) được trao tấm huy chương vàng danh dự Kẻ Thông Minh Nhất Bầu Trời Tự Nhiên, pháo hoa giấy tung bay rực rỡ.
```
</details>

<details><summary>L72</summary>

```text
HÌNH L72 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trí tuệ và khả năng tư duy không phải là đặc quyền duy nhất của bộ linh trưởng, và sự sống hoang dã luôn ẩn chứa những kỳ quan não bộ vượt xa trí tưởng tượng tầm thường của con người.". Bố cục: Bức tranh biểu tượng sự hòa hợp: Con người và loài quạ đen cùng đứng ngắm nhìn bầu trời bao la rộng lớn. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L73</summary>

```text
HÌNH L73 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lần tới nếu bạn vô tình bắt gặp một chú quạ đen bên đường, hãy cúi đầu chào nó thật lịch sự và ném cho nó một vài hạt dẻ thơm ngon nhé, vì rất có thể đôi mắt tinh anh đó đang âm thầm ghi nhớ khuôn mặt của bạn suốt 5 năm đấy!". Bố cục: Một cô bé hoạt hình mỉm cười cúi chào và đặt vài quả óc chó lên bậc thềm cho chú quạ đen đứng gần đó. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L74</summary>

```text
HÌNH L74 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn bây giờ, giữa tài mượn lốp xe ô tô bóc vỏ hạt và khả năng nhớ mặt kẻ thù suốt 5 năm truyền lại cho đời con, bạn thấy siêu trí tuệ nào của Quạ Đen đáng kinh ngạc và gây sốc hơn? Hãy để lại". Bố cục: Cân đo so sánh hai siêu năng lực: Một bên là bánh xe ô tô bóc hạt óc chó, một bên là bộ nhớ khuôn mặt năm năm truyền kiếp. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L75</summary>

```text
HÌNH L75 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "ý kiến bình luận của bạn ngay bên dưới nhé! Và các bạn hãy chuẩn bị tinh thần cho". Bố cục: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat) giơ chiếc kính lúp thám tử chỉ vào ô bình luận nhấp nháy bên dưới màn hình, mời gọi khán giả thảo luận.
```
</details>

<details><summary>L76</summary>

```text
HÌNH L76 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tập 35: Chúng ta sẽ tạm rời bầu trời để lặn xuống đáy đại dương sâu thẳm, đối đầu với một gia tộc Mafia khét tiếng nhất biển cả, kẻ có biệt danh". Bố cục: Khung cảnh đại dương sâu thẳm: Chiếc bóng khổng lồ của Kẻ Thống Trị Đại Dương Cá Voi Sát Thủ lao vút qua với hàm răng sắc nhọn. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>L77</summary>

```text
HÌNH L77 (16:9 ngang, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sát Thủ Biển Đen sở hữu tuyệt chiêu tạo sóng hất văng hải cẩu và dám phẫu thuật hạ gục cả Cá Mập Trắng! Hãy đón xem nhé!". Bố cục: Cảnh quay rượt đuổi nghẹt thở dưới biển: Bầy Cá Voi Sát Thủ bơi đồng bộ tạo nên ngọn sóng thần hất văng tảng băng trôi. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đừng bao giờ đắc tội với một con Quạ Đen nếu bạn không muốn bị cả dòng họ nhà nó". Bố cục: chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng mặc áo khoác măng tô thám tử, giơ một ngón cánh cảnh báo khán giả với nụ cười bí hiểm.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "truy sát suốt 5 năm trời!". Bố cục: Hình ảnh gia tộc quạ đen đông đúc đeo kính râm thám tử bay lượn rợp trời tạo thành đội hình truy lùng gắt gao. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Quạ Đen sở hữu bộ não có mật độ nơ-ron dày đặc ngang loài tinh tinh, đạt trí thông minh tương đương một đứa trẻ 7 tuổi.". Bố cục: Sơ đồ não bộ phát sáng của quạ đen đặt cạnh não tinh tinh với mật độ nơ-ron dày đặc ngang ngửa đứa trẻ bảy tuổi.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Ở Nhật Bản, khi gặp quả óc chó vỏ quá cứng, quạ thản nhiên thả hạt trước bánh xe tải lúc". Bố cục: chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng đứng trên cột đèn tín hiệu Shibuya, mỏ ngậm quả óc chó vỏ cứng nhìn dòng xe cộ chạy bên dưới.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đèn xanh để xe nghiền nát hộ, rồi ung dung đợi". Bố cục: Đèn xanh bật sáng: chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng thả quả óc chó xuống đường, bánh xe tải khổng lồ cán qua làm vỏ hạt nứt toác tung tóe.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đèn đỏ xe dừng hẳn mới sà xuống vạch đi bộ nhặt ăn ngon lành!". Bố cục: Đèn đỏ bật lên: Dòng xe dừng lại hoàn toàn, chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng ung dung sà xuống vạch sang đường gắp hạt béo ngậy ăn ngon lành.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Trong phòng thí nghiệm, chúng biết thả từng viên sỏi đặc vào ống nghiệm để dâng mực nước lấy thức ăn y hệt". Bố cục: chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng gắp từng viên sỏi đặc thả vào ống nghiệm thủy tinh hẹp chứa nước để mực nước dâng lên lấy miếng thịt.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "ngụ ngôn Aesop.". Bố cục: Cuốn sách ngụ ngôn Aesop mở ra với hình minh họa chú quạ thả sỏi dâng nước chuẩn xác như định luật vật lý.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đặc biệt, nghiên cứu tại Đại học Washington chứng minh:". Bố cục: giáo sư già nghiên cứu sinh vật học đeo chiếc mặt nạ quái vật cau có ngộ nghĩnh đeo chiếc mặt nạ quái vật bị bầy quạ nhào xuống tập kích báo thù dữ dội khắp sân trường. KHÔNG có chú Quạ Đen trong cảnh này.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Quạ có thể ghi nhớ chính xác từng đường nét trên khuôn mặt kẻ thù suốt 5 năm, rồi". Bố cục: Kính lúp phóng to hồ sơ nhận diện hình vẽ mặt cười hoạt hình ngộ nghĩnh: Các đường nét góc cạnh trên gương mặt kẻ thù được quạ lưu trữ trong bộ nhớ.
```
</details>

<details><summary>S11</summary>

```text
HÌNH S11 (DỌC 9:16, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "tả lại mặt kẻ đó cho cả bầy đàn cùng quạ con mới sinh để cùng nhau kéo đến trả thù!". Bố cục: Quạ bố mẹ đứng trên cành cây mô tả chi tiết khuôn mặt kẻ thù cho quạ con và cả bầy đàn cùng ghi nhớ.
```
</details>

<details><summary>S12</summary>

```text
HÌNH S12 (DỌC 9:16, phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage thập niên 1920 (Vintage Newspaper Engraving) và nhân vật chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Hãy đối xử thật tử tế với những thiên tài lông vũ này nhé!". Bố cục: chú Quạ Đen thám tử mặc áo măng tô và kính monocle vàng mỉm cười thân thiện, nghiêng đầu nháy mắt chào khán giả với một quả óc chó thơm ngon trên cánh.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/77 của video YouTube về Quạ Đen). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage London thập niên 1920 (Vintage Newspaper Woodcut & Crosshatch Engraving): nét bút sắt crosshatch điêu luyện, độ tương phản đen trắng kịch tính điện ảnh noir, chi tiết kính lúp điều tra, dấu vết hiện trường tinh xảo, vệt sáp niêm phong đỏ, hồ sơ mật giấy kraft hoài cổ điểm xuyết vàng kim sang trọng; NỀN TRẮNG TINH hoàn toàn, không watermark, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat). Nhân vật phụ cố định: thẩm phán cú mèo hoạt hình nghiêm nghị đội tóc giả cổ điển trắng, tay cầm chiếc búa gỗ tòa án; chiếc xe tải lớn màu xanh đang lao qua vạch đường giao thông ngã tư phố; ống nghiệm thủy tinh hẹp chứa nước trong và miếng mồi thịt thơm nổi trên mặt; giáo sư già nghiên cứu sinh vật học đeo chiếc mặt nạ quái vật cau có ngộ nghĩnh. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/12 của video YouTube Shorts về Quạ Đen). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách ký họa trinh thám Sherlock Noir & tranh khắc báo chí vintage London thập niên 1920 (Vintage Newspaper Woodcut & Crosshatch Engraving): nét bút sắt crosshatch điêu luyện, độ tương phản đen trắng kịch tính điện ảnh noir, chi tiết kính lúp điều tra, dấu vết hiện trường tinh xảo, vệt sáp niêm phong đỏ, hồ sơ mật giấy kraft hoài cổ điểm xuyết vàng kim sang trọng; NỀN TRẮNG TINH hoàn toàn, không watermark, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Quạ Đen hoạt hình thông minh sắc sảo, mặc áo khoác măng tô thám tử màu nâu cổ điển, đeo kính một mắt monocle vàng và mỏ ngậm chiếc tẩu thuốc hoạt hình ngộ nghĩnh (cute clever cartoon black crow detective wearing a classic trench coat, golden monocle, and funny Sherlock hat). Nhân vật phụ: giáo sư già nghiên cứu sinh vật học đeo chiếc mặt nạ quái vật cau có ngộ nghĩnh. 
```
</details>

## 7. SEO

- **title:** Trí Tuệ Quái Vật: Nhờ Xe Ô Tô Cán Hạt Cứng & Nhớ Mặt Kẻ Thù 5 Năm?! | Tập 34
- **hook_paragraph:** Quạ Đen (Corvus) sở hữu bộ não có tỷ lệ tương đương loài tinh tinh, đạt trí thông minh ngang ngửa một đứa trẻ bảy tuổi. Chúng không chỉ biết lợi dụng đèn đỏ để xe ô tô cán hộ quả óc chó, mà còn biết tự uốn cong dây thép thành móc câu và ghi nhớ mặt kẻ thù suốt năm năm truyền lại cho đàn con!
- **question:** Giữa tài mượn lốp xe ô tô bóc vỏ hạt và khả năng nhớ mặt kẻ thù suốt 5 năm, bạn thấy siêu trí tuệ nào của Quạ Đen đáng sợ hơn?
- **next_teaser:** loài thú săn mồi đen trắng thống trị đại dương, kẻ hạ gục cá mập trắng chỉ bằng một đòn lật ngửa
- **shorts_title:** Đừng bao giờ đắc tội với Quạ Đen nếu không muốn bị cả đàn trả thù 5 năm!
- **shorts_desc:** Quạ Đen sở hữu trí tuệ tương đương trẻ em 7 tuổi, biết dùng đèn giao thông để xe cán hạt và nhớ mặt kẻ thù suốt 5 năm!
- **bullets:** Bộ não có mật độ nơ-ron dày đặc ngang loài linh trưởng cấp cao · Chiến thuật đèn đỏ đèn xanh: Nhờ lốp xe tải cán hộ hạt cứng không tốn giọt mồ hôi · Thí nghiệm Aesop kinh điển: Thả sỏi dâng mực nước lấy mồi ăn cực kỳ chuẩn xác · Khả năng đọc vị tâm lý đồng loại: Giả vờ chôn giấu mồi để đánh lạc hướng kẻ rình mò · Hồ sơ ghi nhớ mặt người: Nhớ mặt kẻ đeo mặt nạ suốt năm năm và phát động cả bầy báo thù · Teaser Tập 35: Cuộc chạm trán với Kẻ Thống Trị Đại Dương sở hữu chiến thuật săn bầy đàn thượng thừa
- **tags:** quạ đen, quạ, corvus, trí tuệ động vật, chim thông minh, vẽ chuyện hoang dã, whiteboard animation

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-34-qua-den
python src/episode/pipeline.py tts    projects/tap-34-qua-den     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-34-qua-den     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-34-qua-den     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-34-qua-den              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-34-qua-den --force
python scripts/beat_sheet.py projects/tap-34-qua-den               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-34-qua-den/audio/shorts.wav projects/tap-34-qua-den/renders/tap-34-qua-den_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-34-qua-den
python src/episode/pipeline.py seo    projects/tap-34-qua-den
python src/episode/episode_doc.py     projects/tap-34-qua-den
```

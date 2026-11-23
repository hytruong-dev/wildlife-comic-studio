# CẨM NANG VẬN HÀNH & KỊCH BẢN SẢN XUẤT KÊNH YOUTUBE: "VẼ CHUYỆN HOANG DÃ"

Tài liệu này bao gồm toàn bộ quy chuẩn kỹ thuật đã được hiệu chỉnh từ video thực tế của kênh, bộ câu lệnh (Prompt) tạo ảnh AI đồng bộ, kịch bản hoàn chỉnh để sản xuất ngay và lộ trình chi tiết 30 ngày ($60\text{ Video Dài} + 60\text{ YouTube Shorts}$).

---

## PHẦN 1: QUY CHUẨN KỸ THUẬT & HƯỚNG DẪN KHẮC PHỤC LỖI TỪ VIDEO THỰC TẾ

### 1.1. 5 Thay Đổi Bắt Buộc Khi Xuất Video Dài (Giữ Nguyên Intro & Outro Của Kênh)
1. **Xóa nhãn kỹ thuật trên thanh tiêu đề:** Tuyệt đối không in các chữ chỉ dẫn kịch bản như `[PHẦN 1: THE MYTH-BUSTER HOOK]`, `[PHẦN 4: CÚ BẺ LÁI CỦA TẠO HÓA]`, `[PHẦN 6: LỜI NHẮN NHỦ BÌNH THẢN]` hay `02. TEASER` lên màn hình video. Chỉ giữ lại tên chương ngắn gọn, kích thích sự tò mò.
2. **Triệt tiêu "Khoảng chết âm thanh" $3\text{ giây}$ cuối mỗi bức tranh:** Thiết lập trong phần mềm để bàn tay viết dòng chú thích bên dưới bức tranh **chạy song song cùng lúc giọng đọc đang phát câu cuối cùng** của cảnh đó. Ngay khi giọng đọc vừa dứt chữ cuối là chuyển sang vẽ bức tranh tiếp theo ngay lập tức.
3. **Làm sạch lời thoại AI (Voice-over):**
   * Xóa bỏ toàn bộ tiếng cười *"Hơ hơ"* gượng gạo ở đầu các phân cảnh.
   * Không đọc các câu lộ cấu trúc kịch bản (ví dụ: *"vào phút thứ tư của câu chuyện"*).
   * Việt hóa toàn bộ thuật ngữ tiếng Anh chêm giữa câu (không đọc *Pouch Capacity*, *Gluttony*, *Spinal Cooling*, *Gular Pouch*... để tránh làm gãy nhịp nghe tiếng Việt).
4. **Chèn lời dẫn vào cảnh tổng hợp cuối mỗi phần:** Ở các khung hình gom $4 - 5$ bức tranh nhỏ lại với nhau (giây `01:06`, `02:15`, `03:53`...), không được để trống giọng đọc. Hãy chèn 1 câu chuyển ý ngắn dài $3\text{ giây}$ để giữ mạch liên tục.
5. **Không lặp lại thông tin:** Mỗi chi tiết đắt giá (như túi mỏ $13\text{ lít}$, kẹp Capybara, lộn cổ tản nhiệt, đứng đơ $1\text{ phút}$ dốc nước) chỉ được phép giải thích sâu **đúng 1 lần duy nhất** trong video.

---

### 1.2. Quy Chuẩn Khung Hình Dọc $9:16$ Cho YouTube Shorts ($1080 \times 1920\text{ px}$)
* **Từ $0 \rightarrow 200\text{ px}$ (Đỉnh màn hình):** Để trống tránh thanh giao diện tìm kiếm của YouTube.
* **Từ $200 \rightarrow 380\text{ px}$ (Thanh Tiêu Đề Cố Định):** Đặt 1 khung bo tròn duy nhất, chữ in hoa đậm, tối đa $6 - 8\text{ chữ}$ (Ví dụ: `KẺ NUỐT CHỬNG MỌI THỨ BIẾT ĐI!`).
* **Từ $380 \rightarrow 1250\text{ px}$ (Sân Khấu Vẽ Chính):**
  * Chỉ hiển thị **1 bức tranh lớn duy nhất** tại một thời điểm (không chia 2 tầng trên/dưới bằng đường kẻ ngang).
  * Bàn tay cầm bút **vẽ nét viền con vật** trong $1.5 - 2\text{ giây}$, sau đó bung màu rực rỡ kèm hiệu ứng phóng to nhẹ ($100\% \rightarrow 112\%$).
* **Từ $1250 \rightarrow 1480\text{ px}$ (Vùng Phụ Đề Động):** Bỏ hoàn toàn việc dùng bàn tay chép lại lời thoại. Thay bằng phụ đề tự động (Auto Captions) nhảy từng cụm $3 - 4\text{ chữ}$, font chữ dày (Montserrat Black / Anton), màu vàng hoặc trắng viền đen dày.
* **Từ $1480 \rightarrow 1920\text{ px}$ (Vùng Chết Đáy Màn Hình):** Để trống hoàn toàn nền giấy, không đặt chữ hay chi tiết quan trọng vì sẽ bị Tên kênh, Tiêu đề Shorts và nút **Video có liên quan** đè khuất.

---

### 1.3. Công Thức Câu Lệnh (Prompt) Tạo Ảnh AI Đồng Bộ 100%
Để ảnh đưa vào phần mềm vẽ tay có nét viền đen rõ ràng, màu sắc đồng nhất và **không bao giờ bị dính chữ tiếng Anh rác**, hãy luôn ghép **Câu lệnh khóa phong cách (Master Style Prompt)** dưới đây vào cuối mọi mô tả cảnh vẽ:

> **Master Style Prompt:**
> `Clean 2D comic cartoon illustration on pure solid white background, bold black ink outlines, vibrant flat colors, exaggerated funny cartoon facial expressions, clear silhouette for whiteboard animation drawing, no text, no letters, no words, no labels, no numbers, no watermark --ar 16:9` *(Đổi thành `--ar 9:16` hoặc `--ar 1:1` khi làm Shorts)*.

---

## PHẦN 2: KỊCH BẢN NÂNG CẤP HOÀN CHỈNH – TẬP 05: CHIM BỒ NÔNG (BẢN VIDEO DÀI & SHORTS)

*(Bản kịch bản này giữ nguyên Intro `00:00–00:09` và Outro `08:04–08:13` của bạn, nhưng đã cấu trúc lại toàn bộ phần thân từ `00:10` đến `08:03` để xóa sạch lỗi lặp ý 4 lần, bỏ nhãn kỹ thuật và bổ sung tập tính mới).*

### 2.1. Kịch Bản Video Dài Tập 05 (Thời lượng: $8\text{ phút } 15\text{ giây}$)

#### [GIỮ NGUYÊN INTRO KÊNH: 00:00 – 00:09]

#### CHƯƠNG 1: PHẢN XẠ KẸP MỌI THỨ CHUYỂN ĐỘNG (00:10 – 01:15)
* **Cảnh 1.1: Cú kẹp vô tri (00:10 – 00:30)**
  * **Tiêu đề trên màn hình:** `01. PHẢN XẠ KẸP MỌI THỨ` *(Đã xóa dòng [PHẦN 1...])*
  * **Hình vẽ:** Bồ nông há to mỏ kẹp ngang lưng chú Capybara béo tròn đang ngồi ngơ ngác, bên cạnh là cá và chim bay tán loạn.
  * **Lời thoại (Voice):** "Bạn đã bao giờ thấy một kẻ săn mồi có đôi mắt to hơn cả não bộ chưa? Hãy gặp gỡ Chim Bồ Nông — sinh vật kỳ quặc đến mức cứ thấy bất kỳ thứ gì nhúc nhích trước mặt, dù là con cá, chim bồ câu hay cả một chú chuột lang nước Capybara béo ú to gấp năm lần cái đầu của nó, nó cũng phải há to mỏ kẹp thử xem có nuốt trôi hay không!"
  * **Chú thích viết tay (chạy song song câu cuối):** `Thấy gì cử động là há mỏ kẹp thử ngay lập tức`
* **Cảnh 1.2: Cú sốc thế kỷ 18 (00:30 – 00:50)**
  * **Tiêu đề trên màn hình:** `02. CÚ SỐC THẾ KỶ 18`
  * **Hình vẽ:** Ba nhà thám hiểm phương Tây thế kỷ 18 mặc đồ cổ điển ôm đầu kinh ngạc nhìn bồ nông há mỏ xúc nguyên con vịt trời dưới sông.
  * **Lời thoại (Voice):** "Cơn tham ăn vô độ này từng khiến các nhà thám hiểm phương Tây thế kỷ mười tám khi mới đặt chân đến châu Úc phải bàng hoàng. Họ đã ghi chép lại cảnh tượng những con chim bồ nông trắng khổng lồ đứng bên bờ sông, thản nhiên há chiếc mỏ to như chiếc võng da và nuốt chửng cả những con vịt trời đang bơi ngang qua!"
  * **Chú thích viết tay:** `Thế kỷ 18: Thám hiểm bàng hoàng thấy bồ nông nuốt vịt`
* **Cảnh 1.3: Giải mã bộ não phản xạ siêu tốc (00:50 – 01:15)** *(Đôn từ cuối video lên để giải thích nguyên nhân ngay lập tức)*
  * **Tiêu đề trên màn hình:** `03. BỘ NÃO KẸP TRƯỚC NGHĨ SAU`
  * **Hình vẽ:** Sơ đồ cắt lớp hài hước trong đầu bồ nông: Con mắt nhìn thấy con cá $\rightarrow$ Chuông báo động đỏ reo vang bấm nút kéo ròng rọc mở mỏ, trong khi ông già "Não bộ" phía sau vẫn đang nằm ngáy ngủ trên giường.
  * **Lời thoại (Voice):** "Tại sao chúng lại hành động ngớ ngẩn như vậy? Các nhà sinh vật học phát hiện ra vùng phản xạ thị giác của bồ nông cực kỳ nhạy bén với chuyển động. Ngay khi mắt vừa thấy vật thể di chuyển, dây thần kinh lập tức giật chốt mở toang chiếc mỏ để tóm gọn con mồi trước cả khi não bộ kịp thức dậy để phân tích xem thứ đó có ăn được hay không!"
  * **Chú thích viết tay:** `Phản xạ thị giác ra lệnh kẹp mồi trước khi não kịp nghĩ`

#### CHƯƠNG 2: BẢNG CHỈ SỐ SINH TỒN DỊ BIỆT (01:15 – 02:25)
* **Cảnh 2.1: Thẻ bài Sức chứa (01:15 – 01:32)**
  * **Tiêu đề trên màn hình:** `01. CHỈ SỐ SỨC CHỨA: 999/100`
  * **Hình vẽ:** Khung thẻ bài game RPG lấp lánh, bồ nông há mỏ chứa đầy nước và cá.
  * **Lời thoại (Voice):** "Nếu đưa loài chim này vào thế giới game sinh tồn, bảng chỉ số của nó chắc chắn sẽ làm mọi game thủ cạn lời. Đầu tiên là chỉ số Sức chứa túi mỏ đạt mức tối đa chín trăm chín mươi chín điểm! Chiếc túi da dưới cằm có thể phình to như một quả bóng bay khổng lồ, chứa được khối lượng nước gấp ba lần thể tích toàn bộ dạ dày của chính nó."
  * **Chú thích viết tay:** `Sức chứa 999/100: Túi mỏ phình to gấp 3 lần dạ dày`
* **Cảnh 2.2: Thẻ bài Độ tham ăn (01:32 – 01:48)**
  * **Tiêu đề trên màn hình:** `02. ĐỘ THAM ĂN: 999/100`
  * **Hình vẽ:** Thẻ bài RPG vẽ cảnh bồ nông rướn cổ đo thử vòng bụng của Capybara.
  * **Lời thoại (Voice):** "Thứ hai là chỉ số Tham ăn vô độ cũng chạm đỉnh tuyệt đối! Nhờ thực đơn không kén chọn từ cá chép, động vật giáp xác, rùa nhỏ cho đến cả chim biển, bồ nông không bao giờ bỏ lỡ bất kỳ cơ hội kiếm ăn nào xuất hiện trong tầm mắt."
  * **Chú thích viết tay:** `Độ tham ăn 999/100: Thực đơn không từ một thứ gì`
* **Cảnh 2.3: Thẻ bài Tản nhiệt kỳ dị (01:48 – 02:05)**
  * **Tiêu đề trên màn hình:** `03. TUYỆT KỸ TẢN NHIỆT: 900/100`
  * **Hình vẽ:** Thẻ bài RPG khung băng tuyết, bồ nông ngửa cổ thở ra luồng khí mát lạnh.
  * **Lời thoại (Voice):** "Thứ ba là tuyệt kỹ Tản nhiệt cơ thể đạt chín trăm điểm! Không có tuyến mồ hôi như con người, loài chim này sở hữu một cơ chế làm mát bằng cổ họng kỳ dị bậc nhất giới tự nhiên mà chúng ta sẽ bóc trần ở phần sau."
  * **Chú thích viết tay:** `Tản nhiệt 900/100: Làm mát cơ thể qua màng cổ họng`
* **Cảnh 2.4: Thẻ bài Tốc độ thoát nước (02:05 – 02:25)**
  * **Tiêu đề trên màn hình:** `04. TỐC ĐỘ DỐC NƯỚC: 45/100`
  * **Hình vẽ:** Thẻ bài RPG có biểu tượng ốc sên, bồ nông đứng trĩu cổ trên tảng đá chờ nước chảy nhỏ giọt.
  * **Lời thoại (Voice):** "Nhưng điểm yếu chí mạng lại nằm ở chỉ số Tốc độ thoát nước chỉ vỏn vẹn bốn mươi lăm điểm! Xúc nước vào thì nhanh như chớp, nhưng để xả hết chỗ nước đó ra ngoài lại là một cực hình khiến nó gặp vô vàn rắc rối."
  * **Chú thích viết tay:** `Tốc độ dốc nước 45/100: Điểm yếu chí mạng khi đi săn`

#### CHƯƠNG 3: VŨ KHÍ GIẢI PHẪU & HẠM ĐỘI SĂN MỒI (02:25 – 04:15)
* **Cảnh 3.1: Mỏ dài kỷ lục và móc câu sừng (02:25 – 02:48)**
  * **Tiêu đề trên màn hình:** `01. MỎ DÀI KỶ LỤC 47 CM`
  * **Hình vẽ:** Bồ nông trắng Úc kẹp chặt con lươn trơn trượt bằng chiếc gai móc câu sắc nhọn ở đầu mỏ trên.
  * **Lời thoại (Voice):** "Để vận hành cỗ máy săn mồi này, bồ nông trắng Úc được trang bị chiếc mỏ dài tới bốn mươi bảy xăng-ti-mét — giữ kỷ lục chiếc mỏ dài nhất thế giới loài chim! Ngay ở chóp mỏ trên là một chiếc móc sừng nhọn hoắt quặp xuống như lưỡi câu cá, giúp nó khóa chặt những con mồi trơn tuột như cá trê hay lươn biển."
  * **Chú thích viết tay:** `Mỏ dài 47 cm kỷ lục thế giới kèm móc sừng nhọn`
* **Cảnh 3.2: Xương hàm dẻo như rổ bóng rổ (02:48 – 03:12)**
  * **Tiêu đề trên màn hình:** `02. XƯƠNG HÀM DẺO CỰC ĐẠI`
  * **Hình vẽ:** Kính lúp soi vào xương hàm dưới uốn cong sang hai bên như chiếc vành rổ bóng rổ đang hứng trọn đàn cá.
  * **Lời thoại (Voice):** "Bí mật thực sự nằm ở xương hàm dưới. Thay vì cứng nhắc như các loài chim khác, hàm dưới của bồ nông cấu tạo từ hai thanh xương sụn cực kỳ dẻo dai. Khi lao xuống nước, hai thanh xương này tự động uốn cong mở rộng sang hai bên, biến chiếc túi da thành một chiếc vợt bóng rổ khổng lồ cuốn trọn cả đàn cá!"
  * **Chú thích viết tay:** `Xương hàm dẻo uốn cong mở rộng thành lồng lưới xúc cá`
* **Cảnh 3.3: Mạng lưới mao mạch đàn hồi (03:12 – 03:35)**
  * **Tiêu đề trên màn hình:** `03. MẠNG LƯỚI MAO MẠCH ĐÀN HỒI`
  * **Hình vẽ:** Kính lúp soi cận cảnh mạng lưới mạch máu hình lò xo co giãn bên trong lớp da mỏ và xô nước số 13.
  * **Lời thoại (Voice):** "Nuôi dưỡng cho chiếc vợt da mỏng manh đó là một mạng lưới mao mạch máu chằng chịt có khả năng co giãn như lò xo. Khi túi mỏ căng phồng chứa tới mười ba lít nước cùng hàng chục con cá lớn quẫy đạp điên cuồng bên trong, các mạch máu này tự động giãn dài ra mà không hề bị đứt vỡ hay rách màng da."
  * **Chú thích viết tay:** `Mao mạch đàn hồi giữ túi mỏ chứa 13 lít nước không rách`
* **Cảnh 3.4: Hạm đội chữ V và Xe bán tải càn quét (03:35 – 04:15)**
  * **Tiêu đề trên màn hình:** `04. HẠM ĐỘI CHỮ V CÀN QUÉT`
  * **Hình vẽ:** Đàn bồ nông bơi đội hình chữ V đập cánh lùa cá vào bờ cạn, kết hợp cảnh bồ nông đeo kính râm lái xe bán tải gắn gầu xúc cá.
  * **Lời thoại (Voice):** "Không chỉ dựa vào vũ khí cá nhân, bồ nông trắng còn là bậc thầy tác chiến đồng đội. Chúng tập hợp thành hạm đội hình chữ V từ mười đến hai mươi con, đồng loạt đập cánh ầm ầm xuống mặt nước. Làn sóng âm dồn dập khiến đàn cá hoảng loạn tự chui đầu vào vùng nước cạn, nơi những chiếc gầu xúc sống đồng loạt càn quét chẳng khác nào một dàn xe bán tải gắn bồn chứa phóng qua dòng suối!"
  * **Chú thích viết tay:** `Đội hình chữ V đập cánh tạo sóng âm dồn cá vào bờ cạn`

#### CHƯƠNG 4: KHÔNG KÍCH TỪ ĐỘ CAO 20 MÉT & CÁCH NUÔI CON RÙNG RỢN (04:15 – 05:45) *(Chương mới hoàn toàn thay thế đoạn bị lặp)*
* **Cảnh 4.1: Cú lao mình thần phong từ độ cao 20 mét (04:15 – 04:45)**
  * **Tiêu đề trên màn hình:** `01. TÊN LỬA LAO TỪ ĐỘ CAO 20M`
  * **Hình vẽ:** Bồ nông nâu khép cánh hình mũi tên lao thẳng đứng từ bầu trời cao $20\text{ mét}$ cắm phập xuống mặt biển với tốc độ $65\text{ km/h}$ làm nước bắn tung tóe.
  * **Lời thoại (Voice):** "Nếu bồ nông trắng thích bơi lùa cá nhẹ nhàng, thì người anh em của nó là Bồ Nông Nâu lại chọn lối đánh của một quả tên lửa tầm nhiệt! Từ độ cao hai mươi mét trên bầu trời — tương đương tòa nhà sáu tầng — nó phát hiện đàn cá dưới biển nhờ thị lực xuyên thấu mặt nước, lập tức khép chặt cánh và bổ nhào thẳng đứng với vận tốc lên tới sáu mươi lăm ki-lô-mét một giờ!"
  * **Chú thích viết tay:** `Bồ nông nâu bổ nhào từ độ cao 20m với tốc độ 65 km/h`
  * **Prompt tạo ảnh Cảnh 4.1:** `A brown pelican diving straight down like a missile from the sky into the ocean water, speed lines, water splashing, 20 meters height indicator,魚 swimming below, Clean 2D comic cartoon illustration on pure solid white background, bold black ink outlines, vibrant flat colors, exaggerated funny cartoon facial expressions, no text, no letters, no watermark --ar 16:9`
* **Cảnh 4.2: Túi khí giảm chấn dưới da và kỹ thuật xoay cổ (04:45 – 05:15)** *(Điểm đặt Quảng cáo Mid-roll)*
  * **Tiêu đề trên màn hình:** `02. ÁO GIÁP TÚI KHÍ GIẢM CHẤN`
  * **Hình vẽ:** Giải phẫu ngực và cổ bồ nông có các túi đệm khí bơm phồng như túi khí ô tô bảo vệ xương ức khi đâm xuống mặt nước.
  * **Lời thoại (Voice):** "Ở tốc độ kinh hoàng đó, mặt nước cứng chẳng khác nào mặt đường bê tông! Để không bị gãy cổ hay vỡ ngực, ngay trước khoảnh khắc va chạm, bồ nông đồng thời xoay nhẹ cổ để bảo vệ khí quản và bơm căng hệ thống túi khí nằm ngay dưới lớp da ngực. Lớp đệm khí tự nhiên này hoạt động y hệt túi khí an toàn trên xe hơi, hấp thụ toàn bộ lực chấn động và làm choáng váng con cá bên dưới!"
  * **Chú thích viết tay:** `Hệ thống túi khí dưới da ngực giúp giảm chấn như túi khí ô tô`
  * **Prompt tạo ảnh Cảnh 4.2:** `Cross-section diagram of a pelican chest showing inflated air sacs like car airbags under its skin absorbing impact on water surface, magnifying glass view, Clean 2D comic cartoon illustration on pure solid white background, bold black ink outlines, vibrant flat colors, no text, no letters, no watermark --ar 16:9`
* **Cảnh 4.3: Cảnh nuôi con tưởng như... nuốt sống con ruột (05:15 – 05:45)**
  * **Tiêu đề trên màn hình:** `03. CHIM NON CHUI TỌT VÀO HỌNG MẸ`
  * **Hình vẽ:** Chú bồ nông con thò nguyên cả đầu và nửa thân mình chui tọt sâu vào trong cổ họng bồ nông mẹ để lục tìm cá, chỉ còn thò mỗi cái đuôi và hai chân ra ngoài vẫy đạp.
  * **Lời thoại (Voice):** "Không chỉ săn mồi bạo liệt, cách bồ nông cho con ăn cũng khiến người xem phải thót tim. Để lấy phần cá đã được tiêu hóa mềm, bồ nông con sẽ lao thẳng đầu, chui tọt gần như toàn bộ cơ thể vào sâu tận cổ họng của chim bố mẹ! Nhìn từ xa, ai cũng tưởng chim mẹ đang ăn thịt chính con ruột của mình, và sau mỗi bữa ăn kịch tính như vậy, chim non thường lăn ra bất tỉnh vài phút vì... kiệt sức!"
  * **Chú thích viết tay:** `Chim non chui cả người vào cổ họng bố mẹ để lấy thức ăn`
  * **Prompt tạo ảnh Cảnh 4.3:** `A funny baby pelican sticking its entire head and upper body deep inside the mother pelican open throat pouch to eat fish, only baby legs sticking out waving, comical shocked expression, Clean 2D comic cartoon illustration on pure solid white background, bold black ink outlines, vibrant flat colors, no text, no letters, no watermark --ar 16:9`

#### CHƯƠNG 5: NHỮNG PHA BI HÀI & GÓC KHUẤT SINH TỒN (05:45 – 07:40)
* **Cảnh 5.1: Màn ngáp bẻ cổ lộ cột sống như điều hòa 16 độ (05:45 – 06:15)**
  * **Tiêu đề trên màn hình:** `01. LỘN CỘT SỐNG ĐÓN GIÓ MÁT`
  * **Hình vẽ:** Du khách sở thú hốt hoảng nhìn bồ nông ngửa cổ đẩy cột sống trồi qua túi họng, kế bên là hình bồ nông nằm ghế bãi biển tận hưởng điều hòa $16^\circ\text{C}$.
  * **Lời thoại (Voice):** "Vào những trưa hè oi bức, nếu đi ngang qua sở thú và thấy một chú bồ nông đang ngửa cổ bẻ gập ra sau lưng, đẩy cả cột sống cổ trồi gồ lên xuyên qua lớp da mỏ mỏng manh, bạn đừng vội gọi bác sĩ thú y nhé! Đó chính là màn ngáp tản nhiệt độc nhất vô nhị: việc đẩy xương cổ ra ngoài giúp căng rộng tối đa diện tích màng túi họng, giúp máu giải nhiệt nhanh chóng chẳng khác nào đang ngồi trước chiếc điều hòa mười sáu độ!"
  * **Chú thích viết tay:** `Căng màng họng qua cột sống giúp hạ nhiệt như bật điều hòa`
* **Cảnh 5.2: Nín thở bằng miệng và Bi kịch 13 cân nước (06:15 – 06:48)**
  * **Tiêu đề trên màn hình:** `02. NÍN THỞ DỐC NƯỚC & BỊ CƯỚP MỒI`
  * **Hình vẽ:** Sơ đồ lỗ mũi bị tiêu biến phải thở bằng miệng, kết hợp cảnh bồ nông nặng trĩu mỏ bị mòng biển đậu thẳng lên đầu thò mỏ xuống cướp cá.
  * **Lời thoại (Voice):** "Thế nhưng chiếc túi mỏ khổng lồ cũng mang lại một bi kịch vật lý éo le. Một con bồ nông trưởng thành chỉ nặng khoảng mười một cân, nhưng lượng nước nó xúc vào mỏ lại nặng tới mười ba cân — tức là nặng hơn cả cơ thể nó! Đã thế, hai lỗ mũi ngoài của bồ nông đã tiêu biến hoàn toàn để tránh sặc nước, buộc nó phải thở bằng miệng. Vì vậy, sau mỗi cú xúc mồi, nó không thể bay lên mà phải đứng bất động, nín thở dốc nước suốt một phút đồng hồ — tạo cơ hội vàng cho lũ mòng biển ranh mãnh đậu thẳng lên đầu và thò cổ vào túi họng cướp sạch cá ngon!"
  * **Chú thích viết tay:** `Nín thở đứng đơ 1 phút dốc 13 cân nước, bị mòng biển cướp cá`
* **Cảnh 5.3: Vụ án nuốt bồ câu Luân Đôn & Các nạn nhân bi hài (06:48 – 07:15)**
  * **Tiêu đề trên màn hình:** `03. ÁC MỘNG CÔNG VIÊN LUÂN ĐÔN`
  * **Hình vẽ:** Cảnh bồ nông nuốt sống chim bồ câu trước mặt du khách ở công viên Luân Đôn và khung tranh 4 ô kẹp hươu sao, em nhỏ, mèo cưng.
  * **Lời thoại (Voice):** "Bị mòng biển bắt nạt trên biển là thế, nhưng khi lên bờ, bồ nông lại trở thành kẻ khủng bố thực sự. Tại công viên Hoàng gia Luân Đôn, hàng ngàn du khách từng chết lặng chứng kiến cảnh bồ nông tóm sống một chú chim bồ câu, dìm xuống hồ nước rồi ngửa cổ nuốt chửng nguyên con trong tiếng giãy giụa tuyệt vọng! Thậm chí, hươu sao con, bắp chân du khách hay những chú mèo cưng đang nằm ngủ cũng từng trở thành nạn nhân bị chiếc mỏ này kẹp thử và nhận lại một cú tát nhớ đời từ hoàng thượng mèo!"
  * **Chú thích viết tay:** `Nuốt sống bồ câu tại Luân Đôn và kẹp thử cả thú cưng`
* **Cảnh 5.4: Hiểm họa rách túi mỏ và Bàn tay bác sĩ thú y (07:15 – 07:40)**
  * **Tiêu đề trên màn hình:** `04. PHẪU THUẬT KHÂU TÚI MỎ`
  * **Hình vẽ:** Bác sĩ thú y đang tỉ mỉ khâu lại vết rách trên túi mỏ bồ nông bị lưỡi câu móc trúng, xung quanh là các trái tim.
  * **Lời thoại (Voice):** "Đáng thương thay, thói quen thấy gì cũng đớp lại đẩy loài chim sải cánh ba mét này vào nguy hiểm chết người trước rác thải của con người. Chỉ cần nuốt nhầm một chiếc lưỡi câu cá hay mảnh nhựa sắc nhọn làm rách thủng túi màng, thức ăn và nước sẽ trôi tuột ra ngoài khiến chúng chết đói. May mắn là ngày nay, các bác sĩ thú y đã thực hiện hàng trăm ca phẫu thuật khâu vá túi mỏ kỳ diệu, trả lại bầu trời tự do cho những gã khổng lồ tham ăn này."
  * **Chú thích viết tay:** `Bác sĩ thú y khâu lành túi mỏ bị rách do lưỡi câu và rác nhựa`

#### CHƯƠNG 6: BẮC CẦU SANG TẬP TIẾP THEO (07:40 – 08:03)
* **Cảnh 6.1: Teaser Gấu Nước Tardigrade (07:40 – 08:03)** *(Đã bỏ đoạn tổng kết dài dòng, đi thẳng vào mồi nhử tập 6)*
  * **Tiêu đề trên màn hình:** `TẬP TIẾP THEO: SINH VẬT BẤT TỬ`
  * **Hình vẽ:** Chú Gấu Nước Tardigrade mũm mĩm mặc bộ đồ phi hành gia giơ 2 ngón tay chữ V trôi nổi giữa vũ trụ đầy sao hỏa và thiên thạch.
  * **Lời thoại (Voice):** "Một con chim nuốt sống cả bồ câu nghe đã đủ điên rồ, nhưng vẫn chưa là gì so với kẻ dị biệt tiếp theo! Ở video ngay sau đây, chúng ta sẽ gặp gỡ sinh vật duy nhất trên Trái Đất sống sót qua năm cuộc đại tuyệt chủng, chịu được cả chân không vũ trụ lẫn bức xạ hạt nhân, nhưng lại có kết cục vô cùng lãng xẹt trước một con ốc sên: Gấu Nước Tardigrade!"
  * **Chú thích viết tay:** `Đón xem ngay: Gấu Nước Tardigrade — Sinh vật bất tử`

#### [GIỮ NGUYÊN OUTRO KÊNH: 08:04 – 08:13]

---

## PHẦN 3: KỊCH BẢN MỚI HOÀN TOÀN – TẬP 06: GẤU NƯỚC TARDIGRADE (VIDEO DÀI + SHORTS)

*(Đây là kịch bản tập tiếp theo khớp trực tiếp với lời hẹn ở cuối video Chim Bồ Nông của bạn để bạn sản xuất nối tiếp ngay lập tức).*

### 3.1. Kịch Bản Video Dài Tập 06: Gấu Nước Tardigrade (Thời lượng: $8\text{ phút } 30\text{ giây}$)
* **Tiêu đề YouTube gợi ý:** `Sinh Vật Bất Tử Duy Nhất Sống Sót Qua 5 Đại Tuyệt Chủng Nhưng Lại Sợ... Ốc Sên!`
* **Ý tưởng Thumbnail:** Gấu nước mặc giáp siêu nhân đứng cười giữa vụ nổ bom hạt nhân và ngoài vũ trụ, nhưng góc bên phải là một con ốc sên đang há miệng chuẩn bị nuốt gọn nó. Chữ to màu vàng: **`BẤT TỬ HỤT?!`**

#### [INTRO KÊNH: 00:00 – 00:09]

#### CHƯƠNG 1: KẺ CHẤP CẢ VŨ TRỤ NHƯNG LẠI CHẾT VÌ... ỐC SÊN (00:10 – 01:20)
* **Cảnh 1.1: Cú lừa của kẻ thống trị (00:10 – 00:35)**
  * **Tiêu đề trên màn hình:** `01. QUÁI VẬT 8 CHÂN SIÊU CẤP`
  * **Hình vẽ:** Một sinh vật 8 chân có móng vuốt sắc nhọn đang đứng hiên ngang giữa mưa thiên thạch và khủng long T-Rex đang la hét tuyệt chủng phía sau.
  * **Lời thoại (Voice):** "Hãy tưởng tượng một sinh vật đã chứng kiến loài khủng long ra đời rồi bị xóa sổ, cười khẩy bước qua năm cuộc đại tuyệt chủng đẫm máu nhất lịch sử Trái Đất, bị ném thẳng ra ngoài khoảng không vũ trụ không một giọt oxy mà vẫn sống nhăn răng! Bạn nghĩ đó là một con quái vật khổng lồ như Godzilla ư?"
  * **Chú thích viết tay:** `Sống sót qua 5 cuộc đại tuyệt chủng xóa sổ khủng long`
  * **Prompt tạo ảnh Cảnh 1.1:** `A cute chubby 8-legged tardigrade wearing superhero cape standing proudly while meteors fall and T-Rex dinosaurs panic in the background, Clean 2D comic cartoon illustration on pure solid white background, bold black ink outlines, vibrant flat colors, no text, no letters, no watermark --ar 16:9`
* **Cảnh 1.2: Phóng to kính hiển vi (00:35 – 01:00)**
  * **Tiêu đề trên màn hình:** `02. KÍCH THƯỚC 0.5 MI-LI-MÉT`
  * **Hình vẽ:** Bàn tay cầm kính lúp soi vào đám rêu xanh trên hòn đá, phóng to ra chú Gấu Nước béo múp míp đang bò lạch bạch như gấu bông, so sánh kích thước với dấu chấm câu trên trang giấy.
  * **Lời thoại (Voice):** "Thực tế, kẻ bất tử vĩ đại nhất hành tinh đó chỉ dài vỏn vẹn nửa mi-li-mét — tức là nhỏ ngang một dấu chấm câu trên trang giấy bạn đang nhìn! Với thân hình mũm mĩm tám chân ngắn cũn cỡn bò lạch bạch trên các đám rêu ẩm ướt, các nhà khoa học gọi chúng bằng cái tên vô cùng đáng yêu: Gấu Nước hay Heo Rêu!"
  * **Chú thích viết tay:** `Dài 0.5 mm: Nhỏ bằng dấu chấm câu, sống trong rêu ẩm`
  * **Prompt tạo ảnh Cảnh 1.2:** `A magnifying glass zooming into green moss on a rock revealing a chubby cute cartoon tardigrade walking like a bear, size comparison with a tiny period dot on paper, Clean 2D comic cartoon illustration on pure solid white background, bold black ink outlines, vibrant flat colors, no text, no letters, no watermark --ar 16:9`
* **Cảnh 1.3: Nghịch lý sinh tồn hài hước nhất (01:00 – 01:20)**
  * **Tiêu đề trên màn hình:** `03. NGHỊCH LÝ CỘNG ĐIỂM TIẾN HÓA`
  * **Hình vẽ:** Gấu nước đang gồng cơ bắp chống đỡ tia bức xạ và tảng băng khổng lồ, nhưng ngay bên cạnh là một con ốc sên đang trườn tới liếm gọn.
  * **Lời thoại (Voice):** "Điều bi hài nhất là Gấu Nước giống như một game thủ dồn toàn bộ điểm kỹ năng vào khả năng chống chịu thảm họa tận thế vũ trụ, nhưng lại... quên cộng điểm phòng thủ trước những kẻ thù đời thường nhất ngay dưới mặt đất!"
  * **Chú thích viết tay:** `Chống được tận thế vũ trụ nhưng bất lực trước kẻ thù mặt đất`

#### CHƯƠNG 2: BẢNG CHỈ SỐ BẤT TỬ RPG (01:20 – 02:35)
* **Cảnh 2.1: Kháng nhiệt độ cực hạn (01:20 – 01:40)**
  * **Tiêu đề trên màn hình:** `01. KHÁNG NHIỆT ĐỘ: 999/100`
  * **Hình vẽ:** Thẻ bài RPG chia làm nửa băng tuyết ($-272^\circ\text{C}$) và nửa dung nham sôi sục ($150^\circ\text{C}$), Gấu Nước ngồi uống trà sữa ở giữa.
  * **Lời thoại (Voice):** "Hãy nhìn vào bảng chỉ số sinh tồn vượt mọi định luật sinh học của Gấu Nước. Đầu tiên là chỉ số Kháng nhiệt độ đạt chín trăm chín mươi chín điểm! Nó có thể sống sót ở mức âm hai trăm bảy mươi hai độ C — tức là lạnh gần chạm ngưỡng độ không tuyệt đối của vũ trụ — và chịu được cả nồi nước sôi ở một trăm năm mươi độ C!"
  * **Chú thích viết tay:** `Sống sót từ mức lạnh -272 độ C đến nóng 150 độ C`
* **Cảnh 2.2: Kháng áp suất đáy vực sâu (01:40 – 01:58)**
  * **Tiêu đề trên màn hình:** `02. KHÁNG ÁP SUẤT: 999/100`
  * **Hình vẽ:** Thẻ bài RPG vẽ Gấu Nước đứng dưới đáy rãnh Mariana sâu nhất thế giới, trên lưng cõng chiếc tàu ngầm sắt đã bị ép bẹp dúm.
  * **Lời thoại (Voice):** "Thứ hai là chỉ số Kháng áp suất đạt mức tuyệt đối! Dù bị dìm xuống đáy rãnh đại dương sâu nhất hành tinh — nơi áp lực nước đủ sức bóp nát cả một chiếc tàu ngầm thép thành đống sắt vụn — Gấu Nước vẫn thản nhiên đi dạo với áp suất cao gấp sáu lần mức đó!"
  * **Chú thích viết tay:** `Chịu áp suất gấp 6 lần đáy vực Mariana sâu nhất biển`
* **Cảnh 2.3: Kháng bức xạ hạt nhân (01:58 – 02:16)**
  * **Tiêu đề trên màn hình:** `03. KHÁNG BỨC XẠ: 999/100`
  * **Hình vẽ:** Thẻ bài RPG có biểu tượng hạt nhân vàng đen, tia X và tia Gamma bắn vào Gấu Nước nhưng bật ngược ra ngoài.
  * **Lời thoại (Voice):** "Thứ ba là chỉ số Kháng phóng xạ! Trong khi con người sẽ tử vong ngay lập tức ở mức năm đơn vị phóng xạ, thì Gấu Nước có thể tắm mình trong liều lượng bức xạ cao gấp một ngàn lần mà vẫn sinh con đẻ cái bình thường!"
  * **Chú thích viết tay:** `Chịu bức xạ hạt nhân gấp 1.000 lần ngưỡng gây chết người`
* **Cảnh 2.4: Chỉ số tự vệ thực chiến (02:16 – 02:35)**
  * **Tiêu đề trên màn hình:** `04. PHÒNG THỦ THỰC CHIẾN: 01/100`
  * **Hình vẽ:** Thẻ bài RPG rạn nứt, Gấu Nước khóc ròng khi bị một con giun tròn nhỏ xíu rượt đuổi.
  * **Lời thoại (Voice):** "Thế nhưng, chỉ số Chiến đấu thực tế của vị thần bất tử này lại chỉ đạt... một trên một trăm điểm! Bất kỳ một sinh vật nhỏ bé nào trong đám rêu cũng có thể dễ dàng bắt nạt nó."
  * **Chú thích viết tay:** `Chiến đấu thực tế 1/100: Mềm yếu trước mọi kẻ săn mồi`

#### CHƯƠNG 3: TUYỆT KỸ HÓA THỦY TINH & KHIÊN CHẮN ADN (02:35 – 04:25)
* **Cảnh 3.1: Trạng thái ngủ đông "Tun" thu hồi 8 chân (02:35 – 03:05)**
  * **Tiêu đề trên màn hình:** `01. THUỒNG LUỒNG HÓA XÁC ƯỚP`
  * **Hình vẽ:** Quá trình Gấu Nước rút gọn 8 chân vào trong bụng, ép sạch $99\%$ nước ra khỏi cơ thể và cuộn tròn thành một viên nang khô quắt như hạt bụi.
  * **Lời thoại (Voice):** "Làm thế nào một cơ thể mềm nhũn lại làm được những điều phi thường đó? Bí quyết nằm ở tuyệt kỹ tự biến mình thành xác ướp sống! Khi phát hiện môi trường xung quanh bị khô hạn hoặc đóng băng, Gấu Nước lập tức rụt toàn bộ cái đầu và tám chiếc chân vào trong lớp vỏ, tự ép chín mươi chín phần trăm lượng nước ra khỏi cơ thể để cuộn tròn thành một chiếc thùng khô quắt!"
  * **Chú thích viết tay:** `Ép 99% nước khỏi cơ thể, cuộn tròn thành viên nang bất hoạt`
* **Cảnh 3.2: Biến tế bào thành thủy tinh sinh học (03:05 – 03:35)**
  * **Tiêu đề trên màn hình:** `02. HÓA THỦY TINH TẾ BÀO`
  * **Hình vẽ:** Kính lúp soi vào bên trong tế bào Gấu Nước: các phân tử protein đặc biệt kết tinh thành lớp kính thủy tinh trong suốt bọc kín bảo vệ các cơ quan nội tạng.
  * **Lời thoại (Voice):** "Thông thường, nếu tế bào mất hết nước, màng tế bào sẽ rách nát và sinh vật sẽ chết ngay lập tức. Nhưng Gấu Nước lại tiết ra một loại chất đạm đặc biệt chỉ riêng loài này mới có, tự động đông cứng lại thành một lớp thủy tinh sinh học bao bọc toàn bộ các cơ quan bên trong! Ở trạng thái hóa kính này, tốc độ trao đổi chất giảm xuống chỉ còn một phần mười ngàn so với bình thường — một ranh giới kỳ ảo nằm giữa sự sống và cái chết!"
  * **Chú thích viết tay:** `Tiết chất đạm biến nội tạng thành khối thủy tinh bất hoại`
* **Cảnh 3.3: Hồi sinh sau 30 năm chỉ với 1 giọt nước (03:35 – 04:00)**
  * **Tiêu đề trên màn hình:** `03. HỒI SINH SAU 30 NĂM ĐÓNG BĂNG`
  * **Hình vẽ:** Một giọt nước nhỏ xuống viên nang Gấu Nước đã bị đóng băng ở Nam Cực suốt $30\text{ năm}$, lập tức nó bung 8 chân tỉnh dậy vươn vai ngáp và đi kiếm ăn.
  * **Lời thoại (Voice):** "Đáng kinh ngạc hơn, các nhà khoa học Nhật Bản từng lấy một mẫu rêu bị đóng băng suốt ba mươi năm ròng rã ở Nam Cực về phòng thí nghiệm. Chỉ vài phút sau khi được nhỏ vào đúng một giọt nước ấm, lớp thủy tinh tan chảy, chú Gấu Nước từ từ duỗi tám chiếc chân, thức tỉnh sau giấc ngủ ba thập kỷ và đẻ ra mười chín quả trứng khỏe mạnh!"
  * **Chú thích viết tay:** `Chỉ cần 1 giọt nước để sống dậy sau 30 năm đóng băng`
* **Cảnh 3.4: Khiên chắn Protein bảo vệ chuỗi ADN (04:00 – 04:25)**
  * **Tiêu đề trên màn hình:** `04. KHIÊN CHẮN BỌC CHUỖI ADN`
  * **Hình vẽ:** Chuỗi xoắn kép ADN của Gấu Nước được các vệ sĩ mặc giáp ôm chặt che chắn khỏi các tia phóng xạ bắn tới, kèm bàn tay bác sĩ đang khâu nối lại sợi ADN bị đứt.
  * **Lời thoại (Voice):** "Chưa dừng lại ở đó, bên trong nhân tế bào của Gấu Nước còn có một loại protein hoạt động như tấm chăn chống đạn quấn chặt lấy chuỗi xoắn ADN. Ngay cả khi tia phóng xạ hạt nhân cực mạnh bắn đứt gãy ADN, hệ thống sửa chữa siêu tốc của nó sẽ lập tức khâu nối các đoạn mã di truyền lại nguyên vẹn như chưa từng có chuyện gì xảy ra!"
  * **Chú thích viết tay:** `Protein bọc kín và tự khâu nối chuỗi ADN bị tia xạ bắn đứt`

#### CHƯƠNG 4: CHuyến DU HÀNH VŨ TRỤ & VỤ ĐÂM TÀU LÊN MẶT TRĂNG (04:25 – 05:55)
* **Cảnh 4.1: Thí nghiệm phơi mình ngoài không gian năm 2007 (04:25 – 04:55)**
  * **Tiêu đề trên màn hình:** `01. 10 NGÀY PHƠI MÌNH NGOÀI VŨ TRỤ`
  * **Hình vẽ:** Tàu vũ trụ mở cửa khoang ngoài không gian, đẩy 3.000 chú Gấu Nước không mặc đồ bảo hộ ra phơi trực tiếp dưới tia cực tím Mặt Trời và chân không vũ trụ.
  * **Lời thoại (Voice):** "Để thử thách giới hạn cuối cùng của loài vật này, vào năm hai ngàn không trăm linh bảy, Cơ quan Vũ trụ Châu Âu đã đưa ba ngàn chú Gấu Nước lên vệ tinh và mở nắp đẩy thẳng chúng ra ngoài khoảng không vũ trụ! Không bình dưỡng khí, không đồ bảo hộ, chúng bị phơi trực tiếp trong môi trường chân không tuyệt đối và hứng trọn luồng tia cực tím tử thần từ Mặt Trời gấp một ngàn lần trên mặt đất suốt mười ngày liên tiếp!"
  * **Chú thích viết tay:** `Năm 2007: Sống sót sau 10 ngày phơi trần ngoài vũ trụ`
* **Cảnh 4.2: Sinh con sau chuyến đi bão táp (04:55 – 05:25)** *(Điểm đặt Quảng cáo Mid-roll)*
  * **Tiêu đề trên màn hình:** `02. ĐẺ TRỨNG NGAY TRÊN TÀU VŨ TRỤ`
  * **Hình vẽ:** Gấu Nước trở về Trái Đất được đeo huy chương phi hành gia, xung quanh là đàn Gấu Nước con vừa nở ra từ trứng.
  * **Lời thoại (Voice):** "Khi tàu vũ trụ quay trở về Trái Đất và được cấp nước trở lại, giới khoa học đã hoàn toàn chấn động: Hơn sáu mươi tám phần trăm số Gấu Nước đã tỉnh dậy khỏe mạnh! Không những thế, những cá thể cái còn đẻ trứng và nở ra thế hệ con cháu hoàn toàn bình thường, chính thức ghi danh Gấu Nước là loài động vật đầu tiên và duy nhất từng sống sót ngoài không gian vũ trụ!"
  * **Chú thích viết tay:** `68% sống sót trở về và sinh ra thế hệ con khỏe mạnh`
* **Cảnh 4.3: Cư dân định cư bất đắc dĩ trên Mặt Trăng năm 2019 (05:25 – 05:55)**
  * **Tiêu đề trên màn hình:** `03. RƠI XUỐNG MẶT TRĂNG NĂM 2019`
  * **Hình vẽ:** Tàu đổ bộ Beresheet đâm sầm xuống bề mặt Mặt Trăng năm 2019, làm văng chiếc hộp chứa hàng ngàn viên nang Gấu Nước đang nằm ngủ trên cát Mặt Trăng nhìn về Trái Đất.
  * **Lời thoại (Voice):** "Và rất có thể ngay lúc này, chúng đang nằm trên Mặt Trăng nhìn xuống chúng ta! Năm hai ngàn không trăm mười chín, tàu đổ bộ của Israel mang theo hàng ngàn chú Gấu Nước ở trạng thái ngủ đông đã gặp sự cố và đâm sầm xuống bề mặt Mặt Trăng. Với khả năng chịu áp suất và chân không vô địch, các nhà khoa học khẳng định những chiếc kén Gấu Nước này hoàn toàn nguyên vẹn sau cú va chạm, chờ đợi một ngày có người mang giọt nước lên đánh thức chúng dậy!"
  * **Chú thích viết tay:** `Hàng ngàn kén Gấu Nước đang nằm trên Mặt Trăng từ năm 2019`

#### CHƯƠNG 5: CÁI CHẾT LÃNG XẸT & CẤU TẠO CƠ THỂ DỊ BIỆT (05:55 – 07:40)
* **Cảnh 5.1: Cái chết lãng xẹt trong bụng Ốc Sên (05:55 – 06:25)**
  * **Tiêu đề trên màn hình:** `01. TỬ HUYỆT TRƯỚC MỘT CON ỐC SÊN`
  * **Hình vẽ:** Một con ốc sên bò ngang qua đám rêu, thè chiếc lưỡi sần sùi cuốn phăng cả đám Gấu Nước đang ngơ ngác vào bụng, kèm cảnh dịch vị dạ dày ốc sên tiêu hóa gọn.
  * **Lời thoại (Voice):** "Sống sót qua cả vũ trụ và bom hạt nhân là thế, nhưng cuộc đời thực tế của Gấu Nước dưới mặt đất lại là một chuỗi bi kịch đẫm nước mắt! Vì tuyệt kỹ hóa thủy tinh cần tới vài giờ đồng hồ để chuẩn bị và rút nước, nên khi một con ốc sên hay một con giun tròn bất ngờ trườn qua đám rêu và nuốt chửng nó, Gấu Nước hoàn toàn không kịp biến hình! Lớp vỏ mềm oặt của nó lập tức bị hàm răng của ốc sên nghiền nát, kết thúc cuộc đời kẻ bất tử một cách không thể lãng xẹt hơn!"
  * **Chú thích viết tay:** `Không kịp hóa kính khi bị ốc sên và giun tròn nuốt bất ngờ`
* **Cảnh 5.2: Thực đơn hút máu tế bào bằng giáo nhọn (06:25 – 06:55)**
  * **Tiêu đề trên màn hình:** `02. MIỆNG ỐNG HÚT BẮN GIÁO NHỌN`
  * **Hình vẽ:** Cận cảnh cái miệng tròn như ống hút trà sữa của Gấu Nước phóng ra hai chiếc kim nhọn đâm thủng tế bào rêu rồi hút rỗng dịch bên trong.
  * **Lời thoại (Voice):** "Tuy nhiên, đối với thế giới vi sinh vật nhỏ hơn mình, Gấu Nước cũng là một kẻ săn mồi đáng gờm. Chiếc miệng tròn xoe như cái vòi máy hút bụi của nó ẩn giấu hai chiếc gai nhọn hoắt như hai mũi giáo. Khi ăn, nó phóng hai mũi giáo này đâm thủng vách tế bào thực vật hoặc cơ thể những con trùng bánh xe nhỏ bé, rồi hút cạn kiệt toàn bộ chất dịch bên trong như uống một ly sinh tố!"
  * **Chú thích viết tay:** `Miệng giấu 2 gai nhọn đâm thủng tế bào và hút cạn dịch`
* **Cảnh 5.3: Cơ thể không tim, không phổi và cố định số lượng tế bào (06:55 – 07:20)**
  * **Tiêu đề trên màn hình:** `03. CƠ THỂ KHÔNG TIM KHÔNG PHỔI`
  * **Hình vẽ:** Giải phẫu trong suốt của Gấu Nước không có tim và phổi, chỉ có chất dịch chảy quanh bụng và các tế bào phình to lên như bơm bóng thay vì phân chia.
  * **Lời thoại (Voice):** "Một bí mật giải phẫu kỳ lạ nữa là Gấu Nước hoàn toàn không có tim, không có mạch máu và cũng chẳng có phổi! Toàn bộ khoang bụng của nó là một túi dịch lỏng tự đảo trộn theo từng bước chân lạch bạch để vận chuyển oxy và thức ăn. Thậm chí từ lúc mới nở ra cho đến khi già đi, số lượng tế bào trên cơ thể một chú Gấu Nước là cố định không đổi — nó lớn lên không phải bằng cách nhân đôi tế bào, mà bằng cách bơm cho từng tế bào phình to ra!"
  * **Chú thích viết tay:** `Không tim phổi, lớn lên bằng cách làm phình to từng tế bào`
* **Cảnh 5.4: Chìa khóa y học bảo quản vắc-xin cho nhân loại (07:20 – 07:40)**
  * **Tiêu đề trên màn hình:** `04. CHÌA KHÓA Y HỌC TƯƠNG LAI`
  * **Hình vẽ:** Các nhà khoa học đang chiết xuất chất đạm hóa kính từ Gấu Nước để bảo quản lọ vắc-xin và giúp phi hành gia chống bức xạ khi bay tới Sao Hỏa.
  * **Lời thoại (Voice):** "Ngày nay, giới y học đang ráo riết giải mã công thức chất đạm hóa thủy tinh của Gấu Nước. Nếu thành công, nhân loại có thể bảo quản vắc-xin và máu khô ở nhiệt độ thường mà không cần tủ đông lạnh, thậm chí tạo ra thuốc chống phóng xạ giúp con người chinh phục Sao Hỏa trong tương lai!"
  * **Chú thích viết tay:** `Ứng dụng bảo quản vắc-xin không cần tủ lạnh và chống bức xạ`

#### CHƯƠNG 6: BẮC CẦU SANG TẬP 07 (07:40 – 08:03)
* **Cảnh 6.1: Teaser Tôm Tít / Tôm Búa Mantis Shrimp (07:40 – 08:03)**
  * **Tiêu đề trên màn hình:** `TẬP TIẾP THEO: CÚ ĐẤM NÓNG NGANG MẶT TRỜI`
  * **Hình vẽ:** Chú Tôm Tít (Mantis Shrimp) màu sắc rực rỡ đeo găng tay quyền anh tung cú đấm tạo ra quả cầu lửa dưới nước làm vỡ toang tấm kính bể cá dày.
  * **Lời thoại (Voice):** "Nếu Gấu Nước là tấm khiên phòng thủ tuyệt đối của tự nhiên, thì ở video ngay sau đây, chúng ta sẽ chạm trán ngọn giáo tấn công khủng khiếp nhất đại dương! Một võ sĩ quyền anh chỉ dài bằng bàn tay nhưng tung ra cú đấm nhanh ngang đạn súng trường, làm nước biển bốc sôi tạo ra nhiệt độ nóng ngang bề mặt Mặt Trời và đấm vỡ toang cả kính cường lực: Tôm Tít Mantis Shrimp!"
  * **Chú thích viết tay:** `Đón xem ngay: Tôm Tít — Võ sĩ có cú đấm nóng ngang Mặt Trời`

#### [OUTRO KÊNH: 08:04 – 08:13]

---

### 3.2. Kịch Bản YouTube Shorts Tập 06: Gấu Nước Tardigrade ($46\text{ giây}$ – Áp dụng Vòng Lặp Seamless Loop)
* **Thanh tiêu đề cố định trên cùng (`200–380 px`):** `KẺ BẤT TỬ CHẾT LÃNG XẸT VÌ... ỐC SÊN!`
* **0:00 – 0:05 (Hook nối vòng lặp & Cú sốc đầu tiên):**
  * **Hình vẽ (Sân khấu giữa màn hình):** Gấu Nước đeo kính râm ngồi uống nước dừa giữa vụ nổ hạt nhân và không gian vũ trụ.
  * **Voice:** *"...sẽ tiêu đời ngay lập tức! Dù đây là sinh vật duy nhất trên Trái Đất sống sót qua cả năm cuộc đại tuyệt chủng từng xóa sổ loài khủng long!"*
* **0:05 – 0:16 (Đẩy chỉ số điên rồ):**
  * **Hình vẽ:** Gấu Nước dài $0.5\text{ mm}$ đứng cạnh dấu chấm câu, bị đóng băng ở $-272^\circ\text{C}$, luộc sôi ở $150^\circ\text{C}$ và phơi ngoài vũ trụ $10\text{ ngày}$.
  * **Voice:** *"Chỉ dài nửa mi-li-mét bằng một dấu chấm câu, nhưng Gấu Nước chịu được cái lạnh âm hai trăm bảy mươi hai độ C, nước sôi một trăm năm mươi độ, và từng bị ném trần trụi ra ngoài vũ trụ suốt mười ngày mà vẫn về Trái Đất đẻ con bình thường!"*
* **0:16 – 0:28 (Giải thích cơ chế hóa kính):**
  * **Hình vẽ:** Gấu Nước rụt $8\text{ chân}$, ép $99\%$ nước ra ngoài và biến nội tạng thành khối thủy tinh lấp lánh, ngủ đông $30\text{ năm}$.
  * **Voice:** *"Bí mật nằm ở tuyệt kỹ rút chín mươi chín phần trăm nước khỏi cơ thể và tiết chất đạm biến nội tạng thành một khối thủy tinh bất hoại! Chỉ cần nhỏ một giọt nước, nó lập tức sống dậy sau ba mươi năm đóng băng!"*
* **0:28 – 0:39 (Cú bẻ lái hài hước nhất):**
  * **Hình vẽ:** Con ốc sên trườn qua đám rêu, thè lưỡi nuốt chửng chú Gấu Nước đang cuống cuồng chưa kịp biến hình.
  * **Voice:** *"Thế nhưng, vì quá trình hóa thủy tinh mất tới vài tiếng đồng hồ để chuẩn bị, nên khi một con ốc sên bất ngờ bò qua đám rêu và nuốt gọn, vị thần bất tử này hoàn toàn không kịp biến hình!"*
* **0:39 – 0:46 (Đẩy sang Video dài + Khóa vòng lặp Seamless Loop):**
  * **Hình vẽ:** Mũi tên chỉ xuống mục **Video có liên quan** bên dưới, chuyển nhanh sang cảnh Gấu Nước đứng trước miệng ốc sên khổng lồ.
  * **Voice:** *"Bí ẩn về hàng ngàn chú Gấu Nước đang nằm trên Mặt Trăng đã có ở video dài bên dưới kênh. Nên nhớ, dù bất tử ngoài vũ trụ nhưng nếu gặp một con ốc sên, nó..."*
  * *(Nối khớp hoàn hảo về giây `0:00`: **"...nếu gặp một con ốc sên, nó / sẽ tiêu đời ngay lập tức!"**).*

---

## PHẦN 4: LỘ TRÌNH 30 NGÀY SẢN XUẤT CHI TIẾT (CHUẨN HÓA 60 TẬP LẺ + 60 SHORTS + TẬP 61 ĐẶC BIỆT)

* **Tần suất xuất bản:** $2\text{ Ca/ngày}$ — **Ca 1 (11:30 Trưa)** và **Ca 2 (18:00 Tối)**.
* **Tiêu chuẩn kỹ thuật bắt buộc cho mọi tập:**
  * **Video Dài:** Thời lượng $8 - 10\text{ phút}$ (Tối thiểu $> 8\text{ phút } 05\text{ giây}$ để bật quảng cáo Mid-roll), độ phân giải $1080\text{p}$ ($1920 \times 1080\text{ px}$), $60\text{fps}$, âm thanh Stereo $48\text{kHz}$.
  * **Video Shorts:** Thời lượng $45 - 58\text{ giây}$, tỷ lệ dọc $9:16$ ($1080 \times 1920\text{ px}$), $60\text{fps}$, áp dụng cấu trúc 1 tranh trung tâm + kể trọn vẹn (TASTE-66), gắn liên kết trực tiếp về Video dài cùng ca.

### TUẦN 1: NHỮNG "KẺ LỪA ĐẢO" & DỊ NHÂN CỦA TỰ NHIÊN (NGÀY 1 – NGÀY 7)

| Ngày & Ca Đăng | Tập & Chủ Đề Con Vật | Tiêu Đề Video Dài & Góc Khai Thác Chuyên Sâu | Kịch Bản Shorts Đi Kèm (Động Cơ Kéo View) | Thời Lượng & Chất Lượng Yêu Cầu |
| :--- | :--- | :--- | :--- | :--- |
| **Ngày 1 - Ca 1 (11:30)** | **Tập 01: Lửng Mật (Honey Badger)** | **Tại Sao Cả Sư Tử Cũng Không Dám Đụng Vào Kẻ Chí Phèo Này?**<br>Da dày $6\text{ mm}$ xoay $180^\circ$ trong da, kháng nọc rắn hổ mang, giai thoại vượt ngục của Stoffel. | **Shorts 01:** Cú ngủ gật 2 tiếng sau khi bị rắn hổ mang chúa cắn rồi dậy ăn tiếp con rắn. | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 1 - Ca 2 (18:00)** | **Tập 02: Rái Cá Biển (Sea Otter)** | **Đừng Để Vẻ Đáng Yêu Này Lừa Bạn: Bộ Mặt Thật Của Rái Cá!**<br>Bộ lông dày nhất thế giới ($150.000\text{ sợi/cm}^2$), túi nách giấu đá, góc khuất bắt cóc con non đòi tiền chuộc bằng thức ăn. | **Shorts 02:** Tại sao Rái Cá nắm tay nhau ngủ dễ thương nhưng lại là "tội phạm" đáng sợ dưới biển? | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 2 - Ca 1 (11:30)** | **Tập 03: Cá Heo (Dolphin)** | **Sự Thật Đen Tối Về Cá Heo Mà Phim Hoạt Hình Đã Giấu Bạn**<br>Ngủ mở một mắt với nửa bộ não, bắt nạt cá mập, chuyền cá nóc cho nhau để giải trí bằng độc tố nhẹ. | **Shorts 03:** Trò chơi bóng chuyền bằng... cá nóc độc của hội thanh niên Cá Heo đại dương. | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 2 - Ca 2 (18:00)** | **Tập 04: Thú Mỏ Vịt (Platypus)** | **Khi Thượng Đế Nhặt Đồ Thừa Tạo Ra Một Loài Vật: Thú Mỏ Vịt!**<br>Mỏ vịt dò điện trường, đẻ trứng nhưng tiết sữa qua da như đổ mồ hôi, không có dạ dày, cựa chân sau chứa độc tố. | **Shorts 04:** Loài thú kỳ dị không có núm vú, nuôi con bằng cách... đổ mồ hôi sữa ra bụng! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 3 - Ca 1 (11:30)** | **Tập 05: Chim Bồ Nông (Pelican)** | **Loài Chim Cứ Thấy Thứ Gì Chuyển Động Là Cố Nuốt Chửng!**<br>Túi mỏ $13\text{ lít}$, phản xạ thị giác kẹp Capybara, bổ nhào từ độ cao $20\text{m}$, ngáp lộn cột sống tản nhiệt. | **Shorts 05:** Luật rừng của Bồ Nông: Từ Capybara đến Flycam, cứ vừa mồm là nuốt thử! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 3 - Ca 2 (18:00)** | **Tập 06: Gấu Nước (Tardigrade)** | **Sinh Vật Bất Tử Duy Nhất Sống Sót Qua 5 Đại Tuyệt Chủng**<br>Hóa thủy tinh nội tạng, sống ngoài vũ trụ, định cư trên Mặt Trăng nhưng bị ốc sên nuốt gọn. | **Shorts 06:** Chấp cả bom hạt nhân và vũ trụ nhưng vị thần bất tử này lại chết lãng xẹt vì... ốc sên! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 4 - Ca 1 (11:30)** | **Tập 07: Tôm Tít (Mantis Shrimp)** | **Võ Sĩ Quyền Anh Dưới Đáy Biển Có Cú Đấm Nóng Ngang Mặt Trời**<br>Cơ chế lò xo tung cú đấm vận tốc $80\text{ km/h}$ tạo bong bóng siêu nhiệt $4.700^\circ\text{C}$, mắt nhìn thấy 16 thụ thể màu. | **Shorts 07:** Tại sao các thủy cung không dám nhốt loài tôm này vào bể kính thông thường? | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 4 - Ca 2 (18:00)** | **Tập 08: Chồn Gulo (Wolverine)** | **Kẻ Điên Phương Bắc Dám Cướp Mồi Của Cả Đàn Sói Và Gấu Xám!**<br>Chỉ nặng $15\text{ kg}$ nhưng sở hữu chiếc răng hàm carnassial xoay $90^\circ$ nghiền nát xương đông lạnh ở $-50^\circ\text{C}$, chân cấu trúc ủng trượt tuyết lướt tuyết mềm, tuyến xạ Skunk Bear cướp mồi Gấu Xám $300\text{ kg}$, sức bền chạy $70\text{ km/ngày}$. | **Shorts 08:** Nặng vỏn vẹn 15kg đuổi cả Gấu Xám 300kg khỏi bữa ăn! Răng hàm xoay 90 độ bẻ xương đông lạnh, xịt xạ hôi kinh hoàng đuổi cả bầy sói! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 5 - Ca 1 (11:30)** | **Tập 09: Chim Cánh Cụt (Penguin)** | **Đằng Sau Dáng Đi Lạch Bạch Là Những Giao Dịch Đen Tối Ở Nam Cực**<br>Trao đổi sỏi làm tổ, đẩy đồng loại xuống nước thử xem có hải cẩu báo không, khả năng bắn phân xa hàng mét. | **Shorts 09:** Màn "đẩy bạn xuống nước dò mìn" vô tình nhất thế giới động vật của Chim Cánh Cụt. | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 5 - Ca 2 (18:00)** | **Tập 10: Gấu Koala (Koala)** | **Bộ Não Phẳng Lì & Thực Đơn Ăn Lá Độc Kỳ Quặc Nhất Thế Giới**<br>Não nhẵn bóng chiếm $0.2\%$ cơ thể, ngủ $20\text{ tiếng/ngày}$ vì ăn lá khuynh diệp độc, con non ăn phân mẹ để lấy vi khuẩn tiêu hóa. | **Shorts 10:** Điều gì xảy ra nếu bạn hái lá khuynh diệp để lên đĩa bày trước mặt một con Koala? (Nó không nhận ra đồ ăn!). | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 6 - Ca 1 (11:30)** | **Tập 11: Gấu Trúc Lớn (Giant Panda)** | **Kẻ Phản Bội Tổ Tiên Ăn Thịt Để Nhai Tre Suốt 14 Tiếng Mỗi Ngày**<br>Hệ tiêu hóa của thú ăn thịt nhưng lại ăn tre trúc nghèo dinh dưỡng, đi vệ sinh $40\text{ lần/ngày}$, những pha lăn lộn ngớ ngẩn. | **Shorts 11:** Tại sao Gấu Trúc chưa bị tuyệt chủng dù lười giao phối và ngã cây suốt ngày? | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 6 - Ca 2 (18:00)** | **Tập 12: Hà Mã (Hippopotamus)** | **Đừng Nhìn Thân Hình Béo Tròn Mà Nhầm: Cỗ Xe Tăng Hung Hãn Nhất Châu Phi!**<br>Lực cắn $1.800\text{ PSI}$ bẻ đôi cá sấu, không biết bơi mà chạy bộ dưới đáy sông, quay đuôi quạt phân đánh dấu lãnh thổ. | **Shorts 12:** Hà Mã thực chất không hề biết bơi! Vậy chúng di chuyển dưới sông bằng cách nào? | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 7 - Ca 1 (11:30)** | **Tập 13: Con Lười (Sloth)** | **Sinh Vật Sống Chậm Đến Mức Mọc Cả Rêu Xanh Trên Lưng & Tử Huyệt Khi Đi Vệ Sinh**<br>Tốc độ di chuyển $0.2\text{ km/h}$, hệ sinh thái bướm đêm sống trên lông, giảm $1/3$ trọng lượng cơ thể trong 1 lần đi vệ sinh. | **Shorts 13:** Tại sao hơn một nửa số cái chết của loài Lười đều xảy ra... đúng lúc chúng xuống đất đi vệ sinh? | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 7 - Ca 2 (18:00)** | **Tập 14: Chim Tu Hú (Cuckoo)** | **Kẻ Ăn Chực Tàn Nhẫn Nhất Tự Nhiên: Đẻ Trứng Nhờ Và Án Mạng Ngay Khi Vừa Nở**<br>Ngụy trang màu trứng giống hệt chủ nhà, chim non vừa nở chưa mở mắt đã dùng lưng đẩy hết trứng chủ nhà rơi khỏi tổ. | **Shorts 14:** Bản năng sát thủ của chim Tu Hú non ngay giây phút đầu tiên chui ra khỏi vỏ trứng! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |

---

### TUẦN 2: VŨ KHÍ SINH HỌC ĐIÊN RỒ & SIÊU NĂNG LỰC (NGÀY 8 – NGÀY 14)

| Ngày & Ca Đăng | Tập & Chủ Đề Con Vật | Tiêu Đề Video Dài & Góc Khai Thác Chuyên Sâu | Kịch Bản Shorts Đi Kèm (Động Cơ Kéo View) | Thời Lượng & Chất Lượng Yêu Cầu |
| :--- | :--- | :--- | :--- | :--- |
| **Ngày 8 - Ca 1 (11:30)** | **Tập 15: Chuột Lang Nước (Capybara)** | **Bộ Trưởng Bộ Ngoại Giao Tự Nhiên: Tại Sao Cả Cá Sấu Cũng Nằm Phơi Nắng Cùng Nó?**<br>Tuyến mùi hương thân thiện, tính cách điềm tĩnh vô cực, tập tính ăn lại phân của chính mình vào buổi sáng để hấp thụ protein. | **Shorts 15:** Bí mật đằng sau vẻ mặt "tĩnh tâm trước mọi biến cố" của Capybara trước hàm cá sấu. | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 8 - Ca 2 (18:00)** | **Tập 16: Tôm Súng (Pistol Shrimp)** | **Tay Súng Cao Bồi Đại Dương: Một Cú Búng Càng Làm Cá Chết Đứng Từ Xa!**<br>Càng kẹp tạo luồng nước siêu thanh $218\text{ dB}$ (lớn hơn tiếng súng), sóng xung kích đánh ngất con mồi mà không cần chạm vào. | **Shorts 16:** Cú búng tay tạo ra ánh sáng và tiếng nổ làm nhiễu sóng cả tàu ngầm quân sự của Tôm Súng! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 9 - Ca 1 (11:30)** | **Tập 17: Lươn Điện (Electric Eel)** | **Trạm Phát Điện Sống 860 Vôn: Giật Ngất Cả Cá Sấu Lẫn Ngựa Trưởng Thành!**<br>$80\%$ cơ thể là tế bào phát điện xếp như pin nối tiếp, cơ chế nhảy khỏi mặt nước dí cằm vào kẻ thù để tăng gấp đôi dòng điện. | **Shorts 17:** Tại sao Lươn Điện phóng ra dòng điện 860 Vôn giết chết cá sấu nhưng chính nó lại không bị điện giật? | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 9 - Ca 2 (18:00)** | **Tập 18: Bọ Pháo Thủ (Bombardier Beetle)** | **Khẩu Pháo Hóa Học Biết Đi: Bắn Dung Dịch Sôi 100 Độ C Vào Mặt Kẻ Thù!**<br>Hai buồng chứa hóa chất trong bụng trộn lẫn tạo phản ứng nổ liên thanh $500\text{ lần/giây}$, thoát chết ngay cả khi bị cóc nuốt vào bụng. | **Shorts 18:** Bị cóc nuốt chửng vào dạ dày suốt 1 tiếng, con bọ này đã làm gì khiến con cóc phải nôn thốc tháo? | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 10 - Ca 1 (11:30)** | **Tập 19: Thằn Lằn Quỷ Gai (Thorny Devil)** | **Quái Vật Sa Mạc Uống Nước Bằng... Chân Và Chiêu Phun Máu Từ Mắt!**<br>Hệ thống rãnh mao dẫn trên da hút sương sớm từ bàn chân chạy ngược lên miệng, chiếc đầu giả sau gáy và tia máu bắn từ hốc mắt. | **Shorts 19:** Tuyệt kỹ bắn tia máu độc thẳng từ khóe mắt xa hơn 1 mét làm sói đồng cỏ khiếp vía! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 10 - Ca 2 (18:00)** | **Tập 20: Cá Mang Rổ / Cá Cung Thủ (Archerfish)** | **Xạ Thủ Bắn Tỉa Dưới Nước: Hạ Gục Côn Trùng Trên Cành Cây Không Trượt Phát Nào!**<br>Khả năng tính toán góc khúc xạ ánh sáng qua mặt nước, phun tia nước áp lực cao hạ mục tiêu cách $3\text{ mét}$ chỉ trong $0.1\text{ giây}$. | **Shorts 20:** Làm sao một con cá dưới nước giải được bài toán vật lý khúc xạ ánh sáng để bắn rụng côn trùng? | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 11 - Ca 1 (11:30)** | **Tập 21: Cóc Sừng (Frogmouth / Horned Frog) & Ếch Lông (Hairy Frog)** | **Người Sói Của Thế Giới Lưỡng Cư: Tự Bẻ Gãy Xương Ngón Tay Đâm Xuyên Da Làm Vũ Khí!**<br>Khi bị tấn công, Ếch Lông tự co cơ bẻ gãy xương ngón chân đâm thủng lớp đệm thịt ra ngoài thành móng vuốt sắc nhọn như Wolverine. | **Shorts 21:** Loài ếch điên rồ tự bẻ gãy xương của chính mình đâm xuyên qua da để tạo móng vuốt chiến đấu! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 11 - Ca 2 (18:00)** | **Tập 22: Kỳ Nhông Axolotl (Khủng Long Sáu Sừng)** | **Đỉnh Cao Tái Tạo Của Tự Nhiên: Đứt Chân, Mất Tim Hay Tổn Thương Não Đều Mọc Lại Mới Tinh!**<br>Trạng thái trẻ mãi không già (Neoteny), khả năng mọc lại chi, tủy sống, thùy não mà không để lại sẹo, ghép tạng của con khác vào vẫn sống. | **Shorts 22:** Chuyện gì xảy ra khi một con Axolotl bị mất đi một phần trái tim hoặc não bộ? | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 12 - Ca 1 (11:30)** | **Tập 23: Hải Sâm (Sea Cucumber)** | **Vũ Khí Phòng Thủ Kinh Dị Nhất Đại Dương: Bắn Toàn Bộ Ruột Gan Qua Hậu Môn Vào Mặt Kẻ Thù!**<br>Hóa lỏng cơ thể chui qua khe đá hẹp, tự phóng nội tạng dính chặt và chứa độc tố làm ngạt thở cua/cá rồi mọc lại ruột mới sau vài tuần. | **Shorts 23:** Khi bị kẻ thù dồn vào chân tường, Hải Sâm chọn cách... bắn thẳng bộ ruột qua đường hậu môn! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 12 - Ca 2 (18:00)** | **Tập 24: Cá Mút Đá & Cá Mập Ngủ (Hagfish)** | **Cỗ Máy Tạo Chất Nhầy Kinh Hoàng: Biến 20 Lít Nước Biển Thành Đống Keo Đặc Quánh Trong 1 Giây!**<br>Hộp sọ không có xương hàm, chui vào con mồi ăn từ trong ra ngoài, tiết sợi protein làm tắc nghẽn mang của cá mập ngay tức khắc. | **Shorts 24:** Cảnh tượng chiếc xe chở Cá Mút Đá bị lật biến cả đoạn đường cao tốc thành biển chất nhầy! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 13 - Ca 1 (11:30)** | **Tập 25: Bạch Tuộc Bắt Chước (Mimic Octopus)** | **Bậc Thầy Cosplay Đại Dương: Biến Hình Thành 15 Loài Vật Độc Khác Nhau Trong Chớp Mắt!**<br>Sở hữu 9 bộ não và 3 trái tim, máu màu xanh lam, tự đổi màu sắc và uốn các xúc tu giả làm rắn biển, cá sư tử hoặc cá bơn độc. | **Shorts 25:** Khi gặp kẻ thù của rắn biển, Bạch Tuộc lập tức xếp 6 chân lại và biến 2 chân còn lại thành... một con rắn biển! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 13 - Ca 2 (18:00)** | **Tập 26: Gấu Túi Wombat** | **Kiến Trúc Sư Hầm Ngầm Có Cặp Mông Bọc Thép Và Tuyệt Kỹ Đi Vệ Sinh Hình... Khối Lập Phương!**<br>Tấm sụn mông cứng như khiên sắt dùng để ép nát hộp sọ cáo/chó hoang vào trần hang, ruột co bóp không đều đúc phân thành hình vuông. | **Shorts 26:** Sinh vật duy nhất trên thế giới đi vệ sinh ra những viên phân hình vuông vức như viên xúc xắc! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 14 - Ca 1 (11:30)** | **Tập 27: Chuộtũi Sao (Star-nosed Mole)** | **Kẻ Săn Mồi Nhanh Nhất Hành Tinh: Xác Định Và Nuốt Gọn Con Mồi Chỉ Trong 0.12 Giây!**<br>Chiếc mũi gồm 22 xúc tu thịt chứa $25.000\text{ thụ thể cảm giác}$, khả năng thổi bong bóng khí dưới nước rồi hít lại để "ngửi mùi" dưới đáy bùn. | **Shorts 27:** Chiếc mũi kỳ dị như quái vật ngoài hành tinh giúp loài chuột này ăn hết bữa tối trước khi bạn kịp chớp mắt! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 14 - Ca 2 (18:00)** | **Tập 28: Kiến Nổ (Exploding Ant) & Kiến Đạn (Bullet Ant)** | **Đội Quân Cảm Tử Rừng Nhiệt Đới: Tự Kích Nổ Vỡ Tung Cơ Thể Để Phun Keo Độc Dính Chết Kẻ Thù!**<br>Kiến thợ co cơ bụng cực mạnh làm nổ tung thành bụng phun dịch keo vàng độc hại khóa chặt đối phương, và vết đốt đau nhất hành tinh của Kiến Đạn. | **Shorts 28:** Những chiến binh kiến sẵn sàng tự cho nổ tung cơ thể mình như bom cảm tử để bảo vệ tổ! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |

---

### TUẦN 3: BẬC THẦY SINH TỒN & KIẾN TRÚC SƯ ĐỈNH CAO (NGÀY 15 – NGÀY 21)

| Ngày & Ca Đăng | Tập & Chủ Đề Con Vật | Tiêu Đề Video Dài & Góc Khai Thác Chuyên Sâu | Kịch Bản Shorts Đi Kèm (Động Cơ Kéo View) | Thời Lượng & Chất Lượng Yêu Cầu |
| :--- | :--- | :--- | :--- | :--- |
| **Ngày 15 - Ca 1 (11:30)** | **Tập 29: Sứa Bất Tử (Turritopsis dohrnii)** | **Sinh Vật Duy Nhất Đảo Ngược Thời Gian: Già Rồi Lại Tự Biến Ngược Về Thời Sơ Sinh!**<br>Cơ chế chuyển hóa tế bào (Transdifferentiation): khi già yếu hoặc bị thương, sứa chìm xuống đáy biển hóa thành khối polyp và phân tách thành hàng trăm bản sao trẻ sơ sinh. | **Shorts 29:** Hãy tưởng tượng một ông lão 80 tuổi bỗng nhiên biến ngược thành em bé sơ sinh rồi sống lại từ đầu — loài sứa này làm điều đó mỗi ngày! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 15 - Ca 2 (18:00)** | **Tập 30: Hải Ly (Beaver)** | **Kỹ Sư Thủy Lợi Điên Cuồng: Bị Ám Ảnh Bởi Tiếng Nước Chảy Và Con Đập Nhìn Thấy Từ Vũ Trụ!**<br>Răng cửa chứa sắt màu cam tự mài sắc khi cạp gỗ, thí nghiệm bật loa tiếng nước chảy khiến Hải Ly đắp bùn kín cái loa, đập dài $850\text{m}$. | **Shorts 30:** Điều gì xảy ra khi các nhà khoa học đặt một chiếc loa phát tiếng nước chảy trước mặt một con Hải Ly? | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 16 - Ca 1 (11:30)** | **Tập 31: Chim Cắt Lớn (Peregrine Falcon)** | **Tên Lửa Sinh Học Nhanh Nhất Hành Tinh: Bổ Nhào Với Tốc Độ 389 Km/h Xé Toạc Bầu Trời!**<br>Cấu trúc mấu xương hình nón trong lỗ mũi giảm áp suất không khí như động cơ phản lực máy bay siêu thanh, màng nháy mắt thứ 3 làm kính bảo hộ. | **Shorts 31:** Tại sao phổi của Chim Cắt không bị nổ tung khi lao xuống với tốc độ gần 400 km/h? | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 16 - Ca 2 (18:00)** | **Tập 32: Chuột Chũi Trũi Không Lông (Naked Mole-Rat)** | **Sinh Vật Không Biết Đau, Không Bị Ung Thư Và Sống Được 18 Phút Không Cần Oxy!**<br>Chuyển sang hô hấp bằng đường Fructose như thực vật khi hết oxy, miễn nhiễm axit và chất cay, xã hội phân chia giai cấp Nữ hoàng như loài ong. | **Shorts 32:** Bí mật giúp loài chuột xấu xí nhất hành tinh miễn nhiễm hoàn toàn với bệnh ung thư và sống thọ hơn 30 năm! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 17 - Ca 1 (11:30)** | **Tập 33: Ếch Gỗ Bắc Cực (Wood Frog)** | **Đông Đá Cứng Đơ Như Viên Đá Lạnh Suốt Mùa Đông Rồi Tự Rã Đông Sống Dậy Vào Mùa Xuân!**<br>Tim ngừng đập, máu ngừng chảy, $70\%$ cơ thể đóng băng nhưng gan bơm đường Glucose và Ure cực đặc vào tế bào làm chất chống đông. | **Shorts 33:** Trái tim ngừng đập hoàn toàn suốt 7 tháng mùa đông, nhưng khi nắng xuân lên, chú ếch đá này lại nhảy đi kiếm ăn! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 17 - Ca 2 (18:00)** | **Tập 34: Quạ Đen (Crow & Raven)** | **Thiên Tài IQ Cao Ngang Trẻ Lên 7: Biết Dùng Đèn Giao Thông Để Đập Hạt Và Ghi Thù Cả Đời!**<br>Thả hạt cứng dưới bánh xe ô tô lúc đèn đỏ rồi chờ đèn xanh người đi bộ bật lên mới bay xuống nhặt, truyền đạt khuôn mặt kẻ thù cho cả thế hệ con cháu. | **Shorts 34:** Đừng bao giờ đắc tội với một con Quạ, vì nó sẽ mô tả khuôn mặt bạn cho cả đàn và đời con cháu nó cùng trả thù! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 18 - Ca 1 (11:30)** | **Tập 35: Cá Voi Sát Thủ (Orca)** | **Băng Đảng Mafia Thực Sự Của Đại Dương: Phẫu Thuật Lấy Gan Cá Mập Trắng Với Độ Chính Xác Tuyệt Đối!**<br>Chiến thuật tạo sóng đánh trôi hải cẩu trên tảng băng, lật ngửa cá mập trắng gây trạng thái thôi miên bất động rồi mổ lấy lá gan giàu Squalene. | **Shorts 35:** Tại sao chúa tể Cá Mập Trắng lại bỏ chạy trối chết suốt cả năm trời chỉ vì đánh hơi thấy bóng dáng Cá Voi Sát Thủ? | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 18 - Ca 2 (18:00)** | **Tập 36: Chim Gõ Kiến (Woodpecker)** | **Đập Đầu Vào Thân Cây 12.000 Lần Mỗi Ngày Với Lực Gấp 10 Lần Phi Hành Gia Mà Không Bị Chấn Thương Sọ Não!**<br>Chiếc lưỡi dài gấp 3 lần mỏ quấn vòng quanh hộp sọ từ lỗ mũi ra sau gáy làm dây đai giảm chấn, xương xốp hấp thụ xung lực. | **Shorts 36:** Chiếc lưỡi của Chim Gõ Kiến dài đến mức nó phải... quấn vòng quanh hộp sọ để làm đệm chống sốc cho não! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 19 - Ca 1 (11:30)** | **Tập 37: Lạc Đà Sa Mạc (Camel)** | **Cỗ Máy Chinh Phục Sa Mạc: Bướu Lạc Đà Thực Chất Không Chứa Nước Và Màn Nhai Xương Rồng Đẫm Máu!**<br>Bướu chứa $36\text{ kg}$ mỡ dự trữ, vòm miệng có các gai sừng cứng đơ giúp nhai ngấu nghiến cây xương rồng chi chít gai nhọn, uống $150\text{ lít}$ nước trong $10\text{ phút}$. | **Shorts 37:** Bạn từng nghĩ bướu Lạc Đà chứa đầy nước bên trong ư? Sự thật và cấu tạo bên trong miệng của nó sẽ làm bạn rùng mình! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 19 - Ca 2 (18:00)** | **Tập 38: Dê Núi Bắc Mỹ (Mountain Goat)** | **Nghệ Sĩ Leo Vách Đá Thẳng Đứng 90 Độ: Chỉ Cần Một Gờ Đá Rộng 2 Xăng-ti-mét Là Đủ Đứng Vững!**<br>Móng guốc chẻ đôi có viền sừng cứng bên ngoài và lớp đệm cao su nhám siêu bám ở chính giữa, bất chấp trọng lực để liếm muối khoáng trên vách vực. | **Shorts 38:** Bí mật dưới bàn chân giúp Dê Núi đi dạo trên vách đập thủy điện thẳng đứng gần 90 độ như đi trên mặt đất! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 20 - Ca 1 (11:30)** | **Tập 39: Chim Bách Thanh (Shrike / Butcherbird)** | **Đồ Tể Mang Gương Mặt Chim Sẻ: Xiên Con Mồi Lên Gai Nhọn Làm... Tủ Lưu Trữ Thực Phẩm!**<br>Thân hình nhỏ bé dễ thương nhưng dùng gai cây keo và hàng rào dây thép gai để găm côn trùng, thằn lằn, chuột nhằm xé thịt và phân hủy chất độc. | **Shorts 39:** Đừng để ngoại hình mũm mĩm như chim sẻ đánh lừa, đây là "Gã Đồ Tể" tàn bạo chuyên xiên con mồi lên gai nhọn! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 20 - Ca 2 (18:00)** | **Tập 40: Kiến Cắt Lá (Leafcutter Ant)** | **Nền Văn Minh Nông Nghiệp Đầu Tiên Trên Trái Đất: Chúng Không Ăn Lá Mà Trồng Nấm Ngầm Dưới Đất!**<br>Lá cây chỉ là giá thể nuôi vườn nấm khổng lồ sâu $8\text{ mét}$ dưới lòng đất, kiến lính đầu to như xe tăng và kiến y tá mang vi khuẩn kháng sinh trên người. | **Shorts 40:** Kiến Cắt Lá vác những mảnh lá nặng gấp 50 lần cơ thể về tổ nhưng thực chất chúng... không hề ăn một miếng lá nào! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 21 - Ca 1 (11:30)** | **Tập 41: Nhện Nước & Nhện Lặn Chuông (Diving Bell Spider)** | **Kỹ Sư Tàu Ngầm 8 Chân: Tự Dệt Bình Dưỡng Khí Bằng Tơ Để Sống Trọn Đời Dưới Đáy Hồ!**<br>Dùng lông bụng không thấm nước quặp bong bóng oxy từ mặt nước dìm xuống lấp đầy quả chuông tơ có khả năng tự trao đổi khí như mang cá. | **Shorts 41:** Loài nhện duy nhất trên thế giới tự chế tạo "tàu ngầm dưỡng khí" bằng tơ để sống và săn mồi hoàn toàn dưới nước! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 21 - Ca 2 (18:00)** | **Tập 42: Cá Thoi Loi / Cá Bống Tượng Đầm Lầy (Mudskipper)** | **Con Cá Chán Biển Lên Bờ Đi Bộ: Hô Hấp Bằng Da Và Nháy Mắt Để... Nuốt Nước!**<br>Tích nước trong mang như bình lặn của thợ lặn nhưng ngược lại, nhảy cao trên bùn bằng vây ngực cơ bắp, thụt hai nhãn cầu xuống hốc mắt tạo áp lực nuốt mồi. | **Shorts 42:** Một con cá có thể chết đuối nếu bị nhốt quá lâu dưới nước và phải nháy mắt tụt vào trong đầu mới nuốt được thức ăn! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |

---

### TUẦN 4: NHỮNG THIẾT KẾ LỖI CỦA TẠO HÓA & ĐẠI CHIẾN SINH TỒN (NGÀY 22 – NGÀY 30)

| Ngày & Ca Đăng | Tập & Chủ Đề Con Vật | Tiêu Đề Video Dài & Góc Khai Thác Chuyên Sâu | Kịch Bản Shorts Đi Kèm (Động Cơ Kéo View) | Thời Lượng & Chất Lượng Yêu Cầu |
| :--- | :--- | :--- | :--- | :--- |
| **Ngày 22 - Ca 1 (11:30)** | **Tập 43: Ong Bắp Cày Ngọc Lục Bảo (Emerald Cockroach Wasp)** | **Bác Sĩ Phẫu Thuật Thần Kinh Tàn Nhẫn: Biến Gián Thành Zombie Ngoan Ngoãn Tự Đi Vào Huyệt Mộ!**<br>Mũi chích đầu tiên làm liệt chân trước của gián, mũi chích thứ hai đâm chính xác vào hạch não tiết chất khóa phản xạ bỏ chạy, rồi dắt râu gián như dắt chó về hang. | **Shorts 43:** Pha phẫu thuật não chính xác đến từng mi-li-mét biến một con gián khỏe mạnh thành "xác sống" ngoan ngoãn nghe lời! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 22 - Ca 2 (18:00)** | **Tập 44: Cá Mặt Trăng (Ocean Sunfish - Mola Mola)** | **Gã Khổng Lồ Ngơ Ngác Nhất Đại Dương: Nặng 2 Tấn Nhưng Bị Hải Cẩu Cắn Mất Vây Cũng Chỉ Biết... Nằm Im!**<br>Cơ thể như cái đầu cá biết bơi không có đuôi, đẻ $300\text{ triệu}$ trứng mỗi lần (nhiều nhất giới có xương sống), nổi lên mặt biển nhờ chim biển mổ ký sinh trùng. | **Shorts 44:** Nặng tới 2 tấn nhưng loài cá này hiền và chậm đến mức hải cẩu đến cắn rách vây nó cũng chỉ biết... mở mắt nhìn! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 23 - Ca 1 (11:30)** | **Tập 45: Vẹt Kakapo (New Zealand)** | **Loài Vẹt Duy Nhất Quên Cách Bay: Thấy Kẻ Thù Là Đứng Đơ Giả Làm Bụi Cây Dù Đang Ở Dưới Đất!**<br>Tiến hóa trên đảo không có thú săn mồi nên béo nặng tới $4\text{ kg}$, quên cách bay nhưng cứ thích trèo lên ngọn cây rồi nhảy xuống đập mặt, mùi cơ thể thơm như mật ong. | **Shorts 45:** Quên mất mình không biết bay nhưng vẫn leo lên ngọn cây nhảy xuống — đây là loài vẹt ngớ ngẩn nhất hành tinh! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 23 - Ca 2 (18:00)** | **Tập 46: Lợn Rừng Babirusa** | **Thiết Kế Tiến Hóa Tự Hủy: Cặp Răng Nanh Mọc Xuyên Thủng Môi Trên Rồi Cong Ngược Đâm Vào Chính Hộp Sọ!**<br>Răng nanh hàm trên mọc ngược lên trên xuyên qua da mõm, uốn cong về phía trán; nếu không mài gãy kịp thời, răng sẽ đâm xuyên qua sọ não của chính nó. | **Shorts 46:** Khi tiến hóa chơi khăm: Loài lợn có cặp răng nanh càng sống lâu càng cong ngược lại đâm thủng hộp sọ của chính mình! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 24 - Ca 1 (11:30)** | **Tập 47: Hươu Cao Cổ (Giraffe)** | **Cơn Ác Mộng Huyết Áp Của Chiếc Cổ Dài 2 Mét & Cú Rơi Tự Do Chào Đời Từ Độ Cao Gần 2 Mét!**<br>Trái tim nặng $11\text{ kg}$ bơm máu áp lực gấp đôi người, hệ thống van tĩnh mạch cảnh ngăn vỡ mạch máu não khi cúi xuống uống nước, ngủ đứng 30 phút/ngày. | **Shorts 47:** Tại sao Hươu Cao Cổ không bị nổ mạch máu não mỗi khi nó cúi chiếc cổ dài 2 mét xuống thấp để uống nước? | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 24 - Ca 2 (18:00)** | **Tập 48: Cò Mỏ Giày (Shoebill Stork)** | **Khủng Long Thời Tiền Sử Đội Lốt Chim: Tiếng Kêu Như Súng Máy Liên Thanh Và Màn Cúi Chào Lịch Thiệp!**<br>Đứng bất động hàng giờ như tượng đá, chiếc mỏ to như chiếc giày gỗ chặt đứt đầu cá phổi và cá sấu con, cúi đầu chào kết hợp tiếng gõ mỏ như súng AK. | **Shorts 48:** Nhìn con người thì cúi đầu chào cực kỳ lịch sự, nhưng với anh chị em ruột trong tổ thì loài chim này lại tàn nhẫn không ngờ! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 25 - Ca 1 (11:30)** | **Tập 49: Nhím Lông Nhọn (Porcupine) & Thú Lông Nhím (Echidna)** | **Pháo Đài 30.000 Mũi Tên Ngược: Sự Thật Về Tin Đồn Nhím Bắn Lông Và Những Con Báo Hoa Mai Mắc Sai Lầm!**<br>Lông nhím không bắn từ xa được nhưng đầu lông có hàng trăm ngạnh nhỏ như lưỡi câu tự rút sâu vào thịt theo nhịp co cơ của kẻ thù, kèm lớp kháng sinh tự nhiên. | **Shorts 49:** Tại sao chỉ cần một chiếc lông nhím cắm vào mõm cũng đủ sức hạ gục một con báo hoa mai hay sư tử trưởng thành? | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 25 - Ca 2 (18:00)** | **Tập 50: Khỉ Đột Lưng Bạc (Silverback Gorilla)** | **Sức Mạnh Cơ Bắp Gấp 10 Lần Con Người Nhưng Lại Có Hệ Tiêu Hóa Phình To Vì... Đầy Hơi Khí Gas!**<br>Lực đấm và lực cắn vượt xa sư tử nhưng chỉ ăn chay lá cây, chiếc bụng to tròn thực chất là lò lên men thực vật khổng lồ khiến chúng đánh rắm liên tục cả ngày. | **Shorts 50:** Tại sao Khỉ Đột chỉ ăn lá cây và măng rừng nhưng lại sở hữu khối cơ bắp cuồn cuộn nâng được vật nặng 800 kg? | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 26 - Ca 1 (11:30)** | **Tập 51: Cá Nóc Hộp & Cá Nóc Nhím (Pufferfish)** | **Quả Bóng Gai Độc Xyanua Gấp 1.200 Lần Và Nghệ Sĩ Vẽ Tranh Cát Lãng Mạn Nhất Đáy Biển!**<br>Độc tố Tetrodotoxin đủ hạ gục 30 người lớn, cơ chế hút nước phình bụng gấp 3 lần nhưng cá nóc đực lại dùng vây quạt cát suốt 7 ngày tạo vòng tròn Mandala. | **Shorts 51:** Ai đã vẽ những vòng tròn геометри tuyệt đẹp rộng 2 mét dưới đáy biển Nhật Bản? Thủ phạm chỉ dài vỏn vẹn 12 xăng-ti-mét! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 26 - Ca 2 (18:00)** | **Tập 52: Chim Hồng Hạc (Flamingo)** | **Ăn Tối Trong Nước Sôi Độc Hại, Đứng Ngủ Bằng 1 Chân Và Nuôi Con Bằng... Dòng Sữa Màu Đỏ Như Máu!**<br>Cơ chế khóa khớp cổ chân tự động không tốn năng lượng khi đứng 1 chân, mỏ lộn ngược lọc tảo làm lông chuyển hồng, tiết sữa diều màu đỏ tươi nuôi chim non. | **Shorts 52:** Cảnh tượng hai con Hồng Hạc cùng rỏ chất lỏng màu đỏ tươi vào miệng chim non từng khiến người xem tưởng chúng đang cắn nhau chảy máu! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 27 - Ca 1 (11:30)** | **Tập 53: Cầy Mangut (Mongoose) & Meerkat** | **Khắc Tinh Truyền Kiếp Của Rắn Hổ Mang Chúa: Phản Xạ Né Đòn Nhanh Đến Mức Rắn Trông Như Quay Chậm!**<br>Thụ thể Acetylcholine đột biến khiến nọc độc thần kinh của rắn không thể bám vào cơ bắp, chiến thuật khiêu vũ trêu ngươi cho rắn kiệt sức rồi cắn vỡ sọ. | **Shorts 53:** Bí mật sinh học giúp Cầy Mangut biến những cú mổ tử thần của Rắn Hổ Mang thành trò mèo vờn chuột! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 27 - Ca 2 (18:00)** | **Tập 54: Tắc Kè Hoa (Chameleon)** | **Sự Thật Bất Ngờ: Tắc Kè Hoa Đổi Màu Không Phải Để Ngụy Trang, Và Chiếc Lưỡi Phóng Nhanh Hơn Xe Đua F1!**<br>Đổi màu bằng tinh thể nano dưới da để thể hiện cảm xúc và điều chỉnh nhiệt độ, hai mắt xoay độc lập $360^\circ$, lưỡi tăng tốc từ $0 \rightarrow 100\text{ km/h}$ trong $0.01\text{ giây}$. | **Shorts 54:** Hoạt hình đã lừa chúng ta: Tắc Kè Hoa đổi màu sặc sỡ không phải để trốn kẻ thù mà là để... chửi nhau và tán tỉnh! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 28 - Ca 1 (11:30)** | **Tập 55: Cá Vây Chân / Cá Cần Câu Đáy Vực (Anglerfish)** | **Cuộc Hôn Nhân Kinh Dị Nhất Đáy Vực Thẳm: Con Đực Cắn Vào Bụng Con Cái Rồi Tan Chảy Thành Một Bộ Phận Cơ Thể!**<br>Chiếc cần câu phát sáng sinh học giữa bóng tối sâu $2.000\text{m}$, con đực nhỏ bằng ngón tay cái cắn chặt vào da con cái, hòa chung mạch máu và tiêu biến cả mắt lẫn não. | **Shorts 55:** Dưới đáy biển sâu 2.000 mét, khi một con cá đực tìm thấy bạn đời, nó sẽ cắn vào bụng con cái và... tan chảy vĩnh viễn vào đó! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 28 - Ca 2 (18:00)** | **Tập 56: Chim Ruồi (Hummingbird)** | **Chiếc Trực Thăng Duy Nhất Biết Bay Lùi: Tim Đập 1.200 Lần/Phút Và Nguy Cơ Chết Đói Chỉ Sau 2 Tiếng Nhịn Ăn!**<br>Vỗ cánh hình số 8 tới $80\text{ lần/giây}$, trao đổi chất nhanh nhất thế giới động vật có xương sống, ban đêm phải tự hạ thân nhiệt vào trạng thái chết giả để đỡ tốn năng lượng. | **Shorts 56:** Loài chim có tốc độ đốt năng lượng khủng khiếp đến mức mỗi đêm đi ngủ nó phải tự đưa mình vào trạng thái... hôn mê sâu! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 29 - Ca 1 (11:30)** | **Tập 57: Trăn Anaconda Xanh & Trăn Gấm** | **Làm Sao Một Con Trăn Có Thể Mở Rộng Hàm Nuốt Chửng Cả Cá Sấu Caiman Lẫn Hươu Trưởng Thành?**<br>Xương hàm dưới không khớp nối cố định mà liên kết bằng dây chằng co giãn siêu đàn hồi, ống khí quản thò hẳn ra ngoài miệng như ống thở lặn trong lúc nuốt mồi hàng giờ. | **Shorts 57:** Nuốt một con mồi to gấp 3 lần cái đầu mất tới vài tiếng đồng hồ, vậy loài trăn làm cách nào để không bị nghẹt thở? | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 29 - Ca 2 (18:00)** | **Tập 58: Tê Tê (Pangolin) & Tatu (Armadillo)** | **Bộ Giáp Vảy Sừng Chống Đạn Sư Tử Cắn Không Thủng Và Chiếc Lưỡi Dài Hơn Cả Cơ Thể Nằm Tận Khung Xương Chậu!**<br>Vảy Keratin sắc bén xếp lớp cuộn tròn thành quả bóng bất khả xâm phạm trước hàm sư tử, gốc lưỡi không gắn ở họng mà nối tận xương ức và xương chậu để liếm $70\text{ triệu}$ kiến/năm. | **Shorts 58:** Khi một con Tê Tê cuộn tròn lại, ngay cả hàm răng của chúa sơn lâm Sư Tử cũng chỉ biết lăn nó đi như quả bóng đá! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 30 - Ca 1 (11:30)** | **Tập 59: Đà Điểu Châu Phi & Đà Điểu Đầu Mào (Cassowary)** | **Sự Thật Việc Đà Điểu Rúc Đầu Xuống Cát Và Loài Chim Nguy Hiểm Nhất Hành Tinh Có Móng Vuốt Như Dao Găm!**<br>Giải oan lời đồn rúc đầu xuống cát (thực chất là đảo trứng và nằm sát đất ngụy trang), đôi mắt to hơn cả quả bóng bi-a, cú đá gãy xương của Đà Điểu Đầu Mào. | **Shorts 59:** Đừng bao giờ tin câu chuyện Đà Điểu sợ hãi rúc đầu xuống cát, vì một cú đá chân trước của nó có thể hạ gục cả sư tử! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 30 - Ca 2 (18:00)** | **Tập 60: Linh Cẩu Đốm (Spotted Hyena)** | **Đế Chế Nữ Quyền Tàn Khốc: Hàm Răng Nghiền Nát Xương Voi Và Cấu Tạo Cơ Thể Đánh Lừa Cả Giới Khoa Học!**<br>Lực cắn $1.100\text{ PSI}$ cùng axit dạ dày tiêu hóa cả xương và sừng, con cái to khỏe thống trị hoàn toàn con đực, thực chất họ hàng gần với loài mèo hơn loài chó. | **Shorts 60:** Trong thế giới của Linh Cẩu Đốm, con đực trưởng thành thậm chí còn có địa vị thấp hơn cả một... đứa con non vừa mới đẻ! | Dài: $8 - 10\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |
| **Ngày 30 - Ca Đặc Biệt (20:00)** | **Tập 61: Đại Hội Sinh Tồn (Tập Đặc Biệt Tổng Kết Tháng)** | **Ai Mới Là Bá Chủ Tuyệt Đối Của Tự Nhiên? Vòng Chung Kết Loại Trực Tiếp 10 Quán Quân!**<br>So kè bảng điểm RPG và đại chiến sinh tồn giữa các chiến thần (Lửng Mật, Tôm Tít, Gấu Nước, Lươn Điện, Hà Mã, Cá Voi Sát Thủ...) để tìm ra nhà vô địch toàn diện nhất hành tinh. | **Shorts 61:** Nếu nhốt Lửng Mật, Lươn Điện và Tôm Tít vào cùng một đấu trường sinh tồn, ai sẽ là kẻ bước ra cuối cùng? | Dài: $60 - 75\text{ phút}$ ($1080\text{p}/60\text{fps}$)<br>Shorts: $45 - 55\text{s}$ ($9:16$) |

---

## PHẦN 5: QUY TRÌNH ĐĂNG BÀI & TỐI ƯU THUẬT TOÁN (SEO & CTR)

1. **Quy tắc thiết kế Thumbnail cho Video Dài:**
   * Không lấy nguyên ảnh nền trắng trong video làm Thumbnail.
   * Phủ nền màu tương phản cao (Xanh dương đậm, Đỏ cam hoặc Vàng chanh), phóng to nhân vật chính chiếm $65\%$ diện tích khung hình với biểu cảm hoảng hốt hoặc hài hước cực độ.
   * Chỉ chèn đúng $2 - 4\text{ chữ}$ thật to (Font chữ dày, màu vàng tươi `#FFD700` hoặc trắng viền đen dày + đổ bóng). Ví dụ: `NUỐT SỐNG?!`, `BẤT TỬ HỤT!`, `ĐẤM VỠ KÍNH!`.
2. **Kỹ thuật Bắc Cầu (Funneling) từ Shorts sang Video Dài:**
   * Ngay sau khi tải lên cả Video Dài và Video Shorts của cùng một ca, vào **YouTube Studio trên máy tính** $\rightarrow$ Mở phần chỉnh sửa **Video Shorts** $\rightarrow$ Nhìn cột bên phải tìm mục **Video có liên quan (Related Video)** $\rightarrow$ Chọn gắn đúng Video Dài vừa đăng.
   * Ghim 1 bình luận đầu tiên dưới phần bình luận của cả Shorts và Video Dài với câu hỏi gây tranh luận để tăng tương tác (Ví dụ ở Tập 06: *"Theo bạn, nếu Gấu Nước to bằng một con chó Corgi thì con người có trị được nó không? Bình luận bên dưới nhé!"*).
import json
from pathlib import Path

ep43 = {
 "episode_no": 43,
 "animal": "Ong Bắp Cày Ngọc",
 "slug": "tap-43-ong-bap-cay-ngoc",
 "format": "F3",
 "persona": "phien_toa",
 "nickname": "Bác sĩ phẫu thuật thần kinh",
 "sources": [
  "Gal, R. & Libersat, F. (2010). A wasp manipulates neuronal activity in the sub-esophageal ganglion to decrease the drive for walking in its cockroach prey. PLoS ONE, 5(4), e10019 (Chích 2 phát độc tố: phát 1 làm liệt chân trước 2-3 phút, phát 2 vào hạch não dưới thực quản tước đoạt ý chí vận động chủ động)",
  "Libersat, F. et al. (2009). Mind control: how wasps turn cockroaches into zombies. J. Exp. Biol., 212(3), 473-481 (Gián không bại liệt, nếu ném xuống nước vẫn bơi thoát thân, nhưng mất hoàn toàn phản xạ tự vệ và ý chí chạy trốn)",
  "Williams, F. X. (1942). Ampulex compressa (Fabr.), a cockroach-hunting wasp introduced from New Caledonia into Hawaii. Proc. Hawaii. Entomol. Soc., 11(2), 221-233 (Ong cắt bớt 1 phần râu gián, uống dịch râu và nắm râu dắt gián đi như dắt thú cưng vào hang ngầm; đẻ 1 quả trứng lên chân gián)",
  "Keasar, T. et al. (2015). Host manipulation and reproductive success in parasitoid wasps. Behav. Processes, 117, 34-40 (Ấu trùng ăn các cơ quan không thiết yếu trước, giữ gián sống tươi ngon suốt 8-10 ngày trước khi hóa nhộng)",
  "Catania, K. C. (2018). How not to be turned into a zombie. Brain Behav. Evol., 92(1-2), 32-46 (Cú đá hậu karate của gián chống lại cú bổ nhào của ong bắp cày ngọc)"
 ],
 "whisper_prompt": "Ong Bắp Cày Ngọc, Ampulex compressa, Bác sĩ phẫu thuật thần kinh, Sát thủ ngọc bích, gián Zombie, hạch não, sub-esophageal ganglion, octopamine, dopamine, 2-3 phút, 8-10 ngày, Thẩm phán",
 "display_fix": {
  "bốn mươi ba": "43",
  "Bốn mươi ba": "43",
  "Tập bốn mươi ba": "Tập 43",
  "bốn mươi hai": "42",
  "Bốn mươi hai": "42",
  "bốn mươi tư": "44",
  "Bốn mươi tư": "44",
  "bốn mươi bốn": "44",
  "Bốn mươi bốn": "44",
  "số bốn mươi ba": "số 43",
  "Số bốn mươi ba": "Số 43",
  "hai mươi mi-li-mét": "20mm",
  "Hai mươi mi-li-mét": "20mm",
  "hai mi-li-mét": "2mm",
  "Hai mi-li-mét": "2mm",
  "hai đến ba phút": "2-3 phút",
  "Hai đến ba phút": "2-3 phút",
  "hai đến ba ngày": "2-3 ngày",
  "Hai đến ba ngày": "2-3 ngày",
  "tám đến mười ngày": "8-10 ngày",
  "Tám đến mười ngày": "8-10 ngày",
  "hai mươi bốn giờ": "24 giờ",
  "Hai mươi bốn giờ": "24 giờ",
  "hai tấn": "2 tấn",
  "Hai tấn": "2 tấn",
  "sáu lần": "6 lần",
  "Sáu lần": "6 lần",
  "hai tuần": "2 tuần",
  "Hai tuần": "2 tuần",
  "ba mươi phút": "30 phút",
  "Ba mươi phút": "30 phút",
  "một quả trứng": "1 quả trứng",
  "Một quả trứng": "1 quả trứng",
  "một trăm phần trăm": "100%",
  "Một trăm phần trăm": "100%",
  "tám mươi phần trăm": "80%",
  "Tám mươi phần trăm": "80%",
  "sáu mươi phần trăm": "60%",
  "Sáu mươi phần trăm": "60%",
  "hai phát": "2 phát",
  "Hai phát": "2 phát",
  "ba trăm triệu năm": "300 triệu năm",
  "Ba trăm triệu năm": "300 triệu năm",
  "một ngàn": "1.000",
  "Một ngàn": "1.000",
  "năm một ngàn chín trăm bốn mươi hai": "năm 1942",
  "Năm một ngàn chín trăm bốn mươi hai": "Năm 1942",
  "một mét rưỡi": "1.5 mét",
  "Một mét rưỡi": "1.5 mét",
  "phát thứ nhất": "phát 1",
  "phát thứ hai": "phát 2",
  "Phát thứ nhất": "Phát 1",
  "Phát thứ hai": "Phát 2"
 },
 "voice": {
  "format": "F3",
  "persona": "phien_toa",
  "mood_weights": {
   "hao_hung": 0.32,
   "don_dap": 0.24,
   "tram_bi_an": 0.18,
   "nghiem_trang_gia": 0.14,
   "am_ap": 0.12
  },
  "cameo_parts": [
   {"scene": "scene01", "part_idx": 1, "cast": "tham_phan"},
   {"scene": "scene02", "part_idx": 1, "cast": "tham_phan"},
   {"scene": "scene04", "part_idx": 1, "cast": "tham_phan"}
  ]
 },
 "art": {
  "decor": "titanium surgical scalpels, iridescent emerald exoskeleton plates, glowing cybernetic neural wires",
  "shorts_mascot": "A sleek cartoon emerald cockroach wasp with glowing metallic green-blue wings, holding a tiny glowing syringe like a surgeon",
  "thumb_bg": "cyberpunk neon operating theater in deep violet and pitch black with cyan neural wire diagrams",
  "thumb_title": ["THAO TÚNG TÂM TRÍ?!", "BIẾN GIÁN THÀNH XÁC SỐNG"],
  "thumb_scene": "chú ong bắp cày ngọc hoạt hình metallic xanh ngọc bích cầm kim tiêm phát sáng châm vào đầu con gián to gấp sáu lần đang đờ đẫn mắt hình xoắn ốc",
  "thumb_gag": "chú gián đeo dây xích cổ tự giác bước đi ngoan ngoãn như cún con với dấu hỏi chấm"
 },
 "longform": {
  "scenes": [
   {
    "id": "scene01",
    "badge": "CÁO TRẠNG VỤ ÁN",
    "banner_title": "BÁC SĨ PHẪU THUẬT TÀN ĐỘC",
    "chapter_title": "Vụ Án Thao Túng Tâm Trí Chấn Động Giới Côn Trùng",
    "hook": "BẢN CÁO TRẠNG THAO TÚNG NÃO BỘ VÀ TƯỚC ĐOẠT Ý CHÍ TỰ DO",
    "mood": "tram_bi_an",
    "parts": [
     {
      "text": "Trật tự toàn thể phòng xử án hình sự sinh học tối cao! Đại diện Viện Kiểm Sát Tự Nhiên hôm nay chính thức công bố bản cáo trạng điều tra đặc biệt về một vụ án xâm phạm thân thể và thao túng tâm lý tàn bạo bậc nhất trong lịch sử tiến hóa động vật! Không dùng sức mạnh cơ bắp áp đảo, không xé xác nạn nhân tại chỗ, kẻ thủ ác này khoác lên mình một tấm áo choàng ngọc bích lộng lẫy kiêu sa nhưng lại sở hữu thủ đoạn giải phẫu thần kinh lạnh lùng đến rợn gáy! Gã không giết chết con mồi, mà biến một chiến binh gián khỏe mạnh, nhanh nhẹn bậc nhất hành tinh thành một xác sống Zombie ngoan ngoãn tự bước chân vào nấm mồ chôn sống!",
      "mood": "tram_bi_an"
     },
     {
      "text": "Trật tự phiên tòa! Thẩm phán yêu cầu công tố viên công bố danh tính bị cáo và vạch trần thủ đoạn gây án ngay lập tức!",
      "cast": "tham_phan"
     },
     {
      "text": "[surprise-oh] Thưa Hội đồng xét xử! Bị cáo mang mã số bốn mươi ba của chúng ta có tên khoa học là Ampulex compressa, thuộc bộ cánh màng, hay còn được gọi bằng cái tên hoa mỹ là Ong Bắp Cày Ngọc! Nhưng trong giới giang hồ tự nhiên, nạn nhân và các nhà khoa học gọi gã bằng một biệt danh rùng rợn: Bác sĩ phẫu thuật thần kinh! Chiều dài cơ thể của gã chỉ khoảng hai mươi mi-li-mét, khoác lớp vỏ chitin lấp lánh ánh kim màu xanh ngọc lục bảo và lam biếc tuyệt đẹp tựa như một viên đá quý di động! Nhưng đừng để vẻ ngoài kiều diễm ấy đánh lừa, bởi vì chiếc đuôi của gã cất giấu một chiếc kim tiêm vi phẫu tinh xảo đến mức khiến mọi giáo sư phẫu thuật sọ não loài người cũng phải ngả mũ bái phục! [laughter]",
      "mood": "hao_hung"
     },
     {
      "text": "Trước khi đi vào hiện trường gây án, Viện Kiểm Sát xin nhấn mạnh rằng: Nạn nhân của Bác sĩ phẫu thuật thần kinh không phải là những sâu bọ mềm yếu. Nạn nhân là loài gián nhà Mỹ Periplaneta americana, một loài sinh vật sống dai khét tiếng đã tồn tại hơn ba trăm triệu năm trên Trái Đất! Một loài côn trùng có thể sống sót sau bom nguyên tử, chạy trốn với vận tốc một mét rưỡi mỗi giây, và có thể sống cả tuần mà không cần đầu! Nhưng khi đối đầu với mũi kim của Bác sĩ phẫu thuật thần kinh, toàn bộ sức mạnh kiên cường ấy biến thành con số không tròn trĩnh!",
      "mood": "nghiem_trang_gia"
     }
    ]
   },
   {
    "id": "scene02",
    "badge": "ĐÒN TẤN CÔNG #1",
    "banner_title": "CÚ CHÂM LIỆT CHÂN TRƯỚC",
    "chapter_title": "Mũi Tiêm Số 1 Khóa Chặt Khớp Ngực Nạn Nhân",
    "hook": "PHÁT SÚNG GÂY MÊ TẠM THỜI VÀO HẠCH THẦN KINH NGỰC",
    "mood": "don_dap",
    "parts": [
     {
      "text": "Hãy lật lại từng trang hồ sơ khám nghiệm hiện trường vụ tấn công! Nạn nhân được lựa chọn ở đây là loài gián nhà nhiệt đới. Về tương quan thể lực, con gián to lớn và nặng gấp sáu lần Bác sĩ phẫu thuật thần kinh! Gián sở hữu hệ thống lông cảm biến siêu nhạy ở đuôi, phát hiện được cả những dao động không khí nhỏ nhất và có thể tăng tốc tẩu thoát chỉ trong vòng vài phần nghìn giây. Nếu lao vào một cuộc đấu vật tay đôi trực diện, chú ong nhỏ bé chắc chắn sẽ bị con gián khổng lồ đá văng hoặc nghiền nát dưới những chiếc chân gai nhọn hoắt!",
      "mood": "don_dap"
     },
     {
      "text": "Vậy bị cáo đã làm cách nào để khuất phục một gã khổng lồ to xác gấp sáu lần mình?",
      "cast": "tham_phan"
     },
     {
      "text": "[surprise-wa] Đây chính là điểm khởi đầu của kế hoạch gây án bài bản đến kinh ngạc! Bác sĩ phẫu thuật thần kinh không hề chích bừa bãi! Gã phục kích từ trên cao, lao xuống như một tia chớp kim loại và dùng cặp hàm thép kẹp chặt lấy lưng con gián. Ngay trong tích tắc đối phương còn đang bàng hoàng, chiếc kim tiêm từ đuôi ong uốn cong, đâm một phát châm chuẩn xác đến từng mi-li-mét vào hạch thần kinh ngực trước của gián! Độc tố của phát thứ nhất chứa hàm lượng lớn chất ức chế dẫn truyền GABA, ngay lập tức làm tê liệt hoàn toàn hai chiếc chân trước của nạn nhân trong vòng hai đến ba phút! [laughter] Con gián dù vẫn còn tỉnh táo nhưng hai chân trước đã bị liệt hoàn toàn, không thể cựa quậy hay xoay người bỏ chạy! Chiếc áo giáp phản xạ của gián chính thức bị phong tỏa!",
      "mood": "hao_hung"
     },
     {
      "text": "Nhóm nghiên cứu của giáo sư Kenneth Catania tại Đại học Vanderbilt đã sử dụng máy quay tốc độ cao một ngàn khung hình mỗi giây để giải mã cuộc đụng độ này: Khi gián phát hiện bị ong tập kích, nó thường vung chân sau tung ra những cú đá hậu karate cực mạnh nhằm hất văng kẻ thù. Nhưng Bác sĩ phẫu thuật thần kinh cực kỳ ranh mãnh! Gã lượn vòng từ góc mù, túm chặt lấy mép khiên ngực bảo vệ của gián, biến chính điểm tựa của đối phương thành thế gọng kìm bất khả kháng cự! Cú châm kim số một diễn ra chỉ trong vòng nửa giây, nhanh như một mũi tên tẩm thuốc mê bắn trúng tim đen con mồi!",
      "mood": "don_dap"
     }
    ]
   },
   {
    "id": "scene03",
    "badge": "VI PHẪU THẦN KINH",
    "banner_title": "MŨI TIÊM VÀO HẠCH NÃO",
    "chapter_title": "Kỹ Thuật Châm Kim Não Bộ Tước Đoạt Ý Chí Tự Do",
    "hook": "VI PHẪU ĐỘC TỐ ỨC CHẾ NÃO BỘ BIẾN THÀNH XÁC SỐNG",
    "mood": "nghiem_trang_gia",
    "parts": [
     {
      "text": "Sau khi nạn nhân đã bị trói chặt hai chân trước trong trạng thái bất động tạm thời, ca phẫu thuật sọ não rùng rợn nhất hành tinh chính thức bắt đầu! Thưa Hội đồng xét xử, hãy nhìn vào màn hình phóng đại vi phẫu: Bác sĩ phẫu thuật thần kinh từ tốn buông ngực gián ra, bò lên phần đầu của nạn nhân. Gã dùng hàm giữ chặt mép sọ, rồi từ từ chọc chiếc kim tiêm dài luồn qua lớp màng mềm giữa đầu và cổ. Đây không phải là một cú đâm mù quáng! Các nghiên cứu của giáo sư Libersat tại Đại học Ben-Gurion đã phát hiện ra rằng: Trên đầu mũi kim của ong có chứa hàng loạt thụ thể hóa học và cơ học cực nhạy, đóng vai trò như một hệ thống định vị GPS sinh học!",
      "mood": "nghiem_trang_gia"
     },
     {
      "text": "Mũi kim vi phẫu luồn sâu vào trong hộp sọ, dò dẫm từng milimét mô não và chạm thẳng vào trung khu điều khiển vận động tối cao: Đó là hạch não dưới thực quản của gián! Tại đây, gã bơm vào một liều cocktail hóa chất độc quyền gồm dopamine và các hợp chất ức chế thụ thể octopamine. Hợp chất này có tác dụng gì? Nó không hề giết chết tế bào não, cũng không làm gián bị tê liệt toàn thân! Ngược lại, tim gián vẫn đập, cơ bắp vẫn hoạt động bình thường! Nhưng thụ thể octopamine chính là chiếc công tắc khởi động ý chí sinh tồn, động lực chạy trốn và phản xạ sợ hãi của loài gián. Khi công tắc này bị dập tắt, con gián hoàn toàn mất đi ý chí tự do! [surprise-oh] Nếu bạn thả con gián này vào một xô nước, phản xạ bản năng vẫn khiến nó bơi nổi; nhưng nếu để nó trên cạn, nó sẽ chỉ đứng đực mặt ra đó, ngoan ngoãn đến mức ai làm gì cũng cam chịu! Một xác sống Zombie thực thụ đã ra đời dưới ngòi kim của Bác sĩ phẫu thuật thần kinh!",
      "mood": "tram_bi_an"
     },
     {
      "text": "Điều kỳ dị hơn nữa là ngay sau khi mũi kim rút ra khỏi não, lượng dopamine đậm đặc trong nọc độc bắt đầu phát huy tác dụng tâm lý bất ngờ: Con gián không hề bỏ chạy hay quằn quại đau đớn, mà đứng yên tại chỗ và bắt đầu chải chuốt cơ thể một cách cuồng loạn suốt ba mươi phút liên tục! Nó dùng chân lau chùi mắt, vuốt ve râu và làm sạch cơ thể như một kẻ mắc chứng ám ảnh cưỡng chế! Trong lúc nạn nhân đang mải mê làm đẹp trong vô thức, Bác sĩ phẫu thuật thần kinh thong dong bay đi tìm một chiếc hốc đất lý tưởng để chuẩn bị căn phòng giam giữ!",
      "mood": "hao_hung"
     }
    ]
   },
   {
    "id": "scene04",
    "badge": "HIỆN TRƯỜNG DẮT MỒI",
    "banner_title": "DẮT RÂU ĐI DẠO VÀO MỒ",
    "chapter_title": "Màn Dắt Gián Như Thú Cưng Đi Vào Nấm Mồ Ngầm",
    "hook": "CẮT TỈA CẶP ĂNG-TEN VÀ DẮT XÁC SỐNG TỰ BƯỚC ĐI",
    "mood": "hao_hung",
    "parts": [
     {
      "text": "Sau ca phẫu thuật não kéo dài chưa đầy ba mươi phút, tác dụng của mũi tiêm số một tan biến, hai chân trước của con gián cử động trở lại bình thường. Nhưng hỡi ôi, nạn nhân giờ đây chỉ còn là một cái xác không hồn biết thở! Bác sĩ phẫu thuật thần kinh lúc này tiến hành bước xử lý tiếp theo khiến các điều tra viên phải há hốc mồm: Thể trọng con gián quá nặng, gấp sáu lần ong, nên ong hoàn toàn không thể tha hay vác nạn nhân bay trên không trung. Thay vì tốn sức kéo lê con mồi khổng lồ, gã lại bắt con mồi phải tự đi bằng chính đôi chân của mình!",
      "mood": "hao_hung"
     },
     {
      "text": "Con gián to xác tự bước đi theo sau kẻ thù sao?! Thật hoang đường, chuyện này diễn ra như thế nào?",
      "cast": "tham_phan"
     },
     {
      "text": "[surprise-wa] Đúng như Thẩm phán vừa kinh ngạc thốt lên! Bác sĩ phẫu thuật thần kinh tiến lại gần, dùng cặp hàm sắc lẻm cắt tỉa bớt một nửa chiều dài hai sợi râu dài của con gián. Gã ghé miệng vào vết cắt uống từng giọt dịch máu hemolymph tứa ra để nạp lại năng lượng calo sau ca mổ căng thẳng. Sau đó, gã ngậm chặt lấy phần gốc râu còn lại của con gián như cầm một sợi dây dắt chó đi dạo! [laughter] Gã lùi từng bước về phía trước, và con gián to xác răm rắp bước theo từng bước chân của kẻ đã cướp não mình! Nạn nhân thong thả bước xuống căn hầm mộ tối tăm do ong đào sẵn dưới lòng đất, ngoan ngoãn ngồi im trong góc tối mà không có lấy một chút ý định chạy trốn hay phản kháng!",
      "mood": "don_dap"
     },
     {
      "text": "Nhà tự nhiên học Francis Williams khi quan sát hiện tượng này tại quần đảo Hawaii vào năm một ngàn chín trăm bốn mươi hai đã từng miêu tả: Đây là cảnh tượng siêu thực bậc nhất trong rừng nhiệt đới! Một chú ong nhỏ bằng hạt đậu ngọc bích, dùng hàm ngậm râu con gián khổng lồ dắt đi băng qua những đám lá khô mục nát. Con gián bước đi thảnh thơi tựa như đang dạo phố cùng bạn thân, thỉnh thoảng còn dừng lại đợi chú ong vượt qua chướng ngại vật! Toàn bộ hệ thống cơ bắp vận động của con gián vẫn hoạt động một trăm phần trăm công suất, nhưng bộ máy ý chí và bản năng tự vệ đã bị kẻ thù cầm tù vĩnh viễn!",
      "mood": "nghiem_trang_gia"
     }
    ]
   },
   {
    "id": "scene05",
    "badge": "TỦ LẠNH SINH HỌC",
    "banner_title": "ẤU TRÙNG ĂN NỘI TẠNG SỐNG",
    "chapter_title": "Chiến Lược Bảo Quản Thịt Tươi Sống Đỉnh Cao Của Ấu Trùng",
    "hook": "BẢO QUẢN THỰC PHẨM SỐNG SUỐT 8 NGÀY KHÔNG ÔI THIU",
    "mood": "don_dap",
    "parts": [
     {
      "text": "Thưa Hội đồng xét xử, chương man rợ và tinh vi nhất của bản cáo trạng nằm ở căn hầm mộ này! Sau khi dắt được con gián vào hang, Bác sĩ phẫu thuật thần kinh không hề cắn chết nạn nhân. Gã đẻ cẩn thận đúng một quả trứng duy nhất dính chặt vào gốc chân giữa của gián. Sau đó, ong mẹ chui ra khỏi hang, cần mẫn nhặt từng viên sỏi nhỏ, mẩu lá cây và đất vụn lấp kín miệng hang lại để ngăn chặn mọi kẻ xâm nhập từ bên ngoài. Con gián bị nhốt kín bên trong bóng tối vĩnh cửu cùng với quả trứng tử thần!",
      "mood": "don_dap"
     },
     {
      "text": "Sau hai đến ba ngày, quả trứng nở thành một ấu trùng ong nhỏ xíu màu trắng. Ấu trùng dùng hàm cắn thủng một lỗ nhỏ trên lớp vỏ gián để hút dịch cơ thể. Khi lớn hơn, nó chui tọt vào bên trong ổ bụng của gián và bắt đầu bữa tiệc sinh tồn! Hãy lắng nghe nguyên tắc y khoa của ấu trùng: Nếu nó cắn đứt tim hoặc hệ thần kinh trung ương, con gián sẽ chết ngay lập tức; và trong môi trường nhiệt đới nóng ẩm, cái xác sẽ thối rữa và bốc mùi chỉ sau hai mươi bốn giờ, đầu độc chết chính ấu trùng! Do đó, ấu trùng ong được lập trình bản năng chuẩn xác: Nó ăn toàn bộ lớp mỡ thừa và các cơ quan không thiết yếu trước, tuyệt đối tránh xa tim và mạch máu! Con gián vẫn sống, tim vẫn đập suốt tám đến mười ngày liên tục như một chiếc tủ lạnh sinh học bảo quản thịt tươi hoàn hảo! Cho đến khi ăn sạch mọi thứ, ấu trùng mới cắn đứt tim, đan kén nhộng bên trong xác gián khô rỗng rồi lột xác bay ra ngoài!",
      "mood": "nghiem_trang_gia"
     },
     {
      "text": "Chưa dừng lại ở đó, các nhà sinh vật học còn phát hiện ấu trùng ong tiết ra một loại hợp chất kháng sinh cực mạnh từ tuyến nước bọt. Hợp chất này phủ kín toàn bộ khoang bụng của gián, tiêu diệt sạch sẽ mọi vi khuẩn phân hủy và nấm mốc gây hại trong lòng đất ẩm ướt! Nói cách khác, con gián không những bị biến thành thức ăn tươi sống, mà còn được ấu trùng tắm rửa khử trùng đạt chuẩn phòng phẫu thuật vô khuẩn tuyệt đối! Một quy trình bảo quản thực phẩm đỉnh cao mà ngay cả các tập đoàn công nghệ thực phẩm hàng đầu thế giới cũng phải trầm trồ thán phục!",
      "mood": "hao_hung"
     }
    ]
   },
   {
    "id": "scene06",
    "badge": "BẢN ÁN CUỐI CÙNG",
    "banner_title": "TUYỆT TÁC CHÍNH XÁC KỲ DIỆU",
    "chapter_title": "Khép Lại Vụ Án Thao Túng Não Bộ Kỳ Vĩ Của Tự Nhiên",
    "hook": "BẢN ÁN TIẾN HÓA VÀ LỜI GIẢI MÃ BÍ ẨN HỒ SƠ 44",
    "mood": "am_ap",
    "parts": [
     {
      "text": "Phiên tòa xét xử hồ sơ số bốn mươi ba chính thức tuyên bố kết luận: Dưới lăng kính đạo đức con người, hành vi của Ong Bắp Cày Ngọc có thể khiến chúng ta rùng mình ớn lạnh. Nhưng dưới góc nhìn của khoa học tiến hóa, đây là một tuyệt tác cơ sinh học và hóa dược đỉnh cao! Tự nhiên không có thiện hay ác, chỉ có sự thích nghi tột cùng để sinh tồn. Bác sĩ phẫu thuật thần kinh đã chứng minh rằng: Một sinh vật nhỏ bé hoàn toàn có thể khuất phục những kẻ khổng lồ gấp nhiều lần bằng sự chính xác tuyệt đối, chiến lược bài bản và trí tuệ vi phẫu đỉnh cao!",
      "mood": "am_ap"
     },
     {
      "text": "Nếu trong cuộc sống bạn gặp phải những thử thách khổng lồ tưởng chừng không thể vượt qua, đừng vội dùng sức mạnh thô bạo để húc đầu vào đá: Hãy học tập sự sắc bén của ong bắp cày ngọc, tìm ra đúng mắt xích trọng tâm và giải quyết vấn đề bằng sự điềm tĩnh và chính xác nhất!",
      "mood": "hao_hung"
     },
     {
      "text": "Nếu được sở hữu một kỹ năng của loài ong này, bạn muốn sở hữu chiếc áo ngọc bích lấp lánh hay khả năng vi phẫu thao túng tâm trí? Hãy để lại bình luận tranh luận của bạn bên dưới nhé!",
      "mood": "hao_hung"
     },
     {
      "text": "Còn bây giờ, hãy chuẩn bị bước vào hồ sơ bệnh án số bốn mươi tư! Một gã khổng lồ nặng tới hai tấn trôi dạt giữa đại dương, cơ thể dị hợm như chỉ có một cái đầu cụt ngủn biết bơi, ngơ ngác đến mức bị hải cẩu bơi lại cắn đứt từng mảng vây vẫn nằm phơi nắng nhìn trời! Bạn có biết gã khổng lồ vô tri này là ai không?",
      "mood": "tram_bi_an"
     }
    ]
   }
  ]
 },
 "shorts": {
  "target_s": 54.0,
  "mood": "hao_hung",
  "text": "[surprise-oh] Bạn có tin một con ong bé tí chỉ bằng ngón tay lại có thể biến một con gián to gấp sáu lần thành một xác sống Zombie ngoan ngoãn nghe lời răm rắp? Đây là Ong Bắp Cày Ngọc, sát thủ mang biệt danh Bác sĩ phẫu thuật thần kinh! Thay vì giết con mồi, gã tung ra hai phát châm kim độc quyền: Phát thứ nhất châm thẳng vào ngực làm tê liệt hai chân trước của gián trong hai đến ba phút. Sau đó, gã chọc mũi kim xuyên qua sọ gián, tìm chính xác hạch não dưới thực quản để bơm độc tố ức chế ý chí sinh tồn! Hậu quả là con gián vẫn sống, tim vẫn đập, nhưng mất sạch một trăm phần trăm phản xạ sợ hãi và ý chí chạy trốn! Ong chỉ việc cắn bớt râu, ngậm gốc râu dắt con gián tự bước chân vào hang ngầm như dắt thú cưng đi dạo! Một kỳ tích vi phẫu não bộ thao túng tâm lý đỉnh cao và rùng rợn nhất thế giới côn trùng!",
  "title_lines": [
   "ONG PHẪU THUẬT NÃO",
   "BIẾN GIÁN THÀNH ZOMBIE?!"
  ]
 },
 "seo": {
  "title": "Bác Sĩ Phẫu Thuật Thần Kinh: Thao Túng Gián Thành Zombie?! | Ong Bắp Cày Ngọc | Tập 43",
  "hook_paragraph": "Khám phá vụ án chấn động tự nhiên của Ong Bắp Cày Ngọc (Ampulex compressa) — kẻ sở hữu ngòi kim vi phẫu châm chuẩn xác vào hạch não để tước đoạt ý chí tự do, biến con gián to gấp sáu lần thành một xác sống Zombie ngoan ngoãn tự bước vào mồ chôn!",
  "bullets": [
   "Chiếc áo choàng ngọc bích lấp lánh ẩn giấu ngòi kim vi phẫu sọ não tinh xảo nhất giới côn trùng",
   "Phát tiêm số một vào hạch ngực phong tỏa hoàn toàn 2 chân trước trong 2-3 phút",
   "Cú vi phẫu số hai vào hạch não dưới thực quản dập tắt hoàn toàn thụ thể ý chí sinh tồn",
   "Cắt tỉa ăng-ten dắt gián khổng lồ tự đi bộ vào hầm mộ ngầm như dắt thú cưng",
   "Ấu trùng ăn nội tạng có chọn lọc, giữ gián sống tươi ngon suốt 8-10 ngày trong hang"
  ],
  "question": "Nếu được sở hữu một kỹ năng của loài ong này, bạn muốn có bộ giáp ngọc bích kiêu sa hay khả năng vi phẫu thao túng tâm trí?",
  "next_teaser": "Tập 44: Bệnh án gã khổng lồ 2 tấn ngơ ngác như cái đầu cụt bơi giữa đại dương — Cá Mặt Trăng!",
  "hashtags": [
   "#OngBapCayNgoc",
   "#AmpulexCompressa",
   "#TheGioiDongVat",
   "#VeChuyenHoangDa",
   "#KhoaHoc",
   "#DongVatKyThu"
  ],
  "tags": [
   "ong bắp cày ngọc",
   "ong bap cay ngoc",
   "ampulex compressa",
   "emerald cockroach wasp",
   "ong bien gian thanh zombie",
   "gian zombie",
   "phau thuat than kinh con trung",
   "thế giới động vật",
   "vẽ chuyện hoang dã",
   "tập 43"
  ],
  "shorts_title": "Ong phẫu thuật não biến gián thành Zombie?! 🐝🧠 #shorts #dongvat #khoahoc",
  "shorts_desc": "Khám phá cách Ong Bắp Cày Ngọc chích kim vào hạch não tước đoạt ý chí tự do, biến con gián to gấp 6 lần thành xác sống Zombie tự đi vào hang ngầm!",
  "shorts_tags": [
   "ong bắp cày ngọc",
   "gian zombie",
   "shorts",
   "thế giới động vật",
   "vẽ chuyện hoang dã"
  ]
 }
}

with open('projects/tap-43-ong-bap-cay-ngoc/episode.json', 'w', encoding='utf-8') as f:
    json.dump(ep43, f, ensure_ascii=False, indent=1)

print("Episode 43 JSON written successfully!")

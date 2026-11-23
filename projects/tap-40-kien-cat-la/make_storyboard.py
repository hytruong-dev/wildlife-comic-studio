# -*- coding: utf-8 -*-
import json
import os

sb = {
  "_doc": "Storyboard cho Tập 40: Kiến Cắt Lá — Đại Công Trình Sư Rừng Rậm. Phong cách: Architectural Cross-Section & Industrial Blueprint.",
  "visual_style": "Architectural Cross-Section & Industrial Blueprint (phong cách mặt cắt kiến trúc địa tầng ngầm, bản vẽ kỹ thuật CAD/Blueprint trắng xanh công nghiệp, thước đo tỷ lệ mét, đường ống thông khí khí động học, sơ đồ luân chuyển hữu cơ sinh thái, nét vẽ kỹ thuật cơ khí sắc bén kết hợp comic 2D whiteboard; nền trắng tinh sáng sủa, tuyệt đối không chữ rác, không watermark)",
  "style_label": "Architectural Cross-Section & Industrial Blueprint",
  "characters": {
    "HERO": "chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản",
    "HERO_S": "chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ",
    "NO_HERO": "KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này"
  },
  "side_characters": {},
  "shorts_side_characters": {},
  "shorts_title_lines": [
    "ĐẠI CÔNG TRÌNH SƯ",
    "KỲ QUAN NÔNG NGHIỆP 50 TRIỆU NĂM?!"
  ],
  "skip_numbers": [],
  "shorts": [
    {
      "at": 0,
      "layout": "Khung cảnh mở đầu đại công trường: {HERO} đứng trên bản vẽ mặt cắt địa tầng ngầm, tay cầm thước đo chỉ vào độ sâu tám mét.",
      "stickers": [],
      "impacts": []
    },
    {
      "at": "Trước khi con người xuất hiện",
      "layout": "Bản vẽ lịch sử Trái Đất: Dòng thời gian 50 triệu năm trước với biểu tượng vườn nấm ngầm rực rỡ dưới chân khủng long. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "at": "quy mô công nghiệp sâu 8m",
      "layout": "Mặt cắt đứng thành phố ngầm sâu 8m với hàng ngàn phòng chức năng kết nối chằng chịt như mạng lưới tàu điện ngầm. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "at": "Bí mật kinh hoàng nằm ở chỗ",
      "layout": "{HERO} lắc ngón tay chỉ vào chiếc lá cây xanh mướt trên lưng, nụ cười bí ẩn của vị tổng công trình sư.",
      "stickers": [],
      "impacts": []
    },
    {
      "at": "Chúng cắt lá cây không phải để ăn",
      "layout": "Cận cảnh hàm răng cưa rung tần số cao xẻ ngọt phiến lá thành bột mịn rơi xuống luống phân bón hữu cơ. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "at": "như máy cưa xẻ nát lá",
      "layout": "Nhà máy chế biến sinh học: Kiến thợ nhào trộn bột lá với enzyme dịch ruột để nuôi sợi nấm trắng tinh khiết. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "at": "Tổ của chúng đào bới hơn 40 tấn",
      "layout": "Đại kim tự tháp Giza đặt cạnh núi đất 40 tấn do đàn kiến tí hon đào bới vận chuyển lên mặt đất. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "at": "hệ thống thông gió đối lưu tự nhiên",
      "layout": "Sơ đồ khí động học: Luồng khí nóng màu đỏ thoát ra giếng trung tâm, luồng khí mát màu xanh tràn vào giếng ngoại vi. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "at": "giữ nhiệt độ luôn ổn định ở 25°C",
      "layout": "Đồng hồ nhiệt độ điện tử cố định ở 25°C và độ ẩm 90% hoàn hảo giữa thời tiết nhiệt đới khắc nghiệt. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "at": "Thậm chí trên mai kiến còn có vi khuẩn",
      "layout": "Kính hiển vi phóng to lớp phấn trắng trên mai kiến thợ: Vi khuẩn tiết thuốc kháng sinh tiêu diệt nấm mốc dịch bệnh. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "at": "để bảo vệ mùa màng",
      "layout": "Trang trại nấm trắng ngà bồng bềnh sạch bóng mầm bệnh, biểu tượng mùa màng bội thu vô trùng 50 triệu năm. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "at": "Đúng là bậc thầy kiến trúc vĩ đại",
      "layout": "{HERO} hiên ngang đứng trên đỉnh công trình ngầm, giương cao tấm huy chương vàng Kiến Trúc Sư Vĩ Đại Của Thiên Nhiên.",
      "stickers": [],
      "impacts": []
    }
  ],
  "long": [
    # Scene 01 (12 beats)
    {
      "scene": "scene01",
      "at": 0,
      "layout": "Phòng thiết kế kỹ thuật sinh học: {HERO} đứng bên bàn vẽ CAD blueprint trải dài, tay cầm bút chỉ vào mặt cắt lòng đất.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene01",
      "at": "phòng thiết kế kỹ thuật sinh học",
      "layout": "Toàn cảnh rừng mưa nhiệt đới Amazon bạt ngàn với những tán cây cổ thụ khổng lồ vươn lên mây trời. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene01",
      "at": "Hãy quan sát mặt cắt bản vẽ kỹ thuật",
      "layout": "Mặt cắt địa chất 3D bóc tách từng lớp đất từ bề mặt thảm thực vật xuống tận độ sâu 8m dưới lòng đất. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene01",
      "at": "ăn sâu 8m xuống lòng đất",
      "layout": "Thước đo độ sâu thẳng đứng cắm mốc 8m: Hệ thống buồng ngầm đa tầng quy mô đồ sộ như tòa nhà chọc trời đảo ngược. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene01",
      "at": "vận chuyển hơn 40 tấn đất đá",
      "layout": "Núi đất đá 40 tấn khổng lồ trên mặt đất do hàng triệu chú kiến thợ vận chuyển từng viên đất nhỏ bé. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene01",
      "at": "xây dựng đại kim tự tháp Giza",
      "layout": "Hình ảnh so sánh đối chiếu: Đại kim tự tháp Ai Cập bằng đá sừng sững bên cạnh công trình đào đất của đàn kiến. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene01",
      "at": "Thưa Tổng chỉ huy công trình",
      "layout": "Cô trợ lý kỹ thuật đeo kính bảo hộ cầm máy quét siêu âm địa chấn báo cáo thông số cấu trúc ngầm. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene01",
      "at": "có tới hơn 1.000 căn phòng chuyên dụng",
      "layout": "Sơ đồ mạng lưới 1.000 căn phòng chức năng: Phòng ấp trứng, phòng nuôi nấm, phòng kiến chúa và bãi rác ngầm. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene01",
      "at": "Những công trình sư tài ba",
      "layout": "{HERO} nở nụ cười tự hào, hai hàm răng cưa lấp lánh phản chiếu ánh đèn công trường kỹ thuật.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene01",
      "at": "gọi chúng bằng danh hiệu",
      "layout": "Biểu tượng danh hiệu vàng rực: Đại Công Trình Sư Ngầm — Danh hiệu kiến trúc sư tối cao của thế giới tự nhiên.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene01",
      "at": "phát minh ra nền nông nghiệp",
      "layout": "Dòng thời gian so sánh: Loài người làm nông 10.000 năm đối chiếu với kiến cắt lá làm nông 50 triệu năm trước. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene01",
      "at": "Lá cây mà chúng rầm rộ cắt xẻ",
      "layout": "{HERO} gánh mảnh lá xanh khổng lồ hình bán nguyệt trên lưng, chuẩn bị mở ra bản vẽ lưỡi cưa sinh học.",
      "stickers": [],
      "impacts": []
    },

    # Scene 02 (12 beats)
    {
      "scene": "scene02",
      "at": 0,
      "layout": "Bản vẽ cơ khí bóc tách: Cận cảnh cặp hàm răng cưa của kiến thợ được phóng to dưới kính hiển vi điện tử. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene02",
      "at": "Hàm của kiến thợ cắt lá được gia cố",
      "layout": "Mạng lưới tinh thể nguyên tử kẽm và mangan gia cố liên kết kim loại sinh học ở rìa răng cưa. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene02",
      "at": "ngang ngửa với lưỡi dao phẫu thuật",
      "layout": "So sánh độ cứng: Răng cưa kiến thợ cắt ngọt qua kim loại thử nghiệm sắc lẹm như dao mổ titan. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene02",
      "at": "cơ chế rung tần số cao",
      "layout": "{HERO} kích hoạt cơ chế rung bụng, các sóng dao động siêu âm lan tỏa dọc sống lưng xuống hàm.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene02",
      "at": "tần số lên tới 1.000 lần mỗi giây",
      "layout": "Máy đo tần số hiển thị con số 1.000 Hz: Dao cắt siêu âm xẻ từng thớ lá dai nhách không tì vết. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene02",
      "at": "xẻ ngọt phiến lá dai nhách",
      "layout": "Đồng hồ bấm giờ 30 giây: Một mảnh lá tròn hoàn hảo rơi ra sau một đường cắt sắc lẹm hình cung. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene02",
      "at": "Thưa Chỉ huy có phải mỗi mảnh lá cây",
      "layout": "Cô trợ lý kỹ thuật trầm trồ chỉ vào chiếc cân tiểu ly đo đạc trọng lượng mảnh lá cây. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene02",
      "at": "Chính xác tuyệt đối",
      "layout": "Hình ảnh minh họa: Lực sĩ con người gánh chiếc xe hơi 2 tấn trên vai chạy nước rút trên đường đua. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene02",
      "at": "Một chú kiến thợ chỉ nặng vài mi-li-gam",
      "layout": "{HERO} gánh mảnh lá nặng gấp 20 lần cơ thể phi như bay trên cành cây với nụ cười sảng khoái.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene02",
      "at": "Khi hàng triệu chú kiến cùng rầm rộ",
      "layout": "Dòng sông lá xanh cuồn cuộn chảy: Hàng triệu phiến lá xanh di động như làn sóng xanh trên mặt đất rừng. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene02",
      "at": "Tốc độ hành quân của những đoàn kiến",
      "layout": "Đồng hồ đo tốc độ hành quân 15m/phút: Đội hình quân binh kiến di chuyển thẳng tắp theo trật tự hoàn hảo. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene02",
      "at": "xa lộ liên tỉnh bằng phẳng",
      "layout": "Xa lộ cao tốc rừng rậm rộng 30cm được các kỹ sư dọn sạch sỏi đá, phẳng phiu như đường băng cao tốc. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },

    # Scene 03 (12 beats)
    {
      "scene": "scene03",
      "at": 0,
      "layout": "Tầng hầm nông nghiệp ngầm: {HERO} bước vào căn phòng nuôi nấm trắng ngà xốp như bọt biển, tay cầm kính lúp.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene03",
      "at": "Loài nấm này mang tên",
      "layout": "Bảng phân loại sinh học: Sợi nấm Leucoagaricus gongylophorus đan xen dày đặc như tấm thảm bông tuyết. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene03",
      "at": "gắn liền với số phận loài kiến",
      "layout": "Vòng tròn liên minh cộng sinh vĩnh cửu 50 triệu năm giữa loài kiến và vườn nấm ngầm. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene03",
      "at": "Quy trình chế biến thức ăn tại đây",
      "layout": "Dây chuyền sản xuất công nghiệp: Kiến thợ nghiền nhỏ lá cây thành hỗn hợp bột mịn tơi xốp. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene03",
      "at": "tẩm ướp các giọt enzyme tiêu hóa",
      "layout": "Các giọt enzyme tiêu hóa đặc hiệu được phun đều lên luống bột lá để chuẩn bị cấy sợi nấm mới. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene03",
      "at": "Sợi nấm sẽ tiêu hóa chất xơ",
      "layout": "Cấu trúc hiển vi: Sợi nấm phân giải cellulose cứng và hình thành những bọc tròn gongylidia giàu dưỡng chất. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene03",
      "at": "Những viên nang dinh dưỡng này",
      "layout": "Kiến thợ cẩn thận mớm những viên nang gongylidia béo ngậy cho các ấu trùng kiến non và kiến chúa. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene03",
      "at": "Loài nấm này phụ thuộc hoàn toàn",
      "layout": "{HERO} ân cần dùng râu chải chuốt và dọn dẹp các sợi nấm già cỗi, biểu tượng người làm vườn tận tụy.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene03",
      "at": "Nhưng để duy trì một vườn nấm khổng lồ",
      "layout": "Khói khí cacbonic tích tụ trong hầm sâu tăm tối, đặt ra bài toán thông gió sinh tử cho cả tổ kiến. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene03",
      "at": "Ước tính mỗi tổ kiến cắt lá tiêu thụ",
      "layout": "Hình ảnh so sánh: Đàn kiến tiêu thụ lá cây tương đương một chú bò sữa ăn cỏ cả năm. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene03",
      "at": "không bao giờ tàn sát một cái cây",
      "layout": "Bản đồ luân chuyển thu hoạch: Đàn kiến chia tuyến khai thác luân phiên nhiều cây rừng để bảo vệ thảm thực vật. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene03",
      "at": "tránh tích tụ độc tố thực vật",
      "layout": "{HERO} kiểm tra kỹ từng mẫu lá đưa vào kho, đảm bảo chất lượng phân bón tinh khiết nhất.",
      "stickers": [],
      "impacts": []
    },

    # Scene 04 (12 beats)
    {
      "scene": "scene04",
      "at": 0,
      "layout": "Phòng điều hành khí động học: {HERO} đứng bên mô hình các giếng thông gió đối lưu tự nhiên không dùng điện.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene04",
      "at": "Vườn nấm ngầm đòi hỏi một môi trường",
      "layout": "Biểu đồ tiêu chuẩn môi trường: Nhiệt độ 25°C và độ ẩm 90% rực sáng trong khung cảnh hầm ngầm. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene04",
      "at": "bất kể bên ngoài mặt đất đang là nắng hạn",
      "layout": "Đối lập thời tiết: Mặt đất nắng cháy gay gắt hoặc bão giông nhưng dưới hầm nấm vẫn mát mẻ êm dịu. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene04",
      "at": "đào đục hàng ngàn giếng thông gió",
      "layout": "Hệ thống giếng đứng vươn lên mặt đất: Giếng trung tâm cao nhô lên như ống khói nhà máy đón gió lộng. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene04",
      "at": "sự chênh lệch áp suất khí quyển",
      "layout": "Mũi tên chênh lệch áp suất: Áp suất thấp ở miệng giếng cao hút mạnh không khí từ dưới đáy hầm. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene04",
      "at": "Hiệu ứng ống khói đối lưu nhiệt",
      "layout": "Dòng khí nóng chứa CO2 màu đỏ bốc lên giếng trung tâm, dòng khí tươi mát giàu O2 màu xanh tràn xuống giếng biên. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene04",
      "at": "Khi nhiệt độ thay đổi",
      "layout": "Đội cơ động kiến thợ khiêng các hòn đất nhỏ chạy đến miệng giếng để đắp thêm hoặc mở rộng van gió. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene04",
      "at": "Nhiều tòa nhà chọc trời tiết kiệm năng lượng",
      "layout": "Tòa nhà chọc trời Eastgate tại Zimbabwe với kiến trúc ống khói phỏng sinh học mô phỏng tổ kiến. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene04",
      "at": "giảm 90% chi phí điện máy lạnh",
      "layout": "Biểu đồ tiết kiệm năng lượng 90%: Hệ thống xanh bền vững lấy cảm hứng từ Đại Công Trình Sư Ngầm. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene04",
      "at": "Và để bảo vệ kỳ quan đô thị này",
      "layout": "{HERO} đứng bên cạnh chú kiến lính hộ vệ khổng lồ bọc thép uy nghi bảo vệ cửa tổ.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene04",
      "at": "Ngay cả trong những trận mưa lũ",
      "layout": "Mưa lũ nhiệt đới xối xả trên mặt đất nhưng các miệng giếng phễu ngược ngăn nước tuyệt đối. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene04",
      "at": "Một bản lĩnh thiết kế thủy lợi",
      "layout": "Mạng lưới cống rãnh ngầm dẫn nước mưa thừa thoát xa khỏi các khoang nuôi nấm trọng yếu. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },

    # Scene 05 (12 beats)
    {
      "scene": "scene05",
      "at": 0,
      "layout": "Khu căn cứ quân sự và y tế: {HERO} đứng trước bảng phân cấp xã hội 4 tầng lớp kiến chuyên môn hóa.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene05",
      "at": "Chẳng có một xã hội động vật nào",
      "layout": "Bốn đẳng cấp kiến xếp hàng theo kích thước: Kiến lính khổng lồ, kiến thợ lớn, kiến thợ nhỏ và kiến y tế tí hon. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene05",
      "at": "Ở vị trí quân đội thường trực",
      "layout": "Kiến lính bọc thép khổng lồ to gấp 300 lần kiến nhỏ, cơ hàm nở rộng như chiếc kìm bấm titan sắc bén. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene05",
      "at": "cắn thủng lớp da giày",
      "layout": "Kiến lính dũng mãnh ngoạm chặt xua đuổi con thú ăn kiến khổng lồ để bảo vệ cửa hầm tổ. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene05",
      "at": "Ngược lại ở vị trí chăm sóc y tế",
      "layout": "Chú kiến siêu tí hon bằng đầu tăm cưỡi trên phiến lá, cầm chổi mini quét sạch bụi bẩn trên lá. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene05",
      "at": "xua đuổi những con ruồi ký sinh phorid",
      "layout": "Kiến tí hon dũng cảm vung râu xua đuổi con ruồi ký sinh phorid đang lượn lờ muốn đẻ trứng. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene05",
      "at": "trên lớp vỏ mai của kiến thợ",
      "layout": "Cận cảnh vỏ mai kiến thợ phủ lớp phấn trắng vi khuẩn Pseudonocardia phát sáng lung linh. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene05",
      "at": "nhà máy sản xuất thuốc kháng sinh",
      "layout": "Các phân tử kháng sinh tự nhiên tiêu diệt tận gốc mầm nấm mốc ký sinh độc hại Escovopsis. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene05",
      "at": "giữ cho trang trại nấm ngầm luôn vô trùng",
      "layout": "Vườn nấm sạch bong vô trùng tuyệt đối, minh chứng cho nền y tế dự phòng 50 triệu năm không lờn thuốc. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene05",
      "at": "Một hệ thống y tế và an ninh",
      "layout": "{HERO} chào quân hàm cùng đội quân kiến lính và đội ngũ y tế tí hon tận tụy.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene05",
      "at": "bảo vệ sự phồn vinh của đế chế ngầm",
      "layout": "Đế chế ngầm phồn vinh rực rỡ với hàng ngàn ánh đèn công trường hoạt động ngày đêm nhộn nhịp. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene05",
      "at": "thử thách khắc nghiệt của mẹ thiên nhiên",
      "layout": "Tổ kiến vững vàng trước mọi biến động thời tiết, sừng sững tồn tại qua hàng triệu năm lịch sử. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },

    # Scene 06 (10 beats)
    {
      "scene": "scene06",
      "at": 0,
      "layout": "Hội đồng thẩm định kiến trúc tự nhiên: {HERO} đứng trên bục vinh danh đón nhận Bằng Chứng Nhận Kỳ Quan Kiến Trúc.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene06",
      "at": "sau khi khảo sát chi tiết toàn bộ năm bản vẽ",
      "layout": "Năm biểu tượng bản vẽ kỹ thuật: Hầm ngầm 8m, hàm cưa siêu âm, vườn nấm 50 triệu năm, thông gió đối lưu và kháng sinh. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene06",
      "at": "hình mẫu kiểu mẫu về nền kinh tế tuần hoàn",
      "layout": "Sơ đồ kinh tế tuần hoàn khép kín: Toàn bộ chất thải được phân hủy tái chế làm màu mỡ đất rừng. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene06",
      "at": "tạo nên thảm thực vật xanh tươi",
      "layout": "Rừng rậm nhiệt đới tươi tốt ngút ngàn nhờ công lao cải tạo đất của hàng triệu đàn kiến ngầm. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene06",
      "at": "Bài học từ loài kiến nhỏ bé",
      "layout": "{HERO} bắt tay cùng người kỹ sư nhân loại, biểu tượng kết nối giữa thiên nhiên và công nghệ.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene06",
      "at": "tinh thần kỷ luật và sự phân công",
      "layout": "Hàng triệu cánh tay kiến và con người cùng chung sức dựng xây những công trình vĩ đại dời non lấp bể. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene06",
      "at": "Giữa hệ thống điều hòa thông gió đối lưu",
      "layout": "Hai màn hình đối chiếu: Giếng thông gió ống khói không điện và hàm răng cưa rung tần số cao. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene06",
      "at": "Hãy để lại ý kiến đóng góp của bạn",
      "layout": "Biểu tượng ô bình luận ý kiến cùng cộng đồng các nhà khoa học và kỹ sư trẻ nhiệt huyết. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene06",
      "at": "nhấn nút Đăng Ký Kênh",
      "layout": "Nút Đăng Ký Kênh rực sáng cùng chiếc chuông thông báo rung động mời gọi khám phá. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene06",
      "at": "Xin chào tạm biệt và hẹn gặp lại",
      "layout": "{HERO} vẫy tay chào tạm biệt khán giả từ cửa công trình ngầm, hẹn gặp lại ở những hành trình tiếp theo.",
      "stickers": [],
      "impacts": []
    }
  ]
}

os.makedirs("projects/tap-40-kien-cat-la/specs", exist_ok=True)
with open("projects/tap-40-kien-cat-la/specs/storyboard.json", "w", encoding="utf-8") as f:
    json.dump(sb, f, ensure_ascii=False, indent=2)

print("Saved storyboard.json for ep40 successfully! Long beats:", len(sb["long"]), "Shorts beats:", len(sb["shorts"]))


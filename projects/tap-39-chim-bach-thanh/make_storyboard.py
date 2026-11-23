# -*- coding: utf-8 -*-
import json
import os

sb = {
  "_doc": "Storyboard cho Tập 39: Chim Bách Thanh — Hồ Sơ Sát Thủ Ngây Thơ Giấu Mặt. Phong cách: Detective Noir Manga & Forensic Crime Scene Sketch.",
  "visual_style": "Detective Noir Manga & Forensic Crime Scene Sketch (phong cách truyện tranh trinh thám manga đen trắng điện ảnh noir kết hợp bản vẽ giám định pháp y hiện trường vụ án, nét mực sắc sảo mạnh mẽ, chi tiết thước dây pháp y màu vàng neon, bảng chứng cứ ghim chỉ đỏ kết nối, vòng tròn phấn trắng hiện trường vụ án, kính lúp quang học phóng to chi tiết; nền trắng tinh sáng sủa phong cách whiteboard explainer, tuyệt đối không chữ rác, không watermark)",
  "style_label": "Detective Noir Manga & Forensic Crime Scene Sketch",
  "characters": {
    "HERO": "chú chim bách thanh (Lanius) hoạt hình phong cách thám tử noir bí ẩn, bộ lông xám trắng thanh lịch, vệt lông đen tuyền vắt ngang mắt như chiếc mặt nạ hiệp sĩ Zorro, chiếc mỏ móc câu cong sắc bén, ánh mắt suy luận sắc sảo và thông minh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền",
    "HERO_S": "chú chim bách thanh nhỏ nhắn đeo mặt nạ đen Zorro và mỏ móc câu",
    "NO_HERO": "KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này"
  },
  "side_characters": {},
  "shorts_side_characters": {},
  "shorts_title_lines": [
    "SÁT THỦ NGÂY THƠ",
    "BÍ ẨN CÀNH GAI XUYÊN THÂM?!"
  ],
  "skip_numbers": [],
  "shorts": [
    {
      "at": 0,
      "layout": "Khung cảnh mở đầu trinh thám noir: {HERO} đứng trên cành cây với ánh mắt sắc lẹm, bên cạnh là biểu tượng hồ sơ mật vụ án màu vàng neon.",
      "stickers": [],
      "impacts": []
    },
    {
      "at": "Đó chính là Chim Bách Thanh",
      "layout": "Cận cảnh chân dung {HERO} với dải lông đen vắt ngang mắt như mặt nạ hiệp sĩ Zorro huyền bí, bộ lông xám bạc sang trọng.",
      "stickers": [],
      "impacts": []
    },
    {
      "at": "Bí mật rợn người nằm ở chiếc mỏ",
      "layout": "Bản vẽ phân tích pháp y: Chiếc mỏ chim quặp xuống như móc câu sắt với hai chiếc mấu răng xương nhọn hoắt được khoanh tròn bằng mực đỏ. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "at": "hai mấu răng xương sắc bén",
      "layout": "Hình ảnh kính lúp quang học phóng đại cấu trúc mấu răng tomial tooth sắc lẹm của chim bách thanh. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "at": "bẻ gãy đốt sống cổ con mồi",
      "layout": "Sơ đồ động lực học: Mỏ cắm phập vào khoảng hở giữa hai đốt sống cổ con mồi và bẻ gãy tủy sống trong chớp mắt. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "at": "Vì đôi chân chim sẻ quá yếu",
      "layout": "So sánh pháp y đối lập: Đôi bàn chân chim sẻ mảnh khảnh của {HERO} bên cạnh bàn chân móng vuốt đại bàng khổng lồ.",
      "stickers": [],
      "impacts": []
    },
    {
      "at": "sáng tạo ra một tuyệt chiêu độc nhất",
      "layout": "{HERO} nở nụ cười thám tử đắc thắng, chỉ mỏ về phía cành cây gai nhọn hoắt ven bìa rừng.",
      "stickers": [],
      "impacts": []
    },
    {
      "at": "Xiên thủng xác con mồi",
      "layout": "Hiện trường cành cây gai nhọn hoắt cắm xuyên qua xác con mồi làm điểm tựa cơ học giữa không trung. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "at": "làm điểm tựa xé thịt",
      "layout": "{HERO} thong thả dùng mỏ móc câu xé từng thớ thịt từ con mồi đã bị cố định cứng trên cành gai.",
      "stickers": [],
      "impacts": []
    },
    {
      "at": "Thậm chí những con cào cào cực độc",
      "layout": "Mẫu vật pháp y: Chú cào cào lubber khổng lồ sọc vàng đen chứa chất độc cardenolide nguy hiểm. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "at": "treo gai phơi nắng suốt 48 giờ",
      "layout": "Dãy cào cào bị xiên phơi nắng dưới ánh mặt trời rực rỡ, đồng hồ đếm ngược 48 giờ giải phóng độc tố. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "at": "Thật là một sát thủ trinh thám thiên tài",
      "layout": "{HERO} đứng kiêu hãnh trên cành cây cao giữa ánh hoàng hôn, biểu tượng thám tử Sherlock Holmes của rừng sâu.",
      "stickers": [],
      "impacts": []
    }
  ],
  "long": [
    # Scene 01
    {
      "scene": "scene01",
      "at": 0,
      "layout": "Phòng điều tra trọng án sinh thái: {HERO} trong vai thám tử trưởng chỉ gậy vào bảng chứng cứ gắn đầy ảnh và chỉ đỏ.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene01",
      "at": "phòng điều tra trọng án sinh thái",
      "layout": "Cận cảnh tập hồ sơ tuyệt mật màu nâu đề chữ Tuyệt Mật và dấu vân tay hiện trường vụ án bí ẩn. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene01",
      "at": "giải mã hiện trường",
      "layout": "Bóng đen bí ẩn mang mặt nạ hiệp sĩ Zorro lướt qua màn sương đêm bìa rừng u ám. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene01",
      "at": "Một vụ án hóc búa",
      "layout": "{HERO} ngồi chống cằm suy tư bên bàn làm việc đầy hồ sơ và kính lúp quang học kiểu trinh thám cổ điển.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene01",
      "at": "Hãy nhìn vào cành cây mận gai",
      "layout": "Hiện trường bìa rừng: Bụi cây mận gai cằn cỗi với những nhánh gai nhọn dài lởm chởm trong sương mù. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene01",
      "at": "Một hiện trường rùng rợn",
      "layout": "Vòng tròn phấn trắng và thước dây pháp y vàng neon bao quanh cành cây có những chiếc gai nhọn 5cm sắc lẹm. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene01",
      "at": "hàng loạt con mồi từ thằn lằn",
      "layout": "Xác thằn lằn, chuột đồng và chim sẻ nhỏ bị xiên treo lơ lửng trên các cành gai nhọn ven đường. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene01",
      "at": "xiên thủng qua cổ hoặc ức",
      "layout": "Cận cảnh giám định pháp y: Đầu gai nhọn cắm xuyên qua gáy con mồi chuẩn xác đến từng mi-li-mét. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene01",
      "at": "Thưa Thanh tra trưởng",
      "layout": "Cô trợ lý pháp y đeo kính trắng cầm bảng kẹp hồ sơ báo cáo kết quả khám nghiệm hiện trường. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene01",
      "at": "Một quan sát hiện trường",
      "layout": "Sơ đồ giải phẫu hiển vi cho thấy đốt sống cổ bị bẻ gãy gập bằng một lực cắt chớp nhoáng không tì vết. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene01",
      "at": "Thủ phạm của vụ án liên hoàn",
      "layout": "{HERO} xuất hiện trong vùng sáng đèn rọi, ánh mắt sắc bén lấp lánh sau dải lông đen ngang mắt.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene01",
      "at": "thuộc họ Laniidae",
      "layout": "Bảng chân dung truy nã pháp y: Chú chim bách thanh họ Laniidae với danh xưng Sát Thủ Đồ Tể Lừng Danh.",
      "stickers": [],
      "impacts": []
    },

    # Scene 02
    {
      "scene": "scene02",
      "at": 0,
      "layout": "Phòng giải phẫu cơ học: {HERO} đứng bên cạnh mô hình kính hiển vi điện tử chiếu rọi cấu trúc đầu chim.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene02",
      "at": "Đây chính là vũ khí đoạt mạng",
      "layout": "Mô hình 3D chiếc mỏ sát thủ phóng to với các tia laser đo đạc lực cắn và góc uốn cong nguy hiểm. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene02",
      "at": "tiến hóa theo hướng của các loài",
      "layout": "Bản vẽ so sánh: Chiếc mỏ bách thanh mang cấu trúc thu nhỏ của chim ưng và chim cắt dũng mãnh. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene02",
      "at": "Đầu mỏ trên uốn cong",
      "layout": "Cận cảnh đầu mỏ trên uốn quặp xuống như móc câu sắt bằng thép tôi luyện đen nhánh. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene02",
      "at": "Hai mấu răng xương nhọn hoắt",
      "layout": "Phóng to hai mấu răng xương tomial tooth sắc nhọn ở hai bên rìa mỏ trên với mũi tên chỉ thị vàng neon. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene02",
      "at": "Khi lao xuống tấn công con mồi",
      "layout": "{HERO} lao bổ nhào từ cành cây cao xuống như một mũi tên xé gió với đôi cánh khép gọn.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene02",
      "at": "không cắn bừa bãi vào thân xác",
      "layout": "Tâm ngắm chữ thập màu đỏ khóa chặt vào gáy và sau hộp sọ của con chuột đồng đang gặm cỏ. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene02",
      "at": "Hai chiếc mấu răng tomial tooth sẽ cắm",
      "layout": "Khoảnh khắc mấu răng tomial tooth cắm phập vào khe hở giữa hai đốt sống cổ tạo lực đòn bẩy cực đại. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene02",
      "at": "bẻ gãy tủy sống con mồi",
      "layout": "Đồng hồ bấm giờ điện tử ghi nhận 0.1 giây: Đốt sống cổ đứt lìa hoàn toàn, con mồi mất tri giác. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene02",
      "at": "Con mồi lập tức bị liệt toàn thân",
      "layout": "{HERO} đứng trên con mồi đã bất động hoàn toàn, thể hiện độ chính xác tuyệt đối không tốn sức.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene02",
      "at": "Thế nhưng sau khi hạ gục con mồi",
      "layout": "{HERO} đứng gãi đầu nhìn con mồi nặng bằng chính mình, đối mặt với bài toán cơ học nan giải.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene02",
      "at": "Lực cắn đo được từ cơ hàm",
      "layout": "Biểu đồ cột so sánh: Lực cắn cơ hàm chim bách thanh cao gấp 3 lần chim cùng kích cỡ. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },

    # Scene 03
    {
      "scene": "scene03",
      "at": 0,
      "layout": "Khu vực trưng bày vũ khí số 2: {HERO} đứng cạnh cành cây gai bồ kết khổng lồ với nụ cười bí ẩn.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene03",
      "at": "Tại sao chim bách thanh phải xiên",
      "layout": "Dấu chấm hỏi lớn màu đỏ trên nền cành gai nhọn hoắt cắm xác con mồi giữa sương mù. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene03",
      "at": "Các loài chim săn mồi thực thụ",
      "layout": "Bàn chân đại bàng lực lưỡng với những móng vuốt cong vút ghim chặt con mồi xuống tảng đá. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene03",
      "at": "Thế nhưng nghi phạm của chúng ta",
      "layout": "Cận cảnh bàn chân chim sẻ mảnh khảnh của {HERO} với các ngón nhỏ chỉ đủ để đậu cành cây.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene03",
      "at": "Các ngón chân mảnh khảnh",
      "layout": "Hình ảnh con thằn lằn trơn trượt tuột khỏi đôi bàn chân nhỏ bé không có móng quắp. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene03",
      "at": "Để giải quyết nghịch lý cơ học này",
      "layout": "{HERO} nảy ra ý tưởng phát minh thông minh, bóng đèn sáng rực trên đầu trong phòng thí nghiệm rừng.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene03",
      "at": "Nó tha xác con mồi đến những bụi cây",
      "layout": "{HERO} ngậm xác con mồi bay đến hàng rào dây thép gai và bụi mận gai nhọn hoắt.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene03",
      "at": "Nó dùng toàn lực cắm phập xác nạn nhân",
      "layout": "{HERO} dùng toàn lực ấn mạnh xác con mồi ghim chặt vào chiếc đinh gai nhọn như chiếc kẹp bàn thợ cơ khí.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene03",
      "at": "thong thả dùng chiếc mỏ móc câu",
      "layout": "{HERO} nhàn nhã dùng mỏ móc xé từng miếng thịt nhỏ khi con mồi đã bị cố định vững chắc trên gai.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene03",
      "at": "Một bằng chứng hùng hồn",
      "layout": "Bản vẽ phỏng sinh học: Chiếc gai nhọn biến thành cánh tay đòn cơ học ngoại vi thiên tài. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene03",
      "at": "Đáng kinh ngạc hơn nữa",
      "layout": "Bản đồ vệ tinh lãnh thổ rừng với hàng trăm điểm đánh dấu cành gai được lưu trữ trong trí nhớ của {HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene03",
      "at": "Gai mảnh cho thằn lằn và cào cào",
      "layout": "Sơ đồ kho bãi tự nhiên: Phân loại gai mảnh cho cào cào và gai chạc ba cho chuột đồng béo ngậy. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },

    # Scene 04
    {
      "scene": "scene04",
      "at": 0,
      "layout": "Phòng hóa nghiệm sinh hóa: {HERO} đeo kính bảo hộ bên cạnh các ống nghiệm chứa chất độc màu tím và xanh lục.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene04",
      "at": "Đó là những chú cào cào lubber khổng lồ",
      "layout": "Cận cảnh chú cào cào lubber khổng lồ thân màu vàng sọc đen bóng bẩy nằm dưới kính lúp. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene04",
      "at": "loài cào cào này tích tụ hàm lượng chất độc",
      "layout": "Công thức hóa học cardenolide phát sáng cảnh báo nguy hiểm độc tố làm ngừng tim. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene04",
      "at": "Mọi loài chim săn mồi khác",
      "layout": "Các chú chim rừng khác sợ hãi bay dạt ra xa khi thấy chú cào cào độc lubber. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene04",
      "at": "xiên chúng lên cành gai nhọn hoắt",
      "layout": "{HERO} thản nhiên ghim chú cào cào độc lên cành gai cao nhất phơi dưới ánh nắng mặt trời rực rỡ.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene04",
      "at": "Bí mật nằm ở chỗ",
      "layout": "Tia nắng mặt trời và những luồng gió tự nhiên phá vỡ chuỗi phân tử độc tố cardenolide. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene04",
      "at": "sau khoảng 48 giờ đến 72 giờ",
      "layout": "Đồng hồ cát điện tử đếm ngược từ 48 giờ đến 72 giờ: Độc tố giảm dần về 0%. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene04",
      "at": "Chú chim bách thanh kiên nhẫn chờ đợi",
      "layout": "{HERO} đeo khăn ăn cầm dao nĩa phong cách ẩm thực, thưởng thức món cào cào khô đã sạch độc tố.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene04",
      "at": "Đây chẳng khác nào quy trình ủ thực phẩm",
      "layout": "Bếp trưởng ẩm thực rừng xanh: Quy trình ủ men và phơi thịt bò khô của tự nhiên hoang dã. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene04",
      "at": "Vừa là kho lương thực chống đói",
      "layout": "Cành gai phủ đầy tuyết trắng mùa đông treo các gói mồi khô thơm ngon làm lương thực dự trữ. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene04",
      "at": "Trong mùa sinh sản vào mùa xuân",
      "layout": "{HERO} tự hào đứng cạnh hàng rào gai treo đầy thức ăn béo ngậy để khoe tài năng.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene04",
      "at": "Những chú chim mái sẽ bay đi kiểm tra",
      "layout": "Cô chim bách thanh mái bay qua chấm điểm hàng rào gai đầy ắp mồi và gật đầu hài lòng. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },

    # Scene 05
    {
      "scene": "scene05",
      "at": 0,
      "layout": "Hiện trường phục kích: {HERO} nấp sau tán lá rậm rạp, chiếc micro thu âm âm thanh rung động.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene05",
      "at": "chúng ta không thể bỏ qua ngón đòn",
      "layout": "Bản vẽ phân tích tâm lý con mồi với các nốt nhạc ma thuật quyến rũ bay lơ lửng. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene05",
      "at": "chim bách thanh sở hữu thanh quản",
      "layout": "Sơ đồ giải phẫu thanh quản syrinx linh hoạt của {HERO} phát ra những dải sóng âm đa dạng.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene05",
      "at": "Khi đi săn nó sẽ nấp kín",
      "layout": "{HERO} hòa mình hoàn hảo vào vòm lá xanh, chỉ để lộ đôi mắt quan sát sắc lạnh.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene05",
      "at": "giả dạng tiếng chim sẻ non",
      "layout": "Tiếng chim sẻ non nỉ non cầu cứu vang lên từ bụi cây, dụ dỗ những chú chim sẻ tò mò. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene05",
      "at": "Những chú chim nhỏ ngây thơ nghe thấy",
      "layout": "Đàn chim sẻ nhỏ mất cảnh giác bay chầm chậm lại gần bụi cây tìm bạn đồng hành. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene05",
      "at": "Thưa Thanh tra nghĩa là nó dùng",
      "layout": "Cô trợ lý pháp y giật mình kinh ngạc chỉ vào sơ đồ âm thanh bẫy mồi xảo quyệt. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene05",
      "at": "Chính xác 100%",
      "layout": "Vạch đo khoảng cách: Con mồi tiến vào vùng nguy hiểm tử thần dưới 2 mét. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene05",
      "at": "lao ra như một mũi tên xé gió",
      "layout": "{HERO} phóng ra như tia chớp, chiếc mỏ khóa chặt sau gáy con mồi trong chớp mắt.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene05",
      "at": "Từ chiếc mặt nạ đen ngụy trang",
      "layout": "Bảng tổng hợp chiến thuật: Mặt nạ noir, mỏ móc bẻ cổ, cành gai cố định và âm thanh ngụy trang.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene05",
      "at": "Cơ quan phát âm syrinx của chim bách thanh",
      "layout": "Mô hình hai luồng khí độc lập trong cơ quan syrinx tạo hai âm điệu hòa âm cùng một lúc. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene05",
      "at": "khiến ngay cả những kẻ quan sát",
      "layout": "Các nhà điểu học đeo ống nhòm bị đánh lừa bởi tiếng hót ngọt ngào phát ra từ bụi gai. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },

    # Scene 06
    {
      "scene": "scene06",
      "at": 0,
      "layout": "Khép lại hồ sơ vụ án: {HERO} đứng trên bục vinh danh với huy hiệu thám tử vàng sáng chói.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene06",
      "at": "sau khi làm rõ toàn bộ bốn bằng chứng",
      "layout": "Bốn biểu tượng vàng: Mỏ móc câu, cành gai trợ lực, kho lọc độc 48 giờ và tiếng hót thiên tài. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene06",
      "at": "Dù thói quen xiên mồi lên cành gai",
      "layout": "Cánh đồng cỏ xanh mướt thanh bình được bảo vệ khỏi nạn chuột đồng và sâu bệnh phá hoại. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene06",
      "at": "giữ cho cán cân tự nhiên luôn ở trạng thái",
      "layout": "Biểu tượng chiếc cân công lý sinh thái cân bằng giữa các loài sinh vật trong tự nhiên. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene06",
      "at": "Đừng bao giờ đánh giá một sinh vật",
      "layout": "{HERO} nháy mắt tinh nghịch, thông điệp bài học cuộc sống hiện lên lấp lánh.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene06",
      "at": "Trong cuộc sống cũng vậy",
      "layout": "Bàn tay con người vươn tới thành công bằng trí tuệ và sự tận dụng nguồn lực xung quanh. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene06",
      "at": "Giữa kỹ thuật bẻ cổ bằng mấu răng",
      "layout": "Hai màn hình đối chiếu: Cú cắn bẻ tủy sống siêu tốc và cành gai giải trừ độc tố kỳ diệu. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene06",
      "at": "Hãy chia sẻ suy luận phá án của bạn",
      "layout": "Biểu tượng khung bình luận trò chuyện cùng cộng đồng thám tử suy luận sắc sảo. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene06",
      "at": "nhấn nút Đăng Ký Kênh",
      "layout": "Nút Đăng Ký Kênh màu đỏ rực cùng chiếc chuông thông báo rung chuyển sống động. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene06",
      "at": "Tập 40: Khám phá siêu kiến trúc quân sự",
      "layout": "Trailer hé lộ Tập 40: Đội quân Kiến Cắt Lá hùng hậu hành quân mang lá xanh trong rừng rậm nhiệt đới.",
      "stickers": [],
      "impacts": []
    }
  ]
}

os.makedirs("projects/tap-39-chim-bach-thanh/specs", exist_ok=True)
with open("projects/tap-39-chim-bach-thanh/specs/storyboard.json", "w", encoding="utf-8") as f:
    json.dump(sb, f, ensure_ascii=False, indent=2)

print("Saved storyboard.json for ep39 successfully! Long beats:", len(sb["long"]), "Shorts beats:", len(sb["shorts"]))

# -*- coding: utf-8 -*-
"""Generate specs/storyboard.json for Tap 35: Ca Voi Sat Thu."""
import json
from pathlib import Path

storyboard_data = {
  "_doc": "Storyboard Tập 35 — Cá Voi Sát Thủ (Orcinus orca) F6 Bố Già Đại Dương. Chạy: python src/episode/build_plans.py projects/tap-35-ca-voi-sat-thu",
  "visual_style": "tỉ lệ {AR}; phong cách Oceanic Syndicate & Nautical Tattoo Art (băng đảng Mafia đại dương kết hợp tranh khắc cổ điển hàng hải, nét vẽ mực đen-trắng tương phản cao sắc lạnh, chi tiết vàng hoàng gia và đỏ ruby sang trọng, sóng biển cuộn xoáy phong cách cổ điển); NỀN TRẮNG TINH hoàn toàn, không watermark, không logo; chủ thể nằm gọn trong khung, chừa lề trắng",
  "style_label": "Oceanic Syndicate & Nautical Tattoo Art",
  "characters": {
    "HERO": "chú Cá Voi Sát Thủ Orca hoạt hình oai phong lẫm liệt, khoác áo vest măng tô đen Bố Già Mafia sọc kim cương sang trọng, trên đầu đội vương miện mạ vàng nhỏ lệch bên, mắt đeo kính râm đen cực ngầu (cute stylish cartoon Orca killer whale mafia boss wearing a sleek dark pinstripe suit, small golden crown, and cool sunglasses)",
    "HERO_S": "chú Cá Voi Sát Thủ Orca Bố Già mặc vest đen và đội vương miện vàng",
    "NO_HERO": "KHÔNG có Cá Voi Sát Thủ trong cảnh này",
    "MATRIARCH": "Nữ Hoàng Bố Già Cá Voi Sát Thủ khổng lồ đeo chuỗi ngọc trai biển và vương miện cổ đại uy quyền",
    "SEAL": "chú hải cẩu béo tròn ngơ ngác đeo kính râm nằm tắm nắng trên tảng băng trôi",
    "SHARK": "chúa tể cá mập trắng to lớn hung dữ nhưng vẻ mặt đang hoảng loạn tột độ tháo chạy",
    "TAHLEQUAH": "người mẹ cá voi sát thủ Tahlequah ánh mắt chan chứa tình mẫu tử đang dùng trán nâng đứa con bé bỏng"
  },
  "side_characters": [
    "MATRIARCH",
    "SEAL",
    "SHARK",
    "TAHLEQUAH"
  ],
  "shorts_side_characters": [
    "SHARK"
  ],
  "shorts_title_lines": [
    "ĐẾ CHẾ MAFIA:",
    "CÁ VOI SÁT THỦ!"
  ],
  "skip_numbers": [],
  "long": [
    # Scene 01
    {
      "scene": "scene01",
      "at": 0,
      "layout": "Đại dương sâu thẳm mở ra với cánh cổng Mafia huyền bí: {HERO} đứng sừng sững ở vị trí trung tâm, hai tay đút túi áo vest, toát lên phong thái quyền lực tuyệt đối. {NO_HERO}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene01",
      "at": "quyền lực gia tộc tuyệt đối",
      "layout": "Cận cảnh ánh mắt sắc lạnh đeo kính râm của {HERO}, phản chiếu hình ảnh muôn loài sinh vật biển đang cúi mình kính cẩn trước Bố Già.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene01",
      "at": "Người ta thường gọi chúng là Cá Voi Sát Thủ",
      "layout": "Sơ đồ giải phẫu kích thước khổng lồ: {HERO} bơi ngang thước đo 9 mét và cán cân 6 tấn, bên cạnh là một chú cá heo nhỏ bé để so sánh độ tương phản kích cỡ.",
      "stickers": [
        {"text": "9 mét", "sub": "chiều dài cơ thể", "style": "rect", "color": "orange", "x": 0.22, "y": 0.20},
        {"text": "6 tấn", "sub": "trọng lượng áp đảo", "style": "pill", "color": "blue", "x": 0.78, "y": 0.22, "target": {"x": 0.65, "y": 0.45}}
      ],
      "impacts": []
    },
    {
      "scene": "scene01",
      "at": "dưới đáy đại dương",
      "layout": "Bản đồ gia phả Mafia đại dương vẽ theo phong cách gia tộc cổ điển: {MATRIARCH} uy nghi tọa lạc ở đỉnh cao nhất, xung quanh là các thế hệ con cháu quy phục.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene01",
      "at": "quyền lực tối cao thuộc về các Nữ Hoàng Bố Già",
      "layout": "Chân dung tráng lệ của {MATRIARCH}: Thọ 90 năm, ánh mắt thông tuệ nắm giữ tấm bản đồ hải lưu bí truyền dẫn đường cho cả gia tộc vượt bão tố.",
      "stickers": [
        {"text": "90 năm", "sub": "tuổi thọ Nữ Hoàng", "style": "rect", "color": "green", "x": 0.80, "y": 0.25}
      ],
      "impacts": []
    },
    {
      "scene": "scene01",
      "at": "những gã đực cá voi sát thủ",
      "layout": "Cảnh tượng hài hước ấm áp: Một gã cá voi đực to lớn lực lưỡng cao 9 mét nhưng bơi nép sát bên cạnh cá voi mẹ, ngoan ngoãn lắng nghe lời dạy bảo.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene01",
      "at": "vây lưng của những gã đực",
      "layout": "Chiếc vây lưng hình tam giác khổng lồ cao 2 mét của {HERO} nhô thẳng đứng khỏi mặt nước biển rẽ sóng, bên cạnh là đồng hồ đo tốc độ 55 km/h rực lửa.",
      "stickers": [
        {"text": "2 mét", "sub": "chiều cao vây lưng", "style": "rect", "color": "orange", "x": 0.25, "y": 0.20},
        {"text": "55 km/h", "sub": "tốc độ tối đa", "style": "pill", "color": "red", "x": 0.75, "y": 0.22}
      ],
      "impacts": []
    },
    {
      "scene": "scene01",
      "at": "không có bất kỳ mục tiêu nào",
      "layout": "Toàn cảnh gia tộc cá voi sát thủ bơi rẽ sóng đại dương, {HERO} dẫn đầu giương cao lá cờ gia huy mạ vàng quyền lực.",
      "stickers": [],
      "impacts": []
    },

    # Scene 02
    {
      "scene": "scene02",
      "at": 0,
      "layout": "Cảnh tượng băng giá Nam Cực trắng xóa: {SEAL} đang nằm phơi bụng sưởi nắng trên một tảng băng trôi kiên cố, vẻ mặt lười biếng tận hưởng cuộc sống.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene02",
      "at": "không bao giờ lao vào húc bừa bãi",
      "layout": "Dưới làn nước biển trong vắt: {HERO} cùng 3 thành viên gia tộc bơi dàn hàng ngang tàng hình như một phi đội máy bay tiêm kích, giữ cự ly thẳng tắp.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene02",
      "at": "Nước dâng tới cổ là còn may đấy",
      "layout": "Sơ đồ khí động học sóng biển: 4 chiếc đuôi khổng lồ quạt mạnh đồng bộ dưới nước, đẩy lên một luồng áp suất cực đại hướng thẳng về phía tảng băng.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene02",
      "at": "Cột sóng quét ngang làm nứt đôi tảng băng",
      "layout": "Cơn sóng thần dâng cao đánh sập mép băng: Tảng băng nứt toác làm đôi, {SEAL} hoảng hốt trượt chân rơi thẳng xuống mặt nước sủi bọt trắng xóa.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene02",
      "at": "không hề có bất kỳ sự tranh giành",
      "layout": "Vòng tròn gia đình kỷ luật: {HERO} cùng các thành viên nhẹ nhàng vây quanh con mồi, chia sẻ thức ăn theo đúng tôn ti trật tự gia tộc.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene02",
      "at": "các sát thủ trưởng thành sẽ dùng mõm",
      "layout": "Lớp học săn mồi của Bố Già: {HERO} dùng mõm đẩy nhẹ chú hải cẩu lên mép băng để hướng dẫn 2 chú cá voi con tập bơi tạo sóng lần hai.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene02",
      "at": "trường học huấn luyện quân sự thực thụ",
      "layout": "Bảng tổng kết chiến thuật sóng thần Nam Cực: Sơ đồ tác chiến phối hợp 4 bước hoàn hảo của Bố Già Đại Dương.",
      "stickers": [],
      "impacts": []
    },

    # Scene 03
    {
      "scene": "scene03",
      "at": 0,
      "layout": "Bức tranh châm biếm Hollywood: {SHARK} với hàm răng nhọn hoắt đang nhìn thấy bóng lưng đen trắng của {HERO} liền toát mồ hôi hột run rẩy.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene03",
      "at": "cá mập trắng khét tiếng chỉ là một món ăn vặt",
      "layout": "Bàn tiệc Mafia sang trọng dưới đáy biển: {HERO} đeo khăn ăn kẻ sọc, tay cầm nĩa chỉ vào mô hình lá gan cá mập béo ngậy.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene03",
      "at": "vùng vịnh Gansbaai ở Nam Phi",
      "layout": "Hiện trường bờ biển vịnh Gansbaai: Dấu vết hiện trường được căng dây phong tỏa vàng đen, xác cá mập dạt vào bờ với duy nhất một vết rách phẫu thuật.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene03",
      "at": "bộ đôi sát thủ lừng danh mang tên Port và Starboard",
      "layout": "Chân dung bộ đôi sát thủ Port và Starboard: Hai chú cá voi với chiếc vây lưng cong đặc trưng đang phối hợp kẹp chặt {SHARK}.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene03",
      "at": "cú húc lật ngửa con cá mập",
      "layout": "Cơ chế bất động trương lực học: {SHARK} bị lật ngửa bụng lên trời, hai mắt đờ đẫn rơi vào trạng thái hôn mê ngạt thở hoàn toàn không thể phản kháng.",
      "stickers": [
        {"text": "Bất động trương lực", "sub": "tê liệt phản xạ", "style": "pill", "color": "red", "x": 0.50, "y": 0.20}
      ],
      "impacts": []
    },
    {
      "scene": "scene03",
      "at": "rạch một đường chính xác đến từng milimét",
      "layout": "Vết cắt phẫu thuật hoàn hảo: Chiếc vây ngực cá mập được rạch chuẩn xác, buồng gan khổng lồ nặng hàng trăm kg được lấy ra nguyên vẹn.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene03",
      "at": "quần thể cá mập trắng tại vùng biển Nam Phi khiếp vía",
      "layout": "Bản đồ radar sơ tán đại dương: Hàng chục chú cá mập trắng gắn máy định vị bơi tháo chạy tán loạn ra khỏi vịnh Nam Phi.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene03",
      "at": "thống trị tuyệt đối về mặt tâm lý",
      "layout": "Ngai vàng đáy biển: {HERO} uy nghiêm ngự trị trên mỏm đá ngầm, bên dưới là vùng biển sạch bóng cá mập trắng suốt cả năm trời.",
      "stickers": [],
      "impacts": []
    },

    # Scene 04
    {
      "scene": "scene04",
      "at": 0,
      "layout": "Hai gia tộc cá voi đối mặt nhưng không hòa lẫn: Gia tộc ven bờ đội mũ đầu bếp cá hồi, gia tộc du cư khoác áo lông thú săn mồi oai vệ.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene04",
      "at": "mỗi chi nhánh đều giữ gìn danh dự",
      "layout": "Thực đơn ẩm thực gia truyền: Bảng menu khắc gỗ hiển thị thực đơn cá hồi thượng hạng của dòng tộc ven bờ đối lập với thực đơn hải cẩu của dòng tộc du cư.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene04",
      "at": "hệ thống phương ngữ âm thanh độc nhất",
      "layout": "Sóng âm thanh phổ học: Tần số sóng âm tiếng lách cách và huýt sáo của {HERO} hiển thị thành các nốt nhạc mật mã Mafia độc bản.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene04",
      "at": "những âm thanh lách cách và tiếng huýt sáo",
      "layout": "Cảnh tượng hài hước: Chú cá voi gia tộc hàng xóm đeo tai nghe dịch thuật nhưng trên đầu hiện ra vô số dấu hỏi chấm vì không hiểu tiếng lóng.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene04",
      "at": "học tập từng ngữ điệu âm thanh",
      "layout": "Trường học ngôn ngữ gia đình: {HERO} kiên nhẫn phát âm từng tần số sóng siêu âm để dạy cho chú cá con đang chăm chú lắng nghe.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene04",
      "at": "đa văn hóa vô cùng phong phú",
      "layout": "Bản đồ văn hóa các dòng tộc đại dương: Biểu đồ phân bố các vùng lãnh thổ và phương ngữ độc lập của các gia tộc Bố Già trên toàn cầu.",
      "stickers": [],
      "impacts": []
    },

    # Scene 05
    {
      "scene": "scene05",
      "at": 0,
      "layout": "Sơ đồ não bộ 5kg phát sáng: Hình ảnh đồ họa cấu tạo hệ thần kinh thùy paralimbic phân nhánh phức tạp hơn não bộ con người.",
      "stickers": [
        {"text": "5 kilôgam", "sub": "trọng lượng não bộ", "style": "rect", "color": "blue", "x": 0.25, "y": 0.20},
        {"text": "Paralimbic", "sub": "thùy cảm xúc siêu việt", "style": "pill", "color": "green", "x": 0.75, "y": 0.22}
      ],
      "impacts": []
    },
    {
      "scene": "scene05",
      "at": "sự thấu cảm, lòng vị tha",
      "layout": "Cận cảnh ánh mắt sâu thẳm chan chứa tình cảm của {HERO}, toát lên vẻ trầm tư và lòng trắc ẩn của những kẻ cai trị có tâm hồn.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene05",
      "at": "câu chuyện cảm động về người mẹ Tahlequah",
      "layout": "Bức tranh lay động triệu trái tim: {TAHLEQUAH} dùng trán nâng đứa con bé bỏng bơi giữa biển Thái Bình Dương mênh mông bão tuyết.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene05",
      "at": "bơi ròng rã suốt mười bảy ngày",
      "layout": "Hành trình 17 ngày và 1.000 dặm: Bản đồ hải trình di chuyển của {TAHLEQUAH} cùng sự hộ tống sát cánh của toàn bộ các thành viên trong bầy đàn.",
      "stickers": [
        {"text": "17 ngày", "sub": "hành trình tang tóc", "style": "rect", "color": "orange", "x": 0.22, "y": 0.20},
        {"text": "1.000 dặm", "sub": "quãng đường vượt biển", "style": "pill", "color": "blue", "x": 0.78, "y": 0.22}
      ],
      "impacts": []
    },
    {
      "scene": "scene05",
      "at": "nhường thức ăn và hỗ trợ người mẹ",
      "layout": "Sự đoàn kết gia đình: Các thành viên bơi song song mang thức ăn tiếp tế cho người mẹ đau thương, chia sẻ nỗi mất mát thiêng liêng.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene05",
      "at": "giai đoạn mãn kinh",
      "layout": "Tôn vinh thế hệ bà ngoại: Hình ảnh người bà cá voi già 80 tuổi hiền từ đang bơi cùng đàn cháu nhỏ, truyền thụ bí kíp sinh tồn của dòng tộc.",
      "stickers": [],
      "impacts": []
    },

    # Scene 06
    {
      "scene": "scene06",
      "at": 0,
      "layout": "Cán cân so sánh sức mạnh: Một bên là hình ảnh {HERO} dễ dàng quật ngã cá voi xanh khổng lồ 40 tấn, bên kia là hình ảnh con người nhỏ bé trên thuyền buồm.",
      "stickers": [
        {"text": "40 tấn", "sub": "sức mạnh hạ gục con mồi", "style": "rect", "color": "red", "x": 0.25, "y": 0.20}
      ],
      "impacts": []
    },
    {
      "scene": "scene06",
      "at": "chưa từng ghi nhận một vụ tấn công giết người",
      "layout": "Bản hiệp ước hòa bình cổ xưa: Cuộn giấy da cổ khắc điều khoản liên minh giữa Bố Già Đại Dương và loài người hai chân.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene06",
      "at": "hợp tác cùng các ngư dân vịnh Eden",
      "layout": "Huyền thoại vịnh Eden nước Úc: Cá voi sát thủ Old Tom dẫn đầu bầy đàn quẫy đuôi báo hiệu cho thuyền ngư dân ra khơi hợp tác đánh bắt.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene06",
      "at": "tò mò bơi sát mạn thuyền",
      "layout": "Khung cảnh thanh bình: {HERO} ngoi đầu khỏi mặt nước trong xanh, mỉm cười hiền hòa vẫy vây chào người chèo thuyền kayak.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene06",
      "at": "bản hiệp ước bí ẩn và luật ngầm tối cao",
      "layout": "Tượng đài vinh danh Bố Già Đại Dương: {HERO} đội vương miện đứng giữa đại dương bao la, ngẩng cao đầu tự hào về nền văn minh biển cả.",
      "stickers": [],
      "impacts": []
    },
    {
      "scene": "scene06",
      "at": "đón xem Tập ba mươi sáu",
      "layout": "Teaser Tập 36 hấp dẫn: Hình ảnh chú Chim Gõ Kiến ngầu lòi đeo kính bảo hộ cơ khí, cầm búa đập đầu vào thân cây gỗ tạo sóng xung kích.",
      "stickers": [],
      "impacts": []
    }
  ],
  "shorts": [
    {
      "at": 0,
      "layout": "Chúa tể cá mập trắng kinh hoàng tháo chạy: {SHARK} toát mồ hôi hột bỏ chạy tán loạn khi nhìn thấy bóng đen khổng lồ dưới biển.",
      "stickers": [],
      "impacts": []
    },
    {
      "at": "Cá Voi Sát Thủ",
      "layout": "Bóng đen bí ẩn lộ diện: {HERO_S} lướt qua ống kính máy quay với ánh mắt lạnh lùng của một Bố Già thế giới ngầm.",
      "stickers": [],
      "impacts": []
    },
    {
      "at": "hai sát thủ mang tên Port và Starboard",
      "layout": "Bộ đôi sát thủ khét tiếng: Port và Starboard với chiếc vây cong đặc trưng bơi ép sát hai bên sườn {SHARK}.",
      "stickers": [],
      "impacts": []
    },
    {
      "at": "chiến thuật húc lật ngửa con mồi",
      "layout": "Cú húc lật ngửa tử thần: {SHARK} bị lật úp bụng lên trên, mắt đờ đẫn rơi vào trạng thái tê liệt trương lực không thể cử động.",
      "stickers": [],
      "impacts": []
    },
    {
      "at": "rạch một đường chính xác",
      "layout": "Đường phẫu thuật siêu việt: Vết rạch chuẩn xác dưới vây ngực lấy ra buồng gan béo ngậy giàu chất béo.",
      "stickers": [],
      "impacts": []
    },
    {
      "at": "vứt bỏ toàn bộ phần xác còn lại",
      "layout": "Thực đơn kén chọn của Bố Già: {HERO_S} thong thả thưởng thức buồng gan ngon lành, hoàn toàn bỏ qua phần thịt còn lại.",
      "stickers": [],
      "impacts": []
    },
    {
      "at": "khiến toàn bộ đàn cá mập trắng",
      "layout": "Cuộc sơ tán hàng loạt: Hàng trăm chú cá mập trắng hoảng sợ tháo chạy tán loạn khỏi vùng biển Nam Phi suốt một năm.",
      "stickers": [],
      "impacts": []
    },
    {
      "at": "uy quyền tuyệt đối của Bố Già Đại Dương",
      "layout": "Vương quyền biển cả: {HERO_S} ngự trị trên ngai vàng san hô đáy biển, khẳng định vị thế chúa tể bất khả xâm phạm.",
      "stickers": [],
      "impacts": []
    }
  ]
}

out_path = Path("projects/tap-35-ca-voi-sat-thu/specs/storyboard.json")
out_path.parent.mkdir(parents=True, exist_ok=True)
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(storyboard_data, f, ensure_ascii=False, indent=2)

print(f"Written specs/storyboard.json with {len(storyboard_data['long'])} long beats and {len(storyboard_data['shorts'])} shorts beats to {out_path}")


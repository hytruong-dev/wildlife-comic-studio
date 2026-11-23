import json
from pathlib import Path

P = Path("projects/tap-44-ca-mat-trang")
(P / "specs").mkdir(parents=True, exist_ok=True)

storyboard = {
  "_doc": "Kịch bản phân cảnh chi tiết cho Tập 44: Cá Mặt Trăng. Phong cách Pastel Dreamy Oceanic Fauvism & Gentle Giant Caricature. 58 beats dài, 8 beats shorts.",
  "characters": {
    "HERO": "chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây hậu môn cao vút quạt nhịp nhàng như cánh chim",
    "HERO_S": "chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri",
    "NO_HERO": "KHÔNG có cá mặt trăng trong cảnh này",
    "DOC": "bác sĩ cá heo đeo ống nghe và kính viễn vọng, mặc áo blouse trắng hài hước",
    "NURSE": "cô trợ lý hải cẩu đeo tạp dề chữ thập đỏ bưng khay kim tiêm",
    "JELLYFISH": "đàn sứa biển hoạt hình trong suốt phát sáng màu hồng pastel và tím nhạt trôi bồng bềnh",
    "SEAGULL": "chú chim mòng biển hoạt hình trắng muốt mỏ vàng tinh quái đậu rỉa spa"
  },
  "side_characters": {
    "CRANE": "chiếc cần cẩu công nghiệp màu vàng cam rực rỡ với dây cáp thép to bản",
    "SEAL": "chú hải cẩu xám béo tròn đang ngoạm cắn đuôi cá mặt trăng",
    "BABY_MOLA": "chú ấu trùng cá mặt trăng tí hon tròn xoe như quả cầu gai phi thuyền ngoài hành tinh"
  },
  "shorts_side_characters": {
    "SEAL_S": "chú hải cẩu tinh nghịch bơi lại cắn vây cá",
    "SEAGULL_S": "chú chim mòng biển đậu trên lưng cá rỉa spa"
  },
  "shorts_title_lines": [
    "NẶNG 2 TẤN VÔ TRI",
    "BỊ CẮN VẪN PHƠI NẮNG?!"
  ],
  "skip_numbers": False,
  "long": [
    # Scene 01 (9 beats)
    {"scene": "scene01", "at": 0, "layout": "Phòng cấp cứu đa khoa sinh vật biển: {DOC} đang sốt sắng chỉ huy hiện trường, bên cạnh là một bể nước mặn khổng lồ bằng kính trong suốt phát sáng bọt khí pastel turquoise.", "stickers": [], "impacts": []},
    {"scene": "scene01", "at": 18, "layout": "Cận cảnh hiện trường: {CRANE} đang từ từ hạ dây cáp cẩu xuống để chuẩn bị đón nhận một ca bệnh thể trọng khổng lồ; {NURSE} bên cạnh hốt hoảng ôm sổ bệnh án.", "stickers": [{"word": "mười tấn", "kind": "stat", "label": "CẦN CẨU CÔNG NGHIỆP", "value": "10 TẤN", "target": [700, 400]}], "impacts": []},
    {"scene": "scene01", "at": 38, "layout": "{HERO} lừng lững xuất hiện trên móc cẩu: Một thân hình tròn dẹt khổng lồ, hai mắt tròn xoe đờ đẫn nhìn vào hư không không chớp mắt.", "stickers": [], "impacts": []},
    {"scene": "scene01", "at": 55, "layout": "Chiếc bàn cân điện tử công nghiệp bị đè sập gãy đôi xịt khói; {NURSE} ôm đầu kinh hãi; {HERO} vẫn giữ nguyên nụ cười ngây ngô vô số tội.", "stickers": [], "impacts": []},
    {"scene": "scene01", "at": 68, "layout": "{DOC} cầm tấm bảng chẩn đoán phóng to hồ sơ bệnh án Mola mola; nền là bản đồ đại dương màu lam ngọc pastel với dòng chữ GÃ KHỔNG LỒ VÔ TRI.", "stickers": [], "impacts": []},
    {"scene": "scene01", "at": 85, "layout": "So sánh hài hước: BÊN TRÁI là các loài thủy quái biển sâu cơ bắp răng nhọn hoắt khí động học; BÊN PHẢI là {HERO} tròn lẳn cụt lủn như cái đầu cá bị cắt rời lềnh bềnh trôi nước.", "stickers": [], "impacts": []},
    {"scene": "scene01", "at": 105, "layout": "Sơ đồ giải phẫu thể trọng: {HERO} với các mũi tên đo kích thước chiều dài 3 mét và sải vây từ trên xuống dưới 4 mét trên nền giấy can đại dương pastel.", "stickers": [{"word": "hai tấn", "kind": "stat", "label": "THỂ TRỌNG KỶ LỤC", "value": "2 TẤN", "target": [750, 420]}], "impacts": []},
    {"scene": "scene01", "at": 125, "layout": "Cận cảnh gương mặt vô tri: Đôi mắt tròn xoe trống rỗng và chiếc miệng tròn vo há hốc ngơ ngác của {HERO}; vài bong bóng nước lững lờ bay ra.", "stickers": [], "impacts": []},
    {"scene": "scene01", "at": 145, "layout": "{HERO} thong dong trôi giữa đại dương bao la thời tiền sử, đàn cá cổ đại vây quanh tò mò; {DOC} giơ kính lúp nghiên cứu thắc mắc.", "stickers": [], "impacts": []},

    # Scene 02 (11 beats)
    {"scene": "scene02", "at": 0, "layout": "Màn hình chẩn đoán chụp cắt lớp CT toàn thân của {HERO}: Khung xương cá lộ rõ nhưng phần đuôi sau hoàn toàn biến mất; {DOC} chỉ tay phân tích.", "stickers": [], "impacts": []},
    {"scene": "scene02", "at": 18, "layout": "Mô phỏng 3D cơ sinh học: Con cá ngừ rẽ sóng vùn vụt nhờ vây đuôi cơ bắp; đối diện là {HERO} không có đuôi chỉ bơi bằng cách lắc lư hai vây đứng.", "stickers": [], "impacts": []},
    {"scene": "scene02", "at": 35, "layout": "{NURSE} cúi người soi kính lúp vào phần rìa thịt lượn sóng phía sau mông của {HERO}; biểu cảm hoang mang tột độ.", "stickers": [], "impacts": []},
    {"scene": "scene02", "at": 50, "layout": "Phóng to cấu tạo giải phẫu thùy clavus: Phần vây lưng và vây hậu môn hợp nhất thành chiếc bánh lái thịt nhăn nheo như diềm váy búp bê.", "stickers": [{"word": "thùy clavus", "kind": "badge", "label": "DỊ TẬT TIẾN HÓA", "value": "THÙY ĐUÔI", "target": [800, 450]}], "impacts": []},
    {"scene": "scene02", "at": 68, "layout": "Minh họa bánh lái tàu thủy cổ điển gắn sau mông {HERO}, xoay nhẹ để rẽ hướng lờ đờ giữa làn nước xanh pastel.", "stickers": [], "impacts": []},
    {"scene": "scene02", "at": 85, "layout": "Cắt lớp vi thể xương sụn: Bộ xương của {HERO} không phải xương cứng mà là những thớ sụn xốp chứa đầy nước; {DOC} dùng ngón tay ấn thử thấy đàn hồi như thạch.", "stickers": [], "impacts": []},
    {"scene": "scene02", "at": 105, "layout": "Sơ đồ động lực học: {HERO} không có bong bóng cá nhưng sở hữu hai cánh vây lưng và vây bụng khổng lồ đang quạt nhịp nhàng từ trái qua phải như cánh chim cánh cụt bay lượn.", "stickers": [], "impacts": []},
    {"scene": "scene02", "at": 125, "layout": "Thiết bị định vị GPS gắn trên vây lưng {HERO}: Đồng hồ đo tốc độ hiển thị kim chỉ vạch ba chấm hai ki-lô-mét một giờ; {HERO} lướt đi nhẹ nhàng thanh thoát.", "stickers": [{"word": "ba chấm hai ki-lô-mét một giờ", "kind": "stat", "label": "TỐC ĐỘ BƠI", "value": "3.2 KM/H", "target": [720, 380]}], "impacts": []},
    {"scene": "scene02", "at": 145, "layout": "Tấm kính sinh thiết biểu bì da cá: Lớp da collagen dày cộp bảy chấm năm xăng-ti-mét như lốp xe tăng; {DOC} dùng thước kẹp đo độ dày.", "stickers": [{"word": "bảy chấm năm xăng-ti-mét", "kind": "stat", "label": "ĐỘ DÀY DA ĐỆM", "value": "7.5 CM", "target": [750, 430]}], "impacts": []},
    {"scene": "scene02", "at": 165, "layout": "Kính hiển vi điện tử soi bề mặt da: Những chiếc gai vi thể li ti tiết ra màng chất nhờn trong suốt bao bọc cơ thể {HERO}.", "stickers": [], "impacts": []},
    {"scene": "scene02", "at": 185, "layout": "{HERO} bơi va vào tảng đá ngầm nhưng lớp da đệm đàn hồi bật nảy ra êm ru; {HERO} vẫn giữ nguyên ánh mắt vô tri cười toe toét.", "stickers": [], "impacts": []},

    # Scene 03 (10 beats)
    {"scene": "scene03", "at": 0, "layout": "Nhà bếp hải dương: Bàn ăn ngập tràn các đĩa cá ngừ béo ngậy và mực ống thơm lừng, nhưng {HERO} lắc đầu chê bai; {DOC} đứng cạnh ngạc nhiên.", "stickers": [], "impacts": []},
    {"scene": "scene03", "at": 18, "layout": "Cận cảnh chiếc miệng nhỏ xíu của {HERO}: Các răng hợp nhất thành chiếc mỏ vẹt cứng nhắc; phía trước là đàn {JELLYFISH} trôi lững lờ.", "stickers": [], "impacts": []},
    {"scene": "scene03", "at": 35, "layout": "Thực đơn phân tích dinh dưỡng: Chiếc đĩa bày một con sứa trong suốt với nhãn dán thành phần gồm chín mươi chín phần trăm nước muối và một phần trăm thạch gelatin.", "stickers": [{"word": "chín mươi chín phần trăm", "kind": "stat", "label": "THỰC ĐƠN SỨA BIỂN", "value": "99% NƯỚC", "target": [780, 400]}], "impacts": []},
    {"scene": "scene03", "at": 52, "layout": "{HERO} hóa thân thành chiếc máy hút bụi đại dương, há to mỏ hút trọn từng đàn sứa biển trôi nổi như mì sợi vào bụng.", "stickers": [], "impacts": []},
    {"scene": "scene03", "at": 70, "layout": "{DOC} cầm đèn pin soi sâu vào khoang miệng của {HERO}: Cụm răng họng nhọn hoắt xếp tầng tầng lớp lớp hướng cong vào trong như chiếc bẫy gai.", "stickers": [], "impacts": []},
    {"scene": "scene03", "at": 88, "layout": "Mô phỏng máy ép ly tâm: Chiếc cuống họng cá co bóp ép kiệt nước biển phun ra hai bên nắp mang, giữ lại mảng thạch sứa đậm đặc đẩy xuống dạ dày.", "stickers": [], "impacts": []},
    {"scene": "scene03", "at": 108, "layout": "{HERO} lặn thẳng xuống vực sâu thẳm: Ánh sáng mặt trời tắt lịm, đại dương chuyển sang màu tím than sâu thẳm, đồng hồ đo độ sâu chỉ tám trăm mét.", "stickers": [{"word": "tám trăm mét", "kind": "stat", "label": "ĐỘ SÂU LẶN SĂN", "value": "800 M", "target": [760, 420]}], "impacts": []},
    {"scene": "scene03", "at": 128, "layout": "Vùng nước sâu băng giá: Nhiệt kế cắm xuống hiển thị mức nhiệt độ buốt giá bốn độ C; {HERO} vẫn ung dung đớp những con sứa khổng lồ phát quang sinh học.", "stickers": [{"word": "bốn độ C", "kind": "stat", "label": "NHIỆT ĐỘ BIỂN SÂU", "value": "4°C", "target": [740, 410]}], "impacts": []},
    {"scene": "scene03", "at": 148, "layout": "Lớp mỡ trắng ngà dày dưới da {HERO} phát sáng hào quang bảo vệ, giữ ấm cho các cơ quan nội tạng khỏi bị đóng băng.", "stickers": [], "impacts": []},
    {"scene": "scene03", "at": 168, "layout": "{HERO} no nê vỗ bụng dưới đáy sâu, bắt đầu quạt vây hướng mũi bơi thẳng lên mặt nước tìm kiếm ánh mặt trời.", "stickers": [], "impacts": []},

    # Scene 04 (11 beats)
    {"scene": "scene04", "at": 0, "layout": "Mặt biển lấp lánh ánh nắng vàng: {HERO} ngoi lên mặt nước, lật nghiêng thân mình dẹt hai tấn nằm ngửa phơi bụng đón nắng như đang đi nghỉ dưỡng ở resort.", "stickers": [], "impacts": []},
    {"scene": "scene04", "at": 18, "layout": "Cơ thể {HERO} biến thành tấm pin năng lượng mặt trời thu nhỏ, hấp thụ từng luồng nhiệt ấm áp từ mặt trời để sưởi ấm dòng máu lạnh giá.", "stickers": [], "impacts": []},
    {"scene": "scene04", "at": 38, "layout": "{NURSE} hoảng hốt chỉ tay vào kính phóng đại: Trên lưng và mang {HERO} là đàn ký sinh trùng nhiều chân lúc nhúc bò lổm ngổm.", "stickers": [], "impacts": []},
    {"scene": "scene04", "at": 55, "layout": "Bảng tổng kết da liễu: Hình ảnh bốn mươi loài ký sinh trùng khác nhau từ rận biển, giun tròn đến giáp xác bám đầy thân {HERO}.", "stickers": [{"word": "bốn mươi loài", "kind": "stat", "label": "KÝ SINH TRÙNG", "value": "40 LOÀI", "target": [760, 390]}], "impacts": []},
    {"scene": "scene04", "at": 75, "layout": "Ký sinh lồng ký sinh: Một con rận biển to bám trên da cá, trên lưng con rận lại có một cụm giun biển nhỏ xíu đẻ trứng; {DOC} lắc đầu cười trừ.", "stickers": [], "impacts": []},
    {"scene": "scene04", "at": 95, "layout": "Dịch vụ spa bãi biển mở màn: Đàn cá bướm và cá thiên thần sọc màu pastel rực rỡ bơi quanh {HERO}, chăm chỉ rỉa từng con rận biển.", "stickers": [], "impacts": []},
    {"scene": "scene04", "at": 115, "layout": "{SEAGULL} thản nhiên hạ cánh đậu ngay trên má của {HERO} đang nổi ngửa, dùng mỏ mổ từng con ký sinh trùng béo mầm; {HERO} lim dim tận hưởng.", "stickers": [], "impacts": []},
    {"scene": "scene04", "at": 135, "layout": "Bức tranh toàn cảnh spa đại dương cộng sinh hài hòa giữa chim mòng biển trên trời, cá rỉa dưới nước và {HERO} phơi nắng hưởng thụ.", "stickers": [], "impacts": []},
    {"scene": "scene04", "at": 155, "layout": "{HERO} lặn xuống lấy đà dưới làn nước xanh ngắt, quạt vây hết tốc lực chuẩn bị cho một cú nhảy vọt thể thao chấn động.", "stickers": [], "impacts": []},
    {"scene": "scene04", "at": 172, "layout": "Cú phóng vọt ngoạn mục: Khối thân hai tấn của {HERO} bay thẳng lên khỏi mặt biển cao ba mét giữa bầu trời nắng rực; bọt nước bắn tung tóe.", "stickers": [{"word": "ba mét", "kind": "stat", "label": "CÚ PHÓNG VỌT", "value": "3 MÉT", "target": [750, 380]}], "impacts": []},
    {"scene": "scene04", "at": 192, "layout": "{HERO} rơi tự do đập bẹp cả tấm thân dẹt xuống mặt biển tạo làn sóng cuộn trào; lũ ký sinh trùng bị chấn động văng tứ tung ra ngoài.", "stickers": [], "impacts": []},

    # Scene 05 (10 beats)
    {"scene": "scene05", "at": 0, "layout": "{SEAL} hung hăng lao tới cắn rách một mảng vây của {HERO}; {HERO} bị cắn nhưng gương mặt vẫn đờ đẫn mỉm cười nhìn lên bầu trời không chút phản xạ sợ hãi.", "stickers": [], "impacts": []},
    {"scene": "scene05", "at": 18, "layout": "{DOC} và {NURSE} ôm mặt xót xa trước cảnh tượng; trên màn hình hiển thị biểu đồ chỉ số tự vệ và phản xạ trốn chạy của {HERO} ở mức số không tròn trĩnh.", "stickers": [], "impacts": []},
    {"scene": "scene05", "at": 38, "layout": "Đại dương mênh mông bừng sáng: {HERO} mẹ phóng thích một đám mây trứng khổng lồ phát sáng lấp lánh như dải ngân hà dưới làn nước biển.", "stickers": [], "impacts": []},
    {"scene": "scene05", "at": 58, "layout": "Bảng kỷ lục Guinness đại dương: Dòng chữ ba trăm triệu quả trứng vàng son rực rỡ; chiếc cúp vô địch sinh sản động vật có xương sống đặt cạnh {HERO}.", "stickers": [{"word": "ba trăm triệu", "kind": "stat", "label": "SẢN LƯỢNG TRỨNG", "value": "300 TRIỆU", "target": [780, 410]}], "impacts": []},
    {"scene": "scene05", "at": 78, "layout": "Bức ảnh siêu âm ấu trùng: {BABY_MOLA} bé tí xíu chỉ dài hai mi-li-mét, nhỏ hơn hạt vừng đặt cạnh chiếc kim may áo của {DOC}.", "stickers": [{"word": "hai mi-li-mét", "kind": "stat", "label": "KÍCH THƯỚC ẤU TRÙNG", "value": "2 MM", "target": [720, 400]}], "impacts": []},
    {"scene": "scene05", "at": 95, "layout": "Phóng to {BABY_MOLA}: Tròn ung ủng với hàng chục chiếc gai nhọn hoắt chìa ra xung quanh như một phi thuyền ngoài hành tinh mini dễ thương.", "stickers": [], "impacts": []},
    {"scene": "scene05", "at": 115, "layout": "Đàn ấu trùng phi thuyền tí hon bơi lăng quăng giữa các loài sinh vật phù du, những chiếc gai nhọn giúp xua đuổi các loài tôm tép ăn thịt.", "stickers": [], "impacts": []},
    {"scene": "scene05", "at": 135, "layout": "Biểu đồ tiến hóa tăng trưởng thể trọng: Từ ấu trùng 2mm rụng dần gai, lớn dần thành cá nhỏ rồi hóa thành gã khổng lồ hai tấn; mũi tên tăng trưởng gấp sáu mươi triệu lần.", "stickers": [{"word": "sáu mươi triệu lần", "kind": "stat", "label": "TĂNG TRƯỞNG KỶ LỤC", "value": "X60 TRIỆU", "target": [770, 420]}], "impacts": []},
    {"scene": "scene05", "at": 155, "layout": "{HERO} trưởng thành bơi bên cạnh đàn con tí hon; sự tương phản kích thước vĩ đại và kỳ diệu nhất của giới sinh vật biển.", "stickers": [], "impacts": []},
    {"scene": "scene05", "at": 175, "layout": "{DOC} đặt bút ký con dấu ĐÃ KIỂM ĐỊNH vào hồ sơ sinh sản của bệnh nhân với nụ cười khâm phục.", "stickers": [], "impacts": []},

    # Scene 06 (7 beats)
    {"scene": "scene06", "at": 0, "layout": "{DOC} đóng hồ sơ bệnh án số bốn mươi tư, mỉm cười gật gù; phía sau là bức tranh phong cảnh đại dương pastel tuyệt đẹp với {HERO} đang bình thản bơi lượn.", "stickers": [], "impacts": []},
    {"scene": "scene06", "at": 18, "layout": "Triết lý sống vô tri: {HERO} trôi nhẹ nhàng giữa biển cả sóng gió, ánh nắng ấm áp chiếu rọi gương mặt an yên không màng danh lợi.", "stickers": [], "impacts": []},
    {"scene": "scene06", "at": 38, "layout": "Màn hình tương tác người xem: Hai chiếc nút lựa chọn đồ họa pastel hài hước: Nút 1 là đầu cá hai tấn vô tư phơi nắng, Nút 2 là cỗ máy đẻ 300 triệu trứng.", "stickers": [], "impacts": []},
    {"scene": "scene06", "at": 55, "layout": "{NURSE} giơ biển chỉ dẫn mời người xem để lại bình luận chẩn đoán bên dưới video.", "stickers": [], "impacts": []},
    {"scene": "scene06", "at": 70, "layout": "Hồ sơ mật tập 45 hé lộ: Một chú vẹt béo múp lông xanh rêu đang đứng đơ như bụi cây giữa khu rừng rậm New Zealand sương mù huyền ảo.", "stickers": [], "impacts": []},
    {"scene": "scene06", "at": 88, "layout": "Chú vẹt béo trèo lên cành cây cao rồi nhảy ùm xuống đất đập mặt ngơ ngác hài hước; các dấu hỏi chấm xoay quanh đầu chú vẹt.", "stickers": [], "impacts": []},
    {"scene": "scene06", "at": 105, "layout": "Màn hình kết thúc: Dòng chữ HẸN GẶP LẠI Ở TẬP 45 VẸT KAKAPO lung linh với lời kêu gọi đăng ký kênh và ấn chuông theo dõi.", "stickers": [], "impacts": []}
  ],
  "shorts": [
    {"at": 0, "layout": "Cận cảnh mở đầu: {SEAL_S} bơi lại cắn xé vây của {HERO_S}; {HERO_S} nặng hai tấn vẫn nằm ngửa nhìn trời ngơ ngác vô cảm.", "stickers": [{"word": "hai tấn", "kind": "stat", "label": "GÃ KHỔNG LỒ", "value": "2 TẤN", "target": [300, 500]}]},
    {"at": 12, "layout": "{HERO_S} to lớn như một chiếc xe tải bọc thép trôi dạt giữa đại dương; cơ thể cụt lủn không có đuôi cá thật.", "stickers": []},
    {"at": 24, "layout": "{HERO_S} bơi bằng hai cánh vây khổng lồ quạt nhịp nhàng; chiếc miệng tròn vo há hốc hút trọn những con sứa trong suốt.", "stickers": []},
    {"at": 36, "layout": "{HERO_S} lặn xuống vực biển sâu thẳm đen ngòm tám trăm mét, xung quanh nhiệt kế chỉ vạch buốt giá bốn độ C.", "stickers": []},
    {"at": 48, "layout": "{HERO_S} ngoi lên mặt biển thoáng nằm nghiêng phơi bụng đón nắng vàng sưởi ấm thân nhiệt.", "stickers": []},
    {"at": 58, "layout": "{SEAGULL_S} đáp xuống đậu trên thân {HERO_S}, cần mẫn mổ rỉa sạch những con ký sinh trùng bám trên da.", "stickers": []},
    {"at": 68, "layout": "{HERO_S} mẹ phóng thích hàng triệu quả trứng vàng phát sáng lấp lánh như dải ngân hà dưới làn nước biển xanh.", "stickers": [{"word": "ba trăm triệu", "kind": "stat", "label": "KỶ LỤC SINH SẢN", "value": "300 TRIỆU", "target": [320, 520]}]},
    {"at": 78, "layout": "Kỷ lục vô địch tuyệt đối: {HERO_S} cười toe toét bên chiếc cúp vàng sinh sản ba trăm triệu quả trứng; mời gọi đăng ký kênh xem trọn bộ tập 44.", "stickers": []}
  ]
}

(P / "specs" / "storyboard.json").write_text(json.dumps(storyboard, ensure_ascii=False, indent=2), encoding="utf-8")
print("Saved storyboard.json for Ep 44: 58 long beats, 8 shorts beats!")


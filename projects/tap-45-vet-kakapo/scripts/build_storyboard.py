import json
from pathlib import Path

P = Path("projects/tap-45-vet-kakapo")
(P / "specs").mkdir(parents=True, exist_ok=True)

storyboard = {
  "_doc": "Kịch bản phân cảnh chi tiết cho Tập 45: Vẹt Kakapo. Phong cách New Zealand Mossy Forest Folklore & Whimsical Children's Book Illustration. 57 beats dài, 8 beats shorts.",
  "characters": {
    "HERO": "chú vẹt kakapo hoạt hình béo múp míp tròn ủng màu xanh rêu lục bảo đốm vàng ấm áp, đôi mắt tròn xoe ngây ngô tấu hài, chiếc mỏ xám ngà quặp cứng cáp, đôi cánh ngắn tũn nép sát người, đôi chân to khỏe bám rêu rừng nguyên sinh New Zealand",
    "HERO_S": "chú vẹt kakapo hoạt hình tròn vo béo múp 4kg màu xanh rêu, mắt tròn xoe ngơ ngác",
    "NO_HERO": "KHÔNG có chú vẹt kakapo trong cảnh này",
    "REPORTER": "chú chim bói cá phóng viên đeo kính cận, cổ đeo thẻ nhà báo dã ngoại và tay cầm micro đài truyền hình",
    "NEWS_ANCHOR": "phát thanh viên đài truyền hình cú tuyết đeo tai nghe ngồi trong trường quay tin tức thời sự",
    "EAGLE": "bóng đen khổng lồ của đại bàng Haast thời tiền sử sải cánh 3 mét trên bầu trời",
    "FERRET": "chú chồn ec-min nâu nhọn mũi đang hít hà đánh hơi mùi mật ong rừng",
    "RIMU_TREE": "ngọn cây cổ thụ rimu New Zealand cao vút 20 mét trĩu quả chín mọng vàng ươm"
  },
  "side_characters": {},
  "shorts_side_characters": {},
  "shorts_title_lines": [
    "QUÊN MÌNH KHÔNG BIẾT BAY",
    "LEO 20M NHẢY ĐẬP BỤNG?!"
  ],
  "skip_numbers": [],
  "long": [
    # Scene 01 (9 beats)
    {"scene": "scene01", "at": 0, "layout": "Trực tiếp từ hiện trường rừng nguyên sinh New Zealand: {REPORTER} đang cầm micro nói trước ống kính, xung quanh là thảm rêu xanh ngọc và thân cây cổ thụ sương mù mờ ảo.", "stickers": [], "impacts": []},
    {"scene": "scene01", "at": "", "layout": "Màn hình tín hiệu kết nối trường quay: {NEWS_ANCHOR} đeo tai nghe đang theo dõi bản tin hiện trường trực tiếp; bản đồ New Zealand phát sáng điểm đỏ đảo Codfish.", "stickers": [], "impacts": []},
    {"scene": "scene01", "at": "", "layout": "{REPORTER} cầm máy dò sóng vô tuyến reo vang bíp bíp, chỉ tay về phía hốc rễ cây cổ thụ rêu phong rậm rạp.", "stickers": [], "impacts": []},
    {"scene": "scene01", "at": "", "layout": "Cận cảnh hốc cây: {HERO} tròn vo như một trái bơ khổng lồ đang ngủ say sưa, phát ra tiếng ngáy khò khò làm rung rinh vạt cỏ.", "stickers": [], "impacts": []},
    {"scene": "scene01", "at": "", "layout": "{REPORTER} há hốc miệng kinh ngạc trước thân hình béo múp míp của {HERO}; nhãn tên khoa học Strigops habroptilus và biệt danh GÃ BÉO VÔ TRI QUÊN CÁCH BAY hiện lên.", "stickers": [], "impacts": []},
    {"scene": "scene01", "at": "", "layout": "So sánh tương phản hài hước: BÊN TRÁI là đàn vẹt sặc sỡ đang bay lượn nhào lộn điệu nghệ; BÊN PHẢI là {HERO} ngồi bẹp dí dưới đất ngơ ngác như một chú gà béo.", "stickers": [], "impacts": []},
    {"scene": "scene01", "at": "", "layout": "Bàn cân trọng lượng dã ngoại: {HERO} đứng lên khiến kim cân nhảy vọt qua vạch bốn cân; gương mặt tròn xoe tấu hài không chút bận tâm.", "stickers": [{"at": "4 kg", "side": "R", "y": 360, "value": "4 KG", "label": "thể trọng kỷ lục", "target": [0.75, 0.5]}], "impacts": []},
    {"scene": "scene01", "at": "", "layout": "Cận cảnh khuôn mặt ngây thơ: Đôi mắt tròn xoe đờ đẫn và chòm râu ria quanh mỏ của {HERO} trông vừa giống cú mèo vừa giống trái bơ chín.", "stickers": [], "impacts": []},
    {"scene": "scene01", "at": "", "layout": "Đồng hồ bấm giờ sinh tồn hai mươi tư giờ bắt đầu đếm ngược những giây đầu tiên; {REPORTER} nín thở rón rén đi theo dấu chân {HERO}.", "stickers": [], "impacts": []},

    # Scene 02 (10 beats)
    {"scene": "scene02", "at": 0, "layout": "Đồng hồ hiện trường điểm mười giờ sáng: {HERO} bắt đầu vươn vai cựa quậy tỉnh giấc sau một giấc ngủ nướng dài; {REPORTER} quan sát ghi chép.", "stickers": [], "impacts": []},
    {"scene": "scene02", "at": "", "layout": "Thước đo chiều dài sinh học: {HERO} đứng nghiêm chỉnh từ mỏ đến chóp đuôi đạt sáu mươi xăng-ti-mét trên nền giấy kẻ ô cổ tích.", "stickers": [{"at": "60 cm", "side": "L", "y": 380, "value": "60 CM", "label": "chiều dài cơ thể", "target": [0.28, 0.5]}], "impacts": []},
    {"scene": "scene02", "at": "", "layout": "Cúp vàng vinh danh: {HERO} đứng cạnh chiếc cúp loài vẹt nặng nhất thế giới; con số bốn cân vàng son nổi bật.", "stickers": [{"at": "4 kg", "side": "R", "y": 360, "value": "4 KG", "label": "loài vẹt nặng nhất", "target": [0.75, 0.5]}], "impacts": []},
    {"scene": "scene02", "at": "", "layout": "Tấm phim chụp X-quang so sánh giải phẫu: Khung xương chim đại bàng với gờ xương ức nhô cao như lưỡi kiếm; bên cạnh là khung xương {HERO} với xương ức phẳng lì như tấm thớt.", "stickers": [], "impacts": []},
    {"scene": "scene02", "at": "", "layout": "Mô phỏng cơ sinh học: Cơ ngực của {HERO} teo nhỏ xíu không thể tạo lực vỗ cánh; {REPORTER} cầm bảng chẩn đoán chỉ tay giải thích.", "stickers": [], "impacts": []},
    {"scene": "scene02", "at": "", "layout": "{HERO} cố gắng xòe cánh đập phành phạch trong vô vọng; gió chỉ làm bay vài sợi rêu khô dưới chân, khối thân bốn cân vẫn dính chặt mặt đất.", "stickers": [], "impacts": []},
    {"scene": "scene02", "at": "", "layout": "Tiến hóa chơi khăm: Đôi cánh của {HERO} được vẽ biến tấu thành một chiếc áo choàng lông vũ thời trang làm cảnh; {HERO} xoay người tạo dáng hài hước.", "stickers": [], "impacts": []},
    {"scene": "scene02", "at": "", "layout": "Bức tranh tiền sử New Zealand: Thung lũng rêu phong màu ngọc bích ngập tràn hoa quả rụng, không hề có bóng dáng bất kỳ loài thú ăn thịt nào rình rập.", "stickers": [], "impacts": []},
    {"scene": "scene02", "at": "", "layout": "Tổ tiên Kakapo ung dung nhai quả dưới bóng râm, tự nhủ không cần bay lượn tốn sức; đôi cánh dần dần thoái hóa theo thời gian.", "stickers": [], "impacts": []},
    {"scene": "scene02", "at": "", "layout": "{REPORTER} nhún vai cảm thán trước lựa chọn tiến hóa kỳ lạ của loài vẹt độc nhất vô nhị này.", "stickers": [], "impacts": []},

    # Scene 03 (10 beats)
    {"scene": "scene03", "at": 0, "layout": "Đồng hồ bấm giờ điểm mười lăm giờ chiều: Khu rừng đột ngột xào xạc lá cây báo động nguy hiểm; {REPORTER} nép mình sau thân cây thì thào.", "stickers": [], "impacts": []},
    {"scene": "scene03", "at": "", "layout": "{HERO} phát hiện tiếng động lạ, lập tức rụt cổ thụt đầu, đứng đơ phăng phắc như một hòn đá bọc rêu không hề chớp mắt.", "stickers": [], "impacts": []},
    {"scene": "scene03", "at": "", "layout": "{NEWS_ANCHOR} trên màn hình truyền hình ôm trán dở khóc dở cười trước tư thế đứng hình tấu hài của {HERO}.", "stickers": [], "impacts": []},
    {"scene": "scene03", "at": "", "layout": "Bầu trời thời tiền sử: {EAGLE} đang lượn vòng săn mồi bằng mắt; phía dưới {HERO} đứng bất động hòa lẫn hoàn hảo vào thảm thực vật màu xanh rêu.", "stickers": [], "impacts": []},
    {"scene": "scene03", "at": "", "layout": "Chiến thuật tàng hình thành công trước đại bàng: Đại bàng bay qua không nhìn thấy gì; {HERO} hé một bên mắt tinh quái cười thầm.", "stickers": [], "impacts": []},
    {"scene": "scene03", "at": "", "layout": "Con thuyền người định cư cập bến: Các loài động vật ngoại lai chuột, mèo và {FERRET} tràn lên hòn đảo thiên đường.", "stickers": [], "impacts": []},
    {"scene": "scene03", "at": "", "layout": "{FERRET} dùng chiếc mũi thính nhạy hít hà đánh hơi; những dải hương thơm màu hồng phấn hình bông hoa bay lơ lửng từ người {HERO}.", "stickers": [], "impacts": []},
    {"scene": "scene03", "at": "", "layout": "Minh họa lọ nước hoa mật ong rừng và quả chín gắn trên lưng {HERO}; cơ chế tỏa hương ngọt ngào trở thành chiếc bẫy tự sát.", "stickers": [], "impacts": []},
    {"scene": "scene03", "at": "", "layout": "Biểu đồ tuổi thọ sinh học: {HERO} rùa bò thong thả bên cột mốc sáu mươi đến chín mươi năm; loài chim sống thọ kỷ lục nhờ nhịp sống chậm rãi.", "stickers": [{"at": "60", "side": "L", "y": 380, "value": "60-90 NĂM", "label": "tuổi thọ kỷ lục", "target": [0.3, 0.5]}], "impacts": []},
    {"scene": "scene03", "at": "", "layout": "{REPORTER} kiểm tra camera nhiệt, thở phào khi thấy mối nguy hiểm vừa đi qua; {HERO} bắt đầu nhúc nhích cử động trở lại.", "stickers": [], "impacts": []},

    # Scene 04 (11 beats)
    {"scene": "scene04", "at": 0, "layout": "Đồng hồ hiện trường điểm mười chín giờ tối hoàng hôn: Bầu trời nhuộm màu tím than và vàng cam; chiếc bụng đói của {HERO} sôi réo ùng ục.", "stickers": [], "impacts": []},
    {"scene": "scene04", "at": "", "layout": "Kỹ năng leo trèo bất ngờ: {HERO} cắm phập chiếc mỏ quặp cứng như móc leo núi vào thân cây, đôi chân cơ bắp bám chắc đu người lên cao.", "stickers": [], "impacts": []},
    {"scene": "scene04", "at": "", "layout": "{REPORTER} lia máy quay theo bước chân thoăn thoắt của {HERO} đang trèo lên thân cây {RIMU_TREE} cao chót vót.", "stickers": [], "impacts": []},
    {"scene": "scene04", "at": "", "layout": "Đỉnh ngọn cây rimu cao hai mươi mét: {HERO} ngồi vắt vẻo trên cành cao, nhai nhồm nhoàm từng chùm quả rimu chín mọng ngọt ngào.", "stickers": [{"at": "20 mét", "side": "R", "y": 360, "value": "20 MÉT", "label": "độ cao ngọn cây", "target": [0.75, 0.5]}], "impacts": []},
    {"scene": "scene04", "at": "", "layout": "Khuôn mặt thỏa mãn tột cùng của {HERO} khi được no nê quả chín; vệt nước quả vàng ươm dính quanh mép mỏ.", "stickers": [], "impacts": []},
    {"scene": "scene04", "at": "", "layout": "{HERO} đứng trên đầu cành cây nhìn xuống mặt đất hun hút bên dưới, ưỡn ngực xòe cánh tự tin như một chú đại bàng sắp cất cánh.", "stickers": [], "impacts": []},
    {"scene": "scene04", "at": "", "layout": "Pha nhảy dù cảm tử: {HERO} lao mình vút vào không trung; đôi cánh ngắn tũn xòe ra loạng choạng như chiếc dù rách.", "stickers": [], "impacts": []},
    {"scene": "scene04", "at": "", "layout": "Trọng lực kéo khối thân bốn cân rơi tự do vùn vụt; {HERO} hoảng hốt mở to hai mắt, chiếc mỏ há hốc kêu quàng quạc.", "stickers": [], "impacts": []},
    {"scene": "scene04", "at": "", "layout": "Cú tiếp đất kinh thiên động địa: {HERO} đập thẳng bụng và mặt xuống thảm rêu dày đánh BẸP một tiếng; bụi lá và rêu bắn tung tóe.", "stickers": [], "impacts": []},
    {"scene": "scene04", "at": "", "layout": "{REPORTER} ôm miệng nín cười khi thấy {HERO} lồm cồm bò dậy, lắc lắc đầu cho tỉnh táo với những chú chim quay quanh đầu.", "stickers": [], "impacts": []},
    {"scene": "scene04", "at": "", "layout": "{HERO} phủi phủi lông ngực, ung dung bước tiếp như chưa từng có pha đập mặt thảm họa nào xảy ra.", "stickers": [], "impacts": []},

    # Scene 05 (8 beats)
    {"scene": "scene05", "at": 0, "layout": "Đồng hồ hiện trường điểm hai mươi ba giờ đêm: Rừng rậm tối đen như mực; {HERO} bắt đầu sải bước việt dã mạnh mẽ xuyên qua các lối mòn.", "stickers": [], "impacts": []},
    {"scene": "scene05", "at": "", "layout": "{NEWS_ANCHOR} đặt câu hỏi thắc mắc làm sao các chú vẹt tìm thấy nhau trong màn đêm mịt mù của cánh rừng nguyên sinh.", "stickers": [], "impacts": []},
    {"scene": "scene05", "at": "", "layout": "{HERO} đứng trên đỉnh đồi lộng gió, dùng móng vuốt cào bới tạo thành một chiếc hố hình lòng chảo sâu mười xăng-ti-mét trên nền đất mềm.", "stickers": [], "impacts": []},
    {"scene": "scene05", "at": "", "layout": "Sơ đồ âm học phễu loa: Chiếc hố đất hoạt động như bộ khuếch đại sóng âm; {HERO} đứng giữa hố hít căng lồng ngực phồng to như quả bóng.", "stickers": [], "impacts": []},
    {"scene": "scene05", "at": "", "layout": "Đại nhạc hội xuyên đêm: Những đợt sóng âm tần số thấp booming ồm ồm lan tỏa từ chiếc hố, rung chuyển cả màn đêm yên tĩnh.", "stickers": [], "impacts": []},
    {"scene": "scene05", "at": "", "layout": "Bản đồ radar âm thanh: Vòng tròn sóng âm lan tỏa bao phủ bán kính năm cây số khắp các thung lũng xung quanh.", "stickers": [{"at": "5 km", "side": "R", "y": 360, "value": "5 KM", "label": "bán kính âm thanh", "target": [0.75, 0.5]}], "impacts": []},
    {"scene": "scene05", "at": "", "layout": "{REPORTER} đeo tai nghe âm thanh chuyên dụng, giơ micro thu lại những tiếng booming kiên trì suốt tám tiếng của {HERO}.", "stickers": [], "impacts": []},
    {"scene": "scene05", "at": "", "layout": "Bóng dáng một nàng vẹt cái e ấp từ xa đang lần theo tiếng gọi tình yêu bước về phía đỉnh đồi trong niềm hy vọng.", "stickers": [], "impacts": []},

    # Scene 06 (9 beats)
    {"scene": "scene06", "at": 0, "layout": "Đồng hồ lại điểm sáu giờ sáng hôm sau: Ánh nắng bình minh vàng dịu chiếu qua màn sương sớm; bản tin hai mươi tư giờ khép lại một vòng quay.", "stickers": [], "impacts": []},
    {"scene": "scene06", "at": "", "layout": "{HERO} mệt lử sau đêm dài phát loa, lững thững bước về chiếc hốc rễ cây quen thuộc, cuộn tròn bộ lông xanh rêu đi ngủ nướng.", "stickers": [], "impacts": []},
    {"scene": "scene06", "at": "", "layout": "Trung tâm bảo tồn New Zealand: Các nhà khoa học nâng niu chăm sóc từng quả trứng và gắn thiết bị bảo vệ cho chú vẹt béo quý giá.", "stickers": [], "impacts": []},
    {"scene": "scene06", "at": "", "layout": "Tấm bảng thống kê bảo tồn: Con số hai trăm năm mươi cá thể ít ỏi được khoanh tròn trang trọng như những báu vật của Trái Đất.", "stickers": [{"at": "250", "side": "R", "y": 360, "value": "250 CÁ THỂ", "label": "quần thể toàn cầu", "target": [0.75, 0.5]}], "impacts": []},
    {"scene": "scene06", "at": "", "layout": "{REPORTER} khép sổ tay hiện trường, mỉm cười nhìn {HERO} đang say ngủ với thông điệp trân trọng sự ngây thơ thuần khiết của thiên nhiên.", "stickers": [], "impacts": []},
    {"scene": "scene06", "at": "", "layout": "Màn hình tương tác người xem: Khung bình luận mở ra mời khán giả chia sẻ lời nhắn nhủ yêu thương đến chú vẹt béo Kakapo.", "stickers": [], "impacts": []},
    {"scene": "scene06", "at": "", "layout": "Hồ sơ mật tập bốn mươi sáu hé lộ: Một chú lợn rừng kỳ lạ Babirusa giữa rừng rậm nhiệt đới Indonesia với cặp răng nanh uốn cong đâm xuyên sống mũi.", "stickers": [], "impacts": []},
    {"scene": "scene06", "at": "", "layout": "Cận cảnh cặp răng nanh nhọn hoắt tự đâm ngược vào trán hộp sọ một cách bí hiểm; dấu hỏi chấm xoay quanh sinh vật tự sát tiến hóa.", "stickers": [], "impacts": []},
    {"scene": "scene06", "at": "", "layout": "Màn hình kết thúc: Dòng chữ HẸN GẶP LẠI Ở TẬP 46 LỢN HƯƠU BABIRUSA lung linh với lời kêu gọi đăng ký kênh theo dõi.", "stickers": [], "impacts": []}
  ],
  "shorts": [
    {"at": 0, "layout": "Cận cảnh mở đầu: {HERO_S} béo múp 4kg leo lên ngọn cây cao hai mươi mét, xòe cánh nhảy ùm xuống rơi tự do đập bụng bẹp dí xuống thảm rêu.", "stickers": [{"at": "4 kg", "side": "L", "y": 500, "value": "4 KG", "label": "vẹt nặng nhất", "target": [0.3, 0.5]}]},
    {"at": "", "layout": "{HERO_S} là loài vẹt nặng nhất thế giới và loài vẹt duy nhất quên mất cách bay; cơ thể tròn ủng như trái bơ khổng lồ.", "stickers": []},
    {"at": "", "layout": "Khung xương X-quang: Xương ức phẳng lì khiến đôi cánh lông vũ chỉ còn là món đồ trang trí vô dụng.", "stickers": []},
    {"at": "", "layout": "{HERO_S} đứng hình phăng phắc như pho tượng giả làm bụi rêu khi gặp nguy hiểm giữa rừng già.", "stickers": []},
    {"at": "", "layout": "Những làn hương mật ong rừng và quả chín ngọt ngào bay ra từ người {HERO_S}, vô tình mời gọi kẻ săn mồi tới xơi.", "stickers": []},
    {"at": "", "layout": "Ban đêm {HERO_S} đi bộ hàng chục cây số, đào chiếc hố lòng chảo khuếch đại tiếng kêu booming vang xa năm cây số tìm bạn tình.", "stickers": [{"at": "5 km", "side": "R", "y": 520, "value": "5 KM", "label": "loa phóng thanh", "target": [0.7, 0.5]}]},
    {"at": "", "layout": "Nàng vẹt cái e ấp bước tới bên miệng hố; nỗ lực tình yêu nhẫn nại suốt hàng tháng trời được đền đáp.", "stickers": []},
    {"at": "", "layout": "Hiện cả thế giới chỉ còn hai trăm năm mươi cá thể vẹt Kakapo được bảo vệ nghiêm ngặt; mời đăng ký kênh xem trọn bộ tập 45.", "stickers": []}
  ]
}

(P / "specs" / "storyboard.json").write_text(json.dumps(storyboard, ensure_ascii=False, indent=2), encoding="utf-8")
print("Saved storyboard.json for Ep 45: 57 long beats, 8 shorts beats!")


import json
from pathlib import Path

P = Path("projects/tap-46-lon-huou-babirusa")
ep_data = json.loads((P / "episode.json").read_text(encoding="utf-8"))

# Update display_fix
ep_data["display_fix"]["ba mươi"] = "30"
ep_data["display_fix"]["mười một"] = "11"
ep_data["display_fix"]["mười lăm"] = "15"
ep_data["display_fix"]["một hai tuổi"] = "1-2 tuổi"
ep_data["display_fix"]["hai chân sau"] = "2 chân sau"
ep_data["display_fix"]["hai chân"] = "2 chân"
ep_data["display_fix"]["bốn mươi"] = "40"
ep_data["display_fix"]["hai mươi"] = "20"

scenes = ep_data["longform"]["scenes"]

# Scene 02: Add Part about tuổi mọc nanh
scenes[1]["parts"].insert(2, {
    "text": "Khám phá quá trình phát triển của bệnh nhân sẽ khiến quý vị rùng mình hơn nữa: Khi một chú lợn hươu con vừa chào đời, gương mặt gã hoàn toàn bình thường, mõm trơn láng và chưa hề có chiếc nanh nào lộ diện! Nhưng khi bước vào độ tuổi dậy thì khoảng một hai tuổi, chiếc mầm nanh quái đản bắt đầu đội thịt chồi lên! Da mõm gã sưng vù, căng tức cực độ cho đến khi mũi nanh sắc nhọn xé toang thớ thịt, đâm thủng một lỗ hổng vĩnh viễn trên sống mũi để vươn thẳng ra ngoài không khí! Một nghi thức trưởng thành đẫm máu mà tạo hóa bắt gã phải trải qua!",
    "mood": "tram_bi_an"
})

# Scene 03: Add Part about cấu trúc nanh giòn không có men
scenes[2]["parts"].insert(1, {
    "text": "Điều nực cười nhất trong cấu tạo giải phẫu của cặp nanh trên này chính là độ bền cơ học của chúng! Mọi người thường nghĩ răng nanh lợn rừng phải cứng như thép và sắc bén vô song đúng không? Hoàn toàn ngược lại! Cặp răng nanh hàm trên của Babirusa hoàn toàn không có lớp men răng cứng bao bọc bên ngoài, ruột xốp rỗng và cực kỳ giòn xốp! Nếu gã lỡ dại dùng cặp nanh này để húc đá hay ủi gốc cây tìm thức ăn, chúng sẽ gãy vụn ngay lập tức! Nghĩa là gã mang trên mặt một cặp vũ khí tự sát vừa vô dụng vừa dễ gãy!",
    "mood": "hao_hung"
})

# Scene 04: Add Part about đấu quyền Anh đứng bằng 2 chân
scenes[3]["parts"].append({
    "text": "Chính vì cặp nanh trên quá giòn và quý giá, các chàng lợn đực đã sáng tạo ra một nghi thức thi đấu tranh giành bạn tình độc nhất vô nhị: Khi hai gã lợn đực bước vào đấu trường quyết đấu, chúng tuyệt đối không bao giờ lao vào húc nanh đối đầu như lợn rừng thông thường vì sợ gãy mất món bảo bối quyến rũ! Thay vào đó, chúng đứng thẳng dậy bằng hai chân sau như hai võ sĩ quyền Anh hạng nặng, dùng hai mõm tỳ chặt vào nhau rồi vật lộn đẩy ngã đối phương trong tiếng gầm gừ vang dội cánh rừng già!",
    "mood": "hao_hung"
})

# Scene 05: Add Part about liếm bùn khoáng giải độc
scenes[4]["parts"].append({
    "text": "Chưa hết đâu nhé, chế độ ăn nhiều lá cây rừng chứa độc tố tanin đòi hỏi Gã bệnh nhân tự sát tiến hóa phải có một liệu trình giải độc cực kỳ thông minh: Các nhà nghiên cứu phát hiện ra đàn lợn hươu thường xuyên hành hương đến các mỏ đá muối khoáng tự nhiên và suối nước nóng địa nhiệt ở đảo Sulawesi! Tại đây, gã cần mẫn liếm láp những mảng bùn khoáng giàu canxi và natri để trung hòa độc tố trong dạ dày, đồng thời bổ sung khoáng chất giúp nuôi dưỡng cặp nanh khổng lồ mọc dài liên tục!",
    "mood": "hao_hung"
})

(P / "episode.json").write_text(json.dumps(ep_data, ensure_ascii=False, indent=1), encoding="utf-8")
print("Expanded Ep 46 episode.json successfully!")


"""Tập 9 Chim Cánh Cụt — sinh specs/longform_plan.json, specs/shorts_plan.json và specs/image_prompts.json.

Mỗi beat = 1 câu/ý thoại = 1 hình riêng. 'at' là cụm từ dạng phụ đề (đã qua display_fix).
Lời thoại trong prompt được cắt tự động từ kịch bản: từ cụm 'at' của beat tới cụm 'at' của beat kế.

  python projects/tap-09-chim-canh-cut/scripts/build_plans.py          # kiểm tra cụm từ + ghi 3 file
"""
import json
import re
import sys
from pathlib import Path

P = Path(__file__).resolve().parents[1]
ROOT = P.parents[1]
sys.path.insert(0, str(ROOT / "src" / "episode"))
from pipeline import norm, ptext, script_tokens  # noqa: E402

EP = json.loads((P / "episode.json").read_text(encoding="utf-8"))
DISPLAY = EP["display_fix"]

HERO = ("chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có "
        "vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ "
        "nhỏ ở cổ")
HERO_S = "chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ"
JUDGE = "ngài thẩm phán hải mã (walrus) già đội tóc giả trắng xoăn, cầm búa gỗ"
LAWYER = "ông công tố viên hoạt hình đeo kính tròn, mặc áo choàng đen"
NO_HERO = "KHÔNG có chú cánh cụt nơ đỏ trong cảnh này"

# (scene, at, layout, stickers[(at, side, y, value, label, [tx,ty])], impacts)
B = [
 # ---------------- scene01 VỤ ÁN NAM CỰC
 ("scene01", 0, f"Toàn cảnh Nam Cực trong bão tuyết: núi băng trắng xanh, gió cuốn tuyết thành vệt, bầu trời xám. BÊN PHẢI cắm một chiếc nhiệt kế khổng lồ đóng băng, cột đỏ tụt xuống tận đáy. {NO_HERO}.",
  [("-40°C", "R", 360, "-40°C", "lạnh thấu xương", [0.78, 0.6])], []),
 ("scene01", "Một viên sỏi vừa", "Một cái tổ hình vòng tròn xếp bằng những viên sỏi xám nằm trên bãi đá, phía trước tổ có một chỗ trống hình viên sỏi được khoanh bằng nét đứt như hiện trường vụ án; một chiếc kính lúp to ở GIỮA soi vào chỗ trống; BÊN TRÁI một chú cánh cụt hàng xóm (không đeo nơ) há mỏ sửng sốt.",
  [], []),
 ("scene01", "Ở mép băng, một", "Mép một tảng băng trôi trên biển xanh thẫm: một chú cánh cụt (không đeo nơ) đang rơi tõm xuống nước, hai cánh vung loạn, nước bắn tung tóe; trên mép băng thấy một chiếc chân cánh cụt khác vừa rụt lại đầy bí ẩn.",
  [], ["rơi tõm"]),
 ("scene01", "Và trên nền tuyết", "Nhìn từ trên cao: nền tuyết trắng với nhiều vệt màu hồng trắng tỏa ra từ một cái tổ sỏi như tia nắng, giống hiện trường bị bắn súng sơn; một cái bóng đen nhỏ lạch bạch bỏ đi ở góc phải.",
  [], []),
 ("scene01", "Bị cáo, mời đứng", f"Phòng xử án băng giá: Ở GIỮA trên bục cao là {JUDGE}, mặt nghiêm nghị, búa gỗ giơ lên; phía dưới BÊN PHẢI là vành móng ngựa bằng gỗ còn trống, đèn chiếu sáng vào đó.",
  [], ["mời đứng lên"]),
 ("scene01", "Và bị cáo là", f"Trong vành móng ngựa gỗ là {HERO}, nhỏ xíu đến mức chỉ ló được nửa cái đầu qua thành gỗ, đang nhón chân; BÊN TRÁI là một con mèo nhà màu cam ngồi cạnh để so sánh kích cỡ (cao gần bằng nhau); có thước đo chiều cao vẽ vạch (không số) sau lưng chú cánh cụt.",
  [("70cm", "R", 330, "70 CM", "chiều cao bị cáo", [0.62, 0.45]), ("3-6kg", "L", 470, "3-6 KG", "nặng như con mèo", [0.25, 0.6])], []),
 ("scene01", "Kính thưa bồi thẩm", f"Chân dung cận cảnh {HERO}, đứng thẳng như chụp ảnh hồ sơ, hai cánh khép, vòng trắng quanh mắt tròn xoe như vừa bị dọa giật mình, vài giọt mồ hôi lo lắng.",
  [], []),
 ("scene01", "Ở tòa này, chúng", f"{HERO} thêm áo vest đuôi tôm đen bóng như đi dự tiệc cưới, cầm ly nước, cười lịch lãm; BÊN PHẢI là một chồng hồ sơ giấy khổng lồ cao hơn cả chú cánh cụt, sắp đổ.",
  [], []),
 ("scene01", "Hôm nay, công tố", f"{LAWYER} đứng BÊN TRÁI giơ tay chỉ vào một bảng ghim 4 tấm ảnh bằng chứng ở BÊN PHẢI: một viên sỏi, một cú rơi xuống nước bắn tung tóe, một vệt bắn màu hồng trắng, một bàn tay bị tát đỏ ửng.",
  [], []),
 ("scene01", "Còn bồi thẩm đoàn", f"Hàng ghế bồi thẩm đoàn gồm các bạn nhỏ hoạt hình đủ màu da và vài con thú dễ thương, nửa số đang nhìn với đôi mắt trái tim, nửa còn lại nheo mắt nghi ngờ; ở GIỮA phía trước là {HERO} đang chớp mắt ngây thơ.",
  [], []),
 # ---------------- scene02 BẰNG CHỨNG #1
 ("scene02", 0, f"Một túi nilon đựng tang vật trong suốt kẹp nhãn trắng (nhãn trống không chữ) đặt trên bàn gỗ của tòa; bên trong túi chỉ có đúng MỘT viên sỏi xám bé xíu; đèn rọi vào; {NO_HERO}.",
  [], []),
 ("scene02", "Nhưng ở Nam Cực", f"Bản đồ lục địa Nam Cực hoạt hình nhìn từ trên: gần như toàn bộ phủ băng trắng, chỉ có vài mảng đá nâu xám nhỏ xíu dọc bờ biển được khoanh tròn đỏ; một chiếc kính lúp ở GIỮA-PHẢI soi vào một mảng đá. {NO_HERO}.",
  [("2%", "R", 380, "2%", "đất không có băng", [0.7, 0.55])], []),
 ("scene02", "Mỗi mùa xuân, hàng", "Một đoàn cánh cụt Adélie đông nghịt nối đuôi nhau lạch bạch đi từ biển băng lên một bãi đá trống, kéo dài tới tận chân trời, con nào cũng hăm hở.",
  [], []),
 ("scene02", "Và tổ của chúng", "Chia 3 ô: BÊN TRÁI tổ cỏ bị gạch chéo đỏ, Ở GIỮA tổ lông vũ bị gạch chéo đỏ, BÊN PHẢI một cái tổ tròn xếp bằng sỏi xám có dấu tích xanh lá to.",
  [], []),
 ("scene02", "Trung bình mỗi tổ", f"{HERO} ngậm một viên sỏi trong mỏ, mồ hôi nhễ nhại, cạnh một đống sỏi cao như núi nhỏ BÊN PHẢI; BÊN TRÁI là con mèo nhà ngồi nhìn ngạc nhiên để so sánh: con chim nặng bằng con mèo mà phải khuân cả núi đá.",
  [("200 viên", "R", 340, "200 VIÊN", "sỏi cho 1 cái tổ", [0.72, 0.5])], []),
 ("scene02", "Và thế là tội", f"Bãi đá với nhiều tổ sỏi: BÊN TRÁI một chú cánh cụt hàng xóm (không đeo nơ) đang quay lưng ngắm biển; BÊN PHẢI {HERO} đeo mặt nạ kẻ trộm đen che mắt, nhón chân rón rén tiến tới tổ hàng xóm.",
  [], []),
 ("scene02", "Ngoạm một viên! Quay", f"{HERO} ngậm một viên sỏi, chạy lạch bạch thật nhanh với vệt chuyển động phía sau, từ tổ hàng xóm BÊN TRÁI về tổ của mình BÊN PHẢI, mũi tên nét đứt chỉ đường đi.",
  [], []),
 ("scene02", "Có kẻ trộm xong", f"{HERO} đứng ngay sau lưng một chú cánh cụt hàng xóm đang ngủ gật trên tổ, một cánh đặt lên cằm như đang lựa chọn, mắt nheo nhìn viên sỏi đẹp nhất trong tổ của nạn nhân.",
  [], []),
 ("scene02", "Nạn nhân phát hiện", f"Cuộc rượt đuổi vòng quanh bãi đá: một chú cánh cụt hàng xóm giận dữ (không đeo nơ) giơ cánh đuổi theo {HERO} đang ngậm sỏi bỏ chạy; cả hai chạy rất chậm như quay chậm, bên cạnh có một con ốc sên đang vượt qua họ.",
  [("2km/h", "L", 360, "2 KM/H", "tốc độ rượt đuổi", [0.5, 0.55])], []),
 ("scene02", "Điều buồn cười nhất", f"{HERO} đội mũ bảo vệ, cầm đèn pin, đứng gác cái tổ sỏi của mình như bảo vệ ngân hàng, mắt đảo nghi ngờ; BÊN TRÁI một nhóm làm phim tài liệu (người cầm máy quay) đang lén quay lại.",
  [], []),
 ("scene02", "Bồi thẩm đoàn thử", "Nhìn từ trên cao: một vòng tròn khổng lồ gồm rất nhiều tổ sỏi, mỗi chú cánh cụt đều đang lén lấy sỏi của tổ bên cạnh, các mũi tên nhỏ nối thành một vòng xoay; ở giữa vòng tròn có một viên sỏi phát sáng đi theo đường nét đứt quay về đúng tổ ban đầu.",
  [("5 triệu", "R", 400, "5 TRIỆU", "dân số khu phố", [0.5, 0.5])], []),
 ("scene02", "Còn ở họ hàng", "Một chú cánh cụt Gentoo (mỏ cam đỏ, vệt trắng trên đỉnh đầu, chân cam) quỳ một chân, hai cánh dâng lên một viên sỏi tròn bóng lấp lánh như nhẫn kim cương cho một cô cánh cụt Gentoo đang ôm má e thẹn, trái tim bay quanh.",
  [], []),
 ("scene02", "Mà bồi thẩm đoàn biết", f"{HERO} đứng bên tổ sỏi đúng chỗ cũ, cạnh tổ cắm một hòm thư nhỏ hình ngôi nhà (không chữ); xa xa một cô cánh cụt Adélie đeo nơ hồng đang đi tới, bong bóng nghĩ của cô vẽ hình cái tổ năm ngoái giống hệt; trái tim nhỏ bay lên.",
  [], [], "L85"),
 ("scene02", "Tổ xấu quá thì", "Một chú cánh cụt (không đeo nơ) đứng cạnh cái tổ lèo tèo chỉ vài viên sỏi, mặt hi vọng; cô cánh cụt đeo nơ hồng ngẩng cao đầu đi lướt qua, mắt nhìn đi chỗ khác, vẻ coi như không quen biết; chú kia há mỏ thất vọng hài hước.",
  [], [], "L86"),
 ("scene02", "Thưa tòa, cháu không", f"Trong vành móng ngựa: {HERO} chắp hai cánh trước ngực làm mặt ngây thơ, mắt to long lanh; phía sau lưng chú lộ ra một viên đá xám tròn nhỏ; BÊN PHẢI {JUDGE} nhướng một bên mày, mỉm cười hài hước.",
  [], []),
 ("scene02", "Bồi thẩm đoàn đã", f"{HERO} đứng trước bức tường đo chiều cao kiểu chụp ảnh can phạm (chỉ có vạch kẻ ngang, không số), hai cánh ôm một viên sỏi, mặt phụng phịu; đèn flash máy ảnh lóe sáng.",
  [], []),
 # ---------------- scene03 BẰNG CHỨNG #2
 ("scene03", 0, "Mép băng lúc chiều tà, trời cam tím: hàng trăm chú cánh cụt Adélie đứng chen chúc sát mép tảng băng nhìn xuống làn nước biển xanh thẫm phía dưới.",
  [], []),
 ("scene03", "Ai cũng đói. Ai", f"Cận cảnh vài chú cánh cụt trên mép băng ôm bụng đói, bong bóng suy nghĩ phía trên vẽ cá bạc và tôm nhỏ màu hồng; nhưng các ngón chân dừng sát mép băng, run run, không ai dám bước; {HERO} đứng ở hàng giữa.",
  [], []),
 ("scene03", "Vì dưới làn nước", f"Mặt cắt ngang tảng băng và biển: phía trên là chân các chú cánh cụt sát mép, phía dưới mặt nước tối om có một cái bóng to lớn mờ mờ với hai con mắt phát sáng đang rình. {NO_HERO}.",
  [], []),
 ("scene03", "Hải cẩu báo! Dài", f"Một con hải cẩu báo (leopard seal) hoạt hình to dài, thân thon màu xám bạc có đốm đen, đầu to như đầu rắn, nằm dọc khung hình; một chiếc thước dây vàng kéo từ mũi tới đuôi. {NO_HERO}.",
  [("3,5m", "L", 330, "3,5 M", "chiều dài hải cẩu báo", [0.5, 0.62]), ("500kg", "R", 470, "500 KG", "nặng như con bò", [0.62, 0.42])], []),
 ("scene03", "Cái đầu to như", f"Cận cảnh đầu hải cẩu báo há miệng rộng (không máu, phong cách hài), lộ hàm răng nanh dài nhọn trắng, mắt láu cá. {NO_HERO}.",
  [], []),
 ("scene03", "Nó nấp ngay dưới", "Mặt cắt mép băng: hải cẩu báo nấp sát dưới mép băng, chỉ ló mỗi cái mũi trên mặt nước; phía trên mép băng các chú cánh cụt chưa hề hay biết.",
  [], []),
 ("scene03", "So với Quý ông", f"So sánh hài hước: BÊN TRÁI {HERO} bé xíu; BÊN PHẢI hải cẩu báo được vẽ như một chiếc xe tải có bánh xe và hàm răng nanh to đùng, cười nhe răng.",
  [], []),
 ("scene03", "Và thế là cảnh", f"Đám đông cánh cụt trên mép băng chen chúc huých nhau, ủn nhau, cánh vung loạn xạ, mặt hoảng hốt, giống giờ tan tầm; {HERO} kẹt ở giữa đám đông.",
  [], []),
 ("scene03", "Con đứng hàng đầu", "Một chú cánh cụt (không đeo nơ) đứng hàng đầu đang ngả người ra sau, hai chân bấu chặt mép băng, hai cánh chới với; phía sau mấy chú khác dồn lên ép tới.",
  [], []),
 ("scene03", "Và rồi tõm Một", "Chú cánh cụt xui xẻo (không đeo nơ) rơi tõm xuống nước tạo cột nước bắn tung tóe hình vương miện, chữ tượng thanh được thay bằng các tia nước to.",
  [], ["tõm"]),
 ("scene03", "Cả bầy lập tức", f"Cả bầy cánh cụt trên mép băng nghển cổ nhìn xuống nước, mắt mở to nín thở như khán giả xem phim kinh dị, có con ôm hộp bỏng ngô, có con che mắt hé nhìn; {HERO} cắn móng cánh.",
  [], []),
 ("scene03", "Nếu bạn ấy bơi", "Chú cánh cụt dưới nước vẫy cánh vui vẻ bình an; phía trên cả bầy ào ào nhảy xuống theo như đi tắm biển ngày hè, có con đeo kính bơi, có con mang phao vịt.",
  [], []),
 ("scene03", "Còn nếu không thì", f"Cả bầy cánh cụt lùi lại xa mép băng một bước, đứng thành hàng lo lắng, mồ hôi rơi, nhìn đồng hồ cát; mặt nước phía trước chỉ còn bong bóng (không có cảnh bạo lực); {HERO} đứng ở cuối hàng.",
  [], []),
 ("scene03", "Nhân chứng của vụ", f"Năm 1911: một bác sĩ thám hiểm người Anh hoạt hình, râu mép, mặc áo lông thú dày và mũ len, ngồi trên thùng gỗ cạnh túp lều gỗ phủ tuyết, cầm sổ tay và bút chì quan sát đàn cánh cụt Adélie; phong cách hơi cổ điển màu nâu sepia nhẹ.",
  [("1911", "R", 330, "1911", "Cape Adare", [0.3, 0.5])], []),
 ("scene03", "Ông ghi lại cảnh", "Trang sổ tay mở rộng với hình phác thảo bằng bút chì: các chú cánh cụt né qua né lại trên mép băng và đẩy nhau xuống nước, có mũi tên phác thảo; bàn tay bác sĩ cầm bút chì đang vẽ.",
  [], []),
 ("scene03", "Mấy con đứng sau", "Vòng tròn hài hước: những chú cánh cụt hàng đầu suýt rơi liền chạy vòng ra phía sau đám đông để đẩy lại, tạo thành một vòng xoay vô tận có mũi tên tròn; một ông lão nhân chứng râu bạc ở góc trái kể lại, tay chỉ vào.",
  [], []),
 ("scene03", "Bồi thẩm đoàn nghe", f"Trò kéo co ngược chiều: hai đội cánh cụt đứng hai bên mép băng cố đẩy ngược nhau về phía nước; BÊN PHẢI một chú (không đeo nơ) thắng cuộc thong thả ăn con cá, BÊN TRÁI chú thua cuộc bơi dưới nước liếc nhìn lo lắng; {HERO} làm trọng tài thổi còi.",
  [], []),
 # ---------------- scene04 BẰNG CHỨNG #3
 ("scene04", 0, f"{HERO} nằm ấp trứng trên tổ sỏi, mặt kiên nhẫn mệt mỏi, xung quanh các tờ lịch bay vèo vèo thể hiện nhiều ngày trôi qua, tuyết rơi trên đầu; BÊN PHẢI một chiếc khăn phủ che một 'vũ khí' bí ẩn hình ống.",
  [], []),
 ("scene04", "Nó đứng dậy, quay", f"Phong cách hoạt hình hài nhẹ nhàng, thân thiện trẻ em: {HERO} đứng ở mép tổ, quay lưng ra ngoài, chổng đuôi lên, phóng ra một vệt chất lỏng trắng hồng thành đường vòng cung bay xa như vòi nước, vẻ mặt tỉnh bơ; quả trứng trong tổ vẫn sạch sẽ.",
  [], ["bắn"]),
 ("scene04", "Cứ thế, quanh mỗi", "Nhìn từ trên cao: nhiều cái tổ sỏi tròn, quanh mỗi tổ có các vệt trắng hồng tỏa ra đều như tia nắng mặt trời hoặc như vết súng sơn, tạo thành một bức tranh hoa văn đẹp mắt trên bãi đá.",
  [], []),
 ("scene04", "Chuyện nghe thì buồn", "Hai nhà khoa học hoạt hình mặc áo khoác đỏ, một người quỳ cầm thước dây đo độ dài một vệt trắng hồng trên tuyết, người kia cầm máy tính bỏ túi và bảng kẹp giấy với công thức vẽ nguệch ngoạc (không chữ đọc được); một chú cánh cụt đứng nhìn ngơ ngác.",
  [("2003", "R", 330, "2003", "đo vệt phân", [0.4, 0.62])], []),
 ("scene04", "Kết quả: 10-60 kPa", "BÊN TRÁI một chú cánh cụt với chiếc đồng hồ đo áp suất to dán bên cạnh, kim vọt lên vùng đỏ; BÊN PHẢI một chiếc lốp xe hơi với đồng hồ đo áp suất kim cao gấp đôi; dấu bằng một nửa ở giữa.",
  [("10-60 kPa", "L", 340, "60 KPA", "áp suất cực đại", [0.22, 0.4])], []),
 ("scene04", "Công trình này còn", "Lễ trao giải vui nhộn: hai nhà khoa học trên sân khấu cầm chiếc cúp hình chú cánh cụt vàng, khán giả bên dưới cười nghiêng ngả, pháo giấy bay.",
  [("2005", "R", 340, "IG NOBEL", "giải năm 2005", [0.5, 0.4])], []),
 ("scene04", "Chưa hết! Năm 2020", "Hai nhà khoa học Nhật Bản hoạt hình đeo kính đứng cạnh tấm bảng trắng vẽ một đường parabol và các mũi tên lực (không chữ); BÊN PHẢI một chú cánh cụt Humboldt (mặt có mảng da hồng quanh mỏ, một vạch đen ngang ngực) đứng trên tảng đá.",
  [("2020", "R", 330, "2020", "tính lại tầm bắn", [0.25, 0.45])], []),
 ("scene04", "Kết quả: tầm bắn", "Chú cánh cụt Humboldt đứng trên tảng đá BÊN TRÁI, một đường vòng cung nét đứt bay sang BÊN PHẢI đáp xuống cạnh một lá cờ cắm trên đất; một thước dây vàng kéo dài bên dưới dọc theo đường bay.",
  [("1,34m", "R", 360, "1,34 M", "tầm bắn xa nhất", [0.78, 0.68]), ("8km/h", "L", 470, "8 KM/H", "tốc độ bay", [0.45, 0.35])], []),
 ("scene04", "Nếu đổi sang cỡ", "So sánh quy mô: BÊN TRÁI một chú cánh cụt nhỏ với đường vòng cung ngắn; BÊN PHẢI một người đàn ông hoạt hình đứng cạnh một đường vòng cung khổng lồ dài gấp nhiều lần chạm tới lá cờ xa, ông ta ôm mặt ngượng ngùng; phong cách hài lịch sự.",
  [("3m", "R", 360, "> 3 M", "nếu là con người", [0.85, 0.7])], []),
 ("scene04", "Và họ nghiêm túc", "Một nhân viên thủy cung hoạt hình mặc áo mưa vàng, đội mũ bảo hộ, cầm ô che, đứng sau một vạch kẻ an toàn màu vàng đen trên sàn, cách xa một chú cánh cụt Humboldt đang chổng đuôi; mặt nhân viên cảnh giác buồn cười.",
  [("1,34m", "L", 400, "1,34 M", "khoảng cách an toàn", [0.5, 0.78])], []),
 ("scene04", "Và vũ khí này", f"Không gian vũ trụ: một vệ tinh nhân tạo có tấm pin mặt trời bay trên quỹ đạo, bên dưới là quả địa cầu nhìn thấy lục địa Nam Cực trắng xóa; ống kính vệ tinh chiếu tia sáng xuống. {NO_HERO}.",
  [], []),
 ("scene04", "Năm 2012, các nhà", "Các nhà khoa học hoạt hình ngồi trước màn hình máy tính lớn hiển thị ảnh vệ tinh: nền băng trắng có những mảng màu nâu đỏ được khoanh tròn; một người chỉ tay ngạc nhiên, người kia cầm cốc trà.",
  [("2012", "R", 330, "2012", "soi ảnh vệ tinh", [0.55, 0.4])], []),
 ("scene04", "Lần theo dấu vết", "Một đàn cánh cụt hoàng đế khổng lồ (to cao, mảng vàng cam ở cổ và má, mỏ dài có vạch cam) đứng đông nghịt tới tận chân trời trên băng, cạnh đàn là một mảng màu nâu; vài chú con lông xám đứng giữa chân bố mẹ.",
  [("46", "L", 340, "46 ĐÀN", "cánh cụt hoàng đế", [0.4, 0.5]), ("595.000", "R", 460, "595.000", "con được đếm", [0.65, 0.45])], []),
 ("scene04", "Bồi thẩm đoàn thấy", f"Một tấm ảnh vệ tinh khổng lồ treo trong tòa như tấm áp phích truy nã, trên ảnh là một vệt nâu chỉ thẳng tới một băng nhóm cánh cụt đang ngơ ngác; phía trước {HERO} lấy cánh che mặt xấu hổ.",
  [], []),
 # ---------------- scene05 BẰNG CHỨNG #4
 ("scene05", 0, f"Một nhà nghiên cứu hoạt hình mặc áo khoác cam, quỳ xuống cạnh tổ sỏi cầm một chiếc cân treo nhỏ định cân chú cánh cụt con lông xám; {HERO} đứng phắt dậy, mắt trợn giận dữ, lông dựng.",
  [], []),
 ("scene05", "Nó lao tới, đứng", f"{HERO} đứng thẳng người, vung cánh tát mạnh vào ống chân nhà nghiên cứu, các tia sao va chạm và vệt chuyển động; nhà nghiên cứu nhảy lò cò ôm chân, mặt méo xệch hài hước.",
  [], ["Phạch"]),
 ("scene05", "Cánh chim cánh cụt", "Hình mặt cắt kỹ thuật kiểu sách giáo khoa: chiếc cánh cánh cụt dẹt như mái chèo, bên trong lộ xương dẹt đặc màu kem; BÊN PHẢI để so sánh là một cây thước kẻ gỗ và một mái chèo gỗ có hình dạng tương tự.",
  [], []),
 ("scene05", "Không chỉ con người", f"Một con chim cướp biển Skua nâu sải cánh rộng sà xuống định cướp quả trứng; {HERO} nhảy lên vung cánh tát vào mỏ nó, lông Skua bay tán loạn.",
  [("hơn 1m", "R", 340, "> 1 M", "sải cánh chim Skua", [0.6, 0.3])], ["Tát"]),
 ("scene05", "Hải cẩu bò lên", f"Chia đôi khung: BÊN TRÁI {HERO} tát một con hải cẩu lông nâu đang bò lại quá gần tổ khiến nó giật mình lùi lại; BÊN PHẢI {HERO} tát luôn một chú cánh cụt hàng xóm vừa lấn sang nửa bước.",
  [], []),
 ("scene05", "Cả đời bị cáo", f"Chia đôi khung có nút công tắc ở giữa: BÊN TRÁI {HERO} đứng im dễ thương, má hồng, trái tim bay quanh; BÊN PHẢI cùng chú cánh cụt đó mắt đỏ rực, cánh vung tát ra liên tục như cánh quạt.",
  [], []),
 ("scene05", "Và đừng tưởng bị", f"{HERO} đi lạch bạch trên băng như ông cụ đi chợ, khoác giỏ đi chợ trên cánh, chậm rãi; phía sau là một con ốc sên đi cùng tốc độ.",
  [], []),
 ("scene05", "Nhưng xuống nước thì", f"Dưới nước xanh: {HERO} lao đi như tên lửa ngư lôi với vệt bọt khí dài phía sau, đuổi theo đàn cá bạc; bên trái có thang đo độ sâu vẽ vạch xuống tận đáy tối.",
  [("15km/h", "L", 340, "15 KM/H", "tốc độ bơi", [0.5, 0.45]), ("180m", "R", 470, "180 M", "lặn sâu nhất", [0.12, 0.85])], []),
 ("scene05", "và khi phóng lên", f"{HERO} phóng vọt khỏi mặt nước, bay cao lên theo đường cong và đáp gọn lên mặt một tảng băng cao, tư thế ngầu như đặc vụ đeo kính râm; một thước đo chiều cao dựng cạnh tảng băng.",
  [("2m", "R", 360, "2 M", "cú nhảy lên băng", [0.75, 0.3])], []),
 ("scene05", "Còn khi lười đi", f"{HERO} nằm sấp trên tuyết, lấy bụng trắng làm ván trượt, hai chân đạp phía sau tung tuyết, lướt vèo vèo xuống dốc với vệt tốc độ, mặt sung sướng như trẻ con chơi cầu trượt.",
  [], [], "L87"),
 ("scene05", "Còn tòa án gọi", f"Hài hước: {HERO} trượt bụng trên tuyết thoát khỏi một tòa án băng phía sau, miệng ngậm một viên sỏi; phía sau một chú cảnh sát hải cẩu nhỏ đội mũ cảnh sát chạy đuổi theo hụt hơi, còi thổi.",
  [], [], "L88"),
 ("scene05", "Công tố viên xin", f"{LAWYER} đứng BÊN TRÁI giơ tay chỉ mạnh vào bảng ghim 4 bằng chứng BÊN PHẢI: viên sỏi, cú rơi xuống nước, vệt bắn hồng trắng, cú tát vào ống chân; {HERO} ở góc dưới phải toát mồ hôi.",
  [], []),
 ("scene05", "Ngay cả nhân chứng", "Ông bác sĩ thám hiểm năm 1911 (râu mép, áo lông thú) cau mày nhìn một nhóm cánh cụt Adélie trẻ nghịch ngợm mặc áo khoác da, đội mũ lưỡi trai ngược, đang xô đẩy nhau phá phách trên bãi đá.",
  [], []),
 ("scene05", "Ông còn viết một", "Ông bác sĩ thám hiểm năm 1911 ngồi trong lều gỗ dưới ánh đèn dầu, lén lút che một trang nhật ký bằng tay, trên trang có các ký hiệu ngoằn ngoèo bí ẩn bị một ổ khóa vẽ đè lên; vẻ mặt bí mật hài hước.",
  [], []),
 ("scene05", "Bằng chứng đã đủ", f"{LAWYER} đập mạnh tập hồ sơ xuống bàn, giấy bay tứ tung; {JUDGE} trên bục nhìn xuống; {HERO} trong vành móng ngựa run cầm cập.",
  [], []),
 # ---------------- scene06 PHÁN QUYẾT
 ("scene06", 0, "Người đàn ông hoạt hình đeo kính tròn đang cởi chiếc áo choàng đen công tố viên ném sang một bên và khoác lên bộ vest xanh dương của luật sư bào chữa, tay giơ ngón trỏ 'phản đối', vẻ mặt quyết tâm; tia sáng đổi vai phía sau.",
  [], []),
 ("scene06", "Mỗi mùa xuân, tuyết", "Mùa xuân Nam Cực: tuyết tan thành những dòng nước lạnh xanh nhạt chảy tràn qua bãi đá làm tổ của đàn cánh cụt, tạo thành các vũng nước lớn.",
  [], []),
 ("scene06", "Quả trứng nằm sát", "Một quả trứng cánh cụt hoạt hình có khuôn mặt dễ thương nằm sát mặt đất trong vũng nước lạnh, run cầm cập, quấn khăn len, băng giá bám quanh; cái tổ thấp lè tè bị nước tràn vào.",
  [], []),
 ("scene06", "Một đống sỏi cao", f"{HERO} ngồi ấp 2 quả trứng trên một đống sỏi cao như hòn đảo nhỏ giữa dòng nước tan, trứng khô ráo an toàn; các tổ thấp xung quanh bị ngập; có chiếc phao cứu sinh vẽ mờ như biểu tượng.",
  [], []),
 ("scene06", "Thứ bị cáo trộm", f"{HERO} ôm hai quả trứng vào lòng trên tổ sỏi cao, ánh sáng vàng ấm áp tỏa quanh, trái tim nhỏ bay lên, khuôn mặt hiền hậu.",
  [], []),
 ("scene06", "nhiều nhà khoa học cho", "Cảnh giờ cao điểm ở mép băng như ga tàu điện ngầm đông nghịt: hàng trăm chú cánh cụt dồn lên, một chú đầu hàng bị đẩy ra mép một cách vô tình, ai cũng ngơ ngác không cố ý.",
  [], []),
 ("scene06", "Nhảy theo bầy lại", "Hàng trăm chú cánh cụt cùng lúc lao xuống nước tỏa ra mọi hướng; ở giữa một con hải cẩu báo xoay vòng chóng mặt, mắt quay mòng mòng không biết đuổi con nào.",
  [], []),
 ("scene06", "bắn phân ra xa là", f"{HERO} cầm một cây chổi nhỏ quét tổ sỏi sạch bóng lấp lánh, chú cánh cụt con lông xám ngồi trong tổ khô ráo vui vẻ; các vệt trắng hồng nằm xa bên ngoài tổ.",
  [], []),
 ("scene06", "tát cả nhà khoa học?", f"{HERO} bé nhỏ dang hai cánh đứng chắn trước tổ có hai quả trứng; phía trước là ba cái bóng khổng lồ cao gấp nhiều lần: chim Skua, hải cẩu báo và một nhà khoa học; chú cánh cụt không lùi bước, ánh mắt kiên định.",
  [], []),
 ("scene06", "Nếu đó là tội", f"{HERO} làm bố ôm chú cánh cụt con lông xám vừa nở, hai bố con dụi má nhau, trái tim to màu đỏ phía sau, cảnh ấm áp cảm động.",
  [], []),
 ("scene06", "Cộc cộc cộc Tòa", f"{JUDGE} gõ búa xuống bàn có các vạch tượng thanh rung; phía dưới {HERO} trong vành móng ngựa thở phào nhẹ nhõm nhưng đang bị yêu cầu đưa trả lại một viên sỏi.",
  [], ["Cộc cộc cộc"]),
 ("scene06", "Và thế là Quý", f"{HERO} lạch bạch rời khỏi tòa án quay về tổ, trong mỏ ngậm một viên sỏi mới vừa nhặt từ tổ nhà bên cạnh, liếc mắt tinh nghịch; chú hàng xóm phía sau đang ngủ không hay biết.",
  [], []),
 ("scene06", "Còn bạn, nếu là", "Hàng ghế bồi thẩm đoàn các bạn nhỏ hoạt hình đa dạng đang giơ thẻ bài: một nửa thẻ hình ngón cái hướng lên màu xanh, một nửa thẻ hình ngón cái hướng xuống màu đỏ, vẻ mặt đang suy nghĩ hào hứng; không có chữ trên thẻ.",
  [], []),
 ("scene06", "Tập sau, chúng ta", f"Phòng khám bác sĩ thú y hoạt hình sáng sủa: một chú gấu Koala lông xám, tai tròn bông xù, mũi đen to, ngồi trên ghế bệnh nhân mắt lờ đờ ngơ ngác, cạnh đó có ống nghe và tấm phim X-quang treo tường. {NO_HERO}.",
  [], []),
 ("scene06", "Bày sẵn đĩa lá", f"Chú gấu Koala ngồi trước một chiếc đĩa sứ đầy lá bạch đàn xanh tươi đặt ngay trước mặt, nhưng nhìn chằm chằm vào chiếc đĩa với dấu chấm hỏi to trên đầu, bụng sôi òng ọc; {NO_HERO}.",
  [], []),
]

# ---------------- Shorts 9:16
SB = [
 (0, f"Phòng xử án băng giá dọc: phía trên {JUDGE} gõ búa; phía dưới {HERO} trong vành móng ngựa gỗ, một cánh lén lút đẩy một chú cánh cụt khác về phía mép băng có nước biển xanh.", []),
 ("Chú chim cánh cụt mặc", f"{HERO} mặc vest đuôi tôm đen bóng đứng ở mép băng, một cánh đẩy lưng một chú cánh cụt khác (không đeo nơ) đang chới với sắp rơi xuống nước; phía dưới nước thấp thoáng bóng hải cẩu báo.", []),
 ("Bị cáo chỉ cao", f"{HERO} đứng cạnh một con mèo nhà màu cam cao gần bằng; phía sau thước đo chiều cao kẻ vạch; chú cánh cụt đi lạch bạch như trẻ mẫu giáo đeo cặp sách nhỏ.", [("70cm", "L", 620, "70 CM", "chiều cao bị cáo", [0.45, 0.4])]),
 ("Hiện trường: mép băng", "Mép băng Nam Cực dọc khung: hàng trăm chú cánh cụt chen chúc sát mép, ôm bụng đói, bong bóng nghĩ hình cá, nhưng không ai dám bước xuống nước.", []),
 ("Vì dưới nước là", "Mặt cắt dọc: phía trên mép băng là chân các chú cánh cụt; phía dưới là con hải cẩu báo xám đốm đen dài to, đầu như rắn, há miệng lộ răng nanh, đang nấp rình.", [("3,5m", "R", 560, "3,5 M", "hải cẩu báo", [0.5, 0.7]), ("500kg", "L", 900, "500 KG", "nặng như con bò", [0.45, 0.75])]),
 ("Thế là chen lên", "Đám đông cánh cụt chen lấn ủn nhau, một chú (không đeo nơ) bị dồn rơi tõm xuống nước tạo cột nước bắn tung tóe.", []),
 ("Cả bầy nín thở", f"Cả bầy cánh cụt nghển cổ nhìn xuống nước, mắt mở to, có con ôm bỏng ngô, có con che mắt; {HERO} cắn móng cánh.", []),
 ("Bạn ấy bơi đi", "Chú cánh cụt dưới nước vẫy cánh bình an, cả bầy ào ào nhảy xuống theo như đi tắm biển, có con đeo kính bơi, có con mang phao vịt.", []),
 ("Chưa hết, bị cáo", f"{HERO} đeo mặt nạ kẻ trộm ngậm một viên sỏi rón rén bỏ chạy khỏi tổ hàng xóm đang ngủ gật.", []),
 ("và bắn phân xa", f"Phong cách hoạt hình hài thân thiện trẻ em: {HERO} đứng trên tổ sỏi chổng đuôi phóng một vệt trắng hồng thành vòng cung bay xa, có thước dây vàng đo bên dưới tới lá cờ.", [("1,34m", "R", 620, "1,34 M", "tầm bắn", [0.7, 0.62])]),
 ("Nhưng khoan, nhiều nhà", f"Một nhà khoa học hoạt hình mặc áo khoác đỏ cầm kính lúp quan sát đám cánh cụt ở mép băng, giơ một tay ra hiệu 'khoan đã'; {HERO} đứng cạnh gật gù đồng ý, vẻ mặt được minh oan.", [], "S13"),
 ("chỉ là chen lấn", "Cảnh giờ cao điểm ở mép băng như ga tàu điện đông nghịt: hàng trăm chú cánh cụt dồn lên, chú đầu hàng bị đẩy ra mép vô tình, ai cũng ngơ ngác.", []),
 ("Vậy bị cáo có", f"Cận cảnh {HERO} trong vành móng ngựa ngước nhìn thẳng ra người xem với đôi mắt to long lanh ngây thơ, hai cánh ôm một viên sỏi sau lưng, {JUDGE} cầm búa phía sau lưỡng lự.", []),
]

STYLE_L = ("tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, "
           "tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, "
           "không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng")


def tokens_of(scene_id: str) -> list[str]:
    sc = next(s for s in EP["longform"]["scenes"] if s["id"] == scene_id)
    return script_tokens(" ".join(ptext(x) for x in sc["parts"]), DISPLAY)


def find(toks: list[str], phrase, after: int = 0) -> int:
    if phrase in (0, "0", ""):
        return 0
    want = [norm(x) for x in phrase.split() if norm(x)]
    n = [norm(t) for t in toks]
    for i in range(after, len(toks) - len(want) + 1):
        if n[i:i + len(want)] == want:
            return i
    raise SystemExit(f"phrase not found: {phrase!r}")


def check_sticker(toks, phrase, lo, hi, where):
    try:
        i = find(toks, phrase, lo)
    except SystemExit:
        raise SystemExit(f"{where}: sticker phrase {phrase!r} not found")
    if i >= hi:
        print(f"  !! {where}: sticker {phrase!r} spoken after this beat ends")


def main():
    plan = {"_doc": "Sinh bởi scripts/build_plans.py — sửa ở đó rồi chạy lại.", "targets": {}, "scenes": {}}
    prompts, catalog = {}, []
    titles = {s["id"]: s for s in EP["longform"]["scenes"]}
    by_scene: dict = {}
    for b in B:
        by_scene.setdefault(b[0], []).append(b)
    n = 0
    for k, (sid, beats) in enumerate(by_scene.items(), 1):
        toks = tokens_of(sid)
        idx = []
        for b in beats:  # pipeline.spec finds the FIRST match -> phrases must be unique in the chapter
            i = find(toks, b[1])
            if b[1] not in (0, "0", "") and idx and i <= idx[-1]:
                raise SystemExit(f"{sid}: phrase {b[1]!r} first occurs before the previous beat — make it unique")
            idx.append(i)
        for a, c in zip(idx, idx[1:]):
            if c <= a:
                raise SystemExit(f"{sid}: beats out of order near index {c}")
        st = titles[sid]
        sp = {"chapter_no": k, "badge": st["badge"], "title": st["chapter_title"].split(":", 1)[-1].strip().upper(),
              "hook": st.get("hook", ""), "card": k != 1, "beats": []}
        for j, b in enumerate(beats):
            if len(b) > 5:
                img = b[5]
            else:
                n += 1
                if n == 29:  # L29 (cân 500kg) bỏ khỏi plan — beat quá ngắn (1,6s); giữ số cho ảnh sau
                    n += 1
                img = f"L{n:02d}"
            end = idx[j + 1] if j + 1 < len(beats) else len(toks)
            line = " ".join(toks[idx[j]:end])
            for s in b[3]:
                check_sticker(toks, s[0], idx[j], end, f"{sid}/{img}")
            sp["beats"].append({"at": b[1], "image": f"assets/long/{img}.png",
                                "stickers": [{"at": s[0], "side": s[1], "y": s[2], "value": s[3], "label": s[4], "target": s[5]} for s in b[3]],
                                "impacts": b[4]})
            prompts[img] = (f"HÌNH {img} (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật {HERO_S}; nền trắng tinh "
                            f"hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: \"{line}\". Bố cục: {b[2]}")
            catalog.append(f"| {img} | {sid} | {line[:90]} |")
        plan["scenes"][sid] = sp
    stoks = script_tokens(EP["shorts"]["text"], DISPLAY)
    sidx = [find(stoks, b[0]) for b in SB]
    splan = {"title_lines": ["ĐẨY BẠN XUỐNG BIỂN", "ĐỂ THỬ HẢI CẨU?!"], "beats": []}
    k_s = 0
    for j, b in enumerate(SB):
        if len(b) > 3:
            img = b[3]
        else:
            k_s += 1
            img = f"S{k_s:02d}"
        end = sidx[j + 1] if j + 1 < len(SB) else len(stoks)
        for s in b[2]:
            check_sticker(stoks, s[0], sidx[j], end, f"shorts/{img}")
        bt = {"at": b[0], "draw_s": 1.0, "image": f"assets/shorts/{img}.png",
              "stickers": [{"at": s[0], "side": s[1], "y": s[2], "value": s[3], "label": s[4], "target": s[5]} for s in b[2]]}
        if j == 0:
            bt = {"at_s": 0.0, **{k2: v for k2, v in bt.items() if k2 != "at"}}
        splan["beats"].append(bt)
        line = " ".join(stoks[sidx[j]:end])
        prompts[img] = (f"HÌNH {img} (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật {HERO_S}; nền trắng tinh "
                        f"hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: \"{line}\". Bố cục: {b[1]}")
    first_l = (f"Tạo hình ảnh (cảnh 1/{n} của video YouTube về Chim Cánh Cụt). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: {STYLE_L}. "
               f"NHÂN VẬT CHÍNH cố định: {HERO}. Nhân vật phụ cố định: {JUDGE}; {LAWYER}. ") + prompts["L01"]
    first_s = (f"Tạo hình ảnh (cảnh 1/{len(SB)} của video YouTube Shorts về Chim Cánh Cụt). QUY CHUẨN CHUNG cho mọi cảnh: "
               f"{STYLE_L.replace('NGANG 16:9', 'DỌC 9:16')}. NHÂN VẬT CHÍNH cố định: {HERO}. Nhân vật phụ: {JUDGE}. ") + prompts["S01"]
    out = {"_first_long": first_l, "_first_shorts": first_s, **prompts}
    (P / "specs").mkdir(exist_ok=True)
    (P / "specs" / "longform_plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=1), encoding="utf-8")
    (P / "specs" / "shorts_plan.json").write_text(json.dumps(splan, ensure_ascii=False, indent=1), encoding="utf-8")
    (P / "specs" / "image_prompts.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    (P / "specs" / "image_catalog.md").write_text("| Ảnh | Chương | Lời thoại khi ảnh hiện |\n|---|---|---|\n" + "\n".join(catalog) + "\n",
                                                  encoding="utf-8")
    print(f"OK: {n}+inserts long images, {len(SB)} shorts images, {len(prompts)} prompts")


if __name__ == "__main__":
    main()

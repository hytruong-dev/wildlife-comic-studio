import json
from pathlib import Path

ep_path = Path("projects/tap-44-ca-mat-trang/episode.json")
data = json.loads(ep_path.read_text(encoding="utf-8"))

# Update display_fix
display_fix = {
    "bốn mươi tư": "44",
    "Bốn mươi tư": "44",
    "bốn mươi bốn": "44",
    "Bốn mươi bốn": "44",
    "Tập bốn mươi tư": "Tập 44",
    "bốn mươi ba": "43",
    "Bốn mươi ba": "43",
    "bốn mươi lăm": "45",
    "Bốn mươi lăm": "45",
    "số bốn mươi tư": "số 44",
    "Số bốn mươi tư": "Số 44",
    "số bốn mươi lăm": "số 45",
    "Số bốn mươi lăm": "Số 45",
    "hai tấn": "2 tấn",
    "Hai tấn": "2 tấn",
    "mười tấn": "10 tấn",
    "Mười tấn": "10 tấn",
    "ba mét": "3 mét",
    "Ba mét": "3 mét",
    "bốn mét": "4 mét",
    "Bốn mét": "4 mét",
    "ba trăm triệu": "300 triệu",
    "Ba trăm triệu": "300 triệu",
    "tám trăm mét": "800 mét",
    "Tám trăm mét": "800 mét",
    "bốn độ C": "4°C",
    "Bốn độ C": "4°C",
    "chín mươi chín phần trăm": "99%",
    "Chín mươi chín phần trăm": "99%",
    "bốn mươi loài": "40 loài",
    "Bốn mươi loài": "40 loài",
    "ba chấm hai ki-lô-mét một giờ": "3.2 km/h",
    "Ba chấm hai ki-lô-mét một giờ": "3.2 km/h",
    "hai mươi bốn giờ": "24 giờ",
    "Hai mươi bốn giờ": "24 giờ",
    "hàng chục triệu năm": "hàng chục triệu năm",
    "Hàng chục triệu năm": "Hàng chục triệu năm",
    "hàng trăm triệu": "hàng trăm triệu",
    "Hàng trăm triệu": "Hàng trăm triệu",
    "hàng trăm cân": "hàng trăm cân",
    "Hàng trăm cân": "Hàng trăm cân",
    "một trăm mét khối": "100 m³",
    "Một trăm mét khối": "100 m³",
    "bảy chấm năm xăng-ti-mét": "7.5 cm",
    "Bảy chấm năm xăng-ti-mét": "7.5 cm",
    "hai mi-li-mét": "2 mm",
    "Hai mi-li-mét": "2 mm",
    "sáu mươi triệu lần": "60 triệu lần",
    "Sáu mươi triệu lần": "60 triệu lần",
    "sáu mươi triệu": "60 triệu",
    "Sáu mươi triệu": "60 triệu",
    "bốn cân": "4 kg",
    "Bốn cân": "4 kg",
    "chục cây số": "chục cây số",
    "không một loài": "không 1 loài",
    "Không một loài": "Không 1 loài",
    "không một": "không 1",
    "Không một": "Không 1",
    "hàng ngàn": "hàng 1.000",
    "Hàng ngàn": "Hàng 1.000",
    "hàng loạt": "hàng loạt",
    "Hàng loạt": "Hàng loạt",
    "triệu năm": "triệu năm",
    "trăm triệu": "trăm triệu",
    "một trăm": "100",
    "Một trăm": "100"
}
data["display_fix"] = display_fix

# Scenes update
scenes = data["longform"]["scenes"]

# Scene 02: Add Part 4 (Lớp da collagen 7.5cm)
sc2_parts = scenes[1]["parts"]
if len(sc2_parts) == 4:
    sc2_parts.append({
        "text": "Chưa hết đâu nhé, hãy nhìn vào tấm sinh thiết lớp biểu bì của gã! Cơ thể cá mặt trăng hoàn toàn không có vảy cá thông thường, mà được bọc kín bởi một lớp da collagen dày tới bảy chấm năm xăng-ti-mét, dẻo dai tựa như lớp lốp xe tải bọc thép! Phía trên bề mặt da phủ đầy những chiếc gai vi thể li ti tiết ra lớp chất nhờn kháng khuẩn trơn tuột, biến cơ thể gã thành một pháo đài đệm thịt êm ái hấp thụ mọi va đập giữa lòng đại dương sóng gió!",
        "mood": "hao_hung"
    })

# Scene 03: Add Part 2 (Cụm răng họng và ép nước ly tâm)
sc3_parts = scenes[2]["parts"]
if len(sc3_parts) == 3:
    sc3_parts.insert(2, {
        "text": "Nhưng nuốt một con sứa trơn tuột đầy chất nhầy vào bụng không hề đơn giản chút nào! Hãy cầm đèn pin soi sâu vào khoang miệng của bệnh nhân: Toàn bộ phần cuống họng của cá mặt trăng được trang bị những cụm răng họng nhọn hoắt xếp cong về phía sau! Khi gã hút nước nuốt sứa vào, chiếc cuống họng này hoạt động như một chiếc máy ép nước ly tâm: Răng họng giữ chặt con mồi không cho trôi ngược ra ngoài, đồng thời cơ họng co bóp cực mạnh để ép kiệt nước biển thừa ra khỏi mang trước khi tống cả tảng thạch sứa đậm đặc vào dạ dày tiêu hóa!",
        "mood": "hao_hung"
    })

# Scene 04: Add Part 4 (Cú phóng nhảy 3m đập bẹp đè bẹp ký sinh trùng)
sc4_parts = scenes[3]["parts"]
if len(sc4_parts) == 4:
    sc4_parts.append({
        "text": "Đặc biệt hơn nữa, nếu liệu trình spa bằng chim mòng biển vẫn chưa giải quyết dứt điểm những con bọ bám dai dẳng, Gã khổng lồ vô tri sẽ kích hoạt tuyệt chiêu thể dục dưỡng sinh có một không hai: Gã lấy đà từ dưới làn nước sâu, quạt hai cánh vây hết tốc lực rồi phóng vọt cả khối thân nặng hai tấn bay thẳng lên khỏi mặt biển cao tới ba mét! [laughter] Sau đó, gã thả tự do rơi tự do rồi đập cả tấm thân dẹt khổng lồ xuống mặt nước đánh BẸP một tiếng vang dội như một vụ nổ pháo hoa! Cú va chạm bề mặt kinh thiên động địa ấy đủ sức đánh văng hàng loạt loài rận biển cứng đầu ra khỏi da thịt trong sự ngỡ ngàng của giới quan sát!",
        "mood": "hao_hung"
    })

# Scene 05: Add Part 2 (Ấu trùng phi thuyền ngoài hành tinh 2mm gai nhọn)
sc5_parts = scenes[4]["parts"]
if len(sc5_parts) == 3:
    sc5_parts.insert(2, {
        "text": "Hãy nhìn vào bức ảnh siêu âm ấu trùng của bệnh nhân: Chú cá con lúc mới chui ra khỏi vỏ trứng chỉ dài vỏn vẹn hai mi-li-mét, nhỏ hơn cả đầu tăm nhưng lại mang một ngoại hình cực kỳ tấu hài: Toàn thân chú cá con tròn ủng như một quả cầu gai, xung quanh mọc chìa ra hàng chục chiếc gai nhọn hoắt trông hệt như một chiếc phi thuyền người ngoài hành tinh tí hon! Chiếc áo giáp gai nhọn ấy giúp ấu trùng trôi nổi như sinh vật phù du và bảo vệ chúng khỏi miệng những kẻ săn mồi tí hon dưới đáy biển sâu!",
        "mood": "hao_hung"
    })

ep_path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
print("Updated episode.json successfully!")


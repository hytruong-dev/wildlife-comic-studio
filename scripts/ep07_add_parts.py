"""Tập 7: speed the voice up (tempo 1.10) and append 3 new narration parts so the long-form stays >= 8:30."""
import json
from pathlib import Path

p = Path("projects/tap-07-tom-tit/episode.json")
e = json.loads(p.read_text(encoding="utf-8"))
NEW = {
    "scene02": "Mà khoan đã, đó mới chỉ là phe đấm thôi! Họ hàng nhà Tôm Tít còn có cả phe đâm, mang đôi càng đầy gai nhọn "
               "như chiếc xiên nướng, phóng ra xiên trúng con cá đang bơi ngang chỉ trong tích tắc. [laughter] Một phe đấm bốc, "
               "một phe đấu kiếm, đúng là cả một gia tộc võ lâm dưới đáy biển!",
    "scene03": "Mà cái hay nhất là gì biết không? Đôi búa ấy chẳng bao giờ phải đem đi sửa! Cứ mỗi lần lột xác, Tôm Tít lại được "
               "thay luôn một cặp búa mới tinh, cứ như võ sĩ được tài trợ đôi găng mới sau mỗi mùa giải vậy! [laughter] "
               "Nhưng cái giá của món quà đó thì... lát nữa bạn sẽ biết!",
    "scene05": "[surprise-oh] Chưa hết đâu! Tôm Tít còn dùng chính ánh sáng phân cực để nhắn tin bí mật cho nhau, trên cơ thể có "
               "những mảng phát tín hiệu mà kẻ thù nhìn vào chẳng thấy gì. Và gã giang hồ cục súc này hóa ra lại là một người "
               "chồng chung thủy: có loài sống thành cặp trong cùng một hang tới hai mươi năm! [laughter] Ra ngoài thì đấm nứt "
               "kính, về nhà thì ngoan như mèo!",
}
for sc in e["longform"]["scenes"]:
    if sc["id"] in NEW and NEW[sc["id"]] not in sc["parts"]:
        sc["parts"].append(NEW[sc["id"]])
e["voice"]["tempo_long"] = 1.10
e["voice"]["tempo_shorts_min"] = 1.10
e["display_fix"]["hai mươi năm"] = "20 năm"
p.write_text(json.dumps(e, ensure_ascii=False, indent=2), encoding="utf-8")
print("ok", sum(len(x) for x in NEW.values()), "chars added")

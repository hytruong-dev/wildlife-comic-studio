import json
from pathlib import Path

sb_path = Path("projects/tap-36-chim-go-kien/specs/storyboard.json")
sb = json.loads(sb_path.read_text(encoding="utf-8"))

sb["characters"]["CU_VO"] = "Kỹ sư Cú Vọ già đeo kính lão tròn đọc tài liệu"
sb["characters"]["CHUOT_CHUI"] = "Chuột chũi thợ mỏ mặc yếm cầm máy khoan mini"
sb["characters"]["SOC_BAY"] = "Sóc bay thợ hàn đeo kính đen cầm que hàn"
sb["characters"]["KHI_DAU_CHO"] = "Khỉ đầu chó thanh tra an toàn lao động cầm bảng kẹp hồ sơ"
sb["characters"]["NGUOI_QUE"] = "Người que ngất xỉu vì va đầu vào gỗ"
sb["characters"]["KY_SU_CO_KHI"] = "Kỹ sư cơ khí choáng váng đo gia tốc"

sb["side_characters"] = ["CU_VO", "CHUOT_CHUI", "SOC_BAY", "KHI_DAU_CHO"]
sb["shorts_side_characters"] = ["NGUOI_QUE", "KY_SU_CO_KHI"]

# Fix S06 sticker value
sb["shorts"][5]["stickers"][0]["value"] = "120 LẦN"

sb_path.write_text(json.dumps(sb, ensure_ascii=False, indent=2), encoding="utf-8")
print("Updated characters and S06 sticker value successfully!")


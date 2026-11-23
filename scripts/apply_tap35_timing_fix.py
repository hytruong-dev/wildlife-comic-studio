import json
from pathlib import Path

P = Path("projects/tap-35-ca-voi-sat-thu")
sb_file = P / "specs/storyboard.json"
sb = json.loads(sb_file.read_text(encoding="utf-8"))

# Long beats
# Scene 01 (12 beats: L01..L12)
# Fix b07, b11, b12
for b in sb["long"]:
    if b.get("scene") == "scene01":
        if b.get("at") == "Chế độ mẫu hệ Matriarchy":
            # b07
            b["at"] = "bản đồ hải lưu"
        elif b.get("at") == "gia tộc Bố Già đã quyết định ra tay":
            # b12
            b["at"] = "chiếc ca nô cao tốc"

# Scene 02 (11 beats: L13..L23)
# Fix b08, b09, b10, b11
# Original:
# b08: không hề có bất kỳ sự tranh giành
# b09: các sát thủ trưởng thành sẽ dùng mõm
# b10: trường học huấn luyện quân sự thực thụ
# b11: truyền lại từ đời này sang đời khác
for b in sb["long"]:
    if b.get("scene") == "scene02":
        if b.get("at") == "các sát thủ trưởng thành sẽ dùng mõm":
            # change b09 to chia sẻ miếng ăn sòng phẳng
            b["at"] = "chia sẻ miếng ăn sòng phẳng"
        elif b.get("at") == "trường học huấn luyện quân sự thực thụ":
            # change b10 to Thậm chí các nhà làm phim
            b["at"] = "Thậm chí các nhà làm phim"
        elif b.get("at") == "truyền lại từ đời này sang đời khác":
            # change b11 to các sát thủ trưởng thành sẽ dùng mõm
            b["at"] = "các sát thủ trưởng thành sẽ dùng mõm"

# Scene 03 (12 beats: L24..L35)
# Fix b04, b05, b12
for b in sb["long"]:
    if b.get("scene") == "scene03":
        if b.get("at") == "bộ đôi sát thủ lừng danh mang tên Port và Starboard":
            # b05
            b["at"] = "chỉ riêng lá gan"
        elif b.get("at") == "cú húc lật ngửa con cá mập":
            # b06
            b["at"] = "Thủ phạm chính là bộ đôi"
        elif b.get("at") == "quyền lực sinh sát tối thượng":
            # b12
            b["at"] = "lặn sâu xuống hàng trăm mét"

# Scene 04 (11 beats: L36..L46)
# Fix b01 hold > 15s
for b in sb["long"]:
    if b.get("scene") == "scene04":
        if b.get("at") == "mỗi chi nhánh đều giữ gìn danh dự":
            b["at"] = "tính biệt lập văn hóa"

# Scene 05 (12 beats: L47..L58)
# Fix b02, b10, b11
for b in sb["long"]:
    if b.get("scene") == "scene05":
        if b.get("at") == "sự thấu cảm, lòng vị tha":
            b["at"] = "Khối não nặng tới 5kg"
        elif b.get("at") == "nỗi đau buồn mất mát khôn nguôi":
            b["at"] = "sự thấu cảm"
        elif b.get("at") == "giai đoạn mãn kinh":
            b["at"] = "trải qua giai đoạn mãn kinh"
        elif b.get("at") == "hết khả năng sinh sản ở 40 tuổi":
            b["at"] = "các bà mẹ tiếp tục sống thêm"

# Shorts (12 beats: S01..S12)
# Fix s10
for b in sb["shorts"]:
    if b.get("at") == "vứt bỏ toàn bộ phần xác còn lại":
        b["at"] = "Cuộc phẫu thuật tinh vi"

sb_file.write_text(json.dumps(sb, ensure_ascii=False, indent=2), encoding="utf-8")
print("Updated storyboard.json successfully!")


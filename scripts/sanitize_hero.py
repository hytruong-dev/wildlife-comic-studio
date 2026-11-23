import json
from pathlib import Path

sb_path = Path("projects/tap-36-chim-go-kien/specs/storyboard.json")
sb = json.loads(sb_path.read_text(encoding="utf-8"))

sb["characters"]["HERO"] = "chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba"
sb["characters"]["HERO_S"] = "chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk"

sb_path.write_text(json.dumps(sb, ensure_ascii=False, indent=2), encoding="utf-8")
print("Sanitized HERO in storyboard.json!")


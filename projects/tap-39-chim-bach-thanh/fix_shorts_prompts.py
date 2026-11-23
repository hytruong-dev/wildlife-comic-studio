# -*- coding: utf-8 -*-
import json

path = 'projects/tap-39-chim-bach-thanh/specs/image_prompts.json'
data = json.load(open(path, encoding='utf-8'))

data['S01'] = 'HÌNH S01 (DỌC 9:16, hoạt hình 2D whiteboard comic; chú chim bách thanh xám trắng thanh lịch đeo mặt nạ đen Zorro và mỏ cong sắc sảo; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách vui nhộn đáng yêu). Bố cục: Chú chim bách thanh thám tử đứng trên cành cây với ánh mắt thông minh lém lỉnh, bên cạnh là chiếc cặp tài liệu thám tử màu vàng cam.'
data['S03'] = 'HÌNH S03 (DỌC 9:16, hoạt hình 2D whiteboard comic; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách vui nhộn). Bố cục: Bản vẽ kỹ thuật chiếc mỏ chim uốn cong sắc lẹm hình móc câu bằng thép với hai mấu ngàm cơ học đặc biệt. KHÔNG có chú chim bách thanh đeo mặt nạ Zorro trong cảnh này.'
data['S06'] = 'HÌNH S06 (DỌC 9:16, hoạt hình 2D whiteboard comic; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách vui nhộn). Bố cục: Bức tranh đối lập vui nhộn: Một bên là đôi bàn chân chim sẻ nhỏ xíu mảnh khảnh của chú chim bách thanh đeo mặt nạ Zorro, một bên là bàn chân đại bàng lực lưỡng to gấp mười lần.'

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated S01, S03, S06 successfully!")


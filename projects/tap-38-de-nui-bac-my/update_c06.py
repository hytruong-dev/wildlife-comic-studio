# -*- coding: utf-8 -*-
import json

path = 'projects/tap-38-de-nui-bac-my/specs/extra_prompts.json'
with open(path, encoding='utf-8') as f:
    data = json.load(f)

data['C06'] = "Tạo hình ảnh banner chữ nhật nằm ngang tỉ lệ 21:9 trên nền trắng tinh: thanh tiêu đề hai phần phong cách sổ tay thám hiểm núi cao, bên trái là huy hiệu màu tím có chữ 'TRAO HUY CHƯƠNG', bên phải là khung kim loại viền xanh lá có chữ 'ĐỈNH CAO THỂ THAO MẠO HIỂM', trang trí đỉnh núi tuyết tí hon. Nét vẽ hoạt hình 2D rõ nét, nền trắng tinh hoàn toàn, không watermark."

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated C06 prompt successfully!")


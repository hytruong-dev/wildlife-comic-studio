import json
from pathlib import Path

P = Path("projects/tap-45-vet-kakapo")
ep_data = json.loads((P / "episode.json").read_text(encoding="utf-8"))

# Update display_fix
ep_data["display_fix"]["vài năm một lần"] = "vài năm 1 lần"
ep_data["display_fix"]["năm một"] = "năm 1"
ep_data["display_fix"]["sáu mươi"] = "60"
ep_data["display_fix"]["chín mươi"] = "90"
ep_data["display_fix"]["chân thứ ba"] = "chân thứ 3"
ep_data["display_fix"]["ba đến bốn"] = "3 đến 4"
ep_data["display_fix"]["tám tiếng"] = "8 tiếng"

# Expand Scene 03: Add a part about tuổi thọ 60-90 năm
scenes = ep_data["longform"]["scenes"]
sc3_parts = scenes[2]["parts"]
sc3_parts.append({
    "text": "Bù lại cho cơ chế tự vệ tấu hài đầy rủi ro này, Gã béo vô tri quên cách bay lại sở hữu một chỉ số sinh học đáng kinh ngạc: Tuổi thọ trung bình của Kakapo lên tới sáu mươi đến chín mươi năm! Đây là một trong những loài chim sống thọ nhất trên toàn bộ hành tinh Trái Đất! Các nhà sinh học giải thích rằng do không tốn năng lượng cho việc bay lượn trên trời, nhịp trao đổi chất của gã chậm rãi tựa như một chú rùa cạn, giúp các tế bào cơ thể lão hóa cực kỳ từ tốn!",
    "mood": "tram_bi_an"
})

# Expand Scene 04: Add detail about mỏ quặp như chân thứ 3
sc4_parts = scenes[3]["parts"]
sc4_parts.insert(1, {
    "text": "Đặc biệt hơn nữa, chiếc mỏ quặp màu xám ngà của gã hoạt động chẳng khác nào một chiếc chân thứ ba thần thánh! Khi hai bàn chân bám vào vỏ cây xù xì, gã cắm phập chiếc mỏ cứng vào thân cây như chiếc móc leo núi chuyên nghiệp của vận động viên leo vách đá, đu toàn bộ khối thân bốn cân lên cành cao một cách vô cùng điệu nghệ!",
    "mood": "hao_hung"
})

(P / "episode.json").write_text(json.dumps(ep_data, ensure_ascii=False, indent=1), encoding="utf-8")
print("Updated ep45 episode.json!")


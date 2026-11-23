import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from src.episode.pipeline import finder

P = Path('projects/tap-41-nhen-lan-chuong')
sb = json.load(open(P / 'specs/storyboard.json', encoding='utf-8'))
words = json.load(open(P / 'audio/long_words_fixed.json', encoding='utf-8'))
sw = json.load(open(P / 'audio/shorts_words.json', encoding='utf-8'))

# Tag existing long beats with explicit IDs L01 .. L32
for k, b in enumerate(sb['long']):
    b['id'] = f"L{k+1:02d}"

# Tag existing shorts beats with S01 .. S07
for k, b in enumerate(sb['shorts']):
    b['id'] = f"S{k+1:02d}"

# Define the 25 new long beats to insert
new_long_beats = [
    # scene01
    ("scene01", "Quên đi những tàu ngầm", "L33",
     "Cận cảnh chi tiết bụi rong đuôi chó tĩnh lặng dưới đáy hồ: Những bọt khí nhỏ li ti bám trên kẽ lá xanh biếc; {NO_HERO}; tia sáng mặt trời chiếu rọi từ mặt nước mờ ảo."),
    ("scene01", "Đây là loài nhện duy nhất", "L34",
     "Bản đồ phân bố tiến hóa sinh học: Hàng ngàn chấm đỏ đại diện cho 50.000 loài nhện cạn trên các lục địa; một vệt sáng xanh dương duy nhất lao xuống đáy hồ nước ngọt; {HERO} đứng kiêu hãnh giơ cao kính lặn đồng thau."),
    ("scene01", "Nếu bạn thả một con nhện", "L35",
     "Cận cảnh mặt nước hồ: Một chú nhện nhà rơi xuống nước đang hoảng hốt bơi chới với; phía dưới đáy hồ sâu, {HERO} thong dong bơi lặn quanh những cột rong rêu như một thợ lặn chuyên nghiệp."),
    ("scene01", "Hôm nay, xưởng cơ khí sinh học", "L36",
     "Cận cảnh bàn mổ xẻ thiết kế: {ASSISTANT} cầm kính lúp và bút chì kỹ thuật chỉ vào mô hình chuông lặn tơ nhện vi mô; {HERO} khoanh tay đứng cạnh mỉm cười đầy tự hào."),
    
    # scene02
    ("scene02", "Nhưng Thuyền Trưởng Tàu Ngầm Tơ", "L37",
     "Sơ đồ lực học thủy tĩnh: Mũi tên đỏ chỉ lực đẩy Ác-si-mét hướng lên trời; các mũi tên xanh lục neo đa hướng kéo ghì xuống đáy; {HERO} cầm mỏ lết đồng thau siết chặt các khớp neo."),
    ("scene02", "Điểm kỳ diệu nằm ở chỗ:", "L38",
     "Cận cảnh cấu trúc hiển vi của sợi tơ kỵ nước: Các phân tử protein đan xen khít khao phát sáng màu xanh ngọc bích; giọt nước chạm vào màng tơ bị trượt bắn ra ngoài như trượt trên lá sen; {NO_HERO}."),
    ("scene02", "Nước bên ngoài không thể", "L39",
     "Mặt cắt vi mô thành chuông: Bên ngoài là các phân tử nước màu xanh lam bị chặn đứng hoàn toàn bởi lớp nano kỵ nước; bên trong là các phân tử khí ga màu vàng óng được giữ kín bưng; {HERO} bơi tuần tra bên trong."),
    ("scene02", "Gã dùng đầu húc thử", "L40",
     "Cận cảnh kiểm tra độ bền: {HERO} dùng đầu và hai chân trước húc mạnh vào màng tơ chuông lặn; màng tơ đàn hồi co giãn nhịp nhàng như cao su tổng hợp không hề rách; đồng hồ đo áp lực vọt lên mức an toàn."),

    # scene03
    ("scene03", "Gã chỉ nhô đúng phần chóp bụng", "L41",
     "Góc nhìn cận cảnh mặt thoáng: {HERO} chỉ nhô đúng phần chóp bụng và cặp chân sau lên khỏi mặt hồ, thực hiện một cú giật mình chớp nhoáng tạo ra những vòng sóng tròn lan tỏa; {NO_HERO}."),
    ("scene03", "Đây chính là nguồn gốc", "L42",
     "Từ điển bách khoa cổ điển: Cuốn sách cổ Hy Lạp mở trang ghi chữ Argyroneta phát sáng vàng kim; {HERO} soi mình trước quả cầu bạc bọc quanh bụng như một tấm gương cầu lồi lấp lánh."),
    ("scene03", "Gã lặp lại chuyến xe buýt", "L43",
     "Hành trình xe buýt con thoi: Dãy 5 hình bóng {HERO} liên tiếp bơi lên bơi xuống giữa mặt hồ và đáy bùn; quả chuông tơ từ từ phồng to từ một hạt vừng lên thành một hạt đậu phộng căng tròn tỏa sáng lung linh."),
    ("scene03", "Nhờ động cơ thẩm thấu", "L44",
     "Đồng hồ sinh tồn 24 giờ: Mặt đồng hồ cơ khí bằng đồng hiển thị 24h; bên trong quả chuông lặn, {HERO} ung dung ngủ ngon lành trên võng tơ; các luồng oxy xanh biếc liên tục tự thẩm thấu vào vòm chuông."),
    ("scene03", "Chính vì vậy, Thuyền Trưởng", "L45",
     "Chuyến tuần tra bảo dưỡng: {HERO} đeo túi đồ nghề sửa chữa, ngoi lên mặt nước quặp một bọt khí mới toanh mang xuống nạp vào đỉnh chuông lặn; đồng hồ áp suất kim chỉ lại về vạch xanh an toàn."),

    # scene04
    ("scene04", "nơi các nàng nhện cái", "L46",
     "Tương phản sinh học: BÊN TRÁI trên cạn, một nàng nhện cái khổng lồ đang hung dữ cầm nĩa; BÊN PHẢI dưới nước, {HERO} vạm vỡ cơ bắp đang mỉm cười nháy mắt chào đón bạn gái; {NO_HERO}."),
    ("scene04", "Nhện đực to hơn nhện cái", "L47",
     "Bàn cân so sánh kích thước: BÊN TRÁI {HERO} (nhện đực) dài 15mm sải chân vạm vỡ; BÊN PHẢI nàng nhện cái nhỏ nhắn 12mm e ấp; chiếc thước kẹp cơ khí đo tỷ lệ chênh lệch 30% rõ nét."),
    ("scene04", "Thân hình to lớn và đôi chân", "L48",
     "Cảnh bơi lội vượt dòng xiết: {HERO} sải 8 chiếc chân dài cơ bắp quặp quả bọt khí khổng lồ rẽ nước bơi băng băng qua dòng chảy xiết; {MINNOW} bơi bên cạnh nhìn theo trầm trồ thán phục."),
    ("scene04", "Một căn biệt thự thông tầng", "L49",
     "Bản vẽ phối cảnh kiến trúc: Hai quả chuông lặn nối liền nhau bằng đường hầm tơ trong suốt; {HERO} và nàng nhện cái ngồi hai bên đường hầm cụng ly nước ngọt lãng mạn dưới ánh đèn lân tinh."),
    ("scene04", "Nơi đây chứa lượng oxy", "L50",
     "Phòng trẻ sơ sinh dưới nước: Bên trong vòm chuông trên cao, chiếc kén tơ tròn xoe chứa hàng chục nhện con tí hon đang chui ra; các bé nhện con đeo kính bơi tí hon tập quặp những bọt khí nhỏ li ti."),

    # scene05
    ("scene05", "Từ quả chuông lặn trung tâm,", "L51",
     "Mạng lưới radar dây tơ: Từ quả chuông lặn của {HERO}, hàng chục sợi tơ mảnh phát sáng chạy dài đến các bụi cây thủy sinh như mạng dây điện thoại cảnh báo; {HERO} đặt chân lên nút cảm biến trung tâm."),
    ("scene05", "Sau đó, gã kéo chiến lợi phẩm", "L52",
     "Phòng tiệc bên trong chuông lặn: {HERO} ngồi thảnh thơi trên chiếc ghế bành bằng tơ, dùng dao nĩa tí hon thưởng thức món ấu trùng bọ gậy khô ráo; ngoài thành chuông, một chú cá săn mồi bơi qua nhìn thèm thuồng."),
    ("scene05", "Với tốc độ cơ động cực nhanh,", "L53",
     "Kế hoạch thoát hiểm khẩn cấp: Vòm tơ bị cá chép cắn rách, {HERO} phóng vọt qua cửa đáy thoát hiểm núp vào khe đá; sau khi cá bỏ đi, {HERO} thoăn thoắt phun tơ vá lành lỗ rách trong tích tắc."),
    ("scene05", "Nhện lặn chuông bò xuống lớp bùn", "L54",
     "Giấc ngủ đông dưới đáy băng: Mặt hồ phủ lớp băng dày tuyết trắng; sâu dưới lớp bùn ấm áp, {HERO} cuộn tròn ngủ say trong kén tơ siêu dày ôm một túi khí nhỏ; chiếc nhiệt kế cắm cạnh chỉ 0°C."),

    # scene06
    ("scene06", "Khi môi trường sống cạn kiệt", "L55",
     "Biểu tượng triết lý tiến hóa: Hình vẽ cây tiến hóa với các nhánh cạn kiệt cơ hội; {HERO} đứng trên đỉnh một mỏm đá ngầm, tay cầm cờ hải quân tung bay, mở ra một chân trời mới dưới đáy hồ sâu."),
    ("scene06", "Đôi khi, chỉ cần một quả chuông", "L56",
     "Hình ảnh truyền cảm hứng: {HERO} tươi cười rạng rỡ bên trong quả chuông lặn tỏa sáng lung linh giữa đáy hồ tối; xung quanh là dòng nước lạnh giá nhưng bên trong ấm áp tràn đầy dưỡng khí hy vọng."),
    ("scene06", "nếu ngâm nước quá lâu thì lại", "L57",
     "Cận cảnh hình bóng teaser tập 42 (TASTE-68): Bóng đen một con cá kỳ dị hai mắt lồi to tướng ngồi trên cành cây đước bãi lầy, một tay bịt mũi ôm cổ ho sặc sụa dưới nước với dấu hỏi '?' lớn màu vàng.")
]

# Insert each long beat into sb['long'] at the correct position
for sid, at_phrase, img_id, layout in new_long_beats:
    T = finder(words[sid])
    target_t = T(at_phrase)
    inserted = False
    for i, b in enumerate(sb['long']):
        if b['scene'] == sid:
            b_t = 0.0 if b['at'] in (0, '0', '') else T(b['at'])
            if b_t > target_t:
                sb['long'].insert(i, {
                    "scene": sid,
                    "at": at_phrase,
                    "id": img_id,
                    "layout": layout,
                    "stickers": [],
                    "impacts": []
                })
                inserted = True
                break
    if not inserted:
        # append at end of this scene
        last_idx = max(i for i, b in enumerate(sb['long']) if b['scene'] == sid)
        sb['long'].insert(last_idx + 1, {
            "scene": sid,
            "at": at_phrase,
            "id": img_id,
            "layout": layout,
            "stickers": [],
            "impacts": []
        })

# Insert new shorts beat S08
new_short_beat = {
    "at": "tự hút oxy hòa tan",
    "id": "S08",
    "layout": "Cận cảnh thành quả chuông: Các phân tử oxy xanh dương thẩm thấu vào trong chuông, giúp {HERO_S} thở suốt 24 giờ mà không cần ngoi lên mặt hồ; đồng hồ cơ khí quay tròn 24h.",
    "stickers": []
}

for i, b in enumerate(sb['shorts']):
    if b.get('id') == 'S05':
        sb['shorts'].insert(i + 1, new_short_beat)
        break

with open(P / 'specs/storyboard.json', 'w', encoding='utf-8') as f:
    json.dump(sb, f, ensure_ascii=False, indent=1)

print(f"Updated storyboard.json: {len(sb['long'])} long beats, {len(sb['shorts'])} shorts beats.")

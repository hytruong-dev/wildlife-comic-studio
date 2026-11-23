"""
V3 Narration — kịch bản lời bình đã tối ưu giữ chân (retention) cho Tập 1: Lửng Mật
- Cold-open hook trong 3 giây đầu (câu hỏi + con số gây sốc)
- Câu ngắn, dứt khoát, nhiều câu hỏi tu từ / dấu "..." để tạo nhấn nhá
- Mid-dip cliffhanger ở phần 4 (điểm chèn Mid-roll)
- Shorts có vòng lặp (câu cuối nối về câu đầu)

Chạy: python projects/tap-01-lung-mat/scripts/v3_narration.py [scene01 scene02 ... shorts]
"""

import sys
from pathlib import Path

PROJ = Path(__file__).resolve().parent.parent
ROOT = PROJ.parent.parent
sys.path.insert(0, str(ROOT / "src" / "audio"))

NARRATION = {
    "scene01": """Một con vật chỉ nặng mười hai ký... nhưng cả bầy sư tử nhìn thấy nó cũng phải tránh đường. Nó là ai?
Bạn nghĩ ai mới thực sự là bá chủ của thảo nguyên châu Phi? Là sư tử với tiếng gầm rung chuyển núi rừng? Là bầy linh cẩu tham lam? Hay những gã khổng lồ như voi và tê giác?
Quên tất cả những điều đó đi!
Có một sinh vật cao chưa đầy ba mươi centimet, nặng vỏn vẹn mười hai kilôgam, nhưng lại khiến chúa sơn lâm toát mồ hôi hột, tự động né sang một bên đường.
Giới khoa học gọi nó là Mellivora capensis. Còn giang hồ muôn loài gọi nó bằng một cái tên khác: Lửng Mật!
Sách Kỷ lục Guinness từng gọi nó là sinh vật không biết sợ nhất hành tinh. Một gã lùn tịt, lông hai màu đen trắng, dáng đi khệnh khạng đầy vẻ bất cần đời.
Sư tử nặng gấp mười lăm lần, nhưng vẫn không muốn dây vào. Vì sao ư? Đánh nhau với Lửng Mật là mất cả tiếng đồng hồ, rách môi, mẻ vuốt... chỉ để đổi lấy một miếng thịt dai nhách!
Và nếu bạn lỡ động vào nó, nó sẽ đuổi theo bạn tới cùng.""",

    "scene02": """Nếu đưa Lửng Mật vào một tựa game nhập vai, người chơi chắc chắn sẽ khiếu nại vì nhân vật này quá mất cân bằng! Hãy cùng mở bảng chỉ số của gã chiến binh này.
Chỉ số đầu tiên, Sức Mạnh: tám mươi lăm điểm! Dưới lớp lông dày là những bó cơ nén chặt, đủ sức kéo lê con mồi nặng gấp ba lần cơ thể nó.
Chỉ số thứ hai, Phòng Thủ: chín mươi chín điểm! Nó khoác trên mình bộ giáp cao su dày sáu milimét. Răng nanh sư tử, nọc bọ cạp, gai nhím... tất cả đều bị trượt!
Chỉ số thứ ba, Trí Thông Minh: chín mươi điểm. Đây không phải kẻ hữu dũng vô mưu, mà là một thiên tài bẻ khóa và chế tạo công cụ.
Tiếp theo là độ Lì Đòn... và nó phá vỡ luôn thang đo: chín trăm chín mươi chín điểm! Trong từ điển của Lửng Mật, không có nút đầu hàng.
Và chỉ số cuối cùng, chấn động nhất: Sợ Hãi. Không điểm tròn trĩnh! Vùng não xử lý nỗi sợ của nó gần như không phản ứng với nguy hiểm.""",

    "scene03": """Vậy điều gì giúp một sinh vật nhỏ bé như vậy ngạo nghễ bước đi giữa thảo nguyên? Bí mật nằm ở ba vũ khí mà tự nhiên ban tặng!
Vũ khí thứ nhất: lớp da cao su lỏng lẻo. Da nó dày hơn cả da trâu, nhưng lại rộng thùng thình như một chiếc áo khoác.
Hãy tưởng tượng: một con báo hoa mai ngoạm chặt gáy Lửng Mật, tưởng rằng con mồi đã nằm gọn trong miệng. Nhưng không! Lửng Mật xoay người một trăm tám mươi độ ngay bên trong lớp da của chính mình... rồi cắn thẳng vào mũi kẻ săn mồi!
Con báo đau điếng, chỉ còn cách nhả ra ngay lập tức.
Vũ khí thứ hai: bộ móng vuốt dài hơn năm centimet, cong vút và cứng như mũi khoan thép. Tổ mối cứng như bê tông? Vài phút là xới tung!
Còn bộ hàm của nó đủ khỏe để cắn vỡ cả mai rùa, nhai luôn cả xương.
Và vũ khí thứ ba nằm ở phía sau đuôi: một túi xạ phun ra luồng khí thối nồng nặc, khiến cả bầy thú săn mồi cay mắt, buồn nôn và phải tháo chạy!""",

    "scene04": """Nhưng tất cả những vũ khí đó... vẫn chưa là gì so với thực đơn điên rồ của gã giang hồ này!
Món khoái khẩu của Lửng Mật là rắn độc. Rắn hổ mang, rắn lục phì, thậm chí cả mamba đen! Rắn chiếm tới một phần tư khẩu phần ăn của nó.
Chỉ một giọt nọc rắn lục phì đủ để hạ gục một sinh vật to gấp mười lần nó.
Vậy chuyện gì xảy ra khi một con hổ mang cắn ngập răng nanh vào mặt Lửng Mật? Liệu kẻ liều lĩnh này có phải trả giá bằng cả mạng sống?
Câu trả lời là một cú bẻ lái kinh điển của tiến hóa!
Các nhà khoa học phát hiện ra rằng, thụ thể thần kinh của Lửng Mật đã bị đột biến. Đột biến này hoạt động như một lớp áo giáp phân tử, khiến nọc độc thần kinh của rắn không thể bám vào.
Khi bị cắn trúng, Lửng Mật sẽ lảo đảo... rồi lăn đùng ra đất, ngủ mê man như một gã say rượu. Suốt hai tiếng đồng hồ, kẻ thù tưởng nó đã chết.
Thế rồi, nó mở mắt, lắc đầu, đứng dậy tỉnh queo... và thản nhiên ăn nốt nửa con rắn còn lại!""",

    "scene05": """Nhưng thứ khiến các nhà khoa học phải ngả mũ thật sự... là bộ não của nó. Và minh chứng rõ nhất là một chú lửng mật tên Stoffel ở Nam Phi.
Stoffel nổi tiếng đến mức đài BBC làm riêng cả một bộ phim về những phi vụ vượt ngục của nó!
Người ta nhốt Stoffel trong chuồng có tường bê tông cao lút đầu người. Bạn nghĩ bức tường đó giữ được nó?
Stoffel cào đất bùn, nặn thành từng viên to tướng, xếp chồng lên nhau... rồi trèo qua tường!
Dọn sạch bùn, nó gom cành cây làm thang. Dọn sạch cành cây, nó lăn đá tới.
Và khi chuồng sạch bóng không còn một viên sỏi, Stoffel dụ con lửng cái đứng sát góc tường... rồi trèo lên lưng bạn gái để vượt ngục!
Điều hài hước nhất? Nó trốn ra không phải để về rừng, mà để chạy sang chuồng sư tử bên cạnh... gây sự!
Ngay cả khi bị ba con sư tử đực bao vây, Lửng Mật cũng không lùi bước. Nó xù lông, gầm gừ, phun túi xạ... và lao thẳng vào chúng. Cuối cùng, chính bầy sư tử phải rút lui!""",

    "scene06": """Lửng Mật là minh chứng sống cho một điều: kích thước không quyết định vị thế của bạn. Chỉ cần đủ bản lĩnh, bạn có thể khiến cả thế giới phải nể.
Nhưng gã Chí Phèo châu Phi này mới chỉ là sự khởi đầu. Nếu bạn nghĩ sự tàn bạo chỉ tồn tại trên cạn... thì bạn đã nhầm to!
Dưới đại dương, có một sinh vật nổi tiếng với vẻ ngoài siêu đáng yêu, hay nằm ngửa nắm tay nhau ngủ trên mặt nước... nhưng đằng sau đó là những bí mật đen tối bậc nhất thế giới động vật.
Đó chính là Rái Cá Biển!
Bấm ngay vào video trên màn hình để xem bộ mặt thật của nó. Và đừng quên đăng ký kênh Vẽ Chuyện Muông Thú nhé!""",

    "shorts": """Con vật này chỉ nặng mười hai ký... nhưng sư tử thấy nó cũng phải tránh đường!
Sự thật thứ nhất: da nó dày sáu milimét, và lỏng như một chiếc áo khoác. Báo hoa mai cắn vào gáy? Nó xoay một trăm tám mươi độ ngay trong lớp da, rồi cắn ngược vào mũi kẻ thù!
Sự thật thứ hai: rắn hổ mang cắn thẳng vào mặt nó. Nó lăn ra ngủ hai tiếng... rồi tỉnh dậy, ăn nốt con rắn!
Sự thật thứ ba: chú lửng Stoffel vượt ngục hàng chục lần. Bằng bùn, bằng cành cây, bằng đá... và bằng cả lưng của bạn gái nó!
Bị ba con sư tử bao vây? Nó vẫn lao vào đánh.
Đây là Lửng Mật, kẻ Chí Phèo số một hành tinh. Và đó là lý do vì sao con vật chỉ nặng mười hai ký này...""",
}

if __name__ == "__main__":
    from expressive_tts import build_narration
    sys.stdout.reconfigure(encoding="utf-8")
    ids = sys.argv[1:] or list(NARRATION)
    out = PROJ / "audio_v3"
    for sid in ids:
        build_narration(NARRATION[sid], out, sid)

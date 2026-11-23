"""
Sentence-Level Visual Prompt Architect (`src/compiler/sentence_prompt_architect.py`)
Upgrades the AI Video Production Pipeline so that every narration paragraph/sentence is decomposed into
ultra-detailed, literal, zero-imagination-gap 2D Comic Whiteboard Prompts for Google Gemini.

CORE RULES (Zero-Imagination-Gap Protocol):
1. 1-to-1 Paragraph/Sentence Visual Mapping: Never merge two distinct narrative paragraphs into one generic picture.
2. Literal Action & Anatomy Decomposition: Extract every concrete noun, measurement, comparative metaphor, and action verb from the spoken Vietnamese narration and translate them into explicit visual elements in the prompt.
3. Strict Zero-In-Image-Text Enforcement: Always enforce "KHÔNG CÓ CHỮ (NO TEXT, NO WORDS, NO LABELS, NO NUMBERS, NO SPEECH BUBBLES)" so the artwork remains 100% pure visual storytelling, while titles/captions are handwritten externally on the whiteboard.
4. Pure Whiteboard Integration: Always specify "2D minh họa truyện tranh (comic book illustration style) trên nền trắng tinh khiết (#FFFFFF), nét mực đen sắc nét, màu sắc sống động, không đóng khung viền".
"""

import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Dict, Any


@dataclass
class SentenceVisualBeatPrompt:
    scene_id: str
    beat_id: str
    start_ms: int
    end_ms: int
    narration_vi: str
    extracted_visual_details: List[str]
    gemini_prompt_vi: str
    asset_filename: str
    badge_text: str
    caption_text: str


EPISODE_01_LITERAL_PROMPT_CATALOG: List[SentenceVisualBeatPrompt] = [
    # ──────────────────────── SCENE 01 (4 Beats) ────────────────────────
    SentenceVisualBeatPrompt(
        scene_id="scene01",
        beat_id="beat_01",
        start_ms=0,
        end_ms=15200,
        narration_vi="Bạn nghĩ ai mới thực sự là bá chủ tối cao của thảo nguyên hoang dã châu Phi? Là chúa sơn lâm sư tử với tiếng gầm rung chuyển cả đại ngàn? Là đàn linh cẩu tàn nhẫn với số lượng áp đảo? Hay những gã khổng lồ như voi rừng và tê giác hai sừng?",
        extracted_visual_details=[
            "Chúa sơn lâm sư tử đực bờm dày gầm vang",
            "Đàn linh cẩu đốm nhe răng áp đảo số lượng",
            "Voi rừng châu Phi khổng lồ giơ cao vòi và cặp ngà",
            "Tê giác hai sừng cơ bắp sừng sững",
        ],
        gemini_prompt_vi=(
            "Tạo hình ảnh 2D minh họa truyện tranh (comic book illustration style) trên nền trắng tinh khiết (#FFFFFF), "
            "nét mực đen sắc nét, màu sắc sống động, KHÔNG CÓ CHỮ (NO TEXT, NO WORDS, NO LABELS): "
            "Tập hợp 4 bá chủ thảo nguyên châu Phi gồm: Sư tử đực bờm dày đang há miệng gầm vang ở tiền cảnh bên trái, "
            "đàn linh cẩu đốm đông đúc nhe răng hung tợn bên phải, phía sau là voi rừng châu Phi khổng lồ giơ cao vòi "
            "và tê giác hai sừng sừng sững. Nền trắng hoàn toàn, không đóng khung viền."
        ),
        asset_filename="c1_savanna_apex_predators_giants.png",
        badge_text="01. TỨ ĐẠI BÁ CHỦ",
        caption_text="Bá chủ thảo nguyên: Sư tử gầm, đàn linh cẩu, voi rừng & tê giác",
    ),
    SentenceVisualBeatPrompt(
        scene_id="scene01",
        beat_id="beat_02",
        start_ms=15200,
        end_ms=29700,
        narration_vi="Quên tất cả những điều đó đi! Trong từ điển sinh tồn hoang dã, có một sinh vật kỳ dị chỉ cao chưa đầy ba mươi centimet, nặng vỏn vẹn mười hai kilôgam, nhưng lại khiến cả một bầy sư tử nhìn thấy từ đằng xa cũng phải toát mồ hôi hột, tự động né sang một bên đường!",
        extracted_visual_details=[
            "Sinh vật nhỏ bé cao 30cm nặng 12kg đi hiên ngang ở giữa đường",
            "Cả bầy sư tử to lớn nhìn thấy từ xa phải toát mồ hôi hột",
            "Bầy sư tử tự động lùi lại né sang hai bên đường nhường lối",
        ],
        gemini_prompt_vi=(
            "Tạo hình ảnh 2D minh họa truyện tranh (comic book illustration style) trên nền trắng tinh khiết (#FFFFFF), "
            "nét mực đen sắc nét, màu sắc sống động, KHÔNG CÓ CHỮ (NO TEXT, NO WORDS, NO LABELS): "
            "Một con Lửng Mật nhỏ bé chỉ cao 30cm đang bước đi nghênh ngang ở chính giữa, trong khi cả một bầy sư tử "
            "to lớn đứng hai bên phải toát mồ hôi hột, mặt hoảng hốt tự động lùi bước né sang một bên nhường đường. "
            "Nền trắng hoàn toàn, không đóng khung viền."
        ),
        asset_filename="c1_lions_sweating_scared.png",
        badge_text="02. SƯ TỬ NÉ ĐƯỜNG",
        caption_text="Nghịch lý: Bầy sư tử toát mồ hôi tự động né sang một bên đường",
    ),
    SentenceVisualBeatPrompt(
        scene_id="scene01",
        beat_id="beat_03",
        start_ms=29700,
        end_ms=47500,
        narration_vi="Giới khoa học đặt tên cho nó là Mellivora capensis. Còn trên giang hồ của muôn loài hoang dã, nó được phong tặng danh hiệu kẻ Chí Phèo số một hành tinh: Lửng Mật! Sách Kỷ lục Guinness thế giới từng vinh danh nó là sinh vật không biết sợ nhất hành tinh. Một gã lùn tịt với bộ lông hai màu đen trắng tương phản, dáng đi lững thững khệnh khạng đầy vẻ bất cần đời. Sư tử nặng gấp mười lăm lần nhưng không bao giờ muốn dây vào.",
        extracted_visual_details=[
            "Lửng Mật lùn tịt lông hai màu đen trắng tương phản rõ rệt",
            "Huy chương vàng ngôi sao & sách Kỷ lục Guinness vinh danh",
            "Cái bóng đen khổng lồ của sư tử nặng gấp 15 lần phía sau phải e dè lùi bước",
        ],
        gemini_prompt_vi=(
            "Tạo hình ảnh 2D minh họa truyện tranh (comic book illustration style) trên nền trắng tinh khiết (#FFFFFF), "
            "nét mực đen sắc nét, màu sắc sống động, KHÔNG CÓ CHỮ (NO TEXT, NO WORDS, NO LABELS, NO NUMBERS): "
            "Một con Lửng Mật (Honey Badger) nhỏ bé cao 30cm với bộ lông đen trắng tương phản và dáng đi khệnh khạng "
            "bất cần đời đang đeo một tấm huy chương vàng hình ngôi sao lớn lấp lánh trước ngực và đứng trên cuốn sách "
            "kỷ lục vàng mở rộng. Phía sau lưng nó là cái bóng đen khổng lồ cao lớn gấp 15 lần của một con sư tử đực "
            "bờm xù đang phải lùi bước e dè trước khí phách của chú lửng mật nhỏ bé! Nền trắng hoàn toàn."
        ),
        asset_filename="c1_badger_guinness_fearless.png",
        badge_text="03. KỶ LỤC GUINNESS",
        caption_text="Kỷ lục Guinness: Kẻ Chí Phèo 12kg khiến sư tử nặng gấp 15 lần e dè",
    ),
    SentenceVisualBeatPrompt(
        scene_id="scene01",
        beat_id="beat_04",
        start_ms=47500,
        end_ms=68160,
        narration_vi="Vì sao ư? Đánh nhau với Lửng Mật là mất cả tiếng đồng hồ vật lộn, rách môi, mẻ vuốt, chỉ để đổi lấy một miếng thịt dai nhách đầy mùi hôi hám! Và nếu bạn lỡ đụng vào nó, nó sẽ đuổi theo bạn tới cùng trời cuối đất để trả thù!",
        extracted_visual_details=[
            "Hai con sư tử đực tả tơi sau cả tiếng đồng hồ vật lộn",
            "Môi sư tử bị rách chảy máu, móng vuốt bị mẻ gãy",
            "Trước mặt là miếng thịt dai nhách bốc mùi hôi và ruồi nhặng",
            "Phía sau là Lửng Mật nhe răng cười khẩy sẵn sàng truy đuổi trả thù",
        ],
        gemini_prompt_vi=(
            "Tạo hình ảnh 2D minh họa truyện tranh (comic book illustration style) trên nền trắng tinh khiết (#FFFFFF), "
            "nét mực đen sắc nét, màu sắc sống động, KHÔNG CÓ CHỮ (NO TEXT, NO WORDS, NO LABELS): "
            "Hai con sư tử đực tả tơi kiệt sức sau trận vật lộn: môi bị rách, mặt đầy vết cào, móng vuốt bị mẻ gãy, "
            "ngồi nhìn một miếng thịt xám ngoét dai nhách bốc mùi hôi thối có ruồi bay quanh, trong khi Lửng Mật đứng "
            "phía sau cười khẩy thách thức. Nền trắng hoàn toàn, không đóng khung viền."
        ),
        asset_filename="c1_lions_battered_torn_meat.png",
        badge_text="04. LỖ VỐN NẶNG",
        caption_text="Cái giá quá đắt: Rách môi mẻ vuốt đổi lấy miếng thịt dai nhách",
    ),

    # ──────────────────────── SCENE 02 (4 Beats) ────────────────────────
    SentenceVisualBeatPrompt(
        scene_id="scene02",
        beat_id="beat_01",
        start_ms=0,
        end_ms=34360,
        narration_vi="Đầu tiên là chỉ số Sức Mạnh Thể Chất STR: Đạt tám mươi lăm trên một trăm điểm! Dưới lớp lông dày cộp như thảm gai là hệ thống bó cơ nén đặc với mật độ khủng khiếp, giúp Lửng Mật có thể kéo lê một xác linh dương nặng gấp ba lần trọng lượng cơ thể đi qua hàng cây số thảo nguyên gập ghềnh.",
        extracted_visual_details=[
            "Bó cơ vai và chân của Lửng Mật nén đặc cuồn cuộn dưới lớp lông đen trắng",
            "Hàm răng ngoạm chặt cổ kéo lê xác con linh dương sừng xoắn to gấp 3 lần cơ thể",
            "Địa hình đá sỏi thảo nguyên gập ghềnh có vệt kéo lê dài",
        ],
        gemini_prompt_vi=(
            "Tạo hình ảnh 2D minh họa truyện tranh (comic book illustration style) trên nền trắng tinh khiết (#FFFFFF), "
            "nét mực đen sắc nét, màu sắc sống động, KHÔNG CÓ CHỮ (NO TEXT, NO WORDS, NO LABELS): "
            "Một con Lửng Mật (Honey Badger) cơ bắp cuồn cuộn gân guốc dưới lớp lông đen trắng dày như thảm gai, "
            "đang dùng hàm răng khỏe khoắn ngoạm chặt cổ và kéo lê một xác con linh dương sừng xoắn to lớn (nặng gấp "
            "3 lần cơ thể nó) băng qua những tảng đá gập ghềnh trên thảo nguyên. Nền trắng hoàn toàn."
        ),
        asset_filename="c2_badger_muscles_strength.png",
        badge_text="STR 85 / 100",
        caption_text="Sức mạnh STR 85: Cơ nén đặc kéo xác linh dương nặng gấp 3 lần",
    ),
    SentenceVisualBeatPrompt(
        scene_id="scene02",
        beat_id="beat_02",
        start_ms=34360,
        end_ms=54600,
        narration_vi="Thứ hai là chỉ số Phòng Thủ DEF: Chạm mốc tuyệt đối chín mươi chín điểm! Nó khoác lên mình một lớp giáp cao su di động dày tới sáu milimét, kháng cự hoàn toàn từ răng nanh của sư tử, nọc độc bọ cạp đến cả những mũi giáo sắc nhọn bằng kim loại của thổ dân châu Phi. Mọi đòn tấn công khi chém vào lưng nó đều bị trượt đi như chém vào lốp xe tải!",
        extracted_visual_details=[
            "Lớp da lưng cao su dày 6mm đàn hồi như lốp xe tải",
            "Răng nanh sư tử cắn xuống bị trượt lệch",
            "Kim nọc độc của bọ cạp đen đâm vào bị cong gập",
            "Mũi giáo kim loại sắc nhọn của thổ dân đâm vào bị nảy văng tia lửa",
        ],
        gemini_prompt_vi=(
            "Tạo hình ảnh 2D minh họa truyện tranh (comic book illustration style) trên nền trắng tinh khiết (#FFFFFF), "
            "nét mực đen sắc nét, màu sắc sống động, KHÔNG CÓ CHỮ (NO TEXT, NO WORDS, NO LABELS): "
            "Cận cảnh lớp da lưng cao su dày 6mm cực kỳ đàn hồi của Lửng Mật đang đồng thời đánh bật cả 3 đòn tấn công: "
            "(1) Răng nanh sư tử khổng lồ cắn xuống bị trượt lệch, (2) Đuôi kim tiêm nọc độc của bọ cạp đen đâm vào bị "
            "cong gập lại, và (3) Mũi giáo kim loại sắc nhọn của thổ dân đâm vào lưng bị trượt văng đi kèm tia lửa như "
            "chém vào lốp xe tải! Nền trắng hoàn toàn."
        ),
        asset_filename="c2_badger_rubber_armor.png",
        badge_text="DEF 99 / 100",
        caption_text="Phòng thủ DEF 99: Da cao su 6mm bật răng sư tử, bọ cạp & mũi giáo",
    ),
    SentenceVisualBeatPrompt(
        scene_id="scene02",
        beat_id="beat_03",
        start_ms=54600,
        end_ms=77960,
        narration_vi="Thứ ba là chỉ số Trí Thông Minh IQ: Đạt chín mươi điểm. Đây hoàn toàn không phải một kẻ hữu dũng vô mưu, mà là một thiên tài bẻ khóa, chế tạo công cụ và tư duy chiến thuật sinh tồn đỉnh cao! Tiếp theo là Độ Bền Bỉ và Lì Đòn TENACITY: Phá vỡ luôn mọi thang đo với chín trăm chín mươi chín điểm! Trong từ điển của Lửng Mật, không có nút đầu hàng và càng không có khái niệm quay đầu bỏ chạy!",
        extracted_visual_details=[
            "Bên trái: Lửng Mật đeo kính thông thái dùng móng vuốt bẻ khóa chốt sắt cửa chuồng & xếp đá làm thang, bóng đèn sáng trên đầu",
            "Bên phải: Lửng Mật chiến binh rực lửa lao về phía trước, chân đạp vỡ nát biển báo cờ trắng đầu hàng",
        ],
        gemini_prompt_vi=(
            "Tạo hình ảnh 2D minh họa truyện tranh (comic book illustration style) trên nền trắng tinh khiết (#FFFFFF), "
            "nét mực đen sắc nét, màu sắc sống động, KHÔNG CÓ CHỮ (NO TEXT, NO WORDS, NO LABELS): "
            "Bên trái là Lửng Mật thông thái đeo kính tròn dùng móng vuốt khéo léo bẩy mở chốt khóa sắt của cửa chuồng "
            "và xếp đá làm bậc thang, trên đầu có bóng đèn sáng rực rỡ. Bên phải là Lửng Mật chiến binh đang tiến thẳng "
            "về phía trước với hào quang lửa rực cháy, một chân đạp vỡ nát chiếc biển báo cờ trắng (không bao giờ đầu hàng). "
            "Nền trắng hoàn toàn."
        ),
        asset_filename="c2_badger_iq_genius.png",
        badge_text="IQ 90 & LÌ ĐÒN 999",
        caption_text="IQ 90 & Lì đòn 999: Thiên tài bẻ khóa, đạp nát cờ trắng đầu hàng",
    ),
    SentenceVisualBeatPrompt(
        scene_id="scene02",
        beat_id="beat_04",
        start_ms=77960,
        end_ms=95760,
        narration_vi="Và chỉ số cuối cùng chấn động nhất: Cảm Giác Sợ Hãi FEAR: Không điểm tròn trĩnh! Các nhà sinh vật học hàng đầu đã chứng minh rằng hạch hạnh nhân trong não bộ của Lửng Mật dường như đã bị tạo hóa tháo dỡ hoàn toàn khỏi cơ thể, khiến nó không hề có phản xạ sợ hãi trước bất kỳ hiểm nguy nào trên trần đời!",
        extracted_visual_details=[
            "Lửng Mật khoanh tay đứng cười ngạo nghễ thách thức",
            "Sơ đồ bộ não trong suốt phía trên với cục Hạch Hạnh Nhân (Amygdala) màu xanh đang được cờ-lê và tua-vít tháo ốc nhấc hẳn ra ngoài",
            "Chiếc đồng hồ đo nỗi sợ bên cạnh có kim gãy đôi ở vạch thấp nhất",
        ],
        gemini_prompt_vi=(
            "Tạo hình ảnh 2D minh họa truyện tranh (comic book illustration style) trên nền trắng tinh khiết (#FFFFFF), "
            "nét mực đen sắc nét, màu sắc sống động, KHÔNG CÓ CHỮ (NO TEXT, NO WORDS, NO LABELS, NO NUMBERS): "
            "Một con Lửng Mật ngạo nghễ khoanh tay đứng mỉm cười thách thức. Bên trên đầu nó là hình vẽ giải phẫu bộ não "
            "trong suốt, trong đó cục Hạch Hạnh Nhân (Amygdala) màu xanh lá đang được một chiếc cờ-lê và tua-vít cơ khí "
            "tháo ốc nhấc hẳn ra ngoài bộ não! Bên cạnh là chiếc đồng hồ đo có kim bị gãy đôi ở vạch thấp nhất. Nền trắng hoàn toàn."
        ),
        asset_filename="c2_badger_fear_zero.png",
        badge_text="FEAR 0 / 100",
        caption_text="Nỗi sợ FEAR 0: Tạo hóa dùng cờ-lê tháo dỡ hạch hạnh nhân khỏi não",
    ),

    # ──────────────────────── SCENE 03 (4 Beats) ────────────────────────
    SentenceVisualBeatPrompt(
        scene_id="scene03",
        beat_id="beat_01",
        start_ms=0,
        end_ms=26280,
        narration_vi="Điều gì đã giúp một sinh vật nhỏ bé sống sót và ngạo nghễ bước đi giữa chốn thảo nguyên đầy rẫy thú dữ ăn thịt? Bí mật nằm ở ba cơ chế giải phẫu kỳ dị bậc nhất mà mẹ thiên nhiên ưu ái ban tặng cho nó. Cơ chế thứ nhất chính là lớp da cao su đàn hồi cực kỳ lỏng lẻo. Lớp da của Lửng Mật dày hơn cả da trâu mộng trưởng thành, nhưng điều kỳ lạ là nó không hề dính chặt vào các mô cơ bắp bên dưới mà lỏng lẻo như một chiếc áo khoác da quá khổ.",
        extracted_visual_details=[
            "Bên trái: Mặt cắt da trâu mộng trưởng thành dày nhưng dính chặt vào thớ cơ bên dưới",
            "Bên phải: Lửng Mật khoác lớp da đen trắng rộng thùng thình như chiếc áo khoác da quá khổ tách rời hẳn khỏi khối cơ bắp bên trong",
        ],
        gemini_prompt_vi=(
            "Tạo hình ảnh 2D minh họa truyện tranh giải phẫu sinh học trên nền trắng tinh khiết (#FFFFFF), "
            "nét mực đen sắc nét, màu sắc sống động, KHÔNG CÓ CHỮ (NO TEXT, NO WORDS, NO LABELS): "
            "So sánh trực quan cơ chế da lỏng lẻo của Lửng Mật: Bên trái là mặt cắt lớp da của một con trâu mộng bình thường "
            "dính chặt vào bắp thịt bên dưới. Bên phải là một con Lửng Mật đang mặc chính lớp da đen trắng dày hơn cả da trâu "
            "nhưng rộng thùng thình và lỏng lẻo như một chiếc áo khoác da quá khổ tách rời hẳn khỏi lớp cơ bắp bên trong. Nền trắng hoàn toàn."
        ),
        asset_filename="c3_badger_loose_skin_jacket.png",
        badge_text="01. ÁO KHOÁC DA RỘNG",
        caption_text="Cơ chế 1: Lớp da dày hơn da trâu nhưng lỏng lẻo như áo khoác rộng",
    ),
    SentenceVisualBeatPrompt(
        scene_id="scene03",
        beat_id="beat_02",
        start_ms=26280,
        end_ms=51320,
        narration_vi="Hãy hình dung tình huống sinh tử này: Khi một con báo hoa mai hay linh cẩu châu Phi ngoạm chặt hàm răng vào gáy Lửng Mật và ngỡ rằng con mồi đã nằm gọn trong tay, điều ma quỷ xảy ra: Lửng Mật có thể tự do xoay người một trăm tám mươi độ ngay bên trong chính lớp da của mình, rồi quay ngoắt bộ hàm sắc nhọn cắn trả thẳng vào mũi và mắt của kẻ săn mồi! Cú phản công bất ngờ, tàn nhẫn và đau đớn đến thấu xương khiến bất kỳ con báo nào cũng phải hoảng loạn nhả ra ngay lập tức!",
        extracted_visual_details=[
            "Báo hoa mai ngoạm răng vào lớp da gáy lỏng lẻo của Lửng Mật",
            "Lửng Mật xoay ngược cơ thể 180 độ ngay bên trong bao da cổ",
            "Hàm răng Lửng Mật cắn trả thẳng vào mũi khiến báo hoa mai trợn mắt hoảng loạn đau đớn",
        ],
        gemini_prompt_vi=(
            "Tạo hình ảnh 2D minh họa truyện tranh trên nền trắng tinh khiết (#FFFFFF), nét mực đen sắc nét, màu sắc sống động: "
            "Một con báo hoa mai đang ngoạm vào phần da gáy lỏng lẻo của Lửng Mật, nhưng Lửng Mật đã xoay ngược cơ thể 180 độ "
            "ngay bên trong lớp da của chính mình và há hàm răng sắc nhọn cắn trả thẳng vào mũi con báo hoa mai khiến nó trợn "
            "mắt đau đớn tột cùng. Nền trắng hoàn toàn."
        ),
        asset_filename="c3_badger_turn_180.png",
        badge_text="02. XOAY 180° PHẢN ĐÒN",
        caption_text="Tuyệt kỹ xoay 180 độ trong da: Cắn trả thẳng vào mũi báo hoa mai",
    ),
    SentenceVisualBeatPrompt(
        scene_id="scene03",
        beat_id="beat_03",
        start_ms=51320,
        end_ms=78360,
        narration_vi="Cơ chế thứ hai là đôi bàn chân trang bị móng vuốt lưỡi hái trước ngực. Mỗi ngón chân trước của Lửng Mật sở hữu chiếc móng dài hơn năm centimet, cong vút và cứng như mũi khoan thép tôi. Nó có thể xới tung tổ mối cứng như khối bê tông chỉ trong vài phút, hay đào sâu vào lòng đất tạo hang trú ẩn kiên cố nhanh hơn một người khỏe mạnh dùng xẻng xúc đất. Còn bộ hàm của nó đủ khỏe để cắn vỡ cả mai rùa dày, nghiền nát xương con mồi ngọt xớt như nhai kẹo giòn.",
        extracted_visual_details=[
            "Móng vuốt chân trước dài hơn 5cm cong như lưỡi hái thép cào tung tổ mối cứng như bê tông",
            "Đào đường hầm đất nhanh hơn cả người đàn ông khỏe mạnh cầm xẻng xúc đất toát mồ hôi",
            "Bộ hàm khỏe khoắn cắn vỡ nát chiếc mai rùa dày và khúc xương ống lớn",
        ],
        gemini_prompt_vi=(
            "Tạo hình ảnh 2D minh họa truyện tranh trên nền trắng tinh khiết (#FFFFFF), nét mực đen sắc nét, màu sắc sống động, "
            "KHÔNG CÓ CHỮ (NO TEXT, NO WORDS, NO LABELS): Bên trái là Lửng Mật dùng đôi móng vuốt trước cong dài hơn 5cm như "
            "lưỡi hái thép cào tung ụ tổ mối cứng như bê tông và đào hầm nhanh hơn cả người đàn ông lực lưỡng cầm xẻng xúc đất "
            "toát mồ hôi đứng kế bên. Bên phải là hàm răng cực khỏe của Lửng Mật đang cắn vỡ nát cả chiếc mai rùa dày cứng và "
            "khúc xương ống to lớn. Nền trắng hoàn toàn."
        ),
        asset_filename="c3_badger_sharp_claws.png",
        badge_text="03. VUỐT 5CM & HÀM THÉP",
        caption_text="Vuốt 5cm đào nhanh hơn người xúc xẻng & Hàm nghiền nát mai rùa",
    ),
    SentenceVisualBeatPrompt(
        scene_id="scene03",
        beat_id="beat_04",
        start_ms=78360,
        end_ms=104000,
        narration_vi="Và cơ chế thứ ba là vũ khí phòng vệ hóa học độc môn phía sau đuôi. Lửng Mật sở hữu một túi xạ hương đặc biệt có thể đảo ngược ra ngoài, phun ra luồng khí gas thối nồng nặc đến nghẹt thở. Luồng khí này không chỉ xua đuổi bầy ong vò vẽ hung hãn khi nó cướp tổ mật, mà còn làm tê liệt khứu giác siêu nhạy của bầy thú săn mồi lớn, khiến chúng buồn nôn, cay mắt và buộc phải tháo chạy trong sự ức chế tột cùng!",
        extracted_visual_details=[
            "Lửng Mật đứng cạnh tổ ong mật, chổng đuôi phun luồng khói khí gas xanh vàng nồng nặc từ túi xạ hương",
            "Đàn ong vò vẽ hung hãn bị choáng váng rơi lả tả",
            "Sư tử và linh cẩu phải lấy hai chân bịt chặt mũi, chảy nước mắt cay xè, mặt xanh lè buồn nôn tháo chạy",
        ],
        gemini_prompt_vi=(
            "Tạo hình ảnh 2D minh họa truyện tranh hài hước trên nền trắng tinh khiết (#FFFFFF), nét mực đen sắc nét, màu sắc sống động, "
            "KHÔNG CÓ CHỮ (NO TEXT, NO WORDS, NO LABELS): Một con Lửng Mật đứng cạnh tổ ong mật vàng óng, chổng ngược đuôi phun ra "
            "luồng khói khí gas màu xanh vàng nồng nặc. Phía bên trái, đàn ong vò vẽ bị choáng váng rơi lả tả. Phía bên phải, sư tử "
            "và linh cẩu phải lấy hai chân trước bịt chặt mũi, nước mắt chảy ròng ròng vì cay mắt, mặt xanh lè buồn nôn tháo chạy. "
            "Nền trắng hoàn toàn."
        ),
        asset_filename="c3_badger_crushing_turtle_musk.png",
        badge_text="04. BOM XẠ HƯƠNG",
        caption_text="Bom xạ hương: Làm choáng đàn ong vò vẽ, sư tử & linh cẩu bịt mũi chạy",
    ),

    # ──────────────────────── SCENE 04 (4 Beats) ────────────────────────
    SentenceVisualBeatPrompt(
        scene_id="scene04",
        beat_id="beat_01",
        start_ms=0,
        end_ms=30600,
        narration_vi="Thế nhưng tất cả những vũ khí trên vẫn chưa là gì so với thực đơn ăn uống điên rồ và kỳ quặc bậc nhất hành tinh của gã giang hồ này. Lửng Mật nổi tiếng là kẻ nghiện ăn nọc độc tự nhiên. Món ăn khoái khẩu của nó là những loài rắn chết chóc nhất: Rắn phì châu Phi, rắn hổ mang thổi nọc và cả chúa tể rắn hổ mang! Bạn có biết: Rắn chiếm tới hơn một phần tư khẩu phần ăn hằng ngày của nó, và một giọt nọc độc của rắn phì đủ để làm tan rữa tế bào cơ, giết chết mười lăm người trưởng thành trong đau đớn tột cùng chỉ sau ít phút.",
        extracted_visual_details=[
            "Lửng Mật háu ăn liếm mép trước 3 loài rắn: Rắn phì châu Phi (Puff Adder), Rắn hổ mang thổi nọc, và Rắn hổ mang chúa",
            "Giọt nọc độc tím nhỏ xuống làm ăn mòn tan chảy cả tảng đá",
            "Biểu đồ chiếc đĩa thức ăn chia 4 phần với 1/4 khẩu phần là rắn độc",
        ],
        gemini_prompt_vi=(
            "Tạo hình ảnh 2D minh họa truyện tranh trên nền trắng tinh khiết (#FFFFFF), nét mực đen sắc nét, màu sắc sống động, "
            "KHÔNG CÓ CHỮ (NO TEXT, NO WORDS, NO LABELS): Một con Lửng Mật háu ăn đang đứng liếm mép trước 3 loài rắn kịch độc: "
            "(1) Rắn Phì châu Phi thân mập hoa văn chữ V đang nhỏ giọt nọc độc tím làm tan chảy tảng đá bên dưới, (2) Rắn Hổ Mang "
            "Thổi Nọc đang phun tia độc, và (3) Rắn Hổ Mang Chúa khổng lồ phì mang. Bên góc phải có biểu đồ hình tròn chiếc đĩa "
            "thức ăn chia 4 phần, trong đó 1/4 chiếc đĩa xếp đầy rắn độc. Nền trắng hoàn toàn."
        ),
        asset_filename="c4_badger_venom_diet_3snakes.png",
        badge_text="01. THỰC ĐƠN KỊCH ĐỘC",
        caption_text="Thực đơn điên rồ: 1/4 khẩu phần là Rắn Phì, Hổ Mang Thổi Nọc & Hổ Mang Chúa",
    ),
    SentenceVisualBeatPrompt(
        scene_id="scene04",
        beat_id="beat_02",
        start_ms=30600,
        end_ms=47480,
        narration_vi="Vậy điều gì sẽ xảy ra khi một con rắn hổ mang khổng lồ cắn ngập đôi răng nanh đầy nọc độc thần kinh thẳng vào mặt của Lửng Mật? Liệu kẻ liều lĩnh này có phải trả giá bằng cả mạng sống cho sự ngông cuồng của mình không? Câu trả lời là một cú bẻ lái kinh điển của tiến hóa sinh học làm giới khoa học ngỡ ngàng!",
        extracted_visual_details=[
            "Trận kịch chiến sinh tử giữa Lửng Mật và Rắn Hổ Mang Chúa khổng lồ phì mang rộng",
            "Rắn hổ mang tung đòn cắn nanh độc trực diện trong khi Lửng Mật lao vào ghì chặt cổ rắn",
        ],
        gemini_prompt_vi=(
            "Tạo hình ảnh 2D minh họa truyện tranh trên nền trắng tinh khiết (#FFFFFF), nét mực đen sắc nét, màu sắc sống động: "
            "Cảnh giao chiến kịch tính ở cự ly gần giữa Lửng Mật và một con Rắn Hổ Mang Chúa khổng lồ đang phì mang bành rộng, "
            "nanh rắn văng những giọt nọc độc khi Lửng Mật dũng mãnh lao vào ngoạm chặt cổ rắn. Nền trắng hoàn toàn."
        ),
        asset_filename="c4_badger_vs_cobra.png",
        badge_text="02. TỬ CHIẾN HỔ MANG",
        caption_text="Đối đầu sinh tử: Hổ Mang Chúa cắn ngập răng nanh kịch độc vào mặt",
    ),
    SentenceVisualBeatPrompt(
        scene_id="scene04",
        beat_id="beat_03",
        start_ms=47480,
        end_ms=70680,
        narration_vi="Các nhà di truyền học phát hiện ra rằng, các thụ thể nicotinic acetylcholine trong hệ thần kinh của Lửng Mật đã trải qua đột biến phân tử sau hàng triệu năm đối đầu sinh tử với loài rắn. Đột biến này hoạt động như một lớp áo giáp phân tử kiên cố, khiến độc tố thần kinh cực mạnh của rắn không thể bám vào để làm tê liệt hệ cơ quan hô hấp của nó! Nọc độc rắn khi vào máu nó chẳng khác nào một liều thuốc mê liều cao.",
        extracted_visual_details=[
            "Sơ đồ màng tế bào thần kinh với thụ thể Nicotinic Acetylcholine đột biến",
            "Khiên năng lượng phân tử hình lục giác màu xanh ngọc lục bảo bao bọc thụ thể, đánh bật các giọt độc tố màu tím gai góc làm chúng vỡ vụn",
            "Chú Lửng Mật bên cạnh tự tin nháy mắt giơ ngón tay cái (thumbs-up)",
        ],
        gemini_prompt_vi=(
            "Tạo hình ảnh 2D minh họa truyện tranh giải phẫu sinh học phân tử trên nền trắng tinh khiết (#FFFFFF), "
            "nét mực đen sắc nét, màu sắc sống động, KHÔNG CÓ CHỮ (NO TEXT, NO WORDS, NO LABELS, NO BUBBLES): "
            "Bên trái là sơ đồ mặt cắt màng tế bào thần kinh với cấu trúc thụ thể sinh học được bao bọc bởi chiếc khiên "
            "năng lượng tổ ong phát sáng màu xanh ngọc lục bảo kiên cố, đánh bật hàng loạt giọt nọc độc màu tím gai góc "
            "đang lao tới làm chúng vỡ vụn. Bên phải là chú Lửng Mật tự tin nháy mắt giơ ngón tay cái lên. Nền trắng hoàn toàn."
        ),
        asset_filename="c4_acetylcholine_molecular_shield.png",
        badge_text="03. KHIÊN PHÂN TỬ",
        caption_text="Đột biến thụ thể Acetylcholine: Áo giáp phân tử chặn đứng nọc độc thần kinh",
    ),
    SentenceVisualBeatPrompt(
        scene_id="scene04",
        beat_id="beat_04",
        start_ms=70680,
        end_ms=111280,
        narration_vi="Khi bị rắn hổ mang cắn trúng, nọc độc vẫn ngấm vào tuần hoàn máu. Lúc này, Lửng Mật sẽ từ từ lảo đảo, lăn đùng ra đất và rơi vào trạng thái hôn mê sâu giống hệt như một gã say vừa uống cạn một chum rượu mạnh. Toàn thân nó mềm nhũn, tim đập chậm lại suốt hai đến ba tiếng đồng hồ khiến kẻ thù tưởng nó đã chết chắc. Thế nhưng khi men say nọc độc tan hết và gan trung hòa xong độc chất, Lửng Mật bỗng mở to mắt, đứng dậy lắc đầu rũ lông tỉnh queo như vừa ngủ trưa dậy, rồi thản nhiên cúi xuống nhai nốt nửa con rắn còn lại như một món ăn vặt ngon lành! Thậm chí nó còn khoái chí liếm mép như vừa thưởng thức xong một bữa tiệc hoàng gia!",
        extracted_visual_details=[
            "Bên trái: Lửng Mật nằm ngửa mềm nhũn ngủ mê man như gã say rượu bên chum rượu đổ, đồng hồ cát 2 tiếng và lá gan đang lọc độc",
            "Bên phải: Lửng Mật tỉnh dậy mở to mắt sảng khoái, nhai ngấu nghiến nửa thân con rắn hổ mang còn lại và khoái chí liếm mép",
        ],
        gemini_prompt_vi=(
            "Tạo hình ảnh 2D minh họa truyện tranh trên nền trắng tinh khiết (#FFFFFF), nét mực đen sắc nét, màu sắc sống động, "
            "KHÔNG CÓ CHỮ (NO TEXT, NO WORDS, NO LABELS): Bức tranh đối chiếu trước và sau của Lửng Mật: Bên trái là Lửng Mật "
            "lăn đùng ra đất nằm ngửa mềm nhũn hôn mê sâu giống hệt gã say rượu nằm cạnh chum rượu đổ, phía trên có đồng hồ cát "
            "2 tiếng và biểu tượng gan lọc sạch độc tố. Bên phải là Lửng Mật vừa tỉnh dậy sảng khoái, nhai ngấu nghiến nửa thân "
            "con rắn hổ mang còn lại và khoái chí liếm mép! Nền trắng hoàn toàn."
        ),
        asset_filename="c4_badger_sleeping_venom.png",
        badge_text="04. NGỦ 2 TIẾNG DẬY ĂN TIẾP",
        caption_text="Ngủ mê 2 tiếng như say rượu để gan lọc độc, rồi tỉnh dậy chén nốt con rắn",
    ),

    # ──────────────────────── SCENE 05 (4 Beats) ────────────────────────
    SentenceVisualBeatPrompt(
        scene_id="scene05",
        beat_id="beat_01",
        start_ms=0,
        end_ms=25480,
        narration_vi="Bên cạnh thân thể dẻo dai và khả năng kháng độc vô song, trí thông minh của Lửng Mật mới thực sự là thứ khiến các nhà động vật học trên thế giới phải ngả mũ thán phục. Minh chứng sống động nhất cho trí tuệ siêu phàm này chính là chú lửng mật Stoffel tại Trung tâm Phục hồi Hoang dã Moholoholo ở Nam Phi. Stoffel nổi tiếng toàn cầu đến mức được đài truyền hình BBC của Anh làm riêng một bộ phim tài liệu về những phi vụ vượt ngục không tưởng của nó.",
        extracted_visual_details=[
            "Chú Lửng Mật Stoffel đứng tự hào trên bờ tường khu bảo tồn Moholoholo Nam Phi",
            "Đoàn làm phim tài liệu chĩa máy quay phim chuyên nghiệp lớn và micro thu âm về phía Stoffel",
            "Nhà động vật học đội mũ thám hiểm ngả mũ cúi đầu thán phục trí tuệ của nó",
        ],
        gemini_prompt_vi=(
            "Tạo hình ảnh 2D minh họa truyện tranh trên nền trắng tinh khiết (#FFFFFF), nét mực đen sắc nét, màu sắc sống động, "
            "KHÔNG CÓ CHỮ (NO TEXT, NO WORDS, NO LABELS): Chú Lửng Mật Stoffel đang đứng đầy tự hào và tinh quái trên bờ tường "
            "khu bảo tồn hoang dã ở Nam Phi, trước mặt là đoàn làm phim tài liệu đang chĩa máy quay phim chuyên nghiệp lớn và "
            "micro thu âm về phía nó. Bên cạnh có một nhà động vật học đội mũ thám hiểm đang ngả mũ cúi đầu thán phục. Nền trắng hoàn toàn."
        ),
        asset_filename="c5_stoffel_bbc_star.png",
        badge_text="01. NGÔI SAO PHIM TÀI LIỆU",
        caption_text="Huyền thoại Stoffel ở Nam Phi: Khiến giới khoa học ngả mũ & lên sóng BBC",
    ),
    SentenceVisualBeatPrompt(
        scene_id="scene05",
        beat_id="beat_02",
        start_ms=25480,
        end_ms=60040,
        narration_vi="Ban đầu, các chuyên gia nhốt Stoffel trong một khu chuồng rào tường bê tông cao lút đầu người. Bạn nghĩ bức tường bê tông cao sẽ giam giữ được nó? Stoffel đã dùng chân cào đất bùn, nặn thành từng viên bi đất tròn to tướng rồi đẩy chúng vào góc tường, xếp chồng lên nhau thành một gò đất cao để nhảy vọt qua rào trốn thoát! Khi các nhân viên dọn sạch bùn đất, Stoffel đi gom những cành cây khô, dựng đứng tựa vào tường làm thang leo. Họ dọn sạch cành cây, nó liền hợp sức lăn những tảng đá lớn lại. Nó thậm chí còn trộm cả chổi quét sân của nhân viên để làm đòn bẩy vượt rào!",
        extracted_visual_details=[
            "Tường bê tông chuồng giam cao lút đầu người",
            "Gò bi đất bùn tròn to được nặn và xếp chồng lên nhau ở góc tường",
            "Những tảng đá lớn được lăn gom lại và cành cây khô dựng đứng dựa vào tường làm thang",
            "Stoffel cầm cây chổi quét sân cán gỗ dài trộm của nhân viên làm đòn bẩy trèo lên đỉnh tường",
        ],
        gemini_prompt_vi=(
            "Tạo hình ảnh 2D minh họa truyện tranh trên nền trắng tinh khiết (#FFFFFF), nét mực đen sắc nét, màu sắc sống động, "
            "KHÔNG CÓ CHỮ (NO TEXT, NO WORDS, NO LABELS): Chú Lửng Mật Stoffel đang thực hiện liền lúc 4 chiêu trò vượt ngục thông minh "
            "tại bức tường bê tông cao: dưới chân góc tường là những viên bi đất bùn tròn to được nặn và xếp chồng lên nhau, bên cạnh "
            "là những tảng đá lớn được lăn gom lại và những cành cây khô dựng đứng dựa vào tường làm thang, còn trên tay Stoffel đang "
            "cầm cây chổi quét sân cán gỗ dài làm đòn bẩy trèo lên đỉnh tường! Nền trắng hoàn toàn."
        ),
        asset_filename="c5_stoffel_mud_balls_broom_escape.png",
        badge_text="02. 4 CHIÊU VƯỢT NGỤC",
        caption_text="4 chiêu vượt tường bê tông: Xếp bi bùn, dựng cành cây, lăn đá & trộm chổi",
    ),
    SentenceVisualBeatPrompt(
        scene_id="scene05",
        beat_id="beat_03",
        start_ms=60040,
        end_ms=83000,
        narration_vi="Và khi chuồng bị dọn nhẵn thín không còn lấy một viên sỏi, Stoffel thậm chí đã làm quen với một con lửng mật cái cùng phòng, dụ dỗ con cái đứng sát góc tường để nó trèo lên lưng con cái phóng vọt ra ngoài! Và điều hài hước nhất là mục đích vượt ngục của nó: Không phải để tìm đường về với rừng sâu, mà là xông thẳng vào chuồng bầy sư tử kế bên để khiêu chiến và trêu chọc chúa sơn lâm!",
        extracted_visual_details=[
            "Góc tường bê tông bị dọn sạch trơn nhẵn thín",
            "Stoffel dụ bạn gái lửng mật cái đứng sát góc tường rồi giẫm lên lưng bạn gái làm bàn đạp phóng vọt qua đỉnh tường",
            "Bên kia bức tường là chuồng sư tử đực, Stoffel lao thẳng sang chuồng sư tử để khiêu chiến",
        ],
        gemini_prompt_vi=(
            "Tạo hình ảnh 2D minh họa truyện tranh hài hước trên nền trắng tinh khiết (#FFFFFF), nét mực đen sắc nét, màu sắc sống động, "
            "KHÔNG CÓ CHỮ (NO TEXT, NO WORDS, NO LABELS): Trong góc tường bê tông cao đã bị dọn sạch trơn nhẵn thín, chú Lửng Mật đực "
            "Stoffel đang đứng giẫm hai chân sau lên thẳng lưng cô bạn gái lửng mật cái để làm bàn đạp bật nhảy vọt qua đỉnh tường bê tông! "
            "Bên kia bức tường là khu chuồng của sư tử lớn, và Stoffel đang lao thẳng sang phía con sư tử để khiêu chiến! Nền trắng hoàn toàn."
        ),
        asset_filename="c5_stoffel_escape.png",
        badge_text="03. BÀN ĐẠP BẠN GÁI",
        caption_text="Dụ bạn gái làm bàn đạp vượt tường nhẵn thín, nhảy thẳng sang chuồng sư tử",
    ),
    SentenceVisualBeatPrompt(
        scene_id="scene05",
        beat_id="beat_04",
        start_ms=83000,
        end_ms=105920,
        narration_vi="Ngay cả khi bị ba con sư tử đực to lớn bao vây nghẹt thở, Lửng Mật tuyệt đối không bao giờ lùi bước. Nó xù dựng toàn bộ lông lưng, gầm rít dữ dội, phun túi xạ hôi thối và lao thẳng vào giữa bầy sư tử khiến các chúa tể thảo nguyên cũng phải e dè nhượng bộ vì nhận ra cái giá phải trả quá đắt để đổi lấy một bữa ăn dai nhách! Đây chính là đẳng cấp của kẻ giang hồ lỳ lợm nhất thế giới tự nhiên!",
        extracted_visual_details=[
            "1 con Lửng Mật nhỏ bé xù dựng toàn bộ lông lưng, há miệng gầm rít lao thẳng về phía trước",
            "3 con sư tử đực bờm lớn bao vây xung quanh phải giật mình lùi bước nhượng bộ",
        ],
        gemini_prompt_vi=(
            "Tạo hình ảnh 2D minh họa truyện tranh trên nền trắng tinh khiết (#FFFFFF), nét mực đen sắc nét, màu sắc sống động, "
            "KHÔNG CÓ CHỮ (NO TEXT, NO WORDS, NO LABELS): Một con Lửng Mật nhỏ bé xù dựng toàn bộ lông lưng, há miệng gầm rít dữ dội "
            "lao thẳng vào giữa vòng vây của 3 con sư tử đực to lớn khiến cả 3 chúa sơn lâm phải giật mình chùn bước lùi lại. Nền trắng hoàn toàn."
        ),
        asset_filename="c5_badger_vs_3_lions.png",
        badge_text="04. ĐẠI CHIẾN 1 CHỌI 3",
        caption_text="Đẳng cấp giang hồ: 1 mình xù lông gầm rít lao vào 3 sư tử đực khiến cả bầy lùi bước",
    ),

    # ──────────────────────── SCENE 06 (2 Beats) ────────────────────────
    SentenceVisualBeatPrompt(
        scene_id="scene06",
        beat_id="beat_01",
        start_ms=0,
        end_ms=24680,
        narration_vi="Lửng Mật chính là minh chứng sống động nhất trong tự nhiên cho chân lý: Kích thước cơ thể không bao giờ quyết định vị thế của bạn trên đấu trường sinh tồn. Một sinh vật nhỏ bé nhưng mang ý chí kiên cường, lòng dũng cảm bất diệt và tinh thần không bao giờ khuất phục trước bất kỳ thế lực nào, hoàn toàn có thể khiến cả những kẻ khổng lồ mạnh nhất phải kiêng dè nể sợ. Hãy nhớ rằng: Đừng bao giờ đánh giá thấp bất kỳ ai chỉ qua vẻ bề ngoài!",
        extracted_visual_details=[
            "Lửng Mật đứng hiên ngang oai vệ trên đỉnh mỏm đá cao giữa thảo nguyên bao la",
            "Dáng đứng ưỡn ngực ngẩng cao đầu đầy bản lĩnh và ý chí bất khuất",
        ],
        gemini_prompt_vi=(
            "Tạo hình ảnh 2D minh họa truyện tranh trên nền trắng tinh khiết (#FFFFFF), nét mực đen sắc nét, màu sắc sống động, "
            "KHÔNG CÓ CHỮ (NO TEXT, NO WORDS, NO LABELS): Một con Lửng Mật đứng hiên ngang oai phong trên đỉnh một mỏm đá cao "
            "nhìn ra toàn cảnh thảo nguyên rộng lớn bên dưới, ngực ưỡn cao đầy khí phách bất khuất của kẻ chiến thắng. Nền trắng hoàn toàn."
        ),
        asset_filename="c6_badger_triumphant_rock.png",
        badge_text="Ý CHÍ BẤT KHUẤT",
        caption_text="Bài học sinh tồn: Kích thước cơ thể không bao giờ quyết định vị thế của bạn",
    ),
    SentenceVisualBeatPrompt(
        scene_id="scene06",
        beat_id="beat_02",
        start_ms=24680,
        end_ms=62320,
        narration_vi="Thế nhưng, gã Chí Phèo châu Phi này mới chỉ là câu chuyện mở màn cho chuỗi hành trình khám phá những bí ẩn kỳ dị của thế giới muông thú. Nếu bạn nghĩ sự tàn bạo và khó lường chỉ tồn tại trên đất liền thì bạn đã nhầm to. Bởi vì khi lặn xuống đại dương bao la, có một loài sinh vật nổi tiếng với vẻ ngoài siêu đáng yêu, hay nằm ngửa nắm tay nhau ngủ trên mặt nước... nhưng ẩn sau đó lại là những hành vi tâm lý rùng rợn và tàn bạo bậc nhất thế giới động vật: Đó chính là Rái Cá Biển! Chúng bắt cóc con non của hải cẩu, quấy rối các loài vật khác và có những góc khuất man rợ khiến bạn phải lạnh gáy! Cùng vén màn bí mật rùng rợn của loài vật dễ thương này trong tập tiếp theo nhé!",
        extracted_visual_details=[
            "Nửa bên trái: Hai chú Rái Cá Biển nằm ngửa trên mặt nước xanh ngọc, nắm tay nhau ngủ mỉm cười siêu đáng yêu",
            "Nửa bên phải: Góc khuất tàn bạo của con Rái Cá Biển đực ánh mắt sắc lạnh đang giữ chặt bắt cóc một chú hải cẩu con tội nghiệp run rẩy sợ hãi",
        ],
        gemini_prompt_vi=(
            "Tạo hình ảnh 2D minh họa truyện tranh trên nền trắng tinh khiết (#FFFFFF), nét mực đen sắc nét, màu sắc sống động, "
            "KHÔNG CÓ CHỮ (NO TEXT, NO WORDS, NO LABELS): Một bức tranh hai nửa tương phản gây sốc về loài Rái Cá Biển: "
            "Phía bên trái là hai chú rái cá biển bộ lông nâu mềm mại đang nằm ngửa bập bềnh trên làn nước biển xanh ngọc, "
            "hai bàn tay nắm chặt lấy nhau ngủ ngon lành với khuôn mặt mỉm cười siêu đáng yêu. Phía bên phải là góc khuất đáng sợ "
            "của một con rái cá biển đực hung dữ với ánh mắt sắc lạnh đang giữ chặt bắt cóc một chú hải cẩu con tội nghiệp đang "
            "run rẩy sợ hãi. Nền trắng hoàn toàn."
        ),
        asset_filename="c6_sea_otter_teaser.png",
        badge_text="TẬP 2: RÁI CÁ BIỂN",
        caption_text="Hé lộ Tập 2: Rái Cá Biển nắm tay ngủ đáng yêu nhưng bắt cóc hải cẩu con!",
    ),
]


def export_prompt_catalog_json(out_path: Path) -> Path:
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "protocol": "Zero-Imagination-Gap Sentence-Level Visual Prompt Architect V6",
        "total_beats": len(EPISODE_01_LITERAL_PROMPT_CATALOG),
        "beats": [asdict(b) for b in EPISODE_01_LITERAL_PROMPT_CATALOG],
    }
    out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return out_path


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[2]
    target = root / "projects" / "tap-01-lung-mat" / "specs" / "sentence_visual_prompts_v6.json"
    export_prompt_catalog_json(target)
    print(f"[PromptArchitect V6] Exported {len(EPISODE_01_LITERAL_PROMPT_CATALOG)} literal sentence-level prompts -> {target}")

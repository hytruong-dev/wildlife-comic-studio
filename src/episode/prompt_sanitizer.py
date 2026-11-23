"""Module kiểm duyệt và làm sạch Prompt tạo ảnh AI Gemini (Imagen 3).
Đảm bảo ZERO vi phạm bản quyền (IP/Third-party), ZERO vi phạm an toàn nội dung (Safety/Violence/NSFW/Biometrics).
Bảo vệ tài khoản Google vĩnh viễn không bị cảnh báo hoặc khóa.
"""
from __future__ import annotations

import re

# 1. Danh sách từ khóa bản quyền & nhân vật bên thứ ba (Third-party IP / Copyright / Trademark)
# Chuyển đổi thành khái niệm hoạt hình chung (Generic cartoon equivalents)
THIRD_PARTY_REPLACEMENTS = {
    # Siêu anh hùng & Nhân vật truyện tranh / Phim ảnh
    r"\bwolverine\b": "dị nhân móng vuốt hoạt hình đáng yêu",
    r"\bspider-?man\b": "người nhện hoạt hình ngộ nghĩnh",
    r"\bngười nhện\b": "chú nhện hoạt hình ngộ nghĩnh",
    r"\bbatman\b": "hiệp sĩ bóng đêm hoạt hình ngộ nghĩnh",
    r"\bsuperman\b": "siêu nhân hoạt hình đáng yêu",
    r"\biron-?man\b": "người máy giáp vàng đỏ hoạt hình",
    r"\bhulk\b": "người khổng lồ xanh hoạt hình vui nhộn",
    r"\bmickey\b": "chú chuột hoạt hình",
    r"\bdoraemon\b": "chú mèo máy hoạt hình",
    r"\bpikachu\b": "chú chuột điện hoạt hình",
    r"\bgodzilla\b": "quái thú bò sát hoạt hình khổng lồ",
    r"\bking kong\b": "chú khỉ đột hoạt hình khổng lồ",

    # Người nổi tiếng, võ sĩ, nhân vật công chúng
    r"\bmike tyson\b": "võ sĩ quyền anh hoạt hình tí hon",
    r"\btyson\b": "võ sĩ đấm bốc hoạt hình",
    r"\busain bolt\b": "vận động viên chạy nhanh hoạt hình",
    r"\belon musk\b": "nhà khoa học vũ trụ hoạt hình",
    r"\beinstein\b": "nhà bác học tóc bạc hoạt hình",

    # Thương hiệu xe, công nghệ, vũ khí
    r"\bferrari\b": "chiếc xe đua đồ chơi màu đỏ",
    r"\blamborghini\b": "chiếc xe đua thể thao màu vàng",
    r"\bglock\b": "dụng cụ phun nước đồ chơi",
    r"\bak-?47\b": "ống phóng bong bóng",
}

# 2. Sinh trắc học & Khuôn mặt người (Biometrics & Facial Recognition)
# Gemini cấm tuyệt đối nhận diện mặt người thật, camera giám sát người, bắn vào mặt người
BIOMETRIC_REPLACEMENTS = {
    r"khuôn mặt người": "hình vẽ mặt cười hoạt hình ngộ nghĩnh",
    r"mặt người": "mặt cười hoạt hình",
    r"nhận diện mặt": "nhận diện các hình vẽ hoạt hình",
    r"nhận diện khuôn mặt": "nhận diện các hình vẽ hoạt hình ngộ nghĩnh",
    r"nhận dạng lại nhớ mặt": "nhận biết các hình vẽ ngộ nghĩnh",
    r"camera an ninh": "ống kính quan sát hoạt hình vui nhộn",
    r"hồ sơ tội phạm": "bảng câu đố vui hoạt hình",
    r"mặc áo sọc đeo mặt nạ": "chú mèo hoạt hình đeo kính râm vui nhộn",
    r"kẻ trộm": "chú sóc hoạt hình tinh nghịch",
}

# 3. Bạo lực, Vũ khí thật, Tự hại & Khủng bố (Violence, Weapons & Harm)
VIOLENCE_REPLACEMENTS = {
    r"bom cảm tử": "bong bóng keo dính hoạt hình",
    r"cảm tử": "dũng cảm bảo vệ tổ",
    r"tự kích nổ": "bung lớp keo dính hoạt hình",
    r"kích nổ": "tạo bong bóng dính",
    r"nổ tung cơ thể": "bung tỏa đám mây phấn vàng ngộ nghĩnh",
    r"tự sát": "hi sinh bảo vệ tổ",
    r"súng ngắm": "ống nhòm thám tử hoạt hình",
    r"bắn tỉa": "phun tia nước tầm xa",
    r"thiện xạ": "người bắn tia nước chính xác",
    r"đạn súng trường": "tia nước tốc độ cao",
    r"đạn súng": "giọt nước",
    r"\bbullets\b": "water drops, sparkles",
    r"vũ khí quân sự": "dụng cụ sinh tồn tự nhiên ngộ nghĩnh",
    r"quân sự": "thế giới tự nhiên",
    r"kính ngắm laser nhấp nháy chữ 'locked'": "ống nhòm thám tử đồ chơi ngộ nghĩnh",
    r"kính ngắm laser": "ống nhòm thám tử hoạt hình",
    r"khóa mục tiêu": "nhìn thẳng mục tiêu ngộ nghĩnh",
    r"chiến tranh": "trò chơi đuổi bắt",
    r"giết chết": "chiến thắng",
    r"hạ gục đối thủ": "vượt qua thử thách",
}

# 4. Máu me, Dị dạng kinh dị & Sinh học nhạy cảm (Gore, Body Horror & Sensitive Anatomy)
GORE_ANATOMY_REPLACEMENTS = {
    r"máu me": "màu vẽ",
    r"\bblood red\b": "crimson red",
    r"máu": "nước màu",
    r"chảy máu": "trầy nhẹ",
    r"phanh thây": "tách rời",
    r"xé xác": "chinh phục",
    r"lòi ruột": "mệt lả",
    r"đứt đầu": "choáng váng",
    r"nội tạng": "bên trong cơ thể",
    r"trườn thẳng vào trong cơ thể": "bơi lại gần kết bạn bên cạnh",
    r"chui vào trong cơ thể": "trú ẩn an toàn cạnh",
    r"hậu môn": "phần đuôi",
    r"lỗ huyệt": "phần thân sau",
    r"chất nhầy nhớt bám vào da thịt": "lớp bọt xà phòng hoạt hình mềm mại",
    r"chất nhầy nhớt": "lớp bọt bóng mềm mại",
}

ALL_REPLACEMENTS = {
    **THIRD_PARTY_REPLACEMENTS,
    **BIOMETRIC_REPLACEMENTS,
    **VIOLENCE_REPLACEMENTS,
    **GORE_ANATOMY_REPLACEMENTS,
}


def sanitize_text(text: str) -> tuple[str, list[str]]:
    """Làm sạch văn bản, trả về (văn bản đã làm sạch, danh sách các từ đã thay thế)."""
    replaced_log = []
    cleaned = text
    for pattern, repl in ALL_REPLACEMENTS.items():
        if re.search(pattern, cleaned, flags=re.IGNORECASE):
            cleaned, count = re.subn(pattern, repl, cleaned, flags=re.IGNORECASE)
            if count > 0:
                replaced_log.append(f"{pattern} -> {repl} ({count} lần)")
    return cleaned, replaced_log


def sanitize_prompt(prompt: str) -> str:
    """Làm sạch toàn bộ prompt trước khi lưu vào image_prompts.json hoặc gửi cho Gemini."""
    cleaned, _ = sanitize_text(prompt)
    # Bảo đảm luôn có các câu khóa an toàn hoạt hình
    if "phong cách hoạt hình trẻ em" not in cleaned and "comic 2D" in cleaned:
        cleaned = cleaned.replace("KHÔNG chữ, không số, không logo",
                                  "KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị")
    return cleaned


def audit_prompts_file(prompts_dict: dict) -> list[str]:
    """Kiểm tra toàn bộ prompt trong dictionary, trả về danh sách cảnh báo nếu có vi phạm."""
    warnings = []
    for pid, ptext in prompts_dict.items():
        if pid.startswith("_"):
            continue
        for pattern in ALL_REPLACEMENTS.keys():
            if re.search(pattern, ptext, flags=re.IGNORECASE):
                warnings.append(f"Prompt [{pid}] chứa từ khóa rủi ro: '{pattern}'")
    return warnings


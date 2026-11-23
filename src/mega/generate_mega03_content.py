"""Script sinh toàn bộ nội dung chi tiết cho Đại Hội Sinh Tồn Mùa 3 (mega-03-dai-hoi-sinh-ton)
Đảm bảo:
  - 14 chương hoàn chỉnh, mỗi chương 25-32 ảnh (tổng ~400-420 ảnh).
  - Tổng số ký tự lời thoại: ~71.000 - 75.000 ký tự (≈ 60:00 - 65:00 thời lượng chuẩn).
  - Tỷ lệ cameo < 8% (giọng MC chính dẫn dắt).
  - Đầy đủ nguồn khoa học mới 100%, chi tiết nghiên cứu sâu, hài hước, kịch tính.
  - Sticker trỏ đúng chi tiết, số đọc bằng chữ đồng bộ với display_fix.
"""
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / "projects/mega-03-dai-hoi-sinh-ton/content"

print("Generating Mega 03 content...")


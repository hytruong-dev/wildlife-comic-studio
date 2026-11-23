# Tập 9 — script riêng

Đã chuyển thành công cụ chung (dùng cho mọi tập):
- phân cảnh: `specs/storyboard.json` -> `python src/episode/build_plans.py projects/tap-09-chim-canh-cut`
- ảnh Gemini: `node src/episode/gemini_gen.cjs projects/tap-09-chim-canh-cut long|shorts|extra`
- banner/thumbnail prompt: `python src/episode/extra_prompts.py projects/tap-09-chim-canh-cut`

`_legacy_build_plans_ep09.py` = bản gốc đã dùng khi sản xuất (chỉ để tham khảo; storyboard.json được sinh từ nó và tái tạo plan y hệt).

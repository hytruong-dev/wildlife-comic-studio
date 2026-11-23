import json
from pathlib import Path

p = Path("projects/tap-35-ca-voi-sat-thu/episode.json")
ep = json.loads(p.read_text(encoding="utf-8"))

ep["seo"]["shorts_title"] = "Bí Mật Khiến Cá Mập Trắng Tháo Chạy Khỏi Bố Già Đại Dương?!"
ep["seo"]["en_title"] = "Killer Whale: Oceanic Syndicate & Why Great White Sharks Flee?! | EP35"
ep["seo"]["en_hook"] = "Discover the incredible hunting tactics, matriarchal empire, and intelligence of Orcas."
ep["seo"]["en_shorts_title"] = "Why Great White Sharks Flee from Killer Whales?!"

p.write_text(json.dumps(ep, ensure_ascii=False, indent=2), encoding="utf-8")
print("Updated ep35 SEO titles!")


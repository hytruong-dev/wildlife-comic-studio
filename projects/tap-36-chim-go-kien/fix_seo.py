# -*- coding: utf-8 -*-
import json

path = 'projects/tap-36-chim-go-kien/episode.json'
with open(path, encoding='utf-8') as f:
    ep = json.load(f)

ep['seo']['shorts_title'] = "Bí kíp Chim Gõ Kiến đập đầu 1.200G mà não không tổn thương?!"
ep['seo']['en_title'] = "Woodpecker: The 1,200G Shock-Absorbing Machine of Nature! | EP36"
ep['seo']['en_hook'] = "Discover how woodpeckers endure 12,000 head impacts daily at 1,200G acceleration without brain injury!"
ep['seo']['en_shorts_title'] = "How Do Woodpeckers Endure 1,200G Head Impacts?!"

with open(path, 'w', encoding='utf-8') as f:
    json.dump(ep, f, ensure_ascii=False, indent=2)

print("Updated ep36 seo fields successfully!")


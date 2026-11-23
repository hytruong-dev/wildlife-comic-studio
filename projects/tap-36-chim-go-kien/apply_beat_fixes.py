# -*- coding: utf-8 -*-
import json

path = 'projects/tap-36-chim-go-kien/specs/storyboard.json'
with open(path, encoding='utf-8') as f:
    sb = json.load(f)

# Update scene01
for b in sb['long']:
    if b.get('scene') == 'scene01':
        if b.get('at') == '12.000 lần mỗi ngày':
            b['at'] = 'Nếu các kỹ sư chế tạo xe hơi'
        elif b.get('at') == 'Nếu các kỹ sư chế tạo xe hơi':
            b['at'] = 'bài toán phân tán xung lực'
        elif b.get('at') == 'Mỗi cú va chạm chỉ diễn ra':
            b['at'] = 'một phần ngàn giây'
    elif b.get('scene') == 'scene02':
        if b.get('at') == 'tách ra làm hai nhánh':
            b['at'] = 'bò vòng lên tận đỉnh hộp sọ'
    elif b.get('scene') == 'scene06':
        if b.get('at') == 'không chỉ là một loài chim kiếm ăn':
            b['at'] = 'chúng ta phải nghiêng mình'
        elif b.get('at') == 'bình luận bên dưới nhé':
            b['at'] = 'giải pháp cơ khí nào'

with open(path, 'w', encoding='utf-8') as f:
    json.dump(sb, f, ensure_ascii=False, indent=2)

print("Updated storyboard.json successfully!")


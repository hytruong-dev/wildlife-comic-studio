# -*- coding: utf-8 -*-
import json

path = 'projects/tap-37-lac-da-sa-mac/specs/storyboard.json'
with open(path, encoding='utf-8') as f:
    sb = json.load(f)

# Scene 01
for b in sb['long']:
    if b.get('scene') == 'scene01':
        if b.get('at') == 'chỉ số sinh tồn của bệnh nhân':
            b['at'] = '15% lượng nước trong cơ thể'
        elif b.get('at') == '15% lượng nước trong cơ thể':
            b['at'] = 'mất tới 30%'
    elif b.get('scene') == 'scene04':
        if b.get('at') == 'nhóm lửa đun nấu ngay tại chỗ':
            b['at'] = 'khô cong như những viên sỏi gỗ'
    elif b.get('scene') == 'scene05':
        if b.get('at') == 'bốc hơi vô hình nhưng cực kỳ nguy hiểm':
            b['at'] = 'Mỗi hơi thở ra của con người'

# Shorts
for b in sb['shorts']:
    if b.get('at') == 'không hề chứa một giọt nước nào':
        b['at'] = 'Trái ngược với hiểu lầm'

with open(path, 'w', encoding='utf-8') as f:
    json.dump(sb, f, ensure_ascii=False, indent=2)

print("Applied 4 anchor fixes to ep37 storyboard!")


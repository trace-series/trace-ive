with open('trace-ive.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

lines[6661] = lines[6661].replace(
    'IVEメンバーゆかりの場所を地図で探し、巡礼を記録できるアプリです。<br><br>',
    'IVEの軌跡を、地図に刻もう。'
)

with open('trace-ive.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('✅ 完了')
print(lines[6661].strip())

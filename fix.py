with open('trace-ive.html', 'r', encoding='utf-8') as f:
    content = f.read()

old = 'IVEメンバーゆかりの場所を地図で探し、巡礼を記録できるアプリです。<br><br>'
new = 'IVEの軌跡を、地図に刻もう。'

if old in content:
    content = content.replace(old, new)
    print('✅ 完了')
else:
    print('❌ 見つかりません')

with open('trace-ive.html', 'w', encoding='utf-8') as f:
    f.write(content)

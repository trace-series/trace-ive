with open('trace-ive.html', 'r', encoding='utf-8') as f:
    content = f.read()

# カテゴリーとメンバーの判定をselectedに統一（active→selected）
old = "const catChip = document.querySelector('#post-cat-chips .chip.active');"
new = "const catChip = document.querySelector('#post-cat-chips .chip.selected');"

old2 = "const memberChip = document.querySelector('#post-member-chips .chip.active');"
new2 = "const memberChip = document.querySelector('#post-member-chips .chip.selected');"

if old in content:
    content = content.replace(old, new)
    print('✅ カテゴリー修正完了')
else:
    print('❌ カテゴリー対象が見つかりません')

if old2 in content:
    content = content.replace(old2, new2)
    print('✅ メンバー修正完了')
else:
    print('❌ メンバー対象が見つかりません')

with open('trace-ive.html', 'w', encoding='utf-8') as f:
    f.write(content)

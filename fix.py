with open('trace-ive.html', 'r', encoding='utf-8') as f:
    content = f.read()

# カテゴリーの判定をselectedに統一
content = content.replace(
    "const catChip = document.querySelector('#post-cat-chips .chip.active');",
    "const catChip = document.querySelector('#post-cat-chips .chip.selected');"
)

content = content.replace(
    "const memberChip = document.querySelector('#post-member-chips .chip.active');",
    "const memberChip = document.querySelector('#post-member-chips .chip.selected');"
)

with open('trace-ive.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ 完了')

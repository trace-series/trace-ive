with open('trace-ive.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 管理者パネルのリストIDをadmin-pending-listに変更
content = content.replace(
    'const list = document.getElementById(\'pending-list\');',
    'const list = document.getElementById(\'admin-pending-list\');'
)

content = content.replace(
    '<div id="pending-list">',
    '<div id="admin-pending-list">'
)

# 承認待ちバッジも対応
content = content.replace(
    'document.getElementById(\'pending-count-badge\')',
    'document.getElementById(\'pending-count-badge\')'
)

with open('trace-ive.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ 完了')

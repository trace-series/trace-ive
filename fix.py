with open('trace-ive.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    'missinglink4179.github.io/trace-ive',
    'trace-series.github.io/trace-ive'
)

with open('trace-ive.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ 完了')

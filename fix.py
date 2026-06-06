with open('/Users/missinglink/Documents/trace-ive/trace-ive.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    "const r = item.getAttribute('data-region') || 'tokyo'",
    "const r = item.getAttribute('data-region') || 'japan_other'"
)

with open('/Users/missinglink/Documents/trace-ive/trace-ive.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('done')

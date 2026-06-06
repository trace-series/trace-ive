with open('/Users/missinglink/Documents/trace-ive/trace-ive.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    "if (name === 'post') setTimeout(initPostForm, 50);",
    "if (name === 'post') setTimeout(initPostForm, 50);\n  if (name === 'route') renderRouteSpotList();"
)

with open('/Users/missinglink/Documents/trace-ive/trace-ive.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('done')

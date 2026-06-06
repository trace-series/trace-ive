import re

with open('/Users/missinglink/Documents/trace-ive/trace-ive.html', 'r', encoding='utf-8') as f:
    content = f.read()

# adminLevel行の後のregion行を削除
content = re.sub(r"(adminLevel: '[^']*',?\n)\s*region: '[^']*',?\n", r'\1', content)

count = content.count("region: '")
print('region count:', count)

with open('/Users/missinglink/Documents/trace-ive/trace-ive.html', 'w', encoding='utf-8') as f:
    f.write(content)

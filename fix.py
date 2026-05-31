with open('trace-ive.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 4705行目と4708行目を修正（0始まりなので-1）
lines[4704] = lines[4704].replace('.chip.active', '.chip.selected')
lines[4707] = lines[4707].replace('.chip.active', '.chip.selected')

with open('trace-ive.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('✅ 完了')
print('4705:', lines[4704].strip())
print('4708:', lines[4707].strip())

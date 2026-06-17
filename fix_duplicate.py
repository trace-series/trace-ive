path = 'trace-ive.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

old = 'function reportVisit() {\n    if (!currentSpot) return;\n    var sb = getSupabaseClient();'
new = '''function reportVisit() {
    if (window._reportVisitInProgress) return;
    window._reportVisitInProgress = true;
    if (!currentSpot) { window._reportVisitInProgress = false; return; }
    var sb = getSupabaseClient();'''

if old not in content:
    print('置き換え対象が見つかりませんでした。手動確認が必要です。')
else:
    content = content.replace(old, new)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('置き換え完了')

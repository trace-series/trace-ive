import sys, os
if len(sys.argv) < 2:
    print("使い方: python3 fix.py trace-ive.html")
    sys.exit(1)
fp = sys.argv[1]
if not os.path.exists(fp):
    print(f"見つかりません: {fp}")
    sys.exit(1)
with open(fp, 'r', encoding='utf-8') as f:
    html = f.read()
fixes = []
o = "    from { opacity: 0; transform: translateY(12px); }\n    to { opacity: 1; transform: translateY(0); }\n  }"
n = "@keyframes fadeUp {\n  from { opacity: 0; transform: translateY(12px); }\n  to { opacity: 1; transform: translateY(0); }\n}"
if o in html:
    html = html.replace(o, n); fixes.append("OK1 CSS fadeUp")
else:
    fixes.append("NG1 CSS fadeUp")
o = "c.classList.remove('active'));"
n = "c.classList.remove('selected'));"
if o in html:
    html = html.replace(o, n); fixes.append("OK2 remove active->selected")
else:
    fixes.append("NG2 remove active->selected")
o = "c.classList.toggle('active', c.dataset.member === member);"
n = "c.classList.toggle('selected', c.dataset.member === member);"
if o in html:
    html = html.replace(o, n); fixes.append("OK3 toggle active->selected")
else:
    fixes.append("NG3 toggle active->selected")
o = "document.getElementById('admin-pending-list');"
n = "document.getElementById('pending-list');"
if o in html:
    html = html.replace(o, n); fixes.append("OK4 pending-list")
else:
    fixes.append("NG4 pending-list")
out = fp.replace('.html', '_fixed.html')
with open(out, 'w', encoding='utf-8') as f:
    f.write(html)
for x in fixes:
    print(x)
print(f"完了: {out}")

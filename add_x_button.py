path = "/Users/missinglink/Documents/trace-ive/trace-ive.html"

with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

x_button_lines = [
    '      <button onclick="startWithX()" style="\n',
    '        padding:16px;background:#000000;\n',
    '        color:#ffffff;border:1.5px solid rgba(255,255,255,0.25);border-radius:16px;font-size:15px;\n',
    '        font-weight:700;cursor:pointer;font-family:\'Noto Sans JP\',sans-serif;\n',
    '        display:flex;align-items:center;justify-content:center;gap:8px;">\n',
    '        <span style="font-size:18px;font-weight:900;">𝕏</span>Xアカウントで始める\n',
    '      </button>\n'
]

insert_at = 7425
lines[insert_at:insert_at] = x_button_lines

with open(path, "w", encoding="utf-8") as f:
    f.writelines(lines)

print("挿入完了:", insert_at+1, "行目から", insert_at+len(x_button_lines), "行目")

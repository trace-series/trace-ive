path = "trace-ive.html"

with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

target_line = "    function reportVisit() {\n"
idx = None
for i, line in enumerate(lines):
    if line.strip() == "function reportVisit() {":
        idx = i
        break

if idx is None:
    print("見つかりませんでした")
else:
    insert_lines = [
        "      if (window._reportVisitInProgress) return;\n",
        "      window._reportVisitInProgress = true;\n"
    ]
    lines[idx+1:idx+1] = insert_lines
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(lines)
    print("挿入完了: " + str(idx+1) + "行目の直後に追加")

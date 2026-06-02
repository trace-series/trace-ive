with open('trace-ive.html', 'r', encoding='utf-8') as f:
    content = f.read()

changes = []

# 保存済みルートのダミーを削除
old = '''    <div id="saved-routes-list">
      <div class="saved-route-item">
        <div class="sri-left">
          <div class="sri-icon">🗺️</div>
          <div>
            <div class="sri-name">東京IVE遠征2024春</div>
            <div class="sri-meta">3スポット · 2024年3月</div>
          </div>
        </div>
        <div style="display:flex;gap:6px;">
          <button class="btn-secondary" style="padding:6px 10px;font-size:11px;" onclick="printRoute()">🖨️</button>
          <button class="btn-secondary" style="padding:6px 10px;font-size:11px;">𝕏</button>
        </div>
      </div>
    </div>'''
new = '    <div id="saved-routes-list"></div>'
if old in content:
    content = content.replace(old, new, 1)
    changes.append('保存済みルートダミー削除')

# ヘルプ・お問い合わせをX公式へ
old = '''      <div class="settings-item">
        <div class="settings-item-icon">❓</div>
        <div class="settings-item-text">ヘルプ・お問い合わせ</div>
        <div class="settings-item-arrow">›</div>
      </div>'''
new = '''      <div class="settings-item" onclick="window.open('https://x.com/traceI

with open('trace-ive.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 使い方ページを設定画面に追加
old = '      <div class="settings-item" onclick="showView(\'route\')">'

new = '''      <div class="settings-item" onclick="showView('howto')">
        <div class="settings-item-icon">📖</div>
        <div class="settings-item-text">使い方</div>
        <div class="settings-item-arrow">›</div>
      </div>
      <div class="settings-item" onclick="showView('route')">'''

content = content.replace(old, new)

# 使い方ビューを追加（view-routeの直前）
old2 = '  <!-- ROUTE VIEW -->'
new2 = '''  <!-- HOWTO VIEW -->
  <div id="view-howto" style="display:none;padding:20px 16px;">
    <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px;">
      <button onclick="showView(\'profile\')" style="background:var(--purple-pale);border:none;border-radius:10px;padding:6px 12px;font-size:13px;cursor:pointer;color:var(--purple-deep);">← 戻る</button>
      <div class="section-title" style="margin-bottom:0;">使い方</div>
    </div>
    <div class="section-sub">HOW TO USE</div>

    <div style="display:flex;flex-direction:column;gap:16px;margin-top:8px;">

      <div style="background:white;border-radius:18px;padding:20px;border:1px solid var(--border);box-shadow:0 2px 10px rgba(61,26,94,0.06);">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;">
          <div style="width:36px;height:36px;background:linear-gradient(135deg,var(--purple-deep),var(--red));border-radius:10px;display:flex;align-items:center;justify-content:center;color:white;font-size:18px;flex-shrink:0;">1</div>
          <div style="font-size:15px;font-weight:700;color:var(--purple-deep);">🗺️ 地図でスポットを探す</div>
        </div>
        <div style="font-size:13px;color:var(--text-mid);line-height:1.7;">IVEゆかりの聖地をマップで確認。メンバーやカテゴリーで絞り込みができます。</div>
      </div>

      <div style="background:white;border-radius:18px;padding:20px;border:1px solid var(--border);box-shadow:0 2px 10px rgba(61,26,94,0.06);">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;">
          <div style="width:36px;height:36px;background:linear-gradient(135deg,var(--purple-deep),var(--red));border-radius:10px;display:flex;align-items:center;justify-content:center;color:white;font-size:18px;flex-shrink:0;">2</div>
          <div style="font-size:15px;font-weight:700;color:var(--purple-deep);">📍 巡礼して記録する</div>
        </div>
        <div style="font-size:13px;color:var(--text-mid);line-height:1.7;">実際に訪れたら「巡礼した！」ボタンで記録。評価・写真投稿でポイントを獲得できます。</div>
      </div>

      <div style="background:white;border-radius:18px;padding:20px;border:1px solid var(--border);box-shadow:0 2px 10px rgba(61,26,94,0.06);">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;">
          <div style="width:36px;height:36px;background:linear-gradient(135deg,var(--purple-deep),var(--red));border-radius:10px;display:flex;align-items:center;justify-content:center;color:white;font-size:18px;flex-shrink:0;">3</div>
          <div style="font-size:15px;font-weight:700;color:var(--purple-deep);">🏅 ポイントを貯めてランクアップ</div>
        </div>
        <div style="font-size:13px;color:var(--text-mid);line-height:1.7;">誰よりも早く登録すれば発見者として名前が残る。推しメン別ランキングで日本一を目指せ。</div>
      </div>

    </div>
    <div style="padding-bottom:40px;"></div>
  </div>

  <!-- ROUTE VIEW -->'''

content = content.replace(old2, new2)

with open('trace-ive.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ 完了')

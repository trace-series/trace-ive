with open('trace-ive.html', 'r', encoding='utf-8') as f:
    content = f.read()

changes = []

# 1. オンボーディング：Xマーク削除
old = '          𝕏 Xアカウントで始める <span style="font-size:11px;background:rgba(0,0,0,0.15);padding:3px 8px;border-radius:20px;">おすすめ</span>'
new = '          Xアカウントで始める <span style="font-size:11px;background:rgba(0,0,0,0.15);padding:3px 8px;border-radius:20px;">おすすめ</span>'
if old in content: content = content.replace(old, new, 1); changes.append('1. オンボーディング Xマーク削除')

# 2. 近日公開ブロック削除
old = '''        <div style="background:rgba(201,168,76,0.15);border:1px solid rgba(201,168,76,0.4);border-radius:14px;padding:16px;display:flex;gap:14px;align-items:flex-start;">
          <div style="font-size:24px;flex-shrink:0;">🚀</div>
          <div>
            <div style="font-size:14px;font-weight:700;color:#c9a84c;margin-bottom:4px;">近日公開：#TraceIVEでポイント獲得</div>
            <div style="font-size:12px;color:rgba(255,255,255,0.65);line-height:1.6;">Xのポストにタグをつけるだけでポイントがもらえるようになります</div>
          </div>
        </div>'''
if old in content: content = content.replace(old, '', 1); changes.append('2. 近日公開ブロック削除')

# 3. 年号2026
for old, new in [
    ('© 2025 missing link / Trace IVE · All rights reserved.', '© 2026 missing link / Trace IVE · All rights reserved.'),
    ('© 2025 missing link / Trace IVE\n    </div>', '© 2026 missing link / Trace IVE\n    </div>'),
    ('最終更新日：2025年6月1日', '最終更新日：2026年6月1日'),
]:
    if old in content: content = content.replace(old, new); changes.append('3. 年号2026')

# 4. お問い合わせ先変更
old = '<a href="https://x.com/missing_link" style="color:var(--purple-deep);">@missing_link</a>（X/Twitter）'
new = '<a href="https://x.com/traceIVE4179" style="color:var(--purple-deep);">@traceIVE4179</a>（X/Twitter）'
count = content.count(old)
if count: content = content.replace(old, new); changes.append(f'4. お問い合わせ先変更（{count}箇所）')

# 5. ランキングダミー削除
old = '''    <div class="ranking-list" id="ranking-list">
      <div class="ranking-item" onclick="jumpToSpot('東京ドーム')" data-member="IVE">
        <div class="rank-num rank-1">1</div>
        <div class="rank-thumb">🎤</div>
        <div class="rank-info">
          <div class="rank-name">東京ドーム</div>
          <div class="rank-meta">東京都文京区 · SHOW WHAT I HAVE</div>
          <span style="display:inline-block;margin-top:3px;padding:2px 8px;background:var(--purple-pale);color:var(--purple-deep);border-radius:10px;font-size:11px;font-weight:700;">IVE</span>
        </div>
        <div class="rank-score">
          <div class="rank-score-num">0</div>
          <div class="rank-score-label">巡礼数</div>
        </div>
      </div>
      <div class="ranking-item" onclick="jumpToSpot('MIYASHITA PARK')" data-member="レイ">
        <div class="rank-num rank-2">2</div>
        <div class="rank-thumb">📸</div>
        <div class="rank-info">
          <div class="rank-name">MIYASHITA PARK</div>
          <div class="rank-meta">東京都渋谷区 · REBEL HEART MV</div>
          <span style="display:inline-block;margin-top:3px;padding:2px 8px;background:var(--purple-pale);color:var(--purple-deep);border-radius:10px;font-size:11px;font-weight:700;">レイ</span>
        </div>
        <div class="rank-score">
          <div class="rank-score-num">0</div>
          <div class="rank-score-label">巡礼数</div>
        </div>
      </div>
      <div class="ranking-item" onclick="jumpToSpot('渋谷駅前交差点')" data-member="レイ">
        <div class="rank-num rank-3">3</div>
        <div class="rank-thumb">📸</div>
        <div class="rank-info">
          <div class="rank-name">渋谷駅前交差点</div>
          <div class="rank-meta">東京都渋谷区 · REBEL HEART MV</div>
          <span style="display:inline-block;margin-top:3px;padding:2px 8px;background:var(--purple-pale);color:var(--purple-deep);border-radius:10px;font-size:11px;font-weight:700;">レイ</span>
        </div>
        <div class="rank-score">
          <div class="rank-score-num">0</div>
          <div class="rank-score-label">巡礼数</div>
        </div>
      </div>
      <div class="ranking-item" onclick="jumpToSpot('東京ディズニーシー')" data-member="ガウル">
        <div class="rank-num rank-other">4</div>
        <div class="rank-thumb">🏯</div>
        <div class="rank-info">
          <div class="rank-name">東京ディズニーシー</div>
          <div class="rank-meta">千葉県浦安市 · 来日観光</div>
          <span style="display:inline-block;margin-top:3px;padding:2px 8px;background:var(--purple-pale);color:var(--purple-deep);border-radius:10px;font-size:11px;font-weight:700;">ガウル</span>
        </div>
        <div class="rank-score">
          <div class="rank-score-num">0</div>
          <div class="rank-score-label">巡礼数</div>
        </div>
      </div>
      <div class="ranking-item" onclick="jumpToSpot('before sunset')" data-member="アン・ユジン">
        <div class="rank-num rank-other">5</div>
        <div class="rank-thumb">☕</div>
        <div class="rank-info">
          <div class="rank-name">before sunset</div>
          <div class="rank-meta">神奈川県葉山町 · 相席食堂</div>
          <span style="display:inline-block;margin-top:3px;padding:2px 8px;background:var(--purple-pale);color:var(--purple-deep);border-radius:10px;font-size:11px;font-weight:700;">アン・ユジン</span>
        </div>
        <div class="rank-score">
          <div class="rank-score-num">0</div>
          <div class="rank-score-label">巡礼数</div>
        </div>
      </div>
      <div class="ranking-item" onclick="jumpToSpot('名古屋城')" data-member="レイ">
        <div class="rank-num rank-other">6</div>
        <div class="rank-thumb">🏯</div>
        <div class="rank-info">
          <div class="rank-name">名古屋城</div>
          <div class="rank-meta">愛知県名古屋市 · レイYouTube</div>
          <span style="display:inline-block;margin-top:3px;padding:2px 8px;background:var(--purple-pale);color:var(--purple-deep);border-radius:10px;font-size:11px;font-weight:700;">レイ</span>
        </div>
        <div class="rank-score">
          <div class="rank-score-num">0</div>
          <div class="rank-score-label">巡礼数</div>
        </div>
      </div>
    </div>'''
new = '''    <div class="ranking-list" id="ranking-list">
      <div style="text-align:center;padding:40px 20px;color:var(--text-light);">
        <div style="font-size:32px;margin-bottom:8px;">🗺️</div>
        <div style="font-size:14px;">巡礼報告が集まるとランキングが表示されます</div>
      </div>
    </div>'''
if old in content: content = content.replace(old, new, 1); changes.append('5. ランキングダミー削除')

# 6. タイムラインダミー削除
old = '''    <div class="feed-list">
      <div class="feed-item" data-member="ガウル">
        <div class="feed-header">
          <div class="feed-avatar">🌸</div>
          <div class="feed-user">
            <div class="feed-username">@yuna_dive
              <span class="feed-founder">🥇 創設メンバー #3</span>
            </div>
            <div class="feed-time">2時間前</div>
          </div>
        </div>
        <div class="feed-img">
          🎵
          <div class="feed-img-overlay">📍 渋谷スクランブル交差点</div>
        </div>
        <div class="feed-body">
          <div class="feed-spot-name">渋谷スクランブル交差点</div>
          <div class="feed-comment">WAVEのMVと同じ構図で撮れました！夜がおすすめ。ガウルが立っていた場所の特定成功🎉</div>
          <div class="card-badges" style="margin-bottom:10px;">
            <span class="badge badge-red">WAVE MV</span>
            <span class="badge badge-purple">東京</span>
            <span class="badge badge-gold">ガウル</span>
          </div>
          <div class="feed-footer">
            <div class="feed-action liked">❤️ 48</div>
            <div class="feed-action">💬 12</div>
            <div class="feed-action">🔖 保存</div>
            <button class="feed-share">𝕏 シェア</button>
          </div>
        </div>
      </div>

      <div class="feed-item" data-member="レイ">
        <div class="feed-header">
          <div class="feed-avatar">💜</div>
          <div class="feed-user">
            <div class="feed-username">@ive_rei_love</div>
            <div class="feed-time">5時間前</div>
          </div>
        </div>
        <div class="feed-img" style="background:linear-gradient(135deg,#f0e0e8,#e8d0f0);">
          📚
          <div class="feed-img-overlay">📍 代官山 蔦屋書店</div>
        </div>
        <div class="feed-body">
          <div class="feed-spot-name">代官山 蔦屋書店</div>
          <div class="feed-comment">来日の際にレイが訪れたとされる場所。同じ本を探したら見つかりました📖</div>
          <div class="card-badges" style="margin-bottom:10px;">
            <span class="badge badge-purple">来日</span>
            <span class="badge badge-gold">レイ</span>
          </div>
          <div class="feed-footer">
            <div class="feed-action liked">❤️ 31</div>
            <div class="feed-action">💬 7</div>
            <div class="feed-action">🔖 保存</div>
            <button class="feed-share">𝕏 シェア</button>
          </div>
        </div>
      </div>
    </div>'''
new = '''    <div class="feed-list" id="feed-list">
      <div style="text-align:center;padding:40px 20px;color:var(--text-light);">
        <div style="font-size:32px;margin-bottom:8px;">📸</div>
        <div style="font-size:14px;">巡礼報告が投稿されると表示されます</div>
      </div>
    </div>'''
if old in content: content = content.replace(old, new, 1); changes.append('6. タイムラインダミー削除')

# 7. 創設メンバー 0/20・プログレス0%
old = '      <div class="founder-count">7 / 20 名 参加済み</div>'
new = '      <div class="founder-count" id="founder-count">0 / 20 名 参加済み</div>'
if old in content: content = content.replace(old, new); changes.append('7. 創設メンバー0/20')
old = '<div class="founder-progress-bar"></div>'
new = '<div class="founder-progress-bar" id="founder-progress-bar" style="width:0%"></div>'
if old in content: content = content.replace(old, new); changes.append('7b. プログレス0%')

# 8. プロフィールのダミーデータをゼロに
for old, new in [
    ('      <div class="contrib-total" id="profile-contrib-total">347 pt</div>',
     '      <div class="contrib-total" id="profile-contrib-total">0 pt</div>'),
    ('        <div class="contrib-rank-badge">🏆 上位 12%</div>',
     '        <div class="contrib-rank-badge" id="contrib-rank-badge">—</div>'),
    ('        <div class="contrib-bar-fill" style="width:62%"></div>',
     '        <div class="contrib-bar-fill" id="contrib-bar-fill" style="width:0%"></div>'),
    ('      <div class="contrib-next">次のランク「ゴールド」まで あと 153pt</div>',
     '      <div class="contrib-next" id="contrib-next">ポイントを貯めてランクアップしよう</div>'),
    ('          <span class="contrib-item-val">+180pt</span>\n        </div>\n        <div class="contrib-item">\n          <span class="contrib-item-icon">🔍</span>\n          <span class="contrib-item-label">早期発見</span>\n          <span class="contrib-item-val">+120pt</span>\n        </div>\n        <div class="contrib-item">\n          <span class="contrib-item-icon">⚡</span>\n          <span class="contrib-item-label">スピード報告</span>\n          <span class="contrib-item-val">+47pt</span>',
     '          <span class="contrib-item-val" id="contrib-accurate">0pt</span>\n        </div>\n        <div class="contrib-item">\n          <span class="contrib-item-icon">🔍</span>\n          <span class="contrib-item-label">早期発見</span>\n          <span class="contrib-item-val" id="contrib-early">0pt</span>\n        </div>\n        <div class="contrib-item">\n          <span class="contrib-item-icon">⚡</span>\n          <span class="contrib-item-label">スピード報告</span>\n          <span class="contrib-item-val" id="contrib-speed">0pt</span>'),
]:
    if old in content: content = content.replace(old, new); changes.append('8. プロフィールダミー数値→0')

# 9. スタッツ行のダミー数字→0
for old, new in [
    ('<div class="stat-num">7</div>\n        <div class="stat-label">投稿スポット</div>',
     '<div class="stat-num" id="stat-spots">0</div>\n        <div class="stat-label">投稿スポット</div>'),
    ('<div class="stat-num">23</div>\n        <div class="stat-label">巡礼済み</div>',
     '<div class="stat-num" id="stat-pilgrim">0</div>\n        <div class="stat-label">巡礼済み</div>'),
    ('<div class="stat-num">312</div>\n        <div class="stat-label">獲得いいね</div>',
     '<div class="stat-num" id="stat-likes">0</div>\n        <div class="stat-label">獲得いいね</div>'),
    ('<div class="stat-num">4</div>\n        <div class="stat-label">発見者バッジ</div>',
     '<div class="stat-num" id="stat-discoverer">0</div>\n        <div class="stat-label">発見者バッジ</div>'),
]:
    if old in content: content = content.replace(old, new); changes.append('9. スタッツ数字→0')

# 10. 確定待ちポイントのダミー削除
old = '''      <div class="pending-list" id="pending-list">
        <div class="pending-item">
          <div class="pending-item-left">
            <div class="pending-item-name">新大久保 コリアタウン</div>
            <div class="pending-item-type">❌ 場所が違うと報告</div>
          </div>
          <div class="pending-item-pt">+40pt?</div>
        </div>
        <div class="pending-item">
          <div class="pending-item-left">
            <div class="pending-item-name">中目黒 川沿い</div>
            <div class="pending-item-type">📸 行って確認と報告</div>
          </div>
          <div class="pending-item-pt">+30pt?</div>
        </div>
      </div>'''
new = '''      <div class="pending-list" id="pending-list">
        <div style="text-align:center;padding:16px;color:var(--text-light);font-size:12px;">確定待ちのポイントはありません</div>
      </div>'''
if old in content: content = content.replace(old, new, 1); changes.append('10. 確定待ちダミー削除')

# 11. 投稿したスポットのダミー削除
old = '''    <div class="my-spots-list">
      <div class="my-spot-item">
        <div class="my-spot-icon">🎵</div>
        <div class="my-spot-info">
          <div class="my-spot-name">渋谷スクランブル交差点</div>
          <div class="my-spot-meta">WAVE MV · 東京</div>
        </div>
        <div class="my-spot-right">
          <div class="my-spot-likes">❤️ 128</div>
          <div class="my-spot-date">3日前</div>
        </div>
      </div>
      <div class="my-spot-item">
        <div class="my-spot-icon">📚</div>
        <div class="my-spot-info">
          <div class="my-spot-name">代官山 蔦屋書店</div>
          <div class="my-spot-meta">来日スポット · 東京</div>
        </div>
        <div class="my-spot-right">
          <div class="my-spot-likes">❤️ 94</div>
          <div class="my-spot-date">1週間前</div>
        </div>
      </div>
    </div>'''
new = '''    <div class="my-spots-list" id="my-spots-list">
      <div style="text-align:center;padding:20px;color:var(--text-light);font-size:12px;">投稿したスポットはまだありません</div>
    </div>'''
if old in content: content = content.replace(old, new, 1); changes.append('11. 投稿スポットダミー削除')

# 12. プロフィールヘッダーのダミー名前・バッジを空に
old = '''      <div class="profile-avatar-wrap">
        <div class="profile-avatar-img">🌸</div>
        <div class="profile-name-block">
          <div class="profile-name">yuna_dive</div>
          <div class="profile-handle">@yuna_dive · Chiba, JP</div>
        </div>
        <button class="profile-edit-btn">編集</button>
      </div>
      <div class="profile-badges-row">
        <span class="profile-badge pbadge-founder">🥇 創設メンバー #3</span>
        <span class="profile-badge pbadge-discoverer">🔍 発見者 ×4</span>
        <span class="profile-badge pbadge-discoverer">💜 DIVE</span>
      </div>'''
new = '''      <div class="profile-avatar-wrap">
        <div class="profile-avatar-img" id="profile-avatar">👤</div>
        <div class="profile-name-block">
          <div class="profile-name" id="profile-name">匿名ユーザー</div>
          <div class="profile-handle" id="profile-handle">X未連携</div>
        </div>
        <button class="profile-edit-btn" onclick="openProfileEdit()">編集</button>
      </div>
      <div class="profile-badges-row" id="profile-badges-row">
      </div>'''
if old in content: content = content.replace(old, new, 1); changes.append('12. プロフィールダミー名前・バッジ削除')

# 13. X連携カードのダミーを未連携状態に
old = '''    <div class="x-connect-card">
      <div style="width:40px;height:40px;background:white;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:20px;font-weight:900;font-family:sans-serif;flex-shrink:0;">𝕏</div>
      <div class="x-connect-text">
        <div class="x-connect-title">Xアカウント連携済み</div>
        <div class="x-connect-sub">@yuna_dive · 1タップでシェア可能</div>
      </div>
      <div class="x-connect-arrow">›</div>
    </div>'''
new = '''    <div class="x-connect-card" onclick="startXConnect()">
      <div style="width:40px;height:40px;background:white;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:20px;font-weight:900;font-family:sans-serif;flex-shrink:0;">𝕏</div>
      <div class="x-connect-text">
        <div class="x-connect-title" id="x-connect-title">Xアカウントを連携する</div>
        <div class="x-connect-sub" id="x-connect-sub">連携するとポイントや発見者クレジットが保持されます</div>
      </div>
      <div class="x-connect-arrow">›</div>
    </div>'''
if old in content: content = content.replace(old, new, 1); changes.append('13. X連携カード→未連携状態')

# 14. X投稿時メンバーハッシュタグ追加
old = '''  members: [
    { name: 'ユジン',    nameEn: 'YUJIN',     birthday: { month: 9,  day: 1  }, hashtag: 'HAPPY_YUJIN_DAY'    },
    { name: 'ガウル',    nameEn: 'GAEUL',     birthday: { month: 9,  day: 24 }, hashtag: 'HAPPY_GAEUL_DAY'    },
    { name: 'レイ',      nameEn: 'REI',       birthday: { month: 2,  day: 3  }, hashtag: 'HAPPY_REI_DAY'      },
    { name: 'ウォニョン', nameEn: 'WONYOUNG',  birthday: { month: 8,  day: 31 }, hashtag: 'HAPPY_WONYOUNG_DAY' },
    { name: 'リズ',      nameEn: 'LIZ',       birthday: { month: 11, day: 21 }, hashtag: 'HAPPY_LIZ_DAY'      },
    { name: 'イソ',      nameEn: 'LEESEO',    birthday: { month: 2,  day: 21 }, hashtag: 'HAPPY_LEESEO_DAY'   },
  ],'''
new = '''  members: [
    { name: 'ユジン',    nameEn: 'YUJIN',     birthday: { month: 9,  day: 1  }, hashtag: 'HAPPY_YUJIN_DAY',    tags: ['#ユジン', '#YUJIN', '#안유진'] },
    { name: 'ガウル',    nameEn: 'GAEUL',     birthday: { month: 9,  day: 24 }, hashtag: 'HAPPY_GAEUL_DAY',    tags: ['#ガウル', '#GAEUL', '#김가을'] },
    { name: 'レイ',      nameEn: 'REI',       birthday: { month: 2,  day: 3  }, hashtag: 'HAPPY_REI_DAY',      tags: ['#レイ', '#REI', '#나오이레이'] },
    { name: 'ウォニョン', nameEn: 'WONYOUNG',  birthday: { month: 8,  day: 31 }, hashtag: 'HAPPY_WONYOUNG_DAY', tags: ['#ウォニョン', '#WONYOUNG', '#장원영'] },
    { name: 'リズ',      nameEn: 'LIZ',       birthday: { month: 11, day: 21 }, hashtag: 'HAPPY_LIZ_DAY',      tags: ['#リズ', '#LIZ', '#김지원'] },
    { name: 'イソ',      nameEn: 'LEESEO',    birthday: { month: 2,  day: 21 }, hashtag: 'HAPPY_LEESEO_DAY',   tags: ['#イソ', '#LEESEO', '#이서'] },
  ],'''
if old in content: content = content.replace(old, new, 1); changes.append('14. メンバーハッシュタグ（日英韓）追加')

# 15. shareX関数にメンバータグを追加
old = '''function shareX() {
  if (!currentSpot) return;
  const tags = GROUP_CONFIG.hashtags.join(' ');
  const text = encodeURIComponent(`【聖地巡礼】${currentSpot.name}\n${currentSpot.sub}\n\n${tags}`);
  window.open(`https://twitter.com/intent/tweet?text=${text}`, '_blank');
}'''
new = '''function shareX() {
  if (!currentSpot) return;
  const baseTags = GROUP_CONFIG.hashtags.join(' ');
  let memberTags = '';
  if (currentSpot.member && currentSpot.member !== 'IVE') {
    const memberConfig = GROUP_CONFIG.members.find(m => m.name === currentSpot.member || m.nameEn === currentSpot.member);
    if (memberConfig && memberConfig.tags) memberTags = ' ' + memberConfig.tags.join(' ');
  }
  const text = encodeURIComponent(`【聖地巡礼】${currentSpot.name}\n${currentSpot.sub}\n\n${baseTags}${memberTags}`);
  window.open(`https://twitter.com/intent/tweet?text=${text}`, '_blank');
}

// X連携フロー
function startXConnect() {
  const ob = JSON.parse(localStorage.getItem(OB_KEY) || 'null');
  if (ob && ob.method === 'x') {
    alert('✅ すでにXアカウントで登録済みです。');
    return;
  }
  if (confirm('Xアカウントで始めますか？\n\n連携するとポイントや発見者クレジットが端末をまたいで保持されます。')) {
    startWithX();
  }
}

// プロフィール編集（今後実装用のスタブ）
function openProfileEdit() {
  alert('プロフィール編集機能は近日公開予定です。');
}'''
if old in content: content = content.replace(old, new, 1); changes.append('15. shareX メンバータグ + X連携ボタン追加')

# 16. 管理者モーダル内の誤字 "c" を削除
old = '  </div>c\n</div>\n\n<!-- 管理者ログインモーダル -->'
new = '  </div>\n</div>\n\n<!-- 管理者ログインモーダル -->'
if old in content: content = content.replace(old, new, 1); changes.append('16. 管理者モーダル誤字修正')

with open('trace-ive.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ 修正完了')
for c in changes:
    print(f'  ✓ {c}')
print(f'\n合計 {len(changes)} 件修正')
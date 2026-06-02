with open('trace-ive.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. オンボーディング：ページ1のXボタンからXマーク文字を削除
content = content.replace(
    '          𝕏 Xアカウントで始める <span style="font-size:11px;background:rgba(0,0,0,0.15);padding:3px 8px;border-radius:20px;">おすすめ</span>',
    '          Xアカウントで始める <span style="font-size:11px;background:rgba(0,0,0,0.15);padding:3px 8px;border-radius:20px;">おすすめ</span>'
)

# 2. オンボーディング：近日公開ブロック削除
old_soon = '''        <div style="background:rgba(201,168,76,0.15);border:1px solid rgba(201,168,76,0.4);border-radius:14px;padding:16px;display:flex;gap:14px;align-items:flex-start;">
          <div style="font-size:24px;flex-shrink:0;">🚀</div>
          <div>
            <div style="font-size:14px;font-weight:700;color:#c9a84c;margin-bottom:4px;">近日公開：#TraceIVEでポイント獲得</div>
            <div style="font-size:12px;color:rgba(255,255,255,0.65);line-height:1.6;">Xのポストにタグをつけるだけでポイントがもらえるようになります</div>
          </div>
        </div>'''
content = content.replace(old_soon, '')

# 3. スポット削除：寺カフェ代官山（SPOTSリストにないが念のため検索）
# → ファイル確認済み・存在しないためスキップ

# 4. フッター年号 2025→2026（全箇所）
content = content.replace('© 2025 missing link / Trace IVE · All rights reserved.', '© 2026 missing link / Trace IVE · All rights reserved.')
content = content.replace('© 2025 missing link / Trace IVE', '© 2026 missing link / Trace IVE')
content = content.replace('最終更新日：2025年6月1日', '最終更新日：2026年6月1日')

# 5. お問い合わせ先：@missing_link → @traceIVE4179（利用規約・プライバシー）
content = content.replace(
    '<a href="https://x.com/missing_link" style="color:var(--purple-deep);">@missing_link</a>（X/Twitter）',
    '<a href="https://x.com/traceIVE4179" style="color:var(--purple-deep);">@traceIVE4179</a>（X/Twitter）'
)

# 6. ランキングリスト：ダミー6件を削除してDBから動的生成に切り替え（空にする）
old_ranking = '''    <div class="ranking-list" id="ranking-list">
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

new_ranking = '''    <div class="ranking-list" id="ranking-list">
      <div style="text-align:center;padding:40px 20px;color:var(--text-light);">
        <div style="font-size:32px;margin-bottom:8px;">🗺️</div>
        <div style="font-size:14px;">巡礼報告が集まるとランキングが表示されます</div>
      </div>
    </div>'''

content = content.replace(old_ranking, new_ranking)

# 7. タイムライン：ダミー投稿を削除
old_feed = '''    <div class="feed-list">
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

new_feed = '''    <div class="feed-list" id="feed-list">
      <div style="text-align:center;padding:40px 20px;color:var(--text-light);">
        <div style="font-size:32px;margin-bottom:8px;">📸</div>
        <div style="font-size:14px;">巡礼報告が投稿されると表示されます</div>
      </div>
    </div>'''

content = content.replace(old_feed, new_feed)

# 8. 創設メンバー：7/20→0/20、プログレスバーを0%に
content = content.replace('      <div class="founder-count">7 / 20 名 参加済み</div>', '      <div class="founder-count" id="founder-count">0 / 20 名 参加済み</div>')
content = content.replace('<div class="founder-progress-bar"></div>', '<div class="founder-progress-bar" id="founder-progress-bar" style="width:0%"></div>')

# 9. X投稿時のメンバーハッシュタグ追加
# メンバーごとのハッシュタグ定義をGROUP_CONFIGに追加
old_members = '''  members: [
    { name: 'ユジン',    nameEn: 'YUJIN',     birthday: { month: 9,  day: 1  }, hashtag: 'HAPPY_YUJIN_DAY'    },
    { name: 'ガウル',    nameEn: 'GAEUL',     birthday: { month: 9,  day: 24 }, hashtag: 'HAPPY_GAEUL_DAY'    },
    { name: 'レイ',      nameEn: 'REI',       birthday: { month: 2,  day: 3  }, hashtag: 'HAPPY_REI_DAY'      },
    { name: 'ウォニョン', nameEn: 'WONYOUNG',  birthday: { month: 8,  day: 31 }, hashtag: 'HAPPY_WONYOUNG_DAY' },
    { name: 'リズ',      nameEn: 'LIZ',       birthday: { month: 11, day: 21 }, hashtag: 'HAPPY_LIZ_DAY'      },
    { name: 'イソ',      nameEn: 'LEESEO',    birthday: { month: 2,  day: 21 }, hashtag: 'HAPPY_LEESEO_DAY'   },
  ],'''

new_members = '''  members: [
    { name: 'ユジン',    nameEn: 'YUJIN',     birthday: { month: 9,  day: 1  }, hashtag: 'HAPPY_YUJIN_DAY',    tags: ['#ユジン', '#YUJIN', '#안유진'] },
    { name: 'ガウル',    nameEn: 'GAEUL',     birthday: { month: 9,  day: 24 }, hashtag: 'HAPPY_GAEUL_DAY',    tags: ['#ガウル', '#GAEUL', '#김가을'] },
    { name: 'レイ',      nameEn: 'REI',       birthday: { month: 2,  day: 3  }, hashtag: 'HAPPY_REI_DAY',      tags: ['#レイ', '#REI', '#나오이레이'] },
    { name: 'ウォニョン', nameEn: 'WONYOUNG',  birthday: { month: 8,  day: 31 }, hashtag: 'HAPPY_WONYOUNG_DAY', tags: ['#ウォニョン', '#WONYOUNG', '#장원영'] },
    { name: 'リズ',      nameEn: 'LIZ',       birthday: { month: 11, day: 21 }, hashtag: 'HAPPY_LIZ_DAY',      tags: ['#リズ', '#LIZ', '#김지원'] },
    { name: 'イソ',      nameEn: 'LEESEO',    birthday: { month: 2,  day: 21 }, hashtag: 'HAPPY_LEESEO_DAY',   tags: ['#イソ', '#LEESEO', '#이서'] },
  ],'''

content = content.replace(old_members, new_members)

# shareX関数にメンバータグを追加
old_sharex = '''function shareX() {
  if (!currentSpot) return;
  const tags = GROUP_CONFIG.hashtags.join(' ');
  const text = encodeURIComponent(`【聖地巡礼】${currentSpot.name}\n${currentSpot.sub}\n\n${tags}`);
  window.open(`https://twitter.com/intent/tweet?text=${text}`, '_blank');
}'''

new_sharex = '''function shareX() {
  if (!currentSpot) return;
  const baseTags = GROUP_CONFIG.hashtags.join(' ');
  // メンバータグを追加
  let memberTags = '';
  if (currentSpot.member && currentSpot.member !== 'IVE') {
    const memberConfig = GROUP_CONFIG.members.find(m => m.name === currentSpot.member || m.nameEn === currentSpot.member);
    if (memberConfig && memberConfig.tags) {
      memberTags = ' ' + memberConfig.tags.join(' ');
    }
  }
  const text = encodeURIComponent(`【聖地巡礼】${currentSpot.name}\n${currentSpot.sub}\n\n${baseTags}${memberTags}`);
  window.open(`https://twitter.com/intent/tweet?text=${text}`, '_blank');
}'''

content = content.replace(old_sharex, new_sharex)

# プロフィール画面のダミーデータをゼロに
content = content.replace(
    '      <div class="founder-count">7 / 20 名 参加済み</div>',
    '      <div class="founder-count" id="founder-count">0 / 20 名 参加済み</div>'
)

with open('trace-ive.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ 表示・テキスト修正完了")
print("  1. オンボーディング Xマーク削除")
print("  2. 近日公開ブロック削除")
print("  3. 年号2026に更新")
print("  4. お問い合わせ先 @traceIVE4179に変更")
print("  5. ランキングダミー削除")
print("  6. タイムラインダミー削除")
print("  7. 創設メンバー 0/20に修正")
print("  8. Xシェア時メンバーハッシュタグ追加（日英韓）")
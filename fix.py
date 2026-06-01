with open('trace-ive.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 利用規約ビューを追加
old = '  <!-- POINT RULES VIEW -->'
new = '''  <!-- TERMS VIEW -->
  <div id="view-terms" style="display:none;padding:20px 16px;">
    <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px;">
      <button onclick="history.back()" style="background:var(--purple-pale);border:none;border-radius:10px;padding:6px 12px;font-size:13px;cursor:pointer;color:var(--purple-deep);">← 戻る</button>
      <div class="section-title" style="margin-bottom:0;">利用規約</div>
    </div>
    <div class="section-sub">TERMS OF SERVICE</div>
    <div style="font-size:12px;color:var(--text-light);margin-bottom:20px;">最終更新日：2025年6月1日</div>

    <div style="display:flex;flex-direction:column;gap:20px;padding-bottom:40px;">

      <div style="background:white;border-radius:14px;padding:16px;border:1px solid var(--border);">
        <div style="font-size:14px;font-weight:700;color:var(--purple-deep);margin-bottom:8px;">第1条（本サービスについて）</div>
        <div style="font-size:13px;color:var(--text-mid);line-height:1.8;">Trace IVEは、IVEゆかりの場所（聖地）に関する情報をファン同士で共有・記録するための非公式ファンアプリです。本サービスはSTARSHIP ENTERTAINMENT及びIVEとは一切関係ありません。</div>
      </div>

      <div style="background:white;border-radius:14px;padding:16px;border:1px solid var(--border);">
        <div style="font-size:14px;font-weight:700;color:var(--purple-deep);margin-bottom:8px;">第2条（利用条件）</div>
        <div style="font-size:13px;color:var(--text-mid);line-height:1.8;">本サービスを利用するにあたり、以下の条件に同意いただく必要があります。<br><br>
        ・本サービスを合法的な目的のみに使用すること<br>
        ・他のユーザーや第三者の権利を侵害しないこと<br>
        ・虚偽の情報を投稿しないこと<br>
        ・スパムや嫌がらせ行為を行わないこと<br>
        ・アーティストや関係者のプライバシーを尊重すること</div>
      </div>

      <div style="background:white;border-radius:14px;padding:16px;border:1px solid var(--border);">
        <div style="font-size:14px;font-weight:700;color:var(--purple-deep);margin-bottom:8px;">第3条（投稿コンテンツ）</div>
        <div style="font-size:13px;color:var(--text-mid);line-height:1.8;">ユーザーが投稿したスポット情報は、Trace IVEのデータベースに登録されます。投稿者には「発見者」クレジットが永続的に付与されます。運営は不適切な投稿を削除・修正する権限を持ちます。</div>
      </div>

      <div style="background:white;border-radius:14px;padding:16px;border:1px solid var(--border);">
        <div style="font-size:14px;font-weight:700;color:var(--purple-deep);margin-bottom:8px;">第4条（免責事項）</div>
        <div style="font-size:13px;color:var(--text-mid);line-height:1.8;">掲載情報はファンによる投稿・調査に基づくものであり、正確性を保証するものではありません。情報の利用・訪問により生じたいかなる損害についても責任を負いかねます。</div>
      </div>

      <div style="background:white;border-radius:14px;padding:16px;border:1px solid var(--border);">
        <div style="font-size:14px;font-weight:700;color:var(--purple-deep);margin-bottom:8px;">第5条（禁止事項）</div>
        <div style="font-size:13px;color:var(--text-mid);line-height:1.8;">以下の行為を禁止します。<br><br>
        ・本サービスのコンテンツ・デザイン・システムの無断転用<br>
        ・商用目的での利用<br>
        ・自動化ツールによる大量アクセス<br>
        ・他ユーザーへの嫌がらせ・なりすまし<br>
        ・虚偽の評価・スパム投稿</div>
      </div>

      <div style="background:white;border-radius:14px;padding:16px;border:1px solid var(--border);">
        <div style="font-size:14px;font-weight:700;color:var(--purple-deep);margin-bottom:8px;">第6条（サービスの変更・終了）</div>
        <div style="font-size:13px;color:var(--text-mid);line-height:1.8;">運営は予告なくサービス内容の変更・終了を行う場合があります。これにより生じた損害について責任を負いかねます。</div>
      </div>

      <div style="background:var(--purple-pale);border-radius:14px;padding:16px;">
        <div style="font-size:12px;color:var(--text-mid);line-height:1.8;">お問い合わせ：<a href="https://x.com/missing_link" style="color:var(--purple-deep);">@missing_link</a>（X/Twitter）</div>
      </div>

    </div>
  </div>

  <!-- PRIVACY VIEW -->
  <div id="view-privacy" style="display:none;padding:20px 16px;">
    <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px;">
      <button onclick="history.back()" style="background:var(--purple-pale);border:none;border-radius:10px;padding:6px 12px;font-size:13px;cursor:pointer;color:var(--purple-deep);">← 戻る</button>
      <div class="section-title" style="margin-bottom:0;">プライバシーポリシー</div>
    </div>
    <div class="section-sub">PRIVACY POLICY</div>
    <div style="font-size:12px;color:var(--text-light);margin-bottom:20px;">最終更新日：2025年6月1日</div>

    <div style="display:flex;flex-direction:column;gap:20px;padding-bottom:40px;">

      <div style="background:white;border-radius:14px;padding:16px;border:1px solid var(--border);">
        <div style="font-size:14px;font-weight:700;color:var(--purple-deep);margin-bottom:8px;">収集する情報</div>
        <div style="font-size:13px;color:var(--text-mid);line-height:1.8;">本サービスでは以下の情報を収集する場合があります。<br><br>
        ・投稿されたスポット情報（スポット名・住所・説明・カテゴリー）<br>
        ・評価・巡礼報告データ<br>
        ・X連携時のユーザー名（任意）<br>
        ・端末のlocalStorageに保存される設定情報</div>
      </div>

      <div style="background:white;border-radius:14px;padding:16px;border:1px solid var(--border);">
        <div style="font-size:14px;font-weight:700;color:var(--purple-deep);margin-bottom:8px;">情報の利用目的</div>
        <div style="font-size:13px;color:var(--text-mid);line-height:1.8;">収集した情報は以下の目的で使用します。<br><br>
        ・聖地情報の提供・管理<br>
        ・ポイント・ランキングシステムの運営<br>
        ・サービスの改善・不正利用の防止</div>
      </div>

      <div style="background:white;border-radius:14px;padding:16px;border:1px solid var(--border);">
        <div style="font-size:14px;font-weight:700;color:var(--purple-deep);margin-bottom:8px;">第三者への提供</div>
        <div style="font-size:13px;color:var(--text-mid);line-height:1.8;">収集した個人情報を第三者に販売・提供することはありません。ただし法令に基づく場合を除きます。</div>
      </div>

      <div style="background:white;border-radius:14px;padding:16px;border:1px solid var(--border);">
        <div style="font-size:14px;font-weight:700;color:var(--purple-deep);margin-bottom:8px;">使用技術</div>
        <div style="font-size:13px;color:var(--text-mid);line-height:1.8;">本サービスはSupabase（データベース）、Google Maps API（地図表示）、GitHub Pages（ホスティング）を使用しています。各サービスのプライバシーポリシーもご確認ください。</div>
      </div>

      <div style="background:white;border-radius:14px;padding:16px;border:1px solid var(--border);">
        <div style="font-size:14px;font-weight:700;color:var(--purple-deep);margin-bottom:8px;">localStorageについて</div>
        <div style="font-size:13px;color:var(--text-mid);line-height:1.8;">本サービスはブラウザのlocalStorageを使用して、ポイント・設定・評価履歴を端末に保存します。サーバーには送信されません。ブラウザの設定から削除可能です。</div>
      </div>

      <div style="background:var(--purple-pale);border-radius:14px;padding:16px;">
        <div style="font-size:12px;color:var(--text-mid);line-height:1.8;">お問い合わせ：<a href="https://x.com/missing_link" style="color:var(--purple-deep);">@missing_link</a>（X/Twitter）</div>
      </div>

    </div>
  </div>

  <!-- POINT RULES VIEW -->'''

content = content.replace(old, new)

# 設定リストに利規・プライバシーリンクを追加
old2 = '      <div class="settings-item" onclick="openOshiModal()">'
new2 = '''      <div class="settings-item" onclick="showView('terms')">
        <div class="settings-item-icon">📄</div>
        <div class="settings-item-text">利用規約</div>
        <div class="settings-item-arrow">›</div>
      </div>
      <div class="settings-item" onclick="showView('privacy')">
        <div class="settings-item-icon">🔐</div>
        <div class="settings-item-text">プライバシーポリシー</div>
        <div class="settings-item-arrow">›</div>
      </div>
      <div class="settings-item" onclick="openOshiModal()">'''

content = content.replace(old2, new2)

# showView関数のビューリストに追加
content = content.replace(
    "['map','ranking','feed','post','profile','route','pointrules']",
    "['map','ranking','feed','post','profile','route','pointrules','terms','privacy','howto']"
)

with open('trace-ive.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ 完了')

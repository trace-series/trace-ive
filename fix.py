with open('trace-ive.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ─────────────────────────────────────────
# 1. event-ranking-tabs の重複を修正
# ─────────────────────────────────────────
html = html.replace(
    '      <div id="event-ranking-tabs"></div>\n      <div id="event-ranking-tabs"></div>',
    '      <div id="event-ranking-tabs"></div>'
)

# ─────────────────────────────────────────
# 2. filterMemberAndOshi関数を完全削除（重複含む）
# ─────────────────────────────────────────
import re
html = re.sub(
    r'\n*// ── メンバータブ1タップで推しランキング直接切り替え ──\nfunction filterMemberAndOshi[^}]+\}\n+',
    '\n',
    html,
    flags=re.DOTALL
)

# ─────────────────────────────────────────
# 3. 動物アイコンを元に戻す
# ─────────────────────────────────────────
members = ['ユジン','ガウル','レイ','ウォニョン','リズ','イソ']
for name in members:
    old = f'<div class="member-tab-item" onclick="filterMemberAndOshi(this, \'{name}\')">'
    new = f'<div class="member-tab-item" onclick="filterMember(this, \'{name}\')" ondblclick="showOshiRanking(\'{name}\')">'
    html = html.replace(old, new)

# ─────────────────────────────────────────
# 4. oshi-ranking-modalのstyleを変更
#    inset:0 → top:120px（動物アイコンバーの下から表示）
#    これにより動物アイコンバーは常に操作可能
# ─────────────────────────────────────────
old_modal = '<div id="oshi-ranking-modal" style="display:none;position:fixed;inset:0;z-index:600;background:rgba(0,0,0,0.7);overflow-y:auto;" onclick="closeOshiRankingModal(event)">'
new_modal = '<div id="oshi-ranking-modal" style="display:none;position:fixed;top:110px;left:0;right:0;bottom:60px;z-index:600;background:rgba(0,0,0,0.7);overflow-y:auto;" onclick="closeOshiRankingModal(event)">'
html = html.replace(old_modal, new_modal)

# ─────────────────────────────────────────
# 5. showOshiRankingからbody.overflow=hidden を削除
#    （動物アイコンバーのスクロールを妨げないため）
# ─────────────────────────────────────────
html = html.replace(
    "  document.getElementById('oshi-ranking-modal').style.display = 'block';\n  document.body.style.overflow = 'hidden';",
    "  document.getElementById('oshi-ranking-modal').style.display = 'block';"
)

# ─────────────────────────────────────────
# 6. closeOshiRankingModalからbody.overflow=''を削除
# ─────────────────────────────────────────
html = html.replace(
    "document.getElementById('oshi-ranking-modal').style.display = 'none';\n    document.body.style.overflow = '';",
    "document.getElementById('oshi-ranking-modal').style.display = 'none';"
)
# ×ボタンのinlineスタイルも
html = html.replace(
    "document.getElementById('oshi-ranking-modal').style.display='none';document.body.style.overflow='';",
    "document.getElementById('oshi-ranking-modal').style.display='none';"
)

# ─────────────────────────────────────────
# 7. showOshiRankingを修正：開いていればメンバー切り替えのみ
# ─────────────────────────────────────────
old_show = '''function showOshiRanking(member) {
  const isAll = member === 'all';'''

new_show = '''function showOshiRanking(member) {
  const modal = document.getElementById('oshi-ranking-modal');
  if (modal && modal.style.display !== 'none') {
    // 既に開いている → メンバーだけ切り替え
    const isAll2 = member === 'all';
    const icon2 = isAll2 ? '💜' : (MEMBER_ICONS[member] || '💜');
    document.getElementById('oshi-ranking-icon').textContent = icon2;
    document.getElementById('oshi-ranking-title').textContent = isAll2
      ? '総合ポイントランキング'
      : `${member} 推しランキング`;
    modal.dataset.member = member;
    const activeTab = modal.querySelector('.orm-tab.active');
    const period = activeTab ? (activeTab.getAttribute('onclick').match(/'(\w+)'\)/) || ['','year'])[1] : 'year';
    renderOshiRankingList(member, period);
    return;
  }
  const isAll = member === 'all';'''

html = html.replace(old_show, new_show, 1)

with open('trace-ive.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ 完了！変更内容:")
print("  1. event-ranking-tabs重複を修正")
print("  2. filterMemberAndOshi関数を完全削除")
print("  3. MAPページの動物アイコン → フィルターのみ（元に戻した）")
print("  4. 推しランキングモーダル → 動物アイコンバーの下から表示（アイコン操作可能）")
print("  5. モーダルが開いている時に長押し → メンバーが直接切り替わる")
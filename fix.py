with open('/Users/missinglink/Documents/trace-ive/trace-ive.html', 'r', encoding='utf-8') as f:
    html = f.read()

css_add = """
  #list-view-toggle {
    position: fixed;
    top: 118px;
    right: 12px;
    z-index: 200;
    background: white;
    border: 2px solid var(--purple-light);
    border-radius: 20px;
    padding: 6px 14px;
    font-size: 12px;
    font-weight: 700;
    color: var(--purple-deep);
    cursor: pointer;
    box-shadow: 0 2px 8px rgba(0,0,0,0.12);
  }
  #spot-list-container {
    display: none;
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: #f9f7ff;
    overflow-y: auto;
    -webkit-overflow-scrolling: touch;
    z-index: 100;
    padding: 8px 12px 80px;
  }
  .spot-list-item {
    background: white;
    border-radius: 14px;
    padding: 12px 14px;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 12px;
    box-shadow: 0 2px 8px rgba(61,26,94,0.08);
    cursor: pointer;
  }
  .spot-list-icon {
    width: 42px;
    height: 42px;
    border-radius: 10px;
    background: linear-gradient(135deg, var(--purple-pale), var(--purple-light));
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    flex-shrink: 0;
  }
  .spot-list-info { flex: 1; min-width: 0; }
  .spot-list-name {
    font-size: 14px;
    font-weight: 700;
    color: var(--purple-deep);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .spot-list-addr {
    font-size: 11px;
    color: #888;
    margin-top: 2px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .spot-list-score {
    font-size: 12px;
    font-weight: 700;
    color: var(--purple-mid);
    flex-shrink: 0;
  }
"""

html = html.replace('</style>', css_add + '\n</style>', 1)

html = html.replace(
    '      <!-- ローディング -->',
    '      <button id="list-view-toggle" onclick="toggleListView()">リスト</button>\n      <div id="spot-list-container"></div>\n\n      <!-- ローディング -->'
)

js_add = """
// リストビュー
var listViewOpen = false;
function toggleListView() {
  listViewOpen = !listViewOpen;
  var container = document.getElementById('spot-list-container');
  var btn = document.getElementById('list-view-toggle');
  if (listViewOpen) {
    renderSpotList();
    container.style.display = 'block';
    btn.textContent = '地図';
  } else {
    container.style.display = 'none';
    btn.textContent = 'リスト';
  }
}

function renderSpotList() {
  var container = document.getElementById('spot-list-container');
  var filtered = SPOTS.filter(function(s) {
    if (activeCategory !== 'all' && s.category !== activeCategory) return false;
    if (activeMember !== 'all' && !s.members.includes(activeMember)) return false;
    return true;
  });
  if (filtered.length === 0) {
    container.innerHTML = '<div style="text-align:center;padding:40px;color:#aaa;">スポットが見つかりません</div>';
    return;
  }
  var catIcon = {'カフェ・飲食店':'🍜','撮影スポット':'📸','ライブ・イベント会場':'🎤','観光・名所':'🏯','ショップ':'🛍️'};
  container.innerHTML = filtered.map(function(s) {
    var icon = catIcon[s.category] || '📍';
    var score = (s.good_count || 0) - (s.bad_count || 0);
    var safeName = s.name.replace(/\\\\/g, '\\\\\\\\').replace(/'/g, "\\\\'");
    return '<div class="spot-list-item" onclick="selectSpotFromList(\\'' + safeName + '\\')">'
      + '<div class="spot-list-icon">' + icon + '</div>'
      + '<div class="spot-list-info">'
      + '<div class="spot-list-name">' + s.name + '</div>'
      + '<div class="spot-list-addr">' + (s.address || '') + '</div>'
      + '</div>'
      + '<div class="spot-list-score">★' + score + '</div>'
      + '</div>';
  }).join('');
}

function selectSpotFromList(name) {
  var spot = SPOTS.find(function(s) { return s.name === name; });
  if (!spot) return;
  listViewOpen = false;
  document.getElementById('spot-list-container').style.display = 'none';
  document.getElementById('list-view-toggle').textContent = 'リスト';
  if (map) map.panTo({ lat: spot.lat, lng: spot.lng });
  openCard(spot);
}
"""

html = html.replace('// ── フィルター ──', js_add + '\n// ── フィルター ──')

with open('/Users/missinglink/Documents/trace-ive/trace-ive.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('done')

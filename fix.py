with open('/Users/missinglink/Documents/trace-ive/trace-ive.html', 'r', encoding='utf-8') as f:
    html = f.read()

js_add = """
function renderRouteSpotList() {
  var container = document.getElementById('route-spot-list');
  if (!container) return;
  var catIcon = {'カフェ・飲食店':'🍜','撮影スポット':'📸','ライブ・イベント会場':'🎤','観光・名所':'🏯','ショップ':'🛍️'};
  var regionMap = {};
  SPOTS.forEach(function(s) {
    var r = s.region || 'other';
    if (!regionMap[r]) regionMap[r] = [];
    regionMap[r].push(s);
  });
  var regionOrder = ['tokyo', 'korea', 'japan_other'];
  var regionLabel = {'tokyo':'東京','korea':'韓国','japan_other':'その他日本'};
  var html = '';
  regionOrder.forEach(function(region) {
    if (!regionMap[region]) return;
    regionMap[region].forEach(function(s) {
      var icon = catIcon[s.category] || '📍';
      var meta = s.category + ' · ' + (regionLabel[region] || region);
      html += '<div class="route-spot-check" data-spot="' + s.name + '" data-meta="' + meta + '" data-icon="' + icon + '" data-lat="' + s.lat + '" data-lng="' + s.lng + '" data-region="' + region + '">'
        + '<div class="rsc-left">'
        + '<div class="rsc-check" onclick="toggleRouteSpot(this)">□</div>'
        + '<div class="rsc-icon">' + icon + '</div>'
        + '<div class="rsc-info"><div class="rsc-name">' + s.name + '</div><div class="rsc-meta">' + meta + '</div></div>'
        + '</div>'
        + '<div class="rsc-memo-wrap"><input class="rsc-memo" type="text" placeholder="メモ（任意）"></div>'
        + '</div>';
    });
  });
  container.innerHTML = html;
}
"""

html = html.replace('// リストビュー', js_add + '\n// リストビュー')

# showView('route')時にrenderRouteSpotListを呼ぶ
html = html.replace(
    "case 'route':",
    "case 'route':\n      renderRouteSpotList();"
)

with open('/Users/missinglink/Documents/trace-ive/trace-ive.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('done')

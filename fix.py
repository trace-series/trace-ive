with open('/Users/missinglink/Documents/trace-ive/trace-ive.html', 'r', encoding='utf-8') as f:
    html = f.read()

old = "    html += '<div class=\"route-spot-check\" data-spot=\"' + s.name + '\" data-meta=\"' + meta + '\" data-icon=\"' + icon + '\" data-lat=\"' + s.lat + '\" data-lng=\"' + s.lng + '\">';"

new = """    var koreaKeys = ['韓国', 'ソウル', '済州', '釜山', '弘大', 'COEX', '江南', '梨泰院', '明洞'];
    var tokyoKeys = ['東京都', '渋谷区', '新宿区', '港区', '中央区', '千代田区', '豊島区', '品川区', '目黒区', '世田谷区', '杉並区', '文京区', '台東区', '墨田区', '江東区', '足立区', '葛飾区', '北区', '中野区', '板橋区', '練馬区'];
    var addr = s.address || '';
    var spotRegion = koreaKeys.some(function(k){ return addr.indexOf(k) !== -1; }) ? 'korea' : tokyoKeys.some(function(k){ return addr.indexOf(k) !== -1; }) ? 'tokyo' : 'japan_other';
    html += '<div class="route-spot-check" data-spot="' + s.name + '" data-meta="' + meta + '" data-icon="' + icon + '" data-lat="' + s.lat + '" data-lng="' + s.lng + '" data-region="' + spotRegion + '">';"""

html = html.replace(old, new)
print('done' if 'spotRegion' in html else 'not found')

with open('/Users/missinglink/Documents/trace-ive/trace-ive.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('/Users/missinglink/Documents/trace-ive/trace-ive.html', 'r', encoding='utf-8') as f:
    html = f.read()

old = """  var filtered = SPOTS.filter(function(s) {
    if (currentRegion === 'all') return true;
    if (currentRegion === 'tokyo') return s.address && s.address.indexOf('東京') !== -1;
    if (currentRegion === 'korea') return s.address && (s.address.indexOf('韓国') !== -1 || s.address.indexOf('ソウル') !== -1 || s.address.indexOf('済州') !== -1);
    if (currentRegion === 'japan_other') return s.address && s.address.indexOf('東京') === -1 && s.address.indexOf('韓国') === -1 && s.address.indexOf('ソウル') === -1;
    return true;
  });"""

new = """  var filtered = SPOTS.filter(function(s) {
    if (currentRegion === 'all') return true;
    return s.region === currentRegion;
  });"""

html = html.replace(old, new)

with open('/Users/missinglink/Documents/trace-ive/trace-ive.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('done')

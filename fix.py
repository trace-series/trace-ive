with open('trace-ive.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. GPS距離表示のHTML構造を修正（前回の修正確認）
old1 = '''          <div class="card-detail-row">
            <span class="icon">📍</span>
            <span id="card-address">—</span>
            <div class="card-detail-row" id="card-distance-row" style="display:none;">
              <span class="icon">📡</span>
              <span id="card-distance">現在地を取得中…</span>
            </div>


          </div>'''

new1 = '''          <div class="card-detail-row">
            <span class="icon">📍</span>
            <span id="card-address">—</span>
          </div>
          <div class="card-detail-row" id="card-distance-row" style="display:none;">
            <span class="icon">📡</span>
            <span id="card-distance">現在地を取得中…</span>
          </div>'''

content = content.replace(old1, new1, 1)

# 2. GPSボーナス処理をopenCard関数の末尾に追加
old2 = '''  document.getElementById('card-detail').style.display = 'block';
  document.getElementById('map-card').classList.add('open');
  cardOpen = true;
}'''

new2 = '''  document.getElementById('card-detail').style.display = 'block';
  document.getElementById('map-card').classList.add('open');
  cardOpen = true;

  // GPS距離表示＆ボーナスポイント判定
  checkGpsBonus(spot);
}

// ── GPS距離チェック＆ボーナスポイント ──
const GPS_BONUS_KEY = 'traceive_gps_bonus_v1';
const GPS_BONUS_DISTANCE = 200; // メートル
const GPS_BONUS_PT = 50;

function getGpsBonusHistory() {
  try { return JSON.parse(localStorage.getItem(GPS_BONUS_KEY) || '[]'); }
  catch(e) { return []; }
}

function hasGpsBonusReceived(spotName) {
  return getGpsBonusHistory().includes(spotName);
}

function recordGpsBonus(spotName) {
  const h = getGpsBonusHistory();
  if (!h.includes(spotName)) {
    h.push(spotName);
    localStorage.setItem(GPS_BONUS_KEY, JSON.stringify(h));
  }
}

function calcDistance(lat1, lng1, lat2, lng2) {
  const R = 6371000;
  const dLat = (lat2 - lat1) * Math.PI / 180;
  const dLng = (lng2 - lng1) * Math.PI / 180;
  const a = Math.sin(dLat/2) * Math.sin(dLat/2)
    + Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180)
    * Math.sin(dLng/2) * Math.sin(dLng/2);
  return R * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
}

function checkGpsBonus(spot) {
  const row = document.getElementById('card-distance-row');
  const distEl = document.getElementById('card-distance');
  if (!row || !distEl) return;

  if (!navigator.geolocation) {
    row.style.display = 'none';
    return;
  }

  row.style.display = 'flex';
  distEl.textContent = '現在地を取得中…';

  navigator.geolocation.getCurrentPosition(
    (pos) => {
      const dist = calcDistance(pos.coords.latitude, pos.coords.longitude, spot.lat, spot.lng);
      const distKm = (dist / 1000).toFixed(1);
      distEl.textContent = `現在地から ${distKm} km`;

      // 200m以内でボーナス付与（1スポット1回限り）
      if (dist <= GPS_BONUS_DISTANCE && !hasGpsBonusReceived(spot.name)) {
        recordGpsBonus(spot.name);
        distEl.textContent = `現在地から ${distKm} km 🎉 GPS到達ボーナス +${GPS_BONUS_PT}pt！`;
        distEl.style.color = '#15803d';
        distEl.style.fontWeight = '700';
        addPendingPoint(spot.name, '📡 GPS到達ボーナス（200m以内）', GPS_BONUS_PT);
        showEvalToast(`🎉 GPS到達ボーナス +${GPS_BONUS_PT}pt 獲得！`);
        setTimeout(() => {
          distEl.style.color = '';
          distEl.style.fontWeight = '';
        }, 5000);
      } else if (dist <= GPS_BONUS_DISTANCE && hasGpsBonusReceived(spot.name)) {
        distEl.textContent = `現在地から ${distKm} km ✅ GPS到達済み`;
        distEl.style.color = '#9b8aab';
      }
    },
    (err) => {
      row.style.display = 'none';
    },
    { timeout: 8000, maximumAge: 30000 }
  );
}'''

content = content.replace(old2, new2, 1)

with open('trace-ive.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ GPS ボーナスポイント実装完了")
print("  - 200m以内で +50pt（1スポット1回限り）")
print("  - 距離表示も同時実装")
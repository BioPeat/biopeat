// BioPeat API & Admin Panel · Cloudflare Worker (0 € tier) + D1 (EU)
const ALLOWED_ORIGINS = new Set([
  'https://biopeat.github.io',
  'https://biopeat.app',
  'https://www.biopeat.app'
]);

const VAULT_ID_RE = /^[a-f0-9]{64}$/;
const STATUS_SET = new Set(['new', 'triaged', 'accepted', 'done', 'rejected']);
const CAT_SET = new Set(['idea', 'mejora', 'peat', 'error', 'general']);
const MAX_VAULT_BODY = 614400; // 600 KB
const MAX_FEEDBACK_BODY = 8192; // 8 KB
const MAX_PING_BODY = 2048; // 2 KB

function isAllowedOrigin(origin) {
  if (!origin) return false;
  if (ALLOWED_ORIGINS.has(origin)) return true;
  return /^http:\/\/(localhost|127\.0\.0\.1)(:\d+)?$/.test(origin);
}

function baseHeaders(origin) {
  const h = {
    'Strict-Transport-Security': 'max-age=63072000; includeSubDomains',
    'X-Content-Type-Options': 'nosniff',
    'X-Frame-Options': 'DENY',
    'Referrer-Policy': 'no-referrer',
    'Permissions-Policy': 'camera=(), microphone=(), geolocation=()',
    'Cache-Control': 'no-store'
  };
  if (origin && isAllowedOrigin(origin)) {
    h['Access-Control-Allow-Origin'] = origin;
    h['Access-Control-Allow-Methods'] = 'GET, PUT, POST, PATCH, DELETE, OPTIONS';
    h['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-BioPeat-Auth, X-TikTok-Upload-Url, Content-Range';
    h['Access-Control-Max-Age'] = '86400';
    h['Vary'] = 'Origin';
  }
  return h;
}

function jsonResp(data, status = 200, origin = '') {
  return new Response(JSON.stringify(data), {
    status,
    headers: {
      ...baseHeaders(origin),
      'Content-Type': 'application/json; charset=utf-8'
    }
  });
}

async function sha256Hex(input) {
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(input));
  return Array.from(new Uint8Array(buf), b => b.toString(16).padStart(2, '0')).join('');
}

async function timingSafeStrEqual(a, b) {
  if (typeof a !== 'string' || typeof b !== 'string') return false;
  const enc = new TextEncoder();
  const ha = await crypto.subtle.digest('SHA-256', enc.encode(a));
  const hb = await crypto.subtle.digest('SHA-256', enc.encode(b));
  return crypto.subtle.timingSafeEqual(ha, hb);
}

async function readLimitedJson(request, maxBytes) {
  const len = Number(request.headers.get('content-length') || 0);
  if (len > maxBytes) return { error: 'Payload too large', status: 413 };
  if (!request.body) return { error: 'Empty body', status: 400 };
  const reader = request.body.getReader();
  const chunks = [];
  let total = 0;
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    total += value.byteLength;
    if (total > maxBytes) {
      await reader.cancel().catch(() => {});
      return { error: 'Payload too large', status: 413 };
    }
    chunks.push(value);
  }
  const merged = new Uint8Array(total);
  let off = 0;
  for (const c of chunks) {
    merged.set(c, off);
    off += c.byteLength;
  }
  try {
    return { data: JSON.parse(new TextDecoder().decode(merged)) };
  } catch {
    return { error: 'Invalid JSON', status: 400 };
  }
}

function cleanStr(v, max = 120) {
  return String(v ?? '').replace(/[\u0000-\u001f\u007f]/g, ' ').trim().slice(0, max);
}

function cleanMetricToken(v, max = 32) {
  return String(v ?? '').toLowerCase().replace(/[^a-z0-9_.:-]/g, '').slice(0, max);
}

function uaFamily(ua) {
  if (!ua) return 'other';
  if (/iphone|ipad|ipod/i.test(ua)) return 'ios';
  if (/android/i.test(ua)) return 'android';
  if (/windows|macintosh|linux/i.test(ua)) return 'desktop';
  return 'other';
}

let ephemeralSalt = '';
let lastCleanupAt = 0;

function getFallbackSalt() {
  if (!ephemeralSalt) ephemeralSalt = crypto.randomUUID();
  return ephemeralSalt;
}

async function checkRateLimit(env, scope, ip, limit, windowSec = 3600) {
  const nowSec = Math.floor(Date.now() / 1000);
  const slot = Math.floor(nowSec / windowSec);
  const salt = env.SALT_SECRET || getFallbackSalt();
  const bucket = await sha256Hex(`${salt}:rl:${scope}:${slot}:${ip}`);
  const expiresAt = (slot + 1) * windowSec + 300;
  const row = await env.DB.prepare(
    'INSERT INTO rate_limits (bucket, hits, expires_at) VALUES (?, 1, ?) ' +
    'ON CONFLICT(bucket) DO UPDATE SET hits = hits + 1 RETURNING hits'
  ).bind(bucket, expiresAt).first();
  return (row?.hits || 0) <= limit;
}

async function cleanupOldRows(env) {
  const nowSec = Math.floor(Date.now() / 1000);
  const cutoffDate = new Date(Date.now() - 90 * 86400000).toISOString().slice(0, 10);
  await env.DB.batch([
    env.DB.prepare('DELETE FROM rate_limits WHERE expires_at < ?').bind(nowSec),
    env.DB.prepare('DELETE FROM active_visitors_daily WHERE day < ?').bind(cutoffDate)
  ]);
}

async function requireAdmin(request, env) {
  const auth = request.headers.get('authorization') || '';
  const token = auth.startsWith('Bearer ') ? auth.slice(7).trim() : '';
  if (!token || !env.ADMIN_TOKEN) return false;
  return timingSafeStrEqual(token, env.ADMIN_TOKEN);
}

function adminHtml() {
  return `<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>BioPeat · Panel de Estadísticas y Sugerencias</title>
<style>
:root{--bg:#09090b;--card:#111114;--surf:#17171b;--line:#27272a;--txt:#f4f4f5;--mut:#a1a1aa;--gold:#e9bf5c;--ok:#34d399;--warn:#fbbf24;--bad:#fb7185;--sky:#38bdf8}
html[data-theme=light]{--bg:#f6f5f1;--card:#ffffff;--surf:#f1efe9;--line:#e4e4e7;--txt:#111114;--mut:#52525b;--gold:#b45309;--ok:#059669;--warn:#d97706;--bad:#e11d48;--sky:#0284c7}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--txt);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;line-height:1.5;font-variant-numeric:tabular-nums}
.wrap{max-width:1100px;margin:0 auto;padding:18px 16px 64px}
header{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:12px;padding-bottom:16px;border-bottom:1px solid var(--line);margin-bottom:18px}
.brand{display:flex;align-items:center;gap:10px}.brand b{font-size:19px;letter-spacing:-.02em}.brand small{display:block;color:var(--mut);font-size:12px}
.tabs,.controls{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.btn{min-height:40px;padding:0 14px;border-radius:10px;border:1px solid var(--line);background:var(--surf);color:var(--txt);font-weight:700;font-size:13px;cursor:pointer;text-decoration:none;display:inline-flex;align-items:center;gap:6px}
.btn.pri{background:var(--txt);color:var(--bg);border-color:var(--txt)}
.btn.gold{background:var(--gold);color:#09090b;border-color:var(--gold)}
.btn.on{border-color:var(--gold);color:var(--gold)}
.btn.bad{border-color:var(--bad);color:var(--bad)}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px;margin-bottom:14px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:10px;margin-bottom:14px}
.kpi{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px}
.kpi span{display:block;font-size:11.5px;color:var(--mut);text-transform:uppercase;letter-spacing:.05em}
.kpi strong{display:block;font-size:26px;font-weight:800;margin-top:4px;letter-spacing:-.03em}
.kpi small{display:block;font-size:12px;color:var(--mut);margin-top:2px}
.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:14px}
.bars{display:grid;gap:8px}
.bar-row{display:grid;grid-template-columns:120px 1fr 56px;gap:8px;align-items:center;font-size:13px}
.bar-track{height:9px;border-radius:99px;background:var(--surf);overflow:hidden;border:1px solid var(--line)}
.bar-track i{display:block;height:100%;background:var(--gold)}
.chart-svg{width:100%;height:190px;display:block}
.fb-row{padding:14px 0;border-bottom:1px solid var(--line)}
.fb-row:last-child{border-bottom:0}
.fb-head{display:flex;flex-wrap:wrap;gap:8px;align-items:center;justify-content:space-between}
.pill{font-size:11px;font-weight:800;padding:2px 8px;border-radius:999px;border:1px solid var(--line);background:var(--surf);color:var(--mut);text-transform:uppercase}
.pill.new{border-color:var(--sky);color:var(--sky)}.pill.accepted{border-color:var(--warn);color:var(--warn)}.pill.done{border-color:var(--ok);color:var(--ok)}.pill.rejected{border-color:var(--bad);color:var(--bad)}
input,select,textarea{background:var(--surf);color:var(--txt);border:1px solid var(--line);border-radius:10px;padding:9px 11px;font:inherit;font-size:13.5px}
.auth-box{max-width:420px;margin:70px auto;padding:24px;background:var(--card);border:1px solid var(--line);border-radius:16px}
.auth-box h1{margin:0 0 8px;font-size:20px}
.auth-box p{margin:0 0 14px;color:var(--mut);font-size:13.5px}
.auth-box input{width:100%;margin-bottom:10px}
[hidden]{display:none!important}
.mut{color:var(--mut);font-size:13px}
</style>
</head>
<body>
<div class="wrap">
  <div id="login-view" class="auth-box" hidden>
    <h1>BioPeat · Acceso privado</h1>
    <p>Introduce tu clave de administrador (guardada en <code>.biopeat-admin-key.txt</code> en tu carpeta local). No se envía ni se guarda fuera de esta sesión.</p>
    <form id="login-form">
      <input type="password" id="token-in" placeholder="Clave de administrador" autocomplete="current-password" required>
      <button class="btn pri" style="width:100%;justify-content:center" type="submit">Entrar al panel</button>
    </form>
    <p id="login-err" class="mut" style="color:var(--bad);margin-top:10px"></p>
  </div>

  <div id="app-view" hidden>
    <header>
      <div class="brand">
        <div>
          <b>BioPeat · Panel de Control</b>
          <small>Estadísticas sin cookies · Bóvedas cifradas E2EE · Buzón de sugerencias</small>
        </div>
      </div>
      <div class="controls">
        <a class="btn" href="https://biopeat.goatcounter.com/" target="_blank" rel="noopener">GoatCounter ↗</a>
        <button class="btn" id="theme-btn" type="button">Tema</button>
        <button class="btn" id="logout-btn" type="button">Salir</button>
      </div>
    </header>

    <div class="tabs" style="margin-bottom:16px">
      <button class="btn on" data-tab="stats" type="button">Estadísticas</button>
      <button class="btn" data-tab="feedback" type="button">Sugerencias (<span id="fb-new-count">0</span> nuevas)</button>
      <select id="days-sel" aria-label="Periodo">
        <option value="7">Últimos 7 días</option>
        <option value="30" selected>Últimos 30 días</option>
        <option value="90">Últimos 90 días</option>
      </select>
      <button class="btn" id="refresh-btn" type="button">Actualizar</button>
    </div>

    <section id="tab-stats">
      <div class="kpis" id="kpis"></div>
      <div class="card">
        <h3 style="margin:0 0 10px;font-size:15px">Actividad diaria (visitantes únicos y aperturas)</h3>
        <div id="daily-chart"></div>
      </div>
      <div class="grid2" id="breakdowns"></div>
    </section>

    <section id="tab-feedback" hidden>
      <div class="card">
        <div style="display:flex;flex-wrap:wrap;gap:8px;align-items:center;justify-content:space-between">
          <div style="display:flex;flex-wrap:wrap;gap:8px;align-items:center">
            <select id="fb-status-filter">
              <option value="open">Pendientes (new + triaged + accepted)</option>
              <option value="all">Todas</option>
              <option value="new">Solo nuevas</option>
              <option value="accepted">Aceptadas</option>
              <option value="done">Hechas</option>
              <option value="rejected">Descartadas</option>
            </select>
            <select id="fb-cat-filter">
              <option value="">Todas las categorías</option>
              <option value="idea">Idea</option>
              <option value="mejora">Mejora</option>
              <option value="peat">Peat / nutrición</option>
              <option value="error">Error</option>
            </select>
          </div>
          <button class="btn gold" id="copy-prompt-btn" type="button">Copiar seleccionadas para Antigravity</button>
        </div>
      </div>
      <div class="card" id="fb-list"><p class="mut">Cargando…</p></div>
    </section>
  </div>
</div>
<script>
(function(){
  const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const $=id=>document.getElementById(id);
  const KEY='bp_admin_tok';
  let tok = '';
  try { tok = sessionStorage.getItem(KEY) || ''; } catch {}
  try { if (localStorage.getItem('bp_theme') === 'light') document.documentElement.dataset.theme = 'light'; } catch {}
  $('theme-btn').onclick = () => {
    const nxt = document.documentElement.dataset.theme === 'light' ? 'dark' : 'light';
    document.documentElement.dataset.theme = nxt;
    try { localStorage.setItem('bp_theme', nxt); } catch {}
  };
  async function api(path, opts = {}) {
    const res = await fetch(path, {
      ...opts,
      headers: {
        'Content-Type': 'application/json',
        ...(tok ? { Authorization: 'Bearer ' + tok } : {}),
        ...(opts.headers || {})
      }
    });
    if (res.status === 401) { tok = ''; try { sessionStorage.removeItem(KEY); } catch {} showLogin(); throw new Error('Sesión no válida'); }
    if (!res.ok) throw new Error('HTTP ' + res.status);
    return res.json();
  }
  function showLogin() { $('login-view').hidden = false; $('app-view').hidden = true; }
  function showApp() { $('login-view').hidden = true; $('app-view').hidden = false; loadAll(); }
  $('login-form').onsubmit = async e => {
    e.preventDefault();
    tok = $('token-in').value.trim();
    $('login-err').textContent = '';
    try {
      await api('/api/admin/stats?days=7');
      try { sessionStorage.setItem(KEY, tok); } catch {}
      $('token-in').value = '';
      showApp();
    } catch (err) {
      $('login-err').textContent = 'Clave incorrecta o error de conexión.';
    }
  };
  $('logout-btn').onclick = () => { tok = ''; try { sessionStorage.removeItem(KEY); } catch {} showLogin(); };
  document.querySelectorAll('[data-tab]').forEach(b => b.onclick = () => {
    const t = b.dataset.tab;
    document.querySelectorAll('[data-tab]').forEach(x => x.classList.toggle('on', x === b));
    $('tab-stats').hidden = t !== 'stats';
    $('tab-feedback').hidden = t !== 'feedback';
  });
  function drawBars(title, entries) {
    const mx = Math.max(1, ...entries.map(e => e[1]));
    return '<div class="card"><h3 style="margin:0 0 10px;font-size:15px">' + esc(title) + '</h3>' +
      (entries.length ? '<div class="bars">' + entries.slice(0, 10).map(([k, v]) =>
        '<div class="bar-row"><span title="' + esc(k) + '">' + esc(k || '—') + '</span><div class="bar-track"><i style="width:' + Math.round(v / mx * 100) + '%"></i></div><strong style="text-align:right">' + v + '</strong></div>'
      ).join('') + '</div>' : '<p class="mut">Sin datos aún en este periodo.</p>') + '</div>';
  }
  function drawDailyChart(days) {
    if (!days.length) return '<p class="mut">Sin actividad registrada todavía.</p>';
    const W = 720, H = 180, P = 24;
    const mx = Math.max(1, ...days.map(d => Math.max(d.visitors, d.views)));
    const bw = Math.max(3, (W - P * 2) / days.length - 3);
    const x = i => P + i * ((W - P * 2) / Math.max(1, days.length));
    const y = v => H - P - (v / mx) * (H - P * 2);
    const rects = days.map((d, i) => '<rect x="' + x(i).toFixed(1) + '" y="' + y(d.views).toFixed(1) + '" width="' + bw.toFixed(1) + '" height="' + (H - P - y(d.views)).toFixed(1) + '" rx="2" fill="var(--sky)" opacity="0.35"><title>' + esc(d.day) + ': ' + d.views + ' aperturas · ' + d.visitors + ' únicos</title></rect>').join('');
    const pts = days.map((d, i) => (x(i) + bw / 2).toFixed(1) + ',' + y(d.visitors).toFixed(1)).join(' ');
    return '<svg class="chart-svg" viewBox="0 0 ' + W + ' ' + H + '"><line x1="' + P + '" y1="' + (H - P) + '" x2="' + (W - P) + '" y2="' + (H - P) + '" stroke="var(--line)"/>' + rects + '<polyline fill="none" stroke="var(--gold)" stroke-width="2.5" points="' + pts + '"/><text x="' + P + '" y="14" fill="var(--mut)" font-size="11">Máx: ' + mx + ' · Barras azules = aperturas · Línea dorada = únicos/día</text></svg>';
  }
  let fbData = [];
  async function loadStats() {
    const days = $('days-sel').value;
    const s = await api('/api/admin/stats?days=' + encodeURIComponent(days));
    const k = s.kpis;
    const pwaPct = (k.pwaYes + k.pwaNo) ? Math.round(k.pwaYes / (k.pwaYes + k.pwaNo) * 100) : 0;
    const onbPct = k.onboardStart ? Math.round(k.onboardDone / Math.max(1, k.onboardStart) * 100) : 0;
    $('kpis').innerHTML = [
      ['Únicos hoy', k.uniqueToday, 'Visitantes únicos del día'],
      ['Únicos 7 días', k.unique7d, 'Sin cookies ni IP guardada'],
      ['Únicos ' + days + ' d', k.uniquePeriod, k.totalViews + ' aperturas totales'],
      ['App vs Web', k.appViews + ' / ' + k.landingViews, 'App / Landing inicio.html'],
      ['Instalada PWA', pwaPct + '%', k.pwaYes + ' standalone · ' + k.pwaNo + ' navegador'],
      ['Bóvedas E2EE', k.vaultCount, 'Media ' + Math.round((k.vaultAvgBytes || 0) / 1024) + ' KB (solo cifrado)'],
      ['Onboarding', k.onboardDone, onbPct ? onbPct + '% completado' : 'Asistentes cerrados'],
      ['Sugerencias nuevas', k.feedbackNew, k.feedbackTotal + ' totales en buzón']
    ].map(([a, b, c]) => '<div class="kpi"><span>' + esc(a) + '</span><strong>' + esc(b) + '</strong><small>' + esc(c) + '</small></div>').join('');
    $('fb-new-count').textContent = k.feedbackNew;
    $('daily-chart').innerHTML = drawDailyChart(s.daily || []);
    $('breakdowns').innerHTML = [
      drawBars('Idiomas', s.byLang || []),
      drawBars('Temas (Oscuro / Claro)', s.byTheme || []),
      drawBars('Países', s.byCountry || []),
      drawBars('Versiones de la app', s.byVersion || []),
      drawBars('Proveedores de IA usados', s.byAI || []),
      drawBars('Errores JS anónimos', s.byErrors || [])
    ].join('');
  }
  function renderFeedback() {
    const st = $('fb-status-filter').value, cat = $('fb-cat-filter').value;
    const list = fbData.filter(f => {
      if (st === 'open' && !['new', 'triaged', 'accepted'].includes(f.status)) return false;
      if (st !== 'open' && st !== 'all' && f.status !== st) return false;
      if (cat && f.category !== cat) return false;
      return true;
    });
    if (!list.length) { $('fb-list').innerHTML = '<p class="mut">No hay sugerencias en este filtro.</p>'; return; }
    $('fb-list').innerHTML = list.map(f =>
      '<div class="fb-row" data-id="' + f.id + '">' +
      '<div class="fb-head"><label style="display:flex;gap:8px;align-items:center"><input type="checkbox" class="fb-chk" value="' + f.id + '"><b>#' + f.id + ' · ' + esc(f.title) + '</b></label>' +
      '<div style="display:flex;gap:6px;align-items:center"><span class="pill">' + esc(f.category) + '</span><span class="pill ' + esc(f.status) + '">' + esc(f.status) + '</span></div></div>' +
      '<p style="margin:8px 0">' + esc(f.body) + '</p>' +
      '<p class="mut" style="margin:0 0 8px">' + esc(f.created_at) + ' · ' + esc(f.app_version) + ' · ' + esc(f.lang) + (f.view_name ? ' · vista ' + esc(f.view_name) : '') + (f.device ? ' · ' + esc(f.device) : '') + (f.origin ? ' · origen ' + esc(f.origin) : '') + '</p>' +
      '<div style="display:flex;flex-wrap:wrap;gap:6px;align-items:center">' +
      '<select class="fb-st" data-id="' + f.id + '">' + ['new','triaged','accepted','done','rejected'].map(s => '<option value="' + s + '"' + (f.status === s ? ' selected' : '') + '>' + s + '</option>').join('') + '</select>' +
      '<input class="fb-note" data-id="' + f.id + '" value="' + esc(f.ai_notes || '') + '" placeholder="Nota interna / decisión" style="flex:1;min-width:180px">' +
      '<button class="btn" data-save-fb="' + f.id + '" type="button">Guardar</button>' +
      '<button class="btn bad" data-del-fb="' + f.id + '" type="button">Eliminar</button>' +
      '</div></div>'
    ).join('');
  }
  async function loadFeedback() {
    const r = await api('/api/admin/feedback');
    fbData = r.items || [];
    renderFeedback();
  }
  async function loadAll() { await Promise.all([loadStats(), loadFeedback()]); }
  $('days-sel').onchange = loadStats;
  $('refresh-btn').onclick = loadAll;
  $('fb-status-filter').onchange = renderFeedback;
  $('fb-cat-filter').onchange = renderFeedback;
  $('fb-list').onclick = async e => {
    const sv = e.target.closest('[data-save-fb]');
    if (sv) {
      const id = sv.dataset.saveFb;
      const status = document.querySelector('.fb-st[data-id="' + id + '"]').value;
      const ai_notes = document.querySelector('.fb-note[data-id="' + id + '"]').value;
      await api('/api/admin/feedback/' + id, { method: 'PATCH', body: JSON.stringify({ status, ai_notes }) });
      await loadAll();
    }
    const dl = e.target.closest('[data-del-fb]');
    if (dl && confirm('¿Eliminar definitivamente esta sugerencia?')) {
      await api('/api/admin/feedback/' + dl.dataset.delFb, { method: 'DELETE' });
      await loadAll();
    }
  };
  $('copy-prompt-btn').onclick = async () => {
    const ids = new Set([...document.querySelectorAll('.fb-chk:checked')].map(c => Number(c.value)));
    const items = fbData.filter(f => ids.size ? ids.has(f.id) : ['new', 'triaged'].includes(f.status));
    if (!items.length) return alert('Marca alguna sugerencia primero.');
    const txt = 'Analiza estas sugerencias de usuarios de BioPeat (puedes consultar biopeat-db) y dime cuáles recomiendas aplicar:\n\n' +
      items.map(f => '#' + f.id + ' [' + f.category + ' · ' + f.lang + '] ' + f.title + '\n' + f.body).join('\n\n');
    await navigator.clipboard.writeText(txt);
    alert('Copiadas ' + items.length + ' sugerencias para pegar en Antigravity.');
  };
  if (tok) showApp(); else showLogin();
})();
</script>
</body>
</html>`;
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const origin = request.headers.get('origin') || '';
    const ip = request.headers.get('cf-connecting-ip') || '0.0.0.0';

    if (request.method === 'OPTIONS') {
      if (origin && !isAllowedOrigin(origin)) {
        return new Response(null, { status: 403, headers: baseHeaders('') });
      }
      return new Response(null, { status: 204, headers: baseHeaders(origin) });
    }

    if (origin && url.pathname.startsWith('/api/') && !isAllowedOrigin(origin)) {
      return jsonResp({ error: 'Origin not allowed' }, 403, '');
    }

    if (url.pathname === '/api/health' && request.method === 'GET') {
      return jsonResp({ ok: true, service: 'biopeat-api', version: '1.0', time: new Date().toISOString() }, 200, origin);
    }

    // Encrypted E2EE vault endpoints (zero-knowledge: server stores only ciphertext + auth hash)
    const vaultMatch = url.pathname.match(/^\/api\/vault\/([a-f0-9]{64})$/);
    if (vaultMatch) {
      const vaultId = vaultMatch[1];
      if (!VAULT_ID_RE.test(vaultId)) return jsonResp({ error: 'Invalid vault id' }, 400, origin);
      const okRate = await checkRateLimit(env, 'vault', ip, 90, 3600);
      if (!okRate) return jsonResp({ error: 'Too many requests' }, 429, origin);
      const authHeader = cleanStr(request.headers.get('x-biopeat-auth'), 128);
      if (!/^[a-f0-9]{64}$/.test(authHeader)) return jsonResp({ error: 'Missing auth token' }, 401, origin);
      if (!env.SALT_SECRET) return jsonResp({ error: 'Server configuration error' }, 500, origin);
      const authHash = await sha256Hex(env.SALT_SECRET + ':vault:' + authHeader);

      if (request.method === 'GET') {
        const row = await env.DB.prepare(
          'SELECT auth_hash, iv, ciphertext, compressed, rev, updated_at FROM vaults WHERE vault_id = ?'
        ).bind(vaultId).first();
        if (!row) return jsonResp({ error: 'Not found' }, 404, origin);
        if (!(await timingSafeStrEqual(row.auth_hash, authHash))) return jsonResp({ error: 'Forbidden' }, 403, origin);
        return jsonResp({
          iv: row.iv,
          ciphertext: row.ciphertext,
          compressed: !!row.compressed,
          rev: row.rev,
          updated_at: row.updated_at
        }, 200, origin);
      }

      if (request.method === 'PUT') {
        const parsed = await readLimitedJson(request, MAX_VAULT_BODY);
        if (parsed.error) return jsonResp({ error: parsed.error }, parsed.status, origin);
        const body = parsed.data || {};
        const iv = String(body.iv || '');
        const ciphertext = String(body.ciphertext || '');
        const compressed = body.compressed ? 1 : 0;
        const baseRev = body.baseRev == null ? null : Number(body.baseRev);
        const appVersion = cleanStr(body.appVersion, 16);
        if (!/^[A-Za-z0-9+/=_-]{12,64}$/.test(iv) || !/^[A-Za-z0-9+/=_-]{16,}$/.test(ciphertext)) {
          return jsonResp({ error: 'Invalid encrypted payload' }, 400, origin);
        }
        const now = Date.now();
        const existing = await env.DB.prepare(
          'SELECT auth_hash, iv, ciphertext, compressed, rev, updated_at FROM vaults WHERE vault_id = ?'
        ).bind(vaultId).first();

        if (!existing) {
          await env.DB.prepare(
            'INSERT INTO vaults (vault_id, auth_hash, iv, ciphertext, compressed, rev, size_bytes, app_version, updated_at, created_at) ' +
            'VALUES (?, ?, ?, ?, ?, 1, ?, ?, ?, ?)'
          ).bind(vaultId, authHash, iv, ciphertext, compressed, ciphertext.length, appVersion, now, now).run();
          return jsonResp({ ok: true, rev: 1, updated_at: now }, 200, origin);
        }

        if (!(await timingSafeStrEqual(existing.auth_hash, authHash))) {
          return jsonResp({ error: 'Forbidden' }, 403, origin);
        }
        if (baseRev === null || !Number.isFinite(baseRev) || existing.rev > baseRev) {
          return jsonResp({
            conflict: true,
            rev: existing.rev,
            iv: existing.iv,
            ciphertext: existing.ciphertext,
            compressed: !!existing.compressed,
            updated_at: existing.updated_at
          }, 409, origin);
        }
        const nextRev = existing.rev + 1;
        const upd = await env.DB.prepare(
          'UPDATE vaults SET iv = ?, ciphertext = ?, compressed = ?, rev = ?, size_bytes = ?, app_version = ?, updated_at = ? WHERE vault_id = ? AND rev = ?'
        ).bind(iv, ciphertext, compressed, nextRev, ciphertext.length, appVersion, now, vaultId, existing.rev).run();
        if (upd?.meta && upd.meta.changes === 0) {
          const latest = await env.DB.prepare(
            'SELECT iv, ciphertext, compressed, rev, updated_at FROM vaults WHERE vault_id = ?'
          ).bind(vaultId).first();
          if (latest) {
            return jsonResp({
              conflict: true,
              rev: latest.rev,
              iv: latest.iv,
              ciphertext: latest.ciphertext,
              compressed: !!latest.compressed,
              updated_at: latest.updated_at
            }, 409, origin);
          }
        }
        return jsonResp({ ok: true, rev: nextRev, updated_at: now }, 200, origin);
      }

      if (request.method === 'DELETE') {
        const existing = await env.DB.prepare('SELECT auth_hash FROM vaults WHERE vault_id = ?').bind(vaultId).first();
        if (!existing) return jsonResp({ ok: true }, 200, origin);
        if (!(await timingSafeStrEqual(existing.auth_hash, authHash))) return jsonResp({ error: 'Forbidden' }, 403, origin);
        await env.DB.prepare('DELETE FROM vaults WHERE vault_id = ?').bind(vaultId).run();
        return jsonResp({ ok: true }, 200, origin);
      }

      return jsonResp({ error: 'Method not allowed' }, 405, origin);
    }

    // Public anonymous suggestions endpoint
    if (url.pathname === '/api/feedback' && request.method === 'POST') {
      const okRate = await checkRateLimit(env, 'fb', ip, 10, 3600);
      if (!okRate) return jsonResp({ error: 'Too many suggestions, please wait a little.' }, 429, origin);
      const parsed = await readLimitedJson(request, MAX_FEEDBACK_BODY);
      if (parsed.error) return jsonResp({ error: parsed.error }, parsed.status, origin);
      const b = parsed.data || {};
      if (String(b.website || '').trim()) return jsonResp({ ok: true, id: 0 }, 200, origin); // silent honeypot
      const category = CAT_SET.has(b.category) ? b.category : 'idea';
      const title = cleanStr(b.title, 120);
      const body = String(b.body ?? '').replace(/[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/g, '').trim().slice(0, 3500);
      if (title.length < 3 || body.length < 10) {
        return jsonResp({ error: 'Title and description are too short.' }, 400, origin);
      }
      const res = await env.DB.prepare(
        'INSERT INTO feedback (created_at, category, title, body, app_version, lang, view_name, device, origin, status) ' +
        'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
      ).bind(
        new Date().toISOString(),
        category,
        title,
        body,
        cleanStr(b.app_version, 24),
        b.lang === 'en' ? 'en' : 'es',
        cleanStr(b.view_name, 24),
        cleanStr(b.device, 32),
        cleanStr(b.origin, 64),
        'new'
      ).run();
      return jsonResp({ ok: true, id: res.meta?.last_row_id || 0 }, 201, origin);
    }

    // Cookie-less, IP-free aggregate analytics ping
    if (url.pathname === '/api/ping' && request.method === 'POST') {
      const okRate = await checkRateLimit(env, 'ping', ip, 180, 3600);
      if (!okRate) return new Response(null, { status: 204, headers: baseHeaders(origin) });
      const parsed = await readLimitedJson(request, MAX_PING_BODY);
      if (parsed.error) return new Response(null, { status: 204, headers: baseHeaders(origin) });
      const b = parsed.data || {};
      const day = new Date().toISOString().slice(0, 10);
      const surface = b.surface === 'landing' ? 'landing' : 'app';
      const salt = env.SALT_SECRET || getFallbackSalt();
      const ua = request.headers.get('user-agent') || '';
      const visitorHash = (await sha256Hex(`${salt}:v:${day}:${ip}:${uaFamily(ua)}`)).slice(0, 16);
      const country = cleanMetricToken(request.cf?.country || 'xx', 6) || 'xx';
      const metrics = [];
      if (!b.event || b.event === 'pageview') {
        metrics.push('pv:' + surface);
        if (b.lang === 'es' || b.lang === 'en') metrics.push('lang:' + b.lang);
        if (b.theme === 'light' || b.theme === 'dark') metrics.push('theme:' + b.theme);
        if (typeof b.pwa === 'boolean') metrics.push('pwa:' + (b.pwa ? 'standalone' : 'browser'));
        const ver = cleanMetricToken(b.ver, 12);
        if (ver) metrics.push('ver:' + ver);
        metrics.push('country:' + country);
      }
      const ev = cleanMetricToken(b.event, 36);
      if (ev && ev !== 'pageview') metrics.push('event:' + ev);
      const vw = cleanMetricToken(b.view, 24);
      if (vw) metrics.push('view:' + vw);
      const ai = cleanMetricToken(b.ai, 24);
      if (ai) metrics.push('ai:' + ai);
      const errTag = cleanMetricToken(b.err, 40);
      if (errTag) metrics.push('err:' + errTag);

      const stmts = [
        env.DB.prepare('INSERT OR IGNORE INTO active_visitors_daily (day, visitor_hash, surface) VALUES (?, ?, ?)')
          .bind(day, visitorHash, surface)
      ];
      for (const m of metrics.slice(0, 10)) {
        stmts.push(
          env.DB.prepare('INSERT INTO analytics_daily (day, metric, count) VALUES (?, ?, 1) ON CONFLICT(day, metric) DO UPDATE SET count = count + 1')
            .bind(day, m)
        );
      }
      await env.DB.batch(stmts);
      if (Date.now() - lastCleanupAt > 1800000) {
        lastCleanupAt = Date.now();
        ctx.waitUntil(cleanupOldRows(env).catch(() => {}));
      }
      return new Response(null, { status: 204, headers: baseHeaders(origin) });
    }

    // Admin UI
    if (url.pathname === '/admin' && request.method === 'GET') {
      const h = baseHeaders('');
      h['Content-Type'] = 'text/html; charset=utf-8';
      h['X-Robots-Tag'] = 'noindex, nofollow';
      h['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; connect-src 'self'; img-src 'self' data:; object-src 'none'; base-uri 'self'; frame-ancestors 'none'";
      return new Response(adminHtml(), { status: 200, headers: h });
    }

    // Admin API
    if (url.pathname.startsWith('/api/admin/')) {
      const okAdmPre = await checkRateLimit(env, 'admin_pre', ip, 60, 3600);
      if (!okAdmPre) return jsonResp({ error: 'Too many requests' }, 429, origin);
      if (!(await requireAdmin(request, env))) {
        const okAdm = await checkRateLimit(env, 'admin_fail', ip, 12, 3600);
        if (!okAdm) return jsonResp({ error: 'Too many requests' }, 429, origin);
        return jsonResp({ error: 'Unauthorized' }, 401, origin);
      }

      if (url.pathname === '/api/admin/stats' && request.method === 'GET') {
        const daysNum = Math.max(1, Math.min(90, Number(url.searchParams.get('days')) || 30));
        const today = new Date().toISOString().slice(0, 10);
        const d7 = new Date(Date.now() - 6 * 86400000).toISOString().slice(0, 10);
        const dFrom = new Date(Date.now() - (daysNum - 1) * 86400000).toISOString().slice(0, 10);

        const [uniqToday, uniq7, uniqP, dailyVis, metricRows, vaultsAgg, fbAgg] = await Promise.all([
          env.DB.prepare('SELECT COUNT(DISTINCT visitor_hash) AS n FROM active_visitors_daily WHERE day = ?').bind(today).first(),
          env.DB.prepare('SELECT COUNT(DISTINCT visitor_hash) AS n FROM active_visitors_daily WHERE day >= ?').bind(d7).first(),
          env.DB.prepare('SELECT COUNT(DISTINCT visitor_hash) AS n FROM active_visitors_daily WHERE day >= ?').bind(dFrom).first(),
          env.DB.prepare('SELECT day, COUNT(DISTINCT visitor_hash) AS visitors FROM active_visitors_daily WHERE day >= ? GROUP BY day ORDER BY day ASC').bind(dFrom).all(),
          env.DB.prepare('SELECT day, metric, count FROM analytics_daily WHERE day >= ?').bind(dFrom).all(),
          env.DB.prepare('SELECT COUNT(*) AS cnt, COALESCE(AVG(size_bytes), 0) AS avg_bytes FROM vaults').first(),
          env.DB.prepare("SELECT COUNT(*) AS total, SUM(CASE WHEN status = 'new' THEN 1 ELSE 0 END) AS new_cnt FROM feedback").first()
        ]);

        const dayMap = new Map();
        for (const r of (dailyVis.results || [])) dayMap.set(r.day, { day: r.day, visitors: r.visitors, views: 0 });
        const agg = new Map();
        let appViews = 0, landingViews = 0, pwaYes = 0, pwaNo = 0, onboardStart = 0, onboardDone = 0;

        for (const r of (metricRows.results || [])) {
          agg.set(r.metric, (agg.get(r.metric) || 0) + r.count);
          if (r.metric === 'pv:app' || r.metric === 'pv:landing') {
            const cur = dayMap.get(r.day) || { day: r.day, visitors: 0, views: 0 };
            cur.views += r.count;
            dayMap.set(r.day, cur);
            if (r.metric === 'pv:app') appViews += r.count; else landingViews += r.count;
          }
          if (r.metric === 'pwa:standalone') pwaYes += r.count;
          if (r.metric === 'pwa:browser') pwaNo += r.count;
          if (r.metric === 'event:onboardstart') onboardStart += r.count;
          if (r.metric === 'event:onboardcomplete') onboardDone += r.count;
        }

        const pickPrefix = prefix => [...agg.entries()]
          .filter(([k]) => k.startsWith(prefix))
          .map(([k, v]) => [k.slice(prefix.length), v])
          .sort((a, b) => b[1] - a[1]);

        return jsonResp({
          kpis: {
            uniqueToday: uniqToday?.n || 0,
            unique7d: uniq7?.n || 0,
            uniquePeriod: uniqP?.n || 0,
            totalViews: appViews + landingViews,
            appViews,
            landingViews,
            pwaYes,
            pwaNo,
            onboardStart,
            onboardDone,
            vaultCount: vaultsAgg?.cnt || 0,
            vaultAvgBytes: Math.round(vaultsAgg?.avg_bytes || 0),
            feedbackNew: fbAgg?.new_cnt || 0,
            feedbackTotal: fbAgg?.total || 0
          },
          daily: [...dayMap.values()].sort((a, b) => a.day.localeCompare(b.day)),
          byLang: pickPrefix('lang:'),
          byTheme: pickPrefix('theme:'),
          byCountry: pickPrefix('country:'),
          byVersion: pickPrefix('ver:'),
          byAI: pickPrefix('ai:'),
          byErrors: pickPrefix('err:')
        }, 200, origin);
      }

      if (url.pathname === '/api/admin/feedback' && request.method === 'GET') {
        const res = await env.DB.prepare(
          'SELECT id, created_at, category, title, body, app_version, lang, view_name, device, origin, status, ai_notes FROM feedback ORDER BY id DESC LIMIT 200'
        ).all();
        return jsonResp({ items: res.results || [] }, 200, origin);
      }

      const fbMatch = url.pathname.match(/^\/api\/admin\/feedback\/(\d+)$/);
      if (fbMatch && request.method === 'PATCH') {
        const id = Number(fbMatch[1]);
        const parsed = await readLimitedJson(request, MAX_FEEDBACK_BODY);
        if (parsed.error) return jsonResp({ error: parsed.error }, parsed.status, origin);
        const b = parsed.data || {};
        const status = STATUS_SET.has(b.status) ? b.status : 'triaged';
        const aiNotes = String(b.ai_notes ?? '').slice(0, 1500);
        await env.DB.prepare('UPDATE feedback SET status = ?, ai_notes = ? WHERE id = ?').bind(status, aiNotes, id).run();
        return jsonResp({ ok: true }, 200, origin);
      }

      if (fbMatch && request.method === 'DELETE') {
        const id = Number(fbMatch[1]);
        await env.DB.prepare('DELETE FROM feedback WHERE id = ?').bind(id).run();
        return jsonResp({ ok: true }, 200, origin);
      }
    }

    // Stateless TikTok OAuth2 + Content Posting API proxy for BioPeat Studio (no token storage)
    if (url.pathname.startsWith('/api/tiktok/')) {
      if (url.pathname === '/api/tiktok/config' && request.method === 'GET') {
        const ck = String(env.TIKTOK_CLIENT_KEY || '').trim();
        const cs = String(env.TIKTOK_CLIENT_SECRET || '').trim();
        return jsonResp({ configured: Boolean(ck && cs), client_key: ck }, 200, origin);
      }

      if (!isAllowedOrigin(origin)) {
        return jsonResp({ error: 'Origin not allowed' }, 403, origin);
      }

      if (url.pathname === '/api/tiktok/token' && request.method === 'POST') {
        const ck = String(env.TIKTOK_CLIENT_KEY || '').trim();
        const cs = String(env.TIKTOK_CLIENT_SECRET || '').trim();
        if (!ck || !cs) return jsonResp({ error: 'TikTok client credentials not configured on Worker' }, 503, origin);
        const parsed = await readLimitedJson(request, 8192);
        if (parsed.error) return jsonResp({ error: parsed.error }, parsed.status, origin);
        const b = parsed.data || {};
        const code = String(b.code || '').trim();
        const redirectUri = String(b.redirect_uri || '').trim();
        const verifier = String(b.code_verifier || '').trim();
        if (!code || !verifier || !redirectUri.startsWith('https://biopeat.github.io/biopeat/')) {
          return jsonResp({ error: 'Invalid token exchange parameters' }, 400, origin);
        }
        const form = new URLSearchParams({
          client_key: ck,
          client_secret: cs,
          code,
          grant_type: 'authorization_code',
          redirect_uri: redirectUri,
          code_verifier: verifier
        });
        const ttResp = await fetch('https://open.tiktokapis.com/v2/oauth/token/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
          body: form.toString()
        });
        const ttJson = await ttResp.json().catch(() => ({ error: 'Invalid upstream response' }));
        return jsonResp(ttJson, ttResp.status, origin);
      }

      if (url.pathname === '/api/tiktok/upload' && request.method === 'PUT') {
        const uploadUrl = String(request.headers.get('X-TikTok-Upload-Url') || '').trim();
        let parsedUp;
        try { parsedUp = new URL(uploadUrl); } catch { parsedUp = null; }
        if (!parsedUp || parsedUp.protocol !== 'https:' || parsedUp.username || parsedUp.password || !/(^|\.)tiktokapis\.com$/i.test(parsedUp.hostname)) {
          return jsonResp({ error: 'Invalid TikTok upload URL' }, 400, origin);
        }
        const contentLen = Number(request.headers.get('content-length') || 0);
        if (contentLen > 52428800) {
          return jsonResp({ error: 'Video exceeds 50 MB limit' }, 413, origin);
        }
        const buf = await request.arrayBuffer();
        if (buf.byteLength > 52428800) {
          return jsonResp({ error: 'Video exceeds 50 MB limit' }, 413, origin);
        }
        const fwdHeaders = { 'Content-Type': request.headers.get('Content-Type') || 'video/mp4' };
        const cr = request.headers.get('Content-Range');
        if (cr) fwdHeaders['Content-Range'] = cr;
        const putResp = await fetch(uploadUrl, { method: 'PUT', headers: fwdHeaders, body: buf });
        const txt = await putResp.text().catch(() => '');
        return new Response(txt, { status: putResp.status, headers: baseHeaders(origin) });
      }

      const auth = request.headers.get('authorization') || '';
      if (!auth.startsWith('Bearer ')) {
        return jsonResp({ error: 'Missing Bearer token' }, 401, origin);
      }

      if (url.pathname === '/api/tiktok/user-info' && request.method === 'POST') {
        const ttResp = await fetch('https://open.tiktokapis.com/v2/user/info/?fields=open_id,union_id,avatar_url,display_name,username', {
          method: 'GET',
          headers: { Authorization: auth }
        });
        const ttJson = await ttResp.json().catch(() => ({ error: 'Invalid upstream response' }));
        return jsonResp(ttJson, ttResp.status, origin);
      }

      if (url.pathname === '/api/tiktok/creator-info' && request.method === 'POST') {
        const ttResp = await fetch('https://open.tiktokapis.com/v2/post/publish/creator_info/query/', {
          method: 'POST',
          headers: { Authorization: auth, 'Content-Type': 'application/json; charset=UTF-8' },
          body: '{}'
        });
        const ttJson = await ttResp.json().catch(() => ({ error: 'Invalid upstream response' }));
        return jsonResp(ttJson, ttResp.status, origin);
      }

      if (url.pathname === '/api/tiktok/video-list' && request.method === 'POST') {
        const parsed = await readLimitedJson(request, 4096);
        if (parsed.error) return jsonResp({ error: parsed.error }, parsed.status, origin);
        const ttResp = await fetch('https://open.tiktokapis.com/v2/video/list/?fields=id,title,create_time,cover_image_url,share_url,view_count,like_count', {
          method: 'POST',
          headers: { Authorization: auth, 'Content-Type': 'application/json; charset=UTF-8' },
          body: JSON.stringify(parsed.data || { max_count: 6 })
        });
        const ttJson = await ttResp.json().catch(() => ({ error: 'Invalid upstream response' }));
        return jsonResp(ttJson, ttResp.status, origin);
      }

      if (url.pathname === '/api/tiktok/publish-init' && request.method === 'POST') {
        const parsed = await readLimitedJson(request, 16384);
        if (parsed.error) return jsonResp({ error: parsed.error }, parsed.status, origin);
        const isInbox = url.searchParams.get('mode') === 'inbox';
        const endpoint = isInbox
          ? 'https://open.tiktokapis.com/v2/post/publish/inbox/video/init/'
          : 'https://open.tiktokapis.com/v2/post/publish/video/init/';
        const ttResp = await fetch(endpoint, {
          method: 'POST',
          headers: { Authorization: auth, 'Content-Type': 'application/json; charset=UTF-8' },
          body: JSON.stringify(parsed.data || {})
        });
        const ttJson = await ttResp.json().catch(() => ({ error: 'Invalid upstream response' }));
        return jsonResp(ttJson, ttResp.status, origin);
      }

      if (url.pathname === '/api/tiktok/publish-status' && request.method === 'POST') {
        const parsed = await readLimitedJson(request, 4096);
        if (parsed.error) return jsonResp({ error: parsed.error }, parsed.status, origin);
        const ttResp = await fetch('https://open.tiktokapis.com/v2/post/publish/status/fetch/', {
          method: 'POST',
          headers: { Authorization: auth, 'Content-Type': 'application/json; charset=UTF-8' },
          body: JSON.stringify(parsed.data || {})
        });
        const ttJson = await ttResp.json().catch(() => ({ error: 'Invalid upstream response' }));
        return jsonResp(ttJson, ttResp.status, origin);
      }
    }

    return jsonResp({ error: 'Not found' }, 404, origin);
  }
};

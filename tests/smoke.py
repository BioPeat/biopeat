#!/usr/bin/env python3
"""Prueba completa de BioPeat en un navegador real (Chromium sin ventana).

Uso (desde la raíz del repositorio):
    pip install playwright && python -m playwright install --with-deps chromium
    python tests/smoke.py

Termina con «TODO OK» (código 0) o con la lista de fallos (código 1).
No necesita internet: la IA se simula. Usa tests/datos_prueba.json (datos inventados, formato antiguo v29).
"""
import asyncio, functools, http.server, json, os, re, sys, threading
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIXTURE = ROOT / 'tests' / 'datos_prueba.json'
DAY = '2026-10-14'          # miércoles con comidas en los datos de prueba
NOW = '2026-10-14T13:00:00'
FAILS = []

def fail(msg):
    FAILS.append(msg)
    print('  ✗', msg)

def ok(msg):
    print('  ✓', msg)

# ---------- 1. Comprobaciones estáticas (sin navegador) ----------
ALLOWED = {'index.html', 'manifest.json', 'sw.js', 'icon-192.png', 'icon-512.png', 'icon-maskable-512.png',
           'AGENTS.md', 'CONTEXTO_BIOPEAT.md', 'MAPA_DEL_CODIGO.md', 'README.md', '.gitignore',
           'tests/smoke.py', 'tests/datos_prueba.json', 'tools/mapa.py', '.github/workflows/check.yml'}

def static_checks():
    print('1. Comprobaciones del código')
    html = (ROOT / 'index.html').read_text(encoding='utf-8')
    a = html.index('<script id="app">')
    page, js = html[:a], html[a:]
    ids = set(re.findall(r'id="([^"$]+)"', page)) | set(re.findall(r'id="([^"$]+)"', js)) | set(re.findall(r"\.id\s*=\s*'([^']+)'", js))
    used = set(re.findall(r"\$\('([^']+)'\)", js))
    missing = sorted(u for u in used if u not in ids)
    fail('IDs usados en el JS que no existen en el HTML: ' + ', '.join(missing)) if missing else ok('Todos los $(id) existen')
    names = re.findall(r'\bfunction\s+([A-Za-z_$][\w$]*)\s*\(', js)
    dups = sorted({n for n in names if names.count(n) > 1})
    fail('Funciones definidas dos veces: ' + ', '.join(dups)) if dups else ok('Ninguna función duplicada')
    if re.search(r'\balert\(', js): fail('Hay alert(): usa toast()')
    ver = re.search(r"APP_VERSION='(v\d+)'", js)
    rev = re.search(r"APP_REVISION=(\d+)", js)
    if not ver or not rev: fail('No encuentro APP_VERSION o APP_REVISION en index.html')
    else:
        ctx = (ROOT / 'CONTEXTO_BIOPEAT.md').read_text(encoding='utf-8') if (ROOT / 'CONTEXTO_BIOPEAT.md').exists() else ''
        m = re.search(r'Versión actual:\s*\*?\*?(v\d+)', ctx)
        if not m or m.group(1) != ver.group(1): fail(f'CONTEXTO_BIOPEAT.md dice «Versión actual: {m.group(1) if m else "?"}» pero index.html es {ver.group(1)}')
        else: ok(f'Versión {ver.group(1)} (revisión de datos {rev.group(1)}) coherente con CONTEXTO')
        ups = [int(x) for x in re.findall(r'function upgradeTo(\d+)\(', js)]
        if ups and max(ups) > int(rev.group(1)): fail(f'Existe upgradeTo{max(ups)} pero APP_REVISION={rev.group(1)}: súbelo')
    for f in ['CONTEXTO_BIOPEAT.md', 'MAPA_DEL_CODIGO.md', 'AGENTS.md']:
        p = ROOT / f
        if p.exists() and p.stat().st_size > 60000: fail(f'{f} pesa {p.stat().st_size//1000} KB: resúmelo (Gemini lo necesita pequeño, < 60 KB)')
    if (ROOT / '.git').exists():
        import subprocess
        tracked = subprocess.run(['git', 'ls-files'], cwd=ROOT, capture_output=True, text=True).stdout.split()
        extra = sorted(t for t in tracked if t not in ALLOWED)
        fail('Archivos que no deben estar en el repositorio (bórralos): ' + ', '.join(extra)) if extra else ok('Repositorio limpio')

# ---------- 2. Pruebas en navegador ----------
def serve(port):
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a): pass
        def handle(self):
            try: super().handle()
            except (BrokenPipeError, ConnectionResetError): pass
    h = functools.partial(Quiet, directory=str(ROOT))
    srv = http.server.ThreadingHTTPServer(('127.0.0.1', port), h)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv

async def ai_mock(route):
    body = json.loads(route.request.post_data or '{}')
    txt = body['input'][0]['text']
    if 'Responde solo con la palabra OK' in txt: out = 'OK'
    elif 'BIOPEAT_CONFIG' in txt: out = '{"profile":{"weight":78},"summary":"Peso 78"}'
    elif 'BIOPEAT:' in txt: out = 'BIOPEAT:[{"meal":"Comida","name":"Lentejas prueba","grams":300,"kcal":350,"p":20,"c":50,"f":6,"pufa":1.2}]'
    else: out = 'Un vaso de leche y un plátano.'
    await route.fulfill(status=200, content_type='application/json', body=json.dumps({'outputs': [{'type': 'text', 'text': out}]}))

async def browser_checks():
    from playwright.async_api import async_playwright
    port = 8000 + os.getpid() % 900
    serve(port)
    url = f'http://127.0.0.1:{port}/index.html'
    async with async_playwright() as p:
        exe = os.environ.get('CHROMIUM_PATH')
        b = await p.chromium.launch(**({'executable_path': exe} if exe else {}))
        ctx = await b.new_context(viewport={'width': 400, 'height': 850}, reduced_motion='reduce')
        pg = await ctx.new_page()
        await pg.clock.set_fixed_time(NOW)
        errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.on('dialog', lambda d: asyncio.ensure_future(d.accept()))
        await pg.route('https://generativelanguage.googleapis.com/**', ai_mock)
        ev = pg.evaluate
        toast = lambda: ev("document.getElementById('toast').hidden?'':document.getElementById('toast-text').textContent")

        async def load(seed):
            await pg.goto(url)
            await ev("r=>{localStorage.clear(); if(r) localStorage.setItem('biopeat_pro_v10', r)}", seed)
            await pg.reload()
            try:
                await pg.wait_for_function("document.body.dataset.ready==='true'", timeout=10000)
            except Exception:
                raise RuntimeError('la app no termina de arrancar. Errores: ' + (' | '.join(e[:200] for e in errs[:3]) or 'ninguno visible'))
            await pg.wait_for_timeout(300)

        def check_errs(where):
            if errs:
                fail(f'Error de JavaScript en {where}: ' + ' | '.join(e[:200] for e in errs[:3]))
                errs.clear()
                return False
            return True

        print('2. App vacía (usuario nuevo)')
        await load(None)
        if check_errs('arranque vacío'): ok('Arranca sin errores')

        print('3. Datos antiguos (v29) y lectura de macros')
        await load(FIXTURE.read_text(encoding='utf-8'))
        await ev(f"goDate('{DAY}')")
        r = await ev("({kcal:totals().all.kcal,g:dayGoal(),txt:$('energy-current').textContent,ring:$('macro-progress-grid').innerText})")
        if not r['g'] or not r['g'].get('kcal'): fail('dayGoal() no devuelve metas del día')
        elif r['kcal'] <= 0 or r['txt'] in ('', '0'): fail('Hoy no muestra las calorías del día')
        else: ok(f"Hoy lee comidas y metas: {r['txt']} kcal de {round(r['g']['kcal'])}")
        if abs(r['g']['p'] - 145) > 0.5 or abs(r['g']['f'] - 75) > 0.5: fail(f"Plan por defecto de miércoles debería ser 145P/75G y es {r['g']['p']}/{r['g']['f']}")
        else: ok('Plan por defecto correcto (miércoles 145P/75G)')
        if abs(await ev("dayGoal('2026-10-13').p") - 130) > .5: fail('Plan por defecto de martes debería ser 130 g de proteína')
        check_errs('carga de datos antiguos')

        print('4. Guardar y recargar')
        await ev("document.querySelector('[data-preset=breakfast]').click()")
        n = await ev("day().entries.filter(e=>e.kind==='food').length")
        await ev("editTargets()"); await ev("$('target-mode').value='split';$('target-mode').onchange()")
        await ev("(()=>{const f=$('targets-form');f.m_w_p.value=150;f.m_w_f.value=70;f.m_r_p.value=120;f.m_r_f.value=60;f.requestSubmit();})()")
        await pg.wait_for_timeout(400)
        await pg.reload(); await pg.wait_for_function("document.body.dataset.ready==='true'"); await ev(f"goDate('{DAY}')")
        n2 = await ev("day().entries.filter(e=>e.kind==='food').length")
        g = await ev("[state.targetMode,dayGoal().p,dayGoal('2026-10-13').p]")
        fail(f'Las comidas no se guardan al recargar ({n} → {n2})') if n2 != n else ok('Las comidas se guardan al recargar')
        fail(f'Las metas no se guardan al recargar: {g}') if g != ['split', 150, 120] else ok('Las metas se guardan al recargar')
        await ev("$('target-kcal').value=2800;$('target-p').value=140;$('target-f').value=70;$('macro-target-form').requestSubmit()")
        if await ev("dayGoal().kcal") != 2800 or await ev("dayGoal('2026-10-13').p") != 120: fail('El ajuste «solo este día» no funciona')
        else: ok('Ajuste de un solo día correcto')
        await ev("$('target-reset').click()")
        check_errs('guardar/recargar')

        print('5. Añadir comida')
        await ev("$('smart-input').value='200 ml de leche y 2 platanos';$('smart-add').click()"); await pg.wait_for_timeout(300)
        s = await ev("$('meal-ai-status').textContent")
        ok('Texto sin IA reconocido') if 'sin IA' in s else fail('No reconoce «200 ml de leche y 2 platanos» sin IA: ' + s)
        await ev("""$('bp-paste').value='BIOPEAT:{"meal":"Cena","name":"Tortilla","grams":200,"kcal":300,"p":20,"c":5,"f":22,"pufa":2}';$('bp-paste-add').click()""")
        ok('Pegar respuesta de Gemini') if 'Tortilla' in await ev("$('bp-paste-msg').textContent") else fail('No añade la respuesta BIOPEAT pegada')
        await ev("$('ai-mode').value='direct';$('gemini-key').value='CLAVE_DE_PRUEBA';syncAI()")
        await ev("$('smart-input').value='un plato de lentejas';$('smart-add').click()"); await pg.wait_for_timeout(800)
        ok('Texto con IA (simulada)') if 'Guardado' in await ev("$('meal-ai-status').textContent") else fail('El análisis con IA no guarda la comida')
        await ev("document.getElementById('coach-ai-btn').click()"); await pg.wait_for_timeout(600)
        ok('Sugerencia de la IA') if 'leche' in await ev("$('day-coach').innerText") else fail('«Pedir sugerencia a la IA» no muestra nada')
        check_errs('añadir comida')

        print('5b. Equilibrio del día')
        await ev(f"goDate('{DAY}')")
        nr = await ev("document.querySelectorAll('#ratio-summary [data-ratio-key]').length")
        ok('5 equilibrios en Hoy') if nr == 5 else fail(f'Equilibrio del día debería tener 5 tarjetas y tiene {nr}')
        await ev("document.querySelector('[data-ratio-key=c]').click()")
        body = await ev("$('modal-body').innerText")
        ok('Detalle del equilibrio con porqué y cómo') if '¿Por qué importa?' in body and ('Cómo llegar' in body or 'Para mantenerlo' in body) else fail('El detalle del equilibrio no explica el porqué o el cómo')
        fx = await ev("document.querySelectorAll('#modal-body [data-ratio-add]').length")
        if fx:
            n0 = await ev("day().entries.length"); await ev("document.querySelector('#modal-body [data-ratio-add]').click()")
            ok('Añadir la sugerencia del equilibrio') if await ev("day().entries.length") == n0 + 1 else fail('El botón de sugerencia no añade el alimento')
        await ev("$('modal').open&&$('modal').close()")
        check_errs('equilibrio del día')

        print('6. Pauta, gimnasio, semana')
        n0 = await ev("effectiveEntries().filter(e=>e.kind!=='food').length")
        await ev("document.querySelector('[data-supp-skip]').click()")
        n1 = await ev("effectiveEntries().filter(e=>e.kind!=='food').length")
        await ev("document.querySelector('[data-supp-back]').click()")
        n2 = await ev("effectiveEntries().filter(e=>e.kind!=='food').length")
        ok('Quitar y recuperar una toma de hoy') if (n1 == n0 - 1 and n2 == n0) else fail(f'Quitar/recuperar toma no funciona ({n0} → {n1} → {n2})')
        ok('Lo que aporta la pauta') if len(await ev("$('supp-impact').innerHTML")) > 50 else fail('«Lo que te aporta tu pauta» vacío')
        grp = await ev("[...document.querySelectorAll('.supp-slot h3')].map(h=>h.textContent)")
        ok('Pauta agrupada por momentos') if 'Desayuno' in grp and 'Antes de dormir' in grp else fail(f'La pauta no se agrupa por momentos: {grp}')
        csv = 'title,start_time,end_time,exercise_title,set_index,set_type,weight_kg,reps\n"Full body","2026-10-15 18:00:00","2026-10-15 19:00:00","Press de banca",0,normal,80,8\n'
        await pg.set_input_files('#hevy-file', files=[{'name': 'h.csv', 'mimeType': 'text/csv', 'buffer': csv.encode()}]); await pg.wait_for_timeout(300)
        await ev("$('hevy-validate').click()"); await pg.wait_for_timeout(100)
        nw = await ev("state.workouts18.length")
        await ev("$('hevy-commit').click()"); await pg.wait_for_timeout(100)
        ok('Importar CSV de HEVY') if await ev("state.workouts18.length") == nw + 1 else fail('No importa el CSV de HEVY: ' + await ev("$('hevy-status').textContent+' '+$('hevy-previewtext').textContent"))
        await ev("go('exercise')"); await pg.wait_for_timeout(300)
        ok('Gimnasio se dibuja') if len(await ev("$('gp-kpis').innerHTML")) > 50 else fail('Gimnasio vacío')
        await ev("go('week')"); await pg.wait_for_timeout(300)
        ok('Semana se dibuja') if len(await ev("$('week-rings').innerHTML")) > 50 else fail('Semana vacía')
        ok('Día a día con 7 días') if await ev("document.querySelectorAll('#week-strip [data-week-day]').length") == 7 else fail('«Día a día» no tiene 7 días')
        await ev(f"calendarMonth='{DAY[:7]}';calendarSelected='{DAY}';calendarPicked=true;renderCalendar()")
        cal = await ev("({n:document.querySelectorAll('#calendar-grid [data-calday]').length,d:$('calendar-detail').innerText,s:$('calendar-summary').innerHTML.length})")
        ok('Calendario con resumen y ficha del día') if cal['n'] >= 28 and 'Energía' in cal['d'] and cal['s'] > 100 else fail(f'Calendario incompleto: {cal}')
        await ev("document.querySelector('[data-calmetric=p]').click()")
        ok('Calendario cambia de métrica') if 'Proteína' in await ev("$('calendar-summary').innerText") else fail('El selector del calendario no cambia la métrica')
        check_errs('pauta/gimnasio/semana')

        print('7. Pulsar todos los botones')
        await ev("document.querySelectorAll('details').forEach(d=>d.open=true)")
        n = await ev("""()=>{let i=0;document.querySelectorAll('button').forEach(b=>{if(b.closest('dialog')||b.offsetParent===null)return;b.dataset.t=i++;});return i;}""")
        skip = re.compile(r'export|backup|forget|import|clear-foods|bp-clip|menu-backup')
        bad = 0
        for i in range(n):
            info = await ev(f"(()=>{{const b=document.querySelector('[data-t=\"{i}\"]');return b?(b.id||'')+' '+b.textContent.trim().slice(0,30):null}})()")
            if not info or skip.search(info): continue
            try:
                await ev(f"document.querySelector('[data-t=\"{i}\"]').click()")
                await pg.wait_for_timeout(60)
                if await ev("$('modal').open"):
                    await ev("(()=>{const m=$('modal');const bs=[...m.querySelectorAll('button')].filter(x=>!/eliminar|delete/i.test(x.textContent+(x.dataset.deleteworkout||'')+(x.dataset.deletePlan||'')+(x.dataset.deleteFood||'')));for(const x of bs.slice(0,4)){try{x.click()}catch(e){}}})()")
                    await pg.wait_for_timeout(60)
                    await ev("$('modal').open&&$('modal').close()")
            except Exception as ex:
                bad += 1; fail(f'Botón «{info}»: {str(ex)[:120]}')
            if not await ev("typeof $==='function'"):
                bad += 1; fail(f'Botón «{info}» saca de la app (historial): {pg.url}'); await pg.goto(url); await pg.wait_for_function("document.body.dataset.ready==='true'"); await ev("document.querySelectorAll('details').forEach(d=>d.open=true)"); n2=await ev("""()=>{let i=0;document.querySelectorAll('button').forEach(b=>{if(b.closest('dialog')||b.offsetParent===null)return;b.dataset.t=i++;});return i;}""")
            if errs:
                bad += 1; fail(f'Botón «{info}» provoca error: {errs[0][:200]}'); errs.clear()
        ok(f'{n} botones pulsados sin errores') if not bad else None
        await b.close()

async def main():
    static_checks()
    try:
        await browser_checks()
    except ModuleNotFoundError:
        fail('Falta Playwright: pip install playwright && python -m playwright install --with-deps chromium')
    except Exception as ex:
        fail('La prueba en el navegador se detuvo: ' + str(ex).split('\n')[0][:300])
    print()
    if FAILS:
        print(f'FALLOS ({len(FAILS)}):'); [print(' -', f) for f in FAILS]; sys.exit(1)
    print('TODO OK'); sys.exit(0)

asyncio.run(main())

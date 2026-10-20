import re

with open('index.html', 'r') as f:
    content = f.read()

# Fix verify.js to throw errors on toast or attempt
# "En verify.js: haz que cualquier error capturado dentro de attempt(fn) o enviado a toast() durante init(), render() y la ejecución de renderToday(), renderCoach(), renderRatios(), renderSupps(), renderMicros(), renderMicrosForDay(), renderWeekly(), renderCalendar(), renderGym() y renderSettings() (con datos de prueba en state.days y state.workouts18) lance excepción y falle con process.exit(1)."

with open('verify.js', 'r') as f:
    verify_content = f.read()

verify_patch = """
    // Run init and migrate
    if (typeof sandbox.init === 'function') {
      const initResult = sandbox.init();
      if (initResult instanceof Promise) {
        await initResult;
      }
    }
"""

verify_patch_new = """
    // We override toast to throw so we catch errors in views
    sandbox.toast = (msg) => { throw new Error('Toast error: ' + msg); };
    // Override attempt to throw if it catches an error
    sandbox.attempt = (fn) => {
        try {
            const p = fn();
            if (p && typeof p.catch === 'function') p.catch(e => { throw e; });
        } catch(e) {
            throw e;
        }
    };

    if (typeof sandbox.init === 'function') {
      const initResult = sandbox.init();
      if (initResult instanceof Promise) {
        await initResult;
      }
    }

    const testViews = [
        'renderToday', 'renderCoach', 'renderRatios', 'renderSupps', 'renderMicros',
        'renderMicrosForDay', 'renderWeekly', 'renderCalendar', 'renderGym', 'renderSettings'
    ];
    for (const view of testViews) {
        if (typeof sandbox[view] === 'function') {
            sandbox[view]();
        }
    }
"""
verify_content = verify_content.replace(verify_patch, verify_patch_new)

with open('verify.js', 'w') as f:
    f.write(verify_content)

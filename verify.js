const fs = require('fs');
const vm = require('vm');

const startTime = Date.now();

async function run() {
  try {
    const html = fs.readFileSync('index.html', 'utf-8');

    if (!html.trimEnd().endsWith('</html>')) {
      throw new Error('index.html no termina en </html>');
    }

    const protectedFields = [
      'biopeat_pro_v10', 'compare17', 'workouts18', 'favorites22',
      'microTargets17', 'goalOrigin17', 'ratioGoals17',
      'biopeat_lastBackup22', 'biopeat_backupSnooze22', 'biopeat_density19', 'biopeat_ai24'
    ];

    for (const field of protectedFields) {
      if (!html.includes(field)) {
        throw new Error(`Falta el campo protegido: ${field}`);
      }
    }

    const scriptMatch = html.match(/<script id="app">([\s\S]*?)<\/script>/);
    if (!scriptMatch) {
      throw new Error('No se encontró <script id="app">');
    }

    const scriptContent = scriptMatch[1];

    // node --check equivalent: parsing the script
    new vm.Script(scriptContent);

    // Mock environment
    const mockLocalStorage = {
      getItem: (key) => {
        if (key === 'biopeat_state_v20') {
          // Provide valid profile defaults to prevent error in number() during migration
          return JSON.stringify({
            version: 10,
            days: {},
            appRevision: 29,
            profile: { weight: 70, height: 175, age: 30, pufa: 4.5, cap: 1.1 }
          });
        }
        return null;
      },
      setItem: () => {},
      removeItem: () => {}
    };

    class MockEvent {
        constructor(type, options) {
            this.type = type;
        }
    }

    const mockElement = {
      addEventListener: () => {},
      removeEventListener: () => {},
      dispatchEvent: () => true,
      value: '',
      style: {},
      classList: { add: ()=>{}, remove: ()=>{}, toggle: ()=>{}, contains: () => false },
      innerHTML: '',
      dataset: {},
      focus: () => {},
      blur: () => {},
      setAttribute: () => {},
      removeAttribute: () => {},
      getAttribute: () => null,
      appendChild: () => {},
      removeChild: () => {},
      replaceChildren: () => {},
      closest: () => null,
      querySelector: () => mockElement,
      querySelectorAll: () => []
    };

    const sandbox = {
      window: {
        localStorage: mockLocalStorage,
        addEventListener: () => {},
        removeEventListener: () => {},
        dispatchEvent: () => true,
        location: { hash: '' },
        navigator: { serviceWorker: { register: () => Promise.resolve() } },
        scrollTo: () => {},
        requestAnimationFrame: (cb) => { cb(); },
        matchMedia: () => ({ matches: false, addEventListener: () => {} })
      },
      document: {
        getElementById: () => mockElement,
        querySelector: () => mockElement,
        querySelectorAll: () => [],
        addEventListener: () => {},
        removeEventListener: () => {},
        dispatchEvent: () => true,
        createElement: () => mockElement,
        body: mockElement,
        documentElement: mockElement,
        location: { hash: '' },
        activeElement: mockElement
      },
      localStorage: mockLocalStorage,
      console: { log: () => {}, error: () => {}, warn: () => {} },
      setTimeout: (cb) => { cb(); return 1; },
      clearTimeout: () => {},
      setInterval: () => 1,
      clearInterval: () => {},
      fetch: async () => ({ ok: true, json: async () => ({}) }),
      navigator: { serviceWorker: { register: () => Promise.resolve() } },
      location: { hash: '' },
      Math: Math,
      Date: Date,
      JSON: JSON,
      Object: Object,
      Array: Array,
      String: String,
      Number: Number,
      Boolean: Boolean,
      RegExp: RegExp,
      Error: Error,
      Promise: Promise,
      parseInt: parseInt,
      parseFloat: parseFloat,
      isNaN: isNaN,
      isFinite: isFinite,
      encodeURIComponent: encodeURIComponent,
      decodeURIComponent: decodeURIComponent,
      URL: URL,
      Map: Map,
      Set: Set,
      Event: MockEvent,
      CustomEvent: MockEvent,
      FormData: class FormData { append() {} get() { return null; } }
    };

    vm.createContext(sandbox);

    // We execute the script in the sandbox
    vm.runInContext(scriptContent, sandbox);

    // Run init and migrate
    if (typeof sandbox.init === 'function') {
      const initResult = sandbox.init();
      if (initResult instanceof Promise) {
        await initResult;
      }
    }

    if (typeof sandbox.migrate === 'function') {
      // Create a full test v20 state to bypass migrateBase throwing
      sandbox.migrate({
        version: 10,
        days: {},
        appRevision: 29,
        profile: { weight: 70, height: 175, age: 30, pufa: 4.5, cap: 1.1 }
      });
    }

    const duration = Date.now() - startTime;
    if (duration > 1000) {
      throw new Error(`La verificación tardó demasiado: ${duration}ms`);
    }

    console.log(`OK. Validado en ${duration}ms.`);
    process.exit(0);

  } catch (error) {
    console.error(`Error de verificación: ${error.stack}`);
    process.exit(1);
  }
}

run();

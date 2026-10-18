const fs = require('fs');
let content = fs.readFileSync('index.html', 'utf8');

const s = `function ratioDetail(key){
  const t=totals();
  if(key==='pufa'){nutrientDetail('pufa');return;}
  if(key==='ca'){modal('Calcio : fósforo',\`<div class="detail-progress"><strong>\${t.all.phos>0?fmt(t.all.ca/t.all.phos,2)+' : 1':'Sin datos'}</strong><span>Calcio \${fmt(t.all.ca)} mg · Fósforo \${fmt(t.all.phos)} mg</span></div><p class="safe-info">La marca 1,10 es tu preferencia personal. No es un diagnóstico ni una cifra universal verificada de Peat. \${t.missing.ca||t.missing.phos?'Faltan datos en parte de los alimentos.':''}</p><div class="row"><button class="btn btn-slate" data-micro="ca">Ver calcio</button><button class="btn btn-slate" data-micro="phos">Ver fósforo</button></div>\`);return;}
  const g=day().target;modal('Carbohidratos : proteína',\`<div class="detail-progress"><strong>\${t.all.p>0?fmt(t.all.c/t.all.p,2)+' : 1':'Sin datos'}</strong><span>\${fmt(t.all.c,1)} g de carbohidratos / \${fmt(t.all.p,1)} g de proteína alimentaria</span><p class="progress-note">Tu plan de hoy: \${g.p>0?fmt(g.c/g.p,2)+' : 1':'sin objetivo'} (\${fmt(g.c)} g carb. / \${fmt(g.p)} g prot.). Se calcula con tus objetivos del día; cámbialos en Ajustes.</p></div><div class="row"><button class="btn btn-slate" data-macro="c">Ver carbohidratos</button><button class="btn btn-slate" data-macro="p">Ver proteína</button></div><p class="safe-info">Es una relación en gramos, no de calorías ni una medición de glucemia. La glicina libre no se suma a proteína alimentaria.</p>\`);
}`;

const r = `function renderSimulator(type) {
  const t=totals();
  let sim = '<div class="sim-ratios" style="margin-top:16px;display:flex;flex-direction:column;gap:8px;"><strong>Simulador en vivo (añadir a ' + mealByHour() + ')</strong>';
  const opts = type === 'ca' ?
    [{id:'leche_entera', amount: 200, unit:'ml', label: '200 ml Leche entera'}, {id:'parmigiano', amount: 40, unit:'g', label: '40 g Queso'}] :
    [{id:'zumo_naranja', amount: 250, unit:'ml', label: '250 ml Zumo naranja'}, {id:'azucar_blanco', amount: 30, unit:'g', label: '30 g Miel/Azúcar'}, {id:'platano', amount: 1, unit:'ud', label: '1 Plátano (120g)', factor: 120}];
  opts.forEach(o => {
    const f=state.foods[o.id];
    if(!f) return;
    const qty = o.factor || o.amount;
    const ratio = qty / (f.basis||100);
    const n = Object.fromEntries(Object.entries(f.nutrients||{}).map(([k,v])=>[k,v*ratio]));
    let newRatioText = '';
    if (type === 'ca') {
      const newCa = t.all.ca + (n.ca||0);
      const newP = t.all.phos + (n.phos||0);
      newRatioText = newP>0 ? fmt(newCa/newP,2) : '—';
    } else {
      const newC = t.all.c + (n.c||0);
      const newProt = t.all.p + (n.p||0);
      newRatioText = newProt>0 ? fmt(newC/newProt,2) : '—';
    }
    const ratioId = type==='ca'?'Ca:P':'C:P';
    sim += \`<button class="btn btn-sky" style="font-size:13px;padding:8px;justify-content:start" onclick="const m=mealByHour();addEntries([{...quickTemplate(state.foods['\${o.id}']),amount:\${qty},meal:m}],'Añadido a '+m+': \${o.label} (Simulador)');$('modal').close();render();">+ \${o.label} (\${ratioId} pasa a \${newRatioText})</button>\`;
  });
  sim += '</div>';
  return sim;
}
function ratioDetail(key){
  const t=totals();
  if(key==='pufa'){nutrientDetail('pufa');return;}
  if(key==='ca'){modal('Calcio : fósforo',\`<div class="detail-progress"><strong>\${t.all.phos>0?fmt(t.all.ca/t.all.phos,2)+' : 1':'Sin datos'}</strong><span>Calcio \${fmt(t.all.ca)} mg · Fósforo \${fmt(t.all.phos)} mg</span></div>\${renderSimulator('ca')}<p class="safe-info">La marca 1,10 es tu preferencia personal. No es un diagnóstico ni una cifra universal verificada de Peat. \${t.missing.ca||t.missing.phos?'Faltan datos en parte de los alimentos.':''}</p><div class="row"><button class="btn btn-slate" data-micro="ca">Ver calcio</button><button class="btn btn-slate" data-micro="phos">Ver fósforo</button></div>\`);return;}
  const g=day().target;modal('Carbohidratos : proteína',\`<div class="detail-progress"><strong>\${t.all.p>0?fmt(t.all.c/t.all.p,2)+' : 1':'Sin datos'}</strong><span>\${fmt(t.all.c,1)} g de carbohidratos / \${fmt(t.all.p,1)} g de proteína alimentaria</span><p class="progress-note">Tu plan de hoy: \${g.p>0?fmt(g.c/g.p,2)+' : 1':'sin objetivo'} (\${fmt(g.c)} g carb. / \${fmt(g.p)} g prot.). Se calcula con tus objetivos del día; cámbialos en Ajustes.</p></div>\${renderSimulator('c')}<div class="row"><button class="btn btn-slate" data-macro="c">Ver carbohidratos</button><button class="btn btn-slate" data-macro="p">Ver proteína</button></div><p class="safe-info">Es una relación en gramos, no de calorías ni una medición de glucemia. La glicina libre no se suma a proteína alimentaria.</p>\`);
}`;

content = content.replace(s, r);
fs.writeFileSync('index.html', content);
console.log("Ratio Detail patch applied");

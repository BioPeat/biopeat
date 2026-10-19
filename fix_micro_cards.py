import re
with open('index.html', 'r') as f:
    content = f.read()

# Update microStat logic to respect these limits across Today and Micros cards
microStatOrig = """function microStat(m,t=totals()){
  const kind=microKind(m.k),goal=state.targets[m.k];
  if(DEPOSIT.has(m.k)){const r=rollingMicro(m.k);return {kind,dep:true,goal,value:r.value,food:r.food,supp:r.supp,planned:r.planned,partial:false,known:r.known};}
  const known=t.known[m.k]>0,value=t.all[m.k]||0,food=t.food[m.k]||0,supp=t.supp[m.k]||0,planned=t.planned[m.k]||0,partial=t.missing[m.k]>0;
  return {kind,dep:false,goal,value,food,supp,planned,partial,known};
}"""

microStatNew = """function microStat(m,t=totals()){
  const kind=microKind(m.k),goal=state.targets[m.k];
  if(DEPOSIT.has(m.k)){const r=rollingMicro(m.k);return {kind,dep:true,goal,value:r.value,food:r.food,supp:r.supp,planned:r.planned,partial:false,known:r.known};}
  const known=t.known[m.k]>0,value=t.all[m.k]||0,food=t.food[m.k]||0,supp=t.supp[m.k]||0,planned=t.planned[m.k]||0,partial=t.missing[m.k]>0;
  return {kind,dep:false,goal,value,food,supp,planned,partial,known};
}"""

# Actually modify tone logic in renderMicroCards or general logic
# The easiest way is to modify renderMicroCards directly
renderMicroCardsOrig = """function renderMicroCards(){
  const t=totals(),d=day(),g=d.target,personal=$('micro-mode').value==='personal',visible=MICRO.filter(m=>microFilter==='all'||m.group===microFilter);
  $('micros-grid').innerHTML=visible.map(m=>{const x=microStat(m,t),goal=personal?x.goal:m.target,pct=goal?x.value/goal*100:null;return `<button class="micro-card ${x.known?tone(pct,m.k==='fe'?'budget':'micro'):'unknown'}" data-micro="${m.k}" data-daymetric="${m.k}" data-daymetricdate="${date}" aria-label="${m.name}: ${x.known?fmt(x.value,2):'sin dato'} ${m.unit}${pct!=null?', '+fmt(pct)+' por ciento de tu pauta':''}. Alimentos: ${fmt(x.food,2)}. Suplementos: ${fmt(x.supp,2)}"><div class="row between"><span class="name">${m.name} ${kindTag(m.k)}</span><strong>${pct!=null&&x.known?fmt(pct)+'%':'—'}</strong></div><div class="row baseline"><span><span data-current>${x.known?fmt(x.value,2):'—'}</span> <small data-unit>${m.unit}</small></span><span class="micro-goal" data-goal>${goal?'/ '+fmt(goal)+' ':''}</span></div><div class="micro-bar" aria-hidden="true"><div class="micro-progress"><div class="micro-food" style="width:${goal?Math.min(100,x.food/goal*100):x.known?100:0}%"></div><div class="micro-supp" style="width:${goal?Math.min(100-Math.min(100,x.food/goal*100),x.supp/goal*100):0}%"></div><div class="micro-overflow" hidden><span style="width:0%"></span></div></div></div><div class="micro-split"><span data-food>Alimentos: ${fmt(x.food,2)}</span><span data-supp>${x.supp>0||x.planned>0?x.planned>x.supp?'Previstos: '+fmt(x.planned,2):'Suplementos: '+fmt(x.supp,2):'Pauta: 0'}</span></div><div class="micro-status" data-status>${x.known?x.partial?'Faltan datos en algunos alimentos':x.dep?'Depósito de 7 días (media)':'Dosis del día completa':'Sin registro hoy'}</div></button>`;}).join('');
}"""

renderMicroCardsNew = """function renderMicroCards(){
  const t=totals(),d=day(),g=d.target,personal=$('micro-mode').value==='personal',visible=MICRO.filter(m=>microFilter==='all'||m.group===microFilter);
  $('micros-grid').innerHTML=visible.map(m=>{const x=microStat(m,t),goal=personal?x.goal:m.target,pct=goal?x.value/goal*100:null;
  let cssTone=tone(pct,LIMIT.has(m.k)?'budget':'micro'), status=x.known?x.partial?'Faltan datos en algunos alimentos':x.dep?'Depósito de 7 días (media)':'Dosis del día completa':'Sin registro hoy';
  if(x.known) {
    if(m.k==='se') {
      if(x.value>=100&&x.value<=200) cssTone='macro-ok'; else if(x.value>200) cssTone='macro-over';
      if(x.value>200) status='Exceso satura desyodinasa y frena T3.';
    } else if(m.k==='vitA') {
      if(x.value>3800) {cssTone='macro-over'; status='Aviso: posible freno a tiroides >3800.';}
    } else if(m.k==='i') {
      if(x.value>225) {cssTone='macro-over'; status='Exceso de yodo detectado.';}
    } else if(m.k==='fe') {
      if(x.value<=14) cssTone='macro-ok'; else cssTone='macro-over';
      status='Límite estricto ≤ 14 mg/d.';
    }
  }
  return `<button class="micro-card ${x.known?cssTone:'unknown'}" data-micro="${m.k}" data-daymetric="${m.k}" data-daymetricdate="${date}" aria-label="${m.name}: ${x.known?fmt(x.value,2):'sin dato'} ${m.unit}${pct!=null?', '+fmt(pct)+' por ciento de tu pauta':''}. Alimentos: ${fmt(x.food,2)}. Suplementos: ${fmt(x.supp,2)}"><div class="row between"><span class="name">${m.name} ${kindTag(m.k)}</span><strong>${pct!=null&&x.known?fmt(pct)+'%':'—'}</strong></div><div class="row baseline"><span><span data-current>${x.known?fmt(x.value,2):'—'}</span> <small data-unit>${m.unit}</small></span><span class="micro-goal" data-goal>${goal?'/ '+fmt(goal)+' ':''}</span></div><div class="micro-bar" aria-hidden="true"><div class="micro-progress"><div class="micro-food" style="width:${goal?Math.min(100,x.food/goal*100):x.known?100:0}%"></div><div class="micro-supp" style="width:${goal?Math.min(100-Math.min(100,x.food/goal*100),x.supp/goal*100):0}%"></div><div class="micro-overflow" hidden><span style="width:0%"></span></div></div></div><div class="micro-split"><span data-food>Alimentos: ${fmt(x.food,2)}</span><span data-supp>${x.supp>0||x.planned>0?x.planned>x.supp?'Previstos: '+fmt(x.planned,2):'Suplementos: '+fmt(x.supp,2):'Pauta: 0'}</span></div><div class="micro-status" data-status>${status}</div></button>`;}).join('');
}"""

content = content.replace(renderMicroCardsOrig, renderMicroCardsNew)
with open('index.html', 'w') as f:
    f.write(content)

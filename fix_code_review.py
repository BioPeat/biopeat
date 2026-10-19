import re
with open('index.html', 'r') as f:
    content = f.read()

# 1. Update Epley formula in gpSessionMetrics
mE1rm_orig = r"m.e1rm=e.type==='weighted'\?Math\.max\(0,\.\.\.withReps\.filter\(x=>w\(x\)>0&&x\.reps<=12\)\.map\(x=>w\(x\)\*\(1\+x\.reps/30\)\)\)\|\|null:null;"
mE1rm_new = "m.e1rm=e.type==='weighted'?Math.max(0,...withReps.filter(x=>w(x)>0).map(x=>w(x)*(1+x.reps/30)))||null:null;"
content = re.sub(mE1rm_orig, mE1rm_new, content)

# 2. Update micro limits UI in renderWeekMicros
weekMicrosOrig = """const visible=MICRO.filter(m=>weekMicroFilter==='all'||m.group===weekMicroFilter);
  $('week-micros').innerHTML=visible.map(m=>{const a=aggregate(m.k,s),name=m.k==='b1'?'B1 / benfotiamina':m.name,unit=m.k==='b1'?'mg de compuesto':m.unit;return `<button class="week-micro-card ${tone(a.pct,m.k==='fe'?'budget':'micro')}" data-weekdetail="${m.k}"><div class="row between"><b>${name}</b><strong>${pctText(a)}</strong></div><span>${a.known?fmt(a.value,2):'—'} ${unit}</span>${weekProgress(a,'#6ee7b7')}<p>Meta ${a.goal?fmt(a.goal,2)+' '+unit:'sin definir'}</p><small>${a.known}/${s.included.length} días con dato${a.partial?' · parcial':''}${a.planned?' · incluye previstos':''}</small>${m.k==='b1'?'<small>Tiamina alimentaria aparte: '+fmt(s.included.reduce((sum,r)=>sum+r.t.food.b1,0),2)+' mg · puede ser parcial</small>':''}</button>`;}).join('');"""

weekMicrosNew = """const visible=MICRO.filter(m=>weekMicroFilter==='all'||m.group===weekMicroFilter);
  $('week-micros').innerHTML=visible.map(m=>{const a=aggregate(m.k,s),name=m.k==='b1'?'B1 / benfotiamina':m.name,unit=m.k==='b1'?'mg de compuesto':m.unit;
    let extra='', t=tone(a.pct,LIMIT.has(m.k)?'budget':'micro');
    if(m.k==='se') {
      const v=a.value;
      if(v>=100&&v<=200) t='macro-ok'; else if(v>200) t='macro-over';
      if(v>200) extra='<small class="macro-over">Exceso satura desyodinasa y frena T3.</small>';
      else extra='<small>Óptimo 100-200 ug/d.</small>';
    } else if(m.k==='vitA') {
      if(a.value>3800) {t='macro-over'; extra='<small class="macro-over">Aviso: posible freno a tiroides >3800.</small>';}
    } else if(m.k==='i') {
      if(a.value>225) {t='macro-over'; extra='<small class="macro-over">Exceso de yodo detectado.</small>';}
    } else if(m.k==='fe') {
      if(a.value<=14) t='macro-ok'; else t='macro-over';
      extra='<small>Límite estricto ≤ 14 mg/d.</small>';
    }
    return `<button class="week-micro-card ${t}" data-weekdetail="${m.k}"><div class="row between"><b>${name}</b><strong>${pctText(a)}</strong></div><span>${a.known?fmt(a.value,2):'—'} ${unit}</span>${weekProgress(a,'#6ee7b7')}<p>Meta ${a.goal?fmt(a.goal,2)+' '+unit:'sin definir'}</p><small>${a.known}/${s.included.length} días con dato${a.partial?' · parcial':''}${a.planned?' · incluye previstos':''}</small>${m.k==='b1'?'<small>Tiamina alimentaria aparte: '+fmt(s.included.reduce((sum,r)=>sum+r.t.food.b1,0),2)+' mg · puede ser parcial</small>':''}${extra}</button>`;}).join('');"""

content = content.replace(weekMicrosOrig, weekMicrosNew)

with open('index.html', 'w') as f:
    f.write(content)

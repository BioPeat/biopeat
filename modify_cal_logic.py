import re
with open('index.html', 'r') as f:
    content = f.read()

cellOrig = """function calendarCell(dt){
  const today=localDate(),d=state.days[dt],entries=entriesFor(d),t=totals(entries),g=goalsFor(dt).macro,has=entries.some(e=>e.kind==='food'),future=dt>today;
  const pufaLimit=d?.ratioGoals17?.pufa??state.profile.pufa;
  let css='calendar-day',content='',aria='Sin registro';
  if(dt===today)css+=' today';
  if(dt===calendarSelected)css+=' selected';
  if(has){
    const overKcal=t.all.kcal>g.kcal*1.1,underKcal=t.all.kcal<g.kcal*.9;
    if(calendarMetric==='macro'){
      const pctP=g.p?t.all.p/g.p*100:0,pctF=g.f?t.all.f/g.f*100:0;
      const okP=pctP>=80&&pctP<=120,okF=pctF>=80&&pctF<=120;
      css+=' '+(overKcal?'macro-over':okP&&okF&&!underKcal?'macro-ok':'macro-under');
      content=`<span class="cal-kcal">${fmt(t.all.kcal)}</span><div class="cal-dots"><span class="cal-dot ${tone(pctP,'micro')}"></span><span class="cal-dot ${tone(pctF,'micro')}"></span><span class="cal-dot ${underKcal?'under':overKcal?'over':'ok'}"></span></div>`;
      aria=`${fmt(t.all.kcal)} kcal. P ${Math.round(pctP)}%, F ${Math.round(pctF)}%.`;
    }else if(calendarMetric==='pufa'){
      const overPufa=t.all.pufa>pufaLimit;
      css+=' '+(overPufa?'macro-over':t.all.pufa>=pufaLimit*.8?'macro-ok':'macro-under');
      content=`<span class="cal-kcal">${fmt(t.all.pufa,1)}g</span><div class="cal-dots"><span class="cal-dot ${overPufa?'over':'ok'}" style="width:100%"></span></div>`;
      aria=`PUFA: ${fmt(t.all.pufa,1)} g. Límite: ${pufaLimit} g.`;
    }else{
      const cap=t.all.ca/Math.max(1,t.all.phos),capRef=d?.ratioGoals17?.cap??state.profile.cap??1.1;
      const okCap=cap>=capRef;
      css+=' '+(okCap?'macro-ok':'macro-under');
      content=`<span class="cal-kcal">${fmt(cap,2)}</span><div class="cal-dots"><span class="cal-dot ${okCap?'ok':'under'}" style="width:100%"></span></div>`;
      aria=`Ca:P: ${fmt(cap,2)}. Meta: ${capRef}.`;
    }
    if(d.complete)content+='<span class="cal-complete" aria-hidden="true">✓</span>';
  }else if(future){
    css+=' future';
    content=`<span class="cal-kcal">Pv.</span>`;
    aria='Día futuro, plan previsto';
  }else if(d&&d.entries.length){
    content=`<span class="cal-kcal">Pauta</span>`;
    aria='Solo pauta o notas';
  }
  return `<button type="button" class="${css}" data-calday="${dt}" aria-label="${dt}: ${aria}"><span class="cal-d">${dt.slice(8)}</span>${content}</button>`;
}"""

cellNew = """function calendarCell(dt){
  const today=localDate(),d=state.days[dt],entries=entriesFor(d),t=totals(entries),g=goalsFor(dt).macro,has=entries.some(e=>e.kind==='food'),future=dt>today;
  const pufaLimit=d?.ratioGoals17?.pufa??state.profile.pufa;
  let css='calendar-day',content='',aria='Sin registro';
  if(dt===today)css+=' today';
  if(dt===calendarSelected)css+=' selected';
  if(has){
    const overKcal=t.all.kcal>g.kcal*1.1,underKcal=t.all.kcal<g.kcal*.9;
    const pctP=g.p?t.all.p/g.p*100:0,pctF=g.f?t.all.f/g.f*100:0;
    const okP=pctP>=80&&pctP<=120,okF=pctF>=80&&pctF<=120;

    // Gym/Pauta dot
    const hasGym=d.entries.some(e=>e.kind==='workout');
    const dotGym=hasGym?'ok':'under';

    // Ratios Peat dot
    const cap=t.all.ca/Math.max(1,t.all.phos),capRef=d?.ratioGoals17?.cap??state.profile.cap??1.1;
    const cp=t.all.p>0?t.all.c/t.all.p:0;
    const okPeat=cap>=capRef&&t.all.pufa<=pufaLimit&&cp>=3.0;
    const dotPeat=okPeat?'ok':(t.all.pufa>pufaLimit?'over':'under');

    if(calendarMetric==='macro'){
      css+=' '+(overKcal?'macro-over':okP&&okF&&!underKcal?'macro-ok':'macro-under');
      content=`<span class="cal-kcal">${fmt(t.all.kcal)}</span><div class="cal-dots"><span class="cal-dot ${tone(pctP,'micro')}"></span><span class="cal-dot ${tone(pctF,'micro')}"></span><span class="cal-dot ${underKcal?'under':overKcal?'over':'ok'}"></span></div>`;
      aria=`${fmt(t.all.kcal)} kcal. P ${Math.round(pctP)}%, F ${Math.round(pctF)}%.`;
    }else if(calendarMetric==='peat'){
      css+=' '+(okPeat?'macro-ok':(t.all.pufa>pufaLimit?'macro-over':'macro-under'));
      content=`<span class="cal-kcal">${okPeat?'OK':'Revisar'}</span><div class="cal-dots"><span class="cal-dot ${okP&&okF?'ok':'under'}"></span><span class="cal-dot ${dotPeat}"></span><span class="cal-dot ${dotGym}"></span></div>`;
      aria=`Peat: ${okPeat?'OK':'Revisar'}. Macros: ${okP&&okF?'OK':'No'}, Ratios: ${okPeat?'OK':'No'}, Gym: ${hasGym?'Sí':'No'}.`;
    }else if(calendarMetric==='gym'){
      css+=' '+(hasGym?'macro-ok':'macro-under');
      content=`<span class="cal-kcal">${hasGym?'Gym':'-'}</span><div class="cal-dots"><span class="cal-dot ${dotGym}" style="width:100%"></span></div>`;
      aria=`Entreno: ${hasGym?'Sí':'No'}.`;
    }else{
      css+=' '+(overKcal?'macro-over':okP&&okF&&!underKcal?'macro-ok':'macro-under');
      content=`<span class="cal-kcal">${fmt(t.all.kcal)}</span><div class="cal-dots"><span class="cal-dot ${tone(pctP,'micro')}"></span><span class="cal-dot ${tone(pctF,'micro')}"></span><span class="cal-dot ${underKcal?'under':overKcal?'over':'ok'}"></span></div>`;
      aria=`${fmt(t.all.kcal)} kcal. P ${Math.round(pctP)}%, F ${Math.round(pctF)}%.`;
    }
    if(d.complete)content+='<span class="cal-complete" aria-hidden="true">✓</span>';
  }else if(future){
    css+=' future';
    content=`<span class="cal-kcal">Pv.</span>`;
    aria='Día futuro, plan previsto';
  }else if(d&&d.entries.length){
    content=`<span class="cal-kcal">Pauta</span>`;
    aria='Solo pauta o notas';
  }
  return `<button type="button" class="${css}" data-calday="${dt}" aria-label="${dt}: ${aria}"><span class="cal-d">${dt.slice(8)}</span>${content}</button>`;
}"""

content = content.replace(cellOrig, cellNew)
with open('index.html', 'w') as f:
    f.write(content)

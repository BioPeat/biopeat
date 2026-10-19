import re
with open('index.html', 'r') as f:
    content = f.read()

ratiosOrig = """function renderRatios(){
  const t=totals(),d=day(),g=d.target,capRef=d.ratioGoals17?.cap??state.profile.cap??1.1,pufaRef=d.ratioGoals17?.pufa??state.profile.pufa;
  const cap=t.known.ca&&t.all.phos>0?t.all.ca/t.all.phos:null,cp=t.all.p>0&&t.all.c>0?t.all.c/t.all.p:null,cpRef=g.p>0?g.c/g.p:null,pufa=t.known.pufa?t.all.pufa:null;
  const cpMax=Math.max(4,Math.ceil((cpRef||2)*2));
  $('ratio-summary').innerHTML=[
    ratioGauge({key:'ca',name:'Calcio : fósforo',value:cap,label:cap==null?'Sin datos':fmt(cap,2)+' : 1',min:0,max:2,ref:capRef,zone:[capRef,2],ok:v=>v>=capRef,ticks:['0','1','2'],chip:(k,o)=>!k?'Sin datos':o?'✓ En tu referencia':'Por debajo',foot:`Tu referencia: ≥ ${fmt(capRef,2)} : 1 · Ca ${fmt(t.all.ca)} mg / P ${fmt(t.all.phos)} mg${t.missing.ca||t.missing.phos?' · parcial':''}`}),
    ratioGauge({key:'pufa',name:'PUFA · presupuesto',value:pufa,label:pufa==null?'Sin datos':fmt(pufa,1)+' de '+fmt(pufaRef,1)+' g',min:0,max:pufaRef*2,ref:pufaRef,zone:[0,pufaRef],ok:v=>v<=pufaRef,ticks:['0 g',fmt(pufaRef,1)+' g',fmt(pufaRef*2,1)+' g'],chip:(k,o)=>!k?'Sin datos':o?'✓ Quedan '+fmt(pufaRef-pufa,1)+' g':'+'+fmt(pufa-pufaRef,1)+' g sobre el límite',foot:`Tu límite máximo del día: ${fmt(pufaRef,1)} g. Menos es mejor.${t.missing.pufa?' · '+t.missing.pufa+' alimentos sin dato':''}`}),
    ratioGauge({key:'c',name:'Hidratos por cada g de proteína',value:cp,label:cp==null?'Sin datos':fmt(cp,1)+' g',min:0,max:cpMax,ref:cpRef||0,zone:cpRef?[cpRef*.8,Math.min(cpMax,cpRef*1.2)]:[0,0],ok:v=>cpRef?v>=cpRef*.8&&v<=cpRef*1.2:true,ticks:['0',String(cpMax/2),String(cpMax)],chip:(k,o)=>!k?'Sin datos':o?'✓ Cerca de tu plan':cp<cpRef?'Pocos carbohidratos':'Muchos carbohidratos',foot:`Llevas ${fmt(t.all.c)} g de hidratos y ${fmt(t.all.p)} g de proteína. Tu plan de hoy: ${cpRef?fmt(cpRef,1)+' g de hidratos por cada g de proteína ('+fmt(g.c)+' / '+fmt(g.p)+' g)':'sin objetivo'}. Verde = ±20 %.`})
  ].join('');
}"""

ratiosNew = """function renderRatios(){
  const t=totals(),d=day(),g=d.target,capRef=d.ratioGoals17?.cap??state.profile.cap??1.1,pufaRef=d.ratioGoals17?.pufa??state.profile.pufa;
  const cap=t.known.ca&&t.all.phos>0?t.all.ca/t.all.phos:null,cp=t.all.p>0&&t.all.c>0?t.all.c/t.all.p:null,cpRef=state.ratioGoals17?.cp??3.0,pufa=t.known.pufa?t.all.pufa:null;
  const vitA=t.all.vitA||0,vitD=t.all.vitD||0,ad=vitA>0?(vitA*3.33)/Math.max(1,vitD*40):null;
  const zn=t.all.zn||0,cu=t.all.cu||0,zncu=cu>0?zn/cu:null;
  const cpMax=Math.max(4,Math.ceil((cpRef||3)*2));
  $('ratio-summary').innerHTML=[
    ratioGauge({key:'ca',name:'Calcio : fósforo',value:cap,label:cap==null?'Sin datos':fmt(cap,2)+' : 1',min:0,max:2,ref:capRef,zone:[capRef,2],ok:v=>v>=capRef,ticks:['0','1','2'],chip:(k,o)=>!k?'Sin datos':o?'✓ En tu referencia':'Por debajo',foot:`Tu referencia: ≥ ${fmt(capRef,2)} : 1 · Ca ${fmt(t.all.ca)} mg / P ${fmt(t.all.phos)} mg${t.missing.ca||t.missing.phos?' · parcial':''}`}),
    ratioGauge({key:'pufa',name:'PUFA · presupuesto',value:pufa,label:pufa==null?'Sin datos':fmt(pufa,1)+' de '+fmt(pufaRef,1)+' g',min:0,max:pufaRef*2,ref:pufaRef,zone:[0,pufaRef],ok:v=>v<=pufaRef,ticks:['0 g',fmt(pufaRef,1)+' g',fmt(pufaRef*2,1)+' g'],chip:(k,o)=>!k?'Sin datos':o?'✓ Quedan '+fmt(pufaRef-pufa,1)+' g':'+'+fmt(pufa-pufaRef,1)+' g sobre el límite',foot:`Tu límite máximo del día: ${fmt(pufaRef,1)} g. Menos es mejor.${t.missing.pufa?' · '+t.missing.pufa+' alimentos sin dato':''}`}),
    ratioGauge({key:'c',name:'Hidratos por cada g de proteína',value:cp,label:cp==null?'Sin datos':fmt(cp,1)+' : 1',min:0,max:cpMax,ref:cpRef,zone:[3.0,4.0],ok:v=>v>=3.0,ticks:['0','3','6'],chip:(k,o)=>!k?'Sin datos':o?'✓ C:P óptimo':cp<3.0?'Pocos carbohidratos':'Muchos carbohidratos',foot:`Meta C:P ≥ 3.0 : 1. Llevas ${fmt(t.all.c)} g de hidratos y ${fmt(t.all.p)} g de proteína.`}),
    ratioGauge({key:'ad',name:'Equilibrio A:D (UI)',value:ad,label:ad==null?'Sin datos':fmt(ad,1)+' : 1',min:0,max:10,ref:3,zone:[2.0,4.0],ok:v=>v<=5.0,ticks:['0','5','10'],chip:(k,o)=>!k?'Sin datos':ad>5.0?'Exceso de A frena tiroides':'Equilibrio A:D OK',foot:`Meta 2.0-4.0 : 1. Aviso si > 5.0. Vit A: ${fmt(vitA)} ug RAE / Vit D: ${fmt(vitD)} ug.`}),
    ratioGauge({key:'zncu',name:'Equilibrio Zn:Cu',value:zncu,label:zncu==null?'Sin datos':fmt(zncu,1)+' : 1',min:0,max:20,ref:10,zone:[8.0,12.0],ok:v=>v>=8.0&&v<=12.0,ticks:['0','10','20'],chip:(k,o)=>!k?'Sin datos':o?'✓ Respiración mitocondrial OK':'Desequilibrio',foot:`Meta ~10:1 (citocromo c oxidasa). Zn: ${fmt(zn,1)} mg / Cu: ${fmt(cu,1)} mg.`})
  ].join('');
}"""

content = content.replace(ratiosOrig, ratiosNew)
with open('index.html', 'w') as f:
    f.write(content)

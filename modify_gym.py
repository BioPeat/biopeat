import re
with open('index.html', 'r') as f:
    content = f.read()

statusOrig = """function gpStatus(e){
  const h=e.hist;if(h.length<3)return {c:'new',t:'Pocos datos'};
  const k=e.type==='weighted'?'e1rm':e.type==='assisted'?'assist':e.type==='time'?'maxDur':e.type==='bodyweight'?'bestReps':'top';
  const vals=h.map(x=>k==='top'?(x.top||0)*100+(x.repsAtTop||0):x[k]).filter(v=>v!=null);
  if(vals.length<3)return {c:'new',t:'Pocos datos'};
  const low=k==='assist',best=low?Math.min(...vals):Math.max(...vals);
  let since=0;for(let i=vals.length-1;i>=0;i--){if(vals[i]===best)break;since++;}
  const avg=a=>a.reduce((s,v)=>s+v,0)/a.length,recent=vals.slice(-3),older=vals.slice(-6,-3);
  if(since===0)return {c:'up',t:'En récord'};
  if(older.length){const d=(avg(recent)-avg(older))/Math.abs(avg(older)||1)*(low?-1:1);if(d>0.015)return {c:'up',t:'Progresando'};if(d<-0.03)return {c:'down',t:'Bajando'};}
  return since>=4?{c:'flat',t:'Estancado · '+since+' sesiones sin récord'}:{c:'flat',t:'Estable'};
}"""

statusNew = """function gpStatus(e){
  const h=e.hist;if(h.length<2)return {c:'new',t:'Pocos datos'};
  const k=e.type==='weighted'?'e1rm':e.type==='assisted'?'assist':e.type==='time'?'maxDur':e.type==='bodyweight'?'bestReps':'top';
  const vals=h.map(x=>k==='top'?(x.top||0)*100+(x.repsAtTop||0):x[k]).filter(v=>v!=null);
  if(vals.length<2)return {c:'new',t:'Pocos datos'};
  const low=k==='assist',best=low?Math.min(...vals):Math.max(...vals);

  if(k==='e1rm'&&vals.length>=2){
    const curr=vals[vals.length-1],prev=vals[vals.length-2];
    if(curr>prev)return {c:'up',t:'Progresión (+1RM)'};
  }

  let since=0;for(let i=vals.length-1;i>=0;i--){if(vals[i]===best)break;since++;}
  const avg=a=>a.reduce((s,v)=>s+v,0)/a.length,recent=vals.slice(-3),older=vals.slice(-6,-3);
  if(since===0)return {c:'up',t:'En récord'};
  if(older.length){const d=(avg(recent)-avg(older))/Math.abs(avg(older)||1)*(low?-1:1);if(d>0.015)return {c:'up',t:'Progresando'};if(d<-0.03)return {c:'down',t:'Bajando'};}
  return since>=4?{c:'flat',t:'Estancado · '+since+' sesiones sin récord'}:{c:'flat',t:'Estable'};
}"""

content = content.replace(statusOrig, statusNew)
with open('index.html', 'w') as f:
    f.write(content)

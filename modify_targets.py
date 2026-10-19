import re
with open('index.html', 'r') as f:
    content = f.read()

targetFor_orig = """function targetFor(d){
  if(!state||!state.profile)return {kcal:0,p:0,c:0,f:0,activity:weekday(d)};
  const i=weekday(d),w=state.profile.weight/77.5,act=FAF[i];
  let p,f,kcal,c;
  const tM=state.targetMode||'all';
  let mG=null;
  if(tM==='today'&&state.days[d]&&state.days[d].macroGoals)mG=state.days[d].macroGoals;
  else if(tM==='split'&&state.macroGoals&&state.macroGoals.split)mG=[0,2,5,6].includes(i)?state.macroGoals.split.workout:state.macroGoals.split.rest;
  else if(tM==='all'&&state.macroGoals&&state.macroGoals.all)mG=state.macroGoals.all;

  if(mG&&mG.p!=null&&mG.f!=null){
    p=mG.p;
    f=mG.f;
    kcal=Math.round(bmr()*act/5)*5; // Usamos el BMR para el total kcal
    c=(kcal-p*4-f*9)/4;
  } else {
    kcal=Math.round(bmr()*act/5)*5;
    p=[165,150,165,150,150,160,160][i]*w;
    f=[90,85,90,85,85,90,85][i]*w;
    c=(kcal-p*4-f*9)/4;
  }
  return {kcal,p,c,f,activity:i};
}"""

targetFor_new = """function targetFor(d){
  if(!state||!state.profile)return {kcal:0,p:0,c:0,f:0,activity:weekday(d)};
  const i=weekday(d),w=state.profile.weight/77.5,act=FAF[i];
  let p,f,kcal,c;
  const tM=state.targetMode||'all';
  let mG=null;
  if(tM==='today'&&state.days[d]&&state.days[d].macroGoals)mG=state.days[d].macroGoals;
  else if(tM==='split'&&state.macroGoals&&state.macroGoals.split)mG=[0,2,5,6].includes(i)?state.macroGoals.split.workout:state.macroGoals.split.rest;
  else if(tM==='all'&&state.macroGoals&&state.macroGoals.all)mG=state.macroGoals.all;

  if(mG&&mG.p!=null&&mG.f!=null){
    p=mG.p;
    f=mG.f;
    kcal=Math.round(bmr()*act/5)*5;
    c=Math.max(0,(kcal-p*4-f*9)/4);
  } else {
    kcal=Math.round(bmr()*act/5)*5;
    p=[165,150,165,150,150,160,160][i]*w;
    f=[90,85,90,85,85,90,85][i]*w;
    c=Math.max(0,(kcal-p*4-f*9)/4);
  }
  return {kcal,p,c,f,activity:i};
}"""

content = content.replace(targetFor_orig, targetFor_new)

goalsFor_orig = """function goalsFor(dt){
  const d=state.days[dt];
  return {macro:d?.target||targetFor(dt),micro:d?.microTargets17||state.targets,ratio:d?.ratioGoals17||{cap:state.profile.cap??1.1,pufa:state.profile.pufa},reference:!d||d.goalOrigin17!=='saved'};
}"""

goalsFor_new = """function goalsFor(dt){
  const d=state.days[dt];
  const tM=state.targetMode||'all';
  return {macro:tM==='split'||tM==='all'?targetFor(dt):d?.target||targetFor(dt),micro:d?.microTargets17||state.targets,ratio:(tM==='split'||tM==='all')?{cap:state.profile.cap??1.1,pufa:state.profile.pufa}:(d?.ratioGoals17||{cap:state.profile.cap??1.1,pufa:state.profile.pufa}),reference:!d||d.goalOrigin17!=='saved'};
}"""

content = content.replace(goalsFor_orig, goalsFor_new)

with open('index.html', 'w') as f:
    f.write(content)

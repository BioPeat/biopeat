import re
with open('index.html', 'r') as f:
    content = f.read()

onClickOrig = """$('btn-prometabolic').onclick=()=>{
  attempt(()=>{
    change(()=>{
      state.targetMode='split';
      if(!state.macroGoals)state.macroGoals={all:{p:null,f:null},split:{workout:{p:null,f:null},rest:{p:null,f:null}}};
      state.macroGoals.split.workout={p:130,f:65};
      state.macroGoals.split.rest={p:115,f:60};
      state.profile.cap=1.20;
      state.profile.pufa=4.0;
      if(!state.ratioGoals17)state.ratioGoals17={};
      state.ratioGoals17.cp=3.0;
    },'Perfil Prometabólico aplicado (Ca:P 1.20, PUFA 4.0, macros y ratio CP)');
    render();
    toast('Perfil aplicado con éxito.');
  });
};"""

onClickNew = """$('btn-prometabolic').onclick=()=>{
  attempt(()=>{
    change(()=>{
      state.targetMode='split';
      if(!state.macroGoals)state.macroGoals={all:{p:null,f:null},split:{workout:{p:null,f:null},rest:{p:null,f:null}}};
      state.macroGoals.split.workout={p:130,f:65};
      state.macroGoals.split.rest={p:115,f:60};
      state.profile.cap=1.20;
      state.profile.pufa=4.0;
      if(!state.ratioGoals17)state.ratioGoals17={};
      state.ratioGoals17.cp=3.0;
      for(const [dt,d] of Object.entries(state.days)){
        delete d.target;
        delete d.microTargets17;
        delete d.ratioGoals17;
      }
      state.compare17={};
    },'Perfil Prometabólico Peat/Dinkov activado: 130P/65F entreno, 115P/60F descanso, Ca:P 1.20, PUFA <= 4g');
    render();
    renderSettings();
    toast('Perfil Prometabólico Peat/Dinkov activado: 130P/65F entreno, 115P/60F descanso, Ca:P 1.20, PUFA <= 4g', true);
  });
};"""

content = content.replace(onClickOrig, onClickNew)

# migration and context updates
migrateOrig = """function migrate(o){
  const s=migrateBase(o);
  upgradeTo11(s,o);
  upgradeTo12(s,o);
  upgradeTo16(s,o);
  upgradeTo17(s,o);
  upgradeTo18(s,o);
  upgradeTo19(s,o);
  upgradeTo20(s,o);
  upgradeTo21(s,o);
  s.favorites22=Array.isArray(o&&o.favorites22)?o.favorites22.slice(0,40):[];
  s.aiNotes=String(o&&o.aiNotes||'').slice(0,2000);
  return s;
}"""

migrateNew = """function upgradeTo22(s,o){
  if(s.appRevision>=22)return;
  s.targetMode='split';
  if(!s.macroGoals)s.macroGoals={all:{p:null,f:null},split:{workout:{p:null,f:null},rest:{p:null,f:null}}};
  s.macroGoals.split.workout={p:130,f:65};
  s.macroGoals.split.rest={p:115,f:60};
  s.profile.cap=1.20;
  s.profile.pufa=4.0;
  if(!s.ratioGoals17)s.ratioGoals17={};
  s.ratioGoals17.cp=3.0;
  for(const [dt,d] of Object.entries(s.days)){
    delete d.target;
    delete d.microTargets17;
    delete d.ratioGoals17;
  }
  s.compare17={};
  s.appRevision=22;
}
function migrate(o){
  const s=migrateBase(o);
  upgradeTo11(s,o);
  upgradeTo12(s,o);
  upgradeTo16(s,o);
  upgradeTo17(s,o);
  upgradeTo18(s,o);
  upgradeTo19(s,o);
  upgradeTo20(s,o);
  upgradeTo21(s,o);
  upgradeTo22(s,o);
  s.favorites22=Array.isArray(o&&o.favorites22)?o.favorites22.slice(0,40):[];
  s.aiNotes=String(o&&o.aiNotes||'').slice(0,2000);
  return s;
}"""

content = content.replace(migrateOrig, migrateNew)

with open('index.html', 'w') as f:
    f.write(content)

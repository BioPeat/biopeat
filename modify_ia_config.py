import sys
import re

def update_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # Create applyAIConfig
    apply_ai_func = """async function applyAIConfig(raw){
  let conf;
  try {
    const s = raw.substring(raw.indexOf('{'), raw.lastIndexOf('}')+1);
    conf = JSON.parse(s);
  } catch(e){
    throw Error('No se pudo leer la respuesta de la IA como JSON. ' + e.message);
  }

  change(()=>{
    if(conf.profile) {
      if(conf.profile.weight) state.profile.weight = conf.profile.weight;
      if(conf.profile.height) state.profile.height = conf.profile.height;
      if(conf.profile.age) state.profile.age = conf.profile.age;
      if(conf.profile.pufa) state.profile.pufa = conf.profile.pufa;
      if(conf.profile.cap) state.profile.cap = conf.profile.cap;
    }

    if(conf.macroGoals) {
      if(!state.macroGoals)state.macroGoals={all:{p:null,f:null},split:{workout:{p:null,f:null},rest:{p:null,f:null}}};
      if(conf.macroGoals.all) {
        state.targetMode = 'all';
        state.macroGoals.all.p = conf.macroGoals.all.p;
        state.macroGoals.all.f = conf.macroGoals.all.f;
      } else if(conf.macroGoals.split) {
        state.targetMode = 'split';
        if(conf.macroGoals.split.workout){
           state.macroGoals.split.workout.p = conf.macroGoals.split.workout.p;
           state.macroGoals.split.workout.f = conf.macroGoals.split.workout.f;
        }
        if(conf.macroGoals.split.rest){
           state.macroGoals.split.rest.p = conf.macroGoals.split.rest.p;
           state.macroGoals.split.rest.f = conf.macroGoals.split.rest.f;
        }
      }
    }

    if(conf.ratioGoals) {
      if(!state.ratioGoals17) state.ratioGoals17 = {};
      if(conf.ratioGoals.cp) state.ratioGoals17.cp = conf.ratioGoals.cp;
    }

    if(conf.microTargets) {
      for(const k of Object.keys(conf.microTargets)) {
         if(MICRO.find(m=>m.k===k)) state.targets[k] = conf.microTargets[k];
      }
    }

    if(conf.plan && Array.isArray(conf.plan)) {
      state.plan = conf.plan.map(cleanPlan);
    }

    if(conf.context) {
      state.context = conf.context;
    }
  }, 'Ajustes globales de IA aplicados');
  toast(conf.summary || 'Ajustes aplicados correctamente');
  render();
}"""

    # We insert applyAIConfig near requestAI
    content = content.replace("async function requestAI(prompt,img,signal,modelOverride=''){", f"{apply_ai_func}\nasync function requestAI(prompt,img,signal,modelOverride=''){{")

    # Now add the button next to notes logic
    html_target = r'<button class="btn btn-slate full" style="margin-top:8px" type="submit">Guardar notas</button></form>'
    html_replacement = r'<button class="btn btn-slate full" style="margin-top:8px" type="submit">Guardar notas</button><button id="btn-ai-apply" type="button" class="btn btn-amber full" style="margin-top:8px">Aplicar instrucciones en toda la app con IA</button></form>'
    content = content.replace(html_target, html_replacement)

    # Now add the listener for it
    # We find `$(`ai-notes-form`).onsubmit=...`
    listener = """$('btn-ai-apply').onclick=async()=>{
  const notes = $('ai-notes').value.trim();
  if(!notes) { toast('Escribe instrucciones en el cuadro de arriba.'); return; }
  try {
    const sum = {
       profile: state.profile,
       macroGoals: state.macroGoals,
       ratioGoals: state.ratioGoals17 || {},
       microTargets: state.targets,
       plan: state.plan,
       context: state.context
    };
    const prompt = "Instrucciones del usuario:\\n" + notes + "\\n\\nResumen actual JSON:\\n" + JSON.stringify(sum) + "\\n\\nGenera un JSON en la propiedad BIOPEAT_CONFIG: {...} con las actualizaciones correspondientes para profile, macroGoals (usando la estructura con all o split con workout y rest), ratioGoals, microTargets, plan, context, y un summary corto de lo que has modificado. Retorna solo el JSON en la respuesta.";
    $('btn-ai-apply').disabled=true;
    $('btn-ai-apply').textContent='Procesando...';
    const res = await requestAI(prompt);
    await applyAIConfig(res);
  } catch (e) {
    alert(e.message);
  } finally {
    $('btn-ai-apply').disabled=false;
    $('btn-ai-apply').textContent='Aplicar instrucciones en toda la app con IA';
  }
};"""

    # Insert it right below ai-notes-form onsubmit
    content = content.replace("$('ai-notes-form').onsubmit=e=>{e.preventDefault();change(()=>state.aiNotes=$('ai-notes').value.trim().slice(0,2000),state.aiNotes?'Notas guardadas: la IA las usará':'Notas guardadas');};", "$('ai-notes-form').onsubmit=e=>{e.preventDefault();change(()=>state.aiNotes=$('ai-notes').value.trim().slice(0,2000),state.aiNotes?'Notas guardadas: la IA las usará':'Notas guardadas');};\n" + listener)

    with open(filename, 'w') as f:
        f.write(content)

update_file("index.html")

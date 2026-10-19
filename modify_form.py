import sys
import re

def update_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    def repl_edit(m):
        html = m.group(1)
        new_html = html.replace('<p class="section-note">Metas editables', '''<p class="section-note">Metas de macros</p>
<div class="inline-form">
  <label class="wide">Aplicar metas de macros:
    <select id="target-mode" name="targetMode">
      <option value="all" ${state.targetMode==='all'?'selected':''}>Para todos los días</option>
      <option value="split" ${state.targetMode==='split'?'selected':''}>Días de entreno L/X/S/D vs Descanso M/J/V</option>
      <option value="today" ${state.targetMode==='today'?'selected':''}>Solo hoy</option>
    </select>
  </label>
</div>
<div id="macro-fields-all" style="display:${state.targetMode==='all'?'block':'none'}">
  <div class="inline-form">
    <label>Proteína (g)<input type="number" name="m_all_p" min="0" step="any" value="${state.macroGoals?.all?.p??''}"></label>
    <label>Grasa (g)<input type="number" name="m_all_f" min="0" step="any" value="${state.macroGoals?.all?.f??''}"></label>
  </div>
</div>
<div id="macro-fields-split" style="display:${state.targetMode==='split'?'block':'none'}">
  <p class="subtext">Días de entreno (L/X/S/D)</p>
  <div class="inline-form">
    <label>Proteína (g)<input type="number" name="m_split_workout_p" min="0" step="any" value="${state.macroGoals?.split?.workout?.p??''}"></label>
    <label>Grasa (g)<input type="number" name="m_split_workout_f" min="0" step="any" value="${state.macroGoals?.split?.workout?.f??''}"></label>
  </div>
  <p class="subtext">Días de descanso (M/J/V)</p>
  <div class="inline-form">
    <label>Proteína (g)<input type="number" name="m_split_rest_p" min="0" step="any" value="${state.macroGoals?.split?.rest?.p??''}"></label>
    <label>Grasa (g)<input type="number" name="m_split_rest_f" min="0" step="any" value="${state.macroGoals?.split?.rest?.f??''}"></label>
  </div>
</div>
<div id="macro-fields-today" style="display:${state.targetMode==='today'?'block':'none'}">
  <div class="inline-form">
    <label>Proteína (g)<input type="number" name="m_today_p" min="0" step="any" value="${state.days[date]?.macroGoals?.p??''}"></label>
    <label>Grasa (g)<input type="number" name="m_today_f" min="0" step="any" value="${state.days[date]?.macroGoals?.f??''}"></label>
  </div>
</div>
<p class="section-note">Metas editables''')

        # We need to add JS to toggle the forms after modal opens, but editTargetsForm does not run code after modal.
        # Wait, modal string is just an HTML template. We can add an inline script or event delegation.
        # However, the script is better attached via a global listener or inside editTargetsForm after modal returns.
        # modal(title, html) is synchronous, it updates DOM.

        # Let's add the onchange logic via setTimeout or inside the HTML as onchange="...":
        new_html = new_html.replace('<select id="target-mode" name="targetMode">', '<select id="target-mode" name="targetMode" onchange="document.getElementById(\'macro-fields-all\').style.display=this.value===\'all\'?\'block\':\'none\';document.getElementById(\'macro-fields-split\').style.display=this.value===\'split\'?\'block\':\'none\';document.getElementById(\'macro-fields-today\').style.display=this.value===\'today\'?\'block\':\'none\'">')

        return f"function editTargetsForm(){{{new_html}}}"

    content = re.sub(r'function editTargetsForm\(\)\{([^}]+)\}', repl_edit, content)


    def repl_handler(m):
        return """const targetsFormHandler=e=>{
  if(e.target.id!=='targets-form')return;
  e.preventDefault();
  attempt(()=>{
    const fd=new FormData(e.target),goals={};
    for(const m of MICRO){const v=fd.get(m.k);goals[m.k]=v===''?null:number(v,.001,1e6);}
    const tM=fd.get('targetMode');
    const pA=fd.get('m_all_p'),fA=fd.get('m_all_f');
    const pW=fd.get('m_split_workout_p'),fW=fd.get('m_split_workout_f');
    const pR=fd.get('m_split_rest_p'),fR=fd.get('m_split_rest_f');
    const pT=fd.get('m_today_p'),fT=fd.get('m_today_f');
    change(()=>{
      state.targets=goals;
      day().microTargets17=clone(goals);
      day().goalOrigin17='saved';
      state.targetMode=tM;
      if(!state.macroGoals)state.macroGoals={all:{p:null,f:null},split:{workout:{p:null,f:null},rest:{p:null,f:null}}};
      if(tM==='all'){
        state.macroGoals.all={p:pA===''?null:number(pA,0,600),f:fA===''?null:number(fA,0,500)};
      } else if(tM==='split'){
        state.macroGoals.split.workout={p:pW===''?null:number(pW,0,600),f:fW===''?null:number(fW,0,500)};
        state.macroGoals.split.rest={p:pR===''?null:number(pR,0,600),f:fR===''?null:number(fR,0,500)};
      } else if(tM==='today'){
        day().macroGoals={p:pT===''?null:number(pT,0,600),f:fT===''?null:number(fT,0,500)};
      }
    },'Metas guardadas');
    $('modal').close();
  });
};"""

    # find targetsFormHandler definition
    pattern = r'const targetsFormHandler=e=>\{if\(e\.target\.id!==\'targets-form\'\)return;e\.preventDefault\(\);attempt\(\(\)=>\{const fd=new FormData\(e\.target\),goals=\{.*?\};\s*\$\(\'modal\'\)\.close\(\);\s*\}\);\s*\};'
    content = re.sub(pattern, repl_handler, content, flags=re.DOTALL)

    with open(filename, 'w') as f:
        f.write(content)

update_file("index.html")

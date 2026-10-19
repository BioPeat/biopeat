import sys
import re

def update_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # insert the button in HTML
    # We will insert it inside `<details class="card"><summary>Editar objetivos de macros del día</summary>...`
    # or somewhere before `</details><div class="card"><h2>Notas para la IA</h2>`
    # Let's put it right after the macro-target-form:
    # `</form><p class="section-note">Carbohidratos = energía restante con 4/4/9. Es una planificación personal, no una medición del gasto ni un óptimo demostrado de Peat.</p>`

    html_target = r'</form><p class="section-note">Carbohidratos = energía restante con 4/4/9. Es una planificación personal, no una medición del gasto ni un óptimo demostrado de Peat.</p>'
    html_replacement = r'</form><p class="section-note">Carbohidratos = energía restante con 4/4/9. Es una planificación personal, no una medición del gasto ni un óptimo demostrado de Peat.</p><button id="btn-prometabolic" class="btn wide" style="margin-top:12px;width:100%">Aplicar perfil Prometabólico Peat/Dinkov</button>'
    content = content.replace(html_target, html_replacement)

    # insert the event listener
    # `$('profile-form').onsubmit` is defined around line 6680. We can add our listener there.

    js_listener = """$('btn-prometabolic').onclick=()=>{
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

    # We append it before `$('compare-form').onsubmit`
    content = content.replace("$('compare-form').onsubmit=", js_listener + "\n$('compare-form').onsubmit=")

    with open(filename, 'w') as f:
        f.write(content)

update_file("index.html")

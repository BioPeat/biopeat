import sys
import re

def update_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    def repl_addEntries(m):
        func_body = m.group(1)
        # add the auto-complete logic inside change() or after change()
        # "Cuando se añada cualquier comida o toma real en la fecha actual d, comprueba el día anterior (shift(d, -1)): si el día anterior tiene al menos una entrada real registrada (dayActive) y no tiene completed: true, márcalo automáticamente como completado (completed: true)."
        # We can add this inside the `change` callback of addEntries so it runs as part of the same transaction.

        # Original change block:
        # change(()=>{const fresh=clean.map(e=>({...e,id:uid()}));if(opts.remember)fresh.forEach(rememberFood);ensureDay(d).entries.push(...fresh);ensureDay(d).complete=false;},message);

        # Modified block:
        # change(()=>{
        #   const fresh=clean.map(e=>({...e,id:uid()}));
        #   if(opts.remember)fresh.forEach(rememberFood);
        #   ensureDay(d).entries.push(...fresh);
        #   ensureDay(d).complete=false;
        #   if(d===localDate() && clean.some(e=>e.kind==='food'||(!e.auto||e.confirmed))){
        #      const prev=shift(d,-1);
        #      if(state.days[prev] && dayActive(state.days[prev]) && !state.days[prev].complete){
        #         state.days[prev].complete=true;
        #      }
        #   }
        # },message);
        # Note: the instruction says "la fecha actual d". But `d` is just the parameter. The UI date is `date` (from let date=localDate()). We can use `d === localDate()` or `d === date`.
        # `date` is a global let. Wait, UI can change `date`. The instruction says "en la fecha actual d", probably meaning `d === localDate()` to only mark yesterday if we are adding to *today real world*. Or maybe if we just add to any day `d`, we complete `d-1`. "la fecha actual d" likely means we are currently in `d` and we complete `d-1`. Let's just check `d === localDate()`. Wait, `localDate()` returns string '2023-10-15'.

        new_change = """change(()=>{
    const fresh=clean.map(e=>({...e,id:uid()}));
    if(opts.remember)fresh.forEach(rememberFood);
    ensureDay(d).entries.push(...fresh);
    ensureDay(d).complete=false;
    if(d===localDate() && clean.some(e=>e.kind==='food'||!e.auto||e.confirmed)){
      const prev=shift(d,-1);
      if(state.days[prev] && dayActive(state.days[prev]) && !state.days[prev].complete){
        state.days[prev].complete=true;
      }
    }
  },message);"""

        new_body = func_body.replace("change(()=>{const fresh=clean.map(e=>({...e,id:uid()}));if(opts.remember)fresh.forEach(rememberFood);ensureDay(d).entries.push(...fresh);ensureDay(d).complete=false;},message);", new_change)

        return f"function addEntries(entries,message='Añadido',d=date,opts={{}}){{{new_body}}}"

    content = re.sub(r'function addEntries\(entries,message=\'Añadido\',d=date,opts=\{\}\)\{([^}]+)\}', repl_addEntries, content)

    with open(filename, 'w') as f:
        f.write(content)

update_file("index.html")

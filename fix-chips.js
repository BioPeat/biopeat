const fs = require('fs');
let content = fs.readFileSync('index.html', 'utf8');

const CSS_SEARCH = `.bp-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 10px;
}`;

const CSS_REPLACE = `.bp-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 10px;
}
.bp-chips.compact-chips {
    flex-wrap: nowrap;
    overflow-x: auto;
    overflow-y: hidden;
    padding-bottom: 4px;
    scroll-snap-type: x mandatory;
    -webkit-overflow-scrolling: touch;
}
.bp-chips.compact-chips::-webkit-scrollbar {
    display: none;
}
.bp-chips.compact-chips .bp-chip {
    scroll-snap-align: start;
    flex-shrink: 0;
}`;

content = content.replace(CSS_SEARCH, CSS_REPLACE);

const JS_SEARCH = `function drawQuickFoods(){
  $('chips-hint').textContent='Un toque = añadir a '+$('meal-select').value+' · ☆ = favorito';
  const box=$('bp-chips');
  box.textContent='';
  const favs=state.favorites22||[],keys=new Set(favs.map(quickKey));
  favs.forEach(f=>box.append(quickChip(f,true)));
  recentFoods().filter(r=>!keys.has(quickKey(r))).slice(0,8).forEach(r=>box.append(quickChip(r,false)));
  if(!box.children.length){const p=document.createElement('p');p.className='bp-empty';p.textContent='Aquí aparecerán lo que comes a menudo y tus favoritos, para añadirlos con un toque.';box.append(p);}
}`;

const JS_REPLACE = `function drawQuickFoods(){
  $('chips-hint').textContent='Un toque = añadir a '+$('meal-select').value+' · ☆ = favorito';
  const box=$('bp-chips');
  box.textContent='';
  const favs=state.favorites22||[],keys=new Set(favs.map(quickKey));
  favs.forEach(f=>box.append(quickChip(f,true)));
  recentFoods().filter(r=>!keys.has(quickKey(r))).slice(0,8).forEach(r=>box.append(quickChip(r,false)));
  if(!box.children.length){const p=document.createElement('p');p.className='bp-empty';p.textContent='Aquí aparecerán lo que comes a menudo y tus favoritos, para añadirlos con un toque.';box.append(p);}
  else {
    box.classList.add('compact-chips');
    if(!document.getElementById('chips-toggle')){
      const btn=document.createElement('button');
      btn.id='chips-toggle';
      btn.className='btn ghost small';
      btn.textContent='Ver todos';
      btn.style.marginTop='8px';
      btn.onclick=()=>{
        const c=box.classList.contains('compact-chips');
        box.classList.toggle('compact-chips');
        btn.textContent=c?'Plegar':'Ver todos';
      };
      box.parentNode.insertBefore(btn, box.nextSibling);
    } else {
      document.getElementById('chips-toggle').textContent=box.classList.contains('compact-chips')?'Ver todos':'Plegar';
    }
  }
}`;

content = content.replace(JS_SEARCH, JS_REPLACE);
fs.writeFileSync('index.html', content);
console.log("Chips fix applied");

const fs = require('fs');
let content = fs.readFileSync('index.html', 'utf8');

const s = `finally{clearTimeout(timer);aiBusy=false;aiController=null;$('smart-add').disabled=false;$('analyze-photo').disabled=false;$('cancel-ai').hidden=true;}`;
const r = `finally{clearTimeout(timer);aiBusy=false;aiController=null;$('smart-add').disabled=false;$('analyze-photo').disabled=false;$('cancel-ai').hidden=true;if(usePhoto){const f=$('photo-file');if(f)f.value='';const c=$('photo-camera');if(c)c.value='';$('bp-photo').classList.remove('on');}}`;

content = content.replace(s, r);
fs.writeFileSync('index.html', content);
console.log("Analyze patch applied");

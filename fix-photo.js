const fs = require('fs');
let content = fs.readFileSync('index.html', 'utf8');

const SEARCH = `function resetPhoto(){
  photo=null;
  if(photoURL){URL.revokeObjectURL(photoURL);photoURL=null;}
  $('photo-preview').removeAttribute('src');
  $('photo-preview').hidden=true;
  $('photo-note').value='';
  $('photo-file').value='';
  $('photo-camera').value='';
}`;

const REPLACE = `function resetPhoto(){
  photo=null;
  if(photoURL){URL.revokeObjectURL(photoURL);photoURL=null;}
  $('photo-preview').removeAttribute('src');
  $('photo-preview').hidden=true;
  $('photo-note').value='';
  $('photo-file').value='';
  $('photo-camera').value='';
  $('photo-panel').hidden=true;
  syncAddTools();
}`;

content = content.replace(SEARCH, REPLACE);
fs.writeFileSync('index.html', content);
console.log("Photo bug fixed");

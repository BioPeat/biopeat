import sys
import re

def update_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    def repl_renderWeekMicros(m):
        func_body = m.group(1)
        # Adding the selenium warning in `<p>Meta ...`
        new_body = func_body.replace("<p>Meta ${a.goal?fmt(a.goal,2)+' '+unit:'sin definir'}</p>", "<p>Meta ${a.goal?fmt(a.goal,2)+' '+unit:'sin definir'}</p>${m.k==='se'&&a.value>200?'<small class=\"bp-warn\" style=\"color:red\">Aviso: media de 7d &gt; 200 µg</small>':''}")
        return f"function renderWeekMicros(s){{{new_body}}}"

    content = re.sub(r'function renderWeekMicros\(s\)\{([^}]+)\}', repl_renderWeekMicros, content)

    def repl_targetRow(m):
        body = m.group(1)
        new_body = body.replace("<p>Meta: ${fmt(r.goal,2)} ${m.unit}</p>", "<p>Meta: ${fmt(r.goal,2)} ${m.unit}</p>${m.k==='se'&&r.value>200?'<small class=\"bp-warn\" style=\"color:red\">Aviso: media de 7d &gt; 200 µg</small>':''}")
        return f"function targetRow(m,r){{{new_body}}}"

    content = re.sub(r'function targetRow\(m,r\)\{([^}]+)\}', repl_targetRow, content)

    with open(filename, 'w') as f:
        f.write(content)

update_file("index.html")

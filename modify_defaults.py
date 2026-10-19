import sys
import re

def update_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    def repl_defaults(m):
        inner = m.group(1)
        if "targetMode" in inner:
            return m.group(0)

        new_inner = inner.replace("favorites22:[],aiNotes:''", "favorites22:[],targetMode:'all',macroGoals:{all:{p:null,f:null},split:{workout:{p:null,f:null},rest:{p:null,f:null}}},aiNotes:''")
        return f"function defaults(){{{new_inner}}}"

    content = re.sub(r'function defaults\(\)\{([^}]+)\}', repl_defaults, content)

    with open(filename, 'w') as f:
        f.write(content)

update_file("index.html")

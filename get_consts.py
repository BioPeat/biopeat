import sys
import re

def get_const(content, name):
    pattern = r'const\s+' + name + r'\s*='
    match = re.search(pattern, content)
    if not match:
        return f"Const {name} not found."

    start_idx = match.start()
    idx = match.end() - 1
    bracket_count = 0
    brace_count = 0

    while idx < len(content):
        if content[idx] == '[':
            bracket_count += 1
        elif content[idx] == ']':
            bracket_count -= 1
        elif content[idx] == '{':
            brace_count += 1
        elif content[idx] == '}':
            brace_count -= 1
        elif content[idx] == ';' and bracket_count == 0 and brace_count == 0:
            return content[start_idx:idx+1]
        idx += 1

    return "Error: Could not find end of const."

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        content = f.read()

    for const in sys.argv[2:]:
        print(f"--- {const} ---")
        print(get_const(content, const))
        print()

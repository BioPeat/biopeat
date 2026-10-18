import sys
import re

def get_function_body(content, func_name):
    pattern = r'(function\s+' + func_name + r'\s*\([^)]*\)\s*\{|const\s+' + func_name + r'\s*=\s*\([^)]*\)\s*=>\s*\{)'
    match = re.search(pattern, content)
    if not match:
        return f"Function {func_name} not found."

    start_idx = match.start()
    idx = match.end() - 1
    brace_count = 0

    while idx < len(content):
        if content[idx] == '{':
            brace_count += 1
        elif content[idx] == '}':
            brace_count -= 1

        if brace_count == 0:
            return content[start_idx:idx+1]
        idx += 1

    return "Error: Could not find end of function."

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python get_functions.py <file> <func1> [func2...]")
        sys.exit(1)

    with open(sys.argv[1], 'r') as f:
        content = f.read()

    for func in sys.argv[2:]:
        print(f"--- {func} ---")
        print(get_function_body(content, func))
        print()

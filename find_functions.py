import sys

def find_func(filepath, func_name):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    start_idx = -1
    for i, line in enumerate(lines):
        if line.startswith(f"function {func_name}") or line.startswith(f"const {func_name} =") or line.startswith(f"const {func_name}="):
            start_idx = i
            break

    if start_idx != -1:
        # read until closing brace
        open_braces = 0
        end_idx = -1
        for i in range(start_idx, len(lines)):
            open_braces += lines[i].count('{')
            open_braces -= lines[i].count('}')
            if open_braces == 0 and i > start_idx:
                end_idx = i
                break

        if end_idx != -1:
            print("".join(lines[start_idx:end_idx+1]))
            return

    print(f"Function {func_name} not found")

if __name__ == "__main__":
    find_func("index.html", sys.argv[1])

import sys

def get_lines_around(filename, string, context=20):
    with open(filename, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if string in line:
            start = max(0, i - context)
            end = min(len(lines), i + context + 1)
            print(f"--- Found '{string}' at line {i+1} ---")
            for j in range(start, end):
                prefix = ">> " if j == i else "   "
                print(f"{j+1:4d}{prefix}{lines[j].strip()}")
            print("\n")

if __name__ == "__main__":
    get_lines_around(sys.argv[1], sys.argv[2])

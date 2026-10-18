import sys

def get_lines(filename, search_str):
    with open(filename, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if search_str in line:
            print(f"{i+1}: {line.strip()}")

if __name__ == "__main__":
    get_lines(sys.argv[1], sys.argv[2])

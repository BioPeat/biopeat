import sys

def get_lines(filename, start, end):
    with open(filename, 'r') as f:
        lines = f.readlines()
        print(''.join(lines[start-1:end]))

if __name__ == "__main__":
    get_lines(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

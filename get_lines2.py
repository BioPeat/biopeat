import sys
def get_lines(filename, search_term, lines_before, lines_after):
    with open(filename, 'r') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if search_term in line:
            start = max(0, i - lines_before)
            end = min(len(lines), i + lines_after + 1)
            print(f"Match found at line {i+1}:")
            for j in range(start, end):
                prefix = "*" if j == i else " "
                print(f"{prefix} {j+1}: {lines[j]}", end="")
            print("-" * 40)
            return

get_lines("index.html", "function renderMicrosForDay(", 2, 20)

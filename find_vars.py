import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

def find_in_file(pattern):
    for match in re.finditer(pattern, content):
        start = max(0, match.start() - 50)
        end = min(len(content), match.end() + 200)
        print(f"Match found at line {content[:match.start()].count(chr(10)) + 1}:")
        print(content[start:end])
        print("-" * 40)

patterns = [
    r'function targetFor',
    r'function goalsFor',
    r'function editTargetsForm',
    r'function renderSettings',
    r'const CONTEXT',
    r'function migrate',
    r'function renderRatios',
    r'function renderMicrosForDay',
    r'function renderWeekMicros',
    r'function microStat',
    r'const LENS',
    r'function gpSessionMetrics',
    r'function gpStatus',
    r'function renderCalendar',
    r'function renderHeader',
    r'appRevision',
    r'upgradeTo22',
    r'function gpSessionMetrics',
]

for p in patterns:
    print(f"Searching for {p}")
    find_in_file(p)

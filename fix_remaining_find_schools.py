fixes = [
    ("french-bac-navigator.html", "French"),
    ("german-abitur-navigator.html", "German"),
]

for path, cur_value in fixes:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    old = f'''onclick="window.location.href='index.html'" id="findBtn">Find {cur_value} schools ↗</button>'''
    new = f'''onclick="window.location.href='schools.html?cur={cur_value}'" id="findBtn">Find {cur_value} schools ↗</button>'''

    count = content.count(old)
    if count != 1:
        print(f"SKIPPED {path}: expected 1 match, found {count} — check manually.")
        continue
    content = content.replace(old, new, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fixed {path} -> schools.html?cur={cur_value}")

print("Done.")

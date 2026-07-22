files = [
    "ib-curriculum-guide.html",
    "cbse-curriculum-guide.html",
    "frenchbac-curriculum-guide.html",
    "german-abitur-curriculum-guide.html",
    "singapore-curriculum-guide.html",
    "australian-vce-curriculum-guide.html",
    "enem-curriculum-guide.html",
]

old_block = '''    <ellipse cx="32" cy="32" rx="29" ry="12" stroke="#F5C842" stroke-width="0.8" fill="none"/>
  </svg>'''

new_block = '''    <ellipse cx="32" cy="32" rx="29" ry="12" stroke="#F5C842" stroke-width="0.8" fill="none"/>
    <circle cx="32" cy="32" r="3" fill="#F5C842"/>
    <polygon points="32,4 35,25 32,26.5 29,25" fill="#F5C842"/>
  </svg>'''

for path in files:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    count = content.count(old_block)
    if count != 1:
        print(f"SKIPPED {path}: expected 1 match, found {count} — check manually.")
        continue
    content = content.replace(old_block, new_block, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fixed {path}")

print("Done.")

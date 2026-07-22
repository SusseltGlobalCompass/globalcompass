fixes = [
    ("australian-vce-navigator.html", "Australian"),
    ("brazilian-enem-navigator.html", "Brazilian"),
    ("cbse-stream-navigator.html", "CBSE"),
    ("ib-pathway-navigator.html", "IB"),
    ("singapore-pathway-navigator.html", "Singapore"),
]

for path, cur_value in fixes:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    old = f"onclick=\"window.location.href='index.html'\">Find {cur_value if cur_value != 'CBSE' else 'CBSE'} schools ↗</button>"
    # Match the exact "Find X schools" text as it appears per file
    import re
    pattern = re.compile(r"onclick=\"window\.location\.href='index\.html'\">Find [^<]*schools ↗</button>")
    matches = pattern.findall(content)
    if len(matches) != 1:
        print(f"SKIPPED {path}: expected 1 match, found {len(matches)} — check manually.")
        continue
    old_text = matches[0]
    new_text = old_text.replace("window.location.href='index.html'", f"window.location.href='schools.html?cur={cur_value}'")
    content = content.replace(old_text, new_text, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fixed {path} -> schools.html?cur={cur_value}")

print("Done.")

path = "index.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''  <svg class="hero-bg" viewBox="0 0 600 600" fill="none"><circle cx="300" cy="300" r="270" stroke="#F5C842" stroke-width="1"/><ellipse cx="300" cy="300" rx="150" ry="270" stroke="#F5C842" stroke-width="0.7"/><ellipse cx="300" cy="300" rx="270" ry="105" stroke="#F5C842" stroke-width="0.7"/><ellipse cx="300" cy="300" rx="270" ry="195" stroke="#F5C842" stroke-width="0.5"/><line x1="30" y1="300" x2="570" y2="300" stroke="#F5C842" stroke-width="0.6"/><line x1="300" y1="30" x2="300" y2="570" stroke="#F5C842" stroke-width="0.6"/></svg>
'''

count = content.count(old)
if count != 1:
    raise SystemExit(f"ABORTED: expected 1 match, found {count}. No changes made.")

content = content.replace(old, "", 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done. Duplicate background compass removed — the complete one (with needle) remains.")

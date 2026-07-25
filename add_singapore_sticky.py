path = "singapore-pathway-navigator.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

old = '.step-indicator{display:flex;align-items:center;margin-bottom:24px}'
new = '.step-indicator{display:flex;align-items:center;margin-bottom:24px;position:sticky;top:0;background:#F8F9FF;padding:12px 0;z-index:5}'

count = content.count(old)
if count != 1:
    raise SystemExit(f"ABORTED: expected 1 match, found {count}")
content = content.replace(old, new, 1)

# Soften "stress profile" to match the gentler tone
old2 = 'Next — Your stress profile →'
new2 = 'Next — Your profile →'
count2 = content.count(old2)
if count2 != 1:
    raise SystemExit(f"ABORTED at wording: expected 1 match, found {count2}")
content = content.replace(old2, new2, 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Singapore: sticky positioning added, button wording softened.")

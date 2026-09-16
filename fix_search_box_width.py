"""
Fix the university search box appearing tiny/unstyled: the .f-sel CSS
rule was scoped only to <select> elements (select.f-sel), so the new
<input> search box never received any of that styling. Broaden the
selector to apply to both.

Run from inside ~/Desktop/GlobalCompass
"""

FILE = "university-requirements.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

original = content

old = "select.f-sel{width:100%;padding:12px 14px;border:1.5px solid #E0E8F5;border-radius:10px;font-size:14px;color:#0D1F4A;font-family:'Inter',sans-serif;background:#fff;cursor:pointer}"
new = ".f-sel{width:100%;padding:12px 14px;border:1.5px solid #E0E8F5;border-radius:10px;font-size:14px;color:#0D1F4A;font-family:'Inter',sans-serif;background:#fff;cursor:pointer;box-sizing:border-box}"

if old not in content:
    print("ERROR: Could not find the .f-sel CSS rule exactly. No changes made.")
else:
    content = content.replace(old, new)
    with open(FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print("Done. .f-sel now applies to both <select> and <input> elements.")

if content == original:
    print("WARNING: No changes were made at all.")

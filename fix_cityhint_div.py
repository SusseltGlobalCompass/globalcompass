"""
Add the missing cityHint div that the JS logic already references,
fixing the "hintEl is null" runtime error.

Run from inside ~/Desktop/GlobalCompass
"""

FILE = "schools.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

original = content

old_html = '''  <div id="resultsMeta" class="results-meta"></div>'''
new_html = '''  <div id="cityHint" style="display:none;text-align:center;font-size:12px;color:#7A8BAE;margin-bottom:10px;font-family:'Inter',sans-serif"></div>
  <div id="resultsMeta" class="results-meta"></div>'''

count = content.count(old_html)
if count == 0:
    print("ERROR: Could not find resultsMeta anchor. No changes made.")
elif count > 1:
    print(f"ERROR: Found {count} matches, expected exactly 1. Aborting to avoid ambiguity.")
else:
    content = content.replace(old_html, new_html)
    with open(FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print("Done. cityHint div added.")

if content == original:
    print("WARNING: No changes were made at all.")

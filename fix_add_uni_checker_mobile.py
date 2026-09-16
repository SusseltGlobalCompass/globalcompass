"""
Add University Requirements Checker to the mobile menu, correctly
positioned before Subject Explorer this time (previous attempt used
an incorrect anchor assumption).

Run from inside ~/Desktop/GlobalCompass
"""

FILE = "index.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

original = content

old_mobile = '''      <a href="brazilian-enem-navigator.html">Brazilian ENEM</a>
      <a href="subject-explorer.html">Subject Explorer</a>'''
new_mobile = '''      <a href="brazilian-enem-navigator.html">Brazilian ENEM</a>
      <a href="university-requirements.html">University Requirements Checker</a>
      <a href="subject-explorer.html">Subject Explorer</a>'''

count = content.count(old_mobile)
if count == 0:
    print("ERROR: Could not find mobile menu anchor. No changes made.")
elif count > 1:
    print(f"ERROR: Found {count} matches, expected 1. Aborting to avoid ambiguity.")
else:
    content = content.replace(old_mobile, new_mobile)
    with open(FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print("Done. University Requirements Checker added to mobile menu.")

if content == original:
    print("WARNING: No changes were made at all.")

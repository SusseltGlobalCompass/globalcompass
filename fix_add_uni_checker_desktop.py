"""
Add University Requirements Checker to the desktop nav dropdown.
(A previous script had a bug where this edit was computed but never
saved to disk - this run fixes that, saving unconditionally.)

Run from inside ~/Desktop/GlobalCompass
"""

FILE = "index.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

original = content

old_desktop = 'Plan your path</div><a class="di" href="subject-explorer.html">'
new_desktop = 'Plan your path</div><a class="di" href="university-requirements.html"><svg width="16" height="16" viewBox="0 0 32 32" fill="none" style="flex-shrink:0;vertical-align:-3px"><circle cx="16" cy="16" r="13" stroke="#F5C842" stroke-width="1.8"/><ellipse cx="16" cy="16" rx="6.5" ry="13" stroke="#F5C842" stroke-width="0.8" opacity="0.45"/><polygon points="16,3 17.8,10 16,11.5 14.2,10" fill="#F5C842"/><circle cx="16" cy="16" r="2" fill="#F5C842"/><circle cx="22" cy="7" r="2" fill="#F5C842"/></svg> University Requirements Checker</a><a class="di" href="subject-explorer.html">'

count = content.count(old_desktop)
if count == 0:
    print("ERROR: Could not find desktop nav anchor. No changes made.")
elif count > 1:
    print(f"ERROR: Found {count} matches, expected 1. Aborting to avoid ambiguity.")
else:
    content = content.replace(old_desktop, new_desktop)
    with open(FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print("Done. University Requirements Checker added to desktop nav.")

if content == original:
    print("WARNING: No changes were made at all.")

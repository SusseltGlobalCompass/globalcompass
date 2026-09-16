"""
Add University Requirements Checker to the site navigation - both
desktop dropdown and mobile menu - since it was deployed but never
actually linked from anywhere on the site.

Run from inside ~/Desktop/GlobalCompass
"""

FILE = "index.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

original = content

old_desktop = 'Plan your path</div><a class="di" href="subject-explorer.html">'
new_desktop = 'Plan your path</div><a class="di" href="university-requirements.html"><svg width="16" height="16" viewBox="0 0 32 32" fill="none" style="flex-shrink:0;vertical-align:-3px"><circle cx="16" cy="16" r="13" stroke="#F5C842" stroke-width="1.8"/><ellipse cx="16" cy="16" rx="6.5" ry="13" stroke="#F5C842" stroke-width="0.8" opacity="0.45"/><polygon points="16,3 17.8,10 16,11.5 14.2,10" fill="#F5C842"/><circle cx="16" cy="16" r="2" fill="#F5C842"/><circle cx="22" cy="7" r="2" fill="#F5C842"/></svg> University Requirements Checker</a><a class="di" href="subject-explorer.html">'

if old_desktop not in content:
    print("ERROR: Could not find desktop nav anchor. No changes made.")
else:
    content = content.replace(old_desktop, new_desktop)

    old_mobile = '<a href="subject-explorer.html">Subject Explorer</a>\n    </div>'
    new_mobile = '<a href="university-requirements.html">University Requirements Checker</a>\n      <a href="subject-explorer.html">Subject Explorer</a>\n    </div>'

    count = content.count(old_mobile)
    if count == 0:
        print("ERROR: Could not find mobile menu anchor. Desktop nav updated, mobile NOT updated.")
    elif count > 1:
        print(f"ERROR: Found {count} matches for mobile anchor, expected 1 - ambiguous, aborting mobile edit to be safe.")
    else:
        content = content.replace(old_mobile, new_mobile)
        with open(FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print("Done. University Requirements Checker added to both desktop and mobile navigation.")

if content == original:
    print("WARNING: No changes were made at all.")

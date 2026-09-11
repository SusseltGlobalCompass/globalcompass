"""
Fix two real issues on the homepage:
1. hBud dropdown still uses old AED-band VALUES that don't match
   schools.html's new USD-band values - a real functional mismatch,
   not just cosmetic. Update to matching USD values/labels.
2. Australia country card still says "Coming soon" despite having
   10,915 real schools live for two sessions - stale placeholder.

Run from inside ~/Desktop/GlobalCompass
"""

FILE = "index.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

original = content

old_budget = '''        <select class="s-filter-sel" id="hBud">
          <option value="">All budgets</option>
          <option value="0-20000">Under AED 20,000/yr</option>
          <option value="20000-45000">AED 20,000\u201345,000/yr</option>
          <option value="45000-75000">AED 45,000\u201375,000/yr</option>
          <option value="75000-999999">AED 75,000+/yr</option>
        </select>'''
new_budget = '''        <select class="s-filter-sel" id="hBud">
          <option value="">All budgets</option>
          <option value="0-5500">Under $5,500/yr</option>
          <option value="5500-12000">$5,500\u2013$12,000/yr</option>
          <option value="12000-20000">$12,000\u2013$20,000/yr</option>
          <option value="20000-999999">$20,000+/yr</option>
        </select>'''

if old_budget not in content:
    print("ERROR: Could not find hBud dropdown block exactly. No changes made.")
else:
    content = content.replace(old_budget, new_budget)

    old_aus = '<a class="cc" href="schools.html?q=Australia" style="text-decoration:none;cursor:pointer"><span class="c-flag">\U0001F1E6\U0001F1FA</span><div><div class="c-name">Australia</div><div class="c-count">Coming soon</div></div></a>'
    new_aus = '<a class="cc" href="schools.html?q=Australia" style="text-decoration:none;cursor:pointer"><span class="c-flag">\U0001F1E6\U0001F1FA</span><div><div class="c-name">Australia</div><div class="c-count">10,915+ schools</div></div></a>'

    if old_aus not in content:
        print("ERROR: Could not find Australia card. Budget fixed but Australia NOT updated.")
    else:
        content = content.replace(old_aus, new_aus)
        with open(FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print("Done. Homepage budget dropdown now matches USD bands; Australia card no longer says Coming soon.")

if content == original:
    print("WARNING: No changes were made at all.")

"""
Convert the budget filter from AED-only bands/comparison to USD-normalized
bands/comparison, using the new fee_min_usd/fee_max_usd fields. Display
logic (real local currency on cards) is untouched - only the filter itself
changes.

Run from inside ~/Desktop/GlobalCompass
"""

FILE = "schools.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

original = content

old_dropdown = '<select id="budgetSel" class="f-sel"><option value="">All budgets</option><option value="0-20000">Under AED 20,000/yr</option><option value="20000-45000">AED 20,000–45,000/yr</option><option value="45000-75000">AED 45,000–75,000/yr</option><option value="75000-999999">AED 75,000+/yr</option></select>'
new_dropdown = '<select id="budgetSel" class="f-sel"><option value="">All budgets</option><option value="0-5500">Under $5,500/yr</option><option value="5500-12000">$5,500\u2013$12,000/yr</option><option value="12000-20000">$12,000\u2013$20,000/yr</option><option value="20000-999999">$20,000+/yr</option></select>'

if old_dropdown not in content:
    print("ERROR: Could not find AED dropdown. No changes made.")
else:
    content = content.replace(old_dropdown, new_dropdown)

    old_query = '    query = query.lte("fee_min", bMax).gte("fee_max", bMin);'
    new_query = '    query = query.lte("fee_min_usd", bMax).gte("fee_max_usd", bMin);'

    if old_query not in content:
        print("ERROR: Could not find fee query line. Dropdown updated but filter query NOT changed.")
    else:
        content = content.replace(old_query, new_query)
        with open(FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print("Done. Budget filter now uses USD-normalized bands and fields; display logic untouched.")

if content == original:
    print("WARNING: No changes were made at all.")

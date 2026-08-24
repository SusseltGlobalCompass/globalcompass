"""
Add a Public/Private ownership filter dropdown to School Search,
matching the existing age/curriculum/budget filter pattern.
Uses a new 'own' URL parameter (not 'type', which already means
something else - Nursery detection).

Run from inside ~/Desktop/GlobalCompass
"""

FILE = "schools.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

original = content

old_html = '''      <select id="budgetSel" class="f-sel"><option value="">All budgets</option><option value="0-20000">Under AED 20,000/yr</option><option value="20000-45000">AED 20,000–45,000/yr</option><option value="45000-75000">AED 45,000–75,000/yr</option><option value="75000-999999">AED 75,000+/yr</option></select>
      <button class="f-btn" onclick="runSearch()">Search</button>'''
new_html = '''      <select id="budgetSel" class="f-sel"><option value="">All budgets</option><option value="0-20000">Under AED 20,000/yr</option><option value="20000-45000">AED 20,000–45,000/yr</option><option value="45000-75000">AED 45,000–75,000/yr</option><option value="75000-999999">AED 75,000+/yr</option></select>
      <div class="f-div"></div>
      <select id="ownSel" class="f-sel"><option value="">Public &amp; Private</option><option value="Public">Public only</option><option value="Private">Private only</option></select>
      <button class="f-btn" onclick="runSearch()">Search</button>'''

if old_html not in content:
    print("ERROR: Could not find filter-card HTML anchor. No changes made.")
else:
    content = content.replace(old_html, new_html)

    old_read = '  const budget = document.getElementById("budgetSel").value;'
    new_read = '  const budget = document.getElementById("budgetSel").value;\n  const own = document.getElementById("ownSel").value;'

    if old_read not in content:
        print("ERROR: Could not find budget-read line. HTML added but value NOT read.")
    else:
        content = content.replace(old_read, new_read)

        old_url = '  const newUrl = window.location.pathname + "?q=" + encodeURIComponent(q) + "&age=" + age + "&cur=" + cur + "&budget=" + budget;'
        new_url = '  const newUrl = window.location.pathname + "?q=" + encodeURIComponent(q) + "&age=" + age + "&cur=" + cur + "&budget=" + budget + "&own=" + own;'

        if old_url not in content:
            print("ERROR: Could not find URL-building line. Value read but URL NOT updated.")
        else:
            content = content.replace(old_url, new_url)

            old_query = '''  if(budget){
    const [bMin,bMax] = budget.split("-").map(Number);
    query = query.lte("fee_min", bMax).gte("fee_max", bMin);
  }'''
            new_query = '''  if(budget){
    const [bMin,bMax] = budget.split("-").map(Number);
    query = query.lte("fee_min", bMax).gte("fee_max", bMin);
  }
  if(own){
    query = query.eq("school_type", own);
  }'''

            if old_query not in content:
                print("ERROR: Could not find budget query-filter block. URL updated but search filter NOT added.")
            else:
                content = content.replace(old_query, new_query)

                old_apply = '  if(params.budget) document.getElementById("budgetSel").value = params.budget;'
                new_apply = '  if(params.budget) document.getElementById("budgetSel").value = params.budget;\n  if(params.own) document.getElementById("ownSel").value = params.own;'

                if old_apply not in content:
                    print("ERROR: Could not find applyParamsToUI budget line. Filter works but won't restore from URL.")
                else:
                    content = content.replace(old_apply, new_apply)
                    with open(FILE, "w", encoding="utf-8") as f:
                        f.write(content)
                    print("Done. Public/Private ownership filter fully added: dropdown, URL param, query filter, and restore-on-load.")

if content == original:
    print("WARNING: No changes were made at all.")

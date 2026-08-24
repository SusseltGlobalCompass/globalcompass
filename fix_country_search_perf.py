"""
Fix a performance/correctness issue: when a search term resolves to
a real country (e.g. "Brazil"), skip the expensive name/city fuzzy
text search entirely and filter by country_id only. This avoids
combining an expensive OR across three ILIKE scans plus a country
match on a 363,000+ row table, which was timing out (500 error).

Run from inside ~/Desktop/GlobalCompass
"""

FILE = "schools.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

original = content

old_logic = '''  if(q){
    const countryIds = await resolveCountryIds(q);
    const qUnaccented = stripAccents(q);
    let orParts = ["name.ilike.%"+q+"%","city.ilike.%"+q+"%","city_unaccented.ilike.%"+qUnaccented+"%"];
    if(countryIds.length){
      orParts.push("country_id.in.("+countryIds.join(",")+")");
      hintEl.textContent = 'Tip: for more specific results, replace "' + q + '" above with a city name instead, e.g. Sao Paulo or Rio de Janeiro';
      hintEl.style.display = "block";
    }
    query = query.or(orParts.join(","));
  }'''
new_logic = '''  if(q){
    const countryIds = await resolveCountryIds(q);
    if(countryIds.length){
      // The search term matched a real country name exactly - filter by
      // country only, skip the expensive name/city fuzzy search entirely.
      query = query.in("country_id", countryIds);
      hintEl.textContent = 'Tip: for more specific results, replace "' + q + '" above with a city name instead, e.g. Sao Paulo or Rio de Janeiro';
      hintEl.style.display = "block";
    } else {
      const qUnaccented = stripAccents(q);
      query = query.or(["name.ilike.%"+q+"%","city.ilike.%"+q+"%","city_unaccented.ilike.%"+qUnaccented+"%"].join(","));
    }
  }'''

if old_logic not in content:
    print("ERROR: Could not find exact search logic block. No changes made.")
else:
    content = content.replace(old_logic, new_logic)
    with open(FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print("Done. Country-name searches now skip redundant text scanning.")

if content == original:
    print("WARNING: No changes were made at all.")

"""
Add a dynamic hint below the search bar when results are currently
scoped to an entire country (e.g. arrived via a homepage chip), 
nudging the visitor to narrow further by city.

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
    }
    query = query.or(orParts.join(","));
  }'''
new_logic = '''  const hintEl = document.getElementById("cityHint");
  hintEl.style.display = "none";
  if(q){
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

if old_logic not in content:
    print("ERROR: Could not find exact q-search logic block. No changes made.")
else:
    content = content.replace(old_logic, new_logic)
    with open(FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print("Done. City-search hint logic added.")

if content == original:
    print("WARNING: No changes were made at all.")

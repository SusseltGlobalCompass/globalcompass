"""
Add accent-insensitive city search to schools.html, so typing
"sao paulo" (no accent) correctly matches "São Paulo" in the database.

Run from inside ~/Desktop/GlobalCompass
"""

FILE = "schools.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

original = content

old_anchor = "async function resolveCountryIds(q){"
new_anchor = """function stripAccents(str){
  return str.normalize("NFD").replace(/[\\u0300-\\u036f]/g, "");
}

async function resolveCountryIds(q){"""

if old_anchor not in content:
    print("ERROR: Could not find resolveCountryIds anchor. No changes made.")
else:
    content = content.replace(old_anchor, new_anchor, 1)

    old_line = 'let orParts = ["name.ilike.%"+q+"%","city.ilike.%"+q+"%"];'
    new_line = 'const qUnaccented = stripAccents(q);\n    let orParts = ["name.ilike.%"+q+"%","city.ilike.%"+q+"%","city_unaccented.ilike.%"+qUnaccented+"%"];'

    if old_line not in content:
        print("ERROR: Could not find search orParts line. Helper function added but search logic NOT updated.")
    else:
        content = content.replace(old_line, new_line)
        with open(FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print("Done. Accent-insensitive city search added to schools.html.")

if content == original:
    print("WARNING: No changes were made at all.")

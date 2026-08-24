"""
Add Brazil's live schools chip to the homepage, alongside UAE and Australia.
Uses the Americas region colour (#3C8C3C) per Brand Reference, matching
the scalable chip-row pattern.

Run from inside ~/Desktop/GlobalCompass
"""

FILE = "index.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

original = content

old_chips = '''    <a class="region-chip" href="schools.html?q=Australia" style="--rc:#D4A840;--rb:rgba(139,96,0,0.2);--rt:rgba(180,130,0,0.35)">🇦🇺&nbsp;<span id="chipAUS">10,915+</span>&nbsp;Australia</a>
  </div>'''
new_chips = '''    <a class="region-chip" href="schools.html?q=Australia" style="--rc:#D4A840;--rb:rgba(139,96,0,0.2);--rt:rgba(180,130,0,0.35)">🇦🇺&nbsp;<span id="chipAUS">10,915+</span>&nbsp;Australia</a>
    <a class="region-chip" href="schools.html?q=Brazil" style="--rc:#7EC87E;--rb:rgba(26,77,26,0.2);--rt:rgba(60,140,60,0.35)">🇧🇷&nbsp;<span id="chipBR">181,065+</span>&nbsp;Brazil</a>
  </div>'''

if old_chips not in content:
    print("ERROR: Could not find expected chip row. No changes made.")
else:
    content = content.replace(old_chips, new_chips)

    old_script_end = '''  const { count: ausCount } = await sbHome.from('schools').select('*', { count: 'exact', head: true }).eq('country_id', '149c862c-e23b-492d-b051-6f64556905cc');
  if (ausCount) {
    document.getElementById('chipAUS').textContent = ausCount.toLocaleString() + '+';
  }
})();'''
    new_script_end = '''  const { count: ausCount } = await sbHome.from('schools').select('*', { count: 'exact', head: true }).eq('country_id', '149c862c-e23b-492d-b051-6f64556905cc');
  if (ausCount) {
    document.getElementById('chipAUS').textContent = ausCount.toLocaleString() + '+';
  }
  const { count: brCount } = await sbHome.from('schools').select('*', { count: 'exact', head: true }).eq('country_id', 'eb482307-1d5d-4788-b9d9-6d5ca562e6be');
  if (brCount) {
    document.getElementById('chipBR').textContent = brCount.toLocaleString() + '+';
  }
})();'''

    if old_script_end not in content:
        print("ERROR: Supabase script block not found as expected. Chip added but live count NOT wired.")
    else:
        content = content.replace(old_script_end, new_script_end)
        with open(FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print("Done. Brazil chip added to homepage with live Supabase count.")

if content == original:
    print("WARNING: No changes were made at all.")

"""
Add a live Australia schools stat to the homepage, next to the existing
UAE stat. Widens the .stats row and adds flex-wrap for graceful mobile
stacking with 5 items instead of 4.

Run from inside ~/Desktop/GlobalCompass
"""

FILE = "index.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

original = content

old_stats_css = '.stats{display:flex;justify-content:center;gap:0;max-width:540px;margin:0 auto}'
new_stats_css = '.stats{display:flex;flex-wrap:wrap;justify-content:center;gap:0;max-width:660px;margin:0 auto}'

if old_stats_css not in content:
    print("ERROR: .stats CSS rule not found as expected. No changes made.")
else:
    content = content.replace(old_stats_css, new_stats_css)

    old_stat_row = '<div class="stat"><div class="stat-n" id="homeSchoolCount">260+</div><div class="stat-l">UAE Schools</div></div>\n    <div class="stat"><div class="stat-n">190+</div><div class="stat-l">Countries</div></div>'
    new_stat_row = '<div class="stat"><div class="stat-n" id="homeSchoolCount">756+</div><div class="stat-l">UAE Schools</div></div>\n    <div class="stat"><div class="stat-n" id="homeAusSchoolCount">10,915+</div><div class="stat-l">Australia Schools</div></div>\n    <div class="stat"><div class="stat-n">190+</div><div class="stat-l">Countries</div></div>'

    if old_stat_row not in content:
        print("ERROR: Stat row not found as expected. CSS was updated but stat row NOT added.")
    else:
        content = content.replace(old_stat_row, new_stat_row)

        old_script = """  const { count } = await sbHome.from('schools').select('*', { count: 'exact', head: true }).eq('country_id', '9beb50ee-a772-4b1a-b63a-d35a4b0e59e1');
  if (count) {
    document.getElementById('homeSchoolCount').textContent = count + '+';
  }
})();"""
        new_script = """  const { count } = await sbHome.from('schools').select('*', { count: 'exact', head: true }).eq('country_id', '9beb50ee-a772-4b1a-b63a-d35a4b0e59e1');
  if (count) {
    document.getElementById('homeSchoolCount').textContent = count + '+';
  }
  const { count: ausCount } = await sbHome.from('schools').select('*', { count: 'exact', head: true }).eq('country_id', '149c862c-e23b-492d-b051-6f64556905cc');
  if (ausCount) {
    document.getElementById('homeAusSchoolCount').textContent = ausCount.toLocaleString() + '+';
  }
})();"""

        if old_script not in content:
            print("ERROR: Supabase script block not found as expected. Stat row was added but live query NOT added.")
        else:
            content = content.replace(old_script, new_script)
            with open(FILE, "w", encoding="utf-8") as f:
                f.write(content)
            print("Done. Australia stat added to homepage with live Supabase count.")

if content == original:
    print("WARNING: No changes were made at all.")

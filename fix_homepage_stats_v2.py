"""
Revert the main stats row to its clean 3-item original (Countries, Curricula, Free),
and add a separate, scalable country-count chip row (flag + live count) styled
exactly like the existing region-chips, so future countries can be added without
ever breaking the main stats row layout again.

Run from inside ~/Desktop/GlobalCompass
"""

FILE = "index.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

original = content

old_stats_css = '.stats{display:flex;flex-wrap:wrap;justify-content:center;gap:0;max-width:660px;margin:0 auto}'
new_stats_css = '.stats{display:flex;justify-content:center;gap:0;max-width:540px;margin:0 auto}'

if old_stats_css not in content:
    print("ERROR: current .stats CSS not found as expected. No changes made.")
else:
    content = content.replace(old_stats_css, new_stats_css)

    old_stat_block = '''<div class="stat"><div class="stat-n" id="homeSchoolCount">756+</div><div class="stat-l">UAE Schools</div></div>
    <div class="stat"><div class="stat-n" id="homeAusSchoolCount">10,915+</div><div class="stat-l">Australia Schools</div></div>
    <div class="stat"><div class="stat-n">190+</div><div class="stat-l">Countries</div></div>'''
    new_stat_block = '<div class="stat"><div class="stat-n">190+</div><div class="stat-l">Countries</div></div>'

    if old_stat_block not in content:
        print("ERROR: stat block not found as expected. CSS reverted but stat row NOT changed.")
    else:
        content = content.replace(old_stat_block, new_stat_block)

        old_free_close = '<div class="stat"><div class="stat-n">Free</div><div class="stat-l">For every family</div></div>\n  </div>'
        new_free_close = '''<div class="stat"><div class="stat-n">Free</div><div class="stat-l">For every family</div></div>
  </div>
  <div class="region-chips" style="margin-top:16px">
    <a class="region-chip" href="schools.html?q=United Arab Emirates" style="--rc:#F5C842;--rb:rgba(245,200,66,0.15);--rt:rgba(245,200,66,0.35)">🇦🇪&nbsp;<span id="chipUAE">756+</span>&nbsp;UAE</a>
    <a class="region-chip" href="schools.html?q=Australia" style="--rc:#D4A840;--rb:rgba(139,96,0,0.2);--rt:rgba(180,130,0,0.35)">🇦🇺&nbsp;<span id="chipAUS">10,915+</span>&nbsp;Australia</a>
  </div>'''

        if old_free_close not in content:
            print("ERROR: Could not find anchor point to insert country chips. Stats reverted, chips NOT added.")
        else:
            content = content.replace(old_free_close, new_free_close)

            old_script = """  const { count } = await sbHome.from('schools').select('*', { count: 'exact', head: true }).eq('country_id', '9beb50ee-a772-4b1a-b63a-d35a4b0e59e1');
  if (count) {
    document.getElementById('homeSchoolCount').textContent = count + '+';
  }
  const { count: ausCount } = await sbHome.from('schools').select('*', { count: 'exact', head: true }).eq('country_id', '149c862c-e23b-492d-b051-6f64556905cc');
  if (ausCount) {
    document.getElementById('homeAusSchoolCount').textContent = ausCount.toLocaleString() + '+';
  }
})();"""
            new_script = """  const { count } = await sbHome.from('schools').select('*', { count: 'exact', head: true }).eq('country_id', '9beb50ee-a772-4b1a-b63a-d35a4b0e59e1');
  if (count) {
    document.getElementById('chipUAE').textContent = count.toLocaleString() + '+';
  }
  const { count: ausCount } = await sbHome.from('schools').select('*', { count: 'exact', head: true }).eq('country_id', '149c862c-e23b-492d-b051-6f64556905cc');
  if (ausCount) {
    document.getElementById('chipAUS').textContent = ausCount.toLocaleString() + '+';
  }
})();"""

            if old_script not in content:
                print("ERROR: Supabase script block not found as expected. Chips added but live counts NOT wired.")
            else:
                content = content.replace(old_script, new_script)
                with open(FILE, "w", encoding="utf-8") as f:
                    f.write(content)
                print("Done. Stats row reverted to 3 items; UAE + Australia now live in a scalable chip row below.")

if content == original:
    print("WARNING: No changes were made at all.")

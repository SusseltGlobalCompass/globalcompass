"""
Convert Australia's row in countries-oceania.html from "Coming soon"
to a live Supabase-backed schools count, matching the exact pattern
used for UAE on countries-gulf.html.

Run from inside ~/Desktop/GlobalCompass
"""

FILE = "countries-oceania.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

original = content

# 1. Replace Australia's static "Coming soon" row with a live row
old_row = '<div class="country-row"><span class="cn-name">Australia</span><span class="cn-right"><span class="cn-status soon">Coming soon</span></span></div>'
new_row = '<a class="country-row is-live" href="schools.html?q=Australia"><span class="cn-name">Australia</span><span class="cn-right"><span class="cn-status live" id="ausSchoolCount">10,915+ schools</span><i class="ti ti-chevron-right cn-arrow"></i></span></a>'

if old_row not in content:
    print("ERROR: Could not find Australia's row exactly as expected. No changes made.")
else:
    content = content.replace(old_row, new_row)

    # 2. Add the Supabase live-count script before </body>
    old_close = "</div>\n</body>\n</html>"
    new_close = """</div>
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script>
const sb = supabase.createClient("https://qginevdbqaodimcllevb.supabase.co", "sb_publishable_q3hvHIL8bl4oH49Qkyqkgg_w1G2Ud5w");
(async () => {
  const { count } = await sb.from('schools').select('*', { count: 'exact', head: true }).eq('country_id', '149c862c-e23b-492d-b051-6f64556905cc');
  if (count) {
    document.getElementById('ausSchoolCount').textContent = count + '+ schools';
  }
})();
</script>
</body>
</html>"""

    if old_close not in content:
        print("ERROR: Could not find expected closing tags. Row was updated but script NOT added.")
    else:
        content = content.replace(old_close, new_close)
        with open(FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print("Done. Australia row converted to live status, Supabase script added.")

if content == original:
    print("WARNING: No changes were made at all.")

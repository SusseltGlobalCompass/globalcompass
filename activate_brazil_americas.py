"""
Convert Brazil's row in countries-americas.html from "Coming soon"
to a live Supabase-backed schools count, matching the exact pattern
used for UAE (Gulf) and Australia (Oceania). Adds INEP attribution
per the CC BY licence requirement.

Run from inside ~/Desktop/GlobalCompass
"""

FILE = "countries-americas.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

original = content

old_row = '<div class="country-row"><span class="cn-name">Brazil</span><span class="cn-right"><span class="cn-status soon">Coming soon</span></span></div>'
new_row = '<a class="country-row is-live" href="schools.html?q=Brazil"><span class="cn-name">Brazil</span><span class="cn-right"><span class="cn-status live" id="brSchoolCount">181,065+ schools</span><i class="ti ti-chevron-right cn-arrow"></i></span></a>'

if old_row not in content:
    print("ERROR: Could not find Brazil's row exactly as expected. No changes made.")
else:
    content = content.replace(old_row, new_row)

    old_close = """  </div>
</div>
</body>
</html>"""
    new_close = """  </div>
  <p style="font-size:11px;color:#9AB0D0;text-align:center;margin-top:18px;padding:0 20px;line-height:1.6;font-family:'Inter',sans-serif">Brazilian school data provided by <a href="https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/inep-data/catalogo-de-escolas" target="_blank" rel="noopener" style="color:#7A8BAE;text-decoration:underline">INEP</a> (Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira), Catálogo de Escolas, licensed under <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener" style="color:#7A8BAE;text-decoration:underline">CC BY 4.0</a>.</p>
</div>
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script>
const sb = supabase.createClient("https://qginevdbqaodimcllevb.supabase.co", "sb_publishable_q3hvHIL8bl4oH49Qkyqkgg_w1G2Ud5w");
(async () => {
  const { count } = await sb.from('schools').select('*', { count: 'exact', head: true }).eq('country_id', 'eb482307-1d5d-4788-b9d9-6d5ca562e6be');
  if (count) {
    document.getElementById('brSchoolCount').textContent = count.toLocaleString() + '+ schools';
  }
})();
</script>
</body>
</html>"""

    if old_close not in content:
        print("ERROR: Could not find expected closing tags. Row was updated but script/attribution NOT added.")
    else:
        content = content.replace(old_close, new_close)
        with open(FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print("Done. Brazil row converted to live status, INEP attribution added, Supabase script added.")

if content == original:
    print("WARNING: No changes were made at all.")

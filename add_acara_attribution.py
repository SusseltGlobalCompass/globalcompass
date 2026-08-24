"""
Add ACARA data attribution to countries-oceania.html, satisfying the
CC BY 4.0 licence requirement for the Australian Schools List data.

Run from inside ~/Desktop/GlobalCompass
"""

FILE = "countries-oceania.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

original = content

old_block = """  <div class="country-row"><span class="cn-name">Fiji</span><span class="cn-right"><span class="cn-status soon">Coming soon</span></span></div>
  </div>
</div>"""

new_block = """  <div class="country-row"><span class="cn-name">Fiji</span><span class="cn-right"><span class="cn-status soon">Coming soon</span></span></div>
  </div>
  <p style="font-size:11px;color:#9AB0D0;text-align:center;margin-top:18px;padding:0 20px;line-height:1.6;font-family:'Inter',sans-serif">Australian school data provided by <a href="https://asl.acara.edu.au/" target="_blank" rel="noopener" style="color:#7A8BAE;text-decoration:underline">ACARA</a> (Australian Curriculum, Assessment and Reporting Authority), Australian Schools List, licensed under <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener" style="color:#7A8BAE;text-decoration:underline">CC BY 4.0</a>.</p>
</div>"""

if old_block not in content:
    print("ERROR: Could not find expected block. No changes made.")
else:
    content = content.replace(old_block, new_block)
    with open(FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print("Done. ACARA attribution added below the country list.")

if content == original:
    print("WARNING: No changes were made at all.")

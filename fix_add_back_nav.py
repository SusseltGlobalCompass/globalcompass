"""
Add a "Change my background" link on Step 2, allowing the visitor to
go back to Step 1 to change curriculum/language answers - currently
the only navigation option was "Check a different university" which
only returns to Step 2, not Step 1.

Run from inside ~/Desktop/GlobalCompass
"""

FILE = "university-requirements.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

original = content

old_block = '''  <div id="step2" class="card" style="display:none">
    <div class="card-title">Choose your target university</div>
    <div class="card-sub">Select the university you'd like to check requirements for.</div>
    <div id="uniList"><div class="loading-state">Loading universities...</div></div>
  </div>'''

new_block = '''  <div id="step2" class="card" style="display:none">
    <div class="card-title">Choose your target university</div>
    <div class="card-sub">Select the university you'd like to check requirements for.</div>
    <div id="uniList"><div class="loading-state">Loading universities...</div></div>
    <button class="btn-secondary" onclick="goStep(1)">\u2190 Change my background</button>
  </div>'''

if old_block not in content:
    print("ERROR: Could not find Step 2 block exactly. No changes made.")
else:
    content = content.replace(old_block, new_block)
    with open(FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print("Done. 'Change my background' link added to Step 2.")

if content == original:
    print("WARNING: No changes were made at all.")

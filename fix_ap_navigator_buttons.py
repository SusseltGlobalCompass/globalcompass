path = "american-pathway-navigator.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''      <div class="action-row">
        <button class="action-btn" style="background:#1B3A7A;color:#F5C842" onclick="apGoStep(1)">Start again</button>
        <button class="action-btn" style="background:#F5C842;color:#1B3A7A" onclick="switchModule('sat')">Plan my SAT strategy ↗</button>
        <button class="action-btn" style="background:#EEF3FF;color:#2952A3" onclick="window.location.href='index.html'">Find AP schools ↗</button>
      </div>'''

new = '''      <div class="action-row">
        <button class="action-btn" style="background:#1B3A7A;color:#F5C842" onclick="apGoStep(1)">Start again</button>
        <button class="action-btn" style="background:#F5C842;color:#1B3A7A" onclick="switchModule('sat')">Plan my SAT strategy ↗</button>
        <button class="action-btn" style="background:#EEF3FF;color:#2952A3" onclick="window.location.href='schools.html?cur=American'">Find AP schools ↗</button>
        <button class="action-btn" style="background:#EEF3FF;color:#2952A3" onclick="window.location.href='index.html'">Back to GlobalCompass ↗</button>
      </div>'''

count = content.count(old)
if count != 1:
    raise SystemExit(f"ABORTED: expected 1 match, found {count}. No changes made.")

content = content.replace(old, new, 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done. AP results now has a real 'Find AP schools' link and a genuine 'Back to GlobalCompass' button.")

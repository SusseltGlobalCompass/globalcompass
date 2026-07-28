"""
Recolor career-simulator.html (A-Levels / Sixth Form Navigator)
from Royal Blue / Mid Blue to Oxford Burgundy, to match the
British A-Levels curriculum colour (#6B1E3A) per Brand Reference.

Run from inside ~/Desktop/GlobalCompass
"""

import re

FILE = "career-simulator.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

original = content

# 1. Hero bar gradient: #1B3A7A -> #2952A3  becomes  #6B1E3A -> #3D0B1F
content = content.replace(
    "background:linear-gradient(135deg,#1B3A7A,#2952A3)",
    "background:linear-gradient(135deg,#6B1E3A,#3D0B1F)"
)

# 2. Progress bar fill gradient: #1B3A7A -> gold  becomes  #6B1E3A -> gold
content = content.replace(
    "background:linear-gradient(90deg,#1B3A7A,#F5C842)",
    "background:linear-gradient(90deg,#6B1E3A,#F5C842)"
)

# 3. "Essential" subject card bg + border
content = content.replace(
    ".subject-card.essential{background:#1B3A7A;border-color:#1B3A7A}",
    ".subject-card.essential{background:#6B1E3A;border-color:#6B1E3A}"
)

# 4. Hidden requirements title colour
content = content.replace(
    ".hidden-req-title{font-size:12px;font-weight:700;color:#1B3A7A;",
    ".hidden-req-title{font-size:12px;font-weight:700;color:#6B1E3A;"
)

# 5. Workload percentage text colour
content = content.replace(
    ".workload-pct{font-size:12px;font-weight:700;color:#1B3A7A}",
    ".workload-pct{font-size:12px;font-weight:700;color:#6B1E3A}"
)

# 6. UCAS box background
content = content.replace(
    ".ucas-box{background:#1B3A7A;",
    ".ucas-box{background:#6B1E3A;"
)

# 7. "Start again" button (inline style)
content = content.replace(
    'style="background:#1B3A7A;color:#F5C842" onclick="goStep(1)"',
    'style="background:#6B1E3A;color:#F5C842" onclick="goStep(1)"'
)

# 8. Gold "Find schools" button text colour (inline style)
content = content.replace(
    'style="background:#F5C842;color:#1B3A7A" onclick="window.location.href=\'index.html\'">Find schools',
    'style="background:#F5C842;color:#6B1E3A" onclick="window.location.href=\'index.html\'">Find schools'
)

# 9. Result tag background/text (#EEF3FF bg, #2952A3 text) -> keep bg, change text
content = content.replace(
    ".result-tag{display:inline-flex;align-items:center;gap:6px;font-size:10px;padding:4px 12px;border-radius:99px;background:#EEF3FF;color:#2952A3;",
    ".result-tag{display:inline-flex;align-items:center;gap:6px;font-size:10px;padding:4px 12px;border-radius:99px;background:#EEF3FF;color:#6B1E3A;"
)

# 10. AI label accent text colour
content = content.replace(
    ".ai-label{font-size:10px;font-weight:700;color:#2952A3;",
    ".ai-label{font-size:10px;font-weight:700;color:#6B1E3A;"
)

# 11. "Back to GlobalCompass" button (#EEF3FF bg, #2952A3 text) -> change text to burgundy
content = content.replace(
    'style="background:#EEF3FF;color:#2952A3" onclick="window.location.href=\'index.html\'">Back to GlobalCompass',
    'style="background:#EEF3FF;color:#6B1E3A" onclick="window.location.href=\'index.html\'">Back to GlobalCompass'
)

if content == original:
    print("WARNING: No changes were made. Check that the file matches expected patterns.")
else:
    with open(FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print("Done. career-simulator.html recolored from Royal Blue to Oxford Burgundy.")

# Report any remaining #1B3A7A / #2952A3 usages so we can review manually
remaining_royal = len(re.findall(r"#1B3A7A", content))
remaining_mid = len(re.findall(r"#2952A3", content))
print(f"Remaining #1B3A7A occurrences: {remaining_royal}")
print(f"Remaining #2952A3 occurrences: {remaining_mid}")

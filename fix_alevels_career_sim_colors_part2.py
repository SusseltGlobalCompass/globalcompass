"""
Part 2: Recolor remaining page-specific UI elements in career-simulator.html
from Royal Blue / Mid Blue to Oxford Burgundy.
Leaves the top .nav bar (brand-wide chrome) untouched.

Run from inside ~/Desktop/GlobalCompass
"""

import re

FILE = "career-simulator.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

original = content

replacements = [
    # Step circle "done" state
    (".step-circle.done{background:#F5C842;color:#1B3A7A}",
     ".step-circle.done{background:#F5C842;color:#6B1E3A}"),

    # Step circle "active" state
    (".step-circle.active{background:#1B3A7A;color:#F5C842;border:2px solid #F5C842}",
     ".step-circle.active{background:#6B1E3A;color:#F5C842;border:2px solid #F5C842}"),

    # Step label active text
    (".step-label.active{color:#1B3A7A;font-weight:700}",
     ".step-label.active{color:#6B1E3A;font-weight:700}"),

    # Dream input focus border
    (".dream-input:focus{border-color:#1B3A7A}",
     ".dream-input:focus{border-color:#6B1E3A}"),

    # Example pill text colour
    (".ep{font-size:11px;padding:5px 12px;border-radius:99px;border:0.5px solid #C0D0E8;color:#2952A3;",
     ".ep{font-size:11px;padding:5px 12px;border-radius:99px;border:0.5px solid #C0D0E8;color:#6B1E3A;"),

    # Example pill hover state
    (".ep:hover{background:#1B3A7A;color:#F5C842;border-color:#1B3A7A}",
     ".ep:hover{background:#6B1E3A;color:#F5C842;border-color:#6B1E3A}"),

    # Option card hover border
    (".opt-card:hover{border-color:#2952A3;background:#EEF3FF}",
     ".opt-card:hover{border-color:#6B1E3A;background:#EEF3FF}"),

    # Option card selected border
    (".opt-card.selected{border-color:#1B3A7A;background:#EEF3FF}",
     ".opt-card.selected{border-color:#6B1E3A;background:#EEF3FF}"),

    # "Next" button
    (".btn-next{font-size:13px;padding:9px 24px;border-radius:99px;border:none;background:#1B3A7A;color:#F5C842;",
     ".btn-next{font-size:13px;padding:9px 24px;border-radius:99px;border:none;background:#6B1E3A;color:#F5C842;"),

    # "Next" button gold variant text
    (".btn-next.gold{background:#F5C842;color:#1B3A7A}",
     ".btn-next.gold{background:#F5C842;color:#6B1E3A}"),

    # "Recommended" badge text
    (".badge-recommended{background:#C0D0E8;color:#2952A3}",
     ".badge-recommended{background:#C0D0E8;color:#6B1E3A}"),
]

made = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        made += 1
    else:
        print(f"NOT FOUND (skipped): {old[:70]}...")

if content == original:
    print("WARNING: No changes were made.")
else:
    with open(FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Done. {made} of {len(replacements)} replacements applied.")

remaining_royal = len(re.findall(r"#1B3A7A", content))
remaining_mid = len(re.findall(r"#2952A3", content))
print(f"Remaining #1B3A7A occurrences (should be 1, the .nav bar): {remaining_royal}")
print(f"Remaining #2952A3 occurrences (should be 0): {remaining_mid}")

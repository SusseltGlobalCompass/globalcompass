"""
Recolor american-pathway-navigator.html from Royal Blue / Mid Blue
to Deep Indigo (#2D1B6E), to match the American AP curriculum colour
per Brand Reference. Leaves the top .nav bar (brand-wide chrome) untouched,
and leaves the unrelated green .savings-box gradient untouched.

Run from inside ~/Desktop/GlobalCompass
"""

import re

FILE = "american-pathway-navigator.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

original = content

replacements = [
    # Hero gradient
    (".hero-bar{background:linear-gradient(135deg,#0D1F4A,#1B3A7A);padding:28px 24px;text-align:center;border-bottom:2px solid #F5C842}",
     ".hero-bar{background:linear-gradient(135deg,#2D1B6E,#1A0F42);padding:28px 24px;text-align:center;border-bottom:2px solid #F5C842}"),

    # Active tab
    (".tab.active{background:#1B3A7A;color:#F5C842}",
     ".tab.active{background:#2D1B6E;color:#F5C842}"),

    # Step circle done
    (".step-circle.done{background:#F5C842;color:#1B3A7A}",
     ".step-circle.done{background:#F5C842;color:#2D1B6E}"),

    # Step circle active
    (".step-circle.active{background:#1B3A7A;color:#F5C842;border:2px solid #F5C842}",
     ".step-circle.active{background:#2D1B6E;color:#F5C842;border:2px solid #F5C842}"),

    # Step label active
    (".step-label.active{color:#1B3A7A;font-weight:700}",
     ".step-label.active{color:#2D1B6E;font-weight:700}"),

    # Option card hover border
    (".opt-card:hover{border-color:#2952A3;background:#EEF3FF}",
     ".opt-card:hover{border-color:#2D1B6E;background:#EEF3FF}"),

    # Option card selected border
    (".opt-card.selected{border-color:#1B3A7A;background:#EEF3FF}",
     ".opt-card.selected{border-color:#2D1B6E;background:#EEF3FF}"),

    # Dream input focus
    (".dream-input:focus{border-color:#1B3A7A}",
     ".dream-input:focus{border-color:#2D1B6E}"),

    # Example pill text
    (".ep{font-size:11px;padding:5px 12px;border-radius:99px;border:0.5px solid #C0D0E8;color:#2952A3;cursor:pointer;background:#EEF3FF;font-family:'Twemoji Country Flags','Inter',sans-serif;transition:all 0.15s;font-weight:500}",
     ".ep{font-size:11px;padding:5px 12px;border-radius:99px;border:0.5px solid #C0D0E8;color:#2D1B6E;cursor:pointer;background:#EEF3FF;font-family:'Twemoji Country Flags','Inter',sans-serif;transition:all 0.15s;font-weight:500}"),

    # Example pill hover
    (".ep:hover{background:#1B3A7A;color:#F5C842;border-color:#1B3A7A}",
     ".ep:hover{background:#2D1B6E;color:#F5C842;border-color:#2D1B6E}"),

    # Next button
    (".btn-next{font-size:13px;padding:9px 24px;border-radius:99px;border:none;background:#1B3A7A;color:#F5C842;cursor:pointer;font-family:'Twemoji Country Flags','Montserrat',sans-serif;font-weight:700}",
     ".btn-next{font-size:13px;padding:9px 24px;border-radius:99px;border:none;background:#2D1B6E;color:#F5C842;cursor:pointer;font-family:'Twemoji Country Flags','Montserrat',sans-serif;font-weight:700}"),

    # Next button gold variant
    (".btn-next.gold{background:#F5C842;color:#1B3A7A}",
     ".btn-next.gold{background:#F5C842;color:#2D1B6E}"),

    # Result tag text
    (".result-tag{display:inline-flex;align-items:center;gap:6px;font-size:10px;padding:4px 12px;border-radius:99px;background:#EEF3FF;color:#2952A3;margin-bottom:10px;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;font-family:'Twemoji Country Flags','Montserrat',sans-serif}",
     ".result-tag{display:inline-flex;align-items:center;gap:6px;font-size:10px;padding:4px 12px;border-radius:99px;background:#EEF3FF;color:#2D1B6E;margin-bottom:10px;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;font-family:'Twemoji Country Flags','Montserrat',sans-serif}"),

    # "Essential" AP subject card
    (".ap-card.essential{background:#1B3A7A}",
     ".ap-card.essential{background:#2D1B6E}"),

    # "Recommended" badge text
    (".badge-recommended{background:#C0D0E8;color:#2952A3}",
     ".badge-recommended{background:#C0D0E8;color:#2D1B6E}"),

    # AP score dark text
    (".ap-score-dark{font-size:10px;color:#2952A3;margin-bottom:4px}",
     ".ap-score-dark{font-size:10px;color:#2D1B6E;margin-bottom:4px}"),

    # SAT box background
    (".sat-box{background:#1B3A7A;border-radius:14px;padding:18px;margin-bottom:14px}",
     ".sat-box{background:#2D1B6E;border-radius:14px;padding:18px;margin-bottom:14px}"),

    # Timeline title
    (".timeline-title{font-family:'Twemoji Country Flags','Montserrat',sans-serif;font-size:11px;font-weight:700;color:#1B3A7A;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:12px}",
     ".timeline-title{font-family:'Twemoji Country Flags','Montserrat',sans-serif;font-size:11px;font-weight:700;color:#2D1B6E;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:12px}"),

    # Timeline year
    (".timeline-year{font-size:10px;font-weight:700;color:#1B3A7A;font-family:'Twemoji Country Flags','Montserrat',sans-serif;margin-bottom:3px;text-transform:uppercase;letter-spacing:0.06em}",
     ".timeline-year{font-size:10px;font-weight:700;color:#2D1B6E;font-family:'Twemoji Country Flags','Montserrat',sans-serif;margin-bottom:3px;text-transform:uppercase;letter-spacing:0.06em}"),

    # Hidden requirements title
    (".hidden-title{font-size:12px;font-weight:700;color:#1B3A7A;margin-bottom:8px;font-family:'Twemoji Country Flags','Montserrat',sans-serif;text-transform:uppercase;letter-spacing:0.06em}",
     ".hidden-title{font-size:12px;font-weight:700;color:#2D1B6E;margin-bottom:8px;font-family:'Twemoji Country Flags','Montserrat',sans-serif;text-transform:uppercase;letter-spacing:0.06em}"),

    # AI label
    (".ai-label{font-size:10px;font-weight:700;color:#2952A3;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:6px;font-family:'Twemoji Country Flags','Montserrat',sans-serif}",
     ".ai-label{font-size:10px;font-weight:700;color:#2D1B6E;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:6px;font-family:'Twemoji Country Flags','Montserrat',sans-serif}"),

    # Inline buttons - "Start again" (apGoStep)
    ('<button class="action-btn" style="background:#1B3A7A;color:#F5C842" onclick="apGoStep(1)">Start again</button>',
     '<button class="action-btn" style="background:#2D1B6E;color:#F5C842" onclick="apGoStep(1)">Start again</button>'),

    # Inline buttons - "Plan my SAT strategy"
    ('<button class="action-btn" style="background:#F5C842;color:#1B3A7A" onclick="switchModule(\'sat\')">Plan my SAT strategy ↗</button>',
     '<button class="action-btn" style="background:#F5C842;color:#2D1B6E" onclick="switchModule(\'sat\')">Plan my SAT strategy ↗</button>'),

    # Inline buttons - "Find AP schools"
    ('<button class="action-btn" style="background:#EEF3FF;color:#2952A3" onclick="window.location.href=\'schools.html?cur=American\'">Find AP schools ↗</button>',
     '<button class="action-btn" style="background:#EEF3FF;color:#2D1B6E" onclick="window.location.href=\'schools.html?cur=American\'">Find AP schools ↗</button>'),

    # Inline buttons - "Start again" (resetSat)
    ('<button class="action-btn" style="background:#1B3A7A;color:#F5C842" onclick="resetSat()">Start again</button>',
     '<button class="action-btn" style="background:#2D1B6E;color:#F5C842" onclick="resetSat()">Start again</button>'),

    # Inline buttons - "Plan my AP subjects"
    ('<button class="action-btn" style="background:#F5C842;color:#1B3A7A" onclick="switchModule(\'ap\')">Plan my AP subjects ↗</button>',
     '<button class="action-btn" style="background:#F5C842;color:#2D1B6E" onclick="switchModule(\'ap\')">Plan my AP subjects ↗</button>'),
]

made = 0
for old, new in replacements:
    count = content.count(old)
    if count == 0:
        print(f"NOT FOUND (skipped): {old[:70]}...")
    else:
        content = content.replace(old, new)
        made += count

if content == original:
    print("WARNING: No changes were made.")
else:
    with open(FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Done. {made} replacement(s) applied across {len(replacements)} patterns.")

# Note: 2 x "Back to GlobalCompass" buttons use #2952A3 -> also convert those
back_old = "color:#2952A3\" onclick=\"window.location.href='index.html'\">Back to GlobalCompass"
back_new = "color:#2D1B6E\" onclick=\"window.location.href='index.html'\">Back to GlobalCompass"
back_count = content.count(back_old)
if back_count:
    content = content.replace(back_old, back_new)
    with open(FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Also converted {back_count} 'Back to GlobalCompass' button(s).")

remaining_royal = len(re.findall(r"#1B3A7A", content))
remaining_mid = len(re.findall(r"#2952A3", content))
print(f"Remaining #1B3A7A occurrences (should be 1, the .nav bar): {remaining_royal}")
print(f"Remaining #2952A3 occurrences (should be 0): {remaining_mid}")

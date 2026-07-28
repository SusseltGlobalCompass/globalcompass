path = "ib-pathway-navigator.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

def apply(name, old, new, c):
    cnt = c.count(old)
    if cnt != 1:
        raise SystemExit(f"ABORTED at '{name}': expected 1 match, found {cnt}.")
    return c.replace(old, new, 1)

# Liberty Green palette: #1A4D1A (official primary), #0D2E14 (dark gradient partner), #2D6B2D (mid tone), #EAF3EA (light tint)

content = apply("hero-bar gradient",
    '.hero-bar{background:linear-gradient(135deg,#0D1F4A,#1B3A7A);padding:28px 24px;text-align:center;border-bottom:2px solid #F5C842}',
    '.hero-bar{background:linear-gradient(135deg,#0D2E14,#1A4D1A);padding:28px 24px;text-align:center;border-bottom:2px solid #F5C842}',
    content)

content = apply("step-circle.active",
    '.step-circle.active{background:#1B3A7A;color:#F5C842;border:2px solid #F5C842}',
    '.step-circle.active{background:#1A4D1A;color:#F5C842;border:2px solid #F5C842}',
    content)

content = apply("opt-card:hover",
    '.opt-card:hover{border-color:#2952A3;background:#EEF3FF}',
    '.opt-card:hover{border-color:#2D6B2D;background:#EAF3EA}',
    content)

content = apply("opt-card.selected",
    '.opt-card.selected{border-color:#1B3A7A;background:#EEF3FF}',
    '.opt-card.selected{border-color:#1A4D1A;background:#EAF3EA}',
    content)

content = apply("dream-input:focus",
    '.dream-input:focus{border-color:#1B3A7A}',
    '.dream-input:focus{border-color:#1A4D1A}',
    content)

content = apply(".ep:hover",
    '.ep:hover{background:#1B3A7A;color:#F5C842;border-color:#1B3A7A}',
    '.ep:hover{background:#1A4D1A;color:#F5C842;border-color:#1A4D1A}',
    content)

content = apply("btn-next",
    ".btn-next{font-size:13px;padding:9px 24px;border-radius:99px;border:none;background:#1B3A7A;color:#F5C842;cursor:pointer;font-family:'Twemoji Country Flags','Montserrat',sans-serif;font-weight:700}",
    ".btn-next{font-size:13px;padding:9px 24px;border-radius:99px;border:none;background:#1A4D1A;color:#F5C842;cursor:pointer;font-family:'Twemoji Country Flags','Montserrat',sans-serif;font-weight:700}",
    content)

content = apply("result-tag",
    ".result-tag{display:inline-flex;align-items:center;gap:6px;font-size:10px;padding:4px 12px;border-radius:99px;background:#EEF3FF;color:#2952A3;margin-bottom:10px;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;font-family:'Twemoji Country Flags','Montserrat',sans-serif}",
    ".result-tag{display:inline-flex;align-items:center;gap:6px;font-size:10px;padding:4px 12px;border-radius:99px;background:#EAF3EA;color:#2D6B2D;margin-bottom:10px;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;font-family:'Twemoji Country Flags','Montserrat',sans-serif}",
    content)

content = apply("hidden-title",
    ".hidden-title{font-size:12px;font-weight:700;color:#1B3A7A;margin-bottom:8px;font-family:'Twemoji Country Flags','Montserrat',sans-serif;text-transform:uppercase;letter-spacing:0.06em}",
    ".hidden-title{font-size:12px;font-weight:700;color:#1A4D1A;margin-bottom:8px;font-family:'Twemoji Country Flags','Montserrat',sans-serif;text-transform:uppercase;letter-spacing:0.06em}",
    content)

content = apply("ai-label",
    ".ai-label{font-size:10px;font-weight:700;color:#2952A3;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:6px;font-family:'Twemoji Country Flags','Montserrat',sans-serif}",
    ".ai-label{font-size:10px;font-weight:700;color:#2D6B2D;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:6px;font-family:'Twemoji Country Flags','Montserrat',sans-serif}",
    content)

content = apply("action-btn Start again",
    '<button class="action-btn" style="background:#1B3A7A;color:#F5C842" onclick="goStep(1)">Start again</button>',
    '<button class="action-btn" style="background:#1A4D1A;color:#F5C842" onclick="goStep(1)">Start again</button>',
    content)

# Sticky step indicator (matching other navigators)
content = apply("sticky",
    '.step-indicator{display:flex;align-items:center;margin-bottom:24px}',
    '.step-indicator{display:flex;align-items:center;margin-bottom:24px;position:sticky;top:0;background:#F8F9FF;padding:12px 0;z-index:5}',
    content)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("IB corrected to Liberty Green palette (11 targeted replacements), nav bar untouched, sticky stepper added.")

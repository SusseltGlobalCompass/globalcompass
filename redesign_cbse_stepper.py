path = "cbse-stream-navigator.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

edits = []

def apply(name, old, new):
    global content
    c = content.count(old)
    if c != 1:
        raise SystemExit(f"ABORTED at '{name}': expected 1 match, found {c}. No changes made yet.")
    content = content.replace(old, new, 1)
    edits.append(name)

# 1. Make the step indicator sticky
apply("sticky step-indicator",
    '.step-indicator{display:flex;align-items:center;margin-bottom:24px}',
    '.step-indicator{display:flex;align-items:center;margin-bottom:24px;position:sticky;top:0;background:#F8F9FF;padding:12px 0;z-index:5}')

# 2. Rename the step label from Context to Roots
apply("step label rename",
    '<div class="step"><div class="step-circle pending" id="sc4">4</div><div class="step-label">Context</div></div>',
    '<div class="step"><div class="step-circle pending" id="sc4">4</div><div class="step-label">Roots</div></div>')

# 3. Update the button text leading into step 4
apply("nav button into step 4",
    'Next — Your context →',
    'Next — Your roots →')

# 4. Reword the sensitive option card with warmer, dual-honoring language
apply("family option reword",
    '''<div class="opt-card" onclick="selectContext(this,'Family pressure towards Science stream but unsure if right choice')"><span class="opt-emoji">💭</span><div class="opt-title">Family pressure — Science stream</div><div class="opt-sub">Family wants Science but I am unsure</div></div>''',
    '''<div class="opt-card" onclick="selectContext(this,'Honoring family hopes for Science or Medicine, while exploring what feels right for me too')"><span class="opt-emoji">💭</span><div class="opt-title">Honoring family, finding myself</div><div class="opt-sub">My family hopes for Science or Medicine, and I want to explore what's truly right for me too</div></div>''')

# 5. Final CTA button, tying into the map metaphor
apply("final CTA button",
    'Generate my CBSE pathway ↗',
    'Draw my CBSE map ↗')

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("All edits applied successfully:")
for e in edits:
    print(" -", e)

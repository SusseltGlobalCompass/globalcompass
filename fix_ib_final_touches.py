path = "ib-pathway-navigator.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

def apply(name, old, new, c):
    cnt = c.count(old)
    if cnt != 1:
        raise SystemExit(f"ABORTED at '{name}': expected 1 match, found {cnt}.")
    return c.replace(old, new, 1)

content = apply("final CTA",
    'Generate my IB pathway ↗',
    'Draw my IB map ↗',
    content)

content = apply("Find IB schools color",
    '''<button class="action-btn" style="background:#F5C842;color:#1B3A7A" onclick="window.location.href='schools.html?cur=IB'">Find IB schools ↗</button>''',
    '''<button class="action-btn" style="background:#F5C842;color:#1A4D1A" onclick="window.location.href='schools.html?cur=IB'">Find IB schools ↗</button>''',
    content)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Final CTA renamed to 'Draw my IB map'. Find IB schools button now uses Liberty Green.")

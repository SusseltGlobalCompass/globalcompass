path = "australian-vce-navigator.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

before_red = content.count("#CC0000")
before_navy = content.count("#00008B")

content = content.replace("#CC0000", "#8B6000")
content = content.replace("#00008B", "#8B6000")

# Sticky step indicator
old_sticky = '.step-indicator{display:flex;align-items:center;margin-bottom:24px}'
new_sticky = '.step-indicator{display:flex;align-items:center;margin-bottom:24px;position:sticky;top:0;background:#F8F9FF;padding:12px 0;z-index:5}'
count = content.count(old_sticky)
if count != 1:
    raise SystemExit(f"ABORTED at sticky: expected 1 match, found {count}")
content = content.replace(old_sticky, new_sticky, 1)

# Final CTA wording
old_cta = 'Generate my VCE pathway ↗'
new_cta = 'Draw my VCE map ↗'
count2 = content.count(old_cta)
if count2 != 1:
    raise SystemExit(f"ABORTED at CTA: expected 1 match, found {count2}")
content = content.replace(old_cta, new_cta, 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Replaced {before_red} instances of #CC0000 and {before_navy} instances of #00008B with #8B6000 (Ochre Gold).")
print("Sticky positioning added. Final CTA updated to 'Draw my VCE map'.")

path = "academic-passport.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

old = '<p class="hero-p">Your private academic record across any curriculum — IB, A-Levels, AP, or General grading, even more than one at once. See exactly what you need for your target university, and know your data disappears the moment you no longer need it.</p>'

new = old + '\n  <div style="font-size:11px;color:#A8C4F5;background:rgba(255,255,255,0.06);border-radius:8px;padding:10px 14px;margin:12px auto 0;max-width:520px">GlobalCompass provides general guidance to help you plan &mdash; always verify official requirements and deadlines directly with your target university before making any decisions. GlobalCompass is not responsible for outcomes based on information that changes after publication, or for decisions made using this tool alone.</div>'

count = content.count(old)
if count != 1:
    raise SystemExit(f"ABORTED: expected 1 match, found {count}. No changes made.")

content = content.replace(old, new, 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done. Disclaimer added to Track My Scores, right after the hero intro.")

path = "subject-explorer.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

old = '<p class="hero-p">Honest, human descriptions of every subject — what it is really like, who it suits, what doors it opens, and one thing about it that might genuinely surprise you.</p>'

new = old + '\n  <div style="font-size:11px;color:#A8C4F5;background:rgba(255,255,255,0.06);border-radius:8px;padding:10px 14px;margin:12px auto 0;max-width:540px;position:relative;z-index:1">GlobalCompass provides general guidance to help you plan &mdash; always verify official requirements and deadlines directly with your target university before making any decisions. GlobalCompass is not responsible for outcomes based on information that changes after publication, or for decisions made using this tool alone.</div>'

count = content.count(old)
if count != 1:
    raise SystemExit(f"ABORTED: expected 1 match, found {count}. No changes made.")

content = content.replace(old, new, 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done. Disclaimer added to Subject Explorer.")

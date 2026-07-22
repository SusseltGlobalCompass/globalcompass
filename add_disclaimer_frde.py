DISCLAIMER_HTML = '<div style="font-size:11px;color:#7A8BAE;background:#F8F9FF;border-radius:8px;padding:10px 14px;margin:10px 0">GlobalCompass provides general guidance to help you plan &mdash; always verify official requirements and deadlines directly with your target university before making any decisions. GlobalCompass is not responsible for outcomes based on information that changes after publication, or for decisions made using this tool alone.</div>'

fixes = [
    ("french-bac-navigator.html",
     '''<div class="card"><div class="ai-label" style="font-size:10px;font-weight:700;color:#0055A4;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:6px;font-family:'Montserrat',sans-serif" id="insightLabel">GlobalCompass insight</div><div style="background:#EEF3FF;border-radius:0 12px 12px 12px;padding:14px 16px;border:0.5px solid #C0D0E8"><p style="font-size:13px;color:#0D1F4A;line-height:1.7" id="aiInsight"></p></div></div>''',
     None),
    ("german-abitur-navigator.html",
     '''<div class="card"><div style="font-size:10px;font-weight:700;color:#DD0000;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:6px;font-family:'Montserrat',sans-serif" id="insightLabel">GlobalCompass insight</div><div style="background:#FFF0F0;border-radius:0 12px 12px 12px;padding:14px 16px;border:0.5px solid #FFD0D0"><p style="font-size:13px;color:#0D1F4A;line-height:1.7" id="aiInsight"></p></div></div>''',
     None),
]

for path, old, _ in fixes:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    count = content.count(old)
    if count != 1:
        print(f"SKIPPED {path}: expected 1 match, found {count} — check manually.")
        continue
    new = old + "\n    " + DISCLAIMER_HTML
    content = content.replace(old, new, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Added disclaimer to {path}")

print("Done.")

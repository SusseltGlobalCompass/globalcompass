DISCLAIMER_HTML = '<div style="font-size:11px;color:#7A8BAE;background:#F8F9FF;border-radius:8px;padding:10px 14px;margin:10px 0">GlobalCompass provides general guidance to help you plan &mdash; always verify official requirements and deadlines directly with your target university before making any decisions. GlobalCompass is not responsible for outcomes based on information that changes after publication, or for decisions made using this tool alone.</div>'

fixes = [
    ("american-pathway-navigator.html",
     '<div class="card"><div class="ai-label">GlobalCompass insight</div><div class="ai-bubble"><p id="ap-aiInsight"></p></div></div>\n      <div class="action-row">',
     '<div class="card"><div class="ai-label">GlobalCompass insight</div><div class="ai-bubble"><p id="ap-aiInsight"></p></div></div>\n      ' + DISCLAIMER_HTML + '\n      <div class="action-row">'),
    ("american-pathway-navigator.html",
     '<div class="card"><div class="ai-label">GlobalCompass SAT insight</div><div class="ai-bubble"><p id="sat-aiInsight"></p></div></div>\n      <div class="action-row">',
     '<div class="card"><div class="ai-label">GlobalCompass SAT insight</div><div class="ai-bubble"><p id="sat-aiInsight"></p></div></div>\n      ' + DISCLAIMER_HTML + '\n      <div class="action-row">'),
    ("australian-vce-navigator.html",
     '<div class="card"><div class="ai-label">GlobalCompass insight</div><div class="ai-bubble"><p id="aiInsight"></p></div></div>\n    <div class="action-row">',
     '<div class="card"><div class="ai-label">GlobalCompass insight</div><div class="ai-bubble"><p id="aiInsight"></p></div></div>\n    ' + DISCLAIMER_HTML + '\n    <div class="action-row">'),
    ("brazilian-enem-navigator.html",
     '<div class="card"><div class="ai-label">GlobalCompass insight</div><div class="ai-bubble"><p id="aiInsight"></p></div></div>\n    <div class="action-row">',
     '<div class="card"><div class="ai-label">GlobalCompass insight</div><div class="ai-bubble"><p id="aiInsight"></p></div></div>\n    ' + DISCLAIMER_HTML + '\n    <div class="action-row">'),
    ("cbse-stream-navigator.html",
     '<div class="card"><div class="ai-label">GlobalCompass insight</div><div class="ai-bubble"><p id="aiInsight"></p></div></div>\n    <div class="hindi-note">',
     '<div class="card"><div class="ai-label">GlobalCompass insight</div><div class="ai-bubble"><p id="aiInsight"></p></div></div>\n    ' + DISCLAIMER_HTML + '\n    <div class="hindi-note">'),
    ("ib-pathway-navigator.html",
     '<div class="card"><div class="ai-label">GlobalCompass IB insight</div><div class="ai-bubble"><p id="aiInsight"></p></div></div>\n    <div class="action-row">',
     '<div class="card"><div class="ai-label">GlobalCompass IB insight</div><div class="ai-bubble"><p id="aiInsight"></p></div></div>\n    ' + DISCLAIMER_HTML + '\n    <div class="action-row">'),
    ("singapore-pathway-navigator.html",
     '<div class="card"><div class="ai-label">GlobalCompass insight</div><div class="ai-bubble"><p id="aiInsight"></p></div></div>\n    <div class="action-row">',
     '<div class="card"><div class="ai-label">GlobalCompass insight</div><div class="ai-bubble"><p id="aiInsight"></p></div></div>\n    ' + DISCLAIMER_HTML + '\n    <div class="action-row">'),
]

for path, old, new in fixes:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    count = content.count(old)
    if count != 1:
        print(f"SKIPPED {path}: expected 1 match, found {count} — check manually.")
        continue
    content = content.replace(old, new, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Added disclaimer to {path}")

print("Done.")

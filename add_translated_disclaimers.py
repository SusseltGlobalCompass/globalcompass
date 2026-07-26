import re

# --- French Bac ---
path = "french-bac-navigator.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

old_div = '<div style="font-size:11px;color:#7A8BAE;background:#F8F9FF;border-radius:8px;padding:10px 14px;margin:10px 0">GlobalCompass provides general guidance to help you plan &mdash; always verify official requirements and deadlines directly with your target university before making any decisions. GlobalCompass is not responsible for outcomes based on information that changes after publication, or for decisions made using this tool alone.</div>'
new_div = '<div id="disclaimerText" style="font-size:11px;color:#7A8BAE;background:#F8F9FF;border-radius:8px;padding:10px 14px;margin:10px 0">GlobalCompass provides general guidance to help you plan &mdash; always verify official requirements and deadlines directly with your target university before making any decisions. GlobalCompass is not responsible for outcomes based on information that changes after publication, or for decisions made using this tool alone.</div>'
if content.count(old_div) != 1:
    raise SystemExit("ABORTED: French disclaimer div not found uniquely.")
content = content.replace(old_div, new_div, 1)

# Add disclaimerText key to the 'en' block (right after dreamPlaceholder line, before its closing brace) and 'fr' block
en_anchor = "dreamPlaceholder:'ex. What is your career dream?'"
# We don't know the exact EN placeholder text, so anchor on insightLabel instead, which we know exists in both blocks
en_key_anchor = "insightLabel:'GlobalCompass insight',"
fr_key_anchor = "insightLabel:'Conseil GlobalCompass',"

en_disclaimer = "disclaimerText:'GlobalCompass provides general guidance to help you plan — always verify official requirements and deadlines directly with your target university before making any decisions. GlobalCompass is not responsible for outcomes based on information that changes after publication, or for decisions made using this tool alone.',"
fr_disclaimer = "disclaimerText:'GlobalCompass propose des conseils généraux pour vous aider à planifier — vérifiez toujours les exigences et délais officiels directement auprès de votre université cible avant de prendre une décision. GlobalCompass décline toute responsabilité quant aux conséquences liées à des informations ayant changé après publication, ou à des décisions prises en se basant uniquement sur cet outil.',"

if content.count(en_key_anchor) != 1:
    raise SystemExit(f"ABORTED: EN insightLabel anchor found {content.count(en_key_anchor)} times, expected 1.")
content = content.replace(en_key_anchor, en_key_anchor + "\n    " + en_disclaimer, 1)

if content.count(fr_key_anchor) != 1:
    raise SystemExit(f"ABORTED: FR insightLabel anchor found {content.count(fr_key_anchor)} times, expected 1.")
content = content.replace(fr_key_anchor, fr_key_anchor + "\n    " + fr_disclaimer, 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("French Bac: disclaimer now translates with the page language toggle.")

# --- German Abitur ---
path = "german-abitur-navigator.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

old_div = '<div style="font-size:11px;color:#7A8BAE;background:#F8F9FF;border-radius:8px;padding:10px 14px;margin:10px 0">GlobalCompass provides general guidance to help you plan &mdash; always verify official requirements and deadlines directly with your target university before making any decisions. GlobalCompass is not responsible for outcomes based on information that changes after publication, or for decisions made using this tool alone.</div>'
new_div = '<div id="disclaimerText" style="font-size:11px;color:#7A8BAE;background:#F8F9FF;border-radius:8px;padding:10px 14px;margin:10px 0">GlobalCompass provides general guidance to help you plan &mdash; always verify official requirements and deadlines directly with your target university before making any decisions. GlobalCompass is not responsible for outcomes based on information that changes after publication, or for decisions made using this tool alone.</div>'
if content.count(old_div) != 1:
    raise SystemExit("ABORTED: German disclaimer div not found uniquely.")
content = content.replace(old_div, new_div, 1)

en_key_anchor = "insightLabel:'GlobalCompass insight',"
de_key_anchor = "insightLabel:'GlobalCompass-Tipp',"

en_disclaimer = "disclaimerText:'GlobalCompass provides general guidance to help you plan — always verify official requirements and deadlines directly with your target university before making any decisions. GlobalCompass is not responsible for outcomes based on information that changes after publication, or for decisions made using this tool alone.',"
de_disclaimer = "disclaimerText:'GlobalCompass bietet allgemeine Orientierungshilfe zur Planung — bitte überprüfen Sie offizielle Anforderungen und Fristen stets direkt bei Ihrer Zieluniversität, bevor Sie Entscheidungen treffen. GlobalCompass übernimmt keine Verantwortung für Ergebnisse, die auf nach der Veröffentlichung geänderten Informationen beruhen, oder für Entscheidungen, die ausschließlich auf Grundlage dieses Tools getroffen wurden.',"

if content.count(en_key_anchor) != 1:
    raise SystemExit(f"ABORTED: EN insightLabel anchor found {content.count(en_key_anchor)} times, expected 1.")
content = content.replace(en_key_anchor, en_key_anchor + "\n    " + en_disclaimer, 1)

if content.count(de_key_anchor) != 1:
    raise SystemExit(f"ABORTED: DE insightLabel anchor found {content.count(de_key_anchor)} times, expected 1.")
content = content.replace(de_key_anchor, de_key_anchor + "\n    " + de_disclaimer, 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("German Abitur: disclaimer now translates with the page language toggle.")

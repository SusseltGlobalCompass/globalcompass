path = "brazilian-enem-navigator.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Give the disclaimer div an id
old_div = '<div style="font-size:11px;color:#7A8BAE;background:#F8F9FF;border-radius:8px;padding:10px 14px;margin:10px 0">GlobalCompass provides general guidance to help you plan &mdash; always verify official requirements and deadlines directly with your target university before making any decisions. GlobalCompass is not responsible for outcomes based on information that changes after publication, or for decisions made using this tool alone.</div>'
new_div = '<div id="disclaimerText" style="font-size:11px;color:#7A8BAE;background:#F8F9FF;border-radius:8px;padding:10px 14px;margin:10px 0">GlobalCompass provides general guidance to help you plan &mdash; always verify official requirements and deadlines directly with your target university before making any decisions. GlobalCompass is not responsible for outcomes based on information that changes after publication, or for decisions made using this tool alone.</div>'
if content.count(old_div) != 1:
    raise SystemExit("ABORTED: disclaimer div not found uniquely.")
content = content.replace(old_div, new_div, 1)

# 2. Add disclaimerText key to the pt block
pt_anchor = "dreamPlaceholder: 'ex. Quero estudar medicina e me tornar médico...'"
pt_disclaimer = "dreamPlaceholder: 'ex. Quero estudar medicina e me tornar médico...',\n    disclaimerText: 'O GlobalCompass oferece orientação geral para ajudar no seu planejamento — sempre verifique os requisitos e prazos oficiais diretamente com a universidade de destino antes de tomar qualquer decisão. O GlobalCompass não se responsabiliza por resultados baseados em informações que mudem após a publicação, nem por decisões tomadas com base apenas nesta ferramenta.'"
if content.count(pt_anchor) != 1:
    raise SystemExit(f"ABORTED: PT anchor found {content.count(pt_anchor)} times, expected 1.")
content = content.replace(pt_anchor, pt_disclaimer, 1)

# 3. Add disclaimerText key to the en block
en_anchor = "dreamPlaceholder: 'e.g. I want to study medicine and become a doctor...'"
en_disclaimer = "dreamPlaceholder: 'e.g. I want to study medicine and become a doctor...',\n    disclaimerText: 'GlobalCompass provides general guidance to help you plan — always verify official requirements and deadlines directly with your target university before making any decisions. GlobalCompass is not responsible for outcomes based on information that changes after publication, or for decisions made using this tool alone.'"
if content.count(en_anchor) != 1:
    raise SystemExit(f"ABORTED: EN anchor found {content.count(en_anchor)} times, expected 1.")
content = content.replace(en_anchor, en_disclaimer, 1)

# 4. Add the manual DOM assignment inside setLang()
setlang_anchor = "const areasTitle = document.querySelector('#s5 .card-title'); if(areasTitle) areasTitle.textContent = t.areasTitle;"
setlang_new = setlang_anchor + "\n  const disclaimerEl = document.getElementById('disclaimerText'); if(disclaimerEl) disclaimerEl.textContent = t.disclaimerText;"
if content.count(setlang_anchor) != 1:
    raise SystemExit(f"ABORTED: setLang anchor found {content.count(setlang_anchor)} times, expected 1.")
content = content.replace(setlang_anchor, setlang_new, 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Brazilian ENEM: disclaimer now translates with the PT/EN language toggle.")

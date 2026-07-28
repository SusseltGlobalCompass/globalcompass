path = "brazilian-enem-navigator.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

def apply(name, old, new, c):
    cnt = c.count(old)
    if cnt != 1:
        raise SystemExit(f"ABORTED at '{name}': expected 1 match, found {cnt}.")
    return c.replace(old, new, 1)

# 1. Exact color correction
before = content.count("#009739")
content = content.replace("#009739", "#009C3B")

# 2. Sticky step indicator
content = apply("sticky",
    '.step-indicator{display:flex;align-items:center;margin-bottom:24px}',
    '.step-indicator{display:flex;align-items:center;margin-bottom:24px;position:sticky;top:0;background:#F8F9FF;padding:12px 0;z-index:5}',
    content)

# 3. Fix the three static buttons — proper Portuguese defaults, translatable
content = apply("btn1 static text",
    'Next — Seu ano escolar →',
    'Próximo — Seu ano escolar →',
    content)
content = apply("btn2 static text",
    'Next — Sua universidade alvo →',
    'Próximo — Sua universidade alvo →',
    content)
content = apply("btn3 static text",
    'Gerar meu caminho ENEM ↗',
    'Desenhar meu mapa do ENEM ↗',
    content)

# 4. Add translation keys to pt block
content = apply("pt translation keys",
    "dreamPlaceholder: 'ex. Quero estudar medicina e me tornar médico...',\n    disclaimerText:",
    "dreamPlaceholder: 'ex. Quero estudar medicina e me tornar médico...',\n    btn1Text: 'Próximo — Seu ano escolar →',\n    btn2Text: 'Próximo — Sua universidade alvo →',\n    btn3Text: 'Desenhar meu mapa do ENEM →',\n    disclaimerText:",
    content)

# 5. Add translation keys to en block
content = apply("en translation keys",
    "dreamPlaceholder: 'e.g. I want to study medicine and become a doctor...',\n    disclaimerText:",
    "dreamPlaceholder: 'e.g. I want to study medicine and become a doctor...',\n    btn1Text: 'Next — Your school year →',\n    btn2Text: 'Next — Your target university →',\n    btn3Text: 'Draw my ENEM map →',\n    disclaimerText:",
    content)

# 6. Wire the manual DOM assignments into setLang()
content = apply("setLang assignments",
    "const disclaimerEl = document.getElementById('disclaimerText'); if(disclaimerEl) disclaimerEl.textContent = t.disclaimerText;",
    "const disclaimerEl = document.getElementById('disclaimerText'); if(disclaimerEl) disclaimerEl.textContent = t.disclaimerText;\n  const b1 = document.getElementById('btn1'); if(b1) b1.textContent = t.btn1Text;\n  const b2 = document.getElementById('btn2'); if(b2) b2.textContent = t.btn2Text;\n  const b3 = document.getElementById('btn3'); if(b3) b3.textContent = t.btn3Text;",
    content)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Color corrected ({before} instances). Sticky added. All 3 buttons now fully bilingual. Final CTA updated.")

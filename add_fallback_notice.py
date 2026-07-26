path = "brazilian-enem-navigator.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

def apply(name, old, new, c):
    cnt = c.count(old)
    if cnt != 1:
        raise SystemExit(f"ABORTED at '{name}': expected 1 match, found {cnt}.")
    return c.replace(old, new, 1)

# 1. Add the hidden notice banner to the results screen HTML
old_html = '''  <div id="s5" class="screen">
    <div class="result-hero">
      <div class="result-tag">🇧🇷 Seu caminho ENEM</div>'''
new_html = '''  <div id="s5" class="screen">
    <div id="fallbackNotice" style="display:none;background:#FFF3D6;border:1px solid #E8C468;border-radius:8px;padding:12px 16px;margin-bottom:14px;font-size:12px;color:#7A5A00"></div>
    <div class="result-hero">
      <div class="result-tag">🇧🇷 Seu caminho ENEM</div>'''
content = apply("notice HTML", old_html, new_html, content)

# 2. showResults() now accepts an isFallback flag and shows/hides the notice accordingly
old_fn = '''function showResults(r){
  document.getElementById('resultCareer').textContent=r.career;'''
new_fn = '''function showResults(r, isFallback){
  const notice = document.getElementById('fallbackNotice');
  if(notice){
    if(isFallback){
      notice.style.display = 'block';
      notice.textContent = currentLang === 'en'
        ? "We couldn't generate your personalized pathway right now, so here's general guidance instead. Please try again in a few minutes for results tailored specifically to you."
        : 'Não conseguimos gerar seu caminho personalizado no momento, então aqui está uma orientação geral. Tente novamente em alguns minutos para resultados feitos especialmente para você.';
    } else {
      notice.style.display = 'none';
    }
  }
  document.getElementById('resultCareer').textContent=r.career;'''
content = apply("showResults signature", old_fn, new_fn, content)

# 3. showFallback() now passes isFallback=true
old_call = 'function showFallback(){showResults({career:'
new_call = 'function showFallback(){showResults({career:'
# find the exact closing of the object literal to append the flag — safer to just replace the final "});}" of that specific function
old_tail = 'Treat the essay with the same seriousness as Biology and Chemistry."});}'
new_tail = 'Treat the essay with the same seriousness as Biology and Chemistry."}, true);}'
content = apply("showFallback flag", old_tail, new_tail, content)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Honest fallback notice added — visible whenever generic content is shown instead of a real AI-generated pathway.")

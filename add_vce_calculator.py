path = "academic-passport.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

edits_applied = []

def apply_edit(name, old, new, content):
    c = content.count(old)
    if c != 1:
        raise SystemExit(f"ABORTED at '{name}': expected 1 match, found {c}. No changes made yet — file untouched from this point.")
    edits_applied.append(name)
    return content.replace(old, new, 1)

# Edit 1: add VCE to curriculumMeta
old1 = '''  'ENEM': { label: 'EN', name: 'Brazilian ENEM', color: '#009739', textColor: '#FEDD00' }
};'''
new1 = '''  'ENEM': { label: 'EN', name: 'Brazilian ENEM', color: '#009739', textColor: '#FEDD00' },
  'VCE': { label: 'VC', name: 'Australian VCE', color: '#8B6000', textColor: '#fff' }
};'''
content = apply_edit("curriculumMeta", old1, new1, content)

# Edit 2: add the VCE selection card next to the others
old2 = '''        <div class="curr-select-card" data-curr="ENEM" onclick="toggleCurriculum(this,'ENEM')">'''
new2 = '''        <div class="curr-select-card" data-curr="VCE" onclick="toggleCurriculum(this,'VCE')"></div>
        <div class="curr-select-card" data-curr="ENEM" onclick="toggleCurriculum(this,'ENEM')">'''
content = apply_edit("selection card placeholder", old2, new2, content)

# Edit 3: add the status/load branch in the dashboard loop
old3 = '''    } else if(curr === 'General'){'''
new3 = '''    } else if(curr === 'VCE'){
      const { data: subs } = await sb.from('australian_subjects').select('*').eq('user_id', currentUser.id);
      if(subs && subs.length > 0){
        status = `${subs.length} subjects entered`;
      }
      await loadVceData();
    } else if(curr === 'General'){'''
content = apply_edit("dashboard status branch", old3, new3, content)

# Edit 4: extend the panel-id ternary chain
old4 = '''curr === 'ENEM' ? 'enem' : 'general'}-panel', this)">'''
new4 = '''curr === 'ENEM' ? 'enem' : curr === 'VCE' ? 'vce' : 'general'}-panel', this)">'''
content = apply_edit("panel id ternary", old4, new4, content)

# Edit 5: insert the full VCE panel HTML, right before the american-panel block
old5 = '''    <div id="american-panel" class="curr-detail-panel" style="margin-top:14px">'''
new5 = '''    <div id="vce-panel" class="curr-detail-panel" style="margin-top:14px">
    <div class="card">
      <div class="card-title">VCE subjects</div>
      <div class="card-sub">Enter your subjects and raw study scores (0-50). Mark your English-group subject (English, EAL, Literature, or English Language) — VTAC always counts this one first.</div>
      <div id="vceSubjectsContainer"></div>
      <button class="add-row-btn" onclick="addVceSubjectRow()">+ Add subject</button>
      <button class="save-row-btn" onclick="saveVceSubjects()">Save subjects</button>
      <div id="vceSubjectStatus"></div>
      <div class="calc-result-box">
        <div><div class="calc-result-label">Raw aggregate (unscaled)</div></div>
        <div class="calc-result-num" id="vceAggregateDisplay">0.0</div>
      </div>
      <div class="gpa-disclaimer">This is your raw aggregate using VTAC's real formula (best English-group score + next 3 best + 10% of your 5th and 6th) applied to the scores you entered. Your official ATAR also applies VTAC's annual scaling, which adjusts each subject based on that year's statewide cohort — GlobalCompass does not have access to VTAC's confidential yearly scaling tables, so this number is not your ATAR. Always confirm your real ATAR with VTAC.</div>
    </div>
    </div>

    <div id="american-panel" class="curr-detail-panel" style="margin-top:14px">'''
content = apply_edit("VCE panel HTML", old5, new5, content)

# Edit 6: add the row-count variable
old6 = '''let americanSubjectRowCount = 0, apExamRowCount = 0;'''
new6 = '''let americanSubjectRowCount = 0, apExamRowCount = 0, vceSubjectRowCount = 0;'''
content = apply_edit("row count var", old6, new6, content)

# Edit 7: add loadVceData, addVceSubjectRow, recalcVceFromInputs, saveVceSubjects
old7 = '''async function loadAmericanData(){'''
new7 = '''async function loadVceData(){
  const { data: subjects } = await sb.from('australian_subjects').select('*').eq('user_id', currentUser.id);
  document.getElementById('vceSubjectsContainer').innerHTML = '';
  vceSubjectRowCount = 0;
  if(subjects && subjects.length > 0){
    subjects.forEach(s => addVceSubjectRow(s));
  } else {
    for(let i=0;i<6;i++) addVceSubjectRow();
  }
  recalcVceFromInputs();
}

function addVceSubjectRow(existing){
  vceSubjectRowCount++;
  const id = 'vce_row_' + vceSubjectRowCount;
  const row = document.createElement('div');
  row.className = 'subj-row-multi';
  row.id = id;
  row.innerHTML = `
    <input type="text" data-field="subject" placeholder="e.g. Specialist Mathematics" value="${existing && existing.subject ? existing.subject : ''}">
    <label style="display:flex;align-items:center;gap:6px;font-size:12px;color:#7A8BAE"><input type="checkbox" data-field="is_english" onchange="recalcVceFromInputs()" ${existing && existing.is_english ? 'checked' : ''}> English group</label>
    <input type="number" min="0" max="50" data-field="study_score" placeholder="0-50" value="${existing && existing.study_score !== null && existing.study_score !== undefined ? existing.study_score : ''}" onchange="recalcVceFromInputs()">
    <div></div>
    <span class="remove-row-btn" onclick="document.getElementById('${id}').remove();recalcVceFromInputs()">✕</span>
  `;
  if(existing) row.dataset.rowId = existing.id;
  document.getElementById('vceSubjectsContainer').appendChild(row);
}

function recalcVceFromInputs(){
  const rows = document.querySelectorAll('#vceSubjectsContainer .subj-row-multi');
  const entries = [];
  rows.forEach(row => {
    const isEnglish = row.querySelector('[data-field="is_english"]').checked;
    const scoreVal = row.querySelector('[data-field="study_score"]').value;
    if(scoreVal === '') return;
    entries.push({ isEnglish, score: parseFloat(scoreVal) });
  });
  const display = document.getElementById('vceAggregateDisplay');
  if(entries.length === 0){ display.textContent = '0.0'; return; }
  const englishEntries = entries.filter(e => e.isEnglish).sort((a,b) => b.score - a.score);
  const englishScore = englishEntries.length > 0 ? englishEntries[0].score : 0;
  const remaining = entries.filter(e => !(englishEntries.length > 0 && e === englishEntries[0])).sort((a,b) => b.score - a.score);
  const next3 = remaining.slice(0,3);
  const next2 = remaining.slice(3,5);
  const aggregate = englishScore + next3.reduce((s,e) => s + e.score, 0) + next2.reduce((s,e) => s + e.score * 0.1, 0);
  display.textContent = aggregate.toFixed(1);
}

async function saveVceSubjects(){
  const rows = document.querySelectorAll('#vceSubjectsContainer .subj-row-multi');
  const statusEl = document.getElementById('vceSubjectStatus');
  let savedCount = 0;
  for(const row of rows){
    const subject = row.querySelector('[data-field="subject"]').value.trim();
    if(!subject) continue;
    const is_english = row.querySelector('[data-field="is_english"]').checked;
    const scoreVal = row.querySelector('[data-field="study_score"]').value;
    const study_score = scoreVal === '' ? null : parseInt(scoreVal);
    const payload = { user_id: currentUser.id, subject, is_english, study_score, updated_at: new Date().toISOString() };
    if(row.dataset.rowId){
      await sb.from('australian_subjects').update(payload).eq('id', row.dataset.rowId);
    } else {
      const { data } = await sb.from('australian_subjects').insert(payload).select().single();
      if(data) row.dataset.rowId = data.id;
    }
    savedCount++;
  }
  statusEl.innerHTML = '<div class="status-msg status-success">Saved '+savedCount+' subjects!</div>';
  recalcVceFromInputs();
  await loadDashboard();
}

async function loadAmericanData(){'''
content = apply_edit("VCE functions block", old7, new7, content)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("All edits applied successfully:")
for e in edits_applied:
    print(" -", e)

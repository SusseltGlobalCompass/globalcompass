"""
Add a "language of instruction" question to Step 1 (separate from
curriculum, since IB/other curricula are offered in multiple languages)
and add matching logic for the new waived_if_instruction_language_in
condition type (used by UBC's real policy).

Run from inside ~/Desktop/GlobalCompass
"""

FILE = "university-requirements.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

original = content

old_html = '''    <div class="field">
      <label class="field-label">Is English your native/first language?</label>'''
new_html = '''    <div class="field">
      <label class="field-label">What language was most of your schooling taught in?</label>
      <select class="f-sel" id="langSel">
        <option value="">Select a language</option>
        <option value="English">English</option>
        <option value="French">French</option>
        <option value="Spanish">Spanish</option>
        <option value="Other">Other</option>
      </select>
      <div class="help-text">Some curricula (like IB) are offered in more than one language \u2014 this helps us check requirements accurately regardless of which one your school used.</div>
    </div>

    <div class="field">
      <label class="field-label">Is English your native/first language?</label>'''

if old_html not in content:
    print("ERROR: Could not find Step 1 anchor. No changes made.")
else:
    content = content.replace(old_html, new_html)

    old_student = 'let student = { curriculum: "", native: null, resident: null };'
    new_student = 'let student = { curriculum: "", language: "", native: null, resident: null };'
    content = content.replace(old_student, new_student)

    old_listener = '''document.getElementById('curSel').addEventListener('change', function(){
  student.curriculum = this.value;
  checkStep1Complete();
});'''
    new_listener = '''document.getElementById('curSel').addEventListener('change', function(){
  student.curriculum = this.value;
  checkStep1Complete();
});

document.getElementById('langSel').addEventListener('change', function(){
  student.language = this.value;
  checkStep1Complete();
});'''
    content = content.replace(old_listener, new_listener)

    old_check = '''function checkStep1Complete(){
  const complete = student.curriculum && student.native !== null && student.resident !== null;
  document.getElementById('step1Next').disabled = !complete;
}'''
    new_check = '''function checkStep1Complete(){
  const complete = student.curriculum && student.language && student.native !== null && student.resident !== null;
  document.getElementById('step1Next').disabled = !complete;
}'''
    content = content.replace(old_check, new_check)

    old_logic = '''  } else if(r.condition_type === 'waived_if_native_or_3yr_resident'){'''
    new_logic = '''  } else if(r.condition_type === 'waived_if_instruction_language_in'){
    const langList = (r.condition_value || '').split(',').map(s => s.trim());
    if(langList.includes(student.language)){
      status = 'verify';
      note = 'Likely waived \u2014 your schooling was taught in ' + student.language + '. Confirm exact eligibility (years of schooling, course grades) directly with ' + selectedUniversity.name + '.';
    } else {
      status = 'action';
      note = r.notes || 'Required based on your schooling language.';
    }
  } else if(r.condition_type === 'waived_if_native_or_3yr_resident'){'''
    content = content.replace(old_logic, new_logic)

    if content == original:
        print("WARNING: No changes were made at all.")
    else:
        with open(FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print("Done. Language-of-instruction question added, wired up, and UBC matching logic implemented.")

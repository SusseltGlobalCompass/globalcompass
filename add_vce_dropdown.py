path = "academic-passport.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Edit 1: insert vceSubjectGroups + buildVceSubjectOptions, right before loadVceData
old1 = '''async function loadVceData(){'''
new1 = '''const vceSubjectGroups = {
  'English': ['English', 'English as an Additional Language (EAL)', 'English Language', 'Literature'],
  'Mathematics': ['Foundation Mathematics', 'General Mathematics', 'Mathematical Methods', 'Specialist Mathematics'],
  'Sciences': ['Biology', 'Chemistry', 'Physics', 'Psychology', 'Environmental Science'],
  'Humanities': ['Legal Studies', 'History', 'Geography', 'Australian Politics', 'Global Politics', 'Philosophy', 'Economics'],
  'Business': ['Business Management', 'Accounting'],
  'Arts': ['Art Creative Practice', 'Art Making and Exhibiting', 'Music', 'Drama', 'Theatre Studies', 'Media', 'Visual Communication Design', 'Dance'],
  'Languages': ['Chinese Second Language', 'Chinese First Language', 'French', 'Italian', 'Japanese', 'German', 'Spanish', 'Auslan'],
  'Health and Physical Education': ['Health and Human Development', 'Physical Education'],
  'Technology': ['Product Design and Technologies', 'Food Studies', 'Applied Computing']
};

function buildVceSubjectOptions(selected){
  let html = '<option value="">Select subject…</option>';
  for(const group in vceSubjectGroups){
    html += `<optgroup label="${group}">`;
    vceSubjectGroups[group].forEach(subj => {
      html += `<option value="${subj}" ${subj===selected?'selected':''}>${subj}</option>`;
    });
    html += '</optgroup>';
  }
  return html;
}

async function loadVceData(){'''

count1 = content.count(old1)
if count1 != 1:
    raise SystemExit(f"ABORTED at edit 1: expected 1 match, found {count1}. No changes made.")
content = content.replace(old1, new1, 1)

# Edit 2: swap the free-text subject input for the new dropdown
old2 = '''    <input type="text" data-field="subject" placeholder="e.g. Specialist Mathematics" value="${existing && existing.subject ? existing.subject : ''}">'''
new2 = '''    <select data-field="subject">${buildVceSubjectOptions(existing ? existing.subject : '')}</select>'''

count2 = content.count(old2)
if count2 != 1:
    raise SystemExit(f"ABORTED at edit 2: expected 1 match, found {count2}. No changes made.")
content = content.replace(old2, new2, 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done. VCE subject dropdown added with real VCAA subject groups.")

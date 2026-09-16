"""
Add a type-to-filter search box above the university list on Step 2,
so the design scales gracefully as more universities are added over
time (matching the same search-filter interaction already used on
schools.html).

Run from inside ~/Desktop/GlobalCompass
"""

FILE = "university-requirements.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

original = content

old_html = '''    <div id="uniList"><div class="loading-state">Loading universities...</div></div>
    <button class="btn-secondary" onclick="goStep(1)">\u2190 Change my background</button>'''
new_html = '''    <input type="text" class="f-sel" id="uniSearch" placeholder="Search by name or country..." style="margin-bottom:14px" oninput="filterUniversities()">
    <div id="uniList"><div class="loading-state">Loading universities...</div></div>
    <button class="btn-secondary" onclick="goStep(1)">\u2190 Change my background</button>'''

if old_html not in content:
    print("ERROR: Could not find Step 2 uniList block. No changes made.")
else:
    content = content.replace(old_html, new_html)

    old_load = '''async function loadUniversities(){
  const { data, error } = await sb.from('target_universities').select('*').order('name');
  const listEl = document.getElementById('uniList');
  if(error || !data || data.length === 0){
    listEl.innerHTML = '<div class="loading-state">No universities available right now \u2014 please try again shortly.</div>';
    return;
  }
  allUniversities = data;
  listEl.innerHTML = data.map(u =>
    '<div class="uni-card" onclick="selectUniversity(\\'' + u.id + '\\')"><div class="uni-name">' + u.name + '</div><div class="uni-country">' + u.country + '</div></div>'
  ).join('');
}'''

    new_load = '''async function loadUniversities(){
  const { data, error } = await sb.from('target_universities').select('*').order('name');
  const listEl = document.getElementById('uniList');
  if(error || !data || data.length === 0){
    listEl.innerHTML = '<div class="loading-state">No universities available right now \u2014 please try again shortly.</div>';
    return;
  }
  allUniversities = data;
  renderUniversityList(allUniversities);
}

function renderUniversityList(list){
  const listEl = document.getElementById('uniList');
  if(list.length === 0){
    listEl.innerHTML = '<div class="loading-state">No universities match your search.</div>';
    return;
  }
  listEl.innerHTML = list.map(u =>
    '<div class="uni-card" onclick="selectUniversity(\\'' + u.id + '\\')"><div class="uni-name">' + u.name + '</div><div class="uni-country">' + u.country + '</div></div>'
  ).join('');
}

function filterUniversities(){
  const q = document.getElementById('uniSearch').value.trim().toLowerCase();
  if(!q){
    renderUniversityList(allUniversities);
    return;
  }
  const filtered = allUniversities.filter(u =>
    u.name.toLowerCase().includes(q) || u.country.toLowerCase().includes(q)
  );
  renderUniversityList(filtered);
}'''

    if old_load not in content:
        print("ERROR: Could not find loadUniversities function exactly. Search box added but filter logic NOT wired.")
    else:
        content = content.replace(old_load, new_load)
        with open(FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print("Done. University search-filter box added and fully wired.")

if content == original:
    print("WARNING: No changes were made at all.")

path = "forum.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# --- Edit 1: add global state for the active topic filter and cached topics ---
old1 = '''    let currentCategory = null;
    let currentForumUser = null;
    let currentForumProfile = null;'''

new1 = '''    let currentCategory = null;
    let currentForumUser = null;
    let currentForumProfile = null;
    let activeTopicId = null;
    let allTopics = [];'''

c1 = content.count(old1)
if c1 != 1:
    raise SystemExit(f"ABORTED edit 1: expected 1 match, found {c1}. No changes made.")
content = content.replace(old1, new1, 1)

# --- Edit 2: reset the topic filter whenever a category is opened ---
old2 = '''    function openCategory(cat){
      currentCategory = cat;'''

new2 = '''    function openCategory(cat){
      currentCategory = cat;
      activeTopicId = null;'''

c2 = content.count(old2)
if c2 != 1:
    raise SystemExit(f"ABORTED edit 2: expected 1 match, found {c2}. No changes made.")
content = content.replace(old2, new2, 1)

# --- Edit 3: give postsList a sidebar neighbor in the HTML ---
old3 = '''    </div>

    <div id="postsList"></div>
  </div>'''

new3 = '''    </div>

    <div style="display:flex;gap:20px;align-items:flex-start;flex-wrap:wrap">
      <div id="topicSidebar" style="width:180px;flex-shrink:0;display:flex;flex-direction:column;gap:4px"></div>
      <div id="postsList" style="flex:1;min-width:240px"></div>
    </div>
  </div>'''

c3 = content.count(old3)
if c3 != 1:
    raise SystemExit(f"ABORTED edit 3: expected 1 match, found {c3}. No changes made.")
content = content.replace(old3, new3, 1)

# --- Edit 4: loadTopicsIntoDropdown now also caches allTopics for the sidebar ---
old4 = '''    async function loadTopicsIntoDropdown(){
      const sel = document.getElementById('postTopic');
      if (sel.dataset.loaded) return;
      const { data } = await sb.from('forum_topics').select('*').order('sort_order');
      (data || []).forEach(t => {
        const opt = document.createElement('option');
        opt.value = t.id;
        opt.textContent = t.name;
        sel.appendChild(opt);
      });
      sel.dataset.loaded = 'true';
    }'''

new4 = '''    async function loadTopicsIntoDropdown(){
      if (allTopics.length === 0){
        const { data } = await sb.from('forum_topics').select('*').order('sort_order');
        allTopics = data || [];
      }
      const sel = document.getElementById('postTopic');
      if (!sel.dataset.loaded){
        allTopics.forEach(t => {
          const opt = document.createElement('option');
          opt.value = t.id;
          opt.textContent = t.name;
          sel.appendChild(opt);
        });
        sel.dataset.loaded = 'true';
      }
    }

    function selectTopicFilter(topicId){
      activeTopicId = topicId;
      loadPosts();
    }

    function renderTopicSidebar(posts){
      const box = document.getElementById('topicSidebar');
      const counts = {};
      posts.forEach(p => { if (p.topic_id) counts[p.topic_id] = (counts[p.topic_id] || 0) + 1; });
      const allActive = activeTopicId === null;
      let html = '<div style="font-family:sans-serif;font-size:11px;letter-spacing:0.06em;color:#9AB0D0;text-transform:uppercase;margin-bottom:4px">Topics</div>';
      html += '<div onclick="selectTopicFilter(null)" style="cursor:pointer;font-family:sans-serif;font-size:12.5px;font-weight:700;color:'+(allActive?'#1B3A7A':'#333')+';background:'+(allActive?'#EEF3FF':'transparent')+';border-radius:8px;padding:8px 10px;display:flex;justify-content:space-between">All topics<span style="color:#9AB0D0;font-weight:400">'+posts.length+'</span></div>';
      allTopics.forEach(t => {
        const active = activeTopicId === t.id;
        html += '<div onclick="selectTopicFilter(\\''+t.id+'\\')" style="cursor:pointer;font-family:sans-serif;font-size:12.5px;font-weight:'+(active?'700':'400')+';color:'+(active?'#1B3A7A':'#333')+';background:'+(active?'#EEF3FF':'transparent')+';border-radius:8px;padding:8px 10px;display:flex;justify-content:space-between">'+t.name+'<span style="color:#9AB0D0">'+(counts[t.id]||0)+'</span></div>';
      });
      box.innerHTML = html;
    }'''

c4 = content.count(old4)
if c4 != 1:
    raise SystemExit(f"ABORTED edit 4: expected 1 match, found {c4}. No changes made.")
content = content.replace(old4, new4, 1)

# --- Edit 5: loadPosts renders the sidebar and applies the active filter ---
old5 = '''    async function loadPosts(){
      loadTopicsIntoDropdown();
      const { data, error } = await sb.from('forum_posts')
        .select('*')
        .eq('category', currentCategory)
        .order('created_at', { ascending: false });
      const list = document.getElementById('postsList');
      if (error || !data || data.length === 0){
        list.innerHTML = '<div style="text-align:center;padding:30px;color:#7A8BAE;font-size:13px">No posts yet — be the first to share.</div>';
        return;
      }
      const postUserIds = [...new Set(data.map(p => p.user_id))];'''

new5 = '''    async function loadPosts(){
      await loadTopicsIntoDropdown();
      const { data, error } = await sb.from('forum_posts')
        .select('*')
        .eq('category', currentCategory)
        .order('created_at', { ascending: false });
      renderTopicSidebar(data || []);
      const filteredData = activeTopicId ? (data || []).filter(p => p.topic_id === activeTopicId) : (data || []);
      const list = document.getElementById('postsList');
      if (error || !filteredData || filteredData.length === 0){
        list.innerHTML = '<div style="text-align:center;padding:30px;color:#7A8BAE;font-size:13px">No posts yet — be the first to share.</div>';
        return;
      }
      const data2 = filteredData;
      const postUserIds = [...new Set(data2.map(p => p.user_id))];'''

c5 = content.count(old5)
if c5 != 1:
    raise SystemExit(f"ABORTED edit 5: expected 1 match, found {c5}. No changes made.")
content = content.replace(old5, new5, 1)

# --- Edit 6: the rest of loadPosts still refers to `data` for the actual list render — point it at data2 ---
old6 = '''      list.innerHTML = data.map(p => {'''
new6 = '''      list.innerHTML = data2.map(p => {'''

c6 = content.count(old6)
if c6 != 1:
    raise SystemExit(f"ABORTED edit 6: expected 1 match, found {c6}. No changes made.")
content = content.replace(old6, new6, 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done. Sidebar with live topic counts and click-to-filter added.")

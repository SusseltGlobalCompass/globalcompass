path = "forum.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# --- Edit 1: add the topic dropdown to the New Post form ---
old1 = '''      <div id="newPostForm" style="display:none;background:#F8F9FF;border-radius:10px;padding:16px;margin-bottom:20px">
        <input id="postTitle" type="text" placeholder="Title" maxlength="120" style="width:100%;padding:10px 12px;border:1px solid #E0E8F5;border-radius:8px;font-size:13px;margin-bottom:8px">'''

new1 = '''      <div id="newPostForm" style="display:none;background:#F8F9FF;border-radius:10px;padding:16px;margin-bottom:20px">
        <select id="postTopic" style="width:100%;padding:10px 12px;border:1px solid #E0E8F5;border-radius:8px;font-size:13px;margin-bottom:8px;background:#fff">
          <option value="">Choose a topic...</option>
        </select>
        <input id="postTitle" type="text" placeholder="Title" maxlength="120" style="width:100%;padding:10px 12px;border:1px solid #E0E8F5;border-radius:8px;font-size:13px;margin-bottom:8px">'''

c1 = content.count(old1)
if c1 != 1:
    raise SystemExit(f"ABORTED: expected 1 match for edit 1, found {c1}. No changes made.")
content = content.replace(old1, new1, 1)

# --- Edit 2: populate the dropdown (add function + call it) ---
old2 = '''    async function loadPosts(){'''

new2 = '''    async function loadTopicsIntoDropdown(){
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
    }

    async function loadPosts(){
      loadTopicsIntoDropdown();'''

c2 = content.count(old2)
if c2 != 1:
    raise SystemExit(f"ABORTED: expected 1 match for edit 2, found {c2}. No changes made.")
content = content.replace(old2, new2, 1)

# --- Edit 3: save the chosen topic when submitting a post ---
old3 = '''      const { error } = await sb.from('forum_posts').insert({
        user_id: currentForumUser.id,
        category: currentCategory,
        title: title,
        content: contentText,
        is_approved: false,
        is_flagged: !!matched,
        flag_reason: matched ? ('Contains flagged term: ' + matched) : null
      });'''

new3 = '''      const topicId = document.getElementById('postTopic').value || null;
      const { error } = await sb.from('forum_posts').insert({
        user_id: currentForumUser.id,
        category: currentCategory,
        topic_id: topicId,
        title: title,
        content: contentText,
        is_approved: false,
        is_flagged: !!matched,
        flag_reason: matched ? ('Contains flagged term: ' + matched) : null
      });'''

c3 = content.count(old3)
if c3 != 1:
    raise SystemExit(f"ABORTED: expected 1 match for edit 3, found {c3}. No changes made.")
content = content.replace(old3, new3, 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done. Topic dropdown added, populated from forum_topics, and saved on submit.")

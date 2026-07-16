path = "forum.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# --- Edit 1: loadPosts() — real names + member-since ---
old1 = '''    async function loadPosts(){
      const { data, error } = await sb.from('forum_posts')
        .select('*')
        .eq('category', currentCategory)
        .order('created_at', { ascending: false });
      const list = document.getElementById('postsList');
      if (error || !data || data.length === 0){
        list.innerHTML = '<div style="text-align:center;padding:30px;color:#7A8BAE;font-size:13px">No posts yet — be the first to share.</div>';
        return;
      }
      list.innerHTML = data.map(p => {
        const pending = !p.is_approved ? '<span style="font-size:10px;background:#FFF3D6;color:#8a6a14;padding:2px 8px;border-radius:99px;margin-left:8px">Pending review</span>' : '';
        const name = 'Member';
        return '<div id="post-'+p.id+'" style="border-bottom:0.5px solid #F0F3FA;padding:14px 0"><div style="font-weight:600;font-size:14px;color:#0D1F4A">'+p.title+pending+'</div><div style="font-size:12px;color:#7A8BAE;margin:4px 0">'+name+' · '+new Date(p.created_at).toLocaleDateString()+'</div><div style="font-size:13px;color:#333;margin-bottom:8px">'+p.content+'</div>'+'''

new1 = '''    async function loadPosts(){
      const { data, error } = await sb.from('forum_posts')
        .select('*')
        .eq('category', currentCategory)
        .order('created_at', { ascending: false });
      const list = document.getElementById('postsList');
      if (error || !data || data.length === 0){
        list.innerHTML = '<div style="text-align:center;padding:30px;color:#7A8BAE;font-size:13px">No posts yet — be the first to share.</div>';
        return;
      }
      const postUserIds = [...new Set(data.map(p => p.user_id))];
      const { data: postProfiles } = await sb.from('forum_profiles').select('*').in('user_id', postUserIds);
      const postProfileMap = {};
      (postProfiles || []).forEach(pr => { postProfileMap[pr.user_id] = pr; });
      list.innerHTML = data.map(p => {
        const pending = !p.is_approved ? '<span style="font-size:10px;background:#FFF3D6;color:#8a6a14;padding:2px 8px;border-radius:99px;margin-left:8px">Pending review</span>' : '';
        const profile = postProfileMap[p.user_id];
        const name = profile && profile.display_name ? profile.display_name : 'Member';
        const since = profile && profile.created_at ? ' · Member since ' + new Date(profile.created_at).toLocaleDateString('en-US', { month: 'short', year: 'numeric' }) : '';
        return '<div id="post-'+p.id+'" style="border-bottom:0.5px solid #F0F3FA;padding:14px 0"><div style="font-weight:600;font-size:14px;color:#0D1F4A">'+p.title+pending+'</div><div style="font-size:12px;color:#7A8BAE;margin:4px 0">'+name+since+' · '+new Date(p.created_at).toLocaleDateString()+'</div><div style="font-size:13px;color:#333;margin-bottom:8px">'+p.content+'</div>'+'''

c1 = content.count(old1)
if c1 != 1:
    raise SystemExit(f"ABORTED: expected 1 match for edit 1 (loadPosts), found {c1}. No changes made.")
content = content.replace(old1, new1, 1)

# --- Edit 2: loadReplies() — real names ---
old2 = '''      box.innerHTML = data.map(r => {
        const pending = !r.is_approved ? '<span style="font-size:9px;background:#FFF3D6;color:#8a6a14;padding:1px 7px;border-radius:99px;margin-left:6px">Pending review</span>' : '';
        return '<div style="border-left:2px solid #EEF3FF;padding:6px 0 6px 10px;margin-bottom:4px"><div style="font-size:12px;color:#7A8BAE">Member'+pending+' · '+new Date(r.created_at).toLocaleDateString()+'</div><div style="font-size:13px;color:#333">'+r.content+'</div></div>';
      }).join('');'''

new2 = '''      const replyUserIds = [...new Set(data.map(r => r.user_id))];
      const { data: replyProfiles } = await sb.from('forum_profiles').select('*').in('user_id', replyUserIds);
      const replyProfileMap = {};
      (replyProfiles || []).forEach(pr => { replyProfileMap[pr.user_id] = pr; });
      box.innerHTML = data.map(r => {
        const pending = !r.is_approved ? '<span style="font-size:9px;background:#FFF3D6;color:#8a6a14;padding:1px 7px;border-radius:99px;margin-left:6px">Pending review</span>' : '';
        const profile = replyProfileMap[r.user_id];
        const name = profile && profile.display_name ? profile.display_name : 'Member';
        return '<div style="border-left:2px solid #EEF3FF;padding:6px 0 6px 10px;margin-bottom:4px"><div style="font-size:12px;color:#7A8BAE">'+name+pending+' · '+new Date(r.created_at).toLocaleDateString()+'</div><div style="font-size:13px;color:#333">'+r.content+'</div></div>';
      }).join('');'''

c2 = content.count(old2)
if c2 != 1:
    raise SystemExit(f"ABORTED: expected 1 match for edit 2 (loadReplies), found {c2}. No changes made.")
content = content.replace(old2, new2, 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done. Both loadPosts() and loadReplies() now show real display names, with Member-since on posts.")

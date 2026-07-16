path = "forum.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# --- Edit 1: move postsList out of postingArea so it's visible pre-login ---
old1 = '''      <div id="postsList"></div>
    </div>
  </div>

  <script>'''

new1 = '''    </div>

    <div id="postsList"></div>
  </div>

  <script>'''

count1 = content.count(old1)
if count1 != 1:
    raise SystemExit(f"ABORTED: expected exactly 1 match for edit 1, found {count1}. No changes made.")

content = content.replace(old1, new1, 1)

# --- Edit 2: load posts even when not signed in ---
old2 = '''      } else {
        document.getElementById('loginGate').style.display = 'block';
        document.getElementById('profileGate').style.display = 'none';
        document.getElementById('postingArea').style.display = 'none';
      }'''

new2 = '''      } else {
        document.getElementById('loginGate').style.display = 'block';
        document.getElementById('profileGate').style.display = 'none';
        document.getElementById('postingArea').style.display = 'none';
        loadPosts();
      }'''

count2 = content.count(old2)
if count2 != 1:
    raise SystemExit(f"ABORTED: expected exactly 1 match for edit 2, found {count2}. No changes made.")

content = content.replace(old2, new2, 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done. Both edits applied successfully.")

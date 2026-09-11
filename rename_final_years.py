"""
Rename "Final Years" to "University Pathways" consistently across the
site, and upgrade the homepage section eyebrow with the new, more
explicit callout messaging (Option A, agreed with Susselt).

Run from inside ~/Desktop/GlobalCompass
"""

INDEX_FILE = "index.html"
CAREER_FILE = "career-simulator.html"

# ---- index.html ----
with open(INDEX_FILE, "r", encoding="utf-8") as f:
    content = f.read()
original = content
changes_made = []

# 1. Nav dropdown button
old = '<button class="nb">Final Years <i class="ti ti-chevron-down"'
new = '<button class="nb">University Pathways <i class="ti ti-chevron-down"'
if old in content:
    content = content.replace(old, new)
    changes_made.append("nav dropdown button")
else:
    print("ERROR: nav dropdown button text not found.")

# 2. Mobile nav dropdown
old = 'onclick="toggleMobileDD(this)">Final Years <span>\u2304</span></button>'
new = 'onclick="toggleMobileDD(this)">University Pathways <span>\u2304</span></button>'
if old in content:
    content = content.replace(old, new)
    changes_made.append("mobile nav dropdown")
else:
    print("ERROR: mobile nav dropdown text not found.")

# 3. Feature card badge (span class="f-t")
old = '<p class="f-p">Final year students select subjects based on their university major and destination country</p><span class="f-t">Final Years</span>'
new = '<p class="f-p">Final year students select subjects based on their university major and destination country</p><span class="f-t">University Pathways</span>'
if old in content:
    content = content.replace(old, new)
    changes_made.append("feature card badge")
else:
    print("ERROR: feature card badge text not found.")

# 4. Section eyebrow - full upgrade to Option A messaging
old = '<div class="ew lt">Final Years \u2014 the bridge to university</div>'
new = '<div class="ew lt">University Pathways \u2014 tailor today\u2019s subjects to tomorrow\u2019s dream university, and uncover the hidden clues along the way</div>'
if old in content:
    content = content.replace(old, new)
    changes_made.append("section eyebrow + callout")
else:
    print("ERROR: section eyebrow text not found.")

# 5. Footer link
old = '<a class="ft-link" href="#">Final Years</a>'
new = '<a class="ft-link" href="#">University Pathways</a>'
if old in content:
    content = content.replace(old, new)
    changes_made.append("footer link")
else:
    print("ERROR: footer link text not found.")

if content != original:
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"index.html updated: {', '.join(changes_made)}")
else:
    print("WARNING: index.html - no changes made at all.")

# ---- career-simulator.html ----
with open(CAREER_FILE, "r", encoding="utf-8") as f:
    content2 = f.read()
original2 = content2

old = '<div class="nav-tag">Final Years \u00b7 Career Simulator</div>'
new = '<div class="nav-tag">University Pathways \u00b7 Career Simulator</div>'
if old in content2:
    content2 = content2.replace(old, new)
    with open(CAREER_FILE, "w", encoding="utf-8") as f:
        f.write(content2)
    print("career-simulator.html updated: nav tag")
else:
    print("ERROR: career-simulator.html nav tag text not found.")

if content2 == original2:
    print("WARNING: career-simulator.html - no changes made at all.")

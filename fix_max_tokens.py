"""
Raise the shared max_tokens:2000 limit to 3000 across all pathway
navigators, to prevent AI responses being truncated mid-JSON
(the cause of "Unterminated string" parse errors and short results).

Leaves intentionally-short limits (800, 700, 300) untouched, since
those are for shorter, different kinds of outputs.

Run from inside ~/Desktop/GlobalCompass
"""

import glob

files_to_check = glob.glob("*.html")
old_pattern = "max_tokens:2000"
new_pattern = "max_tokens:3000"

changed_files = []
unchanged_files = []

for filename in files_to_check:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    count = content.count(old_pattern)
    if count > 0:
        new_content = content.replace(old_pattern, new_pattern)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(new_content)
        changed_files.append((filename, count))

print(f"Updated {len(changed_files)} file(s):")
for filename, count in changed_files:
    print(f"  - {filename}: {count} occurrence(s) changed from 2000 to 3000")

if not changed_files:
    print("WARNING: No files were changed. Check the pattern matches.")

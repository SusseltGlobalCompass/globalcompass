"""
Fix the school card fee display so fee_label shows on its own when
fee_min/fee_max are null (e.g. Brazilian international schools with
researched fee text but no currency-safe numeric range yet).

Run from inside ~/Desktop/GlobalCompass
"""

FILE = "schools.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

original = content

old_line = '    const feeRange = (s.fee_min!=null && s.fee_max!=null) ? (s.fee_currency||"AED")+" "+s.fee_min.toLocaleString()+"-"+s.fee_max.toLocaleString()+(s.fee_label?(" "+s.fee_label):"/month") : "";'
new_line = '    const feeRange = (s.fee_min!=null && s.fee_max!=null) ? (s.fee_currency||"AED")+" "+s.fee_min.toLocaleString()+"-"+s.fee_max.toLocaleString()+(s.fee_label?(" "+s.fee_label):"/month") : (s.fee_label || "");'

if old_line not in content:
    print("ERROR: Could not find exact feeRange line. No changes made.")
else:
    content = content.replace(old_line, new_line)
    with open(FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print("Done. fee_label now displays independently when no numeric fee range exists.")

if content == original:
    print("WARNING: No changes were made at all.")

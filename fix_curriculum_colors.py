# CBSE: navy -> official Saffron Deep
with open("cbse-stream-navigator.html", "r", encoding="utf-8") as f:
    c = f.read()
c = c.replace(
    '.step-circle.active{background:#1B3A7A;color:#F5C842;border:2px solid #F5C842}',
    '.step-circle.active{background:#8B3A00;color:#F5C842;border:2px solid #F5C842}'
)
c = c.replace(
    '.step-label.active{color:#1B3A7A;font-weight:700}',
    '.step-label.active{color:#8B3A00;font-weight:700}'
)
with open("cbse-stream-navigator.html", "w", encoding="utf-8") as f:
    f.write(c)
print("CBSE corrected to Saffron Deep #8B3A00")

# Singapore: C8102E -> official Lion City Crimson B3001B
with open("singapore-pathway-navigator.html", "r", encoding="utf-8") as f:
    s = f.read()
s = s.replace('#C8102E', '#B3001B')
with open("singapore-pathway-navigator.html", "w", encoding="utf-8") as f:
    f.write(s)
print("Singapore corrected to Lion City Crimson #B3001B")

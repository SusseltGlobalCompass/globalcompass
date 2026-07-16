path = "index.html"

with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

start = 418 - 1
end = 436

before = lines[:start]
after = lines[end:]

new_block = '''<section class="sec md">
  <div class="ew">Explore by country</div>
  <h2 class="sh2">Schools in 190+ countries</h2>
  <div class="s-rule"></div>
  <div class="cg">
    <a class="cc" href="schools.html?q=UAE" style="text-decoration:none;cursor:pointer"><span class="c-flag">\U0001F1E6\U0001F1EA</span><div><div class="c-name">UAE</div><div class="c-count">756+ schools</div></div></a>
    <a class="cc" href="schools.html?q=Singapore" style="text-decoration:none;cursor:pointer"><span class="c-flag">\U0001F1F8\U0001F1EC</span><div><div class="c-name">Singapore</div><div class="c-count">Coming soon</div></div></a>
    <a class="cc" href="schools.html?q=UK" style="text-decoration:none;cursor:pointer"><span class="c-flag">\U0001F1EC\U0001F1E7</span><div><div class="c-name">United Kingdom</div><div class="c-count">Coming soon</div></div></a>
    <a class="cc" href="schools.html?q=Germany" style="text-decoration:none;cursor:pointer"><span class="c-flag">\U0001F1E9\U0001F1EA</span><div><div class="c-name">Germany</div><div class="c-count">Coming soon</div></div></a>
    <a class="cc" href="schools.html?q=Australia" style="text-decoration:none;cursor:pointer"><span class="c-flag">\U0001F1E6\U0001F1FA</span><div><div class="c-name">Australia</div><div class="c-count">Coming soon</div></div></a>
    <a class="cc" href="schools.html?q=Qatar" style="text-decoration:none;cursor:pointer"><span class="c-flag">\U0001F1F6\U0001F1E6</span><div><div class="c-name">Qatar</div><div class="c-count">Coming soon</div></div></a>
    <a class="cc" href="schools.html?q=Canada" style="text-decoration:none;cursor:pointer"><span class="c-flag">\U0001F1E8\U0001F1E6</span><div><div class="c-name">Canada</div><div class="c-count">Coming soon</div></div></a>
    <a class="cc" href="schools.html?q=France" style="text-decoration:none;cursor:pointer"><span class="c-flag">\U0001F1EB\U0001F1F7</span><div><div class="c-name">France</div><div class="c-count">Coming soon</div></div></a>
    <a class="cc" href="schools.html?q=South+Africa" style="text-decoration:none;cursor:pointer"><span class="c-flag">\U0001F1FF\U0001F1E6</span><div><div class="c-name">South Africa</div><div class="c-count">Coming soon</div></div></a>
    <a class="cc" href="schools.html?q=Nigeria" style="text-decoration:none;cursor:pointer"><span class="c-flag">\U0001F1F3\U0001F1EC</span><div><div class="c-name">Nigeria</div><div class="c-count">Coming soon</div></div></a>
    <a class="cc" href="schools.html?q=Kenya" style="text-decoration:none;cursor:pointer"><span class="c-flag">\U0001F1F0\U0001F1EA</span><div><div class="c-name">Kenya</div><div class="c-count">Coming soon</div></div></a>
    <a class="cc" href="schools.html?q=New+Zealand" style="text-decoration:none;cursor:pointer"><span class="c-flag">\U0001F1F3\U0001F1FF</span><div><div class="c-name">New Zealand</div><div class="c-count">Coming soon</div></div></a>
  </div>
</section>
'''

new_lines = before + [new_block] + after

with open(path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("Done. Replaced lines 418-436 with honest version (UAE 756+, others Coming soon).")

import os

HTML_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "portfolio.html")
if not os.path.exists(HTML_PATH) and os.path.exists(r"d:\vinayaka\portfolio.html"):
    HTML_PATH = r"d:\vinayaka\portfolio.html"

with open(HTML_PATH, "r", encoding="utf-8") as f:
    c = f.read()

# 1. Add CSS styles
css_target = ".Hard {\n      color: #e5484d;\n      border-color: #e5484d\n    }"
new_css = css_target + """\n    .lc-wrap { display: flex; gap: 24px; align-items: flex-start; flex-wrap: wrap; margin-top: 18px; }
    .lc-card { background: var(--card); border: 1px solid var(--line); border-radius: 16px; padding: 18px 20px; flex: 1; min-width: 280px; }
    .lc-card h3 { margin: 0 0 14px; font-size: 16px; display: flex; align-items: center; gap: 8px; }
    .lc-img-wrap { width: 100%; border-radius: 12px; overflow: hidden; border: 1px solid var(--line); background: var(--bg); }
    .lc-img-wrap img { width: 100%; height: auto; display: block; }
    .award-img-card { background: var(--card); border: 1px solid var(--line); border-radius: 16px; overflow: hidden; margin: 18px 0 24px; transition: transform .2s ease, box-shadow .2s ease; }
    .award-img-card:hover { box-shadow: 0 10px 28px -10px rgba(0,0,0,0.15); }
    .award-card-inner { display: flex; align-items: stretch; }
    .award-photo-container { position: relative; flex: 0 0 340px; max-width: 360px; min-height: 220px; background: #0b0f1d; overflow: hidden; display: flex; align-items: center; justify-content: center; }
    .award-photo { width: 100%; height: 100%; min-height: 220px; max-height: 280px; object-fit: cover; object-position: center 20%; display: block; transition: transform .35s ease; }
    .award-img-card:hover .award-photo { transform: scale(1.03); }
    .award-badge-overlay { position: absolute; top: 12px; left: 12px; background: rgba(11, 15, 29, 0.82); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); color: #fbbf24; font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 20px; border: 1px solid rgba(251, 191, 36, 0.35); letter-spacing: .02em; }
    .award-content { padding: 22px 24px; flex: 1; display: flex; flex-direction: column; justify-content: center; min-width: 0; }
    .award-tag-row { display: flex; align-items: center; gap: 8px; margin-bottom: 8px; flex-wrap: wrap; }
    .chip-award { display: inline-flex; align-items: center; gap: 4px; font-size: 12px; font-weight: 600; padding: 2px 10px; border-radius: 99px; background: color-mix(in srgb, var(--acc) 14%, transparent); color: var(--acc); border: 1px solid color-mix(in srgb, var(--acc) 30%, transparent); }
    .chip-award-sub { font-size: 12px; color: var(--mute); }
    .award-title { margin: 0 0 6px; font-size: 20px; font-weight: 800; color: var(--ink); line-height: 1.25; }
    .award-institution { font-size: 13px; color: var(--mute); margin-bottom: 12px; }
    .award-institution strong { color: var(--ink); }
    .award-desc { margin: 0 0 14px; font-size: 14px; line-height: 1.6; color: var(--ink); }
    .award-desc em { color: var(--acc); font-style: normal; font-weight: 600; }
    .award-tags { display: flex; flex-wrap: wrap; gap: 6px; }
    @media(max-width:800px) { .lc-wrap { flex-direction: column; } .lc-card { min-width: unset; max-width: 100%!important; } .award-card-inner { flex-direction: column; } .award-photo-container { flex: none; width: 100%; max-width: 100%; min-height: 190px; max-height: 230px; } .award-photo { max-height: 230px; } .award-content { padding: 18px 20px; } }"""

# 2. Update Achievements section
ach_old = """    <section id="ach-s">
      <h2>Achievements <button class="btn owner" data-add="ach">+ Add</button></h2>
      <p class="sub">Awards and certifications.</p>
      <div id="ach"></div>
    </section>"""
ach_new = """    <section id="ach-s">
      <h2>Achievements <button class="btn owner" data-add="ach">+ Add</button></h2>
      <p class="sub">Awards and certifications.</p>
      <div class="award-img-card">
        <div class="award-card-inner">
          <div class="award-photo-container">
            <img src="award.png" alt="Best Project Award 2026 graduation ceremony at Siddaganga Institute of Technology" class="award-photo" loading="lazy">
            <div class="award-badge-overlay">&#x1F3C6; Best Project 2026</div>
          </div>
          <div class="award-content">
            <div class="award-tag-row">
              <span class="chip-award">&#x1F3C6; College Award</span>
              <span class="chip-award-sub">Siddaganga Institute of Technology</span>
            </div>
            <h3 class="award-title">Best Project Award 2026</h3>
            <div class="award-institution">
              <strong>Siddaganga Institute of Technology, Tumakuru</strong> &middot; Dept. of CSE (AIML)
            </div>
            <p class="award-desc">
              Won <strong>Best Project of the Year 2026</strong> for developing the <em>Edge Enabled Framework for Tree Climbing Robot</em> &mdash; an automated robotic system for areca nut harvesting engineered with ESP32 motor controls, camera monitoring, and Raspberry Pi edge intelligence.
            </p>
            <div class="award-tags">
              <span class="chip">Robotics</span>
              <span class="chip">Raspberry Pi</span>
              <span class="chip">ESP32</span>
              <span class="chip">Python</span>
              <span class="chip">Edge AI</span>
            </div>
          </div>
        </div>
      </div>
      <div id="ach"></div>
    </section>"""

# 3. Update DSA section with LeetCode board
dsa_old = """    <section id="dsa">
      <h2>Daily DSA log</h2>
      <p class="sub">Every problem I solve, with my approach and code. <button class="btn owner" data-add="dsa">+ Add
          today’s problem</button></p>
      <div class="stats" id="stats"></div>
      <div class="filters" id="filters"></div>
      <div id="dsa-l"></div>
    </section>"""
dsa_new = """    <section id="dsa">
      <h2>Daily DSA log</h2>
      <p class="sub">Every problem I solve, with my approach and code. <button class="btn owner" data-add="dsa">+ Add today’s problem</button></p>
      <div class="lc-wrap">
        <div class="lc-card">
          <h3>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M13.483 0a1.374 1.374 0 0 0-.961.438L7.116 6.226l-3.854 4.126a5.266 5.266 0 0 0-1.209 2.104 5.35 5.35 0 0 0-.125.513 5.527 5.527 0 0 0 .062 2.362 5.83 5.83 0 0 0 .349 1.017 5.938 5.938 0 0 0 1.271 1.818l4.277 4.193.039.038c2.248 2.165 5.852 2.133 8.063-.074l2.396-2.396c.54-.54.54-1.414.003-1.955a1.378 1.378 0 0 0-1.951-.003l-2.396 2.396a3.021 3.021 0 0 1-4.205.038l-.02-.019-4.276-4.193c-.652-.64-.972-1.469-.948-2.263a2.68 2.68 0 0 1 .066-.523 2.545 2.545 0 0 1 .619-1.164L9.13 8.114c1.058-1.134 3.204-1.27 4.43-.278l3.501 2.831c.593.48 1.461.387 1.94-.207a1.384 1.384 0 0 0-.207-1.943l-3.5-2.831c-.8-.647-1.766-1.045-2.774-1.202l2.015-2.158A1.384 1.384 0 0 0 13.483 0zm-2.866 12.815a1.38 1.38 0 0 0-1.38 1.382 1.38 1.38 0 0 0 1.38 1.382H20.79a1.38 1.38 0 0 0 1.38-1.382 1.38 1.38 0 0 0-1.38-1.382z" fill="var(--acc)"/></svg>
            LeetCode Solved Board
            <a href="https://leetcode.com/u/Vinayaka-07/" target="_blank" rel="noopener" style="margin-left:auto;font-size:12px;font-weight:400;color:var(--mute);text-decoration:none">View Profile &#x2197;</a>
          </h3>
          <div class="lc-img-wrap">
            <a href="https://leetcode.com/u/Vinayaka-07/" target="_blank" rel="noopener">
              <img id="lc-card-img" src="https://leetcard.jacoblin.cool/Vinayaka-07?theme=dark&font=Nunito&ext=activity" alt="LeetCode stats board for Vinayaka-07" loading="lazy" width="495" height="195">
            </a>
          </div>
        </div>
        <div class="lc-card" style="flex:0 0 auto;min-width:240px;max-width:320px">
          <h3>My DSA Stats</h3>
          <div class="stats" id="stats" style="flex-direction:column;gap:14px;margin:0"></div>
        </div>
      </div>
      <div style="margin-top:24px"><div class="filters" id="filters"></div><div id="dsa-l"></div></div>
    </section>"""

# 4. Sync LeetCode card theme
js_swz = "$(\"swz\").addEventListener(\"click\", function (e) { if (e.target.dataset.bg) setBg(e.target.dataset.bg) });"
js_theme = js_swz + """\n    function syncLCTheme(){
      var img=document.getElementById("lc-card-img");if(!img)return;
      var bg=document.documentElement.getAttribute("data-bg")||"auto";
      var isDark=(bg=="forest"||bg=="plum"||bg=="slate")||(bg=="auto"&&window.matchMedia&&window.matchMedia("(prefers-color-scheme:dark)").matches);
      img.src="https://leetcard.jacoblin.cool/Vinayaka-07?font=Nunito&ext=activity&theme="+(isDark?"dark":"light")+"&t="+Date.now();
    }
    document.getElementById("swz").addEventListener("click",function(){setTimeout(syncLCTheme,120)});"""

if "lc-wrap" in c:
    print("INFO: Portfolio already contains the Award image and LeetCode board updates.")
else:
    c = c.replace(css_target, new_css, 1)
    c = c.replace(ach_old, ach_new, 1)
    c = c.replace(dsa_old, dsa_new, 1)
    c = c.replace(js_swz, js_theme, 1)
    c = c.replace("load(); render(); tryOwner();", "load(); render(); tryOwner(); syncLCTheme();", 1)

    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(c)

    print("SUCCESS: Portfolio updated with Award image (award.png) and LeetCode board (Vinayaka-07)!")

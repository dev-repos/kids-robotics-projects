import os, html, shutil
from data import P
import json
NS=json.load(open('sheets.json'))
def tl(s): return ' · '.join(f'[template {i} PNG](template-{i}.png)' for i in range(1,NS[s]+1))
OUT="site"; os.makedirs(OUT,exist_ok=True)
S='stroke="#222" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"'
I={
"box":f'<rect x="15" y="30" width="70" height="55" fill="#d9a066" {S}/><path d="M15 30 L30 15 H100 L85 30 M85 85 L100 70 V15" fill="#c48a52" {S}/>',
"tube":f'<rect x="35" y="10" width="30" height="80" rx="6" fill="#e8c08a" {S}/><ellipse cx="50" cy="12" rx="15" ry="5" fill="#fff" {S}/>',
"caps":f'<circle cx="32" cy="50" r="20" fill="#3dbbff" {S}/><circle cx="72" cy="50" r="20" fill="#ff5c8a" {S}/>',
"glue":f'<rect x="35" y="30" width="30" height="60" rx="5" fill="#9b59b6" {S}/><rect x="40" y="10" width="20" height="22" fill="#fff" {S}/>',
"scissors":f'<circle cx="30" cy="75" r="12" fill="#ff8a3d" {S}/><circle cx="70" cy="75" r="12" fill="#ff8a3d" {S}/><path d="M38 66 L75 15 M62 66 L25 15" fill="none" {S}/>',
"pens":f'<g transform="rotate(-20 50 50)"><rect x="40" y="15" width="20" height="60" fill="#e04f5f" {S}/><path d="M40 75 L50 92 L60 75" fill="#fff" {S}/></g>',
"brush":f'<rect x="15" y="55" width="70" height="14" rx="6" fill="#3dbbff" {S}/><path d="M22 55 V30 M32 55 V30 M42 55 V30 M52 55 V30 M62 55 V30 M72 55 V30" {S}/>',
"motor":f'<rect x="20" y="30" width="50" height="40" rx="8" fill="#bbb" {S}/><path d="M70 50 H88" {S}/><rect x="84" y="38" width="8" height="18" fill="#ffcc00" {S}/>',
"battery":f'<rect x="15" y="30" width="65" height="40" rx="6" fill="#2ec27e" {S}/><rect x="80" y="42" width="8" height="16" fill="#222"/><text x="40" y="58" font-size="22" font-weight="bold" fill="#fff">+</text>',
"tape":f'<circle cx="50" cy="50" r="35" fill="#ffd27a" {S}/><circle cx="50" cy="50" r="14" fill="#fff" {S}/>',
"eyes":f'<circle cx="32" cy="50" r="18" fill="#fff" {S}/><circle cx="36" cy="54" r="7" fill="#222"/><circle cx="70" cy="50" r="18" fill="#fff" {S}/><circle cx="66" cy="54" r="7" fill="#222"/>',
"cup":f'<path d="M22 20 H78 L68 88 H32 Z" fill="#ff5c8a" {S}/>',
"cork":f'<rect x="30" y="25" width="40" height="50" rx="8" fill="#b5835a" {S}/>',
"card":f'<rect x="12" y="25" width="76" height="50" fill="#e0b47c" {S}/><path d="M12 42 H88 M12 58 H88" stroke="#b0824a" stroke-width="3"/>',
"syringe":f'<rect x="25" y="40" width="50" height="20" fill="#dff4ff" {S}/><path d="M75 50 H90 M25 50 H10 M10 38 V62" {S}/><rect x="28" y="43" width="25" height="14" fill="#3dbbff"/>',
"hose":f'<path d="M10 70 C30 10, 70 90, 90 30" fill="none" stroke="#222" stroke-width="12" stroke-linecap="round"/><path d="M10 70 C30 10, 70 90, 90 30" fill="none" stroke="#9fe3ff" stroke-width="6" stroke-linecap="round"/>',
"water":f'<path d="M50 12 C70 45, 78 58, 78 66 A28 28 0 0 1 22 66 C22 58, 30 45, 50 12 Z" fill="#3dbbff" {S}/>',
"pin":f'<circle cx="50" cy="30" r="14" fill="#ffcc00" {S}/><path d="M45 44 L38 88 M55 44 L62 88" {S}/>',
"straw":f'<rect x="42" y="8" width="16" height="84" fill="#fff" {S}/><path d="M42 25 L58 35 M42 45 L58 55 M42 65 L58 75" stroke="#e04f5f" stroke-width="5"/>',
"string":f'<circle cx="50" cy="50" r="30" fill="#c46bff" {S}/><path d="M28 40 Q50 55 72 38 M25 58 Q50 72 75 55" fill="none" {S}/><path d="M78 60 Q90 80 70 92" fill="none" {S}/>',
"paper":f'<path d="M22 10 H65 L80 25 V90 H22 Z" fill="#fff" {S}/><path d="M65 10 V25 H80" fill="none" {S}/>',
"foil":f'<path d="M15 25 L85 20 L80 80 L20 78 Z" fill="#d0d6dc" {S}/><path d="M30 35 L60 60 M55 30 L40 65" stroke="#fff" stroke-width="4"/>',
"led":f'<path d="M30 55 V30 A20 20 0 0 1 70 30 V55 Z" fill="#ff5252" {S}/><rect x="25" y="55" width="50" height="8" fill="#ff5252" {S}/><path d="M40 63 V92 M60 63 V82" {S}/>',
"clip":f'<path d="M20 40 H80 L70 75 H30 Z" fill="#222"/><path d="M30 40 L40 12 M70 40 L60 12" fill="none" stroke="#888" stroke-width="5"/>',
"sponge":f'<rect x="15" y="30" width="70" height="40" rx="8" fill="#ffe14d" {S}/><circle cx="35" cy="45" r="4" fill="#d4b000"/><circle cx="60" cy="55" r="5" fill="#d4b000"/>',
"buzzer":f'<circle cx="45" cy="50" r="28" fill="#333" {S}/><circle cx="45" cy="50" r="6" fill="#fff"/><path d="M80 35 Q88 50 80 65 M88 28 Q100 50 88 72" fill="none" {S}/>',
"wire":f'<path d="M10 30 C40 30 60 70 90 70" fill="none" stroke="#e04f5f" stroke-width="7" stroke-linecap="round"/><path d="M10 50 C40 50 60 90 90 90" fill="none" stroke="#222" stroke-width="7" stroke-linecap="round"/>',
"microbit":f'<rect x="10" y="22" width="80" height="56" rx="8" fill="#2b2b2b" {S}/>'+''.join(f'<rect x="{34+c*7}" y="{34+r*7}" width="4" height="4" fill="#ff3b30"/>' for r in range(5) for c in range(5))+'<circle cx="20" cy="50" r="5" fill="#bbb"/><circle cx="80" cy="50" r="5" fill="#bbb"/>',
"usb":f'<rect x="15" y="40" width="30" height="20" fill="#bbb" {S}/><path d="M45 50 C70 50 70 20 92 20" fill="none" stroke="#222" stroke-width="7" stroke-linecap="round"/>',
"arduino":f'<rect x="10" y="22" width="80" height="56" rx="5" fill="#00979d" {S}/><rect x="15" y="28" width="16" height="14" fill="#bbb"/><rect x="45" y="45" width="36" height="12" fill="#222"/>'+''.join(f'<rect x="{30+i*7}" y="24" width="4" height="6" fill="#222"/>' for i in range(8)),
"breadboard":f'<rect x="8" y="25" width="84" height="50" rx="4" fill="#f4f4f4" {S}/>'+''.join(f'<circle cx="{18+c*10}" cy="{38+r*12}" r="2.5" fill="#888"/>' for r in range(3) for c in range(8)),
"sonar":f'<rect x="10" y="30" width="80" height="40" rx="4" fill="#1f8fff" {S}/><circle cx="32" cy="50" r="14" fill="#ddd" {S}/><circle cx="68" cy="50" r="14" fill="#ddd" {S}/>',
"servo":f'<rect x="20" y="35" width="60" height="40" rx="4" fill="#1f5fff" {S}/><circle cx="38" cy="35" r="10" fill="#fff" {S}/><path d="M38 35 H75" stroke="#fff" stroke-width="8" stroke-linecap="round"/>',
"ir":f'<rect x="20" y="20" width="60" height="55" rx="4" fill="#2e7d32" {S}/><circle cx="40" cy="80" r="8" fill="#222"/><circle cx="60" cy="80" r="8" fill="#38f"/>',
"driver":f'<rect x="15" y="25" width="70" height="55" rx="4" fill="#e53935" {S}/><rect x="35" y="15" width="30" height="25" fill="#222"/><path d="M38 15 V5 M46 15 V5 M54 15 V5 M62 15 V5" stroke="#222" stroke-width="3"/>',
}
ROBOT='''<svg viewBox="0 0 200 220" width="340"><line x1="100" y1="10" x2="100" y2="35" stroke="#222" stroke-width="6"/><circle cx="100" cy="12" r="10" fill="#ffcc00" stroke="#222" stroke-width="5"/>
<rect x="45" y="35" width="110" height="80" rx="22" fill="#7fd3ff" stroke="#222" stroke-width="6"/><circle cx="78" cy="72" r="14" fill="#fff" stroke="#222" stroke-width="5"/><circle cx="122" cy="72" r="14" fill="#fff" stroke="#222" stroke-width="5"/><circle cx="80" cy="74" r="6" fill="#222"/><circle cx="120" cy="74" r="6" fill="#222"/><path d="M82 96 Q100 108 118 96" fill="none" stroke="#222" stroke-width="5" stroke-linecap="round"/>
<rect x="55" y="122" width="90" height="75" rx="16" fill="#ff8a3d" stroke="#222" stroke-width="6"/><circle cx="100" cy="158" r="13" fill="#ffcc00" stroke="#222" stroke-width="5"/><path d="M55 140 L25 170 M145 140 L175 170" stroke="#222" stroke-width="8" stroke-linecap="round"/></svg>'''
def icon(k): return f'<svg viewBox="0 0 100 100" width="150" height="150">{I[k]}</svg>'
CSS='''@page{size:A4;margin:0}*{box-sizing:border-box}body{margin:0;font-family:"Noto Sans","DejaVu Sans",sans-serif;color:#222}
.page{width:210mm;height:297mm;padding:11mm;display:flex;flex-direction:column;gap:3mm;background:#fffdf6}
.head{background:var(--c);border:3px solid #222;border-radius:9mm;padding:4mm 7mm;display:flex;align-items:center;justify-content:space-between;color:#fff}
.head h1{margin:0;font-size:27pt;line-height:1.05;text-shadow:2px 2px 0 #0004}.head .meta{font-size:15pt;margin-top:2mm}
.box{border:3px solid #222;border-radius:7mm;padding:3mm 5mm;background:#fff}h2{margin:0 0 3mm;font-size:16pt;color:var(--c)}
.parts{display:grid;grid-template-columns:repeat(3,1fr);gap:2mm}.part{text-align:center;font-size:10.5pt}.part svg{width:15mm;height:15mm}
ol{margin:0;padding:0;list-style:none;counter-reset:s}li{counter-increment:s;display:flex;align-items:center;gap:4mm;font-size:12pt;margin:1.1mm 0}
li:before{content:counter(s);flex:0 0 9mm;height:9mm;border-radius:50%;background:var(--c);color:#fff;font-weight:bold;font-size:14pt;display:flex;align-items:center;justify-content:center;border:2.5px solid #222}
.row{display:flex;gap:5mm}.row .box{flex:1;font-size:11pt}.safe{background:#fff3cd}.foot{margin-top:auto;font-size:10pt;text-align:center;color:#555}
.check{display:inline-block;width:6mm;height:6mm;border:2px solid #222;border-radius:1.5mm;margin-left:auto}'''
def card(p):
    parts=''.join(f'<div class="part">{icon(k)}<br>{html.escape(t)}</div>' for k,t in p["parts"])
    steps=''.join(f'<li>{html.escape(s)}<span class="check"></span></li>' for s in p["steps"])
    code=f'<br><b>Code:</b> {p["code"][0]} (in the project folder)' if p["code"] else ''
    n=int(p["slug"][:2])
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="page" style="--c:{p["color"]}">
<div class="head"><div><div class="meta">Robotics Project #{n} · Kids.JoinDev</div><h1>{html.escape(p["title"])}</h1><div class="meta">Ages {p["age"]} · {p["time"]} · Build with a grown-up!</div></div>{ROBOT.replace('width="340"','width="110"')}</div>
<div class="box"><h2>🎯 Goal</h2><div style="font-size:14pt">{html.escape(p["goal"])}</div></div>
<div class="box"><h2>🧰 You need</h2><div class="parts">{parts}</div></div>
<div class="box"><h2>🔧 Build it</h2><ol>{steps}</ol></div>
<div class="row"><div class="box safe"><h2>⚠️ Safety</h2>{html.escape(p["safety"])}</div><div class="box"><h2>💡 How it works</h2>{html.escape(p["how"])}{code}</div></div>
<div class="foot">github.com/dev-repos/kids-robotics-projects · youtube.com/@Kids.JoinDev · CC BY 4.0</div></div></body></html>'''
def md(p):
    n=int(p["slug"][:2]); c=p["code"]
    s=f'# Project {n}: {p["title"]}\n\n**Ages:** {p["age"]} · **Time:** {p["time"]} · Build with a grown-up.\n\n![Printable build card](card.png)\n\nPrintable A4 build-steps sheet: [card.png](card.png) · [card.pdf](card.pdf)\n\n**1:1 cut/fold templates (print at 100% / Actual size, do not fit to page):** [templates.pdf](templates.pdf) (preferred) · '+tl(p['slug'])+'. Check the 100 mm calibration bar first. Solid = cut, dashed = fold, grey circles = holes, red = size in mm.\n\n## Goal\n\n{p["goal"]}\n\n## Parts list\n\n'+''.join(f'- {t}\n' for _,t in p["parts"])
    s+='\n## Steps\n\n'+''.join(f'{i}. {x}\n' for i,x in enumerate(p["steps"],1))
    s+=f'\n## Safety with a grown-up\n\n{p["safety"]}\n\n## How it works\n\n{p["how"]}\n\n## Coding piece\n\n'
    s+=(f'See [`{c[0]}`]({c[0]}).\n\n```{"python" if c[0].endswith(".py") else "cpp"}\n{c[1]}```\n' if c else 'No code in this one: it is all hands-on building. 🛠️\n')
    s+='\n## Try next\n\nChange one thing (size, weight, speed, number) and see what happens. Draw what you built!\n'
    return s
from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    b=pw.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg=b.new_page(viewport={"width":794,"height":1123},device_scale_factor=2480/794)
    for p in P:
        d=f'{OUT}/projects/{p["slug"]}'; os.makedirs(d,exist_ok=True)
        open(f'{d}/README.md','w').write(md(p))
        if p["code"]: open(f'{d}/{p["code"][0]}','w').write(p["code"][1])
        h=card(p); open(f'{d}/card.html','w').write(h)
        pg.set_content(h); pg.wait_for_timeout(200)
        assert pg.evaluate("document.querySelector('.page').scrollHeight")<=1123, p["slug"]
        pg.screenshot(path=f'{d}/card_raw.png',clip={"x":0,"y":0,"width":794,"height":1123})
        pg.pdf(path=f'{d}/card.pdf',format="A4",print_background=True)
    b.close()
from PIL import Image
for p in P:
    d=f'{OUT}/projects/{p["slug"]}'; im=Image.open(f'{d}/card_raw.png').convert("RGB").resize((2480,3508),Image.LANCZOS)
    im.save(f'{d}/card.png',dpi=(300,300)); os.remove(f'{d}/card_raw.png')
rows=''.join(f'<a class="c" href="projects/{p["slug"]}/README.md" style="--c:{p["color"]}"><img src="projects/{p["slug"]}/card.png" alt=""><b>#{int(p["slug"][:2])} {html.escape(p["title"])}</b><span>Ages {p["age"]} · {p["time"]}</span></a><div class="l"><a href="projects/{p["slug"]}/README.md">Guide</a> · <a href="projects/{p["slug"]}/card.png">A4 PNG</a> · <a href="projects/{p["slug"]}/card.pdf">A4 PDF</a>'+(f' · <a href="projects/{p["slug"]}/{p["code"][0]}">Code</a>' if p["code"] else '')+'</div>' for p in P)
rows=''.join(f'<div class="cell">{x}</div>' for x in rows.split('</div>')[:-1] ) if False else rows
cells=''
for p in P:
    s=p["slug"]; n=int(s[:2]); code=f' · <a href="projects/{s}/{p["code"][0]}">Code</a>' if p["code"] else ''
    cells+=f'<div class="cell" style="--c:{p["color"]}"><a href="projects/{s}/card.png"><img src="projects/{s}/card.png" alt="{html.escape(p["title"])} build card" loading="lazy"></a><h3>#{n} {html.escape(p["title"])}</h3><p>Ages {p["age"]} · {p["time"]}</p><p><a href="https://github.com/dev-repos/kids-robotics-projects/blob/gh-pages/projects/{s}/README.md">Guide</a> · <a href="projects/{s}/card.png">A4 PNG</a> · <a href="projects/{s}/card.pdf">A4 PDF</a>{code}<br><b>1:1 templates:</b> <a href="projects/{s}/templates.pdf">PDF</a> · '+' · '.join(f'<a href="projects/{s}/template-{i}.png">sheet {i}</a>' for i in range(1,NS[s]+1))+f'</p></div>'
open(f'{OUT}/index.html','w').write(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Robotics Projects for Kids · Kids.JoinDev</title>
<style>body{{margin:0;font-family:system-ui,sans-serif;background:#fffdf6;color:#222}}header{{background:#7fd3ff;border-bottom:4px solid #222;padding:24px;display:flex;gap:20px;align-items:center;justify-content:center;flex-wrap:wrap}}h1{{font-size:2.4rem;margin:0}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:20px;padding:24px;max-width:1200px;margin:auto}}.cell{{background:#fff;border:3px solid #222;border-top:12px solid var(--c);border-radius:16px;padding:12px}}.cell img{{width:100%;border-radius:8px;border:1px solid #ccc}}h3{{margin:8px 0 4px}}p{{margin:4px 0}}a{{color:#0b63c5}}footer{{text-align:center;padding:24px;font-size:.9rem}}</style></head><body>
<header>{ROBOT.replace('width="340"','width="110"')}<div><h1>Robotics Projects for Kids</h1><p>Build real robots with cheap, safe parts. Ages 6–12. Always build with a grown-up!<br>Watch on YouTube: <a href="https://www.youtube.com/playlist?list=PLeEznjsWgvDM">Robotics Projects for Kids playlist</a> · <a href="https://www.youtube.com/@Kids.JoinDev">@Kids.JoinDev</a> · <a href="https://kids.join.dev">kids.join.dev</a></p></div></header>
<div class="grid">{cells}</div><footer>Code: MIT · Guides and build cards: CC BY 4.0 · See <a href="LICENSE">LICENSE</a> · <a href="https://github.com/dev-repos/kids-robotics-projects">Source on GitHub</a></footer></body></html>''')
lst=''.join(f'| {int(p["slug"][:2])} | [{p["title"]}](projects/{p["slug"]}/README.md) | {p["age"]} | {"`"+p["code"][0]+"`" if p["code"] else "no code"} | [PNG](projects/{p["slug"]}/card.png) · [PDF](projects/{p["slug"]}/card.pdf) | [PDF](projects/{p["slug"]}/templates.pdf) ({NS[p["slug"]]} sheets) |\n' for p in P)
open(f'{OUT}/README.md','w').write(f'''# Robotics Projects for Kids 🤖

Hands-on robotics projects for ages 6–12 from [@Kids.JoinDev](https://www.youtube.com/@Kids.JoinDev) ([playlist](https://www.youtube.com/playlist?list=PLeEznjsWgvDM)). Cheap, safe parts: cardboard, straws, syringes, a micro:bit or an Arduino. **Always build with a grown-up.**

Website: https://dev-repos.github.io/kids-robotics-projects/

Every topic lives in its own folder under `projects/` with a guide (`README.md`: goal, parts, steps, safety, how it works, coding piece), any code, and a printable A4 build-steps card (`card.png` 2480×3508 @ 300 dpi, `card.pdf`), and **1:1 scale cut/fold templates** (`templates.pdf` at true A4 210×297 mm — the preferred print file — plus `template-N.png` at 300 dpi, 1 mm = 11.811 px, and `template-N.svg`). Print templates at **100% / Actual size, do not fit to page**, and check the 100 mm calibration bar. New topics are added to this same repo.

| # | Project | Ages | Code | Build sheet | 1:1 templates |
|---|---------|------|------|-------------|---------------|
{lst}
## Licence

- Code (`*.ino`, `*.py`, `build` scripts): MIT
- Guides, build cards and pictures: CC BY 4.0

See [LICENSE](LICENSE).
''')
open(f'{OUT}/LICENSE','w').write('''This repository uses two licences.

1) CODE (all .ino, .py, .html templates and build scripts) - MIT License

Copyright (c) 2026 Kids.JoinDev (Mohammed Siddick)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

2) DOCUMENTS (README/guide markdown, build cards PNG/PDF, drawings) - Creative Commons Attribution 4.0 International (CC BY 4.0)
https://creativecommons.org/licenses/by/4.0/
Attribution: "Kids.JoinDev - Robotics Projects for Kids"
''')
os.makedirs(f'{OUT}/tools',exist_ok=True); shutil.copy('build.py',f'{OUT}/tools/build.py'); shutil.copy('data.py',f'{OUT}/tools/data.py'); shutil.copy('templates.py',f'{OUT}/tools/templates.py')
open(f'{OUT}/.nojekyll','w').write('')
print("done")

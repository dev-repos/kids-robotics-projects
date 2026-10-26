import html,os,shutil,math
src=open('templates.py').read().split('from playwright')[0].split('T={')[0]+open('templates.py').read().split('def ln(')[1].join(['def ln(',''])[0:0]
exec(open('templates.py').read().split('T={')[0])
exec('def ln('+open('templates.py').read().split('def ln(')[1].split('from playwright')[0])
pr=dict(slug="13-wheelbarrow-walker",title="Wheelbarrow Walker Robot",color="#8d6e3f")
D_='/workspace/kids-robotics/site/projects/13-wheelbarrow-walker'; os.makedirs(D_,exist_ok=True)
def hole(cx,cy,d,lab=True):
    s=f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{d/2}" fill="#ddd" stroke="#111" stroke-width=".4"/>'+ln(cx-d/2-2,cy,cx+d/2+2,cy,w=.2)+ln(cx,cy-d/2-2,cx,cy+d/2+2,w=.2)
    return s+(tx(cx,cy+d/2+3,f"Ø{d:g}",2.2) if lab else '')
def poly(pts,fill="#fff",w=.5): return f'<path d="M'+' L'.join(f'{a:.2f},{b:.2f}' for a,b in pts)+f' Z" fill="{fill}" stroke="#111" stroke-width="{w}"/>'
def rect(x,y,w,h,fill="#fff"): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="#111" stroke-width=".5"/>'
def tab(x1,y1,x2,y2,out):  # tab outward along edge, out=(nx,ny) unit*8
    nx,ny=out; L=math.hypot(x2-x1,y2-y1); ux,uy=(x2-x1)/L,(y2-y1)/L; c=3
    p=[(x1,y1),(x1+nx+ux*c,y1+ny+uy*c),(x2+nx-ux*c,y2+ny-uy*c),(x2,y2)]
    s=poly(p,fill="#f4f4f4",w=.4)+ln(x1,y1,x2,y2,True,c="#06c")
    return s+tx((x1+x2)/2+nx/2,(y1+y2)/2+ny/2+1,"glue",2.2,c="#555")
def lab(x,y,t): return tx(x,y,t,2.8,b=True)
# ---------- sheet 1
s1=''
x,y=26,56  # base 90x60 with tabs all round
s1+=tab(x,y,x+90,y,(0,-8))+tab(x+90,y+60,x,y+60,(0,8))+tab(x,y+60,x,y,(-8,0))+tab(x+90,y,x+90,y+60,(8,0))
s1+=f'<rect x="{x}" y="{y}" width="90" height="60" fill="#fff" stroke="none"/>'+ln(x,y,x+90,y,True,c="#06c")+ln(x,y+60,x+90,y+60,True,c="#06c")+ln(x,y,x,y+60,True,c="#06c")+ln(x+90,y,x+90,y+60,True,c="#06c")
s1+=tx(x+45,y+32,"BASE",4,b=True)+tx(x+45,y+38,"tabs fold up, glue walls on",2.4)
s1+=dim(x,y+6,x+90,y+6,"90 mm")+dim(x+6,y,x+6,y+60,"60 mm",vert=True)+dim(x+90,y-11,x+98,y-11,"8")
s1+=lab(x+45,y+75,"Barrow base 90x60 + 8 mm glue tabs")
for i,hy in enumerate((44,80)):  # axle hangers 30x15
    hx=150; s1+=rect(hx,hy,30,15)+hole(hx+15,hy+15-8,4,False)+tx(hx+38,hy+8,"Ø4",2.4,"start")+dim(hx,hy-2.5,hx+30,hy-2.5,"30 mm")+dim(hx-3,hy,hx-3,hy+15,"15",vert=True)
    s1+=dim(hx+24,hy+7,hx+24,hy+15,"8",vert=True)+lab(hx+15,hy+20,f"Axle hanger {i+1}")
s1+=tx(165,112,"hole 8 mm up from bottom edge",2.4)
y=140
for i,x in enumerate((20,112)):   # trapezoid side walls top 90 bottom 70 h40
    s1+=poly([(x,y),(x+90,y),(x+80,y+40),(x+10,y+40)])+dim(x,y-3,x+90,y-3,"top 90 mm")+dim(x+10,y+36,x+80,y+36,"bottom 70 mm")+dim(x+45,y,x+45,y+40,"40 mm",vert=True)
    s1+=tx(x+22,y+18,"SIDE",3.5,b=True)+lab(x+45,y+45,f"Side wall {i+1} (trapezoid)")
y=200  # back wall 60x40 with side tabs + bottom tab
x=26; s1+=tab(x,y+40,x,y,(-8,0))+tab(x+60,y,x+60,y+40,(8,0))+rect(x,y,60,40)+ln(x,y,x,y+40,True,c="#06c")+ln(x+60,y,x+60,y+40,True,c="#06c")
s1+=dim(x,y-3,x+60,y-3,"60 mm")+dim(x+12,y,x+12,y+40,"40 mm",vert=True)+tx(x+35,y+22,"BACK",3.5,b=True)+lab(x+30,y+45,"Back wall 60x40 + tabs")
x=118; s1+=tab(x,y+45,x,y,(-8,0))+tab(x+70,y,x+70,y+45,(8,0))+rect(x,y,70,45)+ln(x,y,x,y+45,True,c="#06c")+ln(x+70,y,x+70,y+45,True,c="#06c")
s1+=dim(x,y-3,x+70,y-3,"70 mm")+dim(x+12,y,x+12,y+45,"45 mm",vert=True)+tx(x+40,y+22,"FRONT",3.5,b=True)+tx(x+40,y+28,"(sloped flap)",2.4)+lab(x+35,y+50,"Front flap 70x45 + tabs")
s1+=tx(105,40,"3 mm corrugated cardboard · grown-up cuts with craft knife",2.8,c="#555")
# ---------- sheet 2 sticks
s2=tx(105,40,"Lay an ice-cream stick (114x10) on each guide, mark the cut at the red line, grown-up cuts.",2.6,c="#555")
S=[("Thigh",45,2),("Shin",50,2),("Upper arm",35,2),("Forearm",40,2),("Hip bar",30,1),("Crank link",25,2),("Handle (full stick)",114,2)]
y=50;X=50
for n,L,q in S:
    s2+=f'<rect x="{X}" y="{y}" width="114" height="10" rx="5" fill="none" stroke="#999" stroke-width=".3" stroke-dasharray="1 1"/>'
    s2+=f'<rect x="{X}" y="{y}" width="{L}" height="10" rx="{5 if L==114 else 0}" fill="#f3e2c0" stroke="#111" stroke-width=".5"/>'
    if L<114: s2+=ln(X+L,y-2,X+L,y+12,w=.6,c="#c00")+tx(X+L+2,y+6,"cut",2.4,"start",c="#c00")
    s2+=ln(X,y+5,X+L,y+5,True,w=.2,c="#888")
    for hx in (X+5,X+L-5): s2+=hole(hx,y+5,3,False)
    s2+=dim(X,y-2,X+L,y-2,f"{L} mm")+dim(X+5,y+13,X+L-5,y+13,f"holes {L-10} apart")
    s2+=tx(X-4,y+4.5,n,3,"end",b=True)+tx(X-4,y+8.5,f"make x{q}",2.6,"end",c="#c00")
    y+=26
s2+=tx(X+57,y-6,"Ø3 pin holes 5 mm from each end (centre lines shown). Pin with toothpick / skewer bits so joints swing.",2.4)
y+=6
for i,fx in enumerate((50,90)):
    s2+=rect(fx,y,20,8,"#f3e2c0")+dim(fx,y-2,fx+20,y-2,"20 mm")+dim(fx-3,y,fx-3,y+8,"8",vert=True)+lab(fx+10,y+13,f"Foot {i+1}")
s2+=tx(150,y+5,"Feet: cut from stick offcuts",2.6)
# ---------- sheet 3 body etc
s3=tx(105,40,"Card or corrugated cardboard (crank discs: 3 mm corrugated, glue 2 layers each)",2.6,c="#555")
x,y=30,70  # torso net: back15? strip: side15 front30 side15 back30 + tab8; top/bottom 30x15 on front
seq=[15,30,15,30];xs=[x];[xs.append(xs[-1]+w) for w in seq]
s3+=tab(x+90,y,x+90,y+40,(8,0))
s3+=tab(x+15,y-15,x+45,y-15,(0,-8)) if False else ''
s3+=rect(x+15,y-15,30,15)+rect(x+15,y+40,30,15)+tab(x+45,y-15,x+45,y,(8,0))+tab(x+45,y+55,x+45,y+40,(8,0)) if False else ''
s3+=tab(x+15,y-15,x+45,y-15,(0,-8))+tab(x+15,y+55,x+45,y+55,(0,8))
s3+=f'<rect x="{x}" y="{y}" width="90" height="40" fill="#fff" stroke="#111" stroke-width=".5"/>'+rect(x+15,y-15,30,15)+rect(x+15,y+40,30,15)
for xx in xs[1:4]: s3+=ln(xx,y,xx,y+40,True,c="#06c")
s3+=ln(x+15,y,x+45,y,True,c="#06c")+ln(x+15,y+40,x+45,y+40,True,c="#06c")
s3+=ln(x+15,y-15,x+45,y-15,True,c="#06c")+ln(x+15,y+55,x+45,y+55,True,c="#06c")
s3+=tx(x+30,y+15,"FRONT",3.2,b=True)+tx(x+7.5,y+30,"side",2.4)+tx(x+52.5,y+30,"side",2.4)+tx(x+75,y+30,"BACK",3,b=True)+tx(x+30,y-6,"top",2.4)+tx(x+30,y+49,"bottom",2.4)
s3+=hole(x+7.5,y+7,3)+hole(x+52.5,y+7,3)+tx(x+30,y+35,"shoulder holes in sides",2.2)
s3+=dim(x+15,y+20,x+45,y+20,"30")+dim(x+87,y,x+87,y+40,"40",vert=True)+dim(x,y+38,x+15,y+38,"15")
s3+=lab(x+50,y+70,"Torso box net 30x40x15 (fold, glue tabs)")
for i,cx in enumerate((150,175)):  # crank discs Ø12
    cy=60; s3+=f'<circle cx="{cx}" cy="{cy}" r="6" fill="#fff" stroke="#111" stroke-width=".5"/>'+hole(cx,cy,4,False)+hole(cx+6-0.0-0,cy,3,False) if False else ''
    s3+=f'<circle cx="{cx}" cy="{cy}" r="6" fill="#fff" stroke="#111" stroke-width=".5"/>'
    s3+=f'<circle cx="{cx}" cy="{cy}" r="2" fill="#ddd" stroke="#111" stroke-width=".3"/><circle cx="{cx}" cy="{cy-6+1.5+0.0}" r="1.5" fill="#ddd" stroke="#111" stroke-width=".3"/>' if False else ''
    # off-centre hole 6 mm from centre would be at the rim of a Ø12 disc -> use tab lobe; draw disc with lobe
    s3+=f'<path d="M{cx},{cy-6} A6,6 0 1,0 {cx},{cy+6} L{cx+6},{cy+3.5} A3.5,3.5 0 0,0 {cx+6},{cy-3.5} Z" fill="#fff" stroke="#111" stroke-width=".5"/>'
    s3+=f'<circle cx="{cx}" cy="{cy}" r="2" fill="#ddd" stroke="#111" stroke-width=".3"/><circle cx="{cx+6}" cy="{cy}" r="1.5" fill="#ddd" stroke="#111" stroke-width=".3"/>'+ln(cx-8,cy,cx+11,cy,w=.2)+ln(cx,cy-8,cx,cy+8,w=.2)
    s3+=dim(cx-6,cy-9,cx+6,cy-9,"Ø12")+dim(cx,cy+10,cx+6,cy+10,"6")+lab(cx+1,cy+16,f"Crank disc {i+1}")
s3+=tx(163,84,"centre Ø4 (axle), Ø3 at 6 mm off-centre",2.3)+tx(163,88,"lobe keeps the Ø3 hole inside the disc",2.3,c="#555")
x,y=22,150  # motor bracket plate 90x40 with 70x22 slot
s3+=rect(x,y,90,40)+f'<rect x="{x+10}" y="{y+5}" width="70" height="22" fill="#e8e8e8" stroke="#111" stroke-width=".4"/>'+tx(x+45,y+17,"cut out slot 70x22 (TT motor)",2.4)
s3+=hole(x+36,y+33,3,False)+hole(x+54,y+33,3,False)+dim(x+36,y+37.5,x+54,y+37.5,"18 apart")+tx(x+62,y+35,"Ø3 screws",2.2,"start")
s3+=dim(x,y-3,x+90,y-3,"90 mm")+dim(x-3,y,x-3,y+40,"40",vert=True)+dim(x+10,y+5+0,x+80,y+5,"70")+dim(x+84,y+5,x+84,y+27,"22",vert=True)
s3+=lab(x+45,y+45,"TT motor bracket")
x,y=128,150; s3+=rect(x,y,58,32)+tx(x+29,y+15,"2xAA holder",3,b=True)+tx(x+29,y+21,"pad (glue under tray)",2.4)+dim(x,y-3,x+58,y-3,"58 mm")+dim(x-3,y,x-3,y+32,"32",vert=True)+lab(x+29,y+37,"Battery pad 58x32")
cx,cy=150,112; s3+=f'<circle cx="{cx}" cy="{cy}" r="16" fill="#fff" stroke="#111" stroke-width=".5"/>'+hole(cx,cy,4,False)+dim(cx-16,cy-19,cx+16,cy-19,"OD 32")+tx(cx,cy+8,"ID Ø4",2.4)+lab(cx,cy+21,"Wheel spacer ring")
cx,cy=186-6,112
cx=184; s3+=f'<circle cx="{cx}" cy="{cy}" r="20" fill="#fff" stroke="#111" stroke-width=".5"/>' if False else ''
# hat brim + handle strips
cx,cy=52,222; s3+=f'<circle cx="{cx}" cy="{cy}" r="20" fill="#fff" stroke="#111" stroke-width=".5"/>'+tx(cx,cy+1,"glue bottle cap here",2.3)+dim(cx-20,cy-23,cx+20,cy-23,"Ø40")+lab(cx,cy+25,"Hat brim")
for i,hy in enumerate((208,232)):
    hx=80; s3+=rect(hx,hy,120,10)+dim(hx,hy-2,hx+120,hy-2,"120 mm")+tx(hx+60,hy+6.5,f"Handle strip {i+1} (optional, wraps stick handle) — 10 mm",2.4)
s3+=tx(140,252,"optional handle strips 120x10",2.6,b=True)
# ---------- sheet 4 build steps
def pic(i,x,y):
    g=''
    if i==1: g=poly([(x+5,y+18),(x+30,y+18),(x+27,y+28),(x+8,y+28)])+ln(x+5,y+18,x+30,y+18,True,c="#06c")+f'<path d="M{x+34},{y+8} l6,6 m0,-6 l-6,6" stroke="#c00" stroke-width=".7"/>'+tx(x+37,y+20,"cut",2.4,c="#c00")
    if i==2: g=ln(x+8,y+20,x+40,y+20,w=1.2,c="#a66")+f'<rect x="{x+15}" y="{y+18.5}" width="20" height="3" fill="#fff" stroke="#2a7" stroke-width=".5"/>'+''.join(f'<circle cx="{cx}" cy="{y+20}" r="5" fill="#e33" stroke="#111" stroke-width=".5"/><circle cx="{cx}" cy="{y+20}" r="1.5" fill="#fff"/>' for cx in (x+12,x+36))
    if i==3: g=f'<path d="M{x+20},{y+6} L{x+14},{y+18} L{x+20},{y+30} M{x+20},{y+6} L{x+27},{y+18} L{x+24},{y+30}" stroke="#c9a467" stroke-width="2.4" fill="none"/>'+''.join(f'<circle cx="{a}" cy="{b}" r="1.3" fill="#fff" stroke="#111" stroke-width=".4"/>' for a,b in ((x+20,y+6),(x+14,y+18),(x+27,y+18)))+f'<path d="M{x+30},{y+14} a6,6 0 0,1 0,8" stroke="#06c" fill="none" stroke-width=".5"/>'
    if i==4: g=ln(x+4,y+12,x+36,y+22,w=2.4,c="#c9a467")+f'<circle cx="{x+8}" cy="{y+13}" r="2.5" fill="#fc0" stroke="#111" stroke-width=".4"/>'+tx(x+20,y+30,"glue hands + hips",2.2)
    if i==5: g=f'<circle cx="{x+10}" cy="{y+20}" r="6" fill="#fff" stroke="#111" stroke-width=".5"/><circle cx="{x+14}" cy="{y+16}" r="1.2" fill="#c00"/>'+ln(x+14,y+16,x+32,y+8,w=1.8,c="#c9a467")+f'<circle cx="{x+32}" cy="{y+8}" r="1.3" fill="#fff" stroke="#111" stroke-width=".4"/>'+tx(x+26,y+27,"25 mm link",2.2)
    if i==6: g=f'<rect x="{x+4}" y="{y+12}" width="16" height="9" fill="#fc0" stroke="#111" stroke-width=".5"/><rect x="{x+24}" y="{y+10}" width="12" height="14" fill="#2a7" stroke="#111" stroke-width=".5"/>'+tx(x+30,y+19,"AA",2.4,c="#fff")+tx(x+12,y+18,"TT",2.4)+tx(x+20,y+31,"or push!",2.4,c="#c00")
    if i==7: g=f'<circle cx="{x+20}" cy="{y+20}" r="8" fill="#fff" stroke="#111" stroke-width=".5"/><ellipse cx="{x+20}" cy="{y+12}" rx="11" ry="2" fill="#36c"/><rect x="{x+15}" y="{y+6}" width="10" height="5" fill="#36c"/><circle cx="{x+17}" cy="{y+19}" r=".9"/><circle cx="{x+23}" cy="{y+19}" r=".9"/><path d="M{x+16},{y+23} q4,3 8,0" stroke="#111" fill="none" stroke-width=".4"/>'
    return g
ST=["Cut and fold the barrow tray (sheet 1). Glue tabs inside.","Push skewer axle through a paper straw; glue a bottle-cap wheel on each end.","Pin thigh+shin and upper arm+forearm with Ø3 pins so they swing.","Glue the hands to the handles and the hip bar to the barrow frame.","Join the axle crank (off-centre Ø3 hole) to the knee with the 25 mm link.","Add TT motor + 2xAA + slide switch — or skip it for push mode.","Add ping-pong ball head and bottle-cap hat. Test, then tune the link."]
def wrap(t,n=34):
    out,cur=[],''
    for w in t.split():
        if len(cur)+len(w)+1>n: out.append(cur);cur=w
        else: cur=(cur+' '+w).strip()
    return out+[cur]
s4=''
for k,t in enumerate(ST):
    col,row=k%2,k//2; x=12+col*95; y=40+row*36
    s4+=f'<rect x="{x}" y="{y}" width="91" height="33" rx="3" fill="#fffdf6" stroke="#222" stroke-width=".5"/><circle cx="{x+6}" cy="{y+6}" r="4" fill="{pr["color"]}" stroke="#222" stroke-width=".4"/>'+tx(x+6,y+7.4,str(k+1),4,c="#fff",b=True)
    s4+=pic(k+1,x+50,y+(6 if k==1 else 0))
    for j,l in enumerate(wrap(t,24)): s4+=tx(x+12,y+8+j*4.2,l,3,"start")
# how it walks (cell 8)
x,y=107,148; s4+=f'<rect x="{x}" y="{y}" width="91" height="33" rx="3" fill="#eef6ff" stroke="#222" stroke-width=".5"/>'+tx(x+4,y+6,"How it walks",3.6,"start",b=True,c=pr["color"])
cx,cy=x+22,y+21; s4+=f'<circle cx="{cx}" cy="{cy}" r="7" fill="#fff" stroke="#111" stroke-width=".5"/><circle cx="{cx}" cy="{cy}" r="4" fill="none" stroke="#c00" stroke-width=".3" stroke-dasharray="1 .7"/><circle cx="{cx}" cy="{cy}" r="1" fill="#111"/><circle cx="{cx+3}" cy="{cy-3}" r="1.2" fill="#c00"/>'
s4+=ln(cx+3,cy-3,x+50,y+12,w=1.6,c="#c9a467")+f'<circle cx="{x+50}" cy="{y+12}" r="1.2" fill="#fff" stroke="#111" stroke-width=".4"/>'+f'<path d="M{x+44},{y+6} L{x+50},{y+12} L{x+46},{y+28}" stroke="#c9a467" stroke-width="2" fill="none"/>'
s4+=f'<path d="M{cx-9},{cy-4} a9,9 0 0,1 8,-6" stroke="#06c" fill="none" stroke-width=".5"/>'+tx(cx,cy+11,"axle crank",2.2)
for j,l in enumerate(["Wheel turns → off-centre","pin goes round → link","pushes knee back & forth","→ legs step!"]): s4+=tx(x+56,y+13+j*4,l,2.4,"start")
# checklist + safety
y=186; s4+=f'<rect x="12" y="{y}" width="110" height="64" rx="3" fill="#fff" stroke="#222" stroke-width=".5"/>'+tx(16,y+6,"Parts checklist",3.6,"start",b=True,c=pr["color"])
PL=["3 mm cardboard","~12 ice-cream sticks","2 bottle caps or 65 mm wheels","Skewer / 3 mm rod","Paper straw","TT gear motor","2xAA holder","Slide switch","Ping-pong ball","Bottle cap (hat)","Hot glue (by a grown-up)"]
for j,t in enumerate(PL):
    cxx=16+(j//6)*54; yy=y+11+(j%6)*8.5
    s4+=f'<rect x="{cxx}" y="{yy}" width="4" height="4" fill="#fff" stroke="#222" stroke-width=".4"/>'+tx(cxx+6,yy+3.4,t,2.7,"start")
s4+=f'<rect x="126" y="{y}" width="72" height="64" rx="3" fill="#fff3cd" stroke="#222" stroke-width=".5"/>'+tx(130,y+6,"Safety first!",3.6,"start",b=True,c="#c00")
SF=["A grown-up uses the hot glue gun.","A grown-up does all craft-knife","cutting and poking holes.","Skewer tips are sharp: snip them.","Batteries: put them in the right","way round, never short the wires,","take them out when finished.","Keep small parts from little kids."]
for j,l in enumerate(SF): s4+=tx(130,y+13+j*6,("• " if not l[0].islower() and j not in (2,5,6) else "  ")+l,2.6,"start")
bodies=[sheet(pr,[],i+1,4).replace('</svg>','') for i in range(4)]
bodies=[b+e for b,e in zip(bodies,[s1,s2,s3,s4])]
from playwright.sync_api import sync_playwright
from PIL import Image
import numpy as np
with sync_playwright() as pw:
    b=pw.chromium.launch(executable_path="/usr/bin/google-chrome");pg=b.new_page(viewport={"width":2480,"height":3508})
    for i,bd in enumerate(bodies,1):
        pg.set_content(f'<html><body style="margin:0"><svg xmlns="http://www.w3.org/2000/svg" width="2480" height="3508" viewBox="0 0 210 297">{bd}</svg></body></html>')
        f=f'{D_}/template-{i}.png';pg.screenshot(path=f,clip={"x":0,"y":0,"width":2480,"height":3508});Image.open(f).convert("RGB").save(f,dpi=(300,300))
        open(f'{D_}/template-{i}.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" viewBox="0 0 210 297">{bd}</svg>')
        a=np.array(Image.open(f).convert('L'));row=a[int(267*11.811)];d=np.where(row<60)[0];d=d[(d>118)&(d<1417)];print(i,"bar px",d.max()-d.min()+1)
    def pdf(bs,out):
        pg.set_content('<html><head><style>@page{size:210mm 297mm;margin:0}body{margin:0}svg{display:block;page-break-after:always}</style></head><body>'+''.join(f'<svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" viewBox="0 0 210 297">{x}</svg>' for x in bs)+'</body></html>')
        pg.pdf(path=out,width="210mm",height="297mm",print_background=True)
    pdf(bodies,f'{D_}/templates.pdf'); pdf(bodies[3:],f'{D_}/card.pdf')
    b.close()
shutil.copy(f'{D_}/template-4.png',f'{D_}/card.png')

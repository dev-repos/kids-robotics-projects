# 1:1 cut/fold templates. All geometry in mm; SVG viewBox = 210x297 mm.
import os, html
from data import P
R=lambda w,h,**k: dict(k=('rect'),w=w,h=h,**k)
D=lambda d,**k: dict(k='disc',w=d,h=d,d=d,**k)
def cube(s,**k): return dict(k='cube',w=4*s+10,h=3*s,s=s,**k)
HAND=dict(k='hand',w=95,h=170)
T={
"01-cardboard-robot-buddy":[cube(42,name="Head (cube net, card)"),R(100,70,name="Face plate",holes=[(30,32,22),(70,32,22)],note="eye holes for bottle caps"),R(80,60,name="Control panel (tummy)",win=[(10,10,25,15)],holes=[(55,18,12),(65,42,10),(20,45,10)]),R(30,110,name="Arm A",folds=[('h',55)]),R(30,110,name="Arm B",folds=[('h',55)]),R(40,40,name="Foot",folds=[('h',10)]),R(40,40,name="Foot",folds=[('h',10)])],
"02-bristlebot":[R(55,25,name="Bristlebot shell (fold over brush)",folds=[('v',15),('v',40)]),R(20,12,name="Motor pad"),D(20,name="CR2032 size check",hole=None,note="battery = 20 mm"),R(60,30,name="Race lane ruler",ticks=True),R(150,40,name="Racing track start line",folds=[]),R(30,30,name="Fence block",folds=[('h',10),('h',20)])],
"03-scribble-bot":[D(90,name="Top lid",hole=6),D(30,name="Off-centre weight",hole=2.5,offset=9),R(60,30,name="Motor strap",folds=[('h',10),('h',20)]),R(20,80,name="Pen holder strip",holes=[(10,15,11),(10,65,11)],note="Ø11 fits most markers"),R(20,80,name="Pen holder strip",holes=[(10,15,11),(10,65,11)]),R(20,80,name="Pen holder strip",holes=[(10,15,11),(10,65,11)])],
"04-hydraulic-robot-arm":[R(80,80,name="Base plate",holes=[(40,40,5)]),R(25,120,name="Tower",holes=[(12.5,10,4),(12.5,110,4)],folds=[('h',20)]),R(20,130,name="Lower arm",holes=[(10,10,4),(10,120,4),(10,65,4)]),R(20,110,name="Upper arm",holes=[(10,10,4),(10,100,4)]),R(20,60,name="Claw jaw A",holes=[(10,10,4)]),R(20,60,name="Claw jaw B",holes=[(10,10,4)]),R(45,30,name="Syringe clamp",folds=[('h',10),('h',20)],holes=[(22.5,15,15)],note="Ø15 for 10 ml syringe"),R(45,30,name="Syringe clamp",folds=[('h',10),('h',20)],holes=[(22.5,15,15)])],
"05-straw-robot-hand":[HAND,R(15,60,name="Straw cutting gauge",ticks=True,note="cut straws 15 mm"),R(95,30,name="Wrist cuff",folds=[('v',20),('v',75)])],
"06-paper-circuit-robot-face":[R(150,110,name="Robot face card (fold in half)",folds=[('v',75)],holes=[(30,40,5),(55,40,5)],circuit=True),D(20,name="Coin battery spot",note="CR2032 Ø20")],
"07-touch-sensor-robot":[R(50,50,name="Switch plate A (foil side in)"),R(50,50,name="Switch plate B (foil side in)"),R(50,50,name="Sponge spacer",holes=[(25,25,25)]),R(90,60,name="Tummy panel",win=[(20,5,50,50)],note="switch shows through")],
"08-microbit-robot-pet":[R(110,90,name="Pet face panel",win=[(29,24,52,42)],holes=[(15,45,8),(95,45,8)],note="window = micro:bit 52x42"),R(110,60,name="Pet side panel",folds=[('h',10)]),R(110,60,name="Pet side panel",folds=[('h',10)]),D(40,name="Ear"),D(40,name="Ear")],
"09-microbit-night-light-robot":[R(110,90,name="Head front",win=[(29,24,52,42)],note="tape tracing paper behind window"),R(110,70,name="Head top",folds=[('h',10),('h',60)]),R(90,70,name="Head side",folds=[('v',10)]),R(90,70,name="Head side",folds=[('v',10)])],
"10-arduino-blink-beep-robot":[R(90,75,name="Arduino Uno mounting plate",holes=[(10+14,75-10-2.5,3.2),(10+15.3,75-10-50.7,3.2),(10+66.1,75-10-7.6,3.2),(10+66.1,75-10-35.5,3.2)],win=[(10,10,68.6,53.4)],winstyle='outline',note="Uno 68.6x53.4, M3 holes"),R(90,60,name="Eye panel",holes=[(30,25,5),(60,25,5),(45,45,12)],note="LED Ø5, buzzer Ø12")],
"11-obstacle-avoiding-robot":[R(60,30,name="Sensor mount (HC-SR04)",holes=[(17,15,16.5),(43,15,16.5)],note="eyes 26 mm apart"),R(40,40,name="Servo cradle (SG90)",win=[(8.5,13.8,23,12.4)],note="slot 23x12.4"),R(100,80,name="Head front",win=[(20,25,60,30)]),R(80,60,name="Base plate",win=[(28.5,18,23,12.4)])],
"12-line-follower-robot":[R(150,100,name="Chassis (corrugated card)",win=[(5,15,22,19),(123,15,22,19)],holes=[(75,85,12),(75,20,6),(60,50,4),(90,50,4)],note="slots for TT motors; Ø12 caster hole"),D(65,name="Wheel (spare)",hole=5.5),D(65,name="Wheel (spare)",hole=5.5),R(80,25,name="Sensor bracket",folds=[('h',10)],holes=[(20,17,4),(60,17,4)],note="sensors 40 mm apart"),R(50,30,name="Battery pack strap",folds=[('v',10),('v',40)])],
}
def ln(x1,y1,x2,y2,dash=False,w=.35,c="#111"): return f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{c}" stroke-width="{w}"{" stroke-dasharray=\"3 2\"" if dash else ""}/>'
def tx(x,y,t,s=3,a="middle",c="#111",b=False,rot=0): return f'<text x="{x:.2f}" y="{y:.2f}" font-size="{s}" text-anchor="{a}" fill="{c}" font-family="DejaVu Sans,sans-serif"{" font-weight=\"bold\"" if b else ""}{f" transform=\"rotate({rot} {x:.2f} {y:.2f})\"" if rot else ""}>{html.escape(t)}</text>'
def dim(x1,y1,x2,y2,label,vert=False):
    a='<path d="M0,0 L2,-0.8 L2,0.8 Z" fill="#c00"/>'
    s=ln(x1,y1,x2,y2,w=.25,c="#c00")
    if vert:
        s+=ln(x1-1.5,y1,x1+1.5,y1,w=.25,c="#c00")+ln(x1-1.5,y2,x1+1.5,y2,w=.25,c="#c00")+tx(x1-1.2,(y1+y2)/2,label,2.6,c="#c00",rot=-90)
    else:
        s+=ln(x1,y1-1.5,x1,y1+1.5,w=.25,c="#c00")+ln(x2,y1-1.5,x2,y1+1.5,w=.25,c="#c00")+tx((x1+x2)/2,y1-1.2,label,2.6,c="#c00")
    return s
def fmt(v): return f"{v:g} mm"
def part(p,x,y):
    w,h=p['w'],p['h'];s=''
    if p['k']=='rect':
        s+=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#fff" stroke="#111" stroke-width=".5"/>'
        for o,v in p.get('folds',[]):
            s+=ln(x,y+v,x+w,y+v,True,c="#06c") if o=='h' else ln(x+v,y,x+v,y+h,True,c="#06c")
        for (wx,wy,ww,wh) in p.get('win',[]):
            st='stroke-dasharray="1.5 1"' if p.get('winstyle')=='outline' else ''
            s+=f'<rect x="{x+wx:.2f}" y="{y+wy:.2f}" width="{ww}" height="{wh}" fill="{"none" if st else "#e8e8e8"}" stroke="#111" stroke-width=".4" {st}/>'
            if not st: s+=tx(x+wx+ww/2,y+wy+wh/2+1,f"cut out {ww:g}x{wh:g}",2.3)
            else: s+=tx(x+wx+ww/2,y+wy+wh/2+1,f"board outline {ww:g}x{wh:g}",2.3,c="#555")
        if p.get('ticks'):
            for i in range(0,int(h)+1,5): s+=ln(x,y+i,x+(6 if i%15==0 else 3),y+i,w=.25)
        if p.get('circuit'):
            s+=f'<path d="M{x+28},{y+40} V{y+80} H{x+70} M{x+57},{y+40} V{y+70} H{x+62}" fill="none" stroke="#c87533" stroke-width="3" opacity=".6"/>'+tx(x+40,y+90,"copper tape paths: + and -",2.5,c="#a0522d")
    elif p['k']=='disc':
        r=p['d']/2;s+=f'<circle cx="{x+r}" cy="{y+r}" r="{r}" fill="#fff" stroke="#111" stroke-width=".5"/>'
        if p.get('hole'):
            cx=x+r+p.get('offset',0); s+=f'<circle cx="{cx}" cy="{y+r}" r="{p["hole"]/2}" fill="#ddd" stroke="#111" stroke-width=".4"/>'+ln(cx-3,y+r,cx+3,y+r,w=.2)+ln(cx,y+r-3,cx,y+r+3,w=.2)
            s+=tx(cx,y+r+p['hole']/2+3.5,f"hole Ø{p['hole']:g}",2.3)
    elif p['k']=='cube':
        a=p['s']
        faces=[(0,a),(a,a),(2*a,a),(3*a,a),(a,0),(a,2*a)]
        out=f'M{x},{y+a} H{x+a} V{y} H{x+2*a} V{y+a} H{x+4*a} L{x+4*a+10},{y+a+5} V{y+2*a-5} L{x+4*a},{y+2*a} H{x+2*a} V{y+3*a} H{x+a} V{y+2*a} H{x} Z'
        s+=f'<path d="{out}" fill="#fff" stroke="#111" stroke-width=".5"/>'
        s+=ln(x+a,y+a,x+a,y+2*a,True,c="#06c")+ln(x+2*a,y+a,x+2*a,y+2*a,True,c="#06c")+ln(x+3*a,y+a,x+3*a,y+2*a,True,c="#06c")+ln(x+a,y+a,x+2*a,y+a,True,c="#06c")+ln(x+a,y+2*a,x+2*a,y+2*a,True,c="#06c")+ln(x+4*a,y+a,x+4*a,y+2*a,True,c="#06c")
        s+=tx(x+1.5*a,y+1.5*a,"FACE",4,b=True)+tx(x+4*a+5,y+1.5*a,"glue",2.2,rot=-90)
        s+=dim(x+a,y-3,x+2*a,y-3,fmt(a))
    elif p['k']=='hand':
        # simple 1:1 kid hand: palm + 5 fingers
        fingers=[(x+12,y+25,15,85),(x+30,y+5,15,105),(x+48,y+0,15,110),(x+66,y+10,15,100)]
        shapes=[f'<rect x="{fx}" y="{fy}" width="{fw}" height="{fh}" rx="7.5"/>' for fx,fy,fw,fh in fingers]
        shapes.append(f'<rect x="{x+10}" y="{y+95}" width="73" height="75" rx="8"/>')
        shapes.append(f'<rect x="{x+76}" y="{y+100}" width="16" height="62" rx="8" transform="rotate(-50 {x+82} {y+162})"/>')
        g=''.join(shapes)
        sx=f'<g fill="none" stroke="#111" stroke-width="1">{g}</g><g fill="#fff" stroke="none">{g}</g>'
        for fx,fy,fw,fh in fingers:
            L=95-(fy-y)
            for k in (L*0.33,L*0.66,L): sx+=ln(fx,fy+k,fx+fw,fy+k,True,c="#06c")
        s+=sx+tx(x+45,y+140,"PALM",4,b=True)+tx(x+45,y+147,"fingers 15 mm wide",2.4)
        return s+tx(x+w/2,y+h+5,"Robot hand (cut out of card)",3,b=True)
    for (hx,hy,hd) in p.get('holes',[]):
        if p['k']=='rect':
            s+=f'<circle cx="{x+hx:.2f}" cy="{y+hy:.2f}" r="{hd/2}" fill="#ddd" stroke="#111" stroke-width=".4"/>'+ln(x+hx-2,y+hy,x+hx+2,y+hy,w=.2)+ln(x+hx,y+hy-2,x+hx,y+hy+2,w=.2)+tx(x+hx,y+hy+hd/2+3,f"Ø{hd:g}",2.2)
    if p['k']!='cube':
        s+=dim(x,y-3,x+w,y-3,fmt(w))+dim(x-3,y,x-3,y+h,fmt(h),vert=True)
    label=p.get('name','')+(f" — {p['note']}" if p.get('note') else '')
    s+=tx(x+w/2,y+h+4.5,label,2.8,b=True)
    return s
def pack(parts):
    sheets=[[]];X0,Y0,X1,Y1=14,36,200,252;x,y,rowh=X0,Y0+6,0
    for p in parts:
        w,h=p['w'],p['h']+14
        if x+w>X1: x,y,rowh=X0,y+rowh+6,0
        if y+h>Y1: sheets.append([]);x,y,rowh=X0,Y0+6,0
        sheets[-1].append((p,x,y));x+=w+12;rowh=max(rowh,h)
    return sheets
def sheet(pr,items,i,n):
    s=f'<rect width="210" height="297" fill="#fff"/><rect x="6" y="6" width="198" height="24" rx="4" fill="{pr["color"]}"/>'
    s+=tx(10,15,f"Robotics Project #{int(pr['slug'][:2])} · Templates {i}/{n} (1:1 scale)",3.6,"start",c="#fff")+tx(10,25,pr['title'],7,"start",c="#fff",b=True)
    s+=tx(200,14,"PRINT AT 100% / ACTUAL SIZE",3.4,"end",c="#fff",b=True)+tx(200,19.5,"Do NOT 'fit to page'",3,"end",c="#fff")+tx(200,25,"Check the 100 mm ruler first!",3,"end",c="#fff")
    s+=ln(10,33,22,33)+tx(24,34,"cut (solid)",2.6,"start")+ln(50,33,62,33,True,c="#06c")+tx(64,34,"fold (dashed)",2.6,"start")+f'<circle cx="95" cy="32.2" r="1.6" fill="#ddd" stroke="#111" stroke-width=".3"/>'+tx(98,34,"hole: grown-up pokes with a pencil/awl",2.6,"start")+tx(170,34,"red = size in mm",2.6,"start",c="#c00")
    for p,x,y in items: s+=part(p,x,y)
    # calibration: 100 mm ruler + 100x10 mm bar + 20 mm square
    by=262;bx=14
    s+=f'<rect id="calbar" x="{bx}" y="{by}" width="100" height="10" fill="#000"/>'+tx(bx+50,by+6.8,"100 mm",4,c="#fff",b=True)
    for m in range(0,101): s+=ln(bx+m,by+10,bx+m,by+10+(5 if m%10==0 else 3 if m%5==0 else 1.8),w=.2)
    for m in range(0,101,10): s+=tx(bx+m,by+19,str(m//10),2.4)
    s+=f'<rect x="125" y="{by}" width="20" height="20" fill="none" stroke="#000" stroke-width=".4"/>'+tx(135,by+11.5,"20 mm",3)
    s+=tx(150,by+5,"Calibration: the black bar must measure",2.6,"start")+tx(150,by+9,"exactly 100 mm and the square 20x20 mm.",2.6,"start")+tx(150,by+13,"If not, reprint at 100% (Actual size).",2.6,"start")+tx(150,by+17,"Use card ~1 mm (cereal box) for parts.",2.6,"start")
    s+=tx(105,292,"github.com/dev-repos/kids-robotics-projects · Kids.JoinDev · CC BY 4.0 · Grown-ups do all craft-knife cutting.",2.5,c="#555")
    return s
from playwright.sync_api import sync_playwright
from PIL import Image
import numpy as np
res={}
with sync_playwright() as pw:
    b=pw.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg=b.new_page(viewport={"width":2480,"height":3508},device_scale_factor=1)
    for pr in P:
        d=f'site/projects/{pr["slug"]}';sh=pack(T[pr['slug']]);bodies=[sheet(pr,it,i+1,len(sh)) for i,it in enumerate(sh)];names=[]
        for i,bd in enumerate(bodies,1):
            pg.set_content(f'<html><body style="margin:0"><svg xmlns="http://www.w3.org/2000/svg" width="2480" height="3508" viewBox="0 0 210 297">{bd}</svg></body></html>')
            f=f'{d}/template-{i}.png';pg.screenshot(path=f,clip={"x":0,"y":0,"width":2480,"height":3508})
            Image.open(f).convert("RGB").save(f,dpi=(300,300));names.append(f)
            open(f'{d}/template-{i}.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" viewBox="0 0 210 297">{bd}</svg>')
        pg.set_content('<html><head><style>@page{size:210mm 297mm;margin:0}body{margin:0}svg{display:block;page-break-after:always}</style></head><body>'+''.join(f'<svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" viewBox="0 0 210 297">{bd}</svg>' for bd in bodies)+'</body></html>')
        pg.pdf(path=f'{d}/templates.pdf',width="210mm",height="297mm",print_background=True)
        res[pr['slug']]=len(bodies)
        # verify scale on first sheet: measure black bar width
        a=np.array(Image.open(names[0]).convert('L'));row=a[int(267*11.811)];dark=np.where(row<60)[0]
        dark=dark[(dark>int(10*11.811))&(dark<int(120*11.811))]
        print(pr['slug'],len(bodies),"sheets; bar px",dark.max()-dark.min()+1,"expected",round(100*2480/210))
    b.close()
import json;json.dump(res,open('sheets.json','w'))

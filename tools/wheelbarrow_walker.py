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
s1=s1.replace('Barrow base 90x60 + 8 mm glue tabs','Barrow base 90x60 + 8 mm glue tabs (wheels roll freely)')
# ---------- SWING LEGS (pendulum, after ref #31): hip peg 30 above shaft, crank R=8 roller in leg slot, foot 105 below hip
R,HH,LF=8,26,88; SL0,SL1,SW=13,39,5.5   # slot centreline 13..39 mm below hip, 5.5 wide (straw roller Ø5); foot sole 88 below hip
def leg(th):  # math coords, shaft (0,0); returns pin P, hip H, foot F, angle
    P=(R*math.cos(th),R*math.sin(th)); a=math.atan2(P[0],HH-P[1])
    return P,(0,HH),(LF*math.sin(a),HH-LF*math.cos(a)),a
PATH=[leg(math.radians(i/2))[2] for i in range(720)]
SWEEP=max(p[0] for p in PATH)-min(p[0] for p in PATH); RISE=max(p[1] for p in PATH)-min(p[1] for p in PATH)
DS=[math.hypot(*leg(math.radians(i/2))[0]) for i in range(1)]
DMIN=min(math.hypot(leg(math.radians(i/2))[0][0],leg(math.radians(i/2))[0][1]-HH) for i in range(720))
DMAX=max(math.hypot(leg(math.radians(i/2))[0][0],leg(math.radians(i/2))[0][1]-HH) for i in range(720))
AMAX=max(abs(math.degrees(leg(math.radians(i/2))[3])) for i in range(720))
print("sweep %.1f rise %.1f pin-to-hip %.1f..%.1f; slot centreline %d..%d (ends rounded, total %.1f..%.1f); pin-centre margin %.1f/%.1f; swing +-%.1f deg"%(SWEEP,RISE,DMIN,DMAX,SL0,SL1,SL0-SW/2,SL1+SW/2,DMIN-SL0,SL1-DMAX,AMAX))
STICK="#c9a467"
TOE,HEEL,FT=42,12,8   # long foot: sole runs 42 mm forward, 12 mm back of the hip line, 8 mm deep
LEGPTS=[(9,0),(10,38),(17,56),(8,LF-FT),(TOE-3,LF-FT),(TOE,LF-FT+3),(TOE,LF),(-HEEL,LF),(-HEEL,LF-FT),(-6,LF-FT),(2,60),(-9,40),(-9,0)]
def legshape(ox,oy,ang=0,fill="#fff",w=.5,full=True,stick=False,mir=1):
    # local coords: hip (0,0), x forward, y down. Bent leg: thigh with slot, forward knee, shin back under hip, long L-foot forward
    c,s=math.cos(ang),math.sin(ang); T=lambda p:(ox+mir*p[0]*c-p[1]*s,oy+mir*p[0]*s+p[1]*c)
    P=[T(p) for p in LEGPTS]; e=T((-9,0)); b=T((9,0))
    g=f'<path d="M{P[0][0]:.2f},{P[0][1]:.2f} '+' '.join(f'L{x:.2f},{y:.2f}' for x,y in P[1:])+f' A9,9 0 0,{1 if mir>0 else 0} {b[0]:.2f},{b[1]:.2f} Z" fill="{fill}" stroke="#111" stroke-width="{w}"/>'
    if stick:
        q=[T(p) for p in ((3,-3),(9.5,-3),(16.5,55),(10,56))]
        g+='<path d="M'+' L'.join(f'{x:.2f},{y:.2f}' for x,y in q)+' Z" fill="#a8d8a0" stroke="#111" stroke-width=".3"/>'
    if full:
        a,b=T((0,SL0)),T((0,SL1))
        g+=f'<line x1="{a[0]:.2f}" y1="{a[1]:.2f}" x2="{b[0]:.2f}" y2="{b[1]:.2f}" stroke="#111" stroke-width="{SW}" stroke-linecap="round"/><line x1="{a[0]:.2f}" y1="{a[1]:.2f}" x2="{b[0]:.2f}" y2="{b[1]:.2f}" stroke="#ddd" stroke-width="{SW-.8}" stroke-linecap="round"/>'
        h=T((0,0)); g+=f'<circle cx="{h[0]:.2f}" cy="{h[1]:.2f}" r="2.75" fill="#ddd" stroke="#111" stroke-width=".4"/>'
    return g
# ---------- sheet 2: legs + feet + skewer/straw guide
s2=tx(105,40,"3 mm corrugated cardboard. Trace and cut each leg TWICE, glue the two layers = one strong 6 mm leg.",2.6,c="#555")
oy=58
for i,(lx,m,nm) in enumerate(((40,1,"LEFT leg (cut 2)"),(150,-1,"RIGHT leg (cut 2, mirror)"))):
    s2+=legshape(lx,oy,mir=m)+tx(lx,oy+LF+7,nm,2.8,b=True)+tx(lx+m*16,oy+2,"HIP Ø5.5",2.2,"start" if m>0 else "end",b=True)
    s2+=f'<path d="M{lx+m*3},{oy-3} L{lx+m*9.5},{oy-3} L{lx+m*16.5},{oy+55} L{lx+m*10},{oy+56} Z" fill="none" stroke="#2a7" stroke-width=".35" stroke-dasharray="1 .8"/>'
    s2+=tx(lx+m*30,oy+75,"walks this way",2.2,c="#06c")+f'<path d="M{lx+m*22},{oy+78} l{m*14},0 l{-m*2},-1.2 m{m*2},1.2 l{-m*2},1.2" stroke="#06c" stroke-width=".4" fill="none"/>'
lx=40
s2+=dim(lx-9,oy-11,lx+9,oy-11,"18")+dim(lx-14,oy,lx-14,oy+SL0,f"{SL0}",vert=True)+dim(lx-14,oy+SL0,lx-14,oy+SL1,f"slot {SL1-SL0}",vert=True)+dim(lx-22,oy,lx-22,oy+LF,f"hip to sole {LF} mm",vert=True)
s2+=dim(lx-HEEL,oy+LF+2,lx+TOE,oy+LF+2,f"foot {TOE+HEEL} mm")+dim(lx+TOE+3,oy+LF-FT,lx+TOE+3,oy+LF,f"{FT}",vert=True)+dim(lx,oy+56,lx+17,oy+56,"knee 17")
s2+=tx(lx+13,oy+26,f"slot {SW} wide",2.2,"start",c="#c00")+tx(lx+22,oy+30,"green dashes = glue",2.2,"start",c="#2a7")+tx(lx+22,oy+33.5,"the pale link stick",2.2,"start",c="#2a7")
s2+=tx(105,oy+120,"Hip hole, slot and sole must stay on one straight line (the centre line) - that is what makes the foot glide flat.",2.4,c="#c00")
y=190; s2+=tx(14,y,"Sole sticks x2 (ice-cream stick, cut)",3,"start",b=True)
for i in range(2):
    fx=14; yy=y+5+i*14; s2+=rect(fx,yy,TOE+HEEL,10,"#f3e2c0")+dim(fx,yy-1.5,fx+TOE+HEEL,yy-1.5,f"{TOE+HEEL} mm")+dim(fx-3,yy,fx-3,yy+10,"10",vert=True)+tx(fx+27,yy+6.5,f"Sole {i+1}",2.6,b=True)
s2+=tx(14,y+36,"Glue a sole stick under each long foot (toe forward).",2.4,"start")+tx(14,y+40,"GRIP: 2 rubber bands round each foot -",2.4,"start",c="#c00")+tx(14,y+44,"the swinging foot pushes, so it must not slide.",2.4,"start",c="#c00")
sx,sy=112,y; s2+=tx(sx,sy,"Skewer Ø3 + straw Ø5 - true length:",3,"start",b=True)
SK=[("Hip peg (skewer)",22,2,"#e9c98f"),("Crank pin (skewer)",18,2,"#e9c98f"),("Hip sleeve (straw)",8,2,"#bfe3ff"),("Roller (straw)",6,2,"#bfe3ff"),("Spacer (straw)",5,2,"#bfe3ff")]
yy=sy+8
for n,L,q,c in SK:
    hgt=3 if c=="#e9c98f" else 5
    s2+=f'<rect x="{sx}" y="{yy-hgt/2}" width="{L}" height="{hgt}" fill="{c}" stroke="#111" stroke-width=".4"/>'+dim(sx,yy-hgt/2-1.5,sx+L,yy-hgt/2-1.5,f"{L}")+tx(sx+26,yy+1,f"{n} x{q}",2.5,"start",b=True)
    yy+=8.5
s2+=tx(14,y+54,"Wheel axle: skewer 110 mm (as before).  Stoppers: 4 cardboard buttons Ø10 (sheet 3) glued on pin/peg ends.",2.4,"start")
# ---------- sheet 3 hip plates + cranks + true-size motor guide
s3=tx(105,40,"3 mm cardboard. Hip plates glue on the two shaft faces of the TT motor (gearbox end DOWN).",2.6,c="#555")
def plate(ox,oy,i):  # shaft centre ox,oy; plate x[-25,25] y[-20,+40] math-up
    X0,Y0=ox-25,oy-40; g=rect(X0,Y0,50,60)
    g+=f'<rect x="{ox-9.5}" y="{oy-54}" width="19" height="66" fill="none" stroke="#06c" stroke-width=".35" stroke-dasharray="1.2 1"/>'+tx(ox+12,oy-22,"motor",2.2,"start",c="#06c")
    g+=f'<circle cx="{ox}" cy="{oy}" r="15" fill="#e8e8e8" stroke="#111" stroke-width=".5"/>'+ln(ox-17,oy,ox+17,oy,w=.2)+ln(ox,oy-17,ox,oy+17,w=.2)+tx(ox,oy+7,"cut out Ø30",2.2)
    g+=hole(ox,oy-HH,3,False)+tx(ox+4,oy-HH-3,"HIP PEG Ø3",2.3,"start",b=True)
    g+=dim(X0,Y0-2,X0+50,Y0-2,"50 mm")+dim(X0-3,Y0,X0-3,Y0+60,"60 mm",vert=True)+dim(ox+19,oy-HH,ox+19,oy,f"{HH}",vert=True)+dim(ox,oy+17.5,ox+25,oy+17.5,"25")
    g+=tx(ox,Y0+66,("Hip plate LEFT" if i==1 else "Hip plate RIGHT"),3,b=True)+tx(ox,Y0+70,"Ø30 round the shaft; blue = motor (66 long)",2.2)
    return g
s3+=plate(55,110,1)+plate(150,110,2)
s3+=tx(105,145,f"Hip peg exactly {HH} mm straight above the shaft - this sets the swing.",2.6,c="#c00")
def disc(cx,cy,flat_to_lobe):
    import math as m
    ix=(64+81-20.25)/16; iy=m.sqrt(81-ix*ix)
    g=f'<path d="M{cx+ix:.3f},{cy-iy:.3f} A9,9 0 1,0 {cx+ix:.3f},{cy+iy:.3f} A4.5,4.5 0 1,0 {cx+ix:.3f},{cy-iy:.3f} Z" fill="#fff" stroke="#111" stroke-width=".5"/>'
    fl=1.0 if flat_to_lobe else -1.0; hh=m.sqrt(2.7**2-1.0)
    g+=f'<path d="M{cx+fl},{cy-hh:.3f} A2.7,2.7 0 1,{0 if fl>0 else 1} {cx+fl},{cy+hh:.3f} Z" fill="#ddd" stroke="#111" stroke-width=".4"/>'
    g+=f'<circle cx="{cx+8}" cy="{cy}" r="1.5" fill="#ddd" stroke="#111" stroke-width=".4"/>'+ln(cx-11,cy,cx+14,cy,w=.15)+ln(cx,cy-11,cx,cy+11,w=.15)
    return g
y=160
for j,(nm,fl) in enumerate((("A",True),("A",True),("B",False),("B",False))):
    cx=24+j*30; s3+=disc(cx,y,fl)+tx(cx+2,y+15,f"Crank {nm}",2.6,b=True)
    if j in (0,2): s3+=dim(cx-9,y-11,cx+9,y-11,"Ø18")+dim(cx,y+11,cx+8,y+11,"8")
for j in range(4):
    cx=150+j*13; s3+=f'<circle cx="{cx}" cy="{y}" r="5" fill="#fff" stroke="#111" stroke-width=".5"/>'+hole(cx,y,3,False)
s3+=dim(145,y-7,155,y-7,"Ø10")+tx(170,y+10,"Button stoppers x4 (Ø3 hole)",2.4,b=True)
s3+=tx(14,y+21,"Glue A+A and B+B = two 6 mm cranks. D-hole Ø5.4, 3.7 across the flat: snug on the shaft + hot glue.",2.4,"start")
s3+=tx(14,y+25,"A has the flat on the lobe side, B away from it: same shaft = pins OPPOSITE = 180° apart.",2.4,"start",c="#c00",b=True)
# true-size motor guide (measured: 66 long incl. motor can, gearbox 38, 22 wide, shaft 12 from gearbox end, nub 5)
mx,my=40,222  # gearbox-end x, centreline y
g=f'<rect x="{mx}" y="{my-11}" width="38" height="22" rx="2" fill="#fff6c2" stroke="#111" stroke-width=".5"/>'
g+=f'<rect x="{mx+38}" y="{my-9}" width="12" height="18" fill="#fff6c2" stroke="#111" stroke-width=".4"/>'
g+=f'<path d="M{mx+50},{my-9} L{mx+60},{my-9} Q{mx+66},{my-9} {mx+66},{my} Q{mx+66},{my+9} {mx+60},{my+9} L{mx+50},{my+9} Z" fill="#eee" stroke="#111" stroke-width=".4"/>'
g+=f'<rect x="{mx-5}" y="{my-2}" width="5" height="4" fill="#fff6c2" stroke="#111" stroke-width=".4"/>'
for sgn in (-1,1): g+=f'<rect x="{mx+12-2.7}" y="{my+sgn*11-(9 if sgn<0 else 0)}" width="5.4" height="9" fill="#fff" stroke="#111" stroke-width=".4"/>'
g+=f'<circle cx="{mx+29}" cy="{my+7}" r="1.2" fill="#ddd" stroke="#111" stroke-width=".3"/><circle cx="{mx+29}" cy="{my-7}" r="1.2" fill="#ddd" stroke="#111" stroke-width=".3"/>'
g+=dim(mx,my+27,mx+66,my+27,"66 mm body")+dim(mx,my-24,mx+38,my-24,"gearbox 38")+dim(mx,my+22,mx+12,my+22,"12")+dim(mx+72,my-11,mx+72,my+11,"22",vert=True)+dim(mx+18,my+11,mx+18,my+20,"9",vert=True)+dim(mx-5,my-5,mx,my-5,"5")
g+=tx(mx+33,my+1,"TT",3,b=True,c="#998")+tx(mx+12,my-21,"D-shaft Ø5.4 (flat 3.7)",2.2,"start")
s3+=g+tx(150,212,"CHECK YOUR MOTOR",3.2,b=True,c=pr["color"])+tx(150,218,"Lay it on the drawing: body, both",2.4)+tx(150,222,"white shafts and the rear nub",2.4)+tx(150,226,"should match (± 1 mm).",2.4)+tx(150,232,"Different? Move the hip peg so it",2.4,c="#c00")+tx(150,236,f"is still {HH} mm above the shaft.",2.4,c="#c00")
# ---------- sheet 4: torso covers, pads + 1:1 swing check
s4=tx(105,40,"Torso covers, battery pad, hat - and a 1:1 side view to check your leg before gluing.",2.6,c="#555")
x,y=14,52
for i,(nm,h) in enumerate((("FRONT",60),("BACK",60))):
    xx=x+i*40; s4+=tab(xx,y+h,xx,y,(-6,0))+tab(xx+25,y,xx+25,y+h,(6,0))+rect(xx,y,25,h)+ln(xx,y,xx,y+h,True,c="#06c")+ln(xx+25,y,xx+25,y+h,True,c="#06c")
    s4+=tx(xx+12.5,y+35,nm,3,b=True)+dim(xx,y-2,xx+25,y-2,"25")+dim(xx+4,y,xx+4,y+h,f"{h} mm",vert=True)
s4+=tx(46,y+67,"Torso covers 25x60 (+6 mm tabs glue to plate edges)",2.4)
xx,yy=14,140; s4+=rect(xx,yy,25,50)+tx(xx+12.5,yy+28,"TOP",3,b=True)+dim(xx,yy-2,xx+25,yy-2,"25")+dim(xx+4,yy,xx+4,yy+50,"50 mm",vert=True)
s4+=hole(xx+12.5,yy+10,3,False)+tx(xx+12.5,yy+15,"neck Ø3",2.2)
xx,yy=46,140; s4+=rect(xx,yy,58,32)+tx(xx+29,yy+14,"2xAA holder",3,b=True)+tx(xx+29,yy+20,"pad: glue under tray",2.4)+dim(xx,yy-2,xx+58,yy-2,"58 mm")+dim(xx-3,yy,xx-3,yy+32,"32",vert=True)
cx,cy=70,198; s4+=f'<circle cx="{cx}" cy="{cy}" r="16" fill="#fff" stroke="#111" stroke-width=".5"/>'+tx(cx,cy+1,"glue bottle cap",2.3)+dim(cx-16,cy-18,cx+16,cy-18,"Ø32")+tx(cx,cy+20,"Hat brim",2.8,b=True)
cx,cy=36,232; s4+=f'<circle cx="{cx}" cy="{cy}" r="10" fill="#fff" stroke="#111" stroke-width=".5"/>'+hole(cx,cy,4,False)+dim(cx-10,cy-12,cx+10,cy-12,"Ø20")+tx(cx,cy+15,"Wheel washer x2 (Ø4)",2.4,b=True)
cx=80; s4+=f'<rect x="{cx-12}" y="{cy-5}" width="24" height="10" fill="#fff" stroke="#111" stroke-width=".5"/>'+f'<rect x="{cx-4}" y="{cy-2}" width="8" height="4" fill="#ddd" stroke="#111" stroke-width=".4"/>'+dim(cx-12,cy-7,cx+12,cy-7,"24")+tx(cx,cy+12,"Switch plate (cut 8x4 slot)",2.4,b=True)
ox,oy=158,128
s4+=f'<rect x="112" y="46" width="92" height="204" rx="3" fill="#f7fbff" stroke="#222" stroke-width=".4"/>'+tx(158,52,"1:1 SWING CHECK (side view)",3.2,b=True,c=pr["color"])+tx(158,56.5,"lay your leg on this drawing",2.4)
s4+=f'<rect x="{ox-25}" y="{oy-40}" width="50" height="60" fill="#fff" stroke="#999" stroke-width=".3"/><rect x="{ox-9.5}" y="{oy-54}" width="19" height="66" fill="#fff3a0" stroke="#999" stroke-width=".3"/>'+tx(ox,oy-44,"TT",3,c="#998")
G=oy-(HH-LF)+1
s4+=ln(114,G,202,G,w=.5,c="#555")+tx(200,G+4,"table",2.4,"end",c="#555")
s4+='<defs><clipPath id="ck"><rect x="112" y="60" width="92" height="190"/></clipPath></defs><g clip-path="url(#ck)">'
for th,col,fl in ((0,"#888","#eee"),(180,"#888","#eee"),(90,"#111","#f3e2c0")):
    P,H,F,a=leg(math.radians(th)); s4+=legshape(ox,oy-HH,-a,fill=fl,w=.4 if col=="#888" else .5,stick=col=="#111")
    s4+=f'<circle cx="{ox+P[0]:.2f}" cy="{oy-P[1]:.2f}" r="2.5" fill="#bfe3ff" stroke="{col}" stroke-width=".4"/>'
s4+='</g>'
s4+=f'<circle cx="{ox}" cy="{oy}" r="{R}" fill="none" stroke="#06c" stroke-width=".35" stroke-dasharray="1 .7"/><circle cx="{ox}" cy="{oy}" r="1" fill="#06c"/>'
s4+='<path d="M'+' L'.join(f'{ox+p[0]:.2f},{oy-p[1]+1:.2f}' for p in PATH[::4])+'" fill="none" stroke="#c00" stroke-width=".7"/>'
s4+=dim(ox-SWEEP/2,G+6,ox+SWEEP/2,G+6,f"foot sweep {SWEEP:.0f} mm")
s4+=tx(ox+14,oy+2,"shaft",2.3,"start",c="#06c")+tx(ox+5,oy-HH-2,"hip peg",2.3,"start")+dim(ox+30,oy,ox+30,G,f"{LF-HH} mm shaft to table",vert=True)+dim(ox+38,oy-HH,ox+38,oy,f"{HH}",vert=True)
s4+=tx(158,236,"Pale legs = crank pin at front / back.",2.4)+tx(158,240,f"Red = foot path: {SWEEP:.0f} mm swing, only {RISE:.0f} mm rise.",2.4,c="#c00")+tx(158,245,"Walks backwards? Swap the 2 motor wires.",2.4,b=True,c="#c00")
# ---------- sheet 5 build steps
def wrap(t,n=34):
    out,cur=[],''
    for w in t.split():
        if len(cur)+len(w)+1>n: out.append(cur);cur=w
        else: cur=(cur+' '+w).strip()
    return out+[cur]
def pic(i,x,y):
    g=''
    if i==1: g=poly([(x+5,y+14),(x+30,y+14),(x+27,y+24),(x+8,y+24)])+ln(x+5,y+14,x+30,y+14,True,c="#06c")+f'<path d="M{x+34},{y+6} l6,6 m0,-6 l-6,6" stroke="#c00" stroke-width=".7"/>'
    if i==2: g=ln(x+8,y+16,x+40,y+16,w=1.2,c="#a66")+f'<rect x="{x+15}" y="{y+14.5}" width="20" height="3" fill="#fff" stroke="#2a7" stroke-width=".5"/>'+''.join(f'<circle cx="{cx}" cy="{y+16}" r="5" fill="#e33" stroke="#111" stroke-width=".5"/><circle cx="{cx}" cy="{y+16}" r="1.5" fill="#fff"/>' for cx in (x+12,x+36))+tx(x+24,y+26,"free-rolling",2.2)
    if i==3: g=f'<rect x="{x+8}" y="{y+3}" width="22" height="24" fill="#fff" stroke="#111" stroke-width=".5"/><rect x="{x+15}" y="{y+5}" width="8" height="18" fill="#fc0" stroke="#111" stroke-width=".4"/><circle cx="{x+19}" cy="{y+21}" r="4" fill="#e8e8e8" stroke="#111" stroke-width=".4"/><circle cx="{x+19}" cy="{y+21}" r="1" fill="#111"/>'+tx(x+19,y+12,"TT",2.2)+f'<circle cx="{x+10}" cy="{y+23}" r=".9" fill="#ddd" stroke="#111" stroke-width=".3"/>'
    if i==4: g=''.join(f'<circle cx="{cx}" cy="{y+14}" r="6" fill="#fff" stroke="#111" stroke-width=".5"/><circle cx="{cx}" cy="{y+14+dy}" r="1.3" fill="{c}"/>' for cx,dy,c in ((x+12,-4.5,"#c00"),(x+30,4.5,"#06c")))+tx(x+21,y+27,"180° apart",2.4,b=True,c="#c00")
    if i==5: g=f'<rect x="{x+8}" y="{y+6}" width="26" height="4" fill="#bfe3ff" stroke="#111" stroke-width=".4"/>'+ln(x+4,y+8,x+38,y+8,w=1,c="#a66")+''.join(f'<circle cx="{cx}" cy="{y+8}" r="2.5" fill="#fff" stroke="#111" stroke-width=".4"/>' for cx in (x+4,x+38))+tx(x+21,y+16,"peg+sleeve+button",2.2)
    if i==6:
        P,H,F,a=leg(math.radians(20)); s=.24; f=lambda p:(x+22+p[0]*s,y+10-p[1]*s)
        p,h,ff=f(P),f(H),f(F)
        g=f'<circle cx="{f((0,0))[0]}" cy="{f((0,0))[1]}" r="{R*s}" fill="none" stroke="#06c" stroke-width=".3"/>'+f'<g transform=\"translate({h[0]},{h[1]}) scale({s}) translate({-h[0]},{-h[1]})\">'+legshape(h[0],h[1],-a,fill=STICK,w=1.2,stick=True).replace('stroke-width=\"5.5\"','stroke-width=\"5.5\"')+'</g>'+f'<circle cx="{p[0]:.2f}" cy="{p[1]:.2f}" r=".9" fill="#bfe3ff" stroke="#111" stroke-width=".3"/><circle cx="{h[0]:.2f}" cy="{h[1]:.2f}" r=".8" fill="#fff" stroke="#111" stroke-width=".3"/>'+tx(x+33,y+14,"roller",2,"start")+tx(x+33,y+17,"in slot",2,"start")
    if i==7: g=ln(x+4,y+10,x+38,y+22,w=2.2,c=STICK)+f'<circle cx="{x+8}" cy="{y+11.5}" r="2.5" fill="#fc0" stroke="#111" stroke-width=".4"/>'+tx(x+24,y+27,"glue hands",2.2)
    if i==8: g=f'<rect x="{x+4}" y="{y+8}" width="14" height="10" fill="#2a7" stroke="#111" stroke-width=".5"/>'+tx(x+11,y+14.5,"AA",2.4,c="#fff")+f'<rect x="{x+22}" y="{y+10}" width="8" height="5" fill="#ddd" stroke="#111" stroke-width=".4"/><rect x="{x+23}" y="{y+11}" width="3" height="3" fill="#111"/>'+tx(x+26,y+24,"ON = walk!",2.4,c="#c00",b=True)
    return g
ST=["Cut and fold the barrow tray (sheet 1). Glue the tabs inside.",
    "Skewer axle through a straw under the tray; glue a wheel on each end. Wheels roll freely.",
    "Hot-glue a hip plate (sheet 3) on each flat side of the TT motor, motor upright, shaft in the Ø30 hole.",
    "Glue crank A on one shaft end, crank B on the other: the pins must point opposite ways.",
    "Glue a 22 mm hip peg in each hip hole. Add a 5 mm straw spacer, then the leg (hip sleeve in its Ø5.5 hole).",
    "Crank pin + straw roller sits in the leg slot. Glue button stoppers on peg and pin ends.",
    "Glue torso covers, arms at the shoulders, hands onto the handles with both feet on the table.",
    "2xAA + switch under the tray, wires along a handle to the motor. Switch on and he walks!"]
s5=''
for k,t in enumerate(ST):
    col,row=k%2,k//2; x=12+col*95; y=40+row*32
    s5+=f'<rect x="{x}" y="{y}" width="91" height="30" rx="3" fill="#fffdf6" stroke="#222" stroke-width=".5"/><circle cx="{x+6}" cy="{y+6}" r="4" fill="{pr["color"]}" stroke="#222" stroke-width=".4"/>'+tx(x+6,y+7.4,str(k+1),4,c="#fff",b=True)
    s5+=pic(k+1,x+50,y+1)
    for j,l in enumerate(wrap(t,23)): s5+=tx(x+12,y+6.5+j*3.8,l,2.6,"start")
# How the legs walk (scaled 0.3: crank pin + roller in the slot, foot path red)
x,y=12,170; s5+=f'<rect x="{x}" y="{y}" width="186" height="42" rx="3" fill="#eef6ff" stroke="#222" stroke-width=".5"/>'+tx(x+4,y+6,"How the legs walk",3.6,"start",b=True,c=pr["color"])
s=.3; bx,by=x+30,y+18
f=lambda p:(bx+p[0]*s,by-p[1]*s)
s5+=f'<circle cx="{bx}" cy="{by}" r="{R*s}" fill="none" stroke="#06c" stroke-width=".3" stroke-dasharray=".6 .4"/>'
for th,col in ((0,"#06c"),(180,"#c00")):
    P,H,F,a=leg(math.radians(th)); h,p,ff=f(H),f(P),f(F)
    sl0=(h[0]+SL0*s*math.sin(a),h[1]+SL0*s*math.cos(a)); sl1=(h[0]+SL1*s*math.sin(a),h[1]+SL1*s*math.cos(a))
    s5+=f'<g transform="translate({h[0]},{h[1]}) scale({s}) translate({-h[0]},{-h[1]})" opacity="{.55 if th==0 else 1}">'+legshape(h[0],h[1],-a,fill=("#2f5d3a" if th==180 else "#5b8f68"),w=1,stick=True)+f'<circle cx="{h[0]}" cy="{h[1]}" r="6" fill="#6a5a78" stroke="#111"/><circle cx="{h[0]+P[0]}" cy="{h[1]+(HH-P[1])}" r="5" fill="#6a5a78" stroke="#111"/></g>'
    s5+=ln(bx,by,*p,w=.5,c="#111")
s5+=f'<circle cx="{bx}" cy="{by-HH*s}" r=".9" fill="#fff" stroke="#111" stroke-width=".3"/>'
s5+='<path d="M'+' L'.join(f'{f(p)[0]:.2f},{f(p)[1]+1.2:.2f}' for p in PATH[::6])+'" fill="none" stroke="#c00" stroke-width=".6"/>'
# zoomed slot detail 1:1
zx,zy=x+72,y+9; k=.55
s5+=f'<defs><clipPath id="cl"><rect x="{zx-8}" y="{zy-6}" width="16" height="31"/></clipPath></defs><g clip-path="url(#cl)"><g transform="translate({zx},{zy}) scale({k}) translate({-zx},{-zy})">'+legshape(zx,zy,0,fill="#f3e2c0",w=.6)
for dd,c_ in ((HH-R,"#06c"),(HH+R,"#c00")): s5+=f'<circle cx="{zx}" cy="{zy+dd}" r="2.5" fill="#bfe3ff" stroke="{c_}" stroke-width=".6"/>'
s5+='</g></g>'+tx(zx+7,zy+(HH-R)*k+1,"pin highest",2,"start",c="#06c")+tx(zx+7,zy+(HH+R)*k+1,"pin lowest",2,"start",c="#c00")+tx(zx+7,zy+1,"hip",2,"start")+tx(zx,zy+29,"slot (x0.55)",2)
for j,l in enumerate(["The motor turns both cranks, half a turn apart.","The crank pin (with a straw roller) slides up and","down in the leg slot and pushes the leg front","and back. The leg swings like a pendulum from","the hip peg: the foot (red) sweeps %d mm along"%round(SWEEP),"the table and rises only %d mm. One foot pushes back"%round(RISE),"while the other swings forward - and his hands","push the barrow! Roller never leaves the slot."]):
    s5+=tx(x+100,y+10+j*4,l,2.5,"start")
y=215; s5+=f'<rect x="12" y="{y}" width="112" height="44" rx="3" fill="#fff" stroke="#222" stroke-width=".5"/>'+tx(16,y+6,"Parts checklist",3.4,"start",b=True,c=pr["color"])
PL=["3 mm cardboard","3 ice-cream sticks","2 wheels (caps/65 mm)","Skewers 3 mm","Paper straw","TT motor (double shaft)","2xAA holder + batteries","Slide switch + wire","Rubber bands (feet)","Ping-pong ball + cap","Hot glue (grown-up)","Pencil, scissors"]
for j,t in enumerate(PL):
    cxx=16+(j//4)*36; yy=y+10+(j%4)*8.3
    s5+=f'<rect x="{cxx}" y="{yy}" width="3.5" height="3.5" fill="#fff" stroke="#222" stroke-width=".4"/>'+tx(cxx+5,yy+3,t,2.3,"start")
s5+=f'<rect x="127" y="{y}" width="71" height="44" rx="3" fill="#fff3cd" stroke="#222" stroke-width=".5"/>'+tx(131,y+6,"Safety first!",3.4,"start",b=True,c="#c00")
SF=["• A grown-up uses the hot glue gun,","  craft knife, and pokes the holes.","• Snip the sharp skewer tips off.","• Fingers away from the cranks when ON.","• Batteries the right way round; never","  join the wires; take them out after.","• Keep small parts from little kids."]
for j,l in enumerate(SF): s5+=tx(131,y+12+j*4.6,l,2.4,"start")
N=5
bodies=[sheet(pr,[],i+1,N).replace('</svg>','') for i in range(N)]
bodies=[b+e for b,e in zip(bodies,[s1,s2,s3,s4,s5])]
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'wheelbarrow_walker_assembly.py')).read())
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
    for i,bd in enumerate(asm,1):
        pg.set_content(f'<html><body style="margin:0"><svg xmlns="http://www.w3.org/2000/svg" width="2480" height="3508" viewBox="0 0 210 297">{bd}</svg></body></html>')
        f=f'{D_}/assembly-{i}.png';pg.screenshot(path=f,clip={"x":0,"y":0,"width":2480,"height":3508});Image.open(f).convert('RGB').save(f,dpi=(300,300))
        open(f'{D_}/assembly-{i}.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" viewBox="0 0 210 297">{bd}</svg>')
    def pdf(bs,out):
        pg.set_content('<html><head><style>@page{size:210mm 297mm;margin:0}body{margin:0}svg{display:block;page-break-after:always}</style></head><body>'+''.join(f'<svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" viewBox="0 0 210 297">{x}</svg>' for x in bs)+'</body></html>')
        pg.pdf(path=out,width="210mm",height="297mm",print_background=True)
    pdf(bodies+asm,f'{D_}/templates.pdf'); pdf(asm,f'{D_}/assembly.pdf'); pdf(bodies[4:],f'{D_}/card.pdf')
    b.close()
shutil.copy(f'{D_}/template-5.png',f'{D_}/card.png')

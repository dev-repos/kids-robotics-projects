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
# ---------- linkage (checked by geo/walk_geom.py): crank R=8, thigh 35, leg 40+40, hip 36 behind / 8 below shaft
R,T,A,FD,HX,HY=8,35,40,40,-36,-8
def leg(th):  # math coords (y up), crank centre (0,0); returns P,K,F
    P=(R*math.cos(th),R*math.sin(th)); dx,dy=HX-P[0],HY-P[1]; d=math.hypot(dx,dy)
    a=(A*A-T*T+d*d)/(2*d); h=math.sqrt(A*A-a*a); bx,by=P[0]+a*dx/d,P[1]+a*dy/d
    K1=(bx+h*dy/d,by-h*dx/d);K2=(bx-h*dy/d,by+h*dx/d);K=K1 if K1[1]<K2[1] else K2
    u=((K[0]-P[0])/A,(K[1]-P[1])/A); return P,K,(P[0]+u[0]*(A+FD),P[1]+u[1]*(A+FD))
PATH=[leg(math.radians(i))[2] for i in range(0,360,3)]
STICK="#c9a467"
# ---------- sheet 2 sticks
s2=tx(105,40,"Lay an ice-cream stick (114x10) on each guide, mark the cut at the red line, grown-up cuts.",2.6,c="#555")
S=[("Thigh",45,2,(5,40)),("Leg stick",90,2,(5,45,85)),("Upper arm",35,2,(5,30)),("Forearm",40,2,(5,35)),("Handle (full stick)",114,2,(5,109))]
y=52;X=56
for n,L,q,hs in S:
    s2+=f'<rect x="{X}" y="{y}" width="114" height="10" rx="5" fill="none" stroke="#999" stroke-width=".3" stroke-dasharray="1 1"/>'
    s2+=f'<rect x="{X}" y="{y}" width="{L}" height="10" rx="{5 if L==114 else 0}" fill="#f3e2c0" stroke="#111" stroke-width=".5"/>'
    if L<114: s2+=ln(X+L,y-2,X+L,y+12,w=.6,c="#c00")+tx(X+L+2,y+6,"cut",2.4,"start",c="#c00")
    s2+=ln(X,y+5,X+L,y+5,True,w=.2,c="#888")
    for h in hs: s2+=hole(X+h,y+5,3,False)
    s2+=dim(X,y-2,X+L,y-2,f"{L} mm")
    for a_,b_ in zip(hs,hs[1:]): s2+=dim(X+a_,y+13,X+b_,y+13,f"{b_-a_}")
    s2+=tx(X-4,y+4.5,n,3,"end",b=True)+tx(X-4,y+8.5,f"make x{q}",2.6,"end",c="#c00")
    y+=24
s2+=tx(105,y-5,"Ø3 pin holes 5 mm from the ends (leg stick: also one in the middle). Wiggle the pencil so pins turn freely.",2.4)
y+=4
s2+=tx(14,y,"Feet (from offcuts)",3,"start",b=True)
for i,fx in enumerate((14,54)):
    yy=y+5; s2+=rect(fx,yy,30,10,"#f3e2c0")+dim(fx,yy-1.5,fx+30,yy-1.5,"30 mm")+dim(fx-3,yy,fx-3,yy+10,"10",vert=True)+tx(fx+15,yy+6.5,f"Foot {i+1}",2.6,b=True)
s2+=tx(14,y+22,"Glue the bottom end of each leg stick across a foot.",2.4,"start")+tx(14,y+26,"GRIP: wrap 2 rubber bands round each foot, or zig-zag",2.4,"start",c="#c00")+tx(14,y+30,"lines of hot glue under it, so it pushes, not slides.",2.4,"start",c="#c00")
# skewer cut guide
sx,sy=112,y+2; s2+=tx(sx,sy,"Skewer (3 mm) pieces - snip, true length:",3,"start",b=True)
SK=[("Hip axle",40,1),("Crank pin",15,2),("Knee pin",12,2),("Wheel axle",110,1)]
yy=sy+7
for n,L,q in SK:
    if L>80: xx=14; yy2=y+42
    else: xx=sx; yy2=yy
    s2+=f'<rect x="{xx}" y="{yy2-1.5}" width="{L}" height="3" fill="#e9c98f" stroke="#111" stroke-width=".4"/>'+dim(xx,yy2-3,xx+L,yy2-3,f"{L} mm")+tx(xx+L+3,yy2+1,f"{n} x{q}",2.6,"start",b=True)
    if L<=80: yy+=9
s2+=tx(14,y+52,"Straw: 4 short rings (3 mm) slide on pin ends as stoppers; glue ring to pin, never to the stick.",2.4,"start")
# ---------- sheet 3 hip frame + cranks
s3=tx(105,40,"3 mm corrugated cardboard. Hip plates hold the TT motor upright in the hips; one crank on each shaft end.",2.6,c="#555")
def plate(ox,oy,i):  # ox,oy = shaft centre on sheet; plate x[-48,18] y[-20,70] (math y up)
    X0,Y0=ox-48,oy-70
    g=rect(X0,Y0,66,90)
    g+=f'<rect x="{ox-11}" y="{oy-59}" width="22" height="70" fill="none" stroke="#06c" stroke-width=".35" stroke-dasharray="1.2 1"/>'+tx(ox,oy-40,"glue",2.4,c="#06c")+tx(ox,oy-36,"TT motor",2.4,c="#06c")+tx(ox,oy-32,"face here",2.4,c="#06c")
    g+=f'<circle cx="{ox}" cy="{oy}" r="15" fill="#e8e8e8" stroke="#111" stroke-width=".5"/>'+ln(ox-17,oy,ox+17,oy,w=.2)+ln(ox,oy-17,ox,oy+17,w=.2)+tx(ox,oy+7,"cut out Ø30",2.2)+tx(ox,oy+10,"(crank turns here)",2)
    g+=hole(ox+HX,oy-HY,3,False)+tx(ox+HX,oy-HY+5,"HIP Ø3",2.3,b=True)
    g+=hole(ox-30,oy-58,3,False)+tx(ox-30,oy-62,"shoulder Ø3",2.2)
    g+=dim(X0,Y0-2,X0+66,Y0-2,"66 mm")+dim(X0-3,Y0,X0-3,Y0+90,"90 mm",vert=True)
    g+=dim(ox+HX,oy+16,ox,oy+16,"36")+dim(ox+HX+5,oy,ox+HX+5,oy-HY,"8",vert=True)+ln(ox+HX+5,oy,ox-15,oy,True,w=.15,c="#c00")
    g+=dim(ox,oy+21,ox+18,oy+21,"18")+dim(ox+15.5,oy-59,ox+15.5,oy,"shaft 59 from top",vert=True)
    g+=tx(ox-15,Y0+97,("Hip plate LEFT" if i==1 else "Hip plate RIGHT"),3,b=True)+tx(ox-15,Y0+101,("same shape - glue it flipped over (mirror)" if i==2 else "shaft through Ø30, motor upright"),2.4)
    return g
s3+=plate(66,124,1)+plate(162,124,2)
s3+=tx(105,160,"Hip hole: 36 mm behind and 8 mm below the shaft (keep exact - this sets the walk).",2.6,c="#c00")
def disc(cx,cy,flat_to_lobe):
    # union of disc r9 and lobe r4.5 centred on the pin at 8 mm; D hole Ø5.4 (3.7 across flat); pin Ø3 at 8 mm
    import math as m
    ix=(64+81-20.25)/16; iy=m.sqrt(81-ix*ix)
    g=f'<path d="M{cx+ix:.3f},{cy-iy:.3f} A9,9 0 1,0 {cx+ix:.3f},{cy+iy:.3f} A4.5,4.5 0 1,0 {cx+ix:.3f},{cy-iy:.3f} Z" fill="#fff" stroke="#111" stroke-width=".5"/>'
    fl=1.0 if flat_to_lobe else -1.0; hh=m.sqrt(2.7**2-1.0)
    g+=f'<path d="M{cx+fl},{cy-hh:.3f} A2.7,2.7 0 1,{0 if fl>0 else 1} {cx+fl},{cy+hh:.3f} Z" fill="#ddd" stroke="#111" stroke-width=".4"/>'
    g+=f'<circle cx="{cx+8}" cy="{cy}" r="1.5" fill="#ddd" stroke="#111" stroke-width=".4"/>'+ln(cx-11,cy,cx+14,cy,w=.15)+ln(cx,cy-11,cx,cy+11,w=.15)
    return g
y=184
for j,(nm,fl) in enumerate((("A",True),("A",True),("B",False),("B",False))):
    cx=30+j*42; s3+=disc(cx,y,fl)+tx(cx+2,y+16,f"Crank disc {nm}",2.8,b=True)
    if j in (0,2): s3+=dim(cx-9,y-11,cx+9,y-11,"Ø18")+dim(cx,y+11,cx+8,y+11,"8")
s3+=tx(105,y+22,"Glue the two A discs into one 6 mm crank, and the two B discs into another.",2.6)
s3+=tx(105,y+27,"Centre: D-hole Ø5.4 with flat (3.7 across) - snug on the TT shaft, then a drop of hot glue.",2.6)
s3+=tx(105,y+32,"A: flat on the lobe side. B: flat away from lobe. On the same shaft the flats line up,",2.6,c="#c00")
s3+=tx(105,y+37,"so A and B pins point OPPOSITE ways = 180° apart = left, right, left, right!",2.6,c="#c00",b=True)
s3+=tx(105,y+42,"Crank pin Ø3 at 8 mm; the lobe keeps 3 mm of card round the pin hole.",2.6)
s3+=tx(105,y+51,"TT gear motor (double shaft): body ~70 x 22 x 18 mm, 5.4 mm D-shaft out both sides (~9 mm each).",2.4,c="#555")
s3+=tx(105,y+55,"Check yours: the Ø30 hole goes round the shaft, the dashed box shows where the body sits.",2.4,c="#555")
# ---------- sheet 4: torso covers, pads + 1:1 leg check drawing
s4=tx(105,40,"Torso covers, battery pad, hat - and a 1:1 side view to check your leg before gluing.",2.6,c="#555")
x,y=14,52
for i,(nm,h) in enumerate((("FRONT",70),("BACK",70))):
    xx=x+i*40; s4+=tab(xx,y+h,xx,y,(-6,0))+tab(xx+25,y,xx+25,y+h,(6,0))+rect(xx,y,25,h)+ln(xx,y,xx,y+h,True,c="#06c")+ln(xx+25,y,xx+25,y+h,True,c="#06c")
    s4+=tx(xx+12.5,y+35,nm,3,b=True)+dim(xx,y-2,xx+25,y-2,"25")+dim(xx+4,y,xx+4,y+h,f"{h} mm",vert=True)
s4+=tx(46,y+77,"Torso covers 25x70 (+6 mm tabs glue to plate edges)",2.4)
xx,yy=14,140; s4+=rect(xx,yy,25,66)+tx(xx+12.5,yy+33,"TOP",3,b=True)+dim(xx,yy-2,xx+25,yy-2,"25")+dim(xx+4,yy,xx+4,yy+66,"66 mm",vert=True)
s4+=hole(xx+12.5,yy+10,3,False)+tx(xx+12.5,yy+15,"neck Ø3",2.2)
xx,yy=46,140; s4+=rect(xx,yy,58,32)+tx(xx+29,yy+14,"2xAA holder",3,b=True)+tx(xx+29,yy+20,"pad: glue under tray",2.4)+dim(xx,yy-2,xx+58,yy-2,"58 mm")+dim(xx-3,yy,xx-3,yy+32,"32",vert=True)
cx,cy=70,198; s4+=f'<circle cx="{cx}" cy="{cy}" r="16" fill="#fff" stroke="#111" stroke-width=".5"/>'+tx(cx,cy+1,"glue bottle cap",2.3)+dim(cx-16,cy-18,cx+16,cy-18,"Ø32")+tx(cx,cy+20,"Hat brim",2.8,b=True)
cx,cy=36,232; s4+=f'<circle cx="{cx}" cy="{cy}" r="10" fill="#fff" stroke="#111" stroke-width=".5"/>'+hole(cx,cy,4,False)+dim(cx-10,cy-12,cx+10,cy-12,"Ø20")+tx(cx,cy+15,"Wheel washer x2 (Ø4)",2.4,b=True)
cx=80; s4+=f'<rect x="{cx-12}" y="{cy-5}" width="24" height="10" fill="#fff" stroke="#111" stroke-width=".5"/>'+f'<rect x="{cx-4}" y="{cy-2}" width="8" height="4" fill="#ddd" stroke="#111" stroke-width=".4"/>'+dim(cx-12,cy-7,cx+12,cy-7,"24")+tx(cx,cy+12,"Switch plate (cut 8x4 slot)",2.4,b=True)
# 1:1 side view
ox,oy=168,138  # crank centre on sheet
s4+=f'<rect x="112" y="46" width="92" height="204" rx="3" fill="#f7fbff" stroke="#222" stroke-width=".4"/>'+tx(158,52,"1:1 LEG CHECK (side view)",3.2,b=True,c=pr["color"])+tx(158,56.5,"lay your leg on this drawing",2.4)
pl=f'<rect x="{ox-48}" y="{oy-70}" width="66" height="90" fill="#fff" stroke="#999" stroke-width=".3"/>'+f'<rect x="{ox-11}" y="{oy-59}" width="22" height="70" fill="#fff3a0" stroke="#999" stroke-width=".3"/>'+tx(ox,oy-30,"TT",3,c="#998")
s4+=pl
G=oy+77.4
s4+=ln(114,G,202,G,w=.5,c="#555")+tx(200,G+4,"table",2.4,"end",c="#555")
s4+='<path d="M'+' L'.join(f'{ox+p[0]:.2f},{oy-p[1]:.2f}' for p in PATH)+' Z" fill="none" stroke="#c00" stroke-width=".45" stroke-dasharray="1.2 .8"/>'
for th,col in ((90,"#111"),(270,"#888")):
    P,K,F=leg(math.radians(th)); f=lambda p:(ox+p[0],oy-p[1])
    p,k,ff,h=f(P),f(K),f(F),f((HX,HY))
    s4+=f'<line x1="{h[0]:.2f}" y1="{h[1]:.2f}" x2="{k[0]:.2f}" y2="{k[1]:.2f}" stroke="{STICK if col=="#111" else "#e6d3ad"}" stroke-width="3" stroke-linecap="round"/>'
    s4+=f'<line x1="{p[0]:.2f}" y1="{p[1]:.2f}" x2="{ff[0]:.2f}" y2="{ff[1]:.2f}" stroke="{STICK if col=="#111" else "#e6d3ad"}" stroke-width="3" stroke-linecap="round" opacity=".9"/>'
    for q in (p,k,h): s4+=f'<circle cx="{q[0]:.2f}" cy="{q[1]:.2f}" r="1.2" fill="#fff" stroke="{col}" stroke-width=".35"/>'
    s4+=f'<rect x="{ff[0]-15:.2f}" y="{ff[1]-1:.2f}" width="30" height="2" fill="{STICK if col=="#111" else "#e6d3ad"}" stroke="{col}" stroke-width=".3" transform="rotate(0)"/>'
s4+=f'<circle cx="{ox}" cy="{oy}" r="8" fill="none" stroke="#06c" stroke-width=".35" stroke-dasharray="1 .7"/><circle cx="{ox}" cy="{oy}" r="1" fill="#06c"/>'
s4+=tx(ox+11,oy+2,"shaft",2.3,"start",c="#06c")+tx(ox+HX-2,oy-HY+5,"hip",2.3,"end")
s4+=dim(ox+22,oy,ox+22,G,"77 mm shaft to table",vert=True)
s4+=tx(158,230,"Walks backwards? Swap the 2 motor wires.",2.4,b=True,c="#c00")+tx(158,236,"Red dashes = path of the foot: flat bit",2.4)+tx(158,240,"~22 mm on the table (the push), then",2.4)+tx(158,244,"it lifts ~9 mm and swings forward.",2.4)
s4+=tx(124,68,"walks this way",2.4,"start",c="#06c")+f'<path d="M150,70 l12,0 l-2,-1.2 m2,1.2 l-2,1.2" stroke="#06c" stroke-width=".4" fill="none"/>'
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
    if i==5: g=ln(x+6,y+8,x+36,y+8,w=1,c="#a66")+''.join(f'<path d="M{cx},{y+8} L{cx+3},{y+24}" stroke="{STICK}" stroke-width="2.4"/>' for cx in (x+8,x+33))+tx(x+21,y+5,"hip skewer",2.2)
    if i==6:
        P,K,F=leg(math.radians(60)); s=.32; f=lambda p:(x+26+p[0]*s,y+4-p[1]*s)
        p,k,ff,h=f(P),f(K),f(F),f((HX,HY))
        g=f'<circle cx="{x+26}" cy="{y+4}" r="{8*s+.6}" fill="none" stroke="#06c" stroke-width=".3"/>'+ln(*h,*k,w=1.6,c=STICK)+ln(*p,*ff,w=1.6,c=STICK)+ln(ff[0]-5,ff[1]+.5,ff[0]+5,ff[1]+.5,w=1.6,c="#555")+''.join(f'<circle cx="{q[0]:.2f}" cy="{q[1]:.2f}" r=".8" fill="#fff" stroke="#111" stroke-width=".3"/>' for q in (p,k,h))
    if i==7: g=ln(x+4,y+10,x+38,y+22,w=2.2,c=STICK)+f'<circle cx="{x+8}" cy="{y+11.5}" r="2.5" fill="#fc0" stroke="#111" stroke-width=".4"/>'+tx(x+24,y+27,"glue hands",2.2)
    if i==8: g=f'<rect x="{x+4}" y="{y+8}" width="14" height="10" fill="#2a7" stroke="#111" stroke-width=".5"/>'+tx(x+11,y+14.5,"AA",2.4,c="#fff")+f'<rect x="{x+22}" y="{y+10}" width="8" height="5" fill="#ddd" stroke="#111" stroke-width=".4"/><rect x="{x+23}" y="{y+11}" width="3" height="3" fill="#111"/>'+tx(x+26,y+24,"ON = walk!",2.4,c="#c00",b=True)
    return g
ST=["Cut and fold the barrow tray (sheet 1). Glue the tabs inside.",
    "Skewer axle through a straw under the tray; glue a wheel on each end. Wheels roll freely.",
    "Hot-glue a hip plate (sheet 3) on each flat side of the TT motor, motor upright, shaft in the Ø30 hole.",
    "Glue crank A on one shaft end, crank B on the other: the pins must point opposite ways.",
    "Push the 40 mm hip skewer through both hip holes. Put a thigh on each end, add straw stoppers.",
    "Leg stick: top hole on the crank pin, middle hole pinned to the thigh knee, foot at the bottom.",
    "Glue torso covers, arms at the shoulders, hands onto the handles with both feet on the table.",
    "2xAA + switch under the tray, wires along a handle to the motor. Switch on and he walks!"]
s5=''
for k,t in enumerate(ST):
    col,row=k%2,k//2; x=12+col*95; y=40+row*32
    s5+=f'<rect x="{x}" y="{y}" width="91" height="30" rx="3" fill="#fffdf6" stroke="#222" stroke-width=".5"/><circle cx="{x+6}" cy="{y+6}" r="4" fill="{pr["color"]}" stroke="#222" stroke-width=".4"/>'+tx(x+6,y+7.4,str(k+1),4,c="#fff",b=True)
    s5+=pic(k+1,x+50,y+1)
    for j,l in enumerate(wrap(t,23)): s5+=tx(x+12,y+6.5+j*3.8,l,2.6,"start")
# How the legs walk
x,y=12,170; s5+=f'<rect x="{x}" y="{y}" width="186" height="42" rx="3" fill="#eef6ff" stroke="#222" stroke-width=".5"/>'+tx(x+4,y+6,"How the legs walk",3.6,"start",b=True,c=pr["color"])
cx,cy=x+22,y+24; s5+=f'<circle cx="{cx}" cy="{cy}" r="11" fill="#fff" stroke="#111" stroke-width=".5"/><circle cx="{cx}" cy="{cy}" r="8" fill="none" stroke="#888" stroke-width=".3" stroke-dasharray="1 .7"/><circle cx="{cx}" cy="{cy}" r="1.3" fill="#111"/>'
s5+=ln(cx,cy,cx,cy-8,w=1,c="#c00")+ln(cx,cy,cx,cy+8,w=1,c="#06c")+f'<circle cx="{cx}" cy="{cy-8}" r="1.6" fill="#c00"/><circle cx="{cx}" cy="{cy+8}" r="1.6" fill="#06c"/>'
s5+=f'<path d="M{cx+12},{cy-6} A13,13 0 0,1 {cx+12},{cy+6}" stroke="#111" fill="none" stroke-width=".5"/><path d="M{cx+12},{cy+6} l-.4,-2.2 m.4,2.2 l2,-1" stroke="#111" fill="none" stroke-width=".5"/>'
s5+=tx(cx,cy-13,"180°",2.6,b=True,c="#c00")+tx(cx+13,cy-9,"left pin",2.2,"start",c="#c00")+tx(cx+13,cy+12,"right pin",2.2,"start",c="#06c")+tx(cx,cy+16.5,"motor shaft, r = 8 mm",2.2)
# mini legs at two phases with foot path
for j,(th,col) in enumerate(((90,"#c00"),(270,"#06c"))):
    bx,by=x+80,y+8; s=.38
    f=lambda p:(bx+p[0]*s,by-p[1]*s)
    if j==0: s5+='<path d="M'+' L'.join(f'{f(p)[0]:.2f},{f(p)[1]:.2f}' for p in PATH)+' Z" fill="none" stroke="#555" stroke-width=".3" stroke-dasharray=".8 .5"/>'
    P,K,F=leg(math.radians(th)); p,k,ff,h=f(P),f(K),f(F),f((HX,HY))
    s5+=ln(*h,*k,w=1.3,c=col)+ln(*p,*ff,w=1.3,c=col)+ln(ff[0]-4.5,ff[1]+.6,ff[0]+4.5,ff[1]+.6,w=1.3,c=col)
s5+=tx(x+50,y+10,"red leg pushes,",2.2,"start",c="#c00")+tx(x+50,y+14,"blue leg lifts",2.2,"start",c="#06c")
for j,l in enumerate(["The motor turns both cranks. The pins are","half a turn apart, so when the left foot","pushes back on the table, the right foot lifts","and swings forward - then they swap.","Each push is ~22 mm; the foot lifts ~9 mm.","The thigh is a guide: it holds the knee so","the foot draws a flat-bottomed loop.","His hands push the barrow along!"]):
    s5+=tx(x+102,y+10+j*4,l,2.6,"start")
y=215; s5+=f'<rect x="12" y="{y}" width="112" height="44" rx="3" fill="#fff" stroke="#222" stroke-width=".5"/>'+tx(16,y+6,"Parts checklist",3.4,"start",b=True,c=pr["color"])
PL=["3 mm cardboard","~10 ice-cream sticks","2 wheels (caps/65 mm)","Skewers 3 mm","Paper straw","TT motor (double shaft)","2xAA holder + batteries","Slide switch + wire","Rubber bands (feet)","Ping-pong ball + cap","Hot glue (grown-up)","Pencil, scissors"]
for j,t in enumerate(PL):
    cxx=16+(j//4)*36; yy=y+10+(j%4)*8.3
    s5+=f'<rect x="{cxx}" y="{yy}" width="3.5" height="3.5" fill="#fff" stroke="#222" stroke-width=".4"/>'+tx(cxx+5,yy+3,t,2.3,"start")
s5+=f'<rect x="127" y="{y}" width="71" height="44" rx="3" fill="#fff3cd" stroke="#222" stroke-width=".5"/>'+tx(131,y+6,"Safety first!",3.4,"start",b=True,c="#c00")
SF=["• A grown-up uses the hot glue gun,","  craft knife, and pokes the holes.","• Snip the sharp skewer tips off.","• Fingers away from the cranks when ON.","• Batteries the right way round; never","  join the wires; take them out after.","• Keep small parts from little kids."]
for j,l in enumerate(SF): s5+=tx(131,y+12+j*4.6,l,2.4,"start")
N=5
bodies=[sheet(pr,[],i+1,N).replace('</svg>','') for i in range(N)]
bodies=[b+e for b,e in zip(bodies,[s1,s2,s3,s4,s5])]
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
    pdf(bodies,f'{D_}/templates.pdf'); pdf(bodies[4:],f'{D_}/card.pdf')
    b.close()
shutil.copy(f'{D_}/template-5.png',f'{D_}/card.png')

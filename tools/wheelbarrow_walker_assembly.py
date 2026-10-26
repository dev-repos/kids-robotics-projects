# Assembly guide pages appended after template sheets
G="#c8c8c8"; GS="#9a9a9a"
def C(hl,col): return (col,"#111") if hl else (G,GS)
def R_(x,y,w,h,f,s,rx=0,sw=.35): return f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{rx}" fill="{f}" stroke="{s}" stroke-width="{sw}"/>'
def Ci(x,y,r,f,s,sw=.35): return f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" fill="{f}" stroke="{s}" stroke-width="{sw}"/>'
def L_(x1,y1,x2,y2,c,w=.6): return f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{c}" stroke-width="{w}" stroke-linecap="round"/>'
def P_(pts,f,s,sw=.35): return '<path d="M'+' L'.join(f'{a:.2f},{b:.2f}' for a,b in pts)+f' Z" fill="{f}" stroke="{s}" stroke-width="{sw}"/>'
def legk(hx,hy,k,ang,hl,col="#2f5d3a",far=False):
    f,s=C(hl,col)
    if far and not hl: f="#b0b0b0"
    g=legshape(hx,hy,ang,fill=f,w=.35/k,stick=True)
    if not hl: g=g.replace('#a8d8a0','#dcdcdc')
    return f'<g transform="translate({hx},{hy}) scale({k}) translate({-hx},{-hy})">{g}</g>'
def scene(px,py,parts,hl=(),th=90,k=.27):
    """side view, walker faces right. parts: set of names"""
    g=''; T=py+48; sx=px+26; sy=T-(LF-HH)*k  # shaft
    H=lambda n:n in hl
    P,Hh,F,a=leg(math.radians(th)); P2,_,_,a2=leg(math.radians(th+180))
    hx,hy=sx,sy-HH*k
    g+=L_(px+1,T,px+79,T,"#777",.4)
    # barrow (right)
    if 'tray' in parts:
        f,s=C(H('tray'),"#e9c27a"); tx0=sx+26
        g+=P_([(tx0,T-20),(tx0+24,T-20),(tx0+21,T-11),(tx0+3,T-11)],f,s)
        g+=L_(tx0+1,T-19,sx+11,T-26,s,.8)  # handle
    if 'batt' in parts:
        f,s=C(H('batt'),"#2a7"); g+=R_(sx+30,T-11,10,3,f,s)
        f2,s2=C(H('batt'),"#ddd"); g+=R_(sx+42,T-11,3,2.5,f2,s2)
        if H('batt'): g+=f'<path d="M{sx+32},{T-11} Q{sx+22},{T-30} {sx+6},{sy-3}" fill="none" stroke="#c00" stroke-width=".4"/><path d="M{sx+34},{T-11} Q{sx+24},{T-28} {sx+6},{sy-1}" fill="none" stroke="#111" stroke-width=".4"/>'
    if 'wheel' in parts:
        f,s=C(H('wheel'),"#e33"); wx=sx+38
        g+=Ci(wx,T-5.5,5.5,f,s)+Ci(wx,T-5.5,1,"#fff",s)
        g+=L_(wx,T-5.5,wx,T-11,s,.5)
    # far leg
    if 'legR' in parts: g+=legk(hx,hy,k,-a2,H('legR'),"#24492d",far=True)
    if 'plates' in parts:
        f,s=C(H('plates'),"#f3e2c0"); g+=R_(sx-25*k,sy-40*k,50*k,60*k,f,s)
    if 'motor' in parts:
        f,s=C(H('motor'),"#fc0"); g+=R_(sx-11*k,sy-26*k,22*k,38*k,f,s)
        f,s=C(H('motor'),"#e8c84a"); g+=R_(sx-10*k,sy-54*k,20*k,28*k,f,s,rx=1.5)
        g+=tx(sx,sy-38*k,"TT",1.8,c="#555")
    if 'torso' in parts:
        f,s=C(H('torso'),"#5aa0e0"); g+=R_(sx-12.5*k,sy-56*k,25*k,60*k,f,s,rx=1)
    if 'head' in parts:
        f,s=C(H('head'),"#fff"); hy0=sy-56*k-20*k
        g+=Ci(sx,hy0,20*k,f,s)+(Ci(sx+8*k,hy0-3*k,3*k,"#111","#111") if H('head') else '')
        f,s=C(H('head'),"#e33"); g+=R_(sx-16*k,hy0-20*k,32*k,1.4,f,s)+R_(sx-9*k,hy0-34*k,18*k,14*k,f,s,rx=1)
    if 'arms' in parts:
        f,s=C(H('arms'),STICK); g+=L_(sx+2,sy-48*k,sx+11,T-26,s if not H('arms') else "#8a6a2a",1.6)+Ci(sx+11,T-26,1.3,("#fc0" if H('arms') else G),s)
    if 'crank' in parts:
        f,s=C(H('crank'),"#4a5a6a"); g+=Ci(sx,sy,9*k,f,s)+Ci(sx+P[0]*k,sy-P[1]*k,1,"#fff",s)
    if 'legL' in parts:
        g+=legk(hx,hy,k,-a,H('legL'))
    if 'pegs' in parts:
        f,s=C(H('pegs'),"#6a5a78"); g+=Ci(hx,hy,1.6,f,s)
    if 'pin' in parts:
        f,s=C(H('pin'),"#6a5a78"); g+=Ci(sx+P[0]*k,sy-P[1]*k,1.5,f,s)
    if 'path' in parts:
        g+='<path d="M'+' L'.join(f'{sx+p[0]*k:.2f},{sy-p[1]*k+1:.2f}' for p in PATH[::6])+'" fill="none" stroke="#c00" stroke-width=".6"/>'
    return g
ALL={'tray','wheel','plates','motor','crank','pegs','legL','pin','legR','torso','head','arms','batt'}
def arrow(x1,y1,x2,y2,c="#c00"): 
    an=math.atan2(y2-y1,x2-x1); return L_(x1,y1,x2,y2,c,.6)+P_([(x2,y2),(x2-2.5*math.cos(an-.4),y2-2.5*math.sin(an-.4)),(x2-2.5*math.cos(an+.4),y2-2.5*math.sin(an+.4))],c,c,.2)
def custom(i,px,py):
    g=''
    if i==1:
        g+=R_(px+18,py+2,40,40,"#fff","#111")+R_(px+22,py+34,30,4,"#000","#000")+tx(px+37,py+37,"100 mm",1.8,c="#fff",b=True)
        g+=R_(px+21,py+40,32,4,"#ffe066","#111")+''.join(L_(px+22+m*3,py+40,px+22+m*3,py+42,"#111",.2) for m in range(11))+tx(px+37,py+48,"ruler = 100 mm?",2.4,c="#c00",b=True)
        for j in range(4): g+=L_(px+23,py+10+j*6,px+52,py+10+j*6,"#999",.4)
    if i==2:
        for j,c_ in enumerate(("#e9c27a","#2f5d3a","#f3e2c0","#5aa0e0")):
            g+=R_(px+4+j*17,py+8+j*2,15,21,"#fff","#111")+R_(px+6+j*17,py+12+j*2,11,8,c_,"#111")+tx(px+11.5+j*17,py+26+j*2,f"sheet {j+1}",1.8)
        g+=f'<g transform="translate({px+40},{py+40})"><circle cx="-4" cy="4" r="3" fill="none" stroke="#c00" stroke-width=".7"/><circle cx="4" cy="4" r="3" fill="none" stroke="#c00" stroke-width=".7"/><line x1="-2" y1="2" x2="6" y2="-9" stroke="#111" stroke-width=".8"/><line x1="2" y1="2" x2="-6" y2="-9" stroke="#111" stroke-width=".8"/></g>'
    if i==3:
        k=.45; hx,hy=px+30,py+8; g+=legk(hx,hy,k,0,False)
        g+=Ci(hx,hy,2.75*k+.6,"none","#c00",.7)+arrow(px+60,py+4,hx+3,hy,"#c00")+tx(px+62,py+12,"hip Ø5.5",2.2,"start",c="#c00")+tx(px+62,py+30,"slot: knife",2.2,"start",c="#c00")+arrow(px+60,py+28,hx+2,hy+26*k,"#c00")
        g+=f'<g transform="translate({px+64},{py+2}) rotate(30)">'+R_(0,0,2.5,12,"#fc0","#111")+P_([(0,12),(2.5,12),(1.25,15)],"#f3e2c0","#111")+'</g>'
    if i==4:
        k=.45; hx,hy=px+26,py+8
        g+=f'<g opacity=".6">{legk(hx+6,hy+2,k,0,False)}</g>'+legk(hx,hy,k,0,False)
        g+=f'<g transform="translate({hx},{hy}) scale({k}) translate({-hx},{-hy})">'+P_([(hx+3,hy-3),(hx+9.5,hy-3),(hx+16.5,hy+55),(hx+10,hy+56)],"#a8d8a0","#111",.8)+'</g>'
        g+=arrow(px+62,py+20,hx+7,hy+12,"#2a7")+tx(px+58,py+16,"stick",2.4,"start",c="#2a7",b=True)+tx(px+58,py+44,"2 layers",2.2,"start")+tx(px+58,py+47.5,"= 6 mm",2.2,"start")
    if i==5:
        k=.45; hx,hy=px+30,py+8; g+=legk(hx,hy,k,0,False)
        fy=hy+LF*k; g+=R_(hx-HEEL*k,fy,(TOE+HEEL)*k,10*k*.5,"#e9c27a","#111")
        for xx in (hx-2,hx+10): g+=f'<ellipse cx="{xx}" cy="{fy-.5}" rx="1.2" ry="3" fill="none" stroke="#c00" stroke-width=".7"/>'
        g+=tx(hx+22,fy-10,"sole 54 mm + 2 bands",2.2,"start",c="#c00")
    if i==10:
        y=py+24
        g+=R_(px+4,y-1.5,4,3,G,GS)+tx(px+6,y+9,"plate",1.8)
        g+=L_(px+8,y,px+50,y,"#a66",1.2)+R_(px+10,y-2.5,10,5,"#bfe3ff","#111")+tx(px+15,y-5,"spacer 5",1.8)
        g+=R_(px+22,y-3.5,6,7,"#2f5d3a","#111")+tx(px+25,y+9,"leg",1.8)+R_(px+29,y-2.5,8,5,"#bfe3ff","#111")
        g+=Ci(px+50,y,3.5,"#6a5a78","#111")+tx(px+50,y+9,"button",1.8)+tx(px+26,y+16,"peg 22 mm, 26 mm above shaft",2.2,c="#c00",b=True)
        g+=tx(px+33,y-8,"sleeve 8 inside leg hole",1.8)
    if i==9:
        for cx,dy,c,nm in ((px+20,-6,"#c00","A"),(px+55,6,"#06c","B")):
            g+=Ci(cx,py+26,9,"#4a5a6a","#111")+Ci(cx,py+26,3,"#a8c4dc","#111")+Ci(cx,py+26+dy,1.6,c,"#111")+tx(cx,py+40,f"crank {nm}",2.4,b=True)
        g+=tx(px+37,py+47,"pins 180° apart (opposite)",2.4,c="#c00",b=True)+L_(px+29,py+26,px+46,py+26,"#fc0",1.4)
    if i==20:
        rows=[("Leg jams?","slot not on centre line - re-cut"),("Feet slip?","more rubber bands"),("Walks back?","swap the 2 wires"),("Wobbles?","glue plates square"),("No buzz?","check batteries/switch")]
        for j,(a_,b_) in enumerate(rows): g+=tx(px+2,py+6+j*9,a_,2.4,"start",b=True,c="#c00")+tx(px+2,py+9.6+j*9,b_,2.2,"start")
    return g
STEPS=[ # (title, parts/sheet, tools, instruction, check, grownup, picture)
("Print and check","All 5 template sheets","Printer, ruler","Print at 100% (Actual size), never 'fit to page'.","The black bar on each sheet measures exactly 100 mm.",False,('c',1)),
("Cut out the parts","Sheet 1 tray, sheet 2 legs, sheet 3 plates & cranks, sheet 4 covers","Scissors, craft knife","Glue each sheet on cardboard, then cut on the solid lines.","You have 4 leg layers, 2 plates, 4 cranks, 4 buttons.",True,('c',2)),
("Poke the holes","Sheet 2: Leg L x2, Leg R x2","Pencil/awl, craft knife","Poke the Ø5.5 hip holes; knife out the 5.5 mm slots.","A straw slides into the hip hole; a straw fits the slot.",True,('c',3)),
("Glue the legs","Sheet 2: Leg layers x4 + 2 ice-cream sticks","Glue","Glue 2 layers per leg, then the pale stick along the thigh front.","Holes and slots line up; leg is flat and stiff.",False,('c',4)),
("Add the long feet","Sheet 2: Sole sticks x2 (54x10)","Glue, rubber bands","Glue a sole stick under each foot, toe forward; add 2 bands.","Both feet lie flat; toe points the walking way.",False,('c',5)),
("Fold the barrow tray","Sheet 1: tray + side walls","Ruler, glue","Score the dashed lines, fold up and glue tabs inside.","Tray box stands square and does not wobble.",False,('s',{'tray'},{'tray'})),
("Axle and wheels","Sheet 1 hangers, skewer 110 mm, straw, 2 wheels","Hot glue","Straw under tray, skewer through, wheel glued on each end.","Spin the wheels: they roll freely.",True,('s',{'tray','wheel'},{'wheel'})),
("Hip plates on motor","Sheet 3: hip plates x2, TT motor","Hot glue","Motor upright (can on top); plate on each side, shaft in Ø30 hole.","Shaft is in the hole centre; hip hole is straight above.",True,('s',{'motor','plates'},{'plates'})),
("Cranks A then B","Sheet 3: crank A x2, crank B x2","Glue","Glue crank A on one shaft end, then B on the other side.","Look from the side: pins point opposite (180°).",False,('c',9)),
("Hip pegs + spacers","Skewer 22 mm x2, straw 5 mm + 8 mm","Hot glue","Glue a peg in each hip hole, 26 mm above shaft; slip on the spacer.","Peg sticks out straight, not tilted.",True,('c',10)),
("Hang the left leg","Leg L, hip sleeve, button","Glue","Slide the leg (sleeve in hip hole) on the left peg; glue a button on the outside.","Leg swings freely, button stops it falling off.",False,('s',{'motor','plates','crank','legL','pegs'},{'legL','pegs'})),
("Pin and roller","Skewer 18 mm, straw roller 6 mm, button","Glue","Glue the crank pin, slip the roller on, put it in the slot, button outside.","Roller slides along the slot without catching.",False,('s',{'motor','plates','crank','legL','pegs','pin'},{'pin'})),
("Right leg the same","Leg R, sleeve, roller, 2 buttons","Glue","Repeat steps 11-12 on the other side (crank B).","Legs hang opposite: one front, one back.",False,('s',{'motor','plates','crank','legL','pegs','pin','legR'},{'legR'},20)),
("Hand-turn test","Sheet 4: 1:1 swing check","Fingers","Turn the shaft slowly by hand for 3 full turns.","No jams; foot sweeps about 54 mm like sheet 4.",False,('s',{'motor','plates','crank','legL','pegs','pin','legR','path'},{'path'},20)),
("Torso covers","Sheet 4: FRONT + BACK covers","Glue","Glue the covers on the plate edges with the side tabs.","Cranks and legs still turn freely.",False,('s',ALL-{'head','arms','tray','wheel','batt'},{'torso'})),
("Head and hat","Ping-pong ball, sheet 4 hat brim + bottle cap","Hot glue","Glue the ball on the neck, brim and cap on top as a hat.","Head sits straight; draw a face.",True,('s',ALL-{'arms','tray','wheel','batt'},{'head'})),
("Arms to handles","Ice-cream stick arms, barrow","Hot glue","Stand both feet on the table, glue hands onto the handles.","Barrow wheels touch the table; feet flat.",True,('s',ALL-{'batt'},{'arms','tray'})),
("Battery and switch","2xAA holder, switch plate (sheet 4), wires","Tape, glue","Holder + switch under tray; wires along a handle to the motor.","Wires do not touch the legs or cranks.",False,('s',ALL,{'batt'})),
("First walk!","Whole robot","Table","Switch ON. Walks backwards? Swap the 2 motor wires.","He pushes the barrow forward, wheels roll.",False,('s',ALL|{'path'},{'path','legL','legR'})),
("Troubleshooting","-","-","Fix the most common problems:","Still stuck? Re-check sheet 4 swing.",False,('c',20)),
]
def gu(x,y): return Ci(x,y,3,"#c00","#111",.3)+tx(x,y+1.3,"!",3.6,c="#fff",b=True)+tx(x-4,y+1,"Grown-up",2.4,"end",c="#c00",b=True)
def panel(n,st,x,y,w,h):
    ti,pa,to,ins,ck,gr,pc=st
    g=R_(x,y,w,h,"#fffdf6","#222",3,.5)+Ci(x+7,y+7,5,pr["color"],"#222",.4)+tx(x+7,y+8.8,str(n),5,c="#fff",b=True)
    g+=R_(x+4,y+14,84,h-18,"#fff","#bbb",2,.3)
    px,py=x+6,y+15
    g+=custom(pc[1],px,py) if pc[0]=='c' else scene(px,py,pc[1],pc[2],*(pc[3:] or (90,)))
    tx0=x+94; g+=tx(x+15,y+9.5,ti,4.4,"start",b=True,c=pr["color"])
    if gr: g+=gu(x+w-6,y+7)
    yy=y+20
    for lab_,val,c_,wd in (("PARTS",pa,"#333",44),("TOOLS",to,"#333",44),("DO",ins,"#111",40),("CHECK ✓",ck,"#0a7a3a",40)):
        g+=tx(tx0,yy,lab_,2.6,"start",b=True,c=c_ if lab_!="PARTS" else "#8d6e3f")
        for j,l in enumerate(wrap(val,wd)): g+=tx(tx0+17,yy+j*3.9,l,2.8 if lab_ in("DO",) else 2.6,"start",c=c_,b=lab_=="DO")
        yy+=max(1,len(wrap(val,wd)))*3.9+3.2
    return g
PAGES=[STEPS[i:i+3] for i in range(0,len(STEPS),3)]
asm=[]; K=len(PAGES); n=1
for pi,ps in enumerate(PAGES):
    b=sheet(pr,[],1,1).replace(f"Templates 1/1 (1:1 scale)",f"Assembly guide {pi+1}/{K} · step by step")
    b+=tx(105,39.5,"Build one step at a time. Colour = the new part, grey = already done.  ! = grown-up step.",2.8,c="#555")
    for j,st in enumerate(ps): b+=panel(n,st,12,42+j*72,186,69); n+=1
    asm.append(b)

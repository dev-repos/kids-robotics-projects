from wheelbarrow_walker_geometry import *
import math
R,T,A,FD,H=8,35,40,40,(-36,-8)
pts,mu=sim(R,H,T,A,FD,360)
s,l,w=metrics(pts,2.0)
ymin=min(p[1] for p in pts)
print("Grashof: ground %.1f crank %d coupler %d rocker %d -> s+l=%d <= p+q=%.1f"%(math.hypot(*H),R,A,T,R+A,math.hypot(*H)+T))
print("stride(flat, foot within 2mm of lowest) %.1f  lift %.1f  total x-sweep %.1f  transmission %.0f-%.0f deg"%(s,l,w,min(mu),max(mu)))
print("foot lowest y %.1f (below crank centre) x range %.1f..%.1f"%(ymin,min(p[0] for p in pts),max(p[0] for p in pts)))
# direction during ground phase (crank CCW = increasing theta)
g=[i for i,p in enumerate(pts) if p[1]<ymin+2]
dx=[pts[(i+1)%360][0]-pts[i][0] for i in g]
print("ground-phase foot dx sum (CCW crank):",round(sum(dx),1),"=> body moves",("forward(+x)" if sum(dx)<0 else "backward"),"; frac of cycle on ground",len(g)/360)
# 180 deg phase: support = lower foot; body height variation
hs=[min(pts[i][1],pts[(i+180)%360][1]) for i in range(360)]
print("support height bob %.1f mm"%(max(hs)-min(hs)))
# effective body advance per rev: support foot x change
adv=0
for i in range(360):
    j=i if pts[i][1]<=pts[(i+180)%360][1] else (i+180)%360
    adv+=-(pts[(j+1)%360][0]-pts[j][0])
print("approx body advance per crank turn %.1f mm (no slip)"%adv)
import json;pass
# clearance: crank pin vs thigh segment (thigh is in the layer the crank pin passes through)
def segd(p,a,b):
    ax,ay=b[0]-a[0],b[1]-a[1]; t=max(0,min(1,((p[0]-a[0])*ax+(p[1]-a[1])*ay)/(ax*ax+ay*ay)))
    return math.hypot(p[0]-a[0]-t*ax,p[1]-a[1]-t*ay)
md=99;kx=[]
for i in range(360):
    th=math.radians(i);P=(R*math.cos(th),R*math.sin(th))
    F=pts[i];ux,uy=(F[0]-P[0])/(A+FD),(F[1]-P[1])/(A+FD);K=(P[0]+ux*A,P[1]+uy*A);kx.append(K)
    md=min(md,segd(P,H,K))
print("min crank-pin to thigh centreline %.1f mm"%md, "knee x %.1f..%.1f y %.1f..%.1f"%(min(k[0] for k in kx),max(k[0] for k in kx),min(k[1] for k in kx),max(k[1] for k in kx)))
print("thigh swing deg %.1f"%(max(math.degrees(math.atan2(k[1]-H[1],k[0]-H[0])) for k in kx)-min(math.degrees(math.atan2(k[1]-H[1],k[0]-H[0])) for k in kx)))

# Wheelbarrow Walker leg linkage check (side view, mm, x forward, y up)
# Crank centre C=(0,0) on TT motor shaft. Crank pin P at radius R.
# Thigh (rocker) pivots at hip H, knee K at thigh length T.
# Leg stick (coupler): top hole on crank pin P, knee hole K at A from P, foot F at A+FD along P->K.
import math,itertools,sys
def sim(R,H,T,A,FD,n=360):
    pts=[];mu=[]
    for i in range(n):
        th=2*math.pi*i/n; P=(R*math.cos(th),R*math.sin(th))
        dx,dy=H[0]-P[0],H[1]-P[1]; d=math.hypot(dx,dy)
        if d<1e-6 or d>A+T or d<abs(A-T): return None
        a=(A*A-T*T+d*d)/(2*d); h=math.sqrt(max(A*A-a*a,0))
        # choose knee on the lower branch (knee in front/below)
        bx,by=P[0]+a*dx/d,P[1]+a*dy/d
        K1=(bx+h*dy/d,by-h*dx/d);K2=(bx-h*dy/d,by+h*dx/d)
        K=K1 if K1[1]<K2[1] else K2
        ux,uy=(K[0]-P[0])/A,(K[1]-P[1])/A
        F=(P[0]+ux*(A+FD),P[1]+uy*(A+FD)); pts.append(F)
        # transmission angle at knee between coupler and thigh
        vx,vy=K[0]-H[0],K[1]-H[1]; c=(ux*vx+uy*vy)/T; mu.append(math.degrees(math.acos(max(-1,min(1,c)))))
    return pts,mu
def metrics(pts,tol=1.0):
    ymin=min(p[1] for p in pts); ymax=max(p[1] for p in pts)
    ground=[p[0] for p in pts if p[1]<ymin+tol]
    return max(ground)-min(ground), ymax-ymin, max(p[0] for p in pts)-min(p[0] for p in pts)
if __name__=="__main__":
    R=8; T=35; A=40; FD=40   # thigh: 45 stick (holes 35 apart); leg: 90 stick, holes at 5,45,85 -> A=40, FD=40
    best=None
    for hx in range(-30,31,2):
        for hy in range(-10,31,2):
            r=sim(R,(hx,hy),T,A,FD)
            if not r: continue
            pts,mu=r; s,l,w=metrics(pts)
            mmin=min(min(mu),180-max(mu))
            if mmin<40: continue
            sc=-abs(s-22)-abs(l-8)*0.8
            if best is None or sc>best[0]: best=(sc,hx,hy,s,l,w,min(mu),max(mu))
    print("best H",best)

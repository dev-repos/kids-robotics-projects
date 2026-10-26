# Wheelbarrow Walker swing-leg (pendulum) geometry, side view, mm, shaft at (0,0), y up.
# Leg hangs from hip peg H=(0,HH); crank pin P (radius R) runs in a slot along the leg; foot at LF from H.
import math
R,HH,LF,SL0,SL1=8,26,88,13,39
def leg(th):
    P=(R*math.cos(th),R*math.sin(th)); a=math.atan2(P[0],HH-P[1])
    return P,(LF*math.sin(a),HH-LF*math.cos(a)),a,math.hypot(P[0],P[1]-HH)

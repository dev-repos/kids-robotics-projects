from wheelbarrow_walker_geometry import *
S=[leg(math.radians(i/4)) for i in range(1440)]
xs=[s[1][0] for s in S]; ys=[s[1][1] for s in S]; d=[s[3] for s in S]
print("foot sweep %.1f mm, rise %.1f mm, swing +-%.1f deg"%(max(xs)-min(xs),max(ys)-min(ys),max(abs(math.degrees(s[2])) for s in S)))
print("pin-to-hip %.1f..%.1f mm, slot centreline %d..%d -> margin %.1f / %.1f mm (no jam, never leaves slot)"%(min(d),max(d),SL0,SL1,min(d)-SL0,SL1-max(d)))
print("shaft to table %.1f mm"%-min(ys))
assert min(d)-SL0>2 and SL1-max(d)>2

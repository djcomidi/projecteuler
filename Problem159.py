#!/usr/bin/env python

LIMIT = 10**6
DRS = []
for n in xrange(LIMIT+1):
	x = n
	while x > 9:
		x = sum( int(c) for c in str(x) )
	DRS.append( x )

def ways(n,minfac,drs,mdrs):
	if n >= LIMIT: return
	mdrs[n] = max( mdrs[n], drs )
	for d in xrange(minfac,(LIMIT//n)+1):
		ways( n*d, max(minfac,d), drs+DRS[d], mdrs )

mdrsLookup = [0]*(LIMIT+1)
ways(1,2,0,mdrsLookup)
print sum( mdrsLookup[2:LIMIT] )
# 2m10s

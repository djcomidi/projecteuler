#!/usr/bin/env python

LIMIT = 10**5
rads = [1]*(LIMIT+1)
for p in xrange(2,LIMIT+1):
	if rads[p] > 1: continue
	for k in xrange(p,LIMIT+1,p):
		rads[k] *= p
radList = sorted( [ (rads[i],i) for i in xrange(1,LIMIT+1) ] )
print radList[10**4-1][1]

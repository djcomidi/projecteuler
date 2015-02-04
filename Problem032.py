#!/usr/bin/env python

from EulerTools import is_pandigital

def checkABC(a,b,c):
	return is_pandigital( str(a) + str(b) + str(c), 1, 9 )

pans = set([])
for a in xrange(1,50):
	for b in xrange(a+1,2000):
		c = a*b
		if checkABC(a,b,c):
			pans.add(c)
print sum(pans)

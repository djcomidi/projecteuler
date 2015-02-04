#!/usr/bin/env python

from EulerTools import is_pandigital

maxs = 0
for k in xrange(2,4):
	for n in xrange(1,10000):
		s = ''.join( str(n*t) for t in xrange(1,k) )
		if is_pandigital(s,1,9):
			maxs = max( maxs, int(s) )
print maxs

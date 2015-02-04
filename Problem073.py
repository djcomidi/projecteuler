#!/usr/bin/env python

from EulerTools import gcd

LOWRANGE, HIGHRANGE = 1.0/3, 1.0/2
t = 0
for n in xrange(4,12001):
	for i in xrange(n//3,n//2+1):
		ratio = (1.0*i)/n
		if gcd(n,i) == 1 and LOWRANGE < ratio < HIGHRANGE:
			t += 1
print t
# ~30s

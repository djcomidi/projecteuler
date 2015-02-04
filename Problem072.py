#!/usr/bin/env python

from EulerTools import next_prime

LIMIT = 10**6
denoms = range(LIMIT+1)
denoms[1] = 0
p = 2
while p < LIMIT:
	for k in xrange(p,LIMIT,p):
		denoms[k] = ( denoms[k] * (p-1) ) // p
	p = next_prime(p)
print sum(denoms)

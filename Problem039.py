#!/usr/bin/env python

from EulerTools import is_square

perims = [0]*1001

for a in xrange(1,400):
	for b in xrange(a+1,400):
		c2 = a**2 + b**2
		if not is_square(c2): continue
		c = int(c2**0.5)
		p = a+b+c
		if p <= 1000:
			perims[p] += 1

print perims.index(max(perims))

#!/usr/bin/env python

from EulerTools import is_prime

total = 0
for n in xrange(10,150*10**6,10):
	if not n%210 in [10,80,130,200]: continue
	p = n**2 + 1
	if not is_prime(p): continue
	if [2,6,8,12,26] == [ q for q in xrange(2,27,2) if is_prime(p+q) ]:
		total += n
print total
# ~1m5s

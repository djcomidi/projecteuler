#!/usr/bin/env python

from EulerTools import mul
from EulerTools import next_prime
from EulerTools import prime_factors_dict

LIMIT = 1000
e = 1
while 3**(e+1) < 2*LIMIT:
	e += 1
factors = [2]
for i in xrange(e):
	factors.append( int(next_prime(factors[-1])) )
minn = 2**31
while len(factors) > 2:
	factors[-1] -= 1
	if factors[-1] == 1: factors = factors[:-1]
	n = reduce( mul, factors, 1 )
	t = reduce( mul, [2*e+1 for e in prime_factors_dict(n).values()], 1 )
	if t >= 2*LIMIT:
		minn = min(n,minn)
print minn

#!/usr/bin/env python

from EulerTools import next_prime
from EulerTools import Memoize

@Memoize
def get_ways(n,minp=2):
	if n == 0: return 1
	ways, p = 0, minp
	while p <= n:
		ways += get_ways(n-p,max(minp,p))
		p = next_prime(p)
	return ways

n = 1
while get_ways(n) < 5000:
	n += 1
print n, get_ways(n)

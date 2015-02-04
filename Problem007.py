#!/usr/bin/env python

from EulerTools import next_prime

n, p = 1, next_prime(1)
while n < 10001:
	p, n = next_prime(p), n+1
print p


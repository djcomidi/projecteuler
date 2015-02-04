#!/usr/bin/env python

from EulerTools import next_prime

n, p = 1, 2
while n*p < 10**6+1:
	n *= p
	p = next_prime(p)
print n

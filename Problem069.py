#!/usr/bin/env python

#from EulerTools import prime_factors, totient
#max_ratio = 0.0
#max_n = 0
#for n in xrange(2,10**6+1):
#	ratio = (1.0*n)/totient(n)
#	if ratio > max_ratio:
#		max_ratio, max_n = ratio, n
#print max_n, max_ratio

from EulerTools import next_prime
n, p = 1, 2
while n*p < 10**6+1:
	n *= p
	p = next_prime(p)
print n

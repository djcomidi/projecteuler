#!/usr/bin/env python

from EulerTools import next_prime

N, K = 20000000, 15000000

def primes_in_fac(p,n):
	m, e = 0, 1
	while p**e <= n:
		m += n//(p**e)
		e += 1
	return m

sumfacs, p = 0, 2
while p <= N:
	sumfacs += p * ( primes_in_fac(p,N) - primes_in_fac(p,K) - primes_in_fac(p,N-K) )
	p = next_prime(p)
print sumfacs

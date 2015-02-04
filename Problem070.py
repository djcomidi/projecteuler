#!/usr/bin/env python

from EulerTools import next_prime

def is_permutation(a,b):
	return sorted(str(a)) == sorted(str(b))

MAXPRIME = 4000
min_ratio = 3.0
min_n = 0
pA = 3
while pA < MAXPRIME:
	pB = next_prime(pA)
	while pB < MAXPRIME:
		n = pA * pB
		if n > 10**7: break
		totn = (pA-1)*(pB-1)
		if is_permutation(n,totn):
			ratio = (1.0*n)/totn
			if ratio < min_ratio:
				min_ratio, min_n = ratio, n
#				print min_n, min_ratio
		pB = next_prime(pB)
	pA = next_prime(pA)
print min_n, min_ratio

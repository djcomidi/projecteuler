#!/usr/bin/env python

from EulerTools import is_prime, next_prime

LIMIT = 10**4

def make_prime(pA,pB):
	return is_prime( int(str(pA)+str(pB)) )

PRIMES = []
p = 2
while p < LIMIT:
	PRIMES.append(p)
	p = next_prime(p)

def find_five(arr):
	for i in xrange(len(arr)-1):
		if not make_prime(arr[-1],arr[i]): return
		if not make_prime(arr[i],arr[-1]): return
	if len(arr) == 5:
		print map(int,arr), sum(arr)
	else:
		for p in filter(lambda x: x > arr[-1], PRIMES):
			find_five(arr+[p])

for p in [2,3,5,7,11,13]:
	find_five([p])

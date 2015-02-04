#!/usr/bin/env python

LIMIT = 10**17
FIBS = [1,2]
while FIBS[-1] < LIMIT:
	FIBS.append( FIBS[-2]+FIBS[-1] )

def count_terms(n,cache={1:0}):
	if not n in cache:
		fib = max( filter( lambda f: f < n, FIBS ) )
		cache[n] = n - fib + count_terms(n-fib) + count_terms(fib)
	return cache[n]

print count_terms(LIMIT)

#!/usr/bin/env python

collatzes = {1:1}
def collatz_terms(n):
	if collatzes.has_key(n): return collatzes[n]
	if n & 1 == 0:
		following = collatz_terms(n//2)
	else:
		following = collatz_terms(3*n+1)
	collatzes[n] = 1 + following
	return collatzes[n]

maxterms = 0
maxstart = 0
for n in xrange(1,1000000):
	terms = collatz_terms(n)
	if terms > maxterms:
		maxterms, maxstart = terms, n
print maxstart

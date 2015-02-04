#!/usr/bin/env python

LIMIT = 10**7

divisors = [0,1] + [2]*LIMIT
sols = 0
for d in xrange(2,LIMIT):
	for k in xrange(d+d,LIMIT,d):
		divisors[k] += 1
	if divisors[d] == divisors[d-1]:
		sols += 1
print sols

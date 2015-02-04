#!/usr/bin/env python

func=lambda x,n: 3*n**2+2*n*x-x**2

LIMIT = 10**6
ways = [0] * LIMIT

for x in xrange(1,LIMIT):
	n = x//3
	while True:
		val = func(x,n)
		if val >= LIMIT: break
		if val >= 0:
			ways[func(x,n)] += 1
		n += 1

print ways.index(10)
print ways.count(10)

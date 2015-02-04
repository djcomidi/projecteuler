#!/usr/bin/env python

LIMIT = 10**10
sol = 0
for i in xrange(1,1001):
	sol += pow(i,i,LIMIT)
print sol % LIMIT

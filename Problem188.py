#!/usr/bin/env python

a, k, modulo = 1777, 1855, 10**8
e = 1

for i in xrange(k):
	e = pow(a,e,modulo)
print e

#!/usr/bin/env python

def funcU(r,k):
	return (900-3*k)*r**(k-1) 

def funcS(r,n):
	return sum( funcU(r,k) for k in xrange(1,n+1) )

TARGET = -600000000000
N = 5000
r, t = 1, 1.0

while r < 10**13:
	r, t, i = 10*r, 10.0*t, 0
	while funcS( (r+i+1)/t, N ) > TARGET:
		i += 1
	r += i
print "%.12f" % (r/t)

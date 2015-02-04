#!/usr/bin/env python

lookup = {}

def p(k,n):
	global lookup
	if not (k,n) in lookup:
		if k > n:
			val = 0
		elif k == n:
			val = 1
		else:
			val = p(k+1,n)
			val += p(k,n-k)
		lookup[(k,n)] = val
	return lookup[(k,n)]

print p(1,100)-1

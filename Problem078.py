#!/usr/bin/env python

from EulerTools import pentagonal

def get_sign(i):
	return 1 - 2 * (((i-1)//2)&1)

def get_term(i):
	global max_p
	if i&1 == 1: p = (i+1)//2
	if i&1 == 0: p = -(i//2)
	return pentagonal(p)

pVals = [1,1]
while pVals[-1] % 10**6 != 0:
	n = len(pVals)
	t, pVal = 1, 0
	while get_term(t) <= n:
		t, pVal = t+1, pVal + (get_sign(t)*pVals[n-get_term(t)])
	pVals.append( pVal % 10**7 )
print len(pVals)-1
# ~1min45

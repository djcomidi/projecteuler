#!/usr/bin/env python

from EulerTools import triangle, pentagonal, hexagonal

tN, pN, hN = 285, 165, 143
t, p, h = triangle(tN), pentagonal(pN), hexagonal(hN)
while True:
	hN += 1
	h = hexagonal(hN)
	while p < h:
		pN += 1
		p = pentagonal(pN)
	while t < p:
		tN += 1
		t = triangle(tN)
	if h == p == t:
		break
print t
	

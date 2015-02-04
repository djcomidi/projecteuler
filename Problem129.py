#!/usr/bin/env python

from EulerTools import next_prime

def A(n):
	r, t = 0, 0
	while True:
		r, t = (10*r+1) % n, t+1
		if r == 0: break
	return t

n = 999999
while A(n) < 10**6:
	n += 2
	if n%5==0: n += 2
print n

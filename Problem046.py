#!/usr/bin/env python

from EulerTools import is_prime, is_square, next_prime

def matches_criteria(n):
	if is_prime(n): return True
	p, has_criteria = 2, False
	while p < n and not has_criteria:
		has_criteria = is_square( (n-p)//2 )
		p = next_prime(p)
	return has_criteria

n = 35
while matches_criteria(n):
	n += 2
print n

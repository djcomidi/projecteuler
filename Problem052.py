#!/usr/bin/env python

def have_same_digits(m,n):
	return sorted(str(m)) == sorted(str(n))

found = False
n = 0
while not found:
	n += 1
	if not have_same_digits(n,2*n): continue
	if not have_same_digits(n,3*n): continue
	if not have_same_digits(n,4*n): continue
	if not have_same_digits(n,5*n): continue
	if not have_same_digits(n,6*n): continue
	found = True
print n

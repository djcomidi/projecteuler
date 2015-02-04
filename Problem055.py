#!/usr/bin/env python

from EulerTools import is_palindrome

def is_lychrel(n):
	for i in xrange(50):
		n = n + int(str(n)[::-1])
		if is_palindrome(n): break
	return not is_palindrome(n)

lychrels = 0
for n in xrange(1,10001):
	if is_lychrel(n):
		lychrels += 1
print lychrels

#!/usr/bin/env python

from EulerTools import is_palindrome

total = 0
for n in xrange(1,10**6,2):
	if not is_palindrome(n): continue
	if is_palindrome(bin(n)[2:]):
		total += n
print total

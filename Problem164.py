#!/usr/bin/env python

from EulerTools import Memoize

@Memoize
def find_number(digitsToDo,lastDigit=0,maxAllowed=10):
	if digitsToDo == 0: return 1
	if digitsToDo == 19 and lastDigit == 0: return 0
	total = 0
	for d in xrange(maxAllowed):
		total += find_number(digitsToDo-1,d,10-lastDigit-d)
	return total

print find_number(20)

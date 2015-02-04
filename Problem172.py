#!/usr/bin/env python

from EulerTools import Memoize

@Memoize
def find_numbers(numLength,x0=3,x1=3,x2=3,x3=3,x4=3,x5=3,x6=3,x7=3,x8=3,x9=3):
#	print "find_numbers(",numLength,x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,")"
	if numLength == 0: return 1
	if x0 == 2 and x0+x1+x2+x3+x4+x5+x6+x7+x8+x9 == 29: return 0
	nValids = 0
	if x0 > 0: nValids += find_numbers(numLength-1,x0-1,x1,x2,x3,x4,x5,x6,x7,x8,x9)
	if x1 > 0: nValids += find_numbers(numLength-1,x0,x1-1,x2,x3,x4,x5,x6,x7,x8,x9)
	if x2 > 0: nValids += find_numbers(numLength-1,x0,x1,x2-1,x3,x4,x5,x6,x7,x8,x9)
	if x3 > 0: nValids += find_numbers(numLength-1,x0,x1,x2,x3-1,x4,x5,x6,x7,x8,x9)
	if x4 > 0: nValids += find_numbers(numLength-1,x0,x1,x2,x3,x4-1,x5,x6,x7,x8,x9)
	if x5 > 0: nValids += find_numbers(numLength-1,x0,x1,x2,x3,x4,x5-1,x6,x7,x8,x9)
	if x6 > 0: nValids += find_numbers(numLength-1,x0,x1,x2,x3,x4,x5,x6-1,x7,x8,x9)
	if x7 > 0: nValids += find_numbers(numLength-1,x0,x1,x2,x3,x4,x5,x6,x7-1,x8,x9)
	if x8 > 0: nValids += find_numbers(numLength-1,x0,x1,x2,x3,x4,x5,x6,x7,x8-1,x9)
	if x9 > 0: nValids += find_numbers(numLength-1,x0,x1,x2,x3,x4,x5,x6,x7,x8,x9-1)
	return nValids

print find_numbers( 18 )

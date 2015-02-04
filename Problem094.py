#!/usr/bin/env python

from EulerTools import is_square

def has_int_area(sideA,sideB,sideC):
	s = (sideA+sideB+sideC)//2
	return is_square( s*(s-sideA)*(s-sideB)*(s-sideC) )

total = 0
for side in xrange(3,333333334,2):
	if has_int_area(side,side,side-1):
		total += 3 * side - 1
		print "%9d %9d %9d %d" % (side, side, side-1, total)
	if has_int_area(side,side,side+1):
		total += 3 * side + 1
		print "%9d %9d %9d %d" % (side, side, side+1, total)
print total

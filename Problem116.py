#!/usr/bin/env python

from EulerTools import Memoize

@Memoize
def fill_count(singleW,size):
	ways = 0
	for pos in xrange(size-singleW+1):
		ways += 1 + fill_count(singleW,size-(pos+singleW))
	return ways

print sum( fill_count(w,50) for w in [2,3,4] )

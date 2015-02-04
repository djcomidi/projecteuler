#!/usr/bin/env python

def sum_of_digits(n):
	return sum( map( int, list(str(n)) ) )

max_sum = 0
for a in xrange(1,100):
	for b in xrange(1,100):
		max_sum = max( max_sum, sum_of_digits(a**b) )
print max_sum

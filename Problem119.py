#!/usr/bin/env python

def sum_digits(n):
	return sum( map( int, list(str(n)) ) )

arr = set()
for n in xrange(2,1000):
	for t in xrange(1000):
		if n**t < 10: continue
		if n**t > 10**15: break
		if sum_digits(n**t) == n:
			arr.add(n**t)
print len(arr)
arr = sorted(arr)
print arr[1]
print arr[9]
print arr[29]

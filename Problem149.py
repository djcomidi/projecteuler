#!/usr/bin/env python

fibs = []
for k in xrange(1,56):
	fibs.append( (100003 - 200003*k + 300007*k**3) % 1000000 - 500000 )
for k in xrange(56,4000001):
	fibs.append( (fibs[-24] + fibs[-55] + 1000000) % 1000000 - 500000 )

maxsum = 0
for i in xrange(2000):
	colsum, rowsum = 0, 0
	for j in xrange(2000):
		colsum = max( colsum + fibs[j*2000+i], 0 )
		rowsum = max( rowsum + fibs[i*2000+j], 0 )
		maxsum = max( maxsum, max( colsum, rowsum ) )
print maxsum

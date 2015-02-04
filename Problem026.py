#!/usr/bin/env python

def count_recur(n):
	checks = []
	q, r = divmod(1,n)
	while not (q,r) in checks and r != 0:
		checks.append( (q,r) )
		q, r = divmod( r*10, n )
	if r == 0: return 0
	return len(checks)-checks.index( (q,r) )

max_recur = 0
max_recur_n = 0
for d in xrange(2,1000):
	d_recur = count_recur(d)
	if d_recur > max_recur:
		max_recur = d_recur
		max_recur_n = d
print "1/%d has a %d-digit recurring cycle" % ( max_recur_n, max_recur )

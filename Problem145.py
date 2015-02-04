#!/usr/bin/env python

reversibles = 0
t = 1
for t in [2,3,4,6,7,8]:
	for n in xrange(10**(t-1),10**t):
		if n%10 == 0: continue
		revn = int(str(n)[::-1])
		if revn < n: continue
		if set(str(n+revn)) <= set("13579"):
			reversibles += 2
	print "10**%d -> %d" % (t,reversibles)
print reversibles
# 8m30s

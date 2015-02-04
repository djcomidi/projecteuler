#!/usr/bin/env python

powers = set()
for a in xrange(2,101):
	for b in xrange(2,101):
		powers.add(a**b)
print len(powers)

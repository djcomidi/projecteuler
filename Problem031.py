#!/usr/bin/env python

COINS = [ 1, 2, 5, 10, 20, 50, 100, 200 ]
ways = 0

def consume(used):
	s = sum(used)
	if s == 200:
		global ways
		ways += 1
	else:
		for c in filter(lambda x: max(used) <= x <= 200-s, COINS):
			consume(used+[c])

consume([0])
print ways
# ~1m40s

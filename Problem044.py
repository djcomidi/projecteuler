#!/usr/bin/env python

from EulerTools import polygonal

SIZE = 2500
pentas = [ polygonal(5,i) for i in xrange(1,SIZE+1) ]

for a in xrange(len(pentas)):
	for b in xrange(a+1,len(pentas)):
		if pentas[b]+pentas[a] in pentas and pentas[b]-pentas[a] in pentas:
			print pentas[b]-pentas[a]
			exit(0)

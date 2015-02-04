#!/usr/bin/env python

from EulerTools import mul
from EulerTools import polygonal

total = 0
for n in xrange(2,16):
	step = (1.0*n)/polygonal(3,n)
	total += int(reduce( mul, [ (step*i)**i for i in xrange(1,n+1) ], 1.0 ))
print total

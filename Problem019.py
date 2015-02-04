#!/usr/bin/env python

from datetime import date

sundays = 0
for y in xrange(1901,2001):
	for m in xrange(1,13):
		if date(y,m,1).weekday() == 6:
			sundays += 1
print sundays

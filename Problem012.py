#!/usr/bin/env python

from EulerTools import number_of_divisors, polygonal

t = 1
while number_of_divisors(polygonal(3,t)) < 500:
	t += 1
print polygonal(3,t)


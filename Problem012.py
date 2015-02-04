#!/usr/bin/env python

from EulerTools import number_of_divisors, triangle

t = 1
while number_of_divisors(triangle(t)) < 500:
	t += 1
print triangle(t)


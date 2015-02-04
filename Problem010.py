#!/usr/bin/env python

from EulerTools import next_prime

p = next_prime(1)
total = 0
while p < 2000000:
	total += p
	p = next_prime(p)
print total


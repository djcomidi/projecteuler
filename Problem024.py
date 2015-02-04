#!/usr/bin/env python

from EulerTools import fac
from math import ceil

# starting from index 0, so millionth perm has index 999999
n = 10**6 - 1
s = list("0123456789")
perm = ""
while len(perm) < 10:
	d = fac(len(s)-1)
	pos, n = divmod(n,d)
	perm += s[pos]
	s.remove(perm[-1])
print perm

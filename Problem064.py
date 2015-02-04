#!/usr/bin/env python

from EulerTools import is_square

def get_period(n):
	a, b, c = int(n**0.5), 1, int(n**0.5)
	confracs = []
	while not (a,b,c) in confracs:
		confracs.append((a,b,c))
		newb = (n-c**2)//b
		newa = int((n**0.5+c)/newb)
		newc = abs(c-newb*newa)
		a, b, c = newa, newb, newc
	return len(confracs)-confracs.index((a,b,c))

count_odd = 0
for n in xrange(2,10001):
	if not is_square(n):
		count_odd += get_period(n) & 1
print count_odd
#!/usr/bin/env python

from EulerTools import next_prime

def get_confracs(n):
	a, b, c = int(n**0.5), 1, int(n**0.5)
	confracs = []
	while not (a,b,c) in confracs:
		confracs.append((a,b,c))
		newb = (n-c**2)//b
		newa = int((n**0.5+c)/newb)
		newc = abs(c-newb*newa)
		a, b, c = newa, newb, newc
	index = confracs.index((a,b,c))
	return [cf[0] for cf in confracs[:index]], [cf[0] for cf in confracs[index:]]

def get_term(start,reps,t):
	if t <= len(start):	return start[t-1]
	else:				return reps[(t-len(start)-1)%len(reps)]

def get_frac(n,i):
	start, reps = get_confracs(n)
	nom, denom = get_term(start,reps,i), 1
	while i > 1:
		i -= 1
		t = get_term(start,reps,i)
		nom, denom = denom + t*nom, nom
	return nom, denom

def find_x(D):
	i = 0
	while True:
		i += 1
		x, y = get_frac(D,i)
		if x**2-D*y**2 == 1:
			break
	return x

max_x, min_D = 0, 0
p = 2
while p < 1000:
	x = find_x(p)
	if x > max_x:
		max_x, min_D = x, p
	p = next_prime(p)
print "min D:", min_D
print "max x:", max_x

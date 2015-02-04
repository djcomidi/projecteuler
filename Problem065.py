#!/usr/bin/env python

def get_part(n):
	if n == 1: return 2
	if n%3 == 0: return 2*(n//3)
	else: return 1

def get_term(n):
	nom, denom = get_part(n), 1
	while n > 1:
		n -= 1
		p = get_part(n)
		nom, denom = p*nom+denom, nom
	return nom, denom

nom, denom = get_term(100)
print sum( map( int, list(str(nom)) ) )

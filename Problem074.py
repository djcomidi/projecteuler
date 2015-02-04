#!/usr/bin/env python

from EulerTools import fac

FACS = [ int(fac(i)) for i in xrange(10) ]
memochains = {}

def sum_fac_digits(n):
	return sum( FACS[int(c)] for c in str(n) )

def make_key(n):
	return ''.join( sorted( str(n).replace('0','1') ) )

def chain_length(n):
	key = make_key(n)
	if key in memochains: return memochains[key]
	chain = []
	while (not n in chain) and (len(chain) <= 60):
		chain.append(n)
		n = sum_fac_digits(n)
	memochains[key] = len(chain)
	return len(chain)

chain_count = 0
for n in xrange(1,10**6):
	if chain_length(n) == 60:
		chain_count += 1
print chain_count

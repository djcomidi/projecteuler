#!/usr/bin/env python

from EulerTools import polygonal

# collect all polygonals in range
fourdigits = []
beginnings, endings = set(), set()
for i in [3,4,5,6,7,8]:
	row = []
	n = 1
	p = polygonal(i,n)
	while p < 10000:
		n += 1
		p = polygonal(i,n)
		if p < 1000: continue
		row.append(p)
		beginnings.add( p//100 )
		endings.add( p%100 )
	fourdigits.append(row)

# make sure every polygonal can be part of a chain
commons = beginnings & endings
for i in xrange(6):
	fourdigits[i] = filter( lambda d: d%100 in commons and d//100 in commons, fourdigits[i] )

# recursively look for chain
def find_chain(rows,terms):
	if len(rows) == 0:
		for p in fourdigits[5]:
			find_chain([5],[p])
	elif len(rows) == 6:
		if terms[5]%100 == terms[0]//100:
			print zip( rows, terms )
			print sum(terms)
	else:
		for r in set(range(6))-set(rows):
			for p in fourdigits[r]:
				if terms[-1]%100 == p//100:
					find_chain(rows+[r],terms+[p])
find_chain([],[])

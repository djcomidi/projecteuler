#!/usr/bin/env python

def find_rings(N,ring=""):
	if ring == "": return find_rings(N,"0"*N)
	if ring[-N:] in ring[:-1]: return 0
	if len(ring) == 2**N:
		if any( ring[-i:]+ring[:N-i] in ring for i in xrange(N) ):
			return 0
		return int(ring,2)
	total = 0
	for c in "01":
		total += find_rings(N,ring+c)
	return total

print find_rings(5)

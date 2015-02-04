#!/usr/bin/env python

from EulerTools import is_prime, next_prime

sequences = {}
p = next_prime(10**3)
while p < 10**4:
	key = ''.join(sorted(str(p)))
	if not key in sequences:
		sequences[key] = [int(p)]
	else:
		sequences[key].append(int(p))
	p = next_prime(p)

for primes in sorted(sequences.values()):
	size = len(primes)
	if size < 3: continue
	for a in xrange(size):
		for b in xrange(a+1,size):
			pA, pB, pC = primes[a], primes[b], 2*primes[b] - primes[a]
			if pC in primes:
				print "%d%d%d" % ( pA, pB, pC )

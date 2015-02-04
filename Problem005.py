#!/usr/bin/env python

from EulerTools import mul, prime_factors_compact

result = {}
for n in xrange(2,21):
	exps = prime_factors_compact(n)
	for p in exps.keys():
		result[p] = max( result.get(p,0), exps[p] )
print reduce( mul, [ item[0]**item[1] for item in result.items() ], 1 )

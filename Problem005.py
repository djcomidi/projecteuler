#!/usr/bin/env python

from EulerTools import get_prime_factors_dict
from operator import mul

result = {}
for n in xrange(2,21):
	exps = get_prime_factors_dict(n)
	for p in exps.keys():
		result[p] = max( result.get(p,0), exps[p] )
print reduce( mul, [ item[0]**item[1] for item in result.items() ], 1 )

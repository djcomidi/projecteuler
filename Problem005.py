from operator import mul
from functools import reduce

from EulerTools import prime_factors_dict

exps = {}
for n in range(2, 21):
    pfd = prime_factors_dict(n)
    for p in pfd:
        exps[p] = max(exps.get(p, 0), pfd[p])
factors = [b ** exps[b] for b in exps]
product = reduce(mul, factors, 1)
print(product)

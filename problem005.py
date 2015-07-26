from operator import mul
from functools import reduce

from tools.euler import prime_factors_exps

exps = {}
for n in range(2, 21):
    for p, e in prime_factors_exps(n):
        exps[p] = max(exps.get(p, 0), e)
factors = [b ** exps[b] for b in exps]
product = reduce(mul, factors, 1)
print(product)

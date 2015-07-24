from gmpy2 import next_prime
from functools import reduce
from operator import mul

from EulerTools import prime_factors_dict

LIMIT = 4 * 10 ** 6
factors = [2]
while 3 ** (len(factors)) < 2 * LIMIT:
    factors.append(int(next_prime(factors[-1])))
minn = 2 ** 64
for i in range(1, 4):
    nFactors = factors[:-i]
    n = reduce(mul, nFactors, 1)
    maxProd = reduce(mul, factors[-i:], 1)
    for x in range(1, maxProd):
        exps = list(prime_factors_dict(n * x).values())
        t = reduce(mul, [2 * e + 1 for e in exps], 1)
        if t >= 2 * LIMIT:
            if n * x < minn:
                minn = min(n * x, minn)
                break

print(minn)

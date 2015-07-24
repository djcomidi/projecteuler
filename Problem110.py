from EulerTools import mul
from EulerTools import next_prime
from EulerTools import prime_factors_dict

LIMIT = 4 * 10 ** 6
factors = [2]
while 3 ** (len(factors)) < 2 * LIMIT:
    factors.append(int(next_prime(factors[-1])))
minn = 2 ** 64
for i in xrange(1, 4):
    nFactors = factors[:-i]
    n = reduce(mul, nFactors, 1)
    maxProd = reduce(mul, factors[-i:], 1)
    for x in xrange(1, maxProd):
        arr = [2 * e + 1 for e in prime_factors_dict(n * x).values()]
        t = reduce(mul, arr, 1)
        if t >= 2 * LIMIT:
            if n * x < minn:
                minn = min(n * x, minn)
                break

print minn

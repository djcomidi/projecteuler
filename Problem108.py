from gmpy2 import next_prime
from functools import reduce
from operator import mul

from EulerTools import prime_factors_exps

LIMIT = 1000
e = 1
while 3 ** (e + 1) < 2 * LIMIT:
    e += 1
factors = [2]
for i in range(e):
    factors.append(int(next_prime(factors[-1])))
minn = 2 ** 31
while len(factors) > 2:
    factors[-1] -= 1
    if factors[-1] == 1:
        factors = factors[:-1]
    n = reduce(mul, factors, 1)
    exps = [t[1] for t in prime_factors_exps(n)]
    t = reduce(mul, [2 * e + 1 for e in exps], 1)
    if t >= 2 * LIMIT:
        minn = min(n, minn)
print(minn)

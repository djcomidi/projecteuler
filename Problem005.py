from EulerTools import mul
from EulerTools import prime_factors_dict

result = {}
for n in xrange(2, 21):
    for p, e in prime_factors_dict(n).items():
        result[p] = max(result.get(p, 0), e)
print reduce(mul, [item[0] ** item[1] for item in result.items()], 1)

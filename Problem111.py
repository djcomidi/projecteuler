from itertools import product, permutations

from EulerTools import is_prime

NUMBERS = "0123456789"
MAXLEN = 10
M, N, S = [0] * 10, [0] * 10, [0] * 10
for repDigit in NUMBERS:
    d, t = int(repDigit), MAXLEN
    while M[d] == 0:
        t -= 1
        arr = set()
        others = set(NUMBERS) - set(repDigit)
        for other in product(others, repeat=MAXLEN - t):
            permSource = repDigit * t + ''.join(other)
            for perm in set(permutations(permSource)):
                if perm[0] == '0':
                    continue
                p = int(''.join(perm))
                if is_prime(p):
                    arr.add(p)
        if len(arr) > 0:
            M[d], N[d], S[d] = t, len(arr), sum(arr)

for i in xrange(10):
    print i, M[i], '\t', N[i], '\t', S[i]
print sum(S)

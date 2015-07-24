from gmpy2 import is_prime
from itertools import product, permutations

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

for i in range(10):
    message = "%d %2d %2d %d" % (i, M[i], N[i], S[i])
    print(message)
total = sum(S)
print(total)

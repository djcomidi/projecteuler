from gmpy2 import is_prime
from itertools import permutations

maxp = 0
for perm in permutations("7654321"):
    p = int(''.join(perm))
    if is_prime(p) and ''.join(sorted(str(p))) == "1234567":
        maxp = max(maxp, p)
print(maxp)

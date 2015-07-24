from itertools import permutations

from EulerTools import is_prime

maxp = 0
for perm in permutations("7654321"):
    p = int(''.join(perm))
    if is_prime(p) and ''.join(sorted(str(p))) == "1234567":
        maxp = max(maxp, p)
print maxp

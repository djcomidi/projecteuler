from gmpy2 import is_prime
from itertools import permutations


def count_valids(s, minp=1):
    if len(s) == 0:
        return 1
    nvalids = 0
    for i in range(1, len(s) + 1):
        p = int(s[:i])
        if p > minp and is_prime(p):
            nvalids += count_valids(s[i:], p)
    return nvalids


valids = 0
for perm in permutations("123456789"):
    if perm[-1] in [2, 4, 6, 8]:
        continue
    valids += count_valids(''.join(perm))
print(valids)

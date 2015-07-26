from gmpy2 import is_prime
from gmpy2 import next_prime

LIMIT = 10 ** 6


def has_multiple(prime, d):
    sprime = str(prime)
    if d == 0:
        return sprime[:-1].count('0') > 2
    if d == 1:
        return sprime[:-1].count('1') > 2
    if d == 2:
        return sprime[:-1].count('2') > 2
    return False


masks = [[], [], []]
p = 2
while p < LIMIT:
    for i in range(3):
        if has_multiple(p, i):
            masks[i].append(p)
    p = next_prime(p)

min_prime = LIMIT
for i in range(3):
    for p in masks[i]:
        s = str(p)
        count = 0
        for c in "0123456789"[i:]:
            if is_prime(int(s.replace(str(i), c))):
                count += 1
        if count == 8:
            print(p)

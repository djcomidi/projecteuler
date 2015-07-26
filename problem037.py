from gmpy2 import is_prime
from gmpy2 import next_prime


def valid_prime(p):
    s = str(p)
    for i in range(1, len(s)):
        if not is_prime(int(s[:i])):
            return False
        if not is_prime(int(s[i:])):
            return False
    return True


p, total = 7, 0
for t in range(11):
    p = next_prime(p)
    while not valid_prime(p):
        p = next_prime(p)
    total += p
print(total)

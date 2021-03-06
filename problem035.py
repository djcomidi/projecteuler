from gmpy2 import is_prime
from gmpy2 import next_prime


def is_circ_prime(p):
    s = str(p)
    for i in range(1, len(s)):
        if not is_prime(int(s[i:] + s[:i])):
            return False
    return True


p = 2
circ_primes = set()
while p < 10 ** 6:
    if is_circ_prime(p):
        circ_primes.add(p)
    p = next_prime(p)
result = len(circ_primes)
print(result)

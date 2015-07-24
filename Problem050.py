from EulerTools import is_prime
from EulerTools import next_prime

LIMIT = 10 ** 6

max_terms = 0
max_prime = 0
pStart = 2
while pStart < LIMIT:
    primes = [pStart]
    while sum(primes) < LIMIT:
        if is_prime(sum(primes)) and len(primes) > max_terms:
            max_terms, max_prime = len(primes), sum(primes)
        primes.append(next_prime(primes[-1]))
    pStart = next_prime(pStart)

print max_terms, max_prime

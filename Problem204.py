from gmpy2 import next_prime


def find_hamming(hamming, primes, limit):
    if hamming > limit:
        return 0
    total = 1
    for p in primes:
        total += find_hamming(hamming * p, primes[primes.index(p):], limit)
    return total


theprimes, p = [], 2
while p < 100:
    theprimes.append(p)
    p = next_prime(p)
result = find_hamming(1, theprimes, 10 ** 9)
print(result)

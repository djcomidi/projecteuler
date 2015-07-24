def find_hamming(hamming, primes, limit):
    if hamming > limit:
        return 0
    total = 1
    for p in primes:
        total += find_hamming(hamming * p, primes[primes.index(p):], limit)
    return total


PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
PRIMES += [61, 67, 71, 73, 79, 83, 89, 97]
print find_hamming(1, PRIMES, 10 ** 9)

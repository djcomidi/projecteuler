from EulerTools import next_prime

LIMIT = 10 ** 8
print "caching primes takes the longest :("
primes = list()
p = 2
while p <= LIMIT // 2:
    primes.append(p)
    p = next_prime(p)

print "searching..."
total = 0
i, j = 0, len(primes) - 1
while i <= j:
    while primes[i] * primes[j] >= LIMIT:
        j -= 1
    total += j - i + 1
    i += 1
print total

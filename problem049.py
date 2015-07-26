from gmpy2 import next_prime

sequences = {}
p = next_prime(10 ** 3)
while p < 10 ** 4:
    key = ''.join(sorted(str(p)))
    if key not in sequences:
        sequences[key] = [int(p)]
    else:
        sequences[key].append(int(p))
    p = next_prime(p)

for primes in sorted(sequences.values()):
    size = len(primes)
    if size < 3:
        continue
    for a in range(size):
        for b in range(a + 1, size):
            pA, pB, pC = primes[a], primes[b], 2 * primes[b] - primes[a]
            if pC in primes:
                message = "%d%d%d" % (pA, pB, pC)
                print(message)

from gmpy2 import is_prime

LIMIT = 10**14
harshards = [1, 2, 3, 4, 5, 6, 7, 8, 9]
primes = []

while len(harshards) > 0:
    h = harshards.pop(0)
    sd = sum(int(c) for c in str(h))
    for x in range(10):
        t = 10 * h + x
        if is_prime(t) and is_prime(h // sd):
            primes.append(t)
        if t < (LIMIT // 10) and t % (sd + x) == 0:
            harshards.append(t)

print(sum(primes))

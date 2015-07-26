from gmpy2 import next_prime

N, K = 20000000, 15000000


def primes_in_fac(prime, n):
    m, e = 0, 1
    while prime ** e <= n:
        m += n // (prime ** e)
        e += 1
    return m


sumfacs, p = 0, 2
while p <= N:
    pifn = primes_in_fac(p, N)
    pifk = primes_in_fac(p, K)
    pifnk = primes_in_fac(p, N - K)
    sumfacs += p * (pifn - pifk - pifnk)
    p = next_prime(p)
print(sumfacs)

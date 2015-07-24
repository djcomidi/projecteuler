# R(n) = (10^n-1)/9 = a*p
# 10^n - 1 = 9*a*p
# 10^n == 1 mod 9*p

from EulerTools import next_prime

primes = []
p = 1
while len(primes) < 40:
    p = next_prime(p)
    if pow(10, 10 ** 9, 9 * p) == 1:
        primes.append(p)
print sum(primes)

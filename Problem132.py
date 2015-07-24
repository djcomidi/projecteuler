from gmpy2 import next_prime

# R(n) = (10^n-1)/9 = a*p
# 10^n - 1 = 9*a*p
# 10^n == 1 mod 9*p

primes = []
p = 1
while len(primes) < 40:
    p = next_prime(p)
    if pow(10, 10 ** 9, 9 * p) == 1:
        primes.append(p)
total = sum(primes)
print(total)

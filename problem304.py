from gmpy2 import next_prime

# A large fibonacci calculator can be found at:
# "8 Quick exact computation of (...) Fibonacci numbers (third strike)"
# https://web.archive.org/web/20120614144609/+
#   http://en.literateprograms.org/Fibonacci_numbers_%28Python%29

LIMIT = 1234567891011
fibs = {0: 0, 1: 1}


def fib(n):
    if n in fibs:
        return fibs[n]
    halfdown, half, halfup = (n - 1) // 2, n // 2, (n + 1) // 2
    if n & 1 == 0:
        fibs[n] = ((2 * fib(half - 1)) + fib(half)) * fib(half)
    else:
        fibs[n] = (fib(halfdown) ** 2) + (fib(halfup) ** 2)
    fibs[n] %= LIMIT
    return fibs[n]


p = 10 ** 14
total = 0
for n in range(1, 10 ** 5 + 1):
    p = next_prime(p)
    total += fib(p)
result = total % LIMIT
print(result)

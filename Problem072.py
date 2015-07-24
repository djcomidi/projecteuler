from gmpy2 import next_prime

LIMIT = 10 ** 6
denoms = list(range(LIMIT + 1))
denoms[1] = 0
p = 2
while p < LIMIT:
    for k in range(p, LIMIT, p):
        denoms[k] = (denoms[k] * (p - 1)) // p
    p = next_prime(p)
result = sum(denoms)
print(result)

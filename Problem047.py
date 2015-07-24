from EulerTools import next_prime

LIMIT = 10 ** 6
prime_count = [0] * LIMIT
p = 2
while p < LIMIT:
    for k in xrange(p, LIMIT, p):
        prime_count[k] += 1
    p = next_prime(p)

n = 1
while n < LIMIT - 4 and prime_count[n:n + 4] != [4, 4, 4, 4]:
    n += 1
print n

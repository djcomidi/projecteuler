LIMIT = 10 ** 10

n = pow(2, 7830457, LIMIT)
n = (n * 28433) % LIMIT
n += 1
print(n)

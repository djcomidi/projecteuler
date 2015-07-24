LIMIT = 10 ** 7

divisors = [0, 1] + [2] * LIMIT
sols = 0
for d in range(2, LIMIT):
    for k in range(d + d, LIMIT, d):
        divisors[k] += 1
    if divisors[d] == divisors[d - 1]:
        sols += 1
print(sols)

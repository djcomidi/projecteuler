def funca(x, n):
    return 3 * n ** 2 + 2 * n * x - x ** 2

LIMIT = 10 ** 6
ways = [0] * LIMIT

for x in range(1, LIMIT):
    n = x // 3
    while True:
        val = funca(x, n)
        if val >= LIMIT:
            break
        if val >= 0:
            ways[funca(x, n)] += 1
        n += 1

result = ways.count(10)
print(result)

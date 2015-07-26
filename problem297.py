LIMIT = 10 ** 17
FIBS = [1, 2]
while FIBS[-1] < LIMIT:
    FIBS.append(FIBS[-2] + FIBS[-1])


def count_terms(n, cache=None):
    if not cache:
        cache = {1: 0}
    if n not in cache:
        fib = max([f for f in FIBS if f < n])
        vala = count_terms(n - fib, cache)
        valb = count_terms(fib, cache)
        cache[n] = n - fib + vala + valb
    return cache[n]


result = count_terms(LIMIT)
print(result)

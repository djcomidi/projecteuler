def find_fib(n, modulo, fibs=None):
    if not fibs:
        fibs = {0: 0, 1: 1, 2: 1}
    if n not in fibs:
        if n & 1 == 1:
            fibs[n] = find_fib(n - 1, modulo) % modulo
        else:
            print n
            a = find_fib(n // 2 - 1, modulo, fibs)
            b = find_fib(n // 2, modulo, fibs)
            c = find_fib(n // 2 + 1, modulo, fibs)
            fibs[n] = ((a * b) + (b * c)) % modulo
    return fibs[n]


print find_fib(10 ** 14, 10 ** 13)

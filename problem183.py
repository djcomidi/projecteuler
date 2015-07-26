from math import log10


def calc_m(n):
    mmax, p = 1, 0.0
    for m in range(1, n // 2 + 1):
        t = m * (log10(n) - log10(m))
        if t > p:
            p, mmax = t, m
    return mmax


def is_terminating(n, d):
    checks = set()
    q, r = 0, 0
    while True:
        q, r = divmod(n, d)
        if (q, r) in checks:
            break
        checks.add((q, r))
        n = r * 10
    return (q, r) == (0, 0)


def calc_d(n):
    if is_terminating(n, calc_m(n)):
        return -n
    else:
        return n


total = sum(calc_d(n) for n in range(5, 10001))
print(total)

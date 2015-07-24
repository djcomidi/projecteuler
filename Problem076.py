from EulerTools import Memoize


@Memoize
def p(k, n):
    if k > n:
        val = 0
    elif k == n:
        val = 1
    else:
        val = p(k + 1, n)
        val += p(k, n - k)
    return val


result = p(1, 100) - 1
print(result)

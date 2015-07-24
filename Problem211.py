from EulerTools import is_square

MAXN = 64 * 10 ** 6
arr = [0] + [1] * MAXN
total = 1
n = 1
while n + 1 < MAXN:
    n += 1
    k, n2 = n, n ** 2
    while k < MAXN:
        arr[k] += n2
        k += n
    if is_square(arr[n]):
        total += n
print total

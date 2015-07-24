def func_u(r, k):
    return (900 - 3 * k) * r ** (k - 1)


def func_s(r, n):
    return sum(func_u(r, k) for k in xrange(1, n + 1))


TARGET = -600000000000
N = 5000
rr, t = 1, 1.0

while rr < 10 ** 13:
    rr, t, i = 10 * rr, 10.0 * t, 0
    while func_s((rr + i + 1) / t, N) > TARGET:
        i += 1
    rr += i
print "%.12f" % (rr / t)

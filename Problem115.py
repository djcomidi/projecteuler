from EulerTools import Memoize


@Memoize
def fill_count(minw, size):
    ways = 1
    for w in xrange(minw, size + 1):
        for pos in xrange(size - w + 1):
            ways += fill_count(minw, size - (pos + w) - 1)
    return ways


n = 1
while fill_count(50, n) < 10 ** 6:
    n += 1
print n, fill_count(50, n)

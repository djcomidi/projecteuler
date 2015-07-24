from EulerTools import Memoize


@Memoize
def fill_count(minw, size):
    ways = 1
    for w in xrange(minw, size + 1):
        for pos in xrange(size - w + 1):
            ways += fill_count(minw, size - (pos + w) - 1)
    return ways


print fill_count(3, 50)

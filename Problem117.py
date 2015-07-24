from EulerTools import Memoize


@Memoize
def fill_count(size):
    ways = 1
    for w in [2, 3, 4]:
        for pos in xrange(size - w + 1):
            ways += fill_count(size - (pos + w))
    return ways


print fill_count(50)

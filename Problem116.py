from EulerTools import Memoize


@Memoize
def fill_count(singlew, size):
    ways = 0
    for pos in xrange(size - singlew + 1):
        ways += 1 + fill_count(singlew, size - (pos + singlew))
    return ways


print sum(fill_count(w, 50) for w in [2, 3, 4])

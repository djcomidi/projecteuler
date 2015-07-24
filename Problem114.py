from EulerTools import Memoize


@Memoize
def fill_count(minw, size):
    ways = 1
    for w in range(minw, size + 1):
        for pos in range(size - w + 1):
            ways += fill_count(minw, size - (pos + w) - 1)
    return ways


result = fill_count(3, 50)
print(result)

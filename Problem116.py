from EulerTools import Memoize


@Memoize
def fill_count(singlew, size):
    ways = 0
    for pos in range(size - singlew + 1):
        ways += 1 + fill_count(singlew, size - (pos + singlew))
    return ways


total = sum(fill_count(w, 50) for w in [2, 3, 4])
print(total)

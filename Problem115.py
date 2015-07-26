from functools import lru_cache


@lru_cache(maxsize=256)
def fill_count(minw, size):
    ways = 1
    for w in range(minw, size + 1):
        for pos in range(size - w + 1):
            ways += fill_count(minw, size - (pos + w) - 1)
    return ways


n = 1
while fill_count(50, n) < 10 ** 6:
    n += 1
message = "n=%d fillcount=%d" % (n, fill_count(50, n))
print(message)

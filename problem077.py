from gmpy2 import next_prime

from functools import lru_cache


@lru_cache(maxsize=512)
def get_ways(num, minp=2):
    if num == 0:
        return 1
    ways, p = 0, minp
    while p <= num:
        ways += get_ways(num - p, max(minp, p))
        p = next_prime(p)
    return ways


n = 1
while get_ways(n) < 5000:
    n += 1
message = "value=%d  ways=%d" % (n, get_ways(n))
print(message)

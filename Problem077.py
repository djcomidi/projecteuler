from gmpy2 import next_prime

from EulerTools import Memoize


@Memoize
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
message = "%d, %d" % (n, get_ways(n))
print(message)

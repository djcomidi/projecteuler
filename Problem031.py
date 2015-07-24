from EulerTools import Memoize

# default recursionlimit (=10**3) gives a
# RuntimeError: maximum recursion depth exceeded
import sys

sys.setrecursionlimit(10 ** 4)

COINS = [1, 2, 5, 10, 20, 50, 100, 200]


@Memoize
def pay(rest, mincoin=1):
    if rest == 0:
        return 1
    ways = 0
    for coin in [c for c in COINS if mincoin <= c <= rest]:
        ways += pay(rest - coin, max(mincoin, coin))
    return ways


payments = pay(200)
print(payments)

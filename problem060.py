from gmpy2 import is_prime
from gmpy2 import next_prime

LIMIT = 10 ** 4


def make_prime(pa, pb):
    return is_prime(int(str(pa) + str(pb)))


PRIMES = []
p = 2
while p < LIMIT:
    PRIMES.append(p)
    p = next_prime(p)


def find_five(arr):
    for i in range(len(arr) - 1):
        if not make_prime(arr[-1], arr[i]):
            return
        if not make_prime(arr[i], arr[-1]):
            return
    if len(arr) == 5:
        message = "%s %d" % ([int(x) for x in arr], int(sum(arr)))
        print(message)
    else:
        for p in [x for x in PRIMES if x > arr[-1]]:
            find_five(arr + [p])


for p in [2, 3, 5, 7, 11, 13]:
    find_five([p])

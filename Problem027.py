from EulerTools import is_prime
from EulerTools import next_prime


def count_func(a, b):
    n = 0
    while is_prime(n ** 2 + a * n + b):
        n += 1
    return n


max_count, max_prod, pB = 0, 0, 2
while pB < 1000:
    pA = 2
    while pA < 1000:
        for k in [-1, 1]:
            c = count_func(k * pA, pB)
            if c > max_count:
                max_count = c
                max_prod = k * pA * pB
        pA = next_prime(pA)
    pB = next_prime(pB)
print max_prod

from gmpy2 import gcd

LOWRANGE, HIGHRANGE = 1.0 / 3, 1.0 / 2
t = 0
for n in range(4, 12001):
    for i in range(n // 3, n // 2 + 1):
        ratio = (1.0 * i) / n
        if gcd(n, i) == 1 and LOWRANGE < ratio < HIGHRANGE:
            t += 1
print(t)

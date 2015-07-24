from gmpy2 import fac

total = 0
for n in range(3, fac(9)):
    sumfacs, t = 0, n
    while t > 0:
        sumfacs, t = sumfacs + fac(t % 10), t // 10
    if n == sumfacs:
        total += n
print(total)

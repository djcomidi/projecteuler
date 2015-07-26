from gmpy2 import is_prime


def funca(num):
    r, t = 0, 0
    while True:
        r, t = (10 * r + 1) % num, t + 1
        if r == 0:
            break
    return t


composites = [91, 259, 451, 481]
n = composites[-1]
while len(composites) < 25:
    n += 2
    while is_prime(n) or n % 5 == 0:
        n += 2
    if (n - 1) % funca(n) == 0:
        composites.append(n)
total = sum(composites)
print(total)

from gmpy2 import is_prime

LIMIT = 5 * 10 ** 7
total = 0
for n in range(2, LIMIT + 1):
    if is_prime(2 * n ** 2 - 1):
        total += 1
        # message = "{0}\t{1}".format(total, n)
        # print(message)
print(total)

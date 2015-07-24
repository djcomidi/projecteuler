from gmpy2 import is_square

from EulerTools import sigma

print("Sit back and watch the valid solutions scroll by... slowly :(")
MAXN = 64 * 10 ** 6
total = 0
for n in range(1, MAXN+1):
    if is_square(sigma(2, n)):
        total += n
        message = "{0}\t{1}".format(n, total)
        print(message)
print(total)

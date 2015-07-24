from EulerTools import fac


def sum_digits_fac(num):
    return sum(fac(i) for i in map(int, list(str(num))))


total = 0
for n in xrange(3, fac(9)):
    if n == sum_digits_fac(n):
        total += n
print total

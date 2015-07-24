from EulerTools import is_square


def find_root_digits(num, t):
    digits = []
    p = 0
    while len(digits) < t:
        x = 0
        while (10 * p + x + 1) * (x + 1) < num:
            x += 1
        digits.append(x)
        num = (num - ((10 * p + x) * x)) * 100
        p = 10 * p + 2 * x
    return digits


total = 0
for n in xrange(1, 100):
    if is_square(n):
        continue
    total += sum(find_root_digits(n, 100))
print total

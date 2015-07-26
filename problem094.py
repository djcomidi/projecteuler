from gmpy2 import is_square


def has_int_area(a, b, c):
    s = (a + b + c) // 2
    return is_square(s * (s - a) * (s - b) * (s - c))


total = 0
for side in range(3, 166666667, 2):
    if has_int_area(side, side, side - 1):
        total += 3 * side - 1
        message = "%9d %9d %9d %d" % (side, side, side - 1, total)
        print(message)
    if has_int_area(side, side, side + 1):
        total += 3 * side + 1
        message = "%9d %9d %9d %d" % (side, side, side + 1, total)
        print(message)
print(total)

#!/usr/bin/env python

from EulerTools import is_square


def has_int_area(a, b, c):
    s = (a + b + c) // 2
    return is_square(s * (s - a) * (s - b) * (s - c))


total = 0
for side in xrange(3, 333333334, 2):
    if has_int_area(side, side, side - 1):
        total += 3 * side - 1
        print "%9d %9d %9d %d" % (side, side, side - 1, total)
    if has_int_area(side, side, side + 1):
        total += 3 * side + 1
        print "%9d %9d %9d %d" % (side, side, side + 1, total)
print total

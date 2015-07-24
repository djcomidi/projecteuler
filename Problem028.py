def get_sum_corners(n):
    lowest = (n - 2) * (n - 1) + 1
    t = (n - 1) // 2
    return 4 * (lowest + t * 3)


sum_diagonals = 1
for n in xrange(3, 1002, 2):
    sum_diagonals += get_sum_corners(n)
print sum_diagonals

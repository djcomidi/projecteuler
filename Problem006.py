LIMIT = 100
sum_of_squares = sum([x ** 2 for x in xrange(1, LIMIT + 1)])
square_of_sums = sum(xrange(1, LIMIT + 1)) ** 2
print square_of_sums - sum_of_squares

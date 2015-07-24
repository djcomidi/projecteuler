LIMIT = 100
sum_of_squares = sum([x ** 2 for x in range(1, LIMIT + 1)])
square_of_sums = sum(range(1, LIMIT + 1)) ** 2
difference = square_of_sums - sum_of_squares
print(difference)

LIMIT = 1000
set_three = set(range(3, LIMIT, 3))
set_five = set(range(5, LIMIT, 5))
total = sum(set_three | set_five)
print(total)

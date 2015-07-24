LIMIT = 10 ** 10
sol = 0
for i in range(1, 1001):
    sol += pow(i, i, LIMIT)
rest = sol % LIMIT
print(rest)

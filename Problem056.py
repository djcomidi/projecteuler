max_sum = 0
for a in range(1, 100):
    for b in range(1, 100):
        sum_digits = sum(int(t) for t in str(a ** b))
        max_sum = max(max_sum, sum_digits)
print(max_sum)

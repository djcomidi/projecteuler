def sum_digits_power(n, e):
    return sum(d ** e for d in map(int, list(str(n))))


sum_n = 0
for n in range(2, 6 * 9 ** 5 + 1):
    if n == sum_digits_power(n, 5):
        sum_n += n
print(sum_n)

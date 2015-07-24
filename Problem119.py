def sum_digits(num):
    return sum([int(x) for x in str(num)])


arr = set()
for n in range(2, 1000):
    for t in range(1000):
        if n ** t < 10:
            continue
        if n ** t > 10 ** 15:
            break
        if sum_digits(n ** t) == n:
            arr.add(n ** t)
result = sorted(arr)[-1]
print(result)

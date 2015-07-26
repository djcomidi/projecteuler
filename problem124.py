LIMIT = 10 ** 5
rads = [1] * (LIMIT + 1)
for p in range(2, LIMIT + 1):
    if rads[p] > 1:
        continue
    for k in range(p, LIMIT + 1, p):
        rads[k] *= p
radList = sorted([(rads[i], i) for i in range(1, LIMIT + 1)])
result = radList[10 ** 4 - 1][1]
print(result)

# when printing (a, rmax) during brute-force, I noticed:
# if a == odd: rmax = a*(a-1)
# if a == even: rmax = a*(a-2)

total = 0
for a in range(3, 1001):
    if a & 1 == 1:
        total += a * (a - 1)
    else:
        total += a * (a - 2)
print(total)

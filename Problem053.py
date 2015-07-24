from gmpy2 import bincoef

count_greater = 0
for n in range(1, 101):
    for r in range(n):
        if bincoef(n, r) > 10 ** 6:
            count_greater += 1
print(count_greater)

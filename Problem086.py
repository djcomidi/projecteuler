from gmpy2 import is_square

count = 0
m = 0
while count < 10 ** 6:
    m += 1
    for bc in range(2, 2 * m + 1):
        if is_square(m ** 2 + bc ** 2):
            count += min(bc, m + 1) - (bc + 1) // 2
print(m)

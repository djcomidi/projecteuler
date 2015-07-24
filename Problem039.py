from gmpy2 import is_square

perims = [0] * 1001

for a in range(1, 400):
    for b in range(a + 1, 400):
        c2 = a ** 2 + b ** 2
        if not is_square(c2):
            continue
        c = int(c2 ** 0.5)
        p = a + b + c
        if p <= 1000:
            perims[p] += 1

idx = perims.index(max(perims))
print(idx)

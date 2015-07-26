from gmpy2 import is_square

b = [15, 85, 493]
t = 0
while t < 10 ** 12:
    b.append(7 * b[-1] - 7 * b[-2] + b[-3])
    bval = 1 + 8 * b[-1] * (b[-1] - 1)
    if is_square(bval):
        t = (int(bval ** 0.5) + 1) // 2
last = b[-1]
print(last)

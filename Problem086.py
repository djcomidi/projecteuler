from EulerTools import is_square

count = 0
M = 0
while count < 10 ** 6:
    M += 1
    for bc in xrange(2, 2 * M + 1):
        if is_square(M ** 2 + bc ** 2):
            count += min(bc, M + 1) - (bc + 1) // 2
print M

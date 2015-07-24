# a = m**2 - n**2
# b = 2*m*n
# c = m**2 + n**2
# a+b+c = m**2 - n**2 + 2*m*n + m**2 + n**2 = 2*m**2 + 2*m*n = 2*m*(m+n)
# k(a+b+c) = 2*k*m*(m+n)
MAXLEN = 1500000
lengths = [0] * (MAXLEN + 1)
alltriples = set()
# print lengths
for n in xrange(1, 700):
    for m in xrange(n + 1, 900):
        a, b, c = m ** 2 - n ** 2, 2 * m * n, m ** 2 + n ** 2
        k = 1
        while k * (a + b + c) <= MAXLEN:
            ka, kb, kc = sorted([k * a, k * b, k * c])
            if not (ka, kb, kc) in alltriples:
                alltriples.add((ka, kb, kc))
                lengths[ka + kb + kc] += 1
            k += 1

# print alltriples
print lengths.count(1)

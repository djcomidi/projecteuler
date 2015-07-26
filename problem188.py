a, k, modulo = 1777, 1855, 10 ** 8
e = 1

for i in range(k):
    e = pow(a, e, modulo)
print(e)

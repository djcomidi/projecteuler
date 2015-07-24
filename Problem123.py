from EulerTools import next_prime

p = 1
pN = 0
while True:
    p, pN = next_prime(p), pN + 1
    d, r = divmod((p - 1) ** pN + (p + 1) ** pN, p ** 2)
    if r > 10 ** 10:
        break
print pN, p

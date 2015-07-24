from EulerTools import is_prime

# n^3 + p*n^2 = x^3
# n^2*(n+p) = x^3
# L> n^2 == cube => n is cube (cubeN)
# L> p+n == cubeB => p = cubeB - n = cubeB - cubeN
# a^3-b^3 = (a-b)(a^2+a*b+b^2)
# for p == a^3-b^3 => a-b = 1 => a=b+1

LIMIT = 10 ** 6
total = 0
i = 0
while True:
    i += 1
    p = 1 + 3 * i + 3 * i ** 2
    if p > LIMIT:
        break
    if is_prime(p):
        total += 1
print total

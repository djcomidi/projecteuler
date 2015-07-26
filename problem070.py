from gmpy2 import next_prime

MAXPRIME = 4000
min_ratio = 3.0
min_n = 0
pA = 3
while pA < MAXPRIME:
    pB = next_prime(pA)
    while pB < MAXPRIME:
        n = pA * pB
        if n > 10 ** 7:
            break
        totn = (pA - 1) * (pB - 1)
        if sorted(str(n)) == sorted(str(totn)):
            ratio = (1.0 * n) / totn
            if ratio < min_ratio:
                min_ratio, min_n = ratio, n
        pB = next_prime(pB)
    pA = next_prime(pA)
message = "n=%d ratio=%d" % (min_n, min_ratio)
print(message)

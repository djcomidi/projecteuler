from gmpy2 import next_prime

LIMIT = 10 ** 6
total = 0
p1, p2 = 3, 5
while p2 < LIMIT:
    p1, p2 = p2, next_prime(p2)
    s1, s2 = str(p1), str(p2)
    x, t = LIMIT + p1, ""
    for i in range(len(s1)):
        q = 0
        while (q * p2) % 10 != x % 10:
            q += 1
        x, t = LIMIT + (x - q * p2) // 10, str(q) + t
    total += int(t) * p2
print(total)

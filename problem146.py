from gmpy2 import is_prime

total = 0
for n in range(10, 150 * 10 ** 6, 10):
    if (n % 210) not in [10, 80, 130, 200]:
        continue
    p = n ** 2 + 1
    if not is_prime(p):
        continue
    if [2, 6, 8, 12, 26] == [q for q in range(2, 27, 2) if is_prime(p + q)]:
        total += n
print(total)

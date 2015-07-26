from gmpy2 import is_prime

diagonals_prime = 3
diagonals_total = 5
n = 3
while ((100 * diagonals_prime) / diagonals_total) >= 10:
    n += 2
    lowest = (n - 2) * (n - 1) + 1
    step = n - 1
    for i in range(4):
        if is_prime(lowest + i * step):
            diagonals_prime += 1
    diagonals_total += 4
print(n)

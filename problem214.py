from gmpy2 import is_prime

MAXP = 40 * 10 ** 6
totients = list(range(MAXP + 1))
connections = [0] * (MAXP + 1)
connections[1] = 1
total = 0
for n in range(2, MAXP):
    if is_prime(n):
        for k in range(n, MAXP, n):
            totients[k] = (totients[k] * (n - 1)) // n
    connections[n] = 1 + connections[totients[n]]
    if is_prime(n) and 25 == connections[n]:
        total += n
print(total)

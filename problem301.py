t, total = 0, 0
for n in range(1, 101):
    if n & (2 * n) == 0:
        total += 1
    if n == 2 ** t:
        message = "2^%d -> %d" % (t, total)
        print(message)
        t += 1
print("...")

fibA, fibB, fibN = 1, 2, 1
while fibN < 30:
    fibA, fibB, fibN = fibB, fibA + fibB, fibN + 1
message = "2^%d -> %d" % (fibN, fibB)
print(message)

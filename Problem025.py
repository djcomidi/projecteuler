fibA, fibB, n = 1, 1, 2
while len(str(fibB)) < 1000:
    fibA, fibB, n = fibB, fibA + fibB, n + 1
print(n)

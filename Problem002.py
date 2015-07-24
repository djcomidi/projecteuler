fibA, fibB = 1, 2
total = 0
while fibB < 4000000:
    if fibB & 1 == 0:
        total += fibB
    fibA, fibB = fibB, fibA + fibB
print(total)

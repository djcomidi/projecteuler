from gmpy2 import fib

from EulerTools import is_pandigital

fibA, fibB = 1, 1
fibN = 2
bFound = False
while not bFound:
    while True:
        fibN, fibA, fibB = fibN + 1, fibB, (fibA + fibB) % (10 ** 9)
        if is_pandigital(fibB):
            break
    bFound = is_pandigital(str(fib(fibN))[:9])
print(fibN)

from gmpy2 import fac

digits = [int(t, 10) for t in str(fac(100))]
total = sum(digits)
print(total)

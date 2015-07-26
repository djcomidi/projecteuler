from gmpy2 import fac

w, h = 20, 20
result = fac(w + h) / (fac(w) * fac(h))
print(result)

from tools.euler import is_pandigital

pans = set([])
for a in range(1, 50):
    for b in range(a + 1, 2000):
        c = a * b
        if is_pandigital(str(a) + str(b) + str(c)):
            pans.add(c)
result = sum(pans)
print(result)

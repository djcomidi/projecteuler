from EulerTools import aliquot_sum

amicables = set()

for n in range(4, 10000):
    if n in amicables:
        continue
    m = aliquot_sum(n)
    if m != n == aliquot_sum(m):
        amicables.add(m)
        amicables.add(n)
total = sum(amicables)
print(total)

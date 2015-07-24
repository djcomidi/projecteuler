s = ""
i = 0
while len(s) <= 10 ** 6:
    s += str(i)
    i += 1
prod = 1
for e in xrange(7):
    prod *= int(s[10 ** e])
print prod

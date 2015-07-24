nLow = int(1020304050607080900 ** 0.5)
nHigh = int(1929394959697989900 ** 0.5)
while nLow % 100 != 70:
    nLow += 1
for n in xrange(nLow, nHigh, 100):
    if str(n ** 2)[::2] == "1234567890":
        print n, n ** 2
        break

t, total = 0, 0
for n in xrange(1, 101):
    if n & (2 * n) == 0:
        total += 1
    if n == 2 ** t:
        print "2^%d -> %d" % (t, total)
        t += 1
print "..."

fibA, fibB, fibN = 1, 2, 1
while fibN < 30:
    fibA, fibB, fibN = fibB, fibA + fibB, fibN + 1
print "2^%d -> %d" % (fibN, fibB)

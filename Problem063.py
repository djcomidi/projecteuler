t = 0  # [1-9]**1
for b in xrange(1, 30):
    for a in xrange(0, 10):
        if a == 0 and b == 1:
            continue
        n = a ** b
        if len(str(n)) == b:
            t += 1
            print t, "%d**%d = %d" % (a, b, n)
print t

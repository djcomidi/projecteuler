t = 0
for b in range(1, 30):
    for a in range(0, 10):
        if a == 0 and b == 1:
            continue
        n = a ** b
        if len(str(n)) == b:
            t += 1
            message = "%2d %d**%d=%d" % (t, a, b, n)
            print(message)
print(t)

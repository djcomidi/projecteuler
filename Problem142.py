from EulerTools import is_square

LIMIT = 1000
mids = {}
for a in xrange(1, LIMIT):
    a2 = a ** 2
    for b in xrange(a + 2, LIMIT, 2):
        b2 = b ** 2
        mid = (a2 + b2) // 2
        mids[mid] = mids.get(mid, []) + [a2]
        if len(mids[mid]) == 2:
            z, y, x = sorted([mid, mid - mids[mid][0], mid - mids[mid][1]])
            if not is_square(x + y):
                continue
            if not is_square(x - y):
                continue
            if not is_square(x + z):
                continue
            if not is_square(x - z):
                continue
            if not is_square(y - z):
                continue
            if not is_square(y + z):
                continue
            print x, y, z, x + y + z

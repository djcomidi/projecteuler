LIMIT = 10 ** 6
DRS = []
for n in xrange(LIMIT + 1):
    x = n
    while x > 9:
        x = sum(int(c) for c in str(x))
    DRS.append(x)


def ways(num, minfac, drs, mdrs):
    if num >= LIMIT:
        return
    mdrs[num] = max(mdrs[num], drs)
    for d in xrange(minfac, (LIMIT // num) + 1):
        ways(num * d, max(minfac, d), drs + DRS[d], mdrs)


mdrsLookup = [0] * (LIMIT + 1)
ways(1, 2, 0, mdrsLookup)
print sum(mdrsLookup[2:LIMIT])

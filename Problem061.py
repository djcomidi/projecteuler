from EulerTools import polygonal

# collect all polygonals in range
fourdigits = []
beginnings, endings = set(), set()
for i in [3, 4, 5, 6, 7, 8]:
    row = []
    n = 1
    p = polygonal(i, n)
    while p < 10000:
        n += 1
        p = polygonal(i, n)
        if p < 1000:
            continue
        row.append(p)
        beginnings.add(p // 100)
        endings.add(p % 100)
    fourdigits.append(row)

# make sure every polygonal can be part of a chain
commons = beginnings & endings
for i in range(6):
    newfourdigits = []
    for fd in fourdigits[i]:
        if fd % 100 in commons and fd // 100 in commons:
            newfourdigits.append(fd)
    fourdigits[i] = newfourdigits


# recursively look for chain
def find_chain(rows, terms):
    if len(rows) == 0:
        for prime in fourdigits[5]:
            find_chain([5], [prime])
    elif len(rows) == 6:
        if terms[5] % 100 == terms[0] // 100:
            message = "%s, %d" % (list(zip(rows, terms)), sum(terms))
            print(message)
    else:
        for r in set(range(6)) - set(rows):
            for prime in fourdigits[r]:
                if terms[-1] % 100 == prime // 100:
                    find_chain(rows + [r], terms + [prime])


find_chain([], [])

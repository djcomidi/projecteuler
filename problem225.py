nondivs = []
n = 1
while len(nondivs) != 124:
    n += 2
    t, tVals, isDiv = (1, 1, 1), set(), False
    while not isDiv and t not in tVals:
        tVals.add(t)
        t = (t[1], t[2], sum(t) % n)
        isDiv = t[2] == 0
    if not isDiv:
        nondivs.append(n)
last = nondivs[-1]
print(last)

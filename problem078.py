from tools.euler import polygonal


def get_sign(i):
    return 1 - 2 * (((i - 1) // 2) & 1)


def get_term(i):
    if i & 1 == 1:
        p = (i + 1) // 2
    else:
        p = -(i // 2)
    return polygonal(5, p)


pVals = [1, 1]
while pVals[-1] % 10 ** 6 != 0:
    n = len(pVals)
    t, pVal = 1, 0
    while get_term(t) <= n:
        t, pVal = t + 1, pVal + (get_sign(t) * pVals[n - get_term(t)])
    pVals.append(pVal % 10 ** 7)
result = len(pVals) - 1
print(result)

from EulerTools import polygonal

tN, pN, hN = 285, 165, 143
t, p, h = polygonal(3, tN), polygonal(5, pN), polygonal(6, hN)
while True:
    hN += 1
    h = polygonal(6, hN)
    while p < h:
        pN += 1
        p = polygonal(5, pN)
    while t < p:
        tN += 1
        t = polygonal(3, tN)
    if h == p == t:
        break
print t

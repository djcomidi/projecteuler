from eulertools import is_pandigital

maxs = 0
for k in range(2, 4):
    for n in range(1, 10000):
        s = ''.join(str(n * t) for t in range(1, k))
        if is_pandigital(s):
            maxs = max(maxs, int(s))
print(maxs)

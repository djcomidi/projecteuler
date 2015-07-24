from operator import mul
from functools import reduce

fracs = []
for nom in range(11, 100):
    if nom % 10 == 0:
        continue
    nomT, nomD = divmod(nom, 10)
    for denom in range(nom + 1, 100):
        if denom % 10 == 0:
            continue
        denomT, denomD = divmod(denom, 10)
        if denomD == nomD and nom * denomT == denom * nomT:
            fracs.append((nomT, denomT))
        if denomT == nomD and nom * denomD == denom * nomT:
            fracs.append((nomT, denomD))
        if denomD == nomT and nom * denomT == denom * nomD:
            fracs.append((nomD, denomT))
        if denomT == nomT and nom * denomD == denom * nomD:
            fracs.append((nomD, denomD))
reduceNom = reduce(mul, [f[1] for f in fracs], 1)
reduceDenom = reduce(mul, [f[0] for f in fracs], 1)
result = reduceNom // reduceDenom
print(result)

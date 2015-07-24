collatzes = {1: 1}


def collatz_terms(idx):
    if idx in collatzes:
        return collatzes[idx]
    if idx & 1 == 0:
        following = collatz_terms(idx // 2)
    else:
        following = collatz_terms(3 * idx + 1)
    collatzes[idx] = 1 + following
    return collatzes[idx]


maxterms = 0
maxstart = 0
for n in xrange(1, 1000000):
    terms = collatz_terms(n)
    if terms > maxterms:
        maxterms, maxstart = terms, n
print maxstart

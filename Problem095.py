LIMIT = 10 ** 6

aliquots = [0] * LIMIT
for d in xrange(1, LIMIT):
    for k in xrange(2 * d, LIMIT, d):
        aliquots[k] += d

maxLen, minTerm = 0, 0
for n in xrange(1, LIMIT):
    chain, t = [], n
    while t not in chain:
        chain.append(t)
        t = aliquots[t]
        if t >= LIMIT:
            break
    if t == chain[0] and len(chain) > maxLen:
        maxLen, minTerm = len(chain), min(chain)
print maxLen, minTerm

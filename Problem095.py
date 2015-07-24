LIMIT = 10 ** 6

aliquots = [0] * LIMIT
for d in range(1, LIMIT):
    for k in range(2 * d, LIMIT, d):
        aliquots[k] += d

maxLen, minTerm = 0, 0
for n in range(1, LIMIT):
    chain, t = [], n
    while t not in chain:
        chain.append(t)
        t = aliquots[t]
        if t >= LIMIT:
            break
    if t == chain[0] and len(chain) > maxLen:
        maxLen, minTerm = len(chain), min(chain)
result = "maxLen=%d minTerm=%d" % (maxLen, minTerm)
print(result)

from itertools import product

total = 1
ppdict = {}
for dice in product([1, 2, 3, 4], repeat=9):
    ppdict[sum(dice)] = ppdict.get(sum(dice), 0) + 1
total *= sum(ppdict.values())

ccdict = {}
for dice in product([1, 2, 3, 4, 5, 6], repeat=6):
    ccdict[sum(dice)] = ccdict.get(sum(dice), 0) + 1
total *= sum(ccdict.values())

ppWins = 0
for pp in list(ppdict.keys()):
    for cc in [x for x in list(ccdict.keys()) if x < pp]:
        ppWins += ppdict[pp] * ccdict[cc]
message = "%.7f" % (ppWins / total)
print(message)

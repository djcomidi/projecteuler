from itertools import product

total = 1
pyramidalPete = {}
for dice in product([1, 2, 3, 4], repeat=9):
    pyramidalPete[sum(dice)] = pyramidalPete.get(sum(dice), 0) + 1
total *= sum(pyramidalPete.values())

cubicColin = {}
for dice in product([1, 2, 3, 4, 5, 6], repeat=6):
    cubicColin[sum(dice)] = cubicColin.get(sum(dice), 0) + 1
total *= sum(cubicColin.values())

ppWins = 0
for pp in pyramidalPete.keys():
    for cc in filter(lambda x: x < pp, cubicColin.keys()):
        ppWins += pyramidalPete[pp] * cubicColin[cc]
print "%.7f" % (float(ppWins) / total)

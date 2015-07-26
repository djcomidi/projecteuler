# L(n)=(t_1,..t_k) =>  n distinct laminae that can be formed using t tiles
# N(n)=len(L(n))

LIMIT = 10 ** 6


def find_laminae(tilesused=0, outersize=0, uniques=None):
    if uniques is None:
        uniques = []
    if tilesused > LIMIT:
        return
    if outersize == 0:
        for size in range(2, LIMIT // 4 + 1):
            find_laminae(tilesused + (size * 4), size, uniques)
    else:
        uniques[tilesused] += 1
        newsize = outersize + 2
        find_laminae(tilesused + newsize * 4, newsize, uniques)


distincts = [0] * (LIMIT + 1)
find_laminae(0, 0, distincts)
total = sum(distincts.count(n) for n in range(1, 11))
print(total)

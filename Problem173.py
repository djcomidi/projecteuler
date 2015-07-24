def find_laminae(tilesleft, outersize=0):
    if tilesleft < 0:
        return 0
    if outersize == 0:
        total = 0
        for size in range(2, tilesleft // 4 + 1):
            total += find_laminae(tilesleft - (size * 4), size)
        return total
    else:
        newsize = outersize + 2
        return 1 + find_laminae(tilesleft - newsize * 4, newsize)


result = find_laminae(10 ** 6)
print(result)

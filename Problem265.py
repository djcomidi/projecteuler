def find_rings(n, ring=""):
    if ring == "":
        return find_rings(n, "0" * n)
    if ring[-n:] in ring[:-1]:
        return 0
    if len(ring) == 2 ** n:
        if any(ring[-i:] + ring[:n - i] in ring for i in xrange(n)):
            return 0
        return int(ring, 2)
    total = 0
    for c in "01":
        total += find_rings(n, ring + c)
    return total


print find_rings(5)

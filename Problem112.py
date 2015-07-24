bouncies = set()
n = 100
pct = 99
while 100 * len(bouncies) < pct * n:
    n += 1
    if n // 10 in bouncies:
        bouncies.add(n)
    else:
        s = ''.join(sorted(str(n)))
        if (s != str(n)) and (s[::-1] != str(n)):
            bouncies.add(n)
print n

VALUES = [None,
          list(range(1, 21)) + [25],
          list(range(1, 21)) + [25],
          list(range(1, 21))]

ways = 0
for x1 in range(1, 4):
    for v1 in VALUES[x1]:
        temp1 = x1 * v1
        if x1 == 2 and temp1 < 100:
            ways += 1
        for x2 in range(1, 4):
            for v2 in VALUES[x2]:
                temp12 = temp1 + x2 * v2
                if x2 == 2 and temp12 < 100:
                    ways += 1
                if (x1 > x2) or (x1 == x2 and v1 < v2):
                    continue
                x3 = 2
                for v3 in VALUES[2]:
                    temp123 = temp12 + x3 * v3
                    if temp123 < 100:
                        ways += 1
print(ways)

import sys

from eulertools import polygonal

SIZE = 2500
pentas = [polygonal(5, i) for i in range(1, SIZE + 1)]

for a in range(len(pentas)):
    for b in range(a + 1, len(pentas)):
        if pentas[b] + pentas[a] in pentas and pentas[b] - pentas[a] in pentas:
            difference = pentas[b] - pentas[a]
            print(difference)
            sys.exit(0)

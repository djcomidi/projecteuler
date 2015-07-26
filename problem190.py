from operator import mul
from functools import reduce

from eulertools import polygonal

total = 0
for n in range(2, 16):
    step = (1.0 * n) / polygonal(3, n)
    total += int(reduce(mul, [(step * i) ** i for i in range(1, n + 1)], 1.0))
print(total)

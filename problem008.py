from operator import mul
from functools import reduce

data = ""
with open('problem008_data.txt') as in_file:
    for line in in_file.readlines():
        data += line[:-1]
max_prod, size = 0, 13
for i in range(len(data) - size):
    chain = [int(t) for t in data[i:i + size]]
    max_prod = max(max_prod, reduce(mul, chain, 1))
print(max_prod)

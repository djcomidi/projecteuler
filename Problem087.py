from gmpy2 import next_prime

LIMIT = 5 * 10 ** 7
p2s = []
p3s = []
p4s = []
p = 2
while p ** 2 < LIMIT:
    p2s.append(p ** 2)
    if p ** 3 < LIMIT:
        p3s.append(p ** 3)
    if p ** 4 < LIMIT:
        p4s.append(p ** 4)
    p = next_prime(p)

valids = set()
for p4 in p4s:
    for p3 in p3s:
        for p2 in p2s:
            if p2 + p3 + p4 < LIMIT:
                valids.add(p2 + p3 + p4)
size = len(valids)
print(size)

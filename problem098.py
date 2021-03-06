from gmpy2 import is_square
from itertools import permutations

with open('problem098_words.txt') as in_file:
    data = in_file.read()[1:-1].split('","')
lookup = {}
for word in data:
    key = ''.join(sorted(word))
    if key in lookup:
        lookup[key].append(word)
    else:
        lookup[key] = [word]
anagramPairs = list(v for v in list(lookup.values()) if len(v) == 2)
# let's ignore the one triple ("POST","SPOT","STOP") for now :)

maxSquare = 0
for a, b in anagramPairs:
    key = ''.join(set(a))
    for perm in permutations("0123456789", len(key)):
        trans = str.maketrans(key, ''.join(perm))
        aVal = int(a.translate(trans))
        bVal = int(b.translate(trans))
        if len(str(aVal)) == len(a) and len(str(bVal)) == len(b):
            if is_square(aVal) and is_square(bVal):
                maxSquare = max(maxSquare, max(aVal, bVal))
print(maxSquare)

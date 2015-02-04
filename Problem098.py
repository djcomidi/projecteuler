#!/usr/bin/env python

from EulerTools import is_square
from string import maketrans
from itertools import permutations
from pprint import pprint

data = []
with open('Problem098_words.txt') as in_file:
	data = in_file.read()[1:-1].split('","')
lookup = {}
for word in data:
	key = ''.join(sorted(word))
	if key in lookup:	lookup[key].append(word)
	else:				lookup[key] = [word]
anagramPairs = list( v for v in lookup.values() if len(v) == 2 )
# let's ignore the one triple ("POST","SPOT","STOP") for now :)

maxSquare = 0
for a, b in anagramPairs:
	key = ''.join(set(a))
	for perm in permutations("0123456789",len(key)):
		trans = maketrans(key,''.join(perm))
		aVal = int( a.translate(trans) )
		bVal = int( b.translate(trans) )
		if len(str(aVal)) == len(a) and len(str(bVal)) == len(b):
			if is_square(aVal) and is_square(bVal):
				maxSquare = max(maxSquare,max(aVal,bVal))
print maxSquare

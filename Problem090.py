#!/usr/bin/env python

from EulerTools import is_square
from itertools import combinations

def testdice(facesA,facesB):
	setA, setB = set(facesA), set(facesB)
	if 6 in facesA or 9 in facesA: setA |= set([6,9])
	if 6 in facesB or 9 in facesB: setB |= set([6,9])
	numbers = set()
	for faceA in setA:
		for faceB in setB:
			numbers.add( 10*faceA + faceB )
			numbers.add( 10*faceB + faceA )
	squares = filter( lambda num: num > 0 and is_square(num), numbers )
	return len(squares) == 9

facesList = [ map( int, faces ) for faces in combinations( "0123456789", 6 ) ]
arrangements = 0
for i, facesA in enumerate( facesList ):
	for facesB in facesList[i+1:]:
		if testdice(facesA,facesB):
			arrangements += 1
print arrangements

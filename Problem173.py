#!/usr/bin/env python

def find_laminae(tilesLeft,outerSize=0):
	if tilesLeft < 0: return 0
	if outerSize == 0:
		total = 0
		for size in xrange(2,tilesLeft//4+1):
			total += find_laminae(tilesLeft-(size*4),size)
		return total
	else:
		newSize = outerSize + 2
		return 1 + find_laminae(tilesLeft-newSize*4,newSize)

print find_laminae(10**6)

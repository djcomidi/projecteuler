#!/usr/bin/env python

# L(n)=(t_1,..t_k) =>  n distinct laminae that can be formed using t tiles
# N(n)=len(L(n))

LIMIT = 10**6

def find_laminae(tilesUsed=0,outerSize=0,distincts=[]):
	if tilesUsed > LIMIT: return
	if outerSize == 0:
		for size in xrange(2,LIMIT//4+1):
			find_laminae(tilesUsed+(size*4),size,distincts)
	else:
		distincts[tilesUsed] += 1
		newSize = outerSize + 2
		find_laminae(tilesUsed+newSize*4,newSize,distincts)

distincts = [0]*(LIMIT+1)
find_laminae(0,0,distincts)
print distincts.count(15)
print sum( distincts.count(n) for n in xrange(1,11) )

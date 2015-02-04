#!/usr/bin/env python

setA = [ 11, 18, 20, 22, 25 ]
setB = [ setA[len(setA)//2] ]
for i in xrange(len(setA)):
	setB.append(setB[0]+setA[i])
print ''.join(map(str,setB))

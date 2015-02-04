#!/usr/bin/env python

def triangle_has_origin(pAx,pAy,pBx,pBy,pCx,pCy):
	ab = pAy*(pAx-pBx)+pAx*(pBy-pAy)
	ca = pCy*(pCx-pAx)+pCx*(pAy-pCy)
	bc = pBy*(pBx-pCx)+pBx*(pCy-pBy)
	return (ab*bc>0 and bc*ca>0 and ca*ab>0)

have_origin = 0
with open('Problem102_triangles.txt') as in_file:
	for line in in_file.readlines():
		pAx, pAy, pBx, pBy, pCx, pCy = map( int, line.strip().split(',') )
		if triangle_has_origin(pAx,pAy,pBx,pBy,pCx,pCy):
			have_origin += 1
print have_origin

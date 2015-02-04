#!/usr/bin/env python

DATA = []
with open('Problem011.data') as in_file:
	for line in in_file.readlines():
		DATA.append( map( int, line[:-1].split(' ') ) )
H, W = len(DATA), len(DATA[0])

def get_max_product(r,c):
	prodE, prodSE, prodS, prodSW = 1, 1, 1, 1
	for i in xrange(4):
		if c <= W - 4:			prodE  *= DATA[r][c+i]
		if c <= W - 4 and r <= H - 4:	prodSE *= DATA[r+i][c+i]
		if r <= H - 4:			prodS  *= DATA[r+i][c]
		if r <= H - 4 and c >= 4:	prodSW *= DATA[r+i][c-i]
	return max( prodE, prodSE, prodS, prodSW )

max_product = 0
for r in xrange(H):
	for c in xrange(W):
		max_product = max( max_product, get_max_product(r,c) )
print max_product


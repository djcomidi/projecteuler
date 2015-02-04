#!/usr/bin/env python

pyramid = []
with open('Problem067_triangle.txt') as in_file:
	for row in in_file.readlines():
		pyramid.append( map( int, row[:-1].split(' ') ) )

for r in xrange(len(pyramid)-2,-1,-1):
	for c in xrange(len(pyramid[r])):
		pyramid[r][c] += max( pyramid[r+1][c], pyramid[r+1][c+1] )
print pyramid[0][0]

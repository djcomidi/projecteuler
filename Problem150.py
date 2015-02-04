#!/usr/bin/env python

def LCG():
	t = 0
	for k in xrange(1,500501):
		t = (615949*t + 797807) % 2**20
		yield t - 2**19

lcg = LCG()
triangle = []
for rowcount in xrange(1,1001):
	row = []
	for i in xrange(rowcount):
		row.append( lcg.next() )
	triangle.append( row )

minimum = 273519
for top_row in xrange(10):
	oldmin = minimum
	for top_col in xrange(len(triangle[top_row])):
		temp_min, right_col = 0, top_col
		for row in xrange(top_row,1000):
			right_col = right_col+1
			temp_min += sum(triangle[row][top_col:right_col])
			minimum = min( temp_min, minimum )
	if minimum < oldmin:
		print top_row, minimum
print minimum

		
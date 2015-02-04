#!/usr/bin/env python

from EulerTools import triangle

TARGET = 2*10**6
closest, closest_rows, closest_cols = 0, 0, 0
for rows in xrange(1,100):
	for cols in xrange(rows+1,100):
		rectangles = triangle(rows)*triangle(cols)
		if abs(TARGET-closest) > abs(TARGET-rectangles):
			closest, closest_rows, closest_cols = rectangles, rows, cols

print closest, closest_rows, closest_cols
print closest_rows * closest_cols

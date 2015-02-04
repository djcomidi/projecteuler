#!/usr/bin/env python

from EulerTools import mul

data = ""
with open('Problem008.data','r') as in_file:
	for line in in_file.readlines():
		data += line[:-1]
max_prod = 0
for i in xrange(len(data)-5):
	five_digits = map( int, list(data[i:i+5]) )
	max_prod = max( max_prod, reduce( mul, five_digits, 1 ) )
print max_prod



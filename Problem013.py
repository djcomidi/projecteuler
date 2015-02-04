#!/usr/bin/env python

the_sum = 0
with open('Problem013.data','r') as in_file:
	for line in in_file.readlines():
		the_sum += int(line[:-1])
print str(the_sum)[:10]

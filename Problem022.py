#!/usr/bin/env python

from string import ascii_uppercase

def get_namescore(s):
	return sum( ascii_uppercase.index(c)+1 for c in s )

names = []
with open('Problem022_names.txt','r') as in_file:
	names = in_file.readline()[1:-1].split('","')
names.sort()
totalnamescore = 0
for i in xrange(len(names)):
	totalnamescore += (i+1)*get_namescore(names[i])
print totalnamescore
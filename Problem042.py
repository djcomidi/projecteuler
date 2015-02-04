#!/usr/bin/env python

from string import ascii_uppercase

def is_triangle_word(w):
	return is_triangle( sum( [ ascii_uppercase.index(c)+1 for c in w ] ) )

words = []
with open('Problem042_words.txt','r') as in_file:
	words = in_file.readline()[1:-1].split('","')

count_triangles = 0
for word in words:
	if is_triangle_word(word):
		count_triangles += 1
print count_triangles

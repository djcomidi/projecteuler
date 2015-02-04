#!/usr/bin/env python

from AStar import a_star

matrix = []
with open('Problem083_matrix.txt') as in_file:
	for line in in_file.readlines():
		matrix.append( map( int, line[:-1].split(',') ) )
ROWS, COLS = len(matrix), len(matrix[0])

graph = a_star(matrix)
print graph.shortest_path()
# ~8s

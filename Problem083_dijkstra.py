#!/usr/bin/env python

from Dijkstra import dijkstra

matrix = []
with open('Problem083_matrix.txt') as in_file:
	for line in in_file.readlines():
		matrix.append( map( int, line[:-1].split(',') ) )
ROWS, COLS = len(matrix), len(matrix[0])

graph = dijkstra(matrix)
print graph.shortest_path()
# ~25s

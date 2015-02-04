#!/usr/bin/env python

from Dijkstra import dijkstra

matrix = []
with open('Problem082_matrix.txt') as in_file:
	for line in in_file.readlines():
		matrix.append( map( int, line[:-1].split(',') ) )
ROWS, COLS = len(matrix), len(matrix[0])

graph = dijkstra(matrix)
graph.set_directions(goLeft=False)
startNodes = [ (r,0) for r in xrange(ROWS) ]
endNodes = [ (r,COLS-1) for r in xrange(ROWS) ]
print graph.shortest_path(startNodes,endNodes)
# ~27s

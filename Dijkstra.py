#!/usr/bin/env python

import sys

class dijkstra:
	def __init__(self,data):
		self.data = data
		self.ROWS = len(self.data)
		self.COLS = len(self.data[0])
		self.set_directions()

	def __get_neighbors(self,u):
		r, c = u
		neighbors = []
		if self.goDown and r < self.ROWS - 1: neighbors.append( (r+1,c) )
		if self.goRight and c < self.COLS - 1: neighbors.append( (r,c+1) )
		if self.goLeft and c > 0: neighbors.append( (r,c-1) )
		if self.goUp and r > 0: neighbors.append( (r-1,c) )
		return neighbors

	def __initdata(self,startNodes,endNodes):
		self.distance = {}
		self.previous = {}
		self.Q = []
		for r in xrange(self.ROWS):
			for c in xrange(self.COLS):
				self.Q.append( (r,c) )
				self.distance[(r,c)] = sys.maxint
				self.previous[(r,c)] = None
				if (r,c) in startNodes:
					self.distance[(r,c)] = self.data[r][c]
		self.endNodes = [(self.ROWS-1,self.COLS-1)]
		if endNodes != None:
			self.endNodes = endNodes[:]

	def set_directions(self,goLeft=True,goRight=True,goUp=True,goDown=True):
		self.goLeft = goLeft
		self.goRight = goRight
		self.goUp = goUp
		self.goDown = goDown
		
	def shortest_path(self,startNodes=[(0,0)],endNodes=None):
		self.__initdata(startNodes,endNodes)
		u = (0,0)
		while len(self.Q) > 0:
			minDistance = min( self.distance[q] for q in self.Q )
			u = [ q for q in self.Q if self.distance[q] == minDistance ][0]
			if self.distance[u] == sys.maxint:
				break
			if u in self.endNodes:
				break
			self.Q.remove(u)
			for v in self.__get_neighbors(u):
				newDistance = self.distance[u] + self.data[v[0]][v[1]]
				if newDistance < self.distance[v]:
					self.distance[v] = newDistance
					self.previous[v] = u
		return self.distance[u]
	

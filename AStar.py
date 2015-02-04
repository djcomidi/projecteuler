#!/usr/bin/env python

class a_star:
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

	def __heuristic_cost_estimate(self,nodeFrom, nodeTo):
		return (nodeFrom[0]-nodeTo[0])**2 + (nodeFrom[1]-nodeTo[1])**2

	def __initdata(self,startNodes,endNodes):
		self.startNodes = startNodes
		self.endNodes = [(self.ROWS-1,self.COLS-1)]
		if endNodes != None:
			self.endNodes = endNodes[:]
		self.closed_nodes = []
		self.open_nodes = startNodes[:]
		self.came_from, self.g_score, self.h_score, self.f_score = {}, {}, {}, {}
		for node in self.open_nodes:
			self.g_score[node] = self.data[node[0]][node[1]]
			self.h_score[node] = self.__heuristic_cost_estimate(node,(self.ROWS-1,self.COLS-1))
			self.f_score[node] = self.g_score[node] + self.h_score[node]

	def set_directions(self,goLeft=True,goRight=True,goUp=True,goDown=True):
		self.goLeft = goLeft
		self.goRight = goRight
		self.goUp = goUp
		self.goDown = goDown

	def shortest_path(self,startNodes=[(0,0)],endNodes=None):
		self.__initdata(startNodes,endNodes)
		x = (0,0)
		while len(self.open_nodes) > 0:
			low_f = min( self.f_score[node] for node in self.open_nodes )
			x = [ node for node in self.open_nodes if self.f_score[node] == low_f ][0]
			if x in self.endNodes:
				break
			self.open_nodes.remove(x)
			self.closed_nodes.append(x)
			for y in self.__get_neighbors(x):
				if y in self.closed_nodes: continue
				new_g_score = self.g_score[x] + self.data[y[0]][y[1]]
				new_g_better = False
				if not y in self.open_nodes:
					self.open_nodes.append(y)
					new_g_better = True
				else:
					new_g_better = new_g_score < self.g_score[y]
				if new_g_better:
					self.came_from[y] = x
					self.g_score[y] = new_g_score
					self.h_score[y] = self.__heuristic_cost_estimate(y, (self.ROWS-1,self.COLS-1))
					self.f_score[y] = self.g_score[y] + self.h_score[y]
		minPath = 0
		while not x in self.startNodes:
			minPath += self.data[x[0]][x[1]]
			x = self.came_from[x]
		return self.data[x[0]][x[1]] + minPath

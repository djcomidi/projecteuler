import sys


class Dijkstra:
    def __init__(self, data):
        self.go_down = self.go_left = self.go_right = self.go_up = False
        self.data = data
        self.ROWS = len(self.data)
        self.COLS = len(self.data[0])
        self.set_directions()

    def __get_neighbors(self, u):
        r, c = u
        neighbors = []
        if self.go_down and r < self.ROWS - 1:
            neighbors.append((r + 1, c))
        if self.go_right and c < self.COLS - 1:
            neighbors.append((r, c + 1))
        if self.go_left and c > 0:
            neighbors.append((r, c - 1))
        if self.go_up and r > 0:
            neighbors.append((r - 1, c))
        return neighbors

    def __initdata(self, startnodes, endnodes):
        self.distance = {}
        self.previous = {}
        self.Q = []
        for r in xrange(self.ROWS):
            for c in xrange(self.COLS):
                self.Q.append((r, c))
                self.distance[(r, c)] = sys.maxint
                self.previous[(r, c)] = None
                if (r, c) in startnodes:
                    self.distance[(r, c)] = self.data[r][c]
        self.endNodes = [(self.ROWS - 1, self.COLS - 1)]
        if endnodes:
            self.endNodes = endnodes[:]

    def set_directions(self, left=True, right=True, up=True, down=True):
        self.go_left = left
        self.go_right = right
        self.go_up = up
        self.go_down = down

    def shortest_path(self, startnodes=None, endnodes=None):
        if startnodes is None:
            startnodes = [(0, 0)]
        self.__initdata(startnodes, endnodes)
        u = (0, 0)
        while len(self.Q) > 0:
            mindistance = min(self.distance[q] for q in self.Q)
            u = [q for q in self.Q if self.distance[q] == mindistance][0]
            if self.distance[u] == sys.maxint:
                break
            if u in self.endNodes:
                break
            self.Q.remove(u)
            for v in self.__get_neighbors(u):
                newdistance = self.distance[u] + self.data[v[0]][v[1]]
                if newdistance < self.distance[v]:
                    self.distance[v] = newdistance
                    self.previous[v] = u
        return self.distance[u]

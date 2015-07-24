class AStar:
    def __init__(self, data):
        self.go_left = self.go_down = self.go_right = self.go_up = True
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

    @staticmethod
    def __cost_estimate(node_from, node_to):
        xdist = (node_from[0] - node_to[0]) ** 2
        ydist = (node_from[1] - node_to[1]) ** 2
        return xdist + ydist

    def __initdata(self, startnodes=None, endnodes=None):
        if not startnodes:
            startnodes = [(0, 0)]
        self.startNodes = startnodes[:]
        if not endnodes:
            endnodes = [(self.ROWS - 1, self.COLS - 1)]
        self.endNodes = endnodes[:]
        self.closed_nodes = []
        self.open_nodes = startnodes[:]
        self.came_from = {}
        self.g_score, self.h_score, self.f_score = {}, {}, {}
        for node in self.open_nodes:
            self.g_score[node] = self.data[node[0]][node[1]]
            tonode = (self.ROWS - 1, self.COLS - 1)
            self.h_score[node] = self.__cost_estimate(node, tonode)
            self.f_score[node] = self.g_score[node] + self.h_score[node]

    def set_directions(self, left=True, right=True, up=True, down=True):
        self.go_left = left
        self.go_right = right
        self.go_up = up
        self.go_down = down

    def shortest_path(self, startnodes=None, endnodes=None):
        self.__initdata(startnodes, endnodes)
        x = (0, 0)
        while len(self.open_nodes) > 0:
            low_f = min(self.f_score[node] for node in self.open_nodes)
            x = [nd for nd in self.open_nodes if self.f_score[nd] == low_f][0]
            if x in self.endNodes:
                break
            self.open_nodes.remove(x)
            self.closed_nodes.append(x)
            for y in self.__get_neighbors(x):
                if y in self.closed_nodes:
                    continue
                new_g_score = self.g_score[x] + self.data[y[0]][y[1]]
                if y not in self.open_nodes:
                    self.open_nodes.append(y)
                    new_g_better = True
                else:
                    new_g_better = new_g_score < self.g_score[y]
                if new_g_better:
                    self.came_from[y] = x
                    self.g_score[y] = new_g_score
                    tonode = (self.ROWS - 1, self.COLS - 1)
                    self.h_score[y] = self.__cost_estimate(y, tonode)
                    self.f_score[y] = self.g_score[y] + self.h_score[y]
        minpath = 0
        while x not in self.startNodes:
            minpath += self.data[x[0]][x[1]]
            x = self.came_from[x]
        return self.data[x[0]][x[1]] + minpath

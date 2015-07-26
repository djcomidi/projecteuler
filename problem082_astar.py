from tools.pathfinding import AStar

matrix = []
with open('problem082_matrix.txt') as in_file:
    for line in in_file.readlines():
        matrix.append([int(x) for x in line[:-1].split(",")])
ROWS, COLS = len(matrix), len(matrix[0])

graph = AStar(matrix)
graph.set_directions(left=False)
startNodes = [(r, 0) for r in range(ROWS)]
endNodes = [(r, COLS - 1) for r in range(ROWS)]
shortpath = graph.shortest_path(startNodes, endNodes)
print(shortpath)

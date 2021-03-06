from tools.pathfinding import AStar

matrix = []
with open('problem083_matrix.txt') as in_file:
    for line in in_file.readlines():
        matrix.append([int(x) for x in line[:-1].split(",")])
ROWS, COLS = len(matrix), len(matrix[0])

graph = AStar(matrix)
shortpath = graph.shortest_path()
print(shortpath)

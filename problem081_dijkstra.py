from tools.pathfinding import Dijkstra

matrix = []
with open('problem081_matrix.txt') as in_file:
    for line in in_file.readlines():
        matrix.append([int(x) for x in line[:-1].split(",")])
ROWS, COLS = len(matrix), len(matrix[0])

graph = Dijkstra(matrix)
graph.set_directions(left=False, up=False)
shortpath = graph.shortest_path()
print(shortpath)

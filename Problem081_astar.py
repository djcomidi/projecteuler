from AStar import AStar

matrix = []
with open('Problem081_matrix.txt') as in_file:
    for line in in_file.readlines():
        matrix.append(map(int, line[:-1].split(',')))
ROWS, COLS = len(matrix), len(matrix[0])

graph = AStar(matrix)
graph.set_directions(left=False, up=False)
print graph.shortest_path()

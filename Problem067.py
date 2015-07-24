pyramid = []
with open('Problem067_triangle.txt') as in_file:
    for row in in_file.readlines():
        pyramid.append([int(x) for x in row[:-1].split(" ")])
        # pyramid.append(map(int, row[:-1].split(' ')))

for r in range(len(pyramid) - 2, -1, -1):
    for c in range(len(pyramid[r])):
        pyramid[r][c] += max(pyramid[r + 1][c], pyramid[r + 1][c + 1])
top = pyramid[0][0]
print(top)

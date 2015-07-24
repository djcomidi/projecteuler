triangle = []
with open('Problem018_data.txt') as in_file:
    for line in in_file.readlines():
        triangle.append(map(int, line[:-1].split(' ')))

for r in xrange(len(triangle) - 2, -1, -1):
    for c in xrange(len(triangle[r])):
        triangle[r][c] += max(triangle[r + 1][c], triangle[r + 1][c + 1])
print triangle[0][0]

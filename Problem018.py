triangle = []
with open('Problem018_data.txt') as in_file:
    for line in in_file.readlines():
        triangle.append([int(t, 10) for t in line[:-1].split(' ')])

for r in range(len(triangle) - 2, -1, -1):
    for c in range(len(triangle[r])):
        triangle[r][c] += max(triangle[r + 1][c], triangle[r + 1][c + 1])
top = triangle[0][0]
print(top)

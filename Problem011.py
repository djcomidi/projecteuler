DATA = []
with open('Problem011_data.txt') as in_file:
    for line in in_file.readlines():
        DATA.append([int(t, 10) for t in line[:-1].split(' ')])
H, W = len(DATA), len(DATA[0])


def get_max_product(row, column):
    east, southeast, south, southwest = 1, 1, 1, 1
    for i in range(4):
        if column <= W - 4:
            east *= DATA[row][column + i]
        if column <= W - 4 and row <= H - 4:
            southeast *= DATA[row + i][column + i]
        if row <= H - 4:
            south *= DATA[row + i][column]
        if row <= H - 4 and column >= 4:
            southwest *= DATA[row + i][column - i]
    return max(east, southeast, south, southwest)


max_product = 0
for r in range(H):
    for c in range(W):
        max_product = max(max_product, get_max_product(r, c))
print(max_product)

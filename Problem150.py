def lcg_generator():
    t = 0
    for k in range(1, 500501):
        t = (615949 * t + 797807) % 2 ** 20
        yield t - 2 ** 19


lcg = lcg_generator()
triangle = []
for rowcount in range(1, 1001):
    row = []
    for i in range(rowcount):
        row.append(next(lcg))
    triangle.append(row)

minimum = 273519
for top_row in range(10):
    oldmin = minimum
    for top_col in range(len(triangle[top_row])):
        temp_min, right_col = 0, top_col
        for row in range(top_row, 1000):
            right_col += 1
            temp_min += sum(triangle[row][top_col:right_col])
            minimum = min(temp_min, minimum)
    if minimum < oldmin:
        message = "minimum at row %d = %d" % (top_row, minimum)
        print(message)
print(minimum)

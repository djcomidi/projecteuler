from EulerTools import polygonal

TARGET = 2 * 10 ** 6
closest, closest_rows, closest_cols = 0, 0, 0
for rows in range(1, 100):
    for cols in range(rows + 1, 100):
        rectangles = polygonal(3, rows) * polygonal(3, cols)
        if abs(TARGET - closest) > abs(TARGET - rectangles):
            closest, closest_rows, closest_cols = rectangles, rows, cols

args = (closest, closest_rows, closest_cols)
message = "closest=%d rows=%d cols=%d" % args
print(message)
message = "rows*cols=%d" % (closest_rows * closest_cols)
print(message)

from EulerTools import polygonal

TARGET = 2 * 10 ** 6
closest, closest_rows, closest_cols = 0, 0, 0
for rows in xrange(1, 100):
    for cols in xrange(rows + 1, 100):
        rectangles = polygonal(3, rows) * polygonal(3, cols)
        if abs(TARGET - closest) > abs(TARGET - rectangles):
            closest, closest_rows, closest_cols = rectangles, rows, cols

print closest, closest_rows, closest_cols
print closest_rows * closest_cols

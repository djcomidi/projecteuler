def triangle_has_origin(ax, ay, bx, by, cx, cy):
    ab = ay * (ax - bx) + ax * (by - ay)
    ca = cy * (cx - ax) + cx * (ay - cy)
    bc = by * (bx - cx) + bx * (cy - by)
    return (ab * bc) > 0 and (bc * ca > 0) and (ca * ab > 0)


have_origin = 0
with open('problem102_triangles.txt') as in_file:
    for line in in_file.readlines():
        ax, ay, bx, by, cx, cy = [int(x) for x in line.strip().split(',')]
        if triangle_has_origin(ax, ay, bx, by, cx, cy):
            have_origin += 1
print(have_origin)

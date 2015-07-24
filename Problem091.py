N = 50
right_angles = 0
for p in xrange(1, (N + 1) ** 2):
    py, px = divmod(p, N + 1)
    OP2 = px ** 2 + py ** 2
    for q in xrange(p + 1, (N + 1) ** 2):
        qy, qx = divmod(q, N + 1)
        OQ2, PQ2 = qx ** 2 + qy ** 2, (px - qx) ** 2 + (py - qy) ** 2
        is_right_angled = False
        is_right_angled |= OP2 + OQ2 == PQ2
        is_right_angled |= OP2 + PQ2 == OQ2
        is_right_angled |= OQ2 + PQ2 == OP2
        if is_right_angled:
            right_angles += 1
print right_angles

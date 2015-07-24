from EulerTools import is_square

B = [15, 85, 493]
T = 0
while T < 10 ** 12:
    B.append(7 * B[-1] - 7 * B[-2] + B[-3])
    b = 1 + 8 * B[-1] * (B[-1] - 1)
    if is_square(b):
        T = (int(b ** 0.5) + 1) // 2
print B[-1]

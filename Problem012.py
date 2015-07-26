from EulerTools import sigma
from EulerTools import polygonal

t = 1
while sigma(0, polygonal(3, t)) < 500:
    t += 1
polygon = polygonal(3, t)
print(polygon)

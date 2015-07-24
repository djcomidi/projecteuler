from EulerTools import number_of_divisors
from EulerTools import polygonal

t = 1
while number_of_divisors(polygonal(3, t)) < 500:
    t += 1
polygon = polygonal(3, t)
print(polygon)

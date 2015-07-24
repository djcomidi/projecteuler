from EulerTools import bincoef
from EulerTools import next_prime

numbers = set()
for n in xrange(50):
    for i in xrange(n + 1):
        numbers.add(bincoef(n, i))
maxnum = max(numbers)

p = 2
while p * p < max(numbers):
    numbers = filter(lambda x: x % (p * p) != 0, numbers)
    p = next_prime(p)
print sum(numbers)

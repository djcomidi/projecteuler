from gmpy2 import bincoef
from gmpy2 import next_prime

numbers = set()
for n in range(50):
    for i in range(n + 1):
        numbers.add(bincoef(n, i))
maxnum = max(numbers)

p = 2
while p * p < max(numbers):
    numbers = [x for x in numbers if x % (p * p) != 0]
    p = next_prime(p)
total = sum(numbers)
print(total)

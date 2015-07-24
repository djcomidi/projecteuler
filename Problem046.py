from gmpy2 import is_prime
from gmpy2 import is_square
from gmpy2 import next_prime


def matches_criteria(num):
    if is_prime(num):
        return True
    p, has_criteria = 2, False
    while p < num and not has_criteria:
        has_criteria = is_square((num - p) // 2)
        p = next_prime(p)
    return has_criteria


n = 35
while matches_criteria(n):
    n += 2
print(n)

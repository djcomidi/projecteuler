from EulerTools import aliquot_sum

LIMIT = 28123
abundants = set(n for n in range(1, LIMIT + 1) if aliquot_sum(n) > n)


def is_abundant_sum(n):
    return any(n - a in abundants for a in abundants)


total = sum(n for n in range(1, LIMIT + 1) if not is_abundant_sum(n))
print(total)

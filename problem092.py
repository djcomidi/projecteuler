key_endings = {'1': 1, '89': 89}


def sum_square_digits(n):
    return sum(int(c) ** 2 for c in str(n))


def find_ending(n):
    key = ''.join(sorted(str(n).replace('0', '')))
    if key not in key_endings:
        key_endings[key] = find_ending(sum_square_digits(n))
    return key_endings[key]


count = 0
for n in range(1, 10 ** 7):
    if find_ending(n) == 89:
        count += 1
print(count)

from EulerTools import Memoize


@Memoize
def find_number(digits_to_do, last_digit=0, max_allowed=10):
    if digits_to_do == 0:
        return 1
    if digits_to_do == 19 and last_digit == 0:
        return 0
    total = 0
    for d in range(max_allowed):
        total += find_number(digits_to_do - 1, d, 10 - last_digit - d)
    return total


result = find_number(20)
print(result)

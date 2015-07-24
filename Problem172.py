from EulerTools import Memoize


@Memoize
def find_numbers(length, arr=None):
    if length == 0:
        return 1
    arr = list(arr) if arr else [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    if arr[0] == 2 and sum(arr) == 29:
        return 0
    valids = 0
    for i in range(10):
        if arr[i] == 0:
            continue
        arr[i] -= 1
        valids += find_numbers(length - 1, tuple(arr))
        arr[i] += 1
    return valids


result = find_numbers(18)
print(result)

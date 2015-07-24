from EulerTools import Memoize


@Memoize
def find_numbers(length, arr=None):
    if length == 0:
        return 1
    if arr is None:
        arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    if arr[0] == 2 and sum(arr) == 29:
        return 0
    valids = 0
    for i in xrange(10):
        arr[i] -= 1
        valids += find_numbers(length - 1, arr)
        arr[i] += 1
    return valids


print find_numbers(18)

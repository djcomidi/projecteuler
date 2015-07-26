from functools import lru_cache


@lru_cache(maxsize=1048576)
def find_numbers(length, arr=(3, 3, 3, 3, 3, 3, 3, 3, 3, 3)):
    if length == 0:
        return 1
    t = list(arr)
    if t[0] == 2 and sum(t) == 29:
        return 0
    valids = 0
    for i in range(10):
        if t[i] == 0:
            continue
        t[i] -= 1
        valids += find_numbers(length - 1, tuple(t))
        t[i] += 1
    return valids


result = find_numbers(18)
print(result)

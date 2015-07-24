from EulerTools import Memoize


@Memoize
def backtrack(daysleft, lcount=0, acount=0):
    if lcount == 2:
        return 0
    if acount == 3:
        return 0
    if daysleft == 0:
        return 1
    total = 0
    total += backtrack(daysleft - 1, lcount, 0)  # add 'O'
    total += backtrack(daysleft - 1, lcount + 1, 0)  # add 'L'
    total += backtrack(daysleft - 1, lcount, acount + 1)  # add 'A'
    return total


print backtrack(30)

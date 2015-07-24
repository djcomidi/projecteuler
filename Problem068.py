from itertools import permutations
#      [0]
#         \      [3]
#        [1]      /
#       /    \  /
#    [8]      [2]
#   /  \      /
# [9]  [6]-[4]-[5]
#        \
#        [7]

maxsol = 0
for perm in permutations("0123456789"):
    arr = map(lambda d: int(d) + 1, perm)
    if arr[0] > 6:
        break
    if arr[0] != min([arr[0], arr[3], arr[5], arr[7], arr[9]]):
        continue
    if arr[0] + arr[1] + arr[2] != arr[2] + arr[3] + arr[4]:
        continue
    if arr[0] + arr[1] + arr[2] != arr[4] + arr[5] + arr[6]:
        continue
    if arr[0] + arr[1] + arr[2] != arr[6] + arr[7] + arr[8]:
        continue
    if arr[0] + arr[1] + arr[2] != arr[1] + arr[8] + arr[9]:
        continue
    arrSol = [arr[0], arr[1], arr[2], arr[3], arr[2], arr[4],
              arr[5], arr[4], arr[6], arr[7], arr[6], arr[8],
              arr[9], arr[8], arr[1]]
    solStr = ''.join(map(str, arrSol))
    solVal = int(solStr)
    if len(solStr) == 16:
        maxsol = max(maxsol, solVal)
print maxsol

from itertools import combinations_with_replacement
from functools import reduce
from operator import mul

# reqn = required number
# before the reqns there are 13 possibilities
# after each first occurrence of a reqn,
# the number of possiblities increases

# when p[0] == 13, it means that the first number is not a reqn
# so the reqns can be exchanged anyhow, thus 6 combinations
# else we have to eliminate that 0 might be the starting number,
# thus only 4 combinations of reqns are valid

# for length 3 there are only 4 possible combinations
# (can't start with a 0)
total = 4
# m is the number places that are not first occurences of required numbers
for m in range(1, 14):
    for p in combinations_with_replacement([13, 14, 15, 16], m):
        t = 6 if p[0] == 13 else 4
        total += reduce(mul, p, t)
result = hex(total)[2:].upper()
print(result)

from itertools import combinations
from itertools import permutations
from itertools import product
from string import maketrans


def eval_rpn(rpn):
    stack = []
    for c in rpn:
        if c in "123456789":
            stack.append(c + ".0")
        else:
            newval = "(" + str(stack[-2]) + c + str(stack[-1]) + ")"
            stack = stack[:-2] + [newval]
    try:
        rpnvalue = eval(stack[0])
        if 0 < rpnvalue == int(rpnvalue):
            return int(rpnvalue)
        else:
            return -1
    except ZeroDivisionError or IndexError:
        return -1


TEMPLATES = ["abXcYdZ", "abXcdYZ", "abcXdYZ", "abcdXYZ", "abcXYdZ"]
RPNS = {}

for keyList in combinations("123456789", 4):
    key = ''.join(keyList)
    for numbers in permutations(keyList):
        for ops in product("+-*/", repeat=3):
            symbols = ''.join(numbers) + ''.join(ops)
            trans = maketrans("abcdXYZ", symbols)
            for template in TEMPLATES:
                rpn = template.translate(trans)
                if key in RPNS:
                    RPNS[key].append(rpn)
                else:
                    RPNS[key] = [rpn]

maxSeq, maxSeqKey = 0, ""
for key, rpns in RPNS.items():
    evals = set(eval_rpn(rpn) for rpn in rpns)
    n = 0
    while n + 1 in evals:
        n += 1
    if n > maxSeq:
        maxSeq, maxSeqKey = n, key

print maxSeq, maxSeqKey

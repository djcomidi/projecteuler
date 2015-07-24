precedes = [[False for c in xrange(10)] for r in xrange(10)]
digits = set()
with open('Problem079_keylog.txt') as in_file:
    for line in in_file.readlines():
        keys = map(int, list(line[:-1]))
        precedes[keys[0]][keys[1]] = True
        precedes[keys[0]][keys[2]] = True
        precedes[keys[1]][keys[2]] = True
        digits |= set(keys)

summary = [(precedes[d].count(True), d) for d in digits]
summary.sort(reverse=True)
sol = ''.join(str(s[1]) for s in summary)
print sol

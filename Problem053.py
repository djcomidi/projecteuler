from EulerTools import bincoef

count_greater = 0
for n in xrange(1, 101):
    for r in xrange(n):
        if bincoef(n, r) > 10 ** 6:
            count_greater += 1
print count_greater

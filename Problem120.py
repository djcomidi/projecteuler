# when printing (a, rmax) during brute-force, I noticed:
# if a == odd: rmax = a*(a-1)
# if a == even: rmax = a*(a-2)
print sum(a * (a - 2 + (a & 1)) for a in xrange(3, 1001))

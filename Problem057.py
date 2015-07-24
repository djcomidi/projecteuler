nom, denom = 3, 2
count_fracs = 0
for i in xrange(1000):
    if len(str(nom)) > len(str(denom)):
        count_fracs += 1
    nom, denom = 2 * denom + nom, denom + nom
print count_fracs

from EulerTools import gcd

TARGET = 3.0 / 7
closest_ratio = 0.0
closest_frac = (1, 1)

for denom in xrange(2, 10 ** 6):
    if denom == 7:
        continue
    nom = (3 * denom) / 7
    ratio = (1.0 * nom) / denom
    if gcd(nom, denom) == 1:
        if closest_ratio < ratio < TARGET:
            closest_ratio, closest_frac = ratio, (nom, denom)
print "%d/%d = %f" % (closest_frac[0], closest_frac[1], closest_ratio)

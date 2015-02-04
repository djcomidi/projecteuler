#!/usr/bin/env python

from EulerTools import mul

fracs = []
for nom in xrange(11,100):
	if nom % 10 == 0: continue
	nomT, nomD = divmod(nom,10)
	for denom in xrange(nom+1,100):
		if denom % 10 == 0: continue
		denomT, denomD = divmod(denom,10);
		if denomD == nomD and nom * denomT == denom * nomT:
			fracs.append((nomT,denomT))
		if denomT == nomD and nom * denomD == denom * nomT:
			fracs.append((nomT,denomD))
		if denomD == nomT and nom * denomT == denom * nomD:
			fracs.append((nomD,denomT))
		if denomT == nomT and nom * denomD == denom * nomD:
			fracs.append((nomD,denomD))
print reduce( mul, [f[1] for f in fracs], 1 ) // reduce( mul, [f[0] for f in fracs], 1 )

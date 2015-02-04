#!/usr/bin/env python

from itertools import permutations
from EulerTools import Memoize

def get_mask_count(mask):
	val, t = 1, 13
	for c in mask:
		if c in "01A": t += 1
		else: val *= t
	return val

@Memoize
def findperms(mask="",requireds=set("01A")):
	if len(mask) > 16: return 0
	if mask == "0": return 0
	perms = 0
	if all( c in mask for c in "01A" ):
		perms += get_mask_count(mask)
	for c in set(".") | requireds:
		perms += findperms(mask+c,requireds-set(c))
	return perms

val = findperms()
print hex(val)[2:].upper()
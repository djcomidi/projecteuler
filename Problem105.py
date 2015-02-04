#!/usr/bin/env python

def get_subsets(arr):
	subsets = []
	for i in xrange(1,2**len(arr)):
		subsets.append( set( arr[j] for j in xrange(len(arr)) if i&(2**j) > 0 ) )
	return subsets

def is_special_set(arr):
	subsets = get_subsets(arr)
	subsets.sort(key=len)
	for iB, subsetB in enumerate(subsets):
		sumB, lenB = sum(subsetB), len(subsetB)
		for subsetC in subsets[:iB]:
			sumC, lenC = sum(subsetC), len(subsetC)
			if not subsetB.isdisjoint(subsetC): continue
			if sumB == sumC: return False
			if lenB > lenC and sumB <= sumC: return False
	return True

sumspecials = 0
with open('Problem105_sets.txt') as in_file:
	for line in in_file.readlines():
		arr = map( int, line.strip().split(',') )
		if is_special_set(arr):
			sumspecials += sum(arr)
print sumspecials

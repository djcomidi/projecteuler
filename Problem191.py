#!/usr/bin/env python

from EulerTools import Memoize

@Memoize
def backtrack(daysLeft,countL=0,countA=0):
	if countL == 2: return 0
	if countA == 3: return 0
	if daysLeft == 0: return 1
	total = 0
	total += backtrack(daysLeft-1,countL,0) # add 'O'
	total += backtrack(daysLeft-1,countL+1,0) # add 'L'
	total += backtrack(daysLeft-1,countL,countA+1) # add 'A'
	return total

print backtrack(30)

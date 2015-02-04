#!/usr/bin/env python

from string import maketrans
from time import time

NUMBERS = "123456789"
RPN_TEMPLATES = [ "abXcYdZ", "abXcdYZ", "abcXdYZ", "abcdXYZ", "abcXYdZ" ]
RPNS = {}

def eval_rpn(rpn):
	stack = []
	for c in rpn:
		if c in NUMBERS:
			stack.append( float(c) )
		else:
			if len(stack) < 2: return -1
			if c == '/' and stack[-1] == 0.0: return -1
			stack = stack[:-2] + [ eval( str(stack[-2]) + c + str(stack[-1]) ) ]
	if 0 < stack[0] == int(stack[0]):
		return int(stack[0])
	return -1

def generate_rpn(symbols=""):
	global RPNS
	if len(symbols) == 7:
		key = ''.join(sorted(symbols[:4]))
		if not key in RPNS: RPNS[key] = []
		for rpntemplate in RPN_TEMPLATES:
			rpn = rpntemplate.translate(maketrans("abcdXYZ",symbols))
			if key in RPNS:	RPNS[key].append( rpn )
			else:			RPNS[key] = [rpn]
	else:
		if len(symbols) < 4:
			for c in set(NUMBERS)-set(symbols):
				generate_rpn(symbols+c)
		elif len(symbols) < 7:
			for op in "+-*/":
				generate_rpn(symbols+op)

print "generating rpns..."
generate_rpn()
print "calculating solution..."
max_consec = 0
max_abcd = 0
for key, rpns in RPNS.items():
	rpnvals = set([ eval_rpn(rpn) for rpn in rpns ])
	highest = 0
	while highest+1 in rpnvals:
		highest += 1
	if highest > max_consec:
		max_consec, max_abcd = highest, key
print max_abcd, max_consec
# ~1m30
